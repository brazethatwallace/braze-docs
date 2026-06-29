---
nav_title: Mises à jour en direct pour Android
article_title: Mises à jour en direct pour le SDK Android de Braze
page_order: 0.1
description: "Découvrez comment configurer les mises à jour en direct pour le SDK Android de Braze."
platform:
  - Android
  - FireOS
hidden: true
---

# Mises à jour en direct pour Android {#live-updates-for-android}

> Découvrez comment utiliser les mises à jour en direct Android dans le SDK de Braze, également connues sous le nom de [Progress Centric Notifications](https://developer.android.com/about/versions/16/features/progress-centric-notifications). Ces notifications sont similaires aux [Live Activities pour le SDK Swift de Braze]({{site.baseurl}}/developer_guide/live_notifications/live_activities), vous permettant d'afficher des notifications interactives sur l'écran de verrouillage. Android 16 introduit les notifications centrées sur la progression pour aider les utilisateurs à suivre de façon fluide les parcours initiés par l'utilisateur, du début à la fin.

## Fonctionnement {#how-it-works}

Vous pouvez utiliser l'interface [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) pour personnaliser l'affichage des notifications push de Braze. En étendant `BrazeNotificationFactory`, Braze appellera la méthode `createNotification()` de votre fabrique avant que la notification ne soit affichée à l'utilisateur. Il transmettra ensuite un payload contenant des paires clé-valeur personnalisées envoyées via le tableau de bord de Braze ou la REST API.

## Afficher une mise à jour en direct {#displaying-a-live-update}

Dans cette section, vous collaborerez avec Superb Owl, l'animateur d'un nouveau jeu télévisé dans lequel des équipes de sauvetage d'animaux sauvages s'affrontent pour savoir qui peut sauver le plus grand nombre de hiboux. Ils cherchent à exploiter les mises à jour en direct dans leur application Android, afin d'afficher l'état d'un match en cours et de mettre à jour dynamiquement la notification en temps réel.

![Exemple de mise à jour en direct depuis Android]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

#{% multi_lang_include developer_guide/prerequisites/android.md %}

### Étape 1 : Créer une fabrique de notifications personnalisée {#step-1-create-a-custom-notification-factory}

Dans votre application, créez un nouveau fichier nommé `MyCustomNotificationFactory.kt` qui étend [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) pour gérer l'affichage des mises à jour en direct de Braze.

Dans l'exemple suivant, Superb Owl a créé une fabrique de notifications personnalisée pour afficher une mise à jour en direct pour les matchs en cours. À l'étape suivante, vous allez créer une nouvelle méthode appelée `getTeamInfo` pour mapper les données d'une équipe à l'activité.

```kotlin
class MyCustomNotificationFactory : IBrazeNotificationFactory {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        val notificationBuilder = populateNotificationBuilder(payload)
        val context = payload.context ?: return null

        if (notificationBuilder == null) {
            brazelog { "Notification could not be built. Returning null as created notification." }
            return null
        }
        notificationBuilder.setContentTitle("Android Live Updates").setContentText("Ongoing updates below")
        setProgressStyle(notificationBuilder, context)
        return notificationBuilder.build()
    }

    private fun setProgressStyle(notificationBuilder: NotificationCompat.Builder, context: Context) {
        val style = NotificationCompat.ProgressStyle()
            .setStyledByProgress(false)
            .setProgress(200)
            .setProgressTrackerIcon(IconCompat.createWithResource(context, R.drawable.notification_small_icon))
            .setProgressSegments(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Segment(1000).setColor(Color.GRAY),
                    NotificationCompat.ProgressStyle.Segment(200).setColor(Color.BLUE),
                )
            )
            .setProgressPoints(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Point(60).setColor(Color.RED),
                    NotificationCompat.ProgressStyle.Point(560).setColor(Color.GREEN)
                )
            )

        notificationBuilder.setStyle(style)
    }
}
```

### Étape 2 : Mapper les données personnalisées {#step-2-map-custom-data}

Dans `MyCustomNotificationFactory.kt`, créez une nouvelle méthode pour traiter les données lorsque des mises à jour en direct sont affichées.

Superb Owl a créé la méthode suivante pour mapper le nom et le logo de chaque équipe aux mises à jour en direct étendues :

```kotlin
class CustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        // Your existing code
        return super.createNotification(payload)
    }

    // Your new method
    private fun getTeamInfo(team: String?): Pair<String, Int> {
        return when (team) {
            "WBF" -> Pair("Wild Bird Fund", R.drawable.team_wbf)
            "OWL" -> Pair("Owl Rehab", R.drawable.team_owl)
            else  -> Pair("Unknown", R.drawable.notification_small_icon)
        }
    }
}
```

### Étape 3 : Définir la fabrique de notifications personnalisée {#step-3-set-the-custom-notification-factory}

Dans votre classe d'application, utilisez [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?) pour définir votre fabrique de notifications personnalisée.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Étape 4 : Envoyer l'activité {#step-4-send-the-activity}

Vous pouvez utiliser l'endpoint REST API [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) pour envoyer une notification push à l'appareil Android d'un utilisateur.

#### Exemple de commande curl {#example-curl-command}

Superb Owl a envoyé sa requête en utilisant la commande curl suivante :

```
curl -X POST "https://BRAZE_REST_ENDPOINT/messages/send" \
  -H "Authorization: Bearer {REST_API_KEY}" \
  -H "Content-Type: application/json" \
  --data '{
    "external_user_ids": ["USER_ID"],
    "messages": {
      "android_push": {
        "title": "WBF vs OWL",
        "alert": "2 to 4 1:33 Q4",
        "extra": {
          "live_update": "true",
          "team1": "WBF",
          "team2": "OWL",
          "score1": "2",
          "score2": "4",
          "time": "1:33",
          "quarter": "Q4"
        },
        "notification_id": "ASSIGNED_NOTIFICATION_ID"
      }
    }
  }'
```

{% alert tip %}
Bien que les commandes curl soient utiles pour les tests, nous recommandons de gérer cet appel dans votre backend, là où vous gérez déjà vos [Live Activities iOS]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?sdktab=swift).
{% endalert %}

#### Paramètres de la requête {#request-parameters}

| Clé | Description |
|------------------------------|------------|
| `REST_API_KEY` | Une clé REST API de Braze avec les autorisations `messages.send`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés API**. |
| `BRAZE_REST_ENDPOINT` | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics#endpoints). |
| `USER_ID` | L'ID de l'utilisateur auquel vous envoyez la notification. |
| `messages.android_push.title` | Le titre du message. Par défaut, il n'est pas utilisé pour les notifications en direct de la fabrique de notifications personnalisée, mais il peut servir de solution de repli. |
| `messages.android_push.alert` | Le corps du message. Par défaut, il n'est pas utilisé pour les notifications en direct de la fabrique de notifications personnalisée, mais il peut servir de solution de repli. |
| `messages.extra` | Paires clé-valeur que la fabrique de notifications personnalisée utilise pour les notifications en direct. Vous pouvez attribuer n'importe quelle chaîne de caractères à cette valeur&#8212;toutefois, dans l'exemple ci-dessus, `live_updates` est utilisé pour déterminer s'il s'agit d'une notification push par défaut ou en direct. |
| `ASSIGNED_NOTIFICATION_ID` | L'ID de notification que vous souhaitez attribuer à la notification en direct de l'utilisateur choisi. L'ID doit être unique pour ce jeu et doit être utilisé pour [mettre à jour la notification existante](#android_step-4-update-data-with-the-braze-rest-api) ultérieurement. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paramètres de la requête" }

### Étape 5 : Mettre à jour l'activité {#step-5-update-the-activity}

Pour mettre à jour la mise à jour en direct existante avec de nouvelles données, modifiez les paires clé-valeur pertinentes attribuées à `messages.extra`, puis utilisez le même `notification_id` et appelez à nouveau l'endpoint `/messages/send`.