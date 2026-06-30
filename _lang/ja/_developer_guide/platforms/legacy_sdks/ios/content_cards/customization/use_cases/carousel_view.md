---
nav_title: カルーセルビュー
article_title: iOS 向けコンテンツカードカルーセルビュー
platform: iOS
page_order: 5
description: "この記事では、iOS アプリケーションを対象にコンテンツカードカルーセルビューのユースケースを実装する方法について説明します。"
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# ユースケース: カルーセルビュー {#use-case-carousel-view}

![記事内でContent Cardsがカルーセル表示されるニュースアプリのサンプル。]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

このセクションでは、ユーザーが水平方向にスワイプして追加の注目カードを表示できるマルチカードカルーセルフィードの実装方法を説明します。カルーセルビューを統合するには、完全にカスタマイズされたContent Cardsの実装を使用する必要があります。これは[クロール、ウォーク、ランアプローチ]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize#customization-approaches)の「ラン」フェーズに該当します。

このアプローチでは、Brazeのビューとデフォルトロジックを使用せず、代わりにBrazeモデルからのデータが取り込まれた独自のビューを使用して、完全にカスタマイズされた方法でContent Cardsを表示します。

開発労力のレベルという点では、基本的な実装とカルーセル実装の主な違いは次のとおりです。

- 独自のビューを構築する
- Content Cardsの分析を記録する
- カルーセルにどのカードを何枚表示するかを指示する追加のクライアント側ロジックを導入する

## 実装 {#implementation}

### ステップ1: カスタムビューコントローラーを作成する {#step-1-create-a-custom-view-controller}

Content Cardsのカルーセルを作成するには、独自のカスタムビューコントローラー（`UICollectionViewController` など）を作成して、[データ更新を配信登録]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#getting-the-data)します。デフォルトの `ABKContentCardTableViewController` はデフォルトのContent Cardsタイプしか扱えないため、拡張したりサブクラス化したりすることはできません。

### ステップ2: 分析を実装する {#step-2-implement-analytics}

完全にカスタマイズされたビューコントローラーを作成する場合、Content Cardsのインプレッション数、クリック数、却下数は自動的に記録されません。インプレッション数、却下イベント、クリック数がBrazeダッシュボードの分析に適切に記録されるようにするには、それぞれの分析メソッドを実装する必要があります。

分析メソッドについては、[カードメソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration#card-methods)を参照してください。

{% alert note %}
同じページには、汎用Content Cardsモデルクラスから継承されたさまざまなプロパティの詳細も記載されています。この情報は、ビューの実装時に役立つ可能性があります。
{% endalert %}

### ステップ3: Content Cardsオブザーバーを作成する {#step-3-create-a-content-card-observer}

Content Cardsの到着を処理する[Content Cardsオブザーバー]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds#step-2-set-up-a-content-card-listener)を作成し、一度に特定の数のカードをカルーセルに表示する条件付きロジックを実装します。デフォルトでは、Content Cardsは作成日順（新しい順）にソートされ、対象となるすべてのカードがユーザーに表示されます。

ただし、追加の表示ロジックを適用して、さまざまな方法でソートすることもできます。たとえば、配列から最初の5つのContent Cardsオブジェクトを選択したり、キーと値のペア（データモデルの `extras` プロパティ）を導入して条件付きロジックを構築したりできます。

セカンダリContent Cardsフィードとしてカルーセルを実装する場合は、[複数のContent Cardsフィードを使用する]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/multiple_feeds)を参照して、キーと値のペアに基づいてカードが正しいフィードにソートされるようにしてください。

{% alert important %}
マーケターがBrazeダッシュボードに入力するキーと値のペアは、開発者がアプリのロジックに組み込むキーと値のペアと正確に一致しなければならないため、マーケティングチームと開発チームが、どのキーと値のペアを使用するか（たとえば `feed_type = brand_homepage`）について確実に調整することが重要です。
{% endalert %}

Content Cardsクラス、メソッド、属性に関するiOS固有の開発者向けドキュメントについては、iOS [`ABKContentCard` クラスリファレンス](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)を参照してください。

## 考慮事項 {#considerations}

- 完全にカスタマイズされたビューを使用すると、`ABKContentCardsController` で使用されるメソッドを拡張したりサブクラス化したりすることはできなくなります。その代わりに、データモデルのメソッドとプロパティを自分で統合する必要があります。
- カルーセルビューのロジックと実装は、BrazeのContent Cardsのデフォルトタイプではないため、ユースケースを実現するためのロジックは開発チームが提供し、サポートする必要があります。
- カルーセルに一度に特定の数のカードを表示するには、クライアント側ロジックを実装する必要があります。