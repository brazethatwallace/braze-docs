---
nav_title: Contextuel
article_title: Messages in-app contextuels
page_order: 3
channel:
  - in-app messages
tool:
  - Media
description: "Cet article de référence couvre les exigences en matière de message et de conception des messages in-app contextuels."

---

# Messages in-app contextuels {#slideup-in-app-messages}

> Nos messages contextuels apparaissent généralement en haut ou en bas de l'écran de l'application (vous pouvez définir cela lors de la création de votre message). Ils sont parfaits pour informer vos utilisateurs de nouvelles conditions d'utilisation, de cookies et d'autres informations utiles. Ils ne sont pas intrusifs et permettent à vos utilisateurs de continuer à interagir avec votre application pendant l'affichage du message.

Ce type de message est disponible dans l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional/).

![Deux messages in-app contextuels, l'un apparaissant en haut de l'écran et l'autre en bas, détaillant les recommandations en matière d'image et de texte. Consultez les sections suivantes pour plus de détails.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Comportement de l'image et du texte {#image-and-copy-behavior}

Les messages contextuels peuvent contenir jusqu'à trois lignes de texte avant troncature avec des points de suspension. Les images dans les messages contextuels ne seront jamais recadrées ni rognées — elles seront toujours redimensionnées pour s'adapter au conteneur d'image de 50 x 50 pixels.

- Toutes les images doivent faire moins de 5&nbsp;Mo.
- Nous acceptons uniquement les formats de fichier PNG, JPEG et GIF.
- Nous recommandons que vos images fassent 500&nbsp;Ko.

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d'images de messages in-app et nos superpositions de zones sûres sont conçus pour s'adapter parfaitement aux appareils de toutes tailles. [Télécharger le ZIP des modèles de conception]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Disposition | Taille de la ressource | Notes |
|--- | --- | --- |
| Image + Texte | Rapport hauteur/largeur 1:1<br>Haute résolution 150 x 150&nbsp;px<br> Minimum 50 x 50&nbsp;px | Les images de différents rapports hauteur/largeur s'adapteront à un conteneur d'image carré, sans recadrage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comportement de l'image et du texte" }

Vous devriez toujours [prévisualiser et tester vos messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=in-app%20message) sur une variété d'appareils pour vous assurer que les zones les plus importantes de votre image et de votre message apparaissent comme prévu. Notez que lors de la prévisualisation de votre message dans le composeur, le rendu réel sur les appareils peut différer.

## Liens hypertextes et texte d'ancrage {#hyperlinks-and-anchor-text}

Pour ajouter un lien dans un message contextuel, saisissez le texte du message dans le champ **Corps** et définissez la destination dans **Comportement au clic** (par exemple, **Rediriger vers une URL**). Lorsque le **Comportement au clic** est configuré, un appui n'importe où sur le message, à l'exception du bouton de fermeture, déclenche cette action.

Pour les messages in-app HTML personnalisés, vous pouvez utiliser des liens HTML directement. Consultez [Messages in-app HTML personnalisés]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/).

## Appareils mobiles {#mobile-devices}

Sur les appareils mobiles, les messages contextuels apparaissent en haut ou en bas de l'écran de l'application. Vous pouvez le spécifier lors de la création de votre message. Les utilisateurs peuvent balayer pour fermer le message contextuel, ou appuyer dessus pour l'ouvrir si une action au clic est incluse. Si une action au clic est ajoutée au message contextuel, un chevron « > » est affiché.

## Écrans plus grands {#larger-screens}

{% tabs %}
{% tab Ordinateur de bureau %}

Sur un navigateur de bureau, un message in-app contextuel s'affichera dans le coin de l'écran comme illustré dans la capture d'écran suivante (sauf indication contraire lors de la création du message in-app). Les utilisateurs peuvent cliquer sur le bouton de fermeture « X » pour fermer le message contextuel.

![Message in-app contextuel tel qu'il apparaît sur un navigateur de bureau. Le message apparaît dans le coin inférieur droit de l'écran et n'occupe pas toute la largeur de l'écran.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablette %}

Sur une tablette, un message in-app contextuel apparaît en bas de l'écran. Comme sur les appareils mobiles, les utilisateurs peuvent balayer pour fermer le message contextuel, ou appuyer dessus pour l'ouvrir si une action au clic est incluse. Si une action au clic est ajoutée au message contextuel, un chevron « > » est affiché. Un bouton de fermeture « X » n'est pas affiché par défaut.

![Message in-app contextuel tel qu'il apparaît sur l'écran d'une tablette. Le message apparaît en bas au centre de l'écran et n'occupe pas toute la largeur de l'écran.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}