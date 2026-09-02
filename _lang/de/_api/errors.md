---
nav_title: Fehler und Antworten
article_title: API-Fehler und Antworten
description: "Dieser Referenzartikel behandelt die verschiedenen Fehler und Server-Antworten, die bei der Verwendung der Braze API auftreten können, und wie Sie diese beheben können."
page_type: reference
page_order: 2.3

---
# API-Fehler und Antworten {#api-errors-and-responses}

> Dieser Referenzartikel behandelt die verschiedenen Fehler und Server-Antworten, die bei der Verwendung der Braze API auftreten können, und wie Sie diese beheben können.

## Serverantworten {#server-responses}

Wenn Ihr POST-Payload von unseren Servern akzeptiert wurde, werden erfolgreiche Nachrichten mit der folgenden Antwort bestätigt:

```json
{
  "message" : "success"
}
```

Beachten Sie, dass „success“ lediglich bedeutet, dass der RESTful-API-Payload korrekt geformt und an unsere Push-Benachrichtigungs-, E-Mail- oder andere Messaging-Dienste weitergeleitet wurde. Es bedeutet nicht, dass die Nachrichten tatsächlich zugestellt wurden, da zusätzliche Faktoren die Zustellung verhindern könnten (zum Beispiel könnte ein Gerät offline sein, das Push-Token / Textbaustein könnte von den Apple-Servern abgelehnt werden, oder Sie haben möglicherweise eine unbekannte Nutzer-ID angegeben).

### Warum gibt meine Anfrage „success“ zurück, obwohl keine Nachricht zugestellt wurde? {#why-does-my-request-return-success-when-no-message-was-delivered}

Eine `message: success`- oder `2XX`-Antwort bedeutet, dass Braze die Anfrage für die beteiligten Endpunkte akzeptiert und in die Warteschlange gestellt hat – nicht, dass jede Empfängerin oder jeder Empfänger eine Nachricht erhalten hat. Beim Messaging hängt die Zustellung weiterhin von der Kanalberechtigung, Tokens, Anbieterfehlern und der Inhaltsvalidierung ab. Sehen Sie sich die Tabelle der [schwerwiegenden Fehler]({{site.baseurl}}/api/errors#fatal-errors) für HTTP-Fehler an, die den Versand blockieren, sowie die Analytics Ihrer Campaign oder Ihres Canvas für nachgelagerte Zustellungsmetriken.

Für Endpunkte wie [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), die keine Nachrichten senden, bedeutet eine Erfolgsmeldung lediglich, dass Braze die Anfrage zur Verarbeitung erhalten hat. Wenn nach der Verarbeitung keine Übereinstimmung für den Alias gefunden wird, wird die Anfrage gestoppt.

Wenn Ihre Nachricht erfolgreich ist, aber nicht schwerwiegende Fehler enthält, erhalten Sie die folgende Antwort:

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

Im Fall eines Erfolgs werden alle Nachrichten, die nicht von einem Fehler im `errors`-Array betroffen waren, weiterhin zugestellt. Wenn Ihre Nachricht einen schwerwiegenden Fehler enthält, erhalten Sie die folgende Antwort:

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Antworten für getrackte Sende-IDs {#responses-for-tracked-send-ids}

Analytics sind für Campaigns immer verfügbar. Darüber hinaus sind Analytics für eine bestimmte Campaign-Sendeinstanz verfügbar, wenn die Campaign als Broadcast versendet wird. Wenn Tracking für eine bestimmte Campaign-Sendeinstanz verfügbar ist, erhalten Sie die folgende Antwort:

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

Die bereitgestellte Sende-ID kann als Parameter für den `/send/data_series`-Endpunkt verwendet werden, um sendespezifische Analytics abzurufen.

## Fehler {#errors}

Das Statuscode-Element einer Serverantwort ist eine 3-stellige Zahl, wobei die erste Ziffer des Codes die Klasse der Antwort definiert.

- Die **2XX-Klasse** der Statuscodes (nicht schwerwiegend) zeigt an, dass **Ihre Anfrage** erfolgreich empfangen, verstanden und akzeptiert wurde.
- Die **4XX-Klasse** der Statuscodes (schwerwiegend) weist auf einen **Client-Fehler** hin. Siehe das Chart der schwerwiegenden Fehler für eine vollständige Liste der 4XX-Fehlercodes und Beschreibungen.
- Die **5XX-Klasse** der Statuscodes (schwerwiegend) weist auf einen **Serverfehler** hin. Es gibt mehrere mögliche Ursachen, zum Beispiel: Der Server, auf den Sie zugreifen möchten, kann die Anfrage nicht ausführen, der Server befindet sich in der Wartung und kann die Anfrage nicht ausführen, oder der Server verzeichnet ein hohes Traffic-Aufkommen. In diesem Fall empfehlen wir, die Anfrage mit exponentiellem Backoff erneut zu versuchen. Im Falle eines Vorfalls oder Ausfalls ist Braze nicht in der Lage, Representational State Transfer-API-Aufrufe, die während des Vorfallszeitraums fehlgeschlagen sind, erneut abzuspielen. Sie müssen alle Aufrufe, die während des Vorfallszeitraums fehlgeschlagen sind, selbst wiederholen.
  - Ein **502-Fehler** ist ein Fehler, bevor die Anfrage den Zielserver erreicht.
  - Ein **503-Fehler** bedeutet, dass die Anfrage den Zielserver erreicht hat, aber die Anfrage nicht abgeschlossen werden kann, weil nicht genügend Kapazität vorhanden ist, ein Netzwerkproblem besteht oder Ähnliches.
  - Ein **504-Fehler** weist darauf hin, dass ein Server keine Antwort von einem anderen vorgelagerten Server erhalten hat.

### Schwerwiegende Fehler {#fatal-errors}

Die folgenden Statuscodes und zugehörigen Fehlermeldungen werden zurückgegeben, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt.

{% alert warning %}
Bei allen folgenden Fehlercodes werden keine Nachrichten gesendet.
{% endalert %}

| Fehlercode | Beschreibung |
|---|---|
| `5XX Internal Server Error` | Versuchen Sie Ihre Anfrage mit exponentiellem Backoff erneut.|
| `400 Bad Request` | Fehlerhafte Syntax. Ungültiges JSON gibt HTTP 400 zurück. Das Feld `error` kann eine Nachricht enthalten, dass Sie gültiges `application/json` im Anfragekörper übergeben müssen, oder `Error while parsing request body. Please check your syntax.` Siehe [Fehler beim Parsen des Anfragekörpers](#error-while-parsing-request-body).|
| `400 No Recipients` | Es sind keine externen IDs oder Segment-IDs bzw. keine Push-Token / Textbaustein in der Anfrage vorhanden.|
| `400 Invalid Campaign ID` | Es wurde keine Messaging-API-Campaign für die von Ihnen angegebene Campaign-ID gefunden.|
| `400 Message Variant Unspecified` | Sie haben eine Campaign-ID angegeben, aber keine Nachrichtenvarianten-ID.|
| `400 Invalid Message Variant` | Sie haben eine gültige Campaign-ID angegeben, aber die Nachrichtenvarianten-ID stimmt mit keiner der Nachrichten dieser Campaign überein.|
| `400 Mismatched Message Type` | Sie haben eine Nachrichtenvariante des falschen Nachrichtentyps für mindestens eine Ihrer Nachrichten angegeben.|
| `400 Invalid Extra Push Payload` | Sie haben den Schlüssel `extra` für `apple_push` oder `android_push` angegeben, aber es handelt sich nicht um ein Dictionary.|
| `400 Max Input Length Exceeded` | Bei `/users/track` wird dieser Fehler durch Überschreitung der maximal zulässigen Anzahl von Objekten in einer einzelnen Anfrage verursacht. Das Limit hängt vom Rate-Limit-Modell ab: Für die meisten Kund:innen unterstützt jede Anfrage bis zu 75 Objekte insgesamt, kombiniert über `attributes`, `events` und `purchases`. Für Kund:innen mit veralteten Rate-Limits unterstützt jedes Array bis zu 75 Objekte unabhängig voneinander. Weitere Informationen finden Sie unter [POST: Nutzer:innen erstellen und Update or aktualisieren or aktualisieren]({{site.baseurl}}/api/endpoints/user_data/post_user_track).|
| `400 The max number of external_ids and aliases per request was exceeded` | Wird durch den Aufruf von mehr als 50 externen IDs verursacht.|
| `400 The max number of ids per request was exceeded` | Wird durch den Aufruf von mehr als 50 externen IDs verursacht.|
| `400 No message to send` | Es wurde kein Payload für die Nachricht angegeben.|
| `400 Slideup Message Length Exceeded` | Die Slideup-Nachricht enthält mehr als 140 Zeichen.|
| `400 Apple Push Length Exceeded` | Der JSON-Payload umfasst mehr als 1.912 Bytes.|
| `400 Android Push Length Exceeded` | Der JSON-Payload umfasst mehr als 4.000 Bytes.|
| `400 Bad Request` | Der `send_at`-Datetime-Wert kann nicht geparst werden.|
| `400 Bad Request` | In Ihrer Anfrage ist `in_local_time` auf „true“ gesetzt, aber `time` liegt bereits in der Zeitzone Ihres Unternehmens in der Vergangenheit.|
| `401 Unauthorized` | Ungültiger API-Schlüssel. Häufige Ursachen sind:<br><br>- **Fehlender oder fehlerhafter Authorization-Header.** Der Header-Wert muss `Bearer` gefolgt von einem Leerzeichen und dann Ihrem API-Schlüssel sein: `Authorization: Bearer YOUR-API-KEY`. Häufige Fehler sind das Auslassen von `Bearer`, das Auslassen des Schlüssels nach `Bearer` oder das Umschließen des Werts mit Anführungszeichen.<br>- **Falscher Representational State Transfer-Endpunkt.** Sie senden die Anfrage an die falsche [Instanz]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). Wenn sich Ihr Konto beispielsweise auf unserer EU-Instanz (`https://dashboard-01.braze.eu`) befindet, sollte die Anfrage an `https://rest.fra-01.braze.eu` gesendet werden.<br>- **Unzureichende Berechtigungen.** Jeder API-Schlüssel ist auf einen bestimmten Workspace und bestimmte Berechtigungen beschränkt. Überprüfen Sie die Berechtigungen des Schlüssels unter **Einstellungen** > **API-Schlüssel** im Dashboard.<br>- **Falscher API-Schlüssel.** API-Schlüssel sind Workspace-spezifisch. Ein Schlüssel aus einem Workspace kann nicht zur Authentifizierung von Anfragen für einen anderen Workspace verwendet werden. |
| `403 Forbidden` | Der Tarifplan unterstützt dies nicht, oder das Konto ist anderweitig deaktiviert.|
| `403 Access Denied` | Der von Ihnen verwendete Representational State Transfer-API-Schlüssel verfügt nicht über ausreichende Berechtigungen. Häufige Ursachen sind: {::nomarkdown}<ul><li><strong>API-Schlüssel wurde vor dem Feature erstellt.</strong> Wenn der API-Schlüssel vor dem Start eines Features erstellt wurde (z. B. Abo-Gruppen oder Kataloge), erbt der Schlüssel nicht automatisch diese Berechtigungen. Erstellen Sie einen neuen API-Schlüssel mit den erforderlichen Berechtigungen unter <strong>Einstellungen</strong> &gt; <strong>API-Schlüssel</strong>.</li><li><strong>Fehlende endpunktspezifische Berechtigung.</strong> Jeder API-Endpunkt erfordert einen bestimmten Berechtigungsumfang (z. B. <code>users.track</code> oder <code>email.status</code>). Überprüfen Sie, ob die Berechtigungen des Schlüssels mit dem aufgerufenen Endpunkt übereinstimmen.</li><li><strong>Abschließender Schrägstrich oder Tippfehler in der URL.</strong> Zum Beispiel kann <code>/users/track/</code> (mit abschließendem Schrägstrich) anstelle von <code>/users/track</code> unerwartete Fehler verursachen.</li></ul>{:/}|
| `404 Not Found` | Ungültige URL. |
| `415 Unsupported Media Type` | Der `Content-Type`-Anfrage-Header fehlt oder ist falsch. Fügen Sie auf der **Einstellungen**-Seite `Content-Type` mit dem Wert `application/json` hinzu. |
| `429 Rate Limited` | Rate-Limit überschritten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schwerwiegende Fehler" }

### Fehler beim Parsen des Anfragekörpers {#error-while-parsing-request-body}

Braze gibt HTTP 400 zurück, wenn der Anfragekörper kein gültiges JSON ist. Dies gilt für Representational State Transfer-Endpunkte, die einen JSON-Body akzeptieren, wie POST, PUT und PATCH.

Das Feld `error` enthält eine Nachricht, dass Sie gültiges `application/json` im Anfragekörper übergeben müssen. Möglicherweise sehen Sie auch `Error while parsing request body. Please check your syntax.`

Häufige Ursachen sind abschließende Kommas, Kommentare innerhalb von JSON, Strings in einfachen Anführungszeichen, eine zusätzliche öffnende `{` vor dem Payload oder das Senden eines verketteten Strings anstelle eines JSON-kodierten Objekts.

Bevor Sie es erneut versuchen:

1. Validieren Sie den Payload mit einem JSON-Linter.
2. Setzen Sie `Content-Type: application/json` und senden Sie UTF-8-kodiertes JSON.
3. Stellen Sie sicher, dass Ihr HTTP-Client das Objekt JSON-kodiert, anstatt rohe Strings zu verketten.

Informationen zu Payload-Größe und Objektlimits pro Anfrage für `/users/track` finden Sie unter [Warum erhalte ich `400 Bad Request` mit einem Syntaxfehler oder Parse-Fehler?]({{site.baseurl}}/api/endpoints/user_data/post_user_track#why-do-i-get-400-bad-request-with-a-bad-syntax-or-parse-error).