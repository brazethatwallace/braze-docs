---
nav_title: Criar landing pages
article_title: Criar landing pages
description: "Este artigo aborda como criar e personalizar landing pages da Braze com o editor de arrastar e soltar."
page_order: 0
---

# Criar landing pages {#create-landing-pages}

> Saiba como criar e personalizar uma landing page usando o editor de arrastar e soltar para expandir seu público e coletar preferências diretamente na Braze.

## Pré-requisitos {#prerequisites}

Para acessar o construtor de landing pages, você precisa de [determinadas permissões]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites). Se você não tiver acesso, peça ajuda ao administrador da Braze.

## Criar uma landing page {#create-a-landing-page}

Uma landing page é uma página web ativa e publicada com uma URL compartilhável que seus clientes podem visitar.

{% alert note %}
Os modelos de landing page são pontos de partida de design não publicados, sem URL pública, o que significa que não podem ser compartilhados com seus clientes. Para criar uma página a partir de um modelo, consulte [Usando modelos](#using-templates).
{% endalert %}

### Etapa 1: Criar um novo rascunho {#step-1-create-a-new-draft}

Acesse **Messaging** > **Landing Pages** e selecione **Create landing page**. Você também pode selecionar o nome de uma landing page existente para duplicá-la ou fazer alterações.

### Etapa 2: Inserir os detalhes da página {#step-2-enter-the-page-details}

Adicione detalhes internos e públicos que ajudam a organizar, personalizar a marca e compartilhar sua landing page.

#### Detalhes gerais {#general-details}

Insira um nome e uma descrição para a landing page. Esses detalhes são usados para pesquisar a página no seu espaço de trabalho interno. Eles não serão visíveis para seus clientes.

#### Detalhes do site {#site-details}

Configure metatags para personalizar como sua página aparece na guia do navegador e otimizar para resultados de mecanismos de busca. Esses detalhes serão visíveis para seus clientes.

Sugerimos seguir estas práticas recomendadas:

| Campo | Descrição | Recomendações |
| --- | --- | --- |
| Título do site | O título exibido na guia do navegador. | Use até 60 caracteres. |
| Meta descrição | Um snippet de texto exibido nos resultados de busca. | Use entre 140 e 160 caracteres. |
| Favicon | O ícone que aparece ao lado do título do site na guia do navegador. | Use uma proporção de 1:1 e um tipo de arquivo compatível: PNG, JPEG ou ICO. |
| URL da página | Este é o caminho da URL para sua landing page. Esse valor também é referenciado ao usar [Liquid tags de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) que você pode incorporar em uma mensagem para identificar automaticamente quando os usuários enviam seu formulário. | Esse valor deve ser único em todo o seu espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Detalhes do site" }

### Etapa 3: Personalizar a página {#step-3-customize-the-page}

Se ainda não fez isso, selecione **Save as draft**. Para começar a personalizar sua página, selecione **Edit landing page**. O editor de arrastar e soltar será pré-carregado com um modelo padrão que você pode personalizar para se adequar ao seu caso de uso.

![Um exemplo de landing page sendo criada no editor de arrastar e soltar.]({% image_buster /assets/img/landing_pages/template.png %})

O editor usa dois tipos de componentes para a composição de landing pages: blocos básicos e blocos de formulário. Todos os blocos devem ser colocados em uma linha. Para uma referência dedicada de cada bloco e suas propriedades, consulte [Blocos do editor (landing pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).

![A seção "Build" contendo "Rows" e "Form Blocks".]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

{% tabs %}
{% tab Blocos básicos %}

Você pode usar esses blocos para adicionar conteúdo e personalizar o layout da sua landing page.

| Tipo de bloco | Descrição |
|-------------|-------------|
| Título | Um bloco de texto para adicionar um cabeçalho ou título ao seu conteúdo. Útil para estruturar seções e melhorar a legibilidade. |
| Parágrafo | Um bloco de texto para descrições mais longas ou contexto adicional. Suporta formatação de rich text. |
| Botão | Um elemento clicável que direciona os usuários para uma ação específica, como abrir um link ou enviar um formulário. |
| Botão de opção | Adiciona uma lista de opções das quais os usuários podem selecionar uma. Quando enviado, o perfil do usuário registra o atributo personalizado associado. |
| Imagem | Um bloco para exibir imagens. Você pode fazer upload de uma imagem ou fornecer uma URL para referenciar uma fonte externa. |
| Link | Um hiperlink que os usuários podem clicar para navegar até uma URL especificada. Pode ser incorporado dentro do texto ou independente. |
| Espaçador | Um bloco invisível que adiciona espaçamento vertical entre elementos para melhorar o layout e a legibilidade. |
| Código personalizado | Um bloco que permite inserir e executar HTML, CSS ou JavaScript personalizados para personalização avançada. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Personalizar a página" }

#### Texto com span {#span-text}

Para aplicar estilos específicos a blocos de texto sem código personalizado, destaque o texto que deseja estilizar e selecione **Wrap with span for style**.

![Caixa de texto com diferentes seções de texto estilizadas, como diferentes tamanhos e cores de fonte, e uma seção destacada que exibe uma barra de ferramentas com a opção "Wrap with span for style".]({% image_buster /assets/img/landing_pages/wrap_with_span.png %}){: style="max-width:50%;"}

Ajuste as propriedades do span para atualizar o estilo do texto, incluindo:

- Família, peso e tamanho da fonte
- Altura da linha
- Espaçamento entre letras
- Alinhamento e cor do texto
- Preenchimento do bloco

![Painel de propriedades do span com diferentes opções para atualizar.]({% image_buster /assets/img/landing_pages/span_properties.png %}){: style="max-width:35%;"}


{% endtab %}
{% tab Blocos de formulário %}

Você pode usar esses blocos para criar um formulário que vincula os dados enviados pelo usuário ao perfil dele na Braze. Lembre-se de que, se você usar blocos de formulário, também precisará criar uma landing page adicional para o estado de confirmação.

![Um bloco de formulário que registra um novo cliente e enviará um código de desconto para o e-mail dele.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Tipo de bloco | Descrição |
|---------------|-------------|
| Captura de e-mail | Um campo de formulário para endereços de e-mail. Quando enviado, o endereço de e-mail é adicionado ao perfil desse usuário na Braze. |
| Captura de telefone | Um campo de formulário para números de telefone. Quando enviado, o usuário é inscrito no seu grupo de inscrições de SMS ou WhatsApp. |
| Campo de entrada | Um campo de formulário que suporta atributos padrão (como nome e sobrenome) ou uma string de atributo personalizado de sua escolha. |
| Menu suspenso | Os usuários podem selecionar um item de uma lista predefinida. Você pode adicionar qualquer string de atributo personalizado à lista. |
| Caixa de seleção | Se um usuário marcar a caixa, o atributo do bloco é definido como `true`. Se não for marcada, o atributo é definido como `false`. |
| Grupo de caixas de seleção | Os usuários podem selecionar entre várias opções apresentadas. Os valores são definidos ou adicionados a um atributo personalizado de array definido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Texto com span" }

{% alert important %}
Após criar uma landing page com um formulário, certifique-se de incorporar a [Liquid tag de landing page]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) na sua mensagem. Com essa tag, a Braze pode identificar e atualizar automaticamente os perfis de usuário existentes quando eles enviam o formulário.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Estilos do contêiner da página {#page-container-styles}

Você pode definir estilos a serem aplicados em todos os blocos de componentes relevantes na sua landing page a partir da guia **Page container**. Esses estilos se aplicam em toda a página, exceto onde você os substituir com um bloco específico.

Recomendamos configurar os estilos no nível do contêiner da página antes de personalizar os estilos no nível do bloco. Você também pode adicionar uma imagem de fundo para a página inteira.

![A seção "Page container" com opções para personalizar imagens de fundo, cores, detalhes de borda e estilo de conteúdo.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:40%;"}

#### Responsivo aos dispositivos dos usuários {#responsive-to-user-devices}

Você pode tornar sua landing page responsiva ao tamanho do dispositivo do usuário empilhando colunas verticalmente em telas menores. Para ativar isso, adicione uma coluna na linha que deseja tornar responsiva e ative **Vertically stack on smaller screens** na seção **Customize columns**.

Quando ativado, você também pode inverter a ordem de empilhamento das colunas para controlar a ordem vertical do conteúdo de múltiplas colunas em telas menores. Isso faz com que as páginas tenham uma aparência e experiência melhores em dispositivos móveis sem código personalizado.

![O botão "Vertically stack on smaller screens" na seção "Customize columns".]({% image_buster /assets/img/landing_pages/device_responsive_toggle.png %}){: style="max-width:50%;"}

{% multi_lang_include drag_and_drop/hide_rows_and_blocks_by_device.md channel='landing_page' %}

#### Campos opcionais e obrigatórios {#optional-and-required-fields}

Você pode escolher se um campo de formulário é obrigatório ou opcional. Campos obrigatórios devem ser preenchidos antes que o formulário possa ser enviado. Campos opcionais podem ser deixados em branco ou não selecionados pelo usuário.

Por exemplo, para exigir a captura de consentimento antes do envio do formulário, você pode ativar **Required field input** para definir uma caixa de seleção como obrigatória com o texto de aviso apropriado.

![Um campo de formulário de caixa de seleção com o botão "Required input field" selecionado.]({% image_buster /assets/img/landing_pages/lp-optional-required.png %}){: style="max-width:50%;"}

### Etapa 4: Criar uma página de confirmação (opcional) {#step-4-create-a-confirmation-page-optional}

Se sua landing page não inclui um formulário, continue para a próxima etapa.

Se sua landing page inclui um [formulário](#form-blocks), crie uma segunda landing page para servir como experiência de confirmação. Essa página deve agradecer aos usuários ou fornecer um próximo passo após o envio do formulário.

Para vincular a página de confirmação:
- Selecione o botão **Submit** no seu formulário
- Use a ação **Open web URL** para vincular à sua página de confirmação

Se você não incluir uma página de confirmação, os usuários podem não saber que o formulário foi enviado com sucesso. Sempre inclua uma experiência de confirmação para completar a jornada.

{% alert note %}
Se sua página de confirmação abrir em uma nova guia, um usuário que retornar à landing page original e reenviar com informações atualizadas pode sobrescrever o envio anterior, resultando em dados inconsistentes.
{% endalert %}

### Etapa 5: Visualizar a página {#step-5-preview-the-page}

Você pode visualizar sua landing page na guia **Preview** do editor. Após salvar sua landing page como rascunho, você pode visitar a URL acessando **Landing Pages** e selecionando **Copy URL** ao lado da sua landing page.

![Uma landing page com o menu aberto mostrando a opção "Copy URL".]({% image_buster /assets/img/landing_pages/copy-url.png %})

#### Compartilhar um link de prévia {#sharing-a-preview-link}

No editor, você também pode selecionar **Copy preview link** para compartilhar a página com revisores que não têm acesso ao dashboard.

- Se sua landing page não usa Liquid, esse link é o mesmo que a URL direta de **Copy URL**, aberta no modo de prévia.
- Se sua landing page usa Liquid e você tem o direito Landing Pages Pro, o link renderiza a página ativa sob demanda e reflete suas alterações atuais em vez de um snapshot de quando você gerou o link. O conteúdo é personalizado por usuário.

Para links de prévia em outros canais, consulte [prévia compartilhável]({{site.baseurl}}/user_guide/messaging/governance/shareable_preview).

### Etapa 6: Publicar {#step-6-publish}

Antes de publicar, certifique-se de que:

- Você não excedeu o limite de landing pages publicadas do seu plano
- Cada página baseada em formulário está vinculada a uma [página de confirmação](#step-4-create-a-confirmation-page) usando a ação **Open web URL**
- Todos os campos obrigatórios da página (como caminho da URL e título) estão completos

Quando estiver pronto, selecione **Publish Landing Page**.

{% alert note %}
Bloqueadores de pop-up e bloqueadores de anúncios agressivos no iOS e no Safari (incluindo os controles integrados do Safari e extensões de terceiros) podem impactar negativamente o comportamento das landing pages quando um botão **Submit** do formulário também abre outra URL, seja na mesma guia ou em uma nova guia.
{% endalert %}

## Usar modelos {#use-templates}

Os modelos de landing page são pontos de partida de design reutilizáveis que ajudam você a criar landing pages mais rapidamente. Um modelo não tem URL pública e não pode ser visitado por clientes. Para criar uma landing page ativa a partir de um modelo, selecione o modelo ao criar uma nova landing page, personalize conforme necessário e publique.

Os modelos podem ser acessados e gerenciados tanto no editor de landing pages quanto na página **Landing Page Templates** (**Content** > **Landing Page**). Os modelos de landing page exigem um nome e uma descrição opcional.

## Gerenciar modelos {#manage-templates}

Você pode visualizar, arquivar ou editar modelos de landing page. É possível duplicar seus próprios modelos de landing page (localizados em **Seus Modelos**), mas não os modelos da Braze. Ao editar uma landing page, você pode salvar sua landing page como modelo, fazer alterações no modelo ou excluir o conteúdo da landing page.

![Um menu suspenso com opções para salvar, alterar e excluir uma landing page.]({% image_buster /assets/img/landing_pages/manage-lp-template.png %}){: style="max-width:60%;"}

## Visualizar análise de dados {#view-analytics}

Para analisar a eficácia da sua landing page, acesse **Messaging** > **Landing Pages** e selecione uma landing page que você publicou. Aqui, você pode acompanhar o número de visualizações de página, cliques na página, envios de formulário e as taxas de envio da sua landing page.

![A seção de análise de dados de uma landing page.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Lidar com erros de envio de formulário {#handling-form-submission-errors}

Se um usuário tentar enviar um formulário com campos ausentes ou entradas não suportadas, ele verá uma mensagem de erro genérica e não conseguirá enviar.

Causas comuns:

- Campos obrigatórios estão em branco
- Caracteres especiais são usados em campos de texto
- Uma caixa de seleção obrigatória não está marcada

As mensagens de erro exibidas aos usuários não podem ser personalizadas. Visualize sua landing page para confirmar o comportamento dos campos antes de publicar.