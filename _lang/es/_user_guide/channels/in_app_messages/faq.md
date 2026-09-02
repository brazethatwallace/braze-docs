---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre mensajes dentro de la aplicación
page_order: 30
description: "Este artículo ofrece respuestas a preguntas frecuentes sobre los mensajes dentro de la aplicación."
tool: in-app messages

---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo ofrece respuestas a algunas preguntas frecuentes sobre los mensajes dentro de la aplicación.

## ¿Qué es un mensaje en el explorador y en qué se diferencia de un mensaje dentro de la aplicación? {#what-is-an-in-browser-message-and-how-does-it-differ-from-an-in-app-message}

Los mensajes en el explorador son mensajes dentro de la aplicación que se envían a navegadores web. Para crear un mensaje en el explorador, asegúrate de seleccionar **Web Browser** en el campo **Send To** al crear tu Campaign de mensajes dentro de la aplicación o Canvas.

## ¿Se muestra un mensaje dentro de la aplicación si un dispositivo está sin conexión? {#does-an-in-app-message-display-if-a-device-is-offline}

Depende. Dado que los mensajes dentro de la aplicación se entregan al inicio de la sesión, si el dispositivo puede descargar la carga útil antes de quedarse sin conexión, el mensaje dentro de la aplicación aún puede mostrarse sin conexión. Si la carga útil no se descarga, el mensaje dentro de la aplicación no se muestra.

## Si un usuario ya tiene una carga útil de mensaje dentro de la aplicación en su dispositivo y se cambia la expiración del mensaje, ¿se actualiza la expiración en su dispositivo? {#if-a-user-already-has-an-in-app-message-payload-on-their-device-and-the-message-expiration-is-changed-does-the-expiration-update-on-their-device}

Cuando un usuario inicia una sesión, Braze comprueba si se han realizado cambios en algún mensaje dentro de la aplicación para el que sea elegible y los actualiza en consecuencia. Por lo tanto, si la expiración ha cambiado y el usuario registra una sesión, el mensaje dentro de la aplicación se envía al dispositivo con la información actualizada.

## ¿Cómo configuro las horas tranquilas para una campaña de mensajes dentro de la aplicación? {#how-do-i-set-up-quiet-hours-for-an-in-app-message-campaign}

La característica de horas tranquilas no está disponible para campañas de mensajes dentro de la aplicación. Esta característica se utiliza para evitar que se envíen mensajes a tus usuarios durante horas específicas. En las campañas de mensajes dentro de la aplicación, tus usuarios reciben mensajes dentro de la aplicación solo si están activos en la aplicación.

Como solución alternativa para enviar mensajes dentro de la aplicación durante un horario específico, utiliza el siguiente código de ejemplo en Liquid. Esto permite que el mensaje se cancele si el mensaje dentro de la aplicación se muestra después de las 7:59 p. m. o antes de las 8 a. m. en la zona horaria especificada.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

## ¿Pueden los usuarios recibir un mensaje dentro de la aplicación de nuevo después de descartarlo? {#can-users-receive-an-in-app-message-again-after-they-dismiss-it}

### Campaigns {#campaigns}

Para Campaigns de mensajes dentro de la aplicación, puedes permitir que los usuarios vuelvan a ser elegibles para recibir la Campaign activando la reelegibilidad en **Controles de entrega** (**Permitir que los usuarios vuelvan a ser elegibles para recibir la Campaign**). La rapidez con la que pueden recibirla de nuevo depende de la ventana de reelegibilidad que configures y de cómo Braze registró el envío anterior. Consulta [Reelegibilidad para Campaigns y Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) para conocer el comportamiento de las Campaigns, incluida la relación entre la reelegibilidad y la recepción del mensaje.

Si la reelegibilidad está desactivada, los usuarios generalmente no recibirán esa misma Campaign de nuevo basándose únicamente en los criterios de calificación después de haberla recibido.

### Canvas {#canvases}

Para los mensajes dentro de la aplicación enviados desde un Canvas, que un usuario pueda ver el mensaje de nuevo depende de los controles de entrada del Canvas (como permitir que los usuarios vuelvan a entrar al Canvas) y de la configuración de tu paso, no solo de los controles de entrega de la Campaign.

## ¿Cuándo se calcula la elegibilidad para un mensaje dentro de la aplicación? {#when-is-eligibility-for-an-in-app-message-calculated}

La elegibilidad para un mensaje dentro de la aplicación se calcula en el momento de la entrega. Si un mensaje dentro de la aplicación está programado para enviarse a las 7 a. m., entonces la elegibilidad se comprueba para ese mensaje dentro de la aplicación a las 7 a. m.

Cuando aparece el mensaje dentro de la aplicación, la elegibilidad depende de cuándo se descarga y se desencadena el mensaje dentro de la aplicación.

## ¿Por qué mi Campaign de mensajes dentro de la aplicación archivada sigue registrando impresiones de mensajes dentro de la aplicación? {#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions}

Esto puede ocurrir con usuarios que cumplieron los criterios del Segment cuando la Campaign de mensajes dentro de la aplicación estaba activa.

Para evitarlo, durante la configuración de tu Campaign, selecciona **Reevaluar la elegibilidad de la campaña antes de mostrar**.

## ¿Por qué no veo aperturas en los mensajes dentro de la aplicación? {#why-dont-i-see-opens-for-in-app-messages}

Los mensajes dentro de la aplicación no utilizan una métrica de *Aperturas*. Braze registra *Impresiones* cuando el mensaje se vuelve visible en la pantalla y *Clics* cuando los usuarios interactúan con el cuerpo del mensaje o los botones. Si una exportación o un informe multicanal incluye filas de mensajes dentro de la aplicación, compara *Impresiones* y *Clics* en lugar de aperturas de estilo correo electrónico. Para consultar las definiciones, visita [Informes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting).

## ¿Pueden mostrarse varios mensajes dentro de la aplicación en la misma sesión? {#can-multiple-in-app-messages-display-in-the-same-session}

Sí, pero solo puede mostrarse un mensaje dentro de la aplicación por cada ocurrencia de un [evento desencadenante]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-trigger). Si varias Campaigns de mensajes dentro de la aplicación comparten el mismo desencadenante (por ejemplo, inicio de sesión), solo el mensaje con mayor prioridad se muestra cada vez que ocurre ese desencadenante. Para los desencadenantes de inicio de sesión, esto significa que solo un mensaje puede mostrarse por sesión, y la siguiente oportunidad para mostrar otro mensaje elegible es la sesión siguiente.

Cuando varios mensajes comparten el mismo nivel de prioridad, se muestra primero el mensaje creado más recientemente. Para los desencadenantes de inicio de sesión, el siguiente mensaje más reciente se muestra en una sesión posterior; para otros tipos de desencadenantes, el siguiente mensaje más reciente se muestra la próxima vez que ocurre ese evento desencadenante, que puede ser dentro de la misma sesión o en una sesión posterior.

Para controlar el orden de visualización dentro de un grupo de prioridad, ve a la configuración de entrega de cualquiera de las Campaigns y selecciona **Set exact priority**, luego arrastra y suelta las Campaigns en el orden deseado. Para más detalles, consulta [Elegir una prioridad]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority).

## ¿Cómo se registran las impresiones y los clics de los mensajes dentro de la aplicación? {#how-are-in-app-message-impressions-and-clicks-logged}

Consulta [Informes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting) para saber cómo se registran las impresiones y los clics según la acción del usuario. Para ver ejemplos específicos de mensajes a pantalla completa creados con el editor tradicional, consulta [Métricas de mensajes a pantalla completa por acción del usuario]({{site.baseurl}}/user_guide/channels/in_app_messages/reporting#fullscreen-metrics-by-user-action).

## ¿Cómo calcula Braze la expiración de un mensaje dentro de la aplicación configurada como "después de 1 día(s)"? {#how-does-braze-calculate-an-in-app-message-expiration-set-to-after-1-days}

Braze calcula un tiempo de expiración de un día como 24 horas después de que los usuarios sean elegibles para recibir un mensaje.

## ¿Qué son los mensajes dentro de la aplicación con plantilla? {#what-are-templated-in-app-messages}

Los mensajes dentro de la aplicación se entregan como mensajes dentro de la aplicación con plantilla cuando se selecciona **Reevaluar la elegibilidad de la campaña antes de mostrar** o si alguna de las siguientes etiquetas de Liquid existe en el mensaje:

- `canvas_entry_properties`
- `connected_content`
- Variables de SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Braze también utiliza la entrega con plantilla para Campaigns de mensajes dentro de la aplicación inactivas (Campaigns que siguen activas pero que ya no envían o ya no se necesitan). Estas Campaigns continúan siguiendo sus reglas de audiencia y desencadenamiento configuradas.

Braze también puede utilizar la entrega con plantilla para proteger el rendimiento de la aplicación. Si preparar el contenido de Liquid retrasa una respuesta de sesión más de unos pocos segundos, Braze aplaza el trabajo restante. Esos mensajes se renderizan cuando se desencadenan.

Esto significa que durante el inicio de sesión, el dispositivo recibe el desencadenante de ese mensaje dentro de la aplicación en lugar del mensaje completo. Cuando el usuario desencadena el mensaje dentro de la aplicación, el dispositivo del usuario realiza una solicitud de red para obtener el mensaje real.

{% alert note %}
El mensaje no se entrega si el dispositivo no tiene acceso a Internet. El mensaje podría no entregarse si la lógica de Liquid tarda demasiado en resolverse.
{% endalert %}

Para reducir la cantidad de Liquid que Braze procesa al inicio de sesión, consulta [Optimizar el rendimiento de los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices/prep_guide#optimize-in-app-message-performance).

## ¿Cómo funciona el comportamiento de cancelación para los mensajes dentro de la aplicación? {#how-does-abort-behavior-work-for-in-app-messages}

En Braze, una cancelación ocurre cuando un usuario realiza una acción que lo hace elegible para recibir un mensaje, pero no lo recibe porque la lógica Liquid lo marca como no elegible. Por ejemplo:

1. Sam realiza una acción que debería desencadenar una Campaign de correo electrónico.
2. El cuerpo del correo electrónico contiene lógica Liquid que dice que si un atributo personalizado de puntuación es menor a 50, no enviar este correo electrónico.
3. La puntuación del atributo personalizado de Sam es 20.
4. Braze reconoce que Sam no debería recibir este correo electrónico, y el correo electrónico se cancela.
5. Se registra un evento de cancelación.

Sin embargo, debido a que los mensajes dentro de la aplicación son un canal de extracción (pull), las cancelaciones funcionan de forma un poco diferente para ellos.

### Comportamiento estándar de cancelación de mensajes dentro de la aplicación {#standard-in-app-message-abort-behavior}

Los mensajes dentro de la aplicación son extraídos por el dispositivo al inicio de la sesión y se almacenan en caché en el dispositivo, de modo que, independientemente de la calidad de la conexión a Internet, el mensaje pueda entregarse instantáneamente al usuario. Por ejemplo, si un usuario recibe cinco mensajes dentro de la aplicación durante su sesión, recibe los cinco al inicio de la sesión. Los mensajes se almacenan en caché localmente y aparecen cuando ocurren sus eventos desencadenantes definidos (inicio de sesión, el usuario hace clic en un botón que registra un evento personalizado, u otros).

En otras palabras, la lógica que determina si un mensaje dentro de la aplicación debe cancelarse ocurre **antes** de que el desencadenante haya ocurrido. Para demostrarlo, supongamos que Sam del ejemplo del correo electrónico está suscrito a las notificaciones push.

1. Sam inicia una sesión abriendo una aplicación con tecnología de Braze en su teléfono.
2. Según los criterios de audiencia de las Campaigns activas en el espacio de trabajo, Sam podría ser elegible para cinco Campaigns diferentes. Las cinco se extraen a su teléfono y se almacenan en caché.
3. Sam **no ha** realizado ninguna acción que desencadene estos mensajes, pero podría recibirlos durante la sesión.
4. El Liquid en dos de los mensajes dentro de la aplicación tiene reglas que excluyen a Sam de recibir el mensaje (como que su atributo personalizado de puntuación no sea lo suficientemente alto).
5. Sam no recibe los dos mensajes dentro de la aplicación que lo excluyen, pero sí recibe los otros tres mensajes.
6. No se registran eventos de cancelación.

Braze no registra ningún evento de cancelación en el caso de Sam porque esto no cumple con la definición de una cancelación; Sam **no realizó** ninguna acción que desencadenara los mensajes. Para los mensajes dentro de la aplicación, los usuarios nunca realizan el desencadenante antes de que Braze determine que no deben ver el mensaje.

### Comportamiento de cancelación de mensajes dentro de la aplicación con plantilla {#templated-in-app-message-abort-behavior}

Los [mensajes dentro de la aplicación con plantilla](#what-are-templated-in-app-messages) obligan al SDK a reevaluar si un mensaje debe mostrarse cuando ocurre el evento desencadenante. Esto tiene un comportamiento de cancelación diferente. Para demostrarlo, considera este ejemplo:

1. Sam inicia una sesión de Braze abriendo una aplicación con tecnología de Braze en su teléfono.
2. Los criterios de audiencia de las Campaigns activas dicen que Sam podría ser elegible para un mensaje dentro de la aplicación con plantilla, por lo que la información del desencadenante se envía a su dispositivo sin la carga útil del mensaje.
3. Sam selecciona un botón que registra un evento personalizado, desencadenando el mensaje dentro de la aplicación con plantilla.
4. El dispositivo de Sam realiza una solicitud de red para obtener el mensaje dentro de la aplicación.
5. La lógica Liquid del mensaje lleva a una cancelación, por lo que Braze lo registra como una cancelación; Sam realizó la acción desencadenante antes de esta evaluación.

### Comparación del comportamiento de cancelación de mensajes dentro de la aplicación {#comparing-in-app-message-abort-behavior}

Esta tabla compara los flujos de mensajes dentro de la aplicación que experimentó Sam:

| Mensaje dentro de la aplicación | Comportamiento de cancelación |
| --- | --- |
| Estándar | No se registró un evento de cancelación porque Sam no realizó ninguna acción que desencadenara un mensaje.<br><br>Los mensajes estándar dentro de la aplicación no registran cancelaciones porque la definición de una cancelación es "no vio el mensaje a pesar de realizar la acción desencadenante". Debido a que los mensajes dentro de la aplicación se entregan al dispositivo antes de que ocurran las acciones desencadenantes, no tiene sentido considerar los mensajes dentro de la aplicación omitidos por la lógica Liquid. |
| Con plantilla | Se registró un evento de cancelación porque Sam realizó la acción desencadenante para desencadenar el mensaje dentro de la aplicación con plantilla, pero recibió una cancelación en la evaluación de la plantilla Liquid.<br><br>Los mensajes dentro de la aplicación con plantilla registran cancelaciones porque la evaluación Liquid ocurre después de que se ha realizado la acción desencadenante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparación del comportamiento de cancelación de mensajes dentro de la aplicación" }

### ¿Cuándo se ejecuta Connected Content para los mensajes dentro de la aplicación? {#when-does-connected-content-run-for-in-app-messages}

Para los [mensajes dentro de la aplicación con plantilla](#what-are-templated-in-app-messages), Connected Content y otras etiquetas Liquid se resuelven cuando ocurre el evento desencadenante y el dispositivo solicita la carga útil del mensaje, no cuando el usuario hace clic en un botón dentro del mensaje. Cada solicitud de plantilla puede incluir llamadas de Connected Content para esa visualización.

Si tu HTML hace referencia a datos REST devueltos por Connected Content, esos datos están disponibles durante la sesión en la que se evaluó la plantilla del mensaje. Múltiples botones pueden hacer referencia a la misma respuesta de Connected Content sin desencadenar llamadas adicionales al hacer clic.

### ¿Cuál es el retraso máximo después de un desencadenante para Campaigns de mensajes dentro de la aplicación? {#what-is-the-maximum-delay-after-a-trigger-for-in-app-message-campaigns}

Las Campaigns de mensajes dentro de la aplicación pueden retrasar la entrega después del evento desencadenante hasta dos horas (7200 segundos). Las opciones de retraso son **Inmediatamente** y **Después de un retraso**. Para una espera más larga, agrega un paso de [retraso]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) antes de un paso de mensaje dentro de la aplicación en un Canvas. Para la configuración del retraso, consulta [Entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-2-select-delay-length).

### ¿Por qué hay un retraso antes de que se muestre mi mensaje dentro de la aplicación? {#why-is-there-a-delay-before-my-in-app-message-displays}

Los mensajes estándar dentro de la aplicación se muestran tan pronto como la carga útil almacenada en caché está lista después del evento desencadenante. En Android e iOS, las imágenes grandes u otros activos alojados en CDN referenciados en el mensaje pueden agregar un breve retraso mientras esos recursos terminan de descargarse antes de que aparezca el mensaje dentro de la aplicación.

Los [mensajes dentro de la aplicación con plantilla](#what-are-templated-in-app-messages) y las Campaigns con **Reevaluar la elegibilidad de la Campaign antes de mostrar** seleccionado requieren una solicitud de red adicional después del desencadenante antes de que aparezca el mensaje. Esto puede agregar un breve retraso (típicamente menos de 100 ms en una conexión estable). Para obtener más información, consulta [Elegir usuarios objetivo]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-users-to-target).

### ¿Por qué mi mensaje dentro de la aplicación se ve diferente a la vista previa del panel? {#why-does-my-in-app-message-look-different-from-the-dashboard-preview}

Los mensajes dentro de la aplicación entregados pueden diferir de la vista previa del panel cuando:

- Tu integración aplica estilos personalizados o anula la interfaz predeterminada de mensajes dentro de la aplicación en ciertas plataformas
- La vista previa usa un perfil de usuario de prueba con atributos diferentes a los del destinatario
- El contenido con plantilla se resuelve de manera diferente en el momento del envío que en el modo de vista previa

Usa [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) con un usuario de prueba cuyo perfil coincida con tu público objetivo al validar la apariencia.

### ¿Por qué un mensaje dentro de la aplicación de varias páginas usa el mismo fondo en todas las páginas? {#why-does-a-multi-page-in-app-message-use-the-same-background-on-every-page}

Cuando **Imagen de fondo** está habilitada en una página de un mensaje dentro de la aplicación de varias páginas, ese fondo se aplica a todas las páginas del mensaje. Para usar diferentes fondos por página, usa un bloque HTML personalizado con JavaScript para intercambiar imágenes entre páginas.

### ¿Cómo pruebo los mensajes dentro de la aplicación en Web? {#how-do-i-test-web-in-app-messages}

Los envíos de prueba de mensajes dentro de la aplicación Web requieren que push esté habilitado en el dispositivo de prueba porque el flujo de prueba entrega una notificación push que abre la aplicación o el sitio donde se muestra el mensaje dentro de la aplicación. La misma ruta de prueba basada en push se aplica en cualquier plataforma donde push no esté configurado con Braze, aunque la falta de push se encuentra con mayor frecuencia en Web porque muchas integraciones móviles ya tienen push habilitado. Usa una Campaign en vivo dirigida a un Segment de prueba interno en su lugar. Para los pasos, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

### ¿Los mensajes dentro de la aplicación requieren integración push? {#do-in-app-messages-require-push-integration}

Los mensajes dentro de la aplicación no requieren notificaciones push para funcionar en producción. Los mensajes dentro de la aplicación se entregan a través del SDK de Braze y aparecen durante una sesión activa de la aplicación sin necesidad de integración push.

Sin embargo, los envíos de prueba de mensajes dentro de la aplicación sí requieren que push esté habilitado en tus dispositivos de prueba. Esto se debe a que los mensajes de prueba dentro de la aplicación se entregan a través de una notificación push que desencadena la visualización del mensaje dentro de la aplicación. El usuario de prueba debe tener push habilitado y debe tocar la notificación push de prueba para ver el mensaje dentro de la aplicación.

Para Campaigns en producción, los usuarios ven los mensajes dentro de la aplicación según los desencadenantes de tu Campaign (como inicio de sesión o eventos personalizados) sin que push esté involucrado.

### ¿Por qué aparecen caracteres adicionales o no renderizados en mi mensaje dentro de la aplicación? {#why-do-extra-or-unrendered-characters-appear-in-my-in-app-message}

Copiar texto de otra aplicación (como un procesador de texto o una página web) puede insertar caracteres invisibles o no imprimibles en el cuerpo de tu mensaje. Esos caracteres pueden aparecer como símbolos sueltos o romper Liquid y HTML en mensajes personalizados.

Para corregir caracteres sueltos o no renderizados, vuelve a escribir el texto afectado en el editor de Braze, o elimina los caracteres no deseados directamente en lugar de seleccionar y reemplazar solo el texto visible. Para mensajes HTML personalizados con caracteres especiales, agrega `<meta charset="UTF-8">` dentro de tu `<head>` HTML. Consulta [Codificación de caracteres]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding) para más detalles.

## ¿Por qué el botón de cierre está oculto en los mensajes HTML dentro de la aplicación a pantalla completa en Android? {#why-is-the-close-button-hidden-on-full-screen-html-in-app-messages-on-android}

En dispositivos con pantallas de borde a borde (incluido Android 15+), los mensajes HTML dentro de la aplicación a pantalla completa pueden dibujarse detrás de la barra de estado del sistema y ocultar un control de cierre en la parte superior del diseño.

La versión 37.0.0 y posteriores del SDK de Braze para Android aplican los márgenes de ventana a los mensajes HTML dentro de la aplicación de forma predeterminada, de modo que los controles permanezcan en el área segura. Si los usuarios siguen viendo superposición, actualiza a la última versión del SDK de Braze para Android.

En versiones anteriores del SDK, los desarrolladores podían habilitar `BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled(true)` antes de que este comportamiento se convirtiera en el predeterminado.

## ¿Qué debo saber al personalizar mensajes dentro de la aplicación de arrastrar y soltar? {#what-should-i-know-when-customizing-drag-and-drop-in-app-messages}

El [editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop) admite los tipos de visualización modal y pantalla completa. Tú construyes el contenido dentro de esos contenedores con bloques de editor.

Ten en cuenta lo siguiente:

- **Enlaces y vínculos profundos:** Cada acción de clic tiene un campo de URL de forma predeterminada. Usa Liquid en la URL para variar los enlaces según el dispositivo, el tipo de aplicación o los atributos del usuario. En el **Contenedor de mensajes**, también puedes activar el comportamiento de clic específico por plataforma para establecer enlaces diferentes por plataforma.
- **Opacidad y fondos:** La opacidad en el contenedor de mensajes afecta a todo el fondo del mensaje. Los bloques individuales pueden establecer sus propios colores de fondo. Para un control más preciso, añade CSS personalizado en un bloque de código personalizado.
- **Ancho del mensaje:** El ancho máximo del **Contenedor de mensajes** no se puede establecer por debajo de 325 px en el editor, lo que mantiene el contenido legible en pantallas más pequeñas. Usa CSS personalizado si necesitas un diseño más estrecho.
- **Fondos específicos por plataforma:** Un único mensaje utiliza la misma imagen de fondo y los mismos colores en la Web y en dispositivos móviles. No puedes establecer fondos diferentes por plataforma en el editor.
- **Mensajes de varias páginas:** Las imágenes de fondo y las acciones de clic a nivel de mensaje se aplican en todas las páginas de un mensaje de varias páginas. Para usar imágenes completas diferentes en cada página, añade botones que enlacen a la página siguiente.
- **Estilos a nivel de mensaje:** Los estilos a nivel de mensaje se aplican a todo el mensaje.
- **Imágenes de fondo:** Las imágenes de fondo se estiran para ajustarse al modal.

Para más consideraciones sobre el editor, consulta la [Guía de preparación de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices/prep_guide#drag-and-drop-editor-considerations).

## ¿Qué significa "Event was published, but no subscribers were found" en los registros del SDK de Android? {#what-does-event-was-published-but-no-subscribers-were-found-mean-in-android-sdk-logs}

Esta línea de registro generalmente no es un error. Suele aparecer cuando Braze publica un evento interno (como `NoMatchingTriggerEvent`) y no hay ningún oyente de mensajes dentro de la aplicación o Content Cards suscrito en ese momento.

Si ves este registro cuando esperas que un evento personalizado desencadene un mensaje dentro de la aplicación, confirma que el evento se ha registrado, que el usuario está en la audiencia de la Campaign o Canvas, y que las Content Cards están sincronizadas cuando el mensaje depende de ellas.