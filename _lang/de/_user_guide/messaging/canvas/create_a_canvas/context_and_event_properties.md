---
nav_title: Context- und Event-Eigenschaften
article_title: Context- und Event-Eigenschaften
page_order: 4.2
page_type: reference
description: "Dieser Referenzartikel beschreibt die Unterschiede zwischen Context- und Event-Eigenschaften und wann welche Eigenschaft verwendet werden sollte."
tool: Canvas
---

# Context- und Event-Eigenschaften {#context-and-event-properties}

> Dieser Referenzartikel behandelt Informationen über `context` und `event_properties`, einschließlich wann welche Eigenschaft verwendet werden sollte und die Unterschiede im Verhalten. <br><br> Allgemeine Informationen zu angepassten Event-Eigenschaften finden Sie unter [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Context-Eigenschaften und Event-Eigenschaften funktionieren innerhalb Ihrer Canvas-Workflows unterschiedlich. Eigenschaften von Events oder API-Aufrufen, die den Eintritt von Nutzer:innen in einen Canvas triggern, werden als `context` bezeichnet. Eigenschaften von Events, die auftreten, während sich Nutzer:innen innerhalb einer Canvas-Journey bewegen, werden als `event_properties` bezeichnet. Der wesentliche Unterschied besteht darin, dass `context` sich nicht nur auf Events konzentriert, sondern auch auf die Eigenschaften von Eingangs-Payloads in API-getriggerten Canvases zugreift.

In der folgenden Tabelle finden Sie eine Zusammenfassung der Unterschiede zwischen Context- und Event-Eigenschaften.

| | Context-Eigenschaften | Event-Eigenschaften |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **Persistenz** | Können von allen [Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)-Schritten für die Dauer eines Canvas referenziert werden. | - Können nur einmal referenziert werden. <br> - Können nicht von nachfolgenden Nachrichten-Schritten referenziert werden. |
| **Canvas-Verhalten** | Können `context` in jedem Schritt eines Canvas referenzieren. Für das Verhalten nach dem Start siehe [Canvases nach dem Start bearbeiten]({{site.baseurl}}/post-launch_edits/#canvas-entry-properties). | - Können `event_properties` im ersten Nachrichten-Schritt **nach** einem [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/)-Schritt referenzieren, bei dem die ausgeführte Aktion ein angepasstes Event oder Kauf-Event ist. <br> - Dürfen nicht nach dem Alle-anderen-Pfad des Aktionspfade-Schritts stehen. <br> - Zwischen den Aktionspfade- und Nachrichten-Schritten können andere Nicht-Nachrichten-Komponenten liegen. Wenn eine dieser Nicht-Nachrichten-Komponenten ein Aktionspfade-Schritt ist, können Nutzer:innen den Alle-anderen-Pfad dieses Aktionspfads durchlaufen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Context- und Event-Eigenschaften" }

{% details Details zum ursprünglichen Canvas-Editor %}

Sie können keine Canvases mehr mit dem ursprünglichen Editor erstellen oder duplizieren. Beachten Sie, dass Canvas Context im ursprünglichen Canvas-Editor nicht unterstützt wird. Dieser Abschnitt dient daher als Referenz für die Verwendung von Canvas-Eingangs-Eigenschaften und Event-Eigenschaften im vorherigen Canvas-Workflow.

**Canvas-Eingangs-Eigenschaften:**
- Persistente Eingangs-Eigenschaften müssen aktiviert sein.
- Können `canvas_entry_properties` nur im ersten vollständigen Schritt eines Canvas referenzieren. Der Canvas muss aktionsbasiert oder API-getriggert sein.

**Eingangs-Eigenschaften:**
- Können `event_properties` in jedem vollständigen Schritt referenzieren, der aktionsbasierte Zustellung in einem Canvas verwendet.
- Können nicht in geplanten vollständigen Schritten verwendet werden, außer im ersten vollständigen Schritt eines aktionsbasierten Canvas. Wenn jedoch eine [Canvas-Komponente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/) verwendet wird, folgt das Verhalten den aktuellen Canvas-Workflow-Regeln für `event_properties`.

**Event-Eigenschaften:**
- Können `event_properties` nicht im führenden Nachrichten-Schritt verwenden. Stattdessen müssen Sie `canvas_entry_properties` verwenden oder einen Aktionspfade-Schritt mit dem entsprechenden Event **vor** dem Nachrichten-Schritt hinzufügen, der `event_properties` enthält.

{% enddetails %}

### Wissenswertes {#things-to-know}

- Context ist nur als Referenz in Liquid verfügbar. Um nach den Eigenschaften innerhalb des Canvas zu filtern, verwenden Sie stattdessen die [Event-Eigenschafts-Segmentierung]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/).
- Für In-App-Nachrichten-Kanäle können Sie `context` und `event_properties` in einem Canvas referenzieren. Auf `event_properties` kann zugegriffen werden, wenn sie im ersten Canvas-Schritt enthalten sind, da dieser triggerbasiert ist.
- Sie können `event_properties` nicht im führenden Nachrichten-Schritt verwenden. Stattdessen können Sie `context` verwenden oder einen Aktionspfade-Schritt mit dem entsprechenden Event **vor** dem Nachrichten-Schritt hinzufügen, der `event_properties` enthält.
- Wenn ein Aktionspfade-Schritt einen „Eingehende SMS-Nachricht gesendet“- oder „Eingehende WhatsApp-Nachricht gesendet“-Trigger enthält, können die nachfolgenden Canvas-Schritte eine SMS- oder WhatsApp-Liquid-Eigenschaft enthalten. Dies spiegelt wider, wie Event-Eigenschaften in Canvases funktionieren. Auf diese Weise können Sie Ihre Nachrichten nutzen, um First-Party-Daten in Nutzerprofilen und konversationsbasiertem Messaging zu speichern und zu referenzieren.

{% alert note %}
Die Zielgruppen-Berechtigung wird einmalig beim Canvas-Eintritt ausgewertet. Wenn Nutzer:innen während des Eintritts zusammengeführt werden, durchlaufen die identifizierten Nutzer:innen den Canvas weiter und werden nicht erneut anhand der Canvas-Segment-Kriterien bewertet.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Zeitstempel für Trigger {#timestamps-for-triggers}

Wenn Sie Zeitstempel mit einem [Datetime-Typ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties/) aus Events verwenden, die aktionsbasierte Canvases triggern und über [Context]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/) referenziert werden, werden Zeitstempel auf UTC normalisiert.

Angesichts dieses Verhaltens empfiehlt Braze dringend, einen Liquid-Zeitzonen-Filter wie im folgenden Beispiel zu verwenden, um sicherzustellen, dass Ihre Nachrichten mit Ihrer [bevorzugten Zeitzone]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters/#time-zone-filter) gesendet werden.

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

## Anwendungsfall {#use-case}

![Ein Aktionspfade-Schritt, gefolgt von einem Verzögerungs-Schritt und einem Nachrichten-Schritt für Nutzer:innen, die einen Artikel zu ihrer Wunschliste hinzugefügt haben, sowie ein Pfad für alle anderen.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Um die Unterschiede zwischen `context` und `event_properties` besser zu verstehen, betrachten wir folgendes Szenario: Nutzer:innen treten in einen aktionsbasierten Canvas ein, wenn sie das angepasste Event „Artikel zur Wunschliste hinzufügen“ ausführen.

Context wird im Schritt [Entry-Zeitplan]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#step-12-determine-your-canvas-entry-schedule) bei der Canvas-Erstellung konfiguriert und entspricht dem Zeitpunkt, an dem Nutzer:innen in einen Canvas eintreten. Context kann auch in jedem Nachrichten-Schritt referenziert werden.

In diesem Canvas haben wir eine Nutzer-Journey, die mit einem Aktionspfade-Schritt beginnt, um festzustellen, ob Nutzer:innen einen Artikel zu ihrer Wunschliste hinzugefügt haben. Wenn dies der Fall ist, erleben sie eine Verzögerung, bevor sie die Nachricht „Neuer Artikel auf Ihrer Wunschliste!“ vom Nachrichten-Schritt erhalten.

Der erste Nachrichten-Schritt in einer Nutzer-Journey hat Zugriff auf die angepassten `event_properties` aus Ihrem Aktionspfade-Schritt. In diesem Fall können wir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` in diesem Nachrichten-Schritt als Teil unseres Nachrichteninhalts einfügen. Wenn Nutzer:innen keinen Artikel zu ihrer Wunschliste hinzufügen, durchlaufen sie den Alle-anderen-Pfad, was bedeutet, dass die `event_properties` nicht referenziert werden können und einen Fehler für ungültige Einstellungen anzeigen.

Beachten Sie, dass Sie nur Zugriff auf `event_properties` haben, wenn Ihr Nachrichten-Schritt auf einen Nicht-Alle-anderen-Pfad in einem Aktionspfade-Schritt zurückverfolgt werden kann. Wenn der Nachrichten-Schritt mit einem Alle-anderen-Pfad verbunden ist, aber auf einen Aktionspfade-Schritt in der Nutzer-Journey zurückverfolgt werden kann, haben Sie ebenfalls weiterhin Zugriff auf `event_properties`. Weitere Informationen zu diesen Verhaltensweisen finden Sie unter [Nachrichten-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/).