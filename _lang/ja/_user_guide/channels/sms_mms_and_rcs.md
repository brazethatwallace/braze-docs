---
nav_title: "SMS、MMS、RCS"
article_title: "SMS、MMS、RCS"
page_order: 8
page_type: landing
channel:
  - SMS
  - MMS
  - RCS
search_rank: 3
description: "このランディングページでは、SMS（ショートメッセージサービス）、MMS（マルチメディアメッセージサービス）、RCS（リッチコミュニケーションサービス）について説明しています。これらのサービスは、ユーザーの電話番号を利用してリアルタイムでリーチできるため、他の多くのメッセージングチャネルよりも直接的にユーザーにアプローチできます。"
---

# SMS、MMS、RCS {#sms-mms-and-rcs}

> SMS（ショートメッセージサービス）、MMS（マルチメディアメッセージサービス）、RCS（リッチコミュニケーションサービス）は、電話番号を利用してリアルタイムでユーザーにリーチする直接的な手段を提供します。SMSは高速で馴染みがあり、時間的制約のある更新情報に効果的であるため、世界中で最も広く利用されているチャネルの1つです。このハブでは、Brazeにおける送信者の設定、コンプライアンス、オプトインの収集、メッセージの作成、SMS・MMS・RCSのレポートについて説明します。最初のメッセージを送信する前に、[法律と規制]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)と[ユーザーのオプトインの収集]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)を確認してください。

## 前提条件 {#prerequisites}

SMS、MMS、およびRCSの利用可否は、お客様のBrazeパッケージによって異なります。開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。

開始する前に、以下の条件が満たされていることを確認してください。

- ショートコード、ロングコード、または英数字の送信者IDが設定されていること。詳細については、[送信者の設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を参照してください。
- SMSに関する法律および規制（TCPAやキャリア要件を含む）を理解していること。詳細については、[法律および規制]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を参照してください。
- ユーザーから明示的なオプトイン同意を取得していること。詳細については、[ユーザーオプトインの収集]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)を参照してください。

## ユースケース {#use-cases}

| ユースケース | 説明 |
| --- | --- |
| 予約リマインダー | 予約前にタイムリーなリマインダーを送信し、無断キャンセルを減らし、顧客に情報を提供します。 |
| 注文の更新 | 注文確認、配送ステータス、配達の更新をリアルタイムで顧客に通知します。 |
| 2要素認証 | アカウントログインやトランザクション確認のためのワンタイム認証コードを配信します。 |
| プロモーションオファー | 期間限定のプロモーション、フラッシュセール、パーソナライズされた割引を顧客の電話に直接届けます。 |
| カスタマーサポート | 双方向の会話を可能にし、顧客からの問い合わせの解決、フィードバックの収集、サービスリクエストの確認を行います。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

## SMS、MMS、RCSの比較 {#sms-mms-and-rcs-compared}

- **SMS**は、最大160文字（Unicodeの場合は70文字）のテキストのみのメッセージを配信します。すべてのモバイルデバイスとキャリアで普遍的にサポートされています。
- **MMS**は、画像、GIF、音声などのマルチメディアコンテンツのサポートによりSMSを拡張します。MMSにはキャリアとデバイスのサポートが必要です。
- **RCS**は、ブランド付き送信者プロファイル、サジェスト返信、カルーセル、開封確認などのリッチな機能を提供する次世代のビジネスメッセージングです。RCSの利用可否はキャリアとデバイスのサポートに依存します。

### RCSを使用する理由 {#why-use-rcs}

RCS（リッチコミュニケーションサービス）は、対応デバイスのデフォルトメッセージングアプリで、よりリッチでアプリのような体験をSMSの上に構築します。ブランドは以下の目的でRCSを使用します。

- プレーンテキストだけでなく、高解像度の画像や動画を配信します。
- サジェスト返信やアクションを追加して、顧客がワンタップで応答できるようにします。
- ブランディング付きの認証済み送信者プロファイルを表示して、メッセージの信頼性を高めます。
- キャリアが許可する場合に、開封確認やタイピングインジケーターをサポートします。

RCSは、トランザクション更新（配送、予約）、リッチクリエイティブを使用したプロモーション、クイックリプライパスを使用したカスタマーサポート、メディアや構造化アクションを活用したオンボーディングやチュートリアルなどのユースケースに適しています。設定やSMSからの移行については、[RCSの設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)を参照してください。

## よくある質問 {#frequently-asked-questions}

### BrazeでSMSを送信する前にオプトイン同意が必要ですか？ {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

はい。明示的なオプトイン同意を取得し、TCPAやキャリアの要件などの適用法に従ってください。[ユーザーオプトインの収集]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)および[法律と規制]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を参照してください。

### SMS、MMS、RCSの違いは何ですか？ {#what-is-the-difference-between-sms-mms-and-rcs}

SMSはテキストのみのメッセージを送信し、MMSは画像などのマルチメディアを追加し、RCSは対応デバイスでブランド付き送信者プロファイルや候補返信などのリッチ機能を追加します。このページの前述の**SMS、MMS、RCSの比較**を参照してください。

### SMSの送信番号を設定するにはどうすればよいですか？ {#how-do-i-configure-sender-numbers-for-sms}

キャンペーンを開始する前に、Brazeでショートコード、ロングコード、または英数字の送信者IDを設定します。[送信者設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を参照してください。

## 次のステップ {#next-steps}

- [メッセージ設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [メッセージを作成する]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)