---
nav_title: Atualizações ao vivo para Android
article_title: Atualizações ao vivo para o SDK Braze do Android
page_order: 0.3
description: "Saiba como usar as atualizações ao vivo do Android no SDK da Braze."
platform:
  - Android
hidden: true
---

# Atualizações ao vivo para Android {#live-updates-for-android}

> Saiba como usar as atualizações ao vivo do Android no SDK da Braze, também conhecidas como [notificações centradas em progresso](https://developer.android.com/about/versions/16/features/progress-centric-notifications). Essas notificações são semelhantes às [Live Activities para o SDK Braze do Swift]({{site.baseurl}}/developer_guide/live_notifications/live_activities), permitindo que você exiba notificações interativas na tela de bloqueio. O Android 16 introduz notificações centradas em progresso para ajudar os usuários a acompanhar jornadas iniciadas pelo usuário, do início ao fim.

## Como funciona {#how-it-works}

Você pode usar a interface [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para personalizar como as notificações por push da Braze são exibidas. Ao estender `BrazeNotificationFactory`, a Braze chamará o método `createNotification()` da sua factory antes que a notificação seja exibida ao usuário. Em seguida, será passada uma carga útil contendo pares chave-valor personalizados enviados pelo dashboard da Braze ou pela REST API.

## Exibindo uma Live Update {#displaying-a-live-update}

Nesta seção, você vai fazer uma parceria com o Superb Owl, o apresentador de um novo programa de TV onde equipes de resgate de animais selvagens competem para ver quem consegue salvar mais corujas. Eles querem aproveitar as Live Updates no app Android para exibir o status de uma partida em andamento e fazer atualizações dinâmicas na notificação em tempo real.

![Um exemplo de Live Update no Android]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

{% multi_lang_include developer_guide/prerequisites/android.md %}

### Etapa 1: Criar uma fábrica de notificações personalizada {#step-1-create-a-custom-notification-factory}

No seu aplicativo, crie um novo arquivo chamado `MyCustomNotificationFactory.kt` que estenda [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para controlar como as Live Updates da Braze são exibidas.

No exemplo a seguir, o Superb Owl criou uma fábrica de notificações personalizada para exibir uma Live Update de partidas em andamento. Na próxima etapa, você criará um novo método chamado `getTeamInfo` para mapear os dados de uma equipe à atividade.

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

### Etapa 2: Mapear dados personalizados {#step-2-map-custom-data}

Em `MyCustomNotificationFactory.kt`, crie um novo método para tratar os dados quando as Live Updates forem exibidas.

O Superb Owl criou o seguinte método para mapear o nome e o logotipo de cada equipe às Live Updates expandidas:

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

### Etapa 3: Definir a fábrica de notificações personalizada {#step-3-set-the-custom-notification-factory}

Na classe do seu aplicativo, use [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?) para definir sua fábrica de notificações personalizada.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Etapa 4: Enviar a atividade {#step-4-send-the-activity}

Você pode usar o endpoint da REST API [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) para enviar uma notificação por push para o dispositivo Android de um usuário.

#### Exemplo de comando curl {#example-curl-command}

O Superb Owl enviou sua solicitação usando o seguinte comando curl:

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
Embora comandos curl sejam úteis para testes, recomendamos tratar essa chamada no seu backend, onde você já está lidando com suas [iOS Live Activities]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift).
{% endalert %}

#### Parâmetros da solicitação {#request-parameters}

| Chave | Descrição |
|------------------------------|------------|
| `REST_API_KEY` | Uma chave da API REST da Braze com permissões `messages.send`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| `BRAZE_REST_ENDPOINT` | A URL do seu endpoint REST. Seu endpoint dependerá da [URL da Braze para a sua instância]({{site.baseurl}}/api/basics#endpoints). |
| `USER_ID` | O ID do usuário para quem você está enviando a notificação. |
| `messages.android_push.title` | O título da mensagem. Por padrão, ele não é usado para as notificações ao vivo da fábrica de notificações personalizada, mas pode ser usado como fallback. |
| `messages.android_push.alert` | O corpo da mensagem. Por padrão, ele não é usado para as notificações ao vivo da fábrica de notificações personalizada, mas pode ser usado como fallback. |
| `messages.extra` | Pares de chave-valor que a fábrica de notificações personalizada usa para notificações ao vivo. Você pode atribuir qualquer string a esse valor&#8212;porém, no [exemplo de comando curl](#example-curl-command), `live_updates` é usado para determinar se é uma notificação por push padrão ou ao vivo. |
| `ASSIGNED_NOTIFICATION_ID` | O ID de notificação que você quer atribuir à notificação ao vivo do usuário escolhido. O ID deve ser único para esta partida e deve ser usado para [atualizar a notificação existente](#android_step-4-update-data-with-the-braze-rest-api) posteriormente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parâmetros da solicitação" }

### Etapa 5: Atualizar a atividade {#step-5-update-the-activity}

Para atualizar a Live Update existente com novos dados, modifique os pares de chave-valor relevantes atribuídos a `messages.extra` e, em seguida, use o mesmo `notification_id` e chame o endpoint `/messages/send` novamente.