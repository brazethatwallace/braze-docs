---
nav_title: Google Tag Manager
article_title: Google Tag Manager con el SDK de Braze
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Aprende a inicializar el SDK de Braze utilizando métodos como la inicialización en tiempo de ejecución, la inicialización diferida o Google Tag Manager."

---

# Google Tag Manager con el SDK de Braze {#google-tag-manager-with-the-braze-sdk}

> Aprende a utilizar [Google Tag Manager (GTM)](https://developers.google.com/tag-platform/tag-manager) con el SDK de Braze, para que puedas controlar de forma remota el seguimiento de eventos y las actualizaciones de atributos de usuario de Braze sin necesidad de realizar cambios en el código ni lanzar nuevas versiones de la aplicación.

{% sdktabs %}
{% sdktab web %}
## Acerca de Google Tag Manager para Web {#google-tag-manager}

Google Tag Manager (GTM) te permite añadir, eliminar y editar etiquetas de forma remota en tu sitio web sin necesidad de liberar código de producción ni recursos de ingeniería. Braze ofrece las siguientes plantillas para el SDK Web:

| Tipo de etiqueta | Caso de uso |
|--------|--------|
| Etiqueta de inicialización | Esta etiqueta te permite [integrar el SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sin necesidad de modificar el código de tu sitio. |
| Etiqueta de acción | Esta etiqueta te permite [crear Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [establecer atributos de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) y [administrar la recopilación de datos]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Acerca de Google Tag Manager para Web" }

## Secuenciación de etiquetas para las etiquetas de acción de Braze {#tag-sequencing-for-braze-action-tags}

Los eventos personalizados y otras etiquetas de acción de Braze pueden fallar cuando se activan antes de que la etiqueta **Braze Initialization** termine de cargar el SDK Web. En Google Tag Manager, abre la etiqueta de acción, ve a **Advanced Settings** > **Tag Sequencing**, selecciona **A tag that fires before [this tag] is fired** y elige tu etiqueta de inicialización de Braze.

Para más detalles, consulta [Verificar la secuenciación de etiquetas para eventos personalizados]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing).

## Registrar compras con GTM {#log-purchases-with-gtm}

En las etiquetas de acción de Braze y las etiquetas HTML personalizadas, llama a `braze.logPurchase()` para registrar ingresos. El espacio de nombres heredado `appboy.logPurchase()` no es compatible con las integraciones actuales del SDK Web.

## Registrar eventos personalizados con GTM {#logging-custom-events-with-gtm}

Puedes registrar eventos personalizados utilizando una etiqueta **Custom HTML** en GTM. Este enfoque utiliza la [capa de datos](https://developers.google.com/tag-platform/tag-manager/datalayer) de GTM para pasar datos de eventos desde tu sitio a una etiqueta de GTM que llama al SDK Web de Braze.

### Paso 1: Enviar el evento a la capa de datos {#step-1-push-the-event-to-the-data-layer}

En el código de tu sitio, envía un evento a la capa de datos donde quieras desencadenar el evento personalizado. Por ejemplo, para registrar un evento personalizado cuando se hace clic en un botón:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Paso 2: Crear un desencadenante en GTM {#step-2-create-a-trigger-in-gtm}

1. En tu contenedor de GTM, ve a **Triggers** y crea un nuevo desencadenante.
2. Establece el **Trigger Type** en **Custom Event**.
3. Establece el **Event Name** con el mismo valor que enviaste a la capa de datos (por ejemplo, `my_custom_event`).
4. Elige cuándo debe activarse el desencadenante (por ejemplo, **All Custom Events**).

### Paso 3: Crear una etiqueta HTML personalizada {#step-3-create-a-custom-html-tag}

1. En GTM, ve a **Tags** y crea una nueva etiqueta.
2. Establece el **Tag Type** en **Custom HTML**.
3. En el campo HTML, añade lo siguiente:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. En **Triggering**, selecciona el desencadenante que creaste en el paso 2.
5. Guarda y publica tu contenedor.

Para incluir propiedades del evento, pásalas como segundo argumento:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Política de consentimiento de usuarios de la UE de Google {#googles-eu-user-consent-policy}

{% alert important %}
Google está actualizando su [Política de consentimiento de usuarios de la UE](https://www.google.com/about/company/user-consent-policy/) en respuesta a los cambios en la [Ley de Mercados Digitales (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que está en vigor desde el 6 de marzo de 2024. Este nuevo cambio requiere que los anunciantes divulguen cierta información a sus usuarios finales del EEE y del Reino Unido, así como que obtengan los consentimientos necesarios de ellos. Consulta la siguiente documentación para obtener más información.
{% endalert %}

Como parte de la Política de consentimiento de usuarios de la UE de Google, los siguientes atributos personalizados booleanos deben registrarse en los perfiles de usuario:

- `$google_ad_user_data`
- `$google_ad_personalization`

Si estableces estos valores a través de la integración de GTM, los atributos personalizados requieren crear una etiqueta HTML personalizada. A continuación se muestra un ejemplo de cómo registrar estos valores como tipos de datos booleanos (no como cadenas):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Para más información, consulta [Audience Sync con Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync).

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## Solución de problemas {#troubleshooting}

Si Braze no se inicializa o los eventos no aparecen como se esperaba, confirma que tu contenedor de GTM está publicado, que los desencadenantes y el orden de activación de las etiquetas están alineados con el [ciclo de vida y la estrategia de inicialización]({{site.baseurl}}/developer_guide/sdk_integration) de tu SDK, y que los dispositivos de prueba no están bloqueando los endpoints de Braze.

Para fallos de inicialización, verifica que la etiqueta de Braze o el proveedor de etiquetas personalizado reciba el `actionType` y los parámetros esperados (consulta las pestañas de Android, Swift y Web en esta página). Para habilitar el registro detallado mientras validas los eventos activados por GTM, activa el registro de depuración del SDK de tu plataforma como se describe en las guías de integración de plataforma enlazadas desde esas pestañas.