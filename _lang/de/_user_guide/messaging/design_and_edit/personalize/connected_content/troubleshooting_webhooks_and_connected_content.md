---
nav_title: Fehlerbehebung bei Webhooks und Connected-Content
article_title: Fehlerbehebung bei Webhook- und Connected-Content-Anfragen
page_order: 4
description: "Diagnostizieren Sie Webhook- und Connected-Content-Fehler mithilfe eines Symptomindex, HTTP-Fehlertabellen und Hinweisen zur Erkennung fehlerhafter Hosts."
---

# Fehlerbehebung bei Webhook- und Connected-Content-Anfragen {#troubleshoot-webhook-and-connected-content-requests}

> Verwenden Sie diese Seite zur Fehlerbehebung häufiger Fehlercodes bei Webhooks und Connected-Content. Informationen zur Einrichtung finden Sie unter [Einen Webhook erstellen]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) und [Einen API-Aufruf durchführen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

## Hier starten: Symptom zuordnen {#start-here-match-your-symptom}

Ordnen Sie Ihr Symptom in der Tabelle zu, um zum entsprechenden Abschnitt zu navigieren.

| Symptom | Gehe zu |
| --- | --- |
| `4XX`-Client-Fehler im Nachrichten-Aktivitätsprotokoll | [4XX-Fehler](#4xx-errors) |
| `5XX`-Server-Fehler oder Timeout | [5XX-Fehler](#5xx-errors) |
| `598 Host Unhealthy` oder kurzzeitig angehaltene Anfragen | [Erkennung fehlerhafter Hosts](#unhealthy-host-detection) |
| Connected-Content wird in der Vorschau oder beim Senden leer dargestellt | [Connected-Content gibt keinen Antworttext zurück](#connected-content-returns-no-response-body) |
| Automatisierte Fehler-E-Mail von Braze | [Automatisierte E-Mails und Einträge im Nachrichten-Aktivitätsprotokoll](#automated-emails-and-message-activity-log-entries) |
| Webhook-Fehlerereignisse in Currents benötigt | [Zusätzliche Fehler-Insights in Braze-Currents](#additional-failure-insights-in-braze-currents) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook- und Connected-Content-Symptom" }

## Standardmäßiger Untersuchungspfad {#standard-investigation-path}

Verwenden Sie diesen Workflow, wenn eine Webhook- oder Connected-Content-Anfrage fehlschlägt oder nicht korrekt gerendert wird. Beginnen Sie bei Schritt 1.

1. Öffnen Sie das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) und notieren Sie den Fehlercode, den Zeitstempel und die Endpunkt-URL.
2. Überprüfen Sie bei `4XX`-Fehlern die Anfrage-Syntax, Authentifizierungs-Header, den URL-Pfad und die HTTP-Methode anhand der Endpunkt-Dokumentation.
3. Überprüfen Sie bei `5XX`-Fehlern den Zustand des Endpunkts, Rate-Limits und ob Braze den Host als fehlerhaft markiert hat.
4. Zeigen Sie bei Connected-Content eine Vorschau der Nachricht für eine Testnutzer:in an und stellen Sie sicher, dass Liquid nicht zu leeren oder JSON-brechenden Werten aufgelöst wird.
5. Falls eine Erkennung fehlerhafter Hosts beteiligt sein könnte, lesen Sie den Abschnitt [Erkennung fehlerhafter Hosts](#unhealthy-host-detection), bevor Sie den [Braze-Support]({{site.baseurl}}/support_contact) kontaktieren.

## 4XX-Fehler {#4xx-errors}

`4XX`-Fehler weisen darauf hin, dass ein Problem mit der an den Endpunkt gesendeten Anfrage vorliegt. Diese Fehler werden in der Regel durch fehlerhafte Anfragen verursacht, einschließlich fehlerhafter Parameter, fehlender Authentifizierungs-Header oder falscher URLs. Beachten Sie, dass diese Fehler auch für den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) gelten.

In der folgenden Tabelle finden Sie Details zu den Fehlercodes und Schritte zur Behebung:

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="4XX-Fehler">
  <thead>
    <tr>
      <th>Fehlercode</th>
      <th>Bedeutung</th>
      <th>Schritte zur Behebung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Bad Request</b></td>
      <td>Die Anfrage enthält eine ungültige Syntax.</td>
      <td>
        <ul>
          <li>Überprüfen Sie den Anfrage-Payload auf Syntaxfehler.</li>
          <li>Stellen Sie sicher, dass alle erforderlichen Felder enthalten und korrekt formatiert sind.</li>
          <li>Wenn Sie einen JSON-Payload senden, validieren Sie die JSON-Struktur.</li>
          <li>Wenn Sie Liquid verwenden, um Personalisierungs-Tags in der Webhook-Anfrage einzufügen, überprüfen Sie, dass Liquid nicht zu einem leeren Wert aufgelöst wird oder JSON-brechende Zeichen erzeugt (z. B. nicht-escapte Anführungszeichen). Zeigen Sie eine Vorschau der Nachricht für eine:n Testnutzer:in an, um zu bestätigen, dass die gerenderte Ausgabe gültig ist.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Unauthorized</b></td>
      <td>Die Anfrage erfordert eine Nutzer:innen-Authentifizierung.</td>
      <td>
        <ul>
          <li>Überprüfen Sie, ob die korrekten Zugangsdaten (z. B. API-Schlüssel oder Token) in den Anfrage-Headern enthalten sind.</li>
          <li>Stellen Sie sicher, dass Sie über die erforderlichen Nutzer:innen-Berechtigungen verfügen, um auf den Endpunkt zuzugreifen.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Forbidden</b></td>
      <td>Der Endpunkt versteht die Anfrage, verweigert jedoch die Autorisierung.</td>
      <td>
        <ul>
          <li>Überprüfen Sie, ob der API-Schlüssel oder das Token über die erforderlichen Berechtigungen verfügt.</li>
          <li>Stellen Sie sicher, dass Sie über die erforderlichen Nutzer:innen-Berechtigungen verfügen, um auf den Endpunkt zuzugreifen.</li>
          <li>Wenn Anfragen konsistent <code>403</code> zurückgeben und die Authentifizierung korrekt erscheint, blockiert möglicherweise Ihr Server, API-Gateway oder Ihre WAF die ausgehenden IP-Adressen von Braze. Setzen Sie die IPs für Ihren Braze-Cluster auf die Allowlist. Für Webhooks siehe <a href="{{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#ip-allowlisting">IP-Allowlisting</a>. Für Connected-Content siehe <a href="{{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting">Connected-Content-IP-Allowlisting</a>.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Not Found</b></td>
      <td>Der Endpunkt kann die angeforderte Ressource nicht finden.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die Endpunkt-URL auf Tippfehler oder falsche Pfade.</li>
          <li>Stellen Sie sicher, dass die Ressource, auf die Sie zugreifen möchten, existiert.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Method Not Allowed</b></td>
      <td>Die Anfragemethode ist dem Endpunkt bekannt, wird aber von der Zielressource nicht unterstützt.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die in der Anfrage verwendete HTTP-Methode (DELETE, GET, POST, PUT).</li>
          <li>Stellen Sie sicher, dass der Endpunkt die von Ihnen verwendete Methode unterstützt.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Request Timeout</b></td>
      <td>Der Endpunkt hat bei der Verarbeitung der Anfrage eine Zeitüberschreitung erreicht.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die in der Anfrage verwendete HTTP-Methode (DELETE, GET, POST, PUT).</li>
          <li>Stellen Sie sicher, dass der Endpunkt die von Ihnen verwendete Methode unterstützt.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflict</b></td>
      <td>Die Anfrage ist aufgrund eines Konflikts mit dem aktuellen Zustand der Ressource unvollständig.</td>
      <td>
        <ul>
          <li>Überprüfen Sie die in der Anfrage verwendete HTTP-Methode (DELETE, GET, POST, PUT).</li>
          <li>Stellen Sie sicher, dass der Endpunkt die von Ihnen verwendete Methode unterstützt.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Too Many Requests</b></td>
      <td>Es wurden zu viele Anfragen in einem bestimmten Zeitraum gesendet.</td>
      <td>
        <ul>
          <li>Senken Sie das Rate-Limit Ihrer Campaign oder Ihres Canvas-Schritts.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 5XX-Fehler {#5xx-errors}

`5XX`-Fehler weisen darauf hin, dass ein Problem mit dem Endpunkt vorliegt. Diese Fehler werden in der Regel durch serverseitige Probleme verursacht.

| Fehlercode                    | Bedeutung                                                                                                                                             |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Internal Server Error** | Der Endpunkt ist auf eine unerwartete Bedingung gestoßen, die ihn daran gehindert hat, die Anfrage abzuschließen.                                    |
| **502 Bad Gateway**           | Der Endpunkt hat eine ungültige Antwort vom Upstream-Server erhalten.                                                                                |
| **503 Service Unavailable**   | Der Endpunkt kann die Anfrage derzeit aufgrund einer vorübergehenden Überlastung oder Wartung nicht bearbeiten.                                      |
| **504 Gateway Timeout**       | Der Endpunkt hat keine rechtzeitige Antwort vom Upstream-Server erhalten.                                                                            |
| **529 Host Overloaded**       | Der Endpunkt-Host ist überlastet und konnte nicht antworten. |
| **598 Host Unhealthy**        | Braze hat die Antwort simuliert, da der Endpunkt-Host vorübergehend als fehlerhaft markiert ist. Weitere Informationen finden Sie unter [Erkennung fehlerhafter Hosts](#unhealthy-host-detection). |
| **599 Connection Error**      | Bei Braze ist ein Netzwerk-Verbindungs-Timeout-Fehler aufgetreten, während versucht wurde, eine Verbindung zum Endpunkt herzustellen. Das bedeutet, dass der Endpunkt möglicherweise instabil oder nicht erreichbar ist. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="5XX-Fehler" }

### 5XX-Fehler beheben {#resolving-5xx-errors}

Hier sind Tipps zur Fehlerbehebung bei häufigen `5XX`-Fehlern:

- Überprüfen Sie die Fehlermeldung auf spezifische Details, die im **Nachrichten-Aktivitätsprotokoll** verfügbar sind. Gehen Sie für Webhooks zum Abschnitt **Performance im Zeitverlauf** auf der Braze-Startseite und wählen Sie die Statistiken für Webhooks aus. Dort finden Sie den Zeitstempel, der angibt, wann die Fehler aufgetreten sind.
- Stellen Sie sicher, dass Sie nicht zu viele Anfragen senden, die den Endpunkt überlasten. Sie können in Stapeln senden oder die Rate-Limits anpassen, um zu prüfen, ob dies die Fehler reduziert.

## Erkennung fehlerhafter Hosts {#unhealthy-host-detection}

Braze-Webhooks und Connected-Content verwenden einen Mechanismus zur Erkennung fehlerhafter Hosts, der erkennt, wenn der Ziel-Host eine hohe Rate an erheblicher Verlangsamung oder Überlastung aufweist, die zu Zeitüberschreitungen, zu vielen Anfragen oder anderen Ergebnissen führt, die Braze daran hindern, erfolgreich mit dem Ziel-Endpunkt zu kommunizieren. Er dient als Schutzmaßnahme, um unnötige Last zu reduzieren, die den Ziel-Host belasten könnte. Er dient auch dazu, die Braze-Infrastruktur zu stabilisieren und schnelle Messaging-Geschwindigkeiten aufrechtzuerhalten.

Die Erkennungsschwellenwerte unterscheiden sich zwischen Webhooks und Connected-Content:
- **Für Webhooks**: Wenn die Anzahl der Fehler 3.000 in einem beliebigen gleitenden Zeitfenster von einer Minute überschreitet (pro eindeutiger Kombination aus Hostname und App-Gruppe&#8212;nicht pro Endpunkt-Pfad), stoppt Braze vorübergehend Anfragen an den Ziel-Host für eine Minute.
- **Für Connected-Content**: Wenn die Anzahl der Fehler 3.000 überschreitet UND die Fehlerrate 90 % in einem beliebigen gleitenden Zeitfenster von einer Minute übersteigt (pro eindeutiger Kombination aus Hostname und App-Gruppe&#8212;nicht pro Endpunkt-Pfad), stoppt Braze vorübergehend Anfragen an den Ziel-Host für eine Minute.

Wenn Anfragen gestoppt werden, simuliert Braze Antworten mit einem `598`-Fehlercode, um den schlechten Zustand anzuzeigen. Nach einer Minute nimmt Braze die Anfragen mit voller Geschwindigkeit wieder auf, wenn der Host als gesund erkannt wird. Wenn der Host weiterhin fehlerhaft ist, wartet Braze eine weitere Minute, bevor es erneut versucht.

Die folgenden Fehlercodes tragen zur Fehlerzählung des Detektors für fehlerhafte Hosts bei: `408`, `429`, `502`, `503`, `504`, `529`.

Für Webhooks wiederholt Braze automatisch HTTP-Anfragen, die vom Detektor für fehlerhafte Hosts gestoppt wurden. Diese automatische Wiederholung verwendet exponentielles Backoff und wiederholt nur wenige Male, bevor sie fehlschlägt. Weitere Informationen zu Webhook-Fehlern finden Sie unter [Fehler, Wiederholungslogik und Zeitüberschreitungen]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#errors-retry-logic-and-timeouts).

Für Connected-Content fährt Braze, wenn Anfragen an den Ziel-Host vom Detektor für fehlerhafte Hosts gestoppt werden, fort, Nachrichten zu rendern und Ihrer Liquid-Logik zu folgen, als hätte es einen Fehler-Antwortcode erhalten. Wenn Sie sicherstellen möchten, dass diese Connected-Content-Anfragen wiederholt werden, wenn sie vom Detektor für fehlerhafte Hosts gestoppt werden, verwenden Sie die Option `:retry`. Weitere Informationen zur Option `:retry` finden Sie unter [Connected-Content-Wiederholungen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

Wenn Sie glauben, dass die Erkennung fehlerhafter Hosts Probleme verursacht, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/support_contact).

### Connected-Content gibt keinen Antworttext zurück {#connected-content-returns-no-response-body}

**Symptom:** Ein Connected-Content-Aufruf wird in Ihrer Nachrichtenvorschau oder beim Senden leer gerendert.

Wenn ein Connected-Content-Aufruf in Ihrer Nachrichtenvorschau oder beim Senden leer gerendert wird, prüfen Sie Folgendes:

- **Geschützte Leerzeichen in der URL:** Braze entfernt geschützte Leerzeichen (`&nbsp;` oder Unicode `U+00A0`) aus Connected-Content-URLs, bevor die Anfrage gesendet wird. Wenn Ihre URL aus einem Dokument oder Dashboard-Feld kopiert wurde, das geschützte Leerzeichen zwischen Zeichen eingefügt hat, kann die Anfrage fehlschlagen oder keinen verwendbaren Antworttext zurückgeben. Geben Sie die URL im Klartext erneut ein oder entfernen Sie versteckte Leerzeichen und zeigen Sie dann erneut die Vorschau an.
- **Weiterleitungsantworten (`3xx`):** Connected-Content folgt keinen Weiterleitungen. Nur `2xx`-Antworten werden als erfolgreich behandelt, sodass ein `301` oder `302` leer gerendert werden kann, selbst wenn dieselbe URL in Postman funktioniert. Verwenden Sie die endgültige Ziel-URL oder konfigurieren Sie den Endpunkt so, dass er eine `2xx`-Antwort (typischerweise `200`) an der von Braze aufgerufenen URL zurückgibt. Siehe [Warum schlägt Connected-Content fehl, wenn mein Endpunkt eine Weiterleitung zurückgibt?]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#why-does-connected-content-fail-when-my-endpoint-returns-a-redirect-301-or-302).
- **HTTP-Fehler und leere Antworttexte:** Bei Statuscodes außerhalb des `2xx`-Bereichs oder blockierten Hosts kann Connected-Content einen leeren String rendern. Siehe [Einen API-Aufruf durchführen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) und überprüfen Sie Fehler im **Nachrichten-Aktivitätsprotokoll**.

## Automatisierte E-Mails und Einträge im Nachrichten-Aktivitätsprotokoll {#automated-emails-and-message-activity-log-entries}

### Einrichtung automatisierter E-Mails {#setting-up-automated-emails}

Wenn in einem Workspace innerhalb von 24 Stunden mehr als 100.000 Webhook- oder Connected-Content-Endpunkt-Fehler (einschließlich Wiederholungen) auftreten, sendet Braze Ihnen eine E-Mail mit den folgenden Informationen zur Behebung der Fehler.

- Name des Workspace
- Ein Link zum Canvas oder zur Campaign
- Endpunkt-URL
- Fehlercode
- Zeitpunkt, zu dem der Fehler zuletzt beobachtet wurde
- Links zum Nachrichten-Aktivitätsprotokoll und zur zugehörigen Dokumentation

{% alert note %}
Sie können den Fehlerschwellenwert pro Workspace konfigurieren. Um diesen Schwellenwert anzupassen, kontaktieren Sie den [Braze-Support]({{site.baseurl}}/support_contact).
{% endalert %}

Die Endpunkt-Fehler sind:

- **`4XX`:** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX`:** `500`, `502`, `503`, `504`, `598`, `599`

Diese E-Mails werden nur einmal pro Tag auf Workspace-Ebene gesendet. Wenn sich keine Nutzer:innen für diese E-Mails anmelden, benachrichtigt Braze alle Unternehmensadministratoren.

Um sich für den Empfang dieser E-Mails anzumelden, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Präferenzen für Benachrichtigungen**.
2. Wählen Sie **Connected Content Errors** und **Webhook Errors** im Abschnitt **Canvas & Campaigns** aus.

### Einträge im Nachrichten-Aktivitätsprotokoll {#message-activity-log-entries}

Wenn ein Fehler auftritt, gibt es mindestens einen Eintrag im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), der damit zusammenhängt. Wenn die Anfrage wiederholt wird und schließlich erfolgreich ist, sind diese Details in Currents und der Snowflake-Datenfreigabe verfügbar. Beachten Sie, dass selbst wenn eine Anfrage nach einer Wiederholung schließlich erfolgreich ist, die Fehler dennoch die automatisierte E-Mail auslösen können.

### Zusätzliche Fehler-Insights in Braze-Currents {#additional-failure-insights-in-braze-currents}

Um die Transparenz bei Webhook-bezogenen Problemen zu erhöhen, streamt Braze detaillierte Webhook-Fehlerereignisse an Currents und die Snowflake-Datenfreigabe. Diese Ereignisse umfassen fehlgeschlagene Webhook-Anfragen (wie HTTP-`4xx`- oder `5xx`-Antworten) und bieten mehr Beobachtbarkeit darüber, wie Webhook-Probleme die Nachrichtenzustellung beeinflussen können. Beachten Sie, dass Fehlerereignisse sowohl terminale Fehler als auch Fehler umfassen, die wiederholt werden.

{% alert note %}
Connected-Content-Anfragen sind in diesen Webhook-Fehlerereignissen nicht enthalten.
{% endalert %}

Weitere Informationen finden Sie im [Glossar der Nachrichten-Engagement-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).