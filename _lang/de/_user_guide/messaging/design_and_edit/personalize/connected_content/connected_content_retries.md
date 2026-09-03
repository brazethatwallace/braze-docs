---
nav_title: Connected-Content-Wiederholungsversuche
article_title: Connected-Content-Wiederholungsversuche
page_order: 5
description: "Dieser Referenzartikel behandelt den Umgang mit Connected-Content-Wiederholungsversuchen."

---

# Wiederholungslogik für Connected-Content verwenden {#use-retry-logic-for-connected-content}

> Auf dieser Seite erfahren Sie, wie Sie Wiederholungsversuche zu Ihren Connected-Content-Aufrufen hinzufügen.

## Funktionsweise von Wiederholungsversuchen {#how-retries-work}

Da Connected Content auf den Empfang von Daten aus APIs angewiesen ist, kann eine API vorübergehend nicht verfügbar sein, während Braze den Aufruf durchführt. In diesem Fall unterstützt Braze eine Wiederholungslogik, um die Anfrage mithilfe von exponentiellem Backoff erneut zu versuchen.

{% alert note %}
Connected-Content `:retry` ist für In-App Messages nicht verfügbar.
{% endalert %}

## Verwendung der Wiederholungslogik {#using-retry-logic}

Um die Wiederholungslogik zu verwenden, fügen Sie dem Connected-Content-Aufruf den Tag `:retry` hinzu, wie im folgenden Code-Snippet gezeigt:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Wenn ein `:retry`-Tag im Connected-Content-Aufruf enthalten ist, versucht Braze, den Aufruf bis zu fünfmal zu wiederholen.

### Vorschauverhalten {#preview-behavior}

Die Wiederholungslogik gilt nur für Live-Sendungen (einschließlich Testsendungen), nicht für Vorschauen. Wenn ein Connected-Content-Aufruf mit `:retry` während der Vorschau fehlschlägt, zeigt die Vorschau möglicherweise die Nachricht „This message would not have been shown because retry functionality was triggered“ an, anstatt den Inhalt zu rendern. Dies ist das erwartete Verhalten und weist nicht auf ein Problem innerhalb von Braze hin.

### Ergebnisse der Wiederholung {#retry-outcomes}

#### Wenn eine Wiederholung erfolgreich ist {#when-a-retry-succeeds}

Wenn ein wiederholter Versuch erfolgreich ist, wird die Nachricht gesendet und es werden keine weiteren Wiederholungen für diese Nachricht unternommen.

#### Wenn der API-Aufruf fehlschlägt und Wiederholungen aktiviert sind {#when-the-api-call-fails-and-retries-are-enabled}

Wenn der API-Aufruf fehlschlägt und diese Funktion aktiviert ist, wiederholt Braze den Aufruf unter Einhaltung des [Rate-Limits]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), das Sie für jede erneute Sendung festgelegt haben. Braze verschiebt fehlgeschlagene Nachrichten an das Ende der Warteschlange und fügt bei Bedarf zusätzliche Minuten zur Gesamtdauer hinzu, die für den Versand Ihrer Nachricht benötigt wird.

Wenn der Connected-Content-Aufruf mehr als fünfmal fehlschlägt, wird die Nachricht abgebrochen, ähnlich wie bei einem ausgelösten [Abbruch-Nachrichten-Tag]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content).

{% multi_lang_include connected_content/abort_and_retry_logic.md %}