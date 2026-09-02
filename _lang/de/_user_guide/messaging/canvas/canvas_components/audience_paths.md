---
nav_title: Zielgruppenpfade
article_title: Zielgruppenpfade
alias: /audience_paths/
page_order: 3
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Zielgruppenpfade in Ihrem Canvas verwenden, um Nutzer:innen intuitiv in großem Umfang zu filtern und zu segmentieren, indem jede:r Nutzer:in den ersten passenden Branch durchläuft."
tool: Canvas

---

# Zielgruppenpfade {#audience-paths}

> Mit Canvas-Zielgruppenpfaden können Sie Nutzer:innen intuitiv in großem Umfang filtern und segmentieren, indem jede:r Nutzer:in den ersten Pfad durchläuft, dessen Kriterien erfüllt werden.

Diese Canvas-Komponente ersetzt die Notwendigkeit, übermäßig viele zielgruppenbasierte vollständige Schritte zu erstellen, und ermöglicht es Ihnen, bis zu acht vollständige Komponenten in einer einzigen zusammenzufassen. Das vereinfacht das Targeting und befreit Ihre Canvase von unnötiger Unübersichtlichkeit und Komplexität.

## So funktioniert es {#how-it-works}

![Ein Zielgruppenpfad mit zwei Gruppen: engagierte Nutzer:innen und alle anderen.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Nutzer:innen werden durch den ersten Branch weitergeleitet, dessen Kriterien sie erfüllen – setzen Sie daher den wichtigsten Pfad an die erste Stelle. Dies reduziert Unklarheiten darüber, wohin Nutzer:innen geleitet werden und welche Nachrichten sie erhalten. Beachten Sie, dass diese Reihenfolge [nach dem Start nicht mehr bearbeitet werden kann]({{site.baseurl}}/post-launch_edits).

Mit Zielgruppenpfaden können Sie:

- Nutzer:innen basierend auf Zielgruppenkriterien auf verschiedene Canvas-Pfade leiten.
- Ihre wichtigsten Zielgruppen an die erste Stelle setzen – Nutzer:innen nehmen den ersten Pfad, für den sie sich qualifizieren.
- Nutzer:innen in großem Umfang präzise ansprechen.
  - Sie können pro Zielgruppenpfade-Schritt bis zu acht Zielgruppen erstellen (zwei standardmäßige und sechs zusätzliche Gruppen), aber Sie können mehrere Zielgruppenpfade-Schritte verbinden, um Ihre Nutzer:innen weiter aufzuteilen.

Innerhalb eines einzelnen Zielgruppenpfade-Schritts werden Nutzer:innen der Reihe nach anhand der Zielgruppen ausgewertet und nehmen den ersten Pfad, für den sie sich qualifizieren. Wenn Sie mehrere Zielgruppenpfade-Schritte in einem Canvas verbinden, werden Nutzer:innen jedes Mal erneut ausgewertet, wenn sie einen neuen Zielgruppenpfade-Schritt erreichen.

### Wie Nutzer:innen ausgewertet werden {#how-users-are-evaluated}

![Canvas mit einer 24-Stunden-Verzögerung nach einem Nachrichten-Schritt, gefolgt von einem Zielgruppenpfad.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Nutzer:innen werden anhand von Filtern und Segment-Zugehörigkeit **in dem Moment ausgewertet, in dem sie den Zielgruppenpfad-Schritt erreichen** – nicht beim Eintritt in den Canvas. Nach der Auswertung werden sie sofort zum passenden Pfad weitergeleitet. Wenn Nutzer:innen einer Zielgruppe zugeordnet wurden, bleiben sie in dieser Gruppe, auch wenn sich ihr Kundenprofil or Nutzerprofil danach ändert.

<div style="clear: both;"></div>

{% alert important %}
Zielgruppenpfade werten basierend auf den aktuellen Attributen, Filtern und der Segment-Zugehörigkeit zum Zeitpunkt der Auswertung aus. Sie werten nicht basierend auf dem spezifischen Event aus, das den Canvas-Eintritt ausgelöst hat. Um Nutzer:innen basierend auf einer durchgeführten Aktion (z. B. einem angepassten Event) weiterzuleiten, verwenden Sie stattdessen [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths).
{% endalert %}

Nutzer:innen werden nicht erneut anhand ihrer Zielgruppe ausgewertet, nachdem sie einen Pfad eingeschlagen haben. Wenn die nachfolgende Nachricht durch einen Verzögerungsschritt, Ruhezeiten, intelligentes Timing, Rate-Limiting oder Zustellung nach Ortszeit verzögert wird, kann sich das Kundenprofil or Nutzerprofil ändern, bevor die Nachricht gesendet wird.

Um sicherzustellen, dass Nutzer:innen vor dem Senden des Nachrichten-Schritts weiterhin die Segment- und Filterkriterien erfüllen, aktivieren Sie **Zielgruppe beim Nachrichtenversand validieren** in den [Zustellungsvalidierungen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) des Nachrichten-Schritts. Zustellungsvalidierungen prüfen nur die Segments und Filter, die Sie zu diesem Nachrichten-Schritt hinzufügen – sie verwenden nicht die Kriterien Ihres Zielgruppenpfads wieder. Bei In-App-Nachrichten werden Zustellungsvalidierungen geprüft, wenn Nutzer:innen den Nachrichten-Schritt erreichen, nicht wenn die Nachricht angezeigt wird.

### Zeit für die Auswertung der Nutzer:innen einplanen {#allowing-time-for-user-evaluations}

Da die Auswertung sofort erfolgt, ist es wichtig, vor dem Zielgruppenpfad eine Verzögerung einzufügen, wenn die Pfadkriterien von einer Interaktion der Nutzer:innen mit einem vorherigen Schritt abhängen.

Wenn Nutzer:innen beispielsweise Nachricht A erhalten und der nächste Schritt ein Zielgruppenpfad ist, der auswertet, ob sie mit dieser Nachricht interagiert haben, werden alle Nutzer:innen zum Schritt für diejenigen weitergeleitet, die nicht mit der Nachricht interagiert haben. Das liegt daran, dass die Nutzer:innen sofort zum Zielgruppenpfad-Schritt weitergeleitet wurden, ohne Zeit für eine Interaktion mit der Nachricht zu haben. Mit anderen Worten: Nutzer:innen werden fast unmittelbar nach dem Senden der Nachricht auf eine Interaktion mit der Nachricht ausgewertet.

Um Nutzer:innen Zeit zu geben, mit einer gesendeten Nachricht zu interagieren, fügen Sie zwischen dem Nachrichten-Schritt und dem Zielgruppenpfad eine Verzögerung ein. Beispielsweise gibt eine 24-Stunden-Verzögerung den Nutzer:innen 24 Stunden nach dem Versand der Nachricht Zeit, mit Nachricht A zu interagieren, bevor die Auswertung stattfindet.

## Einen Zielgruppenpfad erstellen {#creating-an-audience-path}

Um einen Zielgruppenpfade-Schritt hinzuzufügen, gehen Sie wie folgt vor:

1. Fügen Sie Ihrem Canvas einen Schritt hinzu.
2. Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie <i class="fas fa-plus-circle"></i> **Hinzufügen** am unteren Rand eines Schritts und wählen Sie **Zielgruppenpfade**.

Die Standard-Zielgruppenpfade-Komponente enthält zwei Standard-Zielgruppen: **Gruppe 1** und **Alle anderen**. Die Gruppe **Alle anderen** umfasst alle Nutzer:innen, die keiner definierten Zielgruppe zugeordnet sind. Diese Gruppe steht immer an letzter Stelle in der Reihenfolge.

### Zielgruppen definieren {#defining-audience-groups}

Der folgende Screenshot zeigt das Layout eines erweiterten Zielgruppenpfade-Schritts. Hier können Sie bis zu acht Zielgruppen definieren (eine voreingestellte und sieben anpassbare). Um eine Zielgruppe zu definieren, wählen Sie den Gruppennamen im Zielgruppenpfade-Editor aus. Sie können Ihre Zielgruppe umbenennen, die Filter und Segmente auswählen, die für Ihre Gruppe gelten, und Gruppen hinzufügen oder löschen. Wenn Sie beispielsweise Onboarding-Nachrichten an eine bestimmte Nutzer:innengruppe senden möchten, könnten Sie Retargeting-Filter wie „Hat E-Mail angeklickt“ und „Hat In-App-Nachricht angeklickt“ auswählen.

![Ein erweiterter Zielgruppenpfad mit Gruppen für „Liebt asiatische Küche“, „Liebt lateinamerikanische Küche“, „Liebt europäische Küche“ und „Alle anderen“.]({% image_buster /assets/img/audience_path/audience_path3.png %})

Nachdem der Zielgruppenpfade-Schritt abgeschlossen ist, hat jede Zielgruppe einen separaten Branch. Sie können Zielgruppenpfade weiterhin verwenden, um Ihre Zielgruppe weiter zu filtern, oder Ihre Canvas-Journey mit den Standard-Canvas-Schritten fortsetzen.

![Zwei Zielgruppenpfade mit verschiedenen Gruppen basierend auf Engagement.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

#### Vergleichsfilter mit Kontextvariablen verwenden {#using-comparison-filters-with-context-variables}

Wenn Sie nach einer Kontextvariablen aufteilen, die ein Datum enthält, lesen Sie [Jahrestag- und Zeitfilter für Datums-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#day-of-year-and-time-filters-for-date-context-variables), um den richtigen Vergleichstyp auszuwählen.

### Zielgruppen testen {#testing-audience-groups}

Nachdem Sie Segmente und Filter zu Ihren Zielgruppen hinzugefügt haben, können Sie testen, ob Ihre Zielgruppen wie erwartet eingerichtet sind, indem Sie [eine:n Nutzer:in nachschlagen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), um zu bestätigen, dass sie den Zielgruppenkriterien entsprechen.

![Der Bereich „Nutzer:innensuche“.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Zielgruppenpfade verwenden {#using-audience-paths}

Die wahre Stärke der Zielgruppenpfade liegt darin, die Pfade, die Ihnen am wichtigsten sind, an die **erste** Stelle zu setzen. Obwohl dieses Feature nicht zwingend strategisch eingesetzt werden muss, können einige Marketer es nutzen, um bestimmte Produkte wie Sonderangebote oder limitierte Editionen gezielt an Nutzer:innen auszuspielen.

Indem Sie diese Segments zuerst in der Liste platzieren, können Sie Nutzer:innen ansprechen, die bestimmten Filtern und Segments entsprechen, und gleichzeitig Nutzer:innen erreichen, die diese spezifischen Kriterien möglicherweise nicht erfüllen – und das alles in einem einzigen Canvas-Schritt.

![Ein Zielgruppenpfad mit Gruppen für „Mag Big Brand Schuhe“, „Mag Big Brand“ und „Alle anderen“.]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Angenommen, Sie möchten einer Gruppe von Nutzer:innen Werbung für neue Produkte senden. Dann würden Sie zuerst die Filter, die sich auf diese Produkte beziehen, im Zielgruppenpfad **an die erste Stelle** setzen. Wenn Sie eine Marketing-Campaign für das Unternehmen „Big Brand“ erstellen und eine neue Einzelhandelsmarke gerade erschienen ist, könnten Sie Filter wie „Mag Big Brand Schuhe“ oder „Mag Big Brand Taschen“ auswählen und basierend auf der gefilterten Gruppe unterschiedliche E-Mail-Nachrichten senden.

Wenn Nutzer:innen diese Zielgruppenpfade-Komponente betreten, werden sie zuerst für Zielgruppe 1 „Mag Big Brand Schuhe“ – den ersten Pfad in der Liste – ausgewertet. Falls zutreffend, fahren sie mit der nächsten in Ihrem Canvas definierten Komponente fort. Falls sie „Big Brand Schuhe“ nicht mögen, werden sie anschließend für die nächste Zielgruppe ausgewertet, Zielgruppe 2 „Mag Big Brand Taschen“, und fahren mit dem nächsten Schritt fort, wenn die Kriterien erfüllt sind. Nutzer:innen, die in keine der vorherigen Gruppen fallen, landen schließlich in der Gruppe „Alle anderen“ und fahren ebenfalls mit dem nächsten Canvas-Schritt fort, den Sie für diesen Pfad definiert haben.

Sie können die Performance dieses Schritts auch mithilfe der [Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization) einsehen.

### Zielgruppenpfade mit zufälligen Bucket-Nummern segmentieren {#segmenting-audience-paths-with-random-bucket-numbers}

Wenn Ihr Canvas ein [Rate-Limit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) verwendet (z. B. eine Begrenzung der Gesamtzahl der Nutzer:innen, die den Canvas erhalten), empfiehlt Braze, Ihre Zielgruppenpfade nicht mit zufälligen Bucket-Nummern zu segmentieren.

Eine [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) ist ein Nutzerattribut, das verwendet werden kann, um gleichmäßig verteilte Segments zufälliger Nutzer:innen zu erstellen. Braze verwendet die zufällige Bucket-Nummer, um Nutzer:innen während der Segmentierungsphase beim Canvas-Entry zu gruppieren, und jede Gruppe wird separat verarbeitet. Je nachdem, welche Gruppen zuerst verarbeitet werden, können einige Nutzer:innen beim Entry aufgrund des Rate-Limits begrenzt werden, was zu einer ungleichmäßigen Verteilung der Nutzer:innen führen kann, wenn sie den Zielgruppenpfade-Schritt erreichen.

Versuchen Sie in diesem Szenario stattdessen, [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) zu verwenden.

### Intelligenter Kanal-Filter mit Zielgruppenpfaden verwenden {#using-intelligent-channel-filter-with-audience-paths}

Durch die Kombination von Zielgruppenpfade-Schritten und intelligenten Kanal-Filtern können Sie Ihr Messaging-Erlebnis auf die Präferenzen und Verhaltensweisen jeder einzelnen Nutzer:in zuschneiden. Auf diese Weise erhalten Ihre Nutzer:innen die relevantesten Nachrichten über die passenden Kanäle.

In einem Zielgruppenpfade-Schritt können Sie beispielsweise drei Zielgruppen erstellen: E-Mail, Mobile Push und Alle anderen. Fügen Sie für die E-Mail-Zielgruppe den Filter `Intelligent Channel is Email` hinzu. Fügen Sie für die Mobile Push-Zielgruppe den Filter `Intelligent Channel is Mobile Push` hinzu. Anschließend können Sie für jeden der Zielgruppenpfade einen Nachrichtenschritt hinzufügen, um personalisierte und relevante Nachrichten zuzustellen.

{% alert tip %}
Schauen Sie sich unsere [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) an, um Beispiele zu erhalten, wie Sie diese vorgefertigten Templates zu Ihrem Vorteil anpassen können.
{% endalert %}