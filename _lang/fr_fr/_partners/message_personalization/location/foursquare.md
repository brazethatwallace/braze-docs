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

> [Foursquare](https://foursquare.com/) est une plateforme de données de localisation qui fournit un ciblage des données de localisation dans vos campagnes Braze. Utilisez le SDK Pilgrim de Foursquare sur les applications iOS et Android pour déclencher des événements en temps réel en fonction de la localisation, ce qui vous permet d'exploiter les puissantes capacités de ciblage géographique de Foursquare pour envoyer des messages pertinents et personnalisés avec Braze.

_Cette intégration est gérée par Foursquare._

## Conditions préalables {#prerequisites}

| Condition | Description |
|---|---|
| Compte Foursquare | Un compte Foursquare est nécessaire pour bénéficier de ce partenariat. |
| Clé REST API de Braze | Une clé REST API de Braze avec les autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| Espace de travail Braze et identifiants d'applications | L'espace de travail Braze et les identifiants d'applications se trouvent dans la [console de développement]({{site.baseurl}}/api/api_key/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions préalables" }

## Intégration {#integration}

Pour intégrer les deux plateformes, vous devez intégrer les deux SDK et mapper les champs utilisateur correspondants. Après avoir intégré le SDK Pilgrim, vous recevrez des événements de localisation sur l'appareil ou via un webhook.

### Étape 1 : Mapper les champs d'ID utilisateur {#step-1-map-user-id-fields}

Pour mapper correctement les champs entre les deux SDK, définissez le même ID utilisateur dans les deux systèmes à l'aide de la [méthode `changeUser`]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids) du SDK Braze et de la méthode `setUserId` de [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) dans le SDK Pilgrim.

### Étape 2 : Configurer la console Pilgrim {#step-2-configure-pilgrim-console}
![Image de la console Pilgrim demandant l'ID de groupe, l'ID d'application Android et l'ID d'application iOS.]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Recherchez l'espace de travail et les identifiants d'applications dans la console de développement Braze. Ensuite, saisissez votre clé REST API de Braze et vos identifiants d'applications dans la console Foursquare Pilgrim.

Une fois la console Pilgrim configurée, le SDK Pilgrim enregistre les événements de localisation et les transmet à Braze, ce qui vous permet de recibler et de segmenter les clients qualifiés. Consultez le [site des développeurs de Foursquare](https://developer.foursquare.com/) pour plus de détails.

{% alert important %}
Le SDK Pilgrim nécessite que vous activiez les services de localisation.
{% endalert %}

## Déclenchement de messages {#triggering-messages}

Une fois l'intégration configurée, vous pouvez mettre en place une campagne ou un Canvas qui réagira aux événements de localisation générés par le SDK Pilgrim. Cette méthode d'intégration est idéale pour l'envoi de messages en temps réel juste après que les utilisateurs entrent dans un lieu qui les intéresse, ou pour des communications de suivi différées après leur départ, comme une note de remerciement ou un rappel.

Pour envoyer une campagne qui enverra des messages en fonction d'une localisation définie :
- Créez une campagne Braze ou un Canvas avec la **Livraison par événement**
- Pour votre déclencheur, utilisez un événement personnalisé `arrival` avec un filtre de propriétés d'événement pour `locationType`, comme indiqué dans la capture d'écran suivante.

![Une campagne basée sur l'action dans l'étape de livraison montrant « arrival » sélectionné comme option « perform custom event », où « locationType » est égal à « home ».]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Reciblage {#retargeting}

Pour recibler vos utilisateurs, utilisez le SDK Pilgrim pour définir un attribut personnalisé `last_location` sur les profils utilisateur de vos utilisateurs Braze. Vous pouvez ensuite utiliser la comparaison `matches regex` pour recibler les utilisateurs qui se sont rendus à un endroit précis dans le monde réel, par exemple en segmentant tous les utilisateurs qui se sont récemment rendus dans une pizzeria.

![Une campagne basée sur l'action dans l'étape des utilisateurs cibles montrant que « last_location » est égal à « Pizza Place ».]({% image_buster /assets/img_archive/last-location-segment.png %})

Vous pouvez également segmenter les utilisateurs dans Braze qui ont visité un type de lieu particulier en fonction du `primaryCategoryId` de Foursquare au cours d'une période donnée. Pour tirer parti de ce point de données dans vos cas d'utilisation de reciblage, enregistrez `primaryCategoryId` en tant que propriété d'événement lors de votre processus de segmentation d'audience. Pour identifier les utilisateurs et les propriétés utilisés par l'API Foursquare et le SDK Pilgrim, consultez le [site des développeurs de Foursquare](https://developer.foursquare.com/).