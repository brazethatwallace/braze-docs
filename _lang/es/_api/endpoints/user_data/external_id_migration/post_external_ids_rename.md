---
nav_title: "POST: Renombrar ID externo"
article_title: "POST: Renombrar ID externo"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "En este artículo se describen los detalles del endpoint Renombrar ID externos."

---
{% api %}
# Renombrar ID externo {#rename-external-id}
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> Utiliza este endpoint para renombrar los ID externos de tus usuarios.

Puedes enviar hasta 50 objetos de renombramiento por solicitud.

Este endpoint establece un nuevo (principal) `external_id` para el usuario y deja obsoleto su `external_id` existente. Esto significa que el usuario puede ser identificado por cualquiera de los dos `external_id` hasta que se elimine el obsoleto. Tener varios ID externos permite un periodo de migración para que no se rompan las versiones heredadas de tus aplicaciones que utilizan el esquema de nombres de ID externos anterior. El perfil sigue siendo completamente funcional con ambos identificadores durante la ventana de migración: el SDK de Braze, la REST API y los flujos de mensajería pueden seguir haciendo referencia al usuario por cualquiera de los dos ID hasta que el obsoleto se elimine explícitamente.

Cuando ya no utilices tu antiguo esquema de nombres, te recomendamos encarecidamente que elimines los ID externos obsoletos utilizando el [endpoint `/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove).

{% alert warning %}
Asegúrate de eliminar los ID externos obsoletos con el endpoint `/users/external_ids/remove` en lugar de `/users/delete`. Enviar una solicitud a `/users/delete` con el ID externo obsoleto elimina el perfil de usuario por completo y no se puede deshacer.
{% endalert %}

## Cómo funciona el renombramiento {#how-renaming-works}

Cuando llamas a este endpoint, asigna un nuevo `external_id` principal a un perfil de usuario y, al mismo tiempo, convierte el `external_id` principal anterior en un ID externo obsoleto. Tras un renombramiento exitoso, el perfil de usuario contiene exactamente un `external_id` principal (el nuevo valor) y un ID externo obsoleto (el valor anterior).

Se permiten llamadas de renombramiento posteriores en el mismo perfil: cada renombramiento crea un ID externo obsoleto adicional, por lo que un perfil puede acumular un `external_id` principal y varios ID externos obsoletos con el tiempo. Sin embargo, el valor de `new_external_id` no debe existir ya en ningún perfil de Braze, ni como ID principal ni como ID externo obsoleto.

El endpoint no registra puntos de datos y no afecta a los recuentos de MAU. Todos los datos históricos del usuario (eventos, compras, atributos, participación en campañas) permanecen vinculados al mismo perfil.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este endpoint, necesitarás una [clave de API]({{site.baseurl}}/api/api_key) con el permiso `users.external_ids.rename`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Cuerpo de la solicitud {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | Obligatorio | Matriz de objetos de renombramiento de identificadores externos | Consulta el ejemplo de solicitud y las limitaciones siguientes para conocer la estructura del objeto de renombramiento de identificador externo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de solicitud" }

Toma nota de lo siguiente:

- El `current_external_id` debe ser el ID principal del usuario, y no puede ser un ID obsoleto. Si el valor pasado como `current_external_id` es en sí mismo un ID obsoleto en el perfil, la llamada fallará. Antes de reintentar un renombramiento fallido, utiliza el [endpoint `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para confirmar cuál es el ID principal actual.
- El `new_external_id` no debe estar ya en uso ni como ID principal ni como ID obsoleto. Intentar renombrar a un ID que ya está almacenado como ID obsoleto devuelve un error "new_external_id is already in use".
- El `current_external_id` y el `new_external_id` no pueden ser iguales.

## Ejemplo de solicitud {#request-example}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## Respuesta {#response}

La respuesta confirmará todos los renombramientos realizados con éxito, así como los renombramientos fallidos con los errores asociados. Los mensajes de error en el campo `rename_errors` harán referencia al índice del objeto en la matriz de la solicitud original.

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

El campo `message` devolverá `success` para cualquier solicitud válida. Los errores más específicos se recogen en la matriz `rename_errors`. El campo `message` devuelve un error en caso de:

- Clave de API no válida
- Matriz vacía `external_id_renames`
- Matriz `external_id_renames` con más de 50 objetos
- Límite de velocidad alcanzado (más de 1000 solicitudes por minuto)

## Migraciones masivas {#bulk-migrations}

Para migraciones que involucran grandes poblaciones de usuarios, agrupa a los usuarios en lotes de hasta 50 y envía cada lote como una llamada de API independiente. El endpoint está sujeto a un límite de velocidad de 1000 solicitudes por minuto. Con el tamaño máximo de lote (50 objetos por solicitud), esto permite hasta 50 000 renombramientos de usuarios por minuto.

Cada objeto de renombramiento en el lote se procesa de forma independiente. Un fallo en un objeto no bloquea a los demás en la misma solicitud. El cuerpo de la respuesta distingue los renombramientos exitosos (listados en la matriz `external_ids`) de los fallidos (listados en la matriz `rename_errors` con una referencia de índice a la posición del objeto fallido en la matriz de la solicitud).

Al ejecutar migraciones masivas:

1. Itera a través de toda la población de usuarios en lotes de hasta 50 pares.
2. En cada respuesta, inspecciona tanto `external_ids` (éxito) como `rename_errors` (fallo) para identificar a los usuarios que necesitan reintentarse.
3. Recopila los objetos fallidos y programa lotes de reintento por separado. Las causas comunes de fallo incluyen que el `new_external_id` ya esté en uso, o que el `current_external_id` sea un ID obsoleto en lugar de un ID principal.
4. Registra los éxitos y fallos en tus propios registros para que el estado de la migración se rastree fuera de Braze.

## Verificar el ID externo actual {#verifying-the-current-external-id}

Durante una migración, es posible que necesites confirmar cuál es el ID externo principal activo en un perfil determinado, por ejemplo, para determinar si un usuario específico ya ha sido migrado o para solucionar un renombramiento fallido. Utiliza el [endpoint `/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) para este propósito.

El endpoint de exportación resuelve tanto los ID externos principales como los obsoletos al mismo perfil subyacente y siempre devuelve el `external_id` principal actual en la respuesta. Esto significa que puedes consultar cualquier identificador conocido de un usuario, antiguo o nuevo, y la respuesta contendrá el ID principal canónico. Esta es una forma fiable de determinar el estado de la migración.

Para verificar solo el ID externo (en lugar de obtener el perfil completo), pasa `fields_to_export` con solo el campo `external_id`.

## Flujo de trabajo de migración recomendado {#recommended-migration-workflow}

Para la mayoría de los casos de uso de migración, la secuencia recomendada es:

1. **Prueba en staging** — Ejecuta el flujo completo de renombramiento y verificación en un espacio de trabajo de desarrollo o staging antes de tocar producción.
2. **Renombra en lotes** — Utiliza el endpoint `/users/external_ids/rename` en lotes de hasta 50, gestionando los `rename_errors` en cada respuesta y poniendo en cola los pares fallidos para reintento.
3. **Verifica** — Después de cada lote (o al final de la migración), comprueba perfiles de muestra usando `/users/export/ids` para confirmar que el `external_id` principal esperado está establecido.
4. **Mantén la ventana de obsolescencia** — Mantén los ID externos obsoletos activos durante el tiempo que cualquier sistema (incluidas las versiones heredadas de la aplicación en el campo) pueda seguir haciendo referencia a los ID antiguos. No apresures este paso.
5. **Elimina los ID obsoletos** — Una vez que se confirme que todos los sistemas están usando los nuevos ID, utiliza [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) en lotes de hasta 50 para limpiar.

Si también estás migrando tu integración de SDK (por ejemplo, cambiando el valor pasado a `changeUser`), coordina el renombramiento del lado de la API con el calendario de lanzamiento de la aplicación para que el nuevo ID externo esté en uso tanto en el servidor como en el cliente antes de que se eliminen los ID obsoletos.

## Preguntas más frecuentes {#frequently-asked-questions}

### ¿Influye esto en los MAU? {#does-this-impact-mau}
No, porque el número de usuarios sigue siendo el mismo; solo tienen un nuevo `external_id`.

### ¿Cambia históricamente el comportamiento de los usuarios? {#does-user-behavior-change-historically}
No, porque el usuario sigue siendo el mismo, y todo su comportamiento histórico sigue vinculado a él.

### ¿Puede ejecutarse en espacios de trabajo de desarrollo o de pruebas? {#can-it-be-run-on-development-or-staging-workspaces}
Sí. De hecho, recomendamos encarecidamente realizar una migración de prueba en un espacio de trabajo de staging o de desarrollo, y asegurarte de que todo ha ido bien antes de ejecutarla en los datos de producción.

### ¿Registra puntos de datos? {#does-this-log-data-points}
Esta característica no registra puntos de datos.

### ¿Cuál es el periodo de obsolescencia recomendado? {#what-is-the-recommended-deprecation-period}
No tenemos un límite estricto sobre el tiempo que puedes mantener ID externos obsoletos, pero recomendamos encarecidamente eliminarlos cuando ya no sea necesario hacer referencia a los usuarios por el ID obsoleto.

### ¿Cuántos ID externos obsoletos puede tener un perfil? {#how-many-deprecated-external-ids-can-a-profile-have}
Un perfil de usuario puede contener un `external_id` principal y cualquier cantidad de ID externos obsoletos acumulados a través de operaciones de renombramiento sucesivas. No existe un límite documentado en la cantidad de ID obsoletos que un solo perfil puede contener, pero Braze recomienda eliminarlos tan pronto como ya no sean necesarios.

{% endapi %}