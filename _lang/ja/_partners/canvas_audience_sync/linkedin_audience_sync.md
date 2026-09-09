---
nav_title: LinkedIn
article_title: キャンバスオーディエンスのLinkedInへの同期
alias: /linkedin_audience_sync/
description: "このリファレンス記事では、Braze Audience Sync to LinkedInを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
tool:
  - Canvas
page_order: 4

---

# LinkedInへのオーディエンス同期 {#audience-sync-to-linkedin}

Braze Audience Sync to LinkedInを使用すると、ブランドはBraze統合のユーザーデータをLinkedIn顧客リストに追加して、行動トリガー、セグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいてBrazeキャンバスでメッセージをトリガーするために通常使用する基準（プッシュ、メール、SMS、Webhookなど）を使用して、LinkedIn顧客リスト内の該当ユーザーに対して広告をトリガーできるようになりました。

**オーディエンス同期の一般的なユースケース**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

この機能により、ブランドはLinkedInと共有する特定のファーストパーティデータをコントロールできます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

## 前提条件 {#prerequisites}

キャンバスで LinkedIn オーディエンス同期ステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認する必要があります。

| 要件 | Origin | 説明 |
| --- | --- | --- |
| Audience Sync Pro | Braze | LinkedIn は [Audience Sync Pro]({{site.baseurl}}/partners/canvas_audience_sync/overview#audience-sync-pro) パートナーです。広告アカウントを接続する前に、**テクノロジーパートナー**ページで Audience Sync Pro の割り当てから LinkedIn を選択してください。購入の詳細については、Braze アカウントマネージャーにお問い合わせください。 |
| LinkedIn 広告アカウント | [LinkedIn](https://www.linkedin.com/campaignmanager) | ブランドに紐付けられたアクティブな LinkedIn 広告アカウント。<br><br>そのアカウントにアクセスして使用するために、関連する LinkedIn の利用規約に同意していることを確認してください。LinkedIn 管理者は、次のいずれかの広告アカウントロールを付与する必要があります: Account Billing Admin、Account Manager、キャンペーン Manager、または Creative Manager。 |
| LinkedIn の利用規約とポリシー | LinkedIn | LinkedIn オーディエンス同期の使用に関連する LinkedIn の必要な利用規約、ポリシー、ガイドライン、およびドキュメント（参照により組み込まれる利用規約、ポリシー、ガイドライン、およびドキュメントを含む）に準拠することに同意してください。これには、LinkedIn の Services Terms、Ads Agreement、Data Processing Agreement、および Professional Community Guidelines が含まれる場合があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：LinkedInに接続する {#step-1-connect-to-linkedin}

{% alert important %}
LinkedInをBrazeアカウントに接続するには、[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)が必要です。
{% endalert %}

Brazeダッシュボードで**テクノロジーパートナー**に移動し、**LinkedIn**を選択します。**LinkedIn Audience Sync**セクションで**Connect LinkedIn**を選択します。

次にLinkedIn OAuthページにリダイレクトされ、Audience Sync連携に関連する権限をBrazeに付与します。**Confirm**を選択すると、Brazeにリダイレクトされ、同期するLinkedIn広告アカウントを選択できます。

![接続する広告アカウントとして「Braze Self Service」が選択されている画面。]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

正常に接続されると、パートナーページに戻り、接続されているアカウントの確認や既存アカウントの切断ができます。

![正常に接続されたLinkedInアカウント。]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

LinkedInの接続はBrazeワークスペースレベルで適用されます。LinkedIn管理者がLinkedIn広告アカウントからあなたを削除した場合、Brazeは無効なトークンを検出します。その結果、LinkedInを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2：キャンバスのエントリ条件を設定する {#step-2-configure-your-canvas-entry-criteria}

広告トラッキング用のオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したりすること、また[CCPA](https://oag.ca.gov/privacy/ccpa)の「販売または共有の拒否」権利などのプライバシー法に準拠することが必要な場合があります。マーケターは、キャンバスのエントリ条件内でユーザーの適格性に関連するフィルターを実装する必要があります。以下のオプションが役立ちます。

[Braze SDKを通じてiOS IDFAを収集]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)した場合、**Ads Tracking Enabled**フィルターを使用できます。値を`true`に設定して、オプトインしたユーザーのみをAudience Syncの送信先に送信します。iOS広告IDは、LinkedIn Audience Syncのマッチフィールドとしてサポートされていません。

![「Ad Tracking Enabled is true」のフィルターが設定されたエントリオーディエンス。]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、キャンバスのエントリ条件にフィルターとして含める必要があります。

![「opted_in_marketing」が「true」のエントリオーディエンスを持つキャンバス。]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Brazeプラットフォーム内でこれらのデータ保護法に準拠する方法について詳しくは、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance)を参照してください。

### ステップ3：LinkedInを使用したAudience Syncステップを追加する {#step-3-add-an-audience-sync-step-with-linkedin}

キャンバスにコンポーネントを追加し、Audience Syncを選択します。**Custom Audience**ボタンをクリックしてコンポーネントエディターを開きます。

### ステップ4：同期の設定 {#step-4-sync-setup}

1. Audience Syncパートナーとして**LinkedIn**を選択します。
2. 目的のLinkedIn広告アカウントを選択します。
3. **Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンス名を入力します。

{% tabs %}
{% tab 新しいオーディエンスを作成 %}

#### 新しいオーディエンスを作成する {#create-a-new-audience}

新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択して、LinkedInと同期するフィールドを選択します。この連携では、Brazeは現在以下をサポートしています：
- メール
- 姓名（名前マッチングを使用する場合は両方必須）
- Android GAID

iOS広告IDはLinkedInのマッチフィールドとしてサポートされていません。

次に、ステップエディターの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![選択されたBraze広告アカウント、「leads」オーディエンス、オーディエンスにユーザーを追加するアクション、およびメール、Android GAID、姓名をマッチフィールドとして設定した「leads」オーディエンスの例。]({% image_buster /assets/img/linkedin/linkedin10.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。ステップエディターで保存した後、キャンバスジャーニーの後のステップでこのオーディエンスを参照してユーザーの削除を行うことができます。

![「leads」オーディエンスが作成されたことの確認画面。]({% image_buster /assets/img/linkedin/linkedin9.png %})

新しいオーディエンスを使用してキャンバスを起動すると、Brazeは[バッチ処理とレイテンシー]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency)に従い、ユーザーがAudience Syncステップに入った時点で同期を行います。

{% endtab %}
{% tab 既存のオーディエンスと同期 %}

#### 既存のオーディエンスと同期する {#sync-with-an-existing-audience}

Brazeでは、既存のLinkedInオーディエンスにユーザーを追加したり削除したりして、オーディエンスを最新の状態に保つこともできます。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**Add to the Audience**または**Remove from the Audience**を選択します。Brazeは[バッチ処理とレイテンシー]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency)に従い、ユーザーがAudience Syncステップに入った時点で同期を行います。

![Custom Audienceキャンバスステップの展開ビュー。ここでは、目的の広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### ステップ5：キャンバスを起動する {#step-5-launch-canvas}

LinkedInへのAudience Syncの設定が完了したら、キャンバスを起動しましょう。新しいオーディエンスが作成され、Audience Syncステップを通過したユーザーがLinkedIn上のこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

LinkedInでオーディエンスを確認するには、広告アカウントに移動し、ナビゲーションの**Assets**セクションにある**Audiences**を選択します。**Audiences**ページでは、300メンバーを超えた後の各オーディエンスのサイズを確認できます。

![指定されたオーディエンスの以下のメトリクスが表示されたLinkedInページ。]({% image_buster /assets/img/linkedin/linkedin8.png %})

## ユーザー同期とレート制限の考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに到達すると、BrazeはLinkedInに送信する前にバッチ処理のためにユーザーをキューに入れます。Brazeがバッチをディスパッチする方法については、[バッチ処理とレイテンシー]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency)を参照してください。

Brazeは1回のリクエストにつき最大2,000人のユーザーをLinkedInに送信します。LinkedInのAPIレート制限がアカウントに適用された場合、Brazeは約13時間にわたって同期をリトライします。それでも同期できない場合、Brazeはこれらのユーザーをユーザーエラー指標に記録します。

## 分析の理解 {#understanding-analytics}

以下の表には、オーディエンス同期コンポーネントの分析をより深く理解するための指標と説明が含まれています。

| 指標 | 説明 |
| ------ | ----------- |
| エントリ済み | LinkedInに同期するためにこのコンポーネントにエントリしたユーザー数。 |
| 次のステップに進んだ | 次のコンポーネントがある場合、何人のユーザーが次のコンポーネントに進みましたか？キャンバスブランチの最後のステップである場合、すべてのユーザーが自動的に進みます。 |
| 同期されたユーザー | LinkedInに正常に同期されたユーザー数。 |
| 同期されなかったユーザー | マッチングに必要なフィールドが不足しているために同期されなかったユーザー数。 |
| 保留中のユーザー | 現在BrazeがLinkedInへの同期を処理中のユーザー数。 |
| エラーが発生したユーザー | 約13時間のリトライ後、APIエラーによりLinkedInに同期されなかったユーザー数。エラーの原因としては、無効なLinkedInトークンや、LinkedIn上でオーディエンスが削除された場合などが考えられます。 |
| キャンバスを退出 | キャンバスを退出したユーザー数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

{% alert important %}
同期されたユーザーとエラーが発生したユーザーの指標には、それぞれバッチ処理と13時間のリトライにより、レポートに遅延が生じることにご注意ください。
{% endalert %}

{% alert important %}
LinkedInは、プラットフォーム内でマッチ率に関する追加の指標を提供しています。特定のオーディエンス同期のマッチを確認するには、オーディエンス同期ステップの指標を選択して**キャンバスステップの詳細**ページに移動してください。
<br><br>
パートナーとして**LinkedIn**、広告アカウント、オーディエンスを選択すると、LinkedInからのオーディエンスサイズとマッチ率が表示されます。

![10,000人のエントリ済みユーザーを含むオーディエンス同期ステップの指標の例。]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### LinkedInでオーディエンスサイズが反映されるまでどのくらいかかりますか？ {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

LinkedInアカウント内でオーディエンスを確認できるようになるまで、最大48時間の遅延があります。

### LinkedInの広告アカウント内でオーディエンスサイズが反映されるための最小オーディエンスサイズはどれくらいですか？ {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

LinkedInアカウント内でオーディエンスサイズが反映されるには、オーディエンスに少なくとも300人のメンバーが含まれている必要があります。

### 無効なトークンエラーが表示された場合はどうすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

LinkedInパートナーページでLinkedInアカウントを切断し、再接続できます。同期したい広告アカウントへの適切な権限があることを、LinkedIn管理者に確認してください。

### キャンバスの起動が許可されないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

LinkedInパートナーページで、LinkedIn広告アカウントがBrazeに正常に接続されていることを確認してください。次に、広告アカウントを選択し、新しいオーディエンスの名前を入力し、マッチングするフィールドを選択していることを確認してください。

### ユーザーをLinkedInに送信した後、ユーザーがマッチしたかどうかはどのように確認できますか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedInはダッシュボードでマッチ率に関する情報を提供しています。LinkedInの**Audiences**セクションで確認できます。また、Audience Syncステップのキャンバスステップ詳細で、LinkedIn Audienceのマッチ率を確認できます。

### LinkedInはいくつのオーディエンスをサポートできますか？ {#how-many-audiences-can-linkedin-support}

現在、LinkedIn広告アカウント内のオーディエンス数に制限はありません。

### セグメントがBUILDINGステータスのまま更新されないのはなぜですか？ {#why-is-a-segment-stuck-in-building-status-and-not-updated}

セグメントは、下書きまたはアクティブなキャンペーンで30日間継続して使用されない場合、未使用とみなされARCHIVEDに設定されます。このため、ARCHIVEDセグメントに更新がストリーミングされるとBUILDING状態に移行し、再度アーカイブされる直前に、未使用のセグメントに新しい更新がストリーミングされるため、セグメントがBUILDINGで「止まっている」ように見えることがあります。