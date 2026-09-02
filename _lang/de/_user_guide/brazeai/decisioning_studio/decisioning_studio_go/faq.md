---
nav_title: FAQ
article_title: Decisioning Studio Go – FAQ
page_order: 8
page_type: FAQ
description: "Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zu Decisioning Studio Go."
---

# Häufig gestellte Fragen {#frequently-asked-questions}

## Allgemein {#general}

### Was ist Decisioning Studio Go? {#what-is-decisioning-studio-go}

Decisioning Studio Go ist ein KI or künstliche Intelligenz-Decisioning-Agent, der direkt in das Braze-Dashboard integriert ist. Sie kuratieren ein Menü von Optionen – kreative Varianten, Versandzeitpunkte, Wochentage – und der Agent wählt für jede:n einzelne:n Nutzer:in die richtige Kombination aus, optimiert auf Klicks. Es liefert Eins-zu-eins-Personalisierung, ohne dass ein:e Data Scientist oder eine individuelle Integration erforderlich ist. Die erste Version unterstützt E-Mail; weitere Kanäle folgen in separaten Betas, wobei jeder Kanal von einem eigenen Agent verarbeitet wird.

### Wie unterscheidet sich das von A/B-Tests? {#how-is-this-different-from-ab-testing}

A/B-Tests ermitteln die Variante, die im Durchschnitt über eine gesamte Zielgruppe oder innerhalb eines Segments am besten abschneidet, und rollen diese eine Variante an alle in dieser Gruppe aus. Decisioning Studio Go wählt die beste Variante für jede:n einzelne:n Nutzer:in, basierend darauf, womit diese:r Nutzer:in zuvor interagiert hat. Verschiedene Nutzer:innen können beim selben Versand unterschiedliche Varianten erhalten. Anstatt eine Gewinnervariante an eine Gruppe auszurollen, personalisiert Decisioning Studio Go Inhalte auf individueller Ebene.

### Wie unterscheidet sich das von Decisioning Studio Pro? {#how-is-this-different-from-decisioning-studio-pro}

Go ist die Self-Service-Stufe. Es ist der richtige Einstiegspunkt für Marketer, die Eins-zu-eins-E-Mail-Personalisierung ohne großen Implementierungsaufwand wünschen. Es optimiert auf Klicks und arbeitet mit Optionen, die Sie direkt in Braze konfigurieren.

Pro ist die Full-Service-Stufe. Es optimiert für jede beliebige Geschäftsmetrik, verbindet sich mit jeder First-Party-Datenquelle, unterstützt mehrere Kanäle und wird von einem dedizierten Support durch das Braze KI or künstliche Intelligenz Decisioning Services-Team begleitet.

### Welche Art von KI or künstliche Intelligenz ist das? Ist sie generativ? {#what-kind-of-ai-is-this-is-it-generative}

Nein. Der Agent, der entscheidet, was jede:r Nutzer:in erhält, ist ein Decisioning-Agent, kein generativer. Er schreibt keine Inhalte für Sie. Sie stellen die Optionen bereit, und der Agent lernt, welche Option für jede:n einzelne:n Nutzer:in am besten funktioniert.

Decisioning Studio Go basiert auf Reinforcement Learning. Der Agent behandelt jeden Versand als Gelegenheit zu lernen: Er probiert Kombinationen der von Ihnen freigegebenen Optionen aus, beobachtet, ob jede:r Nutzer:in interagiert, und aktualisiert sein Verständnis davon, was für wen funktioniert. Im Laufe der Zeit wird er immer genauer darin, jede:n einzelne:n Nutzer:in mit der Option aus Ihrem Menü abzugleichen, die am wahrscheinlichsten einen Klick auslöst.

## Zielgruppen und Kontrollgruppen {#audiences-and-control-groups}

### Was ist der Unterschied zwischen der Decisioning-Studio-Gruppe und der zufälligen Kontrollgruppe? {#whats-the-difference-between-the-decisioning-studio-group-and-the-random-control-group}

Die Decisioning-Studio-Gruppe erhält KI or künstliche Intelligenz-optimierte E-Mail-Inhalte; der Agent wählt die beste Variante für jede:n Nutzer:in. Die zufällige Kontrollgruppe erhält zufällige Kombinationen derselben Optionen, ohne Optimierung. Beide Gruppen respektieren die von Ihnen konfigurierten Einschränkungen (wenn Sie beispielsweise festgelegt haben, dass eine Betreffzeile nicht innerhalb von 15 Tagen wiederholt werden soll, gilt diese Regel auch für die zufällige Kontrollgruppe). Der Vergleich der beiden Gruppen liefert Ihnen ein sauberes Maß für den Uplift des Agents.

### Ist die zufällige Kontrollgruppe eine Holdout-Gruppe von Nutzer:innen, die keine E-Mail erhalten? {#is-the-random-control-a-holdout-group-of-users-who-receive-no-email}

Nein. Nutzer:innen in der zufälligen Kontrollgruppe erhalten weiterhin E-Mails. Sie erhalten zufällig ausgewählte Kombinationen der von Ihnen konfigurierten Optionen, die an zufällig ausgewählten Tagen innerhalb Ihres Zeitplans versendet werden. So können Sie „KI or künstliche Intelligenz-personalisiert“ mit „derselbe Inhalt, zufällig versendet“ vergleichen, anstatt mit „gar keine E-Mail“.

### Warum ist die zufällige Kontrollgruppe erforderlich? {#why-is-the-random-control-required}

Aus zwei Gründen. Erstens liefert sie Ihnen eine fortlaufende Realtime-Messung, wie stark der Agent eine zufällige Baseline übertrifft. Zweitens nutzt der Agent das Verhalten der zufälligen Kontrollgruppe als Teil seines Lernsignals. Die Mindestgröße der zufälligen Kontrollgruppe beträgt 5 % – das ist der Mindestwert, damit der Agent zuverlässig lernen und die Performance-Messung aussagekräftig sein kann.

### Kann ich ein Segment verwenden, das bereits in einem anderen Canvas oder einer anderen Campaign genutzt wird? {#can-i-use-a-segment-thats-already-used-in-another-canvas-or-campaign}

Das ist möglich, wird aber dringend davon abgeraten, und es erscheint eine Warnung. Wenn dieselben Nutzer:innen gleichzeitig Nachrichten von Decisioning Studio Go und von anderen Canvase oder Campaigns erhalten, beeinflusst das die Interaktion auf eine Weise, die der Agent nicht berücksichtigen kann. Die sauberste Konfiguration ist ein Segment, das ausschließlich dem Agent zugewiesen ist.

## Konfiguration {#configuration}

### Was kann ich personalisieren? {#what-can-i-personalize}

Innerhalb jedes Basis-Kreativs können Sie die Betreffzeile, den CTA und ein Bild mithilfe von Liquid-Tags als Personalisierungspunkte markieren. Der Agent wählt dann pro Nutzer:in unter den Varianten, die Sie für jede Komponente bereitgestellt haben. Sie können auch mehrere Basis-Kreative verwenden; der Agent wählt auch aus, welches Basis-Kreativ verwendet wird.

### Kann ich Content Blocks für die personalisierten Komponenten verwenden? {#can-i-use-content-blocks-for-the-personalized-components}

Nein. Content Blocks funktionieren derzeit nicht als Substitutionspunkte für kreative Komponenten. Platzieren Sie Ihre personalisierte Betreffzeile, Ihren CTA und Ihr Bild direkt im E-Mail-Body und nicht innerhalb eines Content-Blocks.

### Kann ich bildbasierte Templates ohne klickbare Elemente verwenden? {#can-i-use-image-based-templates-with-no-clickable-elements}

Bildbasierte Templates werden unterstützt, schränken aber die Optimierungsmöglichkeiten des Agents ein. Wenn die gesamte E-Mail ein einziges Bild ist, kann der Agent zwar entscheiden, welches Bild gesendet wird, aber er kann Betreffzeile, CTA oder Layout innerhalb der E-Mail nicht optimieren. Mit HTML-basierten Templates mit mehreren Personalisierungspunkten erzielen Sie mehr Uplift.

### Kann ich das Konversions-Event ändern? {#can-i-change-the-conversion-event}

Für die Self-Service-Stufe ist das unterstützte Konversions-Event Klicks. In Decisioning Studio Pro können Sie für jede beliebige angepasste Geschäftsmetrik optimieren.

### Wie funktioniert die Versandfrequenz? {#how-does-send-frequency-work}

Sie wählen eine einzelne Frequenz, z. B. drei Versendungen pro Woche. Der Agent entscheidet nicht zwischen Frequenzen. Innerhalb dieser Frequenz wählt er, an welchen Tagen (aus den von Ihnen zugelassenen Tagen) und zu welchen Zeiten (innerhalb Ihrer Ruhezeiten, in der Ortszeit der Nutzer:innen) gesendet wird.

### Wie funktioniert Frequency-Capping? {#how-do-frequency-caps-work}

Während der Einrichtung können Sie die Frequency-Capping-Regeln Ihres Workspace auf den Agent anwenden und festlegen, ob die Versendungen des Agents auf das globale Frequency-Cap jede:r Nutzer:in angerechnet werden. Ihr CSM or Customer-Success-Manager or Customer-Success-Manager:in oder Solutions Consultant kann Ihnen helfen, den richtigen Ansatz für Ihr Programm zu bestimmen, basierend darauf, wie Frequency-Caps in Ihrem Workspace konfiguriert sind.

### Kann der Agent über mehrere Kanäle hinweg senden? {#can-the-agent-send-across-multiple-channels}

Jeder Agent ist auf einen einzelnen Kanal beschränkt, und der aktuell unterstützte Kanal ist E-Mail. Sie können mehrere Agents parallel für verschiedene Programme betreiben, aber jeder Agent verarbeitet einen Kanal.

## Testen und Start {#testing-and-launch}

### Wie teste ich, bevor ich live gehe? {#how-do-i-test-before-going-live}

Verwenden Sie die native Testversand-Funktion im Braze Composer. Testversendungen zeigen bestimmte Variantenkombinationen, die Sie auswählen – sie dienen der Prüfung der E-Mail selbst, nicht der Vorhersage, was der Agent tatsächlich an eine:n echte:n Nutzer:in senden würde. Die dynamische Vorschau im Composer ermöglicht es Ihnen außerdem zu sehen, wie verschiedene Variantenkombinationen gerendert werden.

### Was passiert direkt nach dem Start? {#what-happens-right-after-i-launch}

Der Agent tritt in eine Trainingsphase ein. E-Mails werden ab dem ersten Tag ohne Wartezeit versendet, aber die Performance kann schwanken, während der Agent Kombinationen erkundet. Das Reporting zeigt an, ob sich der Agent noch im Training befindet oder bereits in die aktive Personalisierung übergegangen ist, sodass Sie immer wissen, in welcher Phase er sich befindet.

### Kann ich den Agent nach dem Start bearbeiten? {#can-i-edit-the-agent-after-launch}

Ja. Zielgruppe, Zeitplan, Kreative und Einschränkungen können alle nach dem Start aktualisiert werden. Änderungen müssen promotet werden, bevor sie wirksam werden.

### Was passiert, wenn ich Inhaltsoptionen nach dem Start aktualisiere? {#what-if-i-update-content-options-after-launch}

Sie können Varianten auf dieselbe Weise hinzufügen, entfernen oder ändern, wie Sie sie ursprünglich eingerichtet haben. Änderungen müssen promotet werden, bevor sie wirksam werden. Das Hinzufügen einer neuen Variante setzt das Training des Agents für bestehende Varianten nicht zurück.

## Reporting und Ergebnisse {#reporting-and-results}

### Stimmt das Decisioning-Studio-Go-Reporting mit dem überein, was ich in meinen E-Mail-Analytics an anderer Stelle in Braze sehe? {#does-decisioning-studio-go-reporting-match-what-i-see-in-my-email-analytics-elsewhere-in-braze}

Die Zahlen können abweichen. Decisioning Studio wendet eine aggressivere Klick-Filterung an als die Standard-E-Mail-Reports, sodass die Gesamtwerte niedriger sein können. Der relative Vergleich zwischen der Decisioning-Studio-Gruppe und der zufälligen Kontrollgruppe ist innerhalb des Decisioning-Studio-Reportings konsistent, da die Klick-Filterung auf beide Gruppen gleichermaßen angewendet wird.

### Für welche Metriken optimiert der Agent? {#what-metrics-does-the-agent-optimize-for}

Eindeutige tägliche Klicks pro Nutzer:in. Das Ziel des Agents ist es, die Anzahl der einzelnen Nutzer:innen zu maximieren, die klicken – nicht das reine Klickvolumen.

### Kann ich sehen, welche Kombinationen am besten abschneiden? {#can-i-see-which-combinations-are-performing-best}

Ja. Das Reporting umfasst die Verteilung einzelner Elemente – wie Betreffzeilen, CTAs und Bilder –, die der Agent versendet.

### Wer ist für die Inhalte verantwortlich, die der Agent versendet? {#whos-accountable-for-the-content-the-agent-sends}

Sie. Der Agent versendet ausschließlich Inhalte, die Sie als Variante hinzugefügt haben. Der Agent entscheidet die Kombination für jede:n Nutzer:in, aber jedes einzelne Element stammt aus den von Ihnen bereitgestellten Varianten.

## Unterstützung {#support}

### Wo erhalte ich Hilfe zu meinem Agent? {#where-do-i-get-help-with-my-agent}

Wenden Sie sich an Ihren Braze CSM or Customer-Success-Manager or Customer-Success-Manager:in oder Solutions Consultant, um Unterstützung bei der Konfiguration, der Performance-Überprüfung oder dem Programmdesign zu erhalten.