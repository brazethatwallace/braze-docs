---
nav_title: おすすめイベント
article_title: おすすめイベント
alias: /recommended_events/
page_order: 2
page_type: reference
description: "このリファレンス記事では、Braze が e コマースイベント向けに提供するおすすめイベントについて説明します。"
---

# おすすめイベント {#recommended-events}

> おすすめイベントは、最も一般的な e コマースのユースケースに対応しています。おすすめイベントを使用することで、構築済みのキャンバステンプレート、カスタマーライフサイクルに対応するレポートダッシュボードなどを活用できます。

例えば、ユーザーがカート内の製品を追加、削除、または更新した際にキャプチャするために、「cart_updated」や「update_to_cart」というカスタムイベントを使用しているかもしれません。おすすめイベントでは、Brazeがイベントテンプレートを提供し、このイベントの定義済みの名前と関連するプロパティが含まれます。

{% alert important %}
おすすめイベントは現在、早期アクセス段階です。この早期アクセスへの参加にご興味がある場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。<br><br>新しい [Shopify コネクター]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)を活用している場合、これらのおすすめイベントはインテグレーションを通じて自動的に利用可能になります。
{% endalert %}

## 仕組み {#how-it-works}

Brazeはすべてのおすすめイベントに特別なバリデーションを適用し、一部のおすすめイベントには特別な後処理アクションがあります。特定の業界向けおすすめイベントについては、CampaignsやCanvasesの新しいアクションベースのトリガーなど、Brazeが特別な処理をサポートする場合があります。

おすすめイベントは[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)と同様に機能します。おすすめイベントはCurrentsからエクスポートしたり、ブロックリストに追加したり、レポートで使用したりできます。また、[Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/)または[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用して、これらのイベントを追跡するためのデータをBrazeに送信することもできます。

### e コマース推奨イベント {#ecommerce-recommended-events}

[e コマース推奨イベント]({{site.baseurl}}/ecommerce_events/)は、おすすめイベントに基づいています。これらの e コマース推奨イベントは、製品の閲覧、カートの更新、チェックアウトプロセスの開始など、顧客が行ったアクションを追跡します。

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### e コマースCanvasテンプレート {#ecommerce-canvas-templates}

Braze Canvasの構築済みテンプレートを使用して重要な戦略を実装する方法についてのアイデアは、専用の [e コマースユースケース]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/)をご覧ください。

## よくある質問 {#frequently-asked-questions}

### おすすめイベントはカスタムイベントと同じですか？ {#are-recommended-events-the-same-as-custom-events}

いいえ。Brazeはおすすめイベントに対して明確なデータスキーマを定義します。これには、Brazeでバリデーションプロセスを経る必須およびオプションのイベントプロパティが含まれます。[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events/)は、アプリやWeb サイトでユーザーが行った特定のアクション、またはユーザーに関する更新であり、追跡したいものです。イベント名と追跡する内容をカスタマイズできます。

### おすすめイベントの名前をカスタマイズできますか？ {#can-i-customize-the-name-of-the-recommended-events}

いいえ。おすすめイベントには標準化されたイベント名とプロパティがあります。これらの標準化により、データ全体の一貫性を確保できます。

### 購入を記録するために購入イベントを引き続き使用できますか？ {#can-i-still-use-purchase-events-to-log-purchases}

e コマース推奨イベントのリリースに伴い、Brazeは将来的にレガシーの購入イベントを段階的に廃止する予定です。現在購入イベントを使用している場合は、廃止計画に関する事前通知を受け取ります。それまでの間、公式の廃止日まで購入イベントを引き続き使用できます。