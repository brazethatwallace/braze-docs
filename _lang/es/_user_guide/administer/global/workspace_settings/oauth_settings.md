---
nav_title: Acceso OAuth y MCP
article_title: Acceso OAuth y MCP en un espacio de trabajo
page_order: 10
page_type: reference
description: "Descubre qué acceso OAuth y MCP puedes controlar por espacio de trabajo y qué permanece a nivel de toda la empresa en la configuración de administrador."
---

# Acceso OAuth y MCP en un espacio de trabajo {#oauth-and-mcp-access-in-a-workspace}

> La política OAuth de toda la empresa se configura en [Configuración de administrador]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin). En un espacio de trabajo, concedes a usuarios individuales permiso para usar el servidor MCP.

No puedes activar ni desactivar el acceso MCP OAuth para un solo espacio de trabajo.

## Qué es a nivel de empresa frente a por espacio de trabajo {#whats-company-wide-versus-per-workspace}

| Control | A nivel de empresa | Por espacio de trabajo |
| --- | --- | --- |
| **Acceso MCP OAuth** | Sí. Este interruptor está en **Configuración** > **Configuración de administrador** > **OAuth** en **Controles de acceso global**. | No. Los administradores del espacio de trabajo no pueden anular la configuración de la empresa. |
| Permiso "Use MCP Server" | No. | Sí. Concede este permiso para cada espacio de trabajo al que el usuario deba acceder a través del servidor MCP. |
| Permisos del panel reflejados por MCP | No. | Sí. El cliente MCP solo puede usar las características de Braze a las que el usuario ya tiene acceso en ese espacio de trabajo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Controles OAuth a nivel de empresa frente a por espacio de trabajo" }

## Si el acceso MCP OAuth está desactivado para la empresa {#if-mcp-oauth-access-is-off-for-the-company}

Cuando el **acceso MCP OAuth** está desactivado en **Configuración de administrador**, Braze deniega MCP OAuth para todos los espacios de trabajo. Los usuarios con el permiso "Use MCP Server" aún no pueden conectarse, y no existe una configuración a nivel de espacio de trabajo para volver a activar el acceso MCP OAuth.

Los usuarios que intenten conectarse pueden ver un mensaje indicando que el acceso remoto MCP no se ha activado para la empresa. Un administrador de la empresa puede activar el **acceso MCP OAuth** en **Configuración** > **Configuración de administrador** > **OAuth**.

Para obtener información sobre el acceso MCP OAuth a nivel de empresa y quién puede cambiar esa configuración, consulta [Gestionar la configuración de OAuth]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin).