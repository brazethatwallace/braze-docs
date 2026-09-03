---
nav_title: カルーセルビュー
article_title: iOS 向けContent Cardsカルーセルビュー
platform: iOS
page_order: 5
description: "この記事では、iOS アプリケーションを対象にContent Cardsカルーセルビューのユースケースを実装する方法について説明します。"
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# ユースケース: カルーセルビュー {#use-case-carousel-view}

![記事内でContent Cardsがカルーセル表示されるニュースアプリのサンプル。]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

このセクションでは、ユーザーが水平方向にスワイプして追加の注目カードを表示できるマルチカードカルーセルフィードの実装方法を説明します。カルーセルビューを統合するには、完全にカスタマイズされたContent Cardsの実装を使用する必要があります。これは[クロール、ウォーク、ランアプローチ]({{site.baseurl}}/developer_guide/getting_started/customization_overview)の「ラン」フェーズに該当します。

このアプローチでは、Brazeのビューとデフォルトロジックを使用せず、代わりにBrazeモデルからのデータが取り込まれた独自のビューを使用して、完全にカスタマイズされた方法でContent Cardsを表示します。

開発労力のレベルという点では、基本的な実装とカルーセル実装の主な違いは次のとおりです。

- 独自のビューを構築する
- Content Cardsの分析を記録する
- カルーセルにどのカードを何枚表示するかを指示する追加のクライアント側ロジックを導入する

## 実装 {#implementation}

### ステップ1:カスタムビューコントローラーを作成する {#step-1-create-a-custom-view-controller}

Content Cardsカルーセルを作成するには、独自のカスタムビューコントローラー（`UICollectionViewController`など）を作成し、[データ更新をサブスクライブ]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#getting-the-data)します。デフォルトの`ABKContentCardTableViewController`は、デフォルトのContent Cardsタイプのみを処理できるため、拡張やサブクラス化はできません。

### ステップ2:分析を実装する {#step-2-implement-analytics}

完全にカスタムのビューコントローラーを作成する場合、Content Cardsのインプレッション、クリック、および却下は自動的に記録されません。インプレッション、却下イベント、およびクリックがBrazeダッシュボードの分析に適切に記録されるように、それぞれの分析メソッドを実装する必要があります。

分析メソッドの詳細については、[カードメソッド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/integration#card-methods)を参照してください。

{% alert note %}
同じページには、汎用のContent Cardsモデルクラスから継承されるさまざまなプロパティも記載されており、ビューの実装時に役立つ場合があります。
{% endalert %}

### ステップ3:Content Cardsオブザーバーを作成する {#step-3-create-a-content-card-observer}

Content Cardsの到着を処理し、カルーセルに一度に表示するカードの数を制御する条件付きロジックを実装する[Content Cardsオブザーバー]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener)を作成します。デフォルトでは、Content Cardsは作成日順（新しいものが先）にソートされ、ユーザーは対象となるすべてのカードを表示できます。

とはいえ、さまざまな方法で順序付けや追加の表示ロジックを適用できます。たとえば、配列から最初の5つのContent Cardsオブジェクトを選択したり、キーと値のペア（データモデルの`extras`プロパティ）を導入して条件付きロジックを構築したりできます。

カルーセルをセカンダリContent Cardsフィードとして実装する場合は、キーと値のペアに基づいてカードを正しいフィードにソートするために、[複数のContent Cardsフィードの使用]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds)を参照してください。

{% alert important %}
マーケティングチームと開発者チームが、使用するキーと値のペア（例：`feed_type = brand_homepage`）について事前に調整することが重要です。マーケターがBrazeダッシュボードに入力するキーと値のペアは、開発者がアプリロジックに組み込むキーと値のペアと正確に一致する必要があります。
{% endalert %}

Content Cardsクラス、メソッド、および属性に関するiOS固有の開発者ドキュメントについては、iOS [`ABKContentCard`クラスリファレンス](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)を参照してください。

## 考慮事項 {#considerations}

- 完全にカスタムのビューを使用する場合、`ABKContentCardsController`で使用されるメソッドを拡張またはサブクラス化することはできません。代わりに、データモデルのメソッドとプロパティを自分で統合する必要があります。
- カルーセルビューのロジックと実装は、BrazeのContent Cardsのデフォルトタイプではないため、ユースケースを実現するためのロジックは開発チームが提供しサポートする必要があります。
- カルーセルに一度に表示するカードの数を指定するためのクライアントサイドロジックを実装する必要があります。