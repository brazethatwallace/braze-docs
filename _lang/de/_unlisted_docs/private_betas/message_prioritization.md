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

Nutzer:innen können nur eine begrenzte Anzahl von Nachrichten erhalten, bevor das Volumen zum Problem wird. Die Nachrichten, die sie erreichen, sollten diejenigen sein, die für Ihr Unternehmen am wichtigsten sind. Die Nachrichtenpriorisierung stellt sicher, dass Ihre wertvollsten Nachrichten diesen begrenzten Platz gewinnen – statt es dem Zufall zu überlassen.

Die meisten Teams steuern das Nachrichtenvolumen mit Frequency-Capping. Für sich allein ist Frequency-Capping ein grobes Instrument. Sobald Nutzer:innen ihr Limit erreicht haben, entscheidet der Sendezeitpunkt darüber, welche Nachrichten durchkommen – nicht die geschäftliche Bedeutung.

Eine weniger wertvolle Aktion, die zuerst ausgelöst wird, kann einen Platz belegen, den eine Kundenbindungs-Belohnung oder eine zeitkritische Nachricht später am selben Tag genutzt hätte. Teams umgehen dies oft mit separaten Begrenzungsregeln, manueller Planung und Ad-hoc-Filtern. Diese Ansätze erfordern ständige Pflege. Sie werden schwieriger zu verwalten, wenn sich Campaigns und Canvases ändern. Und sie können trotzdem nicht garantieren, dass die richtige Nachricht gewinnt.

Die Nachrichtenpriorisierung ändert die Frequency-Capping-Zuteilung von **Wer zuerst kommt, mahlt zuerst** zu **geschäftsprioritätsbewusst**: Sie legen fest, was wichtig ist, und Braze trifft die Sendeentscheidungen für Sie.

Die Nachrichtenpriorisierung bietet mehrere Vorteile:

- **Einmal festlegen, was wichtig ist:** Verwenden Sie Kategorien und priorisierte Regeln, um Ihre Prioritäten abzubilden – zum Beispiel „Kundenbindung“ vor „Bezahlte Partnerschaften“. Jeder für Opt-in freigegebene Versand berücksichtigt diese Rankings automatisch.
- **Vorausschauende Entscheidungen:** Braze prognostiziert, was Nutzer:innen später erhalten könnten. Es kann eine Nachricht mit niedrigerer Priorität zurückhalten, um Kapazität für eine Nachricht mit höherer Priorität zu bewahren.
- **Funktioniert über Nachrichtentypen und Kanäle hinweg:** Geplante Campaigns, aktionsbasierte Campaigns und Canvas-Schritte konkurrieren in einem gemeinsamen, priorisierten Pool innerhalb Ihrer geteilten Frequency-Caps.
- **Wiederholungsfenster:** Eine zurückgestellte Nachricht kann erneut versucht werden, wenn Kapazität frei wird. Dies verbessert den Nachrichtenmix, ohne Nachrichten mit niedrigerer Priorität vollständig zu verwerfen.

Das Ergebnis ist dasselbe begrenzte Sendevolumen, automatisch den Nachrichten zugewiesen, die am wichtigsten sind.

Die Nachrichtenpriorisierung ist besonders wertvoll für Absender mit hohem Volumen, die regelmäßig Frequency-Caps erreichen. Sie funktioniert am besten, wenn sich der Nachrichtenwert klar unterscheiden lässt – zum Beispiel Kundenbindungs- oder umsatzfördernde Nachrichten im Vergleich zu Routineaktionen.

## So funktioniert es {#how-it-works}

Verwenden Sie die Nachrichtenpriorisierung, um [Kategorien](#categories) und [Priorisierungsregeln](#prioritization-rules) zu erstellen, mit denen Sie festlegen, wie Ihre Nachrichten gesendet werden.

Um diese Einstellungen zu verwalten, gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung**. Nur Administrator:innen können die übergeordneten Einstellungen der Nachrichtenpriorisierung konfigurieren. Nutzer:innen benötigen die Berechtigung „View Message Prioritization“, um die Einstellungen in diesem Bereich einzusehen, und die Berechtigung „Edit Message Prioritization“, um sie zu bearbeiten.

Beispiel: Eine Kosmetikmarke, die E-Mail-Aktionen für bezahlte Partnerschaften und Kundenbindungs-Programme verwaltet, nutzt die Nachrichtenpriorisierung, um zwei Kategorien zu erstellen: „Bezahlte Partnerschaften“ und „Kundenbindung“. Die Marke ordnet diese Kategorien nach geschäftlicher Bedeutung. Während der Weihnachtssaison wird „Kundenbindung“ an erster und „Bezahlte Partnerschaften“ an zweiter Stelle eingestuft, um langjährige Mitglieder zu priorisieren.

![Ein Beispiel für Priorisierungsregeln für zwei Kategorien: Bezahlte Partnerschaften und Kundenbindung.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

Zum Sendezeitpunkt vergleicht Braze die zu sendende Nachricht mit anderen Nachrichten, die die Nutzer:innen möglicherweise erhalten und die für die Priorisierung aktiviert sind, eine Prioritätskategorie festgelegt haben und innerhalb desselben Frequency-Capping-Zeitfensters auf dieselbe Frequency-Capping-Regel angerechnet werden. Wenn das Senden der aktuellen Nachricht verhindern würde, dass eine Nachricht mit höherer Priorität später gesendet wird, stuft Braze die Nachricht mit niedrigerer Priorität herab. Je nach konfiguriertem Wiederholungsfenster wird diese Nachricht mit niedrigerer Priorität entweder später erneut versucht oder gar nicht gesendet.

Die Nachrichtenpriorisierung kann Folgendes auswerten:

- Geplante Campaigns
- Aktionsbasierte Campaigns
- Canvases

Derzeit werden API-getriggerte Campaigns oder Canvases von der Nachrichtenpriorisierung nicht unterstützt und nehmen nicht an der Priorisierung teil.

Braze nutzt seine Vorhersage, wann jede Nachricht voraussichtlich gesendet wird, um zu bewerten, ob das Senden einer Nachricht jetzt das spätere Senden einer Nachricht mit höherer Priorität verhindern könnte. Weitere Informationen darüber, wie Braze den zukünftigen Sendezeitpunkt für Campaigns und Canvases vorhersagt, finden Sie unter [Wie sagt Braze vorher, wann eine zukünftige Nachricht gesendet wird?](#how-does-braze-predict-when-a-future-message-sends)

### Unterstützte Nachrichtenkanäle {#supported-message-channels}

Die Nachrichtenpriorisierung unterstützt dieselben Kanäle wie das Frequency-Capping:

- Push-Benachrichtigungen
- E-Mail
- SMS
- Webhooks
- WhatsApp
- LINE

Für Priorisierung und Frequency-Capping werden iOS-Push, Android-Push, Web-Push und andere Push-Benachrichtigungsplattformen als ein gemeinsamer Push-Kanal behandelt, nicht als separate Kanäle.

Diese Kanäle sind nicht für die Nachrichtenpriorisierung geeignet, da sie nicht dem Frequency-Capping unterliegen:

- Content Cards
- In-App-Nachrichten
- Banner

In-App-Nachrichten und Banner verwenden ihre eigenen Prioritätseinstellungen, um zu entscheiden, welche Nachricht angezeigt wird, wenn mehrere Nachrichten um denselben Trigger oder dieselbe Platzierung konkurrieren. Für In-App-Nachrichten siehe [Priorität auswählen]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority). Für Banner siehe [Banner-Priorität]({{site.baseurl}}/user_guide/channels/banners#priority).

Wenn eine Campaign oder ein Canvas-Schritt nur nicht unterstützte Kanäle verwendet, nimmt sie nicht an der Priorisierung teil.

## Kategorien {#categories}

Priorisierungsregeln basieren auf einer Rangfolge von Kategorien, die Labels sind, die Sie einer bestimmten Campaign oder einem Canvas zuweisen können (ähnlich wie ein [Tag]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)). Es gibt eine Obergrenze für die Anzahl der Kategorien, die Sie zu einem bestimmten Zeitpunkt erstellen können. Sprechen Sie mit Ihrem Account Manager, wenn Sie ein höheres Limit wünschen.

So fügen Sie eine neue Kategorie hinzu:

1. Gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung** > **Kategorien**.
2. Wählen Sie **Neue Kategorie erstellen** aus.

![Der Button „Neue Kategorie erstellen“ im Bereich „Nachrichtenpriorisierung“.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Geben Sie der Kategorie einen Namen und eine optionale Beschreibung.
4. Wählen Sie **Kategorie erstellen** aus.

![Eine Beispielkategorie mit dem Namen „P3“ und der Beschreibung „Dies ist meine dritthöchste Prioritätskategorie“.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

Um eine Kategorie zu bearbeiten oder zu löschen, wählen Sie das Menü <i class="fas fa-ellipsis-vertical" aria-label="Mehr Optionen"></i> aus.

## Priorisierungsregeln {#prioritization-rules}

Nachdem Ihre Kategorien eingerichtet sind, können Sie sie in einem Satz von Priorisierungsregeln einstufen. Regeln werden in absteigender Prioritätsreihenfolge eingestuft. Es gibt eine Obergrenze für die Anzahl der Priorisierungsregeln, die Sie zu einem bestimmten Zeitpunkt erstellen können. Wenden Sie sich an Ihren Account Manager, wenn Sie ein höheres Limit wünschen.

1. Gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung** > **Priorisierungsregeln**, um Ihre Regeln zu konfigurieren.

![Abschnitt „Priorisierungsregeln“ ohne bisher festgelegte Prioritäten.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. Wählen Sie **Regel hinzufügen** aus.
3. Wählen Sie eine Kategorie aus dem Dropdown-Menü aus.

![Priorisierungsregel „Priorität 1“ mit P1 als ausgewählter Kategorie.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. Fügen Sie weitere Regeln hinzu, indem Sie **+ Regel hinzufügen** unter Ihrer letzten Regel auswählen.

Um Regeln neu anzuordnen, wählen Sie das <i class="fa-solid fa-grip-vertical" aria-label="Regel ziehen und ablegen"></i>-Symbol einer Regel aus und ziehen Sie es an die gewünschte Position. Um eine Regel zu löschen, wählen Sie das Menü <i class="fas fa-ellipsis-vertical" aria-label="Weitere Optionen"></i> und dann **Regel löschen** aus.

Vergessen Sie nicht, **Speichern** auszuwählen, damit Ihre Änderungen übernommen werden.

## Frequency-Capping {#frequency-caps}

Die Nachrichtenpriorisierung arbeitet innerhalb Ihrer bestehenden Frequency-Capping-Regeln. Damit eine Campaign oder ein Canvas-Schritt für die Priorisierung in Frage kommt, muss ein unterstützter Kanal verwendet werden und der Frequency-Capping-Konfiguration unterliegen. Nachrichten, die nicht dem Frequency-Capping unterliegen, kommen für die Nachrichtenpriorisierung nicht in Frage. Wenn Sie möchten, dass eine Nachricht immer gesendet wird, nehmen Sie sie vom Frequency-Capping aus. Dadurch wird sie auch aus der Nachrichtenpriorisierung entfernt.

Eine priorisierte Nachricht kann nur gesendet werden, wenn:

1. Die relevante Frequency-Capping-Regel für diese:n Nutzer:in noch nicht erreicht wurde, und
2. Das Senden dieser Nachricht nicht dazu führen würde, dass die/der Nutzer:in ein Limit erreicht, bevor eine spätere Nachricht mit höherer Priorität gesendet werden kann.

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

Das Canvas-Opt-in funktioniert ähnlich wie bei Campaigns. Um ein Canvas für die Nachrichtenpriorisierung anzumelden, aktivieren Sie die Nachrichtenpriorisierung in den Canvas-Einstellungen und weisen Sie das Canvas einer Kategorie zu. Alle Schritte im Canvas teilen dieselbe Kategorie und dieselbe Prioritätsstufe, was bedeutet, dass Sie die Priorität nicht individuell pro Schritt festlegen können.

Die Nachrichtenpriorisierung unterstützt geplante Canvases und aktionsbasierte Canvases. API-getriggerte Canvases werden nicht unterstützt.

## Intelligentes Timing {#intelligent-timing}

Beim intelligenten Timing sendet Braze eine Nachricht zum optimalen Sendezeitpunkt jedes einzelnen Nutzers bzw. jeder einzelnen Nutzerin, sodass dieselbe Campaign oder derselbe Canvas-Nachrichtenschritt verschiedene Nutzer:innen zu unterschiedlichen Zeiten erreichen kann. Die Nachrichtenpriorisierung berücksichtigt dies: Anstatt anzunehmen, dass die Nachricht zum geplanten Zeitpunkt an alle gesendet wird, ordnet sie die konkurrierenden Nachrichten eines Nutzers bzw. einer Nutzerin anhand des jeweiligen optimalen Sendezeitpunkts ein.

Für Campaigns und Canvas-Nachrichtenschritte, die intelligentes Timing verwenden, prognostiziert Braze den Sendezeitpunkt nach dem Best-Effort-Prinzip, bis der individuelle Sendezeitpunkt für jeden Nutzer bzw. jede Nutzerin berechnet ist. Bei Campaigns verwendet die Nachrichtenpriorisierung den optimalen Sendezeitpunkt des Nutzers bzw. der Nutzerin für das aktuelle Vorkommen, wenn die Campaign mit den anderen priorisierten Nachrichten verglichen wird, für die der Nutzer bzw. die Nutzerin infrage kommt. Bei wiederkehrenden Campaigns mit intelligentem Timing verwendet Braze den für dieses Vorkommen gewählten optimalen Sendezeitpunkt.

Bei Canvas-Nachrichtenschritten aktualisiert Braze diese Prognose, sobald der Nutzer bzw. die Nutzerin den Schritt erreicht und Braze den optimalen Sendezeitpunkt für diesen Schritt berechnet hat. Die Nachrichtenpriorisierung verwendet diesen berechneten Sendezeitpunkt für den aktuellen Schritt. Auf deterministischen Pfaden (Pfade ohne Verzweigung, bei denen die Schrittfolge festgelegt ist) berücksichtigt Braze dieses aktualisierte Timing auch in den nachfolgenden Nachrichtenschritten bei der Bestimmung ihrer erwarteten Sendezeitpunkte.

## Wiederholungsfenster {#retry-windows}

Ein Wiederholungsfenster ermöglicht es Nachrichten mit Opt-in, sich über eine begrenzte Anzahl von Tagen erneut zu versuchen, wenn der erste Versuch keine ausreichend hohe Priorität zum Senden hat. Die maximale Länge des Wiederholungsfensters hängt von Ihrer Braze-Plattform-Edition ab. An jedem darauffolgenden Tag, zur gleichen Uhrzeit, zu der die Nachricht ursprünglich geplant oder getriggert wurde, wird ein erneuter Sendeversuch unternommen. Nach dem letzten Tag im Wiederholungsfenster wird die Nachricht, wenn sie immer noch nicht gesendet wurde, nicht weiter wiederholt und dauerhaft deprioritisiert.

Bei wiederkehrenden geplanten Campaigns muss das Wiederholungsfenster kürzer sein als die minimale Zeit zwischen den Sendungen dieser Campaign. Wiederholungen finden immer einen Tag nach der ursprünglichen Sendezeit statt, selbst wenn die Campaign normalerweise nicht an diesem Tag zum Senden eingeplant ist. Wenn Sie zum Beispiel eine Campaign haben, die jeden Montag und Mittwoch sendet, erfolgt der Wiederholungsversuch am Dienstag, sodass das Wiederholungsfenster auf einen Tag eingestellt werden muss. Wenn Sie eine Campaign haben, die jeden Montag, Mittwoch und Freitag sendet, und die Freitagssendung mit einem eintägigen Wiederholungsfenster wiederholt wird, erfolgt der Wiederholungsversuch am Samstag, nicht am Montag.

![Die Einstellung „Wiederholungsfenster“ auf 1 Tag eingestellt.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

Bei aktionsbasierten Campaigns basieren Wiederholungen auf dem Zeitpunkt, zu dem die getriggerte Nachricht ursprünglich gesendet werden sollte.

Aktionsbasierte Campaigns, die Ausnahme-Events verwenden, unterstützen keine Wiederholungsfenster.

Wiederholungsfenster für Canvas-Nachrichten werden auf Schrittebene konfiguriert. Wenn bei unterstützten Canvas-Nachrichten-Schritten ein Canvas-Nachrichten-Schritt deprioritisiert wird und ein Wiederholungsfenster konfiguriert ist, kann Braze diesen Schritt später innerhalb seines Wiederholungsfensters erneut versuchen.

## Wie Braze Nachrichten bewertet {#how-braze-evaluates-messages}

{% alert tip %}
Sie müssen nicht alles in diesem Abschnitt verstehen, um die Nachrichtenpriorisierung zu nutzen. Sobald Sie Ihre Kategorien und Regeln festgelegt und Ihre Nachrichten aktiviert haben, bewertet und priorisiert Braze Nachrichten automatisch und gibt sein Bestes, die wichtigsten zu senden. Die Details hier sind für den Fall, dass Sie verstehen möchten, wie diese Entscheidungen getroffen werden.
{% endalert %}

Wenn Nutzer:innen für mehrere priorisierte Nachrichten qualifiziert sind, bewertet Braze aktivierte Campaigns und qualifizierte Canvas-Nachrichtenschritte gemeinsam auf unterstützten Kanälen.

Für Campaigns umfasst dies qualifizierte geplante und aktionsbasierte Sendungen.

Für Canvases umfasst dies:

- Zukünftige geplante Canvases, für die Nutzer:innen qualifiziert sind
- Canvases, in denen sich Nutzer:innen derzeit befinden

Die Canvas-Priorisierung ist kein Alles-oder-nichts-Prinzip. Eine höher priorisierte Campaign kann dazu führen, dass ein Canvas-Schritt herabgestuft wird, während spätere qualifizierte Schritte in demselben Canvas je nach Kategorieranking, Sendezeitpunkt und Frequency-Capping-Regeln weiterhin gesendet werden können.

Braze vergleicht priorisierte Nachrichten nur dann, wenn sie dieselbe anwendbare Frequency-Capping-Regel teilen. Zum Beispiel können zwei E-Mail-Campaigns, die auf dieselbe E-Mail-Frequency-Capping-Regel angerechnet werden, gegeneinander priorisiert werden, aber eine niedriger priorisierte E-Mail-Campaign wird nicht zugunsten einer höher priorisierten SMS-Nachricht herabgestuft, es sei denn, beide werden auf dieselbe Regel angerechnet. Nachrichten außerhalb der Nachrichtenpriorisierung teilen diese Frequency-Cap-Limits ebenfalls, sodass selbst eine hoch priorisierte Nachricht aufgrund einer Nachricht außerhalb der Nachrichtenpriorisierung abgebrochen werden kann.

Braze bewertet Campaigns und Canvases unterschiedlich, da ein Canvas sich verzweigen und über die Zeit entfalten kann.

### Campaigns bewerten {#evaluating-campaigns}

Braze vergleicht jede qualifizierte Campaign-Nachricht anhand des Zeitpunkts, zu dem die Nachricht voraussichtlich gesendet wird.

### Canvases bewerten {#evaluating-canvases}

Um ein Canvas zu bewerten, führt Braze einen **Look-Ahead** durch: Es durchläuft das Canvas von einem Startpunkt aus, um vorherzusagen, welche zukünftigen Nachrichten Nutzer:innen erhalten könnten und wann. Der Look-Ahead startet ab:

- Canvas-Eintritt, bei zukünftigen geplanten Canvases
- Dem aktuellen Schritt der Nutzer:innen, wenn sie sich bereits im Canvas befinden

Beim Look-Ahead behandelt Braze jeden Typ von Canvas-Schritt unterschiedlich. Der Schritttyp bestimmt, ob der Look-Ahead ihn zählt, überspringt, dort stoppt oder sich auf mehrere Pfade aufteilt:

| Schrittkategorie | Auswirkung auf den Look-Ahead |
|---|---|
| Messaging-Schritte | Werden als qualifizierte Nachrichten für die Priorisierung gezählt |
| Fortsetzungsschritte | Übersprungen; der Look-Ahead durchläuft sie |
| Grenzschritte | Der Look-Ahead stoppt, bis Nutzer:innen den Schritt passiert haben |
| Verzweigungsschritte | Der Look-Ahead folgt jedem möglichen Pfad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvases bewerten" }

#### Messaging-Schritte {#messaging-steps}

Diese Schritte werden für die Priorisierung gezählt und der Menge qualifizierter Nachrichten hinzugefügt, wenn sie auf einem unterstützten Kanal senden.

- Nachrichtenschritt
- Content-Optimizer-Schritt

#### Fortsetzungsschritte {#continuation-steps}

Diese Schritte werden bei der Priorisierung ignoriert und beeinflussen den Look-Ahead nicht.

- Kontextaktualisierungsschritt
- Nutzer:innen-Aktualisierungsschritt
- Audience-Sync-Schritt
- Feature-Flag-Schritt
- Verzögerungsschritt mit einer festen Verzögerung

#### Grenzschritte {#boundary-steps}

Braze stoppt den Look-Ahead an diesen Schritten, bis Nutzer:innen tatsächlich im Canvas durch sie hindurchgehen.

- Verzögerungsschritt mit einer personalisierten Verzögerung
- Verzögerungsschritt, der einem Verzweigungsschritt folgt
- Aktionspfadschritt
- Experimentschritt

#### Verzweigungsschritte {#branching-steps}

Diese Schritte teilen das Canvas in mehrere mögliche Pfade auf.

- Decision-Split-Schritt
- Zielgruppenpfadschritt

Wenn ein Priorisierungspfad Verzweigungsschritte enthält, geht Braze davon aus, dass alle Pfade möglich sind, und berücksichtigt alle parallelen Messaging-Schritte auf unterstützten Kanälen für die Priorisierung. Da Frequency-Capping-Regeln kanalspezifisch sein können, werden parallele Messaging-Schritte bei Bedarf nach Kanal dedupliziert.

Zum Beispiel: Wenn ein Zweig eine E-Mail senden kann und ein anderer Zweig ebenfalls eine E-Mail senden kann, behandelt Braze diese während des Look-Aheads als einen einzelnen möglichen E-Mail-Versand. Wenn ein anderer Zweig Push senden kann, berücksichtigt Braze diesen möglichen Push-Versand separat.

Für Canvas-Nachrichtenschritte, die intelligentes Timing verwenden, nutzt Braze den berechneten Sendezeitpunkt jeder Nutzer:in, sobald sie den Schritt erreichen. Details finden Sie unter [Intelligentes Timing](#intelligent-timing).

Content-Optimizer-Schritte werden wie Messaging-Schritte behandelt, da sie immer auf einem bestimmten Kanal senden. Wiederholungsfenster gelten jedoch nicht für Content-Optimizer-Schritte, da Wiederholungen das Experiment beeinträchtigen würden. Andere unterstützte Canvas-Messaging-Schritte können Wiederholungsfenster verwenden. Canvas-Schritte auf nicht unterstützten Kanälen nehmen nicht an der Nachrichtenpriorisierung teil.

## Beispiele {#examples}

### Campaign mit höherer Priorität im Vergleich zu Campaign mit niedrigerer Priorität {#higher-priority-campaign-versus-lower-priority-campaign}

Angenommen, eine Nutzerin oder ein Nutzer ist am selben Tag für zwei E-Mail-Campaigns berechtigt und beide Campaigns zählen für dieselbe Frequency-Capping-Regel. Wenn erwartet wird, dass die Campaign mit höherer Priorität später am Tag gesendet wird, kann Braze die Campaign mit niedrigerer Priorität herabstufen, damit die Campaign mit höherer Priorität stattdessen gesendet werden kann. Falls die Campaign mit niedrigerer Priorität ein Wiederholungsfenster hat, kann Braze sie später erneut versuchen.

### Aktionsbasierte Campaign mit höherer Priorität im Vergleich zu Nachricht mit niedrigerer Priorität {#higher-priority-action-based-campaign-versus-lower-priority-message}

Angenommen, eine Nutzerin oder ein Nutzer triggert eine aktionsbasierte Campaign mit höherer Priorität, die auf einen Versand zwei Stunden später eingestellt ist. Während dieser Verzögerung kann Braze diese bevorstehende aktionsbasierte Campaign berücksichtigen, wenn entschieden wird, ob eine andere priorisierte Nachricht zuerst gesendet werden soll. Dies hilft zu verhindern, dass eine Nachricht mit niedrigerer Priorität jetzt gesendet wird, wenn die aktionsbasierte Campaign mit höherer Priorität voraussichtlich bald gesendet wird.

### Canvas mit höherer Priorität im Vergleich zu Campaign mit niedrigerer Priorität {#higher-priority-canvas-versus-lower-priority-campaign}

Angenommen, eine Nutzerin oder ein Nutzer ist für eine Campaign mit niedrigerer Priorität berechtigt, wird aber voraussichtlich später am Tag auch eine Canvas-Nachricht mit höherer Priorität erhalten. Wenn Braze diese zukünftige Canvas-Nachricht bereits auswerten kann, kann es die Campaign mit niedrigerer Priorität herabstufen, damit die Canvas-Nachricht mit höherer Priorität stattdessen gesendet werden kann.

### Canvas mit höherer Priorität und einem Grenzschritt im Vergleich zu Campaign mit niedrigerer Priorität {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

Angenommen, ein Canvas mit höherer Priorität enthält einen Aktionspfad-Schritt, ein Experiment oder eine personalisierte Verzögerung vor dem nächsten Nachrichten-Schritt. Bis die Nutzerin oder der Nutzer diesen Schritt erreicht und passiert hat, schaut Braze nicht voraus auf die nachgelagerte Canvas-Nachricht mit höherer Priorität. In diesem Fall kann eine Campaign mit niedrigerer Priorität dennoch zuerst gesendet werden.

### Verzweigter Canvas mit höherer Priorität im Vergleich zu Nachricht mit niedrigerer Priorität {#higher-priority-branching-canvas-versus-lower-priority-message}

Angenommen, ein Canvas mit höherer Priorität kann je nach dem Zweig, dem eine Nutzerin oder ein Nutzer folgt, unterschiedliche Nachrichten senden. Braze wertet diese möglichen zukünftigen Pfade beim Vergleich von Nachrichten konservativ aus. Dies hilft zu verhindern, dass eine Nachricht mit niedrigerer Priorität jetzt gesendet wird, wenn ein Canvas-Zweig mit höherer Priorität dasselbe Frequency-Capping später nutzen könnte.

### Canvas-Schritt mit intelligentem Timing und nachgelagerten Schritten {#canvas-step-with-intelligent-timing-and-downstream-steps}

Angenommen, eine Nutzerin oder ein Nutzer tritt in einen Canvas-Nachrichten-Schritt mit höherer Priorität ein, der intelligentes Timing verwendet. Sobald Braze die Sendezeit der Nutzerin oder des Nutzers für den Schritt mit intelligentem Timing berechnet hat, verwendet die Nachrichtenpriorisierung diese nutzerspezifische Sendezeit für den aktuellen Schritt und für spätere Nachrichten-Schritte auf demselben deterministischen Pfad. Dies hilft Braze, nachgelagerte Canvas-Nachrichten mit anderen priorisierten Sendungen auf Basis des aktualisierten Timings statt nur der früheren Pfadschätzung zu vergleichen.

## Einschränkungen {#limitations}

Die Nachrichtenpriorisierung hat die folgenden Feature-Grenzen. Spezifische Grenzen hängen von Ihrer Braze-Plattform-Edition ab; wenden Sie sich an Ihren Braze Account Manager für Details.

- Ein Limit für die Anzahl aktiver, angemeldeter geplanter Campaigns und Canvases (kombiniert)
- Ein Limit für die Anzahl aktiver, angemeldeter aktionsbasierter Campaigns und Canvases (kombiniert)
- Ein Limit für die Anzahl der Priorisierungsentscheidungen pro Monat
- Ein Limit für die Anzahl der Kategorien pro Workspace
- Ein Limit für die Anzahl der Priorisierungsregeln pro Workspace
- Eine maximale Zeitfensterlänge für erneute Versuche

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie werden Gleichstände bei der Priorität zwischen Nachrichten in derselben Kategorie aufgelöst? {#how-are-ties-in-priority-broken-between-messages-in-the-same-category}

Wenn zwei Campaigns in derselben Kategorie gegeneinander priorisiert werden, gibt Braze derjenigen mit der früheren Sendezeit die höhere Priorität. Wenn ein Wiederholungsfenster konfiguriert ist, verwendet Braze das Ende dieses Wiederholungsfensters beim Vergleich von Campaigns innerhalb derselben Prioritätsregel. Bei wiederkehrenden Campaigns wird die Sendezeit als das nächste Vorkommen ab Mitternacht in Unternehmenszeit berechnet. Bei Campaigns, die in Ortszeit geplant sind, geht Braze von einer Sendezeit in Unternehmenszeit aus.

Bei Canvases in derselben Kategorie verwendet Braze den Canvas-Eintrittszeitpunkt als Entscheidungskriterium, sodass alle Schritte im selben Canvas die gleiche relative Priorität gegenüber anderen Campaigns und Canvases beibehalten.

### Wie kann ich sicherstellen, dass eine Nachricht immer gesendet wird? {#how-can-i-make-sure-a-message-is-always-sent}

Es kann Szenarien geben, in denen eine Nachricht immer gesendet werden soll, z. B. bei transaktionalen oder rechtlichen Benachrichtigungen. In diesem Fall sollten Sie die Nachricht vom Frequency-Capping ausnehmen, wodurch sie auch nicht für die Nachrichtenpriorisierung infrage kommt. Die Nachricht wird dann immer dann gesendet, wenn sie geplant oder getriggert wird, ohne Berücksichtigung anderer Sendungen.

### Wann werden Nachrichten tatsächlich priorisiert? Gibt es einen Zeitplan? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Jede Nachricht wird basierend auf ihrem erwarteten Sendezeitpunkt priorisiert. Es gibt keinen universellen Auswertungszeitpunkt für priorisierte Nachrichten.

### Wie sagt Braze voraus, wann eine zukünftige Nachricht gesendet wird? {#how-does-braze-predict-when-a-future-message-sends}

Braze prognostiziert den zukünftigen Sendezeitpunkt für jeden Nachrichtentyp unterschiedlich:

- **Geplante Campaigns:** Braze verwendet den Zeitpunkt, zu dem jede Campaign voraussichtlich gesendet wird. Bei geplanten Campaigns, die intelligentes Timing verwenden, nutzt Braze den optimalen Sendezeitpunkt jedes Nutzers bzw. jeder Nutzerin für dieses Campaign-Vorkommen.
- **Aktionsbasierte Campaigns:** Braze verwendet den Zeitpunkt, zu dem jede getriggerte Nachricht voraussichtlich gesendet wird, einschließlich einer konfigurierten Verzögerung zwischen Trigger und Versand.
- **Canvas-Schritte:** Braze verwendet den Canvas-Eintritt oder die aktuelle Canvas-Position des Nutzers bzw. der Nutzerin sowie das Timing nachfolgender Schritte. Bei Canvas-Nachrichtenschritten, die intelligentes Timing verwenden, nutzt Braze nach dem Eintritt in diesen Schritt den berechneten nutzerspezifischen Sendezeitpunkt. Für nachfolgende Nachrichtenschritte auf demselben deterministischen Pfad wird dieser Sendezeitpunkt des intelligenten Timings bei der Bestimmung späterer erwarteter Sendezeiten herangezogen. Bevor Nutzer:innen den Schritt mit intelligentem Timing erreichen, bleibt die Vorhersage eine Bestmöglichkeitsschätzung.

### Meine Nachricht war bereits zum Senden geplant, wurde aber wegen Rate-Limiting oder anderer Verzögerungen noch nicht gesendet. Was bedeutet das für die Priorisierung anderer Campaigns? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Braze geht davon aus, dass Ihre Nachricht zum ursprünglich geplanten Zeitpunkt gesendet wurde, wenn sie sich noch in der Verarbeitung befindet. Dies bestimmt, ob andere bevorstehende priorisierte Nachrichten gesendet werden. Wenn die Nachricht letztendlich gesendet wird, verwendet Braze den tatsächlichen Sendezeitpunkt.

### Meine Nachricht wurde priorisiert, aber in letzter Minute abgebrochen. Was bedeutet das für die Priorisierung? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Wenn eine Nachricht priorisiert wird, geht Braze davon aus, dass sie zum ursprünglich geplanten Zeitpunkt gesendet wurde. Generell empfehlen wir für die Nachrichtenpriorisierung nicht, Liquid-Abbrüche zu verwenden. Wenn eine Nachricht aufgrund von [`abort_message`-Liquid-Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) abgebrochen wird, gehen wir davon aus, dass sie an diesen Nutzer bzw. diese Nutzerin gesendet wurde, und priorisieren zukünftige Campaigns entsprechend.

Angenommen, Sie haben zwei Nachrichten: Nachricht 1 und Nachricht 2. Wenn Nachricht 1 zugunsten einer zukünftigen höher priorisierten Nachricht 2 abgebrochen wird, garantiert dies nicht, dass Nachricht 2 tatsächlich gesendet wird. Nachricht 2 kann aus verschiedenen Gründen ebenfalls abgebrochen werden, darunter:

- Liquid-Abbruchnachrichten
- Der Nutzer bzw. die Nutzerin befindet sich nicht mehr im Segment
- Frequency-Caps aufgrund einer Nachricht außerhalb der Priorisierungsregeln

Wenn Nachricht 2 abgebrochen wird, gibt es keinen weiteren Versuch, Nachricht 1 zu senden.

Beachten Sie, dass Nutzer:innen eine niedriger priorisierte Nachricht erhalten könnten, aber nicht eine höher priorisierte Nachricht für dieselbe Frequency-Capping-Regel, und zwar aus folgenden Gründen:

- Die höher priorisierte Nachricht wurde durch eine andere Regel vom Frequency-Capping betroffen.
- Die höher priorisierte Nachricht kollidierte mit einer anderen, zukünftigen Campaign mit noch höherer Priorität für eine andere Regel.
- Zum Zeitpunkt des Versands der niedriger priorisierten Nachricht befand sich der Nutzer bzw. die Nutzerin nicht in der Zielgruppe der höher priorisierten Nachricht.
- Beide Nachrichten hätten gesendet werden können, aber eine Nachricht außerhalb der Priorisierungskonfiguration wurde vor der höher priorisierten Nachricht gesendet.

### Wie funktioniert intelligentes Timing mit der Nachrichtenpriorisierung? {#how-does-intelligent-timing-work-with-message-prioritization}

Bei Campaigns verwendet die Nachrichtenpriorisierung den optimalen Sendezeitpunkt jedes Nutzers bzw. jeder Nutzerin für das aktuelle Vorkommen. Bei Canvas-Nachrichtenschritten verwendet Braze den berechneten Sendezeitpunkt jedes Nutzers bzw. jeder Nutzerin, sobald der Schritt erreicht wird, und berücksichtigt dieses Timing in nachfolgenden Nachrichtenschritten auf demselben deterministischen Pfad. Weitere Informationen finden Sie unter [Intelligentes Timing](#intelligent-timing).

### Gibt es spezielle Berichts- oder Analytics-Funktionen für die Nachrichtenpriorisierung? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Braze stellt Events zur Nachrichtenpriorisierung in Currents und Data Sharing für unterstützte Kanäle bereit, darunter E-Mail, LINE, Push-Benachrichtigungen, SMS, Webhooks und WhatsApp. Dazu gehören Events für herabgestufte und vom Frequency-Capping betroffene Nachrichten, die als `users.messages.<channel>.Abort`-Event protokolliert werden, sowie Wiederholungs-Events, die anzeigen, wann eine Nachricht innerhalb des konfigurierten Wiederholungsfensters erneut versucht wurde, protokolliert als `users.messages.<channel>.Retry`-Event.

Sie können auch das Messaging-Diagnose-Dashboard, die bestehenden täglichen Statistiken für herabgestufte und wiederholte Nachrichten sowie die bestehende [Braze-Berichtsfunktionalität]({{site.baseurl}}/user_guide/analytics/reports) nutzen, um den Zustand und die Performance Ihrer priorisierten Campaigns und Canvases zu überwachen.