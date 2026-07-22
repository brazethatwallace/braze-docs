---
nav_title: Propriedades de eventos personalizados
article_title: Propriedades de eventos personalizados
page_order: 0
page_type: reference
description: "Este artigo descreve as propriedades de eventos personalizados, o formato esperado, como usá-las e o armazenamento de propriedades de eventos personalizados."
---

# Propriedades de eventos personalizados {#custom-event-properties}

> Este artigo descreve as propriedades de eventos personalizados, o formato esperado, como usá-las para envio de mensagens e segmentação, e o armazenamento de propriedades de eventos personalizados.

As propriedades de eventos personalizados são metadados ou atributos de eventos personalizados que descrevem uma ocorrência específica de um evento. Essas propriedades podem ser usadas para qualificar ainda mais as condições de gatilho, aumentar a personalização no envio de mensagens, rastrear conversões e gerar análises de dados mais sofisticadas por meio da exportação de dados brutos.

As propriedades de eventos personalizados não são armazenadas no perfil da Braze e, portanto, não registram pontos de dados (consulte [Pontos de dados](#data-points) para exceções).

{% alert important %}
Cada evento personalizado ou compra pode ter até 256 propriedades de eventos personalizados distintas. Se um evento personalizado ou compra for registrado com mais de 256 propriedades, apenas as primeiras 256 serão capturadas e estarão disponíveis para uso.
{% endalert %}

## Formato esperado {#expected-format}

Os valores das propriedades devem ser um objeto: as chaves são os nomes das propriedades (strings não vazias, com 255 caracteres ou menos, sem `$` no início), e os valores são os valores das propriedades. Para tipos de dados compatíveis, requisitos de formato e limites de carga útil, consulte [Tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#event-property-data-types).

Você pode alterar o tipo de dados da propriedade do seu evento personalizado, mas esteja ciente dos impactos de [alterar tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type) após os dados terem sido coletados.

### Chaves reservadas {#reserved-keys}

Você não pode usar chaves reservadas como nomes de propriedades de eventos. Usar uma chave reservada no objeto `properties` retorna o erro "Invalid 'properties' field".

| Propriedade | Chave reservada |
| --- | --- |
| Eventos personalizados | `time` e `event_name` |
| Eventos de compra | `time`, `product_id`, `quantity`, `event_name`, `price`, `currency` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Chaves reservadas" }

## Usando propriedades de eventos personalizados {#using-custom-event-properties}

As propriedades de eventos personalizados podem ser usadas para qualificar gatilhos de Campaigns, rastrear conversões e personalizar mensagens.

### Disparar mensagens {#trigger-messages}

Use propriedades de eventos personalizados para refinar ainda mais o público de uma Campaign ou Canvas específico. Por exemplo, se você tem um aplicativo de e-commerce e deseja enviar uma mensagem a um usuário quando ele abandona o carrinho, pode adicionar uma propriedade de evento personalizado de `price` para melhorar o público-alvo e permitir maior personalização da Campaign.

![Filtros de propriedades de eventos personalizados para um carrinho abandonado. Dois filtros são combinados com um operador AND para enviar esta Campaign a usuários que abandonaram o carrinho com um preço entre 100 e 200 dólares]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"){: style="max-width:70%;"}

Propriedades de eventos personalizados aninhadas também são compatíveis com a [entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Filtros de propriedades de eventos personalizados para um carrinho abandonado. Um filtro é selecionado se algum item no carrinho tiver um preço superior a 100 dólares.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"){: style="max-width:70%;"}

### Personalizar mensagens {#personalize-messages}

Você também pode usar propriedades de eventos personalizados para personalização dentro do modelo de mensagem. Qualquer Campaign que use [entrega baseada em ação]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) com um evento de gatilho pode usar propriedades de eventos personalizados desse evento para personalização de mensagens.

Por exemplo, se você tem um app de jogos e deseja enviar uma mensagem a usuários que completaram uma fase, pode personalizar ainda mais sua mensagem com uma propriedade para o tempo que os usuários levaram para completar essa fase. Neste exemplo, a mensagem é personalizada para três segmentos diferentes usando [lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic). A propriedade de evento personalizado chamada `time_spent` pode ser incluída na mensagem chamando ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Se o usuário não tiver conexão com a internet, mensagens no app disparadas com propriedades de eventos personalizados modeladas (por exemplo, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) falharão e não serão exibidas.
{% endalert %}

Para uma lista completa de Liquid tags que fazem com que mensagens no app sejam entregues como mensagens no app modeladas, consulte as [Perguntas frequentes]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages).

#### Considerações com filtros {#considerations-with-filters}

- **Chamadas de API:** Ao fazer chamadas de API e usar o filtro "está em branco", uma propriedade de evento personalizado é considerada "em branco" se for excluída da chamada. Por exemplo, se você incluir `"event_property": ""`, seus usuários serão considerados "não em branco".
- **Números inteiros:** Ao filtrar por uma propriedade de evento personalizado numérica e o número for muito grande, não use o filtro "exatamente". Se um número for muito grande, ele pode ser arredondado em um determinado comprimento, e seu filtro não funcionará como esperado.

### Segmentação {#segmentation}

Use a segmentação por propriedades de eventos para direcionar usuários com base em eventos personalizados realizados e nas propriedades associadas a esses eventos. Isso aumenta suas opções de filtragem ao segmentar por compras e eventos personalizados.

As propriedades de eventos para eventos personalizados são atualizadas em tempo real para qualquer segmento que as utilize. Você pode gerenciar propriedades acessando **Configurações de dados** > **Eventos personalizados** e selecionando **Gerenciar propriedades** para o evento personalizado associado. As propriedades de eventos personalizados usadas em determinados filtros de segmento têm um histórico máximo de retrospectiva de 30 dias.

#### Adicionando propriedades de eventos para segmentação {#adding-event-properties-for-segmentation}

Você precisa da [permissão de usuário]({{site.baseurl}}/user_guide/data/infrastructure/data_points#viewing-data-point-usage) "Edit Custom Event Property Segmentation" para criar segmentos com base na recência e frequência de propriedades de eventos.

Por padrão, você pode ter 20 propriedades de eventos segmentáveis por espaço de trabalho. Entre em contato com o gerente da sua conta na Braze para aumentar esse limite.

Para adicionar propriedades de eventos para segmentação, faça o seguinte:

1. Acesse seu evento personalizado e selecione **Gerenciar propriedades**.
2. Ative o botão **Ativar segmentação** para adicionar a propriedade de evento para segmentação. Você terá acesso a opções adicionais de filtragem ao segmentar.

Os filtros de segmentação por propriedades de eventos incluem:

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![Um grupo de filtros com "Abandoned Cart" com propriedade "number of items" e valor 2 mais de 1 vez nos últimos 30 dias corridos.]({% image_buster /assets/img/nested_object3.png %})

Os dados são registrados apenas para uma determinada propriedade de evento após você ativá-la, e as propriedades de eventos ficam disponíveis apenas a partir dessa data em diante.

#### Pontos de dados {#data-points}

Em relação ao uso de inscrição, as propriedades de eventos personalizados ativadas para segmentação com os seguintes filtros são todas contadas como pontos de dados separados, além do ponto de dados contado pelo próprio evento personalizado:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propriedades de entrada do Canvas e propriedades de eventos {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### Objetos aninhados {#nested-objects}

Você pode usar objetos aninhados (objetos dentro de outro objeto) para enviar dados JSON aninhados como propriedades de eventos personalizados e compras. Esses dados aninhados podem ser usados para modelar informações personalizadas em mensagens, disparar envios de mensagens e segmentar usuários.

Para saber mais, consulte nossa página dedicada sobre [Objetos aninhados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

## Armazenamento de propriedades de eventos personalizados {#custom-event-property-storage}

As propriedades de eventos personalizados são projetadas para ajudar você a aumentar a precisão do direcionamento e tornar as mensagens ainda mais personalizadas. As propriedades de eventos personalizados podem ser armazenadas na Braze tanto a curto quanto a longo prazo.

Você pode segmentar com base nos valores das propriedades de eventos de duas maneiras:

1. **Dentro de 30 dias:** Você pode usar a segmentação por propriedades de eventos com base na frequência e recência de valores específicos de propriedades de eventos dentro dos Segments da Braze. Essa opção impacta o uso de dados.<br><br>
2. **Dentro e além de 30 dias:** Para cobrir tanto a segmentação de propriedades de eventos de curto quanto de longo prazo, você pode usar [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Esse recurso segmenta usuários com base em eventos personalizados e propriedades de eventos rastreados nos últimos dois anos. Essa opção não impacta o uso de dados.

Entre em contato com o gerente de sucesso do cliente da Braze para recomendações sobre a melhor abordagem, dependendo das suas necessidades específicas.