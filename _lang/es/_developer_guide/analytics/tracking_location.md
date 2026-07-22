---
nav_title: Seguimiento de ubicación
article_title: Seguimiento de la ubicación a través del SDK de Braze
page_order: 3.4
description: "Aprende a realizar el seguimiento de la ubicación a través del SDK de Braze."

---

# Seguimiento de la ubicación {#track-location}

> Aprende a realizar el seguimiento de la ubicación a través del SDK de Braze.

{% sdktabs %}
{% sdktab web %}
## Registro de la ubicación actual {#logging-the-current-location}

Para obtener la ubicación actual de un usuario, utiliza el método [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) de la API de geolocalización. Esto pedirá inmediatamente al usuario que permita o rechace el seguimiento (a menos que ya lo haya hecho).

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

Ahora, cuando se envían datos a Braze, el SDK puede detectar automáticamente el país del usuario utilizando su dirección IP. Para más información, consulta [setLastKnownLocation()](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation).

## Seguimiento continuo de la ubicación {#continuously-tracking-the-location}

Para hacer un seguimiento continuo de la ubicación de un usuario durante la carga de una página, utiliza el método [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) de la API de geolocalización. Al llamar a este método, se pedirá inmediatamente al usuario que permita o rechace el seguimiento (a menos que ya lo haya hecho).

Si acepta la adhesión voluntaria, se invocará una devolución de llamada de éxito cada vez que se actualice su ubicación.

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
Para aprender a desactivar el seguimiento continuo, consulta la [documentación para desarrolladores de Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition).
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