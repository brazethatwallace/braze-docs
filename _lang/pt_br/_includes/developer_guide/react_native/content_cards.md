## Sobre os Content Cards no React Native {#about-react-native-content-cards}

Os SDKs da Braze incluem um feed de cartão padrão para que você comece a usar os Content Cards. Para mostrar o feed do cartão, você pode usar o método `Braze.launchContentCards()`. O feed de cartão padrão incluído com o SDK da Braze lidará com toda a análise de dados, rastreamento, dispensas e renderização para os Content Cards de um usuário.

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Métodos de cartões {#cards-methods}

Para criar sua própria interface do usuário, você pode obter uma lista de cartões disponíveis e ouvir as atualizações dos cartões:

```javascript
// Set initial cards
const [cards, setCards] = useState([]);

// Listen for updates as a result of card refreshes, such as:
// a new session, a manual refresh with `requestContentCardsRefresh()`, or after the timeout period
Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, async (update) => {
    setCards(update.cards);
});

// Manually trigger a refresh of cards
Braze.requestContentCardsRefresh();
```

{% alert important %}
Se você optar por criar sua própria interface do usuário para exibir cartões, deverá chamar `logContentCardImpression` para receber análises de dados desses cartões. Isso inclui os cartões `control`, que devem ser rastreados mesmo que não sejam exibidos ao usuário.
{% endalert %}

Você pode usar esses métodos adicionais para criar um feed de Content Cards personalizado em seu app:

| Método                                   | Descrição                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `launchContentCards()`                   | Inicia o elemento da interface do usuário dos Content Cards.                                                                 |
| `requestContentCardsRefresh()`           | Solicita os Content Cards mais recentes do servidor do SDK da Braze. A lista de cartões resultante é passada para cada um dos [ouvintes de eventos de cartão de conteúdo](#reactnative_cards-methods) registrados anteriormente. |
| `getContentCards()`                      | Recupera os Content Cards do SDK da Braze. Isso retorna uma promessa que é resolvida com a lista mais recente de cartões do servidor. |
| `getCachedContentCards()`                | Retorna a matriz de Content Cards mais recente do cache.                                            |
| `logContentCardClicked(cardId)`          | Registra um clique para o ID do cartão de conteúdo fornecido. Esse método é usado apenas para análise de dados. Para executar a ação de clique, chame também `processContentCardClickAction(cardId)`.                                                        |
| `logContentCardImpression(cardId)`       | Registra uma impressão para o ID do cartão de conteúdo fornecido.                                                      |
| `logContentCardDismissed(cardId)`        | Registra um descarte para o ID do cartão de conteúdo fornecido.                                                        |
| `processContentCardClickAction(cardId)`  | Executa a ação de um determinado cartão.                                                               |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Cards methods" }

## Tipos e propriedades do cartão {#card-types-and-properties}

O modelo de dados dos Content Cards está disponível no React Native SDK e oferece os seguintes tipos de cartões de conteúdo: [Somente imagem](#image-only), [Imagem com legenda](#captioned-image) e [Clássico](#classic). Há também um tipo especial de cartão [Controle](#control), que é retornado aos usuários que estão no grupo de controle de um determinado cartão. Cada tipo herda propriedades comuns de um modelo básico, além de suas próprias propriedades exclusivas.

{% alert tip %}
Para uma referência completa do modelo de dados do Content Card, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard).
{% endalert %}

### Modelo de cartão básico {#base-card-model}

O modelo de cartão básico fornece o comportamento fundamental para todos os cartões.

| Propriedade      | Descrição                                                                                                            |
|--------------|------------------------------------------------------------------------------------------------------------------------|
| `id`          | O ID do cartão definido pela Braze.                                                                                            |
| `created`     | O carimbo de data/hora UNIX do horário de criação do cartão na Braze.                                                             |
| `expiresAt`   | O carimbo de data/hora UNIX do tempo de expiração do cartão. Quando o valor é menor que 0, isso significa que o cartão nunca expira.      |
| `viewed`      | Se o cartão foi lido ou não pelo usuário. Isso não registra análise de dados.                                           |
| `clicked`     | Se o cartão foi clicado pelo usuário.                                                                         |
| `pinned`      | Se o cartão está fixado.                                                                                            |
| `dismissed`   | Se o usuário dispensou este cartão. Marcar um cartão como dispensado que já foi dispensado será uma operação nula. |
| `dismissible` | Se o cartão pode ser descartado pelo usuário.                                                                           |
| `url`         | (Opcional) A string de URL associada à ação de clique do cartão.                                                       |
| `openURLInWebView` | Se os URLs para esse cartão devem ser abertos no Braze WebView ou não.                                            |
| `isControl`   | Se este cartão é um cartão de controle. Os cartões de controle não devem ser exibidos ao usuário.                                |
| `extras`      | O mapa de extras de chave-valor para este cartão.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model" }

Para uma referência completa do cartão base, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Somente imagem {#image-only}

Os cartões somente de imagem são imagens clicáveis e em tamanho real.

| Propriedade           | Descrição                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | O tipo de Content Card, `IMAGE_ONLY`.                                                                              |
| `image`            | A URL da imagem do cartão.                                                                                      |
| `imageAspectRatio` | A proporção da imagem do cartão. Destina-se a servir como uma dica antes que o carregamento da imagem seja concluído. Note que a propriedade pode não ser fornecida em certas circunstâncias. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image only" }

Para uma referência completa do cartão somente de imagem, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct).

### Imagem com legenda {#captioned-image}

Cartões de imagem com legenda são imagens em tamanho real clicáveis com texto descritivo acompanhante.

| Propriedade           | Descrição                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | O tipo de Content Card, `CAPTIONED`.                                                                               |
| `image`            | A URL da imagem do cartão.                                                                                      |
| `imageAspectRatio` | A proporção da imagem do cartão. Destina-se a servir como uma dica antes que o carregamento da imagem seja concluído. Note que a propriedade pode não ser fornecida em certas circunstâncias. |
| `title`            | O texto do título do cartão.                                                                                      |
| `cardDescription`  | O texto de descrição do cartão.                                                                                |
| `domain`           | (Opcional) O texto do link para a URL da propriedade, por exemplo, `"braze.com/resources/"`. Pode ser exibido na interface do usuário do cartão para indicar a ação/direção de clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image" }

Para uma referência completa do cartão de imagem com legenda, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Clássico {#classic}

Os cartões clássicos têm um título, descrição e uma imagem opcional à esquerda do texto.

| Propriedade           | Descrição                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `type`             | O tipo de Content Card, `CLASSIC`.                                                                                 |
| `image`            | (Opcional) A URL da imagem do cartão.                                                                           |
| `title`            | O texto do título do cartão.                                                                                      |
| `cardDescription`  | O texto de descrição do cartão.                                                                                |
| `domain`           | (Opcional) O texto do link para a URL da propriedade, por exemplo, `"braze.com/resources/"`. Pode ser exibido na interface do usuário do cartão para indicar a ação/direção de clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic" }

Para uma referência completa do Content Card clássico (anúncio de texto), consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Para o cartão de imagem clássico (notícias curtas), consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

### Controle {#control}

Os cartões de controle incluem todas as propriedades básicas, com algumas diferenças importantes. E o mais importante:

- A propriedade `isControl` tem a garantia de ser `true`.
- A propriedade `extras` tem a garantia de estar vazia.

Para uma referência completa do cartão de controle, consulte a documentação para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-control-card/index.html) e para [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control-swift.struct).