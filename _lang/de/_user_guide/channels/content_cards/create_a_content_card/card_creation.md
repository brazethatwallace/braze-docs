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

Um dieses Feature nutzen zu können, müssen Sie mindestens auf die folgenden SDK-Versionen upgraden:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Nach dem SDK-Upgrade müssen Ihre mobilen Nutzer:innen ihre App aktualisieren. Sie können Ihre Kampagnen- oder Canvas-Zielgruppe so filtern, dass nur [Nutzer:innen mit diesen Mindest-App-Versionen angesprochen werden]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

## Übersicht {#overview}

{% tabs %}
{% tab Campaign %}

Sie können festlegen, wann Braze eine Karte erstellt – im Schritt **Zustellung** beim Erstellen einer neuen [Content-Card-Kampagne]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) mit geplanter Zustellung.

![Abschnitt „Content-Card-Steuerung“ beim Bearbeiten der Zustellung einer geplanten Content-Card.]({% image_buster /assets/img_archive/card_creation.png %})

Die folgenden Optionen stehen zur Verfügung:

- **Beim Kampagnenstart:** Das bisherige Standardverhalten für Content Cards. Braze ermittelt Zielgruppeneignung und Personalisierung beim Start der Kampagne, erstellt dann die Karte und speichert sie, bis die Nutzer:innen Ihre App öffnen.
- **Bei der ersten Impression (empfohlen):** Wenn die Nutzer:innen das nächste Mal Ihre App öffnen (eine neue [Sitzung](https://www.braze.com/resources/articles/whats-an-app-session-anyway) starten), bestimmt Braze, für welche Content Cards sie berechtigt sind, wendet Personalisierungen wie Liquid oder Connected-Content an und erstellt dann die Karte. Diese Option liefert in der Regel eine bessere Performance.

Unabhängig von der gewählten Option beginnt der Countdown für das Ablaufdatum der Content-Card, wenn die Kampagne gestartet wird.

{% endtab %}
{% tab Canvas %}

Sie können festlegen, wann Braze eine Karte erstellt – im Tab **Messaging-Kanäle** eines Content-Card-[Nachrichtenschritts]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).

![Abschnitt „Content-Card-Steuerung“ beim Bearbeiten der Zustellung einer geplanten Content-Card.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Die folgenden Optionen stehen zur Verfügung:

- **Beim Schritt-Eintritt:** Das bisherige Standardverhalten für Content Cards. Braze ermittelt die Zielgruppeneignung, wenn die Nutzer:innen den Canvas-Schritt betreten, erstellt dann die Karte und speichert sie, bis die Nutzer:innen Ihre App öffnen.
- **Bei der ersten Impression (empfohlen):** Braze ermittelt die Zielgruppeneignung, wenn die Nutzer:innen den Canvas-Schritt betreten. Wenn die Nutzer:innen das nächste Mal Ihre App öffnen (eine neue [Sitzung](https://www.braze.com/resources/articles/whats-an-app-session-anyway) starten), wendet Braze Personalisierungen wie Liquid oder Connected-Content an und erstellt dann die Karte. Diese Option liefert eine bessere Performance bei der Kartenzustellung und aktuellere Personalisierung.

Unabhängig von der gewählten Option beginnt der Countdown für das Ablaufdatum der Content-Card, wenn die Nutzer:innen den Canvas-Schritt betreten.

{% alert tip %}
Wenn Sie möchten, dass anonyme Nutzer:innen eine Content-Card in ihrer allerersten Sitzung sehen, verwenden Sie eine Kampagne anstelle eines Canvas. Der Grund: Wenn anonyme Nutzer:innen einen Canvas betreten, hat ihre Sitzung bereits begonnen, sodass sie die Content-Card erst erhalten, wenn sie eine neue Sitzung starten.
{% endalert %}

### Entfernungs-Event {#removal-event}

Wählen Sie die Option, Content Cards zu entfernen, wenn Nutzer:innen einen Kauf abschließen oder ein angepasstes Event ausführen. Um **Angepasstes Event ausführen** als Entfernungs-Event zu verwenden, wählen Sie Kontextvariablen oder angepasste Attribute für Vergleiche bei der Verwendung von Eigenschaftsfiltern.

![Einstellungen für das Content-Card-Entfernungs-Event mit ausgewähltem „Angepasstes Event ausführen“ und Eigenschaftsfiltern mit Kontextvariablen oder angepassten Attributen.]({% image_buster /assets/img/content_card_removal_event.png %})

### Ablauf {#expiration}

In den Einstellungen **Ablauf (Verweildauer im Feed)** können Sie **Dauer personalisieren** auswählen, um den Ablauf der Content-Card mithilfe von Kontextvariablen festzulegen.

![Ablaufeinstellungen mit „Dauer personalisieren“, konfiguriert mit einer Kontextvariable für den Content-Card-Ablauf.]({% image_buster /assets/img/content_card_personalize_duration.png %})

{% alert important %}
Content Cards haben eine maximale Ablaufzeit von 30 Tagen, auch bei Verwendung personalisierter Dauer mit Kontextvariablen. Jeder Wert über 30 Tage wird auf 30 Tage begrenzt. Weitere Informationen finden Sie unter [Kartenablauf]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#card-expiration).
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Bei beiden Optionen berechnet Braze nach der Erstellung einer Karte die Zielgruppeneignung oder Personalisierung nicht erneut.
{% endalert %}

### Unterschiede zwischen der Kartenerstellung beim Start oder Eintritt und bei der ersten Impression {#differences}

Dieser Abschnitt beschreibt die wesentlichen Unterschiede zwischen der Kartenerstellung beim Kampagnenstart oder Schritt-Eintritt und bei der ersten Impression.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table aria-label="Unterschiede zwischen der Kartenerstellung beim Start oder Eintritt und bei der ersten Impression" class="tg">
  <caption>Unterschiede zwischen der Kartenerstellung beim Start oder Eintritt und bei der ersten Impression</caption>
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Beim Kampagnenstart / Beim Canvas-Schritt-Eintritt</th>
    <th class="tg-0pky">Bei der ersten Impression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Wann verwenden</td>
    <td class="tg-0pky">Wenn der Inhalt zu einem bestimmten Zeitpunkt (dem Startzeitpunkt) festgehalten werden soll.</td>
    <td class="tg-0pky"><ul><li>Wenn Sie Karten neuen oder anonymen Nutzer:innen anzeigen möchten, die dem Segment nach dem Start beitreten könnten (<a href="#campaign_note">nur Campaigns*</a>).</li><li>Wenn Sie Personalisierung verwenden und die aktuellsten Inhalte auf der Karte verfügbar sein sollen.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Zielgruppe</td>
    <td class="tg-0pky">Braze wertet die Zielgruppenzugehörigkeit aus, wenn die Kampagne gesendet wird.<br><br>Neue oder anonyme Nutzer:innen werden nicht auf Berechtigung geprüft, wenn sie versuchen, die Karte nach dem Kampagnenversand anzuzeigen. Bei wiederkehrenden Kampagnen erfolgt dies beim nächsten Wiederholungsintervall.</td>
    <td class="tg-0pky">Braze wertet die Zugehörigkeit aus, wenn die Nutzer:innen das nächste Mal Ihre App öffnen (eine Sitzung starten, <a href="#campaign_note">nur Campaigns*</a>).<br><br>Diese Einstellung erreicht eine größere Zielgruppe, da neue oder anonyme Nutzer:innen immer auf Berechtigung geprüft werden, wenn sie versuchen, die Karte anzuzeigen.<br><br>Zusätzlich gilt: Rate-Limiting (Begrenzung der Anzahl der Personen, die die Karte erhalten) ist bei der Einstellung „Bei der ersten Impression“ nicht anwendbar.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personalisierung</td>
    <td class="tg-0pky">Braze wertet Liquid, Connected-Content und Content Blocks zum Zeitpunkt des Kampagnenstarts oder wenn Nutzer:innen den Canvas-Schritt betreten aus. Bei wiederkehrenden Kampagnen erfolgt dies beim nächsten Wiederholungsintervall.</td>
    <td class="tg-0pky">Braze wertet Liquid, Connected-Content und Content Blocks zum Zeitpunkt der ersten Impression oder nach dem nächsten Wiederholungsintervall aus.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analytics</td>
  <td class="tg-0pky"><em>Gesendete Nachrichten</em> bezieht sich auf die Anzahl der Karten, die Braze erstellt und verfügbar gemacht hat. Dies zählt nicht, ob Nutzer:innen die Karte angesehen haben.</td>
  <td class="tg-0pky"><em>Gesendete Nachrichten</em> bezieht sich auf die Anzahl der Karten, die Braze nach einem Sitzungsstart an Nutzer:innen sendet. In Canvas sendet Braze keine Karte, wenn Nutzer:innen den Schritt betreten, ohne eine Sitzung zu starten – daher stimmt diese Metrik möglicherweise nicht mit der Anzahl der Nutzer:innen überein, die einen Schritt betreten.<br><br>Während erreichbare Nutzer:innen und Impressionen sich nicht ändern, ist bei der Kartenerstellung bei der ersten Impression ein geringeres Sendevolumen (<em>Gesendete Nachrichten</em>) zu erwarten als beim Kampagnenstart oder Canvas-Schritt-Eintritt.</td>
  </tr>
  <tr>
    <td class="leftHeader">Verarbeitungszeit</td>
  <td class="tg-0pky">Braze erstellt Karten für alle berechtigten Nutzer:innen im Segment zum Startzeitpunkt. Wählen Sie bei großen Zielgruppen <b>Bei der ersten Impression</b>, damit Karten nach dem Start schneller verfügbar sind.</td>
  <td class="tg-0pky">Braze erstellt eine Karte, wenn Nutzer:innen zum ersten Mal versuchen, sie anzuzeigen, sodass die Anzeige bei der ersten Impression 1–2 Sekunden dauern kann.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Dieses Szenario gilt nur für Campaigns, da die Canvas-Zielgruppe beim Canvas-Eintritt ausgewertet wird, nicht auf Schrittebene.</sup></p>

## Hinweise {#considerations}

### Mehrkanalige Kampagnen {#multichannel-campaigns}

Mehrkanalige Kampagnen unterstützen keine Karten bei der ersten Impression, sodass alle Content Cards beim Kampagnenstart gesendet werden.

### Verwendung von Canvas-Kontexteigenschaften {#using-canvas-context-properties}

Wenn Sie Content Cards mit [Canvas-Kontexteigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) personalisieren, verwenden Sie die `${...}`-Syntax (zum Beispiel {%raw%}`{{context.${property_name}}}`{%endraw%}). Punktnotation ohne diese Syntax (zum Beispiel {%raw%}`{{context.property_name}}`{%endraw%}) wird in Content Cards möglicherweise nicht korrekt aufgelöst, auch wenn sie in anderen Kanälen wie Push und E-Mail funktioniert.

### Kartenerstellung nach dem Start ändern {#changing-card-creation-after-launch}

Braze empfiehlt, die Art der Kartenerstellung nach dem Start einer Kampagne nicht mehr zu ändern. Aufgrund der Unterschiede bei der Berechnung von „Gesendete Nachrichten“ zwischen den beiden Kartenerstellungstypen kann eine Änderung nach dem Kampagnenstart die Genauigkeit Ihres Sendevolumens beeinträchtigen.

### Mögliche Verarbeitungszeit {#potential-processing-time}

Wählen Sie bei großen Zielgruppen die Option zur Kartenerstellung bei der ersten Impression, damit Karten nach dem Start schnell verfügbar sind. Kampagnen, die beim Sitzungsstart getriggert werden, können ebenfalls von der Umstellung auf die Erstellung bei der ersten Impression profitieren (verfügbar über geplante Zustellung), um die Performance zu verbessern.

Wenn Karten bei der ersten Impression erstellt werden, kann die Verarbeitung einige Sekunden dauern. Die Dauer dieser Verarbeitungszeit hängt von verschiedenen Faktoren ab, wie der Kartengröße und der Komplexität der Nachrichten-Template-Optionen. Beispielsweise ist die Verarbeitungszeit für Karten mit Connected-Content mindestens so lang wie die Antwortzeit des Connected-Content.

### Frühere SDK-Versionen {#previous-sdk-versions}

Wenn die App von Nutzer:innen eine frühere SDK-Version verwendet, erhalten sie weiterhin die von Ihnen gesendeten Content Cards. Allerdings dauert es länger, bis die Karten erscheinen, und sie werden möglicherweise erst bei der nächsten Content-Card-Synchronisierung angezeigt.