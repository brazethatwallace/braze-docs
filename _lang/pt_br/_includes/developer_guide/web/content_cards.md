{% multi_lang_include archive/web-v4-rename.md %}

## Pré-requisitos {#prerequisites}

Antes de usar os Content Cards, é necessário [integrar o SDK da Braze para web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) ao seu app. No entanto, nenhuma configuração adicional é necessária. Para criar sua própria interface, consulte o [guia de personalização de Content Cards]({{site.baseurl}}/developer_guide/content_cards).

{% alert note %}
Alguns bloqueadores de anúncios e extensões de privacidade do navegador podem bloquear o script do SDK da Braze para web ou solicitações de rede relacionadas, o que pode impedir o carregamento dos Content Cards. Se você estiver usando o método de integração via CDN, considere mudar para o [método de integração via NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web), que armazena as bibliotecas do SDK localmente no seu website e pode evitar alguns problemas relacionados a bloqueadores de anúncios.
{% endalert %}

## Interface padrão do feed {#standard-feed-ui}

Para usar a interface de Content Cards incluída, você precisa especificar onde exibir o feed no seu site.

Neste exemplo, temos um `<div id="feed"></div>` no qual queremos posicionar o feed de Content Cards. Usaremos três botões para ocultar, exibir ou alternar (ocultar ou exibir com base no estado atual) o feed.

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script>
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");

   toggle.onclick = function(){
      braze.toggleContentCards(feed);
   }

   hide.onclick = function(){
      braze.hideContentCards();
   }

   show.onclick = function(){
      braze.showContentCards(feed);
   }
</script>
```

Ao usar os métodos `toggleContentCards(parentNode, filterFunction)` e `showContentCards(parentNode, filterFunction)`, se nenhum argumento for fornecido, todos os Content Cards serão exibidos em uma barra lateral com posição fixa na página. Caso contrário, o feed será posicionado no `parentNode` especificado.

| Parâmetros | Descrição |
|---|---|
| `parentNode` | O nó HTML no qual os Content Cards serão renderizados. Se o nó pai já tiver uma visualização de Content Cards da Braze como descendente direto, os Content Cards existentes serão substituídos. Por exemplo, você deve passar `document.querySelector(".my-container")`. |
| `filterFunction` | Uma função de filtro ou classificação para os cartões exibidos nesta visualização. Invocada com o array de objetos `Card`, classificados por `{pinned, date}`. Espera-se que retorne um array de objetos `Card` classificados para renderizar para este usuário. Se omitida, todos os cartões serão exibidos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Interface padrão do feed" }

[Consulte a documentação de referência do SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) para saber mais sobre a alternância de Content Cards.

## Testando Content Cards na web {#testing-content-cards-on-the-web}

Você pode testar a integração dos Content Cards usando as ferramentas de desenvolvedor do seu navegador.

1. Crie uma Campaign de Content Cards e direcione-a ao seu usuário teste.
2. Faça login no website que possui a integração do Web SDK.
3. Abra o console do navegador. No Chrome, clique com o botão direito na página, selecione **Inspecionar** e depois selecione a guia **Console**.
4. Execute estes comandos no console:
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## Tipos de cartão e propriedades {#card-types-and-properties}

O modelo de dados dos Content Cards está disponível no Web SDK e oferece os seguintes tipos de Content Cards: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) e [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Cada tipo herda propriedades comuns de um modelo base [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) e possui as seguintes propriedades adicionais.

{% alert tip %}
Para registrar dados de Content Cards, consulte [Registro de análise de dados]({{site.baseurl}}/developer_guide/content_cards/logging_analytics).
{% endalert %}

### Modelo base do cartão {#base-card-model}

Todos os Content Cards possuem essas propriedades compartilhadas:

| Propriedade | Descrição |
|---|---|
| `expiresAt` | O timestamp UNIX do momento de expiração do cartão. |
| `extras` | (Opcional) Dados de par chave-valor formatados como um objeto string com um valor string. |
| `id` | (Opcional) O ID do cartão. Ele é enviado de volta à Braze junto com eventos para fins de análise de dados. |
| `pinned` | Essa propriedade reflete se o cartão foi configurado como "fixado" no dashboard. |
| `updated` | O timestamp UNIX de quando este cartão foi modificado pela última vez. |
| `viewed` | Essa propriedade reflete se o usuário visualizou o cartão ou não. |
| `isControl` | Essa propriedade é `true` quando um cartão é um grupo de "controle" dentro de um teste A/B. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelo base do cartão" }

### Apenas imagem {#image-only}

Os cartões [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) são imagens clicáveis em tamanho completo.

| Propriedade | Descrição |
|---|---|
| `aspectRatio` | A proporção da imagem do cartão, servindo como uma referência antes que o carregamento da imagem seja concluído. Essa propriedade pode não estar disponível em determinadas circunstâncias. |
| `categories` | Essa propriedade serve exclusivamente para organização na sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se este cartão já foi clicado neste dispositivo. |
| `created` | O timestamp UNIX do momento de criação do cartão na Braze. |
| `dismissed` | Essa propriedade indica se este cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão. |
| `linkText` | O texto de exibição para a URL. |
| `url` | A URL que será aberta após o cartão ser clicado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Apenas imagem" }

### Imagem com legenda {#captioned-image}

Os cartões [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) são imagens clicáveis em tamanho completo com texto descritivo acompanhante.

| Propriedade | Descrição |
|---|---|
| `aspectRatio` | A proporção da imagem do cartão, servindo como uma referência antes que o carregamento da imagem seja concluído. Essa propriedade pode não estar disponível em determinadas circunstâncias. |
| `categories` | Essa propriedade serve exclusivamente para organização na sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se este cartão já foi clicado neste dispositivo. |
| `created` | O timestamp UNIX do momento de criação do cartão na Braze. |
| `dismissed` | Essa propriedade indica se este cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão. |
| `linkText` | O texto de exibição para a URL. |
| `title` | O texto do título deste cartão. |
| `url` | A URL que será aberta após o cartão ser clicado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Imagem com legenda" }

### Clássico {#classic}

O modelo [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) pode conter uma imagem sem texto ou um texto com imagem.

| Propriedade | Descrição |
|---|---|
| `aspectRatio` | A proporção da imagem do cartão, servindo como uma referência antes que o carregamento da imagem seja concluído. Essa propriedade pode não estar disponível em determinadas circunstâncias. |
| `categories` | Essa propriedade serve exclusivamente para organização na sua implementação personalizada; essas categorias podem ser definidas no criador do dashboard. |
| `clicked` | Essa propriedade indica se este cartão já foi clicado neste dispositivo. |
| `created` | O timestamp UNIX do momento de criação do cartão na Braze. |
| `description` | O texto do corpo deste cartão. |
| `dismissed` | Essa propriedade indica se este cartão foi descartado. |
| `dismissible` | Essa propriedade reflete se o usuário pode descartar o cartão, removendo-o da visualização. |
| `imageUrl` | A URL da imagem do cartão. |
| `linkText` | O texto de exibição para a URL. |
| `title` | O texto do título deste cartão. |
| `url` | A URL que será aberta após o cartão ser clicado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Clássico" }

### Formatos de imagem {#image-formats}

As imagens dos Content Cards (incluindo GIFs) são renderizadas usando tags HTML `<img>` padrão. O suporte a GIFs depende das capacidades do navegador do usuário e não exige uma versão mínima do Web SDK. Todos os navegadores modernos suportam a reprodução de GIFs nativamente.

## Grupo de controle {#control-group}

Se você usar o feed padrão de Content Cards, as impressões e os cliques serão rastreados automaticamente.

Se você usar uma integração personalizada para Content Cards, será necessário [registrar impressões]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) quando um cartão de controle teria sido exibido. Como parte desse processo, certifique-se de lidar com cartões de controle ao registrar impressões em um teste A/B. Esses cartões ficam em branco e, embora não sejam vistos pelos usuários, você ainda deve registrar impressões para comparar o desempenho deles com os cartões que não são de controle.

Para determinar se um Content Card está no grupo de controle de um teste A/B, verifique a propriedade `card.isControl` (Web SDK v4.5.0+) ou se o cartão é uma instância de `ControlCard` (`card instanceof braze.ControlCard`).

## Métodos de cartão {#card-methods}

### Métodos padrão do feed {#default-feed-methods}

Use estes métodos ao exibir Content Cards usando a interface padrão do feed da Braze:

| Método | Descrição |
|---|---|
| [`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards) | Exibe o feed padrão de Content Cards. Renderiza os cartões em um elemento HTML `parentNode` fornecido, ou como uma barra lateral de posição fixa se nenhum elemento for informado. Aceita uma `filterFunction` opcional para classificar ou filtrar cartões antes da exibição. |
| [`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards) | Oculta o feed padrão de Content Cards, caso esteja sendo exibido no momento. |
| [`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) | Exibe o feed padrão de Content Cards se estiver oculto, ou oculta se estiver visível. Se você precisar exibir vários feeds de Content Cards simultaneamente, use `showContentCards` e `hideContentCards` em vez disso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos padrão do feed" }

### Métodos de feed personalizado {#custom-feed-methods}

Use estes métodos ao construir sua própria interface de Content Cards:

| Método | Descrição |
|---|---|
| [`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates) | Registra uma função de retorno de chamada que é invocada sempre que os Content Cards são atualizados para o usuário atual, como no início da sessão. Use este método como a forma principal de receber dados de cartão para o seu feed personalizado. Deve ser chamado antes de `openSession()` para receber atualizações na sessão inicial. |
| [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) | Retorna todos os cartões disponíveis no momento a partir da atualização mais recente de Content Cards. Use este método para exibir cartões imediatamente ao carregar a página, sem esperar por uma nova solicitação ao servidor, como quando o usuário retorna a uma página durante uma sessão ativa. |
| [`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh) | Solicita uma atualização imediata dos Content Cards a partir dos servidores da Braze. Por padrão, os cartões são atualizados no início da sessão e quando o feed padrão é reaberto. Use este método para forçar uma atualização em outros momentos, como após uma ação específica do usuário. Esteja ciente dos [limites de frequência]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed#rate-limit). |
| [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions) | Registra eventos de impressão para um array de cartões. Chame este método quando os cartões forem renderizados e visíveis para o usuário. Necessário para relatórios precisos de Campaign ao usar uma interface personalizada, pois as impressões não são rastreadas automaticamente fora do feed padrão. |
| [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick) | Registra um evento de clique para um único cartão. Chame este método quando um usuário interagir com um cartão na sua interface personalizada. Necessário para relatórios precisos de Campaign, pois os cliques não são rastreados automaticamente fora do feed padrão. |
| [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction) | Processa a URL de um cartão e executa a ação de clique configurada, incluindo ações da Braze (URLs `brazeActions://`) e navegação por URL padrão. Chame este método no handler de clique do seu cartão para garantir que os comportamentos ao clicar configurados no dashboard da Braze sejam executados. |
| [`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard) | Descarta um cartão programaticamente, removendo-o do feed do usuário. Use este método para permitir que os usuários descartem cartões na sua interface personalizada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métodos de feed personalizado" }

Para saber mais, consulte a [documentação de referência do SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

## Melhores práticas {#best-practices}

### Chame os métodos na ordem correta {#call-methods-in-the-correct-order}

Para feeds personalizados, os Content Cards são atualizados apenas no início da sessão se `subscribeToContentCardsUpdates()` for chamado antes de `openSession()`. Chame seus métodos da Braze nesta ordem:

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### Use cartões em cache para manter o conteúdo entre carregamentos de página {#use-cached-cards-to-persist-content-across-page-loads}

Como `subscribeToContentCardsUpdates()` invoca seu retorno de chamada apenas quando há novas atualizações (como no início da sessão), os cartões podem desaparecer do seu feed personalizado se o usuário atualizar a página no meio da sessão. Para evitar isso, use `getCachedContentCards()` para renderizar imediatamente os cartões do cache local, junto com a sua inscrição para novas atualizações:

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### Registre a análise de dados para feeds personalizados {#log-analytics-for-custom-feeds}

Ao usar uma interface personalizada, impressões, cliques e descartes não são rastreados automaticamente. Você precisa registrar cada evento manualmente:

- **Impressões:** Chame `logContentCardImpressions([card1, card2, ...])` com um array de objetos de cartão quando os cartões ficarem visíveis para o usuário.
- **Cliques:** Chame `logContentCardClick(card)` quando o usuário interagir com um cartão.
- **Comportamento ao clicar:** Chame `handleBrazeAction(card.url)` para executar a ação configurada ao clicar no cartão (como navegar para uma URL ou registrar um evento personalizado).

{% alert warning %}
O argumento passado para `logContentCardClick()` deve ser um objeto `Card` original da Braze. Se você transformar ou reconstruir os dados do cartão (por exemplo, serializando e desserializando), os cliques não serão registrados e você verá o erro: "card must be a Card object."
{% endalert %}

## Usando o Google Tag Manager {#using-google-tag-manager}

O Google Tag Manager funciona injetando o [CDN da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (uma versão do nosso Web SDK) diretamente no código do seu website, o que significa que todos os métodos do SDK estão disponíveis como se você tivesse integrado o SDK sem o Google Tag Manager, exceto ao implementar Content Cards.

### Configurando Content Cards {#setting-up-content-cards}

{% tabs local %}
{% tab google tag manager %}
Para uma integração padrão do feed de Content Cards, você pode usar uma tag **Custom HTML** no Google Tag Manager. Adicione o seguinte à sua tag Custom HTML, que ativará o feed padrão de Content Cards:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuração de tag no Google Tag Manager de uma tag Custom HTML que exibe o feed de Content Cards.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manual %}
Para mais liberdade na personalização da aparência dos Content Cards e do feed, você pode integrar os Content Cards diretamente no seu website nativo. Existem duas abordagens que você pode adotar: usar a interface padrão do feed ou criar uma interface personalizada do feed.

{% subtabs local %}
{% subtab standard feed %}
Ao implementar a [interface padrão do feed]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration#standard-feed-ui), os métodos da Braze devem ter `window.` adicionado no início do método. Por exemplo, `braze.showContentCards` deve ser usado como `window.braze.showContentCards`.
{% endsubtab %}

{% subtab custom feed %}
Para estilização de [feed personalizado]({{site.baseurl}}/developer_guide/content_cards/creating_cards), as etapas são as mesmas de quando você integrou o SDK sem o GTM. Por exemplo, se você quiser personalizar a largura do feed de Content Cards, pode colar o seguinte no seu arquivo CSS:

{% raw %}
```css
body .ab-feed {
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Atualizando modelos {#upgrading}

Para atualizar para a versão mais recente do Braze Web SDK, siga as três etapas a seguir no seu dashboard do Google Tag Manager:

1. **Atualizar o modelo de tag**<br>Acesse a página **Templates** no seu espaço de trabalho. Você verá um ícone indicando que uma atualização está disponível.<br><br>![Página de Templates mostrando que uma atualização está disponível]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Clique no ícone e, após revisar a alteração, clique em **Accept Update**.<br><br>![Uma tela comparando o modelo de tag antigo e o novo com um botão para aceitar a atualização]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Atualizar o número da versão**<br>Depois que o modelo de tag for atualizado, edite a Braze Initialization Tag e atualize a versão do SDK para a versão `major.minor` mais recente. Por exemplo, se a versão mais recente for `4.1.2`, insira `4.1`. Você pode ver uma lista de versões do SDK no nosso [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Modelo de Braze Initialization com um campo de entrada para alterar a versão do SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA e publicação**<br>Verifique se a nova versão do SDK está funcionando usando a [ferramenta de depuração](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager antes de publicar uma atualização no seu contêiner de tags.

### Solução de problemas {#troubleshooting}

#### Ativar a depuração de tags {#debugging}

Cada modelo de tag da Braze possui uma caixa de seleção opcional **GTM Tag Debugging** que pode ser usada para registrar mensagens de depuração no console JavaScript da sua página web.

![Ferramenta de depuração do Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Entrar no modo de depuração {#enter-debug-mode}

Outra maneira de ajudar a depurar sua integração com o Google Tag Manager é usar o recurso de [modo de prévia](https://support.google.com/tagmanager/answer/6107056) do Google.

Isso ajudará a identificar quais valores estão sendo enviados da camada de dados da sua página web para cada tag da Braze acionada, além de explicar quais tags foram ou não acionadas.

![A página de resumo da Braze Initialization Tag fornece uma visão geral da tag, incluindo informações sobre quais tags foram acionadas.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Verificar o sequenciamento de tags para eventos personalizados {#tag-sequencing}

Se eventos personalizados ou outras ações não estão sendo registrados na Braze, uma causa comum é uma condição de corrida em que uma tag de ação (como **Custom Event** ou **Purchase**) é disparada antes que a tag **Braze Initialization** tenha sido concluída. Para corrigir isso, configure o [sequenciamento de tags](https://support.google.com/tagmanager/answer/6238868) no GTM:

1. Abra a tag de ação que não está registrando corretamente.
2. Em **Advanced Settings** > **Tag Sequencing**, selecione **A tag that fires before \[this tag\]**.
3. Escolha sua tag **Braze Initialization** como a tag de configuração.

Isso garante que o SDK esteja totalmente inicializado antes que qualquer tag de ação tente enviar dados para a Braze.

#### Ativar registro detalhado {#enable-verbose-logging}

Para capturar registros detalhados para solução de problemas, você pode ativar o registro detalhado na sua integração com o Google Tag Manager. Esses registros aparecerão na guia **Console** das [ferramentas para desenvolvedores](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) do seu navegador.

Na sua integração com o Google Tag Manager, navegue até a Braze Initialization Tag e selecione **Enable Web SDK Logging**.

![A página de resumo da Braze Initialization Tag com a opção Enable Web SDK Logging ativada.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md