---
nav_title: クリエイティブの詳細
article_title: コンテンツカードのクリエイティブの詳細
page_order: 2
description: "この記事では、3つの標準コンテンツカードタイプにおける画像サイズの推奨事項や非表示の動作などのクリエイティブの詳細について説明します。"
channel:
  - content cards
tool: Media

---

# コンテンツカードのクリエイティブの詳細 {#creative-details-for-content-cards}

> Content Cardsとそれが配置されるフィードのカスタマイズは、キャンペーン作成プロセス中には行えません。エンジニアや開発者と協力して、カードの構築とカスタマイズを行う必要があります。技術的な詳細については、[開発者ドキュメント]({{site.baseurl}}/developer_guide/getting_started/customization_overview)をご覧ください。

## Content Cardsの種類 {#content-card-types}

{% tabs %}
{% tab クラシック %}

クラシックカードは、標準的なメッセージングや通知、またはアイコンでメッセージを視覚的に分類するのに最適です。画像はオプションですが、1:1の比率にする必要があります。

![クラシックカードの推奨詳細とクラシックカードの例を示す画像]({% image_buster /assets/img/content_card_classic.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| カードの機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px、太字 <br> 1行のテキストが理想的です。<br> Liquidを使用してメッセージをパーソナライズできます。 |
| メッセージテキスト | 13px、標準ウェイト <br> 2〜4行のテキストが理想的です。<br> Liquidを使用してメッセージをパーソナライズできます。 |
| リンクテキスト | オプション。<br> 13&nbsp;px <br> Webページへのリンクまたはアプリ内へのディープリンク。 |
| 画像 | オプション。<br> 1:1の比率にする必要があります。<br> 60 x 60&nbsp;pxの画像品質を推奨します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cardsの種類" }

{% endtab %}
{% tab キャプション付き画像 %}

キャプション付き画像カードは、大型セールや新しいアプリ機能など、重要なコンテンツをアピールして注目を集めるのに最適な方法です。

![キャプション付き画像カードの推奨詳細とキャプション付き画像カードの例を示す画像]({% image_buster /assets/img/content_card_captioned.png %}){: width="2880" height="2877" style="max-width:90%;border:0;"}

| カードの機能 | 詳細 |
| --- | ---|
| ヘッダーテキスト | 18px、太字 <br> 1行のテキストが理想的です。<br> Liquidを使用してメッセージをパーソナライズできます。 |
| メッセージテキスト | 13px、標準ウェイト <br> 2〜4行のテキストが理想的です。<br> Liquidを使用してメッセージをパーソナライズできます。 |
| リンクテキスト | オプション。<br> 13&nbsp;px <br> Webページへのリンクまたはアプリ内へのディープリンク。 |
| 画像 | 4:3の比率を推奨します。<br> 最小幅600&nbsp;px。<br> 高解像度のPNG、JPEG、GIFをサポートしています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cardsの種類" }

{% endtab %}
{% tab 画像のみ %}

よりクリエイティブなコントロールが必要な場合は、画像のみのカードが最適です。お好みのツールを使用して画像を作成し、このカードタイプにアップロードしてください。

![画像のみのContent Cardの推奨詳細と画像のみの例を示す画像]({% image_buster /assets/img/content_card_banner.png %}){: width="1358" height="2871" style="max-width:45%;border:0;"}

| カードの機能 | 詳細 |
| --- | ---|
| リンク付きカード | オプション。<br> 13&nbsp;px <br> クリック時にWebページへのリンクまたはアプリ内へのディープリンクを開きます。 |
| 画像 | 任意のアスペクト比をサポートしています。<br> 最小幅600&nbsp;px。<br> 高解像度のPNG、JPEG、GIFをサポートしています。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content Cardsの種類" }

{% endtab %}
{% endtabs %}

## グローバルクリエイティブの詳細 {#general}

Content Cardsは、テキストと画像（GIFを含む）をデフォルトでサポートしています。現時点では、異なるフォントカラーや複数の画像など、カードのカスタムスタイリングはダッシュボードでは行えません。インテグレーション時にContent Cardsとフィードのカスタムスタイリングを行うことができます。詳細については、Braze SDKの[カードのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards)を参照してください。

### 非表示の動作 {#dismissal-behavior}

ユーザーがカードを非表示にするには、モバイルでスワイプするか、以下のスクリーンショットに示すように`close X`機能を使用します。`x`はWeb SDKの場合のみ、ホバー時に表示されます。

![カードのスワイプまたは閉じるによる非表示の動作を示す画像]({% image_buster /assets/img/dismissal-cc.png %}){: width="1800" height="504"}

ユーザーがすべてのカードを非表示にした場合、または新しい更新をプッシュしていない場合、ユーザーのフィードは通常次のように表示されます。

![空のContent Cardsフィードの画像]({% image_buster /assets/img/empty-cc.png %}){: width="832" height="1478" style="max-width:45%"}

{% alert tip %}
ユーザーが関連するアクションを実行した際に非表示になるように設定して、Content Cardsの関連性を保ちましょう。例えば、プロモーション用のContent Cardsは、ユーザーが購入した時点で非表示になるように設定することで、すでに購入した商品のオファーが引き続き表示されるのを防ぐことができます。
{% endalert %}

### Content CardsでのGIFの使用 {#using-gifs-in-content-cards}

| Android向けContent Cards | iOS向けContent Cards | Web向けContent Cards |
| --- | --- |---|
| Android SDKはデフォルトではアニメーションGIFをサポートしていません。GIFサポートの有効化の詳細については、[GIF]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs?sdktab=android)を参照してください。 | Swift SDKはデフォルトではアニメーションGIFをサポートしていません。GIFサポートの有効化の詳細については、[GIFサポートチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)を参照してください。 | GIFサポートはWeb SDKインテグレーションにデフォルトで含まれています。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Content CardsでのGIFの使用" }