---
nav_title: Dashboard de diagnóstico de mensajería
article_title: Dashboard de diagnóstico de mensajería
description: "Este artículo de referencia cubre el dashboard de diagnóstico de mensajería, que te ayuda a entender por qué los mensajes de tus campañas o Canvas pueden no haberse enviado como se esperaba."
alias: /ccdd/
page_order: 2
toc_headers: h2
---

# Dashboard de diagnóstico de mensajería {#messaging-diagnostics-dashboard}

> El dashboard de **diagnóstico de mensajería** proporciona un desglose de alto nivel de los resultados del envío de mensajes, lo que te permite detectar tendencias y diagnosticar posibles problemas en tu configuración de mensajería. Este dashboard puede ayudarte a entender por qué los mensajes de tus campañas o Canvas pueden no haberse enviado como se esperaba.

{% alert important %}
El dashboard de **diagnóstico de mensajería** se encuentra actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si te interesa participar en el acceso anticipado.
{% endalert %}

## Conceptos clave {#key-concepts}

### Enviado y entregado {#sent-and-delivered}

Es fundamental entender que este dashboard informa sobre cómo Braze procesó internamente un mensaje, no sobre el estado final de entrega del mensaje.

Un mensaje marcado como "enviado" en este dashboard significa que Braze procesó y despachó el mensaje con éxito. Para la mayoría de los canales, esto significa que Braze entregó el mensaje al socio de envío externo correspondiente. Sin embargo, no garantiza la entrega final al dispositivo del usuario.

Cuando Braze "envía" un mensaje, la entrega final puede depender de servicios externos. Considera los siguientes ejemplos para cada canal.

| Canal | Ejemplo de entrega final |
| --- | --- |
| Content Cards | La tarjeta fue enviada y es elegible para ser vista. |
| Correo electrónico | Braze entrega el mensaje a un proveedor de servicios de correo electrónico (ESP). El ESP es entonces responsable de la entrega final. Ese ESP, por ejemplo, puede reportar un "rebote" si la dirección de correo electrónico no es válida o el buzón de entrada está lleno. |
| Mensajes dentro de la aplicación | El mensaje fue mostrado al usuario. |
| LINE | El mensaje fue entregado con éxito a un socio de envío. |
| Push | Braze entrega el mensaje al servicio de notificaciones push correspondiente (como Apple Push Notification service para iOS o Firebase Cloud Messaging para Android). Ese servicio es responsable de la entrega final de la notificación al dispositivo. |
| SMS/MMS/RCS | Braze entrega el mensaje a una pasarela SMS (como Twilio). Esa pasarela es responsable de la entrega final al operador móvil. |
| Webhooks | La solicitud del webhook se realizó con éxito, devolviendo una respuesta `2xx`. |
| WhatsApp | El mensaje fue entregado con éxito a un socio de envío. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sent and delivered" }

### Actualización de datos {#data-freshness}

La frecuencia con la que se actualizan los datos en este dashboard puede variar según la carga del sistema. Aunque la frecuencia de actualización no está garantizada, es probable que sea inferior a una hora en la mayoría de los casos.

## Configurar el dashboard {#configuring-the-dashboard}

Puedes acceder al dashboard de diagnóstico yendo a **Analytics** > **Dashboard Builder** y seleccionando **Messaging Diagnostics** de la lista de dashboards creados por Braze.

Para ejecutar el dashboard y ver tus datos:

1. Elige **Campaigns** o **Canvases** como fuente para los informes de tu dashboard.
2. Selecciona una o más campañas o Canvas.
3. Selecciona **Run Dashboard** para cargar los datos de los filtros seleccionados.

![Ejemplo de diagnóstico de Campaign y Canvas del 25 al 31 de mayo de 2025 para una campaña de serie de bienvenida.]({% image_buster /assets/img/messaging_diagnostics_dashboard_early_access.png %}){: style="max-width:45%;"} ![Ejemplo de diagnóstico de Campaign y Canvas con gráfico al pasar el cursor del 25 al 31 de mayo de 2025 para una campaña de serie de bienvenida.]({% image_buster /assets/img/messaging_diagnostics_dashboard_graph_on_hover.png %}){: style="max-width:45%;"}

## Interpretar los datos {#interpreting-the-data}

{% alert note %}
El dashboard muestra solo los últimos siete días de datos como máximo. Todas las marcas de tiempo se muestran en la zona horaria de tu espacio de trabajo.
{% endalert %}

### Mosaicos de resumen {#summary-tiles}

En la parte superior de la página, hay mosaicos de resumen clave para el período de tiempo seleccionado que muestran:

- **Total Aborts:** El recuento total de mensajes que fueron cancelados. Esto incluye miembros de la audiencia de Canvas que no entraron al Canvas o salieron del Canvas porque experimentaron un fallo en un paso o cumplieron los criterios de salida al realizar un evento de salida.
- **Message Sends:** El recuento total de mensajes que Braze procesó y envió con éxito.
  - **Correo electrónico, SMS/MMS/RCS, WhatsApp, LINE y push:** El mensaje fue entregado con éxito a un socio de envío.
  - **Webhooks:** La solicitud del webhook se realizó con éxito, devolviendo una respuesta `2xx`.
  - **Content Cards:** La tarjeta fue enviada y es elegible para ser vista.
  - **Mensajes dentro de la aplicación:** El mensaje fue mostrado al usuario.

### Resultados de mensajes a lo largo del tiempo {#message-outcomes-over-time}

Este gráfico de series temporales muestra un desglose día a día de las diferentes razones por las que un mensaje fue cancelado o un usuario fue eliminado de un Canvas. Este gráfico no muestra el número de envíos.

{% alert note %}
Para mantener el gráfico organizado, cualquier razón de cancelación o eliminación con cero ocurrencias en el rango de tiempo seleccionado no aparece en el gráfico.
{% endalert %}

### Registro granular de resultados de mensajes {#message-outcomes-granular-log}

Debajo del gráfico de series temporales, el dashboard muestra una tabla granular de resultados individuales de mensajes para los filtros y el rango de tiempo seleccionados. Usa esta tabla para revisar registros específicos, incluyendo la marca de tiempo, el ID de usuario, el paso en Canvas, el resultado y el canal.

Puedes filtrar la tabla para enfocarte en registros específicos:

- **Filtrar por resultado:** Selecciona un resultado del filtro de resultados para mostrar solo las filas con ese resultado (por ejemplo, `Frequency capped` o `User not eligible`).
- **Buscar por ID de usuario:** Ingresa un ID de usuario en el campo de búsqueda para mostrar las filas de ese usuario específico.

Cuando aplicas ambos filtros, la tabla devuelve las filas que coinciden tanto con el resultado seleccionado como con el ID de usuario ingresado.

### Resultados de cancelación {#abort-outcomes}

Las siguientes definiciones explican los resultados de cancelación que se muestran en el dashboard. Los resultados están agrupados por categoría para facilitar la búsqueda del que estás investigando.

#### Contenido y renderizado {#content-and-rendering}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Tarjeta de contenido expirada | La tarjeta de contenido expiró antes de que el usuario la viera. |
| Tarjeta de contenido no válida | La tarjeta de contenido tenía errores y no fue enviada al usuario. Algunas razones comunes incluyen: {::nomarkdown}<ul><li> Se excedió el tamaño máximo (2 KB) </li><li> La fecha de expiración no es válida </li><li> El mensaje contiene caracteres no válidos </li></ul>{:/} |
| Fallo de contenido conectado | Braze intentó enviar el mensaje, pero el contenido conectado falló después del número máximo de reintentos (el predeterminado es cinco). **Nota:** Este recuento representa el número de mensajes cancelados por alcanzar el número máximo de reintentos, no el número total de solicitudes de contenido conectado fallidas. |
| Tiempo de espera de renderizado de mensaje dentro de la aplicación | Después de múltiples intentos de reintento, no se pudo renderizar el Liquid y se agotó el tiempo de espera. |
| Cancelación por Liquid | Se llamó a la etiqueta de Liquid [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/), por lo que el envío fue cancelado. |
| Tiempo de espera de renderizado de Liquid | El renderizado de la plantilla de Liquid tardó demasiado. Es más probable que ocurra con banners, mensajes dentro de la aplicación y correo electrónico. |
| Error de sintaxis de Liquid | La plantilla de Liquid tenía un error de análisis, por lo que el mensaje fue cancelado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content and rendering" }

#### Estado de Campaign y Canvas {#campaign-and-canvas-state}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Fallo en paso de retraso | El [paso de retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/#personalized-delays) falló, causando que el usuario saliera del Canvas. Este fallo puede ocurrir cuando: {::nomarkdown}<ul><li> La variable proporcionada al paso de retraso personalizado estaba vacía o era de un tipo no válido </li><li> El retraso supera la duración máxima permitida dentro del Canvas</li></ul>{:/} |
| Evento de excepción o salida | El usuario era previamente elegible para recibir el mensaje, pero {::nomarkdown}<ul><li> realizó un <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-3-select-exception-events">evento de excepción</a> para una campaña basada en acciones, por lo que el mensaje fue cancelado, o </li><li> cumplió los <a href="/docs/user_guide/messaging/canvas/create_a_canvas#setting-exit-criteria">criterios de salida</a> del Canvas, por lo que fue eliminado a mitad del recorrido.</li></ul>{:/} |
| Inactive campaign | La campaña fue detenida mientras el mensaje estaba en tránsito, por lo que fue cancelado. |
| Inactive Canvas | El Canvas fue detenido antes de que el usuario entrara al recorrido. |
| Inactive Canvas step | Esto puede ocurrir en el Canvas si: {::nomarkdown}<ul><li> El paso en Canvas fue eliminado </li> <li>El Canvas fue detenido, lo que causa que todos los pasos se vuelvan inactivos </li></ul>{:/} |
| Límite de volumen alcanzado | La campaña alcanzó el límite de volumen establecido, por lo que el envío fue cancelado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Campaign and Canvas state" }

#### Limitación de velocidad y temporización {#rate-limiting-and-timing}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Limitación de frecuencia | El usuario ya recibió el número máximo de mensajes permitidos según las reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#about-frequency-capping) de tu espacio de trabajo, por lo que el envío fue cancelado. |
| Cancelación por horas tranquilas | Las horas tranquilas estaban habilitadas para la campaña o el paso en Canvas con la alternativa configurada como **Abort message**. El usuario desencadenó la campaña o entró al paso de mensaje del Canvas durante las horas tranquilas, por lo que el mensaje fue cancelado. Sin embargo, esto no hace que el usuario salga del Canvas. |
| Límite de velocidad superado por más de 72 horas | El mensaje fue limitado durante más de 72 horas debido a los [límites de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting), por lo que el envío fue cancelado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rate limiting and timing" }

#### Elegibilidad del usuario y perfil {#user-eligibility-and-profile}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Identificador de usuario duplicado | Múltiples usuarios con un identificador coincidente (como ID externo, dirección de correo electrónico, número de teléfono) eran elegibles para recibir este mensaje. Para evitar envíos duplicados al mismo usuario, este mensaje fue cancelado. |
| El usuario no pasó la verificación previa para el paso de mensaje | Esta verificación previa se ejecuta antes de las validaciones de entrega. Cuando esto ocurre, el usuario no cumplió la verificación previa básica para este paso de mensaje (usuario no encontrado o no elegible para el canal del paso de mensaje). **Nota:** Para un paso de mensaje multicanal, esto significa que el usuario no fue encontrado; la elegibilidad del canal solo se verifica aquí para pasos de mensaje de un solo canal. |
| El usuario no pasó la verificación previa para mensaje desencadenado | Para un mensaje desencadenado, Braze ejecuta un primer conjunto de verificaciones previas básicas para la elegibilidad de la audiencia, la re-elegibilidad y la elegibilidad del canal antes de crear un mensaje para enviar desde este desencadenador. |
| El usuario ya no es elegible | El usuario estaba inicialmente en la audiencia objetivo, pero ya no cumplía los criterios de audiencia antes de que Braze enviara el mensaje o ingresara al usuario en el Canvas. El tiempo entre que el usuario cumplió inicialmente los criterios de audiencia y dejó de cumplirlos podría deberse a retrasos por: {::nomarkdown}<ul><li>Intelligent Timing</li><li>Horas tranquilas</li><li>Hora local</li><li>Límites de velocidad de entrega (no aplica para la entrada a Canvas)</li><li>Retrasos en el pipeline de mensajería</li></ul>{:/} |
| El usuario no es elegible para el paso | El usuario no cumplió las [validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#delivery-validations) establecidas para el paso de mensaje o formaba parte de una [lista de supresión]({{site.baseurl}}/user_guide/audience/suppression_lists/). Dependiendo de la configuración de **Delivery validations**, el usuario puede haber salido del Canvas o avanzado al siguiente paso. |
| El usuario no es re-elegible | El usuario era elegible para recibir el mensaje o entrar al Canvas, pero el envío fue cancelado debido a la configuración de re-elegibilidad o re-entrada. Esto puede ocurrir si el usuario ya recibió la campaña o entró al Canvas demasiado recientemente, si otro envío de la misma campaña ya está en curso para este usuario, o si la re-elegibilidad o re-entrada está desactivada. |
| Perfil de usuario no encontrado | El usuario nunca existió o ya no existe en Braze. Algunos casos comunes incluyen: {::nomarkdown}<ul><li> El usuario fue dirigido usando mensajería por API, pero nunca existió en Braze. </li><li>El usuario fue eliminado antes de que el mensaje fuera enviado o el paso en Canvas fuera ejecutado. </li><li>El usuario fue fusionado con otro perfil antes de que el mensaje fuera enviado.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="User eligibility and profile" }

#### Canal y entrega {#channel-and-delivery}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Tiempo de espera de entrega del socio | Braze intentó enviar este mensaje a tu socio de entrega durante 24 horas, pero el socio devolvió errores temporales durante toda la ventana. |
| Credenciales push no válidas | Las [credenciales push]({{site.baseurl}}/user_guide/channels/push/faqs/#valid-push-token) para esta aplicación faltan o no son válidas, por lo que el envío fue cancelado. Actualiza tus credenciales en **Configuración de la aplicación**. |
| El usuario no está habilitado para push de Android, aplicación o dispositivo | No se puede enviar push a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene la aplicación instalada.</li> <li> El usuario no tiene un token de notificaciones push válido. </li> <li>El usuario no tiene el dispositivo necesario para esta notificación push. </li> <li> El usuario ha desactivado las notificaciones para esta aplicación en la configuración de su dispositivo. </li> <li> El usuario no está suscrito ni ha optado por recibir notificaciones push.</li></ul>{:/} |
| El usuario no está habilitado para push de iOS, aplicación o dispositivo | Igual que el resultado de cancelación "El usuario no está habilitado para push de Android, aplicación o dispositivo". |
| El usuario no está habilitado para push de Kindle, aplicación o dispositivo | Igual que el resultado de cancelación "El usuario no está habilitado para push de Android, aplicación o dispositivo". |
| El usuario no está habilitado para notificación push web, aplicación o dispositivo | Igual que el resultado de cancelación "El usuario no está habilitado para push de Android, aplicación o dispositivo". |
| El usuario no está habilitado para Content Cards | El usuario no ha utilizado ninguna aplicación que incluya esta Content Card. |
| El usuario no está habilitado para correo electrónico | No se pueden enviar correos electrónicos a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene una dirección de correo electrónico en su perfil de usuario. </li><li> El estado de suscripción del usuario lo excluye de recibir este correo electrónico. </li><li> La dirección de correo electrónico del usuario ha sido previamente marcada como no válida (rebote duro). </li><li> Los mensajes enviados a esta dirección de correo electrónico son marcados consistentemente como correo no deseado, por lo que el envío fue cancelado.</li></ul>{:/} |
| El usuario no está habilitado para LINE | No se pueden enviar mensajes de LINE a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene un número de teléfono en su perfil de usuario. </li><li> El número de teléfono del usuario ha sido marcado como no válido debido a fallos de entrega. </li><li> El estado de suscripción del usuario lo excluye de recibir este mensaje. </li><li> El usuario no tiene un ID de LINE.</li></ul>{:/} |
| El usuario no está habilitado para SMS/MMS/RCS | No se pueden enviar mensajes SMS a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene un número de teléfono en su perfil de usuario. </li><li> El número de teléfono del usuario ha sido marcado como no válido debido a fallos de entrega. </li><li> El número de teléfono del usuario no está en un formato E.164 válido, y los intentos de formatear automáticamente el número fallaron. </li><li> El estado de suscripción del usuario lo excluye de recibir el mensaje SMS.</li><li>El número de teléfono del usuario está en un país bloqueado.</li></ul>{:/} |
| El usuario no está habilitado para WhatsApp | No se pueden enviar mensajes de WhatsApp a este usuario. Algunas razones comunes: {::nomarkdown}<ul><li> El usuario no tiene un número de teléfono en su perfil de usuario. </li><li> El número de teléfono del usuario ha sido marcado como no válido debido a fallos de entrega. </li><li> El estado de suscripción del usuario lo excluye de recibir este mensaje. </li><li> El usuario no tiene una cuenta de WhatsApp.</li></ul>{:/} |
| Fallo del webhook | El webhook recibió un código de respuesta no exitoso (no `2xx`). Consulta el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/#dev-console-troubleshooting) para más detalles. Los registros con más de 60 horas de antigüedad se limpian y ya no son accesibles; los errores de webhook se muestrean hasta 20 registros por hora. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Channel and delivery" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué significa un fallo de "verificación previa"? {#what-does-a-pre-check-failure-mean}

Una "verificación previa" se refiere a una comprobación de validación agrupada de alta velocidad que se ejecuta al inicio de una etapa del pipeline (como cuando se desencadena un mensaje o se envía un paso de mensaje de Canvas). Piensa en ella como una salida anticipada diseñada para máxima velocidad. En lugar de ejecutar muchas comprobaciones separadas que consumen muchos recursos (como validar cada detalle del perfil de un usuario), Braze agrupa varias validaciones básicas en un "primer paso".

Si un usuario no pasa esta comprobación agrupada, es eliminado inmediatamente. Este enfoque agrupado permite a Braze procesar volúmenes masivos de mensajes a alta velocidad y puede contribuir a un rendimiento más rápido y estable para tus campañas y Canvas al reducir la latencia de procesamiento de cada mensaje.

### ¿Qué significa un resultado de cancelación "otro"? {#what-does-an-other-abort-outcome-mean}

Estas son cancelaciones que no encajaron en ninguna de las categorías preexistentes de Braze. Si notas una gran proporción de cancelaciones con este resultado, ponte en contacto con [soporte de Braze]({{site.baseurl}}/braze_support/) para obtener más ayuda.

### ¿Por qué la suma de _Total Aborts_ y _Message Sends_ es menor que el tamaño esperado de mi audiencia? {#why-is-the-sum-of-_total-aborts_-and-_message-sends_-lower-than-my-expected-audience-size}

Esto puede ocurrir por varias razones:

- **Criterios de audiencia:** Menos usuarios de los esperados pueden haber cumplido los criterios de audiencia (por ejemplo, no estaban en el segmento o no tenían los atributos necesarios) cuando se lanzó la campaña o el Canvas.
- **Procesamiento en curso:** Los mensajes pueden estar aún procesándose activamente. Los usuarios pueden estar todavía en pasos anteriores del Canvas y no haber llegado a ningún paso de mensaje.
- **Actualización de datos:** Los datos del dashboard se actualizan aproximadamente cada 15 minutos, pero esto no está garantizado. Los datos más recientes para esta campaña o Canvas pueden no haber llegado al dashboard todavía.
- **Casos límite:** Existe una pequeña posibilidad de que estés encontrando un caso límite que no está capturado en este dashboard en este momento. Si sospechas que este es el caso, ponte en contacto con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support/).

### ¿Por qué la suma de _Total Aborts_ y _Message Sends_ es mayor que la audiencia de una campaña o Canvas? {#why-is-the-sum-of-_total-aborts_-and-_message-sends_-greater-than-the-audience-for-a-campaign-and-canvas}

Esto puede ocurrir por las siguientes razones:

- **Mensajes multicanal:** La campaña o el paso en Canvas fue configurado para enviar en múltiples canales (como SMS y correo electrónico). Un solo usuario puede recibir un resultado de "enviado" para un canal (como correo electrónico) y un resultado de "cancelación" para otro (como "El usuario no está habilitado para SMS/MMS/RCS"). En este caso, ese usuario sería contado dos veces en el gráfico: una vez como "enviado" y otra como "cancelación".
  - **Ejemplo:** Envías una campaña push a 100 usuarios, dirigida tanto a iOS como a Android. Si un usuario solo tiene un dispositivo iOS, recibe el push de iOS ("enviado") pero también desencadena una cancelación para el push de Android ("El usuario no está habilitado para push de Android, aplicación o dispositivo").
- **Múltiples pasos de mensaje (solo Canvas):** Tu Canvas puede tener más de un paso de mensaje en una ruta determinada. Este dashboard agrega todos los resultados, por lo que un solo usuario podría ser contado múltiples veces si pasa por múltiples pasos de mensaje dentro del rango de tiempo seleccionado.
- **Mensajes de prueba:** El envío de pruebas (que se cuenta en el dashboard) hace que los recuentos totales sean mayores que el tamaño de la audiencia.