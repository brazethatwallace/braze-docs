---
nav_title: 7月
page_order: 6
noindex: true
page_type: update
description: "この記事には2019年7月のリリースノートが含まれています。"
---

# 2019年7月 {#july-2019}

{% alert update %}
Brazeでは今月、2回（そうです、**2回**です）の製品リリースサイクルがありました。最新のリリースはページ上部に記載されており、それ以前のリリースは[ページ下部に記載されています](#earlier-this-month)。
{% endalert %}

## SAML/SSO

[シングルサインオン]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/)（SSO）は、Brazeダッシュボードへのアクセスを制御する安全かつ一元化された方法を企業に提供します。つまり、1組の認証情報を使用して、Brazeを含むさまざまなアプリケーションにアクセスできます。

[OAuth 2.0サポートを使用したGoogleサインイン](https://developers.google.com/identity/protocols/OAuth2)に加えて、企業はSecurity Assertion Markup Language（SAML）サポートを使用したSSOを希望しています。これにより、最新の業界標準（SAML 2.0）に対応した[Azure Active Directory]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso/)や[Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta/)を含む大規模なIDプロバイダー（IdP）とシームレスに統合できます。

Brazeは以下をサポートしています。
- [OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/microsoft_entra_sso/)
- [Okta]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/okta/)

## AdjustイベントAPIキーの表示 {#adjust-event-api-key-shows}

Adjustのパートナーページを更新し、お客様がこのAPIキーにアクセスできるようにしました。

## 新しいパートナー {#new-partners}

いくつかの新しいパートナーがAlloysプログラムに参加し、ドキュメントに追加されました。新しいパートナーは以下のとおりです。
- [FiveTran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## キャンペーン詳細の改善 {#campaign-details-improvement}

拡張されたキャンペーン詳細が、**キャンペーン**ページの…お待たせしました…**キャンペーンの詳細**セクションに表示されるようになりました！

## セグメントとキャンバスで「自分のものだけを表示」 {#show-only-mine-in-segments-canvas}

**キャンペーン**ページの「自分のものだけを表示」チェックフィルターは非常に人気があることが証明されています。そのため、キャンバスおよびセグメントリストにもこのオプションを追加します！

### 進行動作 {#advancement-behavior}

ユーザーが1つのキャンバスステップから次のステップに[進むタイミング]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/)を選択できるようになりました。これらのオプションには「メッセージ送信済み」と「遅延後にオーディエンス全体」が含まれます。

### キャンバスのアプリ内メッセージ {#in-app-messages-in-canvas}

[アプリ内メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)をキャンバスで利用できるようになりました。キャンバスステップを追加し、使用可能なチャネルを参照してアプリ内メッセージを追加します。

# 今月上旬 {#earlier-this-month}

## ユーザープロファイル画像の削除 {#user-profile-image-removal}

Brazeユーザープロファイルおよびユーザー検索で表示されるユーザープロファイル画像を削除します。

## Content Cardsのコネクテッドコンテンツ {#connected-content-in-content-cards}

[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)の文字列と機能を[Content Cards]({{site.baseurl}}/user_guide/channels/content_cards/)で使用できるようになりました。

外部サーバーへのコネクテッドコンテンツ呼び出しは、カードがユーザーによって表示されたときではなく、カードが実際に送信されたときに実行されます。メールと同様に、ダイナミックコンテンツはカードが実際に表示されたときではなく、送信時に計算および決定されます。

## Null「返信先」アドレス {#null-reply-to-address}

Brazeの**メール設定**ページから、または[API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification)を使用して、メールメッセージの「返信先」アドレスに`null`値を設定できるようになりました。この設定を使用すると、リストの「差出人」アドレスに返信が送信されます。「差出人」アドレスフィールドを`dan@emailaddress.com`としてパーソナライズできるようになり、お客様はDanに直接返信できるようになります。

Brazeからメールメッセージの「返信先」アドレスに`null`値を設定するには、ナビゲーションの**設定の管理**に移動し、**メール設定**タブに移動します。**送信メール設定**セクションまでスクロールし、デフォルトアドレスとして**「返信先」を除外し、返信を「差出人」に送信**を選択します。

## キャンペーン比較 {#campaign-comparisons}

[複数のキャンペーンを一度に確認し、相対的なパフォーマンスを比較]({{site.baseurl}}/report_builder/)できます。Brazeで1つのウィンドウに並べて表示しましょう！

## LiquidでディスパッチIDをメッセージにテンプレート化する {#template-dispatch-id-into-messages-with-liquid}

{% alert note %}
`dispatch_id`の動作はキャンバスとキャンペーンで異なります。これは、Brazeがキャンバスステップ（スケジュール可能なエントリステップを除く）を、「スケジュール済み」の場合でもトリガーされたイベントとして扱うためです。キャンバスとキャンペーンでの[`dispatch_id`の動作]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id/)の詳細を確認してください。
{% endalert %}

（URLなどで）メッセージ内からメッセージのディスパッチを追跡する場合は、`dispatch_id`でテンプレート化できます。この書式は、サポートされているパーソナライゼーションタグの一覧の[キャンバス属性]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)にあります。

これは`api_id`と同じように動作します。つまり、`api_id`はキャンペーンの作成時に使用できないため、プレースホルダーとしてテンプレート化され、`dispatch_id_for_unsent_campaign`としてプレビューされます。IDはメッセージが送信される前に生成され、送信時に含まれます。

{% alert warning %}
アプリ内メッセージには`dispatch_id`がないため、`dispatch_id_for_unsent_campaign`のLiquidテンプレート化はアプリ内メッセージでは機能しません。
{% endalert %}

## 「自分のものだけを表示」設定の保持 {#show-only-mine-setting-persists}

キャンペーングリッドの「自分のものだけを表示」フィルターは、**キャンペーン**ページにアクセスするたびに保持されるようになりました。

## ABテストの更新 {#ab-testing-updates}

1回限りの[ABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing/)を、最大8つのバリアント（およびオプションのコントロール）とともに、ユーザーが指定した割合のキャンペーンオーディエンスに送信してから、事前にスケジュールされた時間に残りのオーディエンスに最適なバリアントを送信できます。