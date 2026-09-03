---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Cet article de référence décrit le partenariat entre Braze et Foursquare, une plateforme de données de localisation qui permet de déclencher des événements en temps réel en fonction de la localisation."
page_type: partner
search_tag: Partner
---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) est une plateforme de données de localisation qui fournit un ciblage des données de localisation dans vos Campaigns Braze. Utilisez le SDK Pilgrim de Foursquare sur les applications iOS et Android pour déclencher des événements en temps réel en fonction de la localisation, ce qui vous permet d'exploiter les puissantes capacités de ciblage géographique de Foursquare pour envoyer des messages pertinents et personnalisés avec Braze.

_Cette intégration est gérée par Foursquare._

## Prérequis {#prerequisites}

| Condition | Description |
|---|---|
| Compte Foursquare | Un compte Foursquare est requis pour tirer parti de ce partenariat. |
| Clé API REST Braze | Une clé API REST Braze avec les permissions `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Espace de travail Braze et identifiants d'application | L'espace de travail Braze et les identifiants d'application se trouvent dans la [console de développement]({{site.baseurl}}/api/basics). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prérequis" }

## Intégration {#integration}

Pour intégrer les deux plateformes, vous devez intégrer les deux SDK et mapper les champs utilisateur correspondants. Après avoir intégré le SDK Pilgrim, vous recevrez des événements de localisation sur l'appareil ou via un webhook.

### Étape 1 : Mapper les champs d'ID utilisateur {#step-1-map-user-id-fields}

Pour mapper correctement les champs entre les deux SDK, définissez le même ID utilisateur dans les deux systèmes en utilisant la [méthode `changeUser`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#setting-user-ids) dans le SDK Braze et la méthode `setUserId` de [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) dans le SDK Pilgrim.

### Étape 2 : Configurer la console Pilgrim {#step-2-configure-pilgrim-console}
![Image de la console Pilgrim demandant l'ID de groupe, l'ID d'application Android et l'ID d'application iOS.]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Trouvez l'espace de travail et les ID d'application dans la console de développement de Braze. Ensuite, saisissez votre clé REST API Braze et les ID d'application dans la console Foursquare Pilgrim.

Une fois la console Pilgrim configurée, le SDK Pilgrim enregistrera les événements de localisation et les transmettra à Braze, vous permettant de recibler et de segmenter les clients qualifiés. Consultez le [site développeur Foursquare](https://developer.foursquare.com/) pour plus de détails.

{% alert important %}
Le SDK Pilgrim nécessite l'activation des services de localisation.
{% endalert %}

## Déclenchement des messages {#triggering-messages}

Une fois l'intégration configurée, vous pouvez mettre en place une Campaign ou un Canvas qui réagira aux événements de localisation générés par le SDK Pilgrim. Cette voie d'intégration est idéale pour envoyer des messages en temps réel dès qu'un utilisateur entre dans un lieu d'intérêt, ou pour effectuer un suivi différé après son départ, comme une note de remerciement ou un rappel.

Pour envoyer une Campaign qui enverra des messages en fonction d'un emplacement défini :
- Créez une Campaign ou un Canvas Braze configuré avec une **livraison par événement**
- Pour votre déclencheur, utilisez un événement personnalisé `arrival` avec un filtre de propriété d'événement pour `locationType`, comme illustré dans la capture d'écran suivante.

![Une Campaign par événement à l'étape de livraison montrant « arrival » sélectionné comme option « effectuer un événement personnalisé », où « locationType » est égal à « home ».]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Reciblage {#retargeting}

Pour recibler vos utilisateurs, utilisez le SDK Pilgrim afin de définir un attribut personnalisé `last_location` sur les profils utilisateur de vos utilisateurs Braze. Vous pouvez ensuite utiliser la comparaison `matches regex` pour recibler les utilisateurs qui se sont rendus à un endroit précis dans le monde réel, par exemple en segmentant tous les utilisateurs qui se trouvaient récemment dans une pizzeria.

![Une Campaign par événement à l'étape des utilisateurs cibles montrant « last_location » égal à « Pizza Place ».]({% image_buster /assets/img_archive/last-location-segment.png %})

Vous pouvez également segmenter les utilisateurs dans Braze qui ont visité un type de lieu particulier en vous basant sur le `primaryCategoryId` de Foursquare dans une fenêtre de temps donnée. Pour tirer parti de ce point de donnée dans vos cas d'usage de reciblage, enregistrez `primaryCategoryId` en tant que propriété d'événement lors de votre processus de segmentation d'audience. Pour identifier les utilisateurs et les propriétés utilisés par l'API Foursquare et le SDK Pilgrim, consultez le [site développeur de Foursquare](https://developer.foursquare.com/).