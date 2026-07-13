---
nav_title: Front
article_title: Front
description: "Aprende a integrar Front con Braze"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> La integración de Front te permite aprovechar la Transformación de datos de Braze y los webhooks de cada plataforma para establecer un canal SMS conversacional bidireccional.

El webhook entrante de Front contendrá una carga útil que incluye el mensaje enviado por el agente en vivo. Será necesario reformatear la solicitud antes de que pueda ser aceptada por los endpoints de Braze. La plantilla de Transformación de datos de Front reformateará la carga útil y escribirá un evento personalizado en el perfil de usuario titulado **Outbound SMS Sent**, pasando el cuerpo del mensaje como una propiedad del evento.

Antes de configurar una nueva transformación en Braze, recomendamos revisar la matriz de soporte para cada nivel en nuestra documentación de [Transformación de datos]({{site.baseurl}}/user_guide/data/unification/data_transformation). Nuestros niveles Free y Pro ofrecen un número diferente de transformaciones activas y solicitudes entrantes al mes. Confirma que el plan en el que estás actualmente puede admitir tu caso de uso.

## Requisitos previos {#prerequisites}

Antes de empezar, necesitarás lo siguiente:

| Requisito | Descripción |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Una cuenta de Front | Se necesita una cuenta de Front para beneficiarse de esta asociación. |
| URL de webhook de Transformación de datos de Braze | La [Transformación de datos de Braze]({{site.baseurl}}/user_guide/data/unification/data_transformation) se utilizará para reformatear el webhook entrante desde Front, de modo que pueda ser aceptado por el endpoint /users/track de Braze. |
| Una clave de API REST de Front | Se utilizará una clave de API REST de Front para realizar una solicitud de webhook saliente de Braze a Front. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Ejemplos {#use-cases}

- Agiliza tu proceso de generación de clientes potenciales utilizando la mensajería SMS automatizada de Braze para identificar las preferencias de los usuarios y permitir a los agentes de ventas en vivo realizar el seguimiento y cerrar las ventas.
- Reactiva a los clientes que abandonaron sus carritos de la compra impulsando las conversiones de ventas mediante respuestas automatizadas por SMS y asistencia por chat en vivo.

## Integración de Front {#integrating-front}

### Paso 1: Crear una transformación de datos {#step-1-create-a-data-transformation}

Primero, crearás una nueva transformación de datos en Braze. Los pasos siguientes están simplificados; para un recorrido completo, consulta [Crear una transformación]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation).

1. En Braze, ve a **Configuración de datos** > **Transformaciones de datos** y, a continuación, selecciona **Crear transformación**.
2. En **Experiencia de edición**, selecciona **Empezar desde cero**.
3. En **Seleccionar destino**, selecciona **POST: Track Users**.
4. Copia y pega la siguiente plantilla de transformación, luego guárdala y activa el endpoint.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    Tu transformación debe reflejar el ejemplo de JavaScript de esta sección, ajustando nombres de propiedades y rutas para que coincidan con la carga útil del webhook de Front.

{% alert tip %}
Puedes modificar esta plantilla para adaptarla a tus necesidades específicas. Por ejemplo, puedes personalizar el nombre preestablecido del evento personalizado. Para más información, consulta [Resumen de la transformación de datos]({{site.baseurl}}/user_guide/data/unification/data_transformation).
{% endalert %}

### Paso 2: Crear una campaña de SMS salientes {#step-2-create-an-outbound-sms-campaign}

A continuación, crearás una campaña de SMS que escuchará los webhooks de Front y enviará una respuesta personalizada por SMS a tus clientes.

#### Paso 2.1: Redacta tu mensaje {#step-21-compose-your-message}

En el cuadro de texto **Message**, añade el siguiente código Liquid, junto con cualquier texto de exclusión u otro contenido estático.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

Tu mensaje debe ser similar al siguiente:

![Un mensaje de ejemplo utilizando código Liquid.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 Programar la entrega {#22-schedule-the-delivery}

Para el tipo de entrega, selecciona **Entrega basada en acciones**; a continuación, para el desencadenante del evento personalizado, selecciona **Outbound SMS Sent**.

![La página "Programar entrega".]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
Este evento personalizado es la Transformación de datos que escribe en el perfil del usuario. Los mensajes del agente se guardarán como una propiedad del evento en este evento.
{% endalert %}

Por último, en **Controles de entrega**, habilita la posibilidad de volver a ser elegible.

![Reelegibilidad habilitada en "Controles de entrega".]({% image_buster /assets/img/front/braze_reeligibility.png %})

### Paso 3: Crear un canal personalizado {#step-3-create-a-custom-channel}

En el panel de Front, ve a **Settings** > **Channels** > **Add Channels** y, a continuación, selecciona **Custom Channel** e introduce un nombre para tu nuevo canal de Braze.

![Un canal personalizado para Braze en el panel de Front.]({% image_buster /assets/img/front/front_custom_channel.png %})

### Paso 4: Configura los ajustes {#step-4-configure-the-settings}

En el campo del endpoint de la API de salida, introduce la URL de webhook de Transformación de datos [que creaste anteriormente](#step-1-set-up-a-data-transformation-in-braze). Todos los mensajes salientes de los agentes en vivo de tu nuevo canal de Braze se enviarán aquí. Este canal también proporciona una URL de endpoint para que Braze reenvíe los mensajes SMS en el campo **Incoming URL**.

Toma nota de esta URL&#8212;la necesitarás más adelante.

![La configuración del canal para el canal de Braze recién creado en Front.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### Paso 5: Configurar el reenvío de SMS entrantes {#step-5-set-up-inbound-sms-forwarding}

A continuación, crearás dos nuevas campañas webhook en Braze para poder reenviar los SMS entrantes de los clientes al buzón de entrada de Front.

| Número | Propósito |
|---|---|
| Campaña webhook 1 | Señala a Front que se está solicitando una conversación de chat en vivo. |
| Campaña webhook 2 | Reenvía todas las respuestas SMS conversacionales enviadas por el cliente al buzón de entrada de Front. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 5: Configurar el reenvío de SMS entrantes" }

#### Paso 5.1: Crear una categoría de palabras clave SMS {#step-51-create-an-sms-keyword-category}

En el panel de Braze, ve a **Audiencia**, elige tu **grupo de suscripción SMS** y, a continuación, selecciona **Añadir palabra clave personalizada**. Para crear una categoría de palabras clave SMS exclusiva para Front, rellena los siguientes campos.

| Campo | Descripción |
|---|---|
| Categoría de palabras clave | El nombre de tu categoría de palabras clave, como `FrontSMS1`. |
| Palabras clave | Tus palabras clave personalizadas, como `TIMETOMOW`. Evita las palabras comunes para evitar desencadenamientos accidentales. Ten en cuenta que las palabras clave no distinguen entre mayúsculas y minúsculas, por lo que `lawn` coincidiría con `LAWN`. |
| Mensaje de respuesta | El mensaje que se enviará cuando se detecte una palabra clave, como "Un paisajista se pondrá en contacto contigo en breve". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 5.1: Crear una categoría de palabras clave SMS" }

![Un ejemplo de categoría de palabras clave SMS en Braze.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### Paso 5.2: Crea tu primera campaña webhook {#step-52-create-your-first-webhook-campaign}

En el panel de Braze, crea tu primera campaña webhook utilizando la URL [que creaste anteriormente](#step-3-configure-the-settings-for-your-new-custom-braze-channel).

![Un ejemplo de la primera campaña webhook que debe crearse en Braze.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

Añade lo siguiente al cuerpo de tu solicitud:

{% raw %}
```liquid
{
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

En la pestaña de configuración, configura tus encabezados de solicitud `Authorization`, `content-type` y `accept`.

![Un ejemplo de solicitud con los tres encabezados requeridos.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### Paso 5.3: Programar la primera entrega {#step-53-schedule-the-first-delivery}

Para **Programar entrega**, selecciona **Entrega basada en acciones** y, a continuación, elige **Enviar un mensaje SMS entrante** para tu tipo de desencadenante. Añade también el grupo de suscripción SMS y la categoría de palabras clave que [configuraste anteriormente](#step-51-create-an-sms-keyword-category).

![La página "Programar entrega" de la primera campaña webhook.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

En **Controles de entrega**, habilita la posibilidad de volver a ser elegible.

![Reelegibilidad seleccionada en "Controles de entrega" para la primera campaña webhook.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### Paso 5.4: Crea tu segunda campaña webhook {#step-54-create-your-second-webhook-campaign}

Como tu segunda campaña webhook coincide con la primera, puedes [duplicar la primera y cambiarle el nombre]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-or-campaigns).

#### Paso 5.5: Programar la segunda entrega {#step-55-schedule-the-second-delivery}

Para **Programar entrega**, establece el **desencadenante basado en acciones** y el **grupo de suscripción SMS** igual que [en tu primera entrega](#step-53-schedule-the-first-delivery). Sin embargo, para la **categoría de palabras clave**, elige **Other**.

![La página "Programar entrega" de la segunda campaña webhook, con "Other" elegida como categoría de palabras clave.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### Paso 5.6: Añadir un filtro de audiencia {#step-56-add-an-audience-filter}

Tu campaña webhook ahora puede reenviar las respuestas SMS entrantes de tus clientes. Para filtrar las respuestas SMS de modo que solo se reenvíen los mensajes de los chats en vivo, añade el filtro de segmentación **Last Received Message From Specific Campaign** al paso **Público objetivo**.

![Un filtro de audiencia con "Last Received Message From Specific Campaign" seleccionado.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

Después configura tu filtro:

1. En **Campaign**, selecciona la campaña de SMS [que creaste anteriormente](#step-2-create-an-outbound-sms-campaign).
2. En **Operator**, selecciona **Less Than**.
3. En **Time Window**, elige el tiempo que debe permanecer abierto un chat sin respuesta del cliente.

![Los ajustes de configuración del filtro de audiencia seleccionado.]({% image_buster /assets/img/front/front_target_audience.png %})

## Consideraciones {#considerations}

### Segmentos facturables {#billable-segments}

- Los mensajes SMS en Braze se cobran por segmento del mensaje. Entender qué define un segmento y cómo se dividirán estos mensajes es clave para comprender cómo se te facturarán los mensajes. Consulta más información en nuestra [documentación]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).
- Las respuestas largas de los agentes consumirán más segmentos facturables.

### Registro de puntos de datos {#logging-data-points}

Actualmente, esta integración requiere que se escriba un evento personalizado en un perfil de usuario cada vez que un agente en vivo envía un SMS desde Front. Esto puede ser adecuado para intercambios rápidos que solo duren un par de mensajes, pero a medida que las conversaciones se alargan, también lo hacen las implicaciones de los puntos de datos. Si tienes preguntas sobre los matices de los puntos de datos de Braze, tu director de cuentas de Braze puede responderlas.

### Incluir enlaces en los mensajes SMS {#including-links-in-sms-messages}

El envío de un enlace desde el chat en vivo de Front se mostrará con etiquetas HTML adicionales.

### Adjuntar archivo de imagen desde Front {#attaching-image-file-from-front}

Los archivos de imagen en Front no se mostrarán en los mensajes SMS enviados desde Braze.

### Exclusiones voluntarias {#opt-outs}

Los mensajes conversacionales tienen un mayor riesgo de contener la palabra "stop" o expresiones similares que pueden reconocerse como exclusiones difusas.