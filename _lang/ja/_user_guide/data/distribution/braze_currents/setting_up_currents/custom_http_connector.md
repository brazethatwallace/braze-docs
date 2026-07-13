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

BrazeでカスタムCurrentsコネクターを統合するには、エンドポイントURLと[オプションの認証トークン](#authentication)を提供する必要があります。

また、Brazeに複数のアプリグループがある場合は、各グループに対してカスタムCurrentsコネクターを設定する必要があります。ただし、すべてのアプリグループを同じエンドポイント、または`your_app_group_key="Brand A"`のような追加の`GET`パラメーターを持つエンドポイントに向けることができます。

## 統合 {#integration}

### ステップ1:エンドポイントを設定する {#step-1-set-up-your-endpoint}

この統合を設定するには、エンドポイントURLが必要です。エンドポイントはHTTP POSTリクエストを受信し、イベントの正常な受信を確認するために`2XX`ステータスコードを返す必要があります。Brazeからのリクエストを認証する場合は、ベアラートークンも必要です。

### ステップ2:Braze Currentsを設定する {#step-2-configure-braze-currents}

Brazeで、**パートナー連携** > **データのエクスポート**に移動し、**新しいCurrentを作成**をクリックして、**カスタムCurrentsエクスポート**を選択します。

エクスポートに名前と連絡先メールアドレスを入力し、**Currentの詳細**ページに進みます。このページで、エンドポイントURLとオプションのベアラートークンを入力します。

認証情報を設定したら、エクスポートしたいすべてのメッセージエンゲージメント、顧客行動、およびユーザーイベントにチェックを入れ、**Currentを起動**をクリックします。

## サポートされているCurrentsイベント {#supported-currents-events}

Brazeは、カスタムHTTPコネクターへの以下のデータのエクスポートをサポートしています。

- [メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events?tab=custom%20http%20connector)
- [顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events?tab=custom%20http%20connector)

各イベントのペイロード構造については、イベント用語集の**Custom HTTP Connector**タブを選択してください。

## データ損失の防止 {#preventing-data-loss}

### エラー監視 {#error-monitoring}

データ損失やサービス中断を避けるために、エンドポイントを常に監視し、エラーやダウンタイムに迅速に対処することが不可欠です。

ほとんどのエラータイプ（サーバーエラーやネットワーク接続エラーなど）に対して、Brazeはイベント送信を積極的にリトライします。問題が5日以上続く場合、統合は自動的に無効化されます。新しい受信イベントはドロップされ、永久に失われます。

### 変更への耐性 {#change-resilience}

Braze Currentsのスキーマに対して、非破壊的な変更を行うことがあります。非破壊的な変更とは、新しいnull許容カラムやイベントタイプの追加です。

通常、これらの変更については2週間前に通知しますが、それが不可能な場合もあります。認識されないフィールドやイベントタイプを処理できるように統合を設計することが不可欠です。そうしないと、データ損失につながる可能性があります。

{% alert tip %}
Currentsイベントスキーマの完全なリストについては、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)と[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)を参照してください。
{% endalert %}

## バッチ処理とシリアライゼーション {#batching-and-serialization}

ターゲットデータ形式はHTTPS経由のJSONです。デフォルトでは、イベントは最大100件のバッチでエンドポイントに送信されます。

イベントは、以下の形式ですべてのイベントのJSON配列としてエンドポイントに送信されます。

```json
{"events": [event1, event2, event3, etc...]}
```

キー`"events"`を持つトップレベルのJSONオブジェクトがあり、それぞれが単一のイベントを表すJSONオブジェクトの配列にマッピングされます。各イベントには2つのサブオブジェクトが含まれます。

| 名前 | 説明 |
|----|-----------|
| `"user"` | `user_id`、`external_user_id`、`device_id`、`timezone`などのユーザープロパティを含みます。|
| `"properties"` | 適用される`app/campaign/canvas/platform`など、イベントの属性を含みます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ダウンストリームエンドポイントがイベントゼロのペイロードまたは空のリクエストボディを受信した場合、結果はno-op（操作なし）と見なされるべきであり、この呼び出しからダウンストリームへの影響は発生しないことを意味します。ただし、（通常のAPI呼び出しと同様に）`Authorization`ヘッダーを確認し、[無効な認証情報](#authentication)に対して`401`や`403`などの適切なHTTPレスポンスを返す必要があります。これにより、Brazeはコネクターの認証情報が有効であることを確認できます。

## 認証 {#authentication}

ペイロード内の認証トークンはオプションです。[RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1)で規定されている`Bearer`認可スキームを使用して、HTTP `Authorization`ヘッダーを通じて渡すことができます。オプションですが、認証トークンが渡された場合、ペイロードにイベントがない場合でも、Brazeは常に最初にそれを検証します。

RFC 6750に従い、トークンは少なくとも1文字のBase64エンコードされた値である必要があります。RFC 6750では、通常のBase64文字に加えて、`-`、`.`、`_`、`~`の文字をトークンに含めることが許可されています。これらの文字をトークンに含めるかどうかは選択できますが、Base64形式である必要があります。

また、`Authorization`ヘッダーが存在する場合、以下の形式で構成されます。

```plaintext
"Authorization: Bearer " + <token>
```

例えば、認証トークンが`0p3n5354m3==`の場合、`Authorization`ヘッダーは以下のようになります。

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
将来的に、Brazeに固有のカスタムキーバリューペア認可スキームを実装するために`Authorization`ヘッダーを使用する可能性があります。これは[RFC 7235](https://tools.ietf.org/html/rfc7235)仕様に準拠するもので、Amazon Web Services（AWS）などの企業が認証スキームを実装する方法と同様です。
{% endalert %}

## バージョニング {#versioning}

HTTPコネクター統合からのすべてのリクエストは、Currentsリクエストのバージョンを示すカスタムヘッダーとともに送信されます。

```plaintext
Braze-Currents-Version: 1
```

バージョンは常に`1`であり、この番号を頻繁にインクリメントすることは想定していません。

[データウェアハウスストレージスキーマ]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1)と同様に、個々のイベント内のすべてのイベントフィールドは、[Apache Avro](https://avro.apache.org/)の後方互換性の定義に従い、以前のイベントペイロードバージョンとの後方互換性が保証されています。

1. 特定のイベントフィールドは、常に同じデータ型を持つことが保証されています。
2. ペイロードに追加される新しいフィールドは、すべての関係者によってオプションと見なされる必要があります。
3. 必須フィールドが削除されることはありません。

## エラー処理とリトライメカニズム {#error-handling-and-retry-mechanism}

エラーが発生した場合、Brazeは受信したHTTPリターンコードに基づいてリクエストをキューに入れ、リトライします。問題が5日以上続く場合、統合は自動的に無効化されます。新しい受信イベントはドロップされ永久に失われ、すでにキューに入っているイベントは7日間保持された後に永久にドロップされます。データが24時間以上滞留している場合、オンコールエンジニアに自動的にアラートが送信されます。各ステータスコードの処理方法の詳細については、以下のセクションの表を参照してください。

Currents統合が認証エラーを返している場合、Brazeは自動的に通知メールを送信します。

以下のセクションにリストされていないHTTPエラーコードは、HTTP `5XX`エラーとして扱われます。

{% alert warning %}
問題が5日以上続く場合、統合は無効化されます。新しい受信イベントはドロップされ永久に失われ、すでにキューに入っているイベントは7日間保持された後に永久にドロップされます。
{% endalert %}

以下のHTTPステータスコードがコネクタークライアントによって認識されます。

<table aria-label="エラー処理とリトライメカニズム">
  <thead>
    <tr>
      <th>ステータスコード</th>
      <th>応答</th>
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
      <td>イベントデータはジッター付きのエクスポネンシャルバックオフパターンで再送信されます。問題が5日以上続く場合、統合は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>クライアント側エラー</td>
      <td>コネクターが少なくとも1つの不正なイベントを送信しました。イベントデータはサイズ1のバッチに分割されて再送信されます。これらのサイズ1のバッチで再度<code>400</code>レスポンスを受信したイベントは永久にドロップされます。</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>未認証</td>
      <td>コネクターが無効な認証情報で設定されています。失敗したイベントは再送信されません。認証情報を修正し、統合を再度有効にして再開してください。問題が5日以上続く場合、統合は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>禁止</td>
      <td>コネクターが無効な認証情報で設定されています。失敗したイベントは再送信されません。認証情報を修正し、統合を再度有効にして再開してください。問題が5日以上続く場合、統合は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>見つかりません</td>
      <td>コネクターが不正なエンドポイントURLまたは無効な認証情報で設定されています。エンドポイントURLが正しく、到達可能であることを確認してください。設定を修正し、統合を再度有効にして再開してください。問題が5日以上続く場合、統合は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>ペイロードが大きすぎます</td>
      <td>イベントデータはより小さなバッチに分割されて再送信されます。</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>リクエストが多すぎます</td>
      <td>レート制限を示します。イベントデータはジッター付きのエクスポネンシャルバックオフパターンで再送信されます。問題が5日以上続く場合、統合は無効化され、すでにキューに入っているイベントは7日間保持されます。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }