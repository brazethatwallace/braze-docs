---
nav_title: Actualizaciones en vivo para Android
article_title: Actualizaciones en vivo para el SDK or kit de desarrollo de software de Braze para Android
page_order: 0.3
description: "Aprende a utilizar las actualizaciones en vivo de Android en el SDK or kit de desarrollo de software de Braze."
platform:
  - Android
hidden: true
---

# Actualizaciones en vivo para Android {#live-updates-for-android}

> Aprende a utilizar las actualizaciones en vivo de Android en el SDK or kit de desarrollo de software de Braze, también conocidas como [notificaciones centradas en el progreso](https://developer.android.com/about/versions/16/features/progress-centric-notifications). Estas notificaciones son similares a las [actividades en vivo del SDK or kit de desarrollo de software Swift de Braze]({{site.baseurl}}/developer_guide/live_notifications/live_activities), lo que te permite mostrar notificaciones interactivas en la pantalla de bloqueo. Android 16 introduce notificaciones centradas en el progreso para ayudar a los usuarios a realizar fácilmente un seguimiento de los recorridos iniciados por el usuario, de principio a fin.

## Cómo funciona {#how-it-works}

Puedes usar la interfaz [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para personalizar cómo se muestran las notificaciones push de Braze. Al extender `BrazeNotificationFactory`, Braze llamará al método `createNotification()` de tu fábrica antes de que la notificación se muestre al usuario. A continuación, pasará una carga útil que contiene pares clave-valor personalizados enviados a través del panel de Braze o la REST or transferencia de estado representacional API.

## Mostrar una Live Update {#displaying-a-live-update}

En esta sección, colaborarás con Superb Owl, el anfitrión de un nuevo programa de juegos donde equipos de rescate de vida silvestre compiten para ver quién puede salvar la mayor cantidad de búhos. Buscan aprovechar las Live Updates en su aplicación Android, para poder mostrar el estado de un partido en curso y realizar actualizaciones dinámicas a la notificación en tiempo real.

![Un ejemplo de Live Update de Android]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

{% multi_lang_include developer_guide/prerequisites/android.md %}

### Paso 1: Crear una fábrica de notificaciones personalizada {#step-1-create-a-custom-notification-factory}

En tu aplicación, crea un nuevo archivo llamado `MyCustomNotificationFactory.kt` que extienda [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para manejar cómo se muestran las Braze Live Updates.

En el siguiente ejemplo, Superb Owl creó una fábrica de notificaciones personalizada para mostrar una Live Update para partidos en curso. En el siguiente paso, crearás un nuevo método llamado `getTeamInfo` para mapear los datos de un equipo a la actividad.

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

### Paso 2: Mapear datos personalizados {#step-2-map-custom-data}

En `MyCustomNotificationFactory.kt`, crea un nuevo método para manejar los datos cuando se muestran las Live Updates.

Superb Owl creó el siguiente método para mapear el nombre y el logo de cada equipo a las Live Updates expandidas:

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

### Paso 3: Establecer la fábrica de notificaciones personalizada {#step-3-set-the-custom-notification-factory}

En la clase de tu aplicación, usa [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?) para establecer tu fábrica de notificaciones personalizada.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Paso 4: Enviar la actividad {#step-4-send-the-activity}

Puedes usar el endpoint de REST or transferencia de estado representacional API [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) para enviar una notificación push al dispositivo Android de un usuario.

#### Ejemplo de comando curl {#example-curl-command}

Superb Owl envió su solicitud usando el siguiente comando curl:

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
Aunque los comandos curl son útiles para pruebas, recomendamos manejar esta llamada en tu backend donde ya estés gestionando tus [iOS Live Activities]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift).
{% endalert %}

#### Parámetros de la solicitud {#request-parameters}

| Clave | Descripción |
|------------------------------|------------|
| `REST_API_KEY` | Una clave de API REST or transferencia de estado representacional de Braze con permisos `messages.send`. <br><br> Puede crearse en el panel de Braze desde **Configuración** > **Claves de API**. |
| `BRAZE_REST_ENDPOINT` | La URL de tu endpoint REST or transferencia de estado representacional. Tu endpoint dependerá de la [URL de Braze para tu instancia]({{site.baseurl}}/api/basics#endpoints). |
| `USER_ID` | El ID del usuario al que le estás enviando la notificación. |
| `messages.android_push.title` | El título del mensaje. De forma predeterminada, no se usa para las notificaciones en vivo de la fábrica de notificaciones personalizada, pero puede usarse como alternativa. |
| `messages.android_push.alert` | El cuerpo del mensaje. De forma predeterminada, no se usa para las notificaciones en vivo de la fábrica de notificaciones personalizada, pero puede usarse como alternativa. |
| `messages.extra` | Pares clave-valor que la fábrica de notificaciones personalizada utiliza para las notificaciones en vivo. Puedes asignar cualquier cadena a este valor; sin embargo, en el [ejemplo de comando curl](#example-curl-command), `live_updates` se usa para determinar si es una notificación push predeterminada o en vivo. |
| `ASSIGNED_NOTIFICATION_ID` | El ID de notificación que deseas asignar a la notificación en vivo del usuario elegido. El ID debe ser único para este juego y debe usarse para [actualizar su notificación existente](#android_step-4-update-data-with-the-braze-rest-api) posteriormente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parámetros de la solicitud" }

### Paso 5: Actualizar la actividad {#step-5-update-the-activity}

Para actualizar la Live Update existente con nuevos datos, modifica los pares clave-valor relevantes asignados a `messages.extra`, luego usa el mismo `notification_id` y llama al endpoint `/messages/send` de nuevo.