---
nav_title: Connected-Content-Wiederholungsversuche
article_title: Connected-Content-Wiederholungsversuche
page_order: 5
description: "Dieser Referenzartikel behandelt den Umgang mit Connected-Content-Wiederholungsversuchen."

---

# Wiederholungslogik für Connected-Content verwenden {#use-retry-logic-for-connected-content}

> Auf dieser Seite erfahren Sie, wie Sie Wiederholungsversuche zu Ihren Connected-Content-Aufrufen hinzufügen.

## Funktionsweise von Wiederholungsversuchen {#how-retries-work}

Da Connected-Content auf den Empfang von Daten von APIs angewiesen ist, kann eine API zeitweise nicht verfügbar sein, während Braze den Aufruf durchführt. In diesem Fall unterstützt Braze eine Wiederholungslogik, um die Anfrage mit exponentiellem Backoff erneut zu versuchen.

{% alert note %}
Connected-Content `:retry` ist für In-App-Nachrichten nicht verfügbar.
{% endalert %}

## Wiederholungslogik verwenden {#using-retry-logic}

Um die Wiederholungslogik zu verwenden, fügen Sie das `:retry`-Tag zum Connected-Content-Aufruf hinzu, wie im folgenden Code-Snippet gezeigt:

{% raw %}
```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}

Wenn ein `:retry`-Tag im Connected-Content-Aufruf enthalten ist, versucht Braze den Aufruf bis zu fünf Mal zu wiederholen.

### Ergebnisse der Wiederholungsversuche {#retry-outcomes}

#### Wenn ein Wiederholungsversuch erfolgreich ist {#when-a-retry-succeeds}

Wenn ein erneuter Versuch erfolgreich ist, wird die Nachricht gesendet und es werden keine weiteren Wiederholungsversuche für diese Nachricht unternommen.

#### Wenn der API-Aufruf fehlschlägt und Wiederholungsversuche aktiviert sind {#when-the-api-call-fails-and-retries-are-enabled}

Wenn der API-Aufruf fehlschlägt und diese Funktion aktiviert ist, wiederholt Braze den Aufruf unter Einhaltung der [Rate-Limits]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting), die Sie für jeden erneuten Versand festgelegt haben. Braze verschiebt fehlgeschlagene Nachrichten an das Ende der Warteschlange und fügt bei Bedarf zusätzliche Minuten zur Gesamtzeit hinzu, die für den Versand Ihrer Nachricht benötigt wird.

Wenn der Connected-Content-Aufruf mehr als fünf Mal fehlschlägt, wird die Nachricht abgebrochen, ähnlich wie ein [Nachricht-abbrechen-Tag]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content) ausgelöst wird.

{% multi_lang_include connected_content/abort_and_retry_logic.md %}