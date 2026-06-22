---
nav_title: ドラッグ＆ドロップエディター
article_title: ドラッグ＆ドロップエディターでアプリ内メッセージを作成する
alias: /iam_drag_and_drop/
page_order: 1
description: "このリファレンス記事では、ドラッグ＆ドロップエディターを使用したアプリ内メッセージの作成、前提条件、クリエイティブの詳細などについて説明します。"
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-level-styles'
  add-a-custom-font: '/docs/user_guide/channels/in_app_messages/customize/style_settings#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-components'
  creative-details: '/docs/user_guide/channels/in_app_messages/customize/style_settings#creative-details'
---

# ドラッグ＆ドロップでアプリ内メッセージを作成する {#create-an-in-app-message-with-drag-and-drop}

> ドラッグ＆ドロップエディターを使用すると、CampaignまたはCanvasのいずれかで、ドラッグ＆ドロップの編集体験を使って完全にカスタムでパーソナライズされたアプリ内メッセージを作成できます。エディターで使用できるビルディングブロックの詳細については、[エディターブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)を参照してください。


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

既存のカスタムHTMLテンプレートやサードパーティが作成したテンプレートを使用する場合は、ドラッグ＆ドロップエディターで再作成する必要があります。

アプリ内メッセージをCampaignで送信するか[Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)で送信するか迷っていますか？Campaignは単一のターゲットメッセージングに適しており、Canvasはマルチステップのユーザージャーニーに適しています。メッセージの作成場所を選択したら、ドラッグ＆ドロップのアプリ内メッセージを作成する手順を見ていきましょう。

## 前提条件 {#prerequisites}

### SDKの要件 {#sdk-requirements}

| 最小SDKバージョン | 推奨SDKバージョン |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDKの要件" }

{% details 最小SDKの詳細情報 %}

ドラッグ＆ドロップエディターで作成されたメッセージは、最小SDKバージョン（上記の表を参照）のユーザーにのみ送信できます。ユーザーがアプリケーションを更新していない場合（つまり、古いSDKバージョンを使用している場合）、アプリ内メッセージは受信されません。

ドラッグ＆ドロップエディターで利用可能なすべての機能を活用するには、SDKを推奨SDKバージョンに更新してください。これにより、以下の追加機能を利用できます。

- メッセージを閉じないテキストリンク
- プッシュプライマーをリクエストするボタンアクション

以下は、これらの機能の個別の最小SDK要件です。

| テキストリンク* | プッシュプライマーのリクエスト |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDKの要件" }

*アプリ内メッセージにURLにリダイレクトするリンクを含め、エンドユーザーが指定された最小SDKバージョンを使用していない場合、リンクを選択するとメッセージが閉じられ、ユーザーはフォームを送信するためにメッセージに戻ることができません。

{% enddetails %}

### その他の前提条件 {#additional-prerequisites}

- Web SDKの場合、初期化オプション[`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)を`true`に設定する必要があります。`enableHtmlInAppMessages`オプションもこれらのメッセージを機能させますが、非推奨であり、`allowUserSuppliedJavascript`に更新する必要があります。
- Google Tag Managerを使用している場合は、GTM設定で「Allow HTML In-App Messages」を有効にする必要があります。

## ステップ 1: アプリ内メッセージを作成する {#step-1-create-an-in-app-message}

新しいアプリ内メッセージまたはキャンバスステップを作成し、編集体験として**ドラッグ＆ドロップエディター**を選択します。

## ステップ 2: テンプレートを選択する {#step-2-select-your-template}

ドラッグ＆ドロップエディターを編集体験として選択した後、以下を選択できます。

- 空白のモーダルテンプレートから開始する
- Brazeのドラッグ＆ドロップアプリ内メッセージテンプレートを使用する
- 保存済みのドラッグ＆ドロップアプリ内メッセージテンプレートを選択する

**メッセージを作成**を選択して、ドラッグ＆ドロップエディターでアプリ内メッセージのデザインを開始します。

![基本、背景画像、電話番号キャプチャ、または空白テンプレートを選択できるBrazeテンプレートセクション。]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

ダッシュボードの**テンプレート**セクションからすべてのテンプレートにアクセスすることもできます。

## ステップ 3: 追加ページを追加する（オプション） {#multi-page}

アプリ内メッセージにページを追加すると、オンボーディングフローやウェルカムジャーニーのようなシーケンシャルフローでユーザーをガイドできます。ページは**ビルド**タブの**ページ**セクションから管理できます。

![3つのページで構成されたヘルスケア企業のアプリ内メッセージ。]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab ページの追加 %}

アプリ内メッセージはデフォルトで1ページから始まります。新しいページを追加するには：

1. **+ ページを追加**を選択します。
2. カスタムテンプレートまたはBraze提供のテンプレートのリストから選択します。
3. ページにわかりやすい名前を付けます。これはページ同士を接続する際に役立ちます。

{% alert tip %}
アプリ内メッセージごとに最大10ページまで追加できます。
{% endalert %}

既存のページを複製するには：

1. リスト内のページにカーソルを合わせ、<i class="fas fa-ellipsis-vertical" aria-label="その他のオプション"></i>**その他のオプション**を選択します。
2. **複製**を選択します。
3. ページにわかりやすい名前を付けます。これはページ同士を接続する際に役立ちます。

{% endtab %}
{% tab ページの削除または名前変更 %}

ページを削除または名前変更するには：

1. リスト内のページにカーソルを合わせ、<i class="fas fa-ellipsis-vertical" aria-label="その他のオプション"></i>**その他のオプション**を選択します。
2. **名前変更**または**削除**を選択します。

{% endtab %}
{% endtabs %}

### ステップ 3a: ページを接続する {#step-3a-connect-pages-together}

マルチページのアプリ内メッセージはシーケンシャルです。つまり、ユーザーはタップまたはクリックしてフロー内の次のページに移動することでメッセージを操作します。

ページを接続するには：

1. 開始ページを選択します。
2. キャンバス内のボタンまたは画像要素を選択します。
3. **クリック時の動作**を**ページに移動**に設定します。
4. 開始ページからリンクしたいページを選択します。
5. すべてのページがリンクされるまで続けます。

![アプリ内メッセージのページ2に移動するようにプライマリアクションボタンを編集しているユーザー。]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

ページが他のページにリンクされていない場合、メッセージを起動できません。

{% alert note %}
ユーザーはいつでも閉じるXボタンを選択してメッセージを終了できます。このボタンは削除できません。
{% endalert %}

## ステップ 4: アプリ内メッセージを構築・デザインする {#step-4-build-and-design-your-in-app-message}

ここでは、ブランド独自のスタイルでメッセージを仕上げます。エディターブロックとスタイル設定を組み合わせて、アプリ内メッセージをカスタマイズおよびデザインできます。

- 利用可能なエディターブロックとそのプロパティの一覧については、[エディターブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages)を参照してください。
- メッセージの外観と操作感のカスタマイズについては、[スタイル設定]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/)をご確認ください。
- 右から左へのメッセージ作成のベストプラクティスについては、[右から左へのメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/)を参照してください。

## ステップ 5: アプリ内メッセージをテストする {#step-5-test-your-in-app-message}

**プレビューとテスト**セクションでは、さまざまなデバイスでアプリ内メッセージをプレビューし、デバイスにテストメッセージを送信できます。ここで、ドラッグ＆ドロップのアプリ内メッセージCampaignのすべてのプラットフォームで詳細が揃っていることを確認できます。

Campaignを送信する前に、アプリ内メッセージを必ずテストすることが重要です。これにより、ユーザーの視点から最終的なメッセージがどのように見えるかを確認できます。

### ユーザーとしてメッセージをプレビューする {#preview-message-as-a-user}

{% alert warning %}
コンテンツテストグループまたは個別のユーザーにテストを送信するには、送信前にテストデバイスでプッシュが有効になっている必要があります。
{% endalert %}

**プレビューとテスト**タブから、ユーザーとしてメッセージをプレビューできます。特定のユーザー、ランダムなユーザーを選択するか、カスタムユーザーを作成できます。

- **ランダムユーザー：** Brazeがデータベースからランダムにユーザーを選択し、そのユーザーの属性やイベント情報に基づいてアプリ内メッセージをプレビューします。
- **ユーザーを選択：** メールアドレスまたは`external_id`に基づいて特定のユーザーを選択できます。アプリ内メッセージは、そのユーザーの属性とイベント情報に基づいてプレビューされます。
- **カスタムユーザー：** ユーザーをカスタマイズできます。Brazeは利用可能なすべての属性とイベントの入力欄を提供します。プレビューメールで確認したい情報を入力してください。

### テストチェックリスト {#test-checklist}

アプリ内メッセージをテストする際に、以下の質問を検討してください。

- さまざまなデバイスでメッセージをテストしましたか？
- 画像やメディアは期待どおりに表示され、動作していますか？
- Liquidは期待どおりに機能していますか？Liquidが情報を返さない場合のデフォルト属性値を考慮しましたか？
- コピーは明確で、簡潔で、正確ですか？
- ボタンはユーザーを正しい場所に誘導していますか？

## よくある質問 {#frequently-asked-questions}

#### 分析ページにボディクリックが表示されないのはなぜですか？ {#why-are-body-clicks-not-appearing-on-my-analytics-page}

ドラッグ＆ドロップエディターで作成されたアプリ内メッセージでは、ボディクリックは自動的に収集されません。詳細については、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310)および[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100)のSDK変更ログを参照してください。

#### ボタンクリックに基づいてセグメンテーションできますか？ {#can-i-segment-based-on-button-clicks}

はい、メッセージ内の最大2つのボタンのボタンクリックに基づいてセグメンテーションできます。これを行うには、ボタンの**Identifier for Reporting**を「0」と「1」に設定します。これはそれぞれ、セグメンテーションフィルター「Clicked in-app message button 1」と「Clicked in-app message button 2」に対応します。

![値が「0」の「Identifier for Reporting」フィールド。]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

#### カスタムHTMLやJavaScriptを使用してアプリ内メッセージをカスタマイズしたり、既存のHTMLメッセージをエディターに移行したりできますか？ {#can-i-customize-my-in-app-message-using-custom-html-or-javascript-or-transfer-existing-html-messages-into-the-editor}

既存のHTMLメッセージをエディターに直接移行することはできませんが、カスタムコードブロックに生のHTML、CSS、JavaScriptを挿入できます。カスタムコードブロックを使用して、サードパーティの動画や、コネクテッドコンテンツや条件文などの高度なLiquidを埋め込むことができます。

#### スライドアップのアプリ内メッセージを作成するにはどうすればよいですか？ {#how-can-i-create-a-slideup-in-app-message}

現在、エディターはモーダルとフルスクリーンメッセージのみに対応しています。**Message styles**パネルの**Message container**セクションで表示タイプを切り替えることができます。

#### CampaignまたはCanvas内で作成したアプリ内メッセージをテンプレートとして保存できますか？ {#can-i-save-my-in-app-message-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

はい。今後のCampaignまたはキャンバスステップで再利用したいアプリ内メッセージは、エディターを終了した後に表示される**テンプレートとして保存**ボタンを使用して、カスタムテンプレートとして保存できます。テンプレートとして保存する前に、まずCampaignを起動するか、下書きとして保存する必要があります。

![製品ツアーのアプリ内メッセージのプレビュー。]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

**コンテンツ** > **アプリ内メッセージ**に移動して、アプリ内メッセージテンプレートを作成および保存することもできます。