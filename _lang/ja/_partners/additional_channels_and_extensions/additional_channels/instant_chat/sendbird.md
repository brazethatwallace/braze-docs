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

_この統合はSendbirdによって管理されます。_

## 統合について {#about-the-integration}

BrazeとSendbirdの統合により、会社ユーザーは次の操作を実行できます。
* Brazeのセグメンテーションとトリガーの機能を使用して、パーソナライズされたアプリ内通知を開始します。
* Sendbird Notificationsプラットフォームで、アプリ環境内で配信されるカスタマイズされたアプリ内通知を作成し、ユーザーエンゲージメントを強化します。

BrazeとSendbird Notificationsの共同機能を活用することで、企業は効果的なアプリ内通知戦略によって顧客エンゲージメントを高め、コンバージョン率を向上させることができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Sendbirdアカウント | このパートナーシップを活用するには、Sendbirdアカウントが必要です。 |
| Sendbird UIKit | Sendbird UIKitを[iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit)または[Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit)アプリにインストールしておく必要があります。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

![]({% image_buster /assets/img/sendbird/use-cases.png %})

BrazeとSendbird Notificationsの統合により、顧客エンゲージメントを高め、優れたユーザーエクスペリエンスを提供するさまざまなユースケースが提供されます。

- **マーケティング**：閲覧履歴やこれまでの購買履歴に基づく限定割引など、ユーザーの好みに合わせたパーソナライズされたプロモーションやおすすめで、ターゲットを絞ったキャンペーンを強化します。
- **トランザクション**：注文、配送、請求、支払いに関するリアルタイムの最新情報（注文状況、配送の詳細、予定配送時刻の通知など）を提供して、顧客とのコミュニケーションを向上させます。

## 統合 {#integration}

### ステップ1：通知テンプレートの作成 {#step-1-create-a-notification-template}

[Sendbirdテンプレート](https://sendbird.com/docs/notifications/v1/templates)により、複数のテンプレートを作成して各チャネルに使用することで、パーソナライズされたアプリ内通知を送信できます。テンプレートはSendbird Dashboardでコードを書くことなく作成およびカスタマイズできます。

![]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### ステップ2：SendbirdダッシュボードでBraze統合を設定する {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

**Sendbird Dashboard**からアプリケーションを選択し、**Notifications > Integrations**に移動して、**Braze**セクションの**Add**をクリックします。ここでは、Braze REST APIキーとBraze RESTエンドポイントが必要です。

すべてのフィールドを入力したら、**Save**をクリックして統合を完了し、統合エンドポイントおよびAPIトークンにアクセスします。

### ステップ3：Sendbird Notification Builderをインストールする {#step-3-install-sendbird-notification-builder}

次に[Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji)をインストールする必要があります。このGoogle Chrome拡張機能を使用すると、BrazeダッシュボードでSendbirdを通じてカスタマイズした通知を送信できます。

![]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### 拡張機能にSendbird認証情報を追加する {#add-sendbird-credentials-to-the-extension}

拡張機能がインストールされたら、ブラウザのツールバーのSendbirdアイコンをクリックし、**Settings**を選択します。ここでは、**Sendbird Notification Builder**にあるアプリIDとAPIトークンを指定します。

### ステップ4：SendbirdのユーザーIDをBrazeのユーザーIDにマッピングする {#step-4-map-sendbird-user-id-to-braze-user-id}

統合を使用するには、SendbirdユーザーIDを[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)としてBrazeユーザープロファイルに追加する必要があります。[ユーザーインポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)ページから、CSVファイルを使用してユーザープロファイルをアップロードおよび更新できます。あるいは、BrazeのユーザーIDをSendbirdのユーザーIDとして使用できます。

### ステップ5：Webhookテンプレートのセットアップ {#step-5-set-up-your-webhook-template}

Brazeの**テンプレートとメディア**から**Webhookテンプレート**に進み、**Sendbird Webhook Template**を選択します。このテンプレートは、Sendbird Notification Builder拡張機能がインストールされている場合にのみ使用できます。

{% raw %}
1. テンプレートの名前を入力し、必要に応じてチームとタグを追加します。
2. リアルタイムまたはバッチエンドポイントをSendbirdダッシュボードから**Webhook URL**にコピーします。
3. **Receiver**フィールドで<i class="fas fa-plus"></i>アイコンをクリックし、SendbirdのユーザーIDにマッピングされているユーザー属性を挿入します。
    - カスタム属性`sendbird_id`をSendbirdユーザーIDとして使用している場合は`{{ '{{' }}custom_attribute.${sendbird_id}}}`。
    - BrazeユーザーIDをSendbirdユーザーIDとして使用している場合は`{{ '{{' }}${user_id}}}`。
4. **Settings**タブで、`SENDBIRD_API_TOKEN`をSendbirdダッシュボードの通知APIトークンに置き換えます。
5. テンプレートを保存します。
{% endraw %}

## この統合を使う {#using-this-integration}

### キャンペーン

1. Brazeダッシュボードの**キャンペーン**ページで、**キャンペーンを作成** > **Webhook**をクリックします。
2. 上記で作成したWebhookテンプレートを選択します。キャンペーンにはバッチエンドポイントを使用することを強くお勧めします。
3. **作成**タブでテンプレートの変数を編集して、テンプレートをカスタマイズします。

### キャンバス

1. 新規または既存のキャンバスから、**Message**コンポーネントを追加します。
2. コンポーネントを開き、**Messaging Channels**から**Webhook**を選択します。
3. 上記で作成したWebhookテンプレートを選択します。キャンバスにはリアルタイムエンドポイントを使用することを強くお勧めします。
4. **作成**タブでテンプレートの変数を編集して、テンプレートをカスタマイズします。

## カスタマイズ {#customization}

### 配信ステータスと開封ステータスを追跡する {#track-delivery-and-open-status}

通知の配信および開封ステータスのイベントをキャンペーンのコンバージョン指標と統合するには、Brazeダッシュボードにカスタムイベントを追加します。

1. Brazeダッシュボードから**設定 > 設定の管理 > カスタムイベント**に移動し、**+ カスタムイベントを追加**をクリックします。
2. カスタムイベントを作成したら、**プロパティの管理**をクリックし、「status」という名前のプロパティを追加して、プロパティの種類として「文字列」を選択します。
3. キャンペーンまたはキャンバスで通知を作成する場合は、**Event Name**フィールドにカスタムイベントの名前を入力します。

このカスタムイベントは、通知ごとに2回（メッセージが送信された時点と、ユーザーがメッセージを開封した時点）トリガーされます。
- メッセージが送信されると、カスタムイベントが`SENT`ステータスでトリガーされます。
- メッセージが読まれると、カスタムイベントが`READ`ステータスでトリガーされます。