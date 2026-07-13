---
nav_title: Sincronização de coleções do Shopify
article_title: Sincronização de coleções do Shopify
permalink: "/shopify_collections_sync/"
description: "Este artigo de referência aborda como configurar a sincronização de coleções do Shopify, que permite agrupar seus produtos em coleções para que os clientes possam encontrá-los por categoria."
hidden: true
---

# Beta da sincronização de coleções do Shopify {#shopify-collections-sync-beta}

> A sincronização de coleções do Shopify permite agrupar seus produtos em coleções para que os clientes possam encontrá-los por categoria. Para uma experiência de compra mais fluida, você pode incorporar itens das coleções da sua loja nas suas mensagens da Braze.

{% alert important %}
A sincronização de coleções do Shopify está atualmente em beta. Entre em contato com o gerente da sua conta Braze se quiser participar do beta.
{% endalert %}

## Configurando a sincronização de coleções do Shopify {#setting-up-shopify-collections-sync}

Para sincronizar seus produtos da sua loja Shopify com a Braze, marque a caixa de seleção **Sync Shopify collections** na etapa **Sync products** da [integração com o Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#setting-up-shopify-in-braze).<br><br>![Etapa 4 da sincronização de produtos do Shopify com a caixa de seleção "Sync Shopify collections" marcada.][1]

Depois que seus produtos forem sincronizados, você pode visualizar quais produtos estão associados às suas coleções acessando o catálogo do Shopify. <br><br>![Linha da tabela do catálogo mostrando um produto nas coleções "best-sellers" e "front page".][2]

No catálogo do Shopify, você pode visualizar sua coleção do Shopify na guia **Selections**. <br><br>![A guia Selections mostrando uma lista de duas coleções: "best-sellers" e "front page".][3]

### Funcionalidade do beta {#beta-functionality}

- A Braze suportará até 30 coleções.
- A ordem de classificação da sua coleção não é mantida nem suportada no momento. Por enquanto, a ordem de classificação é baseada no seguinte:
    - Os itens mais recentes adicionados à sua coleção.
    - A ordem em que os itens são atualizados durante sincronizações contínuas.
    - A ordem que você seleciona na guia de seleção da sua coleção do Shopify.

## Usando coleções do Shopify {#using-shopify-collections}

Use suas coleções do Shopify para personalizar uma mensagem para cada usuário na sua Campaign, de forma semelhante a como você usaria uma [seleção da Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/).

{% alert warning %}
Esteja ciente do seguinte comportamento no beta: <br><br>Se você atualizar a descrição da coleção do Shopify ou as configurações de filtro, a sincronização da coleção do Shopify será interrompida. Como resultado, sua coleção do Shopify não funcionará como esperado.
{% endalert %}

### Etapa 1: Configure a ordem de classificação da sua coleção do Shopify {#step-1-configure-the-sort-order-of-your-shopify-collection}

1. Especifique a ordem em que os resultados da sua coleção do Shopify são retornados selecionando **Sort Order** na guia de seleção da sua coleção do Shopify. Isso inclui uma opção para randomizar a ordem de classificação.
2. Insira o número máximo de resultados (até 50) em **Limit number**.
3. Selecione **Update Selection**.

![A página Edit Selection onde você pode selecionar as configurações de filtro, tipo de classificação e limite de resultados.][4]

### Etapa 2: Use a coleção em uma Campaign {#step-2-use-the-collection-in-a-campaign}

1. Crie uma Campaign e selecione **+ Personalization** no Criador de mensagens.
2. Selecione o seguinte:<br>- **Catalog Items** como o **Personalization type**<br>- O nome do catálogo<br>- O método de seleção de itens<br>- O nome da seleção (o nome da sua coleção do Shopify) <br>- As informações a serem exibidas na sua mensagem

{: start="3"}
3. Copie e cole o snippet Liquid onde você deseja que as informações apareçam na sua mensagem.

![A seção "Add Personalization" com campos para selecionar seu catálogo, método de seleção de itens e as informações a serem exibidas.][5]{: style="max-width:30%;"}

#### Liquid nos resultados de seleção {#liquid-in-selection-results}

O uso de quaisquer resultados em catálogos, como atributos personalizados e eventos personalizados, pode fazer com que resultados diferentes sejam retornados para cada usuário na sua seleção.

[1]: {% image_buster /assets/unlisted_docs/img/shopify/sync_products.png %}
[2]: {% image_buster /assets/unlisted_docs/img/shopify/view_catalog.png %}
[3]: {% image_buster /assets/unlisted_docs/img/shopify/selections_tab.png %}
[4]: {% image_buster /assets/unlisted_docs/img/shopify/edit_selection.png %}
[5]: {% image_buster /assets/unlisted_docs/img/shopify/add_personalization.png %}