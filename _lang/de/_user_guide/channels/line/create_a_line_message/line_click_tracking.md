---
nav_title: LINE-Klick-Tracking
article_title: LINE-Klick-Tracking
page_order: 2
description: "Diese Seite beschreibt, wie Sie das Klick-Tracking in Ihren LINE-Nachrichten aktivieren, gekürzte Links testen, Ihre benutzerdefinierte Domain in getrackten Links verwenden und mehr."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# LINE-Klick-Tracking {#line-click-tracking}

> Diese Seite beschreibt, wie Sie das Klick-Tracking in Ihren LINE-Nachrichten aktivieren, gekürzte Links testen, Ihre benutzerdefinierte Domain in getrackten Links verwenden und mehr.


Wenn das LINE-Klick-Tracking aktiviert ist, kürzt Braze Ihre URLs automatisch, fügt Tracking-Mechanismen hinzu und zeichnet Klicks in Echtzeit auf. Während LINE Ihnen aggregierte Klickdaten bietet, liefert Braze granulare Nutzer:inneninformationen, die zeitnah und umsetzbar sind. Diese Daten ermöglichen es Ihnen, gezieltere Segmentierungs- und Retargeting-Strategien zu erstellen, z. B. Nutzer:innen basierend auf dem Klickverhalten zu segmentieren und Nachrichten als Reaktion auf bestimmte Klicks zu triggern.

LINE-Klick-Tracking kann für Text-, Rich- und kartenbasierte Nachrichten verwendet werden. Es unterstützt Links innerhalb von Buttons und Image-Mapped-Bereichen, die eine URL als Klick-Aktion haben. Sie können URLs auch mit Liquid und benutzerdefinierten Domains personalisieren.

## Funktionsweise {#how-it-works}

Sie können die Einstellungen für das LINE-Klick-Tracking im Tab **Einstellungen** verwalten, während Sie eine Nachricht erstellen. Wenn diese Option aktiviert ist, werden URLs mithilfe der Standard-Braze-Domain (`https://brz.ai`) oder der für die Abo-Gruppe angegebenen benutzerdefinierten Domain gekürzt und für die Nutzer:innen personalisiert.

Alle URLs, die mit `http://` oder `https://` beginnen, werden gekürzt. Sie können bis zu 25 URLs in einer Nachricht verwenden. Gekürzte URLs, die Liquid-Personalisierung enthalten (z. B. Tracking auf Nutzerebene oder UTM-Parameter), sind zwei Monate lang gültig.

## Klick-Tracking einrichten {#setting-up-click-tracking}

### Textnachrichten {#text-messages}

So richten Sie Klick-Tracking für eine Textnachricht ein:

1. Ziehen Sie eine **Text**-Nachricht in den Editor und fügen Sie eine URL in das Textfeld ein.

![LINE-Nachrichten-Editor mit einer Textnachricht, die vor der Kürzung eine lange URL enthält.]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2. Gehen Sie zum Tab **Einstellungen** und bestätigen Sie, dass **Klick-Tracking** aktiviert ist. Klick-Tracking ist standardmäßig für alle neuen Nachrichten aktiviert.

{% alert note %}
Sie können eine Vorschau des gekürzten Links im Tab **Einstellungen** oder **Vorschau und Test** anzeigen. Der vollständige Link wird im Editor angezeigt, während Sie Ihre Nachricht erstellen.
{% endalert %}

![Tab „Einstellungen“ im LINE-Nachrichten-Editor mit aktiviertem „Klick-Tracking“ und einer Vorschau-Textnachricht mit gekürzter URL: https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Rich-Nachrichten {#rich-messages}

So richten Sie Klick-Tracking für eine Rich-Nachricht ein:

1. Ziehen Sie eine **Rich-Nachricht** in den Editor und wählen Sie ein Template aus.
2. Wählen Sie **URI** als **Klickverhalten** für den entsprechenden tippbaren Bereich.
3. Geben Sie eine URL in das Feld **URL öffnen** ein.

![LINE-Nachrichten-Editor mit einer Rich-Nachricht mit zwei tippbaren Bereichen, die jeweils eine URL enthalten.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4. Gehen Sie zum Tab **Einstellungen** und bestätigen Sie, dass **Klick-Tracking** aktiviert ist. Klick-Tracking ist standardmäßig für alle neuen Nachrichten aktiviert.

### Kartenbasierte Nachrichten {#card-based-messages}

So richten Sie Klick-Tracking für eine kartenbasierte Nachricht ein:

1. Ziehen Sie eine **Kartenbasierte Nachricht** in den Editor.
2. Wählen Sie **URI** als **Klickverhalten** für die entsprechenden Karten- oder Button-Bereiche.

![LINE-Nachrichten-Editor mit einer kartenbasierten Nachricht mit zwei Buttons, die jeweils eine URL enthalten.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3. Gehen Sie zum Tab **Einstellungen** und bestätigen Sie, dass **Klick-Tracking** aktiviert ist. Klick-Tracking ist standardmäßig für alle neuen Nachrichten aktiviert.

{% alert note %}
URLs in den Feldern **Titel** oder **Beschreibung** werden nicht gekürzt, da diese Felder in LINE nicht anklickbar sind.
{% endalert %}

## Angepasste Domains {#custom-domains}

LINE-Klick-Tracking ermöglicht es Ihnen, Ihre eigene Domain zu verwenden, um das Erscheinungsbild Ihrer gekürzten URLs zu personalisieren und so ein einheitliches Markenbild zu vermitteln. Weitere Informationen finden Sie unter [Angepasste Domains]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains).

## Liquid-Personalisierung in URLs {#liquid-personalization-in-urls}

Sie können Ihre URL direkt im Braze-Nachrichten-Editor dynamisch erstellen, sodass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Nutzer:innen eindeutige Links senden können (z. B. um Nutzer:innen zu ihrem verlassenen Warenkorb oder zu einem bestimmten Produkt weiterzuleiten, das wieder auf Lager ist).
Sie können URLs dynamisch generieren, indem Sie beliebige unterstützte Liquid-Personalisierungs-Tags verwenden.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Sie können auch angepasst definierte Liquid-Variablen kürzen, wie im folgenden Beispiel gezeigt:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## URLs kürzen, die durch Liquid-Variablen gerendert werden {#shorten-urls-rendered-by-liquid-variables}

Braze kürzt URLs, die durch Liquid gerendert werden, auch solche, die in API-Trigger-Eigenschaften enthalten sind. Wenn z. B. {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, kürzen und tracken wir diese URL, bevor die LINE-Nachricht gesendet wird.

## Testen {#testing}

Bevor Sie Ihre Campaign oder Ihren Canvas starten, sollten Sie Ihre Nachricht zunächst in der Vorschau anzeigen und testen. Gehen Sie dazu auf den Tab **Test**, um eine LINE-Nachricht in der Vorschau anzuzeigen und an Content-Testgruppen oder einzelne Nutzer:innen zu senden.

Diese Vorschau wird mit relevanter Personalisierung und der gekürzten URL aktualisiert.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine gekürzte URL generiert. Die tatsächliche gekürzte URL wird generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

## Reporting {#reporting}

Die LINE-Performance-Tabelle enthält die Spalte **Klicks insgesamt**, die eine Anzahl der Klick-Ereignisse pro Variante und eine zugehörige Klickrate anzeigt. Weitere Details zu LINE-Metriken finden Sie unter [LINE-Nachrichten-Performance]({{site.baseurl}}/user_guide/channels/line/reporting).

![Performance für einen LINE-Canvas-Schritt.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Klickdaten werden automatisch im Analytics-Dashboard angezeigt.

![LINE-Performance-Analytics-Dashboard.]({% image_buster /assets/img/line/line_performance.png %})

## Retargeting von Nutzer:innen {#retargeting-users}

Sie können Nutzer:innen, die auf eine URL in einer LINE-Nachricht geklickt haben, mit den folgenden Segmentierungsfiltern und Triggern erneut ansprechen:

- Aktionsbasierte Trigger
    - Mit Campaign interagieren
    - Mit Schritt interagieren

![Aktionsbasierter Zustellungs-Trigger für LINE.]({% image_buster /assets/img/line/line_action_based.png %})

- Segmentierungsfilter
    - Campaign angeklickt/geöffnet
    - Campaign oder Canvas mit Tag angeklickt/geöffnet
    - Schritt angeklickt/geöffnet

![Filtergruppe mit allen drei Segmentierungsfiltern: „Campaign angeklickt/geöffnet“, „Campaign oder Canvas mit Tag angeklickt/geöffnet“ und „Schritt angeklickt/geöffnet“.]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Häufig gestellte Fragen {#frequently-asked-questions}

### Sind die Links, die ich beim Testsenden erhalte, echte URLs? {#are-the-links-i-receive-when-test-sending-real-urls}

Ja, beim Testsenden werden echte URLs generiert. Die genaue URL, die in einer gestarteten Campaign gesendet wird, kann sich jedoch von der in einem Testsenden gesendeten unterscheiden.

### Kann ich UTM-Parameter zu einer URL hinzufügen, bevor sie gekürzt wird? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Ja, es können sowohl statische als auch dynamische Parameter hinzugefügt werden.

### Wie lange bleiben gekürzte URLs gültig? {#how-long-do-shortened-urls-remain-valid}

Personalisierte URLs sind ab dem Zeitpunkt der URL-Registrierung zwei Monate lang gültig.

### Muss das Braze SDK installiert sein, um URLs zu kürzen? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

Nein, das Klick-Tracking funktioniert ohne jegliche SDK-Integration.

### Kann ich sehen, welche einzelnen Nutzer:innen auf eine URL klicken? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Ja. Wenn das Klick-Tracking aktiviert ist, können Sie Nutzer:innen, die auf URLs geklickt haben, mithilfe der [LINE-Retargeting-Filter](#retargeting-users) erneut ansprechen.

### Funktioniert das Klick-Tracking mit Deeplinks oder Universal Links? {#does-click-tracking-work-with-deep-links-or-universal-links}

Das Klick-Tracking funktioniert nicht mit Deeplinks. Sie können Universal Links von Anbietern wie Branch oder Appsflyer kürzen, aber Braze kann bei Problemen, die dabei auftreten können (z. B. fehlerhaftes Attribution-Tracking oder fehlgeschlagene Weiterleitungen), keine Unterstützung bieten.

### Zählen Vorschauen in der LINE-App als Klicks? {#do-previews-on-the-line-app-count-as-clicks}

Nein, sie tragen nicht zur Klickrate für LINE-Nachrichten bei.