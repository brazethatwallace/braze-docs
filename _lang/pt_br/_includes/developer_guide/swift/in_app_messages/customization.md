{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configurando o delegate de UI (obrigatório) {#setting-up-the-ui-delegate-required}

Para personalizar a apresentação de mensagens no app e reagir a vários eventos do ciclo de vida, você precisará configurar o [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate). Esse é um protocolo delegate usado para receber e processar cargas úteis de mensagens no app disparadas, receber eventos do ciclo de vida de exibição e controlar o tempo de exibição. Para usar o `BrazeInAppMessageUIDelegate`, você deve:
- Usar a implementação padrão do [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) como seu `inAppMessagePresenter`.
- Incluir a biblioteca `BrazeUI` no seu projeto.

### Etapa 1: Implemente o protocolo `BrazeInAppMessageUIDelegate` {#step-1-implement-the-brazeinappmessageuidelegate-protocol}

Primeiro, implemente o protocolo `BrazeInAppMessageUIDelegate` e quaisquer métodos correspondentes que desejar. No exemplo a seguir, esse protocolo é implementado na classe `AppDelegate` do aplicativo.

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### Etapa 2: Atribua o objeto `delegate` {#step-2-assign-the-delegate-object}

Atribua o objeto `delegate` na instância do `BrazeInAppMessageUI` antes de atribuir essa UI de mensagem no app como seu `inAppMessagePresenter`.

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
Nem todos os métodos do delegate estão disponíveis em Objective-C devido à incompatibilidade de seus parâmetros com o runtime da linguagem.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
Para uma implementação passo a passo do delegate de UI de mensagem no app, consulte este [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
{% endalert %}

## Comportamento ao clicar {#on-click-behavior}

Cada objeto `Braze.InAppMessage` contém um [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction) correspondente, que define o comportamento ao clicar.

### Tipos de ação de clique {#click-action-types}

A propriedade `clickAction` do seu `Braze.InAppMessage` tem como padrão `.none`, mas pode ser definida com um dos seguintes valores:

| `ClickAction` | Comportamento ao clicar |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Abre a URL fornecida em um navegador externo. Se `useWebView` estiver definido como `true`, ela será aberta em uma web view. |
| `.none` | A mensagem será dispensada quando clicada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tipos de ação de clique" }

{% alert important %}
Para mensagens no app que contêm botões, o `clickAction` da mensagem também será incluído na carga útil final se a ação de clique for adicionada antes do texto do botão.
{% endalert %}

### Personalizar o comportamento ao clicar {#customizing-on-click-behavior}

Para personalizar esse comportamento, você pode modificar a propriedade `clickAction` consultando o exemplo a seguir:

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

O método `inAppMessage(_:prepareWith:)` não está disponível em Objective-C.

{% endtab %}
{% endtabs %}

### Lidar com o comportamento personalizado {#handling-the-custom-behavior}

O seguinte método delegado [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) é chamado quando um usuário clica em uma mensagem no app. Esse retorno de chamada é disparado para cliques iniciados pelo usuário em botões de mensagens no app e botões de mensagens no app em HTML (links), e um ID de botão é fornecido como parâmetro opcional para essas interações. Esse retorno de chamada não é invocado para cliques programáticos disparados por `brazeBridge.logClick()`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

Esse método retorna um valor booleano para indicar se a Braze deve continuar executando a ação de clique.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }

    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Deslizar para dispensar mensagens slideup {#swiping-to-dismiss-slideup-messages}

Por padrão, mensagens no app do tipo slideup podem ser dispensadas com um gesto de deslizar. A direção do deslize depende da posição do slideup:

- **Deslizar para a esquerda ou direita:** Dispensa o slideup independentemente de sua posição.
- **Slideup a partir da parte inferior:** Deslizar de cima para baixo dispensa a mensagem. Deslizar de baixo para cima não a dispensa.
- **Slideup a partir da parte superior:** Deslizar de baixo para cima dispensa a mensagem. Deslizar de cima para baixo não a dispensa.

Esse comportamento de deslizar é incorporado ao `BrazeInAppMessageUI` padrão [`SlideupView`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview) e se aplica apenas a mensagens no app do tipo slideup. Mensagens no app do tipo modal e tela cheia não suportam dispensar por deslize. Para personalizar ainda mais a visualização do slideup, incluindo o comportamento de deslize, você pode modificar os [`SlideupView.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview/attributes-swift.struct) ou fornecer uma visualização personalizada por meio de subclassing.

{% alert note %}
Tocar fora de uma mensagem slideup não a dispensa. Para mensagens no app do tipo modal ou tela cheia, você pode ativar a dispensa ao tocar fora usando o atributo `dismissOnBackgroundTap` descrito na seção a seguir.
{% endalert %}

## Personalização do fechamento de modais {#customizing-modal-dismissals}

Para ativar o fechamento ao tocar fora, você pode modificar a propriedade `dismissOnBackgroundTap` na struct `Attributes` do tipo de mensagem no app que deseja personalizar.

Por exemplo, se quiser ativar esse recurso para mensagens no app de imagem modal, configure o seguinte:

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

A personalização por meio de `Attributes` não está disponível em Objective-C.

{% endtab %}
{% endtabs %}

O valor padrão é `false`. Isso determina se a mensagem modal no app será fechada quando o usuário tocar fora da mensagem no app.

| `DismissModalOnOutsideTap` | Descrição |
|----------|-------------|
| `true`         | Mensagens modais no app serão fechadas ao tocar fora.     |
| `false`        | Padrão, mensagens modais no app não serão fechadas ao tocar fora. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalização do fechamento de modais" }

Para mais detalhes sobre personalização de mensagens no app, consulte este [artigo](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).

## Personalizando a orientação da mensagem {#customizing-message-orientation}

Você pode personalizar a orientação das suas mensagens no app. É possível definir uma nova orientação padrão para todas as mensagens ou definir uma orientação personalizada para uma única mensagem.

{% tabs local %}
{% tab all messages %}
Para escolher uma orientação padrão para todas as mensagens no app, use o método [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) para definir a propriedade `preferredOrientation` no `PresentationContext`.

Por exemplo, para definir retrato como a orientação padrão:

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab single message %}
Para definir a orientação de uma única mensagem, modifique a propriedade `orientation` de `Braze.InAppMessage`:

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Depois que a mensagem no app é exibida, qualquer mudança na orientação do dispositivo enquanto a mensagem ainda estiver sendo exibida fará com que ela rotacione junto com o dispositivo (desde que a orientação seja suportada pela configuração de `orientation` da mensagem).

A orientação do dispositivo também precisa ser suportada pela propriedade `orientation` da mensagem no app para que a mensagem seja exibida. Além disso, a configuração `preferredOrientation` só será respeitada se estiver incluída nas orientações de interface suportadas pelo seu aplicativo, na seção **Deployment Info** das configurações do seu target no Xcode.

![Orientações suportadas no Xcode.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %}){: width="2038" height="590"}

{% alert note %}
A orientação é aplicada apenas para a apresentação da mensagem. Depois que o dispositivo muda de orientação, a visualização da mensagem adota uma das orientações que ela suporta. Em dispositivos menores (iPhones, iPod Touch), definir uma orientação paisagem para uma mensagem no app modal ou em tela cheia pode resultar em conteúdo truncado.
{% endalert %}

## Personalizando o tempo de exibição {#customizing-display-timing}

Você pode controlar se uma mensagem no app disponível será exibida em determinados pontos da experiência do usuário. Se houver situações em que você não deseja que a mensagem no app apareça, como durante um jogo em tela cheia ou em uma tela de carregamento, você pode postergar ou descartar mensagens no app pendentes. Para controlar o tempo de exibição da mensagem no app, use o [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` para definir a propriedade `BrazeInAppMessageUI.DisplayChoice`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

Configure `BrazeInAppMessageUI.DisplayChoice` para retornar um dos seguintes valores:

| Opção de exibição                   | Comportamento                                                                                                               |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | A mensagem será exibida imediatamente. Este é o valor padrão.                                                               |
| `.reenqueue`                        | A mensagem não será exibida e será colocada de volta no topo da pilha.                                                      |
| `.later`                            | A mensagem não será exibida e será colocada de volta no topo da pilha. (Obsoleto, use `.reenqueue`)                         |
| `.discard`                          | A mensagem será descartada e não será exibida.                                                                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Personalizando o tempo de exibição" }

{% alert tip %}
Para ver um exemplo de `InAppMessageUI`, confira nosso [repositório Swift do SDK da Braze](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) e o de [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI).
{% endalert %}

## Ocultando a barra de status {#hiding-the-status-bar}

Para mensagens no app `Full`, `FullImage` e `HTML`, o SDK oculta a barra de status por padrão. Para outros tipos de mensagens no app, a barra de status permanece inalterada. Para configurar esse comportamento, use o [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)` para definir a propriedade `statusBarHideBehavior` no `PresentationContext`. Esse campo aceita um dos seguintes valores:

| Comportamento de ocultação da barra de status | Descrição                                                                             |
| ---------------------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                                        | A visualização da mensagem decide o estado de ocultação da barra de status.           |
| `.hidden`                                      | Sempre ocultar a barra de status.                                                     |
| `.visible`                                     | Sempre exibir a barra de status.                                                      |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ocultando a barra de status" }

## Desativando o modo escuro {#disabling-dark-mode}

Para evitar que mensagens no app adotem o estilo do modo escuro quando o dispositivo do usuário tem o modo escuro ativado, implemente o [método delegado](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) `inAppMessage(_:prepareWith:)`. O `PresentationContext` passado ao método contém uma referência ao objeto `InAppMessage` a ser apresentado. Cada `InAppMessage` possui uma propriedade `themes` contendo um tema de modo `dark` e `light`. Se você definir a propriedade `themes.dark` como `nil`, a Braze apresentará automaticamente a mensagem no app usando o tema claro.

Os tipos de mensagem no app que possuem botões têm um objeto `themes` adicional em sua propriedade `buttons`. Para evitar que os botões adotem o estilo do modo escuro, você pode usar [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d) para criar um novo array de botões com o tema `light` e sem o tema `dark`.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup

    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal

    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage

    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full

    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage

    default:
      break
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## Personalizando o prompt de avaliação da App Store {#customizing-the-app-store-review-prompt}

Você pode usar mensagens no app em uma Campaign para pedir aos usuários uma avaliação na App Store.

{% alert note %}
Como este exemplo de prompt substitui o comportamento padrão da Braze, não é possível rastrear impressões automaticamente se ele for implementado. Você precisa [registrar suas próprias análises de dados]({{site.baseurl}}/developer_guide/analytics).
{% endalert %}

### Etapa 1: Definir o delegate de mensagens no app {#step-1-set-the-in-app-message-delegate}

Primeiro, defina o [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization#swift_setting-up-the-ui-delegate-required) no seu app.

### Etapa 2: Desativar a mensagem padrão de avaliação da App Store {#step-2-disable-the-default-app-store-review-message}

Em seguida, implemente o [método delegate](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` para desativar a mensagem padrão de avaliação da App Store.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### Etapa 3: Criar um deep link {#step-3-create-a-deep-link}

No seu manipulador [`scene:openURLContexts:`]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#swift_step-3-implement-a-handler), adicione o código a seguir para processar o deep link `{YOUR-APP-SCHEME}:app-store-review`. Observe que você precisará importar `StoreKit` para usar `SKStoreReviewController`:

{% tabs %}
{% tab swift %}

```swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  guard let url = URLContexts.first?.url else { return }
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSURL *url = URLContexts.allObjects.firstObject.URL;
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### Etapa 4: Definir o comportamento ao clicar personalizado {#step-4-set-custom-on-click-behavior}

Em seguida, crie uma campanha de mensagens no app com o seguinte:

- O par chave-valor `"AppStore Review" : "true"`
- O comportamento ao clicar definido como "Deep Link Into App", usando o deep link `{YOUR-APP-SCHEME}:app-store-review`.

{% endraw %}

{% alert tip %}
A Apple limita os prompts de avaliação da App Store a no máximo três vezes por ano para cada usuário. Portanto, sua Campaign deve ter [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) configurado para três vezes por ano por usuário.<br><br>Os usuários podem desativar os prompts de avaliação da App Store. Por isso, seu prompt de avaliação personalizado não deve prometer que um prompt nativo de avaliação da App Store aparecerá nem pedir diretamente uma avaliação.
{% endalert %}