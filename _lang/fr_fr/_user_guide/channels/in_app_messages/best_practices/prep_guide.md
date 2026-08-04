---
nav_title: Guide de préparation
article_title: Guide de préparation des messages in-app
page_order: 0.5

page_type: reference
description: "Cet article couvre les questions et les bonnes pratiques à prendre en compte avant de créer des messages in-app, notamment le ciblage, la planification, le contenu et les conversions."
channel: in-app messages
toc_headers: h2
---

# Guide de préparation des messages in-app {#in-app-message-prep-guide}

> Avant de créer vos messages in-app, prenez en compte les sujets suivants afin que la création de votre message soit rapide et facile.

## Considérations générales {#general-considerations}

- Si vous créez une Campaign, combien de variantes de ce message souhaitez-vous afficher ? Pour des idées de tests de variantes, consultez [Conseils pour différents canaux]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels).
- Si vous créez un Canvas, ce message sera-t-il associé à d'autres canaux de communication dans cette étape ?
- Quand souhaitez-vous que [votre message expire]({{site.baseurl}}/canvas_in-app_messages) ?

## Considérations relatives au ciblage {#targeting-considerations}

- Les messages in-app sont idéaux pour les utilisateurs qui visitent régulièrement votre application. Incluez-vous cette audience ?
- Où souhaitez-vous que vos utilisateurs voient votre message ? Dans votre application Web ? Dans votre application mobile ?
- Quel événement doit déclencher ce message ?
- Certains de vos utilisateurs utilisent-ils des versions plus anciennes de votre application ? Si c'est le cas, ils pourraient ne pas être en mesure de voir certains éléments de votre message.
- Pour quel type d'appareil ou d'appareils créez-vous ce message ? N'oubliez pas que vous pouvez prévisualiser votre message à l'aide de la boîte **Aperçu** ou de l'onglet **Test**. Consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) pour plus d'informations.

## Planification, délais et démarrages de session {#scheduling-delays-and-session-starts}

Lorsqu'une campagne de messages in-app est configurée avec un **Schedule Delay** déclenché au démarrage de session, un utilisateur qui démarre une session puis ferme l'application avant que le message in-app ne s'affiche peut tout de même recevoir ce message au prochain démarrage de session, une fois le délai écoulé.

Ce comportement peut produire un affichage inattendu, en particulier si l'option **Re-evaluate campaign eligibility before displaying** n'est pas sélectionnée dans la campagne.

Par exemple, un utilisateur pourrait recevoir un message in-app avec un délai de huit secondes un mois après le lancement de la campagne. Cela peut se produire s'il a démarré une session, l'a immédiatement terminée, puis a démarré une nouvelle session un mois plus tard et a reçu le message in-app huit secondes après. S'il quitte l'application sans la fermer, le message in-app s'affiche lorsqu'il y revient.

## Considérations relatives au contenu {#content-considerations}

- Quelles langues utiliserez-vous dans ce message ?
- Quels sont votre en-tête et votre texte principal ? Sont-ils accrocheurs et pertinents pour votre utilisateur ?
- Les messages in-app ne s'affichent que pendant une durée limitée. Votre texte est-il concis et mémorable ?
- Utiliserez-vous [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) pour ajouter du texte personnalisé ?
- Les utilisateurs ont-ils besoin de copier le texte du message (comme un code de réduction ou un bon d'achat) ? Sur iOS et Android, les utilisateurs peuvent appuyer longuement sur du texte ou des champs de saisie pour copier le contenu. L'appui long ne fonctionne pas sur les images, utilisez donc du texte ou des champs de saisie au lieu d'images contenant des codes ou d'autres éléments que les utilisateurs pourraient avoir besoin de copier.
- Pour les messages in-app en plein écran, votre image ou autre média se trouve-t-elle dans la [zone de sécurité]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone) ?
- Pour les messages in-app de type sondage, souhaitez-vous enregistrer des attributs ou des soumissions ? Avez-vous configuré votre page de confirmation ?
- Pour les messages in-app HTML personnalisés, votre HTML inclut-il l'encodage UTF-8 pour afficher correctement les caractères spéciaux ? Consultez [Messages in-app HTML personnalisés]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding) pour plus de détails.
- Si vous incluez une vidéo dans votre message in-app : bien que Braze n'impose pas de limite technique sur la taille des fichiers vidéo pour la lecture locale sur l'appareil, gardez à l'esprit que les utilisateurs peuvent avoir des connexions lentes, des forfaits de données coûteux ou un espace de stockage limité. Optimisez les fichiers vidéo pour trouver un équilibre entre qualité et taille de fichier.

## Considérations relatives à la conversion {#conversion-considerations}

- Quel est votre objectif pour ce message ? Comment pouvez-vous le représenter dans votre message ?
- Vos boutons proposent-ils des options pertinentes pour votre utilisateur ? Quel est votre [appel à l'action principal]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons) ?
- Créez-vous des [deep links vers d'autres contenus in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) ? Utilisez-vous ce message in-app pour envoyer et accepter une [demande d'autorisation ou d'amorce de notification push]({{site.baseurl}}/user_guide/channels/push/best_practices) ?
- Avez-vous une option de sortie du message ? Si ce n'est pas le cas, vous pouvez toujours copier et coller cet extrait de code pour créer un bouton rapide :
    ```html
    <a href="appboy://close">X</a>
    ```

## Considérations relatives à l'éditeur par glisser-déposer {#drag-and-drop-editor-considerations}

### Ajout de deep links pour différents appareils {#adding-deep-links-for-different-devices}

L'éditeur par glisser-déposer ne prend pas en charge l'ajout de deep links différents pour différents appareils (contrairement à l'éditeur traditionnel).

### Ajustement de l'opacité de l'image d'arrière-plan {#adjusting-background-image-opacity}

Le paramètre d'opacité ne permet pas une transparence complète des images d'arrière-plan (contrairement à l'éditeur traditionnel de messages in-app). Vous pouvez utiliser les paramètres d'opacité pour rendre la couleur d'arrière-plan du message complètement transparente.

### Définition de la largeur maximale {#setting-the-maximum-width}

La largeur maximale dans l'éditeur par glisser-déposer est limitée à 325 px ; cela est principalement destiné à s'adapter à l'aperçu du tableau de bord. Les messages peuvent s'afficher correctement sur les appareils à écran plus petit.

### Sélection d'arrière-plans différents pour différentes plateformes {#selecting-different-backgrounds-for-different-platforms}

Il n'est pas possible d'afficher deux arrière-plans différents pour le même message sur différentes plateformes (comme le web et le mobile).

### Application des styles de message {#applying-message-styles}

Les images d'arrière-plan s'appliquent à l'ensemble du message et ne peuvent pas être personnalisées par page. Les styles de message s'appliquent à l'ensemble du message, pas aux pages individuelles.

### Mesure de la hauteur des blocs d'espacement {#measuring-spacer-blocks-height}

L'unité de mesure des blocs d'espacement est le pixel (px) et ne peut pas être modifiée.

### Formats pris en charge {#supported-formats}

Actuellement, seuls les messages in-app modaux et plein écran sont pris en charge dans l'éditeur par glisser-déposer.

### Ajustement à la taille et au rapport hauteur/largeur {#adjusting-to-size-and-aspect-ratio}

L'image d'arrière-plan étirera le message in-app, car la fenêtre modale s'ajuste pour s'adapter à la taille et au rapport hauteur/largeur de l'image d'arrière-plan ; vous pouvez ajuster le rapport selon vos besoins.

### Images d'arrière-plan et comportement au clic {#background-images-and-on-click-behavior}

Ceux-ci persistent d'une page à l'autre. Pour les messages in-app multi-pages avec des images plein format différentes sur chaque page, ajoutez un bouton pour permettre aux utilisateurs de cliquer pour accéder à la page suivante.