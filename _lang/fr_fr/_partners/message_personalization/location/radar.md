---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "Cet article de référence présente le partenariat entre Braze et Radar, une plateforme de géorepérage permettant d'ajouter un contexte de localisation et un suivi à vos applications iOS et Android."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.radar.com/) est la principale plateforme de géorepérage et de suivi de localisation. La plateforme Radar comprend trois produits principaux : [Geofences](https://radar.com/product/geofencing), [Trip Tracking](https://radar.com/product/trip-tracking) et [Geo APIs](https://radar.com/product/api). La combinaison de la plateforme d'engagement Braze, leader du secteur, et des capacités de géorepérage de Radar, également leader du secteur, vous permet de générer du chiffre d'affaires et de la fidélisation grâce à un large éventail d'expériences de produits et de services basées sur la localisation. Il s'agit notamment du suivi des retraits et livraisons, des notifications déclenchées en fonction de l'emplacement, de la personnalisation contextuelle, de la vérification de l'emplacement, des localisateurs de magasins, de la saisie semi-automatique des adresses, et bien plus encore.

_Cette intégration est assurée par Radar._

## À propos de l'intégration {#about-the-integration}

L'intégration de Braze et Radar vous permet d'accéder à des déclencheurs de campagne sophistiqués basés sur la localisation et à l'enrichissement du profil utilisateur grâce à des données de localisation riches et propriétaires. Lorsque des événements de géorepérage ou de suivi de trajet Radar sont générés, des événements personnalisés et des attributs utilisateur sont envoyés à Braze en temps réel. Ces événements et attributs peuvent ensuite être utilisés pour déclencher des campagnes basées sur la localisation, alimenter les opérations de retrait et de livraison sur le dernier kilomètre, surveiller la logistique des flottes et des expéditions, ou créer des segments d'utilisateurs basés sur des modèles de localisation.

De plus, les API Radar Geo peuvent être utilisées pour enrichir ou personnaliser vos campagnes marketing grâce au [contenu connecté]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Radar | Un compte Radar est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec les autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Identifiant de l'application | L'[identifiant de votre application]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) se trouve dans le tableau de bord de Braze sous **Paramètres** > **Clés API**. |
| Clé API iOS<br>Clé API Android | Ces clés API se trouvent dans le tableau de bord de Braze sous **Paramètres** > **Paramètres des applications**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Intégration {#integration}

Pour mapper les données entre les SDK Braze et Radar, vous devez définir les mêmes ID utilisateur ou alias d'utilisateur dans les deux systèmes. Pour ce faire, vous pouvez utiliser la méthode `changeUser()` du SDK Braze et la méthode `setUserId()` du SDK Radar.

Pour activer l'intégration :

1. Dans Radar, recherchez Braze sur la page [Integrations](https://radar.com/documentation/integrations).
1. Réglez l'option **Enabled** sur **Yes**.
3. Collez l'identifiant de votre application et les clés API.

{% alert note %}
Vous pouvez définir des clés API distinctes pour les environnements de test et de production.
{% endalert %}

{:start="4"}
4. Sélectionnez votre endpoint Braze.
5. Saisissez tout filtrage d'événement ou d'attribut d'événement pour vous assurer que seules les données pertinentes sont envoyées à Braze pour le marketing d'engagement. Lorsque des événements Radar sont générés, Radar envoie des événements personnalisés et des attributs utilisateur à Braze. Les événements provenant d'appareils iOS seront envoyés à l'aide de vos clés API iOS ; les événements et les attributs utilisateur provenant d'appareils Android seront envoyés à l'aide de vos clés API Android.

{% alert note %}
Par défaut, le paramètre `userId` de Radar correspond au paramètre `external_id` de Braze pour les utilisateurs connectés. Cependant, vous pouvez suivre les utilisateurs déconnectés ou spécifier des mappages personnalisés en définissant le paramètre `metadata.brazeAlias` ou `metadata.brazeExternalId` dans Radar. Si vous définissez `metadata.brazeAlias`, vous devez également ajouter un alias correspondant dans Braze avec le libellé `radarAlias`.
{% endalert %}

## Cas d'utilisation basés sur les événements et les attributs {#event-and-attribute-based-use-cases}

Vous pouvez utiliser des événements personnalisés et des attributs utilisateur pour créer des segments basés sur la localisation ou déclencher des campagnes basées sur la localisation.

### Déclencher une notification d'arrivée en magasin pour le retrait en bordure de rue {#trigger-a-store-arrival-notification-for-curbside-pickup}

Envoyez une notification push à l'utilisateur avec des instructions d'arrivée lorsqu'il arrive dans votre magasin pour un retrait en bordure de rue.

![Une campagne de livraison par événement indiquant que la campagne sera livrée lorsque l'événement personnalisé « arrived_at_trip_destination » se produit et que « trip_metadata » est égal à « curbside ».]({% image_buster /assets/img_archive/radar-campaign.png %})

### Créer un segment d'audience composé des visiteurs récents de votre magasin {#build-an-audience-segment-of-recent-store-visitors}

Par exemple, ciblez tous les utilisateurs qui ont visité votre magasin au cours des 7 derniers jours, qu'ils aient effectué un achat ou non.

![Un segment où « radar_geofence_tags » comprend la valeur my_store et « radar_updated_at » date de moins de 7 jours.]({% image_buster /assets/img_archive/radar-segment.png %})

## Contenu connecté {#connected-content}

L'exemple suivant montre comment mettre en place une promotion pour inciter les utilisateurs à proximité à se rendre en magasin grâce à une offre numérique.

![Image Android d'un message push de contenu connecté affichant « New In Store Deals, Walmart and Target near you ».]({% image_buster /assets/img/radar_example.png %}){: style="float:right;max-width:30%;border:0;"}

Pour commencer, vous devez disposer de votre clé API publiable Radar, que vous utiliserez dans vos URL de requête.

Ensuite, dans une balise `connected_content`, effectuez une requête GET vers l'[API Search Places](https://radar.com/documentation/api#search-places). L'API Search Places renvoie les emplacements à proximité en se basant sur [Radar Places](https://radar.com/documentation/places) : une base de données d'emplacements pour les lieux, les chaînes et les catégories qui offre une vue d'ensemble du monde.

L'extrait de code suivant est un exemple de ce que Radar renverra sous forme d'objet JSON à partir de l'appel API :

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

Pour construire le message Braze ciblé et personnalisé avec du contenu connecté, vous pouvez utiliser l'attribut `most_recent_location` de Braze comme entrée pour le paramètre `near` dans l'URL de la requête API. L'attribut `most_recent_location` est collecté via l'intégration des événements Radar ou directement via le SDK Braze.

Dans l'exemple suivant, le filtrage par chaîne Radar est appliqué aux emplacements Target et Walmart, et le rayon de recherche des emplacements proches est fixé à 2 km.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

Comme vous pouvez le voir dans la balise `connect_content`, l'objet JSON est stocké dans la variable locale `nearbyplaces` en ajoutant `:save nearbyplaces` après l'URL.
Vous pouvez tester la sortie en vous référant à {% raw %}`{{nearbyplaces.places}}`{% endraw%}.

Pour mettre en œuvre notre cas d'utilisation, voici à quoi ressemblerait la syntaxe de la campagne. Le code suivant parcourt l'objet `nearbyplaces.places`, extrait les valeurs uniques et les concatène avec des délimiteurs lisibles pour le message.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }}
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }}
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
Consultez la [documentation Radar](https://radar.com/documentation/api) pour découvrir toutes les API Radar utilisables avec le contenu connecté.
{% endalert %}