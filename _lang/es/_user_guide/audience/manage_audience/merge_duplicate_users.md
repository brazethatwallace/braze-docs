---
nav_title: Fusionar usuarios duplicados
article_title: Fusionar usuarios duplicados
description: "Aprende a encontrar y fusionar usuarios duplicados en tu panel de Braze."
page_order: 4
---

# Fusionar usuarios duplicados {#merge-duplicate-users}

> Aprende a encontrar y fusionar usuarios duplicados para maximizar la efectividad de tus Campaigns y Canvas.

## REST API: identificar y fusionar usuarios {#rest-api-identify-and-merge-users}

Las herramientas de esta página fusionan perfiles duplicados en el dashboard. También puedes combinar o redirigir perfiles a través de los [puntos de conexión de datos de usuario]({{site.baseurl}}/api/endpoints/user_data/) de Braze:

- [POST: Identificar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) (`/users/identify`): combina un perfil de solo alias, solo correo electrónico o solo número de teléfono con un perfil que tiene un `external_id`.
- [POST: Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) (`/users/merge`): fusiona un perfil de usuario en otro, incluso cuando ambos perfiles ya tienen un `external_id`. Revisa los [Requisitos previos]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#prerequisites) y el [Comportamiento de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior) antes de llamar a este punto de conexión.

Cuando un perfil anónimo coincide con un perfil identificado existente (por ejemplo, a través de una llamada `changeUser()` del SDK o `/users/identify`), Braze desvincula el perfil anónimo y copia solo ciertos campos en el perfil identificado. Para más información, consulta [Qué sucede cuando identificas usuarios anónimos]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users).

Las fusiones de usuarios son difíciles de deshacer. Si planeas una fusión compleja entre múltiples valores de `external_id` o migraciones de perfiles a gran escala, ponte en contacto con tu administrador del éxito del cliente de Braze para obtener orientación antes de depender de `/users/merge`.

Braze gestiona tres tipos de usuarios de forma diferente al fusionar: usuarios marcados para eliminación, usuarios de prueba y usuarios del Grupo de control global. Para más detalles, consulta [Comportamiento de fusión de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/).

## Fusión individual {#individual-merging}

Si una búsqueda de usuarios devuelve perfiles duplicados, puedes fusionar cada perfil individualmente desde el perfil del usuario en el panel de Braze.

### Paso 1: Buscar un perfil duplicado {#step-1-search-for-a-duplicate-profile}

En Braze, selecciona **Audience** > **User Search**.

![El mosaico "User Search" resaltado en el menú de navegación.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Introduce un identificador único, como una dirección de correo electrónico o un número de teléfono, para el perfil duplicado y selecciona **Search**.

![La página "User Search" en el panel de Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Paso 2: Fusionar duplicados {#step-2-merge-duplicates}

Para iniciar el proceso de fusión, selecciona **Merge duplicates**.

![Uno de los perfiles de usuario duplicados.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Elige qué perfil de usuario conservar y cuál fusionar, y luego selecciona **Merge profiles**. Repite este proceso hasta que hayas fusionado todos los perfiles duplicados.


{% alert warning %}
Los perfiles de usuario duplicados no se pueden recuperar después de la fusión.
{% endalert %}

## Fusión masiva {#bulk-merging}

Cuando fusionas usuarios duplicados de forma masiva, Braze encuentra perfiles con identificadores coincidentes (como una dirección de correo electrónico) y conserva un perfil. Braze primero prioriza los perfiles con un `external_id` y luego aplica tu configuración de **Resolving ties**: **Resolve ties using** y **Prioritization**. Si no hay perfiles con un `external_id`, Braze usa **Resolve ties using** y **Prioritization** entre los perfiles sin un `external_id`. Braze solo fusiona usuarios cuando esta configuración identifica un perfil para conservar. Por ejemplo, si **Resolve ties using** es **Updated date** y ambos perfiles tienen la misma marca de tiempo de última actualización, Braze no puede resolver el empate, por lo que esos usuarios no se fusionan.

### Paso 1: Ir a Gestionar audiencia {#step-1-go-to-manage-audience}

En el panel de Braze, selecciona **Audience** > **Manage Audience**.

![El mosaico "Manage Audience" resaltado en el menú de navegación.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Paso 2: Previsualizar los resultados (opcional) {#step-2-preview-the-results-optional}

Para previsualizar tus resultados antes de fusionar tus duplicados, selecciona **Generate list of duplicates**.

![La página "Manage Audience" con "Generate list of duplicates" resaltado.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze generará tu vista previa y la enviará a tu dirección de correo electrónico como un archivo CSV.


En el siguiente ejemplo, Braze utiliza el ID externo del usuario para marcar perfiles duplicados e identificar cuál conservar. Si estos perfiles se fusionan de forma masiva, Braze utilizará el perfil con un ID externo como el nuevo perfil principal del usuario.

{% tabs local %}
{% tab example csv file %}
| Email Address    | External ID | Phone Number   | Braze ID              | Identifier for rule | Profile to keep | Profile to merge |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99   | (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             | (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             | (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2: Previsualizar los resultados (opcional)" }
{% endtab %}
{% endtabs %}

#### Comportamiento de fusión {#merge-behavior}

Braze rellenará los campos vacíos del perfil conservado con valores del perfil fusionado. Para obtener una lista de los campos que se rellenarán, consulta [Comportamiento de fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### Paso 3: Fusionar tus duplicados {#step-3-merge-your-duplicates}

Si estás conforme con los resultados de tu vista previa, selecciona **Merge all duplicates**.

{% alert warning %}
Los perfiles de usuario duplicados no se pueden recuperar después de la fusión.
{% endalert %}


## Fusión basada en reglas {#rules-based-merging}

Puedes usar reglas para controlar cómo se resuelven los perfiles duplicados al ejecutar una fusión, de modo que se conserve el perfil de usuario más relevante. Cuando se establecen reglas, Braze conservará los perfiles que coincidan con tus criterios.

### Paso 1: Definir tus reglas {#step-1-define-your-rules}

1. Ve a **Audience** > **Manage Audience** > **Edit rules**.
2. En la sección **Profile to keep** del panel **Edit rules**, selecciona el **Identifier** para los perfiles que se conservarán al fusionar duplicados. Puede ser la dirección de correo electrónico o el número de teléfono.
3. En la sección **Resolving ties**, selecciona los criterios para determinar cómo resolver empates entre perfiles con criterios coincidentes de **Profile to keep**. Puedes seleccionar lo siguiente:<br>
- **Resolve ties using**: Created date, Updated date, Last session
- **Prioritization**: Newest, Oldest

![El panel "Edit rules" con secciones para seleccionar opciones de "Profile to keep" y "Resolving ties".]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

Por ejemplo, podrías conservar el perfil que tiene un número de teléfono. Si varios usuarios tienen el mismo número de teléfono, podrías resolver empates usando el campo **Updated date** y priorizar el usuario actualizado más recientemente.

### Paso 2: Previsualizar los resultados (opcional)

Después de guardar tus reglas, puedes previsualizar cómo funcionarán seleccionando **Generate a list of duplicates**. Braze generará tu vista previa y la enviará a tu dirección de correo electrónico como un archivo CSV que muestra qué usuarios se conservarían y fusionarían si se aplicaran tus reglas.

### Paso 3: Fusionar duplicados {#step-3-merge-duplicates}

Si estás conforme con los resultados de tu vista previa, vuelve a la página **Manage Audience** y selecciona **Merge all duplicates**.

{% alert warning %}
Los perfiles de usuario duplicados no se pueden recuperar después de la fusión.
{% endalert %}

## Fusión programada {#scheduled-merging}

De forma similar a la fusión basada en reglas, la fusión programada te permite automatizar la fusión de perfiles de usuario de forma diaria utilizando reglas preconfiguradas.

![La página "Manage Audience" con el botón "schedule".]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

Una vez activada la función, Braze asignará automáticamente un horario para realizar el proceso de fusión diariamente, aproximadamente a las 12 am en la zona horaria de la empresa del usuario. Puedes desactivar la fusión programada en cualquier momento. Braze notificará a los administradores de tu espacio de trabajo 24 horas antes de que ocurra la fusión programada, proporcionando un recordatorio y tiempo para revisar la configuración.

{% alert warning %}
Los perfiles de usuario duplicados no se pueden recuperar después de la fusión.
{% endalert %}

## ¿Por qué hay múltiples perfiles de usuario asociados a la misma dirección de correo electrónico? {#why-are-multiple-user-profiles-associated-with-the-same-email-address}

Braze almacena múltiples perfiles de usuario que comparten la misma dirección de correo electrónico cuando los perfiles se crean a través de diferentes identificadores, importaciones o sesiones anónimas antes de la identificación. Este es un comportamiento esperado cuando los usuarios no comparten un único `external_id`.

Antes de fusionar duplicados, usa el [punto de conexión de exportación de perfil de usuario por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para confirmar qué perfiles existen para una dirección de correo electrónico y qué campos contiene cada perfil. También puedes buscar por correo electrónico en **Audience** > **User Search** para revisar duplicados en el dashboard.

## Artículos relacionados {#related-articles}

- [Comportamiento de fusión de usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/)
- [POST: Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
- [Eliminar usuarios]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/)