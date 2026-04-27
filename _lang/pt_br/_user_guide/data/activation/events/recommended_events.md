---
nav_title: Eventos recomendados
article_title: Eventos recomendados
alias: /recommended_events/
page_order: 2
page_type: reference
description: "Este artigo de referência descreve os eventos recomendados, que são recomendações fornecidas pela Braze para eventos de eCommerce."
---

# Eventos recomendados {#recommended-events}

> Os eventos recomendados mapeiam os casos de uso de eCommerce mais comuns. Ao usar eventos recomendados, você pode desbloquear modelos de Canvas pré-construídos, dashboards de relatórios que mapeiam o ciclo de vida do cliente e muito mais.

Por exemplo, você pode ter um evento personalizado chamado "cart_updated" ou "update_to_cart" para capturar quando um usuário adicionou, removeu ou atualizou os produtos no carrinho. Para eventos recomendados, a Braze fornecerá o modelo de evento, que inclui um nome definido e propriedades relevantes para esse evento.

{% alert important %}
Os eventos recomendados estão atualmente em acesso antecipado. Fale com seu gerente de sucesso do cliente da Braze se você tiver interesse em participar deste acesso antecipado. <br><br>Se você está usando o novo [conector Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), esses eventos recomendados estarão automaticamente disponíveis por meio da integração.
{% endalert %}

## Como funciona {#how-it-works}

A Braze aplica validação especial a todos os eventos recomendados, e alguns eventos recomendados possuem ações especiais de pós-processamento. Para determinados eventos recomendados do setor, a Braze pode oferecer tratamento especial, como novos gatilhos baseados em ação para campaigns e Canvas.

Os eventos recomendados funcionam de forma semelhante aos [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/). Você pode exportar eventos recomendados do Currents, bloqueá-los e usá-los em relatórios. Você também pode enviar dados para a Braze para rastreamento desses eventos usando o [SDK da Braze]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/) ou o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

### Eventos recomendados de eCommerce {#ecommerce-recommended-events}

Os [eventos recomendados de eCommerce]({{site.baseurl}}/ecommerce_events/) são baseados em eventos recomendados. Esses eventos recomendados de eCommerce rastreiam ações realizadas pelos seus clientes, como visualizar um produto, atualizar o carrinho ou iniciar o processo de checkout.

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### Modelos de Canvas para eCommerce {#ecommerce-canvas-templates}

Confira nossos [casos de uso de eCommerce]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases/) dedicados para mais ideias sobre como usar os modelos pré-construídos de Canvas da Braze para implementar estratégias essenciais.

## Perguntas frequentes {#frequently-asked-questions}

### Os eventos recomendados são iguais aos eventos personalizados? {#are-recommended-events-the-same-as-custom-events}

Não. A Braze definirá esquemas de dados padronizados para os eventos recomendados. Isso incluirá propriedades de evento obrigatórias e opcionais que passarão por um processo de validação na Braze. Os [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) são ações específicas realizadas pelos seus usuários, ou atualizações sobre eles, no seu app ou site que você deseja rastrear. Você pode personalizar o nome do evento e o que ele rastreia.

### Posso personalizar o nome dos eventos recomendados? {#can-i-customize-the-name-of-the-recommended-events}

Não. Os eventos recomendados possuem nomes e propriedades de evento padronizados. Essas padronizações ajudam a criar consistência nos seus dados.

### Ainda posso usar eventos de compra para registrar compras? {#can-i-still-use-purchase-events-to-log-purchases}

Com o lançamento dos eventos recomendados de eCommerce, a Braze descontinuará o evento de compra legado no futuro. Se você está usando o evento de compra atualmente, receberá um aviso prévio sobre os planos de descontinuação. Enquanto isso, você pode continuar usando os eventos de compra até a data oficial de descontinuação.