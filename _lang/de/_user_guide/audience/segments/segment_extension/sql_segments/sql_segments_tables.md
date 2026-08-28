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
[AGENTCONSOLE_RAWLLMREQUEST_SHARED](#AGENTCONSOLE_RAWLLMREQUEST_SHARED) | Rohinformationen aus jedem LLM-Aufruf (**nur Snowflake Data Sharing**)
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | Wenn ein Tool ausgeführt wird (**nur Snowflake Data Sharing**)
[USER_CUSTOM_ATTRIBUTES_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_VIEW_SHARED) | Periodischer Snapshot angepasster Profilattribute pro Nutzer:in
[USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED) | Historische Standard-Profilattribute mit Gültigkeitszeiträumen
[USER_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_DEFAULT_ATTRIBUTES_VIEW_SHARED) | Periodischer Snapshot von Standard-Profilattributen pro Nutzer:in
[USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED](#USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED) | Nahezu in Echtzeit aktualisierte Standard-Profilattribute pro Nutzer:in
[USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED](#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED) | Historische angepasste Profilattribute mit Gültigkeitszeiträumen (**nur Snowflake Data Sharing**)
[USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED](#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED) | Nahezu in Echtzeit aktualisierte angepasste Profilattribute pro Nutzer:in (**nur Snowflake Data Sharing**)
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Nicht gelöschte Katalogartikel
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | Wenn eine Campaign geändert wird (**nur Snowflake Data Sharing**)
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | Wenn ein Canvas geändert wird (**nur Snowflake Data Sharing**)
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Wenn die globale Kontrollgruppe geändert wird
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Wenn Nutzer:innen ein angepasstes Event ausführen
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Wenn Nutzer:innen eine App installieren und wir die Installation einem Partner zuordnen
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Wenn Nutzer:innen einen Standort aufzeichnen
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Wenn Nutzer:innen einen Kauf tätigen
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Wenn Nutzer:innen eine App deinstallieren
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Wenn Nutzer:innen die App aktualisieren
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Wenn Nutzer:innen ihre erste Sitzung haben
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Wenn Nutzer:innen den News Feed ansehen
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Wenn Nutzer:innen eine Sitzung in einer App beenden
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Wenn Nutzer:innen eine Sitzung in einer App beginnen
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Wenn Nutzer:innen einen Geofence-Bereich auslösen – beispielsweise durch Betreten oder Verlassen eines Geofence. Dieses Ereignis wird mit anderen Ereignissen gebündelt und über den Standard-Endpunkt für Ereignisse empfangen, sodass es möglicherweise nicht in Echtzeit angezeigt wird.<br><br>Um Geofence-Aktivitäten in dieser Tabelle zu protokollieren, aktivieren Sie **Enable Analytics for Enter** und **Enable Analytics for Exit** in den erweiterten Einstellungen jedes Geofence. Weitere Details finden Sie in Schritt 3 unter [Geofences manuell erstellen]({{site.baseurl}}/user_guide/audience/locations_and_geofences/creating_geofences#manually-create-geofences).
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Wenn Nutzer:innen einen Geofence-Bereich auslösen (beispielsweise durch Betreten oder Verlassen eines Geofence). Dieses Ereignis wurde über den dedizierten Geofence-Endpunkt empfangen und wird daher in Echtzeit erfasst, sobald das Gerät erkennt, dass ein Geofence ausgelöst wurde. <br><br>Aufgrund von Rate-Limiting am Geofence-Endpunkt ist es zudem möglich, dass einige Geofence-Ereignisse nicht als RecordEvent widergespiegelt werden. Alle Geofence-Ereignisse werden jedoch durch DataEvent repräsentiert (allerdings möglicherweise mit einer gewissen Verzögerung durch die Bündelung).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Wenn sich ein Push-to-Start-Token einer Live Activity ändert
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Wenn sich ein Update-Token einer Live Activity ändert
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Wenn sich der Status eines Push-Benachrichtigungs-Tokens ändert
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Wenn sich Nutzer:innen global für einen Kanal wie E-Mail an- oder abmelden
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Wenn sich Nutzer:innen für eine Abo-Gruppe an- oder abmelden
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Wenn Nutzer:innen für eine Campaign konvertieren
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Wenn Nutzer:innen in die Kontrollgruppe einer Campaign aufgenommen werden
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Wenn Nutzer:innen für eine Campaign durch ein Frequency Cap begrenzt werden
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Wenn Nutzer:innen innerhalb des primären Konversionszeitraums Umsatz generieren
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Wenn Nutzer:innen zu einem Canvas-Schritt fortschreiten
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Wenn Nutzer:innen für ein Canvas-Konversions-Event konvertieren
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Wenn Nutzer:innen ein Canvas betreten
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Wenn Nutzer:innen ein Canvas verlassen, weil sie den Zielgruppen-Exit-Kriterien entsprechen
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Wenn Nutzer:innen ein Canvas verlassen, weil sie ein Ausnahme-Event ausgeführt haben
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Wenn Nutzer:innen für einen Canvas-Experiment-Schritt konvertieren
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Wenn Nutzer:innen einen Experiment-Schritt-Pfad betreten
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Wenn Nutzer:innen für einen Canvas-Schritt durch ein Frequency Cap begrenzt werden
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Wenn Nutzer:innen innerhalb des primären Konversions-Event-Zeitraums Umsatz generieren
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Eine ursprünglich geplante Banner-Nachricht wurde aus einem bestimmten Grund abgebrochen
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Wenn Nutzer:innen auf ein Banner klicken
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Wenn Nutzer:innen ein Banner ansehen
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Eine ursprünglich geplante Content-Card-Nachricht wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Wenn Nutzer:innen auf eine Content-Card klicken
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Wenn Nutzer:innen eine Content-Card schließen
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Wenn Nutzer:innen eine Content-Card ansehen
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Wenn wir eine Content-Card an Nutzer:innen senden
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Eine ursprünglich geplante E-Mail-Nachricht wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Ein E-Mail-Anbieter hat einen Hard Bounce zurückgegeben. Ein Hard Bounce weist auf einen dauerhaften Zustellbarkeitsfehler hin.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Wenn Nutzer:innen auf einen Link in einer E-Mail klicken
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Wenn eine E-Mail zurückgestellt wird
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Wenn eine E-Mail zugestellt wird
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Wenn eine E-Mail als Spam markiert wird
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Wenn Nutzer:innen eine E-Mail öffnen
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Wenn wir eine E-Mail an Nutzer:innen senden
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Wenn eine E-Mail einen Soft Bounce erhält
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Wenn sich Nutzer:innen von E-Mails abmelden
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | Wenn eine E-Mail-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Wenn Nutzer:innen ein Feature-Flag ansehen
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Eine ursprünglich geplante In-App-Nachricht wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Wenn Nutzer:innen auf eine In-App-Nachricht klicken
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Wenn Nutzer:innen eine In-App-Nachricht ansehen
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Wenn eine geplante LINE-Nachricht vor dem Versand an LINE nicht zugestellt werden kann
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Wenn Nutzer:innen auf einen Link in einer LINE-Nachricht klicken
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Wenn eine LINE-Nachricht von Nutzer:innen empfangen wird
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Wenn eine LINE-Nachricht an LINE gesendet wird
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | Wenn eine LINE-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Wenn eine Live Activity ein Outcome-Ereignis hat
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Wenn eine Live-Activity-Nachricht gesendet wird
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Eine ursprünglich geplante Newsfeed-Card-Nachricht wurde aus einem bestimmten Grund abgebrochen
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Wenn Nutzer:innen auf eine News-Feed-Card klicken
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Wenn Nutzer:innen eine News-Feed-Card ansehen
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Eine ursprünglich geplante Push-Benachrichtigung wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Wenn eine Push-Benachrichtigung einen Bounce erhält
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Wenn Nutzer:innen die App öffnen, nachdem sie eine Benachrichtigung erhalten haben, ohne auf die Benachrichtigung zu klicken
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Wenn Nutzer:innen eine Push-Benachrichtigung erhalten, während die App geöffnet ist. <br><br>Dieses Ereignis wird vom [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) nicht unterstützt und ist im [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) veraltet.
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Wenn Nutzer:innen eine Push-Benachrichtigung öffnen oder auf einen Push-Benachrichtigungs-Button klicken (einschließlich eines CLOSE-Buttons, der die App NICHT öffnet). <br><br> Push-Button-Aktionen haben mehrere Ergebnisse. „No“-, „Decline“- und „Cancel“-Aktionen sind „Klicks“, und „Accept“-Aktionen sind „Öffnungen“. Beides wird in dieser Tabelle dargestellt, kann aber über die Spalte **BUTTON_ACTION_TYPE** unterschieden werden. Beispielsweise kann eine Abfrage verwendet werden, um nach einem `BUTTON_ACTION_TYPE` zu gruppieren, der nicht „No“, „Decline“ oder „Cancel“ ist.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Wenn wir eine Push-Benachrichtigung an Nutzer:innen senden
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Wenn ein RCS-Versand aufgrund eines innerhalb von Braze erkannten Fehlers unterbrochen und die Nachricht verworfen wird
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Wenn Endnutzer:innen mit einer RCS-Nachricht interagieren, indem sie auf ein UI-Element tippen oder klicken
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Wenn eine RCS-Nachricht erfolgreich an das Mobilgerät von Endnutzer:innen zugestellt wird
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Wenn Braze eine RCS-Nachricht empfängt, die von Endnutzer:innen stammt
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Wenn Endnutzer:innen eine RCS-Nachricht auf ihrem Gerät öffnen
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Wenn eine RCS-Nachricht aufgrund einer Intervention des Mobilfunkanbieters nicht zugestellt werden kann
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Wenn eine RCS-Nachricht von den Braze-Systemen an Last-Mile-Zustellpartner gesendet wird
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Eine ursprünglich geplante SMS-Nachricht wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Wenn eine SMS-Nachricht an den Mobilfunkanbieter gesendet wird
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Wenn eine SMS-Nachricht zugestellt wird
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Wenn Braze die SMS-Nachricht nicht an den SMS-Dienstanbieter zustellen kann
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Wenn eine SMS-Nachricht von Nutzer:innen empfangen wird
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Wenn eine SMS-Nachricht nicht an Nutzer:innen zugestellt wird
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Wenn eine SMS-Nachricht gesendet wird
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Wenn Nutzer:innen auf eine von Braze verkürzte URL in einer SMS-Nachricht klicken
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | Wenn eine SMS-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Eine ursprünglich geplante Webhook-Nachricht wurde aus einem bestimmten Grund abgebrochen
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Wenn eine Webhook-Nachricht zugestellt wird, aber mit einer Fehlerantwort vom Endpunkt fehlschlägt
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Wenn wir einen Webhook für Nutzer:innen senden
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | Wenn eine Webhook-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Eine ursprünglich geplante WhatsApp-Nachricht wurde aus einem bestimmten Grund abgebrochen
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Wenn Nutzer:innen auf einen Link oder Button in einer WhatsApp-Nachricht klicken
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | Wenn eine WhatsApp-Nachricht zugestellt wird
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Wenn eine WhatsApp-Nachricht nicht an Nutzer:innen zugestellt wird
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Wenn eine WhatsApp-Nachricht von Nutzer:innen empfangen wird
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Wenn Nutzer:innen eine WhatsApp-Nachricht öffnen
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Wenn wir eine WhatsApp-Nachricht für Nutzer:innen senden
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | Wenn eine WhatsApp-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Wenn die zufällige Bucket-Nummer von Nutzer:innen geändert wird
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Wenn Nutzer:innen auf Kundenanfrage gelöscht werden
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Wenn Nutzer:innen mit dem Profil anderer Nutzer:innen zusammengeführt werden und das ursprüngliche Profil verwaist
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | App-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | Campaign-Nachrichtenvarianten-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | Canvas-Flow-Schritt-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | Canvas-Schritt-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | Canvas-Varianten-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | Experiment-Schritt-Snapshots (**nur Snowflake Data Sharing**)

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED #USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED" }

### USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED {#USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="history" %}

Hinweise zur Verwendung und Beispielabfragen finden Sie unter [Snowflake-Nutzerattribute]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#historical-change-logs).

### USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED {#USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

{% multi_lang_include partners/snowflake_user_attributes_custom_view_schemas.md schema="latest" %}

Hinweise zur Verwendung und Beispielabfragen finden Sie unter [Snowflake-Nutzerattribute]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes#real-time-user-profile-views).

## Kataloge {#catalogs}

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`catalog_id` | `string` | BSON-ID des Katalogs
`item_id` | `string` | BSON-ID des Katalogartikels
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe
`field_name` | `null,`&nbsp;`string` | Name des Feldes
`field_value` | `null,`&nbsp;`string` | Wert des Feldes
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CATALOGSITEMSSHARED #CATALOGSITEMSSHARED" }

## Changelogs {#changelogs}

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event aufgetreten ist
`random_bucket_number` | `null, int` | Neue zufällige Bucket-Nummer
`global_control_group` | `null, boolean` | Mit dieser Änderung ist die Bucket-Nummer in der globalen Kontrollgruppe enthalten
`previous_global_control_group` | `null, boolean` | Vor dieser Änderung war die Bucket-Nummer in der globalen Kontrollgruppe enthalten, ist es aber nicht mehr
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSGLOBALCONTROLGROUPSHARED #CHANGELOGSGLOBALCONTROLGROUPSHARED" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event aufgetreten ist
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID der Campaign
`name` | `null,`&nbsp;`string` | Name der Campaign
`conversion_behaviors` | `null,`&nbsp;`string` | Konversionsverhalten für die Campaign
`actions` | `null,`&nbsp;`string` | Aktionen für die Campaign
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCAMPAIGNSHARED #CHANGELOGSCAMPAIGNSHARED" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event aufgetreten ist
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID des Canvas
`name` | `null,`&nbsp;`string` | Name des Canvas
`conversion_behaviors` | `null,`&nbsp;`string` | Konversionsverhalten für das Canvas
`variations` | `null,`&nbsp;`string` | Varianten für das Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="CHANGELOGSCANVASSHARED #CHANGELOGSCANVASSHARED" }

## Verhalten {#behaviors}

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der das Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Aktion stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die/der Nutzer:in das Ereignis ausgeführt hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das angepasste Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`name` | `string` | Name des angepassten Ereignisses
`properties` | `string` | Angepasste Eigenschaften des Ereignisses, gespeichert als JSON-codierter String
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSCUSTOMEVENTSHARED #USERSBEHAVIORSCUSTOMEVENTSHARED" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der die Installation durchgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem die/der Nutzer:in die Installation durchgeführt hat
`source` | `string` | Quelle der Attribution
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSINSTALLATTRIBUTIONSHARED #USERSBEHAVIORSINSTALLATTRIBUTIONSHARED" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der den Standort aufzeichnet
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieser Standort aufgezeichnet wurde
`time` | `int` | Unix-Zeitstempel, zu dem der Standort aufgezeichnet wurde
`latitude` | `float` | [PII] Breitengrad des aufgezeichneten Standorts
`longitude` | `float` | [PII] Längengrad des aufgezeichneten Standorts
`altitude` | `null, float` | [PII] Höhe des aufgezeichneten Standorts
`ll_accuracy` | `null, float` | Genauigkeit von Breiten- und Längengrad des aufgezeichneten Standorts
`alt_accuracy` | `null, float` | Höhengenauigkeit des aufgezeichneten Standorts
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem der Standort aufgezeichnet wurde
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das bei der Aufzeichnung des Standorts verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLOCATIONSHARED #USERSBEHAVIORSLOCATIONSHARED" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der einen Kauf getätigt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der der Kauf stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die/der Nutzer:in den Kauf getätigt hat
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
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPURCHASESHARED #USERSBEHAVIORSPURCHASESHARED" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der die App deinstalliert hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, die deinstalliert wurde
`time` | `int` | Unix-Zeitstempel, zu dem die/der Nutzer:in die App deinstalliert hat
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUNINSTALLSHARED #USERSBEHAVIORSUNINSTALLSHARED" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der die App aktualisiert hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, die die/der Nutzer:in aktualisiert hat
`time` | `int` | Unix-Zeitstempel, zu dem die/der Nutzer:in die App aktualisiert hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die/der Nutzer:in die App aktualisiert hat
`sdk_version` | `null,`&nbsp;`string` | Version des verwendeten Braze SDK
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`old_app_version` | `null,`&nbsp;`string` | Alte Version der App
`new_app_version` | `null,`&nbsp;`string` | Neue Version der App
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSUPGRADEDAPPSHARED #USERSBEHAVIORSUPGRADEDAPPSHARED" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der diese Aktion ausführt
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Sitzung stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Sitzung gestartet wurde
`session_id` | `string` | UUID der Sitzung
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Sitzung stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während der Sitzung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPFIRSTSESSIONSHARED #USERSBEHAVIORSAPPFIRSTSESSIONSHARED" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis stattfand
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
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
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der diese Aktion ausführt
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Sitzung stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Sitzung beendet wurde
`duration` | `null, float` | Dauer der Sitzung in Sekunden
`session_id` | `string` | UUID der Sitzung
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Sitzung stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während der Sitzung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONENDSHARED #USERSBEHAVIORSAPPSESSIONENDSHARED" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der diese Aktion ausführt
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Sitzung stattfand
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem die Sitzung gestartet wurde
`session_id` | `string` | UUID der Sitzung
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Sitzung stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während der Sitzung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSAPPSESSIONSTARTSHARED #USERSBEHAVIORSAPPSESSIONSTARTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der das Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Aktion stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die/der Nutzer:in das Ereignis ausgeführt hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das angepasste Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`event_type` | `string` | Welche Art von Geofence-Ereignis ausgelöst wurde (zum Beispiel „enter“ oder „exit“)
`location_set_id` | `string` | Die ID des Standortsets des ausgelösten Geofence
`geofence_id` | `string` | Die ID des ausgelösten Geofence
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCEDATAEVENTSHARED #USERSBEHAVIORSGEOFENCEDATAEVENTSHARED" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der das Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Aktion stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die/der Nutzer:in das Ereignis ausgeführt hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das angepasste Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`event_type` | `string` | Welche Art von Geofence-Ereignis ausgelöst wurde (zum Beispiel „enter“ oder „exit“)
`location_set_id` | `string` | Die ID des Standortsets des ausgelösten Geofence
`geofence_id` | `string` | Die ID des ausgelösten Geofence
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSGEOFENCERECORDEVENTSHARED #USERSBEHAVIORSGEOFENCERECORDEVENTSHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`activity_attributes_type` | `null,`&nbsp;`string` | Live-Activity-Attributtyp
`push_to_start_token` | `null,`&nbsp;`string` | Push-to-Start-Token der Live Activity
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS-Push-Tokens, 1 für Entwicklung, 2 für Produktion
`push_token_state_change_type` | `null,`&nbsp;`string` | Beschreibung des Änderungstyps des Push-Token-Status
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYPUSHTOSTARTTOKENCHANGESHARED" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`activity_id` | `null,`&nbsp;`string` | Bezeichner der Live Activity
`update_token` | `null,`&nbsp;`string` | Aktualisierungstoken der Live Activity
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS-Push-Tokens, 1 für Entwicklung, 2 für Produktion
`push_token_state_change_type` | `null,`&nbsp;`string` | Beschreibung des Änderungstyps des Push-Token-Status
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED #USERSBEHAVIORSLIVEACTIVITYUPDATETOKENCHANGESHARED" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`time_ms` | `int` | Zeitpunkt in Millisekunden, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, das während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`push_token` | `null,`&nbsp;`string` | Push-Token des Ereignisses
`push_token_created_at` | `null, int` | UNIX-Zeitstempel, zu dem das Push-Token erstellt wurde
`push_token_updated_at` | `null, int` | UNIX-Zeitstempel, zu dem das Push-Token zuletzt aktualisiert wurde
`push_token_foreground_push_disabled` | `null, boolean` | Flag, ob Vordergrund-Push für das Push-Token deaktiviert ist
`push_token_device_id` | `null,`&nbsp;`string` | Geräte-ID des Push-Tokens
`push_token_provisionally_opted_in` | `null, boolean` | Flag, ob das Push-Token vorläufig angemeldet ist
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS-Push-Tokens, 1 für Entwicklung, 2 für Produktion
`web_push_token_public_key` | `null,`&nbsp;`string` | Public Key des Push-Tokens, gilt nur für Web-Push-Tokens
`web_push_token_user_auth` | `null,`&nbsp;`string` | Nutzer-Authentifizierung des Push-Tokens, gilt nur für Web-Push-Tokens
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | VAPID-Public-Key des Push-Tokens, gilt nur für Web-Push-Tokens
`push_token_state_change_type` | `null,`&nbsp;`string` | Beschreibung des Änderungstyps des Push-Token-Status
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED #USERSBEHAVIORSPUSHNOTIFICATIONTOKENSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des betroffenen Nutzer:in
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der/des Nutzer:in
`state_change_source` | `null,`&nbsp;`string` | Quelle der Statusänderung (REST, SDK, Dashboard usw.)
`subscription_status` | `string` | Abo-Status: „Subscribed“, „Unsubscribed“ oder „Opted In“
`channel` | `null,`&nbsp;`string` | Kanal des globalen Abo-Status, z. B. E-Mail
`time` | `int` | Unix-Zeitstempel, zu dem sich der Abo-Status geändert hat
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, zu der das Ereignis gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, zu der dieses Ereignis gehört
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, von der diese Abo-Statusänderung ausging
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`channel_identifier` | `null,`&nbsp;`string` | [PII] Der Bezeichner der/des Nutzer:in auf dem Kanal, für den das Ereignis bestimmt ist.
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGLOBALSTATECHANGESHARED" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des betroffenen Nutzer:in
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der/des Nutzer:in
`phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der/des Nutzer:in im E.164-Format
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, zu der das Ereignis gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, zu der dieses Ereignis gehört
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`channel` | `null,`&nbsp;`string` | Kanal: „email“ oder „sms“, je nach Kanaltyp der Abo-Gruppe
`subscription_status` | `string` | Abo-Status: „Subscribed“, „Unsubscribed“ oder „Opted In“
`time` | `int` | Unix-Zeitstempel, zu dem sich der Abo-Status geändert hat
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, von der diese Abo-Statusänderung ausging
`state_change_source` | `null,`&nbsp;`string` | Quelle der Statusänderung (REST, SDK, Dashboard usw.)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`channel_identifier` | `null,`&nbsp;`string` | [PII] Der Bezeichner der/des Nutzer:in auf dem Kanal, für den das Ereignis bestimmt ist.
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED #USERSBEHAVIORSSUBSCRIPTIONGROUPSTATECHANGESHARED" }

## Campaigns {#campaigns}

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattgefunden hat
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`conversion_behavior_index` | `null, int` | Index des Konversionsverhaltens
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSCONVERSIONSHARED #USERSCAMPAIGNSCONVERSIONSHARED" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattgefunden hat
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSENROLLINCONTROLSHARED #USERSCAMPAIGNSENROLLINCONTROLSHARED" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattgefunden hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`channel` | `null,`&nbsp;`string` | Kanal, zu dem dieses Event gehört
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSFREQUENCYCAPSHARED #USERSCAMPAIGNSFREQUENCYCAPSHARED" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattgefunden hat
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Campaign, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`revenue` | `long` | Der generierte Umsatz in USD-Cent
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCAMPAIGNSREVENUESHARED #USERSCAMPAIGNSREVENUESHARED" }

## Canvas {#canvas}

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Feld                                   | Typ                      | Beschreibung                                                                                                    |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                                                        |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID der Nutzerin oder des Nutzers, die/der dieses Ereignis ausgeführt hat                                  |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID der Nutzerin oder des Nutzers                                                                  |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das dieser Nutzerin oder diesem Nutzer zugeordnet ist, falls anonym                              |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                                                         |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                                                           |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist                                                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört                       |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                                                |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                                                       |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                                                       |
| `progression_type`                     | `string`,&nbsp;`null`    | Art des Schritt-Progressions-Ereignisses                                                                        |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | Ob dies ein Entry in einen ersten Schritt eines Canvas ist                                                      |
| `exit_reason`                          | `string`,&nbsp;`null`    | Falls dies ein Exit ist, der Grund, warum die Nutzerin oder der Nutzer den Canvas während des Schritts verlassen hat |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | Eindeutiger Bezeichner für diese Instanz einer Nutzerin oder eines Nutzers in einem Canvas                      |
| `next_step_id`                         | `string`,&nbsp;`null`    | BSON-ID des nächsten Schritts im Canvas                                                                         |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | API-ID des nächsten Schritts im Canvas                                                                          |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASSTEPPROGRESSIONSHARED #USERSCANVASSTEPPROGRESSIONSHARED" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Feld                                   | Typ                      | Beschreibung                                                                                                                              |
| -------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                                                                                  |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID der Nutzerin oder des Nutzers, die/der dieses Ereignis ausgeführt hat                                                            |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID der Nutzerin oder des Nutzers                                                                                            |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das dieser Nutzerin oder diesem Nutzer zugeordnet ist, falls anonym                                                        |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                                                                                     |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist                                                                                     |
| `app_api_id`                           | `string`,&nbsp;`null`    | API-ID der App, in der dieses Ereignis aufgetreten ist                                                                                    |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört                                                 |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                                                                          |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                                                                                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                                                                                 |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat                                                         |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | Art des Konversions-Events, das die Nutzerin oder der Nutzer ausgeführt hat, wobei „0“ eine primäre Konversion und „1“ eine sekundäre Konversion ist |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Geschlecht der Nutzerin oder des Nutzers                                                                                            |
| `country`                              | `string`,&nbsp;`null`    | [PII] Land der Nutzerin oder des Nutzers                                                                                                  |
| `timezone`                             | `string`,&nbsp;`null`    | Zeitzone der Nutzerin oder des Nutzers                                                                                                    |
| `language`                             | `string`,&nbsp;`null`    | [PII] Sprache der Nutzerin oder des Nutzers                                                                                               |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASCONVERSIONSHARED #USERSCANVASCONVERSIONSHARED" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Feld                      | Typ                      | Beschreibung                                                                        |
| ------------------------- | ------------------------ | ----------------------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                            |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID der Nutzerin oder des Nutzers, die/der dieses Ereignis ausgeführt hat      |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID der Nutzerin oder des Nutzers                                     |
| `device_id`               | `string`,&nbsp;`null`    | ID des Geräts, das dieser Nutzerin oder diesem Nutzer zugeordnet ist, falls anonym  |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                             |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                               |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist                               |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                    |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                           |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [Veraltet] API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                |
| `gender`                  | `string`,&nbsp;`null`    | [PII] Geschlecht der Nutzerin oder des Nutzers                                     |
| `country`                 | `string`,&nbsp;`null`    | [PII] Land der Nutzerin oder des Nutzers                                            |
| `timezone`                | `string`,&nbsp;`null`    | Zeitzone der Nutzerin oder des Nutzers                                              |
| `language`                | `string`,&nbsp;`null`    | [PII] Sprache der Nutzerin oder des Nutzers                                        |
| `in_control_group`        | `boolean`,&nbsp;`null`   | True, wenn die Nutzerin oder der Nutzer in die Kontrollgruppe aufgenommen wurde     |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASENTRYSHARED #USERSCANVASENTRYSHARED" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Feld                      | Typ                      | Beschreibung                                                                        |
| ------------------------- | ------------------------ | ----------------------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                            |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID der Nutzerin oder des Nutzers, die/der dieses Ereignis ausgeführt hat      |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID der Nutzerin oder des Nutzers                                     |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                             |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                               |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist                               |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                    |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                           |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                           |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITMATCHEDAUDIENCESHARED #USERSCANVASEXITMATCHEDAUDIENCESHARED" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Feld                      | Typ                      | Beschreibung                                                                        |
| ------------------------- | ------------------------ | ----------------------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                            |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID der Nutzerin oder des Nutzers, die/der dieses Ereignis ausgeführt hat      |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID der Nutzerin oder des Nutzers                                     |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                             |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                               |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist                               |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                    |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                           |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                           |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXITPERFORMEDEVENTSHARED #USERSCANVASEXITPERFORMEDEVENTSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Feld                        | Typ                      | Beschreibung                                                                                                                              |
| --------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                                                                                  |
| `user_id`                   | `string`,&nbsp;`null`    | Braze-ID der Nutzerin oder des Nutzers, die/der dieses Ereignis ausgeführt hat                                                            |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] Externe ID der Nutzerin oder des Nutzers                                                                                            |
| `app_group_id`              | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                                                                                   |
| `time`                      | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist                                                                                     |
| `app_api_id`                | `string`,&nbsp;`null`    | API-ID der App, in der dieses Ereignis aufgetreten ist                                                                                    |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört                                                 |
| `canvas_api_id`             | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                                                                          |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                                                                                 |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                                                                                 |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | API-ID des Experiment-Schritts, zu dem dieses Ereignis gehört                                                                             |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | Art des Konversions-Events, das die Nutzerin oder der Nutzer ausgeführt hat, wobei „0“ eine primäre Konversion und „1“ eine sekundäre Konversion ist |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                                                                          |
| `experiment_split_api_id` | `string`,&nbsp;`null` | API-ID des Experiment-Splits, in den die Nutzerin oder der Nutzer aufgenommen wurde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED #USERSCANVASEXPERIMENTSTEPCONVERSIONSHARED" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Feld                      | Typ                      | Beschreibung                                                                        |
| ------------------------- | ------------------------ | ----------------------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                            |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID der Nutzerin oder des Nutzers, die/der dieses Ereignis ausgeführt hat      |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID der Nutzerin oder des Nutzers                                     |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                             |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist                               |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                    |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                           |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                           |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | API-ID des Experiment-Schritts, zu dem dieses Ereignis gehört                       |
| `in_control_group`        | `boolean`,&nbsp;`null`   | True, wenn die Nutzerin oder der Nutzer in die Kontrollgruppe aufgenommen wurde     |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

| `experiment_split_api_id` | `string`,&nbsp;`null` | API-ID des Experiment-Splits, in den die Nutzerin oder der Nutzer aufgenommen wurde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED #USERSCANVASEXPERIMENTSTEPSPLITENTRYSHARED" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Feld                                   | Typ                      | Beschreibung                                                                        |
| -------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                            |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID der Nutzerin oder des Nutzers, die/der dieses Ereignis ausgeführt hat      |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID der Nutzerin oder des Nutzers                                     |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das dieser Nutzerin oder diesem Nutzer zugeordnet ist, falls anonym  |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                             |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                               |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist                               |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                    |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                           |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                           |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat   |
| `channel`                              | `string`,&nbsp;`null`    | Messaging-Kanal, zu dem dieses Ereignis gehört (E-Mail, Push usw.)                  |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Geschlecht der Nutzerin oder des Nutzers                                     |
| `country`                              | `string`,&nbsp;`null`    | [PII] Land der Nutzerin oder des Nutzers                                            |
| `timezone`                             | `string`,&nbsp;`null`    | Zeitzone der Nutzerin oder des Nutzers                                              |
| `language`                             | `string`,&nbsp;`null`    | [PII] Sprache der Nutzerin oder des Nutzers                                        |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASFREQUENCYCAPSHARED #USERSCANVASFREQUENCYCAPSHARED" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Feld                                   | Typ                      | Beschreibung                                                                        |
| -------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Ereignis                                            |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID der Nutzerin oder des Nutzers, die/der dieses Ereignis ausgeführt hat      |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID der Nutzerin oder des Nutzers                                     |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das dieser Nutzerin oder diesem Nutzer zugeordnet ist, falls anonym  |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                             |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                               |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist                               |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für die interne Verwendung durch Braze) ID des Canvas, zu dem dieses Ereignis gehört |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Ereignis gehört                                    |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variante, zu der dieses Ereignis gehört                           |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört                           |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat   |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Geschlecht der Nutzerin oder des Nutzers                                     |
| `country`                              | `string`,&nbsp;`null`    | [PII] Land der Nutzerin oder des Nutzers                                            |
| `timezone`                             | `string`,&nbsp;`null`    | Zeitzone der Nutzerin oder des Nutzers                                              |
| `language`                             | `string`,&nbsp;`null`    | [PII] Sprache der Nutzerin oder des Nutzers                                        |
| `revenue`                              | `int`,&nbsp;`null`       | Höhe des generierten Umsatzes in USD, angegeben in Cent                             |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde                    |
| `app_api_id` | `string`,&nbsp;`null` | API-ID der App, in der dieses Ereignis aufgetreten ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSCANVASREVENUESHARED #USERSCANVASREVENUESHARED" }

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
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus user_agent extrahiert –, in dem die Öffnung stattfand
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Lognachricht mit Abbruchdetails (bis zu 128 Zeichen)
`banner_placement_id` | `null,`&nbsp;`string` | Vom Kunden angegebene Banner-Platzierungs-ID
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
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
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus user_agent extrahiert –, in dem die Öffnung stattfand
`button_id` | `null,`&nbsp;`string` | ID des geklickten Buttons, wenn dieser Klick einen Button-Klick darstellt
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`banner_placement_id` | `null,`&nbsp;`string` | Vom Kunden angegebene Banner-Platzierungs-ID
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
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
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus user_agent extrahiert –, in dem die Öffnung stattfand
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`banner_placement_id` | `null,`&nbsp;`string` | Vom Kunden angegebene Banner-Platzierungs-ID
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESBANNERIMPRESSIONSHARED #USERSMESSAGESBANNERIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Lognachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
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
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
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
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
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
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDIMPRESSIONSHARED #USERSMESSAGESCONTENTCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`content_card_id` | `string` | ID der Card, die dieses Ereignis generiert hat
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESCONTENTCARDSENDSHARED #USERSMESSAGESCONTENTCARDSENDSHARED" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Lognachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILABORTSHARED #USERSMESSAGESEMAILABORTSHARED" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der der E-Mail-Versand erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`bounce_reason` | `null,`&nbsp;`string` | [PII] Der SMTP-Ursachencode und die benutzerfreundliche Nachricht, die für dieses Bounce-Ereignis empfangen wurden
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absende-Domain für die E-Mail
`is_drop` | `null, boolean` | Gibt an, ob dieses Ereignis als Drop-Ereignis zählt
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILBOUNCESHARED #USERSMESSAGESEMAILBOUNCESHARED" }

{% alert note %}
Es kann vorkommen, dass für dieselbe Nutzer:in mehrere Zeilen zu einem einzelnen Hard Bounce angezeigt werden. Das kann passieren, wenn Ereignisse asynchron verarbeitet werden oder wenn zusammenhängende Sendungen unterschiedliche `dispatch_id`-Werte haben. Beim Deduplizieren oder Analysieren von Exporten sollten Sie `dispatch_id`, `time` und `id` gemeinsam berücksichtigen.
{% endalert %}

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`url` | `null,`&nbsp;`string` | URL, auf die die/der Nutzer:in geklickt hat
`user_agent` | `null,`&nbsp;`string` | User-Agent, über den der Klick erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`link_id` | `null,`&nbsp;`string` | Eindeutige ID für den geklickten Link, wie von Braze erstellt
`link_alias` | `null,`&nbsp;`string` | Alias, der mit dieser Link-ID verknüpft ist
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absende-Domain für die E-Mail
`is_amp` | `null, boolean` | Gibt an, ob es sich um ein AMP-Ereignis handelt
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`suspected_bot_click_reason` | `null, object` | Warum dieses Ereignis als Bot klassifiziert wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILCLICKSHARED #USERSMESSAGESEMAILCLICKSHARED" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der/des Nutzer:in
`recipient_domain` | `null,`&nbsp;`string` | E-Mail-Domain der/des Empfänger:in
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (Sparkpost, Sendgrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absende-Domain für die E-Mail
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der der E-Mail-Versand erfolgte
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`deferral_reason` | `null,`&nbsp;`string` | [PII] Der SMTP-Ursachencode und die benutzerfreundliche Nachricht, die für dieses Zurückstellungs-Ereignis empfangen wurden
`attempt_count` | `null, int` | Anzahl der Versuche, die Nachricht zu senden
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDEFERRALSHARED #USERSMESSAGESEMAILDEFERRALSHARED" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der die E-Mail gesendet wurde
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absende-Domain für die E-Mail
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILDELIVERYSHARED #USERSMESSAGESEMAILDELIVERYSHARED" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`user_agent` | `null,`&nbsp;`string` | User-Agent, über den der Spam-Bericht erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absende-Domain für die E-Mail
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILMARKASSPAMSHARED #USERSMESSAGESEMAILMARKASSPAMSHARED" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`user_agent` | `null,`&nbsp;`string` | User-Agent, über den die Öffnung erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`machine_open` | `null,`&nbsp;`string` | Wird auf „true“ gesetzt, wenn das Öffnungs-Ereignis ohne Nutzerinteraktion ausgelöst wird, z. B. durch ein Apple-Gerät mit aktiviertem E-Mail-Datenschutz. Der Wert kann sich im Laufe der Zeit ändern, um mehr Granularität zu bieten.
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absende-Domain für die E-Mail
`is_amp` | `null, boolean` | Gibt an, ob es sich um ein AMP-Ereignis handelt
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILOPENSHARED #USERSMESSAGESEMAILOPENSHARED" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absende-Domain für die E-Mail
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSENDSHARED #USERSMESSAGESEMAILSENDSHARED" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der der E-Mail-Versand erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`bounce_reason` | `null,`&nbsp;`string` | [PII] Der SMTP-Ursachencode und die benutzerfreundliche Nachricht, die für dieses Bounce-Ereignis empfangen wurden
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absende-Domain für die E-Mail
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILSOFTBOUNCESHARED #USERSMESSAGESEMAILSOFTBOUNCESHARED" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Diese Tabelle protokolliert E-Mail-Abmeldungen auf Nachrichtenebene von Empfängerseite: Klick auf einen Abmelde-Link, die Ein-Klick-List-Unsubscribe-Funktion des E-Mail-Clients, Einreichungen über das Preference Center sowie vom ESP gemeldete Abmeldungen. Abmeldungen, die über die REST API vorgenommen werden, sind nicht enthalten; diese erzeugen stattdessen [`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events)- oder [`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events)-Ereignisse.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser/diesem Nutzer:in verknüpft ist, wenn sie/er anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
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
`email_address` | `string` | [PII] E-Mail-Adresse der/des Nutzer:in
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESEMAILUNSUBSCRIBESHARED #USERSMESSAGESEMAILUNSUBSCRIBESHARED" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Ereignis tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | [PII] Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`retry_type` | `null,`&nbsp;`string` | Typ der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zur Wiederholung
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
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
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der/des Nutzer:in
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, von dem der E-Mail-Versand durchgeführt wurde
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
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
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`feature_flag_id_name` | `null,`&nbsp;`string` | Der Feature-Flag-Rollout-Bezeichner
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`browser` | `null,`&nbsp;`string` | Gerätebrowser – extrahiert aus user_agent –, auf dem das Öffnen stattfand
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED #USERSMESSAGESFEATUREFLAGIMPRESSIONSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer:innen-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
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
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`version` | `string` | Version der In-App-Nachricht, Legacy oder getriggert
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`abort_type` | `null,`&nbsp;`string` | Typ des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEABORTSHARED #USERSMESSAGESINAPPMESSAGEABORTSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer:innen-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
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
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`version` | `string` | Version der In-App-Nachricht, Legacy oder getriggert
`button_id` | `null,`&nbsp;`string` | ID des angeklickten Buttons, wenn dieser Klick einen Button-Klick darstellt
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGECLICKSHARED #USERSMESSAGESINAPPMESSAGECLICKSHARED" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer:innen-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
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
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`version` | `string` | Version der In-App-Nachricht, Legacy oder getriggert
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`locale_key` | `null,`&nbsp;`string` | [PII] Der Schlüssel, der den Übersetzungen entspricht (z. B. „en-us“), die zum Verfassen dieser Nachricht verwendet wurden (null für Standard).
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED #USERSMESSAGESINAPPMESSAGEIMPRESSIONSHARED" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (bis zu 128 Zeichen)
`abort_type` | `null,`&nbsp;`string` | Typ des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der die Nachricht gesendet oder empfangen wurde
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINEABORTSHARED #USERSMESSAGESLINEABORTSHARED" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der die Nachricht gesendet oder empfangen wurde
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`short_url` | `null,`&nbsp;`string` | Gekürzte URL, die angeklickt wurde
`url` | `null,`&nbsp;`string` | URL, die die/der Nutzer:in angeklickt hat
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem der Spam-Bericht aufgetreten ist
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
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`media_id` | `null,`&nbsp;`string` | Die von LINE generierte ID, die zum Abrufen eingehender Medien von LINE verwendet werden kann
`message_body` | `null,`&nbsp;`string` | Getippte Antwort der/des Nutzer:in
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der die Nachricht gesendet oder empfangen wurde
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
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
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der die Nachricht gesendet oder empfangen wurde
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINESENDSHARED #USERSMESSAGESLINESENDSHARED" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Ereignis tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | [PII] Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`retry_type` | `null,`&nbsp;`string` | Typ der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zur Wiederholung
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID der/des Nutzer:in, von der die Nachricht gesendet oder empfangen wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLINERETRYSHARED #USERSMESSAGESLINERETRYSHARED" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`activity_id` | `null,`&nbsp;`string` | Live-Activity-Bezeichner
`activity_attributes_type` | `null,`&nbsp;`string` | Attributtyp der Live Activity
`push_to_start_token` | `null,`&nbsp;`string` | Push-to-Start-Token der Live Activity
`update_token` | `null,`&nbsp;`string` | Update-Token der Live Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Ereignistyp der Live Activity. Einer von ['start', 'update', 'end']
`live_activity_event_outcome` | `null,`&nbsp;`string` | Ergebnis des Live-Activity-Ereignisses
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYOUTCOMESHARED #USERSMESSAGESLIVEACTIVITYOUTCOMESHARED" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`activity_id` | `null,`&nbsp;`string` | Live-Activity-Bezeichner
`activity_attributes_type` | `null,`&nbsp;`string` | Attributtyp der Live Activity
`push_to_start_token` | `null,`&nbsp;`string` | Push-to-Start-Token der Live Activity
`update_token` | `null,`&nbsp;`string` | Update-Token der Live Activity
`live_activity_event_type` | `null,`&nbsp;`string` | Ereignistyp der Live Activity. Einer von ['start', 'update', 'end']
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESLIVEACTIVITYSENDSHARED #USERSMESSAGESLIVEACTIVITYSENDSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Gerätebrowser – extrahiert aus user_agent –, auf dem das Öffnen stattfand
`abort_type` | `null,`&nbsp;`string` | Typ des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (bis zu 128 Zeichen)
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDABORTSHARED #USERSMESSAGESNEWSFEEDCARDABORTSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Gerätebrowser – extrahiert aus user_agent –, auf dem das Öffnen stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDCLICKSHARED #USERSMESSAGESNEWSFEEDCARDCLICKSHARED" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer:innen-ID der Person, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der/des Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Card
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der/des Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der/des Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der/des Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Gerätebrowser – extrahiert aus user_agent –, auf dem das Öffnen stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED #USERSMESSAGESNEWSFEEDCARDIMPRESSIONSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer:innen-ID der/des Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, an die ein Zustellversuch unternommen wurde
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
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
`abort_type` | `null,`&nbsp;`string` | Typ des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONABORTSHARED #USERSMESSAGESPUSHNOTIFICATIONABORTSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer:innen-ID der/des Nutzer:in
`push_token` | `null,`&nbsp;`string` | Push-Token, das einen Bounce verursacht hat
`device_id` | `null,`&nbsp;`string` | `device_id`, an die ein Zustellversuch unternommen wurde, der einen Bounce verursachte
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
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
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED #USERSMESSAGESPUSHNOTIFICATIONBOUNCESHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer:innen-ID der/des Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
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
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONINFLUENCEDOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Dieses Ereignis wird vom [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) nicht unterstützt und ist im [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) veraltet.
{% endalert %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Betriebssystemversion des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED #USERSMESSAGESPUSHNOTIFICATIONIOSFOREGROUNDSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Ereignisses verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Betriebssystemversion des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`button_string` | `null,`&nbsp;`string` | Bezeichner (button_string) des angeklickten Push-Benachrichtigungs-Buttons. Null, wenn nicht durch einen Button-Klick ausgelöst
`button_action_type` | `null,`&nbsp;`string` | Aktionstyp des Push-Benachrichtigungs-Buttons. Einer von [URI, DEEP_LINK, NONE, CLOSE]. Null, wenn nicht durch einen Button-Klick ausgelöst
`slide_id` | `null,`&nbsp;`string` | Folienbezeichner der Push-Karussell-Folie, auf die die Nutzer:in geklickt hat
`slide_action_type` | `null,`&nbsp;`string` | Aktionstyp der Push-Karussell-Folie
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONOPENSHARED #USERSMESSAGESPUSHNOTIFICATIONOPENSHARED" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`push_token` | `null,`&nbsp;`string` | Push-Token, an das ein Zustellversuch unternommen wurde
`device_id` | `null,`&nbsp;`string` | `device_id`, an die ein Zustellversuch unternommen wurde
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, auf der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`platform` | `string` | Plattform des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`is_sampled` | `null,`&nbsp;`string` | Gibt an, ob der Push-Versand gesampelt wurde und ein Zustellereignis erwartet wird
`locale_key` | `null,`&nbsp;`string` | [PII] Der Schlüssel, der den Übersetzungen entspricht (zum Beispiel „en-us“), die zum Verfassen dieser Nachricht verwendet wurden (null für Standard).
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESPUSHNOTIFICATIONSENDSHARED #USERSMESSAGESPUSHNOTIFICATIONSENDSHARED" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (bis zu 128 Zeichen)
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese Nutzer:in erhalten hat
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSABORTSHARED #USERSMESSAGESRCSABORTSHARED" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`short_url` | `null,`&nbsp;`string` | Verkürzte URL, die angeklickt wurde
`suspected_bot_click_reason` | `null,`&nbsp;`string` | Warum dieses Ereignis als Bot-Klick klassifiziert wurde
`user_agent` | `null,`&nbsp;`string` | User-Agent, bei dem der Spam-Bericht aufgetreten ist
`user_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Nutzer:in, von der die Nachricht empfangen wurde
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`interaction_type` | `null,`&nbsp;`string` | Der Interaktionstyp, der den Klick ausgelöst hat. Beispielhafte String-Werte: Text URL, Reply, OpenURL
`element_label` | `null,`&nbsp;`string` | Optionale Details zum angeklickten Element, z. B. der Text eines vorgeschlagenen Antwort-Buttons
`element_type` | `null,`&nbsp;`string` | Gibt an, ob ein interaction_type, der sowohl für Vorschläge als auch Buttons gilt, von einem Vorschlag oder Button stammt. Beispiele: Suggestion, Button
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`url` | `null,`&nbsp;`string` | URL, auf die die Nutzer:in geklickt hat
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese Nutzer:in erhalten hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSCLICKSHARED #USERSMESSAGESRCSCLICKSHARED" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der empfangenden Nutzer:in im E.164-Format (zum Beispiel +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`from_rcs_sender` | `null,`&nbsp;`string` | Die RCS-Absender-ID oder der Agentname, die/der zum Senden der Nachricht verwendet wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSDELIVERYSHARED #USERSMESSAGESRCSDELIVERYSHARED" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`action` | `null,`&nbsp;`string` | Aktion, die als Reaktion auf diese Nachricht ausgeführt wurde. (Zum Beispiel Subscribed, Unsubscribed oder None).
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`media_urls` | `null,`&nbsp;`string` | Medien-URLs der Nutzer:in
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`user_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Nutzer:in, von der die Nachricht empfangen wurde
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`message_body` | `null,`&nbsp;`string` | Eingegebene Antwort der Nutzer:in
`to_rcs_sender` | `null,`&nbsp;`string` | Der eingehende RCS-Absender, an den die Nachricht gesendet wurde
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSINBOUNDRECEIVESHARED #USERSMESSAGESRCSINBOUNDRECEIVESHARED" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese Nutzer:in erhalten hat
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der empfangenden Nutzer:in im E.164-Format (zum Beispiel +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREADSHARED #USERSMESSAGESRCSREADSHARED" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`error` | `null,`&nbsp;`string` | Fehlername
`from_rcs_sender` | `null,`&nbsp;`string` | Die RCS-Absender-ID oder der Agentname, die/der zum Senden der Nachricht verwendet wurde
`is_sms_fallback` | `null, boolean` | Gibt an, ob für diese abgelehnte RCS-Nachricht ein SMS-Fallback versucht wurde. Dieses Feld ist mit dem SMS-Zustellereignis verknüpft/gepaart
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode des Anbieters
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der empfangenden Nutzer:in im E.164-Format (zum Beispiel +14155552671)
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSREJECTIONSHARED #USERSMESSAGESRCSREJECTIONSHARED" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese Nutzer:in erhalten hat
`category` | `null,`&nbsp;`string` | Name der Keyword-Kategorie, wird nur bei Auto-Reply-Nachrichten befüllt: „opt-in“, „opt-out“, „help“ oder ein angepasster Wert
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`from_rcs_sender` | `null,`&nbsp;`string` | Die RCS-Absender-ID oder der Agentname, die/der zum Senden der Nachricht verwendet wurde
`message_extras` | `null,`&nbsp;`string` | Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der empfangenden Nutzer:in im E.164-Format (zum Beispiel +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESRCSSENDSHARED #USERSMESSAGESRCSSENDSHARED" }

## SMS-Nachrichtenereignisse und gelöschte Nutzerprofile {#sms-message-events-and-deleted-user-profiles}

{% alert note %}
Für gemeinsam genutzte `USERS_MESSAGES_SMS_*`-Tabellen (einschließlich [`USERS_MESSAGES_SMS_REJECTION_SHARED`](#USERS_MESSAGES_SMS_REJECTION_SHARED), [`USERS_MESSAGES_SMS_DELIVERY_SHARED`](#USERS_MESSAGES_SMS_DELIVERY_SHARED) und [`USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED`](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED)) schreibt Braze nur dann eine Zeile, wenn das Braze-Nutzerprofil zum Zeitpunkt der Verarbeitung des Ereignisses für Snowflake Data Sharing und Currents noch im Workspace vorhanden ist. Falls die Nutzer:in vor Abschluss der Verarbeitung gelöscht wurde, erscheint das Ereignis weder in Snowflake noch in Ihrem Currents-Export, auch wenn die SMS-Workspace-Metriken im Dashboard weiterhin aggregierte Zahlen aus dem Braze-Reporting-Pfad widerspiegeln. Informationen zum entsprechenden Currents-Verhalten finden Sie unter [SMS-Rejection-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#sms-rejection-events) und verwandte SMS-Ereignistypen im selben Glossar.
{% endalert %}

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSABORTSHARED #USERSMESSAGESSMSABORTSHARED" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfänger:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die SMS gesendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSCARRIERSENDSHARED #USERSMESSAGESSMSCARRIERSENDSHARED" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfänger:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die SMS gesendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Ist mit dem SMS-Delivery-Ereignis verknüpft/gekoppelt
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYSHARED #USERSMESSAGESSMSDELIVERYSHARED" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfänger:in
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`error` | `null,`&nbsp;`string` | Fehlername
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode des SMS-Anbieters
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Ist mit dem SMS-Delivery-Ereignis verknüpft/gekoppelt
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSDELIVERYFAILURESHARED #USERSMESSAGESSMSDELIVERYFAILURESHARED" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `null,`&nbsp;`string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, der mit der eingehenden Telefonnummer verknüpft ist
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`user_phone_number` | `string` | [PII] Telefonnummer der Nutzer:in, von der die Nachricht empfangen wurde
`subscription_group_id` | `null,`&nbsp;`string` | ID der Abo-Gruppe, die als Ziel für diese SMS verwendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe, die als Ziel für diese SMS verwendet wurde
`inbound_phone_number` | `string` | Eingehende Nummer, an die die Nachricht gesendet wurde
`action` | `string` | Als Reaktion auf diese Nachricht ausgeführte Aktion. Zum Beispiel `Subscribed`, `Unsubscribed` oder `None`.
`message_body` | `string` | Antwort der Nutzer:in
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Medien-URLs der Nutzer:in
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, zu der dieses Ereignis gehört
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, zu der dieses Ereignis gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSINBOUNDRECEIVESHARED #USERSMESSAGESSMSINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfänger:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die SMS gesendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`error` | `null,`&nbsp;`string` | Fehlername
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode des SMS-Anbieters
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Ist mit dem SMS-Delivery-Ereignis verknüpft/gekoppelt
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSREJECTIONSHARED #USERSMESSAGESSMSREJECTIONSHARED" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfänger:in
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`category` | `null,`&nbsp;`string` | Name der Keyword-Kategorie, nur bei automatischen Antwortnachrichten befüllt: 'Opt-in', 'Opt-out', 'Help' oder benutzerdefinierter Wert
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSENDSHARED #USERSMESSAGESSMSSENDSHARED" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `null,`&nbsp;`string` | Braze-ID der Nutzer:in, die von short_url angesprochen wurde, null wenn short_url kein Nutzer-Klick-Tracking verwendet hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in, die von short_url angesprochen wurde, sofern vorhanden, null wenn short_url kein Nutzer-Klick-Tracking verwendet hat
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, der zum Generieren der short_url verwendet wurde
`time` | `int` | Unix-Zeitstempel, zu dem die short_url angeklickt wurde
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`campaign_id` | `null,`&nbsp;`string` | Braze-ID der Campaign, für die die short_url generiert wurde, null wenn nicht aus einer Campaign
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, für die die short_url generiert wurde, null wenn nicht aus einer Campaign
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, für die die short_url generiert wurde, null wenn nicht aus einer Campaign
`canvas_id` | `null,`&nbsp;`string` | Braze-ID des Canvas, für den die short_url generiert wurde, null wenn nicht aus einem Canvas
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, für den die short_url generiert wurde, null wenn nicht aus einem Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, für die die short_url generiert wurde, null wenn nicht aus einem Canvas
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, für den die short_url generiert wurde, null wenn nicht aus einem Canvas
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, für die die short_url generiert wurde, null wenn nicht aus einem Canvas
`url` | `string` | Original-URL in der Nachricht, auf die die short_url weiterleitet
`short_url` | `string` | Verkürzte URL, die angeklickt wurde
`user_agent` | `null,`&nbsp;`string` | User-Agent, der die short_url anfordert
`user_phone_number` | `string` | [PII] Telefonnummer der Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`suspected_bot_click_reason` | `null, object` | Warum dieses Ereignis als Bot klassifiziert wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSSHORTLINKCLICKSHARED #USERSMESSAGESSMSSHORTLINKCLICKSHARED" }

### USERS_MESSAGES_SMS_RETRY_SHARED {#USERS_MESSAGES_SMS_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Ereignis tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | [PII] Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe
`retry_type` | `null,`&nbsp;`string` | Art des Wiederholungsversuchs
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zum Wiederholungsversuch
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESSMSRETRYSHARED #USERSMESSAGESSMSRETRYSHARED" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKABORTSHARED #USERSMESSAGESWEBHOOKABORTSHARED" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`http_status_code` | `null, int` | HTTP-Statuscode der Antwort
`endpoint_url` | `null,`&nbsp;`string` | Die angeforderte Endpunkt-URL
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`content_length` | `null, int` | Content-Length der Antwort
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`host` | `null,`&nbsp;`string` | Der Host für die Anfrage
`id` | `string` | Global eindeutige ID für dieses Ereignis
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`raw_response` | `null,`&nbsp;`string` | Gekürzte Rohantwort vom Endpunkt
`retry_count` | `null, int` | Anzahl der unternommenen Wiederholungsversuche
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`url_path` | `null,`&nbsp;`string` | Der Pfad der angeforderten URL
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`webhook_duration` | `null, int` | Gesamtdauer dieser Anfrage in Millisekunden
`webhook_failure_source` | `null,`&nbsp;`string` | Gibt an, ob ein Fehler von Braze oder vom Endpunkt selbst erzeugt wurde. Das Feld source kann „External Endpoint“, „Treat no status code to host unreachable“ sein
`is_terminal` | `null, boolean` | Ob dieses Ereignis der letzte Versuch beim Senden war
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKFAILURESHARED #USERSMESSAGESWEBHOOKFAILURESHARED" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`campaign_name` | `null,`&nbsp;`string` | Name der Campaign
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKSENDSHARED #USERSMESSAGESWEBHOOKSENDSHARED" }

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED {#USERS_MESSAGES_WEBHOOK_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Ereignis tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | [PII] Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`retry_type` | `null,`&nbsp;`string` | Art des Wiederholungsversuchs
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zum Wiederholungsversuch
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWEBHOOKRETRYSHARED #USERSMESSAGESWEBHOOKRETRYSHARED" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`to_phone_number` | 	`null,`&nbsp;`string` | [PII] Telefonnummer der Empfänger:in
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs. Eine Liste der Werte finden Sie unter [Abbruchtypen](#abort-types).
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Details zum Abbruch (maximal 2.000 Zeichen)
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPABORTSHARED #USERSMESSAGESWHATSAPPABORTSHARED" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Ereignis aufgetreten ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis aufgetreten ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`url` | `null,`&nbsp;`string` | URL, auf die die Nutzer:in geklickt hat
`short_url` | `null,`&nbsp;`string` | Verkürzte URL, die angeklickt wurde
`user_agent` | `null,`&nbsp;`string` | User-Agent, bei dem der Spam-Bericht aufgetreten ist
`user_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Nutzer:in, von der die Nachricht empfangen wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPCLICKSHARED #USERSMESSAGESWHATSAPPCLICKSHARED" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfänger:in
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nutzer:in auf einen WhatsApp Flow antwortet.
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPDELIVERYSHARED #USERSMESSAGESWHATSAPPDELIVERYSHARED" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfänger:in
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode von WhatsApp
`provider_error_title` | `null, `&nbsp;`string` | Fehlertitel von WhatsApp
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nutzer:in auf einen WhatsApp Flow antwortet.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPFAILURESHARED #USERSMESSAGESWHATSAPPFAILURESHARED" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`user_phone_number` | `string` | [PII] Telefonnummer der Nutzer:in, von der die Nachricht empfangen wurde
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`inbound_phone_number` | `string` | Eingehende Nummer, an die die Nachricht gesendet wurde
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`message_body` | `string` | Antwort der Nutzer:in
`quick_reply_text` | `string` | Text des von der Nutzer:in gedrückten Buttons
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Medien-URLs der Nutzer:in
`action` | `string` | Als Reaktion auf diese Nachricht ausgeführte Aktion. Zum Beispiel `Subscribed`, `Unsubscribed` oder `None`.
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`catalog_id` | `null,`&nbsp;`string` | Katalog-ID eines Produkts, wenn ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls leer.
`product_id` | `null,`&nbsp;`string` | ID des gekauften Produkts
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nutzer:in auf einen WhatsApp Flow antwortet.
`flow_response_json` | `null,`&nbsp;`string` | [PII] Die Formularwerte, mit denen die Nutzer:in geantwortet hat. Vorhanden, wenn die Nutzer:in auf einen WhatsApp Flow antwortet.
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
`in_reply_to` | `null,`&nbsp;`string` | Die message_id der Nachricht, auf die diese Nachricht geantwortet hat
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED #USERSMESSAGESWHATSAPPINBOUNDRECEIVESHARED" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Empfänger:in
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nutzer:in auf einen WhatsApp Flow antwortet.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPREADSHARED #USERSMESSAGESWHATSAPPREADSHARED" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis aufgetreten ist
`to_phone_number` | `null,`&nbsp;`string`	| [PII] Telefonnummer der Empfänger:in
`user_id` | `string` | Braze-ID der Nutzer:in, die dieses Ereignis ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Campaign, zu der dieses Ereignis gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Campaign, zu der dieses Ereignis gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Ereignis gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Dispatch, zu dem diese Nachricht gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn die Nutzer:in auf einen WhatsApp Flow antwortet.
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSMESSAGESWHATSAPPSENDSHARED #USERSMESSAGESWHATSAPPSENDSHARED" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% multi_lang_include partners/snowflake_user_attributes_qb_excluded_view_note.md %}

Dieses Ereignis tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungszeitraums erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Ereignis
`user_id` | `string` | [PII] Braze-Nutzer:innen-ID der/des Nutzer:in, die/der dieses Ereignis ausgeführt hat
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
`retry_log` | `null,`&nbsp;`string` | Lognachricht mit Details zur Wiederholung
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Ereignis von der Snowpipe erfasst wurde
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
| `time`                      | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Event stattgefunden hat                      |
| `random_bucket_number`      | `int`,&nbsp;`null`       | Aktuelle zufällige Bucket-Nummer, die der/dem Nutzer:in zugewiesen ist    |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | Vorherige zufällige Bucket-Nummer, die der/dem Nutzer:in zugewiesen war   |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSRANDOMBUCKETNUMBERUPDATESHARED #USERSRANDOMBUCKETNUMBERUPDATESHARED" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Feld               | Typ                      | Beschreibung                                                                  |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Event                                         |
| `user_id`          | `string`,&nbsp;`null`    | Braze-ID der/des Nutzer:in, die/der gelöscht wurde                            |
| `app_group_id`     | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                       |
| `app_group_api_id` | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                         |
| `time`             | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem die Nutzerlöschanfrage verarbeitet wurde             |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERDELETEREQUESTSHARED #USERSUSERDELETEREQUESTSHARED" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Feld               | Typ                      | Beschreibung                                                                                       |
| ------------------ | ------------------------ | -------------------------------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Event                                                              |
| `user_id`          | `string`,&nbsp;`null`    | Braze-ID der/des verwaisten Nutzer:in                                                              |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] Externe Nutzer-ID der/des Nutzer:in                                                          |
| `device_id`        | `string`,&nbsp;`null`    | ID des Geräts, das mit dieser/diesem Nutzer:in verknüpft ist, wenn die/der Nutzer:in anonym ist    |
| `app_group_id`     | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                                            |
| `app_group_api_id` | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                                              |
| `app_api_id`       | `string`,&nbsp;`null`    | API-ID der App, zu der die/der verwaiste Nutzer:in gehörte                                         |
| `time`             | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem die/der Nutzer:in verwaist wurde                                          |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | Braze-ID der/des Nutzer:in, deren/dessen Profil mit dem Profil der/des verwaisten Nutzer:in zusammengeführt wurde |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERSUSERORPHANSHARED #USERSUSERORPHANSHARED" }

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

## Abbruchtypen {#abort-types}

{% include currents/abort_types_reference.md combined_content_rendering=true %}