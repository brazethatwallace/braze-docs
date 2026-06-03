{% multi_lang_include developer_guide/prerequisites/roku.md %} En outre, les messages in-app ne seront envoyés qu'aux appareils Roku exécutant la version minimale du SDK prise en charge :

{% sdk_min_versions roku:0.1.2 %}

## Types de messages {#message-types}

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Activation des messages in-app {#enabling-in-app-messages}

### Étape 1 : Ajouter un observateur {#step-1-add-an-observer}

Pour traiter les messages in-app, vous pouvez ajouter un observateur sur `BrazeTask.BrazeInAppMessage` :

```brightscript
m.BrazeTask.observeField("BrazeInAppMessage", "onInAppMessageReceived")
```

### Étape 2 : Accéder aux messages déclenchés {#step-2-access-triggered-messages}

Puis, dans votre gestionnaire, vous avez accès au message in-app le plus prioritaire que vos Campaigns ont déclenché :

```brightscript
sub onInAppMessageReceived()
  in_app_message = m.BrazeTask.BrazeInAppMessage
  ...
end sub
```

## Champs de messages {#message-fields}

### Gestion {#handling}

Voici la liste des champs dont vous aurez besoin pour gérer vos messages in-app :

| Champs | Description |
| ------ | ----------- |
| `buttons` | Liste des boutons (peut être une liste vide). |
| `click_action` | `"URI"` ou `"NONE"`. Utilisez ce champ pour indiquer si le message in-app doit s'ouvrir sur un lien URI ou fermer le message lorsqu'on clique dessus. Lorsqu'il n'y a pas de boutons, cela doit se produire lorsque l'utilisateur clique sur « OK » quand le message in-app s'affiche. |
| `dismiss_type` | `"AUTO_DISMISS"` ou `"SWIPE"`. Utilisez ce champ pour indiquer si votre message in-app sera automatiquement fermé ou nécessitera un balayage pour être fermé. |
| `display_delay` | Durée d'attente (en secondes) avant l'affichage du message in-app. |
| `duration` | Durée d'affichage (en millisecondes) du message quand `dismiss_type` est défini sur `"AUTO_DISMISS"`. |
| `extras` | Paires clé-valeur. |
| `header` | Le texte de l'en-tête. |
| `id` | L'ID utilisé pour journaliser les impressions ou les clics. |
| `image_url` | URL de l'image du message in-app. |
| `message` | Texte du corps du message. |
| `uri` | L'URI vers laquelle vos utilisateurs seront redirigés en fonction de votre `click_action`. Ce champ doit être inclus lorsque `click_action` est `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Handling" }

{% alert important %}
Pour les messages in-app contenant des boutons, le `click_action` du message sera également inclus dans le payload final si l'action de clic est ajoutée avant l'ajout du texte du bouton.
{% endalert %}

### Style {#styling}

Il existe également plusieurs champs de style que vous pouvez choisir d'utiliser depuis le tableau de bord :

| Champs | Description |
| ------ | ----------- |
| `bg_color` | Couleur d'arrière-plan. |
| `close_button_color` | Couleur du bouton de fermeture. |
| `frame_color` | Couleur de l'overlay de l'écran d'arrière-plan. |
| `header_text_color` | Couleur du texte de l'en-tête. |
| `message_text_color` | Couleur du texte du message. |
| `text_align` | « START », « CENTER » ou « END ». L'alignement de texte sélectionné. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Styling" }

Vous pouvez également implémenter le message in-app et le styliser dans votre application Roku à l'aide d'une palette standard :

### Boutons {#buttons}

| Champs | Description |
| ------ | ----------- |
| `click_action` | `"URI"` ou `"NONE"`. Utilisez ce champ pour indiquer si le message in-app doit s'ouvrir sur un lien URI ou fermer le message lorsqu'on clique dessus. |
| `id` | La valeur d'ID du bouton lui-même. |
| `text` | Le texte à afficher sur le bouton. |
| `uri` | L'URI vers laquelle vos utilisateurs seront redirigés en fonction de votre `click_action`. Ce champ doit être inclus lorsque `click_action` est `"URI"`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Buttons" }