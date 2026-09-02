---
nav_title: "POST: Nutzer:innen zusammenführen"
article_title: "POST: Nutzer:innen zusammenführen"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Nutzer:innen zusammenführen“."
---
{% api %}
# Nutzer:innen zusammenführen {#merge-users}
{% apimethod post %}
/users/merge
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Nutzer:in mit einer anderen Nutzer:in zusammenzuführen.

Pro Anfrage können bis zu 50 Zusammenführungen angegeben werden. Dieser Endpunkt ist asynchron.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics) mit der Berechtigung `users.merge`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `merge_updates` | Erforderlich | Array | Ein Objekt-Array. Jedes Objekt sollte ein `identifier_to_merge`-Objekt und ein `identifier_to_keep`-Objekt enthalten, die jeweils eine Nutzer:in entweder über `external_id`, `user_alias`, `phone` oder `email` referenzieren sollten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter" }

### Zusammenführungsverhalten {#merge-behavior}

Das unten dokumentierte Verhalten gilt für alle Braze-Features, die **nicht** von Snowflake unterstützt werden. Zusammenführungen von Nutzer:innen werden auf dem Tab **Messaging-Verlauf**, in Segmenterweiterungen, im Abfrage-Builder und in Currents nicht widergespiegelt.

{% alert important %}
Der Endpunkt garantiert nicht die Reihenfolge, in der `merge_updates`-Objekte aktualisiert werden.
{% endalert %}

Dieser Endpunkt führt die folgenden Felder zusammen, wenn sie bei der Zielnutzer:in nicht gefunden werden.

- Vorname
- Nachname
- E-Mail-Adressen (es sei denn, sie sind [verschlüsselt]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption))
- Geschlecht
- Geburtsdatum
- Telefonnummer
- Zeitzone
- Wohnort
- Land
- Sprache
- Geräteinformationen
- Anzahl der Sitzungen (die Summe der Sitzungen aus beiden Profilen)
- Datum der ersten Sitzung (Braze wählt das frühere der beiden Daten)
- Datum der letzten Sitzung (Braze wählt das spätere der beiden Daten)
- Angepasste Attribute (Braze behält vorhandene angepasste Attribute im Zielprofil bei und fügt angepasste Attribute hinzu, die im Zielprofil nicht vorhanden waren)
- Angepasste Event- und Kauf-Event-Daten
- Angepasste Event- und Kauf-Event-Eigenschaften für die Segmentierung „X-mal in Y Tagen“ (wobei X<=50 und Y<=30)
- Segmentierbare Zusammenfassung angepasster Events
  - Event-Anzahl (die Summe aus beiden Profilen)
  - Ereignis erstmals aufgetreten (Braze wählt das frühere der beiden Daten)
  - Ereignis zuletzt aufgetreten (Braze wählt das spätere der beiden Daten)
- In-App-Käufe insgesamt in Cent (die Summe aus beiden Profilen)
- Gesamtzahl der Käufe (die Summe aus beiden Profilen)
- Datum des ersten Kaufs (Braze wählt das frühere der beiden Daten)
- Datum des letzten Kaufs (Braze wählt das spätere der beiden Daten)
- App-Zusammenfassungen
- Last_X_at-Felder (Braze aktualisiert die Felder, wenn die verwaisten Profilfelder aktueller sind)
- Campaign-Interaktionsdaten (Braze wählt die aktuellsten Datumsfelder)
- Workflow-Zusammenfassungen (Braze wählt die aktuellsten Datumsfelder)
- Nachrichten- und Nachrichten-Engagement-Verlauf
- Braze führt Sitzungsdaten nur zusammen, wenn die App in beiden Nutzerprofilen vorhanden ist.

{% alert note %}
Bei der Zusammenführung von Nutzer:innen funktioniert die Verwendung des Endpunkts `/users/merge` genauso wie die Verwendung der [`changeUser()`-Methode](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
{% endalert %}

Braze behandelt drei Nutzertypen bei der Zusammenführung unterschiedlich: zur Löschung markierte Nutzer:innen, Testnutzer:innen und Nutzer:innen der globalen Kontrollgruppe. Weitere Details finden Sie unter [Verhalten bei der Zusammenführung von Nutzer:innen]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior).

#### Verhalten bei angepasstem Event-Datum und Kauf-Event-Datum {#custom-event-date-and-purchase-event-date-behavior}

Diese zusammengeführten Felder Update or aktualisieren or aktualisieren die Filter „für X Events in Y Tagen“. Bei Kauf-Events umfassen diese Filter „Anzahl der Käufe in Y Tagen“ und „Geldausgaben in den letzten Y Tagen“.

### Zusammenführung von Nutzer:innen per E-Mail oder Telefonnummer {#merging-users-by-email-or-phone-number}

Wenn `email` oder `phone` als Bezeichner angegeben wird, müssen Sie einen zusätzlichen `prioritization`-Wert im Bezeichner angeben. `prioritization` sollte ein geordnetes Array sein, das angibt, welche Nutzer:in zusammengeführt werden soll, wenn mehrere Nutzer:innen gefunden werden. Das bedeutet, dass bei mehreren übereinstimmenden Nutzer:innen aus einer Priorisierung keine Zusammenführung erfolgt.

Die zulässigen Werte für das Array sind:

- `identified`
- `unidentified`
- `most_recently_updated` (bezieht sich auf die Priorisierung der zuletzt aktualisierten Nutzer:in)
- `least_recently_updated` (bezieht sich auf die Priorisierung der am längsten nicht aktualisierten Nutzer:in)

Es kann jeweils nur eine der folgenden Optionen im Priorisierungs-Array vorhanden sein:

- `identified` bezieht sich auf die Priorisierung einer Nutzer:in mit einer `external_id`
- `unidentified` bezieht sich auf die Priorisierung einer Nutzer:in ohne eine `external_id`

{% alert important %}
Wenn beide Profile ungültige Telefonnummern haben, führt Braze sie nicht zusammen. Ungültige Nummern werden nicht im E.164-Format gespeichert, und der Zusammenführungsjob kombiniert diese Profile nicht. Der Endpunkt gibt dennoch `202 Accepted` mit einer Erfolgsmeldung zurück, sodass die HTTP-Antwort nicht darauf hinweist, dass die Zusammenführung übersprungen wurde. Korrigieren Sie die Telefonnummern in einem oder beiden Profilen, bevor Sie die Zusammenführung durchführen.
{% endalert %}

## Beispielanfragen {#example-requests}

### Einfache Anfrage {#basic-request}

Dies ist ein einfacher Anfragetext, der das Muster der Anfrage zeigt.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@example.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@example.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### Zusammenführung einer nicht identifizierten Nutzer:in {#merging-unidentified-user}

Die folgende Anfrage würde die zuletzt aktualisierte nicht identifizierte Nutzer:in mit der E-Mail-Adresse `john.smith@example.com` mit der Nutzer:in mit der externen ID `john` zusammenführen. In diesem Beispiel filtert `most_recently_updated` die Abfrage auf eine nicht identifizierte Nutzer:in. Wenn es also zwei nicht identifizierte Nutzer:innen mit dieser E-Mail-Adresse gäbe, würde nur eine mit der Nutzer:in zusammengeführt, die die externe ID `john` hat.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@example.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### Zusammenführung einer nicht identifizierten Nutzer:in in eine identifizierte Nutzer:in {#merging-unidentified-user-into-identified-user}

Das folgende Beispiel führt die zuletzt aktualisierte nicht identifizierte Nutzer:in mit der E-Mail-Adresse `john.smith@example.com` mit der zuletzt aktualisierten identifizierten Nutzer:in mit der E-Mail-Adresse `john.smith@example.com` zusammen.

Die Verwendung von `most_recently_updated` filtert die Abfragen auf jeweils eine Nutzer:in (eine nicht identifizierte Nutzer:in für `identifier_to_merge` und eine identifizierte Nutzer:in für `identifier_to_keep`).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@example.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@example.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### Zusammenführung einer nicht identifizierten Nutzer:in ohne die most_recently_updated-Priorisierung {#merging-an-unidentified-user-without-including-the-most_recently_updated-prioritization}

Wenn es zwei nicht identifizierte Nutzer:innen mit der E-Mail-Adresse `john.smith@example.com` gibt, führt diese Beispielanfrage keine Nutzer:innen zusammen, da es zwei nicht identifizierte Nutzer:innen mit dieser E-Mail-Adresse gibt. Diese Anfrage funktioniert nur, wenn es lediglich eine nicht identifizierte Nutzer:in mit der E-Mail-Adresse `john.smith@example.com` gibt.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@example.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## Antwort {#response}

Für diesen Endpunkt gibt es zwei Statuscode-Antworten: `202` und `400`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `202` könnte den folgenden Antworttext zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antworttext zurückgeben. Weitere Informationen zu Fehlern, die auftreten können, finden Sie unter [Fehlerbehebung](#troubleshooting).

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## Fehlerbehebung {#troubleshooting}

### Eine erfolgreiche Antwort wurde zurückgegeben, aber die zusammengeführte Nutzer:in ist weiterhin auffindbar {#a-success-response-was-returned-but-the-merged-user-is-still-searchable}

Eine erfolgreiche Antwort bestätigt, dass die Anfrage akzeptiert wurde, aber der Zusammenführungsvorgang umfasst zwei Schritte: das Zusammenführen der Profile und anschließend das Entfernen des Quellprofils. Aus diesem Grund kann das `identifier_to_merge`-Profil nach einer erfolgreichen Antwort noch für kurze Zeit im Dashboard auffindbar sein. Dies ist erwartetes Verhalten – warten Sie einige Minuten und überprüfen Sie dann, ob die Zusammenführung abgeschlossen ist.

Wenn die zusammengeführte Nutzer:in nach mehreren Minuten noch existiert, überprüfen Sie, ob die Bezeichner in Ihrer Anfrage korrekt sind und zu Nutzer:innen im selben Workspace gehören wie der für die Anfrage verwendete API-Schlüssel.

### Fehlerreferenz {#error-reference}

Die folgende Tabelle listet mögliche Fehlermeldungen auf, die auftreten können.

| Fehler | Fehlerbehebung |
| --- | --- |
| `'merge_updates' must be an array of objects` | Prüfen Sie, ob `merge_updates` ein Array von Objekten ist. |
| `a single request may not contain more than 50 merge updates` | Sie können in einer einzelnen Anfrage nur bis zu 50 Zusammenführungs-Updates angeben. |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | Überprüfen Sie die Bezeichner in Ihrer Anfrage. |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | Stellen Sie sicher, dass `merge_updates` nur die beiden Objekte `identifier_to_merge` und `identifier_to_keep` enthält. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

{% endapi %}