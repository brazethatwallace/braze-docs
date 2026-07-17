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

> Los grupos de suscripción son la base para enviar mensajes SMS, MMS y RCS a través de Braze. Un grupo de suscripción es una colección de [entidades de envío]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) (como remitentes verificados de RCS, códigos abreviados de SMS, códigos largos de SMS o ID de remitente alfanuméricos de SMS) que se utilizan para un tipo específico de mensajería. Por ejemplo, si una marca planea enviar mensajes SMS tanto transaccionales como promocionales, será necesario configurar dos grupos de suscripción con conjuntos separados de números de teléfono de envío dentro de tu panel de Braze.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Estados de los grupos de suscripción {#subscription-group-states}

Existen dos estados de suscripción para los usuarios de SMS y RCS: `subscribed` y `unsubscribed`. El estado de suscripción de un usuario reside a nivel del grupo de suscripción y no se comparte entre grupos de suscripción, lo que significa que un usuario puede estar `subscribed` a un grupo de suscripción transaccional pero `unsubscribed` de uno promocional. Para las marcas, esta separación de estados garantiza que puedan seguir enviando mensajes SMS y RCS relevantes a sus usuarios.

| Estado | Definición |
| --------- | ---------- |
| Suscrito | El usuario está suscrito para recibir SMS y RCS de un grupo de suscripción específico. Un usuario puede suscribirse ya sea actualizando su estado de suscripción a través de la API de suscripción de Braze o enviando un mensaje de texto con una palabra clave de adhesión voluntaria. Un usuario debe estar suscrito a un grupo de suscripción de SMS o RCS para recibir SMS, RCS o ambos. Cuando la [doble adhesión voluntaria]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) está habilitada, los usuarios deben confirmar su intención de adhesión antes de que su estado de suscripción se actualice a `Subscribed`. |
| Dado de baja | El usuario ha optado explícitamente por no recibir mensajes de tu grupo de suscripción de SMS y RCS y de los números de teléfono de envío dentro del grupo de suscripción. Pueden cancelar la suscripción enviando un mensaje de texto con una palabra clave de cancelación, o puedes cancelar la suscripción de los usuarios a través de la [API de suscripción de Braze]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Los usuarios dados de baja de un grupo de suscripción de SMS y RCS ya no recibirán ningún SMS o RCS de los números de teléfono de envío que pertenezcan al grupo de suscripción.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de los grupos de suscripción" }

### Establecer el estado de un usuario {#set-a-users-state}

Cuando se actualiza un número de teléfono en un perfil de usuario, el nuevo número de teléfono hereda el estado del grupo de suscripción del usuario. Si el número de teléfono se actualiza a un número que ya existe en Braze, se hereda el estado de suscripción de ese número de teléfono existente.

Por ejemplo, si el Usuario A tiene un número de teléfono que está suscrito a varios grupos de suscripción y ese número de teléfono se agrega al Usuario B, el Usuario B estará suscrito a los mismos grupos de suscripción. Para evitar que un usuario herede las suscripciones existentes, puedes restablecer los grupos de suscripción del número anterior a través de la REST API de Braze cada vez que un usuario cambie su número. Si varios usuarios comparten este número de teléfono, todos serán dados de baja.

Para establecer el estado del grupo de suscripción de un usuario, utiliza uno de los siguientes métodos:

- **REST API:** Los perfiles de usuario se pueden configurar programáticamente mediante el [endpoint `/subscription/status/set`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) usando la REST API de Braze.
- **Integración de SDK:** Los usuarios se pueden agregar a un grupo de suscripción de correo electrónico o SMS y RCS usando el método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) o [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Formulario de captura de número de teléfono en IAM:** Los números de teléfono de los usuarios se pueden recopilar a través de la plantilla de captura de número de teléfono en el editor de arrastrar y soltar de mensajes dentro de la aplicación.
- **Gestionado automáticamente al adherirse o cancelar la suscripción del usuario:** Cuando los usuarios envían un mensaje de texto con una [palabra clave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) predeterminada de adhesión o cancelación, Braze configura y actualiza automáticamente el estado de suscripción de los usuarios.
- **Importación de usuarios:** Los usuarios se pueden agregar a grupos de suscripción de correo electrónico o SMS y RCS a través de **Importar usuarios**. Al actualizar el estado del grupo de suscripción, debes tener estas dos columnas en tu CSV: `subscription_group_id` y `subscription_state`. Consulta [Importación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) para más información.

#### Actualizar el estado de un usuario en un Canvas {#update-a-users-state-in-a-canvas}

Al actualizar el estado del grupo de suscripción de un usuario como parte de un flujo de Canvas, utiliza un paso de [Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) en lugar de un webhook. El paso de Actualización de usuario espera a que se complete el procesamiento antes de avanzar al usuario al siguiente paso, de modo que los pasos de mensajería posteriores utilicen el estado de suscripción actualizado.

Si usas un webhook para actualizar los grupos de suscripción, el usuario avanza tan pronto como se envía el webhook, no cuando el cambio de suscripción termina de procesarse. Esto puede crear una condición de carrera en la que un paso de SMS posterior se ejecuta antes de que el usuario esté suscrito, lo que provoca que el mensaje falle para una parte de los usuarios. Si debes usar un webhook, agrega un paso de retraso de al menos 1 minuto antes del siguiente paso de mensajería.

#{% multi_lang_include api/orphaned_subscription_states.md %}

### Verificar el grupo de un usuario {#check-a-users-group}

Para verificar el grupo de suscripción de un usuario, utiliza uno de los siguientes métodos:

- **Perfil de usuario:** Se puede acceder a los perfiles de usuario individuales a través del panel de Braze seleccionando **Búsqueda de usuarios** en la barra lateral. Aquí puedes buscar perfiles de usuario por dirección de correo electrónico, número de teléfono o ID de usuario externo. Dentro de un perfil de usuario, en la pestaña Interacción, puedes ver los grupos de suscripción de SMS y RCS de un usuario.
- **REST API:** El grupo de suscripción de perfiles de usuario individuales se puede consultar mediante el [endpoint Lista de grupos de suscripción de usuarios]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) o el [endpoint Listar el estado del grupo de suscripción del usuario]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) usando la REST API de Braze.

## Enviar mensajes con un grupo de suscripción {#send-messages-with-a-subscription-group}

Para lanzar una campaña de SMS o RCS a través de Braze, selecciona un grupo de suscripción en el menú desplegable **SMS/MMS/RCS Variants**. Una vez seleccionado, se agregará automáticamente un filtro de audiencia a tu campaña o Canvas, asegurando que solo los usuarios `subscribed` al grupo de suscripción seleccionado estén en el público objetivo.

{% alert important %}
De acuerdo con las [normativas y directrices internacionales de telecomunicaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), Braze nunca enviará SMS o RCS a usuarios que no se hayan suscrito al grupo de suscripción seleccionado.
{% endalert %}

![Creador de SMS con el menú desplegable del grupo de suscripción abierto y "Messaging Service A for SMS" resaltado por el usuario.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Mejores prácticas para grupos de suscripción de SMS {#sms-subscription-group-best-practices}

Diseña grupos de suscripción de SMS separados para cada propósito de mensajería (por ejemplo, transaccional versus marketing) y para cada espacio de trabajo. Cuando operas en varios países, considera grupos separados por región para cumplir con las normas de conformidad locales; por ejemplo, las restricciones de Brasil sobre las ventanas de envío promocional.

## Habilitar grupos de suscripción {#enable-subscription-groups}

Para habilitar grupos de suscripción para SMS, MMS o RCS, consulta lo siguiente:

{% tabs local %}
{% tab SMS %}
Durante tu proceso de incorporación de SMS, un administrador de incorporación de Braze configurará los grupos de suscripción para tu cuenta del panel. Trabajará contigo para determinar cuántos grupos de suscripción necesitas y agregará los números de teléfono de envío apropiados a tus grupos de suscripción. Los plazos para configurar un grupo de suscripción dependerán del tipo de números de teléfono que estés agregando. Por ejemplo, las solicitudes de códigos abreviados pueden tardar entre 8 y 12 semanas, mientras que los códigos largos se pueden configurar en un día. Si tienes preguntas sobre la configuración de tu panel de Braze, ponte en contacto con tu representante de Braze para obtener soporte.
{% endtab %}

{% tab MMS %}
Para enviar un mensaje MMS, al menos un número dentro de tu grupo de suscripción debe estar habilitado para enviar MMS. Esto se indica mediante una etiqueta ubicada junto al grupo de suscripción.

![Menú desplegable del grupo de suscripción con "Messaging Service A for SMS" resaltado. La entrada tiene el prefijo de la etiqueta "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Un remitente verificado de RCS debe estar presente dentro de tu grupo de suscripción antes de que puedas enviar un mensaje RCS.

Hay dos formas de agregar un remitente verificado de RCS:
- Agregarlo a un grupo de suscripción existente
- Crear un nuevo grupo de suscripción de RCS
La elección depende en gran medida de los casos de uso de RCS que te interesen.

Dependiendo de tu integración, Braze puede agregar remitentes verificados de RCS a tus grupos de suscripción de SMS existentes o configurar nuevos grupos de suscripción para ti. En cualquier caso, tu administrador de éxito de cliente te guiará a través de una actualización de tráfico SMS fluida y eficiente.
{% endtab %}
{% endtabs %}

## Gestionar cancelaciones de suscripción en lenguaje natural en la Consola de Agente {#handle-natural-language-opt-outs-in-the-agent-console}

Para una gestión integral de suscripciones, puedes capturar la intención de cancelación que queda fuera de las palabras clave estándar o personalizadas (como "Por favor, no me envíes más mensajes"). Al crear un agente de IA, puedes usar el análisis de sentimiento para ayudar a identificar y actuar sobre estas solicitudes automáticamente.

### Configuración {#setup}

1. En la [Consola de Agente]({{site.baseurl}}/user_guide/brazeai/agents), crea un "Agente de análisis de sentimiento de SMS".

{% alert tip %}
Usa [Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) para ayudarte con la configuración inicial del agente.
{% endalert %}

{: start="2"}
2. Crea un Canvas basado en acciones desencadenado por **Send an SMS inbound message**, dentro de la categoría de palabras clave **Other**.
3. Agrega el [paso de Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) al Canvas para identificar la intención de cancelación.
4. Agrega un [paso de Mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) de SMS posterior para confirmar la solicitud: "Parece que estás intentando cancelar la suscripción de SMS, así que vamos a darte de baja. Si esto es un error, envía START para volver a suscribirte."
5. Agrega un [paso de Actualización de usuario]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update#user-update) para cambiar el estado del usuario en el grupo de suscripción de SMS específico a "Dado de baja".

{% alert note %}
El uso de la Consola de Agente consume créditos de mensaje o de acción.
{% endalert %}

## Migrar tráfico de SMS a RCS {#migrate-sms-traffic-to-rcs}

Si tienes grupos de suscripción de SMS y RCS separados, puedes migrar usuarios de SMS a RCS usando un Canvas de un solo paso.

Braze recomienda que primero pruebes el envío de RCS a volúmenes más pequeños de usuarios y migres más usuarios al grupo de suscripción de RCS con el tiempo. Por ejemplo, si tienes 1 000 000 de usuarios suscritos a un grupo de suscripción de SMS, esto podría verse como primero migrar a todos los usuarios al nuevo grupo de suscripción y luego segmentar en una audiencia más pequeña de 50 000 a 100 000 (5-10 %) para probar los mensajes RCS.

### Paso 1: Crear un Canvas y completar el horario de entrada {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Crea un Canvas y nómbralo con algo fácilmente identificable (como "Transferencia de usuarios de grupo de suscripción SMS-RCS"). Luego, programa la campaña cuando te resulte conveniente.

### Paso 2: Definir tu audiencia {#step-2-define-your-audience}
{: #step-2-define-your-audience}

Define tu audiencia usando uno de los siguientes métodos. A continuación, ve al paso **Ajustes de envío** y selecciona **Users who are subscribed or opted-in**.

| Método | Descripción |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Crear un segmento** | Crea un segmento que incluya a todos los usuarios en un grupo de suscripción o un subconjunto usando filtros de segmentación (como un 5-10 % aleatorio). Los segmentos se actualizan antes de cada envío para reflejar tu base de usuarios actual. |
| **Aplicar filtros de campaña o Canvas** | Refina la audiencia en el paso **Público objetivo** de tu campaña o Canvas. Ajusta las opciones de segmentación sin salir de la página para mayor flexibilidad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Definir tu audiencia" }

### Paso 3: Configurar un paso de Actualización de usuario {#step-3-configure-a-user-update-step}

Agrega un paso de Actualización de usuario a tu Canvas. En el paso, abre el **Advanced JSON Editor** e ingresa lo siguiente (para el campo de identificador único de usuario, recomendamos usar el campo `braze_id`):

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

![Objeto de Actualización de usuario que contiene el código JSON indicado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Paso 4: Probar el Canvas {#step-4-test-the-canvas}

Recomendamos encarecidamente [probar tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) para confirmar que funciona como se espera antes de enviarlo a tu audiencia más amplia.

### Paso 5: Lanzar tu Canvas {#step-5-launch-your-canvas}

Después de haber probado exitosamente tu Canvas, ¡adelante y lánzalo para tu subconjunto de usuarios!

Para confirmar que tus usuarios fueron migrados exitosamente, recomendamos verificar algunos perfiles de usuario individuales que fueron actualizados. En la pestaña **Engagement**, busca **Contact Settings** y desplázate para ver los grupos de suscripción a los que el usuario está suscrito. El interruptor del grupo de suscripción de RCS ahora debería estar activado.

Para la configuración del remitente y grupo de suscripción de RCS, consulta también [Configurar RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Mejores prácticas {#best-practices}

### Designar grupos de suscripción separados {#designate-separate-subscription-groups}

- **Tipo de mensajería:** Crea grupos de suscripción distintos para cada tipo de mensajería, como transaccional y marketing.
- **Espacio de trabajo:** Crea grupos de suscripción distintos para cada espacio de trabajo para mantener la claridad y la organización.

Considera el siguiente ejemplo con cuatro grupos de suscripción en dos espacios de trabajo:

- **Espacio de trabajo de producción**
  - Marketing - PROD para SMS
  - Transaccional - PROD para SMS
- **Espacio de trabajo de desarrollo (para pruebas)**
  - Marketing - DEV para SMS
  - Transaccional - DEV para SMS

### Usar convenciones de nomenclatura claras {#use-clear-naming-conventions}

Elige nombres de grupos de suscripción descriptivos y claros para que se seleccione el grupo correcto al crear campañas de SMS.

### Separar grupos por país {#separate-groups-by-country}

Las regulaciones de SMS varían según el país. Sugerimos separar los grupos de suscripción de SMS por país. Esto te ayuda a cumplir con los estándares de conformidad en todas las regiones donde envías mensajes.

Para cada grupo de suscripción, también puedes configurar una lista de países permitidos en **Geographic Permissions** para que los SMS, MMS y RCS solo se envíen a regiones aprobadas. Para más información, consulta [Permisos geográficos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions).

Por ejemplo, en Brasil, el envío de mensajes de marketing fuera del horario de 9 a.m. a 9 p.m. hora local está prohibido, y el país abarca tres zonas horarias. Para cumplir con estas regulaciones, podrías configurar grupos separados para enviar mensajes a Brasil y Estados Unidos. Esto evita que los usuarios en Brasil reciban mensajes de marketing durante las horas prohibidas.