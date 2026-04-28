---
nav_title: Klick-Tracking
article_title: Klick-Tracking
page_order: 2
description: "Dieser Referenzartikel behandelt, wie Sie Klick-Tracking in Ihren WhatsApp-Nachrichten aktivieren, gekürzte Links testen, Ihre benutzerdefinierte Domain in getrackten Links verwenden und mehr."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Klick-Tracking {#click-tracking}

> Diese Seite behandelt, wie Sie Klick-Tracking in Ihren WhatsApp-Nachrichten aktivieren, gekürzte Links testen, Ihre benutzerdefinierte Domain in getrackten Links verwenden und mehr.

Mit Klick-Tracking können Sie messen, wenn jemand auf einen Link in Ihrer WhatsApp-Nachricht tippt. So erhalten Sie einen klaren Überblick darüber, welche Inhalte das Engagement fördern. Braze kürzt Ihre URLs, fügt im Hintergrund Tracking hinzu und protokolliert Klick-Ereignisse in Echtzeit.

Sie können Klick-Tracking sowohl in Antwortnachrichten als auch in Template-Nachrichten aktivieren. Es funktioniert mit Links in Buttons und im Textkörper und unterstützt personalisierte URLs sowie benutzerdefinierte Domains. Nach der Aktivierung sehen Sie Klickdaten in Ihren WhatsApp-Performance-Berichten und können Nutzer:innen basierend darauf segmentieren, wer auf was geklickt hat.

{% alert note %}
Klick-Tracking funktioniert nicht mit Deeplinks. Sie können universelle Links von Anbietern wie Branch oder Appsflyer kürzen, aber Braze kann keine Probleme beheben, die dabei auftreten können (z. B. Unterbrechung der Attribution oder Verursachung einer Weiterleitung).
{% endalert %}

## Funktionsweise {#how-it-works}

### Antwortnachrichten {#response-messages}

So richten Sie Klick-Tracking für Antwortnachrichten ein:
1. Erstellen Sie eine Antwortnachricht, die einen Call-to-Action-Button (CTA) mit einer Website-URL enthält.
2. Aktivieren Sie Klick-Tracking, indem Sie auf den dafür vorgesehenen Button in der Schnittstelle klicken.

Der Link wird auf die Braze-Domain oder die für die Abo-Gruppe angegebene benutzerdefinierte Domain gekürzt und für die Nutzer:innen personalisiert.

Alle statischen URLs, die mit `http://` oder `https://` beginnen, werden gekürzt. Gekürzte URLs, die Liquid-Personalisierung enthalten (z. B. Tracking auf Nutzer:innen-Ebene), sind zwei Monate lang gültig.

![WhatsApp-Nachrichten-Editor mit Textkörper und einem Button.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Template-Nachrichten {#template-messages}

Bei Template-Nachrichten muss die Basis-URL beim Erstellen des Templates korrekt eingereicht werden, um Klick-Tracking zu aktivieren.

#### 1. Schritt: Ein Klick-Tracking-fähiges Template in WhatsApp erstellen {#step-1-build-a-click-tracking-supported-template-in-whatsapp}

1. Erstellen Sie in Ihrem WhatsApp Manager eine Basis-URL, die entweder Ihre benutzerdefinierte Domain oder `brz.ai` ist.
2. Stellen Sie sicher, dass die im Template enthaltenen Links mit Klick-Tracking kompatibel sind.
3. Ändern Sie die Template-Variablen nicht, nachdem es als Campaign in Braze eingerichtet wurde; nachträgliche Änderungen können nicht übernommen werden.
4. Wählen Sie für CTA-Button-Links **Dynamic** und geben Sie dann die Basis-URL (`brz.ai` oder Ihre benutzerdefinierte Domain) an.<br><br>![Abschnitt zum Erstellen eines Call-to-Action.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. Entfernen Sie bei Links im Textkörper beim Schreiben des Templates in Ihrem WhatsApp Manager alle eingefügten Leerzeichen für Links im Textkörper, die Sie tracken möchten.<br><br>![Textfeld zur Eingabe des Textkörpers für den Call-to-Action.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### 2. Schritt: Ihr Template in Braze vervollständigen {#step-2-complete-your-template-in-braze}

Beim Verfassen erkennt Braze automatisch, welche Templates unterstützte URL-Domains haben, sowohl im Textkörper als auch für CTA-Buttons. Der Status wird unten im Template angezeigt.

![Abschnitt „Link-Status“ mit einem aktiven Status für Klick-Tracking.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Unterstützte Links:** Links, die mit der passenden Basis-URL eingereicht werden, haben Klick-Tracking aktiviert.
- **Teilweise unterstützte Links:** Wenn einige Links in einem Template als vollständige URLs eingereicht werden, wird Klick-Tracking auf diese Links **nicht** angewendet.
- **Nicht unterstützte Links:** Links ohne eine genehmigte Basis-URL haben **keine** Klick-Tracking-Funktionalität.

Die Ziel-URL muss für jeden Link angegeben werden, dessen Basis-URL entweder `brz.ai` oder Ihrer benutzerdefinierten Domain entspricht.

![Abschnitt „Buttons“ mit Feldern für einen Button-Namen, eine Website-URL und eine Klick-Tracking-URL.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% alert important %}
**Senden von Template-Nachrichten über die API**: WhatsApp-Klick-Tracking (mit `brz.ai` oder einer benutzerdefinierten Tracking-Domain und dem Feld **Click tracking URL** im Nachrichten-Editor) wird beim Senden von WhatsApp-Template-Nachrichten über den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) nicht unterstützt.

Wenn Sie eine Template-Nachricht über die API senden, können Sie CTA-URL-Variablen (mit `button_variables`) befüllen, aber Braze generiert im API-Anfrage-Flow keine Klick-Tracking-URL oder keinen Weiterleitungslink. Um Klick-Tracking zu nutzen, senden Sie das Template über das Braze-Dashboard oder über einen Braze-Campaign-Trigger.
{% endalert %}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## Liquid-Personalisierung in URLs {#liquid-personalization-in-urls}

Sie können Ihre URL direkt im Braze-Composer dynamisch zusammenstellen, sodass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Nutzer:innen eindeutige Links senden können (z. B. Nutzer:innen zu ihrem abgebrochenen Warenkorb oder zu einem bestimmten Produkt weiterleiten, das wieder auf Lager ist).
URLs können durch die Verwendung aller unterstützten Liquid-Personalisierungs-Tags dynamisch generiert werden.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Wir unterstützen auch das Kürzen von benutzerdefinierten Liquid-Variablen, wie in diesen Beispielen:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Von Liquid-Variablen gerenderte URLs kürzen {#shorten-urls-rendered-by-liquid-variables}

Braze kürzt URLs, die von Liquid gerendert werden, auch solche, die in API-Trigger-Eigenschaften enthalten sind. Wenn beispielsweise {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, wird diese URL vor dem Senden der WhatsApp-Nachricht gekürzt und getrackt.

## Testen {#testing}

Bevor Sie Ihre Campaign oder Ihren Canvas starten, empfiehlt es sich, Ihre Nachricht zunächst in der Vorschau anzuzeigen und zu testen. Gehen Sie dazu zum Tab **Test**, um eine WhatsApp-Nachricht an Inhaltstestgruppen oder einzelne Nutzer:innen in der Vorschau anzuzeigen und zu senden.

Diese Vorschau wird mit der relevanten Personalisierung und der gekürzten URL aktualisiert.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine gekürzte URL generiert. Die tatsächliche gekürzte URL wird generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

## Berichterstattung {#reporting}

Wenn Klick-Tracking aktiviert ist oder mit unterstützten Templates verwendet wird, enthält die WhatsApp-Performance-Tabelle die Spalte **Total Clicks**, die eine Anzahl der Klick-Ereignisse pro Variante und eine zugehörige Klickrate anzeigt. Weitere Details zu WhatsApp-Metriken finden Sie unter [WhatsApp-Nachrichten-Performance]({{site.baseurl}}/user_guide/channels/whatsapp/reporting/).

![WhatsApp-Nachrichten-Canvas-Schritt.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Klickdaten werden automatisch im Analytics-Dashboard angezeigt.

![WhatsApp-Nachrichten-Performance-Tabelle.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Retargeting von Nutzer:innen {#retargeting-users}

Sie können den Filter `Clicked/Opened Step` und die Interaktion `clicked tracked WhatsApp link` verwenden, um Nutzer:innen basierend auf ihren Interaktionen mit den Links zu segmentieren.

![Filtergruppe mit einem Filter für „clicked tracked WhatsApp link“.]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Weiß ich, welche einzelnen Nutzer:innen auf eine URL klicken? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Ja. Wenn Klick-Tracking aktiviert ist (oder basierend auf der Template-Konfiguration aktiviert wurde), können Sie Nutzer:innen, die auf URLs geklickt haben, mithilfe der WhatsApp-Retargeting-Filter oder der WhatsApp-Klick-Ereignisse (`users.messages.whatsapp.Click`) retargeten, die von Currents gesendet werden.

### Zählen Vorschauen auf dem WhatsApp-Gerät als Klicks? {#do-previews-on-the-whatsapp-device-count-as-clicks}

Nein, sie tragen nicht zur Klickrate für WhatsApp-Nachrichten bei.