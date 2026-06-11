---
nav_title: データ変換
article_title: データ変換
page_order: 2
layout: dev_guide
guide_top_header: "データ変換"
guide_top_text: "Braze Data Transformationを使用すると、Webhook連携の構築および管理を行って、外部プラットフォームからBrazeへのデータフローを自動化できます。この新しく統合されたユーザーデータにより、さらに洗練されたマーケティングユースケースを強化できます。Braze Data Transformationでは、コーディングの経験がほとんどなくても迅速にデータ統合ができ、また手動API呼び出し、サードパーティの統合ツール、さらに顧客データプラットフォームへの依存からチームが脱却するうえで役立ちます。"
page_type: landing
description: "このランディングページには、変換の作成方法やユースケースなど、Braze Data Transformationに関する記事がまとめられています。"
alias: /data_transformation/

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: 変換の作成
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation
    image: /assets/img/braze_icons/flip-forward.svg
  - name: ユースケース
    link: /docs/user_guide/data/unification/data_transformation/use_cases
    image: /assets/img/braze_icons/users-01.svg
---

## 仕組み {#how-it-works}

最近のプラットフォームの多くは、「Webhook」、つまり新しいイベントや新しいデータに関する情報をあるプラットフォームから別のプラットフォームに送信するためのリアルタイムAPI通知を装備しています。Data Transformationは以下を提供します。

* このようなWebhookを受信するためのBraze URLアドレス。
* Webhookペイロードを JavaScript コードで変換して、Brazeの `/users/track` や `/catalogs` など、さまざまなBraze APIエンドポイントへの有効なリクエストを作成する機能。例えば、送信先が `/users/track` の場合は、Webhookからどの情報を使用するか、またBrazeユーザープロファイルのユーザー属性、イベント、または購入としてデータをどのように表現するかを選択できます。
* 品質保証、トラブルシューティング、および変換のパフォーマンスの監視を実行するためのログ記録。

最終的には、選択したソースプラットフォームのWebhookをBrazeの更新に変換することで、そのソースプラットフォームを接続するWebhook連携が実現します。

{% details Webhookの詳細 %}
Webhookは、HTTP POSTリクエストを介して特定の宛先に送信されるリアルタイム通知です。Webhookは、あるポイントから別のポイントへのデータ送信によく使用されます。Webhookは、発生したアクションとそのアクションに誰が関与したかに関するデータを渡すことができます。

例えば、調査プラットフォームは、オンラインフォームへのアンケート回答を受信するたびに、選択した宛先にWebhookを送信できます。また、カスタマーサービスプラットフォームは、カスタマーサービスチケットが作成されるたびに、選択した宛先にWebhookを送信できます。
{% enddetails %}

## Data Transformationのティア {#data-transformation-tiers}

次の表で、Data Transformationの無料バージョンとプロバージョンの違いを説明します。

| エリア | 無料版 | Data Transformation Pro |
|----|----|----|
| アクティブ変換 | 1社につき最大5個 | 1社につき最大55個 |
| 月あたり | 月間受信リクエスト30万件 | 月間受信リクエスト1,030万件 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Data Transformationのティア" }

{% alert important %}
Data Transformation Proへのアップグレードをリクエストするには、Brazeアカウントマネージャーに問い合わせるか、Brazeダッシュボードの**Request Upgrade**ボタンを選択してください。
{% endalert %}

### レート制限 {#rate-limits}

Braze Data Transformationのレート制限は、ワークスペースあたり毎分1,000件の受信リクエストです。Data Transformation Proを使用していて、より高いレート制限が必要な場合は、Brazeアカウントマネージャーにお問い合わせください。

## よくある質問 {#frequently-asked-questions}

### Braze Data Transformationでは何が同期されますか? {#what-gets-synced-with-braze-data-transformation}

外部プラットフォームがWebhookで利用可能にしたデータはすべて、Brazeに同期できます。外部プラットフォームがWebhook経由で送信するデータの種類が増えるほど、同期するデータを選択するためのオプションが増えます。

### 私はマーケターです。Braze Data Transformationを使用するには開発者のリソースが必要ですか? {#im-a-marketer-do-i-need-developer-resources-to-use-braze-data-transformation}

開発者にもこの機能を使用していただきたいと考えていますが、Braze Data Transformationを使用するために開発者である必要はありません。マーケターは、開発者のリソースがなくても変換を正常に設定できます。

### 外部プラットフォームが識別子としてメールアドレスまたは電話番号のみを提供する場合でも、Braze Data Transformationを使用できますか? {#can-i-still-use-braze-data-transformation-if-my-external-platform-only-gives-an-email-address-or-phone-number-as-an-identifier}

はい。[メールアドレスまたは電話番号を識別子として]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address)使用して、変換により `/users/track` エンドポイントを更新できます。

これは、変換コード内の識別子プロパティとして、`external_id` または `braze_id` の代わりに `email` または `phone` を使用することで機能します。[変換コード]({{site.baseurl}}/user_guide/data/unification/data_transformation/use_cases/#example-transformation-code)の例では、この機能を使用しています。

{% alert note %}
2023年4月より前にBraze Data Transformationの使用を開始した早期アクセスユーザーは、このユースケースに役立つ `get_user_by_email` 関数をご存知かもしれませんが、その関数は廃止されました。
{% endalert %}

### Braze Data Transformationはデータポイントを記録しますか? {#does-braze-data-transformation-log-data-points}

はい、ほとんどの場合記録します。Braze Data Transformationは最終的に、必要な属性、イベント、および購入を書き込む `/users/track` 呼び出しを作成します。これらは、`/users/track` 呼び出しが独立して行われた場合と同じようにデータポイントを記録します。変換の書き方によって、記録されるデータポイントの数をコントロールできます。

### ユースケースの設定や変換コードのサポートを受けるにはどうすればよいですか? {#how-can-i-get-help-setting-up-my-use-case-or-with-my-transformation-code}

追加のサポートが必要な場合は、Brazeアカウントマネージャーにお問い合わせください。