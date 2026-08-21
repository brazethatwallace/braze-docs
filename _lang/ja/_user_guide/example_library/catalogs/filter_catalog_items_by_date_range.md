---
nav_title: 日付範囲でフィルタリング
article_title: カタログアイテムを日付範囲でフィルタリング
page_order: 1
page_type: reference
description: "カタログセレクションとLiquidの日付式を使用して、今後7日間のイベントなど、ローリングタイムウィンドウ内のカタログアイテムを表示します。"
---

# カタログアイテムを日付範囲でフィルタリング {#filter-catalog-items-by-date-range}

> この例では、架空のチケットマーケットプレイスがカタログセレクションとLiquidの日付式を使用して、送信時点から今後7日以内に開催されるイベントのみを消費者にメールで送信する方法を示します。ローリングタイムフィルターを使用してセレクションを作成し、一致するカタログアイテムをキャンペーンまたはキャンバスメッセージでレンダリングします。

## この例について {#about-this-example}

架空のチケットマーケットプレイスであるMovieCanonは、このパターンを使用して、メールキャンペーンに時間的に関連するコンサートやショーのみをリストします。

このパターンでは、2つのBraze機能を組み合わせて使用します。

- Liquidスニペットで送信時にローリングタイムウィンドウを計算する`time`フィールドフィルターを持つ[カタログセレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- メッセージ本文で一致するカタログ行をレンダリングする{% raw %}`{% catalog_selection_items %}`{% endraw %} Liquidタグ

## 考慮事項 {#considerations}

- フィルタリングする日時列には、文字列フィールドではなくカタログの`time`フィールドを作成してください。値は`2026-06-20T19:30:00Z`のような[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)形式で保存します。サポートされている型については、[サポートされているデータ型]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types)を参照してください。
- `before`および`after`オペレーターは厳密な比較を使用します。境界タイムスタンプと正確に等しいイベントは除外される場合があります。ウィンドウを送信時刻から開始する必要がある場合は、完全なタイムスタンプを使用してください。日付のみの`YYYY-MM-DD`値は、その日のUTC午前0時に変換されます。
- セレクションフィルターのLiquidは送信時に評価されます。`'now'`変数はメッセージがレンダリングされる時刻を反映し、通常はUTCです。結果のウィンドウがタイムゾーン間で意図と一致することを確認してください。
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)、[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)、カタログタグ、および`abort_message`は、カタログセレクションのフィルター値ではサポートされていません。フィルターに許可されていないタグが含まれている場合、セレクションはエラーを発生させずにアイテムを返しません。
- セレクションごとに最大10個のフィルターを追加でき、最大50個のアイテムを返すことができます。`'now'`に加算する秒数を変更することで、7日間のウィンドウを調整できます（`604800` = 7日 × `86400`秒/日）。
- カタログセレクションの結果配列はゼロインデックスです（`items[0]`が最初のアイテムです）。
- 本番オーディエンスに送信する前に、本番ワークスペース外でフィルターのLiquid、メッセージのLiquid、および中止ロジックをテストしてください。

## 設定 {#setup}

この例では、以下のフィールドを持つ`live_events`という名前のカタログを想定しています。

| フィールド | 型 | 値の例 |
| ----- | ---- | ------------- |
| `id` | String | `show-1042` |
| `event_name` | String | `Summer Jazz Night` |
| `event_date_time` | Time | `2026-06-20T19:30:00Z` |
| `ticket_price` | Number | `45` |
| `city` | String | `Austin` |
| `venue` | String | `Riverside Amphitheater` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カタログフィールド" }

同様のカタログがまだない場合は、[カタログを作成]({{site.baseurl}}/user_guide/data/activation/catalogs/create)し、イベントデータをアップロードまたは同期してください。

### ステップ1: カタログセレクションを作成する {#step-1-create-the-catalog-selection}

1. **データ設定** > **カタログ**に移動し、`live_events`カタログを選択します。
2. **セレクション**タブを開き、**セレクションを作成**を選択します。
3. セレクションに`seven_day_window`と名前を付け、「今後7日以内に開催されるイベント」などのオプションの説明を追加します。
4. 返すイベントの最大数として**結果の上限**を設定します（最大50）。
5. まだ保存しないでください。次のステップで日付フィルターを追加します。

### ステップ2: 上限フィルターを追加する {#step-2-add-the-upper-bound-filter}

`event_date_time`フィールドにフィルターを追加します。

| 設定 | 値 |
| ------- | ----- |
| **フィルターフィールド** | `event_date_time` |
| **オペレーター** | `before` |
| **値** | Liquidスニペット |
{: .reset-td-br-1 .reset-td-br-2 aria-label="上限フィルターの設定" }

フィルター値フィールドに、このLiquidスニペットを入力します。送信時から7日後のタイムスタンプを計算します。

{% raw %}
```liquid
{% assign seven_days = 'now' | date: '%s' | plus: 604800 %}{{ seven_days | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

これにより、ウィンドウの上限が設定され、そのタイムスタンプより前のイベントのみが含まれます。

### ステップ3: 下限フィルターを追加する {#step-3-add-the-lower-bound-filter}

同じフィールドに2つ目のフィルターを追加します。

| 設定 | 値 |
| ------- | ----- |
| **フィルターフィールド** | `event_date_time` |
| **オペレーター** | `after` |
| **値** | Liquidスニペット |
{: .reset-td-br-1 .reset-td-br-2 aria-label="下限フィルターの設定" }

下限として、このLiquidスニペットを入力します。現在の送信時刻を使用するため、すでに開始されたイベントは除外されます。

{% raw %}
```liquid
{{ 'now' | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

2つのフィルターを合わせると、`event_date_time`が現在の送信時刻より後かつ送信時から7日以内のカタログアイテムが返されます。**セレクションを作成**を選択して保存します。

### ステップ4: メッセージでセレクションを参照する {#step-4-reference-the-selection-in-a-message}

キャンペーンまたはキャンバスメッセージで、セレクションからアイテムを取得するLiquidを挿入します。**パーソナライゼーションを追加**（**カタログアイテム** > **セレクションを使用**）を使用するか、タグを手動で貼り付けることができます。

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
Here are some upcoming events:

{{ items[0].event_name }} — ${{ items[0].ticket_price }}
{{ items[0].city }} · {{ items[0].venue }}

{{ items[1].event_name }} — ${{ items[1].ticket_price }}
{{ items[1].city }} · {{ items[1].venue }}
```
{% endraw %}

可変数の結果をレンダリングする必要がある場合は、ハードコードされた配列インデックスをループに置き換えてください。

### ステップ5: 空の結果を処理する {#step-5-handle-empty-results}

セレクションに一致するカタログアイテムがない場合、`items`配列は空になり、タグ付きブロックは何もレンダリングしません。送信をスキップするか、フォールバックコピーを表示するには、タグを条件文で囲みます。

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
{% if items.size == 0 %}
{% abort_message('Catalog selection returned 0 items') %}
{% endif %}

Here are some upcoming events:
{{ items[0].event_name }}
```
{% endraw %}

詳細については、[メッセージの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)を参照してください。

## 関連記事 {#related-articles}

- [カタログを作成する]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [キャンペーンでカタログを使用する]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Liquidの`date`フィルター]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter)
- [Liquidユースケースライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)