---
nav_title: Retour en stock
article_title: Retour en stock
page_order: 2
page_type: reference
description: "Cet article décrit comment utiliser un modèle Canvas de Braze pour stimuler les achats en notifiant vos utilisateurs lorsqu'un article est de nouveau en stock grâce à des messages personnalisés."
tool: Canvas
---

# Retour en stock {#back-in-stock}

> Utilisez le modèle de retour en stock pour créer des messages ciblant les utilisateurs qui ont précédemment consulté ou manifesté de l'intérêt pour un article en rupture de stock, mais désormais disponible à l'achat. Cela aide les utilisateurs à obtenir les produits qu'ils souhaitent en les sollicitant au moment critique où un produit redevient disponible.

Cet article vous guidera à travers un cas d'usage du modèle **Retour en stock**, conçu pour l'étape de conversion du cycle de vie de l'utilisateur. À la fin, vous aurez créé un Canvas qui envoie une notification push (web ou mobile), un SMS ou un e-mail aux utilisateurs lorsqu'un article est de nouveau en stock, ainsi que jusqu'à deux rappels.

## Conditions préalables {#prerequisites}

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un [catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create) contenant des informations sur votre article
- Les [notifications de retour en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications#back-in-stock-notifications) doivent être configurées pour l'article au sujet duquel vous souhaitez envoyer des messages aux utilisateurs

## Adapter le modèle à vos besoins {#tailoring-the-template-to-your-needs}

Imaginons que nous travaillons pour PantsLabyrinth, un détaillant de vêtements en vente directe spécialisé dans les pantalons habillés, les jeans, les culottes et bien d'autres types de pantalons. Nous pouvons utiliser le modèle de retour en stock pour notifier les clients sur différents canaux lorsqu'une paire de jeans populaire, le Classic Straight Leg, est de nouveau en stock.

Avant de créer le Canvas, nous [configurons un catalogue]({{site.baseurl}}/user_guide/data/activation/catalogs/create) contenant des informations sur notre inventaire de pantalons droits et [configurons les notifications de retour en stock]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications#setting-up-back-in-stock-notifications) pour le jean Classic Straight Leg. Nous avons fait en sorte que les utilisateurs s'abonnent aux notifications après avoir effectué l'événement personnalisé consistant à ajouter le jean Classic Straight Leg en favori dans l'application.

Pour accéder au modèle de retour en stock, lors de la création d'un nouveau Canvas, sélectionnez **Use a Canvas template** > **Braze templates**. Ensuite, à côté de **Back in Stock**, sélectionnez **Apply Template**. Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Configurer les détails {#step-1-set-up-the-details}

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Edit** à côté du nom du modèle.

![Le titre et la description actuels du Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Mettez à jour le nom du Canvas pour indiquer que le Canvas cible les utilisateurs lorsque notre produit Classic Straight Leg est de nouveau en stock.
3. Mettez à jour la description pour expliquer que ce Canvas contient des messages personnalisés.
4. Ajoutez l'étiquette **Back in Stock**, qui est imbriquée sous l'étiquette **Promotional**, afin de pouvoir filtrer sur la page d'accueil du Canvas.

![L'étape « Set Up Canvas Details » avec un nom de Canvas « Back in Stock - Classic Straight Leg » et une brève description du Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### Étape 2 : Affecter les événements de conversion {#step-2-assign-conversion-events}

Changez l'**événement de conversion principal - A** en **Make a specific purchase** et sélectionnez **Classic Straight Leg** pour le nom du produit.

![La section « Assign Conversion Events » pour le type d'événement de conversion d'achat du produit Classic Straight Leg avec une date limite de conversion de 7 jours.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### Étape 3 : Adapter la planification d'entrée {#step-3-tailor-the-entry-schedule}

Conservons la planification d'entrée en **Action-Based** afin que les utilisateurs entrent dans notre Canvas lorsqu'ils effectuent une action, que le modèle a déjà définie sur **Perform a Back in Stock Event**.

Nous apporterons deux ajustements à cette étape :

1. Sélectionnez le catalogue contenant les informations sur notre jean Classic Straight Leg, que nous avons nommé « Straight Leg Pants ».

![L'étape « Entry Schedule » pour un Canvas basé sur une action.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2. Définissez l'**heure de début (obligatoire)** sur la date et l'heure de début souhaitées.

![La section « Entry Window » avec une heure de début au 2 janvier 2025 à 0 h 00.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### Étape 4 : Sélectionner l'audience cible {#step-4-select-the-target-audience}

Nous définirons notre audience cible comme les utilisateurs les plus susceptibles d'acheter le jean Classic Straight Leg.

1. Sélectionnez notre segment cible, « Favorited - Classic Straight Leg Jeans », qui comprend les utilisateurs ayant ajouté notre jean Classic Straight Leg en favori sur notre application ou notre site web.
2. Sélectionnez un filtre pour inclure les utilisateurs ayant acheté « Jeans » plus de « 0 » fois.

![L'étape « Target Audience » avec le segment « Favorited - Classic Straight Leg Jeans ».]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3. Ajustez les contrôles d'entrée pour permettre aux utilisateurs de réintégrer le Canvas après la durée maximale du Canvas, afin de réduire la probabilité que les utilisateurs déclenchent la même étape simultanément.

![La section « Entry Controls » avec une case à cocher permettant aux utilisateurs de réintégrer ce Canvas avec une durée maximale du Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4. Ajustez les critères de sortie pour retirer les utilisateurs ayant effectué l'événement personnalisé de retrait des favoris du jean Classic Straight Leg.

![La section « Exit Criteria » avec une exception pour les utilisateurs qui effectuent l'événement personnalisé « Unfavorited ».]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### Étape 5 : Sélectionner vos paramètres d'envoi {#step-5-select-your-send-settings}

Nous conserverons les paramètres d'abonnement par défaut, de sorte que nous n'envoyons des messages qu'aux utilisateurs qui se sont abonnés ou ont opté pour la réception de messages ou de notifications, et nous ignorerons les autres paramètres (limite de fréquence, heures calmes et groupes initiateurs).

![L'étape « Send Settings » ciblant les utilisateurs qui sont abonnés ou ont opté pour la réception.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Étape 6 : Personnaliser votre Canvas {#step-6-customize-your-canvas}

Nous allons maintenant construire notre Canvas en personnalisant les canaux et le contenu qui seront envoyés aux utilisateurs. Comme nous utilisons les quatre canaux du modèle (notification push mobile et web, SMS et e-mail) et le filtre [Canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel), nous n'avons pas besoin d'en ajouter ou d'en supprimer.

{% alert tip %}
Vous pouvez utiliser les [propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) pour personnaliser les messages de votre Canvas en fonction du produit auquel vous faites référence.
{% endalert %}

Nous commencerons notre personnalisation en parcourant chaque étape de message pour mettre à jour le contenu.

1. Remplacez `!!YOURCATALOGHERE!!` par le nom de notre catalogue (« Straight_Leg_Pants »).
2. Remplacez `[0]` par le numéro d'index du jean Classic Straight Leg, qui est « 9 » car le jean est le dixième article dans le tableau `items` de notre catalogue. (Les tableaux sont indexés à partir de zéro en Liquid, donc le premier élément est `0` et non `1`.)
3. Répétez les étapes 1 et 2 pour toutes les étapes de message restantes, y compris :
    - Le message « In-Product Msg & Email » qui s'envoie après le délai d'un jour
    - Les messages « Push+Email Alert » qui s'envoient aux utilisateurs n'ayant pas effectué d'achat
4. Mettez à jour l'étape Parcours d'actions en sélectionnant le groupe d'actions **Purchase**. Ensuite, sélectionnez **Make a specific purchase** et choisissez le jean Classic Straight Leg pour le produit.

![Étape Canvas de notification push mobile avec un message notifiant les utilisateurs qu'un produit est de nouveau en stock.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### Étape 7 : Tester et lancer votre Canvas {#step-7-test-and-launch-your-canvas}

Après avoir testé et vérifié que notre Canvas fonctionne comme prévu, nous le lancerons en sélectionnant **Launch Canvas**. Désormais, nos utilisateurs qui ont ajouté notre jean Classic Straight Leg en favori et qui se sont abonnés à nos canaux de communication recevront des notifications lorsqu'il sera de nouveau en stock !

{% alert tip %}
Consultez notre [liste de vérification pré et post-lancement]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) pour les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}