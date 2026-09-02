---
nav_title: "Event-Objekt"
article_title: "Event-Objekt"
page_order: 6
page_type: reference
description: "Dieser Referenzartikel behandelt das Event-Objekt, was es ist und warum es ein wichtiger Bestandteil eventbasierter Campaign-Strategien ist."
---

# Event-Objekt {#event-object}

> Dieser Artikel erläutert die verschiedenen Komponenten eines Event-Objekts, wie Sie dieses Objekt verwenden können und Beispiele, an denen Sie sich orientieren können.

## Was ist ein Event-Objekt? {#what-is-an-event-object}

Ein Event-Objekt ist ein Objekt, das über die API übergeben wird, wenn ein bestimmtes Event auftritt. Event-Objekte befinden sich in einem Events-Array. Jedes Event-Objekt im Events-Array repräsentiert ein einzelnes Vorkommen eines angepassten Events durch eine:n bestimmte:n Nutzer:in zum angegebenen Zeitwert. Das Event-Objekt verfügt über viele verschiedene Felder, mit denen Sie Anpassungen vornehmen können, indem Sie Event-Eigenschaften in Nachrichten, der Datenerfassung und Personalisierung festlegen und verwenden.

Schritte zur Einrichtung angepasster Events für eine bestimmte Plattform finden Sie im Plattform-Integrationsleitfaden im [Entwickler:innen-Leitfaden]({{site.baseurl}}/developer_guide/home). Lesen Sie den entsprechenden Artikel für Ihre Plattform:

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

{% alert note %}
Events mit Zeitstempeln in der Zukunft verwenden standardmäßig die aktuelle Uhrzeit. Dadurch wird sichergestellt, dass angepasste Events mit genauem Timing erfasst werden.
{% endalert %}

- [Externe Nutzer-ID]({{site.baseurl}}/api/basics#user-ids)
- [App-Bezeichner]({{site.baseurl}}/api/identifier_types)
- [ISO 8601-Zeitcode](https://en.wikipedia.org/wiki/ISO_8601)

{% alert note %}
Einige Bezeichner-Paare können nicht gemeinsam in einer einzelnen Anfrage verwendet werden. Wenn sowohl `email` als auch `phone` angegeben werden, hat `email` Vorrang vor `phone`. Vollständige Details finden Sie unter [Bezeichner-Auflösung]({{site.baseurl}}/api/objects_filters/user_attributes_object#identifier-resolution).
{% endalert %}

#### Nur bestehende Profile aktualisieren {#update-existing-profiles-only}

Um nur bestehende Nutzerprofile in Braze zu aktualisieren, sollten Sie den Schlüssel `_update_existing_only` mit dem Wert `true` im Body Ihrer Anfrage übergeben. Wenn dieser Wert weggelassen wird, erstellt Braze ein neues Nutzerprofil, falls die `external_id` noch nicht existiert.

{% alert note %}
Wenn Sie ein reines Alias-Nutzerprofil über den Endpunkt `/users/track` erstellen, muss `_update_existing_only` auf `false` gesetzt werden. Wenn dieser Wert weggelassen wird, wird das reine Alias-Profil nicht erstellt.
{% endalert %}

## Event-Eigenschaften-Objekt {#event-properties-object}

Angepasste Events und Käufe können Event-Eigenschaften haben. Die „properties“-Werte sollten ein Objekt sein, bei dem die Schlüssel die Eigenschaftsnamen und die Werte die Eigenschaftswerte sind. Eigenschaftsnamen müssen nicht-leere Strings mit maximal 255 Zeichen sein und dürfen kein vorangestelltes Dollarzeichen ($) enthalten.

Eigenschaftswerte können einen der folgenden Datentypen haben:

| Datentyp | Beschreibung |
| --- | --- |
| Zahlen | Als [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) oder [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| Boolesche Werte | `true` oder `false` |
| Datums-/Zeitwerte | Müssen als Strings im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format oder in einem der folgenden Formate angegeben werden: <br>- `yyyy-MM-ddTHH:mm:ss:SSSZ` <br>- `yyyy-MM-ddTHH:mm:ss` <br>- `yyyy-MM-dd HH:mm:ss` <br>- `yyyy-MM-dd` <br>- `MM/dd/yyyy` <br>- `ddd MM dd HH:mm:ss.TZD YYYY` <br><br>Innerhalb von Arrays nicht unterstützt. <br><br>Beachten Sie, dass „T“ ein Zeitkennzeichen ist, kein Platzhalter, und nicht geändert oder entfernt werden sollte. <br><br> Zeitattribute ohne Zeitzone werden standardmäßig auf Mitternacht UTC gesetzt (und im Dashboard als Äquivalent von Mitternacht UTC in der Zeitzone des Unternehmens formatiert). <br><br> Events mit Zeitstempeln in der Zukunft werden standardmäßig auf die aktuelle Zeit gesetzt.  |
| Strings | 255 Zeichen oder weniger. |
| Arrays | Arrays können keine Datums-/Zeitwerte enthalten. |
| Objekte | Objekte werden als Strings eingelesen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Event-Eigenschaften-Objekt" }

Event-Eigenschaftsobjekte, die Array- oder Objektwerte enthalten, können eine Event-Eigenschafts-Payload von bis zu 100&nbsp;KB haben.

### Reservierte Schlüssel {#reserved-keys}

Die folgenden Schlüssel sind reserviert und können nicht als Eigenschaftsnamen angepasster Events verwendet werden:

- `time`
- `event_name`

{% alert important %}
Die Verwendung reservierter Schlüssel als Eigenschaftsnamen angepasster Events führt zu API-Fehlern beim Senden von Anfragen an den `/users/track`-Endpunkt.
{% endalert %}

### Persistenz von Event-Eigenschaften {#event-property-persistence}

Event-Eigenschaften sind für die Filterung und Liquid-Personalisierung in Nachrichten vorgesehen, die durch ihre übergeordneten Events ausgelöst werden. Standardmäßig werden sie nicht im Braze-Nutzerprofil gespeichert. Um Event-Eigenschaftswerte in der Segmentierung zu verwenden, lesen Sie den Abschnitt [Angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events), der die verschiedenen Ansätze zur langfristigen Speicherung von Event-Eigenschaftswerten erläutert.

#### Beispielanfrage für Events {#event-example-request}

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
- [ISO 8601 Time Code Wiki](http://en.wikipedia.org/wiki/ISO_8601)

## Event-Objekte {#event-objects}

Anhand des bereitgestellten Beispiels können wir sehen, dass jemand kürzlich einen Trailer angesehen und dann einen Film ausgeliehen hat. Zwar können wir nicht in eine Campaign gehen und die Nutzer:innen anhand dieser Eigenschaften segmentieren, doch wir können diese Eigenschaften strategisch nutzen, indem wir sie in Form einer Quittung verwenden, um über einen Kanal mit Liquid eine angepasste Nachricht zu senden. Zum Beispiel: „Hallo **Alex**, vielen Dank, dass du **The Sad Egg** von **Alex Smith** ausgeliehen hast. Hier sind einige empfohlene Filme basierend auf deiner Ausleihe …“