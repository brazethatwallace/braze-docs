---
nav_title: Push-Primer-In-App-Nachrichten
article_title: Push-Primer-In-App-Nachrichten
page_order: 1
page_type: reference
description: "Dieser Artikel behandelt die Voraussetzungen für Push-Primer-In-App-Nachrichten und wie Sie diese einrichten."
channel: push

---

# Push-Primer-In-App-Nachrichten {#push-primer-in-app-messages}

> Sie haben nur eine Chance, Nutzer:innen um die Push-Berechtigung zu bitten. Daher ist die Optimierung Ihrer Push-Registrierung entscheidend, um die Reichweite Ihrer Push-Nachrichten zu maximieren. Verwenden Sie In-App-Nachrichten, um zu erklären, welche Art von Nachrichten Ihre Nutzer:innen erwarten können, wenn sie sich für ein Opt-in entscheiden, bevor ihnen die native Push-Anfrage angezeigt wird. Dies wird als Push-Primer bezeichnet.

![Push-Primer-In-App-Nachricht für eine Streaming-App. Die Benachrichtigung lautet: „Push-Benachrichtigungen von Movie Cannon erhalten? Benachrichtigungen können neue Filme, TV-Sendungen oder andere Hinweise enthalten und können jederzeit deaktiviert werden.“]({% image_buster /assets/img_archive/push_primer_iam.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

Um eine Push-Primer-In-App-Nachricht in Braze zu erstellen, können Sie beim Erstellen einer In-App-Nachricht für iOS, Android oder Web das Button-Klickverhalten „Request Push Permission“ verwenden.

## Voraussetzungen {#prerequisites}

Dieses Feature erfordert ein [Button-Klickverhalten](#button-actions), das ab den folgenden Mindestversionen unterstützt wird:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

Beachten Sie außerdem die folgenden plattformspezifischen Details:

{% tabs local %}
{% tab android %}
| Betriebssystemversion | Zusätzliche Informationen |
|----------|----------------------|
| **Android 12 und früher** | Die Implementierung von Push-Primern wird nicht empfohlen, da Push standardmäßig aktiviert ist. |
| **Android 13+** | Wenn Nutzer:innen Ihre Push-Berechtigungsanfrage zweimal ablehnen, blockiert Android weitere Anfragen – einschließlich Braze-Push-Primer-Nachrichten. Um danach die Berechtigung zu erteilen, müssen Nutzer:innen Push für Ihre App manuell in den Geräteeinstellungen aktivieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }
{% endtab %}

{% tab swift %}
### Allgemeine Informationen {#general-information}

- Die Push-Anfrage kann nur einmal pro Installation angezeigt werden, was vom Betriebssystem erzwungen wird.
- Die Anfrage wird nicht angezeigt, wenn die Push-Einstellung der App explizit aktiviert oder deaktiviert ist. Sie wird nur für Nutzer:innen mit [vorläufiger Autorisierung](https://developer.apple.com/documentation/usernotifications/asking_permission_to_use_notifications#3544375) angezeigt.
  - **Push-Einstellung der App ist aktiviert:** Braze zeigt die In-App-Nachricht nicht an, da die Nutzer:innen bereits ein Opt-in durchgeführt haben.
  - **Push-Einstellung der App ist deaktiviert:** Sie müssen die Nutzer:innen zu den Push-Benachrichtigungseinstellungen Ihrer App in den Geräteeinstellungen weiterleiten.
- **Erneutes Testen nach Ablehnung:** Wenn Nutzer:innen die native Anfrage ablehnen, zeigt iOS sie für diese App-Installation nicht erneut an. Um den Push-Primer-Ablauf erneut zu testen, müssen Nutzer:innen die App in der Regel deinstallieren und neu installieren oder die Benachrichtigungsberechtigung für Ihre App in den **Einstellungen** ändern.

### Manuelle Code-Entfernung {#manual-code-removal}

Die In-App-Nachricht, die Sie mit diesem Tutorial einrichten, ruft automatisch den nativen Push-Anfrage-Code auf, wenn Nutzer:innen auf den Button der In-App-Nachricht klicken. Um zu vermeiden, dass die Push-Benachrichtigungsberechtigung zweimal oder zum falschen Zeitpunkt angefordert wird, sollten Entwickler:innen jede bestehende Push-Benachrichtigungsintegration so anpassen, dass Ihre In-App-Nachricht der erste Push-Benachrichtigungs-Primer ist, den Ihre Nutzer:innen sehen.

Ihr Entwicklungsteam sollte Ihre Implementierung von Push-Benachrichtigungen für Ihre App oder Website überprüfen und jeglichen Code manuell entfernen, der Push-Berechtigungen anfordert. Entfernen Sie beispielsweise Verweise auf den folgenden Code:

{% subtabs %}
{% subtab OBJECTIVE-C %}
```objc
requestAuthorizationWithOptions
```
{% endsubtab %}
{% subtab swift %}
```swift
requestAuthorization
```
{% endsubtab %}
{% subtab JavaScript %}
```javascript
braze.requestPushPermission()
// or
appboy.registerAppboyPushMessages()
```
{% endsubtab %}
{% subtab Java %}
```java
android.permission.POST_NOTIFICATIONS
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 1. Schritt: In-App-Nachricht erstellen {#step-1-create-an-in-app-message}

Erstellen Sie zunächst eine [In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional) und wählen Sie dann Ihren Nachrichtentyp und Ihr Layout aus.

Um sicherzustellen, dass Sie genügend Platz für Ihre Nachricht und Buttons haben, verwenden Sie ein Vollbild- oder Modal-Nachrichtenlayout. Wenn Sie Vollbild wählen, beachten Sie, dass ein Bild erforderlich ist.

## 2. Schritt: Nachricht erstellen {#step-2-build-your-message}

Jetzt ist es an der Zeit, Ihren Text hinzuzufügen! Denken Sie daran, dass ein Push-Primer die Nutzer:innen dazu bewegen soll, Push-Benachrichtigungen zu aktivieren. Im Nachrichtentext empfehlen wir, die Gründe hervorzuheben, warum Ihre Nutzer:innen Push-Benachrichtigungen aktivieren sollten. Seien Sie konkret, welche Art von Benachrichtigungen Sie senden möchten und welchen Mehrwert sie bieten können.

Beispielsweise könnte eine Nachrichten-App den folgenden Push-Primer verwenden:

```plaintext
Breaking news on the go! Enable push notifications to get alerts for major stories and topics that matter to you.
```

Während eine Streaming-App Folgendes verwenden könnte:

```plaintext
Get push notifications from Movie Cannon? Notifications may include new movies, TV shows, or other notices and can be turned off at any time.
```

Für Best Practices und zusätzliche Ressourcen lesen Sie [Benutzerdefinierte Opt-in-Anfragen erstellen]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages).

## 3. Schritt: Button-Verhalten festlegen {#button-actions}

Um Buttons zu Ihrer In-App-Nachricht hinzuzufügen, ziehen Sie zwei **Button**-Blöcke in Ihre Nachricht, die als primärer und sekundärer Button in Ihrer In-App-Nachricht fungieren. Sie können auch eine Zeile in Ihre Nachricht ziehen und dann die Buttons in die Zeile ziehen, sodass die Buttons in derselben horizontalen Reihe angeordnet sind (anstatt übereinander gestapelt). Wir empfehlen „Allow notifications“ und „Not now“ als Starter-Buttons, aber es gibt viele verschiedene Button-Aufforderungen, die Sie zuweisen können.

Nachdem Sie den Button-Text hinzugefügt haben, legen Sie das Klickverhalten für jeden Button fest:

- **Button 1:** Setzen Sie diesen auf „Close Message“. Dies ist Ihr sekundärer Button bzw. die Option „Not now“.
- **Button 2:** Setzen Sie diesen auf „Request Push Permission“. Dies ist Ihr primärer Button bzw. die Option „Allow notifications“.

![In-App-Nachrichten-Editor mit zwei Buttons: „Allow notifications“ und „Not now“.]({% image_buster /assets/img_archive/push_primer_button_behavior.png %})

## 4. Schritt: Zustellung planen {#step-4-schedule-delivery}

Um Ihren Push-Primer zu einem relevanten Zeitpunkt zu senden, müssen Sie Ihre In-App-Nachricht als aktionsbasierte Nachricht mit **Perform Custom Event** als Trigger-Aktion planen.

Obwohl der ideale Zeitpunkt variiert, empfiehlt Braze, zu warten, bis Nutzer:innen eine Art [hochwertige Aktion](https://www.braze.com/resources/videos/mapping-high-value-actions) abgeschlossen haben, die darauf hinweist, dass sie beginnen, den Wert Ihrer App oder Website zu erkennen, oder wenn ein überzeugender Bedarf besteht, den Push-Benachrichtigungen adressieren können (z. B. nachdem sie eine Bestellung aufgegeben haben und Sie ihnen Versandverfolgungsinformationen anbieten möchten). Auf diese Weise ist die Anfrage für die Kund:innen von Vorteil und nicht nur für Ihre Marke.

![Einstellungen für aktionsbasierte Zustellung, um an Nutzer:innen zu senden, die das angepasste Event „Add to Watch List“ ausgeführt haben.]({% image_buster /assets/img_archive/push_primer_trigger.png %})

## 5. Schritt: Nutzer:innen als Zielgruppe zusammenstellen {#step-5-target-users}

Das Ziel einer Push-Primer-Campaign ist es, Nutzer:innen auf jedem Gerät anzusprechen, auf dem sie noch keine Push-Berechtigungen erteilt haben. Dies kann Erstnutzer:innen oder bestehende Nutzer:innen umfassen, die ein neues Gerät erhalten oder Ihre Anwendung neu installieren.

{% alert important %}
**Automatische Unterdrückung mit No-Code-Push-Primer**: Wenn Sie den No-Code-Push-Primer (die Button-Aktion „Request Push Permission“) verwenden, müssen Sie keine Push-Abo-Filter zu Ihrer Segmentierung hinzufügen. Das SDK unterdrückt die In-App-Nachricht automatisch auf Geräten, die bereits über ein aktives Push-Token verfügen, unabhängig vom Push-Status der Nutzer:innen auf anderen Geräten. Weitere Informationen zum Targeting von Nutzer:innen mit mehreren Geräten finden Sie unter [Nutzer:innen mit mehreren Geräten als Zielgruppe zusammenstellen](#targeting-users-with-multiple-devices).
{% endalert %}

Wenn Sie den No-Code-Push-Primer nicht verwenden, fügen Sie einen Filter hinzu, bei dem `Foreground Push Enabled For App is false`. Dieser Filter identifiziert einzelne App-Installationen, die noch kein Opt-in für Vordergrund-Push-Benachrichtigungen durchgeführt haben.

{% alert important %}
Die Verwendung eines Filters auf Nutzer:innen-Ebene wie `Push Subscription Status is not Opted In` schließt Nutzer:innen aus, die bereits auf einem anderen Gerät ein Opt-in durchgeführt haben, und verhindert, dass sie die Anfrage auf ihrem neuen Gerät erhalten.
{% endalert %}

Darüber hinaus können Sie entscheiden, welche zusätzlichen Segmente Sie für am geeignetsten halten. Beispielsweise könnten Sie Nutzer:innen ansprechen, die einen zweiten Kauf abgeschlossen haben, Nutzer:innen, die gerade ein Konto erstellt haben, um Mitglied zu werden, oder sogar Nutzer:innen, die Ihre App mehr als zweimal pro Woche besuchen. Das Targeting von Nutzer:innen für diese entscheidenden Segmente erhöht die Wahrscheinlichkeit, dass Nutzer:innen ein Opt-in durchführen und Push-fähig werden.

### Nutzer:innen mit mehreren Geräten als Zielgruppe zusammenstellen {#targeting-users-with-multiple-devices}

Da Braze Nutzerdaten auf Profilebene und nicht auf Geräteebene erfasst, kann das Targeting von Nutzer:innen mit mehreren Geräten eine Herausforderung sein. Push-Abo-Filter in der Segmentierung schließen Nutzer:innen basierend auf dem Abo-Status eines einzelnen Geräts ein oder aus, nicht basierend auf dem Abo-Status des spezifisch angesprochenen Geräts. Zusätzlich erhöhen vorläufige Status auf iOS die Komplexität, da diese Geräte technisch über Vordergrund-Push-Token verfügen, die Nutzer:innen aber nicht explizit ein Opt-in durchgeführt haben.

#### Das Problem mit Push-Abo-Filtern {#the-problem-with-push-subscription-filters}

Wenn Nutzer:innen mehrere Geräte mit unterschiedlichen Push-Abo-Status haben, können Push-Abo-Filter in Ihrer Segmentierung einige Geräte möglicherweise nicht ansprechen. Betrachten Sie diese Szenarien:

{% details Szenario 1: Nutzer:in hat zwei Geräte auf verschiedenen Plattformen %}

**Nutzer:in hat zwei Geräte:**
- Gerät A: Android, Push-Opt-in durchgeführt
- Gerät B: iOS, kein Push-Opt-in durchgeführt

**Segment-Filter, die nicht funktionieren:**
- `Push enabled = false` – Nutzer:in hat Push auf dem Android-Gerät aktiviert, fällt also nicht in das Segment. Das Segment enthält das iOS-Gerät nicht.
- `Push subscription status is not opted in` – Nutzer:in hat Push auf dem Android-Gerät aktiviert, fällt also nicht in das Segment. Das Segment enthält das iOS-Gerät nicht.

**Segment-Filter, die funktionieren:**
- `Push enabled for iOS = false` – Nutzer:in hat Push auf dem Android-Gerät aktiviert, aber wir sprechen nur iOS-Geräte an, sodass die Nutzer:innen in das Segment fallen. Das Segment enthält das iOS-Gerät.

{% enddetails %}

{% details Szenario 2: Nutzer:in hat zwei iOS-Geräte mit unterschiedlichen Status %}

**Nutzer:in hat zwei iOS-Geräte:**
- Gerät A: Push-Opt-in durchgeführt
- Gerät B: Vorläufig aktiviert, aber kein Opt-in durchgeführt

**Segment-Filter, die nicht funktionieren:**
- `Push enabled = false` – Gerät A hat ein Push-Opt-in, sodass die Nutzer:innen nicht in das Segment fallen. Das Segment enthält Gerät B nicht.
- `Provisionally opted in = true` – Gerät A hat ein vollständiges Opt-in, was bedeutet, dass es sich nicht im vorläufigen Status befindet. Die Nutzer:innen fallen nicht in das Segment. Das Segment enthält Gerät B nicht.
- `Push enabled for app > iOS = false` – Gerät A hat ein Push-Opt-in auf iOS, sodass die Nutzer:innen nicht in das Segment fallen. Das Segment enthält Gerät B nicht.
- `Push subscription status is not opted in` – Gerät A hat ein Push-Opt-in, sodass die Nutzer:innen nicht in das Segment fallen. Das Segment enthält Gerät B nicht.

**Ergebnis:** Die Verwendung einer beliebigen Kombination dieser Push-Filter führt dazu, dass das Segment mindestens ein Gerät ausschließt.

{% enddetails %}

{% details Szenario 3: Nutzer:in hat drei oder mehr Geräte auf demselben Betriebssystem %}

**Nutzer:in hat drei Geräte:**
- Gerät A: Push-Opt-in durchgeführt
- Gerät B: Kein Push-Opt-in durchgeführt
- Gerät C: Kein Push-Opt-in durchgeführt

**Segment-Filter, die nicht funktionieren:**
- `Push enabled = false` – Gerät A hat ein Push-Opt-in, sodass die Nutzer:innen nicht in das Segment fallen. Das Segment enthält Geräte B und C nicht.
- `Push enabled for app > X = false` – Gerät A hat ein Push-Opt-in für die angegebene App, sodass die Nutzer:innen nicht in das Segment fallen. Das Segment enthält Geräte B und C nicht.
- `Push subscription status is not opted in` – Gerät A hat ein Push-Opt-in, sodass die Nutzer:innen nicht in das Segment fallen. Das Segment enthält Geräte B und C nicht.

**Ergebnis:** Die Verwendung einer beliebigen Kombination dieser Push-Filter lässt mindestens ein Gerät ohne Targeting.

{% enddetails %}

#### Lösung: Den No-Code-Push-Primer verwenden {#solution-use-the-no-code-push-primer}

Die empfohlene Lösung ist die Verwendung des No-Code-Push-Primers (die Button-Aktion „Request Push Permission“) ohne zusätzliche Push-Status-Segmentierungsfilter.

{% alert important %}
**Automatische Unterdrückung**: Der No-Code-Push-Primer wird automatisch auf Geräten unterdrückt, die bereits über ein aktives Push-Token verfügen. Das SDK prüft, ob Nutzer:innen auf ihrem spezifischen Gerät bereits ein Push-Token haben. Wenn das SDK feststellt, dass die Nutzer:innen bereits ein Opt-in durchgeführt haben (z. B. durch eine frühere Anfrage oder über die Geräteeinstellungen), unterdrückt das SDK die In-App-Nachricht automatisch, ohne dass zusätzliche Segmentierungsfilter erforderlich sind. Der Primer wird in allen anderen Szenarien angezeigt, auch wenn Nutzer:innen vorläufig für Push aktiviert sind.
{% endalert %}

Der Vorteil der Verwendung des No-Code-Push-Primers besteht darin, dass die Funktionalität vom Braze SDK unterstützt wird. Da das SDK den Push-Token-Status auf dem spezifischen Gerät erkennen kann, das die Nachricht anzeigt, müssen Sie sich nicht auf Segmentierungsfilter auf Profilebene verlassen, die Nutzer:innen mit mehreren Geräten möglicherweise ausschließen.

#### Überlegungen {#considerations}

**No-Code-Push-Primer erforderlich**: Sie müssen den No-Code-Push-Primer verwenden, damit die automatische Unterdrückung funktioniert. Wenn Sie benutzerdefinierte Logik oder Deeplinks anstelle der Button-Aktion „Request Push Permission“ einrichten, kann das SDK nicht erkennen, dass Sie versuchen, einen Push-Primer anzuzeigen. Dies führt dazu, dass die Nachricht unabhängig vom Abo-Status des Geräts angezeigt wird.

**Unterdrückung für Nutzer:innen, die sich abgemeldet haben**: Möglicherweise möchten Sie die In-App-Nachricht für Nutzer:innen unterdrücken, die sich explizit von Push abgemeldet haben (z. B. über die native Anfrage oder die Geräteeinstellungen), und diese Nutzer:innen mit einer separaten Nurture-Campaign erneut ansprechen. Verwenden Sie dazu die folgende Liquid-Logik in Kombination mit dem No-Code-Primer:

{% raw %}
```liquid
{% if targeted_device.${foreground_push_enabled} == false %}
{% abort_message('user turned off push notifications') %}
{% endif %}
- message goes here -
```
{% endraw %}

Der Liquid-Filter `targeted_device` betrachtet nur das Gerät, auf dem die Nachricht angezeigt wird, und nicht das Nutzerprofil. Auf diesem Gerät wird `foreground_push_enabled` auf `true` gesetzt, wenn ein aktives Vordergrund-Push-Token vorhanden ist, und auf `false`, wenn das Betriebssystem meldet, dass Push-Benachrichtigungen deaktiviert wurden (z. B. wenn die Nutzer:innen sie explizit ausgeschaltet haben). Bei völlig neuen Geräten, die noch nicht auf einen Push-Berechtigungsstatus reagiert haben, ist `foreground_push_enabled` nicht gesetzt und hat keinen Wert. Da die Liquid-Bedingung speziell auf {% raw %}`false`{% endraw %} prüft, wird der Primer nur für Geräte mit einem expliziten Opt-out unterdrückt, während Geräte in diesem unbekannten Status weiterhin qualifiziert sind und den Push-Primer erhalten können.

## 6. Schritt: Konversions-Events {#step-6-conversion-events}

Braze empfiehlt Standardeinstellungen für Conversions, aber Sie können auch [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) rund um Push-Primer einrichten.