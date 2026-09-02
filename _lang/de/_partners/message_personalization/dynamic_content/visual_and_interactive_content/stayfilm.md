---
nav_title: Stayfilm
article_title: Stayfilm
description: "Erfahren Sie, wie Sie das personalisierte Video-Rendering von Stayfilm mithilfe von Webhook-Campaigns, Connected Content und Datentransformation in Braze integrieren."
alias: /partners/stayfilm/
page_type: partner
search_tag: Partner
---

# Stayfilm

> [Stayfilm](https://www.stayfilm.com/) ist eine REST API für die automatisierte, personalisierte Videoproduktion in großem Umfang. Die Plattform integriert Daten, Bilder, Text, Soundtracks, Narration und visuelle Effekte, um angepasste Videoinhalte für E-Commerce, Marktplätze, CRM-Workflows und Marketing-Campaigns zu generieren.
>
> Diese Integration sendet Render-Jobs von Braze an die Stayfilm-API, empfängt Callbacks, wenn Videos bereit sind, und speichert Video-URLs und Status in Nutzerprofilen zur Verwendung in Campaigns und Canvases.

_Diese Integration wird von Stayfilm gepflegt._

## Anwendungsfälle {#use-cases}

Stayfilm unterstützt die personalisierte Videozustellung über den gesamten Kundenlebenszyklus hinweg, unter anderem für:

- **Onboarding und Willkommens-Journeys:** Begrüßen Sie neue Nutzer:innen mit Videos, die auf ihr Profil oder ihren Anmeldekontext zugeschnitten sind
- **Produkt- und Marktplatzinhalte:** Generieren Sie produktbezogene Videos aus Katalogen oder von Nutzer:innen bereitgestellten Medien
- **Konversion und Aktivierung:** Verstärken Sie wichtige Aktionen mit kontextuellem Video-Messaging
- **Kundenbindung und Upselling:** Heben Sie personalisierte Angebote oder Nutzungsmeilensteine im Videoformat hervor
- **Rückgewinnung und Abwanderung-Prävention:** Reaktivieren Sie inaktive Nutzer:innen mit maßgeschneiderten Videoinhalten

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Folgendes vorhanden ist:

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Stayfilm-API-Zugang | Kontaktieren Sie Stayfilm, um Ihre Projekt-Zugangsdaten zu erhalten, einschließlich `idproject`, `Subscription-Key`, OAuth-Client-Zugangsdaten und die Stayfilm-API-Basis-URL. Informationen zur Authentifizierung und zu Endpunkten finden Sie in der [Stayfilm-API-Dokumentation](https://apidoc.stayfilm.com). |
| Braze-Datentransformation | Verwenden Sie die [Braze-Datentransformation]({{site.baseurl}}/user_guide/data/unification/data_transformation), um Stayfilm-Callbacks zu empfangen und sie über den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) Braze-Nutzerprofilen zuzuordnen. |
| Braze-Nutzerbezeichner | Diese Anleitung verwendet `external_id`, um Stayfilm-Jobs mit Braze-Nutzerprofilen zu verknüpfen. Der Wert, den Sie in `CallbackRelayData` übergeben, muss mit der `external_id` der Nutzer:innen in Braze übereinstimmen. |
| Braze-Sandbox (empfohlen) | Testen Sie die Integration in einem Braze-Sandbox-Workspace, bevor Sie sie in der Produktionsumgebung einsetzen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## So funktioniert die Integration {#how-the-integration-works}

Diese Integration verwendet einen bidirektionalen Webhook-Ablauf:

1. **Ausgehend:** Eine Braze-[Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks) sendet einen Render-Auftrag an den Stayfilm-Endpunkt `POST /Job`. Die Anfrage enthält Nutzermedien, die Template-Konfiguration und `CallbackRelayData`, das auf die `external_id` der/des Braze-Nutzer:in gesetzt ist.
2. **Eingehend:** Wenn Stayfilm das Rendering abgeschlossen hat, sendet es einen Callback an Ihre Braze-Datentransformations-Webhook-URL. Die Transformation bildet die Antwort auf [angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) und angepasste Events im entsprechenden Kundenprofil ab.
3. **Zustellung:** Verwenden Sie das gespeicherte Attribut `stayfilm_video_url` in Messaging-Kanälen, z. B. in einer [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages) mit benutzerdefiniertem HTML.

Die Datentransformation in dieser Anleitung schreibt die folgenden angepassten Attribute:

| Attribut | Beschreibung |
| --------- | ----------- |
| `stayfilm_video_status` | `ready`, wenn das Rendering erfolgreich ist, oder `failed`, wenn Stayfilm einen Fehler meldet |
| `stayfilm_video_url` | URL des gerenderten MP4-Videos |
| `stayfilm_job_id` | Stayfilm-Auftragsbezeichner |
| `stayfilm_render_error` | Fehlermeldung, wenn das Rendering fehlschlägt |
| `stayfilm_callback_received_at` | ISO-Zeitstempel des Callbacks |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angepasste Attribute" }

Die Transformation zeichnet außerdem angepasste Events mit den Namen `stayfilm_video_ready` oder `stayfilm_video_failed` auf.

## Integration

Die folgenden Schritte führen Sie durch einen Proof of Concept. Nachdem Sie den Ablauf validiert haben, passen Sie den Job-Payload, die Attribute und das Messaging an Ihren Anwendungsfall an.

### Schritt 1: Testnutzer:in erstellen {#step-1-create-a-test-user}

Erstellen Sie ein Testnutzerprofil, das Sie beim Aufbau und der Validierung der Integration verwenden. Weitere Informationen finden Sie unter [Nutzer:innen importieren]({{site.baseurl}}/user_guide/audience/manage_audience/import_users).

1. Gehen Sie zu **Audience** > **Import Users**.
2. Wählen Sie **Quick User Add** aus.
3. Geben Sie eine `external_id` und alle weiteren erforderlichen Felder ein und wählen Sie dann **Create new user** aus.

{% alert important %}
Verwenden Sie keine personenbezogenen Daten – wie E-Mail, Telefonnummer, vollständigen Namen, Ausweisnummer, Adresse oder Bestelldetails – als `external_id`. Behandeln Sie `external_id` in dieser gesamten Integration als case-sensitive.
{% endalert %}

Diese Anleitung verwendet `stayfilm-poc-001` als Beispiel-`external_id`. Notieren Sie sich den gewählten Wert, da Sie ihn in späteren Schritten benötigen.

### Schritt 2: Datentransformation erstellen {#step-2-create-a-data-transformation}

Erstellen Sie eine Datentransformation, um Stayfilm-Callbacks zu empfangen und Nutzerprofile zu aktualisieren.

1. Gehen Sie zu **Data Settings** > **Data Transformation**.
2. Wählen Sie **Create transformation** aus.
3. Geben Sie einen Namen ein, z. B. `Stayfilm Callback Data Transformation`.
4. Wählen Sie unter **Editing experience** die Option **Start from scratch** aus.
5. Wählen Sie unter **Select destination** > **Destination** die Option **POST: Track users** aus.
6. Wählen Sie **Create transformation** aus.
7. Ersetzen Sie den Standard-Transformationscode durch Folgendes:

```javascript
const brazeExternalId = payload.RelayedData;
if (!brazeExternalId) {
  throw new Error("Missing RelayedData. Expected Stayfilm callback to relay the Braze external_id from CallbackRelayData.");
}

const idJob = payload.IdJob || null;
const producedFiles = payload.ProducedFiles || {};
const videoUrl = producedFiles?.Videos?.VideoMP4?.Url || null;
const errorMessage = payload.ErrorMessage || null;
const hasError = payload.HasError === true || Boolean(errorMessage);
const isReady = !hasError && Boolean(videoUrl);
const now = new Date().toISOString();

let brazecall = {
  attributes: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      stayfilm_video_status: isReady ? "ready" : "failed",
      stayfilm_video_url: videoUrl || null,
      stayfilm_job_id: idJob,
      stayfilm_render_error: errorMessage,
      stayfilm_callback_received_at: now
    }
  ],
  events: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      name: isReady ? "stayfilm_video_ready" : "stayfilm_video_failed",
      time: now,
      properties: {
        stayfilm_job_id: idJob,
        stayfilm_video_url: videoUrl || null,
        stayfilm_render_error: errorMessage,
        stayfilm_status: payload.Status || payload.status || null
      }
    }
  ]
};

return brazecall;
```

{: start="8"}
8. Wählen Sie **Save** aus und kopieren Sie dann die generierte Webhook-URL.
9. Senden Sie eine Test-`POST`-Anfrage an die Webhook-URL mit dem folgenden Beispiel-Stayfilm-Callback-JSON. Setzen Sie `RelayedData` auf die `external_id` der Testnutzer:in, die Sie in Schritt 1 erstellt haben.

```json
{
  "IdJob": "debug-job-001",
  "HasError": false,
  "Status": "DRAFT_DONE",
  "ProducedFiles": {
    "Videos": {
      "VideoMP4": {
        "Url": "https://example.com/stayfilm-poc-video.mp4"
      }
    }
  },
  "RelayedData": "stayfilm-poc-001"
}
```

Senden Sie die Anfrage mit cURL, Postman oder einem ähnlichen Tool. Eine erfolgreiche Antwort gibt den HTTP-Status `201` mit `{"message": "success"}` zurück.

{: start="10"}
10. Gehen Sie zu **Data Settings** > **Data Transformation** und laden Sie die Seite neu, wenn Ihre Transformation nicht in der Liste erscheint.
11. Öffnen Sie die Transformation und wählen Sie **Validate** aus. Bestätigen Sie, dass die Validierung unter **Output** erfolgreich ist.
12. Wählen Sie **Activate** aus.
13. Stellen Sie Stayfilm die kopierte Webhook-URL als Ihre Callback-URL bereit.

{% alert note %}
Wenn Sie mehr als die Braze-`external_id` in `CallbackRelayData` speichern, aktualisieren Sie den Transformationscode, um `RelayedData` entsprechend zu parsen.
{% endalert %}

### Schritt 3: Webhook-Campaign zum Senden von Jobs an Stayfilm erstellen {#step-3-create-a-webhook-campaign-to-send-jobs-to-stayfilm}

Erstellen Sie eine [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks), die Render-Jobs an Stayfilm übermittelt.

{% alert important %}
Bevor Sie die Campaign testen, bestätigen Sie, dass Stayfilm Ihr Projekt mit der Datentransformations-Callback-URL aus Schritt 2 konfiguriert hat.
{% endalert %}

1. Gehen Sie zu **Messaging** > **Campaigns**.
2. Wählen Sie **Create campaign** > **Webhook** aus.
3. Geben Sie einen Campaign-Namen ein, z. B. `Stayfilm Webhook Integration`.
4. Wählen Sie **Compose webhook** > **Start from scratch** aus.
5. Geben Sie unter **Compose Webhook** > **Webhook URL** die von Stayfilm bereitgestellte `POST /Job`-Endpunkt-URL ein. Ersetzen Sie *`{BASE_URL}`* im folgenden Beispiel: `https://{BASE_URL}/stg/v3/job`
6. Setzen Sie **HTTP method** auf **POST**.
7. Wählen Sie unter **Request Body** die Option **Raw Text** aus und fügen Sie dann den von Stayfilm bereitgestellten Job-Payload ein. Sie können [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) verwenden, um den Body dynamisch zu gestalten.

Fügen Sie `CallbackRelayData` ein, das auf die `external_id` der Braze-Nutzer:innen gesetzt ist. Stayfilm gibt diesen Wert im Callback als `RelayedData` zurück.

{% raw %}
```json
{
  "SmartTags": ["Setup-Template"],
  "Medias": [
    {
      "Group": "userMedia",
      "URL": "https://{BASE_URL}/some_media.png"
    }
  ],
  "Videos": [{}],
  "CallbackRelayData": "stayfilm-poc-001"
}
```
{% endraw %}

Fügen Sie die folgenden Anfrage-Header hinzu:

| Schlüssel | Wert |
| --- | ----- |
| `idproject` | Der von Stayfilm bereitgestellte `idproject`-Wert |
| `Subscription-Key` | Der von Stayfilm bereitgestellte `Subscription-Key` |
| `Content-Type` | `application/json` |
| `Authorization` | OAuth-Bearer-Token, das über Connected Content abgerufen wird (siehe folgendes Beispiel) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anfrage-Header" }

Ersetzen Sie im folgenden Connected-Content-Block *`{TENANT_ID}`*, *`{CLIENT_ID}`*, *`{CLIENT_SECRET_URL_ENCODED}`* und *`{SCOPE_URL_ENCODED}`* durch die von Stayfilm bereitgestellten Werte. URL-kodieren Sie *`{CLIENT_SECRET_URL_ENCODED}`* und *`{SCOPE_URL_ENCODED}`*, bevor Sie sie in den Block einfügen. Informationen zu den OAuth-Anforderungen finden Sie in der [Stayfilm-API-Dokumentation](https://apidoc.stayfilm.com).

{% raw %}
```
{% connected_content https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token
  :method post
  :body grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET_URL_ENCODED}&scope={SCOPE_URL_ENCODED}
  :content_type application/x-www-form-urlencoded
  :cache_max_age 3000
  :save stayfilm_auth
%}Bearer {{stayfilm_auth.access_token}}
```
{% endraw %}

{: start="8"}
8. Wählen Sie **Save Draft** aus.

{% alert note %}
Wenn Sie die Campaigns-Seite verlassen und zurückkehren, setzen Sie **Status** auf **All**, um Campaigns zu finden, die sich noch im Status **Draft** befinden.
{% endalert %}

### Schritt 4: Webhook-Campaign testen {#step-4-test-the-webhook-campaign}

1. Wählen Sie im Webhook-Composer den Tab **Test** aus.
2. Wählen Sie unter **Preview message as user** die Option **Select existing user** aus und suchen Sie dann nach Ihrer Testnutzer:in (z. B. `stayfilm-poc-001`).
3. Wählen Sie **Send test** aus.

Eine erfolgreiche Antwort gibt den HTTP-Status `201` mit einem JSON-Body zurück, der dem folgenden ähnelt:

```json
{
  "IdJob": "4557a77e-f56c-48be-81f7-2d8c5e558cb1",
  "Videos": [
    {
      "IdVideo": "87287b25-7814-4fa1-ad1a-f2ea89822d0f",
      "IdGenre": "f07a1334-5904-420a-9f31-92644f245c5a",
      "IdVideoTemplate": "7b77c3df-12a1-4636-a9b4-bc227f4c233f",
      "IdProject": "73ea3e73-b41e-4676-b674-51731d3bf49c",
      "Status": "DRAFT_RENDERING_PENDING",
      "DurationInSeconds": null,
      "URL": null,
      "ErrorMessage": null,
      "CreatedAt": "2026-06-16T00:35:28.7736263Z",
      "UpdatedAt": "2026-06-16T00:35:28.7736264Z",
      "IdVideoFather": null,
      "IdVideoSon": null,
      "ProducingStatus": "PENDING"
    }
  ],
  "Images": []
}
```

### Schritt 5: Stayfilm-Callback bestätigen {#step-5-confirm-the-stayfilm-callback}

Stayfilm rendert das Video asynchron und sendet einen Callback an Ihre Datentransformation, wenn die Verarbeitung abgeschlossen ist. Überwachen Sie den Job-Status über die Stayfilm-API-Endpunkte, die in der [Stayfilm-API-Dokumentation](https://apidoc.stayfilm.com) beschrieben sind.

1. Gehen Sie zu **Data Settings** > **Data Transformation**.
2. Wählen Sie den Tab **Logs** für Ihre Transformation aus.
3. Bestätigen Sie, dass ein Callback mit dem Status **Success** angezeigt wird.

### Schritt 6: Video in einer In-App-Nachricht anzeigen {#step-6-display-the-video-in-an-in-app-message}

Nachdem `stayfilm_video_url` im Kundenprofil befüllt ist, zeigen Sie das gerenderte Video in einer Campaign oder einem Canvas an.

1. Gehen Sie zu **Messaging** > **Campaigns**.
2. Wählen Sie **Create campaign** > **In-app message** aus.
3. Geben Sie einen Campaign-Namen ein, z. B. `Stayfilm Video Show`.
4. Wählen Sie im Nachrichten-Editor den **Traditional Editor** aus.
5. Wählen Sie unter **Send To** die Option **Web Browsers** aus.
6. Setzen Sie **Message Type** auf **Custom Code**.
7. Fügen Sie das folgende HTML in das Feld **HTML** ein:

{% raw %}
```html
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<div id="stayfilm-video-url" style="display: none;">{{custom_attribute.${stayfilm_video_url}}}</div>
<video id="stayfilm-video" controls preload="metadata" playsinline style="width: 100%; max-width: 420px; border-radius: 12px; background: #000;">
Your browser does not support HTML5 video.
</video>
<script>
(function () {
  var urlElement = document.getElementById("stayfilm-video-url");
  var video = document.getElementById("stayfilm-video");
  var videoUrl = urlElement ? urlElement.textContent.trim() : "";
  if (!videoUrl || videoUrl.indexOf("http") !== 0) {
    return;
  }
  var source = document.createElement("source");
  source.src = videoUrl;
  source.type = "video/mp4";
  video.appendChild(source);
  video.load();
})();
</script>
</body>
</html>
```
{% endraw %}

{: start="8"}
8. Wählen Sie **Save Draft** aus.
9. Wählen Sie den Tab **Test** aus.
10. Wählen Sie unter **Preview message as user** die Option **Select existing user** aus und suchen Sie dann nach der `external_id` Ihrer Testnutzer:in.

Das gerenderte Video wird in der Vorschau angezeigt und abgespielt, wenn `stayfilm_video_url` im Profil gesetzt ist.

## Integration erweitern {#extend-the-integration}

Diese Anleitung deckt einen Teil der Stayfilm-API ab. Um Job-Templates, Medieneingaben oder nachgelagertes Messaging anzupassen, lesen Sie die [Stayfilm-API-Dokumentation](https://apidoc.stayfilm.com) und aktualisieren Sie Ihren Webhook-Payload, die Datentransformations-Abbildung und die Campaign-Logik entsprechend.

## Überlegungen {#considerations}

- **Asynchrones Rendering:** Die Videogenerierung erfolgt nicht sofort. Triggern Sie Folgenachrichten über das angepasste Event `stayfilm_video_ready` oder ein Segment basierend auf `stayfilm_video_status`, anstatt die In-App-Nachricht im selben Flow wie den Webhook zu senden.
- **Konsistenz der Bezeichner:** Der Wert in `CallbackRelayData` muss exakt mit der `external_id` der Braze-Nutzer:innen übereinstimmen.
- **OAuth-Token-Caching:** Das Connected-Content-Beispiel speichert das OAuth-Token für 3000 Sekunden im Cache. Passen Sie `cache_max_age` an, falls Stayfilm die Anforderungen für die Token-Lifetime ändert.
- **Sandbox-Tests:** Validieren Sie den vollständigen Callback-Loop in einer Braze-Sandbox, bevor Sie in die Produktionsumgebung wechseln.
- **Kapazität für angepasste Attribute:** Stellen Sie sicher, dass Ihr Workspace über ausreichend Kapazität für die angepassten Attribute und Events verfügt, die diese Stayfilm-Integration erstellt.

## Fehlerbehebung {#troubleshooting}

In der folgenden Tabelle finden Sie Lösungen für mögliche Probleme mit der Stayfilm-Integration.

| Problem | Lösung |
| ----- | ---------- |
| Die Validierung der Datentransformation schlägt fehl | Stellen Sie sicher, dass `RelayedData` in Ihrem Test-Payload einer gültigen Braze `external_id` entspricht, und laden Sie dann die Seite **Datentransformation** neu, bevor Sie **Validate** auswählen. |
| Der Webhook-Test gibt eine Antwort zurück, die nicht 201 ist | Überprüfen Sie die Stayfilm-Zugangsdaten in Ihren Anfrage-Headern, stellen Sie sicher, dass der OAuth-Connected-Content-Block URL-kodierte Werte verwendet, und prüfen Sie, ob Ihre `POST /Job`-URL korrekt ist. |
| Der Callback erscheint nicht in den Transformationsprotokollen | Stellen Sie sicher, dass Stayfilm Ihre aktive Datentransformations-Webhook-URL hat, und warten Sie, bis das Video-Rendering abgeschlossen ist. |
| Die In-App-Vorschau zeigt das Video nicht an | Stellen Sie sicher, dass `stayfilm_video_url` im Profil der Testnutzer:in gesetzt ist und dass die In-App-Nachricht auf **Web Browsers** mit **Custom Code** ausgerichtet ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }