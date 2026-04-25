## Usando blocos de editor de e-mail {#using-email-editor-blocks}

Os blocos de editor estão localizados na seção **Conteúdo** para mensagens de e-mail. Para usar um bloco de editor, arraste um bloco de editor para dentro de uma coluna no editor de arrastar e soltar. Ele se ajustará automaticamente à largura da coluna. Cada bloco do editor tem suas próprias configurações, como o controle granular do preenchimento.

Para saber mais sobre como usar e personalizar esses blocos de editor em seu e-mail, confira [Outras personalizações]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/#other-customizations).

{% alert tip %}
Você também pode adicionar [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) a qualquer URL dentro dos blocos de editor `Image`, `Button` ou `Text`.
{% endalert %}

## Tipos {#types}

A tabela a seguir descreve como os usuários podem usar cada tipo de bloco de editor.

| Nome | Descrição |
|---|---|
|Título| Adiciona texto para cabeçalhos dentro do e-mail. |
|Parágrafo| Insere texto na mensagem. Uma barra de ferramentas ajuda na funcionalidade de edição de texto e fontes. |
|Lista| Adiciona uma lista com marcadores. |
|Botão| Adiciona um botão padrão. As propriedades desse bloco permitem editar e definir links facilmente. |
|Divisor| Insere uma linha sólida, pontilhada ou tracejada para ajudar no espaçamento.|
|Espaçador| Adiciona espaço, ou "padding", entre outros blocos. |
|Imagem| Insere uma imagem da [Biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). |
|Vídeo| Cria um link para o conteúdo do vídeo. |
|Redes sociais| Insere o ícone da plataforma de redes sociais. Você pode fazer upload de imagens personalizadas para ícones específicos da marca. |
|Ícones| Insere um ícone. Você pode fazer upload de imagens personalizadas. A Braze usa um ícone de espaço reservado grande até que você faça upload de uma imagem. |
|HTML| Insere HTML bruto. Recomendado para [Liquid]({{site.baseurl}}/liquid/), como Conteúdo conectado ou declarações condicionais. |
|Menu| Cria um menu flexível para a mensagem que você está projetando. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Personalização em e-mail {#personalization-in-email}

- **Liquid:** Em **Conteúdo** > **Personalização**, selecione um atributo, copie o snippet e cole-o em um bloco de texto (Liquid básico) ou bloco HTML (Liquid avançado). Em geral, embora você possa usar Liquid básico em blocos de texto, recomendamos usar blocos HTML para lógicas mais complexas, a fim de evitar problemas de layout. Note que o Liquid não é compatível com blocos de imagem ou campos de URL de botão.
- **Conteúdo conectado:** Adicione um bloco **HTML** e insira sua chamada {% raw %}`{% connected_content %}`{% endraw %} nele.

## Propriedades {#properties}

Os detalhes das propriedades de cada bloco de editor são fornecidos nas tabelas a seguir.

### Título {#title}
Consulte a tabela a seguir para obter detalhes sobre as propriedades do bloco do editor `Title`.

| Propriedades | Descrição |
|---|---|
|Título| Seleciona o estilo do cabeçalho. |
|Família da fonte| Esse é o estilo da fonte do seu título. |
|Peso da fonte| Esse é o grau de negrito da fonte. |
|Tamanho da fonte| Determina o tamanho do seu texto. |
|Cor do texto| Modifica a cor do título. |
|Cor do link| Modifica a cor do link. |
|Alinhar| Move o título para a esquerda, centro ou direita. |
|Altura da linha| Modifica a distância entre as linhas de texto. |
|Espaçamento de linha| Modifica a distância entre cada caractere. |
|Direção do texto| Padrão da esquerda para a direita, mas pode ser editado para ser [da direita para a esquerda]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Parágrafo {#paragraph}

Consulte a tabela a seguir para obter detalhes sobre as propriedades do bloco do editor `Paragraph`.

| Propriedades | Descrição |
|---|---|
|Família da fonte| Esse é o estilo da fonte do texto do parágrafo. |
|Peso da fonte| Esse é o grau de negrito da fonte. |
|Tamanho da fonte| Determina o tamanho do seu texto. |
|Cor do texto| Modifica a cor do título. |
|Cor do link| Modifica a cor do link. |
|Alinhar| Move o título para a esquerda, centro ou direita. |
|Espaçamento de parágrafo| Modifica o espaço entre os parágrafos. |
|Altura da linha| Modifica a distância entre as linhas de texto. |
|Espaçamento entre letras| Modifica a distância entre cada caractere. |
|Direção do texto| Padrão da esquerda para a direita, mas pode ser editado para ser [da direita para a esquerda]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lista {#list}

Consulte a tabela a seguir para obter detalhes sobre as propriedades do bloco do editor `List`.

| Propriedades | Descrição |
|---|---|
|Tipo de lista| Esse é o tipo de lista. Pode ser com marcadores ou numerada. |
|Tipo de estilo de lista| Determina o estilo da sua lista. |
|Iniciar lista a partir de| Determina o número inicial da sua lista. |
|Família da fonte| Esse é o estilo da fonte do texto do parágrafo. |
|Peso da fonte| Esse é o grau de negrito da fonte. |
|Tamanho da fonte| Determina o tamanho do seu texto. |
|Cor do texto| Modifica a cor do título. |
|Cor do link| Modifica a cor do link. |
|Alinhar| Move o título para a esquerda, centro ou direita. |
|Espaçamento dos itens da lista| Modifica o espaço entre os itens da lista. |
|Recuo dos itens da lista| Modifica o recuo dos itens da lista. |
|Altura da linha| Modifica a distância entre as linhas de texto. |
|Espaçamento entre letras| Modifica a distância entre cada caractere. |
|Direção do texto| Padrão da esquerda para a direita, mas pode ser editado para ser [da direita para a esquerda]({{site.baseurl}}/right_to_left_messages/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Divisor {#divider}

Consulte a tabela a seguir para obter detalhes sobre o bloco do editor `Divider`.

| Propriedades | Descrição |
|---|---|
|Transparente| Se ativada, as opções "line" e "width" serão removidas. |
|Linha| Os diferentes formatos de linha, seja pontilhada, tracejada ou sólida. Além disso, você pode modificar a espessura e a cor da linha divisória. |
|Largura | Ajusta a extensão do divisor em incrementos de 5.  |
|Alinhar| Move a linha para a esquerda, para o centro ou para a direita. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Espaçador {#spacer}

Consulte a tabela a seguir para obter detalhes sobre o bloco do editor `Spacer`.

| Propriedades | Descrição |
|---|---|
|Altura| Ajusta a altura do bloco espaçador. O padrão é 60px.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Imagem {#image}

Consulte a tabela a seguir para obter detalhes sobre o bloco do editor `Image`. Para imagens dinâmicas (imagens com Liquid ou Conteúdo conectado), você deve definir uma imagem de fallback para usar as configurações de largura automática. Para especificações de imagem, consulte nossas [especificações de imagem de e-mail]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#email).

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propriedades | Descrição |
|---|---|
|Largura automática| Modifica a largura da imagem em pixels. |
|Alinhar| Orienta a imagem para a esquerda, centro ou direita do bloco. |
|Imagem com Liquid| Use a lógica [Liquid]({{site.baseurl}}/liquid/) para definir dinamicamente diferentes imagens dentro do mesmo bloco de conteúdo. |
|URL| Defina uma imagem usando o endereço onde está hospedada. |
|Texto alternativo| Uma breve descrição da imagem que fornece aos usuários as mesmas informações mostradas na imagem. Isso é essencial para a acessibilidade de leitores de tela ou quando a imagem não carrega. |
|Imagem com cantos arredondados| Renderiza a imagem com cantos arredondados. Por padrão, as imagens são renderizadas com cantos quadrados. |
|Ação| Aciona uma ação quando o usuário clica na imagem.|
|Opções do bloco| Define o preenchimento ao redor do bloco da imagem. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para `Auto Width`, o redimensionamento automático da imagem escolhe o melhor tamanho para a imagem com base em uma combinação da largura da imagem e do espaço disponível no layout:
- As imagens mais largas do que o espaço disponível serão definidas com 100% de largura e manterão essa proporção no celular, usando toda a largura da tela do dispositivo.
- Imagens menores do que o espaço disponível usarão o tamanho natural da imagem para evitar efeitos de distorção ou imagens borradas.
{% endalert %}

### Vídeo {#video}

Consulte a tabela a seguir para obter detalhes sobre o bloco do editor `Video`.

| Propriedades | Descrição |
|---|---|
|URL| O URL do vídeo. Note que apenas o YouTube e o Vimeo são compatíveis. |
|Título| Gerado automaticamente a partir dos metadados do vídeo ou pode ser personalizado. |
|Estilo do ícone de reprodução| Inclui diferentes opções para o botão de reprodução localizado na parte superior de uma imagem de vídeo. |
|Cor do ícone de reprodução| Opção para selecionar **Claro** ou **Escuro** para o botão de reprodução. |
|Tamanho do ícone de reprodução| Escolha o tamanho em pixels para o botão de reprodução. Intervalo pré-fixado de 50&nbsp;px a 80&nbsp;px (incrementado em 5&nbsp;px). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Os vídeos hospedados pelo Vimeo só funcionarão se estiverem definidos como públicos. Todas as outras configurações de segurança disponíveis no Vimeo (por exemplo, "Hide from Vimeo.com") gerarão um formato de link diferente que não é compatível com este bloco de conteúdo. Esses tipos de links são alterados pelo construtor, o que impede a Braze de gerar uma miniatura.
{% endalert %}

### Redes sociais {#social}

Consulte a tabela a seguir para obter detalhes sobre o bloco do editor `Social`.

| Propriedades | Descrição |
|---|---|
|Selecione a coleção de ícones| Define o estilo da sua coleção de ícones. |
|Configure a coleção de ícones| Define o URL de cada ícone social. Inclui o botão de alternância **Mais opções** para editar o título e o texto alternativo. |
|Alinhar| Move o ícone social para a esquerda, centro ou direita. |
|Espaçamento do ícone| Determina o espaçamento entre cada ícone social. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ícones {#icons}

Consulte a tabela a seguir para obter detalhes sobre o bloco do editor `Icons`.

| Propriedades | Descrição |
|---|---|
|Família da fonte| Esse é o estilo da fonte do texto do parágrafo. |
|Peso da fonte| Esse é o grau de negrito da fonte. |
|Tamanho da fonte| Determina o tamanho do seu texto. |
|Cor do texto| Modifica a cor do título. |
|Cor do link| Modifica a cor do link. |
|Alinhar| Move o ícone para a esquerda, centro ou direita. |
|Espaçamento entre letras| Modifica a distância entre cada caractere. |
|Tamanho do ícone| Determina o tamanho do seu ícone. |
|Espaçamento do ícone| Modifica o espaço do ícone. |
|Preenchimento do ícone| Modifica o preenchimento do ícone. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML

Consulte a tabela a seguir para obter detalhes sobre o bloco do editor `HTML`.

| Propriedades | Descrição |
|---|---|
|Editor de HTML| Digite o HTML bruto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Menu

Consulte a tabela a seguir para obter detalhes sobre o bloco do editor `Menu`.

| Propriedades | Descrição |
|---|---|
|Configurar itens do menu| Adiciona um item de menu. |
|Família da fonte| O estilo a ser usado no seu menu. |
|Tamanho da fonte| O tamanho do seu menu. |
|Cor do texto| Modifica a cor do menu. |
|Cor do link| Modifica a cor do texto do menu. |
|Alinhar| Move o menu para a esquerda, centro ou direita. |
|Espaçamento entre letras| Modifica a distância entre cada caractere. |
|Disposição| Determina que a disposição seja horizontal ou vertical. |
|Separador| Adiciona caractere(s) entre as opções de menu. |
|Menu móvel| Inclui opções para modificar o tamanho, a cor e o tipo do ícone quando exibido em um dispositivo móvel. |
|Preenchimento do item| Modifica o preenchimento usando o botão **+** ou **-** ou inserindo um número específico. |
|Todos os lados| Define um número de preenchimento consistente se o preenchimento do item estiver desativado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ações {#actions}

Você pode atribuir uma ação que ocorre quando um usuário toca em um botão, link ou imagem na mensagem. Você também pode usar [Liquid]({{site.baseurl}}/liquid/) para personalizar as ações. Os detalhes das ações de cada bloco de editor são fornecidos nas tabelas a seguir.

### Botão {#button}

Consulte a tabela a seguir para obter detalhes sobre o bloco do editor `Button`.

| Propriedades | Descrição |
|---|---|
|Tipo de link| Determina a ação ao clicar no botão e define o protocolo apropriado. |
|URL| Dinâmico com base no tipo de link **Abrir página da web**.|
|Para, Assunto e Corpo| Para o tipo de link **Enviar e-mail**, define o endereço de e-mail do destinatário, o assunto e o conteúdo que serão preenchidos em um rascunho de e-mail quando o usuário selecionar o botão.|
|Tel| Para os tipos de link **Fazer chamada** e **Enviar SMS**, define o número de telefone para o qual o usuário ligará ou enviará mensagem ao selecionar o botão.|
|Mensagem| Para o tipo de link **Enviar SMS**, define o conteúdo que será preenchido em um rascunho de mensagem SMS quando o usuário selecionar o botão.|
|Opções do botão| Define várias opções do botão, como fonte, largura, cor e outras.|
|Passar o mouse sobre o botão| O estilo do botão quando um usuário passa o mouse sobre ele usando um mouse ou trackpad. Isso inclui a cor de fundo do botão, a cor da fonte e os estilos de borda.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }