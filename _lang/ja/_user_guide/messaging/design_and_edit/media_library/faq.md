---
nav_title: FAQ
article_title: メディアライブラリ FAQ
page_order: 2
page_type: FAQ
tool: Media
description: "この記事では、Brazeのメディアライブラリに関するよくある質問への回答を提供します。"

---

# よくある質問 {#frequently-asked-questions}

> このページでは、Brazeのメディアライブラリに関するよくある質問への回答を提供します。

## 一般 {#general}

### メディアライブラリ内の画像にストレージ制限はありますか？ {#are-there-storage-limits-for-images-within-the-media-library}

いいえ、メディアライブラリ内のアセットにストレージ制限はありません。ただし、アセットのサイズ制限（最大5 MB）はあります。

### アップロードしたアセットに有効期限はありますか？ {#are-there-expiration-dates-for-uploaded-assets}

いいえ、メディアライブラリにアップロードされたアセットは、Brazeとの契約期間中ずっと保持されます。

### 動画アセットをアップロードできますか？ {#can-i-upload-video-assets}

いいえ、メディアライブラリは動画ファイルをサポートしていません。動画は外部でホスティングするか、YouTubeなどのプラットフォームを使用することをお勧めします。

### すべての画像タイプをトリミングできますか？ {#can-i-crop-all-image-types}

いいえ、メディアライブラリはGIF画像のトリミングをサポートしていません。

### メディアライブラリにアップロードした画像のURLをコピーするにはどうすればよいですか？ {#how-do-i-copy-the-url-of-an-image-uploaded-to-the-media-library}

メディアライブラリにアップロードした画像のURLをコピーするには、**コンテンツ** > **メディアライブラリ**に移動します。参照したい画像にカーソルを合わせ、**画像URLをコピー**アイコンを選択すると、画像URLがクリップボードにコピーされます。

### メールでSVG画像を使用できますか？ {#can-i-use-svg-images-in-email}

SVG画像は、メールクライアント間でのサポートが限定的なため、メールでの使用は推奨されません。Gmailやその他の主要なメールプロバイダーはSVG画像をレンダリングしないため、受信者にとって画像が壊れたり表示されなかったりする可能性があります。信頼性の高いメールレンダリングには、代わりにPNG、JPEG、またはGIF形式を使用してください。

### 既存の画像をトリミングするにはどうすればよいですか？ {#how-do-i-crop-an-existing-image}

既存の画像をトリミングするには、メディアライブラリから画像を選択し、**トリミングして新しい画像として保存**をクリックします。

![メディアライブラリの画像プレビュー。]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

トリミングコンポーザーにリダイレクトされ、比率タイプを選択したり、新しい画像の名前を編集したりできます。**保存**を選択すると、新しい画像が使用可能になります。

![メディアライブラリの画像をトリミングして保存するウィンドウ。]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### 画像をアップロードしようとするとタイムアウトし続けます。どうすればよいですか？ {#my-image-keeps-timing-out-when-i-try-to-upload-it-what-can-i-do-about-this}

これはさまざまな理由で発生する可能性がありますが、一般的な解決策は、アップロードを試みる前に画像を最適化することです。[ImageOptim](https://imageoptim.com/mac)などの画像オプティマイザーを使用して画像を処理してください。

また、画像がPhotoshop（または同様のソフトウェア）で作成され、多くのレイヤーがある場合は、レイヤーを統合して数を減らすことも効果的です。

### 5 MB未満でサポートされている形式の画像をアップロードしても「予期しないエラー」が表示されます。何が問題ですか？ {#i-see-an-unexpected-error-when-uploading-an-image-even-though-its-under-5-mb-and-in-a-supported-format-whats-wrong}

これは主に2つの理由で発生する可能性があります。

1. **ファイル内の無効なメタデータ：** Brazeが画像処理に使用するソフトウェアが、無効または互換性のないメタデータを持つファイルを拒否する場合があります。場合によっては、ファイルが処理される過程で5 MBの制限を超えることもあります。別の画像を使用するか（例えば、画像エディターから再エクスポートまたは再保存する）、別のソースの画像を試してください。
2. **ファイル名の特殊文字：** `&`や`%`などの特殊文字を含むファイル名は、アップロードの失敗を引き起こす可能性があります。ファイル名を英字、数字、ハイフン、またはアンダースコアのみに変更してから、再度アップロードしてください。

### プッシュコンポーザーに任意の画像をアップロードできないのはなぜですか？ {#why-cant-i-upload-any-image-i-want-into-the-push-composers}

これは、ほとんどのコンポーザーに許可される画像の比率サイズに制限があるためです。

### AIを使用して画像を生成する {#generate-an-image-using-ai}

**コンテンツ** > **メディアライブラリ**から**AI画像ジェネレーター**を選択して画像を生成できます。**メディアライブラリアセットの編集**権限が必要です。このオプションが表示されない場合は、Brazeカスタマーチームにお問い合わせください。手順とポリシーの詳細については、[BrazeAIで画像を生成する]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-images)および[BrazeAIによる画像生成]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#generate-ai)を参照してください。

### メディアライブラリの画像アセットにバニティURLを作成できますか？ {#can-i-create-vanity-urls-for-media-library-image-assets}

メディアライブラリアセットのバニティURLはサポートされていません。カスタムURLを使用するとCDN配信が中断されるためです。キャンペーンが既にそのURLを参照している場合は、既存のURLで画像を置き換えることができます。詳細については、[ファイルを置き換える]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file)を参照してください。