---
nav_title: Eingebettete Anmeldung
article_title: WhatsApp – Eingebettete Anmeldung
page_order: 1
description: "Dieser Referenzartikel beschreibt, wie Sie auf den Workflow der eingebetteten WhatsApp-Anmeldung in Braze zugreifen, was Sie vor der Meta-Anmeldung vorbereiten sollten und was nach Abschluss der Anmeldung geschieht."
page_type: reference
channel:
  - WhatsApp
---

# Eingebettete WhatsApp-Anmeldung {#whatsapp-embedded-signup}

> Verwenden Sie die eingebettete Anmeldung, um Braze über den von Meta gehosteten Anmeldeablauf mit einem WhatsApp Business-Konto (WABA) zu verbinden.

Der Workflow für die eingebettete WhatsApp-Anmeldung wird aufgerufen, wenn Sie WhatsApp zum ersten Mal in Ihren Braze-Workspace [integrieren]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) und wenn Sie ein [WhatsApp Business-Konto oder eine Telefonnummer]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) zu einer bestehenden Integration hinzufügen.

{% alert note %}
Sie können [mehrere WhatsApp Business-Konten]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/multiple_business_accounts) zu einem Braze-Workspace hinzufügen. Jedes einzelne WhatsApp Business-Konto kann jedoch nur einem einzigen Braze-Workspace hinzugefügt werden.
{% endalert %}

## Zugriff auf den Workflow {#accessing-the-workflow}

1. Gehen Sie zu **Partnerintegrationen** > **Technologie-Partner**.
2. Suchen Sie nach **WhatsApp** und wählen Sie den Eintrag aus.
3. Wählen Sie die Option aus, die zu Ihrem Anwendungsfall passt:
   - **Erstmalige Integration:** Wählen Sie **Begin Integration** aus.
   - **Zusätzliches Konto oder zusätzliche Nummer:** Wählen Sie auf der Seite **WhatsApp Messaging Integration** die Option **Add account or number** oder **Add WhatsApp Business Account** aus.

Der Meta-Embedded-Signup-Flow ist identisch, unabhängig davon, von welchem Einstiegspunkt aus Sie ihn starten. Ihr Workspace zeigt möglicherweise auch Integrations-Tabs an, z. B. **Native Integration** oder **BYO Connector - Infobip**, je nach Ihrer Konfiguration. Wählen Sie den Tab aus, der zu Ihrem Setup passt, bevor Sie beginnen.

## Anmeldung vorbereiten {#prepare-for-signup}

Wenn Sie **Begin Integration** auswählen, öffnet Braze ein Onboarding-Fenster. Sehen Sie sich jede Folie an und wählen Sie dann erneut **Begin Integration** aus, um die eingebettete Meta-Anmeldung zu starten.

Bereiten Sie vor dem Start Folgendes vor:

- **Zugang zum Meta Business Manager:in:** Die meisten Unternehmen verwenden den Meta Business Manager:in, um Facebook-Seiten, Anzeigen und zugehörige Geschäftsressourcen zu verwalten. Wenn Sie keinen Zugang haben, bitten Sie eine:n Administrator:in, Berechtigungen zu erteilen, oder erstellen Sie während der Anmeldung ein Business-Manager:in-Konto.
- **Telefonnummer:** Verwenden Sie eine Nummer, die [Metas Anforderungen an WhatsApp-Telefonnummern](https://developers.facebook.com/docs/whatsapp/phone-numbers) erfüllt. Während der Anmeldung erhalten Sie einen einmaligen Verifizierungscode per SMS oder Telefonanruf.

{% alert important %}
Sie durchlaufen die erstmalige eingebettete Anmeldung nur einmal pro Integrationspfad. Geben Sie Ihre Geschäftsdaten daher so genau wie möglich ein.
{% endalert %}

## Workflow für die eingebettete WhatsApp-Anmeldung {#whatsapp-embedded-signup-workflow}

Nachdem Braze die eingebettete Meta-Anmeldung gestartet hat, melden Sie sich mit einem Meta-Konto an, das Zugriff auf den Business Manager:in Ihres Unternehmens hat. Meta hostet die Anmeldebildschirme; Braze hat keinen Einfluss auf deren Layout oder Beschriftungen.

{% alert note %}
Meta kann die eingebetteten Anmeldebildschirme ohne Vorankündigung ändern. Wenn der Workflow von diesem Artikel abweicht, folgen Sie den Aufforderungen von Meta und lesen Sie die [Dokumentation zur eingebetteten Anmeldung von Meta](https://developers.facebook.com/docs/whatsapp/embedded-signup/embed-the-flow).
{% endalert %}

Im Allgemeinen führt Meta Sie durch folgende Schritte:

1. **Anmelden und Berechtigungen erteilen.** Authentifizieren Sie sich bei Meta und erlauben Sie Braze, eine Verbindung zu Ihrem WhatsApp Business-Konto herzustellen.
2. **Ihr Unternehmensportfolio auswählen.** Verbinden Sie das Business-Manager:in-Portfolio, das Eigentümer des WhatsApp Business-Kontos sein soll. Wenn Sie das erwartete Portfolio nicht sehen, überprüfen Sie Ihre Meta-Berechtigungen.
3. **Ein WhatsApp Business-Konto verbinden oder erstellen.** Erstellen Sie ein neues Konto oder wählen Sie ein unbenutztes Konto aus, wenn Sie dazu aufgefordert werden. Wählen Sie kein WhatsApp Business-Konto aus, das aktiv mit einem anderen Messaging-Anbieter verbunden ist – diese Verbindung wird in Braze nicht funktionieren. Um [eine Nummer von einem anderen Anbieter zu migrieren]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number), kontaktieren Sie Ihr Braze-Konto-Team, bevor Sie beginnen.
4. **Geschäfts- und Anzeigedetails angeben.** Geben Sie den Kontonamen, den Anzeigenamen und die Kategorie ein, die Meta für Ihr WhatsApp Business-Konto anfordert.
5. **Ihre Telefonnummer verifizieren.** Fügen Sie die Nummer hinzu, die Sie für WhatsApp-Messaging verwenden möchten, und schließen Sie die Verifizierung per SMS oder Telefonanruf ab.

Wenn Meta die eingebettete Anmeldung abgeschlossen hat, wird die Steuerung an Braze zurückgegeben.

## Die Braze-Integration abschließen {#complete-the-braze-integration}

Nach der eingebetteten Registrierung führt Braze die Einrichtungsschritte automatisch durch. Auf der Seite **WhatsApp Messaging Integration** werden möglicherweise Fortschrittsmeldungen wie **Registrierung flow completed, integration with WhatsApp in progress** angezeigt, während Braze Folgendes ausführt:

- Ruft Ihre WhatsApp Business-Konto-ID und Telefonnummern von Meta ab
- Fügt die Braze-Systemnutzer:in zu Ihrem WhatsApp Business-Konto hinzu
- Registriert Telefonnummern und abonniert Webhook-Ereignisse
- Erstellt eine Braze-[Abo-Gruppe]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups) für jede verbundene Nummer

Warten Sie, bis die Integration abgeschlossen ist, bevor Sie Nachrichten senden. Falls die Einrichtung fehlschlägt, überprüfen Sie den Fehler auf der Integrationsseite und lesen Sie [WhatsApp-Einrichtung]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) für allgemeine Hinweise.

## Nächste Schritte {#next-steps}

- [Eine WhatsApp-Telefonnummer erwerben oder migrieren]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers)
- [Eine WhatsApp-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)
- [Abo-Gruppen verwalten]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)