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

Stellen Sie sicher, dass Sie über Folgendes verfügen:

- Ein [Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) für Ihre Eintritts-Zielgruppe, das nicht aktiv in einem anderen Canvas oder einer anderen Campaign verwendet wird
- Mindestens ein E-Mail-Template
- Den Varianteninhalt, den Sie testen möchten, z. B. alternative Betreffzeilen, CTAs und Hero-Bilder. Sie können Varianten während der Einrichtung erstellen, aber wenn Sie sie vorab vorbereiten, beschleunigt das die Konfiguration
- Workspace-Zugriff mit Berechtigungen zur Konfiguration von KI or künstliche Intelligenz-Decisioning-Agenten

Wenn Ihr Workspace nicht für Decisioning Studio Go bereitgestellt wurde, sehen Sie die Agentenkonfigurationsoption im Tab **KI or künstliche Intelligenz Decisioning** nicht. Wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in, um Zugang zu erhalten.

## Schritt 1: Richten Sie Ihren Agenten ein {#step-1-set-up-your-agent}

1. Gehen Sie im Braze-Dashboard zum Tab **KI or künstliche Intelligenz Decisioning**.
2. Wählen Sie **Create Agent** aus.
3. Geben Sie Ihrem Agenten einen Namen, der ihn von anderen in Ihrem Workspace unterscheidet. Ein Beispiel wäre „Loyalty Members—Weekly Engagement“ statt „Email Agent“.
4. (Optional) Fügen Sie eine Beschreibung hinzu, um Kontext bereitzustellen, den Sie oder ein Teammitglied später benötigen könnten. Dazu kann gehören, wofür der Agent gedacht ist, welches Segment er anspricht und wie Erfolg aussieht.


Der Agent optimiert Ihre E-Mail-Kreativinhalte, um echtes Engagement zu maximieren, gemessen an bedeutsamer Klickaktivität pro Nutzer:in. Klicks durchlaufen mehrere unabhängige Validierungsfilter, die automatisierte Aktivitäten und Opt-out-bezogene Klicks herausfiltern, sodass das Signal echtes Kundeninteresse widerspiegelt und nicht das reine Klickvolumen.

## Schritt 2: Zielgruppe auswählen {#step-2-select-the-target-audience}

Wählen Sie das Braze-Segment aus, an das Ihr Agent sendet. Nutzer:innen in diesem Segment werden automatisch in zwei Gruppen aufgeteilt:

- **Decisioning-Studio-Gruppe:** Erhält KI or künstliche Intelligenz-optimierte E-Mail-Inhalte. Der Agent wählt die beste Variantenkombination für jede:n Nutzer:in aus.
- **Zufällige Kontrollgruppe:** Mindestens 5 % des Segments. Erhält zufällig ausgewählte Kombinationen derselben Optionen an zufällig ausgewählten Tagen. Diese Gruppe ist erforderlich.

![Ein ausgewähltes Segment mit 1.100 geschätzten Nutzer:innen.]({% image_buster /assets/img/decisioning_studio_go/audience_details.png %})

### Warum ein dediziertes Segment wichtig ist {#why-a-dedicated-segment-matters}

Wenn Nutzer:innen in Ihrem ausgewählten Segment auch Nachrichten von anderen Canvase oder Campaigns erhalten, wird das vom Agenten beobachtete Engagement durch diese anderen Nachrichten beeinflusst. Der Agent kann nicht unterscheiden, ob ein:e Nutzer:in aufgrund seiner Entscheidungen oder aufgrund anderer Einflüsse geklickt hat. Eine Warnung wird angezeigt, wenn Ihr ausgewähltes Segment an anderer Stelle verwendet wird. Sie können fortfahren, sollten jedoch mit ungenaueren Ergebnissen rechnen.

### Nutzer:innen-Suche {#user-lookup}

Verwenden Sie die **Nutzer:innen-Suche**, um zu überprüfen, ob bestimmte Nutzer:innen Ihre Segmentkriterien erfüllen. Dies ist nützlich, um Ihre Segmentdefinition zu verifizieren.

### Zielgruppenfilter {#audience-filters}

Zielgruppenfilter werden in dieser Version nicht unterstützt. Wenn Sie zusätzliche Targeting-Kriterien benötigen, [erstellen Sie ein Segment]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) mit den entsprechenden Filtern und wählen Sie dieses Segment dann als Ihre Eintrittszielgruppe aus.

### Integration mit bestehenden Canvase {#integrate-with-existing-canvases}

So verwenden Sie Decisioning Studio Go innerhalb einer umfassenderen Journey:

1. Erstellen Sie ein dediziertes Segment für Nutzer:innen, die dem Agenten zugeordnet werden sollen.
2. Verwenden Sie in Ihrem [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) einen User-Update or aktualisieren-Schritt, um die:den Nutzer:in an der richtigen Stelle in der Journey zu diesem Segment hinzuzufügen.
3. Stellen Sie sicher, dass Nutzer:innen das Canvas verlassen, damit der Agent (nicht das Canvas) ab diesem Zeitpunkt den E-Mail-Versand für alle Nutzer:innen im Segment übernimmt.

## Schritt 3: Zeitplan konfigurieren {#step-3-configure-the-schedule}

Legen Sie fest, wann der Agent senden darf.

### Schritt 3.1: Sendehäufigkeit bestimmen {#step-31-determine-the-send-frequency}

Wählen Sie aus, wie oft Nutzer:innen E-Mails von diesem Agenten erhalten – zum Beispiel dreimal pro Woche. Dies ist eine einzelne Auswahl. Der Agent optimiert nicht zwischen verschiedenen Häufigkeiten; er wählt Tage und Uhrzeiten innerhalb der von Ihnen festgelegten Häufigkeit aus.

### Schritt 3.2: Wochentage auswählen {#step-32-select-the-days-of-the-week}

Wählen Sie die Tage aus, an denen der Agent senden darf. Sie müssen mindestens so viele Tage auswählen, wie Ihre Häufigkeit erfordert (wenn der Agent dreimal pro Woche sendet, wählen Sie mindestens drei Tage; mehr Tage geben dem Agenten mehr Flexibilität). Der Agent optimiert innerhalb dieser Auswahl und wählt die besten Tage für jede:n Nutzer:in. Für maximale Flexibilität wählen Sie alle sieben Tage aus.

### Schritt 3.3: Ruhezeiten festlegen {#step-33-set-quiet-hours}

Geben Sie Zeiten an, in denen der Agent nicht senden soll. Ruhezeiten verwenden die Ortszeit der Nutzer:innen. Am häufigsten werden sie verwendet, um Sendungen in der späten Nacht und den frühen Morgenstunden zu blockieren. Außerhalb der Ruhezeiten plant der Agent Sendungen zu den Zeiten, die für jede:n Nutzer:in am wahrscheinlichsten Klicks erzeugen.

### Schritt 3.4: Frequency-Capping-Regeln festlegen {#step-34-set-frequency-capping-rules}

Ihre Frequency-Capping-Regeln können auf Agent-Ebene angewendet werden:

- **Frequency-Cap anwenden:** Verhindert, dass der Agent an eine:n Nutzer:in sendet, sobald das Frequency-Cap erreicht wurde. Je nach Konfiguration Ihrer Regeln kann dieses Cap auf Ebene der einzelnen Nutzer:innen oder auf der gesamten Account-Ebene gelten. In beiden Fällen werden keine Nachrichten an diese:n Nutzer:in gesendet, solange das Cap erreicht ist.
- **Auf das Cap anrechnen:** Wählen Sie, ob Sendungen dieses Agenten auf das Gesamt-Cap der Nutzer:innen angerechnet werden.

{% alert tip %}
Wenn Ihr Frequency-Cap die Nutzererfahrung schützt, sind die Sendungen des Agenten bereits gezielt und Sie müssen sie möglicherweise nicht auf das Cap anrechnen. Wenn Ihr Cap das gesamte Sendevolumen oder die Ausgaben kontrolliert, sollten sie wahrscheinlich angerechnet werden. Ihr CSM or Customer-Success-Manager or Customer-Success-Manager:in oder Solutions Consultant kann Ihnen helfen, den richtigen Ansatz für Ihren Workspace zu bestätigen.
{% endalert %}

## Schritt 4: Inhalte und Templates hinzufügen {#step-4-add-content-and-templates}

Legen Sie fest, womit der Agent arbeiten kann:

- **Basis-Creatives:** Die vollständigen E-Mail-Templates. Der Agent wählt zunächst aus, welches Basis-Creative an eine bestimmte Nutzer:in gesendet werden soll.
- **Creative-Komponenten:** Die spezifischen Elemente innerhalb eines Basis-Creatives – Betreffzeile, CTA und Hero-Bild –, die der Agent pro Nutzer:in personalisiert.

Sie können Basis-Creatives erstellen, indem Sie:

- Den Standard-E-Mail-Composer von Braze verwenden.
- Eine E-Mail aus einem bestehenden Canvas oder einer bestehenden Campaign importieren.

Verwenden Sie ein einzelnes Basis-Creative oder mehrere. Bei einem einzelnen Basis-Creative personalisiert der Agent nur die Komponenten darin. Bei mehreren Basis-Creatives – zum Beispiel einem lockeren, einem formellen und einem werblichen – wählt der Agent zusätzlich aus, welches Basis-Creative für die jeweilige Nutzer:in am besten passt. Der Agent kann auch aus mehreren Basis-Creatives ohne zusätzliche Creative-Komponenten auswählen.

### Schritt 4.1: Personalisierungspunkte mit Liquid-Tags markieren {#step-41-mark-personalization-points-with-liquid-tags}

Ersetzen Sie für jede Komponente, die der Agent personalisieren soll, den statischen Inhalt in Ihrem Basis-Creative durch einen Liquid-Tag aus dem Personalisierungsmenü. Geben Sie dann die Varianten-Optionen im Abschnitt **Creative Components** an.

Die in dieser Version unterstützten Komponenten sind:

- **Betreffzeile:** Ersetzen Sie die Betreffzeile in **Sending Settings** durch den Liquid-Tag für die Betreffzeile.
- **CTA:** Ersetzen Sie den Button-Text im E-Mail-Text durch den Liquid-Tag für den CTA.
- **Bild:** Ersetzen Sie die Hero-Bild-URL durch den Liquid-Tag für das Bild.

{% alert note %}
[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) werden nicht als Ersetzungspunkte für personalisierte Komponenten unterstützt. Platzieren Sie Ihre personalisierte Betreffzeile, Ihren CTA und Ihr Bild direkt im E-Mail-Text und nicht innerhalb eines Content-Blocks.
{% endalert %}

### Schritt 4.2: Varianten hinzufügen {#step-42-add-variants}

Fügen Sie im Abschnitt **Creative Components** die Varianten-Optionen für jeden Personalisierungspunkt hinzu:

- Mehrere Betreffzeilen-Optionen
- Mehrere CTA-Text-Optionen
- Mehrere Bild-URLs

Jede Variante kann bestimmten Basis-Creatives zugeordnet oder für alle Basis-Creatives verfügbar gemacht werden. Wenn Sie beispielsweise ein Basis-Creative für eine Aktion und ein weiteres für Neuheiten haben, können Sie Ihre Betreffzeile `Don't miss our biggest savings of the year` auf das Aktions-Creative beschränken, während Ihr CTA `Just dropped` für beide verfügbar bleibt.

Bilder müssen aus der Braze-Medienbibliothek ausgewählt werden. Wenn Sie ein bestimmtes Bild verwenden möchten, laden Sie es zuerst in die Medienbibliothek hoch.

### Schritt 4.3: Vorschau und Test {#step-43-preview-and-test}

Während Sie weitere Inhalte hinzufügen, können Sie Ihre Nachricht mithilfe der dynamischen Vorschau prüfen und testen, die zeigt, wie verschiedene Varianten-Kombinationen dargestellt werden. So lassen sich Darstellungsprobleme vor dem Start erkennen und beheben. Nachdem Ihre Basis-Creatives und Varianten konfiguriert sind, können Sie eine vollständige Liste aller Kombinationen einsehen, die der Agent senden darf.

Sie können die Nachricht auch testweise an sich selbst oder eine Kollegin bzw. einen Kollegen senden. Testsendungen zeigen die spezifische Varianten-Kombination an, die Sie auswählen – nicht die, die der Agent für eine bestimmte Nutzer:in wählen würde.

## Schritt 5: Einschränkungen definieren {#step-5-define-constraints}

Einschränkungen verhindern, dass der Agent denselben Nutzer:innen wiederholt dieselben Inhalte sendet. Die folgenden Ebenen stehen zur Verfügung:

- **Base-Creative-Ebene:** Verhindert, dass dasselbe Base Creative innerhalb eines von Ihnen definierten Zeitfensters mehr als einmal an eine:n Nutzer:in gesendet wird. Nützlich, wenn sich jedes Base Creative so stark unterscheidet, dass eine Wiederholung innerhalb von z. B. einer Woche als überflüssig empfunden würde.
- **Betreffzeilen-Ebene:** Verhindert, dass dieselbe Betreffzeile innerhalb eines von Ihnen definierten Zeitfensters mehr als einmal an eine:n Nutzer:in gesendet wird. Nützlich, wenn Betreffzeilen das auffälligste Signal für Wiederholungen sind.

Einschränkungen auf Varianten-Ebene für bestimmte Bilder oder CTAs werden in diesem Release nicht unterstützt.

## Schritt 6: Überprüfen und starten {#step-6-review-and-launch}

Der Bildschirm **Überprüfen** zeigt Ihre vollständige Konfiguration an: Zielgruppe und Aufteilung der Kontrollgruppe, Zeitplan, Basis-Creatives, Anzahl der Varianten und aktive Einschränkungen. Überprüfen Sie alle Validierungswarnungen (z. B. Segmentüberschneidung mit einer anderen Campaign), die in diesem Abschnitt angezeigt werden, und beheben Sie diese.

Wählen Sie **Launch** aus, um den Agenten zu aktivieren. Er wechselt von **Draft** zu **Active** und beginnt am nächsten zulässigen Tag mit dem Versand.

## Nach dem Start {#after-launch}

### Trainingsphase {#training-period}

Wenn Ihr Agent gestartet wird, tritt er in eine Trainingsphase ein. In der Berichtsoberfläche wird eine Trainingsanzeige angezeigt. Die Performance kann in den ersten Tagen schwanken, während der Agent Kombinationen ausprobiert. E-Mails werden weiterhin gesendet, während er lernt. Es gibt keine Wartezeit.

Bedeutende Performance-Veränderungen werden sichtbar, nachdem der Agent die Trainingsphase verlassen hat und in die aktive Personalisierung übergegangen ist. Die Berichte zeigen an, wann dieser Übergang stattfindet, sodass Sie jederzeit wissen, in welcher Phase sich Ihr Agent befindet.

### Berichtsansichten {#reporting-views}

Die Berichtsoberfläche bietet drei Hauptansichten:

| Ansicht | Beschreibung |
|---|---|
| **Performance** | Klickraten, Engagement-Metriken und der Uplift der Decisioning-Studio-Gruppe im Vergleich zur zufälligen Kontrollgruppe. |
| **Konfiguration** | Die aktuellen Einstellungen des Agenten – nützlich, um zu bestätigen, was gerade läuft. |
| **Agentenpräferenzen** | Zählung, wie oft jede Variante vom Agenten gewählt wurde, und zeigt, wohin der Agent für Ihre Zielgruppe tendiert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berichtsansichten" }

Aufschlüsselungen auf Elementebene zeigen, wie einzelne Betreffzeilen, CTAs und Bilder über alle Kombinationen hinweg abschneiden.

### Einen aktiven Agenten bearbeiten {#edit-an-active-agent}

Gehen Sie zur Ansicht **Konfiguration**, um Zielgruppe, Zeitplan, Kreativelemente oder Einschränkungen nach dem Start zu ändern. Die Konfigurationsansicht zeigt eine Zusammenfassung der Änderungen. Übernehmen Sie die Änderungen, bevor sie wirksam werden. Das Hinzufügen neuer Varianten setzt das Training des Agenten für bestehende Varianten nicht zurück; es fügt dem Agenten lediglich neue Optionen hinzu.

### Pausieren oder stoppen {#pause-or-stop}

Der Lebenszyklus eines Agenten ist **Entwurf** > **Aktiv** > **Gestoppt**. Wählen Sie jederzeit **Stoppen**, um einen Agenten anzuhalten; er stoppt den Versand und wird fortgesetzt, wenn Sie ihn reaktivieren.

## Referenz {#reference}

Die folgende Tabelle fasst die Bereiche von Decisioning Studio Go und die zugehörigen Details zusammen.

| Bereich | Details |
|---|---|
| **Kanal** | Nur E-Mail |
| **Konversionsmetrik** | Nur Klicks (eindeutige tägliche Klicks pro Nutzer:in) |
| **Personalisierungspunkte** | Betreffzeile, CTA, Hero-Bild (pro Basis-Creative) |
| **Zielgruppe** | Ein Braze-Segment mit erforderlicher zufälliger Kontrollgruppe (mindestens 5 %) |
| **Häufigkeit** | Einzelauswahl (kein Frequency-Decisioning) |
| **Testversand** | Über den Braze-Composer |
| **Reporting** | Ansichten für Performance, Konfiguration und Agent-Präferenzen sowie Aufschlüsselungen auf Elementebene |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio Go im Überblick" }

### Hinweise {#considerations}

- Content Blocks werden nicht als Personalisierungs-Substitutionspunkte unterstützt.
- Bild-URLs müssen manuell hinzugefügt werden. Derzeit wird die Integration der Medienbibliothek nicht unterstützt.
- Zielgruppenfilter werden über die Segmentauswahl hinaus nicht unterstützt.
- Fließtext-, Preheader- und Header-Personalisierung sind noch nicht verfügbar.

## Fehlerbehebung {#troubleshooting}

Wenden Sie sich bei Fragen zur Agentenkonfiguration, Performance-Überprüfung oder Programmgestaltung an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in oder Solutions Consultant.

Häufig gestellte Fragen finden Sie in den [Decisioning Studio Go FAQ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq).