---
nav_title: Guide de préparation
article_title: Guide de préparation des messages in-app
page_order: 0.5

page_type: reference
description: "Cet article couvre les questions et les bonnes pratiques à prendre en compte avant de créer des messages in-app, notamment le ciblage, la planification, le contenu, les performances et les conversions."
channel: in-app messages
toc_headers: h2
---

# Guide de préparation des messages in-app {#in-app-message-prep-guide}

> Avant de créer vos messages in-app, prenez en compte les sujets suivants pour rendre le processus plus efficace.

## Considérations générales {#general-considerations}

- Si vous créez une campagne, combien de variantes de ce message souhaitez-vous afficher ? Pour des idées de tests de variantes, consultez [Conseils pour différents canaux]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels).
- Si vous créez un Canvas, ce message sera-t-il associé à d'autres canaux de communication dans cette étape ?
- Quand souhaitez-vous que [votre message expire]({{site.baseurl}}/canvas_in-app_messages) ?

## Considérations de ciblage {#targeting-considerations}

- Les messages in-app sont idéaux pour les utilisateurs qui visitent régulièrement votre application. Incluez-vous cette audience ?
- Où souhaitez-vous que vos utilisateurs voient votre message ? Dans votre application Web ? Dans votre application mobile ?
- Quel événement doit déclencher ce message ?
- Certains de vos utilisateurs utilisent-ils des versions plus anciennes de votre application ? Si c'est le cas, ils pourraient ne pas être en mesure de voir certains éléments de votre message.
- Pour quel type d'appareil ou quels appareils créez-vous ce message ? N'oubliez pas que vous pouvez prévisualiser votre message à l'aide de la boîte **Preview** ou de l'onglet **Test**. Consultez [Envoyer des messages de test]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) pour plus d'informations.

## Planification, délais et démarrages de session {#scheduling-delays-and-session-starts}

Lorsqu'une campagne de messages in-app comporte un **Schedule Delay** avec un déclencheur au démarrage de session, un utilisateur qui démarre une session puis ferme l'application avant que le message in-app ne s'affiche peut tout de même recevoir ce message au prochain démarrage de session, une fois le délai expiré.

Les campagnes de messages in-app peuvent retarder la distribution jusqu'à deux heures après le déclenchement. Pour un délai plus long, ajoutez une étape [Délai]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) avant une étape de message in-app dans un Canvas. Pour la configuration du délai, consultez [Livraison par événement]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-2-select-delay-length).

Ce comportement temporel peut produire des affichages inattendus, en particulier si l'option **Re-evaluate campaign eligibility before displaying** n'est pas sélectionnée dans la campagne.

Par exemple, un utilisateur pourrait recevoir un message in-app avec un délai de huit secondes un mois après le lancement de la campagne. Cela peut se produire s'il a démarré une session, l'a immédiatement terminée, a démarré une nouvelle session un mois plus tard, puis a reçu le message in-app huit secondes après. S'il quitte l'application sans la fermer, le message in-app s'affiche lorsqu'il revient dans l'application.

## Considérations relatives au contenu {#content-considerations}

- Quelles langues utiliserez-vous dans ce message ?
- Quels sont le titre et le corps de votre texte ? Sont-ils accrocheurs et pertinents pour votre utilisateur ?
- Les messages in-app ne s'affichent que pendant une durée limitée. Votre texte est-il concis et mémorable ?
- Utiliserez-vous [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) pour ajouter du texte personnalisé ?
- Les utilisateurs ont-ils besoin de copier le texte du message (comme un code de réduction ou un bon d'achat) ? Sur iOS et Android, les utilisateurs peuvent appuyer longuement sur du texte ou des champs de saisie de texte pour copier le contenu. L'appui long ne fonctionne pas sur les images : utilisez donc du texte ou des champs de saisie de texte plutôt que des images contenant des codes ou tout autre contenu que les utilisateurs pourraient avoir besoin de copier.
- Pour les messages in-app plein écran, votre image ou autre média se trouve-t-il dans la [zone de sécurité]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone) ?
- Pour les messages in-app de type sondage, souhaitez-vous enregistrer des attributs ou des soumissions ? Avez-vous configuré votre page de confirmation ?
- Pour les messages in-app HTML personnalisés, votre HTML inclut-il l'encodage UTF-8 pour afficher correctement les caractères spéciaux ? Consultez [Messages in-app HTML personnalisés]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding) pour en savoir plus.
- Si vous incluez une vidéo dans votre message in-app : bien que Braze n'impose pas de limite technique sur la taille des fichiers vidéo pour la lecture locale sur l'appareil, gardez à l'esprit que les utilisateurs peuvent avoir des connexions lentes, des forfaits de données coûteux ou un espace de stockage limité. Optimisez les fichiers vidéo pour trouver le juste équilibre entre qualité et taille de fichier.

## Optimiser les performances des messages in-app {#optimize-in-app-message-performance}

Braze envoie les déclencheurs de messages in-app éligibles à l'utilisateur au début de la session. La préparation d'un grand nombre de messages avec Liquid peut retarder le démarrage de la session et affecter les performances de l'application.

Si ce traitement prend plus de quelques secondes, Braze peut différer le rendu Liquid restant. Chaque message est alors rendu au moment du déclenchement et récupéré à la demande. Cette [livraison avec modèle]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages) protège vos utilisateurs d'une dégradation des performances de l'application causée par une latence de réponse accrue.

Utilisez ces bonnes pratiques pour accélérer la livraison de vos messages :

- Ne ciblez que les utilisateurs susceptibles d'effectuer l'action de déclenchement de la campagne. Un ciblage trop large peut conduire des utilisateurs à recevoir un déclencheur de message in-app qu'ils ne pourront jamais activer. Par exemple, un message in-app déclenché par une notification push spécifique peut être restreint pour utiliser la même audience cible. Ce principe peut être appliqué de la même manière pour d'autres types de Campaigns, de Canvas, d'événements personnalisés ne pouvant être déclenchés que par certains utilisateurs, etc.
- Définissez une date de fin pour les Campaigns sensibles au temps. Arrêtez les Campaigns lorsque vous ne vous attendez plus à recevoir des impressions.
- Évitez d'insérer de grandes feuilles de style statiques, des scripts ou des ressources média encodées en base64 directement dans le message ou via un bloc de contenu. Utilisez plutôt la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) pour réduire le temps de rendu de votre message.
- Réduisez la logique Liquid complexe avec branchements ou boucles.
- N'activez la rééligibilité que lorsque les utilisateurs doivent recevoir un message plusieurs fois. Si la rééligibilité est désactivée, Braze cesse d'envoyer le déclencheur de message in-app une fois que l'utilisateur l'a vu. Pour plus d'informations, consultez [Rééligibilité]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- Attribuez une priorité plus élevée aux Campaigns importantes. Braze effectue le rendu des messages éligibles de priorité supérieure en premier, ce qui rend la livraison avec modèle moins probable lorsqu'un utilisateur est éligible à de nombreuses Campaigns. Pour plus d'informations, consultez [Choisir une priorité]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority).

### Séparer le code statique et les ressources {#separate-static-code-and-assets}

Conservez les valeurs personnalisées et les règles conditionnelles dans le message. Hébergez les CSS, JavaScript et ressources média réutilisables dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), puis créez des liens vers ces fichiers.

Cela n'est pas nécessaire pour tous les scripts et styles. C'est principalement utile pour réduire l'encombrement dû à des ressources volumineuses telles que des styles de marque partagés et des scripts complexes comme des widgets interactifs.

Les feuilles de style et les scripts de la bibliothèque multimédia n'évaluent pas le Liquid, ce qui permet à l'appareil de l'utilisateur de les mettre en cache. L'exemple suivant conserve les valeurs dynamiques en ligne et charge le code réutilisable à partir de fichiers statiques :

{% raw %}

```liquid
<head>
  <style>
    /* Select a hero image URL based on the user's subscription tier. */
    {% capture hero_image_url %}
      {% if custom_attribute.${subscription_tier} == 'premium' %}
        https://braze-images.com/path/to/premium/hero.jpg
      {% else %}
        https://braze-images.com/path/to/standard/hero.jpg
      {% endif %}
    {% endcapture %}
    /* Assigning to a CSS variable so it can be used inside our stylesheet. */
    :root {
      --hero-image: url("{{ hero_image_url | url_escape }}");
    }
  </style>
  <script>
    // Assigning to the global window object so the value can be referenced in our script.
    window.brandConfig = {
      subscriptionTier: "{{custom_attribute.${subscription_tier} | json_escape }}"
    };
  </script>
  <!-- Linking to a stylesheet from the Braze media library. -->
  <link rel="stylesheet" href="https://braze-images.com/path/to/media/library/asset.css">
  <!-- Linking to a script from the Braze media library. -->
  <script src="https://braze-images.com/path/to/other/media/library/asset.js" defer></script>
</head>

<body>
  <div class="hero"></div>
  <div class="user-styles" data-subscription-tier="{{custom_attribute.${subscription_tier} | escape}}">
    ...
  </div>
</body>
```

{% endraw %}

La feuille de style de la bibliothèque multimédia peut référencer les variables CSS et définir d'autres styles réutilisables :

```css
.hero {
  background-image: var(--hero-image);
}

.user-styles {
  /* styles for all users */
}

.user-styles[data-subscription-tier="premium"] {
  /* premium subscription tier user styles, color scheme, etc */
}

.user-styles[data-subscription-tier="standard"] {
  /* standard subscription tier user styles, color scheme, etc */
}
```

Le script de la bibliothèque multimédia peut utiliser les variables JavaScript en ligne pour ajouter un comportement réutilisable :

```javascript
const config = window.brandConfig || {};

if (config.subscriptionTier === "standard") {
  // add some sort of logic to show a "subscribe to premium" button
} else if (config.subscriptionTier === "premium") {
  // thank the user for being a premium user
}
```

## Considérations relatives à la conversion {#conversion-considerations}

- Quel est votre objectif pour ce message ? Comment pouvez-vous le représenter dans votre message ?
- Vos boutons offrent-ils des options pertinentes pour votre utilisateur ? Quel est votre [appel à l'action principal]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons) ?
- Créez-vous des [deep links vers d'autres contenus in-app]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content) ? Utilisez-vous ce message in-app pour envoyer et accepter une [demande d'autorisation ou d'amorçage de notification push]({{site.baseurl}}/user_guide/channels/push/best_practices) ?
- Disposez-vous d'une option de fermeture du message ? Si ce n'est pas le cas, vous pouvez toujours copier-coller cet extrait de code pour créer un bouton rapide :
  ```html
  <a href="appboy://close">X</a>
  ```

## Considérations relatives à l'éditeur par glisser-déposer {#drag-and-drop-editor-considerations}

### Ajout de deep links pour différents appareils {#adding-deep-links-for-different-devices}

L'éditeur par glisser-déposer ne prend pas en charge l'ajout de deep links différents pour différents appareils (contrairement à l'éditeur traditionnel).

### Ajustement de l'opacité de l'image d'arrière-plan {#adjusting-background-image-opacity}

Le réglage de l'opacité ne permet pas une transparence complète des images d'arrière-plan (contrairement à l'éditeur traditionnel de messages in-app). Vous pouvez utiliser les paramètres d'opacité pour rendre la couleur d'arrière-plan du message complètement transparente.

### Définition de la largeur maximale {#setting-the-maximum-width}

La largeur maximale dans l'éditeur par glisser-déposer est limitée à 325 px ; cela vise principalement à s'adapter à l'aperçu du tableau de bord. Les messages peuvent s'afficher correctement sur les appareils à écrans plus petits.

### Sélection de différents arrière-plans pour différentes plateformes {#selecting-different-backgrounds-for-different-platforms}

Il n'est pas possible d'afficher deux arrière-plans différents pour le même message sur des plateformes différentes (comme le web et le mobile).

### Application des styles de message {#applying-message-styles}

Les images d'arrière-plan s'appliquent à l'ensemble du message et ne peuvent pas être personnalisées par page. Les styles de message s'appliquent à l'ensemble du message, et non aux pages individuelles.

### Mesure de la hauteur des blocs d'espacement {#measuring-spacer-blocks-height}

L'unité de mesure des blocs d'espacement est le pixel (px) et ne peut pas être modifiée.

### Formats pris en charge {#supported-formats}

Actuellement, seuls les messages in-app de type fenêtre modale et plein écran sont pris en charge dans l'éditeur par glisser-déposer.

### Ajustement à la taille et au rapport hauteur/largeur {#adjusting-to-size-and-aspect-ratio}

L'image d'arrière-plan étirera le message in-app, car la fenêtre modale s'ajuste à la taille et au rapport hauteur/largeur de l'image d'arrière-plan ; vous pouvez ajuster le rapport selon vos besoins.

### Images d'arrière-plan et comportement au clic {#background-images-and-on-click-behavior}

Ceux-ci persistent d'une page à l'autre. Pour les messages in-app multi-pages avec des images pleine page différentes sur chaque page, ajoutez un bouton pour permettre aux utilisateurs de cliquer pour accéder à la page suivante.