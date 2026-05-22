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

## Ihre WhatsApp-Telefonnummer migrieren {#migrating-your-whatsapp-phone-number}

1. Wählen Sie im WhatsApp Manager das WhatsApp Business-Konto (WABA) aus, das mit Ihrer Telefonnummer verknüpft ist, und navigieren Sie dann zu **Account tools** > **Phone numbers**.
2. Wählen Sie **Turn off two-step verification** aus und führen Sie die folgenden Schritte durch.<br><br>![WhatsApp Business Manager, geöffnet auf der Seite „Phone numbers“.]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> Wenn Sie eine Telefonnummer zu einer anderen WhatsApp Business-Gruppe migrieren und Metas Embedded Signup erfordert, dass der Anzeigename übereinstimmt, notieren Sie sich den bestehenden Anzeigenamen auf der Seite **Phone Numbers**. Sie geben diesen Namen im nächsten Schritt ein.<br><br>![Die Seite „Phone Numbers“ des WhatsApp Business Managers mit dem Anzeigenamen „Braze“ neben einer Telefonnummer.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Führen Sie den Embedded-Signup-Workflow von Meta bis zum Abschluss durch.