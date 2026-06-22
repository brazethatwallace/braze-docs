---
nav_title: Canva
article_title: Canva
description: "このリファレンス記事では、BrazeとCanvaのパートナーシップについて説明します。メディアアセットをBrazeメディアライブラリにプッシュしたり、CanvaのメールデザインをBrazeメールテンプレートとして公開したりできます。"
alias: /partners/canva/
page_type: partner
search_tag: Partner

---

# Canva

> [Canva](https://www.canva.com/)は、ソーシャルメディアの投稿、プレゼンテーション、動画などのビジュアルコンテンツを作成できるグラフィックデザインプラットフォームおよびツールです。CanvaのBrazeアプリは、静的デザインをメディアライブラリに送信するだけでなく、**メール**デザインをBrazeメールテンプレートとしてエクスポートすることもサポートしています。

## 連携について {#about-the-integration}

BrazeとCanvaの連携は、2つのエクスポートパスをサポートしています。

| エクスポートタイプ | 機能 |
| --- | --- |
| **画像またはデザインをメディアライブラリへ** | デザインをアセットとしてBrazeメディアライブラリに送信します。 |
| **メールデザインをBrazeへ** | Canvaの**メール**ドキュメントを、件名メタデータを含むBrazeメールテンプレートとして公開します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="連携について" }

## BrazeとCanvaを連携する {#integrate-braze-with-canva}

### ステップ 1:CanvaにBrazeアプリをインストールする {#step-1-install-the-braze-app-in-canva}

Brazeアプリは[Canva Apps Marketplace](https://www.canva.com/your-apps/AAG1cO7kIyc)で見つけることができます。

アプリをインストールすると、デザイン内の**Apps**メニューから利用できるようになります。

![CanvaのAppsメニューに表示されたBrazeアプリ。]({% image_buster /assets/img/canva_integration/braze-canva-app.png %}){: style="max-width:50%;"}

### ステップ 2:Brazeアカウントを認証する {#step-2-authorize-your-braze-account}

Brazeアプリを初めて使用する際、**Apps**メニュー（メディアライブラリエクスポート）または**Share**メニュー（メールエクスポート）のどちらから開いた場合でも、**Connect**を選択して認証を開始します。これにより、Canvaがアクセス可能なBrazeワークスペースを一覧表示し、代わりにメディアライブラリアセットを作成できるようになります。

**メール**エクスポートの場合、Canvaから再度サインインし、**メールテンプレートの作成**権限を含む追加アクセスの承認を求められることがあります。メールデザインをBrazeに公開するには、これらの権限を承認してください。

![CanvaとBrazeを連携するための接続ボタンと認証フロー。]({% image_buster /assets/img/canva_integration/canva-connect-panel.jpg %})

## 画像をメディアライブラリにエクスポートする {#export-images-to-the-media-library}

Brazeメディアライブラリにファイルを保存したい場合、標準的なCanvaデザインでこのフローを使用します。

1. デザインの**Apps**メニューからBrazeアプリを開きます。まだ接続していない場合は、**Connect**を選択し、[Brazeアカウントを認証する](#step-2-authorize-your-braze-account)の手順を完了します。
2. 送信先のワークスペースを選択し、必要に応じてファイル名を入力して、**Start Export**を選択します。

![送信先ワークスペースとStart Exportボタンが表示されたCanvaのエクスポート画面。]({% image_buster /assets/img/canva_integration/canva-upload-screen.jpg %})

{: start="3"}
3. エクスポートが完了すると、新しいアセットが**メディアライブラリ**でソース「Canva」として利用可能になります。

![BrazeメディアライブラリにエクスポートされたCanvaアセット。]({% image_buster /assets/img/canva_integration/media-library-source.jpg %})

## メールデザインをBrazeテンプレートとしてエクスポートする {#export-email-designs-as-braze-templates}

Canvaファイルが**メール**デザインタイプの場合、このフローを使用します。HTMLをテンプレートとしてBrazeに公開します（画像フローと同様のメタデータですが、**Apps**ではなく**Share**から開始します）。

1. Canvaで**メール**デザインを作成するか開きます。ゼロからメッセージを作成するか、Canvaのメールテンプレートを使用します。
2. エディターの右上にある**Share**をクリックし、**Braze**を選択します。Brazeが表示されていない場合は、**See more**を開き、**More options**までスクロールしてBrazeを見つけます。

![CanvaのMore optionsにBrazeが表示された公開オプション。]({% image_buster /assets/img/canva_integration/canva-share-more-options-braze.png %})

{: start="3"}
3. 接続または再度サインインを求められた場合は、Brazeパネルで**Connect**を選択し（またはブラウザのサインインフローを完了し）、Canvaがワークスペースにテンプレートを作成できるようにします。

![メールエクスポートのために接続を促すCanvaのBrazeサイドバー。]({% image_buster /assets/img/canva_integration/canva-email-connect-sidebar.png %})

{: start="4"}
4. Brazeパネルで、公開する**メール**ページを選択し（デザインに複数のページがある場合）、**Brazeワークスペース**を選択し、**テンプレート名**と**件名**を入力して、**Publish now**を選択します。デザインの公開中、Canvaが進捗状況を表示します。

![ワークスペース、テンプレート名、件名、Publish nowが表示されたCanvaのBrazeパネル。]({% image_buster /assets/img/canva_integration/canva-email-publish-fields.png %})

{: start="5"}
5. 公開が完了すると、成功メッセージが表示されます。**Check it out**を選択して、Brazeでメールテンプレートを開きます。

![CanvaのメールデザインをBrazeに公開した後の成功メッセージとCheck it outボタン。]({% image_buster /assets/img/canva_integration/canva-email-publish-success.png %})

{: start="6"}
6. Brazeで、CampaignまたはCanvasでテンプレートを使用する前に、**From**アドレス、プリヘッダー、配信停止リンクなどの必要なメール設定を完了します。

![Canvaから開いたBrazeのメールテンプレート。送信情報とプレビューが表示されています。]({% image_buster /assets/img/canva_integration/braze-email-template-from-canva.png %})