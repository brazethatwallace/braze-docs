---
nav_title: VideoSmart
article_title: VideoSmart
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und VideoSmart, einer personalisierten, interaktiven Videotechnologie, die es Marken ermöglicht, datengestützte, nicht-lineare Inhalte in großem Umfang bereitzustellen."
alias: /partners/videosmart/
page_type: partner
search_tag: Partner
---

# VideoSmart

> [VideoSmart](https://www.videosmart.com/) bietet personalisierte, interaktive Videotechnologie, mit der Sie datengestützte, nicht-lineare Inhalte in großem Umfang bereitstellen können. Jedes Video wird dynamisch anhand von Daten auf Kundenebene generiert, was maßgeschneiderte Nachrichten und Nutzer-Journeys innerhalb eines einzigen Videoerlebnisses ermöglicht.
>
> Die VideoSmart-Integration ermöglicht es Ihnen, personalisierte Videoinhalte in E-Mail-Campaigns einzubetten, indem Sie Braze Connected-Content und Liquid-Templating verwenden, um Video-Assets von VideoSmart anzufordern. Diese Integration wird in der Regel über ein wiederverwendbares Braze Content-Block-Template implementiert, das eine konsistente Bereitstellung über Campaigns hinweg ermöglicht und gleichzeitig Flexibilität bei der Campaign-Auswahl und Personalisierungslogik bietet.

_Diese Integration wird von VideoSmart entwickelt und gepflegt._

## Über diese Integration {#about-this-integration}

VideoSmart integriert sich mit Braze, um zum Sendezeitpunkt dynamisch personalisierte Video-Assets zu generieren, die dann direkt in Ihre Braze-Campaign- und Canvas-E-Mail-Inhalte eingebettet werden.

In Braze wählen Sie die entsprechende VideoSmart-Campaign aus und übergeben beim Senden Kundenattribute (über Liquid-Templating) an VideoSmart. Diese Attribute werden verwendet, um für jede Empfängerin und jeden Empfänger ein einzigartiges, personalisiertes Videoerlebnis zu rendern. Anschließend können Sie Braze Connected-Content verwenden, um Video-URLs oder -Assets in Echtzeit von der VideoSmart-API anzufordern, was skalierbare Personalisierung ermöglicht.

Diese Integration ist für Braze-E-Mail-Nachrichten konzipiert, die Liquid-Templating und Connected-Content unterstützen, und kann so konfiguriert werden, dass sie mit Standard-Braze-Nutzerprofil-Attributen oder angepassten Datenfeldern funktioniert.

## Anwendungsfälle {#use-cases}

Häufige Anwendungsfälle umfassen:

- Kunden-Onboarding und Willkommens-Journeys
- Finanzielle Aufklärung (z. B. Renten und Versicherungspolicen)
- Jahresabrechnungen und regulatorische Mitteilungen
- Produktbekanntheit und Cross-Selling-Campaigns
- Kundenbindungs- und Campaigns zur erneuten Interaktion
- Warenkorb-Abbruch-Erinnerungen: Wenn Kund:innen Produkte in ihren Warenkorb legen, aber nicht kaufen, senden Sie eine E-Mail mit einem personalisierten Video, das die zurückgelassenen Artikel hervorhebt
- Nachkauf-Follow-ups: Senden Sie nach einem Kauf ein personalisiertes Dankesvideo und empfehlen Sie verwandte Produkte

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Sie über Folgendes verfügen:

| Anforderung | Beschreibung |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Braze Connected-Content-Zugangsdaten | Connected-Content-Basic-Authentication-Zugangsdaten mit dem Namen **basic_credentials**, konfiguriert mit von VideoSmart bereitgestellten Werten |
| **VideoSmart Content-Block**-Template | Das **VideoSmart Content-Block**-Template, das Ihrem Braze-Dashboard hinzugefügt wurde (bereitgestellt von VideoSmart) |
| Eine Braze-E-Mail-Nachricht | Eine Braze-Campaign-E-Mail oder ein Canvas-E-Mail-Schritt, in den Sie den **VideoSmart Content-Block** einfügen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Befolgen Sie diese Schritte, um den **VideoSmart Content-Block** zu aktivieren und in einer E-Mail zu verwenden.

### Schritt 1: VideoSmart Content-Block-Template in Braze einrichten {#step-1-set-up-the-videosmart-content-block-template-in-braze}

Fordern Sie das **VideoSmart Content-Block**-Template von Ihrer VideoSmart-Vertretung an und fügen Sie es Ihrem Braze-Dashboard hinzu.

VideoSmart stellt Zugangsdaten für die Connected-Content-Authentifizierung bereit, die vom Content-Block verwendet wird.

### Schritt 2: Connected-Content-Authentifizierung einrichten {#step-2-set-up-connected-content-authentication}

Erstellen Sie in Braze Connected-Content-Basic-Authentication-Zugangsdaten mit dem Namen „basic_credentials“.

- Befolgen Sie die Anweisungen unter [Basic-Authentifizierung verwenden]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-basic-authentication).
- Verwenden Sie den Benutzernamen und das Passwort, die von VideoSmart bereitgestellt wurden.

### Schritt 3: Content-Block zu Ihrer E-Mail hinzufügen {#step-3-add-the-content-block-to-your-email}

Fügen Sie den **VideoSmart Content-Block** an der Stelle in Ihre E-Mail ein, an der der Videoinhalt erscheinen soll.

In den meisten Braze-Konfigurationen werden Content Blocks mit dem folgenden Muster referenziert (ersetzen Sie „VideoSmart_Campaign“ durch den Namen des Content-Blocks in Ihrem Konto):

{% raw %}`{{content_blocks.${VideoSmart_Campaign}}}`{% endraw %}

{% alert important %}
Der Name des Content-Blocks unterscheidet zwischen Groß- und Kleinschreibung und muss genau mit dem übereinstimmen, was Sie in Braze konfiguriert haben.
{% endalert %}

### Schritt 4: Campaign und Datensatzdaten überschreiben (optional) {#step-4-override-campaign-and-record-data-optional}

Wenn Ihr Content-Block Standardwerte unterstützt, können Sie ihn verwenden, ohne Variablen zu setzen.

Wenn Sie eine bestimmte VideoSmart-Campaign auswählen, angepasste Personalisierungsfelder übergeben oder beides tun möchten, setzen Sie die folgenden Liquid-Variablen vor dem Rendern des Content-Blocks:

- `vs_campaign_id`: VideoSmart-Campaign-Bezeichner
- `vs_record_data`: ein JSON-String mit den Werten, die Sie an das VideoSmart-Template übergeben möchten

#### Beispiel {#example}

Dieses Beispiel verwendet Braze-Nutzerattribute für den Vornamen und den Nachnamen:

{% raw %}
```liquid
{% assign vs_campaign_id = "CAMPAIGN_ID" %}

{% capture vs_record_data %}
{
  "FirstName": "{{ ${first_name} | default: 'Alex' | json_escape }}",
  "LastName": "{{ ${last_name} | default: 'Doe' | json_escape }}"
}
{% endcapture %}
{% assign vs_record_data = vs_record_data | strip_newlines %}
```
{% endraw %}

{% alert note %}
- Geben Sie immer Standardwerte für Werte an, die in `vs_record_data` verwendet werden, damit Ihre Braze-E-Mail-Vorschau korrekt angezeigt wird.
- `vs_record_data` muss gültiges JSON sein, kodiert als einzelner String (das Beispiel verwendet `strip_newlines`).
{% endalert %}

### Schritt 5: Die vom VideoSmart Content-Block-Template generierten Variablen verwenden {#step-5-use-the-variables-generated-by-videosmarts-content-block-template}

Nachdem der Content-Block ausgeführt wurde, generiert er Variablen, die Sie an anderer Stelle in Ihrer E-Mail referenzieren können.

Häufige Variablen umfassen:

{% raw %}
| Variable | Beschreibung |
| --------------------------------- | ----------------------------------------------------- |
| `{{ video_url }}` | URL des personalisierten Videos |
| `{{ poster_url }}` | URL des Posterbilds für das Video |
| `{{ output_data.VARIABLE_NAME }}` | Zusätzliche Ausgabefelder, die vom Content-Block bereitgestellt werden |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 5: Die vom VideoSmart Content-Block-Template generierten Variablen verwenden" }
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 5: Die vom VideoSmart Content-Block-Template generierten Variablen verwenden" }

## Rate-Limits

Die VideoSmart-API hat ein Rate-Limit von 10.000 Anfragen pro Minute. Wenn Sie dieses Limit überschreiten, können Fehler auftreten oder Verzögerungen bei der Videogenerierung entstehen.

Um dieses Risiko zu reduzieren, konfigurieren Sie das Braze-Campaign-Rate-Limiting so, dass die Nachrichtenversandrate unter der VideoSmart-API-Kapazität bleibt.

Informationen zur Zustellgeschwindigkeit und zum Rate-Limiting in Braze finden Sie unter [Zustellgeschwindigkeit und Rate-Limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#delivery-speed-rate-limiting).

## Hinweise {#considerations}

- Connected-Content wird ausgeführt, wenn die Nachricht gerendert wird, sodass sich die Werte zwischen Vorschau und Versand unterscheiden können, wenn Ihre Standardwerte oder Attribute abweichen.
- Stellen Sie sicher, dass Ihre E-Mail den Content-Block enthält, bevor Sie Variablen wie `video_url` referenzieren.
- Wenn Sie angepasste Felder in `vs_record_data` verwenden, bestätigen Sie die erwarteten Feldnamen mit VideoSmart.

## Fehlerbehebung {#troubleshooting}

### Vorschau funktioniert nicht {#preview-not-working}

Wenn die Braze-Vorschau fehlschlägt (z. B. wiederholte Wiederholungsversuche oder Authentifizierungsfehler), überprüfen Sie Folgendes:

- Die Connected-Content-Zugangsdaten „basic_credentials“ existieren und sind korrekt konfiguriert.
- Das **VideoSmart Content-Block**-Template ist in Ihrem Braze-Konto vorhanden.
- Alle erforderlichen Variablen (z. B. `vs_campaign_id` oder erforderliche Felder in `vs_record_data`) haben Standardwerte für die Vorschau.

### Variablen des VideoSmart Content-Block-Templates generieren nicht die erwartete Ausgabe {#videosmarts-content-block-template-variables-not-generating-expected-output}

Wenn die vom VideoSmart Content-Block-Template generierten Variablen nicht die erwartete Ausgabe liefern, überprüfen Sie Folgendes:

- Das **VideoSmart Content-Block**-Template ist in Braze korrekt eingerichtet.
- Die Connected-Content-Authentifizierung ist mit den entsprechenden Zugangsdaten korrekt eingerichtet.
- Geben Sie Variablen in Ihrer E-Mail aus, um zu bestätigen, dass sie gesetzt werden. Zum Beispiel: `{% raw %}{{ video_url }}{% endraw %}`

Wenn Sie eine angepasste Campaign verwenden, überprüfen Sie außerdem:

- `vs_campaign_id` ist auf einen gültigen Campaign-Bezeichner gesetzt.
- `vs_record_data` ist gültiges JSON und enthält die erwarteten Felder.