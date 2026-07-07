---
nav_title: Integración de balizas
article_title: Integración de balizas para iOS
platform: iOS
page_order: 4
description: "Este artículo trata sobre el registro de eventos personalizados utilizando Infillion Beacons para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración de balizas {#beacon-integration}

Aquí veremos cómo integrar tipos específicos de balizas con Braze para permitir la segmentación y la mensajería.

## Balizas Infillion {#infillion-beacons}

Una vez que hayas configurado tus balizas Infillion e integrado en tu aplicación, podrás registrar eventos personalizados, como el inicio o el final de una visita, o la detección de una baliza. También puedes registrar propiedades de estos eventos, como el nombre del lugar o el tiempo de permanencia.

Para registrar un evento personalizado cuando un usuario entra en un lugar, introduce este código en el método `didBeginVisit`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

`flushDataAndProcessRequestQueue` confirma que tu evento se registrará aunque la aplicación esté en segundo plano, y el mismo proceso puede aplicarse para abandonar una ubicación. Ten en cuenta que esto creará e incrementará un evento personalizado único para cada nuevo lugar en el que entre el usuario. Si prevés crear más de 50 lugares, te recomendamos que crees un evento personalizado genérico "Place Entered" e incluyas el nombre del lugar como propiedad del evento.