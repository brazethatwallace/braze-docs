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

Por exemplo, um atributo pode aparecer como `NULL` no Snowflake enquanto o dashboard mostra um valor para aquele usuário.

Se você perceber incompatibilidades generalizadas, entre em contato com o seu gerente de sucesso do cliente ou com o suporte da Braze.

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
      <td>Instantâneos do perfil de usuário</td>
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
      <td>Instantâneos do perfil de usuário</td>
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

## Instantâneos do perfil de usuário {#user-profile-snapshots}

Essas visualizações fornecem instantâneos periódicos dos atributos do perfil de usuário. Os dados têm um atraso de até 12 horas, o que os torna úteis para consultas que não exigem atualizações em tempo real.

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### Uso {#usage}

* Fornece um instantâneo dos atributos de usuário com um **atraso de até 12 horas**.
* Apresenta bom desempenho para consultas que não exigem precisão em tempo real.
* Execução de consulta mais rápida, especialmente ao filtrar por atributos diferentes de `USER_ID`.
* **Limitação:** os dados não são atualizados em tempo real.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Esquema de `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_default_attributes_view_shared-schema}

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de USERDEFAULTATTRIBUTESVIEWSHARED" }


### Esquema de `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` {#user_custom_attributes_view_shared-schema}

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de USERCUSTOMATTRIBUTESVIEWSHARED" }

## Visualizações do perfil de usuário em tempo real {#real-time-user-profile-views}

Essas visualizações fornecem atualizações quase em tempo real sobre os atributos do perfil de usuário, com um atraso de até 10 minutos após a ocorrência de uma atualização na Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### Uso

* Fornece atributos de usuário atualizados com atraso mínimo (~10 minutos).
* Útil para análises em tempo real e cenários em que dados recentes são necessários.
* **Considerações de desempenho:**
    * Consultas sobre usuários individuais são mais rápidas (menos de um minuto usando um warehouse grande).
    * Consultas sem filtros de USER_ID exigem agregação em todos os usuários, o que leva a tempos de execução significativamente mais longos.
    * Consultas em um grande conjunto de dados (como mais de 100 milhões de usuários) podem levar muitos minutos.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Esquema de `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_latest_state_default_attributes_view_shared-schema}

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIMEZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED" }

### Esquema de `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` {#user_latest_state_custom_attribute_view_shared-schema}

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJECT |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED" }

## Registros históricos de alterações {#historical-change-logs}

Essas visualizações armazenam registros históricos de alterações de atributos de usuário, capturando mudanças com granularidade de 12 horas.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### Uso

* Fornece um registro de alterações históricas nos atributos de usuário por um período contínuo de 6 meses.
* Os dados são capturados a cada 12 horas, o que significa que várias atualizações nesse período são combinadas em um único registro. Alterações individuais dentro desse intervalo não são mantidas separadamente.
* `EFF_DT` e `END_DT` marcam o início e o fim do estado de um atributo do usuário.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Esquema de `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_default_attributes_history_view_shared-schema}

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de USERDEFAULTATTRIBUTESHISTORYVIEWSHARED" }

### Esquema de `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_custom_attributes_history_view_shared-schema}

| Nome da coluna     | Tipo de dados     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Esquema de USERCUSTOMATTRIBUTESHISTORYVIEWSHARED" }

## Melhores práticas {#best-practices}

### Uso recomendado de consultas {#recommended-query-usage}

| Caso de uso                                               | Visualizações recomendadas                                   | Notas                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Consultas gerais** que não requerem atualizações recentes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` e `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Execução rápida, com dados de até 12 horas.                          |
| Consultas que exigem os **atributos de usuário mais recentes**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` e `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Fornece atualizações quase em tempo real, mas pode ser mais lento para grandes conjuntos de dados. |
| **Rastreamento histórico** de alterações de atributos           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` e `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Armazena alterações de atributos com granularidade de 12 horas.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Uso recomendado de consultas" }

### Considerações de desempenho {#performance-considerations}

* Consultas em `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` devem retornar em menos de 10 segundos para grandes conjuntos de dados (~1 bilhão de usuários) em um warehouse grande.
* Consultas em `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` para um único usuário retornam em menos de um minuto, mas escalam mal sem a filtragem por `USER_ID`.
* Consultas sobre mais de 100 milhões de usuários em `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` ou `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` podem levar vários minutos devido à agregação por usuário.