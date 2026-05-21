---
nav_title: Comportamiento de fusión
article_title: Comportamiento de fusión de usuarios
page_order: 1
page_type: reference
description: "Descubre cómo Braze gestiona la fusión de usuarios para usuarios marcados para eliminación, usuarios de prueba y usuarios del Grupo de control global."
---

# Comportamiento de fusión de usuarios {#user-merge-behavior}

> Descubre cómo Braze gestiona la fusión de usuarios, incluidos los tres tipos de usuario en los que el comportamiento predeterminado no se aplica: usuarios marcados para eliminación, usuarios de prueba y usuarios del Grupo de control global.

Este comportamiento se aplica a todas las fusiones, ya sea que uses la [fusión individual]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#individual-merging), la [fusión masiva]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/#bulk-merging) o el [punto de conexión de la API de fusión de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).

## Comportamiento general de fusión {#general-merge-behavior}

Cuando fusionas dos perfiles de usuario, Braze rellena los campos vacíos del perfil a conservar con los valores del perfil a fusionar. Si un campo tiene un valor en ambos perfiles, Braze conserva el valor del perfil a conservar.

Por ejemplo, si un valor solo existe en uno de los perfiles, Braze lo conserva:

| Campo | Perfil a fusionar | Perfil a conservar | Perfil resultante |
|---|---|---|---|
| `first_name` | Alex | (vacío) | Alex |
| `last_name` | (vacío) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Si ambos perfiles tienen un valor para el mismo campo, Braze conserva el valor del perfil a conservar:

| Campo | Perfil a fusionar | Perfil a conservar | Perfil resultante |
|---|---|---|---|
| `first_name` | Alex | Al | Al |
| `last_name` | (vacío) | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

Este comportamiento funciona bien para atributos predeterminados y personalizados. Sin embargo, Braze gestiona los siguientes tipos de usuario de forma diferente.

## Resumen de comportamiento {#behavior-summary}

| Tipo de usuario | Comportamiento | Motivo |
|---|---|---|
| Usuarios marcados para eliminación | No se fusionan | Los perfiles marcados para eliminación se eliminan en un plazo de 7 días, por lo que no es necesario conservar sus datos. |
| Usuarios de prueba | Se fusionan, conservando el estado de usuario de prueba | Mantener el estado de usuario de prueba te ayuda a conservar una población de prueba utilizable después de una fusión. |
| Usuarios del Grupo de control global | No se fusionan | La fusión cambiaría los números de contenedor aleatorio, lo que afectaría a los experimentos y los informes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Usuarios marcados para eliminación {#users-marked-for-deletion}

Cuando usas la [herramienta de eliminación masiva de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/) para eliminar un segmento, Braze marca esos perfiles de usuario para su eliminación en los próximos 7 días. Braze no fusiona perfiles que están marcados para eliminación, ya sean el perfil a conservar o el perfil a fusionar.

Si necesitas fusionar un perfil que está marcado para eliminación, primero [cancela la eliminación del segmento]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/#cancel) o quita al usuario de la eliminación para que el perfil ya no esté marcado.

## Usuarios de prueba {#test-users}

Braze permite fusionar perfiles de usuarios de prueba y conserva el estado de usuario de prueba en el perfil resultante. Esto difiere del [comportamiento general de fusión](#general-merge-behavior), que de otro modo conservaría el valor del perfil a conservar.

La siguiente tabla muestra el estado de usuario de prueba resultante para cada combinación:

| Perfil a fusionar | Perfil a conservar | Perfil resultante |
|---|---|---|
| No es usuario de prueba | No es usuario de prueba | No es usuario de prueba |
| Usuario de prueba | Usuario de prueba | Usuario de prueba |
| Usuario de prueba | No es usuario de prueba | Usuario de prueba |
| No es usuario de prueba | Usuario de prueba | Usuario de prueba |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para más información sobre los usuarios de prueba, consulta [Grupos internos]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/).

## Usuarios del Grupo de control global {#global-control-group-users}

Braze no fusiona perfiles de usuario en un [Grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group/), ya sean el perfil a conservar o el perfil a fusionar.

La pertenencia al Grupo de control global se determina por el [número de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/) de un usuario. La fusión cambiaría qué usuarios pertenecen al grupo, lo que afectaría a tus experimentos e informes.

## Artículos relacionados {#related-articles}

- [Fusionar usuarios duplicados]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/)
- [POST: Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
- [Eliminar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/)
- [Grupo de control global]({{site.baseurl}}/user_guide/audience/global_control_group/)
- [Números de contenedor aleatorio]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers/)
- [Grupos internos]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/)