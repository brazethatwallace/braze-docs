---
nav_title: Partenaires disponibles
article_title: Partenaires Currents disponibles
page_order: 1
page_type: reference
description: "Cet article de référence décrit les partenaires de données que vous pouvez utiliser pour intégrer à Braze Currents, ainsi que leurs cas d'usage."
tool: Currents
---

# Partenaires disponibles {#available-partners}

> Cette page répertorie les partenaires de données que vous pouvez intégrer à Braze Currents et présente leurs cas d'usage.

{% alert note %}
Les conventions de nommage des événements transmis par Braze pour un partenaire donné peuvent différer d'un partenaire à l'autre. Par exemple, l'événement d'ouverture d'e-mail Currents dans Segment est `Email Opened`, tandis que dans Mixpanel, il s'agit de `Email Open`.
{% endalert %}

## Stockage en entrepôt de données {#data-warehouse-storage}
Le stockage en entrepôt de données offre une source de collecte pour toutes les informations diffusées par Currents. Ces partenaires peuvent servir d'entrepôts (pour le stockage de fichiers plats) ou être utilisés pour alimenter des outils d'aide à la décision et des algorithmes de machine learning, obtenir des informations sur les performances marketing, et bien plus encore.

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents)
* [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)

Nous sommes tellement convaincus de la puissance de Currents associé aux entrepôts de données que [nous l'utilisons nous-mêmes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents) !

## Données client {#customer-data}

Ces plateformes de données client collectent et acheminent les informations provenant de sources multiples vers divers emplacements, afin de vous permettre d'exploiter les données de Braze de la manière la plus efficace possible.

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents)
* [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents)
* [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents)
* [Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents)
* [Amperity]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amperity#using-amperity-with-braze-currents)

## Analyse comportementale {#behavioral-analytics}

Ces partenaires sont spécialisés dans l'analyse produit et l'aide à la décision. Ils peuvent vous aider à interagir avec vos utilisateurs en fonction de leurs actions.

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)
* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel)
* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import)

## Outils de données {#data-tools}

Créez votre propre intégration personnalisée en diffusant les données d'événements Currents directement vers un endpoint HTTP que vous possédez et exploitez.

* [Custom HTTP Connector]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)