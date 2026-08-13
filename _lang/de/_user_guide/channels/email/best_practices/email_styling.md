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

## Adressstil {#address-styling}

Die Betreffzeile ist eines der ersten Dinge, die Empfänger:innen beim Erhalt Ihrer Nachricht sehen. Eine Länge von 6 bis 10 Wörtern erzielt die höchsten Öffnungsraten.

Es gibt auch verschiedene Ansätze, um eine gute Betreffzeile zu erstellen – von einer Frage, die das Interesse der Leser:innen weckt, über einen direkteren Stil bis hin zur Personalisierung, um Ihre Kundschaft anzusprechen. Bleiben Sie nicht bei einer einzigen Betreffzeile, sondern nutzen Sie [A/B-Tests]({{site.baseurl}}/user_guide/messaging/ab_testing/faq#what-is-the-difference-between-ab-testing-and-multivariate-testing), um neue Varianten auszuprobieren und deren Wirksamkeit zu messen. Betreffzeilen sollten nicht mehr als 35 Zeichen umfassen, damit sie auf Mobilgeräten korrekt angezeigt werden.

Das „Von“-Feld sollte klar zeigen, wer der Sender ist. Verwenden Sie möglichst keinen Personennamen oder eine ungewöhnliche Abkürzung. Nutzen Sie stattdessen einen wiedererkennbaren Namen wie Ihren Markennamen. Wenn die Verwendung eines Personennamens zu den Personalisierungsmethoden Ihrer Marke für E-Mails passt, bleiben Sie konsistent, um eine Beziehung zu den Empfänger:innen aufzubauen. Der „Von“-Name sollte nicht mehr als 25 Zeichen umfassen, damit er auf Mobilgeräten korrekt angezeigt wird.

### No-Reply-Adressen {#no-reply-addresses}

No-Reply-E-Mail-Adressen werden aus mehreren Gründen generell nicht empfohlen, da sie Ihre Leser:innen abschrecken. Viele Empfänger:innen antworten auf die E-Mail, um sich abzumelden. Wenn ihnen das nicht möglich ist, besteht der nächste Schritt meistens darin, die E-Mail als Spam zu markieren.

Abwesenheitsbenachrichtigungen können tatsächlich wertvolle Informationen liefern, die Öffnungsraten erhöhen und Spam-Berichte reduzieren (indem diejenigen entfernt werden, die keine E-Mails erhalten möchten). Auf persönlicher Ebene kann eine No-Reply-Adresse auf Empfänger:innen unpersönlich wirken und sie davon abhalten, weitere E-Mails von Ihrem Unternehmen zu empfangen.

## Preheader-Text {#preheader-text}

Der Preheader-Text in einer E-Mail vermittelt den Hauptpunkt der Nachricht effizient, um das Interesse der Leser:innen zu wecken und zum Öffnen zu animieren. Preheader-Text wird von Marketern häufig auch genutzt, um zusätzliche Informationen zum Inhalt einer E-Mail bereitzustellen. Ein Preheader ist der Vorschautext, der direkt nach dem E-Mail-Betreff angezeigt wird. Im folgenden Beispiel lautet der Preheader `- Brand. New. Lounge Shorts`.

![Preheader-Text in einem Gmail-Posteingang mit dem Text „Brand. New. Lounge Shorts“.]({% image_buster /assets/img_archive/preheader_example.png %})

Die Menge des sichtbaren Preheader-Texts hängt vom E-Mail-Client der Nutzer:innen und der Länge der Betreffzeile ab. Generell empfehlen wir, E-Mail-Preheader zwischen 50 und 100 Zeichen lang zu halten.

{% alert note %}
Der Preheader kann auf Liquid im E-Mail-Text verweisen, und der E-Mail-Text kann auf Liquid im Preheader verweisen. Das liegt daran, dass der Preheader-Text Teil des E-Mail-Texts ist, wenn Sie Nachrichten an Empfänger:innen senden.
{% endalert %}

Hier sind einige Best Practices, die Sie beim Verfassen Ihrer Preheader beachten sollten:

1. Handlungsaufforderungen kommen ins Spiel, nachdem die Leser:innen Ihre E-Mail geöffnet haben.
  - Weisen Sie Ihre Leser:innen in die richtige Richtung, egal ob Sie möchten, dass sie sich anmelden, ein Produkt kaufen oder Ihre Website besuchen.
  - Verwenden Sie starke Formulierungen, damit die Leser:innen genau wissen, was Sie von ihnen erwarten, aber stellen Sie sicher, dass dies die Markenstimme Ihres Unternehmens widerspiegelt und dass jede Handlungsaufforderung einen gewissen Mehrwert für die Verbraucher:innen bietet.
  - Der Preheader sollte nicht mehr als 85 Zeichen umfassen und eine beschreibende Handlungsaufforderung enthalten, die die Betreffzeile unterstützt.

2. E-Mails und Landingpages, auf die Sie Ihre Nutzer:innen weiterleiten, sollten für Mobilgeräte optimiert sein:
  - Keine Interstitial-Boxen
  - Große Formularfelder
  - Einfache Navigation
  - Großer Text
  - Großzügiger Weißraum
  - Kurzer, prägnanter Fließtext
  - Klare Handlungsaufforderungen

### Zeichenlimits für Preheader {#preheader-character-limits}

  |   Mobiler E-Mail-Client  |  Limit  |
  |:------------------------:|:-------:|
  | iOS Outlook              | 74      |
  | Android Native           | 43      |
  | Android Gmail            | 24      |
  | iOS Native               | 82      |
  | iOS Gmail                | 30      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Zeichenlimits für Preheader" }

  |  Desktop-E-Mail-Client  |  Limit  |
  |:-----------------------:|:-------:|
  | Apple Mail              | 33      |
  | Outlook '13             | 38      |
  | Outlook for Mac '15     | 53      |
  | Outlook '16             | 50      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Zeichenlimits für Preheader" }


  |  Webmail-E-Mail-Client  |  Limit  |
  |:-----------------------:|:-------:|
  | AOL Mail                | 81      |
  | Gmail                   | 119     |
  | Outlook.com             | 49      |
  | Office 365              | 40      |
  | Mail.ru                 | 64      |
  {: .reset-td-br-1 .reset-td-br-2 aria-label="Zeichenlimits für Preheader" }

## E-Mail-Größe {#email-size}

Die E-Mail-Größe bezieht sich auf die Größe Ihres Nachrichten-HTML in Braze (der Body, den Sie erstellen, und das, was Braze beim Versand der Nachricht hinzufügt).

- Achten Sie darauf, die E-Mail-Größe zu begrenzen. E-Mail-Bodys, die größer als 102&nbsp;KB sind, belasten nicht nur die Braze-Server erheblich, sondern werden auch von Gmail und anderen E-Mail-Clients abgeschnitten.
- Gehostete Bilder, die Sie per URL referenzieren, werden nicht auf die gleiche Weise in das HTML eingebettet wie das Einfügen großer Inline-Assets. Wir empfehlen, die [Medienbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) zu verwenden und per `href` zu verlinken, um die Nachricht kleiner zu halten.

|   Nur Text   | Text mit Bildern |     E-Mail-Breite    |
|:-------------:|:----------------:|:------------------:|
| Maximal 25&nbsp;KB |   Maximal 60&nbsp;KB   | Maximal 600 Pixel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="E-Mail-Größe" }

So reduzieren Sie das Clipping-Risiko:

- Kürzen Sie Texte und Links.
- Setzen Sie kritisches CSS bei Bedarf inline ein. Entfernen Sie überflüssige Leerzeichen im HTML.
- Komprimieren Sie Bilder und HTML-Assets.

{% alert note %}
Um Ihre E-Mail-Campaign oder Ihr Template zu speichern, stellen Sie sicher, dass der E-Mail-Body 400&nbsp;KB nicht überschreitet.
{% endalert %}

### Was kann zur endgültigen E-Mail-Größe beitragen? {#what-can-add-to-the-final-email-size}

Diese Features erhöhen die gerenderte Nachrichtengröße um geringe Beträge:

- Open-Tracking-Pixel: Fügt ein 1 x 1&nbsp;px großes Image-Tag zum Nachrichten-Body hinzu
- Preheader: Fügt ein verstecktes `<div>` am Anfang des Bodys hinzu
- Link Aliasing: Hängt einen 16-stelligen Query-Parameter (`lid=`) an jede getrackte URL an
- Link-Templates: Hängen alle im Dashboard konfigurierten Query-Parameter an passende URLs an
- CSS-Inlining (optional): Wendet eingebettete Stylesheet-Regeln inline auf HTML-Elemente an, was je nach Stylesheet-Komplexität redundantes CSS hinzufügen kann

Der Preheader und das Tracking-Pixel fügen ungefähr 600 Zeichen hinzu (weniger als 1&nbsp;KB). Braze fügt in der Regel zwischen 0&nbsp;KB und 5&nbsp;KB hinzu, abhängig von der Anzahl der Links, der Komplexität der Link-Templates und davon, ob CSS-Inlining aktiviert ist. Wenn Ihre E-Mail-Größe nahe am Limit liegt, empfehlen wir, E-Mails vor dem Versand zu testen, da die endgültige gerenderte Größe von diesen Eingaben abhängt.

## Textlänge {#text-length}

In der folgenden Tabelle finden Sie empfohlene Textlängen.

| Textspezifikationen | Empfohlene Eigenschaften |
| --- | --- |
| Länge der Betreffzeile | Maximal 35 Zeichen (für optimale mobile Darstellung) (6 bis 10 Wörter) |
| Länge des Absendernamens | Maximal 25 Zeichen (für optimale mobile Darstellung) |
| Preheader-Länge | Maximal 85 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Textlänge" }

## Bildgröße {#image-size}

In der folgenden Tabelle finden Sie empfohlene Bildgrößen. Kleinere, hochwertige Bilder laden schneller – verwenden Sie daher das kleinstmögliche Asset, um das gewünschte Ergebnis zu erzielen.

|     Größe    | Breite des Header-Bildes |  Breite des Body-Bildes  |   Dateitypen  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| Maximal 5&nbsp;MB | Maximal 600 Pixel | Maximal 480 Pixel | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bildgröße" }

{% alert note %}
Gmail Web und die Gmail-Mobile-Apps rendern SVG häufig nicht (und die WEBP-Unterstützung ist uneinheitlich). Verwenden Sie PNG oder JPEG für Bilder, die in Gmail zuverlässig angezeigt werden müssen.
{% endalert %}

## Deeplinking {#deep-linking}

Mit Push-Benachrichtigungen und In-App Messages leitet ein [Deeplink]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls) Nutzer:innen direkt zu einem bestimmten Ziel innerhalb einer App. Deeplinks setzen jedoch voraus, dass die App installiert ist, und E-Mails bieten keine Möglichkeit festzustellen, ob Empfänger:innen die App haben. Das bedeutet, dass Deeplinks in E-Mails bei Empfänger:innen, die die App nicht installiert haben, zu Fehlern führen können.

Verwenden Sie stattdessen [Universal Links und App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links), die als Standard-URLs funktionieren. Sie können sie so konfigurieren, dass sie die App öffnen oder Nutzer:innen zu einer bestimmten Seite weiterleiten. Sie können auch zum App Store umleiten oder auf eine Webseite zurückfallen, wenn die App nicht installiert ist.

## Content Blocks mit transparenten Bildern {#content-blocks-with-transparent-images}

Wenn ein Content Block ein Bild mit transparentem Hintergrund enthält (zum Beispiel ein Logo) und über einen Liquid-Tag eingefügt wird, kann hinter dem Bild eine Hintergrundfarbe erscheinen. Diese Farbe stammt aus den [globalen E-Mail-Stileinstellungen]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings) des Drag-and-Drop-Editors – genauer gesagt aus der **E-Mail-Hintergrundfarbe**. Wenn Ihre globalen Stileinstellungen eine andere Farbe als Weiß verwenden, wird stattdessen diese Farbe angezeigt.

So zeigen Sie den Content Block wie vorgesehen an:

- Setzen Sie die Spalten-Hintergrundfarbe des Content Blocks auf die gleiche Farbe wie den E-Mail- oder Template-Hintergrund.
- Alternativ können Sie den Drag-and-Drop-Content-Block in einen HTML-Content-Block umwandeln und dessen Hintergrund auf transparent setzen.

Wenn Sie denselben Content Block in Bereichen mit unterschiedlichen Hintergründen verwenden müssen (zum Beispiel im Textkörper und in der Fußzeile), erstellen Sie zwei Versionen des Blocks, jeweils mit der passenden Spalten-Hintergrundfarbe.

Wenn Sie den Content Block lieber als Zeile in die E-Mail ziehen möchten, können Sie den Spaltenhintergrund der Zeile auf transparent setzen, um den globalen Hintergrund zu überschreiben.

{% alert note %}
Wenn ein Content Block als Zeile eingefügt wird, wird ein vorgerenderter Snapshot eingefügt, der sich nicht automatisch aktualisiert, wenn sich der Quell-Content-Block ändert.
{% endalert %}

## Dark Mode {#dark-mode}

Dark Mode ist eine empfängerseitige Einstellung. Posteingangsanbieter und Apps (wie Gmail und Outlook) können Ihr HTML invertieren oder umfärben, sodass Sie mit unterschiedlicher Darstellung je nach Client rechnen sollten – statt eines einheitlichen Erscheinungsbilds allein durch Braze.

### HTML-Editor {#html-editor}

Wenn Sie den **HTML-Editor** verwenden, können Sie unerwünschte Hintergrundinvertierung in den mobilen Gmail-Apps reduzieren, indem Sie auf Tabellenzellen einen einfarbigen CSS-`linear-gradient` anstelle einer flachen `background-color` anwenden. Beispiele, Einschränkungen (einschließlich der Verwendung von `<td>` oder `<th>` anstelle von `<table>` allein) und die Syntax finden Sie unter [Mobile Gmail-App und Dark Mode]({{site.baseurl}}/user_guide/channels/email/html_editor#gmail-dark-mode).

Um separate Stile für helle und dunkle Darstellung zu erstellen, wo Clients dies unterstützen, verwenden Sie die [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)-Media-Query. Die Unterstützung variiert je nach Posteingang – testen Sie immer eine Vorschau in den Clients, an die Sie senden.

### Drag-and-Drop-Editor {#drag-and-drop-editor}

Im Drag-and-Drop-Editor wird der Dark Mode weiterhin von jedem Posteingangsanbieter gesteuert. Aktivieren Sie die **Dark-Mode-Vorschau** unter **Vorschau und Test**, um Ihr Layout zu überprüfen. Wo Sie die Umschaltfunktion finden und wie Sie testen können, erfahren Sie unter [Kann ich eine Vorschau meiner E-Mail im Dark Mode anzeigen?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#can-i-preview-how-my-email-appears-in-dark-mode). Informationen zu Hintergrundfarben und Lesbarkeit über verschiedene Themes hinweg finden Sie unter [Wie sollte ich E-Mails für Dark Mode und Light Mode gestalten?]({{site.baseurl}}/user_guide/channels/email/drag_and_drop/faq#how-should-i-design-emails-for-dark-mode-and-light-mode).

### Allgemeine Best Practices {#general-best-practices}

- Vermeiden Sie reines Weiß (`#FFFFFF`) und reines Schwarz (`#000000`); verwenden Sie gebrochenes Weiß und abgemilderte Schwarztöne, damit vollständige Invertierungen weniger hart wirken.
- Dämpfen Sie sehr helle Akzentfarben (zum Beispiel auffällige Buttons), damit sie lesbar bleiben, falls ein Client die Farben invertiert.
- Verwenden Sie transparente PNGs, wenn sie zu Ihrem Layout passen.
- Fügen Sie bei Bildern mit Text eine helle Kontur um dunklen Text und eine dunkle Kontur um hellen Text auf dunklen Grafiken hinzu, damit der Text lesbar bleibt, wenn sich die Farben verschieben.