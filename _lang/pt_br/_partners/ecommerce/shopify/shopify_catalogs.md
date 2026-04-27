---
nav_title: Sincronização de produtos da Shopify
article_title: Sincronização de produtos da Shopify
alias: /shopify_catalogs/
page_order: 5
description: "Este artigo de referência aborda como importar seus produtos da Shopify para os catálogos da Braze."
---

# Sincronização de produtos da Shopify {#shopify-product-sync}

> Você pode sincronizar todos os produtos da sua loja Shopify com um [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/) da Braze para uma personalização mais profunda do envio de mensagens.

Os catálogos da Shopify serão atualizados quase em tempo real à medida que você fizer edições e alterações nos produtos da sua loja Shopify. É possível enriquecer seu carrinho abandonado, a confirmação do pedido e muito mais com os detalhes e as informações mais atualizadas do produto.

{% alert warning %}
A Braze sincroniza até 250 variantes de cada produto da Shopify no seu catálogo. Variantes além desse limite não são sincronizadas. Se você precisar de mais de 250 variantes por produto, entre em contato com seu gerente de sucesso do cliente da Braze.
{% endalert %}

## Configurando sua sincronização de produtos da Shopify {#setting-up}

Se você já instalou sua loja Shopify, ainda poderá sincronizar seus produtos seguindo as instruções abaixo.

### Etapa 1: Ativar a sincronização {#step-1-turn-on-the-sync}

Você pode sincronizar seus produtos com um catálogo da Braze por meio do fluxo de instalação da Shopify ou na página de parceiros da Shopify.

![Etapa 3 do processo de configuração com "Shopify Variant ID" como o "Catalog product identifier".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:70%;"}

Os produtos sincronizados com um catálogo da Braze contribuirão para o seu [limite de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers).

### Etapa 2: Selecione o identificador do seu produto {#step-2-select-your-product-identifier}

Selecione o identificador de produto a ser usado como ID do catálogo:
- Shopify Variant ID
- SKU

Os valores de ID e de cabeçalho para o identificador de produto que você escolher só podem incluir letras, números, hífens e sublinhados. Se o identificador do produto não seguir esse formato, a Braze o removerá da sincronização do catálogo.

Esse será o identificador principal que você usará para fazer referência às informações do catálogo da Braze.

{% alert note %}
Se estiver selecionando SKU como ID do catálogo, certifique-se de que todos os seus produtos e variantes na sua loja tenham um SKU definido e que sejam exclusivos.
- Se um item não tiver um SKU, a Braze não poderá sincronizar esse produto no catálogo.
- Se você tiver mais de um produto com o mesmo SKU, isso pode causar um comportamento inesperado ou fazer com que as informações do produto sejam substituídas involuntariamente pelo SKU duplicado.
{% endalert %}

### Etapa 3: Sincronização em andamento {#step-3-sync-in-progress}

Você receberá uma notificação no dashboard e seu status será exibido como "In Progress" para indicar que a sincronização inicial está começando. Note que o tempo necessário para a conclusão da sincronização depende do número de produtos e variantes que a Braze precisa sincronizar da Shopify. Durante esse período, você pode sair desta página e aguardar uma notificação do dashboard ou um e-mail para avisá-lo quando a sincronização for concluída.

Note que, se a sincronização inicial exceder o [limite do seu catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create/#tiers), a Braze interromperá a sincronização de mais produtos. Se você exceder o limite depois que a sincronização for bem-sucedida devido à adição de novos produtos ao longo do tempo, a sincronização não estará mais ativa. Em ambos os casos, as atualizações de produtos da Shopify não serão mais refletidas na Braze. Entre em contato com o gerente da sua conta para considerar a possibilidade de fazer upgrade do seu nível.

### Etapa 4: Sincronização concluída {#step-4-sync-completed}

Você receberá uma notificação no dashboard e um e-mail depois que a sincronização for bem-sucedida. A página de parceiros da Shopify também atualizará o status em catálogos da Shopify para "Syncing". Para visualizar seus produtos, clique no nome do catálogo na página de parceiros da Shopify.

Consulte [Casos de uso adicionais de catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/use/) para saber mais sobre como aproveitar os dados do catálogo para personalizar suas mensagens.

#### Dados de catálogo compatíveis com a Shopify {#supported-shopify-catalog-data}

- `id`
- `store_name`
- `shopify_product_id`
- `shopify_variant_id`
- `product_title`
- `variant_title`
- `status`
- `product_image_url`
- `variant_image_url`
- `vendor`
- `product_type`
- `product_url`
- `product_handle`
- `published_scope`
- `price`
- `compare_at_price`
- `inventory_quantity`
- `options`
- `option_values`
- `sku`

{% alert warning %}
Modificar o catálogo da Shopify de qualquer forma pode interferir involuntariamente nas sincronizações de produtos em tempo real. Não faça edições no catálogo da Shopify, pois elas poderão ser substituídas pela Shopify. Em vez disso, faça as atualizações necessárias do produto na sua instância da Shopify.<br><br>Para excluir seu catálogo da Shopify, acesse a página da Shopify e desative a sincronização. Não exclua o catálogo da Shopify diretamente na página de catálogos.
{% endalert %}

## Casos de uso de reposição de estoque e queda de preço {#back-in-stock-and-price-drop-use-cases}

Para configurar notificações de reposição de estoque, siga as etapas [aqui]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/).

Para configurar notificações de queda de preço, siga as etapas [aqui]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/).

Note que, com a integração da Shopify, será necessário criar um evento personalizado que capture o status da inscrição de um usuário no seu catálogo para cada caso de uso. O evento personalizado exigirá uma propriedade de evento que mapeie o [SKU ou o Shopify Variant ID]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/#step-2-select-your-product-identifier) que você selecionou como parte da sincronização de produtos da Shopify.

## Alteração do ID do catálogo {#changing-catalog-id}

Para alterar o identificador de produto do seu catálogo da Shopify, você precisará desativar a sincronização. Confirme que você parou de enviar mensagens usando esses dados do catálogo da Shopify primeiro. Execute novamente a sincronização inicial do catálogo da Shopify e selecione o identificador de produto desejado seguindo as etapas de [sincronização de produtos](#setting-up).

## Desativar a sincronização de produtos {#deactivate}

A desativação do recurso de sincronização de produtos da Shopify excluirá o catálogo completo e os produtos. Isso também pode afetar quaisquer mensagens que possam estar usando ativamente os dados do produto desse catálogo. Confirme se você atualizou ou pausou essas Campaigns ou Canvas antes da desativação, pois isso pode resultar no envio de mensagens sem detalhes do produto. Não exclua o catálogo da Shopify diretamente na página de catálogos.

## Solução de problemas {#troubleshooting}
Se a sincronização de produtos da Shopify apresentar um erro, ele pode ser resultado dos seguintes problemas. Siga as instruções sobre como corrigir o problema e resolver a sincronização:

| Erro | Motivo | Solução |
| --- | --- | --- |
| Erro do servidor | Isso ocorre se houver um erro de servidor no lado da Shopify quando tentamos sincronizar seus produtos. | [Desative a sincronização](#deactivate) e sincronize novamente todo o seu inventário de produtos. |
| SKU duplicado | Isso ocorre se você usar um SKU como ID do item do catálogo e tiver produtos com o mesmo SKU. Como o ID do item do catálogo deve ser exclusivo, todos os seus produtos devem ter SKUs exclusivos. | Faça uma auditoria na sua lista completa de produtos e variantes na Shopify para garantir que não haja SKUs duplicados. Se houver SKUs duplicados, atualize-os para que sejam SKUs exclusivos somente na sua conta da loja Shopify. Depois que isso for corrigido, [desative a sincronização](#deactivate) e sincronize novamente todo o seu inventário de produtos. |
| Limite de catálogo excedido | Isso ocorre se você exceder o limite do catálogo. A Braze não poderá concluir a sincronização ou manter a sincronização ativa devido à falta de espaço de armazenamento disponível. | Há duas soluções para esse problema:<br><br>1. Entre em contato com o gerente da sua conta para fazer upgrade do seu nível e aumentar o limite do seu catálogo. <br><br>2. Libere espaço de armazenamento excluindo qualquer um dos seguintes itens:<br>- Itens de catálogo de outros catálogos<br>- Outros catálogos<br>- Seleções criadas<br><br> Depois de usar qualquer uma das soluções, a sincronização deve ser desativada e reativada em seguida. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }