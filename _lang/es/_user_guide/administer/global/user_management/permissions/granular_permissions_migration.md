---
nav_title: Migración de permisos granulares
article_title: Migración a permisos granulares
page_order: 5
page_type: reference
alias: /granular_permissions_migration/
description: "Este artículo de referencia explica cómo prepararse para la migración a permisos de usuario granulares en Braze."
tool: Dashboard
---

# Migración a permisos granulares

> Gestionar quién puede acceder a tu cuenta y realizar acciones específicas es fundamental tanto para la seguridad como para la eficiencia operativa. Para ofrecerte un mayor control, Braze introduce permisos granulares, una forma más flexible y precisa de gestionar el acceso de los usuarios a tu cuenta.

La migración incluye las siguientes ventajas:

- **Control más preciso:** Los permisos granulares ofrecen más control, mayor seguridad y una supervisión más clara. Los usuarios solo obtienen el acceso que necesitan.
- **Mapeado automático:** Todos los permisos actuales se mapean automáticamente a sus [equivalentes granulares](#legacy-to-granular-permissions-mapping). Tus usuarios mantendrán el mismo nivel de acceso a menos que tú lo cambies.

## Qué revisar

Cuando se planifique la migración para tu empresa, los administradores de Braze recibirán correos electrónicos y banners en el dashboard notificándoles la migración de permisos granulares. Para prepararte para la migración, recomendamos que un administrador de Braze haga lo siguiente.

1. Identifica los usuarios, roles o conjuntos de permisos que puedan necesitar actualizarse para obtener un acceso más personalizado después de la migración al nuevo marco de permisos.
2. Si tu empresa ha automatizado el aprovisionamiento de usuarios mediante SCIM o herramientas de cumplimiento que se basan en [cadenas de permisos]({{site.baseurl}}/scim_api_appendix/), actualízalas para que coincidan con la nueva estructura granular.
3. Informa a tus usuarios de Braze sobre los próximos cambios para evitar confusiones.
4. En la fecha y hora programadas para la migración, tu empresa migrará automáticamente a permisos granulares. No se requiere ninguna acción adicional por parte de los administradores de la empresa.

{% alert important %}
La posibilidad de actualizar permisos se bloqueará en los 15 minutos previos a la hora programada para la migración. Esto significa que no podrás cambiar ningún permiso hasta que la migración haya finalizado, lo cual estimamos que tardará hasta 15 minutos.
{% endalert %}

## Mapeado de permisos heredados a permisos granulares {#legacy-to-granular-permissions-mapping}

Esta tabla muestra cómo cada permiso heredado se mapea a los permisos granulares. Consulta esta tabla mientras actualizas tus permisos. Por ejemplo, para otorgar a un usuario el mismo acceso que el permiso heredado "Manage Email Settings", ese usuario necesita tener tanto el permiso granular "View Email Settings" como "Edit Email Settings".

| | Permisos heredados | Permisos granulares |
|---------------|---------------|---------------|
| **Nivel** | **Nombre** | **Nombre** |
| Admin | Admin | Admin |
| Espacio de trabajo | Workspace Admin | Workspace Admin |
| Empresa | Create and delete workspaces | Create and delete workspaces |
| Empresa | Manage company settings | Manage company settings |
| Espacio de trabajo | Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers | View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates<br>View Frequency Capping Rules<br>View Message Prioritization<br>View Content Blocks<br>Edit Content Blocks<br>View Custom Attributes<br>View Custom Events<br>View Catalogs<br>View Email Settings<br>View Feature Flags<br>View Segments<br>View Global Control Group<br>View Global Rate Limits<br>View IAM Templates<br>Edit IAM Templates<br>Archive IAM Templates<br>View Email Templates<br>Edit Email Templates<br>Archive Email Templates<br>View Webhook Templates<br>Edit Webhook Templates<br>Archive Webhook Templates<br>View Email Link Templates<br>Edit Email Link Templates<br>View Media Library Assets<br>View Locations<br>Edit Locations<br>Archive Locations<br>View Placements<br>View Promotion Codes<br>Edit Promotion Codes<br>Export Promotion Codes<br>View Preference Centers<br>Edit Preference Centers<br>View Push Settings<br>View Audience Sync Settings<br>View User Merge Records<br>View Dashboard Reports<br>Edit Dashboard Reports<br>Delete Dashboard Reports<br>View Localization Settings<br>View Decisioning Studio Agents<br>View Decisioning Studio Audience<br>View Decisioning Studio Agents<br>View Decisioning Studio Guardrails<br>View Decisioning Studio Action Banks<br>View WhatsApp Settings<br>View WhatsApp Flows<br>View WhatsApp Catalog<br>View WhatsApp Message Templates From Meta |
| Espacio de trabajo | Access Dev Console | View API Keys<br>Edit API Keys<br>View Internal User Groups<br>Edit Internal User Groups<br>Delete Internal Groups<br>View Message Activity Log<br>View Event User Log<br>View API Identifiers<br>View API Usage Dashboard<br>View API Limits<br>View API Usage Alerts<br>Edit API Usage Alerts<br>View SDK Debugger<br>Edit SDK Debugger |
| Espacio de trabajo | Approve and Deny Campaigns | Approve Campaigns |
| Espacio de trabajo | Approve and Deny Canvases | Approve Canvases |
| Espacio de trabajo | Export User Data | Export User Data |
| Espacio de trabajo | Import and Update User Data | View Import Users<br>Import Users<br>Edit User Data |
| Espacio de trabajo | Edit Segments | View Segments<br>Archive Segments<br>View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates |
| Espacio de trabajo | Launch and Manage Content Blocks | View Content Blocks<br>Edit Content Blocks<br>Archive Content Blocks<br>Launch Content Blocks |
| Espacio de trabajo | Manage Media Library | View Media Library Assets<br>Edit Media Library Assets<br>Delete Media Library Assets |
| Espacio de trabajo | Launch Preference Centers | Launch Preference Centers |
| Espacio de trabajo | Manage Apps | Edit App Settings<br>View Push Settings<br>Edit Push Settings<br>View Message Archiving Settings<br>Edit Message Archiving Settings<br>View Placements<br>Edit Placements<br>Archive Placements |
| Espacio de trabajo | Manage Catalogs Dashboard Permission | View Catalogs<br>Edit Catalogs<br>Export Catalogs<br>Delete Catalogs |
| Espacio de trabajo | Manage Custom Event Property Segmentation | View Custom Events<br>View Products<br>Edit Custom Event Property Segmentation<br>Edit Purchase Property Segmentation |
| Espacio de trabajo | Manage Dashboard Users | Edit Dashboard Users |
| Espacio de trabajo | Manage Email Settings | View Email Settings<br>Edit Email Settings |
| Espacio de trabajo | Manage Events, Attributes, Purchases | View Custom Attributes<br>Edit Custom Attributes<br>Blocklist Custom Attributes<br>Delete Custom Attributes<br>Export Custom Attributes<br>View Custom Events<br>Edit Custom Events<br>Blocklist Custom Events<br>Delete Custom Events<br>Export Custom Events<br>View Products<br>Edit Products<br>Blocklist Products |
| Espacio de trabajo | Manage External Integrations | Edit Technology Partners<br>Edit Cloud Data Ingestion<br>View Canvases<br>View Segments<br>View Catalogs<br>Edit Catalogs<br>View API Keys<br>Edit API Keys |
| Espacio de trabajo | Manage Multi Language Settings | View Localization Settings<br>Edit Localization Settings<br>Delete Localization Settings |
| Espacio de trabajo | Manage Subscription Groups | Edit Subscriptions |
| Espacio de trabajo | Manage Tags | View Tags<br>Edit Tags<br>Delete Tags |
| Espacio de trabajo | Manage Teams | View Teams<br>Edit Teams<br>Archive Teams |
| Espacio de trabajo | View Data Transformations | View Data Transformation |
| Espacio de trabajo | Edit Data Transformations | Edit Data Transformation |
| Espacio de trabajo | Manage User Data Encryption | Edit Identifier Field-Level Encryption |
| Espacio de trabajo | Send Campaigns, Canvases | View Campaigns<br>Edit Canvases<br>Launch Campaigns<br>View Canvases<br>Edit Campaigns<br>Launch Canvases<br>View Canvas Templates<br>View Frequency Caps<br>Edit Frequency Caps<br>View Global Control Group<br>Edit Global Control Group<br>View Segments |
| Espacio de trabajo | View Billing Details | View Billing Details |
| Espacio de trabajo | View Currents Integrations | View Currents Integrations |
| Espacio de trabajo | Edit Currents Integrations | Edit Currents Integrations |
| Espacio de trabajo | View Custom Attributes Marked as PII | View Custom Attributes Marked as PII |
| Espacio de trabajo | View PII | View PII |
| Espacio de trabajo | View User Profiles PII Compliant | View User Profiles (PII Redacted) |
| Espacio de trabajo | View Usage Data | View Usage Data |
| Espacio de trabajo | Merge Duplicate Users | View User Merge Records |
| Espacio de trabajo | Create and Edit Canvas Templates | Edit Canvas Templates |
| Espacio de trabajo | View Canvas Templates | View Canvas Templates |
| Espacio de trabajo | Archive Canvas Templates | Archive Canvas Templates |
| Espacio de trabajo | Publish Landing Pages | Publish Landing Pages |
| Espacio de trabajo | Create Landing Page Drafts | Edit Landing Page Drafts |
| Espacio de trabajo | Access Landing Pages | View Landing Pages |
| Espacio de trabajo | Create and Edit Landing Page Templates | Edit Landing Page Templates |
| Espacio de trabajo | View Landing Page Templates | View Landing Page Templates |
| Espacio de trabajo | Archive Landing Page Templates | Archive Landing Page Templates |
| Espacio de trabajo | View Custom AI Agents | View Custom AI Agents |
| Espacio de trabajo | Edit Custom AI Agents | Edit Custom AI Agents<br> Archive Custom AI Agents |
| Espacio de trabajo | View Placements | View Placements |
| Espacio de trabajo | Edit Placements | Edit Placements |
| Espacio de trabajo | Archive Placements | Archive Placements |
| Espacio de trabajo | Nuevo | View Merge Users |
| Espacio de trabajo | Nuevo | View User Deletion Records |
| Espacio de trabajo | Nuevo | View Banner Templates |
| Espacio de trabajo | Nuevo | Edit Banner Templates |
| Espacio de trabajo | Nuevo | Archive Banner Templates |
| Equipo | Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers | View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates<br>View Content Blocks<br>Edit Content Blocks<br>View Media Library Assets<br>View Email Templates<br>Edit Email Templates<br>Archive Email Templates<br>View IAM Templates<br>Edit IAM Templates<br>Archive IAM Templates<br>View Webhook Templates<br>Edit Webhook Templates<br>Archive Webhook Templates<br>View Email Link Templates<br>Edit Email Link Templates<br>View Dashboard Reports<br>Edit Dashboard Reports<br>Delete Dashboard Reports<br>View Segments |
| Equipo | Edit Segments | View Segments<br>Archive Segments<br>View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates |
| Equipo | Launch and Manage Content Blocks | View Content Blocks<br>Edit Content Blocks<br>Archive Content Blocks<br>Launch Content Blocks |
| Equipo | Manage Media Library | View Media Library Assets<br>Edit Media Library Assets<br>Delete Media Library Assets |
| Equipo | Manage Dashboard Users | Edit Dashboard Users |
| Equipo | Send Campaigns, Canvases | View Campaigns<br>Edit Canvases<br>Launch Campaigns<br>View Canvases<br>Edit Campaigns<br>Launch Canvases<br>View Canvas Templates<br>View Segments |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Preguntas frecuentes

### ¿Puedo rechazar o revertir la migración?

Braze no admite la reversión de la migración. Te acompañaremos durante el proceso y supervisaremos la migración de cerca para resolver rápidamente cualquier problema.

### ¿Los usuarios existentes perderán acceso a Braze durante la migración?

No, no habrá tiempo de inactividad en Braze durante la migración. Sin embargo, las actualizaciones de permisos estarán bloqueadas durante la migración. Estimamos que la migración tardará hasta 15 minutos en completarse.