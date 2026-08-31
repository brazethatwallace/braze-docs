Link-Shortening ermöglicht es Ihnen, URLs in SMS- oder RCS-Nachrichten automatisch zu kürzen und Klickraten-Analytics zu erfassen. So erhalten Sie zusätzliche Engagement-Metriken, die Ihnen helfen zu verstehen, wie Nutzer:innen mit Ihren Campaigns interagieren.

Link-Shortening kann auf [Nachrichtenvarianten-Ebene]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign) sowohl in Campaigns als auch in Canvases aktiviert werden. Wenn Link-Shortening aktiviert ist, werden Klicks als [SMS-Klick-Event]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) generiert und über Currents gesendet.

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

Links werden über unsere gemeinsame Short-Domain (`brz.ai`) oder Ihre angepasste Link-Shortening-Domain gekürzt und sind ab dem Erstellungsdatum 9 Wochen lang gültig. Eine Beispiel-URL könnte etwa so aussehen: `https://brz.ai/8jshX2dj`.

## Link-Shortening verwenden {#using-link-shortening}

Um Link-Shortening zu verwenden, stellen Sie sicher, dass das Kontrollkästchen für Link-Shortening im Nachrichten-Editor aktiviert ist.

{% tabs %}
{% tab SMS composer %}

![SMS-Nachrichten-Editor mit aktiviertem Kontrollkästchen für Link-Shortening.]({% image_buster /assets/img/link_shortening/shortening1.png %})

{% endtab %}
{% tab RCS composer %}

![RCS-Nachrichten-Editor mit aktiviertem Kontrollkästchen für Link-Shortening.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %})

{% endtab %}
{% endtabs %}

Braze erkennt nur URLs, die mit `http://` oder `https://` beginnen. Wenn eine URL erkannt wird, aktualisiert sich der Bereich **Vorschau** mit einer Platzhalter-URL. Braze schätzt die Nachrichtenlänge nach dem Kürzen, aber eine Warnung fordert Sie auf, eine:n Testnutzer:in auszuwählen und die Nachricht als Entwurf zu speichern, um eine genauere Schätzung zu erhalten.

![Nachrichten-Editor mit einer langen URL im Feld „Nachricht“ und einem generierten gekürzten Link in der Vorschau.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### UTM-Parameter hinzufügen {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Liquid-Personalisierung in URLs {#liquid-personalization-in-urls}

Informationen darüber, wie Sie URLs direkt im Braze-Nachrichten-Editor dynamisch erstellen, dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Nutzer:innen eindeutige Links senden können, finden Sie unter [Liquid-Personalisierung in URLs verwenden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls).

## Testen {#testing}

Bevor Sie Ihre Campaign oder Ihr Canvas starten, empfiehlt es sich, Ihre Nachricht zuerst in der Vorschau anzuzeigen und zu testen. Gehen Sie dazu zum Tab **Test**, um eine SMS- oder RCS-Nachricht in der Vorschau anzuzeigen und an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) oder einzelne Nutzer:innen zu senden.

Diese Vorschau wird mit der relevanten Personalisierung und der gekürzten URL aktualisiert. Die Zeichenanzahl und die [abrechenbaren Segmente]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator) werden ebenfalls aktualisiert, um die gerenderte Personalisierung und die gekürzte URL widerzuspiegeln.

Stellen Sie sicher, dass Sie die Campaign oder das Canvas speichern, bevor Sie eine Testnachricht senden, um eine Darstellung der gekürzten URL zu erhalten, die in Ihrer Nachricht versendet wird. Wenn die Campaign oder das Canvas vor einem Testversand nicht gespeichert wurde, enthält der Testversand eine Platzhalter-URL.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine gekürzte URL generiert. Die tatsächliche gekürzte URL wird generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

![Tab „Test“ der Nachricht mit Feldern zur Auswahl von Testempfänger:innen.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
Liquid-Personalisierung und gekürzte URLs werden im Tab **Test** als Template angewendet, nachdem ein:e Nutzer:in ausgewählt wurde. Stellen Sie sicher, dass ein:e Nutzer:in ausgewählt ist, um eine genaue Zeichenanzahl zu erhalten.
{% endalert %}

## Klick-Tracking {#click-tracking}

Wenn die Linkverkürzung aktiviert ist, enthält die Tabelle **SMS/MMS/RCS Performance** eine Spalte mit dem Titel **Total Clicks**, die eine Anzahl der Klick-Ereignisse pro Variante und eine zugehörige Klickrate anzeigt. Weitere Informationen zu Metriken finden Sie unter [Nachrichten-Performance]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting).

![Tabelle mit SMS- und MMS-Performance-Metriken.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Die Tabellen **Historical Performance** und **SMS/MMS/RCS Performance** bieten außerdem eine Option für **Total Clicks** und zeigen eine tägliche Zeitreihe der Klick-Ereignisse an. Klicks werden bei einer Weiterleitung gezählt (z. B. wenn Nutzer:innen einen Link aufrufen) und können pro Nutzer:in mehrfach gezählt werden.

## Retargeting von Nutzer:innen {#retargeting-users}

Anleitungen zum Retargeting finden Sie unter [Retargeting]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Kann ich sehen, welche einzelnen Nutzer:innen auf eine URL klicken? {#do-i-know-which-individual-users-are-clicking-on-a-url}

Ja. Sie können Nutzer:innen, die auf URLs geklickt haben, mithilfe der [SMS-Retargeting-Filter]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) oder der SMS-Klick-Ereignisse (`users.messages.sms.ShortLinkClick`) über Currents erneut ansprechen.

### Funktioniert die Linkverkürzung mit Deeplinks oder Universal Links? {#does-link-shortening-work-with-deep-links-or-universal-links}

Die Linkverkürzung funktioniert nicht mit Deeplinks. Alternativ können Sie Universal Links von Drittanbietern wie Branch oder Appsflyer verkürzen, allerdings kann es dabei zu einer kurzen Weiterleitung oder einem „Flicker“-Effekt kommen. Das liegt daran, dass der verkürzte Link zunächst über das Internet geleitet wird, bevor er zum Universal Link aufgelöst wird, der das Öffnen der App unterstützt. Darüber hinaus kann Braze keine Probleme beheben, die beim Verkürzen von Universal Links auftreten können, wie etwa die Beeinträchtigung der Attribution oder unerwartete Weiterleitungen.

{% alert note %}
Testen Sie die Nutzererfahrung, bevor Sie die Linkverkürzung mit Universal Links implementieren, um sicherzustellen, dass sie Ihren Erwartungen entspricht.
{% endalert %}

### Sind `send_ids` mit SMS-Klick-Ereignissen verknüpft? {#are-send_ids-associated-with-sms-click-events}

Nein. Sie können `send_ids` jedoch in der Regel mit Klick-Ereignissen verknüpfen, indem Sie den [Query Builder]({{site.baseurl}}/query_builder) verwenden, um Currents-Daten mit folgender Abfrage abzurufen:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```