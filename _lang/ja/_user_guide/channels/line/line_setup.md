---
nav_title: "セットアップ"
article_title: LINE セットアップ
description: "この記事では、前提条件や推奨される次のステップを含む、Braze LINE チャネルのセットアップ方法について説明します。"
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE セットアップ {#line-setup}

> この記事では、ユーザーのセットアップ、ユーザーIDの照合、BrazeでのLINEテストユーザーの作成方法を含む、BrazeでのLINEチャネルのセットアップ方法について説明します。

## 前提条件 {#prerequisites}

LINEをBrazeと連携するには、以下が必要です。

- [LINEビジネスアカウント](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- プレミアムまたは認証済みアカウントステータス（既存のフォロワーを同期するために必要）
   - [LINEのアカウントガイドライン](https://terms2.line.me/official_account_guideline_oth)を参照してください
- [LINE Developersアカウント](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE Messaging APIチャネル](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

BrazeからLINEメッセージを送信すると、アカウントのメッセージクレジットまたはアクションクレジットが消費されます。

{% alert note %}
**`native_line_id`の設定**: `native_line_id`は、Brazeにユーザー更新を送信することで設定できます（例：[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用）。クライアント側のSDKに`native_line_id`専用のフィールドがない場合は、これらの方法のいずれかを使用してサーバー側のユーザー更新で送信してください。
{% endalert %}

## LINEアカウントの種類 {#types-of-line-accounts}

| アカウントの種類 | 説明 |
| --- | --- |
| 未認証アカウント | 誰でも（個人・法人問わず）取得できる、審査を受けていないアカウントです。灰色のバッジで表示され、LINEアプリ内の検索結果には表示されません。 |
| 認証済みアカウント | LINE Yahooの審査に合格したアカウントです。青色のバッジで表示され、LINEアプリ内の検索結果に表示されます。<br><br>このアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントのみ利用可能です。 |
| プレミアムアカウント | LINE Yahooの審査に合格したアカウントです。緑色のバッジで表示され、LINEアプリ内の検索結果に表示されます。このアカウントの種類は、LINEの裁量により審査時に自動的に付与されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINEアカウントの種類" }

### 必要なアカウントの種類 {#required-account-type}

フォロワーをBrazeに同期するには、LINEアカウントが認証済みまたはプレミアムである必要があります。アカウントを作成すると、デフォルトのステータスは未認証になります。アカウント認証をリクエストする必要があります。

### 認証済みLINEアカウントの申請 {#applying-for-a-verified-line-account}

{% alert important %}
認証済みアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントのみ利用可能です。
{% endalert %}

1. LINEの**公式アカウント**ページで、**設定**を選択します。
2. **情報公開認証ステータス**の下にある**アカウント認証をリクエスト**を選択します。
3. 必要な情報を入力します。
4. 審査結果の通知を待ちます。

## LINEの連携 {#integrating-line}

一貫したユーザー更新を設定するには、既存ユーザーのLINE IDを取り込み、LINEの購読ステータスと同期します。

1. [既存の既知のユーザーをインポートまたは更新する](#step-1-import-or-update-existing-line-users)
2. [LINEチャネルを連携する](#step-2-integrate-line-channel)
3. [ユーザーIDを照合する](#step-3-reconcile-user-ids)
4. [ユーザー更新方法を変更する](#step-4-change-your-user-update-methods)
5. [（オプション）ユーザープロファイルを統合する](#step-5-merge-profiles-optional)

{% alert note %}
1つのワークスペースで使用できるLINEアカウントは1つのみです。複数のLINEアカウントをお持ちの場合は、それぞれ別のワークスペースで使用することをお勧めします。
{% endalert %}

## ステップ1：既存のLINEユーザーをインポートまたは更新する {#step-1-import-or-update-existing-line-users}

このステップは、既存の識別済みLINEユーザーがいる場合に必要です。Brazeは後で自動的にそのユーザーの購読状態を取得し、正しいユーザープロファイルを更新します。以前にユーザーとLINE IDを紐付けたことがない場合は、このステップをスキップしてください。

Brazeがサポートする任意の方法を使用してユーザーをインポートまたは更新できます。[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)が利用可能です。

使用する方法に関係なく、`native_line_id` を更新してユーザーのLINE IDを指定してください。`native_line_id` の詳細については、[ユーザー設定](#user-setup)を参照してください。

{% alert note %}
購読グループの状態は指定する必要はなく、指定しても無視されます。LINEがユーザーの購読ステータスの信頼できる情報源であり、購読同期ツールまたはイベント更新を通じてBrazeに同期されます。
{% endalert %}

## ステップ2: LINEチャネルを連携する {#step-2-integrate-line-channel}

連携プロセスが完了すると、BrazeはそのチャネルのLINEフォロワーを自動的にBrazeに取り込みます。すでにBrazeユーザープロファイルに関連付けられているLINE IDについては、各プロファイルが「subscribed」ステータスに更新され、残りのLINE IDは匿名ユーザーとして生成されます。さらに、LINEチャネルの新しいフォロワーがチャネルをフォローすると、未識別のユーザープロファイルが作成されます。

### ステップ2.1: Webhook設定を編集する {#step-21-edit-webhook-settings}

1. LINEで**Messaging API**タブに移動し、**Webhook設定**を編集します。
   - **Webhook URL**を`https://anna.braze.com/line/events`に設定します。
      - Brazeは連携時にダッシュボードクラスターに基づいて、自動的にこのURLを別のURLに変更します。
   - **Webhookの利用**と**Webhookの再送**をオンにします。<br><br> ![Webhook URLの確認や編集、「Webhookの利用」「Webhookの再送」「エラー統計の集計」のオン・オフを切り替えるWebhook設定ページ。]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. **プロバイダー**タブで以下の情報を確認します。

| 情報の種類 | 場所 |
| --- | --- |
| プロバイダーID | プロバイダーを選択し、**設定** > **基本情報**に移動します |
| チャネルID | プロバイダーを選択し、**チャネル** > 対象のチャネル > **基本設定**に移動します |
| チャネルシークレット | プロバイダーを選択し、**チャネル** > 対象のチャネル > **基本設定**に移動します |
| チャネルアクセストークン | プロバイダーを選択し、**チャネル** > 対象のチャネル > **Messaging API**に移動します。チャネルアクセストークンがない場合は、**発行**を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2.1: Webhook設定を編集する" }

{% alert note %}
すでに連携済みのLINEチャネルのチャネルシークレットとチャネルアクセストークンは、**パートナー連携** > **テクノロジーパートナー** > **LINE**に移動し、連携を選択することで更新またはローテーションできます。
{% endalert %}

{: start="3"}
3. **設定**ページ > **応答設定**に移動し、以下を行います。
   - **あいさつメッセージ**をオフにします。これはBrazeでフォロー時のトリガーとして処理できます。
   - **自動応答メッセージ**をオフにします。トリガーされるメッセージングはすべてBrazeを通じて行う必要があります。これにより、LINEコンソールから直接送信することが妨げられるわけではありません。
   - **Webhook**をオンにします。

![アカウントがチャットをどのように処理するかのトグルがある応答設定ページ。]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### ステップ2.2: Brazeで LINE購読グループを生成する {#step-22-generate-line-subscription-groups-in-braze}

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. BrazeのLINEテクノロジーパートナーページに移動し、LINEの**プロバイダー**タブで確認した情報を入力します。
   - プロバイダーID
   - チャネルID
   - チャネルシークレット
   - チャネルアクセストークン

LINEアカウントでIPホワイトリストを追加する場合は、[IPの許可リスト]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)に記載されているクラスターのすべてのIPアドレスを許可リストに追加してください。

{% alert important %}
連携時には、チャネルシークレットが正しいことを必ず確認してください。正しくない場合、購読ステータスに不整合が生じる可能性があります。
{% endalert %}

![LINE連携セクションがあるLINEメッセージング連携ページ。]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. 接続後、Brazeはワークスペースに正常に追加された各LINE連携に対して、Braze購読グループを自動的に生成します。<br><br> フォロワーリストの変更（新しいフォロワーやフォロー解除など）は自動的にBrazeにプッシュされます。

![「LINE」チャネルの購読グループが1つ表示されているLINE購読グループセクション。]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## ステップ3：ユーザーIDを照合する {#step-3-reconcile-user-ids}

[ユーザーID照合](#user-id-reconciliation)の手順に従って、ユーザーのLINE IDを既存のBrazeユーザープロファイルと統合します。

## ステップ4: ユーザー更新メソッドを変更する {#step-4-change-your-user-update-methods}

Brazeにユーザー更新を提供するメソッドがすでにある場合、新しいフィールド `native_line_id` を含めるように更新する必要があります。これにより、Brazeに送信される後続のユーザー更新にそのフィールドが含まれるようになります。

`native_line_id` を持つ未識別のユーザープロファイルが、購読ステータスの同期プロセスの一環として、または新しいフォロワーがチャネルをフォローした際に作成され、Brazeに存在している場合があります。

LINEユーザーがアプリケーション内で[ユーザー照合](#user-id-reconciliation)やその他の手段を通じて識別された場合、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) エンドポイントを使用して、Braze内の潜在的な未識別ユーザープロファイルをターゲットにできます。`native_line_id` を持つすべての未識別ユーザープロファイルには、ユーザープロファイルを識別するためにターゲットとして使用できるユーザーエイリアス `line_id` もあります。

以下は、ユーザーエイリアス `line_id` によって未識別のユーザープロファイルをターゲットにする `/users/identify` へのペイロードの例です：

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

指定した `external_id` に対応する既存のユーザープロファイルが存在しない場合、未識別のユーザープロファイルに追加され、識別済みになります。`external_id` に対応するユーザープロファイルが既に存在する場合、未識別のユーザープロファイルにのみ存在するすべての属性（`native_line_id` やユーザーの購読ステータスを含む）が既知のユーザープロファイルにコピーされます。

アプリケーションで既知のLINEユーザーは、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイントを通じて、external IDと `native_line_id` を渡すことで更新できます。あるユーザーの未識別ユーザープロファイルが既に存在し、同じ `native_line_id` が `/users/track` を通じて別のユーザープロファイルに追加された場合、そのプロファイルは未識別ユーザープロファイルのすべての購読ステータスを継承します。ただし、同じ `native_line_id` を持つ重複したユーザープロファイルが存在することになります。イベント更新による後続の購読更新は、すべてのプロファイルを適切に更新します。

{% alert note %}
LINEの購読ステータスは `external_id` ではなく `native_line_id` によって追跡されます。たとえば、ユーザーBのユーザープロファイルがユーザーAと同じ `native_line_id` で作成されたが、同じ `external_id` ではない場合、ユーザーBはユーザーAのLINE購読ステータスを継承します。
{% endalert %}

以下は、external IDによってユーザープロファイルを更新し、`native_line_id` を追加する `/users/track` へのペイロードの例です：

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## ステップ5: プロファイルの統合（オプション） {#step-5-merge-profiles-optional}

このセクションで前述したように、同じ `native_line_id` を持つ複数のユーザープロファイルが存在する可能性があります。更新方法によって重複するユーザープロファイルが作成された場合、`/user/merge` エンドポイントを使用して、未識別のユーザープロファイルを識別済みのユーザープロファイルに統合できます。

以下は、ユーザーエイリアス `line_id` で未識別のユーザープロファイルを対象とする `/users/merge` へのペイロードの例です。

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
Brazeでの重複ユーザーの管理について詳しくは、[重複ユーザー]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)を参照してください。
{% endalert %}

## ユーザー設定 {#user-setup}

LINE はユーザーの購読状態に関する信頼できる情報源です。ユーザーの LINE ID（`native_line_id`）を持っていても、そのユーザーが送信元の LINE チャネルをフォローしていない場合、LINE はそのユーザーにメッセージを配信しません。

これを管理するために、Braze は購読の同期や LINE のフォロー・フォロー解除に対するイベント更新など、適切に統合されたユーザー群をサポートするツールとロジックを提供しています。

### 購読の同期とイベントロジック {#subscription-syncing-and-event-logic}

1. **購読同期ツール:** このツールは、LINE チャネルの連携が正常に完了した後に自動的にデプロイされます。既存のプロファイルの更新や新しいプロファイルの作成に使用します。<br><br>LINE チャネルをフォローしている `native_line_id` を持つすべての Braze ユーザープロファイルは、購読グループのステータスが `subscribed` に更新されます。`native_line_id` を持つ Braze ユーザープロファイルが存在しない LINE チャネルのフォロワーには、以下が適用されます。<br><br>- チャネルをフォローしているユーザーの LINE ID が `native_line_id` として設定された匿名ユーザープロファイルが作成されます <br>- チャネルをフォローしているユーザーの LINE ID がユーザーエイリアス `line_id` として設定されます <br>- 購読グループのステータスが `subscribed` に設定されます

{: start="2"}
2. **イベント更新:** ユーザーの購読ステータスを更新するために使用されます。Braze が連携された LINE チャネルのユーザーイベント更新を受信し、そのイベントがフォローである場合、ユーザープロファイルの購読グループのステータスは `subscribed` になります。イベントがフォロー解除である場合、ユーザープロファイルの購読グループのステータスは `unsubscribed` になります。<br><br>- 一致する `native_line_id` を持つすべての Braze ユーザープロファイルが自動的に更新されます。 <br>- イベントに一致するユーザープロファイルが存在しない場合、Braze は[匿名ユーザーを作成]({{site.baseurl}}/line/user_management)します。

## 別のワークスペースで LINE チャネルを再統合する {#re-integrate-a-line-channel-in-another-workspace}

LINE チャネルを別の Braze ワークスペースで使用するには、以下の手順を実行します。

1. 元のワークスペースで、そのチャネルの購読グループをアーカイブします。
2. 対象のワークスペースで、[ステップ 2: LINE チャネルを統合する](#step-2-integrate-line-channel)を使用してチャネルを統合します。

両方のワークスペースで[購読グループの管理]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)権限があることを確認してください。両方のワークスペースで権限がない場合、チャネルがすでに接続されていることを示すエラーが表示され、統合に失敗します。

アーカイブが購読グループに与える影響については、[LINE 購読グループ]({{site.baseurl}}/line/subscription_groups#archive-behavior)を参照してください。

## ユースケース {#use-cases}

以下は、設定ステップを完了した後にユーザーを更新する方法のユースケースです。

### 既存のBrazeユーザープロファイルがすでにLINEチャネルをフォローしている場合 {#existing-braze-user-profile-already-follows-line-channel}

1. Brazeユーザープロファイルが`native_line_id`属性で更新されます。デフォルトの購読ステータスは`unsubscribed`です。
2. 購読同期ツールが実行され、ユーザーがLINEチャネルをフォローしていることを検出し、ユーザープロファイルの購読ステータスを`subscribed`に更新します。
3. 購読ステータスの変更が発生した場合（ユーザーがチャネルをブロック、友だち解除、または再フォローした場合など）、BrazeはLINEから更新を受信し、それに応じて`native_line_id`でユーザープロファイルを更新します。

### 既存のユーザープロファイルがLINEチャネルをブロック、友だち解除、またはフォロー解除している場合 {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. Brazeユーザープロファイルが`native_line_id`属性で更新されます。デフォルトの購読ステータスは`unsubscribed`です。
2. 購読同期ツールはユーザーがLINEチャネルをフォローしていることを検出できず、ユーザーの購読ステータスは`unsubscribed`のままになります。
3. ユーザーが後でチャネルをフォローした場合、BrazeはLINEから更新を受信し、ユーザープロファイルの購読ステータスを`subscribed`に更新します。

### LINEフォロー後にユーザープロファイルが作成される場合 {#user-profile-creation-occurs-after-line-follow}

1. チャネルに新しいLINEフォロワーが追加されます。
2. Brazeは`native_line_id`属性にフォロワーのLINE IDを設定し、`line_id`のユーザーエイリアスにフォロワーのLINE IDを設定した匿名ユーザープロファイルを作成します。このプロファイルの購読ステータスは`subscribed`です。
3. [ユーザー照合](#user-id-reconciliation)を通じて、ユーザーがそのLINE IDを持っていることが特定されます。
  - 匿名ユーザープロファイルは、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントを使用して識別済みにすることができます。その後のこのユーザープロファイルへの更新（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を通じて）は、この既知の`external_id`でユーザーをターゲットにすることができます。

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - 新しいユーザープロファイルは、`native_line_id`を設定することで（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を通じて）作成できます。この新しいプロファイルは、既存の匿名ユーザープロファイルの購読ステータスの状態を継承します。これにより、同じ`native_line_id`を共有する複数のプロファイルが存在することになります。これらは、[ステップ5](#step-5-merge-profiles-optional)で説明されているプロセスで`/users/merge`エンドポイントを使用していつでもマージできます。

### LINEフォロー前にユーザープロファイルが作成される場合 {#user-profile-creation-occurs-before-line-follow}

1. 新しいユーザーを獲得し、その情報をBrazeに送信します。新しいユーザープロファイルが作成されます（プロファイル1）。
2. ユーザーがLINEアカウントをフォローします。
3. Brazeはフォローイベントを受信し、匿名ユーザープロファイルを作成します（プロファイル2）。
4. [ユーザー照合](#user-id-reconciliation)を通じて、ユーザーがそのLINE IDを持っていることが特定されます。
5. プロファイル1を更新して`native_line_id`属性を設定します。このプロファイルはプロファイル2の購読ステータスの状態を継承します。
  - これで、同じ`native_line_id`を持つ2つのユーザープロファイルが存在します。これらは、[ステップ5](#step-5-merge-profiles-optional)で説明されているプロセスで`/users/merge`エンドポイントを使用していつでもマージできます。

## ユーザーIDの照合 {#user-id-reconciliation}

LINE IDは、ユーザーがチャネルをフォローしたとき、またはワンタイムの「フォロワー同期」ワークフローを使用したときに、Brazeが自動的に受信します。LINE IDはユーザーがフォローしたチャネルに固有であるため、ユーザーが自分のLINE IDを提供できる可能性は低いです。

LINE IDを既存のBrazeユーザープロファイルと統合するには、2つの方法があります。

- [LINEログイン](#line-login)
- [ユーザーアカウントリンク](#user-account-linking)

### LINEログイン {#line-login}

この方法では、ソーシャルメディアログインを使用して照合を行います。ユーザーがアプリにログインすると、[LINEログイン](https://developers.line.biz/en/docs/line-login/overview/)を使用してユーザーアカウントを作成するか、ログインするかのオプションが表示されます。

{% alert note %}
各ユーザーの正しいLINE IDを取得するには、Brazeと連携しているLINE公式アカウントまたはチャネルと同じプロバイダーの下にLINEログインを設定してください。
{% endalert %}

1. LINE Developer Consoleにアクセスし、LINEログインを通じてアプリにログインするユーザーの[メールアドレスを取得する権限をリクエスト](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)します。

2. LINEが提供する適切な手順に従って、LINEログインを実装します。<br><br>
  - [Webアプリの手順](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [ネイティブアプリの手順](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>検証リクエストの[スコープ設定](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)に`email`を含めるようにしてください。

{: start="3"}
3. [IDトークン検証呼び出し](https://developers.line.biz/en/reference/line-login/#verify-id-token)を使用して、ユーザーのメールアドレスを取得します。

4. ユーザーのLINE ID（`native_line_id`）を、データベース内で一致するメールアドレスを持つユーザーのプロファイルに保存するか、ユーザーのメールアドレスとLINE IDで新しいユーザープロファイルを作成します。

5. 新規または更新されたユーザー情報を、[`/user/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用してBrazeに送信します。

#### ワークフロー {#workflows}

##### 既存のフォロワーがLINEログインを使用する場合 {#existing-follower-uses-line-login}

**シナリオ：** 初回のサブスクライバー同期中、またはフォローイベントによる連携後に、匿名ユーザーが作成されています。

1. ユーザーがLINEログインを使用してアプリにログインします。
2. LINEがユーザーのメールアドレスを提供します。
3. 更新されたユーザー（LINE IDを追加するための、そのメールアドレスを持つ既存のユーザープロファイル）をBrazeに送信するか、匿名ユーザーをメールアドレスで更新します。

##### 新しいフォロワーがLINEログインを使用する場合 {#new-follower-uses-line-login}

**シナリオ：** ユーザーのLINE IDを持つユーザープロファイルがBrazeに存在しません。

1. ユーザーがLINEログインを使用してアプリにログインします。
2. LINEがユーザーのメールアドレスを提供します。
3. 次のいずれかを行います。
  - そのメールアドレスを持つ既存のユーザープロファイルを更新して、ユーザーのLINE IDも含めます。
  - メールアドレスとLINE IDで新しいユーザープロファイルを作成します。
4. ユーザーがLINE公式アカウントをフォローすると、Brazeがフォローイベントを受信し、ユーザーの購読ステータスを`subscribed`に更新します。

### ユーザーアカウントリンク {#user-account-linking}

この方法では、ユーザーがLINEアカウントをアプリのユーザーアカウントにリンクできます。その後、Brazeで{% raw %}`{{line_id}}`{% endraw %}などのLiquidを使用して、ユーザーのLINE IDをWebサイトやアプリに渡すパーソナライズされたURLを作成し、既知のユーザーに関連付けることができます。

1. 購読状態の変更に基づくアクションベースのキャンバスを作成し、ユーザーがLINEチャネルを購読したときにトリガーされるようにします。<br>![ユーザーがLINEチャネルを購読したときにトリガーされるキャンバス。]({% image_buster /assets/img/line/account_link_1.png %})
2. ユーザーにWebサイトやアプリへのログインを促すメッセージを作成し、ユーザーのLINE IDをクエリパラメーターとして（Liquidを通じて）渡します。例：

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. クーポンコードを配信するフォローアップメッセージを作成します。
4. （オプション）LINEユーザーが識別されたときにトリガーされるアクションベースのキャンペーンまたはキャンバスを作成し、ユーザーにクーポンコードを送信します。<br>![LINEユーザーが識別されたときにトリガーされるアクションベースのキャンペーン。]({% image_buster /assets/img/line/account_link_2.png %})

#### 仕組み {#how-it-works}

ユーザーがログインすると、Webサイトまたはアプリ側で変更が行われ、URLの一部として渡されたLINE IDとユーザーIDを関連付けるためにBrazeに送信されます。コード例は以下のとおりです。

```javascript
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### ワークフロー

##### 既存のユーザーがLINEチャネルをフォローする場合 {#existing-user-follows-your-line-channel}

**シナリオ：** Brazeの既存ユーザーがLINEでチャネルをフォローします。

1. LINEがBrazeにフォローイベントを送信します。
2. BrazeがLINE ID、`line_id`ユーザーエイリアス、およびLINE購読グループステータス`subscribed`を持つ匿名ユーザープロファイルを作成します。
3. ユーザーがWebサイトやアプリへのリンクを含むLINEメッセージを受信し、ログインします。これにより、ユーザープロファイルが既知になります。
4. 作成された匿名ユーザープロファイルが識別され、[/users/identifyエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を通じてユーザーの既知のユーザープロファイルにマージされます。既知のユーザープロファイルにLINE IDが含まれ、購読ステータスが`subscribed`になります。
5. （オプション）ユーザーがクーポンコードを含むLINEメッセージを受信し、Brazeがその送信をBrazeユーザープロファイルに記録します。

## BrazeでのLINEテストユーザーの作成 {#creating-line-test-users-in-braze}

[ユーザー照合](#user-id-reconciliation)を設定する前に、「Who am I」キャンバスまたはキャンペーンを作成してLINEチャネルをテストできます。

1. 特定のトリガーワードでユーザーのBrazeユーザーIDを返すキャンバスを設定します。<br><br>トリガーの例<br><br>![特定の購読グループにインバウンドLINEを送信したユーザーにキャンペーンを送信するトリガー。]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>メッセージの例<br><br>![BrazeユーザーIDを表示するLINEメッセージ。]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Brazeでは、Braze IDを使用して特定のユーザーを検索し、必要に応じて変更できます。

{% alert important %}
キャンバスにグローバルコントロールやコントロールグループが設定されていて送信が妨げられることがないようにしてください。
{% endalert %}