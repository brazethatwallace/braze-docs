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

## ユーザーの同期とレート制限の考慮事項 {#user-syncing-and-rate-limit-considerations}

ユーザーがAudience Syncステップに達すると、BrazeはFacebookのMarketing APIレート制限を尊重しながら、ほぼリアルタイムで同期します。Brazeは、Facebookに送信する前に、5秒ごとに可能な限り多くのユーザーをバッチ処理します。

FacebookのMarketing APIレート制限では、広告アカウント1つにつき、1時間以内に&#126;190,000 APIリクエストまでしか許可されません。顧客がこの制限に達した場合、Brazeは最大&#126;13時間まで同期を再試行します。それでも同期できない場合、BrazeはこれらのユーザーをUsers Errored指標の下にリストアップします。

## 前提条件 {#prerequisites}

キャンバスでFacebookオーディエンスのステップを設定するには、以下の項目の作成および完了を確認する必要があります。

| 必要条件 | 提供元 | 説明 |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | ブランドのFacebookアセット（広告アカウント、ページ、アプリなど）を管理するための集中型ツールです。 |
| Facebook広告アカウント | [Facebook](https://www.facebook.com/business/help/910137316041095) | ブランドのビジネスマネージャーと結びついたアクティブなFacebook広告アカウント。<br><br>Facebook Business Managerの管理者が、Brazeで使用する予定のFacebook広告アカウントに対して「Manage キャンペーン」または「Manage ad accounts」のいずれかの権限を付与していることを確認してください。また、広告アカウントの利用規約に同意していることも確認してください。 |
| Facebookカスタムオーディエンス利用規約 | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Brazeで使用する予定のFacebook広告アカウントについて、Facebookのカスタムオーディエンス規約に同意します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1: Facebookに接続する {#step-1-connect-to-facebook}

{% alert important %}
FacebookをBrazeアカウントに接続するには[「管理者」権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin)が必要です。
{% endalert %}

Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、**Facebook**を選択します。Facebook Audience Exportで、**Connect Facebook**を選択します。

![概要セクションと、Connect Facebookボタンのある Facebook Audience Exportセクションを含むBrazeのFacebookテクノロジーページ。]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Facebook oAuthダイアログウィンドウが表示され、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを承認します。

![最初のFacebookダイアログボックス。「Connect as X」（XはFacebookユーザー名）で接続するように促されます。]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![広告アカウントの広告を管理する許可を求める2番目のFacebookダイアログボックス。]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

BrazeをFacebookアカウントにリンクしてから、Brazeワークスペース内で同期する広告アカウントを選択します。接続されると、パートナーページに戻ります。このページで接続されているアカウントを表示したり、既存のアカウントの接続を解除したりできます。

![広告アカウントが接続されたことを示す更新後のFacebookテクノロジーパートナーページ。]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Facebookとの接続は、Brazeのワークスペースレベルで適用されます。Facebookの管理者がFacebook Business Managerからあなたを削除したり、接続されているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出します。そのため、Facebook Audienceコンポーネントを使用しているアクティブなキャンバスにはエラーが表示され、Brazeはユーザーを同期できません。

{% alert important %}
これまでに[Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management)および[Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard)のFacebookアプリレビュープロセスを受けたことがある顧客のシステムユーザートークンは、Facebook Audienceコンポーネントに対して引き続き有効です。FacebookパートナーページからFacebookシステムユーザートークンを編集したり、取り消したりすることはできません。その代わりに、Facebookアカウントに接続して、Brazeワークスペース内でFacebookシステムユーザートークンを置き換えることができます。

<br><br>Facebook oAuthの設定は、[セグメントを使用したFacebookのエクスポート]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites)にも適用されます。
{% endalert %}

### ステップ2: カスタムオーディエンスの利用規約に同意する {#step-2-accept-custom-audiences-terms-of-service}

キャンバスを構築する前に、以下のリンクからFacebookの下記の利用規約に同意する必要があります。

- **利用する個人アカウントのCustomer List Custom Audiences規約：** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`
- **ビジネスアカウントのFacebook Business Tools規約：** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`

![顧客リストカスタムオーディエンスに関して同意が必要になる規約の例。]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Facebookビジネスツールに関して同意が必要になる規約の例。]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

統合時のFacebookアカウントの監査に関する詳細は、[FAQセクション](#terms)を参照してください。

### ステップ3: キャンバスにFacebook Audienceコンポーネントを追加する {#step-3-add-a-facebook-audience-component-in-canvas}

キャンバスにコンポーネントを追加し、**Facebook Audience**を選択します。

![キャンバスに追加するコンポーネントのリスト。]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Audience Syncコンポーネント。]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### ステップ4: 同期設定 {#step-4-sync-setup}

**Custom Audience**ボタンを選択してコンポーネントエディターを開きます。次に、Audience Syncパートナーとして**Facebook**を選択します。

![パートナー選択のオプションを含む「Audience Syncを設定」画面。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

任意のFacebook広告アカウントを選択します。**Choose a New or Existing Audience**ドロップダウンで、新規または既存のオーディエンスの名前を入力します。

{% tabs %}
{% tab 新しいオーディエンスを作成する %}

1. 新しいカスタムオーディエンスの名前を入力します。
2. **Add Users to Audience**を選択し、Facebookと同期するフィールドを選択します。
3. 次に、**Create Audience**を選択してオーディエンスを保存します。

![メール、電話、名、姓の情報が一致するオーディエンスの同期設定。]({% image_buster /assets/img/audience_sync/fb_sync.png %})

オーディエンスが正常に作成された場合、またはこのプロセス中にエラーが発生した場合は、ステップエディターの上部に通知が表示されます。また、オーディエンスは下書きモードで作成されているため、キャンバスジャーニーの後半でユーザーを削除する際にこのオーディエンスを参照することもできます。

新しいオーディエンスでキャンバスを起動すると、Brazeはキャンバスの起動と同時に新しいカスタムオーディエンスを作成し、その後Audience Syncステップに入るとほぼリアルタイムでユーザーを同期します。

{% endtab %}
{% tab 既存のオーディエンスと同期する %}

Brazeは、既存のFacebookカスタムオーディエンスからユーザーの追加または削除を行い、これらのオーディエンスを最新の状態に保持する機能も提供しています。既存のオーディエンスと同期するには、以下の手順に従います。

1. ドロップダウンに既存のオーディエンス名を入力します。
2. **Add to the Audience**するか、**Remove from the Audience**するかを選択します。
3. Brazeは、ユーザーがFacebook Audienceステップに入ると、ほぼリアルタイムでユーザーを追加または削除します。

![オーディエンス同期の設定で、メール、電話、名、姓の情報を削除する。]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebookでは、オーディエンスのサイズが小さすぎる場合（通常は1,000ユーザー未満）、カスタムオーディエンスからのユーザーの削除を禁止しています。その結果、オーディエンスが適切なサイズに達するまで、BrazeはAudience Syncステップからの削除対象ユーザーを同期できません。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ5: キャンバスを起動する {#step-5-launch-canvas}

Facebook Audienceコンポーネントを設定したら、キャンバスを起動できます。新しいカスタムオーディエンスが作成され、Facebook Audienceステップを通過したユーザーはFacebook上のこのカスタムオーディエンスに渡されます。キャンバスに後続のステップが含まれている場合、ユーザーはユーザージャーニーの次のステップに進みます。

Facebook Audience Managerのカスタムオーディエンスの**History**タブには、Brazeからオーディエンスに送られたユーザー数が反映されます。ユーザーが再びステップに入ると、再びFacebookに送られます。

![オーディエンスの詳細と、特定のFacebookオーディエンスのHistoryタブ。このタブには、アクティビティ、アクティビティの詳細、変更されたアイテム、および日時の列を含むAudience Historyテーブルが表示されています。]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## 分析の理解 {#understanding-analytics}

次の表に、Audience Syncコンポーネントからの分析をよりよく理解するのに役立つ指標と説明を示します。

| 指標 | 説明 |
| --- | --- |
| 入力 | Facebookと同期するためにこのコンポーネントに入ったユーザーの数。 |
| 次のステップに進む | 次のコンポーネントがある場合、次のコンポーネントに進んだユーザーの数。これがキャンバスブランチの最後のステップである場合、すべてのユーザーは自動的に進みます。 |
| 同期されたユーザー | Facebookとの同期に成功したユーザー数。 |
| 同期されていないユーザー | 一致するフィールドが不足しているため、同期されていないユーザーの数。フィールドは「OR」演算子を使用して照合されます。このため、ユーザーにFacebookのフィールドのいずれか1つがあれば、他のすべてのフィールドで一致するものがなくても、Facebookはそのユーザーを一致と判断します。 |
| 保留中のユーザー | 現在、BrazeがFacebookへの同期処理を行っているユーザー数。 |
| エラーが発生したユーザー数 | 約13時間の再試行後、APIエラーのためにFacebookに同期されなかったユーザーの数。エラーの原因としては、無効なFacebookトークンや、Facebook上でカスタムオーディエンスが削除された場合などが考えられます。 |
| キャンバスを退出 | キャンバスを退出したユーザーの数。これは、キャンバスの最後のステップがFacebookステップである場合に発生します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="分析の理解" }

{% alert important %}
内部処理のため、同期したユーザーとエラーが発生したユーザーの指標のレポートに遅延が生じます。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### Audience Syncパートナーのダッシュボードに、オーディエンスが取り込まれるまでどのくらいの時間がかかりますか？ {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

オーディエンスの取り込みにかかる時間は、パートナーに応じて異なります。すべてのネットワークがBrazeからのリクエストを処理し、ユーザーとのマッチングを試みます。カスタムオーディエンスの更新には最大24時間かかることがあります。

### 無効なトークンエラーが表示された場合、次に何をすればよいですか？ {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

FacebookパートナーページでFacebookアカウントの接続を解除してから再接続できます。Facebook Business Managerの管理者に、同期先の広告アカウントに対する適切な権限があることを確認してください。

### キャンバスを起動できないのはなぜですか？ {#why-is-my-canvas-not-allowed-to-launch}

- システムユーザートークンが認証され、Facebook Business Managerで目的の広告アカウントにアクセスできることを確認してください。
- 広告アカウントを選択し、新しいカスタムオーディエンスの名前を入力し、一致するフィールドを選択していることを確認してください。
- Facebookのカスタムオーディエンス数の上限である500に達した可能性があります。キャンバスを使って新しいカスタムオーディエンスを作成する前に、Facebook Audience Managerに移動して不要なオーディエンスを削除してください。

### Facebookにユーザーを渡した後、ユーザーが一致していることを確認するにはどうすればよいですか？ {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

Facebookはプライバシー上の理由からこの情報を提供していません。

### Brazeはバリューベースのカスタムオーディエンスに対応していますか？ {#does-braze-support-value-based-custom-audiences}

現時点では、バリューベースのカスタムオーディエンスはBrazeでサポートされていません。{% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### BrazeはAudience Syncパートナーにデータを送信する前にハッシュ化しますか？ {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

メールデータが正規化されると、BrazeはそれをSHA256でハッシュ化します。

**IDFA/AAID/電話：** BrazeはSHA256でハッシュ化します。同期するオーディエンスのタイプは常に以下のいずれかになります。

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256

頻度に関して、Brazeは、ユーザーが同期の準備段階としてユーザージャーニーのAudience Syncステップに入ったときにのみ、個人識別情報（PII）をハッシュ化します。

### バリューベースの類似カスタムオーディエンスの同期に関する問題を解決するにはどうすればよいですか？ {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

現時点では、バリューベースの類似カスタムオーディエンスはBrazeでサポートされていません。このオーディエンスに同期しようとすると、Audience Syncステップでエラーが発生する可能性があります。これを解決するには、次の手順に従います。

1. Facebook Ad Managerダッシュボードを開き、**Audiences**を選択します。
2. **Create audience** > **Custom audience**を選択します。
3. **Customer list**を選択します。
4. **Value**列を除いたCSVまたはリストをアップロードします。**No, continue with a customer list that doesn't include customer value**を選択します。
5. カスタムオーディエンスの作成を完了します。
6. Brazeで、作成したカスタムオーディエンスを使用してFacebook Audience Syncステップを更新します。

### Facebookのカスタムオーディエンス利用規約に関連するメールが届きました。これを解決するにはどうすればよいですか？ {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

FacebookへのAudience Syncを利用するには、これらの利用規約に同意する必要があります。

- 広告アカウントがFacebookの個人アカウントに直接関連付けられている場合は、こちらから個人アカウントの利用規約に同意できます：`https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`
- 広告アカウントが会社のBusiness Managerアカウントと関連付けられている場合は、こちらからFacebook Business Managerアカウントの利用規約に同意する必要があります：`https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`

Facebookカスタムオーディエンスの利用規約に同意したら、以下を行います。

1. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュします。
2. キャンバスを編集して更新することにより、Facebook Audience Syncステップを再度有効にします。

これにより、ユーザーがFacebook Audience Syncステップに到達するとすぐに、Brazeでユーザーを同期できます。

### **Connected Facebook**フィルターと**Number of Facebook Friends Using App**フィルターはどうなりましたか？ {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

**Number of Facebook Friends Using App**および**Connected Facebook**のBrazeセグメンテーションフィルターは非推奨になりました。FacebookおよびBraze SDKは、これらのフィルターが依存していた基盤データを収集しなくなりました。

非推奨のフィルターは、カスタム属性、カスタムイベント、またはエンゲージメントベースのセグメントに置き換えてください。例えば、**Connected Facebook**の代わりにFacebookログインやソーシャルリンキングを、**Number of Facebook Friends Using App**の代わりに紹介、招待、共有を使用できます。

キャンバスのリターゲティングについては、[ステップ4: 同期設定](#step-4-sync-setup)で示されているように、メール、電話、名、姓を使用してユーザーをマッチングします。リーチを拡大するには、高価値のセグメントをFacebookに同期し、Meta Ads Managerで類似オーディエンスを作成します。

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
      <td><b>無効なトークン</b></td>
      <td>一般的には、統合に接続したユーザーのパスワードの変更や、認証情報の有効期限切れなどが原因となります。</td>
      <td><b>パートナー連携</b> > <b>Facebook</b>に移動し、アカウントの接続を解除してから再接続します。Facebookアカウントを監査する追加手順については、<a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングセクション</a> を参照してください。</td>
    </tr>
    <tr>
      <td><b>オーディエンスのサイズが小さすぎる</b></td>
      <td>このエラーは、オーディエンスからユーザーを削除するAudience Syncステップを作成した場合に発生することがあります。オーディエンスのサイズがゼロに近づくと、ネットワークはオーディエンスのサイズが小さすぎて配信できないというフラグを立てることがあります。</td>
      <td>オーディエンスサイズを使い尽くさない範囲で、定期的にユーザーの追加と削除を行うAudience Sync戦略を使用してください。</td>
    </tr>
    <tr>
      <td><b>オーディエンスが存在しない</b></td>
      <td>Audience Syncステップで、存在しないオーディエンスまたは削除されたオーディエンスが使用されています。これは、オーディエンスへのアクセスに必要な権限がなくなった場合にもトリガーされます。</td>
      <td>パートナープラットフォームで管理者にオーディエンスがまだ存在するかどうかを確認してもらってください。<br><br>存在する場合は、統合を接続したユーザーがオーディエンスに対する権限を持っているかどうかを確認します。権限がない場合は、そのオーディエンスへのアクセス権をユーザーに付与する必要があります。<br><br>オーディエンスが意図的に削除された場合は、アクティブなオーディエンスを追加し、そのステップで新しいオーディエンスを作成します。</td>
    </tr>
    <tr>
      <td><b>広告アカウントへのアクセス試行</b></td>
      <td>選択した広告アカウントまたはオーディエンスに対する権限がありません。</td>
      <td>広告アカウントの管理者と協力して、適切なアクセス権と権限を取得してください。</td>
    </tr>
    <tr>
      <td><b>利用規約への同意がない</b></td>
      <td>Facebookなど、Audience Syncの送信先によっては、Audience Sync機能を使用するために特定の利用規約に同意することが広告ネットワークによって義務付けられています。このエラーは、該当する規約に同意していない場合に発生します。この場合、Brazeから「Your authorization credentials for Facebook are invalid.」という件名のメールが届くこともあります。</td>
      <td>Facebookの必要な規約に同意したことを確認してください。</td>
    </tr>
    <tr>
      <td><b>すべてのユーザーでエラーが発生している</b></td>
      <td>ユーザーにステップで選択したフィールドの値があることを確認しているにもかかわらず、すべてのユーザーでエラーが発生している場合、Facebookアカウントに問題がある可能性があります。</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングセクション</a> の手順に従って、アカウントに問題がないかを確認してください。
      </td>
    </tr>
    <tr>
      <td><b>オーディエンスを作成できない</b></td>
      <td>Facebookテクノロジーパートナーのページでは「Connected」と表示されているにもかかわらず、Facebook Audience Syncステップでオーディエンスの同期時に「Failed to create audience 'audience name'」というエラーが表示されます。Facebookアカウントの認証に失敗しています。テクノロジーパートナーのページにアクセスして、アカウントを再接続してください。</td>
      <td><a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>このトラブルシューティングセクション</a> の手順に従って、アカウントに問題がないかを確認してください。
      </td>
    </tr>
    <tr>
      <td><b>広告アカウントがドロップダウンに表示されない</b></td>
      <td>Facebook Audienceステップを設定する際に、期待する広告アカウントが広告アカウントピッカーに表示されません。</td>
      <td>Facebookアプリが、Marketing APIの使用にFacebookが要求するアクセスレベルで<code>ads_management</code>の<a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">アプリレビュー</a> を完了していることを確認してください。<a href="https://business.facebook.com/">Facebook Business Manager</a> で、システムユーザートークンが適切な権限を持ち、Brazeで使用する広告アカウントに関連付けられていること、および広告アカウントの利用規約に同意していることを確認してください。<br><br>新しいキャンバスではドロップダウンが機能するが、既に編集したキャンバスでは機能しない場合は、ブラウザのハードリフレッシュ（またはキャッシュのクリア）を試し、それらの広告アカウントにアクセスできるユーザーとしてサインインしていることを確認してください。</td>
    </tr>
    <tr>
      <td><b>アクセストークンの検証エラー</b></td>
      <td>BrazeをFacebookに接続する際、またはオーディエンスを同期する際に、Facebookアクセストークンの検証に関するエラーが表示されます。</td>
      <td>ブラウザでFacebookからサインアウトします。Brazeで<b>パートナー連携</b> &gt; <b>Facebook</b>に移動し、保存されたFacebook認証情報を削除してから、再度Facebookに接続します。FacebookのBraze向けテクノロジーパートナーページで、オプションが利用可能な場合は統合を切断してから再接続します。<br><br>問題が続く場合は、<a href="#audit-your-facebook-account">Facebookアカウントの監査</a> に従ってください。</td>
    </tr>
    <tr>
      <td><b>オーディエンスのエクスポートまたは同期の権限エラー</b></td>
      <td>Facebookオーディエンスのエクスポートまたは同期が、認証、管理者、または広告アカウントのエラーで失敗します。</td>
      <td><a href="https://developers.facebook.com/">Meta for Developers</a> でアプリを開き、<b>App roles</b>でユーザーに<b>Admin</b>ロールがあることを確認します。<b>App settings</b> &gt; <b>Advanced</b>で、<b>Advertising accounts</b>にBrazeで使用するアカウントが含まれていることを確認します。<a href="https://business.facebook.com/latest/settings">ビジネス設定</a> で、接続ユーザーまたはシステムユーザーが正しい広告アカウントにアクセスできることを確認します。</td>
    </tr>
  </tbody>
</table>

### Facebookアカウントを監査する {#audit-your-facebook-account}

統合でさらに問題が発生した場合は、以下のセクションと手順を参照して、Facebookアカウントを監査してください。

#### アカウント権限の確認 {#review-account-permissions}

1. [Facebookのドキュメント](https://www.facebook.com/business/help/186007118118684?id=829106167281625)で、プラットフォームにおける権限の管理方法を確認してください。Facebook Business Managerの場合、少なくとも必要な広告アカウントにアクセスできる**Admin**または**Employee**のBusiness Managerロールが必要です。
2. **Employee**として、管理者が、オーディエンスの作成やオーディエンスへのユーザーの同期に使用する各広告アカウントのすべての**Manage Ad Account**権限を付与していることを確認します。
3. 権限が付与された後、アカウントを切断してから再接続する必要があります。

#### 利用規約に同意する {#terms}

Facebookから保留中の利用規約（TOS）に同意します。Facebookは定期的に、あなた（ユーザー）とビジネスマネージャーに、利用規約への再同意を求めます。

1. 接続ユーザーは、各広告アカウントのすべての利用規約に同意する必要があります。
- Facebook個人アカウントのカスタムオーディエンス利用規約：
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![広告アカウントを管理するためのフルコントロール権限を持つアカウント。]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

アカウントIDとビジネスIDを見つけるには、次の手順に従います。

1. [Facebook広告マネージャーのアカウント](https://adsmanager.facebook.com/)にアクセスします。
2. 適正な広告アカウントを使用しているかを、ドロップダウンメニューから確認します。
3. URLで、`act=`の後にアカウントIDが、`business_id=`の後にビジネスIDがあることを確認します。

![アカウントIDとビジネスIDがハイライトされたURL。]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. カスタムオーディエンス規約を読み、**Accept**を選択します。利用規約の上部にあるドロップダウンを使用して、利用規約への署名がどのアカウントに対するものであるかを確認することをおすすめします。

![利用規約に署名しているアカウントを示すドロップダウン。]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. 利用規約に対して**Accept**を選択する必要があります。その後、次のメッセージが表示されます：「You have accepted these terms of service on behalf of Braze」。
6. Facebookアカウントを一旦切断し、再接続することで、BrazeでFacebookアクセストークンをリフレッシュします。
7. キャンバスを編集して更新することにより、Facebook Audience Syncステップを再度有効にします。これにより、ユーザーがFacebook Audienceステップに到達するとすぐに、Brazeで同期できるようになります。
8. 問題が解決しない場合は、管理者権限を持つ別のユーザーを使用して、Ads Managerから手動で規約に同意してみてください。

#### 保留中のタスクを完了させる {#complete-any-pending-tasks}

Facebook Adsサービスの使用をブロックしている可能性がある保留中のタスクがFacebookにないかを確認します。

1. [Facebook Ads Managerにログインします](https://adsmanager.facebook.com/)。
2. 問題のある広告アカウントを選択します。
3. ナビゲーションで、**Account Overview**を選択します。<br> ![Account Overviewを選択したナビゲーション。]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. 対処が必要なアラートがあるかどうかを確認します。<br> ![有効期限が切れたクレジットカードのアカウント。]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. 未完了のセットアップタスクがあるかどうかを確認します。<br> ![アカウントのセットアップが一部完了しているアカウント。]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### 別のユーザーで接続する {#connect-with-a-different-user}

その他のトラブルシューティング手順として、別の管理者ユーザーが次の手順でアカウントに接続してみることをおすすめします。

1. 現在の統合を切断します。
2. 管理者権限を持つ別のユーザーがFacebookユーザーアカウントを接続します。