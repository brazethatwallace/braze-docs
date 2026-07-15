---
nav_title: E-Mail-Styling
article_title: E-Mail-Styling
page_order: 2
page_type: reference
description: "In diesem Artikel finden Sie Best Practices für das E-Mail-Styling, einschließlich Betreffzeilen, Preheader-Text, E-Mail-Größe und Bildempfehlungen."
channel: email

---

# E-Mail-Styling {#email-styling}

> Dieser Artikel beschreibt Best Practices für das E-Mail-Styling, einschließlich Betreffzeilen, Preheader-Text, E-Mail-Größe und Bildempfehlungen.

## Adress-Styling {#address-styling}

Die Betreffzeile ist eines der ersten Dinge, die Empfänger:innen sehen, wenn sie Ihre Nachricht erhalten. Wenn Sie sich auf 6 bis 10 Wörter beschränken, erzielen Sie die höchsten Öffnungsraten.

Es gibt auch verschiedene Ansätze für eine gute Betreffzeile – von einer Frage, um das Interesse der Leser:innen zu wecken, über eine direktere Formulierung bis hin zur Personalisierung, um Ihre Kundschaft gezielt anzusprechen. Bleiben Sie nicht bei einer einzigen Betreffzeile, sondern nutzen Sie [A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/faq#what-is-the-difference-between-ab-testing-and-multivariate-testing), um neue Betreffzeilen auszuprobieren und ihre Wirksamkeit zu messen. Die Betreffzeilen sollten nicht länger als 35 Zeichen sein, damit sie auf Mobilgeräten richtig angezeigt werden.

Im Feld „Von“ sollte klar ersichtlich sein, wer der Sender ist. Verwenden Sie möglichst nicht den Namen einer Person oder eine ungewöhnliche Abkürzung. Verwenden Sie stattdessen einen wiedererkennbaren Namen wie Ihren Markennamen. Wenn die Verwendung eines Personennamens zu den Personalisierungsmethoden Ihrer Marke für E-Mails passt, bleiben Sie konsequent, um eine Beziehung zu den Empfänger:innen aufzubauen. Der „Von“-Name sollte nicht länger als 25 Zeichen sein, damit er auf Mobilgeräten richtig angezeigt wird.

### No-Reply-Adressen {#no-reply-addresses}

No-Reply-E-Mail-Adressen werden aus mehreren Gründen generell nicht empfohlen, da sie Ihre Leser:innen abschrecken. Viele Empfänger:innen antworten auf die E-Mail, um sich abzumelden. Wenn ihnen das nicht möglich ist, besteht die nächste Maßnahme meistens darin, die E-Mail als Spam zu markieren.

Abwesenheitsbenachrichtigungen können tatsächlich wertvolle Informationen liefern, die Öffnungsraten erhöhen und Spam-Berichte reduzieren (indem diejenigen entfernt werden, die keine E-Mails erhalten möchten). Auf persönlicher Ebene kann eine No-Reply-Adresse auf Empfänger:innen unpersönlich wirken und sie davon abhalten, weitere E-Mails von Ihrem Unternehmen zu empfangen.

## Preheader-Text {#preheader-text}

Der Preheader-Text in einer E-Mail kommuniziert den Hauptpunkt der Nachricht effizient, um das Interesse der Leser:innen zu wecken und Öffnungen zu fördern. Preheader-Text wird von E-Mail-Marketern auch häufig verwendet, um zusätzliche Informationen zum Inhalt einer E-Mail bereitzustellen. Ein Preheader ist der Vorschautext, der direkt nach dem E-Mail-Betreff angezeigt wird. Im folgenden Beispiel lautet der Preheader `- Brand. New. Lounge Shorts`.

![Preheader-Text in einem Gmail-Posteingang mit dem Text „Brand. New. Lounge Shorts“.]({% image_buster /assets/img_archive/preheader_example.png %})

Die Menge des sichtbaren Preheader-Texts hängt vom E-Mail-Client der Nutzer:innen und der Länge der Betreffzeile ab. Generell empfehlen wir, dass E-Mail-Preheader zwischen 50 und 100 Zeichen lang sein sollten.

{% alert note %}
Der Preheader kann Liquid im E-Mail-Body referenzieren, und der E-Mail-Body kann Liquid im Preheader referenzieren. Das liegt daran, dass der Preheader-Text Teil des E-Mail-Bodys ist, wenn Sie Nachrichten an Empfänger:innen senden.
{% endalert %}

Hier sind einige Best Practices, die Sie beim Verfassen Ihrer Preheader beachten sollten:

1. Handlungsaufforderungen kommen ins Spiel, nachdem die Leser:innen Ihre E-Mail geöffnet haben.
  - Weisen Sie Ihre Leser:innen in die richtige Richtung, egal ob Sie möchten, dass sie sich anmelden, ein Produkt kaufen oder Ihre Website besuchen.
  - Verwenden Sie starke Formulierungen, damit die Leser:innen genau wissen, was Sie von ihnen erwarten, aber stellen Sie sicher, dass es die Markenstimme Ihres Unternehmens widerspiegelt und dass jede Handlungsaufforderung einen gewissen Mehrwert für die Verbraucher:innen bietet.
  - Der Preheader sollte nicht mehr als 85 Zeichen umfassen und eine beschreibende Handlungsaufforderung enthalten, die die Betreffzeile unterstützt.

2. E-Mails und Landingpages, auf die Sie Ihre Nutzer:innen weiterleiten, sollten für Mobilgeräte optimiert sein:
  - Keine Interstitial-Boxen
  - Große Formularfelder
  - Einfache Navigation
  - Großer Text
  - Großzügiger Weißraum
  - Kurzer, prägnanter Fließtext
  - Klare Handlungsaufforderungen

### Preheader-Zeichenlimits {#preheader-character-limits}

  |   Mobiler E-Mail-Client  |  Limit  |
  |:----------------------:|:-------:|
  | iOS Outlook            | 74      |
  | Android Native         | 43      |
  | Android Gmail          | 24      |
  | iOS Native             | 82      |
  | iOS Gmail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Preheader-Zeichenlimits" }

  |  Desktop-E-Mail-Client  |  Limit  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook for Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Preheader-Zeichenlimits" }


  |  Webmail-E-Mail-Client  |  Limit  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Preheader-Zeichenlimits" }

## E-Mail-Größe {#email-size}

Die E-Mail-Größe bezieht sich auf die Größe Ihres Nachrichten-HTML in Braze (der Body, den Sie erstellen, und das, was Braze beim Senden der Nachricht hinzufügt).

- Achten Sie darauf, Ihre E-Mail-Größe zu begrenzen. E-Mail-Bodys, die größer als 102&nbsp;KB sind, belasten nicht nur die Braze-Server erheblich, sondern werden auch von Gmail und anderen E-Mail-Clients abgeschnitten.
- Gehostete Bilder, die Sie per URL referenzieren, werden nicht auf die gleiche Weise in das HTML eingebettet wie das Einfügen großer Inline-Assets. Wir empfehlen die Verwendung der [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) und die Verlinkung per `href`, um die Nachricht kleiner zu halten.

|   Nur Text   | Text mit Bildern |     E-Mail-Breite    |
|:-------------:|:----------------:|:------------------:|
| Maximal 25&nbsp;KB |   Maximal 60&nbsp;KB   | Maximal 600 Pixel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="E-Mail-Größe" }

Um das Risiko des Abschneidens zu reduzieren:

- Kürzen Sie Texte und Links.
- Inlinen Sie kritisches CSS bei Bedarf. Entfernen Sie überflüssige Leerzeichen im HTML.
- Komprimieren Sie Bilder und HTML-Assets.

{% alert note %}
Um Ihre E-Mail-Campaign oder Ihr Template zu speichern, stellen Sie sicher, dass Ihr E-Mail-Body 400&nbsp;KB nicht überschreitet.
{% endalert %}

### Was kann zur endgültigen E-Mail-Größe beitragen? {#what-can-add-to-the-final-email-size}

Diese Features erhöhen die gerenderte Nachrichtengröße um geringe Beträge:

- Öffnungs-Tracking-Pixel: Fügt ein 1 x 1&nbsp;px Bild-Tag zum Nachrichten-Body hinzu
- Preheader: Fügt ein verstecktes `<div>` am Anfang des Bodys hinzu
- Link Aliasing: Hängt einen 16-Zeichen-Abfrageparameter (`lid=`) an jede getrackte URL an
- Link-Templates: Hängen alle im Dashboard konfigurierten Abfrageparameter an passende URLs an
- CSS-Inlining (optional): Wendet eingebettete Stylesheet-Regeln inline auf HTML-Elemente an, was je nach Stylesheet-Komplexität redundantes CSS hinzufügen kann

Der Preheader und das Tracking-Pixel fügen ungefähr 600 Zeichen hinzu (weniger als 1&nbsp;KB). Braze fügt typischerweise zwischen 0&nbsp;KB und 5&nbsp;KB hinzu, abhängig von der Anzahl der Links, der Link-Template-Komplexität und ob CSS-Inlining aktiviert ist. Wenn Ihre E-Mail-Größe nahe am Limit liegt, empfehlen wir, E-Mails vor dem Senden zu testen, da die endgültige gerenderte Größe von diesen Eingaben abhängt.

## Textlänge {#text-length}

Die folgende Tabelle enthält empfohlene Textlängen.

| Textspezifikationen | Empfohlene Eigenschaften |
| --- | --- |
| Betreffzeilenlänge | Maximal 35 Zeichen (für optimale mobile Anzeige) (6 bis 10 Wörter) |
| Absendernamenlänge | Maximal 25 Zeichen (für optimale mobile Anzeige) |
| Preheader-Länge | Maximal 85 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Textlänge" }

## Bildgröße {#image-size}

Die folgende Tabelle enthält empfohlene Bildgrößen. Kleinere, hochwertige Bilder laden schneller – verwenden Sie daher das kleinstmögliche Asset, um die gewünschte Ausgabe zu erzielen.

|     Größe    | Header-Bildbreite |  Body-Bildbreite  |   Dateitypen  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| Maximal 5&nbsp;MB | Maximal 600 Pixel | Maximal 480 Pixel | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bildgröße" }

{% alert note %}
Gmail Web und die Gmail-Mobile-Apps rendern SVG häufig nicht (und die WEBP-Unterstützung ist inkonsistent). Verwenden Sie PNG oder JPEG für Bilder, die in Gmail zuverlässig angezeigt werden müssen.
{% endalert %}

## Deeplinking {#deep-linking}

Bei Push-Benachrichtigungen und In-App-Nachrichten führt ein [Deeplink]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) Nutzer:innen direkt zu einem bestimmten Ziel innerhalb einer App. Deeplinks erfordern jedoch, dass die App installiert ist, und E-Mails bieten keine Möglichkeit zu wissen, ob Empfänger:innen die App haben. Das bedeutet, dass Deeplinks in E-Mails zu Fehlern bei Empfänger:innen führen können, die die App nicht installiert haben.

Verwenden Sie stattdessen [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links), die als Standard-URLs funktionieren. Sie können sie so konfigurieren, dass sie die App öffnen oder Nutzer:innen zu einer bestimmten Seite weiterleiten. Sie können auch zum App Store weiterleiten oder auf eine Webseite zurückfallen, wenn die App nicht installiert ist.

## Content Blocks mit transparenten Bildern {#content-blocks-with-transparent-images}

Wenn ein Content-Block ein Bild mit transparentem Hintergrund enthält (z. B. ein Logo) und über einen Liquid-Tag eingefügt wird, kann hinter dem Bild eine Hintergrundfarbe erscheinen. Diese Farbe stammt aus den [globalen E-Mail-Stileinstellungen]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) des Drag-and-Drop-Editors – insbesondere der **E-Mail-Hintergrundfarbe**. Wenn Ihre globalen Stileinstellungen eine andere Farbe als Weiß verwenden, erscheint diese Farbe stattdessen.

Um den Content-Block wie beabsichtigt anzuzeigen:

- Setzen Sie die Spalten-Hintergrundfarbe des Content-Blocks so, dass sie mit dem E-Mail- oder Template-Hintergrund übereinstimmt.
- Alternativ können Sie den Drag-and-Drop-Content-Block in einen HTML-Content-Block umwandeln und dessen Hintergrund auf transparent setzen.

Wenn Sie denselben Content-Block in Bereichen mit unterschiedlichen Hintergründen verwenden müssen (z. B. Body und Fußzeile), erstellen Sie zwei Versionen des Blocks, jeweils mit der passenden Spalten-Hintergrundfarbe.

Wenn Sie den Content-Block lieber als Zeile in die E-Mail ziehen möchten, können Sie den Zeilen-Spaltenhintergrund auf transparent setzen, um den globalen Hintergrund zu überschreiben.

{% alert note %}
Das Ziehen eines Content-Blocks als Zeile fügt einen vorgerenderten Snapshot ein, der sich nicht automatisch aktualisiert, wenn sich der Quell-Content-Block ändert.
{% endalert %}