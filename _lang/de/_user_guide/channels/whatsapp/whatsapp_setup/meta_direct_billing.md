---
nav_title: Meta Direct Billing
article_title: Meta Direct Billing
page_order: 7
description: "Dieser Referenzartikel beschreibt, wie Sie Meta Direct Billing einrichten, damit Sie WhatsApp-Messaging-Kosten mit Ihrer eigenen Debit- oder Kreditkarte bezahlen, anstatt über eine Braze- oder Partner-Kreditlinie."
page_type: reference
channel:
  - WhatsApp
alias: /whatsapp_meta_direct_billing/
hidden: true
noindex: true
---

# Meta Direct Billing {#meta-direct-billing}

> Mit Meta Direct Billing bezahlen Sie WhatsApp-Messaging-Kosten direkt mit Ihrer eigenen Debit- oder Kreditkarte, anstatt über eine Braze- oder Partner-Kreditlinie abzurechnen.

## Voraussetzungen {#prerequisites}

Bevor Sie Meta Direct Billing einrichten, stellen Sie sicher, dass Folgendes vorhanden ist:

| Voraussetzung | Beschreibung |
| --- | --- |
| Zugang zum Braze-Workspace | Sie benötigen Zugang zu **Partnerintegrationen** > **Technologie-Partner** in Braze, um den eingebetteten Registrierungsablauf zu starten. |
| Meta Business Manager-Konto | Die Abrechnung wird im Meta Business Manager unter **Billing & payments** konfiguriert. |
| Debit- oder Kreditkarte | Eine gültige Karte ist erforderlich, um die Einrichtung abzuschließen. Die monatliche Rechnungsstellung kann bei einigen Konten als Option angezeigt werden, ist aber nicht garantiert. |
| Vollständige Geschäftsinformationen | Ihr Firmenname, Ihre Adresse und Ihre Währung müssen ausgefüllt und korrekt sein. Meta überprüft diese Angaben, bevor das Messaging aktiviert wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Einrichtung {#setup}

### Schritt 1: Meta Direct Billing auswählen {#step-1-select-meta-direct-billing}

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner**, suchen Sie nach **WhatsApp** und öffnen Sie die Seite **WhatsApp Messaging Integration**.
2. Wählen Sie den Tab **Meta Direct Billing** aus. Das bedeutet, dass Ihre Abrechnungsbeziehung direkt mit Meta besteht und nicht über Braze oder eine Infobip-Abrechnungslinie. Daher ist es wichtig, diesen Tab auszuwählen, bevor Sie fortfahren, anstatt dies später ändern zu wollen.
3. Wählen Sie unter **Add a WhatsApp Business Account or phone number** die Option **Add account or number** aus. Dadurch wird Metas eingebettete Registrierung gestartet, bei der Sie sich bei Meta anmelden, Ihr Geschäftsportfolio auswählen, Ihr WhatsApp Business Account (WABA) erstellen oder auswählen und Ihre Telefonnummer verifizieren.

### Schritt 2: Billing & payments aufrufen {#step-2-go-to-billing-payments}

Nachdem Sie Metas eingebettete Registrierung abgeschlossen haben, führen Sie einen der folgenden Schritte aus:

- Wählen Sie **Add payment method** aus, um zum Meta Business Manager weitergeleitet zu werden.
- Gehen Sie im Meta Business Manager zu **Billing & payments** > **Accounts** und wählen Sie Ihr WABA aus.

### Schritt 3: Zahlungsmethode hinzufügen {#step-3-add-a-payment-method}

1. Wählen Sie **Add payment method** aus.
2. Bestätigen Sie im sich öffnenden Fenster den Eintrag **Business location and currency** (zum Beispiel **Canada, US Dollars USD**), der die Währung bestimmt, in der Sie abgerechnet werden. Wählen Sie **Edit** aus, falls dies geändert werden muss.
3. Unter **Select payment method** werden möglicherweise vorhandene Kreditlinien angezeigt. Diese stehen Ihnen nicht zur Verfügung; wählen Sie sie nicht aus. Weitere Informationen finden Sie unter [Einschränkungen bei Abrechnungslinien](#billing-line-restrictions).

![Das Fenster „Select payment method“ mit ausgewählter Debit- oder Kreditkarte und nicht ausgewählten vorhandenen Infobip- und Braze-Kreditlinien.]({% image_buster /assets/img/whatsapp/payment_methods.png %}){: style="max-width:40%;"}

{: start="4"}
4. Wählen Sie unter **Add payment method** die Option **Debit or credit card** aus und klicken Sie dann auf **Next**.
5. Geben Sie Ihre Kartendaten ein und wählen Sie dann **Save** aus.
6. Ihre Karte wird unter **Payment methods** mit der Kennzeichnung **Default** angezeigt, zusammen mit der maskierten Kartennummer und dem Ablaufdatum.

{% alert note %}
Das Schließen des Einrichtungsfensters nach dem Hinzufügen Ihrer Zahlungsmethode trennt Ihre Telefonnummer nicht. Die verknüpfte Nummer bleibt erhalten.
{% endalert %}

### Schritt 4: Geschäftsinformationen bestätigen {#step-4-confirm-your-business-information}

Meta überprüft Ihren Firmennamen, Ihre Adresse und Ihre Währung, bevor das Messaging aktiviert wird. Unvollständige oder ungenaue Geschäftsinformationen können dazu führen, dass Nachrichten fehlschlagen oder ein Fehler wegen ungültiger Geschäftsinformationen auftritt.

## Einschränkungen bei Abrechnungslinien {#billing-line-restrictions}

Kreditlinien, die in der Liste der Zahlungsmethoden angezeigt werden (zum Beispiel „Infobip Limited“ oder „BRAZE INC.“), gehören dem jeweiligen Unternehmen und nicht Ihnen. Sie werden aufgrund der Verbindung Ihres Kontos angezeigt, können aber nicht ausgewählt werden.

## Meta-Ressourcen {#meta-resources}

- [Meta Business Help Center: Billing and payments](https://business.facebook.com/business/help/535561817791563)
- [Meta Business Help Center: Adding a payment method](https://www.facebook.com/business/help/832746984379005)