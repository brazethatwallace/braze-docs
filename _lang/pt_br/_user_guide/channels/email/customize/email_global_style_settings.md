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

Em **Estilo básico**, você pode definir as cores padrão de fundo do e-mail e do conteúdo para suas Campaigns e Canvas de e-mail. Você também pode selecionar uma fonte padrão, adicionar uma fonte personalizada e editar as cores dos links.

![Opções de estilo básico que incluem opções para editar as cores de fundo do e-mail e do conteúdo, nome da fonte padrão e cor padrão do link.]({% image_buster /assets/img_archive/dnd_basic_styling.png %})

## Fonte personalizada {#custom-font}

Com fontes personalizadas, você pode adicionar manualmente uma fonte web para manter a consistência da marca em diversas plataformas de e-mail. Você pode adicionar uma fonte personalizada para cada seção de estilo.

{% alert note %}
Quaisquer configurações de font-weight no CSS são ignoradas. Em vez disso, selecione um dos pesos predefinidos ao compor a mensagem.
{% endalert %}

### Requisitos {#requirements}

Antes de adicionar uma fonte personalizada, verifique se o arquivo da fonte atende aos seguintes requisitos:

- O CORS deve estar ativado no servidor que fornece o arquivo da fonte personalizada. Isso geralmente é gerenciado pela sua equipe de TI.
  - O arquivo da fonte personalizada deve conter o cabeçalho: `Access-Control-Allow-Origin: *`
- A URL do arquivo deve apontar para um arquivo CSS (não WOFF ou OTF).
- O nome da fonte personalizada deve corresponder ao nome do font face no arquivo CSS.

{% alert important %}
O provedor de fontes personalizadas pode coletar dados pessoais dos seus destinatários. Revise as políticas do seu provedor de fontes antes de usá-lo.
{% endalert %}

### Adicionando uma fonte personalizada {#adding-a-custom-font}

Para adicionar uma fonte personalizada, faça o seguinte:

1. Na seção **Default Font Name** de **Basic Styling**, selecione **Add a custom font**.
2. No campo **Font Name**, insira o mesmo nome de fonte que aparece no arquivo de origem da sua fonte personalizada. Certifique-se de que o nome esteja com a capitalização e o espaçamento corretos.
3. Insira a URL correspondente no campo **Font URL**.
4. Verifique se a prévia exibe a sua fonte personalizada.
5. Selecione **Save** para usar a fonte personalizada como sua fonte de e-mail padrão.

{% alert important %}
O Gmail não oferece suporte a fontes personalizadas, então a sua fonte personalizada pode ser exibida como uma fonte padrão do sistema. Para outras plataformas de e-mail, verifique se a sua fonte personalizada é exibida corretamente antes de enviar as suas mensagens de e-mail.
{% endalert %}

Para usar outras fontes personalizadas nas suas Campaigns de e-mail, você pode criar um [modelo de e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) ou [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) que inclua a fonte personalizada. Por exemplo, você pode criar um modelo de e-mail específico com fontes personalizadas festivas adaptadas ao tema da sua promoção. Certifique-se de que a fonte escolhida ainda seja segura para a web e compatível com as suas plataformas de e-mail.

### Fonte de fallback {#fallback-font}

As fontes de fallback são usadas para o título, cabeçalho e corpo do texto quando a sua fonte padrão não é compatível com o provedor da caixa de entrada ou sistema operacional. Por padrão, a Braze define automaticamente Arial como fonte de fallback quando as configurações de estilo global são salvas. Você também tem a opção de adicionar serif ou sans serif como opções para a família de fontes padrão.

![Exemplo de "Arial" como fonte de fallback com "Sans-serif" como a família de fontes.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

Você pode adicionar até 17 fontes de fallback. A primeira fonte de fallback selecionada será a primeira a ser tentada. A fonte de fallback só será aplicada a modelos, Campaigns de e-mail e componentes do Canvas criados recentemente. A fonte de fallback não é definida automaticamente para mensagens criadas antes da especificação da fonte de fallback. Recomendamos fortemente selecionar fontes de fallback semelhantes ao estilo das suas mensagens de e-mail para manter a consistência da sua marca.

## Estilização de títulos {#title-styling}

Aqui, você pode ajustar os estilos dos títulos do seu e-mail editando o tamanho da fonte, a cor da fonte e o alinhamento do texto.

![Configurações de estilização de título para um cabeçalho principal e um cabeçalho secundário centralizados.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

Opcionalmente, você pode substituir o estilo padrão do tema do editor de arrastar e soltar. Selecione **Substituir estilo padrão** para aplicar a estilização de título de sua preferência. Isso pode incluir a definição de uma fonte e uma cor de link diferentes.

## Estilos de parágrafo {#paragraph-styling}

Para definir um estilo de parágrafo padrão, acesse **Paragraph Styling**, insira o **Font Size** e selecione **Font Color** para escolher uma cor de fonte. Você também pode ajustar o estilo do bloco para o corpo do texto editando os valores de **Padding Top**, **Padding Right**, **Padding Bottom** e **Padding Left**. Isso será aplicado ao espaçamento ao redor das quatro áreas que cercam o bloco de parágrafo.

![Configurações de estilo de parágrafo para texto com fonte de 14pt.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## Estilo de listas {#list-styling}

Ao adicionar listas às suas mensagens, a seção **List Styling** cria consistência na forma como suas listas são estilizadas. Isso inclui detalhes como:

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
- Estilo do tipo de lista

Você pode definir o **List Type** como numerado ou com marcadores. O **List Style Type** oferece personalização adicional para o estilo das suas listas. Por exemplo, você pode definir os tipos de lista para sempre usarem marcadores e para cada marcador ser um quadrado.

![Configurações de estilo de lista para uma lista com marcadores.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## Estilo do botão {#button-styling}

Na seção **Estilo do botão**, você pode editar os seguintes estilos padrão do botão:
- Cor de fundo
- Tamanho da fonte
- Cor da fonte
- Raio da borda
- Cor da borda
- Espessura da borda
- Preenchimento do botão

![Configurações de estilo do botão para um botão retangular com fundo azul.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

Assim como em todas as outras seções de estilo, você pode ajustar o estilo do bloco editando os valores de **Padding Top**, **Padding Right**, **Padding Bottom** e **Padding Left**.

## Largura do modelo de e-mail {#email-template-width}

Com a largura do modelo de e-mail, você pode ajustar e definir uma largura para manter a consistência em suas campanhas de e-mail.

![Largura do modelo de e-mail definida como 600px.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## Largura do Content Block {#content-block-width}

Essa configuração será pré-definida para todos os Content Blocks futuros. Os Content Blocks existentes não serão atualizados. Você pode configurar todos os Content Blocks para 100%, respeitando a largura onde o Content Block é inserido, ou definir um valor específico em pixels.

Recomendamos que a largura do Content Block corresponda à largura do modelo de e-mail.

![Largura do Content Block definida como 600px.]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})