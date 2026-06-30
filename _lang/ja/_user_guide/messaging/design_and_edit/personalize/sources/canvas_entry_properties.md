---
nav_title: Canvasエントリプロパティ
article_title: Canvasエントリプロパティ
page_order: 4
description: "Canvasエントリプロパティをメッセージのパーソナライゼーションソースとして使用する方法を説明します。"
---

# Canvasエントリプロパティ {#canvas-entry-properties}

> Canvasがカスタムイベント、購入、またはAPI呼び出しによってトリガーされると、そのトリガーのメタデータを使用してCanvasワークフロー全体のメッセージをパーソナライズできます。これらの値はエントリプロパティと呼ばれ、Canvas内のすべてのステップにわたって保持されます。

## 仕組み {#how-it-works}

{% raw %}
エントリプロパティは `{{context.${property_name}}}` Liquidタグを通じて利用できます。ユーザーがCanvasにエントリすると、BrazeはトリガーイベントまたはAPI呼び出しからプロパティをキャプチャし、後続の任意のCanvasステップでそれらを参照できます。

たとえば、`product_name` プロパティを持つ `completed_order` イベントによってCanvasがトリガーされた場合:

```liquid
Thanks for ordering {{context.${product_name}}}! We'll send you a tracking number soon.
```
{% endraw %}

エントリプロパティは、アクションベースおよびAPIトリガーのCanvasesで利用できます。

## 永続的なエントリプロパティ {#persistent-entry-properties}

永続的なエントリプロパティを使用すると、遅延後に発生するステップを含め、Canvasのすべてのステップで元のエントリデータを参照できます。永続性がない場合、エントリプロパティは最初のステップでのみ利用可能です。

{% alert important %}
永続的なエントリプロパティは、元のCanvasエントリプロパティワークフローの一部です。現在の更新済みCanvasエディターについては、[コンテキストとイベントプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を参照してください。
{% endalert %}

永続的なエントリプロパティの完全な参照については、[永続的なエントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)を参照してください。