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

> この記事では、ユーザーのセットアップ、ユーザー ID の照合、Brazeでの LINE テストユーザーの作成方法を含む、Brazeでの LINE チャネルのセットアップ方法について説明します。

## 前提条件 {#prerequisites}

LINE をBrazeと統合するには、以下が必要です。

- [LINE ビジネスアカウント](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- プレミアムまたは認証済みアカウントステータス（既存のフォロワーの同期に必要）
   - [LINE のアカウントガイドライン](https://terms2.line.me/official_account_guideline_oth)を参照してください
- [LINE Developers アカウント](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE Messaging API チャネル](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Brazeから LINE メッセージを送信すると、アカウントのメッセージクレジットまたはアクションクレジットが消費されます。

{% alert note %}
**`native_line_id` の設定**: Brazeにユーザー更新を送信することで `native_line_id` を設定できます（例：[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用）。クライアント側のSDKに `native_line_id` 専用のフィールドがない場合は、これらの方法のいずれかを使用してサーバー側のユーザー更新で送信してください。
{% endalert %}

## LINE アカウントの種類 {#types-of-line-accounts}

| アカウントの種類 | 説明 |
| --- | --- |
| 未認証アカウント | 誰でも（個人または法人）取得できる未審査のアカウントです。このアカウントはグレーのバッジで表示され、LINE アプリ内の検索結果には表示されません。 |
| 認証済みアカウント | LINE Yahoo の審査に合格したアカウントです。このアカウントはブルーのバッジで表示され、LINE アプリ内の検索結果に表示されます。<br><br>このアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントのみ利用可能です。 |
| プレミアムアカウント | LINE Yahoo の審査に合格したアカウントです。このアカウントはグリーンのバッジで表示され、LINE アプリ内の検索結果に表示されます。このアカウントの種類は、LINE の裁量により審査中に自動的に付与されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE アカウントの種類" }

### 必要なアカウントの種類 {#required-account-type}

フォロワーをBrazeに同期するには、LINE アカウントが認証済みまたはプレミアムである必要があります。アカウントを作成すると、デフォルトのステータスは未認証になります。アカウントの認証をリクエストする必要があります。

### 認証済み LINE アカウントの申請 {#applying-for-a-verified-line-account}

{% alert important %}
認証済みアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントのみ利用可能です。
{% endalert %}

1. LINE の**公式アカウント**ページで、**設定**を選択します。
2. **情報公開認証ステータス**の下で、**アカウント認証をリクエスト**を選択します。
3. 必要な情報を入力します。
4. 審査結果の通知を待ちます。

## LINE の統合 {#integrating-line}

一貫したユーザー更新をセットアップし、既存ユーザーの LINE ID を取り込み、LINE のサブスクリプション状態にすべて同期するには：

1. [既存の既知のユーザーをインポートまたは更新する](#step-1-import-or-update-existing-line-users)
2. [LINE チャネルを統合する](#step-2-integrate-line-channel)
3. [ユーザー ID を照合する](#step-3-reconcile-user-ids)
4. [ユーザー更新方法を変更する](#step-4-change-your-user-update-methods)
5. [（オプション）ユーザープロファイルをマージする](#step-5-merge-profiles-optional)

{% alert note %}
1つのワークスペースには1つの LINE アカウントのみ設定できます。複数の LINE アカウントがある場合は、それぞれを異なるワークスペースで使用することをお勧めします。
{% endalert %}

## ステップ 1: 既存の LINE ユーザーをインポートまたは更新する {#step-1-import-or-update-existing-line-users}

このステップは、既存の識別済み LINE ユーザーがいる場合に必要です。Brazeが後でサブスクリプション状態を自動的に取得し、正しいユーザープロファイルを更新するためです。以前にユーザーと LINE ID を照合していない場合は、このステップをスキップしてください。

Brazeがサポートする任意の方法を使用してユーザーをインポートまたは更新できます。[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)が利用可能です。

使用する方法に関係なく、`native_line_id` を更新してユーザーの LINE ID を提供してください。`native_line_id` の詳細については、[ユーザーセットアップ](#user-setup)を参照してください。

{% alert note %}
サブスクリプショングループの状態は指定する必要がなく、指定しても無視されます。LINE がユーザーのサブスクリプションステータスの信頼できるソースであり、サブスクリプション同期ツールまたはイベント更新を通じてBrazeに同期されます。
{% endalert %}

## ステップ 2: LINE チャネルを統合する {#step-2-integrate-line-channel}

統合プロセスが完了すると、Brazeはそのチャネルの LINE フォロワーを自動的にBrazeに取り込みます。すでにBrazeユーザープロファイルに関連付けられている LINE ID については、各プロファイルが「購読中」ステータスに更新され、残りの LINE ID については匿名ユーザーが生成されます。さらに、LINE チャネルの新しいフォロワーは、チャネルをフォローした際に未識別のユーザープロファイルが作成されます。

### ステップ 2.1: Webhook 設定を編集する {#step-21-edit-webhook-settings}

1. LINE で **Messaging API** タブに移動し、**Webhook 設定**を編集します：
   - **Webhook URL** を `https://anna.braze.com/line/events` に設定します。
      - Brazeは統合時に、ダッシュボードクラスターに基づいてこれを自動的に別の URL に変更します。
   - **Webhookの利用**と**Webhookの再送**をオンにします。<br><br> ![Webhook URL の確認または編集、「Webhookの利用」、「Webhookの再送」、「エラー統計の集計」のオン/オフを切り替える Webhook 設定ページ。]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. **プロバイダー**タブで以下の情報をメモしてください：

| 情報の種類 | 場所 |
| --- | --- |
| プロバイダー ID | プロバイダーを選択し、**設定** > **基本情報**に移動します |
| チャネル ID | プロバイダーを選択し、**チャネル** > 対象のチャネル > **基本設定**に移動します |
| チャネルシークレット | プロバイダーを選択し、**チャネル** > 対象のチャネル > **基本設定**に移動します |
| チャネルアクセストークン | プロバイダーを選択し、**チャネル** > 対象のチャネル > **Messaging API** に移動します。チャネルアクセストークンがない場合は、**発行**を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ 2.1: Webhook 設定を編集する" }

{% alert note %}
すでに統合済みの LINE チャネルのチャネルシークレットを更新またはローテーションする必要がある場合は、[Brazeサポート]({{site.baseurl}}/braze_support)に連絡して更新をリクエストしてください。
{% endalert %}

{: start="3"}
3. **設定**ページ > **応答設定**に移動し、以下を行います：
   - **あいさつメッセージ**をオフにします。これはBrazeでフォロー時のトリガーで処理できます。
   - **自動応答メッセージ**をオフにします。すべてのトリガーメッセージングはBrazeを通じて行う必要があります。これにより、LINE コンソールから直接送信することは妨げられません。
   - **Webhook** をオンにします。

![チャットの処理方法を切り替える応答設定ページ。]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### ステップ 2.2: Brazeで LINE サブスクリプショングループを生成する {#step-22-generate-line-subscription-groups-in-braze}

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. Brazeのテクノロジーパートナーページで LINE に移動し、LINE の**プロバイダー**タブからメモした情報を入力します：
   - プロバイダー ID
   - チャネル ID
   - チャネルシークレット
   - チャネルアクセストークン

LINE アカウントに IP ホワイトリストを追加する場合は、[IP 許可リスト]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)に記載されているクラスターのすべての IP アドレスを許可リストに追加してください。

{% alert important %}
統合時に、チャネルシークレットが正しいことを必ず確認してください。正しくない場合、サブスクリプションステータスに不整合が生じる可能性があります。
{% endalert %}

![LINE 統合セクションを含む LINE メッセージング統合ページ。]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. 接続後、Brazeはワークスペースに正常に追加された各 LINE 統合に対して、Brazeサブスクリプショングループを自動的に生成します。<br><br> フォロワーリストへの変更（新しいフォロワーやフォロー解除など）は、自動的にBrazeにプッシュされます。

![「LINE」チャネルの1つのサブスクリプショングループを表示する LINE サブスクリプショングループセクション。]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## ステップ 3: ユーザー ID を照合する {#step-3-reconcile-user-ids}

[ユーザー ID の照合](#user-id-reconciliation)の手順に従って、ユーザーの LINE ID を既存のBrazeユーザープロファイルと結合します。

## ステップ 4: ユーザー更新方法を変更する {#step-4-change-your-user-update-methods}

すでにBrazeにユーザー更新を提供する方法がある場合、新しいフィールド `native_line_id` を含めるように更新する必要があります。これにより、Brazeに送信される後続のユーザー更新にそのフィールドが含まれるようになります。

サブスクリプションステータスの同期プロセスの一部として、または新しいフォロワーがチャネルをフォローした際に、`native_line_id` を持つ未識別のユーザープロファイルがBrazeに存在する場合があります。

LINE ユーザーが[ユーザー照合](#user-id-reconciliation)やその他の手段でアプリケーション内で識別された場合、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) エンドポイントを使用して、Braze内の潜在的な未識別ユーザープロファイルをターゲットにできます。`native_line_id` を持つすべての未識別ユーザープロファイルには、ユーザープロファイルを識別するためにターゲットにできるユーザーエイリアス `line_id` もあります。

以下は、ユーザーエイリアス `line_id` で未識別ユーザープロファイルをターゲットにする `/users/identify` へのペイロードの例です：

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

指定した `external_id` に対して既存のユーザープロファイルが存在しない場合、未識別のユーザープロファイルに追加され、識別済みになります。`external_id` に対してユーザープロファイルが存在する場合、未識別のユーザープロファイルにのみ存在するすべての属性（`native_line_id` やユーザーのサブスクリプションステータスを含む）が既知のユーザープロファイルにコピーされます。

アプリケーションで既知の LINE ユーザーは、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイントを通じて、外部識別子と `native_line_id` を渡すことで更新できます。ユーザーに対して未識別のユーザープロファイルがすでに存在し、同じ `native_line_id` が `/users/track` を通じて別のユーザープロファイルに追加された場合、未識別のユーザープロファイルのすべてのサブスクリプション状態を継承します。ただし、同じ `native_line_id` を持つ重複したユーザープロファイルが存在することになります。イベント更新による後続のサブスクリプション更新は、すべてのプロファイルを適切に更新します。

{% alert note %}
LINE のサブスクリプション状態は `external_id` ではなく `native_line_id` で追跡されます。例えば、ユーザー B のユーザープロファイルがユーザー A と同じ `native_line_id` で作成されたが、同じ `external_id` ではない場合、ユーザー B はユーザー A の LINE サブスクリプションステータスを継承します。
{% endalert %}

以下は、外部ユーザー ID でユーザープロファイルを更新して `native_line_id` を追加する `/users/track` へのペイロードの例です：

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

## ステップ 5: プロファイルをマージする（オプション） {#step-5-merge-profiles-optional}

上記のとおり、同じ `native_line_id` を持つ複数のユーザープロファイルが存在する可能性があります。更新方法によって重複したユーザープロファイルが作成された場合、`/user/merge` エンドポイントを使用して、未識別のユーザープロファイルを識別済みのユーザープロファイルにマージできます。

以下は、ユーザーエイリアス `line_id` で未識別ユーザープロファイルをターゲットにする `/users/merge` へのペイロードの例です：

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

## ユーザーセットアップ {#user-setup}

LINE はユーザーのサブスクリプション状態の信頼できるソースです。ユーザーの LINE ID（`native_line_id`）を持っていても、そのユーザーが送信元の LINE チャネルをフォローしていない場合、LINE はそのユーザーにメッセージを配信しません。

これを管理するために、Brazeはサブスクリプション同期や LINE のフォロー/フォロー解除のイベント更新など、適切に統合されたユーザー群をサポートするツールとロジックを提供しています。

### サブスクリプション同期とイベントロジック {#subscription-syncing-and-event-logic}

1. **サブスクリプション同期ツール:** このツールは、LINE チャネルの統合が成功した後に自動的にデプロイされます。既存のプロファイルの更新や新しいプロファイルの作成に使用します。<br><br>LINE チャネルをフォローしている `native_line_id` を持つすべてのBrazeユーザープロファイルは、サブスクリプショングループのステータスが `subscribed` に更新されます。`native_line_id` を持つBrazeユーザープロファイルがない LINE チャネルのフォロワーには、以下が適用されます：<br><br>- チャネルをフォローしているユーザーの LINE ID に `native_line_id` が設定された匿名ユーザープロファイルが作成されます<br>- チャネルをフォローしているユーザーの LINE ID にユーザーエイリアス `line_id` が設定されます<br>- サブスクリプショングループのステータスが `subscribed` になります

{: start="2"}
2. **イベント更新:** ユーザーのサブスクリプションステータスの更新に使用されます。Brazeが統合された LINE チャネルのユーザーイベント更新を受信し、そのイベントがフォローの場合、ユーザープロファイルのサブスクリプショングループのステータスは `subscribed` になります。イベントがフォロー解除の場合、ユーザープロファイルのサブスクリプショングループのステータスは `unsubscribed` になります。<br><br>- 一致する `native_line_id` を持つすべてのBrazeユーザープロファイルが自動的に更新されます。<br>- イベントに一致するユーザープロファイルが存在しない場合、Brazeは[匿名ユーザーを作成]({{site.baseurl}}/line/user_management)します。

## ユースケース {#use-cases}

上記のセットアップ手順に従った後、ユーザーがどのように更新されるかのユースケースです。

### 既存のBrazeユーザープロファイルがすでに LINE チャネルをフォローしている場合 {#existing-braze-user-profile-already-follows-line-channel}

1. Brazeユーザープロファイルが `native_line_id` 属性で更新されます。デフォルトのサブスクリプションステータスは `unsubscribed` です。
2. サブスクリプション同期ツールが実行され、ユーザーが LINE チャネルをフォローしていることを検出し、ユーザープロファイルをサブスクリプションステータス `subscribed` で更新します。
3. サブスクリプションステータスの変更が発生した場合（ユーザーがブロック、友だち解除、または再フォローした場合など）、Brazeは LINE から更新を受信し、`native_line_id` に応じてユーザープロファイルを更新します。

#### 既存のユーザープロファイルが LINE チャネルをブロック、友だち解除、またはフォロー解除している場合 {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. Brazeユーザープロファイルが `native_line_id` 属性で更新されます。デフォルトのサブスクリプションステータスは `unsubscribed` です。
2. サブスクリプション同期ツールはユーザーが LINE チャネルをフォローしていることを検出せず、ユーザーのサブスクリプションステータスは `unsubscribed` のままです。
3. ユーザーが後でチャネルをフォローした場合、Brazeは LINE から更新を受信し、ユーザープロファイルをサブスクリプションステータス `subscribed` で更新します。

##### LINE フォロー後にユーザープロファイルが作成される場合 {#user-profile-creation-occurs-after-line-follow}

1. チャネルに新しい LINE フォロワーが追加されます。
2. Brazeは、フォロワーの LINE ID に `native_line_id` 属性が設定され、フォロワーの LINE ID にユーザーエイリアス `line_id` が設定された匿名ユーザープロファイルを作成します。プロファイルのサブスクリプションステータスは `subscribed` です。
3. [ユーザー照合](#user-id-reconciliation)を通じて、ユーザーが LINE ID を持っていることが識別されます。
  - 匿名ユーザープロファイルは、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) エンドポイントを使用して識別済みにできます。このユーザープロファイルへの後続の更新（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を通じて）は、この既知の `external_id` でユーザーをターゲットにできます。

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

  - 新しいユーザープロファイルは、`native_line_id` を設定することで（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) エンドポイント、[CSV インポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を通じて）作成できます。この新しいプロファイルは、既存の匿名ユーザープロファイルのサブスクリプション状態を継承します。これにより、同じ `native_line_id` を共有する複数のプロファイルが存在することになります。これらは、[ステップ 5](#step-5-merge-profiles-optional) で説明されているプロセスで `/users/merge` エンドポイントを使用していつでもマージできます。

##### LINE フォロー前にユーザープロファイルが作成される場合 {#user-profile-creation-occurs-before-line-follow}

1. 新しいユーザーを獲得し、情報をBrazeに送信します。新しいユーザープロファイルが作成されます（プロファイル 1）。
2. ユーザーが LINE アカウントをフォローします。
3. Brazeはフォローイベントを受信し、匿名ユーザープロファイルを作成します（プロファイル 2）。
4. [ユーザー照合](#user-id-reconciliation)を通じて、ユーザーが LINE ID を持っていることが識別されます。
5. プロファイル 1 を更新して `native_line_id` 属性を設定します。このプロファイルはプロファイル 2 のサブスクリプション状態を継承します。
  - これで、同じ `native_line_id` を持つ2つのユーザープロファイルが存在します。これらは、[ステップ 5](#step-5-merge-profiles-optional) で説明されているプロセスで `/users/merge` エンドポイントを使用していつでもマージできます。

## ユーザー ID の照合 {#user-id-reconciliation}

LINE ID は、ユーザーがチャネルをフォローした際、または一回限りの「フォロワー同期」ワークフローを使用した際に、Brazeによって自動的に受信されます。LINE ID はユーザーがフォローするチャネルに固有であるため、ユーザーが自分の LINE ID を提供できる可能性は低いです。

LINE ID を既存のBrazeユーザープロファイルと結合するには、2つの方法があります：

- [LINE ログイン](#line-login)
- [ユーザーアカウントリンク](#user-account-linking)

### LINE ログイン {#line-login}

この方法では、ソーシャルメディアログインを使用して照合を行います。ユーザーがアプリにログインすると、[LINE ログイン](https://developers.line.biz/en/docs/line-login/overview/)を使用してユーザーアカウントを作成するか、ログインするオプションが提供されます。

{% alert note %}
各ユーザーの正しい LINE ID を取得するには、Brazeと統合された LINE 公式アカウントまたはチャネルと同じプロバイダーの下で LINE ログインをセットアップしてください。
{% endalert %}

1. LINE Developer Console に移動し、LINE ログインを通じてアプリにログインするユーザーの[メールアドレスを取得する権限をリクエスト](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)します。

2. LINE が提供する適切な手順に従って LINE ログインを実装します：<br><br>
  - [Web アプリの手順](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [ネイティブアプリの手順](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>認証リクエストの[スコープ設定](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)に `email` を含めるようにしてください。

{: start="3"}
3. [ID トークンの検証呼び出し](https://developers.line.biz/en/reference/line-login/#verify-id-token)を使用して、ユーザーのメールアドレスを取得します。

4. ユーザーの LINE ID（`native_line_id`）を、データベース内の一致するメールアドレスを持つユーザーのプロファイルに保存するか、ユーザーのメールアドレスと LINE ID で新しいユーザープロファイルを作成します。

5. 新しいまたは更新されたユーザー情報を、[`/user/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users)、[CSV インポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#csv-import)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用してBrazeに送信します。

#### ワークフロー {#workflows}

##### 既存のフォロワーが LINE ログインを使用する場合 {#existing-follower-uses-line-login}

**シナリオ:** 初回のサブスクライバー同期中、または統合後の「フォロー」イベントを通じて匿名ユーザーが作成されました。

1. ユーザーが LINE ログインを使用してアプリにログインします。
2. LINE がユーザーのメールアドレスを提供します。
3. 更新されたユーザー（LINE ID を追加するためのそのメールアドレスを持つ既存のユーザープロファイル）をBrazeに送信するか、匿名ユーザーをメールアドレスで更新します。

##### 新しいフォロワーが LINE ログインを使用する場合 {#new-follower-uses-line-login}

**シナリオ:** ユーザーの LINE ID を持つユーザープロファイルがBrazeに存在しません。

1. ユーザーが LINE ログインを使用してアプリにログインします。
2. LINE がユーザーのメールアドレスを提供します。
3. 以下のいずれかを行います：
  - そのメールアドレスを持つ既存のユーザープロファイルを更新して、ユーザーの LINE ID も含めます。
  - メールアドレスと LINE ID で新しいユーザープロファイルを作成します。
4. ユーザーが LINE 公式アカウントをフォローすると、Brazeはフォローイベントを受信し、ユーザーのサブスクリプションステータスを `subscribed` に更新します。

### ユーザーアカウントリンク {#user-account-linking}

この方法では、ユーザーが LINE アカウントをアプリのユーザーアカウントにリンクできます。Brazeで {% raw %}`{{line_id}}`{% endraw %} などのLiquidを使用して、ユーザーの LINE ID をWebサイトやアプリに渡すパーソナライズされた URL を作成し、既知のユーザーに関連付けることができます。

1. サブスクリプション状態の変更に基づくアクションベースのキャンバスを作成し、ユーザーが LINE チャネルを購読した際にトリガーされるようにします。<br>![ユーザーが LINE チャネルを購読した際にトリガーされるキャンバス。]({% image_buster /assets/img/line/account_link_1.png %})
2. ユーザーにWebサイトやアプリへのログインを促すメッセージを作成し、ユーザーの LINE ID をクエリパラメーターとして（Liquidを通じて）渡します。例：

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. クーポンコードを配信するフォローアップメッセージを作成します。
4. （オプション）LINE ユーザーが識別された際にトリガーされるアクションベースのキャンペーンまたはキャンバスを作成し、ユーザーにクーポンコードを送信します。<br>![LINE ユーザーが識別された際にトリガーされるアクションベースのキャンペーン。]({% image_buster /assets/img/line/account_link_2.png %})

#### 仕組み {#how-it-works}

ユーザーがログインすると、Webサイトまたはアプリで変更が行われ、URL の一部として渡された LINE ID と関連付けるためにユーザー ID がBrazeに送信されます。コード例は以下のとおりです：

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

##### 既存のユーザーが LINE チャネルをフォローする場合 {#existing-user-follows-your-line-channel}

**シナリオ:** Brazeの既存ユーザーが LINE でチャネルをフォローします。

1. LINE がBrazeにフォローイベントを送信します。
2. Brazeは LINE ID、`line_id` ユーザーエイリアス、および LINE サブスクリプショングループのステータス `subscribed` を持つ匿名ユーザープロファイルを作成します。
3. ユーザーがWebサイトやアプリへのリンクを含む LINE メッセージを受信し、ログインします。ユーザープロファイルが既知になります。
4. 作成された匿名ユーザープロファイルが識別され、[/users/identify エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を通じてユーザーの既知のユーザープロファイルにマージされます。既知のユーザープロファイルに LINE ID が含まれ、サブスクリプションステータスが `subscribed` になります。
5. （オプション）ユーザーがクーポンコードを含む LINE メッセージを受信し、BrazeがBrazeユーザープロファイルに送信を記録します。

## Brazeでの LINE テストユーザーの作成 {#creating-line-test-users-in-braze}

[ユーザー照合](#user-id-reconciliation)をセットアップする前に、「Who am I」キャンバスまたはキャンペーンを作成して LINE チャネルをテストできます。

1. 特定のトリガーワードでユーザーのBrazeユーザー ID を返すキャンバスをセットアップします。<br><br>トリガーの例<br><br>![特定のサブスクリプショングループにインバウンド LINE を送信したユーザーにキャンペーンを送信するトリガー。]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>メッセージの例<br><br>![Brazeユーザー ID を表示する LINE メッセージ。]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Brazeで、Braze ID を使用して特定のユーザーを検索し、必要に応じて変更できます。

{% alert important %}
キャンバスにグローバルコントロールやコントロールグループが送信を妨げていないことを確認してください。
{% endalert %}