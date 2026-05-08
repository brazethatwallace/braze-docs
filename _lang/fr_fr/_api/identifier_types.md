---
nav_title: "Types d'identifiant API"
article_title: Types d'identifiant API
page_order: 2.2
toc_headers: h2
description: "Cet article de référence traite des différents types d'identifiants API qui existent dans le tableau de bord de Braze, de l'endroit où vous pouvez les trouver et de leur utilité."
page_type: reference

---

# Types d'identifiant API {#api-identifier-types}

> Ce guide de référence aborde les différents types d'identifiants API que vous trouverez dans le tableau de bord de Braze, leur but, où vous pouvez les trouver et comment ils sont généralement utilisés. Pour plus d'informations sur les clés API REST ou les clés API de l'espace de travail, reportez-vous à l'[aperçu de l'API]({{site.baseurl}}/api/api_key/).

Les identifiants suivants peuvent être utilisés pour accéder à votre modèle, Canvas, Campaign ou Segment à partir de l'API externe de Braze. Tous les messages doivent respecter le codage [UTF-8](https://en.wikipedia.org/wiki/UTF-8).

## Identifiant de l'application {#app-identifier}

L'identifiant de l'application ou `app_id` est un paramètre qui associe l'activité à une application spécifique dans votre espace de travail. Il désigne l'application avec laquelle vous interagissez au sein de l'espace de travail. Par exemple, vous constatez que vous avez un `app_id` pour votre application iOS, un `app_id` pour votre application Android et un `app_id` pour votre intégration web. Chez Braze, il se peut que vous disposiez de plusieurs applications pour la même plateforme sur les différents types de plateformes que Braze prend en charge.

### Où puis-je le trouver ? {#where-can-i-find-it}

Il existe deux façons de localiser votre `app_id` :

{% tabs local %}
{% tab App Identifiers %}
Allez dans **Settings** > **APIs and Identifiers** > **App Identifiers**. Votre clé API pour chaque application est indiquée dans la colonne **Identifier**.
{% endtab %}

{% tab App Settings %}
Allez dans **Settings** > **App Settings**. Votre clé API est indiquée à côté du champ **API Key** dans la section des paramètres.

{% endtab %}
{% endtabs %}

### À quoi cela sert-il ? {#what-can-it-be-used-for}

Les identifiants d'application chez Braze sont utilisés lors de l'intégration du SDK et pour référencer une application spécifique dans les appels REST API. Avec le `app_id`, vous pouvez faire de nombreuses choses comme extraire des données pour un événement personnalisé qui s'est produit pour une application particulière, récupérer les statistiques de désinstallation, les statistiques de nouveaux utilisateurs, les statistiques d'utilisateur actif quotidien et les statistiques de début de session pour une application particulière.

{% alert tip %}
Il peut arriver que l'on vous demande un `app_id`, mais que vous ne travailliez pas avec une application, car il s'agit d'un champ hérité spécifique à une plateforme donnée. Vous pouvez omettre ce champ en incluant n'importe quelle chaîne de caractères comme marque substitutive pour ce paramètre obligatoire.
{% endalert %}

### Identifiants d'application multiples {#multiple-app-identifiers}

Lors de la configuration du SDK, le cas d'usage le plus fréquent avec les identifiants d'application multiples est de séparer ces identifiants entre les variantes de version de débogage et de publication.

Pour basculer facilement entre plusieurs identifiants d'application dans vos builds, nous vous recommandons de créer un fichier `braze.xml` distinct pour chaque [variante de build](https://developer.android.com/studio/build/build-variants.html) pertinente. Une variante de build est une combinaison du type de build et de la variété du produit. Par défaut, un nouveau projet Android est configuré avec les types de build `debug` et `release` et aucune variété de produit.

Pour chaque variante de build pertinente, créez un nouveau `braze.xml` dans `src/<build variant name>/res/values/` :

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Lorsque la variante est compilée, elle utilise le nouvel identifiant.

## Identifiant du modèle {#template-identifier}

Un identifiant de [modèle]({{site.baseurl}}/api/endpoints/templates/) ou ID de modèle est une clé aléatoire générée par Braze pour un modèle donné au sein du tableau de bord. Les ID de modèle sont uniques pour chaque modèle et peuvent être utilisés pour référencer les modèles via l'API.

Les modèles sont très utiles si votre entreprise sous-traite vos conceptions HTML pour des campagnes. Une fois les modèles créés, vous disposez d'un modèle qui n'est pas spécifique à une campagne mais qui peut être appliqué à une série de campagnes, comme une lettre d'information.

### Où puis-je le trouver ? {#where-can-i-find-it}

Vous pouvez trouver l'ID de votre modèle de deux façons :

{% tabs local %}
{% tab Templates %}
Allez dans **Templates**, sélectionnez une page de modèle, puis choisissez un modèle préexistant. Si le modèle que vous voulez n'existe pas encore, créez-en un et enregistrez-le. Au bas de la page du modèle individuel, vous trouverez l'identifiant de votre modèle.
{% endtab %}

{% tab API Keys %}
Allez dans **Settings** > **APIs and Identifiers**. Ici, Braze propose une recherche d'**Additional API Identifiers** qui vous permet de rechercher des identifiants spécifiques.

{% endtab %}
{% endtabs %}

### À quoi cela sert-il ? {#what-can-it-be-used-for}

- Mettre à jour les modèles à l'aide de l'API
- Obtenir des informations sur un modèle spécifique

## Identifiant Canvas {#canvas-identifier}

Un identifiant [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/) ou ID Canvas est une clé aléatoire générée par Braze pour un Canvas donné au sein du tableau de bord. Les ID Canvas sont uniques pour chaque Canvas et peuvent être utilisés pour référencer des Canvas via l'API.

Gardez à l'esprit que si vous avez un Canvas avec des variantes, il existe un ID global pour le Canvas ainsi que des ID individuels pour les variantes, imbriqués dans le Canvas principal.

### Où puis-je le trouver ? {#where-can-i-find-it}

Vous pouvez trouver votre ID Canvas dans le tableau de bord. Allez dans **Messaging** > **Canvas** et sélectionnez un Canvas préexistant. Si le Canvas que vous voulez n'existe pas encore, créez-en un et enregistrez-le. En bas d'une page individuelle de Canvas, cliquez sur **Analyze Variants**. Une fenêtre apparaît avec l'identifiant API Canvas situé en bas.

### À quoi cela sert-il ? {#what-can-it-be-used-for}

- Suivre l'analyse d'un message spécifique
- Obtenir des statistiques globales de haut niveau sur les performances du Canvas
- Obtenir des informations sur un Canvas spécifique
- Avec Currents pour apporter des données au niveau de l'utilisateur pour une approche plus globale des Canvas
- Avec la réception/distribution déclenchée par l'API pour collecter des statistiques sur les messages transactionnels

## Identifiant de Campaign {#campaign-identifier}

Un identifiant de [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/) ou ID de Campaign est une clé aléatoire générée par Braze pour une Campaign donnée dans le tableau de bord. Les ID de Campaign sont uniques pour chaque Campaign et peuvent être utilisés pour référencer des Campaigns via l'API.

Gardez à l'esprit que si vous avez une Campaign avec des variantes, il y a à la fois un ID de Campaign global et des ID de variante individuels imbriqués sous la Campaign principale.

### Où puis-je le trouver ? {#where-can-i-find-it}

Vous pouvez trouver votre ID de Campaign de deux façons :

{% tabs local %}
{% tab Campaigns %}
Allez dans **Messaging** > **Campaigns** et sélectionnez une Campaign préexistante. Si la Campaign que vous souhaitez n'existe pas encore, créez-en une et enregistrez-la. Au bas de la page de la Campaign individuelle, vous trouverez l'**identifiant API de Campaign**.

{% endtab %}

{% tab API Keys %}
Allez dans **Settings** > **APIs and Identifiers**. Ici, Braze propose une recherche d'**Additional API Identifiers** qui vous permet de rechercher des identifiants spécifiques.

{% endtab %}
{% endtabs %}

### À quoi cela sert-il ? {#what-can-it-be-used-for}

- Suivre l'analyse d'un message spécifique
- Obtenir des statistiques globales de haut niveau sur les performances de la Campaign
- Obtenir des informations sur une Campaign spécifique
- Avec Currents pour apporter des données au niveau de l'utilisateur pour bénéficier d'un « tableau général » des Campaigns
- Avec la réception/distribution déclenchée par l'API pour collecter des statistiques sur les messages transactionnels
- Pour [rechercher une Campaign spécifique]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax) sur la page **Campaigns** à l'aide du filtre `api_id:YOUR_API_ID`

## Identifiant de Segment {#segment-identifier}

Un identifiant de [Segment]({{site.baseurl}}/user_guide/audience/segments/) ou ID de Segment est une clé aléatoire générée par Braze pour un Segment donné au sein du tableau de bord. Les ID de Segment sont uniques pour chaque Segment et peuvent être utilisés pour référencer les Segments via l'API.

### Où puis-je le trouver ? {#where-can-i-find-it}

Vous pouvez trouver votre ID de Segment de deux façons :

{% tabs local %}
{% tab Segments %}
Allez dans **Audience** > **Segments** et sélectionnez un Segment préexistant. Si le Segment que vous voulez n'existe pas encore, créez-en un et enregistrez-le. Au bas de la page du Segment individuel, vous trouverez l'identifiant de votre Segment.

{% endtab %}

{% tab API Keys %}
Allez dans **Settings** > **APIs and Identifiers**. Ici, Braze propose une recherche d'**Additional API Identifiers** qui vous permet de rechercher des identifiants spécifiques.

{% endtab %}
{% endtabs %}

### À quoi cela sert-il ? {#what-can-it-be-used-for}

- Obtenir des informations sur un Segment spécifique
- Récupérer l'analyse d'un Segment spécifique
- Récupérer le nombre de fois où un événement personnalisé a été enregistré pour un Segment particulier
- Spécifier et envoyer une Campaign aux membres d'un Segment à partir de l'API

## Identifiant d'envoi {#send-identifier}

Un identifiant d'envoi, ou ID d'envoi, est une clé générée par Braze ou créée par vous pour un envoi de message donné, sous laquelle l'analyse doit être suivie. L'identifiant d'envoi vous permet d'obtenir des analyses pour une instance spécifique d'un envoi de Campaign via l'[endpoint `/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/).

### Où puis-je le trouver ? {#where-can-i-find-it}

Les Campaigns API et déclenchées par l'API qui sont envoyées en tant que diffusion génèrent automatiquement un identifiant d'envoi si aucun identifiant d'envoi n'est fourni. Si vous souhaitez spécifier votre propre identifiant d'envoi, vous devez d'abord en créer un via l'[endpoint `/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/). L'identifiant ne peut comporter que des caractères ASCII et ne peut faire plus de 64 caractères. Vous pouvez réutiliser un identifiant d'envoi sur plusieurs envois de la même Campaign si vous souhaitez regrouper les analyses de ces envois.

### À quoi cela sert-il ? {#what-can-it-be-used-for}
Envoyer et suivre par programme les performances des messages, sans création de Campaign pour chaque envoi.

## Identifiant du groupe d'abonnement {#subscription-group-identifier}

Un identifiant de groupe d'abonnement, ou ID de groupe d'abonnement, est une clé générée par Braze pour un groupe d'abonnement donné. Les ID sont uniques à chaque groupe d'abonnement et peuvent être utilisés pour référencer les groupes d'abonnement via l'API.

### Où puis-je le trouver ? {#where-can-i-find-it}

Allez dans **Audience** > **Subscriptions** et copiez l'ID à côté du groupe d'abonnement concerné.

### À quoi cela sert-il ? {#what-can-it-be-used-for}

- Lister les groupes d'abonnement d'un utilisateur
- Obtenir le statut du groupe d'abonnement d'un utilisateur
- Mettre à jour le statut du groupe d'abonnement d'un utilisateur