---
nav_title: Treasure Data para Currents
article_title: Treasure Data para Currents
description: "Este artigo de referência descreve a parceria entre o Braze Currents e o Treasure Data, uma plataforma de dados do cliente corporativo que transmite dados de eventos da Braze para o Treasure Data para análise e ativação."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data para Currents {#treasure-data-for-currents}

> O [Treasure Data](https://www.treasuredata.com/) é uma plataforma de dados do cliente (CDP) que coleta e encaminha informações de várias fontes para uma variedade de outros locais na sua pilha de marketing.

A integração entre a Braze e o Treasure Data permite que você controle o fluxo de informações entre os dois sistemas. Com o Currents, você pode transmitir dados de eventos da Braze para o Treasure Data e torná-los acionáveis em toda a sua growth stack.

O método recomendado é o conector **Braze Currents Streaming** no Treasure Data, combinado com uma **Custom Currents Export** na Braze. Essa abordagem oferece:

- Transmissão de eventos em tempo real da Braze para o Treasure Data
- Roteamento automático opcional de tabelas por tipo de evento
- Um esquema plano, consultável via SQL, que não exige análise de JSON

{% alert note %}
O conector Braze Currents Streaming está disponível mediante solicitação. Entre em contato com o suporte do Treasure Data para ativá-lo na sua conta do Treasure Data. Para detalhes de configuração do lado do parceiro, consulte a documentação do Treasure Data sobre [Integração de importação do Braze Currents](https://docs.treasuredata.com/int/braze-currents-import-integration).
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Treasure Data | Uma [conta Treasure Data](https://console.treasuredata.com) ativa é necessária para aproveitar esta parceria. |
| Currents | Para exportar dados para o Treasure Data, você precisa do [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) configurado para a sua conta. |
| Conector Braze Currents Streaming | Entre em contato com o suporte do Treasure Data para ativar o conector Braze Currents Streaming na sua conta Treasure Data. |
| Chave de API de escrita do Treasure Data | Uma chave de API de escrita do Treasure Data autentica o fluxo de entrada da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Configurar o conector no Treasure Data {#step-1-configure-the-connector-in-treasure-data}

1. No console do Treasure Data, acesse **Connections** > **New Connection**.
2. Selecione **Braze Currents Streaming**.
3. Em **Authentication**, insira sua chave de API de escrita do Treasure Data.
4. Em **Source Settings**, configure o seguinte:

| Campo | Descrição |
| ----- | --------- |
| Source Name | Um nome descritivo para essa conexão |
| Datastore | Selecione **Plazma** |
| Database | O banco de dados do Treasure Data onde os eventos são armazenados |
| Table | A tabela de destino padrão |
| Multiple Tables | Selecione para direcionar cada tipo de evento da Braze para sua própria tabela |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configurações de origem" }

5. Após salvar, copie o **Unique ID** (`task_id`). Você precisará desse valor na próxima etapa.

### Etapa 2: Criar uma exportação Custom Currents na Braze {#step-2-create-a-custom-currents-export-in-braze}

A opção **Treasure Data Export** na interface de Braze Currents usa o método legado de API Postback e não é mais recomendada. Use **Custom Currents Export** em vez disso.

1. Na Braze, acesse **Partner Integrations** > **Data Export**.
2. Selecione **Create New Current** > **Custom Currents Export**.
3. Insira um nome de integração e um e-mail de contato para notificações de erro.
4. Em **Credentials**, insira a URL do endpoint para sua região do Treasure Data. Insira sua chave de API de escrita do Treasure Data como o **Bearer Token**.

| Região | URL do endpoint |
| ------ | --------------- |
| US | `https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID}` |
| EU | `https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID}` |
| AP02 | `https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID}` |
| Tokyo | `https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs de endpoint por região" }

Substitua `{TASK_ID}` pelo Unique ID que você copiou na [Etapa 1](#step-1-configure-the-connector-in-treasure-data).

5. Selecione os tipos de evento que você deseja exportar. As conexões Custom Currents podem enviar eventos tanto para usuários identificados quanto para usuários sem um `external_user_id`. O Treasure Data ingere ambos.
6. Selecione **Launch Current**.

{% alert warning %}
Mantenha sua chave de API de escrita do Treasure Data e a URL do endpoint atualizadas. Se o endpoint ficar inacessível por mais de **5&nbsp;dias**, a Braze descarta os eventos do conector e os dados são permanentemente perdidos.
{% endalert %}

## Consulte seus dados {#query-your-data}

Depois que os eventos estiverem fluindo, consulte-os com SQL. O Treasure Data planifica a carga útil, então você não precisa fazer parse de JSON.

```sql
SELECT
  id AS event_id,
  event_type,
  user_external_user_id,
  properties_campaign_name,
  properties_email_address,
  time
FROM your_database.your_table
WHERE TD_INTERVAL(time, '-1d', 'JST')
```

{% alert note %}
O campo `time` no Treasure Data é o registro de data/hora de quando o Treasure Data recebeu e processou o evento, não o horário original de ocorrência do evento na Braze.
{% endalert %}

Se você selecionou **Multiple Tables**, cada tipo de evento é direcionado para sua própria tabela (por exemplo, `users_message_email_open` ou `users_behaviors_purchase`).

Para confirmar que os dados estão chegando, execute uma consulta de contagem alguns minutos após iniciar o Currents:

```sql
SELECT COUNT(*)
FROM your_table
WHERE TD_INTERVAL(time, '-1h')
```

## Esquema de dados {#data-schema}

O Treasure Data nivela JSON aninhado em até dois níveis de profundidade:

| Tipo JSON | Tipo de coluna do Treasure Data |
| --------- | ------------------------- |
| string | string |
| number | long |
| boolean | string |
| array | JSON string |
| object (nível 1) | `field_name` |
| object (nível 2) | `parent_field_name_field_name` |
| null | omitido |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mapeamento de tipos de dados" }

Os nomes das colunas usam apenas letras minúsculas e underscores.

## Limites {#limits}

| Item | Limite |
| ---- | ----- |
| Tamanho máximo da carga útil | 1&nbsp;MB por solicitação |
| Tamanho do lote | 100 eventos por lote (padrão) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Limites" }

## Detalhes da integração {#integration-details}

A Braze oferece suporte à exportação de todos os dados listados nos [glossários de eventos do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para o Treasure Data. Isso inclui todas as propriedades em eventos de [engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) e [comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

A estrutura da carga útil dos dados exportados corresponde à estrutura da carga útil dos conectores HTTP personalizados. Você pode consultar exemplos de cargas úteis no [repositório de exemplos para conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Migrar do método legado de Postback {#migrate-from-the-legacy-postback-method}

Se você usava anteriormente o **Treasure Data Export** (Postback) na Braze:

1. Conclua a configuração de Custom Currents Export neste artigo.
2. Confirme se os eventos estão fluindo para a nova tabela.
3. Desative o antigo Current baseado em Postback na Braze.

Os dados legados armazenados como arrays JSON brutos ainda podem ser consultados com `JSON_PARSE` e `UNNEST`. Os novos dados ingeridos pelo conector de streaming usam o esquema plano descrito em [Esquema de dados](#data-schema).