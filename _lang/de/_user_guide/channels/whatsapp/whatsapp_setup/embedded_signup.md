---
nav_title: Eingebettete Anmeldung
article_title: WhatsApp – Eingebettete Anmeldung
page_order: 1
description: "Dieser Referenzartikel bietet eine schrittweise Anleitung für den Workflow der eingebetteten WhatsApp-Anmeldung in Braze."
page_type: reference
channel:
  - WhatsApp
---

# Eingebettete WhatsApp-Anmeldung {#whatsapp-embedded-signup}

> Dieser Referenzartikel bietet eine schrittweise Anleitung für den Workflow der eingebetteten WhatsApp-Anmeldung in Braze.

Der Workflow für die eingebettete WhatsApp-Anmeldung wird aufgerufen, wenn Sie WhatsApp zum ersten Mal in Ihren Braze-Workspace [integrieren]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/) und wenn Sie ein [WhatsApp Business-Konto]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/) zu einer bestehenden WhatsApp-Integration hinzufügen.

{% alert note %}
Sie können [mehrere WhatsApp Business-Konten]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups/) zu einem Braze-Workspace hinzufügen. Jedes einzelne WhatsApp Business-Konto kann jedoch nur einem einzigen Braze-Workspace hinzugefügt werden.
{% endalert %}

## Zugriff auf den Workflow {#accessing-the-workflow}

Gehen Sie zu **Partnerintegrationen** > **Technologie-Partner** und suchen Sie nach **WhatsApp**. Ihre nächste Auswahl hängt von Ihrem Anwendungsfall ab:

- Wenn Sie WhatsApp in Ihren Workspace integrieren, wählen Sie **Begin Integration**. <br><br>![WhatsApp-Partnerseite mit einem Button zum Starten der Integration.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- Wenn Sie ein WhatsApp Business-Konto zu einer bestehenden WhatsApp-Integration hinzufügen, wählen Sie **Add WhatsApp Business Account**. <br><br>![„WhatsApp Messaging Integration“ mit Optionen zum Hinzufügen eines WhatsApp Business-Kontos oder einer Abo-Gruppe und Nummer.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}){: style="max-width:80%;"}

Der Workflow ist ab hier für beide Anwendungsfälle identisch.

## Workflow für die eingebettete WhatsApp-Anmeldung {#whatsapp-embedded-signup-workflow}

1. Wählen Sie im Meta-(Facebook-)Anmeldefenster **Login as** oder **Continue**. <br><br>![Meta-Anmeldefenster.]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Lesen Sie die Berechtigungen, die Sie mit Braze teilen, und wählen Sie dann **Get Started**. <br><br>![Liste der Berechtigungen, die Sie für die Integration mit Braze teilen.]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. Legen Sie auf diesem Bildschirm Folgendes fest und wählen Sie dann **Next**:
- Wählen Sie im Dropdown **Business portfolio** Ihr Unternehmensportfolio aus. Dies stellt die Verbindung zu Ihrem WhatsApp Business-Konto her. Wenn Ihr erwartetes Unternehmensportfolio nicht angezeigt wird, überprüfen Sie Ihre Berechtigungen.
- Wählen Sie im Feld **WhatsApp business account** die Option **Create a new WhatsApp Business Account** – auch dann, wenn Sie ein weiteres WhatsApp Business-Konto zu Ihrem Workspace hinzufügen oder wenn das Konto bereits in Meta existiert. Wählen Sie diese Option anstelle eines vorhandenen WhatsApp Business-Kontos aus dem Dropdown. <br><br>![Ein Fenster mit Feldern zur Eingabe Ihrer Unternehmensinformationen, einschließlich des Namens Ihres Unternehmensportfolios.]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. Wählen Sie für die Dropdown-Felder Folgendes aus und klicken Sie dann auf **Next**.
- **Choose a WhatsApp Business account**: Create a WhatsApp business account
- **Create or select a WhatsApp Business profile**: Create a new WhatsApp business profile <br><br>![Felder zur Angabe, ob Sie ein WhatsApp Business-Konto und -Profil auswählen oder erstellen.]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. Geben Sie Folgendes an und wählen Sie dann **Next**.
- Name des WhatsApp Business-Kontos
- Anzeigename des WhatsApp Business-Kontos
- Kategorie <br><br>![Felder zur Eingabe von Details für das neue WhatsApp Business-Konto.]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. Geben Sie Ihre Telefonnummer ein und wählen Sie entweder **Text message** oder **Phone call**. Bei einer neuen Nummer muss diese die Telefonnummernanforderungen von WhatsApp erfüllen, einschließlich der Bedingung, dass sie bei keinem anderen WhatsApp-Konto registriert sein darf. Wenn Sie eine bestehende Nummer migrieren (siehe Schritt 3) und Meta anzeigt, dass die Nummer bereits verwendet wird, fahren Sie trotz der Warnung fort, um die Migration abzuschließen. <br><br>![Felder zum Hinzufügen einer Telefonnummer.]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. Geben Sie Ihren Zwei-Faktor-Authentifizierungscode ein und wählen Sie dann **Next**. <br><br>![Ein Eingabefeld für einen Zwei-Faktor-Authentifizierungscode.]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. Überprüfen Sie die Berechtigungen, die Ihr WhatsApp Business-Konto erhalten wird, und wählen Sie dann **Continue**. <br><br>![Liste der vom WhatsApp Business-Konto angeforderten Berechtigungen.]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. Fertig! <br><br>![Fenster mit der Nachricht, dass Sie bereit sind, Personen Nachrichten zu senden.]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}