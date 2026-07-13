---
nav_title: Rechts-nach-links-Nachrichten
article_title: Rechts-nach-links-Nachrichten erstellen
page_order: 1
alias: /right_to_left_messages/
page_type: reference
description: "Diese Seite behandelt Best Practices für das Erstellen von Nachrichten in Braze, die von rechts nach links gelesen werden."
---

# Rechts-nach-links-Nachrichten erstellen {#create-right-to-left-messages}

> Das endgültige Erscheinungsbild von Rechts-nach-links-Nachrichten hängt weitgehend davon ab, wie Dienstanbieter (wie Apple, Android und Google) sie darstellen. Diese Seite behandelt Best Practices für das Erstellen von Rechts-nach-links-Nachrichten, damit Ihre Nachrichten so genau wie möglich angezeigt werden.

## Darstellung von Nachrichten {#message-appearance}

Beachten Sie beim Erstellen einer Rechts-nach-links-Nachricht Folgendes:

- **Darstellung im Braze-Dashboard:** Wenn eine Nachricht auf dem Gerät von Nutzer:innen erscheint, wird ihr Erscheinungsbild weitgehend durch das Betriebssystem und die Spracheinstellungen des Geräts bestimmt&#8212;das bedeutet, dass das, was Sie im Dashboard sehen, nicht immer zu 100 % genau ist.
- **Darstellung auf dem Gerät:** Apple und Android haben erheblichen Einfluss darauf, wie Nachrichten dargestellt werden, während E-Mail-Anbieter (ESPs) einen gewissen Einfluss haben. Die HTML-E-Mail-Anpassung in Braze kann flexibler sein; dennoch kann dieselbe Nachricht auf verschiedenen Geräten je nach den Einstellungen der Nutzer:innen unterschiedlich dargestellt werden.

Überprüfen Sie außerdem Satzzeichen und Emojis, um festzustellen, ob Ihre Nachricht standardmäßig oder von rechts nach links dargestellt wird.

| Standardmäßige westliche Darstellung | Rechts-nach-links-Darstellung |
|------------------|------------------------|
| Zeigt das Ausrufezeichen und Emoji am **Ende** der Sätze an. | Zeigt das Ausrufezeichen und Emoji am **Anfang** des Satzes an. |
| ![Ein Beispiel für eine standardmäßige Rechts-nach-links-Nachricht.]({% image_buster /assets/img/right-to-left/standard.png %}) | ![Ein Beispiel für eine Links-nach-rechts-Nachricht.]({% image_buster /assets/img/right-to-left/right-to-left.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Darstellung von Nachrichten" }

## Eine Rechts-nach-links-Nachricht erstellen {#creating-a-right-to-left-message}

So erstellen Sie Ihre Rechts-nach-links-Nachricht in Braze:

1. Verfassen Sie Ihre Standardnachricht im Braze-Editor.
2. Kopieren Sie den Nachrichtentext aus Braze und verwenden Sie dann ein Lokalisierungstool, um ihn in eine Rechts-nach-links-Nachricht umzuwandeln.
3. Fügen Sie Ihre konvertierte Nachricht wieder in Braze ein.
4. Überprüfen Sie die Textformatierung und Ausrichtung. Wenn Sie eine Drag-and-Drop- oder HTML-E-Mail-Nachricht erstellen, können Sie dies direkt im Composer tun. Andernfalls müssen Sie ein separates Textverarbeitungsprogramm verwenden.<br><br>![Menü des E-Mail-Drag-and-Drop-Editors mit Button zum Umschalten der Textausrichtung zwischen Rechts-nach-links und Links-nach-rechts.]({% image_buster /assets/img/rtl_button.png %}){: style="max-width:50%;"}

## Hinweise {#considerations}

### Lange Push-Benachrichtigungen {#long-push-notifications}

Die Kopieren-und-Einfügen-Methode für Push-Nachrichten kann bei längeren Push-Benachrichtigungen schwierig sein, da längerer Inhalt auf einem Mobilgerät in mehrere Zeilen umgebrochen werden kann. Wenn Sie Ihren Nachrichtentext von außerhalb von Braze kopieren (z. B. aus einem Word-Dokument) und direkt in Braze einfügen, können sich die Satzausrichtung und Wortplatzierung ändern. Um dies zu vermeiden, kopieren und fügen Sie in Abschnitten ein und fügen Sie einen Zeilenumbruch hinzu. Kopieren und fügen Sie beispielsweise die ersten fünf Wörter ein, fügen Sie einen Zeilenumbruch hinzu, kopieren Sie die nächsten fünf Wörter, fügen Sie einen Zeilenumbruch hinzu, und so weiter.

Die Vorschau- und Testfunktionen sind für Links-nach-rechts-Nachrichten konzipiert, sodass Rechts-nach-links-Nachrichten im Abschnitt **Preview & Test** nicht korrekt dargestellt werden, aber auf den Geräten der Nutzer:innen korrekt dargestellt werden, wenn deren Einstellungen entsprechend konfiguriert sind. Wir empfehlen, Nachrichten in einer Live-Umgebung an sich selbst zu senden, um zu bestätigen, dass sie basierend auf den Geräteeinstellungen korrekt dargestellt werden.

### Ausrichtung von Titel und Text {#title-and-body-alignment}

Bei Push-Benachrichtigungen folgt die Titelausrichtung in der Regel den Spracheinstellungen des Geräts, während die Textausrichtung dem ersten starken Richtungszeichen in jeder Zeile folgen kann (behandeln Sie jede Zeile nach einem Zeilenumbruch separat). Das bedeutet, dass eine einzelne Push-Benachrichtigung die Ausrichtung zeilenübergreifend mischen kann – zum Beispiel eine Rechts-nach-links-Textzeile gefolgt von einer Links-nach-rechts-Zeile. Wenn Sie ein vorhersehbares Layout benötigen, achten Sie auf eine einheitliche Schreibrichtung und verwenden Sie Zeilenumbrüche zwischen gemischtsprachigen Abschnitten.

{% alert note %}
Die Darstellung hängt weiterhin vom Betriebssystem des Geräts und dem Push-Client ab. Senden Sie [Testnachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages) an Ihre eigenen Geräte, um die Ausrichtung zu bestätigen, bevor Sie live gehen.
{% endalert %}

### Bidirektionaler Text {#bi-directional-text}

Viele Nutzer:innen, die in Rechts-nach-links-Sprachen schreiben, verwenden tatsächlich bidirektionalen Text: eine Kombination aus Links-nach-rechts- und Rechts-nach-links-Sprachen. Beispielsweise kann ein Marketer eine Nachricht auf Hebräisch mit einem englischen Unternehmensnamen senden. Braze kann die Formatierung von bidirektionalem Text nicht verarbeiten. Zwei Möglichkeiten, Formatierungsprobleme zu vermeiden, sind entweder bidirektionalen Text vollständig zu vermeiden oder Links-nach-rechts-Text von Rechts-nach-links-Text durch Zeilenumbrüche zu trennen.

{% alert tip %}
Die korrekte Formatierung von bidirektionalem Text ist besonders wichtig beim Erstellen von Nachrichten, die Promo-Codes enthalten. Promo-Codes sind oft im Links-nach-rechts-Format, da dieselben Codes marktübergreifend verwendet werden können. Zwei Möglichkeiten, Promo-Codes zu berücksichtigen, sind entweder ein Bild für den Promo-Code zu verwenden oder den Promo-Code am Ende der Nachricht nach einem Zeilenumbruch hinzuzufügen.
{% endalert %}

### Sonderzeichen, Zahlen und Emojis {#special-characters-numbers-and-emojis}

Sonderzeichen (wie Satzzeichen, mathematische Symbole und Währungszeichen), Zahlen, Aufzählungszeichen und Emojis können beim Erstellen von Rechts-nach-links-Nachrichten in Braze „herumspringen“. Um dies zu umgehen, schreiben Sie Ihren Text mit korrekter Formatierung in einem externen Textverarbeitungsprogramm und fügen Sie den Text dann in Braze ein. Es kann auch hilfreich sein, Emojis nicht am Anfang Ihres Textes zu platzieren und sie (sowie Sonderzeichen und Zahlen) stattdessen durch Zeilenumbrüche vom Text zu trennen, um Ausrichtungsprobleme zu vermeiden.

### Arabische Nachrichten {#arabic-messages}

Verwenden Sie beim Verfassen arabischer Nachrichten deutlich größere Schriftgrößen, um die gleiche Lesbarkeit zu erreichen wie bei anderen Sprachen. Wir empfehlen eine Schriftgröße, die etwa 20 % größer ist als Ihre übliche Größe für Sprachen, die das lateinische oder römische Alphabet verwenden. Dies liegt daran, dass arabische Schriftarten klein gestaltet sind, um den vertikalen Platz zu berücksichtigen, den diakritische Zeichen (Akzentzeichen) einnehmen.