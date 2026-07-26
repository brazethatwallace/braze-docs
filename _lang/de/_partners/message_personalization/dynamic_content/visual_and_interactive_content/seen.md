---
nav_title: Seen
article_title: Seen
description: "Seen ermöglicht personalisierte Video-Erlebnisse in großem Umfang und hilft Marken, das Engagement entlang der geschäftskunden Journey zu steigern."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Seen

> [Seen](https://seen.io) ermöglicht es Marken, personalisierte Video-Erlebnisse in großem Umfang zu erstellen und zuzustellen. Mit Seen können Sie ein Video rund um Ihre Daten entwerfen, es in großem Umfang in der Cloud personalisieren und dann dort verteilen, wo es am besten funktioniert.
>
> Diese Integration sendet Nutzerdaten von Braze an Seen, generiert personalisierte Videos und gibt Assets – wie eine eindeutige Player-URL und ein Vorschaubild – zur Verwendung in Campaigns und Canvases an Braze zurück.


## Anwendungsfälle {#use-cases}

Seen unterstützt die automatisierte, personalisierte Zustellung von Videos über den gesamten Kundenlebenszyklus, einschließlich:

- **Onboarding**: Begrüßen Sie neue Nutzer:innen mit Videos, die auf ihr Profil oder ihren Anmeldekontext personalisiert sind
- **Conversion und Aktivierung**: Verstärken Sie wichtige Aktionen mit kontextuellem Video-Messaging
- **Loyalität und Upselling**: Heben Sie personalisierte Angebote oder Nutzungs-Meilensteine hervor
- **Rückgewinnung und Churn-Prävention**: Reaktivieren Sie inaktive Nutzer:innen mit maßgeschneiderten Video-Inhalten


## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Sie über die Zugänge und Daten in der folgenden Tabelle verfügen.

| Voraussetzung | Beschreibung |
|--------------|-------------|
| Zugang zur Seen-Plattform | Sie benötigen ein Abo der Seen-Plattform mit einem veröffentlichten Projekt oder eine aktive Seen-Kampagne. Außerdem benötigen Sie Zugriff auf Ihr Projekt, um den Projekt-Endpunkt abzurufen und ein API-Token zu generieren. |
| Braze-Datentransformation-Webhook-URL | Verwenden Sie die Braze-Datentransformation, um die von Seen eingehenden Daten so umzuformatieren, dass sie vom Braze-[`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) akzeptiert werden können. |
| Braze-Nutzerdaten | Für die Video-Personalisierung sind Daten auf Nutzer:innen-Ebene erforderlich. Stellen Sie sicher, dass die relevanten Attribute in Braze verfügbar sind, und übergeben Sie **`braze_id`** als eindeutigen Bezeichner. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }




## Wie Seen-Projekte funktionieren {#how-seen-projects-work}

Seen verwendet den [Run](https://docs.seen.io/run)-Tab in einem Projekt, um zu steuern, wie eingehende Daten verarbeitet und wie Video-Ausgaben erzeugt werden.

Ein Projekt-Workflow:

- Empfängt Daten von externen Systemen (z. B. Braze)
- Wendet Logik und Personalisierungsregeln an
- Erzeugt ein Video und zugehörige Assets
- Gibt eine konfigurierbare Antwort-Payload zurück

Der Run-Tab umfasst Folgendes:

- **Create via API**: Öffnet die Projekt-API-Details.
- **Import CSV**: Importiert Personalisierungsdaten manuell (wird in dieser Anleitung nicht verwendet).
- **Add webhook**: Definiert die an Braze zurückgesendete Antwort-Payload.
- **View videos**: Zeigt generierte Videos und den Status eingehender Daten an.

Webhook-Antworten sind konfigurierbar. Stellen Sie daher sicher, dass die von Seen zurückgegebenen Ausgabefelder den Attributen entsprechen, die Ihre Braze-Datentransformation erwartet.


## Rate-Limit

Die Seen-API akzeptiert 100 Aufrufe pro 10 Sekunden.


## Integration

In diesem Beispiel sendet Braze Nutzerdaten an Seen, um ein personalisiertes Video zu generieren. Seen gibt dann eine eindeutige Video-Player-URL und eine Vorschaubild-URL zurück, die Sie als [angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) in Braze zur Verwendung im [Messaging]({{site.baseurl}}/user_guide/messaging/) speichern.

Wenn Sie mehrere Video-Kampagnen mit Seen durchführen, wiederholen Sie diesen Vorgang für jede Kampagne.

### 1. Schritt: Erstellen Sie eine Webhook-Campaign, um Daten an Seen zu senden {#step-1-create-a-webhook-campaign-to-send-data-to-seen}

Erstellen Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/) in Braze.

Konfigurieren Sie den Webhook wie folgt:

- **Webhook-URL**:
  `https://next.seen.io/v1/projects/{PROJECT_ID}/data`
  Ihren Projekt-Endpunkt finden Sie auf dem Run-Tab Ihres Seen-Plattform-Projekts.

- **HTTP-Methode**: POST

- **Anfrage-Body**: Rohtext
  Verwenden Sie das folgende Beispiel als Ausgangspunkt. Informationen zu Feldoptionen und Limits finden Sie in der [Seen-Dokumentation zur Datenerstellung](https://docs.seen.io/create-data).

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

  Generieren Sie ein [API-Token](https://docs.seen.io/authorization) auf dem Run-Tab Ihres Seen-Plattform-Projekts. Kontaktieren Sie Ihren Seen geschäftskunden-Success-Manager, wenn Sie Unterstützung benötigen.

- Testen Sie den Webhook mit einer/einem Nutzer:in auf dem **Test**-Tab.
- Schließen Sie nach einem erfolgreichen Test die Webhook-Einrichtung ab.


### 2. Schritt: Konfigurieren Sie ein Projekt in der Seen-Plattform {#step-2-configure-a-project-in-the-seen-platform}

Verwenden Sie in Ihrem Seen-Projekt den [Run](https://docs.seen.io/run)-Tab, um Ihr Video zu veröffentlichen und den ausgehenden Webhook zu registrieren. Eine konzeptionelle Übersicht über den Run-Tab finden Sie unter [Wie Seen-Projekte funktionieren](#how-seen-projects-work).

1. Erstellen Sie in der Seen-Plattform ein Projekt, erstellen Sie Ihr Video und wählen Sie dann **Publish**. Videos werden aus eingehenden Daten generiert, sobald das Projekt veröffentlicht ist.
2. Wählen Sie auf dem Run-Tab **Add a webhook**.

#### Anforderungen an die Webhook-Antwort {#webhook-response-requirements}

Die Antwort-Payload ist konfigurierbar. Geben Sie die Felder in der folgenden Tabelle zurück, damit die Braze-Datentransformation im nächsten Schritt sie zuordnen kann.

| Feld | Beschreibung |
|------|-------------|
| `id` | Muss mit der von Braze gesendeten `braze_id` übereinstimmen |
| `player_url` | Eindeutige URL für den personalisierten Video-Player |
| `email_thumbnail_url` | URL des personalisierten Video-Vorschaubilds |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anforderungen an die Webhook-Antwort" }

Wenn Sie zusätzliche Attribute benötigen, fügen Sie diese zur Antwort hinzu und ordnen Sie sie in Braze zu.


### 3. Schritt: Erstellen Sie eine Datentransformation, um Daten von Seen zu empfangen {#step-3-create-a-data-transformation-to-receive-data-from-seen}

Verwenden Sie Braze-Datentransformationen, um die Seen-Antwort zu verarbeiten und Video-Assets im Nutzerprofil zu speichern.

1. Erstellen Sie die folgenden [angepassten Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) in Braze:
   - `player_url`
   - `email_thumbnail_url`

2. Navigieren Sie zu **Dateneinstellungen** > **Datentransformationen** und wählen Sie **Transformation erstellen**.

3. Konfigurieren Sie die Transformation:
   - **Von Grund auf neu erstellen**
   - **Ziel** > POST: Nutzer:innen tracken

4. Geben Sie die generierte Webhook-URL an Seen weiter oder fügen Sie sie zum **Webhook** auf dem Run-Tab Ihres Projekts hinzu.

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
6. Senden Sie eine Test-Payload an den angegebenen Endpunkt. Sie können Daten an Ihr Seen-Plattform-Projekt senden (veröffentlichen Sie das Projekt zuerst) oder eine Payload mit [Postman](https://www.postman.com/) oder einem ähnlichen Tool direkt an Braze senden.
7. Wählen Sie **Validate**, um zu überprüfen, ob die Transformation wie erwartet funktioniert.
8. Wählen Sie **Save** und **Activate**.