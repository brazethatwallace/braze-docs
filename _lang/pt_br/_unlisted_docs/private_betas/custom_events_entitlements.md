---
article_title: Eventos personalizados
permalink: "/custom_events_entitlements/"
hidden: true
---

# [![Curso do Braze Learning]({% image_buster /assets/unlisted_docs/img/logos/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Eventos personalizados {#braze-learning-course-image_buster-assetsunlisted_docsimglogosbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> Este artigo descreve eventos personalizados e propriedades, filtros de segmentação relacionados, propriedades de entrada do Canvas, análise de dados relevante e muito mais. Para saber mais sobre eventos da Braze em geral, consulte [Eventos]({{site.baseurl}}/user_guide/data/activation/events).

Eventos personalizados são ações realizadas por, ou atualizações sobre, seus usuários. Quando eventos personalizados são registrados, eles podem disparar qualquer número e tipo de campanhas de acompanhamento. Você pode então usar [filtros de segmentação](#segmentation-filters) para segmentar usuários com base em quão recentemente e com que frequência esses eventos personalizados ocorreram. Isso torna os eventos personalizados ideais para rastrear interações de alto valor dos usuários dentro do seu aplicativo.

## Casos de uso {#use-cases}

Alguns casos de uso comuns de eventos personalizados incluem:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## Direitos de uso {#entitlements}

Os direitos de uso determinam a capacidade de eventos personalizados, que rastreia o número de nomes de eventos diferentes que você define. Você pode ter até 2.000 eventos personalizados por espaço de trabalho. Se precisar aumentar sua capacidade, entre em contato com seu gerente de conta da Braze para saber mais.

Conforme seu espaço de trabalho se aproxima do número máximo de eventos personalizados, você receberá notificações no dashboard e por e-mail para se manter informado.

Mesmo após atingir a capacidade, os eventos personalizados existentes ainda podem ser recebidos. No entanto, você não poderá criar novos eventos personalizados. Quaisquer dados recebidos para eventos personalizados que ainda não existam não serão processados.

## Gerenciando eventos personalizados {#managing-custom-events}

Você pode gerenciar, criar ou bloquear eventos personalizados no dashboard acessando **Configurações de Dados** > **Eventos Personalizados**.

Selecione o menu ao lado de um evento personalizado para as seguintes ações:

### Bloqueio {#blocklisting}

Você pode bloquear eventos personalizados individuais pelo menu de ações ou selecionar e bloquear até 100 eventos em massa.

Quando você bloqueia um evento personalizado:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

Além disso, se um evento personalizado bloqueado estiver sendo referenciado por filtros ou disparadores em outras áreas da Braze, um modal de aviso aparecerá explicando que todas as instâncias dos filtros ou disparadores que o referenciam serão removidas e arquivadas.

### Adicionando descrições {#adding-descriptions}

Você pode adicionar uma descrição a um evento personalizado após ele ser criado, desde que tenha a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) `Manage Events, Attributes, Purchases`. Selecione **Editar descrição** para o evento personalizado e insira o que quiser, como uma nota para sua equipe.

## Adicionando tags {#adding-tags}

Você pode adicionar tags a um evento personalizado depois que ele for criado, desde que tenha a [permissão de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "Manage Events, Attributes, Purchases". As tags podem então ser usadas para filtrar a lista de eventos.

### Visualizando relatórios de uso {#viewing-usage-reports}

O relatório de uso lista todos os Canvas, Campaigns e Segments que utilizam um evento personalizado específico. A lista não inclui usos de Liquid.

Você pode visualizar até 100 relatórios de uso por vez selecionando as caixas de seleção de vários eventos personalizados e então selecionando **View usage report**.

## Exportando dados {#exporting-data}

Para exportar a lista de eventos personalizados como um arquivo CSV, selecione o botão **Exportar tudo** no topo da página. O arquivo CSV será gerado, e um link para download será enviado para o seu e-mail.

## Registro de eventos personalizados {#logging-custom-events}

Eventos personalizados exigem configuração adicional. Consulte os links da documentação da plataforma para encontrar os métodos usados para registrar eventos personalizados e adicionar propriedades e quantidades.

{% details Expandir para documentação por plataforma %}

- [Android e FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?sdktab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## Armazenamento de eventos personalizados {#custom-event-storage}

Todos os dados armazenados no **Perfil do Usuário**, incluindo metadados de eventos personalizados (primeira ou última ocorrência, contagem total e X em Y nos últimos 30 dias), são retidos indefinidamente enquanto cada perfil estiver [ativo]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#active-users).

## Filtros de segmentação {#segmentation-filters}

A tabela a seguir mostra os filtros disponíveis para segmentar usuários por eventos personalizados.

| Opções de segmentação | Filtro suspenso | Opções de entrada |
| ---------------------| --------------- | ------------- |
| Verificar se o evento personalizado ocorreu **mais de X vezes** | **MORE THAN** | **NUMBER** |
| Verificar se o evento personalizado ocorreu **menos de X vezes** | **LESS THAN** | **NUMBER** |
| Verificar se o evento personalizado ocorreu **exatamente X vezes** | **EXACTLY** | **NUMBER** |
| Verificar se o evento personalizado ocorreu pela última vez **após a data X** | **AFTER** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **antes da data X** | **BEFORE** | **TIME** |
| Verificar se o evento personalizado ocorreu pela última vez **há mais de X dias** | **MORE THAN** | **NUMBER OF DAYS AGO** (número positivo) |
| Verificar se o evento personalizado ocorreu pela última vez **há menos de X dias** | **LESS THAN** | **NUMBER OF DAYS AGO** (número positivo) |
| Verificar se o evento personalizado ocorreu **mais de X (máx. = 50) vezes** | **MORE THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **menos de X (máx. = 50) vezes** | **LESS THAN** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
| Verificar se o evento personalizado ocorreu **exatamente X (máx. = 50) vezes** | **EXACTLY** | nos últimos **Y dias (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Análise de dados {#analytics}

A Braze registra o número de vezes que eventos personalizados ocorreram e a última vez que foram realizados por cada usuário para segmentação. Para configuração de relatórios, filtros e opções de exportação, consulte [Relatório de eventos personalizados]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report).

Na página **Custom Events Report**, você pode visualizar de forma agregada a frequência de cada evento personalizado. As linhas cinzas sobrepostas na série temporal indicam a última vez que uma Campaign foi enviada, o que é útil para verificar como suas Campaigns afetaram a atividade de eventos personalizados.

![Gráfico de contagem de eventos personalizados na página Custom Events no dashboard mostrando tendências de um evento personalizado][8]

Você também pode usar **Filters** para detalhar seus eventos personalizados por hora, média mensal de usuários ativos (MAU), Segments ou fórmulas de KPI.

{% alert tip %}
[Incremente atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#integers) para manter um contador de ações do usuário de forma semelhante a um evento personalizado. No entanto, não é possível visualizar dados de atributos personalizados em uma série temporal. Ações do usuário que não precisam ser analisadas em série temporal devem ser registradas usando esse método.
{% endalert %}

### Por que a análise de eventos personalizados não está aparecendo {#why-custom-events-analytics-arent-showing}

Segments criados com dados de eventos personalizados não podem exibir dados históricos anteriores à data de criação.

## Propriedades de eventos personalizados {#custom-event-properties}

Propriedades de eventos personalizados são metadados ou atributos de eventos personalizados que descrevem uma ocorrência específica de um evento. Essas propriedades podem ser usadas para qualificar ainda mais as condições de disparo, aumentar a personalização no envio de mensagens, rastrear conversões e gerar análises mais sofisticadas por meio da exportação de dados brutos.

As propriedades de eventos personalizados não são armazenadas no perfil da Braze e, portanto, não consomem pontos de dados (consulte [Pontos de dados](#data-points) para exceções).

{% alert important %}
Cada evento personalizado ou compra pode ter até 256 propriedades de eventos personalizados distintas. Se um evento personalizado ou compra for registrado com mais de 256 propriedades, somente as primeiras 256 serão capturadas e estarão disponíveis para uso.
{% endalert %}

### Formato esperado {#expected-format}

Os valores das propriedades devem ser um objeto em que as chaves são os nomes das propriedades e os valores são os valores das propriedades. Os nomes das propriedades devem ser strings não vazias com 255 caracteres ou menos, sem cifrões iniciais (`$`).

Os valores das propriedades podem ser de qualquer um dos seguintes tipos de dados:

| Tipo de dados | Descrição |
| --- | --- |
| Números | Como [inteiros](https://en.wikipedia.org/wiki/Integer) ou [ponto flutuante](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Booleanos | Valor de `true` ou `false`. |
| Datas e horas | Formatados como strings no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ou `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Não suportado dentro de arrays. |
| Strings | 255 caracteres ou menos. |
| Arrays | Arrays não podem incluir datas e horas. |
| Objetos | Objetos serão ingeridos como strings. |
| Objetos aninhados | Objetos que estão dentro de outros objetos. Para saber mais, consulte a seção neste artigo sobre [Objetos aninhados](#nested-objects).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Objetos de propriedade de evento que contêm valores de array ou objeto podem ter uma carga útil de propriedade de evento de até 100&nbsp;KB.

Você pode alterar o tipo de dados da propriedade de evento personalizado, mas esteja ciente dos impactos de [alterar tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type) após os dados terem sido coletados.

### Usando propriedades de eventos personalizados {#using-custom-event-properties}

As propriedades de eventos personalizados podem ser usadas para qualificar disparos de Campaigns, rastrear conversões e personalizar o envio de mensagens.

#### Disparar mensagens {#trigger-messages}

Use propriedades de eventos personalizados para restringir ainda mais o seu público para uma Campaign ou Canvas específico. Por exemplo, se você tiver um aplicativo de e-commerce e quiser enviar uma mensagem a um usuário quando ele abandonar o carrinho, você pode adicionar uma propriedade de evento personalizado de `cart value` para melhorar o público-alvo e permitir maior personalização da Campaign.

![Filtros de propriedade de evento personalizado para um carrinho abandonado. Dois filtros são combinados com um operador AND para enviar esta Campaign a usuários que abandonaram o carrinho com um valor entre 100 e 200 dólares][16]

Propriedades de eventos personalizados aninhadas também são suportadas na [entrega baseada em ação][19].

![Filtros de propriedade de evento personalizado para um carrinho abandonado. Um filtro é selecionado se qualquer item no carrinho tiver um preço superior a 100 dólares.][20]

#### Personalizar mensagens {#personalize-messages}

Você também pode usar propriedades de eventos personalizados para personalização dentro do modelo de envio de mensagens. Qualquer Campaign usando [entrega baseada em ação][19] com um evento-gatilho pode usar propriedades de eventos personalizados desse evento para personalização das mensagens.

Por exemplo, se você tiver um app de jogos e quiser enviar uma mensagem aos usuários que completaram uma fase, você poderia personalizar ainda mais a mensagem com uma propriedade para o tempo que os usuários levaram para completar aquela fase. Neste exemplo, a mensagem é personalizada para três Segments diferentes usando [lógica condicional][18]. A propriedade de evento personalizado chamada `time_spent` pode ser incluída na mensagem chamando ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

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
Se o usuário não tiver uma conexão com a internet, mensagens no app disparadas com propriedades de eventos personalizados modeladas (por exemplo, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) irão falhar e não serão exibidas.
{% endalert %}

Para uma lista completa de Liquid tags que farão com que mensagens no app sejam entregues como mensagens no app modeladas, consulte [Perguntas frequentes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/).

##### Considerações com filtros {#considerations-with-filters}

- **Chamadas de API:** Ao fazer chamadas de API e usar o filtro "está em branco", uma propriedade de evento personalizado é considerada "em branco" se excluída da chamada. Por exemplo, se você incluir `"event_property": ""`, seus usuários seriam considerados "não em branco".
- **Inteiros:** Ao filtrar por uma propriedade de evento personalizado numérica e o número for muito grande, não use o filtro "exatamente". Se um número for muito grande, ele poderá ser arredondado em um determinado comprimento, e seu filtro não funcionará como esperado.

#### Segmentação {#segmentation}

Use a segmentação por propriedade de evento para direcionar usuários com base em eventos personalizados realizados e nas propriedades associadas a esses eventos. Isso aumenta suas opções de filtragem ao segmentar por compra e eventos personalizados.

As propriedades de evento para eventos personalizados são atualizadas em tempo real para qualquer Segment que as utilize. Você pode gerenciar as propriedades acessando **Configurações de dados** > **Eventos personalizados** e selecionando **Gerenciar propriedades** para o evento personalizado associado. As propriedades de eventos personalizados usadas em certos filtros de Segment têm um histórico máximo de 30 dias.

##### Adicionando propriedades de evento para segmentação {#adding-event-properties-for-segmentation}

Você precisará das [permissões de usuário]({{site.baseurl}}/user_guide/data/data_points#viewing-data-point-usage) "Gerenciar segmentação por propriedade de evento personalizado" para criar Segments com base na recência e frequência de propriedade de evento.

Por padrão, você pode ter 20 propriedades de evento Segmentáveis por espaço de trabalho. Entre em contato com seu gerente de conta da Braze para aumentar esse limite.

Para adicionar propriedades de evento para segmentação, faça o seguinte:

1. Acesse seu evento personalizado e selecione **Gerenciar propriedades**.
2. Selecione o botão **Ativar segmentação** para adicionar a propriedade de evento para segmentação. Você poderá acessar opções adicionais de filtragem ao segmentar.

Os filtros de segmentação por propriedade de evento incluem:

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![Um grupo de filtros com "tem 'Carrinho abandonado' com propriedade 'número de itens' e valor '2' 'mais que' '1' '1 vez nos últimos '30' dias corridos.][3]

Os dados são registrados para uma determinada propriedade de evento somente após ela ter sido ativada pelo seu CSM, e as propriedades de evento ficam disponíveis somente a partir dessa data.

##### Pontos de dados {#data-points}

Em relação ao uso de inscrição, as propriedades de eventos personalizados ativadas para segmentação com os seguintes filtros são todas contadas como pontos de dados separados, além do ponto de dados contado pelo próprio evento personalizado:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propriedades de entrada do Canvas e propriedades de evento {#canvas-entry-properties-and-event-properties}

Você pode usar `canvas_entry_properties` e `event_properties` nas jornadas de usuário do Canvas. Consulte [Propriedades de entrada do Canvas e propriedades de evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) para mais informações e exemplos.

{% tabs local %}
{% tab Propriedades de entrada do Canvas %}

[Propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object) são as propriedades que você mapeia para Canvas que são baseados em ação ou disparados por API. Note que o objeto `canvas_entry_properties` tem um limite máximo de tamanho de 50 KB.

{% alert note %}
Especificamente para canais de mensagens no app, `canvas_entry_properties` só pode ser referenciado no Canvas Flow e no editor original do Canvas se você tiver as propriedades de entrada persistentes ativadas no editor original como parte do acesso antecipado anterior.
{% endalert %}

Para envio de mensagens no Canvas Flow, `canvas_entry_properties` pode ser usado em qualquer etapa de Mensagem com este formato Liquid: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. Note que os eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma.

#### Caso de uso {#use-case}

{% raw %}
Digamos que uma loja de varejo, RetailApp, tenha a seguinte solicitação: `"canvas_entry_properties" : {"product_name" : "shoes", "product_price" : 79.99}`. A RetailApp pode incluir o nome do produto (shoes) em uma mensagem com o Liquid `{{canvas_entry_properties.${product_name}}}`.
{% endraw %}

A RetailApp também pode disparar mensagens específicas para enviar com base em diferentes propriedades `product_name` em um Canvas que direciona usuários após eles terem disparado um evento de compra. Por exemplo, eles podem enviar mensagens diferentes para usuários que compraram sapatos e usuários que compraram outra coisa, adicionando o seguinte Liquid em uma etapa de Mensagem.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Expandir para o editor original do Canvas %}

A partir de 28 de fevereiro de 2023, você não pode mais criar ou duplicar Canvas usando o editor original. Esta seção está disponível apenas para referência.

Para Canvas criados com o editor original, `canvas_entry_properties` pode ser referenciado apenas na primeira etapa completa de um Canvas.

{% enddetails %}
{% endtab %}

{% tab Propriedades de evento %}

{% alert important %}
Você não pode usar `event_properties` na primeira etapa de Mensagem. Em vez disso, você deve usar `canvas_entry_properties` ou adicionar uma etapa de jornadas de ação com o evento correspondente **antes** da etapa de Mensagem que inclui `event_properties`.
{% endalert %}

Propriedades de evento referem-se às propriedades que você define para eventos personalizados e compras. Esses `event_properties` podem ser usados em Campaigns com entrega baseada em ação e em Canvas.

No Canvas Flow, propriedades de eventos personalizados e de eventos de compra podem ser usadas em Liquid em qualquer etapa de Mensagem que siga uma etapa de jornadas de ação. Certifique-se de usar {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} ao referenciar esses `event_properties`. Esses eventos devem ser eventos personalizados ou eventos de compra para serem usados dessa forma no componente de Mensagem.

Na primeira etapa de Mensagem após uma jornada de ação, você pode usar `event_properties` relacionadas ao evento referenciado nessa jornada de ação. Esses `event_properties` só podem ser usados se o usuário realmente realizou a ação (e não foi para o grupo Todos os demais). Você pode ter outras etapas (que não sejam outra etapa de jornadas de ação ou de Mensagem) entre essa jornada de ação e a etapa de Mensagem.

{% details Expandir para o editor original do Canvas %}

A partir de 28 de fevereiro de 2023, você não pode mais criar ou duplicar Canvas usando o editor original. Esta seção está disponível apenas para referência.

Para o editor original do Canvas, `event_properties` não pode ser usado em etapas completas agendadas. No entanto, você pode usar `event_properties` na primeira etapa completa de um Canvas baseado em ação, mesmo que a etapa completa seja agendada.

{% enddetails %}

{% endtab %}
{% endtabs %}

### Objetos aninhados {#nested-objects}

Você pode usar objetos aninhados (objetos dentro de outro objeto) para enviar dados JSON aninhados como propriedades de eventos personalizados e compras. Esses dados aninhados podem ser usados para modelar informações personalizadas em mensagens, disparar envios de mensagens e segmentar usuários.

Para saber mais, consulte nossa página dedicada sobre [Objetos aninhados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

## Armazenamento de propriedades de eventos personalizados {#custom-event-property-storage}

As propriedades de eventos personalizados foram projetadas para ajudar você a aumentar a precisão do direcionamento e tornar as mensagens ainda mais personalizadas. As propriedades de eventos personalizados podem ser armazenadas na Braze tanto a curto quanto a longo prazo.

Você pode segmentar com base nos valores das propriedades de eventos de duas formas:

1. **Em até 30 dias:** a equipe de suporte da Braze pode ativar a segmentação por propriedades de eventos com base na frequência e na recência de valores específicos de propriedades de eventos dentro dos Segments da Braze. Se quiser aproveitar as propriedades de eventos dentro dos Segments, entre em contato com o executivo de conta ou o CSM da Braze. Essa opção afetará o uso de dados.<br><br>
2. **Em até 30 dias ou mais:** para cobrir tanto a segmentação de propriedades de eventos de curto prazo quanto de longo prazo, você pode usar as [extensões de Segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Esse recurso segmenta os usuários com base em eventos personalizados e propriedades de eventos rastreados nos últimos dois anos. Essa opção não afetará o uso de dados.

Entre em contato com o CSM da Braze para obter recomendações sobre a melhor abordagem de acordo com suas necessidades específicas.

[1]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object1.png %}
[2]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object2.png %}
[3]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_object3.png %}
[4]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/schema_generation_example.png %}
[8]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[16]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/unlisted_docs/img/custom_events_entitlements/customEventPropertiesNested.png %} "customEventPropertiesNested.png"