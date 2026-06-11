---
nav_title: Fehlerbehebung
article_title: Fehlerbehebung für Canvases
page_order: 7
page_type: reference
description: "Diese Seite enthält Schritte zur Fehlerbehebung für Canvases."
tool: Canvas
---

# Fehlerbehebung für Canvases {#troubleshoot-canvases}

> Diese Seite hilft Ihnen bei der Fehlerbehebung von Problemen mit Ihren Canvases.

## Fehler „Zu viele Canvas-Branches“ {#too-many-canvas-branches-error}

Wenn beim Starten eines geplanten Canvas der Fehler „Zu viele Canvas-Branches“ angezeigt wird, kann die Kombination aus Schritt-Verzweigungen und der Größe der Entry-Zielgruppe zu Performance-Problemen im Braze-Cluster führen, die das Senden von Nachrichten verhindern.

Braze zeigt diese Meldung an, wenn Sie einen Canvas mit geplantem Eintritt starten – nicht beim Speichern eines Entwurfs. Um das Problem zu beheben, versuchen Sie Folgendes:

- Reduzieren Sie die Schritt-Verzweigungen im Canvas.
- Reduzieren Sie die Größe der Entry-Zielgruppe.
- Verwenden Sie [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/), um Verzweigungen zu konsolidieren, anstatt viele parallele Pfade zu verwenden.
- Wenn Ihr Canvas den ursprünglichen Editor verwendet, [klonen Sie ihn zu Canvas Flow]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/) und bauen Sie ihn mit Canvas-Komponenten neu auf.

Wenn Sie den Canvas dennoch ohne Änderungen starten müssen und nicht zu Canvas Flow wechseln können, kontaktieren Sie den [Support]({{site.baseurl}}/support_contact/).

## Warum hat ein:e Nutzer:in einen getriggerten Canvas-Schritt nicht erhalten? {#why-did-a-user-not-receive-a-triggered-canvas-step}

Bestätigen Sie zunächst, dass das angepasste Event an Braze übergeben wird. Gehen Sie zu **Analytics** > **Bericht zu angepassten Events**, und wählen Sie dann das entsprechende angepasste Event und den Zeitraum aus. Wenn das Event nicht angezeigt wird, bestätigen Sie, dass es korrekt eingerichtet ist und dass die Nutzer:innen die richtige Aktion ausgeführt haben.

Wenn das angepasste Event angezeigt wird, führen Sie die folgenden Schritte zur weiteren Fehlerbehebung durch:

- Überprüfen Sie den Profil-Download der Nutzer:innen, um zu bestätigen, dass sie das Event getriggert haben und wann dies geschah. Wenn das Event getriggert wurde, vergleichen Sie den Zeitstempel des Events mit dem Zeitpunkt, zu dem der Canvas live ging. Das Event wurde möglicherweise getriggert, bevor der Canvas live ging.
- Überprüfen Sie die Changelogs für den Canvas und alle Segmente, die beim Targeting verwendet werden, um festzustellen, ob die Nutzer:innen im Segment waren, als ihr angepasstes Event getriggert wurde. Wenn sie nicht im Segment waren, hätten sie den Canvas-Schritt nicht erhalten.
- Überprüfen Sie, ob die Nutzer:innen durch Segmentierung in eine Kontrollgruppe eingeteilt wurden und dadurch am Empfang des Canvas-Schritts gehindert wurden.
- Wenn es eine geplante Verzögerung gibt, prüfen Sie, ob das angepasste Event der Nutzer:innen vor der Verzögerung getriggert wurde. Wenn das Event vor der Verzögerung getriggert wurde, hätten sie den Canvas-Schritt nicht erhalten.

{% alert note %}
In-App Messages können nur durch Events getriggert werden, die über das SDK gesendet werden, nicht über die REST API.
{% endalert %}

## Warum sendet mein Canvas nicht wie erwartet? {#why-isnt-my-canvas-sending-as-expected}

Canvases sind leistungsstark und komplex, und wir wissen, dass Sie Zeit und Sorgfalt in ihre Erstellung investieren. Wenn Sie feststellen, dass Ihr Canvas nicht wie gewünscht sendet, empfehlen wir Ihnen, den Zeitplan, die Entry-Zielgruppe und die Eingangs-Einstellungen Ihres Canvas zu überprüfen und die Schritte zum [Erstellen eines Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/) durchzugehen.

### Zeitplan {#schedule}

- Ist der Canvas [korrekt geplant]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types)?
- Haben Sie das richtige Datum und die richtige Uhrzeit ausgewählt?
- Haben bei der [aktionsbasierten Zustellung]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types) die Nutzer:innen die angegebenen Aktionen ausgeführt, seit Sie den Canvas gestartet haben?

### Eingangs-Einstellungen {#entry-settings}

Die [Eingangs-Einstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=basics#selecting-entry-controls) sind wichtig, um zu verstehen, wie Ihre Canvases senden. Prüfen Sie, ob Sie die Anzahl der Personen begrenzt haben, die potenziell in den Canvas eintreten können.

Nutzer:innen können einen Canvas auch verlassen, wenn sie nicht mehr berechtigt sind, Nachrichten zu empfangen. Wenn der Canvas beispielsweise nur Push-Benachrichtigungen enthält und ein:e Nutzer:in sich nach dem Empfang des ersten Schritts von Push abmeldet, würde diese:r Nutzer:in aus dem Canvas ausscheiden. Erwägen Sie die Verwendung [verschiedener Canvas-Schritte]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about/), um alternative Nutzer-Journeys hinzuzufügen.

### Segmentierung Ihrer Zielgruppe {#segmenting-your-audience}

Berücksichtigen Sie die folgenden Fragen für Ihre Zielgruppe:

- Haben Sie das richtige Segment ausgewählt?
- Wie ist das Segment eingerichtet?
- Haben Sie bestätigt, dass das Segment Nutzer:innen enthält?
- Haben Sie zusätzliche Filter hinzugefügt, die die Anzahl der Nutzer:innen begrenzen würden, die in den Canvas eintreten?
- Sind die Nutzer:innen berechtigt, den ersten Schritt Ihrer Varianten zu empfangen? Wenn beispielsweise der erste Schritt Ihres Canvas eine Push-Benachrichtigung ist, die Entry-Zielgruppe aber alle Push-deaktivierten Nutzer:innen umfasst, werden keine Nutzer:innen Nachrichten erhalten.

## Warum sind die Sendungen oder Zustellungen niedriger als die Größe meiner Zielgruppe? {#why-are-sends-or-deliveries-lower-than-my-target-audience-size}

Die Anzahl der gesendeten oder zugestellten Nachrichten weicht häufig von der geschätzten Zielgruppen- oder Empfänger:innen-Anzahl ab. Häufige Gründe sind:

- **Neubewertung der Zielgruppe:** Nutzer:innen können zwischen dem Eintritt in einen Schritt und dem Senden der Nachricht aus dem Segment fallen.
- **Kanalberechtigung:** Nutzer:innen haben möglicherweise keine E-Mail-Adressen, Push-Token oder den für diesen Kanal in diesem Schritt erforderlichen Abo-Status.
- **Kontrollgruppen:** Eine globale oder Canvas-Kontrollgruppe kann Nutzer:innen vom Messaging ausschließen.
- **Ruhezeiten, intelligentes Timing und Rate-Limits:** Diese Einstellungen können Sendungen verzögern oder unterdrücken.
- **In-App-Messages-Schritte:** In-App Messages können null _Sendungen_ anzeigen, während Impressionen vorhanden sind. Dies ist erwartetes Verhalten, da die In-App-Zustellung anders funktioniert als Push-Benachrichtigungen oder E-Mail. Siehe [Warum kann ein Canvas null Sendungen anzeigen, obwohl Impressionen protokolliert werden?]({{site.baseurl}}/user_guide/messaging/canvas/faqs/#why-may-a-canvas-show-zero-sends-even-though-impressions-are-logged) in den Canvas-FAQ.

Für E-Mail und andere Kanäle gelten viele der gleichen Faktoren wie für Campaigns. Eine detaillierte Liste finden Sie unter [Warum sind die Sendungen niedriger als die geschätzte Zielgruppengröße?]({{site.baseurl}}/user_guide/messaging/campaigns/faq/#why-are-sends-lower-than-the-estimated-audience-size).

## Warum sind an einem Tag mit Zeitumstellung keine Nutzer:innen in meinen täglich geplanten Canvas eingetreten? {#why-did-no-users-enter-my-daily-scheduled-canvas-on-daylight-saving-time-day}

An Tagen mit Zeitumstellung (Sommer-/Winterzeit) können täglich geplante Canvases bis zu eine Stunde früher oder später als üblich ausgeführt werden. Wenn Ihre Eintrittskriterien auf angepassten Attributen oder Events mit Zeitstempeln basieren, die innerhalb einer Stunde der geplanten Eintrittszeit liegen, qualifizieren sich Nutzer:innen am Tag der Zeitumstellung möglicherweise noch nicht, da das Attribut oder Event noch nicht protokolliert wurde.

Angenommen, Nutzer:innen erhalten typischerweise ein Update eines angepassten Attributs um 15:00 Uhr in der Zeitzone Ihres Canvas, und Ihr Canvas läuft täglich um 15:30 Uhr in derselben Zeitzone. An einem Tag mit Vorstellung der Uhr (Sommerzeit) kann der Canvas die Nutzer:innen bis zu eine Stunde früher als üblich relativ zu diesem Attribut-Update auswerten – bevor das Attribut protokolliert wurde. Wenn die Wiedereintritts-Berechtigung deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen eingetreten sind, nicht erneut eintreten, was zu null Eintritten für diesen Tag führt.

Um dies zu vermeiden, stellen Sie sicher, dass Ihre Updates für angepasste Attribute oder Events mehr als eine Stunde vor der geplanten Eintrittszeit des Canvas erfolgen.

## Warum hat sich meine Zielgruppe nicht gleichmäßig zwischen Kontrollgruppe und Variantengruppe aufgeteilt? {#why-didnt-my-audience-split-evenly-between-the-control-group-and-variant-group}

Beim Erstellen Ihres Canvas haben Sie möglicherweise erwartet, dass sich Ihre Zielgruppe gleichmäßig zwischen Ihrer Kontrollgruppe und Ihrer Variantengruppe aufteilt, wie im folgenden [Anwendungsfall](#use-case). Lassen Sie uns besprechen, warum das so ist und wie Sie es beheben können!

Die Gruppe, der ein:e Nutzer:in beitritt, hängt von den Einstellungen ab. Dies kann entweder die Kontrollgruppe oder die Variantengruppe sein. Ein:e Nutzer:in tritt in einen Canvas ein, wenn alle Ihre im [Eingangs-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule) definierten Kriterien erfüllt sind. Beim Einrichten Ihres Canvas legen Sie fest, welcher Prozentsatz der Nutzer:innen in jede Variante und die Kontrollgruppe eintreten soll.

Wenn Ihre Kontrollgruppe im Vergleich zu Ihrer Variantengruppe groß ist (und dies nicht Ihre Absicht ist), empfehlen wir Folgendes:
1. Setzen Sie Ihren Entry-Zielgruppen-Filter auf **is Foreground Push Enabled**.
2. Setzen Sie Ihren Entry-Zielgruppen-Filter für **Push Subscription Status**, **Email Subscription Status** oder beides auf **Opted In** oder **Subscribed**.

Wenn Sie einen Canvas mit einer Kontrollgruppe erstellen, bestätigen Sie, dass alle Nutzer:innen in der Entry-Zielgruppe in der Lage sind, Nachrichten innerhalb des Canvas zu empfangen (z. B. wenn der Canvas Push- und E-Mail-Nachrichten enthält).

### Anwendungsfall {#use-case}

Stellen Sie sich folgendes Szenario vor:
- Ein Canvas hat eine einzelne Variante und eine Kontrollgruppe.
- Der erste Schritt der Variante ist eine Push-Benachrichtigung.
- 90 % der Nutzer:innen wurden ausgewählt, um in die Variante einzutreten, und 10 %, um in die Kontrollgruppe einzutreten.

![Canvas-Beispiel mit 90 % Variante und 10 % Kontrollgruppe.]({% image_buster /assets/img_archive/trouble15.png %})

In diesem Szenario treten 90 % der Nutzer:innen, die in den Canvas eintreten, in die Variante ein.

Wenn wir uns die aktiven Nutzer:innen ansehen, können wir sehen, dass das Segment zwar 29,8k Nutzer:innen enthält, aber nur 64 % von ihnen Push-aktiviert sind:

![Segment mit dem Filter „Push Enabled“ auf „true“ gesetzt und geschätzten 29,8k Nutzer:innen.]({% image_buster /assets/img_archive/trouble16.png %})

Das bedeutet, dass obwohl wir festgelegt haben, dass 90 % der Nutzer:innen in die Variante eintreten sollen, nicht alle dieser Nutzer:innen tatsächlich in der Lage sind, eine Push-Benachrichtigung zu empfangen. Diese Nutzer:innen, die keine Push-Benachrichtigung empfangen können, treten trotzdem in die Variante ein.

## Warum friert der Canvas-Editor ein oder lädt nicht? {#why-is-the-canvas-editor-freezing-or-not-loading}

Wenn Sie Änderungen an großen oder komplexen Canvases mit vielen Branches oder Varianten, vielen Schritten oder sehr breiten Flows vornehmen, kann es vorkommen, dass der Editor nicht lädt oder einfriert. In diesem Fall empfehlen wir Folgendes:

- Leeren Sie den Browser-Cache und die Cookies und laden Sie die Seite neu. Wenn Sie Unternehmens-Werbeblocker oder Browser-Erweiterungen verwenden, können diese die Braze-Plattform beeinträchtigen.
- Verwenden Sie die Canvas-Zoom-Steuerung, um die Ansicht auf 25 % oder 10 % zu reduzieren. Dadurch wird die Menge an UI verringert, die der Browser auf einmal rendern muss.
- Versuchen Sie es mit einem anderen Webbrowser.