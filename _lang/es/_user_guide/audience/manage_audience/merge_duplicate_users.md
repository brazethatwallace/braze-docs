---
nav_title: Fusionar usuarios duplicados
article_title: Fusionar usuarios duplicados
description: "Aprende a encontrar y fusionar usuarios duplicados en tu panel de Braze."
page_order: 4
---

# Fusionar usuarios duplicados {#merge-duplicate-users}

> Aprende a encontrar y fusionar usuarios duplicados para maximizar la efectividad de tus Campaigns y Canvas.

{% alert tip %}
Para fusionar usuarios duplicados usando la REST API de Braze, consulta [POST: Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% endalert %}

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

![La página de fusión individual para un perfil duplicado.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

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

![Un correo electrónico de Braze con un enlace al archivo CSV generado.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

En el siguiente ejemplo, Braze utiliza el ID externo del usuario para marcar perfiles duplicados e identificar cuál conservar. Si estos perfiles se fusionan de forma masiva, Braze utilizará el perfil con un ID externo como el nuevo perfil principal del usuario.

{% tabs local %}
{% tab example csv file %}
| Email Address    | External ID | Phone Number   | Braze ID              | Identifier for rule | Profile to keep | Profile to merge |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99   | (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             | (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             | (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### Comportamiento de la fusión {#merge-behavior}

Braze rellenará los campos vacíos del perfil conservado con valores del perfil fusionado. Para obtener una lista de los campos que se rellenarán, consulta [Comportamiento de la fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### Paso 3: Fusionar tus duplicados {#step-3-merge-your-duplicates}

Si estás conforme con los resultados de tu vista previa, selecciona **Merge all duplicates**.

{% alert warning %}
Los perfiles de usuario duplicados no se pueden recuperar después de la fusión.
{% endalert %}

![La página "Manage Audience" con "Merge all duplicates" resaltado.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

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