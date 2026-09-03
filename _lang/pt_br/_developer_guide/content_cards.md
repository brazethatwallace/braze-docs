---
page_order: 2.2
nav_title: Content Cards
article_title: Content Cards
description: "Saiba como implementar Content Cards com o SDK da Braze, incluindo modelos de dados, tipos de cartões e opções de personalização para seus apps mobile e web."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards {#content-cards}

> Saiba mais sobre os Content Cards para o SDK da Braze, incluindo os diferentes modelos de dados e propriedades específicas de cartões disponíveis para o seu aplicativo.

{% multi_lang_include banners/content_card_alert.md %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/content_cards.md %}
{% endsdktab %}

{% sdktab android %}
## Pré-requisitos {#prerequisites}

Antes de usar os Content Cards da Braze, você precisa integrar o [SDK Android da Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) ao seu app. No entanto, nenhuma configuração adicional é necessária.

## Fragmentos do Google {#google-fragments}

No Android, o feed de Content Cards é implementado como um [fragmento](https://developer.android.com/guide/components/fragments.html) disponível no projeto de UI Android da Braze. A classe [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) atualiza e exibe automaticamente o conteúdo dos Content Cards e registra análises de uso. Os cartões que podem aparecer nos `ContentCards` de um usuário são criados no dashboard da Braze.

Para saber como adicionar um fragmento a uma atividade, consulte a [documentação de fragmentos do Google](https://developer.android.com/guide/fragments#Adding).

## Tipos de cartões e propriedades {#card-types-and-properties}

O modelo de dados dos Content Cards está disponível no SDK Android e oferece os seguintes tipos exclusivos de Content Cards. Cada tipo compartilha um modelo base, o que permite herdar propriedades comuns do modelo base, além de ter suas próprias propriedades exclusivas. Para a documentação de referência completa, consulte [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Modelo de cartão base {#base-card-for-android}

O modelo de [cartão base](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) fornece o comportamento fundamental para todos os cartões.

| Propriedade | Descrição |
|---|---|
| `getId()` | Retorna o ID do cartão definido pela Braze. |
| `getViewed()` | Retorna um booleano que indica se o cartão foi lido ou não pelo usuário. |
| `getExtras()` | Retorna um mapa de extras de chave-valor para este cartão. |
| `getCreated()` | Retorna o timestamp unix do horário de criação do cartão na Braze. |
| `isPinned` | Retorna um booleano que indica se o cartão está fixado. |
| `getOpenUriInWebView()` | Retorna um booleano que indica se as URIs deste cartão devem ser abertas <br> no WebView da Braze ou não. |
| `getExpiredAt()` | Obtém a data de expiração do cartão. |
| `isRemoved()` | Retorna um booleano que indica se o usuário final descartou este cartão. |
| `isDismissibleByUser()` | Retorna um booleano que indica se o cartão pode ser descartado pelo usuário. |
| `isClicked()` | Retorna um booleano que indica o estado de clique deste cartão. |
| `isDismissed` | Retorna um booleano que indica se o cartão foi descartado. Defina como `true` para marcar o cartão como descartado. Se um cartão já estiver marcado como descartado, ele não poderá ser marcado como descartado novamente. |
| `isControl()` | Retorna um booleano indicando se este cartão é um cartão de controle e não deve ser renderizado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelo de cartão base #base-card-for-android" }

### Somente imagem {#banner-image-card-for-android}

Os [cartões somente imagem](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) são imagens clicáveis em tamanho completo.

| Propriedade | Descrição |
|---|---|
| `getImageUrl()` | Retorna a URL da imagem do cartão. |
| `getUrl()` | Retorna a URL que é aberta após o clique no cartão. Pode ser uma URL HTTP(s) ou uma URL de protocolo. |
| `getDomain()` | Retorna o texto do link para a URL da propriedade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Somente imagem #banner-image-card-for-android" }

### Imagem com legenda {#captioned-image-card-for-android}

Os [cartões de imagem com legenda](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) são imagens clicáveis em tamanho completo com texto descritivo acompanhante.

| Propriedade | Descrição |
|---|---|
| `getImageUrl()` | Retorna a URL da imagem do cartão. |
| `getTitle()` | Retorna o texto do título do cartão. |
| `getDescription()` | Retorna o texto do corpo do cartão. |
| `getUrl()` | Retorna a URL que é aberta após o clique no cartão. Pode ser uma URL HTTP(s) ou uma URL de protocolo. |
| `getDomain()` | Retorna o texto do link para a URL da propriedade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Imagem com legenda #captioned-image-card-for-android" }

### Clássico {#text-Announcement-card-for-android}

Um cartão clássico sem imagem resulta em um [cartão de anúncio de texto](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). Se uma imagem for incluída, você receberá um [cartão de notícia curta](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

| Propriedade | Descrição |
|---|---|
| `getTitle()` | Retorna o texto do título do cartão. |
| `getDescription()` | Retorna o texto do corpo do cartão. |
| `getUrl()` | Retorna a URL que é aberta após o clique no cartão. Pode ser uma URL HTTP(s) ou uma URL de protocolo. |
| `getDomain()` | Retorna o texto do link para a URL da propriedade. |
| `getImageUrl()` | Retorna a URL da imagem do cartão, aplicável apenas ao cartão clássico de notícia curta. |
| `isDismissed` | Retorna um booleano que indica se o cartão foi descartado. Defina como `true` para marcar o cartão como descartado. Se um cartão já estiver marcado como descartado, ele não poderá ser marcado como descartado novamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clássico #text-Announcement-card-for-android" }

## Métodos de cartão {#card-methods}

Todos os objetos do modelo de dados [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) oferecem os seguintes métodos de análise de dados para registrar eventos de usuário nos servidores da Braze.

| Método | Descrição |
|---|---|
| `logImpression()` | Registra manualmente uma impressão na Braze para um cartão específico. |
| `logClick()` | Registra manualmente um clique na Braze para um cartão específico. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos de cartão" }

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/content_cards.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/content_cards.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/content_cards.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/content_cards.md %}
{% endsdktab %}

{% sdktab tvos %}
## Pré-requisitos

Antes de usar os Content Cards, integre o [SDK Swift da Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) ao seu app. Em seguida, conclua as etapas para configurar seu app tvOS.

{% alert important %}
Implemente sua própria interface personalizada, pois os Content Cards são compatíveis via UI headless usando o SDK Swift&#8212;que não inclui nenhuma UI ou visualização padrão para tvOS.
{% endalert %}

## Configurando seu app tvOS {#setting-up-your-tvos-app}

### Etapa 1: Criar um novo app iOS {#step-1-create-a-new-ios-app}

Na Braze, selecione **Settings** > **App Settings** e, em seguida, selecione **Add App**. Insira um nome para o seu app tvOS, selecione **iOS**&#8212;_não tvOS_&#8212;e selecione **Add App**.

![Caixa de diálogo Adicionar app na Braze com a plataforma iOS selecionada para registrar um app tvOS.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Se você marcar a caixa de seleção **tvOS**, não será possível personalizar os Content Cards para tvOS.
{% endalert %}

### Etapa 2: Obter a chave de API do seu app {#step-2-get-your-apps-api-key}

Nas configurações do app, selecione seu novo app tvOS e anote a chave de API do app. Use essa chave para configurar seu app no Xcode.

![Configurações do app para um app tvOS mostrando a chave de API usada para integração do SDK.]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Etapa 3: Integrar o BrazeKit {#step-3-integrate-brazekit}

Use a chave de API do seu app para integrar o [SDK Swift da Braze](https://github.com/braze-inc/braze-swift-sdk) ao seu projeto tvOS no Xcode. Você só precisa integrar o BrazeKit do SDK Swift da Braze.

### Etapa 4: Criar sua interface personalizada {#step-4-create-your-custom-ui}

Como a Braze não fornece uma UI padrão para Content Cards no tvOS, personalize-a você mesmo. Para um passo a passo completo, consulte nosso tutorial: [Personalizando Content Cards para tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). Para um projeto de exemplo, consulte os [exemplos do SDK Swift da Braze](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/content_cards.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/content_cards.md %}
{% endsdktab %}
{% endsdktabs %}