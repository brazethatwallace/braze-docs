---
nav_title: Konversions-Events
article_title: Konversions-Events
page_order: 3
page_type: reference
description: "Dieser Referenzartikel definiert Konversions-Events, erklärt, wie Sie damit Ihre Erfolgsmetriken in Braze festlegen, und wie Sie diese Events nutzen können, um zu sehen, wie engagiert Ihre Nutzer:innen sind."
tool:
    - Campaigns
    - Canvas
---

# Konversions-Events {#conversion-events}

> Ein Konversions-Event ist eine Art Erfolgsmetrik, die erfasst, ob ein:e Empfänger:in Ihrer Nachrichten innerhalb eines festgelegten Zeitraums nach Erhalt Ihres Engagements eine wertvolle Aktion ausführt. Nutzen Sie diese Events, um sicherzustellen, dass Sie relevante, nützliche Informationen sammeln, die Sie später verwenden können, um Insights für Ihre Campaign oder Ihren Canvas zu gewinnen.

## So funktioniert es {#how-it-works}

Für eine personalisierte Feiertagskampagne, die auf aktive Nutzer:innen abzielt, kann ein Konversions-Event von **Sitzung starten** innerhalb von zwei oder drei Tagen angemessen sein, da es Ihnen ermöglicht, ein Gefühl für das Nutzer:innen-Engagement nach Erhalt Ihrer Nachricht zu bekommen. Sie können auch zusätzliche Events wie **Bestellung aufgeben**, **App upgraden** oder eines Ihrer angepassten Events als Konversions-Events auswählen.

### Wann beginnt das Konversions-Tracking? {#when-does-conversion-tracking-begin}

{% tabs %}
{% tab Campaign %}

Das Konversions-Tracking beginnt, wenn Nutzer:innen die Campaign erhalten oder der Kontrollgruppe der Campaign zugewiesen werden. Der Empfang einer Nachricht und die Zuweisung zu einer Variante erfolgen in der Regel gleichzeitig. Bei In-App-Nachricht-Campaigns beginnt das Konversions-Tracking, wenn Braze eine Impression erfasst.

{% endtab %}
{% tab Canvas %}

Das Konversions-Tracking beginnt, wenn Nutzer:innen den Canvas betreten. Bei Canvas-Schritten werden Konversionen zugeordnet, solange die Nutzer:innen in diesem Schritt aktiv sind. Wenn die Nutzer:innen zum nächsten Schritt weitergehen, stoppt das Konversions-Tracking für den vorherigen Schritt und beginnt für den nächsten Schritt.

Während sich Nutzer:innen in einem Verzögerungsschritt oder einem anderen Schritt ohne Nachricht befinden, werden Konversionen, die während dieser Wartezeit auftreten, weiterhin dem zuletzt empfangenen Nachrichtenschritt zugeordnet, bis die Nutzer:innen einen weiteren Nachrichtenschritt erhalten. Nachdem die Nutzer:innen den letzten Nachrichtenschritt in ihrem Pfad erhalten haben, können Konversionen weiterhin bis zur Konversionsfrist (gerechnet ab dem Canvas-Entry) erfasst werden, auch wenn keine weiteren Nachrichtenschritte folgen.

{% endtab %}
{% endtabs %}

{% alert tip %}
Weitere Informationen zu Konversionen finden Sie in unserem [Braze-Lernkurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Campaign-Einrichtung.
{% endalert %}

### Regeln für das Konversions-Tracking {#conversion-tracking-rules}

Konversions-Events ordnen Nutzer:innen-Aktionen einem Engagement-Punkt zu. Im Allgemeinen konvertieren Nutzer:innen, solange ein Konversionsfenster offen ist, höchstens einmal pro Konversions-Event für diese Campaign oder diesen Canvas. Wenn sie dieselbe Konversionsaktion vor Ablauf der Frist mehr als einmal ausführen (z. B. zwei Käufe), zählt Braze dennoch nur eine Konversion für dieses Event. Multichannel-Campaigns können für jeden Messaging-Kanal eine separate Konversions-Opportunity erfassen, was zu Konversionsraten von über 100 % führen kann, wenn Sie die Konversionsanzahl mit den eindeutigen Empfänger:innen vergleichen (wie in den folgenden Punkten beschrieben).

Beachten Sie Folgendes zur Handhabung mehrerer Konversionen durch Braze:

- **Einzelkanal-Campaigns:** Konversionen erfolgen pro Nutzer:in, nicht pro Gerät. Innerhalb eines einzelnen Kanals konvertieren Nutzer:innen nur einmal pro Konversions-Event, auch wenn eine Nachricht an mehrere Geräte gesendet wird. Wenn beispielsweise eine Campaign nur ein Konversions-Event hat, das auf „Beliebigen Kauf tätigen“ eingestellt ist, und Nutzer:innen zwei separate Käufe innerhalb der Konversionsfrist tätigen, zählt Braze nur eine Konversion. Wenn jedoch die [Wiederberechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) aktiviert ist, können Nutzer:innen, die die Campaign mehrmals erhalten, bei jedem Versand erneut konvertieren. Bei Campaigns mit Wiederberechtigung erfolgt der Konversionsmechanismus einmal pro Nutzer:in pro Campaign-Versand, was zu höheren Konversionsanzahlen führen kann, wenn Nutzer:innen dieselbe Campaign mehrmals erhalten und daraus konvertieren.
- **Multichannel-Campaigns:** Bei Multichannel-Campaigns hat jeder Kanal seine eigene Konversions-Opportunity. Nutzer:innen können einmal pro Kanal konvertieren, nachdem sie eine Nachricht auf diesem Kanal erhalten haben. Das bedeutet: Wenn Nutzer:innen Nachrichten auf mehreren Kanälen erhalten (z. B. sowohl E-Mail als auch Push) und die Konversionsaktion ausführen, zählt Braze eine Konversion für jeden Kanal, was zu Konversionsraten von über 100 % führen kann.
- **Canvas-Nachrichtenschritte:** Braze ordnet Konversionen, die innerhalb der Konversionsfrist auftreten, dem letzten Canvas-Nachrichtenschritt zu, den die Nutzer:innen erhalten haben. Nachdem sie den nächsten Nachrichtenschritt erhalten, wird die Zuordnung auf diesen Schritt übertragen. Braze misst dieses Fenster ab dem Zeitpunkt, an dem die Nutzer:innen den Canvas betreten, nicht ab jeder einzelnen Nachricht. Konversionen, die während Verzögerungen zwischen Nachrichtenschritten auftreten, werden der Zuordnung des vorherigen Nachrichtenschritts zugerechnet, bis die Nutzer:innen weitergehen; Konversionen nach dem letzten Nachrichtenschritt zählen weiterhin bis zur Canvas-Konversionsfrist.
- **Historische Event-Aufbewahrung:** Das Konversions-Tracking auf Campaign- und Canvas-Dashboards misst historische Aktionen, nicht aktuelle Nutzerprofile. Wenn Nutzer:innen eine Konversionsregel innerhalb des festgelegten Fensters erfüllen, erfasst Braze eine Konversion in den Analytics und entfernt sie nicht, selbst wenn das Profil dieser Nutzer:innen später im Rahmen routinemäßiger Datenpflege oder DSGVO-Compliance gelöscht, zusammengeführt oder archiviert wird. Live-Segment-Zählungen können naturgemäß niedriger sein als Ihre permanenten Dashboard-Event-Protokolle, da dynamische Segmente nur aktive Profile filtern, die aktuell in der Datenbank vorhanden sind.
- Wenn Nutzer:innen ein Konversions-Event innerhalb der Konversionsfristen von zwei separaten Campaigns oder Canvases ausführen, die sie erhalten haben, wird die Konversion bei beiden registriert.
- Nutzer:innen gelten als konvertiert, wenn sie das spezifische Konversions-Event innerhalb des Fensters ausgeführt haben, auch wenn sie die Nachricht nicht geöffnet oder angeklickt haben.

### Primäres Konversions-Event {#primary-conversion-event}

Das primäre Konversions-Event ist das erste Event, das Sie während der Campaign- oder Canvas-Erstellung hinzufügen. Dieses Event hat den größten Einfluss auf Ihr Engagement und Ihre Berichterstattung. Braze verwendet Ihr primäres Konversions-Event, um:

- Die Gewinnervariante in [multivariaten]({{site.baseurl}}/user_guide/messaging/ab_testing/optimizations#winning-variant) Campaigns oder Canvases zu ermitteln.
- Das Fenster zu bestimmen, in dem der Umsatz für die Campaign oder den Canvas berechnet wird.
- Die Nachrichtenverteilung für Campaigns und Canvases mithilfe der [intelligenten Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) anzupassen.

Die Anzahl der primären Konversions-Events ist die Anzahl der aufgetretenen Konversions-Events. Bei Multichannel-Campaigns zählt Braze Konversionen pro Kanal (wie unter [Regeln für das Konversions-Tracking](#conversion-tracking-rules) beschrieben), was bedeutet, dass die Konversionsanzahl die Anzahl der eindeutigen Nutzer:innen übersteigen und zu Konversionsraten von über 100 % führen kann. Braze berechnet die Rate des primären Konversions-Events, indem diese Anzahl durch die Anzahl der eindeutigen Empfänger:innen geteilt wird. Braze betrachtet Nutzer:innen als Empfänger:innen, wenn die Nachricht gesendet oder angezeigt wird, je nach Kanal. Beispielsweise werden Nutzer:innen bei Push oder E-Mail zu Empfänger:innen, nachdem Braze die Nachricht gesendet hat. Bei In-App-Nachrichten oder Content Cards müssen die Nutzer:innen die Nachricht angesehen haben, um als Empfänger:innen zu gelten.

{% alert note %}
Wenn Sie Nachrichten mit dem Liquid-Tag `abort` abbrechen, bricht Braze Nachrichten nur für Nutzer:innen ab, die Varianten durchlaufen. Nachrichten an Nutzer:innen in der Kontrollgruppe werden nicht abgebrochen, was zu verzerrten Konversionsprozentsätzen zwischen Varianten und Kontrollgruppen führen kann. Als Workaround verwenden Sie die [Segmentierung]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), um Ihre Nutzer:innen beim Campaign- und Canvas-Entry zu targeten.
{% endalert %}

## Eine Campaign mit Konversions-Tracking erstellen {#creating-a-campaign-with-conversion-tracking}

### Schritt 1: Campaign einrichten {#step-1-set-up-your-campaign}

[Erstellen Sie eine Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign) für den gewünschten Messaging-Kanal. Nachdem Sie die Nachrichten und den Zeitplan Ihrer Campaign eingerichtet haben, können Sie bis zu vier Konversions-Events für das Tracking hinzufügen.

Verwenden Sie so viele Konversions-Events wie nötig. Das Hinzufügen eines zweiten oder dritten Konversions-Events bereichert Ihr Reporting erheblich. Wenn Sie beispielsweise eine Campaign erstellen, die auf passive Nutzer:innen abzielt, hilft Ihnen ein sekundäres Konversions-Event neben dem primären Konversions-Event **Starts Session** dabei zu verstehen, wie effektiv Ihre Campaign Nutzer:innen zurück in Ihre Anwendung bringt.

### Schritt 2: Konversions-Events hinzufügen {#step-2-add-the-conversion-events}

Wählen Sie zunächst den allgemeinen Event-Typ aus, den Sie verwenden möchten:

| Konversions-Event-Typ   | Beschreibung                |
|-------------------------|----------------------------|
| **Starts Session**      | Eine Konversion wird gezählt, wenn Nutzer:innen eine der von Ihnen angegebenen Apps öffnen (standardmäßig alle Apps im Workspace).|
| **Makes Purchase**      | Eine Konversion wird gezählt, wenn Nutzer:innen ein [Kauf-Event]({{site.baseurl}}/api/objects_filters/purchase_object) aufzeichnen. Standardmäßig wird jeder Kauf erfasst, Sie können aber auch ein bestimmtes Produkt angeben.|
| **Places Order**        | Eine Konversion wird gezählt, wenn Nutzer:innen das [empfohlene E-Commerce-Event „Order Placed“]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#ecommerce-recommended-events?tab=ecommerce.order_placed) auslösen. Standardmäßig wird jede Bestellung erfasst, Sie können aber nach einem bestimmten Produkt filtern.<br><br>Das Event „Places Order“ befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an diesem Early Access teilnehmen möchten. |
| **Performs Custom Event**| Eine Konversion wird gezählt, wenn Nutzer:innen eines Ihrer vorhandenen angepassten Events ausführen (kein Standard, Sie müssen das Event angeben).|
| **Upgrade App**         | Eine Konversion wird gezählt, wenn Nutzer:innen die App-Version einer der von Ihnen angegebenen Apps aktualisieren (standardmäßig alle Apps im Workspace). Braze führt einen Best-Effort-Zahlenvergleich durch, um festzustellen, ob es sich um ein Upgrade handelt. Nicht-numerische Versionen werden als Konversionen gezählt, wenn sich die Version ändert.|
| **Opens email**         | Eine Konversion wird gezählt, wenn Nutzer:innen die E-Mail öffnen (nur für E-Mail-Campaigns).|
| **Clicks email**        | Eine Konversion wird gezählt, wenn Nutzer:innen auf einen Link in der E-Mail klicken (nur für E-Mail-Campaigns).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Konversions-Events hinzufügen" }

{% alert important %}
**Verschachtelte Eigenschaften werden in Konversions-Events nicht unterstützt**. Sie können keine verschachtelten Eigenschaften in Konversions-Events verwenden. Wenn beispielsweise `product_code` oder `product_name` verschachtelte Eigenschaften innerhalb eines `products`-Arrays sind (z. B. `products[].product_code`), können Sie diese nicht verwenden, um zu prüfen, ob ein bestimmter Produktkauf in einem Konversions-Event stattgefunden hat.
{% endalert %}

Legen Sie Ihre Konversionsfrist fest. Dies ist die maximale Zeitspanne, die vergehen darf, bevor Braze eine Konversion berücksichtigt. Sie können ein Fenster von bis zu 30 Tagen festlegen, in dem Braze die Konversion zählt, wenn Nutzer:innen die angegebene Aktion ausführen.

![Der Konversions-Event-Typ „Makes Purchase“ als Beispiel, um Konversionen für Nutzer:innen zu erfassen, die einen beliebigen Kauf tätigen. Die Konversionsfrist beträgt 12 Stunden.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Nachdem Sie Ihre Konversions-Events ausgewählt haben, fahren Sie mit dem Campaign-Erstellungsprozess fort und beginnen Sie mit dem Versand Ihrer Campaign.

### Schritt 3: Ergebnisse anzeigen {#step-3-view-your-results}

Gehen Sie zur Seite **Details**, um die Details für jedes Konversions-Event anzuzeigen, das mit der von Ihnen erstellten Campaign verknüpft ist. Unabhängig von den ausgewählten Konversions-Events können Sie auch den Gesamtumsatz sehen, der dieser spezifischen Campaign sowie bestimmten Varianten während des Fensters des primären Konversions-Events zugeordnet wird.

{% alert note %}
Wenn Sie während der Campaign-Erstellung keine Konversions-Events auswählen, wird die Frist standardmäßig auf drei Tage gesetzt.
{% endalert %}

Darüber hinaus können Sie bei multivariaten Nachrichten die Anzahl der Konversionen und die Konversionsraten für Ihre Kontrollgruppe und jede Variante einsehen.

![Vier Konversions-Events, die Konversionen danach erfassen, ob ein Kauf innerhalb von drei Stunden getätigt wurde, ein Kauf innerhalb von zwei Stunden getätigt wurde, eine Sitzung innerhalb von 30 Minuten gestartet wurde und eine Sitzung innerhalb von 25 Minuten gestartet wurde.]({% image_buster /assets/img_archive/conversion_event_details.png %})

## Konversionsraten auf Canvas-Schritt- versus Variantenebene {#canvas-step-versus-variant-conversion-rates}

Es kommt häufig vor, dass die Gesamtzahl der Konversionen einer Canvas-Variante höher ist als die Summe der Konversionen ihrer einzelnen Schritte. Das liegt daran, dass Konversionen auf Variantenebene und auf Schrittebene unterschiedlich erfasst werden:

- Konversionen auf Variantenebene werden gezählt, sobald Nutzer:innen die Variante betreten.
- Konversionen auf Schrittebene werden erst gezählt, nachdem die Nachricht des Schritts an die Nutzer:innen gesendet wurde.

Das bedeutet, dass alle Nutzer:innen, die den Canvas betreten und das Konversions-Event ausführen, bevor sie einen Schritt erhalten, zur Variantensumme zählen, aber nicht zu einem einzelnen Schritt.

Die folgenden Szenarien können ebenfalls zu dieser Abweichung führen:

- **Nutzer:innen verlassen den Canvas, bevor sie einen Schritt erhalten.** Wenn Nutzer:innen den Canvas betreten, ihn aber verlassen (z. B. aufgrund eines Filters oder einer Zielgruppen-Diskrepanz), bevor eine Nachricht gesendet wird, zählt eine von ihnen durchgeführte Konversion trotzdem auf Variantenebene, aber nicht auf Schrittebene.
- **Ein Schritt richtet sich nur an eine Teilmenge der Nutzer:innen.** Wenn ein Schritt so konfiguriert ist, dass er nur an eine bestimmte Plattform gesendet wird (z. B. Mobilgeräte), können Nutzer:innen auf anderen Plattformen (z. B. Internet) dennoch den Canvas betreten und konvertieren. Da diese Nutzer:innen die Schrittnachricht nie erhalten, wird die Konversion nicht auf Schrittebene gezählt – sondern nur auf Variantenebene.

Weitere Informationen zu Canvas-Analytics finden Sie unter [Messen und Testen mit Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).