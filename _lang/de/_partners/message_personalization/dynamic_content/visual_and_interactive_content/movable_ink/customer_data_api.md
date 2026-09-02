---
nav_title: Verbindung mit der Customer Data API
article_title: Verbindung mit der Movable Ink Customer Data API herstellen
description: "Dieser Referenzartikel beschreibt, wie Sie eine Verbindung herstellen, um in Braze gespeicherte Kunden-Event-Daten zu aktivieren und mit der Customer Data API personalisierte Inhalte in Movable Ink zu generieren."
page_type: partner
search_tag: Partner
---

# Verbindung mit der Movable Ink Customer Data API herstellen {#connect-to-the-movable-ink-customer-data-api}

> Die Integration der Customer Data API von Braze und Movable Ink ermöglicht es Marketern, in Braze gespeicherte Kunden-Event-Daten zu aktivieren, um personalisierte Inhalte in Movable Ink zu generieren.

Movable Ink kann Verhaltens-Events von Braze über die Customer Data API aufnehmen. Die Events werden in den Nutzerprofilen basierend auf der eindeutigen Nutzer-ID (UUID) gespeichert, die an Movable Ink übermittelt wird.

Weitere Informationen über Stories, die Movable Ink Customer Data API und darüber, wie Movable Ink Verhaltensdaten nutzt, finden Sie in den folgenden Support-Center-Artikeln:

- [Inhalte mit Verhaltensdaten unterstützen](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Customer Data API – Einführung und Leitfaden](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ: Customer Data API](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Movable Ink Konto | Ein Movable Ink Konto ist erforderlich, um diese Partnerschaft zu nutzen. |
| Movable Ink API-Zugangsdaten | Das Movable Ink Solutions-Team generiert API-Zugangsdaten für Sie. Die API-Zugangsdaten bestehen aus:{::nomarkdown}<ul><li>Einer Endpunkt-URL (an die die Daten gesendet werden)</li><li>Benutzername und Passwort (zur Authentifizierung der API)</li></ul>{:/} Falls gewünscht, kann Movable Ink den Benutzernamen und das Passwort als base64-kodierten Wert bereitstellen, der als Basic-Authorization-Header-Wert verwendet werden kann. |
| Payloads für Verhaltens-Events | Sie müssen Ihre Event-Payloads mit Ihrem Movable Ink Client Experience Team teilen. Weitere Informationen finden Sie unter [Event-Payloads mit Movable Ink teilen](#event-payloads). |
| Kreative Assets und Geschäftslogik | Sie müssen Movable Ink kreative Assets zur Verfügung stellen, einschließlich Adobe Photoshop (PSD)-Dateien, die Movable Ink zeigen, wie der Block erstellt werden soll, sowie ein Fallback-Bild. Außerdem müssen Sie die Geschäftslogik bereitstellen, die festlegt, wie und wann der vom Partner aktivierte Content-Block angezeigt werden soll. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Erstellen Sie eine Webhook-Campaign in Braze {#step-1-create-a-webhook-campaign-in-braze}

#### Schritt 1a: Erstellen Sie eine neue Campaign {#step-1a-create-a-new-campaign}

1. [Erstellen Sie in Braze eine Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook).
2. Geben Sie Ihrer Campaign einen Namen und eine optionale Beschreibung.
3. Wählen Sie als Template **Blank Template** aus.

#### Schritt 1b: Fügen Sie Ihre Customer Data API-Zugangsdaten hinzu {#step-1b-add-your-customer-data-api-credentials}

1. Geben Sie im Feld **Webhook URL** die Movable Ink Endpunkt-URL ein.

![Tab „Verfassen“ des Webhook-Composers in Braze mit der Movable Ink Endpunkt-URL und dem Anfrage-Body auf JSON-Schlüssel-Wert-Paare eingestellt.]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2. Wählen Sie den Tab **Einstellungen**.
3. Fügen Sie die folgenden Anfrage-Header als Schlüssel-Wert-Paare hinzu:

| Schlüssel | Wert |
| --- | --- |
| Content-Type | application/json |
| Authorization | Geben Sie die Basic-Authentifizierung ein, die Sie von Movable Ink erhalten haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1b: Customer Data API-Zugangsdaten hinzufügen" }

![Tab „Einstellungen“ des Webhook-Composers in Braze mit Schlüssel-Wert-Paaren für Content-Type und Authorization.]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### Schritt 1c: Konfigurieren Sie Ihren Payload {#step-1c-configure-your-payload}

1. Kehren Sie zum Tab **Verfassen** zurück.
2. Erstellen Sie für Ihren **Anfrage-Body** entweder einen eigenen Anfrage-Body mit JSON-Schlüssel-Wert-Paaren oder geben Sie Ihren Event-Payload als Rohtext ein. Beispiele für Standard-E-Commerce-Events finden Sie in den [Beispiel-Payloads](#sample-payloads).

![Tab „Verfassen“ des Webhook-Composers in Braze mit JSON-Schlüssel-Wert-Paaren für ID, Zeitstempel, Nutzer-ID und Event-Typ.]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### Schritt 1d: Testen Sie Ihren Webhook {#step-1d}

Sie müssen Ihrem Movable Ink Client Experience Team einen Beispiel-Payload zur Verfügung stellen. Sie können diesen Payload im Tab **Test** basierend auf dem von Ihnen erstellten Payload generieren.

{% alert important %}
Movable Ink empfiehlt, mit dem Testen Ihres Webhooks in Braze zu warten, bis Ihr Movable Ink Client Experience Team bestätigt hat, dass die Abbildung abgeschlossen ist und ein Test empfangen werden kann. Wenn diese Abbildung nicht vollständig ist, erhalten Sie beim Testen wahrscheinlich eine Fehlermeldung.
{% endalert %}

Um Ihren Webhook zu testen, gehen Sie wie folgt vor:

1. Wählen Sie den Tab **Test**.
2. Zeigen Sie eine Vorschau der Nachricht als Nutzer:in an, um einen Beispiel-Event-Payload für diese:n Nutzer:in zu sehen. Sie können zwischen einer Vorschau als zufällige:r Nutzer:in, bestimmte:r Nutzer:in oder angepasste:r Nutzer:in wählen.
3. Wenn alles gut aussieht, klicken Sie auf **Send test**, um eine Testanfrage zu senden.

![Webhook-Antwortnachricht in Braze mit einer 200-OK-Antwort.]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### Schritt 2: Schließen Sie die Einrichtung Ihrer Campaign ab {#step-2-finalize-your-campaign-setup}

#### Schritt 2a: Planen Sie Ihre Campaign {#step-2a-schedule-your-campaign}

Wenn Sie den Webhook fertiggestellt und getestet haben, [planen Sie Ihre Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Braze unterstützt geplante, aktionsbasierte und API-getriggerte Zustellungen. Die [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) ist in der Regel die beste Lösung für die meisten Anwendungsfälle mit Verhaltens-Events. Bei Fragen dazu, was für Ihren Anwendungsfall sinnvoll ist, wenden Sie sich an Ihre CSM or Customer-Success-Manager or Customer-Success-Manager:in von Braze und Movable Ink.

Für aktionsbasierte Zustellung:

1. Geben Sie die Trigger or triggern-Aktion an. Dies ist das Event, das den Webhook an Movable Ink triggert.
2. Stellen Sie sicher, dass **Schedule Delay** auf **Immediately** eingestellt ist. Event-Daten sollten sofort nach dem Eintreten des Events ohne Verzögerung an Movable Ink gesendet werden.
3. Legen Sie die Dauer der Campaign fest, indem Sie eine Startzeit angeben. Eine Endzeit ist wahrscheinlich nicht erforderlich, kann aber bei Bedarf für den Anwendungsfall festgelegt werden.

{% alert note %}
Um sicherzustellen, dass die Daten in Echtzeit an Movable Ink gestreamt werden, wählen Sie nicht die Option **Send campaign to users in their local time zone**.
{% endalert %}

#### Schritt 2b: Bestimmen Sie Ihre Zielgruppe {#step-2b-specify-your-audience}

Bestimmen Sie als Nächstes, welche Nutzer:innen Sie für diese Campaign ansprechen möchten. Einzelheiten finden Sie unter [Nutzer:innen ansprechen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users).

Stellen Sie sicher, dass Sie keine A/B-Tests in Ihrer Campaign verwenden, indem Sie das Kontrollkästchen **Control Group** deaktivieren. Wenn eine Kontrollgruppe enthalten ist, werden bei einem bestimmten Prozentsatz der Nutzer:innen keine Daten an Movable Ink gesendet. Ihre gesamte Zielgruppe sollte der Variante zugeordnet werden, nicht der Kontrollgruppe.

![A/B-Tests-Panel in einer Braze-Campaign mit 100 % Variantenverteilung für Variante 1 und ohne Kontrollgruppe.]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### Schritt 2c: Wählen Sie Konversions-Events (optional) {#step-2c-choose-conversion-events-optional}

Falls gewünscht, können Sie dieser Campaign innerhalb von Braze Konversions-Events zuweisen.

Da der Webhook jedoch nur zum Streamen von Daten gedacht ist, ist die Attribution auf dieser Ebene wahrscheinlich weniger nützlich als die Betrachtung der Attribution auf Campaign-Ebene, nachdem die Verhaltensdaten von Braze zur Personalisierung von Inhalten verwendet wurden.

### Schritt 3: Campaign starten {#step-3-launch-the-campaign}

Überprüfen Sie Ihre Webhook-Einrichtung und starten Sie Ihre Campaign.

## Überlegungen {#considerations}

### Abstimmung auf einen eindeutigen Nutzer-Bezeichner {#aligning-on-a-unique-user-identifier}

Stellen Sie sicher, dass der eindeutige Nutzer-Bezeichner (UUID), den Sie als `mi_u` verwenden, in Braze verfügbar ist und in die an Movable Ink gesendeten Event-Payloads aufgenommen werden kann.

Dadurch wird sichergestellt, dass die Verhaltens-Events, auf die Movable Ink bei der Erstellung eines Bildes referenziert, mit derselben Kund:in verknüpft sind, für die die Verhaltens-Events empfangen wurden. Wenn der UUID-Wert nicht mit der Braze `external_id` übereinstimmt, muss die UUID erfasst und als Attribut oder in den Event-Eigenschaften eines Braze-Events an Braze übergeben werden, um diesen Bezeichner zu nutzen.

Braze trackt das Nutzerverhalten über mehrere Plattformen hinweg (z. B. Internet und mobile App), sodass eine einzelne Nutzer:in mehrere verschiedene anonyme IDs haben kann. Diese IDs können in das einzige bekannte Stories-Kundenprofil or Nutzerprofil zusammengeführt werden, wenn ein `identify`-Event an Movable Ink gesendet wird, solange das `identify`-Event sowohl einen anonymen Bezeichner als auch den einzigen bekannten Bezeichner enthält.

Sobald Movable Ink eine `user_id` für eine einzelne Nutzer:in erhält, müssen alle zukünftigen Events für diese Nutzer:in dieselbe `user_id` enthalten.

### Event-Payloads mit Movable Ink teilen {#event-payloads}

Bevor Sie den Konnektor zur Customer Data API von Movable Ink einrichten, stellen Sie sicher, dass Sie Ihre Event-Payloads mit Ihrem Movable Ink Client Experience Team teilen. Dies ermöglicht Movable Ink die Abbildung Ihrer Events auf das Event-Schema und verhindert, dass API-Aufrufe abgelehnt werden oder fehlschlagen.

Sie können in Braze einen Event-Payload mit beliebigen Event-Eigenschaften erzeugen. Generieren Sie einen Beispiel-Payload für eine:n zufällige:n Nutzer:in oder durch die Suche nach einer bestimmten Nutzer-ID. Siehe [Schritt 1d](#step-1d) für Details.

Teilen Sie diesen Beispiel-Payload mit Ihrem Movable Ink Client Experience Team. Vergewissern Sie sich, dass keine sensiblen personenbezogenen Daten im Beispiel-Payload enthalten sind (wie z. B. E-Mail-Adresse, Telefonnummer oder vollständige Geburtsdaten).

Wenn Sie mehr über angepasste Event-Eigenschaften und das erwartete Format der in den Eigenschaften enthaltenen Daten erfahren möchten, lesen Sie [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

### Bekannte versus anonyme Nutzer:innen {#known-versus-anonymous-users}

In Braze können Events unter einem anonymen Kundenprofil or Nutzerprofil aufgezeichnet werden. Welche Bezeichner bei der Event-Protokollierung mit dem Kundenprofil or Nutzerprofil verknüpft werden, hängt davon ab, wie die Nutzer:in erstellt wurde (über das Braze SDK or Software-Development-Kit oder die APIs) und in welcher Phase des Nutzerlebenszyklus sich die Nutzer:in befindet.

#### Nur Braze-Events für bekannte Nutzer:innen weiterleiten {#only-forwarding-braze-events-for-known-users}

Verwenden Sie in Ihrer Webhook-Campaign den Filter `External User ID`, um nur Nutzer:innen anzusprechen, die eine `external_id` haben, mit dem Filter `External User ID` `is not blank`.

#### Braze-Events für anonyme und bekannte Nutzer:innen weiterleiten {#forwarding-braze-events-for-anonymous-and-known-users}

Wenn Sie Braze-Events von anonymen Nutzer:innen (Nutzer:innen, deren Profil noch keine `external_id` zugewiesen wurde) weiterleiten möchten, müssen Sie entscheiden, welchen Bezeichner Sie als `anonymous_id` für Movable Ink verwenden möchten, bis eine `external_id` verfügbar ist. Wählen Sie eine `anonymous_id`, die in Ihrem Braze-Kundenprofil or Nutzerprofil konstant bleibt. Sie können die Liquid-Logik im Webhook-Body verwenden, um zu entscheiden, ob eine `anonymous_id` oder eine `user_id` übergeben werden soll.

Weitere Informationen finden Sie in den Beispiel-Webhooks unter [Beispiel-Payloads](#sample-payloads).

## Beispiel-Payloads {#sample-payloads}

### Produktansichts-Event {#product-view-event}

{% tabs local %}
{% tab Example Braze Trigger or triggern Event %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@example.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

In diesem Beispiel wird eine gehashte E-Mail-Adresse als `anonymous_id` für Nutzer:innen verwendet, die keine `external_id` haben.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### Kategorieansichts-Event {#category-view-event}

{% tabs local %}
{% tab Example Braze Trigger or triggern Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Example webhook %}

Dieses Beispiel zeigt einen Webhook, der nur Events für bekannte Nutzer:innen trackt (Nutzer:innen mit einer `external_id`).

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### Identify-Event

{% tabs local %}
{% tab Example Braze Trigger or triggern Event %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Expected Movable Ink Request Payload %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Example webhook %}

In diesem Beispiel wird eine gehashte E-Mail-Adresse als `anonymous_id` für Nutzer:innen verwendet, die keine `external_id` haben.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}