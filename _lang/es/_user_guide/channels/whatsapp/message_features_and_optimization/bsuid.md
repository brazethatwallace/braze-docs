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

Un BSUID es un identificador único y persistente que WhatsApp asigna para representar a un usuario dentro de tu portafolio de negocio específico. Piensa en él como un número de teléfono alternativo para usuarios que eligen mantener su número de teléfono privado.

Los BSUID tienen tres características clave:

| Característica | Descripción |
| ----- | ----- |
| Único | Dos usuarios no comparten el mismo BSUID dentro de tu portafolio de negocio. |
| Con alcance de negocio | El mismo usuario tendrá un BSUID diferente con cada negocio al que envíe mensajes. Los BSUID no se pueden compartir ni comparar entre diferentes portafolios de negocio. |
| Disponible en webhooks | Los BSUID se incluyen en todas las mismas cargas útiles de webhook que actualmente contienen el número de teléfono del usuario. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ID de usuario con alcance de negocio (BSUID)" }

## Cambios en los tipos de usuario de WhatsApp {#changes-to-whatsapp-user-types}

Después del lanzamiento de los nombres de usuario de WhatsApp, habrá dos tipos de usuarios de WhatsApp:

| Tipo de usuario | Identificación de WhatsApp | Lo que Braze recibe |
| ----- | ----- | ----- |
| Usuarios sin nombre de usuario | Número de teléfono (sin cambios) | Número de teléfono (sin cambios) |
| Usuarios con nombre de usuario | Nombre de usuario (mostrado), BSUID (backend) | BSUID, número de teléfono para usuarios que ya tienen una conversación con tu negocio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cambios en los tipos de usuario de WhatsApp" }

La diferencia clave es que un usuario que adopta un nombre de usuario solo comparte su número de teléfono con tu negocio si tuviste una conversación previa con él o si aparece en tu libreta de contactos de WhatsApp.

## Cómo Braze manejará los BSUID {#how-braze-will-handle-bsuids}

Braze almacenará los BSUID como un [alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases) con la etiqueta `whats_app_bsuid` en el perfil de usuario. Esto significa que los usuarios que solo tienen BSUID tendrán perfiles de usuario completos en Braze y podrán entrar en Canvas, recibir mensajes, generar eventos y ser actualizados a través de la API.

### Enviar mensajes {#send-messages}

Cuando Braze envía un mensaje de WhatsApp, utilizará el número de teléfono si hay uno disponible. Si el usuario solo tiene un BSUID (como un usuario que te envía un mensaje por primera vez después de adoptar un nombre de usuario), Braze enviará utilizando el BSUID en su lugar. No se necesitan cambios en tus plantillas de mensajes, Campaigns ni pasos en Canvas.

### Mensajes entrantes y desencadenadores de Canvas {#inbound-messages-and-canvas-triggers}

Cuando un usuario con nombre de usuario te envía un mensaje entrante de WhatsApp, Braze:

1. Buscará al usuario por BSUID o número de teléfono (el que esté disponible en el webhook).
2. Si no se encuentra un usuario coincidente, creará un nuevo perfil de usuario anónimo con el BSUID almacenado como alias de usuario.
3. Desencadenará cualquier Canvas o Campaign configurado para iniciarse con un mensaje entrante de WhatsApp.

### Perfil de usuario {#user-profile}

Podrás ver el BSUID de un usuario en su perfil de usuario de Braze, en la sección de WhatsApp.

![Perfil de usuario con una sección de WhatsApp que contiene su ID de usuario con alcance de negocio.]({% image_buster /assets/img/whatsapp/bsuid_profile.png %}){: style="max-width:60%;"}

### Grupos de suscripción {#subscription-groups}

La gestión de grupos de suscripción funcionará de la misma manera para los usuarios con BSUID que para cualquier usuario identificado mediante un alias de usuario. Puedes actualizar el estado de suscripción de los usuarios con BSUID a través de:

- El [endpoint users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track) usando `user_alias`
- El paso [User Update]({{site.baseurl}}/user_update) de Canvas (funciona automáticamente)
- Carga de CSV

{% alert note %}
El [endpoint subscription/status/set]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) no será compatible con [`user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object). Usa el [endpoint users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para actualizar el estado de suscripción de los usuarios que solo tienen BSUID.
{% endalert %}

### Currents y datos de eventos {#currents-and-event-data}

Todos los eventos de Currents de WhatsApp (envío, entrega, lectura, fallo, recepción entrante, cancelación, reintento) incluirán un campo de BSUID. Para los usuarios que tienen tanto un número de teléfono como un BSUID, se incluirán ambos campos. Para los usuarios que solo tienen un BSUID, solo se incluirá el campo de BSUID (el campo de número de teléfono estará vacío).

## Cómo prepararte para el cambio {#how-to-prepare-for-the-change}

Para la mayoría de los clientes, no se requiere ninguna acción. Braze gestionará automáticamente el enrutamiento de BSUID, la creación de usuarios y el seguimiento de eventos. Sin embargo, te recomendamos [habilitar la Libreta de contactos de WhatsApp](#enable-whatsapp-contact-book) y [vincular los portafolios de negocio](#link-business-portfolios-if-you-use-multiple-wabas) si utilizas varias cuentas de WhatsApp Business (WABA).

### Habilitar la Libreta de contactos de WhatsApp {#enable-whatsapp-contact-book}

La Libreta de contactos es una característica de Meta que registra los números de teléfono de los usuarios con los que ya has conversado. Cuando un usuario adopta un nombre de usuario, su número de teléfono permanece visible para tu negocio si aparece en tu Libreta de contactos. Esto significa que Braze puede seguir identificando a los usuarios por número de teléfono incluso después de que habiliten un nombre de usuario.

Para habilitar la Libreta de contactos:

1. Ve a **Meta Business Suite** > **Business settings** > **Business info**.
2. Confirma que la característica de Libreta de contactos esté habilitada.

{% alert tip %}
La característica de Libreta de contactos está activada de forma predeterminada, pero te recomendamos confirmarlo en la configuración de Meta Business. Si la Libreta de contactos está deshabilitada, los usuarios que adopten nombres de usuario aparecerán como nuevos usuarios solo con BSUID, incluso si ya les habías enviado mensajes anteriormente.
{% endalert %}

### Vincular portafolios de negocio si utilizas varias WABA {#link-business-portfolios-if-you-use-multiple-wabas}

Los BSUID están asociados a un único portafolio de negocio. Si tu organización gestiona WABA de varios portafolios de negocio dentro del mismo espacio de trabajo de Braze, el mismo usuario tendrá un BSUID diferente para cada portafolio. Esto puede generar perfiles de usuario duplicados en Braze.

Para evitar esto, contacta a tu punto de contacto en Meta para verificar si tu negocio es elegible para vincular portafolios. Consulta [Vincular portafolios de negocio y BSUID principales](#link-business-portfolios-and-parent-bsuids) para más detalles.

Si todas tus WABA están dentro del mismo portafolio de negocio, no se requiere ninguna acción.

## Vincular portafolios comerciales y BSUIDs principales {#link-business-portfolios-and-parent-bsuids}

Si tu organización opera varias cuentas comerciales de WhatsApp (WABAs) en diferentes portafolios comerciales, puedes solicitar a tu punto de contacto en Meta que verifique si tu negocio es elegible para vincular esos portafolios entre sí. La elegibilidad la determina Meta y está disponible para negocios gestionados.

### Comportamiento de portafolios vinculados {#linked-portfolio-behavior}

Cuando tus portafolios comerciales están vinculados, WhatsApp incluirá un BSUID principal en todos los webhooks de mensajes junto con el BSUID regular. El BSUID principal se asignará a una nueva propiedad `parent_user_id` en la carga útil del webhook.

Los BSUIDs principales tienen las mismas propiedades que los BSUIDs regulares, pero se compartirán entre todos los números de teléfono comerciales dentro de tu conjunto de portafolios vinculados. Esto significa que el mismo usuario tendrá un identificador único y consistente independientemente de la WABA a la que envíe mensajes, evitando el riesgo de perfiles de usuario duplicados.

Un BSUID principal incluye `ENT` entre el código de país y el identificador alfanumérico. Por ejemplo:

```
US.ENT.11815799212886844830
```

Un BSUID regular no incluye `ENT`.

### Cómo usa Braze los BSUIDs principales {#how-braze-uses-parent-bsuids}

Cuando un webhook contiene tanto un BSUID regular como un BSUID principal, Braze utilizará el BSUID principal como identificador primario. Esto permite que un usuario que envía mensajes a través de múltiples WABAs en tus portafolios vinculados se asocie de forma consistente al mismo perfil de usuario de Braze.

Si no hay un BSUID principal presente (por ejemplo, porque tus portafolios no están vinculados o el usuario está enviando mensajes a una WABA no vinculada), Braze utilizará el BSUID regular. Los BSUIDs regulares seguirán funcionando normalmente en todos los casos.

{% alert note %}
Meta gestiona el proceso de vinculación de portafolios comerciales. Para comenzar, contacta a tu punto de contacto en Meta. Seguirás pudiendo enviar mensajes a los usuarios utilizando su BSUID regular incluso si tus portafolios están vinculados; los BSUIDs principales son adicionales, no un reemplazo.
{% endalert %}

| Escenario | Identificador utilizado por Braze |
| ----- | ----- |
| Un solo portafolio comercial | BSUID regular |
| Múltiples portafolios vinculados | BSUID principal (preferido). Si no existe un BSUID principal, se usa el BSUID regular |
| Múltiples portafolios no vinculados | BSUID regular (puede resultar en perfiles de usuario duplicados por portafolio) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cómo usa Braze los BSUIDs principales" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Mis Campaigns y Canvas existentes dejarán de funcionar cuando se lancen los nombres de usuario de WhatsApp? {#will-my-existing-campaigns-and-canvases-break-when-whatsapp-usernames-launch}

No. Las Campaigns y Canvas existentes seguirán funcionando. Los usuarios que no adopten un nombre de usuario no se verán afectados en absoluto. Para los usuarios que sí adopten un nombre de usuario y tengan un historial de conversación existente con tu empresa, Braze seguirá utilizando su número de teléfono como identificador principal.

### ¿Qué sucede con un usuario que adopta un nombre de usuario pero ya ha enviado mensajes a mi empresa? {#what-happens-to-a-user-who-adopts-a-username-but-has-already-messaged-my-business}

Si tu Libreta de contactos de WhatsApp está habilitada y tuviste una conversación previa con el usuario (o le enviaste un mensaje) en los últimos 30 días, su número de teléfono seguirá apareciendo en las cargas útiles del webhook junto con el BSUID. Braze lo asociará con su perfil de usuario existente. No se crea ningún perfil duplicado.

### ¿Qué pasa si un usuario adopta un nombre de usuario y no tiene conversación previa con mi empresa? {#what-if-a-user-adopts-a-username-and-has-no-prior-conversation-with-my-business}

Braze recibirá el BSUID del usuario en el webhook entrante y lo asociará con un perfil de usuario existente (si previamente almacenaste su BSUID) o creará un nuevo perfil de usuario anónimo con el BSUID almacenado como alias de usuario. Ese usuario podrá entonces ingresar a Canvas, recibir mensajes salientes y ser identificado o fusionado con otros perfiles utilizando las herramientas estándar de resolución de identidad de Braze.

### ¿Puedo segmentar usuarios con BSUID en Segments? {#can-i-target-bsuid-users-in-segments}

Los usuarios con BSUID son perfiles de usuario completos en Braze, por lo que puedes segmentarlos a través de filtros de audiencia estándar (como "ha recibido un mensaje de WhatsApp" o pertenencia a un grupo de suscripción). Sin embargo, segmentar específicamente por valores de BSUID (como "BSUID existe" o "BSUID es igual a X") no está soportado.

### ¿Cómo funciona la tarificación de WhatsApp para usuarios con BSUID? {#how-does-whatsapp-pricing-work-for-bsuid-users}

La tarificación de conversaciones de WhatsApp se determina por el país del usuario. Para usuarios identificados por número de teléfono, Meta determina el país a partir del código de país del número de teléfono. Para usuarios identificados por BSUID, el país está codificado directamente en el propio BSUID; por ejemplo, un BSUID que comienza con `US` representa a un usuario en Estados Unidos.

Esto significa que el comportamiento de la tarificación es consistente tanto si un usuario está identificado por número de teléfono como por BSUID. El país utilizado para calcular las tasas de conversación lo determina el identificador que Meta proporciona, y Braze lo transmite sin modificación. No necesitas hacer nada diferente, pero ten en cuenta que al enviar mensajes a usuarios que solo tienen BSUID, la tarificación basada en el país de Meta se basa en el país codificado en el BSUID del usuario en lugar de un número de teléfono.

### ¿Cómo hago referencia a un usuario con BSUID en llamadas a la API? {#how-do-i-reference-a-bsuid-user-in-api-calls}

Usa el parámetro `user_alias` con `alias_label: "whats_app_bsuid"` y `alias_name` establecido en el valor BSUID del usuario. Por ejemplo:

```json
{
  "user_alias": {
    "alias_label": "whats_app_bsuid",
    "alias_name": "DDC91135R"
  }
}
```

Esto funciona con `users/track`, `users/identify`, carga de CSV y el paso de Canvas de actualización de usuario.

### ¿Se interrumpirán mis pipelines de datos de Currents? {#will-my-currents-data-pipelines-break}

Los eventos de Currents para WhatsApp incluyen un campo `bsuid` junto al campo existente de número de teléfono. Para usuarios que solo tienen BSUID, el campo de número de teléfono estará vacío. Si tus pipelines posteriores tienen requisitos estrictos sobre el campo de número de teléfono, confirma que puedan manejar un valor nulo o vacío.

### Tengo varios WABAs en diferentes portafolios de negocios. ¿El mismo usuario aparecerá como dos perfiles diferentes en Braze? {#i-have-multiple-wabas-across-different-business-portfolios-will-the-same-user-appear-as-two-different-profiles-in-braze}

Sin portafolios vinculados, sí. El mismo usuario de WhatsApp tendrá un BSUID diferente por portafolio de negocios, y Braze creará perfiles separados para cada uno.

Para resolver esto, contacta a tu punto de contacto de Meta para verificar la elegibilidad para la vinculación de portafolios. Cuando están vinculados, Meta proporciona un BSUID padre compartido entre todos los portafolios, y Braze lo utilizará para identificar de forma consistente al usuario en todos tus WABAs. Consulta [Vincular portafolios de negocios y BSUIDs padre](#link-business-portfolios-and-parent-bsuids) para más detalles.

### ¿Puedo desactivar la Libreta de contactos? {#can-i-disable-the-contact-book}

Recomendamos encarecidamente mantener la Libreta de contactos habilitada. Si se desactiva la Libreta de contactos, se pierden todos los registros históricos de números de teléfono de tus usuarios. Los usuarios que adoptaron nombres de usuario aparecerían entonces como nuevos usuarios solo con BSUID, incluso si les habías enviado mensajes previamente.

## Recursos adicionales {#additional-resources}

* [Configuración de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)
* [Alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)
* [Grupos de suscripción de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
* [Eventos de Currents de WhatsApp]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#whatsapp-abort-events)
* [Meta: ID de usuario con alcance empresarial](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids)