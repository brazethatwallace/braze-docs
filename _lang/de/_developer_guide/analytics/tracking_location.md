---
nav_title: Standort verfolgen
article_title: Standort verfolgen
page_order: 3.4
description: "Erfahren Sie, wie Sie Standorte mit dem Braze SDK tracken können."
---

# Standort verfolgen {#track-location}

> Erfahren Sie, wie Sie Standorte mit dem Braze SDK tracken können.

{% sdktabs %}
{% sdktab web %}
## Aufzeichnung des aktuellen Standorts {#logging-the-current-location}

Um den aktuellen Standort einer Nutzer:in zu ermitteln, verwenden Sie die Geolocation-API-Methode [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition). Dadurch wird die Nutzer:in sofort aufgefordert, das Tracking zuzulassen oder zu verbieten (sofern dies nicht bereits geschehen ist).

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

Wenn nun Daten an Braze gesendet werden, kann das SDK das Land der Nutzer:in anhand der IP-Adresse automatisch erkennen. Für weitere Informationen siehe [setLastKnownLocation()](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation).

## Kontinuierliches Tracking des Standorts {#continuously-tracking-the-location}

Um den Standort einer Nutzer:in während des Ladens einer Seite kontinuierlich zu verfolgen, verwenden Sie die Geolocation-API-Methode [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition). Der Aufruf dieser Methode fordert die Nutzer:in sofort auf, das Tracking zuzulassen oder zu verbieten (sofern dies nicht bereits geschehen ist).

Wenn die Nutzer:in per Opt-in zustimmt, wird bei jeder Aktualisierung des Standorts ein Erfolgs-Callback ausgelöst.

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
Um zu erfahren, wie Sie das kontinuierliche Tracking deaktivieren können, lesen Sie die [Mozilla-Entwicklerdokumentation](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition).
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