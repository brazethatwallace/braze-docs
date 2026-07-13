---
nav_title: Composants Canvas
article_title: Composants Canvas
page_order: 3
alias: "/user_guide/messaging/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Composants Canvas"
guide_top_text: "Améliorez vos parcours Canvas grâce aux composants Canvas. Les composants Canvas simplifient le processus d'évaluation de l'efficacité de votre Canvas en remplaçant de nombreuses étapes complètes par une seule. Les composants d'un Canvas correspondent au parcours utilisateur personnalisé dans les branches de votre Canvas."

page_type: landing
description: "Cette page d'accueil regroupe les articles sur les composants Canvas qui vous aideront à créer des Canvas plus avancés. Parmi ces composants, on trouve l'étape de message, l'étape de délai, l'étape de l'arbre décisionnel, et bien d'autres."
tool: Canvas

guide_featured_title: "Articles de la section"
guide_featured_list:
  - name: Étape Parcours d'actions
    link: /docs/user_guide/messaging/canvas/canvas_components/action_paths
    image: /assets/img/braze_icons/zap.svg
  - name: Étape Agent
    link: /docs/user_guide/messaging/canvas/canvas_components/agent_step
    image: /assets/img/braze_icons/briefcase-01.svg
  - name: Étape Parcours d'audience
    link: /docs/user_guide/messaging/canvas/canvas_components/audience_paths
    image: /assets/img/braze_icons/users-01.svg
  - name: Étape Audience Sync
    link: /docs/partners/canvas_audience_sync
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: Étape Optimiseur de contenu
    link: /docs/user_guide/messaging/canvas/canvas_components/content_optimizer_step
    image: /assets/img/braze_icons/target-04.svg
  - name: Étape Contexte
    link: /docs/user_guide/messaging/canvas/canvas_components/context
    image: /assets/img/braze_icons/file-search-02.svg
  - name: Étape Arbre décisionnel
    link: /docs/user_guide/messaging/canvas/canvas_components/decision_split
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Étape de délai
    link: /docs/user_guide/messaging/canvas/canvas_components/delay_step
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Étape Chemins d'expérience
    link: /docs/user_guide/messaging/canvas/canvas_components/experiment_step
    image: /assets/img/braze_icons/columns-01.svg
  - name: Indicateurs de fonctionnalité
    link: /docs/user_guide/messaging/canvas/canvas_components/feature_flags
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Étape de message
    link: /docs/user_guide/messaging/canvas/canvas_components/message_step
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Étape Envoyer vers la destination
    link: /docs/user_guide/messaging/canvas/canvas_components/send_to_destination
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: Étape Mise à jour utilisateur
    link: /docs/user_guide/messaging/canvas/canvas_components/user_update
    image: /assets/img/braze_icons/user-check-01.svg
---

## À propos des composants Canvas {#about-canvas-components}

Les composants Canvas vous permettent de créer de nouveaux parcours utilisateur pour optimiser vos processus et renforcer l'efficacité de vos communications.

### Personnaliser les parcours utilisateur {#customizing-user-journeys}

![Exemple de parcours utilisateur Canvas avec une étape Arbre décisionnel suivie d'étapes de délai et d'étapes de message.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Utilisez les [Parcours d'actions]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) pour diviser votre parcours utilisateur en fonction des actions et des événements d'engagement, comme un achat. Si vous souhaitez filtrer et cibler vos audiences, les [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) simplifient le ciblage de vos utilisateurs en les orientant vers différents chemins Canvas selon des critères d'audience.

Les composants [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) reposent sur une logique simple de type « oui ou non » pour créer deux chemins mutuellement exclusifs dans vos parcours utilisateur, basés sur une action ou un attribut utilisateur. Cela vous aide à identifier et cibler vos groupes d'utilisateurs.

Les composants [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) vous permettent de retarder une étape individuelle de votre Canvas. Cette étape de délai autonome est idéale pour envoyer des messages à vos utilisateurs à un moment précis. De plus, les composants de délai peuvent élargir la portée de votre audience en laissant davantage de temps à vos utilisateurs pour remplir les critères du composant.

### Tests {#testing}

Lors de la création de vos parcours utilisateur, vous pouvez également tester quel chemin Canvas est le plus efficace. Grâce aux [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step), vous pouvez tester plusieurs chemins Canvas à n'importe quelle étape. Vous pouvez aussi utiliser les connexions entre les étapes comme aperçu général. Les connexions orange indiquent que l'étape précédente fait passer immédiatement les utilisateurs à l'étape suivante.

### Intégration {#integration}

Vous souhaitez synchroniser les données first-party de votre marque ? Tirez parti des options d'Audience Sync disponibles pour [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) et [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync).