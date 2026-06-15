---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には、2020年9月のリリースノートが含まれています。"
---

# 9月 {#september}

## ファネルレポート {#funnel-reporting}

ファネルレポートは、[キャンペーン]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/)または[キャンバス]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/)を受信した後に顧客がたどるジャーニーを分析できるビジュアルレポートを提供します。

## iOS 14 アップグレードガイド {#ios-14-upgrade-guide}

Appleの新しいiOS 14で発表された変更に伴い、Braze iOS SDKの統合に必要なBraze関連の変更とアクション項目がいくつかあります。詳細については、この[アップグレードガイド]({{site.baseurl}}/ios_14/)を参照してください。

## iOS 14のIDFAおよびIDFVの変更 {#changes-to-idfa-and-idfv-for-ios-14}

iOS 14では、ユーザーがアプリにアクセスしたときに広告トラッキングをオプトインして、アプリと広告ネットワークにIDFAの読み取りを許可するかどうかを決定する必要があります。それに応じたBrazeの戦略として、代わりに「ベンダーの識別子」（IDFVなど）を使用して、異なるデバイス間でユーザーを継続的に追跡できるようにします。詳しくは、[iOS 14 アップグレードガイド]({{site.baseurl}}/ios_14/)をご覧ください。

## メール検証 {#email-validation}

この新しいメールシンタックス検証プロセスは、Brazeの既存のものへのアップグレードです。これは、Brazeに更新またはインポートされたメールが正しいことを確認するための検査です。詳細については、[これらのガイドラインと注記]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/)を参照してください。

## Currentsにおけるランダムバケットユーザーイベント {#random-bucket-user-event-in-currents}

ランダムバケット番号（RBNなど）は、ワークスペース内で新しいユーザーが作成されるたびに生成されます。このイベントの間、新規ユーザーのそれぞれにランダムなバケット番号が割り当てられます。このバケット番号を使用して、ランダムなユーザーの一様分布セグメントを作成できます。これを使用して、ランダムバケット番号値の範囲をグループ化し、キャンペーンとバリアント間でパフォーマンスを比較できます。このイベントが使用可能かどうかを確認するには、Currentsの[顧客行動イベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)を参照してください。

## キャンバスコンポーネント - 近日提供開始！ {#canvas-components-coming-soon}

Brazeは、キャンバスの柔軟性と機能性を向上させるために、4つの新しいキャンバスコンポーネントを追加しました。これらの新しいコンポーネントには[条件分岐ステップ]({{site.baseurl}}/decision_split/)、[遅延ステップ]({{site.baseurl}}/delay_step/)、[メッセージングステップ]({{site.baseurl}}/message_step/)、[Facebookへのオーディエンス同期]({{site.baseurl}}/audience_sync_facebook/)が含まれます。
- **キャンバスの条件分岐、遅延、およびメッセージングステップ**<br>条件分岐を使用して、ユーザーが定義済みのクエリと一致するかどうかに基づいてキャンバス Branchを作成できます。遅延ステップでは、対応するメッセージを必要とせずに、キャンバスにスタンドアロンの遅延を追加できます。メッセージステップでは、キャンバスフロー内の目的の場所にスタンドアロンのメッセージを追加できます。
- **Facebookへのオーディエンス同期**<br>Braze Facebookへのオーディエンス同期を使用すると、ブランドは独自のBraze統合からのユーザーデータをFacebookのカスタムオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいて広告を配信できます。ユーザーデータに基づいてBraze キャンバスでメッセージをトリガーするために通常使用する基準（プッシュ、メール、SMS、Webhookなど）を、カスタムオーディエンスを介してFacebook内の該当ユーザーに対して広告をトリガーするために使用できるようになりました。

## SMSインバウンド受信イベント {#sms-inbound-received-events}

新しいメッセージングエンゲージメントイベントがCurrentsに追加されました。このイベントは、ユーザーの1人がBraze SMSサブスクリプショングループの電話番号にSMSを送信したときに発生します。詳細については、Currentsの[メッセージングおよびエンゲージメントイベント用語集]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)を参照してください。