---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "Este artículo de referencia describe la asociación entre Braze y Jampp, una plataforma de marketing del rendimiento utilizada para captar y reorientar clientes móviles."
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/) es una plataforma de marketing del rendimiento utilizada para captar y reorientar clientes móviles. Jampp combina datos de comportamiento con tecnología predictiva y programática para generar ingresos para los anunciantes mostrando anuncios personales y relevantes que inspiran a los consumidores a comprar por primera vez o más a menudo.

_Esta integración está mantenida por Jampp._

## Sobre la integración {#about-the-integration}

La integración de Braze y Jampp permite a los usuarios de la empresa sincronizar eventos en Jampp a través de eventos webhook de Braze. Como resultado, los clientes pueden añadir conjuntos de datos más ricos a sus iniciativas de reorientación dentro de sus ecosistemas de publicidad móvil.

Algunos ejemplos de casos en los que querrías reorientar a los clientes con un anuncio:
- Cuando cambia el estado de suscripción de correo electrónico o push de un cliente.
- Cómo interactuó un cliente con una campaña de mensajería de Braze.
- Si el cliente ha desencadenado una geovalla específica.

## Requisitos previos {#prerequisites}

Esta integración es compatible con aplicaciones iOS y Android.

| Requisito | Descripción |
|---|---|
| Cuenta Jampp | Se necesita una [cuenta Jampp](https://www.jampp.com/) para beneficiarse de esta asociación. |
| ID de la aplicación Android | Tu identificador único de aplicación Braze para Android (como "com.example"). |
| ID de la aplicación iOS | Tu identificador único de aplicación Braze para iOS (como "012345678"). |
| Habilitar la recopilación de IDFA en el SDK de Braze | La recopilación de IDFA es opcional dentro del SDK de Braze y está desactivada por defecto. |
| Recopilación del identificador de publicidad de Google mediante un atributo personalizado | La recopilación del ID de publicidad de Google es opcional para los clientes y puede recogerse como un [atributo personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crear una plantilla de webhook en Braze {#step-1-create-a-webhook-template-in-braze}

Para crear una plantilla de webhook de Jampp y utilizarla en futuras Campaigns o Canvas, ve a **Contenido** > **Webhook** en el dashboard de Braze. Luego, selecciona **Crear plantilla de webhook**.

Si deseas hacer una Campaign de webhook de Jampp única o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva Campaign.

En tu nueva plantilla de webhook, rellena los siguientes campos:
- **Request Body**: Raw Text
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

En la URL del webhook, debes:
- Establecer el nombre del evento. Este nombre aparecerá en tu dashboard de Jampp.
- Pasar el identificador único de tu aplicación para Android (como "com.example") e iOS (como "012345678").
- Insertar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid) para el atributo personalizado adecuado que estés rastreando como ID de publicidad de Google. Ten en cuenta que el ID de publicidad de Google aparece como `aaid` en este ejemplo, pero tendrás que sustituirlo por el nombre de atributo personalizado que establezcan tus desarrolladores.

![La URL del webhook y la vista previa del mensaje mostrados en el constructor de webhook de Braze.]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
Braze no recopila automáticamente el IDFA/AAID del dispositivo, por lo que debes almacenar estos valores tú mismo. Ten en cuenta que puedes necesitar el consentimiento del usuario para recopilar estos datos.
{% endalert %}

#### Encabezados de solicitud y método {#request-headers-and-method}

El webhook de Jampp requiere un método HTTP y un encabezado de solicitud.

- **Método HTTP**: GET
- **Encabezados de solicitud**:
  - **Content-Type**: application/json

![Los encabezados de solicitud, el método HTTP y la vista previa del mensaje mostrados en el constructor de webhook de Braze.]({% image_buster /assets/img/jampp_method.png %})

#### Cuerpo de la solicitud {#request-body}

No es necesario definir un cuerpo de solicitud para este webhook.

### Paso 2: Previsualizar tu solicitud {#step-2-preview-your-request}

Previsualiza el mensaje para asegurarte de que la solicitud se muestra correctamente para los distintos usuarios. Recomendamos previsualizar y enviar solicitudes de prueba tanto para usuarios de Android como de iOS. Si la solicitud es correcta, la API responderá con `HTTP 204`.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas de webhook actualizadas pueden encontrarse en la lista **Plantillas de Webhook guardadas** al crear una nueva [campaña de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}