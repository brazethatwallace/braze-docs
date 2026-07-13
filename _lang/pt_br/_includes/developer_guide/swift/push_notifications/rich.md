{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Configurando notificações por push ricas {#setting-up-rich-push-notifications}

### Etapa 1: Criação de uma extensão de serviço {#step-1-creating-a-service-extension}

Para criar uma [extensão de serviço de notificação](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), navegue até **File > New > Target** no Xcode e selecione **Notification Service Extension**.

![Seletor de alvo do Xcode criando uma Notification Service Extension para rich push.]({% image_buster /assets/img_archive/ios10_se_at.png %}){: style="max-width:90%"}

Certifique-se de que **Embed In Application** esteja definido para incorporar a extensão em seu aplicativo.

### Etapa 2: Configuração da extensão do serviço de notificação {#step-2-setting-up-the-notification-service-extension}

Uma extensão de serviço de notificação é seu próprio binário, que é empacotado com seu app. Ela deve ser configurada no [Portal Apple Developer](https://developer.apple.com) com seu próprio ID de app e perfil de provisionamento.

O ID do pacote da extensão do serviço de notificação deve ser diferente do ID do pacote do alvo principal do seu app. Por exemplo, se o ID do pacote do seu app for `com.company.appname`, você poderá usar `com.company.appname.AppNameServiceExtension` para a extensão do serviço.

### Etapa 3: Adicionando um grupo de apps {#step-3-adding-an-app-group}

No Xcode, adicione a capacidade de Grupos de Apps no painel **Signing & Capabilities** ao seu alvo principal do app, bem como ao alvo da Extensão de Serviço de Notificação. Em seguida, clique no botão **+**. Use o ID do pacote do seu app para criar o grupo de apps. Por exemplo, se o ID do pacote do seu app for `com.company.appname`, você pode nomear seu grupo de apps `group.com.company.appname.xyz`.

{% alert important %}
Grupos de apps neste contexto referem-se à [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) da Apple e não ao seu ID de espaço de trabalho da Braze (anteriormente grupo de apps).
{% endalert %}

Você precisa de um grupo de apps compartilhado para que seu app principal e a Extensão de Serviço de Notificação possam acessar dados compartilhados. Se você não adicionar seu app a um grupo de apps, seu app pode falhar ao preencher certos campos da carga útil do push e não funcionará totalmente como esperado.

### Etapa 4: Integração de notificações por push ricas {#step-4-integrating-rich-push-notifications}

Para obter um guia passo a passo sobre a integração de notificações por push ricas com `BrazeNotificationService`, consulte nosso [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Para ver um exemplo, consulte o uso em [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) do nosso app Examples.

#### Adição do framework de rich push ao seu app {#adding-the-rich-push-framework-to-your-app}

{% tabs local %}
{% tab Swift Package Manager %}

Depois de seguir o [guia de integração do Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), adicione `BrazeNotificationService` à sua `Notification Service Extension` fazendo o seguinte:

1. No Xcode, em frameworks e bibliotecas, selecione o ícone <i class="fas fa-plus" title="Adicionar"></i> para adicionar um framework. <br><br>![O ícone de mais está localizado sob frameworks e bibliotecas no Xcode.]({% image_buster /assets/img_archive/rich_notification.png %})<br><br>

2. Selecione o framework "BrazeNotificationService". <br><br>![O framework "BrazeNotificationService" pode ser selecionado no modal que se abre.]({% image_buster /assets/img_archive/rich_notification2.png %})

{% endtab %}
{% tab CocoaPods %}

Adicione o seguinte ao seu Podfile:

```ruby
target 'YourAppTarget' do
  pod 'BrazeKit'
  pod 'BrazeUI'
  pod 'BrazeLocation'
end

target 'YourNotificationServiceExtensionTarget' do
  pod 'BrazeNotificationService'
end

# Only include the below if you want to also integrate Push Stories
target 'YourNotificationContentExtensionTarget' do
  pod 'BrazePushStory'
end
```

{% alert note %}
Para obter instruções sobre como implementar Push Stories, consulte a [documentação]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

Após atualizar o Podfile, navegue até o diretório do seu projeto de app Xcode no seu terminal e execute `pod install`.

{% endtab %}

{% tab Manual %}

Para adicionar `BrazeNotificationService.xcframework` à sua `Notification Service Extension`, consulte [Integração manual]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![Projeto Xcode com BrazeNotificationService.xcframework adicionado à extensão de serviço de notificação.]({% image_buster /assets/img/swift/rich_push/manual1.png %})

{% endtab %}
{% endtabs %}

#### Uso da sua própria UNNotificationServiceExtension {#using-your-own-unnotificationserviceextension}

Se você precisar usar sua própria UNNotificationServiceExtension, poderá chamar [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) no seu método `didReceive`.

```swift
import BrazeNotificationService
import UserNotifications

class NotificationService: UNNotificationServiceExtension {

  override func didReceive(
    _ request: UNNotificationRequest,
    withContentHandler contentHandler: @escaping (UNNotificationContent) -> Void
  ) {
    if brazeHandle(request: request, contentHandler: contentHandler) {
      return
    }

    // Custom handling here

    contentHandler(request.content)
  }
}
```

### Etapa 5: Configurando o grupo de apps na Braze {#step-5-configuring-the-app-group-in-braze}

Antes de inicializar a Braze, atribua o nome do seu grupo de apps à propriedade [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) da configuração da Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### Etapa 6: Criação de uma notificação Rich no seu dashboard {#step-6-creating-a-rich-notification-in-your-dashboard}

Sua equipe de marketing também pode criar notificações ricas a partir do dashboard. Crie uma notificação por push pelo criador de push e anexe uma imagem ou GIF, ou forneça uma URL que hospede uma imagem, GIF ou vídeo. Os ativos são baixados no recebimento das notificações por push, portanto, planeje-se para grandes picos síncronos de solicitações se estiver hospedando seu conteúdo.