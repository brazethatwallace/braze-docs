> Ao construir uma interface personalizada para Content Cards, você deve registrar manualmente análises como impressões, cliques e dispensas, pois isso é tratado automaticamente apenas para modelos de cartão padrão. Registrar esses eventos é uma parte padrão da integração de Content Cards e é essencial para relatórios e faturamento precisos de Campaigns. Para fazer isso, preencha sua interface personalizada com dados dos modelos de dados da Braze e, em seguida, registre manualmente os eventos. Depois de entender como registrar a análise de dados, você poderá ver as maneiras comuns pelas quais os clientes da Braze [criam Content Cards personalizados]({{site.baseurl}}/developer_guide/content_cards/creating_cards).

## Registrando análise de dados {#logging-analytics}

Ao implementar seus Content Cards personalizados, você pode analisar os objetos do cartão de conteúdo e extrair seus dados de carga útil, como `title`, `cardDescription` e `imageUrl`. Em seguida, você pode usar os dados do modelo resultante para preencher sua interface personalizada.

Para obter os modelos de dados do cartão de conteúdo, inscreva-se para receber as atualizações do cartão de conteúdo. Preste atenção especial em duas propriedades:

* **`id`**: Representa a string de ID do cartão de conteúdo. Esse é o identificador exclusivo usado para registrar análises de dados de Content Cards personalizados.
* **`extras`**: Engloba todos os pares de chave-valor do dashboard da Braze.

Todas as propriedades fora de `id` e `extras` são opcionais para análise de Content Cards personalizados. Para saber mais sobre o modelo de dados, consulte o artigo de integração de cada plataforma: [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab web %}

Registre uma função de retorno de chamada para se inscrever para receber atualizações quando os cartões forem atualizados.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Os Content Cards somente serão atualizados no início da sessão se uma solicitação de inscrição for chamada antes de `openSession()`. Você também pode optar por [atualizar manualmente o feed]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed).
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### Etapa 1: Criar uma variável de assinante privada {#step-1-create-a-private-subscriber-variable}

Para assinar as atualizações do cartão, primeiro declare uma variável privada em sua classe personalizada para manter o assinante:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Etapa 2: Inscrever-se para receber atualizações {#step-2-subscribe-to-updates}

Em seguida, adicione o seguinte código para inscrever-se para receber as atualizações dos Content Cards da Braze, normalmente dentro de `Activity.onCreate()` da atividade dos Content Cards personalizados:

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

### Etapa 3: Cancelar inscrição {#step-3-unsubscribe}

Também recomendamos cancelar a inscrição quando sua atividade personalizada sair de vista. Adicione o seguinte código ao método de ciclo de vida `onDestroy()` de sua atividade:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### Etapa 1: Criar uma variável de assinante privada

Para assinar as atualizações do cartão, primeiro declare uma variável privada em sua classe personalizada para manter o assinante:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### Etapa 2: Inscrever-se para receber atualizações

Em seguida, adicione o seguinte código para inscrever-se para receber as atualizações dos Content Cards da Braze, normalmente dentro de `Activity.onCreate()` da atividade dos Content Cards personalizados:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### Etapa 3: Cancelar inscrição

Também recomendamos cancelar a inscrição quando sua atividade personalizada sair de vista. Adicione o seguinte código ao método de ciclo de vida `onDestroy()` de sua atividade:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Para acessar o modelo de dados dos Content Cards, chame [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) na sua instância `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

{% alert note %}
A leitura de `contentCards.cards`, `contentCards.unviewedCards` ou `contentCards.lastUpdate` bloqueia a thread de chamada até que o SDK conclua suas operações pós-inicialização. Use os getters não bloqueantes em [Acessores de snapshot não bloqueantes](#non-blocking-snapshot-accessors) para contextos na thread principal ou sensíveis à latência.
{% endalert %}

Além disso, você também pode manter uma inscrição para observar as alterações nos seus Content Cards. Você pode fazer isso de duas maneiras:
1. Manutenção de um cancelável; ou
2. Manutenção de um `AsyncStream`.

### Cancelável {#cancellable}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

### Acessores de snapshot não bloqueantes {#non-blocking-snapshot-accessors}

Use esses métodos para ler o estado em cache atual sem bloquear a thread de chamada. Cada handler de conclusão é sempre entregue na thread principal.

```swift
// All cached cards.
AppDelegate.braze?.contentCards.getCachedContentCards { cards in
  // Use `cards` here.
}

// Unviewed cards only (excludes control cards).
AppDelegate.braze?.contentCards.getUnviewedCards { cards in
  // Use `cards` here.
}

// Date of the last server sync for the current user (nil until the first sync completes).
AppDelegate.braze?.contentCards.getLastUpdate { date in
  // Use `date` here.
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Além disso, para manter uma inscrição nos seus Content Cards, você pode chamar [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)):

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

Para ler o estado em cache atual sem bloquear a thread de chamada, use os métodos a seguir. Cada handler de conclusão é entregue na thread principal.

```objc
// All cached cards.
[AppDelegate.braze.contentCards getCachedContentCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Unviewed cards only (excludes control cards).
[AppDelegate.braze.contentCards getUnviewedCardsWithCompletion:^(NSArray<BRZContentCardRaw *> *cards) {
  // Use `cards` here.
}];

// Date of the last server sync for the current user (nil until the first sync completes).
[AppDelegate.braze.contentCards getLastUpdateWithCompletion:^(NSDate * _Nullable date) {
  // Use `date` here.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}

Para obter os dados do cartão de conteúdo, use o método `getContentCards`:

```javascript
import Braze from "@braze/react-native-sdk";

const cards = await Braze.getContentCards();
```

Para ouvir atualizações, inscreva-se nos eventos de atualização do cartão de conteúdo:

```javascript
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to log an impression
    } else {
      // Use card.title, card.cardDescription, card.image, etc.
    }
  });
});
```

Para solicitar uma atualização manual dos Content Cards dos servidores da Braze:

```javascript
Braze.requestContentCardsRefresh();
```

Para obter Content Cards em cache sem uma solicitação de rede:

```javascript
const cachedCards = await Braze.getCachedContentCards();
```

{% endtab %}
{% endtabs %}

## Registrando eventos {#logging-events}

O registro de métricas valiosas, como impressões, cliques e dispensas, é rápido e simples. Defina um listener de cliques personalizado para lidar manualmente com essas análises de dados.

{% tabs %}
{% tab web %}

Registre eventos de impressão quando os cartões forem visualizados pelos usuários usando [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Registre os eventos de clique do cartão quando os usuários interagirem com um cartão usando [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick):

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab android %}

O [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) pode referenciar dependências do SDK da Braze, como a lista de objetos do cartão de conteúdo, para obter o [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) e chamar os métodos de registro da Braze. Use a classe base `ContentCardable` para facilitar a referência e o fornecimento de dados para o `BrazeManager`.

Para registrar uma impressão ou clique em um cartão, chame [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) ou [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html), respectivamente.

É possível registrar manualmente ou definir um cartão de conteúdo como "descartado" na Braze com [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html). Se um cartão já tiver sido marcado como descartado, ele não poderá ser marcado como descartado novamente.

Para criar um listener de cliques personalizado, crie uma classe que implemente [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) e registre-a com [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implemente o método [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html), que será chamado quando o usuário clicar em um Content Card. Em seguida, instrua a Braze a usar seu listener de clique do Content Card.

{% subtabs local %}
{% subtab Java %}

Por exemplo:

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

Por exemplo:

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Para lidar com a variante de controle dos Content Cards na sua interface personalizada, passe o objeto [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) e, em seguida, chame o método `logImpression` como faria com qualquer outro tipo de Content Card. O objeto registrará implicitamente uma impressão de controle para informar nossa análise de dados sobre quando um usuário teria visto o cartão de controle.{% endalert %}

{% endtab %}

{% tab swift %}

Implemente o protocolo [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) e defina seu objeto delegado como a propriedade `delegate` de `BrazeContentCardUI.ViewController`. Esse delegado tratará de passar os dados do seu objeto personalizado de volta à Braze para serem registrados. Para ver um exemplo, consulte o [tutorial da interface dos Content Cards](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Para lidar com a variante de controle dos Content Cards na sua interface personalizada, passe o objeto [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) e, em seguida, chame o método `logImpression` como faria com qualquer outro tipo de Content Card. O objeto registrará implicitamente uma impressão de controle para informar nossa análise de dados sobre quando um usuário teria visto o cartão de controle.
{% endalert %}
{% endtab %}

{% tab react native %}

Registre eventos de impressão quando os cartões forem visualizados pelos usuários:

```javascript
Braze.logContentCardImpression(card.id);
```

Registre eventos de clique em cartões quando os usuários interagirem com um cartão:

```javascript
Braze.logContentCardClicked(card.id);
```

Registre eventos de dispensa quando um usuário dispensar um cartão:

```javascript
Braze.logContentCardDismissed(card.id);
```

{% endtab %}
{% endtabs %}

## Lidando com o comportamento ao clicar {#handling-on-click-behavior}

{% tabs %}
{% tab web %}

Quando um usuário clica em um Content Card em um feed personalizado, o comportamento ao clicar (como navegar para uma URL, deep linking ou registrar um evento personalizado) não é tratado automaticamente. Use [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction) para processar a URL do cartão e executar a ação de clique configurada, incluindo ações da Braze (URLs `brazeActions://`).

```javascript
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
  // Log the click
  braze.logContentCardClick(card);

  // Handle the on-click behavior
  if (card.url) {
    braze.handleBrazeAction(card.url);
  }
}
```

| Parâmetro | Descrição |
|---|---|
| `url` | Uma URL válida ou uma URL de ação da Braze válida com o esquema `brazeActions://`. |
| `openLinkInNewTab` | (Opcional) Se a URL deve ser aberta em uma nova guia. O padrão é `false`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lidando com o comportamento ao clicar" }

{% alert important %}
Se você não chamar `handleBrazeAction()`, os comportamentos ao clicar configurados no dashboard da Braze (como "Registrar evento personalizado" ou "Navegar para URL") não serão executados para cartões exibidos em um feed personalizado.
{% endalert %}

{% endtab %}
{% tab android %}

O comportamento ao clicar é tratado automaticamente pela interface padrão dos Content Cards. Para implementações personalizadas, use a interface [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) descrita na seção [Registrando análise de dados](#logging-analytics).

{% endtab %}
{% tab swift %}

O comportamento ao clicar é tratado automaticamente pela interface padrão dos Content Cards. Para implementações personalizadas, use o protocolo [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) descrito na seção [Registrando análise de dados](#logging-analytics).

{% endtab %}
{% endtabs %}