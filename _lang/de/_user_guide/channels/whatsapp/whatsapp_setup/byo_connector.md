---
nav_title: BYO-WhatsApp-Konnektor
article_title: Bring Your Own WhatsApp-Konnektor
page_order: 2
description: "Dieser Referenzartikel bietet eine schrittweise Anleitung zur Einrichtung eines Bring Your Own WhatsApp-Konnektors, der Braze Zugriff auf Ihren Infobip WhatsApp Business Manager gewährt."
page_type: reference
channel:
  - WhatsApp
---

# Bring Your Own WhatsApp-Konnektor {#bring-your-own-whatsapp-connector}

> Der Bring Your Own (BYO) WhatsApp-Konnektor bietet eine Partnerschaft zwischen Braze und Infobip, bei der Sie Braze Zugriff auf Ihren Infobip WhatsApp Business Manager (WABA) gewähren. So können Sie Messaging-Kosten direkt mit Infobip verwalten und bezahlen, während Sie Braze für Segmentierung, Personalisierung und Campaign-Orchestrierung nutzen. Braze behält alle bestehenden Funktionen bei, die der WhatsApp-Kanal bietet, wie ausgehende Nachrichten, Verarbeitung eingehender Nachrichten, WhatsApp-Flows und Analytics.

{% alert note %}
Informationen zur Migration von anderen Business Solution Providers (BSPs) zur Braze-Integration finden Sie unter [Von einem anderen Business Solution Provider migrieren]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-from-another-business-solution-provider).
{% endalert %}

## Anforderungen {#requirements}

| Anforderung | Beschreibung |
| --- | --- |
| Infobip-Konto | Für die Nutzung des BYO-WhatsApp-Konnektors ist ein Infobip-Konto erforderlich. |
| Nachrichten- oder Action-Credits | Beim Versand von WhatsApp-Nachrichten werden Braze Action-Credits verbraucht. |
| WhatsApp-Anforderungen | Erfüllen Sie alle [WhatsApp-Anforderungen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#prerequisites). |
| Telefonnummer | Wir empfehlen, der Einfachheit halber [eine Telefonnummer über Infobip zu erwerben](https://www.infobip.com/docs/numbers/getting-started). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen" }

## Einrichtung {#set-up}

Bevor Sie den BYO-WhatsApp-Konnektor einrichten, stellen Sie sicher, dass der Versand über Ihr WhatsApp Business-Konto zuvor nicht über Infobip erfolgt ist.

### Unterstützte Fälle {#supported-cases}

- WhatsApp Business-Konto und Telefonnummer waren noch nie mit einem Partner verbunden
- WhatsApp Business-Konto ist über die native Integration direkt mit Braze verbunden.
    - Folgen Sie den Schritten unter [Zwischen WhatsApp Business-Konten migrieren]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-between-whatsapp-business-accounts), um Ihre Telefonnummern jeweils einzeln zu einem neuen WhatsApp Business-Konto zu migrieren.
- WhatsApp Business-Konto ist mit einem anderen Lösungsanbieter als Braze und Infobip verbunden
    - Folgen Sie den Schritten unter [Zwischen WhatsApp Business-Konten migrieren]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number#migrate-between-whatsapp-business-accounts), um Ihre Telefonnummern jeweils einzeln zu einem neuen WhatsApp Business-Konto zu migrieren.

## 1. Schritt: Infobip-Kontoinformationen abrufen {#step-1}

1. Identifizieren Sie in Infobip das Konto, das Sie mit Ihrem WhatsApp Business-Konto verwenden möchten.
2. Gehen Sie zu **Developer Tools** > **API Keys** und wählen Sie **Create API Key**.

![Seite „Create API key“ mit einem Erstellungsdatum „16/12/2025“ und einem Ablaufdatum „16/12/36“.]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3. Geben Sie dem Schlüssel einen aussagekräftigen Namen, z. B. „Braze - Mein Workspace-Name - Mein WABA-Name“.
4. Legen Sie ein Ablaufdatum fest, das weit in der Zukunft liegt, um Probleme mit dem Token-Ablauf zu vermeiden.
    - Notieren Sie sich, vor dem Ablaufdatum einen neuen API-Schlüssel zu generieren und Ihr WABA erneut zu verbinden.
5. Wählen Sie diese Berechtigungen aus:
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. Kopieren Sie nach dem Erstellen des Schlüssels den API-Schlüssel.
    - Der Schlüssel kann nur für eine begrenzte Zeit nach der Erstellung kopiert werden. Sie können diese Schritte wiederholen, um einen neuen Schlüssel zu erstellen, falls Sie in Zukunft ein weiteres WhatsApp Business-Konto verbinden müssen.

![„Braze Example API Key“ mit 6 hinzugefügten Berechtigungen.]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7. Kopieren Sie die API-Basis-URL des Kontos.

![Seite „API keys“ mit einer hervorgehobenen API-Basis-URL.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## Schritt 2: Die eingebettete Anmeldung starten {#step-2-start-the-embedded-signup}

1. Gehen Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** > **WhatsApp**.
2. Wählen Sie den Tab **BYO Connector - Infobip** aus.

![Die WhatsApp-Technologie-Partnerseite.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3. Geben Sie den API-Schlüssel und die Basis-URL aus [Schritt 1](#step-1) ein.
4. Wählen Sie **Connect** aus.
5. Fahren Sie mit dem [Workflow für die eingebettete Anmeldung]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup#whatsapp-embedded-signup-workflow) fort und beachten Sie dabei Folgendes:
- Sie können nicht dasselbe Geschäftsportfolio auswählen, das von einem anderen Business Solution Provider verwendet wird.
- Sie können keine Telefonnummer auswählen, die von einem anderen Business Solution Provider verwendet wird.
- Sie müssen ein neues WABA erstellen und kein bestehendes auswählen.

{% alert note %}
Um den Verifizierungscode zu erhalten, gehen Sie zu Ihrem Infobip-Dashboard > **Analyze** > **Logs** und entnehmen Sie den Code aus der eingehenden SMS-Nachricht.
{% endalert %}

![Nachrichtenprotokolle mit einer eingehenden SMS-Nachricht, die den Verifizierungscode enthält.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

Nach Abschluss der Einrichtung wird Ihre Telefonnummer als Abo-Gruppe unter Ihrer WhatsApp Business Group aufgeführt. Die WhatsApp Business Group enthält den Infobip-Kontonamen und die API-Basis-URL, mit der sie verbunden ist. Konten, die über die native Integration verbunden sind, haben keinen Infobip-Kontonamen.

{% alert note %}
Verbinden Sie jedes WhatsApp Business-Konto mit einem einzelnen Infobip-Konto. Jedes Mal, wenn Sie eine zusätzliche Telefonnummer oder Abo-Gruppe verbinden und das WhatsApp Business-Konto bereits mit einem Infobip-Konto verbunden ist, müssen Sie die API-Zugangsdaten für das bestehende Konto erneut eingeben.
{% endalert %}

## Schritt 3: Nachrichten senden {#step-3-sending-messages}

Folgen Sie dem nativen Integrations-Sendeprozess, einschließlich:
- [Nutzer:innen für die Abo-Gruppe anmelden]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
- [Eine WhatsApp-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)

## Fehlerbehebung bei der Einrichtung {#troubleshooting-setup}

### WhatsApp Business Account ID konnte nicht abgerufen werden {#couldnt-retrieve-whatsapp-business-account-id}

Stellen Sie sicher, dass Ihr WhatsApp Business Account nicht mit einem anderen Braze Workspace verbunden ist.

### WhatsApp Business Account ID konnte nicht mit Infobip geteilt werden {#couldnt-share-whatsapp-business-account-id-with-infobip}

1. Stellen Sie sicher, dass Ihr WhatsApp Business Account nicht mit Braze oder einem anderen Partner verbunden ist.
2. Stellen Sie sicher, dass keine Telefonnummern in Ihrem WhatsApp Business Account mit einem anderen Infobip-Konto verbunden sind. Bei importierten Nummern können Sie die Nummer in Infobip finden und **Cancel number** auswählen.

## Überlegungen {#considerations}

Obwohl alle bestehenden Funktionen mit Braze unterstützt werden, werden diese Anwendungsfälle derzeit nicht unterstützt.

| Anwendungsfall | Grund |
| --- | --- |
| Verarbeitung eingehender Nachrichten in Braze und Infobip | Dies verhindert Logikketten, die von einem der beiden Systeme getriggert werden und dadurch doppelte und möglicherweise widersprüchliche Nachrichtenverläufe erzeugen. |
| Senden von Nachrichten über Braze und Infobip | Für WhatsApp Business Accounts, die mit Braze verbunden sind, erfolgt der gesamte Versand über Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Überlegungen" }