---
nav_title: Permisos
article_title: Permisos de usuario de la empresa
page_order: 1
page_type: reference
alias: /braze_permissions/
description: "Este artículo de referencia explica cómo funcionan los permisos de usuario en Braze. Aquí puedes aprender a editar y configurar permisos de usuario, eligiendo quién puede acceder a tus aplicaciones en el dashboard."
tool: Dashboard

---

# Permisos de Braze {#braze-permissions}

> Aprende a crear conjuntos de permisos, crear roles, editar permisos de usuario y exportar permisos de usuario, para que puedas asegurarte de que tus usuarios solo accedan a los espacios de trabajo y las características que más necesitan.
>
> {% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Crear un conjunto de permisos {#create-a-permission-set}

Usa los conjuntos de permisos para agrupar permisos relacionados con áreas temáticas o acciones específicas. Puedes aplicar conjuntos de permisos a los usuarios del dashboard que necesiten el mismo acceso en diferentes espacios de trabajo. Para crear un conjunto de permisos, ve a **Configuración** > **Gestión de usuarios** > **Conjuntos de permisos** y selecciona **Crear conjunto de permisos**. Para una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab conjuntos de permisos de ejemplo %}
| Nombre | Permisos |
|-----------|----------------|
| Desarrolladores | "View API Keys", "Edit API Keys", "View Internal Groups", "Edit Internal Groups", "View Message Activity Log", "View Event User Log", "View API identifiers", "View API Usage Dashboard", "View API Limits", "View API Usage Alerts", "Edit API Usage Alerts", "View SDK Debugger", "Edit SDK Debugger". |
| Especialistas en marketing | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Frequency Capping Rules", "Edit Frequency Capping Rules", "View Message Prioritization", "Edit Message Prioritization", "View Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "Edit Global Control Group", "View IAM Templates", "Edit IAM Templates", "Archive IAM Templates", "View Email Templates", "Edit Email Templates", "Archive Email Templates", "View Webhook Templates", "Edit Webhook Templates", "Archive Webhook Templates", "View Email Link Templates", "Edit Email Link Templates", "View Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers", "Edit Dashboard Reports", "View Banner Templates", "View Localization Settings", "Use Operator", "View Decisioning Studio Agents". |
| Gestión de usuarios | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams". |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Conjunto de permisos de ejemplo" }
{% endtab %}
{% endtabs %}

## Crear un rol {#creating-a-role}

Los roles permiten una mayor estructura al agrupar tus permisos personalizados individuales con controles de acceso al espacio de trabajo. Esto es especialmente útil si tienes muchas marcas o espacios de trabajo regionales en un solo dashboard. Con los roles, puedes añadir usuarios del dashboard a los espacios de trabajo correctos y otorgarles directamente los permisos asociados. Para crear un rol, ve a **Configuración** > **Gestión de usuarios** > **Roles** y selecciona **Crear rol**. Para una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab roles de ejemplo %}
| Nombre del rol | Espacio de trabajo | Permisos
----------- | ----------- | ---------
| Especialista en marketing - Marcas de moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Especialista en marketing - Marcas de cuidado de la piel | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "View Campaigns", "Edit Campaigns", "Archive Campaigns", "View Canvases", "Edit Canvases", "Archive Canvases", "View Content Blocks", "Edit Content Blocks", "Archive Content Blocks", "Launch Content Blocks", "View Feature Flags", "Edit Feature Flags", "Archive Feature Flags", "View Segments", "Edit Segments", "View Banner Templates", "Edit Banner Templates", "View Email Templates", "Edit Email Templates", "View Media Library Assets", "Edit Media Library Assets", "Delete Media Library Assets", "View Locations", "Edit Locations", "Archive Locations", "View Promotion Codes", "Edit Promotion Codes", "Export Promotion Codes", "View Preference Centers", "Edit Preference Centers". |
| Gestión de usuarios - Todas las marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Edit Dashboard Users", "View Teams", "Edit Teams", "Archive Teams" |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Roles de ejemplo" }
{% endtab %}
{% endtabs %}

## ¿En qué se diferencian los conjuntos de permisos y los roles de los equipos? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions.md content="Differences" %}

### Consideraciones para añadir permisos de usuario a equipos {#considerations-for-adding-user-permissions-to-teams}

Puedes encontrar dificultades al intentar guardar permisos en el dashboard de Braze, especialmente al añadir o eliminar usuarios de un espacio de trabajo, o al añadirlos a un equipo. El botón **Guardar/Actualizar usuarios** puede aparecer atenuado si los permisos del usuario son idénticos a los que ya tiene a nivel de espacio de trabajo. Esta restricción existe porque no tiene sentido tener un equipo si todos los usuarios poseen los mismos permisos que todo el espacio de trabajo.

Para añadir correctamente un usuario a un equipo manteniendo los mismos permisos, no asignes ningún permiso a nivel de espacio de trabajo. En su lugar, asigna los permisos exclusivamente a nivel de equipo.

## Usuarios limitados {#limited-users}

Los usuarios limitados tienen permisos específicos que les permiten gestionar ciertos aspectos del dashboard de Braze, pero con restricciones en comparación con los administradores de empresa y los administradores de espacio de trabajo.

| Ámbito | Descripción |
| --- | --- |
| Permisos | Los usuarios limitados pueden editar los permisos de otros usuarios limitados si tienen el permiso "Edit Dashboard Users". También pueden crear nuevos usuarios limitados y modificar sus conjuntos de permisos. Sin embargo, no pueden crear ni gestionar cuentas de administrador de empresa. |
| Limitaciones de rol | Si un usuario limitado tiene todos los permisos excepto "Workspace Admin", seguirá teniendo acceso a todos los demás permisos que normalmente se otorgan a un administrador de espacio de trabajo. |
| Visibilidad de permisos | Si un usuario limitado tiene el permiso "Edit Dashboard Users" para un espacio de trabajo (como Dev) pero no para otro (como Prod), no verá los permisos del espacio de trabajo Prod en su página de detalles de usuarios del dashboard. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permisos para usuarios limitados" }

### Comparar usuarios limitados {#compare-limited-users}

| Tipo de usuario limitado | Descripción |
| --- | --- |
| Administrador de espacio de trabajo | Los administradores de espacio de trabajo tienen permisos específicos para gestionar espacios de trabajo, pero no tienen la misma autoridad que los administradores de empresa. Los usuarios limitados pueden heredar permisos similares a los de los administradores de espacio de trabajo si tienen los permisos necesarios marcados. |
| Administrador (administrador de empresa) | Los administradores de empresa tienen permisos más amplios, incluida la capacidad de eliminar usuarios del dashboard. Sin embargo, no pueden eliminar sus propias cuentas y deben ponerse en contacto con otro administrador de empresa para esa acción. |
| Acceso de solo lectura | Para acceder a partes del dashboard, como la página de Campaigns, los usuarios deben tener permisos de visualización asignados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparación de usuarios limitados" }

### Error de acceso limitado {#limited-access-error}

Los usuarios pueden encontrar mensajes como "Necesitas permisos de «View Landing Pages» para acceder a esta página". En esos casos, el usuario y el administrador de la cuenta deben verificar que se hayan otorgado los permisos necesarios. Si ya están otorgados, intenta resolver el problema deshabilitando y luego volviendo a habilitar los permisos del usuario.

{% alert note %}
No es posible fusionar ni importar permisos de usuario de un usuario del dashboard a otro.
{% endalert %}

## Matices de los permisos de usuario {#nuances-of-user-permissions}

Ten en cuenta los siguientes comportamientos al asignar acceso al dashboard:

- **Administrador de espacio de trabajo frente a administrador de empresa:** los administradores de espacio de trabajo gestionan permisos dentro de los espacios de trabajo asignados. Los administradores de empresa tienen autoridad a nivel de toda la empresa, incluida la eliminación de otros usuarios del dashboard.
- **Usuarios limitados:** los usuarios limitados con el permiso "Edit Dashboard Users" pueden gestionar a otros usuarios limitados, pero no pueden crear ni gestionar cuentas de administrador de empresa.
- **Alcance de gestión de usuarios del dashboard:** en la página de detalles del usuario, los permisos solo aparecen para los espacios de trabajo a los que el editor puede acceder. Un usuario limitado que puede editar usuarios en un espacio de trabajo puede no ver las casillas de permisos de otro espacio de trabajo.
- **Exportar datos de usuario:** exportar datos de usuario requiere acceso a nivel de espacio de trabajo además del permiso de exportación.
- **Permisos compuestos:** algunas áreas requieren múltiples permisos. Por ejemplo, configurar [socios tecnológicos]({{site.baseurl}}/partners) normalmente requiere tanto acceso al socio como un permiso de lectura básico para las características relacionadas del espacio de trabajo.
- **Importar y actualizar datos de usuario:** este permiso incluye la capacidad de editar perfiles de usuario de la aplicación a través de flujos de importación, no solo registros de usuarios del dashboard.

## Editar los permisos de un usuario {#edit-a-users-permissions}

Para editar los permisos actuales de administrador, empresa o espacio de trabajo de un usuario, ve a **Configuración** > **Gestión de usuarios** > **Usuarios de la empresa** y selecciona su nombre.

![La página "Usuarios de la empresa" en Braze mostrando una tabla de usuarios del dashboard.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Administrador %}

### Administrador {#admin}

Los administradores tienen acceso a todas las características y la capacidad de modificar cualquier configuración de la empresa. Pueden:

- Cambiar la [configuración de aprobación]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow)
- Añadir, editar, eliminar, suspender o reactivar otros [usuarios de Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users)
- Exportar usuarios de Braze como CSV

Para otorgar o eliminar privilegios de administrador, selecciona **Este usuario es administrador** y luego selecciona **Actualizar usuario**.

{% alert warning %}
Si eliminas los privilegios de administrador de un usuario, no podrá acceder a Braze hasta que le asignes al menos un [permiso a nivel de empresa o de espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?tab=company&sdktab=granular%20permissions#granularpermissions_editing-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Empresa %}

### Empresa {#company}

Para gestionar los siguientes permisos a nivel de empresa para un usuario, marca o desmarca la casilla junto a ese permiso. Cuando hayas terminado, selecciona **Actualizar usuario**.

| Nombre del permiso | Descripción |
|----------|-----------|
| Gestionar configuración de empresa | Permite a los usuarios modificar la configuración de permisos y la verificación del remitente. |
| Crear y eliminar espacios de trabajo | Permite a los usuarios crear y eliminar espacios de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permisos a nivel de empresa" }

{% endtab %}
{% tab Espacio de trabajo %}

### Espacio de trabajo {#workspace}

Puedes otorgar a un usuario diferentes permisos para cada espacio de trabajo al que pertenezca en Braze. Para gestionar sus permisos a nivel de espacio de trabajo, selecciona **Seleccionar espacios de trabajo y permisos** y luego elige sus permisos manualmente o asigna un [conjunto de permisos o rol]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_creating-a-permission-set) que hayas creado previamente. Si necesitas otorgar a un usuario diferentes permisos para diferentes espacios de trabajo, repite este proceso tantas veces como sea necesario. Para una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/?sdktab=granular%20permissions#granularpermissions_list-of-permissions).

{% subtabs %}
{% subtab Seleccionar manualmente %}

En **Espacios de trabajo**, elige uno o más espacios de trabajo del menú desplegable. Luego, en **Permisos**, selecciona uno o más permisos. Se les asignarán estos permisos solo para los espacios de trabajo que hayas seleccionado. Opcionalmente, puedes seleccionar **Asignar acceso de administrador de espacio de trabajo** si deseas otorgarles permisos completos para ese espacio de trabajo.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel de espacio de trabajo seleccionados manualmente en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Asignar conjunto de permisos %}

En **Espacios de trabajo**, elige uno o más espacios de trabajo del menú desplegable. Luego, en **Conjuntos de permisos**, elige un conjunto de permisos. Se les asignarán estos permisos solo para los espacios de trabajo que hayas seleccionado.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel de espacio de trabajo asignados mediante un conjunto de permisos en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Asignar rol %}

En **Espacios de trabajo**, elige uno o más espacios de trabajo del menú desplegable. Luego, en **Rol**, elige un rol. Se les asignarán estos permisos solo para los espacios de trabajo que hayas seleccionado.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel de espacio de trabajo asignados mediante un rol en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportar permisos de usuario {#exporting-user-permissions}

Para descargar una lista de tus usuarios y sus permisos, ve a **Configuración** > **Gestión de usuarios** > **Usuarios de la empresa** y selecciona **Exportar usuarios**. En breve se enviará un archivo CSV a tu dirección de correo electrónico.

## Lista de permisos {#list-of-permissions}

### Mensajería {#messaging}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Campaigns | View Campaigns | Ver Campaigns |
| Campaigns | Launch Campaigns | Iniciar, detener, pausar o reanudar Campaigns existentes |
| Campaigns | Archive Campaigns | Mover Campaigns al archivo |
| Campaigns | Edit Campaigns | Crear y actualizar Campaigns |
| Campaigns | Approve and Deny Campaigns | Aprobar o rechazar Campaigns. El [flujo de trabajo de aprobación para Campaigns]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals) debe estar activado para que este permiso se aplique. Esta configuración se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas si te interesa participar en el acceso anticipado. |
| Canvas | View Canvases | Ver Canvas |
| Canvas | Archive Canvases | Mover Canvas al archivo |
| Canvas | Edit Canvases | Crear y actualizar Canvas |
| Canvas | Launch Canvases | Iniciar, detener, pausar o reanudar Canvas existentes |
| Canvas | Approve and Deny Canvases | Aprobar o rechazar Canvas. El [flujo de trabajo de aprobación para Canvas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals) debe estar activado para que este permiso se aplique. Esta configuración se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas si te interesa participar en el acceso anticipado. |
| Conmutadores de características | View Feature Flags | Ver conmutadores de características |
| Conmutadores de características | Archive Feature Flags | Mover conmutadores de características al archivo |
| Conmutadores de características | Edit Feature Flags | Crear y actualizar conmutadores de características |
| Limitación de frecuencia | View Frequency Capping Rules | Ver reglas de limitación de frecuencia |
| Limitación de frecuencia | Edit Frequency Capping Rules | Crear y actualizar reglas de limitación de frecuencia |
| Páginas de inicio | View Landing Pages | Ver páginas de inicio |
| Páginas de inicio | Publish Landing Pages | Activar un borrador de página de inicio |
| Páginas de inicio | Edit Landing Page Drafts | Crear y guardar borradores de páginas de inicio |
| Configuración de archivado de mensajes | View Message Archiving Settings | Ver la configuración de archivado de mensajes sin realizar cambios |
| Configuración de archivado de mensajes | Edit Message Archiving Settings | Crear y actualizar la configuración de archivado de mensajes |
| Priorización de mensajes | View Message Prioritization | Ver la configuración de priorización de mensajes sin realizar cambios |
| Priorización de mensajes | Edit Message Prioritization | Crear y actualizar la configuración de priorización de mensajes |
| WhatsApp Flows | View WhatsApp Flows | Ver todos los WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de mensajería" }

### Audiencia {#audience}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Grupo de control global | View Global Control Group | Ver la página de configuración del Grupo de control global |
| Grupo de control global | Edit Global Control Group | Crear y guardar cambios en el Grupo de control global. Los usuarios con el permiso "Edit Global Control Group" también deben tener los permisos "Edit Campaigns" y "Edit Canvases". Los usuarios con el permiso "Edit Global Control Group" también obtienen el permiso "View Global Control Group". |
| Ubicaciones | Archive Locations | Mover ubicaciones al archivo |
| Ubicaciones | View Locations | Ver ubicaciones |
| Ubicaciones | Edit Locations | Crear y editar ubicaciones |
| Segments | View Segments | Ver Segments. Los usuarios deben tener el permiso "View Segments" para tener el permiso "Edit Segments" o "Archive Segments" |
| Segments | Archive Segments | Archivar y desarchivar Segments. Los usuarios con el permiso "Archive Segments" también deben tener el permiso "View Segments" |
| Segments | Edit Segments | Crear y actualizar Segments. Los usuarios con el permiso "Edit Segments" también deben tener el permiso "View Segments" |
| Datos de usuario | View Import Users | Ver importaciones de usuarios en CSV sin realizar cambios |
| Datos de usuario | Import Users | Cargar usuarios al dashboard |
| Datos de usuario | Edit User Data | Crear y actualizar datos de usuario |
| Datos de usuario | Export User Data | Descargar usuarios del dashboard |
| Usuarios duplicados | View User Merge Records | Ver una lista de registros de fusión de usuarios |
| Usuarios | View User Profiles (PII Redacted) | Ver perfiles de usuario de manera compatible con PII |
| Usuarios duplicados | Merge Duplicate Users | Combinar usuarios duplicados en uno solo. Los duplicados se eliminan después de la fusión |
| Eliminar usuarios | View User Deletion Records | Ver una lista de registros de eliminación de usuarios |
| Eliminar usuarios | Delete Users | Eliminar permanentemente usuarios del dashboard de forma individual o masiva |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de audiencia" }

### Plantilla {#template}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Plantillas de banner | View Banner Templates | Ver plantillas de banner |
| Plantillas de banner | Archive Banner Templates | Mover plantillas de banner al archivo |
| Plantillas de banner | Edit Banner Templates | Crear y actualizar plantillas de banner |
| Plantillas de Canvas | View Canvas Templates | Ver plantillas de Canvas |
| Plantillas de Canvas | Archive Canvas Templates | Mover plantillas de Canvas al archivo |
| Plantillas de Canvas | Create and Edit Canvas Templates | Crear y actualizar plantillas de Canvas |
| Content Blocks | View Content Blocks | Ver Content Blocks |
| Content Blocks | Launch Content Blocks | Publicar borradores de Content Blocks, y editar, archivar y desarchivar Content Blocks publicados |
| Content Blocks | Archive Content Blocks | Mover Content Blocks al archivo |
| Content Blocks | Edit Content Blocks | Crear Content Blocks y editar borradores de Content Blocks |
| Plantillas de enlaces de correo electrónico | View Email Link Templates | Ver plantillas de enlaces sin realizar cambios |
| Plantillas de enlaces de correo electrónico | Edit Email Link Templates | Crear y actualizar plantillas de enlaces |
| Plantillas de correo electrónico | View Email Templates | Ver plantillas de correo electrónico |
| Plantillas de correo electrónico | Archive Email Templates | Mover plantillas de correo electrónico al archivo |
| Plantillas de correo electrónico | Edit Email Templates | Crear y actualizar plantillas de correo electrónico |
| Plantillas de mensajes dentro de la aplicación | View IAM Templates | Ver plantillas de mensajes dentro de la aplicación sin realizar cambios |
| Plantillas de mensajes dentro de la aplicación | Archive IAM Templates | Mover plantillas de mensajes dentro de la aplicación al archivo |
| Plantillas de mensajes dentro de la aplicación | Edit IAM Templates | Crear y actualizar plantillas de mensajes dentro de la aplicación |
| Plantillas de páginas de inicio | View Landing Page Templates | Ver plantillas de páginas de inicio |
| Plantillas de páginas de inicio | Archive Landing Page Template | Mover plantillas de páginas de inicio al archivo |
| Plantillas de páginas de inicio | Edit Landing Page Templates | Crear y actualizar plantillas de páginas de inicio |
| Plantillas de webhook | View Webhook Templates | Ver plantillas de webhook sin realizar cambios |
| Plantillas de webhook | Archive Webhook Templates | Mover plantillas de webhook al archivo |
| Plantillas de webhook | Edit Webhook Templates | Crear y actualizar plantillas de webhook |
| Plantillas de mensajes de WhatsApp | View WhatsApp Message Templates | Permite a los usuarios ver [plantillas de mensajes de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) |
| Plantillas de mensajes de WhatsApp | Edit WhatsApp Message Templates | Permite a los usuarios crear plantillas de mensajes de WhatsApp en el constructor de plantillas. Esta característica se encuentra actualmente en acceso anticipado. |
| Plantillas de mensajes de WhatsApp de Meta | View WhatsApp Message Templates From Meta | Ver todas las plantillas de WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de plantillas" }

### Integraciones de socios {#partner-integrations}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Integraciones de Currents | View Currents Integration | Ver integraciones de Currents |
| Integraciones de Currents | Edit Currents Integrations | Crear, actualizar y eliminar integraciones de Currents |
| Socios tecnológicos | Edit Technology Partners | Crear y actualizar socios tecnológicos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de integraciones de socios" }

### Configuración de datos {#data-settings}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Catálogos | View Catalogs | Ver catálogos y selecciones |
| Catálogos | Delete Catalogs | Eliminar permanentemente catálogos |
| Catálogos | Export Catalogs | Descargar catálogos del dashboard |
| Catálogos | Edit Catalogs | Crear y actualizar catálogos y selecciones |
| Ingesta de datos de Cloud | Edit Cloud Data Ingestion | Crear, actualizar y eliminar fuentes y sincronizaciones |
| Atributos personalizados | View Custom Attributes | Ver atributos personalizados e informe de uso |
| Atributos personalizados | Export Custom Attributes | Descargar atributos personalizados del dashboard |
| Atributos personalizados | Delete Custom Attributes | Eliminar permanentemente atributos personalizados |
| Atributos personalizados | Blocklist Custom Attributes | Añadir atributos personalizados a una lista de bloqueo que restringe su uso en el dashboard |
| Atributos personalizados | Edit Custom Attributes | Crear y actualizar atributos personalizados |
| Segmentación por propiedades de eventos personalizados | Edit Custom Event Property Segmentation | Habilitar y deshabilitar la segmentación por propiedades de eventos personalizados |
| Eventos personalizados | View Custom Events | Ver eventos personalizados e informe de uso, y añadir eventos personalizados al correo electrónico del informe de análisis diario |
| Eventos personalizados | Export Custom Events | Descargar eventos personalizados del dashboard |
| PII | View PII | Ver PII |
| Eventos personalizados | Delete Custom Events | Eliminar permanentemente eventos personalizados |
| Eventos personalizados | Blocklist Custom Events | Añadir eventos personalizados a una lista de bloqueo que restringe su uso en el dashboard |
| Eventos personalizados | Edit Custom Events | Crear y actualizar eventos personalizados |
| Productos | View Products | Ver productos |
| Productos | Blocklist Products | Añadir productos a una lista de bloqueo que restringe su uso en el dashboard |
| Productos | Edit Products | Crear y actualizar productos |
| Segmentación por propiedades de compra | Edit Purchase Property Segmentation | Habilitar y deshabilitar la segmentación por propiedades de eventos de compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de configuración de datos" }

### Configuración {#settings}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Identificadores de API | View API identifiers | Ver identificadores de API y otros identificadores |
| Claves de API | View API Keys | Ver claves de API |
| Claves de API | Edit API Keys | Crear y actualizar claves de API |
| Límites de API | View API Limits | Ver límites de velocidad de API |
| Alertas de uso de API | View API Usage Alerts | Ver alertas de uso de API |
| Alertas de uso de API | Edit API Usage Alerts | Crear y actualizar alertas de uso de API |
| Datos de uso de API | View API Usage Dashboard | Ver el dashboard de uso de API |
| Configuración de la aplicación | Edit App Settings | Crear, editar y actualizar aplicaciones dentro de la configuración de la aplicación |
| Configuración de la aplicación | View App Settings | Ver la página de configuración de la aplicación |
| Configuración de Audience Sync | View Audience Sync Settings | Ver toda la configuración de los socios de Audience Sync conectados |
| Usuarios del dashboard | Edit Dashboard Users | Ver, crear y editar usuarios de la empresa |
| Configuración del correo electrónico | View Email Settings | Ver preferencias de correo electrónico |
| Configuración del correo electrónico | Edit Email Settings | Habilitar y actualizar preferencias de correo electrónico |
| Registro de eventos de usuario | View Event User Log | Ver registros de eventos de usuario |
| Grupos internos | View Internal User Groups | Ver grupos internos |
| Grupos internos | Delete Internal User Groups | Eliminar grupos internos |
| Grupos internos | Edit Internal User Groups | Crear y actualizar grupos internos |
| Registro de actividad de mensajes | View Message Activity Log | Ver registros de actividad de mensajes |
| Configuración multilingüe | View Localization Settings | Ver la página de configuración de localización multilingüe |
| Configuración multilingüe | Delete Localization Settings | Eliminar localización multilingüe |
| Configuración multilingüe | Edit Localization Settings | Crear localizaciones multilingües |
| Centros de preferencias | View Preference Centers | Ver centros de preferencias |
| Centros de preferencias | Edit Preference Centers | Crear y actualizar centros de preferencias |
| Centros de preferencias | Launch Preference Centers | Activar un borrador de centro de preferencias o actualizar uno existente |
| Configuración de push | View Push Settings | Ver la configuración de push |
| Configuración de push | Edit Push Settings | Crear y actualizar la configuración de push |
| Depurador de SDK | View SDK Debugger | Ver el depurador de SDK o sesiones de depuración |
| Depurador de SDK | Edit SDK Debugger | Crear y descargar sesiones del depurador de SDK |
| Etiquetas | View Tags | Ver etiquetas |
| Etiquetas | Delete Tags | Eliminar permanentemente etiquetas |
| Etiquetas | Edit Tags | Crear y actualizar etiquetas |
| Equipos | View Teams | Ver equipos |
| Equipos | Archive Teams | Mover equipos al archivo |
| Equipos | Edit Teams | Crear y actualizar equipos |
| Configuración de WhatsApp | View WhatsApp Settings | Ver toda la configuración del canal de WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de configuración" }

### Decisioning Studio

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Agentes de Decisioning Studio | View Decisioning Studio Agent | Ver la configuración de agentes de Decisioning Studio sin realizar cambios |
| Audiencia de Decisioning Studio | View Decisioning Studio Audience | Ver detalles de audiencia en los resúmenes de configuración de agentes de Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de Decisioning Studio" }

### Otros {#other}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Uso de la aplicación | View Usage Data | Ver datos de uso |
| Facturación | View Billing Details | Ver detalles de facturación |
| Agentes personalizados | View Agent Console AI Agents | Permite a los usuarios ver agentes de IA personalizados |
| Agentes personalizados | Archive Agent Console AI Agents | Permite a los usuarios archivar agentes de IA personalizados |
| Agentes personalizados | Edit Agent Console AI Agents | Permite a los usuarios crear y actualizar agentes de IA personalizados |
| Atributos personalizados marcados como PII | View Custom Attributes Marked as PII | Ver atributos personalizados marcados como PII |
| Informes del dashboard | View Dashboard Reports | Ver informes sin realizar cambios |
| Informes del dashboard | Delete Dashboard Reports | Eliminar permanentemente informes |
| Informes del dashboard | Edit Dashboard Reports | Crear y actualizar informes |
| Configuración de dominio | Edit Domain Settings | Añadir dominios delegados y dominios personalizados en Dominios verificados |
| Cifrado a nivel de campo | Edit Identifier Field-Level Encryption | Habilitar y actualizar la configuración de cifrado a nivel de campo |
| Activos de la biblioteca de medios | View Media Library Assets | Ver activos de la biblioteca de medios |
| Activos de la biblioteca de medios | Delete Media Library Assets | Eliminar permanentemente activos de la biblioteca de medios |
| Activos de la biblioteca de medios | Edit Media Library Assets | Crear y actualizar activos de la biblioteca de medios |
| Activos de la biblioteca de medios | Replace Media Library Assets | Reemplazar el archivo de un activo existente de la biblioteca de medios manteniendo estables su URL e ID de activo |
| Límites de velocidad de mensajería | View Messaging Rate Limits | Ver límites de velocidad de mensajería a nivel de espacio de trabajo |
| Límites de velocidad de mensajería | Edit Messaging Rate Limits | Configurar y editar límites de velocidad de mensajería a nivel de espacio de trabajo |
| Operator | Use BrazeAI Operator<sup>TM</sup> | Acceder y usar BrazeAI Operator para responder preguntas, navegar por la configuración, solucionar problemas y generar ideas |
| Ubicaciones de banner | View Placements | Ver ubicaciones de banner |
| Ubicaciones de banner | Archive Placements | Mover ubicaciones de banner al archivo |
| Ubicaciones de banner | Edit Placements | Ver ubicaciones de banner sin realizar cambios |
| Códigos promocionales | View Promotion Codes | Ver códigos promocionales |
| Códigos promocionales | Export Promotion Codes | Descargar una lista de códigos promocionales del dashboard |
| Códigos promocionales | Edit Promotion Codes | Crear y actualizar códigos promocionales |
| Grupos de suscripción | Edit Subscriptions | Crear y actualizar grupos de suscripción |
| Transformaciones | Edit Data Transformation | Crear y actualizar transformaciones de datos |
| Transformaciones | View Data Transformation | Ver transformaciones de datos |
| Tickets de soporte | Create Support Ticket | Crear y actualizar tickets de soporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Otros permisos" }