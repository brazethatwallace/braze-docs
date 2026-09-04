---
nav_title: Style des e-mails
article_title: Style des e-mails
page_order: 2
page_type: reference
description: "Cet article présente les bonnes pratiques de style des e-mails à consulter lors de la création de vos campagnes par e-mail."
channel: email

---

# Style des e-mails {#email-styling}

> Cet article présente les bonnes pratiques de style des e-mails, notamment les lignes d'objet, le texte d'accroche, la taille des e-mails et les recommandations relatives aux images.

## Style de l'adresse {#address-styling}

La ligne d'objet est l'une des premières choses que les destinataires voient lorsqu'ils reçoivent votre message. La limiter à 6 à 10 mots permet d'obtenir les meilleurs taux d'ouverture.

Il existe également différentes approches pour créer une bonne ligne d'objet : poser une question pour piquer la curiosité du lecteur, adopter un ton plus direct, ou encore la personnaliser pour engager votre clientèle. Ne vous limitez pas à une seule ligne d'objet, tirez parti des [tests A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/faq#what-is-the-difference-between-ab-testing-and-multivariate-testing) pour en essayer de nouvelles et évaluer leur efficacité. Les lignes d'objet ne doivent pas dépasser 35 caractères pour s'afficher correctement sur mobile.

Le champ « De » doit clairement indiquer qui est l'expéditeur. Évitez d'utiliser le nom d'une personne ou une abréviation peu courante. Utilisez plutôt un nom reconnaissable, comme le nom de votre marque. Si l'utilisation du nom d'une personne correspond aux méthodes de personnalisation des e-mails de votre marque, restez cohérent afin de développer une relation avec le destinataire. Le nom dans le champ « De » ne doit pas dépasser 25 caractères pour s'afficher correctement sur mobile.

### Adresses sans réponse {#no-reply-addresses}

Les adresses e-mail sans réponse (no-reply) sont généralement déconseillées pour plusieurs raisons, car elles désengagent vos lecteurs. De nombreux destinataires répondent à l'e-mail pour se désabonner. S'ils ne peuvent pas le faire, la réaction suivante consiste le plus souvent à signaler l'e-mail comme courrier indésirable.

Recevoir des réponses d'absence du bureau peut en réalité fournir des informations précieuses, en augmentant les taux d'ouverture et en réduisant les signalements de courrier indésirable (en retirant ceux qui ne souhaitent pas recevoir d'e-mails). Sur un plan personnel, une adresse sans réponse peut paraître impersonnelle aux yeux des destinataires et les dissuader de recevoir d'autres e-mails de votre entreprise.

## Accroche {#preheader-text}

L'accroche d'un e-mail communique efficacement le point principal du message pour capter l'intérêt du lecteur et encourager les ouvertures. L'accroche est aussi souvent utilisée par les marketeurs pour fournir des informations supplémentaires sur le contenu d'un e-mail. Une accroche est le texte d'aperçu affiché immédiatement après l'objet d'un e-mail. Dans l'exemple suivant, l'accroche est `- Brand. New. Lounge Shorts`.

![Accroche dans une boîte de réception Gmail avec le texte « Brand. New. Lounge Shorts ».]({% image_buster /assets/img_archive/preheader_example.png %})

La quantité de texte d'accroche visible dépend du client de messagerie de l'utilisateur et de la longueur de la ligne d'objet de l'e-mail. En général, nous recommandons que les accroches contiennent entre 50 et 100 caractères.

{% alert note %}
L'accroche peut faire référence à du Liquid dans le corps de l'e-mail, et le corps de l'e-mail peut faire référence à du Liquid dans l'accroche. Cela s'explique par le fait que le texte de l'accroche fait partie du corps de l'e-mail lorsque vous envoyez des messages aux destinataires.
{% endalert %}

Voici quelques bonnes pratiques à garder à l'esprit lors de la rédaction de vos accroches :

1. Les appels à l'action entrent en jeu après que les lecteurs ont ouvert votre e-mail.
  - Orientez vos lecteurs dans la bonne direction, que vous souhaitiez qu'ils s'abonnent, achètent un produit ou visitent votre site web.
  - Utilisez des mots percutants pour que le lecteur sache exactement ce que vous lui demandez, mais assurez-vous que cela reflète la voix de marque de votre entreprise et que chaque appel à l'action apporte une certaine valeur au consommateur.
  - L'accroche ne doit pas dépasser 85 caractères et doit contenir un appel à l'action descriptif qui soutient la ligne d'objet.

2. Les e-mails et les pages de destination vers lesquels vous dirigez vos utilisateurs doivent être optimisés pour le mobile :
  - Pas de fenêtres interstitielles
  - Grands champs de formulaire
  - Navigation facile
  - Texte de grande taille
  - Espaces blancs généreux
  - Corps de texte court et concis
  - Appels à l'action clairs

### Limites de caractères pour l'accroche {#preheader-character-limits}

  |   Client de messagerie mobile  |  Limite  |
  |:------------------------------:|:--------:|
  | iOS Outlook            | 74      |
  | Android Native         | 43      |
  | Android Gmail          | 24      |
  | iOS Native             | 82      |
  | iOS Gmail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de caractères pour l'accroche" }

  |  Client de messagerie de bureau  |  Limite  |
  |:--------------------------------:|:--------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook for Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de caractères pour l'accroche" }


  |  Client de messagerie web  |  Limite  |
  |:--------------------------:|:--------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Limites de caractères pour l'accroche" }

## Taille de l'e-mail {#email-size}

La taille de l'e-mail fait référence à la taille du HTML de votre message dans Braze (le corps que vous créez et ce que Braze ajoute lors de l'envoi du message).

- Veillez à limiter la taille de votre e-mail. Les corps d'e-mails supérieurs à 102&nbsp;Ko sont non seulement extrêmement gourmands en ressources pour les serveurs Braze, mais ils sont également tronqués par Gmail et d'autres clients de messagerie.
- Les images hébergées que vous référencez par URL ne sont pas intégrées dans le HTML de la même manière que le collage de ressources volumineuses en ligne. Nous recommandons d'utiliser la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) et de créer des liens via `href`, ce qui permet de réduire la taille du message.

|   Texte uniquement   | Texte avec images |     Largeur de l'e-mail    |
|:-------------:|:----------------:|:------------------:|
| 25&nbsp;Ko maximum |   60&nbsp;Ko maximum   | 600 pixels maximum |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Taille de l'e-mail" }

Pour réduire le risque de troncature :

- Raccourcissez le texte et les liens.
- Intégrez le CSS critique en ligne si nécessaire. Supprimez les espaces superflus dans le HTML.
- Compressez les images et les ressources HTML.

{% alert note %}
Pour enregistrer votre Campaign ou votre modèle d'e-mail, assurez-vous que le corps de votre e-mail ne dépasse pas 400&nbsp;Ko.
{% endalert %}

### Qu'est-ce qui peut augmenter la taille finale de l'e-mail ? {#what-can-add-to-the-final-email-size}

Ces fonctionnalités augmentent légèrement la taille du message rendu :

- Pixel de suivi d'ouverture : ajoute une balise image de 1 x 1&nbsp;px au corps du message
- Accroche : ajoute un `<div>` masqué en haut du corps du message
- aliasage de lien : ajoute un paramètre de requête de 16 caractères (`lid=`) à chaque URL suivie
- Modèles de liens : ajoute les paramètres de requête configurés dans le tableau de bord aux URL correspondantes
- Insertion CSS (optionnelle) : applique les règles de feuille de style intégrées en ligne aux éléments HTML, ce qui peut ajouter du CSS redondant selon la complexité de la feuille de style

L'accroche et le pixel de suivi ajoutent environ 600 caractères (moins de 1&nbsp;Ko). Braze ajoute généralement entre 0&nbsp;Ko et 5&nbsp;Ko selon le nombre de liens, la complexité des modèles de liens et l'activation ou non de l'insertion CSS. Si la taille de votre e-mail est proche de la limite, nous vous recommandons de tester vos e-mails avant l'envoi, car la taille finale rendue dépend de ces paramètres.

## Longueur du texte {#text-length}

Consultez le tableau suivant pour connaître les longueurs de texte recommandées.

| Spécifications du texte | Propriétés recommandées |
| --- | --- |
| Longueur de la ligne d'objet | 35 caractères maximum (pour un affichage mobile optimal) (6 à 10 mots) |
| Longueur du nom de l'expéditeur | 25 caractères maximum (pour un affichage mobile optimal) |
| Longueur de l'accroche | 85 caractères maximum |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Longueur du texte" }

## Taille des images {#image-size}

Consultez le tableau suivant pour connaître les tailles d'images recommandées. Les images plus petites et de haute qualité se chargent plus rapidement, utilisez donc la ressource la plus légère possible pour obtenir le résultat souhaité.

|     Taille    | Largeur de l'image d'en-tête |  Largeur de l'image du corps  |   Types de fichiers  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5&nbsp;Mo maximum | 600 pixels maximum | 480 pixels maximum | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Taille des images" }

{% alert note %}
Les applications web et mobile de Gmail ne prennent généralement pas en charge le rendu des SVG (et la prise en charge du WEBP est incohérente). Utilisez le format PNG ou JPEG pour les images qui doivent s'afficher de manière fiable dans Gmail.
{% endalert %}

## Deep links {#deep-linking}

Avec les notifications push et les messages in-app, un [deep link]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) dirige les utilisateurs directement vers une destination spécifique au sein d'une application. Cependant, les deep links nécessitent que l'application soit installée, et les e-mails ne permettent pas de savoir si les destinataires disposent de l'application. Cela signifie que les deep links dans les e-mails peuvent entraîner des erreurs pour les destinataires qui n'ont pas l'application installée.

Utilisez plutôt les [liens universels et App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links), qui fonctionnent comme des URL standard. Vous pouvez les configurer pour ouvrir l'application ou diriger les utilisateurs vers une page spécifique. Ils peuvent également rediriger vers la boutique d'applications ou basculer vers une page web lorsque l'application n'est pas installée.

## Content Blocks avec images transparentes {#content-blocks-with-transparent-images}

Lorsqu'un Content Block contient une image avec un arrière-plan transparent (par exemple, un logo) et est inséré par une étiquette Liquid, vous pouvez voir une couleur d'arrière-plan apparaître derrière l'image. Cette couleur provient des [paramètres de style global de l'e-mail]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) de l'éditeur par glisser-déposer, plus précisément de la **couleur d'arrière-plan de l'e-mail**. Si vos paramètres de style global utilisent une couleur autre que le blanc, cette couleur apparaît à la place.

Pour afficher le Content Block comme prévu :

- Définissez la couleur d'arrière-plan de la colonne du Content Block pour qu'elle corresponde à l'arrière-plan de l'e-mail ou du modèle.
- Vous pouvez également convertir le Content Block par glisser-déposer en un Content Block HTML et définir son arrière-plan comme transparent.

Si vous devez utiliser le même Content Block dans des zones avec des arrière-plans différents (par exemple, le corps et le pied de page), créez deux versions du bloc, chacune avec la couleur d'arrière-plan de colonne appropriée.

Si vous préférez glisser le Content Block dans l'e-mail en tant que ligne, vous pouvez définir l'arrière-plan de la colonne de la ligne comme transparent pour remplacer l'arrière-plan global.

{% alert note %}
Glisser un Content Block en tant que ligne insère un aperçu pré-rendu, qui ne se met pas automatiquement à jour si le Content Block source est modifié.
{% endalert %}

## Mode sombre {#dark-mode}

Le mode sombre est une préférence côté destinataire. Les fournisseurs de boîte de réception et les applications (comme Gmail et Outlook) peuvent inverser ou recolorer votre HTML, vous devez donc vous attendre à un rendu différent selon les clients plutôt qu'à une apparence fixe unique depuis Braze.

### Éditeur HTML {#html-editor}

Si vous utilisez l'**éditeur HTML**, vous pouvez réduire les inversions d'arrière-plan indésirables dans les applications mobiles Gmail en appliquant un `linear-gradient` CSS monochrome sur les cellules de tableau au lieu d'un simple `background-color`. Pour des exemples, les limitations (notamment l'utilisation de `<td>` ou `<th>` plutôt que `<table>` seul) et la syntaxe, consultez [Application mobile Gmail et mode sombre]({{site.baseurl}}/user_guide/channels/email/html_editor#gmail-dark-mode).

Pour créer des styles distincts pour les modes clair et sombre lorsque les clients les prennent en charge, utilisez la requête média [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme). La prise en charge varie selon la boîte de réception — prévisualisez et testez toujours dans les clients vers lesquels vous envoyez.

### Éditeur par glisser-déposer {#drag-and-drop-editor}

Dans l'éditeur par glisser-déposer, le mode sombre reste contrôlé par chaque fournisseur de boîte de réception. Activez l'**aperçu du mode sombre** dans **Aperçu et test** pour vérifier votre mise en page. Pour savoir où trouver le bouton et comment tester, consultez [Puis-je prévisualiser l'apparence de mon e-mail en mode sombre ?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#can-i-preview-how-my-email-appears-in-dark-mode). Pour les couleurs d'arrière-plan et la lisibilité selon les thèmes, consultez [Comment concevoir des e-mails pour le mode sombre et le mode clair ?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#how-should-i-design-emails-for-dark-mode-and-light-mode).

### Bonnes pratiques générales {#general-best-practices}

- Évitez le blanc pur (`#FFFFFF`) et le noir pur (`#000000`) ; utilisez des blancs cassés et des noirs adoucis pour que les inversions complètes paraissent moins agressives.
- Atténuez les couleurs d'accentuation très vives (par exemple, les boutons aux couleurs éclatantes) afin qu'elles restent lisibles si un client inverse les couleurs.
- Utilisez des PNG transparents lorsqu'ils conviennent à votre mise en page.
- Sur les images contenant du texte, ajoutez un contour clair autour du texte sombre, et un contour sombre autour du texte clair sur les visuels foncés, afin que le texte reste lisible si les couleurs changent.