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

> Com o editor de arrastar e soltar, você pode criar mensagens no app totalmente personalizadas em Campaigns ou Canvas usando a experiência de edição de arrastar e soltar. Para saber mais sobre os blocos de construção disponíveis no editor, consulte [Blocos do editor]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages).


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

Se você quiser usar seus modelos HTML personalizados existentes ou modelos criados por terceiros, eles precisam ser recriados no editor de arrastar e soltar.

Não tem certeza se sua mensagem no app deve ser enviada usando uma campanha ou um [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas é melhor para jornadas de usuário com várias etapas. Depois de selecionar onde construir sua mensagem, vamos mergulhar nas etapas para criar uma mensagem no app com arrastar e soltar.

## Pré-requisitos {#prerequisites}

### Requisitos do SDK {#sdk-requirements}

| Versão mínima do SDK                                                          | Versão recomendada do SDK                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos do SDK" }

{% details Mais informações sobre SDKs mínimos %}

Mensagens criadas usando o editor de arrastar e soltar só podem ser enviadas para usuários nas versões mínimas do SDK (veja a tabela acima). Se um usuário não tiver atualizado seu aplicativo (ou seja, está em uma versão mais antiga do SDK), ele não receberá a mensagem no app.

Para aproveitar todos os recursos disponíveis no editor de arrastar e soltar, atualize seus SDKs para as versões recomendadas. Isso permite que você aproveite os seguintes recursos adicionais:

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
- Se você estiver usando o Google Tag Manager, deve ativar "Allow HTML In-App Messages" na configuração do GTM.

## Etapa 1: Criar uma mensagem no app {#step-1-create-an-in-app-message}

Crie uma nova mensagem no app ou etapa do Canvas e selecione **Drag-And-Drop Editor** como sua experiência de edição.

## Etapa 2: Selecionar seu modelo {#step-2-select-your-template}

Após selecionar o editor de arrastar e soltar como sua experiência de edição, você pode escolher:

- Começar com um modelo modal em branco
- Usar um modelo de mensagem no app de arrastar e soltar da Braze
- Selecionar um modelo salvo de mensagem no app de arrastar e soltar

Selecione **Build message** para começar a projetar sua mensagem no app no editor de arrastar e soltar.

![A seção de modelos da Braze onde você pode escolher um modelo básico, de imagem de fundo, de captura de número de telefone ou em branco.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

Você também pode acessar todos os modelos na seção **Templates** do dashboard.

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

## Etapa 4: Criar e projetar sua mensagem no app {#step-4-build-and-design-your-in-app-message}

É aqui que sua mensagem ganha vida, vestida com o estilo exclusivo da sua marca. Usando uma combinação de blocos do editor e configurações de estilo, você pode personalizar e projetar sua mensagem no app.

- Para uma lista de blocos do editor disponíveis e suas propriedades, consulte [Blocos do editor]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages).
- Para ajuda na personalização da aparência da sua mensagem, confira [Configurações de estilo]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings/).
- Para práticas recomendadas na criação de mensagens da direita para a esquerda, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/).

## Etapa 5: Testar sua mensagem no app {#step-5-test-your-in-app-message}

A seção **Preview & Test** permite pré-visualizar suas mensagens no app em diferentes dispositivos e enviar uma mensagem de teste para o seu dispositivo. Aqui, você pode garantir que os detalhes estejam alinhados em todas as suas plataformas para sua campanha de mensagem no app de arrastar e soltar.

É importante sempre testar suas mensagens no app antes de enviar suas campanhas para ajudar a visualizar como sua mensagem final ficará da perspectiva do usuário.

### Pré-visualizar mensagem como um usuário {#preview-message-as-a-user}

{% alert warning %}
Para enviar um teste para grupos de teste de conteúdo ou usuários individuais, o push deve estar ativado nos seus dispositivos de teste antes do envio.
{% endalert %}

Você pode pré-visualizar mensagens na guia **Preview & Test**, como se fosse um usuário. Você pode selecionar um usuário específico, um usuário aleatório ou criar um usuário personalizado:

- **Random User:** a Braze selecionará aleatoriamente um usuário do banco de dados e pré-visualizará a mensagem no app com base nos atributos ou informações de eventos desse usuário.
- **Select User:** você pode selecionar um usuário específico com base no endereço de e-mail ou `external_id`. A mensagem no app será pré-visualizada com base nos atributos e informações de eventos desse usuário.
- **Custom User:** você pode personalizar um usuário. A Braze oferecerá campos para todos os atributos e eventos disponíveis. Insira qualquer informação que você gostaria de ver no e-mail de pré-visualização.

### Lista de verificação de teste {#test-checklist}

Considere as seguintes perguntas ao testar sua mensagem no app:

- Você testou a mensagem em diferentes dispositivos?
- As imagens e mídias aparecem e funcionam como esperado?
- O Liquid funciona como esperado? Você considerou um valor de atributo padrão caso o Liquid não retorne nenhuma informação?
- Seu texto está claro, conciso e correto?
- Seus botões direcionam o usuário para onde ele deveria ir?

## Perguntas frequentes {#frequently-asked-questions}

### Por que os cliques no corpo não aparecem na minha página de análise de dados? {#why-are-body-clicks-not-appearing-on-my-analytics-page}

Os cliques no corpo não são coletados automaticamente para mensagens no app criadas com o editor de arrastar e soltar. Para mais detalhes, consulte os changelogs do SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) e [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

### Posso segmentar com base em cliques de botão? {#can-i-segment-based-on-button-clicks}

Sim, você pode segmentar com base em cliques de botão para até dois botões na sua mensagem. Para isso, defina o **Identifier for Reporting** dos seus botões como "0" e "1", que corresponderão aos filtros de segmentação "Clicked in-app message button 1" e "Clicked in-app message button 2", respectivamente.

![O campo "Identifier for Reporting" com o valor "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

### Posso personalizar minha mensagem no app usando HTML ou JavaScript personalizados ou transferir mensagens HTML existentes para o editor? {#can-i-customize-my-in-app-message-using-custom-html-or-javascript-or-transfer-existing-html-messages-into-the-editor}

Você não pode transferir diretamente mensagens HTML existentes para o editor, mas pode inserir HTML, CSS e JavaScript brutos em um bloco de código personalizado. Você pode usar blocos de código personalizado para incorporar vídeos de terceiros e Liquid avançado, como Conteúdo conectado ou instruções condicionais.

### Como posso criar uma mensagem no app do tipo slideup? {#how-can-i-create-a-slideup-in-app-message}

Atualmente, o editor é limitado apenas a mensagens modais e de tela cheia. Você pode alternar entre os tipos de exibição na seção **Message container** do painel **Message styles**.

### Posso salvar minha mensagem no app como modelo depois de criá-la na minha campanha ou Canvas? {#can-i-save-my-in-app-message-as-a-template-after-i-build-it-within-my-campaign-or-canvas}

Sim. Para qualquer mensagem no app que você queira reutilizar em uma futura campanha ou etapa do Canvas, você pode salvá-la como um modelo personalizado usando o botão **Save as template**, disponível após sair do editor. Antes de salvá-la como modelo, você deve primeiro lançar a campanha OU salvá-la como rascunho.

![Uma pré-visualização de uma mensagem no app para um tour de produto.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

Você também pode criar e salvar modelos de mensagens no app acessando **Templates** > **In-App Message Templates**.