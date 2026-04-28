---
nav_title: Adoption de fonctionnalité
article_title: Adoption de fonctionnalité
page_order: 3
page_type: reference
description: "Cet article décrit comment utiliser un modèle Canvas de Braze pour envoyer des messages personnalisés et opportuns mettant en avant les avantages et les conseils d'utilisation."
tool: Canvas
---

# Adoption de fonctionnalité {#feature-adoption}

> Ce modèle est conçu pour stimuler l'utilisation de vos nouvelles fonctionnalités, produits existants, offres supplémentaires ou tout autre domaine que vous souhaitez faire découvrir à vos clients. En tirant parti d'une communication personnalisée et d'un ensemble structuré de messages, vous pouvez présenter de façon fluide de nouvelles fonctionnalités aux utilisateurs et recueillir des retours précieux de leur part.

Dans cet article, nous allons parcourir un cas d'utilisation du modèle **Adoption de fonctionnalité**, qui est destiné aux étapes de rétention et de fidélisation du cycle de vie utilisateur. À la fin de cet article, vous aurez personnalisé un parcours utilisateur qui encourage les utilisateurs à utiliser de nouvelles fonctionnalités et recueille leur sentiment.

## Conditions préalables {#prerequisites}

Pour utiliser ce modèle avec succès, vous aurez besoin d'un [événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) qui référence le moment où les utilisateurs ont utilisé la fonctionnalité.

## Adapter le modèle à vos besoins {#tailoring-the-template-to-your-needs}

Imaginons que vous travaillez chez Calorie Rocket, une application de livraison de repas, qui a récemment lancé Cruise Control, une fonctionnalité permettant de planifier des livraisons de repas récurrentes, et que vous souhaitez encourager davantage d'utilisateurs à adopter cette nouvelle fonctionnalité. Dans notre exemple, nous utiliserons l'événement personnalisé `scheduled_delivery` pour suivre quand les utilisateurs ont essayé la fonctionnalité Cruise Control.

Pour accéder au modèle de retour en stock, lors de la création d'un nouveau Canvas, sélectionnez **Use a Canvas template** > **Braze templates**. Ensuite, à côté de **Feature Adoption**, sélectionnez **Apply Template**. Nous pouvons maintenant parcourir le modèle pour l'adapter à nos besoins.

### Étape 1 : Configurer les détails {#step-1-set-up-the-details}

Ajustons les détails du Canvas pour refléter notre objectif.

1. Sélectionnez **Edit** à côté du nom du modèle.

![Le titre et la description actuels du Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2. Mettez à jour le nom du Canvas pour préciser qu'il est destiné au ciblage des utilisateurs afin de recueillir leurs retours.
3. Mettez à jour la description pour préciser que le Canvas vise à encourager les utilisateurs à soumettre des retours et à suivre le sentiment utilisateur pour la nouvelle fonctionnalité Cruise Control.
4. Ajoutez l'étiquette **Feature adoption** afin de pouvoir filtrer le Canvas sur la page d'accueil Canvas.

![Le nouveau nom et la nouvelle description du Canvas. La nouvelle description indique : « Un Canvas d'adoption de fonctionnalité pour suivre l'adoption et le sentiment utilisateur pour Cruise Control, une fonctionnalité de planification de livraisons de repas récurrentes. »]({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Étape 2 : Affecter un événement de conversion {#step-2-assign-a-conversion-event}

Ensuite, ajoutons un événement de conversion à notre Canvas pour signaler l'adoption de la fonctionnalité. Cela nous permettra d'adapter le chemin d'expérience dans notre parcours utilisateur par la suite.

1. Sous **Assign Conversion Events**, sélectionnez **Add Conversion Event**.
2. Sous **Primary Conversion Event - A**, sélectionnez **Performs Custom Event** comme **Conversion event type**.
3. Sélectionnez notre événement personnalisé `scheduled_delivery`.
4. Nous conserverons la date limite de conversion à trois jours.

![La fenêtre d'événement de conversion dans le Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### Étape 3 : Adapter la planification d'entrée {#step-3-tailor-the-entry-schedule}

Notre objectif est d'encourager nos utilisateurs à adopter Cruise Control, mais nous ne voulons pas que nos messages soient trop fréquents. Nous conserverons donc ce Canvas en livraison planifiée et apporterons les ajustements suivants à la section **Time-Based Options**.

1. Mettez à jour la **fréquence d'entrée** sur **Weekly**.
2. Conservez la récurrence telle quelle.
3. Sélectionnez **Mon** pour cibler les utilisateurs en début de semaine.
4. Sélectionnez l'heure de début de notre Canvas.
5. Mettez à jour les **paramètres de fin** pour terminer le Canvas le dernier jour de l'année.

Nous conserverons l'option permettant aux utilisateurs d'entrer dans le Canvas selon leur fuseau horaire local.

### Étape 4 : Sélectionner l'audience cible {#step-4-select-the-target-audience}

Maintenant, configurons notre audience cible en mettant à jour les détails suivants dans le modèle :

1. Sélectionnez le segment **All Users**.
2. Supprimez les filtres supplémentaires du modèle.
3. Créez ce filtre en utilisant notre événement personnalisé : `Has scheduled_delivery for exactly 0 times`. Cela nous permet d'exclure les utilisateurs qui ont déjà utilisé la fonctionnalité de l'entrée dans notre Canvas.

![Le segment pour tous les utilisateurs qui n'ont pas utilisé Cruise Control.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4. En gardant à l'esprit que Calorie Rocket a précédemment permis à quelques utilisateurs de tester en bêta la nouvelle fonctionnalité Cruise Control, nous mettrons à jour les critères de sortie pour exclure ces utilisateurs de l'entrée dans le Canvas.

### Étape 5 : Sélectionner vos paramètres d'envoi {#step-5-select-your-send-settings}

Nous conserverons les paramètres d'abonnement par défaut, de sorte que nous n'envoyons des messages qu'aux utilisateurs qui se sont abonnés ou ont opté pour la réception de messages ou de notifications, et nous ignorerons les autres paramètres (limite de fréquence, heures calmes et groupes initiateurs).

### Étape 6 : Personnaliser votre Canvas {#step-6-customize-your-canvas}

#### Construire le parcours d'action {#build-out-the-action-path}

Ensuite, construisons la première étape de parcours d'action, qui est destinée à indiquer si nos utilisateurs ont un intérêt pour la nouvelle fonctionnalité. Nous apporterons les ajustements suivants au modèle :

1. Puisque la fonctionnalité Cruise Control n'est disponible qu'après l'ajout d'une commande au panier, nous nommerons le premier groupe d'actions **Added to cart** et sélectionnerons `added_to_cart` pour l'événement personnalisé.

![Le nom du groupe d'actions défini sur « Added to cart » et « Perform Custom Event » défini sur « added_to_cart ».]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2. Conservez le deuxième groupe d'actions **Taken Tour** tel quel, car nous voulons évaluer si les utilisateurs ont fait une visite guidée de l'application, et si c'est le cas, ils avanceront vers le deuxième chemin.
3. Pour le parcours d'action suivant nommé **Assess Usage**, remplacez **Used Feature >3x** par **Viewed Cruise Control settings**.
4. Sélectionnez le menu déroulant **Perform Custom Event**, puis sélectionnez `scheduled_delivery` pour l'événement personnalisé.

![Le nom du groupe d'actions défini sur « Used Feature >3x » et « Perform Custom Event » défini sur « scheduled_delivery ».]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Configurer l'enquête de satisfaction {#set-up-feedback-survey}

Ensuite, nous irons à l'étape de message nommée **Feedback Survey** pour inclure notre enquête de satisfaction que nos utilisateurs rempliront après avoir utilisé Cruise Control pour la première fois. Les options de réponse de notre enquête pour nos utilisateurs sont :

- **Loved it!**
- **Not for me.**

1. Pour les deux choix de l'enquête, sélectionnez **Experience Feedback** comme attribut personnalisé pour capturer et suivre les retours sur Cruise Control. Cet attribut personnalisé aura deux valeurs pour représenter les réponses à l'enquête (`good` et `bad`).
2. Mettez à jour les valeurs d'attribut pour correspondre aux options de l'enquête. Cela nous permettra de suivre la réponse d'un utilisateur.

### Étape 7 : Tester et lancer votre Canvas {#step-7-test-and-launch-your-canvas}

Après avoir testé et vérifié que notre Canvas fonctionne comme prévu, sélectionnez **Launch Canvas** pour lancer le Canvas. Nous pouvons maintenant cibler les utilisateurs avec un parcours utilisateur personnalisé pour les encourager à adopter notre nouvelle fonctionnalité Cruise Control.

{% alert tip %}
Consultez notre [liste de vérification pré et post-lancement]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) pour les éléments à prendre en compte avant et après le lancement d'un Canvas.
{% endalert %}