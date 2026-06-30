---
nav_title: Extensões de segmento
article_title: Extensões de segmento
page_order: 5
page_type: reference
description: "Este artigo prático vai orientar você sobre como configurar e usar uma extensão de segmento para aprimorar suas capacidades de segmentação."
tool: Segments
---

# Extensões de segmento {#segment-extensions}

> As extensões de segmento permitem que você crie segmentos muito precisos ao longo de um período estendido do histórico de um usuário. Por exemplo, usando extensões de segmento, você pode direcionar usuários que compraram um produto específico nos últimos dezesseis meses ou que gastaram uma determinada quantia com o seu serviço. Refine esse público usando propriedades de eventos para tornar o direcionamento ainda mais granular.

A segmentação da Braze permite que você direcione usuários com base em eventos personalizados ou comportamento de compra. As extensões de segmento ampliam essa capacidade, permitindo que você utilize dados históricos salvos no perfil do usuário. Com as extensões de segmento, você pode identificar e alcançar usuários que realizaram qualquer evento personalizado ou evento de compra qualquer número de vezes nos últimos dois anos (730 dias).

## Por que usar extensões de segmento? {#why-use-segment-extensions}

Os Segments da Braze oferecem ferramentas poderosas de direcionamento para criar grupos dinâmicos de usuários. Para a maioria dos casos de uso, isso é suficiente para alcançar seu público de forma eficaz. As extensões de segmento são projetadas para casos de uso avançados em que você precisa analisar comportamentos de até dois anos atrás ou aplicar lógica complexa — sem comprometer a retenção de dados ou o desempenho do sistema. Você pode usar consultas [SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) (extensões de segmento SQL) ou dados do seu próprio [data warehouse]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) para refinar ainda mais o seu público.

Por exemplo, a segmentação padrão da Braze encontra usuários que atendem a critérios específicos que você define, como identificar um usuário que comprou recentemente um dos seus produtos. As extensões de segmento permitem ir mais fundo — como identificar usuários que compraram uma cor específica de um produto específico pelo menos duas vezes entre 18 e 24 meses atrás. As extensões de segmento são um aprimoramento, não um requisito. Se você precisa de filtros mais avançados ou uma janela de retrospectiva mais longa, elas são uma ótima ferramenta para ajudar, mantendo o uso de dados otimizado.

{% alert note %}
Há uma alocação padrão de 25 extensões de segmento ativas por espaço de trabalho em um determinado momento. Se você precisar aumentar esse limite, entre em contato com seu gerente de sucesso do cliente da Braze para discutir seu caso de uso.
{% endalert %}

## Criando uma extensão de segmento {#creating-a-segment-extension}

Para criar uma extensão de segmento, você criará um filtro para refinar um segmento dos seus usuários com base em propriedades de eventos personalizados. Ao criar uma extensão de segmento, você escolherá se o segmento será estático ou atualizado dinamicamente em um intervalo definido.

### Etapa 1: Navegue até Extensões de segmento {#step-1-navigate-to-segment-extensions}

Acesse **Audience** > **Segment Extensions**.

Na tabela de extensões de segmento, selecione **Create New Extension** e depois selecione sua experiência de criação de extensão de segmento:

- **Simple extension:** Crie uma extensão de segmento focada em um único evento usando um formulário guiado. Ideal para quando você não quer usar SQL.
- **Start with a template:** Crie um segmento SQL com um modelo personalizável usando dados do Snowflake.
- **Incremental refresh:** Escreva um segmento SQL com Snowflake que atualiza automaticamente os últimos 2 dias de dados ou atualize manualmente conforme necessário. Ideal para equilibrar precisão e eficiência de custos.
- **Full refresh:** Escreva um segmento SQL com dados do Snowflake ou qualquer [fonte conectada via CDI]({{site.baseurl}}/cdi_segment_extensions) que recalcula todo o público ao atualizar manualmente. Ideal para quando você precisa de uma visão completa e atualizada do seu público.

![Tabela com diferentes experiências de criação de extensão de segmento para selecionar.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

Se você selecionar uma experiência que usa SQL, consulte [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) para mais informações. Se você selecionar **Simple extension**, continue para a etapa 2.

#### Uso de créditos SQL {#sql-credit-usage}

Os seguintes tipos de extensão de segmento consomem créditos SQL:

- Extensões de segmento SQL (tanto atualização incremental quanto completa)
- Segments de catálogo
- Segments CDI
    - Os créditos são consumidos dentro do seu próprio data warehouse

### Etapa 2: Nomeie sua extensão de segmento {#step-2-name-your-segment-extension}

Nomeie sua extensão de segmento descrevendo o tipo de usuários que você pretende filtrar. Isso garantirá que essa extensão possa ser facilmente e corretamente encontrada ao aplicá-la como filtro no seu segmento.

![Extensão de segmento chamada "Online Shoppers Extension - 90 Days".]({% image_buster /assets/img/segment/segment_extension2.png %})

### Etapa 3: Escolha seus critérios {#step-3-choose-your-criteria}

Selecione entre critérios de compra, engajamento com mensagem, evento recomendado de eCommerce ou evento personalizado para direcionamento. Depois de selecionar os critérios de tipo de evento desejados, escolha qual item comprado, interação com mensagem, evento recomendado de eCommerce ou evento personalizado você gostaria de direcionar para sua lista de usuários. Em seguida, escolha quantas vezes (mais que, menos que ou igual a) o usuário precisaria ter realizado o evento, e o período — para extensões de segmento especificamente, você pode retroceder até os últimos 730 dias (2 anos).

A segmentação baseada em dados de eventos de mais de 730 dias pode ser feita usando outros filtros localizados em **Segments**. Ao escolher seu período, você pode especificar um intervalo de datas relativo para selecionar os últimos X dias, uma data de início, uma data de término ou um intervalo de datas exato (data A até data B).

![Critérios de segmentação para usuários que realizaram um evento personalizado mais de 2 vezes no intervalo de datas de 1º de março de 2025 a 31 de março de 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

Se você estiver criando uma extensão de segmento usando um evento recomendado de eCommerce, primeiro selecione **eCommerce Recommended Event** como seu critério e depois selecione um evento no menu suspenso.

![Um critério de evento recomendado de eCommerce com um menu suspenso de eventos recomendados disponíveis.]({% image_buster /assets/img/segment/ecommerce_recommended_event_criterion.png %})

#### Segmentação por propriedade de evento {#event-property-segmentation}

Para aumentar a precisão do direcionamento, marque a caixa de seleção **Add Property Filters**. Isso permitirá que você faça uma análise detalhada com base nas propriedades específicas da sua compra ou evento personalizado. Oferecemos suporte à segmentação por propriedade de evento com base em objetos de string, numéricos, booleanos e de data/hora.

Para propriedades de string, você pode inserir vários valores de uma vez. No exemplo abaixo, esse filtro procura usuários com um status igual a qualquer um dos seguintes: ouro, prata ou bronze.

![Segmentação baseada em propriedades de string.]({% image_buster /assets/img/segment/property5.png %})

![Segmentação baseada em propriedades numéricas.]({% image_buster /assets/img/segment/property2.png %})

![Segmentação baseada em propriedades booleanas.]({% image_buster /assets/img/segment/property3.png %})

![Segmentação baseada em objetos de data/hora.]({% image_buster /assets/img/segment/property4.png %})

Se você estiver usando eventos recomendados de eCommerce e adicionar uma propriedade de evento, o menu suspenso de propriedades será preenchido automaticamente com as propriedades disponíveis para aquele evento recomendado de eCommerce específico.

![Detalhes da extensão de segmento com um menu suspenso de propriedades disponíveis.]({% image_buster /assets/img/segment/ecommerce_recommended_event_properties.png %})

Também oferecemos suporte à segmentação baseada em [propriedades de eventos aninhadas]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects). No menu suspenso de comparação, selecione a comparação que corresponde ao tipo de dados da sua propriedade aninhada. Você pode usar a mesma sintaxe de propriedade de evento aninhada para adicionar propriedades aninhadas para qualquer evento recomendado de eCommerce que contenha propriedades aninhadas. Para informações sobre as diferentes propriedades aninhadas disponíveis, consulte [Tipos de eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#types-of-ecommerce-recommended-events). Para gerar o esquema necessário para o nome da propriedade da sua extensão de segmento, siga as etapas em [Objetos aninhados em eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

![Segmentação baseada em propriedades de eventos aninhadas.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

As extensões de segmento dependem do armazenamento de longo prazo de propriedades de eventos e não possuem um limite de armazenamento de propriedades com carimbo de data/hora. Você pode consultar propriedades de eventos rastreadas nos últimos dois anos. O uso de propriedades de eventos dentro de extensões de segmento não afeta o consumo de pontos de dados.

{% alert note %}
Você não precisa de extensões de segmento para usar propriedades de eventos ou atributos personalizados aninhados no seu segmento. As extensões de segmento apenas estendem a janela histórica usada para criar um segmento padrão. Você pode criar um [segmento]({{site.baseurl}}/user_guide/audience/segments) padrão em tempo real que usa propriedades de eventos dos últimos 30 dias ou que usa atributos personalizados aninhados. Da mesma forma, você pode [programar sua mensagem]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para ser disparada em tempo real com base em uma propriedade de evento — sem necessidade de extensão de segmento.
{% endalert %}

### Etapa 4: Defina as configurações de atualização (opcional) {#step-4-designate-refresh-settings-optional}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

### Etapa 5: Salve sua extensão de segmento {#step-5-save-your-segment-extension}

Depois de selecionar **Save**, sua extensão de segmento começará a ser processada. O tempo necessário para gerar sua extensão de segmento depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias você está consultando no histórico.

Enquanto sua extensão de segmento está sendo processada, você verá uma pequena animação ao lado do nome da extensão de segmento e a palavra "Processing" na coluna **Last Processed** na lista de extensões de segmento. Observe que você não poderá editar uma extensão de segmento enquanto ela estiver sendo processada.

![Página "Segment Extensions" com duas extensões ativas.]({% image_buster /assets/img/segment/segment_extension5.png %})

Quando uma extensão de segmento está sendo processada, a Braze continuará usando a versão histórica do segmento padrão de antes do início do processamento para fins de segmentação de público. O processamento ocorre cada vez que um salvamento ou atualização acontece e envolve consultar e atualizar perfis de usuários — em outras palavras, a composição do seu segmento padrão não é atualizada instantaneamente. Isso significa que, a menos que a ação de um usuário seja realizada antes do início do processamento da atualização, não podemos garantir que o usuário será incluído na extensão de segmento quando aquela atualização específica for concluída. Da mesma forma, usuários que estavam na extensão de segmento antes da atualização e que não atendem mais aos critérios continuarão correspondendo ao seu segmento padrão até que o processo de atualização seja concluído e as atualizações sejam aplicadas.

### Etapa 6: Use sua extensão em um segmento {#step-6-use-your-extension-in-a-segment}

Depois de criar uma extensão de segmento, você pode usá-la como filtro ao criar um segmento ou definir um público para uma Campaign ou Canvas. Comece escolhendo **Braze Segment Extension** na lista de filtros na seção **User Attributes**.

![Seção "Filters" com um menu suspenso de filtros mostrando "Braze Segment Extensions".]({% image_buster /assets/img/segment/segment_extension7.png %})

Na lista de filtros de Braze Segment Extension, escolha a extensão de segmento que você deseja incluir ou excluir neste segmento.

![Um filtro "Braze Segment Extensions" que inclui um segmento "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension6.png %})

Para visualizar os critérios da extensão de segmento, selecione **View Extension Details** para exibir os detalhes em uma nova janela.

![Extensão para "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Agora você pode prosseguir normalmente com a [criação do seu segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Perguntas frequentes {#frequently-asked-questions}

### Posso criar uma extensão de segmento que usa vários eventos personalizados? {#can-i-create-a-segment-extension-that-uses-multiple-custom-events}

Sim. Você pode adicionar vários eventos ou referenciar várias tabelas do Snowflake ao usar [extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

Ao usar extensões de segmento de **Simple extension**, você pode selecionar um evento personalizado, um evento de compra ou uma interação de canal. No entanto, você pode combinar várias extensões de segmento com AND ou OR ao criar o segmento padrão.

### Posso arquivar extensões de segmento se elas existem em uma Campaign ativa? {#can-i-archive-segment-extensions-if-they-exist-in-an-active-campaign}

Não. Antes de arquivar uma extensão de segmento, você precisa removê-la de todos os envios de mensagens ativos.

### Posso usar arrays em extensões de segmento? {#can-i-use-arrays-in-segment-extensions}

Sim. Para usar arrays, adicione colchetes (`[]`) ao nome da sua propriedade. Se sua propriedade for `location_code`, você digitaria `location_code[]`.

A Braze usa `[]` para percorrer arrays e verificar se algum item no array percorrido corresponde à propriedade do evento. Por exemplo, você poderia criar uma extensão de segmento de usuários que correspondem a pelo menos um valor de uma propriedade de array.

### Como a Braze calcula o período para um período relativo de "últimos __ dias"? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-__-days}

Quando as extensões de segmento calculam o período relativo ("últimos X dias"), o horário de início é definido como meia-noite UTC. Por exemplo, para uma extensão de segmento que atualiza em 2024-09-16 21:00 UTC e especifica 10 dias, o horário de início é definido como 2024-09-06 00:00 UTC, não 2024-09-06 21:00 UTC.

No entanto, você pode especificar os fusos horários usando segmentos SQL para identificar usuários que realizaram o evento personalizado 10 dias atrás com base na meia-noite no horário da empresa, ou usuários que realizaram o evento 10 dias atrás com base no horário atual.