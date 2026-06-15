# よくある質問 {#frequently-asked-questions}

> これらは、Brazeのバナーに関するよくある質問への回答です。より一般的な情報については、[バナーについて]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}/)を参照してください。

## バナーの更新はいつユーザーに表示されますか？ {#when-do-banner-updates-appear-for-users}

バナーはリフレッシュメソッドを呼び出すたびに最新のデータで更新されます&#8212;バナーキャンペーンを再送信したり更新したりする必要はありません。

## 1回のセッションで何件のプレースメントをリクエストできますか？ {#how-many-placements-can-i-request-in-a-session}

1回のリフレッシュリクエストで、最大10個のプレースメントをリクエストできます。リクエストごとに、Brazeはユーザーが対象となるバナーの中で最も優先度の高いものを返します。追加のリクエストはエラーを返します。

詳細については、[プレースメントリクエスト]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %})を参照してください。

## 同時にアクティブにできるバナーキャンペーンはいくつですか？ {#how-many-banner-campaigns-can-be-active-simultaneously}

各ワークスペースは最大200のアクティブなバナーキャンペーンをサポートできます。この制限に達した場合、新しいキャンペーンを作成する前に、既存のキャンペーンを[アーカイブまたは無効化]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status)する必要があります。

## 同じプレースメントを共有するキャンペーンでは、どのバナーが最初に表示されますか？ {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

ユーザーが同じプレースメントを共有する複数のバナーキャンペーンの対象となる場合、最も優先度の高いバナーが表示されます。詳細については、[バナーの優先度]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %})を参照してください。

## 既存のContent Cardsフィードでバナーを使用できますか？ {#can-i-use-banners-in-my-existing-content-card-feed}

バナーはContent Cardsとは異なるため、同じフィード内でバナーとContent Cardsを併用することはできません。既存のContent CardsフィードをバナーにContent Cardsフィードをバナーに置き換えるには、[アプリやWebサイト内にプレースメントを作成]({{site.baseurl}}/developer_guide/banners/placements/)する必要があります。

## バナーに動画を含めることはできますか？ {#can-banners-include-video}

標準のバナーコンポーザーは画像、テキスト、ボタンをサポートしています。バナーに動画を含めるには、**カスタムコード**ブロックを使用して、アプリやWebサイトで動画や埋め込みプレーヤーをレンダリングできます。

## ユーザーのアクションに基づいてバナーをトリガーできますか？ {#can-i-trigger-a-banner-based-on-user-actions}

バナーは[アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)をサポートしていませんが、セグメンテーションと優先度を活用して、ユーザーの過去のアクションに基づいてターゲティングできます。

例えば、`purchase` イベントを完了したユーザーにのみ特別なバナーを表示するには：
1. **ターゲティング：** キャンペーンで、カスタムイベント `purchase` を少なくとも1回実行したユーザーのSegmentをターゲットに設定します。
2. **優先度：** すべてのユーザー向けの一般的なバナーと、購入者向けの特定のバナーが同じプレースメントをターゲットにしている場合、特定のバナーの優先度を**高**に、一般的なバナーを**中**または**低**に設定します。

ユーザーが新しいセッションを開始するか、アクション実行後にバナーをリフレッシュすると、Brazeは適格性を評価します。「購入」Segmentに一致する場合、優先度の高いバナーが表示されます。


## ユーザーはバナーを閉じることができますか？ {#can-users-dismiss-a-banner}

はい。バナーコンポーザーで閉じる動作を有効にすることで、ユーザーが手動でバナーを閉じることを許可できます。閉じる動作の有効化と閉じるボタンのカスタマイズについては、[閉じる動作の設定]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior)を参照してください。

ユーザーが手動でバナーを閉じることができるのは、閉じる動作が有効になっている場合のみです。閉じる動作が有効でない場合は、ユーザーSegmentの適格性を管理することでバナーの表示をコントロールできます。ユーザーがバナーキャンペーンのターゲティング条件を満たさなくなると、次のセッションではそのバナーが表示されなくなります。

ユーザーがバナーを閉じると、デフォルトではそのキャンペーンの対象外となります。閉じたユーザーに再度バナーを表示するには、キャンペーンの**配信コントロール**ステップで[再適格性を設定]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#re-eligibility)してください。Canvasのバナーステップでは、再適格性の制御にCanvasの再エントリ設定が使用されます。

{% alert important %}
[バナーの閉じる操作]({{site.baseurl}}/developer_guide/banners/placements/#log-dismissals)は現在、早期アクセス段階です。早期アクセスへの参加にご興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

例えば、ユーザーが購入するまでプロモーションバナーを表示する場合、`purchase_completed` などのイベントを記録することで、そのユーザーをターゲットSegmentから除外し、その後のセッションでバナーを非表示にできます。

## Braze APIを使ってバナーキャンペーンの分析データをエクスポートできますか？ {#can-i-export-banners-campaign-analytics-using-the-braze-api}

はい。[`/campaigns/data_series` エンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)を使用して、バナーキャンペーンの表示回数、クリック数、コンバージョン数に関するデータを取得できます。

## ユーザーはいつセグメンテーションされますか？ {#when-are-users-segmented}

ユーザーはセッションの開始時にセグメンテーションされます。キャンペーンのターゲットSegmentsがカスタム属性、カスタムイベント、その他のターゲティング属性に依存する場合、それらはセッション開始時点でユーザーに存在している必要があります。

## レイテンシーを最小限に抑えるために、バナーをどのように構成すればよいですか？ {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

バナーのメッセージがシンプルであるほど、レンダリングが速くなります。ユースケースに対して想定されるレイテンシーでバナーキャンペーンをテストすることをお勧めします。例えば、`catalog_items` などのLiquid属性は必ずテストしてください。

## すべてのLiquidタグはサポートされていますか？ {#are-all-liquid-tags-supported}

いいえ。ただし、ほとんどのLiquidタグはバナーメッセージでサポートされています。例外として、[`:rerender` タグ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)を使用して再レンダリングされる `catalog_items` はサポートされていません。

## クリックイベントをキャプチャできますか？ {#can-i-capture-click-events}

はい。クリックイベントのキャプチャ方法は、バナーのレンダリング方法によって異なります。

- **標準エディターコンポーネント：** バナーが標準のエディターコンポーネント（画像、ボタン、テキスト）を使用している場合、SDKの挿入メソッドを使用するとクリックは自動的にトラッキングされます。
- **カスタムコードブロック：** カスタムコードエディターブロック内の要素のクリックをトラッキングしたい場合、カスタムHTML内から `brazeBridge.logClick()` を呼び出してクリックをトラッキングする必要があります。これは、SDKメソッドを使用してバナーを挿入およびレンダリングする場合にも適用されます。完全なリファレンスについては、[バナー用のカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge)を参照してください。
- **カスタムUI（ヘッドレス）：** バナーのHTMLをレンダリングせずに、バナーのカスタムプロパティを使用して完全にカスタムのUIを構築する場合は、アプリケーションコードからバナーオブジェクトの `logClick()` を呼び出してください。

詳細については、[クリックの記録]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks)を参照してください。