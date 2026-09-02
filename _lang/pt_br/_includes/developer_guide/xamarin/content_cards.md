## Sobre os Content Cards do .NET MAUI {#about-net-maui-content-cards}

O SDK or kit de desenvolvimento de software da Braze para .NET MAUI (anteriormente Xamarin) inclui um feed de cartões padrão para você começar com os Content Cards. O feed de cartões padrão incluído com o SDK or kit de desenvolvimento de software da Braze lidará com toda a análise de dados, rastreamento, dispensas e renderização dos Content Cards de um usuário.

{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Tipos e propriedades de cartões {#card-types-and-properties}

O SDK or kit de desenvolvimento de software da Braze para .NET MAUI possui três tipos únicos de Content Cards que compartilham um modelo base: [Banner](#xamarin_banner), [Imagem com legenda](#xamarin_captioned-image) e [Clássico](#xamarin_classic). Cada tipo herda propriedades comuns de um modelo base e possui as seguintes propriedades adicionais.

### Modelo base de cartão {#base-card-model}

| Propriedade | Descrição |
|-------------------|------------------------------------------------------------------------------------------------------------------------|
| `idString` | O ID do cartão definido pela Braze. |
| `created` | O carimbo de data/hora UNIX do horário de criação do cartão na Braze. |
| `expiresAt` | O carimbo de data/hora UNIX do tempo de expiração do cartão. Quando o valor é menor que 0, significa que o cartão nunca expira. |
| `viewed` | Se o cartão foi lido ou não pelo usuário. Isso não registra análise de dados. |
| `clicked` | Se o cartão foi clicado pelo usuário. |
| `pinned` | Se o cartão está fixado. |
| `dismissed` | Se o usuário dispensou este cartão. Marcar um cartão como dispensado que já foi dispensado será uma operação nula. |
| `dismissible` | Se o cartão pode ser descartado pelo usuário. |
| `urlString` | (Opcional) A string de URL associada à ação de clique do cartão. |
| `openUrlInWebView` | Se as URLs deste cartão devem ser abertas no Braze WebView ou não. |
| `isControlCard` | Se este cartão é um cartão de controle. Os cartões de controle não devem ser exibidos ao usuário. |
| `extras` | O mapa de extras de chave-valor para este cartão. |
| `isTest` | Se este cartão é um cartão de teste. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model" }

Para uma referência completa do cartão base, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct).

### Banner

Os cartões de banner são imagens clicáveis em tamanho completo.

| Propriedade | Descrição |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | A URL da imagem do cartão. |
| `imageAspectRatio` | A proporção da imagem do cartão. Serve como uma dica antes que o carregamento da imagem seja concluído. Note que a propriedade pode não ser fornecida em certas circunstâncias. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Banner" }

Para uma referência completa do cartão de banner, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/imageonly-swift.struct) (agora renomeado para image only).

### Imagem com legenda {#captioned-image}

Os cartões de imagem com legenda são imagens em tamanho completo clicáveis com texto descritivo acompanhante.

| Propriedade | Descrição |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | A URL da imagem do cartão. |
| `imageAspectRatio` | A proporção da imagem do cartão. Serve como uma dica antes que o carregamento da imagem seja concluído. Note que a propriedade pode não ser fornecida em certas circunstâncias. |
| `title` | O texto do título do cartão. |
| `cardDescription` | O texto de descrição do cartão. |
| `domain` | (Opcional) O texto do link para a URL da propriedade, por exemplo, `"braze.com/resources/"`. Pode ser exibido na interface do cartão para indicar a ação/direção ao clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image" }

Para uma referência completa do cartão de imagem com legenda, consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/captionedimage-swift.struct).

### Clássico {#classic}

Os cartões clássicos têm um título, uma descrição e uma imagem opcional antes do texto.

| Propriedade | Descrição |
|-------------------|-------------------------------------------------------------------------------------------------------------------|
| `image` | (Opcional) A URL da imagem do cartão. |
| `title` | O texto do título do cartão. |
| `cardDescription` | O texto de descrição do cartão. |
| `domain` | (Opcional) O texto do link para a URL da propriedade, por exemplo, `"braze.com/resources/"`. Pode ser exibido na interface do cartão para indicar a ação/direção ao clicar no cartão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic" }

Para uma referência completa do Content Card clássico (anúncio de texto), consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classic-swift.struct). Para uma referência completa do cartão de imagem clássico (notícia curta), consulte a documentação do [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) e [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/classicimage-swift.struct).

## Métodos do cartão {#card-methods}

Você pode usar esses métodos adicionais para criar um feed de Content Cards personalizado dentro do seu app:

| Método | Descrição |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `requestContentCardsRefresh()` | Solicita os Content Cards mais recentes do servidor do SDK or kit de desenvolvimento de software da Braze. |
| `getContentCards()` | Recupera os Content Cards do SDK or kit de desenvolvimento de software da Braze. Isso retornará a lista mais recente de cartões do servidor. |
| `logContentCardClicked(cardId)` | Registra um clique para o ID do Content Card fornecido. Este método é usado apenas para análise de dados. |
| `logContentCardImpression(cardId)` | Registra uma impressão para o ID do Content Card fornecido. |
| `logContentCardDismissed(cardId)` | Registra uma dispensa para o ID do Content Card fornecido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }