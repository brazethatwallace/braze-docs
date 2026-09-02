---
nav_title: "Grupos de suscripción"
article_title: Grupos de suscripción de SMS y RCS
page_order: 4
description: "Este artículo de referencia cubre los grupos de suscripción, los estados de suscripción y el proceso de configuración de grupos de suscripción para los canales SMS, MMS y RCS."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS

---

# Grupos de suscripción de SMS, MMS y RCS {#sms-mms-and-rcs-subscription-groups}

> Los grupos de suscripción son la base para enviar mensajes SMS, MMS y RCS a través de Braze. Un grupo de suscripción es una colección de [entidades de envío]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup), como remitentes verificados de RCS, códigos abreviados de SMS, códigos largos de SMS o ID de remitente alfanuméricos de SMS, que se utilizan para un propósito de mensajería específico (por ejemplo, transaccional frente a promocional). Para un resumen multicanal de los grupos de suscripción, consulta [Grupos de suscripción]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups).

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

<a id="subscription-group-states"></a>

## Estados de los grupos de suscripción {#subscription-group-states}
{: #sms-subscription-states}

Existen dos estados de suscripción para los usuarios de SMS y RCS: `subscribed` y `unsubscribed`. El estado de suscripción de un usuario reside a nivel del grupo de suscripción y no se comparte entre grupos de suscripción, lo que significa que un usuario puede estar `subscribed` a un grupo de suscripción transaccional pero `unsubscribed` de uno promocional. Para las marcas, esta separación de estados garantiza que puedan seguir enviando mensajes SMS y RCS relevantes a sus usuarios.

| Estado | Definición |
| --------- | ---------- |
| Suscrito | El usuario está suscrito para recibir SMS y RCS de un grupo de suscripción específico. Un usuario puede suscribirse ya sea actualizando su estado de suscripción a través de la API de suscripción de Braze o enviando un mensaje de texto con una respuesta de palabra clave de adhesión voluntaria. Un usuario debe estar suscrito a un grupo de suscripción de SMS o RCS para recibir SMS, RCS o ambos. Cuando la [doble adhesión voluntaria]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) está habilitada, los usuarios deben confirmar su intención de adhesión antes de que su estado de suscripción se actualice a `Subscribed`. |
| Dado de baja | El usuario ha cancelado explícitamente su suscripción a los mensajes de tu grupo de suscripción de SMS y RCS y de los números de teléfono de envío dentro del grupo de suscripción. Pueden cancelar su suscripción enviando un mensaje de texto con una respuesta de palabra clave de cancelación, o puedes dar de baja a los usuarios a través de la [API de suscripción de Braze]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Los usuarios dados de baja de un grupo de suscripción de SMS y RCS dejan de recibir cualquier SMS o RCS de los números de teléfono de envío que pertenezcan al grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de los grupos de suscripción" }

### Configurar el estado de un usuario {#set-a-users-state}

Cuando se actualiza un número de teléfono en el perfil de un usuario, el nuevo número de teléfono hereda el estado del grupo de suscripción del usuario. Si el número de teléfono se actualiza a un número que ya existe en Braze, se hereda el estado de suscripción de ese número de teléfono existente.

Por ejemplo, si el Usuario A tiene un número de teléfono suscrito a varios grupos de suscripción y ese número de teléfono se añade al Usuario B, el Usuario B queda suscrito a los mismos grupos de suscripción. Para evitar que un usuario herede las suscripciones existentes, puedes restablecer los grupos de suscripción del número anterior a través de la REST API de Braze cada vez que un usuario cambie su número. Si varios usuarios comparten este número de teléfono, todos quedan dados de baja.

Para configurar el estado del grupo de suscripción de un usuario, utiliza uno de los siguientes métodos:

- **REST API:** Usa el [endpoint `/subscription/status/set`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) para configurar programáticamente perfiles de usuario con la REST API de Braze. Cada solicitud puede incluir entre 1 y 25 grupos de suscripción.
- **Integración de SDK:** Los usuarios pueden añadirse o eliminarse de un grupo de suscripción de correo electrónico, SMS o RCS usando `addToSubscriptionGroup` y `removeFromSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) o [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup). Los métodos del SDK no reemplazan los flujos normativos de adhesión voluntaria o cancelación de suscripción gestionados por palabras clave y la REST API.
- **Formulario IAM de captura de número de teléfono:** Los números de teléfono de los usuarios pueden recopilarse a través de la plantilla de captura de número de teléfono en el editor de arrastrar y soltar de mensajes dentro de la aplicación.
- **Gestionado automáticamente en la adhesión voluntaria o cancelación de suscripción del usuario:** Cuando los usuarios envían un mensaje de texto con una [palabra clave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) predeterminada de adhesión voluntaria o cancelación de suscripción, Braze configura y actualiza automáticamente el estado de suscripción de los usuarios.
- **Importación de usuarios**: Los usuarios pueden añadirse a grupos de suscripción de correo electrónico, SMS o RCS a través de **Importar usuarios**. Al actualizar el estado del grupo de suscripción, debes tener estas dos columnas en tu CSV: `subscription_group_id` y `subscription_state`. Consulta [Importación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) para más información.
- **Panel de Braze:** Selecciona **Búsqueda de usuarios** en la barra lateral, abre el perfil de un usuario y actualiza los grupos de suscripción de SMS o RCS en **Configuración de contacto** en la pestaña **Engagement**.
- **Ingesta de datos en la nube (CDI):** Incluye `subscription_group_id` y `subscription_state` en las filas sincronizadas. Consulta [Configuración de tablas de ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup).
- **Paso de actualización de usuario:** Actualiza el estado de suscripción en un Canvas con un paso de [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update). Consulta [Actualizar el estado de un usuario en un Canvas](#update-a-users-state-in-a-canvas) para consideraciones de tiempo.

#### Actualizar el estado de un usuario en un Canvas {#update-a-users-state-in-a-canvas}

Al actualizar el estado del grupo de suscripción de un usuario como parte de un flujo de Canvas, usa un paso de [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) en lugar de un webhook. El paso de Actualización de usuario espera a que se complete el procesamiento antes de avanzar al usuario al siguiente paso, de modo que los pasos de mensajería posteriores utilicen el estado de suscripción actualizado.

Si usas un webhook para actualizar los grupos de suscripción, el usuario avanza tan pronto como se envía el webhook, no cuando el cambio de suscripción termina de procesarse. Esto puede crear una condición de carrera en la que un paso de SMS posterior se ejecuta antes de que el usuario esté suscrito, lo que provoca que el mensaje falle para una parte de los usuarios. Si debes usar un webhook, añade un paso de retraso de al menos 1 minuto antes del siguiente paso de mensajería.

{% multi_lang_include api/orphaned_subscription_states.md %}

### Consultar el grupo de un usuario {#check-a-users-group}

Para consultar el grupo de suscripción de un usuario, utiliza uno de los siguientes métodos:

- **Perfil de usuario:** Se puede acceder a los perfiles de usuario individuales a través del panel de Braze seleccionando **Búsqueda de usuarios** en la barra lateral. Aquí puedes buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID de usuario externo. Dentro del perfil de un usuario, en la pestaña Engagement, puedes ver los grupos de suscripción de SMS y RCS del usuario.
- **REST API:** El grupo de suscripción del perfil de un usuario individual puede consultarse mediante el [endpoint Listar grupos de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) o el [endpoint Listar estado de grupo de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) usando la REST API de Braze.

## Enviar mensajes con un grupo de suscripción {#send-messages-with-a-subscription-group}

Para lanzar una campaña de SMS o RCS a través de Braze, selecciona un grupo de suscripción en el desplegable **SMS/MMS/RCS Variants**. Una vez seleccionado, se añade automáticamente un filtro de audiencia a tu campaña o Canvas, lo que garantiza que solo los usuarios `subscribed` al grupo de suscripción seleccionado formen parte del público objetivo.

Antes de que los usuarios puedan recibir mensajes de una campaña o Canvas, deben estar suscritos al grupo de suscripción seleccionado. Si los envíos fallan para usuarios que de otro modo son válidos, confirma que están suscritos utilizando uno de los métodos en [Configurar el estado de un usuario](#set-a-users-state). Para los requisitos de doble adhesión voluntaria, consulta [Estados de los grupos de suscripción](#sms-subscription-states).

{% alert important %}
En cumplimiento de las [normativas y directrices internacionales de telecomunicaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), Braze nunca envía SMS ni RCS a usuarios que no se hayan suscrito al grupo de suscripción seleccionado.
{% endalert %}

![Creador de SMS con el desplegable de grupo de suscripción abierto y "Messaging Service A for SMS" resaltado por el usuario.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Buenas prácticas para grupos de suscripción de SMS {#sms-subscription-group-best-practices}

Diseña grupos de suscripción de SMS separados para cada propósito de mensajería (por ejemplo, transaccional frente a marketing) y para cada espacio de trabajo. Cuando operes en varios países, considera crear grupos separados por región para cumplir con las normas de cumplimiento locales, por ejemplo, las restricciones de Brasil sobre los horarios de envío promocional.

## Habilitar grupos de suscripción {#enable-subscription-groups}

Para habilitar los grupos de suscripción para SMS, MMS o RCS, consulta lo siguiente:

{% tabs local %}
{% tab SMS %}
Durante el proceso de incorporación de SMS, un administrador de incorporación de Braze configura los grupos de suscripción para tu cuenta del panel. Trabajan contigo para determinar cuántos grupos de suscripción necesitas y añadir los números de teléfono de envío apropiados a tus grupos de suscripción. Los plazos para configurar un grupo de suscripción dependen del tipo de números de teléfono que estés añadiendo. Por ejemplo, las solicitudes de código abreviado pueden tardar entre 8 y 12 semanas, mientras que los códigos largos pueden configurarse en un día. Si tienes preguntas sobre la configuración de tu panel de Braze, ponte en contacto con tu representante de Braze para obtener asistencia.
{% endtab %}

{% tab MMS %}
Para enviar un mensaje MMS, al menos un número dentro de tu grupo de suscripción debe estar habilitado para enviar MMS. Esto se indica mediante una etiqueta situada junto al grupo de suscripción.

![Menú desplegable de grupo de suscripción con "Messaging Service A for SMS" resaltado. La entrada tiene como prefijo la etiqueta "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Un remitente verificado de RCS debe estar presente dentro de tu grupo de suscripción antes de que puedas enviar un mensaje RCS.

Hay dos formas de añadir un remitente verificado de RCS:
- Añadirlo a un grupo de suscripción existente
- Crear un nuevo grupo de suscripción de RCS
La elección depende en gran medida de los ejemplos de RCS que te interesen.

Dependiendo de tu integración, Braze puede añadir remitentes verificados de RCS a tus grupos de suscripción de SMS existentes o configurar nuevos grupos de suscripción para ti. En cualquier caso, tu administrador de éxito de cliente te guiará a través de una actualización de tráfico SMS fluida y eficiente.
{% endtab %}
{% endtabs %}

## Gestionar las cancelaciones de suscripción en lenguaje natural en la consola de agentes {#handle-natural-language-opt-outs-in-the-agent-console}

Para una gestión integral de las suscripciones, puedes capturar la intención de cancelación de suscripción que queda fuera de las palabras clave estándar o personalizadas (como "Por favor, no me envíes mensajes de texto"). Al crear un agente de IA, puedes usar el análisis de sentimiento para ayudar a identificar y actuar sobre estas solicitudes de forma automática.

### Configuración {#setup}

1. En la [consola de agentes]({{site.baseurl}}/user_guide/brazeai/agents), crea un "agente de análisis de sentimiento de SMS".

{% alert tip %}
Usa [Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) para ayudarte con la configuración inicial del agente.
{% endalert %}

{: start="2"}
2. Crea un Canvas basado en acciones que se active mediante **Send an SMS inbound message**, dentro de la categoría de palabras clave **Other**.
3. Añade el [paso de agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) al Canvas para identificar la intención de cancelación de suscripción.
4. Añade un [paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) de SMS posterior para confirmar la solicitud: "Parece que estás intentando cancelar tu suscripción a SMS, así que vamos a darte de baja. Si esto es un error, envía START para volver a suscribirte".
5. Añade un [paso de actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) para cambiar el estado del usuario en el grupo de suscripción de SMS específico a "Unsubscribed".

{% alert note %}
Usar la consola de agentes consume créditos de mensajes o acciones.
{% endalert %}

## Migrar tráfico de SMS a RCS {#migrate-sms-traffic-to-rcs}

Si tienes grupos de suscripción de SMS y RCS separados, puedes migrar usuarios de SMS a RCS usando un Canvas de un solo paso.

Braze recomienda que primero pruebes el envío de RCS a volúmenes más pequeños de usuarios y migres más usuarios al grupo de suscripción de RCS con el tiempo. Por ejemplo, si tienes 1.000.000 de usuarios suscritos a un grupo de suscripción de SMS, podrías migrar primero a todos los usuarios al nuevo grupo de suscripción y luego segmentar a una audiencia más pequeña de 50.000 a 100.000 (5-10%) para probar los mensajes RCS.

### Paso 1: Crea un Canvas y completa la programación de entrada {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Crea un Canvas y nómbralo con algo fácilmente identificable (como "Transferencia de usuarios de grupo de suscripción SMS-RCS"). Luego, programa la campaña en el momento que te resulte conveniente.

### Paso 2: Define tu audiencia {#step-2-define-your-audience}
{: #step-2-define-your-audience}

Define tu audiencia usando uno de los siguientes métodos. A continuación, ve al paso **Configuración de envío** y selecciona **Usuarios que están suscritos o que han dado su adhesión voluntaria**.

| Método | Descripción |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Crear un Segment** | Crea un Segment que incluya a todos los usuarios de un grupo de suscripción o un subconjunto usando filtros de segmentación (como un 5-10% aleatorio). Los Segments se actualizan antes de cada envío para reflejar tu base de usuarios actual. |
| **Aplicar filtros de Campaign o Canvas** | Refina la audiencia en el paso **Público objetivo** de tu Campaign o Canvas. Ajusta las opciones de segmentación sin salir de la página para mayor flexibilidad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Define tu audiencia" }

### Paso 3: Configura un paso de actualización de usuario {#step-3-configure-a-user-update-step}

Añade un paso de actualización de usuario a tu Canvas. En el paso, abre el **Editor JSON avanzado** e introduce lo siguiente (para el campo de identificador único de usuario, recomendamos usar el campo `braze_id`):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

{% alert important %}
Al usar `use_double_opt_in_logic`, ya debe existir un perfil de usuario para que se actualice el estado de suscripción. Si no hay un perfil de usuario asociado con el identificador proporcionado, el estado de suscripción no se actualiza.
{% endalert %}

![Objeto de actualización de usuario que contiene el código JSON mencionado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Paso 4: Prueba el Canvas {#step-4-test-the-canvas}

Recomendamos encarecidamente [probar tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) para confirmar que funciona como se espera antes de enviarlo a tu audiencia más amplia.

### Paso 5: Lanza tu Canvas {#step-5-launch-your-canvas}

Después de haber probado tu Canvas con éxito, ¡lánzalo para tu subconjunto de usuarios!

Para confirmar que tus usuarios fueron migrados con éxito, recomendamos revisar algunos perfiles de usuario individuales que fueron actualizados. En la pestaña **Participación**, busca **Configuración de contacto** y desplázate para ver los grupos de suscripción a los que el usuario está suscrito. El conmutador del grupo de suscripción de RCS debería estar ahora activado.

Para la configuración del remitente y el grupo de suscripción de RCS, consulta también [Configurar RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Buenas prácticas {#best-practices}

### Designa grupos de suscripción separados {#designate-separate-subscription-groups}

- **Tipo de mensajería:** Crea grupos de suscripción distintos para cada tipo de mensajería, como Transaccional y Marketing.
- **Espacio de trabajo:** Crea grupos de suscripción distintos para cada espacio de trabajo para mantener la claridad y la organización.

Considera el siguiente ejemplo con cuatro grupos de suscripción en dos espacios de trabajo:

- **Espacio de trabajo de producción**
  - Marketing - PROD para SMS
  - Transaccional - PROD para SMS
- **Espacio de trabajo de desarrollo (para pruebas)**
  - Marketing - DEV para SMS
  - Transaccional - DEV para SMS

### Usa convenciones de nomenclatura claras {#use-clear-naming-conventions}

Elige nombres de grupo de suscripción descriptivos y claros para que se seleccione el grupo correcto al crear Campaigns de SMS.

### Separa los grupos por país {#separate-groups-by-country}

Las regulaciones de SMS varían según el país. Te sugerimos separar los grupos de suscripción de SMS por país. Esto te ayuda a cumplir con los estándares de conformidad en todas las regiones a las que envías mensajes.

Para cada grupo de suscripción, también puedes configurar una lista de países permitidos en **Permisos geográficos** para que los SMS, MMS y RCS solo se envíen a regiones aprobadas. Para más información, consulta [Permisos geográficos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions).

Por ejemplo, en Brasil está prohibido enviar mensajes de marketing fuera del horario de 9 a. m. a 9 p. m. hora local, y el país abarca tres zonas horarias. Para cumplir con estas regulaciones, podrías configurar grupos separados para enviar mensajes a Brasil y Estados Unidos. Esto evita que los usuarios en Brasil reciban mensajes de marketing durante las horas prohibidas.