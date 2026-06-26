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
| 「View Media Library Assets」権限 | メディアライブラリアセットの表示 |
| 「Edit Media Library Assets」権限 | メディアライブラリアセットの作成と更新 |
| 「Delete Media Library Assets」権限 | メディアライブラリアセットの完全な削除 |
| 「Replace Media Library Assets」権限 | 既存のメディアライブラリアセットのURLとアセットIDを維持したままファイルを置換 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メディアライブラリの権限" }

詳細については、[ユーザー権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/)を参照してください。

## メディアライブラリとCDNの比較 {#media-library-versus-cdn}

CDN（コンテンツデリバリーネットワーク）の代わりにメディアライブラリを使用すると、アプリ内メッセージのキャッシュとパフォーマンスが向上します。アプリ内メッセージに含まれるすべてのメディアライブラリアセットは、より高速な表示のためにプリキャッシュされ、オフライン表示でも利用可能になります。さらに、メディアライブラリはBrazeの作成画面と統合されているため、マーケターは画像URLをコピー＆ペーストする代わりに、画像を選択したりタグ付けしたりできます。

## メディアライブラリへのアクセス {#accessing-the-media-library}

メディアライブラリでは、アセットの種類、サイズ、寸法、URL、ライブラリに追加された日付、その他の情報を確認できます。Brazeのメディアライブラリにアクセスするには、**Content** > **Media Library**に移動します。ここでは、以下の操作が可能です。

* 複数の画像を一度にアップロード
* バーチャルコンタクトファイル（.vcf）のアップロード
* WhatsAppメッセージで使用する動画ファイルのアップロード
* 画像を含むフォルダのアップロード（最大50画像）
* [AIを使用して画像を生成](#generate-ai)し、メディアライブラリに保存
* 既存の画像をトリミングして、メッセージに適した比率を作成
* 既存のアセットのURLを維持したままファイルを置換
* タグやチームを追加して、画像をさらに整理
* メディアライブラリのグリッドでタグやチームで検索
* 画像やフォルダをドラッグ＆ドロップしてアップロード
* 画像の削除

![メディアライブラリページ。ファイルをドラッグ＆ドロップまたはアップロードするための「ライブラリにアップロード」セクションがあります。また、メディアライブラリにアップロードされたコンテンツの一覧も表示されています。]({% image_buster /assets/img_archive/media_library_main.png %})

後でBrazeでメッセージの下書きを作成する際に、メディアライブラリから画像を取り込むことができます。

![メッセージ作成画面に応じたメディアライブラリへの2つの一般的なアクセス方法。1つはメールのドラッグ＆ドロップエディターで、「画像とGIF」というタイトルと「メディアライブラリから追加」ボタンが表示されています。もう1つはプッシュやアプリ内メッセージなどの標準エディターで、「メディア」というタイトルと「画像を追加」ボタンが表示されています。]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} メディアライブラリの詳細については、[メディアライブラリFAQ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/faq/)をご覧ください。{% endalert %}

## ファイルの置換 {#replace-a-file}

メディアライブラリ内の既存アセットのURLとアセットIDを維持したまま、ファイルを置換できます。URLが変わらないため、そのアセットを参照しているメッセージやCampaign（すでに送信済みのメールを含む）は、自動的に更新されたファイルを反映します。これは、ロゴなどの共有アセットを各Campaignを個別に更新するのではなく、一か所で更新したい場合に便利です。

アセットを置換するには、「Replace Media Library Assets」権限が必要です。

1. **Content** > **Media Library**に移動します。
2. 置換したいアセットを選択します。
3. モーダルで**Replace file**を選択します。
4. 置換ファイルをアップロードします。

![メディアライブラリの編集モーダル。アセットに対する「Replace file」、「Crop image」、「Delete」ボタンが表示されています。]({% image_buster /assets/img_archive/media_library_replace_file.png %}){: style="max-width:60%;border:none"}

### 要件と制限事項 {#requirements-and-limitations}

- 置換ファイルは元のファイルと同じファイル拡張子である必要があります。例えば、`.png`アセットを`.jpg`ファイルで置換することはできません。
- 動画アセットは置換できません。
- 置換後、CDNキャッシュの影響により、更新されたファイルがすべての消費者に表示されるまでに時間がかかる場合があります。

### 処理済み画像コピーを使用するチャネル {#channels-with-processed-image-copies}

一部のチャネルでは、メッセージの設定時に画像の最適化コピーが作成され、別のURLが生成されます。元のメディアライブラリアセットを置換しても、これらのチャネルを使用して作成されたメッセージで消費者に表示される内容は更新されません。対象チャネルには、アプリ内メッセージ、Content Cards、プッシュ通知、バナーが含まれます。

[`PUT /media_library/replace_file`]({{site.baseurl}}/api/endpoints/media_library/manage_assets/replace_file/)エンドポイントを使用して、プログラムでアセットを置換することもできます。

## 画像の仕様 {#image-specifications}

メディアライブラリにアップロードするすべての画像は5&nbsp;MB未満である必要があります。サポートされているファイル形式は、PNG、JPEG、GIF、SVG、WebPです。メッセージングチャネル別の推奨画像サイズと仕様については、[画像の仕様]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications/)を参照してください。

{% alert important %}
非常に細長い形状のGIF（例：3000 x 2ピクセル）や300フレーム以上のGIFは、合計ファイルサイズが小さくてもアップロードに失敗する場合があります。
{% endalert %}

## BrazeAI<sup>TM</sup>で画像を生成する {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
この機能を使用する前に、[データがどのように使用され、OpenAIに送信されるか]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#ai-policy)を確認してください。
{% endalert %}

**Media Library**ページに**AI Image Generator**が表示されない場合は、**Edit Media Library Assets**権限があることを確認してください。それでもオプションが表示されない場合は、Brazeカスタマーチームに連絡して、ワークスペースがBrazeAI画像生成にアクセスできることを確認してください。生成に失敗した場合は、[OpenAIコンテンツポリシー]({{site.baseurl}}/user_guide/brazeai/operator/capabilities/#ai-policy)を確認してください。