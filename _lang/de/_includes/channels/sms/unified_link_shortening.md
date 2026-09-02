Link-Shortening ermöglicht es Ihnen, URLs in SMS- oder RCS-Nachrichten automatisch zu kürzen und Klickraten-Analytics zu erfassen. So erhalten Sie zusätzliche Engagement-Metriken, die Ihnen helfen zu verstehen, wie Nutzer:innen mit Ihren Campaigns interagieren.

Link-Shortening kann auf [Nachrichtenvarianten-Ebene]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign) sowohl in Campaigns als auch in Canvases aktiviert werden. Wenn Link-Shortening aktiviert ist, werden Klicks als [SMS-Klick-Event]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) generiert und über Currents gesendet.

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

Links werden über unsere gemeinsame Short-Domain (`brz.ai`) oder Ihre angepasste Link-Shortening-Domain gekürzt und sind ab dem Erstellungsdatum 9 Wochen lang gültig. Eine Beispiel-URL könnte etwa so aussehen: `https://brz.ai/8jshX2dj`.

## Verwendung von Link-Shortening {#using-link-shortening}

Um Link-Shortening zu verwenden, stellen Sie sicher, dass das Kontrollkästchen für Link-Shortening im Nachrichten-Editor aktiviert ist.

{% tabs %}
{% tab SMS composer %}

![SMS-Nachrichten-Editor mit aktiviertem Kontrollkästchen für Link-Shortening.]({% image_buster /assets/img/link_shortening/shortening1.png %}){: width="1562" height="1068"}

{% endtab %}
{% tab RCS composer %}

![RCS-Nachrichten-Editor mit aktiviertem Kontrollkästchen für Link-Shortening.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %}){: width="1476" height="1222"}

{% endtab %}
{% endtabs %}

Braze erkennt nur URLs, die mit `http://` oder `https://` beginnen. Wenn eine URL erkannt wird, aktualisiert sich der Abschnitt **Vorschau** mit einer Platzhalter-URL. Braze schätzt die Nachrichtenlänge nach dem Shortening, aber eine Warnung fordert Sie auf, eine:n Testnutzer:in auszuwählen und die Nachricht als Entwurf zu speichern, um eine genauere Schätzung zu erhalten.

![Nachrichten-Editor mit einer langen URL im Feld „Nachricht“ und einem generierten gekürzten Link in der Vorschau.]({% image_buster /assets/img/link_shortening/shortening3.png %}){: width="1552" height="612"}

### UTM-Parameter hinzufügen {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Liquid-Personalisierung in URLs {#liquid-personalization-in-urls}

Informationen darüber, wie Sie URLs direkt im Braze-Nachrichten-Editor dynamisch erstellen können, um dynamische UTM-Parameter zu Ihren URLs hinzuzufügen oder Nutzer:innen eindeutige Links zu senden, finden Sie unter [Liquid-Personalisierung in URLs verwenden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls).

## Testen {#testing}

Bevor Sie Ihre Campaign oder Ihr Canvas starten, sollten Sie Ihre Nachricht zunächst in der Vorschau ansehen und testen. Gehen Sie dazu auf den Tab **Test**, um eine SMS- oder RCS-Nachricht in der Vorschau anzuzeigen und an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) oder einzelne Nutzer:innen zu senden.

Diese Vorschau wird mit der relevanten Personalisierung und der gekürzten URL aktualisiert. Die Zeichenanzahl und die [abrechenbaren Segmente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) werden ebenfalls aktualisiert, um die gerenderte Personalisierung und die gekürzte URL widerzuspiegeln.

Stellen Sie sicher, dass Sie die Campaign oder das Canvas speichern, bevor Sie eine Testnachricht senden, um eine Darstellung der gekürzten URL zu erhalten, die in Ihrer Nachricht versendet wird. Wenn die Campaign oder das Canvas vor dem Testversand nicht gespeichert wird, enthält der Testversand eine Platzhalter-URL.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine gekürzte URL generiert. Die tatsächliche gekürzte URL wird erst generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

![Tab „Test“ der Nachricht mit Feldern zur Auswahl von Testempfänger:innen.]({% image_buster /assets/img/link_shortening/shortening2.png %}){: width="1544" height="1140"}

{% alert note %}
Liquid-Personalisierung und gekürzte URLs werden im Tab **Test** erst nach Auswahl einer Nutzerin oder eines Nutzers gerendert. Stellen Sie sicher, dass Nutzer:innen ausgewählt sind, um eine genaue Zeichenanzahl zu erhalten.
{% endalert %}

## Klick-Tracking {#click-tracking}

Wenn die Linkverkürzung aktiviert ist, enthält die Tabelle **SMS/MMS/RCS Performance** eine Spalte mit dem Titel **Total Clicks**, die eine Anzahl der Klick-Ereignisse pro Variante und eine zugehörige Klickrate anzeigt. Weitere Informationen zu Metriken finden Sie unter [Nachrichtenperformance]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting).

![Tabelle mit SMS- und MMS-Performance-Metriken.]({% image_buster /assets/img/link_shortening/shortening4.png %}){: width="1586" height="191"}

Die Tabellen **Historical Performance** und **SMS/MMS/RCS Performance** enthalten außerdem eine Option für **Total Clicks** und zeigen eine tägliche Zeitreihe von Klick-Ereignissen an. Klicks werden bei der Weiterleitung gezählt (z. B. wenn Nutzer:innen einen Link aufrufen) und können pro Nutzer:in mehrfach gezählt werden.

## Retargeting von Nutzer:innen {#retargeting-users}

Informationen zum Retargeting finden Sie unter [Retargeting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Kann ich sehen, welche einzelnen Nutzer:innen auf eine URL klicken? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Ja. Sie können Nutzer:innen, die auf URLs geklickt haben, mithilfe der [SMS-Retargeting-Filter]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) oder der SMS-Klick-Events (`users.messages.sms.ShortLinkClick`) über Currents erneut ansprechen.

### Funktioniert die Link-Verkürzung mit Deeplinks oder Universal Links? {#does-link-shortening-work-with-deep-links-or-universal-links}

Die Link-Verkürzung funktioniert nicht mit Deeplinks. Alternativ können Sie Universal Links von Drittanbietern wie Branch oder Appsflyer verkürzen, wobei Nutzer:innen jedoch möglicherweise eine kurze Weiterleitung oder einen „Flacker“-Effekt erleben. Dies geschieht, weil der verkürzte Link zunächst über das Internet geroutet wird, bevor er zum Universal Link aufgelöst wird, der das Öffnen der App unterstützt. Darüber hinaus kann Braze keine Probleme beheben, die beim Verkürzen von Universal Links auftreten können, wie z. B. das Unterbrechen der Attribution oder unerwartete Weiterleitungen.

{% alert note %}
Testen Sie die Nutzererfahrung, bevor Sie die Link-Verkürzung mit Universal Links implementieren, um sicherzustellen, dass sie Ihren Erwartungen entspricht.
{% endalert %}

### Sind `send_ids` mit SMS-Klick-Events verknüpft? {#are-send_ids-associated-with-sms-click-events}

Nein. Sie können `send_ids` jedoch in der Regel Klick-Events zuordnen, indem Sie den [Query Builder]({{site.baseurl}}/query_builder) verwenden, um Currents-Daten mit dieser Abfrage abzufragen:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```