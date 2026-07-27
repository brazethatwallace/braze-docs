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

Diese Canvas-Komponente ersetzt die Notwendigkeit, übermäßig viele zielgruppenbasierte vollständige Schritte zu erstellen, und ermöglicht es Ihnen, bis zu acht vollständige Komponenten in einer einzigen zusammenzufassen. Das vereinfacht das Targeting und befreit Ihre Canvases von unnötiger Unübersichtlichkeit und Komplexität.

## So funktioniert es {#how-it-works}

![Ein Zielgruppenpfad mit zwei Gruppen: engagierte Nutzer:innen und alle anderen.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Nutzer:innen werden in den ersten Branch weitergeleitet, dessen Kriterien sie erfüllen – platzieren Sie daher den wichtigsten Pfad an erster Stelle. Das reduziert Unklarheiten darüber, wohin Nutzer:innen geleitet werden und welche Nachrichten sie erhalten. Beachten Sie, dass diese Reihenfolge [nach dem Start nicht mehr bearbeitet werden kann]({{site.baseurl}}/post-launch_edits).

Mit Zielgruppenpfaden können Sie:

- Nutzer:innen basierend auf Zielgruppenkriterien auf verschiedene Canvas-Pfade leiten.
- Ihre wichtigsten Zielgruppen an die erste Stelle setzen – Nutzer:innen nehmen den ersten Pfad, für den sie sich qualifizieren.
- Nutzer:innen in großem Umfang präzise ansprechen.
  - Sie können pro Zielgruppenpfade-Schritt bis zu acht Zielgruppen erstellen (zwei Standard- und sechs zusätzliche Gruppen), aber Sie können auch mehrere Zielgruppenpfade-Schritte verbinden, um Ihre Nutzer:innen weiter zu sortieren.

Innerhalb eines einzelnen Zielgruppenpfade-Schritts werden Nutzer:innen der Reihe nach anhand der Zielgruppen ausgewertet und nehmen den ersten Pfad, für den sie sich qualifizieren. Wenn Sie mehrere Zielgruppenpfade-Schritte in einem Canvas verbinden, werden Nutzer:innen jedes Mal erneut ausgewertet, wenn sie einen neuen Zielgruppenpfade-Schritt erreichen.

### Wie Nutzer:innen ausgewertet werden {#how-users-are-evaluated}

![Canvas mit einer 24-Stunden-Verzögerung nach einem Nachrichten-Schritt, gefolgt von einem Zielgruppenpfad.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Nutzer:innen werden anhand von Filtern und Segment-Zugehörigkeit **in dem Moment ausgewertet, in dem sie den Zielgruppenpfad-Schritt erreichen** – nicht beim Eintritt in den Canvas. Nach der Auswertung werden sie sofort zum passenden Pfad weitergeleitet. Wenn Nutzer:innen einer Zielgruppe zugeordnet werden, bleiben sie in dieser Gruppe, auch wenn sich ihr Nutzerprofil danach ändert.

<div style="clear: both;"></div>

{% alert important %}
Zielgruppenpfade werten basierend auf den aktuellen Attributen, Filtern und der Segment-Zugehörigkeit der Nutzer:innen zum Zeitpunkt der Auswertung aus. Sie werten nicht basierend auf dem spezifischen Event aus, das den Canvas-Eintritt ausgelöst hat. Um Nutzer:innen basierend auf einer Aktion weiterzuleiten, die sie ausführen (z. B. ein angepasstes Event), verwenden Sie stattdessen [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths).
{% endalert %}

### Zeit für die Auswertung von Nutzer:innen einplanen {#allowing-time-for-user-evaluations}

Da die Auswertung sofort erfolgt, ist es wichtig, vor dem Zielgruppenpfad eine Verzögerung einzufügen, wenn die Pfadkriterien von einer Interaktion der Nutzer:innen mit einem vorherigen Schritt abhängen.

Wenn Nutzer:innen beispielsweise Nachricht A erhalten und der nächste Schritt ein Zielgruppenpfad ist, der auswertet, ob sie mit dieser Nachricht interagiert haben, werden alle Nutzer:innen in den Schritt für diejenigen weitergeleitet, die nicht mit der Nachricht interagiert haben. Das liegt daran, dass die Nutzer:innen sofort zum Zielgruppenpfad-Schritt weitergeleitet wurden, ohne Zeit für eine Interaktion mit der Nachricht zu haben. Anders ausgedrückt: Nutzer:innen werden fast unmittelbar nach dem Versand der Nachricht auf eine Interaktion mit dieser ausgewertet.

Um Nutzer:innen Zeit für die Interaktion mit einer gesendeten Nachricht zu geben, fügen Sie eine Verzögerung zwischen dem Nachrichten-Schritt und dem Zielgruppenpfad ein. Beispielsweise gibt eine 24-Stunden-Verzögerung den Nutzer:innen 24 Stunden nach dem Versand der Nachricht Zeit, mit Nachricht A zu interagieren, bevor die Auswertung erfolgt.

## Erstellen eines Zielgruppenpfads {#creating-an-audience-path}

Um einen Zielgruppenpfade-Schritt hinzuzufügen, gehen Sie wie folgt vor:

1. Fügen Sie Ihrem Canvas einen Schritt hinzu.
2. Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie <i class="fas fa-plus-circle"></i> **Hinzufügen** am unteren Rand eines Schritts und wählen Sie **Zielgruppenpfade**.

Die Standard-Zielgruppenpfade-Komponente enthält zwei Standard-Zielgruppen: **Gruppe 1** und **Alle anderen**. Die Gruppe **Alle anderen** umfasst alle Nutzer:innen, die keiner definierten Zielgruppe zugeordnet sind. Diese Gruppe steht immer an letzter Stelle in der Reihenfolge.

### Zielgruppen definieren {#defining-audience-groups}

Der folgende Screenshot zeigt das Layout eines erweiterten Zielgruppenpfade-Schritts. Hier können Sie bis zu acht Zielgruppen definieren (eine voreingestellte und sieben anpassbare). Um eine Zielgruppe zu definieren, wählen Sie den Gruppennamen im Zielgruppenpfade-Editor aus. Sie können Ihre Zielgruppe umbenennen, die Filter und Segmente auswählen, die für Ihre Gruppe gelten, und Gruppen hinzufügen oder löschen. Wenn Sie beispielsweise Onboarding-Nachrichten an eine bestimmte Nutzer:innengruppe senden möchten, könnten Sie Retargeting-Filter wie „Hat E-Mail angeklickt“ und „Hat In-App-Nachricht angeklickt“ auswählen.

![Ein erweiterter Zielgruppenpfad mit Gruppen für „Liebt asiatische Küche“, „Liebt lateinamerikanische Küche“, „Liebt europäische Küche“ und „Alle anderen“.]({% image_buster /assets/img/audience_path/audience_path3.png %})

Nachdem der Zielgruppenpfade-Schritt abgeschlossen ist, hat jede Zielgruppe einen separaten Branch. Sie können Zielgruppenpfade weiter verwenden, um Ihre Zielgruppe weiter zu filtern, oder Ihre Canvas-Journey mit den Standard-Canvas-Schritten fortsetzen.

![Zwei Zielgruppenpfade mit verschiedenen Gruppen basierend auf Engagement.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

#### Vergleichsfilter mit Kontextvariablen verwenden {#using-comparison-filters-with-context-variables}

Wenn Sie nach einer Kontextvariable aufteilen, die ein Datum enthält, lesen Sie [Tag-des-Jahres- und Zeitfilter für Datums-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#day-of-year-and-time-filters-for-date-context-variables), um den richtigen Vergleichstyp auszuwählen.

### Zielgruppen testen {#testing-audience-groups}

Nachdem Sie Segmente und Filter zu Ihrer Zielgruppe hinzugefügt haben, können Sie testen, ob Ihre Zielgruppen wie erwartet eingerichtet sind, indem Sie [eine:n Nutzer:in nachschlagen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), um zu bestätigen, dass sie den Zielgruppenkriterien entsprechen.

![Der Bereich „Nutzer:innensuche“.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Zielgruppenpfade verwenden {#using-audience-paths}

Die wahre Stärke der Zielgruppenpfade liegt darin, die Pfade, die Ihnen am wichtigsten sind, an **erste** Stelle zu setzen. Obwohl dieses Feature nicht zwingend strategisch eingesetzt werden muss, können einige Marketer es nutzen, um bestimmte Produkte wie Sonderangebote oder limitierte Editionen gezielt an Nutzer:innen zu bewerben.

Indem Sie diese Segmente in der Liste an erste Stelle setzen, können Sie Nutzer:innen ansprechen, die bestimmten Filtern und Segmenten entsprechen, und gleichzeitig Nutzer:innen erreichen, die diese spezifischen Kriterien möglicherweise nicht erfüllen – alles in einem einzigen Canvas-Schritt.

![Ein Zielgruppenpfad mit Gruppen für „Likes Big Brand Shoes“, „Likes Big Brand“ und „Everyone Else“.]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Nehmen wir zum Beispiel an, Sie möchten einer Gruppe von Nutzer:innen Werbung für neue Produkte senden. Sie würden zunächst Filter, die unter diese Produkte fallen, **an erste Stelle** im Zielgruppenpfad setzen. Wenn Sie eine Marketing-Campaign für das Unternehmen „Big Brand“ erstellen und eine neue Einzelhandelsmarke gerade auf den Markt gekommen ist, könnten Sie Filter wie „Likes Big Brand Shoes“ oder „Likes Big Brand Bags“ auswählen und verschiedene E-Mail-Nachrichten basierend auf der gefilterten Gruppe senden, in die die Nutzer:innen fallen.

Wenn Nutzer:innen diese Zielgruppenpfade-Komponente betreten, werden sie zunächst für Zielgruppe 1 „Likes Big Brand Shoes“ – den ersten Pfad in der Liste – ausgewertet. Falls zutreffend, fahren sie mit der nächsten in Ihrem Canvas definierten Komponente fort. Falls sie nicht „Like Big Brand Shoes“ sind, werden sie anschließend für die nächste Zielgruppe ausgewertet, Zielgruppe 2 „Likes Big Brand Bags“, und fahren mit dem nächsten Schritt fort, wenn die Kriterien erfüllt sind. Nutzer:innen, die in keine der vorherigen Gruppen fallen, werden schließlich der Gruppe „Everybody Else“ zugeordnet und fahren ebenfalls mit dem nächsten Canvas-Schritt fort, den Sie für diesen Pfad definiert haben.

Sie können die Performance dieses Schritts auch mithilfe von [Canvas Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization) einsehen.

### Zielgruppenpfade mit zufälligen Bucket-Nummern segmentieren {#segmenting-audience-paths-with-random-bucket-numbers}

Wenn Ihr Canvas ein [Rate-Limit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) verwendet (z. B. eine Begrenzung der Gesamtzahl der Nutzer:innen, die den Canvas erhalten), empfiehlt Braze, keine zufälligen Bucket-Nummern zur Segmentierung Ihrer Zielgruppenpfade zu verwenden.

Eine [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) ist ein Nutzerattribut, das verwendet werden kann, um gleichmäßig verteilte Segmente zufälliger Nutzer:innen zu erstellen. Braze verwendet die zufällige Bucket-Nummer, um Nutzer:innen während der Segmentierungsphase beim Canvas-Entry zu gruppieren, und jede Gruppe wird separat verarbeitet. Je nachdem, welche Gruppen zuerst verarbeitet werden, können einige Nutzer:innen aufgrund des Rate-Limits beim Entry begrenzt werden, was zu einer ungleichmäßigen Verteilung der Nutzer:innen führen kann, wenn sie den Zielgruppenpfade-Schritt erreichen.

Versuchen Sie in diesem Szenario stattdessen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) zu verwenden.

### Intelligenter-Kanal-Filter mit Zielgruppenpfaden verwenden {#using-intelligent-channel-filter-with-audience-paths}

Durch die Kombination von Zielgruppenpfade-Schritten und Intelligenter-Kanal-Filtern können Sie Ihr Messaging-Erlebnis an die Präferenzen und Verhaltensweisen jeder einzelnen Nutzer:in anpassen. So erhalten Ihre Nutzer:innen die relevantesten Nachrichten über die passenden Kanäle.

Beispielsweise können Sie in einem Zielgruppenpfade-Schritt drei Zielgruppen erstellen: E-Mail, Mobile Push und Everyone Else. Für die E-Mail-Zielgruppe fügen Sie den Filter `Intelligent Channel is Email` hinzu. Für die Mobile-Push-Zielgruppe fügen Sie den Filter `Intelligent Channel is Mobile Push` hinzu. Anschließend können Sie für jeden der Zielgruppenpfade einen Nachrichten-Schritt hinzufügen, um personalisierte und relevante Nachrichten zu übermitteln.

{% alert tip %}
Sehen Sie sich unsere [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) an, um Beispiele zu erhalten, wie Sie diese vorgefertigten Templates zu Ihrem Vorteil anpassen können.
{% endalert %}