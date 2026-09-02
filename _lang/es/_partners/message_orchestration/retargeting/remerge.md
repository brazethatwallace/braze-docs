---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "Este artículo de referencia describe la asociación entre Braze y Remerge, una aplicación diseñada específicamente para la reorientación a gran escala, que te proporciona herramientas para segmentar eficazmente las audiencias de las aplicaciones y reorientar a los usuarios."
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/) se ha creado específicamente para la reorientación de aplicaciones a gran escala, y te proporciona herramientas para segmentar eficazmente las audiencias de las aplicaciones y reorientar a los usuarios.

_Esta integración está mantenida por Remerge._

## Sobre la integración {#about-the-integration}

La integración de Braze y Remerge te ayuda a desarrollar sólidas campañas de marketing de ciclo de vida en canales cruzados mediante el envío de datos de usuario a Remerge a través de eventos webhook para ayudar a reorientar a los usuarios a través de su plataforma de demanda móvil.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta Remerge | Se necesita una cuenta Remerge para beneficiarse de esta asociación. |
| Clave de webhook de Remerge | Esta clave será proporcionada por Remerge. |
| ID de la aplicación Android | Tu identificador único de aplicación Braze para Android (como "com.example"). |
| ID de la aplicación iOS | Tu identificador único de aplicación Braze para iOS (como "012345678"). |
| Habilitar la recopilación de IDFA en el SDK or kit de desarrollo de software de Braze | La recopilación de IDFA es opcional dentro del SDK or kit de desarrollo de software de Braze y está desactivada de forma predeterminada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Crea tu plantilla de webhook en Braze {#step-1-create-your-braze-webhook-template}

Para crear una plantilla de webhook de Remerge para futuras Campaigns o Canvas, ve a **Content** > **Webhook** en la plataforma Braze. Luego, selecciona **Create webhook template**.


Si deseas crear una Campaign de webhook de Remerge única o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva Campaign.

En tu nueva plantilla de webhook, rellena los siguientes campos:
- **Request Body**: Raw Text
- **Webhook URL**:
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

En la URL del webhook, debes:
- Utilizar la API `https://remerge.events/event` para enviar tus eventos webhook.
- Establecer el nombre del evento. Este nombre aparecerá en tu dashboard de [remerge.io](https://www.remerge.io/).
- Pasar a Remerge el identificador único de tu aplicación para Android (como "com.example") e iOS (como "012345678").
- Definir una clave; Remerge te la proporcionará.

![La URL del webhook y la vista previa del mensaje mostrados en el constructor de webhook de Braze.]({% image_buster /assets/img_archive/webhook_remerge_preview.png %})

{% alert important %}
Braze no recopila automáticamente el IDFA/AAID del dispositivo, por lo que debes almacenar estos valores tú mismo. Ten en cuenta que puedes necesitar el consentimiento del usuario para recopilar estos datos.
{% endalert %}

#### Encabezados de solicitud y método {#request-headers-and-method}

El webhook de Remerge requiere un método HTTP y un encabezado de solicitud.

- **HTTP Method**: GET
- **Request Headers**:
  - **Content-Type**: application/json

![Los encabezados de solicitud, el método HTTP y la vista previa del mensaje mostrados en el constructor de webhook de Braze.]({% image_buster /assets/img_archive/httpmethod_remerge.png %})

#### Cuerpo de la solicitud {#request-body}

No es necesario definir un cuerpo de solicitud para este webhook.

## Paso 2: Previsualiza tu solicitud {#step-2-preview-your-request}

Previsualiza el mensaje para asegurarte de que la solicitud se muestra correctamente para los distintos usuarios. Recomendamos previsualizar y enviar solicitudes de prueba tanto para usuarios de Android como de iOS. Si la solicitud es correcta, la API responderá con `HTTP 204`.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas de webhook actualizadas pueden encontrarse en la lista **Plantillas de Webhook guardadas** al crear una nueva [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/).
{% endalert %}