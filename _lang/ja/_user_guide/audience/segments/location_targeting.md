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

> この記事では、ロケーションターゲティングの設定方法を説明します。ユーザーの最新のロケーションに基づいてセグメンテーションを行うことができます。

## ステップ1：セグメントを作成する {#step-1-create-your-segment}

**オーディエンス**の下にある**セグメント**ページに移動して、現在のユーザーセグメントをすべて表示します。このページでは、新しいセグメントを作成して名前を付けることができます。開始するには、**セグメントを作成**を選択し、セグメントに名前を付けます。

![セグメントを作成するモーダル。]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## ステップ2: 位置情報をカスタマイズする {#step-2-customize-your-location}

セグメントを作成したら、`Most Recent Location` フィルターを追加して、ユーザーが最後にアプリを使用した場所でハイライトします。標準的な円形の範囲内または範囲外、もしくはカスタマイズ可能な多角形の範囲内または範囲外のユーザーをハイライトするオプションがあります。

![円形範囲内の最新の位置情報によるフィルター。]({% image_buster /assets/img_archive/filter_recent_location.png %})

### 位置情報のないユーザー {#users-without-location-data}

位置情報のないユーザー（以前に位置情報が記録され、その後クリアされたユーザーを含む）は、`most recent location outside of circle` および `most recent location outside of polygon` のフィルターに一致します。位置情報のないユーザーを除外するには、`Most Recent Location` フィルターと `Location Available` フィルターを組み合わせてください。

{% tabs %}
{% tab 円形 %}

### 円形の範囲 {#circular-regions}

円形の範囲では、Originを移動し、セグメンテーションの位置情報の半径を調整できます。

![ニュージャージーとニューヨークの間の都市の円形アウトライン。]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab 多角形 %}

### 多角形の範囲 {#polygonal-regions}

多角形の範囲では、セグメントに含めたいエリアをより具体的に指定できます。

![選択された多角形の範囲としてのニューヨーク州のアウトライン。]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## ビーコンとジオフェンスのパートナーシップサポート {#partnership-support-for-beacon-and-geofence}

既存のビーコンやジオフェンスのサポートと、Brazeのターゲティングおよびメッセージング機能を組み合わせることで、ユーザーの物理的なアクションに関するより多くの情報を取得し、それに応じてメッセージを送信できます。以下のパートナーを活用して位置情報の追跡を行うことができます。

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)