---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "この参考記事では、BrazeとSegmentのパートナーシップについて概説しています。Segmentは、マーケティングスタックのソース間で情報を収集し、ルーティングする顧客データプラットフォームです。"
page_type: partner
search_tag: Partner

---

# セグメント Engage

> [セグメント](https://segment.com) は、顧客データの収集、クリーンアップ、およびアクティブ化を支援する顧客データプラットフォームです。この参考記事では、[Brazeとセグメント Engage](https://segment.com/docs/destinations/braze/#Engage) の接続について概説し、適切な実装と利用のための要件とプロセスを説明します。

Brazeとセグメントの統合により、セグメントに組み込まれたオーディエンスビルダーである[Engage](https://segment.com/docs/engage/)を使って、さまざまなソースから収集したデータに基づいてユーザーのセグメントを作成できます。これらのオーディエンスは、コホートとしてBrazeに同期されるか、[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)や[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-events)を通じてユーザープロファイルに示され、キャンペーンやキャンバスのリターゲティングで使用するBrazeセグメントを作成するために利用できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| セグメントアカウント | このパートナーシップを活用するには、[セグメントアカウント](https://app.segment.com/login)が必要です。 |
| Braze Cloudの送信先 | セグメント統合で[Brazeを送信先として設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)している必要があります。<br><br>これには、[接続設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment#connection-settings)で正しいBrazeデータセンターとREST APIキーを提供することが含まれます。 |
| Brazeデータインポートキー | EngageオーディエンスをコホートとしてBrazeに同期するには、データインポートキーを生成する必要があります。<br><br>コホートのインポート機能は早期アクセスの段階であるため、この機能を利用するにはBrazeのカスタマーサクセスマネージャーにお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## コホート送信先の統合 {#cohorts-destination-integration}

### ステップ1：Engageオーディエンスを作成する {#step-1-create-an-engage-audience}
1. セグメントで、Engageの**Audiences**タブに移動し、**New**をクリックします。
2. オーディエンスを作成します。ページ上部の稲妻アイコンは、オーディエンスがリアルタイムで更新されるかどうかを示します。
3. 次に、送信先としてBrazeを選択します。
4. **Review & Create**をクリックしてオーディエンスをプレビューします。デフォルトでは、セグメントは計算済み特性とオーディエンスの現在の値を設定するため、すべての履歴データをクエリします。このデータを省略するには、**Historical Backfill**のチェックを外します。

### ステップ2：コホートデータインポートキーを取得する {#step-2-capture-your-cohort-data-import-key}

Brazeで、**パートナー連携** > **テクノロジーパートナー**に移動し、**セグメント**を選択します。

ここで、RESTエンドポイントを確認し、Brazeデータインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。

### ステップ3：Brazeコホートの送信先を接続する {#step-3-connect-the-braze-cohorts-destination}
Cohorts Destinationの設定に関する[セグメントの手順](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started)に従って、EngageオーディエンスをコホートとしてBrazeに同期します。

### ステップ4：EngageオーディエンスからBrazeセグメントを作成する {#step-4-create-a-braze-segment-from-the-engage-audience}
Brazeで**セグメント**に移動し、新しいセグメントを作成し、フィルターとして**セグメント Cohorts**を選択します。ここから、含めるセグメントコホートを選択できます。セグメントコホートセグメントを作成した後、キャンペーンやキャンバスを作成する際にオーディエンスフィルターとして選択できます。

![セグメント Cohortsフィルターを使用したBrazeセグメントビルダー。]({% image_buster /assets/img/segment/segment3.png %})

## クラウドモードの統合 {#cloud-mode-integration}

### ステップ1：セグメントの計算済み特性またはオーディエンスを作成する {#step-1-create-a-segment-computed-trait-or-audience}

1. セグメントで、**Engage**の**Computed Traits**タブまたは**Audiences**タブに移動し、**New**をクリックします。
2. 計算済み特性またはオーディエンスを作成します。ページ上部の稲妻アイコンは、計算がリアルタイムで更新されるかどうかを示します。
3. 次に、送信先として**Braze**を選択します。
4. **Review & Create**をクリックしてオーディエンスをプレビューします。デフォルトでは、セグメントは計算済み特性とオーディエンスの現在の値を設定するため、すべての履歴データをクエリします。このデータを省略するには、**Historical Backfill**のチェックを外します。
5. 計算済み特性またはオーディエンスの設定で、Brazeへのデータ送信方法に基づいて接続設定を調整します。

#### 計算済み特性とオーディエンス {#computed-traits-and-audiences}

[計算済み特性](https://segment.com/docs/engage/audiences/computed-traits/)と[オーディエンス](https://segment.com/docs/Engage/audiences/)は、カスタム属性やカスタムイベントとしてBrazeに送信できます。
- `identify` 呼び出しを使用して送信された特性とオーディエンスは、Brazeではカスタム属性として表示されます。
- `track` 呼び出しを使用して送信された特性とオーディエンスは、Brazeではカスタムイベントとして表示されます。

計算済み特性をBrazeの送信先に接続する際に、どちらの方法を使うか（あるいは両方を使うか）を選択できます。

{% tabs %}
{% tab Identify %}

Brazeでカスタム属性を作成するために、計算済み特性とオーディエンスを `identify` 呼び出しとしてBrazeに送信できます。

例えば、「Last Product Viewed Item」に対するEngageの計算済み特性がある場合、ユーザーのBrazeプロファイルの**カスタム属性**に `last_product_viewed_item` が表示されます。これがEngageのオーディエンスであった場合、**カスタム属性**の下に `true` として設定されたオーディエンスが表示されます。

| 計算済み特性 | オーディエンス |
| -------------- | --------- |
| ![ユーザープロファイル内のカスタム属性セクションに「last_product_viewed_item」が「Sweater」と表示されている。]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![ユーザープロファイル内のカスタム属性セクションに「dormant_shopper」が「true」と表示されている。]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="計算済み特性とオーディエンス" }

{% endtab %}
{% tab Track %}

Brazeでカスタムイベントを作成するために、計算済み特性とオーディエンスを `track` 呼び出しとしてBrazeに送信できます。

前の例の続きで、ユーザーが「Last Product Viewed Item」の計算済み特性を持っている場合、ユーザーのBrazeプロファイルに `Trait Computed` として、対応するカウントと最新のタイムスタンプとともに**Custom Events**の下に表示されます。これがEngageオーディエンスであった場合、オーディエンス、カウント、および最新のタイムスタンプが `true` として設定された**カスタム属性**の下に表示されます。

| 計算済み特性 | オーディエンス |
| -------------- | --------- |
| ![ユーザープロファイルのカスタムイベントセクションに「Trait Computed」が「1」回と表示され、最終時刻は「20時間前」となっている。]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![ユーザープロファイル内のカスタム属性セクションに「Audience Entered」が「1」回と表示され、最終時刻は「3月9日午前1時45分」となっている。]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="計算済み特性とオーディエンス" }

{% endtab %}
{% endtabs %}

### ステップ2：Brazeでユーザーをセグメント化する {#step-2-segment-users-in-braze}

Brazeでこれらのユーザーのセグメントを作成するには、**エンゲージメント**の下の**セグメント**に移動し、新しいセグメントを作成してセグメントに名前を付けます。次に、使用した呼び出しに基づいて以下の操作を行います。
- **Identify**：フィルターとして**カスタム属性**を選択し、カスタム属性を探します。次に、「matches regex」オプション（特性）または「equals」オプション（オーディエンス）を使用して、適切な変数を入力します。
- **Track**：フィルターとして**カスタムイベント**を選択し、カスタムイベントを探します。次に、「more than」、「less than」、または「exactly」オプションを使用して必要な値を挿入します。これは、セグメントをどのように定義するかによって異なります。

保存すると、キャンペーンやキャンバスの作成時に、ユーザーのターゲティングステップでこのセグメントを参照できます。

## 同期時間 {#sync-time}

Brazeからセグメント Engageへの接続のデフォルト設定は `Realtime` ですが、ペルソナがリアルタイム同期の対象外となるフィルターがいくつかあります。これには、メッセージ送信時のオーディエンスのサイズを制限する時間ベースのフィルターが含まれます。

## セグメントデバッガーのテスト {#segment-debugger-testing}

セグメントのダッシュボードにある「Debugger」機能により、「ソース」からのデータが期待どおりに「送信先」に転送されているかどうかをテストできます。

この機能はBrazeの[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)に接続するため、識別済みのユーザー（BrazeユーザープロファイルのユーザーIDがすでに設定されているユーザー）のみに使用できます。

これはサイドバイサイドのBraze統合では機能しません。正しいBraze REST API情報が入力されていない場合、サーバーデータは転送されません。