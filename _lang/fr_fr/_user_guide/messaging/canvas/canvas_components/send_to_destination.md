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

## Fonctionnement {#how-it-works}

![Une étape Envoyer vers une destination pour diriger les utilisateurs vers un nouveau Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Votre Canvas actuel contenant l'étape Envoyer vers une destination est la source. Au sein de l'étape, vous pouvez choisir le Canvas de destination. Les utilisateurs provenant du Canvas source doivent respecter les critères d'entrée et d'audience du Canvas de destination. Imaginons que vous ayez deux Canvas :

- **Source :** Canvas 1, qui inclut une étape Envoyer vers une destination dirigeant les utilisateurs vers Canvas 2
- **Destination :** Canvas 2, dont les critères d'entrée acceptent les utilisateurs ayant commandé un article

Cette étape permet aux utilisateurs de Canvas 1 d'être envoyés vers Canvas 2. Lorsque les utilisateurs de Canvas 1 atteignent l'étape Envoyer vers une destination, ils sont évalués selon les critères d'entrée et d'audience de Canvas 2 afin de déterminer s'ils sont éligibles pour y entrer. Dans ce cas, les utilisateurs ayant commandé un article peuvent entrer dans Canvas 2 tout en poursuivant leur parcours dans Canvas 1. Les utilisateurs n'ayant pas commandé d'article continuent uniquement leur parcours dans Canvas 1.

### Comportement d'entrée {#entry-behavior}

L'étape Envoyer vers une destination fait entrer les utilisateurs dans le Canvas de destination dès qu'ils atteignent cette étape. Elle agit comme un point d'entrée unique dans le Canvas de destination. Les utilisateurs qui remplissent les critères d'entrée et d'audience du Canvas de destination commencent ce parcours Canvas. Les utilisateurs qui ne remplissent pas ces critères à ce moment-là n'entrent pas dans le Canvas de destination et poursuivent leur parcours dans le Canvas source.

Si le Canvas de destination utilise une planification d'entrée planifiée, l'étape Envoyer vers une destination contourne cette planification d'entrée. Elle contourne également l'option [**Limiter le volume d'entrée**]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#selecting-entry-controls) sous **Contrôles d'entrée** du Canvas de destination lorsqu'elle est définie sur **À chaque planification du Canvas**. Les utilisateurs envoyés depuis cette étape n'attendent pas la prochaine fenêtre d'évaluation planifiée : ils sont évalués et entrent dans le Canvas lorsqu'ils atteignent l'étape Envoyer vers une destination, à condition de remplir les critères d'entrée et d'audience du Canvas de destination.

Si le Canvas de destination utilise une entrée basée sur une action, l'étape Envoyer vers une destination contourne l'obligation pour les utilisateurs d'effectuer l'action d'entrée configurée pour accéder à ce Canvas.

## Créer une étape Envoyer vers une destination {#create-a-send-to-destination-step}

### Étape 1 : Ajouter une étape {#step-1-add-a-step}

Glissez-déposez le composant **Send to Destination** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Send to Destination**.

### Étape 2 : Choisir votre destination {#step-2-choose-your-destination}

Sélectionnez le menu déroulant ou saisissez le nom du Canvas dans le champ **Destination**. Puis, sélectionnez **Done**.

![Une étape Envoyer vers une destination configurée pour diriger les utilisateurs d'un Canvas nommé « Feature Adoption » vers « New Canvas ».]({% image_buster /assets/img/send_to_destination2.png %})

### Étape 3 : Prévisualiser votre destination {#step-3-preview-your-destination}

Vous pouvez sélectionner **Preview destination** pour visualiser le Canvas vers lequel vous dirigez les utilisateurs.

Après avoir configuré cette étape du Canvas, vous pouvez [prévisualiser le parcours utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/) pour vérifier si un utilisateur passe à l'étape suivante dans le Canvas actuel et s'il progresse également dans le Canvas de destination.

## Questions fréquentes {#frequently-asked-questions}

### Puis-je définir un Canvas en brouillon comme destination ? {#can-i-set-the-destination-to-a-draft-canvas}

Oui. Le Canvas de destination peut avoir un statut de brouillon ou inactif.

### Les variables de contexte sont-elles conservées ? {#are-context-variables-preserved}

Oui. Le [contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) du Canvas source est toujours transmis au Canvas de destination.

### Puis-je utiliser l'étape Envoyer vers une destination pour connecter des Canvas au lieu d'utiliser des solutions de contournement via l'API ou la mise à jour utilisateur ? {#can-i-use-the-send-to-destination-step-to-connect-canvases-instead-of-using-api-or-user-update-workarounds}

Oui. Vous pouvez connecter des Canvas avec l'étape Envoyer vers une destination lorsque les utilisateurs doivent passer directement à un autre parcours Canvas.

Vous n'avez pas besoin d'étapes de mise à jour utilisateur séparées, de déclencheurs API ou de webhooks uniquement pour déplacer des utilisateurs entre des Canvas, tant qu'ils remplissent les critères du Canvas de destination au moment de l'envoi.

### Les utilisateurs entrent-ils au début du Canvas de destination ? {#do-users-enter-at-the-start-of-the-destination-canvas}

Les utilisateurs éligibles entrent immédiatement à la première étape du Canvas de destination. Ils n'attendent pas un horaire d'entrée planifié ultérieur sur le Canvas de destination. Il n'est pas possible de créer un lien vers une étape spécifique à l'intérieur du Canvas de destination.

### L'étape Envoyer vers une destination respecte-t-elle la planification d'entrée d'un Canvas de destination planifié ? {#does-the-send-to-destination-step-respect-a-scheduled-destination-canvas-entry-schedule}

Non. Si le Canvas de destination utilise un type d'entrée planifié, les utilisateurs envoyés depuis l'étape Envoyer vers une destination n'attendent pas la prochaine fenêtre d'évaluation planifiée. Ils sont évalués et entrent dans le Canvas lorsqu'ils atteignent l'étape Envoyer vers une destination, à condition de remplir les critères d'entrée et d'audience du Canvas de destination.

### Comment fonctionne le comportement d'avancement pour les étapes Envoyer vers une destination ? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Les utilisateurs qui atteignent l'étape Envoyer vers une destination poursuivent leur parcours s'il existe des étapes supplémentaires dans le Canvas source. Si les utilisateurs remplissent également les règles d'entrée du Canvas de destination, ils peuvent y entrer et commencer ce parcours.