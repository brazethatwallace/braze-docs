{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
標準統合はShopifyオンラインストア向けに設計されており、シームレスで簡単な設定プロセスを提供します。このオプションを使用すると、ShopifyストアをBrazeにすばやく接続でき、高度な技術的専門知識がなくても強力なカスタマーエンゲージメントツールを活用できます。この統合オプションにより、顧客データの同期、パーソナライズされたメッセージングの自動化、包括的なBraze機能によるマーケティング活動の強化が可能になります。

標準のShopify統合を使用するには、[Shopify標準統合の設定]({{site.baseurl}}/shopify_standard_integration/)を参照してください。
{% endtab %}

{% tab custom %}
カスタム統合は、Shopify Hydrogenを使用している場合やヘッドレスストアをサポートしている場合に、より柔軟で構成可能なソリューションを提供します。このオプションにより、Shopify環境に直接Braze SDKを実装して、より深い統合とカスタマイズされた機能を実現できます。独自のカスタマーエクスペリエンスを創出したい場合でも、特定のワークフローを最適化したい場合でも、カスタム統合はヘッドレス環境においてBrazeの機能を最大限に活用するために必要なツールを提供します。

カスタムのShopify統合を使用するには、[Shopifyカスタム統合の設定]({{site.baseurl}}/shopify_custom_integration/)を参照してください。
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == 'Custom external ID historical backfill' %}

カスタムexternal IDを使用して統合する予定の場合（[標準統合]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4)または[カスタム統合]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6)のいずれか）、カスタムexternal IDをShopify顧客メタフィールドとして既存のすべてのShopify顧客プロファイルに追加し、その後に履歴バックフィルを実行する必要があります。

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

[`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)と[プロモーションコード]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/)を組み合わせることで、プロモーションコード情報をCurrentsに送信できます。`capture`タグを使用してプロモーションコードを変数に保存し、その変数を`message_extras`で参照します。

{% raw %}
```liquid
{% capture code %}
{% promotion('puttshacktest2') %}
{% endcapture %}
Use {{code}} for an exclusive discount!
{% message_extras :key cardscode :value {{code}} %}
```
{% endraw %}

{% endif %}