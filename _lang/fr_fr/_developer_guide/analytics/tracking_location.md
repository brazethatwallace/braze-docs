---
nav_title: Suivi de l'emplacement/localisation
article_title: Suivi de l'emplacement/localisation
page_order: 3.4
description: "Découvrez comment suivre l'emplacement/localisation à l'aide du SDK Braze."
---

# Suivi de l'emplacement/localisation {#track-location}

> Découvrez comment suivre l'emplacement/localisation à l'aide du SDK Braze.

{% sdktabs %}
{% sdktab web %}
## Enregistrement de l'emplacement/localisation actuel {#logging-the-current-location}

Pour obtenir l'emplacement/localisation actuel d'un utilisateur, utilisez la méthode [`getCurrentPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition) de l'API de géolocalisation. L'utilisateur sera immédiatement invité à autoriser ou à refuser le suivi (à moins qu'il ne l'ait déjà fait).

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

Désormais, lorsque des données sont envoyées à Braze, le SDK peut automatiquement détecter le pays de l'utilisateur à l'aide de son adresse IP. Pour plus d'informations, consultez [setLastKnownLocation()](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setlastknownlocation).

## Suivi continu de l'emplacement/localisation {#continuously-tracking-the-location}

Pour suivre en continu l'emplacement/localisation d'un utilisateur pendant le chargement d'une page, utilisez la méthode [`watchPosition()`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition) de l'API de géolocalisation. L'appel de cette méthode invite immédiatement l'utilisateur à autoriser ou à refuser le suivi (à moins qu'il ne l'ait déjà fait).

S'il accepte, un rappel de succès est invoqué chaque fois que son emplacement/localisation est mis à jour.

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
Pour savoir comment désactiver le suivi continu, consultez la [documentation développeur Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/watchPosition).
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