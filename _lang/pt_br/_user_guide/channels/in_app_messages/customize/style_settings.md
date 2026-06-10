---
nav_title: Configurações de estilo
article_title: "Configurações de estilo de mensagens no app"
description: "Este artigo de referência aborda as opções de estilo disponíveis ao criar uma mensagem no app com o editor de arrastar e soltar."
page_order: 1
---

# Configurações de estilo de mensagens no app {#in-app-message-style-settings}

> A experiência de edição de arrastar e soltar é dividida em duas seções: **Build** e **Preview & Test**. Este artigo aborda o que você precisa saber para trabalhar na guia **Build** do editor e pressupõe que você já [criou uma mensagem no app]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/).

![Guia "Message styles".]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Estilos no nível da mensagem {#message-level-styles}

Você pode definir determinados estilos para serem aplicados em todos os blocos relevantes da sua mensagem no app a partir da guia **Message Styles**. Por exemplo, você pode querer personalizar a fonte de todo o texto ou a cor de todos os links na sua mensagem.

Os estilos nesta seção são usados em toda a sua mensagem, exceto quando você os substitui para um bloco específico. Se a sua mensagem tiver [várias páginas]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/#multi-page), você também pode substituir os estilos no nível da mensagem para páginas individuais, exceto o tipo de exibição e a largura máxima.

Para uma experiência de design mais fácil, recomendamos configurar os estilos no nível da mensagem antes de personalizar os estilos no nível do bloco.

Para retornar à guia **Message Styles** a qualquer momento:

- Clique no botão X de fechar nas propriedades de blocos individuais
- Selecione o contêiner da mensagem, o botão X de fechar da mensagem ou o plano de fundo do editor

### Fontes personalizadas {#custom-fonts}

Aceitamos os seguintes tipos de arquivo para fontes: `.ttf`, `.woff`, `.otf` e `.woff2`. Para saber mais, consulte [Arquivos de ativos]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html/#asset-files).

Você pode adicionar múltiplas variações de uma família de fontes, pois algumas opções de estilo podem não estar disponíveis para fontes personalizadas. Atualmente, não oferecemos suporte para adicionar fontes via URL.

Para adicionar uma fonte personalizada:

1. Acesse a seção **Content** na guia **Message styles**.
2. Clique em **Add custom font**.
3. Faça upload da sua fonte usando a biblioteca de mídia.

{% alert note %}
A fonte no nível da mensagem será aplicada apenas à mensagem atual e a quaisquer mensagens duplicadas, mas não a modelos futuros.
{% endalert %}

## Componentes da mensagem {#message-components}

![Um GIF mostrando a criação de uma mensagem promocional no app.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

O editor de arrastar e soltar usa dois componentes principais para compor mensagens no app: **linhas** e **blocos**. Todos os blocos devem ser colocados em uma linha.

### Botão X de fechar {#close-x-button}

Para mensagens no app do tipo modal e tela cheia, você pode personalizar o botão de fechar exibido como <i class="fa-solid fa-xmark"></i> no canto superior direito da sua mensagem. As opções de personalização incluem posição do botão, tamanho, cor de preenchimento, cor de fundo, estilo da borda e raio da borda.

![Opções para personalizar o botão X de fechar em mensagens no app, incluindo tamanho do botão, cor de preenchimento, cor de fundo, estilo da borda e raio da borda.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### Estilização com span {#span-styling}

Adicionar estilização com span ao texto dentro de mensagens no app permite uma personalização aprimorada da aparência da mensagem, possibilitando o uso de diferentes cores de texto, fontes e tamanhos. A estilização com span oferece aos seus usuários uma experiência mais envolvente e visualmente atraente, direcionando a atenção deles para informações importantes e melhorando a clareza geral da mensagem.

![Opção exibida ao destacar texto em uma mensagem no app. Um pequeno ícone de pincel mostra que você pode envolver com span para estilizar.]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

![Painel lateral de "Span Properties" que permite ao usuário personalizar família da fonte, peso da fonte, tamanho da fonte, espaçamento entre letras e cor do texto.]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### Linhas {#rows}

Linhas são unidades estruturais que definem a composição horizontal de uma seção da mensagem usando células.

![Linhas que você pode adicionar na sua mensagem no app.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Quando uma linha é selecionada, você pode adicionar ou remover o número de colunas necessárias na seção **Column customization** para colocar diferentes elementos de conteúdo lado a lado.

Você também pode deslizar para ajustar o tamanho das colunas existentes.

![Ajustando colunas na seção "Column customization".]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

Como prática recomendada, formate as propriedades de linha e coluna antes de formatar qualquer um dos blocos dentro das linhas. Existem muitos lugares onde você pode ajustar o espaçamento e o alinhamento, então começar pela base facilita a edição ao longo do processo.

#### Imagem de fundo {#background-image}

Você pode adicionar uma imagem de fundo a uma linha no painel **Row properties**. Ative a opção **Background image** e forneça uma URL de imagem ou selecione uma imagem da [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/). Por fim, configure o texto alternativo, o tamanho, a posição e se a imagem se repete para criar padrões ao longo da linha.

![Uma imagem de fundo de linha com uma pizza que tem um padrão de repetição horizontal.]({% image_buster /assets/img_archive/background_row.png %})

### Blocos {#blocks}

Blocos representam diferentes tipos de conteúdo que você pode usar na sua mensagem. Arraste um para dentro de um segmento de linha existente, e ele se ajustará automaticamente à largura da célula.

{% alert tip %}
Antes de adicionar blocos, configure os [estilos no nível da mensagem](#set-message-level-styles) para o contêiner da mensagem, fonte, cores e qualquer outra coisa que você queira personalizar. Depois, você pode personalizar blocos individuais conforme necessário. O **botão de fechar** permanecerá na seção superior da sua mensagem para que os usuários sempre tenham a opção de dispensar a mensagem.
{% endalert %}

![Caixas de arrastar e soltar para selecionar.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Cada bloco tem suas próprias configurações, como controle granular de preenchimento (padding). O painel do lado direito alterna automaticamente para um painel de estilização do elemento de conteúdo selecionado. Para saber mais, consulte [Propriedades dos blocos do editor]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks/?sdktab=in-app%20messages#inappmessages_properties).

Ao criar sua mensagem no app, você pode selecionar uma visualização para celular, tablet ou desktop na barra de ferramentas para pré-visualizar como sua mensagem no app ficará para seus grupos de usuários. Isso garante que seu conteúdo seja responsivo, e você pode fazer os ajustes necessários ao longo do caminho.

## Detalhes criativos {#creative-details}

### Tela cheia em telas maiores {#fullscreen}

Em um tablet ou navegador de desktop, uma mensagem no app em tela cheia ficará centralizada na tela do app. Quaisquer edições na largura máxima da mensagem em tela cheia serão aplicadas apenas a dispositivos tablet e desktop.

![Exemplo de mensagem no app em tela cheia.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Adicionando uma imagem de fundo {#adding-a-background-image}

Você pode adicionar uma imagem ao fundo da sua mensagem a partir da guia **Message styles**.

1. Na área do canvas, selecione o contêiner de fundo. Esta é a seção rolável da sua mensagem.
2. Na guia **Message styles**, ative a opção **Background image**.
3. Adicione uma imagem da sua biblioteca de mídia ou insira a URL onde sua imagem está hospedada.

{% alert tip %}
Se você estiver com dificuldade para selecionar um determinado bloco, pode usar a seta para cima na barra de ferramentas inline do bloco para mover o foco para cada bloco pai.
{% endalert %}

### Adicionando Liquid {#adding-liquid}

![Ícone para adicionar personalização Liquid.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Para adicionar [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) à sua mensagem no app, selecione <i class="fa-solid fa-circle-plus"></i> **Add Personalization** na barra de ferramentas do editor. Aqui, você pode adicionar vários tipos de personalização, como atributos padrão, atributos de dispositivo, atributos personalizados e muito mais.

Em seguida, pegue o snippet Liquid gerado e insira-o na sua mensagem. Após projetar e criar sua mensagem no app, acesse **Preview & Test** para pré-visualizar sua mensagem.

### Usando o Assistente de Copywriting com IA {#using-the-ai-copywriter}

Quando um bloco de texto é selecionado na sua mensagem no app, clique em <i class="fa-solid fa-wand-magic-sparkles" title="Assistente de Copywriting com IA"></i> na barra de ferramentas do bloco para abrir o [Assistente de Copywriting com IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). O Assistente de Copywriting com IA envia um breve nome ou descrição do produto para a ferramenta de geração de texto GPT3 da OpenAI para gerar textos de marketing semelhantes aos escritos por humanos para suas mensagens.

{% alert tip %}
Você pode economizar alguns cliques destacando o texto dentro do bloco antes de clicar no ícone. O texto destacado será adicionado à ferramenta, e o texto será gerado imediatamente.
{% endalert %}

![GIF do Assistente de Copywriting com IA.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Redefinindo estilos para o padrão {#resetting-styles-to-default}

Propriedades que você alterou em relação ao estilo padrão são marcadas com um ponto laranja. Para redefinir uma propriedade específica para seu estilo padrão, passe o mouse sobre o campo e selecione **Reset to default**.

![Ponto laranja que redefine o tamanho do texto para seu tamanho padrão.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

Você também pode redefinir toda a estilização de um elemento selecionado clicando em <i class="fas fa-paintbrush" title="Botão de copiar ou colar estilos"></i> ao lado do nome do painel de propriedades e selecionando **Reset to default styles**.

### Copiando e colando estilos {#copying-and-pasting-styles}

Após fazer alterações na estilização de um elemento, você pode copiar e colar esses estilos em outro elemento. Ao colar estilos, apenas as propriedades relevantes para aquele elemento são aplicadas.

![Menu suspenso com opção de copiar estilos.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. Com o elemento selecionado, clique em <i class="fas fa-paintbrush" title="Copiar ou colar estilos"></i> ao lado do nome do painel de propriedades (por exemplo, se você tiver um botão selecionado, ao lado de "Button properties").
2. Clique em **Copy styles** e selecione o elemento onde deseja aplicar o estilo copiado.
3. Clique em <i class="fas fa-paintbrush" title="Copiar ou colar estilos"></i> novamente e escolha **Paste styles**.

#### Atalhos de teclado {#keyboard-shortcuts}

Você também pode usar atalhos de teclado para copiar e colar estilos:

| Ação | Mac | Windows |
| --- | --- | --- |
| Copiar estilos | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> |
| Colar estilos | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atalhos de teclado" }