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

Braze erfasst automatisch grundlegende Informationen zu Deinstallationen aus Ihren regulären Push-Campaigns. Da die Häufigkeit, mit der verschiedene Nutzer:innen Push-Campaigns erhalten, jedoch variieren kann, bieten wir Uninstall-Tracking an, um ein genaueres Bild der Deinstallationsaktivität unter Ihren Nutzer:innen zu liefern.

Wenn Braze eine Deinstallation erkennt, wird die entsprechende Nutzer:in als deinstalliert markiert. Wenn Sie den Filter **Has Not Uninstalled** in einer Campaign verwenden, werden diese markierten Nutzer:innen ausgeschlossen. Wenn Nutzer:innen die App erneut installieren, sie aber nicht öffnen, bleibt das Deinstallations-Tag in ihrem Profil bestehen. Das Tag wird erst entfernt, wenn die Nutzer:innen eine neue Sitzung in der neu installierten App starten. Das bedeutet, dass Nutzer:innen, die die App erneut installieren, aber nie öffnen, weiterhin als deinstalliert angezeigt werden.

Weitere Informationen zur Verwendung von Uninstall-Tracking finden Sie in unserem Blog-Beitrag [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Uninstall-Tracking aktivieren {#turning-on-uninstall-tracking}

Sie können das Uninstall-Tracking auf der Seite **App Settings** unter **Settings** für jede App aktivieren, die Sie tracken möchten.

Wenn Sie das Uninstall-Tracking für eine App aktivieren, sendet Braze jede Nacht eine Push-Benachrichtigung im Hintergrund an Nutzer:innen, die in den letzten 24 Stunden keine Sitzung aufgezeichnet oder keinen Push erhalten haben.

### Konfiguration {#configuration}

Um das Uninstall-Tracking für Ihre iOS-Anwendung zu konfigurieren, verwenden Sie eine [Hilfsmethode]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls?sdktab=swift). Für Ihre Android-Anwendung verwenden Sie [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html). Wenn Braze eine Deinstallation erkennt – sei es durch das Uninstall-Tracking oder die reguläre Zustellung einer Push-Campaign –, wird der bestmöglich geschätzte Zeitpunkt der Deinstallation im Nutzerprofil erfasst. Dieser Zeitpunkt wird als Standardattribut im Nutzerprofil gespeichert und kann verwendet werden, um ein Segment von Nutzer:innen für Rückgewinnungs-Campaigns zu definieren.

## Segmente nach Deinstallationen filtern {#filtering-segments-by-uninstalls}

Der Filter **Deinstalliert** wählt Nutzer:innen aus, die Ihre App innerhalb eines bestimmten Zeitraums deinstalliert haben. Da es schwierig ist, den genauen Zeitpunkt einer Deinstallation zu bestimmen, empfehlen wir, für Deinstallationsfilter breitere Zeiträume zu verwenden, damit alle Nutzer:innen, die die App deinstallieren, irgendwann in das Segment fallen.

Tägliche Statistiken zu Deinstallationen finden Sie auf der **Home**-Seite.

![Deinstallations-Segment.]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

Der Graph kann nach App und Segment aufgeschlüsselt werden, ähnlich wie bei anderen Statistiken, die Braze bereitstellt. Wählen Sie im Abschnitt **Performance overview** Ihren Datumsbereich und gegebenenfalls eine App aus. Scrollen Sie dann nach unten zum Graphen **Performance Over Time** und gehen Sie wie folgt vor:

1. Wählen Sie im Dropdown **Statistics For** die Option **Uninstalls** aus.
2. Wählen Sie im Dropdown **Breakdown** die Option **By segment** aus.
3. Wählen Sie im Dropdown **Breakdown Values** die Segmente aus, die im Graphen enthalten sein sollen.

{% alert note %}
Apps ohne aktiviertes Uninstall-Tracking erfassen Deinstallationen nur von einer Teilmenge ihrer Nutzer:innen (jenen, die mit Push-Benachrichtigungen angesprochen wurden). Die täglichen Deinstallationszahlen können daher höher sein als dargestellt.
{% endalert %}

## Uninstall-Tracking für Campaigns {#uninstall-tracking-for-campaigns}

Das Uninstall-Tracking für Campaigns zeigt die Anzahl der Nutzer:innen, die eine bestimmte Campaign erhalten haben und anschließend Ihre App innerhalb des ausgewählten Zeitraums deinstalliert haben. Dieses Tool gibt Einblick, wie Campaigns möglicherweise unbeabsichtigte negative Verhaltensweisen der Nutzer:innen fördern, und hilft, die Gesamteffektivität von Campaigns zu messen.

Uninstall-Statistiken für Campaigns befinden sich auf der Seite **Campaign Analytics** der jeweiligen Campaign. Bei Multichannel- und multivariaten Campaigns können Deinstallationen nach Kanal bzw. Variante aufgeschlüsselt werden.

![Uninstall-Tracking auf Campaign-Ebene.]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### Wie es funktioniert

Braze verfolgt Deinstallationen, indem beobachtet wird, wann an die Geräte der Nutzer:innen gesendete Push-Nachrichten ein Signal von Firebase Cloud Messaging (FCM) oder dem Apple Push Notification Service (APNs) zurückgeben, dass die App nicht mehr installiert ist. Wenn Sie das globale Uninstall-Tracking für eine App aktivieren, sendet Braze täglich eine stille Push-Nachricht an Nutzer:innen, um zu erkennen, ob sie die App deinstalliert haben. Braze sendet diesen „stillen“ Push an alle Nutzer:innen (es sei denn, Nutzer:innen haben stille Pushes in ihren App-Einstellungen deaktiviert); der Push wird den Nutzer:innen nicht angezeigt. Wenn Braze erkennt, dass Nutzer:innen die App deinstalliert haben, geschieht Folgendes:

* Die Gesamtzahl der Deinstallationen der App wird um eins erhöht.
* Die Deinstallationszahl für jede Campaign, die die Nutzer:innen in den letzten 24 Stunden erfolgreich erhalten haben, wird um eins erhöht.
* Wenn Nutzer:innen innerhalb eines 24-Stunden-Zeitraums drei Campaigns erhalten und dann deinstallieren, wird die Anzahl der „Deinstallationen“ für alle drei Campaigns um eins erhöht.

FCM und APNs setzen dem Uninstall-Tracking Beschränkungen. Braze erhöht die Deinstallationszahl nur, wenn FCM oder APNs mitteilen, dass Nutzer:innen die App deinstalliert haben, aber diese Drittanbietersysteme können uns jederzeit über Deinstallationen informieren. Verwenden Sie das Uninstall-Tracking, um Richtungstrends zu erkennen, nicht für präzise Statistiken.

Braze behandelt eine FCM-Antwort als Token-Entfernung (Deinstallation), wenn FCM meldet, dass das Registrierungs-Token nicht mehr gültig ist, z. B. `DEVICE_UNREGISTERED` oder `NotRegistered`. Braze zeichnet andere Push-Fehler als Bounces auf, ohne das Token zu entfernen.

Weitere Informationen zur Verwendung des Uninstall-Trackings finden Sie in unserem Blogbeitrag [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/).

## Fehlerbehebung {#troubleshooting}

### Wann wird das Profil eines Nutzers/einer Nutzerin als deinstalliert markiert? Wann wird das Uninstall-Tag gelöscht? {#when-is-a-users-profile-flagged-as-uninstalled-when-is-the-uninstall-tag-cleared}

Braze markiert Nutzer:innen als deinstalliert, wenn erkannt wird, dass die App nicht mehr auf dem Gerät vorhanden ist (siehe [Wie es funktioniert](#how-it-works) zur Erkennung mit regulärem Push und optionalem Uninstall-Tracking). Nachdem jemand Ihre App erneut installiert hat, kann das Uninstall-Tag auf dem Profil bestehen bleiben, bis die Person **die App öffnet und eine neue Sitzung startet** – die Neuinstallation allein löscht das Tag nicht. Bis zu dieser Sitzung behandeln Segmente und Filter, die den Uninstall-Status verwenden (zum Beispiel **Has Not Uninstalled**), den/die Nutzer:in weiterhin als deinstalliert.

### Warum sehe ich plötzlich einen Anstieg bei den Deinstallationen? {#why-am-i-suddenly-seeing-a-spike-in-uninstalls}

Wenn Sie einen Anstieg bei den App-Deinstallationen sehen, kann dies daran liegen, dass Firebase Cloud Messaging (FCM) und der Apple Push Notification Service (APNS) alte Token in unterschiedlichen Abständen widerrufen.

{% alert note %}
Aus Datenschutzgründen können die Push-Anbieter von Braze Token in unregelmäßigen Abständen widerrufen, was bedeutet, dass die Deinstallationszahlen in einem bestimmten Zeitraum manchmal sprunghaft ansteigen können.<br><br>Um diese Änderungen zu validieren, überwachen Sie das Uninstall-Tracking zusammen mit einer nutzerbezogenen Aktionsmetrik, wie der direkten Push-Öffnungsrate. Wenn die Deinstallationen stark ansteigen, aber die direkten Push-Öffnungen stabil bleiben, spiegelt der Anstieg wahrscheinlich wider, dass ein Partner alte Token widerruft, und nicht tatsächliches Nutzerverhalten.
{% endalert %}

### Wie kann ich feststellen, ob eine bestimmte Campaign Deinstallationen verursacht hat? {#how-do-i-determine-if-a-specific-campaign-caused-uninstalls}

Überprüfen Sie die Analytics für die Campaigns, die ungefähr zum gleichen Zeitpunkt des Deinstallationsanstiegs Nachrichten gesendet haben. Wenn eine bestimmte Nachricht mit einem Anstieg der Deinstallationen korreliert, könnte sie Nutzer:innen zur Deinstallation bewegen.

So zeigen Sie Deinstallationen nach Segment an:
1. Gehen Sie zur **Startseite** des Dashboards.
2. Wählen Sie im Abschnitt **Performance Over Time** die Option **Uninstalls** für **Statistics For** und **By Segment** für **Breakdown** aus.

Wenn Sie ein Segment haben, das passive Nutzer:innen mit aktiviertem [Analytics-Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) verfolgt, vergleichen Sie dessen Deinstallationstrend mit dem allgemeinen App-Trend.

### Wie kann ich bestätigen, dass Deinstallationen echt sind? {#how-do-i-confirm-uninstalls-are-genuine}

Überprüfen Sie für APNs die Nutzerprofile auf den Push-Fehler `BadDeviceToken`. Wenn Sie diesen Fehler gehäuft im gleichen Zeitraum wie den Deinstallationsanstieg sehen, sind die Deinstallationen wahrscheinlich echt. `BadDeviceToken` zeigt an, dass das Push-Token des Geräts nicht mehr gültig ist, was in der Regel passiert, wenn die App deinstalliert wurde.

### Warum unterscheidet sich die Anzahl der App-Deinstallationen von den Angaben in APNs? {#why-are-the-number-of-app-uninstalls-different-from-whats-in-apns}

Der Unterschied ist zu erwarten.

Apple verwendet einen zufälligen Zeitplan, um die Meldung zu verzögern, wenn ein Push-Token ungültig wird. Das bedeutet, dass APNs auch nach der Deinstallation einer App durch Nutzer:innen für einen gewissen Zeitraum weiterhin erfolgreiche Antworten auf Push-Benachrichtigungen zurückgeben kann. Diese Verzögerung ist beabsichtigt und dient dem Schutz der Privatsphäre der Nutzer:innen. Es wird kein Bounce oder Fehler gemeldet, bis APNs einen `410`-Status für ein ungültiges Token zurückgibt.

### Wie hängt Uninstall-Tracking mit stillen oder Hintergrund-Push-Benachrichtigungen zusammen? {#how-does-uninstall-tracking-relate-to-silent-or-background-push}

Die Uninstall-Erkennung kann Push-Benachrichtigungen mit niedriger Priorität im Hintergrund verwenden, die nicht als sichtbare Benachrichtigung angezeigt werden. Diese sind von den [**Sends**]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) einer Campaign in den Standard-Messaging-Analytics getrennt. Wenn Sie Deinstallationstrends analysieren, überprüfen Sie die Deinstallations-Charts zusammen mit den Push-Engagement-Metriken, anstatt Uninstall-Pushes direkt mit den Marketing-Versandgesamtzahlen zu vergleichen.