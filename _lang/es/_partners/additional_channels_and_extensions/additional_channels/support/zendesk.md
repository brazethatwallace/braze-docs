---
nav_title: Zendesk
article_title: Zendesk
description: "Este artículo de referencia describe la asociación entre Braze y Zendesk, una popular línea de productos de soporte que te permite utilizar webhooks de Braze para sincronizar los datos de soporte entre las dos plataformas."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) ofrece a las empresas la posibilidad de mantener conversaciones naturales con sus clientes a través del soporte omnicanal mediante correo electrónico, webchat, voz o aplicaciones de mensajería social. Zendesk ofrece un sistema de creación de tickets optimizado que valora el seguimiento y la priorización de las interacciones, lo que permite a las empresas tener una visión histórica unificada de sus clientes.

La integración de servidor a servidor de Braze y Zendesk te permite utilizar:
- Webhooks de Braze para automatizar la creación de tickets de soporte en Zendesk a partir de la interacción con mensajes en los recorridos de usuario en Braze. Por ejemplo, después de implementar y probar con éxito una integración, Braze puede crear un ticket de soporte a partir de un usuario que responda negativamente a un mensaje dentro de la aplicación del tipo "¿Te gusta nuestra app?", lo que permite a tu equipo de soporte hacer seguimiento con el cliente.
- Webhooks de Zendesk para admitir casos de uso bidireccionales, como la actualización del perfil de usuario en Braze a partir de la actividad en Zendesk. Por ejemplo, después de resolver un ticket, registrar un evento en el perfil del usuario en Braze.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta de Zendesk | Se requiere una [cuenta de administrador de Zendesk](https://`<your-zendesk-instance>`.zendesk.com/agent/admin) para aprovechar esta asociación. |
| Token de la API de Zendesk | Se necesita un [token de API](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\) de Zendesk para enviar solicitudes desde Braze al punto de conexión de tickets de Zendesk. |
| Identificador común (recomendado) | Se recomienda un [identificador común](#common-identifier) entre Braze y Zendesk. |
| Clave de API de Braze | Se necesita una clave de API de Braze para enviar solicitudes desde Zendesk a un punto de conexión de Braze. Asegúrate de que la clave de API que utilizas tiene los permisos correctos para el punto de conexión de Braze que utiliza tu webhook de Zendesk. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración de Braze con Zendesk {#braze-to-zendesk-integration}

### Paso 1: Crea tu webhook de Braze {#step-1-create-your-braze-webhook}

Para crear un webhook:

- **Campaigns:** Ve a la página **Campaigns** en el dashboard de Braze. Haz clic en **Create Campaign** y selecciona **Webhook**.
- **Canvas:** Desde un Canvas nuevo o existente, crea un paso completo o de mensaje en el constructor de Canvas. A continuación, haz clic en **Messages** y selecciona **Webhook** en las opciones de mensaje.

En tu webhook, rellena los siguientes campos:
- **Webhook URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Request Body**: Raw Text

Otros casos de uso pueden gestionarse a través de las [API de soporte de Zendesk](https://developer.zendesk.com/rest_api/docs/support/introduction), que cambiarían en consecuencia el punto de conexión `/api/v2/` al final de la URL del webhook.

#### Encabezado y método de la solicitud {#request-header-and-method}

Zendesk requiere un encabezado HTTP para la autorización y un método HTTP. En la pestaña **Settings**, sustituye <email_address> por tu correo electrónico de administrador de Zendesk y <api_token> por tu token de la API de Zendesk.

- **HTTP Method**: POST
- **Request Headers**:
  - **Authorization**: Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### Cuerpo de la solicitud {#request-body}

Define los detalles del ticket como tipo, asunto y estado en la carga útil de tu webhook. Los detalles de los tickets se pueden ampliar y personalizar basándose en la [API de tickets de Zendesk](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket). Utiliza el siguiente ejemplo como ayuda para estructurar tu carga útil e introduce los campos que desees.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}",
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### Paso 2: Previsualiza tu solicitud {#step-2-preview-your-request}

Tu texto sin procesar se resaltará automáticamente si es una etiqueta de Braze aplicable.

Previsualiza tu solicitud en el panel de **Preview** o navega hasta la pestaña **Test**, donde puedes seleccionar un usuario aleatorio o un usuario existente, o personalizar el tuyo propio para probar tu webhook.

Por último, comprueba si el ticket se ha creado en el lado de Zendesk.

## Identificador común {#common-identifier}

Si tienes un identificador común entre Braze y Zendesk, se recomienda utilizarlo como `requester_id`. Esto ayudará a unificar los dos conjuntos de usuarios. Alternativamente, si este no es el caso, recomendamos pasar un conjunto de atributos identificativos como nombre, dirección de correo electrónico, número de teléfono u otros.

## Integración de Zendesk con Braze {#zendesk-to-braze-integration}

### Paso 1: Crea un webhook {#step-1-create-a-webhook}

1. En el [Centro de administración](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), haz clic en **Apps and integrations** en la barra lateral y, a continuación, selecciona **Webhooks > Webhooks**.<br><br>
2. Haz clic en **Create webhook**.<br><br>
3. Selecciona **Trigger** o **Automation** y haz clic en **Next**.<br>![]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Proporciona la siguiente información en tu webhook:
- Introduce un nombre y una descripción para el webhook.
- Introduce la URL del punto de conexión de Braze que utilizará tu webhook. {% raw %}En nuestro ejemplo utilizaremos `https://{{instance_url}}/users/track`.{% endraw %}
- Selecciona POST como método de solicitud del webhook y establece el formato de solicitud en JSON.
- Selecciona el método de autenticación de token de portador para el webhook y proporciona tu [clave de API de Braze]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys).
  - Asegúrate de que la clave de API que utilizas tiene los [permisos correctos]({{site.baseurl}}/api/basics/#rest-api-key-permissions) para el punto de conexión de Braze que utiliza tu webhook.<br><br>
5. (Recomendado) Prueba el webhook para comprobar que funciona correctamente.<br><br>
6. Para los webhooks de desencadenamiento y automatización, debes conectar el webhook a un desencadenador o automatización antes de finalizar la configuración. Consulta el paso siguiente para ver nuestro ejemplo de creación de un desencadenador para el webhook. Una vez creado el desencadenador, puedes volver a esta página y seleccionar **Finish setup**.

### Paso 2: Crea un desencadenador o automatización {#step-2-create-a-trigger-or-automation}

[Sigue las instrucciones de Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb) sobre cómo conectar tu webhook a un desencadenador o automatización.

Nuestro ejemplo a continuación utilizará un desencadenador para invocar el webhook cuando el estado de un caso de soporte haya cambiado a "Resuelto" o "Cerrado".

1. En el **Centro de administración**, haz clic en **Objects and rules** en la barra lateral y, a continuación, selecciona **Business rules > Triggers**.<br><br>
2. Selecciona **Add trigger**.<br><br>
3. Asigna un nombre a tu desencadenador y selecciona una categoría.<br><br>
4. Selecciona **Add condition** para configurar qué condiciones deben desencadenar el webhook. Por ejemplo, "Status category changed to closed" o "Status category changed to solved".![]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. Selecciona **Add action**, elige **Notify active webhook** y selecciona del desplegable el webhook creado en el paso anterior.<br><br>
6. Define el cuerpo JSON para que se ajuste a tu punto de conexión de Braze, usando marcadores de posición de variables de Zendesk para rellenar dinámicamente los campos relevantes.<br>![]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. Selecciona **Create**.<br><br>
8. Vuelve a tu webhook y haz clic en **Finish setup**.