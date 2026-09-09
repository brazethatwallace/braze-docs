---
nav_title: Configuración de OAuth
article_title: Gestionar la configuración de OAuth
page_order: 4
page_type: reference
description: "Aprende a gestionar el acceso OAuth de MCP para el servidor MCP de Braze."
---

# Gestionar la configuración de OAuth {#manage-oauth-settings}

> La configuración de OAuth gestiona el acceso a nivel de empresa al [servidor MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server).

La configuración de OAuth se aplica a toda tu empresa. Los permisos asignados a cada usuario determinan a qué espacios de trabajo y características pueden acceder a través del servidor MCP.

## Requisitos {#requirements}

| Requisito | Descripción |
| --- | --- |
| Permiso "Admin" | Debes tener el permiso "Admin" a nivel de empresa para ver la configuración de OAuth o activar o desactivar el acceso OAuth de MCP. |
| Permiso "Use MCP Server" | Los usuarios deben tener este permiso en cada espacio de trabajo al que quieran acceder a través del servidor MCP. Este permiso es independiente del permiso "Admin" utilizado para gestionar la configuración de OAuth. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos para gestionar la configuración de OAuth" }

Para más información sobre la asignación de permisos, consulta [Permisos de usuario]({{site.baseurl}}/user_guide/administer/global/user_management/permissions).

## Cómo funciona el acceso OAuth {#how-oauth-access-works}

La configuración de OAuth y los permisos de usuario funcionan juntos:

- La configuración de OAuth a nivel de empresa determina si los usuarios pueden conectar clientes MCP a Braze.
- El permiso "Use MCP Server" determina si un usuario individual puede usar el servidor MCP en un espacio de trabajo.
- Los permisos existentes del panel del usuario determinan a qué datos y características de Braze puede acceder un cliente MCP.
- Una conexión OAuth solo puede acceder a los espacios de trabajo a los que el usuario tiene autorización para acceder.

Activar el acceso OAuth de MCP no otorga a los usuarios nuevos permisos de espacio de trabajo. Del mismo modo, eliminar un permiso del panel elimina esa capacidad del cliente MCP conectado del usuario.

## Controles de empresa y espacio de trabajo {#company-and-workspace-controls}

La política de OAuth se almacena a nivel de empresa. Los administradores de espacios de trabajo no pueden anular el **acceso OAuth de MCP** para un solo espacio de trabajo.

| Control | Dónde se configura | Alcance |
| --- | --- | --- |
| **Acceso OAuth de MCP** | **Configuración** > **Configuración de administrador** > **OAuth** | Toda la empresa. Cuando está desactivado, el OAuth de MCP se deniega en todos los espacios de trabajo. |
| Permiso "Use MCP Server" | **Configuración** > **Gestión de usuarios** | Por espacio de trabajo. Los usuarios necesitan este permiso en cada espacio de trabajo al que accedan a través del servidor MCP. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Controles de OAuth de empresa y espacio de trabajo" }

Solo los usuarios con el permiso "Admin" pueden cambiar el **acceso OAuth de MCP**. Para saber cómo interactúan los permisos de espacio de trabajo con esta configuración de empresa, consulta [OAuth y acceso MCP]({{site.baseurl}}/user_guide/administer/global/workspace_settings/oauth_settings).

## Activar o desactivar el acceso OAuth de MCP {#turn-mcp-oauth-access-on-or-off}

Para actualizar el acceso OAuth de MCP de tu empresa:

1. Ve a **Configuración** > **Configuración de administrador** > **OAuth**.
2. En **Controles de acceso global**, activa o desactiva el **acceso OAuth de MCP**.

Cuando el **acceso OAuth de MCP** está activado, los usuarios con el permiso "Use MCP Server" pueden autorizar clientes MCP aprobados.

Cuando está desactivado, el acceso OAuth al servidor MCP se deniega para todos los usuarios y espacios de trabajo de tu empresa. Las conexiones MCP existentes dejan de funcionar la próxima vez que usen o actualicen su token de acceso OAuth.

Si Braze ha desactivado el servidor MCP remoto para tu entorno, el interruptor de **acceso OAuth de MCP** está deshabilitado y un mensaje explica que la configuración de empresa no tiene efecto hasta que el servidor MCP remoto se active de nuevo.

## Auditar la actividad OAuth {#audit-oauth-activity}

Braze registra las conexiones OAuth al servidor MCP en el [informe de eventos de seguridad]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report). Usa este informe para auditar cuándo los usuarios se conectan a través de OAuth.

Para revocar el acceso MCP de un usuario, elimina el permiso "Use MCP Server" de ese usuario. Para obtener orientación sobre configuración y solución de problemas, consulta [Configuración del servidor MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server/setup).