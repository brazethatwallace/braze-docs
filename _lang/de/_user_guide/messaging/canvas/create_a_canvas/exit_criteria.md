---
nav_title: Ausstiegskriterien
article_title: Ausstiegskriterien
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Dieser Referenzartikel behandelt Ausstiegskriterien und wie Nutzer:innen Ihren Canvas basierend auf den ausgewählten Kriterien verlassen können."
tool: Canvas
---

# Ausstiegskriterien {#exit-criteria}

> Indem Sie Ausnahme-Events direkt zu Ihren Canvas-Eingangsregeln hinzufügen, können Sie Nutzer:innen aus der Journey entfernen, wenn sie eine bestimmte Aktion ausführen.
> Braze erfasst den Ausstieg, sobald das Event eintritt.
> Wie schnell ein:e Nutzer:in den Canvas vollständig verlässt, hängt vom Schritt ab, in dem sie sich befinden – insbesondere bei Delay-Schritten.
> Weitere Informationen finden Sie unter [Wie Nutzer:innen aussteigen](#how-users-exit).

## So verlassen Nutzer:innen den Canvas {#how-users-exit}

Wenn Nutzer:innen das Exit-Event ausführen, markiert Braze sie sofort zum Verlassen des Canvas. Danach werden sie nicht mehr zu späteren Schritten weitergeleitet.

Wenn sie sich in einem Verzögerungsschritt befinden, bleiben sie in diesem Schritt, bis die Verzögerungszeit abgelaufen ist. Sie gelangen nach Ablauf der Verzögerung nicht in nachfolgende Schritte – stattdessen verlassen sie den Canvas vollständig. Je nachdem, wo Sie die Canvas-Daten einsehen, können Sie Exit-bezogene Aktivitäten sowohl beim Auftreten des Exit-Events als auch beim Abschluss des Verzögerungsschritts und dem endgültigen Verlassen des Canvas sehen.

Wenn sich Nutzer:innen beispielsweise in einem Verzögerungsschritt von 30 Tagen befinden und das Exit-Event am ersten Tag des Verzögerungsschritts ausführen, werden sie sofort zum Verlassen markiert, verlassen den Canvas jedoch erst vollständig, wenn der Verzögerungsschritt endet (29 Tage später).

Betrachten wir ein weiteres Beispiel mit zeitbasierten Exit-Kriterien. Nutzer:innen treten am 1. Juli um 0:00 Uhr in einen auf 24 Stunden eingestellten Verzögerungsschritt ein. Während dieser Verzögerungszeit führen sie um 3:00 Uhr das Exit-Event „Letzte Bestellung vor weniger als 1 Stunde aufgegeben“ aus. Diese Nutzer:innen werden am 2. Juli um 0:00 Uhr auf die Exit-Kriterien hin geprüft, also zum Abschluss der Dauer des Verzögerungsschritts. Da seit ihrer Bestellung am 1. Juli um 3:00 Uhr 21 Stunden vergangen sind, verlassen sie den Canvas nicht, weil sie nicht innerhalb der einen Stunde vor dem Verlassen des Verzögerungsschritts am 2. Juli eine Bestellung aufgegeben haben. Dies wirkt sich auf die „Total Exits by Exit Criteria“ in Ihren Canvas-Analytics aus, die erst aktualisiert werden, nachdem Nutzer:innen den Canvas vollständig verlassen haben.

## Exit-Kriterien einrichten {#setting-up-exit-criteria}

Im Schritt **Zielgruppe zusammenstellen** des Canvas-Builders können Sie Exit-Kriterien festlegen, um zu bestimmen, welche Nutzer:innen Ihren Canvas verlassen sollen.

Die Exit-Kriterien umfassen ein Ausnahme-Event – die spezifische Aktion, die dazu führen kann, dass Nutzer:innen den Canvas verlassen.

![Die eingerichteten Exit-Kriterien zur Reaktivierung von Nutzer:innen, die Produkte angesehen, aber noch nicht in den Warenkorb gelegt oder eine Bestellung aufgegeben haben.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Ausnahme-Events auswählen {#exception-events}

Wenn eine Nutzerin oder ein Nutzer das Ausnahme-Event ausführt, markiert Braze sie für den Exit gemäß [Wie Nutzer:innen den Canvas verlassen](#how-users-exit). Ausnahme-Events gelten, solange sich Nutzer:innen im Canvas befinden – auch wenn sie in einem Schritt wie einem Delay-Schritt warten.

Angenommen, Sie haben einen Canvas eingerichtet, um ein neues Produkt zu bewerben. In diesem Fall wäre die Bestellung des Produkts das Ausnahme-Event. Auf diese Weise erhalten Nutzer:innen nach einer Bestellung keine weiteren Nachrichten über ein Produkt, das sie bereits gekauft haben. Ausnahme-Events sorgen dafür, dass Ihr Messaging relevant und personalisiert bleibt.

Weitere Ausnahme-Events umfassen:

- Bestellung aufgeben
- Sitzung starten
- Angepasstes Event ausführen
- Konversions-Event ausführen
- E-Mail-Adresse hinzufügen
- Wert eines angepassten Attributs ändern
- Abo-Status aktualisieren
- Abo-Gruppenstatus aktualisieren
- Mit einer Campaign interagieren
- Einen Standort betreten
- Einen Geofence triggern
- Eingehende SMS-Nachricht senden
- Eingehende WhatsApp-Nachricht senden
- Eingehende LINE-Nachricht senden
- Warenkorb-Aktualisierungs-Event ausführen

#### Geplante Schritte {#scheduled-steps}

Bei Canvas-Schritten, die Nutzer:innen nicht in einem Delay-Schritt bis zu einem zukünftigen Zeitpunkt halten, verlassen Nutzer:innen den Canvas in der Regel, sobald der aktuelle Schritt abgeschlossen ist. Dieser Abschluss erfolgt oft unmittelbar nach dem Ausnahme-Event, da kein verbleibender Delay-Timer für diesen Schritt aktiv ist. Dies unterscheidet sich von einem Delay-Schritt, bei dem Nutzer:innen bis zum Ende der Verzögerung verbleiben, auch nachdem sie für den Exit markiert wurden (siehe [Wie Nutzer:innen den Canvas verlassen](#how-users-exit)).

#### Getriggerte Schritte {#triggered-steps}

Wenn ein Canvas-Schritt durch ein Event getriggert wird, wird der letzte geplante Versand, der durch diesen Trigger in die Warteschlange gestellt wurde, abgebrochen. Die Nutzerin oder der Nutzer bleibt jedoch für die Dauer des Zeitfensters im Canvas. Das bedeutet, dass der Schritt erneut gesendet werden kann, wenn das Trigger-Event innerhalb des Zeitfensters erneut ausgeführt wird. Nach Ablauf des Zeitfensters verlassen die Nutzer:innen den Canvas.

### Segmente und Filter verwenden {#using-segments-and-filters}

Sie können in den Exit-Kriterien auch Segmente und Filter hinzufügen. Das bedeutet, dass Nutzer:innen, die dem Segment und Filter entsprechen, den Canvas verlassen und keine weiteren Nachrichten erhalten.

Wenn beispielsweise der erste Schritt eines Canvas ein Delay-Schritt mit einer fünftägigen Verzögerung ist, werden die Exit-Kriterien ausgewertet, wenn dieser Schritt abgeschlossen ist. Wenn Nutzer:innen die Exit-Kriterien erfüllen, während sie sich im Delay-Schritt befinden, werden sie sofort für den Exit markiert, verlassen den Canvas jedoch erst nach Ablauf der fünf Tage vollständig (und sie werden nicht zu nachfolgenden Schritten nach dem Delay voranbracht).

{% alert note %}
Array-Attribute werden derzeit nicht als Exit-Kriterien bei Ausnahme-Events unterstützt.
{% endalert %}

### Gleiches Exit-Event und Konversions-Event {#having-the-same-exit-event-and-conversion-event}

Wenn das Exit-Event und das Konversions-Event identisch sind, werden sowohl die Konversion als auch das Exit-Event berücksichtigt. Wenn ein Canvas beispielsweise einen Delay-Schritt hat und Nutzer:innen die Exit-Kriterien während dieses Delay-Schritts erfüllen, wird das Exit-Event inkrementiert, sobald sie den Delay-Schritt verlassen. Die Konversion wird ebenfalls inkrementiert, sobald das Event im Nutzerprofil protokolliert wird.

Konversionen werden auch nach dem Ende des Canvas erfasst, Exits hingegen nicht mehr, nachdem Nutzer:innen den Canvas verlassen haben. Das Konversionsfenster erstreckt sich bis zu drei Tage über die maximale Dauer des Canvas hinaus. Das bedeutet, dass Konversionen weiterhin erfasst werden, nachdem die Erfassung von Exits bereits eingestellt wurde.

Die Mindestdauer für ein Konversionsfenster beträgt fünf Minuten. Stellen Sie die Konversionsfenster auf fünf Minuten ein, damit Ihre Konversions-Events so nah wie möglich an die Exit-Events herankommen. Wir empfehlen außerdem, das Konversionsfenster mindestens auf die Dauer des längsten Pfads im Canvas einzustellen.

Betrachten Sie das folgende Beispiel zur Berechnung der Analytics:

1. Zehn Nutzer:innen durchlaufen den Canvas.
2. Drei Nutzer:innen führen das Konversions-Event innerhalb von fünf Minuten aus (die Anzahl der Exit-Events beträgt drei und die Anzahl der Konversions-Events beträgt drei).
3. Weitere fünf Nutzer:innen verlassen den Canvas nach fünf Minuten, führen das Konversions-Event aber nach zwei Tagen aus (die Anzahl der Exit-Events bleibt gleich, aber die Konversions-Events steigen auf acht).
4. Die letzten beiden Nutzer:innen verlassen den Canvas nach fünf Minuten, führen das Konversions-Event aber nicht aus oder führen es nach drei Tagen und fünf Minuten aus (sie werden weder in den Exit-Event- noch in den Konversions-Event-Metriken gezählt).

## Beispiel {#example}

Angenommen, wir möchten Nutzer:innen ansprechen, die noch keine Bestellung bei unserem Rucksack-Unternehmen aufgegeben haben. Um die Exit-Kriterien einzurichten, würden wir Folgendes tun:

1. Wählen Sie **Bestellung aufgeben** als Ausnahme-Event aus.
2. Wählen Sie **Trigger hinzufügen** aus.
3. Wählen Sie unter **Segments** die Option **Am letzten Tag verwendet** aus, damit beim Start unseres Canvas die Zielgruppe Nutzer:innen ausschließt, die bereits Käufe getätigt haben.
4. Wählen Sie unter **Filter** die Option **Kaufverhalten** > **Anzahl der Käufe** > **Gekauftes Produkt** aus.
5. Setzen Sie die Filtergruppe auf `backpack-example exactly 1`. Das bedeutet, dass Nutzer:innen, die unser Rucksack-Produkt gekauft haben, den Canvas verlassen würden.

![Einstellungen für Exit-Kriterien mit „Beliebigen Kauf tätigen“ als Ausnahme-Event – wenn Nutzer:innen einen Kauf tätigen, verlassen sie diesen Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}

{% alert tip %}
Um Exit-Kriterien einzurichten, die Event-Eigenschaften mit Canvas-Entry-Eigenschaften vergleichen (z. B. Exit nur dann, wenn Nutzer:innen den bestimmten Artikel kaufen, den sie abgebrochen haben), lesen Sie [Exit-Kriterien mit Entry-Events abgleichen]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria).
{% endalert %}