{% multi_lang_include developer_guide/prerequisites/android.md %}

## Configurando notificações por push {#setting-up-push-notifications}

Os telefones mais novos fabricados pela [Huawei](https://huaweimobileservices.com/) vêm equipados com o Huawei Mobile Services (HMS), um serviço usado para enviar push em vez do Firebase Cloud Messaging (FCM) do Google.

### Etapa 1: Registre-se para uma conta de desenvolvedor da Huawei {#step-1-register-for-a-huawei-developer-account}

Antes de começar, você precisará se registrar e configurar uma [conta de desenvolvedor da Huawei](https://developer.huawei.com/consumer/en/console). Em sua conta da Huawei, acesse **My Projects > Project Settings > App Information** e anote os valores de `App ID` e `App secret`.

![Página de informações do app no console de desenvolvedor da Huawei mostrando o App ID e o App secret.]({% image_buster /assets/img/huawei/huawei-credentials.png %})

### Etapa 2: Crie um novo app da Huawei no dashboard da Braze {#step-2-create-a-new-huawei-app-in-the-braze-dashboard}

No dashboard da Braze, acesse **Configurações do app**, listado na navegação de **Configurações**.

Clique em **+ Adicionar app**, forneça um nome (como My Huawei App) e selecione `Android` como a plataforma.

![Diálogo de adição de app na Braze criando um app Android Huawei.]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

Depois que seu novo app da Braze tiver sido criado, localize as configurações de notificação por push e selecione `Huawei` como o provedor de push. Em seguida, forneça seu `Huawei Client Secret` e `Huawei App ID`.

![Configurações do provedor de push Huawei na Braze com os campos Huawei App ID e Client Secret.]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

### Etapa 3: Integre o SDK or kit de desenvolvimento de software de envio de mensagens da Huawei em seu app {#step-3-integrate-the-huawei-messaging-sdk-into-your-app}

A Huawei forneceu um [codelab de integração Android](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) detalhando a integração do Huawei Messaging Service em seu app. Siga essas etapas para começar.

Depois de concluir o codelab, você precisará criar um [Huawei Message Service](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) personalizado para obter tokens por push e encaminhar mensagens para o SDK or kit de desenvolvimento de software da Braze.

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

Depois de adicionar seu serviço push personalizado, adicione o seguinte ao seu `AndroidManifest.xml`:

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### Etapa 4: Gerenciar notificações em primeiro plano {#step-4-handle-foreground-notifications}

Por padrão, quando uma notificação por push chega enquanto seu app está em primeiro plano, a Huawei a exibe automaticamente. Para que a Braze processe a carga útil da notificação por push (para rastreamento de análise de dados, gerenciamento de deep link e processamento personalizado), direcione os dados de push recebidos para a Braze dentro do seu método `HmsMessageService.onMessageReceived`.

Quando você chama `BrazeHuaweiPushHandler.handleHmsRemoteMessageData`, a Braze determina se a carga útil é uma notificação por push da Braze e, se for, cria e exibe a notificação. Para saber mais, veja [Gerenciando notificações em primeiro plano]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications) na documentação de notificações por push do Android.

Para um exemplo completo, veja a [referência do manipulador da Huawei](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-huawei-push-handler/index.html) na documentação do SDK or kit de desenvolvimento de software Android da Braze.

### Etapa 5: Teste suas notificações por push (opcional) {#step-5-test-your-push-notifications-optional}

Neste ponto, você criou um novo app Huawei para Android no dashboard da Braze, configurou-o com suas credenciais de desenvolvedor da Huawei e integrou os SDKs da Braze e da Huawei ao seu app.

Em seguida, podemos testar a integração testando uma nova campanha de push na Braze.

#### Etapa 5.1: Crie uma nova campanha de notificação por push {#step-51-create-a-new-push-notification-campaign}

Na página **Campaigns**, crie uma nova campanha e escolha **Push Notification** como o tipo de mensagem.

Depois de dar um nome à sua campanha, escolha **Android Push** como a plataforma de push.

![O criador de campanha exibindo as plataformas de push disponíveis.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

Em seguida, crie sua campanha de push com um título e uma mensagem.

#### Etapa 5.2: Envie um push de teste {#step-52-send-a-test-push}

Na guia **Teste**, digite o ID do usuário, que foi definido no app usando o [método `changeUser(USER_ID_STRING)`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#assigning-a-user-id), e clique em **Enviar teste** para enviar um push de teste.

![A guia de teste no criador de campanha mostra que você pode enviar uma mensagem de teste para si mesmo fornecendo seu ID de usuário e inserindo-o no campo "Adicionar usuários individuais".]({% image_buster /assets/img/huawei/huawei-test-send.png %})

Nesse momento, você deverá receber uma notificação por push de teste da Braze em seu dispositivo Huawei (HMS).

#### Etapa 5.3: Configure a segmentação da Huawei (opcional) {#step-53-set-up-huawei-segmentation-optional}

Como o app da Huawei no dashboard da Braze foi criado com base na plataforma de push do Android, você tem a flexibilidade de enviar push para todos os usuários do Android (Firebase Cloud Messaging e Huawei Mobile Services) ou pode optar por segmentar o público da campanha para apps específicos.

Para enviar push apenas para apps da Huawei, [crie um novo Segment or segmento]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) e selecione seu app da Huawei na seção **Apps**.

![Filtro de app do Segment na Braze selecionando o app Huawei para direcionamento de push.]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

Claro, se quiser enviar o mesmo push para todos os provedores de push do Android, você pode optar por não especificar o app, o que enviará para todos os apps Android configurados no espaço de trabalho atual.