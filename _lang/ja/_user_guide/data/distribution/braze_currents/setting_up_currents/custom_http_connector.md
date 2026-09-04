---
nav_title: カスタムCurrentsエクスポート
article_title: カスタムCurrentsエクスポート
alias: /currents/custom_http_connector/
page_order: 3
page_type: reference
tool: Currents
description: "このリファレンス記事では、カスタムCurrentsエクスポートを設定して、Braze Currentsのイベントデータを独自のHTTPエンドポイントにリアルタイムでストリーミングする方法について説明します。"
---

# カスタムCurrentsエクスポート {#custom-currents-export}

> カスタムCurrentsコネクターを統合して、Brazeからリアルタイムでイベントデータを取得し、よりカスタマイズされた分析、レポート、オートメーションを実現する方法を説明します。

{% alert note %}
この機能は、技術ドキュメントやAPIリファレンスではカスタムHTTPコネクターとも呼ばれています。
{% endalert %}

## 前提条件 {#prerequisites}

Brazeでカスタム Currents コネクターを連携するには、エンドポイントURLと[オプションの認証トークン](#authentication)を提供する必要があります。

また、Brazeに複数のアプリグループがある場合は、グループごとにカスタム Currents コネクターを設定する必要があります。ただし、すべてのアプリグループを同じエンドポイント、または `your_app_group_key="Brand A"` のような追加の `GET` パラメーターを持つエンドポイントに向けることができます。

## 連携 {#integration}

### ステップ1：エンドポイントを設定する {#step-1-set-up-your-endpoint}

この連携を設定するには、エンドポイントURLが必要です。エンドポイントはHTTP POSTリクエストを受信でき、イベントの受信が成功したことを示す`2XX`ステータスコードを返す必要があります。Brazeからのリクエストを認証する場合は、ベアラートークンも必要です。

### ステップ2：Braze Currentsを設定する {#step-2-configure-braze-currents}

Brazeで**パートナー連携** > **データエクスポート**に移動し、**新しいCurrentを作成**をクリックして、**カスタムCurrentsエクスポート**を選択します。

エクスポートに名前と連絡先メールアドレスを入力し、**Currentの詳細**ページに進みます。このページで、エンドポイントURLとオプションのベアラートークンを入力します。

認証情報を設定したら、エクスポートしたいメッセージエンゲージメント、顧客行動、およびユーザーイベントをすべてチェックし、**Currentを起動**をクリックします。

## サポートされているCurrentsイベント {#supported-currents-events}

Brazeは、カスタムHTTPコネクターに以下のデータをエクスポートすることをサポートしています。

- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events?tab=custom%20http%20connector)
- [顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events?tab=custom%20http%20connector)

各イベントのペイロード構造については、イベント用語集の**カスタムHTTPコネクター**タブを選択してください。

## データ損失の防止 {#preventing-data-loss}

### エラー監視 {#error-monitoring}

データ損失やサービス中断を防ぐために、エンドポイントを常に監視し、エラーやダウンタイムが発生した場合は速やかに対処することが不可欠です。

ほとんどのエラータイプ（サーバーエラーやネットワーク接続エラーなど）に対して、Brazeはイベント送信を自動的にリトライします。問題が5日以上続く場合、連携は自動的に無効化されます。新しい受信イベントはドロップされ、永久に失われます。

### 変更への耐性 {#change-resilience}

Braze Currentsのスキーマに対して、破壊的でない変更を行う場合があります。破壊的でない変更とは、新しいnullable列やイベントタイプの追加です。

通常、これらの変更については2週間前に通知しますが、それが難しい場合もあります。認識できないフィールドやイベントタイプを適切に処理できるよう連携を設計することが不可欠です。そうしないと、データ損失につながる可能性があります。

{% alert tip %}
Currentsのイベントスキーマの完全なリストについては、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)と[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)を参照してください。
{% endalert %}

## バッチ処理とシリアライゼーション {#batching-and-serialization}

ターゲットデータ形式はHTTPS経由のJSONです。デフォルトでは、イベントは最大100件ずつのバッチでエンドポイントに送信されます。

イベントは、以下の形式ですべてのイベントのJSON配列としてエンドポイントに送信されます。

```json
{"events": [event1, event2, event3, etc...]}
```

`"events"`というキーを持つトップレベルのJSONオブジェクトがあり、これはさらなるJSONオブジェクトの配列にマッピングされます。各JSONオブジェクトは単一のイベントを表します。各イベントには2つのサブオブジェクトが含まれます。

|名前|説明|
|----|-----------|
|`"user"`| `user_id`、`external_user_id`、`device_id`、`timezone`などのユーザープロパティを含みます。|
|`"properties"`|適用される`app/campaign/canvas/platform`など、イベントの属性を含みます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ダウンストリームエンドポイントがイベント数がゼロのペイロードまたは空のリクエストボディを受信した場合、その結果はノーオペレーション（no-op）とみなされるべきです。つまり、この呼び出しによってダウンストリームへの影響は発生しないということです。ただし、（通常のAPI呼び出しと同様に）`Authorization`ヘッダーを確認し、`401`や`403`など、[無効な認証情報](#authentication)に対して適切なHTTPレスポンスを返す必要があります。これにより、Brazeはコネクターの認証情報が有効であることを確認できます。

## 認証 {#authentication}

ペイロード内の認証トークンはオプションです。[RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1) に規定されている `Bearer` 認可スキームを使用して、HTTP `Authorization` ヘッダーを通じて渡すことができます。オプションではありますが、認証トークンが渡された場合、Brazeはペイロードにイベントが含まれていなくても、常にまずそのトークンを検証します。

RFC 6750 に基づき、トークンは1文字以上のBase64エンコード値である必要があります。RFC 6750 では、通常のBase64文字に加えて `-`、`.`、`_`、`~` の文字もトークンに含めることができます。これらの文字をトークンに含めるかどうかは自由に選択できます&#8212;ただし、Base64形式である必要があります。

また、`Authorization` ヘッダーが存在する場合、以下の形式で構成されます。

```plaintext
"Authorization: Bearer " + <token>
```

たとえば、認証トークンが `0p3n5354m3==` の場合、`Authorization` ヘッダーは以下のようになります。

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
将来的に、`Authorization` ヘッダーを使用して、Braze独自のカスタムキーバリューペア認可スキームを実装する可能性があります。これは [RFC 7235](https://tools.ietf.org/html/rfc7235) 仕様に準拠するもので、Amazon Web Services（AWS）などの企業が認証スキームを実装する際に使用している方法と同様です。
{% endalert %}

## バージョニング {#versioning}

HTTP コネクター連携からのすべてのリクエストは、Currents リクエストのバージョンを示すカスタムヘッダーとともに送信されます。

```plaintext
Braze-Currents-Version: 1
```

バージョンは常に `1` です。この番号を増やすことはほとんど、あるいはまったくないと想定しています。

[データウェアハウスストレージスキーマ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics?redirected=1)と同様に、個々のイベント内のすべてのイベントフィールドは、[Apache Avro](https://avro.apache.org/) の後方互換性の定義に従い、以前のイベントペイロードバージョンとの後方互換性が保証されています。

1. 特定のイベントフィールドは、常に同じデータ型を維持することが保証されています。
2. ペイロードに追加される新しいフィールドは、すべての関係者によってオプションとみなされる必要があります。
3. 必須フィールドが削除されることはありません。

## エラーハンドリングとリトライメカニズム {#error-handling-and-retry-mechanism}

エラーが発生した場合、Brazeは受信したHTTPリターンコードに基づいてリクエストをキューに入れ、リトライします。問題が5日以上続くと、連携は自動的に無効化されます。新しい受信イベントはドロップされ、永久に失われます。すでにキューに入っているイベントは7日間保持された後、永久にドロップされます。データが24時間以上停滞している場合、オンコールエンジニアに自動的にアラートが送信されます。各ステータスコードの処理方法の詳細については、次のセクションの表を参照してください。

Currents連携が認証エラーを返している場合、Brazeは自動的に通知メールを送信します。

次のセクションに記載されていないHTTPエラーコードは、HTTP `5XX` エラーとして扱われます。

{% alert warning %}
問題が5日以上続くと、連携は無効化されます。新しい受信イベントはドロップされ、永久に失われます。すでにキューに入っているイベントは7日間保持された後、永久にドロップされます。
{% endalert %}

以下のHTTPステータスコードがコネクタークライアントによって認識されます。

<table aria-label="エラーハンドリングとリトライメカニズム">
  <thead>
    <tr>
      <th>ステータスコード</th>
      <th>レスポンス</th>
      <th>説明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>成功</td>
      <td>イベントデータは再送信されません。</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>サーバー側エラー</td>
      <td>イベントデータはジッター付きの指数バックオフパターンで再送信されます。問題が5日以上続くと、連携は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>クライアント側エラー</td>
      <td>コネクターが不正なイベントを少なくとも1つ送信しました。イベントデータはサイズ1のバッチに分割されて再送信されます。これらのサイズ1のバッチで再度 <code>400</code> レスポンスを受信したイベントは永久にドロップされます。</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>未認証</td>
      <td>コネクターが無効な認証情報で設定されていました。失敗したイベントは再送信されません。認証情報を修正し、連携を再度有効化して再開してください。問題が5日以上続くと、連携は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>アクセス禁止</td>
      <td>コネクターが無効な認証情報で設定されていました。失敗したイベントは再送信されません。認証情報を修正し、連携を再度有効化して再開してください。問題が5日以上続くと、連携は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>見つかりません</td>
      <td>コネクターが不正なエンドポイントURLまたは無効な認証情報で設定されていました。エンドポイントURLが正しく、到達可能であることを確認してください。設定を修正し、連携を再度有効化して再開してください。問題が5日以上続くと、連携は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>ペイロードが大きすぎます</td>
      <td>イベントデータはより小さなバッチに分割されて再送信されます。</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>リクエスト過多</td>
      <td>レート制限を示しています。イベントデータはジッター付きの指数バックオフパターンで再送信されます。問題が5日以上続くと、連携は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }