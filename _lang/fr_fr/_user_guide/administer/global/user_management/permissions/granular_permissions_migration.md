---
nav_title: Migration des autorisations granulaires
article_title: Migration vers des autorisations granulaires
page_order: 5
page_type: reference
alias: /granular_permissions_migration/
description: "Cet article de référence explique comment se préparer à la migration vers les autorisations utilisateur granulaires dans Braze."
tool: Dashboard
---

# Migration vers des autorisations granulaires

> Contrôler qui peut accéder à votre compte et effectuer des actions spécifiques est essentiel, tant pour la sécurité que pour l'efficacité opérationnelle. Afin de vous offrir davantage de contrôle, Braze met en place des autorisations granulaires : une méthode plus flexible et plus précise pour gérer l'accès des utilisateurs à votre compte.

La migration offre les avantages suivants :

- **Contrôle plus précis :** Les autorisations granulaires offrent un contrôle accru, une sécurité renforcée et une supervision plus claire. Les utilisateurs n'obtiennent que l'accès dont ils ont besoin.
- **Mappage automatique :** Toutes les autorisations actuelles font l'objet d'un mappage automatique vers leurs [équivalents granulaires](#legacy-to-granular-permissions-mapping). Vos utilisateurs conservent le même niveau d'accès, sauf si vous le modifiez.

## Ce qu'il faut vérifier

Lorsque la migration est planifiée pour votre entreprise, vos administrateurs Braze recevront des e-mails et des bannières sur le tableau de bord les informant de la migration des autorisations granulaires. Pour préparer la migration, nous recommandons qu'un administrateur Braze procède comme suit.

1. Identifiez les utilisateurs, les rôles ou les ensembles d'autorisations qui pourraient nécessiter une mise à jour afin d'offrir un accès plus adapté après la migration vers le nouveau cadre d'autorisations.
2. Si votre entreprise a automatisé le provisionnement des utilisateurs via SCIM ou des outils de conformité qui s'appuient sur les [chaînes d'autorisations]({{site.baseurl}}/scim_api_appendix/), mettez-les à jour pour correspondre à la nouvelle structure granulaire.
3. Informez vos utilisateurs Braze de tout changement à venir pour éviter toute confusion.
4. À la date et à l'heure prévues de la migration, votre entreprise sera automatiquement migrée vers les autorisations granulaires. Aucune action supplémentaire n'est requise de la part des administrateurs de l'entreprise.

{% alert important %}
La possibilité de mettre à jour les autorisations sera verrouillée dans les 15 minutes précédant l'heure de migration prévue. Cela signifie que vous ne pourrez modifier aucune autorisation tant que la migration ne sera pas terminée, ce qui devrait prendre jusqu'à 15 minutes.
{% endalert %}

## Mappage des autorisations héritées vers les autorisations granulaires {#legacy-to-granular-permissions-mapping}

Ce tableau montre comment chaque autorisation héritée correspond aux autorisations granulaires. Consultez ce tableau lors de la mise à jour de vos autorisations. Par exemple, pour accorder à un utilisateur le même accès que l'autorisation héritée « Manage Email Settings », cet utilisateur doit disposer des autorisations granulaires « View Email Settings » et « Edit Email Settings ».

| | Autorisations héritées | Autorisations granulaires |
|---------------|---------------|---------------|
| **Niveau** | **Nom** | **Nom** |
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

## Questions fréquentes

### Puis-je refuser ou annuler la migration ?

Braze ne prend pas en charge l'annulation de la migration. Nous vous accompagnerons tout au long du processus et surveillerons la migration de près afin de résoudre rapidement tout problème éventuel.

### Les utilisateurs existants perdront-ils l'accès à Braze pendant la migration ?

Non, il n'y aura aucun temps d'arrêt de Braze pendant la migration. Cependant, les mises à jour des autorisations seront verrouillées pendant la migration. Nous estimons que la migration prendra jusqu'à 15 minutes.