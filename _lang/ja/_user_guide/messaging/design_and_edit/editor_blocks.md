---
nav_title: エディターブロック
article_title: ドラッグ＆ドロップエディターブロック
alias: "/dnd/editor_blocks/"
channel:
- email
- in-app messages
- landing pages
- banners
- preference center
page_order: 3
page_type: reference
description: "この参照記事では、メール、アプリ内メッセージ、ランディングページ、バナー、およびドラッグ＆ドロップメールユーザー設定センターのドラッグ＆ドロップエディターで使用できるエディターブロックについて説明します。"
tool: Media
---

# ドラッグ＆ドロップエディターブロック {#drag-and-drop-editor-blocks}

> エディターブロックは、ドラッグ＆ドロップエディターで行や列にドラッグするタイルです。

使用しているエディターを選択してください:

{% sdktabs %}

{% sdktab email %}
## メールエディターブロック {#email-editor-blocks}

エディターブロックは、メールメッセージの**コンテンツ**セクションにあります。**ドラッグ＆ドロップエディター**で列内にブロックをドラッグすると、列幅に自動調整されます。

**ドラッグ＆ドロップエディター**でのメール作成の詳細については、[ドラッグ＆ドロップでメールを作成する]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)および同記事の<a href="{{site.baseurl}}/user_guide/channels/email/drag_and_drop/#other-customizations">その他のカスタマイズ</a> を参照してください。

{% alert tip %}
`Image`、`Button`、または`Text`エディターブロック内の任意のURLに[カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes)を追加することもできます。
{% endalert %}

### タイトル {#title}

メール内のヘッダー用テキストを追加します。

| プロパティ | 説明 |
|---|---|
| タイトル | 見出しスタイルを選択します。 |
| フォントファミリー | タイトルのフォントスタイルです。 |
| フォントウェイト | フォントの全体的な太さです。 |
| フォントサイズ | テキストのサイズを決定します。 |
| テキストカラー | タイトルの色を変更します。 |
| リンクカラー | リンクの色を変更します。 |
| 配置 | タイトルを左揃え、中央揃え、または右揃えに移動します。 |
| 行の高さ | テキスト行間の距離を変更します。 |
| 文字間隔 | 各文字間の距離を変更します。 |
| テキスト方向 | デフォルトは左から右ですが、[右から左]({{site.baseurl}}/right_to_left_messages)に編集できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Title" }

### 段落 {#paragraph}

メッセージにテキストを入力します。ツールバーでフォントやテキストの編集機能を利用できます。

| プロパティ | 説明 |
|---|---|
| フォントファミリー | 段落テキストのフォントスタイルです。 |
| フォントウェイト | フォントの全体的な太さです。 |
| フォントサイズ | テキストのサイズを決定します。 |
| テキストカラー | テキストの色を変更します。 |
| リンクカラー | リンクの色を変更します。 |
| 配置 | テキストを左揃え、中央揃え、または右揃えに移動します。 |
| 段落間隔 | 段落間のスペースを変更します。 |
| 行の高さ | テキスト行間の距離を変更します。 |
| 文字間隔 | 各文字間の距離を変更します。 |
| テキスト方向 | デフォルトは左から右ですが、[右から左]({{site.baseurl}}/right_to_left_messages)に編集できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paragraph" }

### リスト {#list}

箇条書きリストを追加します。

| プロパティ | 説明 |
|---|---|
| リストタイプ | リストの種類です。箇条書きまたは番号付きのいずれかです。 |
| リストスタイルタイプ | リストのスタイルを決定します。 |
| リスト開始番号 | リストの開始番号を決定します。 |
| フォントファミリー | 段落テキストのフォントスタイルです。 |
| フォントウェイト | フォントの全体的な太さです。 |
| フォントサイズ | テキストのサイズを決定します。 |
| テキストカラー | テキストの色を変更します。 |
| リンクカラー | リンクの色を変更します。 |
| 配置 | テキストを左揃え、中央揃え、または右揃えに移動します。 |
| リスト項目間隔 | リスト項目間のスペースを変更します。 |
| リスト項目インデント | リスト項目のインデントを変更します。 |
| 行の高さ | テキスト行間の距離を変更します。 |
| 文字間隔 | 各文字間の距離を変更します。 |
| テキスト方向 | デフォルトは左から右ですが、[右から左]({{site.baseurl}}/right_to_left_messages)に編集できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="List" }

### ボタン {#button}

標準ボタンを追加します。プロパティでスタイルの編集やリンク動作の設定ができます。

| プロパティ | 説明 |
|---|---|
| ボタンオプション | フォント、サイズ、幅、色、パディングなど、さまざまなボタンオプションを設定します。 |
| ボタンホバー | マウスやトラックパッドでユーザーがボタンにカーソルを合わせたときのスタイルです。ボタンの背景色、フォント色、ボーダースタイルが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Button" }

#### クリック時の動作 {#on-click-behavior}

| プロパティ | 説明 |
|---|---|
| リンクタイプ | ボタンクリック時のアクションを決定し、適切なプロトコルを設定します。 |
| URL | **Webページを開く**リンクタイプに基づいて動的に変わります。 |
| メール宛先、件名、本文 | **メールを送信**リンクタイプの場合、ユーザーがボタンを選択したときに下書きメールに入力される受信者メールアドレス、件名、コンテンツを設定します。 |
| 電話番号 | **電話をかける**および**SMSを送信**リンクタイプの場合、ユーザーがボタンを選択したときに電話またはテキストする電話番号を設定します。 |
| メッセージ | **SMSを送信**リンクタイプの場合、ユーザーがボタンを選択したときにSMSメッセージの下書きに入力されるコンテンツを設定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="On-click behavior" }

### 区切り線 {#divider}

スペーシングに役立つ実線、点線、または破線を挿入します。

| プロパティ | 説明 |
|---|---|
| 透明 | 有効にすると、線と幅のオプションが削除されます。 |
| 線 | 点線、破線、実線などのさまざまな線の形式です。区切り線の太さと色も変更できます。 |
| 幅 | 5刻みで区切り線の広がりを調整します。 |
| 配置 | 線を左揃え、中央揃え、または右揃えに移動します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Divider" }

### スペーサー {#spacer}

他のブロック間にスペースやパディングを追加します。

| プロパティ | 説明 |
|---|---|
| 高さ | スペーサーブロックの高さを調整します。デフォルトは60pxです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spacer" }

### 画像 {#image}

[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)から画像を挿入します。ダイナミック画像（LiquidやConnected Contentを使用する画像）の場合、自動幅設定を使用するにはフォールバック画像を設定する必要があります。画像の仕様については、[メール画像の仕様]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#email)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| プロパティ | 説明 |
|---|---|
| 自動幅 | 画像の幅をピクセル単位で変更します。 |
| 配置 | ブロック内で画像の配置を左、中央、または右に設定します。 |
| Liquidを使用した画像 | [Liquid]({{site.baseurl}}/liquid)ロジックを使用して、同じコンテンツブロック内で異なる画像を動的に設定します。 |
| URL | 画像がホストされているアドレスを使用して画像を設定します。 |
| 代替テキスト | 画像と同じ情報をユーザーに提供する短い説明です。スクリーンリーダーのアクセシビリティや画像の読み込みに失敗した場合に不可欠です。 |
| 角丸画像 | 角丸で画像をレンダリングします。デフォルトでは、画像は角が四角でレンダリングされます。 |
| アクション | ユーザーが画像をクリックしたときにアクションをトリガーします。 |
| ブロックオプション | 画像ブロック周囲のパディングを設定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image" }

{% alert tip %}
**自動幅**の場合、自動画像リサイズは画像幅と利用可能なレイアウトスペースの組み合わせに基づいて最適なサイズを選択します:
- 利用可能なスペースより広い画像は100%幅に設定され、モバイルでもこの比率を維持し、デバイスの表示幅全体を使用します。
- 利用可能なスペースより小さい画像は、歪みやぼやけを避けるために画像の自然なサイズを使用します。
{% endalert %}

#### Gmailのダウンロードボタンの動作 {#gmail-download-button-behavior}

Gmailは、ハイパーリンク（`href`）が関連付けられていない画像にダウンロードボタンを自動的に追加します。ただし、画像のアスペクト比が299 x 524 px以下の場合、Gmailはダウンロードボタンを表示しません。

大きな画像にダウンロードボタンが表示されないようにするには、「#」リンクの回避策を適用できます:

1. **画像**ブロックを選択します。
2. **ブロックオプション**パネルで、**リンク**セクションに移動します。
3. **リンクタイプ**を**Webページを開く**に設定します。
4. **URL**入力フィールドにポンド記号（`#`）を入力します。

このリンクを追加すると、ユーザーエクスペリエンスに影響を与えることなく、Gmailがダウンロードボタンを表示するのを防ぎます。

### 動画 {#video}

動画コンテンツへのリンクを作成します。YouTubeとVimeoのみがサポートされています。

| プロパティ | 説明 |
|---|---|
| URL | 動画のURLです。 |
| タイトル | 動画のメタデータから自動生成されるか、カスタマイズできます。 |
| 再生アイコンスタイル | 動画画像の上部にある再生ボタンのさまざまなオプションが含まれます。 |
| 再生アイコンカラー | 再生ボタンに**ライト**または**ダーク**を選択するオプションです。 |
| 再生アイコンサイズ | 再生ボタンのピクセルサイズを選択します。50&nbsp;pxから80&nbsp;pxまでの事前定義された範囲（5&nbsp;px刻み）です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Video" }

{% alert tip %}
Vimeoでホストされている動画は、公開に設定されている場合にのみ機能します。Vimeo内で利用可能なその他のセキュリティ設定（例:「Vimeo.comから非表示」）は、このContent Blockでサポートされていない異なるリンク形式を生成します。これらのタイプのリンクはビルダーによって変更され、Brazeがサムネイルを生成できなくなります。
{% endalert %}

### ソーシャル {#social}

ソーシャルメディアプラットフォームのアイコンを挿入します。ブランド固有のアイコン用にカスタム画像をアップロードできます。

| プロパティ | 説明 |
|---|---|
| アイコンコレクションの選択 | アイコンコレクションのスタイルを設定します。 |
| アイコンコレクションの設定 | 各ソーシャルアイコンのURLを設定します。タイトルと代替テキストを編集するための**その他のオプション**トグルが含まれます。 |
| 配置 | ソーシャルアイコンを左揃え、中央揃え、または右揃えに移動します。 |
| アイコン間隔 | 各ソーシャルアイコン間の間隔を決定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Social" }

### アイコン {#icons}

アイコンを挿入します。カスタム画像をアップロードできます。Brazeは、画像をアップロードするまで大きめのプレースホルダーアイコンを使用します。

| プロパティ | 説明 |
|---|---|
| フォントファミリー | 段落テキストのフォントスタイルです。 |
| フォントウェイト | フォントの全体的な太さです。 |
| フォントサイズ | テキストのサイズを決定します。 |
| テキストカラー | タイトルの色を変更します。 |
| リンクカラー | リンクの色を変更します。 |
| 配置 | アイコンを左揃え、中央揃え、または右揃えに移動します。 |
| 文字間隔 | 各文字間の距離を変更します。 |
| アイコンサイズ | アイコンのサイズを決定します。 |
| アイコン間隔 | アイコンのスペースを変更します。 |
| アイコンパディング | アイコンのパディングを変更します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Icons" }

### HTML

生のHTMLを挿入します。Connected Contentや条件文などの[Liquid]({{site.baseurl}}/liquid)に推奨されます。

| プロパティ | 説明 |
|---|---|
| HTML | パーソナライゼーションや条件ロジック用の[Liquid]({{site.baseurl}}/liquid)を含む生のHTMLを追加または編集します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML" }

### メニュー {#menu}

デザイン中のメッセージ用に柔軟なメニューを作成します。

| プロパティ | 説明 |
|---|---|
| メニュー項目の設定 | メニュー項目を追加します。 |
| フォントファミリー | メニューのフォントスタイルです。 |
| フォントサイズ | メニューのサイズです。 |
| テキストカラー | メニューの色を変更します。 |
| リンクカラー | メニューテキストの色を変更します。 |
| 配置 | メニューを左揃え、中央揃え、または右揃えに移動します。 |
| 文字間隔 | 各文字間の距離を変更します。 |
| レイアウト | レイアウトを水平または垂直に決定します。 |
| セパレーター | メニューオプション間に文字を追加します。 |
| モバイルメニュー | モバイルデバイスで表示されるときのアイコンサイズ、色、アイコンタイプを変更するオプションが含まれます。 |
| 項目パディング | **+**または**-**ボタンを使用するか、特定の数値を入力してパディングを変更します。 |
| 全辺 | 項目パディングが無効の場合、一貫したパディング数値を設定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Menu" }

### 商品 {#product}

[商品カタログ]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks)から商品行をレンダリングします。カタログのセレクションからの静的アイテム（最大12件）、またはキャンバスの[eコマーストリガー]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases)（最大24件）によるダイナミック商品として表示できます。

| プロパティ | 説明 |
| --- | --- |
| コンテンツタイプ | 商品が固定カタログの**セレクション**（**静的**、最大12商品）から取得されるか、キャンバスのeコマースレコメンデーショントリガー（**ダイナミック**、最大24商品）から取得されるかを設定します。**ダイナミック**はキャンバスのメッセージステップでのみ利用可能です。 |
| カタログ | 商品データとフィールドマッピングを提供する商品カタログを選択します。 |
| セレクション | *（静的のみ）* 表示する商品を定義するカタログ上のフィルタリングされたセットを選択します。 |
| ソース詳細の表示 | 各商品フィールドにマッピングされている基盤のカタログまたはイベントフィールドを示すヘルプテキストを切り替えます。 |
| バリアント画像 | 各商品タイルのバリアント画像を表示または非表示にします。 |
| 商品タイトル | 各タイルの商品タイトルを表示または非表示にします。 |
| 価格 | 商品価格を表示または非表示にします。 |
| 商品URLボタン | 商品URLにリンクするコールトゥアクションボタンを表示または非表示にします。 |
| 数量 | *（ダイナミック、キャンバスのみ、エントリトリガーが商品閲覧イベントでない場合）* トリガーイベントからの商品数量を表示または非表示にします。 |
| 商品の向き | 各タイル内の画像位置を設定します: **画像左**、**画像中央**、または**画像右**。 |
| 配置 | 各タイル内のコンテンツの水平配置を設定します。 |
| 1行あたりの最大商品数 | 1行に表示する商品数を設定します: **1**、**2**、または**3**（**3**は向きが**画像中央**の場合のみ利用可能）。 |
| 商品間隔 | 商品間の間隔を設定します: **自動**または**カスタム**。 |
| カスタム間隔 | *（**カスタム**が選択された場合）* 商品間のギャップをピクセル単位で設定します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Product" }

## パーソナライゼーション {#personalization}

LiquidまたはConnected Contentを使用してメールにパーソナライゼーションを追加できます。

- **Liquid:** **コンテンツ** > **パーソナライゼーション**で属性を選択し、スニペットをコピーして、HTMLブロックに貼り付けます。基本的なLiquidスニペットはタイトル、段落、リストブロックでも動作する場合がありますが、これらのブロックにLiquidを配置すると予期しない動作やレイアウトの問題が発生する可能性があります。問題を避けるために、LiquidロジックにはHTMLブロックを使用してください。なお、Liquidは画像ブロックやボタンのURLフィールドではサポートされていません。
- **[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content):** **HTML**ブロックを追加し、そこに{% raw %}`{% connected_content %}`{% endraw %}コールを配置します。

{% endsdktab %}

{% sdktab in-app messages %}
## アプリ内メッセージエディターブロック {#in-app-message-editor-blocks}

エディターブロックは、アプリ内メッセージの**ビルド**セクションにあります。列にブロックをドラッグすると、列幅に自動調整されます。ブロックを選択すると、右側パネルで設定を編集できます。

**ドラッグ＆ドロップエディター**でのアプリ内メッセージ作成の詳細については、[ドラッグ＆ドロップでアプリ内メッセージを作成する]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)を参照してください。

### タイトルと段落 {#title-and-paragraph}

メッセージにタイトルまたは段落テキストを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### ボタン

スタイル、リンク、分析を設定可能な標準ボタンを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### ラジオボタン {#radio-button}

ユーザーが1つ選択できるオプションのリストを追加します。送信時、ユーザープロファイルに関連する[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)がログされます。保存するには文字列である必要があります。他のデータ型のカスタム属性はユーザープロファイルに保存されません。

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### 画像 {#image}

[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)から画像を挿入します。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

画像の仕様については、[アプリ内メッセージの画像仕様]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#in-app-messages)を参照してください。

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### リンク {#link}

ユーザーがクリックして指定されたURLに移動できるハイパーリンクを挿入します。テキスト内に埋め込むか、スタンドアロンで使用できます。

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### スペーサー {#spacer}

他のブロック間にスペースやパディングを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### カスタムコード {#custom-code}

高度なカスタマイズ用にカスタムHTML、CSS、またはJavaScriptを挿入します。

| プロパティ | 説明 |
| --- | --- |
| カスタムコード | アプリ内メッセージ用のHTML、CSS、JavaScriptを追加、編集、または削除できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

### 電話番号キャプチャ {#phone-capture}

電話番号用のフォームフィールドを挿入します。送信時、ユーザーは[SMS]({{site.baseurl}}/sms_rcs_subscription_groups)または[WhatsApp購読グループ]({{site.baseurl}}/whatsapp_subscription_groups)に購読されます。

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### メールキャプチャ {#email-capture}

メールアドレス用のフォームフィールドを挿入します。送信時、メールアドレスはBrazeのそのユーザーのプロファイルに追加されます。

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### ショートテキスト {#short-text}

標準属性（名前や姓など）またはカスタム属性文字列をサポートするフォームフィールドを挿入します。

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### ドロップダウン {#dropdown}

ユーザーが1つ選択できる事前定義された項目リストのドロップダウンを挿入します。リストにカスタム属性文字列を追加できます。

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### チェックボックス {#checkbox}

チェックボックスを挿入します。ユーザーがボックスにチェックを入れると、ブロックの[ブーリアンカスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)が`true`に設定されます。チェックされていない場合、属性は`false`に設定されます。

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### チェックボックスグループ {#checkbox-group}

ユーザーが複数の選択肢から選択できます。値は定義された[配列カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)に設定または追加されます。

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### ロングテキスト {#long-text}

アンケートスタイルのフロー用の複数行テキストフィールドです。このブロックが表示されない場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)またはBrazeのカスタマーサクセスマネージャーにお問い合わせください。

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row {#saved-row}

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## 知っておくべきこと {#things-to-know}

- **動画:** 標準コンポーザーには専用の動画ブロックは含まれていません。必要に応じて**カスタムコード**を使用してプレーヤーを埋め込んでください。詳細については、[アプリ内メッセージ: よくある質問]({{site.baseurl}}/user_guide/channels/in_app_messages/faq)を参照してください。

{% endsdktab %}

{% sdktab landing pages %}
## ランディングページエディターブロック {#landing-page-editor-blocks}

ランディングページのエディターブロックは、**ドラッグ＆ドロップエディター**の**ビルド**セクションの**行**とブロックカテゴリの下にあります。行の列にブロックをドラッグすると、列幅に自動調整されます。ブロックを選択すると、右側のプロパティパネルで設定を編集できます。

ランディングページの作成と公開の詳細については、[ランディングページを作成する]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)を参照してください。

### タイトルと段落

見出しまたは本文テキストを追加します。セクションの構造化や読みやすさの向上に役立ちます。

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### ボタン

リンクを開いたりフォームを送信したりするアクション用のクリック可能な要素を追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
**ボタンクリック時にフォームを送信**を設定し、新しいタブでWeb URLを開く場合、iOS Safariがナビゲーションをブロックする可能性があります。フォーム送信時は、送信後のURLを同じタブで開いてください。詳細については、[ランディングページを作成する]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)を参照してください。
{% endalert %}

### ラジオボタン

ユーザーが1つ選択できるオプションのリストを追加します。プロパティパネルを使用して、利用可能なオプションと選択された値を受け取るカスタム属性を設定します。フォーム送信時、ユーザープロファイルに選択された値が[文字列カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)としてログされます。他のデータ型のカスタム属性はユーザープロファイルに保存されません。

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### 画像

アップロードまたは外部URLから画像を表示します。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### リンク

ユーザーが選択してURLに移動できるハイパーリンクを追加します。テキスト内に配置するか、スタンドアロンで使用できます。

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### スペーサー

要素間に垂直方向のスペースを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### カスタムコード

[Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page)などの高度なカスタマイズ用にカスタムHTML、CSS、またはJavaScriptを挿入します。

| プロパティ | 説明 |
| --- | --- |
| カスタムコード | HTML、CSS、JavaScriptを追加、編集、または削除できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Countdown timer {#countdown-timer}

Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.
-->

### メールキャプチャ

メールアドレス用のフォームフィールドを追加します。送信時、アドレスはユーザーのBrazeプロファイルに保存されます。

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### 電話番号キャプチャ

電話番号用のフォームフィールドを追加します。送信時、選択した[SMS]({{site.baseurl}}/sms_rcs_subscription_groups)または[WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups)購読グループにユーザーを購読します。

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### 入力フィールド {#input-field}

標準属性（例: 名前や姓）またはカスタム属性文字列用のフォームフィールドを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### ドロップダウン

事前定義された項目リストで、ユーザーが1つ選択します。値をカスタム属性文字列にマッピングできます。

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### チェックボックス

チェックされると、ブロックの[ブーリアンカスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)を`true`に設定し、チェックされていない場合は`false`に設定します。

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### チェックボックスグループ

ユーザーが複数のオプションを選択できます。値は定義された[配列カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)に設定または追加されます。

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### 購読管理 {#manage-subscriptions}

訪問者がフォーム送信時に購読のオプトインや管理ができるよう、[メール購読グループ]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)のチェックリストを追加します。ブロックに購読グループを追加した後に設定します。このブロックはメール購読グループのみをサポートしており、SMS、RCS、またはWhatsApp購読グループはサポートしていません。

ランディングページの[Liquidタグ]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)を通じてページを開いた識別済みユーザーの場合、ブロックは各チェックボックスにユーザーの現在の購読状態を事前入力するため、ユーザー設定管理ページとしても機能します。

エディターでブロックを選択すると、以下の操作ができます:

- 購読グループの並べ替え
- 購読グループの追加または削除
- 説明の追加または削除
- ブロック内のすべての購読グループを選択する「すべて購読」チェックボックスの追加または削除

| プロパティ | 説明 |
| --- | --- |
| 購読グループ | ブロックに表示される購読グループを追加、削除、または並べ替えます。 |
| 説明を含める | 各購読グループの名前の横に説明を表示します。 |
| **すべて購読**チェックボックス | ブロック内のすべての購読グループを選択するチェックボックスを追加します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Manage subscriptions" }

完全な設定フローについては、[購読管理ブロック]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions)を参照してください。

### ロングテキスト

アンケートスタイルのフロー用の複数行テキストフィールドです。このブロックが表示されない場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)またはBrazeのカスタマーサクセスマネージャーにお問い合わせください。このブロックは標準ランディングページでは利用できません。

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## 知っておくべきこと

- **動画:** 標準コンポーザーには専用の動画ブロックは含まれていません。必要に応じて**カスタムコード**を使用してプレーヤーを埋め込んでください。詳細については、[ランディングページ]({{site.baseurl}}/user_guide/messaging/landing_pages)を参照してください。

{% endsdktab %}

{% sdktab banners %}
## バナーエディターブロック {#banner-editor-blocks}

バナーコンポーザーでは、**ビルド**セクションから行とブロックをキャンバスにドラッグしてメッセージをレイアウトします。**スタイル**を選択してページレベルのスタイルを調整するか、ブロックまたは行を選択してサイドパネルでプロパティを編集します。

バナー作成の完全なフローについては、[バナーを作成する]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner)を参照してください。

バナーコンポーザーは、他のドラッグ＆ドロップサーフェスと同じ種類のレイアウトブロックを提供しますが、完全なフォームブロックセット（例: ラジオボタン、ショートテキスト、ドロップダウン、チェックボックスブロック）は含まれていません。**電話番号キャプチャ**と**メールキャプチャ**ブロックを追加できます。メッセージごとに電話番号キャプチャとメールキャプチャは**それぞれ1つ**のみ許可されています。

### タイトルと段落

リッチテキストオプション付きの見出しまたは本文テキストを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### ボタン

クリック可能なボタンを追加します。プロパティパネルでリンクと分析オプションを設定できます。

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

詳細については、バナー記事の[クリック時の動作を定義する]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional)を参照してください。

### 画像

ホストされたURLから画像を表示します。プロパティパネルで表示オプションを設定します。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### リンク

ユーザーが選択できるハイパーリンクを挿入します。

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### クリック時の動作

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### スペーサー

ブロック間に垂直方向のスペースを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### カスタムコード

高度なレイアウトや埋め込みコンテンツ（例: 動画）用にカスタムHTMLを挿入します。カスタムHTML内のクリックは、`brazeBridge.logClick()`を呼び出さない限りトラッキングされません。詳細については、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/custom_code)を参照してください。

| プロパティ | 説明 |
| --- | --- |
| カスタムコード | バナー用のHTML（および関連アセット）を追加または編集します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom code" }

### 電話番号キャプチャ

電話番号を収集します。送信時、選択した[SMS]({{site.baseurl}}/sms_rcs_subscription_groups)または[WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups)購読グループにユーザーを購読します。バナーごとに1つのみです。

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### メールキャプチャ

メールアドレスを収集し、送信時にユーザーのBrazeプロファイルに追加します。バナーごとに1つのみです。

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### ロングテキスト

アンケートスタイルのフロー用の複数行テキストフィールドです。このブロックが表示されない場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)またはBrazeのカスタマーサクセスマネージャーにお問い合わせください。

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## 知っておくべきこと

- **動画:** 標準コンポーザーには専用の動画ブロックは含まれていません。必要に応じて**カスタムコード**を使用してプレーヤーを埋め込んでください。詳細については、[バナー: よくある質問]({{site.baseurl}}/user_guide/channels/banners/faq)を参照してください。
- **Liquid:** ほとんどのLiquidがサポートされていますが、カタログの再レンダリングタグなどの例外があります。詳細については、[バナー: よくある質問]({{site.baseurl}}/user_guide/channels/banners/faq)を参照してください。

{% endsdktab %}

{% sdktab preference center %}
## ユーザー設定センターエディターブロック {#preference-center-editor-blocks}

ドラッグ＆ドロップユーザー設定センターエディターの**ビルド**セクションから行にブロックをドラッグします。各ブロックには独自の設定があり、右側パネルは選択した要素のプロパティまたはスタイルに切り替わります。

ブロックを編集する前に、購読グループを追加し、購読**スマートブロック**を設定してください（次のセクションを参照）。完全な設定フローについては、[ドラッグ＆ドロップでメールユーザー設定センターを作成する]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center)を参照してください。

### タイトルと段落

リッチテキストオプション付きの見出しまたは本文コピーを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### ボタン

クリック可能なボタン（例: **保存**やナビゲーション）を追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### 画像

[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)またはURLから画像を表示します。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### スペーサー

ブロック間に垂直方向のスペースを追加します。

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### 購読グループ（スマートブロック） {#subscription-groups-smart-block}

購読グループ、オプションの**すべて購読**/**すべて購読解除**コントロール、および説明をリストするテンプレートブロックを追加します。ユーザー設定センターのワークフローでグループを追加した後に設定します。

[購読グループを追加]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-3-add-subscription-groups-to-the-preference-center)した後、キャンバスでスマートブロックを選択して以下を行います:

- 購読グループの並べ替え
- グループの追加または削除
- 説明の追加または削除
- そのブロック内のグループに対する**すべて購読**と**すべて購読解除**の切り替え

デフォルトテンプレートの下部にある**すべて購読解除**コントロールは必須であり、メールからの[グローバル購読解除]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)を実行します。

## 知っておくべきこと

- **共通スタイル:** 個々のブロックを調整する前に、**共通スタイル**でページ全体のデフォルトを設定できます。詳細については、[ドラッグ＆ドロップエディターを使用してユーザー設定センターをカスタマイズする]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-4-customize-the-preference-center-using-the-drag-and-drop-editor)を参照してください。
- **確認ページ:** エディター上部の**確認ページ**に切り替えて、同じブロックタイプを使用して保存後のエクスペリエンスをスタイルします。

{% endsdktab %}

{% endsdktabs %}