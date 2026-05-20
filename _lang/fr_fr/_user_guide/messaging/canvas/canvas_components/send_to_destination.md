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

> L'étape Envoyer vers une destination vous permet de diriger des utilisateurs d'un Canvas vers un autre. Par exemple, si vous avez deux Canvas qui partagent des messages pour des offres promotionnelles, vous pouvez utiliser Envoyer vers une destination pour connecter ces Canvas.

## Fonctionnement {#how-it-works}

![Une étape Envoyer vers une destination pour diriger les utilisateurs vers un nouveau Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Votre Canvas actuel contenant l'étape Envoyer vers une destination est la source. Au sein de l'étape, vous pouvez choisir le Canvas de destination. Les utilisateurs entrants provenant du Canvas source doivent respecter les règles d'entrée du Canvas de destination. Imaginons que vous ayez deux Canvas :

- **Source :** Canvas 1, qui inclut une étape Envoyer vers une destination dirigeant les utilisateurs vers Canvas 2
- **Destination :** Canvas 2, dont les critères d'entrée acceptent les utilisateurs ayant commandé un article

Cette étape permet aux utilisateurs de Canvas 1 d'être envoyés vers Canvas 2. Lorsque les utilisateurs de Canvas 1 atteignent l'étape Envoyer vers une destination, ils sont évalués selon les règles d'entrée de Canvas 2 afin de déterminer s'ils sont éligibles pour y entrer. Dans ce cas, les utilisateurs ayant commandé un article peuvent entrer dans Canvas 2 tout en poursuivant leur parcours dans Canvas 1. Les utilisateurs n'ayant pas commandé d'article continuent uniquement leur parcours dans Canvas 1.

## Créer une étape Envoyer vers une destination {#create-a-send-to-destination-step}

### Étape 1 : Ajouter une étape {#step-1-add-a-step}

Glissez-déposez le composant **Send to Destination** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Send to Destination**.

### Étape 2 : Choisir votre destination {#step-2-choose-your-destination}

Sélectionnez le menu déroulant ou saisissez le nom du Canvas dans le champ **Destination**. Puis, sélectionnez **Done**.

![Une étape Envoyer vers une destination configurée pour diriger les utilisateurs d'un Canvas nommé « Feature Adoption » vers « New Canvas ».]({% image_buster /assets/img/send_to_destination2.png %})

### Étape 3 : Prévisualiser votre destination {#step-3-preview-your-destination}

Vous pouvez sélectionner **Preview destination** pour voir le parcours des utilisateurs qui remplissent les critères d'entrée du Canvas de destination.

Après avoir configuré cette étape du Canvas, vous pouvez [prévisualiser le parcours utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths/) pour vérifier si un utilisateur passe à l'étape suivante dans le Canvas actuel et s'il progresse également dans le Canvas de destination.

## Questions fréquentes {#frequently-asked-questions}

### Puis-je définir un Canvas en brouillon comme destination ? {#can-i-set-the-destination-to-a-draft-canvas}

Oui. Le Canvas de destination peut avoir un statut de brouillon ou inactif.

### Les variables de contexte sont-elles conservées ? {#are-context-variables-preserved}

Oui. Le [contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables/) du Canvas source est toujours transmis au Canvas de destination.

### Les utilisateurs entrent-ils au début du Canvas de destination ? {#do-users-enter-at-the-start-of-the-destination-canvas}

Les utilisateurs entrent au début du Canvas de destination. Pour le moment, il n'est pas possible de créer un lien vers une étape spécifique à l'intérieur du Canvas de destination.

### Comment fonctionne le comportement d'avancement pour les étapes Envoyer vers une destination ? {#how-does-advancement-behavior-work-for-send-to-destination-steps}

Les utilisateurs qui atteignent l'étape Envoyer vers une destination poursuivent leur parcours s'il existe des étapes supplémentaires dans le Canvas source. Si les utilisateurs remplissent également les règles d'entrée du Canvas de destination, ils peuvent y entrer et commencer ce parcours.