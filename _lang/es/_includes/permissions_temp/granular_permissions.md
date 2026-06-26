{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

{% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Creación de un conjunto de permisos {#creating-a-permission-set}

Usa conjuntos de permisos para agrupar permisos relacionados con áreas temáticas o acciones específicas. Puedes aplicar conjuntos de permisos a los usuarios del dashboard que necesiten el mismo acceso en diferentes espacios de trabajo. Para crear un conjunto de permisos, ve a **Configuración** > **Configuración de permisos** y selecciona **Crear conjunto de permisos**. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example permission sets %}
| Nombre | Permisos |
|-----------|----------------|
| Desarrolladores | «Ver claves de API», «Editar claves de API», «Ver grupos internos», «Editar grupos internos», «Ver registro de actividad de mensajes», «Ver registro de eventos de usuario», «Ver identificadores de API», «Ver panel de uso de API», «Ver límites de API», «Ver alertas de uso de API», «Editar alertas de uso de API», «Ver depurador de SDK», «Editar depurador de SDK». |
| Especialistas en marketing | «Ver Campaigns», «Editar Campaigns», «Archivar Campaigns», «Ver Canvas», «Editar Canvas», «Archivar Canvas», «Ver reglas de limitación de frecuencia», «Editar reglas de limitación de frecuencia», «Ver priorización de mensajes», «Editar priorización de mensajes», «Ver Content Blocks», «Ver conmutadores de características», «Editar conmutadores de características», «Archivar conmutadores de características», «Ver Segments», «Editar Segments», «Editar grupo de control global», «Ver plantillas de IAM», «Editar plantillas de IAM», «Archivar plantillas de IAM», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Archivar plantillas de correo electrónico», «Ver plantillas de webhook», «Editar plantillas de webhook», «Archivar plantillas de webhook», «Ver plantillas de enlaces de correo electrónico», «Editar plantillas de enlaces de correo electrónico», «Ver activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias», «Editar informes del dashboard», «Ver plantillas de banners», «Ver configuración de localización», «Usar Operator», «Ver agentes de Decisioning Studio». |
| Gestión de usuarios | «Editar usuarios del dashboard», «Ver equipos», «Editar equipos», «Archivar equipos». |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Creación de un conjunto de permisos" }
{% endtab %}
{% endtabs %}

## Creación de un rol {#creating-a-role}

Los roles permiten una mayor estructura al agrupar los permisos personalizados individuales con los controles de acceso al espacio de trabajo. Esto es especialmente útil si tienes muchas marcas o espacios de trabajo regionales en un mismo dashboard. Con los roles, puedes añadir usuarios del dashboard a los espacios de trabajo adecuados y concederles directamente los permisos asociados. Para ver una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#granularpermissions_list-of-permissions).

{% tabs local %}
{% tab example roles %}
| Nombre del rol    | Espacio de trabajo | Permisos
----------- | ----------- | ---------
| Especialista en marketing - Marcas de moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | «Ver Campaigns», «Editar Campaigns», «Archivar Campaigns», «Ver Canvas», «Editar Canvas», «Archivar Canvas», «Ver Content Blocks», «Editar Content Blocks», «Archivar Content Blocks», «Lanzar Content Blocks», «Ver conmutadores de características», «Editar conmutadores de características», «Archivar conmutadores de características», «Ver Segments», «Editar Segments», «Ver plantillas de banners», «Editar plantillas de banners», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Ver activos de la biblioteca multimedia», «Editar activos de la biblioteca multimedia», «Eliminar activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias». |
| Especialista en marketing - Marcas de cuidado de la piel | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | «Ver Campaigns», «Editar Campaigns», «Archivar Campaigns», «Ver Canvas», «Editar Canvas», «Archivar Canvas», «Ver Content Blocks», «Editar Content Blocks», «Archivar Content Blocks», «Lanzar Content Blocks», «Ver conmutadores de características», «Editar conmutadores de características», «Archivar conmutadores de características», «Ver Segments», «Editar Segments», «Ver plantillas de banners», «Editar plantillas de banners», «Ver plantillas de correo electrónico», «Editar plantillas de correo electrónico», «Ver activos de la biblioteca multimedia», «Editar activos de la biblioteca multimedia», «Eliminar activos de la biblioteca multimedia», «Ver ubicaciones», «Editar ubicaciones», «Archivar ubicaciones», «Ver códigos promocionales», «Editar códigos promocionales», «Exportar códigos promocionales», «Ver centros de preferencias», «Editar centros de preferencias». |
| Gestión de usuarios - Todas las marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | «Editar usuarios del dashboard», «Ver equipos», «Editar equipos», «Archivar equipos» |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Creación de un rol" }
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
{: .reset-td-br-1 .reset-td-br-2 aria-label="Usuarios limitados" }

### Comparación de usuarios limitados {#comparing-limited-users}

| Tipo de usuario limitado | Descripción |
| --- | --- |
| Administrador del espacio de trabajo | Los administradores del espacio de trabajo tienen permisos específicos para gestionar los espacios de trabajo, pero no tienen la misma autoridad que los administradores de la empresa. Los usuarios limitados pueden heredar permisos similares a los de los administradores del espacio de trabajo si tienen marcados los permisos necesarios. |
| Administrador (administrador de la empresa) | Los administradores de la empresa tienen permisos más amplios, incluida la posibilidad de eliminar usuarios del dashboard. Sin embargo, no pueden eliminar sus propias cuentas y deben ponerse en contacto con otro administrador de la empresa para realizar esa acción. |
| Acceso de solo lectura | Para acceder a algunas partes del dashboard, como la página de Campaigns, los usuarios deben tener asignados permisos de visualización. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparación de usuarios limitados" }

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


{% alert warning %}
Si eliminas los privilegios de administrador de un usuario, este no podrá acceder a Braze hasta que le asignes al menos un [permiso a nivel de empresa o de espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Company %}

### Empresa {#company}

Para gestionar los siguientes permisos a nivel de empresa para un usuario, marca o desmarca la casilla junto a ese permiso. Cuando hayas terminado, selecciona **Actualizar usuario**.

| Nombre del permiso | Descripción |
|----------|-----------|
| Administrar configuración de empresa | Permite a los usuarios modificar la configuración de permisos y la verificación del remitente. |
| Crear y eliminar espacios de trabajo | Permite a los usuarios crear y eliminar espacios de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Empresa" }

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

No puedes exportar una matriz completa de permisos para todos los usuarios del dashboard de forma masiva desde el dashboard de Braze. Si necesitas más detalle del que proporciona **Exportar usuarios**, considera estas opciones:

- Usa el [aprovisionamiento automatizado de usuarios]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/) (SCIM) para gestionar las cuentas de los usuarios del dashboard. Por ejemplo, puedes [buscar un usuario del dashboard por correo electrónico]({{site.baseurl}}/api/endpoints/scim/get_search_existing_dashboard_user/) u obtener los detalles del usuario por ID de recurso como se describe en [Ver información de la cuenta de usuario]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information/).
- [Ponte en contacto con soporte de Braze]({{site.baseurl}}/braze_support/). En algunas situaciones, el equipo de soporte puede proporcionar una lista de cuentas, pero no una matriz completa de permisos.
- Filtra el [informe de eventos de seguridad]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings/#security-event-report) de tu empresa, que registra eventos como **Cuenta añadida** y **Permisos actualizados**, para auditar los cambios de permisos fuera del dashboard.

## Lista de permisos {#list-of-permissions}

### Mensajería {#messaging}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Campaigns | View Campaigns | Ver Campaigns |
| Campaigns | Launch Campaigns | Iniciar, detener, pausar o reanudar Campaigns existentes |
| Campaigns | Archive Campaigns | Mover Campaigns al archivo |
| Campaigns | Edit Campaigns | Crear y actualizar Campaigns |
| Campaigns | Approve and Deny Campaigns | Aprobar o rechazar Campaigns. El [flujo de trabajo de aprobación de Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas si te interesa participar en el acceso anticipado. |
| Canvas | View Canvases | Ver Canvas |
| Canvas | Archive Canvases | Mover Canvas al archivo |
| Canvas | Edit Canvases | Crear y actualizar Canvas |
| Canvas | Launch Canvases | Iniciar, detener, pausar o reanudar Canvas existentes |
| Canvas | Approve and Deny Canvases | Aprobar o rechazar Canvas. El [flujo de trabajo de aprobación de Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/) debe estar activado para que se aplique este permiso. Esta configuración está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas si te interesa participar en el acceso anticipado. |
| Feature flags | View Feature Flags | Ver conmutadores de características |
| Feature flags | Archive Feature Flags | Mover conmutadores de características al archivo |
| Feature flags | Edit Feature Flags | Crear y actualizar conmutadores de características |
| Frequency Caps | View Frequency Capping Rules | Ver reglas de limitación de frecuencia |
| Frequency Caps | Edit Frequency Capping Rules | Crear y actualizar reglas de limitación de frecuencia |
| Landing pages | View Landing Pages | Ver páginas de inicio |
| Landing pages | Publish Landing Pages | Activar un borrador de página de inicio |
| Landing pages | Edit Landing Page Drafts | Crear y guardar borradores de páginas de inicio |
| Message Archiving Settings | View Message Archiving Settings | Ver la configuración de archivado de mensajes sin realizar cambios |
| Message Archiving Settings | Edit Message Archiving Settings | Crear y actualizar la configuración de archivado de mensajes |
| Message Prioritization | View Message Prioritization | Ver la configuración de priorización de mensajes sin realizar cambios |
| Message Prioritization | Edit Message Prioritization | Crear y actualizar la configuración de priorización de mensajes |
| WhatsApp Flows | View WhatsApp Flows | Ver todos los WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensajería" }

### Audiencia {#audience}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Global Control Group | View Global Control Group | Ver la página de configuración del grupo de control global |
| Global Control Group | Edit Global Control Group | Crear y guardar cambios en el grupo de control global. Los usuarios con el permiso «Edit Global Control Group» también deben tener permisos para «Edit Campaigns» y «Edit Canvases». Los usuarios con el permiso «Edit Global Control Group» también obtienen el permiso «View Global Control Group». |
| Locations | Archive Locations | Mover ubicaciones al archivo |
| Locations | View Locations | Ver ubicaciones |
| Locations | Edit Locations | Crear y editar ubicaciones |
| Segments | View Segments | Ver Segments. Los usuarios deben tener el permiso «View Segments» para tener el permiso «Edit Segments» o «Archive Segments». |
| Segments | Archive Segments | Archivar y desarchivar Segments. Los usuarios con el permiso «Archive Segments» también deben tener el permiso «View Segments». |
| Segments | Edit Segments | Crear y actualizar Segments. Los usuarios con el permiso «Edit Segments» también deben tener el permiso «View Segments». |
| User Data | View Import Users | Ver importaciones de usuarios en CSV sin realizar cambios |
| User Data | Import Users | Cargar usuarios al dashboard |
| User Data | Edit User Data | Crear y actualizar datos de usuario |
| User Data | Export User Data | Descargar usuarios desde el dashboard |
| User Deletion Records | View User Merge Records | Ver una lista de registros de fusión de usuarios |
| Users | View User Profiles (PII Redacted) | Ver perfiles de usuario de manera compatible con PII |
| Duplicate Users | Merge Duplicate Users | Combinar usuarios duplicados en un solo usuario. Los duplicados se eliminan después de la fusión. |
| Users | Delete Users | Eliminar permanentemente usuarios del dashboard de forma individual o masiva |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Audiencia" }

### Plantilla {#template}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Banner Templates | View Banner Templates | Ver plantillas de banners |
| Banner Templates | Archive Banner Templates | Mover plantillas de banners al archivo |
| Banner Templates | Edit Banner Templates | Crear y actualizar plantillas de banners |
| Canvas Templates | View Canvas Templates | Ver plantillas de Canvas |
| Canvas Templates | Archive Canvas Templates | Mover plantillas de Canvas al archivo |
| Canvas Templates | Create and Edit Canvas Templates | Crear y actualizar plantillas de Canvas |
| Content Blocks | View Content Blocks | Ver Content Blocks |
| Content Blocks | Launch Content Blocks | Publicar borradores de Content Blocks, y editar, archivar y desarchivar Content Blocks lanzados |
| Content Blocks | Archive Content Blocks | Mover Content Blocks al archivo |
| Content Blocks | Edit Content Blocks | Crear Content Blocks y editar borradores de Content Blocks |
| Email Link Templates | View Email Link Templates | Ver plantillas de enlaces sin realizar cambios |
| Email Link Templates | Edit Email Link Templates | Crear y actualizar plantillas de enlaces |
| Email Templates | View Email Templates | Ver plantillas de correo electrónico |
| Email Templates | Archive Email Templates | Mover plantillas de correo electrónico al archivo |
| Email Templates | Edit Email Templates | Crear y actualizar plantillas de correo electrónico |
| IAM Templates | View IAM Templates | Ver plantillas de mensajes dentro de la aplicación sin realizar cambios |
| IAM Templates | Archive IAM Templates | Mover plantillas de IAM al archivo |
| IAM Templates | Edit IAM Templates | Crear y actualizar plantillas de mensajes dentro de la aplicación |
| Landing Page Templates | View Landing Page Templates | Ver plantillas de páginas de inicio |
| Landing Page Templates | Archive Landing Page Template | Mover plantillas de páginas de inicio al archivo |
| Landing Page Templates | Edit Landing Page Templates | Crear y actualizar plantillas de páginas de inicio |
| Webhook Templates | View Webhook Templates | Ver plantillas de webhook sin realizar cambios |
| Webhook Templates | Archive Webhook Templates | Mover plantillas de webhook al archivo |
| Webhook Templates | Edit Webhook Templates | Crear y actualizar plantillas de webhook |
| Whatsapp Message Templates | View WhatsApp Message Templates | Permite a los usuarios ver [plantillas de mensajes de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-2-compose-your-whatsapp-message) |
| Whatsapp Message Templates | Edit WhatsApp Message Templates | Permite a los usuarios crear plantillas de mensajes de WhatsApp en el generador de plantillas. Esta característica está actualmente en acceso anticipado. |
| WhatsApp Message Templates From Meta | View WhatsApp Message Templates From Meta | Ver todas las plantillas de WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Plantilla" }

### Integraciones de socios {#partner-integrations}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Currents Integrations | View Currents Integration | Ver integraciones de Currents |
| Currents Integrations | Edit Currents Integrations | Crear, actualizar y eliminar integraciones de Currents |
| Technology Partners | Edit Technology Partners | Crear y actualizar socios tecnológicos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Integraciones de socios" }

### Configuración de datos {#data-settings}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Catalogs | View Catalogs | Ver catálogos y selecciones |
| Catalogs | Delete Catalogs | Eliminar catálogos de forma permanente |
| Catalogs | Export Catalogs | Descargar catálogos desde el dashboard |
| Catalogs | Edit Catalogs | Crear y actualizar catálogos y selecciones |
| Cloud Data Ingestion | Edit Cloud Data Ingestion | Crear, actualizar y eliminar fuentes y sincronizaciones |
| Custom Attributes | View Custom Attributes | Ver atributos personalizados e informe de uso |
| Custom Attributes | Export Custom Attributes | Descargar atributos personalizados desde el dashboard |
| Custom Attributes | Delete Custom Attributes | Eliminar permanentemente atributos personalizados |
| Custom Attributes | Blocklist Custom Attributes | Añadir atributos personalizados a una lista de bloqueo que restringe su uso en el dashboard |
| Custom Attributes | Edit Custom Attributes | Crear y actualizar atributos personalizados |
| Custom Event Property Segmentation | Edit Custom Event Property Segmentation | Habilitar y deshabilitar la segmentación para propiedades de eventos personalizados |
| Custom Events | View Custom Events | Ver eventos personalizados e informe de uso, y añadir eventos personalizados al correo electrónico del informe de análisis diario |
| Custom Events | Export Custom Events | Descargar eventos personalizados desde el dashboard |
| PII | View PII | Ver PII |
| Custom Events | Delete Custom Events | Eliminar permanentemente eventos personalizados |
| Custom Events | Blocklist Custom Events | Añadir eventos personalizados a una lista de bloqueo que restringe su uso en el dashboard |
| Custom Events | Edit Custom Events | Crear y actualizar eventos personalizados |
| Products | View Products | Ver productos |
| Products | Blocklist Products | Añadir productos a una lista de bloqueo que restringe su uso en el dashboard |
| Products | Edit Products | Crear y actualizar productos |
| Purchase Property Segmentation | Edit Purchase Property Segmentation | Habilitar y deshabilitar la segmentación para propiedades de eventos de compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configuración de datos" }

### Configuración {#settings}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| API Identifiers | View API identifiers | Ver identificadores de API y otros identificadores |
| API Keys | View API Keys | Ver claves de API |
| API Keys | Edit API Keys | Crear y actualizar claves de API |
| API Limits | View API Limits | Ver límites de velocidad de API |
| API Usage Alerts | View API Usage Alerts | Ver alertas de uso de API |
| API Usage Alerts | Edit API Usage Alerts | Crear y actualizar alertas de uso de API |
| API Usage Data | View API Usage Dashboard | Ver el panel de uso de API |
| App Settings | Edit App Settings | Crear, editar y actualizar aplicaciones dentro de la configuración de la aplicación |
| App Settings | View App Settings | Ver la página de configuración de la aplicación |
| Audience Sync Settings | View Audience Sync Settings | Ver toda la configuración de los socios de Audience Sync conectados |
| Dashboard Users | Edit Dashboard Users | Ver, crear y editar usuarios de la empresa |
| Email Settings | View Email Settings | Ver preferencias de correo electrónico |
| Email Settings | Edit Email Settings | Habilitar y actualizar preferencias de correo electrónico |
| Event User Log | View Event User Log | Ver registros de eventos de usuario |
| Internal Groups | View Internal User Groups | Ver grupos internos |
| Internal Groups | Delete Internal User Groups | Eliminar grupos internos |
| Internal Groups | Edit Internal User Groups | Crear y actualizar grupos internos |
| Message Activity Log | View Message Activity Log | Ver registros de actividad de mensajes |
| Multi Language Settings | View Localization Settings | Ver la página de configuración de idiomas múltiples |
| Multi Language Settings | Delete Localization Settings | Eliminar configuraciones regionales de idiomas múltiples |
| Multi Language Settings | Edit Localization Settings | Crear configuraciones regionales de idiomas múltiples |
| Preference Centers | View Preference Centers | Ver centros de preferencias |
| Preference Centers | Edit Preference Centers | Crear y actualizar centros de preferencias |
| Preference Centers | Launch Preference Centers | Activar un borrador de centro de preferencias o actualizar uno existente |
| Push Settings | View Push Settings | Ver configuración de push |
| Push Settings | Edit Push Settings | Crear y actualizar configuración de push |
| SDK Debugger | View SDK Debugger | Ver el depurador de SDK o sesiones de depuración |
| SDK Debugger | Edit SDK Debugger | Crear y descargar sesiones del depurador de SDK |
| Tags | View Tags | Ver etiquetas |
| Tags | Delete Tags | Eliminar etiquetas de forma permanente |
| Tags | Edit Tags | Crear y actualizar etiquetas |
| Teams | View Teams | Ver equipos |
| Teams | Archive Teams | Mover equipos al archivo |
| Teams | Edit Teams | Crear y actualizar equipos |
| WhatsApp Settings | View WhatsApp Settings | Ver toda la configuración del canal de WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configuración" }

### Decisioning Studio

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Decisioning Studio Agents | View Decisioning Studio Agent | Ver la configuración de los agentes de Decisioning Studio sin realizar cambios |
| Decisioning Studio Audience | View Decisioning Studio Audience | Ver los detalles de audiencia en los resúmenes de configuración de los agentes de Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Decisioning Studio" }

### Otros {#other}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| App Usage | View Usage Data | Ver datos de uso |
| Billing | View Billing Details | Ver detalles de facturación |
| Custom Agents | View Agent Console AI Agents | Permite a los usuarios ver agentes de IA personalizados |
| Custom Agents | Archive Agent Console AI Agents | Permite a los usuarios archivar agentes de IA personalizados |
| Custom Agents | Edit Agent Console AI Agents | Permite a los usuarios crear y actualizar agentes de IA personalizados |
| Custom Attributes Marked As PII | View Custom Attributes Marked as PII | Ver atributos personalizados marcados como PII |
| Dashboard Reports | View Dashboard Reports | Ver informes sin realizar cambios |
| Dashboard Reports | Delete Dashboard Reports | Eliminar informes de forma permanente |
| Dashboard Reports | Edit Dashboard Reports | Crear y actualizar informes |
| Domain Settings | Edit Domain Settings | Añadir dominios delegados y dominios personalizados en dominios verificados |
| Field Level Encryption | Edit Identifier Field-Level Encryption | Habilitar y actualizar la configuración de cifrado a nivel de campo |
| Media Library Assets | View Media Library Assets | Ver activos de la biblioteca multimedia |
| Media Library Assets | Delete Media Library Assets | Eliminar permanentemente activos de la biblioteca multimedia |
| Media Library Assets | Edit Media Library Assets | Crear y actualizar activos de la biblioteca multimedia |
| Messaging Rate Limits | View Messaging Rate Limits | Ver los límites de velocidad de mensajería a nivel del espacio de trabajo |
| Messaging Rate Limits | Edit Messaging Rate Limits | Configurar y editar los límites de velocidad de mensajería a nivel del espacio de trabajo |
| Operator | Use BrazeAI Operator<sup>TM</sup> | Acceder y usar Braze Operator para responder preguntas, navegar por la configuración, solucionar problemas y generar ideas |
| Placements | View Placements | Ver ubicaciones de banners |
| Placements | Archive Placements | Mover ubicaciones de banners al archivo |
| Placements | Edit Placements | Ver ubicaciones de banners sin realizar cambios |
| Promotion Codes | View Promotion Codes | Ver códigos promocionales |
| Promotion Codes | Export Promotion Codes | Descargar una lista de códigos promocionales desde el dashboard |
| Promotion Codes | Edit Promotion Codes | Crear y actualizar códigos promocionales |
| Subscription Groups | Edit Subscriptions | Crear y actualizar grupos de suscripción |
| Transformations | Edit Data Transformation | Crear y actualizar transformaciones de datos |
| Transformations | View Data Transformation | Ver transformaciones de datos |
| User Deletion Records | View User Deletion Records | Ver registros de eliminación de usuarios |
| Support Tickets | Create Support Ticket | Crear y actualizar tickets de soporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Otros" }