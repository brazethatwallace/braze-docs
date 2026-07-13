---
nav_title: API REST
article_title: API REST
page_order: 1
description: "Découvrez comment utiliser le contenu connecté pour extraire des données d'API REST dans vos messages et personnaliser en temps réel."
---

# API REST {#rest-api}

> Extrayez des données d'API REST externes directement dans vos messages au moment de l'envoi grâce au [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Vous pouvez ainsi personnaliser vos messages avec des informations en temps réel provenant de vos propres serveurs, de services tiers ou de tout endpoint d'API accessible publiquement.

## Fonctionnement {#how-it-works}

{% raw %}
Le contenu connecté effectue une requête HTTP vers l'URL que vous spécifiez, puis stocke la réponse afin que vous puissiez la référencer avec Liquid. Ajoutez une balise `{% connected_content %}` à votre message, et Braze appelle l'endpoint au moment de l'envoi du message.

```liquid
{% connected_content https://api.example.com/user/{{${user_id}}}/recommendations :save recs %}
We think you'll love {{recs.top_pick}}!
```
{% endraw %}

Le contenu connecté prend en charge les requêtes GET et POST. Braze exige que le serveur réponde dans un délai de deux secondes ; concevez donc vos endpoints pour une faible latence.

## Cas d'utilisation courants {#common-use-cases}

| Cas d'utilisation | Description |
| --- | --- |
| Recommandations produit | Récupérer des suggestions de produits personnalisées depuis un moteur de recommandation |
| Tarifs ou inventaire en temps réel | Afficher les prix actuels ou les niveaux de stock au moment de l'envoi |
| Contenu basé sur la météo | Extraire les données météo locales pour adapter les messages |
| Soldes de points de fidélité | Afficher les récompenses ou soldes de compte à jour |
| Flux de contenu | Insérer les derniers articles de blog, publications ou actualités |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cas d'utilisation courants" }

## Authentification {#authentication}

Braze prend en charge l'authentification basique, l'authentification par jeton et OAuth pour les requêtes de contenu connecté. Vous pouvez stocker vos identifiants de manière sécurisée dans le tableau de bord de Braze sous **Paramètres** > **Contenu connecté** et les référencer dans vos appels API.

Pour en savoir plus, consultez [Effectuer un appel API de contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types).

## Gestion des erreurs {#error-handling}

Si l'endpoint renvoie une erreur ou dépasse le délai d'attente, Braze affiche une chaîne de caractères vide à la place de la réponse du contenu connecté. Vous pouvez détecter les échecs en vérifiant si la variable enregistrée est nulle, puis annuler conditionnellement le message ou afficher un contenu de secours.

Pour en savoir plus, consultez [Annuler le contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content).

## Considérations de performance {#performance-considerations}

Étant donné que Braze envoie des messages en très grand volume, votre serveur doit être capable de gérer des milliers de connexions simultanées. Utilisez la mise en cache lorsque c'est pertinent et définissez des limites de débit sur vos messages pour éviter de surcharger les endpoints externes.

Pour la référence complète du contenu connecté, consultez [Contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).