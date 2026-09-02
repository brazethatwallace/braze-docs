---
nav_title: "Verbundener Zielgruppen-Filter und -Objekt"
article_title: API Verbundenes Zielgruppen-Objekt
page_order: 3
page_type: reference
description: "Dieser Artikel erklärt das verbundene Zielgruppen-Objekt, einschließlich seiner Funktionsweise, Anwendungsfälle und der verschiedenen Filter, aus denen es besteht."
---

# Verbundenes Zielgruppen-Objekt {#connected-audience-object}

> Ein verbundener Zielgruppen-Filter ist ein dynamischer Zielgruppenfilter, den Sie direkt in Ihrer API-Anfrage definieren. So können Sie zum Sendezeitpunkt die richtigen Nutzer:innen ansprechen, ohne Segmente im Braze-Dashboard erstellen oder verwalten zu müssen.

Anstatt für jede mögliche Zielgruppenkombination vorab ein Segment zu erstellen, übergeben Sie die Filterkriterien direkt in Ihrem API-Aufruf. Je nach Endpunkt wird dieses Objekt als `audience` oder `custom_audience` übergeben. Braze wertet jede:n Nutzer:in in Realtime anhand dieser Kriterien aus und stellt die Nachricht nur an Nutzer:innen zu, die den Kriterien entsprechen. Das bedeutet, dass eine einzelne Campaign, ein Canvas oder eine reine API-Nachrichtendefinition eine unbegrenzte Anzahl von Zielgruppenvarianten bedienen kann – vollständig gesteuert durch Ihre Geschäftslogik.

## So funktioniert es {#how-it-works}

1. Definieren Sie Ihre Nachricht, indem Sie entweder eine API-getriggerte Campaign oder ein Canvas im Braze-Dashboard erstellen, oder definieren Sie den Nachrichteninhalt vollständig inline mithilfe der [Messaging-Objekte]({{site.baseurl}}/api/objects_filters#messaging-objects) in Ihrer API-Anfrage. Verwenden Sie [Trigger-Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object) oder [Canvas-Kontext]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) für dynamische Personalisierung.
2. Rufen Sie einen unterstützten Endpunkt auf und fügen Sie Ihre Connected-Audience-Filter im Parameter `audience` ein, oder in `custom_audience` für `/messages/live_activity/start`. Sie können nach angepassten Attributen, Push-Abo-Status, E-Mail-Abo-Status und letzter App-Nutzungszeit filtern.
3. Braze wertet die Filter zum Sendezeitpunkt aus und stellt die Nachricht nur an Nutzer:innen zu, die Ihren Kriterien entsprechen.

{% alert tip %}
Eine `campaign_id` ist nicht erforderlich, wenn Sie den Parameter `audience` verwenden. Die Endpunkte [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) und [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) ermöglichen es Ihnen, Nachrichteninhalte inline zu definieren, ohne eine vorab erstellte Campaign. Wenn Sie jedoch Campaign-bezogene Metriken (wie Sends, Klicks oder Bounces) im Dashboard verfolgen möchten, fügen Sie eine `campaign_id` hinzu.
{% endalert %}

Da die Zielgruppe pro Anfrage definiert wird, können Ihre Backend-Systeme kontextuell relevante Nachrichten als Reaktion auf jedes Geschäftsereignis (eine Preisänderung, eine Wetterwarnung, ein Live-Ergebnis-Update) auslösen – ohne Eingriff über das Dashboard.

### Kompatible Endpunkte {#compatible-endpoints}

Sie können das Connected-Audience-Objekt an diesen Endpunkten verwenden:

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases)
- [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start) (verwendet `custom_audience`)

Beachten Sie, dass der Parameter `audience` kein Array von Objekten unterstützt.

## Anwendungsfälle {#use-cases}

Verwenden Sie Connected Audiences für Szenarien, in denen Ihre Backend-Systeme ein Event erkennen und eine dynamisch bestimmte Gruppe von Nutzer:innen benachrichtigen müssen:

| Kategorie | Beispiel |
| --- | --- |
| Wetterwarnungen | Ein Wetterdatenanbieter erkennt ein schweres Wetterereignis und sendet Push-Benachrichtigungen an Nutzer:innen, deren Attribut `preferred_city` mit dem betroffenen Gebiet übereinstimmt. |
| Sport und Live-Events | Eine Sport-App sendet Realtime-Spielstandaktualisierungen oder Spielbenachrichtigungen an Nutzer:innen, deren Attribut `favorite_team` mit einem der spielenden Teams übereinstimmt. |
| Inhalte und Unterhaltung | Ein Streaming-Dienst benachrichtigt Nutzer:innen, deren Array `favorite_shows` einen Serientitel enthält, sobald eine neue Folge veröffentlicht wird. |
| E-Commerce | Ein Online-Händler sendet Preissenkungen- oder Wieder-verfügbar-Benachrichtigungen an Nutzer:innen, deren Array `wishlisted_products` die relevante Produkt-ID enthält. |
| Reisen | Eine Reise-App sendet Flugverspätungsbenachrichtigungen an Nutzer:innen, deren Attribut `booked_flight` mit der betroffenen Flugnummer übereinstimmt. |
| Finanzdienstleistungen | Eine Handelsplattform benachrichtigt Nutzer:innen, deren Array `watchlist` ein Aktiensymbol enthält, das eine Preisschwelle überschritten hat. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

In jedem Fall deckt eine einzelne Campaign oder eine reine API-Nachrichtendefinition alle Variationen ab. Ihr Backend bestimmt die Filterwerte und übergibt sie in der API-Anfrage, sodass Sie nicht für jedes Produkt, jede Sendung, jedes Team oder jeden Standort ein separates Segment oder eine separate Campaign erstellen müssen.

## Beispielanfrage {#example-request}

Das folgende Beispiel verwendet den Endpunkt [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns), um Nutzer:innen anzusprechen, die eine bestimmte Show als Favorit markiert haben und für Push-Benachrichtigungen angemeldet sind:

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## Objektkörper {#object-body}

Das Connected-Audience-Objekt besteht entweder aus einem einzelnen Connected-Audience-Filter oder aus mehreren Connected-Audience-Filtern, die mit den Operatoren `AND` und `OR` kombiniert werden.

**Beispiel mit mehreren Filtern:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Verknüpfte Zielgruppenfilter {#connected-audience-filters}

Kombinieren Sie mehrere Filter mit den Operatoren `AND` und `OR`, um einen verknüpften Zielgruppenfilter zu erstellen.

### Überlegungen {#considerations}

Verknüpfte Zielgruppen können Nutzer:innen nicht nach folgenden Kriterien filtern:

 - Standardattribute
 - Angepasste Events
 - Segments
 - Nachrichten-Engagement-Events
 - Verschachtelte angepasste Attribute

Um diese Filter zu verwenden, empfehlen wir, sie in ein Zielgruppen-Segment einzubinden und dieses Segment dann im Parameter `segment_id` für den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters) anzugeben. Bei der Verwendung anderer Endpunkte müssen Sie das Segment zunächst der API-getriggerten Campaign oder dem Canvas im Braze-Dashboard hinzufügen. Wenn Sie nach verschachtelten Attributen filtern müssen, verwenden Sie stattdessen ein [Standard-Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment).


### Filter für angepasste Attribute {#custom-attribute-filter}

Dieser Filter ermöglicht die Segmentierung basierend auf einem angepassten Attribut einer Nutzerin oder eines Nutzers. Diese Filter enthalten bis zu drei Felder:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Zulässige Vergleiche nach Datentyp {#allowed-comparisons-by-data-type}

Der Datentyp des angepassten Attributs bestimmt, welche Vergleiche für einen bestimmten Filter gültig sind.

| Typ des angepassten Attributs | Zulässige Vergleiche |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist`, `is_any_of`, `is_none_of` |
| Numeric | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolean | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Time | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Zulässige Vergleiche nach Datentyp" }

#### Hinweise zu Attributvergleichen {#attribute-comparison-caveats}

| Vergleich | Weitere Hinweise |
| --- | --- |
| `value` | Der `value` ist bei Verwendung der Vergleiche `exists` oder `does_not_exist` nicht erforderlich. `value` muss ein ISO-8601-Datetime-String sein, wenn die Vergleiche `before` und `after` verwendet werden. |
| `matches_regex` | Bei Verwendung des Vergleichs `matches_regex` muss der übergebene Wert ein String sein. Weitere Informationen zur Verwendung regulärer Ausdrücke mit Braze finden Sie unter [Reguläre Ausdrücke]({{site.baseurl}}/user_guide/audience/segments/regex) und [Datentypen angepasster Attribute]({{site.baseurl}}/developer_guide/analytics#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Hinweise zu Attributvergleichen" }

#### Mehrwert-Vergleiche {#multi-value-comparisons}

Sowohl `is_any_of` als auch `is_none_of` unterstützen den Abgleich mit mehreren Werten in einem einzelnen Vergleich. Diese Vergleiche funktionieren sowohl mit String- als auch mit Array-Attributen.

- `is_any_of`: Gleicht Nutzer:innen ab, deren Attributwert einem der angegebenen Werte entspricht. Der `value` kann ein einzelner String oder ein String-Array sein.
- `is_none_of`: Gleicht Nutzer:innen ab, deren Attributwert keinem der angegebenen Werte entspricht. Der `value` kann ein einzelner String oder ein String-Array sein. Beachten Sie, dass Nutzer:innen ohne dieses Attribut in ihrem Profil immer für diesen Vergleich qualifiziert sind.

Für Array-Attribute:

- `includes_value` kann ebenfalls ein Array von Werten akzeptieren, um zu prüfen, ob das Array der Nutzerin oder des Nutzers einen der angegebenen Werte enthält.
- Bei der Verwendung von `is_any_of` oder `is_none_of` mit Array-Attributen funktionieren diese genauso wie `includes_value` bzw. `does_not_include_value`.

{% alert tip %}
Verwenden Sie für den Abgleich mit mehreren Werten `is_any_of` anstelle von `includes_value`.
{% endalert %}

#### Beispiele für angepasste Attribute {#custom-attribute-examples}

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```

#### Beispiele für Mehrwert-Vergleiche {#multi-value-comparison-examples}

##### `is_any_of` mit einem String-Array {#is_any_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_color",
    "comparison": "is_any_of",
    "value": ["red", "blue", "green"]
  }
}
```

##### `is_none_of` mit einem String-Array {#is_none_of-with-an-array-of-strings}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscription_tier",
    "comparison": "is_none_of",
    "value": ["bronze", "silver"]
  }
}
```

##### `includes_value` mit einem Array (Array-Attribut) {#includes_value-with-an-array-array-attribute}

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "subscribed_products",
    "comparison": "includes_value",
    "value": ["1001", "1002", "1003"]
  }
}
```

Dies gleicht Nutzer:innen ab, deren `subscribed_products`-Array einen der Werte `"1001"`, `"1002"` oder `"1003"` enthält.

### Push-Abo-Filter {#push-subscription-filter}

Dieser Filter ermöglicht die Segmentierung basierend auf dem Push-Abo-Status einer Nutzerin oder eines Nutzers.

#### Filtertext {#filter-body}

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Zulässige Vergleiche:** `is`, `is_not`
- **Zulässige Werte:** `opted_in`, `subscribed`, `unsubscribed`

### E-Mail-Abo-Filter {#email-subscription-filter}

Dieser Filter ermöglicht die Segmentierung basierend auf dem E-Mail-Abo-Status einer Nutzerin oder eines Nutzers.

#### Filtertext

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Zulässige Vergleiche:** `is`, `is_not`
- **Zulässige Werte:** `opted_in`, `subscribed`, `unsubscribed`

### Filter für letzte App-Nutzung {#last-used-app-filter}

Dieser Filter ermöglicht die Segmentierung basierend darauf, wann die Nutzerin oder der Nutzer die App zuletzt verwendet hat. Diese Filter enthalten zwei Felder:

#### Filtertext

```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Zulässige Vergleiche:** `after`, `before`
- **Zulässige Werte:** Datetime (ISO-8601-String)