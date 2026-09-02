---
nav_title: Anwendungsfälle
article_title: Anwendungsfälle für Braze-Datentransformation
page_order: 2
page_type: reference
description: "Dieser Referenzartikel enthält einige Anwendungsfälle für die Braze-Datentransformation."
---

# Anwendungsfälle für die Datentransformation {#data-transformation-use-cases}

> Betrachten Sie die folgenden möglichen Anwendungsfälle mit der Braze-Datentransformation und einer Kombination aus Webhooks von den beispielhaften externen Plattformen.

## Leads generieren {#generating-leads}

Sie hosten ein Typeform-Formular zur Lead-Generierung auf Ihrer Website. Wenn neue Nutzer:innen dieses Formular ausfüllen, können Sie:
- Neue Nutzer:innen in Braze erstellen.
- Sie zu einer Ihrer Braze-E-Mail-Listen hinzufügen.
- Einige ihrer Antworten als angepasste Attribute in Braze synchronisieren, da ihre Antworten wertvolle First-Party-Daten sind, die in Zukunft personalisierte Messaging-Erlebnisse ermöglichen können.

## Service-Tickets eröffnen {#opening-service-tickets}

Wenn Kund:innen Service-Tickets auf einer Plattform wie Zendesk eröffnen, können Sie:
- Ein angepasstes Event in Braze schreiben, wenn ein Zendesk-Ticket erstellt wird.
- Ein angepasstes Event mit Event-Eigenschaften in Braze schreiben, wenn eine negative CSAT-Bewertung an Zendesk übermittelt wird.

## Integration mit Braze {#integrating-with-braze}

Braze verfügt über eine Integration mit [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate), einer Plattform für Insights und Umfragen. Mit der Datentransformation können Sie mehrere Umfrageantworten unter einem verschachtelten angepassten Attribut speichern, anstatt wie bei der bestehenden Integration mehrere angepasste Attribute zu speichern.

## HubSpot-Kontaktattribute synchronisieren {#sync-hubspot-contact-attributes}

Wenn Sie HubSpot als Ihr CRM or Customer-Relationship-Management [-System] (CRM) und Braze für Messaging verwenden, können Sie die Datentransformation nutzen, um HubSpot-Webhook-Payloads in Braze-`/users/track`-Updates umzuwandeln.

Dieses Beispiel prüft auf eine `external_id`, kopiert das eingehende Nutzerobjekt und sendet alle enthaltenen Felder als angepasste Attribute an Braze.

```
function toBrazeTrackPayload(userObject) {
  if (!userObject.external_id) {
    throw new Error("Braze requires an 'external_id' field.");
  }

  return {
    attributes: [userObject]
  };
}

const brazePayload = toBrazeTrackPayload(payload);
return brazePayload;
```

## Beispiel für Transformationscode {#example-transformation-code}

Sehen Sie sich diese Beispiel-Payload von Typeform an, einer Umfrageplattform, die immer dann gesendet wird, wenn eine Umfrageantwort eingeht.

![Screenshot zum Beispiel für Transformationscode.]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab Einfache Transformation %}

Dieses Beispiel nimmt die Umfrageantworten als Attribute und schreibt ein Event, um anzuzeigen, dass die Umfrage abgeschlossen wurde:

```
return {
  "attributes": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab Erweiterte Transformation %}

Bauen wir das Beispiel für die einfache Transformation weiter aus und führen eine `if`-Anweisung ein, um die Nutzer:innen anhand einer der Antworten zu kategorisieren.

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}