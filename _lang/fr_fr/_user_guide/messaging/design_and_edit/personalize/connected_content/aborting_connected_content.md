---
nav_title: Abandon du Contenu connecté
article_title: Abandon du Contenu connecté
page_order: 2
description: "Cet article de référence présente les bonnes pratiques pour abandonner des messages avec le Contenu connecté."
---

# Abandon du Contenu connecté {#aborting-connected-content}

> Lorsque vous utilisez le templating Liquid, vous avez la possibilité d'abandonner des messages grâce à la logique conditionnelle. Cette page présente les bonnes pratiques à suivre dans ce cas.

Dans l'exemple suivant, les conditions `connected.recommendations.size < 5` et `connected.foo.bar == nil` définissent les situations dans lesquelles le message sera abandonné.

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## Spécifier une raison d'abandon

Vous pouvez également spécifier une raison d'abandon, qui sera enregistrée dans le [Journal d'activité des messages]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/). Cette raison d'abandon doit être une chaîne de caractères et ne peut pas contenir de Liquid.

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Braze ne comptabilise pas les messages abandonnés dans le nombre d'envois de votre compte Braze ni dans Currents.
{% endalert %}

{% multi_lang_include connected_content/abort_and_retry_logic.md %}