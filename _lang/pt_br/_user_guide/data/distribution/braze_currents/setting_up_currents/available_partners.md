---
nav_title: Parceiros disponíveis
article_title: Parceiros Currents disponíveis
page_order: 1
page_type: reference
description: "Este artigo de referência descreve os parceiros de dados que você pode usar para se integrar ao Braze Currents e seus casos de uso."
tool: Currents
---

# Parceiros disponíveis {#available-partners}

> Esta página lista os parceiros de dados com os quais você pode se integrar ao Braze Currents e descreve seus casos de uso.

{% alert note %}
As convenções de nomenclatura para eventos que fluem de um parceiro a partir da Braze podem não corresponder às de outros parceiros. Por exemplo, o evento de abertura de e-mail do Currents no Segment or segmento é `Email Opened`, enquanto no Mixpanel é `Email Open`.
{% endalert %}

## Armazenamento em data warehouse {#data-warehouse-storage}
O armazenamento em data warehouse oferece uma fonte de coleta para todas as informações transmitidas pelo Currents. Esses parceiros podem atuar como warehouses (para armazenamento de arquivos simples) ou ser usados para alimentar ferramentas de business intelligence e algoritmos de machine learning, obter insights sobre o desempenho de marketing e muito mais.

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents)
* [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)

Nós confiamos tanto no poder do Currents combinado com data warehouses que [nós mesmos usamos essa solução]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)!

## Dados de cliente {#customer-data}

Essas plataformas de dados do cliente coletam e direcionam informações de várias fontes para diversos outros destinos, permitindo que você utilize os dados da Braze da melhor forma possível.

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents)
* [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents)
* [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents)
* [Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents)
* [Amperity]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amperity#using-amperity-with-braze-currents)

## Análise de dados comportamentais {#behavioral-analytics}

Esses parceiros são especializados em análise de dados de produtos e business intelligence e podem ajudar você a interagir com seus usuários com base nas ações deles.

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)
* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel)
* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import)

## Ferramentas de dados {#data-tools}

Crie sua própria integração personalizada transmitindo dados de eventos do Currents diretamente para um endpoint HTTP que você possui e opera.

* [Conector HTTP personalizado]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)