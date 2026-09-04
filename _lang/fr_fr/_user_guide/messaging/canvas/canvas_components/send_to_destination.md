---
nav_title: Envoyer vers une destination
article_title: Envoyer vers une destination
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "Cet article de référence présente le composant Envoyer vers une destination et explique comment l'utiliser dans vos Canvas."
tool: Canvas
---

# Étape Envoyer vers une destination {#send-to-destination-step}

> L'étape Envoyer vers une destination vous permet de diriger des utilisateurs d'un Canvas vers un autre. Par exemple, vous pouvez connecter des Canvas qui partagent des messages pour des offres promotionnelles.

## Comment ça fonctionne {#how-it-works}

![Une étape Envoyer vers la destination pour envoyer les utilisateurs vers un nouveau Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Votre Canvas actuel contenant l'étape Envoyer vers la destination est la source. Au sein de cette étape, vous pouvez choisir le Canvas de destination. Les utilisateurs du Canvas source doivent remplir les critères d'audience du Canvas de destination. Imaginons que vous ayez deux Canvas :

- **Source :** Canvas 1, qui comprend une étape Envoyer vers la destination envoyant les utilisateurs vers Canvas 2
- **Destination :** Canvas 2, dont les critères d'audience ciblent les utilisateurs ayant commandé un article

Cette étape permet aux utilisateurs de Canvas 1 d'être envoyés vers Canvas 2. Lorsque les utilisateurs de Canvas 1 atteignent l'étape Envoyer vers la destination, ils sont évalués par rapport aux critères d'audience de Canvas 2 pour déterminer s'ils sont éligibles pour y entrer. Dans ce cas, les utilisateurs ayant commandé un article peuvent entrer dans Canvas 2 tout en poursuivant leur parcours dans Canvas 1. Pour les utilisateurs n'ayant pas commandé d'article, ils poursuivent leur parcours uniquement dans Canvas 1.

### Comportement d'entrée {#entry-behavior}

L'étape Envoyer vers la destination fait entrer les utilisateurs dans le Canvas de destination dès qu'ils atteignent cette étape. Cette étape agit comme un point d'entrée unique dans le Canvas de destination. Les utilisateurs qui remplissent les critères d'audience du Canvas de destination commencent ce parcours Canvas. Ceux qui ne remplissent pas ces critères à ce moment-là n'entrent pas dans le Canvas de destination et poursuivent leur parcours dans le Canvas source.

L'étape Envoyer vers la destination respecte également les [paramètres de réentrée]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) du Canvas de destination sous **Entry Controls**. Si un utilisateur n'est pas éligible pour réentrer dans le Canvas de destination, il n'y est pas envoyé et poursuit son parcours dans le Canvas source.

Si le Canvas de destination utilise une planification d'entrée programmée, l'étape Envoyer vers la destination contourne cette planification d'entrée. Elle contourne également la [**Limit entrance volume**]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) sous **Entry Controls** dans le Canvas de destination lorsqu'elle est définie sur **Every time Canvas is schedule**. Les utilisateurs envoyés depuis cette étape n'attendent pas la prochaine fenêtre d'évaluation programmée : ils sont évalués par rapport aux critères d'audience du Canvas de destination et y entrent immédiatement lorsqu'ils atteignent l'étape Envoyer vers la destination.

Si le Canvas de destination utilise une entrée basée sur une action, l'étape Envoyer vers la destination contourne l'obligation pour les utilisateurs d'effectuer l'action d'entrée configurée pour accéder à ce Canvas.

## Créer une étape Envoyer vers une destination {#create-a-send-to-destination-step}

### Étape 1 : Ajouter une étape {#step-1-add-a-step}

Glissez-déposez le composant **Envoyer vers une destination** depuis la barre latérale, ou sélectionnez le bouton plus <i class="fas fa-plus-circle"></i> en bas d'une étape et sélectionnez **Envoyer vers une destination**.

### Étape 2 : Choisir votre destination {#step-2-choose-your-destination}

Sélectionnez le menu déroulant ou saisissez le nom du Canvas dans le champ **Destination**. Puis, sélectionnez **Terminé**.

![Une étape Envoyer vers une destination configurée pour envoyer les utilisateurs d'un Canvas nommé « Feature Adoption » vers « New Canvas ».]({% image_buster /assets/img/send_to_destination2.png %})

### Étape 3 : Prévisualiser votre destination {#step-3-preview-your-destination}

Vous pouvez sélectionner **Prévisualiser la destination** pour afficher le Canvas vers lequel vous envoyez les utilisateurs.

Après avoir configuré cette étape du Canvas, vous pouvez [prévisualiser le parcours utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) pour vérifier si un utilisateur passe à l'étape suivante dans le Canvas actuel et s'il passe également au Canvas de destination.

## Questions fréquemment posées {#frequently-asked-questions}

### Puis-je définir la destination comme un Canvas en brouillon ? {#can-i-set-the-destination-to-a-draft-canvas}

Oui. Le Canvas de destination peut avoir un statut de brouillon ou inactif.

### Les variables de contexte sont-elles préservées ? {#are-context-variables-preserved}

Oui. Le [contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) du Canvas source est transmis au Canvas de destination. Cependant, les variables de contexte doivent être invoquées dans le Canvas source pour être transmises au Canvas de destination.

### Puis-je utiliser l'étape Envoyer vers la destination pour connecter des Canvas au lieu d'utiliser des solutions de contournement via l'API ou la mise à jour utilisateur ? {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

Oui. Vous pouvez connecter des Canvas avec l'étape Envoyer vers la destination lorsque les utilisateurs doivent passer directement à un autre parcours Canvas.

Vous n'avez pas besoin d'étapes distinctes de mise à jour utilisateur, de déclencheurs API ou de webhooks uniquement pour déplacer les utilisateurs entre des Canvas, tant qu'ils répondent aux critères d'audience du Canvas de destination au moment de l'envoi.

### Les utilisateurs entrent-ils au début du Canvas de destination ? {#do-users-enter-at-the-start-of-the-destination-canvas}

Les utilisateurs éligibles entrent immédiatement à la première étape du Canvas de destination. Ils n'attendent pas un horaire d'entrée planifié ultérieur dans le Canvas de destination. Vous ne pouvez pas rediriger vers une étape spécifique à l'intérieur du Canvas de destination.

### L'étape Envoyer vers la destination respecte-t-elle la planification d'entrée d'un Canvas de destination planifié ? {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

Non. Si le Canvas de destination utilise un type d'entrée planifiée, les utilisateurs envoyés depuis l'étape Envoyer vers la destination n'attendent pas la prochaine fenêtre d'évaluation planifiée. Ils sont évalués par rapport aux critères d'audience et entrent immédiatement lorsqu'ils atteignent l'étape Envoyer vers la destination.

### Comment fonctionne le comportement d'avancement pour les étapes Envoyer vers la destination ? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Les utilisateurs qui entrent dans l'étape Envoyer vers la destination poursuivent leur parcours utilisateur s'il y a des étapes supplémentaires dans le Canvas source. Si les utilisateurs répondent également aux critères d'audience du Canvas de destination, ils peuvent entrer dans ce Canvas et commencer ce parcours.

### L'étape Envoyer vers la destination est-elle soumise aux limites de débit de l'API ? {#is-the-send-to-destination-step-subject-to-api-rate-limits}

Non. Les utilisateurs sont envoyés entre les Canvas au sein de Braze sans effectuer d'appels API externes.