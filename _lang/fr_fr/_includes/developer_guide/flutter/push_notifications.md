{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Mise en place des notifications push {#setting-up-push-notifications}

### Étape 1 : Terminer la configuration initiale {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### Étape 1.1 : S'enregistrer pour les notifications push {#step-11-register-for-push}

Enregistrez-vous pour les notifications push en utilisant l'API Firebase Cloud Messaging (FCM) de Google. Pour une présentation complète, reportez-vous aux étapes suivantes du [guide d'intégration des notifications push Android natif]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/) :

1. [Ajoutez Firebase à votre projet]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Ajoutez Cloud Messaging à vos dépendances]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Créez un compte de service]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [Générez des identifiants JSON]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Téléchargez vos identifiants JSON sur Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

#### Étape 1.2 : Obtenir votre ID d'expéditeur Google {#step-12-get-your-google-sender-id}

Tout d'abord, accédez à la console Firebase, ouvrez votre projet, puis sélectionnez <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![Le projet Firebase avec le menu « Settings » ouvert.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Sélectionnez **Cloud Messaging**, puis sous **Firebase Cloud Messaging API (V1)**, copiez le **Sender ID** dans votre presse-papiers.

![La page « Cloud Messaging » du projet Firebase avec le « Sender ID » mis en surbrillance.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### Étape 1.3 : Mettre à jour votre `braze.xml` {#step-13-update-your-brazexml}

Ajoutez ce qui suit à votre fichier `braze.xml`. Remplacez `FIREBASE_SENDER_ID` par l'ID d'expéditeur que vous avez copié précédemment.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### Étape 1.1 : Télécharger les certificats APNs {#step-11-upload-apns-certificates}

Générez un certificat pour le service de notification push d'Apple (APNs) et téléchargez-le dans le tableau de bord de Braze. Pour une description complète, consultez [Télécharger votre certificat APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

#### Étape 1.2 : Ajouter la prise en charge des notifications push à votre application {#step-12-add-push-notification-support-to-your-app}

Suivez le [guide d'intégration native pour iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

### Étape 2 : Écouter les événements de notification push (facultatif) {#step-2-listen-for-push-notification-events-optional}

Pour écouter les événements de notifications push que Braze a détectés et traités, appelez `subscribeToPushNotificationEvents()` et transmettez un argument à exécuter.

{% alert note %}
Les événements de notification push de Braze sont disponibles sur Android et iOS. En raison des différences entre les plateformes, iOS ne détectera les événements push de Braze que lorsqu'un utilisateur aura interagi avec une notification.
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

##### Champs d'événements de notification push {#push-notification-event-fields}

{% alert note %}
En raison des limitations de la plateforme sur iOS, le SDK de Braze ne peut traiter les payloads des notifications push que lorsque l'application est au premier plan. Les écouteurs ne se déclencheront pour le type d'événement `push_opened` sur iOS qu'après qu'un utilisateur aura interagi avec une notification push.
{% endalert %}

Pour obtenir la liste complète des champs de notifications push, reportez-vous au tableau ci-dessous :

| Nom du champ | Type | Description |
| ------------------ | --------- | ----------- |
| `payloadType` | Chaîne de caractères | Spécifie le type de payload de la notification. Les deux valeurs envoyées par le SDK Braze pour Flutter sont `push_opened` et `push_received`. Seuls les événements `push_opened` sont pris en charge sur iOS. |
| `url` | Chaîne de caractères | Spécifie l'URL qui a été ouverte par la notification. |
| `useWebview` | Valeur booléenne | Si la valeur est `true`, l'URL s'ouvrira dans l'application, dans une fenêtre WebView modale. Si la valeur est `false`, l'URL s'ouvrira dans le navigateur de l'appareil. |
| `title` | Chaîne de caractères | Représente le titre de la notification. |
| `body` | Chaîne de caractères | Représente le corps ou le contenu du texte de la notification. |
| `summaryText` | Chaîne de caractères | Représente le texte résumé de la notification. Celui-ci est mappé à partir de `subtitle` sur iOS. |
| `badgeCount` | Nombre | Représente le nombre de badges de la notification. |
| `timestamp` | Nombre | Représente l'heure à laquelle le payload a été reçu par l'application. |
| `isSilent` | Valeur booléenne | Si la valeur est `true`, le payload est reçu en silence. Pour plus de détails sur l'envoi de notifications push silencieuses sur Android, reportez-vous à la section [Notifications push silencieuses sur Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Pour plus de détails sur l'envoi de notifications push silencieuses sur iOS, reportez-vous à la section [Notifications push silencieuses sur iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `isBrazeInternal` | Valeur booléenne | La valeur sera `true` si un payload de notification a été envoyé pour une fonctionnalité interne du SDK, telle que la synchronisation des indicateurs de fonctionnalités ou le suivi des désinstallations. Le payload est reçu silencieusement par l'utilisateur. |
| `imageUrl` | Chaîne de caractères | Spécifie l'URL associée à l'image de la notification. |
| `brazeProperties` | Objet | Représente les propriétés de Braze associées à la campagne (paires clé-valeur). |
| `ios` | Objet | Représente les champs spécifiques à iOS. |
| `android` | Objet | Représente les champs spécifiques à Android. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push notification event fields" }

### Étape 3 : Tester l'affichage des notifications push {#step-3-test-displaying-push-notifications}

Pour tester votre intégration après avoir configuré les notifications push dans la couche native :

1. Configurez un utilisateur actif dans l'application Flutter. Pour ce faire, initialisez votre plug-in en appelant `braze.changeUser('your-user-id')`.
2. Accédez à **Campaigns** et créez une nouvelle campagne de notification push. Choisissez les plateformes que vous souhaitez tester.
3. Composez votre notification de test et rendez-vous dans l'onglet **Test**. Ajoutez le même `user-id` que l'utilisateur test et cliquez sur **Send Test**.
4. Vous devriez recevoir rapidement la notification sur votre appareil. Vous devrez peut-être vérifier le centre de notifications ou mettre à jour les paramètres si elle ne s'affiche pas.

{% alert tip %}
À partir de Xcode 14, vous pouvez tester les notifications push à distance sur un simulateur iOS.
{% endalert %}