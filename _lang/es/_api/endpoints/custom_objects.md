---
nav_title: Objetos personalizados
article_title: Endpoints de objetos personalizados
search_tag: Endpoint
page_order: 9.5
layout: dev_guide
page_type: landing
description: "Esta página de destino enumera los endpoints de objetos personalizados de Braze."
needs_mermaid: true

guide_top_header: "Endpoints de objetos personalizados"
guide_top_text: "Usa estos endpoints para listar tipos de objetos personalizados, gestionar registros de objetos personalizados y gestionar relaciones entre objetos y usuarios."
guide_top_alert: "Los objetos personalizados se encuentran actualmente en acceso anticipado. Tu espacio de trabajo debe estar habilitado antes de que los permisos de clave de API de objetos personalizados aparezcan en **Configuración** > **Claves de API**."

guide_featured_title: "Endpoints de tipos"
guide_featured_list:
  - name: "GET: Listar tipos de objetos personalizados"
    link: /docs/api/endpoints/custom_objects/types/get_list_custom_object_types
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Obtener tipo de objeto personalizado"
    link: /docs/api/endpoints/custom_objects/types/get_custom_object_type
    image: /assets/img/braze_icons/search-md.svg
  - name: "GET: Listar tipos de relación de usuario"
    link: /docs/api/endpoints/custom_objects/types/get_list_user_relationship_types
    image: /assets/img/braze_icons/users-01.svg
  - name: "GET: Listar tipos de relación de objeto"
    link: /docs/api/endpoints/custom_objects/types/get_list_object_relationship_types
    image: /assets/img/braze_icons/link-external-01.svg

guide_menu_title: "Endpoints de objetos"
guide_menu_list:
  - name: "GET: Listar objetos personalizados"
    link: /docs/api/endpoints/custom_objects/objects/get_list_custom_objects
    image: /assets/img/braze_icons/list.svg
  - name: "GET: Obtener objeto personalizado"
    link: /docs/api/endpoints/custom_objects/objects/get_custom_object
    image: /assets/img/braze_icons/search-md.svg
  - name: "POST: Crear objeto personalizado"
    link: /docs/api/endpoints/custom_objects/objects/post_create_custom_object
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Reemplazar objeto personalizado"
    link: /docs/api/endpoints/custom_objects/objects/put_replace_custom_object
    image: /assets/img/braze_icons/refresh-ccw-04.svg
  - name: "PATCH: Actualizar objeto personalizado"
    link: /docs/api/endpoints/custom_objects/objects/patch_update_custom_object
    image: /assets/img/braze_icons/user-edit.svg
  - name: "DELETE: Eliminar objeto personalizado"
    link: /docs/api/endpoints/custom_objects/objects/delete_custom_object
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title2: "Endpoints de relaciones de objetos"
guide_menu_list2:
  - name: "GET: Listar relaciones de objetos"
    link: /docs/api/endpoints/custom_objects/object_relationships/get_list_object_relationships
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Crear relación de objeto"
    link: /docs/api/endpoints/custom_objects/object_relationships/post_create_object_relationship
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Reemplazar relación de objeto"
    link: /docs/api/endpoints/custom_objects/object_relationships/put_replace_object_relationship
    image: /assets/img/braze_icons/refresh-ccw-04.svg
  - name: "PATCH: Actualizar relación de objeto"
    link: /docs/api/endpoints/custom_objects/object_relationships/patch_update_object_relationship
    image: /assets/img/braze_icons/user-edit.svg
  - name: "DELETE: Eliminar relación de objeto"
    link: /docs/api/endpoints/custom_objects/object_relationships/delete_object_relationship
    image: /assets/img/braze_icons/edit-05.svg

guide_menu_title3: "Endpoints de relaciones de usuario"
guide_menu_list3:
  - name: "GET: Listar relaciones de usuario"
    link: /docs/api/endpoints/custom_objects/user_relationships/get_list_user_relationships
    image: /assets/img/braze_icons/list.svg
  - name: "POST: Crear relación de usuario"
    link: /docs/api/endpoints/custom_objects/user_relationships/post_create_user_relationship
    image: /assets/img/braze_icons/check-square-broken.svg
  - name: "PUT: Reemplazar relación de usuario"
    link: /docs/api/endpoints/custom_objects/user_relationships/put_replace_user_relationship
    image: /assets/img/braze_icons/refresh-ccw-04.svg
  - name: "PATCH: Actualizar relación de usuario"
    link: /docs/api/endpoints/custom_objects/user_relationships/patch_update_user_relationship
    image: /assets/img/braze_icons/user-edit.svg
  - name: "DELETE: Eliminar relación de usuario"
    link: /docs/api/endpoints/custom_objects/user_relationships/delete_user_relationship
    image: /assets/img/braze_icons/edit-05.svg
---

## URL base y autenticación {#base-url-and-authentication}

Usa tu endpoint REST del espacio de trabajo y envía `Authorization: Bearer YOUR_REST_API_KEY`. Esta sección explica dónde se alojan los endpoints de objetos personalizados y cómo se autentican las solicitudes.

- Para los hosts de los endpoints, consulta el [resumen de la API de Braze]({{site.baseurl}}/api/basics#endpoints).
- Todas las cargas útiles de solicitud y respuesta son JSON.
- Las solicitudes se limitan al espacio de trabajo propietario de la clave de API.
- Si la clave tiene una lista de IP permitidas, las direcciones IP no incluidas devuelven `403`.

## Permisos de clave de API {#api-key-permissions}

Esta sección asocia cada endpoint con su permiso requerido para que puedas definir el alcance de las claves de API de forma segura.

| Permiso | Grupo de endpoints |
|---|---|
| `custom_objects.read` | Lecturas de tipos y objetos, y lecturas de relaciones de objetos |
| `custom_objects.create` | Creación de objetos |
| `custom_objects.update` | Reemplazo y actualización de objetos |
| `custom_objects.delete` | Eliminación de objetos |
| `custom_objects.user_relationships.read` | Lecturas de relaciones de usuario |
| `custom_objects.user_relationships.create` | Creación de relaciones de usuario |
| `custom_objects.user_relationships.update` | Reemplazo y actualización de relaciones de usuario |
| `custom_objects.user_relationships.delete` | Eliminación de relaciones de usuario |
| `custom_objects.object_relationships.create` | Creación de relaciones de objetos |
| `custom_objects.object_relationships.update` | Reemplazo y actualización de relaciones de objetos |
| `custom_objects.object_relationships.delete` | Eliminación de relaciones de objetos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Grupos de permisos de objetos personalizados" }

{% alert note %}
Las lecturas de relaciones de objetos usan `custom_objects.read`. No existe un permiso `custom_objects.object_relationships.read`.
{% endalert %}

## Límites de velocidad {#rate-limits}

Esta sección explica las cuotas predeterminadas de solicitudes y los encabezados de respuesta tanto para tráfico de lectura como de escritura.

| Contenedor | Límite predeterminado |
|---|---|
| Lecturas de objetos personalizados | 50 solicitudes por minuto |
| Escrituras de objetos personalizados | 50 solicitudes por minuto |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Límites de velocidad predeterminados de objetos personalizados" }

Cada respuesta incluye `X-RateLimit-Limit`, `X-RateLimit-Remaining` y `X-RateLimit-Reset`.

Para solicitudes limitadas, Braze devuelve `429` y una carga útil de error con `id` y `message`.

```json
{
  "errors": [
    {
      "id": "rate-limit-exceeded",
      "message": "You have exceeded your limit of 50 requests per minute."
    }
  ]
}
```

## Conceptos básicos {#core-concepts}

Esta sección define los identificadores clave utilizados en todos los endpoints de objetos personalizados.

- `type_name`: el nombre de máquina del tipo de objeto personalizado, único dentro de un espacio de trabajo.
- `external_id`: tu identificador de objeto, único dentro de un tipo.
- `braze_id`: el ID de usuario de Braze utilizado en los endpoints de relaciones de usuario.
- `attributes`: datos de objeto o relación con claves de nombre de campo, validados contra el esquema configurado.

## Cómo funcionan las relaciones {#how-relationships-work}

Esta sección explica los tipos de relación, los vínculos de relación y el comportamiento de `anchor` antes de que uses las páginas de referencia de endpoints.

### Modelo de relaciones de un vistazo {#relationship-model-at-a-glance}

Usa este diagrama para ver cómo encajan los tipos, registros y relaciones, y qué te permite hacer vincularlos en Braze. Defines los tipos en el panel y luego escribes los registros y los vínculos entre ellos a través de estos endpoints.

```mermaid
%%{init: {"flowchart": {"wrappingWidth": 400}} }%%
flowchart LR
  subgraph define["Set up in the dashboard"]
    objtype["Custom object types define<br/>the fields a record has"]
    reltype["Relationship types determine<br/>which links are allowed"]
  end

  subgraph write["Write with the API"]
    person["A person you<br/>send messages to"]
    record["A business record<br/>they belong to"]
    related["Another record<br/>connected to it"]
    person -- "A user relationship links<br/>a person to a record" --> record
    record -- "An object relationship links<br/>one record to another" --> related
  end

  subgraph unlock["What it unlocks"]
    segment["Segment people by the<br/>records they belong to"]
    liquid["Personalize messages with<br/>data from those records"]
  end

  define -- "decides what you<br/>are allowed to link" --> write
  write -- "makes these<br/>possible" --> unlock
```

### Los tipos y los vínculos son independientes {#types-and-edges-are-separate}

- Los tipos de relación definen qué vínculos son válidos y se gestionan en el panel.
- Los vínculos de relación son los enlaces reales entre registros y se crean, actualizan y eliminan a través de estos endpoints de API.
- Antes de escribir relaciones, lista los valores válidos de `rel_kind` con:
  - `GET /custom_objects/types/{type_name}/user_relationship_types`
  - `GET /custom_objects/types/{type_name}/object_relationship_types`

### Por qué las relaciones de objetos requieren `related_type_name` {#why-object-relationships-require-related_type_name}

- `rel_kind` no es globalmente único entre todos los pares de tipos de objetos. Por ejemplo, `rel_kind` puede ser `subaccount` para un par de tipos de objetos y `partner_account` para otro.
- Por lo tanto, las escrituras de relaciones de objetos requieren tanto `rel_kind` como `related_type_name` para identificar el tipo de relación previsto junto con el otro tipo de objeto en la asociación.
- Si `related_type_name` no coincide con el tipo de relación para ese `rel_kind`, la solicitud devuelve `400`.

### `anchor` controla la dirección de la relación {#anchor-controls-relationship-direction}

Las relaciones de objetos son direccionales. El objeto de la URL se interpreta en función de `anchor`.

| `anchor` | Rol del objeto en la URL | Clave de objeto relacionado en las respuestas |
|---|---|---|
| `source` (predeterminado) | Lado de origen (vínculo saliente) | `to_custom_object` |
| `target` | Lado de destino (vínculo entrante) | `from_custom_object` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Comportamiento de anchor en las relaciones de objetos" }

Crear el mismo vínculo desde la perspectiva de anchor opuesta sigue apuntando a una única relación subyacente. Una segunda llamada de creación para el mismo vínculo devuelve `409` (`duplicate-object-relationship`).

### Asimetría de rutas en las relaciones de usuario {#path-asymmetry-for-user-relationships}

Las lecturas y escrituras de relaciones de usuario utilizan intencionalmente rutas de endpoints diferentes:

- Lectura: `GET /custom_objects/objects/{type_name}/{external_id}/user_relationships`
- Escritura: `POST|PUT|PATCH|DELETE /custom_objects/objects/{type_name}/{external_id}/users`

### Los atributos de relación son independientes de los atributos de objeto {#relationship-attributes-are-separate-from-object-attributes}

- Los endpoints de relaciones devuelven atributos a nivel de vínculo en el campo `attributes` de nivel superior.
- Los atributos del objeto permanecen anidados bajo `to_custom_object` o `from_custom_object`.
- `PUT` reemplaza los `attributes` de la relación, y `PATCH` los fusiona.

### Ejemplo práctico {#worked-example}

Este ejemplo muestra un flujo de trabajo común con cuentas:

1. Crear `account/acct-123`.
2. Crear `account/acct-456` como cuenta secundaria.
3. Vincular un usuario a `acct-123` con `rel_kind: account_user`.
4. Vincular `acct-123` a `acct-456` con `rel_kind: subaccount`.

Para leer los vínculos:

- `GET /custom_objects/objects/account/acct-123/user_relationships` para usuarios vinculados
- `GET /custom_objects/objects/account/acct-123/object_relationships` para vínculos de objetos salientes
- `GET /custom_objects/objects/account/acct-456/object_relationships?anchor=target` para vínculos de objetos entrantes

{% alert note %}
Los endpoints `DELETE` para relaciones de objetos y relaciones de usuario requieren un cuerpo de solicitud JSON.
{% endalert %}

## Paginación y actualización de datos {#pagination-and-data-freshness}

Esta sección cubre el comportamiento de paginación en los endpoints de listado y los tiempos esperados de visibilidad de los datos después de las escrituras.

- Los endpoints de listado admiten `limit` y `offset`.
- `limit` tiene un valor predeterminado de `100` y está limitado entre `1` y `250`.
- `offset` tiene un valor predeterminado de `0`, y los valores negativos se redondean a `0`.
- Las escrituras son visibles de inmediato para las lecturas y la personalización con Liquid.
- La pertenencia a segmentos basada en objetos personalizados puede tardar hasta una hora, ya que los filtros calculados se actualizan cada hora.

## Comportamiento de errores {#error-behavior}

Esta sección resume los patrones de estado y respuesta de error utilizados en los endpoints de objetos personalizados.

- `404`, `409`, `422` y `429` devuelven un array `errors` con `id` y `message`.
- `400`, `401` y `403` devuelven una cadena `error` simple.
- Los límites de `422` basados en contrato varían según la empresa.