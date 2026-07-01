---
nav_title: Tabelleneinrichtung
article_title: Cloud-Datenaufnahme – Tabelleneinrichtung
toc_headers: h2
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie Ihre CDI-Quelltabelle einrichten und wie sich diese Einrichtung von den Anforderungen an die Payload-Formatierung unterscheidet."
---

# Cloud-Datenaufnahme – Tabelleneinrichtung {#cloud-data-ingestion-table-setup}

> Verwenden Sie diese Seite, um zwei verwandte, aber unterschiedliche Anforderungen für die Cloud-Datenaufnahme (CDI) voneinander abzugrenzen: die Einrichtung der Quelltabelle und die Payload-Formatierung.

## Tabelleneinrichtung im Vergleich zur Payload-Formatierung {#understand-table-setup-compared-to-payload-formatting}

Für CDI-Nutzerdaten-Syncs konfigurieren Sie beides:

| Ebene | Was sie steuert |
| --- | --- |
| Einrichtung der Quelltabelle | Erforderliche Spalten, Nutzer-Bezeichner und `UPDATED_AT`-Sync-Verhalten |
| Payload-Formatierung | JSON-Felder in `PAYLOAD`, einschließlich Objektstruktur für Attribute, Ereignisse und Käufe |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tabelleneinrichtung im Vergleich zur Payload-Formatierung" }

Braze liest zuerst die Zeilen aus Ihrer Quelltabelle und validiert dann das `PAYLOAD`-Feld basierend auf dem ausgewählten Datentyp.

## Quelltabelle einrichten {#set-up-your-source-table}

Für Data-Warehouse-Nutzerdaten-Syncs sollte Ihre Quelltabelle oder -ansicht Folgendes enthalten:

- `UPDATED_AT`
- `PAYLOAD`
- Eine oder mehrere unterstützte Nutzer-Bezeichner-Spalten:
  - `EXTERNAL_ID`
  - `ALIAS_NAME` und `ALIAS_LABEL`
  - `BRAZE_ID`
  - `EMAIL`
  - `PHONE`

Jede Zeile sollte jeweils nur einen Bezeichnertyp enthalten, auch wenn Ihre Tabelle mehrere Bezeichner-Spalten enthält.

### `UPDATED_AT`-Anforderungen {#updated_at-requirements}

- Speichern Sie `UPDATED_AT`-Werte in UTC, um Probleme mit der Sommerzeit zu vermeiden.
- Braze synchronisiert Zeilen, bei denen `UPDATED_AT` später als der zuletzt synchronisierte Wert ist.
- Zeilen am exakten Grenz-Zeitstempel können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen.

Hinweise zu doppelten Zeitstempeln und inkrementellen Updates finden Sie unter [Best Practices für die Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#avoid-resyncing-rows-with-duplicate-timestamps).

{% alert note %}
Dateispeicher-Quellen verwenden andere Einrichtungsanforderungen und unterstützen `UPDATED_AT` nicht. Weitere Informationen finden Sie unter [Dateispeicher-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#required-file-formats).
{% endalert %}

## `PAYLOAD`-Spalte einrichten {#set-up-the-payload-column}

Der `PAYLOAD`-Wert folgt denselben Objektformaten, die vom Braze-Endpunkt `/users/track` für den ausgewählten Datentyp verwendet werden.

| Datentyp | Formatierungsreferenz |
| --- | --- |
| `attributes` | [Nutzerattribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens) |
| `events` | [Ereignis-Objekt]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="PAYLOAD-Spalte einrichten" }

Für verschachtelte Attribute geben Sie Datumsangaben im Format an, das unter [Datumsangaben als Objekteigenschaften erfassen]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#capturing-dates-as-object-properties) beschrieben ist.

### Payload-Beispiele {#payload-examples}

{% tabs local %}
{% tab Verschachtelte angepasste Attribute %}
Sie können verschachtelte angepasste Attribute in der Payload-Spalte für einen Sync angepasster Attribute einschließen.

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab Ereignis %}
Um Ereignisse zu synchronisieren, ist ein Ereignisname erforderlich. Formatieren Sie das `time`-Feld als ISO-8601-String oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Wenn das `time`-Feld nicht vorhanden ist, verwendet Braze den Wert der `UPDATED_AT`-Spalte als Ereigniszeit. Andere Felder, einschließlich `app_id` und `properties`, sind optional.

Sie können ein Ereignis pro Zeile synchronisieren.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Alex Smith"
    }
}
```

{% endtab %}
{% tab Kauf %}
Um Kauf-Events zu synchronisieren, sind `product_id`, `currency` und `price` erforderlich. Formatieren Sie das optionale `time`-Feld als ISO-8601-String oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. Wenn das `time`-Feld nicht vorhanden ist, verwendet Braze den Wert der `UPDATED_AT`-Spalte als Ereigniszeit. Andere Felder, einschließlich `app_id`, `quantity` und `properties`, sind optional.

Sie können ein Kauf-Event pro Zeile synchronisieren.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
        ]
    }
}
```

{% endtab %}
{% tab Abo-Gruppen %}
Um Abo-Gruppenstatus zu synchronisieren, fügen Sie in jeder Zeile ein oder mehrere Paare aus `subscription_group_id` und `subscription_state` ein.
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

## Verwandte CDI-Einrichtungsdokumente {#related-cdi-setup-docs}

- Quellenspezifische DDL-Beispiele finden Sie unter [Data-Warehouse-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views).
- Informationen zur dateibasierten Einrichtung finden Sie unter [Dateispeicher-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations).
- Hinweise zum Sync-Verhalten und zur Optimierung finden Sie unter [Best Practices für die Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices).