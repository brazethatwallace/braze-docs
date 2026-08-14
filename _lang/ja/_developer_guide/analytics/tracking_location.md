---
nav_title: 位置情報の追跡
article_title: Braze SDKを通じて位置情報の追跡を行う
page_order: 3.4
description: "Braze SDKで位置情報を追跡する方法について説明します。"

---

# 位置情報の追跡 {#track-location}

> Braze SDKで位置情報を追跡する方法について説明します。

{% sdktabs %}
{% sdktab web %}
## 現在地を記録する {#logging-the-current-location}

ユーザーの現在地を取得するには、ジオロケーションAPIの[`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition)メソッドを使用します。これにより、ユーザーはトラッキングを許可するかしないかを即座に選択することになります（すでに許可している場合を除く）。

```javascript
import * as braze from "@braze/web-sdk";
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.getCurrentPosition(success);
```

Brazeにデータが送信される際、SDKはユーザーのIPアドレスからユーザーの国を自動的に検出できます。詳細については、[setLastKnownLocation()](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation)を参照してください。

## 位置情報の継続的な追跡 {#continuously-tracking-the-location}

ページの読み込み中にユーザーの位置情報を継続的に追跡するには、ジオロケーションAPIの[`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition)メソッドを使用します。このメソッドを呼び出すと、ユーザーにトラッキングの許可または不許可を即座に促します（すでに許可している場合を除く）。

ユーザーがオプトインすると、位置情報が更新されるたびに成功コールバックが呼び出されます。

```javascript
function success(position) {
  var coords = position.coords;
  braze.getUser().setLastKnownLocation(
    coords.latitude,
    coords.longitude,
    coords.accuracy,
    coords.altitude,
    coords.altitudeAccuracy
  );
}

navigator.geolocation.watchPosition(success);
```

{% alert important %}
継続的なトラッキングを無効にする方法については、[Mozilla開発者向けドキュメント](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition)を参照してください。
{% endalert %}

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/analytics/tracking_location.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/tracking_location.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/analytics/tracking_location.md %}
{% endsdktab %}
{% endsdktabs %}