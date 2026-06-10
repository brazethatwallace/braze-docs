---
nav_title: Facebook
article_title: Facebookオーディエンスエクスポート
alias: /partners/facebook/
description: "このリファレンス記事では、ブランドが顧客にリーチしエンゲージするための主要なソーシャルプラットフォームであるFacebookとBrazeのパートナーシップについて説明します。"
page_type: partner
search_tag: Partner

---

# Facebookオーディエンスエクスポート {#facebook-audience-export}

> BrazeとFacebookの統合により、BrazeのSegmentsを手動でFacebookにエクスポートし、Facebookカスタムオーディエンスを作成できます。これは1回限りの静的オーディエンスエクスポートであり、新しいFacebookカスタムオーディエンスのみが作成されます。

Facebookカスタムオーディエンスをエクスポートする一般的なユースケースには、以下のようなものがあります。
- ライフサイクル内の特定のポイントでユーザーをリターゲティングする
- 除外ターゲットリストの作成
- 新規ユーザーをより効率的に獲得するための[類似オーディエンス](https://www.facebook.com/business/help/164749007013531?id=401668390442328)を作成する
<br><br>

{% alert note %}
Facebookオーディエンスエクスポートは、**ユーザーアクセストークン**を使用してリクエストを承認します。<br><br>
この機能を[Facebookへのオーディエンス同期]({{site.baseurl}}/audience_sync_facebook/)機能と一緒に使用している場合、Brazeはリクエストを承認するために、すでに生成した、より信頼性の高い**システムユーザートークン**をデフォルトで使用します。
{% endalert %}

{% alert note %}
ベータ版のMeta ワークアカウントのテストに参加している場合は、アカウントを接続解除してから[Facebookパートナーページ]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#step-1-connect-to-facebook)に再接続してください。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| [Facebook Business Manager](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | ブランドのFacebook資産（広告アカウント、ページ、アプリなど）を一元管理するツールです。 |
| [Facebook広告アカウント](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Brazeカスタムオーディエンスで使用したい、ブランドのビジネスマネージャーに紐づくアクティブなFacebook広告アカウントです。<br><br>Facebookビジネスマネージャーの管理者が、Brazeで使用する予定のFacebook広告アカウントの管理者権限を付与していること、および広告アカウントの利用規約に同意していることを確認してください。そうしないと、Braze内でFacebook広告アカウントにアクセスできなくなります。 |
| [Facebookカスタムオーディエンス利用規約](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Brazeで使用する予定のFacebook広告アカウントについて、Facebookのカスタムオーディエンス利用規約に同意する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1:Facebookに接続する {#step-1-connect-to-facebook}

1. Brazeダッシュボードで**パートナー連携** > **テクノロジーパートナー**に移動し、**Facebook**を選択します。

{: start="2"}
2. Facebookオーディエンスエクスポートモジュールで、**Connect Facebook**を選択します。<br><br>![BrazeプラットフォームのFacebookテクノロジーパートナーページ。]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. Facebook oAuthダイアログウィンドウで、BrazeがFacebook広告アカウントにカスタムオーディエンスを作成することを承認します。<br><br>![最初のFacebookダイアログボックス。「Connect as X」（XはFacebookユーザー名）で接続するように促されます。]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"} ![広告アカウントの広告を管理する許可を求める2つ目のFacebookダイアログボックス。]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. BrazeがFacebookアカウントとリンクされたら、Brazeワークスペース内で同期したい広告アカウントを選択します。<br><br>![Facebookに接続可能な広告アカウントのリスト。]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> 接続後にパートナーページが再び表示され、どのアカウントが接続されているかを確認したり、既存のアカウントを切断したりできます。<br><br> ![広告アカウントが正常に接続されたことを示す更新後のFacebookテクノロジーパートナーページ。]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Facebookとの接続は、Brazeのワークスペースレベルで適用されます。Facebook管理者があなたをFacebook Business Managerから削除したり、接続しているFacebookアカウントへのアクセスを削除した場合、Brazeは無効なトークンを検出します。その結果、Facebookオーディエンスステップを使用しているアクティブなCanvasesにはエラーが表示され、Brazeはユーザーを同期できません。

{% alert important %}
これまでに[Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management)および[Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard)のFacebookアプリレビュープロセスを受けたことがある顧客のシステムユーザートークンは、Facebookオーディエンスステップに対して引き続き有効です。Facebookのパートナーページを通じて、Facebookシステムユーザートークンを編集したり、取り消したりすることはできません。代わりにFacebookアカウントを接続して、Brazeワークスペース内のFacebookシステムユーザートークンを置き換えることができます。

<br><br>新しいFacebook oAuth設定は、[Segmentsを使用したFacebookエクスポート]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites)にも適用されます。
{% endalert %}

### ステップ2:Facebookにユーザーをエクスポートする {#step-2-export-your-users-into-facebook}

Brazeでは、Facebookオーディエンスのエクスポートは**Segments**ページからアクセスできます。

1. **Segments**ページで、エクスポートするSegmentを選択します。
2. **ユーザーデータ**を選択し、**Facebookオーディエンスとしてエクスポート**を選択します。<br><br>![「ユーザーデータ」を選択したSegmentの「Segment詳細」セクションに、「Facebookオーディエンスとしてエクスポート」を含むオプションのドロップダウンが表示されます。]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Braze内でFacebookをまだアクティブにしていない場合は、ダッシュボードでFacebookテクノロジーパートナーページに移動するように促されます。**テクノロジーパートナー** > **Facebook**を通じてすでにFacebookをアクティブにしている場合は、Facebook広告アカウントとエクスポートするユーザーフィールドを選択できます。<br><br> エクスポートできるフィールドは以下のとおりです。
- デバイスIDFA
- 電話番号
- メール

{% alert note %}
1回のエクスポートで選択できるユーザーフィールドは1つだけです。複数のデータタイプを選択した場合、Brazeはそれぞれに個別のカスタムオーディエンスを作成します。
{% endalert %}

{: start="4"}
4. ユーザーフィールドを選択したら**Segmentをエクスポート**を選択します。CSVエクスポートと同様に、Facebookへのセグメントのエクスポートが完了するとメールが届きます。
5. [Facebook広告マネージャー](https://www.facebook.com/ads/manager/audiences/manage/)でカスタムオーディエンスを表示します。

{% alert important %}
ユーザーのプライバシー上の理由により、Facebookでは以下の内容を表示できません。

- カスタムオーディエンスに正常に追加された正確なユーザー。[詳細をご覧ください。](https://www.facebook.com/business/help/112061095610075)
- カスタムオーディエンスのサイズ。[詳細をご覧ください。](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### オーディエンスのエクスポートを設定する {#configuring-your-audience-export}

Facebookオーディエンスを構築する際、ユーザーの嗜好に基づき、また[CCPA](https://oag.ca.gov/privacy/ccpa)に基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合があります。マーケターは、Canvasのエントリ基準の範囲内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかの選択肢を挙げます。

- [Braze SDKを通じてiOS IDFAを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection)収集した場合、**Ads Tracking Enabled**フィルターを使用できます。ユーザーがオプトインしたオーディエンス同期の送信先にのみユーザーを送信するには、値を`true`に選択します。

![]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- オプトイン、オプトアウト、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集する場合は、Canvasのエントリ基準にこれらをフィルターとして含める必要があります。

![エントリオーディエンスが「opted_in_marketing」が「true」に等しいCanvas。]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### 類似オーディエンス {#lookalike-audiences}

Facebookオーディエンスとしてセグメントをエクスポートしたら、Facebookの[類似オーディエンス](https://www.facebook.com/business/help/164749007013531?id=401668390442328)を使用して追加のグループを作成できます。この機能は、選択したオーディエンスのデモグラフィック、興味、その他の属性を調べ、類似する属性を持つ新しいオーディエンスを作成します。

## トラブルシューティング {#troubleshooting}

### アクセストークンの検証エラー {#error-validating-access-token}

Facebook Exportを使用している場合、以下の状況で`Error Validating Access Token`エラーが表示されます。
- パスワードを変更したため、現在のセッションが無効になった
- セキュリティ上の予防措置として、Facebookがログアウトさせた

このエラーを解決するには、以下のステップに従ってください。
1. Facebookからログアウトし、再度ログインします。
2. BrazeでFacebookの認証情報を削除し、保存します。セグメントをエクスポートしてみて、認証情報が削除されたことを確認します（エクスポートアイコンは無効になっているはずです）。
3. Facebookの認証情報を再度追加して保存します。
4. もう一度エクスポートを試みます。

エクスポートがうまくいかない場合は、以下を行ってください。
1. 認証情報をもう一度削除し、保存します。
2. 認証情報を再度追加し、保存します。
3. **テクノロジーパートナー**ページでFacebookとの連携を解除し、再接続します。

### Facebookオーディエンスのエクスポート時のエラー {#error-when-exporting-a-facebook-audience}

Facebookオーディエンスとしてセグメントをエクスポートする際にエラーが発生した場合、Facebookの開発者ドキュメントでは以下の一般的な原因が記載されています。

1. **アクセストークンが、アプリと広告アカウントの管理者ではないユーザーのものである：** Brazeに接続されているFacebookユーザーの認証情報には、適切な権限が必要です。
2. **エクスポート先の広告アカウントがアプリに関連付けられていない：** Facebook広告アカウントは、Facebookの設定でアプリにリンクされている必要があります。

以下のチェックを行い、設定を確認してください。

- **アプリの管理者であることを確認する：** [developers.facebook.com](https://developers.facebook.com/)にアクセスし、**My Apps**を開いて、会社のアプリを選択します。アプリが表示されない場合は、開発チームにあなたを追加してもらう必要があるかもしれません。アプリのダッシュボードで、左側のメニューの**Roles**に移動し、自分のロール（Admin、Developer、Tester、またはAnalytics User）を確認します。
- **広告アカウントがアプリに関連付けられていることを確認する：** Facebook App Dashboardで、**Settings** > **Advanced**に移動し、**Advertising Accounts**までスクロールして、Brazeオーディエンスエクスポートに使用したいFacebook広告アカウントIDがまだリストにない場合は追加します。
- **広告アカウントの管理者であることを確認する：** [business.facebook.com](https://business.facebook.com/)にアクセスし、左上のドロップダウンから**Business Settings**を選択します。次に、**Accounts** > **Ad accounts**に移動し、広告アカウントを選択します。アクセス権があること、およびカスタムオーディエンスを作成するために必要な権限があることを確認します。

詳細については、[FacebookのCustom Audience APIドキュメント](https://developers.facebook.com/docs/)および[Facebookのビジネスヘルプセンターのカスタムオーディエンスガイド](https://www.facebook.com/business/help)を参照してください。