{% if include.variable_name == "image behavior" %}


| レイアウト | 動作 |
| --- | --- |
| 画像とテキスト | 縦長または細長い画像は縮小され、水平方向の中央に配置されます。幅の広い画像は左右の端が切り取られます。 |
| 画像のみ | メッセージは、ほとんどのアスペクト比の画像に合うようにリサイズされます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テーブル" }

{% endif %}

{% if include.variable_name == "payload size" %}

次のペイロードサイズを推奨します。

| メッセージングシステム | 推奨ペイロード |
| --- | --- |
| iOS (iOS 8 以前) | 0.256 KB |
| iOS (iOS 8 以降) | 2 KB |
| Android (FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テーブル" }

{% endif %}

{% if include.variable_name == "in-app messages" %}

モーダル形式のアプリ内メッセージは、選択した画像またはメッセージのコピーのサイズや比率を維持しつつ、デバイスに最適で最もフィットする比率で表示されるように設計されています。

アプリ内メッセージに含めることができるテキスト文字数に制限はありませんが（ボタン、ヘッドライン、メインボディなども同様）、使用するテキスト文字数は適度に調整してください。テキストが多すぎると、ユーザーはメッセージを展開してスクロールする必要があります。

すべてのアプリ内メッセージの推奨画像サイズは 500 KB、最大画像サイズは 5 MB で、PNG、JPEG、GIF のファイルタイプをサポートしています。WebP 画像はすべてのデバイスやブラウザでサポートされているわけではありません。アプリ内メッセージに追加する前に、WebP 画像を PNG または JPEG に変換することを推奨します。

{% tabs %}
{% tab ポートレート %}

| タイプ | アスペクト比 | 画質 | 備考 |
| --- | --- | --- | --- |
| ポートレート全画面（テキスト付き） | 6:5 | 高解像度 1200 x 1000 px <br>最小解像度 600 x 500 px | すべての辺でクロッピングが発生する可能性がありますが、画像は常にビューポートの上位 50% を占めます。 |
| ポートレート全画面（画像のみ、ボタンあり/なし） | 3:5 | 高解像度 1200 x 2000 px <br> 最小解像度 600 x 1000 px | 縦長のデバイスでは、左右の端でクロッピングが発生することがあります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="テーブル" }

{% endtab %}
{% tab ランドスケープ %}

| タイプ | アスペクト比 | 画質 | 備考 |
| --- | --- | --- | --- |
| ランドスケープ全画面（テキスト付き） | 10:3 | 高解像度 2000 x 600 px <br>最小解像度 1000 x 300 px | すべての辺でクロッピングが発生する可能性がありますが、画像は常にビューポートの上位 50% を占めます。 |
| ランドスケープ全画面（画像のみ、ボタンあり/なし） | 5:3 | 高解像度 2000 x 600 px <br> 最小解像度 1000 x 600 px | 縦長のデバイスでは、左右の端でクロッピングが発生することがあります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="テーブル" }

{% endtab %}
{% tab スライドアップ %}

| タイプ | アスペクト比 | 画質 | 備考 |
| --- | --- | --- | --- |
| スライドアップ | 1:1 | 高解像度 150 x 150 px <br> 最小解像度 50 x 50 px | さまざまなアスペクト比の画像が、クロッピングなしで正方形の画像コンテナに収まります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="テーブル" }

{% endtab %}
{% tab モーダル %}

| タイプ | アスペクト比 | 画質 | 備考 |
| --- | --- | --- | --- |
| モーダル（画像のみ） | 1:1 | 推奨最大解像度: 1200 x 2000 px <br> 最小解像度: 600 x 600 px | メッセージは、ほとんどのアスペクト比の画像に合うようにリサイズされます。推奨最大解像度は 3:5 のアスペクト比であり、最適な結果が得られない場合があります。大きな画像も使用できますが、読み込み時間が長くなる可能性があります。<br> 画像の理想的なアスペクト比は 1:1 です。この比率を満たさない場合、アップロード時に警告が表示されることがあります。この警告は最良の結果を得るための提案であり、大きな画像のアップロードを妨げるものではありません。 |
| テキスト付きモーダル | 29:10 | 高解像度 1450 x 500 px <br> 最小解像度 600 x 205 px | 縦長の画像は縮小され、水平方向の中央に配置されます。幅の広い画像は左右の端が切り取られます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="テーブル" }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| メッセージタイプ | メッセージの最大長 | タイトルの最大長 |
| --- | --- | --- |
| iOS ロック画面 | 175 文字 | 43 文字 |
| iOS 通知 | 175 文字 | 43 文字 |
| iOS バナーアラート | 85 文字 | 43 文字 |
| Android ロック画面 | 49 文字 | 43 文字 |
| Android 通知ドロワー | 597 文字 | 43 文字 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="テーブル" }

すべてのプッシュ画像の推奨サイズは 500 KB です。

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="テーブル">
  <thead>
    <tr>
      <th>画像タイプ</th>
      <th>アスペクト比</th>
      <th>最大ピクセル数</th>
      <th>最大画像サイズ</th>
      <th>ファイルタイプ</th>
      <th>備考</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1（推奨）</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG、JPEG、GIF</td>
      <td>2020年1月現在、iOS リッチプッシュ通知では、10 MB 未満であれば 1038 x 1038 px の画像を処理できますが、できるだけ小さいファイルサイズを使用することを推奨します。実際には、大きなファイルを送信すると不要なネットワーク負荷が発生し、ダウンロードのタイムアウトがより頻繁に起こる可能性があります。<br><br>詳細については、<a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">iOS リッチ通知</a> を参照してください。</td>
    </tr>
    <tr>
      <td>Android プッシュアイコン</td>
      <td>1:1</td>
      <td>該当なし</td>
      <td>500 KB</td>
      <td>PNG、JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Android 拡張通知画像</td>
      <td>2:1</td>
      <td><b>小:</b><br>512 x 256<br><br><b>中:</b><br>1024 x 512<br><br><b>大:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG、JPEG</td>
      <td><a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">Android リッチ通知</a> で使用されます。</td>
    </tr>
    <tr>
      <td>Android インライン画像</td>
      <td>3:2</td>
      <td>該当なし</td>
      <td>該当なし</td>
      <td>PNG、JPEG</td>
      <td>詳細については、<a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Android インライン画像プッシュ</a> を参照してください。</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 aria-label="テーブル" }

{% endif %}

{% if include.variable_name == "email" %}

| メールタイプ | 推奨最大プロパティ |
| --- | --- |
| テキストのみ | 25 KB |
| 画像付きテキスト | 60 KB |
| メール幅 | 600 px |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テーブル" }

| 画像の仕様 | 推奨最大プロパティ |
| --- | --- |
| サイズ | 5 MB |
| 幅 | ヘッダー: 600 px<br>本文: 480 px |
| ファイルタイプ | PNG、JPEG、GIF<br><br> WebP 画像のサポートはメールクライアントによって異なります。信頼性の高いレンダリングのためには、メールメッセージに追加する前に WebP 画像を PNG または JPEG に変換してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テーブル" }

| テキスト仕様 | 推奨最大プロパティ |
| --- | --- |
| 件名の長さ | 35 文字<br>6〜10 ワード |
| `"From: Name"` の長さ | 25 文字 |
| プレヘッダーの長さ | 85 文字 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テーブル" }

{% endif %}

{% if include.variable_name == "content cards" %}

| カードの種類 | アスペクト比     | 画質       |
| --------- | ---------------- | ------------------- |
| クラシック   | 1:1 のアスペクト比 | 60 x 60&nbsp;px        |
| キャプション付き | 4:3 のアスペクト比 | 最小幅 600&nbsp;px |
| バナー    | 任意のアスペクト比 | 最小幅 600&nbsp;px |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="テーブル" }

詳細については、[コンテンツカードのクリエイティブ詳細]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details)を参照してください。

{% endif %}

{% if include.variable_name == "WhatsApp images" %}

これらの仕様は、テンプレートヘッダー、レスポンスメディアメッセージ、および画像メッセージに適用されます。

| プロパティ | 仕様 | 備考 |
|---|---|---|
| サポートされるフォーマット | JPEG、PNG | Meta は画像メッセージに対して JPEG と PNG のみを公式にサポートしています。WebP はスタンプ（標準の画像メッセージではない）でのみサポートされています。 |
| 最大ファイルサイズ | 5 MB | |
| カラーモード | 8 ビット、RGB または RGBA | |
| キャプション（画像メッセージのみ） | オプション、最大 1,024 文字 | |
| 推奨サイズ | 1,125 × 600 px | デバイス間で一貫したレンダリングとMetaの要件への準拠のため、1,125×600 px（1.91:1）の JPEG または PNG 画像の使用を推奨します。 |
| 推奨アスペクト比 | 1.91:1（ワイド） | 正方形（1:1）およびワイド（16:9）フォーマットも使用できますが、ユーザーのデバイスによっては画像がクロッピングまたは拡大される場合があります。<br><br> カルーセルカードの場合、ヘッダー画像はWhatsAppによって自動的にワイド比率にクロッピングされます。ただし、本文テキストがない場合は正方形でレンダリングされます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="テーブル" }

{% endif %}

{% if include.variable_name == "WhatsApp videos" %}

以下の仕様は、テンプレートヘッダー、レスポンスメディアメッセージ、動画メッセージ、およびカルーセルカードヘッダーに適用されます。

| プロパティ | 仕様 |
|---|---|
| サポートされるフォーマット | MP4、3GPP |
| ファイルサイズ | 最大 16 MB |
| 動画コーデック | H.264 のみ |
| オーディオコーデック | AAC のみ |
| オーディオストリーム | 単一オーディオストリームまたはオーディオストリームなし |
| キャプション（動画メッセージのみ） | オプション、最大 1,024 文字 |
| 推奨アスペクト比 | 1.91:1（ワイド） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="テーブル" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

{% endif %}