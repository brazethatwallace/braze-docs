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

Für eine personalisierte Feiertagskampagne, die auf aktive Nutzer:innen abzielt, kann ein Konversions-Event wie **Sitzung starten** innerhalb von zwei oder drei Tagen angemessen sein, da Sie so ein Gefühl für das Nutzer-Engagement nach Erhalt Ihrer Nachricht bekommen. Sie können auch zusätzliche Events wie **Bestellung aufgeben**, **App-Upgrade** oder beliebige angepasste Events als Konversions-Events auswählen.

### Wann beginnt das Konversions-Tracking? {#when-does-conversion-tracking-begin}

{% tabs %}
{% tab Campaign %}

Das Konversions-Tracking beginnt, wenn eine Nutzer:in die Campaign erhält oder in die Kontrollgruppe der Campaign aufgenommen wird. Der Empfang einer Nachricht und die Zuweisung zu einer Variante erfolgen in der Regel gleichzeitig. Bei In-App-Nachricht-Campaigns beginnt das Konversions-Tracking, wenn Braze eine Impression erfasst.

{% endtab %}
{% tab Canvas %}

Das Konversions-Tracking beginnt, wenn eine Nutzer:in den Canvas betritt. Bei Canvas-Schritten werden Konversionen zugeordnet, solange die Nutzer:in in diesem Schritt aktiv ist. Wenn die Nutzer:in zum nächsten Schritt übergeht, stoppt das Konversions-Tracking für den vorherigen Schritt und beginnt für den nächsten Schritt.

Während sich eine Nutzer:in in einem Verzögerungsschritt oder einem anderen Schritt ohne Nachricht befindet, werden Konversionen, die während dieser Wartezeit auftreten, weiterhin dem zuletzt erhaltenen Nachrichtenschritt zugeordnet, bis die Nutzer:in einen weiteren Nachrichtenschritt erhält. Nachdem die Nutzer:in den letzten Nachrichtenschritt in ihrem Pfad erhalten hat, können Konversionen weiterhin bis zum Ablauf der Konversionsfrist (gerechnet ab dem Canvas-Entry) erfasst werden, auch wenn keine weiteren Nachrichtenschritte folgen.

{% endtab %}
{% endtabs %}

{% alert tip %}
Weitere Informationen zu Konversionen finden Sie in unserem [Braze-Lernkurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Campaign-Einrichtung.
{% endalert %}

### Regeln für das Konversions-Tracking {#conversion-tracking-rules}

Konversions-Events ordnen Nutzeraktionen einem Engagement-Punkt zu. Generell konvertiert eine Nutzer:in bei geöffnetem Konversionsfenster höchstens einmal pro Konversions-Event für diese Campaign oder diesen Canvas. Wenn sie dieselbe Konversionsaktion vor Ablauf der Frist mehrfach ausführt (z. B. zwei Käufe), zählt Braze dennoch nur eine Konversion für dieses Event. Multichannel-Campaigns können für jeden Messaging-Kanal eine separate Konversions-Opportunity erfassen, wodurch Konversionsraten von über 100 % entstehen können, wenn Sie die Konversionsanzahl mit den eindeutigen Empfänger:innen vergleichen (wie in den folgenden Punkten beschrieben).

Beachten Sie Folgendes zum Umgang von Braze mit mehreren Konversionen:

- **Einzelkanal-Campaigns:** Konversionen erfolgen auf Nutzer:innenbasis, nicht auf Gerätebasis. Innerhalb eines einzelnen Kanals konvertiert eine Nutzer:in nur einmal pro Konversions-Event, selbst wenn eine Nachricht an mehrere Geräte gesendet wird. Wenn beispielsweise für eine Campaign nur ein Konversions-Event „Beliebigen Kauf tätigen“ festgelegt ist und eine Nutzer:in innerhalb der Konversionsfrist zwei separate Käufe tätigt, zählt Braze nur eine Konversion. Wenn jedoch [Wiederberechtigung]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility) aktiviert ist, können Nutzer:innen, die die Campaign mehrfach erhalten, mit jedem Versand erneut konvertieren. Bei Campaigns mit Wiederberechtigung gilt der Konversionsmechanismus einmal pro Nutzer:in pro Campaign-Versand, was zu höheren Konversionsanzahlen führen kann, wenn Nutzer:innen dieselbe Campaign mehrmals erhalten und daraus konvertieren.
- **Multichannel-Campaigns:** Bei Multichannel-Campaigns hat jeder Kanal seine eigene Konversions-Opportunity. Eine Nutzer:in kann einmal pro Kanal konvertieren, nachdem sie eine Nachricht auf diesem Kanal erhalten hat. Wenn also eine Nutzer:in Nachrichten auf mehreren Kanälen erhält (z. B. sowohl E-Mail als auch Push) und die Konversionsaktion ausführt, zählt Braze eine Konversion für jeden Kanal, was zu Konversionsraten von über 100 % führen kann.
- **Canvas-Nachrichtenschritte:** Braze ordnet Konversionen, die innerhalb der Konversionsfrist auftreten, dem letzten Canvas-Nachrichtenschritt zu, den die Nutzer:in erhalten hat. Nachdem sie den nächsten Nachrichtenschritt erhält, wird die Zuordnung auf diesen Schritt übertragen. Braze misst dieses Fenster ab dem Zeitpunkt, an dem die Nutzer:in den Canvas betritt, nicht ab jeder einzelnen Nachricht. Konversionen, die während Verzögerungen zwischen Nachrichtenschritten auftreten, zählen zur Zuordnung des vorherigen Nachrichtenschritts, bis die Nutzer:in weitergeht; Konversionen nach dem letzten Nachrichtenschritt zählen weiterhin bis zum Ablauf der Canvas-Konversionsfrist.
- **Aufbewahrung historischer Events:** Das Konversions-Tracking in Campaign- und Canvas-Dashboards misst historische Aktionen, nicht aktuelle Nutzerprofile. Wenn eine Nutzer:in eine Konversionsregel innerhalb des festgelegten Fensters erfüllt, erfasst Braze eine Konversion in der Analyse und entfernt sie nicht, selbst wenn das Profil dieser Nutzer:in später gelöscht, zusammengeführt oder im Rahmen routinemäßiger Datenpflege oder DSGVO-Compliance-Maßnahmen archiviert wird. Live-Segment-Zähler können naturgemäß niedriger sein als Ihre permanenten Dashboard-Event-Protokolle, da dynamische Segmente nur aktive Profile filtern, die aktuell in der Datenbank vorhanden sind.
- Wenn eine Nutzer:in ein Konversions-Event innerhalb der Konversionsfristen von zwei separaten Campaigns oder Canvases ausführt, die sie erhalten hat, wird die Konversion bei beiden registriert.
- Eine Nutzer:in gilt als konvertiert, wenn sie das spezifische Konversions-Event innerhalb des Fensters ausgeführt hat, auch wenn sie die Nachricht nicht geöffnet oder angeklickt hat.

### Primäres Konversions-Event {#primary-conversion-event}

Das primäre Konversions-Event ist das erste Event, das Sie bei der Erstellung einer Campaign oder eines Canvas hinzufügen. Dieses Event hat den größten Einfluss auf Ihr Engagement und Ihre Berichte. Braze verwendet Ihr primäres Konversions-Event, um:

- Die leistungsstärkste Nachrichtenvariante in [multivariaten Campaigns]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) oder Canvases auszuwählen.
- Das Fenster zu bestimmen, in dem der Umsatz für die Campaign oder den Canvas berechnet wird.
- Nachrichtenverteilungen für Campaigns und Canvases mithilfe von [Optimierung mit BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) anzupassen.

Die Anzahl der primären Konversions-Events ist die Anzahl der aufgetretenen Konversions-Events. Bei Multichannel-Campaigns zählt Braze Konversionen pro Kanal (wie unter [Regeln für das Konversions-Tracking](#conversion-tracking-rules) beschrieben), was bedeutet, dass die Konversionsanzahl die Anzahl der eindeutigen Nutzer:innen übersteigen und Konversionsraten von über 100 % ergeben kann. Braze berechnet die primäre Konversionsrate, indem diese Anzahl durch die Anzahl der eindeutigen Empfänger:innen geteilt wird. Braze betrachtet eine Nutzer:in als Empfänger:in, wenn die Nachricht gesendet oder angezeigt wird, je nach Kanal. Bei Push oder E-Mail wird eine Nutzer:in zur Empfänger:in, nachdem Braze die Nachricht gesendet hat. Bei In-App-Nachrichten oder Content Cards muss die Nutzer:in die Nachricht gesehen haben, um als Empfänger:in zu gelten.

{% alert note %}
Wenn Sie Nachrichten mithilfe des Liquid-`abort`-Tags abbrechen, bricht Braze Nachrichten nur für Nutzer:innen ab, die Varianten durchlaufen. Nachrichten an Nutzer:innen in der Kontrollgruppe werden nicht abgebrochen, was zu verzerrten Konversionsprozentsätzen zwischen Varianten und Kontrollgruppen führen kann. Als Workaround können Sie die [Segmentierung]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) verwenden, um Ihre Nutzer:innen beim Campaign- und Canvas-Entry gezielt anzusprechen.
{% endalert %}

## Eine Campaign mit Konversions-Tracking erstellen {#creating-a-campaign-with-conversion-tracking}

### Schritt 1: Campaign einrichten {#step-1-set-up-your-campaign}

[Erstellen Sie eine Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign) für den gewünschten Messaging-Kanal. Nachdem Sie die Nachrichten und den Zeitplan Ihrer Campaign eingerichtet haben, können Sie bis zu vier Konversions-Events für das Tracking hinzufügen.

Verwenden Sie so viele Konversions-Events wie nötig. Das Hinzufügen eines zweiten oder dritten Konversions-Events bereichert Ihr Reporting erheblich. Wenn Sie beispielsweise eine Campaign erstellen, die sich an passive Nutzer:innen richtet, können Sie neben dem primären Konversions-Event **Starts Session** ein sekundäres Konversions-Event hinzufügen, um besser zu verstehen, wie effektiv Ihre Campaign dabei ist, Nutzer:innen zurück in Ihre App zu bringen.

### Schritt 2: Konversions-Events hinzufügen {#step-2-add-the-conversion-events}

Wählen Sie zunächst den allgemeinen Event-Typ aus, den Sie verwenden möchten:

| Konversions-Event-Typ   | Beschreibung               |
|-------------------------|----------------------------|
| **Starts Session**      | Nutzer:innen werden als konvertiert gezählt, wenn sie eine der von Ihnen angegebenen Apps öffnen (standardmäßig alle Apps im Workspace).|
| **Makes Purchase**      | Nutzer:innen werden als konvertiert gezählt, wenn sie ein [Kauf-Event]({{site.baseurl}}/api/objects_filters/purchase_object) erfassen. Standardmäßig wird jeder Kauf erfasst, oder Sie können ein bestimmtes Produkt angeben.|
| **Places Order**        | Nutzer:innen werden als konvertiert gezählt, wenn sie das [empfohlene E-Commerce-Event „Order Placed“]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events#ecommerce-recommended-events?tab=ecommerce.order_placed) auslösen. Standardmäßig wird jede Bestellung erfasst, oder Sie können nach einem bestimmten Produkt filtern.<br><br>Das Event „Places Order“ befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze Account Manager:in, wenn Sie an diesem Early Access teilnehmen möchten. |
| **Performs Custom Event**| Nutzer:innen werden als konvertiert gezählt, wenn sie eines Ihrer bestehenden angepassten Events ausführen (kein Standard, Sie müssen das Event angeben).|
| **Upgrade App**         | Nutzer:innen werden als konvertiert gezählt, wenn sie die App-Version einer der von Ihnen angegebenen Apps aktualisieren (standardmäßig alle Apps im Workspace). Braze führt einen numerischen Vergleich nach dem Best-Effort-Prinzip durch, um festzustellen, ob die Änderung ein Upgrade war. Nicht-numerische Versionen werden als Konversionen gezählt, wenn sich die Version ändert.|
| **Opens email**         | Nutzer:innen werden als konvertiert gezählt, wenn sie die E-Mail öffnen (nur für E-Mail-Campaigns).|
| **Clicks email**        | Nutzer:innen werden als konvertiert gezählt, wenn sie auf einen Link in der E-Mail klicken (nur für E-Mail-Campaigns).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Konversions-Events hinzufügen" }

{% alert important %}
**Verschachtelte Eigenschaften werden in Konversions-Events nicht unterstützt**. Sie können verschachtelte Eigenschaften nicht in Konversions-Events verwenden. Wenn beispielsweise `product_code` oder `product_name` verschachtelte Eigenschaften innerhalb eines `products`-Arrays sind (wie `products[].product_code`), können Sie sie nicht verwenden, um in einem Konversions-Event zu prüfen, ob ein bestimmter Produktkauf getätigt wurde.
{% endalert %}

Legen Sie Ihre Konversionsfrist fest. Dies ist die maximale Zeitspanne, die vergehen darf, bevor Braze eine Konversion berücksichtigt. Sie können ein Zeitfenster von bis zu 30 Tagen festlegen, in dem Braze die Konversion zählt, wenn die Nutzer:innen die angegebene Aktion ausführen.

![Der Konversions-Event-Typ „Makes Purchase“ als Beispiel zur Erfassung von Konversionen für Nutzer:innen, die einen beliebigen Kauf tätigen. Dieses Event hat eine Konversionsfrist von 12 Stunden.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Nachdem Sie Ihre Konversions-Events ausgewählt haben, setzen Sie den Erstellungsprozess der Campaign fort und beginnen Sie mit dem Versand Ihrer Campaign.

### Schritt 3: Ergebnisse anzeigen {#step-3-view-your-results}

Navigieren Sie zur Seite **Details**, um die Details zu jedem Konversions-Event anzuzeigen, das mit der von Ihnen erstellten Campaign verknüpft ist. Unabhängig von den ausgewählten Konversions-Events können Sie auch den Gesamtumsatz sehen, der dieser spezifischen Campaign sowie bestimmten Varianten während des Zeitfensters des primären Konversions-Events zugeordnet wird.

{% alert note %}
Wenn Sie während der Campaign-Erstellung keine Konversions-Events auswählen, beträgt der Standardzeitraum drei Tage.
{% endalert %}

Darüber hinaus können Sie bei multivariaten Nachrichten die Anzahl der Konversionen und die Konversionsraten für Ihre Kontrollgruppe und jede Variante einsehen.

![Vier Konversions-Events, die Konversionen erfassen basierend darauf, wann ein Kauf innerhalb von drei Stunden getätigt wurde, ein Kauf innerhalb von zwei Stunden getätigt wurde, eine Sitzung innerhalb von 30 Minuten gestartet wurde und eine Sitzung innerhalb von 25 Minuten gestartet wurde.]({% image_buster /assets/img_archive/conversion_event_details.png %})

## Konversionsraten auf Canvas-Schritt- versus Varianten-Ebene {#canvas-step-versus-variant-conversion-rates}

Es kommt häufig vor, dass die Gesamtzahl der Konversionen einer Canvas-Variante höher ist als die Summe der Konversionen ihrer einzelnen Schritte. Dies liegt daran, dass Konversionen auf Varianten-Ebene und auf Schritt-Ebene unterschiedlich erfasst werden:

- Varianten-Konversionen werden gezählt, sobald die Nutzer:innen die Variante betreten.
- Schritt-Konversionen werden erst gezählt, nachdem die Nachricht des Schritts an die Nutzer:innen gesendet wurde.

Das bedeutet, dass alle Nutzer:innen, die den Canvas betreten und das Konversions-Event ausführen, bevor sie einen Schritt erhalten, zur Varianten-Gesamtzahl zählen, aber nicht zu einem einzelnen Schritt.

Die folgenden Szenarien können ebenfalls zu dieser Abweichung führen:

- **Nutzer:innen verlassen den Canvas, bevor sie einen Schritt erhalten.** Wenn Nutzer:innen den Canvas betreten, ihn aber verlassen (z. B. aufgrund eines Filters oder einer Zielgruppen-Nichtübereinstimmung), bevor eine Nachricht gesendet wird, zählt eine von ihnen durchgeführte Konversion dennoch auf Varianten-Ebene, aber nicht auf Schritt-Ebene.
- **Ein Schritt richtet sich nur an eine Teilmenge der Nutzer:innen.** Wenn ein Schritt so konfiguriert ist, dass er nur an eine bestimmte Plattform gesendet wird (z. B. Mobilgeräte), können Nutzer:innen auf anderen Plattformen (z. B. Internet) dennoch den Canvas betreten und konvertieren. Da diese Nutzer:innen die Schritt-Nachricht nie erhalten, wird die Konversion nicht auf Schritt-Ebene gezählt – sondern nur auf Varianten-Ebene.

Weitere Informationen zu Canvas-Analytics finden Sie unter [Messen und Testen mit Canvas-Analytics]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).