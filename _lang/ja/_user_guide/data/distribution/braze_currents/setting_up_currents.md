---
nav_title: Currentsを設定する
article_title: Currentsの設定
page_order: 1
page_type: tutorial
description: "このハウツー記事では、Braze Currentsの連携と設定を行うプロセスを順に説明します。"
tool: Currents
search_rank: 8
---

# [![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Currentsの設定 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcurrents-the-basics-2-stylefloatrightwidth120pxborder0-classnoimgborderset-up-currents}

> このページでは、Braze Currentsの連携と設定を行う一般的なプロセスを概説します。

{% alert important %}
Currentsは特定のBrazeパッケージに含まれています。ご質問がある場合、またはアクセスを希望する場合は、Brazeの担当者にお問い合わせください。
{% endalert %}

## トラブルシューティング {#troubleshooting}

### 新しいCurrents連携を追加できない {#cannot-add-a-new-currents-integration}

新しい連携を追加する際に「You do not have any remaining Currents integrations」と表示される場合、または新しいCurrentsコネクターを追加するボタンがグレーアウトしている場合、一般的な原因は以下のとおりです。

- このワークスペースにCurrentsのエンタイトルメントが購入されていません。
- Currentsのエンタイトルメントが、同じ会社内の別のワークスペースで利用可能になっています。

これを解決するには、会社内の他のワークスペースを確認してください。別のワークスペースで利用可能なCurrentsのエンタイトルメントが表示される場合があります。エンタイトルメントのリクエストや設定の調整が必要な場合は、Brazeのアカウントマネージャーにお問い合わせください。

## 要件 {#requirements}

Currentsをいずれかのパートナーと使用するには、同じ基本パラメーターと接続方法が必要です。

各パートナーは、Brazeがデータファイルを書き込んで送信する権限を持つことを要求し、Brazeはそれらのファイルを書き込む場所（具体的にはバケット名やキー）を確認します。

以下の要件は、ほとんどのパートナーと連携するための基本的な最低要件です。一部のパートナーでは追加のパラメーターが必要な場合があり、それらは各[パートナードキュメント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)に、これらの基本要件に関連する注意事項とともに記載されています。

| 要件 | Origin | アクセス | 説明
|---|---|---|---|
| パートナーのアカウント | パートナーとアカウントを手配するか、Brazeアカウントマネージャーに相談してください。 | パートナーのサイトを確認するか、パートナーに連絡してサインアップしてください。 | 自社のアカウントを通じてデータにアクセスできない場合、Brazeはパートナーにデータを送信しません。
| パートナーAPIキーまたはトークン | 通常はパートナーのダッシュボードにあります。 | コピーして、Brazeの指定フィールドに貼り付けてください。 | Brazeには、そのパートナーの連携ページに専用のフィールドがあります。これは、データの送信先をマッピングするために必要です。**パートナーキーまたはトークンを常に最新の状態に保ってください。認証情報が無効になると、コネクターが無効化され、イベントがドロップされる可能性があります。**
| 認証コード/キー、シークレットキー、証明書ファイル | パートナーのアカウント担当者に連絡してください。パートナーのダッシュボードにも存在する場合があります。 | キーをコピーしてBrazeの指定フィールドに貼り付けてください。`.json`やその他の証明書ファイルを生成し、Brazeの適切な場所にアップロードしてください。 | Brazeには、そのパートナーの連携ページに専用のフィールドがあります。これにより、Brazeに認証情報が付与され、パートナーアカウントにファイルを書き込む権限が与えられます。**認証情報を常に最新の状態に保つことが重要です。認証情報が無効になると、コネクターが無効化され、イベントがドロップされる可能性があります。**
| バケット、フォルダーパス | 一部のパートナーはバケットごとにデータを整理・分類します。これはパートナーのダッシュボードで確認できます。 | これが必要な場合は、バケット名またはファイルパスをBrazeの指定スペースに正確にコピーしてください。 | これは一部のパートナーでのみ必要ですが、必要な場合は正確に入力することが重要です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="要件" }

{% alert important %}
パートナーキー、パートナートークン、および認証情報を常に最新の状態に保つことが重要です。コネクターの認証情報が期限切れになると、コネクターはイベントの送信を停止します。この状態が**5日間**以上続くと、コネクターのイベントはドロップされ、データは永久に失われます。
{% endalert %}

## Currentsの設定 {#setting-up-currents}

### ステップ1：パートナーを選択する {#step-1-choose-your-partner}

Braze Currentsでは、フラットファイルを使用したデータストレージとの連携、または指定されたエンドポイントへのバッチ処理されたJSONペイロードを使用した行動分析および顧客データパートナーとの連携が可能です。

連携を開始する前に、目的に最適な連携方法を決定することをお勧めします。たとえば、すでにmParticleやセグメントを使用しており、Brazeのデータをそこにストリーミングしたい場合は、バッチ処理されたJSONペイロードを使用するのが最適です。データを独自に操作したい場合や、より複雑なデータ分析システムをお持ちの場合は、データストレージを使用するのが最適かもしれません（[Brazeもこの方法を使用しています]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)！）。

### ステップ2：Currentsを開く {#step-2-open-currents}

開始するには、**パートナー連携** > **Currents**に移動します。Currents連携管理ページが表示されます。

![Brazeダッシュボードの Currents ページ]({% image_buster /assets/img_archive/currents-main-page.png %})

### ステップ3：パートナーを追加する {#step-3-add-your-partner}

画面上部のドロップダウンを選択して、パートナー（「Currentsコネクター」とも呼ばれます）を追加します。

各パートナーには異なる設定ステップが必要です。各連携を有効にするには、[利用可能なパートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)のリストを参照し、それぞれのページの手順に従ってください。

{% multi_lang_include currents/contact_email_notifications.md %}

### ステップ4：イベントを設定する {#step-4-configure-your-events}

利用可能なオプションからチェックを入れて、そのパートナーに渡したいイベントを選択します。これらのイベントの一覧は、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)および[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)ライブラリで確認できます。

![エクスポート用のパートナーイベントが選択されたCurrents設定ページ]({% image_buster /assets/img/current4.png %})

必要に応じて、[イベント配信のセマンティクス]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics)の記事でイベントの詳細を確認できます。

### ステップ5：フィールド変換を設定する {#step-5-set-up-field-transformations}

Currentsのフィールド変換を使用して、文字列フィールドを削除またはハッシュ化できます。

- **削除：**文字列フィールドを`[REDACTED]`に置き換えます。これは、パートナーが欠落または空のフィールドを含むイベントを拒否する場合に便利です。
- **ハッシュ化：**文字列フィールドにSHA-256ハッシュアルゴリズムを適用します。

これらの変換のいずれかにフィールドを選択すると、そのフィールドが含まれるすべてのイベントにその変換が適用されます。たとえば、`email_address`をハッシュ化対象として選択すると、メール送信、メール開封、メールバウンス、および購読グループの状態変更イベントの`email_address`フィールドがハッシュ化されます。

![フィールド変換の追加]({% image_buster /assets/img/current3.png %})

### ステップ6：連携をテストする {#step-6-test-your-integration}

{% alert important %}
Currentsは、900&nbsp;KB を超える過度に大きなペイロードを持つイベントをドロップします。
{% endalert %}

テストを行う前に、[GitHubのCurrentsサンプルデータ](https://github.com/Appboy/currents-examples)を確認することをお勧めします。テストの準備ができたら、以下のセクションからオプションを選択してください。

#### テストイベントを送信する {#sending-test-events}

連携をテストするには、**Send Test Events**を選択して、選択した各イベントタイプから1つのイベントをこのCurrentに送信できます。各イベントタイプの詳細については、[顧客行動イベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)および[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)ライブラリを参照してください。

![Brazeダッシュボードの「Currents テスト」ページ]({% image_buster /assets/img/currents/current_test_events.png %}){: style="max-width:70%;"}

#### Currentsコネクターのテスト {#testing-currents-connectors}

テスト用Currentsコネクターは、既存のコネクターの無料バージョンで、テストやさまざまな送信先の試用に使用できます。テスト用Currentsには以下の特徴があります。

- ワークスペースごとに最大10個のテスト用Currentsコネクター。
- 固定の24時間あたり合計最大1,500イベント（UTC午前0時にリセット）。このイベント合計はダッシュボード上で1時間ごとに更新されます。

テスト用Currentsコネクターが送信上限に達すると、翌日（UTC午前0時）までコネクターはイベントを送信しません。

テスト用Currentsコネクターをアップグレードするには、ダッシュボードで連携を編集し、**Upgrade Test Integration**を選択してください。

## Currentsの更新 {#updating-currents}

{% multi_lang_include currents/updating_currents.md %}

## IP許可リスト {#ip-allowlisting}

Brazeは、以下のIPアドレスからCurrentsデータを送信します。

{% multi_lang_include administer/data_centers.md datacenters='ips' %}