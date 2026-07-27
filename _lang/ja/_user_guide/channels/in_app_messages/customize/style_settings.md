---
nav_title: スタイル設定
article_title: "アプリ内メッセージのスタイル設定"
description: "このリファレンス記事では、ドラッグ＆ドロップエディターでアプリ内メッセージを作成する際に利用できるスタイルオプションについて説明します。"
page_order: 1
---

# アプリ内メッセージのスタイル設定 {#in-app-message-style-settings}

> ドラッグ＆ドロップの編集エクスペリエンスは、**ビルド**と**プレビュー＆テスト**の2つのセクションに分かれています。この記事では、エディターの**ビルド**タブでの作業に必要な情報を説明します。すでに[アプリ内メッセージを作成]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)していることを前提としています。

![「メッセージスタイル」タブ。]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## メッセージレベルのスタイル {#message-level-styles}

**メッセージスタイル**タブから、アプリ内メッセージ内のすべての関連ブロックに適用されるスタイルを設定できます。たとえば、メッセージ内のすべてのテキストのフォントやすべてのリンクの色をカスタマイズしたい場合に使用します。

このセクションのスタイルは、特定のブロックでオーバーライドしない限り、メッセージ全体で使用されます。メッセージに[複数のページ]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page)がある場合、表示タイプと最大幅を除き、個々のページのメッセージレベルのスタイルをオーバーライドすることもできます。

デザインをスムーズに進めるために、ブロックレベルのスタイルをカスタマイズする前に、メッセージレベルのスタイルを設定することをお勧めします。

**メッセージスタイル**タブにいつでも戻るには:

- 個々のブロックプロパティの閉じる X ボタンをクリックします
- メッセージコンテナ、メッセージの閉じる X ボタン、またはエディターの背景を選択します

### カスタムフォント {#custom-fonts}

フォントのファイルタイプは `.ttf`、`.woff`、`.otf`、`.woff2` に対応しています。詳細については、[アセットファイル]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#asset-files)を参照してください。

フォントファミリーの複数のバリエーションを追加できます。カスタムフォントでは一部のスタイルオプションが利用できない場合があります。現在、URL 経由でのフォント追加はサポートしていません。

カスタムフォントを追加するには:

1. **メッセージスタイル**タブの**コンテンツ**セクションに移動します。
2. **カスタムフォントを追加**をクリックします。
3. メディアライブラリを使用してフォントをアップロードします。

{% alert note %}
メッセージレベルのフォントは、現在のメッセージと複製されたメッセージにのみ適用され、今後のテンプレートには適用されません。
{% endalert %}

## メッセージコンポーネント {#message-components}

![プロモーション用アプリ内メッセージの作成過程を示すGIF。]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

ドラッグ＆ドロップエディターでは、アプリ内メッセージの作成に2つの主要コンポーネントを使用します。**行**と**ブロック**です。すべてのブロックは行の中に配置する必要があります。

### 閉じる（×）ボタン {#close-x-button}

モーダルおよびフルスクリーンのアプリ内メッセージでは、メッセージ上部に表示される<i class="fa-solid fa-xmark"></i>の閉じるボタンをカスタマイズできます。カスタマイズオプションには、ボタンの位置、サイズ、塗りつぶしの色、背景色、ボーダースタイル、ボーダーの角丸があります。

![アプリ内メッセージの閉じる（×）ボタンをカスタマイズするオプション。ボタンサイズ、塗りつぶしの色、背景色、ボーダースタイル、ボーダーの角丸が含まれます。]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### スパンスタイリング {#span-styling}

アプリ内メッセージのテキストにスパンスタイリングを追加すると、メッセージの外観をさらにカスタマイズでき、異なるテキストカラー、フォント、サイズを使用できるようになります。スパンスタイリングにより、重要な情報にユーザーの注意を引き、メッセージ全体の明瞭性を向上させることで、より魅力的で視覚的に訴求力のある体験を提供できます。

![アプリ内メッセージでテキストをハイライトしたときに表示されるオプション。小さなペイントブラシアイコンが表示され、スタイル用のスパンで囲むことができます。]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

![「スパンプロパティ」のサイドパネル。フォントファミリー、フォントウェイト、フォントサイズ、文字間隔、テキストカラーをカスタマイズできます。]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### 行 {#rows}

行は、セルを使用してメッセージのセクションの水平方向の構成を定義する構造単位です。

![アプリ内メッセージに追加できる行。]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

行を選択すると、**列のカスタマイズ**セクションから必要な列数を追加または削除して、異なるコンテンツ要素を横に並べて配置できます。

また、スライドして既存の列のサイズを調整することもできます。

![「列のカスタマイズ」セクションから列を調整する様子。]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

ベストプラクティスとして、行内のブロックをフォーマットする前に、行と列のプロパティをフォーマットしてください。スペーシングや配置を調整できる箇所は多数あるため、基盤から始めることで、作業を進めながら編集しやすくなります。

#### 背景画像 {#background-image}

**行プロパティ**パネルで行に背景画像を追加できます。**背景画像**をオンに切り替え、画像URLを入力するか、[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)から画像を選択します。最後に、代替テキスト、サイズ、位置、および行全体にパターンを作成するために画像を繰り返すかどうかを設定します。

![ピザの行背景画像。水平方向の繰り返しパターンが適用されています。]({% image_buster /assets/img_archive/background_row.png %})

### ブロック {#blocks}

ブロックは、メッセージで使用できるさまざまな種類のコンテンツを表します。既存の行セグメント内にドラッグすると、セルの幅に自動的に調整されます。

{% alert tip %}
ブロックを追加する前に、メッセージコンテナ、フォント、色、その他カスタマイズしたい要素の[メッセージレベルのスタイル](#set-message-level-styles)を設定してください。その後、必要に応じて個々のブロックをカスタマイズできます。**閉じるボタン**はメッセージの上部セクションに常に表示されるため、ユーザーはいつでもメッセージを閉じることができます。
{% endalert %}

![選択可能なドラッグ＆ドロップボックス。]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

各ブロックには、パディングの細かいコントロールなど、独自の設定があります。右側のパネルは、選択したコンテンツ要素のスタイリングパネルに自動的に切り替わります。詳細については、[エディターブロックのプロパティ]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages#inappmessages_properties)を参照してください。

アプリ内メッセージを作成する際、ツールバーでモバイル、タブレット、またはデスクトップビューを選択して、ユーザーグループに対してアプリ内メッセージがどのように表示されるかをプレビューできます。これにより、コンテンツがレスポンシブであることを確認し、必要な調整を随時行うことができます。

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='in_app_message' %}

## クリエイティブの詳細 {#creative-details}

### 大きな画面でのフルスクリーン {#fullscreen}

タブレットやデスクトップブラウザでは、フルスクリーンのアプリ内メッセージはアプリ画面の中央に表示されます。フルスクリーンメッセージの最大幅の編集は、タブレットおよびデスクトップデバイスにのみ適用されます。

![フルスクリーンのアプリ内メッセージの例。]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### バックグラウンド画像を追加する {#add-a-background-image}

**メッセージスタイル**タブから、メッセージのバックグラウンドに画像を追加できます。

1. キャンバスエリアで、バックグラウンドコンテナを選択します。これはメッセージのスクロール可能なセクションです。
2. **メッセージスタイル**タブで、**バックグラウンド画像**をオンにします。
3. メディアライブラリから画像を追加するか、画像がホストされているURLを入力します。

{% alert tip %}
特定のブロックの選択が難しい場合は、ブロックのインラインツールバーの上矢印を使用して、各親ブロックにフォーカスを移動できます。
{% endalert %}

#### Liquidでバックグラウンド画像を動的に切り替える {#swap-background-images-with-liquid}

ユーザーデータ（カスタム属性やユーザープロパティなど）に基づいてバックグラウンド画像を動的に切り替えるには、Liquid {% raw %}`{% capture %}`{% endraw %} ブロックを使用して、HTMLとCSSが読み込まれる前に正しい画像URLを変数に割り当てます。

Liquidロジックをメッセージの先頭に配置し、キャプチャした変数をバックグラウンド画像URLフィールドで参照します。これにより、各ユーザーのデータに基づいて正しい画像が選択されます。

画像URLをキャプチャした後、{% raw %}`{{ image_url | strip }}`{% endraw %} を使用して、余分な空白を除去したURLを出力します。このLiquidをバックグラウンド画像URLフィールドに貼り付けることで、異なるユーザーに異なる画像を動的に表示できます。

##### 例 {#example}

{% raw %}
```liquid
{% capture image_url %}
{% if {{custom_attribute.${membership_tier}}} == 'gold' %}
https://example.com/images/gold-background.png
{% elsif {{custom_attribute.${membership_tier}}} == 'silver' %}
https://example.com/images/silver-background.png
{% else %}
https://example.com/images/default-background.png
{% endif %}
{% endcapture %}
{{ image_url | strip }}
```
{% endraw %}

### Liquidを追加する {#add-liquid}

![Liquidパーソナライゼーションを追加するアイコン。]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

アプリ内メッセージに[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を追加するには、エディターツールバーから<i class="fa-solid fa-circle-plus"></i> **パーソナライゼーションを追加**を選択します。ここでは、デフォルト属性、デバイス属性、カスタム属性など、さまざまなパーソナライゼーションタイプを追加できます。

次に、生成されたLiquidスニペットをメッセージに挿入します。アプリ内メッセージのデザインと構築が完了したら、**プレビューとテスト**に移動してメッセージをプレビューします。

### AIコピーライターを使用する {#use-the-ai-copywriter}

アプリ内メッセージでテキストブロックが選択されている状態で、ブロックツールバーの<i class="fa-solid fa-wand-magic-sparkles" title="AIコピーライター"></i> **AIコピーライター**を選択して、[AI搭載コピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)を起動します。AIコピーライティングアシスタントは、簡単な製品名や説明をOpenAIのGPT3コピー生成ツールに渡し、メッセージング用の人間らしいマーケティングコピーを生成します。

{% alert tip %}
ブロック内のテキストをハイライトしてからアイコンをクリックすると、数クリック分の手間を省けます。ハイライトされたテキストがツールに追加され、すぐにコピーが生成されます。
{% endalert %}

![AIコピーライターのGIF。]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### スタイルをデフォルトにリセットする {#reset-styles-to-default}

デフォルトのスタイルから変更したプロパティには、オレンジ色のドットが表示されます。特定のプロパティをデフォルトのスタイルにリセットするには、フィールドにカーソルを合わせて**デフォルトにリセット**を選択します。

![テキストサイズをデフォルトサイズにリセットするオレンジ色のドット。]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

また、プロパティパネル名の横にある<i class="fas fa-paintbrush" title="スタイルのコピーまたは貼り付けボタン"></i>を選択し、**デフォルトスタイルにリセット**を選択することで、選択した要素のすべてのスタイルをリセットすることもできます。

### スタイルのコピーと貼り付け {#copy-and-paste-styles}

要素のスタイルを変更した後、そのスタイルを別の要素にコピーして貼り付けることができます。スタイルを貼り付ける際は、その要素に関連するプロパティのみが適用されます。

![スタイルをコピーするオプションのあるドロップダウンメニュー。]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. 要素を選択した状態で、プロパティパネル名の横にある<i class="fas fa-paintbrush" title="スタイルのコピーまたは貼り付け"></i> **スタイルのコピーまたは貼り付け**を選択します（例えば、ボタンを選択している場合は「ボタンプロパティ」の横）。
2. **スタイルをコピー**をクリックし、コピーしたスタイルを適用したい要素を選択します。
3. <i class="fas fa-paintbrush" title="スタイルのコピーまたは貼り付け"></i> **スタイルのコピーまたは貼り付け**を再度選択し、**スタイルを貼り付け**を選択します。

#### キーボードショートカット {#keyboard-shortcuts}

キーボードショートカットを使用してスタイルのコピーと貼り付けを行うこともできます。

| アクション | Mac | Windows |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| スタイルをコピー | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| スタイルを貼り付け | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="キーボードショートカット" }