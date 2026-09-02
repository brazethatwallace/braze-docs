---
nav_title: "GET: Buscar una cuenta de usuario existente en el panel"
article_title: "GET: Buscar una cuenta de usuario existente en el panel"
alias: /get_see_user_account_information/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe los detalles sobre el endpoint de Braze para buscar el ID de recurso de una cuenta de usuario existente en el panel."
---

{% api %}
# Buscar una cuenta de usuario existente en el panel por ID de recurso {#look-up-an-existing-dashboard-user-account-by-resource-id}
{% apimethod get %}
/scim/v2/Users/{id}
{% endapimethod %}

> Utiliza este endpoint para buscar una cuenta de usuario existente en el panel especificando el recurso `id` devuelto por el método SCIM [`POST`]({{site.baseurl}}/api/endpoints/scim/post_create_user_account).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#3df40764-8f74-4532-aed3-ab8a6cb92122 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás un token SCIM. Utilizarás el origen de tu servicio como encabezado `X-Request-Origin`. Para más información, consulta [Aprovisionamiento automatizado de usuarios]({{site.baseurl}}/scim/automated_user_provisioning).

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='look up dashboard user' %}

## Parámetros de ruta {#path-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `id` | Obligatorio | Cadena | El ID de recurso del usuario. Este parámetro lo devuelven los métodos `POST` `/scim/v2/Users/` o `GET`  `/scim/v2/Users?filter=userName eq "user@example.com"`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de ruta" }

## Parámetros de la solicitud {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
Si recibes una respuesta `401`, confirma que estás utilizando un token SCIM (no una clave de API REST), que `X-Request-Origin` coincide con el origen de tu servicio y que tu dirección IP está en la lista de permitidos de SCIM. Para más detalles, consulta [Aprovisionamiento automatizado de usuarios]({{site.baseurl}}/scim/automated_user_provisioning).
{% endalert %}

## Ejemplo de solicitud {#example-request}
```bash
curl --location --request GET 'https://rest.iad-01.braze.com/scim/v2/Users/dfa245b7-24195aec-887bb3ad-602b3340' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Respuesta {#response}
```json
{
    "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
    "id": "dfa245b7-24195aec-887bb3ad-602b3340",
    "userName": "user@example.com",
    "name": {
        "givenName": "Test",
        "familyName": "User"
    },
    "department": "finance",
    "lastSignInAt": "2024 Nov 11, 4:20 PM",
    "createdAt": "2024 Nov 11, 4:20 PM",
    "permissions": {
        "companyPermissions": ["manage_company_settings"],
        "roles": [
            {
                "roleName": "Another Test Role",
                "roleId": "23125dad23dfaae7",
                "appGroup": [
                    {
                        "appGroupId": "241adcd25adfabcded",
                        "appGroupName": "Production Workspace",
                        "appGroupPermissionSets": [
                            {
                                "appGroupPermissionSetName": "A Permission Set",
                                "appGroupPermissionSetId": "dfa385109bc38",
                                "permissions": ["basic_access","publish_cards"]
                            }
                        ]
                    }
                ]
            }
        ],
        "appGroup": [
            {
                "appGroupId": "241adcd25789fabcded",
                "appGroupName": "Test Workspace",
                "appGroupPermissions": ["basic_access","send_campaigns_canvases"],
                "team": [
                    {
                         "teamId": "241adcd25789fabcded",
                         "teamName": "Test Team",
                         "teamPermissions": ["admin"]
                    }
                ]
            }
        ]
    }
}
```

## Parámetros de respuesta {#response-parameters}

| Parámetro | Tipo de datos | Descripción |
|---|---|---|
| `schemas` | Matriz de cadenas | Esquema de usuario SCIM. |
| `id` | Cadena | El ID de recurso del usuario. |
| `userName` | Cadena | La dirección de correo electrónico del usuario. |
| `name` | Objeto | Contiene `givenName` y `familyName`. |
| `department` | Cadena | El departamento del usuario, si se ha establecido. |
| `createdAt` | Cadena | Fecha en que se creó la cuenta de usuario. Devuelve `N/A` cuando no se ha establecido; de lo contrario, tiene el formato `YYYY Mon DD, H:MM AM/PM`. |
| `lastSignInAt` | Cadena | Fecha en que el usuario inició sesión por última vez. Devuelve `N/A` si el usuario no ha iniciado sesión; de lo contrario, tiene el formato `YYYY Mon DD, H:MM AM/PM`. |
| `permissions` | Objeto | Permisos de empresa, espacio de trabajo, equipo y rol del usuario. Consulta el [objeto de permisos]({{site.baseurl}}/api/objects_filters/scim_api_appendix). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parámetros de respuesta" }

### Estados de error {#error-states}

Si no existe ningún usuario para el `id` de recurso proporcionado, el endpoint devuelve:

```http
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "status": 404,
  "detail": "Resource not found"
}
```

{% endapi %}