---
nav_title: Lancer avec Canvas Flow
article_title: Lancer avec Canvas Flow
page_order: 3
description: "Cet article de référence explique comment préparer et tester un Canvas créé avec Canvas Flow avant son lancement."
page_type: reference
tool: Canvas
---

# Lancer avec Canvas Flow

> Cet article de référence explique comment préparer et tester un Canvas créé avec Canvas Flow avant son lancement. Il couvre notamment les points de contrôle importants tels que les conditions d'entrée du Canvas, les résumés d'audience et les segments d'utilisateurs.

Lorsque vous préparez le lancement de votre Canvas, Braze vous recommande de vérifier votre Canvas à chaque étape du générateur, en prêtant attention aux paramètres susceptibles d'affecter l'envoi de vos messages, notamment :
* [Les conditions de concurrence](#race-conditions)
* [Les horaires de distribution](#delivery-times)
* [Les segments d'utilisateurs](#segment-users)

## Conditions de concurrence

Prenez en compte les [conditions de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/) qui peuvent survenir avant de lancer votre Canvas.

Pour entrer dans un Canvas, les utilisateurs doivent faire partie de l'audience d'entrée avant que la planification d'entrée ne se déclenche, que le Canvas soit planifié, basé sur une action ou déclenché par API.

![Un Canvas basé sur une action qui fait entrer les utilisateurs lorsqu'ils effectuent un achat pendant l'heure locale de l'utilisateur, du 30 avril 2025 à 12 h au 7 mai 2025 à 12 h.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Notez que les utilisateurs qui remplissent les critères de votre audience d'entrée après le lancement du Canvas n'entreront pas dans le Canvas.

{% alert tip %}
Consultez les [types de planification d'entrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-12-determine-your-canvas-entry-schedule) pour obtenir des conseils et des détails sur le choix entre une distribution planifiée, basée sur une action ou déclenchée par API pour votre Canvas !
{% endalert %}

### Vérifier les filtres de l'audience d'entrée

De manière générale, évitez de configurer un Canvas basé sur une action ou déclenché par API avec le même déclencheur que le filtre d'audience. Par exemple, une fois le Canvas lancé, les utilisateurs qui effectuent une action spécifique seront inclus dans l'audience d'entrée, il n'est donc pas nécessaire d'ajouter l'événement en tant que filtre d'audience.

Pour plus de détails sur les filtres de segmentation disponibles pour cibler votre audience, consultez [Filtres de segmentation]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

### Regrouper plusieurs requêtes API

Effectuez vos requêtes dans un même appel API, plutôt que dans plusieurs appels, pour vous assurer que le profil utilisateur est créé ou mis à jour en premier. Consultez [Utiliser plusieurs endpoints]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions#using-multiple-api-endpoints) pour plus d'exemples.

### Ajouter un délai

Une autre option pour éviter les conditions de concurrence consiste à utiliser l'étape Délai (idéalement réglée sur 5 minutes) comme première étape de votre Canvas.

Cela laisse le temps aux attributs, adresses e-mail et jetons de notification push d'être traités pour les nouveaux profils utilisateurs avant qu'ils ne soient ciblés par les étapes suivantes du Canvas. Sans cette étape de délai, il est possible qu'un e-mail soit envoyé à un utilisateur dont l'adresse e-mail n'a pas encore été mise à jour.

## Horaires de distribution

Configurer un horaire de distribution en temps réel pour un Canvas peut contribuer à augmenter les taux d'engagement et de conversion. Prenez note de l'horaire de distribution que vous avez défini pour votre Canvas. Pour améliorer l'engagement et les taux de conversion, il est préférable de déclencher les Canvas en temps réel plutôt que de manière planifiée et récurrente.

Si vous avez sélectionné une distribution planifiée pour votre Canvas, Braze recommande de planifier votre Canvas au moins 24 heures avant la date de lancement souhaitée afin de permettre d'éventuels ajustements.

## Segments d'utilisateurs

Avant de surcharger le parcours utilisateur de votre Canvas Flow avec des composants, réfléchissez à la manière de simplifier ce parcours. Utilisez la vue simplifiée dans l'éditeur de Canvas pour mieux visualiser les ramifications de votre parcours utilisateur.

Quatre composants principaux vous permettent de segmenter vos utilisateurs de manière simple et efficace :

* [Parcours d'audience](#audience-paths)
* [Arbre décisionnel](#decision-split)
* [Parcours d'actions](#action-paths)
* [Chemins d'expérience](#experiment-paths)

### Parcours d'audience

Utilisez les étapes [Parcours d'audience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/) pour segmenter les utilisateurs au sein du Canvas en fonction d'attributs personnalisés, d'événements personnalisés et de données d'engagement avec les messages précédents issues des profils utilisateurs.

### Arbre décisionnel

L'étape [Arbre décisionnel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/) vous permet d'orienter vos utilisateurs vers différents parcours en fonction de leurs réponses à une question binaire.

### Parcours d'actions

Les [Parcours d'actions]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/) se concentrent sur la segmentation des utilisateurs en fonction de comportements en temps réel, tels que les événements personnalisés, les événements d'achat et les modifications d'attributs personnalisés.

### Chemins d'expérience

De manière similaire aux Parcours d'actions, vous pouvez utiliser les étapes [Chemins d'expérience]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/) dans votre Canvas pour tester plusieurs parcours les uns par rapport aux autres, ainsi qu'un groupe de contrôle. Cela permet de suivre les performances de chaque parcours et de prendre des décisions éclairées lors de la construction de votre Canvas.

## Tester avant le lancement

Après avoir vérifié les détails de votre Canvas, consultez [Envoyer des Canvas de test]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases/) pour découvrir les différentes méthodes que vous pouvez utiliser pour tester votre Canvas avec des utilisateurs test.

## Liste de vérification avant le lancement

### Vérifier la disponibilité des utilisateurs

- Assurez-vous que vos utilisateurs remplissent vos critères de segmentation.
- Confirmez que leur état d'abonnement est « abonné » ou « inscrit » et que leur jeton de notification push existe. Si vous avez ajouté ces critères comme règles d'entrée du Canvas, il est possible que les utilisateurs se soient désabonnés entre leur entrée dans le Canvas et la réception de l'étape Message.
- Confirmez qu'ils correspondent à vos paramètres d'envoi du Canvas. (Si les utilisateurs sont « abonnés » mais que les paramètres sont définis sur « Inscrit », les utilisateurs ne seront pas activés pour le canal.)
- Si la limite de fréquence globale est activée pour votre Canvas, vérifiez si vos règles limitent le nombre de fois que chaque utilisateur peut recevoir un message d'un canal spécifique.
- Si les heures calmes sont activées, l'heure d'envoi de votre message pourrait être affectée, ce qui signifie que votre message pourrait être envoyé au prochain créneau disponible (à la fin des heures calmes) ou annulé entièrement.
- Vérifiez la disponibilité des utilisateurs pour les filtres supplémentaires dans votre étape du canvas.

### Confirmer que les utilisateurs ont effectué l'événement personnalisé ou l'achat prérequis

- Vérifiez s'il existe une condition de concurrence, qui affecte les messages reçus par les utilisateurs lorsqu'ils déclenchent plusieurs actions en même temps.
- Assurez-vous qu'il n'y a pas de filtres spécifiques dans l'étape qui auraient pu empêcher les utilisateurs de recevoir le message.
- Recherchez les conflits entre différentes étapes au sein du même Canvas. Par exemple, les utilisateurs qui n'ont pas reçu le message pourraient être bloqués par un filtre exigeant l'achèvement d'une autre étape sur une branche différente.
- Confirmez que les utilisateurs remplissent les règles de validation supplémentaires.
- Confirmez que l'étape du canvas était connectée à l'étape précédente au moment de l'envoi.

### Confirmer que votre Canvas s'enregistre correctement et que toutes les étapes sont valides

Si votre Canvas ne se charge pas et ne progresse pas, cela peut être dû au fait qu'une version précédente du Canvas n'a pas été enregistrée correctement et contient des étapes invalides. Vous pouvez dupliquer le Canvas depuis le tableau de bord. Si le problème persiste, ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).

## Résolution des problèmes

{% details Pourquoi mes utilisateurs ne reçoivent-ils pas les messages de mon Canvas ? %}
**Vérifier la disponibilité des utilisateurs**
- Assurez-vous qu'ils remplissent vos critères de segmentation.
- Confirmez que leur état d'abonnement push est « abonné » ou « inscrit » **et** que leur statut **Push activé** est défini sur « true ». Si vous avez ajouté ces critères comme règles d'entrée du Canvas, il est possible que les utilisateurs se soient désabonnés entre leur entrée dans le Canvas et la réception de l'étape Message.
- Confirmez qu'ils correspondent à vos paramètres d'envoi du Canvas. (Si les utilisateurs sont « abonnés » mais que les paramètres sont définis sur « Inscrit », les utilisateurs ne seront pas activés pour le canal.)
- Si la limite de fréquence globale est activée pour votre Canvas, vérifiez si vos règles limitent le nombre de fois que chaque utilisateur peut recevoir un message d'un canal spécifique.
- Si les heures calmes sont activées, l'heure d'envoi de votre message pourrait être affectée, ce qui signifie que votre message pourrait être envoyé au prochain créneau disponible (à la fin des heures calmes) ou annulé entièrement.

**Vérifier la disponibilité des utilisateurs pour les filtres supplémentaires dans votre étape du canvas**
- Confirmez qu'ils ont effectué l'événement personnalisé ou l'achat prérequis.
- Vérifiez s'il existe une [condition de concurrence]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/race_conditions/), qui affecte les messages reçus par les utilisateurs lorsqu'ils déclenchent plusieurs actions en même temps.
- Assurez-vous qu'il n'y a pas de filtres spécifiques dans l'étape qui auraient pu empêcher les utilisateurs de recevoir le message.
- Recherchez les conflits entre différentes étapes au sein du même Canvas. Par exemple, les utilisateurs qui n'ont pas reçu le message pourraient être bloqués par un filtre exigeant l'achèvement d'une autre étape sur une branche différente.
- Confirmez que les utilisateurs remplissent les règles de validation supplémentaires.
- Confirmez que l'étape du canvas était connectée à l'étape précédente au moment de l'envoi.
{% enddetails %}