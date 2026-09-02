---
nav_title: Rastrear local
article_title: Rastrear local
page_order: 3.4
description: "Aprenda como rastrear local através do SDK or kit de desenvolvimento de software da Braze."
---

# Rastrear local {#track-location}

> Aprenda como rastrear local através do SDK or kit de desenvolvimento de software da Braze.

{% sdktabs %}
{% sdktab web %}
## Registro do local atual {#logging-the-current-location}

Para obter o local atual de um usuário, use o método [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) da API or interface de programação do aplicativo (API) de geolocalização. Isso solicitará imediatamente que o usuário permita ou não o rastreamento (a menos que já o tenha feito).

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

Agora, quando os dados são enviados ao Braze, o SDK or kit de desenvolvimento de software pode detectar automaticamente o país do usuário usando seu endereço IP. Para saber mais, consulte [setLastKnownLocation()](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation).

## Monitoramento contínuo da localização {#continuously-tracking-the-location}

Para monitorar continuamente o local de um usuário durante o carregamento de uma página, use o método [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) da API or interface de programação do aplicativo (API) de geolocalização. A chamada desse método solicitará imediatamente que o usuário permita ou não o rastreamento (a menos que já o tenha feito).

Se houver aceitação, um retorno de chamada de sucesso será invocado sempre que o local for atualizado.

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
Para saber como desativar o monitoramento contínuo, consulte a [documentação para desenvolvedores da Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition).
{% endalert %}

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/analytics/tracking_location.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/tracking_location.md %}
{% endsdktab %}

{% sdktab React Native %}
{% multi_lang_include developer_guide/react_native/analytics/tracking_location.md %}
{% endsdktab %}
{% endsdktabs %}