---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Canvases
page_order: 7
page_type: reference
description: "Diese Seite enthält Schritte zur Fehlerbehebung für Canvases."
tool: Canvas
---

# Fehlerbehebung für Canvases

> Diese Seite hilft Ihnen bei der Fehlerbehebung von Problemen mit Ihren Canvases.

## Warum hat ein:e Nutzer:in einen getriggerten Canvas-Schritt nicht erhalten?

Bestätigen Sie zunächst, dass das angepasste Event an Braze übergeben wird. Gehen Sie zu **Analytics** > **Bericht zu angepassten Events**, und wählen Sie dann das entsprechende angepasste Event und den Zeitraum aus. Wenn das Event nicht angezeigt wird, bestätigen Sie, dass es korrekt eingerichtet ist und dass die Nutzer:innen die richtige Aktion ausgeführt haben.

Wenn das angepasste Event angezeigt wird, führen Sie die folgenden Schritte zur weiteren Fehlerbehebung durch:

- Überprüfen Sie den Profil-Download der Nutzer:innen, um zu bestätigen, dass sie das Event getriggert haben und wann dies geschah. Wenn das Event getriggert wurde, vergleichen Sie den Zeitstempel des Events mit dem Zeitpunkt, zu dem der Canvas live ging. Das Event wurde möglicherweise getriggert, bevor der Canvas live ging.
- Überprüfen Sie die Changelogs für den Canvas und alle Segmente, die beim Targeting verwendet werden, um festzustellen, ob die Nutzer:innen im Segment waren, als ihr angepasstes Event getriggert wurde. Wenn sie nicht im Segment waren, hätten sie den Canvas-Schritt nicht erhalten.
- Überprüfen Sie, ob die Nutzer:innen durch Segmentierung in eine Kontrollgruppe eingeteilt wurden und dadurch am Empfang des Canvas-Schritts gehindert wurden.
- Wenn es eine geplante Verzögerung gibt, prüfen Sie, ob das angepasste Event der Nutzer:innen vor der Verzögerung getriggert wurde. Wenn das Event vor der Verzögerung getriggert wurde, hätten sie den Canvas-Schritt nicht erhalten.

{% alert note %}
In-App-Nachrichten können nur durch Events getriggert werden, die über das SDK gesendet werden, nicht über die REST API.
{% endalert %}

## Warum sendet mein Canvas nicht wie erwartet?

Canvases sind leistungsstark und komplex, und wir wissen, dass Sie Zeit und Sorgfalt in ihre Erstellung investieren. Wenn Sie feststellen, dass Ihr Canvas nicht wie gewünscht sendet, empfehlen wir Ihnen, den Zeitplan, die Entry-Zielgruppe und die Eingangs-Einstellungen Ihres Canvas zu überprüfen und die Schritte zum [Erstellen eines Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) durchzugehen.

### Zeitplan

- Ist der Canvas [korrekt geplant]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types)?
- Haben Sie das richtige Datum und die richtige Uhrzeit ausgewählt?
- Haben bei der [aktionsbasierten Zustellung]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types) die Nutzer:innen die angegebenen Aktionen ausgeführt, seit Sie den Canvas gestartet haben?

### Eingangs-Einstellungen

Die [Eingangs-Einstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=basics#selecting-entry-controls) sind wichtig, um zu verstehen, wie Ihre Canvases senden. Prüfen Sie, ob Sie die Anzahl der Personen begrenzt haben, die potenziell in den Canvas eintreten können.

Nutzer:innen können einen Canvas auch verlassen, wenn sie nicht mehr berechtigt sind, Nachrichten zu empfangen. Wenn der Canvas beispielsweise nur Push-Benachrichtigungen enthält und ein:e Nutzer:in sich nach dem Empfang des ersten Schritts von Push abmeldet, würde diese:r Nutzer:in aus dem Canvas ausscheiden. Erwägen Sie die Verwendung [verschiedener Canvas-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/), um alternative Nutzer-Journeys hinzuzufügen.

### Segmentierung Ihrer Zielgruppe

Berücksichtigen Sie die folgenden Fragen für Ihre Zielgruppe:

- Haben Sie das richtige Segment ausgewählt?
- Wie ist das Segment eingerichtet?
- Haben Sie bestätigt, dass das Segment Nutzer:innen enthält?
- Haben Sie zusätzliche Filter hinzugefügt, die die Anzahl der Nutzer:innen begrenzen würden, die in den Canvas eintreten?
- Sind die Nutzer:innen berechtigt, den ersten Schritt Ihrer Varianten zu empfangen? Wenn beispielsweise der erste Schritt Ihres Canvas eine Push-Benachrichtigung ist, die Entry-Zielgruppe aber alle Push-deaktivierten Nutzer:innen umfasst, werden keine Nutzer:innen Nachrichten erhalten.

## Warum sind die Sendungen oder Zustellungen niedriger als die Größe meiner Zielgruppe?

Die Anzahl der gesendeten oder zugestellten Nachrichten weicht häufig von der geschätzten Zielgruppen- oder Empfänger:innen-Anzahl ab. Häufige Gründe sind:

- **Neubewertung der Zielgruppe:** Nutzer:innen können zwischen dem Eintritt in einen Schritt und dem Senden der Nachricht aus dem Segment fallen.
- **Kanalberechtigung:** Nutzer:innen haben möglicherweise keine E-Mail-Adressen, Push-Token oder den für diesen Kanal in diesem Schritt erforderlichen Abo-Status.
- **Kontrollgruppen:** Eine globale oder Canvas-Kontrollgruppe kann Nutzer:innen vom Messaging ausschließen.
- **Ruhezeiten, intelligentes Timing und Rate-Limits:** Diese Einstellungen können Sendungen verzögern oder unterdrücken.
- **In-App-Nachrichten-Schritte:** In-App-Nachrichten können null _Sendungen_ anzeigen, während Impressionen vorhanden sind. Dies ist erwartetes Verhalten, da die In-App-Zustellung anders funktioniert als Push-Benachrichtigungen oder E-Mail. Siehe [Warum kann ein Canvas null Sendungen anzeigen, obwohl Impressionen protokolliert werden?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged) in den Canvas-FAQ.

Für E-Mail und andere Kanäle gelten viele der gleichen Faktoren wie für Kampagnen. Eine detaillierte Liste finden Sie unter [Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size).

## Warum sind an einem Tag mit Zeitumstellung keine Nutzer:innen in meinen täglich geplanten Canvas eingetreten?

An Tagen mit Zeitumstellung (Sommer-/Winterzeit) können täglich geplante Canvases bis zu eine Stunde früher oder später als üblich ausgeführt werden. Wenn Ihre Eintrittskriterien auf angepassten Attributen oder Events mit Zeitstempeln basieren, die innerhalb einer Stunde der geplanten Eintrittszeit liegen, qualifizieren sich Nutzer:innen am Tag der Zeitumstellung möglicherweise noch nicht, da das Attribut oder Event noch nicht protokolliert wurde.

Angenommen, Nutzer:innen erhalten typischerweise ein Update eines angepassten Attributs um 15:00 Uhr in der Zeitzone Ihres Canvas, und Ihr Canvas läuft täglich um 15:30 Uhr in derselben Zeitzone. An einem Tag mit Vorstellung der Uhr (Sommerzeit) kann der Canvas die Nutzer:innen bis zu eine Stunde früher als üblich relativ zu diesem Attribut-Update auswerten – bevor das Attribut protokolliert wurde. Wenn die Wiedereintritts-Berechtigung deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen eingetreten sind, nicht erneut eintreten, was zu null Eintritten für diesen Tag führt.

Um dies zu vermeiden, stellen Sie sicher, dass Ihre Updates für angepasste Attribute oder Events mehr als eine Stunde vor der geplanten Eintrittszeit des Canvas erfolgen.

## Warum hat sich meine Zielgruppe nicht gleichmäßig zwischen Kontrollgruppe und Variantengruppe aufgeteilt?

Beim Erstellen Ihres Canvas haben Sie möglicherweise erwartet, dass sich Ihre Zielgruppe gleichmäßig zwischen Ihrer Kontrollgruppe und Ihrer Variantengruppe aufteilt, wie im folgenden [Anwendungsfall](#use-case). Lassen Sie uns besprechen, warum das so ist und wie Sie es beheben können!

Die Gruppe, der ein:e Nutzer:in beitritt, hängt von den Einstellungen ab. Dies kann entweder die Kontrollgruppe oder die Variantengruppe sein. Ein:e Nutzer:in tritt in einen Canvas ein, wenn alle Ihre im [Eingangs-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule) definierten Kriterien erfüllt sind. Beim Einrichten Ihres Canvas legen Sie fest, welcher Prozentsatz der Nutzer:innen in jede Variante und die Kontrollgruppe eintreten soll.

Wenn Ihre Kontrollgruppe im Vergleich zu Ihrer Variantengruppe groß ist (und dies nicht Ihre Absicht ist), empfehlen wir Folgendes:
1. Setzen Sie Ihren Entry-Zielgruppen-Filter auf **is Foreground Push Enabled**.
2. Setzen Sie Ihren Entry-Zielgruppen-Filter für **Push Subscription Status**, **Email Subscription Status** oder beides auf **Opted In** oder **Subscribed**.

Wenn Sie einen Canvas mit einer Kontrollgruppe erstellen, bestätigen Sie, dass alle Nutzer:innen in der Entry-Zielgruppe in der Lage sind, Nachrichten innerhalb des Canvas zu empfangen (z. B. wenn der Canvas Push- und E-Mail-Nachrichten enthält).

### Anwendungsfall

Stellen Sie sich folgendes Szenario vor:
- Ein Canvas hat eine einzelne Variante und eine Kontrollgruppe.
- Der erste Schritt der Variante ist eine Push-Benachrichtigung.
- 90 % der Nutzer:innen wurden ausgewählt, um in die Variante einzutreten, und 10 %, um in die Kontrollgruppe einzutreten.

![Canvas-Beispiel mit 90 % Variante und 10 % Kontrollgruppe.]({% image_buster /assets/img_archive/trouble15.png %})

In diesem Szenario treten 90 % der Nutzer:innen, die in den Canvas eintreten, in die Variante ein.

Wenn wir uns die aktiven Nutzer:innen ansehen, können wir sehen, dass das Segment zwar 29,8k Nutzer:innen enthält, aber nur 64 % von ihnen Push-aktiviert sind:

![Segment mit dem Filter „Push Enabled" auf „true" gesetzt und geschätzten 29,8k Nutzer:innen.]({% image_buster /assets/img_archive/trouble16.png %})

Das bedeutet, dass obwohl wir festgelegt haben, dass 90 % der Nutzer:innen in die Variante eintreten sollen, nicht alle dieser Nutzer:innen tatsächlich in der Lage sind, eine Push-Benachrichtigung zu empfangen. Diese Nutzer:innen, die keine Push-Benachrichtigung empfangen können, treten trotzdem in die Variante ein.