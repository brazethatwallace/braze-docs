---
nav_title: Rokt Calendar
article_title: Rokt Calendar
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Rokt Calendar, einer dynamischen Kalender-Marketingtechnologie, die es Marken ermöglicht, 1:1-Ereignisse und Werbebotschaften in Form von Kalenderereignissen und -benachrichtigungen zu pushen."
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) ist eine dynamische Kalender-Marketingtechnologie, die es Marken ermöglicht, 1:1-Ereignisse und Werbebotschaften in Form von Kalenderereignissen und -benachrichtigungen zu pushen.

_Diese Integration wird von Rokt Calendar gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Rokt Calendar ermöglicht es, Ihre Rokt-Calendar-Abonnent:innen und deren Daten über einen Braze-Webhook an Braze zu pushen. Sie können diese Daten dann in Braze Canvase für das Journey-Targeting und die Segmentierung der Zielgruppe mit einem der folgenden angepassten [Rokt-Calendar-Attribute](#audience-segmentation) verwenden.

## Voraussetzungen {#prerequisites}

| Anforderung  | Beschreibung |
| ------------ | ----------- |
| Rokt-Calendar-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein kundenspezifisches Rokt-Calendar-Konto. Kontaktieren Sie [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com), um mit einem Account Manager:in zu sprechen.  |
| Rokt-Calendar-Einrichtung | Ihr Account Manager:in von Rokt Calendar wird mit Ihnen zusammenarbeiten, um den Kalender so einzurichten, dass er Ihren Bedürfnissen am besten entspricht, einschließlich Einstellungen wie:<br>- Merge-Flag<br>- Fallback-Flag für Abonnenten-ID<br>- E-Mail-Erfassung, falls erforderlich |
| Rokt-Calendar-OAuth-Zugangsdaten | Dieser Schlüssel, den Ihnen Ihr Account Manager:in von Rokt Calendar zur Verfügung stellt, ermöglicht es Ihnen, Ihre Braze- und Rokt-Calendar-Konten miteinander zu verbinden.<br><br>Dieser kann im Braze-Dashboard unter **Settings** > **Connected Content** erstellt werden. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. Diesen Schlüssel müssen Sie Ihrem Rokt-Calendar-Account-Manager:in mitteilen.<br><br> Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. |
| [Braze-Representational State Transfer-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) | Ihre Representational State Transfer-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Externe Abonnenten-ID | Dies ist der Bezeichner, der vom Rokt-Calendar-Abo-Prozess verwendet wird, um die Kalender-Abonnent:innen mit den Braze-Nutzer:innen abzugleichen. Diesen Wert übergeben Sie an Rokt Calendar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Segmentierung der Zielgruppe {#audience-segmentation}

Wenn Rokt Calendar neue Nutzer:innen erstellt oder bestehende Abonnent:innen mit Braze-Nutzer:innen abgleicht, sendet Rokt Calendar die folgenden angepassten Abo-Attribute, die Sie in Braze filtern können:

| Angepasstes Attribut  | Definition       | Beispiel          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Code des Rokt-Calendar-Kontos | `brazetest/f5733866ade2` und `brazetest/ff10919f1078` |
| `rokt:account_id` | ID des Rokt-Calendar-Kontos | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Name des Rokt-Calendar-Kontos | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Code des Rokt-Calendar-Kalenders | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID des Rokt-Calendar-Kalenders | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Titel des Rokt-Calendar-Kalenders | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | Ländercode für das erstellte Abo | `AU/f5733866ade2` |
| `rokt:device_name` | Gerätetyp in Bezug auf das erstellte Abo | `Desktop/f5733866ade2` |
| `rokt:geo_country` | Herkunftsland in Bezug auf das erstellte Abo | `Australia/f5733866ade2` |
| `rokt:optIn1` | Ob sich die Nutzer:innen für das erste von 2 Opt-ins in Bezug auf das erstellte Abo entschieden haben | `True/f5733866ade2` |
| `rokt:optIn2` | Ob sich die Nutzer:innen für das zweite von 2 Opt-ins in Bezug auf das erstellte Abo entschieden haben | `True/f5733866ade2` |
| `rokt:source` | Die Quelle des erstellten Abos | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | Die E-Mail-Adresse, die die Nutzer:innen während des Abo-Vorgangs eingegeben haben | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | Die Abo-ID, die als eindeutiger Bezeichner für das erstellte Abo dient | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Abo-Methode (webcal/Google) in Bezug auf das erstellte Abo | `WebCal/f5733866ade2` |
| `rokt:tags` | Verwendete Kalender-Tags im Zusammenhang mit dem erstellten Abo | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Audience segmentation #audience-segmentation" }

Rokt Calendar triggert außerdem ein angepasstes Event `subscribe`, sobald Nutzer:innen Ihren Rokt-Kalender abonniert haben. Dieses Event kann entweder in der Braze-Segmentierung verwendet werden oder als Trigger or triggern für eine Campaign oder eine Canvas-Komponente dienen.

## Integration

### 1. Schritt: Aufbau einer Zielgruppe von Kalender-Abonnent:innen {#step-1-building-an-audience-of-calendar-subscribers}

Um Kalender-Ereignisse aus Canvas heraus zu versenden, müssen Sie zunächst einen Rokt-Kalender mit bereits abonnierten Nutzer:innen einrichten. Dazu müssen Sie Ihren Nutzer:innen mitteilen, wo und wie sie den Kalender abonnieren können. Rokt Calendar empfiehlt Folgendes:

#### Bereitstellung von Abo-Integrationspunkten {#provide-subscription-integration-points}
Um eine Zielgruppe von Kalender-Abonnent:innen aufzubauen, müssen Sie ein Ziel anbieten, zu dem Nutzer:innen navigieren und das sie abonnieren können. Einige Beispiele für Abo-Integrationspunkte sind:
  - Fügen Sie einen Kalender-Button zu Ihrer Website hinzu
  - Fügen Sie einen Kalender-Link in einer E-Mail oder Kurzmitteilungsdienst or SMS hinzu
  - Fügen Sie einen Kalender-Button zu Ihrer App hinzu
  - Fügen Sie einen Kalender-Link in Social Media hinzu

#### Bewerben Sie den Kalender {#promote-the-calendar}
Um eine Zielgruppe von Abonnent:innen aufzubauen, müssen Sie den Kalender bei Ihrer Zielgruppe bekannt machen, damit diese weiß, wie sie ihn abonnieren kann. Einige Beispiele für Kalender-Aktionen sind:
  - Beiträge in Social Media
  - E-Mail-Newsletter und Updates
  - Blog-Beiträge
  - In-App-Benachrichtigungen

### 2. Schritt: Erstellen eines Rokt-Calendar-Webhooks in Braze {#step-2-create-a-rokt-calendar-webhook-in-braze}

Innerhalb von Braze können Sie eine Webhook-Campaign oder einen Webhook innerhalb eines Canvas einrichten, um entweder:

- Ein neues personalisiertes Ereignis zu senden: Ermöglicht das Hinzufügen neuer Ereignisse zu den Kalendern eines Segments von Abonnent:innen.
- Ein personalisiertes Ereignis zu Update or aktualisieren or aktualisieren: Ermöglicht das Update or aktualisieren eines bestehenden Ereignisses in den Kalendern von Abonnent:innen.

Um ein Rokt-Calendar-Webhook-Template zu erstellen, das Sie in zukünftigen Campaigns oder Canvase verwenden können, navigieren Sie auf der Braze-Plattform zu **Templates** > **Webhook Templates**.

Wenn Sie eine einmalige Rokt-Calendar-Webhook-Campaign erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Campaign **Webhook** in Braze aus.

{% tabs %}
{% tab Send a new event %}
Sobald Sie das Rokt-Calendar-Webhook-Template ausgewählt haben, sollten Sie Folgendes sehen:
- **Webhook-URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Anfragetext**: Rohtext
{% endtab %}
{% tab Update or aktualisieren an existing event %}
Sobald Sie das Rokt-Calendar-Webhook-Template ausgewählt haben, sollten Sie Folgendes sehen:
- **Webhook-URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Anfragetext**: Rohtext
{% endtab %}
{% endtabs %}

#### Anfrage-Header und Methode {#request-headers-and-method}

Rokt Calendar benötigt zur Autorisierung einen `HTTP Header`, der den Namen Ihrer Connected-Content-Zugangsdaten für Rokt Calendar enthält. Die folgenden Angaben sind bereits als Schlüssel-Wert-Paare im Template enthalten, aber im Tab **Settings** müssen Sie `<Rokt-Calendar-API>` durch den Namen der Zugangsdaten ersetzen, den Sie unter `Manage Settings > Connected Content > Credential` finden.

{% raw %}
- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Authorization**: Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### Anfragetext {#request-body}

{% tabs local %}
{% tab Send a new event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab Update or aktualisieren an existing event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab Event details %}
Die folgenden Felder enthalten Informationen, die auf der Ebene des Ereignisses angepasst werden können.

| Feld             | Definition       | Beispiel          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>***Erforderlich** | Ein eindeutiger Bezeichner für das Ereignis, das hinzugefügt oder aktualisiert werden soll | `Event_00001`
| `eventTitle` <br>***Erforderlich** | Der Titel des Ereignisses, wie er im Kalender erscheinen würde | Sommerschlussverkauf 2019
| `eventDescr` | Die Beschreibung des Ereignisses, wie sie im Kalender erscheinen würde | Der Verkauf läuft drei Tage lang. Klicken Sie auf diesen Link `www.mybusiness.com/sale`, um die Angebote zu sehen. |
| `eventLocation` | Der Standort des Ereignisses, wie er im Kalender erscheinen würde. Beachten Sie, dass dies oft als zweite Handlungsaufforderung verwendet wird, die den eventTitle ergänzt. | Öffnen Sie das Ereignis und erhalten Sie 50 % Rabatt |
| `eventStart` <br>***Erforderlich**  | Das Startdatum und die Startzeit des Ereignisses, wie es im Kalender erscheinen würde | `2019-02-21T15:00:00` |
| `eventEnd` <br>***Erforderlich**  | Das Enddatum und die Endzeit des Ereignisses, wie es im Kalender erscheinen würde | `2019-02-21T16:00:00` |
| `eventTz` <br>***Erforderlich**  | Die Zeitzone des Ereignisses, wie sie im Kalender erscheinen würde. Beachten Sie, dass die Liste der anwendbaren Zeitzonen [hier](https://roktcalendar-api.readme.io/docs/timezones) zu finden ist. | `Eastern Standard Time` |
| `notifyBefore` <br>***Erforderlich**  | Die Erinnerungszeit des Ereignisses, wie sie im Kalender erscheinen würde. Beachten Sie, dass diese in Minuten ausgedrückt wird. | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Request body" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Eine Liste der gültigen Zeitzonen finden Sie unter [https://roktcalendar-api.readme.io/reference/timezones](https://roktcalendar-api.readme.io/reference/timezones).
{% endalert %}

### 3. Schritt: Vorschau Ihrer Anfrage {#step-3-preview-your-request}

Zeigen Sie eine Vorschau Ihrer Anfrage im Panel **Preview** an oder navigieren Sie zum Tab **Test**, wo Sie zufällige Nutzer:innen oder bestehende Nutzer:innen auswählen oder eigene anpassen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) erstellen.
{% endalert %}