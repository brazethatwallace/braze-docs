---
nav_title: Nouvelles tentatives de Contenu connecté
article_title: Nouvelles tentatives de Contenu connecté
page_order: 5
description: "Cet article de référence explique comment gérer les nouvelles tentatives de Contenu connecté."

---

# Utiliser une logique de nouvelles tentatives pour le Contenu connecté

> Cette page explique comment ajouter des nouvelles tentatives à vos appels de Contenu connecté.

## Fonctionnement des nouvelles tentatives

Étant donné que le Contenu connecté repose sur la réception de données provenant d'API, une API peut être temporairement indisponible au moment où Braze effectue l'appel. Dans ce cas, Braze prend en charge une logique de nouvelles tentatives pour relancer la requête en utilisant des délais exponentiels.

{% alert note %}
Le paramètre `:retry` du Contenu connecté n'est pas disponible pour les messages in-app.
{% endalert %}

## Utiliser la logique de nouvelles tentatives

Pour utiliser la logique de nouvelles tentatives, ajoutez l'étiquette `:retry` à l'appel de Contenu connecté, comme illustré dans l'extrait de code suivant :

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Lorsqu'une étiquette `:retry` est incluse dans l'appel de Contenu connecté, Braze tentera de relancer l'appel jusqu'à cinq fois.

### Résultats des nouvelles tentatives

#### Lorsqu'une nouvelle tentative réussit

Si une nouvelle tentative aboutit, le message est envoyé et aucune autre tentative n'est effectuée pour ce message.

#### Lorsque l'appel API échoue et que les nouvelles tentatives sont activées

Si l'appel API échoue et que cette option est activée, Braze relancera l'appel en respectant la [limite de débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#delivery-speed-rate-limiting) que vous avez définie pour chaque renvoi. Braze déplacera les messages en échec à la fin de la file d'attente et ajoutera des minutes supplémentaires, si nécessaire, au temps total nécessaire pour envoyer votre message.

Si l'appel de Contenu connecté échoue plus de cinq fois, le message est abandonné, de manière similaire au déclenchement d'une [étiquette d'abandon de message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content/).

{% multi_lang_include connected_content/abort_and_retry_logic.md %}