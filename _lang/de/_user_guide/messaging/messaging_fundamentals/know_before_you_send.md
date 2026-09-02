---
nav_title: "Vor dem Senden beachten"
article_title: "Vor dem Senden beachten"
description: "Nachdem Sie unseren Leitfaden zur Vorbereitung des Starts gelesen haben, finden Sie hier eine abschließende Checkliste oder „Stolperfallen“ für Content Cards, E-Mail, In-App-Nachrichten, Push und SMS."
alias: /know_before_send/
page_order: 7
tool:
    - Campaigns
    - Canvas
---

# Vor dem Senden beachten: Kanäle {#know-before-you-send-channels}

> Starten Sie Ihre Campaigns und Canvases mit Zuversicht! Hier finden Sie eine abschließende Checkliste oder „Stolperfallen“ für beliebte Messaging-[Kanäle]({{site.baseurl}}/user_guide/channels) in Braze.

{% alert note %}
Obwohl wir eine umfangreiche Liste von Ressourcen bereitstellen, die Sie vor dem Senden konsultieren können, hat jeder Kanal individuelle Besonderheiten, die sich mit der Weiterentwicklung unserer Produkte ständig erweitern. Die unten aufgeführten Prüfpunkte sind hilfreiche Empfehlungen, und wir empfehlen, Ihre Campaigns und großen Sendungen vor dem Versand gründlich zu testen.
{% endalert %}

## Allgemein {#general}

### Checkliste {#things-to-check}
- [**API-Rate-Limits**](https://braze.com/resources/articles/whats-rate-limiting): Überprüfen Sie die Braze-API-[Rate-Limits]({{site.baseurl}}/api/api_limits) für Ihre Workspaces, um Fehler zu vermeiden. Wenn Sie Ihre Rate-Limits erhöhen möchten (und bereits Anfragen bündeln), wenden Sie sich an Ihren Customer-Success-Manager. Beachten Sie, dass dieser Prozess eine gewisse Vorlaufzeit erfordert – planen Sie entsprechend.
- [**Erforderliche Frequency-Capping-Ausnahmen**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Es gibt einige Campaigns, wie z. B. transaktionale Nachrichten, die Nutzer:innen immer erreichen sollen, auch wenn das Frequency-Capping bereits erreicht wurde (beispielsweise eine Zustellbenachrichtigung). Wenn eine bestimmte Campaign die Frequency-Capping-Regeln umgehen soll, können Sie dies im Braze-Dashboard einrichten, indem Sie beim Planen der Zustellung dieser Campaign das Frequency-Capping deaktivieren.

### Wissenswertes {#things-to-know}
- [**Globale Kontrollgruppen**]({{site.baseurl}}/user_guide/audience/global_control_group): Wenn Sie eine globale Kontrollgruppe verwenden, erhält ein bestimmter Prozentsatz der Nutzer:innen keine Campaigns oder Canvases. (Sie können Ausnahmen mit den [Ausschlusseinstellungen]({{site.baseurl}}/user_guide/audience/global_control_group#step-3-assign-exclusion-settings) erstellen.) Um eine Liste dieser Nutzer:innen einzusehen, exportieren Sie sie per CSV oder [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group).
- [**Canvas-Rate-Limits**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): In einem Canvas gelten die Rate-Limits für das gesamte Canvas, nicht für die einzelnen Schritte. Wenn Sie beispielsweise ein Rate-Limit von 10.000 Nachrichten pro Minute für ein Canvas mit mehreren Schritten festlegen, bleibt es dennoch auf 10.000 Nachrichten begrenzt, da das Limit bereits beim ersten Schritt erreicht wird.
- **Frequency-Capping**:
  - Frequency-Capping-Regeln werden auf Push, E-Mail, SMS und Webhooks angewendet, jedoch nicht auf In-App-Nachrichten und Content Cards.
  - Das globale Frequency-Capping basiert auf der Zeitzone der Nutzer:innen und wird nach Kalendertagen berechnet, nicht nach 24-Stunden-Zeiträumen. Wenn Sie beispielsweise eine Frequency-Capping-Regel festlegen, die maximal eine Campaign pro Tag erlaubt, kann ein:e Nutzer:in um 23 Uhr in der lokalen Zeitzone eine Nachricht erhalten und wäre bereits eine Stunde später für eine weitere Nachricht berechtigt.

{% alert tip %}
Für weitere Unterstützung bei der Fehlerbehebung von Canvases und Campaigns wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten des Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage zur Verfügung stehen.
{% endalert %}

## Banner {#banners}

### Zu überprüfende Punkte
- **Banner-Abmessungen:** Erstellen Sie Ihre Banner mit einem Element fester Abmessungen und testen Sie sie im Editor.
- **Priorität:** Wenn Sie mehrere Banner starten, können Sie die Priorität für die Anzeige jedes Banners manuell festlegen.

### Wissenswertes
- **Liquid-Personalisierung:** Die Liquid-Personalisierung wird bei jeder Aktualisierungsanfrage neu geladen.
- **Platzierung und Banner-Verhältnis:** Jede Banner-Platzierung kann in bis zu 25 Nachrichten in einem Workspace verwendet werden.
- **Klicks und Impressionen:** Klicks und Impressionen für Banner werden automatisch mit dem SDK erfasst.
- **Einschränkungen:** Derzeit werden die folgenden Features nicht unterstützt: Canvas-Integration, API-getriggerte und aktionsbasierte Campaigns, Connected-Content, Aktionscodes und `catalog_items` mit dem [`:rerender`-Tag]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid).
- **Testen:** Um das Testbanner anzuzeigen, muss das verwendete Gerät in der Lage sein, Push-Benachrichtigungen im Vordergrund zu empfangen.
- **Angepasstes HTML:** Nutzen Sie den [JavaScript-Pont]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), um Klicks zu protokollieren, wenn Sie angepasstes HTML zur Definition von Klickaktionen wie Links und Buttons verwenden. Klickaktionen werden nur automatisch protokolliert, wenn die vorgefertigten Komponenten im Drag-and-Drop-Editor verwendet werden.
- **Platzierungen anfordern:** Bis zu 10 Platzierungen können in einer einzelnen Aktualisierungsanfrage an das SDK zurückgegeben werden. Jede Platzierung enthält das Banner mit der höchsten Priorität, für das ein:e Nutzer:in berechtigt ist.

## Content Cards

### Zu prüfende Punkte
- **Content-Card-Größe**: Content-Card-Nachrichtenfelder sind auf 2&nbsp;KB vor der Komprimierung begrenzt, berechnet durch Addition der Byte-Länge der folgenden Felder: Titel, Nachricht, Bild-URL, Linktext, Link-URLs und Schlüssel-Wert-Paare. Nachrichten, die diese Größe überschreiten, werden nicht gesendet. Beachten Sie, dass dies nicht die Größe des Bildes selbst umfasst, sondern die Länge der Bild-URL.
- **Aktualisierung des Textes nach dem Senden**: Nachdem eine Card gesendet wurde, können Sie den Text auf derselben Card nicht mehr aktualisieren. Lesen Sie [Gesendete Cards aktualisieren]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards), um zu erfahren, wie Sie mit diesem Szenario umgehen können.

### Wissenswertes
- **Limit für aktive Content-Card-Campaigns**: Sie können bis zu 500 aktive Content-Card-Campaigns haben. Dieser Zähler umfasst Content Cards, die mit beiden Optionen zur [Card-Erstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) gesendet werden.
- [**Berichtsbegriffe**]({{site.baseurl}}/user_guide/channels/content_cards/reporting): Überprüfen Sie Begriffe wie Gesamtimpressionen, eindeutige Impressionen und eindeutige Empfänger:innen, da die Definitionen manchmal zu Verwirrung führen können.
- **Content-Card-Aktualisierung**: Standardmäßig aktualisiert Braze Content-Card-Anfragen bei der Synchronisierung zum Sitzungsstart, beim Herunterziehen des Feeds (Mobilgerät) und wenn die Card-Ansicht geöffnet wird, sofern die letzte Aktualisierung mehr als eine Minute zurückliegt.
- **Content-Card-Caching**: Optionen zum Content-Card-Caching finden Sie in unserer Dokumentation für [Android/FireOS]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style) und [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards).
- **Frequency-Capping**: Frequency-Capping gilt nicht für Content Cards.
- **Impressionen**: Impressionen werden in der Regel protokolliert, wenn eine Card angesehen wird. Wenn Sie beispielsweise einen vollen Posteingang mit Content Cards haben, wird eine Impression erst protokolliert, wenn Nutzer:innen zur jeweiligen Content Card scrollen. Es gibt einige Unterschiede zwischen den Web-, Android- und iOS-Plattformen.
- **SDK-Sitzungen und Card-Erstellung**: Content Cards werden nicht für Nutzer:innen ohne SDK-Sitzungen erstellt, auch wenn diese die Segment-Kriterien erfüllen. Wenn ein:e Nutzer:in jedoch bereits eine Android-Sitzung hat, werden Content Cards mit iOS-spezifischen Klickaktionen dennoch erstellt, und die Nutzer:innen können diese Content Cards auf iOS anzeigen, sobald sie dort eine Sitzung haben. Weitere Informationen darüber, wann Cards erstellt werden, finden Sie unter [Card-Erstellung]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card).

## E-Mail {#email}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Checkliste
- **Einwilligung der Kund:innen**: Bevor Sie Ihre ersten E-Mails versenden, ist es wichtig, zunächst die Zustimmung Ihrer Kund:innen einzuholen. Weitere Informationen finden Sie unter [Einwilligung und Adresserfassung]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection) und in unserer [Braze-Richtlinie zur akzeptablen Nutzung](https://www.braze.com/company/legal/aup).
- **Erwartetes Volumen**: 2 Millionen E-Mails pro Tag für eine einzelne IP-Adresse ist die allgemeine Empfehlung, solange dieses Volumen ordnungsgemäß [aufgewärmt]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) wurde.
  - Wenn Sie planen, dauerhaft ein höheres Volumen zu versenden, sollten Sie die Verwendung mehrerer IP-Adressen in einem IP-Pool in Betracht ziehen, um zu vermeiden, dass Anbieter den E-Mail-Empfang drosseln, was zu einer hohen Anzahl von Soft Bounces, einer niedrigeren Zustellbarkeitsrate und einer verschlechterten IP-Reputation führen kann.
  - Wenn Sie nur in einem kürzeren Zeitraum senden möchten, empfehlen wir, zu prüfen, wie schnell verschiedene Anbieter E-Mails akzeptieren, um die geeignete Anzahl von IP-Adressen für den Versand zu ermitteln.

### Wissenswertes
- **Faktoren für das Sendevolumen**: Einige Faktoren, die das mögliche Sendevolumen einer IP-Adresse bestimmen, sind:
  - Postfächer: Große E-Mail-Anbieter können wahrscheinlich Millionen pro Tag von einer einzelnen IP-Adresse verarbeiten, während ein kleinerer regionaler Postfachanbieter oder einer mit geringerer Infrastruktur möglicherweise nicht in der Lage ist, diese Menge zu bewältigen.
  - Absender-Reputation: Sie können möglicherweise ein größeres Volumen pro Tag von einer einzelnen IP-Adresse senden, wenn der Sender auf dieses Volumen hochgefahren wurde und die Absender-Reputation bei jedem Postfach oder jeder Domain, an die gesendet wird, stark genug ist.
- **Best Practices**: Lesen Sie die [Best Practices für E-Mails]({{site.baseurl}}/user_guide/channels/email/best_practices) von Braze und wenden Sie sich an Ihr Braze-Account-Team, wenn Sie mehr über Zustellbarkeitsdienste erfahren möchten.

## In-App-Nachrichten {#in-app-messages}

### Wissenswertes
- **Triggern von In-App-Nachrichten**: Beim Sitzungsstart fordert das SDK an, dass alle berechtigten In-App-Nachrichten zusammen mit ihren Triggern an das Gerät gesendet werden, sodass die Nutzer:innen die In-App-Nachricht schnell und zuverlässig empfangen können, wenn sie das Ereignis während der Sitzung ausführen.
- **Gesendet versus Impressionen**: Bei In-App-Nachrichten unterscheidet sich das Konzept „gesendet“ von den anderen verfügbaren Kanälen. Um eine In-App-Nachricht zu sehen, müssen Nutzer:innen eine Sitzung starten, zur berechtigten Zielgruppe gehören und den Trigger auslösen. Aus diesem Grund werden „Impressionen“ erfasst, da dies aussagekräftiger ist.
- **Triggern**: Standardmäßig werden In-App-Nachrichten durch vom SDK protokollierte Ereignisse getriggert. Wenn Sie In-App-Nachrichten durch serverseitig gesendete Ereignisse triggern möchten, können Sie dies auch über diese Anleitungen für [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=swift) und [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android) erreichen.
- [Canvas-In-App-Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#advancement-behavior): Diese Nachrichten werden angezeigt, wenn Nutzer:innen die App zum ersten Mal öffnen (getriggert durch den Sitzungsstart), nachdem die geplante Nachricht in der Canvas-Komponente an sie gesendet wurde.
- **Connected-Content-Aufrufe**: Die Verwendung von Connected Content ermöglicht es Ihnen, dynamischen Content in Nachrichten zu versenden. Wenn Sie Nachrichten über einen Kanal wie In-App-Nachrichten senden, kann dies mehr gleichzeitige Verbindungen zu den Geräten Ihrer Nutzer:innen erzeugen (Nachrichten werden einzeln und nicht in Stapeln gesendet). Um dies zu verwalten, empfehlen wir, Ihre Nachrichten mit [Rate-Limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) zu versehen.

## Push {#push}

### Zu prüfende Punkte
- [**Opted-in/Subscribed und Push aktiviert**]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states): Damit Nutzer:innen eine Push-Nachricht von Braze erhalten können, muss ihr Abo-Status entweder „Opted-in“ (iOS) oder „Subscribed“ (Android) sein und `Push Enabled = True` gelten. Beachten Sie, dass Android 13 eine wesentliche Änderung daran einführt, wie Nutzer:innen Apps verwalten, die Push-Benachrichtigungen senden. Der Braze [Android 13 SDK-Upgrade-Leitfaden]({{site.baseurl}}/developer_guide/platforms/android/android_13) wird weiterhin aktualisiert, sobald neue Android-13-Beta-Versionen veröffentlicht werden.

### Wissenswerte Informationen
- **Web-Push**: Wenn Sie das Braze [Web SDK eingerichtet]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web) haben, sollten Sie Web-Push nutzen, um Nutzer:innen zu erreichen. Web-Push funktioniert genauso wie App-Push-Benachrichtigungen auf Ihrem Smartphone. Weitere Informationen zum Erstellen eines Web-Pushs finden Sie unter [Push-Benachrichtigung erstellen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).
- **Targeting einer einzelnen App**: Lesen Sie die [Unterschiede bei der Segmentierung]({{site.baseurl}}/user_guide/get_started/workspaces), um eine einzelne App und deren Nutzer:innen gezielt anzusprechen.

## SMS

### Zu prüfende Punkte
- **Kontingente und Durchsatz**: Informieren Sie sich darüber, welche SMS-Kontingente derzeit mit Ihrem Konto verknüpft sind (Shortcode, Langcode und ähnliche) und [wie viel Durchsatz Ihnen das bietet]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup), um sicherzustellen, dass Sie genügend Durchsatz haben, um in der gewünschten Zeit zu senden.
- **SMS-Segmente aus dem SMS-Text schätzen**: Testen Sie Ihren SMS-Text im [SMS-Segment-Rechner]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator). Beachten Sie, dass die Anzahl der SMS-Segmente zusammen mit Ihren Durchsatzkapazitäten berücksichtigt werden sollte. (Zielgruppe × SMS-Segmente = benötigter Durchsatz.) Lesen Sie die SMS-FAQ zum Thema [Mehrkosten vermeiden]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs).
- **SMS-Gesetze und -Vorschriften**: [Lesen Sie die SMS-Gesetze, -Vorschriften und die Missbrauchsprävention]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), um sicherzustellen, dass Sie die SMS-Dienste in Übereinstimmung mit allen geltenden Gesetzen nutzen. Holen Sie vor dem Senden unbedingt den Rat Ihres Rechtsberaters ein.

### Wissenswertes
- **SMS-Nachrichtenstandard**: SMS-Nachrichten werden normalerweise standardmäßig über den Shortcode im Sender-Pool gesendet.
- **Alphanumerische Sender-ID**: Zwei-Wege-Messaging funktioniert nicht mehr, wenn Sie eine alphanumerische Sender-ID verwenden; diese sind jetzt nur noch für Einweg-Kommunikation geeignet.
- **Aktualisierter Durchsatz in den USA**: Der Durchsatz hat sich in den USA mit der [A2P 10DLC-Registrierung](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) geändert. Beachten Sie, dass wir vertraglich keine SLAs für die Sendegeschwindigkeit zusichern, da mehrere Faktoren wie Verkehrsüberlastung und Carrier-Probleme die tatsächlichen Zustellraten beeinflussen können.
- **Abo-Gruppe**: Um eine SMS-Campaign über Braze zu starten, muss eine Abo-Gruppe ausgewählt werden. Um die internationalen [Telekommunikations-Compliance- und Richtlinien]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) einzuhalten, sendet Braze niemals SMS an Nutzer:innen, die die [ausgewählte Abo-Gruppe nicht abonniert haben]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#check-a-users-group).

## WhatsApp

### Wissenswertes

- [**Best Practices**]({{site.baseurl}}/user_guide/channels/whatsapp/best_practices): Lesen Sie unsere empfohlenen WhatsApp-Best-Practices.