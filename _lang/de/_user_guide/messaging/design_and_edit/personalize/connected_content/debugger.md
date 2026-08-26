---
nav_title: Connected-Content-Debugger
article_title: Connected-Content-Debugger
page_order: 3.5
description: "Dieser Referenzartikel beschreibt, wie Sie den Connected-Content-Debugger verwenden, um Probleme vor dem Versand Ihrer Nachricht zu beheben."
---

# Connected-Content-Debugger {#connected-content-debugger}

> Verwenden Sie den Connected-Content-Debugger, um die Live-Anfrage und -Antwort für jeden Connected-Content-Aufruf anzuzeigen. So können Sie Ihren Endpunkt, Ihre Header und Ihre Liquid-Tags überprüfen, bevor Sie eine Campaign oder ein Canvas starten.

## Über den Debugger {#about-the-debugger}

Connected-Content ermöglicht es Ihnen, Nachrichten mit Echtzeitdaten anzureichern, indem zum Renderingzeitpunkt ein HTTP-Aufruf an eine externe API durchgeführt und die Antwort mithilfe von Liquid in Ihre Nachricht eingefügt wird. Da dieser Aufruf außerhalb von Braze stattfindet, kann es schwierig sein, genau zu sehen, welche Anfrage Braze gesendet hat, was der Endpunkt zurückgegeben hat oder warum ein Aufruf fehlgeschlagen ist – bevor eine Campaign oder ein Canvas live ist.

Der Connected-Content-Debugger hilft Ihnen, solche Probleme vor dem Start zu beheben. Er zeigt Ihnen die Live-Anfrage und -Antwort für jeden Connected-Content-Aufruf in Ihrer Nachricht im Bereich **Vorschau & Test** an. So können Sie bestätigen, dass Ihr Endpunkt, Ihre Header und Ihre Liquid-Tags korrekt konfiguriert sind – alles innerhalb des Braze-Dashboards.

### Unterstützte Bereiche {#supported-areas}

Der Connected-Content-Debugger ist für die folgenden Bereiche verfügbar:

- Canvas-Context-Schritte
- Content Cards
- E-Mail
    - Einschließlich Templates
    - Ausgenommen Fußzeilen und Abo-Seiten
- In-App-Nachrichten
- Push-Benachrichtigungen
- SMS/MMS/RCS
- Webhooks
    - Einschließlich Templates
- WhatsApp

{% alert note %}
Der Debugger ist für die meisten Kanäle verfügbar, jedoch noch nicht für KakaoTalk, LINE, Banner oder kanalunspezifische Kompositionsoberflächen (wie Content Blocks und Canvas-Nutzer:innen-Aktualisierungsschritte). Wenn Sie den Debugger nicht sehen, wird das Connected-Content-Debugging für dieses Feature möglicherweise noch nicht unterstützt.
{% endalert %}

## Debugger verwenden {#use-the-debugger}

Jedes Mal, wenn Sie eine Vorschau ausführen, rendert Braze automatisch die Ergebnisse des Connected-Content-Aufrufs im Tab **Vorschau**. So verwenden Sie den Debugger:

1. Konfigurieren Sie Ihre Nachricht mit dem {% raw %}`{% connected_content %}`{% endraw %}-Tag.
2. Gehen Sie zum Abschnitt **Vorschau & Test**. Wenn Ihre Nachricht ein Connected-Content-Tag enthält, sehen Sie eine Zusammenfassung mit der Anzahl der Connected-Content-Aufrufe sowie den Erfolgs- und Fehlerstatus.

![Connected-Content-Abschnitt im Test-Bereich.]({% image_buster /assets/img/connected_content/debugger1.png %})

{:start="3"}
3. Wählen Sie **Details anzeigen**, um den Debugger neben Ihrer Vorschau zu öffnen. Das Seitenpanel zeigt eine Tabelle mit der URL und dem Ergebnis für jeden Connected-Content-Aufruf an.

![Connected-Content-Aufrufe mit drei zu überprüfenden URLs.]({% image_buster /assets/img/connected_content/debugger3.png %})

{:start="4"}
4. Wählen Sie neben jeder URL und jedem Ergebnis **Anzeigen**, um die Anfrage- und Antwort-Header, den Payload, die Methode, die Dauer und die Caching-Informationen einzusehen.

![Connected-Content-Aufruf mit Anfrage- und Antwortdetails.]({% image_buster /assets/img/connected_content/debugger4.png %})

{:start="5"}
5. Überprüfen Sie die Ergebnisse und passen Sie Ihr Tag, die Header oder den Endpunkt nach Bedarf an. Generieren Sie anschließend eine neue Vorschau, um die Korrektur zu bestätigen.

Wenn Ihr Template mehr als ein {% raw %}`{% connected_content %}`{% endraw %}-Tag enthält, listet der Debugger jeden ausgeführten Aufruf auf. Bei Kanälen, die aus einem Template mehrere Nachrichtenkörper rendern (zum Beispiel E-Mail, die separate HTML-, Plaintext- und AMP-Körper rendert, oder Quick Push, das separate gerätespezifische Körper rendert), zeigt der Debugger jeden Connected-Content-Aufruf über alle Körper hinweg an – nicht nur den, den Sie gerade in der Vorschau betrachten.

## Die Debug-Ausgabe verstehen {#understand-the-debug-output}

Jeder Connected-Content-Aufruf wird mit eigenen Tabs **Response** und **Request** angezeigt. Der Tab **Response** wird standardmäßig angezeigt, da er in der Regel der erste Indikator ist, um zu bestätigen, ob ein Aufruf erfolgreich war.

### URL-Details {#url-details}

| Feld | Beschreibung |
| --- | --- |
| URL | Die vollständig gerenderte URL, die Braze aufgerufen hat, mit allen aufgelösten Liquid-Tags. |
| Method | Die verwendete HTTP-Methode (GET oder POST). |
| Status code | Der HTTP-Statuscode, den Ihr Endpunkt zurückgegeben hat (zum Beispiel `200`, `404`, `500`). Siehe [Fehlerbehebung bei Antwortcodes](#troubleshooting-response-codes) für Braze-spezifische Codes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL-Details" }

### Tab „Response“ {#response-tab}

| Feld | Beschreibung |
| --- | --- |
| Duration | Wie lange die Anfrage bis zum Abschluss gedauert hat, in Sekunden. Die Dauer wird nur für Live-Aufrufe (nicht aus dem Cache) angezeigt. |
| Served from cache | Gibt an, ob diese Antwort aus dem Connected-Content-Cache von Braze bereitgestellt wurde, anstatt eines Live-Aufrufs an Ihren Endpunkt (`Yes` oder `No`). Ein zwischengespeichertes Ergebnis spiegelt eine frühere Antwort wider, nicht unbedingt den aktuellen Zustand Ihres Endpunkts. |
| Response body | Der von Ihrem Endpunkt zurückgegebene Antwortkörper. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tab „Response“" }

### Tab „Request“ {#request-tab}

| Feld | Beschreibung |
| --- | --- |
| Headers | Header aus Ihrem Connected-Content-Tag (`:headers`, Zugangsdaten und Optionen wie `:content_type`). |
| Body | Der gesendete Anfragekörper, falls vorhanden (POST-Anfragen). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tab „Request“" }

## Welche Anfrage-Header im Debugger angezeigt werden {#which-request-headers-appear-in-the-debugger}

Der Tab **Request** listet Header aus Ihrem Connected-Content-Tag auf: angepasste `:headers`, gespeicherte Zugangsdaten und Header, die durch Tag-Optionen wie `:content_type` und `:basic_auth` festgelegt werden. Braze fügt der ausgehenden Anfrage an Ihren Endpunkt außerdem Standard-Header hinzu (zum Beispiel `User-Agent` und `Host`). Diese von Braze hinzugefügten Header werden im Debugger angezeigt, wenn Sie sie in `:headers` festlegen.

{% alert note %}
Um einen konsistenten `User-Agent` zu senden, legen Sie ihn in `:headers` fest. Braze verwendet Ihren Wert, und der Debugger zeigt diesen Header an.
{% endalert %}

{% multi_lang_include connected_content/outgoing_request_headers.md %}

## Schwärzung von Zugangsdaten {#credential-redaction}

Wenn Ihr Connected-Content-Tag `:basic_auth`, gängige Secret-Header, Schlüssel oder andere [Optionen zur Authentifizierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types) verwendet, schwärzt der Debugger diese Werte im Tab **Request** und ersetzt sie durch eine Reihe von Sternchen (*). So können Sie bestätigen, dass Zugangsdaten in der Anfrage enthalten waren, ohne die Werte in **Preview & Test** offenzulegen.

Authentifizierungsfehler sind auch bei geschwärzten Zugangsdaten sichtbar: Wenn Ihr Endpunkt einen `401`- oder `403`-Statuscode zurückgibt, wird dieser im Tab **Response** normal angezeigt, sodass Sie erkennen können, dass Ihre Anfrage aufgrund der Authentifizierung abgelehnt wurde, obwohl die Zugangsdaten selbst verborgen sind.

## Fehlerbehebung bei Antwortcodes {#troubleshooting-response-codes}

### Endpunktfehler versus von Braze auferlegte Limits {#endpoint-errors-versus-braze-imposed-limits}

Nicht jeder Statuscode außer `2XX` im Tab **Response** stammt von Ihrem Endpunkt. Braze erzwingt eigene Limits für Connected-Content-Aufrufe, und diese können Antworten erzeugen, die einem Endpunktfehler ähnlich sehen.

Wenn Sie [Antwortcodes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#start-here-match-your-symptom) wie `408`, `429`, `502`, `503`, `504` oder `599` sehen, liegt das Problem in der Regel auf der Braze-Seite des Aufrufs – bezogen auf die Host-Verfügbarkeit, Timeouts oder die Payload-Größe. Wenn Ihr Endpunkt regelmäßig große Antworten zurückgibt, sollten Sie die Antwort-Payload auf die Felder reduzieren, die Ihre Nachricht tatsächlich benötigt.

### Endpunkt hat einen unerwarteten Statuscode zurückgegeben {#endpoint-returned-an-unexpected-status-code}

Verwenden Sie den Tab **Request**, um die URL, die Header aus Ihrem Tag und den Body zu überprüfen. Eine häufige Ursache für unerwartete `4XX`-Antworten ist ein Liquid-Tag in der URL, den Headern oder dem Body, der sich nicht wie erwartet aufgelöst hat. Prüfen Sie, ob alle {% raw %}`{{ }}`{% endraw %}-Referenzen auf Felder verweisen, die für die Nutzer:in oder den Kontext existieren, mit dem Sie die Vorschau anzeigen.

### Antwort wirkt veraltet {#response-looks-stale}

Prüfen Sie **Served from cache** im Tab **Response**. Wenn dort `Yes` angezeigt wird, zeigt der Debugger eine zuvor zwischengespeicherte Antwort anstelle eines neuen Aufrufs. Fügen Sie Ihrem Tag vorübergehend `:no_cache` hinzu, oder warten Sie, bis der Cache abläuft (gemäß `:cache_max_age`), um das aktuelle Endpunktverhalten zu bestätigen.

## Verwandte Artikel {#related-articles}

- [Connected-Content-Referenz]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Einen Connected-Content-API-Aufruf durchführen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Ausgehende Anfrage-Header]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#outgoing-request-headers)
- [Fehlerbehebung bei Webhook- und Connected-Content-Anfragen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)