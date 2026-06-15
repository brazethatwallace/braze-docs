---
nav_title: Pinterest
article_title: CanvasオーディエンスのPinterestへの同期
description: "このリファレンス記事では、Braze Audience Sync to Pinterestを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 5
alias: "/audience_sync_pinterest/"

tool:
  - Canvas

---

# Audience Sync to Pinterest

Braze Audience Sync to Pinterestを使用すると、ブランドは独自のBraze統合からのユーザーデータをPinterestオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいてBraze Canvasでメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために通常使用する基準を、Pinterestオーディエンス内の該当ユーザーに対して広告をトリガーするためにも使用できるようになりました。

**オーディエンス同期の一般的なユースケースは次のとおりです。**

- 複数のチャネルを通じて価値の高いユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルに対して反応が薄いユーザーをリターゲティングする
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する
- 新規ユーザーをより効率的に獲得するための類似行動オーディエンスを作成する

この機能により、ブランドはPinterestと共有する特定のファーストパーティデータをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合について最大限の配慮を行っています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro免責条項**<br>
Braze Audience Sync to PinterestはAudience Sync Pro統合です。この統合の詳細については、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

CanvasでPinterestオーディエンスステップを設定する前に、以下の項目が作成、完了、または承諾されていることを確認する必要があります。

| 要件 | 提供元 | 説明 |
| --- | --- | --- |
| Pinterestビジネスハブ | [Pinterest](https://www.pinterest.com/business/hub/) | ブランドのPinterestアセット（広告アカウント、ページ、アプリなど）を管理するための集中管理ツールです。 |
| Pinterest広告アカウント | [Pinterest](https://ads.pinterest.com/) | ブランドのPinterestビジネスハブに関連付けられたアクティブなPinterest広告アカウント。<br><br>Pinterestビジネスハブの管理者が、Brazeで使用するPinterest広告アカウントの管理者権限を付与していることを確認してください。 |
| Pinterestの利用規約とポリシー | Pinterest | Pinterest Audience Syncの利用に関連するPinterestのすべての必須条件、ポリシー、ガイドライン、ドキュメントを遵守することに同意するものとします。これには、引用により組み込まれるすべての条件、ポリシー、ガイドライン、およびドキュメント（利用規約、ビジネス利用規約、プライバシーポリシー、開発者およびAPI利用規約、広告データ利用規約、広告ガイドライン、広告サービス契約、コミュニティガイドライン、ブランドガイドラインなどを含む）が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1:Pinterestに接続する {#step-1-connect-to-pinterest}

{% alert important %}
PinterestをBrazeアカウントに接続するには[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Pinterest**を選択します。Pinterest Audience Syncで、**Connect Pinterest**を選択します。

![BrazeのPinterestテクノロジーページ。概要セクションとPinterest Audience Syncセクション、およびConnected Pinterestボタンが表示されている。]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

その後、広告アカウント管理とオーディエンス管理をBrazeに許可するPinterest OAuthページにリダイレクトされます。

**Confirm**を選択すると、Brazeに戻るので、そこで同期するPinterest広告アカウントを選択します。

![Pinterestに接続できる利用可能な広告アカウントのリスト。]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

接続に成功すると、パートナーページに戻ります。そこでどのアカウントが接続されているかを確認したり、既存のアカウントを切断したりできます。

![広告アカウントが正常に接続されたことを示す更新後のPinterestテクノロジーパートナーページ。]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Pinterest接続はBrazeワークスペースレベルで適用されます。Pinterest管理者がPinterestビジネスハブからユーザーを削除したり、接続されているPinterestアカウントへのアクセスを取り消したりすると、Brazeは無効なトークンを検出します。その結果、Pinterestオーディエンスコンポーネントを使用しているアクティブなCanvasesにはエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2:PinterestでAudience Syncステップを追加する {#step-2-add-an-audience-sync-step-with-pinterest}

Canvasにコンポーネントを追加し、**Audience Sync**を選択します。

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### ステップ3:同期セットアップ {#step-3-sync-setup}

**Custom Audience**ボタンをクリックしてコンポーネントエディターを開きます。

**Pinterest**を目的のAudience Syncパートナーとして選択します。

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

次に、目的のPinterest広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab 新規オーディエンスの作成 %}

**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択し、Pinterestと同期するフィールドを選択します。次に、ステップエディターの下部にある**Create Audience**ボタンをクリックして、オーディエンスを保存します。

![カスタムオーディエンスCanvasステップの展開ビュー。ここで、目的の広告アカウントを選択し、新しいオーディエンスが作成される。]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。ユーザーは、後でCanvasジャーニーでユーザーを削除するためにこのオーディエンスを参照できます。これは、オーディエンスが下書きモードで作成されたためです。

![Canvasコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

新しいオーディエンスを使用してCanvasを起動すると、ユーザーがAudience Syncステップに入る時点で、Brazeはユーザーをほぼリアルタイムで同期します。
{% endtab %}
{% tab 既存のオーディエンスとの同期 %}
**既存のオーディエンスとの同期**<br>
Brazeは、既存のPinterestオーディエンスにユーザーを追加して、オーディエンスを最新の状態に保つ機能も提供しています。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンスの名前を入力し、オーディエンスに追加します。ユーザーがAudience Syncステップに入る時点で、Brazeはほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスCanvasステップの展開ビュー。ここで、希望する広告アカウントと既存のオーディエンスが選択される。]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### ステップ4:Canvasを起動する {#step-4-launch-canvas}

Audience Sync to Pinterestを設定したら、Canvasを起動します。新しいオーディエンスが作成され、Audience Syncステップを通過するユーザーはPinterest上のこのオーディエンスに送られます。Canvasに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Pinterestでオーディエンスを表示するには、広告マネージャーアカウントにログインし、**Ads**ドロップダウンから**Audiences**を選択します。**Audience**ページで、各オーディエンスが約100に達した後のサイズを確認できます。

![オーディエンスの名前、オーディエンスID、オーディエンスの種類、オーディエンスのサイズを含む、指定されたPinterestオーディエンスのオーディエンス詳細。]({% image_buster /assets/img/pinterest/pinterest11.png %})

## ユーザーの同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがAudience Syncステップに達すると、BrazeはPinterestのマーケティングAPIのレート制限を尊重しながら、ほぼリアルタイムで同期します。Brazeは5秒ごとに可能な限り多くのユーザーをバッチ処理してからPinterestに送信します。

PinterestのSegment APIのレート制限では、ユーザー1人あたり毎秒7クエリ、1リクエストあたり1,900ユーザーを超えることはできません。顧客がこの制限に達した場合、Brazeは最大約13時間まで同期を再試行します。それでも同期できない場合、BrazeはこれらのユーザーをUsers Errored指標の下にリストします。

## 分析の理解 {#understanding-analytics}

次の表に、Audience Syncコンポーネントの分析をよりよく理解するための指標と説明を示します。

| 指標 | 説明 |
| --- | --- |
| 入力 | Pinterestと同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数。これがCanvasブランチの最後のステップである場合、すべてのユーザーは自動的に進みます。 |
| ユーザーの同期 | Pinterestに正常に同期されたユーザーの数。 |
| 同期されていないユーザー | 一致するフィールドが不足しているため、同期されなかったユーザーの数。 |
| 保留中のユーザー | BrazeがPinterestへの同期のために現在処理しているユーザーの数。 |
| エラーが発生したユーザー数 | 約13時間の再試行後にAPIエラーのためにPinterestに同期されなかったユーザーの数。エラーの原因としては、Pinterestトークンが無効である場合や、Pinterestでオーディエンスが削除された場合などが考えられます。 |
| Canvasを終了 | Canvasを終了したユーザーの数。これは、Canvasの最後のステップがAudience Syncコンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

{% alert important %}
一括フラッシャーと13時間の再試行により、同期されたユーザーとエラーが発生したユーザーの指標のレポートにそれぞれ遅延が発生することに注意してください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### オーディエンスがPinterestに反映されるまでどのくらいの時間がかかりますか？ {#how-long-will-it-take-for-my-audiences-to-populate-in-pinterest}

オーディエンスのサイズは、Pinterestの広告マネージャーの**Audiences**ページで24〜48時間以内に更新されます。

### Pinterestにユーザーを渡した後、ユーザーがマッチしたかどうかはどうすればわかりますか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-pinterest}

Pinterestは、独自のデータプライバシーポリシーによりこの情報を提供していません。

### 無効なトークンエラーが表示された場合、次に何をすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

同期する広告アカウントに対する適切な権限があることを、Pinterestビジネスハブの管理者に確認してください。また、PinterestパートナーページでPinterestアカウントを切断してから再接続することもできます。

### Canvasを起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

PinterestパートナーページでPinterestアカウントがBrazeに正常に接続されていることを確認してください。広告アカウントを選択し、新しいオーディエンスの名前を入力し、一致するフィールドを選択したことを確認してください。

### Audience Syncステップで広告アカウントを選択できないのはなぜですか？ {#why-cant-i-select-my-ad-account-for-my-audience-sync-step}

トークンが正しいアカウント権限で生成されたことを確認してください。Pinterest広告アカウントのオーディエンスが多すぎる場合、広告アカウントを選択するドロップダウンがタイムアウトすることがあります。この場合は、広告アカウントのオーディエンス数を減らすことをお勧めします。