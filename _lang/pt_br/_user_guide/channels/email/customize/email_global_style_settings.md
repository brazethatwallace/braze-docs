---
nav_title: "Configurações globais de estilo de e-mail"
article_title: "Configurações globais de estilo de e-mail"
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Este artigo de referência aborda como definir configurações globais de estilo de e-mail no editor de arrastar e soltar para suas Campaigns e Canvas."
tool:
  - Campaigns
  - Canvas
---

# Configurações globais de estilo de e-mail {#email-global-style-settings}

> Com as configurações globais de estilo, você pode personalizar a aparência das suas Campaigns de e-mail e Canvas. Você pode adicionar e personalizar um tema padrão para o editor de arrastar e soltar. Isso inclui editar seus estilos para títulos de e-mail, texto, botões e muito mais. Usar uma combinação dessas configurações pode ajudar a criar uma aparência consistente em todo o seu envio de mensagens por e-mail.

Para editar suas configurações globais de estilo, acesse **Configurações** > **Preferências de e-mail** > **Preferências de e-mail de arrastar e soltar**. Após editar os estilos no editor de e-mail de arrastar e soltar, selecione **Salvar**. Para personalizar ainda mais suas Campaigns de e-mail e Canvas, confira como incorporar [Blocos do editor (e-mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email).

![Seção de configurações globais de estilo de e-mail na guia de configurações do editor de arrastar e soltar.]({% image_buster /assets/img_archive/dnd_global_style_settings.png %})

{% alert note %}
As atualizações feitas nas configurações globais de estilo serão aplicadas a todas as futuras Campaigns de e-mail e Canvas.
{% endalert %}

## Estilo básico {#basic-styling}

Em **Estilo básico**, você pode definir as cores padrão de fundo do e-mail e do conteúdo para suas Campaigns de e-mail e Canvas. Você também pode selecionar uma fonte padrão, adicionar uma fonte personalizada e editar as cores dos links.

![Opções de estilo básico que incluem opções para editar as cores de fundo do e-mail e do conteúdo, nome da fonte padrão e cor padrão do link.]({% image_buster /assets/img_archive/dnd_basic_styling.png %})

## Fonte personalizada {#custom-font}

Com fontes personalizadas, você pode adicionar manualmente uma fonte web para manter a consistência da marca em diversas plataformas de e-mail. Você pode adicionar uma fonte personalizada para cada seção de estilo.

### Requisitos {#requirements}

Antes de adicionar uma fonte personalizada, verifique se o arquivo da fonte atende aos seguintes requisitos:

- O CORS deve estar ativado no servidor que fornece o arquivo da fonte personalizada. Isso geralmente é gerenciado pela sua equipe de TI.
  - O arquivo da fonte personalizada deve ter o cabeçalho: `Access-Control-Allow-Origin: *`
- A URL do arquivo deve apontar para um arquivo CSS (não WOFF ou OTF).
- O nome da fonte personalizada deve corresponder ao nome da font face no arquivo CSS.

Observe que o provedor de fontes personalizadas pode coletar dados pessoais dos seus destinatários. Você deve revisar as políticas do seu provedor de fontes antes de usar.

### Adicionando uma fonte personalizada {#adding-a-custom-font}

Para adicionar uma fonte personalizada, faça o seguinte:

1. Na seção **Nome da fonte padrão** em **Estilo básico**, selecione **Adicionar uma fonte personalizada**.
2. No campo **Nome da fonte**, insira o mesmo nome da fonte que aparece no arquivo de origem da sua fonte personalizada. Certifique-se de que o nome esteja com a capitalização e o espaçamento corretos.
3. Insira a URL correspondente no campo **URL da fonte**.
4. Verifique se a pré-visualização mostra sua fonte personalizada.
5. Selecione **Salvar** para usar a fonte personalizada como sua fonte padrão de e-mail.

{% alert important %}
O Gmail não oferece suporte a fontes personalizadas, então sua fonte personalizada pode ser exibida como uma fonte padrão do sistema. Para outras plataformas de e-mail, verifique se sua fonte personalizada é exibida corretamente antes de enviar suas mensagens de e-mail.
{% endalert %}

Para usar outras fontes personalizadas em suas Campaigns de e-mail, você pode criar um [modelo de e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) ou [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) que inclua a fonte personalizada. Por exemplo, você pode criar um modelo de e-mail específico com fontes personalizadas festivas adaptadas ao tema da sua promoção. Certifique-se de verificar se a fonte escolhida é segura para web e compatível com suas plataformas de e-mail.

### Fonte de fallback {#fallback-font}

As fontes de fallback são usadas para o título, cabeçalho e corpo do texto quando a fonte padrão escolhida não é compatível com o provedor de caixa de entrada ou sistema operacional. Por padrão, a Braze define automaticamente Arial como fonte de fallback quando as configurações globais de estilo são salvas. Você também tem a opção de adicionar serif ou sans serif como opções para a família de fontes padrão.

![Um exemplo de "Arial" como fonte de fallback com "Sans-serif" como família de fontes.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

Você pode adicionar até 17 fontes de fallback. A primeira fonte de fallback selecionada será a primeira a ser tentada. A fonte de fallback será aplicada apenas a modelos, Campaigns de e-mail e componentes do Canvas recém-criados. A fonte de fallback não é definida automaticamente para mensagens criadas antes da especificação da fonte de fallback. Recomendamos fortemente selecionar fontes de fallback semelhantes às do seu envio de mensagens por e-mail para manter a consistência da sua marca.

## Estilo de título {#title-styling}

Aqui, você pode ajustar os estilos dos títulos do seu e-mail editando o tamanho da fonte, a cor da fonte e o alinhamento do texto.

![Configurações de estilo de título para um cabeçalho principal e um cabeçalho secundário alinhados ao centro.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

Opcionalmente, você pode substituir o estilo padrão do tema do editor de arrastar e soltar. Selecione **Substituir estilo padrão** para aplicar sua escolha de estilo de título. Isso pode incluir definir uma fonte e cor de link diferentes.

## Estilo de parágrafo {#paragraph-styling}

Para definir um estilo de parágrafo padrão, acesse **Estilo de parágrafo**, insira o **Tamanho da fonte** e selecione **Cor da fonte** para escolher uma cor de fonte. Você também pode ajustar o estilo do bloco para o corpo do texto editando os valores de **Preenchimento superior**, **Preenchimento direito**, **Preenchimento inferior** e **Preenchimento esquerdo**. Isso será aplicado ao espaçamento ao redor das quatro áreas que cercam o bloco de parágrafo.

![Configurações de estilo de parágrafo para texto com fonte de 14pt.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## Estilo de lista {#list-styling}

Ao adicionar listas às suas mensagens, a seção **Estilo de lista** cria consistência na forma como suas listas são estilizadas. Isso inclui detalhes como:

- Tamanho da fonte
- Cor da fonte
- Peso da fonte
- Altura da linha
- Alinhamento
- Direção do texto
- Espaçamento entre letras
- Espaçamento entre itens da lista
- Recuo dos itens da lista
- Tipo de lista
- Tipo de estilo da lista

Você pode definir o **Tipo de lista** como numerada ou com marcadores. O **Tipo de estilo da lista** oferece personalização adicional para o estilo das suas listas. Por exemplo, você pode definir os tipos de lista para sempre usar marcadores e cada marcador ser um quadrado.

![Configurações de estilo de lista para uma lista com marcadores.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## Estilo de botão {#button-styling}

Na seção **Estilo de botão**, você pode editar os seguintes estilos padrão do botão:
- Cor de fundo
- Tamanho da fonte
- Cor da fonte
- Raio da borda
- Cor da borda
- Espessura da borda
- Preenchimento do botão

![Configurações de estilo de botão para um botão retangular com fundo azul.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

Assim como em todas as outras seções de estilo, você pode ajustar o estilo do bloco editando os valores de **Preenchimento superior**, **Preenchimento direito**, **Preenchimento inferior** e **Preenchimento esquerdo**.

## Largura do modelo de e-mail {#email-template-width}

Usando a largura do modelo de e-mail, você pode ajustar e definir uma largura para manter a consistência em suas Campaigns de e-mail.

![Largura do modelo de e-mail definida como 600px.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## Largura do Content Block {#content-block-width}

Essa configuração será pré-configurada para todos os futuros Content Blocks. Os Content Blocks existentes não serão atualizados. Você pode definir todos os Content Blocks para 100%, respeitando a largura onde o Content Block é inserido, ou definir um valor específico em pixels.

Recomendamos que a largura do Content Block corresponda à largura do modelo de e-mail.

![Largura do Content Block definida como 600px.]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})