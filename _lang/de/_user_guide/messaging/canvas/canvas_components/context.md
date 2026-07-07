---
nav_title: Kontext
article_title: Kontext
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Dieser Referenzartikel beschreibt, wie Sie Kontext-Schritte in Ihrem Canvas erstellen und verwenden."
tool: Canvas

---

# Kontext {#context}

> Mit Kontext-Schritten können Sie eine oder mehrere Variablen für Nutzer:innen erstellen und aktualisieren, während diese sich durch einen Canvas bewegen. Wenn Sie beispielsweise einen Canvas haben, der saisonale Rabatte verwaltet, können Sie eine Kontextvariable verwenden, um bei jedem Eintritt in den Canvas einen anderen Rabattcode zu speichern.

## So funktioniert es {#how-it-works}

![Ein Kontext-Schritt als erster Schritt eines Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Kontext-Schritte ermöglichen es Ihnen, temporäre Daten während der Journey von Nutzer:innen durch einen bestimmten Canvas zu erstellen und zu verwenden. Diese Daten existieren nur innerhalb dieser Canvas-Journey und bleiben nicht über verschiedene Canvases hinweg oder außerhalb der Sitzung bestehen.

Kontextvariablen existieren nur für diese spezifische Canvas-Journey. Sie ändern das Profil der Nutzer:innen nicht dauerhaft und erscheinen nicht in anderen Canvases. Das macht sie ideal für temporäre Informationen, die nur für eine bestimmte Campaign oder einen bestimmten Workflow relevant sind.

{% alert tip %}
Eine vollständige Referenz zu Kontextvariablen, einschließlich Datentypen, Verwendung und Best Practices, finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).
{% endalert %}

Innerhalb eines Kontext-Schritts können Sie bis zu 10 Kontextvariablen definieren oder aktualisieren. Diese Variablen können verwendet werden, um Verzögerungen zu personalisieren, Nutzer:innen dynamisch zu segmentieren und Nachrichten im gesamten Canvas anzureichern. Sie könnten beispielsweise eine Kontextvariable für die geplante Flugzeit erstellen und diese dann verwenden, um personalisierte Verzögerungen festzulegen und Erinnerungen zu senden.

Sie können Kontextvariablen auf zwei Arten festlegen:

- **Beim Canvas-Eintritt:** Eigenschaften aus dem angepassten Event oder dem API-Trigger werden automatisch als Kontextvariablen befüllt.
- **In einem Kontext-Schritt:** Definieren oder aktualisieren Sie Kontextvariablen manuell, indem Sie einen Kontext-Schritt hinzufügen.

Jede Kontextvariable erfordert einen Namen, einen Datentyp und einen Wert (festgelegt mit Liquid oder dem Tool „Personalisierung hinzufügen“). Nach der Definition können Sie Kontextvariablen im gesamten Canvas mit Liquid referenzieren, z. B. {% raw %}`{{context.${flight_time}}}`{% endraw %}. Im Feld **Context variable name** können Sie auch den Namen der Kontextvariable eingeben oder ihn aus dem Dropdown im Schritt-Editor auswählen. Details finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

Jeder Canvas-Eintritt definiert Kontextvariablen basierend auf den neuesten Eintrittsdaten und der Canvas-Konfiguration neu, sodass Nutzer:innen mehrere aktive Journeys mit eigenem Kontext haben können. Wenn beispielsweise ein:e Kund:in zwei bevorstehende Flüge hat, laufen zwei separate Journey-Zustände gleichzeitig&#8212;jeder mit eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Zielort. So können Sie personalisierte Erinnerungen über den 14-Uhr-Flug nach New York senden und gleichzeitig andere Updates über den 8-Uhr-Flug nach Los Angeles am nächsten Tag versenden, sodass jede Nachricht für die jeweilige Buchung relevant bleibt.

### Nutzerverarbeitung und Batching {#user-processing-and-batching}

Kontext-Schritte verarbeiten Nutzer:innen in Batches, um die Performance zu optimieren. Wenn Nutzer:innen einen Kontext-Schritt betreten, verarbeitet Braze sie standardmäßig in Batches von 1.000 Nutzer:innen. Diese Batches werden parallel verarbeitet, aber innerhalb jedes Batches werden Nutzer:innen sequenziell verarbeitet.

Das bedeutet:

**Beispiel**: Wenn 3.500 Nutzer:innen einen Kontext-Schritt mit Connected-Content betreten, der 650 ms pro Nutzer:in benötigt:
- Braze erstellt 4 Batches von Nutzer:innen (in diesem Beispiel 1.000, 1.000, 1.000 und 500 Nutzer:innen).
- Jeder Batch verarbeitet Nutzer:innen sequenziell, sodass ein Batch von 1.000 Nutzer:innen ungefähr 10,8 Minuten dauert (650 Sekunden; 1.000 × 650 ms).
- Batches werden zu unterschiedlichen Zeiten fertig, sodass Nutzer:innen nach und nach in den nächsten Schritt gelangen, sobald ihr Batch abgeschlossen ist.
- Die ersten Nutzer:innen können den nächsten Schritt mehrere Minuten vor den letzten Nutzer:innen erreichen, abhängig von der Batch-Größe und den Antwortzeiten des Connected-Content.

Ohne Connected-Content verarbeiten Kontext-Schritte deutlich schneller, da keine externen API-Aufrufe abgewartet werden müssen.

## Hinweise {#considerations}

- Sie können bis zu 10 Kontextvariablen pro Kontext-Schritt definieren.
- Jede Variable erfordert einen eindeutigen Namen (nur Buchstaben, Zahlen, Unterstriche, bis zu 100 Zeichen).
- Die Gesamtgröße aller Variablen in einem Schritt darf 50 KB nicht überschreiten.
- Variablen, die über API-Trigger übergeben werden, teilen sich denselben Namespace wie die in Kontext-Schritten erstellten; das Neudefinieren einer Variable in einem Kontext-Schritt überschreibt den API-Wert.

Weitere Details und fortgeschrittene Nutzung finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

## Einen Kontext-Schritt erstellen {#creating-a-context-step}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### 1. Schritt: Einen Schritt hinzufügen {#step-1-add-a-step}

Fügen Sie Ihrem Canvas einen Schritt hinzu, indem Sie die Komponente per Drag-and-Drop aus der Seitenleiste ziehen oder den <i class="fas fa-plus-circle"></i> Plus-Button auswählen und **Context** wählen.

### 2. Schritt: Die Variablen definieren {#step-2-define-the-variables}

{% alert note %}
Sie können bis zu 10 Kontextvariablen für jeden Kontext-Schritt definieren.
{% endalert %}

So definieren Sie eine Kontextvariable:

1. Geben Sie Ihrer Kontextvariable einen **Namen**.
2. Wählen Sie einen [Datentyp]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#data-types).
3. Schreiben Sie einen Liquid-Ausdruck manuell oder verwenden Sie **Add Personalization**, um ein Liquid-Snippet aus vorhandenen Attributen zu erstellen.
4. Wählen Sie **Preview**, um den Wert Ihrer Kontextvariable zu überprüfen.
5. (Optional) Um weitere Variablen hinzuzufügen, wählen Sie **Add Context variable** und wiederholen Sie die Schritte 1–4.
6. Wenn Sie fertig sind, wählen Sie **Done**.

Jetzt können Sie Ihre Kontextvariable überall dort verwenden, wo Sie Liquid einsetzen, z. B. in Nachrichten- und Nutzeraktualisierungs-Schritten, indem Sie **Add Personalization** auswählen. Im Feld **Context variable name** können Sie auch den Namen der Kontextvariable eingeben oder ihn aus dem Dropdown im Schritt-Editor auswählen. Eine vollständige Anleitung finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

{% alert important %}
Verwenden Sie beim Referenzieren von Kontextvariablen immer das Format {% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Kontextvariablen-Filter {#context-variable-filters}

Sie können Filter mit Kontextvariablen in [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)- und [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)-Schritten erstellen.

Um Nutzer:innen basierend auf der Antwort eines [Agent-Schritts]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) weiterzuleiten, fügen Sie den Agent-Schritt vor Ihrem Zielgruppenpfade- oder Decision-Split-Schritt hinzu. Der Agent-Schritt speichert seine Ausgabe im Canvas-Kontext, die Sie mit Kontextvariablen-Filtern in diesen Verzweigungsschritten auswerten können.

Wenn der Agent ein Objekt zurückgibt und Sie nach einer verschachtelten Eigenschaft filtern möchten, geben Sie den Pfad im Feld **Context variable name** in Punktnotation ein, anstatt nur den übergeordneten Variablennamen zu verwenden (z. B. `intent_agent.persona`, wenn `persona` unter `intent_agent` verschachtelt ist).

Informationen zur Filter-Einrichtung, Vergleichslogik und fortgeschrittenen Beispielen finden Sie in der [Referenz zu Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Nutzerpfade in der Vorschau anzeigen {#previewing-user-paths}

Wir empfehlen, Ihre [Nutzerpfade zu testen und in der Vorschau anzuzeigen]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths), um sicherzustellen, dass Ihre Nachrichten an die richtige Zielgruppe gesendet werden und Kontextvariablen die erwarteten Ergebnisse liefern.

{% alert note %}
Wenn Sie Ihren Canvas im Abschnitt **Preview & Test Send** des Editors in der Vorschau anzeigen, wird der Zeitstempel in der Testnachrichten-Vorschau **nicht** auf UTC standardisiert, da dieses Panel Vorschauen als Strings generiert. Das bedeutet: Wenn ein Canvas so eingerichtet ist, dass er ein `time`-Objekt akzeptiert, zeigt die Nachrichtenvorschau nicht genau an, was passiert, wenn der Canvas live ist. Um Ihren Canvas möglichst genau zu testen, empfehlen wir stattdessen die Vorschau der Nutzerpfade.
{% endalert %}

Achten Sie auf häufige Szenarien, die ungültige Kontextvariablen erzeugen. Bei der Vorschau Ihres Nutzerpfads können Sie die Ergebnisse personalisierter Verzögerungsschritte mit Kontextvariablen sowie alle Zielgruppen- oder Decision-Schritt-Vergleiche einsehen, die Nutzer:innen mit Kontextvariablen abgleichen.

Wenn die Kontextvariable gültig ist, können Sie die Variable im gesamten Canvas referenzieren. Wenn die Kontextvariable jedoch nicht korrekt erstellt wurde, funktionieren auch nachfolgende Schritte in Ihrem Canvas nicht korrekt. Wenn Sie beispielsweise einen Kontext-Schritt erstellen, um Nutzer:innen eine Terminzeit zuzuweisen, und den Wert der Terminzeit auf ein vergangenes Datum setzen, wird die Erinnerungs-E-Mail in Ihrem Nachrichten-Schritt nicht gesendet.

## Connected-Content-Strings in JSON konvertieren {#converting-connected-content-strings-to-json}

Wenn Sie einen [Connected-Content-Aufruf]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) in einem Kontext-Schritt durchführen, wird das vom Aufruf zurückgegebene JSON aus Konsistenz- und Fehlervermeidungsgründen als String-Datentyp ausgewertet. Wenn Sie diesen String in JSON konvertieren möchten, verwenden Sie `as_json_string`. Zum Beispiel:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Fehlerbehebung {#troubleshooting}

### Ungültige Kontextvariablen {#invalid-context-variables}

Eine Kontextvariable gilt als ungültig, wenn:

- Ein Aufruf an einen eingebetteten Connected-Content fehlschlägt.
- Der Liquid-Ausdruck zur Laufzeit einen Wert zurückgibt, der nicht zum Datentyp passt oder leer (null) ist.

Wenn beispielsweise der Datentyp der Kontextvariable **Zahl** ist, der Liquid-Ausdruck aber einen String zurückgibt, ist sie ungültig.

In diesen Fällen:
- Die Nutzer:innen werden zum nächsten Schritt weitergeleitet.
- Die Canvas-Schritt-Analytics zählt dies als _Nicht aktualisiert_.

Überwachen Sie bei der Fehlerbehebung die Metrik _Nicht aktualisiert_, um zu prüfen, ob Ihre Kontextvariable korrekt aktualisiert wird. Wenn die Kontextvariable ungültig ist, können Ihre Nutzer:innen im Canvas über den Kontext-Schritt hinaus fortfahren, qualifizieren sich aber möglicherweise nicht für spätere Schritte.

Informationen zu den Beispielkonfigurationen für jeden Datentyp finden Sie unter [Datentypen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#data-types).

### Verzögerungen beim Senden mit Connected-Content {#delays-in-sending-with-connected-content}

Alle Nutzer:innen in einem Batch werden verarbeitet, bevor Nutzer:innen weitergeleitet werden. Nach Abschluss der Batch-Verarbeitung werden erfolgreiche Nutzer:innen zum nächsten Schritt weitergeleitet, während fehlgeschlagene Nutzer:innen separat erneut versucht werden – erfolgreiche Nutzer:innen warten nicht darauf, dass Wiederholungsversuche erfolgreich sind, bevor sie weitergeleitet werden.

#### Wiederholungsverhalten {#retry-behavior}

In Canvas-Schritten (einschließlich Kontext-Schritten) verwendet Braze Canvas-spezifische Wiederholungsmechanismen anstelle des standardmäßigen Connected-Content-Wiederholungsverhaltens. Wenn ein Connected-Content-Aufruf fehlschlägt:

 - Bei Nachrichten-Schritten können Connected-Content-Aufrufe bis zu fünfmal wiederholt werden.
 - Bei allen anderen Schritten wiederholt Braze den Schritt ungefähr 13 Mal mit exponentiellem Backoff.

Wenn alle Wiederholungsversuche fehlschlagen, verlassen die Nutzer:innen den Canvas.

Das `:retry`-Tag, das im Standard-Connected-Content verwendet wird, gilt nicht für Connected-Content-Aufrufe innerhalb von Canvas-Schritten. Canvas-Schritte haben ihre eigene Wiederholungslogik, die für Canvas-Workflows optimiert ist.

Die Zeit, die benötigt wird, um alle Nutzer:innen durch einen Kontext-Schritt zu verarbeiten, hängt ab von:

- Der Anzahl der Nutzer:innen, die den Schritt betreten
- Ob Connected-Content verwendet wird (und dessen Antwortzeit)
- Der Batch-Größe (Standard: 1.000 Nutzer:innen pro Batch)

Wenn Ihr Connected-Content-Endpunkt Rate-Limits hat, beachten Sie, dass Kontext-Schritte Nutzer:innen innerhalb jedes Batches sequenziell verarbeiten, was die Einhaltung von Rate-Limits auf natürliche Weise unterstützt. Da jedoch mehrere Batches parallel verarbeitet werden, stellen Sie sicher, dass Ihr Endpunkt gleichzeitige Anfragen von mehreren Batches verarbeiten kann.

## Standardisierung der Zeitzonenkonsistenz {#time-zone-consistency-standardization}

Mit der allgemeinen Verfügbarkeit von Canvas-Kontext sind alle Standard-Zeitstempel-Event-Eigenschaften in aktionsbasierten Canvases in UTC. Diese Änderung ist Teil einer umfassenderen Initiative, um eine vorhersehbarere und konsistentere Erfahrung beim Bearbeiten von Canvas-Schritten und Nachrichten zu gewährleisten. Beachten Sie, dass diese Änderung alle aktionsbasierten Canvases betrifft, unabhängig davon, ob der jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

{% alert important %}
In allen Fällen empfehlen wir dringend die Verwendung von [Liquid-time_zone-Filtern]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know) für Zeitstempel, damit diese in der gewünschten Zeitzone dargestellt werden. Ein Beispiel finden Sie in dieser [häufig gestellten Frage](#faq-example).
{% endalert %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Was hat sich geändert, seit Canvas-Kontext allgemein verfügbar ist? {#what-has-changed-since-canvas-context-became-generally-available}

Seit Canvas-Kontext allgemein verfügbar ist, gelten folgende Details:

- Alle Zeitstempel mit einem [Datetime-Typ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) aus [Trigger-Event-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) in aktionsbasierten Canvases sind in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
- Diese Änderung betrifft alle aktionsbasierten Canvases, unabhängig davon, ob der jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

#### Was ist der Grund für diese Änderung? {#what-is-the-reason-for-this-change}

Diese Änderung ist Teil einer umfassenderen Initiative, um eine vorhersehbarere und konsistentere Erfahrung beim Bearbeiten von Canvas-Schritten und Nachrichten zu schaffen.

#### Sind API-getriggerte oder geplante Canvases von dieser Änderung betroffen? {#are-api-triggered-or-scheduled-canvases-impacted-by-this-change}

Nein.

#### Betrifft diese Änderung Canvas-Eingangs-Eigenschaften? {#does-this-change-impact-canvas-entry-properties}

Ja, dies betrifft `canvas_entry_properties`, wenn die `canvas_entry_property` in einem aktionsbasierten Canvas verwendet wird und der Eigenschaftstyp `time` ist. In allen Fällen empfehlen wir die Verwendung von Liquid-`time_zone`-Filtern, damit Zeitstempel in der gewünschten Zeitzone dargestellt werden.

Hier ist ein Beispiel dafür:

| Liquid im Nachrichten-Schritt | Ausgabe | Ist dies die korrekte Art, Zeitzonen in Liquid darzustellen? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | Nein |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | Nein |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Betrifft diese Änderung Canvas-Eingangs-Eigenschaften?" }

#### Was ist ein praktisches Beispiel dafür, wie das neue Zeitstempelverhalten meine Nachrichten beeinflussen könnte? {#faq-example}

Nehmen wir an, wir haben einen aktionsbasierten Canvas mit folgendem Inhalt in einem Nachrichten-Schritt:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Dies ergibt folgende Nachricht:

```
Your appointment is scheduled for 2025-08-05 4:15 PM, we’ll see you then!
```

Da keine Zeitzone mit Liquid angegeben ist, ist der Zeitstempel hier in UTC.

Um eine Zeitzone klar anzugeben, können wir Liquid-`time_zone`-Filter wie folgt verwenden:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Dies ergibt folgende Nachricht:

```
Your appointment is scheduled for 2025-08-05 8:15 AM, we'll see you then!
```

Da die Zeitzone America/Los Angeles mit Liquid angegeben ist, ist der Zeitstempel hier in PST.

Die bevorzugte Zeitzone kann auch im Event-Eigenschaften-Payload gesendet und in der Liquid-Logik verwendet werden:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### Wie unterscheiden sich Kontextvariablen von Canvas-Eingangs-Eigenschaften? {#how-do-context-variables-differ-from-canvas-entry-properties}

Canvas-Eingangs-Eigenschaften werden als Canvas-Kontextvariablen einbezogen. Das bedeutet, Sie können Canvas-Eingangs-Eigenschaften über die Braze-API senden und sie in anderen Schritten referenzieren, ähnlich wie bei der Verwendung einer Kontextvariable mit dem Liquid-Snippet.

### Können Variablen sich gegenseitig in einem einzelnen Kontext-Schritt referenzieren? {#can-variables-reference-each-other-in-a-singular-context-step}

Ja. Alle Variablen in einem Kontext-Schritt werden der Reihe nach ausgewertet, was bedeutet, dass Sie die folgenden Kontextvariablen einrichten könnten:

| Kontextvariable | Wert | Beschreibung |
|---|---|---|
| `favorite_cuisine` | {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | Die Lieblingsküche der Nutzer:innen. |
| `promo_code` | {% raw %}`EATFRESH`{% endraw %} | Der verfügbare Rabattcode für Nutzer:innen. |
| `personalized_message` | {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Eine personalisierte Nachricht, die die vorherigen Variablen kombiniert. In einem Nachrichten-Schritt könnten Sie das Liquid-Snippet {% raw %}`{{context.${personalized_message}}}`{% endraw %} verwenden, um die Kontextvariable zu referenzieren und jeder Nutzer:in eine personalisierte Nachricht zu übermitteln. Sie könnten auch einen Kontext-Schritt verwenden, um den [Aktionscode]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes#creating-a-promotion-code-list)-Wert zu speichern und ihn in anderen Schritten im gesamten Canvas als Template einzusetzen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Können Variablen sich gegenseitig in einem einzelnen Kontext-Schritt referenzieren?" }

Dies gilt auch über mehrere Kontext-Schritte hinweg. Stellen Sie sich beispielsweise folgende Abfolge vor:

1. Ein erster Kontext-Schritt erstellt eine Variable namens `JobInfo` mit dem Wert `job_title`.
2. Ein Nachrichten-Schritt referenziert {% raw %}`{{context.${JobInfo}}}`{% endraw %} und zeigt den Nutzer:innen `job_title` an.
3. Später aktualisiert ein Kontext-Schritt die Kontextvariable und ändert den Wert von `JobInfo` zu `job_description`.
4. Alle nachfolgenden Schritte, die `JobInfo` referenzieren, verwenden nun den aktualisierten Wert `job_description`.

Kontextvariablen verwenden ihren aktuellsten Wert im gesamten Canvas, wobei jede Aktualisierung alle folgenden Schritte beeinflusst, die diese Variable referenzieren.