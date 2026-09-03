---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot est une application mobile conçue pour se connecter de façon fluide à votre tableau de bord de Braze. Elle vous permet de lancer des Campaigns et des Canvas vers l'application, donnant vie aux messages Braze directement sur votre téléphone. Braze Pilot comprend une bibliothèque de simulations d'applications pour des marques fictives représentant différents secteurs, vous permettant de découvrir comment vos messages pourraient apparaître du point de vue de vos clients."
description: "Découvrez les différentes façons d'utiliser Braze pour envoyer des messages depuis le tableau de bord de Braze vers votre téléphone."

guide_featured_title: "Articles de la section"
guide_featured_list:
  - name: Commencer avec Braze Pilot
    link: /docs/user_guide/get_started/braze_pilot/getting_started
    image: /assets/img/braze_icons/brush-02.svg
  - name: Dictionnaire de données
    link: /docs/user_guide/get_started/braze_pilot/data_dictionary
    image: /assets/img/braze_icons/book-closed.svg
  - name: Liens profonds de navigation
    link: /docs/user_guide/get_started/braze_pilot/deep_links
    image: /assets/img/braze_icons/link-03.svg

---

## Simulations de l'application Pilot {#pilot-app-simulations}

Le cœur de Braze Pilot réside dans sa bibliothèque de simulations d'applications. Chaque application est une simulation réaliste d'une marque fictive propre à un secteur d'activité, instrumentée pour enregistrer un large éventail d'événements et d'attributs qui offrent des possibilités infinies pour alimenter les cas d'usage courants de Braze.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington est une application de fitness proposant des entraînements, des objectifs d'exercice et un service premium Steppington+. Elle offre plusieurs emplacements pour présenter les [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards), une section pouvant être dévoilée à l'aide de [feature flags]({{site.baseurl}}/developer_guide/feature_flags), ainsi qu'une bibliothèque complète de journalisation d'événements personnalisés qui permettent d'illustrer de nombreux parcours clients pour ce secteur.

![La page d'accueil de Steppington avec des icônes pour l'entraînement au marathon, le yoga, le cyclisme et la musculation.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

PantsLabyrinth est une application de commerce en ligne qui vend (vous l'aurez deviné) des pantalons ! L'application PantsLabyrinth offre une expérience complète de paiement du panier d'achat, une fonctionnalité optionnelle de liste de souhaits activable via un feature flag, ainsi que de nombreuses occasions de plaisanteries avec des amis britanniques.

![Une page produit pour PantsLabyrinth avec des options permettant d'ajouter des jeans au panier.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon

MovieCanon est un service de streaming parfaitement conçu pour illustrer les cas d'usage courants de Braze en matière d'engagement vis-à-vis du contenu.

![L'application MovieCanon propose divers thrillers à visionner.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Comment Pilot se connecte à votre tableau de bord de Braze {#how-pilot-connects-with-your-braze-dashboard}

Le SDK Braze est un ensemble de code qui collecte les données de vos utilisateurs une fois intégré à votre application ou à votre site web. Lorsque vous connectez Pilot à votre tableau de bord, vous initialisez cette connexion entre l'application Pilot sur votre téléphone et le SDK Braze, et vous établissez une connexion unique avec votre instance Braze en fournissant à Pilot l'identifiant de votre clé API pour votre tableau de bord.

![La première étape de la configuration de Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Une fois Pilot connecté à votre tableau de bord de Braze, le SDK Braze fonctionne dans l'application exactement comme il le fera une fois le SDK intégré à votre propre application ou site web. Concrètement, Braze va :

- Stocker les données relatives à votre activité utilisateur dans Pilot, y compris les données personnalisées propres aux marques fictives de l'application.
- Collecter automatiquement les données de session, les informations sur les appareils et les jetons de notification push.
- Alimenter les notifications push, les messages in-app et les canaux de communication Content Cards qui nécessitent une intégration SDK pour fonctionner.

Pour en savoir plus sur le SDK Braze, consultez la section [Intégration]({{site.baseurl}}/user_guide/get_started/integrations).

![La suite d'engagement client de Braze, qui comprend des intégrations, des API et des SDK pour l'ingestion de données, la classification, l'orchestration, la personnalisation et l'action avec des canaux de communication pour une boucle de rétroaction interactive avec vos clients.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Profils utilisateur dans Braze {#user-profiles-in-braze}

Chaque donnée envoyée à Braze est stockée dans un profil utilisateur dédié à un utilisateur particulier de votre application ou site web. Une fois Pilot connecté à votre tableau de bord de Braze, Braze commence à enregistrer des données vous concernant en tant qu'utilisateur de Pilot. Deux types d'utilisateurs peuvent être créés pour vous via cette connexion : anonyme et identifié.

### Anonyme {#anonymous}

Cet état de connexion représente l'expérience d'un visiteur de votre application ou site web qui ne s'est pas encore connecté. Si vous initialisez Pilot en tant qu'utilisateur anonyme, Braze crée un [profil utilisateur anonyme]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) pour vous et enregistre les données relatives à votre activité dans ce profil. Les utilisateurs anonymes peuvent toujours être ciblés par des Campaigns, mais vous ne pourrez pas consulter leur profil utilisateur directement dans votre tableau de bord de Braze.

### Identifié {#identified}

Cet état de connexion signifie que Braze reconnaît votre profil utilisateur grâce à un identifiant unique qui vous a été attribué, appelé identifiant externe. Vous pouvez rechercher cet identifiant externe dans la page **Recherche d'utilisateurs** de votre tableau de bord afin de localiser votre profil utilisateur, qui stocke tous les attributs utilisateur et événements enregistrés depuis Pilot en fonction de votre activité dans l'application. Dans le tableau de bord de Braze, accédez à **Audience** > **Recherche d'utilisateurs**, saisissez votre **ID externe** Pilot et ouvrez le profil pour consulter les attributs et les événements.

### Type de connexion {#connection-type}

Pour vérifier votre type de connexion, regardez l'indicateur de statut en haut de l'application Pilot.

{% tabs local %}
{% tab Utilisateur anonyme  %}

**Anonyme** indique que vous enregistrez des données en tant qu'utilisateur anonyme. La zone de statut affiche le libellé **Anonyme** (par exemple, une icône de masque ou de navigation privée).

{% endtab %}
{% tab Utilisateur identifié %}

Si vous enregistrez des données en tant qu'utilisateur identifié, la zone de statut affiche **Utilisateur identifié** ainsi que votre ID externe.

{% endtab %}
{% tab Non connecté %}

**Non connecté** indique que vous n'avez pas encore initialisé la connexion du SDK Braze avec Pilot. La zone de statut indique que Pilot n'est pas encore connecté à votre espace de travail Braze.

{% endtab %}
{% endtabs %}

## Campaigns et Canvas {#campaigns-and-canvases}

Les Campaigns et les Canvas vous permettent d'envoyer des messages à vos utilisateurs.

- Les Campaigns sont idéales pour les messages uniques envoyés à un segment d'audience spécifique sur différents canaux.
- Les Canvas sont des workflows avancés qui vous permettent d'automatiser et d'orchestrer des parcours clients personnalisés sur plusieurs canaux. Dans un Canvas, vous pouvez mettre en place une logique de branchement, des délais, des points de décision et des événements de conversion pour guider les clients à travers une série d'interactions. Les Canvas contribuent à garantir une communication cohérente et sans heurts entre les différents points de contact, augmentant ainsi les chances d'engagement client et de conversion.

## Canaux de communication pris en charge {#supported-messaging-channels}

Braze Pilot prend actuellement en charge les [messages in-app]({{site.baseurl}}/in-app_messages), qui apparaissent dans votre application et permettent d'envoyer des messages au moment opportun pendant que l'utilisateur est activement engagé.

![Un message in-app dans l'application MovieCanon « Vous appréciez MovieCanon ? Recommandez-le à vos amis ! » avec la possibilité de saisir votre adresse e-mail pour envoyer une recommandation.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}