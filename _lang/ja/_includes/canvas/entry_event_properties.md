キャンバスのユーザージャーニーでは、キャンバスエントリプロパティとイベントプロパティを使用できます。

{% tabs local %}
{% tab キャンバスエントリプロパティ %}

[キャンバスエントリプロパティ]({{site.baseurl}}/api/objects_filters/context_object)は、アクションベースまたはAPIトリガーのキャンバスにマップするプロパティです。`canvas_entry_properties` オブジェクトのサイズ上限は 50 KB です。

{% alert note %}
特にアプリ内メッセージチャネルでは、`context` はキャンバス内でのみ参照できます。
{% endalert %}

次のLiquid形式を使用して、任意のメッセージステップで`context`を参照できます: ``{% raw %} context.${property_name} {% endraw %}``。このように使用するには、イベントがカスタムイベントまたは購入イベントである必要があります。

#### ユースケース {#use-case}

{% raw %}
小売店のRetailAppに対して次のリクエストがあるとします: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`。

RetailAppは次のLiquidを使用して、商品名（靴）をメッセージに挿入できます: `{{context.${product_name}}}`。
{% endraw %}

RetailAppは、ユーザーが購入イベントをトリガーした後にターゲットとするキャンバス内で、異なる `product_name` プロパティに対して特定のメッセージをトリガーして送信することもできます。たとえば、次のLiquidをメッセージステップに追加することで、靴を購入したユーザーとそれ以外のものを購入したユーザーに異なるメッセージを送信できます。

{% raw %}
```markdown
{% if  {{context.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details 元のキャンバスエディターの場合 %}

元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは参照のみを目的としています。元のエディターで構築されたキャンバスの場合、キャンバスエントリプロパティはキャンバスの最初のフルステップでのみ参照できます。

{% enddetails %}
{% endtab %}

{% tab イベントプロパティ %}

イベントプロパティとは、カスタムイベントと購入に設定するプロパティを指します。これらの `event_properties` は、アクションベースの配信を使用するキャンペーンやキャンバスで使用できます。

{% alert important %}
キャンバスの最初のメッセージステップでは `event_properties` を使用できません。代わりに、`context` を使用するか、`event_properties` を含むメッセージステップの**前に**、対応するイベントを持つアクションパスステップを追加する必要があります。
{% endalert %}

キャンバスでは、カスタムイベントと購入イベントのプロパティは、アクションパスステップに続く任意のメッセージステップでLiquidを使用して参照できます。これらのイベントプロパティを参照する場合は、必ず {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} を使用してください。メッセージコンポーネントでこのように使用するには、これらのイベントがカスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されたイベントに関連するイベントプロパティを使用できます。ただし、これらのイベントプロパティは、ユーザーが実際にそのアクションを実行した場合（その他のユーザーグループに分類されなかった場合）にのみ使用できます。このアクションパスとメッセージステップの間に、他のステップ（別のアクションパスやメッセージステップではないもの）を配置することもできます。

{% details 元のキャンバスエディターの場合 %}

元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは参照のみを目的としています。元のキャンバスエディターでは、スケジュールされたフルステップでイベントプロパティを使用できません。ただし、アクションベースのキャンバスの最初のフルステップでは、そのステップがスケジュールされていても、イベントプロパティを使用できます。

{% enddetails %}

{% endtab %}
{% endtabs %}

詳細と例については、[キャンバスエントリプロパティとイベントプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)を参照してください。