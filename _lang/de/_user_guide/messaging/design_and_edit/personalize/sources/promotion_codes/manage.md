---
nav_title: Codes verwenden
article_title: Aktionscodes verwenden
page_order: 0.2
description: "Erfahren Sie, wie Sie Aktionscodes verwenden und die Nutzung für Ihre Campaigns und Canvases einsehen können."
---

# Aktionscodes verwenden {#use-promotion-codes}

> Erfahren Sie, wie Sie Aktionscodes verwenden und die Nutzung für Ihre Campaigns und Canvases einsehen können.

## Voraussetzungen {#prerequisites}

Bevor Sie Aktionscodes verwenden können, müssen Sie [eine Aktionscode-Liste erstellen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create).

## Aktionscodes verwenden {#using-promotion-codes}

Um einen Aktionscode in einer Nachricht zu senden, wählen Sie **Snippet kopieren** neben der Aktionscode-Liste, [die Sie zuvor erstellt haben]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create).

![Eine Option zum Kopieren des Snippets, um es in Ihre Nachricht einzufügen.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Fügen Sie die Code-Snippets in eine Ihrer Nachrichten in Braze ein und verwenden Sie dann [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid), um einen der eindeutigen Aktionscodes aus Ihrer Liste einzufügen. Dieser Code wird als gesendet markiert, sodass keine andere Nachricht denselben Code sendet.

![Eine Beispielnachricht „Gönnen Sie sich diesen Frühling etwas Schönes mit unserem exklusiven Angebot“, gefolgt vom Code-Snippet.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Über Canvas-Schritte hinweg {#across-canvas-steps}

Wenn ein Code-Snippet in einer Campaign oder einem Canvas mit Multichannel-Nachrichten verwendet wird, erhält jede:r Nutzer:in einen eindeutigen Code. In einem Canvas mit mehreren Schritten, die auf Aktionscodes verweisen, erhält ein:e Nutzer:in für jeden Schritt, den sie/er betritt, einen neuen Code.

Um einen Aktionscode in einem Canvas zuzuweisen und über Schritte hinweg wiederzuverwenden:

1. Weisen Sie den Aktionscode im ersten Schritt (Nutzeraktualisierung) als angepasstes Attribut zu.
2. Verwenden Sie Liquid in späteren Schritten, um auf dieses angepasste Attribut zu verweisen, anstatt einen neuen Code zu generieren.

Wenn ein:e Nutzer:in sich über mehrere Kanäle für einen Code qualifiziert, erhält sie/er in jedem Kanal denselben Code. Wenn sie/er beispielsweise Nachrichten per E-Mail und Push erhält, wird derselbe Code an beide gesendet. Das Reporting spiegelt ebenfalls einen einzelnen Code wider.

{% alert note %}
Wenn keine Aktionscodes verfügbar sind, werden Test- oder Live-Nachrichten, die auf Codes angewiesen sind, nicht gesendet.
{% endalert %}

### In-App-Nachricht-Campaigns {#promotion-codes-iam-campaigns}

Nachdem Sie eine [In-App-Nachricht-Campaign]({{site.baseurl}}/user_guide/channels/in_app_messages) erstellt haben, können Sie ein [Aktionscode-Listen-Snippet]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/manage#using-promotion-codes) in den Nachrichtentext Ihrer In-App-Nachricht einfügen. Aktionscodes in In-App-Nachrichten werden erst abgezogen und verwendet, wenn ein:e Nutzer:in die Anzeige der In-App-Nachricht auslöst.

### Testnachrichten {#test-messages}

Testversendungen und Seed-Gruppen-E-Mail-Versendungen verbrauchen Aktionscodes, sofern nicht anders angefordert. Kontaktieren Sie Ihre:n Braze Account Manager:in, um dieses Feature-Verhalten zu aktualisieren, damit Aktionscodes bei Testversendungen und Seed-Gruppen-E-Mail-Versendungen nicht verwendet werden.

### Mit Message Extras für Currents {#with-message-extras-for-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## Aktionscodes in Nutzerprofilen speichern {#save-to-profile}

Um denselben Aktionscode in nachfolgenden Nachrichten zu referenzieren, muss der Code als angepasstes Attribut im Kundenprofil gespeichert werden. Dies kann über einen [Nutzeraktualisierungs-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) erfolgen, der den Rabattcode einem angepassten Attribut wie „Aktionscode“ direkt vor einem Nachrichten-Schritt zuweist.

Wählen Sie zunächst Folgendes für jedes Feld im Nutzeraktualisierungs-Schritt aus:

- **Attributname:** Aktionscode
- **Aktion:** Update
- **Schlüsselwert:** Das Liquid-Code-Snippet des Aktionscodes, z. B. {% raw %}`{% promotion('spring25') %}`{% endraw %}

Fügen Sie anschließend das angepasste Attribut (in diesem Beispiel {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) zu einer Nachricht hinzu. Der Rabattcode wird dann als Template eingefügt.

## Aktionscode-Nutzung einsehen {#viewing-promotion-code-usage}

Sie finden die verbleibende Code-Anzahl in der Spalte **Verbleibend** der Aktionscode-Liste auf der Seite **Aktionscodes**.

![Ein Beispiel eines Aktionscodes mit nicht verwendeten Codes.]({% image_buster /assets/img/promocodes/promocode11.png %})

Diese Code-Anzahl kann auch beim erneuten Aufrufen einer bestehenden Aktionscode-Listenseite eingesehen werden. Sie können nicht verwendete Codes auch als CSV-Datei exportieren.

![Ein Aktionscode namens „Black Friday Sale“ mit 992 verbleibenden Codes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Multichannel- und Einzelkanal-Versendungen {#multichannel-and-single-channel-sends}

Bei Multichannel- und Einzelversand-Campaigns und Canvases werden alle Aktionscodes, die im Liquid einer Nachricht referenziert werden, **vor** dem Senden der Nachricht abgezogen, um Folgendes sicherzustellen:

- Dieselben Aktionscodes werden kanalübergreifend in einer Multichannel-Nachricht verwendet.
- Zusätzliche Aktionscodes werden nicht verbraucht, wenn eine Nachricht fehlschlägt oder abgebrochen wird.

Wenn ein:e Nutzer:in zwei Aktionscode-Listen hat, die in einer Nachricht referenziert werden, die durch ein Liquid-Tag mit bedingter Logik aufgeteilt wird, werden alle Aktionscodes trotzdem abgezogen – unabhängig davon, welchem bedingten Pfad die/der Nutzer:in folgt.

Wenn ein:e Nutzer:in einen neuen Canvas-Schritt betritt oder erneut in einen Canvas eintritt und das Aktionscode-Liquid-Snippet erneut für eine Nachricht an diese:n Nutzer:in angewendet wird, wird ein neuer Aktionscode verwendet.

### Beispiel {#example}

Im folgenden Beispiel werden beide Aktionscode-Listen `vip-deal` und `regular-deal` abgezogen. Hier ist das Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}

Braze empfiehlt, mehr Aktionscodes hochzuladen, als Sie voraussichtlich benötigen. Wenn eine Aktionscode-Liste abläuft oder keine Aktionscodes mehr vorhanden sind, werden die nachfolgenden Nachrichten abgebrochen.

{% alert tip %}
**Hier ist eine Analogie dafür, wie Aktionscodes in Braze verbraucht werden.** <br><br>Stellen Sie sich vor, das Senden Ihrer Nachricht ist wie das Aufgeben eines Briefes bei der Post. Sie geben den Brief einem Postangestellten, und dieser sieht, dass Ihr Brief einen Coupon enthalten soll. Der Angestellte zieht den ersten Coupon vom Stapel und legt ihn in den Umschlag. Der Angestellte sendet den Brief, aber aus irgendeinem Grund geht der Brief auf dem Postweg verloren (und der Coupon ist nun ebenfalls verloren). <br><br>In diesem Szenario ist Braze der Postangestellte und Ihr Aktionscode ist der Coupon. Wir können ihn nicht zurückholen, nachdem er vom Stapel der Aktionscodes gezogen wurde – unabhängig vom Webhook-Ergebnis.
{% endalert %}