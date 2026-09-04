---
nav_title: SessionM
article_title: SessionM
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und SessionM, einer Customer-Engagement- und Kundenbindungsplattform."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
---

# SessionM Treueplattform {#sessionm-loyalty-platform}

> [SessionM](https://sessionm.com/) ist eine Plattform für Customer-Engagement und Kundentreue, Teil von Capillary Technologies, die Marketern Features für das Kampagnenmanagement und Lösungen für das Loyalitätsmanagement zur Verfügung stellt, um das Engagement und den Gewinn durch gezielte Ansprache zu steigern.

## Voraussetzungen {#prerequisites}

| Quelle | Anforderung | Beschreibung |
| --- | --- | --- |
| Braze | Ein Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `trigger_send`-Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze | Ein Braze REST-Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
| Braze und SessionM | Passender Bezeichner | Um die Integration zu nutzen, stellen Sie sicher, dass sowohl SessionM als auch Braze über einen Datensatz mit den von jeder Plattform verwendeten Bezeichnern verfügen. Verweise auf `user_id` entsprechen dem SessionM-Bezeichner der Nutzer:innen, der zum Zeitpunkt der Profilerstellung in SessionM generiert wurde. |
| SessionM | Ein SessionM-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein SessionM-Konto. |
| SessionM | Ein SessionM Core REST-Endpunkt | Ihr Endpunkt hängt von der SessionM-URL Ihrer Instanz ab. Dieser kann im SessionM-Dashboard unter **Digital Properties** erstellt werden. |
| SessionM | Ein SessionM Core REST-API-Schlüssel | Der SessionM-API-Schlüssel, der mit Ihrer Instanz und der Braze-Integration verbunden ist. Dieser Schlüssel kann für alle Core-basierten Aufrufe einschließlich Tags verwendet werden. Dieser kann im SessionM-Dashboard unter **Digital Properties** erstellt werden. |
| SessionM | Ein SessionM Core REST-API-Geheimnis | Das SessionM-API-Geheimnis, das mit Ihrer Instanz und der Braze-Integration verbunden ist. Dieser Schlüssel kann für alle Core-basierten Aufrufe einschließlich Tags verwendet werden. Dieser kann im SessionM-Dashboard unter **Digital Properties** erstellt werden. |
| SessionM | Ein SessionM Connect REST-Endpunkt | Ihr Endpunkt hängt von der SessionM-URL Ihrer Instanz ab. Wenden Sie sich an Ihren technischen SessionM Account Manager:in oder das Delivery-Team. |
| SessionM | Ein SessionM Connect REST-Autorisierungs-String | Der SessionM Connect Basic-Authorization-String, der mit Ihrer Instanz verknüpft ist. Dieser Authentifizierungs-String kann für alle verbindungsbasierten Aufrufe verwendet werden, einschließlich get_user_offers. Bitte wenden Sie sich an Ihren technischen SessionM Account Manager:in oder das Delivery-Team. |
| SessionM | Eine SessionM Connect REST-Retailer-ID | Eine eindeutige GUID-Kennung für den spezifischen Kunden, der mit Ihrer Instanz verbunden ist. Wenden Sie sich an Ihren technischen SessionM Account Manager:in oder das Delivery-Team. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Die folgenden Anwendungsfälle zeigen einige Möglichkeiten, wie Sie die Integration von SessionM und Braze nutzen können.

- Erstellen Sie eine Segmentierung, die Daten aus allen Kundenbindungs-, Kundenmanagement- und Messaging-Plattformen einbezieht.
- Nutzen Sie eine robuste Segmentierung, um bestimmte Nutzergruppen mit Angeboten und Aktionen anzusprechen.
- Nutzen Sie immer die aktuellsten Nutzer:innen-, Angebots- und Treueinformationen, wenn Sie Nachrichten versenden.
- Informieren Sie Ihre Kund:innen ausführlich über den Fortschritt und den Abschluss von Werbe- und Treueaktionen.
- Benachrichtigen Sie Ihre Kund:innen, wenn ein neues Angebot vergeben wird, und teilen Sie die Angebotsdetails mit.

## Integration von SessionM mit Braze {#integrating-sessionm-with-braze}

### Schritt 1: Segment in Braze erstellen {#step-1-create-a-segment-in-braze}

Erstellen Sie in Braze ein Segment von Nutzer:innen für das Targeting mit SessionM-Aktionen und -Angeboten.

![Segment Builder mit dem ausgewählten Filter „Angepasste Attribute“.]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### Schritt 2: Braze Segments in SessionM importieren {#step-2-import-braze-segments-into-sessionm}

#### Option 1: Export zum SessionM-Tag-Endpunkt (empfohlen) {#option-1-export-to-the-sessionm-tag-endpoint-recommended}

Erstellen Sie zunächst eine Webhook-Kampagne in Braze und setzen Sie die Webhook-URL auf {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Verwenden Sie Liquid, um die `user_id` innerhalb der URL zu definieren.

Stellen Sie den **Body für die Anfrage** des Webhooks mit Hilfe eines Rohtextes so zusammen, dass er die gewünschten Tags, die dem Kundenprofil in SessionM hinzugefügt werden sollen, und die gewünschte Gültigkeitsdauer enthält. Ein Beispiel:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![SessionM-Webhook-Composer mit JSON-Payload für die Einrichtung des Braze-Campaign-Triggers.]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

Fügen Sie im Tab **Einstellungen** die Schlüssel-Wert-Paare für jedes Anfrage-Header-Feld hinzu:
    - Erstellen Sie einen Schlüssel `Content-Type` mit dem entsprechenden Wert `application/json`
    - Erstellen Sie einen Schlüssel `Authorization` mit dem entsprechenden Wert `Basic YOUR-ENCODED-STRING-KEY`. Wenden Sie sich an Ihr SessionM-Team, um den kodierten String-Schlüssel für Ihren Endpunkt zu erhalten.

![Webhook-Einstellungen.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

Planen Sie Ihre Zustellung, legen Sie Ihre **Zielgruppen** für das Targeting des [zuvor erstellten](#step-1-create-a-segment-in-braze) Segments fest und starten Sie dann Ihre Kampagne.

{% alert important %}
Dieser Vorgang kann auch über einen API-Client wie Postman durchgeführt werden, indem Sie eine Anfrage direkt an den [SessionM-Tag-Endpunkt](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) stellen und dabei die Kund:in, den Tag-Namen und eine Gültigkeitsdauer für jede Nutzer:in im Aufruf angeben (eine Nutzer:in pro Aufruf).
<br><br>
Die folgende Beispielanfrage verwendet cURL.

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### Option 2: CSV-Import

Exportieren Sie Ihr Braze Segment mit dem Braze Segmenter und stellen Sie SessionM eine CSV-Datei zur Verfügung, die die zu taggenden Kund:innen, den Tag-Namen und eine Gültigkeitsdauer für jede Nutzer:in in der Datei enthält.

## Realtime-Angebotsmappe mit Braze abrufen {#retrieving-real-time-offer-wallet-with-braze}

Die Integration von SessionM mit Braze ermöglicht den Abruf von SessionM-Nutzerdaten in Echtzeit zum Zeitpunkt des Nachrichtenversands mithilfe von Connected-Content, um das Risiko auszuschließen, dass veraltete, abgelaufene oder bereits eingelöste Treueangebote an Kund:innen übermittelt werden.

Das folgende Beispiel zeigt, wie Connected-Content verwendet wird, um Daten der Angebotsmappe als Template in eine Nachricht einzufügen. Connected-Content kann jedoch mit jedem der Connect-Endpunkte von SessionM verwendet werden.

### Schritt 1: Angebot in SessionM ausgeben {#step-1-issue-offer-in-sessionm}

SessionM gibt Kund:innen Angebote über verschiedene interne Hebel aus, die konfiguriert werden können. Nach der Ausgabe werden die Angebote in einen Zustand versetzt, den SessionM als „Angebotsmappe“ bezeichnet.

Eine Kund:in muss die erforderliche Aktion durchführen oder das Targeting erfüllen und erhält das Angebot innerhalb von SessionM.

SessionM fügt das Angebot dann der Angebotsmappe der Kund:in im ausgegebenen Zustand hinzu.

### Schritt 2: SessionM Offer Wallet API aufrufen {#step-2-call-sessionm-offer-wallet-api}

Verwenden Sie in einer Kampagne oder einem Canvas-Schritt mit den SessionM-Angeboten [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call), um einen API-Aufruf an den [SessionM `get_user_offers`-Endpunkt](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/) zu tätigen.

Geben Sie in der Connected-Content-Anfrage die SessionM `user_id` der Nutzer:in und Ihre `retailer_id` an, um die vollständige Liste der aktiven Angebote abzurufen, die die Kund:in in ihrer Angebotsmappe hat. Jede Anfrage an diesen Endpunkt kann eine einzelne Nutzer:in enthalten. Wenden Sie sich an das SessionM-Team, um den kodierten String-Schlüssel für den Basic-Authorization-Header in Ihrem Connected-Content-Aufruf zu erhalten.

Im Anfrage-Body ist `culture` standardmäßig auf `en-US` eingestellt, aber Sie können Liquid verwenden, um die Sprache einer Nutzer:in für mehrsprachige SessionM-Angebote als Template einzusetzen (z. B. mit {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### Schritt 3: Angebotsmappe für Braze-Messaging befüllen {#step-3-populate-offer-wallet-to-braze-messaging}

Nachdem eine Anfrage an den Endpunkt gestellt wurde, gibt SessionM die vollständige Liste der Angebote im ausgegebenen Zustand zurück, zusammen mit den vollständigen Details zu jedem Angebot. Dies ist ein Beispiel für eine zurückgegebene Antwort:

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Mit der Liquid-Dot-Notation kann dies in die Nachricht eingefügt werden. Um die Nachricht beispielsweise mit der resultierenden `offer_id` zu personalisieren, könnten Sie die Rückgabe-Payload nutzen, indem Sie {% raw %}`{{wallet.payload.available_points}}`{% endraw %} verwenden, was `100` zurückgibt.

{% alert note %}
Dies ist eine individuelle API. Wenn Sie beabsichtigen, einen Batch von mehr als 500 Nutzer:innen zu versenden, erkundigen Sie sich bei Ihrem SessionM-Team, wie Sie Massendaten in die Integration einbeziehen können.
{% endalert %}

## Getriggertes Messaging einrichten {#setting-up-triggered-messaging}

Die Integration von SessionM und Braze ermöglicht es, Nutzerprofildaten, Angebotsdetails und Punktesalden dynamisch in Messaging einzubringen und in Echtzeit an die Kund:innen zu senden, sobald diese aktiv werden.

### Schritt 1: SessionM Delivery-Team konfiguriert Templates {#step-1-sessionm-delivery-team-configures-templates}

Arbeiten Sie mit Ihrem SessionM Delivery-Team zusammen, um Templates für die Verwendung in Ihren getriggerten Nachrichten zu entwickeln. SessionM fügt Nutzerprofildaten, Angebotsdetails und Punktesalden in das Messaging ein und triggert sie in Braze für Realtime-Nachrichten.

Zu den Standardfeldern in allen Templates von SessionM gehören:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
Wenn Sie das `broadcast flag` auf `true` setzen, wird die Nachricht an das gesamte Segment gesendet, auf das die Kampagne oder das Canvas in Braze abzielt.
{% endalert %}

Zusätzliche Felder können je nach Bedarf konfiguriert werden:

- **Angebotsdaten:** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **Punkteprämien-Daten:** `point award amount`, `point account name`
- **Ereignis-Trigger-Daten:** Alle Daten im Trigger-Ereignis, die das Ergebnis des Trigger/Sende-Webhooks nutzen
- **Kampagnenspezifische Daten:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

Zusätzliche Felder werden als `trigger_properties` an Braze gesendet, um die Nachricht zu personalisieren.

### Schritt 2: Braze-Kampagne oder Canvas erstellen {#step-2-create-a-braze-campaign-or-canvas}

Erstellen Sie eine API-getriggerte Kampagne oder ein Canvas in Braze, das von SessionM getriggert werden kann. Wenn zusätzliche Felder konfiguriert wurden, wie `offer_id` oder `offer title`, verwenden Sie Liquid (z. B. {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}), um die personalisierten Felder in Ihre Nachrichten einzufügen.

![API-Trigger-Eigenschaften.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

Notieren Sie sich im Tab **Zustellung planen** die ID der Kampagne oder des Canvas, da diese zu den **erweiterten Einstellungen** der SessionM-Kampagne hinzugefügt wird.

![API-getriggerte Kampagne.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Schließen Sie die Details Ihrer Kampagne oder Ihres Canvas ab und wählen Sie **Starten**.

### Schritt 3: SessionM Werbe- oder Messaging-Kampagne erstellen {#step-3-create-a-sessionm-promotional-or-messaging-campaign}

Erstellen Sie als Nächstes Ihre Kampagne in SessionM.

![SessionM-Kampagne erstellen.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

Aktualisieren Sie die erweiterten Einstellungen in der SessionM-Kampagne, um die folgende JSON-Payload einzuschließen, die die `braze_campaign_id` oder `braze_canvas_id` enthält.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![Erweiterte Einstellungen von SessionM.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

Erstellen Sie einen Nachrichten-Trigger nach dem gewünschten Zeitplan oder Verhalten. Wählen Sie dann im Menü **External Message** die **Braze Messaging Variant** als **Messaging Variant** aus, um das Template zu verwenden.

![Externe Nachricht von SessionM.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

Dieses Template ruft die relevanten statischen und dynamischen Attribute ab und stellt eine Anfrage an den Braze-Endpunkt.

![SessionM Braze-Template.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}