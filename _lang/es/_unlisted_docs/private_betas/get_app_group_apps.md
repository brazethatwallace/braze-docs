---
nav_title: "GET: Listar aplicaciones del espacio de trabajo"
layout: api_page
page_type: reference
hidden: true
permalink: /get_app_group_apps/

platform: API
description: "Este artículo describe los detalles del punto de conexión de Braze para listar las aplicaciones del espacio de trabajo."
---
{% api %}
# Listar aplicaciones del espacio de trabajo {#list-workspace-apps}
{% apimethod get %}
/app_group/apps
{% endapimethod %}

> Utiliza este punto de conexión para listar el nombre y el identificador único (`api_key`) de las aplicaciones de un espacio de trabajo.

Acceder a este punto de conexión devuelve una matriz de objetos llamada `apps`. Cada objeto en `apps` contiene el nombre y el identificador único de la aplicación.

{% apiref postman %}  {% endapiref %}

## Límite de velocidad {#rate-limit}

Este punto de conexión tiene un límite de velocidad de 100 solicitudes por día (24 horas).

## Parámetros de la solicitud {#request-parameters}

Esta solicitud no acepta parámetros.

## Ejemplo de solicitud {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/app_group/apps' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Respuesta {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "apps": [
        {
          "name": "App Name",
          "api_key": 00000000-0000-0000-0000-000000000000
        }
    ],
    "message": "success"
}
```

### Solución de problemas {#troubleshooting}

La siguiente tabla enumera los posibles errores devueltos y los pasos de solución de problemas asociados.

| Error | Solución de problemas |
| --- | --- |
| `401: Unauthorized` | La clave de API no tiene los permisos necesarios. Asegúrate de que tu clave de API tenga permisos de `apps.get`. |
| `403: Forbidden` | El conmutador de características no está activado para esta empresa. Ponte en contacto con tu administrador del éxito del cliente para obtener ayuda. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}