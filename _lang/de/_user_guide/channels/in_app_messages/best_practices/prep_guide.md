---
nav_title: Vorbereitungsleitfaden
article_title: Vorbereitungsleitfaden für In-App-Nachrichten
page_order: 0.5

page_type: reference
description: "Dieser Artikel behandelt Fragen und Best Practices, die Sie vor dem Erstellen von In-App-Nachrichten berücksichtigen sollten, einschließlich Targeting, Zeitplanung, Inhalt und Konversionen."
channel: in-app messages
toc_headers: h2
---

# Vorbereitungsleitfaden für In-App-Nachrichten {#in-app-message-prep-guide}

> Bevor Sie Ihre In-App-Nachrichten erstellen, sollten Sie einige der folgenden Themen berücksichtigen, damit das Erstellen Ihrer Nachricht schnell und einfach gelingt.

## Allgemeine Überlegungen {#general-considerations}

- Wenn Sie eine Campaign erstellen, wie viele Varianten dieser Nachricht möchten Sie anzeigen? Ideen für Variantentests finden Sie unter [Tipps für verschiedene Kanäle]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels).
- Wenn Sie einen Canvas erstellen, wird diese Nachricht in diesem Schritt mit anderen Messaging-Kanälen kombiniert?
- Wann soll [Ihre Nachricht ablaufen]({{site.baseurl}}/canvas_in-app_messages)?

## Überlegungen zum Targeting {#targeting-considerations}

- In-App-Nachrichten eignen sich am besten für Nutzer:innen, die Ihre App regelmäßig besuchen. Schließen Sie diese Zielgruppe ein?
- Wo sollen Ihre Nutzer:innen Ihre Nachricht sehen? In Ihrer Web-App? In Ihrer mobilen App?
- Welches Ereignis soll diese Nachricht triggern?
- Verwenden einige Ihrer Nutzer:innen ältere Versionen Ihrer App? Falls ja, können sie möglicherweise einige Elemente Ihrer Nachricht nicht sehen.
- Für welchen Gerätetyp oder welche Geräte erstellen Sie diese Nachricht? Denken Sie daran, dass Sie Ihre Nachricht über das Feld **Vorschau** oder den Tab **Test** in der Vorschau anzeigen können. Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

## Zeitplanung, Verzögerungen und Sitzungsstarts {#scheduling-delays-and-session-starts}

Wenn eine In-App-Nachricht-Campaign eine **Zeitplanverzögerung** mit einem Trigger beim Sitzungsstart hat, kann eine Nutzer:in, die eine Sitzung startet und dann die App schließt, bevor die In-App-Nachricht angezeigt wird, diese Nachricht trotzdem beim nächsten Sitzungsstart erhalten, nachdem die Verzögerung abgelaufen ist.

Dieses Timing kann zu unerwartetem Anzeigeverhalten führen, insbesondere wenn **Kampagnenberechtigung vor der Anzeige erneut prüfen** in der Campaign nicht ausgewählt ist.

Beispielsweise könnte eine Nutzer:in eine In-App-Nachricht mit einer Verzögerung von acht Sekunden einen Monat nach dem Start der Campaign erhalten. Das kann passieren, wenn sie eine Sitzung gestartet, die Sitzung sofort beendet, einen Monat später eine neue Sitzung gestartet hat und dann acht Sekunden später die In-App-Nachricht erhalten hat. Wenn sie die App verlässt, ohne sie zu schließen, wird die In-App-Nachricht angezeigt, wenn sie zur App zurückkehrt.

## Überlegungen zum Inhalt {#content-considerations}

- Welche Sprachen werden Sie in dieser Nachricht verwenden?
- Wie lauten Ihre Überschrift und Ihr Fließtext? Sind sie aufmerksamkeitsstark und relevant für Ihre Nutzer:innen?
- In-App-Nachrichten werden nur für eine begrenzte Zeit angezeigt. Ist Ihr Text prägnant und einprägsam?
- Werden Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) verwenden, um angepassten Text hinzuzufügen?
- Müssen Nutzer:innen den Nachrichtentext kopieren (z. B. einen Rabatt- oder Gutscheincode)? Auf iOS und Android können Nutzer:innen Text oder Texteingabefelder durch langes Drücken kopieren. Langes Drücken funktioniert nicht bei Bildern – verwenden Sie daher Text oder Texteingabefelder anstelle von Bildern, die Codes oder andere Inhalte enthalten, die Nutzer:innen möglicherweise kopieren müssen.
- Befindet sich bei Vollbild-In-App-Nachrichten Ihr Bild oder anderes Medium innerhalb der [sicheren Zone]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)?
- Möchten Sie bei Umfrage-In-App-Nachrichten Attribute oder Einreichungen protokollieren? Haben Sie Ihre Bestätigungsseite eingerichtet?
- Enthält Ihr HTML bei angepassten HTML-In-App-Nachrichten UTF-8-Kodierung, um Sonderzeichen korrekt darzustellen? Weitere Informationen finden Sie unter [Angepasste HTML-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding).
- Wenn Sie Video in Ihre In-App-Nachricht einbinden: Braze erzwingt zwar keine technische Begrenzung der Videodateigröße für die lokale Wiedergabe auf dem Gerät, bedenken Sie jedoch, dass Nutzer:innen möglicherweise langsame Verbindungen, teure Datentarife oder begrenzten Speicherplatz haben. Optimieren Sie Videodateien, um ein ausgewogenes Verhältnis zwischen Qualität und Dateigröße zu erreichen.

## Überlegungen zur Konversion {#conversion-considerations}

- Was ist Ihr Ziel für diese Nachricht? Wie können Sie das in Ihrer Nachricht darstellen?
- Bieten Ihre Buttons Optionen, die für Ihre Nutzer:innen sinnvoll sind? Was ist Ihr [primärer Call-to-Action]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)?
- Nutzen Sie [Deeplinking zu anderen In-App-Inhalten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)? Verwenden Sie diese In-App-Nachricht, um eine [Berechtigungs- oder Push-Priming-Anfrage]({{site.baseurl}}/user_guide/channels/push/best_practices) zu senden und zu akzeptieren?
- Haben Sie eine Exit-Option für die Nachricht? Falls nicht, können Sie jederzeit dieses Snippet kopieren und einfügen, um einen schnellen Button zu erstellen:
    ```html
    <a href="appboy://close">X</a>
    ```

## Überlegungen zum Drag-and-Drop-Editor {#drag-and-drop-editor-considerations}

### Deeplinks für verschiedene Geräte hinzufügen {#adding-deep-links-for-different-devices}

Der Drag-and-Drop-Editor unterstützt nicht das Hinzufügen unterschiedlicher Deeplinks für verschiedene Geräte (im Gegensatz zum traditionellen Editor).

### Deckkraft von Hintergrundbildern anpassen {#adjusting-background-image-opacity}

Die Deckkraft-Einstellung erlaubt keine vollständige Transparenz von Hintergrundbildern (im Gegensatz zum traditionellen IAM-Editor). Sie können die Deckkraft-Einstellungen verwenden, um die Hintergrundfarbe der Nachricht vollständig transparent zu machen.

### Maximale Breite festlegen {#setting-the-maximum-width}

Die maximale Breite im Drag-and-Drop-Editor ist auf 325 px begrenzt; dies dient in erster Linie der Dashboard-Vorschau. Nachrichten können auf Geräten mit kleineren Bildschirmen korrekt angezeigt werden.

### Unterschiedliche Hintergründe für verschiedene Plattformen auswählen {#selecting-different-backgrounds-for-different-platforms}

Es ist nicht möglich, zwei verschiedene Hintergründe für dieselbe Nachricht auf unterschiedlichen Plattformen (z. B. Internet und Mobilgerät) anzuzeigen.

### Nachrichtenstile anwenden {#applying-message-styles}

Hintergrundbilder gelten für die gesamte Nachricht und können nicht pro Seite angepasst werden. Nachrichtenstile gelten für die gesamte Nachricht, nicht für einzelne Seiten.

### Höhe von Spacer-Blöcken messen {#measuring-spacer-blocks-height}

Die Maßeinheit für Spacer-Blöcke ist Pixel (px) und kann nicht geändert werden.

### Unterstützte Formate {#supported-formats}

Derzeit werden im Drag-and-Drop-Editor nur modale und Vollbild-In-App-Nachrichten unterstützt.

### Größe und Seitenverhältnis anpassen {#adjusting-to-size-and-aspect-ratio}

Das Hintergrundbild dehnt die In-App-Nachricht, da sich das Modal an die Größe und das Seitenverhältnis des Hintergrundbilds anpasst; Sie können das Verhältnis nach Bedarf anpassen.

### Hintergrundbilder und Klickverhalten {#background-images-and-on-click-behavior}

Diese bleiben seitenübergreifend bestehen. Fügen Sie bei mehrseitigen In-App-Nachrichten mit unterschiedlichen Vollbildern auf jeder Seite einen Button hinzu, damit Nutzer:innen zur nächsten Seite klicken können.