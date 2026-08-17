{% if include.schema == "history" %}

| Nome da coluna     | Tipo de dados     | Descrição |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identificador do seu espaço de trabalho Braze |
| `USER_ID` | VARCHAR | O identificador exclusivo de usuário da Braze |
| `APP_ID` | VARCHAR | O app específico dentro do seu espaço de trabalho |
| `EXTERNAL_USER_ID` | VARCHAR | Seu próprio identificador de usuário (se definido) |
| `TIME` | NUMBER | Timestamp Unix (segundos) da atualização do perfil |
| `TIME_MS` | NUMBER | Timestamp Unix (milissegundos) da atualização do perfil |
| `UPDATE_SOURCE` | VARCHAR | A origem da atualização do atributo (API, SDK, dashboard, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Quando os dados foram atualizados pela última vez no Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | Objeto JSON contendo todos os atributos personalizados (pares chave-valor) |
| `ARCHIVED` | BOOLEAN | Se o perfil de usuário está arquivado |
| `EFF_DT` | TIMESTAMP_NTZ | Data efetiva: quando esse estado de atributo começou |
| `END_DT` | TIMESTAMP_NTZ | Data final: quando esse estado de atributo terminou (NULL para o estado atual) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema USERCUSTOMATTRIBUTESHISTORYVIEWSHARED" }

{% elsif include.schema == "latest" %}

| Nome da coluna     | Tipo de dados     | Descrição |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Identificador do seu espaço de trabalho Braze |
| `USER_ID` | VARCHAR | O identificador exclusivo de usuário da Braze |
| `EXTERNAL_USER_ID` | VARCHAR | Seu próprio identificador de usuário (se definido) |
| `TIME` | NUMBER | Timestamp Unix (segundos) da atualização do perfil |
| `TIME_MS` | NUMBER | Timestamp Unix (milissegundos) da atualização do perfil |
| `UPDATE_SOURCE` | VARCHAR | A origem da atualização do atributo (API, SDK, dashboard, etc.) |
| `ARCHIVED` | BOOLEAN | Se o perfil de usuário está arquivado |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Quando os dados foram atualizados pela última vez no Snowflake |
| `APP_ID` | VARCHAR | O app específico dentro do seu espaço de trabalho |
| `CUSTOM_ATTRIBUTES` | OBJECT | Objeto JSON contendo todos os atributos personalizados (pares chave-valor) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED" }

{% alert note %}
Esta visualização usa o tipo `OBJECT` para `CUSTOM_ATTRIBUTES` em vez de `VARIANT`. Use a mesma sintaxe de acessor JSON (`:attribute_name::TYPE`) para consultar atributos individuais.
{% endalert %}

{% endif %}