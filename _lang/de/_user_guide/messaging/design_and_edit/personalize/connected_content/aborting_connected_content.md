---
nav_title: Connected-Content abbrechen
article_title: Connected-Content abbrechen
page_order: 2
description: "Dieser Referenzartikel behandelt einige Best Practices zum Abbrechen von Nachrichten bei Connected-Content."
---

# Connected-Content abbrechen {#aborting-connected-content}

> Wenn Sie Liquid-Templating verwenden, haben Sie die Möglichkeit, Nachrichten mit bedingter Logik abzubrechen. Diese Seite behandelt Best Practices dabei.

Im folgenden Beispiel geben die Bedingungen `connected.recommendations.size < 5` und `connected.foo.bar == nil` Situationen an, in denen die Nachricht abgebrochen wird.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Einen Abbruchgrund angeben

Sie können auch einen Abbruchgrund angeben, der im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/) gespeichert wird. Dieser Abbruchgrund muss ein String sein und darf kein Liquid enthalten.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze zählt abgebrochene Nachrichten nicht zur Sendeanzahl in Ihrem Braze-Konto oder in Currents.
{% endalert %}

{% multi_lang_include connected_content/abort_and_retry_logic.md %}