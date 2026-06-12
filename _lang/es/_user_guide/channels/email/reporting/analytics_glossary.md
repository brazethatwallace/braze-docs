---
nav_title: Glosario de análisis de correo electrónico
article_title: Glosario de análisis de correo electrónico
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Este glosario incluye los términos que encontrarás en la sección de análisis de tu campaña de correo electrónico o Canvas, tras el lanzamiento. Este glosario no incluye las métricas de Currents."
channel:
  - email
---

> Este glosario define las métricas en la pestaña **Analytics** para campañas de correo electrónico y Canvas. Braze no ofrece una página alojada de «ver este correo electrónico en un navegador»; consulta [¿Puedo agregar un enlace de «ver este correo electrónico en un navegador» a mis correos electrónicos?]({{site.baseurl}}/user_guide/channels/email/faq/#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails) para una solución alternativa. Para otros problemas que abarcan varias métricas, consulta [Preguntas frecuentes sobre correo electrónico]({{site.baseurl}}/user_guide/channels/email/faq/).

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variante {#variation}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Envío por correo electrónico {#emailable}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### % de audiencia {#audience}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatarios en la variante) / (Destinatarios únicos)</span>

{% endapi %}

{% api %}

### Destinatarios únicos {#unique-recipients}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Este número se recibe de Braze.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Envíos {#sends}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Esta métrica la proporciona Braze.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Mensajes enviados {#messages-sent}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Esta métrica la proporciona Braze.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

### Entregas {#deliveries}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Para correos electrónicos, *Entregas* es el número total de mensajes (Envíos) enviados correctamente y recibidos por las partes con direcciones de correo electrónico válidas.

<span class="calculation-line">Cálculo: (Envíos) - (Rebotes) </span>

{% alert note %}
Para el estado de **recibido** a nivel de usuario y la lógica relacionada (como la limitación de frecuencia), Braze generalmente marca a un usuario cuando el envío se procesa y se entrega para su distribución, no cuando el proveedor de servicios de correo electrónico (ESP) confirma la entrega final al buzón de entrada. Esto evita desfases de tiempo entre la confirmación del ESP y las reglas del producto. Puede diferir de los informes de entrega del ESP o de terceros.
{% endalert %}

{% endapi %}

{% api %}

### % de entregas

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Cálculo: (Envíos - Rebotes) / (Envíos) </span>

{% endapi %}

{% api %}

### Rebotes {#bounces}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %}

Para correo electrónico, el *% de rebotes* o la *tasa de rebote* es el porcentaje de mensajes que no se enviaron correctamente o que fueron designados como «devueltos» o «no recibidos» por los servicios de envío utilizados, o que no fueron recibidos por los usuarios con direcciones de correo electrónico válidas.

Un rebote de correo electrónico para clientes que usan SendGrid consiste en rebotes duros, correo no deseado (`spam_report_drops`) y correos electrónicos enviados a direcciones no válidas (`invalid_emails`).

{% alert note %}
En [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), los aplazamientos temporales del ESP a menudo se representan como rebotes blandos. Las herramientas de capacidad de entrega (por ejemplo, los informes nativos de SendGrid o los modelos de Looker) pueden usar aplazamientos para la misma situación. Los aplazamientos suelen ser temporales y el correo a menudo se entrega después de reintentos. Tras reintentos prolongados (hasta aproximadamente 72 horas para rebotes blandos en los análisis de Campaign), un mensaje puede tratarse como no entregable según tu ESP. Los eventos de correo electrónico de Currents son de solo adición: un rebote blando registrado no se elimina posteriormente si el mensaje finalmente se entrega.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Rebotes</i>:</b> Recuento</li>
        <li><b><i>% de rebotes</i> o <i>% de tasa de rebote</i>:</b> (Rebotes) / (Envíos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Rebote duro {#hard-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Cuando un correo electrónico tiene un rebote duro o se marca como correo no deseado, Braze marca la dirección de correo electrónico como no válida, pero no actualiza el [estado de suscripción]({{site.baseurl}}/user_guide/channels/email/subscriptions/) del usuario. Braze detiene cualquier envío futuro a esa dirección de correo electrónico. Para eliminar una dirección de correo electrónico de tu lista de rebotes duros, usa el [punto de conexión para eliminar correos electrónicos con rebote duro]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/).

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Rebote blando {#soft-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un correo electrónico recibe un rebote blando, normalmente se reintentará en un plazo de 72 horas, pero el número de reintentos varía según el receptor.

Aunque los rebotes blandos no se rastrean en los análisis de tu Campaign, puedes monitorear los rebotes blandos en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) o excluir a estos usuarios de tu envío con el [filtro de Segment de rebote blando]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#soft-bounced). En el Registro de actividad de mensajes, también puedes ver la razón de los rebotes blandos y comprender posibles discrepancias entre los «envíos» y las «entregas» de tus campañas de correo electrónico.

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Correo no deseado {#spam}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Correo no deseado</i>:</b> Recuento</li>
        <li><b><i>% de correo no deseado</i> o <i>% de tasa de correo no deseado</i>:</b> (Marcados como correo no deseado) / (Envíos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Aperturas únicas {#unique-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Para correo electrónico, esto se rastrea durante un período de siete días. Esto significa que un mismo usuario que abre el mismo correo electrónico de nuevo después de siete días cuenta como una nueva apertura única. Como resultado, los recuentos de aperturas únicas en el dashboard pueden ser mayores que una simple consulta `DISTINCT user_id` en los datos de Currents. Para que coincidan los recuentos del dashboard con Currents, filtra por eventos donde `is_unique` sea `true`.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Aperturas únicas</i>:</b> Recuento</li>
        <li><b><i>% de aperturas únicas</i> o <i>Tasa de aperturas únicas</i>:</b> (Aperturas únicas) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Clics únicos {#unique-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Esto se rastrea durante un período de siete días para correo electrónico y se mide por <a href='/docs/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a> (un único intento de envío). Esto incluye clics en los enlaces de cancelación de suscripción proporcionados por Braze. Las URL de cancelación de suscripción personalizadas rastreadas también cuentan para *Clics únicos* cuando un usuario selecciona el enlace. Después de siete días, otro clic único se contabiliza para el mismo usuario si hace clic de nuevo. Las métricas de interacción de correo electrónico del dashboard, incluidos los _Clics únicos_, se calculan en Braze y no se concilian a partir de informes agregados del ESP. Para que coincidan los recuentos del dashboard con Currents, filtra por eventos donde `is_unique` sea `true`.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Clics únicos</i>:</b> Recuento</li>
        <li><b><i>% de clics únicos</i> o <i>Tasa de clics</i>:</b> (Clics únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

#### Enlaces inesperados en el mapa de calor del correo electrónico {#unexpected-links-on-the-email-heatmap}

Cuando el [mapa de calor del correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting/) muestra enlaces que no esperas, inspecciona el HTML del mensaje en busca de [bloques de contenido]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/dnd_editor_blocks/) o espacios entre palabras que crean URL rastreadas. Usa la **tabla de enlaces por clics totales** en la vista del mapa de calor para identificar URL que no coinciden con el texto visible.

{% endapi %}

{% api %}

### Clics totales {#total-clicks}

{% apitags %}
Count, Percentage
{% endapitags %}

<i>Clics totales</i> es el número total de veces que los usuarios hicieron clic en enlaces del correo electrónico entregado, incluidos múltiples clics del mismo usuario. Esto incluye clics en los enlaces de cancelación de suscripción de Braze y en las URL de cancelación de suscripción personalizadas rastreadas.

Cuando los *Clics totales* son mucho mayores que los *Clics únicos*, es posible que herramientas de seguridad o proveedores de buzón estén escaneando los enlaces sin que los usuarios abran el mensaje. Compara los *Clics únicos* cuando evalúes la interacción internamente.

{% endapi %}

{% api %}

### Cancelaciones de suscripción {#unsubscribers-or-unsub}

{% apitags %}
Count, Percentage
{% endapitags %}

Las _cancelaciones de suscripción_ reflejan el enlace estándar de cancelación de suscripción de Braze. Las páginas personalizadas para cancelar la suscripción no incrementarán esta métrica a menos que actualices a los usuarios mediante la API. Las **series temporales de grupos de suscripción** sí reflejan los cambios realizados a través de la API.

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Cancelaciones de suscripción</i>:</b> Recuento</li>
        <li><b><i>% de cancelaciones de suscripción</i> o <i>Tasa de cancelación de suscripción</i>:</b> (Cancelaciones de suscripción) / (Entregas)</li>
    </ul>
</span>
{:/}

#### Por qué las *cancelaciones de suscripción* y los clics en el enlace de cancelación de suscripción pueden diferir {#why-unsubscribes-and-unsubscribe-link-clicks-can-differ}

En la página de **Analytics** de una campaña de correo electrónico o Canvas, compara el recuento de *Cancelaciones de suscripción* con los clics en la URL de cancelación de suscripción de Braze en el desglose por enlace cuando expandes **Total Clicks** o **Unique Clicks**. Ambos suelen coincidir, pero pueden diferir:

- **Más *cancelaciones de suscripción* que clics en la URL de cancelación de suscripción del cuerpo:** [List-unsubscribe]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#list-unsubscribe) es una vía adicional de cancelación de suscripción en el encabezado del correo electrónico (no el enlace en el cuerpo de tu mensaje). Cuando un usuario cancela su suscripción de esta forma, se contabiliza en *Cancelaciones de suscripción*, pero no como un clic en la URL de cancelación de suscripción rastreada en el cuerpo.
- **Más clics en la URL de cancelación de suscripción del cuerpo que *cancelaciones de suscripción*:** Un usuario puede seleccionar ese enlace más de una vez. Si cancela su suscripción, se vuelve a suscribir y cancela de nuevo, los análisis de correo electrónico pueden registrar múltiples clics (por ejemplo, dos) en el desglose de clics.

Para más información, consulta [¿Por qué veo un número diferente de cancelaciones de suscripción que de clics en mi enlace de cancelación de suscripción?]({{site.baseurl}}/user_guide/channels/email/faq/#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

{% endapi %}

{% api %}

### Ingresos {#revenue}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Conversiones primarias (A) o evento de conversión primaria {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Para correo electrónico, push y webhooks, comenzamos a rastrear las conversiones después del envío inicial.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Conversiones primarias (A)</i> o <i>Evento de conversión primaria</i>:</b> Recuento</li>
        <li><b><i>% de conversiones primarias (A)</i> o <i>Tasa de evento de conversión primaria</i>:</b> (Conversiones primarias) / (Destinatarios únicos)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Confianza {#confidence}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Aperturas automáticas {#machine-opens}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Esta métrica se rastrea desde el 11 de noviembre de 2021 para SendGrid y desde el 2 de diciembre de 2021 para SparkPost.

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Otras aperturas {#other-opens}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Ten en cuenta que un usuario también puede abrir un correo electrónico (de modo que la apertura cuenta para <i>Otras aperturas</i>) antes de que se registre un recuento de <i>Aperturas automáticas</i>. Si un usuario abre un correo electrónico una vez (o más) después de un evento de apertura automática desde un buzón de entrada que no sea Apple Mail, entonces la cantidad de veces que el usuario abre el correo electrónico se calcula para <i>Otras aperturas</i> y solo una vez para <i>Aperturas únicas</i>.

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Aperturas reales estimadas {#estimated-real-opens}

{% apitags %}
Count, Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %} Braze recalcula esta estimación a medida que llegan nuevos datos de aperturas y clics. El valor suele estabilizarse unos días después del envío, pero continúa actualizándose cuando se producen nuevos eventos que califican.

{% endapi %}

{% api %}

### Tasa de clic a apertura {#click-to-open-rate}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Clics únicos) / (Aperturas únicas) (para correo electrónico)</span>

#### Puntuaciones de probabilidad de apertura de mensajes (segmentación) {#message-open-likelihood-scores-segmentation}

El filtro de Segment [`Message Open Likelihood`]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#message-open-likelihood) puntúa la probabilidad de que un usuario abra un correo electrónico en una escala de 0 a 100 %. Los usuarios sin suficiente historial de envíos o aperturas para el canal aparecen en blanco. Para correo electrónico, las aperturas automáticas se excluyen del cálculo, que utiliza el historial de mensajes recientes en ese canal (consulta [Filtro de probabilidad de apertura de mensajes para canales individuales]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/#individual-channels)).

{% endapi %}

## Solución de problemas y preguntas frecuentes sobre informes de correo electrónico {#email-reporting-troubleshooting-and-faqs}

### Enlaces de cancelación de suscripción y clics únicos {#unsubscribe-links-and-unique-clicks}

Cuando un destinatario hace clic en un enlace de cancelación de suscripción, Braze lo cuenta como un clic porque la acción utiliza una URL. Esto se aplica a los enlaces de cancelación de suscripción proporcionados por Braze y a los enlaces de cancelación de suscripción personalizados en el cuerpo de tu mensaje. Esos clics contribuyen a *Clics únicos* y *Clics totales* junto con otros clics en enlaces. Para las definiciones de métricas, consulta [Clics únicos](#unique-clicks) más arriba y [¿Por qué veo un número diferente de cancelaciones de suscripción que de clics en mi enlace de cancelación de suscripción?]({{site.baseurl}}/user_guide/channels/email/faq/#why-am-i-seeing-a-different-number-of-unsubscribes-than-clicks-on-my-unsubscribe-link).

### Ver en el navegador {#view-in-browser}

Braze no incluye una función integrada de «Ver este correo electrónico en un navegador». Aloja el contenido del correo electrónico en una página de inicio externa (como tu sitio web) y agrega un enlace desde el mensaje usando la herramienta **Enlace** del editor de correo electrónico. Para más información, consulta [¿Puedo agregar un enlace de «ver este correo electrónico en un navegador» a mis correos electrónicos?]({{site.baseurl}}/user_guide/channels/email/faq/#can-i-add-a-view-this-email-in-a-browser-link-to-my-emails).

### Actualizaciones de la página personalizada para cancelar la suscripción {#custom-unsubscribe-page-updates}

Los cambios en tu [página personalizada para cancelar la suscripción]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/) aparecen en pocos minutos. Los envíos en vivo usan una caché de corta duración de la página que se actualiza cuando guardas los cambios.

### Rebotes por cuota excedida y buzón lleno {#over-quota-and-full-mailbox-bounces}

Un rebote por cuota excedida o buzón lleno significa que el buzón del destinatario no puede aceptar correo nuevo. Puedes ver estas direcciones entre nuevos registros con direcciones no válidas o de riesgo, o entre perfiles inactivos durante mucho tiempo cuyos buzones se llenaron mientras estaban inactivos.

Revisa las tasas de rebote por segmento y fuente, elimina o retira las direcciones que rebotan repetidamente de forma dura, y usa la adhesión voluntaria confirmada o doble para nuevos suscriptores. Para prácticas de higiene de listas, consulta [Trampas de capacidad de entrega y correo no deseado]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/) e [Informes de correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting/#troubleshooting).

### 550 5.7.1 correo no solicitado {#550-571-unsolicited-mail}

Una respuesta `550 5.7.1` como «Nuestro sistema ha detectado que este mensaje probablemente es correo no solicitado» suele provenir de proveedores de buzón estrictos (por ejemplo, Gmail) cuando las señales de reputación o interacción son deficientes. Los factores comunes incluyen quejas de correo no deseado, baja interacción, listas compradas o alquiladas y picos repentinos de volumen.

Concéntrate en el crecimiento de listas basado en el consentimiento, retira a los suscriptores inactivos y monitorea las tasas de quejas y rebotes. Para más información, consulta [Trampas de capacidad de entrega y correo no deseado]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/).

### Buenas tasas de capacidad de entrega de correo electrónico {#good-email-deliverability-rates}

La **entrega** indica si el servidor receptor acepta tu mensaje; puedes medirla con métricas como *Entregas* y la tasa de rebote. La **capacidad de entrega** (ubicación en el buzón de entrada) depende del filtrado del proveedor y no se muestra como una única métrica de Braze.

Como guía general, apunta a una entrega cercana al 99 % con rebotes duros por debajo de aproximadamente el 1 %, y observa las aperturas y los clics para detectar tendencias de interacción. Los objetivos exactos varían según la industria y el patrón de envío. Para prácticas que respaldan la reputación, consulta [Mejorar la capacidad de entrega del correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices/improve_deliverability/) y [Trampas de capacidad de entrega y correo no deseado]({{site.baseurl}}/user_guide/channels/email/email_setup/deliverability_pitfalls_and_spam_traps/).

### «La Campaign ya está en la ventana de retraso, por lo que no se pone en cola otra» {#campaign-is-already-in-delay-window-so-not-enqueueing-another}

En el registro de actividad de mensajes o los registros de diagnóstico de [campañas basadas en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/), este resultado de procesamiento significa que Braze bloqueó un envío duplicado mientras un desencadenante anterior para el mismo usuario aún se encuentra dentro de la ventana de entrega de la Campaign. Un bloqueo de antirrebote evita múltiples puestas en cola para la misma ráfaga de desencadenantes.

Puedes ver este resultado incluso cuando la Campaign muestra **Enviar inmediatamente** si se cumple alguna de las siguientes condiciones:

- La Campaign usa un [evento de excepción]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/exit_criteria/#exception-events) o un retraso en el momento de envío que afecta la temporización.
- Los usuarios tienen un período de [reelegibilidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/), por lo que no pueden recibir el mensaje de nuevo hasta que pase esa ventana.
- Otro mensaje de Campaign o paso de mensaje de Canvas con mayor prioridad consumió el espacio de envío cuando los desencadenantes se superponen.

Si un usuario debería haber recibido el mensaje pero no lo hizo, verifica los resultados anteriores para el mismo desencadenante (por ejemplo, rebote de correo electrónico o canal no habilitado). Otro mensaje en el mismo flujo de trabajo puede haber impedido este envío.