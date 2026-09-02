---
nav_title: "Atributos do perfil de usuário"
article_title: Visualizações de atributos de usuário no Snowflake
page_order: 10
page_type: partner
search_tag: Partner
toc_headers: h2
---

# Atributos do perfil de usuário {#user-profile-attributes}

> Esta página serve como referência para as visualizações de atributos padrão e personalizados no Snowflake. Há três visualizações para atributos padrão e três visualizações para atributos personalizados, cada uma projetada para um caso de uso específico com suas próprias considerações de desempenho.

## Paridade de dados com o dashboard {#data-parity-with-the-dashboard}

Em circunstâncias raras, os valores de atributos padrão e personalizados nas visualizações do Snowflake nesta página podem não corresponder ao que você vê no perfil de um usuário no dashboard da Braze.

Por exemplo, um atributo pode aparecer como `NULL` no Snowflake, enquanto o dashboard mostra um valor para esse usuário.

Se você perceber discrepâncias generalizadas, entre em contato com seu CSM ou com o suporte da Braze.

## Visualizações disponíveis {#available-views}

<table aria-label="Visualizações disponíveis">
  <caption>Visualizações disponíveis</caption>
  <thead>
    <tr>
      <th>Tipo</th>
      <th>Visualização</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Atributo padrão</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Snapshots de perfis de usuário</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Perfis de usuário em tempo real</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Registros históricos de alterações</td>
    </tr>
    <tr>
      <td rowspan="3">Atributo personalizado</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Snapshots de perfis de usuário</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Perfis de usuário em tempo real</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Registros históricos de alterações</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Visualizações disponíveis" }

## Snapshots de perfil de usuário {#user-profile-snapshots}

Essas visualizações fornecem snapshots periódicos dos atributos do perfil de usuário. Os dados têm um atraso de até 12 horas, o que os torna úteis para consultas que não exigem atualizações em tempo real.

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### Uso {#usage}

* Fornece um snapshot dos atributos de usuário com um atraso de até **12 horas**.
* Tem bom desempenho para consultas que não exigem precisão em tempo real.
* Execução de consultas mais rápida, especialmente ao filtrar por atributos diferentes de `USER_ID`.
* **Limitação:** os dados não são atualizados em tempo real.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Schema de `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_default_attributes_view_shared-schema}

| Nome da coluna     | Tipo de dados     | Descrição |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identificador do seu espaço de trabalho da Braze |
| `APP_ID` | VARCHAR | O app específico dentro do seu espaço de trabalho |
| `USER_ID` | VARCHAR | O identificador exclusivo de usuário da Braze |
| `TIME` | NUMBER | Timestamp Unix (segundos) da atualização do perfil |
| `TIME_MS` | NUMBER | Timestamp Unix (milissegundos) da atualização do perfil |
| `UPDATE_SOURCE` | VARCHAR | A origem da atualização do atributo (API, SDK, dashboard, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Quando os dados foram atualizados pela última vez no Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Seu próprio identificador de usuário (se definido) |
| `FIRST_NAME` | VARCHAR | Nome do usuário |
| `LAST_NAME` | VARCHAR | Sobrenome do usuário |
| `EMAIL_ADDRESS` | VARCHAR | Endereço de e-mail do usuário |
| `GENDER` | VARCHAR | Gênero do usuário |
| `PHONE_NUMBER` | VARCHAR | Número de telefone do usuário |
| `DOB` | VARCHAR | Data de nascimento do usuário |
| `TIME_ZONE` | VARCHAR | Fuso horário do usuário |
| `HOME_CITY` | VARCHAR | Cidade do usuário |
| `COUNTRY` | VARCHAR | País do usuário |
| `LANGUAGE` | VARCHAR | Preferência de idioma do usuário |
| `ARCHIVED` | BOOLEAN | Se o perfil de usuário está arquivado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schema de USERDEFAULTATTRIBUTESVIEWSHARED" }


### Schema de `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` {#user_custom_attributes_view_shared-schema}

| Nome da coluna     | Tipo de dados     | Descrição |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identificador do seu espaço de trabalho da Braze |
| `APP_ID` | VARCHAR | O app específico dentro do seu espaço de trabalho |
| `USER_ID` | VARCHAR | O identificador exclusivo de usuário da Braze |
| `EXTERNAL_USER_ID` | VARCHAR | Seu próprio identificador de usuário (se definido) |
| `TIME` | NUMBER | Timestamp Unix (segundos) da atualização do perfil |
| `TIME_MS` | NUMBER | Timestamp Unix (milissegundos) da atualização do perfil |
| `UPDATE_SOURCE` | VARCHAR | A origem da atualização do atributo (API, SDK, dashboard, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Quando os dados foram atualizados pela última vez no Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | Objeto JSON contendo todos os atributos personalizados (pares chave-valor) |
| `ARCHIVED` | BOOLEAN | Se o perfil de usuário está arquivado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schema de USERCUSTOMATTRIBUTESVIEWSHARED" }

#### Trabalhando com CUSTOM_ATTRIBUTES {#working-with-custom_attributes}

A coluna `CUSTOM_ATTRIBUTES` armazena todos os seus atributos personalizados como um objeto JSON. Você pode acessar atributos individuais usando as funções JSON do Snowflake.

**Exemplo: consultando atributos personalizados específicos**

```sql
-- Get users with a specific loyalty tier
SELECT
  USER_ID,
  EXTERNAL_USER_ID,
  CUSTOM_ATTRIBUTES:loyalty_tier::STRING as loyalty_tier,
  CUSTOM_ATTRIBUTES:points::NUMBER as points
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:loyalty_tier::STRING = 'gold';

-- Get users who made a purchase above a certain amount
SELECT
  USER_ID,
  CUSTOM_ATTRIBUTES:last_purchase_amount::NUMBER as last_purchase_amount
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:last_purchase_amount::NUMBER > 100;
```

**Exemplo: analisando dados de atributos personalizados**

```sql
-- Count users by subscription status
SELECT
  CUSTOM_ATTRIBUTES:subscription_status::STRING as subscription_status,
  COUNT(*) as user_count
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
GROUP BY CUSTOM_ATTRIBUTES:subscription_status::STRING;

-- Find average order value by customer segment
SELECT
  CUSTOM_ATTRIBUTES:customer_segment::STRING as segment,
  AVG(CUSTOM_ATTRIBUTES:lifetime_value::NUMBER) as avg_lifetime_value
FROM USER_CUSTOM_ATTRIBUTES_VIEW_SHARED
WHERE CUSTOM_ATTRIBUTES:customer_segment IS NOT NULL
GROUP BY CUSTOM_ATTRIBUTES:customer_segment::STRING;
```

## Visualizações de perfil de usuário em tempo real {#real-time-user-profile-views}

Essas visualizações fornecem atualizações quase em tempo real sobre atributos de perfil de usuário, com dados atrasados em até 10 minutos após uma atualização ocorrer na Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### Uso

* Fornece atributos de usuário atualizados com atraso mínimo (~10 minutos).
* Útil para análises em tempo real e cenários em que dados recentes são necessários.
* **Considerações de desempenho:**
    * Consultas em usuários individuais são mais rápidas (menos de um minuto usando um warehouse grande).
    * Consultas sem filtros de USER_ID exigem agregação entre todos os usuários, resultando em tempos de execução significativamente mais longos.
    * Consultas em um grande conjunto de dados (como mais de 100 milhões de usuários) podem levar muitos minutos.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Esquema de `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_latest_state_default_attributes_view_shared-schema}

| Nome da coluna     | Tipo de dados     | Descrição |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identificador do seu espaço de trabalho na Braze |
| `APP_ID` | VARCHAR | O app específico dentro do seu espaço de trabalho |
| `USER_ID` | VARCHAR | O identificador exclusivo de usuário da Braze |
| `TIME` | NUMBER | Timestamp Unix (segundos) da atualização do perfil |
| `TIME_MS` | NUMBER | Timestamp Unix (milissegundos) da atualização do perfil |
| `UPDATE_SOURCE` | VARCHAR | A origem da atualização do atributo (API, SDK, dashboard, etc.) |
| `ARCHIVED` | BOOLEAN | Se o perfil de usuário está arquivado |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ | Quando os dados foram atualizados pela última vez no Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Seu próprio identificador de usuário (se definido) |
| `FIRST_NAME` | VARCHAR | Nome do usuário |
| `LAST_NAME` | VARCHAR | Sobrenome do usuário |
| `EMAIL_ADDRESS` | VARCHAR | Endereço de e-mail do usuário |
| `GENDER` | VARCHAR | Gênero do usuário |
| `PHONE_NUMBER` | VARCHAR | Número de telefone do usuário |
| `DOB` | VARCHAR | Data de nascimento do usuário |
| `HOME_CITY` | VARCHAR | Cidade do usuário |
| `COUNTRY` | VARCHAR | País do usuário |
| `LANGUAGE` | VARCHAR | Preferência de idioma do usuário |
| `TIME_ZONE` | VARCHAR | Fuso horário do usuário |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED" }

### Esquema de `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` {#user_latest_state_custom_attribute_view_shared-schema}

{% include partners/snowflake_user_attributes_custom_view_schemas.md schema="latest" %}

## Registros históricos de alterações {#historical-change-logs}

Essas visualizações armazenam registros históricos de alterações de atributos de usuário, capturando mudanças com uma granularidade de 12 horas.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### Uso

* Fornece um registro de alterações históricas nos atributos de usuário para um período contínuo de 6 meses.
* Os dados são capturados a cada 12 horas, o que significa que várias atualizações nessa janela são combinadas em um único registro. Alterações individuais dentro desse período não são retidas separadamente.
* `EFF_DT` e `END_DT` marcam o início e o fim do estado de um atributo do usuário.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Esquema de `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_default_attributes_history_view_shared-schema}

| Nome da coluna     | Tipo de dados     | Descrição |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identificador do seu espaço de trabalho da Braze |
| `USER_ID` | VARCHAR | Identificador único do usuário na Braze |
| `APP_ID` | VARCHAR | O app específico dentro do seu espaço de trabalho |
| `TIME` | NUMBER | Timestamp Unix (segundos) da atualização do perfil |
| `TIME_MS` | NUMBER | Timestamp Unix (milissegundos) da atualização do perfil |
| `UPDATE_SOURCE` | VARCHAR | A origem da atualização do atributo (API, SDK, dashboard, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Quando os dados foram atualizados pela última vez no Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Seu próprio identificador de usuário (se definido) |
| `FIRST_NAME` | VARCHAR | Nome do usuário |
| `LAST_NAME` | VARCHAR | Sobrenome do usuário |
| `EMAIL_ADDRESS` | VARCHAR | Endereço de e-mail do usuário |
| `GENDER` | VARCHAR | Gênero do usuário |
| `PHONE_NUMBER` | VARCHAR | Número de telefone do usuário |
| `DOB` | VARCHAR | Data de nascimento do usuário |
| `TIME_ZONE` | VARCHAR | Fuso horário do usuário |
| `HOME_CITY` | VARCHAR | Cidade do usuário |
| `COUNTRY` | VARCHAR | País do usuário |
| `LANGUAGE` | VARCHAR | Preferência de idioma do usuário |
| `EFF_DT` | TIMESTAMP_NTZ | Data efetiva: quando esse estado do atributo começou |
| `END_DT` | TIMESTAMP_NTZ | Data final: quando esse estado do atributo terminou (NULL para o estado atual) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de USERDEFAULTATTRIBUTESHISTORYVIEWSHARED" }

### Esquema de `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_custom_attributes_history_view_shared-schema}

{% include partners/snowflake_user_attributes_custom_view_schemas.md schema="history" %}

## Casos de uso comuns {#common-use-cases}

### Criando Segments de usuários {#building-user-segments}

```sql
-- Find active users in a specific city who haven't received an email recently
SELECT
  d.EXTERNAL_USER_ID,
  d.EMAIL_ADDRESS,
  d.HOME_CITY,
  c.CUSTOM_ATTRIBUTES:last_email_sent::TIMESTAMP as last_email_sent
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c
  ON d.USER_ID = c.USER_ID
WHERE d.HOME_CITY = 'New York'
  AND d.EMAIL_ADDRESS IS NOT NULL
  AND (c.CUSTOM_ATTRIBUTES:last_email_sent::TIMESTAMP < DATEADD(day, -30, CURRENT_TIMESTAMP())
       OR c.CUSTOM_ATTRIBUTES:last_email_sent IS NULL);
```

### Analisando o comportamento do usuário ao longo do tempo {#analyzing-user-behavior-over-time}

```sql
-- Track how a user's loyalty tier changed over the past 6 months
SELECT
  USER_ID,
  CUSTOM_ATTRIBUTES:loyalty_tier::STRING as loyalty_tier,
  EFF_DT,
  END_DT
FROM USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED
WHERE USER_ID = 'user_123'
  AND EFF_DT >= DATEADD(month, -6, CURRENT_TIMESTAMP())
ORDER BY EFF_DT DESC;
```

### Combinando atributos padrão e personalizados {#combining-default-and-custom-attributes}

```sql
-- Get a complete user profile with both default and custom attributes
SELECT
  d.EXTERNAL_USER_ID,
  d.FIRST_NAME,
  d.LAST_NAME,
  d.EMAIL_ADDRESS,
  d.COUNTRY,
  c.CUSTOM_ATTRIBUTES:subscription_status::STRING as subscription_status,
  c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER as lifetime_value,
  c.CUSTOM_ATTRIBUTES:last_purchase_date::DATE as last_purchase_date
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
LEFT JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c
  ON d.USER_ID = c.USER_ID
WHERE d.EXTERNAL_USER_ID = 'customer_456';
```

### Encontrando clientes de alto valor {#finding-high-value-customers}

```sql
-- Identify users with high lifetime value who are at risk of churning
SELECT
  d.EXTERNAL_USER_ID,
  d.EMAIL_ADDRESS,
  c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER as lifetime_value,
  c.CUSTOM_ATTRIBUTES:days_since_last_purchase::NUMBER as days_since_last_purchase
FROM USER_DEFAULT_ATTRIBUTES_VIEW_SHARED d
JOIN USER_CUSTOM_ATTRIBUTES_VIEW_SHARED c
  ON d.USER_ID = c.USER_ID
WHERE c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER > 1000
  AND c.CUSTOM_ATTRIBUTES:days_since_last_purchase::NUMBER > 90
ORDER BY c.CUSTOM_ATTRIBUTES:lifetime_value::NUMBER DESC;
```

## Boas práticas {#best-practices}

### Uso recomendado de consultas {#recommended-query-usage}

| Caso de uso                                               | Views recomendadas                                   | Notas                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Consultas gerais** que não exigem atualizações recentes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` e `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Execução rápida, com dados de até 12 horas atrás.                          |
| Consultas que exigem os **atributos de usuário mais recentes**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` e `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Fornece atualizações quase em tempo real, mas pode ser mais lenta para grandes conjuntos de dados. |
| **Rastreamento histórico** de alterações de atributos           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` e `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Armazena alterações de atributos com granularidade de 12 horas.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Uso recomendado de consultas" }

### Considerações de desempenho {#performance-considerations}

* Consultas em `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` devem retornar em menos de 10 segundos para grandes conjuntos de dados (~1 bilhão de usuários) em um warehouse de grande porte.
* Consultas em `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` para um único usuário retornam em menos de um minuto, mas escalam mal sem filtragem por `USER_ID`.
* Consultas com mais de 100 milhões de usuários em `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` podem levar vários minutos devido à agregação por usuário.