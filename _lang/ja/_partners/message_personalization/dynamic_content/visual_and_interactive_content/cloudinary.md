---
nav_title: Cloudinary
article_title: Cloudinary
description: "このリファレンス記事では、BrazeとCloudinaryの連携について説明します。"
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# Cloudinary

> [Cloudinary](https://www.cloudinary.com?utm_source=braze_partner_page)は、画像と動画の管理、編集、最適化、配信に使用される画像・動画プラットフォームで、チャネルやカスタマージャーニー全体にわたるあらゆるキャンペーンに対してスケーラブルに提供します。統合して有効にすると、Cloudinaryのメディア管理機能により、Brazeのキャンペーンやキャンバスに対してダイナミックで文脈に応じたパーソナライズ済みのアセット配信が可能になります。

## この連携について {#about-this-integration}

CloudinaryをBrazeに接続すると、Cloudinary Assetsに保存されているビジュアルメディアをBrazeのメッセージングチャネルで使用できるようになります。Cloudinaryのダイナミックリンクを使用すると、Brazeのユーザー属性に基づいてリアルタイムで画像や動画を選択・カスタマイズできます。CloudinaryとBrazeを組み合わせることで、各製品のストーリーを伝え、唯一無二の体験をスケーラブルに提供する、視覚的にリッチでパーソナライズされたキャンペーンの構築を支援します。

このページでは、CloudinaryとBrazeの間で可能な4つの連携方法について説明します（ただし、これらに限定されるものではありません）。これらの連携方法は、主にCloudinaryのメディアライブラリから手動でコピーしたアセットリンクの変更に依存しています。

{% alert important %}
[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)を使用してCloudinaryの[Admin API](https://cloudinary.com/documentation/admin_api#banner)を呼び出すなど、より高度な連携方法も可能ですが、アプローチは顧客ごとに異なります。詳しくは、CloudinaryおよびBrazeのカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件     | 説明 |
|-----------------------|-----------------|
| Cloudinaryアカウント  | この連携を利用するには、[Cloudinaryアカウント](https://cloudinary.com/users/register_free?utm_source=braze+docs+page)が必要です  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携方法 {#integration-methods}

{% alert tip %}
これらの連携方法の一部では、`f_auto`および`q_auto`のCloudinary Transformationsを使用します。これにより、[画像](https://cloudinary.com/documentation/image_transformations#banner)および[動画](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner)アセットの動作と外観をより詳細にカスタマイズできます。CloudinaryアセットリンクにTransformationsを含める方法の詳細については、[Transformation URL構造](https://cloudinary.com/documentation/image_transformations#transformation_url_structure)を参照してください。
{% endalert %}

{% tabs %}
{% tab Cloudinary DAM %}

## Cloudinary DAMからキャンペーンアセットを選択する {#select-campaign-assets-through-cloudinary-dam}

Brazeのキャンペーンやキャンバスで、CloudinaryのDAMから画像や動画を直接使用する最も簡単な方法は、Cloudinaryメディアライブラリの**アセット**ページからURLを取得することです。

![Cloudinaryの画像アセットライブラリのグリッドビュー。1つの画像がハイライトされ、「URLをコピー」ツールチップが表示されています。]({% image_buster /assets/img/cloudinary/one.png %})

### 画像とGIFの設定 {#images-and-gifs-setup}

1. CloudinaryのDAMから、**Assets** > **Media Library** > **Assets** > **Copy URL**に移動して、画像またはGIFのURLをコピーします。
2. HTMLで画像タグを作成し、コピーしたURLに`f_auto,q_auto`を追加して画像またはGIFを最適化します。

#### 画像URLの例 {#example-image-url}

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```
{% endraw %}

### 動画の設定 {#videos-setup}

1. CloudinaryのDAMから、**Assets** > **Media Library** > **Assets** > **Copy URL**に移動して、動画のリンクをコピーします。
2. HTMLで動画タグを作成し、コピーしたURLに`f_auto,q_auto`を追加して、動画のフォーマットと品質を自動的に最適化します。

#### 動画URLの例 {#example-video-url}

{% raw %}
```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```
{% endraw %}

AndroidおよびiOS固有の考慮事項については、[動画]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/video_in_custom_html)を参照してください。

{% endtab %}
{% tab 動画をGIFに変換 %}

## メール用に動画をGIFに変換する {#convert-videos-to-gifs-for-emails}

`f_auto:animated` [Cloudinary Transformation](https://cloudinary.com/documentation/image_transformations/)を使用して、動画アセットを自動的にGIFに変換します。これは、Brazeのメールチャネルを使用している場合に特に有用です。GIFはメールのペイロードを削減するために最適化されており、ペイロードが大きすぎると配信性の問題を引き起こす可能性があります。

### 変換の設定 {#conversion-setup}

1. Cloudinary DAMから動画URLをコピーします。
2. 画像タグを作成し、`f_auto:animated,fl_lossy`を追加してGIFサイズを縮小し、クライアントに最適なアニメーション形式を選択します。
3. `c_scale,w_nnn`を追加して、メールレイアウトで必要なGIF幅に対応します。
4. `e_loop`を追加してアニメーションをループさせます。

#### GIF URLの例 {#example-gif-url}

{% raw %}
```
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
{% endraw %}

{% endtab %}
{% tab ターゲット属性 %}

## ターゲティング属性に基づいてキャンペーンアセットを動的に選択する {#dynamically-select-campaign-assets-based-on-targeting-attributes}

この連携方法は、各ユーザーの属性に基づいてリアルタイムで最適なアセットをインテリジェントに選択することで、ダイナミックなメディアパーソナライゼーションを実現します。

Brazeのキャンペーンメッセージ内のCloudinaryリンクにLiquidタグをパラメータとして含めると、メッセージ送信時に関連するBraze属性がLiquidタグを動的に置き換えます。これには、言語や顧客ティアなどのユーザー固有のデータを使用できます。Cloudinaryはこれらの属性を使用して、そのユーザーに最も適したキャンペーンアセットを判断し、正しい画像または動画を自動的に返します。これにより、受信者は文脈に応じた関連性があり、ブランド承認済みのアセットのみを受け取ります。

### 仕組み {#how-it-works}

Cloudinaryは、[タグ](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags)および[構造化メタデータ（SMD）](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata)を使用してキャンペーンアセットを整理し、検索可能にします。

各キャンペーンアセットは、キャンペーンタグ（例：`spring_launch`）でグループ化され、`language=en`や`tier=gold`などのBraze属性に対応する構造化メタデータフィールドで拡張されます。BrazeがCloudinaryリンクを呼び出すと、[Custom Function](https://cloudinary.com/documentation/custom_functions#javascript_filters)が受信属性を処理し、一致するタグとメタデータを持つアセットを検索して、最適な一致を返します。

完全一致が見つからない場合は、すべてのエクスペリエンスで継続性を確保するために、フォールバックまたは「次善」のオプションが自動的に選択されます。アセットが選択されると、Cloudinaryのトランスフォーメーションレイヤー（例：`f_auto`や`q_auto`）が配信用にメディアを最適化します。このようにタグ付け、メタデータ、カスタムファンクションを組み合わせることで、開発者はパーソナライズされたアセット配信を自動化する柔軟なAPI駆動の方法を利用できます。

{% alert tip %}
カスタムファンクションの作成と適用の手順、および特定のキャンペーンのアセット選択とフォールバックオプションのカスタムファンクション例については、Cloudinaryの[`braze-personalization` GitHubリポジトリ](https://github.com/cloudinary-devs/braze-personalization)を参照してください。詳しいガイダンスについては、Cloudinaryサポートチームにお問い合わせください。
{% endalert %}

### 前提条件

ダイナミックなアセット選択を有効にするには、Cloudinaryがタグとメタデータに基づいてアセットのセットを返せる必要があります。リスト配信タイプが制限されている場合、Cloudinaryはキャンペーンでのパーソナライズされたアセット選択に必要なダイナミックリストを提供できません。
- リスト配信タイプの制限を解除します：Cloudinaryコンソールでセキュリティ設定を開き、制限画像タイプのリソースリスト項目をクリアします。

### ダイナミック選択の設定 {#dynamic-selection-setup}

1. Cloudinaryでアセットのタグとメタデータを設定します。
2. カスタムファンクションをCloudinary DAMにアップロードします。
3. 目的のタグのCloudinary URLを作成します。
4. タグURLをベースとして、ダイナミック画像Liquidタグを追加してBraze属性とカスタムファンクションを組み込みます。

#### URLの例 {#example-url}

この例では、Cloudinaryのアセットに、Braze属性に対応する期待値が入力された2つの定義済みSMDフィールド（「locale」と「audience」）があることを前提としています。また、キャンペーンに必要なアセットには「samples」タグが付与され、カスタムファンクション`segmentedBanner.js`がCloudinaryアカウントにアップロードされています。

{% raw %}
```bash

// Use the appropriate Braze attributes.
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %}
{% assign locale = {{${language}}}%}

// The URL for the "samples" tag used in the campaign is https://solutions-demo-res.cloudinary.com/image/list/v1690000000/samples.json, which is the base for the dynamic image URL.
<img src="https://solutions-demo-res.cloudinary.com/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner">
```
{% endraw %}

##### 出力URL {#output-urls}

- オーディエンスが`internal`でロケールが`en`のユーザーの出力URL：
```
https://solutions-demo-res.cloudinary.com/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- オーディエンスが`external`でロケールが`es`のユーザーの出力URL：
```
https://solutions-demo-res.cloudinary.com/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- フォールバック画像URL：
```
https://solutions-demo-res.cloudinary.com/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```

{% endtab %}
{% tab パーソナライズ画像の生成 %}

## パーソナライズ画像の生成 {#personalized-image-generation}

Cloudinaryの[テキストオーバーレイトランスフォーメーション](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos/)は、Cloudinaryアセット内でBrazeのユーザーデータを直接使用します。

以下の例では、`l_text`トランスフォーメーションを使用してユーザーの名前をアセットに挿入する方法を示しています。キャンペーンやキャンバスを開発する際にLiquidタグを活用して、`l_text`パラメータに入力するテキストを決定することで、さらなるカスタマイズが可能です。

トランスフォーメーションパラメータを使用してアセットをデザインする方法の詳細については、Cloudinaryサポートチームにお問い合わせください。

### `l_text`トランスフォーメーションの例 {#example-l_text-transformation}

{% raw %}
```bash
{% assign first_name = {{${first_name}}}%}
{% assign second_name = {{${last_name}}}%}

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

#### 出力URLの例 {#example-output-url}

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

![海を見下ろす青い屋根の白い教会。画像の上に半透明の暗い長方形があり、その中に「John Smith」という文字が表示されています。]({% image_buster /assets/img/cloudinary/two.png %})

```
{% endtab %}
{% endtabs %}