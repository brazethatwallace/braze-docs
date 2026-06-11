---
nav_title: よくある質問
article_title: エクスポートに関してよくある質問
page_order: 7
page_type: FAQ
description: "この記事では、API と CSV エクスポートに関してよくある質問をいくつか取り上げます。"

---

# よくある質問 {#frequently-asked-questions}

> このページでは、API と CSV エクスポートに関してよくある質問への回答を提供します。

### 特定のエクスポートを S3 バケットに入れて、他のエクスポートを入れないようにできますか? {#can-you-make-certain-exports-appear-in-your-s3-bucket-and-others-not}

いいえ。S3 認証情報を指定した場合、エクスポートはすべて S3 バケットに入れられます。認証情報を指定しない場合は、Brazeに属する S3 バケットにエクスポートが入れられます。

### データをエクスポートするために、Brazeに S3 の認証情報を追加する必要がありますか? {#do-i-have-to-add-s3-credentials-to-braze-to-export-data}

いいえ。S3 の認証情報を追加しない場合、Brazeに属する S3 バケットにエクスポートが入れられます。

### ダッシュボードで S3 の認証情報を設定したが、「これをデフォルトのデータエクスポート先にする」を選択しないとどうなりますか? {#what-happens-if-you-set-up-s3-credentials-in-the-dashboard-but-dont-select-make-this-the-default-data-export-destination}

**これをデフォルトのデータエクスポート先にする**チェックボックスは、S3 と Azure の両方の認証情報を追加した場合に、エクスポート先が S3 と Azure のどちらになるかを決定します。

### デフォルトのデータエクスポート先は Braze Currentsに影響しますか? {#does-the-default-data-export-destination-affect-braze-currents}

いいえ。Currentsは独自のコネクターとストレージ設定を使用します。CSV および API 駆動のエクスポートのデフォルトエクスポート先を選択しても、Currentsのデータの書き込み先は変わりません。

### ユーザープロファイルを S3 にエクスポートしたときに、複数のファイルを受け取ったのはなぜですか? {#why-did-i-receive-multiple-files-when-exporting-user-profiles-to-s3}

これは、多数のユーザーがいるワークスペースでは予期される動作です。Brazeでは、ワークスペース内のユーザー数に応じて、エクスポートを複数のファイルに分割します。通常、5,000 人のユーザーにつき 1 つのファイルが出力されます。大きなワークスペース内の小さなSegmentをエクスポートしている場合でも、複数のファイルを受け取る可能性があることに注意してください。

### REST APIでSegment別にユーザーをエクスポートすると、重複が表示されるのはなぜですか? {#why-do-i-see-duplicates-when-i-export-users-by-segment-through-rest-api}

これは、データベースプロバイダーの基盤となるアーキテクチャに起因する非常にまれな事象です。重複は毎週クリーンアップされますが、ほとんどの週では重複がクリアされることはありません。

### ExcelでCSVレポートを開くにはどうすればよいですか? {#how-do-i-open-csv-reports-in-excel}

CSVファイルは通常デフォルトでExcelで自動的に開かれますが、常にそうとは限りません。Excelをデフォルトのプログラムとして設定する手順については、[Windows](https://support.microsoft.com/en-us/windows/change-which-programs-windows-7-uses-by-default-62fd162f-8c82-0436-806f-c60d69dcf495) および [Apple](https://support.apple.com/guide/mac-help/choose-an-app-to-open-a-file-on-mac-mh35597/mac) のトラブルシューティング記事を参照してください。

CSVをXLSXまたはXLSに変換したり、データ値間のカンマを除去したりするには、ExcelへのCSVインポートに関する[こちらのガイド](https://www.ablebits.com/office-addins-blog/convert-csv-excel/#import-csv-wizard)を参照してください。

CSVエクスポートでユーザー IDの先頭のゼロが削除されている場合、これはExcelがCSV内の数値をテキストではなくデータとして扱うために発生します。この問題を解決するには、[Excelのテキストインポートウィザード](https://www.ablebits.com/office-addins-blog/converting-csv-excel-issues/#leading-zeros)を実行してください。