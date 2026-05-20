---
nav_title: 9月
page_order: 4
noindex: true
page_type: update
description: "この記事には2019年9月のリリースノートが含まれています。"
---

# 2019年9月 {#september-2019}

## OneLogin内のBrazeアプリ {#braze-app-within-onelogin}

[OneLogin]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/onelogin/)内でBrazeを検索し、サービスプロバイダーまたはIdP開始ログイン用に選択できるようになりました。これにより、OneLogin内にカスタムアプリケーションを追加する必要がなくなります。その結果、SAML SSOの導入以降に確認されていた属性などの特定の設定が事前入力されます。

## Rokt Calendarパートナーシップ {#rokt-calendar-partnership}

[Rokt Calendar]({{site.baseurl}}/partners/home/)は、Brazeのお客様にパーソナライズされたマーケティングイニシアティブを調整し、パーソナライズされたコンテンツをエンドユーザーのカレンダーに拡張する機能を提供します。これにより、エンドユーザーのエクスペリエンスがよりシームレスになり、お客様のサービスのスティッキネスがさらに向上します。以下を実行できるようになります。

- Brazeプラットフォーム経由でカレンダーの招待状を送信し、「日付を保存」してコミュニケーションを拡張する
- イベントの内容が変更された場合、既存の招待を更新する

## Passkitパートナーシップ {#passkit-partnership}

[Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit/)により、Brazeのお客様はカスタマーエンゲージメントをモバイルウォレットに拡張できます。Brazeの強力なセグメンテーションを利用しながらウォレットキャンペーンをパーソナライズし、プッシュやアプリ内メッセージなどのチャネルとのオーケストレーションを実現できます。

## メッセージングエンドポイント経由でのディスパッチID値の返却 {#dispatch-id-value-return-via-messaging-endpoints}

メッセージの`dispatch_id`は、以下のメッセージングエンドポイントのレスポンスに含まれます。
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-API-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#api-triggered-canvases)

これにより、トランザクションメッセージングを使用するお客様は、Currentsを介してコールバックをトレースできます。

## キャンバスの変更ログ {#canvas-changelogs}

自分のアカウントでキャンバスに取り組んでいるのが誰なのか、もっと詳しく知りたいと思ったことはありませんか？もうその必要はありません。キャンバスの変更ログにアクセスできるようになりました。

![キャンバスの変更ログ]({% image_buster /assets/img/canvas-changelog1.png %})
![キャンバスの変更ログ]({% image_buster /assets/img/canvas-changelog2.png %})