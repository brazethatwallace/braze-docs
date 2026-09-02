---
nav_title: Open Loyalty
article_title: Open Loyalty
description: "Die Integration von Braze und Open Loyalty ermöglicht es Ihnen, Loyalitätsdaten – wie Punktestand, Tier-Änderungen und Ablaufwarnungen – in Realtime direkt mit Braze zu synchronisieren."
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Open Loyalty

> [Open Loyalty](https://www.openloyalty.io/) ist eine cloudbasierte Plattform für Kundenbindungs-Programme, mit der Sie Kundenbindungs- und Rewards-Programme erstellen und verwalten können. Die Integration von Braze und Open Loyalty synchronisiert Loyalitätsdaten – wie Punktestand, Tier-Änderungen und Ablaufwarnungen – in Realtime direkt mit Braze. So können Sie personalisierte Nachrichten (E-Mail, Push, SMS) triggern, wenn sich der Loyalitätsstatus einer Nutzerin oder eines Nutzers ändert.

_Diese Integration wird von Open Loyalty gepflegt._

## Über die Integration {#about-the-integration}

Diese Integration verwendet Braze-Datentransformationen, um Webhooks von Open Loyalty zu erfassen und auf Braze-Nutzerprofile abzubilden.

* **Realtime-Updates**: Pushen Sie Loyalitäts-Events (verdiente Punkte, Tier-Upgrades) an Braze.
* **Personalisierung**: Verwenden Sie Loyalitäts-Attribute (aktueller Saldo, Name der nächsten Stufe) in Ihren Braze-Templates.
* **Bidirektional**: Aktualisieren Sie angepasste Attribute von Open-Loyalty-Kund:innen auf Grundlage von Braze-Engagement-Daten.

## Anwendungsfälle {#use-cases}

Diese Integration umfasst die folgenden Datenflüsse:

1. **Events mit Braze synchronisieren (eingehend)**: Verfolgen Sie Punkteänderungen, Tier-Upgrades oder Prämieneinlösungen, indem Sie Daten von Open Loyalty an Braze senden. Die Datentransformation wandelt diese Daten in ein Nutzer-Event um.
2. **Open-Loyalty-Mitglieder ändern (ausgehend)**: Aktualisieren Sie automatisch Mitgliedsdaten in Open Loyalty auf Grundlage des Nutzerverhaltens in Braze, z. B. durch Hinzufügen von „VIP“-Labels oder Aktualisieren angepasster Attribute.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung | Beschreibung |
| :--- | :--- |
| Open-Loyalty-Konto | Sie benötigen ein Admin-Konto auf einem Open-Loyalty-Tenant, um diese Partnerschaft nutzen zu können. |
| Open Loyalty REST-API-Schlüssel | Ein Open Loyalty REST-API-Schlüssel (für Integrationen, die Daten von Braze an Open Loyalty senden). <br><br> Erstellen Sie diesen unter **Settings > Admins > API Keys**. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Erstellen Sie diesen Schlüssel im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. |
| Braze-Datentransformation | Sie benötigen Zugriff auf den Tab „Dateneinstellungen“ in Braze, um Webhook-Listener zu konfigurieren. |
| Übereinstimmende IDs | Die `external_id` der Nutzerin oder des Nutzers in Braze muss mit der `loyaltyCardNumber` (oder einem anderen Standardbezeichner) in Open Loyalty übereinstimmen. |
| Tenant-ID | Ihre Open-Loyalty-Tenant-ID (erforderlich für ausgehende Updates). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

Die primäre Integration synchronisiert Open-Loyalty-Webhook-Events über Datentransformation mit Braze.

### Schritt 1: Webhook-URL in Braze generieren {#step-1-generate-the-webhook-url-in-braze}

Erstellen Sie zunächst eine Datentransformation in Braze, um eine eindeutige URL für den Datenempfang zu generieren.

1.  Öffnen Sie in Braze **Data Settings > Data Transformation**.
2.  Klicken Sie auf **Create Transformation**.
3.  Füllen Sie die folgenden Felder aus:
     * **Transformation name**: Geben Sie einen beschreibenden Namen ein (z. B. „Open Loyalty Point Update Events“).
     * **Select destination**: Wählen Sie **POST: Track users**.
4.  Klicken Sie auf **Create Transformation**.
5.  Suchen Sie die **Webhook URL** im Detailbereich und klicken Sie auf **Copy**.

{% alert important %}
Bewahren Sie diese URL sicher auf – Sie benötigen sie für den nächsten Schritt.
{% endalert %}

### Schritt 2: Webhook-Abo in Open Loyalty erstellen {#step-2-create-the-webhook-subscription-in-open-loyalty}

Weisen Sie Open Loyalty an, bestimmte Events an die soeben generierte URL zu senden.

1.  Melden Sie sich in Ihrem Open Loyalty Admin Panel an.
2.  Navigieren Sie zu **General > Webhooks**.
3.  Klicken Sie auf **Add new webhook** und konfigurieren Sie das Abo:
    * **eventName**: Wählen Sie das Event aus, das Sie tracken möchten (z. B. `AvailablePointsAmountChanged`, `CustomerLevelChanged` oder `CampaignEffectWasApplied`).
    * **url**: Fügen Sie die Braze-Webhook-URL aus Schritt 1 ein.
    * Fügen Sie die folgenden Header hinzu:
      * `Content-Type: application/json`
      * `User-Agent: partner-OpenLoyalty`
4.  Speichern Sie das Webhook-Abo.

### Schritt 3: Datentransformation konfigurieren {#step-3-configure-the-data-transformation}

Schreiben Sie die JavaScript-Logik in Braze, um den eingehenden Open-Loyalty-Payload auf Braze-Eigenschaften abzubilden.

1.  Öffnen Sie in Braze die Datentransformation, die Sie in Schritt 1 erstellt haben.
2.  Triggern Sie das Event in Open Loyalty (z. B. ändern Sie die Punkte eines Mitglieds oder weisen Sie eine Stufe zu), um einen Beispiel-Payload im Bereich **Webhook details** zu erzeugen.
3.  Schreiben Sie im **Transformation code**-Editor ein Skript zur Abbildung der eingehenden Daten. Verwenden Sie das folgende Beispiel als Anhaltspunkt:

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,

      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",

      // timestamp
      "time": new Date().toISOString(),

      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4. Klicken Sie auf **Validate**, um sicherzustellen, dass der Code mit Ihrem Beispiel-Payload funktioniert, und klicken Sie dann auf **Activate**.


## Open Loyalty mit Braze verwenden {#using-open-loyalty-with-braze}

Nachdem Sie die eingehende Integration abgeschlossen haben, konfigurieren Sie **ausgehende Updates**, um Open-Loyalty-Mitglieder auf Grundlage des Braze-Verhaltens zu ändern.

### Schritt 1: Braze-Webhook-Campaign konfigurieren {#step-1-configure-braze-webhook-campaign}

Dieser Prozess verwendet Braze-Webhooks, um eine `PATCH`-Anfrage an die Open Loyalty Member API zu senden (z. B. um ein „VIP“-Label hinzuzufügen).

1.  Erstellen Sie in Braze eine neue **Webhook Campaign** (oder verwenden Sie einen Webhook innerhalb eines Canvas).
2.  Klicken Sie auf **Compose Webhook**.
3.  **Webhook URL**: Konstruieren Sie die URL unter Verwendung Ihrer Open-Loyalty-Instanz, der Tenant-ID und der Braze-Liquid-Variable für die Nutzer-ID.
    * Format:
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. Füllen Sie die folgenden Felder aus:
    * **Request Method**: `PATCH`
    * **Request Headers**:
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-Agent: Braze`
5.  **Request Body**: Wählen Sie `Raw text` und fügen Sie den Payload ein:

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### Schritt 2: Trigger konfigurieren {#step-2-configure-the-trigger}

1.  Navigieren Sie zum Tab **Delivery** oder **Entry Schedule**.
2.  Füllen Sie die folgenden Felder aus:
    * **Delivery Method**: Action-Based.
    * **Trigger**: Definieren Sie den entsprechenden Trigger (z. B. eine Nutzerin oder ein Nutzer tritt einem bestimmten Segment in Braze bei).
    * **Launch**: Aktivieren Sie die Campaign.

## Fehlerbehebung {#troubleshooting}

### Eingehende Events überprüfen {#verify-inbound-events}
Wenn die Datentransformation aktiv ist, erscheinen die Daten in Braze als angepasstes Event. Überprüfen Sie dies, indem Sie eine Campaign mit einem **Perform Custom Event**-Trigger erstellen und prüfen, ob das von Ihnen definierte Event (z. B. `Loyalty Event Triggered`) verfügbar ist.

### Ausgehende Webhooks überprüfen {#verify-outbound-webhooks}
Überprüfen Sie das Nachrichten-Aktivitätsprotokoll in Braze, um sicherzustellen, dass der Webhook den Status `200 OK` zurückgegeben hat.
* **401-Fehler**: Überprüfen Sie Ihr Open Loyalty API-Token / Textbaustein.
* **404-Fehler**: Die Nutzer-ID in Braze existiert nicht in Open Loyalty.