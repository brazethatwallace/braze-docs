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
データウェアハウスストレージは、Currentsからストリーミングされるすべての情報の収集ソースを提供します。これらのパートナーは、ウェアハウス（フラットファイルストレージ）として機能するか、ビジネスインテリジェンスツールや機械学習アルゴリズムの活用、マーケティングパフォーマンスのインサイト取得などに利用できます。

* [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3)
* [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents)
* [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents)

Currentsとデータウェアハウスの組み合わせの力を確信しているからこそ、[私たち自身も活用しています]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)！

## 顧客データ {#customer-data}

これらの顧客データプラットフォームは、複数のソースから情報を収集してさまざまな場所にルーティングし、Brazeデータを最適な方法で活用できるようにします。

* [mParticle]({{site.baseurl}}/partners/mparticle_for_currents)
* [セグメント]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents)
* [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents)
* [トレジャーデータ]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/treasure_data_for_currents)
* [Rudderstack]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/rudderstack/rudderstack_for_currents)
* [Adobe]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/adobe/adobe_for_currents)
* [Amperity]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amperity#using-amperity-with-braze-currents)

## 行動分析 {#behavioral-analytics}

これらのパートナーは、プロダクト分析とビジネスインテリジェンスを専門としており、ユーザーのアクションに基づいてユーザーとのインタラクションを支援します。

* [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents)
* [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel)
* [Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/heap_cohort_import)

## データツール {#data-tools}

Currentsのイベントデータを、自身が所有・運用するHTTPエンドポイントに直接ストリーミングすることで、独自のカスタムインテグレーションを構築できます。

* [カスタムHTTPコネクター]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)