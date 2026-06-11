---
nav_title: 位置情報の追跡
article_title: 位置情報の追跡
page_order: 0
page_type: reference
description: "このリファレンス記事では、アプリで位置情報の追跡と位置情報ターゲティングを使用する方法、および位置情報の追跡をサポートするパートナーについて説明します。"
tool: Location
search_rank: 2
---

# 位置情報の追跡 {#location-tracking}

> 位置情報の収集は、アプリが開かれた際に GPS 位置データを使用してユーザーの最新の位置情報をキャプチャします。この情報を使用して、定義された位置にいたユーザーに基づいてデータをセグメント化できます。

## 位置情報の追跡を有効にする {#enabling-location-tracking}

アプリで位置情報の収集を有効にするには、使用しているプラットフォームの開発者ガイドを参照してください。

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location/?sdktab=web)

一般的に、モバイルアプリはデバイスの GPS チップやその他のシステム（Wi-Fi スキャンなど）を使用してユーザーの位置を追跡します。Web アプリは WPS（Wi-Fi Positioning System）を使用してユーザーの位置を追跡します。これらのプラットフォームはすべて、ユーザーが位置情報の追跡にオプトインする必要があります。位置情報の追跡データの精度は、ユーザーがデバイスで Wi-Fi を有効にしているかどうかによって影響を受ける場合があります。Android ユーザーは異なる位置モードを選択することもできます。「バッテリー節約」または「デバイスのみ」モードのユーザーは、不正確なデータになる可能性があります。

### IP アドレスによる SDK ユーザーの位置情報 {#sdk-user-location-by-ip-address}

Brazeは、最初のSDKセッション開始時のIPアドレスを使用して、ジオロケーションされた国からユーザーの位置を検出します。

以前は、BrazeはSDKユーザー作成時および最初のセッション中にデバイスロケールの国コードを使用していました。最初のセッション開始が処理された後にのみ、IPアドレスがユーザーのより信頼性の高い国の設定に使用されていました。これは、ユーザーの国がより高い精度で設定されるのは、最初のセッション開始が処理された後の2回目のセッション以降のみであったことを意味します。

現在、BrazeはSDKを通じて作成されたユーザープロファイルの国の値を設定するためにIPアドレスを使用しており、そのIPベースの国の設定は最初のセッション中およびその後に利用可能です。

#### 自動位置情報の収集 {#automatic-location-collection}

有効にすると、SDKの自動位置情報の収集はIPベースの国の動作とは別のものです。これは、ユーザーが許可を付与した場合のGPSなどのデバイス位置信号に関連し、`Most Recent Location` などのフィルターを動作させます。IPのみから市区町村などの詳細なフィールドを自動的に入力するものではありません。

市区町村や郵便番号レベルのターゲティングには、[`setLastKnownLocation()`]({{site.baseurl}}/developer_guide/analytics/tracking_location/)（お使いのプラットフォームのSDK記事を参照）、カスタム属性を書き込む独自のIPジオロケーションサービス、または収集したデータを使用した[位置情報ターゲティング]({{site.baseurl}}/user_guide/audience/segments/location_targeting/)を使用してください。

## 位置情報ターゲティング {#location-targeting}

位置情報の追跡データとSegmentsを使用して、位置情報ベースのCampaignと戦略を設定できます。たとえば、特定の地域に住んでいるユーザー向けにプロモーションCampaignを実行したり、より厳しい規制がある地域のユーザーを除外したりすることができます。

位置情報Segmentの作成の詳細については、[位置情報ターゲティング]({{site.baseurl}}/user_guide/audience/segments/location_targeting/)を参照してください。

## デフォルトの位置属性をハード設定する {#hard-setting-the-default-location-attribute}

APIの[`users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、[`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) 標準属性項目を更新することもできます。例を以下に示します。

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## ビーコンとジオフェンスのパートナーシップサポート {#partnership-support-for-beacon-and-geofence}

既存のビーコンまたはジオフェンスサポートとターゲティングおよびメッセージング機能を組み合わせることで、ユーザーの物理的なアクションに関するより多くの情報を得て、それに応じてメッセージを送信できます。一部のパートナーと位置情報の追跡を活用できます。

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

## ジオフェンスと位置情報の追跡の違い {#differences-between-geofences-and-location-tracking}

{% multi_lang_include locations_and_geofences/geofences_vs_location_tracking.md %}

## よくある質問 {#frequently-asked-questions}

### Brazeはいつ位置データを収集しますか？ {#when-does-braze-collect-location-data}

Brazeは、アプリケーションがフォアグラウンドで開いている場合にのみ位置情報を収集します。そのため、`Most Recent Location` フィルターは、ユーザーが最後にアプリケーションを開いた場所（セッション開始とも呼ばれます）に基づいてターゲティングします。

以下のニュアンスにも留意してください。

- 位置情報が無効になっている場合、`Most Recent Location` フィルターは最後に記録された位置を表示します。
- ユーザーのプロファイルに位置情報が保存されたことがある場合、その後位置情報の追跡をオプトアウトしていても、`Location Available` フィルターの条件を満たします。

### Most Recent Device Locale フィルターと Most Recent Location フィルターの違いは何ですか？ {#whats-the-difference-between-the-most-recent-device-locale-and-most-recent-location-filters}

`Most Recent Device Locale` はユーザーのデバイス設定から取得されます。たとえば、iPhone ユーザーの場合、デバイスの**設定** > **一般** > **言語と地域**に表示されます。このフィルターは、日付や住所などの言語と地域のフォーマットをキャプチャするために使用され、`Most Recent Location` フィルターとは独立しています。

`Most Recent Location` は、デバイスの最後の既知の GPS 位置です。これはセッション開始時に更新され、ユーザーのプロファイルに保存されます。

### ユーザーが位置情報の追跡をオプトアウトした場合、以前の位置データは Braze から削除されますか？ {#if-a-user-opts-out-of-location-tracking-is-their-previous-location-data-removed-from-braze}

いいえ。ユーザーのプロファイルに位置情報が保存されたことがある場合、その後位置情報の追跡をオプトアウトしても、そのデータは自動的に削除されません。

## トラブルシューティング {#troubleshooting}

### 利用可能な位置情報を持つユーザーがいない {#no-users-have-available-locations}

BrazeはデフォルトでSDKを通じてユーザーの最新の位置情報をキャプチャします。これは通常、「最新の位置」がユーザーが最後にアプリを使用した位置であることを意味します。Brazeにバックグラウンド位置データを送信している場合、より詳細なデータが利用可能な場合があります。

利用可能な位置情報を持つユーザーがいない場合、2つの簡単なチェックでデータ収集とデータ転送を確認できます。

#### データ収集 {#data-collection}

アプリが位置データを収集していることを確認します。

- iOSの場合、これはユーザーがユーザージャーニーのある時点でプロンプトを通じて位置データの共有にオプトインすることを意味します。
- Androidの場合、アプリがインストール時に精密または大まかな位置情報の権限を要求していることを確認します。

ユーザーの位置データがBrazeに送信されているかどうかを確認するには、**Location Available** フィルターを使用します。このフィルターを使用すると、「最新の位置」を持つユーザーの割合を確認できます。

![「Location Available」フィルターを使用した「Test Location」セグメント。]({% image_buster /assets/img_archive/trouble7.png %})

#### データ転送 {#data-transfer}

開発者が位置データをBrazeに渡していることを確認します。通常、位置データの受け渡しはユーザーが権限を付与した後にSDKによって自動的に処理されますが、開発者がBrazeで位置情報の追跡を無効にしている可能性があります。位置情報の追跡の詳細については、以下を参照してください。
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)