---
nav_title: Seen
article_title: Seen
description: "Seen ermöglicht personalisierte Video-Erlebnisse in großem Umfang und hilft Marken, das Engagement entlang der Customer Journey zu steigern."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Seen

> [Seen](https://seen.io) ermöglicht es Marken, personalisierte Video-Erlebnisse in großem Umfang zu erstellen und zuzustellen. Mit Seen können Sie ein Video rund um Ihre Daten entwerfen, es in großem Umfang in der Cloud personalisieren und dann dort verteilen, wo es am besten funktioniert.
>
> Die Integration von Braze und Seen ermöglicht es Ihnen, Nutzerdaten von Braze an Seen zu senden, dynamisch personalisierte Videos zu generieren und Video-Assets – wie eine eindeutige Player-URL und ein Vorschaubild – zur Verwendung in Campaigns und Canvases an Braze zurückzugeben.


## Anwendungsfälle {#use-cases}

Seen unterstützt die automatisierte, personalisierte Zustellung von Videos über den gesamten Kundenlebenszyklus, einschließlich:

- **Onboarding**: Begrüßen Sie neue Nutzer:innen mit Videos, die auf ihr Profil oder ihren Anmeldekontext personalisiert sind
- **Conversion und Aktivierung**: Verstärken Sie wichtige Aktionen mit kontextuellem Video-Messaging
- **Loyalität und Upselling**: Heben Sie personalisierte Angebote oder Nutzungs-Meilensteine hervor
- **Rückgewinnung und Churn-Prävention**: Reaktivieren Sie inaktive Nutzer:innen mit maßgeschneiderten Video-Inhalten


## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung | Beschreibung |
|--------------|-------------|
| Zugang zur Seen-Plattform | Sie benötigen ein Abo der Seen-Plattform oder eine aktive Seen-Kampagne. Sie benötigen Zugriff auf Ihre Workspace-Einstellungen, um Ihre Workspace-ID abzurufen und ein API-Token zu generieren. |
| Braze-Datentransformation-Webhook-URL | Die Braze-Datentransformation formatiert die von Seen eingehenden Daten so um, dass sie vom `/users/track`-Endpunkt von Braze akzeptiert werden können. |
| Braze-Nutzerdaten | Für die Video-Personalisierung sind Daten auf Nutzer:innen-Ebene erforderlich. Stellen Sie sicher, dass die relevanten Attribute in Braze verfügbar sind und dass Sie **braze_id** als eindeutigen Bezeichner übergeben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }




## Wie Seen Journeys funktionieren {#how-seen-journeys-work}

Seen verwendet [Journeys](https://docs.seen.io/journey), um zu steuern, wie eingehende Daten verarbeitet werden und wie Video-Ausgaben erzeugt werden.

Eine Journey ist ein konfigurierbarer Workflow, der:
- Daten von externen Systemen empfängt (z. B. Braze)
- Logik und Personalisierungsregeln anwendet
- Ein Video und zugehörige Assets erzeugt
- Eine konfigurierbare Antwort-Payload zurückgibt

Journeys bestehen aus **Knoten**, die jeweils eine bestimmte Funktion haben:

- **Trigger-Knoten**: Legt fest, wie und wann eine Journey startet (für Braze-Integrationen verwenden Sie einen `On Create`-Trigger)
- **Bedingter Knoten**: Leitet Nutzer:innen auf der Grundlage von Datenwerten durch verschiedene logische Pfade
- **Projekt-Knoten**: Wendet dynamische Video-Personalisierung anhand der eingehenden Daten an
- **Player-Knoten**: Erzeugt eine eindeutige Video-Player-URL
- **Webhook-Knoten**: Definiert die an Braze zurückgesendete Antwort-Payload

Da Journey-Antworten konfigurierbar sind, stellen Sie sicher, dass die von Seen zurückgegebenen Ausgabefelder den von Ihrer Braze-Datentransformation erwarteten Attributen entsprechen.


## Rate-Limit
Die Seen-API akzeptiert bis zu 100 Aufrufe alle 10 Sekunden.


## Integration

In diesem Beispiel sendet Braze Nutzerdaten an Seen, um ein personalisiertes Video zu generieren. Seen liefert dann eine eindeutige Video-Player-URL und eine Vorschaubild-URL zurück, die als angepasste Attribute in Braze zur Verwendung im Messaging gespeichert werden.

Wenn Sie mehrere Video-Kampagnen mit Seen haben, wiederholen Sie den Vorgang, um Braze mit allen Video-Kampagnen zu verbinden.

### 1. Schritt: Erstellen Sie eine Webhook-Campaign, um Daten an Seen zu senden {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Erstellen Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/) in Braze.

Konfigurieren Sie den Webhook wie folgt:

- **Webhook-URL**:
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`
  Ihre Workspace-ID finden Sie in den Einstellungen der Seen-Plattform.

- **HTTP-Methode**: POST
- **Anfrage-Body**: Rohtext
  Verwenden Sie das folgende Beispiel als Ausgangspunkt. Weitere Informationen finden Sie in der [Seen-Dokumentation zur Datenerstellung](https://docs.seen.io/create-data).

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}
- **Anfrage-Header**:
  - `Authorization`: Bearer `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  > Generieren Sie ein [API-Token](https://docs.seen.io/authorization) in der Seen-Plattform unter Workspace-Einstellungen. Sie können sich an Ihren Seen Customer-Success-Manager wenden, um Unterstützung zu erhalten.

- Um den Webhook mit einer/einem Nutzer:in zu testen, wechseln Sie auf den Tab **Test**.
- Nachdem Sie bestätigt haben, dass der Test wie vorgesehen funktioniert, schließen Sie die Einrichtung des Webhooks ab.


### 2. Schritt: Konfigurieren Sie eine Journey in der Seen-Plattform {#step-2-configure-a-journey-in-the-seen-platform}

Seen verwendet [Journeys](https://docs.seen.io/journey), um festzulegen, wie eingehende Daten verarbeitet, personalisiert und an Braze zurückgegeben werden.
Jede Journey ist ein konfigurierbarer Workflow, der aus Knoten besteht, mit denen Sie sowohl die Logik der Videogenerierung als auch die Antwort-Payload steuern können.

So konfigurieren Sie Ihre Journey:

1. Erstellen Sie eine neue Journey in der Seen-Plattform
2. Fügen Sie einen **Trigger-Knoten** hinzu und wählen Sie den Trigger `On Create`
   Dadurch wird sichergestellt, dass die Journey startet, wenn Braze Daten an Seen sendet. Erstellen Sie bei Bedarf eine [Segmentierungslogik](https://docs.seen.io/segments) in Ihrem Workspace und fügen Sie diese hinzu.
3. Bauen Sie Ihre Logik nach Bedarf mit den folgenden Knoten auf:
   - **Bedingter Knoten**: Leiten Sie Nutzer:innen auf der Grundlage von Attributwerten weiter (z. B. Tarifart oder Region)
   - **Projekt-Knoten**: Wenden Sie die dynamische Video-Personalisierung anhand der eingehenden Daten an
   - **Player-Knoten**: Generieren Sie eine eindeutige Video-Player-URL
4. Fügen Sie einen **Webhook-Knoten** hinzu, um die Antwort zu definieren, die an Braze zurückgesendet wird

#### Antwortanforderungen des Webhook-Knotens {#webhook-node-response-requirements}

Da die Antwort-Payload konfigurierbar ist, stellen Sie sicher, dass die folgenden Felder zurückgegeben werden, um die im nächsten Schritt beschriebene Braze-Datentransformation zu unterstützen:

| Feld | Beschreibung |
|------|-------------|
| `id` | Muss mit der von Braze gesendeten `braze_id` übereinstimmen |
| `player_url` | Eindeutige URL für den personalisierten Video-Player |
| `email_thumbnail_url` | URL des generierten Video-Vorschaubilds |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook node response requirements" }

Wenn Ihr Anwendungsfall zusätzliche Attribute erfordert, fügen Sie diese in die Antwort ein und ordnen Sie sie in Braze zu.


### 3. Schritt: Erstellen Sie eine Datentransformation, um Daten von Seen zu empfangen {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Verwenden Sie Braze-Datentransformationen, um die Seen-Journey-Antwort aufzunehmen und Video-Assets im Nutzerprofil zu speichern.

1. Erstellen Sie die folgenden [angepassten Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) in Braze:
   - `player_url`
   - `email_thumbnail_url`
2. Navigieren Sie zu **Dateneinstellungen** → **Datentransformation** und klicken Sie auf **Transformation erstellen**
3. Konfigurieren Sie die Transformation:
   - **Von Grund auf neu erstellen**
   - **Ziel** → POST: Nutzer:innen tracken
4. Geben Sie die generierte Webhook-URL an Seen weiter oder fügen Sie sie direkt zum Journey-**Webhook-Knoten** hinzu
5. Verwenden Sie den folgenden Transformations-Code:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6. Senden Sie eine Test-Payload an den angegebenen Endpunkt. Senden Sie Daten an die Seen-Plattform, um Ihre Journey auszuführen, oder senden Sie die Payload mit [Postman](https://www.postman.com/) oder einem anderen ähnlichen Dienst direkt an Braze.
7. Wählen Sie **Validate**, um sicherzustellen, dass alles wie vorgesehen funktioniert.
8. Wählen Sie **Save** und **Activate**.