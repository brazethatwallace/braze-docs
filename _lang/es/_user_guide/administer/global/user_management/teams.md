---
nav_title: Equipos
article_title: Equipos
page_order: 2
page_type: reference
alias: /teams/
description: "Este artículo de referencia explica cómo utilizar Braze Teams en el panel. Aquí puedes aprender a crear equipos, asignar roles y asignar etiquetas y filtros."

---

# Equipos {#teams}

> Como administrador de Braze, puedes agrupar a los usuarios de tu empresa en equipos con diferentes roles y permisos de usuario. Esto te permite tener varios grupos de usuarios de la empresa, sin relación entre sí, trabajando juntos en un mismo espacio de trabajo, separando los tipos de contenido que se pueden editar.

Los equipos se pueden configurar según la ubicación de la base de clientes, el idioma y los atributos personalizados, de modo que los miembros del equipo y los que no lo son tengan un acceso diferente a las características de mensajería y a los datos de clientes. Se pueden asignar filtros y etiquetas de equipo en varias herramientas de participación. No hay límite en cuanto al número de equipos que puedes crear en tu espacio de trabajo.

Los equipos no están disponibles en todos los contratos de Braze. Para acceder a esta característica, ponte en contacto con tu director de cuentas de Braze o [contáctanos](mailto:success@braze.com) para una consulta.

## ¿En qué se diferencian los equipos de los conjuntos de permisos y los roles? {#how-do-teams-differ-from-permission-sets-and-roles}

{% multi_lang_include permissions/differences.md content="Differences" %}

## Crear equipos {#creating-teams}

Ve a **Configuración** > **Equipos internos** y selecciona <i class="fas fa-plus" aria-label="Añadir"></i> **Añadir equipo**.

![Ventana para añadir un nuevo equipo.]({% image_buster /assets/img_archive/adding_a_team.png %})

Introduce el **nombre del equipo**. Si lo deseas, usa el campo **Definir equipo (opcional)** para seleccionar un atributo personalizado, una ubicación o un idioma para definir con más detalle a qué datos de usuario tiene acceso el equipo. Por ejemplo, un posible caso de uso es realizar [pruebas con equipos](#test-with-teams) creando un equipo de desarrollo que solo tenga acceso a usuarios de prueba, identificados por un atributo personalizado. Otro caso de uso es restringir la comunicación con los usuarios en función del producto.

Si un equipo se define por un atributo personalizado, un idioma o un país, puedes usar el equipo para filtrar usuarios finales en características como Campaigns, Canvas, Content Cards, Segments y más. Para más información, consulta [Asignar etiquetas de equipo](#tags-and-filters).

## Asignar usuarios a equipos {#assign-users-to-teams}

Los administradores de Braze y los usuarios limitados con el permiso a nivel de empresa "Can Manage Company Settings" pueden asignar permisos a nivel de equipo a un usuario de la empresa con acceso limitado. Cuando se asigna a un equipo, los usuarios de la empresa se limitan a solo leer o escribir datos disponibles para sus equipos particulares, como el idioma del usuario, la ubicación o un atributo personalizado, según se definió cuando se creó el equipo.

### Limitar los permisos de un usuario de la empresa sin eliminar al usuario {#limit-company-user-permissions-without-deleting-a-user}

Para impedir que un usuario de la empresa inicie sesión y al mismo tiempo conservar su cuenta, [suspende al usuario]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#suspending-company-users). La suspensión pone la cuenta en un estado inactivo en el que el usuario no puede iniciar sesión.

Si el usuario debe poder seguir iniciando sesión con capacidades limitadas, ve a **Configuración** > **Usuarios de la empresa**, selecciona al usuario y edita sus permisos. Elimina los permisos a nivel de espacio de trabajo para Campaigns, Canvas, Segments y datos de usuario, y deja solo el acceso mínimo, por ejemplo, "View Media Library Assets". Para más información, consulta [Editar los permisos de un usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions).

Los permisos de equipo funcionan sobre los permisos del espacio de trabajo. Si asignas al usuario a un equipo, otorga solo los permisos mínimos a nivel de equipo que necesite y no otorgues permisos para Campaigns, Canvas, Segments ni perfiles de usuario. El usuario permanece en el espacio de trabajo y puede iniciar sesión, pero no puede realizar la mayoría de las acciones de mensajería o audiencia.

Para asignar un usuario a un equipo, ve a **Configuración** > **Usuarios de la empresa** y selecciona al usuario que deseas agregar a tu equipo.

Luego realiza los siguientes pasos:

1. En la sección **Permisos a nivel de espacio de trabajo**, agrega al usuario al espacio de trabajo correspondiente si aún no está incluido.

![Permisos a nivel de espacio de trabajo con el permiso de plantilla de banner configurado.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Selecciona **+ Add team-level permissions** y luego selecciona el **equipo** al que deseas agregar a este usuario.
3. Asigna permisos específicos desde la sección de permisos de **equipo**.

![Permisos de plantilla de página de destino a nivel de equipo.]({% image_buster /assets/img/teams.png %})

### Permisos disponibles a nivel de equipo {#available-team-level-permissions}

Los siguientes son todos los permisos disponibles que puedes asignar a nivel de equipo. Los permisos que no aparecen aquí solo se otorgan a nivel de espacio de trabajo, y estos permisos aparecerán como "--" en la columna de permisos de **equipos**.

- Ver Campaigns
- Editar Campaigns
- Archivar Campaigns
- Lanzar Campaigns
- Aprobar Campaigns
- Ver Canvas
- Editar Canvas
- Archivar Canvas
- Lanzar Canvas
- Aprobar Canvas
- Ver Content Blocks
- Editar Content Blocks
- Archivar Content Blocks
- Lanzar Content Blocks
- Ver Segments
- Editar Segments
- Archivar Segments
- Ver plantillas de IAM
- Editar plantillas de IAM
- Archivar plantillas de IAM
- Ver plantillas de correo electrónico
- Editar plantillas de correo electrónico
- Archivar plantillas de correo electrónico
- Ver plantillas de webhook
- Editar plantillas de webhook
- Archivar plantillas de webhook
- Ver plantillas de enlaces de correo electrónico
- Editar plantillas de enlaces de correo electrónico
- Ver activos de la biblioteca multimedia
- Editar activos de la biblioteca multimedia
- Eliminar activos de la biblioteca multimedia
- Exportar datos de usuario
- Ver perfiles de usuario (PII oculta)
- Ver PII
- Editar usuarios del panel
- Editar plantillas de Canvas
- Ver plantillas de Canvas
- Archivar plantillas de Canvas
- Ver informes del panel
- Editar informes del panel
- Eliminar informes del panel

Para ver las descripciones de lo que incluye cada permiso de usuario y cómo utilizarlos, consulta nuestra sección de [Permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Asignar etiquetas de equipo {#tags-and-filters}

Puedes asignar un equipo a Canvas, Campaigns, Content Cards, Segments, plantillas de correo electrónico, plantillas de webhook, Content Blocks y activos de la biblioteca de medios con el filtro **Añadir equipo**.

En el caso de Canvas, los filtros de equipo solo validan a los usuarios en la entrada de Canvas. Después de que un usuario entra en un Canvas, sigue recibiendo mensajes de todos los pasos del Canvas aunque sus atributos cambien y ya no coincidan con los criterios del filtro de equipo. Los filtros de equipo no se comportan como las validaciones de entrega, que reevalúan a los usuarios en cada paso del mensaje.

![Añadir una etiqueta de equipo a una Campaign.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Según las definiciones aplicadas cuando se creó el equipo, cuando se asigna un filtro de equipo, la audiencia de esa herramienta de participación se restringe a los perfiles de usuario que coincidan con la definición.
- Según los permisos asignados, los miembros del equipo solo pueden acceder a las herramientas de participación del panel que tengan configurado su filtro de equipo. Si tienen permisos de espacio de trabajo limitados o nulos, deben añadir un filtro de equipo a ciertos objetos antes de poder guardarlos o lanzarlos. Los miembros del equipo también pueden filtrar Canvas, Campaigns, Content Cards y Segments por equipo para identificar el contenido relevante para ellos.
- Los usuarios con permisos solo a nivel de equipo no ven los filtros **Creado por** ni **Última edición por** en las páginas de Segments, Campaigns o Canvas. Braze oculta estos filtros para que los usuarios con permisos solo de equipo no puedan explorar todos los usuarios de Braze desde esos menús desplegables.

### Ejemplos {#use-cases}

Considera los siguientes dos escenarios para una especialista en marketing en Braze llamada Michelle. Michelle es miembro de un equipo llamado "Desarrollo". Tiene acceso a todos los permisos a nivel de equipo del equipo de Desarrollo.

{% tabs %}
{% tab Escenario 1: solo permisos de equipo %}

En este escenario, Michelle es una usuaria limitada que no tiene permisos a nivel de espacio de trabajo. Sus permisos se ven así:

![Permisos personalizados sin permisos a nivel de espacio de trabajo y 16 permisos basados en equipo.]({% image_buster /assets/img_archive/scenario1.png %})

Según los permisos asignados a Michelle, cada vez que crea una campaña, solo puede asignar el equipo "Desarrollo" a esa campaña. No puede lanzar la campaña a menos que el equipo esté asignado, y no puede ver ni acceder a ninguna otra etiqueta de equipo.

![Menú desplegable de etiqueta de equipo de Campaign que solo muestra la etiqueta de equipo "Desarrollo".]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Escenario 2: permisos de equipo y de espacio de trabajo %}

En este escenario, Michelle sigue siendo miembro del equipo de Desarrollo, pero también tiene un permiso adicional a nivel de espacio de trabajo.

![Permisos personalizados con un permiso a nivel de espacio de trabajo y 15 permisos basados en equipo.]({% image_buster /assets/img_archive/scenario2.png %})

Dado que Michelle tiene el permiso a nivel de espacio de trabajo de "Acceder a Campaigns, Canvas, tarjetas, Content Blocks, conmutadores de características, Segments, biblioteca de medios y centros de preferencias", puede ver y asignar otros filtros de equipo a la campaña que crea.

![Menú desplegable de etiqueta de equipo de Campaign con múltiples etiquetas de equipo.]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Al igual que en el primer escenario, Michelle debe añadir la etiqueta del equipo de Desarrollo a la campaña antes de poder lanzarla.

{% endtab %}
{% endtabs %}

## Prueba con equipos {#test-with-teams}

Un posible ejemplo de equipos es crear un sistema de aprobación basado en equipos para probar y lanzar contenido en un entorno de producción.

Para ello, crea un equipo "Desarrollo" que solo tenga acceso a usuarios de prueba. Puedes limitar un equipo para que solo acceda a usuarios de prueba si tus usuarios de prueba son identificables mediante un atributo personalizado. Luego, añade el atributo personalizado como definición al crear o editar el equipo (consulta la sección anterior [Crear equipos](#creating-Teams)). Tus aprobadores deben tener acceso a todos los usuarios.

El proceso general sería el siguiente:

1. El equipo de Desarrollo crea una Campaign y añade la etiqueta de equipo "Desarrollo".
2. El equipo de Desarrollo lanza la Campaign a los usuarios de prueba.
3. El equipo de Aprobación valida el diseño local de la Campaign, la promueve y la lanza. Para lanzarla, el equipo de Aprobación cambia la etiqueta de equipo de "Desarrollo" a "[Todos los equipos]" y relanza la Campaign.

Para cambios en Campaigns activas:

1. El equipo de Desarrollo clona la Campaign en ejecución, añade la etiqueta de equipo "Desarrollo" y guarda.
2. El equipo de Desarrollo realiza las ediciones y las comparte con el equipo de Aprobación.
3. El equipo de Aprobación elimina la etiqueta de equipo "Desarrollo", pausa la Campaign anterior y lanza la nueva Campaign.

## Archivar un equipo existente {#archive-an-existing-team}

Puedes archivar equipos desde la página **Equipos internos**.

Selecciona uno o varios equipos para archivar. Si el equipo no está asociado con ningún objeto dentro de Braze, se archiva de inmediato. Si el equipo está asociado con un objeto, se te presenta la opción de eliminar el equipo después del proceso de archivado o reemplazar el equipo.

![Archivado de un equipo asociado con un objeto en Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Los administradores de Braze pueden desarchivar un equipo seleccionando el equipo archivado y seleccionando **Desarchivar**.