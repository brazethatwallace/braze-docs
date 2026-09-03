---
nav_title: "Types d'identifiant API"
article_title: "Types d'identifiant API"
page_order: 2.2
toc_headers: h2
description: "Cet article de référence traite des différents types d'identifiants API qui existent dans le tableau de bord de Braze, de l'endroit où vous pouvez les trouver et de leur utilité."
page_type: reference
---

# Types d'identifiant API {#api-identifier-types}

> Ce guide de référence aborde les différents types d'identifiants API que vous trouverez dans le tableau de bord de Braze, leur but, où vous pouvez les trouver et comment ils sont généralement utilisés. Pour plus d'informations sur les clés API REST ou les clés API de l'espace de travail, reportez-vous à l'[aperçu de l'API]({{site.baseurl}}/api/basics).

Les identifiants suivants peuvent être utilisés pour accéder à votre modèle, Canvas, Campaign ou Segment à partir de l'API externe de Braze. Tous les messages doivent respecter le codage [UTF-8](https://en.wikipedia.org/wiki/UTF-8).

## Identifiant d'application {#app-identifier}

L'identifiant d'application ou `app_id` est un paramètre qui associe l'activité à une application spécifique dans votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. Par exemple, vous pouvez avoir un `app_id` pour votre application iOS, un `app_id` pour votre application Android et un `app_id` pour votre intégration web. Chez Braze, vous pouvez avoir plusieurs applications pour la même plateforme parmi les différents types de plateformes pris en charge par Braze.

### Où le trouver ? {#where-can-i-find-it}

Il existe deux façons de localiser votre `app_id` :

{% tabs local %}
{% tab Identifiants d'application %}
Allez dans **Paramètres** > **API et identifiants** > **Identifiants d'application**. Votre clé API pour chaque application est répertoriée dans la colonne **Identifiant**.
{% endtab %}

{% tab Paramètres de l'application %}
Allez dans **Paramètres** > **Paramètres de l'application**. Votre clé API est indiquée à côté du champ **Clé API** dans la section des paramètres.

{% endtab %}
{% endtabs %}

### À quoi sert-il ? {#what-can-it-be-used-for}

Les identifiants d'application chez Braze sont utilisés lors de l'intégration du SDK et servent également à référencer une application spécifique dans les appels REST API. Avec l'`app_id`, vous pouvez effectuer de nombreuses actions, comme récupérer des données pour un événement personnalisé survenu pour une application particulière, obtenir des statistiques de désinstallation, de nouveaux utilisateurs, d'utilisateurs actifs par jour et de démarrage de session pour une application donnée.

{% alert tip %}
Il peut arriver que l'on vous demande un `app_id` alors que vous ne travaillez pas avec une application, car il s'agit d'un champ hérité spécifique à une plateforme particulière. Dans ce cas, vous pouvez omettre ce champ en incluant n'importe quelle chaîne de caractères comme marque substitutive pour ce paramètre obligatoire.
{% endalert %}

### Identifiants d'application multiples {#multiple-app-identifiers}

Lors de la configuration du SDK, le cas d'usage le plus courant pour les identifiants d'application multiples est de séparer ces identifiants pour les variantes de build de débogage et de production.

Pour basculer facilement entre plusieurs identifiants d'application dans vos builds, nous recommandons de créer un fichier `braze.xml` distinct pour chaque [variante de build](https://developer.android.com/studio/build/build-variants.html) pertinente. Une variante de build est une combinaison de type de build et de saveur de produit. Par défaut, un nouveau projet Android est configuré avec les types de build `debug` et `release` et aucune saveur de produit.

Pour chaque variante de build pertinente, créez un nouveau fichier `braze.xml` dans `src/<build variant name>/res/values/` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Lorsque la variante de build est compilée, elle utilise le nouvel identifiant.

## Identifiant de modèle {#template-identifier}

Un identifiant de [modèle]({{site.baseurl}}/api/endpoints/templates) ou ID de modèle est une clé aléatoire générée par Braze pour un modèle donné dans le tableau de bord. Les ID de modèle sont uniques pour chaque modèle et peuvent être utilisés pour référencer des modèles via l'API.

Les modèles sont très utiles si votre entreprise externalise la conception HTML de ses Campaigns. Une fois les modèles créés, vous disposez d'un modèle qui n'est pas spécifique à une Campaign mais qui peut être appliqué à une série de Campaigns, comme une newsletter.

### Où le trouver ?

Vous pouvez trouver votre ID de modèle de deux façons :

{% tabs local %}
{% tab Modèles %}
Accédez à **Modèles**, sélectionnez une page de modèle, puis sélectionnez un modèle préexistant. Si le modèle souhaité n'existe pas encore, créez-en un et enregistrez-le. En bas de la page du modèle individuel, vous trouverez votre identifiant de modèle.
{% endtab %}

{% tab Clés API %}
Accédez à **Paramètres** > **API et identifiants**. Braze propose ici une recherche d'**identifiants API supplémentaires** où vous pouvez rechercher des identifiants spécifiques.

{% endtab %}
{% endtabs %}

### À quoi peut-il servir ?

- Mettre à jour des modèles via l'API
- Récupérer des informations sur un modèle spécifique

## Identifiant Canvas {#canvas-identifier}

Un identifiant [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) ou Canvas ID est une clé aléatoire générée par Braze pour un Canvas donné au sein du tableau de bord. Les Canvas ID sont uniques pour chaque Canvas et peuvent être utilisés pour référencer les Canvas via l'API.

Gardez à l'esprit que si vous avez un Canvas qui comporte des variantes, il existe un Canvas ID global ainsi que des Canvas ID de variantes individuelles imbriqués sous le Canvas principal.

### Où le trouver ?

Vous pouvez trouver votre Canvas ID dans le tableau de bord. Accédez à **Messaging** > **Canvas** et sélectionnez un Canvas existant. Si le Canvas souhaité n'existe pas encore, créez-en un et enregistrez-le. En bas de la page d'un Canvas individuel, cliquez sur **Analyze Variants**. Une fenêtre apparaît avec l'identifiant API du Canvas situé en bas.

### À quoi peut-il servir ?

- Suivre l'analyse d'un message spécifique
- Obtenir des statistiques agrégées de haut niveau sur les performances d'un Canvas
- Obtenir des détails sur un Canvas spécifique
- Avec Currents, pour intégrer des données au niveau de l'utilisateur dans une approche « vue d'ensemble » des Canvas
- Avec la distribution déclenchée par API, pour collecter des statistiques sur les messages transactionnels

## Identifiant de Campaign {#campaign-identifier}

Un identifiant de [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou ID de Campaign est une clé aléatoire générée par Braze pour une Campaign donnée dans le tableau de bord. Les ID de Campaign sont uniques pour chaque Campaign et peuvent être utilisés pour référencer les Campaigns via l'API.

Gardez à l'esprit que si vous avez une Campaign avec des variantes, il existe à la fois un ID de Campaign global ainsi que des ID de Campaign individuels pour chaque variante, imbriqués sous la Campaign principale.

### Où le trouver ?

Vous pouvez trouver votre ID de Campaign de deux manières :

{% tabs local %}
{% tab Campaigns %}
Accédez à **Messaging** > **Campaigns** et sélectionnez une Campaign existante. Si la Campaign souhaitée n'existe pas encore, créez-en une et enregistrez-la. En bas de la page de la Campaign, vous trouverez votre **Campaign API Identifier**.

{% endtab %}

{% tab API Keys %}
Accédez à **Settings** > **APIs and Identifiers**. Braze propose ici une recherche **Additional API Identifiers** où vous pouvez rechercher des identifiants spécifiques.

{% endtab %}
{% endtabs %}

### À quoi peut-il servir ?

- Suivre l'analyse d'un message spécifique
- Obtenir des statistiques agrégées de haut niveau sur les performances d'une Campaign
- Obtenir des détails sur une Campaign spécifique
- Avec Currents, pour intégrer des données au niveau de l'utilisateur dans une approche « vue d'ensemble » des Campaigns
- Avec la distribution déclenchée par API, pour collecter des statistiques sur les messages transactionnels
- Pour [rechercher une Campaign spécifique]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns) sur la page **Campaigns** en utilisant le filtre `api_id:YOUR_API_ID`

## Identifiant de segment {#segment-identifier}

Un identifiant de [segment]({{site.baseurl}}/user_guide/audience/segments), ou segment ID, est une clé aléatoire générée par Braze pour un segment donné dans le tableau de bord. Les identifiants de segment sont uniques pour chaque segment et peuvent être utilisés pour référencer des segments via l'API.

### Où le trouver ?

Vous pouvez trouver votre identifiant de segment de deux manières :

{% tabs local %}
{% tab Segments %}
Allez dans **Audience** > **Segments** et sélectionnez un segment existant. Si le segment souhaité n'existe pas encore, créez-en un et enregistrez-le. En bas de la page individuelle du segment, vous trouverez votre identifiant de segment.

{% endtab %}

{% tab Clés API %}
Allez dans **Paramètres** > **API et identifiants**. Braze propose ici une recherche d'**identifiants API supplémentaires** qui vous permet de rechercher des identifiants spécifiques.

{% endtab %}
{% endtabs %}

### À quoi sert-il ?

- Obtenir des détails sur un segment spécifique
- Récupérer les données analytiques d'un segment spécifique
- Déterminer combien de fois un événement personnalisé a été enregistré pour un segment particulier
- Spécifier et envoyer une Campaign aux membres d'un segment via l'API

## Identifiant d'envoi {#send-identifier}

Un identifiant d'envoi, ou send ID, est une clé générée par Braze ou créée par vous pour un envoi de message donné, sous laquelle les analyses sont suivies. L'identifiant d'envoi vous permet de récupérer les analyses d'une instance spécifique d'un envoi de Campaign via l'[endpoint `/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics).

### Où le trouver ?

Les Campaigns déclenchées par API et envoyées en tant que diffusion génèrent automatiquement un identifiant d'envoi si aucun n'est fourni. Si vous souhaitez spécifier votre propre identifiant d'envoi, vous devez d'abord en créer un via l'[endpoint `/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids). L'identifiant doit être composé exclusivement de caractères ASCII et ne doit pas dépasser 64 caractères. Vous pouvez réutiliser un identifiant d'envoi pour plusieurs envois d'une même Campaign si vous souhaitez regrouper les analyses de ces envois.

### À quoi sert-il ?
Envoyez et suivez les performances des messages de manière programmatique, sans avoir à créer de Campaign pour chaque envoi.

## Identifiant de groupe d'abonnement {#subscription-group-identifier}

Un identifiant de groupe d'abonnement, ou ID de groupe d'abonnement, est une clé générée par Braze pour un groupe d'abonnement donné. Les ID sont uniques pour chaque groupe d'abonnement et peuvent être utilisés pour référencer les groupes d'abonnement via l'API.

### Où le trouver ?

Accédez à **Audience** > **Subscriptions** et copiez l'ID à côté du groupe d'abonnement concerné.

### À quoi peut-il servir ?

- Lister les groupes d'abonnement d'un utilisateur
- Récupérer le statut du groupe d'abonnement d'un utilisateur
- Mettre à jour le statut du groupe d'abonnement d'un utilisateur