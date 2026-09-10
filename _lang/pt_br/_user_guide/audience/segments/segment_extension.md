---
nav_title: Extensões de Segment
article_title: Extensões de Segment
page_order: 5
page_type: reference
description: "Este artigo prático vai orientar você sobre como configurar e usar uma extensão de Segment para aprimorar suas capacidades de segmentação."
tool: Segments
---

# Extensões de Segment {#segment-extensions}

> As extensões de Segment permitem que você crie segmentos muito precisos ao longo de um período estendido do histórico de um usuário. Por exemplo, usando extensões de Segment, você pode direcionar usuários que compraram um produto específico nos últimos dezesseis meses ou que gastaram uma determinada quantia com o seu serviço. Refine esse público usando propriedades de eventos para tornar o direcionamento ainda mais granular.

A segmentação da Braze permite que você direcione usuários com base em eventos personalizados ou comportamento de compra. As extensões de Segment ampliam essa capacidade, permitindo que você utilize dados históricos salvos no perfil do usuário. Com as extensões de Segment, você pode identificar e alcançar usuários que realizaram qualquer evento personalizado ou evento de compra qualquer número de vezes nos últimos dois anos (730 dias).

## Por que usar extensões de Segment? {#why-use-segment-extensions}

Os Segments da Braze oferecem ferramentas de direcionamento poderosas para criar grupos dinâmicos de usuários. Para a maioria dos casos de uso, isso é suficiente para alcançar seu público de forma eficaz. As extensões de Segment são projetadas para casos de uso avançados em que você precisa analisar comportamentos de até dois anos atrás ou aplicar lógica complexa — sem comprometer a retenção de dados ou o desempenho do sistema. Você pode usar consultas [SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) (extensões de Segment SQL) ou dados do seu próprio [data warehouse]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) para refinar ainda mais o seu público.

Por exemplo, a segmentação padrão da Braze encontra usuários que atendem a critérios específicos que você define, como identificar um usuário que comprou recentemente um dos seus produtos. As extensões de Segment permitem ir mais fundo — como identificar usuários que compraram uma cor específica de um produto específico pelo menos duas vezes entre 18 e 24 meses atrás. Extensões de Segment são um aprimoramento, não um requisito. Se você precisa de filtros mais avançados ou de uma janela de retrospectiva mais longa, elas são uma ótima ferramenta para ajudar, mantendo o uso de dados otimizado.

{% alert note %}
Existe uma cota padrão de 50 extensões de Segment ativas por espaço de trabalho em um determinado momento. Se você precisar aumentar esse limite, entre em contato com o seu gerente de sucesso do cliente da Braze para discutir o seu caso de uso.
{% endalert %}

## Criando uma extensão de Segment {#creating-a-segment-extension}

Para criar uma extensão de Segment, você cria um filtro para refinar um segmento dos seus usuários com base em propriedades de eventos personalizados. Ao criar uma extensão de Segment, você escolhe se o segmento é estático ou atualizado dinamicamente em um intervalo definido.

### Etapa 1: Navegue até extensões de Segment {#step-1-navigate-to-segment-extensions}

Acesse **Audience** > **Segment Extensions**.

Na tabela de extensões de Segment, selecione **Create New Extension** e depois selecione sua experiência de criação de extensão de Segment:

- **Simple extension:** Crie uma extensão de Segment focada em um único evento usando um formulário guiado. Ideal para quando você não quer usar SQL.
- **Start with a template:** Crie um Segment SQL com um modelo personalizável usando dados do Snowflake.
- **Incremental refresh:** Escreva um Segment SQL no Snowflake que atualiza automaticamente os últimos 2 dias de dados ou atualize manualmente conforme necessário. Ideal para equilibrar precisão e custo-benefício.
- **Full refresh:** Escreva um Segment SQL com dados do Snowflake ou qualquer [fonte conectada CDI]({{site.baseurl}}/cdi_segment_extensions) que recalcula todo o público mediante atualização manual. Ideal para quando você precisa de uma visão completa e atualizada do seu público.

![Tabela com diferentes experiências de criação de extensão de Segment para selecionar.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Se você selecionar uma experiência que usa SQL, consulte [Extensões de Segment SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) para mais informações. Se você selecionar **Simple extension**, continue para a etapa 2.

#### Uso de créditos SQL {#sql-credit-usage}

Os seguintes tipos de extensão de Segment consomem créditos SQL:

- Extensões de Segment SQL (atualização incremental e completa)
- Segments de catálogo
- Segments CDI
    - Os créditos são consumidos no seu próprio data warehouse

### Etapa 2: Nomeie sua extensão de Segment {#step-2-name-your-segment-extension}

Nomeie sua extensão de Segment descrevendo o tipo de usuários que você pretende filtrar. Isso ajuda outras pessoas a encontrar e aplicar a extensão corretamente.

![Extensão de Segment chamada "Online Shoppers Extension - 90 Days".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Etapa 3: Escolha seus critérios {#step-3-choose-your-criteria}

Selecione entre critérios de compra, engajamento com mensagem, evento recomendado de eCommerce ou evento personalizado para direcionamento. Após selecionar os critérios do tipo de evento desejado, escolha qual item comprado, interação com mensagem, evento recomendado de eCommerce ou evento personalizado você gostaria de direcionar para sua lista de usuários. Em seguida, escolha quantas vezes (mais que, menos que ou igual a) o usuário precisaria ter concluído o evento, e o período — para extensões de Segment especificamente, você pode retroceder até os últimos 730 dias (2 anos).

A segmentação baseada em dados de eventos com mais de 730 dias pode ser feita usando outros filtros localizados em **Segments**. Ao escolher seu período, você pode especificar um intervalo de datas relativo para selecionar os últimos X dias, uma data de início, uma data de término ou um intervalo de datas exato (data A até data B).

![Critérios de segmentação para usuários que realizaram um evento personalizado mais de 2 vezes no intervalo de datas de 1º de março de 2025 a 31 de março de 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

Se você estiver criando uma extensão de Segment usando um evento recomendado de eCommerce, primeiro selecione **eCommerce Recommended Event** como seu critério e depois selecione um evento no menu suspenso.

![Um critério de evento recomendado de eCommerce com um menu suspenso de eventos recomendados disponíveis.]({% image_buster /assets/img/segment/ecommerce_recommended_event_criterion.png %})

#### Segmentação por propriedade de evento {#event-property-segmentation}

Para aumentar a precisão do direcionamento, marque a caixa de seleção **Add Property Filters**. Isso permitirá que você refine com base nas propriedades específicas da sua compra ou evento personalizado. Oferecemos suporte à segmentação por propriedade de evento baseada em objetos de string, numérico, booleano e tempo.

##### Tipos de dados de propriedade {#property-data-types}

Para propriedades de string, você pode inserir vários valores de uma vez. No exemplo a seguir, este filtro procura usuários com uma raça de cachorro igual a qualquer uma das seis raças específicas.

![Segmentação baseada em propriedades de string.]({% image_buster /assets/img/segment/property5.png %})

##### Propriedades de eventos recomendados de eCommerce {#ecommerce-recommended-event-properties}

Quando você adiciona uma propriedade de evento para um evento recomendado de eCommerce, o menu suspenso de propriedades é preenchido automaticamente com as propriedades disponíveis para aquele evento.

As extensões de Segment suportam apenas propriedades de evento na lista de permissões documentada para cada evento recomendado de eCommerce. Propriedades personalizadas de nível superior que você envia pela API ou SDK não são válidas para filtros de propriedade da extensão — mesmo que essas propriedades apareçam nos seus dados de evento. Usar uma propriedade de nível superior não listada impede que a extensão seja salva ou desarquivada.

Se você precisar filtrar por propriedades não padrão, aninhe-as dentro de `metadata` ao registrar o evento (por exemplo, `metadata.color` em vez de `color`). Para propriedades suportadas, consulte [Esquemas de eventos]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas) e [Tipos de eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events).

![Detalhes da extensão de Segment com um menu suspenso de propriedades disponíveis.]({% image_buster /assets/img/segment/ecommerce_recommended_event_properties.png %})

##### Propriedades de evento aninhadas {#nested-event-properties}

Também oferecemos suporte à segmentação baseada em [propriedades de evento aninhadas]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects). No menu suspenso de comparação, selecione a comparação que corresponde ao tipo de dados da sua propriedade aninhada. Você pode usar a mesma sintaxe de propriedade de evento aninhada para adicionar propriedades aninhadas para qualquer evento recomendado de eCommerce que contenha propriedades aninhadas.

Para informações sobre as diferentes propriedades aninhadas disponíveis, consulte [Tipos de eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events). Para gerar o esquema necessário para o nome da propriedade da sua extensão de Segment, siga as etapas em [Objetos aninhados em eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

![Segmentação baseada em propriedades de evento aninhadas.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

##### Janela de retrospectiva e pontos de dados {#lookback-window-and-data-points}

As extensões de Segment dependem do armazenamento de longo prazo de propriedades de evento e não têm um limite de armazenamento de propriedades com carimbo de data/hora. Você pode consultar propriedades de eventos rastreadas nos últimos dois anos. Usar propriedades de evento dentro de extensões de Segment não afeta o uso de pontos de dados.

{% alert note %}
Você não precisa de extensões de Segment para usar propriedades de evento ou atributos personalizados aninhados no seu segmento. As extensões de Segment apenas ampliam a janela histórica usada para criar um segmento padrão. Você pode criar um [segmento]({{site.baseurl}}/user_guide/audience/segments) padrão em tempo real que use propriedades de evento dos últimos 30 dias ou que use atributos personalizados aninhados. Da mesma forma, você pode [agendar sua mensagem]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para disparar em tempo real com base em uma propriedade de evento — sem necessidade de extensão de Segment.
{% endalert %}

### Etapa 4: Defina as configurações de atualização (opcional) {#step-4-designate-refresh-settings-optional}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

### Etapa 5: Salve sua extensão de Segment {#step-5-save-your-segment-extension}

Após selecionar **Save**, sua extensão de Segment começa a ser processada. O tempo necessário para gerar sua extensão de Segment depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias está retrocedendo no histórico.

Enquanto sua extensão de Segment está sendo processada, você verá uma pequena animação ao lado do nome da extensão de Segment e **Processing** na coluna **Status** na lista de extensões de Segment. Note que você não pode editar uma extensão de Segment enquanto ela está sendo processada.

![Página "Segment Extensions" com duas extensões ativas.]({% image_buster /assets/img/segment/segment_extension5.png %})

Quando uma extensão de Segment está sendo processada, a Braze continuará usando a versão histórica do segmento padrão anterior ao início do processamento para fins de segmentação de público. O processamento ocorre cada vez que um salvamento ou atualização é realizado, e envolve consultar e atualizar perfis de usuários — em outras palavras, a composição do seu segmento padrão não é atualizada instantaneamente. Isso significa que, a menos que a ação de um usuário seja realizada antes do início do processamento da atualização, não podemos garantir que o usuário será incluído na extensão de Segment quando aquela atualização específica for concluída. Por outro lado, usuários que estavam na extensão de Segment antes da atualização e que não atendem mais aos critérios continuarão fazendo parte do seu segmento padrão até que o processo de atualização seja concluído e as alterações sejam aplicadas.

#### Status das extensões de Segment {#segment-extension-statuses}

Na página **Segment Extensions**, cada extensão exibe um **Status** e um carimbo de data/hora **Last Processed**. Após salvar ou atualizar uma extensão, use essas colunas para confirmar se o processamento foi concluído com sucesso.

| Status | Descrição |
|---|---|
| Active | A extensão foi processada com sucesso e está disponível para segmentação. **Last Processed** mostra quando a atualização mais recente foi concluída. |
| Draft | A extensão foi salva, mas ainda não foi ativada. |
| Archived | A extensão está arquivada e indisponível para segmentação. |
| Refresh disabled | As atualizações recorrentes de público estão desativadas. |
| Processing | A Braze está processando um salvamento ou atualização. A coluna **Status** mostra **Processing**, uma pequena animação aparece ao lado do nome da extensão, e você não pode editar a extensão até que o processamento seja concluído. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status das extensões de Segment" }

Quando o processamento não é concluído com sucesso, um ícone de erro aparece ao lado do nome da extensão, mesmo que a coluna **Status** ainda mostre **Active**. Passe o cursor sobre o ícone para ver o motivo da falha. Se você receber uma falha, mas acreditar que a extensão deveria ter sido processada, tente atualizar a extensão primeiro — o status pode estar desatualizado.

### Etapa 6: Use sua extensão em um segmento {#step-6-use-your-extension-in-a-segment}

Após criar uma extensão de Segment, você pode usá-la como filtro ao criar um segmento ou definir um público para uma Campaign ou Canvas. Comece escolhendo **Braze Segment Extension** na lista de filtros na seção **User Attributes**.

![Seção "Filters" com um menu suspenso de filtro mostrando "Braze Segment Extensions".]({% image_buster /assets/img/segment/segment_extension7.png %})

Na lista de filtros de Braze Segment Extension, escolha a extensão de Segment que deseja incluir ou excluir neste segmento.

![Um filtro "Braze Segment Extensions" que inclui um segmento "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension6.png %})

Para visualizar os critérios da extensão de Segment, selecione **View Extension Details** para exibir os detalhes em uma nova janela.

![Extensão para "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Agora você pode prosseguir normalmente com a [criação do seu segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Perguntas frequentes {#frequently-asked-questions}

### Posso criar uma extensão de Segment que usa vários eventos personalizados? {#can-i-create-a-segment-extension-that-uses-multiple-custom-events}

Sim. Você pode adicionar vários eventos ou referenciar várias tabelas do Snowflake ao usar [extensões de Segment SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

Ao usar extensões de Segment do tipo **Extensão simples**, você pode selecionar um evento personalizado, um evento de compra ou uma interação de canal. No entanto, é possível combinar várias extensões de Segment com AND ou OR ao criar o Segment padrão.

### Posso arquivar extensões de Segment se elas existirem em uma Campaign ativa? {#can-i-archive-segment-extensions-if-they-exist-in-an-active-campaign}

Não. Antes de arquivar uma extensão de Segment, você precisa removê-la de todos os envios de mensagens ativos.

### Posso usar arrays em extensões de Segment? {#can-i-use-arrays-in-segment-extensions}

Sim. Para usar arrays, adicione colchetes (`[]`) ao nome da sua propriedade. Se a sua propriedade for `location_code`, você digitaria `location_code[]`.

A Braze usa `[]` para percorrer arrays e verificar se algum item no array percorrido corresponde à propriedade do evento. Por exemplo, você poderia criar uma extensão de Segment de usuários que correspondem a pelo menos um valor de uma propriedade de array.

### Como a Braze calcula o período de tempo para um período relativo de "últimos __ dias"? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-__-days}

Quando as extensões de Segment calculam o período relativo ("últimos X dias"), o horário de início é definido como meia-noite UTC. Por exemplo, para uma extensão de Segment que é atualizada em 16/09/2024 às 21:00 UTC e especifica 10 dias, o horário de início é definido como 06/09/2024 às 00:00 UTC, e não 06/09/2024 às 21:00 UTC.

No entanto, você pode especificar os fusos horários usando Segments SQL para identificar usuários que realizaram o evento personalizado 10 dias atrás com base na meia-noite no horário da empresa, ou usuários que realizaram o evento 10 dias atrás com base no horário atual.