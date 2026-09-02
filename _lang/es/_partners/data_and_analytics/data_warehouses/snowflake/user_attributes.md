---
nav_title: "Atributos del perfil de usuario"
article_title: Vistas de atributos de usuario en Snowflake
page_order: 10
page_type: partner
search_tag: Partner
toc_headers: h2
---

# Atributos del perfil de usuario {#user-profile-attributes}

> Esta página sirve de referencia para las vistas de atributos predeterminados y personalizados en Snowflake. Hay tres vistas para atributos predeterminados y tres vistas para atributos personalizados, cada una diseñada para un caso de uso específico con sus propias consideraciones de rendimiento.

## Paridad de datos con el panel {#data-parity-with-the-dashboard}

En circunstancias excepcionales, los valores de atributos predeterminados y personalizados en las vistas de Snowflake de esta página pueden no coincidir con lo que ves en el perfil de un usuario en el panel de Braze.

Por ejemplo, un atributo puede aparecer como `NULL` en Snowflake mientras que el panel muestra un valor para ese usuario.

Si observas discrepancias generalizadas, contacta a tu CSM or administrador de éxito de cliente or administrador de éxito de cliente o a soporte de Braze.

## Vistas disponibles {#available-views}

<table aria-label="Vistas disponibles">
  <caption>Vistas disponibles</caption>
  <thead>
    <tr>
      <th>Tipo</th>
      <th>Vista</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Atributo predeterminado</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantáneas de perfiles de usuario</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Perfiles de usuario en tiempo real</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Registros de cambios históricos</td>
    </tr>
    <tr>
      <td rowspan="3">Atributo personalizado</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantáneas de perfiles de usuario</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Perfiles de usuario en tiempo real</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Registros de cambios históricos</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Vistas disponibles" }

## Instantáneas del perfil de usuario {#user-profile-snapshots}

Estas vistas proporcionan instantáneas periódicas de los atributos del perfil de usuario. Los datos tienen un retraso de hasta 12 horas, lo que las hace útiles para consultas que no requieren actualizaciones en tiempo real.

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### Uso {#usage}

* Proporciona una instantánea de los atributos de usuario con un retraso de hasta **12 horas**.
* Funciona bien para consultas que no requieren precisión en tiempo real.
* Ejecución de consultas más rápida, especialmente al filtrar por atributos distintos de `USER_ID`.
* **Limitación:** Los datos no están actualizados en tiempo real.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Esquema de `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_default_attributes_view_shared-schema}

| Nombre de columna | Tipo de datos | Descripción |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | El identificador de tu espacio de trabajo de Braze |
| `APP_ID` | VARCHAR | La aplicación específica dentro de tu espacio de trabajo |
| `USER_ID` | VARCHAR | El identificador único de usuario de Braze |
| `TIME` | NUMBER | Marca de tiempo unix (segundos) de la actualización del perfil |
| `TIME_MS` | NUMBER | Marca de tiempo unix (milisegundos) de la actualización del perfil |
| `UPDATE_SOURCE` | VARCHAR | La fuente de la actualización del atributo (API, SDK or kit de desarrollo de software, panel, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Cuándo se actualizaron los datos por última vez en Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Tu propio identificador de usuario (si está configurado) |
| `FIRST_NAME` | VARCHAR | Nombre del usuario |
| `LAST_NAME` | VARCHAR | Apellido del usuario |
| `EMAIL_ADDRESS` | VARCHAR | Dirección de correo electrónico del usuario |
| `GENDER` | VARCHAR | Género del usuario |
| `PHONE_NUMBER` | VARCHAR | Número de teléfono del usuario |
| `DOB` | VARCHAR | Fecha de nacimiento del usuario |
| `TIME_ZONE` | VARCHAR | Zona horaria del usuario |
| `HOME_CITY` | VARCHAR | Ciudad de residencia del usuario |
| `COUNTRY` | VARCHAR | País del usuario |
| `LANGUAGE` | VARCHAR | Preferencia de idioma del usuario |
| `ARCHIVED` | BOOLEAN | Si el perfil de usuario está archivado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de USERDEFAULTATTRIBUTESVIEWSHARED" }


### Esquema de `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` {#user_custom_attributes_view_shared-schema}

| Nombre de columna | Tipo de datos | Descripción |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | El identificador de tu espacio de trabajo de Braze |
| `APP_ID` | VARCHAR | La aplicación específica dentro de tu espacio de trabajo |
| `USER_ID` | VARCHAR | El identificador único de usuario de Braze |
| `EXTERNAL_USER_ID` | VARCHAR | Tu propio identificador de usuario (si está configurado) |
| `TIME` | NUMBER | Marca de tiempo unix (segundos) de la actualización del perfil |
| `TIME_MS` | NUMBER | Marca de tiempo unix (milisegundos) de la actualización del perfil |
| `UPDATE_SOURCE` | VARCHAR | La fuente de la actualización del atributo (API, SDK or kit de desarrollo de software, panel, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Cuándo se actualizaron los datos por última vez en Snowflake |
| `CUSTOM_ATTRIBUTES` | VARIANT | Objeto JSON que contiene todos los atributos personalizados (pares clave-valor) |
| `ARCHIVED` | BOOLEAN | Si el perfil de usuario está archivado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de USERCUSTOMATTRIBUTESVIEWSHARED" }

#### Trabajar con CUSTOM_ATTRIBUTES {#working-with-custom_attributes}

La columna `CUSTOM_ATTRIBUTES` almacena todos tus atributos personalizados como un objeto JSON. Puedes acceder a atributos individuales utilizando las funciones JSON de Snowflake.

**Ejemplo: Consultar atributos personalizados específicos**

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

**Ejemplo: Analizar datos de atributos personalizados**

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

## Vistas de perfil de usuario en tiempo real {#real-time-user-profile-views}

Estas vistas proporcionan actualizaciones casi en tiempo real de los atributos del perfil de usuario, con datos retrasados hasta 10 minutos después de que se produce una actualización en Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### Uso

* Proporciona atributos de usuario actualizados con un retraso mínimo (~10 minutos).
* Útil para análisis en tiempo real y escenarios en los que se requieren datos recientes.
* **Consideraciones de rendimiento:**
    * Las consultas sobre usuarios individuales son más rápidas (menos de un minuto usando un almacén grande).
    * Las consultas sin filtros de USER_ID requieren agregación entre todos los usuarios, lo que genera tiempos de ejecución significativamente más largos.
    * Las consultas sobre un conjunto de datos grande (como más de 100 millones de usuarios) pueden tardar muchos minutos.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Esquema de `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_latest_state_default_attributes_view_shared-schema}

| Nombre de columna | Tipo de datos | Descripción |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | El identificador de tu espacio de trabajo de Braze |
| `APP_ID` | VARCHAR | La aplicación específica dentro de tu espacio de trabajo |
| `USER_ID` | VARCHAR | El identificador único de usuario de Braze |
| `TIME` | NUMBER | Marca de tiempo unix (segundos) de la actualización del perfil |
| `TIME_MS` | NUMBER | Marca de tiempo unix (milisegundos) de la actualización del perfil |
| `UPDATE_SOURCE` | VARCHAR | La fuente de la actualización del atributo (API, SDK or kit de desarrollo de software, panel, etc.) |
| `ARCHIVED` | BOOLEAN | Si el perfil de usuario está archivado |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ | Cuándo se actualizaron los datos por última vez en Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Tu propio identificador de usuario (si está configurado) |
| `FIRST_NAME` | VARCHAR | Nombre del usuario |
| `LAST_NAME` | VARCHAR | Apellido del usuario |
| `EMAIL_ADDRESS` | VARCHAR | Dirección de correo electrónico del usuario |
| `GENDER` | VARCHAR | Género del usuario |
| `PHONE_NUMBER` | VARCHAR | Número de teléfono del usuario |
| `DOB` | VARCHAR | Fecha de nacimiento del usuario |
| `HOME_CITY` | VARCHAR | Ciudad de residencia del usuario |
| `COUNTRY` | VARCHAR | País del usuario |
| `LANGUAGE` | VARCHAR | Preferencia de idioma del usuario |
| `TIME_ZONE` | VARCHAR | Zona horaria del usuario |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED" }

### Esquema de `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` {#user_latest_state_custom_attribute_view_shared-schema}

{% include partners/snowflake_user_attributes_custom_view_schemas.md schema="latest" %}

## Registros de cambios históricos {#historical-change-logs}

Estas vistas almacenan registros de cambios históricos de atributos de usuario, capturando los cambios con una granularidad de 12 horas.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### Uso

* Proporciona un registro de cambios históricos en los atributos de usuario durante un periodo continuo de 6 meses.
* Los datos se capturan en instantáneas cada 12 horas, lo que significa que múltiples actualizaciones en esta ventana se combinan en un único registro. Los cambios individuales dentro de este periodo no se conservan por separado.
* `EFF_DT` y `END_DT` marcan el inicio y el fin del estado de un atributo de usuario.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### Esquema de `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_default_attributes_history_view_shared-schema}

| Nombre de columna | Tipo de datos | Descripción |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | El identificador de tu espacio de trabajo de Braze |
| `USER_ID` | VARCHAR | El identificador único de usuario de Braze |
| `APP_ID` | VARCHAR | La aplicación específica dentro de tu espacio de trabajo |
| `TIME` | NUMBER | Marca de tiempo unix (segundos) de la actualización del perfil |
| `TIME_MS` | NUMBER | Marca de tiempo unix (milisegundos) de la actualización del perfil |
| `UPDATE_SOURCE` | VARCHAR | La fuente de la actualización del atributo (API, SDK or kit de desarrollo de software, panel, etc.) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Cuándo se actualizaron los datos por última vez en Snowflake |
| `EXTERNAL_USER_ID` | VARCHAR | Tu propio identificador de usuario (si está configurado) |
| `FIRST_NAME` | VARCHAR | Nombre del usuario |
| `LAST_NAME` | VARCHAR | Apellido del usuario |
| `EMAIL_ADDRESS` | VARCHAR | Dirección de correo electrónico del usuario |
| `GENDER` | VARCHAR | Género del usuario |
| `PHONE_NUMBER` | VARCHAR | Número de teléfono del usuario |
| `DOB` | VARCHAR | Fecha de nacimiento del usuario |
| `TIME_ZONE` | VARCHAR | Zona horaria del usuario |
| `HOME_CITY` | VARCHAR | Ciudad de residencia del usuario |
| `COUNTRY` | VARCHAR | País del usuario |
| `LANGUAGE` | VARCHAR | Preferencia de idioma del usuario |
| `EFF_DT` | TIMESTAMP_NTZ | Fecha efectiva: cuándo comenzó este estado del atributo |
| `END_DT` | TIMESTAMP_NTZ | Fecha de fin: cuándo terminó este estado del atributo (NULL para el estado actual) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Esquema de USERDEFAULTATTRIBUTESHISTORYVIEWSHARED" }

### Esquema de `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_custom_attributes_history_view_shared-schema}

{% include partners/snowflake_user_attributes_custom_view_schemas.md schema="history" %}

## Ejemplos comunes {#common-use-cases}

### Creación de Segments de usuarios {#building-user-segments}

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

### Análisis del comportamiento de los usuarios a lo largo del tiempo {#analyzing-user-behavior-over-time}

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

### Combinación de atributos predeterminados y personalizados {#combining-default-and-custom-attributes}

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

### Identificación de clientes de alto valor {#finding-high-value-customers}

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

## Buenas prácticas {#best-practices}

### Uso recomendado de consultas {#recommended-query-usage}

| Caso de uso                                               | Vistas recomendadas                                   | Notas                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Consultas generales** que no requieren actualizaciones recientes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` y `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | Ejecución rápida, con datos de hasta 12 horas de antigüedad.                          |
| Consultas que requieren los **atributos de usuario más recientes**       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` y `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Proporciona actualizaciones casi en tiempo real, pero puede ser más lenta para conjuntos de datos grandes. |
| **Seguimiento histórico** de cambios en atributos           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` y `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | Almacena los cambios de atributos con una granularidad de 12 horas.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Uso recomendado de consultas" }

### Consideraciones de rendimiento {#performance-considerations}

* Las consultas en `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` o `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` deberían devolver resultados en menos de 10 segundos para conjuntos de datos grandes (~1000 millones de usuarios) en un almacén de datos grande.
* Las consultas en `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` o `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` para un solo usuario devuelven resultados en menos de un minuto, pero escalan mal sin filtrado por `USER_ID`.
* Las consultas sobre más de 100 millones de usuarios en `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` o `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` pueden tardar varios minutos debido a la agregación por usuario.