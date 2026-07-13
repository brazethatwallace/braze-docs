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

Für eine personalisierte Feiertagskampagne, die sich an aktive Nutzer:innen richtet, kann ein Konversions-Event **Sitzung starten** innerhalb von zwei oder drei Tagen angemessen sein, da es Ihnen ermöglicht, ein Gefühl für das Nutzer:innen-Engagement nach Erhalt Ihrer Nachricht zu bekommen. Sie können auch zusätzliche Events wie **Bestellung aufgeben**, **App upgraden** oder eines Ihrer angepassten Events als Konversions-Events auswählen.

### Wann beginnt das Conversion-Tracking? {#when-does-conversion-tracking-begin}

{% tabs %}
{% tab Campaign %}

Das Conversion-Tracking beginnt, wenn ein:e Nutzer:in die Campaign erhält oder der Kontrollgruppe der Campaign zugewiesen wird. Der Empfang einer Nachricht und die Zuweisung zu einer Variante erfolgen in der Regel gleichzeitig. Bei In-App-Nachricht-Campaigns beginnt das Conversion-Tracking, wenn Braze eine Impression erfasst.

{% endtab %}
{% tab Canvas %}

Das Conversion-Tracking beginnt, wenn ein:e Nutzer:in den Canvas betritt. Bei Canvas-Schritten werden Conversions zugeordnet, solange der/die Nutzer:in in diesem Schritt aktiv ist. Wenn der/die Nutzer:in zu einem anderen Schritt übergeht, stoppt das Conversion-Tracking für den vorherigen Schritt und beginnt für den nächsten Schritt.

Während sich ein:e Nutzer:in in einem Verzögerungs-Schritt oder einem anderen Nicht-Nachrichten-Schritt befindet, werden Conversions, die während dieser Wartezeit auftreten, weiterhin dem letzten Nachrichtenschritt zugeordnet, bis der/die Nutzer:in einen weiteren Nachrichtenschritt erhält. Nachdem der/die Nutzer:in den letzten Nachrichtenschritt in seinem/ihrem Pfad erhalten hat, können Conversions weiterhin bis zur Canvas-Konversionsfrist (ab Canvas-Eintritt gezählt) erfasst werden, auch wenn keine weiteren Nachrichtenschritte folgen.

{% endtab %}
{% endtabs %}

{% alert tip %}
Weitere Informationen zu Conversions finden Sie in unserem [Braze-Lernkurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Campaign-Einrichtung.
{% endalert %}

### Regeln für das Conversion-Tracking {#conversion-tracking-rules}

Konversions-Events ordnen Nutzer:innen-Aktionen einem Engagement-Punkt zu. Im Allgemeinen konvertiert ein:e Nutzer:in, solange ein Konversionsfenster offen ist, höchstens einmal pro Konversions-Event für diese Campaign oder diesen Canvas. Wenn er/sie dieselbe Konversions-Aktion vor Ablauf der Frist mehr als einmal ausführt (z. B. zwei Käufe), zählt Braze dennoch nur eine Conversion für dieses Event. Mehrkanal-Campaigns können eine separate Konversions-Möglichkeit für jeden Messaging-Kanal erfassen, was Konversionsraten über 100 % ergeben kann, wenn Sie die Conversion-Anzahl mit den eindeutigen Empfänger:innen vergleichen (wie in den folgenden Punkten beschrieben).

Beachten Sie Folgendes dazu, wie Braze mit mehreren Conversions umgeht:

- **Einzelkanal-Campaigns:** Conversions erfolgen pro Nutzer:in, nicht pro Gerät. Innerhalb eines einzelnen Kanals konvertiert ein:e Nutzer:in nur einmal pro Konversions-Event, selbst wenn eine Nachricht an mehrere Geräte gesendet wird. Wenn eine Campaign beispielsweise nur ein Konversions-Event hat, das auf „Tätigt einen Kauf“ eingestellt ist, und ein:e Nutzer:in zwei separate Käufe innerhalb der Konversionsfrist tätigt, zählt Braze nur eine Conversion.
- **Mehrkanal-Campaigns:** Bei Mehrkanal-Campaigns hat jeder Kanal seine eigene Konversions-Möglichkeit. Ein:e Nutzer:in kann einmal pro Kanal konvertieren, nachdem er/sie eine Nachricht auf diesem Kanal erhalten hat. Das bedeutet: Wenn ein:e Nutzer:in Nachrichten auf mehreren Kanälen erhält (z. B. sowohl E-Mail als auch Push) und die Konversions-Aktion ausführt, zählt Braze eine Conversion für jeden Kanal, was dazu führen kann, dass die Konversionsraten 100 % übersteigen.
- **Canvas-Nachrichtenschritte:** Braze ordnet Conversions, die innerhalb der Konversionsfrist auftreten, dem letzten Canvas-Nachrichtenschritt zu, den der/die Nutzer:in erhalten hat. Nachdem er/sie den nächsten Nachrichtenschritt erhalten hat, wird die Zuordnung auf diesen Schritt verschoben. Braze misst dieses Zeitfenster ab dem Zeitpunkt, an dem der/die Nutzer:in den Canvas betritt, nicht ab jeder einzelnen Nachricht. Conversions, die während Verzögerungen zwischen Nachrichtenschritten auftreten, werden der Zuordnung des vorherigen Nachrichtenschritts zugerechnet, bis der/die Nutzer:in weitergeht; Conversions nach dem letzten Nachrichtenschritt zählen weiterhin bis zur Canvas-Konversionsfrist.
- **Aufbewahrung historischer Events:** Das Conversion-Tracking in Campaign- und Canvas-Dashboards misst historische Aktionen, nicht aktuelle Nutzerprofile. Wenn ein:e Nutzer:in eine Konversionsregel innerhalb des festgelegten Zeitfensters erfüllt, erfasst Braze eine Conversion in den Analytics und entfernt sie nicht, selbst wenn das Profil dieser:dieses Nutzer:in später gelöscht, zusammengeführt oder im Rahmen routinemäßiger Datenpflege oder DSGVO-Compliance-Maßnahmen archiviert wird. Live-Segment-Zählungen können naturgemäß niedriger sein als Ihre permanenten Dashboard-Event-Protokolle, da dynamische Segmente nur aktive Profile filtern, die aktuell in der Datenbank vorhanden sind.
- Wenn ein:e Nutzer:in ein Konversions-Event innerhalb der Konversionsfristen von zwei separaten Campaigns oder Canvases ausführt, die er/sie erhalten hat, wird die Conversion bei beiden registriert.
- Ein:e Nutzer:in gilt als konvertiert, wenn er/sie das spezifische Konversions-Event innerhalb des Zeitfensters ausgeführt hat, auch wenn er/sie die Nachricht nicht geöffnet oder angeklickt hat.

### Primäres Konversions-Event {#primary-conversion-event}

Das primäre Konversions-Event ist das erste Event, das Sie während der Erstellung einer Campaign oder eines Canvas hinzufügen. Dieses Event hat den größten Einfluss auf Ihr Engagement und Ihre Berichterstattung. Braze verwendet Ihr primäres Konversions-Event, um:

- Die Gewinnervariante in [multivariaten]({{site.baseurl}}/user_guide/messaging/ab_testing#multivariate-and-ab-testing) Campaigns oder Canvases zu berechnen.
- Das Zeitfenster zu bestimmen, in dem der Umsatz für die Campaign oder den Canvas berechnet wird.
- Die Nachrichtenverteilung für Campaigns und Canvases mithilfe der [intelligenten Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection) anzupassen.

Die Anzahl der primären Konversions-Events ist die Anzahl der aufgetretenen Konversions-Events. Bei Mehrkanal-Campaigns zählt Braze Conversions pro Kanal (wie in den [Regeln für das Conversion-Tracking](#conversion-tracking-rules) beschrieben), was bedeutet, dass die Conversion-Anzahl die Anzahl der eindeutigen Nutzer:innen übersteigen kann und Konversionsraten von über 100 % ergeben kann. Braze berechnet die primäre Konversionsrate, indem diese Anzahl durch die Anzahl der eindeutigen Empfänger:innen geteilt wird. Braze betrachtet eine:n Nutzer:in als Empfänger:in, wenn die Nachricht gesendet oder angezeigt wird, je nach Kanal. Beispielsweise wird bei Push oder E-Mail ein:e Nutzer:in zum/zur Empfänger:in, nachdem Braze die Nachricht gesendet hat. Bei In-App-Nachrichten oder Content Cards muss der/die Nutzer:in die Nachricht angesehen haben, um als Empfänger:in zu gelten.

{% alert note %}
Wenn Sie Nachrichten mit dem Liquid-Tag `abort` abbrechen, bricht Braze Nachrichten nur für Nutzer:innen ab, die Varianten durchlaufen. Nachrichten an Nutzer:innen in der Kontrollgruppe werden nicht abgebrochen, was zu verzerrten Konversionsprozentsätzen zwischen Varianten und Kontrollgruppen führen kann. Als Workaround verwenden Sie die [Segmentierung]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment), um Ihre Nutzer:innen beim Eintritt in die Campaign oder den Canvas zu targeten.
{% endalert %}

## Eine Campaign mit Conversion-Tracking erstellen {#creating-a-campaign-with-conversion-tracking}

### Schritt 1: Campaign einrichten {#step-1-set-up-your-campaign}

[Erstellen Sie eine Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign) für Ihren gewünschten Messaging-Kanal. Nachdem Sie die Nachrichten und den Zeitplan Ihrer Campaign eingerichtet haben, können Sie bis zu vier Konversions-Events für das Tracking hinzufügen.

Verwenden Sie so viele Konversions-Events wie nötig. Das Hinzufügen eines zweiten oder dritten Konversions-Events bereichert Ihre Berichterstattung erheblich. Wenn Sie beispielsweise eine Campaign haben, die sich an passive Nutzer:innen richtet, kann das Hinzufügen eines sekundären Konversions-Events zusammen mit dem primären Konversions-Event **Sitzung starten** Ihnen helfen zu verstehen, wie effektiv Ihre Campaign darin ist, Nutzer:innen zurück in Ihre Anwendung zu bringen.

### Schritt 2: Konversions-Events hinzufügen {#step-2-add-the-conversion-events}

Wählen Sie zunächst den allgemeinen Event-Typ aus, den Sie verwenden möchten:

| Konversions-Event-Typ | Beschreibung |
|-------------------------|----------------------------|
| **Sitzung starten** | Ein:e Nutzer:in gilt als konvertiert, wenn er/sie eine der von Ihnen angegebenen Apps öffnet (standardmäßig alle Apps im Workspace). |
| **Kauf tätigen** | Ein:e Nutzer:in gilt als konvertiert, wenn er/sie ein [Kauf-Event]({{site.baseurl}}/api/objects_filters/purchase_object) aufzeichnet. Dies erfasst standardmäßig jeden Kauf, oder Sie können ein bestimmtes Produkt angeben. |
| **Bestellung aufgeben** | Ein:e Nutzer:in gilt als konvertiert, wenn er/sie das [empfohlene E-Commerce-Event „Bestellung aufgegeben“]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#ecommerce-recommended-events?tab=ecommerce.order_placed) auslöst. Dies erfasst standardmäßig jede Bestellung, oder Sie können nach einem bestimmten Produkt filtern.<br><br>Das Event „Bestellung aufgeben“ befindet sich derzeit im Early Access. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Teilnahme an diesem Early Access interessiert sind. |
| **Angepasstes Event ausführen** | Ein:e Nutzer:in gilt als konvertiert, wenn er/sie eines Ihrer vorhandenen angepassten Events ausführt (kein Standard, Sie müssen das Event angeben). |
| **App upgraden** | Ein:e Nutzer:in gilt als konvertiert, wenn er/sie die App-Version einer der von Ihnen angegebenen Apps aktualisiert (standardmäßig alle Apps im Workspace). Braze führt einen Best-Effort-Zahlenvergleich durch, um festzustellen, ob die Änderung ein Upgrade war. Nicht-numerische Versionen werden als Conversions gezählt, wenn sich die Version ändert. |
| **E-Mail öffnen** | Ein:e Nutzer:in gilt als konvertiert, wenn er/sie die E-Mail öffnet (nur für E-Mail-Campaigns). |
| **E-Mail-Link klicken** | Ein:e Nutzer:in gilt als konvertiert, wenn er/sie auf einen Link in der E-Mail klickt (nur für E-Mail-Campaigns). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Konversions-Events hinzufügen" }

{% alert important %}
**Verschachtelte Eigenschaften werden in Konversions-Events nicht unterstützt**. Sie können keine verschachtelten Eigenschaften in Konversions-Events verwenden. Wenn beispielsweise `product_code` oder `product_name` verschachtelte Eigenschaften innerhalb eines `products`-Arrays sind (wie `products[].product_code`), können Sie diese nicht verwenden, um zu prüfen, ob ein bestimmter Produktkauf in einem Konversions-Event getätigt wurde.
{% endalert %}

Legen Sie Ihre Konversionsfrist fest. Dies ist die maximale Zeitspanne, die vergehen kann, bevor Braze eine Conversion berücksichtigt. Sie können ein Zeitfenster von bis zu 30 Tagen festlegen, in dem Braze die Conversion zählt, wenn der/die Nutzer:in die angegebene Aktion ausführt.

![Der Konversions-Event-Typ „Kauf tätigen“ als Beispiel zur Erfassung von Conversions für Nutzer:innen, die einen beliebigen Kauf tätigen. Dies hat eine Konversionsfrist von 12 Stunden.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Nachdem Sie Ihre Konversions-Events ausgewählt haben, fahren Sie mit dem Campaign-Erstellungsprozess fort und beginnen Sie mit dem Versand Ihrer Campaign.

### Schritt 3: Ergebnisse anzeigen {#step-3-view-your-results}

Gehen Sie zur Seite **Details**, um die Details für jedes Konversions-Event anzuzeigen, das mit der von Ihnen erstellten Campaign verknüpft ist. Unabhängig von Ihren ausgewählten Konversions-Events können Sie auch den Gesamtumsatz sehen, der dieser spezifischen Campaign sowie bestimmten Varianten während des Zeitfensters des primären Konversions-Events zugeordnet wird.

{% alert note %}
Wenn Sie während der Campaign-Erstellung keine Konversions-Events auswählen, beträgt die Standardzeit drei Tage.
{% endalert %}

Zusätzlich können Sie bei multivariaten Nachrichten die Anzahl der Conversions und die Konversionsprozentsätze für Ihre Kontrollgruppe und jede Variante sehen.

![Vier Konversions-Events, die Conversions erfassen, basierend darauf, wann ein Kauf innerhalb von drei Stunden getätigt wurde, ein Kauf innerhalb von zwei Stunden getätigt wurde, eine Sitzung innerhalb von 30 Minuten gestartet wurde und eine Sitzung innerhalb von 25 Minuten gestartet wurde.]({% image_buster /assets/img_archive/conversion_event_details.png %})

## Konversionsraten auf Canvas-Schritt- vs. Varianten-Ebene {#canvas-step-versus-variant-conversion-rates}

Es kommt häufig vor, dass die Gesamt-Conversion-Anzahl einer Canvas-Variante höher ist als die Summe der Conversion-Anzahlen ihrer einzelnen Schritte. Das liegt daran, dass Conversions auf Varianten-Ebene und auf Schritt-Ebene unterschiedlich erfasst werden:

- Varianten-Conversions werden gezählt, sobald der/die Nutzer:in die Variante betritt.
- Schritt-Conversions werden erst gezählt, nachdem die Nachricht des Schritts an den/die Nutzer:in gesendet wurde.

Das bedeutet, dass jede:r Nutzer:in, der/die den Canvas betritt und das Konversions-Event ausführt, bevor er/sie einen Schritt erhält, zur Varianten-Gesamtzahl zählt, aber nicht zu einem einzelnen Schritt.

Die folgenden Szenarien können ebenfalls zu dieser Diskrepanz führen:

- **Nutzer:in verlässt den Canvas, bevor ein Schritt empfangen wird.** Wenn ein:e Nutzer:in den Canvas betritt, ihn aber verlässt (z. B. aufgrund eines Filters oder einer Zielgruppen-Nichtübereinstimmung), bevor eine Nachricht gesendet wird, zählt eine von ihm/ihr ausgeführte Conversion weiterhin auf Varianten-Ebene, aber nicht auf Schritt-Ebene.
- **Schritt richtet sich an eine Teilmenge der Nutzer:innen.** Wenn ein Schritt so konfiguriert ist, dass er nur an eine bestimmte Plattform gesendet wird (z. B. Mobilgerät), können Nutzer:innen auf anderen Plattformen (z. B. Internet) dennoch den Canvas betreten und konvertieren. Da diese Nutzer:innen die Schritt-Nachricht nie erhalten, zählt die Conversion nicht auf Schritt-Ebene – nur auf Varianten-Ebene.

Weitere Informationen zu Canvas-Analytics finden Sie unter [Messen und Testen mit Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).