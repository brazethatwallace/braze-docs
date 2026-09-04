{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Configuration des notifications push {#setting-up-push-notifications}

### Étape 1 : Effectuer la configuration initiale {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### Étape 1.1 : S'inscrire aux notifications push {#step-11-register-for-push}

Inscrivez-vous aux notifications push à l'aide de l'API Firebase Cloud Messaging (FCM) de Google. Pour une procédure complète, consultez les étapes suivantes du [guide d'intégration push natif Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/) :

1. [Ajouter Firebase à votre projet]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-1-add-firebase-to-your-project).
2. [Ajouter Cloud Messaging à vos dépendances]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-2-add-cloud-messaging-to-your-dependencies).
3. [Créer un compte de service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-3-create-a-service-account).
4. [Générer des identifiants JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-generate-json-credentials).
5. [Charger vos identifiants JSON dans Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-5-upload-your-json-credentials-to-braze).

#### Étape 1.2 : Obtenir votre Google Sender ID {#step-12-get-your-google-sender-id}

Tout d'abord, accédez à la console Firebase, ouvrez votre projet, puis sélectionnez <i class="fa-solid fa-gear" aria-label="Paramètres"></i>&nbsp;**Settings** > **Project settings**.

![Le projet Firebase avec le menu « Settings » ouvert.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Sélectionnez **Cloud Messaging**, puis sous **Firebase Cloud Messaging API (V1)**, copiez le **Sender ID** dans votre presse-papiers.

![La page « Cloud Messaging » du projet Firebase avec le « Sender ID » mis en évidence.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### Étape 1.3 : Mettre à jour votre `braze.xml` {#step-13-update-your-brazexml}

Ajoutez ce qui suit à votre fichier `braze.xml`. Remplacez `FIREBASE_SENDER_ID` par l'identifiant d'expéditeur que vous avez copié précédemment.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### Étape 1.1 : Charger les certificats APNs {#step-11-upload-apns-certificates}

Générez un certificat Apple Push Notification service (APNs) et chargez-le dans le tableau de bord de Braze. Pour une procédure complète, consultez [Charger votre certificat APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-upload-your-apns-certificate).

#### Étape 1.2 : Ajouter la prise en charge des notifications push à votre application {#step-12-add-push-notification-support-to-your-app}

Suivez le [guide d'intégration natif iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

### Étape 2 : Écouter les événements de notification push (facultatif) {#step-2-listen-for-push-notification-events-optional}

Pour écouter les événements de notification push que Braze a détectés et traités, appelez `subscribeToPushNotificationEvents()` et passez un argument à exécuter.

{% alert note %}
Les événements de notification push de Braze sont disponibles sur Android et iOS. En raison des différences entre les plateformes, iOS ne détecte les événements push de Braze que lorsqu'un utilisateur a interagi avec une notification.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### Champs des événements de notification push {#push-notification-event-fields}

{% alert note %}
En raison des limitations de la plateforme iOS, le SDK de Braze ne peut traiter les payloads push que lorsque l'application est au premier plan. Les écouteurs ne se déclenchent que pour le type d'événement `push_opened` sur iOS après qu'un utilisateur a interagi avec une notification push.
{% endalert %}

Pour une liste complète des champs de notification push, consultez le tableau suivant :

| Nom du champ | Type | Description |
| ------------------ | --------- | ----------- |
| `payloadType` | String | Spécifie le type de payload de la notification. Les deux valeurs envoyées par le SDK Flutter de Braze sont `push_opened` et `push_received`. Seuls les événements `push_opened` sont pris en charge sur iOS. |
| `url` | String | Spécifie l'URL ouverte par la notification. |
| `useWebview` | Boolean | Si `true`, l'URL s'ouvre dans l'application dans une webview modale. Si `false`, l'URL s'ouvre dans le navigateur de l'appareil. |
| `title` | String | Représente le titre de la notification. |
| `body` | String | Représente le corps ou le texte de contenu de la notification. |
| `summaryText` | String | Représente le texte résumé de la notification. Correspond à `subtitle` sur iOS. |
| `badgeCount` | Number | Représente le nombre de badges de la notification. |
| `timestamp` | Number | Représente l'heure à laquelle le payload a été reçu par l'application. |
| `isSilent` | Boolean | Si `true`, le payload est reçu silencieusement. Pour plus de détails sur l'envoi de notifications push silencieuses sur Android, consultez [Notifications push silencieuses sur Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Pour plus de détails sur l'envoi de notifications push silencieuses sur iOS, consultez [Notifications push silencieuses sur iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `isBrazeInternal` | Boolean | Vaut `true` si un payload de notification a été envoyé pour une fonctionnalité interne du SDK, comme la synchronisation des Feature Flags ou le suivi des désinstallations. Le payload est reçu silencieusement pour l'utilisateur. |
| `imageUrl` | String | Spécifie l'URL associée à l'image de la notification. |
| `brazeProperties` | Object | Représente les propriétés Braze associées à la Campaign (paires clé-valeur). |
| `ios` | Object | Représente les champs spécifiques à iOS. |
| `android` | Object | Représente les champs spécifiques à Android. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Champs des événements de notification push" }

### Étape 3 : Tester l'affichage des notifications push {#step-3-test-displaying-push-notifications}

Pour tester votre intégration après avoir configuré les notifications push dans la couche native :

1. Définissez un utilisateur actif dans l'application Flutter. Pour ce faire, initialisez votre plugin en appelant `braze.changeUser('your-user-id')`.
2. Accédez à **Campaigns** et créez une nouvelle Campaign de notification push. Choisissez les plateformes que vous souhaitez tester.
3. Composez votre notification de test et rendez-vous dans l'onglet **Test**. Ajoutez le même `user-id` que l'utilisateur test et cliquez sur **Send Test**.
4. Vous devriez recevoir la notification sur votre appareil sous peu. Vous devrez peut-être vérifier le centre de notifications ou mettre à jour les paramètres si elle ne s'affiche pas.

{% alert tip %}
À partir de Xcode 14, vous pouvez tester les notifications push distantes sur un simulateur iOS.
{% endalert %}

### Étape 4 : Ajouter des deep links (Android) {#step-4-add-deep-links-android}

{% alert warning %}
Sur Android, `com_braze_handle_push_deep_links_automatically` est défini par défaut sur `false`. Avec cette valeur par défaut, appuyer sur une notification push envoie toujours un événement `push_opened` à votre écouteur Dart, mais le SDK natif ne met pas votre application au premier plan et n'ouvre pas automatiquement la destination du deep link. Si votre application ne se lance pas lorsqu'une notification est tapée, ce paramètre en est la cause la plus probable.
{% endalert %}

Pour permettre à Braze d'ouvrir automatiquement votre application et tout deep link lorsqu'une notification push est tapée, définissez `com_braze_handle_push_deep_links_automatically` sur `true` dans votre `braze.xml` :

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Ce paramètre peut également être défini via la [configuration à l'exécution]({{site.baseurl}}/developer_guide/sdk_integration#android_runtime-configuration) dans votre code Android natif :

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

Si vous souhaitez gérer les deep links de manière personnalisée, utilisez l'écouteur `subscribeToPushNotificationEvents()` décrit à l'étape 2 pour router vous-même le champ `url` de l'événement `push_opened`. Pour plus d'informations, consultez [Création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=flutter).