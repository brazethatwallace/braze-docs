---
article_title: Nachrichtenpriorisierung
permalink: /message_prioritization/
toc_headers: h2
description: "Dieser Referenzartikel beschreibt die übergeordnete Nachrichtenpriorisierung und wie Sie diese für Ihren Workspace konfigurieren."
---

# Nachrichtenpriorisierung {#message-prioritization}

> Verwenden Sie die Nachrichtenpriorisierung, um sicherzustellen, dass Ihre Nutzer:innen die Nachrichten erhalten, die für Ihr Unternehmen am wichtigsten sind – und nicht nur diejenigen, die zufällig zuerst gesendet werden.

{% alert important %}
Die Nachrichtenpriorisierung befindet sich derzeit in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Teilnahme an dieser Beta interessiert sind.<br><br>Dieser Artikel spiegelt die Version der Nachrichtenpriorisierung wider, die für das Produktionsrelease Ende Juli 2026 geplant ist. Einige hier beschriebene Verhaltensweisen sind möglicherweise noch nicht in allen Beta-Workspaces verfügbar.
{% endalert %}

## Warum Nachrichtenpriorisierung verwenden? {#why-use-message-prioritization}

Nutzer:innen können nur eine begrenzte Anzahl von Nachrichten erhalten, bevor das Volumen zum Problem wird. Die Nachrichten, die sie erreichen, sollten diejenigen sein, die für Ihr Unternehmen am wichtigsten sind. Die Nachrichtenpriorisierung stellt sicher, dass Ihre wertvollsten Nachrichten diesen begrenzten Platz gewinnen, anstatt dies dem Zufall zu überlassen.

Die meisten Teams steuern das Nachrichtenvolumen mit Frequency-Capping. Für sich allein ist Frequency-Capping ein grobes Instrument. Sobald Nutzer:innen ihr Limit erreicht haben, entscheidet der Sendezeitpunkt darüber, welche Nachrichten durchkommen – nicht die geschäftliche Bedeutung.

Eine weniger wertvolle Aktion, die zuerst ausgelöst wird, kann einen Platz belegen, den eine Kundenbindungs-Belohnung oder eine zeitkritische Nachricht später am Tag genutzt hätte. Teams umgehen dies oft mit separaten Begrenzungsregeln, manueller Zeitplanung und Ad-hoc-Filtern. Diese Ansätze erfordern ständige Pflege. Sie werden schwieriger zu verwalten, wenn sich Campaigns und Canvases ändern. Und sie können trotzdem nicht garantieren, dass die richtige Nachricht gewinnt.

Die Nachrichtenpriorisierung ändert die Frequency-Capping-Zuweisung von **„Wer zuerst kommt, mahlt zuerst“** zu **„geschäftsprioritätsbewusst“**: Sie legen fest, was wichtig ist, und Braze trifft die Sendeentscheidungen für Sie.

Die Nachrichtenpriorisierung bietet mehrere Vorteile:

- **Einmal festlegen, was wichtig ist:** Verwenden Sie Kategorien und priorisierte Regeln, um Ihre Prioritäten abzubilden – zum Beispiel „Kundenbindung“ vor „Bezahlte Partnerschaften“. Jeder Opt-in-Versand berücksichtigt diese Rangfolge automatisch.
- **Vorausschauende Entscheidungen:** Braze prognostiziert, was Nutzer:innen später erhalten könnten. Es kann eine Nachricht mit niedrigerer Priorität zurückhalten, um Kapazität für eine Nachricht mit höherer Priorität freizuhalten.
- **Funktioniert über Nachrichtentypen und Kanäle hinweg:** Geplante Campaigns, aktionsbasierte Campaigns und Canvas-Schritte konkurrieren in einem gemeinsamen priorisierten Pool innerhalb Ihres geteilten Frequency-Cappings.
- **Wiederholungsfenster:** Eine herabgestufte Nachricht kann erneut versucht werden, wenn Kapazität frei wird. Dies verbessert den Nachrichtenmix, ohne Sendungen mit niedrigerer Priorität vollständig zu verwerfen.

Das Ergebnis ist dasselbe begrenzte Sendevolumen, automatisch den Nachrichten zugewiesen, die am wichtigsten sind.

Die Nachrichtenpriorisierung ist besonders wertvoll für Absender mit hohem Volumen, die regelmäßig an Frequency-Capping-Grenzen stoßen. Sie funktioniert am besten, wenn der Nachrichtenwert klar differenziert ist – zum Beispiel Kundenbindungs- oder umsatzfördernde Nachrichten im Vergleich zu routinemäßigen Aktionen.

## So funktioniert es {#how-it-works}

Verwenden Sie die Nachrichtenpriorisierung, um [Kategorien](#categories) und [Priorisierungsregeln](#prioritization-rules) zu erstellen, die festlegen, in welcher Reihenfolge Ihre Nachrichten gesendet werden.

Um diese Einstellungen zu verwalten, gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung**. Nur Administrator:innen können die übergeordneten Einstellungen der Nachrichtenpriorisierung konfigurieren. Nutzer:innen benötigen die Berechtigung „View Message Prioritization“, um die Einstellungen in diesem Bereich anzuzeigen, und die Berechtigung „Edit Message Prioritization“, um sie zu bearbeiten.

Beispiel: Eine Beauty-Marke, die E-Mail-Aktionen für bezahlte Partnerschaften und Kundenbindungs-Programme verwaltet, nutzt die Nachrichtenpriorisierung, um zwei Kategorien zu erstellen: „Bezahlte Partnerschaften“ und „Kundenbindung“. Die Marke ordnet diese Kategorien nach geschäftlicher Bedeutung. Während der Weihnachtssaison wird „Kundenbindung“ an erste und „Bezahlte Partnerschaften“ an zweite Stelle gesetzt, um langjährige Mitglieder zu priorisieren.

![Ein Beispiel für Priorisierungsregeln für zwei Kategorien: Bezahlte Partnerschaften und Kundenbindung.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

Zum Sendezeitpunkt vergleicht Braze die zu sendende Nachricht mit anderen Nachrichten, die die Nutzer:innen möglicherweise erhalten und die für die Priorisierung aktiviert sind, eine Prioritätskategorie zugewiesen haben und innerhalb desselben Frequency-Capping-Fensters auf dieselbe Frequency-Capping-Regel angerechnet werden. Wenn das Senden der aktuellen Nachricht verhindern würde, dass eine Nachricht mit höherer Priorität später gesendet wird, stuft Braze die Nachricht mit niedrigerer Priorität herab. Je nach konfiguriertem Wiederholungsfenster wird diese Nachricht mit niedrigerer Priorität entweder später erneut versucht oder gar nicht gesendet.

Die Nachrichtenpriorisierung kann Folgendes auswerten:

- Geplante Campaigns
- Aktionsbasierte Campaigns
- Canvases

Derzeit werden API-getriggerte Campaigns oder Canvases von der Nachrichtenpriorisierung nicht unterstützt und nehmen nicht an der Priorisierung teil.

Braze nutzt seine Vorhersage, wann jede Nachricht voraussichtlich gesendet wird, um zu bewerten, ob das Senden einer Nachricht jetzt das Senden einer Nachricht mit höherer Priorität zu einem späteren Zeitpunkt verhindern könnte. Weitere Informationen dazu, wie Braze den zukünftigen Sendezeitpunkt für Campaigns und Canvases vorhersagt, finden Sie unter [Wie sagt Braze vorher, wann eine zukünftige Nachricht gesendet wird?](#how-does-braze-predict-when-a-future-message-sends)

### Unterstützte Nachrichtenkanäle {#supported-message-channels}

Die Nachrichtenpriorisierung unterstützt dieselben Kanäle wie Frequency-Capping:

- Push-Benachrichtigungen
- E-Mail
- SMS
- Webhooks
- WhatsApp
- LINE

Für die Priorisierung und das Frequency-Capping werden iOS-Push, Android-Push, Web-Push und andere Push-Benachrichtigungsplattformen als ein gemeinsamer Push-Kanal behandelt, nicht als separate Kanäle.

Diese Kanäle sind für die Nachrichtenpriorisierung nicht geeignet, da sie keinem Frequency-Capping unterliegen:

- Content Cards
- In-App-Nachrichten
- Banner

In-App-Nachrichten und Banner verwenden ihre eigenen Prioritätseinstellungen, um zu entscheiden, welche Nachricht angezeigt wird, wenn mehrere Nachrichten um denselben Trigger oder dieselbe Platzierung konkurrieren. Für In-App-Nachrichten siehe [Priorität auswählen]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority). Für Banner siehe [Banner-Priorität]({{site.baseurl}}/user_guide/channels/banners#priority).

Wenn eine Campaign oder ein Canvas-Schritt nur nicht geeignete Kanäle verwendet, nimmt sie bzw. er nicht an der Priorisierung teil.

## Kategorien {#categories}

Priorisierungsregeln basieren auf einer Rangfolge von Kategorien, bei denen es sich um Labels handelt, die Sie einer bestimmten Campaign oder einem Canvas zuweisen können (ähnlich wie ein [Tag]({{site.baseurl}}/user_guide/administrative/app_settings/tags)). Es gibt eine Obergrenze für die Anzahl der Kategorien, die Sie zu einem bestimmten Zeitpunkt erstellen können. Wenden Sie sich an Ihren Account Manager, wenn Sie ein höheres Limit wünschen.

So fügen Sie eine neue Kategorie hinzu:

1. Gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung** > **Kategorien**.
2. Wählen Sie **Neue Kategorie erstellen** aus.

![Der Button „Neue Kategorie erstellen“ im Bereich „Nachrichtenpriorisierung“.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Geben Sie der Kategorie einen Namen und eine optionale Beschreibung.
4. Wählen Sie **Kategorie erstellen** aus.

![Eine Beispielkategorie mit dem Namen „P3“ und der Beschreibung „This is my third highest priority category.“]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Um eine Kategorie zu bearbeiten oder zu löschen, wählen Sie das Menü <i class="fas fa-ellipsis-vertical" aria-label="Mehr Optionen"></i> aus.

## Priorisierungsregeln {#prioritization-rules}

Nachdem Ihre Kategorien eingerichtet sind, können Sie sie in einer Reihe von Priorisierungsregeln ordnen. Regeln werden in absteigender Prioritätsreihenfolge eingestuft. Es gibt eine Obergrenze für die Anzahl der Priorisierungsregeln, die Sie zu einem bestimmten Zeitpunkt erstellen können. Wenden Sie sich an Ihren Account Manager, wenn Sie ein höheres Limit wünschen.

1. Gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung** > **Priorisierungsregeln**, um Ihre Regeln zu konfigurieren.

![Abschnitt „Priorisierungsregeln“ ohne bisher festgelegte Prioritäten.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Wählen Sie **Regel hinzufügen** aus.
3. Wählen Sie eine Kategorie aus dem Dropdown-Menü aus.

![Priorisierungsregel „Priorität 1“ mit P1 als ausgewählter Kategorie.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Fügen Sie weitere Regeln hinzu, indem Sie **+ Regel hinzufügen** unter Ihrer letzten Regel auswählen.

Um Regeln neu zu ordnen, wählen Sie das <i class="fa-solid fa-grip-vertical" aria-label="Regel ziehen und ablegen"></i>-Symbol einer Regel aus und ziehen Sie es an die gewünschte Position. Um eine Regel zu löschen, wählen Sie das <i class="fas fa-ellipsis-vertical" aria-label="Weitere Optionen"></i>-Menü und dann **Regel löschen** aus.

Vergessen Sie nicht, **Speichern** auszuwählen, damit Ihre Änderungen übernommen werden.

## Frequency-Capping {#frequency-caps}

Die Nachrichtenpriorisierung arbeitet innerhalb Ihrer bestehenden Frequency-Capping-Regeln. Damit eine Campaign oder ein Canvas-Schritt für die Priorisierung infrage kommt, muss ein unterstützter Kanal verwendet werden und die Frequency-Capping-Konfiguration greifen. Nachrichten, die nicht dem Frequency-Capping unterliegen, kommen nicht für die Nachrichtenpriorisierung infrage. Wenn eine Nachricht immer gesendet werden soll, nehmen Sie sie vom Frequency-Capping aus. Dadurch wird sie auch aus der Nachrichtenpriorisierung entfernt.

Eine priorisierte Nachricht wird nur gesendet, wenn:

1. Die relevante Frequency-Capping-Regel für diese:n Nutzer:in noch nicht erreicht wurde, und
2. das Senden dieser Nachricht nicht dazu führen würde, dass die:der Nutzer:in ein Limit erreicht, bevor eine spätere Nachricht mit höherer Priorität gesendet werden kann.

![Ein Beispiel für eine Frequency-Capping-Regel.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

Sie können kanalspezifische Frequency-Capping-Regeln, kategoriespezifische Regeln, Tag-Filter oder Regeln verwenden, die für jeden Kanal gelten. Die Nachrichtenpriorisierung funktioniert mit allen Regeln, die für Ihre aktivierten Nachrichten gelten.

Sie können auch Frequency-Capping-Regeln nach Kategorie erstellen, um zu steuern, wie viele Nachrichten Nutzer:innen aus einer bestimmten Kategorie erhalten. Dies verhindert, dass eine Kategorie mit hoher Priorität zu viele Nachrichten sendet. Wählen Sie **Message prioritization category** unter **Additional filters** aus und wählen Sie eine Kategorie aus dem Dropdown-Menü.

![Ein Beispiel für die Frequency-Capping-Regel mit dem Dropdown-Feld „Category“ zur Auswahl von P2 oder P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

## Opt-in {#opting-in}

### Campaign-Opt-in

Um eine Campaign für die Priorisierung anzumelden, aktivieren Sie das Kontrollkästchen **Opt-in to Message Prioritization** in den Zustellungseinstellungen der Campaign.

![Das Kontrollkästchen für „Opt-in to Message Prioritization“.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Weisen Sie die Campaign anschließend einer Kategorie zu, indem Sie eine aus dem **Category**-Dropdown auswählen.

![Das Dropdown für die Nachrichtenpriorisierungs-Kategorie in den Zustellungseinstellungen einer Campaign.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

Die Nachrichtenpriorisierung unterstützt geplante Campaigns und aktionsbasierte Campaigns. API-getriggerte Campaigns werden nicht unterstützt.

### Canvas-Opt-in

Das Canvas-Opt-in funktioniert ähnlich wie bei Campaigns. Um ein Canvas für die Nachrichtenpriorisierung anzumelden, aktivieren Sie die Nachrichtenpriorisierung in den Canvas-Einstellungen und weisen Sie das Canvas einer Kategorie zu. Alle Schritte im Canvas teilen sich diese Kategorie und dieselbe Prioritätsstufe, was bedeutet, dass Sie die Priorität nicht einzeln pro Schritt festlegen können.

Die Nachrichtenpriorisierung unterstützt geplante Canvases und aktionsbasierte Canvases. API-getriggerte Canvases werden nicht unterstützt.

## Intelligentes Timing {#intelligent-timing}

Beim intelligenten Timing sendet Braze eine Nachricht zum optimalen Sendezeitpunkt jeder einzelnen Nutzer:in, sodass dieselbe Campaign oder derselbe Canvas-Nachrichtenschritt verschiedene Nutzer:innen zu unterschiedlichen Zeiten erreichen kann. Die Nachrichtenpriorisierung berücksichtigt dies: Anstatt davon auszugehen, dass die Nachricht zum geplanten Zeitpunkt an alle gesendet wird, ordnet sie die konkurrierenden Nachrichten einer Nutzer:in anhand des optimalen Sendezeitpunkts dieser Nutzer:in ein.

Für Campaigns und Canvas-Nachrichtenschritte, die intelligentes Timing verwenden, prognostiziert Braze den Sendezeitpunkt nach dem Best-Effort-Prinzip, bis der individuelle Sendezeitpunkt für jede Nutzer:in berechnet ist. Bei Campaigns verwendet die Nachrichtenpriorisierung den optimalen Sendezeitpunkt der Nutzer:in für das aktuelle Vorkommen, wenn die Campaign mit den anderen priorisierten Nachrichten dieser Nutzer:in verglichen wird. Bei wiederkehrenden Campaigns mit intelligentem Timing verwendet Braze den für dieses Vorkommen gewählten optimalen Sendezeitpunkt.

Bei Canvas-Nachrichtenschritten aktualisiert Braze diese Prognose, sobald die Nutzer:in den Schritt betritt und Braze den optimalen Sendezeitpunkt dieser Nutzer:in für den Schritt berechnet. Die Nachrichtenpriorisierung verwendet diesen berechneten Sendezeitpunkt für den aktuellen Schritt. Auf deterministischen Pfaden (Pfade ohne Verzweigung, bei denen die Schrittabfolge festgelegt ist) berücksichtigt Braze dieses aktualisierte Timing auch in den nachfolgenden Nachrichtenschritten bei der Bestimmung ihrer voraussichtlichen Sendezeitpunkte.

## Wiederholungsfenster {#retry-windows}

Ein Wiederholungsfenster ermöglicht es Nachrichten mit Opt-in, die Zustellung über eine begrenzte Anzahl von Tagen erneut zu versuchen, wenn der erste Versuch keine ausreichend hohe Priorität für den Versand hat. Die maximale Länge des Wiederholungsfensters hängt von Ihrer Braze-Plattform-Edition ab. An jedem darauffolgenden Tag wird die Nachricht zur selben Zeit, zu der sie ursprünglich geplant oder getriggert wurde, erneut versucht. Wenn die Nachricht nach dem letzten Tag im Wiederholungsfenster immer noch nicht gesendet wurde, wird kein weiterer Versuch unternommen und die Nachricht wird dauerhaft herabgestuft.

Bei wiederkehrenden geplanten Campaigns muss das Wiederholungsfenster kürzer sein als die minimale Zeit zwischen den Sendungen dieser Campaign. Wiederholungen erfolgen immer einen Tag nach der ursprünglichen Sendezeit, auch wenn die Campaign an diesem Tag normalerweise nicht zum Senden geplant ist. Wenn Sie beispielsweise eine Campaign haben, die jeden Montag und Mittwoch sendet, erfolgt der Wiederholungsversuch am Dienstag, sodass das Wiederholungsfenster auf einen Tag eingestellt werden muss. Wenn Sie eine Campaign haben, die jeden Montag, Mittwoch und Freitag sendet, und der Freitagsversand mit einem eintägigen Wiederholungsfenster wiederholt wird, erfolgt der Wiederholungsversuch am Samstag, nicht am Montag.

![Die Einstellung „Wiederholungsfenster“ auf 1 Tag eingestellt.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Bei aktionsbasierten Campaigns basieren Wiederholungen auf dem Zeitpunkt, zu dem die getriggerte Nachricht ursprünglich gesendet werden sollte.

Aktionsbasierte Campaigns, die Ausnahme-Events verwenden, unterstützen keine Wiederholungsfenster.

Wiederholungsfenster für Canvas-Nachrichten werden auf Schrittebene konfiguriert. Wenn bei unterstützten Canvas-Messaging-Schritten ein Canvas-Nachrichtenschritt herabgestuft wird und ein Wiederholungsfenster konfiguriert ist, kann Braze diesen Schritt später innerhalb seines Wiederholungsfensters erneut versuchen.

## Wie Braze Nachrichten bewertet {#how-braze-evaluates-messages}

{% alert tip %}
Sie müssen nicht alles in diesem Abschnitt verstehen, um die Nachrichtenpriorisierung zu nutzen. Sobald Sie Ihre Kategorien und Regeln festgelegt und Ihre Nachrichten aktiviert haben, bewertet und priorisiert Braze Nachrichten automatisch und gibt sein Bestes, die wichtigsten zu senden. Die Details hier sind für den Fall gedacht, dass Sie verstehen möchten, wie diese Entscheidungen getroffen werden.
{% endalert %}

Wenn Nutzer:innen für mehrere priorisierte Nachrichten infrage kommen, bewertet Braze aktivierte Campaigns und infrage kommende Canvas-Nachrichtenschritte gemeinsam auf unterstützten Kanälen.

Für Campaigns umfasst dies infrage kommende geplante und aktionsbasierte Sendungen.

Für Canvases umfasst dies:

- Zukünftig geplante Canvases, für die Nutzer:innen infrage kommen
- Canvases, in denen sich Nutzer:innen aktuell befinden

Die Canvas-Priorisierung ist kein Alles-oder-Nichts-Prinzip. Eine höher priorisierte Campaign kann dazu führen, dass ein Canvas-Schritt herabgestuft wird, während spätere infrage kommende Schritte in demselben Canvas je nach Kategorierang, Sendezeitpunkt und Frequency-Capping-Regeln weiterhin gesendet werden können.

Braze vergleicht priorisierte Nachrichten nur dann, wenn sie dieselbe geltende Frequency-Capping-Regel teilen. Zum Beispiel können zwei E-Mail-Campaigns, die auf dieselbe E-Mail-Frequency-Capping-Regel angerechnet werden, gegeneinander priorisiert werden, aber eine niedriger priorisierte E-Mail-Campaign wird nicht zugunsten einer höher priorisierten SMS-Nachricht herabgestuft, es sei denn, beide werden auf dieselbe Regel angerechnet. Nachrichten außerhalb der Nachrichtenpriorisierung teilen diese Frequency-Cap-Limits ebenfalls, sodass selbst eine hoch priorisierte Nachricht aufgrund einer Nachricht außerhalb der Nachrichtenpriorisierung abgebrochen werden kann.

Braze bewertet Campaigns und Canvases unterschiedlich, da ein Canvas sich verzweigen und über die Zeit entfalten kann.

### Campaigns bewerten {#evaluating-campaigns}

Braze vergleicht jede infrage kommende Campaign-Nachricht anhand des Zeitpunkts, zu dem die Nachricht voraussichtlich gesendet wird.

### Canvases bewerten {#evaluating-canvases}

Um ein Canvas zu bewerten, führt Braze einen **Look-Ahead** durch: Es durchläuft das Canvas von einem Startpunkt aus, um vorherzusagen, welche zukünftigen Nachrichten Nutzer:innen erhalten könnten und wann. Der Look-Ahead beginnt bei:

- Canvas-Entry, für zukünftig geplante Canvases
- Dem aktuellen Schritt der Nutzer:innen, wenn sie sich bereits im Canvas befinden

Während des Look-Aheads behandelt Braze jeden Typ von Canvas-Schritt unterschiedlich. Der Schritttyp bestimmt, ob der Look-Ahead ihn zählt, überspringt, dort stoppt oder sich auf mehrere Pfade aufteilt:

| Schrittkategorie | Auswirkung auf den Look-Ahead |
|---|---|
| Nachrichtenschritte | Werden als infrage kommende Nachrichten für die Priorisierung gezählt |
| Fortsetzungsschritte | Werden übersprungen; der Look-Ahead läuft durch sie hindurch |
| Grenzschritte | Der Look-Ahead stoppt, bis Nutzer:innen den Schritt passiert haben |
| Verzweigungsschritte | Der Look-Ahead folgt jedem möglichen Pfad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvases bewerten" }

#### Nachrichtenschritte {#messaging-steps}

Diese Schritte werden für die Priorisierung gezählt und der Menge infrage kommender Nachrichten hinzugefügt, wenn sie auf einem unterstützten Kanal senden.

- Nachrichtenschritt
- Content-Optimizer-Schritt

#### Fortsetzungsschritte {#continuation-steps}

Diese Schritte werden für die Priorisierung ignoriert und beeinflussen den Look-Ahead nicht.

- Context-Update-Schritt
- User-Update-Schritt
- Audience-Sync-Schritt
- Feature-Flag-Schritt
- Verzögerungsschritt mit fester Verzögerung

#### Grenzschritte {#boundary-steps}

Braze stoppt den Look-Ahead an diesen Schritten, bis Nutzer:innen tatsächlich im Canvas durch sie hindurchgehen.

- Verzögerungsschritt mit personalisierter Verzögerung
- Verzögerungsschritt, der auf einen Verzweigungsschritt folgt
- Aktionspfad-Schritt
- Experimentschritt

#### Verzweigungsschritte {#branching-steps}

Diese Schritte teilen das Canvas in mehrere mögliche Pfade auf.

- Decision-Split-Schritt
- Zielgruppenpfad-Schritt

Wenn ein Priorisierungspfad Verzweigungsschritte enthält, geht Braze davon aus, dass alle Pfade möglich sind, und berücksichtigt alle parallelen Nachrichtenschritte auf unterstützten Kanälen für die Priorisierung. Da Frequency-Capping-Regeln kanalspezifisch sein können, werden parallele Nachrichtenschritte bei Bedarf nach Kanal dedupliziert.

Wenn beispielsweise ein Zweig E-Mail senden kann und ein anderer Zweig ebenfalls E-Mail senden kann, behandelt Braze diese während des Look-Aheads als einen einzigen möglichen E-Mail-Versand. Wenn ein weiterer Zweig Push senden kann, berücksichtigt Braze diesen möglichen Push-Versand separat.

Für Canvas-Nachrichtenschritte, die intelligentes Timing verwenden, nutzt Braze die berechnete Sendezeit jeder Nutzer:in, sobald sie den Schritt erreicht. Weitere Details finden Sie unter [Intelligentes Timing](#intelligent-timing).

Content-Optimizer-Schritte werden wie Nachrichtenschritte behandelt, da sie immer auf einem bestimmten Kanal senden. Wiederholungsfenster gelten jedoch nicht für Content-Optimizer-Schritte, da eine Wiederholung das Experiment beeinträchtigen würde. Andere unterstützte Canvas-Nachrichtenschritte können Wiederholungsfenster verwenden. Canvas-Schritte auf nicht unterstützten Kanälen nehmen nicht an der Nachrichtenpriorisierung teil.

## Beispiele {#examples}

### Campaign mit höherer Priorität gegenüber Campaign mit niedrigerer Priorität {#higher-priority-campaign-versus-lower-priority-campaign}

Angenommen, ein:e Nutzer:in ist am selben Tag für zwei E-Mail-Campaigns berechtigt, und beide Campaigns zählen für dieselbe Frequency-Capping-Regel. Wenn die Campaign mit höherer Priorität voraussichtlich später an diesem Tag gesendet wird, kann Braze die Campaign mit niedrigerer Priorität herabstufen, damit die Campaign mit höherer Priorität stattdessen gesendet werden kann. Wenn die Campaign mit niedrigerer Priorität ein Wiederholungsfenster hat, kann Braze sie später erneut versuchen.

### Aktionsbasierte Campaign mit höherer Priorität gegenüber Nachricht mit niedrigerer Priorität {#higher-priority-action-based-campaign-versus-lower-priority-message}

Angenommen, ein:e Nutzer:in triggert eine aktionsbasierte Campaign mit höherer Priorität, die so eingestellt ist, dass sie zwei Stunden später gesendet wird. Während dieser Verzögerung kann Braze diese bevorstehende aktionsbasierte Campaign berücksichtigen, wenn entschieden wird, ob eine andere priorisierte Nachricht zuerst gesendet werden soll. Dies hilft zu verhindern, dass eine Nachricht mit niedrigerer Priorität jetzt gesendet wird, wenn die aktionsbasierte Campaign mit höherer Priorität voraussichtlich bald gesendet wird.

### Canvas mit höherer Priorität gegenüber Campaign mit niedrigerer Priorität {#higher-priority-canvas-versus-lower-priority-campaign}

Angenommen, ein:e Nutzer:in ist für eine Campaign mit niedrigerer Priorität berechtigt, wird aber voraussichtlich auch eine Canvas-Nachricht mit höherer Priorität später an diesem Tag erhalten. Wenn Braze diese zukünftige Canvas-Nachricht bereits auswerten kann, kann die Campaign mit niedrigerer Priorität herabgestuft werden, damit die Canvas-Nachricht mit höherer Priorität stattdessen gesendet werden kann.

### Canvas mit höherer Priorität und einem Grenzschritt gegenüber Campaign mit niedrigerer Priorität {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Angenommen, ein Canvas mit höherer Priorität enthält einen Aktionspfad-Schritt, ein Experiment oder eine personalisierte Verzögerung vor dem nächsten Nachrichtenschritt. Bis der/die Nutzer:in diesen Schritt erreicht und passiert hat, schaut Braze nicht voraus auf die nachgelagerte Canvas-Nachricht mit höherer Priorität. In diesem Fall kann eine Campaign mit niedrigerer Priorität trotzdem zuerst gesendet werden.

### Verzweigtes Canvas mit höherer Priorität gegenüber Nachricht mit niedrigerer Priorität {#higher-priority-branching-canvas-versus-lower-priority-message}

Angenommen, ein Canvas mit höherer Priorität kann je nach Zweig, dem ein:e Nutzer:in folgt, unterschiedliche Nachrichten senden. Braze bewertet diese möglichen zukünftigen Pfade konservativ beim Vergleich von Nachrichten. Dies hilft zu verhindern, dass eine Nachricht mit niedrigerer Priorität jetzt gesendet wird, wenn ein Canvas-Zweig mit höherer Priorität dasselbe Frequency-Cap später nutzen könnte.

### Canvas-Schritt mit intelligentem Timing und nachgelagerten Schritten {#canvas-step-with-intelligent-timing-and-downstream-steps}

Angenommen, ein:e Nutzer:in betritt einen Canvas-Nachrichtenschritt mit höherer Priorität, der intelligentes Timing verwendet. Sobald Braze die Sendezeit des/der Nutzer:in für den Schritt mit intelligentem Timing berechnet hat, verwendet die Nachrichtenpriorisierung diese nutzerspezifische Sendezeit für den aktuellen Schritt und für spätere Nachrichtenschritte auf demselben deterministischen Pfad. Dies hilft Braze, nachgelagerte Canvas-Nachrichten mit anderen priorisierten Sendungen anhand des aktualisierten Timings zu vergleichen, anstatt nur die frühere Pfadschätzung zu verwenden.

## Einschränkungen {#limitations}

Die Nachrichtenpriorisierung unterliegt den folgenden Feature-Limits. Die spezifischen Limits hängen von Ihrer Braze-Plattform-Edition ab. Wenden Sie sich für Details an Ihren Braze Account Manager.

- Ein Limit für die Anzahl aktiver, aktivierter geplanter Campaigns und Canvases (kombiniert)
- Ein Limit für die Anzahl aktiver, aktivierter aktionsbasierter Campaigns und Canvases (kombiniert)
- Ein Limit für die Anzahl der Priorisierungsentscheidungen pro Monat
- Ein Limit für die Anzahl der Kategorien pro Workspace
- Ein Limit für die Anzahl der Priorisierungsregeln pro Workspace
- Eine maximale Länge des Wiederholungsfensters

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie werden Gleichstände bei der Priorität zwischen Nachrichten in derselben Kategorie aufgelöst? {#how-are-ties-in-priority-broken-between-messages-in-the-same-category}

Wenn zwei Campaigns in derselben Kategorie gegeneinander priorisiert werden, gibt Braze derjenigen mit der früheren Sendezeit die höhere Priorität. Wenn ein Wiederholungsfenster konfiguriert ist, verwendet Braze das Ende dieses Wiederholungsfensters beim Vergleich von Campaigns innerhalb derselben Prioritätsregel. Bei wiederkehrenden Campaigns wird die Sendezeit als das nächste Vorkommen ab Mitternacht in Unternehmenszeit berechnet. Bei Campaigns, die in Ortszeit geplant sind, nimmt Braze eine Sendezeit in Unternehmenszeit an.

Bei Canvases in derselben Kategorie verwendet Braze den Canvas-Eintrittszeitpunkt als Tiebreaker, sodass alle Schritte im selben Canvas die gleiche relative Priorität gegenüber anderen Campaigns und Canvases beibehalten.

### Wie kann ich sicherstellen, dass eine Nachricht immer gesendet wird? {#how-can-i-make-sure-a-message-is-always-sent}

Es kann Szenarien geben, in denen Sie möchten, dass eine Nachricht immer gesendet wird, z. B. bei transaktionalen oder rechtlichen Benachrichtigungen. In diesem Fall sollten Sie die Nachricht vom Frequency-Capping ausnehmen, wodurch sie auch für die Nachrichtenpriorisierung nicht berücksichtigt wird. Die Nachricht wird dann immer gesendet, wenn sie geplant oder getriggert wird, ohne Berücksichtigung anderer gleichzeitig gesendeter Nachrichten.

### Wann werden Nachrichten tatsächlich priorisiert? Gibt es einen Zeitplan? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Jede Nachricht wird basierend auf dem erwarteten Sendezeitpunkt priorisiert. Es gibt keinen universellen Auswertungszeitpunkt für priorisierte Nachrichten.

### Wie prognostiziert Braze, wann eine zukünftige Nachricht gesendet wird? {#how-does-braze-predict-when-a-future-message-sends}

Braze prognostiziert den zukünftigen Sendezeitpunkt für jeden Nachrichtentyp unterschiedlich:

- **Geplante Campaigns:** Braze verwendet den Zeitpunkt, zu dem jede Campaign voraussichtlich gesendet wird. Bei geplanten Campaigns, die intelligentes Timing verwenden, nutzt Braze den optimalen Sendezeitpunkt jeder Nutzerin und jedes Nutzers für das jeweilige Campaign-Vorkommen.
- **Aktionsbasierte Campaigns:** Braze verwendet den Zeitpunkt, zu dem jede getriggerte Nachricht voraussichtlich gesendet wird, einschließlich einer konfigurierten Verzögerung zwischen Trigger und Versand.
- **Canvas-Schritte:** Braze verwendet den Canvas-Eintritt oder die aktuelle Canvas-Position der Nutzerin bzw. des Nutzers sowie das Timing nachgelagerter Schritte. Bei Canvas-Nachrichtenschritten, die intelligentes Timing verwenden, nutzt Braze nach dem Eintritt in diesen Schritt den berechneten Sendezeitpunkt für diese Person. Für nachfolgende Nachrichtenschritte auf demselben deterministischen Pfad verwendet Braze diesen Sendezeitpunkt des intelligenten Timings zur Bestimmung des späteren erwarteten Sendezeitpunkts. Bevor eine Person den Schritt mit intelligentem Timing erreicht, bleibt die Prognose eine bestmögliche Schätzung.

### Meine Nachricht war bereits zum Senden geplant, wurde aber aufgrund von Rate-Limiting oder anderen Verzögerungen noch nicht gesendet. Was bedeutet das für die Priorisierung anderer Campaigns? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Braze geht davon aus, dass Ihre Nachricht zum ursprünglich geplanten Zeitpunkt gesendet wurde, wenn sie noch verarbeitet wird. Dies bestimmt, ob andere bevorstehende priorisierte Nachrichten gesendet werden. Wenn die Nachricht letztendlich gesendet wird, verwendet Braze den tatsächlichen Sendezeitpunkt.

### Meine Nachricht wurde priorisiert, aber in letzter Minute abgebrochen. Was bedeutet das für die Priorisierung? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Wenn eine Nachricht priorisiert wird, geht Braze davon aus, dass sie zum ursprünglich geplanten Zeitpunkt gesendet wurde. Generell empfehlen wir bei der Nachrichtenpriorisierung nicht, Liquid-Abbrüche zu verwenden. Wenn eine Nachricht aufgrund von [`abort_message`-Liquid-Logik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) abgebrochen wird, gehen wir davon aus, dass sie an diese Person gesendet wurde, und priorisieren zukünftige Campaigns entsprechend.

Nehmen wir an, Sie haben zwei Nachrichten: Nachricht 1 und Nachricht 2. Wenn Nachricht 1 zugunsten einer zukünftigen höher priorisierten Nachricht 2 abgebrochen wird, garantiert dies nicht, dass Nachricht 2 tatsächlich gesendet wird. Nachricht 2 kann aus verschiedenen Gründen ebenfalls abgebrochen werden, darunter:

- Liquid-Abbruchnachrichten
- Die Person befindet sich nicht mehr im Segment
- Frequency-Caps aufgrund einer Nachricht außerhalb der Priorisierungsregeln

Wenn Nachricht 2 abgebrochen wird, gibt es keinen weiteren Versuch, Nachricht 1 zu senden.

Beachten Sie, dass Nutzer:innen eine niedriger priorisierte Nachricht erhalten können, aber nicht eine höher priorisierte Nachricht für dieselbe Frequency-Capping-Regel, und zwar aus folgenden Gründen:

- Die höher priorisierte Nachricht wurde durch eine andere Regel vom Frequency-Capping betroffen.
- Die höher priorisierte Nachricht stand im Konflikt mit einer anderen, zukünftigen Campaign mit noch höherer Priorität für eine andere Regel.
- Zum Zeitpunkt des Versands der niedriger priorisierten Nachricht befand sich die Person nicht in der Zielgruppe der höher priorisierten Nachricht.
- Beide Nachrichten hätten gesendet werden können, aber eine Nachricht außerhalb der Priorisierungskonfiguration wurde vor der höher priorisierten Nachricht gesendet.

### Wie funktioniert intelligentes Timing mit der Nachrichtenpriorisierung? {#how-does-intelligent-timing-work-with-message-prioritization}

Bei Campaigns verwendet die Nachrichtenpriorisierung den optimalen Sendezeitpunkt jeder Nutzerin und jedes Nutzers für das aktuelle Vorkommen. Bei Canvas-Nachrichtenschritten verwendet Braze den berechneten Sendezeitpunkt jeder Person, sobald sie den Schritt erreicht, und berücksichtigt dieses Timing in nachfolgenden Nachrichtenschritten auf demselben deterministischen Pfad. Weitere Details finden Sie unter [Intelligentes Timing](#intelligent-timing).

### Gibt es Berichts- oder Analytics-Funktionen speziell für die Nachrichtenpriorisierung? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Braze stellt Ereignisse zur Nachrichtenpriorisierung in Currents und im Data Sharing für unterstützte Kanäle bereit, darunter E-Mail, LINE, Push-Benachrichtigungen, SMS, Webhooks und WhatsApp. Dazu gehören Depriorisierungs- und Frequency-Capping-Ereignisse, die als `users.messages.<channel>.Abort`-Ereignis protokolliert werden, sowie Wiederholungsereignisse, die anzeigen, wann eine Nachricht innerhalb des konfigurierten Wiederholungsfensters erneut versucht wurde, protokolliert als `users.messages.<channel>.Retry`-Ereignis.

Sie können auch das Messaging-Diagnostics-Dashboard, die vorhandenen täglichen Statistiken zu Depriorisierungen und Wiederholungen sowie die bestehende [Braze-Berichtsfunktionalität]({{site.baseurl}}/user_guide/analytics/reporting) nutzen, um den Zustand und die Performance Ihrer priorisierten Campaigns und Canvases zu überwachen.