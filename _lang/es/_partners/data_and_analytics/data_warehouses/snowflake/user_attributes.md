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

## Paridad de datos con el dashboard {#data-parity-with-the-dashboard}

En circunstancias excepcionales, los valores de atributos predeterminados y personalizados en las vistas de Snowflake de esta página pueden no coincidir con lo que ves en el perfil de un usuario en el panel de Braze.

Por ejemplo, un atributo puede aparecer como `NULL` en Snowflake mientras que el dashboard muestra un valor para ese usuario.

Si observas discrepancias generalizadas, ponte en contacto con tu administrador del éxito del cliente o con el soporte de Braze.

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
      <td>Instantáneas del perfil de usuario</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Perfiles de usuario en tiempo real</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historial de cambios</td>
    </tr>
    <tr>
      <td rowspan="3">Atributo personalizado</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>Instantáneas del perfil de usuario</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>Perfiles de usuario en tiempo real</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>Historial de cambios</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Vistas disponibles" }

## Instantáneas del perfil de usuario {#user-profile-snapshots}

Estas vistas proporcionan instantáneas periódicas de los atributos del perfil de usuario. Los datos se retrasan hasta 12 horas, por lo que resultan útiles para consultas que no requieren actualizaciones en tiempo real.

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### Uso {#usage}

* Proporciona una instantánea de los atributos del usuario con un **retraso de hasta 12 horas**.
* Funciona bien para consultas que no requieren precisión en tiempo real.
* Ejecución más rápida de la consulta, sobre todo al filtrar por atributos distintos de `USER_ID`.
* **Limitación:** Los datos no están actualizados en tiempo real.

{% alert note %}
El campo `TIME` representa la hora en segundos de la actualización del perfil de usuario; el campo `TIME_MS` indica lo mismo con precisión de milisegundos. Para los datos rellenados retroactivamente, los valores de `TIME` y `TIME_MS` corresponden a la hora del relleno retroactivo.
{% endalert %}

### Esquema de `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_default_attributes_view_shared-schema}

| Nombre de columna | Tipo de datos |
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

| Nombre de columna | Tipo de datos |
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

## Vistas del perfil de usuario en tiempo real {#real-time-user-profile-views}

Estas vistas proporcionan actualizaciones casi en tiempo real de los atributos del perfil de usuario, con datos retrasados hasta 10 minutos después de que se produzca una actualización en Braze.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### Uso

* Proporciona atributos de usuario actualizados con un retraso mínimo (~10 minutos).
* Útil para análisis en tiempo real y situaciones en las que se necesitan datos recientes.
* **Consideraciones de rendimiento:**
    * Las consultas sobre usuarios individuales son más rápidas (menos de un minuto utilizando un almacén grande).
    * Las consultas sin filtros de USER_ID requieren la agregación de todos los usuarios, lo que conlleva tiempos de ejecución significativamente más largos.
    * Las consultas en un gran conjunto de datos (como más de 100 millones de usuarios) pueden tardar muchos minutos.

{% alert note %}
El campo `TIME` representa la hora en segundos de la actualización del perfil de usuario; el campo `TIME_MS` indica lo mismo con precisión de milisegundos. Para los datos rellenados retroactivamente, los valores de `TIME` y `TIME_MS` corresponden a la hora del relleno retroactivo.
{% endalert %}

### Esquema de `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` {#user_latest_state_default_attributes_view_shared-schema}

| Nombre de columna | Tipo de datos |
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

| Nombre de columna | Tipo de datos |
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

## Historial de cambios {#historical-change-logs}

Estas vistas almacenan registros de cambios históricos de los atributos de los usuarios, capturando los cambios con una granularidad de 12 horas.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### Uso

* Proporciona un registro de los cambios históricos en los atributos de los usuarios durante un periodo continuo de 6 meses.
* Los datos se capturan en instantáneas cada 12 horas, lo que significa que varias actualizaciones en esta ventana se combinan en un único registro. Los cambios individuales dentro de este periodo no se conservan por separado.
* `EFF_DT` y `END_DT` marcan el inicio y el final del estado de atributo de un usuario.

{% alert note %}
El campo `TIME` representa la hora en segundos de la actualización del perfil de usuario; el campo `TIME_MS` indica lo mismo con precisión de milisegundos. Para los datos rellenados retroactivamente, los valores de `TIME` y `TIME_MS` corresponden a la hora del relleno retroactivo.
{% endalert %}

### Esquema de `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` {#user_default_attributes_history_view_shared-schema}

| Nombre de columna | Tipo de datos |
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

| Nombre de columna | Tipo de datos |
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

## Buenas prácticas {#best-practices}

### Uso recomendado de consultas {#recommended-query-usage}

| Caso de uso | Vistas recomendadas | Notas |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| **Consultas generales** que no requieren actualizaciones recientes | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` y `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` | Ejecución rápida, con datos de hasta 12 horas de antigüedad. |
| Consultas que requieren los **últimos atributos del usuario** | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` y `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | Proporciona actualizaciones casi en tiempo real, pero puede ser más lento para grandes conjuntos de datos. |
| **Seguimiento histórico** de los cambios de atributos | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` y `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` | Almacena los cambios de atributos con una granularidad de 12 horas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Uso recomendado de consultas" }

### Consideraciones de rendimiento {#performance-considerations}

* Las consultas en `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` o `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` deberían dar resultados en menos de 10 segundos para grandes conjuntos de datos (~1000 millones de usuarios) en un almacén grande.
* Las consultas en `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` o `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED ` para un solo usuario se devuelven en menos de un minuto, pero escalan mal sin filtrar por `USER_ID`.
* Las consultas sobre más de 100 millones de usuarios en `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` o `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` pueden tardar varios minutos debido a la agregación por usuario.