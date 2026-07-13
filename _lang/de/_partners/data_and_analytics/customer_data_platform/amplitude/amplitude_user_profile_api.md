---
nav_title: Amplitude und Connected-Content
article_title: Amplitude und Connected-Content
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "Die User-Profile-API von Amplitude stellt Amplitude-Nutzerprofile bereit. Dazu gehören Nutzereigenschaften, berechnete Nutzereigenschaften, eine Liste der Kohorten-IDs von Kohorten, die die Nutzer:innen enthalten, und Empfehlungen."
search_tag: Partner

---

# Amplitude und Connected-Content {#amplitude-and-connected-content}

> Die User-Profile-API von Amplitude stellt Amplitude-Nutzerprofile bereit. Dazu gehören Nutzereigenschaften, berechnete Nutzereigenschaften, eine Liste der Kohorten-IDs von Kohorten, die die Nutzer:innen enthalten, und Empfehlungen. Im Folgenden finden Sie eine Liste gängiger Amplitude-API-Endpunkte, die mit Connected-Content verwendet werden können.

## Endpunkt-Parameter {#endpoint-parameters}

Die folgende Tabelle enthält die Parameter, die Sie in Ihren Aufrufen der User-Profile-API verwenden können.

| Parameter | Erforderlich | Beschreibung |
| --------- | -------- | ----------- |
| `user_id` | Optional | Nutzer-ID (externe Datenbank-ID), die abgefragt werden soll. Erforderlich, sofern `device_id` nicht gesetzt ist. |
| `device_id` | Optional | Geräte-ID (anonyme ID), die abgefragt werden soll. Erforderlich, sofern `user_id` nicht gesetzt ist. |
| `get_recs` | Optional<br>(Standardmäßig false) | Gibt ein Empfehlungsergebnis für diese Nutzer:innen zurück. |
| `rec_id` | Optional | Abzurufende Empfehlung(en). Erforderlich, wenn `get_recs` true ist. Mehrere Empfehlungen können abgerufen werden, indem die `rec_ids` durch Kommas getrennt werden. |
| `rec_type` | Optional | Überschreibt die standardmäßige experimentelle Kontrolleinstellung. `rec_type=model` liefert modellierte Empfehlungen und `rec_type=random` liefert zufällige Empfehlungen. Weitere Optionen können in Zukunft verfügbar sein. |
| `get_amp_props` | Optional<br>(Standardmäßig false) | Gibt einen vollständigen Satz von Nutzereigenschaften für diese Nutzer:innen zurück, ohne Berechnungen. |
| `get_cohort_ids` | Optional<br>(Standardmäßig false) | Gibt eine Liste aller Kohorten-IDs zurück, zu denen diese Nutzer:innen gehören und die für das Tracking eingerichtet wurden. Standardmäßig wird die Kohortenzugehörigkeit für keine Kohorte getrackt. |
| `get_computations` | Optional<br>(Standardmäßig false) | Gibt eine Liste aller Berechnungen zurück, die für diese Nutzer:innen aktiviert sind. |
| `comp_id` | Optional | Gibt eine einzelne Berechnung zurück, die für diese Nutzer:innen aktiviert sein könnte. Es wird ein Nullwert zurückgegeben, wenn sie nicht existiert. Wenn `get_computations` true ist, werden alle Werte abgerufen, einschließlich dieses einen (sofern er nicht archiviert oder gelöscht wurde). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

Die folgende Tabelle enthält die Parameter, die Sie in der Regel in den Antworten von Amplitude erwarten können.

| Antwort-Parameter | Beschreibung |
| ------------------ | ----------- |
| `rec_id` | Die angeforderte Empfehlungs-ID. |
| `child_rec_id` | Eine detailliertere Empfehlungs-ID, die Amplitude im Backend als Teil eines internen Experiments verwenden kann, um die Performance des Modells zu verbessern. In den meisten Fällen ist dies identisch mit `rec_id`. |
| `items` | Liste der Empfehlungen für diese Nutzer:innen. |
| `is_control` | true, wenn diese Nutzer:innen zur Kontrollgruppe gehören. |
| `recommendation_source` | Name des Modells, das zur Erstellung dieser Empfehlung verwendet wurde. |
| `last_updated` | Zeitstempel, wann diese Empfehlung zuletzt erstellt und synchronisiert wurde. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

## Gängige Amplitude-Endpunkte {#common-amplitude-endpoints}

### Eine Empfehlung abrufen {#get-a-recommendation}

#### Endpunkt {#endpoint}
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### Beispielantwort {#example-response}
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Mehrere Empfehlungen abrufen {#get-multiple-recommendations}

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### Beispielantwort
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Nutzereigenschaften abrufen {#get-user-properties}

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### Beispielantwort
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### Kohorten-IDs abrufen {#get-cohort-ids}

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### Beispielantwort
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### Eine einzelne Berechnung abrufen {#get-a-single-computation}

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### Beispielantwort
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### Alle Berechnungen abrufen {#get-all-computations}

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### Beispielantwort
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

