---
nav_title: WhatsApp-Nachricht erstellen
article_title: WhatsApp-Nachricht erstellen
page_order: 1
description: "Dieser Referenzartikel behandelt, wie Sie eine WhatsApp-Nachricht erstellen und WhatsApp-spezifische Felder, Einstellungen und das Nachrichtenverhalten konfigurieren."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - WhatsApp
search_rank: 1
---

# WhatsApp-Nachricht erstellen {#create-a-whatsapp-message}

> Nutzen Sie WhatsApp-Campaigns, um Ihre Kund:innen direkt zu erreichen. Verwenden Sie Liquid und andere dynamische Inhalte, um jede Nachricht zu personalisieren und ein einheitliches Markenerlebnis zu schaffen.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Folgendes vorhanden ist:

| Anforderung | Beschreibung |
| --- | --- |
| Campaign oder Canvas | Richten Sie eine [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) oder ein [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) ein, bevor Sie Ihre WhatsApp-Nachricht verfassen. |
| WhatsApp-Kanal einrichten | Schließen Sie den [WhatsApp-Einrichtungsprozess]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) ab: Bestätigen Sie die Richtlinien, richten Sie Ihre Verbindung ein und konfigurieren Sie die Versand-Infrastruktur. |
| Genehmigte Templates | Erstellen und genehmigen Sie für vom Unternehmen initiierte Sendungen Templates bei Meta. Weitere Informationen finden Sie in [Schritt 3 der WhatsApp-Einrichtung]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen für WhatsApp-Nachrichten" }

## Nachrichtentyp {#message-type}

WhatsApp unterstützt zwei Nachrichtentypen in Braze:

- **Template-Nachrichten:** Für vom Unternehmen initiierte Konversationen. Templates müssen vor dem Versand bei Meta genehmigt werden.
- **Antwortnachrichten:** Zum Antworten auf eingehende Nachrichten von Nutzer:innen innerhalb eines aktiven 24-Stunden-Konversationsfensters.

## Abo-Gruppe {#subscription-group}

Wählen Sie für jede Nachrichtenvariante oder jeden Canvas-Nachrichten-Schritt eine WhatsApp-Abo-Gruppe aus. Die Abo-Gruppe bestimmt, welche Absenderkonfiguration verwendet wird und welche Nutzer:innen zum Empfang der Nachricht berechtigt sind.

## Sprachen für Template-Nachrichten {#languages-for-template-messages}

Jedes genehmigte Template ist an eine bestimmte Sprache gebunden. Konfigurieren Sie separate Varianten oder Canvas-Schritte, wenn Sie mehrere Template-Sprachen unterstützen möchten.

Wenn Sie Text in einer Rechts-nach-links-Sprache hinzufügen, lesen Sie [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

## Erstellung {#step-2-compose-your-whatsapp-message}

Verfassen Sie Ihren WhatsApp-Content im Nachrichten-Editor. Für WhatsApp-spezifische Einstellungsoptionen verwenden Sie die folgende Feldreferenz.

| Feld oder Einstellung | Funktion | Hinweise |
| --- | --- | --- |
| **Abo-Gruppe** | Der WhatsApp-Sender und die berechtigte Zielgruppe für die Nachricht. | Die zugehörige Absender-Telefonnummer wird im Hinweis des **Test**-Tabs angezeigt. |
| **Nachrichtentyp** | Ob die Variante eine Template-Nachricht oder eine Antwortnachricht sendet. | Vom Unternehmen initiierte Sendungen erfordern ein Template. Antwortnachrichten erfordern ein aktives Konversationsfenster. |
| **Template** (Template-Nachrichten) | Das genehmigte Meta-Template, das zum Senden der Nachricht verwendet wird. | Deaktivierte Felder im Editor stammen aus dem genehmigten Template und können nur in Meta geändert und erneut genehmigt werden. |
| **Sprache** (Template-Nachrichten) | Die für die Variante oder den Schritt ausgewählte Template-Sprache. | Erstellen Sie pro Sprache eine Kampagnenvariante oder einen Canvas-Schritt, damit Empfänger:innen korrekt zugeordnet werden. |
| **Variablen** (Template-Nachrichten) | Werte, die in die Platzhalter der Template-Variablen eingefügt werden. | Verwenden Sie Liquid oder Klartext in doppelten geschweiften Klammern. Fügen Sie Standardwerte für Liquid hinzu, damit Sendungen nicht fehlschlagen, wenn Profildaten fehlen. |
| **Dynamische Links** | Personalisierte Call-to-Action-URLs. | Meta erfordert, dass Variablen am Ende von CTA-URLs stehen. |
| **Dynamische Bilder** | Medien-URL oder Bild aus der Medienbibliothek, das in Template- oder Antwortnachrichten verwendet wird. | Dynamische Bilder unterstützen Liquid und Connected-Content in URLs. |
| **Antwort-Layout** (Antwortnachrichten) | Das Format des Antwort-Contents. | Unterstützte Layouts sind Quick Reply, Text Message, Media Message, Call-to-action Button, List Message, Flow Message, Meta Product Messages und Carousel. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="WhatsApp-spezifische Felder und Einstellungen" }

{% tabs %}
{% tab Template-Nachrichten %}

### Template-Nachrichten {#template-messages}

Verwenden Sie [genehmigte WhatsApp-Template-Nachrichten]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates), um Konversationen auf WhatsApp zu starten. Template-Genehmigungen werden von Meta abgewickelt und können bis zu 24 Stunden dauern. Wenn Sie den Template-Text bearbeiten, Update or aktualisieren or aktualisieren Sie ihn in Meta und reichen Sie ihn erneut zur Genehmigung ein.

Um ein neues Template zu erstellen und einzureichen, ohne den Campaign- oder Canvas-Editor zu verlassen, wählen Sie **Neues Template erstellen**. Informationen zu Kategorien, Typen und dem vollständigen Erstellungsprozess finden Sie unter [WhatsApp-Template-Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder).

Deaktivierte Textfelder (grau hervorgehoben) können nicht bearbeitet werden, da sie Teil des genehmigten WhatsApp-Templates sind. Um den deaktivierten Text zu Update or aktualisieren or aktualisieren, müssen Sie Ihr Template bearbeiten und erneut genehmigen lassen.

#### Content-Felder {#content-fields}

Verwenden Sie die Feldreferenz-Tabelle für Definitionen von Variablen, dynamischen Links und dynamischen Bildern. Dieser Abschnitt behandelt Template-spezifisches Verhalten und Beispiele.

![Liste von Templates mit Vorschau ihrer Nachrichten, ihren zugewiesenen Sprachen und ihrem Genehmigungsstatus.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

{% alert tip %}
Wenn Sie Liquid verwenden, fügen Sie Standardwerte für Personalisierungsfelder hinzu. Nachrichten mit fehlenden Personalisierungswerten werden von WhatsApp nicht gesendet.
{% endalert %}

![Das Tool „Personalisierung hinzufügen“ mit dem Attribut „first_name“ und dem Standardwert „you“.]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Dynamische Bilder {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Antwortnachrichten %}

### Antwortnachrichten {#response-messages}

Verwenden Sie Antwortnachrichten, um während des aktiven 24-Stunden-Konversationsfensters auf eingehende Nachrichten von Nutzer:innen zu antworten. Diese Nachrichten werden in Braze erstellt und können jederzeit bearbeitet werden.

Antwortnachrichten unterstützen die folgenden Layouts:
- Quick Reply
- Text Message
- Media Message
- Call-to-action Button
- List Message
- Flow Message
- Meta Product Messages
- Carousel

![Der Nachrichten-Editor für Antwortnachrichten mit einer Willkommensnachricht für neue Nutzer:innen inklusive Rabattcode.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

## Ergebnisse des WhatsApp-Testversands {#step-4-view-test-send-results}

Nach dem Senden einer WhatsApp-Testnachricht können Sie einen detaillierten Zustellungsbericht direkt im Nachrichten-Editor einsehen. So können Sie bestätigen, dass Ihre Nachricht die gewünschten Empfänger:innen erreicht hat, und Fehler vor dem Launch beheben.

Der Button **Testergebnisse anzeigen** wird angezeigt, wenn Testversanddaten für die aktuelle Campaign oder den aktuellen Canvas-Schritt verfügbar sind. Wählen Sie ihn aus, um das Ergebnis-Panel zu öffnen.

Das Ergebnis-Panel zeigt jede Phase, die Ihre Nachricht auf dem Weg zu den Empfänger:innen durchlaufen hat:
- **Braze:** Ob Braze die Nachricht erfolgreich verarbeitet und versendet hat
- **Meta:** Ob Meta die Nachricht zur Zustellung akzeptiert hat
- **Nutzergerät:** Ob die Nachricht auf dem Gerät der Empfänger:innen zugestellt wurde

Jede Phase zeigt ihren aktuellen Status an. Wenn eine Phase fehlgeschlagen ist, zeigt das Panel den aufgetretenen Fehler und Hinweise zur Behebung an. Die Ergebnisse bleiben erhalten, wenn Sie dieselbe Campaign oder dasselbe Canvas schließen und erneut öffnen.

![Ergebnis-Panel für Testversand mit zwei erfolgreichen Testversendungen und einem fehlgeschlagenen Testversand.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

### Wiederholungsversuche und frühere Versuche {#retries-and-past-attempts}

Wenn ein Testversand fehlschlägt, wiederholt Braze die Zustellung automatisch bis zu 24 Stunden lang. Das Ergebnis-Panel spiegelt dies mit zwei Tabs wider:

- **Aktuell:** Der letzte Zustellungsversuch, der in Echtzeit aktualisiert wird, wenn Wiederholungsversuche stattfinden
- **Frühere Versuche:** Ein Verlauf früherer Wiederholungsversuche, jeweils mit den Phasenstatus und aufgetretenen Fehlern

Wenn das endgültige Ergebnis feststeht (erfolgreiche Zustellung, ausgeschöpfte Wiederholungsversuche oder ein Fehler, der durch Wiederholen nicht behoben werden kann), werden die Tabs in **Ergebnis** und **Wiederholungsverlauf** umbenannt.

{% alert note %}
Da Wiederholungsversuche bis zu 24 Stunden andauern können, sehen Sie möglicherweise nicht sofort ein endgültiges Ergebnis nach einem fehlgeschlagenen Versand.
{% endalert %}

### Fehler beheben {#troubleshoot-failures}

Wenn eine Phase einen Fehler anzeigt, zeigt das Panel den Fehler und empfohlene nächste Schritte an. Häufige Gründe für fehlgeschlagene Testversendungen sind:

- Das Nachrichten-Template ist pausiert oder noch nicht bei Meta genehmigt
- Die Telefonnummer der Empfänger:innen unterliegt einem Rate-Limit
- Liquid-Variablen in der Nachricht wurden für die ausgewählte Testnutzer:in nicht befüllt

Überprüfen Sie bei anhaltenden Problemen den Template-Status im Meta Business Manager:in oder stellen Sie sicher, dass Ihre Testempfänger:innen die erforderlichen Nutzerattribute in Braze hinterlegt haben.

## Wissenswertes {#supported-whatsapp-features}

### Ausgehende Nachrichten {#outbound-messages}

Die folgenden Features werden für ausgehende WhatsApp-Nachrichten unterstützt, die Sie über Braze senden:

| Feature | Details | Max. Größe | Unterstützte Formate |
| ------- | ------- | ------------- | ---------------------- |
| Kopfzeilentext | Strings und variable Parameter werden unterstützt. | — | —
| Textkörper | Strings und variable Parameter werden unterstützt. | — | — |
| Fußzeilentext | Strings und variable Parameter werden unterstützt. | — | — |
| CTA-Links | Verschiedene Call-to-Action-Typen (CTA) werden unterstützt. Weitere Details finden Sie unter [Call-to-Action-Typen](#ctas). | — | — |
| Bilder | Bilder können in den Textkörper eingebettet werden. Sie müssen 8-Bit sein und entweder ein RGB- oder RGBA-Farbmodell verwenden. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| Dokumente | Dokumente können in den Textkörper eingebettet werden. Dateien müssen über eine URL gehostet werden. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Videos | Videos können in den Textkörper eingebettet werden. Dateien müssen über eine URL oder in der [Braze-Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) gehostet werden. | < 16 MB | `.3gp`, `.mp4` |
| Audio | Audio wird nur über Antwortnachrichten unterstützt. Dateien müssen über eine URL gehostet werden. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Ausgehende Nachrichten" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### Eingehende Nachrichten {#inbound-messages}

Die folgenden Features werden für eingehende WhatsApp-Nachrichten unterstützt, die Sie über Braze empfangen:

| Feature | Details | Unterstützte Formate |
| ------- | ------- | ------------------ |
| Textkörper | Nur Standard-Strings werden unterstützt. | — |
| Bilder | Bilder müssen 8-Bit sein und entweder ein RGB- oder RGBA-Farbmodell verwenden. Dateien müssen kleiner als 5 MB sein. | `.jpg`, `.png` |
| Audio | Nur Ogg-Dateien, die mit dem Opus-Codec codiert sind, werden unterstützt. Andere Ogg-Formate werden nicht unterstützt. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Dokumente | Dokumente werden über Nachrichtenanhänge unterstützt. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Video | Nur der H.264-Video-Codec und der AAC-Audio-Codec werden unterstützt. Videos müssen entweder einen einzelnen Audio-Stream oder keinen Audio-Stream enthalten. | `.mp4`, `.3gp` |
| CTA-Links | Verschiedene Call-to-Action-Typen (CTA) werden unterstützt. Weitere Details finden Sie unter [Call-to-Action-Typen](#ctas). | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Eingehende Nachrichten" }

### Call-to-Action-Typen {#ctas}

Die folgenden Call-to-Action-Typen werden für WhatsApp-Nachrichten unterstützt, die Sie über Braze senden:

| CTA-Typ    | Details |
| ----------- |---------------- |
| Website besuchen | Maximal ein Button (einschließlich variabler Parameter). |
| Telefonnummer anrufen | Nur für Template-Nachrichten verfügbar. <br>Maximal ein Button. |
| Benutzerdefinierte Schnellantwort-Buttons | Maximal drei Buttons. |
| Marketing-Opt-out-Button | Standardmäßig werden Abo-Status nicht automatisch aktualisiert. Eine vollständige Anleitung finden Sie unter [Opt-ins und Opt-outs]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#marketing-opt-out-selection). |
| Aktionscode-Template-Nachrichten | Nur für Template-Nachrichten verfügbar. <br>Diese können wie andere Template-Nachrichten geöffnet und bearbeitet werden und sind mit Liquid und Braze-Aktionscodes kompatibel. |
| CTA-Antwortnachrichten  | Erstellen Sie eine Antwortnachricht, die einen Call-to-Action-Button enthält. |
| [Listen-Antwortnachrichten]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#list-messages) | Erstellen Sie eine Antwortnachricht, die eine Liste mit bis zu 10 Optionen enthält, aus denen Nutzer:innen wählen können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Call-to-Action-Typen #ctas" }

## Nächste Schritte {#next-steps}

Nachdem Sie Ihre WhatsApp-Nachricht erstellt haben, fahren Sie mit dem Aufbau und der Validierung Ihres Versands fort:

- [Planen Sie Ihre Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) oder konfigurieren Sie [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) weiter
- [Stellen Sie die Zielgruppe zusammen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) und legen Sie [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) fest
- [Senden Sie Testnachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp)
- Sehen Sie sich das [WhatsApp-Reporting]({{site.baseurl}}/user_guide/channels/whatsapp/reporting) an