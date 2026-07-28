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

{% alert important %}
El conector Braze Currents Streaming está en beta. Ponte en contacto con el soporte de Treasure Data para habilitarlo en tu cuenta de Treasure Data. Para obtener detalles de configuración del lado del partner, consulta la [integración de importación de Braze Currents](https://docs.treasuredata.com/int/braze-currents-import-integration) de Treasure Data.
{% endalert %}

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Treasure Data | Se necesita una [cuenta activa de Treasure Data](https://console.treasuredata.com) para beneficiarse de esta asociación. |
| Currents | Para exportar datos a Treasure Data, debes tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) en tu cuenta. |
| Conector Braze Currents Streaming | Ponte en contacto con el soporte de Treasure Data para habilitar el conector Braze Currents Streaming (beta) en tu cuenta de Treasure Data. |
| Clave de API de escritura de Treasure Data | Una clave de API de escritura de Treasure Data autentica el flujo entrante desde Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Configurar el conector en Treasure Data {#step-1-configure-the-connector-in-treasure-data}

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
| Multiple Tables | Selecciona esta opción para enrutar cada tipo de evento de Braze a su propia tabla |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración de origen" }

5. Después de guardar, copia el **Unique ID** (`task_id`). Necesitarás este valor en el siguiente paso.

### Paso 2: Crear una exportación de Currents personalizada en Braze {#step-2-create-a-custom-currents-export-in-braze}

La opción **Treasure Data Export** en la interfaz de Braze Currents utiliza el método heredado de API Postback y ya no se recomienda. Usa **Custom Currents Export** en su lugar.

1. En Braze, ve a **Partner Integrations** > **Data Export**.
2. Selecciona **Create New Current** > **Custom Currents Export**.
3. Introduce un nombre de integración y un correo electrónico de contacto para notificaciones de errores.
4. En **Credentials**, introduce la URL del endpoint para tu región de Treasure Data. Introduce tu clave de API de escritura de Treasure Data como **Bearer Token**.

| Región | URL del endpoint |
| ------ | ------------ |
| US | `https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID}` |
| EU | `https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID}` |
| AP02 | `https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID}` |
| Tokyo | `https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLs de endpoint por región" }

Reemplaza `{TASK_ID}` con el Unique ID que copiaste en el [Paso 1](#step-1-configure-the-connector-in-treasure-data).

5. Selecciona los tipos de eventos que deseas exportar. Las conexiones de Currents personalizadas pueden enviar eventos tanto para usuarios identificados como para usuarios sin un `external_user_id`. Treasure Data ingesta ambos.
6. Selecciona **Launch Current**.

{% alert warning %}
Mantén actualizados tu clave de API de escritura de Treasure Data y la URL del endpoint. Si el endpoint no es accesible durante más de **5&nbsp;días**, Braze descarta los eventos del conector y los datos se pierden permanentemente.
{% endalert %}

## Consultar tus datos {#query-your-data}

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
El campo `time` en Treasure Data es la marca de tiempo en la que Treasure Data recibió y procesó el evento, no el momento original de ocurrencia del evento en Braze.
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

| Tipo JSON | Tipo de columna en Treasure Data |
| --------- | ------------------------- |
| string | string |
| number | long |
| boolean | string |
| array | JSON string |
| object (nivel 1) | `field_name` |
| object (nivel 2) | `parent_field_name_field_name` |
| null | omitido |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mapeado de tipos de datos" }

Los nombres de columna usan solo letras minúsculas y guiones bajos.

## Límites {#limits}

| Elemento | Límite |
| ---- | ----- |
| Tamaño máximo de carga útil | 1&nbsp;MB por solicitud |
| Tamaño de lote | 100 eventos por lote (predeterminado) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Límites" }

## Detalles de la integración {#integration-details}

Braze admite la exportación a Treasure Data de todos los datos enumerados en los [glosarios de eventos de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), incluidas todas las propiedades tanto de los eventos de [interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) como de [comportamiento del cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

La estructura de la carga útil de los datos exportados es la misma que la de los conectores HTTP personalizados. Puedes revisar cargas útiles de ejemplo en el [repositorio de ejemplos de conectores HTTP personalizados](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Migrar desde el método heredado de Postback {#migrate-from-the-legacy-postback-method}

Si anteriormente usabas **Treasure Data Export** (Postback) en Braze:

1. Completa la configuración de la exportación de Currents personalizada en este artículo.
2. Confirma que los eventos están fluyendo a la nueva tabla.
3. Desactiva el Current basado en Postback anterior en Braze.

Los datos heredados almacenados como arrays JSON sin procesar aún pueden consultarse con `JSON_PARSE` y `UNNEST`. Los nuevos datos ingestados a través del conector de streaming usan el esquema plano descrito en [Esquema de datos](#data-schema).