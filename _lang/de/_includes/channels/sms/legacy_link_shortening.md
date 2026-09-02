Linkverkürzung und Klick, der or klicken-Tracking ermöglichen es Ihnen, URLs in Kurzmitteilungsdienst or SMS- oder RCS-Nachrichten automatisch zu verkürzen und Klick, der or klicken-through-Rate-Analytics zu erfassen. So erhalten Sie zusätzliche Engagement-Metriken, die Ihnen helfen zu verstehen, wie Nutzer:innen mit Ihren Campaigns interagieren.

Linkverkürzung und Klick, der or klicken-Tracking können auf der [Nachrichtenvarianten-Ebene]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign) sowohl in Campaigns als auch in Canvase aktiviert werden.

{% multi_lang_include channels/Kurzmitteilungsdienst or SMS/rcs_link_shortening_note.md %}

Die Länge der URL wird durch die Art des aktivierten Trackings bestimmt:
- **Basis-Tracking** ermöglicht Klick, der or klicken-Tracking auf Campaign-Ebene. Statische URLs haben eine Länge von 20 Zeichen, und personalisierte URLs haben eine Länge von 25 Zeichen.
- **Erweitertes Tracking** ermöglicht Klick, der or klicken-Tracking auf Campaign- und Nutzer:innen-Ebene und erlaubt die Nutzung von Segmentierungs- und Retargeting-Funktionen, die auf Klicks basieren. Klicks erzeugen außerdem ein [Kurzmitteilungsdienst or SMS-Klick-Ereignis]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), das über Currents gesendet wird. Statische URLs mit erweitertem Tracking haben eine Länge von 27–28 Zeichen, sodass Sie Segmente von Nutzer:innen erstellen können, die auf URLs geklickt haben. Personalisierte URLs haben eine Länge von 32–33 Zeichen.

Links werden über unsere gemeinsame Kurz-Domain (`brz.ai`) oder Ihre angepasste Linkverkürzungs-Domain verkürzt. Eine Beispiel-URL könnte so aussehen: `https://brz.ai/8jshX` (Basis, statisch) oder `https://brz.ai/p/8jshX/2dj8d` (erweitert, personalisiert). Weitere Informationen finden Sie unter [Testen](#testing).

Alle statischen URLs, die mit `http://` oder `https://` beginnen, werden verkürzt. Statisch verkürzte URLs sind ein Jahr ab dem Erstellungsdatum gültig. Verkürzte URLs, die Liquid-Personalisierung enthalten, sind zwei Monate gültig.

{% alert note %}
Verkürzte Braze-Links enthalten immer das Protokoll `https://` und können nicht für die Verwendung eines anderen Protokolls konfiguriert werden.
{% endalert %}

## Linkverkürzung verwenden {#using-link-shortening}

Um die Linkverkürzung zu verwenden, stellen Sie sicher, dass der Linkverkürzungs-Toggle im Nachrichten-Editor aktiviert ist. Wählen Sie dann entweder Basis- oder erweitertes Tracking.

![Nachrichten-Editor mit einem Toggle für die Linkverkürzung.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %})

Braze erkennt nur URLs, die mit `http://` oder `https://` beginnen. Wenn eine URL erkannt wird, aktualisiert sich der Abschnitt **Vorschau** mit einer Platzhalter-URL. Braze schätzt die Länge der URL nach der Verkürzung, aber eine Warnung fordert Sie auf, eine:n Testnutzer:in auszuwählen und die Nachricht als Entwurf zu speichern, um eine genauere Schätzung zu erhalten.

![Nachrichten-Editor mit einer langen URL im Feld „Nachricht“ und einem generierten verkürzten Link in der Vorschau.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %})

{% alert note %}
Wenn Sie den BrazeAI<sup>TM</sup> [Intelligenter-Kanal-Filter]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) verwenden möchten und die Kurzmitteilungsdienst or SMS- und RCS-Kanäle auswählbar sein sollen, aktivieren Sie die Linkverkürzung mit erweitertem Tracking.
{% endalert %}

### UTM-Parameter hinzufügen {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Liquid-Personalisierung in URLs {#liquid-personalization-in-urls}

Sie können Ihre URL direkt im Braze-Composer dynamisch erstellen, sodass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Nutzer:innen eindeutige Links senden können (z. B. um Nutzer:innen zu ihrem Warenkorb-Abbruch oder zu einem bestimmten Produkt weiterzuleiten, das wieder auf Lager ist).

### Eine URL mit unterstützten Liquid-Personalisierungs-Tags erstellen {#create-a-url-with-supported-liquid-personalization-tags}

URLs können dynamisch durch die Verwendung beliebiger [unterstützter Liquid-Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) generiert werden.

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Wir unterstützen auch die Verkürzung angepasster Liquid-Variablen. Nachfolgend finden Sie einige Beispiele:

### Eine URL mit Liquid-Variablen erstellen {#create-a-url-using-liquid-variables}

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Von Liquid-Variablen gerenderte URLs verkürzen {#shorten-urls-rendered-by-liquid-variables}

**Unterstützte Kanäle:** KakaoTalk, LINE, Kurzmitteilungsdienst or SMS, RCS, WhatsApp

Wir verkürzen URLs, die von Liquid gerendert werden, auch solche, die in API-Trigger or triggern-Eigenschaften enthalten sind. Wenn beispielsweise {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, verkürzen und tracken wir diese URL, bevor die Nachricht gesendet wird.

### URLs im `/messages/send`-Endpunkt verkürzen {#shorten-urls-in-messagessend-endpoint}

Die Linkverkürzung ist auch für reine API-Nachrichten über den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) aktiviert. Um zusätzlich Basis- oder erweitertes Tracking zu aktivieren, verwenden Sie die Anfrageparameter `link_shortening_enabled` oder `user_click_tracking_enabled`.

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `link_shortening_enabled` | Optional | Boolescher Wert | Setzen Sie `link_shortening_enabled` auf `true`, um die Linkverkürzung und das Klick, der or klicken-Tracking auf Campaign-Ebene zu aktivieren. Für die Nutzung des Trackings müssen eine `campaign_id` und eine `message_variation_id` vorhanden sein. |
| `user_click_tracking_enabled` | Optional | Boolescher Wert | Setzen Sie `user_click_tracking_enabled` auf `true`, um die Linkverkürzung sowie das Klick, der or klicken-Tracking auf Campaign- und Nutzer:innen-Ebene zu aktivieren. Sie können die getrackten Daten verwenden, um Segmente von Nutzer:innen zu erstellen, die auf URLs geklickt haben.<br><br> Um diesen Parameter zu verwenden, muss `link_shortening_enabled` auf `true` gesetzt sein, und eine `campaign_id` sowie eine `message_variation_id` müssen vorhanden sein. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="URLs im /messages/send-Endpunkt verkürzen" }

Eine vollständige Liste der Anfrageparameter finden Sie unter [Anfrageparameter]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters).

## Testen {#testing}

Bevor Sie Ihre Campaign oder Ihr Canvas starten, empfiehlt es sich, Ihre Nachricht zunächst in der Vorschau anzuzeigen und zu testen. Gehen Sie dazu zum Tab **Test**, um eine Kurzmitteilungsdienst or SMS- oder RCS-Nachricht an [Inhalts-Testgruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) oder eine:n einzelne:n Nutzer:in in der Vorschau anzuzeigen und zu senden.

Diese Vorschau wird mit der relevanten Personalisierung und der verkürzten URL aktualisiert. Die Zeichenanzahl und die [abrechenbaren Segmente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) werden ebenfalls aktualisiert, um die gerenderte Personalisierung und die verkürzte URL widerzuspiegeln.

Stellen Sie sicher, dass Sie die Campaign oder das Canvas speichern, bevor Sie eine Testnachricht senden, um eine Darstellung der verkürzten URL zu erhalten, die in Ihrer Nachricht versendet wird. Wenn die Campaign oder das Canvas vor dem Testversand nicht gespeichert wird, enthält der Testversand eine Platzhalter-URL.

Damit Canvase im Filter „Verkürzten Kurzmitteilungsdienst or SMS-Link angeklickt“ erscheinen, muss der Canvas-Schritt, der den Kurzlink enthält, ebenfalls mit erweitertem Tracking aktiviert sein, das Klick, der or klicken-Tracking auf Nutzer:innen-Ebene ermöglicht. Wenn der Kurzlink mit Basis-Tracking konfiguriert ist, steht die Option zum Filtern von Kurzmitteilungsdienst or SMS-Kurzlink-Klick-Ereignissen nicht zur Verfügung. Dieselbe Anforderung für erweitertes Tracking gilt, wenn Sie Canvas-Eingangs- oder Aktionspfade konfigurieren, die von angeklickten verkürzten Kurzmitteilungsdienst or SMS-Links abhängen.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine verkürzte URL generiert. Die tatsächliche verkürzte URL wird generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

![Tab „Test“ der Nachricht mit Feldern zur Auswahl von Testempfänger:innen.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %})

{% alert note %}
Liquid-Personalisierung und verkürzte URLs werden im Tab **Test** erst nach Auswahl einer:eines Nutzer:in gerendert. Stellen Sie sicher, dass eine:ein Nutzer:in ausgewählt ist, um eine genaue Zeichenanzahl zu erhalten.
{% endalert %}

## Klick, der or klicken-Tracking

Wenn die Linkverkürzung aktiviert ist, enthält die Tabelle **Kurzmitteilungsdienst or SMS/MMS/RCS-Performance** eine Spalte mit dem Titel **Klicks gesamt**, die eine Anzahl der Klick-Ereignisse pro Variante und eine zugehörige Klickrate anzeigt. Weitere Details zu Metriken finden Sie unter [Nachrichten-Performance]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting).

![Tabelle mit SMS- und MMS-Performance-Metriken.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Die Tabellen **Historische Performance** und **Kurzmitteilungsdienst or SMS/MMS/RCS-Performance** enthalten auch eine Option für **Klicks gesamt** und zeigen eine tägliche Zeitreihe der Klick-Ereignisse. Klicks werden bei der Weiterleitung gezählt (z. B. wenn eine:ein Nutzer:in einen Link besucht) und können pro Nutzer:in mehrfach gezählt werden.

## Retargeting von Nutzer:innen {#retargeting-users}

Hinweise zum Retargeting finden Sie unter [Retargeting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Kann ich sehen, welche einzelnen Nutzer:innen auf eine URL klicken? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Ja. Wenn **Erweitertes Tracking** aktiviert ist, können Sie Nutzer:innen, die auf URLs geklickt haben, über die [Kurzmitteilungsdienst or SMS-Retargeting-Filter]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) oder die Kurzmitteilungsdienst or SMS-Klick-Ereignisse (`users.messages.sms.ShortLinkClick`) retargeten, die über Currents gesendet werden.

### Funktioniert die Linkverkürzung mit Deeplinks oder Universal Links? {#does-link-shortening-work-with-deep-links-or-universal-links}

Die Linkverkürzung funktioniert nicht mit Deeplinks. Alternativ können Sie Universal Links von Drittanbietern wie Branch oder Appsflyer verkürzen, aber Nutzer:innen können eine kurze Weiterleitung oder einen „Flicker“-Effekt erleben. Dies geschieht, weil der verkürzte Link zuerst über das Internet geleitet wird, bevor er zum Universal Link aufgelöst wird, der das Öffnen der App unterstützt. Darüber hinaus kann Braze keine Probleme beheben, die beim Verkürzen von Universal Links auftreten können, wie z. B. das Unterbrechen der Attribution oder unerwartete Weiterleitungen.

{% alert note %}
Testen Sie die Nutzererfahrung, bevor Sie die Linkverkürzung mit Universal Links implementieren, um sicherzustellen, dass sie Ihren Erwartungen entspricht.
{% endalert %}

### Sind `send_ids` mit Kurzmitteilungsdienst or SMS-Klick-Ereignissen verknüpft? {#are-send_ids-associated-with-sms-click-events}

Nein. Wenn Sie jedoch erweitertes Tracking aktiviert haben, können Sie `send_ids` in der Regel mit Klick-Ereignissen verknüpfen, indem Sie den [Abfrage-Builder]({{site.baseurl}}/query_builder) verwenden, um Currents-Daten mit dieser Abfrage abzufragen:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```