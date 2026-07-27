---
nav_title: Richten Sie Ihren Agenten ein
article_title: Richten Sie Ihren Decisioning Studio Go-Agenten ein
page_order: 0
page_type: reference
description: "Dieser Artikel beschreibt den Einrichtungsablauf von Decisioning Studio Go, um Zielgruppe, Zeitplan, Kreativinhalte, Einschränkungen zu konfigurieren und Ihren Agenten zu starten."
toc_headers: h2
---

# Richten Sie Ihren Decisioning Studio Go-Agenten ein {#set-up-your-decisioning-studio-go-agent}

> Dieser Artikel beschreibt, wie Sie einen Decisioning Studio Go-Agenten mit dem Self-Service-Einrichtungsablauf im Braze-Dashboard konfigurieren.

Einen Überblick über die Funktionsweise von Decisioning Studio Go finden Sie unter [BrazeAI Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go). Um vor der Konfiguration eines Agenten zu prüfen, ob Ihr Programm geeignet ist, lesen Sie [Beispiele für Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples).

## Voraussetzungen {#prerequisites}

Stellen Sie sicher, dass Sie Folgendes bereit haben:

- Ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) für Ihre Eintritts-Zielgruppe, das nicht aktiv in einem anderen Canvas oder einer anderen Campaign verwendet wird
- Mindestens ein E-Mail-Template
- Die Varianteninhalte, die Sie testen möchten, wie alternative Betreffzeilen, CTAs und Hero-Bilder. Sie können Varianten während der Einrichtung erstellen, aber wenn Sie sie vorab vorbereiten, beschleunigt das die Konfiguration
- Workspace-Zugriff mit Berechtigungen zur Konfiguration von KI-Decisioning-Agenten

Wenn Ihr Workspace nicht für Decisioning Studio Go bereitgestellt wurde, sehen Sie die Option zur Agentenkonfiguration im Tab **AI Decisioning** nicht. Wenden Sie sich an Ihren Customer-Success-Manager, um Zugang zu erhalten.

## Schritt 1: Richten Sie Ihren Agenten ein {#step-1-set-up-your-agent}

1. Gehen Sie im Braze-Dashboard zum Tab **AI Decisioning**.
2. Wählen Sie **Create Agent** aus.
3. Geben Sie Ihrem Agenten einen Namen, der ihn von anderen Agenten in Ihrem Workspace unterscheidet. Ein Beispiel wäre „Loyalty Members—Weekly Engagement“ statt „Email Agent“.
4. (Optional) Fügen Sie eine Beschreibung hinzu, um Kontext bereitzustellen, den Sie oder ein Teammitglied später benötigen könnten. Dies kann beinhalten, wofür der Agent gedacht ist, welches Segment er anspricht und wie Erfolg aussieht.


Der Agent optimiert Ihre E-Mail-Kreativinhalte, um echtes Engagement zu maximieren, gemessen an bedeutsamer Klickaktivität pro Nutzer:in. Klicks durchlaufen mehrere unabhängige Validierungsfilter, die automatisierte Aktivitäten und Opt-out-bezogene Klicks herausfiltern, sodass das Signal echtes Kundeninteresse widerspiegelt und nicht das reine Klickvolumen.

## Schritt 2: Wählen Sie die Zielgruppe aus {#step-2-select-the-target-audience}

Wählen Sie das Braze-Segment aus, an das Ihr Agent sendet. Nutzer:innen in diesem Segment werden automatisch in zwei Gruppen aufgeteilt:

- **Decisioning Studio-Gruppe:** Erhält KI-optimierte E-Mail-Inhalte. Der Agent wählt die beste Variantenkombination für jede:n Nutzer:in aus.
- **Zufällige Kontrollgruppe:** Mindestens 5 % des Segments. Erhält zufällig ausgewählte Kombinationen derselben Optionen an zufällig ausgewählten Tagen. Diese Gruppe ist erforderlich.

![Ein ausgewähltes Segment mit 1.100 geschätzten Nutzer:innen.]({% image_buster /assets/img/decisioning_studio_go/audience_details.png %})

### Warum ein dediziertes Segment wichtig ist {#why-a-dedicated-segment-matters}

Wenn Nutzer:innen in Ihrem ausgewählten Segment auch Nachrichten von anderen Canvases oder Campaigns erhalten, wird das vom Agenten beobachtete Engagement durch diese anderen Nachrichten beeinflusst. Der Agent kann nicht unterscheiden, ob ein:e Nutzer:in aufgrund seiner Entscheidungen oder aufgrund von etwas anderem geklickt hat. Eine Warnung erscheint, wenn Ihr ausgewähltes Segment anderweitig verwendet wird; Sie können fortfahren, sollten aber mit verrauschteren Ergebnissen rechnen.

### Nutzersuche {#user-lookup}

Verwenden Sie **User Lookup**, um zu überprüfen, ob bestimmte Nutzer:innen Ihre Segmentkriterien erfüllen. Dies ist nützlich, um Ihre Segmentdefinition zu verifizieren.

### Zielgruppenfilter {#audience-filters}

Zielgruppenfilter werden in dieser Version nicht unterstützt. Wenn Sie zusätzliche Targeting-Kriterien benötigen, [erstellen Sie ein Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) mit diesen angewendeten Filtern und wählen Sie dann dieses Segment als Ihre Eintritts-Zielgruppe aus.

### Integration mit bestehenden Canvases {#integrate-with-existing-canvases}

Um Decisioning Studio Go innerhalb einer umfassenderen Journey zu verwenden:

1. Erstellen Sie ein dediziertes Segment für Nutzer:innen, die im Agenten sein sollen.
2. Verwenden Sie in Ihrem [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) einen User-Update-Schritt, um die:den Nutzer:in zum richtigen Zeitpunkt in der Journey zu diesem Segment hinzuzufügen.
3. Stellen Sie sicher, dass Nutzer:innen das Canvas verlassen, damit der Agent (nicht das Canvas) den E-Mail-Versand für alle im Segment ab diesem Zeitpunkt übernimmt.

## Schritt 3: Konfigurieren Sie den Zeitplan {#step-3-configure-the-schedule}

Legen Sie fest, wann der Agent senden darf.

### Schritt 3.1: Bestimmen Sie die Sendehäufigkeit {#step-31-determine-the-send-frequency}

Wählen Sie aus, wie oft Nutzer:innen E-Mails von diesem Agenten erhalten – zum Beispiel dreimal pro Woche. Dies ist eine einzelne Auswahl. Der Agent optimiert nicht zwischen verschiedenen Häufigkeiten; er wählt Tage und Zeiten innerhalb der von Ihnen festgelegten Häufigkeit.

### Schritt 3.2: Wählen Sie die Wochentage aus {#step-32-select-the-days-of-the-week}

Wählen Sie aus, an welchen Tagen der Agent senden darf. Sie müssen mindestens so viele Tage auswählen, wie Ihre Häufigkeit erfordert (wenn der Agent dreimal pro Woche sendet, wählen Sie mindestens drei Tage; mehr Tage geben dem Agenten mehr Flexibilität). Der Agent optimiert innerhalb dieser Auswahl und wählt die besten Tage für jede:n Nutzer:in. Für maximale Flexibilität wählen Sie alle sieben Tage.

### Schritt 3.3: Legen Sie Ruhezeiten fest {#step-33-set-quiet-hours}

Geben Sie Zeiten an, in denen der Agent nicht senden soll. Ruhezeiten verwenden die Ortszeit der:des Nutzer:in. Die häufigste Verwendung ist das Blockieren von Sendungen in der späten Nacht und den frühen Morgenstunden. Außerhalb der Ruhezeiten plant der Agent Sendungen zu den Zeiten, die am wahrscheinlichsten Klicks für jede:n Nutzer:in generieren.

### Schritt 3.4: Legen Sie Frequency-Capping-Regeln fest {#step-34-set-frequency-capping-rules}

Ihre Frequency-Capping-Regeln können auf Agentenebene angewendet werden:

- **Frequency-Cap anwenden:** Verhindert, dass der Agent an eine:n Nutzer:in sendet, sobald deren Frequency-Cap erreicht ist. Je nach Konfiguration Ihrer Regeln kann dieses Cap auf der Ebene einzelner Nutzer:innen oder auf der gesamten Kontoebene gelten. In beiden Fällen werden keine Nachrichten an diese:n Nutzer:in gesendet, solange das Cap erreicht ist.
- **Auf Cap anrechnen:** Wählen Sie, ob Sendungen dieses Agenten auf das Gesamt-Cap der:des Nutzer:in angerechnet werden.

{% alert tip %}
Wenn Ihr Frequency-Cap die Nutzererfahrung schützt, sind die Sendungen des Agenten bereits gezielt und Sie müssen sie möglicherweise nicht auf das Cap anrechnen. Wenn Ihr Cap das gesamte Sendevolumen oder die Ausgaben kontrolliert, möchten Sie sie wahrscheinlich anrechnen lassen. Ihr Customer-Success-Manager oder Solutions Consultant kann Ihnen helfen, den richtigen Ansatz für Ihren Workspace zu bestätigen.
{% endalert %}

## Schritt 4: Fügen Sie Inhalte und Templates hinzu {#step-4-add-content-and-templates}

Definieren Sie, womit der Agent arbeiten kann:

- **Basis-Kreativinhalte:** Die vollständigen E-Mail-Templates. Der Agent wählt zuerst aus, welchen Basis-Kreativinhalt er an eine:n bestimmte:n Nutzer:in sendet.
- **Kreativkomponenten:** Die spezifischen Elemente innerhalb eines Basis-Kreativinhalts – Betreffzeile, CTA und Hero-Bild –, die der Agent pro Nutzer:in personalisiert.

Sie können Basis-Kreativinhalte erstellen, indem Sie:

- Den Standard-E-Mail-Composer von Braze verwenden.
- Eine E-Mail aus einem bestehenden Canvas oder einer bestehenden Campaign importieren.

Verwenden Sie einen einzelnen Basis-Kreativinhalt oder mehrere. Mit einem Basis-Kreativinhalt personalisiert der Agent nur die Komponenten darin. Mit mehreren Basis-Kreativinhalten – zum Beispiel einem lockeren, einem formellen und einem werblichen – wählt der Agent auch aus, welcher Basis-Kreativinhalt für jede:n Nutzer:in richtig ist. Der Agent kann auch aus mehreren Basis-Kreativinhalten ohne zusätzliche Kreativkomponenten wählen.

### Schritt 4.1: Markieren Sie Personalisierungspunkte mit Liquid-Tags {#step-41-mark-personalization-points-with-liquid-tags}

Ersetzen Sie für jede Komponente, die der Agent personalisieren soll, den statischen Inhalt in Ihrem Basis-Kreativinhalt durch einen Liquid-Tag aus dem Personalisierungsmenü. Geben Sie dann die Variantenoptionen im Abschnitt **Creative Components** an.

Die unterstützten Komponenten in dieser Version sind:

- **Betreffzeile:** Ersetzen Sie die Betreffzeile in **Sending Settings** durch den Liquid-Tag für die Betreffzeile.
- **CTA:** Ersetzen Sie den Button-Text im E-Mail-Body durch den Liquid-Tag für CTA.
- **Bild:** Ersetzen Sie die Hero-Bild-URL durch den Liquid-Tag für Bild.

{% alert note %}
[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) werden nicht als Substitutionspunkte für personalisierte Komponenten unterstützt. Platzieren Sie Ihre personalisierte Betreffzeile, CTA und Ihr Bild direkt im E-Mail-Body und nicht innerhalb eines Content-Blocks.
{% endalert %}

### Schritt 4.2: Fügen Sie Varianten hinzu {#step-42-add-variants}

Fügen Sie im Abschnitt **Creative Components** die Variantenoptionen für jeden Personalisierungspunkt hinzu:

- Mehrere Betreffzeilenoptionen
- Mehrere CTA-Textoptionen
- Mehrere Bild-URLs

Jede Variante kann bestimmten Basis-Kreativinhalten zugeordnet oder für alle Basis-Kreativinhalte verfügbar gemacht werden. Wenn Sie beispielsweise einen Basis-Kreativinhalt haben, der einen Sale bewirbt, und einen anderen, der Neuheiten bewirbt, können Sie Ihre Betreffzeile `Don't miss our biggest savings of the year` nur auf den Sale-Kreativinhalt beschränken, während Sie Ihren CTA `Just dropped` für beide verfügbar halten.

Bilder müssen aus der Braze-Medienbibliothek ausgewählt werden. Wenn Sie ein Bild verwenden möchten, laden Sie es zuerst in die Medienbibliothek hoch.

### Schritt 4.3: Vorschau und Test {#step-43-preview-and-test}

Während Sie weitere Inhalte hinzufügen, können Sie Ihre Nachricht mithilfe der dynamischen Vorschau ansehen und testen, die zeigt, wie verschiedene Variantenkombinationen gerendert werden. Dies ist hilfreich, um Darstellungsprobleme vor dem Start zu erkennen und zu beheben. Nachdem Ihre Basis-Kreativinhalte und Varianten konfiguriert sind, können Sie eine vollständige Liste aller Kombinationen sehen, die der Agent senden darf.

Sie können die Nachricht auch testweise an sich selbst oder ein Teammitglied senden. Testsendungen zeigen die spezifische Variantenkombination an, die Sie auswählen, nicht das, was der Agent für eine:n bestimmte:n Nutzer:in wählen würde.

## Schritt 5: Definieren Sie Einschränkungen {#step-5-define-constraints}

Einschränkungen verhindern, dass der Agent repetitive Inhalte an dieselbe:n Nutzer:in sendet. Die folgenden Ebenen sind verfügbar:

- **Basis-Kreativinhalt-Ebene:** Verhindert, dass derselbe Basis-Kreativinhalt innerhalb eines von Ihnen definierten Zeitfensters mehr als einmal an eine:n Nutzer:in gesendet wird. Nützlich, wenn jeder Basis-Kreativinhalt so unterschiedlich ist, dass eine Wiederholung innerhalb von beispielsweise einer Woche veraltet wirken würde.
- **Betreffzeilen-Ebene:** Verhindert, dass dieselbe Betreffzeile innerhalb eines von Ihnen definierten Zeitfensters mehr als einmal an eine:n Nutzer:in gesendet wird. Nützlich, wenn Betreffzeilen das sichtbarste Wiederholungssignal sind.

Einschränkungen auf Variantenebene für bestimmte Bilder oder CTAs werden in dieser Version nicht unterstützt.

## Schritt 6: Überprüfen und starten {#step-6-review-and-launch}

Der Bildschirm **Review** zeigt Ihre vollständige Konfiguration an: Zielgruppe und Aufteilung der zufälligen Kontrollgruppe, Zeitplan, Basis-Kreativinhalte, Variantenanzahl und aktive Einschränkungen. Überprüfen und beheben Sie alle Validierungswarnungen (zum Beispiel Segmentüberschneidung mit einer anderen Campaign), die in diesem Abschnitt angezeigt werden.

Wählen Sie **Launch** aus, um den Agenten zu aktivieren. Er wechselt von **Draft** zu **Live** und beginnt am nächsten zulässigen Tag mit dem Versand.

## Nach dem Start {#after-launch}

### Trainingsphase {#training-period}

Wenn Ihr Agent startet, tritt er in eine Trainingsphase ein. Ein Trainingsindikator wird in der Reporting-Oberfläche angezeigt. Die Performance kann in den ersten Tagen schwanken, während der Agent Kombinationen erkundet. E-Mails werden weiterhin gesendet, während er lernt. Es gibt keine Wartezeit.

Bedeutsame Veränderungen in der Performance zeigen sich, nachdem der Agent die Trainingsphase verlassen hat und in die aktive Personalisierung übergegangen ist. Das Reporting zeigt an, wann dieser Übergang stattfindet, sodass Sie immer wissen, in welcher Phase sich Ihr Agent befindet.

### Reporting-Ansichten {#reporting-views}

Die Reporting-Oberfläche bietet drei Hauptansichten:

| Ansicht | Beschreibung |
|---|---|
| **Performance** | Klickraten, Engagement-Metriken und der Lift der Decisioning Studio-Gruppe gegenüber der zufälligen Kontrollgruppe. |
| **Konfiguration** | Die aktuellen Einstellungen des Agenten – nützlich, um zu bestätigen, was gerade läuft. |
| **Agentenpräferenzen** | Zählt, wie oft jede Variante vom Agenten gewählt wurde, und zeigt, wohin der Agent für Ihre Zielgruppe tendiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reporting-Ansichten" }

Aufschlüsselungen auf Elementebene zeigen, wie einzelne Betreffzeilen, CTAs und Bilder über alle Kombinationen hinweg performen.

### Einen aktiven Agenten bearbeiten {#edit-a-live-agent}

Gehen Sie zur Ansicht **Konfiguration**, um Zielgruppe, Zeitplan, Kreativinhalte oder Einschränkungen nach dem Start zu ändern. Die Konfigurationsansicht zeigt eine Zusammenfassung der Änderungen. Übernehmen Sie Änderungen, bevor sie wirksam werden. Das Hinzufügen neuer Varianten setzt das Training des Agenten für bestehende Varianten nicht zurück; es fügt dem Menü des Agenten neue Optionen hinzu.

### Pausieren oder stoppen {#pause-or-stop}

Der Lebenszyklus eines Agenten ist **Draft** > **Live** > **Stopped**. Wählen Sie jederzeit **Stop** aus, um einen Agenten anzuhalten; er stoppt den Versand und nimmt ihn wieder auf, wenn Sie ihn reaktivieren.

## Referenz {#reference}

Die folgende Tabelle fasst die Bereiche von Decisioning Studio Go und zugehörige Details zusammen.

| Bereich | Details |
|---|---|
| **Kanal** | Nur E-Mail |
| **Konversionsmetrik** | Nur Klicks (eindeutige tägliche Klicks pro Nutzer:in) |
| **Personalisierungspunkte** | Betreffzeile, CTA, Hero-Bild (pro Basis-Kreativinhalt) |
| **Zielgruppe** | Ein Braze-Segment mit erforderlicher zufälliger Kontrollgruppe (mindestens 5 %) |
| **Häufigkeit** | Einzelauswahl (kein Häufigkeits-Decisioning) |
| **Testsendungen** | Über den Braze-Composer |
| **Reporting** | Ansichten für Performance, Konfiguration und Agentenpräferenzen sowie Aufschlüsselungen auf Elementebene |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Umfang von Decisioning Studio Go" }

### Hinweise {#considerations}

- Content Blocks werden nicht als Personalisierungs-Substitutionspunkte unterstützt.
- Bild-URLs müssen manuell hinzugefügt werden. Derzeit wird die Integration der Medienbibliothek nicht unterstützt.
- Zielgruppenfilter werden über die Segmentauswahl hinaus nicht unterstützt.
- Personalisierung von Body-Text, Preheader und Header ist noch nicht verfügbar.

## Fehlerbehebung {#troubleshooting}

Wenden Sie sich an Ihren Customer-Success-Manager oder Solutions Consultant, um Hilfe bei der Agentenkonfiguration, Performance-Überprüfung oder Programmgestaltung zu erhalten.

Häufig gestellte Fragen finden Sie in den [Decisioning Studio Go FAQ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq).