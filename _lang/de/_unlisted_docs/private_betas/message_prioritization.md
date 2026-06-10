---
article_title: Nachrichtenpriorisierung
permalink: /message_prioritization/
toc_headers: h2
description: "Dieser Referenzartikel beschreibt die übergeordnete Nachrichtenpriorisierung und wie Sie diese für Ihren Workspace konfigurieren."
---

# Nachrichtenpriorisierung {#message-prioritization}

> Verwenden Sie die Nachrichtenpriorisierung, um sicherzustellen, dass Ihre Nutzer:innen die Campaigns erhalten, die am wichtigsten sind.

{% alert important %}
Die Nachrichtenpriorisierung befindet sich derzeit in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Teilnahme an dieser Beta interessiert sind.
{% endalert %}

Nur Administrator:innen können die übergeordneten Einstellungen der Nachrichtenpriorisierung konfigurieren. Nutzer:innen mit eingeschränkten Rechten können jede Seite in diesem Abschnitt einsehen, aber keine Änderungen vornehmen.

Für die übergeordneten Einstellungen der Nachrichtenpriorisierung gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung**.

## Funktionsweise {#how-it-works}

Die Nachrichtenpriorisierung ermöglicht es Ihnen, [Kategorien](#categories) und [Priorisierungsregeln](#prioritization-rules) zu erstellen, um die Reihenfolge Ihrer Nachrichten festzulegen.

Nehmen wir an, Sie verwalten E-Mail-Aktionen für bezahlte Partnerschaften und Kundenbindungs-Programme einer Kosmetikmarke. Mit der Nachrichtenpriorisierung könnten Sie zwei Kategorien mit den Namen „Bezahlte Partnerschaften“ und „Kundenbindung“ erstellen. Anschließend könnten Sie diese Kategorien danach ordnen, welche für Ihre Marke geschäftskritischer ist. Beispielsweise könnten Sie während der Weihnachtszeit „Kundenbindung“ höher als „Bezahlte Partnerschaften“ einstufen, um Kund:innen Ihrer Marke zu priorisieren, die seit über einem Jahr Teil Ihres Mitgliedschaftsprogramms sind.

![Ein Beispiel für Priorisierungsregeln für zwei Kategorien: „Bezahlte Partnerschaften“ und „Kundenbindung“.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

## Kategorien {#categories}

Priorisierungsregeln basieren auf einer Rangfolge von Kategorien, die ein Label darstellen, das Sie einer bestimmten Campaign zuweisen können (ähnlich wie ein [Tag](https://www.braze.com/docs/user_guide/administrative/app_settings/tags)). Sie können bis zu 20 Kategorien gleichzeitig erstellen.

So fügen Sie eine neue Kategorie hinzu:

1. Gehen Sie zu **Einstellungen** > **Nachrichtenpriorisierung** > **Kategorien**.
2. Wählen Sie **Neue Kategorie erstellen**.

![Der Button „Neue Kategorie erstellen“ im Abschnitt Nachrichtenpriorisierung.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. Geben Sie der Kategorie einen Namen und eine optionale Beschreibung.
4. Wählen Sie **Kategorie erstellen**.

![Eine Beispielkategorie mit dem Namen „P3“ und der Beschreibung „Dies wird meine dritthöchste Prioritätskategorie.“]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

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

Um Regeln neu zu ordnen, wählen und ziehen Sie das <i class="fa-solid fa-grip-vertical"></i>-Symbol oben links einer Regel. Um eine Regel zu löschen, wählen Sie das <i class="fas fa-ellipsis-vertical"></i>-Menü und dann **Regel löschen**.

Stellen Sie sicher, dass Sie **Speichern** auswählen, damit Ihre Änderungen übernommen werden.

## Einstellungen auf Campaign-Ebene {#campaign-level-settings}

### Opt-in

{% alert important %}
Derzeit können nur geplante Einkanal-Campaigns für die Priorisierung aktiviert werden. Aktionsbasierte und API-getriggerte Campaigns sowie Canvases werden nicht unterstützt.
{% endalert %}

Um eine Campaign für die Priorisierung zu aktivieren, wählen Sie das Kontrollkästchen **Opt-in zur Nachrichtenpriorisierung** auf der Seite **Zustellung planen** der Campaign.

![Das Kontrollkästchen für „Opt-in zur Nachrichtenpriorisierung“.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

Weisen Sie anschließend die Campaign einer Kategorie zu, indem Sie eine aus dem Dropdown-Menü **Kategorie** auswählen.

![Das Kontrollkästchen für „Opt-in zur Nachrichtenpriorisierung“.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

Sie können bis zu 25 aktive Campaigns gleichzeitig aktivieren. Entwürfe, gestoppte oder archivierte Campaigns zählen nicht zu diesem Limit.

### Wiederholungsfenster {#retry-window}

Ein Wiederholungsfenster ermöglicht es aktivierten Campaigns, bis zu drei Tage lang erneut zu versuchen, wenn der erste Versuch keine ausreichend hohe Priorität zum Senden hatte. An jedem folgenden Tag wird zur gleichen Zeit, zu der die Nachricht ursprünglich geplant war, ein erneuter Sendeversuch unternommen. Nach dem letzten Tag im Wiederholungsfenster wird die Nachricht, falls sie immer noch nicht gesendet wurde, nicht weiter versucht und dauerhaft herabgestuft.

Das Wiederholungsfenster muss kürzer sein als der Zeitraum zwischen den Sendungen dieser Campaign. Wenn eine Campaign jeden Montag und Mittwoch sendet, erfolgt der Wiederholungsversuch am Dienstag. Das bedeutet, dass das Wiederholungsfenster auf einen Tag eingestellt werden muss.

![Die Einstellung „Wiederholungsfenster“ auf 1 Tag eingestellt.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

## Frequency-Capping {#frequency-caps}

### Für Campaigns {#for-campaigns}

Um für die Nachrichtenpriorisierung berechtigt zu sein, muss eine Campaign für Frequency-Capping aktiviert sein. Sie können bestätigen, dass die Campaign aktiviert ist, im Abschnitt **Zustellungs-Kontrollgruppen** auf der Seite **Zustellung planen**.

![Ein Beispiel für die Frequency-Capping-Regel für jeden anwendbaren Kanal und ohne zusätzliche Filter.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### Frequency-Capping-Regeln {#frequency-capping-rules}

Wir optimieren die Priorität innerhalb Ihrer bestehenden Frequency-Capping-Regeln. Obwohl nicht erforderlich, empfehlen wir dringend, mindestens eine Frequency-Capping-Regel festzulegen, die alle Nachrichten unabhängig von Kanal, Tag oder Kategorie erfasst. Diese Frequency-Capping-Regel erfasst jede Nachricht, die für die Nachrichtenpriorisierung aktiviert ist, sodass priorisierte Nachrichten miteinander verglichen werden – nicht nur mit anderen Nachrichten, die dieselben Merkmale teilen.

Um dies einzurichten, gehen Sie zu **Einstellungen** > **Frequency-Capping-Regeln**. Erstellen Sie eine Regel, bei der der Kanal **Jeder anwendbare Kanal** ist und zusätzliche Filter auf **Keine** gesetzt sind.

![Ein Beispiel für die Frequency-Capping-Regel für jeden anwendbaren Kanal und ohne zusätzliche Filter.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization11.png %})

Sie können auch Frequency-Capping-Regeln nach Kategorie erstellen. So können Sie Ihre Marketing-Nachrichten verwalten und vermeiden, zu viele Nachrichten aus einer bestimmten Kategorie zu senden, nur weil sie als hohe Priorität markiert ist. Wählen Sie **Nachrichtenpriorisierungs-Kategorie** unter **Zusätzliche Filter** und wählen Sie eine Kategorie aus dem Dropdown-Menü.

![Ein Beispiel für die Frequency-Capping-Regel mit dem Dropdown-Feld „Kategorie“ zur Auswahl von P2 oder P1.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

Nachrichten außerhalb der Nachrichtenpriorisierung teilen sich die Frequency-Cap-Limits mit priorisierten Nachrichten, sodass selbst eine Nachricht mit hoher Priorität aufgrund einer Nachricht außerhalb der Nachrichtenpriorisierung abgebrochen werden kann.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie werden Gleichstände zwischen Nachrichten in derselben Kategorie aufgelöst? {#how-are-ties-broken-between-messages-in-the-same-category}

Bei der Priorisierung zweier Nachrichten in derselben Kategorie wird der Nachricht mit der frühesten Sendezeit eine höhere Priorität eingeräumt. Bei wiederkehrenden Campaigns wird die Sendezeit als das nächste Vorkommen ab Mitternacht des heutigen Tages in Unternehmenszeit berechnet. Bei Campaigns, die in Ortszeit geplant sind, wird eine Sendezeit in Unternehmenszeit angenommen.

### Welche Beziehung besteht zwischen Nachrichtenpriorisierung und Frequency-Capping? {#what-is-the-relationship-between-message-prioritization-and-frequency-capping}

Zum Sendezeitpunkt vergleichen wir die zu sendende Nachricht mit anderen Nachrichten, für die die Nutzer:innen berechtigt sind, die derselben Frequency-Capping-Regel folgen und für die Nachrichtenpriorisierung aktiviert sind. Die Nachricht wird gesendet, wenn:

1. Die relevante Frequency-Capping-Regel für diese Nutzer:innen noch nicht erreicht wurde, und
2. Das Senden dieser Nachricht an diese Nutzer:innen nicht dazu führen würde, dass ein Cap erreicht wird, bevor eine nachfolgende Nachricht mit höherer Priorität gesendet wird.

### Wie kann ich sicherstellen, dass eine Nachricht immer gesendet wird? {#how-can-i-make-sure-a-message-is-always-sent}

Es kann Szenarien geben, in denen Sie möchten, dass eine Nachricht immer gesendet wird, z. B. bei transaktionalen oder rechtlichen Benachrichtigungen. In diesem Fall sollten Sie die Nachricht vom Frequency-Capping abmelden (was sie auch für die Nachrichtenpriorisierung nicht berechtigt macht). Dadurch wird die Nachricht immer dann gesendet, wenn sie geplant oder getriggert wird, ohne Berücksichtigung anderer Sendungen.

### Wann werden Nachrichten tatsächlich priorisiert? Gibt es einen Zeitplan? {#when-are-messages-actually-prioritized-is-there-a-schedule}

Jede Nachricht wird zu ihrem eigenen geplanten Sendezeitpunkt priorisiert. Es gibt keinen universellen Auswertungszeitpunkt für priorisierte Nachrichten.

### Meine Nachricht war bereits zum Senden geplant, wurde aber aufgrund von Rate-Limiting oder anderen Verzögerungen noch nicht gesendet. Was bedeutet das für die Priorisierung anderer Campaigns? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

Wir gehen davon aus, dass Ihre Nachricht zum ursprünglich geplanten Zeitpunkt gesendet wurde, wenn sie noch verarbeitet wird. Wir verwenden diese Annahme, um zu bestimmen, ob andere bevorstehende priorisierte Nachrichten gesendet werden sollen. Wenn die Nachricht letztendlich gesendet wird, verwenden wir die tatsächliche Sendezeit.

### Meine Nachricht wurde priorisiert, aber in letzter Minute abgebrochen. Was bedeutet das für die Priorisierung? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

Wenn eine Nachricht priorisiert wird, geht Braze davon aus, dass sie zum ursprünglich geplanten Zeitpunkt gesendet wurde. Generell empfehlen wir für die Nachrichtenpriorisierung nicht die Verwendung von Liquid-Abbrüchen. Wenn eine Nachricht aufgrund von [`abort_message`-Liquid-Logik](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) abgebrochen wird, gehen wir davon aus, dass sie an diese Nutzer:innen gesendet wurde, und priorisieren zukünftige Campaigns entsprechend.

Nehmen wir an, Sie haben zwei Nachrichten: Nachricht 1 und Nachricht 2. Wenn Nachricht 1 zugunsten einer zukünftigen Nachricht 2 mit höherer Priorität abgebrochen wird, garantiert dies nicht, dass Nachricht 2 tatsächlich gesendet wird. Nachricht 2 kann aus verschiedenen Gründen ebenfalls abgebrochen werden, darunter:

- Liquid-Abbruchnachrichten
- Die Nutzer:innen befinden sich nicht mehr im Segment
- Frequency-Caps aufgrund einer Nachricht außerhalb der Priorisierungsregeln.

Wenn Nachricht 2 abgebrochen wird, gibt es keinen weiteren Versuch, Nachricht 1 zu senden.

Beachten Sie, dass Nutzer:innen eine Nachricht mit niedrigerer Priorität erhalten könnten, aber nicht eine Nachricht mit höherer Priorität für dieselbe Frequency-Capping-Regel, aus folgenden Gründen:

- Die Nachricht mit höherer Priorität wurde durch eine andere Regel einem Frequency-Cap unterworfen.
- Die Nachricht mit höherer Priorität stand im Konflikt mit einer anderen, zukünftigen Campaign mit noch höherer Priorität für eine andere Regel.
- Zum Zeitpunkt des Sendens der Nachricht mit niedrigerer Priorität befanden sich die Nutzer:innen nicht in der Zielgruppe für die Nachricht mit höherer Priorität.
- Beide Nachrichten hätten gesendet werden können, aber eine Nachricht außerhalb der Priorisierungseinrichtung wurde vor der Nachricht mit höherer Priorität gesendet.

### Kann ich Canvases für die Nachrichtenpriorisierung aktivieren? {#can-i-opt-canvases-into-message-prioritization}

Nein. Derzeit können Sie Canvases nicht für die Nachrichtenpriorisierung aktivieren.

### Was ist mit aktionsbasierten oder API-getriggerten Campaigns? {#what-about-action-based-or-api-triggered-campaigns}

Derzeit wird die Nachrichtenpriorisierung für aktionsbasierte oder API-getriggerte Campaigns nicht unterstützt.

### Gibt es Berichts- oder Analytics-Funktionen speziell für die Nachrichtenpriorisierung? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Derzeit gibt es keine Berichts- oder Analytics-Funktionen speziell für dieses Feature. Wir empfehlen Ihnen, die bestehende [Braze-Berichtsfunktionalität](https://www.braze.com/docs/user_guide/analytics/reporting) zu nutzen, um den Zustand und die Performance Ihrer priorisierten Campaigns zu überwachen.