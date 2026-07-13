---
nav_title: Regal
article_title: Regal
description: "Este artículo de referencia describe la asociación entre Braze y Regal, una plataforma de agentes de IA de voz que te ayuda a orquestar recorridos del cliente personalizados y omnicanal utilizando datos de Braze y conversaciones de Regal."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) es una plataforma de agentes de IA de voz que ayuda a las empresas a impulsar mejores experiencias del cliente a través de conversaciones inteligentes y en tiempo real en todos los canales.

_Esta integración es mantenida por Regal._

Al integrar Regal con Braze, puedes unificar datos de comportamiento e IA conversacional para orquestar recorridos del cliente personalizados y omnicanal. Braze captura señales a lo largo del ciclo de vida del cliente, que Regal utiliza para potenciar conversaciones con agentes de IA, enrutamiento y decisiones en tiempo real.

Usa datos de Braze para dar forma a lo que dicen tus agentes de IA, cómo responden y cuándo interactuar. Envía resultados de conversaciones e información de vuelta a Braze para mejorar la segmentación y el marketing del ciclo de vida. Desencadena llamadas y SMS impulsados por IA en momentos clave del recorrido del cliente, y haz seguimiento en Braze en función de lo que ocurra en cada conversación.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Regal | Se necesita una cuenta Regal para beneficiarse de esta asociación. |
| Clave de API de Regal | Una clave de API de Regal te permite enviar eventos de Braze a Regal.<br><br>Envía un correo electrónico a [support@regal.io](mailto:support@regal.io) para obtener esta clave. |
| Transformación de datos de Braze | Se requiere una [Transformación de datos]({{site.baseurl}}/data_transformation) para recibir datos de Regal. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración: envío de datos de Braze a Regal {#integration-sending-data-from-braze-to-regal}

Usa webhooks de Canvas o Campaign de Braze para enviar datos de perfil de cliente y eventos de Braze a Regal.

### Paso 1: Crear nuevos contactos en Regal {#step-1-create-new-contacts-in-regal}

Crea un Canvas o una Campaign que envíe webhooks a Regal cada vez que crees un nuevo perfil de Braze que deba estar disponible para llamadas y mensajes de texto en Regal.

1. Crea un Canvas o una Campaign con el título "Crear nuevo contacto para Regal" y selecciona **Basado en acciones** como tipo de entrada.

2. Establece la lógica de desencadenamiento como **Evento personalizado** y selecciona el evento que se dispara cuando se crea un perfil con un número de teléfono. Regal también recomienda añadir un filtro para confirmar que el campo de teléfono está configurado.

3. En tu nueva plantilla de webhook, rellena los siguientes campos:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **Request Body**: Raw Text

#### Encabezados de solicitud y método {#request-headers-and-method}

Regal también requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya está incluido en la plantilla como pares clave-valor en la pestaña **Settings**:
{% raw %}
- **HTTP Method**: POST
- **Request Headers**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud {#request-body}

El único identificador obligatorio es un número de teléfono dentro de `traits.phones`. Usa el objeto `traits.phones` para asociar uno o más números de teléfono con un contacto. Cada número de teléfono puede almacenar su propia etiqueta, designación principal y estado de adhesión voluntaria para voz y SMS. Esta estructura es especialmente útil cuando un contacto tiene múltiples números de teléfono.

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "custom1": "<custom1>",
    "custom2": "<custom2>"
  },
  "eventSource": "braze"
}
```

El ejemplo de carga útil anterior supone que los números de teléfono listados incluyen el estado actual de consentimiento para voz y SMS. Si no es así, puedes omitir `voiceOptIn` y `smsOptIn` al crear el contacto y configurar un Canvas o una Campaign independiente para actualizar el consentimiento en el número de teléfono correspondiente cuando se recopile la adhesión voluntaria.

### Paso 2: Actualizar la información de adhesión voluntaria {#step-2-update-opt-in-information}

Si la adhesión voluntaria y la exclusión pueden producirse en diferentes puntos de tu aplicación, actualiza Regal cuando los usuarios cambien su estado de suscripción.

Regal recomienda usar el esquema `traits.phones` para que puedas gestionar la adhesión voluntaria y la exclusión por número de teléfono, en lugar de a nivel de contacto.

Usa la siguiente configuración de Canvas para enviar información actualizada de adhesión voluntaria a Regal.

1. Crea un nuevo Canvas o una nueva Campaign con el título "Enviar adhesión voluntaria o baja a Regal".

2. Selecciona una de las siguientes opciones de desencadenamiento y selecciona el campo que represente el estado de adhesión voluntaria del usuario:
    - **Campo de perfil de usuario actualizado**
    - **Actualizar el estado del grupo de suscripción**
    - **Estado de la suscripción**

3. En tu nueva plantilla de webhook, rellena los siguientes campos:
   - **Webhook URL**: <https://events.regalvoice.com/events>
   - **Request Body**: Raw Text

#### Encabezados de solicitud y método

Regal también requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya está incluido en la plantilla como pares clave-valor en la pestaña **Settings**:
{% raw %}
- **HTTP Method**: POST
- **Request Headers**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<phoneNumber>": {
        "voiceOptIn": {
          "subscribed": "<voice_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": "<sms_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    }
  },
  "eventSource": "braze"
}
```

También puedes incluir atributos adicionales del perfil de usuario en esta carga útil para mantener otros atributos actualizados al mismo tiempo.

### Paso 3: Enviar eventos personalizados {#step-3-send-custom-events}

Configura un Canvas o una Campaign para cada evento clave que quieras enviar a Regal.

Estos eventos hacen más que desencadenar comunicaciones (por ejemplo, un mensaje de texto de confirmación cuando un lead completa el registro). Proporcionan el contexto en tiempo real que impulsa cómo los agentes de IA de Regal hablan, toman decisiones y enrutan conversaciones a lo largo del recorrido del cliente. Al enviar datos de eventos y atributos desde Braze, permites que los agentes de IA adapten las conversaciones en función del comportamiento, las preferencias y la etapa del ciclo de vida de cada usuario.

Por ejemplo, los eventos y atributos de Braze se pueden usar en Regal para:

- **Personalizar el discurso del agente de IA**: hacer referencia al comportamiento reciente o al interés en un producto directamente en las conversaciones.
  - Ejemplo: si un usuario exploró opciones de seguro de vida, el agente puede hacer referencia a `contact.firstName` y `contact.brazeProductInterest` en la conversación.
- **Impulsar la lógica dinámica de la conversación**: ajustar lo que el agente prioriza en tiempo real.
  - Ejemplo: si `contact.brazeAge` es mayor de 65, priorizar la cobertura de Medicare; de lo contrario, centrarse en los planes ACA y el estado actual del seguro.
- **Habilitar el enrutamiento y la escalación inteligentes**: enrutar conversaciones en función del valor o la intención.
  - Ejemplo: si `contact.brazeLeadTier` es "High Value", transferir a un agente senior después de la calificación; de lo contrario, continuar con el agente de IA.
- **Alinear mensajes y ofertas**: adaptar lo que el agente presenta en función del contexto de la campaña.
  - Ejemplo: si `contact.brazeCampaignName` es "Spring Mortgage Promo", destacar la oferta promocional durante la conversación.

Crea un nuevo Canvas o una nueva Campaign con el título "Enviar evento de interés en producto a Regal".

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "brazeProductInterest": "Life Insurance",
    "brazeAge": 68,
    "brazeLeadTier": "High Value",
    "brazeCampaignName": "Spring Insurance Promo"
  },
  "name": "Product Interest Captured",
  "properties": {
    "action": "Viewed Product Comparison",
    "productCategory": "Life Insurance",
    "intentScore": "High",
    "lastPage": "Compare Life Insurance Plans",
    "readyToCommit": true
  },
  "eventSource": "braze"
}
```

#### Atributos de contacto actualizados {#up-to-date-contact-attributes}

Regal también recomienda enviar atributos clave del perfil de usuario en las cargas útiles de eventos para que Regal tenga atributos de contacto actualizados cuando ocurran eventos clave.

{% alert note %}
Si tienes preguntas sobre qué eventos enviar a Regal o cómo configurar estos Canvas y Campaigns, envía un correo electrónico a [support@regal.io](mailto:support@regal.io).
{% endalert %}

## Integración: envío de datos de Regal a Braze {#integration-sending-data-from-regal-to-braze}

Usa los webhooks de informes de Regal y la Transformación de datos de Braze para enviar eventos de informes de Regal (como `SMS.sent` y `call.completed`) a Braze. Después de mapear estos eventos, aparecen en los perfiles de usuario y están disponibles para segmentación, Canvas y Campaigns.

### Paso 1: Crear una Transformación de datos en Braze {#step-1-create-a-data-transformation-in-braze}

Crea una Transformación de datos por cada webhook de Regal que planees enviar a Braze.

Para crear una Transformación de datos:
1. Ve a la página **Transformations** en tu panel de Braze.
2. Dale un nombre a tu transformación y haz clic en **Create transformation**.
3. En la lista de transformaciones, selecciona <i class="fa-solid fa-ellipsis-vertical" title="Ver acciones"></i> **Ver acciones** y selecciona **Copy webhook URL**.

### Paso 2: Habilitar webhooks de informes en Regal {#step-2-enable-reporting-webhooks-in-regal}

Para configurar webhooks de informes:
1. Ve a la aplicación Regal y abre la página de **Settings**.

2. En la sección **Reporting Webhooks**, haz clic en **Create Webhooks**.

3. En la entrada del endpoint del webhook, añade la URL del webhook de Transformación de datos de Braze para la Transformación de datos asociada.

#### Actualización de un endpoint {#updating-an-endpoint}

Cuando editas un endpoint, la caché puede tardar hasta 5 minutos en actualizarse y enviar eventos a tu nuevo endpoint.

#### Reintentos {#retries}

Actualmente, Regal no reintenta estos eventos. Si Braze no responde en 5 segundos, Regal descarta el evento. Regal planea añadir reintentos en una futura versión.

#### Eventos {#events}
Para la lista completa de eventos de informes, definiciones de propiedades y ejemplos de cargas útiles, consulta la [guía de webhooks de informes](https://developer.regal.io/docs/reporting-webhooks#events) de Regal.

### Paso 3: Transformar los eventos de Regal en eventos de Braze {#step-3-transform-regal-events-into-braze-events}

La característica de [Transformación de datos]({{site.baseurl}}/data_transformation) de Braze te permite mapear los eventos entrantes de Regal en el formato necesario para añadirlos como atributos, eventos o compras en Braze.

1. Dale un nombre a tu Transformación de datos. Se recomienda configurar una Transformación de datos por webhook de evento.

2. Para probar la conexión, crea una llamada saliente desde el escritorio del agente de Regal a tu teléfono y envía el formulario de resumen de conversación para crear un evento `call.completed`.

3. Determina qué identificadores utilizarás para mapear tus contactos de Regal a tus perfiles de Braze. Los identificadores disponibles en los eventos de Regal incluyen:
   - `userId` - solo se establece en eventos si previamente se ha enviado este identificador para un contacto
   - `traits.phone`
   - `traits.email` - solo se establece en eventos si previamente se ha enviado este identificador para un contacto

En las cargas útiles de eventos de Braze a Regal, Regal recomienda usar `traits.phones` para admitir múltiples números de teléfono y consentimiento a nivel de teléfono. En los eventos de informes de Regal enviados de vuelta a Braze, `traits.phone` puede seguir apareciendo como identificador en las cargas útiles de eventos.

#### Identificadores compatibles con Braze {#braze-supported-identifiers}
- Braze no admite números de teléfono como identificador. Para utilizarlo como identificador, el número de teléfono puede configurarse como [alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) en Braze.
- Al utilizar la Transformación de datos de Braze, la dirección de correo electrónico puede utilizarse como identificador. Si la dirección de correo electrónico existe como perfil en Braze, se actualizará el perfil existente. Si la dirección de correo electrónico aún no existe en Braze, se creará un perfil solo para correo electrónico.

## Ejemplos {#use-cases}

{% tabs %}
{% tab Trigger an email %}

**Desencadenar un correo electrónico de Braze basado en una disposición de llamada en Regal**

A continuación se muestra un ejemplo de carga útil para un evento `call.completed` en Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Alex",
    "agent_fullname": "Alex Lee",
    "agent_id": "xxxx@example.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+15555550200",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+15555550123",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

A continuación se muestra un ejemplo de Transformación de datos para mapear esto a un evento personalizado en Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Update profile attributes %}

**Actualizar los atributos del perfil en Braze basándote en los eventos `contact.attribute.edited` de Regal**

A continuación se muestra un ejemplo de carga útil para un evento `contact.attribute.edited` en Regal. Regal envía este evento cuando un agente actualiza un atributo en el perfil de un contacto durante una conversación.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@example.com",
    "contact_phone": "+15555550123",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

A continuación se muestra un ejemplo de Transformación de datos para mapear los nuevos valores de propiedades personalizadas a los atributos pertinentes de tus perfiles de Braze:

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Keep your experiments in sync %}

**Mantén sincronizados tus experimentos en Braze y Regal mediante eventos `contact.experiment.assigned`**

A continuación se muestra un ejemplo de carga útil para un evento `contact.experiment.assigned` en Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

A continuación se muestra un ejemplo de Transformación de datos para mapear esto a un evento personalizado en Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab Unsubscribe a contact %}

**Cancelar la suscripción de un contacto en Braze basándote en un evento `contact.unsubscribed` de Regal**

A continuación se muestra un ejemplo de carga útil para un evento `contact.unsubscribed` en Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

A continuación se muestra un ejemplo de Transformación de datos para cancelar la suscripción del contacto en Braze.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Trigger follow-up from call analysis %}

**Desencadenar recorridos de seguimiento personalizados en Braze basándote en eventos `call.analysis.available` de Regal**

Usa el evento `call.analysis.available` de Regal para identificar la razón principal por la que un cliente no convirtió y desencadenar un recorrido de seguimiento personalizado en Braze.

Por ejemplo:

- Cuando la objeción principal es el precio, envía un correo electrónico de seguimiento orientado al valor.
- Cuando la objeción principal es el momento, coloca al usuario en una secuencia de nurturing para una reconsideración posterior.
- Cuando la objeción principal es la confianza, envía testimonios, calificaciones o garantías de cumplimiento.
- Cuando `needs_human_agent` es verdadero, notifica a un equipo de ventas o soporte y suprime los mensajes automatizados adicionales.

A continuación se muestra un ejemplo de carga útil para un evento `call.analysis.available` en Regal.

```json
{
  "traits": {
    "phone": "+1XXXXXXXXXX",
    "email": "xxx@example.com"
  },
  "name": "call.analysis.available",
  "brand": "circle-bank",
  "contact_email": "xxx@example.com",
  "contact_phone": "+1XXXXXXXXXX",
  "created_at": "1754079836",
  "entity_type": "event",
  "event_id": "9f5d8dbb2973b0e2359c6fd34111111",
  "event_type": "regal_voice_event",
  "external_id": "41dd1aa2-1111-f011-a2d5-00505611111",
  "original_timestamp": "1754079835",
  "profile_id": "62653af1111111173af128291e92",
  "properties": {
    "agent_email": "xxx@example.com",
    "call_analysis": {
      "purchase_intent": "medium",
      "primary_objection": "price",
      "secondary_objection": "needs_to_compare",
      "product_interest": "Life Insurance",
      "follow_up_required": true,
      "follow_up_email_text": "Thanks for speaking with us today. I know cost is top of mind, so I wanted to send over a simple summary of the life insurance options we discussed and what may fit your budget.",
      "recommended_next_action": "send_value_oriented_follow_up",
      "needs_human_agent": false,
      "customer_sentiment_label": "interested_but_hesitant"
    },
    "contact_phone": "+1XXXXXXXXXX",
    "incoming_sip_headers": {
      "Via": "SIP/2.0/UDP srv1.example.com;branch=z9hG4bK776asdhds",
      "From": "<sip:customer@example.com>;tag=1928301774",
      "Call-ID": "a84b4c76e66710"
    },
    "is_ai_agent": true,
    "outgoing_sip_headers": {
      "Via": "SIP/2.0/TCP srv2.example.com;branch=z9hG4bKgsdh7723",
      "To": "<sip:agent@example.com>",
      "User-Agent": "RegalVoiceAI/1.0"
    },
    "task_id": "WT7f3ea47fa6e6055aa847f0a62111111"
  },
  "originalTimestamp": "1754079835",
  "source": "Regal Voice"
}
```

Usa una Transformación de datos para mapear los campos de `call_analysis` (como `primary_objection` y `needs_human_agent`) a eventos personalizados o atributos de perfil de Braze. Luego construye la lógica de Canvas o Campaign en Braze que se ramifique en función de esos valores.

{% endtab %}
{% tab Store call transcript links %}

**Actualizar atributos del perfil con enlaces de transcripción de eventos `call.transcript.available`**

Usa el evento `call.transcript.available` para enviar un enlace a la transcripción completa de la llamada a Braze. Mapea la URL de la transcripción a un atributo del perfil de usuario de Braze con la Transformación de datos para que tu equipo pueda acceder y revisar las conversaciones desde el perfil de usuario.

A continuación se muestra un ejemplo de carga útil para un evento `call.transcript.available` en Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.transcript.available",
  "properties": {
    "agent_email": "xxx@example.com",
    "task_id": "WT953358e8822dd9333fc38dfbac25e1e1",
    "call_summary": "The agent Yuri explained insurance options to Alex and he said he'll need to think about it before moving forward Agent politely ended the call.",
    "contact_name": "Alex Smith",
    "contact_phone": "+15555550123",
    "is_voicemail": false,
    "moments_count": 18,
    "recording_id": "RE0118052841b7299d0630d1dff610c1fb",
    "recording_link": "https://api.twilio.com/2010-04-01/Accounts/ACxxx/Recordings/xxx.mp3",
    "recording_duration": 78.75987,
    "request_timestamp": 1657799128,
    "response_timestamp": 1657799136,
    "sentiments": {
      "contact_sentiment": 70,
      "agent_sentiment": 75,
      "agent_sentiment_reason": "Yuri was polite and attentive, effectively gathering information and providing a resource, which contributed to a positive interaction.",
      "contact_sentiment_reason": "Alex was satisfied with the information provided but may have wanted more assistance regarding insurance options."
    },
    "trackers": [
      {
        "tracker_id": "4be87957-9140-4451-894a-bdbaed1f2460",
        "tracker_name": "Refinance"
      },
      {
        "tracker_id": "eb2577c6-5e23-4c65-9e04-5cc5d49eee7e",
        "tracker_name": "High Intent"
      }
    ],
    "transcript": "[handling agent]: Hi Alex, this is Yuri with BrightCover Insurance. I'll be going over some insurance options with you today. [contact]: Sounds good. [handling agent]: Before we start, I'm going to transfer you to a specialist for a moment. One sec. [transfer agent]: Hi Alex, this is Lee. Just verifying a few details before sending you back to Yuri. [contact]: Okay. [handling agent]: Thanks, Alex. Based on what you shared, here are some plan options... [contact]: I'll need to think about it. [handling agent]: Totally understandable. Feel free to reach out anytime. Have a great day! END OF TRANSCRIPT",
    "transcript_is_truncated": false,
    "transcript_url": "https://app.regalvoice.com/transcripts/WT953358e8822dd9333fc38dfbac25e1e1"
  },
  "originalTimestamp": "1657843308",
  "eventSource": "Regal Voice",
  "eventId": "f49a3cf9cb1336683bd5f19dwe4c61147"
}
```

{% endtab %}
{% endtabs %}