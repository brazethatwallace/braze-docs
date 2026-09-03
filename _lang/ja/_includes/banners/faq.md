# よくある質問 {#frequently-asked-questions}

> これらは、Brazeのバナーに関するよくある質問への回答です。より一般的な情報については、[バナーについて]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %})を参照してください。

## ユーザーにバナーの更新が表示されるのはいつですか？ {#when-do-banner-updates-appear-for-users}

バナーは、更新メソッドを呼び出すたびに最新のデータで更新されます。バナーキャンペーンを再送信したり更新したりする必要はありません。

## 1回のセッションでリクエストできるプレースメントの数はいくつですか？ {#how-many-placements-can-i-request-in-a-session}

1回のリフレッシュリクエストで、最大10個のプレースメントをリクエストできます。リクエストごとに、Brazeはユーザーが対象となる最も優先度の高いバナーを返します。追加のリクエストはエラーを返します。

詳細については、[プレースメントリクエスト]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %})を参照してください。

## 同時にアクティブにできるバナーキャンペーンの数はいくつですか？ {#how-many-banner-campaigns-can-be-active-simultaneously}

各ワークスペースでは、最大200件のアクティブなバナーキャンペーンをサポートできます。この制限に達した場合、新しいキャンペーンを作成する前に、既存のキャンペーンを[アーカイブまたは非アクティブ化]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses#changing-the-status)する必要があります。

## 同じプレースメントを共有するキャンペーンでは、どのバナーが最初に表示されますか？ {#for-campaigns-sharing-a-placement-which-banner-is-displayed-first}

ユーザーが同じプレースメントを共有する複数のバナーキャンペーンの対象となる場合、最も優先度の高いバナーが表示されます。詳細については、[バナーの優先順位]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %})を参照してください。

## 既存のContent Cardsフィードでバナーを使用できますか？ {#can-i-use-banners-in-my-existing-content-card-feed}

バナーはContent Cardsとは異なるため、バナーとContent Cardsを同じフィードで使用することはできません。既存のContent Cardsフィードをバナーに置き換えるには、[アプリまたはWebサイトにプレースメントを作成する]({{site.baseurl}}/developer_guide/banners/placements)必要があります。

## バナーとアプリ内メッセージの違いは何ですか？ {#how-are-banners-different-from-in-app-messages}

バナーと[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages)はどちらもアプリやWebサイト内でユーザーにリーチしますが、配信モデルが異なります。バナーを既存のアプリ内メッセージの設定と比較する場合、トリガー、更新タイミング、テストに違いがあり、単純な置き換えではないことに注意してください。

| トピック | バナー | アプリ内メッセージ |
| --- | --- | --- |
| メッセージの表示場所 | アプリやサイトで定義した[プレースメント]({{site.baseurl}}/developer_guide/banners/placements)にインラインで表示 | SDKが管理するフルスクリーン、モーダル、またはスライドアップのオーバーレイ |
| コンテンツの更新タイミング | アプリやサイトがバナーの更新を呼び出したとき（例：セッション開始時やセッション中） | テンプレート化されたメッセージは、ペイロードがデバイスにキャッシュされた後、アプリ内メッセージがトリガーされたとき（例：カスタムイベントやセッション開始時）にLiquidを評価します |
| アクションベースのトリガー | [アクションベース配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)なし。代わりにセグメント、優先度、更新タイミングを使用します | アクションベースおよびAPIトリガー配信をサポート |
| テスト | ユーザーをプレビューし、アプリやサイトでプレースメントの更新により期待されるバナーが表示されることを確認します | トリガーベースの表示には**テスト送信**またはアプリ内プレビューフローを使用します |
| レポート | バナーのビューとクリックはバナー分析に準拠します | アプリ内のインプレッションとクリックはアプリ内メッセージ分析に準拠します |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="バナーとアプリ内メッセージの違いは何ですか？" }

## バナーに動画を含めることはできますか？ {#can-banners-include-video}

標準のバナービルダーは、画像、テキスト、ボタンをサポートしています。バナーに動画を含めるには、ビルダーで**カスタムコード**ブロックを使用するか、HTMLエディターでバナー全体を構築し、HTML内に動画プレーヤーを直接埋め込みます。

## ユーザーのアクションに基づいてバナーをトリガーできますか？ {#can-i-trigger-a-banner-based-on-user-actions}

バナーは[アクションベース配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)をサポートしていませんが、セグメンテーションと優先度を使用して、過去のアクションに基づいてユーザーをターゲットにすることができます。

例えば、`purchase`イベントを完了したユーザーにのみ特別なバナーを表示するには：
1. **ターゲティング：** キャンペーンで、カスタムイベント`purchase`を少なくとも1回実行したユーザーのセグメントをターゲットにします。
2. **優先度：** すべてのユーザー向けの一般的なバナーと、同じプレースメントをターゲットにした購入者向けの特定のバナーがある場合、特定のバナーの優先度を**高**に、一般的なバナーを**中**または**低**に設定します。

ユーザーが新しいセッションを開始するか、アクションの実行後にバナーを更新すると、Brazeはユーザーの適格性を評価します。「購入」セグメントに一致する場合、優先度の高いバナーが表示されます。

## ユーザーはバナーを閉じることができますか？ {#can-users-dismiss-a-banner}

はい。ユーザーがバナーを手動で閉じることを許可できます。ビルダーおよびHTMLエディターでの閉じる動作の設定方法について詳しくは、[閉じる動作の設定]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior)を参照してください。

ユーザーがバナーを手動で閉じることができるのは、閉じる動作が有効になっている場合のみです。閉じる動作が有効になっていない場合は、ユーザーセグメントの適格性を管理することでバナーの表示を制御できます。ユーザーがバナーキャンペーンのターゲティング条件を満たさなくなった場合、次のセッションではバナーが表示されなくなります。

ユーザーがバナーを閉じると、デフォルトではそのキャンペーンの対象外となります。閉じたユーザーに再度バナーを表示するには、キャンペーンの**配信コントロール**ステップで[再適格性を設定]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility)してください。キャンバスのバナーステップでは、代わりにキャンバスの再エントリ設定を使用して再適格性を制御します。

例えば、ユーザーが購入を完了するまでプロモーションバナーを表示している場合、`purchase_completed`などのイベントを記録することで、そのユーザーをターゲットセグメントから除外し、以降のセッションでバナーを非表示にすることができます。

## バナーキャンペーンの分析データをBraze APIを使ってエクスポートできますか？ {#can-i-export-banners-campaign-analytics-using-the-braze-api}

はい。[`/campaigns/data_series`エンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics)を使用して、バナーキャンペーンの閲覧数、クリック数、コンバージョン数に関するデータを取得できます。

## ユーザーはいつセグメント化されますか？ {#when-are-users-segmented}

ユーザーはセッション開始時にセグメント化されます。キャンペーンのターゲットセグメントがカスタム属性、カスタムイベント、またはその他のターゲティング属性に依存している場合、それらはセッション開始時にユーザーに存在している必要があります。

## バナーのレイテンシーを最小限に抑えるには、どのように構成すればよいですか？ {#how-can-i-compose-banners-to-ensure-the-lowest-latency}

バナーのメッセージがシンプルであるほど、レンダリングが速くなります。ユースケースで想定されるレイテンシーに対してバナーキャンペーンをテストすることをお勧めします。例えば、`catalog_items`のようなLiquid属性を必ずテストしてください。

[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)（早期アクセス中）を使用する場合、各呼び出しは1回の更新におけるすべてのプレースメントで共有される約2秒のレンダリング予算に対してカウントされることに注意してください。予算を超過するか、呼び出しがタイムアウトした場合、Connected Contentの結果はnullとして扱われ、バナーはリトライしません。レイテンシーを最小限に抑えるには：

- エンドポイントを高速に保ち、可能な限り[レスポンスをキャッシュ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)してください。
- 同時にレンダリングされるプレースメント間で、一意のConnected Content URLの数を制限してください。
- あるConnected Contentのレスポンスが次のURLを決定するような、呼び出しの連鎖を避けてください。
- Liquidのガードステートメントや[`default`フィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values)を使用して、null結果を処理し、空白のバナーを回避してください。

## すべてのLiquidタグはサポートされていますか？ {#are-all-liquid-tags-supported}

いいえ。ただし、バナーメッセージではほとんどのLiquidタグがサポートされています。例外として、[`:rerender`タグ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs#using-liquid)を使用して再レンダリングされる`catalog_items`はサポートされていません。

## クリックイベントをキャプチャできますか？ {#can-i-capture-click-events}

はい。クリックイベントのキャプチャ方法は、バナーのレンダリング方法によって異なります。

- **ビルダー — 標準コンポーネント:** バナーが標準エディターコンポーネント（画像、ボタン、テキスト）を使用している場合、SDKの挿入メソッドを使用するとクリックは自動的にトラッキングされます。
- **ビルダー — カスタムコードブロック:** カスタムコードエディターブロック内の要素のクリックをトラッキングしたい場合、カスタムHTML内から`brazeBridge.logClick()`を呼び出す必要があります。これは、SDKメソッドを使用してバナーを挿入・レンダリングする場合でも同様です。
- **HTMLエディター:** クリックトラッキングは自動ではありません。トラッキングしたいすべてのクリック可能な要素に対して`brazeBridge.logClick()`を呼び出す必要があります。完全なリファレンスについては、[バナーのカスタムコードとJavaScriptブリッジ]({{site.baseurl}}/user_guide/channels/banners/custom_code#javascript-bridge)を参照してください。
- **カスタムUI（ヘッドレス）:** バナーHTMLをレンダリングする代わりにバナーのカスタムプロパティを使用して完全にカスタムのUIを構築している場合、アプリケーションコードからバナーオブジェクトの`logClick()`を呼び出してください。

詳細については、[クリックのロギング]({{site.baseurl}}/developer_guide/banners/placements#logging-clicks)を参照してください。