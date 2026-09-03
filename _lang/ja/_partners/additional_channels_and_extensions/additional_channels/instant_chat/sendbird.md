---
nav_title: Sendbird
article_title: Sendbird
description: "このリファレンス記事では、BrazeとSendbirdのパートナーシップについて説明します。Sendbirdは、業界をリードするアプリ内メッセージソリューションであり、ユーザーがSendbirdプラットフォームでアプリ内通知を受信できるようにします。"
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird](https://sendbird.com/) Notificationsは、マーケターと製品マネージャーに、アプリ内で持続的でインタラクティブな一方向メッセージにより顧客とコミュニケーションできる強力な新しいチャネルを提供します。これらのメッセージはあらゆるコミュニケーションに利用できますが、プロモーションやトランザクションの目的で最も一般的に利用されています。

_この統合はSendbirdによって管理されています。_

## 連携について {#about-the-integration}

BrazeとSendbirdの連携により、企業ユーザーは以下のことが可能になります。
{% multi_lang_include partners/instant_chat/sendbird_integration_bullets.md %}

BrazeとSendbird Notificationsの機能を組み合わせることで、効果的なアプリ内通知戦略を通じてカスタマーエンゲージメントを向上させ、より高いコンバージョン率を実現できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Sendbird アカウント | このパートナーシップを利用するには、Sendbird アカウントが必要です。 |
| Sendbird UIKit | [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) または [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit) アプリに Sendbird UIKit がインストールされている必要があります。 |
| Braze REST APIキー | `users.track` 権限を持つ Braze REST APIキー。<br><br> これは、Braze ダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)。エンドポイントは、お使いのインスタンスの Braze URL に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

![マーケティングおよびトランザクションメッセージングにおけるBrazeとSendbird Notifications連携のユースケースをまとめた図。]({% image_buster /assets/img/sendbird/use-cases.png %})

BrazeとSendbird Notificationsの連携は、カスタマーエンゲージメントを高め、優れたユーザー体験を提供するためのさまざまなユースケースを提供します。

- **マーケティング**：閲覧履歴や過去の購入に基づく限定割引など、ユーザーの好みに合わせたパーソナライズされたプロモーションやレコメンデーションでターゲットキャンペーンを強化します。
- **トランザクション**：注文、配送、請求、支払いに関するリアルタイムの更新を通じて顧客コミュニケーションを向上させます。注文ステータス、配送の詳細、配達予定時間に関する通知が含まれます。

## 連携 {#integration}

### ステップ1：通知テンプレートを作成する {#step-1-create-a-notification-template}

[Sendbirdテンプレート](https://sendbird.com/docs/notifications/v1/templates)を使用すると、各チャネルに対して複数のテンプレートを作成・使用し、パーソナライズされたアプリ内通知を送信できます。テンプレートはSendbirdダッシュボードでコーディングなしに作成・カスタマイズできます。

![通知テンプレートを作成するためのSendbirdダッシュボードテンプレートエディター。]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### ステップ2：SendbirdダッシュボードでBraze連携を設定する {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

**Sendbirdダッシュボード**からアプリケーションを選択し、**Notifications > Integrations**に移動して、**Braze**セクションの下にある**Add**をクリックします。ここで、Braze REST APIキーとBraze RESTエンドポイントが必要になります。

すべてのフィールドを入力したら、**Save**をクリックして連携を完了し、連携エンドポイントとAPIトークンにアクセスします。

### ステップ3：Sendbird Notification Builderをインストールする {#step-3-install-sendbird-notification-builder}

次に、[Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji)をインストールする必要があります。このGoogle Chrome拡張機能を使用すると、BrazeダッシュボードでSendbirdを通じてカスタマイズされた通知を送信できます。

![BrazeダッシュボードのSendbird Notification Builder Chrome拡張機能パネル。]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### 拡張機能にSendbirdの認証情報を追加する {#add-sendbird-credentials-to-the-extension}

拡張機能がインストールされたら、ブラウザのツールバーにあるSendbirdアイコンをクリックし、**Settings**を選択します。ここで、**Sendbird Notification Builder**にあるアプリIDとAPIトークンを入力します。

### ステップ4：SendbirdユーザーIDをBrazeユーザーIDにマッピングする {#step-4-map-sendbird-user-id-to-braze-user-id}

連携を使用するには、SendbirdユーザーIDを[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)としてBrazeユーザープロファイルに追加する必要があります。[ユーザーインポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv)ページからCSVファイルを使用してユーザープロファイルをアップロードおよび更新できます。または、BrazeユーザーIDをSendbirdユーザーIDとして使用することもできます。

### ステップ5：Webhookテンプレートを設定する {#step-5-set-up-your-webhook-template}

Brazeで、**Templates & Media**から**Webhook Templates**に移動し、**Sendbird Webhook Template**を選択します。このテンプレートは、Sendbird Notification Builder拡張機能がインストールされている場合にのみ利用可能です。

{% raw %}
1. テンプレート名を入力し、必要に応じてチームとタグを追加します。
2. Sendbirdダッシュボードからリアルタイムまたはバッチエンドポイントをコピーして、**Webhook URL**に貼り付けます。
3. **Receiver**フィールドで、<i class="fas fa-plus" aria-label="追加"></i>アイコンをクリックし、SendbirdユーザーIDにマッピングされたユーザー属性を挿入します。
    - SendbirdユーザーIDとしてカスタム属性`sendbird_id`を使用している場合は、`{{ '{{' }}custom_attribute.${sendbird_id}}}`を使用します。
    - BrazeユーザーIDをSendbirdユーザーIDとして使用している場合は、`{{ '{{' }}${user_id}}}`を使用します。
4. **Settings**タブで、`SENDBIRD_API_TOKEN`をSendbirdダッシュボードの通知APIトークンに置き換えます。
5. テンプレートを保存します。
{% endraw %}

## この連携の使用 {#using-this-integration}

### キャンペーン {#campaigns}

1. Brazeダッシュボードの**キャンペーン**ページで、**キャンペーンを作成** > **Webhook** をクリックします。
2. このセクションで作成したWebhookテンプレートを選択します。キャンペーンにはバッチエンドポイントを使用することを強くお勧めします。
3. **作成**タブで変数を編集してテンプレートをカスタマイズします。

### キャンバス {#canvas}

1. 新規または既存のキャンバスから、**メッセージ**コンポーネントを追加します。
2. コンポーネントを開き、**メッセージングチャネル**から**Webhook**を選択します。
3. このセクションで作成したWebhookテンプレートを選択します。キャンバスにはリアルタイムエンドポイントを使用することを強くお勧めします。
4. **作成**タブで変数を編集してテンプレートをカスタマイズします。

## カスタマイズ {#customization}

### 配信および開封ステータスの追跡 {#track-delivery-and-open-status}

通知の配信および開封ステータスイベントをキャンペーンのコンバージョン指標と統合するには、Brazeダッシュボードでカスタムイベントを追加します。

1. Brazeダッシュボードから、**設定 > 設定の管理 > カスタムイベント**に移動し、**+ カスタムイベントを追加**をクリックします。
2. カスタムイベントを作成したら、**プロパティの管理**をクリックし、「status」という名前のプロパティを追加して、プロパティタイプとして「String」を選択します。
3. キャンペーンまたはキャンバスで通知を作成する際、**Event Name**フィールドにカスタムイベントの名前を入力します。

このカスタムイベントは、各通知に対してメッセージの送信時とユーザーがメッセージを開封した時の2回トリガーされます。
- メッセージが送信されると、`SENT`ステータスでカスタムイベントがトリガーされます。
- メッセージが既読になると、`READ`ステータスでカスタムイベントがトリガーされます。