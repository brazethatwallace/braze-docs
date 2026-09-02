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
description: "BrazeにおけるSMS、MMS、RCSについて学びましょう。設定、コンプライアンス、電話番号を通じてユーザーにリーチするためのベストプラクティスなどを説明します。"
---

# SMS、MMS、RCS {#sms-mms-and-rcs}

> SMS（ショートメッセージサービス）、MMS（マルチメディアメッセージサービス）、RCS（リッチコミュニケーションサービス）は、電話番号を利用してリアルタイムでユーザーにリーチする直接的な手段を提供します。SMSは高速で馴染みがあり、時間的制約のある更新情報に効果的であるため、世界中で最も広く利用されているチャネルの1つです。このハブでは、Brazeにおける送信者の設定、コンプライアンス、オプトインの収集、メッセージの作成、SMS・MMS・RCSのレポートについて説明します。最初のメッセージを送信する前に、[法律と規制]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)と[ユーザーのオプトインの収集]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)を確認してください。

## 前提条件 {#prerequisites}

SMS、MMS、RCSの利用可能性は、Brazeのパッケージによって異なります。開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。

始める前に、以下の準備が整っていることを確認してください。

- ショートコード、ロングコード、または英数字の送信者IDが設定されていること。詳細については、[送信者設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を参照してください。
- TCPAやキャリア要件を含むSMSの法律と規制に精通していること。詳細については、[法律と規制]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を参照してください。
- ユーザーから明示的なオプトイン同意を取得していること。詳細については、[ユーザーのオプトイン収集]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)を参照してください。

## ユースケース {#use-cases}

| ユースケース | 説明 |
| --- | --- |
| 予約リマインダー | 予約時刻の前にタイムリーなリマインダーを送信し、無断キャンセルを減らして顧客に情報を提供します。 |
| 注文の更新 | 注文確認、配送状況、配達の更新をリアルタイムで顧客に通知します。 |
| 2要素認証 | アカウントログインや取引確認のためのワンタイム認証コードを配信します。 |
| プロモーションオファー | 期間限定のプロモーション、フラッシュセール、パーソナライズされた割引を顧客の携帯に直接届けます。 |
| カスタマーサポート | 双方向の会話を通じて顧客の問い合わせを解決し、フィードバックを収集し、サービスリクエストを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

## SMS、MMS、RCSの比較 {#sms-mms-and-rcs-compared}

- **SMS**は、160文字（Unicodeの場合は70文字）までのテキストのみのメッセージを配信します。すべてのモバイルデバイスとキャリアで普遍的にサポートされています。
- **MMS**は、画像、GIF、オーディオなどのマルチメディアコンテンツのサポートによりSMSを拡張します。MMSにはキャリアとデバイスのサポートが必要です。
- **RCS**は次世代のビジネスメッセージングであり、ブランド送信者プロファイル、候補返信、カルーセル、既読確認などのリッチな機能を提供します。RCSの利用可能性はキャリアとデバイスのサポートに依存します。

### RCSを使用する理由 {#why-use-rcs}

RCS（Rich Communication Services）は、対応デバイスのデフォルトメッセージングアプリで、よりリッチでアプリに近い体験をSMSの上に構築します。ブランドがRCSを使用する目的は以下のとおりです。

- プレーンテキストだけでなく、高解像度の画像や動画を配信します。
- 候補返信やアクションを追加し、顧客がワンタップで応答できるようにします。
- ブランディング付きの認証済み送信者プロファイルを表示し、メッセージの信頼性を高めます。
- キャリアが許可している場合、既読確認やタイピングインジケーターをサポートします。

RCSは、トランザクション更新（配送、予約）、リッチクリエイティブを使用したプロモーション、クイックリプライパスを使用したカスタマーサポート、メディアや構造化アクションが役立つオンボーディングやチュートリアルなどのユースケースに適しています。セットアップとSMSからの移行については、[RCS設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)を参照してください。

## よくある質問 {#frequently-asked-questions}

### BrazeでSMSを送信する前にオプトインの同意が必要ですか？ {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

はい。明示的なオプトインの同意を取得し、TCPAやキャリア要件などの適用される法律に従ってください。[ユーザーのオプトインの収集]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)および[法律と規制]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を参照してください。

### SMS、MMS、RCSの違いは何ですか？ {#what-is-the-difference-between-sms-mms-and-rcs}

SMSはテキストのみのメッセージを送信し、MMSは画像などのマルチメディアを追加し、RCSは対応デバイスでブランド送信者プロファイルや候補返信などのリッチ機能を追加します。このページの前半にある**SMS、MMS、RCSの比較**を参照してください。

### SMSの送信者番号はどのように設定しますか？ {#how-do-i-configure-sender-numbers-for-sms}

キャンペーンを開始する前に、Brazeでショートコード、ロングコード、または英数字の送信者IDを設定します。[送信者設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を参照してください。

## 次のステップ {#next-steps}

- [メッセージ設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup)
- [メッセージを作成する]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create)