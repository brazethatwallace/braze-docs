---
nav_title: Grupos de suscripción
article_title: Grupos de suscripción
page_order: 4
description: "Aprende cómo funcionan los grupos de suscripción en los canales de Braze, cómo crearlos y gestionarlos, y el comportamiento específico de cada canal para correo electrónico, WhatsApp, servicio de mensajes cortos, MMS, RCS y LINE."
---

# Grupos de suscripción {#subscription-groups}

> Aprende cómo funcionan los grupos de suscripción en los canales de Braze, cómo crearlos y gestionarlos en el panel, y dónde se aplican las reglas específicas de cada canal.

Los grupos de suscripción controlan qué usuarios pueden recibir mensajes de un conjunto específico de recursos de envío dentro de un canal.

Para el correo electrónico, los grupos de suscripción son filtros de categoría opcionales sobre el estado de suscripción global. Para servicio de mensajes cortos, WhatsApp y LINE, los grupos de suscripción son filtros de audiencia obligatorios para cada envío. Te permiten ofrecer opciones granulares de adhesión voluntaria y cancelación de suscripción, como boletines frente a promociones, o servicio de mensajes cortos transaccionales frente a marketing, sin cambiar el estado de suscripción global del canal de un usuario donde este exista.

Usa los [endpoints de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups) para gestionar programáticamente los grupos de suscripción almacenados en tu espacio de trabajo de Braze.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Estado de suscripción global frente a grupos de suscripción {#global-subscription-state-versus-subscription-groups}

Algunos canales tienen tanto un estado de suscripción global como grupos de suscripción:

| Canal | Estado de suscripción global | Grupos de suscripción |
| --- | --- | --- |
| Correo electrónico | Con adhesión voluntaria, suscrito o dado de baja de todo el correo electrónico | Categorías opcionales (por ejemplo, boletines o promociones) dentro del correo electrónico |
| servicio de mensajes cortos, MMS y RCS | Sin estado global de servicio de mensajes cortos; la suscripción es por grupo | Obligatorio para cada envío; cada grupo contiene números de teléfono de envío o remitentes RCS |
| WhatsApp | Sin estado global de WhatsApp; la suscripción es por grupo | Se crea al integrar WhatsApp; cada grupo se asigna a un número de teléfono de envío |
| LINE | Sin estado global de LINE; la suscripción es por grupo | Se crea por integración de canal de LINE; seguir o dejar de seguir en la aplicación de LINE determina el estado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Estado de suscripción global frente a grupos de suscripción" }

Un usuario puede estar suscrito globalmente al correo electrónico y al mismo tiempo estar dado de baja de un grupo de suscripción de correo electrónico específico. Para servicio de mensajes cortos, un usuario puede estar suscrito a un grupo transaccional y dado de baja de un grupo promocional al mismo tiempo.

## Crear un grupo de suscripción {#create-a-subscription-group}

Cómo se obtiene un grupo de suscripción depende del canal. Los grupos de correo electrónico se crean en el panel; los grupos de servicio de mensajes cortos, MMS y RCS se aprovisionan durante la incorporación; los grupos de WhatsApp y LINE se crean durante la integración del canal. Para detalles de aprovisionamiento específicos de cada canal, consulta [Comportamiento específico del canal](#channel-specific-behavior).

### Correo electrónico {#email}

1. Ve a **Audiencia** > **Administración del grupo de suscripción**.
2. Selecciona **Crear grupo de suscripción de correo electrónico**.
3. Ingresa un nombre y una descripción. Cada grupo de suscripción en tu espacio de trabajo debe tener un nombre único. Si ingresas un nombre que ya existe, el panel muestra un error y no guarda el grupo.
4. Selecciona **Guardar**.

![Campos para crear un grupo de suscripción.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

## Segmentar con grupos de suscripción {#segment-with-subscription-groups}

Cuando creas un segmento, añade un filtro de grupo de suscripción para dirigirte a los usuarios que optaron por ese grupo. Esto es útil para boletines mensuales, programas de cupones, niveles de membresía y otros envíos basados en categorías.

![Ejemplo de segmentación de usuarios en el segmento "Lapsed Users" con el filtro de usuarios en el grupo de suscripción "Weekly Emails".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

## Archivar grupos de suscripción {#archive-subscription-groups}

Los grupos de suscripción archivados no se pueden editar y ya no aparecen en los filtros de segmentos ni en los centros de preferencias. Si archivas un grupo utilizado como filtro de segmento en una Campaign activa, un Canvas o un segmento, recibirás un error hasta que elimines esas referencias.

Para archivar un grupo desde **Administración del grupo de suscripción**, busca el grupo y selecciona **Archivar** desde el menú <i class="fa-solid fa-ellipsis-vertical" aria-label="Más opciones"></i>.

Braze bloquea la mensajería a grupos archivados, por lo que no puedes usar un grupo de suscripción archivado en envíos nuevos o activos.

Algunos canales tienen reglas de archivado adicionales. Consulta [Grupos de suscripción de LINE](#line-subscription-groups) para el comportamiento de espacio de trabajo y reintegración.

## Verificar los grupos de suscripción de un usuario {#check-a-users-subscription-groups}

- **Perfil de usuario:** Abre un perfil desde [Buscar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles). En la pestaña **Participación**, consulta los grupos de suscripción y el estado para correo electrónico, servicio de mensajes cortos, WhatsApp y canales relacionados.
- **REST or transferencia de estado representacional API:** Usa los endpoints [Listar grupos de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) o [Listar estado del grupo de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status).

### Actualizar el estado del grupo de suscripción {#update-subscription-group-status}

Puedes actualizar la pertenencia de un usuario a un grupo de suscripción a través de la REST or transferencia de estado representacional API, el SDK or kit de desarrollo de software, la importación de usuarios, el perfil de usuario, el centro de preferencias de correo electrónico, el paso de actualización de usuario en un Canvas y otros flujos específicos del canal. Los métodos exactos dependen del canal: consulta cada [sección del canal](#channel-specific-behavior) y [Grupos de suscripción de servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#set-a-users-state) para orientación sobre la temporalidad específica de servicio de mensajes cortos.

## Centros de preferencias {#preference-centers}

Los grupos de suscripción de correo electrónico pueden aparecer en un [centro de preferencias de correo electrónico]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) para que los usuarios gestionen las adhesiones voluntarias de correo electrónico a nivel de categoría en un solo lugar. Los grupos de suscripción de correo electrónico activos están disponibles para agregar cuando construyes un centro de preferencias; los centros de preferencias heredados listan todos los grupos de correo electrónico activos automáticamente.

Para servicio de mensajes cortos y WhatsApp, gestiona el estado de suscripción a través de la REST or transferencia de estado representacional API, flujos de adhesión voluntaria, palabras clave (servicio de mensajes cortos), perfil de usuario y otros métodos específicos del canal en cada [sección del canal](#channel-specific-behavior).

## Comportamiento específico del canal {#channel-specific-behavior}

### Grupos de suscripción de correo electrónico {#email-subscription-groups}

Los grupos de suscripción de correo electrónico se sitúan sobre los [estados de suscripción globales de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) (con adhesión voluntaria, suscrito y dado de baja). Los usuarios en el estado global `unsubscribed` no reciben correo electrónico, independientemente de su pertenencia a un grupo de suscripción.

Detalles específicos de correo electrónico:

- **Centro de preferencias:** Cada grupo de suscripción de correo electrónico que crees está disponible para agregar a un centro de preferencias.
- **Análisis de Campaign:** En la página **Rendimiento del mensaje de correo electrónico** de una Campaign, abre **Grupos de suscripción** para ver los recuentos agregados de suscripciones y cancelaciones de suscripción para ese envío.

#### Ver el tamaño de los grupos de suscripción {#viewing-subscription-group-sizes}

En **Administración del grupo de suscripción**, los gráficos de series temporales reportan:

- **Tamaño del grupo de suscripción:** usuarios suscritos a ese grupo en una fecha determinada
- **Tamaño de dados de baja del grupo de suscripción:** usuarios dados de baja de ese grupo en una fecha determinada

Estos recuentos reflejan la pertenencia a ese grupo, no el estado de suscripción global de correo electrónico. Pueden diferir de un segmento que usa **El estado de suscripción de correo electrónico es Dado de baja**, que refleja el [estado de suscripción global de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states).

El tamaño del grupo de suscripción de hoy no se calcula de forma predeterminada. Si tu rango de fechas incluye hoy, selecciona **Calcular las estadísticas de hoy** para añadir el valor de hoy a la serie temporal. Para espacios de trabajo muy grandes, Braze puede mostrar recuentos estimados en lugar de recuentos exactos.

Para pies de página, páginas de cancelación de suscripción y gestión global de suscripción de correo electrónico, consulta [Suscripciones de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions).

### Grupos de suscripción de WhatsApp {#whatsapp-subscription-groups}

Los grupos de suscripción de WhatsApp se crean cuando [integras WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) con tu espacio de trabajo a través del portal de socios tecnológicos.

| Estado | Definición |
| --- | --- |
| Suscrito | El usuario ha confirmado explícitamente que desea recibir mensajes de WhatsApp de tu negocio. Los usuarios pueden suscribirse a través de la API de suscripción de Braze o tu flujo de adhesión voluntaria. |
| Dado de baja | El usuario no optó por la adhesión voluntaria o fue eliminado del grupo. Los usuarios dados de baja no reciben mensajes de WhatsApp de los números de teléfono de ese grupo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de suscripción de WhatsApp" }

WhatsApp requiere una adhesión voluntaria explícita. Las palabras clave de adhesión voluntaria no son compatibles con este canal: tú mantienes el consentimiento y el estado de suscripción. Para flujos de adhesión voluntaria y cancelación de suscripción, consulta [Adhesiones voluntarias y cancelaciones de suscripción en WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs).

Para pasos de archivado, actualizaciones de Canvas y ejemplos de REST or transferencia de estado representacional API, consulta [Grupos de suscripción de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups).

### Grupos de suscripción de servicio de mensajes cortos, MMS y RCS {#sms-mms-and-rcs-subscription-groups}

Los grupos de suscripción de servicio de mensajes cortos, MMS y RCS son la base para enviar mensajes en esos canales. Cada grupo es una colección de [entidades de envío]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup), como códigos abreviados, códigos largos, ID de remitente alfanuméricos o remitentes verificados de RCS, para un propósito de mensajería específico (por ejemplo, transaccional frente a promocional).

| Estado | Definición |
| --- | --- |
| Suscrito | El usuario está suscrito para recibir mensajes de ese grupo de suscripción, a través de la API de suscripción, palabras clave de adhesión voluntaria u otros flujos compatibles. Con la [doble adhesión voluntaria]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) habilitada, los usuarios deben confirmar antes de que el estado se actualice a suscrito. |
| Dado de baja | El usuario canceló la suscripción a través de una palabra clave o actualización de API. Los usuarios dados de baja no reciben servicio de mensajes cortos, MMS ni RCS de los remitentes de ese grupo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de suscripción de servicio de mensajes cortos y RCS" }

Cuando lanzas un mensaje servicio de mensajes cortos o RCS, seleccionas un grupo de suscripción en el creador. Braze añade un filtro de audiencia para que solo se dirija a los usuarios suscritos. Braze no envía servicio de mensajes cortos ni RCS a usuarios que no estén suscritos al grupo seleccionado. Para recibir un mensaje de prueba de servicio de mensajes cortos, el destinatario debe pertenecer al grupo de suscripción que selecciones para la prueba. Para más detalles, consulta [Preguntas frecuentes sobre servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages).

Los grupos de suscripción para servicio de mensajes cortos se aprovisionan durante la incorporación. Para etiquetas de MMS, configuración de remitente RCS, permisos geográficos, migración de RCS y gestión avanzada de cancelación de suscripción, consulta [Grupos de suscripción de servicio de mensajes cortos, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups).

### Grupos de suscripción de LINE {#line-subscription-groups}

Cada grupo de suscripción de LINE se conecta a una integración de canal de LINE.

| Estado | Definición |
| --- | --- |
| Suscrito | El usuario siguió el canal de LINE en la aplicación de LINE. Después de la integración, Braze suscribe a los usuarios cuando siguen el canal. |
| Dado de baja | El usuario no siguió el canal o dejó de seguirlo. Los usuarios dados de baja no reciben mensajes de LINE de ese grupo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de suscripción de LINE" }

LINE es la fuente de verdad para el estado de suscripción. Braze procesa los eventos de seguimiento y cancelación de seguimiento para actualizar los perfiles.

Los grupos de suscripción de LINE no se pueden mover entre espacios de trabajo. Si archivas un grupo y reintegras el canal en otro espacio de trabajo, Braze crea un nuevo grupo de suscripción en el espacio de trabajo de destino.

Para el comportamiento de archivado, reconciliación de usuarios y pasos de integración, consulta [Grupos de suscripción de LINE]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups) y [Configuración de LINE]({{site.baseurl}}/user_guide/channels/line/line_setup).