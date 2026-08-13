---
nav_title: TikTok
article_title: キャンバスオーディエンスのTikTokへの同期
alias: /tiktok_audience_sync/
description: "このリファレンス記事では、Braze Audience Sync to TikTokを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
tool:
  - Canvas
page_order: 8

---

# Audience Sync to TikTok

Braze Audience Sync to TikTokを使用すると、ブランドは独自のBraze統合からのユーザーデータをTikTokオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。Brazeキャンバスでメッセージ（プッシュ、メール、SMS、Webhookなど）をトリガーするために通常使用する基準はすべて利用可能です。

**オーディエンス同期の一般的なユースケースには次のものがあります。**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

この機能により、ブランドは特定のファーストパーティデータがTikTokと共有されるかどうかをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合について最大限の配慮を行っています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% alert important %}
**Audience Sync Pro免責条項**<br>
Braze Audience Sync to TikTokはAudience Sync Pro統合です。この統合の詳細については、Brazeアカウントマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

キャンバスでTikTokオーディエンスステップを設定する前に、以下の項目が作成、完了、および/または承認されていることを確認する必要があります。

| 要件 | Origin | 説明 |
| ----------- | ------ | ----------- |
| TikTok for Business Centerアカウント | [TikTok](https://business.tiktok.com/) | ブランドのTikTokアセット（広告アカウント、ページ、アプリなど）を管理するための一元化されたツールです。 |
| TikTok広告アカウント | [TikTok](https://ads.tiktok.com/) | ブランドのBusiness Centerアカウントに紐づけられたアクティブなTikTok広告アカウントです。<br><br>TikTok Business Centerの管理者が、Brazeで使用する予定のTikTok広告アカウントへの管理者権限を付与していることを確認してください。 |
| TikTokの利用規約とポリシー | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | TikTok Audience Syncの使用に関連するTikTokの必須の利用規約、ポリシー、ガイドライン、およびドキュメント（参照により組み込まれる利用規約、ポリシー、ガイドライン、およびドキュメントを含む）に準拠することに同意してください。これには、商用利用規約、広告利用規約、プライバシーポリシー、カスタムオーディエンス利用規約、開発者利用規約、開発者データ共有契約、広告ポリシー、ブランドガイドライン、およびコミュニティガイドラインが含まれる場合があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：TikTokに接続する {#step-1-connect-to-tiktok}

{% alert important %}
TikTokをBrazeアカウントに接続するには、[「管理者」権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー**に移動し、**TikTok**を選択します。TikTok Audience Syncの下で、**Connect TikTok**を選択します。

![BrazeのTikTokテクノロジーページには、概要セクションとTikTok Audience Syncセクション（Connected TikTokボタン付き）が含まれています。]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

その後、TikTokのOAuthページにリダイレクトされ、Brazeに広告アカウント管理とオーディエンス管理の権限を付与します。**Confirm**を選択すると、Brazeに戻り、同期するTikTok広告アカウントを選択できます。

![Brazeオーディエンス管理のアクセスを要求するTikTok OAuth認証ページ。]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

接続が完了すると、パートナーページに戻ります。ここでは、接続されているアカウントの確認や、既存のアカウントの切断ができます。

![接続されたTikTok広告アカウントを表示するBraze TikTokパートナーページ。]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

TikTokの接続はBrazeワークスペースレベルで適用されます。TikTokの管理者がTikTok Business Centerからあなたを削除したり、接続されたTikTokアカウントへのアクセスを取り消したりした場合、Brazeは無効なトークンを検出します。その結果、TikTok Audienceコンポーネントを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2：キャンバスにTikTok Audienceコンポーネントを追加する {#step-2-add-a-tiktok-audience-component-in-canvas}

キャンバスにコンポーネントを追加し、**Audience Sync**を選択します。

![Audience Syncコンポーネントオプションが表示されたキャンバスステップセレクター。]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![キャンバスパスに追加されたAudience Syncコンポーネントカード。]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### ステップ3：同期の設定 {#step-3-sync-setup}

**Custom Audience**ボタンをクリックして、コンポーネントエディターを開きます。

Audience Syncパートナーとして**TikTok**を選択します。

![TikTokが同期パートナーとして選択されたAudience Syncコンポーネントエディター。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

次に、目的のTikTok広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンス名を入力します。

![広告アカウントの選択とオーディエンスドロップダウンが表示されたTikTok Audience Syncエディター。]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab 新しいオーディエンスを作成 %}

**新しいオーディエンスを作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択して、TikTokと同期するフィールドを選択します。次に、ステップエディターの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![マッチフィールドが選択されたTikTok Audience Syncステップの新規オーディエンス作成フォーム。]({% image_buster /assets/img/audience_sync/tiktok3.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。オーディエンスは下書きモードで作成されるため、ユーザーはキャンバスジャーニーの後半でユーザー削除のためにこのオーディエンスを参照できます。

![新しいTikTokオーディエンスの作成後にAudience Syncステップに表示される成功通知。]({% image_buster /assets/img/audience_sync/tiktok2.png %})

新しいオーディエンスでキャンバスを起動すると、Brazeはユーザーがオーディエンスステップに入るとほぼリアルタイムで同期します。

{% endtab %}
{% tab 既存のオーディエンスと同期 %}

**既存のオーディエンスと同期**<br>
Brazeでは、既存のTikTokオーディエンスにユーザーを追加して、オーディエンスを最新の状態に保つこともできます。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**Add to the Audience**を選択します。Brazeは、ユーザーがTikTok Audienceステップに入るとほぼリアルタイムで追加します。

![カスタムオーディエンスキャンバスステップの展開ビュー。ここでは、目的の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### ステップ4：キャンバスを起動する {#step-4-launch-canvas}
TikTok Audienceコンポーネントを設定したら、キャンバスを起動します。新しいオーディエンスが作成され、TikTok Audienceコンポーネントを通過するユーザーはTikTok上のこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

TikTokでオーディエンスを確認するには、**Ads Manager Account**にアクセスし、**Assets**ドロップダウンから**Audiences**を選択します。**Audience**ページでは、各オーディエンスのサイズが&#126;1,000に達した後に確認できます。

![指定されたオーディエンスの以下の指標を一覧表示するTikTokページ。]({% image_buster /assets/img/tiktok/tiktok5.png %})

## ユーザー同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに到達すると、BrazeはTikTokのMarketing APIレート制限を遵守しながら、ほぼリアルタイムでユーザーを同期します。Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理し、TikTokに送信します。

TikTokのセグメントAPIレート制限では、1秒あたり50クエリ、1リクエストあたり10,000ユーザーまでに制限されています。顧客がこの制限に達した場合、Brazeは最大&#126;13時間にわたって同期をリトライします。それでも同期ができない場合、Brazeはこれらのユーザーをユーザーエラー指標に記録します。

## 分析について {#understanding-analytics}

以下の表には、Audience Sync コンポーネントの分析をより深く理解するための指標と説明が含まれています。

| 指標 | 説明 |
| ------ | ----------- |
| 入場済み | TikTok に同期するためにこのコンポーネントに入ったユーザー数。 |
| 次のステップに進んだ | 次のコンポーネントが存在する場合、そこに進んだユーザー数。キャンバスブランチの最後のステップである場合、すべてのユーザーが自動的に進みます。 |
| 同期済みユーザー | TikTok に正常に同期されたユーザー数。これは TikTok でマッチしたユーザー数と同じではないことに注意してください。 |
| 未同期ユーザー | マッチに必要なフィールドが不足しているため同期されなかったユーザー数。 |
| 保留中のユーザー | 現在 Braze が TikTok への同期を処理中のユーザー数。 |
| エラーが発生したユーザー | 約13時間のリトライ後に API エラーにより TikTok に同期されなかったユーザー数。エラーの原因としては、無効な TikTok トークンや、TikTok 上でオーディエンスが削除された場合などが考えられます。 |
| キャンバスを退出 | キャンバスを退出したユーザー数。これは、キャンバスの最後のステップが Audience Sync コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析について" }

{% alert important %}
同期済みユーザーとエラーが発生したユーザーの指標のレポートには、それぞれ一括フラッシャーと13時間のリトライにより遅延が生じることに注意してください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### 無効なトークンエラーが表示された場合、次に何をすべきですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

TikTokパートナーページでTikTokアカウントを切断し、再接続できます。同期したい広告アカウントに対して適切な権限を持っているか、TikTok Business Centerの管理者に確認してください。

### キャンバスの起動が許可されないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

TikTokパートナーページで、TikTokアカウントがBrazeに正常に接続されていることを確認してください。次に、広告アカウントを選択し、新しいオーディエンスの名前を入力し、マッチするフィールドを選択していることを確認してください。

### TikTokにユーザーを渡した後、ユーザーがマッチしたかどうかはどうすればわかりますか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-tiktok}

TikTokはデータプライバシーポリシーにより、この情報を提供していません。

### TikTokでオーディエンスが反映されるまでどのくらいかかりますか？ {#how-long-will-it-take-for-my-audiences-to-populate-in-tiktok}

オーディエンスサイズは、TikTok Ads Managerのオーディエンスページで24〜48時間以内に更新されます。

### TikTok広告アカウントで保持できるオーディエンスの最大数はいくつですか？ {#what-is-the-maximum-number-of-audiences-i-can-have-in-my-tiktok-ad-account}

TikTok広告アカウントごとに最大400のオーディエンスを保持できます。

### TikTokでのオーディエンスサイズやマッチ率が、BrazeのAudience Syncで同期されたユーザー数よりも高いのはなぜですか？ {#why-is-my-audience-size-or-match-rate-in-tiktok-higher-than-the-users-synced-in-braze-with-audience-sync}

これは、TikTokでは1つのIDが複数のTikTokユーザーに関連付けられている場合があるためです。これは、クライアントがモバイル広告ID（iOS IDFAおよびAndroid GAID）を使用している場合に最も多く発生します。1つのデバイスに複数のTikTokユーザーがログインしている可能性があるためです。

さらに、TikTokはPangleユーザーもマッチしたユーザーとしてカウントするため、場合によってはマッチ率が高くなることがあります。ただし、広告配信にオーディエンスを使用する場合、実際に配信可能なオーディエンスサイズは、配置やその他の影響要因に依存するため、マッチしたユーザーサイズほど高くならない場合があります。

### 「Audience Does Not Exist For キャンバス」という件名のメールが届くのはなぜですか？ {#why-am-i-receiving-an-email-with-the-subject-audience-does-not-exist-for-canvas}

これは、同期先として選択したオーディエンスがストリーミングオーディエンスではない場合（例えば、類似オーディエンスやユーザーファイルオーディエンスの場合）に発生する可能性があります。Braze Audience Syncキャンバスステップを通じて新しいオーディエンスを作成してみてください。