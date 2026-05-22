---
nav_title: Aktionscodes
article_title: Aktionscodes
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Erfahren Sie mehr über Aktionscode-Listen, damit Sie diese zu Ihren Kampagnen und Canvases hinzufügen können."
---

# Aktionscodes

> Erfahren Sie mehr über Aktionscode-Listen, damit Sie diese zu Ihren Kampagnen und Canvases hinzufügen können.

## Über Aktionscodes

Mit Aktionscodes können Sie eindeutige, zeitlich begrenzte Werte in Nachrichten einfügen, um Conversions zu fördern. Jede Liste kann bis zu 20 Millionen Codes enthalten, und jeder Code kann bis zu sechs Monate gültig sein, bevor er abläuft.

Wenn Braze eine Nachricht mit einem Aktionscode sendet, wird der Code abgezogen, bevor die Nachricht versendet wird. Um sicherzustellen, dass Codes konsistent, eindeutig und nie wiederverwendet werden:

- Eine fehlgeschlagene Nachricht verbraucht dennoch den Code.
- Bei Multichannel-Sendungen wird derselbe Code über alle Kanäle hinweg angewendet.
- Bei bedingtem Liquid werden aus allen referenzierten Listen Codes abgezogen, auch wenn nur ein Branch angezeigt wird.
- Das Eintreten oder erneute Eintreten in einen Canvas-Schritt verbraucht einen neuen Code.

Wenn Sie mehrere Snippets aus derselben Liste in einer Nachricht platzieren, wendet Braze denselben Code auf alle Snippets an. Um ein Ausgehen der Codes zu vermeiden, empfehlen wir, mehr Codes hochzuladen, als Sie voraussichtlich benötigen.

{% tabs local %}
{% tab Beispiel %}
Stellen Sie sich Aktionscodes wie Gutscheine bei der Post vor. Sobald der Mitarbeiter einen Gutschein vom Stack für Ihren Brief nimmt, ist er weg – auch wenn der Brief nie ankommt.

Im folgenden bedingten Liquid-Beispiel werden Codes aus beiden Listen (`vip-deal` und `regular-deal`) abgezogen, obwohl jeder Nutzer nur einen Branch sieht:

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
Aktionscodes können nicht in In-App-Nachrichten in Canvas gesendet werden.
{% endalert %}

## Nächste Schritte

Sie suchen nach den nächsten Schritten? Starten Sie hier:

- [Eine Aktionscode-Liste erstellen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/)
- [Aktionscodes verwenden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#using-promotion-codes)
- [Aktionscode-Nutzung anzeigen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#viewing-promotion-code-usage)

## Häufig gestellte Fragen

### Welche Messaging-Kanäle kann ich mit Aktionscodes verwenden?

Aktionscodes werden derzeit für E-Mail, mobilen Push, Web-Push, Content-Cards, Webhook, SMS und WhatsApp unterstützt. Braze-Transaktions-E-Mail-Kampagnen und In-App-Nachrichten unterstützen derzeit keine Aktionscodes.

### Zählen Test- und Seed-Sendungen zur Nutzung?

Standardmäßig verwenden Testsendungen und Seed-Gruppen-E-Mail-Sendungen Aktionscodes pro Nutzer:in und pro Testsendung. Sie können jedoch Ihren Braze Account Manager kontaktieren, um dieses Verhalten so zu ändern, dass während des Testens keine Aktionscodes verwendet werden.

### Was passiert, wenn mehrere Messaging-Kanäle dasselbe Aktionscode-Snippet verwenden?

Wenn ein bestimmter Nutzer berechtigt ist, einen Code über mehrere Kanäle zu erhalten, erhält er denselben Code über jeden Kanal. Es wird nur ein Aktionscode verwendet, unabhängig von den empfangenen Kanälen.

### Kann ich mehrere Liquid-Snippets verwenden, um dieselbe Aktionscode-Liste in einer Nachricht zu referenzieren?

Ja. Braze wendet denselben Aktionscode auf alle Instanzen dieses Snippets in der Nachricht an und stellt so sicher, dass der Nutzer nur einen eindeutigen Code erhält.

### Was passiert, wenn eine Aktionscode-Liste abgelaufen oder leer ist?

Abgelaufene Codes werden nach sechs Monaten gelöscht.

Wenn die Nachricht einen Aktionscode aus einer leeren oder abgelaufenen Liste hätte enthalten sollen, wird die Nachricht abgebrochen.

Wenn die Nachricht Liquid-Logik enthält, die bedingt einen Aktionscode einfügt, wird die Nachricht nur abgebrochen, wenn sie einen Aktionscode hätte enthalten sollen. Wenn die Nachricht keinen Aktionscode hätte enthalten sollen, wird die Nachricht normal gesendet.

### Wenn ich die falschen Aktionscodes hochgeladen habe, kann ich sie aktualisieren?

Ja. Sie können dies lösen, indem Sie die gesamte Liste als veraltet markieren oder einen Platzhalter verwenden, um die Liste zu löschen. Weitere Informationen finden Sie unter [Eine Aktionscode-Liste aktualisieren]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create/#updating-a-promotion-code-list).

### Kann ich einen Aktionscode im Nutzerprofil für zukünftige Nachrichten speichern?

Ja. Sie können Aktionscodes über einen Nutzeraktualisierung-Schritt im Nutzerprofil speichern. Weitere Informationen finden Sie unter [Aktionscodes in Nutzerprofilen speichern]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage/#save-to-profile).