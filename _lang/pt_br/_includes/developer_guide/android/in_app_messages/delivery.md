{% multi_lang_include developer_guide/prerequisites/android.md %}

## Gatilhos de mensagem {#message-triggers}

### Tipos de disparo {#trigger-types}

As mensagens no app são acionadas automaticamente quando o SDK registra um dos seguintes tipos de evento personalizado: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` e `Push Click`. Observe que os gatilhos `Specific Purchase` e `Custom Event` também contêm filtros de propriedade robustos.

{% alert note %}
As mensagens no app não podem ser acionadas pela API ou por eventos da API&#8212;apenas por eventos personalizados registrados pelo SDK. Para saber mais sobre registro, consulte [Registro de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Semântica de entrega {#delivery-semantics}

Todas as mensagens no app elegíveis são entregues ao dispositivo do usuário no início da sessão. Quando entregues, o SDK faz o pré-carregamento dos ativos para que estejam disponíveis no momento do acionamento, minimizando a latência de exibição. Se o evento de gatilho tiver mais de uma mensagem no app elegível, apenas a mensagem com a maior prioridade será entregue.

Para saber mais sobre a semântica de início de sessão do SDK, consulte [Ciclo de vida da sessão]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android).

### Limite de taxa {#rate-limit}

Por padrão, o SDK limita o disparo de mensagens no app a uma vez a cada 30 segundos, garantindo uma experiência de qualidade para o usuário.

Para apps em produção, não defina esse valor abaixo de 10 segundos, para que os usuários não sejam sobrecarregados com mensagens no app consecutivas. Para testes e fluxos de apps de exemplo, 5 segundos é uma configuração comum.

Você pode definir esse intervalo como `0` para testes. No entanto, um intervalo de `0` segundos não força a exibição de várias mensagens no app ao mesmo tempo. Se uma mensagem ainda estiver visível, a próxima não será exibida até que a mensagem atual seja dispensada.

Para substituir esse valor, defina `com_braze_trigger_action_minimum_time_interval_seconds` no seu `braze.xml` via:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Pares de chave-valor {#key-value-pairs}

Quando você cria uma campaign na Braze, pode definir pares de chave-valor como `extras`, que o objeto de mensagem no app pode usar para enviar dados ao seu app. Por exemplo:

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
Para saber mais, consulte o [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}

## Desativando gatilhos automáticos {#disabling-automatic-triggers}

Para evitar que mensagens no app sejam acionadas automaticamente:

1. Certifique-se de usar o inicializador de integração automática, que está ativado por padrão a partir da versão `2.2.0`.
2. Defina o padrão da operação de mensagem no app como `DISCARD` adicionando a seguinte linha ao seu arquivo `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## Disparando mensagens manualmente {#manually-triggering-messages}

Por padrão, as mensagens no app são acionadas automaticamente quando o SDK registra um evento personalizado. No entanto, você pode disparar uma mensagem manualmente usando os métodos a seguir.

### Usando um evento do lado do servidor {#using-a-server-side-event}

Para disparar uma mensagem no app usando um evento enviado pelo servidor, envie uma notificação por push silenciosa para o dispositivo. Isso permite que um retorno de chamada de push personalizado registre um evento baseado no SDK, que então disparará a mensagem no app voltada para o usuário.

#### Etapa 1: Crie um retorno de chamada push para receber o push silencioso {#step-1-create-a-push-callback-to-receive-the-silent-push}

Registre [seu retorno de chamada de evento push personalizado]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback) para escutar uma notificação por push silenciosa específica.

No exemplo a seguir, dois eventos serão registrados para que a mensagem no app seja entregue: um pelo servidor e outro de dentro do seu retorno de chamada push personalizado. Para garantir que o mesmo evento não seja duplicado, o evento registrado a partir do retorno de chamada push deve seguir uma convenção de nomenclatura genérica, por exemplo, "evento de gatilho de mensagem no app", e não o mesmo nome do evento enviado pelo servidor. Se isso não for feito, a segmentação e os dados de usuários podem ser afetados por eventos duplicados registrados para uma única ação do usuário.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endtab %}
{% endtabs %}

#### Etapa 2: Crie uma campaign de push {#step-2-create-a-push-campaign}

Crie uma [campaign de push silenciosa]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) disparada pelo evento enviado pelo servidor.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

A campaign de push deve incluir extras de pares de chave-valor que indiquem que essa campaign de push é enviada para registrar um evento personalizado do SDK. Esse evento será usado para disparar a mensagem no app.

![Dois conjuntos de pares de chave-valor: IS_SERVER_EVENT definido como "true" e CAMPAIGN_NAME definido como "nome da campanha de exemplo".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

O código de exemplo do retorno de chamada push anterior reconhece os pares de chave-valor e registra o evento personalizado apropriado do SDK.

Se você quiser incluir propriedades de evento para anexar ao seu evento "gatilho de mensagem no app", passe-as nos pares de chave-valor da carga útil do push. Neste exemplo, o nome da campaign da mensagem no app subsequente foi incluído. Seu retorno de chamada de push personalizado pode então passar o valor como parâmetro da propriedade do evento ao registrar o evento personalizado.

#### Etapa 3: Crie uma campaign de mensagem no app {#step-3-create-an-in-app-message-campaign}

Crie sua campaign de mensagem no app visível para o usuário no dashboard da Braze. Essa campaign deve ter uma entrega baseada em ação e ser disparada a partir do evento personalizado registrado dentro do seu retorno de chamada push personalizado.

No exemplo a seguir, a mensagem no app específica a ser disparada foi configurada enviando a propriedade do evento como parte do push silencioso inicial.

![Uma campaign de entrega baseada em ação onde uma mensagem no app será disparada quando "campaign_name" for igual a "exemplo de nome da campaign IAM".]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Se um evento enviado pelo servidor for registrado enquanto o app não estiver em primeiro plano, o evento será registrado, mas a mensagem no app não será exibida. Se você quiser que o evento seja postergado até que o aplicativo esteja em primeiro plano, uma verificação deve ser incluída no seu receptor de push personalizado para dispensar ou postergar o evento até que o app entre em primeiro plano.

### Exibindo uma mensagem pré-definida {#displaying-a-pre-defined-message}

Para exibir manualmente uma mensagem no app pré-definida, use o seguinte método:

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

### Exibindo uma mensagem em tempo real {#displaying-a-message-in-real-time}

Você também pode criar e exibir mensagens no app locais em tempo real, usando as mesmas opções de personalização disponíveis no dashboard. Para isso:

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
Não exiba mensagens no app quando o teclado virtual estiver sendo exibido na tela, pois a renderização é indefinida nessa circunstância.
{% endalert %}