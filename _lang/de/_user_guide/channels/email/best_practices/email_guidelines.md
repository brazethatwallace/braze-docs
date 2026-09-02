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

## Allgemeines {#general}

Hier sind einige kurze Tipps, die Sie beim Erstellen Ihrer Inhalte beachten sollten:

- Verwenden Sie beim Formatieren Ihrer E-Mail Inline-Stylesheets als CSS.
- Um ein E-Mail-Template sowohl für die mobile als auch die Desktop-Version zu verwenden, halten Sie die Breite unter 500 Pixeln.
- Bilder müssen unter 5&nbsp;MB groß sein. Wir empfehlen die Verwendung von PNG, JPEG oder GIF für maximale Kompatibilität. Vermeiden Sie SVG und WebP, da viele große E-Mail-Clients diese noch nicht unterstützen.
- Legen Sie keine Höhen und Breiten für Bilder fest, da dies unnötige Leerräume in einer eingeschränkt dargestellten E-Mail verursachen kann.
- `div`-Tags sollten nicht verwendet werden, da die meisten E-Mail-Clients deren Verwendung nicht unterstützen. Verwenden Sie stattdessen verschachtelte Tabellen.
- Vermeiden Sie die Verwendung von JavaScript, da es mit keinem E-Mail-Anbieter or ESP funktioniert.
- Vermeiden Sie `position: absolute` und `position: relative` in CSS in E-Mail-Templates. Die meisten E-Mail-Clients unterstützen keine CSS-Positionierung, was zu Layoutabweichungen zwischen der Braze-Vorschau und zugestellten E-Mails führt. Verwenden Sie tabellenbasierte Layouts, um geschichtete oder überlappende Effekte zu erzielen.
- Braze verbessert die Ladezeiten durch die Verwendung eines globalen CDN zum Hosten aller E-Mail-Bilder.
- Auf Mobilgeräten sind Bildspalten schmal (~100 px pro Spalte), sodass Zeilen mit mehreren Bildern dennoch passen (zum Beispiel vier Bilder ≈ vier nutzbare Spalten).

## Alternativtext {#alternative-text}

Da Spam-Filter sowohl nach einer HTML- als auch nach einer Klartextversion einer Nachricht suchen, ist die Verwendung von Klartextalternativen eine hervorragende Möglichkeit, Ihren Spam-Score zu senken. Darüber hinaus kann Alternativtext `(alt="")` dazu dienen, Bilder im E-Mail-Text zu ergänzen und in manchen Fällen zu ersetzen, die möglicherweise vom E-Mail-Anbieter der Nutzer:innen herausgefiltert wurden. Screenreader lesen Alternativtext vor, um Bilder zu erklären – dies ist also eine Gelegenheit, in einfacher Sprache wichtige Informationen über ein Bild bereitzustellen.

Der E-Mail-Client der Empfänger:innen – nicht Braze – bestimmt, wie Alternativtext angezeigt wird. Einzelheiten zu diesem Verhalten bei Clients wie Gmail, Outlook und Apple Mail finden Sie unter [Wie E-Mail-Clients Alternativtext anzeigen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text).

{% alert note %}
Wenn Ihr Alternativtext Anführungszeichen enthält, verwenden Sie einfache Anführungszeichen (`'`) anstelle von doppelten Anführungszeichen (`"`). Doppelte Anführungszeichen können dazu führen, dass das HTML-Attribut vorzeitig geschlossen wird und der Text abgeschnitten wird. Zum Beispiel funktioniert `alt="Product 'Premium' Edition"` korrekt, aber `alt="Product "Premium" Edition"` wird abgeschnitten.
{% endalert %}

## E-Mail-Validierung {#email-validation}

{% alert important %}
Die Validierung wird für Dashboard-E-Mail-Adressen, E-Mail-Adressen von Endnutzer:innen (Ihre Kund:innen) sowie Absender- und Antwort-E-Mail-Adressen einer E-Mail-Nachricht verwendet.
{% endalert %}

Die E-Mail-Validierung erfolgt, wenn die E-Mail-Adresse einer Nutzer:in aktualisiert oder über die API, einen CSV-Upload, das SDK or Software-Development-Kit in Braze importiert bzw. im Dashboard geändert wird. Beachten Sie, dass E-Mail-Adressen keine Leerzeichen enthalten dürfen. Wenn sie über die API gesendet werden, können Leerzeichen zu einem `400`-Fehler führen.

E-Mail-Adressen, die über die Braze-Server angesprochen werden, müssen gemäß den Standards von [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822) validiert werden. Braze akzeptiert bestimmte Zeichen nicht und erkennt sie als ungültig. Wenn eine E-Mail einen Bounce verursacht, markiert Braze die E-Mail als ungültig, und der Abo-Status wird nicht geändert.

Informationen zu nicht zulässigen Zeichen und E-Mail-Validierungsregeln finden Sie unter [E-Mail-Validierung]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation#how-it-works).

## Absender- und Antwortadressen {#from-and-reply-to-addresses}

Achten Sie beim Festlegen Ihrer Absenderadressen darauf, dass Ihre Absender-E-Mail-Domain mit Ihrer Versanddomain übereinstimmt (z. B. `marketing.yourdomain.com`). Andernfalls kann es zu einer SPF- und DKIM-Fehlausrichtung kommen. Alle Antwort-E-Mails können auf Ihre Root-Domain eingestellt werden.

{% alert note %}
Unicode-Codierung wird in Absenderadressen nicht unterstützt.
{% endalert %}


### Versanddomains und eingehende E-Mails {#sending-domains-and-inbound-mail}

Braze versendet E-Mails ausschließlich ausgehend. Versanddomains und -Subdomains werden für die Zustellbarkeit konfiguriert (SPF, DKIM und zugehörige DNS-Einträge), sind jedoch keine eingehenden Postfächer.

Sie können keine Antworten, die an eine Versand-Subdomain gesendet werden, über Braze in ein persönliches Postfach weiterleiten. Um Antworten von Nutzer:innen zu empfangen, konfigurieren Sie eine separate Antwortadresse auf einer Domain, die Sie kontrollieren und die über ein eingehendes Postfach verfügt. Siehe [Absender- und Antwortadressen](#from-and-reply-to-addresses).

## Anhänge in E-Mails {#attachments}

Wenn Sie Anhänge zu E-Mail-Nachrichten hinzufügen, beachten Sie die folgenden Best Practices für die Zustellbarkeit:

- Spam-Filter scannen Anhänge und können Ihre Nachricht markieren.
- E-Mail-Anbieter benötigen manchmal länger, um Nachrichten mit Anhängen zu akzeptieren.
- Außerhalb von Eins-zu-eins-Nachrichten können Anhänge Ihre Nachricht im Posteingang riskant erscheinen lassen.
- Halten Sie jeden Anhang unter 2&nbsp;MB.
- Senden Sie keine sensiblen Informationen als Anhang. Leiten Sie Nutzer:innen stattdessen zu Ihrem sicheren Portal weiter, um die Informationen dort einzusehen.

## Layout (Drag-and-drop und angepasstes HTML) {#layout-drag-and-drop-and-custom-html}

Das Layout kann beschädigt werden, wenn von Braze generiertes HTML/CSS mit angepasstem HTML in Konflikt gerät. Gehen Sie in diesem Fall wie folgt vor:

- Entfernen Sie zunächst angepasstes HTML/CSS
- Überprüfen Sie, ob angepasste Schriftarten in der Vorschau korrekt geladen werden
- Überprüfen Sie das Padding von Zeilen und Spalten
- Bevorzugen Sie tabellenbasierte Layouts und bleiben Sie innerhalb der Breite des Editors

Content Blocks, die HTML von außerhalb des Editors einbinden, können ebenfalls das Layout beschädigen.

## UTM-Parameter in E-Mail-URLs {#utm-parameters-in-email-urls}

UTM-Parameter versehen URLs mit Tags für Analytics. Sie können sie mit Liquid und angepassten Attributen erstellen.

- Verwenden Sie nur ein einziges Fragezeichen `?` in der endgültigen URL (zusätzliche `?`-Zeichen können Anfragen unterbrechen).
- Vermeiden Sie Leerzeichen und Sonderzeichen in Werten (verwenden Sie `_` oder `-`).
- Stellen Sie sicher, dass Ihr Analytics-Tool UTMs verarbeitet. Entfernen Sie nachfolgende Leerzeichen in Liquid-`capture`-Blöcken. UTMs sind case-sensitive.

### HTML-Details prüfen {#check-html-details}

Beachten Sie, dass einige HTML-Tags und -Attribute nicht zulässig sind, da sie möglicherweise Schadcode im Browser ausführen könnten.

Sehen Sie sich die folgenden Listen an, um zu erfahren, welche HTML-Tags und -Attribute in Ihren E-Mails nicht zulässig sind:
{% details Für nicht zulässige HTML-Tags aufklappen %}
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

{% details Für nicht zulässige HTML-Attribute aufklappen %}
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

## Fehlerbehebung bei doppelten E-Mails {#troubleshooting-duplicate-emails}

Wenn Nutzer:innen berichten, dass sie doppelte E-Mails erhalten, können die folgenden Szenarien dabei helfen, die Ursache zu identifizieren:

### Konfigurationsfehler bei der Erstellung von Campaigns oder Canvas {#configuration-error-at-campaign-or-canvas-creation}

Nutzer:innen erhalten möglicherweise nicht dieselbe E-Mail zweimal, sondern zwei separate E-Mails mit derselben Betreffzeile. Wenn eine Campaign oder ein Canvas dupliziert wird, können grundlegende E-Mail-Konfigurationsdetails wie Bilder oder die Betreffzeile leicht übersehen werden.

So gehen Sie bei der Untersuchung vor:

1. Überprüfen Sie das Kundenprofil or Nutzerprofil und sehen Sie sich jedes Canvas und jede Campaign an, die der/die Nutzer:in erhalten hat.
2. Überprüfen Sie die Änderungsprotokolle, um festzustellen, ob die Campaign oder das Canvas nach dem Start geändert wurde. Es ist möglich, dass die Campaign oder das Canvas zum Zeitpunkt des Empfangs dieselbe Betreffzeile wie das Original hatte.

### Campaign wurde mehrfach gesendet {#campaign-sent-multiple-times}

Wenn die Anzahl der gesendeten Nachrichten deutlich größer ist als die Anzahl der Nutzer:innen in der Zielgruppe, kann dies darauf hindeuten, dass die Campaign mehrfach gestartet wurde.

Weitere Informationen darüber, wie Braze mit doppelten E-Mail-Adressen und Deduplizierung umgeht, finden Sie in den [E-Mail-FAQ]({{site.baseurl}}/user_guide/channels/email/faq#what-happens-when-an-email-is-sent-out-and-multiple-profiles-have-the-same-email-address).