---
nav_title: Connected-Content-Aufruf durchführen
article_title: Connected-Content-API-Aufruf durchführen
page_order: 0
description: "Dieser Referenzartikel behandelt, wie Sie einen Connected-Content-API-Aufruf durchführen, einschließlich hilfreicher Beispiele und fortgeschrittener Connected-Content-Anwendungsfälle."
search_rank: 2
toc_headers: h2
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Connected-Content-API-Aufruf durchführen {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

> Verwenden Sie Connected-Content, um beliebige über eine API zugängliche Informationen direkt in Nachrichten einzufügen, die Sie an Nutzer:innen senden. Sie können Inhalte entweder direkt von Ihrem Webserver oder von öffentlich zugänglichen APIs abrufen.<br><br>Diese Seite behandelt, wie Sie Connected-Content-API-Aufrufe durchführen, fortgeschrittene Connected-Content-Anwendungsfälle, Fehlerbehandlung und mehr.

## Connected-Content-Aufrufvolumen verstehen {#understanding-connected-content-call-volume}

{% alert important %}
Ein Versand entspricht nicht einem Connected-Content-Aufruf. Braze garantiert kein 1:1-Verhältnis zwischen Nachrichtenversand und Connected-Content-Anfragen. Das System ist darauf ausgelegt, korrektes Nachrichten-Rendering und korrekte Zustellung gegenüber der Minimierung der Anzahl von Aufrufen zu bevorzugen. Ihre Endpunkte müssen so konzipiert sein, dass sie mehr Anfragen verarbeiten können als die Anzahl der Empfänger:innen oder gesendeten Nachrichten.
{% endalert %}

Braze kann denselben Connected-Content-API-Aufruf pro Empfänger:in mehr als einmal durchführen. Häufige Gründe sind:

- **E-Mail mit mehreren Teilen:** Eine einzelne E-Mail kann separate Rendering-Durchläufe für den HTML-Body, den Nur-Text-Body und die Accelerated Mobile Pages (AMP)-Version (falls vorhanden) auslösen. Jeder Durchlauf kann Connected-Content in diesem Teil auslösen, sodass eine Empfängerin oder ein Empfänger mehrere identische oder ähnliche Aufrufe erzeugen kann.
- **Validierung und Wiederholungsversuche:** Nachrichten-Payloads können pro Empfänger:in mehrmals für Validierung, Wiederholungslogik oder andere interne Zwecke gerendert werden.
- **Kanalverhalten:** Connected-Content wird ausgeführt, wenn die Nachricht gerendert wird. Bei In-App-Nachrichten wird die Nachricht zum Zeitpunkt der Impression gerendert.

Wenn Sie in Ihren Logs mehr Connected-Content-Aufrufe als Versendungen oder Empfänger:innen sehen, ist dieses Verhalten erwartungsgemäß. Hinweise zur Reduzierung der Last und zur Skalierungsplanung finden Sie unter [Best Practices für Endpunkte mit hohem Volumen](#best-practices-for-high-volume-endpoints).

## Einen Connected-Content-Aufruf senden {#send-a-connected-content-call}

Um einen Connected-Content-Aufruf zu senden, verwenden Sie den {% raw %}`{% connected_content %}`{% endraw %}-Tag. Mit diesem Tag können Sie Variablen mithilfe von `:save` zuweisen oder deklarieren. Aspekte dieser Variablen können später in der Nachricht mit [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) referenziert werden.

### Den API-Aufruf aufschlüsseln {#break-down-the-api-call}

Das folgende Beispiel verwendet die Sunrise-Sunset-API und fügt die heutige Sonnenaufgangszeit in eine Nachricht ein:

{% raw %}
```
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :save result %}
Hi there, today's sunrise in NYC is at {{result.sunrise}}.
```
{% endraw %}

Hier ist die Funktion jedes Teils:

| Komponente | Funktion |
| --- | --- |
| `connected_content`-Tag | Weist Braze an, beim Rendern der Nachricht eine HTTP-Anfrage zu stellen. |
| `https://api.sunrise-sunset.org/v2` | Der API-Endpunkt, den Braze aufruft. |
| `lat=40.7128&lng=-74.0060` | Abfrageparameter für die Koordinaten von New York City. |
| `date=today` | Fordert Daten für den aktuellen Tag an diesen Koordinaten an. |
| `:save result` | Speichert die API-Antwort in einer lokalen Variable namens `result`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Den API-Aufruf aufschlüsseln" }

### Wie die Sunrise-Sunset-API-Antwort funktioniert {#how-the-sunrise-sunset-api-response-works}

Dieser Endpunkt gibt JSON mit Feldern auf oberster Ebene wie `sunrise`, `sunset` und `tzid` zurück. Zeiten werden standardmäßig in der Zeitzone des Standorts zurückgegeben (in diesem Beispiel New Yorker Zeit).

Die Antwortstruktur sieht beispielsweise so aus:

```json
{
  "date": "2026-07-23",
  "tzid": "America/New_York",
  "sunrise": "2026-07-23T05:42:11-04:00",
  "sunset": "2026-07-23T20:21:32-04:00"
}
```

### Die API-Antwort auf Liquid abbilden {#map-the-api-response-to-liquid}

Da die Antwort als `result` gespeichert wird, können Sie jedes Feld direkt von diesem Objekt referenzieren.

{% raw %}
```liquid
{{result.sunrise}}
{{result.sunset}}
{{result.tzid}}
```
{% endraw %}

Verwenden Sie dieses Muster immer, wenn Sie JSON aus Connected Content speichern:

1. Speichern Sie die API-Antwort mit `:save`.
2. Finden Sie das gewünschte Feld in der JSON-Antwort.
3. Referenzieren Sie es in Liquid als `saved_variable.field_name`.

### Variablen hinzufügen {#add-variables}

Sie können auch Nutzerprofilattribute als Variablen in den URL-String einfügen, wenn Sie Connected-Content-Anfragen stellen.

Beispielsweise könnten Sie einen Webdienst haben, der Inhalte basierend auf der E-Mail-Adresse und ID einer Nutzerin oder eines Nutzers zurückgibt. Wenn Sie Attribute übergeben, die Sonderzeichen enthalten, wie das At-Zeichen (@), stellen Sie sicher, dass Sie den Liquid-Filter `url_param_escape` verwenden, um alle in URLs nicht zulässigen Zeichen durch ihre URL-freundlichen, escapten Versionen zu ersetzen, wie im folgenden E-Mail-Adressattribut gezeigt.

{% raw %}
```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Attributwerte müssen von `${}` umgeben sein, damit sie in unserer Version der Liquid-Syntax korrekt funktionieren.
{% endalert %}

Connected-Content-Anfragen unterstützen ausschließlich GET- und POST-Anfragen.

## Fehlerbehandlung {#error-handling}

Wenn die URL nicht erreichbar ist und eine 404-Seite zurückgibt, rendert Braze an deren Stelle einen leeren String. Wenn die URL eine HTTP-500- oder 502-Seite zurückgibt, schlägt die URL bei der Wiederholungslogik fehl.

Wenn der Endpunkt JSON zurückgibt, können Sie dies erkennen, indem Sie prüfen, ob der `connected`-Wert null ist, und dann [die Nachricht bedingt abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content). Braze erlaubt nur URLs, die über Port 80 (HTTP) und 443 (HTTPS) kommunizieren.

### Erkennung ungesunder Hosts {#unhealthy-host-detection}

Connected-Content verwendet einen Erkennungsmechanismus für ungesunde Hosts, der erkennt, wenn der Zielhost eine hohe Rate an erheblicher Verlangsamung oder Überlastung aufweist, was zu Timeouts, zu vielen Anfragen oder anderen Ergebnissen führt, die Braze daran hindern, erfolgreich mit dem Zielendpunkt zu kommunizieren. Er dient als Schutzmaßnahme, um unnötige Last zu reduzieren, die den Zielhost möglicherweise beeinträchtigt. Außerdem dient er der Stabilisierung der Braze-Infrastruktur und der Aufrechterhaltung schneller Messaging-Geschwindigkeiten.

Wenn der Zielhost eine hohe Rate an erheblicher Verlangsamung oder Überlastung aufweist, stoppt Braze vorübergehend Anfragen an den Zielhost für eine Minute und simuliert stattdessen Antworten, die den Fehler anzeigen. Nach einer Minute prüft Braze den Zustand des Hosts mit einer kleinen Anzahl von Anfragen, bevor die Anfragen mit voller Geschwindigkeit wieder aufgenommen werden, wenn der Host als gesund eingestuft wird. Wenn der Host weiterhin ungesund ist, wartet Braze eine weitere Minute, bevor ein erneuter Versuch unternommen wird.

Wenn Anfragen an den Zielhost durch den Detektor für ungesunde Hosts gestoppt werden, rendert Braze weiterhin Nachrichten und folgt Ihrer Liquid-Logik, als hätte es einen Fehlerantwortcode erhalten. Wenn Sie sicherstellen möchten, dass diese Connected-Content-Anfragen erneut versucht werden, wenn sie durch den Detektor für ungesunde Hosts gestoppt werden, verwenden Sie die Option `:retry`. Weitere Informationen zur Option `:retry` finden Sie unter [Connected-Content-Wiederholungen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

Wenn Sie vermuten, dass die Erkennung ungesunder Hosts Probleme verursacht, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/support_contact).

{% alert note %}
Sie können bestimmte URLs auf eine Zulassungsliste setzen, die für Connected-Content verwendet werden sollen. Um auf dieses Feature zuzugreifen, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

{% alert tip %}
Weitere Informationen zu häufigen Fehlercodes finden Sie unter [Fehlerbehebung bei Webhook- und Connected-Content-Anfragen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection).
{% endalert %}

### Rate-Limits (429) im Vergleich zur Erkennung ungesunder Hosts {#rate-limits-429-versus-unhealthy-host-detection}

Die folgenden Mechanismen sind unterschiedlich:

- **429 Too Many Requests:** Ihr Endpunkt (oder ein vorgelagerter Dienst) gibt diese Antwort zurück. Das bedeutet, dass Ihr Server oder Ihre Middleware den Datenverkehr ablehnt, häufig weil ein eigenes Rate-Limit besteht. Braze wendet kein separates Rate-Limit auf Connected-Content an; das Anfragevolumen von Connected-Content skaliert direkt mit Ihrem [Rate-Limit für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting). Da Nachrichten pro Empfänger:in mehrfach gerendert werden können (zum Beispiel für E-Mail-HTML, Klartext und AMP), kann die Anzahl der Connected-Content-Anfragen dieses Rate-Limit überschreiten – gehen Sie nicht davon aus, dass sie kleiner oder gleich der von Ihnen festgelegten Nachrichten pro Minute ist. Wenn Sie 429-Fehler sehen, skalieren Sie Ihren Endpunkt oder Ihre Middleware, um das erwartete Anfragevolumen zu bewältigen, oder senken Sie das [Rate-Limit für die Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) der Campaign oder des Canvas, damit weniger Nachrichten (und somit weniger Connected-Content-Aufrufe) pro Minute gesendet werden.
- **Erkennung ungesunder Hosts:** Eine Braze-seitige Schutzmaßnahme, die nach einer hohen Rate und einem hohen Volumen an *Fehlern* innerhalb eines Einminutenfensters ausgelöst wird. Die Fehleranzahl umfasst die Statuscodes `408`, `429`, `502`, `503`, `504` und `529`. Wenn sie ausgelöst wird, stoppt Braze vorübergehend Anfragen an diesen Host und simuliert eine Fehlerantwort. Dies ist unabhängig von Ihrem eigenen Rate-Limiting. Für Erkennungsschwellenwerte und weitere Details siehe [Fehlerbehebung bei Webhook- und Connected-Content-Anfragen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection). Um das Auslösen der Erkennung ungesunder Hosts zu vermeiden, stellen Sie sicher, dass Ihr Endpunkt das unter [Verständnis des Connected-Content-Aufrufvolumens](#understanding-connected-content-call-volume) und [Best Practices für Endpunkte mit hohem Volumen](#best-practices-for-high-volume-endpoints) beschriebene Aufrufvolumen bewältigen kann.

## Effiziente Performance ermöglichen {#allowing-for-efficient-performance}

Da Braze Nachrichten mit sehr hoher Geschwindigkeit zustellt, stellen Sie sicher, dass Ihr Server Tausende gleichzeitiger Verbindungen verarbeiten kann, damit er beim Abrufen von Inhalten nicht überlastet wird. Wenn Sie öffentliche APIs verwenden, bestätigen Sie, dass Ihre Nutzung keine Rate-Limits verletzt, die der API-Anbieter möglicherweise einsetzt. Braze erfordert aus Performance-Gründen, dass die Serverantwortzeit weniger als zwei Sekunden beträgt; wenn der Server länger als zwei Sekunden für die Antwort benötigt, wird der Inhalt nicht eingefügt.

Weitere Informationen zur Planung der Endpunktkapazität und zur Reduzierung des Aufrufvolumens finden Sie unter [Best Practices für Endpunkte mit hohem Volumen](#best-practices-for-high-volume-endpoints).

## Wissenswertes {#things-to-know}

- Braze berechnet keine Gebühren für API-Aufrufe und diese werden nicht auf Ihre Datenpunkt-Nutzung angerechnet.
- Für Connected-Content-Antworten gilt ein Limit von 1 MB.
- Connected Content wird ausgeführt, wenn die Nachricht gerendert wird. Bei In-App-Nachrichten wird die Nachricht zum Zeitpunkt der Impression gerendert.
- Connected-Content-Aufrufe folgen keinen Weiterleitungen.

### Wie Connected-Content-Aufrufe verarbeitet werden {#how-connected-content-calls-are-processed}

Connected-Content-Aufrufe innerhalb eines einzelnen Nachrichten-Templates werden während des Liquid-Renderings sequenziell (von oben nach unten) ausgeführt. Das bedeutet, dass nachfolgende Aufrufe auf Variablen verweisen können, die von vorherigen Aufrufen gesetzt wurden. In diesem Beispiel ruft der erste Aufruf Nutzerdaten ab, und der zweite Aufruf verwendet diese Daten, um Präferenzen abzurufen:

{% raw %}
```liquid
{% connected_content https://api.example.com/user :save user_data %}
{% connected_content https://api.example.com/preferences?user_id={{user_data.id}} :save preferences %}
```
{% endraw %}

### Globaler Versand und Anfragevolumen {#global-sending-and-request-volume}

Während Connected-Content-Aufrufe innerhalb einer einzelnen Nachricht sequenziell ausgeführt werden, werden Nachrichten über Ihre Campaigns und Canvases hinweg parallel gesendet. Versendungen mit hohem Volumen können während Spitzenzeiten erheblichen Anfrage-Traffic an Ihre Endpunkte erzeugen. Informationen zum Verwalten und Drosseln dieses Traffics – einschließlich Workspace-Messaging-Rate-Limits, Rate-Limiting der Zustellgeschwindigkeit und Caching – finden Sie unter [Best Practices für Endpunkte mit hohem Volumen](#best-practices-for-high-volume-endpoints).

## Best Practices für Endpunkte mit hohem Volumen {#best-practices-for-high-volume-endpoints}

Wenn Ihre Nachrichten Connected-Content verwenden und Sie in hohem Volumen versenden, planen Sie mehr Anfragen ein als die Anzahl der Empfänger:innen oder Sendungen:

- **Spitzenlast abschätzen:** Verwenden Sie einen konservativen Multiplikator, wenn Sie Ihren Endpunkt oder Ihre Middleware dimensionieren – Connected-Content-Anfragen können die Anzahl der Empfänger:innen oder gesendeten Nachrichten übersteigen. Bei E-Mails kann beispielsweise eine einzelne Empfängerin oder ein einzelner Empfänger mehrere Aufrufe erzeugen (HTML, Klartext und AMP), sodass Empfänger:innen × 2 oder × 3 häufig als konservative Schätzung verwendet wird.
- **Caching nutzen, wo es sinnvoll ist:** GET-Anfragen werden standardmäßig gecacht. Fügen Sie bei POST-Anfragen `:cache_max_age` hinzu, wenn die Antwort für einen bestimmten Zeitraum wiederverwendet werden kann (zum Beispiel Token oder Inhalte, die sich nicht pro Anfrage ändern). Siehe [Antworten cachen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) und die [FAQ zum POST-Caching](#what-is-caching-behavior) im folgenden Abschnitt.
- **Rate-Limits für Nachrichten festlegen:** [Workspace-Messaging-Rate-Limits]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) und [Zustellgeschwindigkeits-Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) für Campaigns oder Canvases begrenzen indirekt das Anfragevolumen von Connected-Content – Braze selbst wendet kein Rate-Limiting auf Connected-Content an. Diese Einstellungen sind Näherungswerte, keine exakten Steuerungen, da Connected-Content-Anfragen nicht im Verhältnis 1:1 zu Nachrichten stehen. Nutzen Sie sie, um das Nachrichten- (und damit Connected-Content-)Volumen innerhalb der Kapazität Ihres Endpunkts zu halten.
- **Idempotenz und Wiederholungsversuche einplanen:** Braze kann Ihren Endpunkt pro Empfänger:in mehr als einmal aufrufen. Stellen Sie sicher, dass Ihr Endpunkt doppelte Anfragen ohne unerwünschte Nebeneffekte verarbeiten kann.

## Authentifizierungstypen {#authentication-types}

### Einfache Authentifizierung verwenden {#using-basic-authentication}

Wenn die URL eine einfache Authentifizierung erfordert, kann Braze Zugangsdaten für die einfache Authentifizierung speichern, die Sie in Ihrem API-Aufruf verwenden können. Sie können bestehende Zugangsdaten für die einfache Authentifizierung verwalten und neue hinzufügen unter **Einstellungen** > **Connected-Content**.

![Die Connected-Content-Einstellungen im Braze-Dashboard.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Um neue Zugangsdaten hinzuzufügen, wählen Sie **Zugangsdaten hinzufügen** > **Einfache Authentifizierung**.

![Dropdown „Zugangsdaten hinzufügen“ mit der Option, einfache Authentifizierung oder Token-Authentifizierung zu verwenden.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Geben Sie Ihren Zugangsdaten einen Namen und tragen Sie den Benutzernamen und das Passwort ein.

![Das Fenster „Neue Zugangsdaten erstellen“ mit der Option, einen Namen, Benutzernamen und ein Passwort einzugeben.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

Sie können diese Zugangsdaten für die einfache Authentifizierung dann in Ihren API-Aufrufen verwenden, indem Sie den Namen des Tokens referenzieren:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Wenn Sie Zugangsdaten löschen, beachten Sie, dass alle Connected-Content-Aufrufe, die versuchen, diese zu verwenden, abgebrochen werden.
{% endalert %}

Gespeicherte Zugangsdaten gelten für {% raw %}`{% connected_content %}`{% endraw %}-Anfragen, während Braze eine Nachricht rendert. Sie werden nicht auf die primäre HTTP-Anfrage angewendet, die in einem [Webhook]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#authentication-and-connected-content-credentials)-Schritt konfiguriert ist. Verwenden Sie Anfrage-Header oder ein {% raw %}`{% connected_content %}`{% endraw %}-Tag innerhalb eines Webhook-Header- oder Body-Felds, wenn Sie Secrets für diesen Aufruf abrufen müssen.

### Token-Authentifizierung verwenden {#using-token-authentication}

Bei der Verwendung von Braze Connected-Content stellen Sie möglicherweise fest, dass bestimmte APIs anstelle eines Benutzernamens und Passworts ein Token erfordern. Braze kann auch Zugangsdaten speichern, die Token-Authentifizierungs-Header-Werte enthalten.

Um Zugangsdaten hinzuzufügen, die Token-Werte enthalten, wählen Sie **Zugangsdaten hinzufügen** > **Token-Authentifizierung**. Fügen Sie dann die Schlüssel-Wert-Paare für Ihre API-Aufruf-Header und die zulässige Domain hinzu.

![Ein Beispiel-Token „token_credential_abc“ mit Token-Authentifizierungsdetails.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

Sie können diese Zugangsdaten dann in Ihren API-Aufrufen verwenden, indem Sie den Namen der Zugangsdaten referenzieren:

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Open Authentication (OAuth) verwenden {#use-open-authentication-oauth}

Einige API-Konfigurationen erfordern das Abrufen eines Zugriffstokens, das dann zur Authentifizierung des API-Endpunkts verwendet werden kann, auf den Sie zugreifen möchten.

#### Schritt 1: Zugriffstoken abrufen {#step-1-retrieve-the-access-token}

Das folgende Beispiel veranschaulicht das Abrufen und Speichern eines Zugriffstokens in einer lokalen Variablen, die dann zur Authentifizierung des nachfolgenden API-Aufrufs verwendet werden kann. Ein `:cache_max_age`-Parameter kann hinzugefügt werden, um die Gültigkeitsdauer des Zugriffstokens abzugleichen und die Anzahl der ausgehenden Connected-Content-Aufrufe zu reduzieren. Weitere Informationen finden Sie unter [Konfigurierbares Caching]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

{% alert note %}
Wenn der Token-Endpunkt `application/x-www-form-urlencoded` erwartet und Sie Zugangsdaten in `:body` übergeben, URL-kodieren Sie alle Sonderzeichen in Parameterwerten. Zum Beispiel werden Schrägstriche (`/`) zu `%2F` und Pluszeichen (`+`) zu `%2B`. Nicht kodierte Sonderzeichen können dazu führen, dass OAuth-Token-Anfragen fehlschlagen.
{% endalert %}

#### Schritt 2: API mit dem abgerufenen Zugriffstoken autorisieren {#step-2-authorize-the-api-using-the-retrieved-access-token}

Nachdem das Token gespeichert wurde, kann es dynamisch in den nachfolgenden Connected-Content-Aufruf eingebunden werden, um die Anfrage zu autorisieren:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### Zugangsdaten bearbeiten {#editing-credentials}

Sie können den Namen der Zugangsdaten für Authentifizierungstypen bearbeiten.

- Bei der einfachen Authentifizierung können Sie den Benutzernamen und das Passwort aktualisieren. Beachten Sie, dass das zuvor eingegebene Passwort nicht sichtbar sein wird.
- Bei der Token-Authentifizierung können Sie die Header-Schlüssel-Wert-Paare und die zulässige Domain aktualisieren. Beachten Sie, dass die zuvor festgelegten Header-Werte nicht sichtbar sein werden.

## Connected-Content-IP-Zulassungsliste {#connected-content-ip-allowlisting}

Wenn eine Nachricht mit Connected Content von Braze gesendet wird, stellen die Braze-Server automatisch Netzwerkanfragen an die Server unserer Kund:innen oder Drittanbieter, um Daten abzurufen. Mit der IP-Zulassungsliste können Sie überprüfen, ob Connected-Content-Anfragen tatsächlich von Braze stammen, und so eine zusätzliche Sicherheitsebene hinzufügen.

Braze sendet Connected-Content-Anfragen aus den folgenden IP-Bereichen. Die aufgeführten Bereiche werden automatisch und dynamisch zu allen API-Schlüsseln hinzugefügt, für die die Zulassungsliste aktiviert wurde.

Braze verfügt über einen reservierten Satz von IPs, die für alle Dienste verwendet werden – nicht alle davon sind zu einem bestimmten Zeitpunkt aktiv. Dies ist so konzipiert, dass Braze bei Bedarf von einem anderen Rechenzentrum aus senden oder Wartungsarbeiten durchführen kann, ohne Kund:innen zu beeinträchtigen. Braze kann eine, eine Teilmenge oder alle der folgenden aufgeführten IPs verwenden, wenn Connected-Content-Anfragen gestellt werden.

Wenn Connected-Content-Anfragen durchgehend `403 Forbidden` zurückgeben und die Authentifizierung korrekt konfiguriert ist, nehmen Sie diese IPs auf dem Server, der die Anfrage empfängt, in die Zulassungsliste auf. Ein `403`-Fehler kann auch auf unzureichende Berechtigungen oder ungültige Zugangsdaten hinweisen – überprüfen Sie daher sowohl die Netzwerk- als auch die Authentifizierungseinstellungen. Webhook-spezifische Hinweise finden Sie unter [403 Forbidden und IP-Zulassungsliste]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#403-forbidden-and-ip-allowlisting).

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### `User-Agent`-Header {#user-agent-header}

Braze fügt allen Connected-Content- und Webhook-Anfragen einen `User-Agent`-Header hinzu, der in etwa wie folgt aussieht:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Beachten Sie, dass sich der Hash-Wert regelmäßig ändert. Wenn Sie den Datenverkehr nach `User-Agent` filtern, lassen Sie alle Werte zu, die mit `Braze Sender` beginnen.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

Wenn Ihr Connected-Content-Aufruf nicht korrekt oder gar nicht gerendert wird, überprüfen Sie die folgenden Details:

- **Bestätigen Sie, dass ein Connected-Content-Aufruf durchgeführt wurde:** Sie können im [Tab „Messaging-Verlauf“]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab) überprüfen, ob ein Aufruf durchgeführt wurde. Sie können auch einen einzelnen Connected-Content-Request als Test senden.
- **Überprüfen Sie über Postman oder einen CURL-Request, ob der gewünschte Request erfolgreich ist:** Wenn der Request funktioniert und eine Antwort zurückgibt, vergleichen Sie den Request im Detail (einschließlich Header). Bestätigen Sie, dass die Header in Schlüssel-Wert-Paaren mit doppelten Anführungszeichen erfasst werden.
- **Stellen Sie sicher, dass die Autorisierung korrekt gehandhabt wird:** Bestätigen Sie, dass die Option `:basic_auth`/`:auth_credentials` verwendet wird und die Connected-Content-Autorisierung zu den Connected-Content-Workspace-Einstellungen hinzugefügt wurde. Manchmal erfordert die Connected-Content-URL Header über die Authentifizierung hinaus, die eingegeben werden müssen.
- **Überprüfen Sie, ob die Daten im erwarteten Format vorliegen:** Für den Antwort-Body parst Braze gültiges JSON in ein Liquid-Objekt; andernfalls wird die Antwort als Klartext behandelt (einschließlich HTML). Die Option `:content_type` setzt die ausgehenden `Content-Type`- und `Accept`-Header für Ihren Request und beeinflusst nicht das Parsen der Antwort. Wenn Ihr JSON für den Request-`:body` Leerzeichen enthält, folgen Sie der Anleitung im Abschnitt [JSON-Body bereitstellen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables#providing-json-body).
- **Bestätigen Sie, dass die Daten korrekt geparst wurden:** Überprüfen Sie, ob das Liquid korrekt auf das erwartete Feld verweist. Verwenden Sie für verschachteltes JSON {% raw %}`{{sampleresult.data[0].sample_field}}`{% endraw %}, um auf das gewünschte verschachtelte Feld zu verweisen. Sie können die verschachtelten JSON-Eigenschaften überprüfen, indem Sie das erwartete Ergebnis mit {% raw %}`RESPONSE:{{sampleresult.data}}`{% endraw %} ausgeben.
- **Überprüfen Sie den Antwort-Statuscode:** Der Antwort-Statuscode muss ein `2XX`-Code sein. Connected Content bietet keine Möglichkeit, die Antwort zu verarbeiten, wenn der Code nicht `2XX` ist.

Sie können auch [Webhook.site](https://webhook.site/) verwenden, um Ihre Connected-Content-Aufrufe zu debuggen und Probleme mit den Request-Headern, dem Request-Body und anderen Informationen zu diagnostizieren, die im Aufruf gesendet werden.

1. Ersetzen Sie die URL in Ihrem Connected-Content-Aufruf durch die eindeutige URL, die auf der Website generiert wurde.
2. Zeigen Sie eine Vorschau Ihrer Campaign oder Ihres Canvas-Schritts an und testen Sie sie, um die Requests auf dieser Website einzusehen.

Sie können auch überprüfen, ob der Liquid-Tag die Parameter enthält, die Ihr Endpunkt erwartet (zum Beispiel `:method`, `:headers`, `:content_type`, `:body` und `:basic_auth`, wenn erforderlich). Wenn Sie sich auf den HTTP-Statuscode-Schlüssel in einem gespeicherten JSON-Objekt verlassen, muss der Endpunkt ein JSON-Objekt und einen `2XX`-Status zurückgeben.

Bei hohen Fehlerraten von Ihrem Host lesen Sie [Erkennung fehlerhafter Hosts]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) und [Aufrufvolumen von Connected Content](#understanding-connected-content-call-volume).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum gibt es mehr Connected-Content-Aufrufe als Nutzer:innen oder Sendungen? {#why-are-there-more-connected-content-calls-than-users-or-sends}

Braze kann denselben Connected-Content-API-Aufruf pro Empfänger:in mehr als einmal durchführen, um einen Nachrichten-Payload zu rendern. Nachrichten-Payloads können pro Empfänger:in mehrfach gerendert werden – für Validierung, Wiederholungslogik oder andere interne Zwecke. Beachten Sie jedoch, dass nur einer der Connected-Content-Aufrufe eine Nachricht befüllt.

Es ist zu erwarten, dass ein Connected-Content-API-Aufruf pro Empfänger:in mehr als einmal durchgeführt werden kann, selbst wenn die Wiederholungslogik im Aufruf nicht verwendet wird. Wir empfehlen, das Rate-Limit für alle Nachrichten mit Connected Content festzulegen oder Ihre Server so zu konfigurieren, dass sie das erwartete Volumen besser bewältigen können, das mehrere Connected-Content-Aufrufe pro Nachrichtenversand berücksichtigt.

Weitere Informationen und Maßnahmen finden Sie unter [Aufrufvolumen von Connected Content verstehen](#understanding-connected-content-call-volume) und [Best Practices für Endpunkte mit hohem Volumen](#best-practices-for-high-volume-endpoints).

### Wie funktioniert Rate-Limiting mit Connected Content? {#how-does-rate-limiting-work-with-connected-content}

Connected Content hat kein eigenes Rate-Limit. Stattdessen basiert das Rate-Limit auf der Nachrichtenversandrate. Wir empfehlen, das Messaging-Rate-Limit höher als Ihr beabsichtigtes Connected-Content-Rate-Limit festzulegen, wenn es mehr Connected-Content-Aufrufe als gesendete Nachrichten gibt.

### Wie verhält sich das Caching? {#what-is-caching-behavior}

GET-Anfragen werden standardmäßig gecacht (siehe [Antworten cachen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)). **POST-Anfragen werden standardmäßig nicht gecacht**, aber Sie können das Caching aktivieren, indem Sie `:cache_max_age` zum Connected-Content-Aufruf hinzufügen. Dies kann die Endpunkt-Last reduzieren, wenn derselbe POST (zum Beispiel eine Token- oder Content-Anfrage) innerhalb des Cache-Fensters wiederholt durchgeführt würde.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

Caching kann dazu beitragen, doppelte Connected-Content-Aufrufe zu reduzieren, garantiert aber nicht, dass nur ein einziger Aufruf pro Nutzer:in erfolgt. Die Cache-Dauer liegt zwischen fünf Minuten und vier Stunden. Alle Details finden Sie unter [Antworten cachen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses).

### Wie ist das HTTP-Standardverhalten von Connected Content? {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### Was passiert, wenn ich denselben Connected-Content-Aufruf an mehreren Stellen verwende? {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

Jeder Connected-Content-Tag wird separat ausgewertet, auch wenn mehrere Tags dieselbe URL und dieselben Parameter verwenden. Wenn URL und Cache-Einstellungen es zulassen, können identische Anfragen aus dem Cache bedient werden, anstatt eine neue ausgehende Anfrage auszulösen (siehe [Antworten cachen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses) für Details).