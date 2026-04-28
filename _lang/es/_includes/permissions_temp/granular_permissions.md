{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

## Creación de un conjunto de permisos {#creating-a-permission-set}

Usa conjuntos de permisos para agrupar permisos relacionados con áreas temáticas o acciones específicas. Puedes aplicar conjuntos de permisos a los usuarios del dashboard que necesiten el mismo acceso en diferentes espacios de trabajo. Para crear un conjunto de permisos, ve a **Configuración** > **Configuración de permisos** y selecciona **Crear conjunto de permisos**. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
|Nombre|Permisos|
|-----------|----------------|
|Desarrolladores|«Ver claves de API», «Editar claves de API», «Ver grupos internos», «Editar grupos internos», «Ver registro de actividad de mensajes», «Ver registro de eventos de usuario», «Ver identificadores de API», «Ver panel de uso de API», «Ver límites de API», «Ver alertas de uso de API», «Editar alertas de uso de API», «Ver depurador de SDK», «Editar depurador de SDK».|
|Especialistas en marketing|«Ver Campaigns», «Editar Campaigns», «Archivar Campaigns», «Ver Canvas», «Editar Canvas», «Archivar Canvas», «Ver reglas de limitación de frecuencia», «Editar reglas de limitación de frecuencia», «Ver priorización de mensajes», «Editar priorización de mensajes», «Ver Content Blocks», «Ver conmutadores de características», «Editar conmutadores de características», «Archivar conmutadores de características», «Ver Segments», «Editar Segments», «Editar grupo de control global», «Ver plantillas de IAM», «Editar plantillas de IAM», «Archivar plantillas de IAM», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Archivar plantillas de correo electrónico», «Ver plantillas de webhook», «Editar plantillas de webhook», «Archivar plantillas de webhook», «Ver plantillas de enlaces de correo electrónico», «Editar plantillas de enlaces de correo electrónico», «Ver activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias», «Editar informes del dashboard», «Ver plantillas de banners», «Ver configuración de localización», «Usar Operator», «Ver agentes de Decisioning Studio».|
|Gestión de usuarios|«Editar usuarios del dashboard», «Ver equipos», «Editar equipos», «Archivar equipos».|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Creación de un rol {#creating-a-role}

Los roles permiten una mayor estructura al agrupar los permisos personalizados individuales con los controles de acceso al espacio de trabajo. Esto es especialmente útil si tienes muchas marcas o espacios de trabajo regionales en un mismo dashboard. Con los roles, puedes añadir usuarios del dashboard a los espacios de trabajo adecuados y concederles directamente los permisos asociados. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nombre del rol    | Espacio de trabajo | Permisos
----------- | ----------- | ---------
| Especialista en marketing - Marcas de moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | «Ver Campaigns», «Editar Campaigns», «Archivar Campaigns», «Ver Canvas», «Editar Canvas», «Archivar Canvas», «Ver Content Blocks», «Editar Content Blocks», «Archivar Content Blocks», «Lanzar Content Blocks», «Ver conmutadores de características», «Editar conmutadores de características», «Archivar conmutadores de características», «Ver Segments», «Editar Segments», «Ver plantillas de banners», «Editar plantillas de banners», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Ver activos de la biblioteca multimedia», «Editar activos de la biblioteca multimedia», «Eliminar activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias». |
| Especialista en marketing - Marcas de cuidado de la piel | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} |«Ver Campaigns», «Editar Campaigns», «Archivar Campaigns», «Ver Canvas», «Editar Canvas», «Archivar Canvas», «Ver Content Blocks», «Editar Content Blocks», «Archivar Content Blocks», «Lanzar Content Blocks», «Ver conmutadores de características», «Editar conmutadores de características», «Archivar conmutadores de características», «Ver Segments», «Editar Segments», «Ver plantillas de banners», «Editar plantillas de banners», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Ver activos de la biblioteca multimedia», «Editar activos de la biblioteca multimedia», «Eliminar activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias».|
| Gestión de usuarios - Todas las marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | «Editar usuarios del dashboard», «Ver equipos», «Editar equipos», «Archivar equipos»|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

## ¿En qué se diferencian los conjuntos de permisos y los roles de los equipos? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions.md content="Differences" %}

### Consideraciones para agregar permisos de usuario a equipos {#considerations-for-adding-user-permissions-to-teams}

Es posible que encuentres dificultades al intentar guardar los permisos en el dashboard de Braze, especialmente al añadir o eliminar usuarios de un espacio de trabajo, o al añadirlos a un equipo. El botón **Guardar/Actualizar usuarios** puede aparecer en gris si los permisos del usuario son idénticos a los que ya tiene a nivel del espacio de trabajo. Esta restricción existe porque no tiene sentido tener un equipo si todos los usuarios poseen los mismos permisos que todo el espacio de trabajo.

Para añadir correctamente un usuario a un equipo manteniendo los mismos permisos, no asignes ningún permiso a nivel del espacio de trabajo. En su lugar, asigna permisos exclusivamente a nivel de equipo.

## Usuarios limitados {#limited-users}

Los usuarios limitados tienen permisos específicos que les permiten gestionar determinados aspectos del dashboard de Braze, pero con restricciones en comparación con los administradores de la empresa y los administradores del espacio de trabajo.

| Ámbito | Descripción |
| --- | --- |
| Permisos | Los usuarios limitados pueden editar los permisos de otros usuarios limitados si tienen el permiso «Editar usuarios del dashboard». También pueden crear nuevos usuarios limitados y modificar sus conjuntos de permisos. Sin embargo, no pueden crear ni gestionar cuentas de administrador de la empresa. |
| Limitaciones de roles | Si un usuario limitado tiene todos los permisos excepto «Administrador del espacio de trabajo», seguirá teniendo acceso a todos los demás permisos que normalmente se conceden a un administrador del espacio de trabajo. |
| Visibilidad de los permisos | Si un usuario limitado tiene el permiso «Editar usuarios del dashboard» para un espacio de trabajo (como Dev) pero no para otro (como Prod), no verá los permisos del espacio de trabajo Prod en la página de detalles de los usuarios del dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Comparación de usuarios limitados {#comparing-limited-users}

| Tipo de usuario limitado | Descripción |
| --- | --- |
| Administrador del espacio de trabajo | Los administradores del espacio de trabajo tienen permisos específicos para gestionar los espacios de trabajo, pero no tienen la misma autoridad que los administradores de la empresa. Los usuarios limitados pueden heredar permisos similares a los de los administradores del espacio de trabajo si tienen marcados los permisos necesarios. |
| Administrador (administrador de la empresa) | Los administradores de la empresa tienen permisos más amplios, incluida la posibilidad de eliminar usuarios del dashboard. Sin embargo, no pueden eliminar sus propias cuentas y deben ponerse en contacto con otro administrador de la empresa para realizar esa acción. |
| Acceso de solo lectura | Para acceder a algunas partes del dashboard, como la página de Campaigns, los usuarios deben tener asignados permisos de visualización. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Error de acceso limitado {#limited-access-error}

Los usuarios pueden encontrar mensajes como «Necesitas el permiso "Ver páginas de inicio" para acceder a esta página». En tales casos, el usuario y el administrador de la cuenta deben verificar que se hayan concedido los permisos necesarios. Si es así, intenta resolver el problema desactivando y volviendo a habilitar los permisos del usuario.

{% alert note %}
No es posible fusionar o importar permisos de usuario de un usuario del dashboard a otro.
{% endalert %}

## Editar los permisos de un usuario {#editing-a-users-permissions}

Para editar los permisos actuales de administrador, empresa o espacio de trabajo de un usuario, ve a **Configuración** > **Usuarios de la empresa** y selecciona su nombre.

![La página «Usuarios de la empresa» en Braze muestra una tabla con los usuarios del dashboard.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Admin %}

### Administrador {#admin}

Los administradores tienen acceso a todas las funciones y la posibilidad de modificar cualquier configuración de la empresa. Pueden:

- Cambiar [la configuración de aprobación]({{site.baseurl}}/user_guide/messaging/governance/approvals/#turning-on-the-approval-workflow)
- Añadir, editar, eliminar, suspender o anular la suspensión de otros [usuarios de Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/#adding-company-users)
- Exportar usuarios de Braze como archivo CSV

Para conceder o eliminar privilegios de administrador, selecciona **Este usuario es un administrador** y luego selecciona **Actualizar usuario**.

![Los detalles del usuario seleccionado con la casilla de verificación de administrador activada.]({% image_buster /assets/img/braze_permissions/admin_level_permissions.png %}){: style="max-width:70%;"}

{% alert warning %}
Si eliminas los privilegios de administrador de un usuario, este no podrá acceder a Braze hasta que le asignes al menos un [permiso a nivel de empresa o de espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa {#company}

Para gestionar los siguientes permisos a nivel de empresa para un usuario, marca o desmarca la casilla junto a ese permiso. Cuando hayas terminado, selecciona **Actualizar usuario**.

|Nombre del permiso|Descripción|
|----------|-----------|
|Administrar configuración de empresa|Permite a los usuarios modificar la configuración de permisos y la verificación del remitente.|
|Crear y eliminar espacios de trabajo|Permite a los usuarios crear y eliminar espacios de trabajo.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Workspace %}

### Espacio de trabajo {#workspace}

Puedes dar a un usuario permisos diferentes para cada espacio de trabajo al que pertenezca en Braze. Para gestionar los permisos a nivel del espacio de trabajo, selecciona **Seleccionar espacios de trabajo y permisos** y luego elige los permisos manualmente o asigna un [conjunto de permisos o un rol]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que hayas creado previamente. Si necesitas dar a un usuario permisos diferentes para distintos espacios de trabajo, repite este proceso tantas veces como sea necesario. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Select manually %}

En **Espacios de trabajo**, selecciona uno o varios espacios de trabajo en el menú desplegable. Luego, en **Permisos**, selecciona uno o varios permisos. Se les asignarán estos permisos solo para los espacios de trabajo que hayas seleccionado. Opcionalmente, puedes seleccionar **Asignar acceso de administrador al espacio de trabajo** si prefieres concederles permisos completos para este espacio de trabajo.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel del espacio de trabajo seleccionados manualmente en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Assign permission set %}

En **Espacios de trabajo**, selecciona uno o varios espacios de trabajo en el menú desplegable. Luego, en **Conjuntos de permisos**, selecciona un conjunto de permisos. Se les asignarán estos permisos solo para los espacios de trabajo que hayas seleccionado.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel del espacio de trabajo asignados a través de un conjunto de permisos en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Assign role %}

En **Espacios de trabajo**, selecciona uno o varios espacios de trabajo en el menú desplegable. Luego, en **Rol**, elige un rol. Se les asignarán estos permisos solo para los espacios de trabajo que hayas seleccionado.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel del espacio de trabajo asignados a través de un rol en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportación de permisos de usuario {#exporting-user-permissions}

Para descargar una lista de tus usuarios y sus permisos, ve a **Configuración** > **Usuarios de la empresa** y selecciona **Exportar usuarios**. En breve se enviará un archivo CSV a tu dirección de correo electrónico.

![La página «Usuarios de la empresa» en Braze con la opción «Exportar usuarios» resaltada.]({% image_buster /assets/img/braze_permissions/exporting_user_permissions.png %})

## Lista de permisos {#list-of-permissions}

### Mensajería {#messaging}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Campaigns | Ver Campaigns | Ver Campaigns |
| Campaigns | Lanzar Campaigns | Iniciar, detener, pausar o reanudar Campaigns existentes |
| Campaigns | Archivar Campaigns | Mover Campaigns al archivo |
| Campaigns | Editar Campaigns | Crear y actualizar Campaigns |
| Campaigns | Aprobar y rechazar Campaigns | Aprobar o rechazar Campaigns. El [flujo de trabajo de aprobación de Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas si te interesa participar en el acceso anticipado. |
| Canvas | Ver Canvas | Ver Canvas |
| Canvas | Archivar Canvas | Mover Canvas al archivo |
| Canvas | Editar Canvas | Crear y actualizar Canvas |
| Canvas | Lanzar Canvas | Iniciar, detener, pausar o reanudar Canvas existentes |
| Canvas | Aprobar y rechazar Canvas | Aprobar o rechazar Canvas. El [flujo de trabajo de aprobación de Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas si te interesa participar en el acceso anticipado. |
| Conmutadores de características | Ver conmutadores de características | Ver conmutadores de características |
| Conmutadores de características | Archivar conmutadores de características | Mover conmutadores de características al archivo |
| Conmutadores de características | Editar conmutadores de características | Crear y actualizar conmutadores de características |
| Limitación de frecuencia | Ver reglas de limitación de frecuencia | Ver reglas de limitación de frecuencia |
| Limitación de frecuencia | Editar reglas de limitación de frecuencia | Crear y actualizar reglas de limitación de frecuencia |
| Páginas de inicio | Ver páginas de inicio | Ver páginas de inicio |
| Páginas de inicio | Publicar páginas de inicio | Activar un borrador de página de inicio |
| Páginas de inicio | Editar borradores de páginas de inicio | Crear y guardar borradores de páginas de inicio |
| Configuración de archivado de mensajes | Ver configuración de archivado de mensajes | Ver la configuración de archivado de mensajes sin realizar cambios |
| Configuración de archivado de mensajes | Editar configuración de archivado de mensajes | Crear y actualizar la configuración de archivado de mensajes |
| Priorización de mensajes | Ver priorización de mensajes | Ver la configuración de priorización de mensajes sin realizar cambios |
| Priorización de mensajes | Editar priorización de mensajes | Crear y actualizar la configuración de priorización de mensajes |
| WhatsApp Flows | Ver WhatsApp Flows | Ver todos los WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Audiencia {#audience}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Grupo de control global | Ver grupo de control global | Ver la página de configuración del grupo de control global |
| Grupo de control global | Editar grupo de control global | Crear y guardar cambios en el grupo de control global. Los usuarios con el permiso «Editar grupo de control global» también deben tener permisos para «Editar Campaigns» y «Editar Canvas». Los usuarios con el permiso «Editar grupo de control global» también obtienen el permiso «Ver grupo de control global». |
| Ubicaciones | Archivar ubicaciones | Mover ubicaciones al archivo |
| Ubicaciones | Ver ubicaciones | Ver ubicaciones |
| Ubicaciones | Editar ubicaciones | Crear y editar ubicaciones |
| Segments | Ver Segments | Ver Segments. Los usuarios deben tener el permiso «Ver Segments» para tener el permiso «Editar Segments» o «Archivar Segments». |
| Segments | Archivar Segments | Archivar y desarchivar Segments. Los usuarios con el permiso «Archivar Segments» también deben tener el permiso «Ver Segments». |
| Segments | Editar Segments | Crear y actualizar Segments. Los usuarios con el permiso «Editar Segments» también deben tener el permiso «Ver Segments». |
| Datos de usuario | Ver importación de usuarios | Ver importaciones de usuarios en CSV sin realizar cambios |
| Datos de usuario | Importar usuarios | Cargar usuarios al dashboard |
| Datos de usuario | Editar datos de usuario | Crear y actualizar datos de usuario |
| Datos de usuario | Exportar datos de usuario | Descargar usuarios desde el dashboard |
| Registros de eliminación de usuarios | Ver registros de fusión de usuarios | Ver una lista de registros de fusión de usuarios |
| Usuarios | Ver perfiles de usuario (PII censurada) | Ver perfiles de usuario de manera compatible con PII |
| Usuarios duplicados | Fusionar usuarios duplicados | Combinar usuarios duplicados en un solo usuario. Los duplicados se eliminan después de la fusión. |
| Usuarios | Eliminar usuarios | Eliminar permanentemente usuarios del dashboard de forma individual o masiva |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Plantilla {#template}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Plantillas de banners | Ver plantillas de banners | Ver plantillas de banners |
| Plantillas de banners | Archivar plantillas de banners | Mover plantillas de banners al archivo |
| Plantillas de banners | Editar plantillas de banners | Crear y actualizar plantillas de banners |
| Plantillas de Canvas | Ver plantillas de Canvas | Ver plantillas de Canvas |
| Plantillas de Canvas | Archivar plantillas de Canvas | Mover plantillas de Canvas al archivo |
| Plantillas de Canvas | Crear y editar plantillas de Canvas | Crear y actualizar plantillas de Canvas |
| Content Blocks | Ver Content Blocks | Ver Content Blocks |
| Content Blocks | Lanzar Content Blocks | Lanzar Content Blocks |
| Content Blocks | Archivar Content Blocks | Mover Content Blocks al archivo |
| Content Blocks | Editar Content Blocks | Crear y actualizar Content Blocks |
| Plantillas de enlaces de correo electrónico | Ver plantillas de enlaces de correo electrónico | Ver plantillas de enlaces sin realizar cambios |
| Plantillas de enlaces de correo electrónico | Editar plantillas de enlaces de correo electrónico | Crear y actualizar plantillas de enlaces |
| Plantillas de correo electrónico | Ver plantillas de correo electrónico | Ver plantillas de correo electrónico |
| Plantillas de correo electrónico | Archivar plantillas de correo electrónico | Mover plantillas de correo electrónico al archivo |
| Plantillas de correo electrónico | Editar plantillas de correo electrónico | Crear y actualizar plantillas de correo electrónico |
| Plantillas de IAM | Ver plantillas de IAM | Ver plantillas de mensajes dentro de la aplicación sin realizar cambios |
| Plantillas de IAM | Archivar plantillas de IAM | Mover plantillas de IAM al archivo |
| Plantillas de IAM | Editar plantillas de IAM | Crear y actualizar plantillas de mensajes dentro de la aplicación |
| Plantillas de páginas de inicio | Ver plantillas de páginas de inicio | Ver plantillas de páginas de inicio |
| Plantillas de páginas de inicio | Archivar plantillas de páginas de inicio | Mover plantillas de páginas de inicio al archivo |
| Plantillas de páginas de inicio | Editar plantillas de páginas de inicio | Crear y actualizar plantillas de páginas de inicio |
| Plantillas de webhook | Ver plantillas de webhook | Ver plantillas de webhook sin realizar cambios |
| Plantillas de webhook | Archivar plantillas de webhook | Mover plantillas de webhook al archivo |
| Plantillas de webhook | Editar plantillas de webhook | Crear y actualizar plantillas de webhook |
| Plantillas de mensajes de WhatsApp | Ver plantillas de mensajes de WhatsApp | Permite a los usuarios ver [plantillas de mensajes de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-2-compose-your-whatsapp-message) |
| Plantillas de mensajes de WhatsApp | Editar plantillas de mensajes de WhatsApp | Permite a los usuarios crear plantillas de mensajes de WhatsApp en el generador de plantillas. Esta característica está actualmente en acceso anticipado. |
| Plantillas de mensajes de WhatsApp de Meta | Ver plantillas de mensajes de WhatsApp de Meta | Ver todas las plantillas de WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Integraciones de socios {#partner-integrations}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Integraciones de Currents | Ver integración de Currents | Ver integraciones de Currents |
| Integraciones de Currents | Editar integraciones de Currents | Crear, actualizar y eliminar integraciones de Currents |
| Socios tecnológicos | Editar socios tecnológicos | Crear y actualizar socios tecnológicos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Configuración de datos {#data-settings}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Catálogos | Ver catálogos | Ver catálogos y selecciones |
| Catálogos | Eliminar catálogos | Eliminar catálogos de forma permanente |
| Catálogos | Exportar catálogos | Descargar catálogos desde el dashboard |
| Catálogos | Editar catálogos | Crear y actualizar catálogos y selecciones |
| Ingesta de datos de Cloud | Editar ingesta de datos de Cloud | Crear, actualizar y eliminar fuentes y sincronizaciones |
| Atributos personalizados | Ver atributos personalizados | Ver atributos personalizados e informe de uso |
| Atributos personalizados | Exportar atributos personalizados | Descargar atributos personalizados desde el dashboard |
| Atributos personalizados | Eliminar atributos personalizados | Eliminar permanentemente atributos personalizados |
| Atributos personalizados | Bloquear atributos personalizados | Añadir atributos personalizados a una lista de bloqueo que restringe su uso en el dashboard |
| Atributos personalizados | Editar atributos personalizados | Crear y actualizar atributos personalizados |
| Segmentación de propiedades de eventos personalizados | Editar segmentación de propiedades de eventos personalizados | Habilitar y deshabilitar la segmentación para propiedades de eventos personalizados |
| Eventos personalizados | Ver eventos personalizados | Ver eventos personalizados e informe de uso, y añadir eventos personalizados al correo electrónico del informe de análisis diario |
| Eventos personalizados | Exportar eventos personalizados | Descargar eventos personalizados desde el dashboard |
| PII | Ver PII | Ver PII |
| Eventos personalizados | Eliminar eventos personalizados | Eliminar permanentemente eventos personalizados |
| Eventos personalizados | Bloquear eventos personalizados | Añadir eventos personalizados a una lista de bloqueo que restringe su uso en el dashboard |
| Eventos personalizados | Editar eventos personalizados | Crear y actualizar eventos personalizados |
| Productos | Ver productos | Ver productos |
| Productos | Bloquear productos | Añadir productos a una lista de bloqueo que restringe su uso en el dashboard |
| Productos | Editar productos | Crear y actualizar productos |
| Segmentación de propiedades de compra | Editar segmentación de propiedades de compra | Habilitar y deshabilitar la segmentación para propiedades de eventos de compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Configuración {#settings}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Identificadores de API | Ver identificadores de API | Ver identificadores de API y otros identificadores |
| Claves de API | Ver claves de API | Ver claves de API |
| Claves de API | Editar claves de API | Crear y actualizar claves de API |
| Límites de API | Ver límites de API | Ver límites de velocidad de API |
| Alertas de uso de API | Ver alertas de uso de API | Ver alertas de uso de API |
| Alertas de uso de API | Editar alertas de uso de API | Crear y actualizar alertas de uso de API |
| Datos de uso de API | Ver panel de uso de API | Ver el panel de uso de API |
| Configuración de la aplicación | Editar configuración de la aplicación | Crear, editar y actualizar aplicaciones dentro de la configuración de la aplicación |
| Configuración de la aplicación | Ver configuración de la aplicación | Ver la página de configuración de la aplicación |
| Configuración de Audience Sync | Ver configuración de Audience Sync | Ver toda la configuración de los socios de Audience Sync conectados |
| Usuarios del dashboard | Editar usuarios del dashboard | Ver, crear y editar usuarios de la empresa |
| Configuración del correo electrónico | Ver configuración del correo electrónico | Ver preferencias de correo electrónico |
| Configuración del correo electrónico | Editar configuración del correo electrónico | Habilitar y actualizar preferencias de correo electrónico |
| Registro de eventos de usuario | Ver registro de eventos de usuario | Ver registros de eventos de usuario |
| Grupos internos | Ver grupos internos | Ver grupos internos |
| Grupos internos | Eliminar grupos internos | Eliminar grupos internos |
| Grupos internos | Editar grupos internos | Crear y actualizar grupos internos |
| Registro de actividad de mensajes | Ver registro de actividad de mensajes | Ver registros de actividad de mensajes |
| Configuración de idiomas múltiples | Ver configuración de localización | Ver la página de configuración de idiomas múltiples |
| Configuración de idiomas múltiples | Eliminar configuración de localización | Eliminar configuraciones regionales de idiomas múltiples |
| Configuración de idiomas múltiples | Editar configuración de localización | Crear configuraciones regionales de idiomas múltiples |
| Centros de preferencias | Ver centros de preferencias | Ver centros de preferencias |
| Centros de preferencias | Editar centros de preferencias | Crear y actualizar centros de preferencias |
| Centros de preferencias | Lanzar centros de preferencias | Activar un borrador de centro de preferencias o actualizar uno existente |
| Configuración de push | Ver configuración de push | Ver configuración de push |
| Configuración de push | Editar configuración de push | Crear y actualizar configuración de push |
| Depurador de SDK | Ver depurador de SDK | Ver el depurador de SDK o sesiones de depuración |
| Depurador de SDK | Editar depurador de SDK | Crear y descargar sesiones del depurador de SDK |
| Etiquetas | Ver etiquetas | Ver etiquetas |
| Etiquetas | Eliminar etiquetas | Eliminar etiquetas de forma permanente |
| Etiquetas | Editar etiquetas | Crear y actualizar etiquetas |
| Equipos | Ver equipos | Ver equipos |
| Equipos | Archivar equipos | Mover equipos al archivo |
| Equipos | Editar equipos | Crear y actualizar equipos |
| Configuración de WhatsApp | Ver configuración de WhatsApp | Ver toda la configuración del canal de WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Decisioning Studio {#decisioning-studio}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Agentes de Decisioning Studio | Ver agentes de Decisioning Studio | Ver la configuración de los agentes de Decisioning Studio sin realizar cambios |
| Audiencia de Decisioning Studio | Ver audiencia de Decisioning Studio | Ver los detalles de audiencia en los resúmenes de configuración de los agentes de Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Otros {#other}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Uso de la aplicación | Ver datos de uso | Ver datos de uso |
| Facturación | Ver detalles de facturación | Ver detalles de facturación |
| Agentes personalizados | Ver agentes de IA de la Consola de Agente | Permite a los usuarios ver agentes de IA personalizados |
| Agentes personalizados | Archivar agentes de IA de la Consola de Agente | Permite a los usuarios archivar agentes de IA personalizados |
| Agentes personalizados | Editar agentes de IA de la Consola de Agente | Permite a los usuarios crear y actualizar agentes de IA personalizados |
| Atributos personalizados marcados como PII | Ver atributos personalizados marcados como PII | Ver atributos personalizados marcados como PII |
| Informes del dashboard | Ver informes del dashboard | Ver informes sin realizar cambios |
| Informes del dashboard | Eliminar informes del dashboard | Eliminar informes de forma permanente |
| Informes del dashboard | Editar informes del dashboard | Crear y actualizar informes |
| Configuración de dominio | Editar configuración de dominio | Añadir dominios delegados y dominios personalizados en dominios verificados |
| Cifrado a nivel de campo | Editar cifrado a nivel de campo del identificador | Habilitar y actualizar la configuración de cifrado a nivel de campo |
| Activos de la biblioteca multimedia | Ver activos de la biblioteca multimedia | Ver activos de la biblioteca multimedia |
| Activos de la biblioteca multimedia | Eliminar activos de la biblioteca multimedia | Eliminar permanentemente activos de la biblioteca multimedia |
| Activos de la biblioteca multimedia | Editar activos de la biblioteca multimedia | Crear y actualizar activos de la biblioteca multimedia |
| Límites de velocidad de mensajería | Ver límites de velocidad de mensajería | Ver los límites de velocidad de mensajería a nivel del espacio de trabajo |
| Límites de velocidad de mensajería | Editar límites de velocidad de mensajería | Configurar y editar los límites de velocidad de mensajería a nivel del espacio de trabajo |
| Operator | Usar BrazeAI Operator<sup>TM</sup> | Acceder y usar Braze Operator para responder preguntas, navegar por la configuración, solucionar problemas y generar ideas |
| Ubicaciones de banners | Ver ubicaciones de banners | Ver ubicaciones de banners |
| Ubicaciones de banners | Archivar ubicaciones de banners | Mover ubicaciones de banners al archivo |
| Ubicaciones de banners | Editar ubicaciones de banners | Ver ubicaciones de banners sin realizar cambios |
| Códigos promocionales | Ver códigos promocionales | Ver códigos promocionales |
| Códigos promocionales | Exportar códigos promocionales | Descargar una lista de códigos promocionales desde el dashboard |
| Códigos promocionales | Editar códigos promocionales | Crear y actualizar códigos promocionales |
| Grupos de suscripción | Editar suscripciones | Crear y actualizar grupos de suscripción |
| Transformaciones | Editar transformación de datos | Crear y actualizar transformaciones de datos |
| Transformaciones | Ver transformación de datos | Ver transformaciones de datos |
| Registros de eliminación de usuarios | Ver registros de eliminación de usuarios | Ver registros de eliminación de usuarios |
| Tickets de soporte | Crear ticket de soporte | Crear y actualizar tickets de soporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }