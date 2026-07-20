---
nav_title: 利用可能なパートナー
article_title: 利用可能なCurrentsパートナー
page_order: 1
page_type: reference
description: "このリファレンス記事では、Braze Currentsとの連携に使用できるデータパートナーとそのユースケースについて概説します。"
tool: Currents

---

# 利用可能なパートナー {#available-partners}

> このページでは、Braze Currentsと連携できるデータパートナーの一覧と、そのユースケースの概要を説明します。

{% alert note %}
Brazeから配信されるイベントの命名規則は、パートナーによって異なる場合があります。たとえば、セグメントでのCurrentsメール開封イベントは `Email Opened` ですが、Mixpanelでは `Email Open` になります。
{% endalert %}

## データウェアハウスストレージ {#data-warehouse-storage}
データウェアハウスストレージは、Currentsからストリーミングされるすべての情報の収集ソースを提供します。これらのパートナーは、ウェアハウス（フラットファイルストレージ用）として機能するか、ビジネスインテリジェンスツールや機械学習アルゴリズムの活用、マーケティングパフォーマンスに関するインサイトの取得などに活用できます。

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents)
* [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)

Brazeでは、Currentsとデータウェアハウスの組み合わせの力を確信しており、[社内でも活用しています]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)。

## 顧客データ {#customer-data}

ここに示す顧客データプラットフォームは、複数のソースから情報を収集してさまざまな場所に転送するため、Brazeのデータを最大限に活用できます。

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents)
* [セグメント]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents)
* [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents#tealium-for-currents)
* [トレジャーデータ]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents)
* [RudderStack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents)
* [Amperity]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity#using-amperity-with-braze-currents)

## 行動分析 {#behavioral-analytics}

これらのパートナーは、製品分析とビジネスインテリジェンスに特化しており、ユーザーのアクションに基づいてユーザーとのインタラクションを行うのに役立ちます。

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)
* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel)
* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import)

## データツール {#data-tools}

Currentsのイベントデータを、自社で所有・運用するHTTPエンドポイントに直接ストリーミングして、独自のカスタム連携を構築できます。

* [カスタムHTTPコネクター]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)