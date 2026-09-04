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

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## 前提条件 {#prerequisites}

キャンバスで LinkedIn オーディエンス同期ステップを設定する前に、以下の項目が作成、完了、または承認されていることを確認する必要があります。

| 要件 | Origin | 説明 |
| --- | --- | --- |
| LinkedIn 広告アカウント | [LinkedIn](https://www.linkedin.com/campaignmanager) | ブランドに紐づけられたアクティブな LinkedIn 広告アカウント。<br><br>そのアカウントにアクセスして使用するために、関連する LinkedIn の利用規約に同意していること、また LinkedIn 管理者からオーディエンス管理に必要な適切な権限が付与されていることを確認してください。 |
| LinkedIn の利用規約とポリシー | LinkedIn | LinkedIn オーディエンス同期の使用に関連する LinkedIn の必須の利用規約、ポリシー、ガイドライン、およびドキュメント（参照により組み込まれるものを含む）に準拠することに同意してください。これには、LinkedIn のサービス利用規約、広告契約、データ処理契約、およびプロフェッショナルコミュニティガイドラインが含まれる場合があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：LinkedInに接続する {#step-1-connect-to-linkedin}

{% alert important %}
LinkedInをBrazeアカウントに接続するには、[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**テクノロジーパートナー**に移動し、**LinkedIn**を選択します。**LinkedIn Audience Sync**セクションで、**Connect LinkedIn**を選択します。

![BrazeのLinkedInテクノロジーページには、概要セクションとLinkedIn Audience Syncセクションがあり、Connected LinkedInボタンが表示されています。]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

その後、LinkedIn OAuthページにリダイレクトされ、Audience Sync連携に関連する権限をBrazeに付与します。**Confirm**を選択すると、Brazeに戻り、同期するLinkedIn広告アカウントを選択できます。

![接続する広告アカウントとして「Braze Self Service」が選択されています。]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

正常に接続されると、パートナーページに戻り、接続されているアカウントの確認や既存アカウントの切断ができます。

![正常に接続されたLinkedInアカウント。]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

LinkedInの接続はBrazeワークスペースレベルで適用されます。LinkedIn管理者がLinkedIn広告アカウントからあなたを削除した場合、Brazeは無効なトークンを検出します。その結果、LinkedInを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

### ステップ2：キャンバスのエントリ条件を設定する {#step-2-configure-your-canvas-entry-criteria}

広告トラッキング用のオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したりすることや、[CCPA](https://oag.ca.gov/privacy/ccpa)の「販売または共有の拒否」権利などのプライバシー法に準拠することが必要になる場合があります。マーケターは、キャンバスのエントリ条件内にユーザーの適格性に関する適切なフィルターを実装する必要があります。以下のオプションが役立ちます。

[Braze SDKを通じてiOS IDFAを収集]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)している場合、**Ads Tracking Enabled**フィルターを使用できます。値を`true`に設定すると、オプトインしたユーザーのみをAudience Syncの送信先に送信します。

![「Ad Tracking Enabled is true」フィルターが設定されたエントリオーディエンス。]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、これらをフィルターとしてキャンバスのエントリ条件に含める必要があります。

![エントリオーディエンスが「opted_in_marketing」が「true」に設定されたキャンバス。]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Brazeプラットフォーム内でこれらのデータ保護法に準拠する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance)を参照してください。

### ステップ3：LinkedInを使用したAudience Syncステップを追加する {#step-3-add-an-audience-sync-step-with-linkedin}

キャンバスにコンポーネントを追加し、Audience Syncを選択します。**Custom Audience**ボタンをクリックして、コンポーネントエディターを開きます。

![利用可能なコンポーネントのリストが表示されたキャンバスエディター。]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![選択されたAudience Syncコンポーネント。]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### ステップ4：同期の設定 {#step-4-sync-setup}

希望するAudience Syncパートナーとして**LinkedIn**を選択します。

![複数のパートナーから選択できる「Set up Audience Sync」の詳細。]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

次に、希望するLinkedIn広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンス名を入力します。

![広告アカウントとしてBrazeが選択されたLinkedInへのAudience Sync。]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab 新しいオーディエンスを作成 %}

**新しいオーディエンスを作成**<br>
新しいオーディエンスの名前を入力し、**Add Users to Audience**を選択して、LinkedInと同期するフィールドを選択します。この連携では、現在以下をサポートしています：
- メール
- 姓名
- Android GAID

次に、ステップエディターの下部にある**Create Audience**ボタンをクリックしてオーディエンスを保存します。

![選択されたBraze広告アカウント、「leads」オーディエンス、オーディエンスにユーザーを追加するアクション、およびマッチするフィールドとしてメール、Android GAID、姓名が設定された「leads」オーディエンスの例。]({% image_buster /assets/img/linkedin/linkedin10.png %})

オーディエンスが正常に作成された場合、またはエラーが発生した場合、Brazeはステップエディターの上部に通知を表示します。オーディエンスは下書きモードで作成されるため、ユーザーはキャンバスジャーニーの後半でユーザー削除のためにこのオーディエンスを参照できます。

![「leads」オーディエンスが作成されたことの確認。]({% image_buster /assets/img/linkedin/linkedin9.png %})

新しいオーディエンスを含むキャンバスを起動すると、BrazeはユーザーがAudience Syncコンポーネントに入るとほぼリアルタイムで同期します。

{% endtab %}
{% tab 既存のオーディエンスと同期 %}

**既存のオーディエンスと同期**<br>
Brazeは、既存のLinkedInオーディエンスにユーザーを追加して、オーディエンスを最新の状態に保つ機能も提供しています。既存のオーディエンスと同期するには、ドロップダウンに既存のオーディエンス名を入力し、**Add to the Audience**を選択します。Brazeは、ユーザーがAudience Syncコンポーネントに入るとほぼリアルタイムでユーザーを追加します。

![Custom Audienceキャンバスステップの展開ビュー。ここでは、希望する広告アカウントと既存のオーディエンスが選択されています。]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### ステップ5：キャンバスを起動する {#step-5-launch-canvas}

LinkedInへのAudience Syncを設定したら、キャンバスを起動します。新しいオーディエンスが作成され、Audience Syncステップを通過するユーザーはLinkedIn上のこのオーディエンスに渡されます。キャンバスに後続のコンポーネントが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

LinkedInでオーディエンスを確認するには、広告アカウントに移動し、ナビゲーションの**Assets**セクションの下にある**Audiences**を選択します。**Audiences**ページから、300人以上のメンバーに達した後の各オーディエンスのサイズを確認できます。

![指定されたオーディエンスの以下のメトリクスを一覧表示するLinkedInページ。]({% image_buster /assets/img/linkedin/linkedin8.png %})

## ユーザー同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに到達すると、BrazeはLinkedInのAPIレート制限を遵守しながら、ほぼリアルタイムでユーザーを同期します。Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理し、LinkedInに送信します。

LinkedInのAPIレート制限では、1秒あたり10クエリ、1リクエストあたり100,000ユーザーまでに制限されています。顧客がこの制限に達した場合、Brazeは約13時間にわたって同期を再試行します。それでも同期できない場合、Brazeはこれらのユーザーをユーザーエラー指標に記録します。

## 分析について {#understanding-analytics}

以下の表には、オーディエンス同期コンポーネントの分析をより深く理解するための指標と説明が含まれています。

| 指標 | 説明 |
| ------ | ----------- |
| エントリ済み | LinkedInに同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進んだ | 次のコンポーネントがある場合、何人のユーザーが次のコンポーネントに進みましたか？キャンバスブランチの最後のステップである場合、すべてのユーザーが自動的に進みます。 |
| 同期済みユーザー | LinkedInに正常に同期されたユーザーの数。 |
| 未同期ユーザー | マッチするフィールドが不足しているため同期されなかったユーザーの数。 |
| 保留中のユーザー | 現在BrazeがLinkedInへの同期を処理中のユーザーの数。 |
| エラーが発生したユーザー | 約13時間のリトライ後にAPIエラーによりLinkedInに同期されなかったユーザーの数。エラーの原因としては、無効なLinkedInトークンや、LinkedIn上でオーディエンスが削除された場合などが考えられます。 |
| キャンバスを退出 | キャンバスを退出したユーザーの数。これは、キャンバスの最後のステップがオーディエンス同期コンポーネントである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析について" }

{% alert important %}
同期済みユーザーとエラーが発生したユーザーの指標については、一括フラッシャーと13時間のリトライにより、それぞれレポートに遅延が生じることに注意してください。
{% endalert %}

{% alert important %}
LinkedInは、プラットフォーム内でマッチ率に関する追加の指標を提供しています。特定のオーディエンス同期のマッチを確認するには、オーディエンス同期ステップの指標を選択して**キャンバスステップの詳細**ページに移動します。
<br><br>
パートナーとして**LinkedIn**、広告アカウント、およびオーディエンスを選択すると、LinkedInからのオーディエンスサイズとマッチ率を確認できます。

![10,000人のエントリ済みユーザーを含むオーディエンス同期ステップ指標の例。]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### LinkedInでオーディエンスサイズが反映されるまでどのくらいかかりますか？ {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

LinkedInアカウント内でオーディエンスを確認できるようになるまで、最大48時間の遅延があります。

### LinkedInの広告アカウントにオーディエンスサイズが反映されるための最小オーディエンスサイズはどのくらいですか？ {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

LinkedInアカウント内でオーディエンスサイズが反映されるには、オーディエンスに少なくとも300人のメンバーが含まれている必要があります。

### 無効なトークンエラーが表示された場合はどうすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

LinkedInパートナーページでLinkedInアカウントを切断してから再接続できます。同期したい広告アカウントに対する適切な権限があることをLinkedIn管理者に確認してください。

### キャンバスが起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

LinkedInパートナーページで、LinkedIn広告アカウントがBrazeに正常に接続されていることを確認してください。次に、広告アカウントを選択し、新しいオーディエンスの名前を入力し、マッチングするフィールドを選択していることを確認してください。

### ユーザーをLinkedInに渡した後、ユーザーがマッチしたかどうかはどうすればわかりますか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

LinkedInはダッシュボードでマッチ率に関する情報を提供しています。LinkedInの**オーディエンス**セクションで確認できます。また、Audience Syncステップのキャンバスステップ詳細でLinkedInオーディエンスのマッチ率を確認できます。

### LinkedInはいくつのオーディエンスをサポートできますか？ {#how-many-audiences-can-linkedin-support}

現在、LinkedIn広告アカウント内のオーディエンス数に制限はありません。

### セグメントがBUILDINGステータスのまま更新されないのはなぜですか？ {#why-is-a-segment-stuck-in-building-status-and-not-updated}

セグメントは、下書きまたはアクティブなキャンペーンで30日間継続的に使用されない場合、未使用とみなされARCHIVEDに設定されます。このため、ARCHIVEDセグメントに更新がストリーミングされるとBUILDING状態に移行し、再びアーカイブされる直前に未使用のセグメントに新しい更新がストリーミングされるため、セグメントがBUILDINGのまま「停滞」しているように見えることがあります。