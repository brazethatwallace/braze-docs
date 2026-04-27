---
nav_title: Envoyer vers une destination
article_title: Envoyer vers une destination
alias: "/send_to_destination/"
page_order: 11.5
page_type: reference
description: "Cet article de référence présente le composant Envoyer vers une destination et explique comment l'utiliser dans vos Canvas."
tool: Canvas
---

# Étape Envoyer vers une destination

> L'étape Envoyer vers une destination vous permet de diriger des utilisateurs d'un Canvas vers un autre. Par exemple, si vous avez deux Canvas qui partagent des messages pour des offres promotionnelles, vous pouvez utiliser Envoyer vers une destination pour connecter ces Canvas.

## Fonctionnement

![Une étape Envoyer vers une destination pour diriger les utilisateurs vers un nouveau Canvas.]({% image_buster /assets/img/send_to_destination1.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Votre Canvas actuel contenant l'étape Envoyer vers une destination est la source. Au sein de l'étape, vous pouvez choisir le Canvas de destination. À partir de là, les utilisateurs sont envoyés vers le Canvas de destination. Ils progresseront dans ce Canvas s'ils remplissent les critères d'entrée correspondants, tout en continuant à avancer dans le Canvas source.

## Créer une étape Envoyer vers une destination

### Étape 1 : Ajouter une étape

Glissez-déposez le composant **Envoyer vers une destination** depuis la barre latérale, ou sélectionnez le bouton <i class="fas fa-plus-circle"></i> plus en bas d'une étape et sélectionnez **Envoyer vers une destination**.

### Étape 2 : Choisir votre destination

Sélectionnez le menu déroulant ou saisissez le nom du Canvas dans le champ **Destination**. Puis, sélectionnez **Terminé**.

![Une étape Envoyer vers une destination configurée pour diriger les utilisateurs d'un Canvas nommé « Feature Adoption » vers « New Canvas ».]({% image_buster /assets/img/send_to_destination2.png %})

### Étape 3 : Prévisualiser votre destination

Vous pouvez sélectionner **Prévisualiser la destination** pour voir le parcours des utilisateurs qui remplissent les critères d'entrée du Canvas de destination.

Après avoir configuré cette étape du canvas, vous pouvez [prévisualiser le parcours utilisateur]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) pour vérifier si un utilisateur passe à l'étape suivante dans le Canvas actuel et s'il progresse également dans le Canvas de destination.

## Questions fréquentes

### Puis-je définir un Canvas en brouillon comme destination ?

Oui. Le Canvas de destination peut avoir un statut de brouillon ou inactif.

### Les variables de contexte sont-elles conservées ?

Oui. Le [contexte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) du Canvas source est toujours transmis au Canvas de destination.