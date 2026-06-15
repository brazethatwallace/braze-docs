---
nav_title: Nombres de usuario y BSUID
article_title: Nombres de usuario de WhatsApp e ID de usuario con alcance de negocio
page_order: 7
description: "Descubre cómo los nombres de usuario de WhatsApp y los ID de usuario con alcance de negocio (BSUID) afectan la identificación de usuarios, la mensajería y el manejo de datos en Braze."
page_type: reference
alias: "/whatsapp_usernames/"
channel:
  - WhatsApp
hidden: true
noindex: true
---

# Nombres de usuario de WhatsApp e ID de usuario con alcance de negocio {#whatsapp-usernames-and-business-scoped-user-ids}

> En junio de 2026, WhatsApp planea introducir nombres de usuario: una característica de privacidad opcional que oculta los números de teléfono de los usuarios cuando envían mensajes a empresas. Braze está completamente preparado para manejar este cambio; para la mayoría de los clientes, nada en tus Campaigns o Canvas necesita cambiar.

{% alert important %}
Se espera que los nombres de usuario de WhatsApp y los ID de usuario con alcance de negocio (BSUID) se lancen en junio de 2026, con actualizaciones de Braze programadas para coincidir con este lanzamiento. Las actualizaciones de Braze en este artículo **no se han** lanzado.
{% endalert %}

Cuando los usuarios de WhatsApp adoptan un nombre de usuario, su número de teléfono ya no se comparte automáticamente con las empresas a las que envían mensajes. En su lugar, WhatsApp proporciona a las empresas un ID de usuario con alcance de negocio (BSUID), un identificador único que es específico para cada par de portafolio de negocio y usuario.

Braze manejará los BSUID automáticamente. Los usuarios que adopten un nombre de usuario seguirán apareciendo en tu espacio de trabajo de Braze, recibirán mensajes, activarán Canvas y generarán eventos. Algunos clientes pueden necesitar [prepararse para el cambio](#how-to-prepare-for-the-change).

## ID de usuario con alcance de negocio (BSUID) {#business-scoped-user-id-bsuid}

Un BSUID es un identificador único y persistente que WhatsApp asigna para representar a un usuario dentro de tu portafolio de negocio específico. Piensa en él como un número de teléfono alternativo para los usuarios que eligen mantener su número de teléfono privado.

Los BSUID tienen tres características clave:

| Característica | Descripción |
| ----- | ----- |
| Único | Dos usuarios no comparten el mismo BSUID dentro de tu portafolio de negocio. |
| Con alcance de negocio | El mismo usuario tendrá un BSUID diferente con cada empresa a la que envíe mensajes. Los BSUID no se pueden compartir ni comparar entre diferentes portafolios de negocio. |
| Disponible en webhooks | Los BSUID se incluyen en todas las mismas cargas útiles de webhook que actualmente llevan el número de teléfono del usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Business-scoped user ID (BSUID)" }

## Cambios en los tipos de usuario de WhatsApp {#changes-to-whatsapp-user-types}

Después del lanzamiento de los nombres de usuario de WhatsApp, habrá dos tipos de usuarios de WhatsApp:

| Tipo de usuario | Identificación en WhatsApp | Lo que Braze recibe |
| ----- | ----- | ----- |
| Usuarios sin nombre de usuario | Número de teléfono (sin cambios) | Número de teléfono (sin cambios) |
| Usuarios con nombre de usuario | Nombre de usuario (mostrado), BSUID (backend) | BSUID, número de teléfono para usuarios que tienen una conversación existente con tu empresa |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Changes to WhatsApp user types" }

La diferencia clave es que un usuario que adopta un nombre de usuario solo comparte su número de teléfono con tu empresa si tuviste una conversación previa con él o si aparece en tu libreta de contactos de WhatsApp.

## Cómo Braze manejará los BSUID {#how-braze-will-handle-bsuids}

Braze almacenará los BSUID como un [alias de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases) con la etiqueta `whats_app_bsuid` en el perfil de usuario. Esto significa que los usuarios que solo tienen BSUID tendrán perfiles de usuario completos en Braze y podrán entrar en Canvas, recibir mensajes, generar eventos y ser actualizados a través de la API.

### Enviar mensajes {#send-messages}

Cuando Braze envía un mensaje de WhatsApp, utilizará el número de teléfono si hay uno disponible. Si el usuario solo tiene un BSUID (como un usuario que te envía un mensaje por primera vez después de adoptar un nombre de usuario), Braze enviará usando el BSUID en su lugar. No se necesitan cambios en tus plantillas de mensajes, Campaigns o pasos en Canvas.

### Mensajes de entrada y activadores de Canvas {#inbound-messages-and-canvas-triggers}

Cuando un usuario con nombre de usuario te envía un mensaje de WhatsApp de entrada, Braze:

1. Buscará al usuario por BSUID o número de teléfono (el que esté disponible en el webhook).
2. Si no se encuentra un usuario coincidente, creará un nuevo perfil de usuario anónimo con el BSUID almacenado como alias de usuario.
3. Activará cualquier Canvas o Campaign configurado para iniciarse con un mensaje de WhatsApp de entrada.

### Perfil de usuario {#user-profile}

Podrás ver el BSUID de un usuario en su perfil de usuario de Braze en la sección de WhatsApp.

![Perfil de usuario con una sección de WhatsApp que contiene su ID de usuario con alcance de negocio.]({% image_buster /assets/img/whatsapp/bsuid_profile.png %}){: style="max-width:60%;"}

### Grupos de suscripción {#subscription-groups}

La administración de grupos de suscripción funcionará de la misma manera para los usuarios con BSUID que para cualquier usuario identificado por un alias de usuario. Puedes actualizar el estado de suscripción de los usuarios con BSUID a través de:

- El [punto de conexión users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) usando `user_alias`
- El paso de [Actualización de usuario]({{site.baseurl}}/user_update/) en Canvas (funciona automáticamente)
- Carga de CSV

{% alert note %}
El [punto de conexión subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) no admitirá [`user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object/). Usa el [punto de conexión users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para actualizar el estado de suscripción de los usuarios que solo tienen BSUID.
{% endalert %}

### Currents y datos de eventos {#currents-and-event-data}

Todos los eventos de Currents de WhatsApp (envío, entrega, lectura, fallo, recepción de entrada, cancelación, reintento) incluirán un campo BSUID. Para los usuarios que tienen tanto un número de teléfono como un BSUID, se incluirán ambos campos. Para los usuarios que solo tienen un BSUID, solo se incluirá el campo BSUID (el campo de número de teléfono estará vacío).

## Cómo prepararse para el cambio {#how-to-prepare-for-the-change}

Para la mayoría de los clientes, no se requiere ninguna acción. Braze manejará automáticamente el enrutamiento de BSUID, la creación de usuarios y el seguimiento de eventos. Sin embargo, recomendamos [habilitar la libreta de contactos de WhatsApp](#enable-whatsapp-contact-book) y [vincular portafolios de negocio](#link-business-portfolios-if-you-use-multiple-wabas) si usas múltiples cuentas de WhatsApp Business (WABA).

### Habilitar la libreta de contactos de WhatsApp {#enable-whatsapp-contact-book}

La libreta de contactos es una característica de Meta que registra los números de teléfono de los usuarios con los que ya has conversado. Cuando un usuario adopta un nombre de usuario, su número de teléfono sigue siendo visible para tu empresa si aparece en tu libreta de contactos. Esto significa que Braze puede seguir identificando a los usuarios por número de teléfono incluso después de que habiliten un nombre de usuario.

Para habilitar la libreta de contactos:

1. Ve a **Meta Business Suite** > **Business settings** > **Business info**.
2. Confirma que la característica de libreta de contactos está habilitada.

{% alert tip %}
La característica de libreta de contactos está activada de forma predeterminada, pero recomendamos confirmar esto en la configuración de tu Meta Business. Si la libreta de contactos está deshabilitada, los usuarios que adopten nombres de usuario aparecerán como nuevos usuarios solo con BSUID, incluso si les habías enviado mensajes anteriormente.
{% endalert %}

### Vincular portafolios de negocio si usas múltiples WABA {#link-business-portfolios-if-you-use-multiple-wabas}

Los BSUID tienen alcance a un solo portafolio de negocio. Si tu organización administra WABA de múltiples portafolios de negocio dentro del mismo espacio de trabajo de Braze, el mismo usuario tendrá un BSUID diferente para cada portafolio. Esto puede resultar en perfiles de usuario duplicados en Braze.

Para evitar esto, ponte en contacto con tu punto de contacto de Meta para verificar si tu empresa es elegible para vincular portafolios. Consulta [Vincular portafolios de negocio y BSUID principales](#link-business-portfolios-and-parent-bsuids) para más detalles.

Si todas tus WABA están dentro del mismo portafolio de negocio, no se necesita ninguna acción.

## Vincular portafolios de negocio y BSUID principales {#link-business-portfolios-and-parent-bsuids}

Si tu organización opera múltiples cuentas de WhatsApp Business (WABA) en diferentes portafolios de negocio, puedes pedirle a tu punto de contacto de Meta que verifique si tu empresa es elegible para vincular esos portafolios. La elegibilidad la determina Meta y está disponible para empresas gestionadas.

### Comportamiento de portafolios vinculados {#linked-portfolio-behavior}

Cuando tus portafolios de negocio están vinculados, WhatsApp incluirá un BSUID principal en todos los webhooks de mensajes junto con el BSUID regular. El BSUID principal se asignará a una nueva propiedad `parent_user_id` en la carga útil del webhook.

Los BSUID principales tienen las mismas propiedades que los BSUID regulares, pero se compartirán entre todos los números de teléfono de negocio dentro de tu conjunto de portafolios vinculados. Esto significa que el mismo usuario tendrá un único identificador consistente independientemente de la WABA a la que envíe mensajes, evitando el riesgo de perfiles de usuario duplicados.

Un BSUID principal incluye `ENT` entre el código de país y el identificador alfanumérico. Por ejemplo:

```
US.ENT.11815799212886844830
```

Un BSUID regular no incluye `ENT`.

### Cómo Braze usa los BSUID principales {#how-braze-uses-parent-bsuids}

Cuando un webhook contiene tanto un BSUID regular como un BSUID principal, Braze usará el BSUID principal como identificador primario. Esto permite que un usuario que envía mensajes a través de múltiples WABA en tus portafolios vinculados sea emparejado de manera consistente con el mismo perfil de usuario de Braze.

Si no hay un BSUID principal presente (por ejemplo, porque tus portafolios no están vinculados o el usuario está enviando mensajes a una WABA no vinculada), Braze usará el BSUID regular. Los BSUID regulares seguirán funcionando normalmente en todos los casos.

{% alert note %}
Meta gestiona el proceso de vinculación de portafolios de negocio. Para comenzar, ponte en contacto con tu punto de contacto de Meta. Seguirás pudiendo enviar mensajes a los usuarios usando su BSUID regular incluso si tus portafolios están vinculados; los BSUID principales son aditivos, no un reemplazo.
{% endalert %}

| Escenario | Identificador usado por Braze |
| ----- | ----- |
| Un solo portafolio de negocio | BSUID regular |
| Múltiples portafolios vinculados | BSUID principal (preferido). Si no existe un BSUID principal, se usa el BSUID regular |
| Múltiples portafolios no vinculados | BSUID regular (puede resultar en perfiles de usuario duplicados por portafolio) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="How Braze uses parent BSUIDs" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Mis Campaigns y Canvas existentes dejarán de funcionar cuando se lancen los nombres de usuario de WhatsApp? {#will-my-existing-campaigns-and-canvases-break-when-whatsapp-usernames-launch}

No. Las Campaigns y los Canvas existentes seguirán funcionando. Los usuarios que no adopten un nombre de usuario no se verán afectados en absoluto. Para los usuarios que adopten un nombre de usuario y tengan un historial de conversación existente con tu empresa, Braze seguirá usando su número de teléfono como identificador principal.

### ¿Qué sucede con un usuario que adopta un nombre de usuario pero ya ha enviado mensajes a mi empresa? {#what-happens-to-a-user-who-adopts-a-username-but-has-already-messaged-my-business}

Si tu libreta de contactos de WhatsApp está habilitada y tuviste una conversación previa con el usuario (o le enviaste un mensaje) en los últimos 30 días, su número de teléfono seguirá apareciendo en las cargas útiles del webhook junto con el BSUID. Braze los emparejará con su perfil de usuario existente. No se crea un perfil duplicado.

### ¿Qué pasa si un usuario adopta un nombre de usuario y no tiene conversación previa con mi empresa? {#what-if-a-user-adopts-a-username-and-has-no-prior-conversation-with-my-business}

Braze recibirá el BSUID del usuario en el webhook de entrada y lo emparejará con un perfil de usuario existente (si previamente almacenaste su BSUID) o creará un nuevo perfil de usuario anónimo con el BSUID almacenado como alias de usuario. Ese usuario podrá entonces entrar en Canvas, recibir mensajes salientes y ser identificado o fusionado con otros perfiles usando las herramientas estándar de resolución de identidad de Braze.

### ¿Puedo segmentar usuarios con BSUID en Segments? {#can-i-target-bsuid-users-in-segments}

Los usuarios con BSUID son perfiles de usuario completos en Braze, por lo que puedes segmentarlos a través de filtros de audiencia estándar (como "ha recibido un mensaje de WhatsApp" o membresía de grupo de suscripción). Sin embargo, no se admite la segmentación específica por valores de BSUID (como "BSUID existe" o "BSUID es igual a X").

### ¿Cómo funciona la tarificación de WhatsApp para los usuarios con BSUID? {#how-does-whatsapp-pricing-work-for-bsuid-users}

La tarificación de conversaciones de WhatsApp se determina por el país del usuario. Para los usuarios identificados por número de teléfono, Meta deriva el país del código de país del número de teléfono. Para los usuarios identificados por BSUID, el país está codificado directamente en el propio BSUID; por ejemplo, un BSUID que comienza con `US` representa a un usuario en Estados Unidos.

Esto significa que el comportamiento de tarificación es consistente ya sea que un usuario esté identificado por número de teléfono o BSUID. El país utilizado para calcular las tasas de conversación lo determina el identificador que Meta proporciona, y Braze lo transmite sin modificación. No necesitas hacer nada diferente, pero ten en cuenta que al enviar mensajes a usuarios que solo tienen BSUID, la tarificación basada en país de Meta se basa en el país codificado en el BSUID del usuario en lugar de un número de teléfono.

### ¿Cómo hago referencia a un usuario con BSUID en llamadas a la API? {#how-do-i-reference-a-bsuid-user-in-api-calls}

Usa el parámetro `user_alias` con `alias_label: "whats_app_bsuid"` y `alias_name` configurado con el valor del BSUID del usuario. Por ejemplo:

```json
{
  "user_alias": {
    "alias_label": "whats_app_bsuid",
    "alias_name": "DDC91135R"
  }
}
```

Esto funciona con `users/track`, `users/identify`, carga de CSV y el paso de Actualización de usuario en Canvas.

### ¿Se interrumpirán mis pipelines de datos de Currents? {#will-my-currents-data-pipelines-break}

Los eventos de Currents para WhatsApp incluyen un campo `bsuid` junto con el campo de número de teléfono existente. Para los usuarios que solo tienen un BSUID, el campo de número de teléfono estará vacío. Si tus pipelines posteriores tienen requisitos estrictos sobre el campo de número de teléfono, confirma que pueden manejar un valor nulo o vacío.

### Tengo múltiples WABA en diferentes portafolios de negocio. ¿El mismo usuario aparecerá como dos perfiles diferentes en Braze? {#i-have-multiple-wabas-across-different-business-portfolios-will-the-same-user-appear-as-two-different-profiles-in-braze}

Sin portafolios vinculados, sí. El mismo usuario de WhatsApp tendrá un BSUID diferente por portafolio de negocio, y Braze creará perfiles separados para cada uno.

Para resolver esto, ponte en contacto con tu punto de contacto de Meta para verificar la elegibilidad para la vinculación de portafolios. Cuando estén vinculados, Meta proporciona un BSUID principal compartido entre todos los portafolios, y Braze lo usará para identificar de manera consistente al usuario en todas tus WABA. Consulta [Vincular portafolios de negocio y BSUID principales](#link-business-portfolios-and-parent-bsuids) para más detalles.

### ¿Puedo deshabilitar la libreta de contactos? {#can-i-disable-the-contact-book}

Recomendamos encarecidamente mantener la libreta de contactos habilitada. Si la libreta de contactos está deshabilitada, se perderán todos los registros históricos de números de teléfono de tus usuarios. Los usuarios que adoptaron nombres de usuario aparecerían entonces como nuevos usuarios solo con BSUID, incluso si les habías enviado mensajes anteriormente.

## Recursos adicionales {#additional-resources}

* [Configuración de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/)
* [Alias de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases)
* [Grupos de suscripción de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/)
* [Eventos de Currents de WhatsApp]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#whatsapp)
* [Meta: ID de usuario con alcance de negocio](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids)