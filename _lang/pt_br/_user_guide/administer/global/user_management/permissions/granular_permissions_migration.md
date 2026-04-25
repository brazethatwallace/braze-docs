---
nav_title: Migração de permissões granulares
article_title: Migrando para permissões granulares
page_order: 5
page_type: reference
alias: /granular_permissions_migration/
description: "Este artigo de referência cobre como se preparar para a migração para permissões de usuário granulares na Braze."
tool: Dashboard
---

# Migrando para permissões granulares

> Gerenciar quem pode acessar sua conta e realizar ações específicas é fundamental tanto para a segurança quanto para a eficiência operacional. Para dar a você mais controle, a Braze está introduzindo permissões granulares, uma maneira mais flexível e precisa de gerenciar o acesso dos usuários em toda a sua conta.

A migração inclui estes benefícios:

- **Controle mais preciso:** Permissões granulares oferecem mais controle, melhor segurança e supervisão mais clara. Os usuários recebem apenas o acesso de que precisam.
- **Mapeamento automático:** Todas as permissões atuais são mapeadas automaticamente para seus [equivalentes granulares](#legacy-to-granular-permissions-mapping). Seus usuários mantêm o mesmo nível de acesso, a menos que você o altere.

## O que analisar

Quando a migração for planejada para sua empresa, os administradores da Braze receberão e-mails e banners no dashboard notificando-os sobre a migração de permissões granulares. Para se preparar para a migração, recomendamos que um administrador da Braze faça o seguinte.

1. Identifique usuários, funções ou conjuntos de permissões que podem precisar ser atualizados para um acesso mais personalizado após você migrar para a nova estrutura de permissões.
2. Se sua empresa tem provisionamento automático de usuários usando SCIM ou ferramentas de conformidade que dependem de [strings de permissão]({{site.baseurl}}/scim_api_appendix/), atualize-as para corresponder à nova estrutura granular.
3. Informe seus usuários da Braze sobre quaisquer mudanças futuras para evitar confusão.
4. Na data e hora programadas para a migração, sua empresa será migrada automaticamente para permissões granulares. Nenhuma ação adicional é necessária dos administradores da empresa.

{% alert important %}
A capacidade de atualizar permissões será bloqueada 15 minutos antes do horário programado para a migração. Isso significa que você não poderá alterar nenhuma permissão até que a migração seja concluída, o que estimamos levar até 15 minutos.
{% endalert %}

## Mapeamento de permissões legadas para granulares {#legacy-to-granular-permissions-mapping}

Esta tabela mostra como cada permissão legada é mapeada para as permissões granulares. Consulte esta tabela ao atualizar suas permissões. Por exemplo, para dar a um usuário o mesmo acesso que a permissão legada "Manage Email Settings", esse usuário precisa ter as permissões granulares "View Email Settings" e "Edit Email Settings".

| | Permissões legadas | Permissões granulares |
|---------------|---------------|---------------|
| **Nível** | **Nome** | **Nome** |
| Admin | Admin | Admin |
| Workspace | Workspace Admin | Workspace Admin |
| Company | Create and delete workspaces | Create and delete workspaces |
| Company | Manage company settings | Manage company settings |
| Workspace | Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers | View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates<br>View Frequency Capping Rules<br>View Message Prioritization<br>View Content Blocks<br>Edit Content Blocks<br>View Custom Attributes<br>View Custom Events<br>View Catalogs<br>View Email Settings<br>View Feature Flags<br>View Segments<br>View Global Control Group<br>View Global Rate Limits<br>View IAM Templates<br>Edit IAM Templates<br>Archive IAM Templates<br>View Email Templates<br>Edit Email Templates<br>Archive Email Templates<br>View Webhook Templates<br>Edit Webhook Templates<br>Archive Webhook Templates<br>View Email Link Templates<br>Edit Email Link Templates<br>View Media Library Assets<br>View Locations<br>Edit Locations<br>Archive Locations<br>View Placements<br>View Promotion Codes<br>Edit Promotion Codes<br>Export Promotion Codes<br>View Preference Centers<br>Edit Preference Centers<br>View Push Settings<br>View Audience Sync Settings<br>View User Merge Records<br>View Dashboard Reports<br>Edit Dashboard Reports<br>Delete Dashboard Reports<br>View Localization Settings<br>View Decisioning Studio Agents<br>View Decisioning Studio Audience<br>View Decisioning Studio Agents<br>View Decisioning Studio Guardrails<br>View Decisioning Studio Action Banks<br>View WhatsApp Settings<br>View WhatsApp Flows<br>View WhatsApp Catalog<br>View WhatsApp Message Templates From Meta |
| Workspace | Access Dev Console | View API Keys<br>Edit API Keys<br>View Internal User Groups<br>Edit Internal User Groups<br>Delete Internal Groups<br>View Message Activity Log<br>View Event User Log<br>View API Identifiers<br>View API Usage Dashboard<br>View API Limits<br>View API Usage Alerts<br>Edit API Usage Alerts<br>View SDK Debugger<br>Edit SDK Debugger |
| Workspace | Approve and Deny Campaigns | Approve Campaigns |
| Workspace | Approve and Deny Canvases | Approve Canvases |
| Workspace | Export User Data | Export User Data |
| Workspace | Import and Update User Data | View Import Users<br>Import Users<br>Edit User Data |
| Workspace | Edit Segments | View Segments<br>Archive Segments<br>View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates |
| Workspace | Launch and Manage Content Blocks | View Content Blocks<br>Edit Content Blocks<br>Archive Content Blocks<br>Launch Content Blocks |
| Workspace | Manage Media Library | View Media Library Assets<br>Edit Media Library Assets<br>Delete Media Library Assets |
| Workspace | Launch Preference Centers | Launch Preference Centers |
| Workspace | Manage Apps | Edit App Settings<br>View Push Settings<br>Edit Push Settings<br>View Message Archiving Settings<br>Edit Message Archiving Settings<br>View Placements<br>Edit Placements<br>Archive Placements |
| Workspace | Manage Catalogs Dashboard Permission | View Catalogs<br>Edit Catalogs<br>Export Catalogs<br>Delete Catalogs |
| Workspace | Manage Custom Event Property Segmentation | View Custom Events<br>View Products<br>Edit Custom Event Property Segmentation<br>Edit Purchase Property Segmentation |
| Workspace | Manage Dashboard Users | Edit Dashboard Users |
| Workspace | Manage Email Settings | View Email Settings<br>Edit Email Settings |
| Workspace | Manage Events, Attributes, Purchases | View Custom Attributes<br>Edit Custom Attributes<br>Blocklist Custom Attributes<br>Delete Custom Attributes<br>Export Custom Attributes<br>View Custom Events<br>Edit Custom Events<br>Blocklist Custom Events<br>Delete Custom Events<br>Export Custom Events<br>View Products<br>Edit Products<br>Blocklist Products |
| Workspace | Manage External Integrations | Edit Technology Partners<br>Edit Cloud Data Ingestion<br>View Canvases<br>View Segments<br>View Catalogs<br>Edit Catalogs<br>View API Keys<br>Edit API Keys |
| Workspace | Manage Multi Language Settings | View Localization Settings<br>Edit Localization Settings<br>Delete Localization Settings |
| Workspace | Manage Subscription Groups | Edit Subscriptions |
| Workspace | Manage Tags | View Tags<br>Edit Tags<br>Delete Tags |
| Workspace | Manage Teams | View Teams<br>Edit Teams<br>Archive Teams |
| Workspace | View Data Transformations | View Data Transformation |
| Workspace | Edit Data Transformations | Edit Data Transformation |
| Workspace | Manage User Data Encryption | Edit Identifier Field-Level Encryption |
| Workspace | Send Campaigns, Canvases | View Campaigns<br>Edit Canvases<br>Launch Campaigns<br>View Canvases<br>Edit Campaigns<br>Launch Canvases<br>View Canvas Templates<br>View Frequency Caps<br>Edit Frequency Caps<br>View Global Control Group<br>Edit Global Control Group<br>View Segments |
| Workspace | View Billing Details | View Billing Details |
| Workspace | View Currents Integrations | View Currents Integrations |
| Workspace | Edit Currents Integrations | Edit Currents Integrations |
| Workspace | View Custom Attributes Marked as PII | View Custom Attributes Marked as PII |
| Workspace | View PII | View PII |
| Workspace | View User Profiles PII Compliant | View User Profiles (PII Redacted) |
| Workspace | View Usage Data | View Usage Data |
| Workspace | Merge Duplicate Users | View User Merge Records |
| Workspace | Create and Edit Canvas Templates | Edit Canvas Templates |
| Workspace | View Canvas Templates | View Canvas Templates |
| Workspace | Archive Canvas Templates | Archive Canvas Templates |
| Workspace | Publish Landing Pages | Publish Landing Pages |
| Workspace | Create Landing Page Drafts | Edit Landing Page Drafts |
| Workspace | Access Landing Pages | View Landing Pages |
| Workspace | Create and Edit Landing Page Templates | Edit Landing Page Templates |
| Workspace | View Landing Page Templates | View Landing Page Templates |
| Workspace | Archive Landing Page Templates | Archive Landing Page Templates |
| Workspace | View Custom AI Agents | View Custom AI Agents |
| Workspace | Edit Custom AI Agents | Edit Custom AI Agents<br> Archive Custom AI Agents |
| Workspace | View Placements | View Placements |
| Workspace | Edit Placements | Edit Placements |
| Workspace | Archive Placements | Archive Placements |
| Workspace | New | View Merge Users |
| Workspace | New | View User Deletion Records |
| Workspace | New | View Banner Templates |
| Workspace | New | Edit Banner Templates |
| Workspace | New | Archive Banner Templates |
| Team | Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers | View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates<br>View Content Blocks<br>Edit Content Blocks<br>View Media Library Assets<br>View Email Templates<br>Edit Email Templates<br>Archive Email Templates<br>View IAM Templates<br>Edit IAM Templates<br>Archive IAM Templates<br>View Webhook Templates<br>Edit Webhook Templates<br>Archive Webhook Templates<br>View Email Link Templates<br>Edit Email Link Templates<br>View Dashboard Reports<br>Edit Dashboard Reports<br>Delete Dashboard Reports<br>View Segments |
| Team | Edit Segments | View Segments<br>Archive Segments<br>View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates |
| Team | Launch and Manage Content Blocks | View Content Blocks<br>Edit Content Blocks<br>Archive Content Blocks<br>Launch Content Blocks |
| Team | Manage Media Library | View Media Library Assets<br>Edit Media Library Assets<br>Delete Media Library Assets |
| Team | Manage Dashboard Users | Edit Dashboard Users |
| Team | Send Campaigns, Canvases | View Campaigns<br>Edit Canvases<br>Launch Campaigns<br>View Canvases<br>Edit Campaigns<br>Launch Canvases<br>View Canvas Templates<br>View Segments |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Perguntas frequentes

### Posso cancelar ou reverter a migração?

A Braze não oferece suporte à reversão da migração. Daremos suporte a você durante a migração e a monitoraremos de perto para resolver rapidamente quaisquer problemas.

### Os usuários existentes perderão acesso à Braze durante a migração?

Não, não haverá indisponibilidade da Braze durante a migração. No entanto, as atualizações de permissões serão bloqueadas durante a migração. Estimamos que a migração leve até 15 minutos para ser concluída.