---
nav_title: Rendimiento del canal
article_title: Dashboards de rendimiento del canal
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre el dashboard de rendimiento del canal, que te permite ver métricas de rendimiento para canales completos tanto en Campaigns como en Canvas."
tool:
  - Reports
toc_headers: h2
---

# Dashboards de rendimiento del canal {#channel-performance-dashboards}

> Los dashboards de rendimiento del canal muestran métricas de rendimiento agregadas para un canal completo, tanto de Campaigns como de Canvas. Estos dashboards están disponibles actualmente para correo electrónico, push y SMS.

## Paneles {#dashboards}

Selecciona una pestaña para ver los detalles de los paneles de rendimiento de canal disponibles.

{% tabs %}
{% tab Rendimiento de correo electrónico %}

### Panel de rendimiento de correo electrónico {#email-performance-dashboard}

Consulta tu panel de rendimiento de correo electrónico yendo a **Analytics** > **Email Performance** y seleccionando el intervalo de fechas del periodo cuyos datos quieres ver. Tu intervalo de fechas puede abarcar hasta un año en el pasado.

{% alert note %}
Para ver el panel **Email Performance**, necesitas el permiso "View Usage Data" o "View Dashboard Reports".
{% endalert %}

![Panel de rendimiento de correo electrónico que muestra la participación del canal de correo electrónico en los últimos treinta días.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Un ejemplo de Campaign de correo electrónico con 335.630 envíos, con un promedio de 11.187,667 por día.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Cómo se calculan las métricas {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envíos | Recuento | Número total de envíos en cada día del intervalo de fechas |
| Tasa de entrega | Tasa | (Número total de entregas en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de rebote | Tasa | (Número total de rebotes en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de cancelaciones | Tasa | (Número total de cancelaciones de suscripción únicas en cada día del intervalo de fechas) / (Número total de entregas en el intervalo de fechas)<br><br>Esto utiliza cancelaciones de suscripción únicas, que también se usan en los análisis de Campaign, en el resumen y en el generador de informes. Estas cancelaciones de suscripción se registran en todas las fuentes (como la REST API, las importaciones CSV, los correos electrónicos y las cancelaciones de suscripción de listas). Las tasas de cancelación de suscripción en los análisis de Campaign y Canvas son cancelaciones que ocurren como resultado de un clic de cancelación de suscripción en un correo electrónico entregado por Braze.  |
| Tasa de Unique Opens | Tasa | (Número total de aperturas únicas en cada día del intervalo de fechas) / (Número total de entregas en el intervalo de fechas) |
| Tasa de otras aperturas | Tasa | (Número total de otras aperturas en cada día del intervalo de fechas) / (Número total de entregas en el intervalo de fechas)<br><br>Otras aperturas incluye correos electrónicos que no se han identificado como aperturas de máquina, como cuando un usuario abre un correo electrónico. Esta métrica no es única y es una submétrica del total de aperturas.  |
| Tasa de clics únicos | Tasa | (Número total de clics únicos en cada día del intervalo de fechas) / (Número total de entregas en el intervalo de fechas) |
| Tasa de clics únicos sobre aperturas | Tasa | (Número total de clics únicos en cada día del intervalo de fechas) / (Número total de aperturas únicas en cada día del intervalo de fechas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cómo se calculan las métricas" }

{% endtab %}
{% tab Información de correo electrónico %}

### Panel de información de correo electrónico {#email-insights-dashboard}

El panel de información de correo electrónico rastrea dónde y cuándo tus clientes interactúan con tus correos electrónicos. Estos informes pueden proporcionar datos detallados y granulares sobre cómo optimizar tus correos electrónicos para impulsar una mayor participación. El panel de información de correo electrónico incluye hasta los últimos seis meses de datos. Para acceder al panel, ve a **Analytics** > **Email Performance** > **Email Insights**.

#### Participación por dispositivo {#engagement-by-device}

El informe **Engagement by Device** proporciona un desglose de los dispositivos que tus usuarios utilizan para interactuar con tu correo electrónico. Estos datos rastrean la participación del correo electrónico en dispositivos móviles, de escritorio, tabletas y otros tipos de dispositivos. Estos datos se basan en la cadena de agente de usuario transmitida desde los dispositivos de tus usuarios.

{% alert note %}
Si usas CloudFront como tu CDN, asegúrate de que el agente de usuario de tus usuarios se transmita al ESP. De lo contrario, cada agente de usuario será "Amazon Cloudfront".
{% endalert %}

La categoría "Other" incluye cualquier cadena de usuario que no pueda identificarse como escritorio, móvil o tableta. Por ejemplo, televisión, automóvil, consola de videojuegos, OTT (over-the-top o streaming) y similares. Esto también puede incluir valores nulos o vacíos.

Para comprender mejor qué contiene esta categoría "Other", puedes extraer los agentes de usuario utilizando cualquiera de estas opciones:

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) te enviará la cadena exacta de agente de usuario que se recuperó de los dispositivos de tus usuarios.
2. Aprovecha nuestro [generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para usar SQL o nuestro [generador de consultas con IA]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder) para ver los agentes de usuario.

![Informe de participación por dispositivo que muestra el número de clics para dispositivos móviles, de escritorio, tabletas y otros dispositivos. La mayor cantidad de clics ocurre en dispositivos móviles.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Para las aperturas de correo electrónico, Braze separará Google Image Proxy, Apple Image Proxy y Yahoo Mail Proxy. Estos servicios almacenan en caché y cargan todas las imágenes incrustadas en un correo electrónico antes de que se entregue al destinatario. Como resultado, esto activará una apertura de correo electrónico desde los servidores del proveedor de buzón en lugar del servidor del destinatario, lo que puede generar aperturas de correo electrónico infladas. Estos servicios están diseñados para mejorar la privacidad, la seguridad, el rendimiento y la eficiencia al cargar imágenes. Esto también puede contener aperturas reales de los destinatarios, ya que estos servicios de proxy enmascaran el agente de usuario, y Braze categoriza los datos de proxy utilizando el agente de usuario.

![Informe de participación por dispositivo que muestra el número de clics para móvil, escritorio, tableta, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy y otros. La mayor cantidad de aperturas ocurre en dispositivos móviles.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Participación por proveedor de buzón {#engagement-by-mailbox-provider}

El informe **Engagement by Mailbox Provider** muestra los principales proveedores de buzón que contribuyen a tus clics o aperturas. Puedes hacer clic en proveedores de buzón principales específicos para profundizar en dominios de recepción específicos. Por ejemplo, si Microsoft aparece en este informe como una de tus principales métricas de proveedor de buzón, puedes ver más detalles de sus dominios de recepción, como "outlook.com", "hotmail.com", "live.com" y más.

![Un ejemplo de informe de participación por proveedor de buzón con Google, Apple iCloud, Yahoo, Microsoft y Mail.Ru Group y su número correspondiente de clics.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Momento de la participación {#time-of-engagement}

El informe **Time of Engagement** muestra datos sobre cuándo los usuarios interactúan con tus correos electrónicos. Esto puede ayudar a responder preguntas como qué día de la semana o a qué hora se produce la mayor participación de tus clientes. Con esta información, puedes experimentar con el mejor día u hora para enviar tus mensajes e impulsar una mayor participación. Ten en cuenta que estos horarios se basan en la zona horaria de tu empresa.

El informe de participación **Day of the week** desglosa las aperturas o los clics por día de la semana.

![Un ejemplo de informe de participación por día de la semana con la mayor cantidad de clics los lunes y miércoles.]({% image_buster /assets/img_archive/time_engagement.png %})

El informe de participación **Time of the day** desglosa las aperturas o los clics por cada hora en una ventana de tiempo de 24 horas.

![Un ejemplo de informe de participación por hora del día con las aperturas o clics de 12 a. m. a 11 p. m.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Para obtener más información sobre los análisis de tus correos electrónicos, consulta [Informes de correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting).

{% endtab %}
{% tab Rendimiento de SMS %}

### Panel de rendimiento de SMS {#sms-performance-dashboard}

Para usar tu panel de rendimiento de SMS, ve a **Analytics** > **SMS Performance** y selecciona el intervalo de fechas del periodo cuyos datos quieres ver. Tu intervalo de fechas puede abarcar hasta un año en el pasado.

![Un ejemplo de Campaign de SMS con 335.630 envíos, con un promedio de 11.187,667 por día.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Cómo se calculan las métricas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envíos | Recuento | Número total de envíos en cada día del intervalo de fechas |
| Tasa de entregas confirmadas | Tasa | (Número total de entregas en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de fallos de entrega | Tasa | (Número total de fallos en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de rechazos | Tasa | (Número total de rechazos en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de clics | Tasa | (Número total de clics en cada día del intervalo de fechas) / (Número total de entregas en cada día del intervalo de fechas) |
| Total de adhesiones voluntarias | Tasa | Número total de adhesiones voluntarias de mensajes entrantes en cada día del intervalo de fechas |
| Total de cancelaciones | Tasa | Número total de cancelaciones de mensajes entrantes en cada día del intervalo de fechas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cómo se calculan las métricas" }

{% endtab %}
{% tab Rendimiento de push %}

### Panel de rendimiento de push {#push-performance-dashboard}

El panel **Push Performance** te ofrece una vista única a nivel de canal de la participación push, que incluye envíos, rebotes, entregas y tasas de Direct Opens, Influenced Opens y aperturas totales en una ventana de tiempo configurable. Úsalo para comprender el estado general de tu canal push sin tener que agregar datos de Campaigns o Canvas individuales.

Para abrir el panel, ve a **Analytics** > **Dashboard Builder** y selecciona **Push Channel Dashboard**. Tu intervalo de fechas puede abarcar hasta un año en el pasado.

![Un ejemplo de Campaign push con más de 63 millones de envíos.]({% image_buster /assets/img_archive/push_performance_dashboard.png %})

#### Cómo se calculan las métricas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envíos | Recuento | Número total de envíos en cada día del intervalo de fechas |
| Tasa de rebote | Tasa | (Número total de rebotes en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de entrega | Tasa | (Número total de entregas en cada día del intervalo de fechas) / (Número total de envíos en cada día del intervalo de fechas) |
| Tasa de Direct Opens | Tasa | (Número total de Direct Opens en cada día del intervalo de fechas) / (Número total de entregas en cada día del intervalo de fechas) |
| Tasa de Influenced Opens | Tasa | (Número total de Influenced Opens en cada día del intervalo de fechas) / (Número total de entregas en cada día del intervalo de fechas) |
| Tasa de aperturas totales | Tasa | (Número total de aperturas totales en cada día del intervalo de fechas) / (Número total de entregas en cada día del intervalo de fechas)<br><br>Las aperturas totales incluyen tanto Direct Opens como Influenced Opens. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cómo se calculan las métricas" }

{% endtab %}
{% endtabs %}

## Filtros del panel {#dashboard-filters}

Puedes filtrar los datos de tu panel utilizando las siguientes opciones de filtro:

- **Etiqueta:** Elige una etiqueta. Cuando se aplica, tu panel mostrará métricas solo para la etiqueta seleccionada.
- **Plataformas:** (Solo panel de rendimiento push) Elige una plataforma push, como **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** o **Web**. Cuando se aplica, tu panel mostrará métricas solo para la plataforma seleccionada.
- **Canvas:** Elige hasta 10 Canvas. Cuando se aplica, tu panel mostrará métricas solo para los Canvas seleccionados. Si seleccionas primero un filtro de etiqueta, las opciones de filtros de Canvas solo incluirán los Canvas que tengan la etiqueta seleccionada.
- **Campaign:** Elige hasta 10 Campaigns. Cuando se aplica, tu panel mostrará métricas solo para las Campaigns seleccionadas. Si seleccionas primero un filtro de etiqueta, las opciones de filtros de Campaign solo incluirán las Campaigns que tengan la etiqueta seleccionada.

![Opciones de filtro en el panel de rendimiento del canal donde puedes seleccionar una etiqueta y una lista de Canvas para filtrar.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparación de periodos de tiempo {#comparing-time-periods}

El panel de rendimiento del canal compara automáticamente el periodo de tiempo que has seleccionado en el rango de fechas con el periodo anterior, sumando el mismo número de días. Por ejemplo, si eliges "Últimos 7 días" como rango de fechas en el panel, la comparación con el periodo anterior comparará las métricas de los últimos siete días con los siete días previos. Si seleccionas un rango de fechas personalizado, digamos del 10 al 15 de mayo, que son seis días de datos, el panel comparará las métricas de esos días con las métricas del 4 al 9 de mayo.

La comparación es el cambio porcentual entre el periodo anterior y el actual, calculado tomando la diferencia entre los dos periodos y dividiéndola por la métrica del periodo anterior.

### Visualización de cambios en totales y tasas {#viewing-changes-in-total-counts-and-rates}

Puedes alternar entre **Show Change in Totals**, que compara los recuentos totales (como el número de correos electrónicos entregados) entre los dos periodos, y **Show Change in Rates**, que compara las tasas (como la tasa de entrega).

![Botones de opción para alternar entre mostrar el cambio en totales o el cambio en tasas en el panel de rendimiento del canal.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué mi panel muestra valores vacíos? {#why-is-my-dashboard-displaying-empty-values}

Hay algunos escenarios que podrían generar valores vacíos para una métrica:

- Braze registró ceros para esa métrica en particular en el rango de fechas seleccionado.
- No has enviado ningún mensaje durante el rango de fechas seleccionado.
- Aunque hubo métricas como aperturas, clics o cancelaciones de suscripción para un rango de fechas seleccionado, no hubo entregas ni envíos. En este caso, Braze no calculará una métrica de tasa.

Para ver más métricas, intenta ampliar el rango de fechas.

### ¿Por qué mi panel de correo electrónico muestra más Other Opens que Unique Opens? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Para la métrica _Unique Opens_, Braze deduplicará cualquier apertura repetida registrada por un usuario determinado (ya sea que incluya _Machine Opens_ u _Other Opens_) de modo que solo se incremente una única _Unique Open_ si un usuario abre varias veces. Para _Other Opens_, Braze no deduplica.

<!---Temporarily hidden until functionality is added

## Valores vacíos en tus datos {#empty-values-in-your-data}

### Si una métrica muestra "0%" o "0" {#if-a-metric-displays-0-or-0}

Esto significa que Braze registró cero para esa métrica en particular durante el periodo de tiempo que seleccionaste.

#### Si una métrica muestra "N/A" {#if-a-metric-displays-na}

Esto significa que, aunque Braze registró recuentos positivos para una métrica en particular durante el periodo de tiempo que seleccionaste, el denominador para el cálculo de la tasa (ya sea envíos o entregas en la mayoría de los casos) fue cero. Esto puede ocurrir cuando los correos electrónicos se envían un día y las aperturas y los clics se registran en los días siguientes, si el periodo de tiempo seleccionado no incluye la fecha en que se enviaron los mensajes.

#### Si una métrica muestra "--" {#if-a-metric-displays}

Esto significa que Braze no ha registrado ningún dato para esa métrica durante el tiempo que seleccionaste. Si aún no has configurado ni enviado ningún correo electrónico, obtén más información sobre cómo hacerlo en nuestra sección dedicada de [correo electrónico]({{site.baseurl}}/user_guide/channels/email).

--->