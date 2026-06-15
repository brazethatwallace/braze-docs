---
nav_title: Treasure Data für Currents
article_title: Treasure Data für Currents
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und Treasure Data, einer Customer Data Platform (CDP) für Unternehmen, die es Ihnen erlaubt, Auftragsergebnisse direkt in Braze zu schreiben."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data für Currents {#treasure-data-for-currents}

> [Treasure Data](https://www.treasuredata.com/) ist eine Customer Data Platform (CDP), die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl anderer Standorte in Ihrem Marketing Stack weiterleitet.

Die Integration von Braze und Treasure Data erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit Currents können Sie Daten auch mit Treasure Data verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Treasure Data | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Treasure Data-Konto](https://console.treasuredata.com/users/sign_in). |
| Currents | Um Daten zurück in Treasure Data zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto einrichten lassen. |
| Treasure Data-URL | Diese erhalten Sie, indem Sie zu Ihrem Treasure Data-Dashboard navigieren und die Datenaufnahme-URL kopieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% alert note %}
Treasure Data protokolliert jedes Ereignis in Stapeln. Weitere Informationen darüber, wie Sie Treasure Data abfragen können, um die Anzahl der Ereignisse zu ermitteln, finden Sie unter [Daten abfragen](https://docs.treasuredata.com/articles/int/braze-currents-import-integration/a/h2__592056238).<br><br>Wenn Sie eine Integration mit dem neuen Braze-Streaming-Konnektor von Treasure Data anstreben, lesen Sie die detaillierten Einrichtungsschritte in [Braze Currents Streaming Import Integration](https://docs.treasuredata.com/articles/#!int/braze-currents-import-integration/q/braze/qid/72364/qp/4). Wenn Sie Fragen zur Integration oder Einrichtung innerhalb von Braze haben, wenden Sie sich an Ihr Braze-Kontoteam.
{% endalert %}

## Integration

Die empfohlene Methode zur Verbindung mit Treasure Data ist die Postback API. Für diese Methode ist kein Standardkonnektor erforderlich und die Daten können über einen Push-Ansatz empfangen werden. Alle in einem Datenstapel gesendeten Ereignisse befinden sich in einem Feld einer Zeile in einem JSON-Array, das geparst werden muss, um die gewünschten Daten zu erhalten.

{% alert important %}
Die Datenaufnahme in Treasure Data über den Event-Collector erfolgt derzeit nicht in Realtime und kann bis zu fünf Minuten dauern.
{% endalert %}

### 1. Schritt: Treasure Data Postback API mit Braze einrichten {#step-1-setup-treasure-data-postback-api-with-braze}

Eine Anleitung zur Erstellung einer Postback API finden Sie auf der [Website von Treasure Data](https://docs.treasuredata.com/display/public/PD/Postback+API). Braze sendet die aktualisierten Ereignisse direkt und in Realtime an Treasure Data, mit Ausnahme der Datenaufnahme durch den Event-Collector. Wenn Sie fertig sind, stellt Treasure Data eine Datenquellen-URL zur Verfügung, die Sie für den nächsten Schritt kopieren können.

### 2. Schritt: Current erstellen {#step-2-create-current}

Navigieren Sie in Braze zu **Currents** > **+ Create Current** > **Treasure Data Export**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail und Ihre Treasure Data-URL an. Wählen Sie dann aus der Liste der verfügbaren Ereignisse aus, was Sie tracken möchten, und klicken Sie auf **Launch Current**.

Alle Ereignisse, die an Treasure Data gesendet werden, enthalten die `external_user_id` der Nutzer:innen. Derzeit sendet Braze keine Ereignisdaten an Treasure Data für Nutzer:innen, die ihre `external_user_id` nicht festgelegt haben.

{% alert important %}
Halten Sie Ihre Treasure Data-URL auf dem neuesten Stand. Wenn die URL Ihres Konnektors falsch ist, kann Braze keine Ereignisse senden. Wenn dieser Zustand länger als **5 Tage** anhält, werden die Ereignisse des Konnektors verworfen und die Daten gehen dauerhaft verloren.
{% endalert %}

#### Beispiel für einen Ereignisfeldwert {#example-event-field-value}
```json
{
    "events": [
        {
            "event_type": "users.message.email.Open",
            "id": "a1234567-89ab-cdef-0123-456789abcdef",
            "time": 1477502783,
            "user": {
                "user_id": "user_id",
                "timezone": "America/Chicago"
        },
            "properties": {
                "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
                "campaign_name": "Test Campaign",
                "dispatch_id": "12345qwert",
                "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
                "email_address": "test@example.com",
                "send_id": "f123456789abcdef01234567",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
            }
        }
    ]
}
```

#### Beispiel für die aufgenommene Ansicht {#example-of-the-ingested-view}

![Beispiel für die aufgenommene Ansicht in Treasure Data][4]{: style="max-width:70%;"}

## Details zur Integration {#integration-details}

Braze unterstützt den Export aller Daten, die in den [Currents-Ereignisglossaren]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) aufgeführt sind (einschließlich aller Eigenschaften von [Nachrichten-Engagement-]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) und [Kundenverhalten-Ereignissen]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)), in Treasure Data.

Die Payload-Struktur für exportierte Daten entspricht der Payload-Struktur für angepasste HTTP-Konnektoren, die Sie im [Beispiel-Repository für angepasste HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.


[4]: {% image_buster /assets/img/treasure_data/treasure_data_ingested_view.png %}