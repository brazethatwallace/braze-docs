---
nav_title: Quikly
article_title: Quikly
description: "Este artículo de referencia describe la asociación entre Braze y Quikly, una plataforma de marketing de urgencia, que te permite acelerar las conversiones en eventos dentro de un recorrido del cliente de Braze."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Quikly

> [Quikly](https://www.quikly.com), una plataforma de marketing de urgencia, utiliza la psicología para motivar a los consumidores, de modo que las marcas puedan aumentar inmediatamente la respuesta en torno a sus iniciativas clave de marketing.

_Esta integración está mantenida por Quikly._

## Sobre la integración {#about-the-integration}

La asociación entre Braze y Quikly te permite acelerar las conversiones en eventos dentro de un recorrido del cliente de Braze. Quikly lo consigue utilizando la psicología de la urgencia para motivar a los consumidores de forma divertida e instantánea. Por ejemplo, las marcas pueden utilizar Quikly para captar inmediatamente nuevos suscriptores de correo electrónico y servicio de mensajes cortos directamente en Braze o para motivar otros objetivos clave de marketing como la descarga de tu aplicación móvil.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Quikly | Se requiere una cuenta de partner de marca de [Quikly](https://www.quikly.com) para aprovechar esta asociación. |
| Clave de API REST or transferencia de estado representacional de Braze | Una clave de API REST or transferencia de estado representacional de Braze con permisos `users.track`, `subscription.status.set`, `users.export.ids` y `subscription.status.get`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**. |
| Endpoint REST or transferencia de estado representacional de Braze | [La URL de tu endpoint REST or transferencia de estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Tu endpoint dependerá de la URL de Braze de tu instancia. |
| Clave de API de Quikly (opcional) | Una clave de API de Quikly proporcionada por tu CSM or administrador de éxito de cliente or administrador de éxito de clientes (solo webhook). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Casos de uso {#use-cases}

Quikly permite a las marcas acelerar la adquisición por correo electrónico o servicio de mensajes cortos y motiva a los suscriptores a proporcionar datos propios directamente dentro de Braze. También puedes utilizar Braze para dirigirte a los clientes inactivos con una activación de Quikly que reactive y retenga a esa audiencia. Además, los especialistas en marketing pueden utilizar esta integración para incentivar eventos específicos del recorrido del cliente con estructuras de recompensa únicas.

Por ejemplo:
 - Genera expectación e interacción a lo largo de los días mientras los consumidores se adhieren voluntariamente para tener la oportunidad de conseguir recompensas emocionantes con [Quikly Hype](https://www.quikly.com/urgency-marketing/platform/product-overview/hype). Los datos propios se transfieren automáticamente a Braze.
 - Acelera la captación de nuevos suscriptores de correo electrónico y servicio de mensajes cortos mediante ofertas únicas en tiempo real basadas en la velocidad de respuesta del consumidor, su clasificación frente a otros, de forma aleatoria o antes de que se agote el tiempo o las cantidades con [Quikly Swap](https://www.quikly.com/urgency-marketing/platform/product-overview/swap).
 - Motiva pasos específicos en el recorrido del cliente con estructuras de recompensa únicas utilizando webhooks.
 - Aplica atributos o eventos personalizados al perfil del usuario al participar en una activación de Quikly.

## Integración {#integration}

A continuación se describen cuatro integraciones diferentes: adquisición por correo electrónico, adquisición por servicio de mensajes cortos, atributos personalizados y webhooks. La integración que elijas dependerá de tu activación de Quikly y de tu caso de uso.

{% tabs %}
{% tab Adquisición por correo electrónico %}

### Adquisición por correo electrónico {#email-acquisition}

Si tus activaciones de Quikly recopilan direcciones de correo electrónico de clientes o datos de perfil, el único paso necesario es proporcionar a Quikly tu clave de API REST or transferencia de estado representacional y endpoint. Quikly configurará tu cuenta de marca para pasar estos datos a Braze. Si hay atributos de usuario adicionales que te gustaría incluir, menciónalo cuando proporciones las credenciales de la API a Quikly.

Aquí tienes un esquema de cómo Quikly ejecuta este flujo de trabajo.
1. Al participar en una activación de Quikly, Quikly programa una búsqueda de usuarios utilizando la [API de exportación]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para ver si existe un usuario con un determinado `email_address`.
2. Registrar o actualizar el usuario.
  - Si el usuario existe:
    - No crees un nuevo perfil.
    - Si lo deseas, Quikly puede registrar un atributo personalizado en el perfil del usuario para indicar que el usuario participó en la activación.
  - Si el usuario no existe:
    - Quikly crea un perfil de solo alias a través del [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze, estableciendo el correo electrónico del usuario como alias de usuario para hacer referencia a ese usuario en el futuro (ya que el usuario no tendrá un ID externo).
    - Si lo deseas, Quikly puede registrar eventos personalizados para indicar que este perfil participó en la activación de Quikly.

{% details Solicitud /users/track %}

#### Encabezados de solicitud {#request-headers}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Cuerpo de la solicitud {#request-body}
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Adquisición por servicio de mensajes cortos %}

### Suscripciones servicio de mensajes cortos {#sms-subscriptions}

Las activaciones de Quikly pueden recopilar números de teléfono móvil directamente de los clientes e iniciar una nueva suscripción por servicio de mensajes cortos. Para habilitar esta integración, proporciona a tu CSM or administrador de éxito de cliente or administrador de éxito de clientes de Quikly el `subscription_group_id`. Puedes acceder al `subscription_group_id` de un grupo de suscripción navegando a la página **Grupo de suscripción**.

Quikly realizará una búsqueda de suscripciones utilizando el número de teléfono del cliente y lo acreditará automáticamente en la activación si ya existe una suscripción servicio de mensajes cortos. En caso contrario, se iniciará una nueva suscripción y, una vez verificado el estado de la misma, se acreditará al cliente.

Este es el flujo de trabajo completo cuando un cliente proporciona su número de móvil y su consentimiento a través de Quikly:
1. Quikly realiza una búsqueda de suscripciones utilizando el [estado del grupo de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) para ver si un determinado `phone` está suscrito a un `subscription_group_id`. Si existe una suscripción, acredita al usuario en la activación de Quikly. No es necesario realizar ninguna otra acción.
2. Quikly realiza una búsqueda de usuarios utilizando el [endpoint Exportar perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para ver si existe un perfil de usuario con un determinado `email_address`. Si no existe ningún usuario, crea un perfil de solo alias a través del [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de Braze, configurando el correo electrónico del usuario como alias de usuario para hacer referencia a ese usuario en el futuro (ya que el usuario no tendrá un ID externo).
3. Actualiza el estado de la suscripción utilizando el [endpoint Actualizar el estado del grupo de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status).

Para admitir los flujos de trabajo de suscripción por servicio de mensajes cortos de doble adhesión voluntaria existentes, Quikly puede enviar un evento personalizado a Braze en lugar del flujo de trabajo anterior. En ese caso, en lugar de actualizar el estado de la suscripción directamente, el [evento personalizado activa el proceso de doble adhesión voluntaria]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) y el estado de la suscripción se monitorea periódicamente para verificar que el usuario se ha adherido completamente antes de acreditarlo en la activación de Quikly.

{% alert important %}
Braze aconseja que, al crear nuevos usuarios a través del endpoint `/users/track`, haya un retraso de unos 2 minutos antes de añadir usuarios al grupo de suscripción correspondiente para dar tiempo a Braze a crear completamente el perfil de usuario.
{% endalert %}

{% details Solicitud detallada /subscription/status/set %}
#### Encabezados de solicitud
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Cuerpo de la solicitud
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Atributos personalizados %}
### Atributos personalizados {#custom-attributes}

Dependiendo de tu implementación de Braze, puede que quieras que los eventos dentro de la activación de Quikly pasen en cascada a través de Braze para su posterior procesamiento. Por ejemplo, es posible que desees aplicar un atributo de usuario personalizado basado en qué nivel o incentivo se logró en la activación de Quikly, lo que te permite mostrar la tarjeta de contenido relevante cuando abren tu aplicación o inician sesión en tu sitio web. Quikly trabajará contigo directamente para implementar estas integraciones.

{% endtab %}
{% tab Webhooks %}
### Webhooks
Utiliza webhooks para desencadenar incentivos para eventos específicos en el recorrido del cliente. Por ejemplo, si tienes un evento de Braze para cuando un usuario inicia sesión en tu aplicación, activa las notificaciones push o utiliza tu localizador de tiendas, puedes utilizar un webhook para desencadenar una oferta personalizada para ese usuario basada en la configuración de una activación de Quikly específica. Ejemplos de tácticas incluyen recompensar al primer número X de usuarios que realizan una acción (como iniciar sesión en tu aplicación) con una oferta personalizada o proporcionar una oferta que disminuye en valor a medida que transcurre más tiempo para motivar una respuesta inmediata.

### Crear un webhook de Quikly en Braze {#create-a-quikly-webhook-in-braze}

Para crear una plantilla de webhook de Quikly para futuras Campaigns o Canvas, navega a **Contenido** > **Webhook** en la plataforma Braze. Luego, selecciona **Crear plantilla de webhook**.

Si deseas crear una Campaign de webhook de Quikly única o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva Campaign.

Selecciona **Plantilla en blanco** e introduce lo siguiente para la URL del webhook y el cuerpo de la solicitud:
- **URL del webhook**: https://api.quikly.com/webhook/braze
- **Cuerpo de la solicitud**: pares clave/valor JSON

#### Encabezados de solicitud y método {#request-headers-and-method}

Quikly requiere un `HTTP Header` para la autorización.

- **Método HTTP**: POST
- **Encabezado de solicitud**:
  - **Authorization**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Content-Type**: application/json

#### Cuerpo de la solicitud

Selecciona ***Pares clave/valor JSON*** y añade los siguientes pares:
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### Vista previa de tu solicitud {#preview-your-request}

Previsualiza tu solicitud en el panel de **Vista previa** o navega hasta la pestaña `Test`, donde puedes seleccionar un usuario al azar, un usuario existente o personalizar el tuyo propio para probar tu webhook.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas de webhook actualizadas pueden encontrarse en la lista **Plantillas de webhook guardadas** al crear una nueva [Campaign de webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).
{% endalert %}

{% endtab %}
{% endtabs %}

## Soporte {#support}
Ponte en contacto con tu CSM or administrador de éxito de cliente or administrador de éxito de clientes en Quikly si tienes alguna pregunta.