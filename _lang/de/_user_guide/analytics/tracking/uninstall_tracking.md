---
nav_title: Uninstall-Tracking
article_title: Uninstall-Tracking
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt die Implementierung von Uninstall-Tracking für Statistiken auf Kampagnen- und App-Ebene."
tool: Reports

---

# Uninstall-Tracking {#uninstall-tracking}

> Dieser Artikel zeigt Ihnen, wie Sie die Gesamtheit der App-Deinstallationen im Laufe der Zeit betrachten können, um Trends und Anomalien zu erkennen, und wie Sie Deinstallationen auf Kampagnenebene verfolgen können, um festzustellen, ob eine bestimmte Campaign App-Installationen fördert oder verhindert.

Uninstall-Tracking in Braze liefert die folgenden Details:

1. Tägliche Deinstallationsstatistiken auf App-Ebene in einem Zeitreihendiagramm auf der **Home**-Seite.
2. Deinstallationsstatistiken auf Kampagnenebene in einem Zeitreihendiagramm auf der Seite **Campaign Details** für eine bestimmte Campaign. Diese Statistik gibt die Anzahl der Kampagnenempfänger:innen an, die jeden Tag deinstallieren.

{% alert note %}
Sie müssen das Uninstall-Tracking in Ihrem Braze-Dashboard aktivieren. Dieses Feature ist für Apps auf iOS, Android und Fire OS verfügbar.
{% endalert %}

## Funktionsweise {#how-it-works}

Braze sammelt automatisch grundlegende Deinstallationsinformationen aus Ihren regulären Push-Campaigns. Da die Häufigkeit, mit der verschiedene Nutzer:innen Push-Campaigns erhalten, jedoch variieren kann, bieten wir Uninstall-Tracking an, um eine genauere Momentaufnahme der Deinstallationsaktivitäten Ihrer Nutzer:innen zu erhalten.

Wenn Braze eine Deinstallation erkennt, wird der oder die Nutzer:in als deinstalliert markiert. Wenn Sie den Filter **Has Not Uninstalled** in einer Campaign verwenden, werden diese markierten Nutzer:innen ausgeschlossen. Wenn ein:e Nutzer:in die App erneut installiert, sie aber nicht öffnet, bleibt die Deinstallationsmarkierung im Profil bestehen. Die Markierung wird erst entfernt, wenn der oder die Nutzer:in eine neue Sitzung in der neu installierten App startet. Das bedeutet, dass ein:e Nutzer:in, der oder die die App erneut installiert, aber nie öffnet, weiterhin als deinstalliert angezeigt wird.

Weitere Informationen zur Verwendung des Uninstall-Trackings finden Sie in unserem Blogbeitrag [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Uninstall-Tracking aktivieren {#turning-on-uninstall-tracking}

Sie können das Uninstall-Tracking auf der Seite **App Settings** unter **Settings** für jede App aktivieren, die Sie verfolgen möchten.

Wenn Sie das Uninstall-Tracking für eine App aktivieren, sendet Braze jede Nacht eine Push-Nachricht im Hintergrund an Nutzer:innen, die innerhalb der letzten 24 Stunden keine Sitzung aufgezeichnet oder keine Push-Nachricht erhalten haben.

### Konfiguration {#configuration}

Um das Uninstall-Tracking für Ihre iOS-Anwendung zu konfigurieren, verwenden Sie eine [Utility-Methode]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift). Verwenden Sie für Ihre Android-Anwendung [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Wenn Braze eine Deinstallation feststellt – sei es durch Uninstall-Tracking oder durch die normale Zustellung von Push-Campaigns – erfassen wir den bestmöglich geschätzten Zeitpunkt der Deinstallation beim Nutzer oder bei der Nutzerin. Dieser Zeitpunkt wird im Nutzerprofil als Standardattribut gespeichert und kann zur Definition eines Segments von Nutzer:innen für Rückgewinnungskampagnen verwendet werden.

## Segmente nach Deinstallationen filtern {#filtering-segments-by-uninstalls}

Der Filter **Uninstalled** wählt Nutzer:innen aus, die Ihre App innerhalb eines bestimmten Zeitraums deinstalliert haben. Da es schwierig ist, den genauen Zeitpunkt einer Deinstallation zu bestimmen, empfehlen wir, bei Deinstallationsfiltern breitere Zeitspannen zu verwenden, um sicherzustellen, dass alle Nutzer:innen, die deinstallieren, irgendwann in das Segment fallen.

Tägliche Statistiken über Deinstallationen finden Sie auf der **Home**-Seite.

![Deinstallations-Segment.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

Das Diagramm kann nach App und Segment aufgeschlüsselt werden, ähnlich wie andere Statistiken, die Braze bereitstellt. Wählen Sie im Abschnitt **Performance overview** Ihren Datumsbereich und, falls gewünscht, eine App aus. Scrollen Sie dann zum Diagramm **Performance Over Time** und gehen Sie wie folgt vor:

1. Wählen Sie in der Dropdown-Liste **Statistics For** die Option **Uninstalls** aus.
2. Wählen Sie in der Dropdown-Liste **Breakdown** die Option **By segment** aus.
3. Wählen Sie in der Dropdown-Liste **Breakdown Values** die Segmente aus, die in das Diagramm aufgenommen werden sollen.

{% alert note %}
Apps ohne aktiviertes Uninstall-Tracking melden Deinstallationen nur von einer Teilmenge ihrer Nutzer:innen (denjenigen, die mit Push-Benachrichtigungen angesprochen wurden), sodass die tägliche Gesamtzahl der Deinstallationen höher sein kann als angezeigt.
{% endalert %}

## Uninstall-Tracking für Campaigns {#uninstall-tracking-for-campaigns}

Das Uninstall-Tracking für Campaigns zeigt die Anzahl der Nutzer:innen, die eine bestimmte Campaign erhalten und anschließend Ihre App innerhalb des ausgewählten Zeitraums deinstalliert haben. Dieses Tool gibt Aufschluss darüber, wie Campaigns unbeabsichtigtes negatives Nutzerverhalten fördern können, und hilft dabei, die Gesamtwirksamkeit von Campaigns zu messen.

Die Deinstallationsstatistiken für Campaigns befinden sich auf der Seite **Campaign Analytics** der jeweiligen Campaign. Bei Multichannel- und multivariaten Campaigns können die Deinstallationen nach Kanal bzw. Variante aufgeschlüsselt werden.

![Deinstallation auf Kampagnenebene.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Funktionsweise

Braze verfolgt Deinstallationen, indem es beobachtet, wann Push-Nachrichten, die an die Geräte der Nutzer:innen gesendet werden, entweder von Firebase Cloud Messaging (FCM) oder vom Apple Push Notification Service (APNs) ein Signal zurückgeben, dass die App nicht mehr installiert ist. Wenn Sie das globale Uninstall-Tracking für eine App aktivieren, sendet Braze täglich eine stille Push-Nachricht an die Nutzer:innen, um festzustellen, ob sie die App deinstalliert haben. Braze sendet diesen „stillen“ Push an alle Nutzer:innen (es sei denn, der oder die Nutzer:in hat stille Pushes in den App-Einstellungen deaktiviert); der Push wird den Nutzer:innen nicht angezeigt. Wenn Braze feststellt, dass ein:e Nutzer:in die App deinstalliert hat, geschieht Folgendes:

* Die Gesamtzahl der Deinstallationen der App wird um eins erhöht.
* Die Deinstallationszahl für jede Campaign, die der oder die Nutzer:in in den letzten 24 Stunden erfolgreich erhalten hat, wird um eins erhöht.
* Wenn ein:e Nutzer:in in einem Zeitraum von 24 Stunden drei Campaigns erhält und dann deinstalliert, erhöhen wir die Anzahl der „Deinstallationen“ für alle drei Campaigns.

FCM und APNs unterliegen Einschränkungen hinsichtlich des Uninstall-Trackings. Braze erhöht die Deinstallationszahl nur, wenn FCM oder APNs uns mitteilen, dass ein:e Nutzer:in die App deinstalliert hat. Diese Drittanbietersysteme können uns jedoch jederzeit über Deinstallationen informieren. Verwenden Sie das Uninstall-Tracking, um allgemeine Trends zu erkennen, anstatt präzise Statistiken zu erwarten.

Braze behandelt die folgenden FCM-Antworten als Token-Entfernungs-Antworten (Deinstallation): `DEVICE_UNREGISTERED`, `BAD_REGISTRATION` und `SENDER_ID_MISMATCH`.

Weitere Informationen zur Verwendung des Uninstall-Trackings finden Sie in unserem Blogbeitrag [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Fehlerbehebung {#troubleshooting}

### Warum sehe ich plötzlich einen Anstieg bei den Deinstallationen? {#why-am-i-suddenly-seeing-a-spike-in-uninstalls}

Wenn die Deinstallationen von Apps sprunghaft ansteigen, kann das daran liegen, dass Firebase Cloud Messaging (FCM) und der Apple Push Notification Service (APNS) alte Token in unterschiedlicher Häufigkeit widerrufen.

{% alert note %}
Aus Datenschutzgründen können die Push-Anbieter von Braze Token in unregelmäßigen Abständen widerrufen, was dazu führen kann, dass die Anzahl der Deinstallationen in einem bestimmten Zeitraum gelegentlich stark ansteigt.<br><br>Um diese Änderungen zu validieren, überwachen Sie das Uninstall-Tracking zusammen mit einer Metrik für Nutzeraktionen, wie beispielsweise der direkten Push-Öffnungsrate. Wenn die Deinstallationen stark zunehmen, die direkten Push-Öffnungen jedoch stabil bleiben, spiegelt der Anstieg wahrscheinlich eher die Aufhebung alter Token durch einen Anbieter wider als das tatsächliche Nutzerverhalten.
{% endalert %}

### Wie kann ich feststellen, ob eine bestimmte Campaign Deinstallationen verursacht hat? {#how-do-i-determine-if-a-specific-campaign-caused-uninstalls}

Überprüfen Sie die Analytics der Campaigns, die ungefähr zum gleichen Zeitpunkt wie der Anstieg der Deinstallationen Nachrichten gesendet haben. Wenn eine bestimmte Nachricht mit einem Anstieg der Deinstallationen korreliert, beeinflusst sie möglicherweise Nutzer:innen zur Deinstallation.

So zeigen Sie Deinstallationen nach Segment an:
1. Gehen Sie zur **Home**-Seite des Dashboards.
2. Wählen Sie im Abschnitt **Performance Over Time** die Option **Uninstalls** für **Statistics For** und **By Segment** für **Breakdown** aus.

Wenn Sie ein Segment haben, das passive Nutzer:innen mit aktiviertem [Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) verfolgt, vergleichen Sie dessen Deinstallationstrend mit dem allgemeinen App-Trend.

### Wie kann ich bestätigen, dass Deinstallationen echt sind? {#how-do-i-confirm-uninstalls-are-genuine}

Überprüfen Sie bei APNs die Nutzerprofile auf den Push-Fehler `BadDeviceToken`. Wenn Sie diesen Fehler gehäuft im gleichen Zeitraum wie den Anstieg der Deinstallationen sehen, sind die Deinstallationen wahrscheinlich echt. `BadDeviceToken` zeigt an, dass das Push-Token des Geräts nicht mehr gültig ist, was typischerweise passiert, wenn die App deinstalliert wird.

### Warum unterscheidet sich die Anzahl der App-Deinstallationen von den Angaben in den APNs? {#why-are-the-number-of-app-uninstalls-different-from-whats-in-apns}

Der Unterschied ist zu erwarten.

Apple verwendet einen zufälligen Zeitplan, um die Meldung zu verzögern, wenn ein Push-Token ungültig wird. Das bedeutet, dass APNs auch nach der Deinstallation einer App noch für eine gewisse Zeit erfolgreiche Antworten auf Push-Benachrichtigungen zurückgeben können. Diese Verzögerung ist beabsichtigt und dient dem Schutz der Privatsphäre der Nutzer:innen. Es wird kein Bounce oder Fehler gemeldet, bis APNs einen `410`-Status für ein ungültiges Token zurückgibt.