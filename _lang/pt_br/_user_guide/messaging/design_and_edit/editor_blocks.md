---
nav_title: Blocos do editor
article_title: Blocos do editor de arrastar e soltar
alias: "/dnd/editor_blocks/"
channel:
- email
- in-app messages
- landing pages
- banners
- preference center
page_order: 3
page_type: reference
description: "Este artigo de referência aborda os blocos do editor no editor de arrastar e soltar para e-mail, mensagens no app, landing pages, Banners e Central de Preferências de e-mail de arrastar e soltar."
tool: Media
---

# Blocos do editor de arrastar e soltar {#drag-and-drop-editor-blocks}

> Blocos do editor são os blocos que você arrasta para linhas e colunas no editor de arrastar e soltar.

Selecione o editor que você está usando:

{% sdktabs %}

{% sdktab email %}
## Blocos do editor de e-mail {#email-editor-blocks}

Os blocos do editor ficam na seção **Conteúdo** para mensagens de e-mail. Arraste um bloco para dentro de uma coluna no **editor de arrastar e soltar**; ele se ajusta automaticamente à largura da coluna.

Para saber mais sobre como criar e-mails no **editor de arrastar e soltar**, consulte [Criar um e-mail com arrastar e soltar]({{site.baseurl}}/user_guide/channels/email/drag_and_drop) e <a href="{{site.baseurl}}/user_guide/channels/email/drag_and_drop/#other-customizations">Outras personalizações</a> nesse artigo.

{% alert tip %}
Você também pode adicionar [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types) a qualquer URL dentro dos blocos do editor `Image`, `Button` ou `Text`.
{% endalert %}

### Título {#title}

Adiciona texto para cabeçalhos dentro do e-mail.

| Propriedade | Descrição |
|---|---|
| Título | Seleciona o estilo do cabeçalho. |
| Família da fonte | O estilo de fonte do seu título. |
| Peso da fonte | O nível geral de negrito da fonte. |
| Tamanho da fonte | Determina o tamanho do seu texto. |
| Cor do texto | Modifica a cor do título. |
| Cor do link | Modifica a cor do link. |
| Alinhamento | Move o título para ficar alinhado à esquerda, ao centro ou à direita. |
| Altura da linha | Modifica a distância entre as linhas de texto. |
| Espaçamento entre letras | Modifica a distância entre cada caractere. |
| Direção do texto | Padrão da esquerda para a direita, mas pode ser editado para [da direita para a esquerda]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Título" }

### Parágrafo {#paragraph}

Insere texto na mensagem. Uma barra de ferramentas ajuda com a funcionalidade de edição de fonte e texto.

| Propriedade | Descrição |
|---|---|
| Família da fonte | O estilo de fonte do texto do parágrafo. |
| Peso da fonte | O nível geral de negrito da fonte. |
| Tamanho da fonte | Determina o tamanho do seu texto. |
| Cor do texto | Modifica a cor do texto. |
| Cor do link | Modifica a cor do link. |
| Alinhamento | Move o texto para ficar alinhado à esquerda, ao centro ou à direita. |
| Espaçamento entre parágrafos | Modifica o espaço entre parágrafos. |
| Altura da linha | Modifica a distância entre as linhas de texto. |
| Espaçamento entre letras | Modifica a distância entre cada caractere. |
| Direção do texto | Padrão da esquerda para a direita, mas pode ser editado para [da direita para a esquerda]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parágrafo" }

### Lista {#list}

Adiciona uma lista com marcadores.

| Propriedade | Descrição |
|---|---|
| Tipo de lista | O tipo de lista. Pode ser com marcadores ou numerada. |
| Estilo do tipo de lista | Determina o estilo da sua lista. |
| Iniciar lista a partir de | Determina o número inicial da sua lista. |
| Família da fonte | O estilo de fonte do texto do parágrafo. |
| Peso da fonte | O nível geral de negrito da fonte. |
| Tamanho da fonte | Determina o tamanho do seu texto. |
| Cor do texto | Modifica a cor do texto. |
| Cor do link | Modifica a cor do link. |
| Alinhamento | Move o texto para ficar alinhado à esquerda, ao centro ou à direita. |
| Espaçamento entre itens da lista | Modifica o espaço entre os itens da lista. |
| Recuo dos itens da lista | Modifica o recuo dos itens da lista. |
| Altura da linha | Modifica a distância entre as linhas de texto. |
| Espaçamento entre letras | Modifica a distância entre cada caractere. |
| Direção do texto | Padrão da esquerda para a direita, mas pode ser editado para [da direita para a esquerda]({{site.baseurl}}/right_to_left_messages). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Lista" }

### Botão {#button}

Adiciona um botão padrão. As propriedades permitem editar o estilo e definir o comportamento do link.

| Propriedade | Descrição |
|---|---|
| Opções do botão | Define várias opções do botão, como fonte, tamanho, largura, cor e preenchimento. |
| Hover do botão | O estilo do botão quando o usuário passa o mouse ou trackpad sobre ele. Inclui a cor de fundo do botão, a cor da fonte e os estilos de borda. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Botão" }

#### Comportamento ao clicar {#on-click-behavior}

| Propriedade | Descrição |
|---|---|
| Tipo de link | Determina a ação ao clicar no botão e define o protocolo apropriado. |
| URL | Dinâmico com base no tipo de link **Abrir página da web**. |
| Destinatário, assunto e corpo | Para o tipo de link **Enviar e-mail**, define o endereço de e-mail do destinatário, o assunto e o conteúdo que serão preenchidos em um rascunho de e-mail quando o usuário selecionar o botão. |
| Tel | Para os tipos de link **Fazer chamada** e **Enviar SMS**, define o número de telefone para o qual o usuário ligará ou enviará mensagem ao selecionar o botão. |
| Mensagem | Para o tipo de link **Enviar SMS**, define o conteúdo que será preenchido em um rascunho de mensagem SMS quando o usuário selecionar o botão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamento ao clicar" }

### Divisor {#divider}

Insere uma linha sólida, pontilhada ou tracejada para ajudar com o espaçamento.

| Propriedade | Descrição |
|---|---|
| Transparente | Se ativado, as opções de linha e largura são removidas. |
| Linha | Os diferentes formatos de linha, seja pontilhada, tracejada ou sólida. Você também pode modificar a espessura e a cor da linha divisória. |
| Largura | Ajusta a extensão do divisor em incrementos de 5. |
| Alinhamento | Move a linha para ficar alinhada à esquerda, ao centro ou à direita. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Divisor" }

### Espaçador {#spacer}

Adiciona espaço ou preenchimento entre outros blocos.

| Propriedade | Descrição |
|---|---|
| Altura | Ajusta a altura do bloco espaçador. O padrão é 60px. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Espaçador" }

### Imagem {#image}

Insere uma imagem da [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library). Para imagens dinâmicas (imagens com Liquid ou Connected Content), você deve definir uma imagem de fallback para usar as configurações de largura automática. Para especificações de imagem, consulte [especificações de imagem de e-mail]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propriedade | Descrição |
|---|---|
| Largura automática | Modifica a largura da imagem em pixels. |
| Alinhamento | Define o alinhamento da imagem à esquerda, ao centro ou à direita dentro do bloco. |
| Imagem com Liquid | Use a lógica [Liquid]({{site.baseurl}}/liquid) para definir dinamicamente diferentes imagens dentro do mesmo bloco de conteúdo. |
| URL | Defina uma imagem usando o endereço onde ela está hospedada. |
| Texto alternativo | Uma breve descrição da imagem que fornece aos usuários as mesmas informações mostradas na imagem. Essencial para acessibilidade de leitores de tela ou quando a imagem não carrega. |
| Imagem com cantos arredondados | Renderiza a imagem com cantos arredondados. Por padrão, as imagens são renderizadas com cantos quadrados. |
| Ação | Dispara uma ação quando o usuário clica na imagem. |
| Opções do bloco | Define o preenchimento ao redor do bloco de imagem. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Imagem" }

{% alert tip %}
Para **Largura automática**, o redimensionamento automático de imagem escolhe o melhor tamanho para a imagem com base em uma combinação da largura da imagem e do espaço disponível no layout:
- Imagens mais largas que o espaço disponível são definidas com 100% de largura e mantêm essa proporção no celular, usando toda a largura de exibição do dispositivo.
- Imagens menores que o espaço disponível usam o tamanho natural da imagem para evitar efeitos de distorção ou imagens borradas.
{% endalert %}

#### Comportamento do botão de download do Gmail {#gmail-download-button-behavior}

O Gmail adiciona automaticamente um botão de download a imagens que não possuem um hiperlink (`href`) associado a elas. No entanto, se a proporção da imagem for 299 x 524 px ou menor, o Gmail não exibirá o botão de download.

Para evitar que o botão de download apareça em imagens maiores, você pode aplicar a solução alternativa do link "#":

1. Selecione o bloco **Imagem**.
2. No painel **Opções do bloco**, vá até a seção **Link**.
3. Defina o **Tipo de link** como **Abrir página da web**.
4. Insira um sinal de cerquilha (`#`) no campo de entrada **URL**.

Adicionar esse link impede que o Gmail exiba o botão de download sem afetar a experiência do usuário.

### Vídeo {#video}

Cria um link para conteúdo de vídeo. Apenas YouTube e Vimeo são compatíveis.

| Propriedade | Descrição |
|---|---|
| URL | A URL do vídeo. |
| Título | Gerado automaticamente a partir dos metadados do vídeo ou pode ser personalizado. |
| Estilo do ícone de reprodução | Inclui diferentes opções para o botão de reprodução localizado na parte superior de uma imagem de vídeo. |
| Cor do ícone de reprodução | Opção para selecionar **Claro** ou **Escuro** para o botão de reprodução. |
| Tamanho do ícone de reprodução | Escolha o tamanho em pixels para o botão de reprodução. Intervalo predefinido de 50&nbsp;px a 80&nbsp;px (incrementado em 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Vídeo" }

{% alert tip %}
Vídeos hospedados pelo Vimeo só funcionam se estiverem definidos como públicos. Todas as outras configurações de segurança disponíveis no Vimeo (por exemplo, "Ocultar do Vimeo.com") geram um formato de link diferente que não é compatível com este Content Block. Esses tipos de links são alterados pelo construtor, o que impede a Braze de gerar uma miniatura.
{% endalert %}

### Social {#social}

Insere ícones de plataformas de redes sociais. Você pode fazer upload de imagens personalizadas para ícones específicos da marca.

| Propriedade | Descrição |
|---|---|
| Selecionar coleção de ícones | Define o estilo da sua coleção de ícones. |
| Configurar coleção de ícones | Define a URL para cada ícone social. Inclui o botão **Mais opções** para editar o título e o texto alternativo. |
| Alinhamento | Move o ícone social para ficar alinhado à esquerda, ao centro ou à direita. |
| Espaçamento entre ícones | Determina o espaçamento entre cada ícone social. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Social" }

### Ícones {#icons}

Insere um ícone. Você pode fazer upload de imagens personalizadas. A Braze usa um ícone de espaço reservado grande até que você faça upload de uma imagem.

| Propriedade | Descrição |
|---|---|
| Família da fonte | O estilo de fonte do texto do parágrafo. |
| Peso da fonte | O nível geral de negrito da fonte. |
| Tamanho da fonte | Determina o tamanho do seu texto. |
| Cor do texto | Modifica a cor do título. |
| Cor do link | Modifica a cor do link. |
| Alinhamento | Move o ícone para ficar alinhado à esquerda, ao centro ou à direita. |
| Espaçamento entre letras | Modifica a distância entre cada caractere. |
| Tamanho do ícone | Determina o tamanho do seu ícone. |
| Espaçamento do ícone | Modifica o espaço do ícone. |
| Preenchimento do ícone | Modifica o preenchimento do ícone. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ícones" }

### HTML

Insere HTML bruto. Recomendado para [Liquid]({{site.baseurl}}/liquid), como Connected Content ou instruções condicionais.

| Propriedade | Descrição |
|---|---|
| HTML | Adicione ou edite HTML bruto, incluindo [Liquid]({{site.baseurl}}/liquid) para personalização ou lógica condicional. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTML" }

### Menu {#menu}

Cria um menu flexível para a mensagem que você está criando.

| Propriedade | Descrição |
|---|---|
| Configurar itens do menu | Adiciona um item de menu. |
| Família da fonte | O estilo de fonte do menu. |
| Tamanho da fonte | O tamanho do seu menu. |
| Cor do texto | Modifica a cor do menu. |
| Cor do link | Modifica a cor do texto do menu. |
| Alinhamento | Move o menu para ficar alinhado à esquerda, ao centro ou à direita. |
| Espaçamento entre letras | Modifica a distância entre cada caractere. |
| Layout | Determina o layout como horizontal ou vertical. |
| Separador | Adiciona caractere(s) entre as opções do menu. |
| Menu mobile | Inclui opções para modificar o tamanho do ícone, a cor e o tipo de ícone quando exibido em um dispositivo móvel. |
| Preenchimento do item | Modifica o preenchimento usando o botão **+** ou **-**, ou inserindo um número específico. |
| Todos os lados | Define um número de preenchimento consistente se o preenchimento do item estiver desativado. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Menu" }

### Produto {#product}

Renderiza linhas de produtos de um [Catálogo de Produtos]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks), seja como itens estáticos de uma Seleção de catálogo (até 12) ou como produtos dinâmicos acionados por um [gatilho de eCommerce do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases) (até 24).

| Propriedade | Descrição |
| --- | --- |
| Tipo de conteúdo | Define se os produtos vêm de uma **Seleção** fixa do catálogo (**Estático**, até 12 produtos) ou de um gatilho de recomendação de eCommerce do Canvas (**Dinâmico**, até 24 produtos). **Dinâmico** está disponível apenas em etapas de mensagem do Canvas. |
| Catálogo | Seleciona qual Catálogo de Produtos fornece os dados e mapeamentos de campos dos produtos. |
| Seleção | *(Apenas estático)* Seleciona qual conjunto filtrado no catálogo define quais produtos aparecem. |
| Mostrar detalhes da origem | Alterna o texto de ajuda mostrando o catálogo ou campo de evento subjacente mapeado para cada campo do produto. |
| Imagem da variante | Mostra ou oculta a imagem da variante para cada bloco de produto. |
| Título do produto | Mostra ou oculta o título do produto para cada bloco. |
| Preço | Mostra ou oculta o preço do produto. |
| Botão para URL do produto | Mostra ou oculta um botão de chamada para ação vinculado à URL do produto. |
| Quantidade | *(Dinâmico, apenas Canvas, quando o evento-gatilho de entrada não é um evento de visualização de produto)* Mostra ou oculta a quantidade do produto do evento-gatilho. |
| Orientação do produto | Define a posição da imagem dentro de cada bloco: **Imagem à esquerda**, **Imagem ao centro** ou **Imagem à direita**. |
| Alinhamento | Define o alinhamento horizontal do conteúdo dentro de cada bloco. |
| Máximo de produtos por linha | Define quantos produtos aparecem por linha: **1**, **2** ou **3** (**3** está disponível apenas quando a orientação é **Imagem ao centro**). |
| Espaçamento entre produtos | Define o espaçamento entre produtos: **Automático** ou **Personalizado**. |
| Espaçamento personalizado | *(Quando **Personalizado** está selecionado)* Define o espaço em pixels entre os produtos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Produto" }

## Personalização {#personalization}

Você pode adicionar personalização ao seu e-mail usando Liquid ou Connected Content.

- **Liquid:** Em **Conteúdo** > **Personalização**, selecione um atributo, copie o snippet e cole-o em um bloco HTML. Embora snippets básicos de Liquid possam funcionar em blocos de Título, Parágrafo e Lista, colocar Liquid nesses blocos pode causar comportamento inesperado e problemas de layout. Para evitar problemas, use blocos HTML para qualquer lógica Liquid. Observe que o Liquid não é compatível em blocos de imagem ou em campos de URL de botão.
- **[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content):** Adicione um bloco **HTML** e coloque sua chamada {% raw %}`{% connected_content %}`{% endraw %} lá.

{% endsdktab %}

{% sdktab in-app messages %}
## Blocos do editor de mensagens no app {#in-app-message-editor-blocks}

Os blocos do editor ficam na seção **Criar** para mensagens no app. Arraste um bloco para uma coluna; ele se ajusta automaticamente à largura da coluna. Selecione um bloco para editar suas configurações no painel lateral direito.

Para saber mais sobre como criar mensagens no app no **editor de arrastar e soltar**, consulte [Criar uma mensagem no app com arrastar e soltar]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop).

### Título e parágrafo {#title-and-paragraph}

Adiciona texto de título ou parágrafo à mensagem.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botão

Adiciona um botão padrão com estilo, links e análise de dados configuráveis.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

### Botão de opção {#radio-button}

Adiciona uma lista de opções da qual os usuários podem selecionar uma. Quando enviado, o perfil do usuário registra o [atributo personalizado]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) associado, que deve ser uma string para ser salvo. Atributos personalizados com outros tipos de dados não são salvos no perfil do usuário.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Imagem

Insere uma imagem da [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

Para especificações de imagem, consulte nossas [especificações de imagem de mensagens no app]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/image_specifications#in-app-messages).

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link {#link}

Insere um hiperlink que os usuários podem clicar para navegar até uma URL especificada. Pode ser incorporado dentro do texto ou independente.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaçador

Adiciona espaço ou preenchimento entre outros blocos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado {#custom-code}

Insere HTML, CSS ou JavaScript personalizado para personalização avançada.

| Propriedade | Descrição |
| --- | --- |
| Código personalizado | Permite adicionar, editar ou excluir HTML, CSS e JavaScript para uma mensagem no app. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

### Captura de telefone {#phone-capture}

Insere um campo de formulário para números de telefone. Quando enviado, o usuário é inscrito no grupo de inscrições de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups).

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Captura de e-mail {#email-capture}

Insere um campo de formulário para endereços de e-mail. Quando enviado, o endereço de e-mail é adicionado ao perfil desse usuário na Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texto curto {#short-text}

Insere um campo de formulário que aceita atributos padrão (como nome e sobrenome) ou uma string de atributo personalizado de sua escolha.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Menu suspenso {#dropdown}

Insere um menu suspenso com uma lista predefinida de itens da qual os usuários podem selecionar um. Você pode adicionar qualquer string de atributo personalizado à lista.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Caixa de seleção {#checkbox}

Insere uma caixa de seleção. Se o usuário marcar a caixa, o [atributo personalizado booleano]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) do bloco é definido como `true`. Se não for marcado, seu atributo é definido como `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Grupo de caixas de seleção {#checkbox-group}

Os usuários podem selecionar entre várias opções. Os valores são definidos ou adicionados a um [atributo personalizado de array]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) definido.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Texto longo {#long-text}

Campo de texto multilinha para fluxos no estilo de pesquisa. Se você não vir este bloco, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou seu gerente de sucesso do cliente da Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row {#saved-row}

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## Informações importantes {#things-to-know}

- **Vídeo:** O criador padrão não inclui um bloco de vídeo dedicado. Use **Código personalizado** para incorporar um player, se necessário. Para saber mais, consulte [Mensagens no app: perguntas frequentes]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

{% endsdktab %}

{% sdktab landing pages %}
## Blocos do editor de landing pages {#landing-page-editor-blocks}

Os blocos do editor para landing pages ficam na seção **Criar** do **editor de arrastar e soltar**, em **Linhas** e categorias de blocos. Arraste um bloco para uma coluna de linha; ele se ajusta automaticamente à largura da coluna. Selecione um bloco para editar suas configurações no painel de propriedades lateral direito.

Para saber mais sobre como criar e publicar landing pages, consulte [Criar landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).

### Título e parágrafo

Adiciona texto de cabeçalho ou corpo. Útil para estruturar seções e melhorar a legibilidade.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botão

Adiciona um elemento clicável para ações como abrir um link ou enviar um formulário.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

{% alert important %}
Se você configurar um botão com **Enviar formulário ao clicar no botão** e abrir uma URL da web em uma nova guia, o Safari do iOS pode bloquear a navegação. Abra a URL pós-envio na mesma guia ao enviar formulários. Para saber mais, consulte [Criar landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages).
{% endalert %}

### Botão de opção

Adiciona uma lista de opções da qual os usuários podem selecionar uma. Use o painel de propriedades para configurar as opções disponíveis e o atributo personalizado que recebe o valor selecionado. O perfil do usuário registra o valor selecionado como um [atributo personalizado de string]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) quando o formulário é enviado. Atributos personalizados com outros tipos de dados não são salvos no perfil do usuário.

{% multi_lang_include drag_and_drop/editor_block_properties/radio_button_properties.md %}

### Imagem

Exibe uma imagem de um upload ou URL externa.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Adiciona um hiperlink que os usuários podem selecionar para ir a uma URL. Pode ficar dentro do texto ou independente.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaçador

Adiciona espaçamento vertical entre elementos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado

Insere HTML, CSS ou JavaScript personalizado para personalização avançada, como [Google Tag Manager]({{site.baseurl}}/user_guide/messaging/landing_pages#adding-google-tag-manager-to-a-landing-page).

| Propriedade | Descrição |
| --- | --- |
| Código personalizado | Permite adicionar, editar ou excluir HTML, CSS e JavaScript. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

<!-- Countdown timer is not yet released. Uncomment when available.
### Countdown timer {#countdown-timer}

Displays a countdown to a date and time you set. If you don't see this block, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.

After you add a **Countdown timer** block, use the properties panel to set the target date and time, labels, and styling.
-->

### Captura de e-mail

Adiciona um campo de formulário para endereços de e-mail. Ao enviar, o endereço é salvo no perfil do usuário na Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Captura de telefone

Adiciona um campo de formulário para números de telefone. Ao enviar, inscreve o usuário no grupo de inscrições de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups) selecionado.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Campo de entrada {#input-field}

Adiciona um campo de formulário para atributos padrão (por exemplo, nome ou sobrenome) ou uma string de atributo personalizado.

{% multi_lang_include drag_and_drop/editor_block_properties/short_text_properties.md %}

### Menu suspenso

Uma lista predefinida de itens; os usuários escolhem um. Você pode mapear valores para strings de atributo personalizado.

{% multi_lang_include drag_and_drop/editor_block_properties/dropdown_properties.md %}

### Caixa de seleção

Quando marcada, define o [atributo personalizado booleano]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) do bloco como `true`; quando desmarcada, como `false`.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_properties.md %}

### Grupo de caixas de seleção

Os usuários escolhem várias opções; os valores são definidos ou adicionados a um [atributo personalizado de array]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) definido.

{% multi_lang_include drag_and_drop/editor_block_properties/checkbox_group_properties.md %}

### Gerenciar inscrições {#manage-subscriptions}

Adiciona uma lista de verificação de grupos de inscrições de [e-mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) ou [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states) para que os visitantes possam optar por participar ou gerenciar suas inscrições ao enviar o formulário. Cada bloco é para um canal. Configure-o depois de adicionar grupos de inscrições ao bloco. Este bloco não lista grupos de inscrições de RCS.

Para usuários identificados que abrem a página por meio da [Liquid tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) da landing page, o bloco preenche previamente cada caixa de seleção com o estado de inscrição atual do usuário, podendo também servir como uma página de gerenciamento de preferências.

Selecione o bloco no editor para:

- Reordenar grupos de inscrições
- Adicionar ou remover grupos de inscrições
- Adicionar ou remover descrições
- Adicionar ou remover uma caixa de seleção "Inscrever-se em todos" que seleciona todos os grupos de inscrições no bloco

| Propriedade | Descrição |
| --- | --- |
| Grupos de inscrições | Adicione, remova ou reordene os grupos de inscrições exibidos no bloco. |
| Incluir descrições | Exibe a descrição de cada grupo de inscrições ao lado do seu nome. |
| Caixa de seleção **Inscrever-se em todos** | Adiciona uma caixa de seleção que seleciona todos os grupos de inscrições no bloco. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gerenciar inscrições" }

Para o fluxo completo de configuração, consulte [Bloco Gerenciar inscrições]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions).

### Texto longo

Campo de texto multilinha para fluxos no estilo de pesquisa. Se você não vir este bloco, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou seu gerente de sucesso do cliente da Braze. Este bloco não está disponível para landing pages padrão.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## Informações importantes

- **Vídeo:** O criador padrão não inclui um bloco de vídeo dedicado. Use **Código personalizado** para incorporar um player, se necessário. Para saber mais, consulte [Landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages).

{% endsdktab %}

{% sdktab banners %}
## Blocos do editor de Banner {#banner-editor-blocks}

No criador de Banner, arraste linhas e blocos da seção **Criar** para o canvas para organizar o layout da sua mensagem. Selecione **Estilos** para ajustar o estilo no nível da página, ou selecione um bloco ou linha para editar suas propriedades no painel lateral.

Para o fluxo completo de criação de Banner, consulte [Criar um Banner]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner).

O criador de Banner oferece os mesmos tipos de blocos de layout que outras superfícies de arrastar e soltar, mas não o conjunto completo de blocos de formulário (por exemplo, sem blocos de botão de opção, texto curto, menu suspenso ou caixa de seleção). Você pode adicionar blocos de **Captura de telefone** e **Captura de e-mail**; apenas **um** bloco de captura de telefone e **um** de captura de e-mail são permitidos por mensagem.

### Título e parágrafo

Adiciona texto de cabeçalho ou corpo com opções de texto rico.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botão

Adiciona um botão clicável. Você pode definir links e opções de análise de dados no painel de propriedades.

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/button_actions.md %}

Para saber mais, consulte [Definir comportamento ao clicar]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional) no artigo sobre Banner.

### Imagem

Exibe uma imagem de uma URL hospedada. Configure as opções de exibição no painel de propriedades.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/image_actions.md %}

### Link

Insere um hiperlink que os usuários podem selecionar.

{% multi_lang_include drag_and_drop/editor_block_properties/link_properties.md %}

#### Comportamento ao clicar

{% multi_lang_include drag_and_drop/editor_block_properties/link_actions.md %}

### Espaçador

Adiciona espaçamento vertical entre blocos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Código personalizado

Insere HTML personalizado para layouts avançados ou conteúdo incorporado (por exemplo, vídeo). Cliques dentro de HTML personalizado não são rastreados a menos que você chame `brazeBridge.logClick()` — consulte [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/custom_code).

| Propriedade | Descrição |
| --- | --- |
| Código personalizado | Adicione ou edite HTML (e ativos relacionados) para o Banner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Código personalizado" }

### Captura de telefone

Coleta um número de telefone. Ao enviar, inscreve o usuário no grupo de inscrições de [SMS]({{site.baseurl}}/sms_rcs_subscription_groups) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups) selecionado. Apenas um por Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/phone_capture.md %}

### Captura de e-mail

Coleta um endereço de e-mail e o adiciona ao perfil do usuário na Braze ao enviar. Apenas um por Banner.

{% multi_lang_include drag_and_drop/editor_block_properties/email_capture.md %}

### Texto longo

Campo de texto multilinha para fluxos no estilo de pesquisa. Se você não vir este bloco, entre em contato com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) ou seu gerente de sucesso do cliente da Braze.

{% multi_lang_include drag_and_drop/editor_block_properties/long_text.md %}

<!-- Saved row is not yet released. Uncomment when available.
### Saved row

Inserts a reusable row you saved earlier as a drag-and-drop Content Block. Saved rows are **not linked** to the original Content Block — if the original is updated, you'll need to drag it into the editor again to get the latest version. For more information, see [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). If you don't see **Saved row** under **Rows**, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) or your Braze customer success manager.
-->

## Informações importantes

- **Vídeo:** O criador padrão não inclui um bloco de vídeo dedicado. Use **Código personalizado** para incorporar um player, se necessário. Para saber mais, consulte [Banners: perguntas frequentes]({{site.baseurl}}/user_guide/channels/banners/faq).
- **Liquid:** A maioria do Liquid é compatível; há exceções como tags de re-renderização de catálogo. Para saber mais, consulte [Banners: perguntas frequentes]({{site.baseurl}}/user_guide/channels/banners/faq).

{% endsdktab %}

{% sdktab preference center %}
## Blocos do editor da Central de Preferências {#preference-center-editor-blocks}

Arraste blocos da seção **Criar** para uma linha no editor de arrastar e soltar da Central de Preferências. Cada bloco tem suas próprias configurações; o painel lateral direito alterna para propriedades ou estilo do elemento selecionado.

Antes de editar blocos, adicione grupos de inscrições e configure o **bloco inteligente** de inscrição (veja a seção a seguir). Para o fluxo completo de configuração, consulte [Criar uma Central de Preferências de e-mail com arrastar e soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center).

### Título e parágrafo

Adiciona texto de cabeçalho ou corpo com opções de texto rico.

{% multi_lang_include drag_and_drop/editor_block_properties/title_paragraph.md %}

### Botão

Adiciona um botão clicável (por exemplo, **Salvar** ou navegação).

{% multi_lang_include drag_and_drop/editor_block_properties/button_properties.md %}

### Imagem

Exibe uma imagem da [biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) ou de uma URL.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% multi_lang_include drag_and_drop/editor_block_properties/image_properties.md %}

### Espaçador

Adiciona espaçamento vertical entre blocos.

{% multi_lang_include drag_and_drop/editor_block_properties/spacer.md %}

### Grupos de inscrições (bloco inteligente) {#subscription-groups-smart-block}

Adiciona um bloco de modelo que lista grupos de inscrições, controles opcionais de **Inscrever-se em todos** / **Cancelar inscrição de todos** e descrições. Configure-o depois de adicionar grupos no fluxo de trabalho da Central de Preferências.

Depois de [adicionar grupos de inscrições]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-3-add-subscription-groups-to-the-preference-center), selecione o bloco inteligente no canvas para:

- Reordenar grupos de inscrições
- Adicionar ou remover grupos
- Adicionar ou remover descrições
- Alternar **Inscrever-se em todos** e **Cancelar inscrição de todos** para os grupos nesse bloco

O controle **Cancelar inscrição de todos** na parte inferior do modelo padrão é obrigatório e realiza um [cancelamento global de inscrição]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) de e-mail.

## Informações importantes

- **Estilos comuns:** Você pode definir padrões para toda a página em **Estilos comuns** antes de ajustar blocos individuais. Para saber mais, consulte [Personalizar a Central de Preferências usando o editor de arrastar e soltar]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center#step-4-customize-the-preference-center-using-the-drag-and-drop-editor).
- **Página de confirmação:** Alterne para **Página de confirmação** na parte superior do editor para estilizar a experiência pós-salvamento usando os mesmos tipos de bloco.

{% endsdktab %}

{% endsdktabs %}