---
nav_title: Zeotap Symphony
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Zeotap, einer geschäftskunden Data Platform der nächsten Generation, die Identitätsauflösung, Insights und Datenanreicherung bietet."
page_type: partner
search_tag: Partner
page_order: 2
---

# Zeotap Symphony

Die Integration von Braze und Zeotap Symphony ermöglicht es Ihnen, Realtime-Orchestrierungen zu erstellen und Campaigns per E-Mail und Push-Benachrichtigung durchzuführen.

- Senden Sie Vor- und Nachnamen über Zeotap, auf deren Grundlage Nutzer:innen personalisierte E-Mails über Braze versenden können.
- Senden Sie angepasste Events oder ein Kauf-Event in Realtime über Zeotap, auf deren Grundlage Nutzer:innen innerhalb von Braze Campaign-Trigger erstellen können, um ihre Kund:innen zu targetieren.

{% alert note %}
Um E-Mail-Marketing-Campaigns zu erstellen, onboarden Sie die Roh-E-Mails in Zeotap, indem Sie sie `Email Raw` im Zeotap-Katalog zuordnen.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Client Name | Dies ist Ihr Client-Name für Ihr Braze-Konto. Sie finden ihn, indem Sie zur Braze-Konsole navigieren. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Instanz | Ihre Braze-Instanz erhalten Sie von Ihrer/Ihrem Braze-Onboarding-Manager:in oder auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Dieser Abschnitt enthält Informationen zu den beiden Methoden, mit denen Sie Braze integrieren können:

### Methode 1 {#method-1}
Bei dieser Methode müssen Sie die folgenden Aufgaben ausführen:
1. Integrieren Sie das Braze SDK auf Ihrer Website oder in Ihrer App.
2. Integrieren Sie Braze mit Zeotap über Symphony.

- `User traits` müssen den entsprechenden Braze-Feldern auf dem Tab **Data To Send** zugeordnet werden. Wenn Sie die Attribute `Event` und `Purchase` abbilden, führt dies zu einer Duplizierung von Events innerhalb von Braze.
- Bilden Sie `External ID` auf die `User ID` ab, die beim Einrichten des Braze SDK konfiguriert wurde.

Wenn die Integration erfolgreich eingerichtet ist, können Sie Campaigns per E-Mail und Push-Benachrichtigung erstellen, die auf angepassten Attributen basieren, die über Symphony an Braze gesendet werden.

### Methode 2 {#method-2}
Bei dieser Methode können Sie Braze über Symphony mit Zeotap integrieren.

- Diese Methode unterstützt nicht die UI-Features von Braze wie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen.
- Zeotap empfiehlt, die im Zeotap-Katalog verfügbare `hashed email` auf die `External ID` abzubilden.

Wenn die Integration erfolgreich eingerichtet ist, können Sie nur E-Mail-Campaigns erstellen, die auf angepassten Attributen basieren, die über Symphony an Braze gesendet werden.

## Datenfluss zu Braze und unterstützte Bezeichner {#data-flow-to-braze-and-supported-identifiers}

Die Daten fließen von Zeotap zu Braze über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Die folgenden Punkte fassen den Datenfluss zusammen:

1. Zeotap sendet Nutzerprofil-Attribute, angepasste Attribute, angepasste Events und Kauffelder.
2. Sie bilden alle relevanten Zeotap-Katalogfelder auf die Braze-Felder unter dem Tab **Data To Send** ab.
3. Die Daten werden anschließend in Braze hochgeladen.

Details zu den verschiedenen Attributen finden Sie im Abschnitt [Data To Send](#data-to-send-tab).

## Ziel einrichten {#destination-setup}

Nachdem Sie in Symphony Filter angewendet oder eine Bedingung für Ihre Nutzer:innen hinzugefügt haben, können Sie diese in Braze unter **Send to Destinations** aktivieren. Es öffnet sich ein neues Fenster, in dem Sie Ihr Ziel einrichten können. Sie können ein vorhandenes Ziel aus der Liste der **Available Destinations** verwenden oder ein neues erstellen.

### Neues Ziel hinzufügen {#add-new-destination}
Führen Sie die folgenden Schritte aus, um ein neues Ziel hinzuzufügen:
1. Wählen Sie **Add New Destination**.
2. Suchen Sie nach **Braze**.
3. Fügen Sie den **Client Name**, den **API Key** und die **Instance** hinzu und speichern Sie das Ziel.

Das Ziel wird erstellt und unter **Available Destinations** verfügbar gemacht.

### Eingaben auf Workflow-Ebene hinzufügen {#add-workflow-level-inputs}
Nachdem Sie ein Ziel erstellt haben, müssen Sie als Nächstes Eingaben auf Workflow-Ebene hinzufügen, wie in diesem Abschnitt beschrieben.
1. Wählen Sie das Ziel aus der Liste der verfügbaren Ziele mithilfe der Suchfunktion aus.
2. Die Felder **Client Name**, **API Key** und **Instance** werden automatisch auf Grundlage der Werte ausgefüllt, die Sie bei der Erstellung des Ziels eingegeben haben.
3. Geben Sie den **Audience Name** ein, den Sie für diesen Workflow-Knoten erstellen möchten. Dieser wird als **Custom Attribute** an Braze gesendet.
4. Vervollständigen Sie die Katalog-zu-Ziel-Abbildung unter dem Tab **Data To Send**. Details zur Durchführung der Abbildung finden Sie in diesem Abschnitt.

### Tab „Data To Send“ {#data-to-send-tab}
Der Tab **Data To Send** ermöglicht es Ihnen, die Zeotap-Katalogfelder den Braze-Feldern zuzuordnen, die an Braze gesendet werden können. Die Abbildung kann auf eine der folgenden Arten erfolgen:
- **Statische Abbildung** – Es gibt bestimmte Felder, die Zeotap automatisch den entsprechenden Braze-Feldern zuordnet, z. B. E-Mail, Telefon, Vorname, Nachname usw.<br>
- **Dropdown-Auswahl** – Ordnen Sie die relevanten, in Zeotap aufgenommenen Felder den im Dropdown-Menü bereitgestellten Braze-Feldern zu.<br>![Verschiedene Nutzer-Traits, die in Zeotap eingestellt sind, wie Sprache, Ort, Geburtstag und mehr.]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **Eingabe angepasster Daten** – Fügen Sie angepasste Daten hinzu, die dem entsprechenden Zeotap-Feld zugeordnet sind, und senden Sie diese an Braze.<br>![Auswahl von „loyalty_points“ als Nutzer-Trait in Zeotap.]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## Unterstützte Attribute {#supported-attributes}
In diesem Abschnitt finden Sie Details zu allen Braze-Feldern.

| Braze-Feld | Abbildungstyp | Beschreibung |
| --- | --- | --- |
| External ID | Dropdown-Auswahl | Dies ist die persistente `User ID`, die Sie in Braze definiert haben, um Nutzer:innen geräte- und plattformübergreifend zu tracken. Wir empfehlen, `User ID` auf `External ID` abzubilden; andernfalls kann Zeotap E-Mails als Nutzer-Alias senden.<br><br>Zeotap empfiehlt, die im Zeotap-Katalog verfügbare `hashed email` auf die `External ID` abzubilden. |
| E-Mail | Statische Abbildung | Wird im Zeotap-Katalog auf `Email Raw` abgebildet. |
| Telefon | Statische Abbildung | Wird im Zeotap-Katalog auf `Mobile Raw` abgebildet.<br><br>• Braze akzeptiert Telefonnummern im `E.164`-Format. Zeotap führt keine Transformation durch. Daher müssen Sie die Telefonnummern im vorgeschriebenen Format einpflegen. Weitere Informationen finden Sie unter [Nutzer-Telefonnummern]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers). |
| Vorname | Statische Abbildung | Wird im Zeotap-Katalog auf `First Name` abgebildet. |
| Nachname | Statische Abbildung | Wird im Zeotap-Katalog auf `Last Name` abgebildet. |
| Geschlecht | Statische Abbildung | Wird im Zeotap-Katalog auf `Gender` abgebildet. |
| Name des angepassten Events | Statische Abbildung | Wird im Zeotap-Katalog auf `Event Name` abgebildet.<br><br>Sowohl der Name des angepassten Events als auch der Zeitstempel des angepassten Events müssen abgebildet werden, um angepasste Events in Braze zu erfassen. Das angepasste Event kann nicht verarbeitet werden, wenn eines der beiden nicht abgebildet ist. Weitere Informationen finden Sie unter [Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object). |
| Zeitstempel des angepassten Events | Statische Abbildung | Wird im Zeotap-Katalog auf `Event Timestamp` abgebildet.<br><br>Sowohl der Name des angepassten Events als auch der Zeitstempel des angepassten Events müssen abgebildet werden, um angepasste Events in Braze zu erfassen. Das angepasste Event kann nicht verarbeitet werden, wenn eines der beiden nicht abgebildet ist. Weitere Informationen finden Sie unter [Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object). |
| E-Mail-Abonnement | Dropdown-Auswahl | Onboarden Sie ein `Email Marketing Preference`-Feld und bilden Sie es ab.<br><br>Zeotap sendet die folgenden drei Werte:<br>• `opted_in` – Zeigt an, dass sich die Nutzer:innen explizit für E-Mail-Marketing registriert haben.<br>• `unsubscribed` – Zeigt an, dass sich die Nutzer:innen explizit von E-Mail-Nachrichten abgemeldet haben.<br>• `subscribed` – Zeigt an, dass die Nutzer:innen weder ein Opt-in noch ein Opt-out vorgenommen haben. |
| Push-Abonnement | Dropdown-Auswahl | Onboarden Sie ein `Push Marketing Preference`-Feld und bilden Sie es ab.<br><br>Zeotap sendet die folgenden drei Werte:<br>• `opted_in` – Zeigt an, dass sich die Nutzer:innen ausdrücklich für Push-Marketing registriert haben.<br>• `unsubscribed` – Zeigt an, dass sich die Nutzer:innen ausdrücklich von Push-Nachrichten abgemeldet haben.<br>• `subscribed` – Zeigt an, dass die Nutzer:innen weder ein Opt-in noch ein Opt-out vorgenommen haben. |
| E-Mail-Öffnungs-Tracking aktivieren | Dropdown-Auswahl | Bilden Sie das entsprechende `Marketing Preference`-Feld ab.<br><br>Wenn auf „true“ gesetzt, wird ein Öffnungs-Tracking-Pixel zu allen zukünftigen E-Mails hinzugefügt, die an diese Nutzer:innen gesendet werden. |
| E-Mail-Klick-Tracking aktivieren | Dropdown-Auswahl | Bilden Sie das entsprechende `Marketing Preference`-Feld ab.<br><br>Wenn auf „true“ gesetzt, wird das Klick-Tracking für alle Links in allen zukünftigen E-Mails aktiviert, die an diese Nutzer:innen gesendet werden. |
| Product ID | Dropdown-Auswahl | • Bezeichner für eine Kaufaktion `(Product Name/Product Category)`. Weitere Details finden Sie unter [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object).<br>• Onboarden Sie das entsprechende Attribut in den Zeotap-Katalog und bilden Sie es ab.<br><br>`Product ID`, `Currency` und `Price` müssen zwingend abgebildet werden, um Kauf-Events in Braze zu erfassen. Das Kauf-Event kann nicht verarbeitet werden, wenn eines der drei fehlt. Weitere Informationen finden Sie unter [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object). |
| Währung | Dropdown-Auswahl | • Währungsattribut für die Kaufaktion.<br>• Das unterstützte Format ist `ISO 4217 Alphabetic Currency Code`.<br>• Onboarden Sie korrekt formatierte Währungsdaten in den Zeotap-Katalog und bilden Sie sie ab.<br><br>`Product ID`, `Currency` und `Price` müssen zwingend abgebildet werden, um Kauf-Events in Braze zu erfassen. Das Kauf-Event kann nicht verarbeitet werden, wenn eines der drei fehlt. |
| Preis | Dropdown-Auswahl | • Preisattribut für die Kaufaktion.<br>• Onboarden Sie das entsprechende Attribut in den Zeotap-Katalog und bilden Sie es ab.<br><br>`Product ID`, `Currency` und `Price` müssen zwingend abgebildet werden, um Kauf-Events in Braze zu erfassen. Das Kauf-Event kann nicht verarbeitet werden, wenn eines der drei fehlt. |
| Menge | Dropdown-Auswahl | • Mengenattribut für die Kaufaktion.<br>• Onboarden Sie das entsprechende Attribut in den Zeotap-Katalog und bilden Sie es ab. |
| Land | Dropdown-Auswahl | Bilden Sie es auf das `Country`-Katalogfeld ab, das Sie onboarden. |
| Ort | Dropdown-Auswahl | Bilden Sie es auf das `City`-Katalogfeld ab, das Sie onboarden. |
| Sprache | Dropdown-Auswahl | • Das akzeptierte Format ist der `ISO-639-1`-Standard (zum Beispiel en).<br>• Onboarden Sie die korrekt formatierte Sprache und bilden Sie sie ab. |
| Geburtsdatum | Dropdown-Auswahl | Bilden Sie es auf das `Date of Birth`-Feld ab, das Sie onboarden. |
| Angepasstes Attribut | Eingabe angepasster Daten | Bilden Sie jedes Nutzerattribut auf eine angepasste Dateneingabe ab, die dann an Braze gesendet wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Unterstützte Attribute" }

## Daten in der Braze-Konsole anzeigen {#viewing-data-on-braze-console}

Nachdem Sie die relevanten Attribute abgebildet und den Workflow veröffentlicht haben, beginnen die Events auf Grundlage der definierten Kriterien an Braze zu fließen. Sie können in der Braze-Konsole nach E-Mail-ID oder externer ID suchen.

![Braze-Nutzerprofil-Ansicht mit eingehenden Zeotap-Attributen und -Events.]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

Verschiedene Attribute befinden sich in unterschiedlichen Abschnitten des Nutzer-Dashboards in Braze.
- Der Tab **Profil** enthält die Nutzerattribute.
- Der Tab **Angepasste Attribute** enthält die von Nutzer:innen definierten angepassten Attribute.
- Der Tab **Angepasste Events** enthält die von Nutzer:innen definierten angepassten Events.
- Der Tab **Käufe** enthält die Käufe, die Nutzer:innen über einen bestimmten Zeitraum getätigt haben.

## Erstellung von Campaigns {#campaign-creation}

Nutzer:innen können in Braze Campaigns erstellen und Nutzer:innen in Realtime oder nach Zeitplan aktivieren. Campaigns können auf Grundlage der von Nutzer:innen durchgeführten Aktionen (angepasstes Event, Kauf) oder der Nutzerattribute ausgelöst werden.