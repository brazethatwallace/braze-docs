---
nav_title: "Event-Objekt"
article_title: API-Event-Objekt
page_order: 6
page_type: reference
description: "Dieser Referenzartikel behandelt das Event-Objekt, was es ist und warum es ein wichtiger Bestandteil eventbasierter Campaign-Strategien ist."

---

# Event-Objekt {#event-object}

> Dieser Artikel erläutert die verschiedenen Komponenten eines Event-Objekts, wie Sie dieses Objekt verwenden können und Beispiele, an denen Sie sich orientieren können.

## Was ist ein Event-Objekt? {#what-is-an-event-object}

Ein Event-Objekt ist ein Objekt, das über die API übergeben wird, wenn ein bestimmtes Ereignis eintritt. Event-Objekte sind in einem Events-Array untergebracht. Jedes Event-Objekt im Events-Array repräsentiert ein einzelnes Vorkommen eines angepassten Events durch eine:n bestimmte:n Nutzer:in zum angegebenen Zeitwert. Das Event-Objekt verfügt über viele verschiedene Felder, mit denen Sie durch das Festlegen und Verwenden von Event-Eigenschaften in Nachrichten, Datenerfassung und Personalisierung anpassen können.

Wie Sie angepasste Events für eine bestimmte Plattform einrichten, erfahren Sie in der Anleitung zur Plattformintegration im [Entwicklerhandbuch]({{site.baseurl}}/developer_guide/home). Lesen Sie den entsprechenden Artikel für Ihre Plattform:

- [Android]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)

### Objektkörper {#object-body}

```json
{
  // One of "external_id" or "user_alias" or "braze_id" or "email" or "phone" is required
  "external_id" : (optional, string) External user ID,
  "user_alias" : (optional, User Alias Object) User alias object,
  "braze_id" : (optional, string) Braze user identifier,
  "email": (optional, string) User email address,
  "phone": (optional, string) User phone number,
  "app_id" : (optional, string) see App Identifier,
  "name" : (required, string) the name of the event,
  "time" : (required, datetime as string in ISO 8601 or in `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format),
  "properties" : (optional, Properties Object) properties of the event
  // Setting this flag to true will put the API in "Update Only" mode.
  // When using a "user_alias", "Update Only" mode is always true.
  "_update_existing_only" : (optional, boolean)
  // See following notes regarding anonymous push token imports
}
```

- [Externe Nutzer-ID]({{site.baseurl}}/api/basics#user-ids)
- [App-Bezeichner]({{site.baseurl}}/api/identifier_types)
- [ISO 8601 Zeitcode](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
Einige Bezeichnerpaare können nicht zusammen in einer einzigen Anfrage verwendet werden. Wenn sowohl `email` als auch `phone` angegeben sind, hat `email` Vorrang vor `phone`. Ausführliche Informationen finden Sie unter [Bezeichnerauflösung]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution).
{% endalert %}

#### Nur bestehende Profile aktualisieren {#update-existing-profiles-only}

Um nur bestehende Nutzerprofile in Braze zu aktualisieren, sollten Sie den Schlüssel `_update_existing_only` mit dem Wert `true` im Hauptteil Ihrer Anfrage übergeben. Wenn dieser Wert weggelassen wird, erstellt Braze ein neues Nutzerprofil, wenn die `external_id` nicht bereits existiert.

{% alert note %}
Wenn Sie über den Endpunkt `/users/track` ein Nutzerprofil erstellen, das nur aus Aliasen besteht, muss `_update_existing_only` auf `false` gesetzt werden. Wenn dieser Wert weggelassen wird, wird das Profil, das nur einen Alias enthält, nicht erstellt.
{% endalert %}

## Event-Eigenschaften-Objekt {#event-properties-object}

Angepasste Events und Käufe können Event-Eigenschaften haben. Die „properties“-Werte sollten ein Objekt sein, bei dem die Schlüssel die Eigenschaftsnamen und die Werte die Eigenschaftswerte sind. Eigenschaftsnamen müssen nicht-leere Strings mit maximal 255 Zeichen sein, ohne führende Dollarzeichen ($).

Bei den Eigenschaftswerten kann es sich um jeden der folgenden Datentypen handeln:

| Datentyp | Beschreibung |
| --- | --- |
| Zahlen | Entweder als [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) oder [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Boolesche Werte | `true` oder `false` |
| Datumsangaben | Müssen als Strings im Format [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) oder in einem der folgenden Formate formatiert sein: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Innerhalb von Arrays nicht unterstützt. <br><br>Beachten Sie, dass „T“ ein Zeitbezeichner und kein Platzhalter ist und nicht geändert oder entfernt werden sollte. <br><br>Zeitattribute ohne Zeitzone werden standardmäßig auf Mitternacht UTC gesetzt (und auf dem Dashboard als das Äquivalent zu Mitternacht UTC in der Zeitzone des Unternehmens formatiert). <br><br> Ereignisse mit Zeitstempeln in der Zukunft werden standardmäßig auf die aktuelle Zeit gesetzt.  |
| Strings | 255 Zeichen oder weniger. |
| Arrays | Arrays können keine Datumsangaben enthalten. |
| Objekte | Objekte werden als Strings eingelesen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Event-Eigenschaften-Objekt" }

Event-Eigenschaftsobjekte, die Array- oder Objektwerte enthalten, können eine Event-Eigenschafts-Nutzlast von bis zu 100&nbsp;KB haben.

### Reservierte Schlüssel {#reserved-keys}

Die folgenden Schlüssel sind reserviert und können nicht als angepasste Event-Eigenschaftsnamen verwendet werden:

- `time`
- `event_name`

{% alert important %}
Die Verwendung reservierter Schlüssel als angepasste Event-Eigenschaftsnamen führt zu API-Fehlern beim Senden von Anfragen an den Endpunkt `/users/track`.
{% endalert %}

### Persistenz von Event-Eigenschaften {#event-property-persistence}

Event-Eigenschaften dienen zum Filtern und zur Liquid-Personalisierung von Nachrichten, die durch ihre übergeordneten Ereignisse getriggert werden. Standardmäßig werden sie nicht auf dem Braze-Nutzerprofil persistent gehalten. Um Event-Eigenschaftswerte bei der Segmentierung zu verwenden, lesen Sie den Abschnitt [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events), in dem die verschiedenen Ansätze zur langfristigen Speicherung von Event-Eigenschaftswerten beschrieben werden.

#### Beispielanfrage für ein Event {#event-example-request}

```http
POST https://YOUR_REST_API_URL/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:30+01:00"
    },
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "rented_movie",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
      }
    },
    {
      "user_alias" : { "alias_name" : "device123", "alias_label" : "my_device_identifier"},
      "app_id" : "your-app-id",
      "name" : "watched_trailer",
      "time" : "2013-07-16T19:20:50+01:00"
    }
  ]
}
```
- [ISO 8601 Zeitcode Wiki](http://en.wikipedia.org/wiki/ISO_8601)

## Event-Objekte {#event-objects}

Anhand des angegebenen Beispiels können wir sehen, dass jemand vor Kurzem einen Trailer gesehen und dann einen Film ausgeliehen hat. Wir können zwar nicht in eine Campaign gehen und die Nutzer:innen auf der Grundlage dieser Eigenschaften segmentieren, aber wir können diese Eigenschaften strategisch nutzen, indem wir sie in Form einer Quittung verwenden, um eine angepasste Nachricht über einen Kanal mit Liquid zu versenden. Zum Beispiel: „Hallo **Alex**, danke, dass Sie **The Sad Egg** von **Alex Smith** ausgeliehen haben. Hier sind einige Filmempfehlungen, die auf Ihrer Ausleihe basieren …“