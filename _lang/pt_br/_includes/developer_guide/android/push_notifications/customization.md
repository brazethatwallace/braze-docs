{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Usando um retorno de chamada para eventos de push {#push-callback}

A Braze fornece um retorno de chamada [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) para quando notificações por push são recebidas, abertas ou descartadas. Recomenda-se colocar este retorno de chamada no seu `Application.onCreate()` para não perder nenhum evento que ocorra enquanto seu aplicativo não estiver em execução.

{% alert note %}
Se anteriormente usava um Custom Broadcast Receiver para essa funcionalidade em seu aplicativo, você pode removê-lo com segurança em favor desta opção de integração.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Com os botões de ação de notificação, as intents `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` são acionadas quando os botões com ações `opens app` ou `deep link` são clicados. O tratamento de deep link e extras permanece o mesmo. Os botões com ações `close` não disparam as intents `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` e descartam a notificação automaticamente.
{% endalert %}

{% alert important %}
Crie seu listener de notificação por push em `Application.onCreate` para garantir que ele seja disparado depois que um usuário final tocar em uma notificação enquanto o app estiver em estado finalizado.
{% endalert %}

## Personalizando a exibição de notificações {#customization-display}

### Etapa 1: Crie sua fábrica de notificações personalizada {#step-1-create-your-custom-notification-factory}

Em alguns cenários, você pode querer personalizar as notificações por push de maneiras que seriam complicadas ou não estariam disponíveis no lado do servidor. Para que você tenha controle total sobre a exibição de notificações, adicionamos a capacidade de definir seu próprio [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) para criar objetos de notificação para serem exibidos pela Braze.

Se um `IBrazeNotificationFactory` personalizado for definido, a Braze chamará o método `createNotification()` da sua fábrica no recebimento do push antes que a notificação seja exibida ao usuário. A Braze transmitirá um `Bundle` contendo dados de push da Braze e outro `Bundle` contendo pares de chave-valor personalizados enviados por meio do dashboard ou das APIs de envio de mensagens:

A Braze passará um [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) contendo dados da notificação por push da Braze.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Você pode retornar `null` do seu método personalizado `createNotification()` para não mostrar a notificação, usar `BrazeNotificationFactory.getInstance().createNotification()` para obter nosso objeto padrão `notification` para esses dados e modificá-lo antes da exibição, ou gerar um objeto `notification` completamente separado para exibição.

{% alert note %}
Para obter a documentação sobre as chaves de dados push da Braze, consulte o [SDK do Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Etapa 2: Defina sua fábrica de notificações personalizada {#step-2-set-your-custom-notification-factory}

Para instruir a Braze a usar sua fábrica de notificações personalizada, use o método `setCustomBrazeNotificationFactory` para definir seu [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html):

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

O local recomendado para definir seu `IBrazeNotificationFactory` personalizado é no método do ciclo de vida do aplicativo `Application.onCreate()` (não na atividade). Isso permitirá que a fábrica de notificações seja definida corretamente sempre que o processo do seu app estiver ativo.

{% alert important %}
Criar sua própria notificação do zero é um caso de uso avançado e deve ser feito somente com testes completos e um profundo conhecimento da funcionalidade push da Braze. Por exemplo, é preciso garantir que a notificação registre as aberturas de push corretamente.
{% endalert %}

Para cancelar a configuração personalizada do [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) e retornar ao tratamento padrão da Braze para push, passe `null` para o configurador de fábrica de notificações personalizadas:

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Renderizando texto multicolorido {#rendering-multicolor-text}

Na versão 3.1.1 do SDK da Braze, HTML pode ser enviado a um dispositivo para renderizar texto multicolorido em notificações por push.

![Uma mensagem push do Android "Multicolor Push test message" em que as letras são de cores diferentes, em itálico e com uma cor de fundo.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Esse exemplo é renderizado com o seguinte HTML:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Tenha em mente que o Android limita quais elementos e tags HTML são válidos em suas notificações por push. Por exemplo, `marquee` não é permitido.

{% alert important %}
A renderização de texto multicolorido é específica do dispositivo e pode não ser exibida com base no dispositivo ou versão do Android.
{% endalert %}

Para renderizar texto multicolorido em uma notificação por push, você pode atualizar seu `braze.xml` ou `BrazeConfig`:

{% tabs local %}
{% tab braze.xml %}
Adicione o seguinte no seu `braze.xml`:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
Adicione o seguinte no seu [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration#runtime-configuration):

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Tags HTML suportadas {#supported-html-tags}

Atualmente, o Google não lista suas tags HTML suportadas para Android diretamente em sua documentação&#8212;essa informação só pode ser encontrada no [arquivo `Html.java` do repositório Git](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java) deles. Tenha isso em mente ao consultar a tabela a seguir, pois essa informação foi extraída deste arquivo e as tags HTML suportadas podem estar sujeitas a alterações.

<table aria-label="Tags HTML suportadas">
  <thead>
    <tr>
      <th>Categoria</th>
      <th>Tag HTML</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Estilização básica de texto</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Texto em negrito</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Texto em itálico</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Texto sublinhado</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Texto tachado</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Texto sobrescrito</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Texto subscrito</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Texto monoespaçado</td>
    </tr>
    <tr>
      <td rowspan="3">Tamanho/Fonte</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Alterações relativas no tamanho do texto</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Define a cor do primeiro plano</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (com CSS inline)</td>
      <td>Estilos inline (ex.: cor, fundo)</td>
    </tr>
    <tr>
      <td rowspan="4">Parágrafo &amp; Bloco</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Seções de nível de bloco</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Quebra de linha</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Bloco de citação</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Lista não ordenada com marcadores</td>
    </tr>
    <tr>
      <td>Títulos</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>Títulos (vários tamanhos)</td>
    </tr>
    <tr>
      <td rowspan="2">Links &amp; Imagens</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Link clicável</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Imagem inline</td>
    </tr>
    <tr>
      <td>Outros inline</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Sinônimos para itálico ou negrito</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tags HTML suportadas" }

## Renderização de imagens inline {#rendering-inline-images}

### Como funciona {#how-it-works}

Você pode exibir uma imagem maior dentro da sua notificação por push do Android usando push de imagem inline. Com esse design, os usuários não precisarão expandir manualmente o push para ampliar a imagem. Ao contrário das notificações por push normais do Android, as imagens de push inline têm uma proporção de 3:2.

![Prévia de notificação por push do Android mostrando a renderização de push com imagem inline.]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### Compatibilidade {#compatibility}

Embora você possa enviar imagens inline para qualquer dispositivo, dispositivos e SDKs que não atendem às versões mínimas exibirão uma imagem padrão. Para que as imagens inline sejam exibidas corretamente, tanto o SDK da Braze para Android v10.0.0+ quanto um dispositivo rodando Android M+ são necessários. O SDK também deve estar ativado para que a imagem seja renderizada.

{% alert note %}
Os dispositivos que executam o Android 12 serão renderizados de forma diferente devido a alterações nos estilos de notificação por push personalizados.
{% endalert %}

### Enviando um push de imagem inline {#sending-an-inline-image-push}

Ao criar uma mensagem push para Android, esse recurso está disponível no menu suspenso **Notification Type**.

![O editor de Campaign de push mostrando a localização do dropdown "Notification Type" próximo à prévia padrão do push.]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## Configurações {#settings}

Existem muitas configurações avançadas disponíveis para notificações por push do Android enviadas pelo dashboard da Braze. Este artigo descreve esses recursos e como usá-los com sucesso.

![Painel de configurações avançadas do criador de push Android da Braze.]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### ID da notificação {#notification-id}

Um **ID de notificação** é um identificador único para uma categoria de mensagem de sua escolha que informa o serviço de envio de mensagens a respeitar apenas a mensagem mais recente desse ID. Definir um ID de notificação permite que você envie apenas a mensagem mais recente e relevante, em vez de uma pilha de mensagens desatualizadas e irrelevantes.

### Prioridade de entrega do Firebase Messaging {#fcm-priority}

O campo [Prioridade de entrega do Firebase Messaging](https://firebase.google.com/docs/cloud-messaging/android/message-priority#setting-priority-for-messages) permite que você controle se um push é enviado com prioridade "normal" ou "alta" para o Firebase Cloud Messaging.

### Time to live (TTL) {#ttl}

O campo **TTL** permite que você defina um tempo personalizado para armazenar mensagens com o serviço de push. Os valores padrão para TTL são quatro semanas para FCM e 31 dias para ADM.

### Texto resumido {#summary-text}

O texto resumido permite que você defina texto adicional na visualização expandida da notificação. Ele também serve como legenda para notificações com imagens.

![Uma mensagem do Android com o título "This is the title for the notification." e texto resumido "This is the summary text for the notification."]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

O texto resumido será exibido sob o corpo da mensagem na visualização expandida.

![Uma mensagem do Android com o título "This is the title for the notification." e texto resumido "This is the summary text for the notification."]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Para notificações por push que incluem imagens, o texto da mensagem será mostrado na visualização recolhida, enquanto o texto resumido será exibido como a legenda da imagem quando a notificação for expandida.

### URIs personalizados {#custom-uri}

O recurso **Custom URI** permite que você especifique um URL da web ou um recurso do Android para navegar quando a notificação for clicada. Se nenhum URI personalizado for especificado, clicar na notificação leva os usuários para o seu app. Você pode usar o URI personalizado para fazer deep link dentro do seu app e direcionar os usuários para recursos que existem fora do seu app. Isso pode ser especificado por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) ou do nosso dashboard em **Advanced Settings** no criador de push, conforme ilustrado:

![A configuração avançada de deep linking no criador de push da Braze.]({% image_buster /assets/img_archive/deep_link.png %})

### Prioridade de exibição de notificação {#notification-priority}

{% alert important %}
A configuração de prioridade de exibição de notificação não é mais usada em dispositivos com Android O ou mais recente. Para dispositivos mais novos, defina a prioridade por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

O nível de prioridade de uma notificação por push afeta a forma como a notificação é exibida na bandeja de notificações em relação a outras notificações. Também pode afetar a velocidade e a maneira de entrega, pois mensagens normais e de baixa prioridade podem ser enviadas com uma latência ligeiramente maior ou agrupadas para preservar a vida útil da bateria, enquanto mensagens de alta prioridade são sempre enviadas imediatamente.

No Android O, a prioridade de notificação se tornou uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir a prioridade de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar seus sons de notificação. Para dispositivos que executam versões do Android anteriores ao O, especificar um nível de prioridade para notificações do Android é possível por meio do dashboard da Braze e da API de envio de mensagens.

Para enviar mensagens para toda a sua base de usuários com uma prioridade específica, recomendamos que você especifique indiretamente a prioridade por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance) (para direcionar dispositivos O+) *e* envie a prioridade individual a partir do dashboard (para direcionar dispositivos &#60;O).

Os níveis de prioridade que você pode definir em notificações por push do Android ou Fire OS são:

| Prioridade | Descrição/Uso pretendido | Valor de `priority` (para mensagens de API) |
|----------|--------------------------|-------------------------------------|
| Máx.      | Mensagens urgentes ou críticas em termos de tempo | `2` |
| Alta     | Comunicação importante, como uma nova mensagem de um amigo | `1` |
| Padrão  | A maioria das notificações — use se sua mensagem não se enquadrar explicitamente em nenhum dos outros tipos de prioridade | `0` |
| Baixa      | Informações que você deseja que os usuários saibam, mas que não exigem ação imediata | `-1` |
| Mín.      | Informações contextuais ou de segundo plano | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prioridade de exibição de notificação" }

Para saber mais, consulte a documentação de [notificação do Android](http://developer.android.com/design/patterns/notifications.html) do Google.

### Sons {#sounds}

No Android O, os sons de notificação se tornaram uma propriedade dos canais de notificação. Você precisará trabalhar com seu desenvolvedor para definir o som de um canal durante sua configuração e, em seguida, usar o dashboard para selecionar o canal adequado ao enviar suas notificações.

Para dispositivos executando versões do Android anteriores ao O, a Braze permite que você defina o som de uma mensagem push individual por meio do criador do dashboard. Você pode fazer isso especificando um recurso de som local no dispositivo (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`). Especificar "default" neste campo reproduzirá o som de notificação padrão no dispositivo. Isso pode ser especificado por meio da [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging) ou do dashboard em **Advanced Settings** no criador de push.

![A configuração avançada de som no criador de push da Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Digite o URI completo do recurso de som (por exemplo, `android.resource://com.mycompany.myapp/raw/mysound`) no prompt do dashboard.

Para enviar mensagens para toda a sua base de usuários com um som específico, recomendamos que você especifique indiretamente o som por meio da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels) (para direcionar dispositivos O+) *e* envie o som individual a partir do dashboard (para direcionar dispositivos &#60;O).