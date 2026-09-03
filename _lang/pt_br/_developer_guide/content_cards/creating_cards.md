---
nav_title: Criar cartões
article_title: Criar Content Cards
page_order: 0
description: "Este artigo aborda os componentes para criar uma interface de usuário personalizada de Content Cards."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Criar Content Cards {#create-content-cards}

> Este artigo discute a abordagem básica que você usará ao implementar Content Cards personalizados, bem como três casos de uso comuns. Ele pressupõe que você já tenha lido os outros artigos do guia de personalização de Content Cards para entender o que pode ser feito por padrão e o que requer código personalizado. É especialmente útil entender como [registrar análise de dados]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) para seus Content Cards personalizados.

{% multi_lang_include banners/content_card_alert.md %}

## Criando um cartão {#creating-a-card}

### Etapa 1: Criar uma interface personalizada {#step-1-create-a-custom-ui}

{% tabs local %}
{% tab web %}

Primeiro, crie seu componente HTML personalizado que será usado para renderizar os cartões.

{% endtab %}
{% tab android %}

Primeiro, crie seu próprio fragment personalizado. O [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) padrão foi projetado apenas para lidar com nossos tipos padrão de Content Cards, mas é um bom ponto de partida.

{% endtab %}
{% tab swift %}

Primeiro, crie seu próprio componente de view controller personalizado. O [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) padrão foi projetado apenas para lidar com nossos tipos padrão de Content Cards, mas é um bom ponto de partida.

{% endtab %}
{% endtabs %}

### Etapa 2: Inscrever-se para atualizações de cartões {#step-2-subscribe-to-card-updates}

Registre uma função de retorno de chamada para se inscrever e receber atualizações de dados quando os cartões forem atualizados. Você pode analisar os objetos de Content Cards e extrair os dados de carga útil, como `title`, `cardDescription` e `imageUrl`, e então usar os dados do modelo resultante para preencher sua interface personalizada.

Para obter os modelos de dados de Content Cards, inscreva-se para atualizações de Content Cards. Preste atenção especial às seguintes propriedades:

* **`id`:** Representa a string de ID do Content Card. Este é o identificador exclusivo usado para registrar análises de dados a partir de Content Cards personalizados.
* **`extras`:** Abrange todos os pares de chave-valor do dashboard da Braze.

Todas as propriedades fora de `id` e `extras` são opcionais para análise em Content Cards personalizados. Para saber mais sobre o modelo de dados, consulte o artigo de integração de cada plataforma: [Android]({{site.baseurl}}/developer_guide/content_cards?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards?sdktab=web).

{% tabs local %}
{% tab web %}

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
Content Cards só são atualizados no início da sessão se `subscribeToContentCardsUpdates()` for chamado antes de `openSession()`. Você também pode [atualizar manualmente o feed]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) a qualquer momento.
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

#### Etapa 2a: Criar uma variável privada de assinante {#step-2a-create-a-private-subscriber-variable}

Para se inscrever nas atualizações de cartões, primeiro declare uma variável privada em sua classe personalizada para armazenar seu assinante:

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

#### Etapa 2b: Inscrever-se para atualizações {#step-2b-subscribe-to-updates}

Adicione o código a seguir para se inscrever nas atualizações de Content Cards da Braze, normalmente dentro do `Activity.onCreate()` da sua atividade personalizada de Content Cards:

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

#### Etapa 2c: Cancelar inscrição {#step-2c-unsubscribe}

Cancele a inscrição quando sua atividade personalizada sair da visualização. Adicione o código a seguir ao método de ciclo de vida `onDestroy()` da sua atividade:

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

#### Etapa 2a: Criar uma variável privada de assinante

Para se inscrever nas atualizações de cartões, primeiro declare uma variável privada em sua classe personalizada para armazenar seu assinante:

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

#### Etapa 2b: Inscrever-se para atualizações

Adicione o código a seguir para se inscrever nas atualizações de Content Cards da Braze, normalmente dentro do `Activity.onCreate()` da sua atividade personalizada de Content Cards:

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

#### Etapa 2c: Cancelar inscrição

Cancele a inscrição quando sua atividade personalizada sair da visualização. Adicione o código a seguir ao método de ciclo de vida `onDestroy()` da sua atividade:

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Para acessar o modelo de dados de Content Cards, chame [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) na sua instância `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Além disso, você pode manter uma inscrição para observar alterações nos seus Content Cards. Isso pode ser feito de duas maneiras:
1. Mantendo um cancelável; ou
2. Mantendo um `AsyncStream`.

##### Cancelável {#cancellable}

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

##### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Além disso, se você quiser manter uma inscrição para seus cartões de conteúdo, pode chamar [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)):

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}


### Etapa 3: Implementar análise de dados {#step-3-implement-analytics}

Impressões, cliques e dispensas de Content Cards não são registrados automaticamente na sua visualização personalizada. Você deve [implementar cada método correspondente]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) para registrar corretamente todas as métricas de volta na análise de dados do dashboard da Braze.

### Etapa 4: Testar seu cartão (opcional) {#step-4-test-your-card-optional}

Para testar seu Content Card:

1. Defina um usuário ativo no seu aplicativo chamando o método [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
2. Na Braze, acesse **Campaigns** e [crie uma nova campanha de Content Card]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card).
3. Na sua campanha, selecione **Test** e insira o `user-id` do usuário teste. Quando estiver pronto, selecione **Send Test**. Em breve, você poderá lançar um Content Card no seu dispositivo.

![Uma campanha de Content Card da Braze mostrando que você pode adicionar seu próprio ID de usuário como destinatário de teste para testar seu Content Card.]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

## Posicionamentos de Content Cards {#content-card-placements}

Content Cards podem ser usados de diversas formas. Três implementações comuns são utilizá-los como centro de mensagens, anúncio dinâmico com imagem ou carrossel de imagens. Para cada um desses posicionamentos, você atribuirá [pares chave-valor]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior) (a propriedade `extras` no modelo de dados) aos seus Content Cards e, com base nos valores, ajustará dinamicamente o comportamento, a aparência ou a funcionalidade do cartão durante a execução.

![Diagrama mostrando três exemplos de posicionamento de Content Cards: caixa de entrada de mensagens, anúncio dinâmico com imagem e carrossel de imagens.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Caixa de entrada de mensagens {#message-inbox}

Content Cards podem ser usados para simular um centro de mensagens. Nesse formato, cada mensagem é um cartão próprio que contém [pares chave-valor]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior) que controlam eventos ao clicar. Esses pares chave-valor são os identificadores-chave que o aplicativo analisa ao decidir para onde direcionar o usuário quando ele clica em uma mensagem da caixa de entrada. Os valores dos pares chave-valor são arbitrários.

#### Exemplo {#example}

Por exemplo, talvez você queira criar dois cartões de mensagem: uma chamada para ação incentivando os usuários a ativar recomendações de leitura e um código de cupom oferecido ao seu Segment de novos inscritos.

Chaves como `body`, `title` e `buttonText` podem ter valores de string simples que seus profissionais de marketing podem definir. Chaves como `terms` podem ter valores que fornecem uma pequena coleção de frases aprovadas pelo seu departamento jurídico. Chaves como `style` e `class_type` possuem valores de string que você pode definir para determinar como o cartão é renderizado no seu app ou site.

{% tabs local %}
{% tab Recomendações de leitura %}
Pares chave-valor para o cartão de recomendação de leitura:

| Chave       | Valor                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Adicione seus interesses ao seu perfil Politer Weekly para receber recomendações de leitura personalizadas. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemplo" }
{% endtab %}

{% tab Cupom para novos inscritos %}
Pares chave-valor para um cupom de novos inscritos:

| Chave       | Valor                                                            |
|------------|------------------------------------------------------------------|
| `title`      | Inscreva-se para jogos ilimitados                                |
| `body`       | Especial de fim de verão - Aproveite 10% de desconto em jogos Politer |
| `buttonText` | Inscreva-se agora                                                |
| `style`      | promo                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exemplo" }
{% endtab %}
{% endtabs %}

{% details Informações adicionais para Android %}

No SDK para Android e FireOS, a lógica do centro de mensagens é controlada pelo valor de `class_type` fornecido pelos pares chave-valor da Braze. Usando o método [`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards), você pode filtrar e identificar esses tipos de classe.

{% tabs local %}
{% tab Kotlin %}
**Usando `class_type` para comportamento ao clicar**<br>
Quando preenchemos os dados de Content Cards nas nossas classes personalizadas, usamos a propriedade `ContentCardClass` dos dados para determinar qual subclasse concreta deve ser usada para armazenar os dados.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

Depois, ao lidar com a interação do usuário com a lista de mensagens, podemos usar o tipo da mensagem para determinar qual visualização exibir.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**Usando `class_type` para comportamento ao clicar**<br>
Quando preenchemos os dados de Content Cards nas nossas classes personalizadas, usamos a propriedade `ContentCardClass` dos dados para determinar qual subclasse concreta deve ser usada para armazenar os dados.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Depois, ao lidar com a interação do usuário com a lista de mensagens, podemos usar o tipo da mensagem para determinar qual visualização exibir.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### Carrossel {#carousel}

Você pode configurar Content Cards em um feed de carrossel totalmente personalizado, permitindo que os usuários deslizem e visualizem cartões em destaque adicionais. Por padrão, Content Cards são classificados pela data de criação (mais recentes primeiro) e seus usuários verão todos os cartões para os quais são elegíveis.

Para implementar um carrossel de Content Cards:

1. Crie uma lógica personalizada que observe [mudanças nos seus Content Cards]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed) e lide com a chegada de novos cartões.
2. Crie uma lógica personalizada no lado do cliente para exibir um número específico de cartões no carrossel a qualquer momento. Por exemplo, você pode selecionar os cinco primeiros objetos de Content Cards do array ou introduzir pares chave-valor para construir uma lógica condicional.

{% alert tip %}
Se você estiver implementando um carrossel como um feed secundário de Content Cards, certifique-se de [classificar os cartões no feed correto usando pares chave-valor]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed).
{% endalert %}

### Somente imagem {#image-only}

Content Cards não precisam parecer "cartões". Por exemplo, Content Cards podem aparecer como uma imagem dinâmica que é exibida de forma persistente na sua página inicial ou no topo de páginas designadas.

Para conseguir isso, seus profissionais de marketing criarão uma Campaign ou etapa do Canvas com um tipo de Content Card **somente imagem**. Depois, defina pares chave-valor apropriados para usar [Content Cards como conteúdo complementar]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/behavior).