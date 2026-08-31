---
nav_title: OAuth and MCP access
article_title: OAuth and MCP access in a workspace
page_order: 10
page_type: reference
description: "Learn what OAuth and MCP access you can control per workspace, and what remains company-wide in Admin settings."
---

# OAuth and MCP access in a workspace

> Company-wide OAuth policy is configured in [Admin settings]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin/). In a workspace, you grant individual users permission to use the MCP server.

You can't turn MCP OAuth access on or off for one workspace.

## What's company-wide versus per-workspace

| Control | Company-wide | Per workspace |
| --- | --- | --- |
| **MCP OAuth access** | Yes. This toggle is in **Settings** > **Admin Settings** > **OAuth** under **Global access controls**. | No. Workspace admins can't override the company setting. |
| "Use MCP Server" permission | No. | Yes. Grant this permission for each workspace the user should access through the MCP server. |
| Dashboard permissions mirrored by MCP | No. | Yes. The MCP client can use only the Braze features the user can already access in that workspace. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Company-wide versus per-workspace OAuth controls" }

## If MCP OAuth access is off for the company

When **MCP OAuth access** is off in **Admin Settings**, Braze denies MCP OAuth for every workspace. Users with the "Use MCP Server" permission still can't connect, and there is no workspace-level setting to turn MCP OAuth access back on.

Users who try to connect may see a message that remote MCP access hasn't been turned on for the company. A company admin can turn on **MCP OAuth access** in **Settings** > **Admin Settings** > **OAuth**.

For company-level MCP OAuth access and who can change that setting, see [Manage OAuth settings]({{site.baseurl}}/user_guide/administer/global/admin_settings/oauth_admin/).
