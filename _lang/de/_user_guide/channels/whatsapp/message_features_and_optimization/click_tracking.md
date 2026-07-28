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
2. Aktivieren Sie Klick-Tracking, indem Sie auf den dafür vorgesehenen Button in der Oberfläche klicken.

Der Link wird auf die Braze-Domain oder die für die Abo-Gruppe angegebene benutzerdefinierte Domain gekürzt und für die Nutzer:innen personalisiert.

Alle statischen URLs, die mit `http://` oder `https://` beginnen, werden gekürzt. Gekürzte URLs, die Liquid-Personalisierung enthalten (z. B. Tracking auf Nutzer:innen-Ebene), sind zwei Monate lang gültig.

![WhatsApp-Nachrichten-Editor mit Textkörper und einem Button.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Template-Nachrichten {#template-messages}

Wir empfehlen, Klick-Tracking für Template-Nachrichten über den **WhatsApp Template Builder** in Braze zu aktivieren. Diese Aktivierungsmethode übernimmt automatisch die URL-Formatierungsanforderungen, sodass Sie nichts manuell im WhatsApp Business Manager konfigurieren müssen.

Wenn Sie Templates stattdessen direkt im WhatsApp Business Manager erstellen, lesen Sie [Klick-Tracking über den WhatsApp Business Manager konfigurieren](#configuring-click-tracking-from-whatsapp-business-manager).

#### Template Builder verwenden {#use-the-template-builder}

Beim Erstellen eines Templates im Template Builder wird Klick-Tracking im Tab **Settings** konfiguriert.

##### Schritt 1: Klick-Tracking aktivieren {#step-1-enable-click-tracking}

Gehen Sie im Template Builder zum Tab **Settings**. Aktivieren Sie unter **Link options** das Kontrollkästchen **Click tracking**. Wenn aktiviert, werden alle Links in Ihrem Template (sowohl im Nachrichtentext als auch in CTA-Website-Buttons) gekürzt und getrackt.

![Tab „Settings“ im Template Builder mit dem Abschnitt „Link options“ und aktiviertem Kontrollkästchen „Click tracking“ sowie einem Dropdown für benutzerdefinierte Domains.]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_settings.png %})

##### Schritt 2: Benutzerdefinierte Domain auswählen (optional) {#step-2-select-a-custom-domain-optional}

Wählen Sie unter **Custom domain** die Domain aus, die Sie für gekürzte Links verwenden möchten. Das Dropdown zeigt alle benutzerdefinierten Tracking-Domains an, die für Ihren Workspace konfiguriert sind. Wenn Sie keine auswählen, verwendet Braze die Standard-Domain `brz.ai`.

Um Domains hinzuzufügen oder zu ändern, wählen Sie **Subscription Group Management**.

{% alert important %}
Nachdem ein Template zur Genehmigung an Meta übermittelt wurde, kann die Tracking-Domain nicht mehr geändert werden. Vergewissern Sie sich, dass Sie die richtige Domain ausgewählt haben, bevor Sie das Template einreichen.
{% endalert %}

##### Schritt 3: Ziel-URLs hinzufügen {#step-3-add-your-destination-urls}

Gehen Sie zurück zum Tab **Compose** und fügen Sie Ihren Nachrichteninhalt hinzu.

- **Für CTA-Website-Buttons:** Geben Sie die Ziel-URL im Feld **Click tracking URL** ein. Braze speichert Ihre Ziel-URL und formatiert die Website-URL des Buttons automatisch mit der Tracking-Domain und einem Variablen-Platzhalter {% raw %}(z. B. `https://brz.ai/{{1}}`){% endraw %}. Dieser Platzhalter wird an Meta übermittelt. Zum Sendezeitpunkt generiert Braze die vollständige getrackte URL für jede:n Nutzer:in und befüllt die Variable.
- **Für Links im Textkörper:** Geben Sie URLs direkt im Textkörper ein.

Sie können das Format der getrackten URL für jeden Button direkt im Feld **Website URL** in der Vorschau anzeigen (z. B. `https://brz.ai/XXXXXXXX`).

![Abschnitt „Call to Action buttons“ mit einem „Visit website“-Button, dessen Website-URL im getrackten Format vorausgefüllt ist, und einem Feld für die Click tracking URL für das Ziel.]({% image_buster /assets/img/whatsapp/click_tracking/template_builder_compose.png %}){: style="max-width:70%;"}

##### Ziel-URLs nach der Einreichung aktualisieren {#update-destination-urls-after-submission}

Nachdem ein Template an Meta übermittelt wurde, ist die Tracking-Domain gesperrt, aber die Ziel-URL kann jederzeit bearbeitet werden. Um zu ändern, wohin ein Link verweist, bearbeiten Sie das Feld **Click tracking URL** für diesen Button. Das Format der getrackten URL bleibt gleich; Braze leitet Nutzer:innen zum Sendezeitpunkt an das neue Ziel weiter.

#### Klick-Tracking über den WhatsApp Business Manager konfigurieren {#configuring-click-tracking-from-whatsapp-business-manager}

Wenn Sie Templates im WhatsApp Business Manager statt im Template Builder erstellen, befolgen Sie diese Schritte, damit Klick-Tracking korrekt funktioniert, wenn das Template in Braze verwendet wird.

##### Schritt 1: Ein Klick-Tracking-fähiges Template im WhatsApp Business Manager erstellen {#step-1-build-a-click-tracking-supported-template-in-whatsapp-business-manager}

1. Erstellen Sie in Ihrem WhatsApp Business Manager eine Basis-URL, die entweder Ihre benutzerdefinierte Domain oder `brz.ai` ist.
2. Stellen Sie sicher, dass die im Template enthaltenen Links mit Klick-Tracking kompatibel sind.
3. Ändern Sie die Template-Variablen nicht, nachdem es als Campaign in Braze eingerichtet wurde; nachträgliche Änderungen können nicht übernommen werden.
4. Wählen Sie für CTA-Button-Links **Dynamic** und geben Sie dann die Basis-URL (`brz.ai` oder Ihre benutzerdefinierte Domain) an.

![Abschnitt zum Erstellen eines Call-to-Action.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %}){: style="max-width:70%;"}

{: start="5"}
5. Entfernen Sie bei Links im Textkörper beim Schreiben des Templates in Ihrem WhatsApp Business Manager alle eingefügten Leerzeichen für Links im Textkörper, die Sie tracken möchten.

![Textfeld zur Eingabe des Textkörpers für den Call-to-Action.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %}){: style="max-width:70%;"}

##### Schritt 2: Ihr Template in Braze vervollständigen {#step-2-complete-your-template-in-braze}

Beim Verfassen erkennt Braze automatisch, welche Templates unterstützte URL-Domains haben, sowohl im Textkörper als auch für CTA-Buttons. Der Status wird unten im Template angezeigt.

![Abschnitt „Link Status“ mit einem aktiven Status für Klick-Tracking.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Unterstützte Links:** Links, die mit der passenden Basis-URL eingereicht werden, haben Klick-Tracking aktiviert.
- **Teilweise unterstützte Links:** Wenn einige Links in einem Template als vollständige URLs eingereicht werden, wird Klick-Tracking auf diese Links **nicht** angewendet.
- **Nicht unterstützte Links:** Links ohne eine genehmigte Basis-URL haben **keine** Klick-Tracking-Funktionalität.

Die Ziel-URL muss für jeden Link angegeben werden, dessen Basis-URL entweder `brz.ai` oder Ihrer benutzerdefinierten Domain entspricht.

![Abschnitt „Buttons“ mit Feldern für einen Button-Namen, eine Website-URL und eine Klick-Tracking-URL.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% alert important %}
**Senden von Template-Nachrichten über die API**: WhatsApp-Klick-Tracking (mit `brz.ai` oder einer benutzerdefinierten Tracking-Domain und dem Feld **Click tracking URL** im Nachrichten-Editor) wird beim Senden von WhatsApp-Template-Nachrichten über den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) nicht unterstützt.

Wenn Sie eine Template-Nachricht über die API senden, können Sie CTA-URL-Variablen (mit `button_variables`) befüllen, aber Braze generiert im API-Anfrage-Flow keine Klick-Tracking-URL und keinen Weiterleitungslink. Um Klick-Tracking zu nutzen, senden Sie das Template über das Braze-Dashboard oder über einen Braze-Campaign-Trigger.
{% endalert %}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## Liquid-Personalisierung in URLs {#liquid-personalization-in-urls}

Sie können Ihre URL direkt im Braze-Composer dynamisch zusammenstellen, sodass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Nutzer:innen eindeutige Links senden können (z. B. Nutzer:innen zu ihrem Warenkorb-Abbruch oder zu einem bestimmten Produkt weiterleiten, das wieder auf Lager ist).
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

Wenn Klick-Tracking aktiviert ist oder mit unterstützten Templates verwendet wird, enthält die WhatsApp-Performance-Tabelle die Spalte **Total Clicks**, die eine Anzahl der Klick-Ereignisse pro Variante und eine zugehörige Klickrate anzeigt. Weitere Details zu WhatsApp-Metriken finden Sie unter [WhatsApp-Nachrichten-Performance]({{site.baseurl}}/user_guide/channels/whatsapp/reporting).

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