---
nav_title: Suivi de localisation
article_title: Suivi de la localisation
page_order: 0
page_type: reference
description: "Cet article de référence explique comment utiliser le suivi de la localisation et le ciblage par localisation dans vos applications, et quels partenaires prennent en charge le suivi de la localisation."
tool: Location
search_rank: 2
---

# Suivi de la localisation {#location-tracking}

> La collecte de localisation capture la position la plus récente d'un utilisateur au moment de l'ouverture de l'application, à l'aide des données de localisation GPS. Vous pouvez utiliser ces informations pour segmenter les données en fonction des utilisateurs qui se trouvaient dans un emplacement défini.

## Activer le suivi de la localisation {#enabling-location-tracking}

Pour activer la collecte de localisation dans votre application, consultez le guide développeur correspondant à la plateforme que vous utilisez :

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)

De manière générale, les applications mobiles utilisent la puce GPS de l'appareil et d'autres systèmes (tels que le scan Wi-Fi) pour suivre la localisation d'un utilisateur. Les applications web utilisent le WPS (Wi-Fi Positioning System) pour suivre la localisation d'un utilisateur. Toutes ces plateformes nécessitent que les utilisateurs acceptent le suivi de la localisation. La précision de vos données de suivi de localisation peut être affectée selon que vos utilisateurs ont activé ou non le Wi-Fi sur leurs appareils. Les utilisateurs Android peuvent également choisir différents modes de localisation : les utilisateurs en mode « Économie de batterie » ou « Appareil uniquement » peuvent avoir des données imprécises.

### Localisation de l'utilisateur SDK par adresse IP {#sdk-user-location-by-ip-address}

Braze détecte la localisation des utilisateurs à partir du pays géolocalisé en utilisant l'adresse IP dès le début de la première session SDK.

Auparavant, Braze utilisait le code pays issu des paramètres régionaux de l'appareil lors de la création de l'utilisateur SDK et pendant toute la durée de la première session. Ce n'est qu'après le traitement du premier démarrage de session que l'adresse IP était utilisée pour définir le pays de manière plus fiable sur l'utilisateur. Cela signifiait que le pays de l'utilisateur n'était défini avec une plus grande précision qu'à partir de la deuxième session, uniquement après le traitement du premier démarrage de session.

Désormais, Braze utilise l'adresse IP pour définir la valeur du pays sur les profils utilisateur créés via le SDK, et ce paramètre de pays basé sur l'IP est disponible pendant et après la première session.

#### Collecte automatique de la localisation {#automatic-location-collection}

Lorsqu'elle est activée, la collecte automatique de la localisation dans le SDK est distincte du comportement de détection du pays par IP. Elle concerne les signaux de localisation de l'appareil tels que le GPS lorsque l'utilisateur a accordé l'autorisation, ce qui alimente des filtres comme `Most Recent Location`. Elle ne renseigne pas automatiquement les champs de granularité fine tels que la ville à partir de l'IP seule.

Pour le ciblage au niveau de la ville ou du code postal, utilisez [`setLastKnownLocation()`]({{site.baseurl}}/developer_guide/analytics/tracking_location) (consultez l'article SDK pour votre plateforme), votre propre service de géolocalisation par IP écrivant des attributs personnalisés, ou le [ciblage par localisation]({{site.baseurl}}/user_guide/audience/segments/location_targeting) avec les données que vous collectez.

## Ciblage par localisation {#location-targeting}

En utilisant les données de suivi de localisation et les segments, vous pouvez mettre en place des campagnes et des stratégies basées sur la localisation. Par exemple, vous pouvez souhaiter lancer une campagne promotionnelle pour les utilisateurs vivant dans une région particulière, ou exclure les utilisateurs d'une région soumise à des réglementations plus strictes.

Consultez [Ciblage par localisation]({{site.baseurl}}/user_guide/audience/segments/location_targeting) pour plus d'informations sur la création d'un segment basé sur la localisation.

## Définir manuellement l'attribut de localisation par défaut {#hard-setting-the-default-location-attribute}

Vous pouvez également utiliser l'[endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) de notre API pour mettre à jour l'attribut standard [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens). Voici un exemple :

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Prise en charge des balises et du géorepérage par les partenaires {#partnership-support-for-beacon-and-geofence}

La combinaison de la prise en charge existante des balises ou du géorepérage avec nos fonctionnalités de ciblage et d'envoi de messages vous donne plus d'informations sur les actions physiques de vos utilisateurs, afin de pouvoir leur envoyer des messages en conséquence. Vous pouvez tirer parti du suivi de la localisation avec certains de nos partenaires :

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)

## Différences entre géorepérage et suivi de la localisation {#differences-between-geofences-and-location-tracking}

{% multi_lang_include locations_and_geofences/geofences_vs_location_tracking.md %}

## Questions fréquemment posées {#frequently-asked-questions}

### Quand Braze collecte-t-il les données de localisation ? {#when-does-braze-collect-location-data}

Braze ne collecte la localisation que lorsque l'application est ouverte au premier plan. Par conséquent, notre filtre `Most Recent Location` cible les utilisateurs en fonction de l'endroit où ils ont ouvert l'application pour la dernière fois (également appelé démarrage de session).

Vous devez également garder à l'esprit les nuances suivantes :

- Si la localisation est désactivée, le filtre `Most Recent Location` affiche la dernière localisation enregistrée.
- Si un utilisateur a déjà eu une localisation enregistrée sur son profil, il est éligible au filtre `Location Available`, même s'il a désactivé le suivi de la localisation depuis.

### Quelle est la différence entre les filtres Most Recent Device Locale et Most Recent Location ? {#whats-the-difference-between-the-most-recent-device-locale-and-most-recent-location-filters}

Le filtre `Most Recent Device Locale` provient des paramètres de l'appareil de l'utilisateur. Par exemple, pour les utilisateurs d'iPhone, il apparaît dans l'appareil sous **Réglages** > **Général** > **Langue et région**. Ce filtre est utilisé pour capturer la langue et le formatage régional, comme les dates et les adresses, et est indépendant du filtre `Most Recent Location`.

Le filtre `Most Recent Location` correspond à la dernière position GPS connue de l'appareil. Il est mis à jour au démarrage de la session et est stocké sur le profil de l'utilisateur.

### Si un utilisateur désactive le suivi de la localisation, ses données de localisation précédentes sont-elles supprimées de Braze ? {#if-a-user-opts-out-of-location-tracking-is-their-previous-location-data-removed-from-braze}

Non. Si un utilisateur a déjà eu une localisation enregistrée sur son profil, ces données ne sont pas automatiquement supprimées s'il désactive ultérieurement le suivi de la localisation.

## Résolution des problèmes {#troubleshooting}

### Aucun utilisateur n'a de localisation disponible {#no-users-have-available-locations}

Braze capture par défaut la localisation la plus récente d'un utilisateur via le SDK. Cela signifie généralement que la « localisation récente » correspond à l'emplacement depuis lequel votre utilisateur a utilisé votre application le plus récemment. Si vous envoyez des données de localisation en arrière-plan à Braze, vous pouvez disposer de données plus granulaires.

Si aucun utilisateur n'a de localisation disponible, deux vérifications rapides peuvent vous aider à confirmer la collecte et le transfert des données.

#### Collecte des données {#data-collection}

Confirmez que votre application collecte les données de localisation :

- Pour iOS, cela signifie que les utilisateurs acceptent de partager leurs données de localisation via une invite à un moment donné du parcours utilisateur.
- Pour Android, confirmez que votre application demande les autorisations de localisation fine ou approximative lors de l'installation.

Pour vérifier si les données de localisation des utilisateurs sont envoyées à Braze, utilisez le filtre **Location Available**. Ce filtre vous permet de voir le pourcentage d'utilisateurs ayant une « localisation la plus récente ».

![Un segment « Test Location » qui utilise le filtre « Location Available ».]({% image_buster /assets/img_archive/trouble7.png %})

#### Transfert des données {#data-transfer}

Confirmez que vos développeurs transmettent les données de localisation à Braze. Normalement, la transmission des données de localisation est gérée automatiquement par le SDK une fois que l'utilisateur a accordé les autorisations, mais vos développeurs peuvent avoir désactivé le suivi de la localisation dans Braze. Plus d'informations sur le suivi de la localisation sont disponibles pour :
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)