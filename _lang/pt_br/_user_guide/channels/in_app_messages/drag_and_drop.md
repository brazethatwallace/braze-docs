---
nav_title: Editor de arrastar e soltar
article_title: Criar uma mensagem no app no editor de arrastar e soltar
alias: /iam_drag_and_drop/
page_order: 1
description: "Este artigo de referência aborda a criação de uma mensagem no app com o editor de arrastar e soltar, pré-requisitos, detalhes criativos e mais."
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-level-styles'
  add-a-custom-font: '/docs/user_guide/channels/in_app_messages/customize/style_settings#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/channels/in_app_messages/customize/style_settings#message-components'
  creative-details: '/docs/user_guide/channels/in_app_messages/customize/style_settings#creative-details'
---

# Criar uma mensagem no app com arrastar e soltar {#create-an-in-app-message-with-drag-and-drop}

> Com o editor de arrastar e soltar, você pode criar mensagens no app totalmente personalizadas em Campaigns ou Canvas usando a experiência de edição de arrastar e soltar. Para saber mais sobre os blocos de construção disponíveis no editor, consulte [Blocos do editor]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages).


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

Se você quiser usar seus modelos HTML personalizados existentes ou modelos criados por terceiros, eles precisam ser recriados no editor de arrastar e soltar.

Não tem certeza se sua mensagem no app deve ser enviada usando uma campanha ou um [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas)? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas é melhor para jornadas de usuário com várias etapas. Depois de selecionar onde construir sua mensagem, vamos mergulhar nas etapas para criar uma mensagem no app com arrastar e soltar.

## Pré-requisitos {#prerequisites}

### Requisitos do SDK {#sdk-requirements}

| Versão mínima do SDK                                                          | Versão recomendada do SDK                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos do SDK" }

{% details Mais informações sobre SDKs mínimos %}

Mensagens criadas usando o editor de arrastar e soltar só podem ser enviadas para usuários nas versões mínimas do SDK (consulte a tabela na seção anterior). Se um usuário não tiver atualizado seu aplicativo (ou seja, estiver em uma versão mais antiga do SDK), ele não receberá a mensagem no app.

Para aproveitar todos os recursos disponíveis no editor de arrastar e soltar, atualize seus SDKs para as versões recomendadas do SDK. Isso permite que você aproveite os seguintes recursos adicionais:

- Links de texto que não dispensam a mensagem
- Ação de botão para solicitar push primer

A seguir estão os requisitos mínimos individuais do SDK para esses recursos:

| Links de texto*                                                         | Solicitar push primer                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos do SDK" }

*Se você incluir um link na sua mensagem no app que redireciona para uma URL e o usuário final não estiver nas versões mínimas do SDK especificadas, selecionar o link fechará a mensagem e o usuário não poderá retornar à mensagem para enviar o formulário.

{% enddetails %}

### Pré-requisitos adicionais {#additional-prerequisites}

- Para o SDK web, a opção de inicialização [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) deve ser definida como `true`. A opção `enableHtmlInAppMessages` também permite que essas mensagens funcionem, mas está obsoleta e deve ser atualizada para `allowUserSuppliedJavascript`.
- Se você estiver usando o Google Tag Manager, será necessário ativar "Allow HTML In-App Messages" na configuração do GTM.

## Etapa 1: Crie uma mensagem no app {#step-1-create-an-in-app-message}

Crie uma nova mensagem no app ou etapa do Canvas e selecione **Editor de arrastar e soltar** como sua experiência de edição.

## Etapa 2: Selecione seu modelo {#step-2-select-your-template}

Depois de selecionar o editor de arrastar e soltar como sua experiência de edição, você pode escolher:

- Começar com um modelo modal em branco
- Usar um modelo de mensagem no app de arrastar e soltar da Braze
- Selecionar um modelo salvo de mensagem no app de arrastar e soltar

Selecione **Criar mensagem** para começar a projetar sua mensagem no app no editor de arrastar e soltar.

![A seção de modelos da Braze onde você pode escolher um modelo básico, de imagem de fundo, de captura de número de telefone ou em branco.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

Você também pode acessar todos os modelos na seção **Modelos** do dashboard.

## Etapa 3: Adicionar páginas adicionais (opcional) {#multi-page}

Adicionar páginas à sua mensagem no app permite guiar os usuários por um fluxo sequencial, como um fluxo de integração ou jornada de boas-vindas. Você pode gerenciar páginas na seção **Pages** da guia **Build**.

![Uma mensagem no app para uma empresa de saúde composta por três páginas.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Adicionando páginas %}

As mensagens no app começam com uma página por padrão. Para adicionar uma nova página:

1. Selecione **+ Add page**.
2. Selecione na lista de modelos personalizados ou fornecidos pela Braze.
3. Dê um nome significativo à página. Isso ajudará quando você conectar as páginas entre si.

{% alert tip %}
Você pode adicionar até 10 páginas por mensagem no app.
{% endalert %}

Para duplicar uma página existente:

1. Passe o mouse sobre a página na lista e selecione <i class="fas fa-ellipsis-vertical" aria-label="Abrir mais opções"></i> **Mais opções**.
2. Selecione **Duplicate**.
3. Dê um nome significativo à página. Isso ajudará quando você conectar as páginas entre si.

{% endtab %}
{% tab Excluindo ou renomeando páginas %}

Para excluir ou renomear uma página:

1. Passe o mouse sobre a página na lista e selecione <i class="fas fa-ellipsis-vertical" aria-label="Abrir mais opções"></i> **Mais opções**.
2. Selecione **Rename** ou **Delete**.

{% endtab %}
{% endtabs %}

### Etapa 3a: Conectar páginas entre si {#step-3a-connect-pages-together}

Mensagens no app com várias páginas são sequenciais, o que significa que os usuários interagem com a mensagem tocando ou clicando para avançar para a próxima página no fluxo.

Para conectar páginas entre si:

1. Selecione sua página inicial.
2. Selecione um elemento de botão ou imagem no canvas.
3. Defina **On-click behavior** como **Go to page**.
4. Selecione a página para a qual deseja vincular a partir da página inicial.
5. Continue até que todas as páginas estejam vinculadas.

![Um usuário está editando o botão de ação principal para ir para a Página 2 da mensagem no app.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Se uma página não estiver vinculada a nenhuma outra página, a mensagem não poderá ser lançada.

{% alert note %}
Os usuários podem selecionar o botão X de fechar para sair da mensagem a qualquer momento. Esse botão não pode ser removido.
{% endalert %}

## Etapa 4: Crie e projete sua mensagem no app {#step-4-build-and-design-your-in-app-message}

É aqui que sua mensagem ganha vida, vestida com o estilo exclusivo da sua marca. Usando uma combinação de blocos do editor e configurações de estilo, você pode personalizar e projetar sua mensagem no app.

- Para ver uma lista dos blocos do editor disponíveis e suas propriedades, consulte [Blocos do editor]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=in-app%20messages).
- Para ajuda na personalização da aparência da sua mensagem, confira [Configurações de estilo]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings).
- Para práticas recomendadas na criação de mensagens da direita para a esquerda, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Etapa 5: Teste sua mensagem no app {#step-5-test-your-in-app-message}

A seção **Prévia e Teste** permite que você visualize suas mensagens no app em diferentes dispositivos e envie uma mensagem de teste para o seu dispositivo. Aqui, você pode garantir que os detalhes estejam alinhados em todas as suas plataformas para sua campanha de mensagem no app com arrastar e soltar.

É importante sempre testar suas mensagens no app antes de enviar suas campanhas para ajudar a visualizar como sua mensagem final ficará na perspectiva do usuário.

### Visualizar mensagem como um usuário {#preview-message-as-a-user}

{% alert warning %}
Para enviar um teste para Grupos de Teste de Conteúdo ou usuários individuais, o push deve estar ativado nos seus dispositivos de teste antes do envio.
{% endalert %}

Você pode visualizar mensagens na guia **Prévia e Teste**, como se fosse um usuário. Você pode selecionar um usuário específico, um usuário aleatório ou criar um usuário personalizado:

- **Usuário aleatório:** a Braze selecionará aleatoriamente um usuário do banco de dados e visualizará a mensagem no app com base nos atributos ou informações de eventos desse usuário.
- **Selecionar usuário:** você pode selecionar um usuário específico com base no endereço de e-mail ou `external_id`. A mensagem no app será visualizada com base nos atributos e informações de eventos desse usuário.
- **Usuário personalizado:** você pode personalizar um usuário. A Braze oferecerá campos para todos os atributos e eventos disponíveis. Insira qualquer informação que você gostaria de ver no e-mail de prévia.

### Lista de verificação de teste {#test-checklist}

Considere as seguintes perguntas ao testar sua mensagem no app:

- Você testou a mensagem em diferentes dispositivos?
- As imagens e mídias aparecem e funcionam como esperado?
- O Liquid funciona como esperado? Você considerou um valor de atributo padrão caso o Liquid não retorne nenhuma informação?
- Seu texto está claro, conciso e correto?
- Seus botões direcionam o usuário para onde ele deveria ir?

## Perguntas frequentes {#frequently-asked-questions}

### Por que os cliques no corpo não estão aparecendo na minha página de análise de dados? {#why-are-body-clicks-not-appearing-on-my-analytics-page}

Os cliques no corpo não são coletados automaticamente para mensagens no app criadas com o editor de arrastar e soltar. Para mais detalhes, consulte os changelogs do SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) e [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

### Posso segmentar com base em cliques de botão? {#can-i-segment-based-on-button-clicks}

Sim, você pode segmentar com base em cliques de botão para até dois botões na sua mensagem. Para isso, defina o **Identifier for Reporting** dos seus botões como "0" e "1", que corresponderão aos filtros de segmentação "Clicked in-app message button 1" e "Clicked in-app message button 2", respectivamente.

![O campo "Identifier for Reporting" com o valor "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

### Posso personalizar minha mensagem no app usando HTML ou JavaScript personalizados, ou transferir mensagens HTML existentes para o editor? {#can-i-customize-my-in-app-message-using-custom-html-or-javascript-or-transfer-existing-html-messages-into-the-editor}

Não é possível transferir diretamente mensagens HTML existentes para o editor, mas você pode inserir HTML, CSS e JavaScript brutos em um bloco de **Custom code**. Você pode usar blocos de **Custom code** para incorporar vídeos de terceiros e Liquid avançado, como Connected Content ou instruções condicionais. Para métodos JavaScript `brazeBridge` e exemplos de rastreamento de cliques, consulte [Mensagens no app com HTML personalizado]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html).

### Por que a visualização do criador do editor de arrastar e soltar pode parecer diferente da mensagem final? {#why-might-the-drag-and-drop-editors-composer-view-look-different-from-the-final-message}

O editor de arrastar e soltar renderiza sua mensagem dentro de um criador e aplica estilos e padrões exclusivos da prévia para que você possa construir e revisar o layout. Esses tratamentos ajudam você a ver a estrutura e o conteúdo de espaço reservado enquanto edita; eles não são incluídos na mensagem que seus usuários recebem.

Exemplos comuns de comportamento exclusivo do editor incluem:

- O editor envolve blocos de **Custom code** em um contêiner `bz-html-code-block` com um `min-height` padrão de `40px`, para que blocos vazios ou curtos permaneçam visíveis enquanto você edita
- Imagens em branco ou que contêm Liquid exibindo um espaço reservado no editor
- Grupos de caixas de seleção e botões de opção que pré-selecionam a primeira opção para que você possa visualizar o estado ativo

Se algo parece diferente apenas no editor, geralmente é um comportamento de prévia. Ao solucionar problemas da mensagem entregue, revise os estilos e a marcação nos blocos da sua mensagem — não o quadro exclusivo do editor ou os padrões de prévia.

### Como posso criar uma mensagem no app do tipo slideup? {#how-can-i-create-a-slideup-in-app-message}

Atualmente, o editor é limitado apenas a mensagens modais e em tela cheia. Você pode alternar entre os tipos de exibição na seção **Message container** do painel **Message styles**.

### Posso salvar minha mensagem no app como modelo depois de criá-la na minha Campaign ou Canvas? {#can-i-save-my-in-app-message-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Sim. Para qualquer mensagem no app que você queira reutilizar em uma Campaign ou etapa do Canvas futura, você pode salvá-la como modelo personalizado usando o botão **Save as template**, disponível após sair do editor. Antes de salvá-la como modelo, você deve primeiro lançar a Campaign OU salvá-la como rascunho.

![Uma prévia de uma mensagem no app para um tour de produto.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

Você também pode criar e salvar modelos de mensagens no app acessando **Content** > **In-App Message**.

### Por que minha sintaxe Liquid está aparecendo como texto simples na minha mensagem no app paginada? {#why-is-my-liquid-syntax-appearing-as-plain-text-in-my-paginated-in-app-message}

Se você está vendo a sintaxe Liquid aparecer como texto simples ao testar uma mensagem no app paginada (em vez do conteúdo personalizado), pode haver um erro de sintaxe Liquid em uma das páginas. Se houver um erro de sintaxe em uma página, isso afeta a renderização do Liquid em todas as páginas da mensagem — as páginas não são independentes.

Para solucionar problemas:

1. Verifique todas as páginas da sua mensagem em busca de erros de sintaxe Liquid. Uma prévia quebrada em uma página não significa que o erro está nessa página — como as páginas não são independentes, o erro de sintaxe pode estar em qualquer lugar da mensagem.
2. Verifique se todas as tags Liquid estão devidamente fechadas e formatadas corretamente.