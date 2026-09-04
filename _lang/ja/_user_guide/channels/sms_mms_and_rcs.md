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

SMS、MMS、およびRCSの利用可否はBrazeのパッケージによって異なります。開始するには、アカウントマネージャーまたはカスタマーサクセスマネージャーにお問い合わせください。

始める前に、以下の要件を満たしていることを確認してください。

- ショートコード、ロングコード、または英数字の送信者IDが設定済みであること。詳細については、[送信者の設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を参照してください。
- TCPAやキャリア要件を含むSMSの法律と規制に精通していること。詳細については、[法律と規制]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を参照してください。
- ユーザーから明示的なオプトイン同意を取得済みであること。詳細については、[ユーザーのオプトイン収集]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)を参照してください。

## ユースケース {#use-cases}

| ユースケース | 説明 |
| --- | --- |
| 予約リマインダー | 予約時間前にタイムリーなリマインダーを送信し、無断キャンセルを減らして顧客に情報を提供します。 |
| 注文状況の更新 | 注文確認、配送ステータス、配達状況の更新をリアルタイムで顧客に通知します。 |
| 2要素認証 | アカウントログインや取引確認のためのワンタイム認証コードを配信します。 |
| プロモーションオファー | 期間限定のプロモーション、フラッシュセール、パーソナライズされた割引を顧客の携帯に直接届けます。 |
| カスタマーサポート | 双方向の会話を通じて、顧客からの問い合わせの解決、フィードバックの収集、サービスリクエストの確認を行います。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

## SMS、MMS、RCSの比較 {#sms-mms-and-rcs-compared}

- **SMS**は、最大160文字（Unicodeの場合は70文字）のテキストのみのメッセージを配信します。すべてのモバイルデバイスとキャリアで普遍的にサポートされています。
- **MMS**は、画像、GIF、オーディオなどのマルチメディアコンテンツのサポートにより、SMSを拡張します。MMSにはキャリアとデバイスのサポートが必要です。
- **RCS**は次世代のビジネスメッセージングであり、ブランド付き送信者プロファイル、提案された返信、カルーセル、既読確認などのリッチな機能を提供します。RCSの利用可能性はキャリアとデバイスのサポートに依存します。

### なぜRCSを使用するのか？ {#why-use-rcs}

RCS（Rich Communication Services）は、対応デバイスのデフォルトメッセージングアプリで、よりリッチでアプリのような体験をSMSの上に構築します。ブランドはRCSを以下の目的で使用します。

- プレーンテキストだけでなく、高解像度の画像や動画を配信できます。
- 提案された返信やアクションを追加して、顧客がワンタップで応答できるようにします。
- ブランディング付きの認証済み送信者プロファイルを表示し、メッセージの信頼性を高めます。
- キャリアが許可している場合、既読確認や入力中インジケーターをサポートします。

RCSは、トランザクション更新（配送、予約）、リッチクリエイティブを使ったプロモーション、クイックリプライパスを使ったカスタマーサポート、メディアや構造化されたアクションの恩恵を受けるオンボーディングやチュートリアルなどのユースケースに適しています。設定とSMSからの移行については、[RCSの設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup)を参照してください。

## よくある質問 {#frequently-asked-questions}

### BrazeでSMSを送信する前にオプトイン同意が必要ですか？ {#do-i-need-opt-in-consent-before-sending-sms-in-braze}

はい。明示的なオプトイン同意を収集し、TCPAやキャリアの要件などの適用される法律に従ってください。[ユーザーのオプトインの収集]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/collecting_user_opt_ins)および[法律と規制]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)を参照してください。

### SMS、MMS、RCSの違いは何ですか？ {#what-is-the-difference-between-sms-mms-and-rcs}

SMSはテキストのみのメッセージを送信し、MMSは画像などのマルチメディアを追加し、RCSは対応デバイスでブランド付き送信者プロファイルや候補返信などのリッチ機能を追加します。このページの前半にある**SMS、MMS、RCSの比較**を参照してください。

### SMSの送信者番号はどのように設定しますか？ {#how-do-i-configure-sender-numbers-for-sms}

キャンペーンを開始する前に、Brazeでショートコード、ロングコード、または英数字の送信者IDを設定してください。[送信者の設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)を参照してください。

## 次のステップ {#next-steps}

{% article_tiles %}
- name: メッセージの設定
  link: /docs/user_guide/channels/sms_mms_and_rcs/message_setup
  description: 送信前に、送信者番号、コンプライアンス設定、チャネルの前提条件を構成します。
- name: メッセージを作成する
  link: /docs/user_guide/channels/sms_mms_and_rcs/create
  description: BrazeでSMS、MMS、またはRCSキャンペーンを作成し、配信します。
{% endarticle_tiles %}