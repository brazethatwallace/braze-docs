---
nav_title: "E-Mail-Richtlinien"
article_title: "E-Mail-Richtlinien"
page_order: 1
page_type: reference
description: "Dieser Artikel behandelt allgemeine Tipps und Tricks, die Sie beim Erstellen von E-Mail-Campaigns für verschiedene Anwendungsfälle und Themen beachten sollten."
channel: email

---

# E-Mail-Richtlinien {#email-guidelines}

> Beim Erstellen Ihrer E-Mail-Campaign ist es wichtig zu beachten, wie Ihre E-Mail-Nachrichten bei Ihren verschiedenen Nutzer:innen und E-Mail-Anbietern (ESPs) ankommen.

## Allgemein {#general}

Hier sind einige kurze Tipps, die Sie beim Erstellen Ihrer Inhalte beachten sollten:

- Verwenden Sie beim Formatieren Ihrer E-Mail Inline-Stylesheets als CSS.
- Um ein E-Mail-Template sowohl für die mobile als auch die Desktop-Version zu verwenden, halten Sie die Breite unter 500 Pixeln.
- Bilder müssen unter 5&nbsp;MB groß sein. Wir empfehlen die Verwendung von PNG, JPEG oder GIF für maximale Kompatibilität. Vermeiden Sie SVG und WebP, da viele große E-Mail-Clients diese noch nicht unterstützen.
- Legen Sie keine Höhen und Breiten für Bilder fest, da dies unnötigen Leerraum in einer degradierten E-Mail verursachen kann.
- `div`-Tags sollten nicht verwendet werden, da die meisten E-Mail-Clients deren Verwendung nicht unterstützen. Verwenden Sie stattdessen verschachtelte Tabellen.
- Vermeiden Sie die Verwendung von JavaScript, da es mit keinem ESP funktioniert.
- Braze verbessert die Ladezeiten durch die Verwendung eines globalen CDN zum Hosten aller E-Mail-Bilder.
- Auf Mobilgeräten sind Bildspalten schmal (~100 px pro Spalte), sodass Zeilen mit mehreren Bildern trotzdem passen (zum Beispiel vier Bilder ≈ vier nutzbare Spalten).

## Alternativtext {#alternative-text}

Da Spamfilter sowohl auf eine HTML- als auch auf eine Nur-Text-Version einer Nachricht achten, ist die Verwendung von Nur-Text-Alternativen eine hervorragende Möglichkeit, Ihren Spam-Score zu senken. Darüber hinaus kann Alternativtext `(alt="")` dazu dienen, Bilder im E-Mail-Text zu ergänzen und in manchen Fällen zu ersetzen, die möglicherweise vom E-Mail-Anbieter der Nutzer:innen herausgefiltert wurden. Screenreader lesen den Alternativtext vor, um Bilder zu erklären. Dies ist also eine Gelegenheit, in einfacher Sprache wichtige Informationen über ein Bild bereitzustellen.

{% alert note %}
Wenn Ihr Alternativtext Anführungszeichen enthält, verwenden Sie einfache Anführungszeichen (`'`) anstelle von doppelten Anführungszeichen (`"`). Doppelte Anführungszeichen können dazu führen, dass das HTML-Attribut vorzeitig geschlossen wird und der Text abgeschnitten wird. Zum Beispiel funktioniert `alt="Product 'Premium' Edition"` korrekt, aber `alt="Product "Premium" Edition"` wird abgeschnitten.
{% endalert %}

## E-Mail-Validierung {#email-validation}

{% alert important %}
Die Validierung wird für Dashboard-E-Mail-Adressen, E-Mail-Adressen von Endnutzer:innen (Ihre Kund:innen) sowie für Absender- und Antwort-E-Mail-Adressen einer E-Mail-Nachricht verwendet.
{% endalert %}

Die E-Mail-Validierung erfolgt, wenn die E-Mail-Adresse einer Nutzer:in aktualisiert oder über die API, einen CSV-Upload, das SDK in Braze importiert oder im Dashboard geändert wird. Beachten Sie, dass E-Mail-Adressen keine Leerzeichen enthalten dürfen. Werden sie über die API gesendet, können Leerzeichen zu einem `400`-Fehler führen.

E-Mail-Adressen, die über die Braze-Server angesprochen werden, müssen gemäß den Standards von [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822) validiert werden. Braze akzeptiert bestimmte Zeichen nicht und erkennt sie als ungültig. Wenn eine E-Mail einen Bounce verursacht, markiert Braze die E-Mail als ungültig, und der Abo-Status wird nicht geändert.

Informationen zu unzulässigen Zeichen und E-Mail-Validierungsregeln finden Sie unter [E-Mail-Validierung]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation#how-it-works).

## Absender- und Antwort-E-Mail-Adressen {#from-and-reply-to-addresses}

Achten Sie beim Festlegen Ihrer Absenderadressen darauf, dass die Domain Ihrer Absender-E-Mail mit Ihrer Versanddomain übereinstimmt (z. B. `marketing.yourdomain.com`). Andernfalls kann es zu einer Fehlausrichtung von SPF und DKIM kommen. Alle Antwort-E-Mail-Adressen können auf Ihre Root-Domain gesetzt werden.

{% alert note %}
Unicode-Kodierung wird in Absenderadressen nicht unterstützt.
{% endalert %}

## Anhänge in E-Mails {#attachments}

Wenn Sie Anhänge zu E-Mail-Nachrichten hinzufügen, beachten Sie die folgenden Best Practices für die Zustellbarkeit:

- Spam-Filter scannen Anhänge und können Ihre Nachricht markieren.
- E-Mail-Anbieter benötigen manchmal länger, um Nachrichten mit Anhängen zu akzeptieren.
- Außerhalb von Eins-zu-eins-Nachrichten können Anhänge Ihre Nachricht im Posteingang riskant erscheinen lassen.
- Halten Sie jeden Anhang unter 2&nbsp;MB.
- Senden Sie keine sensiblen Informationen als Anhang. Leiten Sie Nutzer:innen stattdessen zu Ihrem sicheren Portal weiter, um die Informationen dort einzusehen.

## Layout (Drag-and-Drop und benutzerdefiniertes HTML) {#layout-drag-and-drop-and-custom-html}

Das Layout kann fehlerhaft dargestellt werden, wenn von Braze generiertes HTML/CSS mit benutzerdefiniertem HTML in Konflikt gerät. Gehen Sie in diesem Fall wie folgt vor:

- Entfernen Sie zunächst benutzerdefiniertes HTML/CSS
- Überprüfen Sie, ob benutzerdefinierte Schriftarten in der Vorschau korrekt geladen werden
- Überprüfen Sie das Padding von Zeilen und Spalten
- Bevorzugen Sie tabellenbasierte Layouts und bleiben Sie innerhalb der Breite des Editors

Content Blocks, die HTML von außerhalb des Editors einbinden, können ebenfalls das Layout beeinträchtigen.

## UTM-Parameter in E-Mail-URLs {#utm-parameters-in-email-urls}

UTM-Parameter kennzeichnen URLs für Analytics. Sie können sie mit Liquid und angepassten Attributen erstellen.

- Verwenden Sie nur ein Fragezeichen `?` in der endgültigen URL (zusätzliche `?`-Zeichen können Anfragen unterbrechen).
- Vermeiden Sie Leerzeichen und Sonderzeichen in Werten (verwenden Sie `_` oder `-`).
- Stellen Sie sicher, dass Ihr Analytics-Tool UTMs verarbeitet. Entfernen Sie nachgestellte Leerzeichen in Liquid-`capture`-Blöcken. UTMs unterscheiden zwischen Groß- und Kleinschreibung.

### HTML-Details prüfen {#check-html-details}

Beachten Sie, dass einige HTML-Tags und -Attribute nicht zulässig sind, da sie potenziell Schadcode im Browser ausführen könnten.

Sehen Sie sich die folgenden Listen für HTML-Tags und -Attribute an, die in Ihren E-Mails nicht zulässig sind:
{% details Erweitern für nicht zulässige HTML-Tags %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `iframe`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details Erweitern für nicht zulässige HTML-Attribute %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}