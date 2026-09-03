{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Configuração de notificações por push ricas {#setting-up-rich-push-notifications}

### Etapa 1: Criar uma extensão de serviço {#step-1-creating-a-service-extension}

Para criar uma [extensão de serviço de notificação](https://developer.apple.com/reference/usernotifications/unnotificationserviceextension), navegue até **File > New > Target** no Xcode e selecione **Notification Service Extension**.

![Seletor de destino do Xcode criando uma extensão de serviço de notificação para push rico.]({% image_buster /assets/img_archive/ios10_se_at.png %}){: width="1442" height="1030" style="max-width:90%"}

Certifique-se de que **Embed In Application** esteja configurado para incorporar a extensão em seu app.

### Etapa 2: Configurar a extensão de serviço de notificação {#step-2-setting-up-the-notification-service-extension}

Uma extensão de serviço de notificação é um binário separado que é empacotado com seu app. Ela deve ser configurada no [Apple Developer Portal](https://developer.apple.com) com seu próprio ID de app e perfil de provisionamento.

O bundle ID da extensão de serviço de notificação deve ser diferente do bundle ID do alvo principal do seu app. Por exemplo, se o bundle ID do seu app for `com.company.appname`, você pode usar `com.company.appname.AppNameServiceExtension` para sua extensão de serviço.

### Etapa 3: Adicionar um App Group {#step-3-adding-an-app-group}

No Xcode, adicione a capacidade App Groups no painel **Signing & Capabilities** tanto ao alvo principal do app quanto ao alvo da extensão de serviço de notificação. Em seguida, clique no botão **+**. Use o bundle ID do seu app para criar o grupo de apps. Por exemplo, se o bundle ID do seu app for `com.company.appname`, você pode nomear seu grupo de apps como `group.com.company.appname.xyz`.

{% alert important %}
App Groups neste contexto se refere ao [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) da Apple e não ao ID do seu espaço de trabalho da Braze (anteriormente grupo de apps).
{% endalert %}

Você precisa de um App Group compartilhado para que seu app principal e a extensão de serviço de notificação possam acessar dados compartilhados. Se você não adicionar seu app a um grupo de apps, seu app pode falhar ao preencher determinados campos da carga útil do push e não funcionará completamente como esperado.

### Etapa 4: Integrar notificações por push ricas {#step-4-integrating-rich-push-notifications}

Para obter um guia passo a passo sobre como integrar notificações por push ricas com `BrazeNotificationService`, consulte nosso [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

Para ver um exemplo, consulte o uso em [`NotificationService`](https://github.com/braze-inc/braze-swift-sdk/blob/main/Examples/Swift/Sources/PushNotificationsServiceExtension/NotificationService.swift) do nosso app de exemplos.

#### Adicionar o framework de push rico ao seu app {#adding-the-rich-push-framework-to-your-app}

{% tabs local %}
{% tab Swift Package Manager %}

Após seguir o [guia de integração do Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), adicione `BrazeNotificationService` à sua `Notification Service Extension` fazendo o seguinte:

1. No Xcode, em frameworks e bibliotecas, selecione o ícone de adição <i class="fas fa-plus" aria-label="Adicionar framework"></i> para adicionar um framework. <br><br>![O ícone de adição está localizado em frameworks e bibliotecas no Xcode.]({% image_buster /assets/img_archive/rich_notification.png %}){: width="1930" height="446"}<br><br>

2. Selecione o framework "BrazeNotificationService". <br><br>![O framework BrazeNotificationService pode ser selecionado no modal que é aberto.]({% image_buster /assets/img_archive/rich_notification2.png %}){: width="2248" height="1102"}

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
Para instruções sobre como implementar Push Stories, consulte a [documentação]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/?tab=swift%20package%20manager).
{% endalert %}

Após atualizar o Podfile, navegue até o diretório do seu projeto Xcode no terminal e execute `pod install`.

{% endtab %}

{% tab Manual %}

Para adicionar `BrazeNotificationService.xcframework` à sua `Notification Service Extension`, consulte [Integração manual]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration?tab=manual/).

![Projeto Xcode com BrazeNotificationService.xcframework adicionado à extensão de serviço de notificação.]({% image_buster /assets/img/swift/rich_push/manual1.png %}){: width="1069" height="170"}

{% endtab %}
{% endtabs %}

#### Usar sua própria UNNotificationServiceExtension {#using-your-own-unnotificationserviceextension}

Se você precisar usar sua própria UNNotificationServiceExtension, em vez disso pode chamar [`brazeHandle`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazenotificationservice/brazehandle(request:contenthandler:)) no seu método `didReceive`.

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

### Etapa 5: Configurar o App Group na Braze {#step-5-configuring-the-app-group-in-braze}

Antes de inicializar a Braze, atribua o nome do seu grupo de apps à propriedade [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) da configuração da Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```

### Etapa 6: Criar uma notificação rica no dashboard {#step-6-creating-a-rich-notification-in-your-dashboard}

Sua equipe de marketing também pode criar notificações ricas pelo dashboard. Crie uma notificação por push pelo criador de push e anexe uma imagem ou GIF, ou forneça uma URL que hospede uma imagem, GIF ou vídeo. Os ativos são baixados no recebimento das notificações por push, então planeje-se para grandes picos sincronizados de requisições caso esteja hospedando seu próprio conteúdo.