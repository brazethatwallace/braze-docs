---
nav_title: Blocos de produto
article_title: Blocos de produto de arrastar e soltar
page_order: 5
description: "Este artigo de referência aborda os blocos de produto de arrastar e soltar, que permitem aos usuários adicionar e configurar rapidamente vitrines dinâmicas ou estáticas de itens do catálogo."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# Blocos de produto de arrastar e soltar {#drag-and-drop-product-blocks}

> O editor de arrastar e soltar permite que você adicione e configure rapidamente blocos de produto nas suas mensagens para vitrines de produtos integradas, sem precisar criar código Liquid personalizado.

{% alert important %}
O recurso de bloco de produto de arrastar e soltar está em acesso antecipado e, no momento, está disponível apenas para e-mail. Fale com o gerente da sua conta na Braze se tiver interesse em participar do acesso antecipado.
{% endalert %}

## Requisitos {#requirements}

| Requisito | Descrição |
| --- | --- |
| Eventos recomendados de eCommerce | Os [eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_events/) fornecem esquemas de dados padronizados para eventos comportamentais importantes que ocorrem antes e depois de um pedido ser realizado. Esses eventos eventualmente substituirão o evento de compra legado da Braze e se tornarão o padrão para rastreamento de comportamento relacionado a comércio. <br><br> Os eventos recomendados de eCommerce são obrigatórios para blocos de produto dinâmicos. |
| Modelos de Canvas de eCommerce | Os eventos recomendados de eCommerce oferecem suporte a modelos pré-construídos, incluindo modelos de Canvas de eCommerce projetados para casos de uso essenciais, como navegação abandonada, carrinho abandonado e confirmações de pedido. <br><br>Se você planeja implementar qualquer um desses casos de uso essenciais de eCommerce usando os [modelos de Canvas de eCommerce]({{site.baseurl}}/ecommerce_use_cases/), é necessário usar ou seguir o modelo de Canvas fornecido. |
| Catálogo da Braze | Você precisa criar um catálogo da Braze que inclua os seguintes campos, que serão usados na configuração do seu bloco de produto:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| Seleção de catálogo | Para blocos de produto estáticos, você precisa criar uma [seleção de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para especificar quais produtos incluir no seu bloco de produto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requirements" }

## Tipos de blocos de produto de arrastar e soltar {#types-of-drag-and-drop-product-blocks}

| Bloco de produto | Finalidade | Casos de uso | Disponibilidade |
| --- | --- | --- | --- |
| Dinâmico | Personalize suas mensagens com uma vitrine de produtos baseada nas interações do cliente, usando [eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_events/) e catálogos dentro dos nossos [modelos de Canvas de eCommerce]({{site.baseurl}}/ecommerce_use_cases/). | {::nomarkdown}<ul><li>Navegação abandonada</li><li>Carrinho abandonado</li><li>Checkout abandonado</li><li>Confirmações de pedido</li></ul>{:/} | Disponível apenas em Canvas. |
| Estático | Personalize produtos usando dados armazenados em um catálogo da Braze. Você precisa usar uma [seleção de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para especificar quais produtos incluir. | Ideal para destacar lançamentos de novos produtos ou ofertas específicas por categoria. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Types of drag-and-drop product blocks" }

## Configuração de conteúdo do bloco de produto {#product-block-content-configuration}

Cada tipo de bloco tem configurações de conteúdo diferentes.

### Campos de produto {#product-fields}

Na seção **Product Fields**, selecione o tipo de bloco de produto e ative os campos que deseja incluir para cada produto. Cada campo é extraído de fontes diferentes com base no tipo de bloco de produto selecionado.

#### Bloco de produto dinâmico {#dynamic-product-block}

| Campo de produto | Origem |
| --- | --- |
| Imagem da variante | Catálogos |
| Título do produto | Catálogos |
| Botão para URL do produto | Catálogos |
| Preço | Propriedade do evento recomendado de eCommerce |
| Quantidade | Propriedade do evento recomendado de eCommerce |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dynamic product block" }

![Campos de produto para um bloco de produto dinâmico, divididos em dados do catálogo e dados do evento.]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### Bloco de produto estático {#static-product-block}

| Campo de produto | Origem |
| --- | --- |
| Imagem da variante | Catálogos |
| Título do produto | Catálogos |
| Botão para URL do produto | Catálogos |
| Preço | Catálogos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Static product block" }

![Campos de produto para um bloco de produto estático, todos categorizados como dados do catálogo.]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### Opções de layout {#layout-options}

Use as opções de layout para personalizar como seus produtos são exibidos dentro do bloco de produto.

| Opção | Descrição |
| --- | --- |
| Orientação do produto | Escolha como a imagem e os campos de produto dentro do bloco são orientados. |
| Alinhamento | Ajuste o alinhamento dos campos de texto e do botão dentro do bloco. |
| Máximo de produtos por linha | Exiba até três produtos por linha, até 12 produtos no total para blocos de produto estáticos e até 24 produtos no total para blocos de produto dinâmicos. |
| Espaçamento entre produtos | Defina o espaçamento entre os produtos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Layout options" }

![Opções de layout para orientação do produto, alinhamento, máximo de produtos por linha e espaçamento entre produtos.]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### Configurações globais de estilo de e-mail {#global-email-style-settings}

As [configurações globais de estilo de e-mail]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings/) permitem aplicar estilos consistentes aos seus e-mails na Braze. Isso significa que você pode definir estilos específicos — como fontes, cores e designs de botões — que serão aplicados automaticamente a todos os seus e-mails.

#### Como as configurações globais de estilo de e-mail funcionam com blocos de produto {#how-global-email-style-settings-work-with-product-blocks}

Os estilos existentes para parágrafos e botões são aplicados automaticamente aos elementos de texto e botão dentro do bloco de produto. Isso significa que o seu bloco de produto usa de forma consistente qualquer formatação que você tenha definido para parágrafos e botões, mantendo uma aparência coesa em todo o e-mail.

## Configurando blocos de produto {#setting-up-product-blocks}

### Configuração do catálogo {#catalog-setup}

{% alert important %}
Se você está usando a integração da Braze com a Shopify para [sincronização de produtos]({{site.baseurl}}/shopify_catalogs/), não é necessário realizar nenhuma etapa adicional para usar os blocos de produto de arrastar e soltar.<br><br> Se você não tem informações de variantes de produto, é necessário duplicar as informações do produto de nível superior tanto nos campos de produto quanto nos campos de variante de produto dentro das cargas úteis de eventos e catálogos. Isso significa que você precisa fornecer os mesmos detalhes do produto para ambos os identificadores para manter a consistência e garantir o funcionamento correto do bloco de produto.
{% endalert %}

Para usar blocos de produto de arrastar e soltar, você precisa configurar um catálogo da Braze que inclua valores de campos específicos. Esses campos são usados na configuração do seu bloco de produto. Certifique-se de que o seu catálogo inclua os seguintes campos:

| Campo | Descrição |
| --- | --- |
| `product_title` | O título do produto. |
| `product_url` | A URL onde os clientes podem visualizar ou comprar o produto. |
| `variant_image_url` | A URL da imagem da variante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Catalog setup" }

Comece rapidamente usando este [catálogo de produtos de exemplo]({{site.baseurl}}/assets/download_file/ecommerce_product_catalog_sample.csv), que inclui os campos obrigatórios.

![Um arquivo CSV de exemplo com os campos obrigatórios, além de outros.]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

#### Mapeamento para campos do catálogo {#mapping-to-catalog-fields}

Na guia **Settings** do seu catálogo, você pode selecionar o toggle **Product blocks** para mapear campos e informações específicas do seu catálogo. Isso permite selecionar quais campos usar como título do produto, URL do produto e URL da imagem. Os campos do catálogo da Shopify são mapeados por padrão e não podem ser alterados.

{% alert note %}
Se você não está usando a Shopify, pode entrar em contato com o gerente da sua conta para ativar o mapeamento de campos, que permite conectar qualquer catálogo aos blocos de produto e mapear seus campos para `product_title`, `product_url` e `variant_image_url`.
{% endalert %}

## Criando blocos de produto {#creating-product-blocks}

Este guia vai orientar você nas etapas para criar, testar e garantir o funcionamento de um bloco de produto dinâmico ou estático usando o editor de arrastar e soltar de e-mail.

### Etapa 1: Crie uma campanha de e-mail ou uma etapa de e-mail no Canvas {#step-1-create-an-email-campaign-or-email-canvas-step}

#### Bloco de produto dinâmico

{% alert note %}
Os blocos de produto dinâmicos exigem [eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_events/) e só podem ser usados dentro de [Canvas]({{site.baseurl}}/ecommerce_use_cases/). Para usuários da Braze com Shopify, esses eventos são incluídos automaticamente como parte da integração. Para usuários que não usam Shopify, é necessário trabalhar com seus desenvolvedores para enviar esses eventos para a Braze e garantir que o identificador principal do produto dentro dos eventos seja adicionado como ID do item do catálogo.
{% endalert %}

Crie um novo Canvas que use um dos modelos disponíveis da Braze para o seu caso de uso específico:
- Navegação abandonada
- Carrinho abandonado
- Checkout abandonado
- Confirmações de pedido

Para instruções detalhadas sobre como criar seus Canvas de eCommerce, consulte [Casos de uso de eCommerce]({{site.baseurl}}/ecommerce_use_cases/).

#### Bloco de produto estático

Crie uma campanha de e-mail de arrastar e soltar, um Canvas baseado em ação ou um modelo que tenha uma etapa de mensagem de e-mail de arrastar e soltar.

### Etapa 2: Adicione um bloco de produto {#step-2-add-a-product-block}

{% tabs %}
{% tab Bloco de produto dinâmico %}

Na etapa de mensagem, crie um e-mail ou modifique o modelo existente usando o criador de e-mail de arrastar e soltar.
Arraste um bloco de produto para a sua mensagem de e-mail.
Confirme que o tipo de bloco dinâmico está selecionado.
Selecione o catálogo de produtos que deseja usar para personalização. Certifique-se de que ele esteja alinhado com os produtos dos eventos de entrada que você está direcionando.

{% endtab %}
{% tab Bloco de produto estático %}

Arraste um bloco de produto para a sua mensagem de e-mail e selecione o tipo de bloco estático.
Selecione o catálogo que deseja usar para o seu bloco de produto. Você precisa selecionar uma seleção de catálogo para especificar quais produtos serão exibidos no seu bloco de produto.

{% endtab %}
{% endtabs %}

![A guia "Content" contendo blocos do editor, como blocos de produto.]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### Etapa 3: Configure os campos de produto {#step-3-configure-product-fields}

Selecione quais [campos de produto](#product-fields) devem ser exibidos no bloco de produto. Selecione **Apply Settings** após cada alteração para ver as atualizações no editor.

Você também pode personalizar o texto antes das suas Liquid tags. Por exemplo, você pode adicionar um cifrão (R$) antes do preço de um item ou alterar o termo de quantidade para "unidades" ou outro rótulo de sua preferência.

![Bloco de produto com um cifrão adicionado antes do preço do item.]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### Etapa 4: Configure as opções de layout {#step-4-configure-layout-settings}

Altere as [opções de layout](#layout-options) para atualizar como os produtos são exibidos dentro do seu bloco de produto, e certifique-se de selecionar **Apply settings** após cada alteração.

### Etapa 5: Pré-visualize e teste sua mensagem {#step-5-preview-and-test-your-message}

{% tabs %}
{% tab Bloco de produto dinâmico %}

1. Na seção **Preview & Test**, pré-visualize a mensagem como um usuário personalizado.
2. Especifique quantos itens deseja renderizar na pré-visualização.
3. Confirme que o número correto de itens aparece e que suas opções de layout estão aplicadas corretamente. Os itens que aparecem são selecionados aleatoriamente.

![Guia "Preview as a User" com uma seção dropdown "Dynamic product block" que especifica mostrar 4 itens.]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab Bloco de produto estático %}

Uma pré-visualização será gerada dentro do criador de arrastar e soltar quando você aplicar alterações ao seu bloco de produto.

![Criador de e-mail de arrastar e soltar mostrando um bloco de produto gerado com diferentes cards de itens.]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

Depois de terminar de criar sua mensagem e confirmar que ela está como esperado, você está pronto para enviar!