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

Los mensajes en el explorador son mensajes dentro de la aplicación enviados a navegadores web. Para crear un mensaje en el explorador, asegúrate de seleccionar **Web Browser** en el campo **Send To** al crear tu Campaign de mensajes dentro de la aplicación o Canvas.

## ¿Se mostrará un mensaje dentro de la aplicación si el dispositivo está sin conexión? {#does-an-in-app-message-display-if-a-device-is-offline}

Depende. Dado que los mensajes dentro de la aplicación se entregan al inicio de la sesión, si el dispositivo puede descargar la carga útil antes de quedarse sin conexión, el mensaje dentro de la aplicación puede mostrarse mientras está sin conexión. Si la carga útil no se descarga, el mensaje dentro de la aplicación no se mostrará.

## Si un usuario ya tiene la carga útil de un mensaje dentro de la aplicación en su dispositivo y se cambia la expiración del mensaje, ¿se actualizará la expiración en su dispositivo? {#if-a-user-already-has-an-in-app-message-payload-on-their-device-and-the-message-expiration-is-changed-does-the-expiration-update-on-their-device}

Cuando un usuario inicia una sesión, Braze comprueba si se han realizado cambios en los mensajes dentro de la aplicación para los que es elegible y los actualiza en consecuencia. Así que si la expiración ha cambiado y el usuario registra una sesión, el mensaje dentro de la aplicación se envía al dispositivo con la información actualizada.

## ¿Cómo configuro las horas tranquilas para una campaña de mensajes dentro de la aplicación? {#how-do-i-set-up-quiet-hours-for-an-in-app-message-campaign}

La función de horas tranquilas no está disponible para campañas de mensajes dentro de la aplicación. Esta función se utiliza para evitar que se envíen mensajes a tus usuarios durante horas específicas. En las campañas de mensajes dentro de la aplicación, tus usuarios solo recibirán mensajes dentro de la aplicación si están activos en la aplicación.

Como alternativa para enviar mensajes dentro de la aplicación durante un horario específico, utiliza el siguiente código Liquid de ejemplo. Esto permite que el mensaje se cancele si el mensaje dentro de la aplicación se muestra después de las 7:59 pm o antes de las 8 am en la zona horaria especificada.

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

### Campaigns

Para campañas de mensajes dentro de la aplicación, puedes permitir que los usuarios vuelvan a ser elegibles para recibir la campaña activando la reelegibilidad en **Controles de entrega** (**Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña**). La rapidez con la que pueden recibirla de nuevo depende de la ventana de reelegibilidad que establezcas y de cómo Braze registró el envío anterior. Consulta [Reelegibilidad para Campaigns y Canvas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/) para conocer el comportamiento de las campañas, incluyendo cómo la reelegibilidad se relaciona con la recepción de mensajes.

Si la reelegibilidad está desactivada, los usuarios generalmente no recibirán esa misma campaña de nuevo basándose únicamente en los criterios de calificación después de haberla recibido.

### Canvas {#canvases}

Para los mensajes dentro de la aplicación enviados desde un Canvas, que un usuario pueda ver el mensaje de nuevo depende de los controles de entrada del Canvas (como permitir que los usuarios vuelvan a entrar en el Canvas) y de la configuración de tu paso, no solo de los controles de entrega de la campaña.

## ¿Cuándo se calcula la elegibilidad para un mensaje dentro de la aplicación? {#when-is-eligibility-for-an-in-app-message-calculated}

La elegibilidad para un mensaje dentro de la aplicación se calcula en el momento de la entrega. Si un mensaje dentro de la aplicación está programado para enviarse a las 7 am, la elegibilidad se comprueba para este mensaje dentro de la aplicación a las 7 am.

Una vez que se muestra el mensaje dentro de la aplicación, la elegibilidad depende de cuándo se descargó y se desencadenó el mensaje dentro de la aplicación.

## ¿Por qué mi campaña archivada de mensajes dentro de la aplicación sigue generando impresiones de mensajes dentro de la aplicación? {#why-is-my-archived-in-app-message-campaign-still-delivering-in-app-message-impressions}

Esto puede ocurrir con usuarios que cumplieron los criterios del segmento cuando la campaña de mensajes dentro de la aplicación estaba activa.

Para evitar esto, durante la configuración de tu campaña, selecciona **Re-evaluate campaign eligibility before displaying**.

## ¿Pueden mostrarse varios mensajes dentro de la aplicación en la misma sesión? {#can-multiple-in-app-messages-display-in-the-same-session}

Sí, pero solo se puede mostrar un mensaje dentro de la aplicación por cada ocurrencia de un [evento desencadenante]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create/#choose-a-trigger). Si varias campañas de mensajes dentro de la aplicación comparten el mismo desencadenante (por ejemplo, inicio de sesión), solo se muestra el mensaje de mayor prioridad cada vez que ocurre ese desencadenante. Para los desencadenantes de inicio de sesión, esto significa que solo se puede mostrar un mensaje por sesión, y la siguiente oportunidad para mostrar otro mensaje elegible es la siguiente sesión.

Cuando varios mensajes comparten el mismo nivel de prioridad, se muestra primero el mensaje creado más recientemente. Para los desencadenantes de inicio de sesión, el siguiente mensaje más reciente se muestra en una sesión posterior; para otros tipos de desencadenantes, el siguiente mensaje más reciente se muestra la próxima vez que ocurra ese evento desencadenante, lo cual puede ser dentro de la misma sesión o en una sesión posterior.

Para controlar el orden de visualización dentro de un grupo de prioridad, ve a la configuración de entrega de cualquiera de las campañas y selecciona **Establece la prioridad exacta**, luego arrastra y suelta las campañas en el orden deseado. Para más detalles, consulta [Elegir una prioridad]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/create/#choose-a-priority).

## ¿Cómo calcula Braze la expiración de un mensaje dentro de la aplicación configurada como "después de 1 día(s)"? {#how-does-braze-calculate-an-in-app-message-expiration-set-to-after-1-days}

Braze calcula un tiempo de expiración de un día como 24 horas después de que los usuarios sean elegibles para recibir un mensaje.

## ¿Qué son los mensajes dentro de la aplicación con plantilla? {#what-are-templated-in-app-messages}

Los mensajes dentro de la aplicación se entregan como mensajes dentro de la aplicación con plantilla cuando se selecciona **Re-evaluate campaign eligibility before displaying** o si alguna de las siguientes etiquetas de Liquid existe en el mensaje:

- `canvas_entry_properties`
- `connected_content`
- Variables de SMS como {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Esto significa que durante el inicio de sesión, el dispositivo recibe el desencadenante de ese mensaje dentro de la aplicación en lugar del mensaje completo. Cuando el usuario desencadena el mensaje dentro de la aplicación, el dispositivo del usuario realiza una solicitud de red para obtener el mensaje real.

{% alert note %}
El mensaje no se entrega si el dispositivo no tiene acceso a internet. Es posible que el mensaje no se entregue si la lógica de Liquid tarda demasiado en resolverse.
{% endalert %}

## ¿Cómo funciona el comportamiento de cancelación para los mensajes dentro de la aplicación? {#how-does-abort-behavior-work-for-in-app-messages}

En Braze, una cancelación ocurre cuando un usuario realiza una acción que lo hace elegible para recibir un mensaje, pero no recibe el mensaje porque su lógica de Liquid lo marca como no elegible. Por ejemplo:

1. Sam realiza una acción que debería desencadenar una campaña de correo electrónico.
2. El cuerpo del correo electrónico contiene lógica de Liquid que dice que si un atributo personalizado de puntuación es menor que 50, no enviar este correo electrónico.
3. La puntuación del atributo personalizado de Sam es 20.
4. Braze reconoce que Sam no debería recibir este correo electrónico, y el correo electrónico se cancela.
5. Se registra un evento de cancelación.

Sin embargo, dado que los mensajes dentro de la aplicación son un canal de tipo pull, las cancelaciones funcionan de manera un poco diferente para ellos.

### Comportamiento estándar de cancelación de mensajes dentro de la aplicación {#standard-in-app-message-abort-behavior}

Los mensajes dentro de la aplicación son obtenidos por el dispositivo al inicio de la sesión y se almacenan en caché en el dispositivo, por lo que independientemente de la calidad de la conexión a internet, el mensaje puede entregarse instantáneamente al usuario. Por ejemplo, si un usuario recibe cinco mensajes dentro de la aplicación durante su sesión, recibe los cinco al inicio de la sesión. Los mensajes se almacenan en caché localmente y aparecen cuando ocurren sus eventos desencadenantes definidos (inicio de sesión, el usuario hace clic en un botón que registra un evento personalizado, u otros).

En otras palabras, la lógica que determina si un mensaje dentro de la aplicación debe cancelarse ocurre **antes** de que el desencadenante haya ocurrido. Para demostrar esto, supongamos que Sam del ejemplo del correo electrónico está suscrito a notificaciones push.

1. Sam inicia una sesión abriendo una aplicación con tecnología de Braze en su teléfono.
2. Según los criterios de audiencia de las campañas activas en el espacio de trabajo, Sam podría ser elegible para cinco campañas diferentes. Las cinco se descargan en su teléfono y se almacenan en caché.
3. Sam **no ha** realizado ninguna acción que desencadenaría estos mensajes, pero podría recibir esos mensajes en la sesión.
4. El Liquid en dos de los mensajes dentro de la aplicación tiene reglas que excluyen a Sam de recibir el mensaje (como que su atributo personalizado de puntuación no sea lo suficientemente alto).
5. Sam no recibe los dos mensajes dentro de la aplicación que lo excluyen, pero sí recibe los otros tres mensajes.
6. No se registran eventos de cancelación.

Braze no registra ningún evento de cancelación en el caso de Sam porque esto no cumple la definición de una cancelación; Sam **no realizó** ninguna acción que desencadenaría los mensajes. Para los mensajes dentro de la aplicación, los usuarios nunca realizan realmente el desencadenante antes de que Braze determine que no deberían ver el mensaje.

### Comportamiento de cancelación de mensajes dentro de la aplicación con plantilla {#templated-in-app-message-abort-behavior}

Los [mensajes dentro de la aplicación con plantilla](#what-are-templated-in-app-messages) obligan al SDK a reevaluar si un mensaje debe mostrarse cuando ocurre el evento desencadenante. Esto tiene un comportamiento de cancelación diferente. Para demostrarlo, considera este ejemplo:

1. Sam inicia una sesión de Braze abriendo una aplicación con tecnología de Braze en su teléfono.
2. Los criterios de audiencia de las campañas activas dicen que Sam podría ser elegible para un mensaje dentro de la aplicación con plantilla, por lo que la información del desencadenante se envía a su dispositivo sin la carga útil del mensaje.
3. Sam selecciona un botón que registra un evento personalizado, desencadenando el mensaje dentro de la aplicación con plantilla.
4. El dispositivo de Sam realiza una solicitud de red para obtener el mensaje dentro de la aplicación.
5. La lógica de Liquid del mensaje lleva a una cancelación, por lo que Braze lo registra como una cancelación; Sam realizó la acción desencadenante antes de esta evaluación.

### Comparación del comportamiento de cancelación de mensajes dentro de la aplicación {#comparing-in-app-message-abort-behavior}

Esta tabla compara los flujos de mensajes dentro de la aplicación que experimentó Sam:

| Mensaje dentro de la aplicación | Comportamiento de cancelación |
| --- | --- |
| Estándar | No se registró un evento de cancelación porque Sam no realizó ninguna acción que desencadenaría un mensaje.<br><br>Los mensajes dentro de la aplicación estándar no registran cancelaciones porque la definición de una cancelación es "no vio el mensaje a pesar de realizar la acción desencadenante". Dado que los mensajes dentro de la aplicación se entregan al dispositivo antes de que ocurran las acciones desencadenantes, no tiene sentido considerar como cancelados los mensajes dentro de la aplicación omitidos debido a la lógica de Liquid. |
| Con plantilla | Se registró un evento de cancelación porque Sam realizó la acción desencadenante para desencadenar el mensaje dentro de la aplicación con plantilla, pero recibió una cancelación en la plantilla de Liquid.<br><br>Los mensajes dentro de la aplicación con plantilla registran cancelaciones porque la evaluación de Liquid ocurre después de que se ha realizado la acción desencadenante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparación del comportamiento de cancelación de mensajes dentro de la aplicación" }

## ¿Por qué el botón de cierre está oculto en los mensajes dentro de la aplicación HTML de pantalla completa en Android? {#why-is-the-close-button-hidden-on-full-screen-html-in-app-messages-on-android}

En dispositivos con pantallas de borde a borde (incluido Android 15+), los mensajes dentro de la aplicación HTML de pantalla completa pueden dibujarse detrás de la barra de estado del sistema y ocultar un control de cierre en la parte superior del diseño.

La versión 37.0.0 y posteriores del SDK de Braze para Android aplican márgenes de ventana a los mensajes dentro de la aplicación HTML de forma predeterminada para que los controles permanezcan en el área segura. Si los usuarios siguen viendo superposición, actualiza a la última versión del SDK de Braze para Android.

En versiones anteriores del SDK, los desarrolladores podían habilitar `BrazeConfig.setIsHtmlInAppMessageApplyWindowInsetsEnabled(true)` antes de que este comportamiento se convirtiera en el predeterminado.

## ¿Qué debo saber al personalizar mensajes dentro de la aplicación de arrastrar y soltar? {#what-should-i-know-when-customizing-drag-and-drop-in-app-messages}

El [editor de arrastrar y soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/) admite tipos de visualización modal y de pantalla completa. Construyes el contenido dentro de esos contenedores con bloques de editor.

Ten en cuenta lo siguiente:

- **Vínculos y vínculos profundos:** Cada acción de clic tiene un campo de URL de forma predeterminada. Usa Liquid en la URL para variar los vínculos según el dispositivo, el tipo de aplicación o los atributos del usuario. En el **Contenedor del mensaje**, también puedes activar el comportamiento de clic específico por plataforma para establecer vínculos diferentes por plataforma.
- **Opacidad y fondos:** La opacidad en el contenedor del mensaje afecta a todo el fondo del mensaje. Los bloques individuales pueden establecer sus propios colores de fondo. Para un control más preciso, añade CSS personalizado en un bloque de código personalizado.
- **Ancho del mensaje:** El ancho máximo del **Contenedor del mensaje** no se puede establecer por debajo de 325 px en el editor, lo que mantiene el contenido legible en pantallas más pequeñas. Usa CSS personalizado si necesitas un diseño más estrecho.
- **Fondos específicos por plataforma:** Un solo mensaje usa la misma imagen de fondo y colores en web y móvil. No puedes establecer fondos diferentes por plataforma en el editor.
- **Mensajes de varias páginas:** Las imágenes de fondo y las acciones de clic a nivel de mensaje se aplican a todas las páginas en un mensaje de varias páginas. Para usar imágenes completas diferentes en cada página, añade botones que enlacen a la página siguiente.
- **Estilos a nivel de mensaje:** Los estilos a nivel de mensaje se aplican a todo el mensaje.
- **Imágenes de fondo:** Las imágenes de fondo se estiran para ajustarse al modal.

Para más consideraciones del editor, consulta la [Guía de preparación de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/channels/in_app_messages/best_practices/prep_guide/#drag-and-drop-editor-considerations).

## ¿Qué significa "Event was published, but no subscribers were found" en los registros del SDK de Android? {#what-does-event-was-published-but-no-subscribers-were-found-mean-in-android-sdk-logs}

Esta línea de registro generalmente no es un error. A menudo aparece cuando Braze publica un evento interno (como `NoMatchingTriggerEvent`) y ningún listener de mensajes dentro de la aplicación o Content Cards está suscrito en ese momento.

Si ves este registro cuando esperas que un evento personalizado desencadene un mensaje dentro de la aplicación, confirma que el evento se registró, que el usuario está en la audiencia de la Campaign o Canvas, y que las Content Cards están sincronizadas cuando el mensaje depende de ellas.