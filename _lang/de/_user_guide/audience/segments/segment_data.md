---
nav_title: Segment-Daten
article_title: Segment-Daten
page_order: 4
page_type: reference
description: "Diese Seite erläutert den Bereich Segments in Ihrem Braze-Dashboard und enthält eine Zusammenfassung der bereitgestellten Statistiken."
alias: /viewing_and_understanding_segment_data/
tool:
  - Segments
  - Reports

---
# Segment-Daten {#segment-data}

> Diese Seite erläutert den Bereich Segments in Ihrem Braze-Dashboard und enthält eine Zusammenfassung der bereitgestellten Statistiken.

## Zugriff auf Daten zu Ihren Segmenten und Mitgliedschaften {#accessing-data-about-your-segments-and-membership}

Die Seite **Segments** in Ihrem Braze-Dashboard enthält eine Zusammenfassung aller Ihrer Segmente und ermöglicht es Ihnen, detaillierte Daten für jedes einzelne einzusehen. Suchen Sie auf dieser Seite nach dem Namen eines Segments und wählen Sie es aus, um es zu bearbeiten und seine Daten anzuzeigen. Informationen zum Erstellen eines Segments finden Sie unter [Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#creating-a-segment).

![Seite „Segments“]({% image_buster /assets/img_archive/segments.png %})

Nachdem Sie den Namen eines Segments ausgewählt haben, können Sie Segment-Statistiken und Filter einsehen und das Segment bearbeiten, indem Sie Filter hinzufügen oder entfernen. Vergessen Sie nicht, alle Änderungen zu speichern!

Wenn Sie das [Analytics-Tracking für ein Segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) aktivieren, können Sie Sitzungen, angepasste Events und Umsatz im Zeitverlauf für dieses Segment anzeigen.

![Umschalter für Analytics-Tracking eines Segments]({% image_buster /assets/img_archive/A_Tracking_2.png %})

### Segment-Statistiken {#segment-statistics}

Sie können die folgenden Segment-Statistiken einsehen, die sich in Realtime aktualisieren, wenn Sie Filter hinzufügen oder entfernen:

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Segment-Statistiken">
  <caption>Segment-Statistiken</caption>
    <thead>
        <tr>
            <th>Statistik</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total Users</td>
            <td class="no-split">Die Gesamtzahl der Nutzer:innen Ihrer App.</td>
        </tr>
        <tr>
            <td class="no-split">Selected Users</td>
            <td class="no-split">Wie viele Nutzer:innen sich in Ihrem Segment befinden und welchen Prozentsatz Ihrer gesamten Nutzerbasis sie ausmachen.</td>
        </tr>
        <tr>
            <td class="no-split">LTV (Paying Users)</td>
            <td class="no-split">Der Lifetime-Value pro Nutzer:in (LTV) in diesem Segment und der Lifetime-Value pro zahlende:r Nutzer:in in diesem Segment. Der LTV wird berechnet, indem Ihr Lifetime-Umsatz durch die Lifetime-Nutzer:innen geteilt wird.</td>
        </tr>
        <tr>
            <td class="no-split">Emailable (Opted-In)</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Emailable' %} Aufgrund von <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">Spam-Vorschriften</a> empfiehlt es sich, Ihre Nutzer:innen ausdrücklich um ein Opt-in zu bitten, indem Sie eine Double-Opt-in-Richtlinie implementieren, bei der Nutzer:innen auf einen Link in einer ersten Bestätigungs-E-Mail klicken müssen. Um mehr Nutzer:innen zum Opt-in zu bewegen, können Sie eine Nachricht an <a href="/docs/user_guide/channels/email/subscriptions#segmenting-by-user-subscriptions">diejenigen richten, die weder ein Opt-in noch ein Opt-out durchgeführt haben</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Push Enabled (Opted-In)</td>
            <td class="no-split">„Push Enabled“ bezieht sich auf die Anzahl der Nutzer:innen mit mindestens einem Push-Token. Einige Nutzer:innen können mehrere Push-Token haben (z. B. wenn sie ein iPhone und ein iPad besitzen), sodass die Anzahl der Push-Benachrichtigungen, die Sie an dieses Segment senden, größer sein kann als die Anzahl der „Push Enabled“-Nutzer:innen. „Opted In“ bezieht sich auf die Anzahl der Nutzer:innen, die sich ausdrücklich für Push-Benachrichtigungen entschieden haben. Nutzer:innen müssen immer ausdrücklich ein Opt-in durchführen, damit Sie ihnen Push-Benachrichtigungen senden können.</td>
        </tr>
    </tbody>
</table>

### Segment-Insights {#segment-insights}

Sie können sehen, wie ein Segment im Vergleich zu einem anderen anhand einer Reihe vorausgewählter KPIs abschneidet, indem Sie die Seite [Segment-Insights]({{site.baseurl}}/user_guide/audience/segments/segment_insights/) in Ihrem Dashboard aufrufen.

### Messaging-Nutzung {#messaging-use}
Der Abschnitt **Messaging Use** zeigt, welche Segmente, derzeit aktivierten Campaigns und derzeit aktivierten Canvases Ihr Segment als Zielgruppe verwenden.

### Historische Mitgliedschaft {#historical-membership}

Der Abschnitt **Historical Membership** zeigt, wie sich die Größe Ihres Segments im Zeitverlauf verändert hat. Verwenden Sie das Dropdown-Menü, um die Segment-Mitgliedschaft nach Zeitraum zu filtern.

Weitere Informationen zur Überwachung der Mitgliedschaft und Größe Ihres Segments finden Sie unter [Segment-Größe messen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/).

### Nutzer:innen-Vorschau {#user-preview}

Um detaillierte, nutzerspezifische Informationen zu Ihren Segmenten anzuzeigen, klicken Sie auf **User Data** und wählen Sie **User Preview** aus.

Auf dieser Seite können Sie eine Reihe nutzerspezifischer Attribute einsehen, wie z. B. Geschlecht, Alter, Anzahl der Sitzungen und ob ein Opt-in für Push und E-Mail vorliegt.

Beachten Sie, dass in Fällen, in denen Ihr Segment im Verhältnis zur Workspace-Größe sehr klein ist, die Nutzer:innen-Vorschau möglicherweise null Nutzer:innen zurückgibt. Das bedeutet nicht unbedingt, dass sich null Nutzer:innen in Ihrem Segment befinden. Führen Sie [Exakte Statistiken berechnen]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size/#statistics-for-segment-size) aus, um die genaue Größe Ihres Segments zu ermitteln.

![Nutzer:innen-Vorschau]({% image_buster /assets/img_archive/user_preview.png %})

## Performance-Daten nach Segment anzeigen {#viewing-performance-data-by-segment}

Verwenden Sie [Berichtsvorlagen des Abfrage-Builders]({{site.baseurl}}/user_guide/analytics/reports/query_builder/data_by_segments/), um Performance-Metriken für Campaigns, Canvases, Varianten und Schritte nach Segmenten aufzuschlüsseln.

## Einen Segment-Aufschlüsselungsbericht mit dem Abfrage-Builder erstellen {#creating-a-segment-breakdown-report-using-query-builder}

Um einen Bericht aus einer Vorlage des [Abfrage-Builders]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) zu erstellen, navigieren Sie zum **Query Builder** und gehen Sie wie folgt vor:

1. Wählen Sie **Create SQL Query** > **Query Template**.
2. Filtern Sie die Vorlagen nach solchen, deren Metriken „segment breakdowns“ enthalten.
3. Wählen Sie die gewünschte Vorlage aus.
4. Füllen Sie die Variablen in Ihrer SQL-Vorlage im Tab [Variablen](#variables) aus.
5. (Optional) Bearbeiten Sie das SQL in der Vorlage direkt.
6. Wählen Sie **Run Query**. Ihre Ergebnisse werden in einer Tabelle angezeigt.

## Variablen {#variables}

Bevor Sie Ihren Bericht generieren, navigieren Sie zum Tab **Variables**, um Informationen für die Berichts-Builder-Vorlage bereitzustellen, einschließlich erforderlicher Variablen, die je nach Bericht variieren.

Die Variablen umfassen:

- **Kampagne oder Canvas:** Sie können eine oder mehrere Campaigns oder Canvases einbeziehen (es gibt kein Maximum für die Anzahl der Campaigns oder Canvases, die Sie angeben können). Wenn Sie keine Campaigns oder Canvases angeben, enthält der Bericht alle Campaigns oder Canvases aus Ihrem gewählten Zeitraum.
- **Variante:** Wenn Sie eine Vorlage verwenden, die Aufschlüsselungen auf Variantenebene bietet, können Sie nach Auswahl einer Campaign oder eines Canvas Varianten innerhalb dieser Campaign oder dieses Canvas auswählen. Wenn Sie mehrere Varianten auswählen, werden Ihre Ergebnisse nach Variante gruppiert.
- **Schritt:** Wenn Sie eine Canvas-Variante auswählen, können Sie einen Canvas-Schritt auswählen. Sie können keinen Schritt auswählen, ohne zuvor eine Canvas-Variante ausgewählt zu haben.
- **Zeitraum:** Legen Sie den Zeitraum fest, aus dem Sie Daten abrufen möchten. Wenn kein Zeitraum angegeben wird, werden standardmäßig die letzten 30 Tage verwendet.
- **Produktname:** Wenn Sie einen Bericht für Kaufdaten erstellen, können Sie ein bestimmtes Produkt angeben, für das Daten abgerufen werden sollen.
- **Conversion-Fenster:** Immer erforderlich für Berichte mit Umsatz- und Kaufdaten. Die Anzahl der Tage nach E-Mail-Empfang oder -Klick, in denen Braze Käufe oder Umsatz zuordnen soll.
- **Segmente:** Geben Sie die Segmente an, nach denen die Daten aufgeschlüsselt werden sollen. Wenn keine angegeben werden, wird der Bericht für alle Segmente ausgeführt, für die Analytics-Tracking aktiviert ist.
- **Tags:** Geben Sie Tags unter **Variables** an, um Ihren Bericht für alle Campaigns oder Canvases mit bestimmten Tags auszuführen. Sie können mehrere Tags einbeziehen. Wenn Sie sowohl Tags als auch bestimmte Campaigns oder Canvases zu einem Bericht hinzufügen, enthält Ihr Bericht Daten aus Ihren Tags und den angegebenen Campaigns oder Canvases.

## Datenverfügbarkeit {#data-availability}

Daten sind für Zeiträume verfügbar, in denen beide der folgenden Bedingungen erfüllt sind:

1. [Segment-Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) ist für die Segmente aktiviert, für die Sie Daten einsehen möchten.
2. Das Feature „Performance-Daten nach Segment“ ist aktiviert.

Sie können nicht auf Daten aus Zeiträumen zugreifen, die vor der Aktivierung dieses Features für Ihr Unternehmen liegen. Wenn beispielsweise Analytics-Tracking für Segment A am 1. Oktober aktiviert wird und dieses Feature für Ihr Unternehmen am 2. Oktober aktiviert wird, können Sie nur Daten für Segment A für die Campaigns und Canvases einsehen, die nach dem 2. Oktober Metriken aufgezeichnet haben.

Wenn Ihr Unternehmen dieses Feature am 2. Oktober aktiviert hat und Analytics-Tracking für Segment B am 3. Oktober aktiviert wurde, können Sie nur Daten für Segment B für die Campaigns und Canvases einsehen, die nach dem 3. Oktober Metriken aufgezeichnet haben.