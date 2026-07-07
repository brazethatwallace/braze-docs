---
nav_title: Filtros calculados
article_title: Filtros calculados
page_order: 5.5
page_type: reference
description: "Este artigo de referência aborda como os filtros calculados funcionam, como eles se comparam às Extensões de segmento SQL e como criar e gerenciar filtros calculados."
tool: Segments
---

# Filtros calculados {#calculated-filters}

> Os filtros calculados permitem criar segmentos muito precisos ao longo de um período estendido do histórico de um usuário. Por exemplo, use filtros calculados para direcionar usuários que compraram um produto específico nos últimos 16 meses ou que gastaram um determinado valor com o seu serviço. Refine esse público usando propriedades de eventos para tornar o direcionamento ainda mais granular.

{% alert important %}
Os filtros calculados estão atualmente em acesso antecipado. Se você tem interesse em participar do acesso antecipado, entre em contato com o seu gerente de sucesso do cliente.
{% endalert %}

## Como funciona {#how-it-works}

Os segmentos da Braze oferecem ferramentas poderosas de direcionamento para criar grupos dinâmicos de usuários. Para a maioria dos casos de uso, isso é suficiente para alcançar seu público de forma eficaz. Os filtros calculados são projetados para casos de uso avançados em que você precisa analisar comportamentos de até dois anos atrás ou aplicar lógica complexa — sem comprometer a retenção de dados ou o desempenho do sistema. Você pode usar dados do seu próprio [data warehouse]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) para refinar ainda mais o seu público.

Por exemplo, a segmentação padrão da Braze encontra usuários que atendem a critérios específicos que você define, como identificar um usuário que comprou recentemente um dos seus produtos. Os filtros calculados permitem ir mais fundo — como identificar usuários que compraram uma cor específica de um produto específico pelo menos duas vezes entre 18 e 24 meses atrás. Os filtros calculados são um aprimoramento, não um requisito. Se você precisa de filtros mais avançados ou de uma janela histórica mais longa, eles são uma ótima ferramenta para ajudar, mantendo o uso de dados otimizado.

## Filtros calculados e Extensões de segmento SQL {#calculated-filters-and-sql-segment-extensions}

As [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) e os filtros calculados ajudam a criar públicos com base em comportamentos de compra e eventos personalizados, mas usam ferramentas e fontes de dados diferentes. As Extensões de segmento SQL usam SQL que você escreve contra os dados do Snowflake conectado.

| Comportamento | Filtros calculados | Extensões de segmento SQL |
|---|---|---|
| Como você define o público | Escolha compras, eventos recomendados de eCommerce, interação com mensagens ou eventos personalizados, além de contagens, janelas de tempo e filtros de propriedade opcionais | Escreva SQL contra a sua conexão Snowflake; use modelos, atualização incremental ou atualização completa |
| Onde a lógica é executada | Os critérios e a atualização são gerenciados na Braze como filtros calculados | A consulta é executada no contexto do seu data warehouse de acordo com a configuração da sua extensão |
| Página de lista de filtros | Um tipo de filtro calculado; a coluna **Segments** mostra quantos segmentos usam cada filtro; os status **Processando** e **Falha no processamento** refletem o estado de geração | Inclui uma coluna **Tipo** e filtros que variam por tipo de extensão |
| Casos de uso típicos | Frequência de compra, gasto total, contagens de eventos personalizados e regras baseadas em propriedades na janela selecionada | Lógica baseada em data warehouse, junções entre tabelas e janelas históricas ou agregações além do formulário de filtro calculado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Filtros calculados e Extensões de segmento SQL" }

### Quando usar filtros calculados {#when-to-use-calculated-filters}

Use filtros calculados quando as regras guiadas pelo dashboard para compras, eCommerce, interação com mensagens e eventos personalizados forem suficientes e você não precisar de SQL arbitrário em tabelas do data warehouse.

### Quando usar outros tipos de extensão de segmento {#when-to-use-other-segment-extension-types}

Use [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) quando precisar de SQL completo, dados baseados em Snowflake, modelos ou modos de atualização projetados para consultas grandes ou complexas no data warehouse. Use [Extensões de segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) quando precisar de SQL que consulte diretamente o seu data warehouse usando dados de conexões de [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

### Use filtros calculados e Extensões de segmento juntos {#use-calculated-filters-and-segment-extensions-together}

Um segmento pode referenciar um filtro calculado junto com uma Extensão de segmento SQL ou CDI — por exemplo, uma coorte definida no data warehouse a partir de uma extensão, combinada com regras de compra ou eventos personalizados que você mantém no criador de filtros calculados.

## Criar um filtro calculado {#create-a-calculated-filter}

Para criar um filtro calculado, defina critérios com base no comportamento do usuário, depois salve e ative o filtro antes de usá-lo em um segmento.

### Etapa 1: Configurar os detalhes {#step-1-set-up-details}

1. Acesse **Público** > **Filtros calculados**.
2. Selecione **Criar filtro calculado**.
3. Dê um nome ao seu filtro calculado descrevendo os usuários que você pretende direcionar. Um nome descritivo facilita encontrar o filtro quando você adicioná-lo a um segmento.
4. (Opcional) Adicione [tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) para organizar os filtros calculados no seu espaço de trabalho.

Você também pode selecionar **Ativar atualização recorrente de público** para atualizar o filtro em uma programação recorrente. Se você não ativar essa configuração, o filtro calculado não será atualizado a menos que você atualize o filtro ou selecione **Atualizar público**.

### Etapa 2: Escolher seus critérios {#step-2-choose-your-criteria}

Escolha um critério de compra, eCommerce, evento personalizado ou interação com mensagem para direcionamento. Depois de selecionar um tipo de evento, escolha o evento específico, quantas vezes o usuário deve tê-lo concluído (mais que, menos que ou igual a) e o período de tempo.

Ao escolher o período de tempo, você pode especificar um intervalo de datas relativo (os últimos X dias), uma data de início, uma data de término ou um intervalo de datas exato.

![Critérios de filtro calculado para usuários que realizaram um evento personalizado mais de zero vezes no intervalo de datas de 21 de junho de 2026 a 27 de junho de 2026.]({% image_buster /assets/img/segment/calculated_filter_example.png %})

#### Segmentação por propriedade de evento {#event-property-segmentation}

Para aumentar a precisão do direcionamento, selecione **Adicionar filtros de propriedade**. Isso permite filtrar por propriedades da sua compra, evento de eCommerce ou evento personalizado. A Braze oferece suporte à segmentação por propriedade de evento com base em objetos de string, numéricos, booleanos e de tempo.

Para propriedades de string, insira vários valores de uma vez — por exemplo, direcionando usuários com status igual a ouro, prata ou bronze. Para eventos recomendados de eCommerce, o menu suspenso de propriedades é preenchido com as propriedades disponíveis para aquele evento.

{% alert note %}
Você não precisa de filtros calculados para usar propriedades de evento no seu segmento. Os filtros calculados apenas estendem a janela histórica usada para criar um segmento padrão. Você pode criar um [segmento]({{site.baseurl}}/user_guide/audience/segments) padrão em tempo real que usa propriedades de evento dos últimos 30 dias. Da mesma forma, você pode [programar sua mensagem]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) para ser disparada em tempo real com base em uma propriedade de evento — sem necessidade de filtro calculado.
{% endalert %}

### Etapa 3: Salvar e ativar seu filtro {#step-3-save-and-activate-your-filter}

Selecione **Salvar** para salvar o seu filtro calculado. Você pode salvar um filtro sem ativá-lo, mas deve ativar um filtro antes que ele apareça como opção ao criar um segmento.

Depois de ativar um filtro calculado, a Braze o avalia em tempo real quando um segmento, uma Campaign ou um Canvas que o referencia é avaliado.

## Usar um filtro calculado em um segmento {#use-a-calculated-filter-in-a-segment}

Depois de criar e ativar um filtro calculado, adicione-o ao criar um segmento ou definir um público para uma Campaign ou Canvas.

1. No criador de segmentos, abra a lista de filtros.
2. Em **Outros filtros**, selecione **Filtro calculado existente**.
3. Selecione o filtro calculado para incluir na definição do segmento.

Depois de adicionar o filtro, selecione o ícone ao lado do menu suspenso do filtro para visualizar os detalhes do filtro e confirmar os critérios aplicados ao seu público.

![Filtro calculado em um criador de segmentos com um ícone para visualizar mais detalhes.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

Para saber mais sobre como criar segmentos, consulte [Criar um segmento]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).

## Gerenciar filtros calculados {#manage-calculated-filters}

Acesse **Público** > **Filtros calculados** para visualizar, editar e gerenciar filtros calculados no seu espaço de trabalho.

A página **Filtros calculados** lista todos os filtros calculados no seu espaço de trabalho. Você pode refinar a lista com os controles disponíveis. Como existe apenas um tipo de filtro calculado, não há opção para filtrar por tipo, e a tabela não inclui uma coluna **Tipo**. Use a coluna **Segments** para ver quantos segmentos usam cada filtro calculado.

### Rótulos de status {#status-labels}

Cada filtro calculado exibe um dos seguintes status. **Processando** e **Falha no processamento** aparecem quando a geração de membros está em andamento ou não foi concluída com sucesso.

| Status | Descrição |
|---|---|
| Ativo | O filtro está ativado e disponível para uso em segmentos. |
| Rascunho | O filtro está salvo, mas não ativado. |
| Arquivado | O filtro está arquivado. |
| Processando | A Braze está processando uma atualização do filtro. |
| Falha no processamento | A tentativa de processamento mais recente não foi concluída com sucesso. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Rótulos de status" }

### Editar e gerenciar filtros individuais {#edit-and-manage-individual-filters}

Abra o menu de linha de um filtro calculado para editar, arquivar, atualizar o público ou ver como ele está sendo usado no envio de mensagens. Você não pode editar um filtro calculado enquanto ele está sendo processado.

{% alert note %}
Seu espaço de trabalho pode ter até 500 filtros calculados ativados por vez. Entre em contato com o gerente de conta da Braze se precisar aumentar esse limite.
{% endalert %}

#### Salvar versus ativar {#save-versus-activate}

Você pode salvar um filtro calculado sem ativá-lo. Filtros inativos permanecem no seu espaço de trabalho, mas não podem ser adicionados a segmentos até que você os ative. Selecione **Ativar filtro** para usar o filtro na segmentação.

## Perguntas frequentes {#frequently-asked-questions}

### Posso criar um filtro calculado que usa vários eventos personalizados? {#can-i-create-a-calculated-filter-that-uses-multiple-custom-events}

Ao usar filtros calculados, você pode selecionar um evento personalizado, um evento de compra, um evento de eCommerce ou uma interação de canal. No entanto, você pode combinar vários filtros calculados com AND ou OR ao criar o segmento.

Você pode adicionar vários eventos ou referenciar várias tabelas do Snowflake ao usar [Extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

### Posso arquivar filtros calculados se eles existem em uma Campaign ativa? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

Não. Antes de arquivar um filtro calculado, você precisa removê-lo de todo o envio de mensagens ativo.

### Posso usar arrays em filtros calculados? {#can-i-use-arrays-in-calculated-filters}

Sim. Para usar arrays, adicione colchetes (`[]`) ao nome da sua propriedade. Se a sua propriedade for `location_code`, você digitaria `location_code[]`.

A Braze usa `[]` para percorrer arrays e verificar se algum item no array percorrido corresponde à propriedade do evento. Por exemplo, você poderia criar um filtro calculado de usuários que correspondem a pelo menos um valor de uma propriedade de array.

### Como a Braze calcula o período de tempo para um período relativo de "últimos X dias"? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

Quando os filtros calculados calculam o período de tempo relativo ("últimos X dias"), o horário de início é definido como meia-noite UTC. Por exemplo, para um filtro calculado que é atualizado em 16/09/2024 às 21:00 UTC e especifica 10 dias, o horário de início é definido como 06/09/2024 às 00:00 UTC, e não 06/09/2024 às 21:00 UTC.

No entanto, você pode especificar os fusos horários usando segmentos SQL para identificar usuários que realizaram o evento personalizado 10 dias atrás com base na meia-noite no horário da empresa, ou usuários que realizaram o evento 10 dias atrás com base no horário atual.