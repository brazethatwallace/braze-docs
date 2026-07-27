---
nav_title: "HTML personalizado"
article_title: "HTML personalizado"
page_order: 4
page_type: reference
description: "Este artigo fornece uma visão geral das mensagens no app com código personalizado, incluindo métodos JavaScript, rastreamento de botões e uso da pré-visualização interativa de HTML na Braze."
channel:
  - in-app messages
---

# Mensagens no app com HTML personalizado {#custom-html-messages}

> Embora nossas mensagens no app padrão possam ser personalizadas de diversas formas, você pode obter ainda mais controle sobre a aparência das suas campanhas usando mensagens projetadas e criadas com HTML, CSS e JavaScript. Com uma composição simples, você pode desbloquear funcionalidades e identidade visual personalizadas para atender a qualquer necessidade.

Esse tipo de mensagem está disponível no [editor tradicional]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional).

## Como funciona {#how-it-works}

As mensagens no app em HTML permitem maior controle sobre a aparência e o estilo de uma mensagem, incluindo:

- Fontes e estilos personalizados
- Vídeos
- Múltiplas imagens
- Comportamentos ao clicar
- Componentes interativos
- Animações personalizadas

As mensagens HTML personalizadas podem usar os métodos do [JavaScript Bridge](#javascript-bridge) para registrar eventos, definir atributos personalizados, fechar a mensagem e muito mais! Confira nosso [repositório no GitHub](https://github.com/braze-inc/in-app-message-templates), que contém instruções detalhadas sobre como usar e personalizar mensagens no app em HTML de acordo com suas necessidades, além de um conjunto de modelos de mensagens no app em HTML5 para ajudar você a começar.

{% alert note %}
Para ativar mensagens no app em HTML por meio do SDK para web, você deve fornecer a opção de inicialização `allowUserSuppliedJavascript` à Braze: por exemplo, `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Isso é necessário por motivos de segurança, já que mensagens no app em HTML podem executar JavaScript, então exigimos que um mantenedor do site as ative.
{% endalert %}

## JavaScript bridge {#javascript-bridge}

{% include javascript_bridge/reference.md %}

## Ações baseadas em links {#link-based-actions}

Além do JavaScript personalizado, os SDKs da Braze também podem enviar dados de análise com esses atalhos de URL convenientes. Note que esses parâmetros de consulta e esquemas de URL diferenciam maiúsculas de minúsculas.

### Rastreamento de clique em botão (descontinuado) {#button-click-tracking-deprecated}

{% alert warning %}
O uso de `abButtonID` não é compatível com os tipos de mensagem [HTML com prévia]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview). Para saber mais, consulte nosso [guia de upgrade]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#html-upload-with-preview).
{% endalert %}

Para registrar cliques em botões na análise de mensagens no app, você pode adicionar `abButtonId` como parâmetro de consulta a qualquer deep link, URL de redirecionamento ou elemento âncora `<a>`. Use `?abButtonId=0` para registrar um clique no "Botão 1" e `?abButtonId=1` para registrar um clique no "Botão 2".

Assim como outros parâmetros de URL, o primeiro parâmetro deve começar com um ponto de interrogação `?`, enquanto os parâmetros subsequentes devem ser separados por um "e" comercial `&`.

#### Exemplos de URLs {#example-urls}

- `https://example.com/?abButtonId=0` - Clique no Botão 1
- `https://example.com/?abButtonId=1` - Clique no Botão 2
- `https://example.com/?utm_source=braze&abButtonId=0` - Clique no Botão 1 com outros parâmetros de URL existentes
- `myApp://deep-link?page=home&abButtonId=1` - Deep link mobile com clique no Botão 2
- `<a href="https://example.com/?abButtonId=1">` - Elemento âncora `<a>` com clique no Botão 2

{% alert note %}
As mensagens no app suportam apenas cliques no Botão 1 e no Botão 2. URLs que não especificam um desses dois IDs de botão serão registradas como "cliques no corpo" genéricos.
{% endalert %}

### Abrir link em nova janela (somente mobile) {#open-link-in-new-window-mobile-only}

Para abrir links fora do seu app em uma nova janela, defina `?abExternalOpen=true`. A mensagem será fechada antes de abrir o link.

Para deep linking, a Braze abrirá sua URL independentemente do valor de `abExternalOpen`.

### Abrir como deep link (somente mobile) {#open-as-deeplink-mobile-only}

Para que a Braze trate seu link HTTP ou HTTPS como um deep link, defina `?abDeepLink=true`.

Quando esse parâmetro de consulta está ausente ou definido como `false`, a Braze tentará abrir o link web em um navegador web interno dentro do app host.

### Fechar mensagem no app {#close-in-app-message}

Para fechar uma mensagem no app, você pode usar o método JavaScript `brazeBridge.closeMessage()`.

Por exemplo, `<a onclick="brazeBridge.closeMessage()" href="#">Fechar</a>` fechará a mensagem no app.

## Upload de HTML com prévia {#html-upload-with-preview}

Ao criar mensagens no app com HTML personalizado, você pode visualizar seu conteúdo interativo diretamente na Braze.

O painel de prévia de mensagem do editor mostra uma prévia realista que renderiza o JavaScript incluído na sua mensagem. Você pode visualizar e interagir com suas mensagens personalizadas no painel de prévia clicando na paginação, enviando formulários ou pesquisas, assistindo animações JavaScript e muito mais!

![Interagindo com a prévia de HTML ao deslizar entre páginas.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Quaisquer métodos JavaScript `brazeBridge` que você usar no seu HTML não atualizarão perfis de usuário durante a prévia no dashboard.
{% endalert %}

### Criando uma campanha {#instructions}

#### Arquivos de ativos {#asset-files}

Ao criar mensagens no app com código personalizado usando upload de HTML, você pode fazer upload de ativos da campanha para a [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) para referenciá-los na sua mensagem.

Os seguintes tipos de arquivo são compatíveis para upload:

| Tipo de arquivo       | Extensão do arquivo               |
| :-------------------- | :-------------------------------- |
| Arquivos de fonte      | `.ttf`, `.woff`, `.otf`, `.woff2` |
| Imagens SVG            | `.svg`                            |
| Arquivos JavaScript    | `.js`                             |
| Arquivos CSS           | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Arquivos de ativos" }

A Braze recomenda fazer upload de ativos para a biblioteca de mídia por dois motivos:

1. Ativos adicionados a uma campanha pela biblioteca de mídia permitem que suas mensagens sejam exibidas mesmo quando o usuário está offline ou com uma conexão de internet ruim.
2. Ativos enviados para a Braze podem ser reutilizados em diferentes campanhas.

##### Adicionando arquivos de ativos {#adding-asset-files}

Você pode adicionar ativos novos ou existentes à sua campanha.

Para adicionar novos ativos à sua campanha, use a seção de arrastar e soltar para fazer upload de um arquivo. Ativos adicionados nesta seção também serão automaticamente adicionados à biblioteca de mídia. Para adicionar ativos que você já enviou para a biblioteca de mídia, selecione **Adicionar da Biblioteca de Mídia**.

Depois que seus ativos forem adicionados, eles aparecerão na seção **Ativos para esta campanha**.

Se o nome de um ativo corresponder ao de um ativo HTML local, ele será substituído automaticamente (por exemplo, `cat.png` é enviado e `<img src="cat.png" />` existe).

Caso contrário, passe o cursor sobre um ativo da lista e selecione <i class="fas fa-copy"></i> **Copiar** para copiar a URL do arquivo para a área de transferência. Em seguida, cole a URL do ativo copiado no seu HTML como faria normalmente ao referenciar um ativo remoto.

### Editor de HTML {#html-editor}

As alterações que você faz no HTML são renderizadas automaticamente no painel de prévia conforme você digita. Quaisquer métodos JavaScript [`brazeBridge`](#bridge) que você usar no seu HTML não atualizarão perfis de usuário durante a prévia no dashboard.

{% alert tip %}
Você pode selecionar <i class="fa-solid fa-magnifying-glass" aria-label="Pesquisar"></i> **Pesquisar** no editor de HTML para buscar dentro do seu código!
{% endalert %}

### Rastreamento de botões {#button-tracking-improvements}

Você pode rastrear o desempenho dentro da sua mensagem no app com código personalizado usando o método JavaScript [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types). Isso permite rastrear programaticamente "Botão 1", "Botão 2" e "Cliques no corpo" usando `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` ou `brazeBridge.logClick()`, respectivamente.

| Cliques    | Método                       |
| ---------- | ---------------------------- |
| Botão 1    | `brazeBridge.logClick('0')` |
| Botão 2    | `brazeBridge.logClick('1')` |
| Clique no corpo | `brazeBridge.logClick()`    |
| Rastreamento de botão personalizado | `brazeBridge.logClick('your custom name here')` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rastreamento de botões" }

{% alert note %}
Este método de rastreamento de botões substitui os métodos anteriores de rastreamento automático de cliques (como `?abButtonId=0`), que foram removidos.
{% endalert %}

Use [`brazeBridge.logClick(button_id)`](#button-tracking-improvements) para mensagens HTML com prévia quando você precisar de mais de dois botões rastreados. Botão 1 e Botão 2 correspondem a `'0'` e `'1'`; botões adicionais usam IDs personalizados (até 100 IDs únicos por campanha). Para restrições de caracteres em IDs de botões, consulte [Rastreamento de botões](#button-tracking-improvements).

### Solução de problemas com links HTML personalizados e comportamento de fechamento {#troubleshoot-custom-html-links-and-close-behavior}

#### Cliques no botão não abrem o link {#button-clicks-do-not-open-the-link}

Se um botão na sua mensagem no app com HTML personalizado não carregar ao ser clicado, verifique se o link usa uma URL válida ou um esquema de deep link compatível. URLs malformadas ou esquemas personalizados não compatíveis podem impedir que a ação de clique seja concluída.

#### Cliques no corpo ao fechar a mensagem {#body-clicks-when-closing-the-message}

Chamar `brazeBridge.closeMessage()` fecha a mensagem, mas não registra análises por conta própria. Para registrar um clique no corpo quando o usuário fecha a mensagem, chame `brazeBridge.logClick()` antes de `brazeBridge.closeMessage()` para que o registro de cliques permaneça consistente entre plataformas.

### Alterações incompatíveis com versões anteriores {#backward-incompatible-changes}

1. O deep link `braze://close`, que era anteriormente compatível com apps móveis, foi removido em favor do JavaScript `brazeBridge.closeMessage()`. Isso permite mensagens HTML multiplataforma, já que a web não é compatível com deep links.
2. O rastreamento automático de cliques, que usava `?abButtonId=0` para IDs de botões, e o rastreamento de "clique no corpo" em botões de fechar foram removidos. Os exemplos de código a seguir mostram como alterar seu HTML para usar nossos novos métodos JavaScript de rastreamento de cliques:

   | Antes | Depois |
   |:-------- |:------------|
   |<code>&lt;a href="braze://close"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="braze://close?abButtonId=0"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="app://deeplink?abButtonId=0">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="app://deeplink" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "braze://close?abButtonId=1"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Alterações incompatíveis com versões anteriores" }