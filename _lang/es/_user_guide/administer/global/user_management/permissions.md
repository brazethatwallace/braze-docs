---
nav_title: Permisos
article_title: "Permisos de Braze"
page_order: 1
page_type: reference
alias: /braze_permissions/
description: "Este artículo de referencia explica cómo funcionan los permisos de usuario en Braze. Aquí puedes aprender a editar y configurar permisos de usuario, eligiendo quién puede acceder."
tool: Dashboard
---

# Permisos de Braze {#braze-permissions}

> Aprende a crear conjuntos de permisos, crear roles, editar permisos de usuario y exportar permisos de usuario, para que puedas asegurarte de que tus usuarios solo accedan a los espacios de trabajo y las características que más necesitan.
>
> {% multi_lang_include video.html id="nv699nw706" source="wistia" %}

## Crear un conjunto de permisos {#create-a-permission-set}

Utiliza los conjuntos de permisos para agrupar permisos relacionados con áreas temáticas o acciones específicas. Puedes aplicar conjuntos de permisos a los usuarios del panel que necesiten el mismo acceso en distintos espacios de trabajo. Para crear un conjunto de permisos, ve a **Configuración** > **Gestión de usuarios** > **Conjuntos de permisos** y selecciona **Crear conjunto de permisos**. Para obtener una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

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

## Creación de un rol {#creating-a-role}

Los roles permiten más estructura al agrupar tus permisos personalizados individuales con controles de acceso al espacio de trabajo. Esto es especialmente útil si tienes muchas marcas o espacios de trabajo regionales en un solo panel. Con los roles, puedes añadir usuarios del panel a los espacios de trabajo apropiados y concederles directamente los permisos asociados. Para crear un rol, ve a **Configuración** > **Gestión de usuarios** > **Roles** y selecciona **Crear rol**. Para una descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% tabs local %}
{% tab roles de ejemplo %}
| Nombre del rol    | Espacio de trabajo | Permisos
----------- | ----------- | ---------
| Especialista en marketing - Marcas de moda | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand {:/} | "Ver Campaigns", "Editar Campaigns", "Archivar Campaigns", "Ver Canvas", "Editar Canvas", "Archivar Canvas", "Ver Content Blocks", "Editar Content Blocks", "Archivar Content Blocks", "Lanzar Content Blocks", "Ver conmutadores de características", "Editar conmutadores de características", "Archivar conmutadores de características", "Ver Segments", "Editar Segments", "Ver plantillas de banner", "Editar plantillas de banner", "Ver plantillas de correo electrónico", "Editar plantillas de correo electrónico", "Ver activos de la biblioteca multimedia", "Editar activos de la biblioteca multimedia", "Eliminar activos de la biblioteca multimedia", "Ver ubicaciones", "Editar ubicaciones", "Archivar ubicaciones", "Ver códigos promocionales", "Editar códigos promocionales", "Exportar códigos promocionales", "Ver centros de preferencias", "Editar centros de preferencias". |
| Especialista en marketing - Marcas de cuidado de la piel | {::nomarkdown}[DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Ver Campaigns", "Editar Campaigns", "Archivar Campaigns", "Ver Canvas", "Editar Canvas", "Archivar Canvas", "Ver Content Blocks", "Editar Content Blocks", "Archivar Content Blocks", "Lanzar Content Blocks", "Ver conmutadores de características", "Editar conmutadores de características", "Archivar conmutadores de características", "Ver Segments", "Editar Segments", "Ver plantillas de banner", "Editar plantillas de banner", "Ver plantillas de correo electrónico", "Editar plantillas de correo electrónico", "Ver activos de la biblioteca multimedia", "Editar activos de la biblioteca multimedia", "Eliminar activos de la biblioteca multimedia", "Ver ubicaciones", "Editar ubicaciones", "Archivar ubicaciones", "Ver códigos promocionales", "Editar códigos promocionales", "Exportar códigos promocionales", "Ver centros de preferencias", "Editar centros de preferencias".|
| Gestión de usuarios - Todas las marcas | {::nomarkdown}[DEV] Fashion Brand, [QA] Fashion Brand, [PROD] Fashion Brand, [DEV] Skincare Brand, [QA] Skincare Brand, [PROD] Skincare Brand {:/} | "Editar usuarios del panel", "Ver equipos", "Editar equipos", "Archivar equipos"|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Roles de ejemplo" }
{% endtab %}
{% endtabs %}

## ¿En qué se diferencian los conjuntos de permisos y los roles de los equipos? {#how-do-permission-sets-and-roles-differ-from-teams}

{% multi_lang_include permissions/differences.md content="Differences" %}

### Consideraciones para añadir permisos de usuario a los equipos {#considerations-for-adding-user-permissions-to-teams}

Es posible que encuentres dificultades al intentar guardar permisos en el panel de Braze, en particular al añadir o eliminar usuarios de un espacio de trabajo, o al añadirlos a un equipo. El botón **Guardar/Actualizar usuarios** puede aparecer en gris si los permisos del usuario son idénticos a los que ya tiene a nivel de espacio de trabajo. Esta restricción existe porque no tiene sentido tener un equipo si todos los usuarios poseen los mismos permisos que todo el espacio de trabajo.

Para añadir correctamente un usuario a un equipo manteniendo los mismos permisos, no asignes ningún permiso a nivel de espacio de trabajo. En su lugar, asigna los permisos exclusivamente a nivel de equipo.

## Usuarios con acceso limitado {#limited-users}

Los usuarios con acceso limitado tienen permisos específicos que les permiten administrar ciertos aspectos del panel de Braze, al tiempo que tienen restricciones en comparación con los administradores de empresa y los administradores de espacio de trabajo.

| Alcance | Descripción |
| --- | --- |
| Permisos | Los usuarios con acceso limitado pueden editar los permisos de otros usuarios con acceso limitado si tienen el permiso "Editar usuarios del panel". También pueden crear nuevos usuarios con acceso limitado y modificar sus conjuntos de permisos. Sin embargo, no pueden crear ni administrar cuentas de administrador de empresa. |
| Limitaciones de rol | Si un usuario con acceso limitado tiene todos los permisos excepto "Administrador de espacio de trabajo", aún tendrá acceso a todos los demás permisos que normalmente se conceden a un administrador de espacio de trabajo. |
| Visibilidad de permisos | Si un usuario con acceso limitado tiene el permiso "Editar usuarios del panel" para un espacio de trabajo (como Dev) pero no para otro (como Prod), no verá los permisos del espacio de trabajo Prod en la página de detalles de usuarios del panel. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permisos para usuarios con acceso limitado" }

### Comparar usuarios con acceso limitado {#compare-limited-users}

| Tipo de usuario con acceso limitado | Descripción |
| --- | --- |
| Administrador de espacio de trabajo | Los administradores de espacio de trabajo tienen permisos específicos para administrar espacios de trabajo, pero no tienen la misma autoridad que los administradores de empresa. Los usuarios con acceso limitado pueden heredar permisos similares a los de los administradores de espacio de trabajo si tienen los permisos necesarios marcados. |
| Administrador (administrador de empresa) | Los administradores de empresa tienen permisos más amplios, incluida la capacidad de eliminar usuarios del panel. Sin embargo, no pueden eliminar sus propias cuentas y deben ponerse en contacto con otro administrador de empresa para esa acción. |
| Acceso de solo lectura | Para acceder a partes del panel, como la página de Campaigns, los usuarios deben tener permisos de visualización asignados. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comparación de usuarios con acceso limitado" }

### Error de acceso limitado {#limited-access-error}

Los usuarios pueden encontrarse con mensajes como "Necesitas permisos de 'Ver páginas de destino' para acceder a esta página". En esos casos, el usuario y el administrador de la cuenta deben verificar que se han concedido los permisos necesarios. Si es así, intenta resolver el problema deshabilitando y luego volviendo a habilitar los permisos del usuario.

{% alert note %}
No es posible fusionar ni importar permisos de usuario de un usuario del panel a otro.
{% endalert %}

## Matices de los permisos de usuario {#nuances-of-user-permissions}

Ten en cuenta los siguientes comportamientos cuando asignes acceso al panel:

- **Administrador del espacio de trabajo versus administrador de la empresa:** Los administradores del espacio de trabajo gestionan los permisos dentro de los espacios de trabajo asignados. Los administradores de la empresa tienen autoridad a nivel de toda la empresa, incluida la eliminación de otros usuarios del panel.
- **Usuarios limitados:** Los usuarios limitados con el permiso "Editar usuarios del panel" pueden gestionar a otros usuarios limitados, pero no pueden crear ni gestionar cuentas de administrador de la empresa.
- **Alcance de Gestionar usuarios del panel:** En la página de detalle del usuario, los permisos solo aparecen para los espacios de trabajo a los que el editor puede acceder. Un usuario limitado que puede editar usuarios en un espacio de trabajo puede no ver las casillas de verificación de permisos de otro espacio de trabajo.
- **Botón Asignar permisos:** Cuando editas un usuario y este ya tiene permisos a nivel de espacio de trabajo o conjuntos de permisos para todos los espacios de trabajo que puedes gestionar, el botón **Asignar permisos** desaparece. Esto ocurre porque no quedan espacios de trabajo adicionales para asignar a nivel de espacio de trabajo.
- **Exportar datos de usuario:** Exportar datos de usuario requiere acceso a nivel de espacio de trabajo además del permiso de exportación.
- **Permisos compuestos:** Algunas áreas requieren varios permisos. Por ejemplo, configurar [Partners tecnológicos]({{site.baseurl}}/partners) normalmente requiere tanto acceso al partner como un permiso de lectura básico para las características relacionadas del espacio de trabajo.
- **Importar y actualizar datos de usuario:** Este permiso incluye la capacidad de editar perfiles de usuario de la aplicación a través de flujos de importación, no solo registros de usuarios del panel.

## Editar los permisos de un usuario {#edit-a-users-permissions}

Para editar los permisos actuales de administrador, empresa o espacio de trabajo de un usuario, ve a **Configuración** > **Gestión de usuarios** > **Usuarios de la empresa** y, a continuación, selecciona su nombre.

![La página "Usuarios de la empresa" en Braze mostrando una tabla de usuarios del panel.]({% image_buster /assets/img/braze_permissions/selecting_a_user.png %})

{% tabs local %}
{% tab Administrador %}

### Administrador {#admin}

Los administradores tienen acceso a todas las características y la capacidad de modificar cualquier configuración de la empresa. Pueden:

- Cambiar la [configuración de aprobaciones]({{site.baseurl}}/user_guide/messaging/governance/approvals#turning-on-the-approval-workflow)
- Añadir, editar, eliminar, suspender o reactivar a otros [usuarios de Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users#adding-company-users)
- Exportar los usuarios de Braze como un archivo CSV

Para conceder o revocar privilegios de administrador, selecciona **Este usuario es un administrador** y luego selecciona **Actualizar usuario**.

{% alert warning %}
Si eliminas los privilegios de administrador de un usuario, este no podrá acceder a Braze hasta que le asignes al menos un [permiso a nivel de empresa o a nivel de espacio de trabajo]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions).
{% endalert %}

{% endtab %}
{% tab Empresa %}

### Empresa {#company}

Para gestionar los siguientes permisos a nivel de empresa de un usuario, marca o desmarca la casilla junto a ese permiso. Cuando hayas terminado, selecciona **Actualizar usuario**.

| Nombre del permiso | Descripción |
|----------|-----------|
| Gestionar configuración de la empresa | Permite a los usuarios modificar la configuración de permisos y la verificación de remitente. |
| Crear y eliminar espacios de trabajo | Permite a los usuarios crear y eliminar espacios de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permisos a nivel de empresa" }

{% endtab %}
{% tab Espacio de trabajo %}

### Espacio de trabajo {#workspace}

Puedes otorgar a un usuario diferentes permisos para cada espacio de trabajo al que pertenezca en Braze. Para gestionar sus permisos a nivel de espacio de trabajo, selecciona **Seleccionar espacios de trabajo y permisos** y luego elige sus permisos manualmente o asigna un [conjunto de permisos o rol]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set) que hayas creado previamente. Si necesitas dar a un usuario diferentes permisos para diferentes espacios de trabajo, repite este proceso tantas veces como sea necesario. Para ver la descripción de cada permiso, consulta [Lista de permisos]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions).

{% subtabs %}
{% subtab Seleccionar manualmente %}

En **Espacios de trabajo**, elige uno o más espacios de trabajo del menú desplegable. Luego, en **Permisos**, selecciona uno o más permisos. Se les asignarán estos permisos únicamente para los espacios de trabajo que hayas seleccionado. Opcionalmente, puedes seleccionar **Asignar acceso de administrador del espacio de trabajo** si prefieres otorgarles permisos completos para este espacio de trabajo.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel de espacio de trabajo siendo seleccionados manualmente en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_individual.png %})

{% endsubtab %}
{% subtab Asignar conjunto de permisos %}

En **Espacios de trabajo**, elige uno o más espacios de trabajo del menú desplegable. Luego, en **Conjuntos de permisos**, elige un conjunto de permisos. Se les asignarán estos permisos únicamente para los espacios de trabajo que hayas seleccionado.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel de espacio de trabajo siendo asignados a través de un conjunto de permisos en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_permissions_set.png %})

{% endsubtab %}
{% subtab Asignar rol %}

En **Espacios de trabajo**, elige uno o más espacios de trabajo del menú desplegable. Luego, en **Rol**, elige un rol. Se les asignarán estos permisos únicamente para los espacios de trabajo que hayas seleccionado.

Cuando hayas terminado, selecciona **Actualizar usuario**.

![Permisos a nivel de espacio de trabajo siendo asignados a través de un rol en Braze.]({% image_buster /assets/img/braze_permissions/workspace_level_role.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Exportación de permisos de usuario {#exporting-user-permissions}

Para descargar una lista de tus usuarios y sus permisos, ve a **Configuración** > **Administración de usuarios** > **Usuarios de la empresa**, y luego selecciona **Exportar usuarios**. En breve se enviará un archivo CSV a tu dirección de correo electrónico.

## Lista de permisos {#list-of-permissions}

### Mensajería {#messaging}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Campaigns | Ver Campaigns | Ver Campaigns |
| Campaigns | Lanzar Campaigns | Iniciar, detener, pausar o reanudar Campaigns existentes |
| Campaigns | Archivar Campaigns | Mover Campaigns al archivo |
| Campaigns | Editar Campaigns | Crear y actualizar Campaigns |
| Campaigns | Aprobar y denegar Campaigns | Aprobar o denegar Campaigns. El [flujo de trabajo de aprobación para Campaigns]({{site.baseurl}}/user_guide/messaging/governance/approvals) debe estar activado para que se aplique este permiso. |
| Canvas | Ver Canvas | Ver Canvas |
| Canvas | Archivar Canvas | Mover Canvas al archivo |
| Canvas | Editar Canvas | Crear y actualizar Canvas |
| Canvas | Lanzar Canvas | Iniciar, detener, pausar o reanudar Canvas existentes |
| Canvas | Aprobar y denegar Canvas | Aprobar o denegar Canvas. El [flujo de trabajo de aprobación para Canvas]({{site.baseurl}}/user_guide/messaging/governance/approvals) debe estar activado para que se aplique este permiso. |
| Conmutadores de características | Ver conmutadores de características | Ver conmutadores de características |
| Conmutadores de características | Archivar conmutadores de características | Mover conmutadores de características al archivo |
| Conmutadores de características | Editar conmutadores de características | Crear y actualizar conmutadores de características |
| Límites de frecuencia | Ver reglas de limitación de frecuencia | Ver reglas de limitación de frecuencia |
| Límites de frecuencia | Editar reglas de limitación de frecuencia | Crear y actualizar reglas de limitación de frecuencia |
| Páginas de destino | Ver páginas de destino | Ver páginas de destino |
| Páginas de destino | Publicar páginas de destino | Activar un borrador de página de destino |
| Páginas de destino | Editar borradores de páginas de destino | Crear y guardar borradores de páginas de destino |
| Configuración de archivado de mensajes | Ver configuración de archivado de mensajes | Ver la configuración de archivado de mensajes sin realizar cambios |
| Configuración de archivado de mensajes | Editar configuración de archivado de mensajes | Crear y actualizar la configuración de archivado de mensajes |
| Priorización de mensajes | Ver priorización de mensajes | Ver la configuración de priorización de mensajes sin realizar cambios |
| Priorización de mensajes | Editar priorización de mensajes | Crear y actualizar la configuración de priorización de mensajes |
| WhatsApp Flows | Ver WhatsApp Flows | Ver todos los WhatsApp Flows |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de mensajería" }

### Audiencia {#audience}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Grupo de control global | Ver grupo de control global | Ver la página de configuración del grupo de control global |
| Grupo de control global | Editar grupo de control global | Crear y guardar cambios en el grupo de control global. Los usuarios con el permiso "Editar grupo de control global" también deben tener permisos para "Editar Campaigns" y "Editar Canvas". Los usuarios con el permiso "Editar grupo de control global" también obtienen el permiso "Ver grupo de control global". |
| Ubicaciones | Archivar ubicaciones | Mover ubicaciones al archivo |
| Ubicaciones | Ver ubicaciones | Ver ubicaciones |
| Ubicaciones | Editar ubicaciones | Crear y editar ubicaciones |
| Segments | Ver Segments | Ver Segments. Los usuarios deben tener el permiso "Ver Segments" para tener el permiso "Editar Segments" o "Archivar Segments" |
| Segments | Archivar Segments | Archivar y desarchivar Segments. Los usuarios con el permiso "Archivar Segments" también deben tener el permiso "Ver Segments" |
| Segments | Editar Segments | Crear y actualizar Segments. Los usuarios con el permiso "Editar Segments" también deben tener el permiso "Ver Segments" |
| Datos de usuario | Ver importación de usuarios | Ver importaciones de usuarios en CSV sin realizar cambios |
| Datos de usuario | Importar usuarios | Cargar usuarios al panel |
| Datos de usuario | Editar datos de usuario | Crear y actualizar datos de usuario |
| Datos de usuario | Exportar datos de usuario | Descargar usuarios del panel |
| Usuarios duplicados | Ver registros de fusión de usuarios | Ver una lista de registros de fusión de usuarios |
| Usuarios | Ver perfiles de usuario (PII censurada) | Ver perfiles de usuario de manera compatible con PII. Los usuarios con este permiso no pueden guardar ni lanzar Campaigns que hagan referencia a atributos personalizados marcados como PII a menos que también tengan el permiso "Ver atributos personalizados marcados como PII".<br><br>El permiso "Ver perfiles de usuario (PII censurada)" debe habilitarse antes de su uso. Ponte en contacto con tu administrador de éxito de cliente para habilitarlo en tu espacio de trabajo. |
| Usuarios | Ver propiedades de eventos de usuario | Ver propiedades de eventos en la pestaña **Historial de eventos** en los perfiles de usuario |
| Usuarios duplicados | Fusionar usuarios duplicados | Combinar usuarios duplicados en un solo usuario. Los duplicados se eliminan después de la fusión |
| Eliminar usuarios | Ver registros de eliminación de usuarios | Ver una lista de registros de eliminación de usuarios |
| Eliminar usuarios | Eliminar usuarios | Eliminar permanentemente usuarios del panel de forma individual o masiva |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de audiencia" }

### Plantilla {#template}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Plantillas de banner | Ver plantillas de banner | Ver plantillas de banner |
| Plantillas de banner | Archivar plantillas de banner | Mover plantillas de banner al archivo |
| Plantillas de banner | Editar plantillas de banner | Crear y actualizar plantillas de banner |
| Plantillas de Canvas | Ver plantillas de Canvas | Ver plantillas de Canvas |
| Plantillas de Canvas | Archivar plantillas de Canvas | Mover plantillas de Canvas al archivo |
| Plantillas de Canvas | Crear y editar plantillas de Canvas | Crear y actualizar plantillas de Canvas |
| Content Blocks | Ver Content Blocks | Ver Content Blocks |
| Content Blocks | Lanzar Content Blocks | Publicar borradores de Content Blocks, y editar, archivar y desarchivar Content Blocks lanzados |
| Content Blocks | Archivar Content Blocks | Mover Content Blocks al archivo |
| Content Blocks | Editar Content Blocks | Crear Content Blocks y editar borradores de Content Blocks |
| Plantillas de enlaces de correo electrónico | Ver plantillas de enlaces de correo electrónico | Ver plantillas de enlaces sin realizar cambios |
| Plantillas de enlaces de correo electrónico | Editar plantillas de enlaces de correo electrónico | Crear y actualizar plantillas de enlaces |
| Plantillas de correo electrónico | Ver plantillas de correo electrónico | Ver plantillas de correo electrónico |
| Plantillas de correo electrónico | Archivar plantillas de correo electrónico | Mover plantillas de correo electrónico al archivo |
| Plantillas de correo electrónico | Editar plantillas de correo electrónico | Crear y actualizar plantillas de correo electrónico |
| Plantillas de IAM | Ver plantillas de IAM | Ver plantillas de mensajes dentro de la aplicación sin realizar cambios |
| Plantillas de IAM | Archivar plantillas de IAM | Mover plantillas de IAM al archivo |
| Plantillas de IAM | Editar plantillas de IAM | Crear y actualizar plantillas de mensajes dentro de la aplicación |
| Plantillas de páginas de destino | Ver plantillas de páginas de destino | Ver plantillas de páginas de destino |
| Plantillas de páginas de destino | Archivar plantillas de páginas de destino | Mover plantillas de páginas de destino al archivo |
| Plantillas de páginas de destino | Editar plantillas de páginas de destino | Crear y actualizar plantillas de páginas de destino |
| Plantillas de webhook | Ver plantillas de webhook | Ver plantillas de webhook sin realizar cambios |
| Plantillas de webhook | Archivar plantillas de webhook | Mover plantillas de webhook al archivo |
| Plantillas de webhook | Editar plantillas de webhook | Crear y actualizar plantillas de webhook |
| Plantillas de mensajes de WhatsApp | Ver plantillas de mensajes de WhatsApp | Permite a los usuarios ver [plantillas de mensajes de WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-2-compose-your-whatsapp-message) |
| Plantillas de mensajes de WhatsApp | Editar plantillas de mensajes de WhatsApp | Permite a los usuarios crear plantillas de mensajes de WhatsApp en el constructor de plantillas. Esta característica se encuentra actualmente en acceso anticipado. |
| Plantillas de mensajes de WhatsApp de Meta | Ver plantillas de mensajes de WhatsApp de Meta | Ver todas las plantillas de WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de plantillas" }

### Integraciones del partner {#partner-integrations}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Integraciones de Currents | Ver integración de Currents | Ver integraciones de Currents |
| Integraciones de Currents | Editar integraciones de Currents | Crear, actualizar y eliminar integraciones de Currents |
| Partners tecnológicos | Editar partners tecnológicos | Crear y actualizar partners tecnológicos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de integraciones del partner" }

### Configuración de datos {#data-settings}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Catálogos | Ver catálogos | Ver catálogos y selecciones |
| Catálogos | Eliminar catálogos | Eliminar catálogos permanentemente |
| Catálogos | Exportar catálogos | Descargar catálogos del panel |
| Catálogos | Editar catálogos | Crear y actualizar catálogos y selecciones |
| Ingesta de datos en la nube | Editar ingesta de datos en la nube | Crear, actualizar y eliminar fuentes y sincronizaciones |
| Atributos personalizados | Ver atributos personalizados | Ver atributos personalizados e informe de uso |
| Atributos personalizados | Exportar atributos personalizados | Descargar atributos personalizados del panel |
| Atributos personalizados | Eliminar atributos personalizados | Eliminar atributos personalizados permanentemente |
| Atributos personalizados | Bloquear atributos personalizados | Añadir atributos personalizados a una lista de bloqueo que restringe su uso en el panel |
| Atributos personalizados | Editar atributos personalizados | Crear y actualizar atributos personalizados |
| Segmentación por propiedades de eventos personalizados | Editar segmentación por propiedades de eventos personalizados | Habilitar y deshabilitar la segmentación para propiedades de eventos personalizados |
| Eventos personalizados | Ver eventos personalizados | Ver eventos personalizados e informe de uso, y añadir eventos personalizados al correo electrónico de informe de análisis diario |
| Eventos personalizados | Exportar eventos personalizados | Descargar eventos personalizados del panel |
| PII | Ver PII | Ver PII |
| Eventos personalizados | Eliminar eventos personalizados | Eliminar eventos personalizados permanentemente |
| Eventos personalizados | Bloquear eventos personalizados | Añadir eventos personalizados a una lista de bloqueo que restringe su uso en el panel |
| Eventos personalizados | Editar eventos personalizados | Crear y actualizar eventos personalizados |
| Productos | Ver productos | Ver productos |
| Productos | Bloquear productos | Añadir productos a una lista de bloqueo que restringe su uso en el panel |
| Productos | Editar productos | Crear y actualizar productos |
| Segmentación por propiedades de compra | Editar segmentación por propiedades de compra | Habilitar y deshabilitar la segmentación para propiedades de eventos de compra |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de configuración de datos" }

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
| Configuración de Audience Sync | Ver configuración de Audience Sync | Ver toda la configuración de sus partners conectados de Audience Sync |
| Usuarios del panel | Editar usuarios del panel | Ver, crear y editar usuarios de la empresa |
| Configuración de correo electrónico | Ver configuración de correo electrónico | Ver preferencias de correo electrónico |
| Configuración de correo electrónico | Editar configuración de correo electrónico | Habilitar y actualizar preferencias de correo electrónico |
| Registro de usuarios del evento | Ver registro de usuarios del evento | Ver registros de usuarios del evento |
| Grupos internos | Ver grupos internos de usuarios | Ver grupos internos |
| Grupos internos | Eliminar grupos internos de usuarios | Eliminar grupos internos |
| Grupos internos | Editar grupos internos de usuarios | Crear y actualizar grupos internos |
| Registro de actividad de mensajes | Ver registro de actividad de mensajes | Ver registros de actividad de mensajes |
| Configuración multilingüe | Ver configuración de localización | Ver la página de configuración de idiomas multilingüe |
| Configuración multilingüe | Eliminar configuración de localización | Eliminar idioma multilingüe |
| Configuración multilingüe | Editar configuración de localización | Crear idiomas multilingües |
| Centros de preferencias | Ver centros de preferencias | Ver centros de preferencias |
| Centros de preferencias | Editar centros de preferencias | Crear y actualizar centros de preferencias |
| Centros de preferencias | Lanzar centros de preferencias | Activar un borrador de centro de preferencias o actualizar uno existente |
| Configuración push | Ver configuración push | Ver configuración push |
| Configuración push | Editar configuración push | Crear y actualizar configuración push |
| Depurador de SDK | Ver depurador de SDK | Ver el depurador de SDK o las sesiones de depuración |
| Depurador de SDK | Editar depurador de SDK | Crear y descargar sesiones del depurador de SDK |
| Etiquetas | Ver etiquetas | Ver etiquetas |
| Etiquetas | Eliminar etiquetas | Eliminar etiquetas permanentemente |
| Etiquetas | Editar etiquetas | Crear y actualizar etiquetas |
| Equipos | Ver equipos | Ver equipos |
| Equipos | Archivar equipos | Mover equipos al archivo |
| Equipos | Editar equipos | Crear y actualizar equipos |
| Configuración de WhatsApp | Ver configuración de WhatsApp | Ver toda la configuración del canal de WhatsApp |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de configuración" }

### Decisioning Studio

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Agentes de Decisioning Studio | Ver agente de Decisioning Studio | Ver la configuración de agentes de Decisioning Studio sin realizar cambios |
| Audiencia de Decisioning Studio | Ver audiencia de Decisioning Studio | Ver detalles de audiencia en los resúmenes de configuración de agentes de Decisioning Studio |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permisos de Decisioning Studio" }

### Otros {#other}

| Área de producto | Permiso | Definición |
| --- | --- | --- |
| Uso de la aplicación | Ver datos de uso | Ver datos de uso |
| Facturación | Ver detalles de facturación | Ver detalles de facturación |
| Agentes personalizados | Ver agentes de IA de la consola de agentes | Permite a los usuarios ver agentes de IA personalizados |
| Agentes personalizados | Archivar agentes de IA de la consola de agentes | Permite a los usuarios archivar agentes de IA personalizados |
| Agentes personalizados | Editar agentes de IA de la consola de agentes | Permite a los usuarios crear y actualizar agentes de IA personalizados |
| Atributos personalizados marcados como PII | Ver atributos personalizados marcados como PII | Ver atributos personalizados marcados como PII |
| Informes del panel | Ver informes del panel | Ver informes sin realizar cambios |
| Informes del panel | Eliminar informes del panel | Eliminar informes permanentemente |
| Informes del panel | Editar informes del panel | Crear y actualizar informes |
| Configuración de dominio | Editar configuración de dominio | Añadir dominios delegados y dominios personalizados en Dominios verificados |
| Cifrado a nivel de campo | Editar cifrado a nivel de campo de identificadores | Habilitar y actualizar la configuración de cifrado a nivel de campo |
| Activos de la biblioteca multimedia | Ver activos de la biblioteca multimedia | Ver activos de la biblioteca multimedia |
| Activos de la biblioteca multimedia | Eliminar activos de la biblioteca multimedia | Eliminar activos de la biblioteca multimedia de la interfaz. Los activos eliminados siguen alojados en Braze para evitar que se rompan los mensajes que los referencian. Para eliminar un activo permanentemente, ponte en contacto con soporte de Braze. |
| Activos de la biblioteca multimedia | Editar activos de la biblioteca multimedia | Crear y actualizar activos de la biblioteca multimedia |
| Activos de la biblioteca multimedia | Reemplazar activos de la biblioteca multimedia | Reemplazar el archivo de un activo existente de la biblioteca multimedia manteniendo estables su URL e ID de activo |
| Límites de velocidad de mensajería | Ver límites de velocidad de mensajería | Ver los límites de velocidad de mensajería a nivel del espacio de trabajo |
| Límites de velocidad de mensajería | Editar límites de velocidad de mensajería | Configurar y editar los límites de velocidad de mensajería a nivel del espacio de trabajo |
| Operator | Usar BrazeAI Operator<sup>TM</sup> | Acceder y usar Braze Operator para responder preguntas, guiar la configuración, solucionar problemas y generar ideas |
| Placements | Ver placements | Ver placements de banner |
| Placements | Archivar placements | Mover placements de banner al archivo |
| Placements | Editar placements | Crear y actualizar placements de banner |
| Códigos promocionales | Ver códigos promocionales | Ver códigos promocionales |
| Códigos promocionales | Exportar códigos promocionales | Descargar una lista de códigos promocionales del panel |
| Códigos promocionales | Editar códigos promocionales | Crear y actualizar códigos promocionales |
| Grupos de suscripción | Editar suscripciones | Crear y actualizar grupos de suscripción |
| Transformaciones | Editar transformación de datos | Crear y actualizar transformaciones de datos |
| Transformaciones | Ver transformación de datos | Ver transformaciones de datos |
| Tickets de soporte | Crear ticket de soporte | Crear y actualizar tickets de soporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Otros permisos" }