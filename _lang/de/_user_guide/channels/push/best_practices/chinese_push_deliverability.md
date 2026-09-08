---
nav_title: Zustellbarkeit für chinesische Android-Geräte
article_title: Push-Zustellbarkeit für chinesische Android-Geräte
page_order: 10

page_type: reference
description: "Dieser Artikel behandelt Besonderheiten der Push-Zustellbarkeit, die Sie beachten sollten, wenn Sie Nutzer:innen auf Android-Geräten chinesischer OEMs ansprechen."
channel: push

---

# Push-Zustellbarkeit für chinesische Android-Geräte {#push-deliverability-for-chinese-android-devices}

> Einige Android-Geräte, die von chinesischen Originalgeräteherstellern (OEMs) wie Xiaomi, OPPO, Vivo und Huawei produziert werden, optimieren die Akkulaufzeit durch ein aggressives App-Lifecycle-Management. Diese Optimierung kann den unbeabsichtigten Nebeneffekt haben, dass die Hintergrundverarbeitung von Apps beendet wird, was die Zustellbarkeit Ihrer Push-Benachrichtigungen verringern kann.<br><br>Um sicherzustellen, dass die Messaging-Performance Ihrer App auf diesen Geräten wie erwartet funktioniert, sollten Ihr Marketing- und Ihr Entwicklerteam zusammenarbeiten und die in diesem Artikel beschriebenen Schritte befolgen.

## Schritte für Entwickler:innen {#steps-for-developers}
Diese OEMs führen ihre Optimierungen durch, indem sie Hintergrundanwendungen aggressiv beenden und verhindern, dass diese sich selbständig starten, um Hintergrundaufgaben auszuführen. Als Entwickler:in müssen Sie Ihre App so konfigurieren, dass sie Nutzer:innen auffordert, diese Einschränkungen nach Möglichkeit zu lockern.

Dies lässt sich erreichen, indem Ihre App automatisch auf dem Gerät Ihrer Endnutzer:innen startet. Dadurch erhält Ihre App die Berechtigung, im Hintergrund zu laufen und auf Nachrichten von Braze zu warten. Da es sich hierbei leider um ein OEM-spezifisches und nicht um ein Android-Problem handelt, gibt es keine dokumentierten APIs, um die Autostart-Berechtigungsabfrage für jeden OEM aufzurufen.

Um dieses Problem zu lösen, integrieren Sie eine Bibliothek wie [AutoStarter](https://github.com/judemanutd/AutoStarter) in Ihre Anwendung. AutoStarter unterstützt mehrere Hersteller und bietet Ihnen eine einfache Möglichkeit, den Startberechtigungs-Manager auf einer Vielzahl von Geräten aufzurufen. Nachdem Sie AutoStarter integriert haben, rufen Sie `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` auf, um den Startberechtigungs-Manager auf dem Gerät Ihrer Endnutzer:innen zu öffnen. Kombinieren Sie diese Aktion mit einer Aufforderung, die Endnutzer:innen dazu ermutigt, den „Autostart“ für Ihre App zu aktivieren. Ihr Marketing-Team wird diese Nachricht gestalten – lesen Sie dazu den nächsten Abschnitt!

## Schritte für Marketer {#steps-for-marketers}
Nachdem Ihre Nutzer:innen dem Empfang von Push-Benachrichtigungen zugestimmt haben, können sie auf ihrer Seite weitere Schritte unternehmen, um die Nachrichtenzustellung für diese Geräte zu verbessern. Wir empfehlen, Ihre [Push-Einführungsnachricht]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) mit einer In-App-Nachricht zu ergänzen, die sich an Nutzer:innen auf chinesischen OEM-Geräten richtet und diese zusätzlichen Schritte enthält:

- „Autostart“ für die App aktivieren
- Batterieoptimierung für die App deaktivieren

### Nutzer:innen auf chinesischen OEM-Geräten identifizieren {#identifying-users-on-chinese-oem-devices}

Um Ihre In-App-Nachricht gezielt an Nutzer:innen auf bestimmten chinesischen OEM-Geräten auszurichten, verwenden Sie die [Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) **Device Model** oder **Device OS**:

- **Device Model:** Verwenden Sie diesen Filter, um Nutzer:innen nach dem Modell ihres Mobiltelefons anzusprechen. Um beispielsweise Huawei-Geräte zu identifizieren, verwenden Sie ein Regex-Muster mit `huawei`, um Modellnamen abzugleichen. Schrittweise Einrichtungsanleitungen finden Sie unter [Ein Device-Model-Regex für Huawei-Geräte erstellen](#build-a-device-model-regex-for-huawei-devices).
- **Device OS:** Verwenden Sie diesen Filter, um Nutzer:innen nach Betriebssystem anzusprechen. Einige chinesische OEMs wie Huawei geben möglicherweise ihre angepasste Android-Version explizit im Device-OS-Feld an. Informationen zu Überprüfungsschritten finden Sie unter [Device-OS-Werte vor dem Targeting überprüfen](#verify-device-os-values-before-you-target).

#### Ein Device-Model-Regex für Huawei-Geräte erstellen {#build-a-device-model-regex-for-huawei-devices}

1. Gehen Sie zu **Audience** > **Segments** und erstellen oder bearbeiten Sie ein Segment.
2. Fügen Sie den Filter **Device Model** hinzu.
3. Setzen Sie den Operator auf **matches regex**.
4. Geben Sie `huawei` ein, um Huawei-Modellnamen abzugleichen.
5. (Optional) Wenn Sie auch Honor-Markengeräte einschließen möchten, verwenden Sie `(huawei|honor)`.

Weitere Informationen zum Regex-Verhalten in Braze und zum Testen von Mustern finden Sie unter [Reguläre Ausdrücke]({{site.baseurl}}/user_guide/audience/segments/regex).

#### Device-OS-Werte vor dem Targeting überprüfen {#verify-device-os-values-before-you-target}

Einige OEM-Varianten können angepasste Betriebssystemnamen in den Gerätemetadaten melden. Da dieser Wert je nach Gerätemodell und Android-Distribution variieren kann, überprüfen Sie, was Ihre Nutzer:innen in Braze senden, bevor Sie das Segment erstellen:

1. Gehen Sie zu **Search Users** und öffnen Sie ein Profil für eine:n bekannte:n Zielnutzer:in.
2. Überprüfen Sie im Tab **Overview** unter **Recent devices** den für dieses Gerät angezeigten Betriebssystemwert.
3. Kopieren Sie den exakten Betriebssystem-String in Ihren Segmentfilter:
   - Verwenden Sie **Device OS**, wenn Sie einen exakten oder Regex-basierten Betriebssystem-String-Abgleich benötigen.
   - Verwenden Sie **Device OS Version Number**, wenn Sie numerische Versionsbereiche benötigen.
4. Verwenden Sie im Segment-Composer **User Lookup**, um zu bestätigen, dass Testnutzer:innen wie erwartet übereinstimmen.

Details dazu, wo Sie Gerätemetadaten in Profilen finden, finden Sie unter [Nutzerprofile]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). Details zum Testen der Segmentlogik finden Sie unter [Ein Segment erstellen]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments).