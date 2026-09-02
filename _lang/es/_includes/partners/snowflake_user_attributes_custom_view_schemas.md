{% if include.schema == "history" %}

| Nombre de columna     | Tipo de datos     | Descripción |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | El identificador de tu espacio de trabajo de Braze |
| `USER_ID` | VARCHAR | El identificador único de usuario de Braze |
| `APP_ID` | VARCHAR | La aplicación específica dentro de tu espacio de trabajo |
| `EXTERNAL_USER_ID` | VARCHAR | Tu propio identificador de usuario (si está configurado) |
| `TIME` | NUMBER | Marca de tiempo unix (segundos) de la actualización del perfil |
| `TIME_MS` | NUMBER | Marca de tiempo unix (milisegundos) de la actualización del perfil |
| `UPDATE_SOURCE` | VARCHAR | La fuente de la actualización del atributo (API, SDK or kit de desarrollo de software, panel, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Cuándo se actualizaron los datos por última vez en Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | Objeto JSON que contiene todos los atributos personalizados (pares clave-valor) |
| `ARCHIVED` | BOOLEAN | Si el perfil de usuario está archivado |
| `EFF_DT` | TIMESTAMP_NTZ | Fecha efectiva: cuándo comenzó este estado de atributo |
| `END_DT` | TIMESTAMP_NTZ | Fecha de fin: cuándo terminó este estado de atributo (NULL para el estado actual) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de USERCUSTOMATTRIBUTESHISTORYVIEWSHARED" }

{% elsif include.schema == "latest" %}

| Nombre de columna     | Tipo de datos     | Descripción |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | El identificador de tu espacio de trabajo de Braze |
| `USER_ID` | VARCHAR | El identificador único de usuario de Braze |
| `EXTERNAL_USER_ID` | VARCHAR | Tu propio identificador de usuario (si está configurado) |
| `TIME` | NUMBER | Marca de tiempo unix (segundos) de la actualización del perfil |
| `TIME_MS` | NUMBER | Marca de tiempo unix (milisegundos) de la actualización del perfil |
| `UPDATE_SOURCE` | VARCHAR | La fuente de la actualización del atributo (API, SDK or kit de desarrollo de software, panel, etc.) |
| `ARCHIVED` | BOOLEAN | Si el perfil de usuario está archivado |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Cuándo se actualizaron los datos por última vez en Snowflake |
| `APP_ID` | VARCHAR | La aplicación específica dentro de tu espacio de trabajo |
| `CUSTOM_ATTRIBUTES` | OBJECT | Objeto JSON que contiene todos los atributos personalizados (pares clave-valor) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED" }

{% alert note %}
Esta vista utiliza el tipo `OBJECT` para `CUSTOM_ATTRIBUTES` en lugar de `VARIANT`. Usa la misma sintaxis de acceso JSON (`:attribute_name::TYPE`) para consultar atributos individuales.
{% endalert %}

{% endif %}