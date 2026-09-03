---
nav_title: "HTML personnalisé"
article_title: "HTML personnalisé"
page_order: 4
page_type: reference
description: "Cet article fournit un aperçu des messages in-app avec code personnalisé, y compris les méthodes JavaScript, le suivi des boutons et l'utilisation de la prévisualisation HTML interactive dans Braze."
channel:
  - in-app messages
---

# Messages in-app HTML personnalisés {#custom-html-messages}

> Bien que nos messages in-app standard puissent être personnalisés de nombreuses façons, vous pouvez obtenir un contrôle encore plus grand sur l'apparence de vos campagnes en utilisant des messages conçus et construits avec HTML, CSS et JavaScript. Avec une composition simple, vous pouvez débloquer des fonctionnalités et un branding personnalisés pour répondre à tous vos besoins.

Ce type de message est disponible dans l'[éditeur traditionnel]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

## Fonctionnement {#how-it-works}

Les messages in-app HTML permettent un contrôle accru sur l'apparence et le rendu d'un message, notamment les éléments suivants :

- Polices et styles personnalisés
- Vidéos
- Images multiples
- Comportements au clic
- Composants interactifs
- Animations personnalisées

Les messages HTML personnalisés peuvent utiliser les méthodes du [pont JavaScript](#javascript-bridge) pour enregistrer des événements, définir des attributs personnalisés, fermer le message, et bien plus encore ! Consultez notre [dépôt GitHub](https://github.com/braze-inc/in-app-message-templates) qui contient des instructions détaillées sur la façon d'utiliser et de personnaliser les messages in-app HTML selon vos besoins, ainsi qu'un ensemble de modèles de messages in-app HTML5 pour vous aider à démarrer.

{% alert note %}
Pour activer les messages in-app HTML via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze : par exemple, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Ceci est nécessaire pour des raisons de sécurité, car les messages in-app HTML peuvent exécuter du JavaScript, et un responsable du site doit donc les activer.
{% endalert %}

### Environnements de rendu {#rendering-environments}

Les messages in-app HTML personnalisés s'affichent directement dans le navigateur sur le web, mais à l'intérieur d'une WebView de la plateforme sur iOS et Android. Étant donné que chaque environnement utilise un moteur de rendu différent, le même HTML et CSS peut s'afficher avec de légères différences visuelles selon les plateformes, en particulier pour les mises en page en colonnes, les polices et l'espacement.

Pour minimiser les différences entre plateformes :

- Utilisez des valeurs CSS explicites plutôt que de vous appuyer sur les valeurs par défaut du navigateur
- Incluez une balise meta viewport (par exemple, `<meta name="viewport" content="width=device-width, initial-scale=1">`)
- Testez sur des appareils réels avec des envois de test

## Encodage des caractères {#character-encoding}

Lorsque vous créez des messages in-app HTML personnalisés contenant des caractères spéciaux — tels que l'alphabet cyrillique, des caractères accentués ou d'autres textes non ASCII — incluez l'encodage UTF-8 dans votre HTML pour garantir un affichage correct. Sans l'encodage UTF-8, ces caractères peuvent apparaître cassés ou manquants lors du rendu dans la webview.

Pour activer l'encodage UTF-8, ajoutez la balise meta suivante dans la section `<head>` de votre HTML :

```html
<meta charset="UTF-8">
```

Cela force l'encodage UTF-8, qui est le jeu de caractères attendu pour les webviews affichant les messages in-app.

## Pont JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}

## Actions basées sur les liens {#link-based-actions}

En plus du JavaScript personnalisé, les SDK Braze peuvent également envoyer des données analytiques avec ces raccourcis d'URL pratiques. Notez que ces paramètres de requête et schémas d'URL sont tous sensibles à la casse.

### Suivi des clics sur les boutons (obsolète) {#button-click-tracking-deprecated}

{% alert warning %}
L'utilisation de `abButtonID` n'est pas prise en charge dans les types de messages [HTML avec aperçu]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview). Pour plus d'informations, consultez notre [guide de mise à niveau]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview).
{% endalert %}

Pour enregistrer les clics sur les boutons dans les analyses des messages in-app, vous pouvez ajouter `abButtonId` comme paramètre de requête à tout deep link, URL de redirection ou élément d'ancrage `<a>`. Utilisez `?abButtonId=0` pour enregistrer un clic sur « Bouton 1 », et `?abButtonId=1` pour enregistrer un clic sur « Bouton 2 ».

Comme pour les autres paramètres d'URL, le premier paramètre doit commencer par un point d'interrogation `?`, tandis que les paramètres suivants doivent être séparés par une esperluette `&`.

#### Exemples d'URL {#example-urls}

- `https://example.com/?abButtonId=0` - Clic sur le bouton 1
- `https://example.com/?abButtonId=1` - Clic sur le bouton 2
- `https://example.com/?utm_source=braze&abButtonId=0` - Clic sur le bouton 1 avec d'autres paramètres d'URL existants
- `myApp://deep-link?page=home&abButtonId=1` - Deep link mobile avec clic sur le bouton 2
- `<a href="https://example.com/?abButtonId=1">` - Élément d'ancrage `<a>` avec clic sur le bouton 2

{% alert note %}
Les messages in-app ne prennent en charge que les clics sur le bouton 1 et le bouton 2. Les URL qui ne spécifient pas l'un de ces deux identifiants de bouton seront enregistrées comme des « clics sur le corps » génériques.
{% endalert %}

### Ouvrir un lien dans une nouvelle fenêtre (mobile uniquement) {#open-link-in-new-window-mobile-only}

Pour ouvrir des liens en dehors de votre application dans une nouvelle fenêtre, définissez `?abExternalOpen=true`. Le message sera fermé avant l'ouverture du lien.

Pour le deep linking, Braze ouvrira votre URL quelle que soit la valeur de `abExternalOpen`.

### Ouvrir en tant que deep link (mobile uniquement) {#open-as-deeplink-mobile-only}

Pour que Braze traite votre lien HTTP ou HTTPS comme un deep link, définissez `?abDeepLink=true`.

Lorsque ce paramètre de chaîne de requête est absent ou défini sur `false`, Braze tentera d'ouvrir le lien web dans un navigateur web interne à l'intérieur de l'application hôte.

### Fermer le message in-app {#close-in-app-message}

Pour fermer un message in-app, vous pouvez utiliser la méthode JavaScript `brazeBridge.closeMessage()`.

Par exemple, `<a onclick="brazeBridge.closeMessage()" href="#">Fermer</a>` fermera le message in-app.

## Téléchargement HTML avec aperçu {#html-upload-with-preview}

Lors de la création de messages in-app HTML personnalisés, vous pouvez prévisualiser votre contenu interactif directement dans Braze.

Le panneau d'aperçu du message dans l'éditeur affiche un aperçu réaliste qui exécute le JavaScript inclus dans votre message. Vous pouvez prévisualiser et interagir avec vos messages personnalisés depuis le panneau d'aperçu en naviguant entre les pages, en soumettant des formulaires ou des sondages, en regardant des animations JavaScript, et plus encore !

![Interaction avec l'aperçu HTML en faisant défiler les pages.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Les méthodes JavaScript `brazeBridge` que vous utilisez dans votre HTML ne mettront pas à jour les profils utilisateur lors de la prévisualisation dans le tableau de bord.
{% endalert %}

### Créer une campagne {#instructions}

#### Fichiers de ressources {#asset-files}

Lors de la création de messages in-app avec code personnalisé par téléchargement HTML, vous pouvez télécharger les ressources de la campagne dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) pour les référencer dans votre message.

Les types de fichiers suivants sont pris en charge pour le téléchargement :

| Type de fichier        | Extension de fichier              |
| :--------------------- | :-------------------------------- |
| Fichiers de polices    | `.ttf`, `.woff`, `.otf`, `.woff2` |
| Images SVG             | `.svg`                            |
| Fichiers JavaScript    | `.js`                             |
| Fichiers CSS           | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fichiers de ressources" }

Braze recommande de télécharger les ressources dans la bibliothèque multimédia pour deux raisons :

1. Les ressources ajoutées à une campagne via la bibliothèque multimédia permettent à vos messages de s'afficher même lorsque l'utilisateur est hors ligne ou dispose d'une mauvaise connexion Internet.
2. Les ressources téléchargées dans Braze peuvent être réutilisées dans plusieurs campagnes.

##### Ajouter des fichiers de ressources {#adding-asset-files}

Vous pouvez ajouter des ressources nouvelles ou existantes à votre campagne.

Pour ajouter de nouvelles ressources à votre campagne, utilisez la section de glisser-déposer pour télécharger un fichier. Les ressources ajoutées dans cette section seront également automatiquement ajoutées à la bibliothèque multimédia. Pour ajouter des ressources que vous avez déjà téléchargées dans la bibliothèque multimédia, sélectionnez **Add from Media Library**.

Une fois vos ressources ajoutées, elles apparaîtront dans la section **Assets for this campaign**.

Si le nom de fichier d'une ressource correspond à celui d'une ressource HTML locale, elle est remplacée automatiquement (par exemple, `cat.png` est téléchargé et `<img src="cat.png" />` existe).

Sinon, survolez une ressource dans la liste et sélectionnez <i class="fas fa-copy"></i> **Copy** pour copier l'URL du fichier dans votre presse-papiers. Collez ensuite l'URL de la ressource copiée dans votre HTML comme vous le feriez normalement pour référencer une ressource distante.

### Éditeur HTML {#html-editor}

Les modifications que vous apportez dans le HTML s'affichent automatiquement dans le panneau d'aperçu au fur et à mesure de la saisie. Les méthodes JavaScript [`brazeBridge`](#bridge) que vous utilisez dans votre HTML ne mettront pas à jour les profils utilisateur lors de la prévisualisation dans le tableau de bord.

{% alert tip %}
Vous pouvez sélectionner <i class="fa-solid fa-magnifying-glass" aria-label="Rechercher"></i> **Search** dans l'éditeur HTML pour effectuer une recherche dans votre code !
{% endalert %}

### Suivi des boutons {#button-tracking-improvements}

Vous pouvez suivre les performances au sein de votre message in-app avec code personnalisé en utilisant la méthode JavaScript [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types). Cela vous permet de suivre programmatiquement « Button 1 », « Button 2 » et « Body Clicks » en utilisant respectivement `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` ou `brazeBridge.logClick()`.

| Clics     | Méthode                       |
| ---------- | ---------------------------- |
| Button 1   | `brazeBridge.logClick('0')` |
| Button 2   | `brazeBridge.logClick('1')` |
| Clic sur le corps | `brazeBridge.logClick()`    |
| Suivi de bouton personnalisé |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Suivi des boutons" }

{% alert note %}
Cette méthode de suivi des boutons remplace les méthodes de suivi automatique des clics précédentes (telles que `?abButtonId=0`), qui ont été supprimées.
{% endalert %}

Utilisez [`brazeBridge.logClick(button_id)`](#button-tracking-improvements) pour les messages HTML avec aperçu lorsque vous avez besoin de plus de deux boutons suivis. Button 1 et Button 2 correspondent à `'0'` et `'1'` ; les boutons supplémentaires utilisent des ID personnalisés (jusqu'à 100 ID uniques par campagne). Pour les restrictions de caractères sur les ID de boutons, consultez [Suivi des boutons](#button-tracking-improvements).

### Résoudre les problèmes de liens HTML personnalisés et de comportement de fermeture {#troubleshoot-custom-html-links-and-close-behavior}

#### Les clics sur les boutons n'ouvrent pas le lien {#button-clicks-do-not-open-the-link}

Si un bouton de votre message in-app HTML personnalisé ne se charge pas lorsqu'on clique dessus, vérifiez que le lien utilise une URL valide ou un schéma de deep link pris en charge. Les URL mal formées ou les schémas personnalisés non pris en charge peuvent empêcher l'action de clic de s'exécuter.

#### Clics sur le corps lors de la fermeture du message {#body-clicks-when-closing-the-message}

L'appel à `brazeBridge.closeMessage()` ferme le message mais n'enregistre pas d'analyse en soi. Pour enregistrer un clic sur le corps lorsque l'utilisateur ferme le message, appelez `brazeBridge.logClick()` avant `brazeBridge.closeMessage()` afin que l'enregistrement des clics reste cohérent sur toutes les plateformes.

#### Le HTML personnalisé ne s'affiche pas sur Android (fichiers zip Windows) {#custom-html-not-rendering-on-android-windows-zip-files}

Si votre message in-app HTML personnalisé s'affiche dans l'aperçu mais ne s'affiche pas sur les appareils Android, vérifiez comment vos fichiers HTML et de ressources ont été empaquetés. Certains utilitaires de compression Windows ajoutent des entrées de répertoire (chemins de dossiers) à l'intérieur de l'archive au lieu de placer les fichiers au niveau racine.

Android peut échouer à charger les ressources référencées avec des chemins relatifs lorsque le zip inclut des entrées de répertoire imbriquées. Pour corriger cela :

1. Extrayez vos fichiers HTML, CSS, JavaScript et images dans un seul dossier.
2. Sélectionnez tous les fichiers (pas le dossier parent) lors de la création de l'archive zip.
3. Confirmez que les chemins dans votre HTML référencent les fichiers à la racine du zip (par exemple, `style.css`, et non `assets/style.css`), ou ajustez les chemins pour correspondre à la structure aplatie.
4. Téléchargez à nouveau le zip et envoyez un message de test à un appareil Android.

Vous pouvez également télécharger les ressources via la [bibliothèque multimédia](#asset-files) au lieu de les regrouper dans un fichier zip.

### Modifications rétro-incompatibles {#backward-incompatible-changes}

1. Le deep link `braze://close`, qui était auparavant pris en charge sur les applications mobiles, a été supprimé au profit de la méthode JavaScript `brazeBridge.closeMessage()`. Cela permet des messages HTML multiplateformes, puisque le web ne prend pas en charge les deep links.
2. Le suivi automatique des clics, qui utilisait `?abButtonId=0` pour les ID de boutons, et le suivi des « clics sur le corps » sur les boutons de fermeture ont été supprimés. Les exemples de code suivants montrent comment modifier votre HTML pour utiliser nos nouvelles méthodes JavaScript de suivi des clics :

   | Avant | Après |
   |:-------- |:------------|
   |<code>&lt;a href="braze://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="braze://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "braze://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modifications rétro-incompatibles" }