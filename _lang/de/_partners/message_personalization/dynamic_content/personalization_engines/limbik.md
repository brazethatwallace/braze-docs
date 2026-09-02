---
nav_title: Limbik
article_title: Limbik
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Limbik, einer KI-Resonanzschicht, die mithilfe synthetischer Zielgruppen und Prognosen vorhersagt, wie Zielgruppen Nachrichten interpretieren und darauf reagieren."
alias: /partners/limbik/
page_type: partner
search_tag: Partner
---

# Limbik

> [Limbik](https://limbik.com/cognitive-ai) ist Ihre KI-Resonanzschicht – sie sagt vorher, wie reale Zielgruppen Nachrichten, Konzepte und KI-Ausgaben interpretieren und darauf reagieren, bevor diese den Markt erreichen. Gestützt auf kontinuierliche Primärforschung in über 60 Ländern und mehr als 25 Sprachen liefert Limbik menschlich validierte synthetische Zielgruppen – digitale Populationen, die reale Zielgruppenreaktionen mit Maschinengeschwindigkeit und forschungsgerechter Genauigkeit simulieren (95 % Konfidenz, 1,5 % bis 3 % Fehlermarge). Limbik gibt Ihnen die Möglichkeit, sofort sicherzustellen, dass Ihre Nachrichten mit den Überzeugungen und Gefühlen Ihrer Zielgruppe resonieren.

_Diese Integration wird von Limbik gepflegt._

## Voraussetzungen {#prerequisites}

Folgendes ist erforderlich, um Limbik mit Braze zu verwenden:

| Anforderungen | Beschreibung |
| --- | --- |
| Limbik `account_id` | Wenden Sie sich an Ihr Limbik-Kontoteam oder senden Sie eine GET-Anfrage an Limbiks `/rest/api/organizations`-Endpunkt. |
| Limbik-Zugriffstoken (`access_token`) | Senden Sie eine POST-Anfrage an Limbiks `login`-Endpunkt und verwenden Sie den zurückgegebenen `access_token`-Wert als Bearer-Token im `Authorization`-Header. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit „Messages“-Berechtigungen. Erstellen Sie einen im Braze-Dashboard unter **Settings** > **API Keys**. |
| Braze `campaign_id` | Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie eine Campaign aus. Falls die gewünschte Campaign noch nicht existiert, erstellen Sie eine und speichern Sie sie. Am Ende der Campaign-Seite finden Sie den Campaign-API-Bezeichner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

Bevor Sie einen der Prognose-Endpunkte verwenden, müssen Sie zunächst ermitteln, auf welche Organisation (`account_id`) Sie Zugriff haben. Während die meisten Kund:innen nur eine Organisation haben, stehen einigen Konten möglicherweise mehrere Organisationen zur Verfügung.

{% details Verfügbare Organisationen abrufen %}

Fragen Sie den Organisations-Endpunkt ab, um Ihre verfügbaren Organisationen abzurufen:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/organizations' \
  -H 'accept: application/json'
```

{% enddetails %}

{% details Beispielantwort %}

```json
{
  "data": [
    {
      "uid": "aca61bd5-7132-499c-946e-42d092cc1156",
      "name": "Braze API"
    }
  ]
}
```

Wählen Sie die `uid` Ihrer gewünschten Organisation aus, um sie als `account_id`-Header in allen nachfolgenden API-Anfragen zu verwenden.

{% enddetails %}

## Authentifizierung {#authentication}

Um auf die API-Endpunkte zuzugreifen, benötigen Sie ein Bearer-Token zur Authentifizierung. Erhalten Sie Ihr Token, indem Sie sich mit Ihren Zugangsdaten authentifizieren.

{% details Anmeldeanfrage %}

```sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/auth/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "your_username",
  "password": "your_password"
}'
```

{% enddetails %}

{% details Beispielantwort %}

Die Antwort enthält ein `access_token`, das Sie als Bearer-Token in allen nachfolgenden API-Anfragen verwenden können:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer"
}
```

Fügen Sie dieses Token im `Authorization`-Header für alle API-Anfragen ein:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

{% alert note %}
Sie können API-Plattformen wie Postman verwenden, um automatisierte Workflows einzurichten, die mehrere REST-API-Endpunkte verschiedener Organisationen aufrufen, wie den folgenden Workflow.
{% endalert %}

{% enddetails %}

## Anwendungsfall – Nachrichtentext generieren {#use-case-generating-message-copy}

Durch die Nutzung der REST-API-Endpunkte von Braze und Limbik können Sie Limbiks generative Prognosen verwenden, um Nachrichtentext zu erstellen und über Braze-Messaging-Kanäle zu versenden, oder bestehenden Text anzupassen, um die Wirkung bei Ihrer Zielgruppe zu verbessern. Beide Plattformen stellen Funktionalitäten bereit, die Sie programmatisch aufrufen können, um anspruchsvolle Workflows zu erstellen.

Diese Dokumentation beschreibt zwei Beispiele: die Generierung von Nachrichtentext in Limbik und die Verwendung dieses Textes in einer anschließend über Braze versendeten Nachricht sowie die Nutzung von Limbik zur Bewertung der Qualität einer bestimmten Nachricht für Ihre gewählte Zielgruppe.

{% details Limbik-Anfrage für generative Prognose %}

Verwenden Sie diesen Endpunkt, um eine Nachricht zu generieren und in einem Prognose-Template zurückzugeben. Beispielanfrage:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/generate/template?prompt=YOUR_PROMPT' \
  -H 'account_id: YOUR_ACCOUNT_ID' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'accept: application/json'
```

Ersetzen Sie `YOUR_PROMPT`, `YOUR_ACCOUNT_ID` und `YOUR_ACCESS_TOKEN` durch Ihren Prompt-Text, die Organisations-ID (vom Organisations-Endpunkt) und das Bearer-Token vom Anmelde-Endpunkt.

{% enddetails %}

{% details Beispielantwort %}

Beispiel einer Limbik-Prognose-Template-Antwort:

```json
[
  {
    "type": "Message",
    "displayText": "Formula one next race",
    "additionalDetail": "The latest dev in Formula...",
    "messages": [
      {
        "body": "The latest dev in Formula ..."
      }
    ],
    "population": {
      "id": 56,
      "name": "us2",
      "org_enabled": true,
      "org_visible": true,
      "categories": [],
      "display_name": "US Adults",
      "composite_key": "us2",
      "enabled": true
    }
  }
]
```

Das Schlüsselelement für diesen Anwendungsfall ist das Feld `additionalDetail`, das den von Limbik generierten Nachrichtentext enthält.

Verwenden Sie diesen Wert, um eine an Braze gesendete Nachricht zu befüllen. Beispielsweise können Sie beim POST-Endpunkt `/campaigns/trigger/send` das Feld `additionalDetail` verwenden, um ein Payload-Feld zu befüllen. Beim POST-Endpunkt `/messages/send` verwenden Sie es, um das Nachrichtenobjekt Ihrer Wahl zu befüllen.

{% enddetails %}

### Antwortfelder {#response-fields}

Die Antwort enthält die folgenden Schlüsselfelder:

- **`type`:** Der Nachrichtentyp (zum Beispiel `"Generate"` für KI-generierte Inhalte, `"Message"` für validierte Nachrichten)
- **`displayText`:** Ein kurzer Titel oder eine Zusammenfassung der Nachricht
- **`additionalDetail`**: **Der vollständige KI-generierte Nachrichtentext** – Dies ist das primäre Feld mit dem vollständigen Nachrichtentext, den Sie über Ihre Messaging-Plattform versenden können
- **`population`:** Die Zielpopulation und Segmente für diese Nachricht

### Verwendung mit Braze {#using-with-braze}

Das Feld `additionalDetail` aus Limbiks Antwort enthält den Nachrichtentext, den Sie an Braze senden. Ein gängiges Integrationsmuster besteht darin, diesen Wert in `trigger_properties.payload` zu übergeben, wenn Sie den Braze-Trigger-Send-Endpunkt aufrufen. Ersetzen Sie im folgenden Beispiel `{{additionalDetail}}` durch den tatsächlichen String aus Limbiks `additionalDetail`-Feld und `{{YOUR_CAMPAIGN_ID}}` durch Ihre Campaign-ID.

### Beispiel einer Braze-Trigger-Nachrichtenanfrage {#braze-trigger-message-request-example}

```json
{
  "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
  "trigger_properties": {
    "payload": "{{additionalDetail}}"
  },
  "broadcast": true
}
```

## Anwendungsfall – Details zu synthetischen Zielgruppen {#use-case-synthetic-audience-details}

Aufbauend auf dem ersten Anwendungsfall verwenden Sie Limbiks Endpunkt `/rest/api/populations/{account_id}/{population_id}`.

Dieser Endpunkt gibt wichtige Datenpunkte zurück, die die Zusammensetzung von Limbiks synthetischen Zielgruppen beschreiben, wie Geschlecht, Standort und so weiter. Sie können diese Werte verwenden, um Connected-Audience-Objekte zu befüllen, wenn Sie Braze-Messaging-Endpunkte aufrufen.

{% alert note %}
Connected-Audience-Objekte können Nutzer:innen nicht anhand von Braze-Standardattributen ansprechen, daher müssen Sie alle Attribute, die Sie ansprechen möchten, als angepasste Attribute in Braze speichern.
{% endalert %}

Um Prognosewerte für bestimmte Segmente zu erhalten, identifizieren Sie die verfügbaren Länder und ihre entsprechenden Segmente.

### 1. Schritt: Verfügbare Länder auflisten {#step-1-list-available-countries}

Rufen Sie die Liste der für Ihr Konto verfügbaren Länder ab:

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/list/aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'accept: application/json'
```

Identifizieren Sie aus der Antwort das gewünschte Land. Beispielsweise haben die Vereinigten Staaten eine `id` von `56`.

### 2. Schritt: Verfügbare Segmente abrufen {#step-2-retrieve-available-segments}

Nachdem Sie die Länder-ID abgerufen haben, rufen Sie die vollständige Liste der Segmente für dieses Land ab.

{% details Beispielaufruf %}

```sh
curl -X 'GET' \
  'https://cortex.prod.limbik.com/rest/api/populations/aca61bd5-7132-499c-946e-42d092cc1156/56' \
  -H 'accept: application/json'
```

{% alert note %}
Die Antwort kann umfangreich sein. Cachen Sie diese Daten (zum Beispiel in Redis) nach Name oder Schlüssel für bessere Performance.
{% endalert %}

{% enddetails %}

{% details Beispielantwort %}

Um beispielsweise Frauen in der US-Erwachsenenpopulation anzusprechen:

```json
[
  {
    "id": 56,
    "name": "us2",
    "composite_key": "us2",
    "categories": [
      {
        "id": 9331,
        "name": "gender",
        "composite_key": "us2::gender",
        "segments": [
          {
            "id": 63793,
            "name": "female",
            "composite_key": "us2::gender::female"
          }
        ]
      }
    ]
  }
]
```

{% alert note %}
- Segmente werden mit einem vereinfachten Composite-Key-Format angegeben (zum Beispiel `gender::female`).
- Der vollständige Composite Key aus der API-Antwort (`us2::gender::female`) wird auf den Kategorie- und Segmentnamen verkürzt.
- Eine vollständige Referenz der verfügbaren Populationen und Segmente finden Sie unter [Limbik-Zielgruppen](https://audiences.limbik.com/).
{% endalert %}

Mithilfe des Composite-Key-Werts für Ihre gewählte Prognosenachricht können Sie diese synthetischen Zielgruppenbeschreibungen auf Werte realer Nutzerprofile in Braze abbilden.

Beispielsweise können Sie den Composite Key (`fr1::education_level::master_s_degree`) in einem Braze-Connected-Audience-Objekt wie folgt verwenden:

```json
{
  "AND": [
    {
      "custom_attribute": {
        "custom_attribute_name": "education_level",
        "comparison": "equals",
        "value": "masters"
      }
    }
  ]
}
```

{% enddetails %}

## Anwendungsfall – Prognosewert auswerten {#use-case-evaluating-forecast-score}

Sie können Limbik verwenden, um einen geschätzten Score für eine Nachricht gegenüber einer synthetischen Zielgruppe zu erstellen. Tun Sie dies programmatisch mit Limbiks `forecasts/synchronous`-Endpunkt.

### Option 1 – Synchrone Prognose {#option-1-synchronous-forecast}

Sie können die Antwort-Payload aus der Template-Generierung direkt mit dem synchronen Prognose-Endpunkt verwenden:

{% details Beispiel einer generischen Anfrage %}

```sh
curl -X 'POST' \
  'https://cortex.prod.limbik.com/rest/api/forecasts/synchronous' \
  -H 'accept: application/json' \
  -H 'account_id: aca61bd5-7132-499c-946e-42d092cc1156' \
  -H 'Content-Type: application/json' \
  -d '{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "Day 1 of the 2026 Formula 1 Bahrain testing session has concluded. Lando Norris recorded the fastest time in the McLaren, with Ferrari in second place. Cadillac drivers Sergio Perez and Valtteri Bottas completed 107 laps, nearly two race distances, and Audi introduced significant upgrades. Which team do you expect to perform best in Australia? #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": []
  }
}'
```

{% enddetails %}

{% details Beispielantwort (gekürzt) %}

```json
{
  "uid": "6c5e28ef-8796-4659-a743-d842a06c9bf7",
  "datetime": "2026-02-11T20:04:06.545+00:00",
  "userId": "9cdd921c-f62f-46a6-902f-a6b0d1702f99",
  "accountId": "aca61bd5-7132-499c-946e-42d092cc1156",
  "name": "Formula one season t...",
  "user_message_context": "",
  "population": [
    {
      "name": "us2",
      "display_name": "US Adults",
      "categories": []
    }
  ],
  "privacy_compliant": false,
  "model_outputs": {
    "belmetrics": {
      "metrics": {
        "moe": 0.02144,
        "pfi": "0.3611",
        "min_val": 0.2941,
        "mean_val": 0.41831
      }
    },
    "virmetrics": {
      "metrics": {
        "moe": 0.02381,
        "pfi": "0.3611",
        "min_val": 0.2,
        "mean_val": 0.30395
      }
    },
    "model_variant": "v4_0_0"
  }
}
```

{% enddetails %}

### Option 2: Prognose-Payload mit Segmenten vorbereiten {#option-2-prepare-forecast-payload-with-segments}

Erstellen Sie Ihre Prognose-Payload mit den ausgewählten Segmenten. Segmente verwenden ein vereinfachtes Composite-Key-Format.

{% details Beispiel einer segmentspezifischen Anfrage %}

```json
{
  "type": "Generate",
  "displayText": "Formula one season testing 2026",
  "additionalDetail": "🚀 Day 1 of 2026 F1 Bahrain testing just dropped BOMBS! Lando Norris edged out Max Verstappen for P1 in McLaren's beast, with Ferrari hot on their heels 🔥. But the real shocker? Cadillac's debutants Sergio Perez & Valtteri Bottas smashed 107 laps – nearly TWO race distances! New kids on the block are HERE to stay. Audi's radical upgrades already turning heads too. Who's your early fave for Australia? 👀 #F12026 #BahrainTesting #LandoNorris",
  "population": {
    "population": "us2",
    "segments": [
      "gender::female"
    ]
  }
}
```

{% enddetails %}