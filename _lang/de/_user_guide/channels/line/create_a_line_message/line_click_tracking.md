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

Sie können die Einstellungen für das LINE-Klick-Tracking im Tab **Einstellungen** verwalten, während Sie eine Nachricht verfassen. Wenn es aktiviert ist, werden URLs mit der Standard-Braze-Domain (`https://brz.ai`) oder der für die Abo-Gruppe angegebenen benutzerdefinierten Domain gekürzt und für die Nutzer:innen personalisiert.

Alle URLs, die mit `http://` oder `https://` beginnen, werden gekürzt. Sie können bis zu 25 URLs in einer Nachricht verwenden. Gekürzte URLs, die Liquid-Personalisierung enthalten (wie nutzerspezifisches Tracking oder UTM-Parameter), sind zwei Monate lang gültig.

## Klick-Tracking einrichten {#setting-up-click-tracking}

### Textnachrichten {#text-messages}

So richten Sie das Klick-Tracking für eine Textnachricht ein:

1. Ziehen Sie eine **Text**-Nachricht in den Editor und fügen Sie eine URL in das Textfeld ein.

![LINE-Nachrichten-Editor mit einer Textnachricht, die eine lange URL enthält: {{site.baseurl}}/user_guide/channels/line/create/]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2. Gehen Sie zum Tab **Einstellungen** und bestätigen Sie, dass **Click Tracking** aktiviert ist. Klick-Tracking ist standardmäßig für alle neuen Nachrichten aktiviert.

{% alert note %}
Sie können Vorschauen des gekürzten Links im Tab **Einstellungen** oder **Vorschau & Test** anzeigen. Der vollständige Link wird im Editor angezeigt, während Sie Ihre Nachricht erstellen.
{% endalert %}

![LINE-Nachrichten-Editor, Tab „Einstellungen“ mit aktiviertem „Click Tracking“ und einer Vorschau-Textnachricht mit gekürzter URL: https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Rich-Nachrichten {#rich-messages}

So richten Sie das Klick-Tracking für eine Rich-Nachricht ein:

1. Ziehen Sie eine **Rich message** in den Editor und wählen Sie ein Template aus.
2. Wählen Sie **URI** für das **On-click behavior** des entsprechenden tippbaren Bereichs.
3. Geben Sie eine URL in das Feld **Open URL** ein.

![LINE-Nachrichten-Editor mit einer Rich-Nachricht mit zwei tippbaren Bereichen, die jeweils eine URL haben.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4. Gehen Sie zum Tab **Einstellungen** und bestätigen Sie, dass **Click Tracking** aktiviert ist. Klick-Tracking ist standardmäßig für alle neuen Nachrichten aktiviert.

### Kartenbasierte Nachrichten {#card-based-messages}

So richten Sie das Klick-Tracking für eine kartenbasierte Nachricht ein:

1. Ziehen Sie eine **Card-based message** in den Editor.
2. Wählen Sie **URI** für das **On-click behavior** der entsprechenden Karten- oder Button-Bereiche.

![LINE-Nachrichten-Editor mit einer kartenbasierten Nachricht mit zwei Buttons, die jeweils eine URL haben.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3. Gehen Sie zum Tab **Einstellungen** und bestätigen Sie, dass **Click Tracking** aktiviert ist. Klick-Tracking ist standardmäßig für alle neuen Nachrichten aktiviert.

{% alert note %}
URLs in den Feldern **Title** oder **Description** werden nicht gekürzt, da diese Felder innerhalb von LINE nicht klickbar sind.
{% endalert %}

## Benutzerdefinierte Domains {#custom-domains}

LINE-Klick-Tracking ermöglicht es Ihnen, Ihre eigene Domain zu verwenden, um das Erscheinungsbild Ihrer gekürzten URLs zu personalisieren und so ein einheitliches Markenbild zu vermitteln. Weitere Informationen finden Sie unter [Benutzerdefinierte Domains]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains/).

## Liquid-Personalisierung in URLs {#liquid-personalization-in-urls}

Sie können Ihre URL direkt im Braze-Editor dynamisch erstellen, sodass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Nutzer:innen eindeutige Links senden können (z. B. Nutzer:innen zu ihrem abgebrochenen Warenkorb oder zu einem bestimmten Produkt weiterleiten, das wieder auf Lager ist).
URLs können durch die Verwendung aller unterstützten Liquid-Personalisierungs-Tags dynamisch generiert werden.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Sie können auch benutzerdefinierte Liquid-Variablen kürzen, wie im folgenden Beispiel gezeigt:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Durch Liquid-Variablen gerenderte URLs kürzen {#shorten-urls-rendered-by-liquid-variables}

Braze kürzt URLs, die durch Liquid gerendert werden, auch solche, die in API-Trigger-Eigenschaften enthalten sind. Wenn beispielsweise {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, wird diese URL vor dem Senden der LINE-Nachricht gekürzt und getrackt.

## Testen {#testing}

Bevor Sie Ihre Kampagne oder Ihren Canvas starten, empfiehlt es sich, Ihre Nachricht zunächst in der Vorschau anzuzeigen und zu testen. Gehen Sie dazu zum Tab **Test**, um eine LINE-Nachricht an Inhaltstestgruppen oder einzelne Nutzer:innen in der Vorschau anzuzeigen und zu senden.

Diese Vorschau wird mit der relevanten Personalisierung und der gekürzten URL aktualisiert.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine gekürzte URL generiert. Die tatsächliche gekürzte URL wird generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

## Berichte und Auswertung {#reporting}

Die LINE-Performance-Tabelle enthält die Spalte **Total Clicks**, die eine Anzahl der Klick-Ereignisse pro Variante und eine zugehörige Klickrate anzeigt. Weitere Details zu LINE-Metriken finden Sie unter [LINE-Nachrichten-Performance]({{site.baseurl}}/user_guide/channels/line/reporting/).

![Performance für einen LINE-Canvas-Schritt.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Klickdaten werden automatisch im Analytics-Dashboard angezeigt.

![LINE-Performance-Analytics-Dashboard.]({% image_buster /assets/img/line/line_performance.png %})

## Retargeting von Nutzer:innen {#retargeting-users}

Sie können Nutzer:innen, die auf eine URL in einer LINE-Nachricht geklickt haben, mit den folgenden Segmentierungsfiltern und Triggern erneut ansprechen:

- Aktionsbasierte Trigger
    - Mit Campaign interagieren
    - Mit Schritt interagieren

![Aktionsbasierter LINE-Zustellungstrigger.]({% image_buster /assets/img/line/line_action_based.png %})

- Segmentierungsfilter
    - Campaign angeklickt/geöffnet
    - Campaign oder Canvas mit Tag angeklickt/geöffnet
    - Schritt angeklickt/geöffnet

![Filtergruppe mit allen drei Segmentierungsfiltern: „Campaign angeklickt/geöffnet“, „Campaign oder Canvas mit Tag angeklickt/geöffnet“ und „Schritt angeklickt/geöffnet“.]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Häufig gestellte Fragen {#frequently-asked-questions}

### Sind die Links, die ich beim Testsenden erhalte, echte URLs? {#are-the-links-i-receive-when-test-sending-real-urls}

Ja, beim Testsenden werden echte URLs generiert. Die genaue URL, die in einer gestarteten Kampagne gesendet wird, kann sich jedoch von der im Testsenden gesendeten URL unterscheiden.

### Kann ich UTM-Parameter zu einer URL hinzufügen, bevor sie gekürzt wird? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Ja, sowohl statische als auch dynamische Parameter können hinzugefügt werden.

### Wie lange bleiben gekürzte URLs gültig? {#how-long-do-shortened-urls-remain-valid}

Personalisierte URLs sind ab dem Zeitpunkt der URL-Registrierung zwei Monate lang gültig.

### Muss das Braze SDK installiert sein, um URLs zu kürzen? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

Nein, Klick-Tracking funktioniert ohne jegliche SDK-Integration.

### Weiß ich, welche einzelnen Nutzer:innen auf eine URL klicken? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Ja. Wenn Klick-Tracking aktiviert ist, können Sie Nutzer:innen, die auf URLs geklickt haben, mithilfe der [LINE-Retargeting-Filter](#retargeting-users) erneut ansprechen.

### Funktioniert Klick-Tracking mit Deeplinks oder Universal Links? {#does-click-tracking-work-with-deep-links-or-universal-links}

Klick-Tracking funktioniert nicht mit Deeplinks. Sie können Universal Links von Anbietern wie Branch oder Appsflyer kürzen, aber Braze kann keine Probleme beheben, die dabei auftreten können (z. B. fehlerhafte Attribution oder fehlgeschlagene Weiterleitungen).

### Zählen Vorschauen in der LINE-App als Klicks? {#do-previews-on-the-line-app-count-as-clicks}

Nein, sie tragen nicht zur Klickrate für LINE-Nachrichten bei.