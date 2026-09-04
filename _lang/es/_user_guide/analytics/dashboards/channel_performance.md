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

Consulta tu panel de rendimiento de correo electrónico yendo a **Analytics** > **Email Performance** y seleccionando el intervalo de fechas del periodo del que quieres ver datos. Tu intervalo de fechas puede abarcar hasta un año en el pasado.

{% alert note %}
Para ver el panel de **Email Performance**, necesitas el permiso "View Usage Data" o "View Dashboard Reports".
{% endalert %}

![Panel de rendimiento de correo electrónico que muestra la participación del canal de correo electrónico en los últimos treinta días.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

![Un ejemplo de Campaign de correo electrónico con 335.630 envíos y un promedio de 11.187,667 por día.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Cómo se calculan las métricas {#how-metrics-are-calculated}

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="email" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envíos | Recuento | Número total de envíos de cada día en el intervalo de fechas |
| Tasa de entrega | Tasa | (Número total de entregas de cada día en el intervalo de fechas) / (Número total de envíos de cada día en el intervalo de fechas) |
| Tasa de rebote | Tasa | (Número total de rebotes de cada día en el intervalo de fechas) / (Número total de envíos de cada día en el intervalo de fechas) |
| Tasa de cancelaciones | Tasa | (Número total de cancelaciones de suscripción únicas de cada día en el intervalo de fechas) / (Número total de entregas en un intervalo de fechas)<br><br>Esto usa cancelaciones de suscripción únicas, que también se usan en los análisis de Campaigns, el resumen y el generador de informes. Estas cancelaciones de suscripción se registran en todas las fuentes (como la REST API, las importaciones CSV, los correos electrónicos y las cancelaciones de suscripción por lista). Las tasas de cancelaciones de suscripción en los análisis de Campaign y Canvas son cancelaciones que se producen como resultado de un clic en cancelar suscripción en un correo electrónico entregado por Braze.  |
| Tasa de aperturas únicas | Tasa | (Número total de aperturas únicas de cada día en el intervalo de fechas) / (Número total de entregas en un intervalo de fechas) |
| Tasa de otras aperturas | Tasa | (Número total de otras aperturas de cada día en el intervalo de fechas) / (Número total de entregas en un intervalo de fechas)<br><br>Otras aperturas incluyen correos electrónicos que no se han identificado como aperturas de máquina, como cuando un usuario abre un correo electrónico. Esta métrica no es única y es una submétrica de las aperturas totales.  |
| Tasa de clics únicos | Tasa | (Número total de clics únicos de cada día en el intervalo de fechas) / (Número total de entregas en un intervalo de fechas) |
| Tasa de clic a apertura única | Tasa | (Número total de clics únicos de cada día en el intervalo de fechas) / (Número total de aperturas únicas de cada día en el intervalo de fechas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cómo se calculan las métricas" }

{% endtab %}
{% tab Información sobre correo electrónico %}

### Panel de información sobre correo electrónico {#email-insights-dashboard}

El panel de información sobre correo electrónico rastrea dónde y cuándo tus clientes interactúan con tus correos electrónicos. Estos informes pueden proporcionar datos detallados y granulares sobre cómo optimizar tus correos electrónicos para generar mayor participación. El panel de información sobre correo electrónico incluye hasta los últimos seis meses de datos. Para acceder al panel, ve a **Analytics** > **Email Performance** > **Email Insights**.

#### Participación por dispositivo {#engagement-by-device}

El informe **Engagement by Device** proporciona un desglose de qué dispositivos están usando tus usuarios para interactuar con tu correo electrónico. Estos datos rastrean la participación del correo electrónico en dispositivos móviles, de escritorio, tabletas y otros tipos de dispositivos. Estos datos se basan en la cadena de agente de usuario transmitida desde los dispositivos de tus usuarios.

{% alert note %}
Si utilizas CloudFront como tu CDN, asegúrate de que el agente de usuario de tus usuarios se transmita al ESP. De lo contrario, cada agente de usuario se mostrará como "Amazon Cloudfront".
{% endalert %}

La categoría "Otro" incluye cualquier cadena de usuario que no pueda identificarse como escritorio, móvil o tableta. Por ejemplo, televisión, automóvil, consola de videojuegos, OTT (over-the-top o streaming) y similares. Esto también puede incluir valores nulos o vacíos.

Para comprender mejor qué hay en esta categoría "Otro", puedes extraer los agentes de usuario usando cualquiera de estas opciones:

1. [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) te enviará la cadena exacta de agente de usuario que se recuperó de los dispositivos de tus usuarios.
2. Aprovecha nuestro [generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para usar SQL o nuestro [generador de consultas de IA]({{site.baseurl}}/user_guide/analytics/reports/query_builder#generating-sql-with-the-ai-query-builder) para ver los agentes de usuario.

![Informe de participación por dispositivo que muestra el número de clics para dispositivos móviles, de escritorio, tabletas y otros. La mayor cantidad de clics se produce en dispositivos móviles.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Para las aperturas de correo electrónico, Braze separará Google Image Proxy, Apple Image Proxy y Yahoo Mail Proxy. Estos servicios almacenan en caché y cargan todas las imágenes incrustadas en un correo electrónico antes de que se entregue al destinatario. Como resultado, esto activará una apertura de correo electrónico desde los servidores del proveedor de buzón en lugar del servidor del destinatario, lo que puede llevar a aperturas de correo electrónico infladas. Estos servicios están destinados a mejorar la privacidad, la seguridad, el rendimiento y la eficiencia al cargar imágenes. Esto también puede contener aperturas reales de destinatarios, ya que estos servicios proxy enmascaran el agente de usuario, y Braze categoriza los datos proxy usando el agente de usuario.

![Informe de participación por dispositivo que muestra el número de clics para dispositivos móviles, de escritorio, tabletas, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy y otros. La mayor cantidad de aperturas se produce en dispositivos móviles.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

#### Participación por proveedor de buzón {#engagement-by-mailbox-provider}

El informe **Engagement by Mailbox Provider** muestra los principales proveedores de buzón que contribuyen a tus clics o aperturas. Puedes hacer clic en proveedores de buzón principales específicos para profundizar en dominios de recepción específicos. Por ejemplo, si Microsoft aparece en este informe como una de tus principales métricas de proveedor de buzón, puedes ver más detalles de sus dominios de recepción, como "outlook.com", "hotmail.com", "live.com" y más.

![Un ejemplo de informe de participación por proveedor de buzón con Google, Apple iCloud, Yahoo, Microsoft y Mail.Ru Group y su número correspondiente de clics.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

#### Momento de la participación {#time-of-engagement}

El informe **Time of Engagement** muestra datos sobre cuándo los usuarios interactúan con tus correos electrónicos. Esto puede ayudar a responder preguntas como qué día de la semana o qué hora presenta la mayor participación de tus clientes. Con esta información, puedes experimentar con el mejor día u hora para enviar tus mensajes y generar una mayor participación. Ten en cuenta que estos horarios se basan en la zona horaria de tu empresa.

El informe de participación por **día de la semana** desglosa las aperturas o clics por día de la semana.

![Un ejemplo de informe de participación por día de la semana con la mayor cantidad de clics los lunes y miércoles.]({% image_buster /assets/img_archive/time_engagement.png %})

El informe de participación por **hora del día** desglosa las aperturas o clics por cada hora en una ventana de tiempo de 24 horas.

![Un ejemplo de informe de participación por hora del día con las aperturas o clics de 12 a.m. a 11 p.m.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Para obtener más información sobre los análisis de tus correos electrónicos, consulta [Informes de correo electrónico]({{site.baseurl}}/user_guide/channels/email/reporting).

{% endtab %}
{% tab Rendimiento de SMS %}

### Panel de rendimiento de SMS {#sms-performance-dashboard}

Para usar tu panel de rendimiento de SMS, ve a **Analytics** > **SMS Performance** y selecciona el intervalo de fechas del periodo del que quieres ver datos. Tu intervalo de fechas puede abarcar hasta un año en el pasado.

![Un ejemplo de Campaign de SMS con 335.630 envíos y un promedio de 11.187,667 por día.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

#### Cómo se calculan las métricas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="SMS" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envíos | Recuento | Número total de envíos de cada día en el intervalo de fechas |
| Tasa de entregas confirmadas | Tasa | (Número total de entregas de cada día en el intervalo de fechas) / (Número total de envíos de cada día en el intervalo de fechas) |
| Tasa de fallos de entrega | Tasa | (Número total de fallos de cada día en el intervalo de fechas) / (Número total de envíos de cada día en el intervalo de fechas) |
| Tasa de rechazos | Tasa | (Número total de rechazos de cada día en el intervalo de fechas) / (Número total de envíos de cada día en el intervalo de fechas) |
| Tasa de clics | Tasa | (Número total de clics de cada día en el intervalo de fechas) / (Número total de entregas de cada día en el intervalo de fechas) |
| Total de adhesiones voluntarias | Tasa | Número total de adhesiones voluntarias por mensaje entrante de cada día en el intervalo de fechas |
| Total de cancelaciones | Tasa | Número total de cancelaciones por mensaje entrante de cada día en el intervalo de fechas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cómo se calculan las métricas" }

{% endtab %}
{% tab Rendimiento de push %}

### Panel de rendimiento de push {#push-performance-dashboard}

El panel de **Push Performance** te ofrece una vista a nivel de canal de la participación push en todas tus Campaigns y Canvas, para que puedas comprender el estado del canal sin tener que acumular datos de mensajes individuales.

Para abrir el panel, ve a **Analytics** > **Push Performance** y selecciona el intervalo de fechas del periodo del que quieres ver datos. Tu intervalo de fechas puede abarcar hasta un año en el pasado.

![Panel de rendimiento de push que muestra la participación del canal push en los últimos treinta días.]({% image_buster /assets/img_archive/push_performance_dashboard_performance_tab.png %})

#### Resumen {#overview}

El banner de resumen presenta cuatro métricas principales para el intervalo de fechas seleccionado: *Envíos*, *Tasa de entrega*, *Tarifa abierta* y *Tasa de conversión*. Cada ficha muestra un valor principal, un recuento de apoyo y una descripción emergente con detalles estadísticos adicionales.

La tasa de conversión en este panel está limitada únicamente a tu evento de conversión primaria. Para analizar eventos de conversión secundarios, usa el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

#### Participación a lo largo del tiempo {#engagement-over-time}

En la sección de participación a lo largo del tiempo, cada métrica se representa como un gráfico de línea en el intervalo de fechas seleccionado:

- Envíos
- Aperturas totales
- Direct Opens
- Influenced Opens
- Tasa de Direct Opens
- Tasa de conversión
- Rebotes

Puedes activar un punto de referencia de la industria en el gráfico de tasa de Direct Opens. Los puntos de referencia están desactivados de forma predeterminada. Para más información, consulta [Puntos de referencia](#benchmarking).

#### Cómo se calculan las métricas

{% multi_lang_include analytics/channel_performance_how_metrics_calculated.md channel="push" %}

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Envíos | Recuento | Número total de envíos de cada día en el intervalo de fechas |
| Tasa de entrega | Tasa | (Número total de entregas de cada día en el intervalo de fechas) / (Número total de envíos de cada día en el intervalo de fechas) |
| Tasa de rebote | Tasa | (Número total de rebotes de cada día en el intervalo de fechas) / (Número total de envíos de cada día en el intervalo de fechas) |
| Tasa de Direct Opens | Tasa | (Número total de Direct Opens de cada día en el intervalo de fechas) / (Número total de entregas de cada día en el intervalo de fechas) |
| Tasa de Influenced Opens | Tasa | (Número total de Influenced Opens de cada día en el intervalo de fechas) / (Número total de entregas de cada día en el intervalo de fechas) |
| Tasa total de aperturas | Tasa | (Número total de aperturas totales de cada día en el intervalo de fechas) / (Número total de entregas de cada día en el intervalo de fechas)<br><br>Las aperturas totales incluyen tanto Direct Opens como Influenced Opens. |
| Tasa de conversión | Tasa | (Número total de conversiones primarias de cada día en el intervalo de fechas) / (Número total de destinatarios de cada día en el intervalo de fechas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cómo se calculan las métricas" }

{% endtab %}
{% tab Información sobre push %}

### Panel de información sobre push {#push-insights-dashboard}

El panel de información sobre push presenta patrones sobre cómo tu audiencia responde a las notificaciones push, para que puedas ajustar lo que envías y con qué frecuencia. Para acceder, ve a **Analytics** > **Push Performance** > **Insights**.

#### Frecuencia {#frequency}

El informe de frecuencia muestra la relación entre cuántas notificaciones push recibe un usuario y su tarifa abierta, para que puedas encontrar el punto en el que los envíos adicionales dejan de generar participación. El gráfico destaca un volumen de envío recomendado basado en datos de referencia para tu vertical.

{% alert important %}
Los informes de frecuencia y cadencia usan un período mínimo de análisis de tres meses. Si seleccionas un intervalo de fechas más corto, Braze puede ampliar la fecha de inicio para incluir hasta tres meses de datos cuando estén disponibles. Estos informes no se ven afectados por los filtros de etiqueta, Campaign, Canvas o plataforma: siempre reflejan tu volumen total de push para el intervalo de fechas seleccionado.
{% endalert %}

#### Cadencia {#cadence}

Mientras que el informe de frecuencia te indica cuántos mensajes enviar, el informe de cadencia te indica cómo espaciarlos. Grafica la tarifa abierta frente a la cadencia de envío, para que puedas ver si concentrar tus envíos, por ejemplo, tres notificaciones push aterrizando en un fin de semana, te cuesta participación en comparación con distribuirlos a lo largo de la semana.

Úsalo junto con el informe de frecuencia: la frecuencia establece tu objetivo de volumen, la cadencia establece la distribución.

#### Distribución del rendimiento de Campaigns {#campaign-performance-distribution}

Este informe grafica cada Campaign de push en tu intervalo de fechas por tarifa abierta y tasa de conversión, para que puedas ver a tus Campaigns con mejor y peor rendimiento de un vistazo y buscar qué tienen en común.

En el gráfico de distribución del rendimiento de Campaigns, haz clic en el icono de tres puntos y selecciona **Ver tabla de datos**, que muestra una tabla ordenable que enumera las mismas Campaigns. Puedes ordenar por tarifa abierta o tasa de conversión para clasificar el rendimiento, y usarla para abrir los análisis de una Campaign individual.

{% endtab %}
{% tab Capacidad de entrega de push %}

### Panel de capacidad de entrega de push {#push-deliverability-dashboard}

El panel de capacidad de entrega de push rastrea la salud de tu audiencia push a lo largo del tiempo, para que puedas ver cómo tu mensajería afecta a tu base alcanzable. Para acceder, ve a **Analytics** > **Push Performance** > **Deliverability**.

Este panel se filtra solo por intervalo de fechas, y cada métrica se desglosa por plataforma.

#### Tasa de rebote {#bounce-rate}

Los rebotes en el intervalo de fechas seleccionado, desglosados por plataforma. Puedes activar un punto de referencia de la industria en este gráfico. Está desactivado de forma predeterminada.

#### Tasa de desinstalación {#uninstall-rate}

Las desinstalaciones en el intervalo de fechas seleccionado, desglosadas por plataforma. Usa esto para ver si un periodo de envío intenso coincidió con la pérdida de usuarios. Los datos de desinstalación dependen de tu configuración de Uninstall Tracking. Consulta [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking). Uninstall Tracking es compatible con iOS, Android (excepto Huawei) y Kindle. Si Uninstall Tracking está desactivado, los datos de tasa de desinstalación son menos completos y pueden ser menos precisos. Dependiendo del sistema operativo, los informes de desinstalación pueden llegar más tarde o en lotes, por lo que el gráfico podría no reflejar la fecha exacta de desinstalación.

#### Cómo se calculan las métricas

| Métrica | Tipo | Cálculo |
| --- | --- | ---- |
| Tasa de desinstalación | Tasa | (Número total de dispositivos en los que Braze ha recibido una señal de que fueron desinstalados de cada día en el intervalo de fechas) / (Número total de dispositivos con tokens válidos de cada día en el intervalo de fechas) |
| Tasa de rebote | Tasa | (Número total de rebotes de cada día en el intervalo de fechas) / (Número total de envíos de cada día en el intervalo de fechas) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Cómo se calculan las métricas" }

{% endtab %}
{% endtabs %}

## Filtros del panel {#dashboard-filters}

Puedes filtrar los datos de tu panel utilizando las siguientes opciones de filtro:

- **Etiqueta:** Elige una etiqueta. Cuando se aplique, tu panel mostrará métricas solo para la etiqueta seleccionada. Ten en cuenta que el panel de push admite múltiples etiquetas.
- **Plataformas:** (Solo paneles de push) Elige una plataforma de push, como **All Push**, **Android**, **iOS**, **Mobile combined**, **Kindle** o **Web**. Cuando se aplique, tu panel mostrará métricas solo para la plataforma seleccionada.
- **Canvas:** Elige hasta 10 Canvas. Cuando se aplique, tu panel mostrará métricas solo para los Canvas seleccionados. Si seleccionas primero un filtro de etiqueta, las opciones para filtros de Canvas solo incluirán los Canvas que tengan la etiqueta seleccionada.
- **Campaign:** Elige hasta 10 Campaigns. Cuando se aplique, tu panel mostrará métricas solo para las Campaigns seleccionadas. Si seleccionas primero un filtro de etiqueta, las opciones para filtros de Campaign solo incluirán las Campaigns que tengan la etiqueta seleccionada.

{% alert note %}
Los filtros se aplican de manera diferente en los distintos paneles de push. El panel de rendimiento de push admite todos los filtros. El panel de capacidad de entrega de push solo admite el rango de fechas, con un desglose por plataforma mostrado en cada gráfico. Los informes de frecuencia y cadencia en el panel de información de push solo admiten el rango de fechas.
{% endalert %}

![Opciones de filtro en el panel de rendimiento del canal donde puedes seleccionar una etiqueta y una lista de Canvas para filtrar.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Comparación de períodos de tiempo {#comparing-time-periods}

El panel de rendimiento del canal compara automáticamente el período de tiempo que has seleccionado en el rango de fechas con el período anterior, sumando la misma cantidad de días. Por ejemplo, si eliges "Últimos 7 días" como rango de fechas en el panel, la comparación con el período anterior contrastará las métricas de los últimos siete días con las de los siete días previos. Si seleccionas un rango de fechas personalizado, digamos del 10 de mayo al 15 de mayo, lo que equivale a seis días de datos, el panel comparará las métricas de esos días con las métricas del 4 de mayo al 9 de mayo.

La comparación es el cambio porcentual entre el período anterior y el actual, calculado tomando la diferencia entre los dos períodos y dividiéndola entre la métrica del período anterior.

### Ver cambios en totales y tasas {#viewing-changes-in-total-counts-and-rates}

Puedes alternar entre **Show Change in Totals**, que compara los recuentos totales (como la cantidad de correos electrónicos entregados) entre los dos períodos, y **Show Change in Rates**, que compara las tasas (como la tasa de entrega).

![Botones de opción para alternar entre mostrar el cambio en totales o el cambio en tasas en el panel de rendimiento del canal.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Evaluación comparativa {#benchmarking}

En los paneles push, puedes comparar tu rendimiento con datos agregados y anonimizados de Braze.

### Evaluaciones comparativas disponibles {#available-benchmarks}

| Evaluación comparativa | Dónde aparece | Predeterminado |
| --- | --- | ---- |
| Tarifa abierta directa | Rendimiento push | Desactivado |
| Tasa de rebote | Capacidad de entrega push | Desactivado |
| Frecuencia | Información push | Activado |
| Cadencia | Información push | Activado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Evaluaciones comparativas disponibles" }

Las evaluaciones comparativas de tarifa abierta directa y tasa de rebote se desglosan por plataforma. Todas las evaluaciones comparativas push se miden con respecto a la tarifa abierta, no a la tasa de conversión.

### Comparar verticales {#comparing-verticals}

Los datos de evaluación comparativa se dividen por vertical. Tu panel se configura de forma predeterminada con la vertical de tu cuenta, y puedes usar el menú desplegable para comparar con otra.

### Comparar regiones {#comparing-regions}

Los datos de evaluación comparativa se dividen por región. Tu panel se configura de forma predeterminada con la región de tu cuenta, y puedes usar el menú desplegable para comparar con otra.

{% alert note %}
Si los datos de evaluación comparativa más recientes no están disponibles para el intervalo de tiempo seleccionado, Braze muestra una evaluación comparativa estimada.

Los datos de evaluación comparativa se actualizan mensualmente.
{% endalert %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Por qué mi panel muestra valores vacíos? {#why-is-my-dashboard-displaying-empty-values}

Hay algunos escenarios que podrían dar lugar a valores vacíos para una métrica:

- Braze registró ceros para esa métrica en particular en el intervalo de fechas seleccionado.
- No has enviado ningún mensaje durante el intervalo de fechas seleccionado.
- Aunque hubo métricas como aperturas, clics o cancelaciones de suscripción en el intervalo de fechas seleccionado, no hubo entregas ni envíos. En este caso, Braze no calculará una métrica de tasa.

Para ver más métricas, intenta ampliar el intervalo de fechas.

### ¿Por qué mi panel de correo electrónico muestra más Other Opens que Unique Opens? {#why-does-my-email-dashboard-display-more-other-opens-than-unique-opens}

Para la métrica _Unique Opens_, Braze deduplicará cualquier apertura repetida registrada por un usuario determinado (ya sea que incluya _Machine Opens_ u _Other Opens_) de modo que solo se incremente una única _Unique Open_ si un usuario abre varias veces. Para _Other Opens_, Braze no deduplica.

### ¿Por qué mis informes de frecuencia y cadencia están vacíos? {#why-are-my-frequency-and-cadence-reports-empty}

Estos informes utilizan una ventana de análisis de tres meses. Si el intervalo seleccionado es más corto, Braze puede ampliar el intervalo para incluir fechas anteriores cuando los datos estén disponibles.

Si tu intervalo de fechas es lo suficientemente largo y los informes siguen vacíos, es posible que los datos de referencia aún no estén disponibles para tu espacio de trabajo. Contacta con soporte de Braze si tienes alguna pregunta.

### ¿Por qué mis filtros no cambian los informes de frecuencia y cadencia? {#why-dont-my-filters-change-the-frequency-and-cadence-reports}

Los informes de frecuencia y cadencia siempre reflejan tu volumen total de push, porque su valor proviene de medir la carga total de mensajes sobre un usuario. Filtrar por un subconjunto de Campaigns subestimaría la cantidad de mensajes que ese usuario realmente recibió. Solo se aplica el filtro de intervalo de fechas.
<!---Temporarily hidden until functionality is added

## Valores vacíos en tus datos {#empty-values-in-your-data}

### Si una métrica muestra "0%" o "0" {#if-a-metric-displays-0-or-0}

Esto significa que Braze registró cero para esa métrica en particular durante el periodo de tiempo que seleccionaste.

#### Si una métrica muestra "N/A" {#if-a-metric-displays-na}

Esto significa que, aunque Braze registró recuentos positivos para una métrica en particular durante el periodo de tiempo que seleccionaste, el denominador para el cálculo de la tasa (ya sea envíos o entregas en la mayoría de los casos) fue cero. Esto puede ocurrir cuando los correos electrónicos se envían un día y las aperturas y clics se registran en los días siguientes, si el periodo de tiempo seleccionado no incluye la fecha en que se enviaron los mensajes.

#### Si una métrica muestra "--" {#if-a-metric-displays}

Esto significa que Braze no ha registrado ningún dato para esa métrica durante el tiempo que seleccionaste. Si aún no has configurado ni enviado ningún correo electrónico, obtén más información sobre cómo hacerlo en nuestra sección dedicada de [correo electrónico]({{site.baseurl}}/user_guide/channels/email).

--->