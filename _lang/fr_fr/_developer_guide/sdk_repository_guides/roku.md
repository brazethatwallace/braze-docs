---
nav_title: SDK Roku
article_title: Guide du dépôt du SDK Roku
page_order: 8
description: "Référence du README du SDK Roku de Braze, miroir depuis GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## À propos du SDK Roku de Braze {#about-the-braze-roku-sdk}

Le SDK Roku de Braze vous aide à intégrer les fonctionnalités d'envoi de messages, d'analyse et d'engagement utilisateur de Braze dans votre application.

Pour commencer, consultez les ressources suivantes :

- [Guide utilisateur de Braze]({{site.baseurl}}/user_guide/introduction/)
- [Guide développeur de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku)

## Intégration initiale du SDK {#initial-sdk-integration}

Le SDK Roku de Braze vous fournira une API pour transmettre des informations destinées à l'analyse, la segmentation et l'engagement.

## Étape 1 : Ajouter des fichiers {#step-1-add-files}

1. Ajoutez `BrazeSDK.brs` à votre application dans le répertoire `source`.
2. Ajoutez `BrazeTask.brs` et `BrazeTask.xml` à votre application dans le répertoire `components`.

## Étape 2 : Ajouter des références {#step-2-add-references}

Ajoutez une référence à `BrazeSDK.brs` dans votre scène principale en utilisant l'élément `script` suivant :

``` text
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Étape 3 : Configurer {#step-3-configure}

Dans `main.brs`, définissez la configuration Braze sur le nœud global :

``` text
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = "YOUR_API_KEY_HERE"
config[config_fields.ENDPOINT] = "YOUR_ENDPOINT_HERE (e.g. https://sdk.iad-01.braze.com/)"
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

## Étape 4 : Initialiser Braze {#step-4-initialize-braze}

Initialisez l'instance Braze :

``` text
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configuration des messages in-app {#in-app-message-setup}

Pour traiter les messages in-app, vous pouvez ajouter un observateur sur `BrazeTask.BrazeInAppMessage` :

``` text
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

Puis, dans votre gestionnaire, vous avez accès au message in-app le plus prioritaire que vos Campaigns ont déclenché :

``` text
in_app_message = m.BrazeTask.BrazeInAppMessage
```

Vous pouvez ensuite décider quoi faire avec le message in-app. Voici quelques-uns des champs disponibles :

- `in_app_message.message` - Le corps du texte du message in-app
- `in_app_message.buttons` - Liste des boutons (peut être une liste vide).
- `in_app_message.id` - ID à utiliser lors de la journalisation des impressions ou des clics
- `in_app_message.extras` - Paires clé/valeur
- `in_app_message.image_url` - URL de l'image
- `in_app_message.click_action` - Lorsqu'il n'y a pas de boutons, c'est ce qui doit se passer lorsque l'utilisateur clique sur « OK » quand le message in-app est affiché. Peut être « URI » ou « NONE ».
- `in_app_message.dismiss_type` - Peut être « AUTO_DISMISS » ou « SWIPE »
- `in_app_message.display_delay` - Délai d'attente (en secondes) avant d'afficher le message in-app
- `in_app_message.duration` - Durée (en millisecondes) pendant laquelle le message doit être affiché lorsque `dismiss_type` est « AUTO_DISMISS »
- `in_app_message.header` - Le texte d'en-tête du message in-app
- `in_app_message.uri` - Lorsque `click_action` est « URI », ceci doit être affiché

Il existe également divers champs de style que vous pouvez choisir d'utiliser depuis le tableau de bord. Vous pouvez aussi implémenter le message in-app et le styliser dans votre application Roku en utilisant une palette standard.
- `in_app_message.bg_color` - Couleur d'arrière-plan
- `in_app_message.close_button_color` - Couleur du bouton de fermeture
- `in_app_message.frame_color` - La couleur de la superposition d'écran d'arrière-plan
- `in_app_message.header_text_color` - Couleur du texte d'en-tête
- `in_app_message.message_text_color` - Couleur du texte du message
- `in_app_message.text_align` - Peut être « START », « CENTER » ou « END »

Les champs des boutons incluent :
- `buttons[0].click_action` - Peut être « URI » pour indiquer d'ouvrir le champ `uri`. Peut être « NONE » pour indiquer que ce bouton doit fermer le message in-app.
- `buttons[0].id` - La valeur d'ID du bouton lui-même
- `buttons[0].text` - Le texte à afficher sur le bouton
- `buttons[0].uri` - Lorsque `click_action` est « URI », ceci doit être affiché
- `buttons[0].bg_color` - Couleur d'arrière-plan du bouton
- `buttons[0].border_color` - Couleur de bordure du bouton
- `buttons[0].text_color` - Couleur du texte du bouton

Lorsqu'un message est affiché ou vu, journalisez une impression :

``` text
LogInAppMessageImpression(in_app_message.id, brazetask)
```

Une fois qu'un utilisateur clique sur le message, enregistrez un clic :
``` text
LogInAppMessageClick(in_app_message.id, brazetask)
```
puis traitez `in_app_message.click_action`

Si l'utilisateur clique sur un bouton, journalisez le clic sur le bouton :

``` text
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```
puis traitez `inappmessage.buttons[selected].click_action`

Après avoir traité le message in-app, vous devez effacer le champ :

``` text
m.BrazeTask.BrazeInAppMessage = invalid
```

## Intégration de base du SDK terminée {#basic-sdk-integration-complete}

Braze devrait maintenant collecter des données depuis votre application. Veuillez consulter notre documentation publique pour savoir comment journaliser des attributs, des événements et des achats via notre SDK. La scène `MainScene.brs` de notre application d'exemple contient également des exemples d'utilisation de l'API.

`BrazeInAppMessage.brs` et `CustomSideBySideInAppMessage.brs` montrent des exemples de gestion des messages in-app. `onInAppMessageTriggered()` dans `MainScene.brs` montre comment prendre en charge plusieurs dispositions.

## Référence supplémentaire {#additional-reference}

Le répertoire `torchietv` contient une application d'exemple avec le SDK Braze intégré.
<!-- END GENERATED README CONTENT -->

Pour les détails du dépôt et les projets d'exemple, consultez [https://github.com/braze-inc/braze-roku-sdk](https://github.com/braze-inc/braze-roku-sdk).