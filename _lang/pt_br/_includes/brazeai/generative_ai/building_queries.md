> Saiba como usar o Criador de consultas para gerar relatórios usando dados da Braze no Snowflake. O Criador de consultas vem com [modelos de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) de SQL pré-construídos para você começar, ou você pode escrever suas próprias consultas de SQL personalizadas para desbloquear ainda mais insights.

## Pré-requisitos {#prerequisites}

Você precisará de [permissões "Ver IPI"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) para usar o Criador de consultas, pois ele permite acesso direto a alguns dados de cliente.

## Usando o Criador de consultas {#using-the-query-builder}

### Etapa 1: Criar uma consulta SQL {#step-1-create-an-sql-query}

Para criar uma nova consulta, acesse **Analytics** > **Query Builder** e selecione **Create SQL Query**.

![As opções "Query Template" e "SQL Editor" encontradas no menu suspenso "Create SQL Query".]({% image_buster /assets/img_archive/create_sql_query_button.png %}){: style="max-width:60%;"}

Se você precisa de inspiração ou ajuda para elaborar sua consulta, escolha **Query Template** e selecione um [modelo pronto]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates). Para começar com uma consulta em branco, selecione **SQL Editor**.

Seu relatório recebe automaticamente um nome com a data e hora atuais. Passe o cursor sobre o nome e selecione <i class="fas fa-pencil" alt="Editar"></i> para dar à sua consulta SQL um nome significativo.

![Um exemplo de nome de relatório: "Channel engagement for May 2025".]({% image_buster /assets/img_archive/report_name_example.png %}){: style="max-width:80%;"}

### Etapa 2: Montar sua consulta {#step-2-build-your-query}

Ao montar sua consulta, você pode optar por receber ajuda da IA ou criar por conta própria.

{% tabs local %}
{% tab Usando BrazeAI %}
O Criador de consultas com IA utiliza o [GPT](https://openai.com/gpt-4), da OpenAI, para recomendar SQL para sua consulta. Para gerar SQL com o Criador de consultas com IA:

1. Depois de criar um relatório no Criador de consultas, selecione a guia **AI Query Builder**.
2. Digite seu prompt ou selecione um prompt de exemplo e selecione **Generate** para traduzir seu prompt em SQL.
3. Revise o SQL gerado para confirmar que está correto e selecione **Insert into Editor**.

![O Criador de consultas SQL com IA.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

#### Dicas {#tips}

- Familiarize-se com as [tabelas de dados disponíveis no Snowflake]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables). Solicitar dados que não existem nessas tabelas pode fazer com que o ChatGPT invente uma tabela fictícia.
- Familiarize-se com as [regras de escrita de SQL]({{site.baseurl}}/user_guide/data_and_analytics/query_builder#custom-sql) desse recurso. Não seguir essas regras causará um erro.
- Você pode enviar até 20 prompts por minuto com o Criador de consultas com IA.

##{% multi_lang_include brazeai/generative_ai/policy.md %}
{% endtab %}

{% tab Por conta própria %}
Escreva sua consulta SQL usando a [sintaxe do Snowflake](https://docs.snowflake.com/en/sql-reference). Consulte a [referência de tabelas]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables) para obter a lista completa de tabelas e colunas disponíveis para consulta.

Para visualizar detalhes das tabelas dentro do Criador de consultas:

1. Na página do **Query Builder**, abra o painel **Reference** e selecione **Available Data Tables** para ver as tabelas de dados disponíveis e seus nomes.
3. Selecione <i class="fas fa-chevron-down" alt=""></i> **See Details** para ver a descrição da tabela e informações sobre as colunas, como tipos de dados.
4. Para inserir o nome da tabela no seu SQL, selecione <i class="fas fa-copy" title="Copiar nome da tabela para o editor SQL"></i>.

Restringir sua consulta a um período específico ajudará a gerar resultados mais rapidamente. O exemplo a seguir obtém o número de compras e a receita gerada na última hora.

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

Se você consultar `CANVAS_ID`, `CANVAS_VARIATION_API_ID` ou `CAMPAIGN_ID`, as colunas de nome associadas serão automaticamente incluídas na tabela de resultados. Não é necessário incluí-las na própria consulta `SELECT`.

| Nome do ID | Coluna de nome associada |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dicas" }

Esta consulta recupera os três IDs e suas colunas de nome associadas com um máximo de 100 linhas:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

#### Solução de problemas {#troubleshooting}

Sua consulta pode falhar por qualquer um dos seguintes motivos:

- Erros de sintaxe na sua consulta SQL
- Tempo limite de processamento (após 6 minutos)
    - Relatórios que levam mais de 6 minutos para rodar atingirão o tempo limite.
    - Se um relatório atingir o tempo limite, tente limitar o intervalo de tempo da consulta ou consultar um conjunto de dados mais específico.
{% endtab %}
{% endtabs %}

### Etapa 3: Gerar seu relatório {#step-3-generate-your-report}

Quando terminar de montar sua consulta, selecione **Run Query**. Se não houver erros ou [tempos limite do relatório](#report-timeouts), um arquivo CSV será gerado a partir da consulta.

Para baixar o relatório CSV, selecione **Export**.

![O Criador de consultas mostrando os resultados para a consulta de modelo "Channel engagement and revenue for the last 30 days".]({% image_buster /assets/img_archive/query_builder.png %})

{% alert important %}
Cada relatório pode gerar resultados apenas uma vez por dia. Se você executar o mesmo relatório várias vezes em um único dia, verá os mesmos resultados em cada relatório.
{% endalert %}

## Tempo limite de relatórios {#report-timeouts}

Relatórios que levam mais de seis minutos para serem executados sofrerão tempo limite. Se esta for a primeira consulta que você está executando após algum tempo, o processamento pode demorar mais e, portanto, há uma probabilidade maior de tempo limite. Se isso acontecer, tente executar o relatório novamente.

Se o seu relatório continuar sofrendo tempo limite após várias tentativas, [entre em contato com o Suporte]({{site.baseurl}}/help/support#braze-support).

## Consultando motivos de interrupção {#querying-abort-reasons}

Você pode consultar a coluna `ABORT_TYPE` em qualquer tabela `USERS_MESSAGES_*_ABORT_SHARED` para analisar por que as mensagens não foram enviadas. O campo `ABORT_TYPE` contém um valor da string descrevendo o motivo específico da interrupção, e o campo complementar `ABORT_LOG` contém detalhes adicionais (como a regra de limite de frequência que foi disparada).

Por exemplo, para contar interrupções de e-mail por tipo nos últimos 30 dias:

```sql
SELECT ABORT_TYPE, COUNT(*) as abort_count
FROM USERS_MESSAGES_EMAIL_ABORT_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY ABORT_TYPE
ORDER BY abort_count DESC
```

Para a lista completa de valores de `ABORT_TYPE` e suas descrições, consulte [Tipos de interrupção]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables#abort-types).

## Dados e resultados {#data-and-results}

Todas as consultas exibem dados dos últimos 60 dias. Quando você exportar seus resultados, o arquivo conterá no máximo 1.000 linhas. Para relatórios que exigem volumes maiores de dados, você pode usar ferramentas como o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou o [endpoint de exportação da API]({{site.baseurl}}/api/endpoints/export).

## Créditos do Snowflake {#snowflake-credits}

Cada empresa tem 5 créditos do Snowflake disponíveis por mês, compartilhados entre todos os espaços de trabalho. Uma pequena parte de um crédito do Snowflake é utilizada sempre que você executa uma consulta ou visualiza a prévia de uma tabela.

{% alert note %}
Os créditos do Snowflake não são compartilhados entre recursos. Por exemplo, os créditos das extensões de Segment SQL e do Criador de consultas são independentes entre si.
{% endalert %}

O uso de créditos está correlacionado ao tempo de execução da sua consulta SQL. Quanto maior o tempo de execução, maior a parte de um crédito do Snowflake que a consulta consumirá. O tempo de execução pode variar dependendo da complexidade e do tamanho das suas consultas ao longo do tempo. Quanto mais complexas e frequentes forem as consultas executadas, maior será a alocação de recursos e mais rápido será o tempo de execução.

Os créditos não são utilizados ao escrever, editar ou salvar relatórios no editor SQL da Braze. Seus créditos serão redefinidos para 5 no primeiro dia de cada mês à meia-noite (UTC). Você pode monitorar o uso mensal de créditos no topo da página do Criador de consultas.

![Criador de consultas mostrando a quantidade de créditos utilizados no mês atual.]({% image_buster /assets/img_archive/query_builder_credits.png %}){: style="max-width:60%;"}

Quando você atingir o limite de créditos, não será possível executar consultas, mas você ainda poderá criar, editar e salvar relatórios SQL. Se quiser adquirir mais créditos do Criador de consultas, entre em contato com seu gerente de conta.