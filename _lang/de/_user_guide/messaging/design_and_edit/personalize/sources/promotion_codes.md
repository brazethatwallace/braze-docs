---
nav_title: Aktionscodes
article_title: Aktionscodes
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Erfahren Sie mehr über Aktionscode-Listen, damit Sie diese zu Ihren Campaigns und Canvases hinzufügen können."
---

# Aktionscodes {#promotion-codes}

> Erfahren Sie mehr über Aktionscode-Listen, damit Sie diese zu Ihren Campaigns und Canvases hinzufügen können.

## Über Aktionscodes {#about-promotion-codes}

Mit Aktionscodes können Sie eindeutige, zeitlich begrenzte Werte in Nachrichten einfügen, um Conversions zu fördern. Jede Liste kann bis zu 20 Millionen Codes enthalten, und jeder Code kann bis zu sechs Monate gültig sein, bevor er abläuft.

Wenn Braze eine Nachricht mit einem Aktionscode sendet, wird der Code abgezogen, bevor die Nachricht versendet wird. Um sicherzustellen, dass Codes konsistent, eindeutig und nie wiederverwendet werden:

- Eine fehlgeschlagene Nachricht verbraucht dennoch den Code.
- Bei Multichannel-Sendungen wird derselbe Code über alle Kanäle hinweg angewendet.
- Bei bedingtem Liquid werden aus allen referenzierten Listen Codes abgezogen, auch wenn nur ein Branch angezeigt wird.
- Das Eintreten oder erneute Eintreten in einen Canvas-Schritt verbraucht einen neuen Code.

Wenn Sie mehrere Snippets aus derselben Liste in einer Nachricht platzieren, wendet Braze denselben Code auf alle Snippets an. Um ein Ausgehen der Codes zu vermeiden, empfehlen wir, mehr Codes hochzuladen, als Sie voraussichtlich benötigen.

{% tabs local %}
{% tab Beispiel %}
Stellen Sie sich Aktionscodes wie Gutscheine bei der Post vor. Sobald der Mitarbeiter einen Gutschein vom Stapel für Ihren Brief nimmt, ist er weg – auch wenn der Brief nie ankommt.

Im folgenden bedingten Liquid-Beispiel werden Codes aus beiden Listen (`vip-deal` und `regular-deal`) abgezogen, obwohl jede:r Nutzer:in nur einen Branch sieht:

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Aktionscodes sind in In-App-Nachrichten-Campaigns als Early-Access-Feature verfügbar, können jedoch nicht in In-App-Nachrichten in Canvas gesendet werden.
{% endalert %}

## Nächste Schritte {#next-steps}

Sie suchen nach den nächsten Schritten? Starten Sie hier:

- [Eine Aktionscode-Liste erstellen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create)
- [Aktionscodes verwenden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes)
- [Aktionscode-Nutzung anzeigen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#viewing-promotion-code-usage)

## Häufig gestellte Fragen {#frequently-asked-questions}

### Welche Messaging-Kanäle kann ich mit Aktionscodes verwenden? {#which-messaging-channels-can-i-use-with-promotion-codes}

Aktionscodes werden für E-Mail, mobilen Push, Web-Push, Content Cards, Webhook, SMS und WhatsApp unterstützt. In-App-Nachrichten-Campaigns unterstützen Aktionscodes als Early-Access-Feature. Braze-Transaktions-E-Mail-Campaigns und In-App-Nachrichten in Canvas unterstützen keine Aktionscodes.

### Zählen Test- und Seed-Sendungen zur Nutzung? {#do-test-and-seed-sends-count-towards-usage}

Standardmäßig verwenden Testsendungen und Seed-Gruppen-E-Mail-Sendungen Aktionscodes pro Nutzer:in und pro Testsendung. Sie können jedoch Ihren Braze Account Manager:in kontaktieren, um dieses Verhalten so zu ändern, dass während des Testens keine Aktionscodes verwendet werden.

### Was passiert, wenn mehrere Messaging-Kanäle dasselbe Aktionscode-Snippet verwenden? {#what-happens-when-multiple-messaging-channels-use-the-same-promotion-code-snippet}

Wenn ein:e bestimmte:r Nutzer:in berechtigt ist, einen Code über mehrere Kanäle zu erhalten, erhält diese Person denselben Code über jeden Kanal. Es wird nur ein Aktionscode verwendet, unabhängig von den empfangenen Kanälen.

### Kann ich mehrere Liquid-Snippets verwenden, um dieselbe Aktionscode-Liste in einer Nachricht zu referenzieren? {#can-i-use-multiple-liquid-snippets-to-reference-the-same-promotion-code-list-in-one-message}

Ja. Braze wendet denselben Aktionscode auf alle Instanzen dieses Snippets in der Nachricht an und stellt so sicher, dass die Nutzer:innen nur einen eindeutigen Code erhalten.

### Was passiert, wenn eine Aktionscode-Liste abgelaufen oder leer ist? {#what-happens-when-a-promotion-code-list-is-expired-or-empty}

Abgelaufene Codes werden nach sechs Monaten gelöscht.

Wenn die Nachricht einen Aktionscode aus einer leeren oder abgelaufenen Liste hätte enthalten sollen, wird die Nachricht abgebrochen.

Wenn die Nachricht Liquid-Logik enthält, die bedingt einen Aktionscode einfügt, wird die Nachricht nur abgebrochen, wenn sie einen Aktionscode hätte enthalten sollen. Wenn die Nachricht keinen Aktionscode hätte enthalten sollen, wird die Nachricht normal gesendet.

### Wenn ich die falschen Aktionscodes hochgeladen habe, kann ich sie aktualisieren? {#if-i-uploaded-the-wrong-promotion-codes-can-i-update-them}

Wenn Sie falsche Codes hochgeladen haben, haben Sie zwei Möglichkeiten, das Problem zu beheben:

- **Die gesamte Liste als veraltet markieren:** Verwenden Sie die aktuelle Liste nicht mehr in Campaigns, Canvases oder Templates. Laden Sie dann die korrekten Codes in eine neue Liste hoch und stellen Sie alle Ihre Nachrichten auf die neue Liste um.
- **Die falschen Codes aufbrauchen:** Erstellen Sie eine Campaign, die Codes aus der fehlerhaften Liste an eine:n Platzhalter-Nutzer:in sendet, bis alle falschen Codes verbraucht sind. Laden Sie danach die korrekten Codes in dieselbe Liste hoch, wobei Sie die fehlerhaften ausschließen.

Allgemeine Hinweise zum Aktualisieren einer Liste finden Sie unter [Eine Aktionscode-Liste aktualisieren]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#updating-a-promotion-code-list).

### Verfolgt Braze, welche Nutzer:innen welche Aktionscodes erhalten oder eingelöst haben? {#does-braze-track-which-users-received-or-redeemed-which-promotion-codes}

Wenn eine Nachricht einen Aktionscode verwendet, markiert Braze diesen Code als verbraucht, damit er nicht erneut gesendet werden kann, und aktualisiert die verbleibende Anzahl der Liste. Braze führt keinen Bericht über gesendete Codes, verfolgt nicht, welche Nutzer:innen welchen Code erhalten haben, und verfolgt nicht, ob Codes eingelöst wurden.

Wenn Sie Codes mit Nutzer:innen verknüpfen oder die Einlösung selbst nachverfolgen möchten, können Sie:

- Aktionscodes über einen Nutzeraktualisierung-Schritt in Nutzerprofilen speichern. Weitere Informationen finden Sie unter [Aktionscodes in Nutzerprofilen speichern]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile).
- Aktionscode-Werte über den `message_extras`-Liquid-Tag an Currents senden. Weitere Informationen finden Sie unter [Aktionscode-Informationen an Currents senden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras#sending-promotion-code-information-to-currents).

### Kann ich einen Aktionscode im Kundenprofil für zukünftige Nachrichten speichern? {#can-i-save-a-promotion-code-to-a-users-profile-for-future-messages}

Ja. Sie können Aktionscodes über einen Nutzeraktualisierung-Schritt im Kundenprofil speichern. Weitere Informationen finden Sie unter [Aktionscodes in Nutzerprofilen speichern]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#save-to-profile).