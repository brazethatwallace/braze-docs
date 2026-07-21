---
nav_title: Mensagens de produto
article_title: Mensagens de produto
page_order: 4
description: "Esta página aborda como usar mensagens de produto do WhatsApp para enviar mensagens interativas do WhatsApp que exibem produtos do seu catálogo Meta."
page_type: reference
alias: "/whatsapp_product_messages/"
tool:
 - Campaigns
channel:
 - WhatsApp
---

# Mensagens de produto {#product-messages}

> As mensagens de produto permitem que você envie mensagens interativas do WhatsApp que exibem produtos diretamente do seu catálogo Meta.

Quando você envia uma mensagem de produto do WhatsApp para um usuário, ele segue a seguinte jornada do cliente:

1. O usuário recebe sua mensagem de produto ou catálogo no WhatsApp.
2. O usuário adiciona produtos ao carrinho diretamente pelo WhatsApp.
3. O usuário toca em **Place order** no WhatsApp.
4. Seu site ou app recebe os dados do carrinho da Braze e gera um link de checkout.
5. O usuário é direcionado ao seu site ou app para concluir a compra.

Quando os usuários adicionam itens ao carrinho por meio de mensagens de catálogo, a Braze recebe dados de webhook para ações de acompanhamento.

## Requisitos {#requirements}

| Requisito | Descrição |
| --- | --- |
| Conta WhatsApp Business | Para usar mensagens de produto do WhatsApp, você precisa ter uma conta WhatsApp Business conectada à Braze. |
| Catálogo Meta | Você precisa configurar um catálogo Meta no seu Commerce Manager. |
| Conformidade com os termos | Cumpra os [Termos e Políticas de Comércio da Meta](https://www.facebook.com/policies_center/commerce). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos" }

## Tipos de mensagens de produto {#product-message-types}

{% alert note %}
Aprimore sua experiência com mensagens de produto usando o seletor de produtos integrado, que é acessado durante a etapa 4 de [Configurando mensagens de produto](#setting-up-product-messages).
{% endalert %}

{% tabs local %}
{% tab Mensagens de catálogo %}

As mensagens de catálogo exibem todo o seu catálogo de produtos em um formato interativo. Elas estão disponíveis como [mensagens de modelo e de resposta](#building-a-product-message).

Se você habilitou as permissões de catálogo para a Braze durante a [configuração](#setting-up-product-messages), pode selecionar qual miniatura ficará visível para os usuários.

{% alert note %}
Você não precisa fazer seleções adicionais de produtos na Braze, pois a conexão do catálogo é gerenciada pela Meta e, portanto, é herdada no seu catálogo de produtos.
{% endalert %}


{% endtab %}
{% tab Mensagens multiproduto %}

As mensagens multiproduto destacam produtos específicos do seu catálogo, com até 30 itens destacados por mensagem. Elas estão disponíveis como [mensagens de modelo e de resposta](#building-a-product-message).

Você pode selecionar os produtos manualmente com IDs ou, se habilitou as permissões de catálogo durante a [configuração](#setting-up-product-messages), usar o seletor de produtos no menu suspenso.

{% alert important %}
Há um problema conhecido de exibição de cabeçalho com modelos de mensagens multiproduto na Meta. A Meta está ciente do problema e trabalhando em uma correção.
{% endalert %}

{% endtab %}
{% tab Produto individual %}

As mensagens de produto individual destacam um produto específico do seu catálogo de produtos. Elas estão disponíveis como [mensagens de resposta](#building-a-product-message).

Você pode selecionar os produtos manualmente com IDs ou, se habilitou as permissões de catálogo durante a [configuração](#setting-up-product-messages), usar o seletor de produtos no menu suspenso.

{% endtab %}
{% endtabs %}

## Configurando mensagens de produto {#setting-up-product-messages}

1. No [Meta Commerce Manager](https://business.facebook.com/business/loginpage/?next=https%3A%2F%2Fbusiness.facebook.com%2Fcommerce_manager%2F#), siga as [instruções da Meta](https://www.facebook.com/business/help/1275400645914358?id=725943027795860&ref=search_new_1) para criar seu catálogo Meta. Certifique-se de estar no mesmo Meta Business Portfolio onde sua conta WhatsApp Business conectada à Braze está localizada.
2. Siga as instruções da Meta para [conectar seu catálogo Meta](https://www.facebook.com/business/help/1953352334878186?id=2042840805783715) à sua conta WhatsApp Business conectada à Braze, atribuindo a permissão "Manage Catalog" no Meta Business Manager.

![Página "Catalogs" da Meta com uma seta apontando para o botão "Assign partner" do catálogo chamado "sweeney_catalog".]({% image_buster /assets/img/whatsapp/meta_catalog.png %}){: style="max-width:90%;"}

Certifique-se de usar o ID do Braze Business Manager, `332231937299182`, como o ID do parceiro comercial.

![Janela para compartilhar um catálogo com um parceiro contendo campos para inserir o ID do parceiro comercial e atribuir a permissão "Manage catalog".]({% image_buster /assets/img/whatsapp/share_meta_catalog.png %}){: style="max-width:70%;"}

{: start="3"}
3. Selecione as configurações do seu catálogo Meta. Você deve selecionar **Show catalog icon in chat header** para enviar mensagens de catálogo.

![Página de configurações do WhatsApp Manager para o catálogo "Catalog_products".]({% image_buster /assets/img/whatsapp/meta_catalog_settings.png %}){: style="max-width:90%;"}

{: start="4"}
4. Na Braze, passe pelo processo de [cadastro integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) para fornecer permissões. Certifique-se de selecionar **todos** os catálogos para os quais deseja fornecer permissões. Isso desbloqueará o seletor de produtos integrado da Braze.

![Janela com cinco catálogos selecionados para fornecer permissões.]({% image_buster /assets/img/whatsapp/select_catalogs.png %}){: style="max-width:50%;"}

{% alert tip %}
Para conhecer as práticas recomendadas ao criar catálogos Meta, consulte [Dicas para criar um catálogo de alta qualidade no Commerce Manager](https://www.facebook.com/business/help/2086567618225367?id=725943027795860).
{% endalert %}

## Criando uma mensagem de produto {#building-a-product-message}

Você pode criar uma mensagem de produto usando um modelo de mensagem do WhatsApp ou uma mensagem de resposta.

{% tabs local %}
{% tab Modelo de mensagem do WhatsApp %}

1. No seu Meta Business Manager, acesse **Message Templates**.
2. Selecione **Catalog** como formato e escolha entre **Catalog message** (exibe o catálogo completo) e **Multi-product catalog message** (destaca itens específicos).
3. Na Braze, crie uma Campaign do WhatsApp ou uma etapa de mensagem do Canvas.
4. Selecione o grupo de inscrições correspondente ao local onde você enviou o modelo.
5. Selecione **WhatsApp Template Message**.
6. Selecione o modelo que deseja usar.
    - Se você selecionar um modelo multiproduto, forneça o título da seção e os IDs de conteúdo dos produtos a serem destacados. Você pode copiar o Content ID diretamente do seu Meta Commerce Manager ou, se habilitou as permissões para o seletor de produtos integrado, selecionar os itens.

![Lista de itens com campos para inserir títulos de seção e ID de conteúdo.]({% image_buster /assets/img/whatsapp/multi_product_template.png %}){: style="max-width:60%;"}

![Lista de itens com menu suspenso de itens para selecionar.]({% image_buster /assets/img/whatsapp/content_id_items.png %}){: style="max-width:60%;"}

{: start="7"}
7. Continue criando sua mensagem.

{% endtab %}
{% tab Mensagem de resposta %}

1. Na Braze, crie uma Campaign do WhatsApp ou uma etapa de mensagem do Canvas.
2. Selecione um grupo de inscrições.
3. Selecione **Response Message**.
4. Selecione **Meta Product Messages**.

![Opções para selecionar um tipo de mensagem e layout de mensagem de resposta, com "Response Message" e "Meta Product Messages" destacados.]({% image_buster /assets/img/whatsapp/response_message_layouts.png %}){: style="max-width:90%;"}

{: start="5"}
5. Selecione o [tipo de mensagem](#product-message-types) que deseja usar.

![Seleção de layout de mensagem "Multi-product".]({% image_buster /assets/img/whatsapp/multi-product_message_layout.png %}){: style="max-width:90%;"}

{: start="6"}
6. Continue criando sua mensagem.

![Exemplo de mensagem de produto Meta com informações preenchidas para os produtos.]({% image_buster /assets/img/whatsapp/example_response_message.png %}){: style="max-width:90%;"}

{% endtab %}
{% endtabs %}

## Gerenciando produtos {#managing-products}

### Acessando o Commerce Manager {#accessing-commerce-manager}

No seu Meta Business Manager, acesse **Commerce Manager** e selecione sua organização. Aqui, você pode gerenciar os ativos do seu catálogo, como:
- Criar novos catálogos
- Adicionar produtos a catálogos existentes
- Atualizar informações de produtos
- Remover itens descontinuados

{% alert important %}
Se você remover produtos referenciados do seu catálogo, as mensagens associadas não serão enviadas.
{% endalert %}

## Recebendo perguntas sobre produtos {#receiving-inbound-product-questions}

Os usuários podem responder à sua mensagem de produto ou catálogo com perguntas sobre produtos. Essas perguntas chegam como mensagens de entrada, que podem ser classificadas com uma [Jornada de ação]({{site.baseurl}}/action_paths).

Além disso, a Braze extrai o ID do produto e o ID do catálogo dessas perguntas. Então, se você deseja automatizar respostas ou encaminhar perguntas para outra equipe (como suporte ao cliente), pode incluir esses detalhes. Por exemplo, você pode personalizar respostas com as propriedades do WhatsApp `inbound_product_id` ou `inbound_catalog_id`.

![Janela "Add Personalization" com tipo de personalização "WhatsApp Properties" e atributo "inbound_product_id" destacado.]({% image_buster /assets/img/whatsapp/inbound_product_questions.png %}){: style="max-width:60%;"}

## Checkout: processamento de carrinho e webhooks {#checkout-cart-processing-and-webhooks}

Quando os usuários interagem com suas mensagens de produto do WhatsApp, eles podem navegar pelos produtos e adicionar itens ao carrinho. No entanto, atualmente não há funcionalidade de checkout integrada para informações de envio ou processamento de pagamento. Em vez disso, recomendamos que você crie um carrinho no seu próprio app ou site e direcione os usuários para esse carrinho usando um link personalizado.

### Considerações {#considerations}

- **Sem checkout no app:** os usuários não podem concluir compras diretamente no WhatsApp. Todas as transações devem ser redirecionadas para seu site ou app.
- **Link personalizado necessário:** você precisa criar um link personalizado que direcione os usuários ao carrinho na sua plataforma.
- **Configuração manual:** o processo de configuração requer configuração manual do seu carrinho e fluxos de envio de mensagens.

{% alert note %}
Atualmente, não oferecemos suporte a pagamentos diretamente no WhatsApp, e o suporte futuro será específico por país (atualmente, a Meta oferece isso apenas para empresas sediadas e que trabalham diretamente com usuários na Índia, Brasil e Singapura).
{% endalert %}

### Configurando gatilhos de eventos de carrinho {#setting-up-cart-event-triggers}

Quando um cliente faz um pedido no WhatsApp, a Braze automaticamente:
1. Recebe o conteúdo do carrinho do WhatsApp (IDs de produtos, quantidades e outros dados do pedido).
2. Cria um evento de eCommerce `ecommerce.cart_update` com todos os dados relevantes, incluindo `source = whats_app`.
3. Dispara uma resposta, permitindo que você configure Campaigns automatizadas para responder ao pedido.

O evento de eCommerce `ecommerce.cart_update` só aparece listado na Braze após um evento ter sido enviado, o que pode ser feito gerando uma mensagem de produto de teste na Braze e enviando um evento de carrinho.
O evento de carrinho inclui:

- **ID do carrinho:** identificador único do carrinho
- **Produtos:** lista de itens com IDs de produtos, quantidades e preços
- **Valor total:** soma de todos os itens
- **Moeda:** moeda do carrinho
- **Origem:** marcado como "whats_app"
- **Metadados:** dados adicionais como ID do catálogo e texto da mensagem

Você pode encontrar informações adicionais sobre eventos de carrinho da Braze em [Tipos de eventos de eCommerce recomendados]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).

### Configurando uma resposta disparada {#setting-up-a-triggered-response}

1. Crie um gatilho de evento personalizado para `ecommerce.cart_updated`.
2. Adicione um filtro de propriedade para `source = "whats_app"`.

![Etapa do Canvas para um gatilho de evento personalizado `ecommerce.cart_updated` com a propriedade básica "source" igual a `whats_app`.]({% image_buster /assets/img/whatsapp/product_message_canvas_step.png %})

{: start="3"}
3. Configure ações de acompanhamento com base nos dados do carrinho.

### Implementações de checkout recomendadas {#recommended-checkout-implementations}

{% tabs local %}
{% tab Links de carrinho baseados em Liquid %}

Use Liquid para criar URLs de carrinho diretamente na sua mensagem de resposta. Essa é a melhor opção se você tem IDs de produtos consistentes entre o WhatsApp e sua plataforma de eCommerce.

#### Exemplo de Liquid {#example-liquid}

{% raw %}
```liquid
{% assign cart_link = "http://alejandro-test-new.myshopify.com/cart/" %}
{% for product in event_properties.products %}
 {% assign variant_id = product.product_id %}
 {% assign quantity = product.quantity %}
 {% if forloop.first %}
   {% assign cart_link = cart_link | append: variant_id | append: ":" | append: quantity %}
 {% else %}
   {% assign cart_link = cart_link | append: "," | append: variant_id | append: ":" | append: quantity %}
 {% endif %}
{% endfor %}
{{ cart_link }}
```
{% endraw %}

#### Configuração {#setup}

1. Crie uma Campaign de mensagem de resposta do WhatsApp com o gatilho de um evento de eCommerce `ecommerce.cart_update`.
2. Crie uma mensagem subsequente com a URL do carrinho.
3. Construa sua URL de carrinho com Liquid. Se você usa Shopify, pode [criar um permalink de carrinho](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks) com o exemplo de Liquid anterior.

![Diagrama mostrando o fluxo de experiência de checkout para um carrinho gerado por Liquid: a Meta envia uma mensagem de pedido recebido para a Braze, que dispara um gatilho baseado em ação e cria uma mensagem com link do carrinho, que então envia uma mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/liquid_generated_cart_link_checkout.png %})

{% endtab %}
{% tab Conteúdo conectado %}

Faça uma chamada de API para seu sistema de eCommerce para gerar uma URL de checkout personalizada. Essa é a melhor opção se você precisa de geração dinâmica de URL de carrinho ou mapeamento complexo de produtos.

#### Configuração

1. Crie uma Campaign de webhook ou etapa do Canvas disparada pelo evento de eCommerce [`ecommerce.cart_update`]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events?tab=ecommerce.cart_updated), que enviará os dados do carrinho para seu sistema de eCommerce.
2. Crie uma Campaign do WhatsApp ou etapa de mensagem do Canvas disparada pelo mesmo evento de eCommerce para enviar uma mensagem de resposta do WhatsApp com a URL do carrinho para o usuário. Siga as instruções na mensagem de resposta subsequente para usar [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).

![Diagrama mostrando o fluxo de experiência de checkout para uma chamada de Conteúdo conectado: a Meta envia uma mensagem de pedido recebido para a Braze, que faz chamadas de ida e volta com uma plataforma de eCommerce, e então envia uma mensagem do WhatsApp.]({% image_buster /assets/img/whatsapp/connected_content_checkout.png %})

{% endtab %}
{% tab Webhooks e eventos personalizados %}

Use webhooks para enviar dados do carrinho para seu sistema e, em seguida, dispare mensagens de acompanhamento por meio de eventos personalizados. Essa é a melhor opção para integrações complexas que exigem processamento extenso de carrinho ou fluxos de trabalho com várias etapas.

#### Configuração

Crie uma Campaign de webhook ou etapa do Canvas disparada pelo evento de eCommerce `ecommerce.cart_update`, que enviará os dados do carrinho para seu sistema de eCommerce. Sua API então irá:
1. Receber os dados do carrinho
2. Criar um carrinho no seu sistema
3. Gerar a URL de checkout
4. Enviar um evento `checkout_started` para a Braze, disparando o envio da sua mensagem do WhatsApp com o link de checkout

![Diagrama mostrando o fluxo de experiência de checkout para webhooks e eventos personalizados: a Meta envia uma mensagem de pedido recebido para a Braze, que faz chamadas de ida e volta com uma plataforma de eCommerce, e então envia uma mensagem do WhatsApp com a URL do carrinho.]({% image_buster /assets/img/whatsapp/webhooks_custom_events_checkout.png %})

{% endtab %}
{% endtabs %}

## Testes e validação {#testing-and-validation}

### Requisitos para mensagens de teste {#test-message-requirements}

A funcionalidade do carrinho é mantida entre mensagens de teste, mas o processamento do resultado de entrada não é mantido.

### Prévia da mensagem {#message-preview}

- As imagens e detalhes dos produtos são obtidos do seu catálogo Meta.
- A prévia interativa mostra espaços reservados até que a integração seja concluída.

### Códigos de erro {#error-codes}

- Se um ID de produto não existir no catálogo, você receberá o erro `product not found for product_retailer_id, fake-product-id, in catalog_id, 1903196950214359`.
- Se um catálogo estiver desconectado da WABA, você receberá o erro `Check if catalog is linked to the WhatsApp Business Account and the catalog is enabled in the WhatsApp Commerce Settings`.