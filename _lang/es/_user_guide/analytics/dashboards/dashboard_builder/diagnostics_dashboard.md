---
nav_title: Dashboard de diagnóstico de mensajería
article_title: Dashboard de diagnóstico de mensajería
description: "Este artículo de referencia cubre el dashboard de diagnóstico de mensajería, que te ayuda a entender por qué los mensajes de tus Campaigns o Canvas pueden no haberse enviado como se esperaba."
alias: /ccdd/
page_order: 2
toc_headers: h2
---

# Dashboard de diagnóstico de mensajería {#messaging-diagnostics-dashboard}

> El dashboard de **diagnóstico de mensajería** proporciona un desglose de alto nivel de los resultados del envío de mensajes, lo que te permite detectar tendencias y diagnosticar posibles problemas en tu configuración de mensajería. Este dashboard puede ayudarte a entender por qué los mensajes de tus Campaigns o Canvas pueden no haberse enviado como se esperaba.

{% alert important %}
El dashboard de **diagnóstico de mensajería** está disponible de forma general. Ponte en contacto con tu administrador de éxito de cliente si te interesa obtener acceso a esta característica.
{% endalert %}

{% alert note %}
Para acceder al dashboard de **diagnóstico de mensajería**, necesitas el [permiso de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "View Dashboard Reports" en tu espacio de trabajo.
{% endalert %}

## Conceptos clave {#key-concepts}

### Enviado y entregado {#sent-and-delivered}

Es fundamental entender que este panel informa sobre cómo Braze procesó internamente un mensaje, no sobre el estado final de entrega del mensaje.

Un mensaje marcado como "enviado" en este panel significa que Braze procesó y despachó el mensaje con éxito. Para la mayoría de los canales, esto significa que Braze entregó el mensaje al partner de envío externo correspondiente. Sin embargo, no garantiza la entrega final al dispositivo del usuario.

Cuando Braze "envía" un mensaje, la entrega final puede depender de servicios externos. Considera los siguientes ejemplos para cada canal.

| Canal | Ejemplo de entrega final |
| --- | --- |
| Content Cards | La tarjeta fue enviada y es elegible para ser vista. |
| Correo electrónico | Braze entrega el mensaje a un proveedor de servicios de correo electrónico (ESP). El ESP es entonces responsable de la entrega final. Ese ESP, por ejemplo, puede reportar un "rebote" si la dirección de correo electrónico no es válida o el buzón de entrada está lleno. |
| In-App Messages | El mensaje fue visto por el usuario y se registró una impresión. |
| LINE | El mensaje fue entregado con éxito a un partner de envío. |
| Push | Braze entrega el mensaje al servicio de notificaciones push correspondiente (como Apple Push Notification service para iOS o Firebase Cloud Messaging para Android). Ese servicio es responsable de la entrega final de la notificación al dispositivo. |
| SMS/MMS/RCS | Braze entrega el mensaje a una pasarela SMS (como Twilio). Esa pasarela es responsable de la entrega final al operador móvil. |
| Webhooks | La solicitud del webhook se realizó con éxito, devolviendo una respuesta `2xx`. |
| WhatsApp | El mensaje fue entregado con éxito a un partner de envío. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enviado y entregado" }

### Actualización de los datos {#data-freshness}

La frecuencia con la que se actualizan los datos en este panel puede variar en función de la carga del sistema. Aunque la frecuencia de actualización no está garantizada, es probable que sea inferior a una hora en la mayoría de los casos.

## Configuración del panel {#configuring-the-dashboard}

Puedes acceder al panel de diagnóstico yendo a **Analytics** > **Dashboard Builder** y seleccionando **Messaging Diagnostics** de la lista de paneles creados por Braze.

Para ejecutar el panel y ver tus datos:

1. Elige **Campaigns** o **Canvas** como la fuente para los informes de tu panel.
2. Selecciona una o más Campaigns o Canvas.
3. Selecciona **Run Dashboard** para cargar los datos de los filtros seleccionados.

![Ejemplo de diagnóstico de Campaign y Canvas del 25 al 31 de mayo de 2025 para una campaña de serie de bienvenida.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Ejemplo de diagnóstico de Campaign y Canvas con gráfico al pasar el cursor del 25 al 31 de mayo de 2025 para una campaña de serie de bienvenida.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

## Interpretación de los datos {#interpreting-the-data}

{% alert note %}
El panel muestra solo hasta los últimos siete días de datos. Todas las marcas de tiempo se muestran en la zona horaria de tu espacio de trabajo.
{% endalert %}

### Mosaicos de resumen {#summary-tiles}

En la parte superior de la página, hay mosaicos de resumen clave para el periodo de tiempo seleccionado que muestran:

- **Enviados:** El recuento total de mensajes que Braze procesó y envió correctamente.
  - **Correo electrónico, SMS/MMS/RCS, WhatsApp, LINE y push:** El mensaje se entregó correctamente a un partner de envío.
  - **Webhooks:** La solicitud de webhook se realizó correctamente y devolvió una respuesta `2xx`.
  - **Content Cards:** La tarjeta se envió y es elegible para ser vista.
  - **In-App Messages:** El mensaje se mostró al usuario.
- **No enviados:** El recuento total de mensajes que fueron cancelados. Esto incluye miembros de la audiencia de Canvas que no entraron al Canvas o salieron del Canvas porque experimentaron un fallo en un paso o cumplieron los criterios de salida mientras realizaban un evento de salida.

### Resultados de mensajes a lo largo del tiempo {#message-outcomes-over-time}

Este gráfico de series temporales muestra un desglose por hora de por qué un mensaje fue cancelado o por qué un usuario fue eliminado de un Canvas. Las etiquetas de resultados en este gráfico son etiquetas normalizadas del panel, no valores sin procesar de la carga útil del evento. Este gráfico no muestra el número de envíos.

### Registro granular de resultados de mensajes {#message-outcomes-granular-log}

El panel muestra una tabla granular de resultados individuales de mensajes para los filtros y el rango de tiempo seleccionados. Usa esta tabla para revisar registros específicos, incluyendo la marca de tiempo, el ID de usuario, el paso en Canvas, el resultado, los detalles y el canal.

Puedes filtrar la tabla para centrarte en registros específicos:

- **Filtrar por resultado:** Selecciona un resultado del filtro de resultados para mostrar solo las filas con ese resultado (por ejemplo, `Frequency capped` o `User not eligible for channel`).
- **Buscar por ID de usuario:** Introduce un ID de usuario en el campo de búsqueda para mostrar las filas de ese usuario específico.

Cuando aplicas ambos filtros, la tabla devuelve las filas que coinciden tanto con el resultado seleccionado como con el ID de usuario introducido.

Selecciona una fila en la tabla para abrir el panel de detalles. El panel de detalles proporciona contexto adicional sobre ese resultado y Ask Operator ofrece orientación de corrección para ayudarte a solucionar el problema subyacente.

![Registro granular de resultados de Messaging Diagnostics con una fila seleccionada y acceso al panel de detalles.]({% image_buster /assets/img/messaging_diagnostics_dashboard_details_log.png %}){: style="max-width:45%;"} ![Panel de detalles de Messaging Diagnostics expandido con contexto del resultado y orientación de corrección.]({% image_buster /assets/img/messaging_diagnostics_dashboard_drawer_expanded.png %}){: style="max-width:45%;"}

{% alert note %}
Los filtros de canal se aplican a resultados que están vinculados a un canal de mensajería específico. Algunos resultados son independientes del canal, por lo que pueden seguir apareciendo en vistas agregadas incluso cuando aplicas un filtro de canal.
{% endalert %}

### Resultados de cancelación {#abort-outcomes}

Las siguientes definiciones explican los resultados de cancelación que se muestran en el panel. Los resultados están agrupados por categoría para facilitar la búsqueda del que estás investigando.

{% alert note %}
Los resultados de cancelación en Messaging Diagnostics son etiquetas legibles del panel. En los [eventos de participación de mensajes de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), la información de cancelación se representa con campos como `abort_type` y `abort_log`. Dado que estos conjuntos de datos tienen representaciones y rutas de procesamiento diferentes, los recuentos o la nomenclatura pueden diferir entre Currents y Messaging Diagnostics.
{% endalert %}

#### Contenido y renderizado {#content-and-rendering}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Content Card expirada | La Content Card expiró antes de que el usuario la viera. |
| Content Card no válida | La Content Card tenía errores y no se envió al usuario. Algunas razones comunes incluyen: {::nomarkdown}<ul><li> Se superó el tamaño máximo (2 KB) </li><li> La fecha de expiración no es válida </li><li> El mensaje contiene caracteres no válidos </li></ul>{:/} |
| Fallo de contenido conectado | Braze intentó enviar el mensaje, pero el contenido conectado falló después del número máximo de reintentos (cinco por defecto). **Nota:** Este recuento representa el número de mensajes cancelados por alcanzar el número máximo de reintentos, no el número total de solicitudes de contenido conectado fallidas. |
| Tiempo de espera de renderizado de mensaje dentro de la aplicación | Después de múltiples intentos de reintento, el Liquid no pudo renderizarse y se agotó el tiempo de espera. |
| Cancelación por Liquid | Se llamó a la etiqueta de Liquid [abort_message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), por lo que se canceló el envío. |
| Tiempo de espera de renderizado de Liquid | El renderizado de la plantilla de Liquid tardó demasiado. Es más probable que ocurra con Banners, mensajes dentro de la aplicación y correo electrónico. |
| Error de sintaxis de Liquid | La plantilla de Liquid tuvo un error de análisis, por lo que se canceló el mensaje. |
| Fallo de URL de medios | Braze no pudo procesar la URL de medios en el mensaje. Esto puede ocurrir cuando la URL está bloqueada, no es válida, se agota el tiempo de espera, devuelve un estado HTTP no válido o falla la validación SSL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Contenido y renderizado" }

#### Estado de Campaign y Canvas {#campaign-and-canvas-state}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Fallo en el paso de retraso | El [paso de retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) falló, lo que provocó que el usuario saliera del Canvas. Este fallo puede ocurrir cuando: {::nomarkdown}<ul><li> La variable proporcionada al paso de retraso personalizado estaba vacía o era de un tipo no válido </li><li> El retraso supera la duración máxima permitida dentro del Canvas</li></ul>{:/} |
| Evento de excepción o de salida | El usuario era previamente elegible para recibir el mensaje, pero {::nomarkdown}<ul><li> realizó un <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-3-select-exception-events">evento de excepción</a> para una Campaign basada en acciones, por lo que se canceló el mensaje, o </li><li> cumplió los <a href="/docs/user_guide/messaging/canvas/create_a_canvas#setting-exit-criteria">criterios de salida</a> del Canvas, por lo que fue eliminado a mitad del recorrido.</li></ul>{:/} |
| Campaign inactiva | La Campaign se detuvo mientras el mensaje estaba en tránsito, por lo que se canceló. |
| Canvas inactivo | El Canvas se detuvo antes de que el usuario entrara en el recorrido. |
| Paso de Canvas inactivo | Esto puede ocurrir en el Canvas si: {::nomarkdown}<ul><li> El paso de Canvas fue eliminado </li> <li>El Canvas se detuvo, lo que hace que todos los pasos se vuelvan inactivos </li></ul>{:/} |
| Límite de volumen alcanzado | La Campaign alcanzó el límite de volumen establecido, por lo que se canceló el envío. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estado de Campaign y Canvas" }

#### Limitación de velocidad y sincronización {#rate-limiting-and-timing}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Limitación de frecuencia | El usuario ya recibió el número máximo de mensajes permitidos según las reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) de tu espacio de trabajo, por lo que se canceló el envío. |
| Cancelación por horas tranquilas | Las horas tranquilas estaban habilitadas para la Campaign o el paso en Canvas con la alternativa configurada como **Cancelar mensaje**. El usuario activó la Campaign o entró en el paso de mensaje del Canvas durante las horas tranquilas, por lo que se canceló el mensaje. Sin embargo, esto no hace que el usuario salga del Canvas. |
| Límite de velocidad superado durante más de 72 horas | El mensaje fue limitado durante más de 72 horas debido a los [límites de velocidad de entrega]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), por lo que se canceló el envío. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limitación de velocidad y sincronización" }

#### Elegibilidad del usuario y perfil {#user-eligibility-and-profile}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Identificador de usuario duplicado | Múltiples usuarios con un identificador coincidente (como ID externo, dirección de correo electrónico, número de teléfono) eran elegibles para recibir este mensaje. Para evitar envíos duplicados al mismo usuario, se canceló este mensaje. |
| El usuario no pasó la verificación previa del paso de mensaje | Braze ejecuta un primer conjunto de verificaciones previas básicas de elegibilidad de audiencia, reelegibilidad y elegibilidad de canal antes de las validaciones completas de entrega para un paso de mensaje de Canvas. Este resultado significa que el usuario o el mensaje no pasó una de esas verificaciones, por lo que se canceló el mensaje para ese paso. |
| El usuario no pasó la verificación previa del mensaje desencadenado | Braze ejecuta un primer conjunto de verificaciones previas básicas de elegibilidad de audiencia, reelegibilidad y elegibilidad de canal antes de crear un mensaje para enviar desde este desencadenador. Este resultado significa que el usuario o el mensaje no pasó una de esas verificaciones, por lo que se canceló el mensaje. |
| El usuario ya no es elegible | El usuario estaba inicialmente en el público objetivo, pero ya no coincidía con los criterios de audiencia antes de que Braze enviara el mensaje o ingresara al usuario en el Canvas. El tiempo entre que el usuario cumplió inicialmente los criterios de audiencia y dejó de cumplirlos puede deberse a retrasos por: {::nomarkdown}<ul><li>Sincronización inteligente</li><li>Horas tranquilas</li><li>Hora local</li><li>Límites de velocidad de entrega (no aplica para la entrada al Canvas)</li><li>Retrasos en la canalización de mensajería</li></ul>{:/} |
| El usuario no es elegible para el paso | El usuario no cumplió las [validaciones de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) establecidas para el paso de mensaje o formaba parte de una [lista de supresión]({{site.baseurl}}/user_guide/audience/suppression_lists). Dependiendo de la configuración de **Validaciones de entrega**, el usuario puede haber salido del Canvas o avanzado al siguiente paso. |
| El usuario no es reelegible | El usuario era elegible para recibir el mensaje o entrar en el Canvas, pero se canceló el envío debido a la configuración de reelegibilidad o reentrada. Esto puede ocurrir si el usuario ya recibió la Campaign o entró en el Canvas demasiado recientemente, si otro envío de la misma Campaign ya está en curso para este usuario, o si la reelegibilidad o la reentrada están desactivadas. |
| Perfil de usuario no encontrado | El usuario nunca existió o ya no existe en Braze. Algunos casos comunes incluyen: {::nomarkdown}<ul><li> El usuario fue segmentado mediante mensajería de API, pero nunca existió en Braze. </li><li>El usuario fue eliminado antes de que se enviara el mensaje o se ejecutara el paso en Canvas. </li><li>El usuario fue fusionado con otro perfil antes de que se enviara el mensaje.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Elegibilidad del usuario y perfil" }

#### Canal y entrega {#channel-and-delivery}

| Resultado de cancelación | Explicación |
| ---- | ---- |
| Error de entrega del partner | Braze intentó enviar este mensaje a tu partner de entrega durante 24 horas, pero el partner devolvió errores temporales durante toda la ventana. |
| Credenciales push no válidas | Las [credenciales push]({{site.baseurl}}/user_guide/channels/push/faqs#why-doesnt-an-opted-in-user-have-a-push-token) para esta aplicación faltan o no son válidas, por lo que se canceló el envío. Actualiza tus credenciales en **Configuración de la aplicación**. |
| Fallo del grupo de suscripción | El mensaje no pudo enviarse debido a problemas de configuración del grupo de suscripción o del servicio de mensajería. Las razones comunes incluyen números de envío faltantes para SMS o WhatsApp, o MMS no compatible en el servicio de mensajería configurado. |
| El usuario no es elegible para el canal | El usuario no es elegible para recibir este mensaje en el canal seleccionado. Las razones comunes incluyen identificadores de canal faltantes o no válidos, tokens de notificaciones push no elegibles, restricciones de estado de suscripción, capacidad de canal no compatible o países bloqueados para canales basados en teléfono. |
| Fallo del webhook | El webhook recibió un código de respuesta no exitoso (distinto de `2xx`). Los códigos de error comunes pueden ser errores de cliente `4XX`, error o tiempo de espera del servidor `5XX`, o `598 Host Unhealthy` o solicitudes detenidas brevemente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canal y entrega" }

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué significa un fallo de "comprobación previa"? {#what-does-a-pre-check-failure-mean}

Una "comprobación previa" se refiere a una verificación de validación agrupada y de alta velocidad que se ejecuta al inicio de una etapa del pipeline (como cuando se desencadena un mensaje o se envía un paso de mensaje en Canvas). Piensa en ella como una salida anticipada diseñada para máxima velocidad. En lugar de ejecutar muchas comprobaciones separadas que consumen muchos recursos (como validar cada detalle del perfil de un usuario), Braze agrupa varias validaciones básicas en una sola "primera pasada".

Si un usuario no supera esta comprobación agrupada, se descarta de inmediato. Este enfoque agrupado permite a Braze procesar volúmenes masivos de mensajes a alta velocidad y puede contribuir a un rendimiento más rápido y estable para tus Campaigns y Canvas al reducir la latencia de procesamiento de cada mensaje.

### ¿Qué significa un resultado de cancelación "otro"? {#what-does-an-other-abort-outcome-mean}

Se trata de cancelaciones que no encajan en las categorías existentes del panel. Si sigues observando una gran proporción de cancelaciones con "Otro", contacta con [soporte de Braze]({{site.baseurl}}/braze_support) para obtener más ayuda.

### ¿Por qué la suma de _No enviados_ y _Enviados_ es menor que el tamaño de audiencia esperado? {#why-is-the-sum-of-_not-sent_-and-_sent_-lower-than-my-expected-audience-size}

Esto puede ocurrir por varias razones:

- **Criterios de audiencia:** Menos usuarios de los esperados pueden haber cumplido los criterios de audiencia (por ejemplo, no estaban en el Segment o no tenían los atributos necesarios) cuando se lanzó la Campaign o el Canvas.
- **Procesamiento en curso:** Es posible que los mensajes aún se estén procesando activamente. Los usuarios pueden estar todavía en pasos anteriores del Canvas y no haber llegado a ningún paso de mensaje.
- **Actualización de datos:** Los datos del panel se actualizan aproximadamente cada 15 minutos, pero esto no está garantizado. Es posible que los datos más recientes de esta Campaign o Canvas aún no hayan llegado al panel.
- **Casos límite:** Existe una pequeña posibilidad de que estés encontrando un caso límite que no se captura en este panel en este momento. Si sospechas que este es el caso, contacta con [soporte de Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### ¿Por qué la suma de _No enviados_ y _Enviados_ es mayor que la audiencia de una Campaign y un Canvas? {#why-is-the-sum-of-_not-sent_-and-_sent_-greater-than-the-audience-for-a-campaign-and-canvas}

Esto puede ocurrir por las siguientes razones:

- **Mensajes multicanal:** La Campaign o el paso en Canvas se configuró para enviar en múltiples canales (como SMS y correo electrónico). Un solo usuario puede recibir un resultado de "enviado" para un canal (como correo electrónico) y un resultado de "cancelación" para otro (como "Usuario no elegible para el canal"). En este caso, ese usuario se contaría dos veces en el gráfico: una como "enviado" y otra como "cancelación".
  - **Ejemplo:** Envías una Campaign push a 100 usuarios, dirigida tanto a iOS como a Android. Si un usuario solo tiene un dispositivo iOS, recibe la notificación push de iOS ("enviado") pero también desencadena una cancelación para la notificación push de Android ("Usuario no elegible para el canal").
- **Múltiples pasos de mensaje (solo Canvas):** Tu Canvas puede tener más de un paso de mensaje en una ruta determinada. Este panel agrega todos los resultados, por lo que un solo usuario podría contarse varias veces si pasa por múltiples pasos de mensaje dentro del rango de tiempo seleccionado.
- **Mensajes de prueba:** Los envíos de prueba (que se cuentan en el panel) hacen que los totales sean mayores que el tamaño de la audiencia.