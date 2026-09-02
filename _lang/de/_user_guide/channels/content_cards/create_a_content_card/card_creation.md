---
nav_title: Kartenerstellung
article_title: Kartenerstellung
alias: /card_creation/
description: "Dieser Artikel beschreibt die Unterschiede zwischen der Content-Card-Erstellung beim Kampagnenstart oder Canvas-Schritt-Eintritt und der Erstellung bei der ersten Impression."
page_order: 0
tool: Campaigns
channel:
  - content cards
toc_headers: h2
---

# Kartenerstellung {#card-creation}

> Sie können festlegen, wann Braze die Zielgruppeneignung und Personalisierung für neue Content-Card-Kampagnen und Canvas-Schritte ermittelt, indem Sie bestimmen, wann die Karte erstellt wird.

## Voraussetzungen {#prerequisites}

Um dieses Feature nutzen zu können, müssen Sie auf die folgenden Mindest-SDK or Software-Development-Kit-Versionen upgraden:

{% sdk_min_versions swift:5.2.0 objc:4.5.0 android:23.0.0 web:4.2.0 %}

Unter iOS unterstützt das Swift SDK or Software-Development-Kit dieses Feature ab Version 5.2.0, und das Legacy-Objective-C-SDK or Software-Development-Kit unterstützt es ab Version 4.5.0. Die Swift-SDK or Software-Development-Kit-Versionen 5.0.0 bis 5.1.x unterstützen es nicht.

Nach dem SDK or Software-Development-Kit-Upgrade or upgraden müssen Ihre mobilen Nutzer:innen ihre App Update or aktualisieren or aktualisieren. Sie können Ihre Campaign- oder Canvas-Zielgruppe filtern, um nur [Nutzer:innen mit diesen Mindest-App-Versionen anzusprechen]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

## Übersicht {#overview}

{% tabs %}
{% tab Campaign %}

Sie können wählen, wann Braze eine Karte erstellt – im Schritt **Zustellung** beim Anlegen einer neuen [Content-Card-Kampagne]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) mit geplanter Zustellung.

![Bereich „Content-Card-Steuerung“ beim Bearbeiten der Zustellung einer geplanten Content Card.]({% image_buster /assets/img_archive/card_creation.png %})

Folgende Optionen stehen zur Verfügung:

- **Beim Kampagnenstart:** Das bisherige Standardverhalten für Content Cards. Braze berechnet die Zielgruppen-Eignung und Personalisierung beim Start der Campaign, erstellt dann die Karte und speichert sie, bis die Nutzer:innen Ihre App öffnen.
- **Beim ersten Impression (empfohlen):** Wenn Nutzer:innen das nächste Mal Ihre App öffnen (eine neue [Session](https://www.braze.com/resources/articles/whats-an-app-session-anyway) starten), ermittelt Braze, für welche Content Cards sie berechtigt sind, setzt Personalisierungen wie Liquid oder Connected-Content um und erstellt dann die Karte. Diese Option liefert in der Regel eine bessere Performance.

Unabhängig von der gewählten Option beginnt der Countdown für das Ablaufdatum der Content Card beim Kampagnenstart.

{% endtab %}
{% tab Canvas %}

Sie können wählen, wann Braze eine Karte erstellt – im Tab **Messaging-Kanäle** eines Content-Card-[Nachrichtenschritts]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

![Bereich „Content-Card-Steuerung“ beim Bearbeiten der Zustellung einer geplanten Content Card.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Folgende Optionen stehen zur Verfügung:

- **Beim Schritteintritt:** Das bisherige Standardverhalten für Content Cards. Braze berechnet die Zielgruppen-Eignung, wenn Nutzer:innen den Canvas-Schritt betreten, erstellt dann die Karte und speichert sie, bis die Nutzer:innen Ihre App öffnen.
- **Beim ersten Impression (empfohlen):** Braze berechnet die Zielgruppen-Eignung, wenn Nutzer:innen den Canvas-Schritt betreten. Wenn die Nutzer:innen das nächste Mal Ihre App öffnen (eine neue [Session](https://www.braze.com/resources/articles/whats-an-app-session-anyway) starten), setzt Braze Personalisierungen wie Liquid oder Connected-Content um und erstellt dann die Karte. Diese Option liefert eine bessere Performance bei der Kartenzustellung und eine aktuellere Personalisierung.

Unabhängig von der gewählten Option beginnt der Countdown für das Ablaufdatum der Content Card, wenn Nutzer:innen den Canvas-Schritt betreten.

{% alert tip %}
Wenn Sie möchten, dass anonyme Nutzer:innen eine Content Card gleich in ihrer allerersten Session sehen, verwenden Sie eine Campaign anstelle eines Canvas. Denn wenn anonyme Nutzer:innen einen Canvas betreten, hat ihre Session bereits begonnen, sodass sie die Content Card erst erhalten, wenn sie eine neue Session starten.
{% endalert %}

### Entfernungsereignis {#removal-event}

Wählen Sie die Option, um Content Cards zu entfernen, wenn Nutzer:innen einen Kauf abschließen oder ein angepasstes Event ausführen. Um **Angepasstes Event ausführen** als Entfernungsereignis zu verwenden, wählen Sie Kontextvariablen oder angepasste Attribute für Vergleiche bei Eigenschafts-Filtern.

![Einstellungen für das Content-Card-Entfernungsereignis mit ausgewähltem „Angepasstes Event ausführen“ und Eigenschafts-Filtern unter Verwendung von Kontextvariablen oder angepassten Attributen.]({% image_buster /assets/img/content_card_removal_event.png %})

### Ablauf {#expiration}

In den Einstellungen für **Ablauf (Verweildauer im Feed)** können Sie **Dauer personalisieren** auswählen, um das Ablaufdatum der Content Card mithilfe von Kontextvariablen festzulegen.

![Ablaufeinstellungen mit „Dauer personalisieren“, konfiguriert mit einer Kontextvariable für den Content-Card-Ablauf.]({% image_buster /assets/img/content_card_personalize_duration.png %})

{% alert important %}
Content Cards haben eine maximale Gültigkeit von 30 Tagen, auch bei personalisierter Dauer mit Kontextvariablen. Jeder Wert über 30 Tage wird auf 30 Tage begrenzt. Weitere Informationen finden Sie unter [Kartenablauf]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-expiration).
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Bei beiden Optionen berechnet Braze nach der Kartenerstellung die Zielgruppen-Eignung und Personalisierung nicht erneut.
{% endalert %}

### Unterschiede zwischen Kartenerstellung beim Start bzw. Eintritt und beim ersten Impression {#differences}

Dieser Abschnitt beschreibt die wesentlichen Unterschiede zwischen der Kartenerstellung beim Kampagnenstart oder Schritteintritt und beim ersten Impression.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table aria-label="Unterschiede zwischen Kartenerstellung beim Start bzw. Eintritt und beim ersten Impression" class="tg">
  <caption>Unterschiede zwischen Kartenerstellung beim Start bzw. Eintritt und beim ersten Impression</caption>
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Beim Kampagnenstart / beim Canvas-Schritteintritt</th>
    <th class="tg-0pky">Beim ersten Impression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Wann verwenden</td>
    <td class="tg-0pky">Wenn Sie Inhalte zu einem bestimmten Zeitpunkt (dem Startzeitpunkt) festhalten müssen.</td>
    <td class="tg-0pky"><ul><li>Wenn Sie Karten neuen oder anonymen Nutzer:innen anzeigen möchten, die dem Segment nach dem Start beitreten könnten (<a href="#campaign_note">nur Campaigns*</a>).</li><li>Wenn Sie Personalisierung verwenden und die aktuellsten Inhalte auf der Karte verfügbar sein sollen.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Zielgruppe</td>
    <td class="tg-0pky">Braze wertet die Zielgruppen-Zugehörigkeit beim Versand der Campaign aus.<br><br>Neue oder anonyme Nutzer:innen werden nicht auf Eignung geprüft, wenn sie die Karte nach dem Kampagnenversand aufrufen möchten. Bei wiederkehrenden Campaigns erfolgt dies beim nächsten Wiederholungsintervall.</td>
    <td class="tg-0pky">Braze wertet die Zugehörigkeit aus, wenn Nutzer:innen das nächste Mal Ihre App öffnen (eine Session starten, <a href="#campaign_note">nur Campaigns*</a>).<br><br> Diese Einstellung erreicht eine größere Zielgruppe, da neue oder anonyme Nutzer:innen immer auf Eignung geprüft werden, wenn sie die Karte aufrufen möchten.<br><br>Darüber hinaus gelten Rate-Limits (Begrenzung der Anzahl der Personen, die die Karte erhalten) nicht, wenn die Option „Beim ersten Impression“ eingestellt ist.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalisierung</td>
    <td class="tg-0pky">Braze wertet Liquid, Connected-Content und Content Blocks zum Zeitpunkt des Kampagnenstarts oder beim Eintritt in den Canvas-Schritt aus. Bei wiederkehrenden Campaigns erfolgt dies beim nächsten Wiederholungsintervall.</td>
    <td class="tg-0pky">Braze wertet Liquid, Connected-Content und Content Blocks zum Zeitpunkt des ersten Impressions oder nach dem nächsten Wiederholungsintervall aus.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analytics</td>
  <td class="tg-0pky"><em>Gesendete Nachrichten</em> bezieht sich auf die Anzahl der Karten, die Braze erstellt und verfügbar gemacht hat. Es wird nicht gezählt, ob Nutzer:innen die Karte angesehen haben.</td>
  <td class="tg-0pky"><em>Gesendete Nachrichten</em> bezieht sich auf die Anzahl der Karten, die Braze nach einem Session-Start an Nutzer:innen sendet. In Canvas wird keine Karte gesendet, wenn Nutzer:innen den Schritt betreten, ohne eine Session zu starten – daher stimmt dieser Wert möglicherweise nicht mit der Anzahl der Nutzer:innen überein, die einen Schritt betreten.<br><br>Obwohl sich erreichbare Nutzer:innen und Impressionen nicht ändern, ist bei Kartenerstellung beim ersten Impression ein geringeres Sendevolumen (<em>Gesendete Nachrichten</em>) zu erwarten als beim Kampagnenstart oder Canvas-Schritteintritt.</td>
  </tr>
  <tr>
    <td class="leftHeader">Verarbeitungszeit</td>
  <td class="tg-0pky">Braze erstellt zum Startzeitpunkt Karten für alle berechtigten Nutzer:innen im Segment. Wählen Sie bei großen Zielgruppen <b>Beim ersten Impression</b>, damit Karten nach dem Start schneller verfügbar sind.</td>
  <td class="tg-0pky">Braze erstellt eine Karte beim ersten Versuch der Nutzer:innen, sie anzuzeigen. Die Anzeige kann daher beim ersten Impression 1–2 Sekunden dauern.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Dieses Szenario gilt nur für Campaigns, da die Canvas-Zielgruppe beim Canvas-Eintritt ausgewertet wird, nicht auf Schrittebene.</sup></p>

## Überlegungen {#considerations}

### Multichannel-Campaigns {#multichannel-campaigns}

Multichannel-Campaigns unterstützen keine Karten bei erster Impression, sodass alle Content Cards beim Start der Campaign gesendet werden.

### Canvas-Kontexteigenschaften verwenden {#using-canvas-context-properties}

Wenn Sie Content Cards mit [Canvas-Kontexteigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) personalisieren, verwenden Sie die `${...}`-Syntax (zum Beispiel {%raw%}`{{context.${property_name}}}`{%endraw%}). Punktnotation ohne diese Syntax (zum Beispiel {%raw%}`{{context.property_name}}`{%endraw%}) wird in Content Cards möglicherweise nicht korrekt aufgelöst, selbst wenn sie in anderen Kanälen wie Push und E-Mail funktioniert.

### Kartenerstellung nach dem Start ändern {#changing-card-creation-after-launch}

Braze empfiehlt, die Art der Kartenerstellung nach dem Start einer Campaign nicht mehr zu ändern. Aufgrund der Unterschiede bei der Berechnung der gesendeten Nachrichten zwischen den beiden Kartenerstellungstypen kann eine Änderung nach dem Start der Campaign die Genauigkeit Ihres Sendevolumens beeinträchtigen.

### Mögliche Verarbeitungszeit {#potential-processing-time}

Wählen Sie bei großen Zielgruppen die Option, Karten bei erster Impression zu erstellen, damit die Karten nach dem Start schnell verfügbar sind. Campaigns, die beim Sitzungsstart ausgelöst werden, können ebenfalls davon profitieren, auf die Erstellung bei erster Impression umzusteigen (verfügbar über geplante Zustellung), um die Performance zu verbessern.

Wenn Karten bei erster Impression erstellt werden, kann die Verarbeitung der Karten einige Sekunden dauern. Die Dauer dieser Verarbeitungszeit hängt von verschiedenen Faktoren ab, wie der Kartengröße und der Komplexität der Optionen für das Nachrichten-Templating. Zum Beispiel ist die Verarbeitungszeit für Karten, die Connected-Content verwenden, mindestens so lang wie die Antwortzeit des Connected-Content.

### Frühere SDK or Software-Development-Kit-Versionen {#previous-sdk-versions}

Wenn die App einer Nutzerin oder eines Nutzers eine frühere SDK or Software-Development-Kit-Version verwendet, erhält sie oder er trotzdem die von Ihnen gesendeten Content Cards. Allerdings dauert es länger, bis die Karten erscheinen, und sie werden möglicherweise erst bei der nächsten Content-Card-Synchronisierung angezeigt.