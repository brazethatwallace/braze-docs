---
nav_title: Grupos internos
article_title: Grupos internos
page_order: 4
page_type: reference
description: "Este artículo de referencia describe los grupos internos, una excelente forma de obtener información sobre los registros del SDK or kit de desarrollo de software o la API de tu dispositivo de prueba al probar la integración del SDK or kit de desarrollo de software."

---

# Grupos internos {#internal-groups}

> Los grupos internos son una excelente forma de crear y organizar grupos de prueba internos o de terceros. Proporcionan información sobre los registros de tu SDK or kit de desarrollo de software o API y son útiles al probar la integración de tu SDK or kit de desarrollo de software. Puedes crear un número ilimitado de grupos internos personalizados con hasta 1000 usuarios.

{% alert tip %}
También te recomendamos consultar nuestro curso de Braze Learning [Pruebas y solución de problemas](https://learning.braze.com/path/developer/testing-and-troubleshooting), que explica cómo usar los grupos internos para realizar tu propia solución de problemas y depuración.
{% endalert %}

## Requisitos previos {#prerequisites}

Para crear y gestionar grupos internos, necesitas los siguientes [permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions):

- Ver claves de API
- Editar claves de API
- Ver grupos internos
- Editar grupos internos
- Ver registro de actividad de mensajes
- Ver registro de usuarios del evento
- Ver identificadores de API
- Ver panel de uso de API
- Ver límites de API
- Ver alertas de uso de API
- Editar alertas de uso de API
- Editar depurador de SDK or kit de desarrollo de software
- Ver depurador de SDK or kit de desarrollo de software

## Crear un grupo interno {#creating-an-internal-group}

Para crear un grupo interno:

1. Ve a **Configuración** > **Grupos internos**.
2. Selecciona **Crear grupo interno**.
3. Dale un nombre a tu grupo, como "Grupo de prueba de correo electrónico".
4. Elige uno o más tipos de grupo, como se indica en la siguiente tabla.

| Tipo de grupo         | Descripción                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
| **Grupo de eventos de usuario**   | Utiliza esto para verificar eventos o registros desde tu dispositivo de prueba.<br><br>Para capturar registros de SDK or kit de desarrollo de software y REST or transferencia de estado representacional API para los miembros del grupo, selecciona la casilla **Eventos de usuario**. Sin esta configuración, los usuarios añadidos al grupo no mostrarán registros en el [registro de usuarios del evento]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log). |
| **Grupo de prueba de contenido** | Utiliza esto en push, correo electrónico y mensajes dentro de la aplicación para enviar una copia renderizada del mensaje. |
| **Grupo semilla**         | Envía automáticamente una copia del correo electrónico a todos los miembros del grupo semilla en el momento del envío.               |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Crear un grupo interno" }

{:start="5"}
5. Selecciona **Crear grupo interno** de nuevo.

### Añadir usuarios de prueba {#adding-test-users}

Después de crear tu grupo interno, añade usuarios de prueba como miembros de ese grupo.

1. Desde la página de gestión de tu grupo interno, selecciona **Añadir usuarios de prueba**.
2. Elige entre los siguientes métodos para buscar y seleccionar tus usuarios de prueba.

| Método                  | Descripción                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Añadir usuario identificado** | Busca al usuario por su ID externo, dirección de correo electrónico, número de teléfono o token de notificaciones push.                                                                                                                                                           |
| **Añadir usuario anónimo**  | Busca por dirección IP. Luego, proporciona un nombre para cada usuario de prueba que añadas. Este es el nombre con el que se asocian todos los registros de eventos en la página del [registro de usuarios del evento]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log). |
| **Añadir usuarios en bloque**      | Copia y pega una lista de direcciones de correo electrónico o ID externos. Solo puedes añadir usuarios que ya sean conocidos en el panel. Para más información, consulta [Importación de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Añadir usuarios de prueba" }

### Grupos de prueba de contenido {#content-test-groups}

De forma similar a enviar una vista previa de prueba de un mensaje, el grupo de prueba de contenido te ahorra tiempo y te permite lanzar pruebas a una lista predefinida de usuarios de Braze simultáneamente. Esto está disponible para push, mensajes dentro de la aplicación, servicio de mensajes cortos, correo electrónico y Content Cards en Braze. Solo los grupos etiquetados como grupos de prueba de contenido están disponibles en la sección de vista previa de un mensaje.

{% alert note %}
Los mensajes de prueba de [servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) solo se pueden enviar a números de teléfono válidos en la base de datos.
{% endalert %}

Selecciona usuarios individuales de Braze o cualquier número de grupos internos a los que enviar el mensaje. Si tu mensaje incluye Liquid u otra personalización dinámica, Braze utiliza los atributos disponibles para cada usuario para personalizar el contenido del mensaje. Para los usuarios que no tienen atributos, Braze utiliza el valor predeterminado establecido.

Además, si previsualizas el mensaje como un usuario aleatorio, un usuario personalizado o un usuario existente, puedes enviar esa versión previsualizada en su lugar. Desmarcar la casilla te permite enviar basándote en los atributos de cada usuario en lugar de la versión previsualizada.

Si utilizas un grupo de IP para enviar un correo electrónico, selecciona desde qué grupo de IP enviar el correo electrónico eligiéndolo en el menú desplegable disponible.

![La sección de prueba del editor de mensajes dentro de la aplicación para seleccionar el grupo de prueba de contenido.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Grupos semilla {#seed-groups}

Los grupos semilla solo son compatibles con el canal de correo electrónico. Añade usuarios a un grupo semilla para enviar copias de cada variante de mensaje de correo electrónico a todos los miembros del grupo.

Los grupos semilla no están disponibles para Campaigns de API, pero puedes incluir grupos semilla utilizando una entrada activada por API en la Campaign. Utiliza esto para medir métricas de capacidad de entrega y para mantener un registro del contenido de tu correo electrónico con fines históricos y de archivo.

Después de crear un grupo interno y etiquetarlo para ser utilizado como grupo semilla, selecciónalo en el paso **Públicos objetivo** del editor de Campaigns, o en el paso **Configuración de envío** en un Canvas.

Los correos electrónicos semilla tienen `[SEED]` antepuesto a la línea del asunto. Ten en cuenta que los correos electrónicos semilla **no**:

- Incrementan los envíos en los análisis del panel.
- Afectan los análisis de correo electrónico ni la reorientación.
- Actualizan la lista de **Campaigns recibidas** del perfil de usuario.
- Afectan la limitación de frecuencia.
- Cuentan ni afectan los límites de velocidad de entrega.

#### Comportamiento de suscripción {#subscription-behavior}

Los envíos semilla están diseñados para QA y revisión interna, por lo que omiten intencionalmente las verificaciones de suscripción para los usuarios de la empresa incluidos como semilla. Esto significa que los usuarios con direcciones de correo electrónico válidas que forman parte de un grupo semilla reciben el mensaje incluso si no están suscritos. Sin embargo, el mensaje debe estar configurado para enviar copias semilla a ese grupo.

{% alert tip %}
Si los miembros del grupo semilla no ven el mensaje, confirma que están en el grupo interno, utiliza líneas del asunto distintas para que Gmail no agrupe los mensajes, y pídeles que revisen la carpeta de correo no deseado.

Si el correo electrónico utiliza [Liquid `abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), los miembros del grupo semilla aún deben cumplir la condición de cancelación para recibir el envío.
{% endalert %}

#### Para Campaigns {#for-campaigns}

Al redactar una Campaign de correo electrónico, edita tus grupos semilla en la sección **Públicos objetivo** del editor.

{% alert important %}
Si configuras un grupo semilla para que se adjunte automáticamente a todas las Campaigns, esto solo se aplica a las Campaigns nuevas. No se aplica cuando copias Campaigns existentes. Debes aplicar manualmente los grupos semilla deseados a la Campaign copiada en la sección **Públicos objetivo**.
{% endalert %}

Los grupos semilla envían a cada variante de correo electrónico una vez y se entregan la primera vez que tu usuario recibe esa variante en particular. Para mensajes programados, esto suele ser la primera vez que se lanza la Campaign. Para Campaigns basadas en acciones o activadas por API, es el momento en que se envía un mensaje al primer usuario.

Si tu Campaign es multivariante y tu variante tiene un porcentaje de envío del 0 %, no se envía a los grupos semilla. Además, si la variante ya se envió y no se actualizó para reenviar en **Editar grupos semilla** en el paso **Objetivo**, no se envía de nuevo de forma predeterminada.

{% alert note %}
Si tienes una Campaign recurrente y alguna de las variantes se actualiza, puedes elegir enviar de nuevo solo las variantes actualizadas o todas las variantes, o desactivar el envío del grupo semilla tras la actualización.
{% endalert %}

![El grupo semilla "Email seed test" seleccionado para recibir la Campaign de correo electrónico de la variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Para Canvas {#for-canvas}

Los grupos semilla en Canvas funcionan de manera similar a cualquier Campaign activada. Braze detecta automáticamente todos los pasos que contienen un mensaje de correo electrónico y los envía cuando tu usuario llega por primera vez a ese paso de correo electrónico en particular.

Si un paso de correo electrónico se actualizó después de que se envió al grupo semilla, Braze presenta la opción de enviar solo a los pasos actualizados, a todos los pasos, o desactivar los envíos semilla.