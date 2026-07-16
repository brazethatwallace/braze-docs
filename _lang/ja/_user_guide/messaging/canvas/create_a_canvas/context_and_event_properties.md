---
nav_title: コンテキストとイベントプロパティ
article_title: コンテキストとイベントプロパティ
page_order: 4.2
page_type: reference
description: "このリファレンス記事では、コンテキストとイベントプロパティの違い、およびそれぞれのプロパティを使用するタイミングについて説明します。"
tool: Canvas
---

# コンテキストとイベントプロパティ {#context-and-event-properties}

> このリファレンス記事では、`context`と`event_properties`に関する情報を取り上げます。それぞれのプロパティを使用するタイミングや動作の違いについて説明します。<br><br> カスタムイベントプロパティ全般については、[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)をご覧ください。

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

コンテキストプロパティとイベントプロパティは、キャンバスワークフロー内で異なる動作をします。ユーザーのキャンバスへのエントリをトリガーするイベントまたはAPI呼び出しのプロパティは`context`と呼ばれます。ユーザーがキャンバスジャーニー内を移動する際に発生するイベントのプロパティは`event_properties`と呼ばれます。主な違いは、`context`がイベントだけでなく、APIトリガーキャンバスのエントリペイロードのプロパティにもアクセスできる点です。

コンテキストとイベントプロパティの違いの概要については、以下の表を参照してください。

| | コンテキストプロパティ | イベントプロパティ |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **永続性** | キャンバスを使用して構築されたキャンバスの期間中、すべての[メッセージ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)ステップで参照できます。 | - 一度だけ参照できます。<br> - 後続のメッセージステップでは参照できません。 |
| **キャンバスの動作** | キャンバスの任意のステップで`context`を参照できます。起動後の動作については、[起動後のキャンバスの編集]({{site.baseurl}}/post-launch_edits#canvas-entry-properties)を参照してください。 | - [アクションパス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)ステップの**後**の最初のメッセージステップで`event_properties`を参照できます。ここでのアクションはカスタムイベントまたは購入イベントです。<br> - アクションパスステップのその他のユーザーパスの後では参照できません。<br> - アクションパスとメッセージステップの間に、メッセージ以外のコンポーネントを配置できます。これらのメッセージ以外のコンポーネントの1つがアクションパスステップの場合、ユーザーはそのアクションパスのその他のユーザーパスを通過できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="コンテキストとイベントプロパティ" }

{% details オリジナルキャンバスエディターの詳細 %}

オリジナルエディターを使用してキャンバスを作成または複製することはできなくなりました。キャンバスコンテキストはオリジナルキャンバスエディターではサポートされていないため、このセクションは以前のキャンバスワークフローでキャンバスエントリプロパティとイベントプロパティを使用する際の参照用として提供されています。

**キャンバスエントリプロパティ:**
- 永続的なエントリプロパティを有効にする必要があります。
- キャンバスの最初のフルステップでのみ`canvas_entry_properties`を参照できます。キャンバスはアクションベースまたはAPIトリガーである必要があります。

**エントリプロパティ:**
- キャンバス内でアクションベースの配信を使用する任意のフルステップで`event_properties`を参照できます。
- アクションベースのキャンバスの最初のフルステップ以外のスケジュールされたフルステップでは使用できません。ただし、ユーザーが[キャンバスコンポーネント]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about)を使用している場合、動作は`event_properties`の現在のキャンバスワークフロールールに従います。

**イベントプロパティ:**
- 先頭のメッセージステップでは`event_properties`を使用できません。代わりに、`canvas_entry_properties`を使用するか、`event_properties`を含むメッセージステップの**前**に対応するイベントを持つアクションパスステップを追加する必要があります。

{% enddetails %}

## 知っておくべきこと {#things-to-know}

- コンテキストはLiquidでの参照にのみ使用できます。キャンバス内のプロパティでフィルタリングするには、代わりに[イベントプロパティセグメンテーション]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)を使用してください。
- アプリ内メッセージチャネルでは、キャンバスで`context`と`event_properties`を参照できます。`event_properties`はトリガーベースであるため、最初のキャンバスステップに含まれている場合にアクセスできます。
- 先頭のメッセージステップでは`event_properties`を使用できません。代わりに、`context`を使用するか、`event_properties`を含むメッセージステップの**前**に対応するイベントを持つアクションパスステップを追加できます。
- アクションパスステップに「SMS受信メッセージを送信」または「WhatsApp受信メッセージを送信」トリガーが含まれている場合、後続のキャンバスステップにSMSまたはWhatsAppのLiquidプロパティを含めることができます。これはキャンバスでのイベントプロパティの動作と同様です。これにより、メッセージを活用してファーストパーティデータをユーザープロファイルや会話型メッセージングに保存・参照できます。

{% alert note %}
オーディエンスの適格性は、キャンバスエントリ時に一度だけ評価されます。エントリ中にユーザーがマージされた場合、識別されたユーザーはキャンバスを続行し、キャンバスのセグメント基準に対して再評価されることはありません。
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### トリガーのタイムスタンプ {#timestamps-for-triggers}

アクションベースのキャンバスをトリガーするイベントからの[日時型]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)のタイムスタンプを使用し、[コンテキスト]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を使用して参照する場合、タイムスタンプはUTCに正規化されます。

この動作を考慮して、メッセージが[希望するタイムゾーン]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters)で送信されることを保証するために、以下の例のようなLiquidタイムゾーンフィルターを使用することを強くお勧めします。

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

## ユースケース {#use-case}

![ウィッシュリストにアイテムを追加したユーザー向けのアクションパスステップ、遅延ステップ、メッセージステップ、およびその他のユーザー向けのパス。]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

`context`と`event_properties`の違いをさらに理解するために、ユーザーがカスタムイベント「ウィッシュリストにアイテムを追加」を実行した場合にアクションベースのキャンバスに入るシナリオを考えてみましょう。

コンテキストはキャンバス作成の[エントリスケジュール]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule)ステップで設定され、ユーザーがキャンバスに入るタイミングに対応します。コンテキストは任意のメッセージステップでも参照できます。

このキャンバスでは、ユーザーがウィッシュリストにアイテムを追加したかどうかを判定するアクションパスステップからユーザージャーニーが始まります。ここで、ユーザーがアイテムを追加した場合、遅延を経てメッセージステップから「ウィッシュリストに新しいアイテムがあります！」というメッセージを受け取ります。

ユーザージャーニーの最初のメッセージステップは、アクションパスステップからのカスタム`event_properties`にアクセスできます。この場合、メッセージコンテンツの一部として、このメッセージステップに``{% raw %} {{event_properties.${property_name}}} {% endraw %}``を含めることができます。ユーザーがウィッシュリストにアイテムを追加しなかった場合、その他のユーザーパスを通過するため、`event_properties`は参照できず、無効な設定エラーが表示されます。

`event_properties`にアクセスできるのは、メッセージステップがアクションパスステップのその他のユーザー以外のパスに遡れる場合のみです。メッセージステップがその他のユーザーパスに接続されていても、ユーザージャーニー内のアクションパスステップに遡れる場合は、`event_properties`にアクセスできます。これらの動作の詳細については、[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を参照してください。