## Intégrer le SDK Cordova {#integrating-the-cordova-sdk}

### Conditions préalables {#prerequisites}

Avant de commencer, vérifiez que votre environnement est pris en charge par la [dernière version du SDK Cordova de Braze](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements).

### Étape 1 : Ajouter le SDK à votre projet {#step-1-add-the-sdk-to-your-project}

{% alert warning %}
Ajoutez le SDK Cordova de Braze uniquement en utilisant les méthodes suivantes. N'essayez pas de l'installer par d'autres moyens, car cela pourrait entraîner une faille de sécurité.
{% endalert %}

Si vous utilisez Cordova 6 ou une version ultérieure, vous pouvez ajouter le SDK directement depuis GitHub. Vous pouvez également télécharger un fichier ZIP du [dépôt GitHub](https://github.com/braze-inc/braze-cordova-sdk) et ajouter le SDK manuellement.

{% tabs local %}
{% tab géorepérage désactivé %}
Si vous ne prévoyez pas d'utiliser la collecte de localisation et les géorepérages, utilisez la branche `master` depuis GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab géorepérage activé %}
Si vous prévoyez d'utiliser la collecte de localisation et les géorepérages, utilisez la branche `geofence-branch` depuis GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Vous pouvez basculer entre `master` et `geofence-branch` à tout moment en répétant cette étape.
{% endalert %}

### Étape 2 : Configurer votre projet {#step-2-configure-your-project}

Ensuite, ajoutez les préférences suivantes à l'élément `platform` dans le fichier `config.xml` de votre projet.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Remplacez les valeurs suivantes :

| Valeur                | Description                                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BRAZE_API_KEY`       | Votre [clé API REST de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab#rest-api-keys).                                                              |
| `CUSTOM_API_ENDPOINT` | Un endpoint API personnalisé. Cet endpoint est utilisé pour acheminer les données de votre instance Braze vers le groupe d'applications approprié dans votre tableau de bord de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Étape 2 : Configurer votre projet" }

L'élément `platform` dans votre fichier `config.xml` devrait ressembler à ce qui suit :

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Syntaxe spécifique à la plateforme {#platform-specific-syntax}

La section suivante couvre la syntaxe spécifique à la plateforme lors de l'utilisation de Cordova avec iOS ou Android.

### Entiers {#integers}

{% tabs %}
{% tab ios %}
Les préférences de type entier sont lues sous forme de représentations en chaîne de caractères, comme dans l'exemple suivant :

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
En raison de la manière dont le framework Cordova 8.0.0+ gère les préférences, les préférences exclusivement de type entier (telles que les identifiants d'expéditeur) doivent être définies sous forme de chaînes de caractères précédées de `str_`, comme dans l'exemple suivant :

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### Booléens {#booleans}

{% tabs %}
{% tab ios %}
Les préférences de type booléen sont lues par le SDK à l'aide des mots-clés `YES` et `NO` sous forme de représentation en chaîne de caractères, comme dans l'exemple suivant :

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
Les préférences de type booléen sont lues par le SDK à l'aide des mots-clés `true` et `false` sous forme de représentation en chaîne de caractères, comme dans l'exemple suivant :

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Configurations optionnelles {#optional}

Vous pouvez ajouter l'une des préférences suivantes à l'élément `platform` dans le fichier `config.xml` de votre projet :

{% tabs %}
{% tab ios %}
| Méthode                                           | Description                                                                                                                                                                                                                                           |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key`                                     | Définit la clé API pour votre application.                                                                                                                                                                                                            |
| `ios_api_endpoint`                                | Définit l'[endpoint SDK]({{site.baseurl}}/api/basics#endpoints) pour votre application.                                                                                                                                                              |
| `ios_disable_automatic_push_registration`         | Détermine si l'enregistrement automatique des notifications push doit être désactivé.                                                                                                                                                                 |
| `ios_disable_automatic_push_handling`             | Détermine si la gestion automatique des notifications push doit être désactivée.                                                                                                                                                                      |
| `ios_enable_idfa_automatic_collection`            | Détermine si le SDK Braze doit collecter automatiquement les informations IDFA. Pour plus d'informations, consultez [la documentation relative à la méthode Braze IDFA](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection`                      | Détermine si la collecte automatique de la localisation est activée (si l'utilisateur l'autorise). La `geofence-branch`                                                                                                                              |
| `geofences_enabled`                               | Détermine si les géorepérages sont activés.                                                                                                                                                                                                           |
| `ios_session_timeout`                             | Définit le délai d'expiration de la session Braze pour votre application en secondes. La valeur par défaut est de 10 secondes.                                                                                                                        |
| `sdk_authentication_enabled`                      | Détermine si la fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) doit être activée.                                                                                      |
| `display_foreground_push_notifications`           | Détermine si les notifications push doivent s'afficher lorsque l'application est au premier plan.                                                                                                                                                     |
| `ios_disable_un_authorization_option_provisional` | Détermine si `UNAuthorizationOptionProvisional` doit être désactivé.                                                                                                                                                                                  |
| `trigger_action_minimum_time_interval_seconds`    | Définit l'intervalle de temps minimum en secondes entre les déclencheurs. La valeur par défaut est de 30 secondes.                                                                                                                                    |
| `ios_push_app_group`                              | Définit l'ID du groupe d'applications pour les extensions push iOS.                                                                                                                                                                                   |
| `ios_forward_universal_links`                     | Détermine si le SDK reconnaît et transfère automatiquement les liens universels vers les méthodes système. Nécessaire pour que les deep links à partir des notifications push fonctionnent sur iOS. Désactivé par défaut.                              |
| `ios_log_level`                                   | Définit le niveau de journalisation minimum pour `Braze.Configuration.Logger`.                                                                                                                                                                        |
| `ios_use_uuid_as_device_id`                       | Détermine si un UUID généré aléatoirement doit être utilisé comme identifiant de l'appareil.                                                                                                                                                          |
| `ios_flush_interval_seconds`                      | Définit l'intervalle en secondes entre les vidages automatiques des données. La valeur par défaut est de 10 secondes.                                                                                                                                 |
| `ios_use_automatic_request_policy`                | Détermine si la politique de requête pour `Braze.Configuration.Api` doit être automatique ou manuelle.                                                                                                                                                |
| `should_opt_in_when_push_authorized`              | Détermine si l'état d'abonnement aux notifications d'un utilisateur doit être automatiquement défini sur `optedIn` lorsque les autorisations push sont accordées.                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurations optionnelles" }

{% alert tip %}
Pour plus d'informations, consultez [GitHub : plug-in Cordova iOS Braze](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Méthode                                                           | Description                                                                                                                                                                                   |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key`                                                 | Définit la clé API pour votre application.                                                                                                                                                    |
| `android_api_endpoint`                                            | Définit l'[endpoint SDK]({{site.baseurl}}/api/basics#endpoints) pour votre application.                                                                                                      |
| `android_small_notification_icon`                                 | Définit la petite icône de notification.                                                                                                                                                      |
| `android_large_notification_icon`                                 | Définit la grande icône de notification.                                                                                                                                                      |
| `android_notification_accent_color`                               | Définit la couleur d'accentuation des notifications à l'aide d'une représentation hexadécimale.                                                                                               |
| `android_default_session_timeout`                                 | Définit le délai d'expiration de la session Braze pour votre application en secondes. La valeur par défaut est de 10 secondes.                                                                |
| `android_handle_push_deep_links_automatically`                    | Détermine si le SDK Braze gère automatiquement les deep links push. Nécessaire pour que les deep links à partir des notifications push fonctionnent sur Android. Désactivé par défaut.         |
| `android_log_level`                                               | Définit le niveau de journalisation pour votre application. Le niveau par défaut est 4 et enregistre un minimum d'informations. Pour activer la journalisation détaillée à des fins de débogage, utilisez le niveau 2. |
| `firebase_cloud_messaging_registration_enabled`                   | Détermine s'il convient d'utiliser Firebase Cloud Messaging pour les notifications push.                                                                                                      |
| `android_fcm_sender_id`                                           | Définit l'ID de l'expéditeur Firebase Cloud Messaging.                                                                                                                                        |
| `enable_location_collection`                                      | Détermine si la collecte automatique de la localisation est activée (si l'utilisateur l'autorise).                                                                                            |
| `geofences_enabled`                                               | Détermine si les géorepérages sont activés.                                                                                                                                                   |
| `android_disable_auto_session_tracking`                           | Désactive le suivi automatique des sessions par le plug-in Android Cordova. Pour plus d'informations, consultez [Désactivation du suivi automatique des sessions](#cordova_disable-automatic-session-tracking). |
| `sdk_authentication_enabled`                                      | Détermine si la fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) doit être activée.                              |
| `trigger_action_minimum_time_interval_seconds`                    | Définit l'intervalle de temps minimum en secondes entre les déclencheurs. La valeur par défaut est de 30 secondes.                                                                            |
| `is_session_start_based_timeout_enabled`                          | Détermine si le comportement de délai d'expiration de session doit être basé sur les événements de début ou de fin de session.                                                                |
| `default_notification_channel_name`                               | Définit le nom visible par l'utilisateur via `NotificationChannel.getName` pour le `NotificationChannel` par défaut de Braze.                                                                 |
| `default_notification_channel_description`                        | Définit la description visible par l'utilisateur via `NotificationChannel.getDescription` pour le `NotificationChannel` par défaut de Braze.                                                  |
| `does_push_story_dismiss_on_click`                                | Détermine si une Push Story est automatiquement fermée lorsqu'on clique dessus.                                                                                                               |
| `is_fallback_firebase_messaging_service_enabled`                  | Détermine si l'utilisation d'un service Firebase Cloud Messaging de secours est activée.                                                                                                      |
| `fallback_firebase_messaging_service_classpath`                   | Définit le chemin d'accès aux classes pour le service Firebase Cloud Messaging de secours.                                                                                                    |
| `is_content_cards_unread_visual_indicator_enabled`                | Détermine si l'indicateur visuel de Content Cards non lues est activé.                                                                                                                        |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Détermine si le SDK Braze enregistrera automatiquement les jetons dans `com.google.firebase.messaging.FirebaseMessagingService.onNewToken`.                                                   |
| `is_push_deep_link_back_stack_activity_enabled`                   | Détermine si Braze ajoutera une activité à la pile arrière lors du suivi automatique des deep links pour les notifications push.                                                              |
| `push_deep_link_back_stack_activity_class_name`                   | Définit l'activité que Braze ajoutera à la pile arrière lors du suivi automatique des deep links pour les notifications push.                                                                 |
| `should_opt_in_when_push_authorized`                              | Détermine si Braze doit automatiquement abonner l'utilisateur lorsque les notifications push sont autorisées.                                                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurations optionnelles" }

{% alert tip %}
Pour plus d'informations, consultez [GitHub : plug-in Cordova Android Braze](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt).
{% endalert %}
{% endtab %}
{% endtabs %}

Voici un exemple de fichier `config.xml` avec des configurations supplémentaires :

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO"/"YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO"/"YES" />
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES"/"NO" />
    <preference name="com.braze.enable_location_collection" value="NO"/"YES" />
    <preference name="com.braze.geofences_enabled" value="NO"/"YES" />
    <preference name="com.braze.ios_session_timeout" value="5" />
    <preference name="com.braze.sdk_authentication_enabled" value="YES"/"NO" />
    <preference name="com.braze.display_foreground_push_notifications" value="YES"/"NO" />
    <preference name="com.braze.ios_disable_un_authorization_option_provisional" value="NO"/"YES" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" />
    <preference name="com.braze.ios_push_app_group" value="PUSH_APP_GROUP_ID" />
    <preference name="com.braze.ios_forward_universal_links" value="YES"/"NO" />
    <preference name="com.braze.ios_log_level" value="2" />
    <preference name="com.braze.ios_use_uuid_as_device_id" value="YES"/"NO" />
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_use_automatic_request_policy" value="YES"/"NO" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES"/"NO" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value="str_LOG_LEVEL_INTEGER" />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
    <preference name="com.braze.sdk_authentication_enabled" value="true"/"false" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="str_MINIMUM_INTERVAL_INTEGER" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false"/"true" />
    <preference name="com.braze.default_notification_channel_name" value="DEFAULT_NAME" />
    <preference name="com.braze.default_notification_channel_description" value="DEFAULT_DESCRIPTION" />
    <preference name="com.braze.does_push_story_dismiss_on_click" value="true"/"false" />
    <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true"/"false" />
    <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="FALLBACK_FIREBASE_MESSAGING_CLASSPATH" />
    <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true"/"false" />
    <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true"/"false" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true"/"false" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="DEEPLINK_BACKSTACK_ACTIVITY_CLASS_NAME" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true"/"false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Désactivation du suivi automatique des sessions (Android uniquement) {#disable-automatic-session-tracking}

Par défaut, le plug-in Android Cordova assure automatiquement le suivi des sessions. Pour désactiver le suivi automatique des sessions, ajoutez la préférence suivante à l'élément `platform` dans le fichier `config.xml` de votre projet :

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Pour recommencer à suivre les sessions, appelez `BrazePlugin.startSessionTracking()`. Gardez à l'esprit que seules les sessions démarrées après le prochain `Activity.onStart()` seront suivies.

## Configuration des canaux de notification pour les notifications heads-up (Android uniquement) {#configuring-notification-channels-for-heads-up-notifications-android-only}

Sur Android 8.0 (niveau d'API 26) et versions ultérieures, le comportement des notifications est contrôlé par les canaux de notification. Pour afficher des notifications heads-up — des alertes qui apparaissent brièvement en haut de l'écran lorsque l'utilisateur utilise son appareil — vous devez créer un canal de notification avec `NotificationManager.IMPORTANCE_HIGH` dans le code de votre application Android.

Bien que le SDK Cordova vous permette de définir le nom et la description du canal de notification par défaut via les préférences `config.xml` (`default_notification_channel_name` et `default_notification_channel_description`), le niveau d'importance doit être configuré de manière programmatique dans votre code Android natif.

### Exemple : Création d'un canal de notification de haute importance {#example-creating-a-high-importance-notification-channel}

Ajoutez le code suivant à la méthode `onCreate()` de la classe `Application` de votre application Android :

{% subtabs local %}
{% subtab Kotlin %}
```kotlin
import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Build

override fun onCreate() {
    super.onCreate()

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        val channelId = "high_priority_channel"
        val channelName = "High Priority Notifications"
        val importance = NotificationManager.IMPORTANCE_HIGH

        val channel = NotificationChannel(channelId, channelName, importance).apply {
            description = "Notifications that require immediate attention"
        }

        val notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        notificationManager.createNotificationChannel(channel)
    }
}
```
{% endsubtab %}

{% subtab Java %}
```java
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.os.Build;

@Override
public void onCreate() {
    super.onCreate();

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        String channelId = "high_priority_channel";
        String channelName = "High Priority Notifications";
        int importance = NotificationManager.IMPORTANCE_HIGH;

        NotificationChannel channel = new NotificationChannel(channelId, channelName, importance);
        channel.setDescription("Notifications that require immediate attention");

        NotificationManager notificationManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        notificationManager.createNotificationChannel(channel);
    }
}
```
{% endsubtab %}
{% endsubtabs %}

Après avoir créé le canal dans votre code Android, utilisez l'identifiant du canal lors de l'envoi de notifications push depuis le tableau de bord de Braze. Pour plus d'informations sur les canaux de notification, consultez [Canaux de notification Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels).