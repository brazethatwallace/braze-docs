---
nav_title: "Einrichtung"
article_title: "WhatsApp-Einrichtung"
alias: /partners/whatsapp/
description: "In diesem Artikel erfahren Sie, wie Sie den Braze WhatsApp-Kanal einrichten, einschließlich Voraussetzungen und empfohlener nächster Schritte."
page_type: partner
search_tag: Partner
page_order: 0
channel:
  - WhatsApp
search_rank: 2
---

# WhatsApp-Einrichtung {#whatsapp-setup}

> [WhatsApp](https://www.whatsapp.com/) Business Messaging ist eine weltweit beliebte Peer-to-Peer-Messaging-Plattform, die Unternehmen konversationsbasiertes Messaging bietet.

## Voraussetzungen {#prerequisites}

Bitte beachten Sie Folgendes, bevor Sie mit der Integration fortfahren:

- **Opt-in-Richtlinie:** WhatsApp verlangt, dass Unternehmen die Zustimmung der Kund:innen zum Empfang von Nachrichten einholen.
- **WhatsApp-Inhaltsregeln:** WhatsApp hat mehrere [Inhaltsregeln](https://www.whatsapp.com/legal/commerce-policy?l=en), die eingehalten werden müssen.
- **Compliance:** Halten Sie alle geltenden Braze- und Meta-Dokumentationen sowie alle anwendbaren [Meta-Richtlinien](https://www.whatsapp.com/legal/?lang=en) ein.
- **24-Stunden-Konversationslimits:** Nachdem ein Unternehmen eine erste Template-Nachricht gesendet hat oder eine Nutzerin bzw. ein Nutzer eine Nachricht sendet, öffnet sich ein 24-Stunden-Fenster, in dem beide Parteien hin und her kommunizieren können.
- **Konversation starten:** Nutzer:innen können jederzeit eine Konversation starten. Ein Unternehmen kann eine Konversation nur über ein genehmigtes Nachrichtentemplate starten.
<br><br>

| Voraussetzung | Beschreibung |
| --- | --- |
| Meta Business Manager:in-Konto | Ein Meta Business-Konto ist erforderlich, um diesen Messaging-Kanal zu nutzen. |
| WhatsApp Business-Konto | Ein WhatsApp Business-Konto ist erforderlich, um diesen Messaging-Kanal zu nutzen. |
| WhatsApp-Telefonnummer | Sie müssen eine Telefonnummer erwerben, die den WhatsApp-Anforderungen für die [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) oder die [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) entspricht, um den Messaging-Kanal nutzen zu können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration {#integration}

### Schritt 1: WhatsApp Messenger mit Braze verbinden {#step-1-connect-whatsapp-messenger-to-braze}

Gehen Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie nach **WhatsApp**.

Wählen Sie auf der WhatsApp-Partnerseite **Begin Integration** aus.

![WhatsApp-Partnerseite mit einem Button zum Starten der Integration.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

Wählen Sie im geöffneten Fenster **Next** aus, bis der Button **Begin Integration** erscheint. Wählen Sie den Button aus, um den Integrationsprozess zu starten.

![Anleitung zum Verbinden von Braze mit WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Schritt 2: WhatsApp-Einrichtung {#step-2-whatsapp-setup}

Als Nächstes werden Sie durch den Braze-Einrichtungs-Workflow geführt. Eine schrittweise Anleitung finden Sie unter [Eingebettete WhatsApp-Anmeldung]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup).

In diesem Ablauf werden Sie:
1. Ihre Meta- und WhatsApp-Geschäftskonten erstellen oder auswählen. Stellen Sie sicher, dass Sie die [Richtlinien für den WhatsApp-Anzeigenamen](https://www.facebook.com/business/help/757569725593362) überprüfen. <br><br>Es ist wahrscheinlich, dass in Ihrem Unternehmen bereits mindestens ein Meta-Geschäftskonto vorhanden ist. Wenn das der Fall ist, wählen Sie dasjenige aus, in dem Ihr WhatsApp-Geschäftskonto angesiedelt sein soll. Nutzerberechtigungen und die Geschäftsverifizierung für WhatsApp werden zentral in Ihrem Meta-Geschäftskonto verwaltet.<br><br>
2. Ihr WhatsApp-Geschäftsprofil erstellen.
3. Ihre WhatsApp-Geschäftsnummer verifizieren.<br><br>

Nach Abschluss der Einrichtung wird eine eigene [WhatsApp-Abo-Gruppe]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#whatsapp-subscription-groups) für Ihre Nutzer:innen erstellt.

### Schritt 3: WhatsApp-Templates erstellen {#step-3-create-whatsapp-templates}

Nur genehmigte WhatsApp-Nachrichtentemplates können verwendet werden, um Gespräche mit Kund:innen zu initiieren. WhatsApp-Templates können im [Meta Business Manager:in](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343) erstellt werden. Eine Liste der von Braze unterstützten WhatsApp-Messaging-Features finden Sie unter [Unterstützte WhatsApp-Features]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#supported-whatsapp-features).

1. **Navigieren Sie zum [Template-Manager:in](https://business.facebook.com/wa/manage/message-templates)**<br>
Wählen Sie im Meta Business Manager:in unter **Account Tools** die Option **Message Templates** aus.
Wählen Sie anschließend **Create Templates** aus.<br><br>![WhatsApp-Manager mit einer Liste von Nachrichtentemplates.]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Nachrichteneinstellungen**<br>
Wählen Sie im neuen Nachrichtentemplate-Composer die Kategorie Ihrer Nachricht aus, benennen Sie Ihr Template und wählen Sie die Sprachen aus, die Sie unterstützen möchten. Sie können Sprachen später löschen oder hinzufügen.<br><br>
	Die verfügbaren Nachrichtentemplate-Kategorien umfassen Folgendes:
	- Marketing: Senden Sie Werbeangebote, Produktankündigungen und mehr, um die Bekanntheit und das Engagement zu steigern
	- Utility: Senden Sie Konto-Updates, Bestellaktualisierungen, Benachrichtigungen und mehr, um wichtige Informationen zu teilen
	- Authentifizierung: Senden Sie Codes, mit denen Ihre Kund:innen auf ihre Konten zugreifen können<br><br>
	![Nachrichtentemplate-Composer mit Kategorien für Marketing, Utility und Authentifizierung.]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Template bearbeiten**<br>
Erstellen Sie als Nächstes Ihr Nachrichtentemplate. <br><br>Sie können eine Text- oder Medien-Kopfzeile, den Textkörper, eine Fußzeile und Buttons bereitstellen. Beachten Sie, dass Video- und Dokument-Header derzeit nicht verfügbar sind und Header entweder vom Typ Text oder Bild sein müssen. Alle Medien, die Sie hinzufügen, dienen als Beispiel für den Überprüfungsprozess und sind **nicht** in der Template-Nachricht enthalten. Medien müssen in Braze hinzugefügt werden. Eine Vorschau Ihrer Nachricht wird in einem Panel angezeigt. <br><br>Meta unterstützt zwar kein Liquid, Sie können jedoch Variablen einsetzen, die später in Braze durch Liquid-Variablen ersetzt werden können. Wählen Sie dazu den Button **+ Add variable** aus.<br><br>![Template-Composer.]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

Wenn Sie Ihr Template fertiggestellt haben, klicken Sie auf **Submit**.

#### Genehmigungszeit für Templates {#template-approval-time}

Sie können den Genehmigungsstatus Ihres Nachrichtentemplates entweder auf der Seite **Message Template** im Meta Business Manager:in oder beim Erstellen einer Campaign oder eines Canvas in Braze überprüfen. Zusätzlich können Sie je nach Ihren Benachrichtigungseinstellungen per E-Mail vom WhatsApp-Team benachrichtigt werden.

{% alert note %}
Genehmigte Templates können in beliebig vielen Campaigns und Canvase verwendet werden. Sie können auch an beliebig viele Nutzer:innen mit Opt-in gesendet werden. Dies gilt, solange die Qualität des Templates nicht abnimmt.
{% endalert %}

### Schritt 4: Eine WhatsApp-Campaign erstellen {#step-4-create-a-whatsapp-campaign}

Sobald WhatsApp-Templates genehmigt sind, können Sie zum Dashboard wechseln, um eine [WhatsApp-Campaign oder ein Canvas]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) zu erstellen.

{% alert note %}
Nachdem Ihr WhatsApp-Geschäftskonto erstellt wurde, legt Meta Ihr anfängliches Nachrichtenlimit fest. Weitere Informationen finden Sie unter [Durchsatz]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/10dlc#throughput).
{% endalert %}

## Nächste Schritte {#next-steps}

Nach Abschluss der Integration empfehlen wir, die folgenden beiden Meta-Prozesse durchzuführen:
- [Unternehmensverifizierung](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Möglicherweise haben Sie bereits eine Unternehmensverifizierung, wenn Sie einen bestehenden Meta Business Manager:in verwendet haben.
- [Offizielles Geschäftskonto](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

Wir empfehlen außerdem, sich über [Telefonnummern von Nutzer:innen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/user_phone_numbers) zu informieren und alle Nutzer:innen hinzuzufügen, die Zugriff zum Erstellen von Nachrichten-[Templates in Ihrer Organisation](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143) benötigen.

### WhatsApp Cloud API Local Storage {#whatsapp-cloud-api-local-storage}

Braze unterstützt die [Cloud API Local Storage](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) von WhatsApp. Um diese Funktion aktivieren zu lassen, wenden Sie sich an Ihre:n Braze-Kundenbetreuer:in.