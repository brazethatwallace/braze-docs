---
nav_title: Noviembre
page_order: 1
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de noviembre de 2021."
---
# Noviembre de 2021 {#november-2021}

## Métrica de informe de la tasa de clics sobre aperturas {#click-to-open-rate-reporting-metric}
Braze ha añadido una nueva métrica de correo electrónico, la tasa de clics sobre aperturas, disponible en el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder/). Esta métrica representa el porcentaje de correos electrónicos abiertos en los que se ha hecho clic.

## Métrica de informe de aperturas de máquina {#machine-open-reporting-metric}

Una nueva métrica de correo electrónico, [Aperturas de máquina]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens), está disponible en las páginas de análisis de Canvas y Campaigns para los correos electrónicos. Esta métrica identifica las aperturas de correo electrónico que no son humanas (como las abiertas por los servidores de Apple), mostradas como un subconjunto del total de aperturas.

## Variable Liquid random_bucket_number {#randombucketnumber-liquid-variable}
Se ha añadido la variable `random_bucket_number` a la lista de [variables compatibles de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) para la personalización de mensajes.

## Directrices para las notificaciones push enriquecidas de iOS 15 {#ios-15-rich-push-notification-guidelines}
Se han añadido nuevas [directrices sobre notificaciones push de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/) a los documentos enriquecidos de iOS, incluida información sobre los estados de las notificaciones y un desglose de las variables de truncamiento de texto.

## IP en lista blanca en la UE para webhooks y contenido conectado {#ips-to-whitelist-in-eu-for-webhooks-and-connected-content}
Se han añadido IP adicionales a la lista blanca de la UE para webhooks y contenido conectado en nuestro artículo sobre [webhooks]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) y [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/). Estas nuevas IP incluyen `18.157.135.97`, `3.123.166.46`, `3.64.27.36`, `3.65.88.25`, `3.68.144.188` y `3.70.107.88`.

## Punto de conexión de exportación de compras {#export-purchases-endpoint}
Se añadió a Braze un nuevo [punto de conexión `/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/). Este punto de conexión devuelve listas paginadas de ID de productos.

## Nuevas asociaciones de Braze {#new-braze-partnerships}

### Adobe - Plataforma de datos de los clientes {#adobe-customer-data-platform}
La integración de Braze y [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) permite a las marcas conectar y mapear sus datos de Adobe (atributos personalizados y segmentos) con Braze en tiempo real. Las marcas pueden entonces actuar a partir de estos datos, entregando experiencias personalizadas y dirigidas a esos usuarios.

### BlueConic - Plataforma de datos de los clientes {#blueconic-customer-data-platform}
Con [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic), los usuarios de la empresa pueden unificar los datos en perfiles persistentes e individuales y sincronizarlos después en todos los sistemas y puntos de intervención con el cliente para apoyar una amplia gama de iniciativas centradas en el crecimiento, como la orquestación del ciclo de vida del cliente, el modelado y el análisis, los productos y experiencias digitales, la monetización basada en la audiencia y mucho más.

### Worthy - Contenido dinámico {#worthy-dynamic-content}
La integración de Braze y [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) te permite crear fácilmente experiencias ricas y personalizadas dentro de la aplicación utilizando el editor de contenido dinámico de arrastrar y soltar de Worthy y entregarlas a través de Braze.

### Judo - Contenido dinámico {#judo-dynamic-content}
La integración de [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) y Braze te permite sobrescribir componentes de tu campaña y sustituirlos por experiencias de Judo. Los datos de Braze pueden utilizarse para apoyar el contenido personalizado en una experiencia de Judo. Los eventos del usuario y los datos de la experiencia pueden retroalimentarse a Braze para la atribución y la segmentación.

### Line - Mensajería {#line-messaging}
La integración de [Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) y Braze te permite aprovechar los webhooks de Braze y las características avanzadas de segmentación, personalización y desencadenamiento para enviar mensajes a tus usuarios en Line a través de la [API de mensajería de Line](https://developers.line.biz/en/docs/messaging-api/overview/).

### RevenueCat - Pagos {#revenuecat-payments}
La integración de [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) y Braze te permite sincronizar automáticamente los eventos del ciclo de vida de compra y suscripción de tus clientes en todas las plataformas. Esto te permite crear campañas que reaccionen a la etapa del ciclo de vida de suscripción de tus clientes, como interactuar con los clientes que se dieron de baja durante su prueba gratuita o enviar recordatorios a los clientes con problemas de facturación.

### Punchh - Fidelización {#punchh-loyalty}
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) se ha asociado con Braze para sincronizar los datos de ambas plataformas con fines de regalo y fidelización. Los datos publicados en Braze estarán disponibles para la segmentación y pueden sincronizar los datos de usuario de nuevo en Punchh a través de plantillas de webhook configuradas en Braze.