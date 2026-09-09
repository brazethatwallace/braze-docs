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

**メッセージスタイル**タブから、アプリ内メッセージ内のすべての関連ブロックに適用されるスタイルを設定できます。例えば、メッセージ内のすべてのテキストのフォントやすべてのリンクの色をカスタマイズしたい場合などに利用します。

このセクションのスタイルは、特定のブロックでオーバーライドする場合を除き、メッセージ全体で使用されます。メッセージに[複数のページ]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop#multi-page)がある場合、表示タイプと最大幅を除き、個々のページに対してメッセージレベルのスタイルをオーバーライドすることもできます。

デザイン作業をスムーズに進めるために、ブロックレベルのスタイルをカスタマイズする前に、メッセージレベルのスタイルを設定することをお勧めします。

**メッセージスタイル**タブにいつでも戻るには、以下のいずれかを行います。

- 個々のブロックプロパティの閉じる X ボタンをクリックする
- メッセージコンテナ、メッセージの閉じる X ボタン、またはエディターの背景を選択する

### カスタムフォント {#custom-fonts}

フォントのファイル形式は`.ttf`、`.woff`、`.otf`、`.woff2`に対応しています。詳しくは、[アセットファイル]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#asset-files)を参照してください。

フォントファミリーの複数のバリエーションを追加できます。一部のスタイルオプションはカスタムフォントでは利用できない場合があります。現在、URLによるフォントの追加はサポートしていません。

カスタムフォントを追加するには:

1. **メッセージスタイル**タブの**コンテンツ**セクションに移動します。
2. **カスタムフォントを追加**をクリックします。
3. メディアライブラリを使用してフォントをアップロードします。

{% alert note %}
メッセージレベルのフォントは、現在のメッセージとその複製メッセージにのみ適用され、将来のテンプレートには適用されません。
{% endalert %}

## メッセージコンポーネント {#message-components}

![プロモーション用アプリ内メッセージを作成する様子を示すGIF。]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

ドラッグ＆ドロップエディターは、アプリ内メッセージを構成するために2つの主要コンポーネントを使用します。**行**と**ブロック**です。すべてのブロックは行の中に配置する必要があります。

### 閉じる（×）ボタン {#close-x-button}

モーダルおよびフルスクリーンのアプリ内メッセージでは、メッセージ上部に <i class="fa-solid fa-xmark"></i> として表示される閉じるボタンをカスタマイズできます。カスタマイズオプションには、ボタンの位置、サイズ、塗りつぶしの色、背景色、枠線スタイル、枠線の角丸が含まれます。

![アプリ内メッセージの閉じる（×）ボタンをカスタマイズするオプション。ボタンサイズ、塗りつぶしの色、背景色、枠線スタイル、枠線の角丸が含まれます。]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### スパンスタイリング {#span-styling}

アプリ内メッセージのテキストにスパンスタイリングを追加すると、メッセージの外観をさらにカスタマイズでき、異なるテキストの色、フォント、サイズを使用できるようになります。スパンスタイリングにより、重要な情報にユーザーの注意を引きつけ、メッセージ全体の明瞭さを向上させることで、より魅力的で視覚的に優れたエクスペリエンスを提供できます。

![アプリ内メッセージでテキストをハイライトしたときに表示されるオプション。小さなペイントブラシアイコンが表示され、スタイルを適用するためにスパンで囲むことができます。]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

![「スパンプロパティ」のサイドパネル。フォントファミリー、フォントの太さ、フォントサイズ、文字間隔、テキストの色をカスタマイズできます。]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### 行 {#rows}

行は、セルを使用してメッセージのセクションの水平方向の構成を定義する構造単位です。

![アプリ内メッセージに追加できる行。]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

行を選択すると、**列のカスタマイズ**セクションから必要な列の数を追加または削除して、異なるコンテンツ要素を横並びに配置できます。

また、スライドして既存の列のサイズを調整することもできます。

![「列のカスタマイズ」セクションから列を調整する様子。]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

ベストプラクティスとして、行内のブロックをフォーマットする前に、行と列のプロパティをフォーマットしてください。スペーシングと配置を調整できる箇所は多数あるため、基盤から始めることで編集が容易になります。

#### 背景画像 {#background-image}

**行のプロパティ**パネルで行に背景画像を追加できます。**背景画像**をオンに切り替え、画像URLを入力するか、[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)から画像を選択します。最後に、代替テキスト、サイズ、位置、行全体にパターンを作成するために画像を繰り返すかどうかを設定します。

![ピザの行背景画像。水平方向のリピートパターンが適用されています。]({% image_buster /assets/img_archive/background_row.png %})

### ブロック {#blocks}

ブロックは、メッセージで使用できるさまざまな種類のコンテンツを表します。既存の行セグメント内にドラッグすると、セルの幅に自動的に調整されます。

{% alert tip %}
ブロックを追加する前に、メッセージコンテナ、フォント、色、その他カスタマイズしたい要素の[メッセージレベルのスタイル](#set-message-level-styles)を設定してください。その後、必要に応じて個々のブロックをカスタマイズできます。**閉じるボタン**はメッセージの上部セクションに常に表示されるため、ユーザーはいつでもメッセージを閉じることができます。
{% endalert %}

![選択可能なドラッグ＆ドロップのボックス。]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

すべてのブロックには、パディングの詳細な制御などの独自の設定があります。右側のパネルは、選択されたコンテンツ要素のスタイリングパネルに自動的に切り替わります。詳細については、[エディターブロックのプロパティ]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages#inappmessages_properties)を参照してください。

アプリ内メッセージを作成する際、ツールバーでモバイル、タブレット、またはデスクトップビューを選択して、ユーザーグループに対してアプリ内メッセージがどのように表示されるかをプレビューできます。これにより、コンテンツがレスポンシブであることを確認し、必要な調整を随時行うことができます。

## クリエイティブの詳細 {#creative-details}

### 大画面でのフルスクリーン {#fullscreen}

タブレットやデスクトップブラウザでは、フルスクリーンのアプリ内メッセージはアプリ画面の中央に表示されます。フルスクリーンメッセージの最大幅に対する編集は、タブレットおよびデスクトップデバイスにのみ適用されます。

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

ユーザーデータ（カスタム属性やユーザープロパティなど）に基づいてバックグラウンド画像を動的に切り替えるには、Liquid {% raw %}`{% capture %}`{% endraw %}ブロックを使用して、HTMLとCSSが読み込まれる前に正しい画像URLを変数に割り当てます。

Liquidロジックをメッセージの先頭に配置し、キャプチャした変数をバックグラウンド画像のURLフィールドで参照します。これにより、各ユーザーのデータに基づいて正しい画像が選択されます。

画像URLをキャプチャした後、{% raw %}`{{ image_url | strip }}`{% endraw %}を使用して、余分な空白を除去したURLを出力します。このLiquidをバックグラウンド画像のURLフィールドに貼り付けることで、ユーザーごとに異なる画像を動的に表示できます。

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

アプリ内メッセージに[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を追加するには、エディターツールバーから<i class="fa-solid fa-circle-plus"></i>**パーソナライゼーションを追加**を選択します。ここでは、デフォルト属性、デバイス属性、カスタム属性など、さまざまなパーソナライゼーションタイプを追加できます。

次に、生成されたLiquidスニペットをメッセージに挿入します。アプリ内メッセージのデザインと構築が完了したら、**プレビューとテスト**に移動してメッセージをプレビューします。

### AIコピーライターを使用する {#use-the-ai-copywriter}

アプリ内メッセージでテキストブロックが選択されている場合、ブロックツールバーの<i class="fa-solid fa-wand-magic-sparkles" title="AIコピーライター"></i>**AIコピーライター**を選択して、[AI搭載コピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy)を起動します。AIコピーライティングアシスタントは、簡単な商品名や説明をOpenAIのGPT3コピー生成ツールに渡し、メッセージング向けの人間らしいマーケティングコピーを生成します。

{% alert tip %}
ブロック内のテキストをハイライトしてからアイコンをクリックすると、数回のクリックを省略できます。ハイライトされたテキストがツールに追加され、すぐにコピーが生成されます。
{% endalert %}

![AIコピーライターのGIF。]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### スタイルをデフォルトにリセットする {#reset-styles-to-default}

デフォルトのスタイルから変更したプロパティには、オレンジ色のドットが表示されます。特定のプロパティをデフォルトスタイルにリセットするには、フィールドにカーソルを合わせて**デフォルトにリセット**を選択します。

![テキストサイズをデフォルトサイズにリセットするオレンジ色のドット。]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

また、プロパティパネル名の横にある<i class="fas fa-paintbrush" title="スタイルのコピーまたは貼り付けボタン"></i>を選択し、**デフォルトスタイルにリセット**を選択することで、選択した要素のすべてのスタイルをリセットすることもできます。

### スタイルのコピーと貼り付け {#copy-and-paste-styles}

要素のスタイルを変更した後、それらのスタイルを別の要素にコピーして貼り付けることができます。スタイルを貼り付ける際は、その要素に関連するプロパティのみが適用されます。

![スタイルをコピーするオプションのドロップダウンメニュー。]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. 要素を選択した状態で、プロパティパネル名の横にある<i class="fas fa-paintbrush" title="スタイルのコピーまたは貼り付け"></i>**スタイルのコピーまたは貼り付け**を選択します（例えば、ボタンが選択されている場合は「ボタンのプロパティ」の横）。
2. **スタイルをコピー**をクリックし、コピーしたスタイルを適用したい要素を選択します。
3. <i class="fas fa-paintbrush" title="スタイルのコピーまたは貼り付け"></i>**スタイルのコピーまたは貼り付け**を再度選択し、**スタイルを貼り付け**を選択します。

#### キーボードショートカット {#keyboard-shortcuts}

キーボードショートカットを使用してスタイルのコピーと貼り付けを行うこともできます。

| アクション | Mac | Windows |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| スタイルをコピー | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| スタイルを貼り付け | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="キーボードショートカット" }