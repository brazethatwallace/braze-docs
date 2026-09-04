---
nav_title: Glosario de métricas
article_title: Glosario de métricas
layout: report_metrics
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Este glosario define los términos que encontrarás en tus informes en tu cuenta de Braze."
tool: Reports
---

<style>
  .calculation-line {
    color: #5B6B75;
    font-size: 14px;
  }
</style>

{% api %}

## páginas móviles aceleradas Clicks {#amp-clicks}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='páginas móviles aceleradas Clicks' %}

{% endapi %}

{% api %}

## páginas móviles aceleradas Opens {#amp-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='páginas móviles aceleradas Opens' %}

{% endapi %}

{% api %}

## Audiencia {#audience}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Cálculo: (Número de destinatarios en la variante) / (Destinatarios únicos)</span>

{% endapi %}

{% api %}

## Rebotes {#bounces}

{% apitags %}
Email, Web Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Esto podría ocurrir porque no hay un token de notificaciones push válido, el usuario canceló su suscripción después de que se lanzó la campaña, o la dirección de correo electrónico es incorrecta o está desactivada.

| Canal | Información adicional |
|-------|-----------------------|
| Correo electrónico | Un rebote de correo electrónico para clientes que usan SendGrid consiste en rebotes duros, correo no deseado (`spam_report_drops`) y correos electrónicos enviados a direcciones no válidas (`invalid_emails`).<br><br>Para correo electrónico, *% de rebote* o *tasa de rebote* es el porcentaje de mensajes que no se enviaron correctamente o que fueron designados como "devueltos" o "no recibidos" por los servicios de envío utilizados, o que no fueron recibidos por los usuarios con correo electrónico válido.|
| Push | Estos usuarios han sido dados de baja automáticamente de todas las notificaciones push futuras.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rebotes" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Bounces</i>: Recuento</li>
        <li><i>Bounce %</i> o <i>Bounce Rate %</i>: (Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Body Click {#body-click}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">Cálculo: (Body Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

## Body Clicks {#body-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %}

<span class="calculation-line">Cálculo: (Body Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

## Button 1 Clicks {#button-1-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} Los informes de _Button 1 Clicks_ solo funcionan cuando especificas el **Identifier for Reporting** como "0" en el mensaje dentro de la aplicación.

<span class="calculation-line">Cálculo: (Button 1 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

## Button 2 Clicks {#button-2-clicks}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} Los informes de _Button 2 Clicks_ solo funcionan cuando especificas el **Identifier for Reporting** como "1" en el mensaje dentro de la aplicación.

<span class="calculation-line">Cálculo: (Button 2 Clicks) / (Impressions)</span>

{% endapi %}

{% api %}

## Análisis de Campaign {#campaign-analytics}

{% apitags %}
Feature Flags
{% endapitags %}

El rendimiento del mensaje a través de varios canales. Las métricas mostradas dependen del canal de mensajería seleccionado y de si el [experimento de conmutador de características]({{site.baseurl}}/developer_guide/feature_flags/experiments#campaign-analytics) es una prueba multivariante.

{% endapi %}

{% api %}

## Choices Submitted {#choices-submitted}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

## Click-to-Open Rate {#click-to-open-rate}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Cálculo: (Unique Clicks) / (Unique Opens) (para correo electrónico)</span>

{% endapi %}

{% api %}

## RCS Confirmed Deliveries o SMS Confirmed Deliveries {#rcs-confirmed-deliveries-or-sms-confirmed-deliveries}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Como cliente de Braze, las entregas se cargan a tu asignación de SMS.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Confirmed Deliveries</i>: Recuento</li>
        <li><i>Confirmed Delivery Rate</i>: (Confirmed Deliveries) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Confidence {#confidence}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

## Confirmation Page Button {#confirmation-page-button}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

## Confirmation Page Dismissals {#confirmation-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

## Conversiones (B, C, D) {#conversions-b-c-d}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Este evento definido lo determinas tú al crear la campaña.

| Canal | Información adicional |
|-------|-----------------------|
| Correo electrónico, push, webhooks | Las conversiones se rastrean después del envío inicial.|
| Content Cards | Las conversiones se cuentan cuando el usuario ve una Content Card por primera vez.|
| Mensajes dentro de la aplicación | Una conversión se cuenta si el usuario ha recibido y visto la campaña de mensaje dentro de la aplicación, y posteriormente realiza el evento de conversión específico dentro de la ventana de conversión definida, independientemente de si hizo clic en el mensaje o no.<br><br>Las conversiones se atribuyen al mensaje recibido más recientemente. Si la reelegibilidad está habilitada, la conversión se asignará al último mensaje dentro de la aplicación recibido, siempre que ocurra dentro de la ventana de conversión definida. Sin embargo, si el mensaje dentro de la aplicación ya tiene una conversión asignada, la nueva conversión no se puede registrar para ese mensaje específico. Esto significa que cada entrega de mensaje dentro de la aplicación está asociada con una sola conversión.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conversiones (B, C, D)" }

{% endapi %}

{% api %}

## Total Conversions {#total-conversions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Cuando un usuario ve una campaña de mensaje dentro de la aplicación solo una vez, solo se cuenta una conversión, incluso si realiza el evento de conversión varias veces después. Sin embargo, si la reelegibilidad está activada y el usuario ve la campaña de mensaje dentro de la aplicación varias veces, las *Total Conversions* pueden aumentar una vez por cada vez que el usuario registra una impresión para una nueva instancia de la campaña de mensaje dentro de la aplicación.

Por ejemplo, si un usuario activa un mensaje dentro de la aplicación dos veces y convierte después de cada impresión del mensaje dentro de la aplicación (lo que resulta en dos conversiones), entonces las *Total Conversions* aumentarán en dos. Sin embargo, si solo hubo una impresión de mensaje dentro de la aplicación seguida de dos eventos de conversión, solo se registrará una conversión y las *Total Conversions* aumentarán en uno.

{% endapi %}

{% api %}

## Close Message {#close-message}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

## Tasa de conversión {#conversion-rate}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

| Canal | Información adicional |
|-------|-----------------------|
| Mensajes dentro de la aplicación | La métrica de <i>Unique Impressions</i> diarias totales se utiliza para calcular la <i>Conversion Rate</i> para mensajes dentro de la aplicación.<br><br>Las <i>Unique Impressions</i> para mensajes dentro de la aplicación solo se pueden contar una vez por día calendario en la zona horaria de tu espacio de trabajo. El número de veces que un usuario completa una acción deseada (una "conversión") puede aumentar dentro de ese mismo día calendario. Aunque las conversiones pueden ocurrir más de una vez al día, las <i>Unique Impressions</i> no. Por lo tanto, si un usuario completa una conversión varias veces en un día, la <i>Conversion Rate</i> puede aumentar en consecuencia, pero las <i>Unique Impressions</i> solo se cuentan una vez para ese día calendario. Para más detalles, consulta <a href="/docs/user_guide/channels/in_app_messages/reporting">Informes de mensajes dentro de la aplicación</a>.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tasa de conversión" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Mensajes dentro de la aplicación</b>: (Primary Conversions) / (Unique Impressions)</li>
        <li><b>Otros canales</b>: (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Ventana de conversión {#conversion-window}

{% apitags %}
All
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

## Entregas {#deliveries}

{% apitags %}
Email, Web Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

| Canal | Información adicional |
|-------|-----------------------|
| Correo electrónico | Se refiere al número total de mensajes (envíos) enviados correctamente y recibidos por las partes con correo electrónico válido.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entregas" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Deliveries</i>: Recuento</li>
        <li><i>Deliveries %</i>: (Sends - Bounces) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## RCS Delivery Failures o SMS Delivery Failures {#rcs-delivery-failures-or-sms-delivery-failures}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Ponte en contacto con <a href="/docs/braze_support">soporte de Braze</a> para obtener ayuda para comprender las razones de los fallos de entrega.

<span class="calculation-line">Cálculo: (Sends) - (Sends to Carrier)</span>

{% endapi %}

{% api %}

## Delivery Failures {#delivery-failures}

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Ponte en contacto con <a href="/docs/braze_support">soporte de Braze</a> para obtener ayuda para comprender las razones de los fallos de entrega.

<span class="calculation-line">Cálculo: (Sends) - (Sends to Carrier)</span>

{% endapi %}

{% api %}

## Tasa de entrega fallida {#failed-delivery-rate}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Ponte en contacto con <a href="/docs/braze_support">soporte de Braze</a> para obtener ayuda para comprender las razones de los fallos de entrega.

<span class="calculation-line">Cálculo: (Delivery Failures) / (Sends)</span>

{% endapi %}

{% api %}

## Direct Opens {#direct-opens}

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Cálculo: (Direct Opens) / (Deliveries)</span>

{% endapi %}

{% api %}

## Emailable {#emailable}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

## Errores {#errors}

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Los errores se incluyen en el recuento de <i>Sends</i>, pero no se incluyen en el recuento de <i>Unique Recipients</i>.

{% endapi %}

{% api %}

## Estimated Real Opens {#estimated-real-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

## Fallos {#failures}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} Los fallos se incluyen en el recuento de <i>Sends</i>, pero no en el recuento de <i>Deliveries</i>.</td>

<span class="calculation-line">Cálculo (<i>Failure Rate</i>): (Failures) / (Sends)</span>

{% endapi %}

{% api %}

## Rendimiento del experimento de conmutador de características {#feature-flag-experiment-performance}

{% apitags %}
Feature Flags
{% endapitags %}

Métricas de rendimiento para el mensaje en un experimento de conmutador de características. Las métricas específicas mostradas variarán según el canal de mensajería y si el experimento fue o no una prueba multivariante.

{% endapi %}

{% api %}

## Rebote duro {#hard-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %}

Cuando esto ocurre, Braze marca la dirección de correo electrónico como no válida, pero no actualiza el [estado de suscripción]({{site.baseurl}}/user_guide/channels/email/subscriptions) del usuario. Si un correo electrónico recibe un rebote duro, Braze deja de realizar cualquier solicitud futura a esta dirección de correo electrónico.

{% endapi %}

{% api %}

## Help {#help}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} La respuesta de un usuario se mide cada vez que un usuario envía un mensaje de entrada dentro de las cuatro horas posteriores a la recepción de tu mensaje.

{% endapi %}

{% api %}

## Influenced Opens {#influenced-opens}

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Cálculo: (Influenced Opens) / (Deliveries)</span>

{% endapi %}

{% api %}

## Ingresos del ciclo de vida {#lifetime-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

## Valor del ciclo de vida por usuario {#lifetime-value-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='LTV Per User' %}

{% endapi %}

{% api %}

## Ingresos diarios promedio {#average-daily-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

## Compras diarias {#daily-purchases}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

## Ingresos diarios por usuario {#daily-revenue-per-user}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

## Machine Opens {#machine-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Esta métrica se rastrea desde el 11 de noviembre de 2021 para SendGrid y desde el 2 de diciembre de 2021 para SparkPost. Para Amazon SES, los análisis se mostrarán como _Opens_. Sin embargo, se admitirá el filtrado de bots para clics.

{% endapi %}

{% api %}

## Aperturas {#opens}

{% apitags %}
Web Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

## Opt-Out {#opt-out}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} La respuesta de un usuario se mide cada vez que un usuario envía un mensaje de entrada dentro de las cuatro horas posteriores a la recepción de tu mensaje.

{% endapi %}

{% api %}

## Other Opens {#other-opens}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Ten en cuenta que un usuario también puede abrir un correo electrónico (de modo que la apertura cuenta para Other Opens) antes de que se registre un recuento de Machine Opens. Si un usuario abre un correo electrónico una vez (o más) después de un evento de apertura de máquina desde una bandeja de entrada que no sea Apple Mail, entonces la cantidad de veces que el usuario abre el correo electrónico se calcula para Other Opens y solo una vez para Unique Opens.

{% endapi %}

{% api %}

## Pending Retry {#pending-retry}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

## Primary Conversions (A) o conversión primaria Event {#primary-conversions-a-or-primary-conversion-event}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or conversión primaria Event' %}

| Canal | Información adicional |
|-------|-----------------------|
| Correo electrónico, push, webhooks | Después del envío inicial.|
| Content Cards, mensajes dentro de la aplicación | Cuando el usuario ve la Content Card o el mensaje por primera vez.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Primary Conversions (A) o conversión primaria Event" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Primary Conversions (A) o conversión primaria Event</i>: Recuento</li>
        <li><i>Primary Conversions (A) %</i> o <i>conversión primaria Event Rate</i>: (Primary Conversions) / (Unique Recipients)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Lecturas {#reads}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

## Tasa de lectura {#read-rate}

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">Cálculo: (Reads con confirmación de lectura) / (Sends)</span>

{% endapi %}

{% api %}

## Recibido {#received}

{% apitags %}
Email, Content Cards, In-App Message, Web Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %}

| Canal | Información adicional |
|-------|-------|
| Content Cards | Recibido cuando los usuarios ven la tarjeta en la aplicación.|
| Push | Recibido cuando los mensajes se envían desde el servidor de Braze al proveedor de push.|
| Correo electrónico | Recibido cuando los mensajes se envían desde el servidor de Braze al proveedor de servicios de correo electrónico.|
| SMS/MMS | "Entregado" después de que el proveedor de SMS recibe la confirmación del operador ascendente y el dispositivo de destino.|
| Mensaje dentro de la aplicación | Recibido en el momento de la visualización según la acción desencadenante definida.|
| WhatsApp | Recibido en el momento de la visualización según la acción desencadenante definida.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Recibido" }

{% endapi %}

{% api %}

## RCS Rejections o SMS Rejections {#rcs-rejections-or-sms-rejections}

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Como cliente de Braze, los rechazos se cargan a tu asignación de SMS.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Rejections</i>: Recuento</li>
        <li><i>Rejection Rate</i>: (Rejections) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Ingresos {#revenue}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

## Sent {#sent}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

## Envíos {#sends}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Esta métrica es proporcionada por Braze. Ten en cuenta que al lanzar una campaña planificada, esta métrica incluirá todos los mensajes enviados, independientemente de si ya se han enviado debido al límite de velocidad.

{% alert tip %}
Para Content Cards, esta métrica se calcula de forma diferente según lo que hayas seleccionado para [Creación de tarjeta]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation):

- **Al lanzamiento o entrada al paso:** El número de tarjetas creadas y disponibles para ser vistas. Esto no cuenta si los usuarios vieron la tarjeta.
- **En la primera impresión:** El número de tarjetas mostradas a los usuarios.
{% endalert %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

## Mensajes enviados {#messages-sent}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Esta métrica es proporcionada por Braze. Ten en cuenta que al lanzar una campaña planificada, esta métrica incluirá todos los mensajes enviados, independientemente de si ya se han enviado debido al límite de velocidad.

{% alert tip %}
Para Content Cards, esta métrica se calcula de forma diferente según lo que hayas seleccionado para [Creación de tarjeta]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation):

- **Al lanzamiento o entrada al paso:** El número de tarjetas creadas y disponibles para ser vistas. Esto no cuenta si los usuarios vieron la tarjeta.
- **En la primera impresión:** El número de tarjetas mostradas a los usuarios.
{% endalert %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

## Sends to Carrier {#sends-to-carrier}

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Sends to Carrier</i>: Recuento</li>
        <li><i>Sends to Carrier Rate</i>: (Sends to Carrier) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Rebote blando {#soft-bounce}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Si un correo electrónico recibe un rebote blando, normalmente reintentaremos dentro de las 72 horas, pero el número de intentos de reintento varía de un receptor a otro.

Ten en cuenta que los *rebotes blandos* difieren de los *aplazamientos*. Si no se entrega correctamente ningún correo electrónico durante este período de reintento, Braze envía un evento de rebote blando por cada intento de envío de campaña. Antes del 25 de febrero de 2025, estos reintentos se contaban como múltiples rebotes blandos para un envío de campaña.

Aunque los rebotes blandos no se rastrean en los análisis de tu campaña, puedes monitorear los rebotes blandos en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log). También puedes excluir a estos usuarios de tu envío o consultar la cantidad de rebotes blandos de los últimos 30 días con el [filtro de segmento de rebote blando]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#soft-bounced). En el Registro de actividad de mensajes, también puedes ver la razón de los rebotes blandos y comprender posibles discrepancias entre los "envíos" y las "entregas" de tus campañas de correo electrónico.

{% endapi %}

{% api %}

## Correo no deseado {#spam}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
Las quejas de correo no deseado son gestionadas directamente por los proveedores de servicios de correo electrónico y luego transmitidas a Braze a través de un bucle de retroalimentación. La mayoría de los bucles de retroalimentación solo informan una parte de las quejas reales, por lo que la métrica de *Spam* a menudo representa una fracción del total real. Solo los proveedores de servicios de correo electrónico pueden ver el volumen real de quejas de correo no deseado, lo que significa que *Spam* debe verse como una métrica indicativa, no exhaustiva.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Spam</i>: Recuento</li>
        <li><i>Spam %</i> o <i>Spam Rate %</i>: (Marked as Spam) / (Sends)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Survey Page Dismissals {#survey-page-dismissals}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

## Survey Submissions {#survey-submissions}

{% apitags %}
In-App Message
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

## Clics totales {#total-clicks}

{% apitags %}
Email, Content Cards, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

| Canal | Información adicional |
|-------|-------|
| LINE | Se rastrea después de alcanzar un umbral mínimo de 20 mensajes por día. Los correos electrónicos páginas móviles aceleradas incluyen clics registrados tanto en las versiones HTML como de texto plano. Este número puede estar inflado artificialmente por herramientas antispam.|
| Banners | El número total (y porcentaje) de usuarios que hicieron clic dentro del mensaje entregado, independientemente de si el mismo usuario hace clic varias veces.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clics totales" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Correo electrónico:</b> (Total Clicks) / (Deliveries)</li>
        <li><b>Content Cards:</b> (Total Clicks) / (Total Impressions)</li>
        <li><b>SMS:</b> (Click Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Descartes totales {#total-dismissals}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Para Content Cards, si un usuario recibe dos tarjetas diferentes de la misma campaña y descarta ambas, este recuento aumenta en dos. La reelegibilidad te permite incrementar los _Total Dismissals_ una vez cada vez que un usuario recibe una tarjeta; cada tarjeta es un mensaje diferente. Para Banners, esto cuenta cada descarte cuando el comportamiento de descarte está habilitado.

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Total Dismissals:</i> Recuento</li>
        <li><i>Total Dismissal Rate:</i> Total Dismissals / Total Impressions</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Impresiones totales {#total-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Este número es una suma del número de eventos de impresión que Braze recibe de los SDK.

| Canal | Información adicional |
|-------|-----------------------|
| Content Cards | El recuento total de impresiones registradas para una Content Card determinada. Esto puede incrementarse varias veces para el mismo usuario.|
| Mensajes dentro de la aplicación | Si hay varios dispositivos y la reelegibilidad está desactivada, el usuario solo debería ver el mensaje dentro de la aplicación una vez. Incluso si el usuario usa varios dispositivos, solo lo verá en el primer dispositivo objetivo. Esto supone que el perfil tiene dispositivos consolidados y un usuario tiene un ID de usuario con el que ha iniciado sesión en todos los dispositivos. Si la reelegibilidad está activada, se registra una impresión cada vez que el usuario ve el mensaje dentro de la aplicación. Para más detalles, consulta <a href="/docs/user_guide/channels/in_app_messages/reporting">Informes de mensajes dentro de la aplicación</a>.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Impresiones totales" }

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

## Aperturas totales {#total-opens}

{% apitags %}
Email, iOS Push, Android Push, Web Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

| Canal | Información adicional |
|-------|-----------------------|
| LINE | Se rastrea después de alcanzar un umbral mínimo de 20 mensajes por día.|
| Correos electrónicos páginas móviles aceleradas | Las aperturas totales para las versiones HTML y de texto plano.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aperturas totales" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><b>Correo electrónico <i>Total Opens</i>:</b> Recuento</li>
        <li><b>Correo electrónico <i>Total Open Rate</i>:</b> (Opens) / (Deliveries)</li>
        <li><b>Notificación push web <i>Total Opens</i>:</b> Recuento de <i>Direct Opens</i></li>
        <li><b>Notificación push web <i>Total Open Rate</i>:</b> (Total Opens) / (Deliveries)</li>
        <li><b>Push de iOS, Android y Kindle <i>Total Opens</i>:</b> (Direct Opens) + (Influenced Opens)</li>
        <li><b>Push de iOS, Android y Kindle <i>Total Open Rate</i>:</b> (Total Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Ingresos totales {#total-revenue}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Esta métrica solo está disponible en los informes de comparación de Campaigns a través del <a href='/docs/user_guide/analytics/reports/report_builder'>generador de informes</a>.

{% endapi %}

{% api %}

## Clics únicos {#unique-clicks}

{% apitags %}
Email, Content Cards, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Esto incluye clics en los enlaces de cancelación de suscripción proporcionados por Braze.

| Canal | Información adicional |
|-------|-----------------------|
| Correo electrónico | Se rastrea durante un período de siete días.|
| LINE | Se rastrea después de alcanzar un umbral mínimo de 20 mensajes por día.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clics únicos" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Unique Clicks</i>: Recuento</li>
        <li><b>Content Cards</b> <i>Unique Clicks %</i> o <i>Unique Clicks Rate</i>: (Unique Clicks) / (Unique Impressions)</li>
        <li><b>Correo electrónico</b> <i>Unique Clicks %</i> o <i>Unique Clicks Rate</i>: (Unique Clicks) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Descartes únicos {#unique-dismissals}

{% apitags %}
Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Cálculo: (Unique Dismissals) / (Unique Impressions)</span>

{% endapi %}

{% api %}

## Impresiones diarias únicas {#unique-daily-impressions}

{% apitags %}
Content Cards, Banners
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Daily Impressions' %}

Este número es recibido de Braze y se basa en el `user_id`. Las impresiones diarias únicas se cuentan a nivel de campaña o paso en Canvas.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

## Impresiones únicas {#unique-impressions}

{% apitags %}
In-App Message, Content Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %}

| Canal | Información adicional |
|-------|-----------------------|
| Mensajes dentro de la aplicación | Las impresiones únicas pueden incrementarse de nuevo en un nuevo día calendario en la zona horaria de tu espacio de trabajo si la reelegibilidad está activada y un usuario realiza la acción desencadenante. Si la reelegibilidad está activada, <i>Unique Impressions</i> = <i>Unique Recipients</i>. Para más detalles, consulta <a href="/docs/user_guide/channels/in_app_messages/reporting">Informes de mensajes dentro de la aplicación</a>.|
| Content Cards | El recuento no debería incrementarse la segunda vez que un usuario ve una tarjeta.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Impresiones únicas" }

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

## Aperturas únicas {#unique-opens}

{% apitags %}
Email, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Al evaluar un período de tiempo específico, las <i>Unique Opens</i> pueden parecer más altas que los <i>Sends</i> para ese mismo período. Esto puede ocurrir porque los usuarios aún pueden registrar eventos de apertura para mensajes que se enviaron fuera de ese período de tiempo. Durante toda la duración de la campaña, las <i>Unique Opens</i> siempre son menores que el total de <i>Sends</i>.

| Canal | Información adicional |
|-------|-----------------------|
| Correo electrónico | Se rastrea durante un período de 7 días.|
| LINE | Se rastrea después de alcanzar un umbral mínimo de 20 mensajes por día.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aperturas únicas" }

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Unique Opens</i>: Recuento</li>
        <li><i>Unique Opens %</i> o <i>Unique Open Rate</i>: (Unique Opens) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Destinatarios únicos {#unique-recipients}

{% apitags %}
Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Dado que un espectador puede ser un destinatario único cada día, deberías esperar que este valor sea mayor que las <i>Unique Impressions</i>. Este número es recibido de Braze y se basa en el `user_id`. Los destinatarios únicos se cuentan a nivel de campaña o paso en Canvas, no a nivel de <a href='{{ site.homeurl }}{{ site.baseurl }}/api/identifier_types/#send-identifier'>identificador de envío</a>.

Los usuarios que rebotan aún cuentan como <i>Unique Recipients</i> cuando Braze los cuenta como destinatarios para ese día de envío. Los <i>Unique Recipients</i> se basan en los usuarios a los que Braze dirigió el mensaje ese día, no solo en las entregas exitosas.

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}

{% api %}

## Unsubscribers o Unsub {#unsubscribers-or-unsub}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Cálculo:
    <ul>
        <li><i>Unsubscribers</i> o <i>Unsub</i>: Recuento</li>
        <li><i>Unsubscribers %</i> o <i>Unsub Rate</i>: (Unsubscribes) / (Deliveries)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

## Unsubscribes {#unsubscribes}

{% apitags %}
Email
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Cálculo: (Unsubscribes) / (Deliveries)</span>

{% endapi %}

{% api %}

## Variante {#variation}

{% apitags %}
Content Cards, Email, In-App Message, Web Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Cálculo: Recuento</span>

{% endapi %}