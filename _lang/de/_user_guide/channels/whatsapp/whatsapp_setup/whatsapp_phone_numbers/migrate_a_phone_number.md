---
nav_title: "Eine Nummer migrieren"
article_title: "Eine WhatsApp-Telefonnummer migrieren"
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie Ihre WhatsApp-Telefonnummer migrieren."
page_type: reference
channel:
  - WhatsApp
---

# Eine WhatsApp-Telefonnummer migrieren {#migrate-a-whatsapp-phone-number}

> Migrieren Sie Ihre WhatsApp-Telefonnummer zwischen WhatsApp Business-Konten mithilfe von Metas Embedded Signup.

## Voraussetzungen {#prerequisites}

Ihre Telefonnummer muss die Anforderungen von Meta erfüllen, um für die Migration berechtigt zu sein:

- Ihr Meta Business-Konto ist verifiziert.
- Ihr bestehendes WhatsApp Business-Konto ist genehmigt.
- Ihr bestehendes WhatsApp Business-Konto verfügt über eine gültige Zahlungsmethode unter **Payment Settings**.
- Für Ihre geschäftliche Telefonnummer ist die zweistufige Verifizierung deaktiviert. Wenn Sie Eigentümer:in Ihres WhatsApp Business-Kontos sind, können Sie die zweistufige Verifizierung für die Nummer im WhatsApp Manager deaktivieren. Andernfalls müssen Sie Ihren Lösungsanbieter bitten, sie für Sie zu deaktivieren.

Informationen zur Migration Ihrer WhatsApp-Telefonnummer finden Sie in der Meta-Dokumentation unter [Telefonnummern zwischen WhatsApp Business-Konten über Embedded Signup migrieren](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/).

## Zwischen WhatsApp Business-Konten migrieren {#migrate-between-whatsapp-business-accounts}

1. Wählen Sie im WhatsApp Manager das WhatsApp Business-Konto (WABA) aus, das mit Ihrer Telefonnummer verknüpft ist, und navigieren Sie dann zu **Account tools** > **Phone numbers**.
2. Wählen Sie **Turn off two-step verification** aus und führen Sie die folgenden Schritte durch.<br><br>![WhatsApp Business Manager, geöffnet auf der Seite „Phone numbers“.]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> Wenn Sie eine Telefonnummer zu einer anderen WhatsApp Business-Gruppe migrieren und Metas Embedded Signup erfordert, dass der Anzeigename übereinstimmt, notieren Sie sich den bestehenden Anzeigenamen auf der Seite **Phone Numbers**. Sie geben diesen Namen im nächsten Schritt ein.<br><br>![Die Seite „Phone Numbers“ des WhatsApp Business Managers mit dem Anzeigenamen „Braze“ neben einer Telefonnummer.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Führen Sie den Embedded-Signup-Workflow von Meta bis zum Abschluss durch.

## Von einem anderen Business Solution Provider (BSP) migrieren {#migrate-from-another-business-solution-provider}

Wenn Ihre WhatsApp-Telefonnummer bei einem anderen BSP registriert ist, müssen Sie die Nummer zu einem mit Braze verbundenen WhatsApp Business-Konto migrieren, bevor Braze über diese Nummer senden kann.

### Vor der Migration {#before-you-migrate}

- Beachten Sie, dass eine Telefonnummer jeweils nur bei einem BSP aktiv sein kann. Durch die Migration wird der Versand auf Braze umgestellt; Ihr bisheriger BSP verliert den Zugriff auf die Nummer.
- Prüfen Sie Verträge und Abrechnungen mit Ihrem aktuellen Anbieter. Nachrichtenverläufe und Templates werden möglicherweise nicht automatisch übertragen.
- Deaktivieren Sie die zweistufige Verifizierung für die Nummer gemäß den Anforderungen von Meta.
- Wenn Sie separate Support- und Marketing-Nummern benötigen, lesen Sie [Integrationen, Daten und Reporting]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) in den WhatsApp-FAQ.

### Migrationspfade {#migration-paths}

| Aktuelle Konfiguration | Empfohlener Pfad |
|---|---|
| Nummer bei einem anderen BSP, vollständiger Wechsel zu Braze | Migration über [Embedded Signup]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup) in ein neues oder bestehendes Braze-WABA |
| Nummer auf nativer Braze-Integration, Wechsel zur Infobip-Abrechnung | [BYO WhatsApp-Konnektor]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector) (nur Infobip) |
| Marketing über Braze, Support über ein anderes WABA | Separate WABAs und Telefonnummern beibehalten; siehe die [WhatsApp-FAQ]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting) und [WhatsApp und externe Systeme]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Migrationspfade" }

## Entwicklungs- und Produktions-Workspaces {#development-and-production-workspaces}

Braze empfiehlt nach Möglichkeit separate WhatsApp Business-Konten für Entwicklung und Produktion:

- Binden Sie Ihre Produktions-Telefonnummer nicht an einen Sandbox- oder Entwicklungs-Workspace.
- Verwenden Sie ein dediziertes Test-WABA und eine Test-Telefonnummer für Integrationstests.
- Template-Genehmigungen gelten pro WABA; genehmigen Sie Templates in dem WABA, das mit dem Workspace verknüpft ist, über den Sie senden.