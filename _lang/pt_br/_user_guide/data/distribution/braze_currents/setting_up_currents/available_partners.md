---
nav_title: Parceiros disponíveis
article_title: Parceiros Currents disponíveis
page_order: 1
page_type: reference
description: "Este artigo de referência descreve os parceiros de dados que você pode usar para se integrar ao Braze Currents e seus casos de uso."
tool: Currents

---

# Parceiros disponíveis

> Esta página lista os parceiros de dados com os quais você pode se integrar ao Braze Currents e descreve seus casos de uso.

{% alert note %}
As convenções de nomes para eventos que fluem para um parceiro do Braze Currents podem não corresponder a outros parceiros. Por exemplo, o evento de abertura de e-mail Currents no Segment é `Email Opened`, enquanto no Mixpanel é `Email Open`.
{% endalert %}

## Armazenamento de data warehouse
O armazenamento de data warehouse oferece uma fonte de coleta para todas as informações enviadas pelo Currents. Esses parceiros podem atuar como armazéns (para armazenamento de arquivos simples) ou ser usados para alimentar ferramentas de business intelligence, algoritmos de machine learning, obter insights sobre o desempenho do marketing e muito mais.

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
* [Armazenamento de Blob do Microsoft Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

Estamos tão confiantes no poder do Currents e dos data warehouses juntos que [nós mesmos os usamos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents/)!

## Dados de cliente

Essas plataformas de dados do cliente coletam e direcionam informações de múltiplas fontes para diversos outros destinos, permitindo que você utilize os dados da Braze da melhor forma possível.

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents/)
* [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents/#tealium-for-currents)
* [Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents/)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents/)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents/)
* [Amperity]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/#using-amperity-with-braze-currents)

## Análise de dados comportamentais

Esses parceiros são especializados em análise de dados de produto e business intelligence, e podem ajudar você a interagir com seus usuários com base nas ações deles.

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/)
* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)
* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import/)