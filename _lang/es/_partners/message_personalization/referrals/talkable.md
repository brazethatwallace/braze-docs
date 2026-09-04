---
nav_title: Talkable
article_title: Talkable
description: "Este artículo de referencia describe la asociación entre Braze y Talkable, una plataforma de marketing de referidos que sincroniza las adhesiones voluntarias de correo electrónico de marketing desde campañas de referidos a Braze en tiempo real."
alias: /partners/talkable/
page_type: partner
search_tag: Partner
---

# Talkable

> [Talkable](https://www.talkable.com/) ayuda a las marcas de consumo a convertir a los clientes satisfechos en un canal de referidos escalable. Con la integración de Braze, las adhesiones voluntarias de correo electrónico de marketing capturadas en campañas de referidos de Talkable fluyen hacia Braze en tiempo real, proporcionando a tu equipo el consentimiento, el contexto y los datos de campaña que necesitas para dar la bienvenida, segmentar e interactuar con cada nuevo promotor y amigo.

_Esta integración es mantenida por Talkable._

## Acerca de la integración {#about-the-integration}

Talkable incorpora la adquisición impulsada por embajadores en el recorrido del cliente que Braze potencia. La integración traslada cada adhesión voluntaria de referidos que Talkable captura al perfil de Braze correspondiente en tiempo real, de modo que los flujos de bienvenida, los recorridos de referidos, la segmentación y la mensajería de ciclo de vida pueden lanzarse a partir de un consentimiento confiable y del contexto de referidos, todo sin exportaciones manuales de listas ni sincronizaciones por lotes.

Talkable captura adhesiones voluntarias de marketing en dos escenarios:

* **Registro del embajador:** Un embajador se registra en una campaña de referidos de Talkable y acepta recibir correo electrónico de marketing.
* **Filtro de correo electrónico del amigo:** Un amigo completa el paso de filtro de correo electrónico de Talkable y acepta recibir correo electrónico de marketing.

En cualquiera de los dos casos, Talkable crea o actualiza el perfil de usuario de Braze correspondiente en tiempo real y establece el estado de suscripción de correo electrónico del usuario en **Opted In**.

### Comportamiento predeterminado {#default-behavior}

Talkable envía datos a Braze solo cuando se produce un evento de adhesión voluntaria explícito por parte de alguien que ha dado su consentimiento en Talkable, ya sea un embajador que se registra en una campaña o un amigo que acepta durante el filtro de correo electrónico. Talkable no ejecuta lotes nocturnos, sincronizaciones completas ni actualizaciones implícitas de perfiles. Talkable nunca envía a Braze perfiles que no han dado su adhesión voluntaria.

## Ejemplos {#use-cases}

- Desencadena un Canvas de bienvenida en Braze en el momento en que un promotor se registra en una campaña de referidos de Talkable.
- Activa a los amigos referidos con un Canvas específico para amigos y una oferta personalizada de primera compra en cuanto un amigo acepta la adhesión voluntaria.
- Segmenta por contexto de referidos utilizando indicadores de promotor y amigo, así como metadatos de campaña enviados como atributos personalizados de Braze.
- Dirige las adhesiones voluntarias de referidos a un grupo de suscripción designado en Braze para el envío de boletines con cumplimiento normativo.

## Requisitos previos {#prerequisites}

Antes de comenzar, necesitas lo siguiente:

| Requisito previo | Descripción |
| --- | --- |
| Una cuenta de Talkable | Se necesita un sitio de Talkable con al menos una campaña configurada para aprovechar esta integración. |
| Una clave de API REST de Braze | Una clave de API REST de Braze con permisos de `users.track`. Crea esta clave en el panel de Braze desde **Configuración** > **Claves de API**. Para más información, consulta [Crear claves de API REST]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| Un endpoint REST de Braze | La URL de tu endpoint REST de Braze (por ejemplo, `https://rest.iad-01.braze.com`). Se admiten tanto los clústeres de Braze en EE. UU. (`.com`) como en la UE (`.eu`). Para más información, consulta [Endpoints de la REST API]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Instalar la aplicación de Braze en Talkable {#step-1-install-the-braze-app-in-talkable}

1. Inicia sesión en tu panel de administración de Talkable, abre el menú y ve a **All Site Settings** > **App Store**.
2. Localiza **Braze** y selecciona **Install**.
3. Introduce tu endpoint REST de Braze y una clave de API REST con permisos de `users.track`, y selecciona **Save**.

### Paso 2: Configurar la acción de adhesión voluntaria por correo electrónico {#step-2-configure-the-email-opt-in-action}

1. En la aplicación de Braze en Talkable, abre la acción **Email opt-in**.
2. (Opcional) Introduce un identificador de grupo de suscripción de Braze, añade atributos personalizados y/o configura un alias de usuario. Para más información, consulta [Personalizar Talkable](#customizing-talkable).
3. Selecciona **Save**. Deja la acción deshabilitada para que puedas verificar la configuración con una carga útil de prueba antes de que los eventos de adhesión voluntaria en vivo comiencen a sincronizarse.

### Paso 3: Probar con una carga útil de ejemplo {#step-3-test-with-a-sample-payload}

1. En Talkable, selecciona **Send sample payload** en la acción **Email opt-in** para enviar una solicitud de prueba a Braze.
2. En Braze, ve a **Audiencia** > **Búsqueda de usuarios** y busca por la dirección de correo electrónico de prueba.
3. Confirma que el perfil existe con **Email Subscribe** configurado como **Opted In** y que cualquier atributo personalizado, inscripción en grupo de suscripción o alias de usuario que hayas configurado aparezca como se esperaba.

### Paso 4: Habilitar la acción para el tráfico en vivo {#step-4-enable-the-action-for-live-traffic}

Cuando el perfil de prueba se vea correcto en Braze, regresa a Talkable y habilita la acción **Email opt-in**.

A partir de este punto, cada evento de adhesión voluntaria de Talkable sincroniza el perfil correspondiente con Braze en tiempo real.

## Atributos de usuario predeterminados enviados a Braze {#default-user-attributes-sent-to-braze}

En cada evento de adhesión voluntaria, Talkable crea o actualiza el perfil de usuario de Braze correspondiente con los siguientes atributos de usuario estándar de Braze. Los valores vacíos se omiten.

| Atributo de Braze | Tipo | Notas |
| --- | --- | --- |
| `email_subscribe` | Cadena | Se establece en **Opted In** en cada evento de adhesión voluntaria de Talkable. |
| `email` | Cadena | Identificador principal utilizado para hacer coincidir el perfil de Braze. |
| `phone` | Cadena | Se captura únicamente como atributo de usuario. Braze espera el formato E.164; se envía tal como está almacenado en Talkable. |
| `first_name` | Cadena | El nombre de la persona. |
| `last_name` | Cadena | El apellido de la persona. |
| Inscripción en grupo de suscripción | No aplica | Talkable inscribe al usuario como suscrito cuando se configura un grupo de suscripción. |
| Alias de usuario | No aplica | Se agrega solo cuando se configura un alias de usuario. Para más información, consulta [Personalización de Talkable](#customizing-talkable). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos de usuario predeterminados enviados a Braze" }

## Personalizar Talkable {#customize-talkable}

Las siguientes personalizaciones opcionales están disponibles. Configura cualquier combinación; son independientes.

### Inscribir adhesiones voluntarias en un grupo de suscripción de Braze {#enroll-opt-ins-in-a-braze-subscription-group}

1. En Braze, copia un ID de grupo de suscripción desde **Audience** > **Subscription Group Management**. Para más información, consulta [Gestión de suscripciones de usuario]({{site.baseurl}}/user_guide/channels/email/subscriptions).
2. En la acción **Email opt-in** de Talkable, pégalo en el campo **Subscription group identifier**.

Talkable inscribe cada adhesión voluntaria en ese grupo de suscripción como suscrito, limitando las adhesiones voluntarias de referidos a ese grupo en lugar de una suscripción global. Talkable solo añade suscripciones; nunca las elimina.

### Enviar atributos personalizados {#send-custom-attributes}

Añade cualquier par clave-valor en el editor de carga útil de la acción. La clave que introduzcas se convierte en el nombre del atributo en el perfil de usuario de Braze.

Los valores utilizan plantillas Liquid. Las siguientes variables están disponibles:

{% raw %}
| Variable | Contenido |
| --- | --- |
| `{{ person }}` | El promotor o amigo que se adhirió voluntariamente (`email`, `first_name`, `last_name`, `phone_number`, `username`, `is_advocate`, `custom_properties`, y más). |
| `{{ ip }}` | La dirección IP desde la que se realizó la adhesión voluntaria. |
| `{{ campaign }}` | La Campaign de Talkable de origen (`name`, `type`, `tag_names`, y más). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Variables de plantilla Liquid" }
{% endraw %}

{% raw %}
Ejemplo: añade `talkable_is_advocate` = `{{ person.is_advocate }}` y `talkable_campaign_name` = `{{ campaign.name }}` para segmentar por contexto de referidos en Braze.
{% endraw %}

### Identificar usuarios con alias de usuario de Braze {#identify-users-with-braze-user-aliases}

En el editor de carga útil, añade `user_alias.alias_name` (por ejemplo, {% raw %}`{{ person.username }}`{% endraw %}) y `user_alias.alias_label` (por ejemplo, `username`). Para más información, consulta [Objeto de alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object).

Cuando ambos campos están presentes, el sistema identifica al usuario por el alias además del correo electrónico, y Braze crea un nuevo perfil con alias si no existe una coincidencia.

{% alert note %}
Ambos campos de alias son obligatorios. Si solo se establece uno de `alias_name` o `alias_label`, Talkable no envía un alias de usuario y el perfil se asocia únicamente por correo electrónico.
{% endalert %}

## Encontrar y crear usuarios en Braze {#find-and-create-users-in-braze}

* De forma predeterminada, Braze busca coincidencias en el perfil por dirección de correo electrónico. Si no existe un perfil coincidente, Braze crea uno nuevo.
* Cuando se configura un alias de usuario, Braze también busca coincidencias con ese alias y crea un nuevo perfil con alias si no encuentra ninguna coincidencia.
* Esta integración no utiliza ID externos. Para vincular las adhesiones voluntarias de Talkable a un perfil existente identificado externamente, configura un alias de usuario cuya etiqueta de alias coincida con el alias conocido de ese perfil.

## Usa Talkable con Braze {#use-talkable-with-braze}

### Encontrar un usuario sincronizado {#find-a-synced-user}

Ve a **Audiencia** > **Búsqueda de usuarios** y busca por correo electrónico para ver un perfil que Talkable creó o actualizó.

Los campos estándar (correo electrónico, teléfono, nombre o apellido) y cualquier atributo personalizado que hayas configurado aparecen en el perfil; **Email Subscribe** muestra **Opted In**.

### Crear un Segment de referidos {#build-a-referral-segment}

1. Crea un Segment filtrado donde **Email Subscribe** sea **Opted In**.
2. Refina con los atributos personalizados que envía Talkable, por ejemplo, `talkable_is_advocate` igual a `true` para dirigirte a promotores, o `talkable_campaign_name` igual a tu campaña para dirigirte a un programa de referidos específico.

### Desencadenar mensajería del ciclo de vida {#trigger-lifecycle-messaging}

1. Crea un Canvas o una Campaign con entrega basada en acciones. Los siguientes tipos de desencadenadores de Braze funcionan con esta integración:
* **Update Subscription Status** (por ejemplo, la suscripción de correo electrónico cambia a **Opted In**)
* **Update Subscription Group Status** (cuando se configura un grupo de suscripción)
* **Change Custom Attribute Value** (para cualquier atributo personalizado de Talkable que envíes).
2. Personaliza los mensajes con los atributos personalizados de Talkable en el perfil (nombre de la campaña, valor de la recompensa, referente, etc.).

## Consideraciones {#considerations}

* **Solo adhesión voluntaria por correo electrónico:** Los números de teléfono se capturan como un atributo de usuario estándar, pero la integración no establece un estado de suscripción SMS. Talkable no sincroniza las adhesiones voluntarias de SMS.
* **Formato de teléfono:** Braze espera los números de teléfono en formato internacional (E.164).
* **Sincronización en tiempo real basada en eventos:** Talkable envía una solicitud por evento de adhesión voluntaria (un usuario por solicitud). No hay procesamiento por lotes ni sincronización completa periódica; el volumen se corresponde con tu volumen de adhesiones voluntarias de referidos.
* **Entrega fiable:** Si Braze devuelve un error temporalmente, Talkable reintenta automáticamente. Los fallos persistentes envían una alerta por correo electrónico al administrador del sitio.

## Solución de problemas {#troubleshooting}

| Error | Causa probable | Solución |
| --- | --- | --- |
| 401 Unauthorized | A la clave de API REST le faltan los permisos `users.track`, o el endpoint apunta al clúster incorrecto. | Vuelve a emitir la clave con los permisos `users.track` y confirma que el endpoint REST coincide con tu clúster de Braze. |
| El endpoint REST se rechaza durante la instalación | La URL no es un endpoint REST de Braze. | Usa el endpoint REST de tu clúster, por ejemplo `https://rest.iad-01.braze.com`. Una URL del panel no funciona. |
| Se crea el perfil pero no aparece en un grupo de suscripción | No se configuró ningún ID de grupo de suscripción. | Introduce el ID del grupo de suscripción en la acción **Email opt-in**. |
| No se aplica el alias de usuario | Solo se completó uno de los dos campos de alias (nombre o etiqueta). | Introduce ambos campos en la acción: nombre de alias y etiqueta de alias. |
| El perfil no aparece | Aún no se ha enviado la solicitud de muestra o la acción está deshabilitada. | Selecciona **Send sample payload** en Talkable y asegúrate de que la acción **Email opt-in** esté habilitada. |
| Las solicitudes dejaron de enviarse tras una rotación de clave | La clave de API almacenada fue revocada o reemplazada en Braze. | En la **App Store** de Talkable, abre la aplicación de Braze, pega la nueva clave de API REST y selecciona **Save**; vuelve a probar con **Send sample payload**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Solución de problemas" }

Para obtener más información sobre la integración de Talkable, consulta la [documentación de integración de Talkable con Braze](https://docs.talkable.com/email_marketing_and_automation/braze/). Para contactar con el soporte de Talkable, envía un correo electrónico a [support@talkable.com](mailto:support@talkable.com).