---
nav_title: おすすめイベント
article_title: おすすめイベント
alias: /recommended_events/
page_order: 2
page_type: reference
description: "このリファレンス記事では、Braze が e コマースイベント向けに提供するおすすめイベントについて説明します。"
---

# おすすめイベント

> おすすめイベントは、最も一般的な e コマースのユースケースに対応しています。おすすめイベントを使用することで、構築済みのキャンバステンプレート、カスタマーライフサイクルに対応するレポートダッシュボードなどを活用できます。

例えば、ユーザーがカート内の製品を追加、削除、または更新した際にキャプチャするために、「cart_updated」や「update_to_cart」というカスタムイベントを使用しているかもしれません。おすすめイベントでは、Braze がイベントテンプレートを提供し、このイベントの定義済みの名前と関連するプロパティが含まれます。

{% alert important %}
おすすめイベントは現在、早期アクセス段階です。この早期アクセスへの参加に興味がある場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。<br><br>新しい [Shopify コネクター]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)を活用している場合、これらのおすすめイベントは統合を通じて自動的に利用可能になります。
{% endalert %}

## 仕組み

Braze はすべてのおすすめイベントに特別なバリデーションを適用し、一部のおすすめイベントには特別な後処理アクションがあります。特定の業界向けおすすめイベントについては、キャンペーンやキャンバスの新しいアクションベースのトリガーなど、Braze が特別な処理をサポートする場合があります。

おすすめイベントは[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)と同様に機能します。おすすめイベントは Currents からエクスポートしたり、ブロックリストに追加したり、レポートで使用したりできます。また、[Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) または [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、これらのイベントを追跡するためのデータを Braze に送信することもできます。

### e コマースおすすめイベント

[e コマースおすすめイベント]({{site.baseurl}}/ecommerce_events/)は、おすすめイベントに基づいています。これらの e コマースおすすめイベントは、製品の閲覧、カートの更新、チェックアウトプロセスの開始など、顧客が行ったアクションを追跡します。

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### e コマースキャンバステンプレート

Braze キャンバスの構築済みテンプレートを使用して重要な戦略を実装する方法についてのアイデアは、専用の [e コマースユースケース]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/)をご覧ください。

## よくある質問

### おすすめイベントはカスタムイベントと同じですか？

いいえ。Braze はおすすめイベントに対して明確なデータスキーマを定義します。これには、Braze でバリデーションプロセスを経る必須およびオプションのイベントプロパティが含まれます。[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)は、アプリや Web サイトでユーザーが行った特定のアクション、またはユーザーに関する更新であり、追跡したいものです。イベント名と追跡する内容をカスタマイズできます。

### おすすめイベントの名前をカスタマイズできますか？

いいえ。おすすめイベントには標準化されたイベント名とプロパティがあります。これらの標準化により、データ全体の一貫性を確保できます。

### 購入を記録するために購入イベントを引き続き使用できますか？

e コマースおすすめイベントのリリースに伴い、Braze は将来的にレガシーの購入イベントを段階的に廃止する予定です。現在購入イベントを使用している場合は、廃止計画に関する事前通知を受け取ります。それまでの間、公式の廃止日まで購入イベントを引き続き使用できます。