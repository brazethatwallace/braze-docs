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

### Wie Nutzer:innen aussteigen {#how-users-exit}

Wenn ein:e Nutzer:in das Ausstiegs-Event ausführt, markiert Braze sie sofort für den Ausstieg aus dem Canvas. Danach gelangen sie nicht mehr zu späteren Schritten.

Wenn sie sich in einem Delay-Schritt befinden, bleiben sie in diesem Schritt, bis die Verzögerungszeit abgelaufen ist. Sie gelangen nach Ablauf der Verzögerung nicht in nachfolgende Schritte – stattdessen verlassen sie den Canvas vollständig. Je nachdem, wo Sie die Canvas-Daten einsehen, können Sie ausstiegsbezogene Aktivitäten sowohl beim Eintreten des Ausstiegs-Events als auch beim Abschluss des Delay-Schritts und dem vollständigen Ausstieg der Nutzer:innen aus dem Canvas sehen.

Wenn sich ein:e Nutzer:in beispielsweise in einem Delay-Schritt von 30 Tagen befindet und am ersten Tag des Delay-Schritts das Ausstiegs-Event ausführt, wird sie sofort für den Ausstieg markiert, verlässt den Canvas aber erst vollständig, wenn der Delay-Schritt endet (29 Tage später).

Betrachten wir ein weiteres Beispiel mit zeitbasierten Ausstiegskriterien. Ein:e Nutzer:in tritt am 1. Juli um 0:00 Uhr in einen Delay-Schritt ein, der auf 24 Stunden eingestellt ist. Während dieser Verzögerungszeit führt sie um 3:00 Uhr das Ausstiegs-Event „Letzter Kauf vor weniger als 1 Stunde“ aus. Diese:r Nutzer:in wird am 2. Juli um 0:00 Uhr auf die Ausstiegskriterien geprüft, also zum Abschluss der Delay-Schritt-Dauer. Da seit dem Kauf am 1. Juli um 3:00 Uhr 21 Stunden vergangen sind, wird sie den Canvas nicht verlassen, da sie nicht innerhalb einer Stunde vor dem Ende des Delay-Schritts am 2. Juli einen Kauf getätigt hat. Dies wirkt sich auf die „Gesamtausstiege nach Ausstiegskriterien“ in Ihren Canvas-Analytics aus, die erst aktualisiert werden, nachdem ein:e Nutzer:in den Canvas vollständig verlassen hat.

## Ausstiegskriterien einrichten {#setting-up-exit-criteria}

Im Schritt **Zielgruppe** des Canvas-Builders können Sie Ausstiegskriterien einrichten, um festzulegen, welche Nutzer:innen Ihren Canvas verlassen sollen.

Die Ausstiegskriterien umfassen ein Ausnahme-Event – die spezifische Aktion, die dazu führen kann, dass Nutzer:innen den Canvas verlassen.

![Die Ausstiegskriterien sind so eingerichtet, dass Nutzer:innen erneut angesprochen werden, die Produkte durchsucht, aber noch nicht in den Warenkorb gelegt oder eine Bestellung aufgegeben haben.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Ausnahme-Events auswählen {#exception-events}

Wenn ein:e Nutzer:in das Ausnahme-Event ausführt, markiert Braze sie für den Ausstieg gemäß [Wie Nutzer:innen aussteigen](#how-users-exit). Ausnahme-Events gelten, solange sich ein:e Nutzer:in im Canvas befindet, auch wenn sie in einem Schritt wie einem Delay-Schritt warten.

Angenommen, Sie haben einen Canvas eingerichtet, um ein neues Produkt zu bewerben. In diesem Fall wäre der Kauf des Produkts das Ausnahme-Event. Auf diese Weise erhält ein:e Nutzer:in nach dem Kauf keine weiteren Nachrichten über ein Produkt, das sie bereits gekauft hat. Ausnahme-Events sorgen dafür, dass Ihr Messaging relevant und personalisiert bleibt.

Weitere Ausnahme-Events umfassen:

- Einen Kauf tätigen
- Eine Sitzung starten
- Ein angepasstes Event ausführen
- Ein Konversions-Event ausführen
- Eine E-Mail-Adresse hinzufügen
- Einen angepassten Attributwert ändern
- Einen Abo-Status aktualisieren
- Einen Abo-Gruppenstatus aktualisieren
- Mit einer Campaign interagieren
- Einen Standort betreten
- Einen Geofence triggern
- Eine eingehende SMS-Nachricht senden
- Eine eingehende WhatsApp-Nachricht senden
- Eine eingehende LINE-Nachricht senden
- Ein Warenkorb-Update-Event ausführen
- Ein Checkout-abgeschlossen-Event ausführen
- Ein Checkout-gestartet-Event ausführen

#### Geplante Schritte {#scheduled-steps}

Bei Canvas-Schritten, die Nutzer:innen nicht in einem Delay-Schritt bis zu einem zukünftigen Zeitpunkt halten, verlassen Nutzer:innen den Canvas in der Regel, sobald der aktuelle Schritt abgeschlossen ist. Dieser Abschluss erfolgt oft unmittelbar nach dem Ausnahme-Event, da für diesen Schritt kein verbleibender Verzögerungs-Timer läuft. Dies unterscheidet sich von einem Delay-Schritt, bei dem Nutzer:innen bis zum Ende der Verzögerung bleiben, auch nachdem sie für den Ausstieg markiert wurden (siehe [Wie Nutzer:innen aussteigen](#how-users-exit)).

#### Getriggerte Schritte {#triggered-steps}

Wenn ein Canvas-Schritt durch ein Event getriggert wird, wird der letzte geplante Versand, der durch diesen Trigger in die Warteschlange gestellt wurde, abgebrochen, aber die Nutzer:innen bleiben für die Dauer des Fensters im Canvas. Das bedeutet, dass Nutzer:innen den Schritt dennoch erhalten können, wenn sie das Trigger-Event innerhalb des Fensters erneut ausführen. Nach Ablauf des Fensters verlassen die Nutzer:innen den Canvas.

### Segmente und Filter verwenden {#using-segments-and-filters}

Sie können auch Segmente und Filter in den Ausstiegskriterien hinzufügen. Das bedeutet, dass Nutzer:innen, die dem Segment und Filter entsprechen, den Canvas verlassen und keine weiteren Nachrichten erhalten.

Wenn beispielsweise der erste Schritt in einem Canvas ein Delay-Schritt mit einer fünftägigen Verzögerung ist, werden die Ausstiegskriterien geprüft, wenn dieser Schritt abgeschlossen ist. Wenn ein:e Nutzer:in die Ausstiegskriterien erfüllt, während sie sich im Delay-Schritt befindet, wird sie sofort für den Ausstieg markiert, verlässt den Canvas aber erst vollständig am Ende der fünf Tage (und gelangt nicht zu Schritten nach dem Delay).

{% alert note %}
Array-Attribute werden derzeit nicht als Ausstiegskriterien bei Ausnahme-Events unterstützt.
{% endalert %}

### Gleiches Ausstiegs-Event und Konversions-Event {#having-the-same-exit-event-and-conversion-event}

Wenn das Ausstiegs-Event und das Konversions-Event identisch sind, werden sowohl das Konversions- als auch das Ausstiegs-Event berücksichtigt. Wenn ein Canvas beispielsweise einen Delay-Schritt hat und ein:e Nutzer:in die Ausstiegskriterien während dieses Delay-Schritts erfüllt, wird das Ausstiegs-Event gezählt, sobald die Nutzer:innen den Delay-Schritt verlassen. Die Conversion wird ebenfalls gezählt, sobald das Event im Nutzerprofil protokolliert wird.

Conversions werden auch nach dem Ende des Canvas erfasst, Ausstiege jedoch nicht mehr, nachdem die Nutzer:innen den Canvas verlassen haben. Das Conversion-Fenster erstreckt sich bis zu drei Tage über die maximale Dauer des Canvas hinaus. Das bedeutet, dass Conversions weiterhin erfasst werden, nachdem die Erfassung von Ausstiegen bereits beendet ist.

Die Mindestzeit für ein Conversion-Fenster beträgt fünf Minuten. Stellen Sie die Conversion-Fenster für Ihre Konversions-Events auf fünf Minuten ein, um eine möglichst genaue Übereinstimmung mit den Ausstiegs-Events zu erreichen. Wir empfehlen außerdem, das Conversion-Fenster mindestens auf die Dauer des längsten Pfads im Canvas einzustellen.

Betrachten Sie das folgende Beispiel zur Berechnung der Analytics:

1. Zehn Nutzer:innen durchlaufen den Canvas.
2. Drei Nutzer:innen führen das Konversions-Event innerhalb von fünf Minuten aus (die Anzahl der Ausstiegs-Events beträgt drei, und die Anzahl der Konversions-Events beträgt drei).
3. Weitere fünf Nutzer:innen verlassen den Canvas nach fünf Minuten, führen aber das Konversions-Event nach zwei Tagen aus (die Anzahl der Ausstiegs-Events bleibt gleich, aber die Konversions-Events steigen auf acht).
4. Die letzten zwei Nutzer:innen verlassen den Canvas nach fünf Minuten, führen aber das Konversions-Event nicht aus oder führen es erst nach drei Tagen und fünf Minuten aus (sie werden weder bei den Ausstiegs-Events noch bei den Konversions-Events gezählt).

## Beispiel {#example}

Angenommen, wir möchten Nutzer:innen ansprechen, die noch keinen Kauf bei unserem Rucksack-Unternehmen getätigt haben. Um die Ausstiegskriterien einzurichten, würden wir:

1. **Place an Order** als Ausnahme-Event auswählen.
2. **Add Trigger** auswählen.
3. Für **Segments** die Option **Used in last day** auswählen, damit beim Start unseres Canvas die Zielgruppe Nutzer:innen ausschließt, die bereits Käufe getätigt haben.
4. Für **Filter** die Option **Purchase behavior** > **Number of purchases** > **Purchased product** auswählen.
5. Die Filtergruppe auf `backpack-example exactly 1` setzen. Das bedeutet, dass Nutzer:innen, die unser Rucksack-Produkt gekauft haben, den Canvas verlassen würden.

![Ausstiegskriterien-Einstellungen mit „Makes Any Purchase“ als Ausnahme-Event. Wenn ein:e Nutzer:in einen Kauf tätigt, verlässt sie diesen Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}

{% alert tip %}
Um Ausstiegskriterien einzurichten, die Event-Eigenschaften mit Canvas-Eingangs-Eigenschaften vergleichen (z. B. nur dann aussteigen, wenn ein:e Nutzer:in den spezifischen Artikel kauft, den sie aufgegeben hat), lesen Sie [Ausstiegskriterien mit Eingangs-Events abgleichen]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/matching_entry_and_exit_criteria/).
{% endalert %}