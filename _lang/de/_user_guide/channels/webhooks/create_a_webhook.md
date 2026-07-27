---
nav_title: Webhook erstellen
article_title: Webhook erstellen
page_order: 1
channel:
  - webhooks
description: "Dieser Referenzartikel beschreibt, wie Sie eine Webhook-Kampagne erstellen und konfigurieren."
search_rank: 2
---

# Eine Webhook-Kampagne erstellen {#create-a-webhook-campaign}

> Durch das Erstellen einer Webhook-Kampagne oder das Einbinden eines Webhooks in eine Multichannel-Kampagne können Sie Nicht-App-Aktionen auslösen, indem Sie anderen Systemen und Anwendungen Echtzeitinformationen bereitstellen.

Sie können Webhooks verwenden, um Informationen an Systeme wie Salesforce oder Marketo oder an Ihre Backend-Systeme zu senden. Beispielsweise möchten Sie möglicherweise die Konten Ihrer Kund:innen mit einer Aktion gutschreiben, nachdem sie ein angepasstes Event eine bestimmte Anzahl von Malen ausgeführt haben.

{% alert tip %}
Um mehr darüber zu erfahren, was Webhooks sind und wie Sie sie in Braze verwenden können, lesen Sie [Webhooks]({{site.baseurl}}/user_guide/channels/webhooks), bevor Sie fortfahren.
{% endalert %}

## Schritt 1: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten {#step-1-choose-where-to-build-your-message}

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Campaign oder ein Canvas gesendet werden soll? Campaigns eignen sich besser für einzelne, gezielte Messaging-Kampagnen, während Canvases besser für mehrstufige User-Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

**Schritte:**

1. Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Campaign erstellen**.
2. Wählen Sie **Webhook** oder, für Campaigns, die auf mehrere Kanäle abzielen, **Multichannel**.
3. Geben Sie Ihrer Campaign einen eindeutigen und aussagekräftigen Namen.
4. (Optional) Fügen Sie eine Beschreibung hinzu, um zu erläutern, wie diese Campaign verwendet wird.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) hinzu.
   * Tags erleichtern das Auffinden Ihrer Campaigns und das Erstellen von Berichten. Wenn Sie beispielsweise den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reports/report_builder) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu und benennen Sie sie, wie Sie für Ihre Campaign benötigen. Sie können für jede Ihrer hinzugefügten Varianten unterschiedliche Webhook-Templates auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Campaign ähnlich sein oder denselben Inhalt haben werden, verfassen Sie Ihre Nachricht, bevor Sie weitere Varianten hinzufügen. Sie können dann **Aus Variante kopieren** aus dem Dropdown **Variante hinzufügen** auswählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Schritte:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## Schritt 2: Webhook erstellen {#step-2-build-your-webhook}

Sie können einen Webhook von Grund auf neu erstellen, ein vorhandenes Template verwenden oder eines unserer bestehenden Templates nutzen. Erstellen Sie dann Ihren Webhook im Tab **Compose** des Editors.

Der Tab **Compose** besteht aus den folgenden Feldern:

- Sprache
- Webhook-URL
- HTTP-Methode
- Anfrage-Body

![Der Tab „Compose“ mit einem Beispiel-Webhook-Template.]({% image_buster /assets/img_archive/webhook_compose.png %})

### Sprache {#internationalization}

[Internationalisierung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) wird in der URL und im Anfrage-Body unterstützt. Um Ihre Nachricht zu internationalisieren, wählen Sie **Add languages** aus und füllen Sie die erforderlichen Felder aus.

Wir empfehlen, Ihre Sprachen auszuwählen, bevor Sie Ihren Inhalt verfassen, damit Sie Ihren Text an der richtigen Stelle im Liquid einfügen können. Eine vollständige Liste der verfügbaren Sprachen finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

Wenn Sie Text in einer Sprache hinzufügen, die von rechts nach links geschrieben wird, beachten Sie, dass das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten weitgehend davon abhängt, wie Dienstanbieter sie darstellen. Best Practices für die Erstellung von Rechts-nach-links-Nachrichten, die möglichst genau angezeigt werden, finden Sie unter [Rechts-nach-links-Nachrichten erstellen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Webhook-URL {#webhook-url}

Die Webhook-URL, oder HTTP-URL, gibt Ihren Endpunkt an. Der Endpunkt ist der Ort, an den Sie die Informationen senden, die Sie im Webhook erfassen.

Wenn Sie Informationen an einen Anbieter senden möchten, sollte der Anbieter diese URL in seiner API-Dokumentation bereitstellen. Wenn Sie Informationen an Ihre eigenen Systeme senden, wenden Sie sich an Ihr Entwicklerteam, um sicherzustellen, dass Sie die richtige URL verwenden.

Braze erlaubt nur URLs, die über die Standardports `80` (HTTP) und `443` (HTTPS) kommunizieren.

#### Liquid verwenden {#using-liquid}

Sie können Ihre Webhook-URLs mit [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) personalisieren. Manchmal erfordern bestimmte Endpunkte, dass Sie Nutzer:innen identifizieren oder nutzerspezifische Informationen als Teil Ihrer URL angeben. Wenn Sie Liquid verwenden, stellen Sie sicher, dass Sie für jede nutzerspezifische Information, die Sie in Ihrer URL verwenden, einen [Standardwert]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) angeben.

### HTTP-Methode {#http-method}

Die zu verwendende HTTP-Methode variiert je nach Endpunkt, an den Sie Informationen senden. In den meisten Fällen verwenden Sie POST.

| HTTP-Methode | Beschreibung |
| ----------- | ----------- |
| POST | Schreibt neue Informationen auf den empfangenden Server. Dies ist die am häufigsten verwendete Methode beim Senden von Daten. |
| GET | Ruft vorhandene Informationen ab, anstatt neue Informationen zu schreiben. Per Definition unterstützt eine GET-Anfrage keinen Anfrage-Body. |
| PUT | Aktualisiert Informationen am Endpunkt und ersetzt vorhandene Informationen durch den Inhalt des Anfrage-Bodys. |
| DELETE | Löscht die Ressource in der HTTP-URL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTTP-Methode" }

### Anfrage-Body {#request-body}

Der Anfrage-Body enthält die Informationen, die an die von Ihnen angegebene URL gesendet werden. Sie können den Body Ihrer Webhook-Anfrage mit JSON-Schlüssel-Wert-Paaren oder Rohtext erstellen.

#### JSON-Schlüssel-Wert-Paare {#json-key-value-pairs}

JSON-Schlüssel-Wert-Paare ermöglichen es Ihnen, einfach eine Anfrage für einen Endpunkt zu schreiben, der ein JSON-Format erwartet. Sie können dies nur mit einem Endpunkt verwenden, der eine JSON-Anfrage erwartet. Wenn Ihr Schlüssel beispielsweise `message_body` ist, könnte der entsprechende Wert `Your order just arrived!` lauten. Nachdem Sie Ihr Schlüssel-Wert-Paar eingegeben haben, konfiguriert der Composer Ihre Anfrage in JSON-Syntax, und eine Vorschau Ihrer JSON-Anfrage wird automatisch angezeigt.

![Anfrage-Body mit JSON-Schlüssel-Wert-Paaren.]({% image_buster /assets/img/webhook_json_1.png %})

Sie können Ihre Schlüssel-Wert-Paare mit Liquid personalisieren, z. B. indem Sie beliebige Nutzerattribute, [angepasste Attribute]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#additional-notes-and-best-practices) oder [Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events) in Ihre Anfrage aufnehmen. Sie können beispielsweise den Vornamen und die E-Mail-Adresse von Kund:innen in Ihre Anfrage aufnehmen. Stellen Sie sicher, dass Sie für jedes Attribut einen [Standardwert]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) angeben.

#### Rohtext {#raw-text}

Die Rohtext-Option bietet Ihnen die Flexibilität, eine Anfrage für einen Endpunkt zu schreiben, der einen Body in einem beliebigen Format erwartet. Sie können dies beispielsweise verwenden, um eine Anfrage für einen Endpunkt zu schreiben, der Ihre Anfrage im XML-Format erwartet.

Sowohl [Personalisierung]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) als auch [Internationalisierung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) mit Liquid werden im Rohtext unterstützt.

![Ein Beispiel für einen Anfrage-Body mit Rohtext unter Verwendung von Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Wenn Sie den `Content-Type`-[Anfrage-Header](#request-headers-optional) auf `application/x-www-form-url-encoded` setzen, muss der Anfrage-Body als URL-codierter String formatiert sein. Zum Beispiel:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Anfrage-Body mit URL-codiertem String.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Schritt 3: Zusätzliche Einstellungen konfigurieren {#step-3-configure-additional-settings}

### Anfrage-Header (optional) {#request-headers-optional}

Bestimmte Endpunkte erfordern möglicherweise, dass Sie Header in Ihre Anfrage aufnehmen. Im Abschnitt **Compose** des Composers können Sie so viele Header hinzufügen, wie benötigt werden.

![Beispiele für Anfrage-Header mit dem Schlüssel „Authorization“ und dem Schlüssel „Content-Type“.]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Gängige Anfrage-Header sind [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)-Spezifikationen (die beschreiben, welche Art von Daten im Body erwartet werden, z. B. XML oder JSON) und [`Authorization`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)-Header, die Ihre Zugangsdaten für Ihren Anbieter oder Ihr System enthalten.

{% alert note %}
HTTP-Header-Namen sind gemäß [RFC 7230, Abschnitt 3.2 („Each header field consists of a case-insensitive field name“)](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2) nicht case-sensitiv. Wenn Ihr empfangender Endpunkt oder zwischengeschaltete Dienste (wie CDNs) die Groß-/Kleinschreibung von Headern ändern, hat dies keinen Einfluss auf die Header-Verarbeitung – `Content-Type`, `content-type` und `CONTENT-TYPE` werden alle identisch behandelt.
{% endalert %}

Content-Typ-Spezifikationen müssen den Schlüssel `Content-Type` verwenden. Gängige Werte sind `application/json` oder `application/x-www-form-urlencoded`.

Authorization-Header müssen den Schlüssel `Authorization` verwenden. Gängige Werte sind {% raw %} `Bearer {{YOUR_TOKEN}}` oder `Basic {{YOUR_TOKEN}}` {% endraw %}, wobei `YOUR_TOKEN` die von Ihrem Anbieter oder System bereitgestellten Zugangsdaten sind.

## Schritt 4: Testnachricht senden {#step-4-test-send-your-message}

Bevor Sie Ihre Campaign live schalten, empfiehlt Braze, den Webhook zu testen, um sicherzustellen, dass die Anfrage korrekt formatiert ist.

Wechseln Sie dazu zum Tab **Test** und senden Sie einen Test-Webhook. Sie können den Webhook als zufällige:r Nutzer:in, als bestimmte:r Nutzer:in (durch Eingabe der E-Mail-Adresse oder externen Nutzer-ID) oder als angepasste:r Nutzer:in mit Attributen Ihrer Wahl testen.

Nach dem Senden des Test-Webhooks erscheint ein Dialogfeld mit der Antwortnachricht. Wenn die Webhook-Anfrage nicht erfolgreich ist, nutzen Sie die Fehlermeldung zur Fehlerbehebung Ihres Webhooks. Das folgende Beispiel zeigt die Antwort eines Webhooks mit einer ungültigen Webhook-URL.

```http
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=webhook).

## Schritt 5: Erstellen Sie den Rest Ihrer Campaign oder Ihres Canvas {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Erstellen Sie als Nächstes den Rest Ihrer Campaign. In den folgenden Abschnitten finden Sie weitere Details zur optimalen Nutzung unserer Tools zum Erstellen von Webhooks.

### Zustellungszeitplan oder Trigger wählen {#choose-delivery-schedule-or-trigger}

Webhooks können basierend auf einem geplanten Zeitpunkt, einer Aktion oder einem API-Trigger zugestellt werden. Weitere Informationen finden Sie unter [Ihre Campaign planen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Bei aktionsbasierter Zustellung können Sie auch die Dauer der Campaign und die [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours) festlegen.

In diesem Schritt können Sie auch Zustellungskontrollen festlegen, z. B. ob Nutzer:innen [erneut berechtigt]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) werden können, die Campaign zu erhalten, oder ob [Frequency-Capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)-Regeln aktiviert werden sollen.

### Zielgruppe zusammenstellen {#choose-users-to-target}

Als Nächstes müssen Sie [Nutzer:innen als Zielgruppe auswählen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users), indem Sie Segmente oder Filter wählen, um Ihre Zielgruppe einzugrenzen. In diesem Schritt wählen Sie die größere Zielgruppe aus Ihren Segmenten aus und grenzen dieses Segment bei Bedarf mit unseren Filtern weiter ein. Sie erhalten automatisch eine Vorschau der ungefähren Segmentgröße. Beachten Sie, dass die genaue Segmentzugehörigkeit immer vor dem Versand der Nachricht berechnet wird.

{% multi_lang_include audience/target_audiences.md %}

### Konversions-Events wählen {#choose-conversion-events}

Braze ermöglicht es Ihnen, nachzuverfolgen, wie oft Nutzer:innen bestimmte Aktionen, sogenannte [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), nach Erhalt einer Campaign ausführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen festzulegen, in dem eine Konversion gezählt wird, wenn die Nutzer:innen die angegebene Aktion ausführen.

{% endtab %}

{% tab Canvas %}

Falls noch nicht geschehen, vervollständigen Sie die verbleibenden Abschnitte Ihres Canvas-Schritts. Weitere Details zum Aufbau des restlichen Canvas, zur Implementierung multivariater Tests und der intelligenten Auswahl und mehr finden Sie im Schritt [Canvas erstellen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## Schritt 6: Überprüfen und bereitstellen {#step-6-review-and-deploy}

Nachdem Sie den letzten Teil Ihrer Campaign oder Ihres Canvas fertig erstellt haben, überprüfen Sie die Details, testen Sie alles und senden Sie es ab!

## Wissenswertes {#things-to-know}

### Fehler, Wiederholungslogik und Timeouts {#errors-retry-logic-and-timeouts}

Webhooks basieren darauf, dass Braze-Server Anfragen an einen externen Endpunkt senden, und gelegentlich können Fehler auftreten. Die häufigsten Fehler sind Syntaxfehler, abgelaufene API-Schlüssel, Rate-Limits und unerwartete serverseitige Probleme. Bevor Sie eine Webhook-Campaign senden:

- Testen Sie Ihren Webhook auf Syntaxfehler
- Stellen Sie sicher, dass personalisierte Variablen Standardwerte haben

Wenn Ihr Webhook nicht gesendet werden kann, wird eine Fehlermeldung im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) protokolliert, die Details wie den Fehlerzeitstempel, den App-Namen und Informationen zum Fehler enthält.

![Webhook-Fehler mit der Meldung „An active access token must be used to query information about the current user“.]({% image_buster /assets/img_archive/webhook-error.png %})

Wenn die Fehlermeldung nicht ausreichend Aufschluss über die Fehlerursache gibt, sollten Sie die Dokumentation des verwendeten API-Endpunkts prüfen. Diese enthält in der Regel eine Erklärung der Fehlercodes, die der Endpunkt verwendet, sowie deren typische Ursachen.

#### Antwortcodes und Wiederholungslogik {#response-codes-and-retry-logic}

Wenn die Webhook-Anfrage gesendet wird, gibt der empfangende Server einen Antwortcode zurück, der angibt, was mit der Anfrage passiert ist. Die folgende Tabelle fasst die verschiedenen Antworten zusammen, die der Server senden kann, wie sie sich auf die Campaign-Analytics auswirken und ob Braze im Fehlerfall versucht, die Campaign erneut zuzustellen:

| Antwortcode | Als empfangen markiert? | Wiederholung? |
|---------------|-----------|----------|
| `20x` (Erfolg)  | Ja |   N/A  |
| `30x` (Weiterleitung)  | Nein | Nein |
| `408` (Anfrage-Timeout)  | Nein | Ja |
| `429` (Rate-Limit erreicht)  | Nein | Ja |
| `Andere 4XX` (Client-Fehler)  | Nein | Nein |
| `5XX` (Server-Fehler)   | Nein | Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Antwortcodes und Wiederholungslogik" }

{% alert note %}
Braze wiederholt die weiter oben in diesem Abschnitt genannten Statuscodes bis zu fünfmal innerhalb von 30 Minuten mit exponentiellem Backoff. Wenn Ihr Endpunkt nicht erreichbar ist, können sich die Wiederholungen über einen Zeitraum von 24 Stunden verteilen.<br><br>Jeder Webhook hat ein Timeout von 90 Sekunden.
{% endalert %}

`Retry-After`- und Rate-Limit-Antwort-Header können beeinflussen, wie lange Braze vor einem **wiederholbaren** Versuch wartet (zum Beispiel nach `408`, `429` oder `5XX`). Sie machen nicht wiederholbare Antworten wie `401` nicht für eine Wiederholung zulässig.

#### 403 Forbidden und IP-Allowlisting {#403-forbidden-and-ip-allowlisting}

`403 Forbidden`-Antworten bedeuten, dass Ihr Endpunkt die Anfrage empfangen, aber abgelehnt hat. Häufige Ursachen sind ungültige oder fehlende Authentifizierung, unzureichende API-Berechtigungen und Netzwerkregeln (wie eine Firewall oder Web Application Firewall), die die ausgehenden IP-Adressen von Braze blockieren.

Wenn Webhook-Anfragen durchgehend `403` zurückgeben und Ihre Authentifizierungs-Header korrekt sind, setzen Sie die Braze-IPs für Ihren Cluster auf dem Server, der den Webhook empfängt, auf die Allowlist. Siehe [IP-Allowlisting](#ip-allowlisting). Connected-Content-Anfragen verwenden dieselben ausgehenden IPs; siehe [Connected-Content-IP-Allowlisting]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting).

Für weitere `4XX`-Fehlerbehebungsschritte siehe [Fehlerbehebung bei Webhook- und Connected-Content-Anfragen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#4xx-errors).

#### Authentifizierung und Connected-Content-Zugangsdaten {#authentication-and-connected-content-credentials}

Die ausgehende Webhook-HTTP-Anfrage unterstützt nicht das Anhängen von [Connected-Content-Zugangsdaten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types) (`:basic_auth` oder `:auth_credentials`) zur Authentifizierung gegenüber Ihrem Endpunkt. Richten Sie die Authentifizierung stattdessen über **Anfrage-Header** im Webhook ein. Um ein Token oder Secret zum Sendezeitpunkt abzurufen, können Sie ein {% raw %}`{% connected_content %}`{% endraw %}-Tag in ein Header- oder Body-Feld einfügen, damit Liquid es auflöst, bevor der Webhook gesendet wird.

#### Gespeicherte Webhook-Templates und Campaign-Nutzung {#saved-webhook-templates-and-campaign-usage}

Braze bietet keinen integrierten Bericht, der jede Campaign oder jeden Canvas-Schritt auflistet, die auf ein bestimmtes **gespeichertes Webhook-Template** verweisen. Um die Nutzung zu prüfen, überprüfen Sie Webhook-Schritte, die dieselbe URL und HTTP-Methode verwenden, oder kontaktieren Sie den [Braze-Support]({{site.baseurl}}/support_contact).

#### Fehlerbehebung und zusätzliche Fehlerdetails {#troubleshooting-and-additional-error-details}

Ausführliche Erklärungen, Fehlerbehebungsschritte und Anleitungen zur Behebung spezifischer Webhook-Fehler finden Sie unter [Fehlerbehebung bei Webhook- und Connected-Content-Anfragen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content). Dort finden Sie auch weitere Erklärungen zur Funktionsweise unseres Systems zur Erkennung fehlerhafter Hosts und dazu, wie Braze Fehlerbenachrichtigungen über automatisierte E-Mails und zusätzliche Protokollierung in Braze-Currents bereitstellt.

### IP-Allowlisting {#ip-allowlisting}

Wenn ein Webhook von Braze gesendet wird, stellen die Braze-Server Netzwerkanfragen an Kund:innen- oder Drittanbieter-Server. Mit IP-Allowlisting können Sie überprüfen, ob Webhook-Anfragen von Braze stammen, und so eine zusätzliche Sicherheitsebene hinzufügen.

Braze sendet Webhooks von den folgenden IPs. Die aufgeführten IPs werden automatisch und dynamisch zu allen API-Schlüsseln hinzugefügt, die für das Allowlisting aktiviert wurden.

{% alert important %}
Wenn Sie einen Braze-zu-Braze-Webhook erstellen und Allowlisting verwenden, sollten Sie alle folgenden IPs auf die Allowlist setzen, einschließlich `127.0.0.1`.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Nutzer:innen löschen {#delete-users}

Um einzelne Nutzer:innen oder ein Segment von Nutzer:innen zu löschen, gehen Sie zu **Audience** > **Manage Audience** > **Delete Users**. Das Dashboard unterstützt die Massenlöschung von Segmenten (bis zu 10 Millionen Profile), bietet ein 7-tägiges Stornierungsfenster und verbraucht keine gemeinsamen REST API-Rate-Limits. Schritte, Limits und Berechtigungen finden Sie unter [Nutzer:innen löschen]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users).

Für die programmatische Löschung in kleineren Batches verwenden Sie den [`/users/delete`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) anstelle einer Webhook-Campaign.