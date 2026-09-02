---
nav_title: Facebook
article_title: Facebookオーディエンスエクスポート
alias: /partners/facebook/
description: "このリファレンス記事では、ブランドが顧客にリーチしエンゲージするための主要なソーシャルプラットフォームであるFacebookとBrazeのパートナーシップについて説明します。"
page_type: partner
search_tag: Partner
---

# Facebookオーディエンスエクスポート {#facebook-audience-export}

> BrazeとFacebookの統合により、Brazeのセグメントを手動でFacebookにエクスポートし、Facebookカスタムオーディエンスを作成できます。これは1回限りの静的オーディエンスエクスポートであり、新しいFacebookカスタムオーディエンスのみが作成されます。

Facebookカスタムオーディエンスをエクスポートする一般的なユースケースには、以下のようなものがあります。
- ライフサイクル内の特定のポイントでユーザーをリターゲティングする
- 除外ターゲットリストの作成
- 新規ユーザーをより効率的に獲得するための[類似オーディエンス](https://www.facebook.com/business/help/164749007013531?id=401668390442328)を作成する
<br><br>

{% alert note %}
Facebookオーディエンスエクスポートは、**ユーザーアクセストークン**を使用してリクエストを承認します。<br><br>
この機能を[Facebookへのオーディエンス同期]({{site.baseurl}}/audience_sync_facebook)機能と一緒に使用している場合、Brazeはリクエストを承認するために、すでに生成した、より信頼性の高い**システムユーザートークン**をデフォルトで使用します。
{% endalert %}

{% alert note %}
ベータ版のMeta ワークアカウントのテストに参加している場合は、アカウントを接続解除してから[Facebookパートナーページ]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync#step-1-connect-to-facebook)に再接続してください。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| [Facebook Business Manager](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | ブランドのFacebookアセット（広告アカウント、ページ、アプリなど）を管理するための一元的なツールです。 |
| [Facebook広告アカウント](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | ブランドのBusiness Managerに紐づいたアクティブなFacebook広告アカウントで、Brazeカスタムオーディエンスで使用するものです。<br><br>Facebook Business Managerの管理者が、Brazeで使用する予定のFacebook広告アカウントに対する管理者権限を付与していること、また広告アカウントの利用規約に同意していることを確認してください。これらが完了していない場合、Braze内でFacebook広告アカウントにアクセスできません。 |
| [Facebookカスタムオーディエンス利用規約](https://www.facebook.com/ads/manage/customaudiences/tos.php)| Brazeで使用する予定のFacebook広告アカウントについて、Facebookのカスタムオーディエンス利用規約に同意する必要があります。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1：Facebookに接続する {#step-1-connect-to-facebook}

1. Brazeダッシュボードで、**パートナー連携** > **テクノロジーパートナー**に移動し、**Facebook**を選択します。

{: start="2"}
2. Facebook オーディエンスエクスポートモジュールで、**Connect Facebook**を選択します。<br><br>![BrazeプラットフォームのFacebookテクノロジーパートナーページ。]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. FacebookのoAuthダイアログウィンドウで、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを承認します。<br><br>![Facebookユーザー名として接続するよう求める最初のFacebookダイアログボックス。]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![広告アカウントの広告管理の権限を求める2番目のFacebookダイアログボックス。]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. BrazeがFacebookアカウントにリンクされたら、Brazeワークスペース内で同期する広告アカウントを選択します。<br><br>![Facebookに接続可能な広告アカウントの一覧。]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> 接続後、パートナーページに戻り、接続されているアカウントの確認や既存アカウントの切断が可能です。<br><br> ![広告アカウントが正常に接続されたことを示すFacebookテクノロジーパートナーページの更新版。]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Facebookの接続はBrazeワークスペースレベルで適用されます。Facebook管理者がFacebook Business Managerからあなたを削除したり、接続されたFacebookアカウントへのアクセスを取り消したりした場合、Brazeは無効なトークンを検出します。その結果、Facebook オーディエンスステップを使用しているアクティブなキャンバスにエラーが表示され、Brazeはユーザーを同期できなくなります。

{% alert important %}
[Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management)および[Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard)のFacebookアプリレビュープロセスを以前に受けた顧客の場合、システムユーザートークンは引き続きFacebook オーディエンスステップで有効です。Facebookパートナーページからシステムユーザートークンを編集または取り消すことはできません。代わりに、Facebookアカウントを接続して、Brazeワークスペース内のFacebookシステムユーザートークンを置き換えることができます。

<br><br>新しいFacebook oAuth設定は、[セグメント経由のFacebookエクスポート]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites)にも適用されます。
{% endalert %}

### ステップ2：ユーザーをFacebookにエクスポートする {#step-2-export-your-users-into-facebook}

Brazeでは、Facebook オーディエンスエクスポートは**セグメント**ページからアクセスできます。

1. **セグメント**ページで、エクスポートしたいセグメントを選択します。
2. **ユーザーデータ**を選択し、次に**Export as Facebook Audience**を選択します。<br><br>![セグメントの「セグメント詳細」セクションで「ユーザーデータ」が選択され、「Export as Facebook Audience」を含むオプションのドロップダウンが表示されている画面。]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Braze内でFacebookをまだ有効にしていない場合、ダッシュボードのFacebookテクノロジーパートナーページに移動するよう求められます。**テクノロジーパートナー** > **Facebook**からすでにFacebookを有効にしている場合は、Facebook広告アカウントとエクスポートするユーザーフィールドを選択できます。<br><br> 以下のフィールドをエクスポートできます：
- デバイスIDFA
- 電話番号
- メール

{% alert note %}
1回のエクスポートで選択できるユーザーフィールドは1つのみです。複数のデータタイプを選択した場合、Brazeはそれぞれに個別のカスタムオーディエンスを作成します。
{% endalert %}

{: start="4"}
4. ユーザーフィールドを選択した後、**Export セグメント**を選択します。CSVエクスポートと同様に、セグメントのFacebookへのエクスポートが完了するとメールが届きます。
5. [Facebook Ads Manager](https://www.facebook.com/ads/manager/audiences/manage/)でカスタムオーディエンスを確認します。

{% alert important %}
ユーザーのプライバシー上の理由から、Facebookでは以下を確認できません：

- カスタムオーディエンスに正常に追加された正確なユーザー。[個々のオーディエンスメンバーが非表示になる理由については、Facebookの詳細を参照してください](https://www.facebook.com/business/help/112061095610075)。
- カスタムオーディエンスのサイズ。[Facebookのオーディエンスサイズ推定値の変更に関する詳細を参照してください](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)。
{% endalert %}

#### オーディエンスエクスポートの設定 {#configuring-your-audience-export}

Facebook オーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したりしたい場合があります。また、[CCPA](https://oag.ca.gov/privacy/ccpa)に基づく「販売または共有の拒否」権利などのプライバシー法に準拠するためにも必要です。マーケターは、キャンバスのエントリ条件内にユーザーの適格性に関する関連フィルターを実装する必要があります。以下のオプションが役立ちます。

- [Braze SDKを通じてiOS IDFAを収集]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)している場合は、**Ads Tracking Enabled**フィルターを使用できます。値を`true`に設定すると、オプトインしたユーザーのみがオーディエンス同期の送信先に送信されます。

![Ads Tracking Enabledがtrueに設定されたキャンバスのエントリフィルター。]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- オプトイン、オプトアウト、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、キャンバスのエントリ条件にフィルターとして含める必要があります：

![エントリオーディエンスが「opted_in_marketing」が「true」に等しいキャンバス。]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### 類似オーディエンス {#lookalike-audiences}

セグメントをFacebook オーディエンスとして正常にエクスポートしたら、Facebookの[類似オーディエンス](https://www.facebook.com/business/help/164749007013531?id=401668390442328)を使用して追加のグループを作成できます。この機能は、選択したオーディエンスのデモグラフィック、興味、その他の属性を分析し、類似した属性を持つ新しいオーディエンスを作成します。

## トラブルシューティング {#troubleshooting}

### アクセストークンの検証エラー {#error-validating-access-token}

Facebook エクスポートを使用する際、`Error Validating Access Token` エラーは以下の場合に表示されます。
- パスワードを変更して、現在のセッションが無効になった場合
- セキュリティ上の理由で Facebook からログアウトされた場合

このエラーを解決するには、以下の手順に従ってください。
1. Facebook からログアウトし、再度ログインします。
2. Brazeで Facebook の認証情報を削除して保存します。セグメントのエクスポートを試みて（エクスポートアイコンが無効になっているはずです）、認証情報が削除されたことを確認します。
3. Facebook の認証情報を再度追加して保存します。
4. 再度エクスポートを試みます。

エクスポートがうまくいかない場合は、以下を行ってください。
1. 認証情報を再度削除して保存します。
2. 認証情報を再度追加して保存します。
3. **テクノロジーパートナー**ページで Facebook 連携を切断し、再接続します。

### Facebook オーディエンスのエクスポート時のエラー {#error-when-exporting-a-facebook-audience}

セグメントを Facebook オーディエンスとしてエクスポートする際にエラーが発生した場合、Facebook の開発者ドキュメントでは以下の一般的な原因が記載されています。

1. **アクセストークンがアプリと広告アカウントの管理者ではないユーザーのものである：** Brazeに接続されている Facebook ユーザーの認証情報には、適切な権限が必要です。
2. **エクスポート先の広告アカウントがアプリに関連付けられていない：** Facebook 広告アカウントが Facebook の設定でアプリにリンクされている必要があります。

以下のチェックで設定を確認してください。

- **アプリの管理者であることを確認する：** [developers.facebook.com](https://developers.facebook.com/) にアクセスし、**My Apps** を開き、自社のアプリを選択します。アプリが表示されない場合は、開発チームにあなたを追加してもらう必要がある場合があります。アプリのダッシュボードで **Roles** に移動し、自分のロール（Admin、Developer、Tester、または Analytics User）を確認します。
- **広告アカウントがアプリに関連付けられていることを確認する：** Facebook App Dashboard で **Settings** > **Advanced** に移動し、**Advertising Accounts** までスクロールして、Brazeオーディエンスエクスポートに使用する Facebook 広告アカウント ID がまだ一覧にない場合は追加します。
- **広告アカウントの管理者であることを確認する：** [business.facebook.com](https://business.facebook.com/) にアクセスし、メインメニューから **Business Settings** を開き、**Accounts** > **Ad accounts** に移動して広告アカウントを選択します。自分のアクセス権と、カスタムオーディエンスを作成するために必要な権限があることを確認します。

詳細については、[Facebook のカスタムオーディエンス API ドキュメント](https://developers.facebook.com/docs/)と [Facebook のビジネスヘルプセンターのカスタムオーディエンスガイド](https://www.facebook.com/business/help)を参照してください。