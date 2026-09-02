---
nav_title: "GET: Buscar cuenta de usuario existente en el panel por correo electrónico"
article_title: "GET: Buscar cuenta de usuario existente en el panel por correo electrónico"
alias: /get_search_existing_dashboard_user_email/
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint de Braze para buscar una cuenta de usuario existente en el panel por correo electrónico."
---

{% api %}
# Buscar cuenta de usuario existente en el panel por correo electrónico {#search-existing-dashboard-user-account-by-email}
{% apimethod get %}
scim/v2/Users?filter=userName%20eq%20"user%40test.com"
{% endapimethod %}

> Usa este endpoint para buscar una cuenta de usuario del panel existente especificando su correo electrónico en el parámetro de consulta del filtro.

Ten en cuenta que cuando el parámetro de consulta está codificado en URL se leerá así:

`/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22`

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5037d810-b822-4c54-bb51-f30470a42a95 {% endapiref %}

{% multi_lang_include scim/scim_alerts.md alert='custom_endpoint' %}

## Requisitos previos {#prerequisites}

Para usar este endpoint, necesitarás un token SCIM. Utilizarás el Origin de tu servicio como encabezado `X-Request-Origin`. Para más información, consulta [Aprovisionamiento automatizado de usuarios]({{site.baseurl}}/scim/automated_user_provisioning).

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='look up dashboard user email' %}

## Parámetros de consulta {#query-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|---|---|---|---|
| `filter` | Obligatorio | Cadena | Expresión de filtro SCIM para buscar por correo electrónico. Braze solo admite `userName eq "user@example.com"`. El valor del correo electrónico debe estar entre comillas dobles. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parámetros de consulta" }

{% alert important %}
Braze solo admite filtros de coincidencia exacta en `userName` utilizando el operador `eq`. Otros campos u operadores de filtro SCIM devuelven una respuesta `400`.
{% endalert %}

## Parámetros de la solicitud {#request-parameters}

```http
Content-Type: application/json
X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE
Authorization: Bearer YOUR-SCIM-TOKEN-HERE
```

{% alert note %}
Si recibes una respuesta `401`, confirma que estás usando un token SCIM (no una clave de API REST or transferencia de estado representacional), que `X-Request-Origin` coincide con el Origin de tu servicio y que tu dirección IP está en la lista de permitidos de SCIM. Para más detalles, consulta [Aprovisionamiento automatizado de usuarios]({{site.baseurl}}/scim/automated_user_provisioning).
{% endalert %}

## Ejemplo de solicitud {#example-request}
```bash
curl --location --request GET \ 'https://rest.iad-01.braze.com/scim/v2/Users?filter=userName%20eq%20%22user@example.com%22' \
--header 'Content-Type: application/json' \
--header 'X-Request-Origin: YOUR-REQUEST-ORIGIN-HERE' \
--header 'Authorization: Bearer YOUR-SCIM-TOKEN-HERE' \
```

## Respuesta {#response}
```json
{
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
    "totalResults": 1,
    "Resources": [
        {
            "userName": "user@example.com",
            "id": "dfa245b7-24195aec-887bb3ad-602b3340",
            "name": {
                "givenName": "Test",
                "familyName": "User"
            },
            "department": "finance",
            "createdAt": "2024 Nov 11, 4:20 PM",
            "lastSignInAt": "N/A",
            "permissions": {
                "companyPermissions": ["manage_company_settings"],
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
    ]
}
```

## Parámetros de respuesta {#response-parameters}

| Parámetro | Tipo de datos | Descripción |
|---|---|---|
| `schemas` | Matriz de cadenas | Esquema de respuesta de lista SCIM. |
| `totalResults` | Entero | Número de usuarios del panel coincidentes (0 si no hay coincidencias). |
| `Resources` | Matriz | Matriz de objetos de usuario. Cada objeto utiliza los mismos campos que [GET: Buscar una cuenta de usuario existente en el panel]({{site.baseurl}}/get_see_user_account_information). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parámetros de respuesta" }

### Campos del objeto de usuario {#user-object-fields}

| Parámetro | Tipo de datos | Descripción |
|---|---|---|
| `id` | Cadena | El ID de recurso del usuario. |
| `userName` | Cadena | La dirección de correo electrónico del usuario. |
| `name` | Objeto | Contiene `givenName` y `familyName`. |
| `department` | Cadena | El departamento del usuario, si está configurado. |
| `createdAt` | Cadena | Fecha en la que se creó la cuenta de usuario. Devuelve `N/A` cuando no está configurado; de lo contrario, tiene el formato `YYYY Mon DD, H:MM AM/PM`. |
| `lastSignInAt` | Cadena | Fecha en la que el usuario inició sesión por última vez. Devuelve `N/A` si el usuario no ha iniciado sesión; de lo contrario, tiene el formato `YYYY Mon DD, H:MM AM/PM`. |
| `permissions` | Objeto | Permisos de empresa, espacio de trabajo, equipo y rol. Consulta el [objeto de permisos]({{site.baseurl}}/api/objects_filters/scim_api_appendix). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos del objeto de usuario" }

### Estados de error {#error-states}

Si el parámetro `filter` no se incluye o tiene un formato incorrecto, el endpoint devuelve:

```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
  "status": 400,
  "detail": "Request is unparsable, syntactically incorrect, or violates schema."
}
```

{% endapi %}