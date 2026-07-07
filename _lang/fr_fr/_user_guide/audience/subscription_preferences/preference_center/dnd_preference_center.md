---
nav_title: Centre de préférences e-mail par glisser-déposer
article_title: Centre de préférences e-mail par glisser-déposer
alias: "/dnd_preference_center/"
description: "Cette page de référence explique comment créer un centre de préférences e-mail avec l'éditeur par glisser-déposer."
page_order: 2
---

# Créer un centre de préférences e-mail par glisser-déposer {#create-an-email-preference-center-with-drag-and-drop}

> L'éditeur par glisser-déposer vous permet de créer et de personnaliser un centre de préférences pour gérer les types de communication que reçoivent vos utilisateurs. Vous pouvez disposer de 100 centres de préférences par espace de travail.

Vous pouvez gérer les centres de préférences par glisser-déposer existants depuis **Audience** > **Centre de préférence des e-mails** :

- Pour modifier le nom ou le contenu d'un centre de préférences, ouvrez-le depuis le tableau de bord.
- Les centres de préférences par glisser-déposer ne peuvent pas être supprimés depuis le tableau de bord. Pour en supprimer un, retirez d'abord son étiquette Liquid de toutes les Campaigns ou étapes du Canvas concernées, puis contactez l'[assistance Braze]({{site.baseurl}}/support_contact).
- Si un centre de préférences supprimé était utilisé dans des messages précédemment envoyés, il cessera de fonctionner dans ces e-mails déjà délivrés.
{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Étape 1 : Créer un centre de préférences e-mail {#step-1-create-an-email-preference-center}

Créez un centre de préférences en accédant à **Audience** > **Centre de préférence des e-mails**.

Une liste de centres de préférences personnalisés s'affichera. Sélectionnez **Créer** pour créer un nouveau centre de préférences, ou sélectionnez le nom d'un centre existant pour le modifier.


## Étape 2 : Nommer le centre de préférences e-mail {#step-2-name-the-email-preference-center}

Les noms des centres de préférences ne peuvent contenir que des caractères alphanumériques, des tirets ou des underscores. Le nom que vous fournissez déterminera la syntaxe de l'étiquette Liquid générée.

Cette étiquette Liquid peut être incluse dans n'importe quelle Campaign ou étape du Canvas sortante et dirigera les utilisateurs vers le centre de préférences.


## Étape 3 : Ajouter des groupes d'abonnement au centre de préférences {#step-3-add-subscription-groups-to-the-preference-center}

Sélectionnez **Lancer l'éditeur** pour commencer à concevoir votre centre de préférences dans l'éditeur par glisser-déposer.

### Définir les groupes d'abonnement disponibles {#define-available-subscription-groups}

Pour déterminer quels groupes d'abonnement doivent apparaître dans le centre de préférences, sélectionnez le bouton **+ Add subscription groups** pour ouvrir une fenêtre modale dans laquelle vous pouvez sélectionner les groupes d'abonnement souhaités. Après votre sélection, cliquez sur le bouton **Add Subscription Groups** pour les ajouter au centre de préférences.

Vous pouvez configurer davantage les groupes d'abonnement sélectionnés en cliquant sur le bloc intelligent et en ajustant les propriétés du bloc.
- Ajuster l'ordre des groupes d'abonnement
- Ajouter ou supprimer des groupes d'abonnement supplémentaires
- Inclure des descriptions
- Ajouter ou supprimer une case à cocher **Subscribe to all** qui abonnera l'utilisateur à tous les groupes d'abonnement affichés dans ce bloc
- Ajouter ou supprimer une case à cocher **Unsubscribe from all** qui désabonnera l'utilisateur de tous les groupes d'abonnement affichés dans ce bloc


Le bouton **Unsubscribe from all** en bas du modèle ne peut pas être supprimé et [désabonnera globalement]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) l'utilisateur de la réception de tout message e-mail.

## Étape 4 : Personnaliser le centre de préférences avec l'éditeur par glisser-déposer {#step-4-customize-the-preference-center-using-the-drag-and-drop-editor}

### Définir les styles communs {#set-common-styles}

Vous pouvez définir certains styles qui s'appliqueront à tous les blocs pertinents de votre centre de préférences depuis l'onglet **Common Styles**. Les styles définis dans cette section sont utilisés partout dans votre message, sauf lorsque vous les remplacez pour un bloc spécifique. Pour une expérience de conception plus fluide, nous vous recommandons de configurer les styles au niveau de la page avant de personnaliser les styles au niveau des blocs.

![Un exemple de paramètres de styles communs pour le texte, les boutons et les liens.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Pour revenir aux styles communs, sélectionnez le bouton « X » dans les propriétés de chaque bloc. Ensuite, sélectionnez le conteneur du message, le bouton « X » du message ou l'arrière-plan de l'éditeur.
{% endalert %}

## Composants du centre de préférences par glisser-déposer {#drag-and-drop-preference-center-components}

L'éditeur par glisser-déposer utilise deux composants clés pour rendre la composition du centre de préférences rapide et facile : les lignes et les blocs. Tous les blocs doivent être placés dans une ligne.

{% tabs %}
{% tab Lignes %}

Les lignes sont des unités structurelles qui définissent la composition horizontale d'une section du message à l'aide de cellules.

![Option pour sélectionner le type de ligne dans votre message.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Lorsqu'une ligne est sélectionnée, vous pouvez ajouter ou supprimer le nombre de colonnes nécessaires depuis la section de personnalisation des colonnes pour placer différents éléments de contenu côte à côte. Vous pouvez également faire glisser pour ajuster la taille des colonnes existantes.

![Options pour personnaliser les propriétés de vos colonnes, y compris la couleur d'arrière-plan, le style de bordure, le rayon de bordure et le remplissage.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

En tant que bonne pratique, mettez en forme les propriétés de vos lignes et colonnes avant de mettre en forme les blocs à l'intérieur des lignes. Vous pouvez ajuster l'espacement et l'alignement à de nombreux endroits, donc commencer par les fondations facilite les modifications au fur et à mesure.

{% endtab %}
{% tab Blocs %}

Les blocs représentent différents types de contenu que vous pouvez utiliser dans votre message. Faites-en glisser un dans un segment de ligne existant, et il s'ajustera automatiquement à la largeur de la cellule.

![Option pour sélectionner des blocs, y compris titre, paragraphe, bouton, image et espacement.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Chaque bloc possède ses propres paramètres, comme un contrôle granulaire du remplissage. Le panneau de droite bascule automatiquement vers un panneau de style pour l'élément de contenu sélectionné. Pour plus d'informations, consultez [Blocs éditeur (centre de préférences)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=preference%20center).

Si vous utilisez le bloc de code personnalisé dans votre centre de préférences, les cadres intégrés (iframes) peuvent ne pas être générés dans le code personnalisé lors de la livraison à vos utilisateurs.

{% endtab %}
{% endtabs %}

## Étape 5 : Personnaliser votre page de confirmation {#step-5-customize-your-confirmation-page}

N'oubliez pas de personnaliser la page de confirmation ! Vous pouvez modifier cette page en sélectionnant **Confirmation Page** en haut de la fenêtre de l'éditeur par glisser-déposer. Cette page sera affichée aux utilisateurs après la mise à jour de leurs préférences via le centre de préférences. Les mêmes fonctionnalités de style décrites ci-dessus s'appliquent également à cette page.

![Un exemple de page de confirmation indiquant à l'utilisateur que ses préférences ont été mises à jour.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Étape 6 : Prévisualiser et lancer votre centre de préférences {#step-6-preview-and-launch-your-preference-center}

Vous pouvez prévisualiser votre centre de préférences en sélectionnant l'onglet **Preview** dans l'éditeur. Cependant, la fonctionnalité de test est désactivée. Après avoir modifié votre centre de préférences, vous pouvez fermer l'éditeur en sélectionnant le bouton **Done**.

Vous verrez un aperçu du centre de préférences et de la page de confirmation. Sélectionnez **Enregistrer en tant que brouillon** pour revenir à ce centre de préférences ultérieurement, ou si vous êtes satisfait, sélectionnez **Launch Preference Center**.

Lors du lancement du centre de préférences, vous serez invité à confirmer le nom, car il ne pourra plus être modifié après le lancement. Après avoir confirmé le nom, le centre de préférences sera lancé et prêt à être utilisé.

## Utiliser le centre de préférences {#using-the-preference-center}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Pour placer un lien vers le centre de préférences dans vos e-mails, copiez l'étiquette Liquid du centre de préférences souhaité en sélectionnant l'icône **Copier le Liquid**.

![L'option Copier le Liquid dans la ligne d'un centre de préférences.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Ajoutez l'étiquette Liquid à l'emplacement souhaité dans votre e-mail, de la même manière que les [URL de désabonnement]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer#adding-a-custom-unsubscribe-link) sont insérées.

## Gestion des erreurs {#handling-errors}

Si une erreur survient lorsqu'un utilisateur sélectionne **Save** dans un centre de préférences, le message d'erreur par défaut suivant s'affichera. Ce message ne peut être ni personnalisé ni stylisé dans l'éditeur. Cependant, la localisation des messages d'erreur est toujours prise en charge sur ces pages.

![Un message d'erreur indiquant « Un problème est survenu lors de l'enregistrement de vos préférences. Veuillez réessayer. »]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}