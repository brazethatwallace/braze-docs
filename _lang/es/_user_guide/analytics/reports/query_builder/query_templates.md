---
nav_title: Plantillas de consultas
article_title: Plantillas del Generador de consultas
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artículo de referencia enumera los tipos de informes que puedes crear utilizando datos de Braze desde Snowflake en el Generador de consultas."
tool: Reports
---

# Plantillas del Generador de consultas {#query-builder-templates}

> Accede a las plantillas del [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) seleccionando **Query Template** al crear un informe. Todas las plantillas muestran datos de hasta los últimos 60 días, pero puedes editar directamente ese y otros valores en el editor.<br><br>Para consultar las definiciones de las métricas que pueden aparecer en tus informes del Generador de consultas, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary) y filtra por el canal correspondiente.

## Plantillas de canal {#channel-templates}

<style>
table th:nth-child(1) {
    width: 30%;
}
table th:nth-child(2) {
    width: 70%;
}
table td {
    word-break: break-word;
}
</style>

| Nombre de la consulta | Descripción |
| --- | --- |
| Interacción y ingresos por canal | Este informe muestra, para cada canal, todas las métricas de interacción (como aperturas y clics), ingresos, número de transacciones y precio promedio. {::nomarkdown} <ul> <li> <i>Número de transacciones:</i> Número de eventos de compra </li> <li> <i>Precio promedio:</i> Ingresos divididos entre transacciones </li> </ul> {:/} ![Captura de pantalla relacionada con las plantillas de canal.]({% image_buster /assets/img_archive/channel_engagement_revenue.png %}) |
| Compras e ingresos por segmento | Este informe muestra métricas de los mensajes enviados para un segmento específico. <br><br> Las métricas de compra son únicas durante todo el periodo del informe. Un usuario puede generar como máximo una compra. Los ingresos tienen en cuenta cada compra del periodo del informe. |
| Compras e ingresos por variantes o pasos, por segmento | Este informe muestra métricas de las variantes o pasos en Canvas de los mensajes enviados a cada segmento. <br><br> Las métricas de compra son únicas durante todo el periodo del informe. Un usuario puede generar como máximo una compra. Los ingresos tienen en cuenta cada compra del periodo del informe. |
| Mejores/peores mensajes en compras | Este informe muestra métricas de compra de las mejores o peores campañas, Canvas o pasos en Canvas. Cada fila es una campaña, Canvas o paso en Canvas. Debes especificar si deseas mostrar los de mejor o peor rendimiento, y la métrica específica para ejecutar este análisis (como *Compras únicas tras recepción*, *Ingresos tras recepción*, *Destinatarios únicos*). <br><br> Las filas en los informes de mejor rendimiento se ordenan de mejor a peor, mientras que las filas en los informes de peor rendimiento se ordenan de peor a mejor. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de canal" }

## Plantillas de Campaign {#campaign-templates}

| Nombre de la consulta | Descripción |
| --- | --- |
| Ingresos de Campaign por país | Este informe muestra los ingresos por país para una Campaign específica. Para ejecutar este informe, debes especificar el identificador de API de una Campaign. Puedes encontrar el identificador de API de una Campaign en la parte inferior de la página de detalles de esa Campaign. <br><br> Este informe muestra, para cada país, la cantidad de ingresos generados, el número de pedidos, el número de devoluciones, los ingresos netos y los ingresos brutos.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devoluciones:</i> Número de eventos de compra con valores de ingresos negativos </li> <li><i> Ingresos netos:</i> Ingresos de todas las no devoluciones </li> <li><i> Ingresos brutos:</i> Ingresos que incluyen el valor de las devoluciones </li></ul>{:/} ![Captura de pantalla relacionada con las plantillas de Campaign.]({% image_buster /assets/img_archive/campaign_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de Campaign" }

## Plantillas de Canvas {#canvas-templates}

| Nombre de la consulta | Descripción |
| --- | --- |
| Ingresos de Canvas por país | Este informe muestra los ingresos por país para un Canvas específico. Para ejecutar este informe, debes especificar el identificador de API de un Canvas. Puedes encontrar el identificador de API del Canvas en **Analyze Variants**. <br><br> Este informe muestra, para cada país, la cantidad de ingresos generados, el número de pedidos, el número de devoluciones, los ingresos netos y los ingresos brutos.<br><br> {::nomarkdown} <ul> <li> <i>Pedidos:</i> Número de eventos de compra </li> <li><i> Devoluciones:</i> Número de eventos de compra con valores de ingresos negativos </li> <li><i> Ingresos netos:</i> Ingresos de todas las no devoluciones </li> <li><i> Ingresos brutos:</i> Ingresos que incluyen el valor de las devoluciones </li></ul>{:/} ![Captura de pantalla relacionada con las plantillas de Canvas.]({% image_buster /assets/img_archive/canvas_revenue_country.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de Canvas" }

## Plantillas de correo electrónico {#email-templates}

| Nombre de la consulta | Descripción |
| --- | --- |
| Rebotes de correo electrónico por dominio | El número de rebotes por dominio de correo electrónico, desglosado en rebotes totales, rebotes duros y rebotes blandos. <br> ![Captura de pantalla relacionada con las plantillas de correo electrónico.]({% image_buster /assets/img_archive/query_builder_q4.png %}){: style="max-width:60%;"} |
| Métricas de entrega de correo electrónico por día | Este informe muestra métricas de los mensajes enviados cada día, como cuántos correos electrónicos se enviaron, entregaron, rebotaron con rebote blando y rebotaron con rebote duro. <br><br> Todas las métricas son únicas durante todo el periodo del informe. Por ejemplo, si un correo electrónico de bienvenida tuvo un rebote blando una vez el 21 de noviembre, dos veces el 22 de noviembre y nunca se entregó: {::nomarkdown} <ul><li> La métrica de <i>Rebotes blandos</i> del 21 de noviembre aumenta en uno.</li><li> La métrica de <i>Rebotes blandos</i> del 22 de noviembre no se ve afectada. </li></ul>{:/} ![Captura de pantalla relacionada con las plantillas de correo electrónico.]({% image_buster /assets/img_archive/email_delivery_day.png %})|
| Métricas de interacción de correo electrónico por segmento | Este informe muestra métricas de los mensajes enviados a cada segmento, como cuántos correos electrónicos se enviaron, entregaron, rebotaron con rebote blando y rebotaron con rebote duro. <br><br> Todas las métricas son únicas durante todo el periodo del informe. Por ejemplo, si un correo electrónico de bienvenida tuvo un rebote blando una vez el 21 de noviembre, dos veces el 22 de noviembre y nunca se entregó: {::nomarkdown} <ul><li> La métrica de <i>Rebotes blandos</i> del 21 de noviembre aumenta en uno. </li><li> La métrica de <i>Rebotes blandos</i> del 22 de noviembre no se ve afectada.</li></ul>{:/} ![Captura de pantalla relacionada con las plantillas de correo electrónico.]({% image_buster /assets/img_archive/email_engagement_segment.png %}) |
| Métricas de interacción de correo electrónico por variantes o pasos, por segmento | Este informe muestra métricas de las variantes o pasos en Canvas de los mensajes enviados a cada segmento. Estas métricas incluyen cuántos correos electrónicos se enviaron, entregaron, rebotaron con rebote blando y rebotaron con rebote duro. <br><br> Todas las métricas son únicas durante todo el periodo del informe. Por ejemplo, si un correo electrónico de bienvenida tuvo un rebote blando una vez el 21 de noviembre, dos veces el 22 de noviembre y nunca se entregó: {::nomarkdown} <ul><li> La métrica de <i>Rebotes blandos</i> del 21 de noviembre aumenta en uno. </li> <li> La métrica de <i>Rebotes blandos</i> del 22 de noviembre no se ve afectada.</li></ul> {:/} |
| Rendimiento de correo electrónico por país | Este informe muestra las siguientes métricas para cada país: envíos, tasa de apertura indirecta y tasa de apertura directa. El país es el país del usuario en el momento del envío del correo electrónico. <br><br> ![Captura de pantalla relacionada con las plantillas de correo electrónico.]({% image_buster /assets/img_archive/query_builder_q3.png %}) |
| Registros de cambios de suscripción de correo electrónico | Este informe muestra las métricas registradas sobre el cambio de suscripción de cada usuario, como su dirección de correo electrónico, estado de suscripción, la hora en que se cambió su estado y la Campaign o Canvas asociado. |
| Adhesiones y cancelaciones de grupos de suscripción de correo electrónico | Este informe muestra el número de adhesiones y cancelaciones únicas de usuarios para cualquier grupo de suscripción de correo electrónico por semana. Debes tener al menos un [grupo de suscripción de correo electrónico]({{site.baseurl}}/user_guide/channels/email/subscriptions) en el espacio de trabajo para ejecutar esta consulta. <br><br> ![Captura de pantalla relacionada con las plantillas de correo electrónico.]({% image_buster /assets/img_archive/query_builder_q2.png %}){: style="max-width:70%;"} |
| URLs de correo electrónico con clics | Este informe muestra el número de clics que tuvo cada enlace en un correo electrónico. Para ejecutar este informe, necesitarás especificar el identificador de API de una Campaign o Canvas. Puedes encontrar el identificador de API de una Campaign en la parte inferior de la página de detalles de esa Campaign y el identificador de API del Canvas en **Analyze Variants**. <br><br> Este informe muestra enlaces despersonalizados y un recuento de clics para cada enlace. Tu descarga CSV incluirá los ID de usuario de todos los usuarios que hicieron clic, el enlace en el que hicieron clic y una marca de tiempo de cuándo hicieron clic. <br><br> *URLs despersonalizadas:* URLs a las que se les han eliminado las etiquetas de Liquid. <br><br> ![Captura de pantalla relacionada con las plantillas de correo electrónico.]({% image_buster /assets/img_archive/query_builder_q5.png %}){: style="max-width:70%;"} |
| Mejores/peores mensajes en interacción de correo electrónico | Este informe muestra métricas de interacción de correo electrónico de las mejores o peores campañas, Canvas o pasos en Canvas. Debes especificar si deseas mostrar los de mejor o peor rendimiento, y la métrica específica para ejecutar este análisis (como *Enviados*, *Rebotes blandos* y *Aperturas únicas*). <br><br> Las filas en los informes de mejor rendimiento se ordenan de mejor a peor, mientras que las filas en los informes de peor rendimiento se ordenan de peor a mejor. <br><br> ![Captura de pantalla relacionada con las plantillas de correo electrónico.]({% image_buster /assets/img_archive/top-bottom-email.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas de correo electrónico" }

## Plantillas móviles {#mobile-templates}

| Nombre de la consulta | Descripción |
| --- | --- |
| Operadores de dispositivos | El número de usuarios por operador de dispositivo, como Verizon y T-Mobile. <br><br> ![Captura de pantalla relacionada con las plantillas móviles.]({% image_buster /assets/img_archive/device_carriers.png %}){: style="max-width:50%;"} |
| Modelos de dispositivos | El número de usuarios por modelo de dispositivo, como iPhone 15 Pro y Pixel 7. <br><br> ![Captura de pantalla relacionada con las plantillas móviles.]({% image_buster /assets/img_archive/device_models.png %}){: style="max-width:50%;"} |
| Sistemas operativos de dispositivos | El número de usuarios por sistema operativo, como 17.4 y Android 14. <br><br> ![Captura de pantalla relacionada con las plantillas móviles.]({% image_buster /assets/img_archive/os_version.png %}){: style="max-width:50%;"} |
| Resoluciones de pantalla de dispositivos | El número de usuarios por resolución de pantalla del dispositivo, como 1179x2556 y 750x1334. <br><br> ![Captura de pantalla relacionada con las plantillas móviles.]({% image_buster /assets/img_archive/device_screen_resolutions.png %}){: style="max-width:40%;"} |
| Códigos de error de SMS | Este informe muestra el tipo de error y el número de errores para cada código de error de SMS. <br><br>![Captura de pantalla relacionada con las plantillas móviles.]({% image_buster /assets/img_archive/sms_errors.png %}){: style="max-width:50%;"} |
| Errores de proveedor de SMS por usuario | Este informe muestra los códigos de error de SMS para un usuario específico. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas móviles" }

## Plantillas push {#push-templates}

| Nombre de la consulta | Descripción |
| --- | --- |
| Rendimiento push por país | Este informe muestra las siguientes métricas para cada país: entregas, tasa de apertura y tasa de clics. El país es el país del usuario en el momento del envío del correo electrónico. <br><br> ![Captura de pantalla relacionada con las plantillas push.]({% image_buster /assets/img_archive/query_builder_q7.png %}){: style="max-width:70%;"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Plantillas push" }

## Desglose por segmento {#segment-breakdown}

| Nombre de la consulta | Descripción |
| -- | -- |
| Métricas de interacción de correo electrónico por segmento | Este informe muestra métricas de rendimiento de correo electrónico desglosadas por segmento a nivel de Campaign o Canvas. |
| Compras e ingresos por segmento | Este informe muestra métricas de compras e ingresos desglosadas por segmento para una Campaign o Canvas específico. |
| Mejores/peores mensajes en interacción de correo electrónico | Este informe muestra las campañas, Canvas o pasos en Canvas que tuvieron el mejor o peor rendimiento para una métrica de interacción de correo electrónico especificada. |
| Mejores/peores mensajes en compras | Este informe muestra las campañas, Canvas o pasos en Canvas que tuvieron el mejor o peor rendimiento para una métrica de compras o ingresos especificada. |
| Rendimiento push por segmento | Este informe muestra métricas push desglosadas por segmento. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Desglose por segmento" }