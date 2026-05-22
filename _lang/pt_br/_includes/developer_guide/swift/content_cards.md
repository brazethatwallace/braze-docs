## Pré-requisitos {#prerequisites}

Antes de poder usar os Content Cards, você precisará integrar o [Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) em seu app. No entanto, não é necessária nenhuma configuração adicional.

## Contextos de view controller {#view-controller-contexts}

A interface padrão dos Content Cards pode ser integrada a partir da biblioteca `BrazeUI` do SDK da Braze. Crie o view controller dos Content Cards usando a instância `braze`. Se quiser interceptar e reagir ao ciclo de vida da interface do Content Card, implemente [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) como o delegado do seu `BrazeContentCardUI.ViewController`.

{% alert note %}
Para saber mais sobre as opções de view controller do iOS, consulte a [documentação da Apple para desenvolvedores](https://developer.apple.com/documentation/uikit/view_controllers/showing_and_hiding_view_controllers).
{% endalert %}

A biblioteca `BrazeUI` do Swift SDK fornece dois contextos de view controller padrão: [navegação](#swift_navigation) ou [modal](#swift_modal). Isso significa que você pode integrar os Content Cards nesses contextos adicionando algumas linhas de código ao seu app ou site. Ambas as visualizações oferecem opções de personalização e estilo, conforme descrito no [guia de personalização]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_styles/?tab=ios). Você também pode criar um view controller de cartão de conteúdo personalizado em vez de usar o padrão da Braze para ter ainda mais opções de personalização — consulte o [tutorial Content Cards UI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/) para obter um exemplo.

{% alert important %}
Para lidar com a variante de controle dos Content Cards em sua interface personalizada, passe o objeto [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) e, em seguida, chame o método `logImpression` como faria com qualquer outro tipo de Content Card. O objeto registrará implicitamente uma impressão de controle para informar nossa análise de dados sobre quando um usuário teria visto o cartão de controle.
{% endalert %}

### Navegação {#navigation}

Um navigation controller é um view controller que gerencia um ou mais child view controllers em uma interface de navegação. Veja um exemplo de como inserir uma instância `BrazeContentCardUI.ViewController` em um navigation controller:

{% tabs %}
{% tab swift %}

```swift
func pushViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsController = BrazeContentCardUI.ViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsController.delegate = self
  self.navigationController?.pushViewController(contentCardsController, animated: true)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)pushViewController {
  BRZContentCardUIViewController *contentCardsController = [[BRZContentCardUIViewController alloc] initWithBraze:self.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsController setDelegate:self];
  [self.navigationController pushViewController:contentCardsController animated:YES];
}
```

{% endtab %}
{% endtabs %}

### Modal

Use apresentações modais para criar interrupções temporárias no fluxo de trabalho do seu app, como solicitar informações importantes ao usuário. Essa visualização modal tem uma barra de navegação na parte superior e um botão **Done** na lateral da barra. Veja um exemplo de como inserir uma instância `BrazeContentCard.ViewController` em um modal controller:

{% tabs %}
{% tab swift %}

```swift
func presentModalViewController() {
  guard let braze = AppDelegate.braze else { return }
  let contentCardsModal = BrazeContentCardUI.ModalViewController(braze: braze)
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  contentCardsModal.viewController.delegate = self
  self.navigationController?.present(contentCardsModal, animated: true, completion: nil)
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)presentModalViewController {
  BRZContentCardUIModalViewController *contentCardsModal = [[BRZContentCardUIModalViewController alloc] initWithBraze:AppDelegate.braze];
  // Implement and set `BrazeContentCardUIViewControllerDelegate` if you wish to intercept click actions.
  [contentCardsModal.viewController setDelegate:self];
  [self.navigationController presentViewController:contentCardsModal animated:YES completion:nil];
}
```

{% endtab %}
{% endtabs %}

Para obter um exemplo de uso dos view controllers `BrazeUI`, confira as amostras correspondentes da interface dos Content Cards em nosso [app Examples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples).

## Modelo de cartão básico {#base-card-model}

O modelo de dados dos Content Cards está disponível no módulo `BrazeKit` do Braze Swift SDK. Este módulo contém os seguintes tipos de Content Card, que são uma implementação do tipo `Braze.ContentCard`. Para obter uma lista completa das propriedades do Content Card e seu uso, consulte a [classe `ContentCard`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).

- Somente imagem
- Imagem legendada
- Clássico
- Imagem clássica
- Controle

Para acessar o modelo de dados dos Content Cards, chame `contentCards.cards` em sua instância `braze`. Consulte [Registro de análise de dados]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) para saber mais sobre a assinatura de dados de cartões.

{% alert note %}
Lembre-se de que o `BrazeKit` oferece uma classe alternativa [`ContentCardRaw`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw) para compatibilidade com Objective-C.
{% endalert %}

## Métodos do cartão {#card-methods}

Cada cartão é inicializado com um objeto `Context`, que contém vários métodos para gerenciar o estado do cartão. Chame esses métodos quando quiser modificar a propriedade de estado correspondente em um objeto de cartão específico.

| Método | Descrição |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `card.context?.logImpression()` | Registra o evento de impressão do cartão de conteúdo. |
| `card.context?.logClick()` | Registra o evento de clique do cartão de conteúdo. |
| `card.context?.processClickAction()` | Processa uma determinada entrada [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/clickaction). |
| `card.context?.logDismissed()` | Registra o evento de descarte do cartão de conteúdo. |
| `card.context?.logError()` | Registra um erro relacionado ao cartão de conteúdo. |
| `card.context?.loadImage()` | Carrega uma determinada imagem de cartão de conteúdo a partir de um URL. Esse método pode ser nulo quando o cartão de conteúdo não tiver uma imagem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }

Para saber mais, consulte a [documentação da classe `Context`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcardraw/context-swift.class)