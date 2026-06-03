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

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variación {#variation}

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

Cuando un correo electrónico tiene un rebote duro o se marca como correo no deseado, Braze marca la dirección de correo electrónico como no válida, pero no actualiza el [estado de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) del usuario. Braze detiene cualquier envío futuro a esa dirección de correo electrónico. Para eliminar una dirección de correo electrónico de tu lista de rebotes duros, usa el [punto de conexión para eliminar correos electrónicos con rebote duro]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/).

<span class="calculation-line">Cálculo: Recuento </span>

{% endapi %}

{% api %}

### Rebote blando {#soft-bounce}

{% apitags %}
Count
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un correo electrónico recibe un rebote blando, normalmente se reintentará en un plazo de 72 horas, pero el número de reintentos varía según el receptor.

Aunque los rebotes blandos no se rastrean en los análisis de tu campaña, puedes monitorear los rebotes blandos en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) o excluir a estos usuarios de tu envío con el [filtro de segmento de rebote blando]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/#soft-bounced). En el Registro de actividad de mensajes, también puedes ver la razón de los rebotes blandos y comprender posibles discrepancias entre los «envíos» y las «entregas» de tus campañas de correo electrónico.

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

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Esto se rastrea durante un período de siete días para correo electrónico y se mide por <a href='/docs/user_guide/messaging/messaging_fundamentals/dispatch_id/'>dispatch_id</a>. Esto incluye clics en los enlaces de cancelación de suscripción proporcionados por Braze. Después de siete días, otro clic único puede contarse para el mismo usuario si hace clic de nuevo. Para que coincidan los recuentos del dashboard con Currents, filtra por eventos donde `is_unique` sea `true`.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b><i>Clics únicos</i>:</b> Recuento</li>
        <li><b><i>% de clics únicos</i> o <i>Tasa de clics</i>:</b> (Clics únicos) / (Entregas)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Cancelaciones de suscripción {#unsubscribers-or-unsub}

{% apitags %}
Count, Percentage
{% endapitags %}

Las *cancelaciones de suscripción* reflejan el enlace estándar de cancelación de suscripción de Braze. Las páginas personalizadas para cancelar la suscripción no incrementarán esta métrica a menos que actualices a los usuarios mediante la API. Las **series temporales de grupos de suscripción** sí reflejan los cambios realizados a través de la API.

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

### Tasa de clic a apertura {#click-to-open-rate}

{% apitags %}
Percentage
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Clics únicos) / (Aperturas únicas) (para correo electrónico)</span>

{% endapi %}