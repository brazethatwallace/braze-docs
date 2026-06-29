---
nav_title: Intention abandonnée
article_title: Intention abandonnée
page_order: 1
page_type: reference
description: "Cet article décrit comment utiliser un modèle Canvas de Braze pour interagir avec les utilisateurs en temps réel afin de les encourager à finaliser leurs achats."
tool: Canvas
---

# Intention abandonnée {#abandoned-intent}

> Interagissez avec les utilisateurs en temps réel pour les encourager à finaliser leurs achats tant que les produits sont encore présents à l'esprit. Ce modèle déclenché par API fait entrer les utilisateurs immédiatement lorsqu'ils abandonnent un panier, envoie des rappels opportuns sur le canal optimal (e-mail, SMS ou message in-app), vérifie la finalisation de l'achat à deux points du parcours et synchronise les utilisateurs qui ne convertissent pas vers des audiences publicitaires pour le reciblage.

Dans cet article, nous allons parcourir un cas d'utilisation du modèle **Abandoned Intent**, conçu pour la phase de considération du cycle de vie de l'utilisateur. À la fin de cet article, vous aurez personnalisé un parcours utilisateur qui encourage les achats des utilisateurs n'ayant pas finalisé leurs commandes après avoir ajouté des articles à leur panier.

{% alert tip %}
Utilisez [BrazeAI Operator<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/operator/) pour configurer et personnaliser ce modèle. Sélectionnez **BrazeAI Operator<sup>TM</sup>** à côté de votre profil utilisateur lors de la création ou de la modification de votre Canvas. Décrivez ensuite votre objectif, par exemple « Aidez-moi à configurer le modèle Abandoned Intent pour réengager les utilisateurs qui ont abandonné leur panier ».
{% endalert %}

## Conditions préalables {#prerequisites}

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un Canvas de parcours utilisateur post-achat séparé, car effectuer un achat dans ce Canvas entraînera la sortie des utilisateurs du Canvas.
- Une [synchronisation d'audience Braze]({{site.baseurl}}/partners/canvas_audience_sync/) configurée avec les partenaires et audiences que vous utilisez.

## Adapter le modèle à vos besoins {#tailoring-the-template-to-your-needs}

Imaginons que nous travaillons chez Kitchenerie, une marque de vente au détail spécialisée dans les ustensiles de cuisine, et que notre objectif est de réengager les utilisateurs qui ont ajouté le dernier produit « Enormous Paper Plate » à leur panier mais n'ont pas finalisé leur achat.

Avant de créer le Canvas, nous avons configuré l'intégration [Synchronisation d'audience Braze vers Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) afin de pouvoir ajouter des données utilisateur de Braze aux audiences Facebook pour envoyer des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore.

Le modèle **Abandoned Intent** suit ce flux : vérification de l'achat, envoi d'un rappel immédiat, attente, routage vers le canal optimal, relance, nouvelle vérification et reciblage des non-convertis. Il comprend les étapes suivantes :

| Étape du Canvas | Nom de l'étape dans le modèle | Objectif |
|---|---|---|
| Parcours d'actions | Made purchase? | Première vérification de finalisation ; les utilisateurs ayant déjà acheté sortent du Canvas. |
| Message | Itemized Reminder | Rappel immédiat du panier envoyé juste après l'entrée. |
| Délai | Delay | Attente de 30 minutes pour que la relance arrive alors que le produit est encore présent à l'esprit. |
| Parcours d'audience | Intelligent Channel split | Oriente les utilisateurs vers l'e-mail ou le SMS en fonction du classement [Canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/). |
| Message | Abandoned Cart Email, Abandoned Cart SMS et Abandoned Cart In-App Message | Relances spécifiques par canal. Le canal intelligent choisit entre l'e-mail et le SMS ; le message in-app est envoyé sur un parcours distinct dans le modèle. |
| Parcours d'actions | Made purchase? (2) | Deuxième vérification de finalisation avant le reciblage. |
| Audience Sync | Ad Retargeting | Synchronise les non-convertis vers des audiences publicitaires (comme Facebook) pour un reciblage hors canal. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Étapes du modèle Abandoned Intent" }

### Étape 1 : Configurer les détails {#step-1-set-up-the-details}

Appliquons le modèle Canvas et mettons à jour les détails pour refléter notre objectif.

1. Accédez à **Messaging** > **Canvas**.
2. Sélectionnez **Create Canvas** > **Use a Canvas Template**.
3. Sélectionnez l'onglet **Braze templates**, puis sélectionnez **Apply Template** à côté de **Abandoned Intent**.
4. Mettez à jour la description pour préciser que le Canvas vise à encourager les utilisateurs à finaliser leurs achats lors du dernier lancement saisonnier d'ustensiles de cuisine.
5. Ajoutez l'étiquette **Intent** afin de pouvoir filtrer par celle-ci sur la page d'accueil Canvas.

![Le nouveau nom, la nouvelle description et la nouvelle étiquette du Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Étape 2 : Affecter vos événements de conversion {#step-2-assign-your-conversion-events}

Le modèle définit l'**événement de conversion principal A** sur **Makes Purchase (Legacy)** avec **Make any purchase (Legacy)** sélectionné par défaut. Comme nous nous concentrons sur notre produit « Enormous Paper Plate », nous personnalisons l'événement de conversion comme suit :

1. Sélectionnez **Make a specific purchase (Legacy)**.
2. Pour **Product name**, saisissez **Enormous Paper Plate**.

![Événement de conversion principal - A avec le type de conversion « Makes Purchase » et le nom de produit « Enormous Paper Plate ». Il y a un délai de conversion de 3 jours.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

{% alert note %}
Si votre espace de travail utilise l'événement de conversion **Places order**, les options liées aux achats peuvent apparaître avec **(Legacy)** dans le libellé. Les étapes de cet article utilisent le flux de conversion d'achat legacy.
{% endalert %}

### Étape 3 : Définir une planification d'entrée {#step-3-set-an-entry-schedule}

Le modèle **Abandoned Intent** utilise une planification d'entrée **API-Triggered** afin de faire entrer les utilisateurs dans le Canvas dès qu'ils abandonnent leur panier. Cela correspond à notre cas d'utilisation, car nous souhaitons réagir tant que le produit est encore présent à l'esprit.

1. Conservez **API-Triggered** comme type de planification d'entrée.
2. Notez l'identifiant du Canvas et utilisez l'[endpoint `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) pour ajouter des utilisateurs lorsque votre application ou site web détecte un panier abandonné.
3. Vous pouvez éventuellement transmettre des [variables de contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) (comme le nom du produit ou les détails du panier) pour personnaliser les messages en aval.

Si vous préférez une entrée basée sur une action, sélectionnez **Action-Based** et choisissez un déclencheur correspondant à la façon dont votre marque suit les paniers abandonnés, par exemple **Perform Custom Event** pour un événement `abandoned_cart` enregistré.

### Étape 4 : Déterminer qui entre dans le Canvas {#step-4-determine-who-enters-the-canvas}

Ensuite, définissons notre audience cible comme les utilisateurs ayant fait des achats exclusivement en ligne chez nous au cours des 90 derniers jours. Cela nous aide à restreindre notre audience aux utilisateurs dont nous savons qu'ils sont engagés avec nos produits.

![« Online Shoppers Segment - 90 Days » comme segment d'utilisateurs à cibler pour ce Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Nous laissons les contrôles d'entrée tels quels, de sorte que les utilisateurs ne soient pas autorisés à réentrer dans ce Canvas et qu'il n'y ait pas de limite au nombre de personnes pouvant potentiellement y entrer.

Le modèle ne définit pas de critères de sortie globaux par défaut. Les utilisateurs sortent plutôt lorsqu'ils effectuent un achat dans les étapes Parcours d'actions **Made purchase?**, que nous personnaliserons à l'étape 6.

### Étape 5 : Sélectionner vos paramètres d'envoi {#step-5-select-your-send-settings}

Nous conservons les paramètres d'abonnement par défaut, de sorte que nous n'envoyons des messages qu'aux utilisateurs qui se sont abonnés ou ont opté pour la réception de messages ou de notifications, et nous laissons les autres paramètres tels quels.

### Étape 6 : Personnaliser votre Canvas {#step-6-customize-your-canvas}

Personnalisez les étapes du Canvas dans l'ordre dans lequel les utilisateurs les parcourent :

#### Vérifier l'achat à l'entrée {#check-for-purchase-at-entry}

1. Sélectionnez l'étape Parcours d'actions **Made purchase?**, puis sélectionnez le groupe d'actions **Made purchase**.
2. Pour **Make Purchase**, sélectionnez **Make a specific purchase (Legacy)** et choisissez **Enormous Paper Plate** pour le produit. Les utilisateurs qui achètent ce produit sortiront du Canvas.

#### Envoyer le rappel immédiat {#send-the-immediate-reminder}

1. Sélectionnez l'étape Message **Itemized Reminder**, puis sélectionnez **Edit message** pour personnaliser le premier e-mail de rappel. Ce message est envoyé immédiatement après l'entrée, avant le délai.
2. Conservez l'étape **Delay** telle quelle. Le modèle utilise un délai de 30 minutes avant l'envoi des messages de relance, laissant aux utilisateurs le temps de finaliser leur commande tant que le produit est encore présent à l'esprit.

{% alert tip %}
Vous pouvez utiliser les [propriétés de contexte Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) pour personnaliser les messages de votre Canvas en fonction du produit auquel vous faites référence.
{% endalert %}

#### Orienter vers le canal optimal {#route-to-the-optimal-channel}

1. Examinez l'étape Parcours d'audience **Intelligent Channel split**. Elle oriente les utilisateurs vers **Abandoned Cart Email** ou **Abandoned Cart SMS** en fonction du classement [Canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel/). Ajustez les parcours si nécessaire.
2. Personnalisez les étapes **Abandoned Cart Email**, **Abandoned Cart SMS** et **Abandoned Cart In-App Message**. Sélectionnez **Edit message** sur chaque étape pour mettre à jour le contenu et le message pour ce canal. Le message in-app s'exécute sur un parcours distinct de la répartition par canal intelligent et n'est pas sélectionné par le classement du canal intelligent.

#### Recibler les non-convertis {#retarget-non-converters}

1. Sélectionnez l'étape Parcours d'actions **Made purchase? (2)**, puis sélectionnez le groupe d'actions **Made purchase**.
2. Sélectionnez **Make a specific purchase (Legacy)** et choisissez **Enormous Paper Plate** pour le produit. Les utilisateurs qui achètent ici sortent du Canvas avant d'atteindre le reciblage.
3. Sélectionnez l'étape Audience Sync **Ad Retargeting** et configurez-la pour se synchroniser avec Facebook. Les utilisateurs qui atteignent cette étape n'ont pas acheté — synchronisez-les vers votre audience publicitaire pour un reciblage hors canal.

### Étape 7 : Tester et lancer le Canvas {#step-7-test-and-launch-the-canvas}

Après avoir testé et vérifié que notre Canvas fonctionne comme prévu, sélectionnez **Launch Canvas** pour lancer le Canvas. Nous pouvons désormais cibler de manière réfléchie les utilisateurs avec un parcours personnalisé pour les encourager à finaliser l'achat du produit qu'ils ont ajouté à leur panier !

{% alert tip %}
Consultez notre [liste de vérification pré et post-lancement]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) pour les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}