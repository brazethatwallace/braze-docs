---
nav_title: Editor de arrastar e soltar
article_title: Crie um e-mail com arrastar e soltar
alias: /dnd/
page_order: 1
description: "Este artigo explica como configurar e usar corretamente o editor de arrastar e soltar para mensagens de e-mail."
channel: email
tool:
- Campaigns
- Canvas
---

# Crie um e-mail com arrastar e soltar {#create-an-email-with-drag-and-drop}

> Usando o editor de arrastar e soltar, você pode criar mensagens de e-mail totalmente personalizadas para Campaigns ou Canvas, sem precisar usar HTML para construir o corpo do e-mail.

## Sobre o editor {#about-the-editor}

O editor de arrastar e soltar usa [Conteúdo](#content) e [Linhas](#rows) como os dois componentes principais para simplificar seu fluxo de trabalho, sem o uso adicional de HTML.

<table aria-label="Sobre o editor" style="width: 100%; table-layout: fixed;">
    <caption>Componentes do editor: Conteúdo e Linhas</caption>
    <thead>
    <tr>
        <th style="width: 50%;">Conteúdo</th>
        <th style="width: 50%;">Linhas</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="A guia 'Linhas' que inclui diferentes combinações estruturais para o layout do seu e-mail." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="A guia 'Conteúdo' que inclui blocos básicos, mídia e avançados." style="max-width: 100%; height: auto;">
        </td>
    </tr>
    </tbody>
</table>
{: .reset-td-br-1 aria-label="Sobre o editor" }

### Conteúdo {#content}

**Conteúdo** inclui uma série de blocos que representam diferentes tipos de conteúdo que você pode usar na sua mensagem. Eles são organizados em três categorias: básico, mídia e avançado.

{% tabs %}
{% tab Básico %}

Os blocos básicos são a base do seu e-mail. Com esses blocos, você pode adicionar qualquer um dos seguintes elementos ao corpo do seu e-mail:

- Título
- Parágrafo
- Lista
- Botão
- Divisor
- Espaçador

{% endtab %}
{% tab Mídia %}

Com os blocos de mídia, você pode adicionar diferentes tipos de conteúdo visual, como imagens, vídeos, ícones e links de redes sociais e ícones personalizáveis.

{% endtab %}
{% tab Avançado %}

Embora o editor de arrastar e soltar simplifique seu fluxo de trabalho com esses blocos, você também pode usar blocos avançados para inserir HTML ou adicionar um menu ao corpo do seu e-mail. Observe que o uso do seu próprio HTML pode afetar a renderização da mensagem.

{% endtab %}
{% endtabs %}

### Linhas {#rows}

**Linhas** são unidades estruturais que definem a composição horizontal de uma seção da mensagem usando colunas. Você pode usar linhas vazias ou [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Usar mais de uma coluna permite colocar diferentes elementos de conteúdo lado a lado. Dessa forma, você pode adicionar todos os elementos estruturais necessários à sua mensagem, independentemente do modelo selecionado no início.

#### Aninhar imagens dentro de blocos de texto {#nesting-images-inside-text-blocks}

Não é possível aninhar uma imagem dentro de um parágrafo ou outro bloco de texto no editor de arrastar e soltar. Para posicionar uma imagem ao lado ou dentro de um layout de texto, use colunas em uma **Linha**: por exemplo, uma linha com várias colunas no desktop com **Hide on mobile** para essa linha, e uma linha separada apenas para dispositivos móveis (com **Hide on desktop** e **Do not stack on mobile** conforme necessário) para que a imagem e o texto fiquem alinhados corretamente em telas pequenas.

#### Estilo de cartões {#cards-style}

**Cards Style** é uma propriedade de linha que permite adicionar espaçamento entre colunas e arredondar seus cantos. Com a formatação em estilo de cartão, você pode criar layouts visualmente mais atraentes para destacar seu conteúdo mais importante, como novos recursos de produtos, depoimentos, ofertas especiais, novidades e muito mais.

## Usando o editor de arrastar e soltar {#using-the-drag-and-drop-editor}

Não tem certeza se sua mensagem de e-mail deve ser enviada usando uma Campaign ou um Canvas? Campaigns são melhores para campanhas de mensagens únicas e direcionadas, enquanto Canvas é melhor para jornadas de usuário com várias etapas.

{% alert note %}
Você não pode salvar um e-mail de arrastar e soltar de uma Campaign ou Canvas diretamente em **Modelos** > **Modelos de e-mail** como um modelo de e-mail. Crie primeiro em **Modelos**, ou consulte [Posso salvar meu e-mail de arrastar e soltar como modelo depois de criá-lo na minha Campaign ou Canvas?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#can-i-save-my-drag-and-drop-email-as-a-template-after-i-build-it-within-my-campaign-or-canvas) para recriar um modelo de arrastar e soltar ou exportar HTML com **Download de arquivo**.
{% endalert %}

Depois de selecionar onde construir sua mensagem, vamos mergulhar nas etapas para criar um e-mail de arrastar e soltar.

### Etapa 1: Selecione seu modelo {#step-1-select-your-template}

Depois de selecionar o editor de arrastar e soltar como sua experiência de edição, você pode escolher:

- Começar com um modelo em branco.
- Usar um modelo de e-mail de arrastar e soltar predefinido da Braze.
- Usar um modelo de e-mail de arrastar e soltar salvo.

{% alert note %}
Para usar um modelo HTML personalizado existente ou modelos criados por terceiros, você deve recriar o modelo acessando **Conteúdo** > **E-mail** e selecionando **Editor de arrastar e soltar** como sua experiência de edição.
{% endalert %}

Você também pode acessar todos os modelos na seção **Modelos**.

Depois de selecionar seu modelo, você verá uma visão geral do seu e-mail em **Variantes de e-mail**, que inclui as informações de envio e o corpo do e-mail.

Em seguida, selecione **Editar corpo do e-mail** para começar a projetar a estrutura do e-mail no editor de arrastar e soltar.

![A seção "Variantes de e-mail" com um exemplo de corpo de e-mail.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Etapa 2: Crie seu e-mail {#step-2-build-your-email}

A experiência de edição de arrastar e soltar é dividida em três seções: **Configurações de envio**, **Conteúdo** e **Prévia e teste**. A parte principal da construção do corpo do seu e-mail acontece na seção **Conteúdo**. Antes de criar seu e-mail, é importante entender os componentes principais que orientam sua experiência de criação de e-mail. Se precisar revisar, consulte [Sobre o editor](#about-the-editor).

Quando estiver pronto, use os blocos de conteúdo de arrastar e soltar para criar seu e-mail.

1. Selecione o painel **Linhas**. Arraste e solte as configurações de linha no editor principal. Isso mapeia o layout do conteúdo do seu e-mail.
- Observe que novas configurações devem ser arrastadas para o topo ou fundo de uma seção existente.
- Ao selecionar uma configuração de linha, as configurações de **Propriedades da linha** aparecem para personalização adicional de cores de fundo da linha, imagens e tamanhos de coluna personalizados.
2. Selecione o painel **Conteúdo**. Arraste e solte os blocos de conteúdo desejados nos componentes da linha.
- Você também pode arrastar qualquer bloco de **Conteúdo** para o editor principal. Isso cria uma linha para o bloco.
- Você pode refinar ainda mais o bloco selecionando-o e ajustando os campos em **Propriedades do conteúdo** e **Opções de bloco**. Isso inclui editar espaçamento entre letras, preenchimento, altura da linha e mais.

Confira [Outras personalizações](#other-customizations) para outras formas de personalizar ainda mais seu e-mail de arrastar e soltar.

Ao criar seu e-mail, você pode alternar entre as visualizações de desktop e mobile para pré-visualizar como suas mensagens de e-mail aparecerão para seus grupos de usuários. Isso verifica se seu conteúdo é responsivo, e você pode fazer os ajustes necessários ao longo do caminho.

{% alert tip %}
Precisa de ajuda para criar textos incríveis? Tente usar o [Assistente de copywriting com IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Insira o nome ou a descrição de um produto, e a IA gerará textos de marketing semelhantes aos humanos para uso no seu envio de mensagens.

![Botão de copywriting, localizado no painel de Conteúdo ao lado de Configurações de estilo no editor de arrastar e soltar.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Etapa 3: Adicione suas informações de envio {#step-3-add-your-sending-information}

Depois de terminar de projetar e criar sua mensagem de e-mail, é hora de adicionar suas informações de envio na seção **Configurações de envio**.

{% multi_lang_include email/sending_info_steps.md %}

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Uma prévia no painel à direita será preenchida com as informações de envio que você adicionou. Essas informações também podem ser atualizadas acessando **Configurações** > **Preferências de e-mail** > **Configuração de envio**.

#### Adicionar anexos de e-mail {#add-email-attachments}

Em **Configurações de envio** > **Avançado**, você pode adicionar anexos de e-mail pelos seguintes métodos:

{% multi_lang_include email/attachment_upload_options.md %}

Consulte as [Diretrizes de e-mail]({{site.baseurl}}/user_guide/channels/email/best_practices/email_guidelines) para práticas recomendadas específicas a serem consideradas.

#### Personalizar o cabeçalho do e-mail (avançado) {#personalize-your-email-header-advanced}

Em **Configurações de envio**, você pode adicionar personalização para cabeçalhos de e-mail e extras de e-mail, o que permite enviar dados adicionais de volta para outros provedores de serviços de e-mail. Personalizar um cabeçalho de e-mail, como incluir o nome do destinatário, também pode contribuir para a probabilidade de seu e-mail ser aberto.

{% alert note %}
A funcionalidade avançada aparecerá no criador de Campaign ou Canvas. Na funcionalidade avançada, você pode modificar sua configuração de CSS inline e inserir um cabeçalho ou pares de chave-valor extras (se configurados).
{% endalert %}

### Etapa 4: Teste seu e-mail {#step-4-test-your-email}

Depois de adicionar suas informações de envio, é hora de finalmente testar seu e-mail.

{% alert tip %}
Se o e-mail parecer diferente no editor do que na prévia ou no envio de teste, confirme que todas as tags estão fechadas, os atributos de imagem têm valores e as imagens de fundo não estão desfocadas nas bordas.
{% endalert %}

Acesse a seção **Prévia e teste**. Aqui, você tem a opção de pré-visualizar seu e-mail como um usuário ou enviar uma mensagem de teste. Esta seção também inclui o [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision), que permite verificar se seu e-mail foi renderizado corretamente em diferentes clientes de e-mail móveis e web.

{% alert tip %}
Você também pode usar o botão **Prévia no modo escuro** no painel de prévia para visualizar o corpo do seu e-mail no modo escuro e ajustar seu e-mail conforme necessário.
{% endalert %}

Como você pode visualizar três versões diferentes do mesmo e-mail — no editor, no Inbox Vision e como um e-mail de teste real — é importante alinhar os detalhes em todas as suas plataformas.

#### Prévia e envio de teste {#preview-and-test-send}

Na guia **Prévia como usuário**, você pode selecionar os seguintes tipos de usuários para pré-visualizar sua mensagem.

- **Usuário aleatório:** a Braze selecionará aleatoriamente um usuário do banco de dados e pré-visualizará o e-mail com base nos atributos ou informações de eventos desse usuário.
- **Selecionar usuário:** você pode selecionar um usuário específico com base no endereço de e-mail ou ID externo. O e-mail será pré-visualizado com base nos atributos e informações de eventos desse usuário.
- **Usuário personalizado:** você pode personalizar um usuário. A Braze oferecerá campos de entrada para todos os atributos e eventos disponíveis. Você pode inserir qualquer informação que deseja ver no e-mail de prévia.

{% alert note %}
O usuário aleatório pode ou não fazer parte dos seus critérios de segmentação. A segmentação é selecionada depois, então a Braze não conhece seu público-alvo neste momento.
{% endalert %}

Você também pode selecionar **Copiar link de prévia** para gerar e copiar um link de prévia compartilhável que mostra como o e-mail aparecerá para um usuário aleatório. Para saber mais, consulte [Prévia compartilhável]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

![Prévia de e-mail com um botão para "Copiar link de prévia" e copiar o link gerado.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Usar o Inbox Vision {#use-inbox-vision}

O Inbox Vision permite visualizar suas Campaigns de e-mail da perspectiva de clientes de e-mail e dispositivos móveis. Para testar sua mensagem de e-mail usando o Inbox Vision, selecione **Inbox Vision** na seção **Prévia e teste** e selecione **Executar Inbox Vision**.

É importante testar e verificar os detalhes mais finos da sua mensagem de e-mail. Por exemplo, imagens de fundo em mensagens de e-mail às vezes podem causar o aparecimento de linhas brancas ou desconexões entre imagens, ou clientes como o Windows Outlook podem não exibir imagens de fundo. Usar o Inbox Vision pode ajudar a identificar essas discrepâncias entre clientes. Nesse cenário, defina uma cor de fundo de fallback para que essas imagens possam ser renderizadas conforme esperado.

Para saber mais, consulte [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=email).

Depois de usar o editor de arrastar e soltar para projetar e criar sua mensagem de e-mail, continue a [construir]({{site.baseurl}}/user_guide/channels/email/html_editor#step-4-build-the-remainder-of-your-campaign-or-canvas) o restante da sua Campaign ou Canvas.

{% details Sobre o mecanismo HTML atualizado %}
O mecanismo subjacente que produz HTML a partir do editor de arrastar e soltar foi otimizado e atualizado, resultando em benefícios relacionados à compressão de arquivos HTML e renderização.

O tamanho médio dos dados HTML exportados foi reduzido, levando a carregamento e renderização mais rápidos, menos cortes em dispositivos móveis e menor consumo de largura de banda.

A renderização HTML foi aprimorada com base nas seguintes atualizações que minimizam o número de comentários condicionais e media queries CSS. Como resultado, os arquivos HTML são menores e codificados de forma mais eficiente.
- Migração de um design baseado em elementos `<div>` para um codebase formatado em `<table aria-label="Usar Inbox Vision">` padrão
  <caption>Usar Inbox Vision</caption>
- Os [Blocos do editor (e-mail)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) foram recodificados para maior concisão
- O código HTML final é comprimido para remover espaços em branco entre as tags
- Divisores transparentes são automaticamente convertidos em preenchimento de conteúdo
{% enddetails %}

## Outras personalizações {#other-customizations}

À medida que você continua construindo e-mails de arrastar e soltar, pode personalizar ainda mais cada corpo de e-mail usando uma combinação desses detalhes criativos para capturar a atenção e o interesse do seu público na sua mensagem.

{% alert tip %}
Você pode criar um tema personalizado para o editor de arrastar e soltar usando as [configurações de estilo global]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings).
{% endalert %}

### Imagens com largura automática {#auto-width-images}

As imagens adicionadas ao seu e-mail serão automaticamente definidas como **Largura automática**. Para ajustar essa configuração, desative a opção **Largura automática** e ajuste a porcentagem da largura conforme necessário.

![Opção de largura automática na guia Conteúdo do editor de arrastar e soltar.]({% image_buster /assets/img/dnd/dnd1.png %})

### Camadas de cores {#color-layering}

Usando camadas de cores, você pode alterar a cor do plano de fundo do e-mail, da área de conteúdo e de diferentes componentes de conteúdo. A ordem das cores da frente para trás é: cor do componente de conteúdo, cor de fundo da área de conteúdo e cor de fundo.

![Exemplo de camadas de cores no editor de arrastar e soltar.]({% image_buster /assets/img/dnd/dnd2.png %})

### Preenchimento de conteúdo {#content-padding}

![Opções de bloco para o editor de arrastar e soltar.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Para ajustar o preenchimento, role para baixo até **Opções de bloco** e selecione **Mais opções**. Você pode ajustar o preenchimento para deixar seu e-mail com a aparência ideal.

### Fundo do conteúdo {#content-background}

Você pode adicionar uma imagem de fundo à configuração de linha, permitindo incorporar mais design e conteúdo visual na sua campanha de e-mail.

### Atributo de idioma {#language-attribute}

Você pode definir o atributo de idioma acessando a guia **Configurações** e selecionando o idioma desejado. Você também pode direcionar o atributo do usuário {%raw%} `{{${language}}}` {%endraw%} se a mensagem for destinada a usuários com valores de idioma dinâmicos.

![Definindo o valor de "Idioma" para um e-mail.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### Personalização {#personalization}

![Opções para adicionar personalização no editor de arrastar e soltar.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Liquid básico é compatível com o editor de e-mail de arrastar e soltar. Para adicionar personalização ao seu e-mail:

1. Selecione **Personalização** na seção **Conteúdo**.
2. Selecione o tipo de personalização. Isso inclui atributos padrão (standard), atributos de dispositivo, atributos personalizados e mais.
3. Pesquise o atributo a ser adicionado.
4. Copie o snippet de Liquid gerado e cole no corpo do seu e-mail.

A personalização com Liquid não é compatível com blocos de imagem e campos de tipo de link de botão.

#### Imagens dinâmicas {#dynamic-images}

Você pode optar por incluir imagens dinâmicas no envio de mensagens de e-mail incluindo [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) ou [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) no atributo de origem da imagem. Por exemplo, em vez de uma imagem estática, você pode inserir {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como a URL da imagem para incluir o nome do usuário na imagem. Isso ajuda a personalizar seus e-mails para cada usuário.

{% alert important %}
A URL da sua imagem deve começar com `https://`. Usar `http://` causa falha no seu app.
{% endalert %}

### Direção do texto {#text-direction}

Ao escrever sua mensagem, você pode alternar a direção do texto entre da esquerda para a direita e da direita para a esquerda selecionando o respectivo botão **Direção do texto**. Você pode usar essa opção ao criar mensagens em idiomas como árabe e hebraico.

![Menu do editor de arrastar e soltar de e-mail com botão para alternar o alinhamento do texto entre da direita para a esquerda e da esquerda para a direita.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

A aparência final das mensagens da direita para a esquerda depende muito de como os provedores de serviço as renderizam. Para práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### HTML

#### Atributos HTML para links {#html-attributes-to-links}

![A seção "Atributos" com o atributo "clicktracking" desativado para um link.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Ao usar links, botões, imagens e vídeos no editor de arrastar e soltar, selecione **Adicionar novo atributo** em **Atributos** na seção **Conteúdo** para adicionar informações adicionais às tags HTML nos e-mails. Isso pode ser especialmente útil para personalização de mensagens, segmentação e estilização.

Um caso de uso comum é desativar o rastreamento de cliques para links específicos ao enviar pela Braze. Você pode fazer isso de duas maneiras:

- **Usar atributos do módulo de link:** Selecione um elemento de link (como um botão ou módulo de link), depois use **Adicionar novo atributo** em **Atributos** para adicionar:
  - Para SendGrid, use `clicktracking` como nome e `off` como valor.
  - Para SparkPost, use `data-msys-clicktrack` como nome e `0` como valor.
- **Usar bloco HTML:** Insira um bloco HTML e inclua o atributo de rastreamento de cliques diretamente no código da sua tag de âncora:
  - Para SendGrid, use `<a href="your-url" clicktracking="off">Texto do link</a>`.
  - Para SparkPost, use `<a href="your-url" data-msys-clicktrack="0">Texto do link</a>`.

Outro caso de uso comum é sinalizar links específicos como links universais. Links universais são links que redirecionam para o seu app, oferecendo aos seus usuários uma experiência integrada.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (um [subcaminho personalizado](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) deve ser configurado)

Para configurar links universais, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links).

Alternativamente, você pode integrar com um dos nossos parceiros de atribuição, como [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) ou [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/deeplinking/appsflyer/appsflyer#integrate-appsflyer-with-braze-for-deep-linking), para gerenciar links universais.

Por fim, atributos predefinidos estão disponíveis para ajudar a tornar sua mensagem acessível. Saiba mais no nosso artigo dedicado [Criando mensagens acessíveis na Braze]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility), incluindo [como clientes de e-mail exibem texto alternativo]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text).

#### Tags de cabeçalho personalizadas {#custom-head-tags}

Use tags `<head>` para adicionar CSS e metadados na sua mensagem de e-mail. Por exemplo, você pode usar essas tags para adicionar uma folha de estilos ou favicon. Liquid é compatível com tags `<head>`.

Qualquer conteúdo adicionado fora das tags `<head>` será inserido após a tag `<body>` no seu e-mail. Isso significa que o conteúdo adicionado será exibido no e-mail.

##### Tags e atributos permitidos por tag {#allowed-tags-and-attributes-by-tag}

| Nome da tag | Descrição | Exemplo |
| --- | --- | --- |
| `base` | Especifica a URL base para todas as URLs relativas na mensagem. | `<base href="https://example.com" target="_blank">` |
| `link`| Define relações entre a mensagem e recursos externos. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | Fornece metadados como descrição da página ou palavras-chave. | `<meta name="description" content="Free Web tutorials">` |
| `style` | Incorpora estilos CSS internos. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | Define o título do documento exibido nas abas do navegador. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Tags e atributos permitidos por tag" }

| Tag | Atributo | Descrição | Exemplo |
| --- | --- | --- | --- |
| `base` | `href` | URL base a ser usada para URLs relativas. | ```<base href="https://braze.com">``` |
| `base` | `target`| Alvo padrão para todos os hiperlinks e formulários. | ```<base target="_blank">``` |
| `link` | `href` | URL para o recurso externo. | ```<link href="style.css">``` |
| `link` | `rel` | Define relações entre a mensagem atual e a vinculada. | ```<link rel="stylesheet">``` |
| `link` | `type` | Tipo de recurso vinculado. | ```<link type="text/css">``` |
| `link` | `sizes` | Especifica os tamanhos dos ícones. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | Especifica a mídia ou dispositivo para o qual os estilos se aplicam. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | Define o título do documento exibido nas abas do navegador. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | Define o título do documento exibido nas abas do navegador. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | Declara a codificação de caracteres. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | Define o título do documento exibido nas abas do navegador. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | Tipo MIME do conteúdo de estilo. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | Especifica a mídia ou dispositivo para o qual os estilos se aplicam. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | Sem atributos | A tag `title` não aceita nenhum atributo. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Tags e atributos permitidos por tag" }

{% alert note %}
Os nomes de links podem ter até 63 bytes e são automaticamente truncados se excederem o limite.
{% endalert %}