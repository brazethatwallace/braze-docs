---
nav_title: "POST: Desencadenar sincronización"
article_title: "POST: Desencadenar sincronización"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del punto de conexión Desencadenar sincronización de Braze."

---
{% api %}
# Desencadenar una sincronización {#trigger-a-sync}
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> Utiliza este punto de conexión para desencadenar una sincronización para una integración determinada.

{% alert note %}
Para utilizar este punto de conexión, debes generar una clave de API con el permiso `cdi.integration_sync`.
{% endalert %}

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## Parámetros de la ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `integration_id` | Obligatorio | Cadena | ID de integración. Se encuentra en la URL cuando se visualiza una integración en el panel de Braze. El formato de la URL es `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de la ruta" }

## Ejemplo de solicitud {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Respuesta {#response}

### Ejemplo de respuesta satisfactoria {#example-success-response}

El código de estado `202` podría devolver el siguiente cuerpo de respuesta:

```json
{
  "message": "success"
}
```

## Solución de problemas {#troubleshooting}

La siguiente tabla enumera los posibles errores devueltos y sus pasos asociados para la solución de problemas.

| Error | Solución de problemas |
| --- | --- |
| `400 Invalid integration ID` | Comprueba que tu `integration_id` es válido. |
| `404 Integration not found` | No existe ninguna integración para el ID de integración dado. Asegúrate de que tu ID de integración es válido. |
| `429 Another job is in progress` | Actualmente se está ejecutando una sincronización para esta integración. Inténtalo de nuevo cuando se haya completado la sincronización. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solución de problemas" }

Para obtener más códigos de estado y mensajes de error asociados, consulta [Errores fatales y respuestas]({{site.baseurl}}/api/errors#fatal-errors).

{% endapi %}