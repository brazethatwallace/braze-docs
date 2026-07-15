---
nav_title: Vorbereitungsleitfaden
article_title: Vorbereitungsleitfaden für In-App-Nachrichten
page_order: 0.5

page_type: reference
description: "Dieser Artikel behandelt Fragen und Best Practices, die Sie vor dem Erstellen von In-App-Nachrichten berücksichtigen sollten, einschließlich Targeting, Zeitplanung, Inhalt und Conversions."
channel: in-app messages
toc_headers: h2
---

# Vorbereitungsleitfaden für In-App-Nachrichten {#in-app-message-prep-guide}

> Bevor Sie Ihre In-App-Nachrichten erstellen, sollten Sie einige der folgenden Themen berücksichtigen, damit das Erstellen Ihrer Nachricht schnell und einfach gelingt.

## Allgemeine Überlegungen {#general-considerations}

- Wenn Sie eine Campaign erstellen, wie viele Varianten dieser Nachricht möchten Sie anzeigen? Ideen für Variantentests finden Sie unter [Tipps für verschiedene Kanäle]({{site.baseurl}}/user_guide/messaging/ab_testing#tips-different-channels).
- Wenn Sie einen Canvas erstellen, wird diese Nachricht in diesem Schritt mit anderen Messaging-Kanälen kombiniert?
- Wann soll [Ihre Nachricht ablaufen]({{site.baseurl}}/canvas_in-app_messages)?

## Überlegungen zum Targeting {#targeting-considerations}

- In-App-Nachrichten eignen sich am besten für Nutzer:innen, die Ihre App regelmäßig besuchen. Schließen Sie diese Zielgruppe ein?
- Wo sollen Ihre Nutzer:innen Ihre Nachricht sehen? In Ihrer Web-App? In Ihrer mobilen App?
- Welches Ereignis soll diese Nachricht auslösen?
- Verwenden einige Ihrer Nutzer:innen ältere Versionen Ihrer App? Falls ja, können sie möglicherweise einige Elemente Ihrer Nachricht nicht sehen.
- Für welchen Gerätetyp oder welche Geräte erstellen Sie diese Nachricht? Denken Sie daran, dass Sie Ihre Nachricht über das Feld **Vorschau** oder den Tab **Test** in der Vorschau anzeigen können. Weitere Informationen finden Sie unter [Testnachrichten senden]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message).

## Zeitplanung, Delays und Sitzungsstarts {#scheduling-delays-and-session-starts}

Wenn eine In-App-Nachrichten-Campaign **Delay planen** mit einem Trigger beim Sitzungsstart hat, kann ein:e Nutzer:in, der/die eine Sitzung startet und dann die App schließt, bevor die In-App-Nachricht angezeigt wird, diese Nachricht trotzdem beim nächsten Sitzungsstart erhalten, nachdem der Delay abgelaufen ist.

Dieses Timing kann zu unerwartetem Anzeigeverhalten führen, insbesondere wenn **Re-evaluate campaign eligibility before displaying** in der Campaign nicht ausgewählt ist.

Beispielsweise könnte ein:e Nutzer:in eine In-App-Nachricht mit einem acht Sekunden langen Delay einen Monat nach dem Start der Campaign erhalten. Das kann passieren, wenn die Person eine Sitzung gestartet, die Sitzung sofort beendet, einen Monat später eine neue Sitzung gestartet hat und dann acht Sekunden später die In-App-Nachricht erhalten hat. Wenn sie die App verlässt, ohne sie zu schließen, wird die In-App-Nachricht angezeigt, wenn sie zur App zurückkehrt.

## Überlegungen zum Inhalt {#content-considerations}

- Welche Sprachen werden Sie in dieser Nachricht verwenden?
- Was ist Ihr Header- und Body-Text? Sind sie auffällig und relevant für Ihre Nutzer:innen?
- In-App-Nachrichten werden nur für eine festgelegte Zeitspanne angezeigt. Ist Ihr Text prägnant und einprägsam?
- Werden Sie [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) verwenden, um benutzerdefinierten Text hinzuzufügen?
- Müssen Nutzer:innen Nachrichtentext kopieren (z. B. einen Rabatt- oder Gutscheincode)? Auf iOS und Android können Nutzer:innen Text oder Texteingabefelder durch langes Drücken kopieren. Langes Drücken funktioniert nicht bei Bildern – verwenden Sie daher Text oder Texteingabefelder anstelle von Bildern, die Codes oder andere Inhalte enthalten, die Nutzer:innen möglicherweise kopieren müssen.
- Befindet sich Ihr Bild oder anderes Medium bei Vollbild-In-App-Nachrichten innerhalb der [sicheren Zone]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)?
- Möchten Sie bei Umfrage-In-App-Nachrichten Attribute oder Einreichungen protokollieren? Haben Sie Ihre Bestätigungsseite eingerichtet?

## Überlegungen zu Conversions {#conversion-considerations}

- Was ist Ihr Ziel für diese Nachricht? Wie können Sie das in Ihrer Nachricht darstellen?
- Bieten Ihre Buttons Optionen, die für Ihre Nutzer:innen sinnvoll sind? Was ist Ihr [primärer Call-to-Action]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)?
- Erstellen Sie [Deeplinks zu anderen In-App-Inhalten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)? Verwenden Sie diese In-App-Nachricht, um eine [Berechtigungs- oder Push-Priming-Anfrage]({{site.baseurl}}/user_guide/channels/push/best_practices) zu senden und zu akzeptieren?
- Haben Sie eine Option zum Schließen der Nachricht? Falls nicht, können Sie jederzeit dieses Snippet kopieren und einfügen, um einen schnellen Button zu erstellen:
    ```html
    <a href="appboy://close">X</a>
    ```

## Überlegungen zum Drag-and-Drop-Editor {#drag-and-drop-editor-considerations}

### Deeplinks für verschiedene Geräte hinzufügen {#adding-deep-links-for-different-devices}

Der Drag-and-Drop-Editor unterstützt nicht das Hinzufügen verschiedener Deeplinks für verschiedene Geräte (im Gegensatz zum traditionellen Editor).

### Deckkraft des Hintergrundbilds anpassen {#adjusting-background-image-opacity}

Die Deckkraft-Einstellung erlaubt keine vollständige Transparenz von Hintergrundbildern (im Gegensatz zum traditionellen IAM-Editor). Sie können die Deckkraft-Einstellungen verwenden, um die Hintergrundfarbe der Nachricht vollständig transparent zu machen.

### Maximale Breite festlegen {#setting-the-maximum-width}

Die maximale Breite im Drag-and-Drop-Editor ist auf 325 px begrenzt; dies dient hauptsächlich der Dashboard-Vorschau. Nachrichten können auf kleineren Bildschirmgeräten korrekt angezeigt werden.

### Verschiedene Hintergründe für verschiedene Plattformen auswählen {#selecting-different-backgrounds-for-different-platforms}

Es ist nicht möglich, zwei verschiedene Hintergründe für dieselbe Nachricht auf verschiedenen Plattformen (z. B. Internet und Mobilgerät) anzuzeigen.

### Nachrichtenstile anwenden {#applying-message-styles}

Hintergrundbilder gelten für die gesamte Nachricht und können nicht pro Seite angepasst werden. Nachrichtenstile gelten für die gesamte Nachricht, nicht für einzelne Seiten.

### Höhe von Spacer-Blöcken messen {#measuring-spacer-blocks-height}

Die Maßeinheit für Spacer-Blöcke ist Pixel (px) und kann nicht geändert werden.

### Unterstützte Formate {#supported-formats}

Derzeit werden im Drag-and-Drop-Editor nur modale und Vollbild-In-App-Nachrichten unterstützt.

### Anpassung an Größe und Seitenverhältnis {#adjusting-to-size-and-aspect-ratio}

Das Hintergrundbild dehnt die In-App-Nachricht, da sich das Modal an die Größe und das Seitenverhältnis des Hintergrundbilds anpasst; Sie können das Verhältnis nach Bedarf anpassen.

### Hintergrundbilder und Klickverhalten {#background-images-and-on-click-behavior}

Diese bleiben über Seiten hinweg bestehen. Fügen Sie bei mehrseitigen In-App-Nachrichten mit verschiedenen Vollbildern auf jeder Seite einen Button hinzu, damit Nutzer:innen zur nächsten Seite klicken können.