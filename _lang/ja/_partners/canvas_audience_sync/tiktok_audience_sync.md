---
nav_title: TikTok
article_title: CanvasオーディエンスのTikTokへの同期
alias: /tiktok_audience_sync/
description: "このリファレンス記事では、Braze Audience Sync to TikTokを使用して、行動トリガー、セグメンテーションなどに基づいて広告を配信する方法について説明します。"
tool:
  - Canvas
page_order: 8

---

# Audience Sync to TikTok

Braze Audience Sync to TikTokを使用すると、ブランドは独自のBraze統合からのユーザーデータをTikTokオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。Brazeキャンバスでメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために通常使用する基準はすべて利用可能です。

**オーディエンス同期の一般的なユースケースには次のものがあります。**

- 複数のチャネルを通じて高価値ユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルに対して反応が薄いユーザーをリターゲティングする
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する
- 新しいユーザーをより効率的に獲得するためのActalikeオーディエンスを作成する

この機能により、ブランドは特定のファーストパーティデータがTikTokと共有されるかどうかをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合について最大限の配慮を行っています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro免責条項**<br>
Braze Audience Sync to TikTokはAudience Sync Pro統合です。この統合の詳細については、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

CanvasでTikTokオーディエンスステップを設定する前に、次の項目が作成、完了、および/または承認されていることを確認する必要があります。

| 要件 | 提供元 | 説明 |
| ----------- | ------ | ----------- |
| TikTok for Business Centerアカウント | [TikTok](https://business.tiktok.com/) | ブランドのTikTokアセット（広告アカウント、ページ、アプリなど）を管理するための集中型ツールです。 |
| TikTok広告アカウント | [TikTok](https://ads.tiktok.com/) | ブランドのビジネスセンターアカウントに紐づけられたアクティブなTikTok広告アカウントです。<br><br>TikTokビジネスセンターマネージャーの管理者が、Brazeで使用する予定のTikTok広告アカウントに対する管理者権限を付与していることを確認してください。 |
| TikTok利用規約とポリシー | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Pinterest Audience Syncの使用に関連するTikTokの必要な条件、ポリシー、ガイドライン、およびドキュメント（それらに参照として組み込まれている条件、ポリシー、ガイドライン、およびドキュメントを含む）に同意すること。これには、商業利用規約、広告利用規約、プライバシーポリシー、カスタムオーディエンス利用規約、開発者利用規約、開発者データ共有契約、広告ポリシー、ブランドガイドライン、コミュニティガイドラインが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1:TikTokに接続する {#step-1-connect-to-tiktok}

{% alert important %}
TikTokをBrazeアカウントに接続するには[「管理者」権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー**に移動し、**TikTok**を選択します。TikTok Audience Syncで、**Connect TikTok**を選択します。

![BrazeのTikTokテクノロジーページには、概要セクションとTikTok Audience Syncセクションがあり、Connected TikTokボタンがあります。]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

その後、TikTokのOAuthページにリダイレクトされ、Brazeの広告アカウント管理およびオーディエンス管理を承認するよう求められます。**Confirm**を選択すると、Brazeに戻り、同期するTikTok広告アカウントを選択できます。

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

接続に成功すると、パートナーページに戻ります。ここでは、接続されているアカウントを表示したり、既存のアカウントの接続を解除したりできます。

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

TikTok接続はBrazeアプリグループレベルで適用されます。TikTokの管理者がTikTokビジネスセンターまたは接続されたTikTokアカウントへのアクセスからあなたを削除した場合、Brazeは無効なトークンを検出します。その結果、TikTokオーディエンスコンポーネントを使用しているアクティブなCanvasにはエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2:CanvasにTikTokオーディエンスコンポーネントを追加する {#step-2-add-a-tiktok-audience-component-in-canvas}

Canvasにコンポーネントを追加し、**Audience Sync**を選択します。

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### ステップ3:同期のセットアップ {#step-3-sync-setup}

**Custom Audience**ボタンをクリックしてコンポーネントエディターを開きます。

Audience Syncパートナーとして**TikTok**を選択します。

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

次に、目的のTikTok広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンスの名前を入力します。

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab 新規オーディエンスの作成 %}

**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択し、TikTokと同期したいフィールドを選択します。次に、ステップエディターの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。オーディエンスは下書きモードで作成されるため、後でCanvasジャーニーでユーザーの削除にこのオーディエンスを参照できます。

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

新しいオーディエンスを使用してCanvasを起動すると、ユーザーがオーディエンスステップに入る時点で、Brazeはほぼリアルタイムでユーザーを同期します。

{% endtab %}
{% tab 既存のオーディエンスとの同期 %}

**既存のオーディエンスとの同期**<br>
Brazeは、オーディエンスを最新の状態に保つために、ユーザーを既存のTikTokオーディエンスに追加する機能も提供しています。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、**Add to the Audience**を選択します。Brazeは、ユーザーがTikTokオーディエンスステップに入ると、ほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスCanvasステップの展開ビュー。ここで、希望の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### ステップ4:Canvasを起動する {#step-4-launch-canvas}
TikTokオーディエンスコンポーネントを構成したら、Canvasを起動するだけです！新しいオーディエンスが作成され、TikTokオーディエンスコンポーネントを通過するユーザーはTikTokのこのオーディエンスに送られます。Canvasに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

TikTokでオーディエンスを表示するには、**Ads Manager Account**にログインし、**Assets**のドロップダウンから**Audiences**を選択します。**Audience**ページで、各オーディエンスが&#126;1,000に達した後のサイズを確認できます。

![指定したオーディエンスの指標をリストするTikTokページ]({% image_buster /assets/img/tiktok/tiktok5.png %})

## ユーザーの同期とレート制限の考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがAudience Syncステップに達すると、BrazeはTikTokのマーケティングAPIのレート制限を尊重しながら、ほぼリアルタイムで同期します。Brazeは、TikTokに送信する前に、5秒ごとにできるだけ多くのユーザーをバッチ処理します。

TikTokのセグメント APIのレート制限では、1秒あたり50クエリ、1リクエストあたり10,000ユーザーを超えることはできません。顧客がこの制限に達した場合、Brazeは最大&#126;13時間まで同期を再試行します。それでも同期できない場合、BrazeはこれらのユーザーをUsers Errored指標にリストアップします。

## 分析の理解 {#understanding-analytics}

次の表に、Audience Syncコンポーネントからの分析をよりよく理解するのに役立つ指標と説明を示します。

| 指標 | 説明 |
| ------ | ----------- |
| 入力済み | TikTokと同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進みました | 次のコンポーネントに進んだユーザーの数（存在する場合）。これがCanvasブランチの最後のステップである場合、すべてのユーザーは自動的に進みます。 |
| ユーザーが同期されました | TikTokに正常に同期されたユーザーの数。これはTikTokでマッチしたユーザー数と同じではないことに注意してください。 |
| 同期されていないユーザー | マッチするフィールドが不足しているため、同期されなかったユーザーの数。 |
| 保留中のユーザー | BrazeがTikTokへの同期のために現在処理中のユーザーの数。 |
| エラーが発生したユーザー数 | 約13時間のリトライ後、APIエラーのためにTikTokに同期されなかったユーザーの数。エラーの潜在的な原因には、無効なTikTokトークンや、TikTokでオーディエンスが削除された場合が含まれます。 |
| Canvasを終了済み | Canvasを終了したユーザーの数。これは、Canvasの最後のステップがAudience Syncコンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

{% alert important %}
一括フラッシャーと13時間の再試行により、同期されたユーザーとエラーが発生したユーザーの指標のレポートに遅延が発生することに注意してください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### 無効なトークンエラーが表示された場合、次に何をすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

TikTokパートナーページでTikTokアカウントを切断して再接続できます。TikTokビジネスセンターの管理者に、同期したい広告アカウントに対する適切な権限があることを確認してください。

### Canvasを起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

TikTokパートナーページで、TikTokアカウントがBrazeに正常に接続されていることを確認してください。次に、広告アカウントの選択、新しいオーディエンスの名前の入力、マッチングするフィールドの選択が完了していることを確認します。

### ユーザーをTikTokに渡した後、ユーザーがマッチしたかどうかを確認するにはどうすればよいですか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-tiktok}

TikTokはデータプライバシーポリシーにより、この情報を提供していません。

### オーディエンスがTikTokに反映されるまでどのくらいかかりますか？ {#how-long-will-it-take-for-my-audiences-to-populate-in-tiktok}

オーディエンスのサイズは、TikTokの広告マネージャーのオーディエンスページで24〜48時間以内に更新されます。

### TikTok広告アカウントで保持できるオーディエンスの最大数はいくつですか？ {#what-is-the-maximum-number-of-audiences-i-can-have-in-my-tiktok-ad-account}

TikTok広告アカウント1つにつき、最大400オーディエンスまで設定できます。

### TikTokでのオーディエンスサイズやマッチ率が、BrazeのAudience Syncで同期されたユーザー数よりも高いのはなぜですか？ {#why-is-my-audience-size-or-match-rate-in-tiktok-higher-than-the-users-synced-in-braze-with-audience-sync}

TikTokでは、1つのIDが複数のTikTokユーザーに関連付けられている場合があるためです。これは、クライアントがモバイル広告ID（iOS IDFAおよびAndroid GAID）を使用する場合に最もよく発生します。1つのデバイスに複数のTikTokユーザーがログインしている可能性があるためです。

さらに、TikTokはPangleユーザーもマッチしたユーザーとしてカウントするため、場合によってはマッチ率が高くなることがあります。ただし、広告配信にオーディエンスを使用する場合、配置やその他の影響要因に左右されるため、実際に配信可能なオーディエンスサイズはマッチしたユーザーサイズほど大きくならない可能性があります。

### 「Audience Does Not Exist For Canvas」という件名のメールが届くのはなぜですか？ {#why-am-i-receiving-an-email-with-the-subject-audience-does-not-exist-for-canvas}

これは、同期先として選択したオーディエンスがストリーミングオーディエンスでない場合に発生する可能性があります（たとえば、類似オーディエンスやユーザーファイルオーディエンスの場合）。Braze Audience SyncのCanvasステップで新しいオーディエンスを作成してみてください。