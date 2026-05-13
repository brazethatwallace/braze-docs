---
nav_title: 세분화된 권한 마이그레이션
article_title: 세분화된 권한으로 마이그레이션
page_order: 5
page_type: reference
alias: /granular_permissions_migration/
description: "이 참조 문서에서는 Braze에서 세분화된 사용자 권한으로의 마이그레이션을 준비하는 방법을 다룹니다."
tool: Dashboard
---

# 세분화된 권한으로 마이그레이션 {#migrating-to-granular-permissions}

> 계정에 접근하고 특정 동작을 수행할 수 있는 사용자를 관리하는 것은 보안과 운영 효율성 모두에 매우 중요합니다. Braze는 더 많은 제어를 제공하기 위해, 계정 전반에서 사용자 접근을 보다 유연하고 정밀하게 관리할 수 있는 세분화된 권한을 도입하고 있습니다.

마이그레이션에는 다음과 같은 이점이 포함됩니다:

- **보다 정밀한 제어:** 세분화된 권한은 더 많은 제어, 더 나은 보안, 더 명확한 감독을 제공합니다. 사용자는 필요한 접근 권한만 부여받습니다.
- **자동 매핑:** 모든 기존 권한은 [세분화된 동등 권한](#legacy-to-granular-permissions-mapping)에 자동으로 매핑됩니다. 변경하지 않는 한 사용자의 접근 수준은 동일하게 유지됩니다.

## 검토할 사항 {#what-to-review}

귀사의 마이그레이션이 계획되면, Braze 관리자에게 세분화된 권한 마이그레이션을 알리는 이메일과 대시보드 내 배너가 전송됩니다. 마이그레이션을 준비하기 위해 Braze 관리자가 다음을 수행할 것을 권장합니다.

1. 새 권한 프레임워크로 마이그레이션한 후 보다 맞춤화된 접근을 위해 업데이트가 필요할 수 있는 사용자, 역할 또는 권한 세트를 식별합니다.
2. 귀사에서 SCIM 또는 [권한 문자열]({{site.baseurl}}/scim_api_appendix/)에 의존하는 규정 준수 도구를 사용하여 자동 사용자 프로비저닝을 하고 있다면, 새로운 세분화된 구조에 맞게 업데이트하세요.
3. 혼란을 방지하기 위해 Braze 사용자에게 예정된 변경 사항을 알립니다.
4. 예정된 마이그레이션 날짜와 시간에 귀사는 자동으로 세분화된 권한으로 마이그레이션됩니다. 회사 관리자의 추가 조치는 필요하지 않습니다.

{% alert important %}
권한 업데이트 기능은 예정된 마이그레이션 시간 15분 전에 잠깁니다. 이는 마이그레이션이 완료될 때까지 권한을 변경할 수 없음을 의미하며, 마이그레이션은 최대 15분이 소요될 것으로 예상됩니다.
{% endalert %}

## 레거시에서 세분화된 권한 매핑 {#legacy-to-granular-permissions-mapping}

이 표는 각 레거시 권한이 세분화된 권한에 어떻게 매핑되는지를 보여줍니다. 권한을 업데이트할 때 이 표를 참조하세요. 예를 들어, 사용자에게 "Manage Email Settings" 레거시 권한과 동일한 접근 권한을 부여하려면 해당 사용자에게 "View Email Settings"와 "Edit Email Settings" 세분화된 권한을 모두 부여해야 합니다.

| | 레거시 권한 | 세분화된 권한 |
|---------------|---------------|---------------|
| **레벨** | **이름** | **이름** |
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
| Workspace | Edit Custom AI Agents | Edit Custom AI Agents<br>Archive Custom AI Agents |
| Workspace | View Placements | View Placements |
| Workspace | Edit Placements | Edit Placements |
| Workspace | Archive Placements | Archive Placements |
| Workspace | New | View Merge Users |
| Workspace | New | View User Deletion Records |
| Workspace | New | View Banner Templates |
| Workspace | New | Edit Banner Templates |
| Workspace | New | Archive Banner Templates |
| Teams | Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library, Locations, Promotion Codes, and Preference Centers | View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates<br>View Content Blocks<br>Edit Content Blocks<br>View Media Library Assets<br>View Email Templates<br>Edit Email Templates<br>Archive Email Templates<br>View IAM Templates<br>Edit IAM Templates<br>Archive IAM Templates<br>View Webhook Templates<br>Edit Webhook Templates<br>Archive Webhook Templates<br>View Email Link Templates<br>Edit Email Link Templates<br>View Dashboard Reports<br>Edit Dashboard Reports<br>Delete Dashboard Reports<br>View Segments |
| Teams | Edit Segments | View Segments<br>Archive Segments<br>View Campaigns<br>Edit Campaigns<br>Archive Campaigns<br>View Canvases<br>Edit Canvases<br>Archive Canvases<br>View Canvas Templates |
| Teams | Launch and Manage Content Blocks | View Content Blocks<br>Edit Content Blocks<br>Archive Content Blocks<br>Launch Content Blocks |
| Teams | Manage Media Library | View Media Library Assets<br>Edit Media Library Assets<br>Delete Media Library Assets |
| Teams | Manage Dashboard Users | Edit Dashboard Users |
| Teams | Send Campaigns, Canvases | View Campaigns<br>Edit Canvases<br>Launch Campaigns<br>View Canvases<br>Edit Campaigns<br>Launch Canvases<br>View Canvas Templates<br>View Segments |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Legacy to granular permissions mapping" }

## 자주 묻는 질문 {#frequently-asked-questions}

### 마이그레이션을 거부하거나 되돌릴 수 있나요? {#can-i-opt-out-of-or-revert-the-migration}

Braze는 마이그레이션 되돌리기를 지원하지 않습니다. 마이그레이션 과정에서 지원을 제공하며, 문제가 발생하면 신속하게 해결할 수 있도록 마이그레이션을 면밀히 모니터링합니다.

### 마이그레이션 중에 기존 사용자가 Braze에 접근할 수 없게 되나요? {#will-existing-users-lose-access-to-braze-during-the-migration}

아니요, 마이그레이션 중에 Braze 중단 시간은 없습니다. 다만, 마이그레이션 중에는 권한 업데이트가 잠깁니다. 마이그레이션은 완료까지 최대 15분이 소요될 것으로 예상됩니다.