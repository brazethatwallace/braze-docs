---
nav_title: Interne Gruppen
article_title: Interne Gruppen
page_order: 4
page_type: reference
description: "Dieser Referenzartikel beschreibt interne Gruppen – eine hervorragende Möglichkeit, Einblicke in die SDK- oder API-Protokolle Ihres Testgeräts zu erhalten, wenn Sie die SDK-Integration testen."

---

# Interne Gruppen {#internal-groups}

> Interne Gruppen sind eine hervorragende Möglichkeit, interne oder externe Testgruppen zu erstellen und zu organisieren. Sie bieten Einblicke in Ihre SDK- oder API-Protokolle und sind nützlich beim Testen Ihrer SDK-Integration. Sie können eine unbegrenzte Anzahl angepasster interner Gruppen mit bis zu 1.000 Nutzer:innen erstellen.

{% alert tip %}
Wir empfehlen außerdem, unseren Braze-Lernkurs [Testen und Fehlerbehebung](https://learning.braze.com/path/developer/testing-and-troubleshooting) zu besuchen, der erklärt, wie Sie interne Gruppen für Ihre eigene Fehlerbehebung und Fehlersuche nutzen können.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um interne Gruppen zu erstellen und zu verwalten, benötigen Sie die folgenden [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions):

- API-Schlüssel anzeigen
- API-Schlüssel bearbeiten
- Interne Gruppen anzeigen
- Interne Gruppen bearbeiten
- Nachrichtenaktivitätsprotokoll anzeigen
- Event-Nutzerprotokoll anzeigen
- API-Bezeichner anzeigen
- API-Nutzungs-Dashboard anzeigen
- API-Limits anzeigen
- API-Nutzungswarnungen anzeigen
- API-Nutzungswarnungen bearbeiten
- SDK-Debugger bearbeiten
- SDK-Debugger anzeigen

## Erstellen einer internen Gruppe {#creating-an-internal-group}

So erstellen Sie eine interne Gruppe:

1. Gehen Sie zu **Einstellungen** > **Interne Gruppen**.
2. Wählen Sie **Interne Gruppe erstellen** aus.
3. Geben Sie Ihrer Gruppe einen Namen, z. B. „E-Mail-Testgruppe“.
4. Wählen Sie einen oder mehrere Gruppentypen aus, wie in der folgenden Tabelle aufgeführt.

| Gruppentyp | Beschreibung |
|--------------------|---------------------------------------------------------------------------------------------|
| **User-Event-Gruppe** | Verwenden Sie diese, um Ereignisse oder Protokolle von Ihrem Testgerät zu überprüfen.<br><br>Um SDK- und REST API-Protokolle für Gruppenmitglieder zu erfassen, aktivieren Sie das Kontrollkästchen **User Events**. Ohne diese Einstellung werden für Nutzer:innen, die der Gruppe hinzugefügt wurden, keine Protokolle im [Event-Nutzerprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) angezeigt. |
| **Content-Testgruppe** | Verwenden Sie diese für Push, E-Mail und In-App-Nachrichten, um eine gerenderte Kopie der Nachricht zu senden. |
| **Seed-Gruppe** | Sendet beim Versand automatisch eine Kopie der E-Mail an alle Mitglieder der Seed-Gruppe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erstellen einer internen Gruppe" }

{:start="5"}
5. Wählen Sie erneut **Interne Gruppe erstellen** aus.

### Testnutzer:innen hinzufügen {#adding-test-users}

Nachdem Sie Ihre interne Gruppe erstellt haben, fügen Sie Testnutzer:innen als Mitglieder dieser Gruppe hinzu.

1. Wählen Sie auf der Verwaltungsseite Ihrer internen Gruppe **Testnutzer:innen hinzufügen** aus.
2. Wählen Sie eine der folgenden Methoden zum Suchen und Auswählen Ihrer Testnutzer:innen.

| Methode | Beschreibung |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Identifizierte:n Nutzer:in hinzufügen** | Suchen Sie nach der/dem Nutzer:in anhand der externen ID, E-Mail-Adresse, Telefonnummer oder des Push-Tokens. |
| **Anonyme:n Nutzer:in hinzufügen** | Suchen Sie nach IP-Adresse. Geben Sie dann einen Namen für jede:n Testnutzer:in an, die/den Sie hinzufügen. Dies ist der Name, mit dem alle Ereignisprotokolle auf der Seite [Event-Nutzerprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) verknüpft werden. |
| **Nutzer:innen in großer Anzahl hinzufügen** | Kopieren Sie eine Liste von E-Mail-Adressen oder externen IDs und fügen Sie sie ein. Sie können nur Nutzer:innen hinzufügen, die bereits im Dashboard bekannt sind. Weitere Informationen finden Sie unter [Nutzerimport]({{site.baseurl}}/user_guide/audience/manage_audience/import_users). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Testnutzer:innen hinzufügen" }

### Content-Testgruppen {#content-test-groups}

Ähnlich wie beim Senden einer Vorschau-Testnachricht spart die Content-Testgruppe Zeit und ermöglicht es Ihnen, Tests gleichzeitig an eine vordefinierte Liste von Braze-Nutzer:innen zu senden. Dies ist für Push, In-App-Nachrichten, SMS, E-Mail und Content Cards in Braze verfügbar. Nur Gruppen, die als Content-Testgruppen gekennzeichnet sind, stehen im Vorschaubereich einer Nachricht zur Verfügung.

{% alert note %}
[SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)-Testnachrichten können nur an gültige Telefonnummern in der Datenbank gesendet werden.
{% endalert %}

Wählen Sie einzelne Braze-Nutzer:innen oder eine beliebige Anzahl interner Gruppen aus, an die die Nachricht gesendet werden soll. Wenn Ihre Nachricht Liquid oder andere dynamische Personalisierung enthält, verwendet Braze die für jede:n Nutzer:in verfügbaren Attribute, um den Nachrichteninhalt zu personalisieren. Für Nutzer:innen ohne Attribute verwendet Braze den festgelegten Standardwert.

Wenn Sie die Nachricht als zufällige:r Nutzer:in, angepasste:r Nutzer:in oder bestehende:r Nutzer:in in der Vorschau anzeigen, können Sie stattdessen diese Vorschauversion senden. Durch Deaktivieren des Kontrollkästchens wird die Nachricht basierend auf den Attributen der einzelnen Nutzer:innen gesendet, anstatt die Vorschauversion zu verwenden.

Wenn Sie einen IP-Pool zum Versenden einer E-Mail verwenden, wählen Sie den IP-Pool aus, von dem die E-Mail gesendet werden soll, indem Sie den Pool aus dem verfügbaren Dropdown-Menü auswählen.

![Der Testbereich des In-App-Nachrichten-Editors zur Auswahl der Content-Testgruppe.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Seed-Gruppen {#seed-groups}

Seed-Gruppen werden nur für den E-Mail-Kanal unterstützt. Fügen Sie Nutzer:innen zu einer Seed-Gruppe hinzu, um Kopien jeder E-Mail-Variante an alle Mitglieder der Gruppe zu senden.

Seed-Gruppen sind für API-Campaigns nicht verfügbar, aber Sie können Seed-Gruppen über einen API-getriggerten Einstieg in die Campaign einbinden. Verwenden Sie dies, um Zustellbarkeitsmetriken zu messen und eine Aufzeichnung Ihrer E-Mail-Inhalte für historische und Archivierungszwecke zu führen.

Nachdem Sie eine interne Gruppe erstellt und als Seed-Gruppe gekennzeichnet haben, wählen Sie sie im Schritt **Zielgruppen** des Campaign-Editors oder im Schritt **Sendeeinstellungen** in einem Canvas aus.

Seed-E-Mails haben `[SEED]` vor der Betreffzeile. Beachten Sie, dass Seed-E-Mails **nicht**:

- Die Sendezähler in den Dashboard-Analytics erhöhen.
- E-Mail-Analytics oder Retargeting beeinflussen.
- Die Liste **Campaign erhalten** eines Nutzerprofils aktualisieren.
- Frequency-Capping beeinflussen.
- Die Rate-Limits für die Zustellgeschwindigkeit berücksichtigen oder beeinflussen.

#### Abo-Verhalten {#subscription-behavior}

Seed-Sendungen sind für interne Qualitätssicherung und Überprüfung konzipiert und umgehen daher absichtlich Abo-Prüfungen für die geseedeten Unternehmensnutzer:innen. Das bedeutet, dass Nutzer:innen mit gültigen E-Mail-Adressen, die Teil einer Seed-Gruppe sind, die Nachricht erhalten, auch wenn sie kein Abo haben. Die Nachricht muss jedoch so konfiguriert sein, dass Seed-Kopien an diese Gruppe gesendet werden.

{% alert tip %}
Wenn Seed-Gruppen-Mitglieder die Nachricht nicht sehen, bestätigen Sie, dass sie in der internen Gruppe sind, verwenden Sie unterschiedliche Betreffzeilen, damit Gmail Nachrichten nicht zusammenfasst, und bitten Sie sie, den Spam-Ordner zu überprüfen.

Wenn die E-Mail [`abort_message()` Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) verwendet, müssen Seed-Gruppen-Mitglieder weiterhin die Abbruchbedingung erfüllen, um die Sendung zu erhalten.
{% endalert %}

#### Für Campaigns {#for-campaigns}

Beim Erstellen einer E-Mail-Campaign bearbeiten Sie Ihre Seed-Gruppen im Abschnitt **Zielgruppen** des Editors.

{% alert important %}
Wenn Sie eine Seed-Gruppe so konfigurieren, dass sie automatisch an alle Campaigns angehängt wird, gilt dies nur für neue Campaigns. Es gilt nicht, wenn Sie bestehende Campaigns kopieren. Sie müssen Ihre gewünschten Seed-Gruppen manuell auf die kopierte Campaign im Abschnitt **Zielgruppen** anwenden.
{% endalert %}

Seed-Gruppen senden an jede E-Mail-Variante einmal und werden beim ersten Mal zugestellt, wenn Ihre Nutzer:innen diese bestimmte Variante erhalten. Bei geplanten Nachrichten ist dies in der Regel der erste Start der Campaign. Bei aktionsbasierten oder API-getriggerten Campaigns ist dies der Zeitpunkt, zu dem die erste Nachricht an eine:n Nutzer:in gesendet wird.

Wenn Ihre Campaign multivariat ist und Ihre Variante einen Sendeprozentsatz von 0 % hat, wird sie nicht an Seed-Gruppen gesendet. Wenn die Variante bereits gesendet wurde und nicht unter **Seed-Gruppen bearbeiten** im Schritt **Zielgruppe** zum erneuten Senden aktualisiert wurde, wird sie standardmäßig nicht erneut gesendet.

{% alert note %}
Wenn Sie eine wiederkehrende Campaign haben und eine der Varianten aktualisiert wird, können Sie wählen, ob Sie nur an die aktualisierten Varianten, an alle Varianten erneut senden oder den Seed-Gruppen-Versand bei Aktualisierung deaktivieren möchten.
{% endalert %}

![Die Seed-Gruppe „E-Mail-Seed-Test“ ist ausgewählt, um die E-Mail-Campaign der Variante 1 zu erhalten.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Für Canvas {#for-canvas}

Seed-Gruppen in Canvas funktionieren ähnlich wie bei jeder getriggerten Campaign. Braze erkennt automatisch alle Schritte, die eine E-Mail-Nachricht enthalten, und sendet an diese, wenn Ihre Nutzer:innen zum ersten Mal diesen bestimmten E-Mail-Schritt erreichen.

Wenn ein E-Mail-Schritt aktualisiert wurde, nachdem die Seed-Gruppe bereits versendet wurde, bietet Braze die Option, nur an aktualisierte Schritte, an alle Schritte zu senden oder Seeds zu deaktivieren.