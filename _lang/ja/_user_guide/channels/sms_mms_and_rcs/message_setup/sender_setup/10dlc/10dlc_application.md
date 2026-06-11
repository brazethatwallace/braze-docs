---
nav_title: 10DLCアプリケーション
article_title: 10DLCアプリケーションに必要な情報
alias: /10dlc_application/
page_type: reference
description: "この記事では、10DLCの登録をBrazeと連携して行う場合にBrazeが必要とする会社情報とSMS キャンペーン情報について説明します。"
channel:
  - SMS
---

# 10DLCアプリケーションに必要な情報 {#required-information-for-10dlc-application}

> この記事では、10DLCの登録をBrazeと連携して行う場合にBrazeが必要とする会社情報とSMS キャンペーン情報について説明します。

Brazeに10DLCの登録支援を依頼された場合は、契約に基づき、以下に記載されたすべての必要情報を下記のメールアドレスにお送りいただく必要があります。

関連するスクリーンショットや添付ファイルを含め、すべてを [smsapplications@braze.com](mailto:smsapplications@braze.com) にお送りください。10DLCについてご質問がある場合は、[Braze SMS 10DLCガイド]({{site.baseurl}}/assets/pdf/SMS_10DLC_Guide.pdf)をご確認いただくか、Brazeのカスタマーサクセスマネージャーにお問い合わせください。


## 会社情報（10DLC） {#company-information-10dlc}

米国のすべてのキャリアは、新しいキャンペーン申請に以下の会社情報を必要とします。


| フィールド                                                         | オプション（該当する場合）                                       | 説明                                                  |
|---------------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------------|
| 正式な法人名                                           |                                                               | EINに登録されている正確な法人名を入力してください。（例：Braze ではなく Braze Inc.） |
| 事業形態                                                 | {::nomarkdown} <ul><li>Corporation</li><li>Co-operative</li><li>Limited Liability Corporation</li><li>Non-profit</li><li>Partnership</li><li>Sole Proprietorship</li></ul> {:/}|   |
| 事業者EIN / 税務ID番号                                  |                                                               | 事業者を識別するために使用される番号です。   |
| 事業者登録ID種別                                 | {::nomarkdown}<ul><li>USA: Employer Identification Number (EIN)</li><li>Canada: Canadian Corporation Number (CCN)</li><li>Great Britain: Company Number</li><li>Australia: Company Number from ASIC (ACN)</li><li>India: Corporate Identity Number</li><li>VAT Number</li><li>Israel: Registration Number</li><li>Other</li></ul>{:/}  |                                                              |
| 事業者登録ID種別で「Other」を選択した場合、事業者を識別するために使用するその他の登録機関を指定してください。|                                                              |
| 業種                                             | {::nomarkdown} <ul><li>Automotive</li><li>Agriculture</li><li>Banking</li><li>Consumer</li><li>Education</li><li>Electronics</li><li>Engineering</li><li>Energy</li><li>Fast Moving Consumer Goods</li><li>Financial</li><li>Fintech</li><li>Food & Beverage</li><li>Government</li><li>Healthcare</li><li>Hospitality</li><li>Insurance</li><li>Jewelry</li><li>Legal</li><li>Manufacturing</li><li>Media</li><li>Not-for-Profit</li><li>Oil & Gas</li><li>Online</li><li>Raw Materials</li><li>Real Estate</li><li>Religion</li><li>Retail</li><li>Technology</li><li>Telecommunications</li><li>Transportation</li><li>Travel</li></ul>{:/} | |
| WebサイトURL                                                   |                                                               | 提供するWebサイトは、登録されたブランドを反映し、アクセス可能である必要があります。 |
| 事業展開地域（該当するものをすべて選択）        | {::nomarkdown} <ul><li>Africa</li><li>Asia</li><li>Europe</li><li>Latin America</li><li>USA & Canada</li></ul>{:/}    |    |
| 正式な法人住所（番地、市区町村、州、郵便番号）        |                                                               | EINまたは登録リストに記載されている事業所住所を入力してください。  |
| 会社種別                                                  | {::nomarkdown} <ul><li>Private</li><li>Non-Profit</li><li>Government</li><li>Public</li></ul> {:/}  |     |
| 上場企業の場合、ティッカーシンボルを提供してください                         |                                                               |                                                              |
| 正規代表者 #1&nbsp;-&nbsp;氏名                           |                                                               | ショートコードに関する問題が発生した場合、Brazeが最初の連絡窓口となります。これは一般公開される情報ではなく、キャリアがファイルに保管するためのものです（この項目および以降の項目に適用されます）。 |
| 正規代表者 #1&nbsp;-&nbsp;メールアドレス                          |                                                               |                                                              |
| 正規代表者 #1&nbsp;-&nbsp;役職名                 |                                                               |                                                              |
| 正規代表者 #1&nbsp;-&nbsp;職位                   |                                                               |                                                              |
| 正規代表者 #1&nbsp;-&nbsp;電話番号                   |                                                               |                                                              |
| オプション 正規代表者 #2&nbsp;-&nbsp;氏名                  |                                                               |                                                              |
| オプション 正規代表者 #2&nbsp;-&nbsp;メールアドレス                 |                                                               |                                                              |
| オプション 正規代表者 #2&nbsp;-&nbsp;役職名        |                                                               |                                                              |
| オプション 正規代表者 #2&nbsp;-&nbsp;職位          |                                                               |                                                              |
| オプション 正規代表者 #2&nbsp;-&nbsp;電話番号          |                                                               |                                                              |
| 正式な法人住所（番地、市区町村、州、郵便番号）        |                                                               |                                                              |
| 会社種別（private、non-profit、government、public（ティッカーシンボルを提供してください）） |                                       |                                                              |
| 上場企業の場合、ティッカーシンボルを提供してください                         |                                                               |                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Company Information (10DLC)" }

## SMS キャンペーン情報 {#sms-campaign-information}

米国のロングコードを含む各SMSサブスクリプショングループを、それぞれ独自のA2P 10DLC キャンペーン（ユースケースとも呼ばれます）に登録する必要があります。米国のロングコードを含むSMSサブスクリプショングループごとに、以下の情報を1回ずつ提供してください。

| フィールド | オプション（該当する場合） | 説明 |
| ------ | ------------------------ | --------------- |
| キャンペーンのユースケース（最も適切なものを1つ選択） | {::nomarkdown} <ul><li>Marketing</li><li>Account Notifications</li><li>Delivery Notifications</li><li>Customer Care</li><li>Security Alert</li><li>Fraud Alert Messaging</li><li>Higher Education</li><li>Mixed</li><li>Polling and Voting</li><li>Public Service Announcement</li></ul>{:/} | 注：サブスクリプショングループに「Mixed」ユースケースを使用する予定の場合は、事前にカスタマーサクセスマネージャーまたはカスタマーオンボーディングマネージャーに重要な詳細をご確認ください。 |
| キャンペーン名 | | {::nomarkdown}<p>SMS キャンペーン名は、メッセージング、利用規約、およびユーザーがプログラムに登録するすべての場所で一貫して表示される必要があります。</p><p>例：</p><ul><li>Braze Marking Alerts</li><li>Braze Account Notifications</li><li>Braze Cart Reminders</li></ul>{:/} |
| キャンペーンの説明 | | このキャンペーンは、特別オファー/クーポンやカートリマインダー通知など、SMSの受信をオプトインしたユーザーにマーケティングおよびプロモーションメッセージを送信します。 |
| カスタマーサポートのメールアドレス | | エンドユーザーがヘルプやサポートのためにメールで連絡できる宛先です。 |
| カスタマーサポートの電話番号 | | エンドユーザーがヘルプやサポートのために電話で連絡できる番号です。 |
| SMS利用規約URL | | {::nomarkdown} <p>米国A2P 10DLC登録を完了するには、SMS利用規約ページに以下の内容を含める必要があります：</p><ol><li>プログラム（ブランド）名</li><li>Webサイトとメッセージフローで一貫した製品開示</li><li>メッセージ頻度（メッセージフローと一致）</li><li>「Message and Data rates may apply」の免責事項</li><li>HELP/STOPの手順またはカスタマーケアの連絡先情報</li></ol><p>このページが公開されていない場合、または必要な開示事項が不足している場合は、SMS利用規約のドラフトと、ライブWebページへの実装予定日が登録プロセスの完了に必要となります。</p>{:/} |
| エンドユーザーはどのようにSMS キャンペーンにオプトインしますか？（エンドユーザーがSMSプログラムにオプトインする方法、つまりSMSメッセージの受信に同意する方法を共有してください。複数のオプトイン方法を使用する場合は、すべてここに記載する必要があります。） | | {::nomarkdown}<p>例：</p><ul><li>エンドユーザーはXXXXXXXXXXにSTARTとテキスト送信してオプトインします。</li><li>エンドユーザーはWebサイトにアクセスし、携帯電話番号を追加します。その後、SMSの受信に同意するチェックボックスにチェックを入れます。</li><li>選択したオプトイン方法がまだ公開されていない場合は、オプトイン方法のモックアップ/スクリーンショットを提供してください。</li></ul>{:/} |
| オプトインキーワード | | {::nomarkdown} <p>エンドユーザーがキーワードをテキスト送信してこのキャンペーンからSMSの受信を開始できる場合、それらのキーワードを提供する必要があります。デフォルトでは、Brazeは以下のキーワードを設定しています：</p><ul><li>START</li><li>UNSTOP</li><li>YES</li></ul><p>キーワードの追加をご希望の場合はお知らせください。</p> {:/} |
| オプトイン確認メッセージ | | エンドユーザーのオプトインを確認するために送信される自動返信メッセージを提供する必要があります。オプトイン応答には、ブランド名、定期メッセージキャンペーンへのオプトイン登録の確認、ヘルプの取得方法、およびオプトアウト方法の明確な説明を含める必要があります。（例：Thanks for joining Braze Marketing Alerts! Message frequency varies. Message and data rates may apply. Reply HELP for help or STOP to opt out.） |
| オプトアウトキーワード | | {::nomarkdown} <p>エンドユーザーは、キーワードをテキスト送信してこのキャンペーンからのメッセージ受信を停止できる必要があります。デフォルトでは、Brazeは以下のキーワードを設定しています：</p><ul>  <li>STOP</li><li>STOPALL</li><li>UNSUBSCRIBE</li><li>CANCEL</li><li>END</li><li>QUIT</li></ul><p>キーワードの追加をご希望の場合はお知らせください。</p>{:/} |
| オプトアウトメッセージ | | エンドユーザーからオプトアウトキーワードを受信した際、キャリアはオプトアウトリクエストの確認と、今後メッセージが送信されないことの確認を含む自動生成応答を期待しています。また、これらのオプトアウトメッセージにはブランド名を含めることが推奨されます。（例：Braze Marketing Alerts: You are unsubscribed from all messages. Reply HELP for help.） <br><br>最大320文字|
| ヘルプキーワード | | エンドユーザーは、キーワードをテキスト送信してヘルプを受けられる必要があります。デフォルトでは、Brazeは以下のキーワードを設定しています：-HELP -INFO キーワードの追加をご希望の場合はお知らせください。 |
| ヘルプメッセージ | | エンドユーザーからヘルプキーワードを受信した際、キャリアはブランド名と追加のサポート連絡先情報を含む自動生成応答を期待しています。（例：Braze Marketing Alerts: For help call 555-555-555. Msg&data rates may apply. Msg freq may vary, Text STOP to cancel）<br><br>最大320文字|
| サンプルメッセージ 1/2 | | Customer/Brand Updates: Hello and Welcome to Customer Brand Updates. Please visit our website at www.customerwebsite.com. Please type HELP for help or STOP to opt out. |
| サンプルメッセージ 2/2 | | Customer/Brand Updates: Check out our latest holiday sale for 20% off all items through Monday. Please visit our website at www.customerwebsite.com. Please type HELP for help or STOP to opt out. |
| 1日あたりの推定送信量 | | この特定のユースケース/サブスクリプショングループにおける1日あたりの平均送信メッセージ数の推定値を示してください（例：10,000）。 |
| コールトゥアクションチェックリスト | | {::nomarkdown} <p>コールトゥアクションには以下を含める必要があります：</p><ol><li>製品の説明</li><li>メッセージ頻度の開示</li><li>完全な利用規約へのリンク</li><li>完全なプライバシーポリシーへのリンク</li><li>STOPキーワードの手順</li><li>HELPキーワードの手順</li><li>「Message and Data Rates」が適用される場合がある旨の開示</li></ol> {:/} |
| コールトゥアクションの例 | | ![必要な詳細がすべて含まれたコールトゥアクションの例。]({{site.baseurl}}/assets/img_archive/10dlc_cta_example.png) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS campaign information" }