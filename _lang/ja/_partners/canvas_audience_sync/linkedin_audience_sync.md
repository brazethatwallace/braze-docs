---
nav_title: LinkedIn
article_title: Canvas オーディエンスの LinkedIn への同期
alias: /linkedin_audience_sync/
description: "このリファレンス記事では、Braze Audience Sync to LinkedIn を使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
tool:
  - Canvas
page_order: 4

---

# LinkedIn へのオーディエンス同期 {#audience-sync-to-linkedin}

Braze Audience Sync to LinkedIn を使用すると、ブランドは Braze 統合のユーザーデータを LinkedIn 顧客リストに追加して、行動トリガー、セグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいて Braze Canvasでメッセージをトリガーするために通常使用する基準（プッシュ、メール、SMS、Webhook など）を使用して、LinkedIn 顧客リスト内の該当ユーザーに対して広告をトリガーできるようになりました。

**オーディエンス同期の一般的なユースケース**:

- 複数のチャネルを通じて高価値ユーザーをターゲットにして、購入やエンゲージメントを促進する
- 他のマーケティングチャネルにあまり反応しないユーザーをリターゲティングする
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する

この機能により、ブランドは LinkedIn と共有する特定のファーストパーティデータをコントロールできます。Braze では、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

{% multi_lang_include early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## 前提条件 {#prerequisites}

Canvasで LinkedIn へのオーディエンス同期ステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認する必要があります。

| 必要条件 | 提供元 | 説明 |
| --- | --- | --- |
| LinkedIn 広告アカウント | [LinkedIn](https://www.linkedin.com/campaignmanager) | ブランドに関連付けられたアクティブな LinkedIn 広告アカウント。<br><br>そのアカウントにアクセスして使用するための関連する LinkedIn の利用規約に同意していること、および LinkedIn 管理者によってオーディエンスを管理するための適切な権限が付与されていることを確認してください。 |
| LinkedIn の利用規約とポリシー | LinkedIn | LinkedIn Audience Sync の使用に関連する LinkedIn の必須規約、ポリシー、ガイドライン、およびドキュメント（参照によって組み込まれるものを含む）を遵守することに同意するものとします。これには、LinkedIn のサービス規約、広告契約、データ処理契約、プロフェッショナルコミュニティガイドラインが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合 {#integration}

### ステップ 1: LinkedIn への接続 {#step-1-connect-to-linkedin}

{% alert important %}
LinkedIn を Braze アカウントに接続するには、[「Admin」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)が必要です。
{% endalert %}

Braze ダッシュボードで、**テクノロジーパートナー**に移動し、**LinkedIn** を選択します。**LinkedIn Audience Sync** セクションで、**Connect LinkedIn** を選択します。

![Braze の LinkedIn テクノロジーページ。概要セクションと LinkedIn Audience Sync セクションがあり、「Connected LinkedIn」ボタンが表示されています。]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

次に、LinkedIn OAuth ページにリダイレクトされ、Audience Sync 統合に関連する権限を Braze に承認します。**Confirm** を選択すると、Braze にリダイレクトされ、同期する LinkedIn 広告アカウントを選択します。

![接続する広告アカウントとして「Braze Self Service」が選択されています。]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

接続に成功すると、パートナーページに戻り、接続されているアカウントの確認や既存のアカウントの切断ができます。

![LinkedIn アカウントが正常に接続された状態。]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

LinkedIn 接続は Braze ワークスペースレベルで適用されます。LinkedIn 管理者が LinkedIn 広告アカウントからユーザーを削除した場合、Braze は無効なトークンを検出します。その結果、LinkedIn を使用しているアクティブな Canvasesにはエラーが表示され、Braze はユーザーを同期できなくなります。

### ステップ 2: Canvasのエントリ条件を設定する {#step-2-configure-your-canvas-entry-criteria}

広告トラッキング用のオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したり、[CCPA](https://oag.ca.gov/privacy/ccpa) の「販売・共有の拒否」権利などのプライバシー法に準拠したりすることが必要になる場合があります。マーケターは、Canvasのエントリ条件内でユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかのオプションを示します。

[Braze SDKを通じて iOS IDFA を]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection)収集した場合、**Ads Tracking Enabled** フィルターを使用できます。値を `true` に選択すると、オプトインしたオーディエンス同期の宛先にのみユーザーを送信します。

![「Ad Tracking Enabled is true」というフィルターを持つエントリオーディエンス。]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、Canvasのエントリ条件にこれらをフィルターとして含める必要があります。

![「opted_in_marketing」が「true」と等しいエントリオーディエンスを持つ Canvas。]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Braze プラットフォーム内でこれらのデータ保護法に準拠する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance/)を参照してください。

### ステップ 3: LinkedIn を使用したオーディエンス同期ステップの追加 {#step-3-add-an-audience-sync-step-with-linkedin}

Canvasにコンポーネントを追加し、「Audience Sync」を選択します。**Custom Audience** ボタンをクリックしてコンポーネントエディターを開きます。

![利用可能なコンポーネントのリストが表示された Canvas エディター。]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![選択されたオーディエンス同期コンポーネント。]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### ステップ 4: 同期設定 {#step-4-sync-setup}

**LinkedIn** を目的のオーディエンス同期パートナーとして選択します。

![「Set up Audience Sync」の詳細。複数のパートナーから選択可能。]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

次に、目的の LinkedIn 広告アカウントを選択します。**Choose a New or Existing Audience** ドロップダウンで、新しいオーディエンスまたは既存のオーディエンスの名前を入力します。

![広告アカウントとして Braze が選択された状態で LinkedIn に同期するオーディエンス。]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab 新規オーディエンスの作成 %}

**新規オーディエンスの作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience** を選択し、LinkedIn と同期するフィールドを選択します。この統合では、現在以下をサポートしています。
- メール
- 名前と苗字
- Android GAID

次に、ステップエディターの下部にある **Create Audience** ボタンをクリックしてオーディエンスを保存します。

![「leads」オーディエンスの例。Braze 広告アカウントが選択され、「leads」オーディエンスにユーザーを追加するアクションが設定されており、メール、Android GAID、名前と苗字がマッチングフィールドとして選択されています。]({% image_buster /assets/img/linkedin/linkedin10.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Braze はステップエディターの上部に通知を表示します。オーディエンスは下書きモードで作成されるため、ユーザーは後で Canvas ジャーニーでユーザーの削除のためにこのオーディエンスを参照できます。

![「leads」オーディエンスが作成されたことの確認。]({% image_buster /assets/img/linkedin/linkedin9.png %})

新しいオーディエンスを使用して Canvasを起動すると、オーディエンス同期コンポーネントに入る時点で、Braze はユーザーをほぼリアルタイムで同期します。

{% endtab %}
{% tab 既存のオーディエンスとの同期 %}

**既存のオーディエンスとの同期**<br>
Braze は、既存の LinkedIn オーディエンスにユーザーを追加して、オーディエンスを最新の状態に保つ機能も提供しています。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**Add to the Audience** を選択します。Braze は、オーディエンス同期コンポーネントに入ると、ほぼリアルタイムでユーザーを追加します。

![カスタムオーディエンス Canvas ステップの展開ビュー。目的の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### ステップ 5: Canvasの起動 {#step-5-launch-canvas}

LinkedIn へのオーディエンス同期を設定したら、Canvasを起動するだけです！新しいオーディエンスが作成され、オーディエンス同期ステップを通過するユーザーは LinkedIn のこのオーディエンスに送られます。Canvasに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

LinkedIn でオーディエンスを表示するには、広告アカウントに移動し、ナビゲーションの **Assets** セクションで **Audiences** を選択します。**Audiences** ページでは、300人以上のメンバーに達した後、各オーディエンスのサイズを確認できます。

![指定したオーディエンスの指標を一覧表示する LinkedIn ページ。]({% image_buster /assets/img/linkedin/linkedin8.png %})

## ユーザーの同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに到達すると、Braze は LinkedIn の API レート制限を尊重しながらほぼリアルタイムで同期します。Braze は 5 秒ごとにできるだけ多くのユーザーをバッチ処理してから LinkedIn に送信します。

LinkedIn の API レート制限では、1 秒あたり最大 10 クエリ、1 リクエストあたり 100,000 ユーザーが許可されています。顧客がこの制限に達すると、Braze は最大約 13 時間同期を再試行します。それでも同期できない場合、Braze はこれらのユーザーを「エラーが発生したユーザー」指標に一覧表示します。

## 分析の理解 {#understanding-analytics}

次の表には、オーディエンス同期コンポーネントからの分析をよりよく理解するための指標と説明が含まれています。

| 指標 | 説明 |
| ------ | ----------- |
| 入力 | LinkedIn と同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数。Canvas ブランチの最後のステップである場合、すべてのユーザーが自動的に進みます。 |
| ユーザーの同期 | LinkedIn に正常に同期されたユーザーの数。 |
| 同期されていないユーザー | マッチングフィールドの不足により同期されなかったユーザーの数。 |
| 保留中のユーザー | Braze が LinkedIn に同期するために現在処理中のユーザーの数。 |
| エラーが発生したユーザー | 約 13 時間の再試行後に API エラーのため LinkedIn に同期されなかったユーザーの数。エラーの原因としては、LinkedIn トークンが無効である場合や、LinkedIn でオーディエンスが削除された場合などが考えられます。 |
| Canvasの終了 | Canvasを終了したユーザーの数。これは、Canvasの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
一括フラッシャーと 13 時間の再試行により、同期されたユーザーとエラーが発生したユーザーの指標のレポートに遅延が発生することに注意してください。
{% endalert %}

{% alert important %}
LinkedIn は、プラットフォーム内のマッチ率に関する追加の指標を提供しています。特定のオーディエンス同期のマッチを確認するには、オーディエンス同期のステップ指標を選択して、**Canvas Step Details** ページに移動します。
<br><br>
パートナーとして **LinkedIn**、広告アカウント、およびオーディエンスを選択して、LinkedIn からのオーディエンスサイズとマッチ率を確認します。

![オーディエンス同期ステップ指標の例。10,000 人のユーザーが入力されています。]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### オーディエンスサイズが LinkedIn に反映されるまでにどのくらいの時間がかかりますか？ {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

LinkedIn アカウント内のオーディエンスを表示するまでに最大 48 時間の遅延があります。

### LinkedIn の広告アカウントに反映されるオーディエンスの最小サイズはどのくらいですか？ {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

LinkedIn アカウントにオーディエンスサイズが反映されるためには、少なくとも 300 人のメンバーを含む必要があります。

### 無効なトークンエラーが表示された場合、次に何をすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

LinkedIn パートナーページで LinkedIn アカウントを切断して再接続できます。同期する広告アカウントに対する適切な権限があることを LinkedIn 管理者に確認してください。

### Canvasを起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

LinkedIn 広告アカウントが LinkedIn パートナーページで Braze に正常に接続されていることを確認してください。次に、広告アカウントの選択、新しいオーディエンスの名前の入力、マッチングするフィールドの選択が完了していることを確認します。

### ユーザーを LinkedIn に渡した後、ユーザーがマッチしたかどうかを知るにはどうすればよいですか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedIn は、ダッシュボードでマッチ率に関する情報を提供しています。LinkedIn の **Audiences** セクションで確認できます。LinkedIn オーディエンスのマッチ率は、オーディエンス同期ステップの Canvas ステップの詳細で確認できます。

### LinkedIn で対応できるオーディエンスの数はどのくらいですか？ {#how-many-audiences-can-linkedin-support}

現在、LinkedIn 広告アカウントのオーディエンス数に制限はありません。

### Segmentが BUILDING ステータスに留まり、更新されないのはなぜですか？ {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Segmentは、下書きまたはアクティブな Campaignで 30 日間継続的に使用されない場合、未使用と見なされ ARCHIVED に設定されます。このため、更新が ARCHIVED のSegmentにストリーミングされると、Segmentが BUILDING 状態に「スタック」したように見えることがあります。BUILDING 状態に移行し、再度アーカイブされる直前に、新しい更新が未使用のSegmentにストリーミングされます。