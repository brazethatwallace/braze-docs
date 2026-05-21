---
nav_title: コンテキスト
article_title: コンテキスト
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "このリファレンス記事では、キャンバスでコンテキストステップを作成して使用する方法について説明します。"
tool: Canvas

---

# コンテキスト {#context}

> コンテキストステップを使用すると、ユーザーがキャンバスを進む際に、1つ以上の変数を作成・更新できます。たとえば、季節割引を管理するキャンバスがある場合、コンテキスト変数を使用して、ユーザーがキャンバスに入るたびに異なる割引コードを保存できます。

## 仕組み {#how-it-works}

![キャンバスの最初のステップとしてのコンテキストステップ。]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

コンテキストステップを使用すると、特定のキャンバスにおけるユーザーのジャーニー中に一時的なデータを作成して使用できます。このデータはそのキャンバスジャーニー内にのみ存在し、異なるキャンバスやセッション外には保持されません。

コンテキスト変数は、その特定のキャンバスジャーニーにのみ存在します。ユーザーのプロファイルを永続的に変更することはなく、他のキャンバスにも表示されません。そのため、特定のキャンペーンやワークフローにのみ関連する一時的な情報に最適です。

{% alert tip %}
コンテキスト変数の完全なリファレンス（データタイプ、使用方法、ベストプラクティスを含む）については、[コンテキスト変数リファレンス]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)を参照してください。
{% endalert %}

コンテキストステップ内では、最大10個のコンテキスト変数を定義または更新できます。これらの変数は、遅延のパーソナライズ、ユーザーのダイナミックなセグメント化、キャンバス全体でのメッセージングの充実に使用できます。たとえば、ユーザーの予定フライト時刻のコンテキスト変数を作成し、それを使用してパーソナライズされた遅延を設定してリマインダーを送信できます。

コンテキスト変数は2つの方法で設定できます：

- **キャンバスエントリ時：** カスタムイベントまたはAPIトリガーからのプロパティが、コンテキスト変数として自動的に入力されます。
- **コンテキストステップ内：** コンテキストステップを追加して、コンテキスト変数を手動で定義または更新します。

各コンテキスト変数には、名前、データタイプ、および値（Liquidまたはパーソナライゼーションの追加ツールを使用して設定）が必要です。定義すると、{% raw %}`{{context.${flight_time}}}`{% endraw %}のようにLiquidを使用してキャンバス全体でコンテキスト変数を参照できます。**コンテキスト変数名**フィールドでは、コンテキスト変数名を入力するか、ステップエディターのドロップダウンから選択することもできます。詳細については、[コンテキスト変数リファレンス]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)を参照してください。

キャンバスへのエントリごとに、最新のエントリデータとキャンバス設定に基づいてコンテキスト変数が再定義されるため、ユーザーはそれぞれ独自のコンテキストを持つ複数のアクティブなジャーニーを持つことができます。たとえば、顧客に2つの今後のフライトがある場合、2つの別々のジャーニー状態が同時に実行されます&#8212;それぞれが出発時刻や目的地などの独自のフライト固有のコンテキスト変数を持ちます。これにより、ニューヨーク行きの午後2時のフライトに関するパーソナライズされたリマインダーを送信しながら、明日のロサンゼルス行きの午前8時のフライトに関する別の更新を送信でき、各メッセージが特定の予約に関連したものになります。

### ユーザー処理とバッチ処理 {#user-processing-and-batching}

コンテキストステップは、パフォーマンスを最適化するためにユーザーをバッチで処理します。ユーザーがコンテキストステップに入ると、Brazeはデフォルトで1,000ユーザーのバッチで処理します。これらのバッチは並列で処理されますが、各バッチ内ではユーザーは順次処理されます。

つまり：

**例**：3,500人のユーザーが、ユーザーあたり650msかかるコネクテッドコンテンツを含むコンテキストステップに入った場合：
- Brazeは4つのバッチを作成します（この例では1,000、1,000、1,000、500ユーザー）。
- 各バッチはユーザーを順次処理するため、1,000ユーザーのバッチは約10.8分（650秒、1,000 × 650ms）かかります。
- バッチは異なるタイミングで完了するため、バッチが完了するにつれてユーザーは次のステップに順次進みます。
- バッチサイズとコネクテッドコンテンツの応答時間に応じて、最初のユーザーは最後のユーザーよりも数分早く次のステップに到達する場合があります。

コネクテッドコンテンツがない場合、外部APIコールを待つ必要がないため、コンテキストステップの処理ははるかに高速になります。

## 考慮事項 {#considerations}

- コンテキストステップごとに最大10個のコンテキスト変数を定義できます。
- 各変数にはユニークな名前が必要です（文字、数字、アンダースコアのみ、最大100文字）。
- ステップ内のすべての変数の合計サイズは50 KBを超えることはできません。
- APIトリガーで渡された変数は、コンテキストステップで作成された変数と同じ名前空間を共有します。コンテキストステップで変数を再定義すると、API値が上書きされます。

詳細と高度な使用方法については、[コンテキスト変数リファレンス]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)を参照してください。

## コンテキストステップの作成 {#creating-a-context-step}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### ステップ 1: ステップを追加する {#step-1-add-a-step}

キャンバスにステップを追加し、サイドバーからコンポーネントをドラッグ＆ドロップするか、<i class="fas fa-plus-circle"></i>プラスボタンを選択して**Context**を選択します。

### ステップ 2: 変数を定義する {#step-2-define-the-variables}

{% alert note %}
各コンテキストステップに対して最大10個のコンテキスト変数を定義できます。
{% endalert %}

コンテキスト変数を定義するには：

1. コンテキスト変数に**名前**を付けます。
2. [データタイプ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#data-types)を選択します。
3. Liquid式を手動で記述するか、**Add Personalization**を使用して既存の属性からLiquidスニペットを作成します。
4. **Preview**を選択して、コンテキスト変数の値を確認します。
5. （オプション）追加の変数を追加するには、**Add Context variable**を選択してステップ1〜4を繰り返します。
6. 完了したら、**Done**を選択します。

これで、メッセージステップやユーザーの更新ステップなど、Liquidを使用するあらゆる場所で**Add Personalization**を選択してコンテキスト変数を使用できます。**コンテキスト変数名**フィールドでは、コンテキスト変数名を入力するか、ステップエディターのドロップダウンから選択することもできます。完全なウォークスルーについては、[コンテキスト変数リファレンス]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/)を参照してください。

{% alert important %}
コンテキスト変数を参照する際は、常に{% raw %}`{{context.${variable_name}}}`{% endraw %}の形式を使用してください。
{% endalert %}

### コンテキスト変数フィルター {#context-variable-filters}

[オーディエンスパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/)および[条件分岐]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)ステップで、コンテキスト変数を使用してフィルターを作成できます。

[Agentステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step/)の応答に基づいてユーザーをルーティングするには、オーディエンスパスまたは条件分岐ステップの前にAgentステップを追加します。Agentステップはその出力をキャンバスコンテキストに保存するため、それらの分岐ステップでコンテキスト変数フィルターを使用して評価できます。

Agentがオブジェクトを返し、ネストされたプロパティでフィルタリングしたい場合は、トップレベルの変数名だけでなく、**コンテキスト変数名**フィールドにドット表記でパスを入力します（たとえば、`persona`が`intent_agent`の下にネストされている場合は`intent_agent.persona`）。

フィルターの設定、比較ロジック、高度な例については、[コンテキスト変数リファレンス]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#context-variable-filters)を参照してください。

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## ユーザーパスのプレビュー {#previewing-user-paths}

メッセージが適切なオーディエンスに送信され、コンテキスト変数が期待どおりの結果に評価されることを確認するために、テストと[ユーザーパスのプレビュー]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/)をお勧めします。

{% alert note %}
エディターの**Preview & Test Send**セクションでキャンバスをプレビューしている場合、テストメッセージプレビューのタイムスタンプはUTCに標準化**されません**。これは、このパネルがプレビューを文字列として生成するためです。つまり、キャンバスが`time`オブジェクトを受け入れるように設定されている場合、メッセージプレビューはキャンバスがライブのときに発生する内容を正確にプレビューしません。キャンバスを最も正確にテストするには、代わりにユーザーパスのプレビューをお勧めします。
{% endalert %}

無効なコンテキスト変数を作成する一般的なシナリオに注意してください。ユーザーパスをプレビューすると、コンテキスト変数を使用したパーソナライズされた遅延ステップの結果や、ユーザーをコンテキスト変数に一致させるオーディエンスまたは条件分岐ステップの比較を確認できます。

コンテキスト変数が有効な場合、キャンバス全体で変数を参照できます。ただし、コンテキスト変数が正しく作成されなかった場合、キャンバスの後続のステップも正しく動作しません。たとえば、ユーザーに予約時間を割り当てるコンテキストステップを作成し、予約時間の値を過去の日付に設定した場合、メッセージステップのリマインダーメールは送信されません。

## コネクテッドコンテンツの文字列をJSONに変換する {#converting-connected-content-strings-to-json}

コンテキストステップで[コネクテッドコンテンツコール]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)を行う場合、コールから返されたJSONは一貫性とエラー防止のために文字列データタイプとして評価されます。この文字列をJSONに変換したい場合は、`as_json_string`を使用して変換します。例：

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## トラブルシューティング {#troubleshooting}

### 無効なコンテキスト変数 {#invalid-context-variables}

コンテキスト変数は以下の場合に無効とみなされます：

- 埋め込まれたコネクテッドコンテンツへのコールが失敗した場合。
- ランタイムでLiquid式がデータタイプに一致しない値または空（null）の値を返した場合。

たとえば、コンテキスト変数のデータタイプが**数値**であるにもかかわらず、Liquid式が文字列を返した場合、無効となります。

このような状況では：
- ユーザーは次のステップに進みます。
- キャンバスステップの分析では、これが「_未更新_」としてカウントされます。

トラブルシューティングの際は、「_未更新_」指標を監視して、コンテキスト変数が正しく更新されているか確認してください。コンテキスト変数が無効な場合、ユーザーはコンテキストステップを通過してキャンバスを続行できますが、後続のステップの条件を満たさない可能性があります。

各データタイプの設定例については、[データタイプ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/#data-types)を参照してください。

### コネクテッドコンテンツによる送信の遅延 {#delays-in-sending-with-connected-content}

バッチ内のすべてのユーザーが処理されてから、ユーザーが次に進みます。バッチ処理が完了すると、成功したユーザーは次のステップに進み、失敗したユーザーは別途リトライされます。成功したユーザーは、リトライが成功するのを待たずに先に進みます。

#### リトライ動作 {#retry-behavior}

キャンバスステップ（コンテキストステップを含む）では、Brazeは標準のコネクテッドコンテンツのリトライ動作ではなく、キャンバス固有のリトライメカニズムを使用します。コネクテッドコンテンツコールが失敗した場合：

 - メッセージステップでは、コネクテッドコンテンツコールは最大5回リトライできます。
 - その他すべてのステップでは、Brazeはエクスポネンシャルバックオフで約13回ステップをリトライします。

すべてのリトライが失敗した場合、ユーザーはキャンバスを退出します。

標準のコネクテッドコンテンツで使用される`:retry`タグは、キャンバスステップ内で行われるコネクテッドコンテンツコールには適用されません。キャンバスステップには、キャンバスワークフロー向けに最適化された独自のリトライロジックがあります。

コンテキストステップですべてのユーザーを処理するのにかかる時間は、以下に依存します：

- ステップに入るユーザー数
- コネクテッドコンテンツが使用されているかどうか（およびその応答時間）
- バッチサイズ（デフォルトはバッチあたり1,000ユーザー）

コネクテッドコンテンツのエンドポイントにレート制限がある場合、コンテキストステップは各バッチ内でユーザーを順次処理するため、レート制限を自然に尊重するのに役立ちます。ただし、複数のバッチは並列で処理されるため、エンドポイントが複数のバッチからの同時リクエストを処理できることを確認してください。

## タイムゾーンの一貫性の標準化 {#time-zone-consistency-standardization}

キャンバスコンテキストの一般提供に伴い、アクションベースのキャンバスにおけるすべてのデフォルトのタイムスタンプイベントプロパティはUTCになります。この変更は、キャンバスステップやメッセージの編集時に、より予測可能で一貫性のある体験を確保するための広範な取り組みの一環です。この変更は、特定のキャンバスがコンテキストステップを使用しているかどうかに関係なく、すべてのアクションベースのキャンバスに影響します。

{% alert important %}
すべての状況において、タイムスタンプを希望するタイムゾーンで表示するために、[Liquid time_zoneフィルター]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/#things-to-know)を使用することを強くお勧めします。例については、この[よくある質問](#faq-example)を参照してください。
{% endalert %}

## よくある質問 {#frequently-asked-questions}

### キャンバスコンテキストの一般提供以降、何が変わりましたか？ {#what-has-changed-since-canvas-context-became-generally-available}

キャンバスコンテキストが一般提供されたことにより、以下の詳細が適用されます：

- アクションベースのキャンバスにおける[トリガーイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)の[datetimeタイプ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/)を持つすべてのタイムスタンプは[UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)になります。
- この変更は、特定のキャンバスがコンテキストステップを使用しているかどうかに関係なく、すべてのアクションベースのキャンバスに影響します。

#### この変更の理由は何ですか？ {#what-is-the-reason-for-this-change}

この変更は、キャンバスステップやメッセージの編集時に、より予測可能で一貫性のある体験を作り出すための広範な取り組みの一環です。

#### APIトリガーまたはスケジュールされたキャンバスはこの変更の影響を受けますか？ {#are-api-triggered-or-scheduled-canvases-impacted-by-this-change}

いいえ。

#### この変更はキャンバスエントリプロパティに影響しますか？ {#does-this-change-impact-canvas-entry-properties}

はい、`canvas_entry_property`がアクションベースのキャンバスで使用されており、プロパティタイプが`time`の場合、`canvas_entry_properties`に影響します。すべての状況において、タイムスタンプを希望するタイムゾーンで表示するために、Liquidの`time_zone`フィルターを使用することをお勧めします。

以下はその方法の例です：

| メッセージステップのLiquid | 出力 | Liquidでタイムゾーンを正しく表現する方法ですか？ |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | いいえ |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | いいえ |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="この変更はキャンバスエントリプロパティに影響しますか？" }

#### 新しいタイムスタンプの動作がメッセージにどのように影響するかの実用的な例は何ですか？ {#faq-example}

メッセージステップに以下のコンテンツを含むアクションベースのキャンバスがあるとします：

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

これにより、以下のメッセージが生成されます：

```
Your appointment is scheduled for 2025-08-05 4:15 PM, we’ll see you then!
```

Liquidでタイムゾーンが指定されていないため、ここのタイムスタンプはUTCです。

タイムゾーンを明確に指定するには、Liquidの`time_zone`フィルターを次のように使用できます：

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

これにより、以下のメッセージが生成されます：

```
Your appointment is scheduled for 2025-08-05 8:15 AM, we'll see you then!
```

LiquidでAmerica/Los Angelesタイムゾーンが指定されているため、ここのタイムスタンプはPSTです。

希望するタイムゾーンは、イベントプロパティのペイロードで送信し、Liquidロジックで使用することもできます：

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### コンテキスト変数はキャンバスエントリプロパティとどう異なりますか？ {#how-do-context-variables-differ-from-canvas-entry-properties}

キャンバスエントリプロパティは、キャンバスコンテキスト変数として含まれます。つまり、Braze APIを使用してキャンバスエントリプロパティを送信し、Liquidスニペットでコンテキスト変数を使用するのと同様に、他のステップで参照できます。

### 1つのコンテキストステップ内で変数同士を参照できますか？ {#can-variables-reference-each-other-in-a-singular-context-step}

はい。コンテキストステップ内のすべての変数は順番に評価されるため、以下のようなコンテキスト変数を設定できます：

| コンテキスト変数 | 値 | 説明 |
|---|---|---|
| `favorite_cuisine` | {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | ユーザーのお気に入りの料理ジャンル。 |
| `promo_code` | {% raw %}`EATFRESH`{% endraw %} | ユーザーが利用可能な割引コード。 |
| `personalized_message` | {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | 前の変数を組み合わせたパーソナライズされたメッセージです。メッセージステップでは、Liquidスニペット{% raw %}`{{context.${personalized_message}}}`{% endraw %}を使用してコンテキスト変数を参照し、各ユーザーにパーソナライズされたメッセージを配信できます。また、コンテキストステップを使用して[プロモーションコード]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/#creating-a-promotion-code-list)の値を保存し、キャンバス全体の他のステップでテンプレート化することもできます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="1つのコンテキストステップ内で変数同士を参照できますか？" }

これは複数のコンテキストステップにまたがっても適用されます。たとえば、次のシーケンスを想像してください：

1. 最初のコンテキストステップで、値が`job_title`の`JobInfo`という変数を作成します。
2. メッセージステップが{% raw %}`{{context.${JobInfo}}}`{% endraw %}を参照し、ユーザーに`job_title`を表示します。
3. その後、コンテキストステップがコンテキスト変数を更新し、`JobInfo`の値を`job_description`に変更します。
4. `JobInfo`を参照するすべての後続ステップは、更新された値`job_description`を使用するようになります。

コンテキスト変数はキャンバス全体で最新の値を使用し、各更新はその変数を参照するすべての後続ステップに影響します。