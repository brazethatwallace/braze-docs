{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Layout de notificação personalizado {#custom-notification-layout}

As notificações da Braze são enviadas como [mensagens de dados](https://firebase.google.com/docs/cloud-messaging/concept-options), o que significa que seu aplicativo sempre terá a chance de responder e executar o comportamento adequado, mesmo em segundo plano (diferentemente das mensagens de notificação, que podem ser tratadas automaticamente pelo sistema quando seu app está em segundo plano). Dessa forma, seu aplicativo terá a chance de personalizar a experiência, por exemplo, exibindo elementos personalizados de interface dentro da notificação entregue na bandeja de notificações. Embora implementar push dessa maneira possa não ser familiar para alguns, um de nossos recursos mais conhecidos na Braze, o [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories), é um excelente exemplo do uso de componentes de visualização personalizados para criar uma experiência envolvente!

{% alert important %}
O Android impõe algumas limitações quanto aos componentes que podem ser usados para implementar visualizações de notificação personalizadas. Os layouts de visualização de notificação devem conter _apenas_ objetos de visualização compatíveis com o framework [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews).
{% endalert %}

Você pode usar a interface [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para personalizar como as notificações por push da Braze são exibidas. Ao estender `BrazeNotificationFactory`, a Braze chamará o método `createNotification()` da sua fábrica antes que a notificação seja exibida ao usuário. Em seguida, será passada uma carga útil contendo pares de chave-valor personalizados enviados pelo dashboard da Braze ou pela REST API.

Nesta seção, você fará parceria com a Superb Owl, a apresentadora de um novo game show em que equipes de resgate de animais selvagens competem para ver quem consegue salvar mais corujas. Eles querem aproveitar as notificações de atualização ao vivo em seu app Android, para que possam exibir o status de uma partida em andamento e fazer atualizações dinâmicas na notificação em tempo real.

![A atualização ao vivo que a Superb Owl quer mostrar exibe uma partida em andamento entre "Wild Bird Fund" e "Owl Rescue". No momento, estamos no quarto período e o placar está em 2 a 4, com a OWL na liderança.]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

### Etapa 1: Adicionar um layout personalizado {#step-1-add-a-custom-layout}

Você pode adicionar um ou mais layouts RemoteView de notificação personalizados ao seu projeto. Eles são úteis para controlar como as notificações são exibidas quando recolhidas ou expandidas. Sua estrutura de diretórios deve ser semelhante à seguinte:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

Em cada arquivo XML, crie um layout personalizado. A Superb Owl criou os seguintes layouts para seus layouts RemoteView recolhidos e expandidos:

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
{% details Mostrar o código de exemplo %}
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

### Etapa 2: Criar uma fábrica de notificações personalizada {#step-2-create-a-custom-notification-factory}

Em seu aplicativo, crie um novo arquivo chamado `MyCustomNotificationFactory.kt` que estende [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para controlar como os layouts personalizados do RemoteView são exibidos.

No exemplo a seguir, a Superb Owl criou uma fábrica de notificações personalizada para exibir um layout RemoteView para partidas em andamento. Na [próxima etapa](#android_step-3-map-custom-data), eles criarão um novo método chamado `getTeamInfo` para mapear os dados de uma equipe para a atividade.

{% details Mostrar o código de exemplo %}
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

### Etapa 3: Mapear dados personalizados {#step-3-map-custom-data}

Em `MyCustomNotificationFactory.kt`, crie um novo método para tratar os dados quando as atualizações ao vivo forem exibidas.

A Superb Owl criou o seguinte método para mapear o nome e o logotipo de cada equipe para as atualizações ao vivo expandidas:

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

### Etapa 4: Definir a fábrica de notificações personalizada {#step-4-set-the-custom-notification-factory}

Em sua classe de aplicativo, use [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?) para definir sua fábrica de notificações personalizada.

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

### Etapa 5: Enviar a atividade {#step-5-send-the-activity}

Você pode usar o endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) da REST API para enviar uma notificação por push para o dispositivo Android de um usuário.

#### Exemplo de comando curl {#example-curl-command}

A Superb Owl enviou sua solicitação usando o seguinte comando curl:

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
Embora os comandos curl sejam úteis para testes, recomendamos lidar com essa chamada no seu backend, onde você já está lidando com as [iOS Live Activities]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift).
{% endalert %}

#### Parâmetros de solicitação {#request-parameters}

| Chave | Descrição |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REST_API_KEY`                | Uma chave da API REST da Braze com permissões `messages.send`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**.                                                                                                     |
| `BRAZE_REST_ENDPOINT`         | Sua URL de endpoint REST. Seu endpoint dependerá da [URL da Braze para sua instância]({{site.baseurl}}/api/basics#endpoints).                                                                                                                  |
| `USER_ID`                     | O ID do usuário para o qual você está enviando a notificação.                                                                                                                                                                                          |
| `messages.android_push.title` | O título da mensagem. Por padrão, isso não é usado para as notificações ao vivo da fábrica de notificações personalizada, mas pode ser usado como fallback.                                                                                                    |
| `messages.android_push.alert` | O corpo da mensagem. Por padrão, isso não é usado para as notificações ao vivo da fábrica de notificações personalizada, mas pode ser usado como fallback.                                                                                                     |
| `messages.extra`              | Pares de chave-valor que a fábrica de notificações personalizada usa para notificações ao vivo. Você pode atribuir qualquer string a esse valor&#8212;no entanto, neste exemplo, `live_updates` é usado para determinar se é uma notificação por push padrão ou ao vivo.  |
| `ASSIGNED_NOTIFICATION_ID`    | O ID de notificação que você deseja atribuir à notificação ao vivo do usuário escolhido. O ID deve ser exclusivo para esse jogo e deve ser usado para [atualizar a notificação existente](#android_step-4-update-data-with-the-braze-rest-api) posteriormente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parâmetros de solicitação" }

### Etapa 6: Atualizar a atividade {#step-6-update-the-activity}

Para atualizar a notificação existente do RemoteView com novos dados, modifique os pares de chave-valor relevantes atribuídos a `messages.extra` e, em seguida, use o mesmo `notification_id` e chame novamente o endpoint `/messages/send`.

## Notificações por push personalizadas {#personalized-push-notifications}

As notificações por push podem exibir informações específicas do usuário dentro de uma hierarquia de visualização personalizada. No exemplo a seguir, um disparo de API é usado para enviar uma notificação por push personalizada a um usuário para que ele possa verificar seu progresso atual depois de concluir uma tarefa específica no app.

![Exemplo de push personalizado no dashboard]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

Para configurar um push personalizado no dashboard, registre a categoria específica que deseja exibir e, em seguida, defina quaisquer atributos de usuário relevantes que gostaria de exibir usando Liquid.

![Exemplo de configuração de push personalizado no dashboard]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}