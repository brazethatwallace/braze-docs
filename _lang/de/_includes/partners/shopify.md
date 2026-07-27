{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
Die Standard-Integration ist auf Shopify-Onlineshops zugeschnitten und bietet einen nahtlosen und unkomplizierten Einrichtungsprozess. Diese Option erlaubt es Ihnen, Ihren Shopify-Shop schnell mit Braze zu verbinden, sodass Sie leistungsstarke Customer-Engagement-Tools nutzen können, ohne über umfangreiche technische Kenntnisse zu verfügen. Mit dieser Integrationsoption können Sie Kundendaten synchronisieren, personalisiertes Messaging automatisieren und Ihre Marketingmaßnahmen durch umfassende Features von Braze verbessern.

Um die standardmäßige Shopify-Integration zu verwenden, lesen Sie bitte [Shopify Standard-Integration einrichten]({{site.baseurl}}/shopify_standard_integration).
{% endtab %}

{% tab custom %}
Die angepasste Integration bietet eine flexiblere und modularere Lösung, wenn Sie Shopify Hydrogen verwenden oder einen Headless-Shop unterstützen. Mit dieser Option können Sie die SDKs von Braze direkt in Ihre Shopify-Umgebung implementieren, was eine tiefere Integration und maßgeschneiderte Funktionalitäten ermöglicht. Ganz gleich, ob Sie einzigartige Kundenerlebnisse schaffen oder bestimmte Arbeitsabläufe optimieren möchten – die angepasste Integration bietet die notwendigen Werkzeuge, um die Möglichkeiten von Braze in einem Headless-Setup voll zu nutzen.

Um die angepasste Shopify-Integration zu verwenden, lesen Sie bitte [Shopify angepasste Integration einrichten]({{site.baseurl}}/shopify_custom_integration).
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == 'Custom external ID historical backfill' %}

Wenn Sie eine Integration mit einer angepassten externen ID planen (entweder für die [Standard-Integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#step-4) oder die [angepasste Integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration#step-6)), müssen Sie Ihre angepasste externe ID als Shopify-Kund:innen-Metafeld zu allen bestehenden Shopify-Kundenprofilen hinzufügen und anschließend den historischen Backfill durchführen.

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

Sie können [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras) mit [Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) kombinieren, um Informationen zu Aktionscodes an Currents zu senden. Verwenden Sie den `capture`-Tag, um den Aktionscode in einer Variablen zu speichern, und referenzieren Sie diese Variable dann in `message_extras`:

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