---
nav_title: Treasure Data para Currents
article_title: Treasure Data para Currents
description: "Este artículo de referencia describe la asociación entre Braze Currents y Treasure Data, una plataforma de datos de clientes empresariales que transmite datos de eventos de Braze a Treasure Data para su análisis y activación."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data para Currents {#treasure-data-for-currents}

> [Treasure Data](https://www.treasuredata.com/) es una plataforma de datos de clientes (CDP) que recopila y encamina información de múltiples fuentes a una variedad de otras ubicaciones en tu stack de marketing.

La integración de Braze y Treasure Data te permite controlar el flujo de información entre ambos sistemas. Con Currents, puedes transmitir datos de eventos de Braze a Treasure Data y hacerlos procesables en todo tu stack de crecimiento.

El método recomendado es el conector **Braze Currents Streaming** en Treasure Data, combinado con una **exportación de Currents personalizada** en Braze. Este enfoque proporciona:

- Transmisión de eventos en tiempo real desde Braze a Treasure Data
- Enrutamiento automático opcional de tablas por tipo de evento
- Un esquema plano consultable con SQL que no requiere análisis de JSON

{% alert note %}
El conector Braze Currents Streaming está disponible bajo solicitud. Ponte en contacto con el soporte de Treasure Data para habilitarlo en tu cuenta de Treasure Data. Para obtener detalles de configuración del lado del partner, consulta la [integración de importación de Braze Currents](https://docs.treasuredata.com/int/braze-currents-import-integration) de Treasure Data.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Treasure Data | Se requiere una [cuenta activa de Treasure Data](https://console.treasuredata.com) para aprovechar esta integración. |
| Currents | Para exportar datos a Treasure Data, necesitas tener [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) configurado en tu cuenta. |
| Conector de streaming de Braze Currents | Ponte en contacto con el soporte de Treasure Data para habilitar el conector de streaming de Braze Currents en tu cuenta de Treasure Data. |
| Clave de API de escritura de Treasure Data | Una clave de API de escritura de Treasure Data autentica el flujo de entrada desde Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Configura el conector en Treasure Data {#step-1-configure-the-connector-in-treasure-data}

1. En la consola de Treasure Data, ve a **Connections** > **New Connection**.
2. Selecciona **Braze Currents Streaming**.
3. En **Authentication**, introduce tu clave de API de escritura de Treasure Data.
4. En **Source Settings**, configura lo siguiente:

| Campo | Descripción |
| ----- | ----------- |
| Source Name | Un nombre descriptivo para esta conexión |
| Datastore | Selecciona **Plazma** |
| Database | La base de datos de Treasure Data donde se almacenan los eventos |
| Table | La tabla de destino predeterminada |
| Multiple Tables | Selecciona esta opción para dirigir cada tipo de evento de Braze a su propia tabla |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración de origen" }

5. Después de guardar, copia el **Unique ID** (`task_id`). Necesitas este valor en el siguiente paso.

### Paso 2: Crea una exportación de Currents personalizada en Braze {#step-2-create-a-custom-currents-export-in-braze}

La opción **Treasure Data Export** en la interfaz de Braze Currents utiliza el método heredado de Postback API y ya no se recomienda. Usa **Custom Currents Export** en su lugar.

1. En Braze, ve a **Partner Integrations** > **Data Export**.
2. Selecciona **Create New Current** > **Custom Currents Export**.
3. Introduce un nombre de integración y un correo electrónico de contacto para las notificaciones de errores.
4. En **Credentials**, introduce la URL del endpoint para tu región de Treasure Data. Introduce tu clave de API de escritura de Treasure Data como **Bearer Token**.

| Región | URL del endpoint |
| ------ | ---------------- |
| US | `https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID}` |
| EU | `https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID}` |
| AP02 | `https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID}` |
| Tokyo | `https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs de endpoints por región" }

Reemplaza `{TASK_ID}` con el Unique ID que copiaste en el [Paso 1](#step-1-configure-the-connector-in-treasure-data).

5. Selecciona los tipos de eventos que deseas exportar. Las conexiones de Currents personalizadas pueden enviar eventos para usuarios identificados y para usuarios sin un `external_user_id`. Treasure Data ingiere ambos.
6. Selecciona **Launch Current**.

{% alert warning %}
Mantén tu clave de API de escritura de Treasure Data y la URL del endpoint actualizadas. Si el endpoint no es accesible durante más de **5&nbsp;días**, Braze descarta los eventos del conector y los datos se pierden de forma permanente.
{% endalert %}

## Consulta tus datos {#query-your-data}

Una vez que los eventos estén fluyendo, consúltalos con SQL. Treasure Data aplana la carga útil, por lo que no necesitas analizar JSON.

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
El campo `time` en Treasure Data es la marca de tiempo en que Treasure Data recibió y procesó el evento, no la hora de ocurrencia original del evento en Braze.
{% endalert %}

Si seleccionaste **Multiple Tables**, cada tipo de evento se almacena en su propia tabla (por ejemplo, `users_message_email_open` o `users_behaviors_purchase`).

Para confirmar que los datos están llegando, ejecuta una consulta de conteo unos minutos después de lanzar el Current:

```sql
SELECT COUNT(*)
FROM your_table
WHERE TD_INTERVAL(time, '-1h')
```

## Esquema de datos {#data-schema}

Treasure Data aplana el JSON anidado hasta dos niveles de profundidad:

| Tipo de JSON | Tipo de columna en Treasure Data |
| --------- | ------------------------- |
| string | string |
| number | long |
| boolean | string |
| array | cadena JSON |
| object (nivel 1) | `field_name` |
| object (nivel 2) | `parent_field_name_field_name` |
| null | omitido |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mapeado de tipos de datos" }

Los nombres de columna solo utilizan letras minúsculas y guiones bajos.

## Límites {#limits}

| Elemento | Límite |
| ---- | ----- |
| Tamaño máximo de la carga útil | 1&nbsp;MB por solicitud |
| Tamaño del lote | 100 eventos por lote (predeterminado) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Límites" }

## Detalles de la integración {#integration-details}

Braze permite exportar todos los datos enumerados en los [glosarios de eventos de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) a Treasure Data. Esto incluye todas las propiedades tanto en los eventos de [participación en mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) como en los de [comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

La estructura de la carga útil de los datos exportados coincide con la estructura de carga útil de los conectores HTTP personalizados. Puedes revisar ejemplos de cargas útiles en el [repositorio de ejemplos para conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Migración desde el método legacy de Postback {#migrate-from-the-legacy-postback-method}

Si anteriormente usabas **Treasure Data Export** (Postback) en Braze:

1. Completa la configuración de Custom Currents Export en este artículo.
2. Confirma que los eventos fluyen hacia la nueva tabla.
3. Deshabilita el antiguo Current basado en Postback en Braze.

Los datos legacy almacenados como arreglos JSON sin procesar aún pueden consultarse con `JSON_PARSE` y `UNNEST`. Los nuevos datos ingeridos a través del conector de streaming usan el esquema plano descrito en [Esquema de datos](#data-schema).