---
nav_title: Zum-Kalender-hinzufügen-Links
article_title: Zum-Kalender-hinzufügen-Links
page_order: 1
page_type: tutorial
description: "Dieser Artikel beschreibt, wie Sie einen Zum-Kalender-hinzufügen-Link in Ihre E-Mail-Campaigns einfügen können."
channel: email

---

# Zum-Kalender-hinzufügen-Links {#add-to-calendar-links}

> Wenn Sie ein Event, einen Sale oder einen Termin bewerben, können Sie es Ihren Nutzer:innen erleichtern, das Event in ihrem Kalender zu speichern, indem Sie einen „Zum Kalender hinzufügen“-Link in Ihre E-Mails einfügen.

Verfassen Sie Ihre E-Mail und legen Sie fest, wo die beiden Kalenderoptionen erscheinen sollen: ein Link für Google Calendar und einer für andere Kalender (wie iCal oder Outlook). Verwenden Sie Linktexte wie „Zu Google Calendar hinzufügen“ und „Zu iCal oder Outlook hinzufügen“.

Wie Sie die URLs einfügen, hängt davon ab, welchen E-Mail-Editor Sie verwenden:

- **Drag-and-Drop-Editor:** Wählen Sie in einem **Paragraph**-Block die zu verlinkenden Wörter aus, öffnen Sie das **Link**-Steuerelement in der Symbolleiste und fügen Sie die URL aus dem [URL-Format](#url-format) ein. Alternativ können Sie einen **Button**-Block verwenden, den **Linktyp** auf **Webseite öffnen** setzen und die URL in **URL** einfügen.
- **HTML-Editor:** Verwenden Sie die Rich-Text-Link-Steuerelemente für verlinkten Text oder fügen Sie `<a href="...">` Tags in Ihrem HTML für jede Kalender-URL hinzu.

## URL-Format {#url-format}

Fügen Sie Ihren Links die folgende URL hinzu und ersetzen Sie die Platzhalter. Der einzige Unterschied zwischen diesen beiden URLs besteht darin, dass Google Kalender einen zusätzlichen Parameter benötigt: `&format=gcal`.

{% tabs %}
{% tab Google Kalender %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal oder Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

Ersetzen Sie Folgendes:

- `EVENT_SUBJECT`: Titel des Ereignisses
- `EVENT_LOCATION`: Standort des Ereignisses
- `START_TIME`: Startzeit des Ereignisses im ISO-8601-Format (YYYY-MM-DDTHH:MM:SSZ) als UTC
- `END_TIME`: Endzeit des Ereignisses im ISO-8601-Format (YYYY-MM-DDTHH:MM:SSZ) als UTC
- `EVENT_DESCRIPTION`: Beschreibung des Ereignisses

Ersetzen Sie alle Leerzeichen durch den HTML-Escape-Code `%20`. Zum Beispiel würde ein Betreff „Meet Braze“ zu „Meet%20Braze“.

Hier ist ein Beispiel für eine „Zu Google Kalender hinzufügen“-URL:

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### Zusätzliche Parameter {#additional-parameters}

Die folgenden Parameter sind optional und können verwendet werden, um weitere Aspekte eines Ereignisses zu definieren.

- **Name des Organisators:** `&organizer=name`
- **URL zum Ereignis anhängen:** `&attach=http://www.example.com/`
- **Dauer:** `duration=30M`, als Alternative zur Endzeit des Ereignisses (dtend) können Sie eine Dauer wie 1H oder 30M angeben
- **Erinnerungsalarm in Minuten:** `&reminder=15`
- **Ganztägiges Ereignis:** `&allday=1`
- **UID:** optionaler Parameter, um den eindeutigen Bezeichner für das Ereignis fest zu codieren, sodass einige Kalender-Apps das Ereignis im Laufe der Zeit aktualisieren können. Der String @ics.agical.io wird automatisch an den Wert angehängt.

Sie können auch zusätzliche Parameter für wiederkehrende Ereignisse hinzufügen:
- **Wöchentliche Ereignisse:** `&recur=weekly`
- **Monatliche Ereignisse:** `&recur=monthly`
- **Ende der Wiederholung:** `&recuruntil=END_DATE`, wobei `END_DATE` das Datum und die Uhrzeit ist, zu der die Wiederholung endet, im ISO-8601-Format (YYYY-MM-DDTHH:MM:SSZ) als UTC

## Linkverhalten {#link-behavior}

Wenn Nutzer:innen auf den Link klicken, wandeln Kalender die UTC-Zeitstempel in den URLs automatisch so um, dass sie die in ihrem Kalender eingestellte Zeitzone widerspiegeln.

Wenn Sie beispielsweise den Beispiellink „Zu Google Kalender hinzufügen“ öffnen und Ihr Kalender auf CST eingestellt ist, wird die Uhrzeit des Ereignisses entsprechend dem Wert von 15:00 Uhr UTC in CST (10:00 Uhr) vorausgefüllt.

### Google Kalender {#google-calendar}

Beim Klicken öffnet sich Google Kalender in einem neuen Tab oder Fenster, wobei die Details des Ereignisses in der Einladung vorausgefüllt und zum Speichern bereit sind. Dies funktioniert sowohl auf Mobilgeräten als auch auf dem Desktop.

![Google-Kalender-Dialog zum Hinzufügen eines Ereignisses mit vorausgefüllten Ereignisdetails, bereit zum Speichern.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal oder Outlook {#ical-or-outlook}

Beim Klicken auf dem Desktop wird eine ICS-Datei heruntergeladen. Nutzer:innen müssen dann die ICS-Datei öffnen, wodurch iCal oder Outlook gestartet wird und sie aufgefordert werden, das Ereignis zu ihrem Kalender hinzuzufügen.

![iCal-Kalender mit einem Dialog zum Hinzufügen eines neuen Ereignisses, der Nutzer:innen auffordert, einen Kalender auszuwählen und zu bestätigen.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![iCal-Kalender mit dem hinzugefügten Ereignis.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

Auf Mobilgeräten hängt das Verhalten vom Gerät und der E-Mail-App ab.

{% alert note %}
Auf dem iPhone laden die Mail-App und Microsoft Outlook die ICS-Datei herunter, wenn Nutzer:innen auf den iCal-Link tippen, aber diese Apps öffnen den Kalender nicht über den Link. Um das Ereignis hinzuzufügen, öffnen Sie die heruntergeladene Datei über **Dateien**, **Downloads** oder die Anhangsansicht (je nach App) und führen Sie dann die Schritte im Kalender aus.
{% endalert %}

In einigen anderen mobilen E-Mail-Apps oder Browsern kann durch langes Drücken auf den Link eine Option zum Hinzufügen des Ereignisses zu einem Kalender angezeigt werden.

![iOS-Pop-up beim langen Drücken auf einen Kalenderlink mit einem Button „Zum Kalender hinzufügen“.]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

Weitere Informationen finden Sie unter:
* [Ereignisse für Google Kalender erstellen](https://developers.google.com/calendar/api/guides/create-events)
* [Einen „Zum Kalender hinzufügen“-Link in einer E-Mail-Nachricht erstellen](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)