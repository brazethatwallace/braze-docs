---
nav_title: "POST: Identificar usuarios"
article_title: "POST: Identificar usuarios"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
alias: /users_identify_merge/
description: "En este artículo se describen los detalles del endpoint Identificar usuarios de Braze."
---
{% api %}
# Identificar usuarios {#identify-users}
{% apimethod post %}
/users/identify
{% endapimethod %}

> Utiliza este endpoint para identificar a un usuario no identificado (solo alias, solo correo electrónico o solo número de teléfono) utilizando el ID externo proporcionado.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5f74e0f7-0620-4c7b-b0a2-f5f38fdbff58 {% endapiref %}

## Cómo funciona {#how-it-works}

La llamada `/users/identify` combina un perfil de usuario identificado por un alias (perfil solo con alias), una dirección de correo electrónico (perfil solo con correo electrónico) o un número de teléfono (perfil solo con número de teléfono) con un perfil de usuario que tiene un `external_id` (perfil identificado) y, a continuación, elimina el perfil solo con alias.

Para identificar a un usuario es necesario incluir un `external_id` en los siguientes objetos:

- `aliases_to_identify`
- `emails_to_identify`
- `phone_numbers_to_identify`

Si no hay ningún usuario con ese `external_id`, el `external_id` se añade al registro del usuario con asignación de alias y se considera que el usuario está identificado. Los usuarios solo pueden tener un alias para una etiqueta específica. Si ya existe un usuario con el `external_id` y tiene un alias existente con la misma etiqueta que el perfil solo con alias, entonces los perfiles de usuario no se combinan.

{% alert tip %}
Para evitar la pérdida inesperada de datos al identificar a los usuarios, te recomendamos encarecidamente que primero consultes las [mejores prácticas de recopilación de datos]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices) para saber cómo capturar datos de usuario cuando ya existe información de usuario solo con alias.
{% endalert %}

### Comportamiento de fusión {#merging-behavior}

De forma predeterminada, este endpoint fusiona la siguiente lista de campos que se encuentran **exclusivamente** en el usuario anónimo con el usuario identificado.

{% details Lista de campos que se fusionan %}
- Nombre
- Apellido
- Correo electrónico
- Género
- Fecha de nacimiento
- Número de teléfono
- Zona horaria
- Ciudad de origen
- País
- Idioma
- Recuento de sesiones (la suma de las sesiones de ambos perfiles)
- Fecha de la primera sesión (Braze elige la fecha más temprana de las dos)
- Fecha de la última sesión (Braze elige la fecha más reciente de las dos)
- Atributos personalizados
- Datos de eventos personalizados y eventos de compra
- Propiedades de eventos personalizados y de compra para la segmentación «X veces en Y días» (donde X<=50 e Y<=30)
- Resumen segmentable de eventos personalizados
  - Recuento de eventos (la suma de ambos perfiles)
  - Primera vez que ocurrió el evento (Braze elige la fecha más temprana de las dos)
  - Última vez que ocurrió el evento (Braze elige la fecha más reciente de las dos)
- Total de compras dentro de la aplicación en céntimos (la suma de ambos perfiles)
- Número total de compras (la suma de ambos perfiles)
- Fecha de la primera compra (Braze elige la fecha más temprana de las dos)
- Fecha de la última compra (Braze elige la fecha más reciente de las dos)
- Resúmenes de la aplicación
- Campos Last_X_at (Braze actualiza los campos si los campos del perfil huérfano son más recientes)
- Resúmenes de Campaign (Braze selecciona los campos de fecha más recientes)
- Resúmenes del flujo de trabajo (Braze selecciona los campos de fecha más recientes)
- Historial de mensajes e interacción con mensajes
- Recuento de eventos personalizados y eventos de compra, y marcas de tiempo de primera y última fecha
  - Estos campos fusionados actualizan los filtros «para X eventos en Y días». Para los eventos de compra, estos filtros incluyen «número de compras en Y días» y «dinero gastado en los últimos Y días».
- Datos de sesión si la aplicación existe en ambos perfiles de usuario
  - Por ejemplo, si nuestro usuario objetivo no tiene un resumen de la aplicación «ABCApp», pero nuestro usuario original sí, el usuario objetivo tendrá el resumen de la aplicación «ABCApp» en su perfil después de la fusión.
{% enddetails %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/basics) con el permiso `users.identify`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users identify' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "aliases_to_identify" : (required, array of alias to identify objects),
   "emails_to_identify": (optional, array of alias to identify objects) User emails to identify,
   "phone_numbers_to_identify": (optional, array of alias to identify objects) User phone numbers to identify,
},
```

### Parámetros de la solicitud {#request-parameters}

Puedes añadir hasta 50 alias de usuario por solicitud. Puedes asociar varios alias de usuario adicionales a un único `external_id`.

{% alert important %}
Se requiere uno de los siguientes por solicitud: `aliases_to_identify`, `emails_to_identify` o `phone_numbers_to_identify`. Por ejemplo, puedes utilizar este endpoint para identificar a los usuarios por correo electrónico utilizando `emails_to_identify` en tu solicitud.
{% endalert %}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
|-----------------------------|----------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `aliases_to_identify` | Obligatorio | Conjunto de objetos de alias para identificar | Ver [objeto de alias para identificar]({{site.baseurl}}/api/objects_filters/aliases_to_identify) y [objeto de alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object). |
| `emails_to_identify` | Obligatorio | Conjunto de objetos de alias para identificar | Obligatorio si se especifica `email` como identificador. Direcciones de correo electrónico para identificar usuarios. Ver [Identificación de usuarios por correo electrónico](#identifying-users-by-email-addresses-and-phone-numbers). |
| `phone_numbers_to_identify` | Obligatorio | Conjunto de objetos de alias para identificar | Números de teléfono para identificar usuarios. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

### Identificación de usuarios mediante direcciones de correo electrónico y números de teléfono {#identifying-users-by-email-addresses-and-phone-numbers}

Si se especifica una dirección de correo electrónico o un número de teléfono como identificador, también debes incluir `prioritization` en el identificador.

`prioritization` debe ser una matriz que especifique qué usuario fusionar si se encuentran varios usuarios. `prioritization` es una matriz ordenada, lo que significa que si más de un usuario coincide a partir de una priorización, no se produce la fusión.

Los valores permitidos para la matriz son:

- `identified`
- `unidentified`
- `most_recently_updated` (se refiere a dar prioridad al usuario actualizado más recientemente)
- `least_recently_updated` (se refiere a dar prioridad al usuario actualizado menos recientemente)

En la matriz de priorización solo puede existir una de las siguientes opciones a la vez:

- `identified` se refiere a dar prioridad a un usuario con un `external_id`
- `unidentified` se refiere a dar prioridad a un usuario sin un `external_id`

{% alert note %}
No se produce una fusión si la dirección de correo electrónico o el número de teléfono coincide con varios usuarios. Esto incluye los casos en los que uno de esos usuarios tiene el mismo `external_id` que el especificado en la solicitud. En estos casos, el endpoint devuelve `"message": "success"`, pero los perfiles de usuario no se combinan. Para evitar esto, verifica que la dirección de correo electrónico o el número de teléfono esté asociado únicamente a usuarios no identificados antes de llamar a este endpoint.
{% endalert %}

## Ejemplo de solicitud {#request-example}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/identify' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "aliases_to_identify": [
    {
      "external_id": "external_identifier",
      "user_alias": {
          "alias_name": "example_alias",
          "alias_label": "example_label"
      }
    }
  ],
  "emails_to_identify": [
    {
      "external_id": "external_identifier_2",
      "email": "john.smith@example.com",
      "prioritization": ["unidentified", "most_recently_updated"]
    }
  ]
}'
```

### Distinción entre mayúsculas y minúsculas {#case-sensitivity}

El campo `alias_name` distingue entre mayúsculas y minúsculas. Una solicitud que devuelve un código de estado `201` solo confirma que la sintaxis de la solicitud era válida; no confirma que el alias haya coincidido. Si las mayúsculas y minúsculas de `alias_name` en tu solicitud no coinciden exactamente con el alias almacenado en el perfil de usuario, la operación fallará silenciosamente y el `external_id` no se asignará. Por ejemplo, si el alias almacenado es `JimJones@example.com`, una solicitud con `jimjones@example.com` devolverá éxito pero no producirá ningún resultado.

{% alert tip %}
Para más información sobre `alias_name` y `alias_label`, consulta nuestra documentación sobre [alias de usuario]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).
{% endalert %}

### ¿Por qué mi solicitud de identificación devuelve éxito pero el perfil no se fusionó? {#why-does-my-identify-request-return-success-but-the-profile-did-not-merge}

`201 Created` con `message: success` significa que Braze aceptó la solicitud. No garantiza que cada alias o correo electrónico en la carga útil haya coincidido con un perfil existente; las diferencias de mayúsculas y minúsculas en `alias_name`, los perfiles duplicados o las reglas de priorización de Braze pueden dar como resultado que no se produzca ninguna fusión visible aunque la llamada haya tenido éxito. Verifica que las mayúsculas y minúsculas de `alias_name` coincidan exactamente con los valores almacenados, comprueba si hay perfiles duplicados con [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) y revisa [`prioritization`](#identifying-users-by-email-addresses-and-phone-numbers) cuando utilices `emails_to_identify`.

## Respuesta {#response}

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

{% endapi %}