---
nav_title: "Reporting"
article_title: "Reporting"
page_order: 21
description: "Dieser Referenzartikel behandelt SMS-, MMS- und RCS-Metriken, die in Braze verwendet werden, sowie deren Anzeige in Ihren SMS-, MMS- und RCS-Campaigns."
alias: /sms_mms_rcs_reporting/
page_type: reference
tool:
  - Reports
channel:
  - SMS
  - MMS
  - RCS


---

# Reporting für SMS, MMS und RCS {#reporting-for-sms-mms-and-rcs}

> Dieser Referenzartikel behandelt SMS-, MMS- und RCS-Metriken, die in Braze verwendet werden, sowie deren Anzeige in Ihren SMS-, MMS- und RCS-Campaigns.

{% multi_lang_include analytics/campaign_analytics.md channel="SMS" %}

{% alert note %}
Dashboard-Klickmetriken wie *Total Clicks* schließen vermutete Bot-Aktivitäten aus, aber Currents exportiert weiterhin alle Klick-Ereignisse mit `is_suspected_bot_click` und `suspected_bot_click_reason` für den Data-Warehouse-Abgleich. Informationen zu betroffenen Dashboard-Metriken, Segmentierung und Orchestrierung finden Sie unter [Bot-Klickfilterung für SMS-/RCS-Links]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/bot_click_filtering).
{% endalert %}

## SMS-Opt-ins und -Opt-outs verfolgen {#track-sms-opt-ins-and-opt-outs}

Sie können SMS-Opt-ins und -Opt-outs mit den folgenden Methoden verfolgen:

| Methode | Beschreibung |
|--------|-------------|
| Segmentierer | Der Segmentierer zeigt die Anzahl der Nutzer:innen in einer bestimmten [Abo-Gruppe]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#subscription-group) an. Er dedupliziert nicht nach Telefonnummer – wenn mehrere Nutzer:innen dieselbe Telefonnummer teilen, wird jede Instanz separat gezählt. |
| Abo-Gruppen-Zeitreihe | Bietet eine tägliche Momentaufnahme der Abos für E-Mail und Telefonnummern. Die Zeitreihe zählt Abos, Abmeldungen und erneute Anmeldungen. Wenn sich beispielsweise Nutzer:innen anmelden, abmelden und dann erneut anmelden, werden sie als eine:r abonnierte:r Nutzer:in gezählt. |
| Currents | Verwenden Sie Currents, um [Abo- und Engagement-Ereignisse]({{site.baseurl}}/message_events_glossary) für Ihr eigenes Reporting zu exportieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMS-Opt-ins und -Opt-outs verfolgen" }

{% alert note %}
Die Statistiken zu _Opt-in_ und _Opt-out_ im Panel **SMS/MMS/RCS Performance** spiegeln Nutzer:innen wider, die sich über eingehende Schlüsselwörter an- oder abmelden (z. B. „START“ für Opt-in oder „STOP“ für Opt-out). Diese Zahlen sind in der Regel niedriger als die im Segmentierer angezeigten Werte, da sie die Anzahl der gesendeten Schlüsselwort-Nachrichten zählen, nicht die Gesamtzahl der für SMS abonnierten Nutzer:innen.
{% endalert %}

### SMS-Campaign-Opt-outs verfolgen {#track-sms-campaign-opt-outs}

Verfolgen Sie SMS-Opt-outs auf Campaign-Ebene, indem Sie die Tabelle für eingehende Empfänge anstelle der Tabelle für Abo-Gruppen-Statusänderungen verwenden. Zum Beispiel können Sie im [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) oder in Ihrem Data Warehouse eine Abfrage ausführen, die auf die Tabelle `USERS_MESSAGES_SMS_INBOUNDRECEIVE` oder [`USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED`]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) verweist.

Diese Beispielabfrage referenziert die Tabelle `USERS_MESSAGES_SMS_INBOUNDRECEIVE`:

```sql
SELECT *
FROM USERS_MESSAGES_SMS_INBOUNDRECEIVE
WHERE app_group_id = 'app-group-id'
AND subscription_group_api_id = 'subscription_group_api_id'
AND action = 'Unsubscribed'
AND (campaign_id IS NOT NULL OR canvas_id IS NOT NULL);
```

Diese Abfrage gibt Nutzer:innen zurück, die sich von der SMS-Kommunikation für den angegebenen Workspace und die Abo-Gruppe abgemeldet haben, gefiltert nach denjenigen, die mit Campaigns oder Canvases verknüpft sind.

### Zeitpunkt des Opt-outs {#opt-out-timing}

Schlüsselwort- und eingehende Nachrichtenereignisse in Currents oder Ihrem Data Warehouse, wie Zeitstempel in [`users.messages.sms.InboundReceive`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-inbound-received-events) oder Ereignisse zur Abo-Gruppen-Statusänderung, sind die maßgebliche Quelle dafür, wann Braze das Opt-out erfasst hat.

{% alert note %}
Ereignis-Zeitstempel geben an, wann Braze die eingehende Nachricht empfangen oder verarbeitet hat, nicht unbedingt, wann die Nutzer:innen die SMS gesendet haben oder wann ein Mobilfunkanbieter oder SMS-Provider sie empfangen hat. Wenn Ihre Analyse Opt-outs als den Zeitpunkt betrachtet, zu dem Braze den eingehenden Opt-out-Pfad verarbeitet hat, stimmen diese Zeitstempel mit dieser Definition überein.
{% endalert %}

Das Kundenprofil zeigt den aktuellen Abo-Status an, enthält aber möglicherweise kein einzelnes Feld „SMS abgemeldet am“, es sei denn, Sie setzen ein [angepasstes Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) oder einen ähnlichen Mechanismus bei der Verarbeitung von Opt-outs.

## Gebühren für SMS-Sendeergebnisse {#charges-applied-to-sms-sending-outcomes}

Diese Tabelle spiegelt die Braze-Abrechnung wider, nicht die Abrechnung Ihres Anbieters. Ergebnisse, die von Braze nicht berechnet werden, können von Ihrem Anbieter berechnet werden.

| Ergebnis | Definition | Von Braze berechnet |
|--------|------------|--------|
| Gesendet | Eine Campaign oder ein Canvas-Schritt wurde gestartet oder getriggert, und ein SMS-Payload wurde an den SMS-Anbieter gesendet. | Keine Gebühr |
| Zustellung fehlgeschlagen | Der SMS-Payload konnte nicht an den SMS-Anbieter gesendet werden. Dies kann durch überlaufende Warteschlangen, gesperrte Konten oder Medienfehler (im Fall von MMS) auftreten. | Keine Gebühr |
| Zugestellt | Der SMS-Anbieter hat eine Bestätigung der Nachrichtenzustellung vom vorgelagerten Netzbetreiber (und, sofern verfügbar, vom Zielgerät) erhalten. | Gebühr |
| Abgelehnt | Der SMS-Anbieter hat eine Ablehnungsbestätigung erhalten, die darauf hinweist, dass die Nachricht nicht zugestellt wurde. Dies kann verschiedene Gründe haben, darunter Inhaltsfilterung durch den Netzbetreiber oder Nichterreichbarkeit des Zielgeräts. | Gebühr |
| **Sends to Carrier** | {% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} Veraltet für neue Dashboards. Einige Dashboards zeigen diese Metrik möglicherweise noch als **Sent to Carrier** an. | Gebühren können je nach individuellem Nachrichtensendeergebnis anfallen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Gebühren für SMS-Sendeergebnisse" }

{% alert note %}
**Sends to Carrier** ist für neue Dashboards veraltet. Verwenden Sie **Sent**, **Confirmed Delivery**, **Delivery Failed** und **Rejections** für das aktuelle Reporting. Definitionen finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary).
{% endalert %}

## RCS- und SMS-Fallback-Reporting {#rcs-and-sms-fallback-reporting}

Informationen zum RCS-SMS-Fallback-Ereignisverhalten (einschließlich `IS_SMS_FALLBACK=TRUE`) finden Sie unter [Wie SMS-Fallback mit Ereignissen und Segmentierung funktioniert]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup#how-sms-fallback-works-with-events-and-segmentation).

{% alert note %}
Die Campaign-Analytics im Dashboard und Snowflake-Exporte können sich in Bezug auf Timing und Aggregation geringfügig unterscheiden. Für den Abgleich im Data Warehouse sollten Sie Snowflake- oder Currents-Ereignis-Streams als die granularere Quelle verwenden, wenn die Metriken nicht exakt mit dem Dashboard übereinstimmen.
{% endalert %}

## *Rejections* mit Snowflake oder Currents abgleichen {#reconcile-rejections-with-snowflake-or-currents}

Die Metrik *Rejections* im Dashboard ist eine aggregierte Workspace-Zählung. Es handelt sich nicht um einen Export auf Zeilenebene, daher können Sie nicht jede Ablehnung immer einer einzelnen Zeile in Snowflake oder einem einzelnen `users.messages.sms.Rejection`-Ereignis in Currents zuordnen. Wenn beispielsweise das Kundenprofil gelöscht wurde, bevor Braze die Verarbeitung der Ablehnung für den Data-Warehouse-Export abgeschlossen hat, erscheint diese Ablehnung nicht in Ihrer `USERS_MESSAGES_SMS_REJECTION_SHARED`-Tabelle oder im Currents-Payload, während das aggregierte SMS-Reporting das Ergebnis dennoch widerspiegeln kann. Weitere Informationen finden Sie in der [SQL-Tabellenreferenz]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#sms-message-events-and-deleted-user-profiles) und unter [SMS-Rejection-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) im Currents-Ereignis-Glossar.