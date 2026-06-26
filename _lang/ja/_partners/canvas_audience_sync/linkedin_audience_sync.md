---
nav_title: LinkedIn
article_title: CanvasオーディエンスのLinkedInへの同期
alias: /linkedin_audience_sync/
description: "このリファレンス記事では、Braze Audience Sync to LinkedInを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
tool:
  - Canvas
page_order: 4

---

# LinkedInへのオーディエンス同期 {#audience-sync-to-linkedin}

Braze Audience Sync to LinkedInを使用すると、ブランドはBraze統合のユーザーデータをLinkedIn顧客リストに追加して、行動トリガー、セグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいてBraze Canvasでメッセージをトリガーするために通常使用する基準（プッシュ、メール、SMS、Webhookなど）を使用して、LinkedIn顧客リスト内の該当ユーザーに対して広告をトリガーできるようになりました。

**オーディエンス同期の一般的なユースケース**:

- 複数のチャネルを通じて高価値ユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルにあまり反応しないユーザーをリターゲティングする
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する

この機能により、ブランドはLinkedInと共有する特定のファーストパーティデータをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## 前提条件 {#prerequisites}

CanvasでLinkedInへのオーディエンス同期ステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認する必要があります。

| 必要条件 | 提供元 | 説明 |
| --- | --- | --- |
| LinkedIn広告アカウント | [LinkedIn](https://www.linkedin.com/campaignmanager) | ブランドに関連付けられたアクティブなLinkedIn広告アカウント。<br><br>そのアカウントにアクセスして使用するための関連するLinkedInの利用規約に同意していること、およびLinkedIn管理者によってオーディエンスを管理するための適切な権限が付与されていることを確認してください。 |
| LinkedInの利用規約とポリシー | LinkedIn | LinkedIn Audience Syncの使用に関連するLinkedInの必須規約、ポリシー、ガイドライン、およびドキュメント（参照によって組み込まれるものを含む）を遵守することに同意するものとします。これには、LinkedInのサービス規約、広告契約、データ処理契約、プロフェッショナルコミュニティガイドラインが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1: LinkedInへの接続 {#step-1-connect-to-linkedin}

{% alert important %}
LinkedInをBrazeアカウントに接続するには、[「Admin」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**テクノロジーパートナー**に移動し、**LinkedIn**を選択します。**LinkedIn Audience Sync**セクションで、**Connect LinkedIn**を選択します。

![BrazeのLinkedInテクノロジーページ。概要セクションとLinkedIn Audience Syncセクションがあり、「Connected LinkedIn」ボタンが表示されています。]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

次に、LinkedIn OAuthページにリダイレクトされ、Audience Sync統合に関連する権限をBrazeに承認します。**Confirm**を選択すると、Brazeにリダイレクトされ、同期するLinkedIn広告アカウントを選択します。

![接続する広告アカウントとして「Braze Self Service」が選択されています。]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

接続に成功すると、パートナーページに戻り、接続されているアカウントの確認や既存のアカウントの切断ができます。

![LinkedInアカウントが正常に接続された状態。]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

LinkedIn接続はBrazeワークスペースレベルで適用されます。LinkedIn管理者がLinkedIn広告アカウントからユーザーを削除した場合、Brazeは無効なトークンを検出します。その結果、LinkedInを使用しているアクティブなCanvasesにはエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2: Canvasのエントリ条件を設定する {#step-2-configure-your-canvas-entry-criteria}

広告トラッキング用のオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したり、[CCPA](https://oag.ca.gov/privacy/ccpa)の「販売・共有の拒否」権利などのプライバシー法に準拠したりすることが必要になる場合があります。マーケターは、Canvasのエントリ条件内でユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかのオプションを示します。

[Braze SDKを通じてiOS IDFAを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection)収集した場合、**Ads Tracking Enabled**フィルターを使用できます。値を`true`に選択すると、オプトインしたオーディエンス同期の宛先にのみユーザーを送信します。

![「Ad Tracking Enabled is true」というフィルターを持つエントリオーディエンス。]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、Canvasのエントリ条件にこれらをフィルターとして含める必要があります。

![「opted_in_marketing」が「true」と等しいエントリオーディエンスを持つCanvas。]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Brazeプラットフォーム内でこれらのデータ保護法に準拠する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

### ステップ3: LinkedInを使用したオーディエンス同期ステップの追加 {#step-3-add-an-audience-sync-step-with-linkedin}

Canvasにコンポーネントを追加し、「Audience Sync」を選択します。**Custom Audience**ボタンをクリックしてコンポーネントエディターを開きます。

![利用可能なコンポーネントのリストが表示されたCanvasエディター。]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![選択されたオーディエンス同期コンポーネント。]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### ステップ4: 同期設定 {#step-4-sync-setup}

**LinkedIn**を目的のオーディエンス同期パートナーとして選択します。

![「Set up Audience Sync」の詳細。複数のパートナーから選択可能。]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

次に、目的のLinkedIn広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新しいオーディエンスまたは既存のオーディエンスの名前を入力します。

![広告アカウントとしてBrazeが選択された状態でLinkedInに同期するオーディエンス。]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab 新規オーディエンスの作成 %}

**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択し、LinkedInと同期するフィールドを選択します。この統合では、現在以下をサポートしています。
- メール
- 名前と苗字
- Android GAID

次に、ステップエディターの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![「leads」オーディエンスの例。Braze広告アカウントが選択され、「leads」オーディエンスにユーザーを追加するアクションが設定されており、メール、Android GAID、名前と苗字がマッチングフィールドとして選択されています。]({% image_buster /assets/img/linkedin/linkedin10.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。オーディエンスは下書きモードで作成されるため、ユーザーは後でCanvasジャーニーでユーザーの削除のためにこのオーディエンスを参照できます。

![「leads」オーディエンスが作成されたことの確認。]({% image_buster /assets/img/linkedin/linkedin9.png %})

新しいオーディエンスを使用してCanvasを起動すると、オーディエンス同期コンポーネントに入る時点で、Brazeはユーザーをほぼリアルタイムで同期します。

{% endtab %}
{% tab 既存のオーディエンスとの同期 %}

**既存のオーディエンスとの同期**<br>
Brazeは、既存のLinkedInオーディエンスにユーザーを追加して、オーディエンスを最新の状態に保つ機能も提供しています。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**Add to the Audience**を選択します。Brazeは、オーディエンス同期コンポーネントに入ると、ほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンスCanvasステップの展開ビュー。目的の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### ステップ5: Canvasの起動 {#step-5-launch-canvas}

LinkedInへのオーディエンス同期を設定したら、Canvasを起動するだけです！新しいオーディエンスが作成され、オーディエンス同期ステップを通過するユーザーはLinkedInのこのオーディエンスに送られます。Canvasに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

LinkedInでオーディエンスを表示するには、広告アカウントに移動し、ナビゲーションの**Assets**セクションで**Audiences**を選択します。**Audiences**ページでは、300人以上のメンバーに達した後、各オーディエンスのサイズを確認できます。

![指定したオーディエンスの指標を一覧表示するLinkedInページ。]({% image_buster /assets/img/linkedin/linkedin8.png %})

## ユーザーの同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに到達すると、BrazeはLinkedInのAPIレート制限を尊重しながらほぼリアルタイムで同期します。Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理してからLinkedInに送信します。

LinkedInのAPIレート制限では、1秒あたり最大10クエリ、1リクエストあたり100,000ユーザーが許可されています。顧客がこの制限に達すると、Brazeは最大約13時間同期を再試行します。それでも同期できない場合、Brazeはこれらのユーザーを「エラーが発生したユーザー」指標に一覧表示します。

## 分析の理解 {#understanding-analytics}

次の表には、オーディエンス同期コンポーネントからの分析をよりよく理解するための指標と説明が含まれています。

| 指標 | 説明 |
| ------ | ----------- |
| 入力 | LinkedInと同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数。Canvasブランチの最後のステップである場合、すべてのユーザーが自動的に進みます。 |
| ユーザーの同期 | LinkedInに正常に同期されたユーザーの数。 |
| 同期されていないユーザー | マッチングフィールドの不足により同期されなかったユーザーの数。 |
| 保留中のユーザー | BrazeがLinkedInに同期するために現在処理中のユーザーの数。 |
| エラーが発生したユーザー | 約13時間の再試行後にAPIエラーのためLinkedInに同期されなかったユーザーの数。エラーの原因としては、LinkedInトークンが無効である場合や、LinkedInでオーディエンスが削除された場合などが考えられます。 |
| Canvasの終了 | Canvasを終了したユーザーの数。これは、Canvasの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

{% alert important %}
一括フラッシャーと13時間の再試行により、同期されたユーザーとエラーが発生したユーザーの指標のレポートに遅延が発生することに注意してください。
{% endalert %}

{% alert important %}
LinkedInは、プラットフォーム内のマッチ率に関する追加の指標を提供しています。特定のオーディエンス同期のマッチを確認するには、オーディエンス同期のステップ指標を選択して、**Canvas Step Details**ページに移動します。
<br><br>
パートナーとして**LinkedIn**、広告アカウント、およびオーディエンスを選択して、LinkedInからのオーディエンスサイズとマッチ率を確認します。

![オーディエンス同期ステップ指標の例。10,000人のユーザーが入力されています。]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### オーディエンスサイズがLinkedInに反映されるまでにどのくらいの時間がかかりますか？ {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

LinkedInアカウント内のオーディエンスを表示するまでに最大48時間の遅延があります。

### LinkedInの広告アカウントに反映されるオーディエンスの最小サイズはどのくらいですか？ {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

LinkedInアカウントにオーディエンスサイズが反映されるためには、少なくとも300人のメンバーを含む必要があります。

### 無効なトークンエラーが表示された場合、次に何をすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

LinkedInパートナーページでLinkedInアカウントを切断して再接続できます。同期する広告アカウントに対する適切な権限があることをLinkedIn管理者に確認してください。

### Canvasを起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

LinkedIn広告アカウントがLinkedInパートナーページでBrazeに正常に接続されていることを確認してください。次に、広告アカウントの選択、新しいオーディエンスの名前の入力、マッチングするフィールドの選択が完了していることを確認します。

### ユーザーをLinkedInに渡した後、ユーザーがマッチしたかどうかを知るにはどうすればよいですか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedInは、ダッシュボードでマッチ率に関する情報を提供しています。LinkedInの**Audiences**セクションで確認できます。LinkedInオーディエンスのマッチ率は、オーディエンス同期ステップのCanvasステップの詳細で確認できます。

### LinkedInで対応できるオーディエンスの数はどのくらいですか？ {#how-many-audiences-can-linkedin-support}

現在、LinkedIn広告アカウントのオーディエンス数に制限はありません。

### セグメントが「BUILDING」ステータスに留まり、更新されないのはなぜですか？ {#why-is-a-segment-stuck-in-building-status-and-not-updated}

セグメントは、下書きまたはアクティブなCampaignで30日間継続的に使用されない場合、未使用と見なされARCHIVEDに設定されます。このため、更新がARCHIVEDのセグメントにストリーミングされると、セグメントがBUILDING状態に「スタック」したように見えることがあります。BUILDING状態に移行し、再度アーカイブされる直前に、新しい更新が未使用のセグメントにストリーミングされます。