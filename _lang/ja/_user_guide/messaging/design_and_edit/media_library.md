---
nav_title: メディアライブラリ
article_title: メディアライブラリ
page_order: 2
page_type: reference
description: "このリファレンス記事では、メディアライブラリについて説明します。アセットを一元管理する方法、AIを使用して画像を生成する方法、メッセージ作成画面でメディアにアクセスする方法について学ぶことができます。"
tool: Media

---

# メディアライブラリ {#media-library}

> メディアライブラリを使用すると、アセットを一元管理された場所で管理できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| 「View Media Library Assets」権限 | メディアライブラリのアセットを表示します |
| 「Edit Media Library Assets」権限 | メディアライブラリのアセットを作成および更新します |
| 「Delete Media Library Assets」権限 | UIからメディアライブラリのアセットを削除します。削除されたアセットは、それを参照しているメッセージが壊れないよう、Brazeによって引き続きホスティングされます。アセットを完全に削除するには、Brazeサポートにお問い合わせください。 |
| 「Replace Media Library Assets」権限 | 既存のメディアライブラリアセットのファイルを、URLとアセットIDを維持したまま置き換えます |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メディアライブラリの権限" }

詳細については、[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)を参照してください。

## メディアライブラリとCDNの比較 {#media-library-versus-cdn}

コンテンツデリバリーネットワーク（CDN）の代わりにメディアライブラリを使用すると、アプリ内メッセージのキャッシュとパフォーマンスが向上します。アプリ内メッセージに含まれるすべてのメディアライブラリアセットは、より高速な表示のためにプリキャッシュされ、オフライン表示でも利用可能になります。さらに、メディアライブラリはBrazeの作成画面と統合されているため、マーケターは画像URLをコピー＆ペーストする代わりに、画像を選択したりタグを付けたりできます。

## メディアライブラリへのアクセス {#accessing-the-media-library}

メディアライブラリでは、アセットタイプ、サイズ、寸法、URL、ライブラリに追加された日付、その他の情報を確認できます。Brazeのメディアライブラリにアクセスするには、**コンテンツ** > **メディアライブラリ**に移動します。ここでは、以下の操作が可能です。

* 複数の画像を一度にアップロードする
* 仮想連絡先ファイル（.vcf）をアップロードする
* WhatsAppメッセージで使用する動画ファイルをアップロードする
* 画像を含むフォルダをアップロードする（最大50画像）
* [AIを使用して画像を生成](#generate-ai)し、メディアライブラリに保存する
* 既存の画像をトリミングして、メッセージに適した比率を作成する
* 既存のアセットのファイルを置き換えながら、URLを安定した状態に保つ
* タグやチームを追加して、画像をさらに整理する
* メディアライブラリのグリッドでタグやチームで検索する
* 画像やフォルダをドラッグ＆ドロップしてアップロードする
* 画像を削除する

![メディアライブラリページ。ファイルをドラッグ＆ドロップまたはアップロードするための「Upload To Library」セクションが含まれています。また、メディアライブラリにアップロードされたコンテンツの一覧も表示されています。]({% image_buster /assets/img_archive/media_library_main.png %})

後でBrazeでメッセージを作成する際に、メディアライブラリから画像を取り込むことができます。

![メッセージ作成画面に応じたメディアライブラリへの2つの一般的なアクセス方法。1つはメールのドラッグ＆ドロップエディターで、「Images and GIFs」というタイトルと「Add from Media Library」ボタンが表示されています。もう1つはプッシュやアプリ内メッセージなどの標準エディターで、「Media」というタイトルと「Add Image」ボタンが表示されています。]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} メディアライブラリの詳細については、[メディアライブラリ FAQ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq)をご覧ください。{% endalert %}

## ZIPファイルのアップロード {#zip-file-uploads}

ZIPファイルをメディアライブラリにアップロードする場合、すべてのファイルはZIPフォルダのルートに配置する必要があります。サブディレクトリを含めないでください。

これはアーカイブ内のすべてのファイルに適用されます。フォントファイル（`.ttf`、`.woff`、`.otf`、`.woff2`）、HTML、CSS、JavaScript、画像も含まれます。各ファイルを他のファイルと一緒にZIPのルートに配置してください。

または、ZIPにまとめずに、アセットを個別にメディアライブラリにアップロードすることもできます。

## ファイルの置き換え {#replace-a-file}

メディアライブラリ内の既存アセットのファイルを、URLとアセットIDを維持したまま置き換えることができます。URLが変わらないため、そのアセットを参照しているメッセージやキャンペーン（すでに送信済みのメールを含む）には、更新されたファイルが自動的に反映されます。これは、ロゴなどの共有アセットを、個々のキャンペーンをそれぞれ更新するのではなく、一か所で更新したい場合に便利です。

アセットを置き換えるには、「Replace Media Library Assets」権限が必要です。

1. **Content** > **Media Library** に移動します。
2. 置き換えたいアセットを選択します。
3. モーダルで **Replace file** を選択します。
4. 置き換え用のファイルをアップロードします。

![アセットの「Replace file」、「Crop image」、「Delete」ボタンが表示されたメディアライブラリ編集モーダル。]({% image_buster /assets/img_archive/media_library_replace_file.png %}){: style="max-width:60%;border:none"}

### 要件と制限事項 {#requirements-and-limitations}

- 置き換え用のファイルは、元のファイルと同じ拡張子である必要があります。たとえば、`.png` アセットを `.jpg` ファイルに置き換えることはできません。
- 動画アセットは置き換えできません。
- 置き換え後、CDNキャッシュの影響により、更新されたファイルがすべての消費者に表示されるまでに時間がかかる場合があります。

### 処理済み画像コピーを使用するチャネル {#channels-with-processed-image-copies}

一部のチャネルでは、メッセージの設定時に画像の最適化コピーが作成され、別のURLが生成されます。元のメディアライブラリアセットを置き換えても、これらのチャネルを使用して作成されたメッセージで消費者に表示される内容は更新されません。対象となるチャネルには、アプリ内メッセージ、Content Cards、プッシュ通知、バナーが含まれます。

[`PUT /media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file) エンドポイントを使用して、プログラムでアセットを置き換えることもできます。

## 画像の仕様 {#image-specifications}

メディアライブラリにアップロードするすべての画像は5&nbsp;MB未満である必要があります。サポートされているファイルタイプは、PNG、JPEG、GIF、SVG、WebPです。メッセージングチャネル別の推奨画像サイズと仕様については、[画像の仕様]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications)を参照してください。

{% alert important %}
非常に細長い形状のGIF（例：3000 x 2ピクセル）や300フレーム以上のGIFは、合計ファイルサイズが小さくてもアップロードに失敗する場合があります。
{% endalert %}

## BrazeAI<sup>TM</sup>で画像を生成する {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
この機能を使用する前に、[データがどのように使用され、OpenAIに送信されるか]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security)を確認してください。
{% endalert %}

**メディアライブラリ**ページに**AI Image Generator**が表示されない場合は、**Edit Media Library Assets**権限があることを確認してください。それでもオプションが表示されない場合は、Brazeカスタマーチームに連絡して、ワークスペースがBrazeAI画像生成にアクセスできることを確認してください。生成に失敗した場合は、[OpenAIコンテンツポリシー]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#data-privacy-and-security)を確認してください。