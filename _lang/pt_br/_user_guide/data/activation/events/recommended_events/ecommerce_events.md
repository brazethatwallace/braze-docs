---
nav_title: Usar eventos recomendados de eCommerce
article_title: Como usar eventos de eCommerce
page_type: reference
alias: /ecommerce_events/
description: "Saiba como usar eventos recomendados de eCommerce na Braze, incluindo recursos suportados, métricas principais e práticas recomendadas para segmentação e envio de mensagens."
---

# Como usar eventos de eCommerce {#how-to-use-ecommerce-events}

> Os [eventos recomendados]({{site.baseurl}}/recommended_events) de eCommerce usam um esquema compartilhado no nível do pedido, o que permite à Braze criar recursos confiáveis com base nos seus dados de eCommerce — incluindo perfis de usuário, segmentação, envio de mensagens, relatórios e recomendações com IA. As seções deste artigo abordam como usar cada recurso na Braze.<br><br> Consulte [Esquemas de eventos]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas) para requisitos de propriedades e tipos de dados, e [Validação de eventos e solução de problemas]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-validation-and-troubleshooting) para saber o que acontece quando um evento falha na validação.

Como os eventos de eCommerce seguem um esquema previsível, a Braze pode criar recursos confiáveis com base neles, desde rastreamento de receita e modelos de Canvas pré-construídos até recomendações com IA. As seções a seguir oferecem uma visão geral rápida de cada recurso com links para a documentação completa.

{% alert note %}
Os eventos de eCommerce da Braze e suas propriedades de evento segmentáveis não contam como [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points).
{% endalert %}

<a id="transactions-tab" aria-hidden="true"></a>

## Guia Comércio {#commerce-tab}

A guia **Comércio** em cada perfil de usuário combina dois módulos: **Atividade de pedidos** (métricas calculadas de receita e pedidos) e **Carrinho ativo** (o carrinho mais recente dos eventos `ecommerce.cart_updated`).

### Atividade de pedidos {#order-activity}

O módulo **Atividade de pedidos** exibe três métricas calculadas que são atualizadas em tempo real conforme os eventos são processados. O modelo no nível do pedido desses cálculos separa claramente os preços dos produtos do valor total do pedido.

{% alert note %}
Os eventos recomendados de eCommerce não preenchem a seção **Histórico de compras** da guia **Comércio**. O histórico de compras é preenchido por eventos de compra legados. Use as métricas da tabela a seguir para receita e atividade de pedidos a partir de eventos recomendados.
{% endalert %}

| Métrica | Fórmula |
| ----- | ----- |
| Receita total | soma (`order_placed.total_value`) − soma (`order_refunded.total_value`) |
| Total de pedidos | contagem (distintos `order_placed`) − contagem (distintos `order_cancelled`) |
| Valor total de reembolsos | soma (`order_refunded.total_value`) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de atividade de pedidos" }

### Carrinho ativo {#active-cart}

O módulo **Carrinho ativo** mostra o carrinho mais recente no perfil do usuário. Essa visualização é especialmente útil durante os testes. Você pode usá-la para confirmar o conteúdo do carrinho, validar jornadas baseadas em carrinho ou verificar se os eventos `ecommerce.cart_updated` estão atualizando o perfil conforme esperado.

O **Carrinho ativo** inclui o seguinte:

- **ID do carrinho** — Identificador do carrinho que recebeu o último evento `ecommerce.cart_updated`.
- **Última atualização** — Timestamp da atualização mais recente do carrinho.
- **Valor total do carrinho** — Valor total dos itens de linha no carrinho atual.
- **Ver produtos** — Um link para abrir a lista de produtos no carrinho (até 50 produtos).

## Orquestração de eCommerce {#ecommerce-orchestration}

### Segmentação {#segmentation}

A Braze oferece três maneiras de segmentar usuários com base em dados de eCommerce:

- **Filtros de eCommerce:** Use a categoria **eCommerce** no segmentador, que contém filtros alimentados por eventos recomendados de eCommerce (como **Last Order Placed**, **Total Revenue** e **Average Order Value**). Para ver a lista completa de filtros disponíveis, consulte [Filtros de segmento]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
- **Filtros de eventos personalizados:** Como os eventos de eCommerce se comportam como eventos personalizados, todos os filtros de eventos personalizados existentes funcionam imediatamente. Por exemplo, você pode filtrar por "Realizou evento personalizado `ecommerce.order_placed` mais de X vezes" ou "Realizou evento personalizado `ecommerce.order_placed` pela primeira vez".
- **Extensões de segmento:** Para segmentar com base em propriedades de evento aninhadas, incluindo o array de produtos aninhados ou as propriedades de objetos de metadados, use [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) com filtragem de propriedades de evento aninhadas. Isso permite criar públicos como "usuários que compraram o produto SKU-123 nos últimos 90 dias" ou combinar critérios em diferentes propriedades do mesmo pedido.

{% alert important %}
As extensões de segmento para eventos recomendados de eCommerce são um recurso pago e estão em acesso antecipado. Se você tiver interesse em participar do acesso antecipado, entre em contato com seu gerente de sucesso do cliente. Confirme se seu plano inclui acesso antes de recomendar a segmentação por propriedades aninhadas à sua equipe.
{% endalert %}

### Disparo {#triggering}

Você pode usar disparos de eventos personalizados realizados com eventos de eCommerce em toda a Braze, da mesma forma que com outros eventos personalizados. Para fluxos de carrinho abandonado, use o disparo **Perform Cart Updated Event** para capturar corretamente as atualizações do carrinho.

Além disso, a Braze oferece um disparo dedicado **Places Order**, que permite iniciar jornadas ou realizar ações com base em qualquer pedido realizado, ou em pedidos que incluam um produto específico. Você pode filtrar esse disparo por nome do produto, `product_id` ou `variant_id` para segmentar cenários de compra específicos. Para saber mais, consulte [Entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Disparo Places Order com a opção selecionada de realizar qualquer pedido.]({% image_buster /assets/img/recommended_events/places_order_trigger.png %})

### Personalização com Liquid {#liquid-personalization}

Os eventos de eCommerce suportam [personalização com Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) da mesma forma que os eventos personalizados; você pode referenciar propriedades de evento diretamente nas suas mensagens. Para incluir imagens de produtos, preços ou outros dados do catálogo nas suas mensagens, vincule seu catálogo ao evento usando `product_id` ou `variant_id` como identificador de ligação. A tag Liquid {% raw %}`{% shopping_cart %}`{% endraw %} permite percorrer o conteúdo atual do carrinho de um usuário para lembretes de carrinho abandonado, incentivos de checkout ou confirmações de pedido. Para exemplos de código prontos para uso, consulte [Casos de uso de eCommerce]({{site.baseurl}}/ecommerce_use_cases).

Como alternativa sem código, os [blocos de produto de arrastar e soltar]({{site.baseurl}}/user_guide/messaging/design_and_edit/product_blocks) estão disponíveis no programa de acesso antecipado.

### Modelos de Canvas para eCommerce {#ecommerce-canvas-templates}

A Braze fornece modelos de Canvas prontos para uso, pré-configurados com eventos recomendados de eCommerce como critérios de entrada, saída e conversão, para que você possa lançar fluxos de ciclo de vida sem configuração personalizada. Cada modelo inclui designs de e-mail de arrastar e soltar e suporta blocos de produto de arrastar e soltar (atualmente em acesso antecipado). Para casos de uso detalhados e exemplos com Liquid, consulte [Casos de uso de eCommerce]({{site.baseurl}}/ecommerce_use_cases).

Esses modelos cobrem os fluxos de ciclo de vida de eCommerce mais comuns. Use-os como ponto de partida e personalize o tempo, os canais e o criativo para o seu público.

{% tabs %}
{% tab Navegação abandonada %}

Reengaja usuários que visualizaram um produto, mas não o adicionaram ao carrinho.

Use este modelo quando quiser trazer navegadores de volta para considerar produtos que visualizaram recentemente, mas não agiram.

| Configuração | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.product_viewed` |
| Eventos de saída | `ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Evento de conversão | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de Canvas para eCommerce" }

{% endtab %}
{% tab Carrinho abandonado %}

Recupera usuários que adicionaram itens ao carrinho, mas não iniciaram o checkout.

Use este modelo quando quiser lembrar os usuários sobre os itens no carrinho e incentivá-los a concluir a compra.

| Configuração | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.cart_updated` |
| Eventos de saída | `ecommerce.cart_updated`, `ecommerce.checkout_started`, Placed Order |
| Evento de conversão | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de Canvas para eCommerce" }

{% alert tip %}
O evento `ecommerce.cart_updated` suporta substituição completa do carrinho (cada evento pode descrever o carrinho inteiro) ou atualizações incrementais usando os valores `add` e `remove` para a propriedade opcional `action`. Escolha uma abordagem por carrinho e evite misturar atualizações de substituição e incrementais para o mesmo `cart_id`. Use a tag Liquid {% raw %}`{% shopping_cart %}`{% endraw %} na sua mensagem para exibir dinamicamente o conteúdo atual do carrinho no momento do envio.
{% endalert %}

{% endtab %}
{% tab Checkout abandonado %}

Recupera usuários que iniciaram o checkout, mas não concluíram a compra.

Use este modelo quando quiser recuperar compras no estágio de maior intenção do funil.

| Configuração | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.checkout_started` |
| Evento de saída | Placed Order |
| Evento de conversão | Placed Order |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de Canvas para eCommerce" }

{% endtab %}
{% tab Confirmação de pedido e pesquisa %}

Confirma uma compra bem-sucedida e faz um acompanhamento com uma pesquisa de feedback para coletar avaliações e impulsionar o engajamento pós-compra.

Use este modelo quando quiser simplificar a comunicação pós-compra e coletar feedback dos clientes em um único fluxo de trabalho.

| Configuração | Valor |
| --- | --- |
| Evento de entrada | `ecommerce.order_placed` |
| Evento de conversão | Start Session ou `ecommerce.product_viewed` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modelos de Canvas para eCommerce" }

{% endtab %}
{% endtabs %}

#### Personalizar modelos {#customize-templates}

Esses modelos foram projetados como ponto de partida. Personalizações comuns incluem:
  - **Personalizar o e-mail:** Cada modelo inclui um e-mail pré-configurado criado com o editor de arrastar e soltar, totalmente editável para combinar com sua marca e conteúdo.
  - **Adicionar canais:** Combine e-mail com push, SMS ou mensagens no app para reforço entre canais.
  - **Adicionar postergações e divisões de decisão:** Ramifique os usuários por comportamento (por exemplo, carrinho de alto valor comparado com carrinho de baixo valor) ou períodos de espera entre mensagens.
  - **Trocar o criativo:** Substitua o modelo de e-mail incluído pelo estilo visual da sua marca.
  - **Usar blocos de produto:** Use blocos de produto de arrastar e soltar (no programa de acesso antecipado) para renderizar dinamicamente o conteúdo de carrinhos abandonados ou produtos visualizados sem escrever Liquid personalizado.

Para estratégias de ciclo de vida mais avançadas, incluindo exemplos de personalização com Liquid, consulte [Casos de uso de eCommerce]({{site.baseurl}}/ecommerce_use_cases).

## Relatórios de eCommerce {#ecommerce-reporting}

Os eventos recomendados de eCommerce alimentam as mesmas superfícies de receita que os clientes já utilizam hoje. Quando sua integração está enviando eventos de eCommerce, os relatórios a seguir incluem a receita de eCommerce automaticamente:

| Relatório                                    | O que mostra                              |
|----------------------------------------------|-------------------------------------------|
| Relatório de receita                         | Receita total, receita média diária, compras diárias e receita por usuário ao longo do tempo em todas as fontes para o intervalo de datas e apps selecionados.                                                                                     |
| Dashboard de receita por último ponto de contato | Receita atribuída à última Campaign ou Canvas com que o usuário interagiu antes de fazer um pedido. Os eventos de contato incluem cliques em e-mail, aberturas de push, cliques em cartões de conteúdo, cliques em mensagens no app e cliques em links curtos de SMS ou WhatsApp. |
| Análises de Campaign e Canvas                | Receita total atribuída a uma Campaign ou Canvas específica dentro da janela de conversão primária.                                                                                   |
| Relatório de conversões                      | Receita vinculada a eventos de conversão em Campaigns e Canvas.<br> **Nota:** Para contabilizar a receita de `ecommerce.order_placed`, a Campaign ou Canvas deve usar o tipo de evento de conversão "Place Order" como seu evento de conversão.                                                                                    |
| Insights de segmento                         | Comparações de receita entre segmentos no dashboard de insights de segmento.                                                               |
| Report Builder                               | Métricas de receita em relatórios personalizados criados no Report Builder.                                                                                  |
| Dashboard Builder                            | Métricas de receita em dashboards personalizados criados no Dashboard Builder.                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Relatórios de eCommerce" }

Para campos calculados que não são de usuário (por exemplo, receita de Campaign ou Canvas), a receita é calculada da mesma forma em todos os relatórios: `price` multiplicado por `quantity` por produto no pedido, somando todos os produtos em cada evento `order_placed`.

{% alert note %}
Os cálculos de receita limitam as quantidades individuais de produtos a 1.000 unidades por pedido. Se o campo de quantidade estiver ausente para um produto, o padrão é uma unidade. O evento original `ecommerce.order_placed` mantém a quantidade total que você enviou — apenas o cálculo de receita aplica o limite.<br><br>
Se você está migrando de eventos de compra legados para `ecommerce.order_placed`, coordene com sua equipe de conta da Braze antes de fazer qualquer alteração na integração. Durante o período de transição, envie tanto os eventos de compra legados quanto os eventos `ecommerce.order_placed` para confirmar que estão sendo disparados corretamente e para preparar suas Campaigns, Canvas e Segments ativos para migrar para o novo evento. Sua equipe de conta pode ajudar você a planejar a transição para mudar os relatórios de receita dos eventos de compra legados para `ecommerce.order_placed`.
{% endalert %}

### BrazeAI<sup>TM</sup>

[Eventos Preditivos]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events), [Churn Preditivo]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn) e [recomendações de itens]({{site.baseurl}}/user_guide/brazeai/item_recommendations) aceitam eventos de eCommerce como eventos-alvo e sinais, e possuem uma opção dedicada "Order Placed". O esquema padronizado torna esses modelos mais confiáveis porque os dados são consistentes em toda a sua base de usuários.

### Exportar dados {#export-data}

A Braze oferece várias maneiras de exportar dados de eventos de eCommerce para uso em seu data warehouse, ferramentas de BI ou sistemas downstream. Os eventos recomendados de eCommerce são exportados pelos mesmos canais que seus outros dados de eventos.

| Caminho de exportação                | O que está incluído                                                                                                                                                                            |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)                            | Os eventos de eCommerce são transmitidos como eventos personalizados; pesquise o namespace `ecommerce.*` para encontrá-los. Os produtos de cada pedido estão disponíveis como compras.                                                |
| [Compartilhamento de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing)               | Os eventos de eCommerce são compartilhados como eventos personalizados; pesquise o namespace `ecommerce.*` para encontrá-los. Os produtos de cada pedido estão disponíveis na tabela de compras.                                   |
| [Exportar dados de segmento para CSV]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv)           | Exportação em CSV dos membros do segmento. Para incluir eventos de eCommerce, selecione-os pelo nome no dropdown de eventos personalizados.                                                                                |
| [Exportar perfil de usuário por Segment (API)]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment#prerequisites) | Dados de perfil de usuário para membros do segmento, retornados via API. Os eventos de eCommerce são incluídos como eventos personalizados.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Exportar dados" }

### Como segmentar usuários por um produto específico? {#how-do-i-segment-users-by-a-specific-product}

O segmentador permite filtrar pelo número de vezes que um usuário realizou um evento de eCommerce. Para filtrar por propriedades específicas de produto (como `product_id` ou `product_name`), use [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension), que aceitam filtragem por propriedades de evento aninhadas. Por exemplo, você pode encontrar todos os usuários que compraram o produto "SKU-123" nos últimos 90 dias.