---
nav_title: スウィム
article_title: スウィム
description: "このリファレンス記事では、BrazeとSwymのパートナーシップについて説明します。このパートナーシップにより、買い物客は商品を保存し、Webサイト、モバイルアプリ、小売店でシームレスに買い物を続けることができます。"
alias: /partners/swym/
page_type: partner
search_tag: Partner
---

# スウィム {#swym}

> [Swym](https://getswym.com/)は、ウィッシュリスト、後で購入、ギフトレジストリ、再入荷アラートを活用して、eコマースブランドがショッピングの意図を捉えるのを支援します。権限ベースの豊富なデータを使用することで、ハイパーターゲティングキャンペーンを作成し、エンゲージメントを促進し、コンバージョンを向上させ、ロイヤルティを高めるパーソナライズされたショッピング体験を提供できます。

*この統合はSwymによって管理されています。*

## 統合について {#about-the-integration}

SwymとBrazeの統合により、パーソナライズされたイベント駆動型のマーケティングキャンペーンを配信し、買い物客の購買意欲を売上につなげることができます。この統合を利用することで、買い物客は前回の続きから買い物を再開したり、ショッピングジャーニーを通じて他のユーザーと協力したり、パフォーマンスの高いリターゲティングキャンペーンを受け取ったりすることができます。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 要件 | 説明 |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Swym | Swym Wishlist Plus、Back in Stockアプリ、またはその両方がeコマースプラットフォーム（ShopifyまたはBigCommerce）にインストールされており、エンタープライズプランに加入していること。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

SwymのWishlist PlusおよびBack in Stock AlertsアプリをBrazeと接続することで、ウィッシュリストへの追加、再入荷サブスクリプション、値下げアラート、リマインダーなどの買い物客のアクティビティイベントを、カスタムイベントとしてBrazeに自動送信できます。これらのイベントは、Brazeでの自動メッセージのトリガーとして使用でき、タイムリーで適切かつ魅力的なコミュニケーションを促進し、買い物客を購入へと導きます。

## Swymの統合 {#integrating-swym}

### ステップ 1: SwymアプリをBrazeに接続する {#step-1-connect-your-swym-app-to-braze}

現在、BrazeとSwymの統合はマネージド統合であり、セルフサービスではありません。開始するには、Swymサポートチーム（[support@getswym.com](mailto:support@getswym.com)）に連絡し、以下の情報を提供してください。Swymが代わりに統合を設定します。

1. Brazeダッシュボードで `users.track` 権限を持つ[REST APIキー]({{site.baseurl}}/api/basics/#about-rest-api-keys)を生成します。

![BrazeでAPIキーを生成する。]({% image_buster /assets/img/swym/braze-api-key.png %})

{% alert important %}
APIキーを保護するため、Swymではワンタイム自己破壊型リンクツール（例：[OneTimeSecret](https://onetimesecret.com/)）を使用して認証情報を安全に共有することを推奨しています。
{% endalert %}

{: start="2"}
2. BrazeはダッシュボードとRESTエンドポイント用に複数のインスタンスを管理しています。プロビジョニングされたインスタンスの[RESTエンドポイント]({{site.baseurl}}/api/basics/#endpoints)を提供してください。

3. APIキーとインスタンスURLをSwymサポートチームと共有した後、チームが統合を設定し、確認の返信をします。

4. セットアップが完了すると、Swymのカスタムイベントが自動的にBrazeに登録されます。Brazeダッシュボードの**データ設定** > **カスタムイベント**で、登録されたSwymイベントの一覧を確認できます。

5. 対応するカスタムイベントの**Manage Properties**を選択して、各Swymイベントのプロパティを表示します。これらのプロパティには、メッセージをパーソナライズするために使用できるイベント値が含まれています。

![Brazeのカスタムプロパティ。]({% image_buster /assets/img/swym/braze-custom-properties.png %})

### ステップ 2: Brazeに送信したいイベントをサブスクライブする {#step-2-subscribe-to-events-you-want-to-send-to-braze}

Wishlist Plusアプリから**Marketing**タブに移動し、**Automations**セクションを見つけます。ここで、サブスクライブしたいイベントを選択できます。

![サブスクライブするイベント。]({% image_buster /assets/img/swym/braze-event-subscription.png %})

#### Swym Wishlist Plusアプリのイベント {#swym-wishlist-plus-app-events}

| イベント名 | このイベントがトリガーされるタイミング |
|------------|------------------------------|
| ウィッシュリストの共有 | 買い物客が他の人とウィッシュリストを共有した場合 |
| ウィッシュリストへの追加 | 買い物客が商品をウィッシュリストに追加した場合 |
| ウィッシュリストリマインダー | 買い物客のウィッシュリストにある商品についてのリマインダー |
| 後で購入リマインダー | 買い物客の「後で購入」アイテムに関するリマインダー |
| 値下げアラート | ウィッシュリストの商品がセールになった場合 |
| 在庫僅少アラート | ウィッシュリストの商品の在庫が少なくなっている場合 |
| 再入荷アラート | ウィッシュリストの商品が再入荷した場合 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Swym Wishlist Plusアプリのイベント" }

#### Swym Back in Stockアラートアプリのイベント {#swym-back-in-stock-alerts-app-events}

| イベント名 | このイベントがトリガーされるタイミング |
|------------|------------------------------|
| 再入荷確認 | 買い物客が商品の再入荷通知をサブスクライブした場合 |
| 再入荷アラート | 買い物客が再入荷アラートをリクエストした商品が再入荷された場合 |
| 再入荷リマインダー | フォローアップアラート（通常、最初の再入荷アラートから約24時間後、設定可能） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Swym Back in Stockアラートアプリのイベント" }

### ステップ 3: Brazeのキャンペーンまたはキャンバスを作成する {#step-3-create-a-braze-campaign-or-canvas}

買い物客へのパーソナライズされたメッセージ配信を自動化するには、サブスクライブした各イベントに対して、Brazeで個別のキャンペーンまたはキャンバスを作成する必要があります。各キャンペーンまたはキャンバスは、特定のイベントに基づいてトリガーされるように設定し、対応するイベントプロパティを使用してメッセージにダイナミックなコンテンツを挿入する必要があります。ステップバイステップのガイダンスについては、[はじめに：キャンペーンとキャンバス]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases/)を参照してください。

![アクションベースのイベント。]({% image_buster /assets/img/swym/braze-canvas-setup.png %})

詳細については、[Swymヘルプセンター](https://help.getswym.com/en/articles/12344153-braze-integration)を参照するか、Swymサポートチーム（[support@getswym.com](mailto:support@getswym.com)）にお問い合わせください。