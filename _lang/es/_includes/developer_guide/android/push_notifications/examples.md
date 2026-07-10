{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Diseño de notificación personalizado {#custom-notification-layout}

Las notificaciones de Braze se envían como [mensajes de datos](https://firebase.google.com/docs/cloud-messaging/concept-options), lo que significa que tu aplicación siempre tendrá la oportunidad de responder y realizar un comportamiento acorde, incluso en segundo plano (a diferencia de los mensajes de notificación, que pueden ser gestionados automáticamente por el sistema cuando tu aplicación está en segundo plano). Como tal, tu aplicación tendrá la oportunidad de personalizar la experiencia, por ejemplo, mostrando elementos de interfaz de usuario personalizados dentro de la notificación entregada en la bandeja de notificaciones. Aunque implementar el push de esta forma puede resultar desconocido para algunos, una de nuestras características más conocidas en Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories), ¡son un excelente ejemplo del uso de componentes de vista personalizados para crear una experiencia atractiva!

{% alert important %}
Android impone algunas limitaciones a los componentes que pueden utilizarse para implementar vistas de notificación personalizadas. Los diseños de las vistas de notificación _solo_ deben contener objetos View compatibles con el marco [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews).
{% endalert %}

Puedes utilizar la interfaz [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para personalizar cómo se muestran las notificaciones push de Braze. Al extender `BrazeNotificationFactory`, Braze llamará al método `createNotification()` de tu fábrica antes de que la notificación se muestre al usuario. A continuación, pasará una carga útil que contiene pares clave-valor personalizados enviados a través del panel de Braze o la REST API.

En esta sección, te asociarás con Superb Owl, el presentador de un nuevo programa de juegos en el que equipos de rescate de animales salvajes compiten para ver quién salva más búhos. Quieren aprovechar las notificaciones con actualización en vivo en su aplicación Android, para poder mostrar el estado de un partido en curso y realizar actualizaciones dinámicas de la notificación en tiempo real.

![La actualización en vivo que Superb Owl quiere mostrar, con un partido en curso entre "Wild Bird Fund" y "Owl Rescue". Estamos en el último cuarto y el marcador es 2-4, con OWL a la cabeza.]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

### Paso 1: Añadir un diseño personalizado {#step-1-add-a-custom-layout}

Puedes añadir uno o varios diseños personalizados de notificación RemoteView a tu proyecto. Son útiles para manejar cómo se muestran las notificaciones cuando se contraen o expanden. Tu estructura de directorios debe ser similar a la siguiente:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

En cada archivo XML, crea un diseño personalizado. Superb Owl creó los siguientes diseños para sus RemoteView colapsados y expandidos:

{% tabs local %}
{% tab  Example: Collapsed layout %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/notification_title"
        style="@style/TextAppearance.Compat.Notification.Title"
        android:layout_width="wrap_content"
        android:layout_height="0dp"
        android:layout_weight="1" />
</LinearLayout>
```
{% endtab %}

{% tab Example: Expanded layout %}
{% details Mostrar el código de ejemplo %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"

        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team1logo"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:layout_gravity="center"
            android:src="@drawable/team_default1"/>

        <TextView
            android:id="@+id/team1name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1.6"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/score"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="2-4"
            android:textColor="#555555"
            android:textAlignment="center"
            android:textSize="32sp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/timeInfo"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>


    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team2logo"
            android:layout_gravity="center"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:src="@drawable/team_default2"/>

        <TextView
            android:id="@+id/team2name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>
</LinearLayout>
```
{% enddetails %}
{% endtab %}
{% endtabs %}

### Paso 2: Crear una fábrica de notificaciones personalizada {#step-2-create-a-custom-notification-factory}

En tu aplicación, crea un nuevo archivo llamado `MyCustomNotificationFactory.kt` que extienda [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para gestionar cómo se muestran los diseños personalizados de RemoteView.

En el siguiente ejemplo, Superb Owl creó una fábrica de notificaciones personalizada para mostrar un diseño RemoteView para los partidos en curso. En el [siguiente paso](#android_step-3-map-custom-data), crearán un nuevo método llamado `getTeamInfo` para mapear los datos de un equipo a la actividad.

{% details Mostrar el código de ejemplo %}
```kotlin
import android.app.Notification
import android.widget.RemoteViews
import androidx.core.app.NotificationCompat
import com.braze.models.push.BrazeNotificationPayload
import com.braze.push.BrazeNotificationFactory
import com.braze.push.BrazeNotificationUtils.getOrCreateNotificationChannelId
import com.braze.support.BrazeLogger.brazelog

class MyCustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        if (payload.extras.containsKey("live_update")) {
            val kvp = payload.extras
            val notificationChannelId = getOrCreateNotificationChannelId(payload)
            val context = payload.context

            if (context == null) {
                brazelog { "BrazeNotificationPayload has null context. Not creating notification" }
                return null
            }

            val team1 = kvp["team1"]
            val team2 = kvp["team2"]
            val score1 = kvp["score1"]
            val score2 = kvp["score2"]
            val time = kvp["time"]
            val quarter = kvp["quarter"]

            // Superb Owl will define the 'getTeamInfo' method in the next step.
            val (team1name, team1icon) = getTeamInfo(team1)
            val (team2name, team2icon) = getTeamInfo(team2)

            // Get the layouts to use in the custom notification.
            val notificationLayoutCollapsed = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_collapsed)
            val notificationLayoutExpanded = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_expanded)

            // Very simple notification for the small layout
            notificationLayoutCollapsed.setTextViewText(
                R.id.notification_title,
                "$team1 $score1 - $score2 $team2\n$time $quarter"
            )

            notificationLayoutExpanded.setTextViewText(R.id.score, "$score1 - $score2")
            notificationLayoutExpanded.setTextViewText(R.id.team1name, team1name)
            notificationLayoutExpanded.setTextViewText(R.id.team2name, team2name)
            notificationLayoutExpanded.setTextViewText(R.id.timeInfo, "$time - $quarter")
            notificationLayoutExpanded.setImageViewResource(R.id.team1logo, team1icon)
            notificationLayoutExpanded.setImageViewResource(R.id.team2logo, team2icon)

            val customNotification = NotificationCompat.Builder(context, notificationChannelId)
                .setSmallIcon(R.drawable.notification_small_icon)
                .setStyle(NotificationCompat.DecoratedCustomViewStyle())
                .setCustomContentView(notificationLayout)
                .setCustomBigContentView(notificationLayoutExpanded)
                .build()
            return customNotification
        } else {
            // Use the BrazeNotificationFactory for all other notifications
            return super.createNotification(payload)
        }
    }
}
```
{% enddetails %}

### Paso 3: Mapear datos personalizados {#step-3-map-custom-data}

En `MyCustomNotificationFactory.kt`, crea un nuevo método para manejar los datos cuando se muestren las actualizaciones en vivo.

Superb Owl creó el siguiente método para mapear el nombre y el logotipo de cada equipo a las actualizaciones en vivo expandidas:

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

### Paso 4: Configurar la fábrica de notificaciones personalizada {#step-4-set-the-custom-notification-factory}

En tu clase de aplicación, utiliza [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?) para configurar tu fábrica de notificaciones personalizada.

```kotlin
import com.braze.Braze

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Paso 5: Enviar la actividad {#step-5-send-the-activity}

Puedes utilizar el endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) de la REST API para enviar una notificación push al dispositivo Android de un usuario.

#### Ejemplo de comando curl {#example-curl-command}

Superb Owl envió su solicitud utilizando el siguiente comando curl:

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
Aunque los comandos curl son útiles para las pruebas, te recomendamos que gestiones esta llamada en tu backend, donde ya estás gestionando tus [actividades en vivo de iOS]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift).
{% endalert %}

#### Parámetros de la solicitud {#request-parameters}

| Clave | Descripción |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REST_API_KEY`                | Una clave de API REST de Braze con permisos `messages.send`. <br><br> Se puede crear en el panel de Braze desde **Configuración** > **Claves de API**.                                                                                                     |
| `BRAZE_REST_ENDPOINT`         | La URL de tu endpoint REST. Tu endpoint dependerá de la [URL de Braze de tu instancia]({{site.baseurl}}/api/basics#endpoints).                                                                                                                  |
| `USER_ID`                     | El ID del usuario al que envías la notificación.                                                                                                                                                                                          |
| `messages.android_push.title` | El título del mensaje. De forma predeterminada, no se utiliza para las notificaciones en vivo de la fábrica de notificaciones personalizada, pero puede utilizarse como alternativa.                                                                                                    |
| `messages.android_push.alert` | El cuerpo del mensaje. De forma predeterminada, no se utiliza para las notificaciones en vivo de la fábrica de notificaciones personalizada, pero puede utilizarse como alternativa.                                                                                                     |
| `messages.extra`              | Pares clave-valor que la fábrica de notificaciones personalizada utiliza para las notificaciones en vivo. Puedes asignar cualquier cadena a este valor&#8212;sin embargo, en este ejemplo, se utiliza `live_updates` para determinar si se trata de una notificación push predeterminada o en vivo.  |
| `ASSIGNED_NOTIFICATION_ID`    | El ID de notificación que quieres asignar a la notificación en vivo del usuario elegido. El ID debe ser único para este juego, y debe utilizarse para [actualizar su notificación existente](#android_step-4-update-data-with-the-braze-rest-api) posteriormente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parámetros de la solicitud" }

### Paso 6: Actualizar la actividad {#step-6-update-the-activity}

Para actualizar la notificación RemoteView existente con nuevos datos, modifica los pares clave-valor correspondientes asignados a `messages.extra`, luego utiliza el mismo `notification_id` y vuelve a llamar al endpoint `/messages/send`.

## Notificaciones push personalizadas {#personalized-push-notifications}

Las notificaciones push pueden mostrar información específica del usuario dentro de una jerarquía de vistas personalizada. En el siguiente ejemplo, se utiliza un desencadenador de API para enviar una notificación push personalizada a un usuario para que pueda comprobar su progreso actual tras completar una tarea específica en la aplicación.

![Ejemplo de push personalizado en el panel]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

Para configurar un push personalizado en el panel, registra la categoría específica que quieres que se muestre y, a continuación, establece los atributos de usuario relevantes que te gustaría mostrar utilizando Liquid.

![Ejemplo de configuración de push personalizado en el panel]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}