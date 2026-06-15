---
nav_title: Retour d'expérience post-achat
article_title: Retour d'expérience post-achat
page_order: 6
page_type: reference
description: "Cet article décrit comment utiliser un modèle Canvas de Braze pour orchestrer des expériences personnalisées qui vous permettent de répondre aux retours d'expérience et de construire une relation avec vos utilisateurs."
tool: Canvas
---

# Retour d'expérience post-achat {#post-purchase-feedback}

> Utilisez le modèle de retour d'expérience post-achat pour obtenir des informations essentielles sur la façon dont vos clients interagissent avec votre marque et vous assurer qu'ils continuent à vivre des expériences positives. En tirant parti d'une communication personnalisée et d'un ensemble structuré de messages, vous pouvez continuer à construire et à entretenir vos relations clients.

Cet article vous guidera à travers un cas d'utilisation du modèle **Post-Purchase Feedback**, conçu pour l'étape de conversion du cycle de vie utilisateur. À la fin, vous aurez créé un Canvas qui encourage les utilisateurs à fournir des retours d'expérience pour votre application.

## Conditions préalables {#prerequisites}

Pour utiliser ce modèle avec succès, vous aurez besoin des éléments suivants :

- Un [attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes) à référencer pour les résultats de l'enquête de satisfaction.
- Une intégration [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) configurée avec les partenaires et audiences que vous utilisez.

## Adapter le modèle à vos besoins {#tailoring-the-template-to-your-needs}

Imaginons que nous travaillons pour Decorumsoft, un développeur de jeux vidéo mobiles. Nous utiliserons le modèle de retour d'expérience post-achat pour évaluer les retours sur le lancement de notre dernier jeu vidéo, Proxy War 3: War of Thirst. Grâce à ces retours, nous orienterons nos plans de développement pour le pack d'extension, Liquid Mirage.

Avant de créer le Canvas, nous avons configuré l'intégration [Braze Audience Sync vers Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) afin de pouvoir ajouter des données utilisateur de Braze aux audiences Google pour envoyer des publicités basées sur des déclencheurs comportementaux, la segmentation, et plus encore.

Pour accéder au modèle de retour d'expérience post-achat, lors de la création d'un nouveau Canvas, sélectionnez **Use a Canvas template** > **Braze templates**. Ensuite, à côté de **Post-Purchase Feedback**, sélectionnez **Apply Template**. Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Configurer les détails du Canvas {#step-1-set-up-canvas-details}

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Edit** à côté du nom du modèle.

![Le titre et la description actuels du Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2. Mettez à jour le nom du Canvas pour préciser qu'il cible les utilisateurs récents.
3. Mettez à jour la description pour préciser que le Canvas vise à encourager les utilisateurs à soumettre des retours d'expérience.
4. Ajoutez l'étiquette **Feedback** pour le filtrer sur la page d'accueil Canvas.

![Le nouveau nom et la nouvelle description du Canvas. La nouvelle description indique : « Un Canvas de retour d'expérience post-achat pour évaluer l'intérêt pour la prochaine extension de PWD3, Liquid Mirage. »]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### Étape 2 : Attribuer les événements de conversion {#step-2-assign-conversion-events}

Ensuite, attribuons nos événements de conversion. Mettez à jour l'**événement de conversion principal - A** sur **Make a specific purchase** et sélectionnez **Proxy War**.

![Section « Attribuer les événements de conversion » pour le type d'événement de conversion correspondant à l'achat du produit de jeu Proxy War.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

Nous conserverons la date limite de conversion de trois jours du modèle, car nous souhaitons cibler nos utilisateurs les plus récents.

### Étape 3 : Définir une planification d'entrée {#step-3-set-an-entry-schedule}

1. Conservez le type de planification d'entrée sur **Action-Based**.
2. Définissez l'**heure de début** de la fenêtre d'entrée à la date de lancement du jeu.

### Étape 4 : Déterminer qui entre dans le Canvas {#step-4-determine-who-enters-the-canvas}

Notre audience cible pour les retours d'expérience est constituée des utilisateurs qui ont récemment acheté Proxy War 3.

1. Sélectionnez notre segment cible, « Purchased Proxy War 3 », qui regroupe les utilisateurs ayant acheté le jeu.
2. Sélectionnez un filtre pour inclure les utilisateurs ayant acheté « Proxy War 3 » plus de « 0 » fois.

![Un segment nommé « Purchased Proxy War 3 » qui segmente les utilisateurs ayant acheté le jeu.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3. Mettez à jour les contrôles d'entrée pour ne pas permettre aux utilisateurs de réintégrer le Canvas après la durée maximale du Canvas.

### Étape 5 : Sélectionner vos paramètres d'envoi {#step-5-select-your-send-settings}

Nous conserverons les paramètres d'abonnement par défaut, afin de n'envoyer des messages qu'aux utilisateurs qui se sont abonnés ou ont opté pour la réception de messages ou de notifications.

Parce que nous souhaitons être attentifs à nos envois, nous sélectionnerons **Enable Quiet Hours** pour éviter de demander des retours entre 23 h et 10 h dans le fuseau horaire de nos utilisateurs, et n'envoyer qu'au prochain créneau disponible.

![Étape « Paramètres d'envoi » ciblant les utilisateurs abonnés ou ayant opté pour la réception. Les heures calmes sont activées.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

Pour notre exemple, nous ignorerons les autres paramètres (limite de fréquence et groupes initiateurs).

### Étape 6 : Personnaliser votre Canvas {#step-6-customize-your-canvas}

Ensuite, nous allons construire notre Canvas en personnalisant les canaux de communication et le contenu qui sera envoyé aux utilisateurs. Comme nous ne cherchons à recueillir des retours que par e-mail, message in-app et webhook, nous parcourrons le modèle et supprimerons les variantes SMS des étapes de message.

Nous commencerons notre personnalisation en parcourant chaque composant de message pour mettre à jour le contenu. Notre attribut personnalisé de référence est `Experience Feedback`.

1. Dans le générateur Canvas, sélectionnez la première étape de message dans le parcours utilisateur.
2. Sélectionnez la variante **Email**.
3. Remplissez les **informations d'envoi** avec un objet qui encourage les retours des utilisateurs.
4. Sélectionnez **Edit message** pour remplacer le message e-mail du modèle par notre message d'enquête de satisfaction. Cela inclut le remplacement des liens pour chaque appel à l'action afin de capturer l'option sélectionnée, qui sera référencée dans l'étape de parcours d'action de notre parcours utilisateur.

{% alert tip %}
Vous pouvez utiliser les [propriétés d'entrée Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) pour personnaliser les messages de votre Canvas en fonction du produit auquel vous faites référence.
{% endalert %}

#### Configurer l'enquête de satisfaction {#set-up-feedback-survey}

Ensuite, nous devrons remplir les détails de la variante **In-App Message**. C'est ici que nous devons spécifier notre attribut personnalisé `Experience Feedback` qui indique le sentiment de nos retours utilisateur. (Nous le référencerons également dans l'étape de parcours d'action suivante.)

1. Dans la même première étape de message, sélectionnez la variante **In-App Messages**. Nous conserverons les contrôles de message tels quels.
2. Pour l'en-tête et le corps, nous utiliserons un langage encourageant les utilisateurs à être honnêtes sur leur expérience avec Proxy War 3.
3. Comme nous souhaitons que leurs réponses à l'enquête soient enregistrées dans leurs profils, nous conserverons l'enquête en **Single-choice selection** et **Log attributes upon submission**.
4. Pour chacun des trois choix de l'enquête, sélectionnez **Experience Feedback** comme attribut personnalisé.
5. Nous conserverons les valeurs d'attribut sur le profil utilisateur telles quelles, car ces valeurs correspondent à notre attribut personnalisé.

![Une enquête demandant à l'utilisateur s'il a apprécié son récent achat de Proxy War 3 avec trois options : « Loved it », « It was OK » et « Not for me ».]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### Construire le parcours d'action {#build-out-the-action-path}

En utilisant notre attribut personnalisé `Experience Feedback` et les valeurs d'attribut de la section précédente, nous mettrons à jour le parcours d'action du modèle pour correspondre à notre attribut et nos valeurs.

![Le groupe « Good feedback » pour l'étape de parcours d'action qui inclut les utilisateurs ayant répondu « Loved it » à notre enquête.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### Configurer le reciblage publicitaire {#set-up-ad-retargeting}

Nous nous assurerons que notre synchronisation Google Audience est configurée dans notre étape **Ad Retargeting**. Cela inclura la sélection de notre compte publicitaire, d'une audience existante et de l'option d'ajouter des utilisateurs à l'audience.

### Configurer les cas de support par webhook {#set-up-webhook-support-cases}

Ensuite, configurons le webhook pour déclencher des cas de support potentiels. Cela peut être particulièrement instructif en combinaison avec l'analyse de nos retours utilisateur.

Pour l'étape de message nommée **Support Case Creation**, nous mettrons à jour le modèle pour composer un webhook destiné aux utilisateurs insatisfaits de leur achat et souhaitant un remboursement.

![Un webhook qui crée des cas de support pour les clients ayant un sentiment négatif et souhaitant un remboursement pour leur achat de Proxy War 3.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### Étape 6 : Tester et lancer le Canvas {#step-6-test-and-launch-the-canvas}

Après avoir testé et vérifié que notre Canvas fonctionne comme prévu, sélectionnez **Launch Canvas** pour lancer le Canvas. Nous pouvons désormais cibler les utilisateurs de manière réfléchie avec un parcours utilisateur personnalisé pour les encourager à répondre à notre enquête de satisfaction en fonction de leur récent achat de Proxy War 3 !

{% alert tip %}
Consultez notre [liste de vérification pré et post-lancement]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) pour les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}