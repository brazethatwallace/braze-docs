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

LINE をBrazeと連携するには、以下が必要です。

- [LINE ビジネスアカウント](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- プレミアムまたは認証済みアカウントステータス（既存のフォロワーの同期に必要）
   - [LINE のアカウントガイドライン](https://terms2.line.me/official_account_guideline_oth)を参照してください
- [LINE Developers アカウント](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE Messaging API チャネル](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Brazeから LINE メッセージを送信すると、アカウントのメッセージクレジットまたはアクションクレジットが消費されます。

{% alert note %}
**`native_line_id` の設定**: `native_line_id` は、Brazeにユーザー更新を送信することで設定できます（たとえば、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) を使用します）。クライアント側のSDKに `native_line_id` 専用のフィールドがない場合は、これらの方法のいずれかを使用してサーバー側のユーザー更新で送信してください。
{% endalert %}

## LINE アカウントの種類 {#types-of-line-accounts}

| アカウントの種類 | 説明 |
| --- | --- |
| 未認証アカウント | 誰でも（個人・法人を問わず）取得できる、審査を受けていないアカウントです。灰色のバッジで表示され、LINE アプリ内の検索結果には表示されません。 |
| 認証済みアカウント | LINE ヤフーの審査に合格したアカウントです。青色のバッジで表示され、LINE アプリ内の検索結果に表示されます。<br><br>このアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントのみが利用できます。 |
| プレミアムアカウント | LINE ヤフーの審査に合格したアカウントです。緑色のバッジで表示され、LINE アプリ内の検索結果に表示されます。このアカウントの種類は、LINE の裁量により審査時に自動的に付与されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE アカウントの種類" }

### 必要なアカウントの種類 {#required-account-type}

フォロワーを Braze に同期するには、LINE アカウントが認証済みまたはプレミアムである必要があります。アカウントを作成すると、デフォルトのステータスは未認証になります。アカウントの認証をリクエストする必要があります。

### 認証済み LINE アカウントの申請 {#applying-for-a-verified-line-account}

{% alert important %}
認証済みアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントのみが利用できます。
{% endalert %}

1. LINE の **Official Account** ページで、**設定** を選択します。
2. **情報公開の認証ステータス** の下で、**アカウント認証をリクエスト** を選択します。
3. 必要な情報を入力します。
4. 審査結果の通知を待ちます。

## LINEの連携 {#integrating-line}

一貫したユーザー更新を設定するには、既存ユーザーのLINE IDを取り込み、LINEの購読ステータスとすべて同期します。

1. [既存の既知のユーザーをインポートまたは更新する](#step-1-import-or-update-existing-line-users)
2. [LINEチャネルを連携する](#step-2-integrate-line-channel)
3. [ユーザーIDを照合する](#step-3-reconcile-user-ids)
4. [ユーザー更新方法を変更する](#step-4-change-your-user-update-methods)
5. [(オプション) ユーザープロファイルを統合する](#step-5-merge-profiles-optional)

{% alert note %}
1つのワークスペースで使用できるLINEアカウントは1つだけです。複数のLINEアカウントがある場合は、それぞれ別のワークスペースで使用することをお勧めします。
{% endalert %}

## ステップ1：既存のLINEユーザーをインポートまたは更新する {#step-1-import-or-update-existing-line-users}

このステップは、既存の識別済みLINEユーザーがいる場合に必要です。Brazeは後でそのユーザーの購読状態を自動的に取得し、正しいユーザープロファイルを更新します。以前にユーザーとLINE IDを紐付けたことがない場合は、このステップをスキップしてください。

Brazeがサポートする任意の方法を使用してユーザーをインポートまたは更新できます。[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)が利用可能です。

使用する方法に関係なく、`native_line_id` を更新してユーザーのLINE IDを指定してください。`native_line_id` の詳細については、[ユーザー設定](#user-setup)を参照してください。

{% alert note %}
購読グループの状態は指定する必要はなく、指定しても無視されます。LINEはユーザーの購読ステータスに関する信頼できるソースであり、購読同期ツールまたはイベント更新を通じてBrazeに同期されます。
{% endalert %}

## ステップ2: LINEチャネルの連携 {#step-2-integrate-line-channel}

連携プロセスが完了すると、Brazeはそのチャネルの LINE フォロワーを自動的に Braze に取り込みます。Brazeユーザープロファイルに既に関連付けられている LINE ID については、各プロファイルが「subscribed」ステータスに更新され、残りの LINE ID については匿名ユーザーが生成されます。さらに、LINE チャネルの新しいフォロワーがチャネルをフォローすると、未識別のユーザープロファイルが作成されます。

### ステップ2.1: Webhook設定の編集 {#step-21-edit-webhook-settings}

1. LINE で**Messaging API**タブに移動し、**Webhook settings**を編集します。
   - **Webhook URL**を`https://anna.braze.com/line/events`に設定します。
      - Brazeは連携時にダッシュボードクラスターに基づいて、これを自動的に別の URL に変更します。
   - **Use webhook**と**Webhook redelivery**をオンにします。<br><br> ![Webhook URLの確認・編集、「Use webhook」、「Webhook redelivery」、「Error statistics aggregation」のオン・オフを切り替えるWebhook設定ページ。]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. **Providers**タブで以下の情報をメモしてください。

| 情報の種類 | 場所 |
| --- | --- |
| プロバイダーID | プロバイダーを選択し、***Settings** > **Basic information**に移動します |
| チャネルID | プロバイダーを選択し、**Channels** > 対象チャネル > **Basic settings**に移動します |
| チャネルシークレット | プロバイダーを選択し、**Channels** > 対象チャネル > **Basic settings**に移動します |
| チャネルアクセストークン | プロバイダーを選択し、**Channels** > 対象チャネル > **Messaging API**に移動します。チャネルアクセストークンがない場合は、**Issue**を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2.1: Webhook設定の編集" }

{% alert note %}
既に連携済みの LINE チャネルのチャネルシークレットとチャネルアクセストークンは、**パートナー連携** > **テクノロジーパートナー** > **LINE**に移動して連携を選択することで更新またはローテーションできます。
{% endalert %}

{: start="3"}
3. **Settings**ページ > **Response settings**に移動し、以下を行います。
   - **Greeting message**をオフにします。これは Braze でフォロー時のトリガーによって処理できます。
   - **Auto-response messages**をオフにします。すべてのトリガーメッセージングは Braze を通じて行う必要があります。これにより、LINE コンソールから直接送信することが妨げられるわけではありません。
   - **Webhooks**をオンにします。

![チャットの処理方法を切り替えるトグルがある応答設定ページ。]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### ステップ2.2: BrazeでLINE購読グループを生成する {#step-22-generate-line-subscription-groups-in-braze}

Brazeは、連携する各 LINE チャネルに対して[購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#line-subscription-groups)を作成します。LINE 購読グループの仕組みについては、[LINE 購読グループ]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups)を参照してください。

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. Braze の LINE テクノロジーパートナーページに移動し、LINE の**Providers**タブでメモした情報を入力します。
   - プロバイダーID
   - チャネルID
   - チャネルシークレット
   - チャネルアクセストークン

LINE アカウントで IP ホワイトリストを追加する場合は、[IP 許可リスト]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)に記載されているクラスターのすべての IP アドレスを許可リストに追加してください。

{% alert important %}
連携時に、チャネルシークレットが正しいことを必ず確認してください。正しくない場合、購読ステータスに不整合が生じる可能性があります。
{% endalert %}

![LINE連携セクションがあるLINEメッセージング連携ページ。]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. 接続後、Brazeはワークスペースに正常に追加された各 LINE 連携に対して、Braze 購読グループを自動的に生成します。<br><br> フォロワーリストへの変更（新しいフォロワーやフォロー解除など）は、自動的に Braze にプッシュされます。

![「LINE」チャネルの購読グループが1つ表示されているLINE購読グループセクション。]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## ステップ 3: ユーザー IDを照合する {#step-3-reconcile-user-ids}

[ユーザー ID の照合](#user-id-reconciliation)の手順に従って、ユーザーの LINE ID を既存の Braze ユーザープロファイルと統合します。

## ステップ4: ユーザー更新メソッドを変更する {#step-4-change-your-user-update-methods}

すでにBrazeにユーザー更新を提供するメソッドがある場合は、新しいフィールド`native_line_id`を含めるように更新し、以降Brazeに送信されるユーザー更新にそのフィールドが含まれるようにする必要があります。

`native_line_id`を持つ未識別のユーザープロファイルが、購読ステータスの同期プロセスの一環として、または新しいフォロワーがチャネルをフォローした際に作成され、Brazeに存在している場合があります。

LINEユーザーがアプリケーション内で[ユーザー照合](#user-id-reconciliation)やその他の手段を通じて識別された場合、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントを使用して、Braze内の潜在的な未識別ユーザープロファイルをターゲットにできます。`native_line_id`を持つすべての未識別ユーザープロファイルには、識別対象のユーザープロファイルをターゲットにするために使用できるユーザーエイリアス`line_id`もあります。

以下は、ユーザーエイリアス`line_id`で未識別のユーザープロファイルをターゲットにする`/users/identify`へのペイロードの例です:

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

提供した`external_id`に対応する既存のユーザープロファイルが存在しない場合、未識別のユーザープロファイルに追加され、識別済みになります。`external_id`に対応するユーザープロファイルが既に存在する場合、未識別のユーザープロファイルにのみ存在するすべての属性（`native_line_id`やユーザーの購読ステータスを含む）が既知のユーザープロファイルにコピーされます。

アプリケーション内で既知のLINEユーザーは、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントを通じて、外部識別子と`native_line_id`を渡すことで更新できます。あるユーザーに対して未識別のユーザープロファイルが既に存在し、同じ`native_line_id`が`/users/track`を通じて別のユーザープロファイルに追加された場合、そのプロファイルは未識別のユーザープロファイルのすべての購読ステータスを継承します。ただし、同じ`native_line_id`を持つ重複したユーザープロファイルが存在することになります。イベント更新による以降の購読更新は、すべてのプロファイルを適宜更新します。

{% alert note %}
LINEの購読ステータスは`external_id`ではなく`native_line_id`によって追跡されます。たとえば、ユーザーBのユーザープロファイルがユーザーAと同じ`native_line_id`で作成されたが、同じ`external_id`ではない場合、ユーザーBはユーザーAのLINE購読ステータスを継承します。
{% endalert %}

以下は、外部ユーザーIDでユーザープロファイルを更新して`native_line_id`を追加する`/users/track`へのペイロードの例です:

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

## ステップ5: プロファイルのマージ（オプション） {#step-5-merge-profiles-optional}

このセクションで先に説明したように、同じ `native_line_id` を持つ複数のユーザープロファイルが存在する可能性があります。更新方法によって重複するユーザープロファイルが作成された場合は、`/user/merge` エンドポイントを使用して、未識別のユーザープロファイルを識別済みのユーザープロファイルにマージできます。

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

LINE はユーザーの購読ステータスの正式なソースです。ユーザーの LINE ID（`native_line_id`）を持っていたとしても、そのユーザーが送信元の LINE チャネルをフォローしていない場合、LINE はそのユーザーにメッセージを配信しません。

これを管理するために、Braze は購読の同期や LINE のフォロー・フォロー解除に対するイベント更新など、適切に統合されたユーザー群をサポートするツールとロジックを提供しています。

### 購読の同期とイベントロジック {#subscription-syncing-and-event-logic}

購読同期ツールとフォロー・フォロー解除のイベント更新によって LINE の購読ステータスが Braze と整合される仕組みについては、[購読ステータス]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#line)を参照してください。

## 別のワークスペースで LINE チャネルを再連携する {#re-integrate-a-line-channel-in-another-workspace}

LINE チャネルを別の Braze ワークスペースで使用するには、以下の手順に従います。

1. 元のワークスペースで、そのチャネルの購読グループをアーカイブします。
2. 移行先のワークスペースで、[ステップ 2: LINE チャネルの連携](#step-2-integrate-line-channel)を使用してチャネルを連携します。

両方のワークスペースで[購読グループの管理]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)権限があることを確認してください。両方のワークスペースで権限がない場合、チャネルがすでに接続されていることを示すエラーが発生し、連携に失敗します。

アーカイブが購読グループに与える影響については、[LINE 購読グループ]({{site.baseurl}}/line/subscription_groups#archive-behavior)を参照してください。

## ユースケース {#use-cases}

以下は、設定ステップを完了した後にユーザーを更新する方法のユースケースです。

### 既存のBrazeユーザープロファイルがすでにLINEチャネルをフォローしている場合 {#existing-braze-user-profile-already-follows-line-channel}

1. Brazeユーザープロファイルが`native_line_id`属性で更新されます。デフォルトの購読ステータスは`unsubscribed`です。
2. 購読同期ツールが実行され、ユーザーがLINEチャネルをフォローしていることを検出し、購読ステータスを`subscribed`に更新します。
3. 購読ステータスに変更が発生した場合（ユーザーがチャネルをブロック、友達削除、または再フォローした場合など）、BrazeはLINEから更新を受け取り、対応する`native_line_id`でユーザープロファイルを更新します。

### 既存のユーザープロファイルがLINEチャネルをブロック、友達削除、またはフォロー解除した場合 {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. Brazeユーザープロファイルが`native_line_id`属性で更新されます。デフォルトの購読ステータスは`unsubscribed`です。
2. 購読同期ツールは、ユーザーがLINEチャネルをフォローしていないことを確認し、ユーザーの購読ステータスは`unsubscribed`のままとなります。
3. ユーザーが後でチャネルをフォローした場合、BrazeはLINEから更新を受け取り、購読ステータスを`subscribed`に更新します。

### LINEフォロー後にユーザープロファイルが作成される場合 {#user-profile-creation-occurs-after-line-follow}

1. チャネルに新しいLINEフォロワーが追加されます。
2. Brazeは、`native_line_id`属性にフォロワーのLINE IDを設定し、`line_id`のユーザーエイリアスにフォロワーのLINE IDを設定した匿名ユーザープロファイルを作成します。このプロファイルの購読ステータスは`subscribed`です。
3. ユーザーは[ユーザー照合](#user-id-reconciliation)を通じてLINE IDを持つユーザーとして識別されます。
  - 匿名ユーザープロファイルは、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントを使用して識別済みにすることができます。以降のこのユーザープロファイルへの更新（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を通じて）は、この既知の`external_id`でユーザーを対象にすることができます。

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

  - 新しいユーザープロファイルは、`native_line_id`を設定することで（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を通じて）作成できます。この新しいプロファイルは、既存の匿名ユーザープロファイルの購読ステータスを継承します。これにより、同じ`native_line_id`を共有する複数のプロファイルが生成されることに注意してください。これらは、[ステップ5](#step-5-merge-profiles-optional)に記載されたプロセスで`/users/merge`エンドポイントを使用していつでもマージできます。

### LINEフォロー前にユーザープロファイルが作成される場合 {#user-profile-creation-occurs-before-line-follow}

1. 新しいユーザーを獲得し、その情報をBrazeに送信します。新しいユーザープロファイル（プロファイル1）が作成されます。
2. ユーザーがLINEアカウントをフォローします。
3. Brazeはフォローイベントを受信し、匿名ユーザープロファイル（プロファイル2）を作成します。
4. ユーザーは[ユーザー照合](#user-id-reconciliation)を通じてLINE IDを持つユーザーとして識別されます。
5. プロファイル1を更新して`native_line_id`属性を設定します。このプロファイルはプロファイル2の購読ステータスを継承します。
  - これで、同じ`native_line_id`を持つ2つのユーザープロファイルが存在します。これらは、[ステップ5](#step-5-merge-profiles-optional)に記載されたプロセスで`/users/merge`エンドポイントを使用していつでもマージできます。

## ユーザーIDの照合 {#user-id-reconciliation}

LINE IDは、ユーザーがチャネルをフォローしたとき、または一度限りの「フォロワー同期」ワークフローを使用したときに、Brazeが自動的に受信します。LINE IDはユーザーがフォローするチャネルに固有であるため、ユーザーが自分のLINE IDを提供することはほとんどありません。

LINE IDを既存のBrazeユーザープロファイルと結合するには、次の2つの方法があります。

- [LINEログイン](#line-login)
- [ユーザーアカウントリンク](#user-account-linking)

### LINEログイン {#line-login}

この方法は、ソーシャルメディアログインを使用して照合を行います。ユーザーがアプリにログインする際、[LINEログイン](https://developers.line.biz/en/docs/line-login/overview/)を使用してユーザーアカウントを作成するか、ログインするオプションが提示されます。

{% alert note %}
各ユーザーの正しいLINE IDを取得するには、Brazeと連携しているLINE公式アカウントまたはチャネルと同じプロバイダーの下でLINEログインを設定してください。
{% endalert %}

1. LINE Developer Consoleにアクセスし、LINEログインを通じてアプリにログインしたユーザーの[メールアドレスの取得許可を申請](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)します。

2. LINEが提供する適切な手順に従ってLINEログインを実装します。<br><br>
  - [Webアプリの手順](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [ネイティブアプリの手順](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>検証リクエストの[スコープ設定](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)に`email`を含めてください。

{: start="3"}
3. [IDトークン検証呼び出し](https://developers.line.biz/en/reference/line-login/#verify-id-token)を使用して、ユーザーのメールアドレスを取得します。

4. ユーザーのLINE ID（`native_line_id`）を、データベース内で一致するメールアドレスを持つユーザーのプロファイルに保存するか、ユーザーのメールアドレスとLINE IDで新しいユーザープロファイルを作成します。

5. [`/user/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用して、新規または更新されたユーザー情報をBrazeに送信します。

#### ワークフロー {#workflows}

##### 既存のフォロワーがLINEログインを使用する場合 {#existing-follower-uses-line-login}

**シナリオ：** 初期サブスクライバー同期中、または連携後の「フォロー」イベントによって匿名ユーザーが作成されている場合。

1. ユーザーがLINEログインを使用してアプリにログインします。
2. LINEがユーザーのメールアドレスを提供します。
3. 更新されたユーザー（LINE IDを追加するために該当するメールアドレスを持つ既存のユーザープロファイル）をBrazeに送信するか、匿名ユーザーをメールアドレスで更新します。

##### 新しいフォロワーがLINEログインを使用する場合 {#new-follower-uses-line-login}

**シナリオ：** ユーザーのLINE IDを持つユーザープロファイルがBrazeに存在しない場合。

1. ユーザーがLINEログインを使用してアプリにログインします。
2. LINEがユーザーのメールアドレスを提供します。
3. 次のいずれかを行います。
  - 該当するメールアドレスを持つ既存のユーザープロファイルを更新して、ユーザーのLINE IDも含めます。
  - メールアドレスとLINE IDで新しいユーザープロファイルを作成します。
4. ユーザーがLINE公式アカウントをフォローすると、Brazeがフォローイベントを受信し、ユーザーの購読ステータスを`subscribed`に更新します。

### ユーザーアカウントリンク {#user-account-linking}

この方法では、ユーザーがLINEアカウントをアプリのユーザーアカウントにリンクできます。その後、BrazeでLiquidを使用して（{% raw %}`{{line_id}}`{% endraw %}など）、ユーザーのLINE IDをWebサイトやアプリに渡すパーソナライズされたURLを作成でき、それを既知のユーザーに関連付けることができます。

1. 購読ステータスの変更に基づくアクションベースのキャンバスを作成し、ユーザーがLINEチャネルを購読したときにトリガーされるようにします。<br>![ユーザーがLINEチャネルを購読したときにトリガーされるキャンバス。]({% image_buster /assets/img/line/account_link_1.png %})
2. ユーザーにWebサイトやアプリへのログインを促すメッセージを作成し、ユーザーのLINE IDをクエリパラメーターとして（Liquidを通じて）渡します。例：

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. クーポンコードを配信するフォローアップメッセージを作成します。
4. （オプション）LINEユーザーが特定されたときにトリガーされるアクションベースのキャンペーンまたはキャンバスを作成し、ユーザーにクーポンコードを送信します。<br>![LINEユーザーが特定されたときにトリガーされるアクションベースのキャンペーン。]({% image_buster /assets/img/line/account_link_2.png %})

#### 仕組み {#how-it-works}

ユーザーがログインした後、WebサイトまたはアプリでユーザーIDがBrazeに返送され、URLの一部として渡されたLINE IDと関連付けられるように変更が行われます。コード例は次のとおりです。

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

##### 既存ユーザーがLINEチャネルをフォローする場合 {#existing-user-follows-your-line-channel}

**シナリオ：** Brazeの既存ユーザーがLINEでチャネルをフォローする場合。

1. LINEがBrazeにフォローイベントを送信します。
2. Brazeが、LINE ID、`line_id`ユーザーエイリアス、およびLINE購読グループステータスが`subscribed`の匿名ユーザープロファイルを作成します。
3. ユーザーがWebサイトとアプリへのリンクを含むLINEメッセージを受信し、ログインします。これでユーザープロファイルが既知になります。
4. 作成された匿名ユーザープロファイルが特定され、[/users/identifyエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を通じてユーザーの既知のユーザープロファイルにマージされます。既知のユーザープロファイルにLINE IDが含まれ、購読ステータスが`subscribed`になります。
5. （オプション）ユーザーがクーポンコード付きのLINEメッセージを受信し、Brazeが送信をBrazeユーザープロファイルに記録します。

## BrazeでのLINEテストユーザーの作成 {#creating-line-test-users-in-braze}

[ユーザー照合](#user-id-reconciliation)を設定する前に、「Who am I」キャンバスまたはキャンペーンを作成してLINEチャネルをテストできます。

1. 特定のトリガーワードでユーザーのBrazeユーザーIDを返すキャンバスを設定します。<br><br>トリガーの例<br><br>![特定の購読グループにインバウンドLINEを送信したユーザーにキャンペーンを送信するトリガー。]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>メッセージの例<br><br>![BrazeユーザーIDを表示するLINEメッセージ。]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Brazeでは、Braze IDを使用して特定のユーザーを検索し、必要に応じて変更できます。

{% alert important %}
キャンバスにグローバルコントロールやコントロールグループが設定されていて送信を妨げていないことを確認してください。
{% endalert %}