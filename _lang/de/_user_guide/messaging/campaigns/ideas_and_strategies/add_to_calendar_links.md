---
nav_title: Zum-Kalender-hinzufügen-Links
article_title: Zum-Kalender-hinzufügen-Links
page_order: 1
page_type: tutorial
description: "Dieser Artikel beschreibt, wie Sie einen Zum-Kalender-hinzufügen-Link in Ihre E-Mail-Kampagnen einfügen können."
channel: email

---

# Zum-Kalender-hinzufügen-Links

> Wenn Sie ein Event, einen Sale oder einen Termin bewerben, können Sie es Ihren Nutzer:innen erleichtern, das Event in ihrem Kalender zu speichern, indem Sie einen „Zum Kalender hinzufügen"-Link in Ihre E-Mails einfügen.

Verfassen Sie dazu Ihre E-Mail und legen Sie fest, wo Ihre Links platziert werden sollen. Fügen Sie dann zwei Optionen hinzu: eine für Google Calendar und eine für andere Kalender (wie iCal oder Outlook). Zum Beispiel „Zu Google Calendar hinzufügen" und „Zu iCal oder Outlook hinzufügen".

![Link-Dialog beim Hinzufügen eines Links im Dashboard. Der Tab „Link Info" ist ausgewählt und der Text ist auf „Add to Google Calendar" gesetzt.]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## URL-Format

Fügen Sie die folgende URL zu Ihren Links hinzu und ersetzen Sie die Platzhalter. Der einzige Unterschied zwischen diesen beiden URLs ist, dass Google Calendar einen zusätzlichen Parameter benötigt: `&format=gcal`.

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal or Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Ersetzen Sie Folgendes:

- `EVENT_SUBJECT`: Titel des Events
- `EVENT_LOCATION`: Standort des Events
- `START_TIME`: Startzeit des Events im ISO-8601-Format (YYYY-MM-DDTHH:MM:SSZ) als UTC
- `END_TIME`: Endzeit des Events im ISO-8601-Format (YYYY-MM-DDTHH:MM:SSZ) als UTC
- `EVENT_DESCRIPTION`: Beschreibung des Events

Ersetzen Sie Leerzeichen durch den HTML-Escape-Code `%20`. Zum Beispiel würde ein Betreff „Meet Braze" zu „Meet%20Braze" werden.

Hier ist ein Beispiel für eine „Zu Google Calendar hinzufügen"-URL:

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Zusätzliche Parameter

Die folgenden Parameter sind optional und können verwendet werden, um weitere Aspekte eines Events zu definieren.

- **Name des Organisators:** `&organizer=name`
- **URL zum Event anhängen:** `&attach=http://www.example.com/`
- **Dauer:** `duration=30M` – als Alternative zur Endzeit des Events (dtend) können Sie eine Dauer wie 1H oder 30M angeben
- **Erinnerungsalarm in Minuten:** `&reminder=15`
- **Ganztägiges Event:** `&allday=1`
- **UID:** Optionaler Parameter, um den eindeutigen Bezeichner für das Event fest zu codieren, sodass einige Kalender-Apps das Event im Laufe der Zeit aktualisieren können. Der String @ics.agical.io wird automatisch an den Wert angehängt.

Sie können auch zusätzliche Parameter für wiederkehrende Events hinzufügen:
- **Wöchentliche Events:** `&recur=weekly`
- **Monatliche Events:** `&recur=monthly`
- **Ende der Wiederholung:** `&recuruntil=END_DATE`, wobei `END_DATE` das Datum und die Uhrzeit ist, zu der die Wiederholung endet, im ISO-8601-Format (YYYY-MM-DDTHH:MM:SSZ) als UTC

## Link-Verhalten

Wenn Nutzer:innen auf den Link klicken, wandeln Kalender die UTC-Zeitstempel in den URLs automatisch in die Zeitzone um, die in ihrem Kalender eingestellt ist.

Wenn Sie zum Beispiel den Beispiel-Link „Zu Google Calendar hinzufügen" öffnen und Ihr Kalender auf CST eingestellt ist, wird die Uhrzeit des Events entsprechend dem Wert von 15:00 Uhr UTC in CST (10:00 Uhr) vorausgefüllt.

### Google Calendar

Beim Klicken öffnet sich Google Calendar in einem neuen Tab oder Fenster, wobei die Event-Details in der Einladung vorausgefüllt sind und die Nutzer:innen das Event direkt speichern können. Dies funktioniert sowohl auf Mobilgeräten als auch auf dem Desktop.

![Google-Calendar-Dialog zum Hinzufügen eines Events mit vorausgefüllten Event-Details, bereit zum Speichern.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal oder Outlook

Beim Klicken auf dem Desktop wird eine ICS-Datei heruntergeladen. Die Nutzer:innen müssen dann die ICS-Datei öffnen, wodurch iCal oder Outlook geöffnet wird und sie aufgefordert werden, das Event zu ihrem Kalender hinzuzufügen.

![iCal-Kalender mit einem Dialog zum Hinzufügen eines neuen Events, der die Nutzer:innen auffordert, einen Kalender auszuwählen und zu bestätigen.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![iCal-Kalender mit dem hinzugefügten Event.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

Auf Mobilgeräten müssen Nutzer:innen den Link gedrückt halten, woraufhin sie aufgefordert werden, ihn zu ihrem Kalender hinzuzufügen.

![iOS-Pop-up beim Gedrückthalten eines Kalender-Links mit einem Button „Zum Kalender hinzufügen".]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Weitere Informationen finden Sie unter:
* [Create events for Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Create an Add to calendar link in an email message](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)