---
nav_title: Filtros calculados
article_title: Filtros calculados
page_order: 5.5
page_type: reference
description: "Este artigo de referência aborda como os filtros calculados funcionam, como eles se comparam às extensões de Segment SQL e como criar e gerenciar filtros calculados."
tool: Segments
---

# Filtros calculados {#calculated-filters}

> Os filtros calculados permitem criar segmentos muito precisos ao longo de um período estendido do histórico de um usuário. Por exemplo, use filtros calculados para direcionar usuários que compraram um produto específico nos últimos 16 meses ou que gastaram um determinado valor com o seu serviço. Refine esse público usando propriedades de eventos para tornar o direcionamento ainda mais granular.

{% alert important %}
Os filtros calculados estão atualmente em acesso antecipado. Se você tem interesse em participar do acesso antecipado, entre em contato com o seu gerente de conta da Braze.
{% endalert %}

## Como funciona {#how-it-works}

Os Segments da Braze oferecem ferramentas de direcionamento poderosas para criar grupos dinâmicos de usuários. Para a maioria dos casos de uso, isso é suficiente para alcançar seu público de forma eficaz. Os filtros calculados são projetados para casos de uso avançados em que você precisa analisar comportamentos de até dois anos atrás ou aplicar lógica complexa, sem comprometer a retenção de dados ou o desempenho do sistema. Use **filtros de atividade do usuário** para critérios de compra e eventos de eCommerce, ou **filtros de objetos de dados** para direcionamento por conta e objetos personalizados.

Por exemplo, a segmentação padrão da Braze encontra usuários que atendem a critérios específicos definidos por você, como identificar um usuário que comprou recentemente um de seus produtos. Os filtros calculados permitem ir mais fundo, como identificar usuários que compraram uma cor específica de um produto específico pelo menos duas vezes entre 18 e 24 meses atrás. Os filtros calculados são um aprimoramento, não um requisito. Se você precisa de filtros mais avançados ou de uma janela histórica mais longa, eles são uma ótima ferramenta para ajudar, mantendo o uso de dados otimizado.

## Filtros calculados e extensões de segmento SQL {#calculated-filters-and-sql-segment-extensions}

[Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) e filtros calculados ajudam a criar públicos com base no comportamento de compra, mas usam ferramentas e fontes de dados diferentes. As extensões de segmento SQL usam SQL que você escreve com base nos dados do Snowflake conectado.

| Comportamento | Filtros calculados | Extensões de segmento SQL |
|---|---|---|
| Como você define o público | Escolha compras ou eventos recomendados de eCommerce, além de contagens, janelas de tempo e filtros opcionais de propriedades | Escreva SQL usando sua conexão com o Snowflake; use modelos, atualização incremental ou atualização completa |
| Onde a lógica é executada | Os critérios e a atualização são gerenciados na Braze como filtros calculados | A consulta é executada no contexto do seu data warehouse de acordo com a configuração da sua extensão |
| Página de lista de filtros | Uma lista compartilhada para filtros de atividade do usuário e objetos de dados. A coluna **Segments** mostra quantos segmentos usam cada filtro, e os status de processamento refletem o estado de geração | Inclui uma coluna **Type** e filtros que variam de acordo com o tipo de extensão |
| Casos de uso típicos | Frequência de compra, gasto total e regras baseadas em propriedades na janela selecionada | Lógica baseada no data warehouse, junções entre tabelas e janelas históricas ou agregações que vão além do formulário de filtros calculados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtros calculados e extensões de segmento SQL" }

### Quando usar filtros calculados {#when-to-use-calculated-filters}

Use filtros calculados quando as regras guiadas pelo dashboard para atividade do usuário ou objetos de dados forem suficientes e você não precisar de SQL arbitrário em tabelas do data warehouse.

### Quando usar outros tipos de extensão de segmento {#when-to-use-other-segment-extension-types}

Use [extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) quando precisar de SQL completo, dados baseados no Snowflake, modelos ou modos de atualização projetados para consultas grandes ou complexas no data warehouse. Use [extensões de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) quando precisar de SQL que consulte diretamente seu data warehouse usando dados de conexões de [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

### Use filtros calculados e extensões de segmento juntos {#use-calculated-filters-and-segment-extensions-together}

Um segmento pode referenciar um filtro calculado junto com uma extensão de segmento SQL ou CDI — por exemplo, uma coorte definida no data warehouse a partir de uma extensão, combinada com regras de compra que você mantém no criador de filtros calculados.

## Criar um filtro calculado {#create-a-calculated-filter}

Para criar um filtro calculado, escolha um tipo de filtro se solicitado, defina seus critérios e salve e ative o filtro antes de usá-lo em um Segment.

### Etapa 1: Configurar detalhes {#step-1-set-up-details}

1. Acesse **Público** > **Filtros calculados**.
2. Selecione **Criar filtro**.
3. Se o seu espaço de trabalho tiver [Contas]({{site.baseurl}}/user_guide/data/activation/accounts) ativadas, selecione um tipo de filtro:
   - **Filtros de atividade do usuário:** Ações e comportamentos dos usuários.
   - **Filtros de objetos de dados:** Atributos e relacionamentos para objetos de dados.
4. Insira um nome que descreva o público que você pretende direcionar. Um nome descritivo facilita encontrar o filtro ao adicioná-lo a um Segment.
5. (Opcional) Adicione [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) para organizar filtros calculados no seu espaço de trabalho.

Para **Filtros de atividade do usuário**, selecione **Ativar atualização recorrente do público** para atualizar o filtro em um cronograma recorrente. Se você não ativar essa configuração, o filtro não será atualizado a menos que você o atualize ou selecione **Atualizar público**. Os **Filtros de objetos de dados** são atualizados a cada hora.

### Etapa 2: Escolher seus critérios {#step-2-choose-your-criteria}

{% tabs %}
{% tab Filtros de objetos de dados %}

Se você selecionou **Filtros de objetos de dados**, escolha um objeto de dados e, em seguida, adicione condições de atributo, relacionamento ou grupo de filtros. Para direcionamento baseado em conta, consulte [Objetos de conta]({{site.baseurl}}/user_guide/data/activation/accounts).

{% endtab %}
{% tab Filtros de atividade do usuário %}

Se **Criar filtro** abrir diretamente o construtor de atividade do usuário, ou se você selecionar **Filtros de atividade do usuário**, escolha uma das seguintes opções de **Critério** para direcionamento:

- **Fez uma compra**
- **Realizou um evento de eCommerce**

Após selecionar um tipo de evento, escolha o evento específico, quantas vezes o usuário deve tê-lo concluído (mais que, menos que ou igual a) e o período de tempo.

{% alert note %}
Os filtros **mais que** e **menos que** são exclusivos — eles não incluem o número que você especifica. Por exemplo, um filtro para **mais que 4 vezes e menos que 16 vezes** inclui usuários que tiveram 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ou 15 vezes.
{% endalert %}

Ao escolher o período de tempo, você pode especificar um intervalo de datas relativo (os últimos X dias), uma data de início, uma data de término ou um intervalo de datas exato. Para intervalos relativos, insira de **1** a **730** dias (dois anos). Para intervalos de datas absolutos, a data de início deve estar dentro dos últimos dois anos e a data de término deve estar dentro dos próximos dois anos.

#### Segmentação por propriedade de evento {#event-property-segmentation}

Para aumentar a precisão do direcionamento, selecione **Adicionar filtros de propriedade de evento**. Isso permite filtrar com base nas propriedades da sua compra ou evento de eCommerce. A Braze oferece suporte à segmentação por propriedade de evento com base em objetos de string, numéricos, booleanos e de tempo.

Para propriedades de string, insira vários valores de uma vez — por exemplo, direcionar usuários com status igual a ouro, prata ou bronze. Para eventos recomendados de eCommerce, o menu suspenso de propriedades é preenchido com as propriedades disponíveis para aquele evento.

{% alert note %}
Você não precisa de filtros calculados para usar propriedades de evento no seu Segment. Os filtros calculados apenas estendem a janela histórica usada para criar um Segment padrão. Você pode criar um [Segment]({{site.baseurl}}/user_guide/audience/segments) padrão em tempo real que usa propriedades de evento dos últimos 30 dias. Da mesma forma, você pode [agendar sua mensagem]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para disparar em tempo real com base em uma propriedade de evento — sem necessidade de filtro calculado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 3: Salvar e ativar seu filtro {#step-3-save-and-activate-your-filter}

Selecione **Salvar como rascunho** para salvar um novo filtro calculado sem ativá-lo. Para um filtro ativado, selecione **Salvar alterações** para salvar suas atualizações. Você deve selecionar **Ativar filtro** antes que o filtro esteja disponível no criador de segmentos.

Depois que você ativar um filtro calculado, a Braze começará a calcular o público. Quando o processamento estiver concluído, você poderá selecionar o filtro ao criar um público.

## Usar um filtro calculado em um Segment {#use-a-calculated-filter-in-a-segment}

Após criar e ativar um filtro calculado, adicione-o ao criar um Segment ou definir um público para uma Campaign ou Canvas.

1. No criador de segmentos, abra a lista de filtros.
2. Em **Outros filtros**, selecione **Filtro calculado existente**.
3. Selecione o filtro calculado a ser incluído na definição do Segment.

Após adicionar o filtro, selecione o ícone ao lado do menu suspenso do filtro para visualizar os detalhes do filtro e confirmar os critérios aplicados ao seu público.

![Filtro calculado em um criador de segmentos com um ícone para visualizar mais detalhes.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

Para saber mais sobre a criação de segmentos, consulte [Criar um Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Gerenciar filtros calculados {#manage-calculated-filters}

Acesse **Audience** > **Calculated Filters** para visualizar, editar e gerenciar filtros calculados no seu espaço de trabalho.

A página **Calculated Filters** lista filtros de atividade do usuário e de objetos de dados juntos. Você pode refinar a lista com os controles disponíveis, mas a página não inclui um controle de filtro por tipo nem uma coluna **Type**. Use a coluna **Segments** para ver quantos Segments usam cada filtro calculado.

### Rótulos de status {#status-labels}

Cada filtro calculado exibe um dos status a seguir. **Processing** e **Processing failed** aparecem quando a geração de membros está em andamento ou não foi concluída com sucesso.

| Status | Descrição |
|---|---|
| Active | O filtro está ativado e disponível para uso em Segments. |
| Draft | O filtro está salvo, mas não ativado. |
| Archived | O filtro está arquivado. |
| Refresh disabled | As atualizações recorrentes de público estão desativadas. A Braze pode definir esse status automaticamente quando um filtro com atualização agendada não é utilizado. |
| Processing | A Braze está processando uma atualização do filtro. |
| Processing failed | A tentativa de processamento mais recente não foi concluída com sucesso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rótulos de status" }

### Editar e gerenciar filtros individuais {#edit-and-manage-individual-filters}

Abra o menu de linha de um filtro calculado para executar uma ação. As ações disponíveis dependem do status do filtro.

Para filtros que não estão arquivados, o menu de linha inclui **Edit**, **Messaging use**, **Archive** e **Update audience**. **Update audience** está disponível para filtros ativos que não estão em processamento. Você pode editar um filtro calculado enquanto ele está sendo processado, mas não pode salvar suas alterações até que o processamento seja concluído.

{% alert note %}
Seu espaço de trabalho pode ter até 100 filtros calculados ativos por vez. Entre em contato com o gerente de conta da Braze se precisar aumentar esse limite.
{% endalert %}

#### Desarquivar {#unarchive}

Você pode desarquivar um filtro de qualquer uma das seguintes formas:

- Selecione **Unarchive** no menu de linha do filtro.
- Selecione um ou mais filtros arquivados e depois selecione **Unarchive**.
- Abra um filtro calculado arquivado e selecione **Unarchive** na página dele.

Quando você desarquiva um filtro, o status dele retorna ao que era antes do arquivamento:

- Um rascunho retorna para **Draft**.
- Um filtro ativado retorna para **Active**, conta para o limite de filtros ativos, e a Braze inicia uma atualização de público.

Aguarde até que o processamento termine antes de desarquivar um filtro que exibe **Processing**. Se você atingiu o limite de filtros ativos, arquive um filtro ativo antes de desarquivar outro filtro ativo.

#### Salvar versus ativar {#save-versus-activate}

Você pode salvar um filtro calculado sem ativá-lo. Filtros inativos permanecem no seu espaço de trabalho, mas não podem ser adicionados a Segments até que sejam ativados. Selecione **Activate filter** para usar o filtro na segmentação.

## Perguntas frequentes {#frequently-asked-questions}

### Posso arquivar um filtro calculado se ele estiver em uso? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

Não. Antes de arquivar um filtro calculado, remova-o de todos os Campaigns, Canvas e Segments que o utilizam. Também não é possível arquivar um filtro enquanto o status dele estiver como **Processing**; aguarde até que o processamento seja concluído.

### Posso usar arrays em filtros calculados? {#can-i-use-arrays-in-calculated-filters}

Sim. Para usar arrays, adicione colchetes (`[]`) ao nome da sua propriedade. Se a sua propriedade for `location_code`, você digitaria `location_code[]`.

A Braze usa `[]` para percorrer arrays e verificar se algum item no array percorrido corresponde à propriedade do evento. Por exemplo, você poderia criar um filtro calculado de usuários que correspondem a pelo menos um valor de uma propriedade de array.

### Como a Braze calcula o período de tempo para um período relativo de "últimos X dias"? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Quando os filtros calculados calculam o período de tempo relativo ("últimos X dias"), o horário de início é definido como meia-noite UTC. Por exemplo, para um filtro calculado que é atualizado em 2024-09-16 21:00 UTC e especifica 10 dias, o horário de início é definido como 2024-09-06 00:00 UTC, e não 2024-09-06 21:00 UTC. Filtros calculados sempre usam UTC para janelas de tempo; o fuso horário do seu espaço de trabalho não se aplica.

No entanto, você pode especificar fusos horários usando [extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) para identificar usuários que realizaram um evento 10 dias atrás com base na meia-noite no horário da empresa, ou usuários que realizaram o evento 10 dias atrás com base no horário atual.