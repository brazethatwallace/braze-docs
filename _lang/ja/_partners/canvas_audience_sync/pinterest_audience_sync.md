---
nav_title: Pinterest
article_title: キャンバスオーディエンスのPinterestへの同期
description: "このリファレンス記事では、Braze Audience Sync to Pinterestを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 5
alias: "/audience_sync_pinterest/"

tool:
  - Canvas

---

# Audience Sync to Pinterest

Braze Audience Sync to Pinterestを使用すると、ブランドは独自のBraze統合からのユーザーデータをPinterestオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいてBrazeキャンバスでメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために通常使用する基準を、Pinterestオーディエンス内の該当ユーザーに対して広告をトリガーするためにも使用できるようになりました。

**オーディエンス同期の一般的なユースケースは次のとおりです。**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

この機能により、ブランドはPinterestと共有する特定のファーストパーティデータをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合について最大限の配慮を行っています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro免責条項**<br>
Braze Audience Sync to PinterestはAudience Sync Pro統合です。この統合の詳細については、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}
キャンバスでPinterestオーディエンスステップを設定する前に、以下の項目が作成、完了、および/または承認されていることを確認する必要があります。

| 要件 | Origin | 説明 |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | ブランドのPinterestアセット（広告アカウント、ページ、アプリなど）を管理するための一元化ツールです。 |
| Pinterest広告アカウント | [Pinterest](https://ads.pinterest.com/) | ブランドのPinterest Business Hubに紐づけられたアクティブなPinterest広告アカウントです。<br><br>Pinterest Business Hubの管理者が、Brazeで使用する予定のPinterest広告アカウントに対する管理者権限を付与していることを確認してください。 |
| Pinterestの利用規約とポリシー | Pinterest | Pinterest Audience Syncの使用に関連するPinterestの必須の利用規約、ポリシー、ガイドライン、およびドキュメント（参照により組み込まれる利用規約、ポリシー、ガイドライン、およびドキュメントを含む）に準拠することに同意してください。これには、利用規約、ビジネス利用規約、プライバシーポリシー、開発者およびAPI利用規約、広告データ規約、広告ガイドライン、広告サービス契約、コミュニティガイドライン、およびブランドガイドラインが含まれる場合があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：Pinterestに接続する {#step-1-connect-to-pinterest}

{% alert important %}
PinterestをBrazeアカウントに接続するには、[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Pinterest**を選択します。Pinterest Audience Syncの下で、**Connect Pinterest**を選択します。

![概要セクションとPinterest Audience Syncセクション（Connect Pinterestボタンを含む）が表示されたBrazeのPinterestテクノロジーページ。]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

その後、PinterestのOAuthページにリダイレクトされ、広告アカウント管理とオーディエンス管理のためにBrazeを認証します。

**Confirm**を選択すると、Brazeにリダイレクトされ、同期したいPinterest広告アカウントを選択できます。

![Pinterestに接続できる利用可能な広告アカウントのリスト。]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

接続が成功すると、パートナーページに戻り、接続されているアカウントの確認や既存アカウントの切断ができます。

![広告アカウントが正常に接続されたことを示す、更新されたPinterestテクノロジーパートナーページ。]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Pinterestの接続はBrazeワークスペースレベルで適用されます。Pinterestの管理者がPinterest Business Hubからあなたを削除したり、接続されたPinterestアカウントへのアクセスを取り消したりした場合、Brazeは無効なトークンを検出します。その結果、Pinterest Audienceコンポーネントを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2：PinterestでAudience Syncステップを追加する {#step-2-add-an-audience-sync-step-with-pinterest}

キャンバスにコンポーネントを追加し、**Audience Sync**を選択します。

![Audience Syncコンポーネントオプションが表示されたキャンバスステップセレクター。]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![キャンバスパスに追加されたAudience Syncコンポーネントカード。]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### ステップ3：同期の設定 {#step-3-sync-setup}

**Custom Audience**ボタンをクリックして、コンポーネントエディターを開きます。

Audience Syncパートナーとして**Pinterest**を選択します。

![同期パートナーとしてPinterestが選択されたAudience Syncコンポーネントエディター。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

次に、目的のPinterest広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンス名を入力します。

{% tabs %}
{% tab 新しいオーディエンスを作成 %}

**新しいオーディエンスを作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択して、Pinterestと同期するフィールドを選択します。次に、ステップエディターの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![Custom Audienceキャンバスステップの展開ビュー。ここでは、目的の広告アカウントが選択され、新しいオーディエンスが作成されています。]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。オーディエンスは下書きモードで作成されるため、ユーザーはキャンバスジャーニーの後半でユーザー削除のためにこのオーディエンスを参照できます。

![キャンバスコンポーネントで新しいオーディエンスが作成された後に表示されるアラート。]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

新しいオーディエンスでキャンバスを起動すると、BrazeはユーザーがAudience Syncステップに入るとほぼリアルタイムでユーザーを同期します。
{% endtab %}
{% tab 既存のオーディエンスと同期 %}
**既存のオーディエンスと同期**<br>
Brazeでは、既存のPinterestオーディエンスにユーザーを追加して、オーディエンスを最新の状態に保つこともできます。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、オーディエンスに追加します。BrazeはユーザーがAudience Syncステップに入るとほぼリアルタイムでユーザーを追加します。

![Custom Audienceキャンバスステップの展開ビュー。ここでは、目的の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### ステップ4：キャンバスを起動する {#step-4-launch-canvas}

Pinterestへの Audience Syncを設定したら、キャンバスを起動します。新しいオーディエンスが作成され、Audience Syncステップを通過するユーザーはPinterest上のこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Pinterestでオーディエンスを確認するには、広告マネージャーアカウントにアクセスし、Adsドロップダウンから Audiences を選択します。Audienceページでは、各オーディエンスのサイズが約100に達した後に確認できます。

![オーディエンス名、オーディエンスID、オーディエンスタイプ、オーディエンスサイズを含む、特定のPinterestオーディエンスのオーディエンス詳細。]({% image_buster /assets/img/pinterest/pinterest11.png %})

## ユーザー同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに到達すると、BrazeはPinterestのMarketing APIレート制限を遵守しながら、ほぼリアルタイムでユーザーを同期します。Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理し、Pinterestに送信します。

PinterestのセグメントAPIレート制限では、1ユーザーあたり1秒間に7クエリまで、1リクエストあたり1,900ユーザーまでに制限されています。顧客がこの制限に達した場合、Brazeは最大約13時間にわたって同期をリトライします。それでも同期ができない場合、Brazeはこれらのユーザーをユーザーエラー指標に記録します。

## 分析の理解 {#understanding-analytics}

以下の表には、オーディエンス同期コンポーネントの分析をより深く理解するための指標と説明が含まれています。

| 指標 | 説明 |
| --- | --- |
| エントリー済み | Pinterestに同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進んだ | 次のコンポーネントがある場合、何人のユーザーが次のコンポーネントに進みましたか？キャンバスブランチの最後のステップである場合、すべてのユーザーが自動的に進みます。 |
| 同期済みユーザー | Pinterestへの同期に成功したユーザーの数。 |
| 未同期ユーザー | マッチングに必要なフィールドが不足しているため、同期されなかったユーザーの数。 |
| 保留中のユーザー | 現在BrazeがPinterestへの同期を処理中のユーザーの数。 |
| エラーが発生したユーザー | 約13時間のリトライ後にAPIエラーによりPinterestに同期されなかったユーザーの数。エラーの原因としては、無効なPinterestトークンや、Pinterest上でオーディエンスが削除された場合などが考えられます。 |
| キャンバスを退出 | キャンバスを退出したユーザーの数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

{% alert important %}
同期済みユーザーとエラー指標のレポートには、それぞれ一括フラッシャーと13時間のリトライにより遅延が発生することにご注意ください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### Pinterest でオーディエンスが反映されるまでどのくらいかかりますか？ {#how-long-will-it-take-for-my-audiences-to-populate-in-pinterest}

オーディエンスのサイズは、Pinterest の Ads Manager の**Audiences**ページで24〜48時間以内に更新されます。

### Pinterest にユーザーを渡した後、ユーザーがマッチしたかどうかはどうすればわかりますか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-pinterest}

Pinterest は、独自のデータプライバシーポリシーにより、この情報を提供していません。

### 無効なトークンエラーが表示された場合はどうすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Pinterest Business Hub の管理者に、同期したい広告アカウントに対する適切な権限があることを確認してください。また、Pinterest パートナーページで Pinterest アカウントを切断してから再接続することもできます。

### キャンバスを起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

Pinterest パートナーページで Pinterest アカウントが Braze に正常に接続されていることを確認してください。広告アカウントを選択し、新しいオーディエンスの名前を入力し、マッチするフィールドを選択していることを確認してください。

### Audience Sync ステップで広告アカウントを選択できないのはなぜですか？ {#why-cant-i-select-my-ad-account-for-my-audience-sync-step}

トークンが正しいアカウント権限で生成されたことを確認してください。Pinterest の広告アカウントにオーディエンスが多すぎる場合、広告アカウントを選択するドロップダウンがタイムアウトする可能性があります。この場合、広告アカウント内のオーディエンス数を減らすことをお勧めします。