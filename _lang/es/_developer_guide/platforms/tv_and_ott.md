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

La siguiente tabla resume la compatibilidad de canales de mensajería para las plataformas de TV y OTT más comunes. Todas las plataformas también admiten datos y análisis, Canvas y conmutadores de características. Para Kindle Fire, usa las mismas indicaciones que para Amazon Fire TV. Para Apple Vision Pro, consulta la [compatibilidad con visionOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/visionos).

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
<table aria-label="Compatibilidad de canales de mensajería de TV y OTT" id="tv-feature-table">
  <caption>Compatibilidad de canales de mensajería de TV y OTT</caption>
    <thead>
        <tr>
            <th>Tipo de dispositivo</th>
            <th>SDK</th>
            <th>Mensajes dentro de la aplicación</th>
            <th>Content Cards</th>
            <th>Notificaciones push</th>
            <th>Banners</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td><a href="https://github.com/braze-inc/braze-vega-sdk">Vega SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td><a href="https://github.com/braze-inc/braze-android-sdk">Android SDK</a></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">✅</span><span class="sr-only">Compatible</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">No compatible con la plataforma OTT</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">No compatible con la plataforma OTT</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td><a href="https://github.com/braze-inc/braze-roku-sdk">SDK de Roku</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">No compatible con Braze</span></td>
            <td><span aria-hidden="true">➖</span><span class="sr-only">No compatible con la plataforma OTT</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">No compatible con Braze</span></td>
        </tr>
        <tr>
            <td>Apple TV OS (tvOS)</td>
            <td><a href="https://github.com/braze-inc/braze-swift-sdk">Swift SDK</a></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
            <td><span aria-hidden="true">❌</span><span class="sr-only">No compatible con Braze</span></td>
            <td><span aria-hidden="true">🔧</span><span class="sr-only">Solo headless</span></td>
        </tr>
    </tbody>
</table>

- <span aria-hidden="true">✅</span> = Compatible
- <span aria-hidden="true">🔧</span> = Solo headless (necesitarás crear una interfaz de usuario personalizada)
- <span aria-hidden="true">➖</span> = No compatible con la plataforma OTT
- <span aria-hidden="true">❌</span> = No compatible con Braze

## Guías de integración {#integration-guides}

### Amazon Fire TV {#fire-tv}

Utiliza el SDK Braze Fire OS para integrarte con los dispositivos Amazon Fire TV.

Entre sus características se incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Notificaciones push (conocidas como ["Heads Up Notifications"](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup))
  - La prioridad debe configurarse como "HIGH" para que aparezcan. Todas las notificaciones aparecen en el menú de configuración de Fire TV.
- Content Cards
- Conmutadores de características
- Mensajes dentro de la aplicación
  - Para mostrar mensajes HTML en entornos no táctiles como televisores, configura `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` en `false` (disponible a partir de [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación Fire TV.

Para más información, visita la [guía de integración de Fire OS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Kindle Fire {#kindle-fire}

Utiliza el SDK Braze Fire OS para integrarte con los dispositivos Kindle Fire de Amazon.

Entre sus características se incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Notificaciones push
- Content Cards
- Conmutadores de características
- Mensajes dentro de la aplicación
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu Kindle Fire.

Para más información, visita la [guía de integración de Fire OS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Android TV {#android-tv}

Utiliza el SDK para Android de Braze para integrarte con dispositivos Android TV.

Entre sus características se incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Content Cards
- Conmutadores de características
- Mensajes dentro de la aplicación
  - Para mostrar mensajes HTML en entornos no táctiles como televisores, configura `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` en `false` (disponible a partir de [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- &#42; Notificaciones push (requiere integración manual)
  - Las notificaciones push no son compatibles de forma nativa con Android TV. Para saber por qué, consulta las [directrices de diseño](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html) de Google. Sin embargo, puedes **hacer una integración manual de la interfaz de usuario de notificaciones push para conseguirlo**. Consulta nuestra [documentación]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android%20tv) sobre cómo configurarlo.
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación Android TV.

Para más información, visita la [guía de integración del SDK de Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

{% alert note %}
Asegúrate de crear una nueva aplicación Android en el panel para tu integración OTT de Android.
{% endalert %}

### LG webOS {#lg-webos}

Utiliza el SDK Web de Braze para integrarte con [los televisores webOS de LG](https://webostv.developer.lge.com/discover).

Entre sus características se incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Content Cards (a través de [Headless UI](#custom-ui))
- Conmutadores de características
- Mensajes dentro de la aplicación (mediante [Headless UI](#custom-ui))
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación webOS.

Para más información, visita la [guía de integración de Web Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Samsung Tizen {#tizen}

Utiliza el SDK Web de Braze para integrarte con los [televisores Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Entre sus características se incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Content Cards (a través de [Headless UI](#custom-ui))
- Conmutadores de características
- Mensajes dentro de la aplicación (mediante [Headless UI](#custom-ui))
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación Tizen.

Para más información, visita la [guía de integración de Web Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Roku {#roku}

Utiliza el SDK de Roku de Braze para integrarte con [los televisores Roku](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Entre sus características se incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Mensajes dentro de la aplicación (mediante [Headless UI](#custom-ui))
  - Las vistas web no son compatibles con la plataforma Roku, por lo que los mensajes HTML dentro de la aplicación tampoco son compatibles.
- Conmutadores de características

Para más información, visita la [guía de integración de Roku]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=roku).

### Apple TV OS {#tvos}

Utiliza el SDK Swift de Braze para integrarte con tvOS. Ten en cuenta que el SDK Swift no incluye ninguna interfaz ni vistas predeterminadas para tvOS, así que tendrás que implementar las tuyas propias.

Entre sus características se incluyen:

- Recopilación de datos y análisis para la participación multicanal
- Content Cards (a través de [Headless UI](#custom-ui))
- Conmutadores de características
- Mensajes dentro de la aplicación (mediante [Headless UI](#custom-ui))
  - Las vistas web no son compatibles con la plataforma tvOS, por lo que los mensajes HTML dentro de la aplicación tampoco son compatibles.
  - Consulta nuestra [aplicación de ejemplo](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) para saber más sobre cómo utilizar Headless UI para mensajería personalizada en tvOS.
- Notificaciones push silenciosas y actualización de insignias
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación tvOS.

Para obtener más información, visita la [guía de integración del SDK Swift de iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
Para evitar mostrar mensajes dentro de la aplicación móvil a tus usuarios de TV, asegúrate de configurar la [segmentación por aplicaciones](#app-targeting) o de utilizar pares clave-valor para filtrar los mensajes. Por ejemplo, mostrar solo los mensajes de tvOS si contienen un par clave-valor especial `tv = true`.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Utiliza el SDK Swift de Braze para integrarte con visionOS. La mayoría de las características disponibles en iOS también están disponibles en visionOS, entre ellas:

- Análisis (sesiones, eventos personalizados, compras, etc.)
- Mensajería dentro de la aplicación (modelos de datos e interfaz de usuario)
- Content Cards (modelos de datos e interfaz de usuario)
- Notificaciones push (visibles para el usuario con botones de acción y notificaciones silenciosas)
- Conmutadores de características
- Análisis de ubicación
- Banners
  - Usa las [ubicaciones de Banner]({{site.baseurl}}/developer_guide/banners/placements) para insertar mensajes directamente en tu aplicación visionOS.

Para obtener más información, visita la [guía de integración del SDK Swift de iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Algunas características de iOS son parcialmente compatibles o no compatibles. Para ver la lista completa, consulta la [compatibilidad con visionOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/visionos).
{% endalert %}

## Segmentación por aplicaciones {#app-targeting}

Para segmentar las aplicaciones OTT para mensajería, te recomendamos que crees un segmento específico para tu aplicación OTT.

![Un segmento creado utilizando la aplicación OTT de Android.]({% image_buster /assets/img/android_ott.png %})

## Headless UI {#custom-ui}

{% alert important %}
Las plataformas que admiten mensajes dentro de la aplicación o Content Cards a través de Headless UI **no** incluyen ninguna interfaz de usuario ni vistas predeterminadas. Crea tu propia interfaz de usuario personalizada (por ejemplo, para mensajes dentro de la aplicación) y, a continuación, utiliza los modelos de datos proporcionados por el SDK para rellenar esas interfaces de usuario.
{% endalert %}

Con Headless UI, Braze entregará un modelo de datos, como JSON, que tu aplicación puede leer y utilizar dentro de una interfaz de usuario que tu aplicación controla. Estos datos contendrán los campos configurados en el panel (título, cuerpo, texto del botón, colores, etc.) que tu aplicación podrá leer y mostrar en consecuencia. Para más información sobre la gestión personalizada de mensajería, consulta lo siguiente:

**SDK para Android**
- [Personalización de In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android#android_setting-custom-manager-listeners)
- [Personalización de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)

**SDK Swift**
- [Personalización de In-App Messages](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Aplicación de ejemplo de Headless UI](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Personalización de Content Cards](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**SDK Web**
- [Personalización de In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web)
- [Personalización de Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)