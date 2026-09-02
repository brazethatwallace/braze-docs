---
nav_title: Televisión y OTT
article_title: Integraciones de TV y OTT para Braze
page_order: 15

description: "Este artículo te dará detalles sobre las características, integraciones, plataformas disponibles y otras capacidades de Braze TV y OTT."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# Integraciones de TV y OTT {#tv-and-ott-integrations}

> A medida que la tecnología evoluciona hacia nuevas plataformas y dispositivos, ¡también puede hacerlo tu mensajería con Braze! Braze ofrece diferentes canales de participación para varios sistemas operativos de televisión y métodos de entrega de contenido Over-the-Top (OTT).

## Plataformas y características {#platforms-and-features}

La siguiente tabla resume la compatibilidad de los canales de mensajería para plataformas comunes de TV y OTT. Todas las plataformas también son compatibles con datos y análisis, Canvas y conmutadores de características. Para Kindle Fire, usa las mismas indicaciones que para Amazon Fire TV. Para Apple Vision Pro, consulta [Compatibilidad con visionOS]({{site.baseurl}}/developer_guide/platforms/swift/visionos).

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center;
    vertical-align: middle;
    word-break: normal;
    overflow-wrap: normal;
    hyphens: none;
}

#tv-feature-table td:first-child,
#tv-feature-table th:first-child {
    text-align: left;
}

</style>
<table aria-label="Compatibilidad de canales de mensajería para TV y OTT" id="tv-feature-table">
  <caption>Compatibilidad de canales de mensajería para TV y OTT</caption>
    <thead>
        <tr>
            <th>Tipo de dispositivo</th>
            <th>SDK or kit de desarrollo de software</th>
            <th>In-App Messages</th>
            <th>Content Cards</th>
            <th>Notificaciones push</th>
            <th>Banners</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td><a href="https://github.com/braze-inc/braze-vega-sdk">Vega SDK or kit de desarrollo de software</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td><a href="https://github.com/braze-inc/braze-android-sdk">Android SDK or kit de desarrollo de software</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK or kit de desarrollo de software</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">No compatible con la plataforma OTT</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK or kit de desarrollo de software</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">No compatible con la plataforma OTT</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td><a href="https://github.com/braze-inc/braze-roku-sdk">SDK or kit de desarrollo de software de Roku</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">No compatible con Braze</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">No compatible con la plataforma OTT</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">No compatible con Braze</span></td>
        </tr>
        <tr>
            <td>Apple TV OS (tvOS)</td>
            <td><a href="https://github.com/braze-inc/braze-swift-sdk">Swift SDK or kit de desarrollo de software</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">No compatible con Braze</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
    </tbody>
</table>

- <span aria-hidden="true">✅</span> = Compatible
- <span aria-hidden="true">🔧</span> = Solo headless (necesitarás crear una interfaz personalizada)
- <span aria-hidden="true">➖</span> = No compatible con la plataforma OTT
- <span aria-hidden="true">❌</span> = No compatible con Braze

## Guías de integración {#integration-guides}

### Amazon Fire TV {#fire-tv}

Usa el SDK or kit de desarrollo de software de Braze Fire OS para integrarlo con dispositivos Amazon Fire TV.

Las características incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Notificaciones push (conocidas como ["Notificaciones Heads Up"](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup))
  - La prioridad debe establecerse en "HIGH" para que aparezcan. Todas las notificaciones aparecen en el menú de configuración de Fire TV.
- Content Cards
- Conmutadores de características
- Mensajes dentro de la aplicación
  - Para mostrar mensajes HTML en entornos no táctiles como televisores, establece `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` en `false` (disponible a partir del [SDK or kit de desarrollo de software de Android v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación de Fire TV.

Para obtener más información, visita la [guía de integración de Fire OS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Kindle Fire {#kindle-fire}

Usa el SDK or kit de desarrollo de software de Braze Fire OS para integrarlo con dispositivos Amazon Kindle Fire.

Las características incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Notificaciones push
- Content Cards
- Conmutadores de características
- Mensajes dentro de la aplicación
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu Kindle Fire.

Para obtener más información, visita la [guía de integración de Fire OS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Android TV {#android-tv}

Usa el SDK or kit de desarrollo de software de Android de Braze para integrarlo con dispositivos Android TV.

Las características incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Content Cards
- Conmutadores de características
- Mensajes dentro de la aplicación
  - Para mostrar mensajes HTML en entornos no táctiles como televisores, establece `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` en `false` (disponible a partir del [SDK or kit de desarrollo de software de Android v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- &#42; Notificaciones push (se requiere integración manual)
  - Las notificaciones push no son compatibles de forma nativa en Android TV. Para saber por qué, consulta las [directrices de diseño](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html) de Google. Sin embargo, puedes **realizar una integración manual de la interfaz de notificaciones push para lograrlo**. Consulta nuestra [documentación]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android%20tv) sobre cómo configurar esto.
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación de Android TV.

Para obtener más información, visita la [guía de integración del SDK or kit de desarrollo de software de Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

{% alert note %}
Asegúrate de crear una nueva aplicación de Android en el panel para tu integración de Android OTT.
{% endalert %}

### LG webOS {#lg-webos}

Usa el SDK or kit de desarrollo de software Web de Braze para integrarlo con [televisores LG webOS](https://webostv.developer.lge.com/discover).

Las características incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Content Cards (a través de [interfaz sin cabecera](#custom-ui))
- Conmutadores de características
- Mensajes dentro de la aplicación (a través de [interfaz sin cabecera](#custom-ui))
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación webOS.

Para obtener más información, visita la [guía de integración Web para Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Samsung Tizen {#tizen}

Usa el SDK or kit de desarrollo de software Web de Braze para integrarlo con [televisores Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Las características incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Content Cards (a través de [interfaz sin cabecera](#custom-ui))
- Conmutadores de características
- Mensajes dentro de la aplicación (a través de [interfaz sin cabecera](#custom-ui))
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación Tizen.

Para obtener más información, visita la [guía de integración Web para Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Roku {#roku}

Usa el SDK or kit de desarrollo de software de Roku de Braze para integrarlo con [televisores Roku](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Las características incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Mensajes dentro de la aplicación (a través de [interfaz sin cabecera](#custom-ui))
  - La plataforma Roku no admite vistas web, por lo que los mensajes HTML dentro de la aplicación no son compatibles.
- Conmutadores de características

Para obtener más información, visita la [guía de integración de Roku]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=roku).

### Apple TV OS {#tvos}

Usa el SDK or kit de desarrollo de software Swift de Braze para integrarlo con tvOS. Ten en cuenta que el SDK or kit de desarrollo de software Swift no incluye ninguna interfaz ni vista predeterminada para tvOS, por lo que necesitarás implementar las tuyas propias.

Las características incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Content Cards (a través de [interfaz sin cabecera](#custom-ui))
- Conmutadores de características
- Mensajes dentro de la aplicación (a través de [interfaz sin cabecera](#custom-ui))
  - La plataforma tvOS no admite vistas web, por lo que los mensajes HTML dentro de la aplicación no son compatibles.
  - Consulta nuestra [aplicación de ejemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) para aprender más sobre cómo usar una interfaz sin cabecera para mensajería personalizada en tvOS.
- Notificaciones push silenciosas y actualización de insignias
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación tvOS.

Para obtener más información, visita la [guía de integración del SDK or kit de desarrollo de software Swift de iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
Para evitar mostrar mensajes dentro de la aplicación para dispositivos móviles a tus usuarios de TV, asegúrate de configurar la [segmentación por aplicación](#app-targeting) o usar pares clave-valor para filtrar los mensajes. Por ejemplo, mostrar solo los mensajes de tvOS si contienen un par clave-valor especial `tv = true`.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Usa el SDK or kit de desarrollo de software Swift de Braze para integrarlo con visionOS. La mayoría de las características disponibles en iOS también están disponibles en visionOS, incluyendo:

- Análisis (sesiones, eventos personalizados, compras, etc.)
- In-App Messages (modelos de datos e interfaz)
- Content Cards (modelos de datos e interfaz)
- Notificaciones push (visibles para el usuario con botones de acción y notificaciones silenciosas)
- Conmutadores de características
- Análisis de ubicación
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación visionOS.

Para obtener más información, visita la [guía de integración del SDK or kit de desarrollo de software Swift de iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Algunas características de iOS son parcialmente compatibles o no son compatibles. Para ver la lista completa, consulta [compatibilidad con visionOS]({{site.baseurl}}/developer_guide/platforms/swift/visionos).
{% endalert %}

## Segmentación por aplicaciones {#app-targeting}

Para segmentar las aplicaciones OTT para mensajería, te recomendamos que crees un segmento específico para tu aplicación OTT.

![Un segmento creado utilizando la aplicación OTT de Android.]({% image_buster /assets/img/android_ott.png %})

## Headless UI {#custom-ui}

{% alert important %}
Las plataformas que admiten mensajes dentro de la aplicación o Content Cards a través de Headless UI **no** incluyen ninguna interfaz de usuario ni vistas predeterminadas. Crea tu propia interfaz de usuario personalizada (por ejemplo, para mensajes dentro de la aplicación) y, a continuación, utiliza los modelos de datos proporcionados por el SDK or kit de desarrollo de software para rellenar esas interfaces de usuario.
{% endalert %}

Con Headless UI, Braze entregará un modelo de datos, como JSON, que tu aplicación puede leer y utilizar dentro de una interfaz de usuario que tu aplicación controla. Estos datos contendrán los campos configurados en el panel (título, cuerpo, texto del botón, colores, etc.) que tu aplicación podrá leer y mostrar en consecuencia. Para más información sobre la gestión personalizada de mensajería, consulta lo siguiente:

**SDK or kit de desarrollo de software para Android**
- [Personalización de In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android#android_setting-custom-manager-listeners)
- [Personalización de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)

**SDK or kit de desarrollo de software Swift**
- [Personalización de In-App Messages](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Aplicación de ejemplo de Headless UI](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Personalización de Content Cards](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**SDK or kit de desarrollo de software Web**
- [Personalización de In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web)
- [Personalización de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)