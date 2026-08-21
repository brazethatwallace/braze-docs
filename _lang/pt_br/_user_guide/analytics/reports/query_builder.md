---
nav_title: Criador de consultas
article_title: Criador de consultas
page_order: 4
description: "Este artigo de referência descreve como criar relatórios usando dados da Braze no Snowflake por meio do Criador de consultas."
tool: Reports
alias: /query_builder/
---

# Criador de consultas {#query-builder}

> O Criador de consultas gera relatórios usando dados da Braze no Snowflake. O Criador de consultas vem com [modelos de consulta]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) SQL pré-criados para você começar, ou você pode escrever suas próprias consultas SQL personalizadas para obter ainda mais insights.

Como o Criador de consultas permite acesso direto a alguns dados de cliente, você só pode acessá-lo se tiver a [permissão]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) "View PII".

## Tabelas de dados disponíveis {#available-data-tables}

O Criador de consultas usa as mesmas tabelas SQL do Snowflake que as [extensões de segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) e o [Compartilhamento de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake). Para uma lista completa das tabelas disponíveis e suas colunas, consulte a [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables).

### Visualizações de atributos do perfil de usuário {#user-profile-attribute-views}

O Criador de consultas e as extensões de segmento SQL incluem a maioria das [visualizações de atributos do perfil de usuário]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#user-profile-attribute-views), como snapshots periódicos e histórico de atributos padrão.

Duas visualizações de atributos personalizados estão disponíveis apenas por meio do [Compartilhamento de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes):

- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

A Braze exclui essas visualizações do Criador de consultas e das extensões de segmento SQL porque elas são lentas para consultar na escala do espaço de trabalho e frequentemente excedem o tempo limite. Use `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` para snapshots de atributos personalizados no Criador de consultas. Se você precisar de dados históricos ou quase em tempo real de atributos personalizados, consulte as visualizações excluídas por meio do Compartilhamento de dados do Snowflake.

## Executando relatórios no Criador de consultas {#running-reports-in-the-query-builder}

Para executar um relatório no Criador de consultas:

1. Acesse **Analytics** > **Query Builder**.
2. Selecione **Create SQL Query**. Se precisar de inspiração ou ajuda para elaborar sua consulta, selecione **Query Template** e escolha um modelo da lista. Caso contrário, selecione **SQL Editor** para ir direto ao editor.
3. Seu relatório recebe automaticamente um nome com a data e hora atuais. Passe o cursor sobre o nome e selecione <i class="fas fa-pencil" alt="Editar"></i> para dar um nome significativo à sua consulta SQL.
4. Escreva sua consulta SQL no editor ou [obtenha ajuda da IA](#ai-query-builder) na guia **AI Query Builder**. Se estiver escrevendo seu próprio SQL, consulte [Escrevendo consultas SQL personalizadas](#custom-sql) para requisitos e recursos.
5. Selecione **Run Query**.
6. Salve sua consulta.
7. Para baixar um CSV do seu relatório, selecione **Export**.

![Criador de consultas mostrando os resultados para a consulta de modelo "Engajamento e receita por canal nos últimos 30 dias".]({% image_buster /assets/img_archive/query_builder.png %})

Os resultados de cada relatório podem ser gerados uma vez por dia. Se você executar o mesmo relatório mais de uma vez no mesmo dia, verá os mesmos resultados em ambos os relatórios.

### Modelos de consulta {#query-templates}

Acesse os modelos de consulta selecionando **Create SQL Query** > **Query Template** ao criar um relatório pela primeira vez.

Consulte [Modelos de consulta]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) para ver a lista de modelos disponíveis.

### Período dos dados {#data-timeframe}

As consultas retornam dados dos últimos 60 dias. Se você usa Currents ou [Compartilhamento de dados do Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake), é possível consultar até dois anos de dados, que é o tempo de retenção dos seus dados no Snowflake. Para mais detalhes sobre retenção estendida de dados, entre em contato com seu gerente de sucesso do cliente.

### Fuso horário do Criador de consultas {#query-builder-time-zone}

O fuso horário padrão para consultas no nosso banco de dados Snowflake é UTC. Como resultado, pode haver algumas discrepâncias de dados entre a página **Email Channel Engagement** (que segue o fuso horário da sua empresa) e os resultados do Criador de consultas.

Para converter o fuso horário nos resultados da sua consulta, adicione o seguinte SQL à sua consulta e personalize-o para o fuso horário da sua empresa:

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

### Histórico de consultas {#query-history}

A seção **Query history** no Criador de consultas exibe suas consultas executadas anteriormente para ajudar a rastrear e reutilizar seu trabalho. O histórico de consultas é retido por sete dias, o que significa que consultas com mais de sete dias são removidas automaticamente.

Se você precisar auditar o uso de consultas por períodos mais longos ou manter registros além de sete dias, recomendamos exportar ou salvar os resultados de consultas importantes antes que expirem.

### Comparando o Criador de consultas com outras fontes de relatório {#comparing-query-builder-with-other-reporting-sources}

Os resultados do Criador de consultas podem diferir de outras ferramentas de relatório porque utilizam fontes de dados e métodos de processamento diferentes.

Por exemplo, as contagens de soft bounce no Criador de consultas podem ser maiores do que nos relatórios de entregabilidade do SendGrid. O Criador de consultas conta todas as ocorrências de soft bounces sem deduplicação. Se um usuário sofre soft bounce várias vezes antes da entrega final (ou após tentativas prolongadas), cada tentativa de soft bounce é contada. O SendGrid Deliverability usa seus próprios dados e lógica, nos quais a Braze não tem visibilidade, então as contagens entre os dois relatórios podem não coincidir.

Para saber mais sobre como os soft bounces são rastreados em diferentes fontes de relatório, consulte [Soft bounce]({{site.baseurl}}/user_guide/channels/email/reporting/analytics_glossary#soft-bounce) no glossário de análise de dados de e-mail.

## Gerando SQL com o Criador de consultas com IA {#generating-sql-with-the-ai-query-builder}

O Criador de consultas com IA utiliza o [GPT](https://openai.com/gpt-4), desenvolvido pela OpenAI, para recomendar SQL para sua consulta.

![O Criador de consultas SQL com IA.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

Para gerar SQL com o Criador de consultas com IA:

1. Após criar um relatório no Criador de consultas, selecione a guia **AI Query Builder**.
2. Digite seu prompt ou selecione um prompt de exemplo e clique em **Generate** para traduzir seu prompt em SQL.
3. Revise o SQL gerado para verificar se está correto e selecione **Insert into Editor**.

### Dicas {#tips}

- Familiarize-se com as tabelas e colunas disponíveis na [referência de tabelas SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Solicitar dados que não existem nessas tabelas pode fazer com que o ChatGPT invente uma tabela fictícia.
- Familiarize-se com as [regras de escrita SQL]({{site.baseurl}}/user_guide/analytics/reports/query_builder#custom-sql) desse recurso. Não seguir essas regras causará um erro.
- Você pode enviar até 20 prompts por minuto com o Criador de consultas com IA.

#{% multi_lang_include brazeai/generative_ai/policy.md %}

## Escrevendo consultas SQL personalizadas {#custom-sql}

Escreva sua consulta SQL usando a [sintaxe do Snowflake](https://docs.snowflake.com/en/sql-reference). Consulte a [referência de tabelas]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) para uma lista completa de tabelas e colunas disponíveis para consulta.

Para visualizar detalhes das tabelas dentro do Criador de consultas:

1. Na página do **Criador de consultas**, abra o painel **Reference** e selecione **Available Data Tables** para visualizar as tabelas de dados disponíveis e seus nomes.
3. Selecione <i class="fas fa-chevron-down" alt=""></i> **See Details** para visualizar a descrição da tabela e informações sobre as colunas, como tipos de dados.
4. Para inserir o nome da tabela no seu SQL, selecione <i class="fas fa-copy" title="Copiar nome da tabela para o editor SQL"></i> **Copy table name to SQL editor**.

Para usar consultas pré-escritas fornecidas pela Braze, selecione **Query Template** ao criar um relatório pela primeira vez no Criador de consultas.

Restringir sua consulta a um período específico ajudará a gerar resultados mais rapidamente. A seguir, um exemplo de consulta que obtém o número de compras e a receita gerada na última hora.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

Esta consulta recupera o número de envios de e-mail no último mês:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

Se você consultar `CANVAS_ID`, `CANVAS_VARIATION_API_ID` ou `CAMPAIGN_ID`, as colunas de nome associadas serão automaticamente incluídas na tabela de resultados. Você não precisa incluí-las na própria consulta `SELECT`.

| Nome do ID | Coluna de nome associada |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Escrevendo consultas SQL personalizadas" }

Esta consulta recupera todos os três IDs e suas colunas de nome associadas com um máximo de 100 linhas:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### Preencher automaticamente o nome da variante de campanha {#automatically-populate-the-campaign-variant-name}

Se você quiser que o nome da variante de campanha seja preenchido automaticamente, inclua o nome da coluna `MESSAGE_VARIATION_API_ID` na sua consulta, como neste exemplo:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### Solução de problemas {#troubleshooting}

Sua consulta pode falhar por qualquer um dos seguintes motivos:

- Erros de sintaxe na sua consulta SQL
- Tempo limite de processamento (após 6 minutos)
    - Relatórios que levam mais de 6 minutos para serem executados atingirão o tempo limite.
    - Se um relatório atingir o tempo limite, tente limitar o período no qual você está consultando dados ou consulte um conjunto de dados mais específico.

## Usando variáveis {#using-variables}

Use variáveis para utilizar tipos de variáveis predefinidos em SQL para referenciar valores sem precisar copiar manualmente o valor. Por exemplo, em vez de copiar manualmente o ID de uma Campaign para o editor SQL, você pode usar {% raw %}`{{campaign.${My campaign}}}`{% endraw %} para selecionar diretamente uma Campaign em um menu suspenso na guia **Variables**.

Depois que uma variável é criada, ela aparecerá na guia **Variables** do seu relatório do Criador de consultas. Os benefícios de usar variáveis SQL incluem:

{% multi_lang_include analytics/sql_variables_benefits.md %}

### Diretrizes {#guidelines}

As variáveis devem seguir a seguinte sintaxe Liquid: {% raw %}`{{ type.${name}}}`{% endraw %}, em que `type` deve ser um dos tipos aceitos e `name` pode ser qualquer nome que você escolher. Os rótulos dessas variáveis usam o nome da variável como padrão.

Por padrão, todas as variáveis são obrigatórias (e seu relatório não será executado a menos que os valores das variáveis sejam selecionados), exceto o intervalo de datas, que usa como padrão os últimos 30 dias quando o valor não é fornecido.

### Tipos de variáveis {#variable-types}

Os seguintes tipos de variáveis são aceitos:

- [Número](#number)
- [Intervalo de datas](#date-range)
- [Envio de mensagens](#messaging)
- [Produtos](#products)
- [Eventos personalizados](#custom-events)
- [Propriedades de eventos personalizados](#custom-event-properties)
- [Espaço de trabalho](#workspace)
- [Catálogos](#catalogs)
- [Campos de catálogo](#catalog-fields)
- [Opções](#options)
- [Segments](#segments)
- [String](#string)
- [Tags](#tags)

#### Número {#number}

- **Valor de substituição:** O valor fornecido, como `5.5`
- **Exemplo de uso:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### Intervalo de datas {#date-range}

Se estiver usando `start_date` e `end_date`, ambos devem ter o mesmo nome para que possam ser usados como um intervalo de datas.

##### Valores de exemplo {#example-values}

O tipo de intervalo de datas pode ser relativo, data de início, data de término ou intervalo de datas.

Todos os quatro tipos são exibidos se `start_date` e `end_date` forem usados com o mesmo nome. Se apenas um for usado, somente os tipos relevantes serão exibidos.

| Tipo de intervalo de datas | Descrição | Valores obrigatórios |
| --- | --- | --- |
| Relativo | Especifica os últimos X dias | Requer `start_date` |
| Data de início | Especifica uma data de início | Requer `start_date` |
| Data de término | Especifica uma data de término | Requer `end_date` |
| Intervalo de datas | Especifica uma data de início e uma data de término | Requer `start_date` e `end_date` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Valores de exemplo" }

- **Valor de substituição:** Substitui `start_date` e `end_date` por um timestamp Unix em segundos para uma data especificada em UTC, como `1696517353`.
- **Exemplo de uso:** Para todas as variáveis de relativo, data de início, data de término e intervalo de datas:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - Você pode usar `start_date` ou `end_date` se não quiser um intervalo de datas.

#### Envio de mensagens {#messaging}

Todas as variáveis de envio de mensagens devem compartilhar o mesmo identificador quando você deseja vincular seus estados em um grupo.

##### Canvas {#canvas}

Para selecionar um Canvas. Compartilhar o mesmo nome com uma Campaign resultará em um botão de opção na guia **Variables** para selecionar Canvas ou Campaign.

- **Valor de substituição:** BSON ID do Canvas
- **Exemplo de uso:** {% raw %}`canvas_id = '{{canvas.${some name}}}'`{% endraw %}

##### Canvas (múltiplos) {#canvases}

Para selecionar múltiplos Canvas. Compartilhar o mesmo nome com uma Campaign resultará em um botão de opção na guia **Variables** para selecionar Canvas ou Campaign.

- **Valor de substituição:** BSON IDs dos Canvas
- **Exemplo de uso:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campaign {#campaign}

Para selecionar uma Campaign. Compartilhar o mesmo nome com um Canvas resultará em um botão de opção na guia **Variables** para selecionar Canvas ou Campaign.

- **Valor de substituição:** BSON ID da Campaign
- **Exemplo de uso:** {% raw %}`campaign_id = '{{campaign.${some name}}}'`{% endraw %}

##### Campaigns {#campaigns}

Para selecionar múltiplas Campaigns. Compartilhar o mesmo nome com um Canvas resultará em um botão de opção na guia **Variables** para selecionar Canvas ou Campaign.

- **Valor de substituição:** BSON IDs das Campaigns
- **Exemplo de uso:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### Variantes de Campaign {#campaign-variants}

Para selecionar variantes de Campaign que pertencem à Campaign selecionada. Deve ser usada em conjunto com uma variável de Campaign ou Campaigns.

- **Valor de substituição:** IDs de API das variantes de Campaign, strings delimitadas por vírgulas, como `api-id1, api-id2`.
- **Exemplo de uso:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### Variantes de Canvas {#canvas-variants}

Para selecionar variantes de Canvas que pertencem a um Canvas escolhido. Deve ser usada com uma variável de Canvas ou Canvas (múltiplos).

- **Valor de substituição:** IDs de API das variantes de Canvas, strings delimitadas por vírgulas, como `api-id1, api-id2`.
- **Exemplo de uso:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### Etapa do Canvas {#canvas-step}

Para selecionar uma etapa do Canvas que pertence a um Canvas escolhido. Deve ser usada com uma variável de Canvas.

- **Valor de substituição:** ID de API da etapa do Canvas
- **Exemplo de uso:** {% raw %}`canvas_step_api_id = '{{canvas_step.${some name}}}'`{% endraw %}

##### Etapas do Canvas {#canvas-steps}

Para selecionar etapas do Canvas que pertencem a Canvas escolhidos. Deve ser usada com uma variável de Canvas ou Canvas (múltiplos).

- **Valor de substituição:** IDs de API das etapas do Canvas
- **Exemplo de uso:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}