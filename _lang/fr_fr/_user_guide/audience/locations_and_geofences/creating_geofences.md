---
nav_title: Créer des géorepérages
article_title: Créer des géorepérages
page_order: 1
page_type: reference
toc_headers: h2
description: "Découvrez comment configurer les autorisations de localisation, créer un message d'amorçage pour les autorisations de localisation et créer des géorepérages pour des campagnes basées sur la localisation."
tool:
  - Location
search_rank: 9
---

# Géorepérages {#geofences}

> Un géorepérage est une zone géographique virtuelle, représentée par une latitude et une longitude combinées à un rayon, formant un cercle autour d'une position globale spécifique. Les géorepérages peuvent varier de la taille d'un bâtiment à celle d'une ville entière. Vous pouvez utiliser les géorepérages pour déclencher des campagnes en temps réel lorsque les utilisateurs entrent ou sortent de leurs limites, ou pour envoyer des campagnes de suivi des heures ou des jours plus tard.

{% alert tip %}
Pour un guide pas à pas, consultez le cours d'apprentissage Braze [Créer un géorepérage](https://learning.braze.com/create-a-geofence).
{% endalert %}

## Fonctionnement {#how-it-works}

Les géorepérages sont organisés en ensembles de géorepérages, c'est-à-dire un groupe de géorepérages que vous pouvez utiliser pour segmenter ou engager les utilisateurs sur l'ensemble de la plateforme. Chaque ensemble de géorepérages peut contenir un maximum de 10 000 géorepérages. Vous pouvez créer ou télécharger un nombre illimité de géorepérages.

Les utilisateurs qui entrent ou sortent de vos géorepérages ajoutent une nouvelle couche de données utilisateur que vous pouvez utiliser pour la segmentation et le reciblage.

Gardez à l'esprit les limites suivantes par appareil :

- Les applications Android peuvent stocker jusqu'à 100 géorepérages localement à la fois. Braze est configuré pour ne stocker que 20 géorepérages localement par application.
- Les appareils iOS peuvent surveiller jusqu'à 20 géorepérages à la fois par application. Braze surveille jusqu'à 20 emplacements si de l'espace est disponible.
- Si l'utilisateur est éligible pour recevoir plus de 20 géorepérages, Braze télécharge le nombre maximum d'emplacements en fonction de la proximité de l'utilisateur au démarrage de la session.
- Pour que les géorepérages fonctionnent correctement, assurez-vous que votre application n'utilise pas tous les emplacements de géorepérage disponibles.

Le tableau suivant décrit les termes courants liés aux géorepérages :

| Terme | Description |
|---|---|
| Latitude et longitude | Le centre géographique du géorepérage. |
| Rayon | Le rayon du géorepérage en mètres, mesuré à partir du centre géographique. Définissez un rayon minimum de 100 à 150 mètres pour tous les géorepérages. |
| Période de refroidissement | Les utilisateurs reçoivent des notifications déclenchées par géorepérage après avoir effectué des transitions d'entrée ou de sortie sur des géorepérages individuels. Après une transition, il existe une période prédéfinie pendant laquelle cet utilisateur ne peut pas effectuer la même transition sur ce géorepérage individuel. Cette « période de refroidissement » est prédéfinie par Braze et son objectif principal est d'éviter les requêtes réseau inutiles. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fonctionnement" }

## Conditions préalables {#prerequisites}

### Exigences SDK et plateforme {#sdk-and-platform-requirements}

Les campagnes déclenchées par géorepérage sont disponibles sur iOS et Android. Pour prendre en charge les géorepérages, les éléments suivants sont requis :

* Les géorepérages Braze ou la collecte de localisation doivent être activés.
* L'utilisateur doit accorder l'accès à la localisation « Toujours autoriser ».

{% alert important %}
La collecte de localisation Braze est désactivée par défaut. Pour vérifier qu'elle est activée sur Android, confirmez que `com_braze_enable_location_collection` est défini sur `true` dans votre `braze.xml`.
{% endalert %}

Pour les instructions de configuration spécifiques à chaque plateforme, consultez [Géorepérages]({{site.baseurl}}/developer_guide/geofences) dans le guide du développeur.

### Autorisations de localisation {#location-permissions}

Avant que vos géorepérages puissent fonctionner, les utilisateurs doivent accorder à votre application l'autorisation d'accéder à leur localisation. Comprendre les différents niveaux d'autorisation et leur impact sur le géorepérage est essentiel pour élaborer une stratégie efficace basée sur la localisation.

## Comprendre les autorisations de localisation {#understanding-location-permissions}

iOS et Android offrent tous deux plusieurs niveaux d'accès à la localisation. Le niveau d'autorisation accordé par un utilisateur affecte directement le fonctionnement du géorepérage et la précision des données de localisation.

### Niveaux d'autorisation {#permission-levels}

{% tabs local %}
{% tab iOS %}

| Autorisation | Description | Prise en charge du géorepérage |
|---|---|---|
| **Autoriser une fois** | Accorde l'accès à la localisation pour une seule session. L'invite réapparaît la prochaine fois que l'utilisateur ouvre l'application. | Non. Le suivi en arrière-plan est désactivé, donc l'appareil ne reçoit des mises à jour de localisation que lorsque l'application est ouverte. |
| **Autoriser pendant l'utilisation de l'app** | Accorde l'accès à la localisation chaque fois que l'application est au premier plan. Une fois cette autorisation accordée, iOS peut présenter une invite de suivi demandant à l'utilisateur de passer à « Toujours autoriser ». | Oui. iOS active la surveillance de la localisation en arrière-plan, y compris les transitions de géorepérage, pour les applications disposant de cette autorisation. |
| **Toujours autoriser** | Accorde un accès continu à la localisation, y compris en arrière-plan et lorsque l'application est fermée. | Oui. Cela fournit la surveillance de géorepérage la plus fiable. |
| **Ne pas autoriser** | Refuse tout accès à la localisation. | Non. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Niveaux d'autorisation" }

{% endtab %}
{% tab Android %}

| Autorisation | Description | Prise en charge du géorepérage |
|---|---|---|
| **Pendant l'utilisation de l'app** | Accorde l'accès à la localisation lorsque l'application est au premier plan. | Non. Sur Android, l'accès à la localisation en arrière-plan est requis pour la surveillance des géorepérages. |
| **Toujours autoriser** | Accorde un accès continu à la localisation, y compris en arrière-plan. Sur Android 10 et versions ultérieures, cela nécessite une invite séparée après l'octroi initial de l'autorisation « Pendant l'utilisation de l'app ». | Oui. Cela est requis pour le géorepérage sur Android. |
| **Ne pas autoriser** | Refuse tout accès à la localisation. Sur Android 13 et versions ultérieures, si un utilisateur refuse l'invite de localisation deux fois, le système d'exploitation bloque les invites ultérieures dans l'application. | Non. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Niveaux d'autorisation" }

{% endtab %}
{% endtabs %}

### Localisation précise versus approximative {#precise-versus-approximate-location}

Sur iOS 14+ et Android 12+, les utilisateurs peuvent choisir entre la localisation précise et approximative.

| Paramètre | Précision | Impact sur le géorepérage |
|---|---|---|
| **Localisation précise (activée)** | Précision de l'ordre de 5 à 50 mètres, utilisant le GPS, le Wi-Fi et la triangulation cellulaire. | Les géorepérages fonctionnent comme prévu. Recommandé pour tous les cas d'usage basés sur le géorepérage. |
| **Localisation approximative (désactivée)** | Précision d'environ 3 kilomètres carrés (environ 1 mile carré). L'appareil renvoie une zone générale plutôt que des coordonnées exactes. | Les géorepérages ne se déclenchent pas de manière fiable. L'appareil ne peut pas déterminer avec précision si un utilisateur se trouve à l'intérieur ou à l'extérieur d'une limite de géorepérage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Localisation précise versus approximative" }

{% alert important %}
Pour que le géorepérage fonctionne de manière fiable, les utilisateurs doivent activer la localisation précise. Incluez cette recommandation dans votre message d'amorçage des autorisations de localisation afin que les utilisateurs comprennent pourquoi la localisation précise est importante.
{% endalert %}

## Configurer un message d'amorçage des autorisations de localisation {#setting-up-a-location-permission-primer}

Un message d'amorçage des autorisations de localisation est un message in-app qui explique la valeur du partage des données de localisation avant que l'utilisateur ne voie l'invite native d'autorisation du système d'exploitation. Étant donné que l'invite native de localisation ne peut être affichée qu'une seule fois (sur iOS) ou un nombre limité de fois (sur Android), préparer les utilisateurs à l'avance augmente les taux d'abonnement.

### Étape 1 : Collaborer avec votre équipe de développement {#step-1-work-with-your-development-team}

Étant donné que les messages in-app de Braze n'incluent pas d'action de bouton intégrée pour invoquer l'invite native d'autorisation de localisation, votre équipe de développement doit gérer les autorisations de localisation côté appareil. Avant de créer le message in-app dans Braze, coordonnez-vous avec votre équipe de développement pour configurer des deep links que votre message in-app peut appeler. L'implémentation spécifique dépend de l'architecture de votre application, mais les approches courantes incluent :

- Un deep link qui déclenche l'invite native d'autorisation de localisation depuis votre application.
- Un deep link qui ouvre la page des paramètres de localisation de l'application dans les paramètres du système d'exploitation de l'appareil, ce qui est utile pour relancer les utilisateurs qui ont précédemment refusé ou limité leurs autorisations.

Pour plus d'informations sur les deep links, consultez [Création de liens profonds vers le contenu in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls). Pour des conseils spécifiques à chaque plateforme sur l'intégration de la localisation et du géorepérage, consultez [Géorepérages]({{site.baseurl}}/developer_guide/geofences) dans le guide du développeur.

### Étape 2 : Créer le message in-app d'amorçage de localisation {#step-2-build-the-location-primer-in-app-message}

Créez une campagne de message in-app qui explique la valeur de l'accès à la localisation. Tous les types de messages in-app prennent en charge cet abonnement, y compris le glisser-déposer.

1. Allez dans **Messaging** > **Campaigns**, puis sélectionnez **Create Campaign** > **In-App Message**.
2. Choisissez un type de message et une disposition. Une disposition **Modal** ou **Full** vous donne plus d'espace pour expliquer les avantages.
3. Rédigez un message qui explique clairement pourquoi l'accès à la localisation profite à l'utilisateur. Par exemple :
    - « Activez la localisation pour être informé des offres à proximité. »
    - « Activez la localisation pour que nous puissions vous prévenir lorsque votre commande est prête à être retirée dans votre magasin le plus proche. »
4. Ajoutez un bouton d'appel à l'action principal (tel que **Turn On Location**) et définissez son comportement au clic sur **Deep Link into App**, en utilisant le deep link créé par votre équipe de développement pour déclencher l'invite native de localisation.
5. Ajoutez un bouton secondaire (tel que **Not Now**) qui ferme le message.

### Étape 3 : Cibler la bonne audience {#step-3-target-the-right-audience}

Pour de meilleurs résultats, affichez le message d'amorçage de localisation lorsque les utilisateurs sont engagés et susceptibles de voir la valeur du partage de leur localisation.

- **Ciblez les utilisateurs qui n'ont pas encore accordé l'accès à la localisation.** Collaborez avec votre équipe de développement pour déterminer la meilleure façon de suivre et de segmenter les utilisateurs en fonction de leur statut d'autorisation de localisation.
- **Programmez le message d'amorçage après une action à forte valeur,** comme la finalisation d'un achat, l'enregistrement d'un magasin en favori ou la consultation d'événements à proximité. Les utilisateurs sont plus susceptibles de s'abonner lorsqu'ils comprennent l'avantage.
- **Évitez d'afficher le message d'amorçage au premier lancement.** Attendez que les utilisateurs aient suffisamment apprécié la valeur de l'application pour souhaiter une expérience plus personnalisée.

### Étape 4 : Encourager le niveau d'autorisation recommandé {#step-4-encourage-the-recommended-permission-level}

Votre message d'amorçage doit encourager les utilisateurs à accorder le niveau d'autorisation qui active le géorepérage :

- **Sur iOS,** encouragez les utilisateurs à sélectionner **Allow While Using the App** au minimum. iOS peut ensuite inviter l'utilisateur à passer à **Always Allow** de lui-même. Vous pouvez également effectuer un suivi avec une campagne séparée pour expliquer pourquoi « Toujours autoriser » offre la meilleure expérience.
- **Sur Android,** encouragez les utilisateurs à accorder **Always Allow**. Sur Android 10 et versions ultérieures, l'utilisateur doit d'abord accorder « Pendant l'utilisation de l'app », puis accorder « Toujours autoriser » dans une invite de suivi séparée. Guidez-les à travers les deux étapes.

Dans les deux cas, rappelez aux utilisateurs de garder la **Localisation précise** activée pour la meilleure expérience.

## Rediriger les utilisateurs vers les paramètres du système d'exploitation {#redirecting-users-to-os-settings}

Si un utilisateur a précédemment refusé l'accès à la localisation ou sélectionné une autorisation limitée, vous ne pouvez pas déclencher à nouveau l'invite native depuis l'application sur la plupart des versions du système d'exploitation. Au lieu de cela, dirigez-les vers la mise à jour de leurs autorisations dans les paramètres de l'appareil.

Utilisez un deep link dans un [message in-app]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) personnalisé pour diriger l'utilisateur vers la page des paramètres de localisation de l'application dans le système d'exploitation. Votre équipe de développement peut configurer un deep link à cet effet dans le cadre de la gestion des autorisations de localisation de votre application (consultez l'[étape 1](#step-1-work-with-your-development-team)).

Lors de la création de ce message in-app, tenez compte des éléments suivants :

- **Quand l'afficher :** Ciblez les utilisateurs qui ont l'autorisation « Pendant l'utilisation de l'app » lorsque vous avez besoin de « Toujours autoriser », ou les utilisateurs qui ont précédemment refusé l'accès à la localisation.
- **Exemple de message :** « Pour profiter pleinement des fonctionnalités basées sur la localisation, mettez à jour vos paramètres de localisation sur "Toujours autoriser". Appuyez ci-dessous pour accéder aux paramètres. »

{% alert tip %}
Vous pouvez déclencher ce message in-app à tout moment du parcours utilisateur, après un achat, lors de la consultation de contenu à proximité ou dans le cadre d'un flux Canvas. Soyez sélectif lorsque vous relancez : limitez ces campagnes aux utilisateurs fidèles ou très engagés pour éviter la lassitude liée aux demandes d'abonnement.
{% endalert %}

## Exemples de stratégies d'amorçage de localisation {#example-location-priming-strategies}

### Message d'amorçage « Pendant l'utilisation de l'app » {#while-using-the-app-primer}

Une application de vente au détail affiche un message in-app modal après qu'un utilisateur a enregistré un magasin en favori :

- **Titre :** « Soyez informé des offres en magasin »
- **Corps :** « Activez la localisation pour que nous puissions vous envoyer des offres exclusives lorsque vous êtes à proximité de vos magasins favoris. Votre localisation n'est consultée que pendant l'utilisation de l'application. »
- **CTA :** **Turn On Location** crée un deep link vers l'invite native d'autorisation de localisation
- **Fermer :** **Maybe Later** ferme le message

Cette approche est efficace car l'utilisateur a déjà exprimé son intérêt pour un magasin spécifique, créant un contexte naturel pour la demande d'autorisation de localisation.

### Suivi « Toujours autoriser » {#always-allow-follow-up}

Après qu'un utilisateur a accordé l'autorisation « Pendant l'utilisation de l'app », affichez un message in-app de suivi lors de la session suivante :

- **Titre :** « Ne manquez jamais une offre à proximité »
- **Corps :** « Mettez à jour vos paramètres de localisation sur "Toujours" pour que nous puissions vous informer des offres même lorsque vous ne naviguez pas dans l'application. Nous n'enverrons que des alertes pertinentes lorsque vous serez à proximité des emplacements participants. »
- **CTA :** **Update Settings** crée un deep link vers la page des paramètres de localisation de l'application dans le système d'exploitation
- **Fermer :** **Keep Current Settings** ferme le message

Ce suivi donne à l'utilisateur le contexte expliquant pourquoi le passage à « Toujours autoriser » apporte une valeur supplémentaire au-delà du niveau d'autorisation initial.

## Créer manuellement des géorepérages {#manually-create-geofences}

### Étape 1 : Créer un ensemble de géorepérages {#step-1-create-a-geofence-set}

Pour créer un géorepérage, créez d'abord un ensemble de géorepérages.

1. Allez dans **Audience** > **Locations** dans le tableau de bord de Braze.
2. Sélectionnez **Create Geofence Set**.
3. Pour **Set name**, saisissez un nom pour votre ensemble de géorepérages.
4. (Facultatif) Ajoutez des étiquettes pour filtrer votre ensemble.

### Étape 2 : Ajouter les géorepérages {#step-2-add-the-geofences}

Ensuite, ajoutez des géorepérages à votre ensemble de géorepérages.

1. Sélectionnez **Draw Geofence** pour cliquer et faire glisser le cercle sur la carte. Répétez l'opération pour ajouter d'autres géorepérages à votre ensemble selon vos besoins.
2. (Facultatif) Sélectionnez **Edit** et remplacez la description du géorepérage par un nom.
3. (Facultatif) Sélectionnez **Show Advanced Settings**, puis utilisez ces paramètres pour contrôler la façon dont les analyses de géorepérage sont enregistrées :
  - Sélectionnez **Enable Analytics for Enter** et **Enable Analytics for Exit** pour enregistrer l'activité d'entrée et de sortie dans la [table SQL `USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) à des fins de reporting et d'analyse.
  - Configurez une période de refroidissement pour définir le nombre de secondes qui doivent s'écouler avant que le même utilisateur puisse déclencher un autre événement d'entrée ou de sortie pour ce géorepérage. Si vous ne définissez pas de période de refroidissement, la valeur par défaut est de six heures.
  - Utilisez **Android Notification Responsiveness** pour définir le délai maximum, en secondes, que les appareils Android utilisent lors de la transmission des événements d'entrée ou de sortie à votre application.

{: start="4" }
4. Sélectionnez **Save Geofence Set** pour enregistrer.

{% alert tip %}
Créez des géorepérages avec un rayon d'au moins 200 mètres pour un fonctionnement optimal. Pour plus d'informations, consultez les [bonnes pratiques pour les géorepérages](#geofence-best-practices).
{% endalert %}

![Un ensemble de géorepérages avec deux géorepérages « EastCoastGreaterNY » et « WesternRegion » avec deux cercles sur la carte.]({% image_buster /assets/img/geofence_example.png %})

## Téléchargement en masse de géorepérages {#creating-geofence-sets-via-bulk-upload}

Vous pouvez télécharger des géorepérages en masse sous forme d'objet GeoJSON de type `FeatureCollection`. Chaque géorepérage est un type de géométrie `Point` dans la collection de fonctionnalités. Les propriétés de chaque fonctionnalité nécessitent une clé `radius` et une clé optionnelle `name` pour chaque géorepérage.

Pour télécharger votre fichier JSON, sélectionnez **More** > **Upload JSON**.

Lors de la création de vos géorepérages, tenez compte des détails suivants :

- La valeur `coordinates` dans le GeoJSON est formatée comme `[Longitude, Latitude]`.
- Le rayon maximum de géorepérage pouvant être téléchargé est de 10 000 mètres (environ 10 kilomètres ou 6,2 miles).

### Exemple {#example}

L'exemple suivant montre le format GeoJSON correct pour spécifier deux géorepérages : un pour le siège de Braze à NYC et un pour la Statue de la Liberté au sud de Manhattan.

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.9853689, 40.7434683]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Utiliser les événements de géorepérage {#using-geofence-events}

Après avoir configuré vos géorepérages, vous pouvez les utiliser pour enrichir et améliorer la façon dont vous communiquez avec vos utilisateurs.

### Déclencher des Campaigns et des Canvas {#triggering-campaigns-and-canvases}

Pour utiliser les données de géorepérage dans le cadre des déclencheurs de Campaign et de Canvas, choisissez **Livraison par événement** comme méthode de réception. Ensuite, ajoutez une action de déclenchement `Trigger a Geofence`. Enfin, choisissez l'ensemble de géorepérages et les types d'événements de transition de géorepérage pour votre message. Vous pouvez également faire progresser les utilisateurs dans un Canvas à l'aide d'événements de géorepérage.

![Une Campaign par événement avec un géorepérage qui se déclenchera lorsqu'un utilisateur entre dans les aéroports allemands.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personnaliser les messages {#personalizing-messages}

Pour utiliser les données de géorepérage afin de personnaliser un message, vous pouvez utiliser la syntaxe de personnalisation Liquid suivante :

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Mettre à jour les ensembles de géorepérages {#updating-geofence-sets}

Le SDK Braze ne demande les géorepérages qu'une seule fois par jour au démarrage de la session. Si vous apportez des modifications aux ensembles de géorepérages après le démarrage de la session, vous devez attendre 24 heures à partir du moment où les ensembles sont initialement téléchargés pour recevoir l'ensemble mis à jour.

{% alert note %}
Si les géorepérages ne sont pas chargés localement sur l'appareil, l'utilisateur ne peut pas déclencher le géorepérage même s'il entre dans la zone.
{% endalert %}

## Bonnes pratiques pour les géorepérages {#geofence-best-practices}

### Configuration des géorepérages {#geofence-configuration}

- Utilisez un rayon de 200 mètres ou plus pour un déclenchement fiable.
- Évitez de configurer des géorepérages qui se chevauchent ou sont imbriqués les uns dans les autres, car cela peut causer des problèmes de déclenchement.
- Un géorepérage ne peut déclencher un événement d'entrée qu'une seule fois toutes les six heures. Cette période de refroidissement est appliquée localement. Si un utilisateur désinstalle l'application ou efface les données de l'application, toutes les périodes de refroidissement sont réinitialisées.
- Un maximum de 20 géorepérages peut être stocké sur un appareil. Si l'utilisateur est éligible pour plus de 20, Braze télécharge les emplacements les plus proches en fonction de la proximité au démarrage de la session.
- Braze n'envoie que les géorepérages situés dans un rayon de 2 000 kilomètres de l'utilisateur vers l'appareil.

### Exigences de l'appareil {#device-requirements}

- Les utilisateurs de votre application doivent accorder les autorisations de localisation. Consultez la section [Autorisations de localisation](#location-permissions) pour plus d'informations.

{% alert note %}
L'intégration SDK de base active uniquement le suivi de localisation. Le géorepérage nécessite des étapes de configuration supplémentaires pour iOS et Android. Pour plus de détails, consultez [Géorepérages]({{site.baseurl}}/developer_guide/geofences) dans le guide du développeur.
{% endalert %}

Vous pouvez également utiliser les géorepérages avec les partenaires technologiques de Braze, tels que [Radar]({{site.baseurl}}/partners/message_personalization/location/radar) et [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare).

## Différences entre les géorepérages et le suivi de localisation {#differences-between-geofences-and-location-tracking}

{% multi_lang_include locations_and_geofences/geofences_vs_location_tracking.md %}

## Questions fréquemment posées {#frequently-asked-questions}

### Quelle est la précision des géorepérages Braze ? {#how-accurate-are-braze-geofences}

Les géorepérages Braze utilisent une combinaison de tous les fournisseurs de localisation disponibles sur un appareil pour trianguler la position de l'utilisateur, y compris le Wi-Fi, le GPS et les antennes cellulaires.

La précision typique se situe dans une plage de 20 à 50 mètres, et la meilleure précision se situe dans une plage de 5 à 10 mètres. Dans les zones rurales, la précision peut se dégrader considérablement, pouvant aller jusqu'à plusieurs kilomètres. Créez des géorepérages avec des rayons plus grands dans les zones rurales.

La précision dépend également de l'activation de la localisation précise par l'utilisateur. Avec la localisation approximative uniquement, la précision chute à environ 3 kilomètres carrés, rendant les géorepérages peu fiables. Pour plus d'informations, consultez [Localisation précise versus approximative](#precise-versus-approximate-location).

### Comment les géorepérages affectent-ils l'autonomie de la batterie ? {#how-do-geofences-affect-battery-life}

Le géorepérage Braze utilise le service système natif de géorepérage sur iOS et Android. Il est optimisé pour équilibrer intelligemment précision et consommation d'énergie, préservant l'autonomie de la batterie et améliorant les performances à mesure que le service sous-jacent s'améliore.

### Quand les géorepérages sont-ils actifs ? {#when-are-geofences-active}

Les géorepérages Braze fonctionnent à toute heure du jour et de la nuit, même lorsque votre application est fermée. Ils deviennent actifs dès qu'ils sont définis et téléchargés dans le tableau de bord de Braze. Cependant, les géorepérages ne peuvent pas fonctionner si un utilisateur a désactivé le suivi de localisation.

Pour que les géorepérages fonctionnent, les utilisateurs doivent avoir les services de localisation activés sur leur appareil et avoir accordé à votre application le niveau d'autorisation de localisation requis. Pour plus d'informations, consultez [Comprendre les autorisations de localisation](#understanding-location-permissions).

### Les données de géorepérage sont-elles stockées dans les profils utilisateur ? {#is-geofence-data-stored-in-user-profiles}

Non, Braze ne stocke pas les données de géorepérage dans les profils utilisateur. Les géorepérages sont surveillés par les services de localisation d'Apple et de Google, et Braze n'est notifié que lorsqu'un utilisateur déclenche un géorepérage. À ce moment-là, Braze traite toutes les Campaigns de déclenchement associées.

### Puis-je configurer un géorepérage à l'intérieur d'un géorepérage ? {#can-i-set-up-a-geofence-within-a-geofence}

En tant que bonne pratique, évitez de configurer des géorepérages qui se chevauchent, car cela peut causer des problèmes de déclenchement des notifications.

### Que se passe-t-il si un utilisateur refuse l'accès à la localisation ? {#what-if-a-user-denies-location-access}

Votre équipe de développement peut configurer un deep link qui ouvre la page des paramètres de localisation de l'application dans le système d'exploitation, où les utilisateurs peuvent mettre à jour leurs autorisations. Vous pouvez utiliser ce deep link dans un message in-app personnalisé à tout moment du parcours utilisateur. Soyez sélectif quant au moment où vous affichez ce message : ciblez les utilisateurs qui sont engagés ou qui ont effectué une action à forte valeur pour augmenter les chances d'abonnement. Pour plus d'informations, consultez [Rediriger les utilisateurs vers les paramètres du système d'exploitation](#redirecting-users-to-os-settings).