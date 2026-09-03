---
nav_title: Facebook
article_title: キャンバスオーディエンスのFacebook同期
description: "このリファレンス記事では、Braze Audience Sync to Facebookを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 2
alias: /audience_sync_facebook/

tool:
  - Canvas

---

# オーディエンスのFacebook同期 {#audience-sync-to-facebook}

> Braze Audience Sync to Facebookを使用すると、Braze統合からのユーザーデータをFacebookカスタムオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。

ユーザーデータに基づいてBrazeキャンバスでメッセージ（プッシュ、メール、SMS、Webhook）をトリガーするために通常使用する基準はすべて、カスタムオーディエンスを使用してFacebook内の該当ユーザーに対して広告をトリガーするためにも使用できるようになりました。例えば、FacebookへのAudience Syncを設定する場合、メール、電話、名、姓など、さまざまなファーストパーティフィールドを使用できます。

**カスタムオーディエンスの同期の一般的なユースケース**：

- 複数のチャネルを通じて高価値ユーザーをターゲットにして、購入やエンゲージメントを促進する。
- 他のマーケティングチャネルに対して反応が薄いユーザーをリターゲティングする。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成する。
- 新規ユーザーの獲得を効率化するための類似オーディエンスを作成する。

この機能により、ブランドはFacebookと共有する特定のファーストパーティデータを制御できます。Brazeでは、ファーストパーティデータを共有できる統合と共有できない統合を最大限に考慮しています。詳細については、[プライバシーポリシー](https://www.braze.com/privacy)を参照してください。

## ユーザー同期とレート制限に関する考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがオーディエンス同期ステップに到達すると、BrazeはFacebookのMarketing APIレート制限を遵守しながら、ほぼリアルタイムでユーザーを同期します。Brazeは5秒ごとにできるだけ多くのユーザーをバッチ処理し、Facebookに送信します。

FacebookのMarketing APIレート制限では、1時間あたり1つの広告アカウントにつき&#126;190,000件以下のAPIリクエストしか許可されていません。顧客がこの制限に達した場合、Brazeは最大&#126;13時間にわたって同期をリトライします。それでも同期ができない場合、Brazeはこれらのユーザーをユーザーエラー指標に記録します。

## 前提条件 {#prerequisites}

キャンバスでFacebook オーディエンスステップを設定する前に、以下の項目が作成・完了していることを確認する必要があります。

| 要件 | Origin | 説明 |
| ----------- | ------ | ----------- |
| Facebook ビジネスマネージャー | [Facebook](https://www.facebook.com/business/help/113163272211510) | ブランドのFacebookアセット（広告アカウント、ページ、アプリなど）を管理するための一元的なツールです。 |
| Facebook 広告アカウント | [Facebook](https://www.facebook.com/business/help/910137316041095) | ブランドのビジネスマネージャーに紐づけられたアクティブなFacebook広告アカウントです。<br><br>Facebook ビジネスマネージャーの管理者が、Brazeで使用する予定のFacebook広告アカウントに対して「キャンペーンの管理」または「広告アカウントの管理」権限を付与していることを確認してください。また、広告アカウントの利用規約に同意していることも確認してください。 |
| Facebook カスタムオーディエンス規約 | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Brazeで使用する予定のFacebook広告アカウントについて、Facebookのカスタムオーディエンス規約に同意してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：Facebookに接続する {#step-1-connect-to-facebook}

{% alert important %}
FacebookをBrazeアカウントに接続するには、[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)が必要です。
{% endalert %}

Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Facebook**を選択します。Facebookオーディエンスエクスポートの下で、**Connect Facebook**を選択します。

![概要セクションとFacebookオーディエンスエクスポートセクションを含むBrazeのFacebookテクノロジーページ。Connect Facebookボタンが表示されています。]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Facebook oAuthダイアログウィンドウが表示され、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成する権限を承認します。

![最初のFacebookダイアログボックス。「Xとして接続」と表示され、XはFacebookのユーザー名です。]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![2番目のFacebookダイアログボックス。広告アカウントの広告を管理する権限を求めています。]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

BrazeをFacebookアカウントにリンクした後、Brazeワークスペース内で同期したい広告アカウントを選択します。接続が完了すると、パートナーページに戻り、接続されているアカウントの確認や既存アカウントの切断ができます。

![正常に接続された広告アカウントが表示されている、更新されたFacebookテクノロジーパートナーページ。]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Facebook接続はBrazeワークスペースレベルで適用されます。Facebook管理者がFacebook Business Managerからあなたを削除したり、接続されたFacebookアカウントへのアクセスを取り消したりした場合、Brazeは無効なトークンを検出します。その結果、Facebookオーディエンスコンポーネントを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

{% alert important %}
以前に[広告管理](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management)および[広告管理標準アクセス](https://developers.facebook.com/docs/marketing-api/access#standard)のFacebookアプリレビュープロセスを完了しているお客様の場合、システムユーザートークンはFacebookオーディエンスコンポーネントで引き続き有効です。Facebookパートナーページからはシステムユーザートークンの編集や取り消しはできません。代わりに、Facebookアカウントを接続して、Brazeワークスペース内のFacebookシステムユーザートークンを置き換えることができます。

<br><br>Facebook oAuth設定は、[セグメントを使用したFacebookエクスポート]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites)にも適用されます。
{% endalert %}

### ステップ2：カスタムオーディエンスの利用規約に同意する {#step-2-accept-custom-audiences-terms-of-service}

キャンバスを構築する前に、以下のリンクからFacebookの利用規約に同意する必要があります。

- **個人アカウントの顧客リストカスタムオーディエンス利用規約：** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`
- **ビジネスアカウントのFacebookビジネスツール利用規約：** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`

![顧客リストカスタムオーディエンスの同意が必要な利用規約の例。]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Facebookビジネスツールの同意が必要な利用規約の例。]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

連携時のFacebookアカウントの監査について詳しくは、[FAQセクション](#terms)を参照してください。

### ステップ3：キャンバスにFacebookオーディエンスコンポーネントを追加する {#step-3-add-a-facebook-audience-component-in-canvas}

キャンバスにコンポーネントを追加し、**Facebook Audience**を選択します。

![キャンバスに追加できるコンポーネントのリスト。]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![オーディエンス同期コンポーネント。]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### ステップ4：同期の設定 {#step-4-sync-setup}

**Custom Audience**ボタンを選択してコンポーネントエディターを開きます。次に、オーディエンス同期パートナーとして**Facebook**を選択します。

![パートナーを選択するオプションが表示された「オーディエンス同期の設定」画面。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

目的のFacebook広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンス名を入力します。

{% tabs %}
{% tab 新しいオーディエンスを作成 %}

1. 新しいカスタムオーディエンスの名前を入力します。
2. **Add Users to Audience**を選択し、Facebookと同期するフィールドを選択します。
3. 次に、**Create Audience**を選択してオーディエンスを保存します。

![メール、電話番号、名、姓の情報をマッチングするオーディエンス同期の設定。]({% image_buster /assets/img/audience_sync/fb_sync.png %})

オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合は、ステップエディターの上部に通知が表示されます。オーディエンスは下書きモードで作成されるため、キャンバスジャーニーの後半でユーザー削除のためにこのオーディエンスを参照することもできます。

新しいオーディエンスを含むキャンバスを起動すると、Brazeはキャンバスの起動時に新しいカスタムオーディエンスを作成し、その後ユーザーがオーディエンス同期ステップに入るとほぼリアルタイムで同期します。

各オーディエンス同期ステップは、そのステップで設定されたFacebookオーディエンスにマッピングされます。キャンバスが再度実行される場合（例えば、定期スケジュールで）、Brazeは対象ユーザーを同じオーディエンスに同期します。キャンバスの実行ごとに新しいFacebookオーディエンスが作成されるわけではありません。

{% endtab %}
{% tab 既存のオーディエンスと同期 %}

Brazeでは、既存のFacebookカスタムオーディエンスにユーザーを追加または削除して、オーディエンスを最新の状態に保つことができます。既存のオーディエンスと同期するには、以下の手順を実行します。

1. ドロップダウンに既存のオーディエンス名を入力します。
2. **Add to the Audience**または**Remove from the Audience**のいずれかを選択します。
3. ユーザーがFacebookオーディエンスステップに入ると、Brazeはほぼリアルタイムでユーザーを追加または削除します。

![メール、電話番号、名、姓の情報を削除するオーディエンス同期の設定。]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebookでは、オーディエンスサイズが小さすぎる（通常1,000ユーザー未満）カスタムオーディエンスからのユーザー削除を禁止しています。そのため、オーディエンスが適切なサイズに達するまで、Brazeはオーディエンス同期ステップからの削除のためにユーザーを同期できません。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ5：キャンバスを起動する {#step-5-launch-canvas}

Facebookオーディエンスコンポーネントの設定が完了したら、キャンバスを起動します。新しいカスタムオーディエンスが作成され、Facebookオーディエンスステップを通過するユーザーはFacebook上のこのカスタムオーディエンスに渡されます。キャンバスに後続のステップが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Facebookオーディエンスマネージャーのカスタムオーディエンスの**履歴**タブには、Brazeからオーディエンスに送信されたユーザー数が反映されます。ユーザーがステップに再度入った場合、再びFacebookに送信されます。

![オーディエンスの詳細と、特定のFacebookオーディエンスの履歴タブ。アクティビティ、アクティビティの詳細、変更された項目、日時の列を含むオーディエンス履歴テーブルが表示されています。]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## 分析の理解 {#understanding-analytics}

以下の表には、Audience Sync コンポーネントの分析をより深く理解するための指標と説明が含まれています。

| 指標 | 説明 |
| --- | --- |
| 入場済み | Facebook に同期するためにこのコンポーネントに入ったユーザーの数です。 |
| 次のステップに進んだ | 次のコンポーネントがある場合、そこに進んだユーザーの数です。キャンバスブランチの最後のステップである場合、すべてのユーザーが自動的に進みます。 |
| 同期済みユーザー | Facebook に正常に同期されたユーザーの数です。 |
| 未同期ユーザー | マッチングに必要なフィールドが不足しているため同期されなかったユーザーの数です。フィールドは「OR」演算子を使用してマッチングされるため、ユーザーが Facebook のフィールドのうち1つでも持っていれば、他のすべてのフィールドでマッチしなくても Facebook はそのユーザーをマッチングします。 |
| 保留中のユーザー | 現在 Braze が Facebook への同期を処理中のユーザーの数です。 |
| エラーが発生したユーザー | 約13時間のリトライ後に API エラーにより Facebook に同期されなかったユーザーの数です。エラーの原因としては、無効な Facebook トークンや、Facebook 上でカスタムオーディエンスが削除された場合などが考えられます。 |
| キャンバスを退出 | キャンバスを退出したユーザーの数です。これは、キャンバスの最後のステップが Facebook ステップである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

{% alert important %}
内部処理のため、同期済みユーザーおよびエラーが発生したユーザーの指標のレポートには遅延が生じます。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### オーディエンス同期パートナーのダッシュボードにオーディエンスが反映されるまでどのくらいかかりますか？ {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

オーディエンスが反映されるまでの時間は、パートナーによって異なります。すべてのネットワークはBrazeからのリクエストを処理し、ユーザーのマッチングを試みます。カスタムオーディエンスの更新には最大24時間かかる場合があります。

### 無効なトークンエラーが表示された場合、どうすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Facebookパートナーページで、Facebookアカウントを切断してから再接続してください。同期したい広告アカウントに対する適切な権限があることを、Facebook Business Managerの管理者に確認してください。

### キャンバスを起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

- システムユーザートークンが認証されており、Facebook Business Managerで目的の広告アカウントにアクセスできることを確認してください。
- 広告アカウントを選択し、新しいカスタムオーディエンスの名前を入力し、マッチングするフィールドを選択していることを確認してください。
- Facebookのカスタムオーディエンスの上限（500件）に達している可能性があります。キャンバスを使用して新しいカスタムオーディエンスを作成する前に、Facebook Audience Managerで不要なものを削除してください。

### ユーザーをFacebookに渡した後、ユーザーがマッチしたかどうかはどうすればわかりますか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

Facebookはプライバシー上の理由から、この情報を提供していません。

### Brazeは価値ベースのカスタムオーディエンスをサポートしていますか？ {#does-braze-support-value-based-custom-audiences}

現時点では、価値ベースのカスタムオーディエンスはBrazeでサポートされていません。{% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### Brazeはオーディエンス同期パートナーにデータを送信する前にハッシュ化しますか？ {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

メールデータが正規化されると、BrazeはSHA256でハッシュ化します。

**IDFA/AAID/電話番号：** BrazeはSHA256でハッシュ化します。同期するオーディエンスタイプは、常に以下のいずれかです。

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256

頻度に関しては、Brazeは同期の準備として、ユーザーがユーザージャーニーのオーディエンス同期ステップに入った時点でのみ、ユーザーの個人識別情報（PII）をハッシュ化します。

### 価値ベースの類似カスタムオーディエンスの同期に関する問題を解決するにはどうすればよいですか？ {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

現時点では、価値ベースの類似カスタムオーディエンスはBrazeでサポートされていません。このオーディエンスに同期しようとすると、オーディエンス同期ステップでエラーが発生する可能性があります。この問題を解決するには、以下のステップに従ってください。

1. Facebook Ad Managerダッシュボードに移動し、**Audiences** を選択します。
2. **Create audience** > **Custom audience** を選択します。
3. **Customer list** を選択します。
4. **Value** 列を含まないCSVまたはリストをアップロードします。**No, continue with a customer list that doesn't include customer value** を選択します。
5. カスタムオーディエンスの作成を完了します。
6. Brazeで、作成したカスタムオーディエンスを使用してFacebookオーディエンス同期ステップを更新します。

### Facebookカスタムオーディエンスの利用規約に関するメールを受け取りました。この問題を解決するにはどうすればよいですか？ {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Facebookへのオーディエンス同期を使用するには、この利用規約に同意する必要があります。

- 広告アカウントが個人のFacebookアカウントに直接関連付けられている場合は、個人アカウントから利用規約に同意できます：`https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`
- 広告アカウントが会社のBusiness Managerアカウントに紐づいている場合は、Facebook Business Managerアカウントから利用規約に同意する必要があります：`https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`

Facebookカスタムオーディエンスの利用規約に同意した後、以下を行ってください。

1. Facebookアカウントを切断してから再接続し、BrazeでFacebookアクセストークンを更新します。
2. キャンバスを編集・更新して、Facebookオーディエンス同期ステップを再度有効にします。

これにより、ユーザーがFacebookオーディエンス同期ステップに到達するとすぐに、Brazeがユーザーを同期できるようになります。

### **Connected Facebook** フィルターと **Number of Facebook Friends Using App** フィルターはどうなりましたか？ {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

**Number of Facebook Friends Using App** および **Connected Facebook** のBrazeセグメンテーションフィルターは非推奨になりました。FacebookおよびBraze SDKは、これらのフィルターが依存していた基礎データを収集しなくなりました。

非推奨のフィルターは、カスタム属性、カスタムイベント、またはエンゲージメントベースのセグメントに置き換えてください。たとえば、**Connected Facebook** の代わりにFacebookログインやソーシャルリンキングを、**Number of Facebook Friends Using App** の代わりに紹介、招待、共有を使用できます。

キャンバスのリターゲティングでは、[ステップ4：同期の設定](#step-4-sync-setup)で示されているように、メール、電話番号、名、姓でユーザーをマッチングします。リーチを拡大するには、高価値セグメントをFacebookに同期し、Meta Ads Managerで類似オーディエンスを作成してください。

## トラブルシューティング {#troubleshooting}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table aria-label="トラブルシューティング">
  <thead>
    <tr>
      <th>エラー</th>
      <th>説明</th>
      <th>解決手順</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Invalid Token</b></td>
      <td>連携を接続したユーザーがパスワードを変更した場合や、認証情報の有効期限が切れた場合などに発生します。</td>
      <td><b>パートナー連携</b> > <b>Facebook</b> に移動し、アカウントを切断してから再接続してください。Facebookアカウントを監査するための追加手順については、<a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングセクション</a> を参照してください。</td>
    </tr>
    <tr>
      <td><b>Audience Size Too Low</b></td>
      <td>このエラーは、オーディエンスからユーザーを削除するオーディエンス同期ステップを作成した場合に発生することがあります。オーディエンスサイズがゼロに近づくと、ネットワークがオーディエンスサイズが小さすぎると判断する場合があります。</td>
      <td>オーディエンスサイズを完全に枯渇させないよう、定期的にユーザーを追加および削除するオーディエンス同期戦略を使用してください。</td>
    </tr>
    <tr>
      <td><b>Audience Does Not Exist</b></td>
      <td>オーディエンス同期ステップが、存在しないか削除されたオーディエンスを使用しています。オーディエンスへのアクセスに必要な権限がなくなった場合にもトリガーされることがあります。</td>
      <td>管理者にパートナープラットフォームでオーディエンスがまだ存在するかどうかを確認してもらってください。<br><br>存在する場合は、連携を接続したユーザーがそのオーディエンスへの権限を持っているかどうかを確認してください。権限がない場合は、そのオーディエンスへのアクセスを付与する必要があります。<br><br>オーディエンスが意図的に削除された場合は、アクティブなオーディエンスを追加し、ステップで新しいオーディエンスを作成してください。</td>
    </tr>
    <tr>
      <td><b>Ad Account Access Attempt</b></td>
      <td>選択した広告アカウントまたはオーディエンスに対する権限がありません。</td>
      <td>広告アカウントの管理者と連携して、適切なアクセスと権限を取得してください。</td>
    </tr>
    <tr>
      <td><b>Terms of Service Not Accepted</b></td>
      <td>Facebookなどの一部のオーディエンス同期送信先では、オーディエンス同期機能を使用するために広告ネットワークの特定の利用規約に同意する必要があります。このエラーは、適切な利用規約に同意していない場合にトリガーされます。その結果、Brazeから「Your authorization credentials for Facebook are invalid.」という件名のメールを受信している場合もあります。</td>
      <td>Facebookの必要な利用規約に同意しているか確認してください。</td>
    </tr>
    <tr>
      <td><b>All Users Are Erroring Out</b></td>
      <td>ステップで選択したフィールドに値があることを確認したにもかかわらず、すべてのユーザーがステップでエラーになっている場合、Facebookアカウントに問題がある可能性があります。</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングセクション</a> の手順に従って、アカウントに問題がないか確認してください。
      </td>
    </tr>
    <tr>
      <td><b>Failed to create audience</b></td>
      <td>Facebookテクノロジーパートナーページでは「Connected」と表示されていますが、Facebookオーディエンス同期ステップでオーディエンスを同期する際に「Failed to create audience 'audience name'」というエラーが発生します。Facebookアカウントの認証に失敗しました。テクノロジーパートナーページにアクセスしてアカウントを再接続してください。</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングセクション</a> の手順に従って、アカウントに問題がないか確認してください。
      </td>
    </tr>
    <tr>
      <td><b>Ad account missing from dropdown</b></td>
      <td>Facebookオーディエンスステップを設定する際に、期待する広告アカウントが広告アカウントピッカーに表示されません。</td>
      <td>Facebookアプリが、Marketing APIの使用にFacebookが要求するアクセスレベルで<code>ads_management</code>の<a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">アプリレビュー</a> を完了していることを確認してください。<a href="https://business.facebook.com/">Facebook Business Manager</a> で、システムユーザートークンが適切な権限を持ち、Brazeで使用する広告アカウントに関連付けられていること、および広告アカウントの利用規約に同意していることを確認してください。<br><br>新しいキャンバスではドロップダウンが機能するが、既に編集したキャンバスでは機能しない場合は、ブラウザのハードリフレッシュ（またはキャッシュのクリア）を試し、それらの広告アカウントへのアクセス権を持つユーザーとしてサインインしていることを確認してください。</td>
    </tr>
    <tr>
      <td><b>Error validating access token</b></td>
      <td>BrazeをFacebookに接続する際、またはオーディエンスを同期する際に、Facebookアクセストークンの検証に関するエラーが表示されます。</td>
      <td>ブラウザでFacebookからサインアウトしてください。Brazeで<b>パートナー連携</b> &gt; <b>Facebook</b>に移動し、保存されたFacebook認証情報を削除してから、Facebookを再接続してください。FacebookのBraze用テクノロジーパートナーページで、オプションが利用可能な場合は連携を切断して再接続してください。<br><br>問題が続く場合は、<a href="#audit-your-facebook-account">Facebookアカウントの監査</a> に従ってください。</td>
    </tr>
    <tr>
      <td><b>Audience export or sync permission errors</b></td>
      <td>Facebookオーディエンスのエクスポートまたは同期が、認証、管理者、または広告アカウントのエラーで失敗します。</td>
      <td><a href="https://developers.facebook.com/">Meta for Developers</a> でアプリを開き、<b>App roles</b>でユーザーに<b>Admin</b>ロールがあることを確認してください。<b>App settings</b> &gt; <b>Advanced</b>で、<b>Advertising accounts</b>にBrazeで使用するアカウントが含まれていることを確認してください。<a href="https://business.facebook.com/latest/settings">Business settings</a> で、接続ユーザーまたはシステムユーザーが正しい広告アカウントへのアクセス権を持っていることを確認してください。</td>
    </tr>
  </tbody>
</table>

### Facebookアカウントの監査 {#audit-your-facebook-account}

連携に関する追加の問題が発生した場合は、以下のセクションと手順を参照してFacebookアカウントを監査してください。

#### アカウント権限の確認 {#review-account-permissions}

1. プラットフォームでこれらの権限を管理する方法については、[Facebookのドキュメント](https://www.facebook.com/business/help/186007118118684?id=829106167281625)を確認してください。Facebook Business Managerでは、必要な広告アカウントへのアクセス権を持つ**Admin**または**Employee**のBusiness Managerロールが少なくとも必要です。
2. **Employee**の場合は、オーディエンスの作成やオーディエンスへのユーザー同期を行うために、管理者が各広告アカウントに対する完全な**Manage Ad Account**権限を付与していることを確認してください。
3. 権限が付与された後、アカウントを切断して再接続する必要があります。

#### 利用規約への同意 {#terms}

Facebookからの保留中の利用規約（TOS）に同意してください。Facebookは定期的にユーザーとビジネスマネージャーに利用規約の再承認を求めます。

1. 接続ユーザーは、各広告アカウントのすべての利用規約に同意する必要があります:
- 個人のFacebookアカウントのカスタムオーディエンスTOS:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![広告アカウントを管理するための完全なコントロール権限を持つアカウント。]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

アカウントIDとビジネスIDを確認するには、以下の手順に従ってください:

1. [Facebook Ads Managerアカウント](https://adsmanager.facebook.com/)にアクセスします。
2. ドロップダウンメニューで正しい広告アカウントを使用していることを確認します。
3. URLで、`act=`の後にアカウントID、`business_id=`の後にビジネスIDを確認します。

![アカウントIDとビジネスIDがハイライトされたURL。]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. カスタムオーディエンスの利用規約を読み、**Accept**を選択してください。利用規約の上部にあるドロップダウンを使用して、どのアカウントの利用規約に署名しているかを確認することをお勧めします。

![利用規約に署名するアカウントを表示するドロップダウン。]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. 利用規約に対して**Accept**を選択する必要があります。その後、「You have accepted these terms of service on behalf of Braze」というメッセージが表示されます。
6. Facebookアカウントを切断して再接続することで、BrazeのFacebookアクセストークンを更新してください。
7. キャンバスを編集して更新することで、Facebookオーディエンス同期ステップを再有効化してください。これにより、Brazeはユーザーがキャンバスのオーディエンスステップに到達するとすぐに同期できるようになります。
8. 問題が解決しない場合は、管理者権限を持つ別のユーザーを使用して、Ads Managerから手動で利用規約に同意してみてください。

#### 保留中のタスクの完了 {#complete-any-pending-tasks}

Facebook広告サービスの使用をブロックしている可能性のある保留中のタスクがないか確認してください:

1. [Facebook Ads Managerにログイン](https://adsmanager.facebook.com/)します。
2. 問題が発生している広告アカウントを選択します。
3. ナビゲーションで**Account Overview**を選択します。<br> ![Account Overviewが選択されたナビゲーション。]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. 対処が必要なアラートがないか確認します。<br> ![クレジットカードの有効期限が切れたアカウント。]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. 完了する必要のあるセットアップタスクがないか確認します。<br> ![アカウント設定が部分的に完了したアカウント。]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### 別のユーザーで接続する {#connect-with-a-different-user}

別のトラブルシューティング手順として、別の管理者ユーザーが以下の手順でアカウントを接続することをお勧めします:

1. 現在の連携を切断します。
2. 管理者権限を持つ別のユーザーがFacebookユーザーアカウントを接続します。