---
nav_title: Eventos de compra
article_title: Eventos de compra
page_order: 3
page_type: reference
description: "Este artigo de referência descreve eventos e propriedades de compra, seu uso, segmentação, onde visualizar a análise de dados relevante e mais."
search_rank: 3
---

# Eventos de compra {#purchase-events}

> Esta página aborda eventos e propriedades de compra, seu uso, segmentação, onde visualizar análises de dados relevantes e muito mais.

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation' %}

Os eventos de compra são ações de compra realizadas por seus usuários e são usados para registrar compras no app e estabelecer o Lifetime Value (LTV) para cada perfil de usuário. Esses eventos devem ser configurados pela sua equipe. Registrar eventos de compra permite adicionar propriedades como quantidade e tipo, ajudando a direcionar ainda mais seus usuários com base nessas propriedades.

## Registrar eventos de compra {#log-purchase-events}

Você pode registrar compras passando um [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object) pelo [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), ou usando uma das nossas bibliotecas de SDK listadas na seção a seguir.

{% alert note %}
As propriedades de eventos de compra usam os mesmos tipos de dados que as [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties#expected-format).
{% endalert %}

A lista a seguir apresenta os métodos usados em diversas plataformas para registrar compras. Nessas páginas, você também encontrará documentação sobre como adicionar propriedades e quantidades ao seu evento de compra. Você pode direcionar ainda mais seus usuários com base nessas propriedades.

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=unity)
- [.NET MAUI (anteriormente Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases?tab=roku)

## Visualizar dados de compra {#view-purchase-data}

Após configurar e começar a registrar eventos de compra, você pode visualizar esses dados de compra no perfil de um usuário na [guia Visão geral]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab).

## Usar dados de compra {#use-purchase-data}

Existem várias maneiras de usar dados de compra na Braze:

- **[Segmentação](#purchase-event-segmentation):** Use dados de compra para criar Segments de usuários com base no comportamento de compra.
- **[Personalização](#personalization):** Use dados de compra para personalizar mensagens para os usuários.
- **[Disparar mensagens](#trigger-messages):** Configure mensagens para serem disparadas com base em eventos de compra.
- **[Análise de dados](#analytics):** Analise seus dados de compra para obter insights sobre o comportamento dos usuários e a eficácia das suas Campaigns de marketing.

### Segmentação {#purchase-event-segmentation}

Você pode disparar qualquer número ou tipo de Campaigns de acompanhamento com base em eventos de compra registrados. Por exemplo, você pode criar um Segment de usuários que fizeram uma compra nos últimos 30 dias, ou um Segment de usuários que gastaram acima de um determinado valor.

Os seguintes filtros de segmentação estão disponíveis ao direcionar usuários:

- First Made Purchase
- First Purchase For App
- Last Purchased Product
- Money Spent
- Purchased Product
- Total Number of Purchases
- X Money Spent in Y Days
- X Product Purchased in Y Days
- X Purchase Property in Y Days
- X Purchases in Last Y Days

Para detalhes sobre cada filtro, consulte o glossário de [filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) e filtre por "Purchase behavior".

![Filtrando usuários que fizeram exatamente três compras]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Para segmentar pelo número de vezes que uma compra específica ocorreu, registre essa compra individualmente como um [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview#custom-attribute-storage).
{% endalert %}

### Personalização {#personalization}

Assim como qualquer outro tipo de dado coletado dos seus usuários, você pode usar dados de compra para personalizar suas mensagens por meio do Liquid. Por exemplo, você pode enviar um e-mail personalizado a um usuário recomendando produtos semelhantes aos que ele acabou de comprar.

Suponha que você tenha uma propriedade de evento de compra chamada `last_purchased_product` que armazena o nome do último produto que um usuário comprou. Você pode usar essa propriedade para personalizar uma mensagem de e-mail assim:

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

Neste exemplo, a mensagem é personalizada com base na propriedade `last_purchased_product`. Se o último produto que o usuário comprou foi "Running Shoes", ele recebe uma mensagem recomendando shorts de corrida e garrafas de água. Se o último produto foi "Yoga Mat", ele recebe uma mensagem recomendando blocos e faixas de yoga. Se o `last_purchased_product` for qualquer outra coisa, ele recebe uma mensagem genérica de agradecimento.

### Disparar mensagens {#trigger-messages}

Um caso de uso comum é enviar automaticamente uma mensagem, como um e-mail, quando um usuário faz uma compra. Por exemplo, você pode enviar uma mensagem de agradecimento ou um código de desconto para uma compra futura.

Para fazer isso, crie uma Campaign ou Canvas baseada em ação e defina a ação-gatilho como **Make Purchase**. Você também pode especificar condições adicionais para o disparo, como o produto comprado ou o valor da compra.

Você também pode personalizar sua mensagem disparada com Liquid. No exemplo a seguir, `${purchase_product_name}` é um atributo personalizado que você substituiria pelo nome real do atributo que armazena o nome do produto comprado na sua configuração da Braze.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Análise de dados {#analytics}

Além de rastrear métricas de compra para segmentação, a Braze também registra o número de compras de cada produto e a receita gerada ao longo do tempo. Isso pode ser útil para identificar os produtos mais populares ou medir o impacto de uma Campaign promocional nas vendas.

Você pode encontrar esses dados na página [Relatório de receita]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#exporting-revenue-data).

### Cálculos de receita {#revenue-calculations}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Cálculos de receita">
  <caption>Cálculos de receita</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definição</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">Receita vitalícia</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">Valor vitalício por usuário</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">Receita média diária</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">Compras diárias</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">Receita diária por usuário</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### Conversão de moeda {#currency-conversion}

Quando eventos de compra são registrados em uma moeda diferente de USD, a Braze converte o valor para USD usando taxas de câmbio do [Open Exchange Rates](http://openexchangerates.org). Essas taxas são atualizadas uma vez a cada 24 horas (por volta das 4h ET). Como as taxas de câmbio são armazenadas em cache, pode haver pequenas diferenças em relação à taxa de mercado em tempo real, especialmente para moedas com flutuações rápidas.

#### Cálculo de receita vitalícia {#lifetime-revenue-calculation}

A Braze usa eventos de compra para calcular a receita vitalícia (também chamada de valor do tempo de vida ou LTV) de um usuário, que é uma previsão do lucro líquido atribuído a todo o relacionamento futuro com um cliente. Isso pode ajudar você a tomar decisões informadas sobre estratégias de aquisição e retenção de clientes.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$

Existem dois lugares principais na Braze onde você pode consultar o LTV dos seus usuários:

- Para métricas gerais como *receita vitalícia* e o *valor do tempo de vida por usuário* para cada app e site, consulte seu [Relatório de receita]({{site.baseurl}}/user_guide/analytics/reports/revenue_report#exporting-revenue-data).
- Para entender a receita vitalícia de um usuário específico, consulte o [perfil de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#overview-tab) dele.

##### Impacto dos reembolsos na receita vitalícia {#impact-of-refunds-on-lifetime-revenue}

Ao usar eventos de compra para rastrear dados de compra, você deve rastrear reembolsos registrando um evento de compra na Braze com uma propriedade `price` negativa. Essa abordagem mantém um total preciso para a receita vitalícia.

No entanto, tenha em mente que o reembolso contará como um evento de compra adicional. Vamos considerar o seguinte exemplo. Sam faz sua primeira compra de $12, mas devolve parte da compra para um reembolso de $5. O perfil de Sam registraria:

- 1 compra com um preço de $12
- 1 compra com um preço de -$5
- Receita vitalícia de $7

Embora Sam tenha dois eventos de compra no perfil, na realidade, ele fez apenas uma compra. Isso é importante considerar se você tem Segments ou casos de uso baseados no número de compras que um usuário fez. Reembolsos constantes inflarão a contagem de compras no perfil do usuário.

## Propriedades de eventos de compra {#purchase-properties}

Com propriedades de eventos de compra, você pode definir propriedades nas compras que podem ser usadas para qualificar ainda mais condições de gatilho, aumentar a personalização nas mensagens e gerar análises de dados mais sofisticadas por meio da exportação de dados brutos. Os tipos de valor das propriedades (string, numérico, booleano, data) variam por plataforma e geralmente são atribuídos como pares chave-valor.

{% alert warning %}
As seguintes chaves são reservadas e não podem ser usadas como nomes de propriedades de eventos de compra: `time`, `product_id`, `quantity`, `event_name`, `price` e `currency`. Usar uma chave reservada no objeto `properties` retornará o erro "Invalid 'properties' field".
{% endalert %}

Por exemplo, se você tem um aplicativo de e-commerce e deseja enviar uma mensagem a um usuário após uma compra, pode melhorar ainda mais seu público-alvo e permitir maior personalização da campanha adicionando uma propriedade de evento de compra `brand_name`.

**Exemplo de disparo baseado em propriedades de eventos de compra:**

![Configurações de entrega baseada em ação para enviar uma campanha a usuários que compraram fones de ouvido com nome de marca igual a HeadphoneMart]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Consulte o [objeto de propriedades de compra]({{site.baseurl}}/api/objects_filters/purchase_object#purchase-properties-object) para mais informações.

### Segmentação por propriedades de eventos {#event-property-segmentation}

A segmentação por propriedades de eventos permite direcionar usuários com base não apenas nos eventos personalizados realizados, mas também nas propriedades associadas a esses eventos. Isso adiciona opções de filtragem adicionais ao segmentar compras e eventos personalizados.

![Filtros de segmentação para propriedades de eventos de compra, exibindo opções para filtrar usuários com base em valores específicos de propriedades de eventos de compra, como filtrar usuários que compraram um produto com uma determinada propriedade dentro de um período definido.]({% image_buster /assets/img/purchase_event_property.png %}){: style="max-width:80%;margin-left:15px;"}

Esses filtros de segmentação incluem:
- Realizou o evento personalizado com propriedade Y com valor V X vezes nos últimos Y dias
- Fez qualquer compra com propriedade Y com valor V X vezes nos últimos Y dias
- Adiciona segmentação de 1 a 30 dias em todas as compras, eventos e propriedades dentro de compras e eventos

Diferentemente das [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension), os segmentos usados são atualizados em tempo real, suportam uma quantidade ilimitada de segmentos, oferecem um histórico retroativo de no máximo 30 dias e consomem pontos de dados. Devido à cobrança adicional de pontos de dados, você deve entrar em contato com seu gerente de sucesso do cliente da Braze para ativar as propriedades de eventos para seus eventos personalizados.

Quando aprovadas, propriedades adicionais podem ser adicionadas no dashboard em **Configurações de dados** > **Eventos personalizados** selecionando **Manage Properties**. Você pode então usar essas propriedades de eventos na etapa de direcionamento do construtor de Campaigns ou Canvas.

{% include data_activation/segmentable_purchase_properties_keys_note.md %}

### Propriedades de entrada do Canvas e propriedades de eventos {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### Registrar compras no nível do pedido {#log-purchases-at-the-order-level}

Para registrar compras no nível do pedido em vez do nível do produto, use o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação do objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object#naming-conventions) para saber mais.

### Convenções de nomenclatura de Product ID {#product-id-naming-conventions}

Na Braze, oferecemos algumas convenções gerais de nomenclatura para o `product_id` do objeto de compra. Ao escolher o `product_id`, a Braze sugere usar nomes simples como o nome do produto ou a categoria do produto (em vez de SKUs) com a intenção de agrupar todos os itens registrados por esse `product_id`.

Isso torna os produtos fáceis de identificar para segmentação e disparo.

## Bloquear eventos de compra {#blocklist-purchase-events}

Ocasionalmente, você pode identificar eventos de compra que registram muitos pontos de dados, que não são mais úteis para sua estratégia de marketing ou que foram registrados por engano. Para impedir que esses dados sejam enviados à Braze, você pode bloquear o objeto de dados personalizado enquanto sua equipe de engenharia trabalha para removê-lo do backend do seu app ou website.

No dashboard da Braze, você pode gerenciar o bloqueio em **Configurações de Dados** > **Produtos**. Confira [Gerenciando dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data) para saber mais.