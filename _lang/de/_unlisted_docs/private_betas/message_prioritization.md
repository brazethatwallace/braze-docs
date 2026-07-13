---
article_title: Nachrichtenpriorisierung
permalink: /message_prioritization/
toc_headers: h2
description: "Dieser Referenzartikel beschreibt die übergeordnete Nachrichtenpriorisierung und wie Sie diese für Ihren Workspace konfigurieren."
---

# Nachrichtenpriorisierung {#message-prioritization}

> Verwenden Sie die Nachrichtenpriorisierung, um sicherzustellen, dass Ihre Nutzer:innen die Campaigns erhalten, die am wichtigsten sind.

{% alert important %}
Die Nachrichtenpriorisierung befindet sich derzeit in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Teilnahme an dieser Beta interessiert sind.<br><br>Dieser Artikel spiegelt die Version der Nachrichtenpriorisierung wider, die für das Produktionsrelease Ende Juli 2026 geplant ist. Einige hier beschriebene Verhaltensweisen sind möglicherweise noch nicht in allen Beta-Workspaces verfügbar.
{% endalert %}

Nur Administrator:innen können die übergeordneten Einstellungen der Nachrichtenpriorisierung konfigurieren. Nutzer:innen mit eingeschränkten Rechten können jede Seite in diesem Abschnitt einsehen, aber keine Änderungen vornehmen.

Für die übergeordneten Einstellungen der Nachrichtenpriorisierung gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung**.

## Funktionsweise {#how-it-works}

Die Nachrichtenpriorisierung ermöglicht es Ihnen, [Kategorien](#categories) und [Priorisierungsregeln](#prioritization-rules) zu erstellen, um die Reihenfolge Ihrer Nachrichten festzulegen.

Nehmen wir an, eine Kosmetikmarke verwaltet E-Mail-Aktionen für bezahlte Partnerschaften und Kundenbindungs-Programme. Mit der Nachrichtenpriorisierung erstellt die Marke zwei Kategorien mit den Namen „Bezahlte Partnerschaften“ und „Kundenbindung“. Die Marke ordnet diese Kategorien danach, welche geschäftskritischer ist. Während der Weihnachtszeit stuft die Marke „Kundenbindung“ höher als „Bezahlte Partnerschaften“ ein, um Kund:innen zu priorisieren, die seit über einem Jahr Teil des Mitgliedschaftsprogramms sind.

![Ein Beispiel für Priorisierungsregeln für zwei Kategorien: „Bezahlte Partnerschaften“ und „Kundenbindung“.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

Zum Sendezeitpunkt vergleicht Braze die zu sendende Nachricht mit anderen Nachrichten, die die Nutzer:innen möglicherweise erhalten und die für die Priorisierung aktiviert sind, eine Prioritätskategorie zugewiesen haben und auf dieselbe Frequency-Capping-Regel innerhalb desselben Frequency-Capping-Fensters angerechnet werden. Wenn das Senden der aktuellen Nachricht verhindern würde, dass eine Nachricht mit höherer Priorität später gesendet wird, stuft Braze die Nachricht mit niedrigerer Priorität herab. Abhängig vom konfigurierten Wiederholungsfenster wird diese Nachricht mit niedrigerer Priorität entweder später erneut versucht oder nicht gesendet.

Die Nachrichtenpriorisierung kann Folgendes auswerten:

- Geplante Campaigns
- Aktionsbasierte Campaigns
- Canvases

Braze verwendet seine Vorhersage, wann jede Nachricht voraussichtlich gesendet wird, um zu bewerten, ob das Senden einer Nachricht jetzt verhindern könnte, dass eine Nachricht mit höherer Priorität später gesendet wird. Weitere Informationen darüber, wie Braze den zukünftigen Sendezeitpunkt für Campaigns und Canvases vorhersagt, finden Sie unter [Wie sagt Braze vorher, wann eine zukünftige Nachricht gesendet wird?](#how-does-braze-predict-when-a-future-message-sends)

### Unterstützte Nachrichtentypen {#supported-message-types}

Die Nachrichtenpriorisierung unterstützt dieselben Kanäle wie Frequency-Capping:

- Push-Benachrichtigungen
- E-Mail
- SMS
- Webhooks
- WhatsApp
- LINE

Für die Priorisierung und das Frequency-Capping werden iOS-Push, Android-Push, Web-Push und andere Push-Benachrichtigungsplattformen als ein gemeinsamer Push-Kanal behandelt, nicht als separate Kanäle.

## Kategorien {#categories}

Priorisierungsregeln basieren auf einer Rangfolge von Kategorien, die ein Label darstellen, das Sie einer bestimmten Campaign oder einem Canvas zuweisen können (ähnlich wie ein [Tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags)). Sie können bis zu 20 Kategorien gleichzeitig erstellen.

So fügen Sie eine neue Kategorie hinzu:

1. Gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung** > **Kategorien**.
2. Wählen Sie **Neue Kategorie erstellen**.

![Der Button „Neue Kategorie erstellen“ im Abschnitt Nachrichtenpriorisierung.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Geben Sie der Kategorie einen Namen und eine optionale Beschreibung.
4. Wählen Sie **Kategorie erstellen**.

![Eine Beispielkategorie mit dem Namen „P3“ und der Beschreibung „Dies ist meine dritthöchste Prioritätskategorie.“]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Um eine Kategorie zu bearbeiten oder zu löschen, wählen Sie das <i class="fas fa-ellipsis-vertical"></i>-Menü.

## Priorisierungsregeln {#prioritization-rules}

Nachdem Ihre Kategorien eingerichtet sind, können Sie sie in einem Satz von Priorisierungsregeln ordnen. Regeln werden in absteigender Prioritätsreihenfolge geordnet. Sie können bis zu 10 Priorisierungsregeln gleichzeitig erstellen.

1. Gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung** > **Priorisierungsregeln**, um Ihre Regeln zu konfigurieren.

![Der Abschnitt „Priorisierungsregeln“ ohne bisher festgelegte Prioritäten.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Wählen Sie **Regel hinzufügen**.
3. Wählen Sie eine Kategorie aus dem Dropdown-Menü.

![Priorisierungsregel „Priorität 1“ mit P1 als ausgewählter Kategorie.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Fügen Sie weitere Regeln hinzu, indem Sie **+ Regel hinzufügen** unter Ihrer letzten Regel auswählen.

Um Regeln neu zu ordnen, wählen und ziehen Sie das <i class="fa-solid fa-grip-vertical"></i>-Symbol einer Regel. Um eine Regel zu löschen, wählen Sie das <i class="fas fa-ellipsis-vertical"></i>-Menü und dann **Regel löschen**.

Stellen Sie sicher, dass Sie **Speichern** auswählen, damit Ihre Änderungen übernommen werden.

## Einstellungen auf Campaign-Ebene {#campaign-level-settings}

### Opt-in

Um eine Campaign für die Priorisierung zu aktivieren, wählen Sie das Kontrollkästchen **Opt-in zur Nachrichtenpriorisierung** in den Zustellungseinstellungen der Campaign.

![Das Kontrollkästchen für „Opt-in zur Nachrichtenpriorisierung“.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Weisen Sie anschließend die Campaign einer Kategorie zu, indem Sie eine aus dem Dropdown-Menü **Kategorie** auswählen.

![Das Dropdown-Menü für die Nachrichtenpriorisierungs-Kategorie in den Zustellungseinstellungen einer Campaign.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

Die Nachrichtenpriorisierung unterstützt geplante Campaigns und aktionsbasierte Campaigns.

### Intelligentes Timing {#intelligent-timing}

Für Campaigns, die intelligentes Timing verwenden, vergleicht die Nachrichtenpriorisierung Nachrichten anhand des Sendezeitpunkts, den Braze für jede:n Nutzer:in auswählt, anstatt nur den ursprünglichen Campaign-Zeitplan zu verwenden. So kann Braze die Nachricht berücksichtigen, die am wahrscheinlichsten zuerst an diese:n Nutzer:in gesendet wird.

Für wiederkehrende Campaigns mit intelligentem Timing kann Braze den bekannten Sendezeitpunkt der aktuellen Wiederholung verwenden, wenn diese Campaign mit anderen berechtigten priorisierten Nachrichten verglichen wird.

### Wiederholungsfenster {#retry-window}

Ein Wiederholungsfenster ermöglicht es aktivierten Nachrichten, bis zu drei Tage lang erneut versucht zu werden, wenn der erste Versuch keine ausreichend hohe Priorität zum Senden hatte. An jedem folgenden Tag wird zur gleichen Zeit, zu der die Nachricht ursprünglich geplant oder getriggert wurde, ein erneuter Sendeversuch unternommen. Nach dem letzten Tag im Wiederholungsfenster wird die Nachricht, falls sie immer noch nicht gesendet wurde, nicht weiter versucht und dauerhaft herabgestuft.

Für wiederkehrende geplante Campaigns muss das Wiederholungsfenster kürzer sein als der minimale Zeitraum zwischen den Sendungen dieser Campaign. Wiederholungen erfolgen immer einen Tag nach dem ursprünglichen Sendezeitpunkt, auch wenn die Campaign normalerweise nicht an diesem Tag zum Senden geplant ist. Wenn Sie beispielsweise eine Campaign haben, die jeden Montag und Mittwoch sendet, erfolgt der Wiederholungsversuch am Dienstag, sodass das Wiederholungsfenster auf einen Tag eingestellt werden muss. Wenn Sie eine Campaign haben, die jeden Montag, Mittwoch und Freitag sendet und der Freitagsversand mit einem eintägigen Wiederholungsfenster wiederholt wird, erfolgt der Wiederholungsversuch am Samstag, nicht am Montag.

![Die Einstellung „Wiederholungsfenster“ auf 1 Tag eingestellt.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Für aktionsbasierte Campaigns basieren Wiederholungen auf dem Zeitpunkt, zu dem die getriggerte Nachricht ursprünglich gesendet werden sollte.

Aktionsbasierte Campaigns, die Ausnahme-Events verwenden, unterstützen keine Wiederholungsfenster.

Wiederholungsfenster für Canvas-Nachrichten werden auf Schrittebene konfiguriert. Für unterstützte Canvas-Nachrichtenschritte kann Braze, wenn ein Canvas-Nachrichtenschritt herabgestuft wird und ein Wiederholungsfenster konfiguriert ist, diesen Schritt später innerhalb seines Wiederholungsfensters erneut versuchen.

## Einstellungen auf Canvas-Ebene {#canvas-level-settings}

Um ein Canvas für die Nachrichtenpriorisierung zu aktivieren, aktivieren Sie die Nachrichtenpriorisierung in den Canvas-Einstellungen und weisen Sie das Canvas einer Kategorie zu.

Wenn Nutzer:innen für mehrere priorisierte Nachrichten berechtigt sind, bewertet Braze aktivierte Campaigns und berechtigte Canvas-Nachrichtenschritte gemeinsam auf unterstützten Kanälen.

Für Campaigns umfasst dies berechtigte geplante und aktionsbasierte Sendungen.

Für Canvases umfasst dies:

- Zukünftige geplante Canvases, für die die Nutzer:innen zum Eintritt berechtigt sind
- Canvases, in denen sich die Nutzer:innen derzeit befinden

Die Canvas-Priorisierung ist kein Alles-oder-Nichts-Prinzip. Eine Campaign mit höherer Priorität kann dazu führen, dass ein Canvas-Schritt herabgestuft wird, während spätere berechtigte Schritte in demselben Canvas je nach Kategorierangfolge, Sendezeitpunkt und Frequency-Capping-Regeln weiterhin gesendet werden können.

### Wie Braze zukünftige Nachrichten bewertet {#how-braze-evaluates-future-messages}

Braze bewertet Campaigns und Canvases je nach Nachrichtentyp unterschiedlich.

#### Campaigns

Braze vergleicht jede berechtigte Campaign-Nachricht anhand des Zeitpunkts, zu dem diese Nachricht voraussichtlich gesendet wird.

#### Canvases

Braze durchläuft das Canvas, um zu bestimmen, welche zukünftigen Nachrichten Nutzer:innen erhalten könnten, beginnend ab:

- Canvas-Eintritt, für zukünftige geplante Canvases
- Dem aktuellen Schritt der Nutzer:innen, wenn sie sich bereits im Canvas befinden

Braze bewertet Canvas-Schritte dann auf folgende Weise.

##### Nachrichtenschritte {#messaging-steps}

Diese Schritte werden für die Priorisierung gezählt und zur Menge der berechtigten Nachrichten hinzugefügt, wenn sie auf einem unterstützten Kanal senden.

- Nachrichtenschritt
- Content-Optimizer-Schritt

##### Fortsetzungsschritte {#continuation-steps}

Diese Schritte werden für die Priorisierung ignoriert und beeinflussen die Vorausschau nicht.

- Kontextaktualisierungsschritt
- Nutzer:innen-Aktualisierungsschritt
- Audience-Sync-Schritt
- Feature-Flag-Schritt
- Verzögerungsschritt mit fester Verzögerung

##### Grenzschritte {#boundary-steps}

Braze stoppt die Vorausschau an diesen Schritten, bis die Nutzer:innen tatsächlich im Canvas durch sie hindurchgehen.

- Verzögerungsschritt mit personalisierter Verzögerung
- Verzögerungsschritt, der auf einen Verzweigungsschritt folgt
- Aktionspfad-Schritt
- Experimentschritt

##### Verzweigungsschritte {#branching-steps}

Diese Schritte teilen das Canvas in mehrere mögliche Pfade auf.

- Decision-Split-Schritt
- Zielgruppenpfad-Schritt

Wenn ein Priorisierungspfad Verzweigungsschritte enthält, geht Braze davon aus, dass alle Pfade möglich sind, und berücksichtigt alle parallelen Nachrichtenschritte auf unterstützten Kanälen für die Priorisierung. Da Frequency-Capping-Regeln kanalspezifisch sein können, werden parallele Nachrichtenschritte bei Bedarf nach Kanal dedupliziert.

Wenn beispielsweise ein Zweig E-Mail senden kann und ein anderer Zweig ebenfalls E-Mail senden kann, behandelt Braze diese als einen einzigen möglichen E-Mail-Versand für die vorausschauende Priorisierung. Wenn ein weiterer Zweig Push senden kann, berücksichtigt Braze diesen möglichen Push-Versand separat.

Für Canvas-Nachrichtenschritte, die intelligentes Timing verwenden, sagt Braze den Zeitpunkt bestmöglich vorher, bis die Nutzer:innen diesen Schritt tatsächlich erreichen. Sobald die Nutzer:innen den Schritt mit intelligentem Timing betreten und Braze den nutzerspezifischen Sendezeitpunkt berechnet, verwendet die Nachrichtenpriorisierung diesen berechneten Sendezeitpunkt für den aktuellen Schritt. Auf deterministischen Pfaden spiegelt Braze diesen aktualisierten Zeitpunkt auch in nachfolgenden Nachrichtenschritten wider, wenn deren erwartete Sendezeitpunkte bestimmt werden.

Content-Optimizer-Schritte werden wie Nachrichtenschritte behandelt, da sie immer auf einem bestimmten Kanal senden. Wiederholungsfenster gelten jedoch nicht für Content-Optimizer-Schritte, da eine Wiederholung das Experiment beeinträchtigen würde. Andere unterstützte Canvas-Nachrichtenschritte können Wiederholungsfenster verwenden. Canvas-Schritte auf nicht unterstützten Kanälen nehmen nicht an der Nachrichtenpriorisierung teil.

## Frequency-Capping {#frequency-caps}

Die Nachrichtenpriorisierung arbeitet innerhalb Ihrer bestehenden Frequency-Capping-Regeln. Eine priorisierte Nachricht kann nur gesendet werden, wenn:

1. Die relevante Frequency-Capping-Regel für diese:n Nutzer:in noch nicht erreicht wurde, und
2. Das Senden dieser Nachricht nicht dazu führen würde, dass die Nutzer:innen ein Cap erreichen, bevor eine spätere Nachricht mit höherer Priorität gesendet werden kann.

Nachrichten, die keinem Frequency-Capping unterliegen, sind nicht für die Nachrichtenpriorisierung berechtigt. Wenn Sie möchten, dass eine Nachricht immer gesendet wird, deaktivieren Sie das Frequency-Capping für diese Nachricht. Dadurch wird sie auch aus der Nachrichtenpriorisierung entfernt.

### Für unterstützte Campaigns und Canvas-Schritte {#for-supported-campaigns-and-canvas-steps}

Um für die Nachrichtenpriorisierung berechtigt zu sein, muss die Campaign oder der Canvas-Schritt einen unterstützten Kanal verwenden und innerhalb Ihrer Frequency-Capping-Konfiguration ausgewertet werden.

![Ein Beispiel für eine Frequency-Capping-Regel.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Frequency-Capping-Regeln {#frequency-capping-rules}

Braze optimiert die Priorität innerhalb Ihrer bestehenden Frequency-Capping-Regeln. Priorisierte Nachrichten werden nur verglichen, wenn sie derselben anwendbaren Frequency-Capping-Regel unterliegen.

Beispielsweise können zwei E-Mail-Campaigns, die auf dieselbe E-Mail-Frequency-Capping-Regel angerechnet werden, gegeneinander priorisiert werden. Eine E-Mail-Campaign mit niedrigerer Priorität wird nicht zugunsten einer SMS-Nachricht mit höherer Priorität herabgestuft, es sei denn, beide Nachrichten werden auf dieselbe Frequency-Capping-Regel angerechnet.

Sie können kanalspezifische Frequency-Capping-Regeln, kategoriespezifische Regeln, Tag-Filter oder Regeln verwenden, die für jeden Kanal gelten. Die Nachrichtenpriorisierung arbeitet mit den Regeln, die für Ihre aktivierten Nachrichten gelten.

Sie können Frequency-Capping-Regeln nach Kategorie erstellen, um zu verwalten, wie viele Nachrichten Nutzer:innen aus einer bestimmten Kategorie erhalten. So wird verhindert, dass eine Kategorie mit hoher Priorität zu viele Nachrichten sendet. Wählen Sie **Nachrichtenpriorisierungs-Kategorie** unter **Zusätzliche Filter** und wählen Sie eine Kategorie aus dem Dropdown-Menü.

![Ein Beispiel für die Frequency-Capping-Regel mit dem Dropdown-Feld „Kategorie“ zur Auswahl von P2 oder P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Nachrichten außerhalb der Nachrichtenpriorisierung teilen sich die Frequency-Cap-Limits mit priorisierten Nachrichten, sodass selbst eine Nachricht mit hoher Priorität aufgrund einer Nachricht außerhalb der Nachrichtenpriorisierung abgebrochen werden kann.

## Beispiele {#examples}

### Campaign mit höherer Priorität versus Campaign mit niedrigerer Priorität {#higher-priority-campaign-versus-lower-priority-campaign}

Angenommen, Nutzer:innen sind am selben Tag für zwei E-Mail-Campaigns berechtigt, und beide Campaigns werden auf dieselbe Frequency-Capping-Regel angerechnet. Wenn die Campaign mit höherer Priorität voraussichtlich später an diesem Tag gesendet wird, kann Braze die Campaign mit niedrigerer Priorität herabstufen, damit die Campaign mit höherer Priorität stattdessen gesendet werden kann. Wenn die Campaign mit niedrigerer Priorität ein Wiederholungsfenster hat, kann Braze sie später erneut versuchen.

### Aktionsbasierte Campaign mit höherer Priorität versus Nachricht mit niedrigerer Priorität {#higher-priority-action-based-campaign-versus-lower-priority-message}

Angenommen, Nutzer:innen triggern eine aktionsbasierte Campaign mit höherer Priorität, die zwei Stunden später gesendet werden soll. Während dieser Verzögerung kann Braze diese bevorstehende aktionsbasierte Campaign berücksichtigen, wenn entschieden wird, ob eine andere priorisierte Nachricht zuerst gesendet werden soll. So wird verhindert, dass eine Nachricht mit niedrigerer Priorität jetzt gesendet wird, wenn die aktionsbasierte Campaign mit höherer Priorität voraussichtlich bald gesendet wird.

### Canvas mit höherer Priorität versus Campaign mit niedrigerer Priorität {#higher-priority-canvas-versus-lower-priority-campaign}

Angenommen, Nutzer:innen sind für eine Campaign mit niedrigerer Priorität berechtigt, sollen aber auch später an diesem Tag eine Canvas-Nachricht mit höherer Priorität erhalten. Wenn Braze diese zukünftige Canvas-Nachricht bereits auswerten kann, kann es die Campaign mit niedrigerer Priorität herabstufen, damit die Canvas-Nachricht mit höherer Priorität stattdessen gesendet werden kann.

### Canvas mit höherer Priorität und Grenzschritt versus Campaign mit niedrigerer Priorität {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Angenommen, ein Canvas mit höherer Priorität enthält einen Aktionspfad-Schritt, ein Experiment oder eine personalisierte Verzögerung vor seinem nächsten Nachrichtenschritt. Bis die Nutzer:innen diesen Schritt erreichen und passieren, schaut Braze nicht über diesen Schritt hinaus zur nachgelagerten Canvas-Nachricht mit höherer Priorität. In diesem Fall kann eine Campaign mit niedrigerer Priorität trotzdem zuerst gesendet werden.

### Canvas mit höherer Priorität und Verzweigung versus Nachricht mit niedrigerer Priorität {#higher-priority-branching-canvas-versus-lower-priority-message}

Angenommen, ein Canvas mit höherer Priorität kann je nach Zweig, dem die Nutzer:innen folgen, unterschiedliche Nachrichten senden. Braze bewertet diese möglichen zukünftigen Pfade konservativ beim Vergleich von Nachrichten. So wird verhindert, dass eine Nachricht mit niedrigerer Priorität jetzt gesendet wird, wenn ein Canvas-Zweig mit höherer Priorität dasselbe Frequency-Cap später nutzen könnte.

### Canvas-Schritt mit intelligentem Timing und nachgelagerte Schritte {#canvas-intelligent-timing-step-and-downstream-steps}

Angenommen, Nutzer:innen betreten einen Canvas-Nachrichtenschritt mit höherer Priorität, der intelligentes Timing verwendet. Sobald Braze den Sendezeitpunkt für diese:n Nutzer:in für den Schritt mit intelligentem Timing berechnet, verwendet die Nachrichtenpriorisierung diesen nutzerspezifischen Sendezeitpunkt für den aktuellen Schritt und für spätere Nachrichtenschritte auf demselben deterministischen Pfad. So kann Braze nachgelagerte Canvas-Nachrichten mit anderen priorisierten Sendungen anhand des aktualisierten Zeitpunkts vergleichen, anstatt nur die frühere Pfadschätzung zu verwenden.

## Einschränkungen {#limitations}

Die Nachrichtenpriorisierung hat folgende Einschränkungen:

- Bis zu 20 Kategorien pro Workspace
- Bis zu 10 Priorisierungsregeln pro Workspace
- Bis zu 25 aktive, für die Priorisierung aktivierte geplante Elemente gleichzeitig
- Bis zu 25 aktive, für die Priorisierung aktivierte aktionsbasierte Elemente gleichzeitig
- Wiederholungsfenster von bis zu 3 Tagen

Das Limit für geplante Elemente ist eine kombinierte Gesamtzahl aus geplanten Campaigns und geplanten aktivierten Canvases. Das Limit für aktionsbasierte Elemente ist eine kombinierte Gesamtzahl aus aktionsbasierten Campaigns und aktionsbasierten aktivierten Canvases.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie werden Gleichstände zwischen Nachrichten in derselben Kategorie aufgelöst? {#how-are-ties-broken-between-messages-in-the-same-category}

Bei der Priorisierung zweier Campaigns in derselben Kategorie räumt Braze der Campaign mit dem früheren Sendezeitpunkt eine höhere Priorität ein. Wenn ein Wiederholungsfenster konfiguriert ist, verwendet Braze das Ende dieses Wiederholungsfensters beim Vergleich von Campaigns innerhalb derselben Prioritätsregel. Bei wiederkehrenden Campaigns wird die Sendezeit als das nächste Vorkommen ab Mitternacht in Unternehmenszeit berechnet. Bei Campaigns, die in Ortszeit geplant sind, nimmt Braze eine Sendezeit in Unternehmenszeit an.

Für Canvases in derselben Kategorie verwendet Braze den Canvas-Eintrittszeitpunkt als Tiebreaker, sodass alle Schritte im selben Canvas dieselbe relative Priorität gegenüber anderen Campaigns und Canvases beibehalten.

### Wie kann ich sicherstellen, dass eine Nachricht immer gesendet wird? {#how-can-i-make-sure-a-message-is-always-sent}

Es kann Szenarien geben, in denen Sie möchten, dass eine Nachricht immer gesendet wird, z. B. bei transaktionalen oder rechtlichen Benachrichtigungen. In diesem Fall sollten Sie die Nachricht vom Frequency-Capping abmelden, was sie auch für die Nachrichtenpriorisierung nicht berechtigt macht. Dadurch wird die Nachricht immer dann gesendet, wenn sie geplant oder getriggert wird, ohne Berücksichtigung anderer Sendungen.

### Wann werden Nachrichten tatsächlich priorisiert? Gibt es einen Zeitplan? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Jede Nachricht wird basierend auf ihrem erwarteten Sendezeitpunkt priorisiert. Es gibt keinen universellen Auswertungszeitpunkt für priorisierte Nachrichten.

### Wie sagt Braze vorher, wann eine zukünftige Nachricht gesendet wird? {#how-does-braze-predict-when-a-future-message-sends}

Braze sagt den zukünftigen Sendezeitpunkt für jeden Nachrichtentyp unterschiedlich vorher:

- **Geplante Campaigns:** Braze verwendet den Zeitpunkt, zu dem jede Campaign voraussichtlich gesendet wird. Für geplante Campaigns, die intelligentes Timing verwenden, nutzt Braze den optimalen Sendezeitpunkt jeder:jedes Nutzer:in für dieses Campaign-Vorkommen.
- **Aktionsbasierte Campaigns:** Braze verwendet den Zeitpunkt, zu dem jede getriggerte Nachricht voraussichtlich gesendet wird, einschließlich einer konfigurierten Verzögerung zwischen Trigger und Versand.
- **Canvas-Schritte:** Braze verwendet den Canvas-Eintritt oder die aktuelle Canvas-Position der Nutzer:innen plus den Zeitpunkt der nachgelagerten Schritte. Für Canvas-Nachrichtenschritte, die intelligentes Timing verwenden, nutzt Braze nach dem Eintritt der Nutzer:innen in diesen Schritt den nutzerspezifischen Sendezeitpunkt, den es für diese:n Nutzer:in berechnet. Für nachfolgende Nachrichtenschritte auf demselben deterministischen Priorisierungspfad verwendet Braze diesen Sendezeitpunkt des intelligenten Timings bei der Bestimmung späterer erwarteter Sendezeitpunkte. Bevor Nutzer:innen den Schritt mit intelligentem Timing erreichen, bleibt die Vorhersage bestmöglich.

### Meine Nachricht war bereits zum Senden geplant, wurde aber aufgrund von Rate-Limiting oder anderen Verzögerungen noch nicht gesendet. Was bedeutet das für die Priorisierung anderer Campaigns? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Braze geht davon aus, dass Ihre Nachricht zum ursprünglich geplanten Zeitpunkt gesendet wurde, wenn sie noch verarbeitet wird. Dies bestimmt, ob andere bevorstehende priorisierte Nachrichten gesendet werden sollen. Wenn die Nachricht letztendlich gesendet wird, verwendet Braze die tatsächliche Sendezeit.

### Meine Nachricht wurde priorisiert, aber in letzter Minute abgebrochen. Was bedeutet das für die Priorisierung? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Wenn eine Nachricht priorisiert wird, geht Braze davon aus, dass sie zum ursprünglich geplanten Zeitpunkt gesendet wurde. Generell empfehlen wir für die Nachrichtenpriorisierung nicht die Verwendung von Liquid-Abbrüchen. Wenn eine Nachricht aufgrund von [`abort_message`-Liquid-Logik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) abgebrochen wird, gehen wir davon aus, dass sie an diese:n Nutzer:in gesendet wurde, und priorisieren zukünftige Campaigns entsprechend.

Nehmen wir an, Sie haben zwei Nachrichten: Nachricht 1 und Nachricht 2. Wenn Nachricht 1 zugunsten einer zukünftigen Nachricht 2 mit höherer Priorität abgebrochen wird, garantiert dies nicht, dass Nachricht 2 tatsächlich gesendet wird. Nachricht 2 kann aus verschiedenen Gründen ebenfalls abgebrochen werden, darunter:

- Liquid-Abbruchnachrichten
- Die Nutzer:innen befinden sich nicht mehr im Segment
- Frequency-Caps aufgrund einer Nachricht außerhalb der Priorisierungsregeln

Wenn Nachricht 2 abgebrochen wird, gibt es keinen weiteren Versuch, Nachricht 1 zu senden.

Beachten Sie, dass Nutzer:innen eine Nachricht mit niedrigerer Priorität erhalten könnten, aber nicht eine Nachricht mit höherer Priorität für dieselbe Frequency-Capping-Regel, aus folgenden Gründen:

- Die Nachricht mit höherer Priorität wurde durch eine andere Regel einem Frequency-Cap unterworfen.
- Die Nachricht mit höherer Priorität stand im Konflikt mit einer anderen, zukünftigen Campaign mit noch höherer Priorität für eine andere Regel.
- Zum Zeitpunkt des Sendens der Nachricht mit niedrigerer Priorität befanden sich die Nutzer:innen nicht in der Zielgruppe für die Nachricht mit höherer Priorität.
- Beide Nachrichten hätten gesendet werden können, aber eine Nachricht außerhalb der Priorisierungseinrichtung wurde vor der Nachricht mit höherer Priorität gesendet.

### Wie beeinflussen Grenzschritte die Canvas-Priorisierung? {#how-do-boundary-steps-affect-canvas-prioritization}

Grenzschritte stoppen die Vorausschau durch das Canvas, bis die Nutzer:innen diesen Punkt im Canvas tatsächlich erreichen oder abschließen. Wenn beispielsweise eine Nachricht mit höherer Priorität nach einem Aktionspfad-Schritt, einer personalisierten Verzögerung oder einem Experimentschritt liegt, verwendet Braze diese nachgelagerte Nachricht nicht, um eine Campaign mit niedrigerer Priorität zu blockieren, bis die Nutzer:innen diesen Grenzschritt passiert haben.

### Wie funktioniert die Verzweigung bei der Canvas-Priorisierung? {#how-does-branching-work-in-canvas-prioritization}

Wenn ein Canvas Verzweigungspfade enthält, geht Braze davon aus, dass jeder Pfad möglich ist, und vergleicht das höchstmögliche zukünftige Sendevolumen nach Kanal. So wird vermieden, dass eine Nachricht mit niedrigerer Priorität jetzt gesendet wird, wenn ein Canvas-Pfad mit höherer Priorität dasselbe Frequency-Cap später nutzen könnte.

### Was passiert, wenn Nutzer:innen gleichzeitig mehrere Pfade durch ein priorisiertes Canvas haben? {#what-happens-if-a-user-has-multiple-paths-through-a-prioritized-canvas-at-the-same-time}

Braze behandelt jeden möglichen Pfad als potenziellen zukünftigen Pfad und bewertet die berechtigten Nachrichtenschritte auf diesen Pfaden unabhängig. Wenn mehrere Pfade auf demselben Kanal senden können, dedupliziert Braze diese möglichen Sendungen bei Bedarf nach Kanal.

### Wie funktioniert intelligentes Timing bei der Canvas-Priorisierung? {#how-does-intelligent-timing-work-in-canvas-prioritization}

Bevor Nutzer:innen einen Canvas-Nachrichtenschritt mit intelligentem Timing erreichen, sagt Braze den Zeitpunkt dieses Schritts bestmöglich vorher. Sobald die Nutzer:innen den Schritt betreten und Braze den nutzerspezifischen Sendezeitpunkt berechnet, verwendet die Nachrichtenpriorisierung diesen berechneten Sendezeitpunkt für den aktuellen Schritt und für nachfolgende Nachrichtenschritte auf demselben deterministischen Priorisierungspfad.

### Gibt es Berichts- oder Analytics-Funktionen speziell für die Nachrichtenpriorisierung? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Braze stellt Ereignisse zur Nachrichtenpriorisierung in Currents und im Daten-Sharing für unterstützte Kanäle bereit, darunter E-Mail, LINE, Push-Benachrichtigungen, SMS, Webhooks und WhatsApp. Dazu gehören Ereignisse für herabgestufte und durch Frequency-Capping begrenzte Nachrichten, die in der Tabelle `users.messages.<channel>.abort` protokolliert werden, sowie Wiederholungsereignisse, die anzeigen, wann eine Nachricht später innerhalb des konfigurierten Wiederholungsfensters erneut versucht wurde, protokolliert in der Tabelle `user_messages_<channel>_retry`.

Für Campaigns können Sie außerdem das Messaging-Diagnostics-Dashboard, die bestehenden täglichen Statistiken für herabgestufte und wiederholte Nachrichten sowie die bestehende [Braze-Berichtsfunktionalität]({{site.baseurl}}/user_guide/analytics/reporting) nutzen, um den Zustand und die Performance Ihrer priorisierten Campaigns und Canvases zu überwachen.