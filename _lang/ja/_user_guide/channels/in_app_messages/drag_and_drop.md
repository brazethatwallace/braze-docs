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

> ドラッグ＆ドロップエディターを使用すると、キャンペーンまたはキャンバスのいずれかで、ドラッグ＆ドロップの編集体験を使って完全にカスタムでパーソナライズされたアプリ内メッセージを作成できます。エディターで使用できるビルディングブロックの詳細については、[エディターブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages)を参照してください。


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

既存のカスタムHTMLテンプレートやサードパーティが作成したテンプレートを使用する場合は、ドラッグ＆ドロップエディターで再作成する必要があります。

アプリ内メッセージをキャンペーンで送信するか[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas)で送信するか迷っていますか？キャンペーンは単一のターゲットメッセージングに適しており、キャンバスはマルチステップのユーザージャーニーに適しています。メッセージの作成場所を選択したら、ドラッグ＆ドロップのアプリ内メッセージを作成する手順を見ていきましょう。

## 前提条件 {#prerequisites}

### SDKの要件 {#sdk-requirements}

| 最小SDKバージョン                                                          | 推奨SDKバージョン                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDKの要件" }

{% details 最小SDKの詳細情報 %}

ドラッグ＆ドロップエディターを使用して作成されたメッセージは、最小SDKバージョン（前のセクションの表を参照）のユーザーにのみ送信できます。ユーザーがアプリケーションを更新していない場合（つまり、古いSDKバージョンを使用している場合）、アプリ内メッセージは受信されません。

ドラッグ＆ドロップエディターで利用可能なすべての機能を活用するには、SDKを推奨SDKバージョンに更新してください。これにより、以下の追加機能を利用できます。

- メッセージを閉じないテキストリンク
- プッシュプライマーをリクエストするボタンアクション

以下は、これらの機能の個別の最小SDK要件です。

| テキストリンク*                                                         | プッシュプライマーのリクエスト                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SDKの要件" }

*アプリ内メッセージにURLにリダイレクトするリンクを含めた場合、エンドユーザーが指定された最小SDKバージョンを使用していないと、リンクを選択するとメッセージが閉じられ、ユーザーはフォームを送信するためにメッセージに戻ることができません。

{% enddetails %}

### その他の前提条件 {#additional-prerequisites}

- Web SDKの場合、初期化オプション[`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)を`true`に設定する必要があります。`enableHtmlInAppMessages`オプションでもこれらのメッセージは機能しますが、非推奨であるため`allowUserSuppliedJavascript`に更新してください。
- Google Tag Managerを使用している場合は、GTM設定で「Allow HTML In-App Messages」を有効にする必要があります。

## ステップ1：アプリ内メッセージを作成する {#step-1-create-an-in-app-message}

新しいアプリ内メッセージまたはキャンバスステップを作成し、編集エクスペリエンスとして**ドラッグ＆ドロップエディター**を選択します。

## ステップ2：テンプレートを選択する {#step-2-select-your-template}

編集エクスペリエンスとしてドラッグ＆ドロップエディターを選択した後、以下のオプションから選択できます。

- 空白のモーダルテンプレートから始める
- Brazeのドラッグ＆ドロップアプリ内メッセージテンプレートを使用する
- 保存済みのドラッグ＆ドロップアプリ内メッセージテンプレートを選択する

**メッセージを作成**を選択して、ドラッグ＆ドロップエディターでアプリ内メッセージのデザインを開始します。

![基本、背景画像、電話番号キャプチャ、または空白テンプレートを選択できるBrazeテンプレートセクション。]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

ダッシュボードの**テンプレート**セクションからすべてのテンプレートにアクセスすることもできます。

## ステップ3:追加ページを追加する（オプション） {#multi-page}

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

1. リスト内のページにカーソルを合わせ、<i class="fas fa-ellipsis-vertical" aria-label="その他のオプション"></i> **その他のオプション**を選択します。
2. **複製**を選択します。
3. ページにわかりやすい名前を付けます。これはページ同士を接続する際に役立ちます。

{% endtab %}
{% tab ページの削除または名前変更 %}

ページを削除または名前変更するには：

1. リスト内のページにカーソルを合わせ、<i class="fas fa-ellipsis-vertical" aria-label="その他のオプション"></i> **その他のオプション**を選択します。
2. **名前変更**または**削除**を選択します。

{% endtab %}
{% endtabs %}

### ステップ3a:ページを接続する {#step-3a-connect-pages-together}

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

## ステップ4: アプリ内メッセージを構築・デザインする {#step-4-build-and-design-your-in-app-message}

ここでは、ブランド独自のスタイルを反映させてメッセージをデザインします。エディターブロックとスタイル設定を組み合わせて、アプリ内メッセージをカスタマイズおよびデザインできます。

- 利用可能なエディターブロックとそのプロパティの一覧については、[エディターブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages)を参照してください。
- メッセージのルック＆フィールのカスタマイズについては、[スタイル設定]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings)をご確認ください。
- 右から左に読むメッセージの作成に関するベストプラクティスについては、[右から左に読むメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

## ステップ5：アプリ内メッセージをテストする {#step-5-test-your-in-app-message}

**プレビューとテスト**セクションでは、さまざまなデバイスでアプリ内メッセージをプレビューし、デバイスにテストメッセージを送信できます。ここでは、ドラッグ＆ドロップのアプリ内メッセージキャンペーンのすべてのプラットフォームで詳細が整合していることを確認できます。

キャンペーンを送信する前に、必ずアプリ内メッセージをテストすることが重要です。これにより、ユーザーの視点から最終的なメッセージがどのように表示されるかを確認できます。

### ユーザーとしてメッセージをプレビューする {#preview-message-as-a-user}

{% alert warning %}
コンテンツテストグループまたは個々のユーザーにテストを送信するには、送信前にテストデバイスでプッシュを有効にする必要があります。
{% endalert %}

**プレビューとテスト**タブから、ユーザーとしてメッセージをプレビューできます。特定のユーザー、ランダムなユーザーを選択するか、カスタムユーザーを作成できます。

- **ランダムなユーザー：** Brazeはデータベースからランダムにユーザーを選択し、そのユーザーの属性やイベント情報に基づいてアプリ内メッセージをプレビューします。
- **ユーザーを選択：** メールアドレスまたは`external_id`に基づいて特定のユーザーを選択できます。アプリ内メッセージは、そのユーザーの属性とイベント情報に基づいてプレビューされます。
- **カスタムユーザー：** ユーザーをカスタマイズできます。Brazeは利用可能なすべての属性とイベントの入力フィールドを提供します。プレビューメールに表示したい情報を入力してください。

### テストチェックリスト {#test-checklist}

アプリ内メッセージをテストする際に、以下の点を確認してください。

- さまざまなデバイスでメッセージをテストしましたか？
- 画像やメディアは期待どおりに表示され、動作しますか？
- Liquidは期待どおりに機能しますか？Liquidが情報を返さない場合に備えて、デフォルトの属性値を設定しましたか？
- コピーは明確で簡潔、かつ正確ですか？
- ボタンはユーザーを適切な場所に誘導しますか？

## よくある質問 {#frequently-asked-questions}

### 分析ページにボディクリックが表示されないのはなぜですか？ {#why-are-body-clicks-not-appearing-on-my-analytics-page}

ドラッグ＆ドロップエディターで作成されたアプリ内メッセージでは、ボディクリックは自動的に収集されません。詳細については、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310)および[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100)のSDK変更ログを参照してください。

### ボタンクリックに基づいてセグメントを作成できますか？ {#can-i-segment-based-on-button-clicks}

はい、メッセージ内の最大2つのボタンのクリックに基づいてセグメントを作成できます。これを行うには、ボタンの**レポート用識別子**を「0」と「1」に設定します。これにより、セグメンテーションフィルター「アプリ内メッセージボタン1をクリック」と「アプリ内メッセージボタン2をクリック」にそれぞれ対応します。

![「レポート用識別子」フィールドに値「0」が設定されている画面]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

### カスタムHTMLやJavaScriptを使用してアプリ内メッセージをカスタマイズしたり、既存のHTMLメッセージをエディターに移行したりできますか？ {#can-i-customize-my-in-app-message-using-custom-html-or-javascript-or-transfer-existing-html-messages-into-the-editor}

既存のHTMLメッセージをエディターに直接移行することはできませんが、**カスタムコード**ブロックに生のHTML、CSS、JavaScriptを挿入できます。**カスタムコード**ブロックを使用して、サードパーティの動画や、Connected Contentや条件文などの高度なLiquidを埋め込むことができます。`brazeBridge` JavaScriptメソッドとクリックトラッキングの例については、[カスタムHTMLアプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html)を参照してください。

### ドラッグ＆ドロップエディターのコンポーザービューが最終的なメッセージと異なって見えるのはなぜですか？ {#why-might-the-drag-and-drop-editors-composer-view-look-different-from-the-final-message}

ドラッグ＆ドロップエディターは、コンポーザー内でメッセージをレンダリングし、プレビュー専用のスタイルとデフォルトを適用して、レイアウトの構築と確認ができるようにしています。これらの処理は、編集中に構造やプレースホルダーコンテンツを確認するためのものであり、ユーザーが受け取るメッセージには含まれません。

エディター専用の動作の一般的な例は以下のとおりです。

- エディターは**カスタムコード**ブロックを`bz-html-code-block`コンテナでラップし、デフォルトの`min-height`を`40px`に設定するため、空のブロックや短いブロックでも編集中に表示されます
- 画像が空白であったり、Liquidを含んでいる場合にエディターでプレースホルダーが表示されます
- チェックボックスグループやラジオボタンが最初のオプションを事前選択し、アクティブ状態をプレビューできるようにします

エディターでのみ異なって見える場合は、通常プレビューの動作です。配信されたメッセージのトラブルシューティングを行う際は、エディター専用のフレームやプレビューのデフォルトではなく、メッセージブロック内のスタイルとマークアップを確認してください。

### スライドアップアプリ内メッセージを作成するにはどうすればよいですか？ {#how-can-i-create-a-slideup-in-app-message}

現在、エディターはモーダルとフルスクリーンメッセージのみに対応しています。**メッセージスタイル**パネルの**メッセージコンテナ**セクションで表示タイプを切り替えることができます。

### キャンペーンまたはキャンバス内で作成したアプリ内メッセージをテンプレートとして保存できますか？ {#can-i-save-my-in-app-message-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

はい。今後のキャンペーンやキャンバスステップで再利用したいアプリ内メッセージは、エディターを終了した後に表示される**テンプレートとして保存**ボタンを使用して、カスタムテンプレートとして保存できます。テンプレートとして保存するには、まずキャンペーンを開始するか、下書きとして保存する必要があります。

![製品ツアー用のアプリ内メッセージのプレビュー]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

また、**コンテンツ** > **アプリ内メッセージ**に移動して、アプリ内メッセージテンプレートを作成・保存することもできます。

### ページ分割されたアプリ内メッセージでLiquid構文がプレーンテキストとして表示されるのはなぜですか？ {#why-is-my-liquid-syntax-appearing-as-plain-text-in-my-paginated-in-app-message}

ページ分割されたアプリ内メッセージのテスト時にLiquid構文がプレーンテキストとして表示される場合（パーソナライズされたコンテンツの代わりに）、いずれかのページにLiquid構文エラーがある可能性があります。1つのページに構文エラーがあると、メッセージ内のすべてのページのLiquidレンダリングに影響します。ページは独立していません。

トラブルシューティングの手順：

1. メッセージ内のすべてのページでLiquid構文エラーを確認してください。1つのページでプレビューが壊れていても、そのページにエラーがあるとは限りません。ページは独立していないため、構文エラーはメッセージ内のどこにでも存在する可能性があります。
2. すべてのLiquidタグが正しく閉じられ、正しい形式になっていることを確認してください。