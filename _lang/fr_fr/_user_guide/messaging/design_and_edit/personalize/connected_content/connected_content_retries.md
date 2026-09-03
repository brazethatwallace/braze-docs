---
nav_title: Nouvelles tentatives de Contenu connecté
article_title: Nouvelles tentatives de Contenu connecté
page_order: 5
description: "Cet article de référence explique comment gérer les nouvelles tentatives de Contenu connecté."

---

# Utiliser une logique de nouvelles tentatives pour le Contenu connecté {#use-retry-logic-for-connected-content}

> Cette page explique comment ajouter des nouvelles tentatives à vos appels de Contenu connecté.

## Fonctionnement des nouvelles tentatives {#how-retries-work}

Étant donné que le contenu connecté repose sur la réception de données provenant d'API, une API peut être temporairement indisponible au moment où Braze effectue l'appel. Dans ce cas, Braze prend en charge une logique de nouvelles tentatives pour relancer la requête en utilisant des délais exponentiels.

{% alert note %}
Le `:retry` du contenu connecté n'est pas disponible pour les messages in-app.
{% endalert %}

## Utiliser la logique de nouvelle tentative {#using-retry-logic}

Pour utiliser la logique de nouvelle tentative, ajoutez l'étiquette `:retry` à l'appel de contenu connecté, comme illustré dans l'extrait de code suivant :

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Lorsqu'une étiquette `:retry` est incluse dans l'appel de contenu connecté, Braze tente de relancer l'appel jusqu'à cinq fois.

### Comportement en prévisualisation {#preview-behavior}

La logique de nouvelle tentative s'applique uniquement aux envois en direct (y compris les envois de test), et non aux prévisualisations. Si un appel de contenu connecté avec `:retry` échoue lors de la prévisualisation, celle-ci peut afficher le message « This message would not have been shown because retry functionality was triggered » au lieu de rendre le contenu. Il s'agit d'un comportement attendu qui n'indique pas un problème au sein de Braze.

### Résultats des nouvelles tentatives {#retry-outcomes}

#### Lorsqu'une nouvelle tentative réussit {#when-a-retry-succeeds}

Si une tentative relancée aboutit, le message est envoyé et aucune nouvelle tentative supplémentaire n'est effectuée pour ce message.

#### Lorsque l'appel API échoue et que les nouvelles tentatives sont activées {#when-the-api-call-fails-and-retries-are-enabled}

Si l'appel API échoue et que cette fonctionnalité est activée, Braze relancera l'appel en respectant la [limitation du débit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) que vous avez définie pour chaque renvoi. Braze déplacera les messages ayant échoué à la fin de la file d'attente et ajoutera des minutes supplémentaires, si nécessaire, au temps total nécessaire pour envoyer votre message.

Si l'appel de contenu connecté échoue plus de cinq fois, le message est abandonné, de manière similaire au déclenchement d'une [étiquette d'abandon de message]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content).

{% multi_lang_include connected_content/abort_and_retry_logic.md %}