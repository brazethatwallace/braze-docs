---
nav_title: "GET: Estado de la sincronización de trabajos"
article_title: "GET: Estado de sincronización de trabajos"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_job_sync/
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Listar estado de sincronización de trabajos de Braze."

---
{% api %}
# Listar estado de sincronización de trabajos {#list-job-sync-status}
{% apimethod get %}
/cdi/integrations/{integration_id}/job_sync_status
{% endapimethod %}

> Usa este punto de conexión para devolver una lista de estados de sincronización anteriores para una integración determinada.

{% alert note %}
Para usar este punto de conexión, deberás generar una clave de API con el permiso `cdi.integration_job_status`.
{% endalert %}

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='cdi job sync status' %}

## Parámetros de la ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `integration_id` | Obligatorio | Cadena | ID de integración. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de la ruta" }

## Parámetros de consulta {#query-parameters}

Cada llamada a este punto de conexión devolverá 10 elementos. Para una integración con más de 10 sincronizaciones, usa el encabezado `Link` para recuperar los datos en la página siguiente, como se muestra en el siguiente ejemplo de respuesta.

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `cursor` | Opcional | Cadena | Determina la paginación del estado de sincronización. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta" }

## Ejemplo de solicitud {#example-request}

### Sin cursor {#without-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Con cursor {#with-cursor}

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

### Ejemplo de respuesta correcta {#example-success-response}

El código de estado `200` podría devolver el siguiente cuerpo de respuesta.

{% alert note %}
El encabezado `Link` no existirá si hay 10 sincronizaciones o menos en total. En las llamadas sin cursor, `prev` no se mostrará. Al consultar la última página de elementos, `next` no se mostrará.
{% endalert %}

```
Link: </cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow>; rel="prev",</cdi/integrations00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
        "job_status": (string) status of the sync, see below for explanation of different statuses,
        "sync_start_time": (string) time the sync started in ISO 8601,
        "sync_finish_time": (string) time the sync finished in ISO 8601,
        "last_timestamp_synced": (string) last UPDATED_AT timestamp processed by the sync in ISO 8601,
        "rows_synced": (integer) number of rows successfully synced to Braze,
        "rows_failed_with_errors": (integer) number of rows failed because of errors
    }
  ],
  "message": "success"
}
```

| job_status | Explicación |
| --- | --- |
| `running` | El trabajo se está ejecutando actualmente. |
| `success` | Todas las filas se sincronizaron correctamente. |
| `partial` | Algunas filas no se sincronizaron debido a errores. |
| `error` | No se sincronizó ninguna fila. |
| `config_error` | Se produjo un error en la configuración de la integración. Comprueba tu configuración de integración. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ejemplo de respuesta correcta" }

## Solución de problemas {#troubleshooting}

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `400 Invalid cursor` | Comprueba que tu `cursor` es válido. |
| `400 Invalid integration ID` | Comprueba que tu `integration_id` es válido. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

Para obtener más códigos de estado y mensajes de error asociados, consulta [Errores fatales y respuestas]({{site.baseurl}}/api/errors#fatal-errors).

{% endapi %}