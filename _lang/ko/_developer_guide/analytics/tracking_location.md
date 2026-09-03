---
nav_title: 위치 추적
article_title: 위치 추적
page_order: 3.4
description: "Braze SDK를 통해 위치를 추적하는 방법을 알아보세요."
---

# 위치 추적 {#track-location}

> Braze SDK를 통해 위치를 추적하는 방법을 알아보세요.

{% sdktabs %}
{% sdktab web %}
## 현재 위치 로깅하기 {#logging-the-current-location}

사용자의 현재 위치를 가져오려면 지리 위치 API의 [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) 메서드를 사용합니다. 이렇게 하면 사용자에게 추적을 허용하거나 허용하지 않을지 묻는 메시지가 즉시 표시됩니다(이미 허용하지 않은 경우).

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

이제 데이터가 Braze로 전송되면 SDK에서 IP 주소를 사용하여 사용자의 국가를 자동으로 감지할 수 있습니다. 자세한 내용은 [setLastKnownLocation()](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation)을 참조하세요.

## 지속적인 위치 추적 {#continuously-tracking-the-location}

페이지 로드 중에 사용자의 위치를 지속적으로 추적하려면 지리 위치 API의 [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) 메서드를 사용합니다. 이 메서드를 호출하면 사용자에게 추적을 허용하거나 허용하지 않을지 묻는 메시지가 즉시 표시됩니다(이미 허용하지 않은 경우).

옵트인하면 위치가 업데이트될 때마다 성공 콜백이 호출됩니다.

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
연속 추적을 비활성화하는 방법을 알아보려면 [Mozilla 개발자 문서](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition)를 참조하세요.
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