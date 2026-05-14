---
nav_title: Migration granularer Berechtigungen
article_title: Migration zu granularen Berechtigungen
page_order: 5
page_type: reference
alias: /granular_permissions_migration/
description: "Dieser Referenzartikel behandelt die Vorbereitung auf die Migration zu granularen Nutzerberechtigungen in Braze."
tool: Dashboard
---

# Migration zu granularen Berechtigungen {#migrating-to-granular-permissions}

> Die Verwaltung der Zugriffsrechte auf Ihr Konto und die Ausführung bestimmter Aktionen ist sowohl für die Sicherheit als auch für die betriebliche Effizienz von entscheidender Bedeutung. Um Ihnen mehr Kontrolle zu geben, führt Braze granulare Berechtigungen ein – eine flexiblere und präzisere Methode zur Verwaltung des Nutzerzugriffs auf Ihr Konto.

Die Migration bietet folgende Vorteile:

- **Präzisere Steuerung:** Granulare Berechtigungen bieten mehr Kontrolle, höhere Sicherheit und eine übersichtlichere Übersicht. Nutzer:innen erhalten ausschließlich die Zugriffsrechte, die sie benötigen.
- **Automatische Abbildung:** Alle aktuellen Berechtigungen werden automatisch auf ihre [granularen Entsprechungen](#legacy-to-granular-permissions-mapping) abgebildet. Ihre Nutzer:innen behalten die gleiche Zugriffsebene, sofern Sie diese nicht ändern.

## Was Sie überprüfen sollten {#what-to-review}

Wenn für Ihr Unternehmen eine Migration geplant ist, erhalten Ihre Braze-Administratoren E-Mails und Banner im Dashboard, die sie über die Migration der granularen Berechtigungen informieren. Zur Vorbereitung auf die Migration empfehlen wir, dass ein Braze-Administrator die folgenden Schritte durchführt.

1. Identifizieren Sie Nutzer:innen, Rollen oder Berechtigungssätze, die möglicherweise aktualisiert werden müssen, um nach der Migration zum neuen Berechtigungsrahmen einen maßgeschneiderten Zugriff zu gewährleisten.
2. Wenn Ihr Unternehmen die automatisierte Nutzerbereitstellung über SCIM oder Compliance-Tools nutzt, die auf [Berechtigungs-Strings]({{site.baseurl}}/scim_api_appendix/) basieren, aktualisieren Sie diese, damit sie der neuen granularen Struktur entsprechen.
3. Informieren Sie Ihre Braze-Nutzer:innen über bevorstehende Änderungen, um Verwirrung zu vermeiden.
4. Zum geplanten Migrationszeitpunkt wird Ihr Unternehmen automatisch auf granulare Berechtigungen migriert. Es sind keine weiteren Maßnahmen seitens der Unternehmensadministratoren erforderlich.

{% alert important %}
Die Möglichkeit, Berechtigungen zu aktualisieren, wird 15 Minuten vor dem geplanten Migrationszeitpunkt gesperrt. Das bedeutet, dass Sie keine Berechtigungen ändern können, bis die Migration abgeschlossen ist – dies dauert voraussichtlich bis zu 15 Minuten.
{% endalert %}

## Abbildung von Legacy- auf granulare Berechtigungen {#legacy-to-granular-permissions-mapping}

Diese Tabelle zeigt, wie jede Legacy-Berechtigung auf die granularen Berechtigungen abgebildet wird. Verwenden Sie diese Tabelle bei der Aktualisierung Ihrer Berechtigungen. Um beispielsweise einer Nutzerin oder einem Nutzer den gleichen Zugriff wie bei der Legacy-Berechtigung „Manage Email Settings“ zu gewähren, benötigt diese Person sowohl die granulare Berechtigung „View Email Settings“ als auch „Edit Email Settings“.

| | Legacy-Berechtigungen | Granulare Berechtigungen |
|---------------|---------------|---------------|
| **Ebene** | **Name** | **Name** |
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Legacy to granular permissions mapping" }

## Häufig gestellte Fragen {#frequently-asked-questions}

### Kann ich die Migration ablehnen oder rückgängig machen? {#can-i-opt-out-of-or-revert-the-migration}

Braze unterstützt keine Rücknahme der Migration. Wir begleiten Sie durch die Migration und überwachen den Prozess engmaschig, um auftretende Probleme schnell zu beheben.

### Verlieren bestehende Nutzer:innen während der Migration den Zugriff auf Braze? {#will-existing-users-lose-access-to-braze-during-the-migration}

Nein, es gibt während der Migration keine Ausfallzeit bei Braze. Allerdings werden Änderungen an Berechtigungen während der Migration gesperrt. Wir gehen davon aus, dass die Migration bis zu 15 Minuten dauert.