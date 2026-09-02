---
nav_title: Zustellbarkeit für chinesische Android-Geräte
article_title: Push-Zustellbarkeit für chinesische Android-Geräte
page_order: 10

page_type: reference
description: "Dieser Artikel behandelt Besonderheiten der Push-Zustellbarkeit, die Sie beachten sollten, wenn Sie Nutzer:innen auf Android-Geräten chinesischer OEMs ansprechen."
channel: push

---

# Push-Zustellbarkeit für chinesische Android-Geräte {#push-deliverability-for-chinese-android-devices}

> Einige Android-Geräte, die von chinesischen Originalgeräteherstellern (OEMs) wie Xiaomi, OPPO und Vivo produziert werden, optimieren die Akkulaufzeit durch ein aggressives App-Lifecycle-Management. Diese Optimierung kann den unbeabsichtigten Nebeneffekt haben, dass die Hintergrundverarbeitung von Apps beendet wird, was die Zustellbarkeit Ihrer Push-Benachrichtigungen verringern kann.<br><br>Um sicherzustellen, dass die Messaging-Performance Ihrer App auf diesen Geräten wie erwartet funktioniert, sollten Ihr Marketing- und Ihr Entwicklerteam zusammenarbeiten und die in diesem Artikel beschriebenen Schritte befolgen.

## Schritte für Entwickler:innen {#steps-for-developers}
Diese OEMs führen ihre Optimierungen durch, indem sie Hintergrund-Apps aggressiv beenden und deren automatischen Neustart für Hintergrundaufgaben blockieren. Als Entwickler:in müssen Sie Ihre App so konfigurieren, dass sie die Nutzer:innen auffordert, diese Einschränkungen nach Möglichkeit zu lockern.

Dies kann erreicht werden, indem Ihre App auf dem Gerät der Endnutzer:innen automatisch gestartet wird, wodurch Ihre App die Berechtigung erhält, im Hintergrund zu laufen und auf Nachrichten von Braze zu warten. Da es sich hierbei leider um ein OEM-spezifisches Problem und nicht um ein Android-Problem handelt, gibt es keine dokumentierten APIs, um die Autostart-Berechtigungsabfrage für jeden OEM aufzurufen.

Um dieses Problem zu lösen, integrieren Sie eine Bibliothek wie [AutoStarter](https://github.com/judemanutd/AutoStarter) in Ihre Anwendung. AutoStarter unterstützt mehrere Hersteller und bietet Ihnen eine einfache Möglichkeit, den Startup-Berechtigungsmanager auf einer Vielzahl von Geräten aufzurufen. Nachdem Sie AutoStarter integriert haben, rufen Sie `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)` auf, um den Startup-Berechtigungsmanager auf dem Gerät der Endnutzer:innen zu öffnen. Kombinieren Sie diese Aktion mit einer Aufforderung, die die Endnutzer:innen ermutigt, den „Autostart“ für Ihre App zu aktivieren. Ihr Marketing-Team wird diese Nachricht gestalten – siehe den nächsten Abschnitt!

## Schritte für Marketer {#steps-for-marketers}
Nachdem Ihre Nutzer:innen dem Empfang von Push-Benachrichtigungen zugestimmt haben, gibt es zusätzliche Schritte, die sie auf ihrer Seite unternehmen können, um die Nachrichtenzustellung auf diesen Geräten zu verbessern. Wir empfehlen, Ihre [Push-Primer-Nachricht]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) mit einer In-App-Nachricht zu ergänzen, die an Nutzer:innen auf chinesischen OEM-Geräten gerichtet ist und diese zusätzlichen Schritte enthält:

- „Autostart“ für die App aktivieren
- Akkuoptimierung für die App deaktivieren

Um Ihre Nachricht weiter zu verstärken, nutzen Sie zusätzliche Kanäle, um Informationen aus ungeöffneten Push-Benachrichtigungen über Out-of-App-Kanäle wie Kurzmitteilungsdienst or SMS, WhatsApp und LINE sowie In-App-Kanäle wie In-App-Nachrichten und Content Cards erneut anzuzeigen. Ihre Nutzer:innen können alles sehen, was sie möglicherweise verpasst haben, wenn sie die App das nächste Mal öffnen.