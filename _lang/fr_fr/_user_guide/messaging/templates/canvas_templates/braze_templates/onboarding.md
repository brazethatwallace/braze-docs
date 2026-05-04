---
nav_title: Onboarding
article_title: Onboarding
page_order: 5
page_type: reference
description: "Cet article décrit comment utiliser un modèle Canvas de Braze pour créer des parcours d'onboarding qui favorisent une adoption initiale solide et encouragent des relations durables avec vos utilisateurs."
tool: Canvas
---

# Onboarding

> Lancez le parcours de vos utilisateurs avec ce modèle d'onboarding. Ce modèle est conçu pour favoriser une adoption initiale solide et encourager des relations durables avec vos utilisateurs. En tirant parti d'une communication personnalisée et d'un ensemble structuré de messages, vous pouvez présenter votre marque à vos utilisateurs de façon fluide et initier le début d'une relation durable.

Dans cet article, nous allons vous présenter un cas d'utilisation du modèle **Onboarding**, destiné à la phase de considération du cycle de vie de l'utilisateur, afin de créer un parcours d'onboarding fluide pour les nouveaux utilisateurs. À la fin de cet article, vous aurez personnalisé ce modèle Canvas de Braze avec des messages adaptés à ces nouveaux utilisateurs.

## Conditions préalables {#prerequisites}

Avant d'utiliser ce modèle, vous devez créer les [modèles d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template/) suivants à référencer dans le Canvas :

- Un e-mail de bienvenue pour tous les utilisateurs de votre application
- Un e-mail contenant des conseils sur l'utilisation de votre application
- Un e-mail de feedback incluant un sondage utilisateur

## Adapter le modèle à vos besoins {#tailoring-the-template-to-your-needs}

Imaginons que nous travaillons chez PantsLabyrinth et que notre objectif est d'améliorer l'engagement des utilisateurs, de bâtir la confiance et la fidélité avec nos utilisateurs, et de les encourager à rester engagés. Pour ce faire, nous souhaitons nous concentrer sur la création de messages ciblant les nouveaux utilisateurs qui n'ont pas encore interagi avec l'application.

Pour accéder au modèle d'onboarding, lors de la création d'un nouveau Canvas, sélectionnez **Use a Canvas template** > **Braze templates**. Ensuite, à côté de **Onboarding**, sélectionnez **Apply Template**. Commençons à personnaliser ce modèle pour l'adapter à notre cas d'utilisation.

### Étape 1 : Configurer les détails {#step-1-set-up-the-details}

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Edit** à côté du nom du modèle.

![Le titre et la description actuels du Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Mettez à jour le nom du Canvas pour indiquer qu'il est destiné à l'onboarding des nouveaux utilisateurs.
3. Mettez à jour la description pour préciser que le Canvas trace un parcours utilisateur qui favorise la confiance et la fidélité.
4. Ajoutez l'étiquette **Onboarding** afin de pouvoir filtrer le Canvas sur la page d'accueil Canvas.

![Le nouveau nom, la nouvelle description et la nouvelle étiquette du Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### Étape 2 : Affecter vos événements de conversion {#step-2-assign-your-conversion-events}

Ensuite, affectons nos événements de conversion. Les événements de conversion sont un type d'indicateur qui peut être utilisé pour mesurer le succès du Canvas. Pour **Custom event name**, sélectionnez **Email Click** comme événement personnalisé.

![Événement de conversion principal - A avec le type de conversion « Performs Custom Event » et le nom d'événement personnalisé « Email Click ». Le délai de conversion est de 4 jours.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

Cela signifie que les nouveaux utilisateurs disposent de quatre jours maximum pour cliquer sur l'e-mail de bienvenue. Dans ce cas, nous souhaitons que nos nouveaux utilisateurs ressentent un sentiment d'urgence à interagir avec PantsLabyrinth et à s'abonner à une livraison récurrente de vêtements de saison.

### Étape 3 : Définir une planification d'entrée {#step-3-set-an-entry-schedule}

Puisque l'objectif est de cibler les nouveaux utilisateurs de PantsLabyrinth, nous conserverons le Canvas en mode basé sur les actions. Pour **Start Session**, sélectionnez **Start Session in Any App** afin de permettre aux utilisateurs qui démarrent une session dans n'importe quelle application d'entrer dans le Canvas.

Ensuite, ajustez la **Entry Window** pour déterminer quand les utilisateurs peuvent entrer dans le Canvas. Supposons qu'un lancement d'abonnement PantsLabyrinth est prévu fin octobre. C'est ici que nous définirons l'heure de début sur **2024/10/28 8:00 am**. Facultativement, nous pouvons également permettre aux utilisateurs d'entrer dans le Canvas dans leur fuseau horaire local.

![Une fenêtre d'entrée avec l'heure de début le 28 octobre 2024 à 8 h. Les utilisateurs entreront dans ce message dans leur fuseau horaire local.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### Étape 4 : Cibler votre audience {#step-4-target-your-audience}

En ciblant la bonne audience, nous pouvons interagir efficacement avec les nouveaux utilisateurs. Par exemple, ce modèle cible tous les utilisateurs qui ont utilisé une application pour la première fois il y a moins d'un jour, ce qui correspond à notre cas d'utilisation. Nous laisserons donc cette section telle quelle.

### Étape 5 : Définir les paramètres d'envoi {#step-5-set-send-settings}

Par défaut, ce Canvas est envoyé aux utilisateurs qui sont abonnés ou ont donné leur accord et respecte les règles de limite de fréquence. Nous conserverons ces paramètres tels quels.

### Étape 6 : Personnaliser votre Canvas {#step-6-customize-your-canvas}

Maintenant, construisons le Canvas en personnalisant les étapes du modèle.

#### Configurer l'e-mail de bienvenue {#set-up-the-welcome-email}

1. Sélectionnez l'étape Message nommée « Welcome Email ».
2. Sélectionnez **Edit message** pour remplacer l'e-mail du modèle par notre e-mail de bienvenue.
3. Sélectionnez **Done**.

Désormais, nos utilisateurs recevront cet e-mail de bienvenue après avoir démarré une session dans notre application. Pour ne pas submerger les utilisateurs avec des messages répétés, nous recommandons d'utiliser l'étape Délai dans le parcours utilisateur.

#### Personnaliser le parcours d'audience {#customize-the-audience-path}

Dans l'étape Parcours d'audience nommée **Audience Split**, nous pouvons personnaliser le filtre pour nos utilisateurs engagés. Dans le modèle, le filtre est **Has clicked email for step Welcome Email**, ce qui signifie que les utilisateurs sont répartis en deux groupes : ceux qui ont cliqué sur l'e-mail de bienvenue et ceux qui ne l'ont pas fait.

![Une étape Audience Split avec un parcours pour les utilisateurs engagés et un parcours pour tous les autres.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

En tant que détaillant de vêtements en ligne, PantsLabyrinth dispose également d'un groupe actif d'utilisateurs mobiles. Ainsi, dans un Canvas d'onboarding séparé, nous pouvons également sélectionner le filtre suivant pour identifier et répartir nos utilisateurs mobiles dans ces segments :

- **Has clicked content card for step Welcome Content Card**
- **Everyone Else**

#### Cibler davantage d'utilisateurs avec les parcours d'audience {#target-more-users-with-audience-paths}

À partir de l'ensemble des utilisateurs qui n'ont pas interagi avec notre application, nous pouvons cibler davantage ces utilisateurs en modifiant l'étape « Check for Clicks » et l'étape « Winback Nudge ».

### Étape 7 : Tester et lancer votre Canvas {#step-7-test-and-launch-your-canvas}

Après avoir testé et vérifié que notre Canvas fonctionne comme prévu, sélectionnez **Launch Canvas** pour lancer le Canvas. Nous pouvons désormais offrir à nos nouveaux utilisateurs une expérience d'onboarding personnalisée pour encourager une relation durable !

{% alert tip %}
Consultez notre [checklist pré et post-lancement]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) pour les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}