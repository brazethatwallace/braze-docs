---
nav_title: Integração
article_title: Integração do controlador de visualização de Content Cards para iOS
platform: iOS
page_order: 1
description: "Este artigo de referência aborda as etapas de integração, modelos de dados e propriedades específicas de cartão disponíveis para seu app iOS."
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração de Content Cards {#content-card-integration}

## Modelo de dados de Content Cards {#content-cards-data-model}

O modelo de dados de Content Cards está disponível no SDK para iOS.

### Obtenção dos dados {#getting-the-data}

Para acessar o modelo de dados de Content Cards, inscreva-se nos eventos de atualização de Content Cards:

{% tabs %}
{% tab OBJECTIVE-C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab swift %}
```swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

Se você quiser alterar os dados do cartão depois de enviados pela Braze, recomendamos armazenar uma cópia profunda dos dados do cartão localmente, atualizar os dados e exibi-los você mesmo. Os cartões são acessíveis via [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html).

## Modelo de Content Card {#content-card-model}

A Braze oferece três tipos de Content Cards: banner, imagem legendada e clássico. Cada tipo herda propriedades comuns de uma classe base `ABKContentCard` e possui as seguintes propriedades adicionais.

### Propriedades do modelo de Content Card base - ABKContentCard {#base-content-card-model-properties-abkcontentcard}

| Propriedade | Descrição |
|---|---|
| `idString` | (Somente leitura) O ID do cartão definido pela Braze. |
| `viewed` | Essa propriedade reflete se o usuário visualizou o cartão ou não. |
| `created` | (Somente leitura) Essa propriedade é o timestamp unix do horário de criação do cartão na Braze. |
| `expiresAt` | (Somente leitura) Essa propriedade é o timestamp unix do tempo de expiração do cartão. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão. |
| `pinned` | Essa propriedade reflete se o cartão foi configurado como "fixado" no dashboard. |
| `dismissed` | Essa propriedade reflete se o usuário descartou o cartão. |
| `url` | A URL que será aberta após o cartão ser clicado. Pode ser uma URL HTTP(s) ou uma URL de protocolo. |
| `openURLInWebView` | Essa propriedade determina se a URL será aberta dentro do app ou em um navegador de internet externo. |
| `extras` | Um `NSDictionary` opcional de valores `NSString`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base Content Card model properties - ABKContentCard" }

### Propriedades do Content Card de banner - ABKBannerContentCard {#banner-content-card-properties-abkbannercontentcard}

| Propriedade | Descrição |
|---|---|
| `image` | Essa propriedade é a URL da imagem do cartão. |
| `imageAspectRatio` | Essa propriedade é a proporção da imagem do cartão e serve como uma dica antes que o carregamento da imagem seja concluído. Observe que a propriedade pode não ser fornecida em certas circunstâncias. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Banner Content Card properties - ABKBannerContentCard" }

### Propriedades do Content Card de imagem legendada - ABKCaptionedImageCard {#captioned-image-content-card-properties-abkcaptionedimagecard}

| Propriedade | Descrição |
|---|---|
| `image` | Essa propriedade é a URL da imagem do cartão. |
| `imageAspectRatio` | Essa propriedade é a proporção da imagem do cartão. |
| `title` | O texto do título do cartão. |
| `cardDescription` | O texto do corpo do cartão. |
| `domain` | O texto do link para a URL da propriedade, como @"blog.braze.com". Pode ser exibido na interface do cartão para indicar a ação/direção ao clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image Content Card properties - ABKCaptionedImageCard" }

### Propriedades do Content Card clássico - ABKClassicContentCard {#classic-content-card-properties-abkclassiccontentcard}

| Propriedade | Descrição |
|---|---|
| `image` | (Opcional) Essa propriedade é a URL da imagem do cartão. |
| `title` | O texto do título do cartão. |
| `cardDescription` | O texto do corpo do cartão. |
| `domain` | O texto do link para a URL da propriedade, como @"blog.braze.com". Pode ser exibido na interface do cartão para indicar a ação e a direção ao clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic Content Card properties - ABKClassicContentCard" }

## Métodos do cartão {#card-methods}

| Método | Descrição |
|---|---|
| `logContentCardImpression` | Registre manualmente uma impressão na Braze para um determinado cartão. |
| `logContentCardClicked` | Registre manualmente um clique na Braze para um determinado cartão. O SDK só registrará um clique no cartão quando o cartão tiver a propriedade `url` com um valor válido. |
| `logContentCardDismissed` | Registre manualmente um descarte na Braze para um cartão específico. O SDK só registrará um descarte de cartão se a propriedade `dismissed` do cartão ainda não estiver definida como `true`. |
| `isControlCard` | Determine se um cartão é o cartão de Controle para um teste A/B. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }

Para saber mais, consulte a [documentação de referência da classe](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html).

## Integração do controlador de visualização de Content Cards {#content-cards-view-controller-integration}

Content Cards podem ser integrados com dois contextos de controlador de visualização: navegação ou modal.

### Contexto de navegação {#navigation-context}

Exemplo de como inserir uma instância `ABKContentCardsTableViewController` em um controlador de navegação:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Para personalizar o título da barra de navegação, defina a propriedade title do `navigationItem` da instância `ABKContentCardsTableViewController`.
{% endalert %}

### Contexto modal {#modal-context}

Este modal é usado para apresentar o controlador de visualização em uma visualização modal, com uma barra de navegação no topo e um botão **Done** na lateral da barra.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

Para exemplos de controlador de visualização, confira o [app de exemplo de Content Cards](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp).

{% alert note %}
Para personalizar o cabeçalho, defina a propriedade title do `navigationItem` pertencente à instância `ABKContentCardsTableViewController` incorporada na instância pai `ABKContentCardsViewController`.
{% endalert %}