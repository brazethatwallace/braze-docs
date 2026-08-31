---
nav_title: Chord
article_title: Chord
description: "Connectez la plateforme de données client (CDP) Chord à Braze pour transmettre les événements eCommerce et les mises à jour d'identité à des fins d'envoi de messages, de segmentation et de parcours."
alias: /partners/chord/
page_type: partner
search_tag: Partner
---

# Chord

> [Chord](https://www.chord.co/) fournit une plateforme de données client qui capture et standardise les événements provenant de votre vitrine eCommerce. Lorsque vous connectez Chord à Braze, l'activité d'achat, les événements comportementaux et les mises à jour d'identité sont transmis à Braze afin que vous puissiez déclencher des Campaigns et maintenir les profils à jour sans avoir à construire ces pipelines vous-même.

_Cette intégration est maintenue par Chord._

Pour plus d'informations sur la configuration, les options de connexion et les listes de champs, consultez l'[intégration Chord Braze](https://docs.chord.co/braze#chord-x-braze-integration).

## À propos de l'intégration {#about-the-integration}

Chord agit comme la couche de données entre votre boutique et Braze. Après avoir connecté Braze en tant que destination dans le CDP Chord, Chord mappe les événements de son plan de suivi vers Braze. Utilisez ces données dans les Segments, les Canvas et la personnalisation des messages pour refléter ce que vos consommateurs font sur votre site.

## Prérequis {#prerequisites}

Avant de connecter Chord et Braze, vérifiez que vous disposez des éléments suivants :

| Condition | Description |
| ----------- | ----------- |
| Compte Chord | Un compte Chord est requis pour utiliser cette intégration. |
| Identifiants API Braze | Les identifiants dont vous avez besoin dépendent de votre [mode de connexion](#connection-modes). Le mode cloud utilise une clé REST API Braze. Le mode appareil utilise la clé API du canal Web pour le SDK Braze, qui est distincte de votre clé REST API. |
| Endpoint REST Braze | Chord envoie les données côté serveur aux endpoints [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) et [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify). Votre URL de base dépend de votre instance Braze, par exemple `https://rest.iad-01.braze.com`. Pour plus d'informations, consultez [Endpoints REST API Braze]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conditions requises" }

## Modes de connexion {#connection-modes}

Chord prend en charge le mode cloud (appels serveur-à-serveur via les REST API de Braze) et le mode appareil (Chord initialise le SDK Web de Braze et transmet les appels mappés). Choisissez le mode qui correspond à vos besoins : fonctionnalités complètes du SDK Web (par exemple, les messages in-app) ou uniquement le transfert d'événements côté serveur.

### Mode cloud {#cloud-mode}

1. Dans la plateforme de données Chord, ouvrez la CDP et accédez à **Destinations**.
2. Sélectionnez **Add** à côté des destinations, choisissez **Braze** dans le catalogue, puis saisissez un nom de destination et votre clé REST API Braze.
3. Créez la destination pour finaliser la connexion.

Créez la clé REST API dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. Si vous utilisez l'ancienne navigation, accédez à **Console de développement** > **Paramètres API**. Sauf si Chord spécifie des exigences différentes pour votre espace de travail, la clé nécessite les permissions `users.track` et `users.identify`. Pour en savoir plus, consultez [Clés API]({{site.baseurl}}/api/api_key).

### Mode appareil {#device-mode}

1. Dans la plateforme de données Chord, ouvrez la CDP et accédez à **Destinations**.
2. Sélectionnez **Add** à côté des destinations, choisissez **Braze (device mode)** dans le catalogue, puis saisissez un nom de destination et votre clé API du canal Web.
3. Créez la destination pour finaliser la connexion.

Utilisez la clé API du canal Web depuis **Paramètres** > **Paramètres de l'application** > **Web** > **Clé API** dans le tableau de bord de Braze. N'utilisez pas votre clé REST API pour le mode appareil.

### Configuration du mode appareil {#device-mode-configuration}

Dans les paramètres de destination Chord, configurez les éléments suivants :

- **Version du SDK Web de Braze :** Chord expose des versions sélectionnables du SDK dans la CDP ; confirmez la plage disponible dans la documentation de Chord.
- **Endpoint du SDK :** Doit correspondre à votre instance Braze. Pour en savoir plus, consultez [Endpoints API et SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints).
- **Options d'événements et du SDK :** Par exemple, quels comportements track ou identify envoyer, la gestion des événements de page, le comportement des messages in-app, le moment d'initialisation du SDK et les paramètres liés au consentement.

## Mappage des événements (mode appareil) {#event-mapping-device-mode}

Lorsque vous utilisez le mode appareil, Chord mappe les événements vers Braze comme indiqué dans ce tableau :

| Chord | Braze |
| ----- | ----- |
| Commande terminée | `logPurchase` |
| Autres événements `track` | `logCustomEvent` |
| Identify | Mises à jour de l'utilisateur (par exemple, attributs via l'objet utilisateur du SDK) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Seuls les événements inclus dans votre plan de suivi Chord et configurés pour la destination Braze sont transmis.

## Utilisation de l'intégration {#using-the-integration}

### Étape 1 : Confirmer les événements dans Braze {#step-1-confirm-events-in-braze}

Une fois que les données circulent, ouvrez les profils utilisateur ou vos outils d'événements dans Braze pour confirmer que les événements et les attributs arrivent comme prévu.

### Étape 2 : Créer des audiences et des parcours {#step-2-build-audiences-and-journeys}

Utilisez les événements et attributs synchronisés dans les [Segments]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), les [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) et les Campaigns pour cibler les consommateurs en fonction de leur comportement en magasin.

## Cas d'usage {#use-cases}

- **Envoi de messages post-achat :** Déclenchez des confirmations, des ventes croisées ou des demandes d'avis lorsque Chord reçoit des commandes finalisées.
- **Enrichissement de profil :** Maintenez les attributs Braze alignés avec les données de profil consommateur les plus récentes provenant de Chord pour une segmentation plus précise.
- **Reciblage comportemental :** Réengagez les consommateurs qui n'ont pas acheté ou converti récemment en utilisant les événements comportementaux de Chord.

## Considérations {#considerations}

{% alert important %}
Si un autre outil envoie déjà les mêmes événements à Braze, coordonnez-vous avec les responsables de cette intégration avant de connecter Braze via la CDP Chord. L'exécution de destinations en parallèle peut créer des événements en double en aval.
{% endalert %}

## Résolution des problèmes {#troubleshooting}

Si les événements n'apparaissent pas dans Braze :

1. Dans le CDP Chord, confirmez que les événements en direct arrivent bien de vos sources.
2. Vérifiez que la destination Braze utilise la bonne clé API, la bonne version du SDK (mode appareil) et le bon endpoint REST ou SDK pour votre instance.
3. Confirmez que la destination est associée à la source attendue dans Chord.
4. Dans Chord, consultez les journaux de la destination API ou les journaux de fonctions pour vérifier que les appels à `/users/track` et `/users/identify` ont bien abouti, puis vérifiez de nouveau dans Braze.

Pour les emplacements des journaux et les étapes dans l'interface propres à Chord, consultez l'[intégration Chord Braze](https://docs.chord.co/braze#chord-x-braze-integration).