{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift), o que inclui a implementação do framework `UNNotification`.

A seguinte versão mínima do SDK é necessária para receber Push Stories:

{% sdk_min_versions swift:5.0.0 %}

## Configurando Push Stories {#setting-up-push-stories}

### Etapa 1: Adicionando o alvo da extensão de conteúdo de notificação {#notification-content-extension}

No seu projeto de app, acesse o menu **File > New > Target** e adicione um novo alvo `Notification Content Extension` e ative-o.

![Seletor de alvo do Xcode criando uma Notification Content Extension para Push Stories.]({% image_buster /assets/img/swift/push_story/add_content_extension.png %})

O Xcode deve gerar um novo alvo e criar arquivos automaticamente para você, incluindo:

- `NotificationViewController.swift`
- `MainInterface.storyboard`

### Etapa 2: Ativar capacidades {#enable-capabilities}

No Xcode, adicione a capacidade Background Modes usando o painel **Signing & Capabilities** ao alvo principal do app. Selecione as caixas de seleção **Background fetch** e **Remote notifications**.

![Painel de capacidades do Xcode com Background Modes ativado.]({% image_buster /assets/img/swift/push_story/enable_background_mode.png %})

#### Adicionando um grupo de app {#adding-an-app-group}

Além disso, no painel **Signing & Capabilities** no Xcode, adicione a capacidade App Groups ao alvo principal do seu app, bem como aos alvos da extensão de conteúdo de notificação. Em seguida, clique no botão **+**. Use o ID do pacote do seu app para criar o grupo de app. Por exemplo, se o ID do pacote do seu app for `com.company.appname`, você pode nomear seu grupo de app `group.com.company.appname.xyz`.

{% alert important %}
Grupos de app neste contexto referem-se à [App Groups Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) da Apple e não ao seu ID de espaço de trabalho da Braze (anteriormente grupo de app).
{% endalert %}

Se você não adicionar seu app a um grupo de app, seu app pode falhar em preencher certos campos da carga útil do push e não funcionará totalmente como esperado.

### Etapa 3: Adicionando o framework de Push Story ao seu app

{% tabs local %}
{% tab Swift Package Manager %}

Depois de seguir o [guia de integração do Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sdk_integration/?tab=swift%20package%20manager/), adicione `BrazePushStory` ao seu `Notification Content Extension`:

![No Xcode, em frameworks e bibliotecas, selecione o ícone "+" para adicionar um framework.]({% image_buster /assets/img/swift/push_story/spm1.png %})

![Seleção de produto de pacote do Xcode adicionando BrazePushStory ao alvo da extensão de conteúdo de notificação.]({% image_buster /assets/img/swift/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Adicione a seguinte linha ao seu Podfile:

```ruby
target 'YourAppTarget' do
pod 'BrazeKit'
pod 'BrazeUI'
pod 'BrazeLocation'
end

target 'YourNotificationContentExtensionTarget' do
pod 'BrazePushStory'
end

# Only include the below if you want to also integrate Rich Push
target 'YourNotificationServiceExtensionTarget' do
pod 'BrazeNotificationService'
end
```

{% alert note %}
Para obter instruções sobre como implementar Rich Push, consulte [Notificações Rich]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/?tab=swift%20package%20manager).
{% endalert %}

Após atualizar o Podfile, navegue até o diretório do seu projeto de app Xcode no terminal e execute `pod install`.

{% endtab %}
{% tab Manual %}

Baixe o último `BrazePushStory.zip` da [página de lançamentos do GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), extraia-o e adicione o `BrazePushStory.xcframework` à `Notification Content Extension` do seu projeto.

![Configurações de framework do Xcode mostrando BrazePushStory.xcframework adicionado com Do Not Embed selecionado.]({% image_buster /assets/img/swift/push_story/manual1.png %})

{% alert important %}
Certifique-se de que **Do Not Embed** esteja selecionado para **BrazePushStory.xcframework** na coluna **Embed**.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 4: Atualizando seu controlador de visualização de notificações

Em `NotificationViewController.swift`, adicione a seguinte linha para importar os arquivos de cabeçalho:

```swift
import BrazePushStory
```

Em seguida, substitua a implementação padrão herdando [`BrazePushStory.NotificationViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/):

```swift
class NotificationViewController: BrazePushStory.NotificationViewController {}
```

#### Tratamento personalizado de eventos de story por push {#custom-handling-push-story-events}

Se você quiser implementar sua própria lógica personalizada para lidar com eventos de notificação de story por push, herde `BrazePushStory.NotificationViewController` como mostrado no exemplo anterior e substitua os métodos [`didReceive`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazepushstory/notificationviewcontroller/didreceive(_:)) no exemplo a seguir.

```swift
import BrazePushStory
import UserNotifications
import UserNotificationsUI

class NotificationViewController: BrazePushStory.NotificationViewController {
  override func didReceive(_ notification: UNNotification) {
    super.didReceive(notification)

    // Custom handling logic
  }

  override func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    super.didReceive(response, completionHandler: completion)

    // Custom handling logic
  }
}
```

### Etapa 5: Configurando o plist da extensão de conteúdo de notificação

Abra o arquivo `Info.plist` da `Notification Content Extension`, depois adicione e altere as seguintes chaves em `NSExtension \ NSExtensionAttributes`:

| Chave                                            | Tipo     | Valor                  |
|--------------------------------------------------|----------|------------------------|
| `UNNotificationExtensionCategory`                | String   | `ab_cat_push_story_v2` |
| `UNNotificationExtensionDefaultContentHidden`    | Booleano | `YES`                  |
| `UNNotificationExtensionInitialContentSizeRatio` | Número   | `0.6`                  |
| `UNNotificationExtensionUserInteractionEnabled`  | Booleano | `YES`                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 5: Configurando o plist da extensão de conteúdo de notificação" }

Além disso, adicione o seguinte dicionário `Braze` de nível superior ao mesmo arquivo `Info.plist`, substituindo `REPLACE_WITH_APPGROUP` pelo grupo de app que você criou na [Etapa 2](#enable-capabilities):

| Chave            | Tipo   | Valor                   |
|------------------|--------|-------------------------|
| `Braze.AppGroup` | String | `REPLACE_WITH_APPGROUP` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 5: Configurando o plist da extensão de conteúdo de notificação" }

Seu arquivo `Info.plist` deve corresponder à seguinte imagem:

![Info.plist da extensão de conteúdo de notificação com as chaves de Push Story da Braze e configurações de grupo de app.]({% image_buster /assets/img/swift/push_story/notificationcontentextension_plist.png %})

### Etapa 6: Atualizando a integração da Braze no seu app principal {#update-braze}

Antes de inicializar a Braze, atribua o nome do seu grupo de app à propriedade [`push.appGroup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/push-swift.class/appgroup) da configuração da Braze.

```swift
let configuration = Braze.Configuration(apiKey: "<YOUR-BRAZE-API-KEY>",
                                        endpoint: "<YOUR-BRAZE-ENDPOINT>")
configuration.push.appGroup = "REPLACE_WITH_APPGROUP"
let braze = Braze(configuration: configuration)
```
