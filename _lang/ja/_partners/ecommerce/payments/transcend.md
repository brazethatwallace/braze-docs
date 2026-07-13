---
nav_title: Transcend
article_title: Transcend
description: "このリファレンス記事では、BrazeとTranscendのパートナーシップについて説明します。Transcendはデータプライバシーインフラストラクチャプラットフォームであり、Brazeユーザーがデータ主体リクエストの履行を自動化できるようにします。"
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcendはデータプライバシーインフラストラクチャ企業であり、企業がユーザーに自身のデータの管理権を簡単に提供できるようにし、すべてのデータシステムおよびベンダーにわたるデータ主体リクエストを社内で自動的に履行します。

_この統合はTranscendによって管理されています。_

## 統合について {#about-the-integration}

BrazeとTranscendのパートナーシップは、数十のデータシステムにわたってデータをオーケストレーションすることでプライバシーリクエストを自動化し、チームがGDPRやCCPAなどの規制に準拠できるよう支援します。Transcendはエンドユーザーに対し、`privacy.\<company\>.com` でホストされるコントロールパネル（プライバシーセンター）を提供します。ユーザーはここでプライバシー設定の管理、データのエクスポート、データの削除を行うことができます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Transcendアカウント | このパートナーシップを利用するには、管理者権限を持つ [Transcend](https://app.transcend.io/) アカウントが必要です。 |
| Braze APIキー | `users.delete, users.alias.new, users.export.ids, email.unsubscribe,` および `email.blacklist` の権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

Transcendでは、データプライバシー規制に従って、Brazeプラットフォームでのアクセス、消去、コミュニケーションからのユーザーのオプトアウトをプログラムで実行できます。

### ステップ 1:Braze統合をセットアップする {#step-1-set-up-the-braze-integration}
開始するには、[Transcend](https://app.transcend.io/login) にログインします。
1. **Data Map** > **Add Data Silo** > **Braze** に移動し、**Connect** ボタンを選択します。<br><br>
2. アカウントがプロビジョニングされると、対応するURLのいずれかにログインします：`https://dashboard-01.braze.com`、`https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`。<br> 以下の[表]({{site.baseurl}}/api/basics/#endpoints)を使用して、ダッシュボードURLに基づいてどのサブドメインを含めるべきかを確認してください。<br><br>
3. 接続したら、Transcendの**Privacy Center**タブに移動します。ここで、Brazeのデータをデータプラクティスにマッピングする必要があります。これを行うには、適切な命名規則で新しいカテゴリと新しいデータコレクションを作成します（「Mailing Lists or User Profile」など）。完了したら、**Publish** を選択します。<br><br>
4. Data Mapに戻り、Brazeデータサイロを選択します。**Manage Datapoints** を展開して、前のステップで作成したコレクションラベル（カテゴリ）をドロップダウンから選択します。また、どのデータポイントに対してどのデータアクション（アクセスや消去など）を有効にするかを選択することもできます。<br><br>
5. 次に、Brazeデータサイロが表示された状態で、**Manage Identifiers** を展開します。有効にしたい識別子のチェックボックスをオンにします。たとえば、Transcendでユーザーをメールアドレスで検索する場合は、チェックボックスをオンにしてメールアドレス識別子を有効にします。

{% alert note %}
識別子が適切に有効化されていない場合、Transcendは特定のユーザーのリクエストを処理できないことがあります。
{% endalert %}

### ステップ 2:リクエストをテストする {#step-2-test-requests}
Transcendは、エンドユーザーからのリクエストの処理を開始する前に、Data Map全体でリクエストをテストすることを推奨しています。
1. Transcendの**Privacy Center**に移動し、**View your Privacy Center** を選択します。<br><br>
2. **Privacy Center**から**Take Control** を選択し、**Download my data** を選択します。リクエストを送信する前に、メールアドレスを入力するかログインして本人確認を行います。<br><br>
3. メールでTranscendからのメッセージを確認します。リクエストを確認するために、確認リンクをクリックするよう求められます。<br><br>
4. 次に、**Admin** ダッシュボードに戻り、**Incoming Requests** タブに移動してリクエストを選択します。ここにリクエストが表示されない場合は、Transcend（[support@transcend.io](mailto:support@transcend.io)）までお問い合わせください。<br><br>
5. リクエストをクリックしたら、**Data Silos** タブに移動し、**Braze** を選択します。返されたデータを検査し、確認します。<br><br>
6. 最後に、**Report** タブに移動し、**Approve and Send** をクリックします。リクエスト時に送信したメールアドレスにレポートが届きます。

## Braze統合を削除する {#remove-the-braze-integration}
Transcend Data MapからBrazeデータサイロを削除するには、次の手順に従います。
1. **Data Map** に移動し、**Braze** をクリックします。<br><br>
2. 画面の下部で **Remove Braze** を展開し、**Remove Silo** をクリックします。サイロを削除するかどうかを確認するプロンプトが表示されます。**Ok** をクリックします。<br><br>
3. Data Mapに戻り、サイロが削除されたことを確認します。