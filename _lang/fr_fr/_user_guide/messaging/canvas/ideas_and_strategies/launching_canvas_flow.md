---
nav_title: Lancer avec Canvas Flow
article_title: Lancer avec Canvas Flow
page_order: 3
description: "Cet article de référence explique comment préparer et tester un Canvas créé avec Canvas Flow avant son lancement."
page_type: reference
tool: Canvas
---

# Lancer avec Canvas Flow {#launch-with-canvas-flow}

> Cet article de référence explique comment préparer et tester un Canvas créé avec Canvas Flow avant son lancement. Il couvre notamment les points de contrôle importants tels que les conditions d'entrée du Canvas, les résumés d'audience et les segments d'utilisateurs.

Lorsque vous préparez le lancement de votre Canvas, Braze vous recommande de vérifier votre Canvas à chaque étape du générateur, en prêtant attention aux paramètres susceptibles d'affecter l'envoi de vos messages, notamment :
* [Les conditions de concurrence](#race-conditions)
* [Les horaires de distribution](#delivery-times)
* [Les segments d'utilisateurs](#segment-users)

## Conditions de concurrence {#race-conditions}

Considérez les [conditions de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions) qui peuvent survenir avant de lancer votre Canvas.

Pour entrer dans un Canvas, les utilisateurs doivent faire partie de l'audience d'entrée avant que la planification d'entrée ne se déclenche, que le Canvas soit planifié, basé sur une action ou déclenché par API.

![Un Canvas basé sur une action qui fait entrer les utilisateurs lorsqu'ils effectuent un achat pendant l'heure locale de l'utilisateur, du 30 avril 2025 à 12 h au 7 mai 2025 à 12 h.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Notez que les utilisateurs qui deviennent éligibles pour votre audience d'entrée après le lancement du Canvas n'entreront pas dans le Canvas.

{% alert tip %}
Consultez [Types de planification d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) pour obtenir des conseils et des détails sur le moment d'utiliser la distribution planifiée, basée sur une action ou déclenchée par API pour votre Canvas !
{% endalert %}

### Vérifier les filtres d'audience d'entrée {#review-entry-audience-filters}

En général, évitez de configurer un Canvas basé sur une action ou déclenché par API avec le même déclencheur que le filtre d'audience. Par exemple, après le lancement d'un Canvas, les utilisateurs qui effectuent une action spécifique seront inclus dans l'audience d'entrée, il n'est donc pas nécessaire d'ajouter l'événement en tant que filtre d'audience.

Pour plus de détails sur les filtres de segmentation disponibles pour cibler votre audience, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Regrouper plusieurs requêtes API {#batch-multiple-api-requests}

Effectuez vos requêtes dans le même appel API, plutôt que dans plusieurs appels, pour confirmer que le profil utilisateur est créé ou mis à jour en premier. Reportez-vous à [Utiliser plusieurs endpoints]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#scenario-2-using-multiple-api-endpoints) pour plus d'exemples.

### Ajouter un délai {#add-a-delay}

Une autre option pour éviter les conditions de concurrence consiste à utiliser l'étape de délai (idéalement réglée sur 5 minutes) comme première étape de votre Canvas.

Cela laisse le temps aux attributs, adresses e-mail et jetons de notification push d'être traités sur les nouveaux profils utilisateurs avant qu'ils ne soient ciblés pour les étapes Canvas suivantes. Sans cette étape de délai, il est possible qu'un e-mail soit envoyé à un utilisateur dont l'adresse e-mail n'a pas encore été mise à jour.

## Horaires de réception {#delivery-times}

Définir un horaire de réception du Canvas en temps réel peut contribuer à augmenter les taux d'engagement et de conversion. Prenez note de l'horaire de réception que vous avez défini pour votre Canvas. Pour améliorer les taux d'engagement et de conversion, il est préférable de déclencher les Canvas en temps réel plutôt que de manière planifiée et récurrente.

Si vous avez sélectionné une réception planifiée pour votre Canvas, Braze recommande de planifier votre Canvas au moins 24 heures avant le lancement souhaité afin de permettre d'éventuels ajustements.

## Segments d'utilisateurs {#user-segments}

Avant de surcharger votre parcours utilisateur Canvas Flow avec des composants, réfléchissez à la manière de garder un parcours utilisateur simple. Utilisez la vue simplifiée dans l'éditeur de Canvas pour mieux visualiser les ramifications de votre parcours utilisateur.

Il existe quatre composants principaux que vous pouvez utiliser pour segmenter vos utilisateurs de manière simple et efficace :

* [Parcours d'audience](#audience-paths)
* [Arbre décisionnel](#decision-split)
* [Parcours d'action](#action-paths)
* [Chemins d'expérience](#experiment-paths)

### Parcours d'audience {#audience-paths}

Utilisez les étapes [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) pour segmenter les utilisateurs au sein du Canvas en fonction d'attributs personnalisés, d'événements personnalisés et de données d'engagement aux messages précédents issues des profils utilisateur.

### Arbre décisionnel {#decision-split}

L'étape [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) vous permet d'orienter vos utilisateurs vers différents parcours en fonction de leurs réponses à une question binaire.

### Parcours d'action {#action-paths}

Les [Parcours d'action]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) se concentrent sur la segmentation des utilisateurs en fonction de comportements en temps réel, tels que les événements personnalisés, les événements d'achat et les modifications d'attributs personnalisés.

### Chemins d'expérience {#experiment-paths}

Similaires aux parcours d'action, les étapes [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) vous permettent de tester plusieurs parcours Canvas les uns par rapport aux autres, ainsi qu'un groupe de contrôle. Cela permet de suivre les performances de chaque parcours afin de prendre des décisions éclairées lors de la construction de votre parcours Canvas.

## Test avant le lancement {#testing-before-launch}

Après avoir passé en revue les détails de votre Canvas, consultez [Envoyer des Canvas de test]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) pour découvrir les différentes méthodes que vous pouvez exploiter pour tester votre Canvas avec des utilisateurs test.

## Liste de vérification avant le lancement {#launch-checklist}

### Vérifier la disponibilité des utilisateurs {#check-user-availability}

- Assurez-vous que vos utilisateurs remplissent vos critères de segmentation.
- Confirmez que leur état d'abonnement est « subscribed » ou « opted-in » et que leur jeton push existe. Si vous avez ajouté ces conditions comme règles d'entrée du Canvas, il est possible que les utilisateurs se soient désabonnés entre leur entrée dans le Canvas et la réception de l'étape Message.
- Confirmez qu'ils correspondent aux paramètres d'envoi de votre Canvas. (Si les utilisateurs sont « subscribed » mais que les paramètres sont définis sur « Opted-in », les utilisateurs ne seront pas activés pour le canal.)
- Si la limite de fréquence globale est activée pour votre Canvas, vérifiez si vos règles limitent le nombre de fois que chaque utilisateur peut recevoir un message d'un canal spécifique.
- Si les heures calmes sont activées, l'heure d'envoi de votre message pourrait être affectée, ce qui signifie que votre message pourrait être envoyé au prochain créneau disponible (à la fin des heures calmes) ou annulé entièrement.
- Vérifiez la disponibilité des utilisateurs pour les filtres supplémentaires dans votre étape du Canvas.

### Confirmer qu'ils ont effectué l'événement personnalisé ou l'achat prérequis {#confirm-that-they-performed-the-prerequisite-custom-event-or-purchase}

- Vérifiez s'il existe une condition de concurrence, qui affecte les messages que les utilisateurs reçoivent lorsqu'ils déclenchent plusieurs actions en même temps.
- Assurez-vous qu'il n'y a pas de filtres spécifiques dans l'étape qui auraient pu empêcher les utilisateurs de recevoir le message.
- Recherchez les conflits entre différentes étapes au sein du même Canvas. Par exemple, les utilisateurs qui n'ont pas reçu le message pourraient être bloqués par un filtre exigeant l'achèvement d'une autre étape sur une branche différente.
- Confirmez que les utilisateurs remplissent les règles de validation supplémentaires.
- Confirmez que l'étape du Canvas était connectée à l'étape précédente au moment de l'envoi.

### Confirmer que votre Canvas s'enregistre correctement et que toutes les étapes sont valides {#confirm-your-canvas-saves-correctly-and-all-steps-are-valid}

Si votre Canvas ne se charge pas et ne progresse pas, cela peut être dû au fait qu'une version précédente du Canvas n'a pas été enregistrée correctement et contient des étapes invalides. Vous pouvez dupliquer le Canvas depuis le tableau de bord. Si le problème persiste, ouvrez un [ticket d'assistance]({{site.baseurl}}/user_guide/administer/personal/braze_support).

## Résolution des problèmes {#troubleshooting}

{% details Pourquoi mes utilisateurs ne reçoivent-ils pas mes messages Canvas ? %}
**Vérifier la disponibilité des utilisateurs**
- Assurez-vous qu'ils répondent à vos critères de segmentation.
- Confirmez que leur état d'abonnement aux notifications push est « subscribed » ou « opted-in » **et** que leur statut **Push Enabled** est défini sur « true ». Si vous avez ajouté ces règles comme conditions d'entrée dans le Canvas, il est possible que les utilisateurs se soient désabonnés entre le moment où ils sont entrés dans votre Canvas et celui où ils ont reçu l'étape de message.
- Confirmez qu'ils correspondent aux paramètres d'envoi de votre Canvas. (Si les utilisateurs sont « subscribed » mais que les paramètres sont définis sur « Opted-in », les utilisateurs ne seront pas activés pour le canal.)
- Si la limite de fréquence globale est activée pour votre Canvas, vérifiez si vos règles limitent le nombre de fois que chaque utilisateur peut recevoir un message d'un canal spécifique.
- Si les heures calmes sont activées, l'heure d'envoi de votre message pourrait être affectée, ce qui signifie que votre message pourrait être envoyé au prochain créneau disponible (lorsque les heures calmes prennent fin) ou annulé entièrement.

**Vérifier la disponibilité des utilisateurs pour les filtres supplémentaires dans votre étape Canvas**
- Confirmez qu'ils ont effectué l'événement personnalisé ou l'achat requis.
- Vérifiez s'il existe une [condition de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions), qui impacte les messages que les utilisateurs reçoivent s'ils déclenchent plusieurs actions en même temps.
- Assurez-vous qu'il n'y a pas de filtres spécifiques dans l'étape qui auraient pu empêcher les utilisateurs de recevoir le message.
- Recherchez les conflits entre les différentes étapes au sein du même Canvas. Par exemple, les utilisateurs qui n'ont pas reçu le message pourraient être arrêtés par un filtre qui exige l'achèvement d'une autre étape sur une branche différente.
- Confirmez que les utilisateurs répondent aux règles de validation supplémentaires.
- Confirmez que l'étape Canvas était connectée à l'étape précédente au moment de l'envoi.
{% enddetails %}