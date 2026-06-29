---
nav_title: KakaoTalk-Klick-Tracking
article_title: KakaoTalk-Klick-Tracking
page_order: 3
description: "Diese Seite beschreibt, wie Sie das Klick-Tracking in Ihren KakaoTalk-Nachrichten aktivieren, gekürzte Links testen, Ihre benutzerdefinierte Domain in getrackten Links verwenden und mehr."
page_type: reference
alias: /kakaotalk_click_tracking/
channel:
 - KakaoTalk
---

# KakaoTalk-Klick-Tracking {#kakaotalk-click-tracking}

> Diese Seite beschreibt, wie Sie das Klick-Tracking in Ihren KakaoTalk-Nachrichten aktivieren, gekürzte Links testen, Ihre benutzerdefinierte Domain in getrackten Links verwenden und mehr.

Wenn das KakaoTalk-Klick-Tracking aktiviert ist, kürzt Braze Ihre URLs automatisch, fügt Tracking-Mechanismen hinzu und zeichnet Klicks in Echtzeit auf. Diese Daten ermöglichen es Ihnen, gezieltere Segmentierungs- und Retargeting-Strategien zu erstellen, z. B. Nutzer:innen basierend auf dem Klickverhalten zu segmentieren und Nachrichten als Reaktion auf bestimmte Klicks zu triggern.

KakaoTalk-Klick-Tracking kann für Text-, Bild- und Listenelementnachrichten verwendet werden. Es unterstützt Links innerhalb von Buttons und Bild-Klick-Aktionen. Sie können URLs auch mit Liquid und benutzerdefinierten Domains personalisieren.

## Funktionsweise {#how-it-works}

Sie können die Einstellungen für das KakaoTalk-Klick-Tracking im Abschnitt **Link options** des Editors verwalten. Wenn es aktiviert ist, werden URLs mit der Standard-Braze-Domain (`https://brz.ai`) oder der für die Abo-Gruppe angegebenen benutzerdefinierten Domain gekürzt und für die Nutzer:innen personalisiert.

Alle URLs, die mit `http://` oder `https://` beginnen, werden gekürzt. Sie können bis zu 25 URLs in einer Nachricht verwenden. Gekürzte URLs, die Liquid-Personalisierung enthalten (z. B. Tracking auf Nutzer:innenebene oder UTM-Parameter), sind zwei Monate lang gültig.

## Klick-Tracking einrichten {#set-up-click-tracking}

### Textnachrichten {#text-messages}

So richten Sie das Klick-Tracking für eine Textnachricht ein:

1. Verfassen Sie eine **Text**-Nachricht und fügen Sie eine URL in das Textfeld oder den Button ein.
2. Bestätigen Sie im Abschnitt **Link options** des Editors, dass **Click Tracking** aktiviert ist. Das Klick-Tracking ist standardmäßig für alle neuen Nachrichten aktiviert.

![KakaoTalk-Textnachrichten-Editor mit dem Abschnitt „Link options“ und aktiviertem „Click Tracking“.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

### Bildnachrichten {#image-messages}

So richten Sie das Klick-Tracking für eine Bildnachricht ein:

1. Verfassen Sie eine **Image**-Nachricht und stellen Sie das Klickverhalten so ein, dass eine URL geöffnet wird.
2. Geben Sie eine URL in das URL-Feld ein.
3. Bestätigen Sie im Abschnitt **Link options** des Editors, dass **Click Tracking** aktiviert ist.

### Listenelementnachrichten {#list-item-messages}

So richten Sie das Klick-Tracking für eine Listenelementnachricht ein:

1. Verfassen Sie eine **List item**-Nachricht und fügen Sie eine URL in das Feld **Website URL** für ein beliebiges Element ein.
2. Bestätigen Sie im Abschnitt **Link options** des Editors, dass **Click Tracking** aktiviert ist.

## Benutzerdefinierte Domains {#custom-domains}

Das KakaoTalk-Klick-Tracking ermöglicht es Ihnen, Ihre eigene Domain zu verwenden, um das Erscheinungsbild Ihrer gekürzten URLs zu personalisieren und so ein einheitliches Markenbild zu vermitteln. Weitere Informationen finden Sie unter [Benutzerdefinierte Domains]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains).

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

Braze kürzt URLs, die von Liquid gerendert werden, einschließlich solcher, die in API-Trigger-Eigenschaften enthalten sind. Wenn beispielsweise {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, wird Braze diese URL kürzen und tracken, bevor die KakaoTalk-Nachricht gesendet wird.

## Testen {#testing}

Bevor Sie Ihre Kampagne oder Ihren Canvas starten, empfiehlt es sich, Ihre Nachricht zunächst in der Vorschau anzuzeigen und zu testen. Gehen Sie dazu zum Tab **Test**, um eine KakaoTalk-Nachricht in der Vorschau anzuzeigen und an Inhaltstestgruppen oder einzelne Nutzer:innen zu senden.

Die Vorschau wird mit der relevanten Personalisierung und der gekürzten URL aktualisiert.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine gekürzte URL generiert. Die tatsächliche gekürzte URL wird generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

## Reporting {#reporting}

Die KakaoTalk-Performance-Tabelle enthält die Spalte **Total Clicks**, die eine Anzahl der Klick-Ereignisse pro Variante und eine zugehörige Klickrate anzeigt. Weitere Details zu KakaoTalk-Metriken finden Sie unter [KakaoTalk-Reporting]({{site.baseurl}}/kakaotalk_reporting).

Klickdaten werden automatisch im Analytics-Dashboard angezeigt.

## Nutzer:innen retargeten {#retarget-users}

Sie können Nutzer:innen, die auf eine URL in einer KakaoTalk-Nachricht geklickt haben, mit den folgenden Segmentierungsfiltern und Triggern retargeten:

- Aktionsbasierte Trigger
    - Mit Campaign interagiert
    - Mit Schritt interagiert

- Segmentierungsfilter
    - Campaign angeklickt/geöffnet
    - Campaign oder Canvas mit Tag angeklickt/geöffnet
    - Schritt angeklickt/geöffnet

## Häufig gestellte Fragen {#frequently-asked-questions}

### Sind die Links, die ich beim Testsenden erhalte, echte URLs? {#are-the-links-i-receive-when-test-sending-real-urls}

Ja, beim Testsenden werden echte URLs generiert. Die genaue URL, die in einer gestarteten Kampagne gesendet wird, kann sich jedoch von der im Testsenden gesendeten URL unterscheiden.

### Kann ich UTM-Parameter zu einer URL hinzufügen, bevor sie gekürzt wird? {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

Ja, sowohl statische als auch dynamische Parameter können hinzugefügt werden.

### Wie lange bleiben gekürzte URLs gültig? {#how-long-do-shortened-urls-remain-valid}

Personalisierte URLs sind zwei Monate ab dem Zeitpunkt der URL-Registrierung gültig.

### Muss das Braze SDK installiert sein, um URLs zu kürzen? {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

Nein, das Klick-Tracking funktioniert ohne jegliche SDK-Integration.

### Weiß ich, welche einzelnen Nutzer:innen auf eine URL klicken? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Ja. Wenn das Klick-Tracking aktiviert ist, können Sie Nutzer:innen, die auf URLs geklickt haben, mithilfe der [KakaoTalk-Retargeting-Filter](#retargeting-users) retargeten.

### Funktioniert das Klick-Tracking mit Deeplinks oder Universal Links? {#does-click-tracking-work-with-deep-links-or-universal-links}

Das Klick-Tracking gilt für Web-URLs. Für Deeplinks können Sie einen Deeplink direkt als Klick-Aktionstyp für Buttons in KakaoTalk festlegen – diese durchlaufen keine URL-Kürzung und kein Klick-Tracking. Wenn Sie Universal Links von Anbietern wie Branch oder Appsflyer verwenden möchten, können diese gekürzt werden, aber Braze kann keine Probleme beheben, die dabei auftreten können (z. B. fehlerhafte Attribution oder fehlgeschlagene Weiterleitungen).