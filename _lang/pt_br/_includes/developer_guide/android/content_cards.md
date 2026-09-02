## Pré-requisitos {#prerequisites}

Antes de usar os Content Cards da Braze, você precisará integrar o [SDK or kit de desenvolvimento de software da Braze para Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) ao seu app. No entanto, nenhuma configuração adicional é necessária.

## Fragmentos do Google {#google-fragments}

No Android, o feed de Content Cards é implementado como um [fragmento](https://developer.android.com/guide/components/fragments.html) disponível no projeto de UI da Braze para Android. A classe [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) será atualizada automaticamente e exibirá o conteúdo dos Content Cards, além de registrar a análise de dados de uso. Os cartões que podem aparecer no `ContentCards` de um usuário são criados no dashboard da Braze.

Para saber como adicionar um fragmento a uma atividade, consulte a [documentação de fragmentos do Google](https://developer.android.com/guide/fragments#Adding).

## Tipos e propriedades de cartões {#card-types-and-properties}

O modelo de dados dos Content Cards está disponível no SDK or kit de desenvolvimento de software para Android e oferece os seguintes tipos exclusivos de Content Cards. Cada tipo compartilha um modelo base, que permite herdar propriedades comuns do modelo base, além de ter suas próprias propriedades exclusivas. Para a documentação de referência completa, consulte [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Modelo de cartão base {#base-card-for-android}

O modelo de [cartão base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fornece o comportamento fundamental para todos os cartões.

| Propriedade | Descrição |
|---|---|
| `getId()` | Retorna o ID do cartão definido pela Braze.|
| `getViewed()` | Retorna um booleano que indica se o cartão foi lido ou não pelo usuário.|
| `getExtras()` | Retorna um mapa de extras de chave-valor para este cartão.|
| `getCreated()` | Retorna o timestamp unix do horário de criação do cartão na Braze.|
| `isPinned` | Retorna um booleano que indica se o cartão está fixado.|
| `getOpenUriInWebView()` | Retorna um booleano que indica se as URIs deste cartão devem ser abertas <br> no WebView da Braze ou não.|
| `getExpiredAt()` | Obtém a data de expiração do cartão.|
| `isRemoved()` | Retorna um booleano que indica se o usuário final descartou este cartão.|
| `isDismissibleByUser()` | Retorna um booleano que indica se o cartão pode ser dispensado pelo usuário.|
| `isClicked()` | Retorna um booleano que indica o estado de clique deste cartão.|
| `isDismissed` | Retorna um booleano que indica se o cartão foi dispensado. Defina como `true` para marcar o cartão como dispensado. Se um cartão já estiver marcado como dispensado, ele não poderá ser marcado como dispensado novamente.|
| `isControl()` | Retorna um booleano indicando se este cartão é um cartão de controle e não deve ser renderizado.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model #base-card-for-android" }

### Somente imagem {#banner-image-card-for-android}

[Cartões somente com imagem](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) são imagens clicáveis em tamanho completo.

| Propriedade | Descrição |
|---|---|
| `getImageUrl()` | Retorna a URL da imagem do cartão.|
| `getUrl()` | Retorna a URL que será aberta após o cartão ser clicado. Pode ser uma URL HTTP(s) ou uma URL de protocolo.|
| `getDomain()` | Retorna o texto do link para a URL da propriedade.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image only #banner-image-card-for-android" }

### Imagem com legenda {#captioned-image-card-for-android}

[Cartões de imagem com legenda](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) são imagens clicáveis em tamanho completo com texto descritivo acompanhante.

| Propriedade | Descrição |
|---|---|
| `getImageUrl()` | Retorna a URL da imagem do cartão.|
| `getTitle()` | Retorna o texto do título do cartão.|
| `getDescription()` | Retorna o texto do corpo do cartão.|
| `getUrl()` | Retorna a URL que será aberta após o cartão ser clicado. Pode ser uma URL HTTP(s) ou uma URL de protocolo.|
| `getDomain()` | Retorna o texto do link para a URL da propriedade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image #captioned-image-card-for-android" }

### Clássico {#text-Announcement-card-for-android}

Um cartão clássico sem imagem resultará em um [cartão de anúncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Se uma imagem for incluída, você receberá um [cartão de notícias curtas](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

| Propriedade | Descrição |
|---|---|
| `getTitle()` | Retorna o texto do título do cartão. |
| `getDescription()` | Retorna o texto do corpo do cartão. |
| `getUrl()` | Retorna a URL que será aberta após o cartão ser clicado. Pode ser uma URL HTTP(s) ou uma URL de protocolo. |
| `getDomain()` | Retorna o texto do link para a URL da propriedade. |
| `getImageUrl()` | Retorna a URL da imagem do cartão. Aplica-se apenas ao cartão de notícias curtas clássico. |
| `isDismissed` | Retorna um booleano que indica se o cartão foi dispensado. Defina como `true` para marcar o cartão como dispensado. Se um cartão já estiver marcado como dispensado, ele não poderá ser marcado como dispensado novamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic #text-Announcement-card-for-android" }

## Métodos do cartão {#card-methods}

Todos os objetos do modelo de dados [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) oferecem os seguintes métodos de análise de dados para registrar eventos de usuários nos servidores da Braze.

| Método | Descrição |
|---|---|
| `logImpression()` | Registra manualmente uma impressão na Braze para um determinado cartão. |
| `logClick()` | Registra manualmente um clique na Braze para um determinado cartão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }