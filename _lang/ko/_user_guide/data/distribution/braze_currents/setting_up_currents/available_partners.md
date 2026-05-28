---
nav_title: 사용 가능한 파트너
article_title: 사용 가능한 Currents 파트너
page_order: 1
page_type: reference
description: "이 참조 문서에서는 Braze 커런츠와 통합하는 데 사용할 수 있는 데이터 파트너와 그 활용 사례를 간략하게 설명합니다."
tool: Currents

---

# 사용 가능한 파트너 {#available-partners}

> 이 페이지에는 Braze 커런츠와 통합할 수 있는 데이터 파트너가 나열되어 있으며, 활용 사례에 대한 개요가 나와 있습니다.

{% alert note %}
Braze에서 한 파트너로 전달되는 이벤트의 명명 규칙이 다른 파트너와 일치하지 않을 수 있습니다. 예를 들어, Segment의 Currents 이메일 열기 이벤트는 `Email Opened`이며, Mixpanel에서는 `Email Open`입니다.
{% endalert %}

## 데이터 웨어하우스 스토리지 {#data-warehouse-storage}
데이터 웨어하우스 스토리지는 Currents에서 스트리밍되는 모든 정보에 대한 수집 소스를 제공합니다. 이러한 파트너는 플랫 파일 스토리지를 위한 웨어하우스 역할을 하거나 비즈니스 인텔리전스 도구 및 머신 러닝 알고리즘을 강화하고 마케팅 성과에 대한 인사이트를 얻는 데 사용할 수 있습니다.

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/)
* [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)

저희는 Currents와 데이터 웨어하우스를 함께 사용하는 것의 효과를 확신하며, [직접 사용하고 있습니다]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents/)!

## 고객 데이터 {#customer-data}

이러한 고객 데이터 플랫폼은 여러 소스에서 정보를 수집하고 다양한 위치로 라우팅하여 Braze 데이터를 최상의 방법으로 활용할 수 있도록 지원합니다.

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents/)
* [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents/#tealium-for-currents)
* [Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents/)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents/)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents/)
* [Amperity]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/#using-amperity-with-braze-currents)

## 행동 분석 {#behavioral-analytics}

이러한 파트너는 제품 분석 및 비즈니스 인텔리전스를 전문으로 하며, 사용자의 행동을 기반으로 사용자와 상호작용하는 데 도움을 줄 수 있습니다.

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/)
* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/)
* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import/)

## 데이터 도구 {#data-tools}

Currents 이벤트 데이터를 직접 소유하고 운영하는 HTTP 엔드포인트로 스트리밍하여 커스텀 통합을 구축할 수 있습니다.

* [커스텀 HTTP 커넥터]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector/)