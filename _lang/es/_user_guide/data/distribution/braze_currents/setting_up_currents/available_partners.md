---
nav_title: Socios disponibles
article_title: Socios de Currents disponibles
page_order: 1
page_type: reference
description: "Este artículo de referencia describe los partners de datos que puedes utilizar para integrar con Braze Currents y sus casos de uso."
tool: Currents
---

# Socios disponibles {#available-partners}

> Esta página enumera los partners de datos que puedes integrar con Braze Currents y describe sus casos de uso.

{% alert note %}
Las convenciones de nomenclatura para los eventos que fluyen de Braze hacia un partner pueden no coincidir con las de otros partners. Por ejemplo, el evento de apertura de correo electrónico de Currents en Segment es `Email Opened`, mientras que en Mixpanel es `Email Open`.
{% endalert %}

## Almacenamiento en almacén de datos {#data-warehouse-storage}
El almacenamiento en almacén de datos ofrece una fuente de recopilación para toda la información transmitida desde Currents. Estos partners pueden actuar como almacenes (para almacenamiento de archivos planos) o utilizarse para potenciar herramientas de inteligencia empresarial y algoritmos de aprendizaje automático, obtener información sobre el rendimiento del marketing, y mucho más.

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents)
* [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)

Estamos tan seguros del poder de Currents y los almacenes de datos juntos que [lo usamos nosotros mismos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents).

## Datos de clientes {#customer-data}

Estas plataformas de datos de los clientes recopilan y dirigen información de múltiples fuentes a una variedad de otras ubicaciones para ayudarte a utilizar los datos de Braze de la mejor manera posible.

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents)
* [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents)
* [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents)
* [Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents)
* [Amperity]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amperity#using-amperity-with-braze-currents)

## Análisis del comportamiento {#behavioral-analytics}

Estos partners se especializan en análisis de productos e inteligencia empresarial, y pueden ayudarte a interactuar con tus usuarios en función de sus acciones.

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)
* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel)
* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import)

## Herramientas de datos {#data-tools}

Crea tu propia integración personalizada transmitiendo datos de eventos de Currents directamente a un endpoint HTTP que poseas y operes.

* [Conector HTTP personalizado]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)