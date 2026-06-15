---
nav_title: Badge-Zähler nutzen
article_title: Badge-Zähler nutzen
page_order: 8

page_type: reference
description: "Dieser Artikel behandelt die Verwendung des iOS-Badge-Zählers, um Nutzer:innen erneut anzusprechen, die eine Push-Benachrichtigung nicht bemerkt haben oder die Push-Benachrichtigungen im Vordergrund deaktiviert haben."
platform: iOS
channel:
- push
- in-app messages

---

# Badge-Zähler nutzen {#utilizing-badge-count}

> Der iOS-Badge-Zähler zeigt die Anzahl ungelesener Benachrichtigungen innerhalb Ihrer Anwendung an und erscheint als roter Kreis in der oberen rechten Ecke des App-Symbols. In den letzten Jahren hat sich Badging zu einem effektiven Mittel entwickelt, um App-Nutzer:innen erneut zu aktivieren.

Der Badge-Zähler kann verwendet werden, um Nutzer:innen erneut anzusprechen, die eine Push-Benachrichtigung nicht bemerkt haben oder die Push-Benachrichtigungen im Vordergrund deaktiviert haben. Ebenso kann er genutzt werden, um Nutzer:innen über nicht angesehene Nachrichten wie In-App-Updates zu informieren.

## Badge-Zähler mit Braze {#badge-count-with-braze}

Sie können den gewünschten Badge-Zähler angeben, wenn Sie eine Push-Benachrichtigung über das Braze-Dashboard verfassen. Dieser kann auf ein Nutzer:innen-Attribut mit personalisiertem Messaging gesetzt werden, was endlos anpassbare Logik ermöglicht. Wenn Sie eine stille Push-Benachrichtigung senden möchten, die den Badge-Zähler aktualisiert, ohne die Nutzer:innen zu stören, fügen Sie das Flag „Content-Available“ zu Ihrer Push-Benachrichtigung hinzu und lassen Sie den Nachrichteninhalt leer.

{% alert note %}
Sie fragen sich, wie Sie Badge-Zähler für Android festlegen können? Android handhabt App-Badging für Push automatisch, daher gibt es in Braze keine Anpassungseinstellungen für Badging.
{% endalert %}

### Badge-Zähler entfernen {#removing-the-badge-count}

Setzen Sie den Badge-Zähler auf 0 oder „", um den Badge-Zähler vom App-Symbol zu entfernen. Braze löscht den Badge außerdem automatisch, wenn eine Push-Benachrichtigung empfangen wird, während die App im Vordergrund ist.

## Best Practices {#best-practices}

Um die Reaktivierungskraft von Badging optimal zu nutzen, ist es entscheidend, dass Sie Ihre Badge-Einstellungen so konfigurieren, dass die Nutzererfahrung so einfach wie möglich gestaltet wird.

### Badge-Zähler niedrig halten {#keep-the-badge-count-low}
Studien zeigen, dass Nutzer:innen nach Überschreiten des zweistelligen Bereichs beim Badge-Zähler in der Regel das Interesse an den Updates verlieren und die App häufig gar nicht mehr verwenden.

> Es kann Ausnahmen von dieser Regel geben, abhängig von der Art Ihrer App (zum Beispiel E-Mail- und Gruppen-Messaging-Apps).

### Begrenzen Sie, was ein Badge-Zähler darstellen kann {#limit-the-things-a-badge-count-can-represent}
Beim Badging sollten Sie die Benachrichtigungen so klar und direkt wie möglich gestalten. Indem Sie die Anzahl der Dinge begrenzen, die eine Badge-Benachrichtigung darstellen kann, vermitteln Sie Ihren Nutzer:innen ein Gefühl der Vertrautheit mit den Features und Updates Ihrer App.