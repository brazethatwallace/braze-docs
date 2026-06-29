---
nav_title: Crear y administrar espacios de trabajo
article_title: Crear y administrar espacios de trabajo
page_order: 0
layout: dev_guide
guide_top_header: "Crear y administrar espacios de trabajo"
guide_top_text: "Este artículo explica cómo crear, configurar y administrar tus espacios de trabajo."
page_type: reference
description: "Este artículo explica cómo crear, configurar y administrar tus espacios de trabajo."

guide_featured_title: "Artículos de la sección"
guide_featured_list:
- name: Migrar datos entre espacios de trabajo
  link: /docs/user_guide/administer/global/create_and_manage_workspaces/migrate_workspace_data
  image: /assets/img/braze_icons/switch-horizontal-01.svg
---

<br>

# Crear y administrar espacios de trabajo {#create-and-manage-workspaces}

> Este artículo explica cómo crear, configurar y administrar tus espacios de trabajo.

## ¿Qué es un espacio de trabajo? {#what-is-a-workspace}

Todo lo que haces en Braze ocurre dentro de un espacio de trabajo. Los espacios de trabajo son un entorno compartido para que puedas rastrear y gestionar la interacción de aplicaciones móviles o sitios web relacionados. Los espacios de trabajo agrupan aplicaciones iguales o muy similares: por ejemplo, las versiones Android e iOS de tu aplicación móvil.

## Crear un espacio de trabajo {#creating-a-workspace}

### Paso 1: Ten un plan {#step-1-have-a-plan}

Antes de empezar, asegúrate de haber trabajado con tu equipo y tu administrador de incorporación de Braze para determinar la mejor configuración de espacio de trabajo para tu caso de uso. Para obtener más información sobre la planificación de tus espacios de trabajo en Braze, consulta nuestra guía [Primeros pasos: Espacios de trabajo]({{site.baseurl}}/user_guide/get_started/workspaces/).

### Paso 2: Añade tu espacio de trabajo {#step-2-add-your-workspace}

Puedes crear nuevos espacios de trabajo o cambiar entre espacios de trabajo existentes desde el menú desplegable de espacios de trabajo en el encabezado global.

1. Selecciona el menú desplegable de espacios de trabajo y luego selecciona <i class="fa-solid fa-square-plus" style="color: #0b8294;" aria-hidden="true"></i> **Crear espacio de trabajo**.

![El menú desplegable de espacios de trabajo con el botón "Crear espacio de trabajo".]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2. Dale un nombre a tu espacio de trabajo.

{% alert tip %}
Puede que quieras adoptar una convención de nomenclatura para que otras personas de tu empresa puedan encontrar fácilmente tu espacio de trabajo. Por ejemplo: "Upon Voyage US – Production" y "Upon Voyage US – Staging".
{% endalert %}

{:start="3"}
3. Selecciona **Crear**. Braze puede tardar unos segundos en crear tu espacio de trabajo.

![Modal "Crear espacio de trabajo" con el nombre "Upon Voyage US - Staging".]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

Se te dirigirá a la página **Configuración de la aplicación** para comenzar a añadir tus instancias de la aplicación. Puedes acceder a esta página en cualquier momento desde **Configuración** > **Configuración de la aplicación**.

![Página "Configuración de la aplicación" para el espacio de trabajo Upon Voyage US - Staging con un botón para añadir una aplicación.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### Paso 3: Añade tus instancias de la aplicación {#step-3-add-your-app-instances}

Nos referimos a los diferentes sitios y aplicaciones que se recopilan dentro de un espacio de trabajo como "instancias de la aplicación".

1. Desde la página **Configuración de la aplicación**, selecciona **+ Add app**.
2. Dale un nombre a tu instancia de la aplicación y selecciona en qué plataforma o plataformas se encuentra esta instancia. Si seleccionas múltiples plataformas, Braze creará una instancia de la aplicación para cada plataforma.

![Modal "Add New App to Upon Voyage US - Staging" con opciones para seleccionar los detalles de la aplicación.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3. Selecciona **Add app** para confirmar.

#### Claves de API de la aplicación {#app-api-keys}

Después de añadir tu instancia de la aplicación, tendrás acceso a su clave de API. La clave de API se utiliza para realizar solicitudes entre tu instancia de la aplicación y la API de Braze. La clave de API también es importante para integrar el SDK de Braze con tu aplicación o sitio web.

![Página de configuración de la aplicación Upon Voyage iOS con campos para la clave de API y el punto final de SDK.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
Debes crear instancias de la aplicación separadas para cada versión de tu aplicación en cada plataforma. Por ejemplo, si tienes versiones Free y Pro de tu aplicación tanto en iOS como en Android, crea cuatro instancias de la aplicación dentro de tu espacio de trabajo (aplicación Free iOS, aplicación Free Android, aplicación Pro iOS y aplicación Pro Android). Esto te dará cuatro claves de API para usar, una para cada instancia de la aplicación.
{% endalert %}

#### Versión del SDK en vivo {#live-sdk-version}

La versión del SDK en vivo que se muestra en la página Configuración de la aplicación para una aplicación específica es la versión más alta de la aplicación con al menos el 5 % del total de tus sesiones diarias y que tiene al menos 500 sesiones en el último día.

Este campo aparece después de que hayas integrado el SDK de Braze con tu aplicación o sitio web. Si hay una versión más reciente del SDK de Braze disponible para tu plataforma, se indicará aquí con la etiqueta "Newer Version Available".

![Sección "Versión del SDK en vivo" con un valor de campo de "5.4.0" y un icono que indica que hay una nueva versión disponible.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### Paso 4: Repite según sea necesario {#step-4-repeat-as-needed}

Repite los pasos 2 y 3 para configurar tantos espacios de trabajo como requiera tu plan. Como práctica recomendada, te sugerimos crear un espacio de trabajo de pruebas para la integración y las pruebas de campañas.

{% alert tip %}
**Añade un espacio de trabajo de pruebas**<br>Puedes realizar pruebas de la aplicación aislando completamente a ciertos usuarios de tu instancia de producción. Crea un nuevo espacio de trabajo y, cuando publiques tu aplicación, asegúrate de cambiar la clave de API que Braze está utilizando para que coincida con la de tu espacio de trabajo de producción en lugar de tu espacio de trabajo de pruebas.
{% endalert %}

## Administrar espacios de trabajo {#managing-workspaces}

### Añadir favoritos {#adding-favorites}

Puedes añadir espacios de trabajo favoritos para acceder aún más rápido a los espacios de trabajo que más utilizas.

![Menú desplegable de espacios de trabajo con la pestaña "Espacios favoritos".]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

Para añadir espacios de trabajo favoritos:

1. Selecciona el menú desplegable de tu perfil y luego selecciona **Gestiona tu cuenta**.
2. En la sección **Perfil de cuenta**, localiza el campo **Espacios favoritos**.
3. Selecciona tus espacios de trabajo de la lista.
4. Selecciona **Guardar cambios**.

No hay límite en la cantidad de espacios de trabajo que puedes marcar como favoritos, pero te recomendamos mantener esta lista corta por comodidad.

### Renombrar espacios de trabajo {#renaming-workspaces}

Para renombrar tu espacio de trabajo:

1. Ve a **Configuración** > **Configuración de la aplicación**.
2. Pasa el cursor sobre el nombre de tu espacio de trabajo y selecciona <i class="fa-solid fa-pencil" style="color: #0b8294;" aria-hidden="true"></i> **Editar**.
3. Dale un nuevo nombre a tu espacio de trabajo y luego selecciona <i class="fa-solid fa-square-check" style="color: #0b8294;" aria-hidden="true"></i> **Guardar**.

![El icono de lápiz apareciendo junto al nombre del espacio de trabajo.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Eliminar espacios de trabajo e instancias de la aplicación {#deleting-workspaces-and-app-instances}

Para eliminar tu espacio de trabajo o instancia de la aplicación:

1. Ve a **Configuración** > **Configuración de la aplicación**.
2. Selecciona **Eliminar espacio de trabajo** para eliminar el espacio de trabajo correspondiente, o selecciona el icono de papelera junto a la instancia de la aplicación correspondiente.

No puedes eliminar instancias de la aplicación o espacios de trabajo que se estén utilizando actualmente para segmentar usuarios o que tengan más de 1000 usuarios. Si intentas hacerlo, recibirás un mensaje de error. Para proceder y eliminarlos, [crea un caso de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support/) que incluya un enlace al dashboard y el nombre de la instancia de la aplicación o espacio de trabajo que se va a eliminar.

{% alert warning %}
¡Ten cuidado al eliminar espacios de trabajo! Una vez que se elimina un espacio de trabajo, no se puede restaurar.
{% endalert %}

![La página Configuración de la aplicación con un botón para eliminar un espacio de trabajo y un icono de papelera para eliminar una aplicación.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Debo crear un nuevo espacio de trabajo cuando lanzo una aplicación actualizada? {#should-i-create-a-new-workspace-when-im-releasing-an-updated-app}

Esto depende de si estás actualizando tu aplicación o creando una completamente nueva.

#### Actualizar tu aplicación {#updating-your-app}

Si estás actualizando tu aplicación, debes separar las versiones antigua y nueva creando una nueva instancia de la aplicación dentro del mismo espacio de trabajo. De esta manera, puedes segmentar eficazmente a los usuarios de la nueva versión cuando selecciones esa aplicación durante la segmentación. Si quieres enviar mensajes a los usuarios que están en la versión anterior, puedes usar filtros para [segmentar por la versión anterior de la aplicación]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

Si creas un nuevo espacio de trabajo, tus usuarios existirán en dos lugares: el espacio de trabajo antiguo y el nuevo. También podrían tener el mismo token de notificaciones push. Esto puede llevar a que los usuarios reciban un mensaje de marketing destinado solo a los usuarios del espacio de trabajo antiguo, incluso si ya han actualizado.

#### Lanzar una nueva aplicación {#releasing-a-new-app}

Si estás lanzando una aplicación completamente nueva en la tienda de aplicaciones, debes crear un nuevo espacio de trabajo. Al crear un nuevo espacio de trabajo, todos los datos históricos y perfiles de usuario de la versión anterior de la aplicación no existirán en este nuevo espacio de trabajo. Así, después de que los usuarios existentes actualicen a la nueva versión de la aplicación, tendrán un nuevo perfil creado sin ninguno de los datos de comportamiento de la aplicación anterior.

### Tengo múltiples instancias de la aplicación en un espacio de trabajo: ¿cómo puedo asegurarme de dirigirme solo a una aplicación con mi mensaje? {#singular-app}

Para asegurarte de que tu mensaje solo se dirija a una aplicación específica, añade un segmento que solo incluya a los usuarios de las instancias de la aplicación elegidas. Esto es especialmente importante si un usuario puede tener dos tokens de notificaciones push para diferentes instancias de la aplicación en el mismo espacio de trabajo. En este escenario, los usuarios podrían recibir una notificación para una aplicación diferente a la que están usando. ¡No es una experiencia ideal!

De forma predeterminada, un segmento se dirige a todas las aplicaciones y sitios web del espacio de trabajo. Para configurar un segmento que solo se dirija a una aplicación o sitio web:

1. Crea un segmento con un nombre significativo. En Braze, usamos el formato "All Users ({Name} {Platform})". Por ejemplo, "All Users (Upon Voyage iOS)".
2. Para **Apps and websites targeted**, selecciona **Users from specific apps**.
3. En el menú desplegable **Specific apps**, selecciona tu aplicación o sitio.

![Segmento que se dirige a usuarios de aplicaciones específicas.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

Luego puedes añadir este segmento a tu mensaje y comenzar a refinar aún más tu audiencia con segmentos y filtros adicionales si es necesario.

#### Campaigns

Para Campaigns, añade tu segmento al paso **Target Audiences** del compositor.

#### Canvas

En Canvas, añade tu segmento a tus pasos de mensaje, en la sección **Delivery Validations**. Las validaciones de entrega verifican que tu audiencia cumple con tus criterios de entrega en el momento del envío del mensaje. Recuerda especificar las validaciones de entrega para cada paso de mensaje para asegurarte de que se entregará a la aplicación correcta. No es necesario segmentar a nivel de entrada.

{% details Expande para ver los pasos en el flujo de trabajo original de Canvas %}

En el flujo de trabajo original de Canvas, añade tu segmento a nivel de componente de Canvas en la sección **Audience**. No es necesario segmentar a nivel de entrada.

{% enddetails %}

## Próximos pasos {#next-steps}

Después de crear tu espacio de trabajo, configúralo:

- [Configuración del espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/workspace_settings/) para configurar claves de API, preferencias de correo electrónico, configuración de push y más.
- [Administrar usuarios de la empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/) para añadir usuarios y asignar permisos para este espacio de trabajo.