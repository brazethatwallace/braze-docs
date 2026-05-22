---
nav_title: Panier abandonné
article_title: Panier abandonné
page_order: 1
page_type: reference
description: "Cet article décrit comment utiliser un modèle Canvas de Braze pour interagir avec les utilisateurs en temps réel afin de les encourager à finaliser leurs achats."
tool: Canvas
---

# Panier abandonné {#abandoned-cart}

> Interagissez avec les utilisateurs en temps réel pour les encourager à finaliser leurs achats. Utilisez ce modèle pour créer un parcours utilisateur axé sur l'envoi de messages personnalisés et opportuns qui rappellent aux utilisateurs leurs paniers abandonnés en mettant en avant les avantages des produits et en proposant des incitations, telles que des codes de réduction.

Dans cet article, nous allons parcourir un cas d'utilisation du modèle **Abandoned Intent**, conçu pour la phase de considération du cycle de vie de l'utilisateur. À la fin de cet article, vous aurez personnalisé un parcours utilisateur qui encourage les achats des utilisateurs n'ayant pas finalisé leurs commandes après avoir ajouté des articles à leur panier.

## Conditions préalables {#prerequisites}

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un Canvas de parcours utilisateur post-achat séparé, car effectuer un achat dans ce Canvas entraînera la sortie des utilisateurs du Canvas.
- Une [synchronisation d'audience Braze]({{site.baseurl}}/partners/canvas_audience_sync/) configurée avec les partenaires et audiences que vous utilisez.

## Adapter le modèle à vos besoins {#tailoring-the-template-to-your-needs}

Imaginons que nous travaillons chez Kitchenerie, une marque de vente au détail spécialisée dans les ustensiles de cuisine, et que notre objectif est de réengager les utilisateurs qui ont ajouté le dernier produit « Enormous Paper Plate » à leur panier mais n'ont pas finalisé leur achat.

Avant de créer le Canvas, nous avons configuré l'intégration [Synchronisation d'audience Braze vers Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) afin de pouvoir ajouter des données utilisateur de Braze aux audiences Facebook pour envoyer des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore.

Pour accéder au modèle d'intention abandonnée, lors de la création d'un nouveau Canvas, sélectionnez **Use a Canvas template** > **Braze templates**. Ensuite, à côté de **Abandoned Intent**, sélectionnez **Apply Template**. Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Configurer les détails {#step-1-set-up-the-details}

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Edit** à côté du nom du modèle.

![Le titre et la description actuels du Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Mettez à jour le nom du Canvas pour indiquer qu'il cible les utilisateurs ayant des paniers abandonnés.
3. Mettez à jour la description pour préciser que le Canvas vise à encourager les utilisateurs à finaliser leurs achats lors du dernier lancement saisonnier d'ustensiles de cuisine.
4. Ajoutez l'étiquette **Abandon Cart** afin de pouvoir filtrer par celle-ci sur la page d'accueil Canvas.

![Le nouveau nom, la nouvelle description et la nouvelle étiquette du Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Étape 2 : Affecter vos événements de conversion {#step-2-assign-your-conversion-events}

Ensuite, affectons notre événement de conversion. Comme nous nous concentrons sur notre produit « Enormous Paper Plate », nous allons procéder comme suit pour l'**événement de conversion principal A** :

1. Pour le **type d'événement de conversion**, sélectionnez **Makes Purchase**.
2. Sélectionnez **Make a specific purchase**. Cela nous permet de sélectionner un nom de produit spécifique.
3. Sélectionnez **Enormous Paper Plate**.

![Événement de conversion principal - A avec le type de conversion « Makes Purchase » et le nom de produit « Enormous Paper Plate ». Il y a un délai de conversion de 3 jours.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### Étape 3 : Définir une planification d'entrée {#step-3-set-an-entry-schedule}

Bien que la planification d'entrée de ce modèle soit définie sur **API-Triggered**, notre cas d'utilisation bénéficiera davantage d'une entrée basée sur une action pour ce Canvas, car nous souhaitons cibler les utilisateurs qui ont abandonné leur panier (ce qui est une action).

1. Sélectionnez **Action-Based** comme type de planification d'entrée.
2. Sélectionnez **Abandoned Cart** comme déclencheur.
3. Pour la fenêtre d'entrée, sélectionnez la date de début.
4. Sélectionnez l'option permettant aux utilisateurs d'entrer dans leur fuseau horaire local. Cela peut maintenir la pertinence de nos messages et conduire à un engagement plus élevé si les messages sont envoyés à des moments optimaux.

![Un Canvas basé sur une action qui cible les utilisateurs ayant abandonné leur panier, avec une fenêtre d'entrée le 15 octobre 2024 à 15h20 dans le fuseau horaire local des utilisateurs.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### Étape 4 : Déterminer qui entre dans le Canvas {#step-4-determine-who-enters-the-canvas}

Ensuite, définissons notre audience cible comme les utilisateurs ayant fait des achats exclusivement en ligne chez nous au cours des 90 derniers jours. Cela nous aide à restreindre notre audience aux utilisateurs dont nous savons qu'ils sont engagés avec nos produits.

![« Online Shoppers Segment - 90 Days » comme Segment d'utilisateurs à cibler pour ce Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Nous laisserons les contrôles d'entrée tels quels, de sorte que les utilisateurs ne soient pas autorisés à réentrer dans ce Canvas et qu'il n'y ait pas de limite au nombre de personnes pouvant potentiellement y entrer.

Pour les critères de sortie, les utilisateurs quitteront le Canvas s'ils ont acheté le « Enormous Paper Plate ». De cette façon, ils ne recevront pas de messages supplémentaires concernant un article qu'ils ont déjà acheté.

![Critères de sortie déterminant que les utilisateurs effectuant un achat spécifique du « Enormous Paper Plate » quitteront le Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### Étape 5 : Sélectionner vos paramètres d'envoi {#step-5-select-your-send-settings}

Nous conserverons les paramètres d'abonnement par défaut, de sorte que nous n'envoyons des messages qu'aux utilisateurs qui se sont abonnés ou ont opté pour la réception de messages ou de notifications, et nous laisserons les autres paramètres tels quels.

### Étape 6 : Personnaliser votre Canvas {#step-6-customize-your-canvas}

Maintenant, nous allons construire notre Canvas en personnalisant les étapes du modèle :

1. Sélectionnez l'étape Parcours d'actions, puis sélectionnez le nom du groupe d'actions **Made purchase**.
2. Pour **Make Purchase**, sélectionnez **Make A Specific Purchase** et choisissez **Enormous Paper Plate** pour le produit. Comme pour les critères de sortie, les utilisateurs qui achètent ce produit quitteront le Canvas.

![Groupe d'actions « Made purchase » qui entraînera la sortie du Canvas si l'utilisateur achète le « Enormous Paper Plate ».]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3. Pour l'étape Message, sélectionnez **Edit message** pour personnaliser l'e-mail qui sera envoyé à nos utilisateurs, les informant des articles dans leur panier abandonné.
4. Conservez l'étape Délai telle quelle.
5. Dans les étapes Message suivant l'étape Parcours d'audience, nous personnaliserons l'e-mail et le message SMS que nos utilisateurs recevront. C'est ici que nous souhaitons encourager nos utilisateurs à acheter des produits avec des messages personnalisés.

![Un aperçu du message SMS que les utilisateurs recevront : « Hi there, you left the enormous paper plate behind in your cart! Complete your purchase now and step up your hosting game. Use code MYPLATE at checkout for 20 percent off your order! »]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6. Dans l'étape Parcours d'actions suivante, sélectionnez le groupe d'actions **Made purchase**. Ensuite, sélectionnez **Make a specific purchase** et choisissez **Enormous Paper Plate** pour le produit. Cette étape reproduira la première étape Parcours d'actions en faisant sortir les utilisateurs qui ont acheté notre produit afin qu'ils ne reçoivent plus de messages.
7. Assurez-vous que notre étape de synchronisation d'audience est configurée pour se synchroniser avec Facebook. Cela aidera davantage au reciblage publicitaire.

{% alert tip %}
Vous pouvez utiliser les [propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) pour personnaliser les messages de votre Canvas en fonction du produit auquel vous faites référence.
{% endalert %}

### Étape 7 : Tester et lancer le Canvas {#step-7-test-and-launch-the-canvas}

Après avoir testé et vérifié que notre Canvas fonctionne comme prévu, sélectionnez **Launch Canvas** pour lancer le Canvas. Nous pouvons désormais cibler de manière réfléchie les utilisateurs avec un parcours personnalisé pour les encourager à finaliser l'achat du produit qu'ils ont ajouté à leur panier !

{% alert tip %}
Consultez notre [liste de vérification pré et post-lancement]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) pour les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}