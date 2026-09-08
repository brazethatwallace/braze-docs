---
nav_title: "SQL-Tabellenreferenz"
article_title: "SQL-Tabellenreferenz"
page_order: 3
page_type: reference
toc_headers: h2
description: "Diese Seite ist eine Referenz der Snowflake-SQL-Tabellen und -Spalten, die im Query Builder, in SQL-Segmenterweiterungen und in der Snowflake-Datenfreigabe verwendet werden."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL-Tabellenreferenz {#sql-table-reference}

Diese Seite ist eine Referenz der Snowflake-SQL-Tabellen und -Spalten, die in den folgenden Braze-Tools verfügbar sind:

- [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)
- [Snowflake-Datenfreigabe]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)

Die meisten Tabellen sind in allen drei Tools verfügbar. Tabellen, die mit **Nur Snowflake-Datenfreigabe** gekennzeichnet sind, stehen ausschließlich in der Snowflake-Datenfreigabe zur Verfügung und sind im Query Builder oder in SQL-Segmenterweiterungen nicht zugänglich.

{% alert tip %}
Diese SQL-Tabellen entsprechen den Ereignissen, die im [Currents-Ereignisglossar]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) dokumentiert sind. Beispielsweise entspricht die SQL-Tabelle `USERS_MESSAGES_EMAIL_SEND_SHARED` dem Currents-Ereignis `users.messages.email.Send`. Wenn Sie JSON-Ereignisschemata oder partnerspezifische Formate (Amplitude, Mixpanel, Segment) benötigen, lesen Sie das Currents-Glossar.
{% endalert %}

## Inhaltsverzeichnis {#table-of-contents}

Tabelle | Beschreibung
------|------------
[AGENTCONSOLE_AGENTEXECUTED_SHARED](#AGENTCONSOLE_AGENTEXECUTED_SHARED) | Wenn ein Agent-Console-Agent ausgeführt wird (**nur Snowflake Data Sharing**)
[AGENTCONSOLE_RAWLLMREQUEST_SHARED](#AGENTCONSOLE_RAWLLMREQUEST_SHARED) | Rohinformationen zu jedem LLM-Aufruf (**nur Snowflake Data Sharing**)
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | Wenn ein Tool ausgeführt wird (**nur Snowflake Data Sharing**)
[USER_CUSTOM_ATTRIBUTES_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED) | Periodischer Snapshot angepasster Profilattribute pro Nutzer:in
[USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED) | Historische Standard-Profilattribute mit Gültigkeitszeiträumen
[USER_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED) | Periodischer Snapshot von Standard-Profilattributen pro Nutzer:in
[USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED) | Nahezu in Echtzeit erfasste Standard-Profilattribute pro Nutzer:in
[USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED) | Historische angepasste Profilattribute mit Gültigkeitszeiträumen (**nur Snowflake Data Sharing**)
[USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED](#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED) | Nahezu in Echtzeit erfasste angepasste Profilattribute pro Nutzer:in (**nur Snowflake Data Sharing**)
[USER_DEFAULT_ATTRIBUTES_HISTORY_RAW_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_HISTORY_RAW_VIEW_SHARED) | Historische Roh-Standard-Profilattribute ohne Enddatum (**nur Snowflake Data Sharing**)
[USER_CUSTOM_ATTRIBUTES_HISTORY_RAW_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_HISTORY_RAW_VIEW_SHARED) | Historische rohe angepasste Profilattribute ohne Enddatum (**nur Snowflake Data Sharing**)
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Nicht gelöschte Katalogartikel
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | Wenn eine Campaign geändert wird (**nur Snowflake Data Sharing**)
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | Wenn ein Canvas geändert wird (**nur Snowflake Data Sharing**)
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Wenn die globale Kontrollgruppe geändert wird
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Wenn ein:e Nutzer:in ein angepasstes Event ausführt
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Wenn ein:e Nutzer:in eine App installiert und wir dies einem Partner zuordnen
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Wenn ein:e Nutzer:in einen Standort aufzeichnet
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Wenn ein:e Nutzer:in einen Kauf tätigt
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Wenn ein:e Nutzer:in eine App deinstalliert
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Wenn ein:e Nutzer:in die App upgradet
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Wenn ein:e Nutzer:in die erste Sitzung hat
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Wenn ein:e Nutzer:in den News Feed aufruft
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Wenn ein:e Nutzer:in eine Sitzung in einer App beendet
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Wenn ein:e Nutzer:in eine Sitzung in einer App beginnt
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Wenn ein:e Nutzer:in einen Geofence-Bereich auslöst – zum Beispiel beim Betreten oder Verlassen eines Geofence. Dieses Ereignis wird mit anderen Ereignissen gebündelt und über den Standard-Endpunkt für Ereignisse empfangen, sodass es möglicherweise nicht in Echtzeit angezeigt wird.<br><br>Um Geofence-Aktivitäten in dieser Tabelle zu protokollieren, aktivieren Sie **Enable Analytics for Enter** und **Enable Analytics for Exit** in den erweiterten Einstellungen für jeden Geofence. Weitere Details finden Sie in Schritt 3 unter [Geofences manuell erstellen]({{site.baseurl}}/user_guide/audience/locations_and_geofences/creating_geofences#manually-create-geofences).
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Wenn ein:e Nutzer:in einen Geofence-Bereich auslöst (z. B. beim Betreten oder Verlassen eines Geofence). Dieses Ereignis wurde über den dedizierten Geofence-Endpunkt empfangen und geht daher in Echtzeit ein, sobald das Gerät erkennt, dass ein Geofence ausgelöst wurde. <br><br>Aufgrund von Rate-Limiting am Geofence-Endpunkt kann es außerdem vorkommen, dass einige Geofence-Ereignisse nicht als RecordEvent erfasst werden. Alle Geofence-Ereignisse werden jedoch durch DataEvent abgebildet (ggf. mit einer Verzögerung durch die Bündelung).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Wenn sich ein Push-to-Start-Token einer Live Activity ändert
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Wenn sich ein Update-Token einer Live Activity ändert
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Wenn sich der Status eines Push-Benachrichtigungs-Tokens ändert
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Wenn ein:e Nutzer:in global für einen Kanal wie E-Mail an- oder abgemeldet wird
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Wenn ein:e Nutzer:in in einer Abo-Gruppe an- oder abgemeldet wird
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Wenn ein:e Nutzer:in für eine Campaign konvertiert
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Wenn ein:e Nutzer:in in die Kontrollgruppe einer Campaign aufgenommen wird
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Wenn ein:e Nutzer:in das Frequency Cap für eine Campaign erreicht
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Wenn ein:e Nutzer:in innerhalb des primären Konversionszeitraums Umsatz generiert
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Wenn ein:e Nutzer:in zu einem Canvas-Schritt fortschreitet
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Wenn ein:e Nutzer:in für ein Canvas-Konversions-Event konvertiert
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Wenn ein:e Nutzer:in in ein Canvas eintritt
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Wenn ein:e Nutzer:in ein Canvas verlässt, weil er/sie die Exit-Kriterien der Zielgruppe erfüllt
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Wenn ein:e Nutzer:in ein Canvas verlässt, weil er/sie ein Ausnahme-Event ausgeführt hat
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Wenn ein:e Nutzer:in für einen Canvas-Experiment-Schritt konvertiert
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Wenn ein:e Nutzer:in einen Experiment-Schritt-Pfad betritt
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Wenn ein:e Nutzer:in das Frequency Cap für einen Canvas-Schritt erreicht
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Wenn ein:e Nutzer:in innerhalb des primären Konversions-Event-Zeitraums Umsatz generiert
[USERS_CANVAS_COSTEP_CONVERSION_SHARED](#USERS_CANVAS_COSTEP_CONVERSION_SHARED) | Konversions-Events für den Content-Optimizer-Canvas-Schritt
[USERS_CANVAS_COSTEP_SEND_SHARED](#USERS_CANVAS_COSTEP_SEND_SHARED) | Die Canvas-Sendungen für den Content-Optimization-Canvas-Schritt
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Eine ursprünglich geplante Banner-Nachricht wurde aus irgendeinem Grund abgebrochen
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Wenn ein:e Nutzer:in auf ein Banner klickt
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Wenn ein:e Nutzer:in ein Banner anzeigt
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Eine ursprünglich geplante Content-Card-Nachricht wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Wenn ein:e Nutzer:in auf eine Content-Card klickt
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Wenn ein:e Nutzer:in eine Content-Card schließt
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Wenn ein:e Nutzer:in eine Content-Card ansieht
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Wenn wir eine Content-Card an eine:n Nutzer:in senden
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Eine ursprünglich geplante E-Mail-Nachricht wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Ein E-Mail-Anbieter hat einen Hard Bounce zurückgegeben. Ein Hard Bounce bedeutet ein dauerhaftes Zustellbarkeitsproblem.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Wenn ein:e Nutzer:in auf einen Link in einer E-Mail klickt
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Wenn eine E-Mail zurückgestellt wird
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Wenn eine E-Mail zugestellt wird
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Wenn eine E-Mail als Spam markiert wird
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Wenn ein:e Nutzer:in eine E-Mail öffnet
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Wenn wir eine E-Mail an eine:n Nutzer:in senden
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Wenn eine E-Mail einen Soft Bounce verursacht
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Wenn sich ein:e Nutzer:in von E-Mails abmeldet
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | Wenn eine E-Mail-Nachricht nach Deprioritisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Wenn ein:e Nutzer:in ein Feature-Flag anzeigt
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Eine ursprünglich geplante In-App-Nachricht wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Wenn ein:e Nutzer:in auf eine In-App-Nachricht klickt
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Wenn ein:e Nutzer:in eine In-App-Nachricht ansieht
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Wenn eine geplante LINE-Nachricht vor dem Senden an LINE nicht zugestellt werden kann
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Wenn ein:e Nutzer:in auf einen Link in einer LINE-Nachricht klickt
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Wenn eine LINE-Nachricht von einer/einem Nutzer:in empfangen wird
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Wenn eine LINE-Nachricht an LINE gesendet wird
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | Wenn eine LINE-Nachricht nach Deprioritisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Wenn eine Live Activity ein Ergebnis-Ereignis aufweist
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Wenn eine Live-Activity-Nachricht gesendet wird
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Eine ursprünglich geplante Newsfeed-Card-Nachricht wurde aus irgendeinem Grund abgebrochen
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Wenn ein:e Nutzer:in auf eine Newsfeed-Card klickt
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Wenn ein:e Nutzer:in eine Newsfeed-Card ansieht
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Eine ursprünglich geplante Push-Benachrichtigungsnachricht wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Wenn eine Push-Benachrichtigung bounct
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Wenn ein:e Nutzer:in die App öffnet, nachdem er/sie eine Benachrichtigung erhalten hat, ohne darauf zu klicken
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Wenn ein:e Nutzer:in eine Push-Benachrichtigung erhält, während die App geöffnet ist. <br><br>Dieses Ereignis wird vom [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) nicht unterstützt und ist im [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) veraltet.
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Wenn ein:e Nutzer:in eine Push-Benachrichtigung öffnet oder auf einen Push-Benachrichtigungs-Button klickt (einschließlich eines CLOSE-Buttons, der die App NICHT öffnet). <br><br> Push-Button-Aktionen haben mehrere mögliche Ergebnisse. „No“-, „Decline“- und „Cancel“-Aktionen sind „Klicks“, und „Accept“-Aktionen sind „Öffnungen“. Beide werden in dieser Tabelle abgebildet und können über die Spalte **BUTTON_ACTION_TYPE** unterschieden werden. Zum Beispiel kann eine Abfrage verwendet werden, um nach einem `BUTTON_ACTION_TYPE` zu gruppieren, der nicht „No“, „Decline“ oder „Cancel“ ist.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Wenn wir eine Push-Benachrichtigung an eine:n Nutzer:in senden
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Wenn ein RCS-Versand aufgrund eines in Braze erkannten Fehlers unterbrochen wird und die Nachricht verworfen wird
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Wenn die/der Endnutzer:in mit einer RCS-Nachricht interagiert, indem sie/er auf ein UI-Element tippt oder klickt
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Wenn eine RCS-Nachricht erfolgreich an das Mobilgerät der/des Endnutzer:in zugestellt wird
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Wenn Braze eine RCS-Nachricht empfängt, die von der/dem Endnutzer:in stammt
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Wenn die/der Endnutzer:in eine RCS-Nachricht auf ihrem/seinem Gerät öffnet
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Wenn eine RCS-Nachricht aufgrund einer Intervention durch den Carrier nicht zugestellt werden kann
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Wenn eine RCS-Nachricht aus den Braze-Systemen an Last-Mile-Zustellpartner gesendet wird
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Eine ursprünglich geplante SMS-Nachricht wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Wenn eine SMS-Nachricht an den Carrier gesendet wird
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Wenn eine SMS-Nachricht zugestellt wird
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Wenn Braze die SMS-Nachricht nicht an den SMS-Dienstanbieter zustellen kann
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Wenn eine SMS-Nachricht von einer/einem Nutzer:in empfangen wird
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Wenn eine SMS-Nachricht nicht an eine:n Nutzer:in zugestellt wird
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Wenn eine SMS-Nachricht gesendet wird
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Wenn ein:e Nutzer:in auf eine von Braze gekürzte URL in einer SMS-Nachricht klickt
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | Wenn eine SMS-Nachricht nach Deprioritisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Eine ursprünglich geplante Webhook-Nachricht wurde aus irgendeinem Grund abgebrochen
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Wenn eine Webhook-Nachricht zugestellt wird, aber mit einer Fehlerantwort vom Endpunkt fehlschlägt
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Wenn wir einen Webhook für eine:n Nutzer:in senden
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | Wenn eine Webhook-Nachricht nach Deprioritisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Eine ursprünglich geplante WhatsApp-Nachricht wurde aus irgendeinem Grund abgebrochen
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Wenn ein:e Nutzer:in auf einen Link oder Button in einer WhatsApp-Nachricht klickt
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | Wenn eine WhatsApp-Nachricht zugestellt wird
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Wenn eine WhatsApp-Nachricht nicht an eine:n Nutzer:in zugestellt wird
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Wenn eine WhatsApp-Nachricht von einer/einem Nutzer:in empfangen wird
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Wenn ein:e Nutzer:in eine WhatsApp-Nachricht öffnet
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Wenn wir eine WhatsApp-Nachricht für eine:n Nutzer:in senden
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | Wenn eine WhatsApp-Nachricht nach Deprioritisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_BANNER_DISMISS_SHARED](#USERS_MESSAGES_BANNER_DISMISS_SHARED) | Wenn ein:e Nutzer:in ein Banner schließt.
[USERS_MESSAGES_LANDINGPAGE_CLICK_SHARED](#USERS_MESSAGES_LANDINGPAGE_CLICK_SHARED) | Dieses Ereignis tritt auf, wenn ein:e Endnutzer:in auf ausgewählte Elemente und Formularfelder auf einer Landing-Page klickt
[USERS_MESSAGES_LANDINGPAGE_FORMSUBMISSION_SHARED](#USERS_MESSAGES_LANDINGPAGE_FORMSUBMISSION_SHARED) | Dieses Ereignis tritt auf, wenn ein:e Endnutzer:in ein Formular auf einer Landing-Page ausfüllt und auf den Button zum Absenden der Informationen klickt
[USERS_MESSAGES_LANDINGPAGE_IMPRESSION_SHARED](#USERS_MESSAGES_LANDINGPAGE_IMPRESSION_SHARED) | Dieses Ereignis tritt auf, wenn der Browser einer/eines Endnutzer:in eine Landing-Page lädt und anzeigt
[USERS_MESSAGES_PUSHNOTIFICATION_RETRY_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_RETRY_SHARED) | Dieses Ereignis tritt auf, wenn eine Nachricht deprioritisiert oder durch Frequency Capping begrenzt wurde und innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird. Dies ist nur für Kund:innen der Message-Prioritization-Beta verfügbar
[USERS_MESSAGES_SURVEY_RESPONSE_SHARED](#USERS_MESSAGES_SURVEY_RESPONSE_SHARED) | Von Endnutzer:innen übermittelte Umfrageantworten
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Wenn die zufällige Bucket-Nummer einer/eines Nutzer:in geändert wird
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Wenn ein:e Nutzer:in durch eine Kundenanfrage gelöscht wird
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Wenn ein:e Nutzer:in mit dem Profil einer/eines anderen Nutzer:in zusammengeführt wird und das ursprüngliche Profil verwaist
[USERS_PROFILE_UPDATE_SHARED](#USERS_PROFILE_UPDATE_SHARED) | Nachricht, die die Profilaktualisierungen für eine:n Nutzer:in darstellt
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | App-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | Campaign-Nachrichtenvarianten-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | Canvas-Flow-Schritt-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | Canvas-Schritt-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | Canvas-Varianten-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | Experiment-Schritt-Snapshots (**nur Snowflake Data Sharing**)
[CONTENTOPTIMIZER_COMPONENTSTORE_SHARED](#CONTENTOPTIMIZER_COMPONENTSTORE_SHARED) | Aktualisierungen des Komponentenspeichers

## Agentenkonsole {#agent-console}

{% alert note %}
Agentenkonsole-Tabellen sind nur in der Snowflake-Datenfreigabe verfügbar.
{% endalert %}

### AGENTCONSOLE_AGENTEXECUTED_SHARED {#AGENTCONSOLE_AGENTEXECUTED_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`invocation_id` | `string` | Global eindeutige ID für diese Nachricht
`request_id` | `string` | Eindeutige ID für diese gesamte LLM-Anfrage und vollständige Ausführung
`duration` | `int` | Dauer der Sitzung in Sekunden
`prompt_tokens` | `int` | Wie viele Prompt-Tokens diese Anfrage verbraucht hat
`completion_tokens` | `int` | Wie viele Completion-Tokens diese Anfrage verbraucht hat
`total_tokens` | `int` | Wie viele Tokens diese Anfrage insgesamt verbraucht hat
`cache_tokens` | `int` | Wie viele gecachte Tokens diese Anfrage verbraucht hat
`reasoning_tokens` | `int` | Wie viele Reasoning-Tokens diese Anfrage verbraucht hat
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`agent_id` | `string` | BSON-ID des CustomerDefinedAgent
`agent_name` | `string` | Name des CustomerDefinedAgent
`model_provider` | `string` | Name des LLM-Modellanbieters
`model_name` | `string` | Name des in dieser Anfrage verwendeten LLM-Modells
`provider_request_id` | `string` | Vom Modellanbieter für den API-Aufruf vergebene Anfrage-ID
`cache_hit` | `boolean` | Ob diese Anfrage den Cache getroffen hat, um die Antwort zurückzugeben
`llm_owned_by_customer` | `boolean` | Wenn true, wurde der API-Schlüssel der/des Kund:in verwendet; wenn false, wurde der Braze-Schlüssel verwendet
`is_error` | `boolean` | Ob diese Anfrage einen Fehler verursacht hat
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`user_id` | `string` | [PII] Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`input` | `null,`&nbsp;`string` | [PII] Eingabe an das LLM
`output` | `null,`&nbsp;`string` | [PII] Antwort vom LLM
`invocation_source` | `null,`&nbsp;`string` | Welches Ruby-Objekt die LLM-Anfrage ausgelöst hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Ereignis von der Snowpipe erfasst wurde
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`error` | `string` | Fehlername
`thinking_level` | `string` | Die für die Anfrage verwendete Denk-/Reasoning-Stufe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLEAGENTEXECUTEDSHARED #AGENTCONSOLEAGENTEXECUTEDSHARED" }

### AGENTCONSOLE_RAWLLMREQUEST_SHARED {#AGENTCONSOLE_RAWLLMREQUEST_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`invocation_id` | `string` | Global eindeutige ID für diese Nachricht
`request_id` | `string` | Eindeutige ID für diese gesamte LLM-Anfrage und vollständige Ausführung
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der dieses Ereignis gehört
`agent_id` | `string` | BSON-ID des CustomerDefinedAgent
`agent_name` | `string` | Name des CustomerDefinedAgent
`model_provider` | `string` | Name des LLM-Modellanbieters
`model_name` | `string` | Name des in dieser Anfrage verwendeten LLM-Modells
`duration` | `int`,&nbsp;`null` | Dauer der Sitzung in Sekunden
`request` | `string` | [PII] In der Anfrage verwendeter Prompt
`http_status_code` | `int`,&nbsp;`null` | HTTP-Statuscode der Antwort
`response_body` | `string`,&nbsp;`null` | [PII] Antwort vom LLM
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLERAWLLMREQUESTSHARED #AGENTCONSOLERAWLLMREQUESTSHARED" }

### AGENTCONSOLE_TOOLINVOCATION_SHARED {#AGENTCONSOLE_TOOLINVOCATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`tool_call_id` | `string` | Global eindeutige ID für diesen Tool-Aufruf
`duration` | `int` | Dauer der Sitzung in Sekunden
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`agent_id` | `string` | BSON-ID des CustomerDefinedAgent
`agent_name` | `string` | Name des CustomerDefinedAgent
`is_error` | `boolean` | Ob diese Anfrage einen Fehler verursacht hat
`tool_name` | `string` | Name des Tools
`tool_arguments` | `null,`&nbsp;`string` | [PII] JSON der Tool-Argumente
`invocation_source` | `null,`&nbsp;`string` | Welches Ruby-Objekt die LLM-Anfrage ausgelöst hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Ereignis von der Snowpipe erfasst wurde
`request_id` | `string` | Eindeutige ID für diese gesamte LLM-Anfrage und vollständige Ausführung
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="AGENTCONSOLETOOLINVOCATIONSHARED #AGENTCONSOLETOOLINVOCATIONSHARED" }

## Nutzerprofil-Attributansichten {#user-profile-attribute-views}

### USER_CUSTOM_ATTRIBUTES_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_id` | `string` | BSON-ID des Workspace
`app_id` | `string` | BSON-ID der App
`user_id` | `string` | [PII] Braze-Nutzer-ID
`time` | `int` | UNIX-Zeitstempel in Sekunden der Profilaktualisierung (bei nachträglich aufgefüllten Zeilen der Zeitpunkt der Auffüllung)
`time_ms` | `int` | UNIX-Zeitstempel in Millisekunden der Profilaktualisierung (bei nachträglich aufgefüllten Zeilen der Zeitpunkt der Auffüllung)
`update_source` | `string` | Quelle der Profilaktualisierung
`sf_updated_at` | `timestamp` | Wann diese Zeile in Snowflake aktualisiert wurde
`custom_attributes` | `variant` | [PII] Angepasste Attribute als JSON-Objekt
`archived` | `boolean` | Ob das Nutzerprofil archiviert ist
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED #USERCUSTOMATTRIBUTESVIEWSHARED" }

### USER_DEFAULT_ATTRIBUTES_VIEW_SHARED {#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_id` | `string` | BSON-ID des Workspace
`app_id` | `string` | BSON-ID der App
`user_id` | `string` | [PII] Braze-Nutzer-ID
`time` | `int` | UNIX-Zeitstempel in Sekunden der Profilaktualisierung (bei nachträglich aufgefüllten Zeilen der Zeitpunkt der Auffüllung)
`time_ms` | `int` | UNIX-Zeitstempel in Millisekunden der Profilaktualisierung (bei nachträglich aufgefüllten Zeilen der Zeitpunkt der Auffüllung)
`update_source` | `string` | Quelle der Profilaktualisierung
`sf_updated_at` | `timestamp` | Wann diese Zeile in Snowflake aktualisiert wurde
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`first_name` | `string` | [PII] Vorname
`last_name` | `string` | [PII] Nachname
`email_address` | `string` | [PII] E-Mail-Adresse
`gender` | `string` | [PII] Geschlecht
`phone_number` | `string` | [PII] Telefonnummer
`dob` | `string` | [PII] Geburtsdatum
`TIME_ZONE` | `string` | [PII] Zeitzone
`home_city` | `string` | [PII] Wohnort
`country` | `string` | [PII] Land
`language` | `string` | [PII] Sprache
`archived` | `boolean` | Ob das Nutzerprofil archiviert ist
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED #USERDEFAULTATTRIBUTESVIEWSHARED" }

### USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED {#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_id` | `string` | BSON-ID des Workspace
`user_id` | `string` | [PII] Braze-Nutzer-ID
`app_id` | `string` | BSON-ID der App
`time` | `int` | UNIX-Zeitstempel in Sekunden der Profilaktualisierung (bei nachträglich aufgefüllten Zeilen der Zeitpunkt der Auffüllung)
`time_ms` | `int` | UNIX-Zeitstempel in Millisekunden der Profilaktualisierung (bei nachträglich aufgefüllten Zeilen der Zeitpunkt der Auffüllung)
`update_source` | `string` | Quelle der Profilaktualisierung
`sf_updated_at` | `timestamp` | Wann diese Zeile in Snowflake aktualisiert wurde
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`first_name` | `string` | [PII] Vorname
`last_name` | `string` | [PII] Nachname
`email_address` | `string` | [PII] E-Mail-Adresse
`gender` | `string` | [PII] Geschlecht
`phone_number` | `string` | [PII] Telefonnummer
`dob` | `string` | [PII] Geburtsdatum
`TIME_ZONE` | `string` | [PII] Zeitzone
`home_city` | `string` | [PII] Wohnort
`country` | `string` | [PII] Land
`language` | `string` | [PII] Sprache
`eff_dt` | `timestamp` | Beginn des Intervalls, in dem dieser Attributstatus aktuell war
`end_dt` | `timestamp` | Ende dieses Intervalls
`archived` | `boolean` | Ob das Nutzerprofil archiviert ist
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED #USERDEFAULTATTRIBUTESHISTORYVIEWSHARED" }

### USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED {#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_id` | `string` | BSON-ID des Workspace
`app_id` | `string` | BSON-ID der App
`user_id` | `string` | [PII] Braze-Nutzer-ID
`time` | `int` | UNIX-Zeitstempel in Sekunden der Profilaktualisierung (bei nachträglich aufgefüllten Zeilen der Zeitpunkt der Auffüllung)
`time_ms` | `int` | UNIX-Zeitstempel in Millisekunden der Profilaktualisierung (bei nachträglich aufgefüllten Zeilen der Zeitpunkt der Auffüllung)
`update_source` | `string` | Quelle der Profilaktualisierung
`sf_updated_at` | `timestamp` | Wann diese Zeile in Snowflake aktualisiert wurde
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`first_name` | `string` | [PII] Vorname
`last_name` | `string` | [PII] Nachname
`email_address` | `string` | [PII] E-Mail-Adresse
`gender` | `string` | [PII] Geschlecht
`phone_number` | `string` | [PII] Telefonnummer
`dob` | `string` | [PII] Geburtsdatum
`home_city` | `string` | [PII] Wohnort
`country` | `string` | [PII] Land
`language` | `string` | [PII] Sprache
`TIME_ZONE` | `string` | [PII] Zeitzone
`archived` | `boolean` | Ob das Nutzerprofil archiviert ist
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED #USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED" }

### USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="history" %}

Hinweise zur Verwendung und Beispielabfragen finden Sie unter [Snowflake-Nutzerattribute]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#historical-change-logs).

### USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED {#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="latest" %}

Hinweise zur Verwendung und Beispielabfragen finden Sie unter [Snowflake-Nutzerattribute]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#real-time-user-profile-views).

### USER_DEFAULT_ATTRIBUTES_HISTORY_RAW_VIEW_SHARED {#USER_DEFAULT_ATTRIBUTES_HISTORY_RAW_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Feld | Typ | Beschreibung
------|------|------------
`user_id` | `string` | [PII] Braze-Nutzer-ID
`app_group_id` | `string` | BSON-ID des Workspace
`app_id` | `string` | BSON-ID der App
`update_source` | `string` | Quelle der Profilaktualisierung
`time` | `int` | UNIX-Zeitstempel in Sekunden der Profilaktualisierung
`archived` | `boolean` | Ob das Nutzerprofil archiviert ist
`sf_updated_at` | `timestamp` | Wann diese Zeile in Snowflake aktualisiert wurde
`first_name` | `string` | [PII] Vorname
`last_name` | `string` | [PII] Nachname
`gender` | `string` | [PII] Geschlecht
`dob` | `string` | [PII] Geburtsdatum
`home_city` | `string` | [PII] Wohnort
`country` | `string` | [PII] Land
`language` | `string` | [PII] Sprache
`eff_dt` | `timestamp` | Beginn des Intervalls, in dem dieser Attributstatus aktuell war
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERDEFAULTATTRIBUTESHISTORYRAWVIEWSHARED #USERDEFAULTATTRIBUTESHISTORYRAWVIEWSHARED" }

### USER_CUSTOM_ATTRIBUTES_HISTORY_RAW_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_HISTORY_RAW_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Feld | Typ | Beschreibung
------|------|------------
`user_id` | `string` | [PII] Braze-Nutzer-ID
`app_group_id` | `string` | BSON-ID des Workspace
`app_id` | `string` | BSON-ID der App
`update_source` | `string` | Quelle der Profilaktualisierung
`time` | `int` | UNIX-Zeitstempel in Sekunden der Profilaktualisierung
`archived` | `boolean` | Ob das Nutzerprofil archiviert ist
`sf_updated_at` | `timestamp` | Wann diese Zeile in Snowflake aktualisiert wurde
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`custom_attributes` | `variant` | [PII] Angepasste Attribute als JSON-Objekt
`eff_dt` | `timestamp` | Beginn des Intervalls, in dem dieser Attributstatus aktuell war
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESHISTORYRAWVIEWSHARED #USERCUSTOMATTRIBUTESHISTORYRAWVIEWSHARED" }

## Kataloge {#catalogs}

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`catalog_id` | `string` | BSON-ID des Katalogs
`item_id` | `string` | BSON-ID des Katalogartikels
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe
`field_name` | `null,`&nbsp;`string` | Name des Felds
`field_value` | `null,`&nbsp;`string` | Wert des Felds
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CATALOGSITEMSSHARED #CATALOGSITEMSSHARED" }

## Changelogs {#changelogs}

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattgefunden hat
`random_bucket_number` | `null, int` | Neue zufällige Bucket-Nummer
`global_control_group` | `null, boolean` | Mit dieser Änderung ist die Bucket-Nummer in der globalen Kontrollgruppe enthalten
`previous_global_control_group` | `null, boolean` | Vor dieser Änderung war die Bucket-Nummer in der globalen Kontrollgruppe enthalten, ist es jetzt aber nicht mehr
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSGLOBALCONTROLGROUPSHARED #CHANGELOGSGLOBALCONTROLGROUPSHARED" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID der Campaign
`name` | `null,`&nbsp;`string` | Name der Campaign
`conversion_behaviors` | `null,`&nbsp;`string` | Konversions-Verhalten für die Campaign
`actions` | `null,`&nbsp;`string` | Aktionen für die Campaign
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCAMPAIGNSHARED #CHANGELOGSCAMPAIGNSHARED" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID des Canvas
`name` | `null,`&nbsp;`string` | Name des Canvas
`conversion_behaviors` | `null,`&nbsp;`string` | Konversions-Verhalten für das Canvas
`variations` | `null,`&nbsp;`string` | Variationen für das Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCANVASSHARED #CHANGELOGSCANVASSHARED" }

## Verhaltensweisen {#behaviors}

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die das Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Aktion stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in das Ereignis ausgeführt hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das angepasste Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`name` | `string` | Name des angepassten Ereignisses
`properties` | `string` | Angepasste Eigenschaften des Ereignisses, gespeichert als JSON-codierter String
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSCUSTOMEVENTSHARED #USERSBEHAVIORSCUSTOMEVENTSHARED" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die die Installation durchgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn sie anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in die Installation durchgeführt hat
`source` | `string` | Quelle der Attribution
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSINSTALLATTRIBUTIONSHARED #USERSBEHAVIORSINSTALLATTRIBUTIONSHARED" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die den Standort aufzeichnet
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieser Standort aufgezeichnet wurde
`time` | `int` | Unix-Zeitstempel, zu dem der Standort aufgezeichnet wurde
`latitude` | `float` | [PII] Breitengrad des aufgezeichneten Standorts
`longitude` | `float` | [PII] Längengrad des aufgezeichneten Standorts
`altitude` | `null, float` | [PII] Höhe des aufgezeichneten Standorts
`ll_accuracy` | `null, float` | Genauigkeit von Breiten- und Längengrad des aufgezeichneten Standorts
`alt_accuracy` | `null, float` | Höhengenauigkeit des aufgezeichneten Standorts
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem der Standort aufgezeichnet wurde
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das bei der Standortaufzeichnung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLOCATIONSHARED #USERSBEHAVIORSLOCATIONSHARED" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die einen Kauf getätigt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der der Kauf stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in den Kauf getätigt hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem der Kauf stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Kaufs verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`product_id` | `string` | ID des gekauften Produkts
`price` | `float` | Preis des Kaufs
`currency` | `string` | Währung des Kaufs
`properties` | `string` | Angepasste Eigenschaften des Kaufs, gespeichert als JSON-codierter String
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPURCHASESHARED #USERSBEHAVIORSPURCHASESHARED" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die die Deinstallation durchgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn sie anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, die deinstalliert wurde
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in die Deinstallation durchgeführt hat
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUNINSTALLSHARED #USERSBEHAVIORSUNINSTALLSHARED" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die die App aktualisiert hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, die die Nutzer:in aktualisiert hat
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in die App aktualisiert hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Nutzer:in die App aktualisiert hat
`sdk_version` | `null,`&nbsp;`string` | Version des verwendeten Braze SDK
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`old_app_version` | `null,`&nbsp;`string` | Alte Version der App
`new_app_version` | `null,`&nbsp;`string` | Neue Version der App
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUPGRADEDAPPSHARED #USERSBEHAVIORSUPGRADEDAPPSHARED" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die diese Aktion ausführt
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Sitzung stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Sitzung gestartet wurde
`session_id` | `string` | UUID der Sitzung
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Sitzung stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während der Sitzung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPFIRSTSESSIONSHARED #USERSBEHAVIORSAPPFIRSTSESSIONSHARED" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED #USERSBEHAVIORSAPPNEWSFEEDIMPRESSIONSHARED" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die diese Aktion ausführt
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Sitzung stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Sitzung endete
`duration` | `null, float` | Dauer der Sitzung in Sekunden
`session_id` | `string` | UUID der Sitzung
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Sitzung stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während der Sitzung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONENDSHARED #USERSBEHAVIORSAPPSESSIONENDSHARED" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die diese Aktion ausführt
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Sitzung stattfand
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem die Sitzung gestartet wurde
`session_id` | `string` | UUID der Sitzung
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Sitzung stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während der Sitzung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONSTARTSHARED #USERSBEHAVIORSAPPSESSIONSTARTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die das Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Aktion stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in das Ereignis ausgeführt hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das angepasste Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`event_type` | `string` | Art des ausgelösten Geofence-Ereignisses (z. B. „enter“ oder „exit“)
`location_set_id` | `string` | ID des Standort-Sets des ausgelösten Geofence
`geofence_id` | `string` | ID des ausgelösten Geofence
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCEDATAEVENTSHARED #USERSBEHAVIORSGEOFENCEDATAEVENTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die das Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Aktion stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in das Ereignis ausgeführt hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das angepasste Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`event_type` | `string` | Art des ausgelösten Geofence-Ereignisses (z. B. „enter“ oder „exit“)
`location_set_id` | `string` | ID des Standort-Sets des ausgelösten Geofence
`geofence_id` | `string` | ID des ausgelösten Geofence
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCERECORDEVENTSHARED #USERSBEHAVIORSGEOFENCERECORDEVENTSHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`activity_attributes_type` | `null,`&nbsp;`string` | Attributtyp der Live Activity
`push_to_start_token` | `null,`&nbsp;`string` | Push-to-Start-Token der Live Activity
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS-Push-Token, 1 für Entwicklung, 2 für Produktion
`push_token_state_change_type` | `null,`&nbsp;`string` | Beschreibung des Typs der Push-Token-Statusänderung
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`activity_id` | `null,`&nbsp;`string` | Live-Activity-Bezeichner
`update_token` | `null,`&nbsp;`string` | Update-Token der Live Activity
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS-Push-Token, 1 für Entwicklung, 2 für Produktion
`push_token_state_change_type` | `null,`&nbsp;`string` | Beschreibung des Typs der Push-Token-Statusänderung
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`time_ms` | `int` | Zeit in Millisekunden, zu der das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`push_token` | `null,`&nbsp;`string` | Push-Token des Ereignisses
`push_token_created_at` | `null, int` | UNIX-Zeitstempel, zu dem das Push-Token erstellt wurde
`push_token_updated_at` | `null, int` | UNIX-Zeitstempel, zu dem das Push-Token zuletzt aktualisiert wurde
`push_token_foreground_push_disabled` | `null, boolean` | Flag, ob Vordergrund-Push für das Push-Token deaktiviert ist
`push_token_device_id` | `null,`&nbsp;`string` | Geräte-ID des Push-Tokens
`push_token_provisionally_opted_in` | `null, boolean` | Flag, ob das Push-Token vorläufig aktiviert ist
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS-Push-Token, 1 für Entwicklung, 2 für Produktion
`web_push_token_public_key` | `null,`&nbsp;`string` | Public Key des Push-Tokens, gilt nur für Web-Push-Token
`web_push_token_user_auth` | `null,`&nbsp;`string` | Nutzer-Authentifizierung des Push-Tokens, gilt nur für Web-Push-Token
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | VAPID-Public-Key des Push-Tokens, gilt nur für Web-Push-Token
`push_token_state_change_type` | `null,`&nbsp;`string` | Beschreibung des Typs der Push-Token-Statusänderung
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED #USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der betroffenen Nutzer:in
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der Nutzer:in
`state_change_source` | `null,`&nbsp;`string` | Quelle der Statusänderung (REST, SDK, Dashboard usw.)
`subscription_status` | `string` | Abo-Status: „Subscribed“, „Unsubscribed“ oder „Opted In“
`channel` | `null,`&nbsp;`string` | Kanal des globalen Abo-Status, z. B. E-Mail
`time` | `int` | Unix-Zeitstempel, zu dem sich der Abo-Status geändert hat
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, zu der das Ereignis gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, zu der dieses Ereignis gehört
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, von der diese Abo-Statusänderung ausging
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`channel_identifier` | `null,`&nbsp;`string` | [PII] Bezeichner der Nutzer:in auf dem Kanal, für den das Ereignis bestimmt ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der betroffenen Nutzer:in
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn sie anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der Nutzer:in
`phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Nutzer:in im E.164-Format
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, zu der das Ereignis gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, zu der dieses Ereignis gehört
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`channel` | `null,`&nbsp;`string` | Kanal: „email“ oder „sms“, abhängig vom Kanaltyp der Abo-Gruppe
`subscription_status` | `string` | Abo-Status: „Subscribed“, „Unsubscribed“ oder „Opted In“
`time` | `int` | Unix-Zeitstempel, zu dem sich der Abo-Status geändert hat
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, von der diese Abo-Statusänderung ausging
`state_change_source` | `null,`&nbsp;`string` | Quelle der Statusänderung (REST, SDK, Dashboard usw.)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`channel_identifier` | `null,`&nbsp;`string` | [PII] Bezeichner der Nutzer:in auf dem Kanal, für den das Ereignis bestimmt ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED" }

## Campaigns {#campaigns}

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese/r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese/r Nutzer:in erhalten hat
`conversion_behavior_index` | `null, int` | Index des Konversionsverhaltens
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese/r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`conversion_behavior` | `string` | JSON-codierter String, der das Konversionsverhalten beschreibt
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSCONVERSIONSHARED #USERSCAMPAIGNSCONVERSIONSHARED" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese/r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese/r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese/r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSENROLLINCONTROLSHARED #USERSCAMPAIGNSENROLLINCONTROLSHARED" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese/r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese/r Nutzer:in erhalten hat
`channel` | `null,`&nbsp;`string` | Kanal, zu dem dieses Ereignis gehört
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese/r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSFREQUENCYCAPSHARED #USERSCAMPAIGNSFREQUENCYCAPSHARED" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese/r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese/r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`revenue` | `long` | Umsatzbetrag in USD-Cent
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese/r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSREVENUESHARED #USERSCAMPAIGNSREVENUESHARED" }

## Canvas {#canvas}

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Feld                                   | Typ                      | Beschreibung                                                                                                     |
| -------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                                                         |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID der Person, die dieses Ereignis ausgeführt hat                                                          |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID der Person                                                                                      |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das dieser Person zugeordnet ist, falls die Person anonym ist                                     |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese Person gehört                                                               |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese Person gehört                                                                 |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                                                            |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört                        |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                                                 |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                                                        |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                                                        |
| `progression_type`                     | `string`,&nbsp;`null`    | Typ des Schrittfortschritts-Ereignisses                                                                          |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | Ob dies der Eintritt in einen ersten Schritt in einem Canvas ist                                                 |
| `exit_reason`                          | `string`,&nbsp;`null`    | Falls dies ein Exit ist, der Grund, warum die Person den Canvas während des Schritts verlassen hat               |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | Eindeutiger Bezeichner für diese Instanz einer Person in einem Canvas                                            |
| `next_step_id`                         | `string`,&nbsp;`null`    | BSON-ID des nächsten Schritts im Canvas                                                                          |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | API-ID des nächsten Schritts im Canvas                                                                           |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                                                 |
| `canvas_name` | `string` | Name des Canvas |
| `canvas_variation_name` | `string` | Name der Canvas-Variante, die diese Person erhalten hat |
| `canvas_step_name` | `string` | Name des Canvas-Schritts |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASSTEPPROGRESSIONSHARED #USERSCANVASSTEPPROGRESSIONSHARED" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Feld                                   | Typ                      | Beschreibung                                                                                                                               |
| -------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                                   | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                                                                                   |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID der Person, die dieses Ereignis ausgeführt hat                                                                                    |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID der Person                                                                                                                |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das dieser Person zugeordnet ist, falls die Person anonym ist                                                               |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese Person gehört                                                                                         |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese Person gehört                                                                                           |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                                                                                      |
| `app_api_id`                           | `string`,&nbsp;`null`    | API-ID der App, in der dieses Ereignis aufgetreten ist                                                                                     |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört                                                  |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                                                                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                                                                                  |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                                                                                  |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Person erhalten hat                                                               |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | Typ des Konversions-Events, das die Person ausgeführt hat, wobei „0“ eine primäre Konversion und „1“ eine sekundäre Konversion bedeutet    |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Geschlecht der Person                                                                                                                |
| `country`                              | `string`,&nbsp;`null`    | [PII] Land der Person                                                                                                                      |
| `timezone`                             | `string`,&nbsp;`null`    | Zeitzone der Person                                                                                                                        |
| `language`                             | `string`,&nbsp;`null`    | [PII] Sprache der Person                                                                                                                   |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                                                                           |
| `canvas_name` | `string` | Name des Canvas |
| `canvas_variation_name` | `string` | Name der Canvas-Variante, die diese Person erhalten hat |
| `canvas_step_name` | `string` | Name des Canvas-Schritts |
| `conversion_behavior` | `string` | JSON-kodierter String, der das Konversionsverhalten beschreibt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASCONVERSIONSHARED #USERSCANVASCONVERSIONSHARED" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Feld                      | Typ                      | Beschreibung                                                                       |
| ------------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                           |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID der Person, die dieses Ereignis ausgeführt hat                            |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID der Person                                                        |
| `device_id`               | `string`,&nbsp;`null`    | ID des Geräts, das dieser Person zugeordnet ist, falls die Person anonym ist       |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese Person gehört                                 |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese Person gehört                                   |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                              |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                   |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                          |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [Veraltet] API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört               |
| `gender`                  | `string`,&nbsp;`null`    | [PII] Geschlecht der Person                                                        |
| `country`                 | `string`,&nbsp;`null`    | [PII] Land der Person                                                              |
| `timezone`                | `string`,&nbsp;`null`    | Zeitzone der Person                                                                |
| `language`                | `string`,&nbsp;`null`    | [PII] Sprache der Person                                                           |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Wahr, wenn die Person in die Kontrollgruppe aufgenommen wurde                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                   |
| `canvas_name` | `string` | Name des Canvas |
| `canvas_variation_name` | `string` | Name der Canvas-Variante, die diese Person erhalten hat |
| `canvas_step_name` | `string` | Name des Canvas-Schritts |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASENTRYSHARED #USERSCANVASENTRYSHARED" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Feld                      | Typ                      | Beschreibung                                                                       |
| ------------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                           |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID der Person, die dieses Ereignis ausgeführt hat                            |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID der Person                                                        |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese Person gehört                                 |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese Person gehört                                   |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                              |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                   |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                          |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                          |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                   |
| `canvas_name` | `string` | Name des Canvas |
| `canvas_variation_name` | `string` | Name der Canvas-Variante, die diese Person erhalten hat |
| `canvas_step_name` | `string` | Name des Canvas-Schritts |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED #USERSCANVASEXITMATCHEDAUDIENCESHARED" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Feld                      | Typ                      | Beschreibung                                                                       |
| ------------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                           |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID der Person, die dieses Ereignis ausgeführt hat                            |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID der Person                                                        |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese Person gehört                                 |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese Person gehört                                   |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                              |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                   |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                          |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                          |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                   |
| `canvas_name` | `string` | Name des Canvas |
| `canvas_variation_name` | `string` | Name der Canvas-Variante, die diese Person erhalten hat |
| `canvas_step_name` | `string` | Name des Canvas-Schritts |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITPERFORMEDEVENTSHARED #USERSCANVASEXITPERFORMEDEVENTSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Feld                        | Typ                      | Beschreibung                                                                                                                               |
| --------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                        | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                                                                                   |
| `user_id`                   | `string`,&nbsp;`null`    | Braze-ID der Person, die dieses Ereignis ausgeführt hat                                                                                    |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] Externe ID der Person                                                                                                                |
| `app_group_id`              | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese Person gehört                                                                                         |
| `time`                      | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                                                                                      |
| `app_api_id`                | `string`,&nbsp;`null`    | API-ID der App, in der dieses Ereignis aufgetreten ist                                                                                     |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört                                                  |
| `canvas_api_id`             | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                                                                           |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                                                                                  |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                                                                                  |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | API-ID des Experiment-Schritts, zu dem dieses Ereignis gehört                                                                              |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | Typ des Konversions-Events, das die Person ausgeführt hat, wobei „0“ eine primäre Konversion und „1“ eine sekundäre Konversion bedeutet    |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                                                                           |
| `experiment_split_api_id` | `string`,&nbsp;`null` | API-ID des Experiment-Splits, in den die Person aufgenommen wurde |
| `canvas_name` | `string` | Name des Canvas |
| `canvas_variation_name` | `string` | Name der Canvas-Variante, die diese Person erhalten hat |
| `canvas_step_name` | `string` | Name des Canvas-Schritts |
| `experiment_split_name` | `string` | Name des Experiment-Splits |
| `conversion_behavior` | `string` | JSON-kodierter String, der das Konversionsverhalten beschreibt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED #USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Feld                      | Typ                      | Beschreibung                                                                       |
| ------------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                           |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID der Person, die dieses Ereignis ausgeführt hat                            |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID der Person                                                        |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese Person gehört                                 |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                              |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                   |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                          |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                          |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | API-ID des Experiment-Schritts, zu dem dieses Ereignis gehört                      |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Wahr, wenn die Person in die Kontrollgruppe aufgenommen wurde                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                   |
| `experiment_split_api_id` | `string` | API-ID des Experiment-Splits, in den die Person aufgenommen wurde |
| `canvas_name` | `string` | Name des Canvas |
| `canvas_variation_name` | `string` | Name der Canvas-Variante, die diese Person erhalten hat |
| `canvas_step_name` | `string` | Name des Canvas-Schritts |
| `experiment_split_name` | `string` | Name des Experiment-Splits |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

| `experiment_split_api_id` | `string`,&nbsp;`null` | API-ID des Experiment-Splits, in den die Person aufgenommen wurde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED #USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Feld                                   | Typ                      | Beschreibung                                                                       |
| -------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                           |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID der Person, die dieses Ereignis ausgeführt hat                            |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID der Person                                                        |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das dieser Person zugeordnet ist, falls die Person anonym ist       |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese Person gehört                                 |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese Person gehört                                   |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                              |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                   |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                          |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                          |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Person erhalten hat       |
| `channel`                              | `string`,&nbsp;`null`    | Messaging-Kanal, zu dem dieses Ereignis gehört (E-Mail, Push usw.)                 |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Geschlecht der Person                                                        |
| `country`                              | `string`,&nbsp;`null`    | [PII] Land der Person                                                              |
| `timezone`                             | `string`,&nbsp;`null`    | Zeitzone der Person                                                                |
| `language`                             | `string`,&nbsp;`null`    | [PII] Sprache der Person                                                           |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASFREQUENCYCAPSHARED #USERSCANVASFREQUENCYCAPSHARED" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Feld                                   | Typ                      | Beschreibung                                                                       |
| -------------------------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                           |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID der Person, die dieses Ereignis ausgeführt hat                            |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID der Person                                                        |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das dieser Person zugeordnet ist, falls die Person anonym ist       |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese Person gehört                                 |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese Person gehört                                   |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                              |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                   |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                          |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                          |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Person erhalten hat       |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Geschlecht der Person                                                        |
| `country`                              | `string`,&nbsp;`null`    | [PII] Land der Person                                                              |
| `timezone`                             | `string`,&nbsp;`null`    | Zeitzone der Person                                                                |
| `language`                             | `string`,&nbsp;`null`    | [PII] Sprache der Person                                                           |
| `revenue`                              | `int`,&nbsp;`null`       | Höhe des erzielten Umsatzes in USD, angegeben in Cent                              |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                   |
| `app_api_id` | `string`,&nbsp;`null` | API-ID der App, in der dieses Ereignis aufgetreten ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASREVENUESHARED #USERSCANVASREVENUESHARED" }

### USERS_CANVAS_COSTEP_CONVERSION_SHARED {#USERS_CANVAS_COSTEP_CONVERSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese Person gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese Person gehört
`external_user_id` | `string` | [PII] Externe ID der Person
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | [PII] Braze-ID der Person, die dieses Ereignis ausgeführt hat
`dispatch_id` | `string` | ID des Versands, zu dem diese Nachricht gehört
`channel` | `string` | Kanal, zu dem dieses Ereignis gehört
`conversion_type` | `string` | Typ der Konversion (Öffnung oder Klick)
`combination_token` | `string` | Zugewiesene Komponentenkombination
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASCOSTEPCONVERSIONSHARED #USERSCANVASCOSTEPCONVERSIONSHARED" }

### USERS_CANVAS_COSTEP_SEND_SHARED {#USERS_CANVAS_COSTEP_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese Person gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese Person gehört
`external_user_id` | `string` | [PII] Externe ID der Person
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | [PII] Braze-ID der Person, die dieses Ereignis ausgeführt hat
`dispatch_id` | `string` | ID des Versands, zu dem diese Nachricht gehört
`channel` | `string` | Kanal, zu dem dieses Ereignis gehört
`canvas_id` | `string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`content_optimizer_step_id` | `string` | Interne ID des CO-Schritts
`combination_token` | `string` | Zugewiesene Komponentenkombination
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASCOSTEPSENDSHARED #USERSCANVASCOSTEPSENDSHARED" }

## Nachrichten {#messages}


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts – aus dem user_agent extrahiert –, in dem das Öffnen stattfand
`ad_id` | `null,`&nbsp;`string` | [PII] Werbekennung
`ad_id_type` | `null,`&nbsp;`string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`abort_type` | `null,`&nbsp;`string` | Typ des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (bis zu 128 Zeichen)
`banner_placement_id` | `null,`&nbsp;`string` | Vom Kunden festgelegte Banner-Platzierungs-ID
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_id` | `string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `string` | Name des Canvas
`canvas_step_name` | `string` | Name des Canvas-Schritts
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERABORTSHARED #USERSMESSAGESBANNERABORTSHARED" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts – aus dem user_agent extrahiert –, in dem das Öffnen stattfand
`button_id` | `null,`&nbsp;`string` | ID des angeklickten Buttons, wenn dieser Klick einen Klick auf einen Button darstellt
`ad_id` | `null,`&nbsp;`string` | [PII] Werbekennung
`ad_id_type` | `null,`&nbsp;`string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`banner_placement_id` | `null,`&nbsp;`string` | Vom Kunden festgelegte Banner-Platzierungs-ID
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_id` | `string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `string` | Name des Canvas
`canvas_step_name` | `string` | Name des Canvas-Schritts
`canvas_step_message_variation_api_id` | `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`is_unique` | `boolean` | Ob dieses Ereignis bei der Verarbeitung als 7-Tage-eindeutig gewertet wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERCLICKSHARED #USERSMESSAGESBANNERCLICKSHARED" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts – aus dem user_agent extrahiert –, in dem das Öffnen stattfand
`ad_id` | `null,`&nbsp;`string` | [PII] Werbekennung
`ad_id_type` | `null,`&nbsp;`string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`banner_placement_id` | `null,`&nbsp;`string` | Vom Kunden festgelegte Banner-Platzierungs-ID
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_id` | `string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `string` | Name des Canvas
`canvas_step_name` | `string` | Name des Canvas-Schritts
`canvas_step_message_variation_api_id` | `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`is_unique` | `boolean` | Ob dieses Ereignis bei der Verarbeitung als 7-Tage-eindeutig gewertet wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERIMPRESSIONSHARED #USERSMESSAGESBANNERIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`abort_type` | `null,`&nbsp;`string` | Typ des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDABORTSHARED #USERSMESSAGESCONTENTCARDABORTSHARED" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`content_card_id` | `string` | ID der Card, die dieses Ereignis generiert hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbekennung
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`is_unique` | `boolean` | Ob dieses Ereignis bei der Verarbeitung als 7-Tage-eindeutig gewertet wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDCLICKSHARED #USERSMESSAGESCONTENTCARDCLICKSHARED" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`content_card_id` | `string` | ID der Card, die dieses Ereignis generiert hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbekennung
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`is_unique` | `boolean` | Ob dieses Ereignis bei der Verarbeitung als 7-Tage-eindeutig gewertet wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDDISMISSSHARED #USERSMESSAGESCONTENTCARDDISMISSSHARED" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`content_card_id` | `string` | ID der Card, die dieses Ereignis generiert hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbekennung
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`is_unique` | `boolean` | Ob dieses Ereignis bei der Verarbeitung als 7-Tage-eindeutig gewertet wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDIMPRESSIONSHARED #USERSMESSAGESCONTENTCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`content_card_id` | `string` | ID der Card, die dieses Ereignis generiert hat
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDSENDSHARED #USERSMESSAGESCONTENTCARDSENDSHARED" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`abort_type` | `null,`&nbsp;`string` | Typ des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`message_extras` | `string` | [PII] JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILABORTSHARED #USERSMESSAGESEMAILABORTSHARED" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, über die der E-Mail-Versand erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`bounce_reason` | `null,`&nbsp;`string` | [PII] SMTP-Fehlercode und benutzerfreundliche Nachricht, die für dieses Bounce-Ereignis empfangen wurde
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absenderdomain für die E-Mail
`is_drop` | `null, boolean` | Gibt an, dass dieses Ereignis als Drop-Ereignis gezählt wird
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`send_time` | `int` | Zeitpunkt des zugehörigen Sendeereignisses
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILBOUNCESHARED #USERSMESSAGESEMAILBOUNCESHARED" }

{% alert note %}
Es kann vorkommen, dass für eine:n Nutzer:in bei einem einzelnen Hard Bounce mehrere Zeilen angezeigt werden. Dies kann passieren, wenn Ereignisse asynchron verarbeitet werden oder wenn zugehörige Sendungen unterschiedliche `dispatch_id`-Werte haben. Berücksichtigen Sie bei der Deduplizierung oder Analyse von Exporten `dispatch_id`, `time` und `id` gemeinsam.
{% endalert %}

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`url` | `null,`&nbsp;`string` | URL, auf die die/der Nutzer:in geklickt hat
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem der Klick erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, aus dem der E-Mail-Versand erfolgte
`link_id` | `null,`&nbsp;`string` | Eindeutige ID für den angeklickten Link, wie von Braze erstellt
`link_alias` | `null,`&nbsp;`string` | Alias, der mit dieser Link-ID verknüpft ist
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`is_amp` | `null, boolean` | Gibt an, dass es sich um ein AMP-Ereignis handelt
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`suspected_bot_click_reason` | `null, object` | Warum dieses Ereignis als Bot klassifiziert wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`send_time` | `int` | Zeitpunkt des zugehörigen Sende-Ereignisses
`has_url_parameters` | `boolean` | Ob die angeklickte URL Abfrageparameter enthielt
`link_aliasing_enabled` | `boolean` | Ob Link Aliasing für den Workspace aktiviert war, als dieser Klick verarbeitet wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILCLICKSHARED #USERSMESSAGESEMAILCLICKSHARED" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der/des Nutzer:in
`recipient_domain` | `null,`&nbsp;`string` | E-Mail-Domain der/des Empfänger:in
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (Sparkpost oder Sendgrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, aus dem der E-Mail-Versand erfolgte
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der der E-Mail-Versand erfolgte
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`deferral_reason` | `null,`&nbsp;`string` | [PII] SMTP-Antwortcode und benutzerfreundliche Nachricht, die für dieses Zurückstellungs-Ereignis empfangen wurde
`attempt_count` | `null, int` | Anzahl der Zustellversuche für die Nachricht
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`send_time` | `int` | Zeitpunkt des zugehörigen Sende-Ereignisses
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDEFERRALSHARED #USERSMESSAGESEMAILDEFERRALSHARED" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der die E-Mail gesendet wurde
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, aus dem der E-Mail-Versand erfolgte
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`send_time` | `int` | Zeitpunkt des zugehörigen Sende-Ereignisses
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDELIVERYSHARED #USERSMESSAGESEMAILDELIVERYSHARED" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem der Spam-Bericht erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, aus dem der E-Mail-Versand erfolgte
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`send_time` | `int` | Zeitpunkt des zugehörigen Sende-Ereignisses
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILMARKASSPAMSHARED #USERSMESSAGESEMAILMARKASSPAMSHARED" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem die Öffnung erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, aus dem der E-Mail-Versand erfolgte
`machine_open` | `null,`&nbsp;`string` | Wird auf „true“ gesetzt, wenn das Öffnungs-Ereignis ohne Nutzerinteraktion ausgelöst wurde, z. B. durch ein Apple-Gerät mit aktiviertem E-Mail-Datenschutz (Mail Privacy Protection). Der Wert kann sich im Laufe der Zeit ändern, um eine feinere Granularität zu bieten.
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`is_amp` | `null, boolean` | Gibt an, dass es sich um ein AMP-Ereignis handelt
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`send_time` | `int` | Zeitpunkt des zugehörigen Sende-Ereignisses
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILOPENSHARED #USERSMESSAGESEMAILOPENSHARED" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, aus dem der E-Mail-Versand erfolgte
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSENDSHARED #USERSMESSAGESEMAILSENDSHARED" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der der E-Mail-Versand erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, aus dem der E-Mail-Versand erfolgte
`bounce_reason` | `null,`&nbsp;`string` | [PII] SMTP-Antwortcode und benutzerfreundliche Nachricht, die für dieses Bounce-Ereignis empfangen wurde
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`send_time` | `int` | Zeitpunkt des zugehörigen Sende-Ereignisses
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSOFTBOUNCESHARED #USERSMESSAGESEMAILSOFTBOUNCESHARED" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Diese Tabelle protokolliert E-Mail-Abmeldungen auf Nachrichtenebene seitens der/des Empfänger:in: Klick auf einen Abmelde-Link, Ein-Klick-List-Unsubscribe des E-Mail-Clients, Einreichungen über das Präferenzcenter und vom ESP gemeldete Abmeldungen. Über die REST API durchgeführte Abmeldungen sind nicht enthalten; diese erzeugen stattdessen [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events)- oder [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events)-Ereignisse.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, aus dem der E-Mail-Versand erfolgte
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILUNSUBSCRIBESHARED #USERSMESSAGESEMAILUNSUBSCRIBESHARED" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Ereignis tritt auf, wenn eine Nachricht de-priorisiert oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | [PII] Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`retry_type` | `null,`&nbsp;`string` | Art des Wiederholungsversuchs
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zum Wiederholungsversuch
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der/des Nutzer:in
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, aus dem der E-Mail-Versand erfolgte
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILRETRYSHARED #USERSMESSAGESEMAILRETRYSHARED" }

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`feature_flag_id_name` | `null,`&nbsp;`string` | Der Bezeichner des Feature-Flag-Rollouts
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`browser` | `null,`&nbsp;`string` | Gerätebrowser – aus dem User-Agent extrahiert – auf dem die Öffnung erfolgte
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die zum Zeitpunkt des Ereignisses verwendet wurde
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`canvas_name` | `string` | Name des Canvas
`canvas_step_name` | `string` | Name des Canvas-Schritts
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`message_variation_name` | `string` | Name der Nachrichtenvariante
`is_unique` | `boolean` | Ob dieses Ereignis bei der Verarbeitung als 7-Tage-eindeutig eingestuft wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED #USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die zum Zeitpunkt des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`version` | `string` | Welche Version der In-App-Nachricht, Legacy oder Triggered
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Identifikator
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEABORTSHARED #USERSMESSAGESINAPPMESSAGEABORTSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die zum Zeitpunkt des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`version` | `string` | Welche Version der In-App-Nachricht, Legacy oder Triggered
`button_id` | `null,`&nbsp;`string` | ID des angeklickten Buttons, wenn dieser Klick einen Klick auf einen Button darstellt
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Identifikator
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`dispatch_id` | `string` | ID des Versands, zu dem diese Nachricht gehört
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGECLICKSHARED #USERSMESSAGESINAPPMESSAGECLICKSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die zum Zeitpunkt des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`version` | `string` | Welche Version der In-App-Nachricht, Legacy oder Triggered
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Identifikator
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`locale_key` | `null,`&nbsp;`string` | [PII] Der Schlüssel, der den verwendeten Übersetzungen entspricht (z. B. „en-us“), mit denen diese Nachricht erstellt wurde (null für Standard).
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`dispatch_id` | `string` | ID des Versands, zu dem diese Nachricht gehört
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED #USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (bis zu 128 Zeichen)
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die bzw. von der die Nachricht gesendet/empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den bzw. von dem die Nachricht gesendet/empfangen wurde
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der bzw. an die die Nachricht gesendet/empfangen wurde
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`message_extras` | `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEABORTSHARED #USERSMESSAGESLINEABORTSHARED" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der bzw. an die die Nachricht gesendet/empfangen wurde
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die bzw. von der die Nachricht gesendet/empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den bzw. von dem die Nachricht gesendet/empfangen wurde
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`short_url` | `null,`&nbsp;`string` | Gekürzte URL, auf die geklickt wurde
`url` | `null,`&nbsp;`string` | URL, auf die die/der Nutzer:in geklickt hat
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem der Spam-Bericht erfolgte
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINECLICKSHARED #USERSMESSAGESLINECLICKSHARED" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die bzw. von der die Nachricht gesendet/empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den bzw. von dem die Nachricht gesendet/empfangen wurde
`media_id` | `null,`&nbsp;`string` | Die von LINE generierte ID, die zum Abrufen eingehender Medien von LINE verwendet werden kann
`message_body` | `null,`&nbsp;`string` | Eingegebene Antwort der/des Nutzer:in
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der bzw. an die die Nachricht gesendet/empfangen wurde
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEINBOUNDRECEIVESHARED #USERSMESSAGESLINEINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgelöst hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die bzw. von der die Nachricht gesendet/empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den bzw. von dem die Nachricht gesendet/empfangen wurde
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der bzw. an die die Nachricht gesendet/empfangen wurde
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINESENDSHARED #USERSMESSAGESLINESENDSHARED" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Ereignis tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungszeitfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | [PII] Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`retry_type` | `null,`&nbsp;`string` | Art des Wiederholungsversuchs
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zum Wiederholungsversuch
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattgefunden hat
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der die Nachricht gesendet oder empfangen wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINERETRYSHARED #USERSMESSAGESLINERETRYSHARED" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`activity_id` | `null,`&nbsp;`string` | Live-Activity-Bezeichner
`activity_attributes_type` | `null,`&nbsp;`string` | Live-Activity-Attributtyp
`push_to_start_token` | `null,`&nbsp;`string` | Push-to-Start-Token der Live Activity
`update_token` | `null,`&nbsp;`string` | Update-Token der Live Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Ereignistyp der Live Activity. Einer von ['start', 'update', 'end']
`live_activity_event_outcome` | `null,`&nbsp;`string` | Ergebnis des Live-Activity-Ereignisses
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis stattgefunden hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYOUTCOMESHARED #USERSMESSAGESLIVEACTIVITYOUTCOMESHARED" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`activity_id` | `null,`&nbsp;`string` | Live-Activity-Bezeichner
`activity_attributes_type` | `null,`&nbsp;`string` | Live-Activity-Attributtyp
`push_to_start_token` | `null,`&nbsp;`string` | Push-to-Start-Token der Live Activity
`update_token` | `null,`&nbsp;`string` | Update-Token der Live Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Ereignistyp der Live Activity. Einer von ['start', 'update', 'end']
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis stattgefunden hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYSENDSHARED #USERSMESSAGESLIVEACTIVITYSENDSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis stattgefunden hat
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattgefunden hat
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Betriebssystemversion des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Gerätebrowser – extrahiert aus user_agent –, in dem das Öffnen stattfand
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (bis zu 128 Zeichen)
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDABORTSHARED #USERSMESSAGESNEWSFEEDCARDABORTSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis stattgefunden hat
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattgefunden hat
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Betriebssystemversion des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Gerätebrowser – extrahiert aus user_agent –, in dem das Öffnen stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDCLICKSHARED #USERSMESSAGESNEWSFEEDCARDCLICKSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis stattgefunden hat
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattgefunden hat
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Betriebssystemversion des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Gerätebrowser – extrahiert aus user_agent –, in dem das Öffnen stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED #USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, an die ein Zustellungsversuch unternommen wurde
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis stattgefunden hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`platform` | `string` | Plattform des Geräts
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`message_extras` | `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONABORTSHARED #USERSMESSAGESPUSHNOTIFICATIONABORTSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`push_token` | `null,`&nbsp;`string` | Push-Token, das einen Bounce erzeugt hat
`device_id` | `null,`&nbsp;`string` | `device_id`, an die ein Zustellungsversuch unternommen wurde, der einen Bounce erzeugt hat
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis stattgefunden hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellungsversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED #USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis stattgefunden hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattgefunden hat
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Betriebssystemversion des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Dieses Ereignis wird vom [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) nicht unterstützt und ist im [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) veraltet.
{% endalert %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Betriebssystemversion des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellungsversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED #USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Betriebssystemversion des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`button_string` | `null,`&nbsp;`string` | Bezeichner (button_string) des angeklickten Push-Benachrichtigungs-Buttons. Null, wenn nicht durch einen Button-Klick ausgelöst
`button_action_type` | `null,`&nbsp;`string` | Aktionstyp des Push-Benachrichtigungs-Buttons. Einer von [URI, DEEP_LINK, NONE, CLOSE]. Null, wenn nicht durch einen Button-Klick ausgelöst
`slide_id` | `null,`&nbsp;`string` | Slide-Bezeichner der Push-Karussell-Slide, auf die die/der Nutzer:in geklickt hat
`slide_action_type` | `null,`&nbsp;`string` | Aktionstyp der Push-Karussell-Slide
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellungsversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`push_token` | `null,`&nbsp;`string` | Push-Token, an das ein Zustellungsversuch unternommen wurde
`device_id` | `null,`&nbsp;`string` | `device_id`, an die ein Zustellungsversuch unternommen wurde
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`platform` | `string` | Plattform des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellungsversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`is_sampled` | `null,`&nbsp;`string` | Gibt an, ob der Push-Versand gesampelt wurde und ein Zustellungsereignis erwartet wurde
`locale_key` | `null,`&nbsp;`string` | [PII] Der Schlüssel, der den Übersetzungen entspricht (z. B. „en-us“), die zum Verfassen dieser Nachricht verwendet wurden (null für Standard).
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONSENDSHARED #USERSMESSAGESPUSHNOTIFICATIONSENDSHARED" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`abort_log` | `null,`&nbsp;`string` | [PII] Lognachricht mit Details zum Abbruch (bis zu 128 Zeichen)
`abort_type` | `null,`&nbsp;`string` | Typ des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`message_extras` | `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSABORTSHARED #USERSMESSAGESRCSABORTSHARED" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`short_url` | `null,`&nbsp;`string` | Verkürzte URL, die angeklickt wurde
`suspected_bot_click_reason` | `null,`&nbsp;`string` | Grund, warum dieses Ereignis als Bot klassifiziert wurde
`user_agent` | `null,`&nbsp;`string` | User-Agent, bei dem der Spam-Bericht aufgetreten ist
`user_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Nutzer:in, von der die Nachricht empfangen wurde
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`interaction_type` | `null,`&nbsp;`string` | Der Interaktionstyp, der den Klick ausgelöst hat. Beispiel-String-Werte: Text URL, Reply, OpenURL
`element_label` | `null,`&nbsp;`string` | Optionale Details zum angeklickten Element, z. B. der Text einer vorgeschlagenen Antwort oder eines Buttons
`element_type` | `null,`&nbsp;`string` | Gibt an, ob ein interaction_type, der bei Vorschlägen und Buttons gleich ist, von einem Vorschlag oder Button stammt. Beispiele: Suggestion, Button
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`url` | `null,`&nbsp;`string` | URL, auf die die/der Nutzer:in geklickt hat
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSCLICKSHARED #USERSMESSAGESRCSCLICKSHARED" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Nutzer:in, die die Nachricht empfängt, im E.164-Format (z. B. +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`from_rcs_sender` | `null,`&nbsp;`string` | Die RCS-Absender-ID oder der Agent-Name, mit dem die Nachricht gesendet wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSDELIVERYSHARED #USERSMESSAGESRCSDELIVERYSHARED" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`action` | `null,`&nbsp;`string` | Als Reaktion auf diese Nachricht ausgeführte Aktion (z. B. Subscribed, Unsubscribed oder None).
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`media_urls` | `null,`&nbsp;`string` | Medien-URLs der/des Nutzer:in
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`user_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Nutzer:in, von der die Nachricht empfangen wurde
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`message_body` | `null,`&nbsp;`string` | Getippte Antwort der/des Nutzer:in
`to_rcs_sender` | `null,`&nbsp;`string` | Der eingehende RCS-Absender, an den die Nachricht gesendet wurde
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSINBOUNDRECEIVESHARED #USERSMESSAGESRCSINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Nutzer:in, die die Nachricht empfängt, im E.164-Format (z. B. +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREADSHARED #USERSMESSAGESRCSREADSHARED" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`error` | `null,`&nbsp;`string` | Fehlername
`from_rcs_sender` | `null,`&nbsp;`string` | Die RCS-Absender-ID oder der Agent-Name, mit dem die Nachricht gesendet wurde
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Dieses Feld ist mit dem SMS-Zustellungsereignis verknüpft/gepaart
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode des Anbieters
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Nutzer:in, die die Nachricht empfängt, im E.164-Format (z. B. +14155552671)
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREJECTIONSHARED #USERSMESSAGESRCSREJECTIONSHARED" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`category` | `null,`&nbsp;`string` | Name der Keyword-Kategorie, wird nur für automatische Antwortnachrichten befüllt: „opt-in“, „opt-out“, „help“ oder benutzerdefinierter Wert
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`from_rcs_sender` | `null,`&nbsp;`string` | Die RCS-Absender-ID oder der Agent-Name, mit dem die Nachricht gesendet wurde
`message_extras` | `null,`&nbsp;`string` | Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Nutzer:in, die die Nachricht empfängt, im E.164-Format (z. B. +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSSENDSHARED #USERSMESSAGESRCSSENDSHARED" }

### USERS_MESSAGES_BANNER_DISMISS_SHARED {#USERS_MESSAGES_BANNER_DISMISS_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | [PII] Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`app_api_id` | `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`campaign_id` | `string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `string` | [PII] Geschlecht der/des Nutzer:in
`country` | `string` | [PII] Land der/des Nutzer:in
`TIME_ZONE` | `string` | Zeitzone der/des Nutzer:in
`language` | `string` | [PII] Sprache der/des Nutzer:in
`device_id` | `string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `string` | Plattform des Geräts
`os_version` | `string` | Betriebssystemversion des Geräts
`device_model` | `string` | Modell des Geräts
`resolution` | `string` | Auflösung des Geräts
`carrier` | `string` | Mobilfunkanbieter des Geräts
`browser` | `string` | Geräte-Browser – extrahiert aus user_agent –, in dem das Öffnen stattfand
`button_id` | `string` | ID des angeklickten Buttons, wenn dieser Klick einen Button-Klick darstellt
`ad_id_type` | `string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`banner_placement_id` | `string` | Vom Kunden festgelegte Banner-Placement-ID
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_id` | `string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `string` | Name des Canvas
`canvas_step_name` | `string` | Name des Canvas-Schritts
`canvas_step_message_variation_api_id` | `string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`ad_id` | `string` | [PII] Werbe-Bezeichner
`is_unique` | `boolean` | Ob dieses Ereignis bei der Verarbeitung als 7-Tage-eindeutig eingestuft wurde
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERDISMISSSHARED #USERSMESSAGESBANNERDISMISSSHARED" }

### USERS_MESSAGES_LANDINGPAGE_CLICK_SHARED {#USERS_MESSAGES_LANDINGPAGE_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | [PII] Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`target` | `string` | Konfigurierte Tracking-ID des angeklickten Elements
`landing_page_api_id` | `string` | API-ID der Landing-Page, zu der dieses Ereignis gehört
`landing_page_name` | `string` | Name der Landing-Page
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLANDINGPAGECLICKSHARED #USERSMESSAGESLANDINGPAGECLICKSHARED" }

### USERS_MESSAGES_LANDINGPAGE_FORMSUBMISSION_SHARED {#USERS_MESSAGES_LANDINGPAGE_FORMSUBMISSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | [PII] Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`landing_page_api_id` | `string` | API-ID der Landing-Page, zu der dieses Ereignis gehört
`landing_page_name` | `string` | Name der Landing-Page
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLANDINGPAGEFORMSUBMISSIONSHARED #USERSMESSAGESLANDINGPAGEFORMSUBMISSIONSHARED" }

### USERS_MESSAGES_LANDINGPAGE_IMPRESSION_SHARED {#USERS_MESSAGES_LANDINGPAGE_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | [PII] Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`landing_page_api_id` | `string` | API-ID der Landing-Page, zu der dieses Ereignis gehört
`liquid_enabled` | `boolean` | Ein boolescher Wert, der angibt, ob die Landing-Page Liquid enthält und durch die Liquid-Rendering-Pipeline verarbeitet wurde.
`landing_page_name` | `string` | Name der Landing-Page
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLANDINGPAGEIMPRESSIONSHARED #USERSMESSAGESLANDINGPAGEIMPRESSIONSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_RETRY_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_RETRY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | [PII] Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`device_id` | `string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`app_api_id` | `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`gender` | `string` | [PII] Geschlecht der/des Nutzer:in
`country` | `string` | [PII] Land der/des Nutzer:in
`TIME_ZONE` | `string` | Zeitzone der/des Nutzer:in
`language` | `string` | [PII] Sprache der/des Nutzer:in
`platform` | `string` | Plattform des Geräts
`retry_type` | `string` | Typ des Wiederholungsversuchs
`retry_log` | `string` | Lognachricht mit Details zum Wiederholungsversuch
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONRETRYSHARED #USERSMESSAGESPUSHNOTIFICATIONRETRYSHARED" }

### USERS_MESSAGES_SURVEY_RESPONSE_SHARED {#USERS_MESSAGES_SURVEY_RESPONSE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | [PII] Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`survey_id` | `string` | UUID der Umfrage, zu der diese Antwort gehört.
`question_id` | `string` | UUID der Frage, zu der diese Antwort gehört.
`message_extras` | `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`gender` | `string` | [PII] Geschlecht der/des Nutzer:in
`country` | `string` | [PII] Land der/des Nutzer:in
`TIME_ZONE` | `string` | Zeitzone der/des Nutzer:in
`device_id` | `string` | [PII] ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `string` | Plattform des Geräts
`os_version` | `string` | Betriebssystemversion des Geräts
`device_model` | `string` | Modell des Geräts
`carrier` | `string` | Mobilfunkanbieter des Geräts
`browser` | `string` | Geräte-Browser – extrahiert aus user_agent –, in dem das Öffnen stattfand
`ad_id` | `string` | [PII] Werbe-Bezeichner
`ad_id_type` | `string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`answer_single_string` | `string` | [PII] Die Rohantwort, wenn der Antworttyp single_string ist
`answer_single_boolean` | `boolean` | [PII] Die Rohantwort, wenn der Antworttyp single_boolean ist
`answer_type` | `string` | Antworttyp des Ereignisses, einer von ['single_int', 'single_string', 'single_boolean']
`answer_long_string` | `string` | [PII] Die Rohantwort, wenn der Antworttyp free_form_text ist
`survey_session_id` | `string` | Eindeutiger Bezeichner zum Gruppieren aller Antworten einer einzelnen Umfrage-Sitzung
`landing_page_api_id` | `string` | API-ID der Landing-Page, zu der dieses Ereignis gehört
`campaign_api_id` | `string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_api_id` | `string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `string` | API-ID der Nachrichtenvariante des Canvas-Schritts, die diese:r Nutzer:in erhalten hat
`answer_multiple_strings` | `string` | [PII] Die Rohantwort, wenn der Antworttyp multiple_string ist.
`survey_completion_status` | `string` | Einer von ['completed', 'incomplete']
`response_id` | `string` | Eindeutiger Bezeichner, der die Antwort repräsentiert
`campaign_name` | `string` | Name der Campaign
`canvas_name` | `string` | Name des Canvas
`canvas_step_name` | `string` | Name des Canvas-Schritts
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`message_variation_name` | `string` | Name der Nachrichtenvariante
`app_api_id` | `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`question_reporting_id` | `string` | Der Reporting-Bezeichner für die Umfrage-Frage
`landing_page_name` | `string` | Name der Landing-Page
`answer_single_number` | `float` | [PII] Die Rohantwort, wenn der Antworttyp single_number ist
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSURVEYRESPONSESHARED #USERSMESSAGESSURVEYRESPONSESHARED" }

## SMS-Nachrichten-Events und gelöschte Nutzer:innenprofile {#sms-message-events-and-deleted-user-profiles}

{% alert note %}
Für gemeinsam genutzte `USERS_MESSAGES_SMS_*`-Tabellen (einschließlich [`USERS_MESSAGES_SMS_REJECTION_SHARED`](#USERS_MESSAGES_SMS_REJECTION_SHARED), [`USERS_MESSAGES_SMS_DELIVERY_SHARED`](#USERS_MESSAGES_SMS_DELIVERY_SHARED) und [`USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED`](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED)) schreibt Braze nur dann eine Zeile, wenn das Braze-Nutzerprofil zum Zeitpunkt der Verarbeitung des Events für Snowflake Data Sharing und Currents noch im Workspace vorhanden ist. Wurde die/der Nutzer:in vor Abschluss der Verarbeitung gelöscht, erscheint das Event nicht in Snowflake oder Ihrem Currents-Export, auch wenn die SMS-Workspace-Metriken im Dashboard weiterhin aggregierte Zählwerte aus dem Braze-Berichtspfad enthalten. Informationen zum entsprechenden Currents-Verhalten finden Sie unter [SMS-Rejection-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) und verwandte SMS-Event-Typen im selben Glossar.
{% endalert %}

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzerin/Nutzers
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`message_extras` | `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSABORTSHARED #USERSMESSAGESSMSABORTSHARED" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzerin/Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzerin/Nutzers
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzerin/Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzerin/Nutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzerin/Nutzers
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfängerin/des Empfängers
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die SMS gesendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSCARRIERSENDSHARED #USERSMESSAGESSMSCARRIERSENDSHARED" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzerin/Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzerin/Nutzers
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzerin/Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzerin/Nutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzerin/Nutzers
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfängerin/des Empfängers
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die SMS gesendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Verknüpft/gepaart mit dem SMS-Delivery-Event
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYSHARED #USERSMESSAGESSMSDELIVERYSHARED" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzerin/Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzerin/Nutzers
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzerin/Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzerin/Nutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzerin/Nutzers
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfängerin/des Empfängers
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`error` | `null,`&nbsp;`string` | Fehlername
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode des SMS-Dienstanbieters
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Verknüpft/gepaart mit dem SMS-Delivery-Event
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYFAILURESHARED #USERSMESSAGESSMSDELIVERYFAILURESHARED" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `null,`&nbsp;`string` | Braze-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzerin/Nutzers
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, der mit der eingehenden Telefonnummer verknüpft ist
`time` | `int` | Unix-Zeitstempel, zu dem das Event aufgetreten ist
`user_phone_number` | `string` | [PII] Telefonnummer der/des Nutzerin/Nutzers, von der die Nachricht empfangen wurde
`subscription_group_id` | `null,`&nbsp;`string` | ID der Abo-Gruppe, die für diese SMS-Nachricht verwendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe, die für diese SMS-Nachricht verwendet wurde
`inbound_phone_number` | `string` | Die eingehende Nummer, an die die Nachricht gesendet wurde
`action` | `string` | Als Reaktion auf diese Nachricht ausgeführte Aktion. Beispiel: `Subscribed`, `Unsubscribed` oder `None`.
`message_body` | `string` | Antwort der/des Nutzerin/Nutzers
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Medien-URLs der/des Nutzerin/Nutzers
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, zu der dieses Event gehört
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, zu der dieses Event gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSINBOUNDRECEIVESHARED #USERSMESSAGESSMSINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzerin/Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzerin/Nutzers
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzerin/Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzerin/Nutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzerin/Nutzers
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfängerin/des Empfängers
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die SMS gesendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`error` | `null,`&nbsp;`string` | Fehlername
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode des SMS-Dienstanbieters
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Verknüpft/gepaart mit dem SMS-Delivery-Event
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSREJECTIONSHARED #USERSMESSAGESSMSREJECTIONSHARED" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzerin/Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzerin/Nutzers
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzerin/Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzerin/Nutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzerin/Nutzers
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfängerin/des Empfängers
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`category` | `null,`&nbsp;`string` | Name der Keyword-Kategorie, nur für automatische Antwortnachrichten befüllt: 'Opt-in', 'Opt-out', 'Help' oder ein angepasster Wert
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSENDSHARED #USERSMESSAGESSMSSENDSHARED" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `null,`&nbsp;`string` | Braze-ID der/des Nutzerin/Nutzers, die/der mit short_url angesprochen wurde; null, wenn short_url kein Nutzer:innen-Klick-Tracking verwendet
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzerin/Nutzers, die/der mit short_url angesprochen wurde, sofern vorhanden; null, wenn short_url kein Nutzer:innen-Klick-Tracking verwendet
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, der zur Erstellung von short_url verwendet wurde
`time` | `int` | Unix-Zeitstempel, zu dem short_url angeklickt wurde
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzerin/Nutzers
`campaign_id` | `null,`&nbsp;`string` | Braze-ID der Campaign, für die short_url erstellt wurde; null, wenn nicht aus einer Campaign
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, für die short_url erstellt wurde; null, wenn nicht aus einer Campaign
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, für die short_url erstellt wurde; null, wenn nicht aus einer Campaign
`canvas_id` | `null,`&nbsp;`string` | Braze-ID des Canvas, für den short_url erstellt wurde; null, wenn nicht aus einem Canvas
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, für den short_url erstellt wurde; null, wenn nicht aus einem Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, für die short_url erstellt wurde; null, wenn nicht aus einem Canvas
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, für den short_url erstellt wurde; null, wenn nicht aus einem Canvas
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, für die short_url erstellt wurde; null, wenn nicht aus einem Canvas
`url` | `string` | Ursprüngliche URL in der Nachricht, auf die short_url weiterleitet
`short_url` | `string` | Gekürzte URL, die angeklickt wurde
`user_agent` | `null,`&nbsp;`string` | User-Agent, der short_url angefordert hat
`user_phone_number` | `string` | [PII] Telefonnummer der/des Nutzerin/Nutzers
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Event als Bot-Event verarbeitet wurde
`suspected_bot_click_reason` | `null, object` | Grund, warum dieses Event als Bot klassifiziert wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSHORTLINKCLICKSHARED #USERSMESSAGESSMSSHORTLINKCLICKSHARED" }

### USERS_MESSAGES_SMS_RETRY_SHARED {#USERS_MESSAGES_SMS_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Event tritt auf, wenn eine Nachricht herabpriorisiert oder durch Frequency-Capping begrenzt wird und innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | [PII] Braze-Nutzer-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzerin/Nutzers
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe
`retry_type` | `null,`&nbsp;`string` | Art der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zur Wiederholung
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSRETRYSHARED #USERSMESSAGESSMSRETRYSHARED" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzerin/Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzerin/Nutzers
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzerin/Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzerin/Nutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzerin/Nutzers
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`message_extras` | `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKABORTSHARED #USERSMESSAGESWEBHOOKABORTSHARED" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`http_status_code` | `null, int` | HTTP-Statuscode der Antwort
`endpoint_url` | `null,`&nbsp;`string` | Die angeforderte Endpunkt-URL
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`content_length` | `null, int` | Inhaltslänge der Antwort
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzerin/Nutzers
`host` | `null,`&nbsp;`string` | Der Host für die Anfrage
`id` | `string` | Global eindeutige ID für dieses Event
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`raw_response` | `null,`&nbsp;`string` | Gekürzte Roh-Antwort des Endpunkts
`retry_count` | `null, int` | Anzahl der durchgeführten Wiederholungsversuche
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event aufgetreten ist
`url_path` | `null,`&nbsp;`string` | Der Pfad der angeforderten URL
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`webhook_duration` | `null, int` | Gesamtdauer dieser Anfrage in Millisekunden
`webhook_failure_source` | `null,`&nbsp;`string` | Gibt an, ob ein Fehler von Braze oder vom Endpunkt selbst erzeugt wurde. Das Feld „source“ kann folgende Werte enthalten: External Endpoint, Treat no status code to host unreachable
`is_terminal` | `null, boolean` | Ob dieses Event der letzte Versuch eines Sendevorgangs war
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`canvas_name` | `string` | Name des Canvas
`canvas_step_name` | `string` | Name des Canvas-Schritts
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`message_variation_name` | `string` | Name der Nachrichtenvariante
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKFAILURESHARED #USERSMESSAGESWEBHOOKFAILURESHARED" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der/des Nutzerin/Nutzers, die/der dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzerin/Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Sende-ID der Nachricht, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzerin/Nutzers
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzerin/Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzerin/Nutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzerin/Nutzers
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKSENDSHARED #USERSMESSAGESWEBHOOKSENDSHARED" }

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED {#USERS_MESSAGES_WEBHOOK_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Ereignis tritt auf, wenn eine Nachricht herabpriorisiert oder durch Frequency Capping begrenzt wurde und innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | [PII] Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Send-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`retry_type` | `null,`&nbsp;`string` | Art der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Log-Nachricht mit Details zur Wiederholung
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKRETRYSHARED #USERSMESSAGESWEBHOOKRETRYSHARED" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`to_phone_number` | 	`null,`&nbsp;`string` | [PII] Telefonnummer der/des Empfänger:in
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die dieser/diesem Nutzer:in zugeordnet ist, wenn die/der Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Log-Nachricht mit Details zum Abbruch (maximal 2.000 Zeichen)
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`bsuid` | `string` | Die WhatsApp-Business-Scoped-User-ID der/des Nutzer:in, von der/dem die Nachricht empfangen wurde.
`message_extras` | `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPABORTSHARED #USERSMESSAGESWHATSAPPABORTSHARED" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`url` | `null,`&nbsp;`string` | URL, auf die die/der Nutzer:in geklickt hat
`short_url` | `null,`&nbsp;`string` | Gekürzte URL, auf die geklickt wurde
`user_agent` | `null,`&nbsp;`string` | User-Agent, bei dem der Spam-Bericht aufgetreten ist
`user_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Nutzer:in, von der die Nachricht empfangen wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPCLICKSHARED #USERSMESSAGESWHATSAPPCLICKSHARED" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Empfänger:in
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die dieser/diesem Nutzer:in zugeordnet ist, wenn die/der Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichten-Send-ID, zu der diese Nachricht gehört
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die/der Nutzer:in auf einen WhatsApp Flow antwortet.
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`message_id` | `null,`&nbsp;`string` | Die von Meta für diese Nachricht generierte eindeutige ID
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`bsuid` | `string` | Die WhatsApp-Business-Scoped-User-ID der/des Nutzer:in, von der/dem die Nachricht empfangen wurde.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPDELIVERYSHARED #USERSMESSAGESWHATSAPPDELIVERYSHARED" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Empfänger:in
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die dieser/diesem Nutzer:in zugeordnet ist, wenn die/der Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode von WhatsApp
`provider_error_title` | `null, `&nbsp;`string` | Fehlertitel von WhatsApp
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichten-Send-ID, zu der diese Nachricht gehört
`message_id` | `null,`&nbsp;`string` | Die von Meta für diese Nachricht generierte eindeutige ID
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die/der Nutzer:in auf einen WhatsApp Flow antwortet.
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`bsuid` | `string` | Die WhatsApp-Business-Scoped-User-ID der/des Nutzer:in, von der/dem die Nachricht empfangen wurde.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPFAILURESHARED #USERSMESSAGESWHATSAPPFAILURESHARED" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`user_phone_number` | `string` | [PII] Telefonnummer der/des Nutzer:in, von der die Nachricht empfangen wurde
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`inbound_phone_number` | `string` | Die eingehende Nummer, an die die Nachricht gesendet wurde
`device_id` | `null,`&nbsp;`string` | `device_id`, die dieser/diesem Nutzer:in zugeordnet ist, wenn die/der Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`message_body` | `string` | Antwort der/des Nutzer:in
`quick_reply_text` | `string` | Text des Buttons, den die/der Nutzer:in gedrückt hat
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Medien-URLs der/des Nutzer:in
`action` | `string` | Als Reaktion auf diese Nachricht ausgeführte Aktion. Zum Beispiel `Subscribed`, `Unsubscribed` oder `None`.
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`catalog_id` | `null,`&nbsp;`string` | Katalog-ID eines Produkts, wenn ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls leer.
`product_id` | `null,`&nbsp;`string` | ID des gekauften Produkts
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die/der Nutzer:in auf einen WhatsApp Flow antwortet.
`flow_response_json` | `null,`&nbsp;`string` | [PII] Die Formularwerte, mit denen die/der Nutzer:in geantwortet hat. Vorhanden, wenn die/der Nutzer:in auf einen WhatsApp Flow antwortet.
`message_id` | `null,`&nbsp;`string` | Die von Meta für diese Nachricht generierte eindeutige ID
`in_reply_to` | `null,`&nbsp;`string` | Die message_id der Nachricht, auf die diese Nachricht geantwortet hat
`campaign_name` | `string` | Name der Campaign
`canvas_name` | `string` | Name des Canvas
`canvas_step_name` | `string` | Name des Canvas-Schritts
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`message_variation_name` | `string` | Name der Nachrichtenvariante
`bsuid` | `string` | Die WhatsApp-Business-Scoped-User-ID der/des Nutzer:in, von der/dem die Nachricht empfangen wurde.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED #USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Empfänger:in
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die dieser/diesem Nutzer:in zugeordnet ist, wenn die/der Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichten-Send-ID, zu der diese Nachricht gehört
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`message_id` | `null,`&nbsp;`string` | Die von Meta für diese Nachricht generierte eindeutige ID
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die/der Nutzer:in auf einen WhatsApp Flow antwortet.
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`bsuid` | `string` | Die WhatsApp-Business-Scoped-User-ID der/des Nutzer:in, von der/dem die Nachricht empfangen wurde.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPREADSHARED #USERSMESSAGESWHATSAPPREADSHARED" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`to_phone_number` | `null,`&nbsp;`string`	| [PII] Telefonnummer der/des Empfänger:in
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die dieser/diesem Nutzer:in zugeordnet ist, wenn die/der Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichten-Send-ID, zu der diese Nachricht gehört
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die/der Nutzer:in auf einen WhatsApp Flow antwortet.
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`message_id` | `null,`&nbsp;`string` | Die von Meta für diese Nachricht generierte eindeutige ID
`campaign_name` | `string` | Name der Campaign
`canvas_name` | `string` | Name des Canvas
`canvas_step_name` | `string` | Name des Canvas-Schritts
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`message_variation_name` | `string` | Name der Nachrichtenvariante
`bsuid` | `string` | Die WhatsApp-Business-Scoped-User-ID der/des Nutzer:in, von der/dem die Nachricht empfangen wurde.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPSENDSHARED #USERSMESSAGESWHATSAPPSENDSHARED" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Ereignis tritt auf, wenn eine Nachricht herabpriorisiert oder durch Frequency Capping begrenzt wurde und innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | [PII] Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Nutzer:in, die/der die Nachricht empfängt, im E.164-Format
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`retry_type` | `null,`&nbsp;`string` | Art der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Log-Nachricht mit Details zur Wiederholung
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`campaign_name` | `string` | Name der Campaign
`message_variation_name` | `string` | Name der Nachrichtenvariante
`canvas_name` | `string` | Name des Canvas
`canvas_variation_name` | `string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `string` | Name des Canvas-Schritts
`bsuid` | `string` | Die WhatsApp-Business-Scoped-User-ID der/des Nutzer:in, von der/dem die Nachricht empfangen wurde.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPRETRYSHARED #USERSMESSAGESWHATSAPPRETRYSHARED" }

## Nutzer:innen {#users}

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Feld                        | Typ                      | Beschreibung                                                              |
| --------------------------- | ------------------------ | ------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Event                                     |
| `app_group_id`              | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                   |
| `app_group_api_id`          | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                     |
| `user_id`                   | `string`,&nbsp;`null`    | Braze-ID der/des Nutzer:in, die/der dieses Event ausgeführt hat           |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] Externe Nutzer-ID der/des Nutzer:in                                 |
| `time`                      | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Event aufgetreten ist                        |
| `random_bucket_number`      | `int`,&nbsp;`null`       | Aktuelle zufällige Bucket-Nummer, die der/dem Nutzer:in zugewiesen ist    |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | Vorherige zufällige Bucket-Nummer, die der/dem Nutzer:in zugewiesen war   |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSRANDOMBUCKETNUMBERUPDATESHARED #USERSRANDOMBUCKETNUMBERUPDATESHARED" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Feld               | Typ                      | Beschreibung                                                                    |
| ------------------ | ------------------------ | ------------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Event                                           |
| `user_id`          | `string`,&nbsp;`null`    | Braze-ID der/des Nutzer:in, die/der gelöscht wurde                              |
| `app_group_id`     | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                         |
| `app_group_api_id` | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                           |
| `time`             | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem die Löschanfrage der/des Nutzer:in verarbeitet wurde   |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERDELETEREQUESTSHARED #USERSUSERDELETEREQUESTSHARED" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Feld               | Typ                      | Beschreibung                                                                                                    |
| ------------------ | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Event                                                                           |
| `user_id`          | `string`,&nbsp;`null`    | Braze-ID der/des Nutzer:in, die/der verwaist wurde                                                              |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] Externe Nutzer-ID der/des Nutzer:in                                                                       |
| `device_id`        | `string`,&nbsp;`null`    | ID des Geräts, das mit dieser/diesem Nutzer:in verknüpft ist, falls die/der Nutzer:in anonym ist                |
| `app_group_id`     | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                                                         |
| `app_group_api_id` | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                                                           |
| `app_api_id`       | `string`,&nbsp;`null`    | API-ID der App, zu der die/der verwaiste Nutzer:in gehörte                                                      |
| `time`             | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem die/der Nutzer:in verwaist wurde                                                       |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | Braze-ID der/des Nutzer:in, deren/dessen Profil mit dem Profil der/des verwaisten Nutzer:in zusammengeführt wurde |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERORPHANSHARED #USERSUSERORPHANSHARED" }

### USERS_PROFILE_UPDATE_SHARED {#USERS_PROFILE_UPDATE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event aufgetreten ist
`time_ms` | `int` | Zeit in Millisekunden, zu der das Event aufgetreten ist
`user_id` | `string` | [PII] Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Event ausgeführt hat
`app_api_id` | `string` | API-ID der App, in der dieses Event aufgetreten ist
`update_source` | `string` | Die Quelle dieses Updates
`archived` | `boolean` | Wenn auf „True“ gesetzt, bedeutet dies, dass diese:r Nutzer:in in Braze archiviert wurde
`first_name` | `string` | [PII] Vorname der/des Nutzer:in
`last_name` | `string` | [PII] Nachname der/des Nutzer:in
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`gender` | `string` | [PII] Geschlecht der/des Nutzer:in
`phone_number` | `string` | [PII] Telefonnummer der/des Nutzer:in im E.164-Format (zum Beispiel +14155552671)
`dob` | `string` | [PII] Geburtsdatum der/des Nutzer:in im Format „YYYY-MM-DD“
`TIME_ZONE` | `string` | Zeitzone der/des Nutzer:in
`home_city` | `string` | [PII] Heimatort der/des Nutzer:in
`country` | `string` | [PII] Land der/des Nutzer:in
`language` | `string` | [PII] Sprache der/des Nutzer:in
`custom_attributes` | `string` | Gültiger JSON-String der aktualisierten angepassten Attribute
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSPROFILEUPDATESHARED #USERSPROFILEUPDATESHARED" }

## Snapshots {#snapshots}

{% alert note %}
Snapshot-Tabellen sind nur in Snowflake Data Sharing verfügbar.
{% endalert %}

### SNAPSHOTS_APP_SHARED {#SNAPSHOTS_APP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID der App
`name` | `null,`&nbsp;`string` | Name der App
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSAPPSHARED #SNAPSHOTSAPPSHARED" }

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID der Campaign-Nachrichtenvariante
`name` | `null,`&nbsp;`string` | Name der Campaign-Nachrichtenvariante
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCAMPAIGNMESSAGEVARIATIONSHARED #SNAPSHOTSCAMPAIGNMESSAGEVARIATIONSHARED" }

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`type` | `null,`&nbsp;`string` | Typ des Canvas-Flow-Schritts
`api_step_id` | `string` | API-ID des Canvas-Schritts
`experiment_splits` | `null,`&nbsp;`string` | Experiment-Splits für den Schritt
`conversion_behaviors` | `null,`&nbsp;`string` | Konversions-Verhalten für den Schritt
`name` | `null,`&nbsp;`string` | Name des Canvas-Flow-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASFLOWSTEPSHARED #SNAPSHOTSCANVASFLOWSTEPSHARED" }

### SNAPSHOTS_CANVAS_STEP_SHARED {#SNAPSHOTS_CANVAS_STEP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID des Canvas-Schritts
`name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`actions` | `null,`&nbsp;`string` | Aktionen für den Canvas-Schritt
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASSTEPSHARED #SNAPSHOTSCANVASSTEPSHARED" }

### SNAPSHOTS_CANVAS_VARIATION_SHARED {#SNAPSHOTS_CANVAS_VARIATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID der Canvas-Variante
`name` | `null,`&nbsp;`string` | Name der Canvas-Variante
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSCANVASVARIATIONSHARED #SNAPSHOTSCANVASVARIATIONSHARED" }

### SNAPSHOTS_EXPERIMENT_STEP_SHARED {#SNAPSHOTS_EXPERIMENT_STEP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`type` | `null,`&nbsp;`string` | Typ des Experiment-Schritts
`api_step_id` | `string` | API-ID des Experiment-Schritts
`experiment_splits` | `null,`&nbsp;`string` | Experiment-Splits für den Schritt
`conversion_behaviors` | `null,`&nbsp;`string` | Konversions-Verhalten für den Schritt
`name` | `null,`&nbsp;`string` | Name des Experiment-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SNAPSHOTSEXPERIMENTSTEPSHARED #SNAPSHOTSEXPERIMENTSTEPSHARED" }

### CONTENTOPTIMIZER_COMPONENTSTORE_SHARED {#CONTENTOPTIMIZER_COMPONENTSTORE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattgefunden hat
`content_optimizer_step_id` | `string` | Interne ID des CO-Schritts
`combination_token` | `string` | Zugewiesene Komponentenkombination
`content` | `string` | Gerenderter Inhalts-Payload im JSON-Format
`is_active` | `boolean` | Ob das Kombinations-Token aktiv für die Auslieferung genutzt wird
`sf_created_at` | `timestamp` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CONTENTOPTIMIZERCOMPONENTSTORESHARED #CONTENTOPTIMIZERCOMPONENTSTORESHARED" }

## Abbruchtypen {#abort-types}

{% include currents/abort_types_reference.md combined_content_rendering=true %}