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

LINEをBrazeと統合するには、以下が必要です。

- [LINEビジネスアカウント](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- プレミアムまたは認証済みアカウントステータス（既存のフォロワーの同期に必要）
   - [LINEのアカウントガイドライン](https://terms2.line.me/official_account_guideline_oth)を参照してください
- [LINE Developersアカウント](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE Messaging APIチャネル](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

BrazeからLINEメッセージを送信すると、アカウントのメッセージクレジットまたはアクションクレジットが消費されます。

{% alert note %}
**`native_line_id`の設定**: Brazeにユーザー更新を送信することで`native_line_id`を設定できます（例：[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用）。クライアント側のSDKに`native_line_id`専用のフィールドがない場合は、これらの方法のいずれかを使用してサーバー側のユーザー更新で送信してください。
{% endalert %}

## LINEアカウントの種類 {#types-of-line-accounts}

| アカウントの種類 | 説明 |
| --- | --- |
| 未認証アカウント | 誰でも（個人または法人）取得できる未審査のアカウントです。このアカウントはグレーのバッジで表示され、LINEアプリ内の検索結果には表示されません。 |
| 認証済みアカウント | LINE Yahooの審査に合格したアカウントです。このアカウントはブルーのバッジで表示され、LINEアプリ内の検索結果に表示されます。<br><br>このアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントのみ利用可能です。 |
| プレミアムアカウント | LINE Yahooの審査に合格したアカウントです。このアカウントはグリーンのバッジで表示され、LINEアプリ内の検索結果に表示されます。このアカウントの種類は、LINEの裁量により審査中に自動的に付与されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINEアカウントの種類" }

### 必要なアカウントの種類 {#required-account-type}

フォロワーをBrazeに同期するには、LINEアカウントが認証済みまたはプレミアムである必要があります。アカウントを作成すると、デフォルトのステータスは未認証になります。アカウントの認証をリクエストする必要があります。

### 認証済みLINEアカウントの申請 {#applying-for-a-verified-line-account}

{% alert important %}
認証済みアカウントは、日本、台湾、タイ、インドネシアに拠点を置くアカウントのみ利用可能です。
{% endalert %}

1. LINEの**公式アカウント**ページで、**設定**を選択します。
2. **情報公開認証ステータス**の下で、**アカウント認証をリクエスト**を選択します。
3. 必要な情報を入力します。
4. 審査結果の通知を待ちます。

## LINEの統合 {#integrating-line}

一貫したユーザー更新をセットアップし、既存ユーザーのLINE IDを取り込み、LINEの購読状態にすべて同期するには：

1. [既存の既知のユーザーをインポートまたは更新する](#step-1-import-or-update-existing-line-users)
2. [LINEチャネルを統合する](#step-2-integrate-line-channel)
3. [ユーザーIDを照合する](#step-3-reconcile-user-ids)
4. [ユーザー更新方法を変更する](#step-4-change-your-user-update-methods)
5. [（オプション）ユーザープロファイルをマージする](#step-5-merge-profiles-optional)

{% alert note %}
1つのワークスペースには1つのLINEアカウントのみ設定できます。複数のLINEアカウントがある場合は、それぞれを異なるワークスペースで使用することをお勧めします。
{% endalert %}

## ステップ1:既存のLINEユーザーをインポートまたは更新する {#step-1-import-or-update-existing-line-users}

このステップは、既存の識別済みLINEユーザーがいる場合に必要です。Brazeが後で購読状態を自動的に取得し、正しいユーザープロファイルを更新するためです。以前にユーザーとLINE IDを照合していない場合は、このステップをスキップしてください。

Brazeがサポートする任意の方法を使用してユーザーをインポートまたは更新できます。[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)が利用可能です。

使用する方法に関係なく、`native_line_id`を更新してユーザーのLINE IDを提供してください。`native_line_id`の詳細については、[ユーザーセットアップ](#user-setup)を参照してください。

{% alert note %}
購読グループの状態は指定する必要がなく、指定しても無視されます。LINEがユーザーの購読ステータスの信頼できるソースであり、購読同期ツールまたはイベント更新を通じてBrazeに同期されます。
{% endalert %}

## ステップ2:LINEチャネルを統合する {#step-2-integrate-line-channel}

統合プロセスが完了すると、Brazeはそのチャネルの LINEフォロワーを自動的にBrazeに取り込みます。すでにBrazeユーザープロファイルに関連付けられているLINE IDについては、各プロファイルが「購読中」ステータスに更新され、残りのLINE IDについては匿名ユーザーが生成されます。さらに、LINEチャネルの新しいフォロワーは、チャネルをフォローした際に未識別のユーザープロファイルが作成されます。

### ステップ2.1:Webhook設定を編集する {#step-21-edit-webhook-settings}

1. LINEで**Messaging API**タブに移動し、**Webhook設定**を編集します：
   - **Webhook URL**を`https://anna.braze.com/line/events`に設定します。
      - Brazeは統合時に、ダッシュボードクラスターに基づいてこれを自動的に別のURLに変更します。
   - **Webhookの利用**と**Webhookの再送**をオンにします。<br><br> ![Webhook URLの確認または編集、「Webhookの利用」、「Webhookの再送」、「エラー統計の集計」のオン/オフを切り替えるWebhook設定ページ。]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. **プロバイダー**タブで以下の情報をメモしてください：

| 情報の種類 | 場所 |
| --- | --- |
| プロバイダーID | プロバイダーを選択し、**設定** > **基本情報**に移動します |
| チャネルID | プロバイダーを選択し、**チャネル** > 対象のチャネル > **基本設定**に移動します |
| チャネルシークレット | プロバイダーを選択し、**チャネル** > 対象のチャネル > **基本設定**に移動します |
| チャネルアクセストークン | プロバイダーを選択し、**チャネル** > 対象のチャネル > **Messaging API**に移動します。チャネルアクセストークンがない場合は、**発行**を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2.1:Webhook設定を編集する" }

{% alert note %}
すでに統合済みのLINEチャネルのチャネルシークレットを更新またはローテーションする必要がある場合は、[Brazeサポート]({{site.baseurl}}/braze_support)に連絡して更新をリクエストしてください。
{% endalert %}

{: start="3"}
3. **設定**ページ > **応答設定**に移動し、以下を行います：
   - **あいさつメッセージ**をオフにします。これはBrazeでフォロー時のトリガーで処理できます。
   - **自動応答メッセージ**をオフにします。すべてのトリガーメッセージングはBrazeを通じて行う必要があります。これにより、LINEコンソールから直接送信することは妨げられません。
   - **Webhook**をオンにします。

![チャットの処理方法を切り替える応答設定ページ。]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### ステップ2.2:BrazeでLINE購読グループを生成する {#step-22-generate-line-subscription-groups-in-braze}

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

1. BrazeのテクノロジーパートナーページでLINEに移動し、LINEの**プロバイダー**タブからメモした情報を入力します：
   - プロバイダーID
   - チャネルID
   - チャネルシークレット
   - チャネルアクセストークン

LINEアカウントにIPホワイトリストを追加する場合は、[IP許可リスト]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting)に記載されているクラスターのすべてのIPアドレスを許可リストに追加してください。

{% alert important %}
統合時に、チャネルシークレットが正しいことを必ず確認してください。正しくない場合、購読ステータスに不整合が生じる可能性があります。
{% endalert %}

![LINE統合セクションを含むLINEメッセージング統合ページ。]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. 接続後、Brazeはワークスペースに正常に追加された各LINE統合に対して、Braze購読グループを自動的に生成します。<br><br>フォロワーリストへの変更（新しいフォロワーやフォロー解除など）は、自動的にBrazeにプッシュされます。

![「LINE」チャネルの1つの購読グループを表示するLINE購読グループセクション。]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## ステップ3:ユーザーIDを照合する {#step-3-reconcile-user-ids}

[ユーザーIDの照合](#user-id-reconciliation)の手順に従って、ユーザーのLINE IDを既存のBrazeユーザープロファイルと結合します。

## ステップ4:ユーザー更新方法を変更する {#step-4-change-your-user-update-methods}

すでにBrazeにユーザー更新を提供する方法がある場合、新しいフィールド`native_line_id`を含めるように更新する必要があります。これにより、Brazeに送信される後続のユーザー更新にそのフィールドが含まれるようになります。

購読ステータスの同期プロセスの一部として、または新しいフォロワーがチャネルをフォローした際に、`native_line_id`を持つ未識別のユーザープロファイルがBrazeに存在する場合があります。

LINEユーザーが[ユーザー照合](#user-id-reconciliation)やその他の手段でアプリケーション内で識別された場合、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントを使用して、Braze内の潜在的な未識別ユーザープロファイルをターゲットにできます。`native_line_id`を持つすべての未識別ユーザープロファイルには、ユーザープロファイルを識別するためにターゲットにできるユーザーエイリアス`line_id`もあります。

以下は、ユーザーエイリアス`line_id`で未識別ユーザープロファイルをターゲットにする`/users/identify`へのペイロードの例です：

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

指定した`external_id`に対して既存のユーザープロファイルが存在しない場合、未識別のユーザープロファイルに追加され、識別済みになります。`external_id`に対してユーザープロファイルが存在する場合、未識別のユーザープロファイルにのみ存在するすべての属性（`native_line_id`やユーザーの購読ステータスを含む）が既知のユーザープロファイルにコピーされます。

アプリケーションで既知のLINEユーザーは、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントを通じて、外部識別子と`native_line_id`を渡すことで更新できます。ユーザーに対して未識別のユーザープロファイルがすでに存在し、同じ`native_line_id`が`/users/track`を通じて別のユーザープロファイルに追加された場合、未識別のユーザープロファイルのすべての購読状態を継承します。ただし、同じ`native_line_id`を持つ重複したユーザープロファイルが存在することになります。イベント更新による後続の購読更新は、すべてのプロファイルを適切に更新します。

{% alert note %}
LINEの購読状態は`external_id`ではなく`native_line_id`で追跡されます。例えば、ユーザーBのユーザープロファイルがユーザーAと同じ`native_line_id`で作成されたが、同じ`external_id`ではない場合、ユーザーBはユーザーAのLINE購読ステータスを継承します。
{% endalert %}

以下は、外部ユーザーIDでユーザープロファイルを更新して`native_line_id`を追加する`/users/track`へのペイロードの例です：

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

## ステップ5:プロファイルをマージする（オプション） {#step-5-merge-profiles-optional}

このセクションで前述したとおり、同じ`native_line_id`を持つ複数のユーザープロファイルが存在する可能性があります。更新方法によって重複したユーザープロファイルが作成された場合、`/user/merge`エンドポイントを使用して、未識別のユーザープロファイルを識別済みのユーザープロファイルにマージできます。

以下は、ユーザーエイリアス`line_id`で未識別ユーザープロファイルをターゲットにする`/users/merge`へのペイロードの例です：

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

LINEはユーザーの購読状態の信頼できるソースです。ユーザーのLINE ID（`native_line_id`）を持っていても、そのユーザーが送信元のLINEチャネルをフォローしていない場合、LINEはそのユーザーにメッセージを配信しません。

これを管理するために、Brazeは購読同期やLINEのフォロー/フォロー解除のイベント更新など、適切に統合されたユーザー群をサポートするツールとロジックを提供しています。

### 購読同期とイベントロジック {#subscription-syncing-and-event-logic}

1. **購読同期ツール:** このツールは、LINEチャネルの統合が成功した後に自動的にデプロイされます。既存のプロファイルの更新や新しいプロファイルの作成に使用します。<br><br>LINEチャネルをフォローしている`native_line_id`を持つすべてのBrazeユーザープロファイルは、購読グループのステータスが`subscribed`に更新されます。`native_line_id`を持つBrazeユーザープロファイルがないLINEチャネルのフォロワーには、以下が適用されます：<br><br>- チャネルをフォローしているユーザーのLINE IDに`native_line_id`が設定された匿名ユーザープロファイルが作成されます<br>- チャネルをフォローしているユーザーのLINE IDにユーザーエイリアス`line_id`が設定されます<br>- 購読グループのステータスが`subscribed`になります

{: start="2"}
2. **イベント更新:** ユーザーの購読ステータスの更新に使用されます。Brazeが統合されたLINEチャネルのユーザーイベント更新を受信し、そのイベントがフォローの場合、ユーザープロファイルの購読グループのステータスは`subscribed`になります。イベントがフォロー解除の場合、ユーザープロファイルの購読グループのステータスは`unsubscribed`になります。<br><br>- 一致する`native_line_id`を持つすべてのBrazeユーザープロファイルが自動的に更新されます。<br>- イベントに一致するユーザープロファイルが存在しない場合、Brazeは[匿名ユーザーを作成]({{site.baseurl}}/line/user_management)します。

## 別のワークスペースでLINEチャネルを再統合する {#re-integrate-a-line-channel-in-another-workspace}

LINEチャネルを別のBrazeワークスペースで使用するには：

1. 元のワークスペースで、そのチャネルの購読グループをアーカイブします。
2. ターゲットのワークスペースで、[ステップ2:LINEチャネルを統合する](#step-2-integrate-line-channel)を使用してチャネルを統合します。

両方のワークスペースで[購読グループの管理]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions)権限があることを確認してください。両方のワークスペースで権限がない場合、チャネルがすでに接続されていることを示すエラーで統合が失敗します。

アーカイブが購読グループに与える影響については、[LINE購読グループ]({{site.baseurl}}/line/subscription_groups#archive-behavior)を参照してください。

## ユースケース {#use-cases}

セットアップ手順に従った後、ユーザーがどのように更新されるかのユースケースです。

### 既存のBrazeユーザープロファイルがすでにLINEチャネルをフォローしている場合 {#existing-braze-user-profile-already-follows-line-channel}

1. Brazeユーザープロファイルが`native_line_id`属性で更新されます。デフォルトの購読ステータスは`unsubscribed`です。
2. 購読同期ツールが実行され、ユーザーがLINEチャネルをフォローしていることを検出し、ユーザープロファイルを購読ステータス`subscribed`で更新します。
3. 購読ステータスの変更が発生した場合（ユーザーがブロック、友だち解除、または再フォローした場合など）、BrazeはLINEから更新を受信し、`native_line_id`に応じてユーザープロファイルを更新します。

### 既存のユーザープロファイルがLINEチャネルをブロック、友だち解除、またはフォロー解除している場合 {#existing-user-profile-has-blocked-unfriended-or-unfollowed-line-channel}

1. Brazeユーザープロファイルが`native_line_id`属性で更新されます。デフォルトの購読ステータスは`unsubscribed`です。
2. 購読同期ツールはユーザーがLINEチャネルをフォローしていることを検出せず、ユーザーの購読ステータスは`unsubscribed`のままです。
3. ユーザーが後でチャネルをフォローした場合、BrazeはLINEから更新を受信し、ユーザープロファイルを購読ステータス`subscribed`で更新します。

### LINEフォロー後にユーザープロファイルが作成される場合 {#user-profile-creation-occurs-after-line-follow}

1. チャネルに新しいLINEフォロワーが追加されます。
2. Brazeは、フォロワーのLINE IDに`native_line_id`属性が設定され、フォロワーのLINE IDにユーザーエイリアス`line_id`が設定された匿名ユーザープロファイルを作成します。プロファイルの購読ステータスは`subscribed`です。
3. [ユーザー照合](#user-id-reconciliation)を通じて、ユーザーがLINE IDを持っていることが識別されます。
  - 匿名ユーザープロファイルは、[`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)エンドポイントを使用して識別済みにできます。このユーザープロファイルへの後続の更新（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を通じて）は、この既知の`external_id`でユーザーをターゲットにできます。

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

  - 新しいユーザープロファイルは、`native_line_id`を設定することで（[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイント、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を通じて）作成できます。この新しいプロファイルは、既存の匿名ユーザープロファイルの購読状態を継承します。これにより、同じ`native_line_id`を共有する複数のプロファイルが存在することになります。これらは、[ステップ5](#step-5-merge-profiles-optional)で説明されているプロセスで`/users/merge`エンドポイントを使用していつでもマージできます。

### LINEフォロー前にユーザープロファイルが作成される場合 {#user-profile-creation-occurs-before-line-follow}

1. 新しいユーザーを獲得し、情報をBrazeに送信します。新しいユーザープロファイルが作成されます（プロファイル1）。
2. ユーザーがLINEアカウントをフォローします。
3. Brazeはフォローイベントを受信し、匿名ユーザープロファイルを作成します（プロファイル2）。
4. [ユーザー照合](#user-id-reconciliation)を通じて、ユーザーがLINE IDを持っていることが識別されます。
5. プロファイル1を更新して`native_line_id`属性を設定します。このプロファイルはプロファイル2の購読状態を継承します。
  - これで、同じ`native_line_id`を持つ2つのユーザープロファイルが存在します。これらは、[ステップ5](#step-5-merge-profiles-optional)で説明されているプロセスで`/users/merge`エンドポイントを使用していつでもマージできます。

## ユーザーIDの照合 {#user-id-reconciliation}

LINE IDは、ユーザーがチャネルをフォローした際、または一回限りの「フォロワー同期」ワークフローを使用した際に、Brazeによって自動的に受信されます。LINE IDはユーザーがフォローするチャネルに固有であるため、ユーザーが自分のLINE IDを提供できる可能性は低いです。

LINE IDを既存のBrazeユーザープロファイルと結合するには、2つの方法があります：

- [LINEログイン](#line-login)
- [ユーザーアカウントリンク](#user-account-linking)

### LINEログイン {#line-login}

この方法では、ソーシャルメディアログインを使用して照合を行います。ユーザーがアプリにログインすると、[LINEログイン](https://developers.line.biz/en/docs/line-login/overview/)を使用してユーザーアカウントを作成するか、ログインするオプションが提供されます。

{% alert note %}
各ユーザーの正しいLINE IDを取得するには、Brazeと統合されたLINE公式アカウントまたはチャネルと同じプロバイダーの下でLINEログインをセットアップしてください。
{% endalert %}

1. LINE Developer Consoleに移動し、LINEログインを通じてアプリにログインするユーザーの[メールアドレスを取得する権限をリクエスト](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)します。

2. LINEが提供する適切な手順に従ってLINEログインを実装します：<br><br>
  - [Webアプリの手順](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [ネイティブアプリの手順](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>認証リクエストの[スコープ設定](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)に`email`を含めるようにしてください。

{: start="3"}
3. [IDトークンの検証呼び出し](https://developers.line.biz/en/reference/line-login/#verify-id-token)を使用して、ユーザーのメールアドレスを取得します。

4. ユーザーのLINE ID（`native_line_id`）を、データベース内の一致するメールアドレスを持つユーザーのプロファイルに保存するか、ユーザーのメールアドレスとLINE IDで新しいユーザープロファイルを作成します。

5. 新しいまたは更新されたユーザー情報を、[`/user/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)、[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)を使用してBrazeに送信します。

#### ワークフロー {#workflows}

##### 既存のフォロワーがLINEログインを使用する場合 {#existing-follower-uses-line-login}

**シナリオ:** 初回のサブスクライバー同期中、または統合後の「フォロー」イベントを通じて匿名ユーザーが作成されました。

1. ユーザーがLINEログインを使用してアプリにログインします。
2. LINEがユーザーのメールアドレスを提供します。
3. 更新されたユーザー（LINE IDを追加するためのそのメールアドレスを持つ既存のユーザープロファイル）をBrazeに送信するか、匿名ユーザーをメールアドレスで更新します。

##### 新しいフォロワーがLINEログインを使用する場合 {#new-follower-uses-line-login}

**シナリオ:** ユーザーのLINE IDを持つユーザープロファイルがBrazeに存在しません。

1. ユーザーがLINEログインを使用してアプリにログインします。
2. LINEがユーザーのメールアドレスを提供します。
3. 以下のいずれかを行います：
  - そのメールアドレスを持つ既存のユーザープロファイルを更新して、ユーザーのLINE IDも含めます。
  - メールアドレスとLINE IDで新しいユーザープロファイルを作成します。
4. ユーザーがLINE公式アカウントをフォローすると、Brazeはフォローイベントを受信し、ユーザーの購読ステータスを`subscribed`に更新します。

### ユーザーアカウントリンク {#user-account-linking}

この方法では、ユーザーがLINEアカウントをアプリのユーザーアカウントにリンクできます。Brazeで{% raw %}`{{line_id}}`{% endraw %}などのLiquidを使用して、ユーザーのLINE IDをWebサイトやアプリに渡すパーソナライズされたURLを作成し、既知のユーザーに関連付けることができます。

1. 購読状態の変更に基づくアクションベースのキャンバスを作成し、ユーザーがLINEチャネルを購読した際にトリガーされるようにします。<br>![ユーザーがLINEチャネルを購読した際にトリガーされるキャンバス。]({% image_buster /assets/img/line/account_link_1.png %})
2. ユーザーにWebサイトやアプリへのログインを促すメッセージを作成し、ユーザーのLINE IDをクエリパラメーターとして（Liquidを通じて）渡します。例：

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. クーポンコードを配信するフォローアップメッセージを作成します。
4. （オプション）LINEユーザーが識別された際にトリガーされるアクションベースのキャンペーンまたはキャンバスを作成し、ユーザーにクーポンコードを送信します。<br>![LINEユーザーが識別された際にトリガーされるアクションベースのキャンペーン。]({% image_buster /assets/img/line/account_link_2.png %})

#### 仕組み {#how-it-works}

ユーザーがログインすると、WebサイトまたはアプリでユーザーIDがBrazeに送信され、URLの一部として渡されたLINE IDと関連付けられます。コード例は以下のとおりです：

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

**シナリオ:** Brazeの既存ユーザーがLINEでチャネルをフォローします。

1. LINEがBrazeにフォローイベントを送信します。
2. BrazeはLINE ID、`line_id`ユーザーエイリアス、およびLINE購読グループのステータス`subscribed`を持つ匿名ユーザープロファイルを作成します。
3. ユーザーがWebサイトやアプリへのリンクを含むLINEメッセージを受信し、ログインします。ユーザープロファイルが既知になります。
4. 作成された匿名ユーザープロファイルが識別され、[/users/identifyエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)を通じてユーザーの既知のユーザープロファイルにマージされます。既知のユーザープロファイルにLINE IDが含まれ、購読ステータスが`subscribed`になります。
5. （オプション）ユーザーがクーポンコードを含むLINEメッセージを受信し、BrazeがBrazeユーザープロファイルに送信を記録します。

## BrazeでのLINEテストユーザーの作成 {#creating-line-test-users-in-braze}

[ユーザー照合](#user-id-reconciliation)をセットアップする前に、「Who am I」キャンバスまたはキャンペーンを作成してLINEチャネルをテストできます。

1. 特定のトリガーワードでユーザーのBrazeユーザーIDを返すキャンバスをセットアップします。<br><br>トリガーの例<br><br>![特定の購読グループにインバウンドLINEを送信したユーザーにキャンペーンを送信するトリガー。]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>メッセージの例<br><br>![BrazeユーザーIDを表示するLINEメッセージ。]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. Brazeで、Braze IDを使用して特定のユーザーを検索し、必要に応じて変更できます。

{% alert important %}
キャンバスにグローバルコントロールやコントロールグループが送信を妨げていないことを確認してください。
{% endalert %}