---
nav_title: ロケーションターゲティング
article_title: ロケーションターゲティング
page_order: 7
page_type: tutorial
tool:
- Segments
- Location
description: "このハウツー記事では、ロケーションターゲティングの設定方法を説明し、ロケーションによるユーザーのセグメンテーションを可能にします。"

---

# ロケーションターゲティング {#location-targeting}

> この記事では、ロケーションターゲティングの設定方法を説明します。ユーザーの最新のロケーションに基づいてセグメンテーションを行うことができます。ロケーションベースのCampaignsや戦略を検討している場合に最適です。

## ステップ 1: Segmentを作成する {#step-1-create-your-segment}

**オーディエンス**の下にある**Segments**ページに移動して、現在のユーザーSegmentsをすべて表示します。このページでは、新しいSegmentを作成して名前を付けることができます。開始するには、**セグメントを作成**を選択してSegmentに名前を付けます。

![Segmentを作成するモーダル。]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## ステップ 2: ロケーションをカスタマイズする {#step-2-customize-your-location}

Segmentを作成したら、**最新のロケーション**フィルターを追加して、ユーザーがアプリを最後に使用した場所でターゲティングします。標準的な円形領域またはカスタマイズ可能な多角形領域の範囲内または範囲外のユーザーをハイライトするオプションがあります。

![円の範囲内の最新のロケーションのフィルター。]({% image_buster /assets/img_archive/filter_recent_location.png %})

{% tabs %}
{% tab 円形 %}

### 円形領域 {#circular-regions}

円形領域の場合、Originを移動し、セグメンテーションのロケーション半径を調整できます。

![ニュージャージーとニューヨークの間の都市の円形アウトライン。]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab 多角形 %}

### 多角形領域 {#polygonal-regions}

多角形領域の場合、Segmentに含めたいエリアをより具体的に指定できます。

![選択された多角形領域としてのニューヨーク州のアウトライン。]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## ビーコンとジオフェンスのパートナーシップサポート {#partnership-support-for-beacon-and-geofence}

既存のビーコンまたはジオフェンスサポートとBrazeのターゲティングおよびメッセージング機能を組み合わせることで、ユーザーの物理的なアクションに関するより多くの情報を取得し、それに応じてメッセージを送信できます。以下のパートナーと連携して位置情報の追跡を活用できます。

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)