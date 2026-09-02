---
nav_title: "API-Übersicht"
article_title: "API-Übersicht"
page_order: 2.1
description: "Dieser Referenzartikel behandelt die API-Grundlagen, einschließlich dessen, was eine Representational State Transfer API ist, die Terminologie und eine Übersicht über API-Schlüssel."
page_type: reference
alias: /api/api_key/
---

# API-Übersicht {#api-overview}

> Dieser Referenzartikel behandelt die API-Grundlagen, einschließlich gängiger Terminologie und einer Übersicht über Representational State Transfer-API-Schlüssel, Berechtigungen und deren Sicherheit.

## Braze Representational State Transfer API-Sammlung {#braze-rest-api-collection}

| Sammlung                                                                   | Zweck                                                                                          |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [Catalogs]({{site.baseurl}}/api/endpoints/catalogs)                       | Erstellen und verwalten Sie Kataloge und Katalogartikel, auf die Sie in Ihren Braze-Campaigns verweisen können. |
| [Cloud-Datenaufnahme]({{site.baseurl}}/api/endpoints/cdi)                 | Verwalten Sie Ihre Data-Warehouse-Integrationen und -Synchronisierungen.                       |
| [E-Mail-Listen und -Adressen]({{site.baseurl}}/api/endpoints/email)       | Richten Sie eine bidirektionale Synchronisierung zwischen Braze und Ihren E-Mail-Systemen ein und verwalten Sie diese. |
| [Export]({{site.baseurl}}/api/endpoints/export)                           | Greifen Sie auf verschiedene Details Ihrer Campaigns, Canvase, KPIs und mehr zu und exportieren Sie diese. |
| [Medienbibliothek]({{site.baseurl}}/api/endpoints/media_library)          | Verwalten Sie Assets in Braze.                                                                 |
| [Nachrichten]({{site.baseurl}}/api/endpoints/messaging)                   | Planen, senden und verwalten Sie Ihre Campaigns und Canvase.                                  |
| [Präferenzzentrum]({{site.baseurl}}/api/endpoints/preference_center)      | Erstellen Sie Ihr Präferenzzentrum und Update or aktualisieren or aktualisieren Sie dessen Darstellung.                    |
| [SCIM]({{site.baseurl}}/api/endpoints/scim)                               | Verwalten Sie Nutzer:innenidentitäten in cloudbasierten Anwendungen und Diensten.              |
| [Kurzmitteilungsdienst or SMS]({{site.baseurl}}/api/endpoints/sms)                                 | Verwalten Sie die Telefonnummern Ihrer Nutzer:innen in Ihren Abo-Gruppen.                      |
| [Abo-Gruppen]({{site.baseurl}}/api/endpoints/subscription_groups)         | Listen Sie Kurzmitteilungsdienst or SMS- und E-Mail-Abo-Gruppen auf, die im Braze-Dashboard gespeichert sind, und Update or aktualisieren or aktualisieren Sie diese. |
| [Templates]({{site.baseurl}}/api/endpoints/templates)                     | Erstellen und Update or aktualisieren or aktualisieren Sie Templates für E-Mail-Messaging und Content Blocks.             |
| [Nutzerdaten]({{site.baseurl}}/api/endpoints/user_data)                   | Identifizieren, verfolgen und verwalten Sie Ihre Nutzer:innen.                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze Representational State Transfer API-Sammlung" }

## API-Definitionen {#api-definitions}

Im Folgenden finden Sie eine Übersicht der Begriffe, die Ihnen in der Braze Representational State Transfer API-Dokumentation begegnen können.

### Endpunkte {#endpoints}

Braze verwaltet eine Reihe verschiedener Instanzen für unser Dashboard und unsere Representational State Transfer-Endpunkte. Wenn Ihr Konto eingerichtet wird, melden Sie sich bei einer der folgenden URLs an. Verwenden Sie den richtigen Representational State Transfer-Endpunkt basierend auf der Instanz, der Sie zugewiesen sind. Falls Sie sich nicht sicher sind, eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support) oder nutzen Sie die folgende Tabelle, um die URL des von Ihnen verwendeten Dashboards dem richtigen Representational State Transfer-Endpunkt zuzuordnen.

So finden Sie Ihren Representational State Transfer-Endpunkt in Braze:

1. Melden Sie sich bei Braze an und navigieren Sie zu **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel**.
2. Wählen Sie einen vorhandenen API-Schlüssel aus oder wählen Sie **API-Schlüssel erstellen**, um einen neuen Schlüssel anzulegen.
3. Kopieren Sie den auf diesem Tab angezeigten Representational State Transfer-Endpunkt und verwenden Sie diesen Endpunkt für Ihre API-Anfragen.

{% alert important %}
Wenn Sie Endpunkte für API-Aufrufe verwenden, nutzen Sie den Representational State Transfer-Endpunkt.

Für die SDK or Software-Development-Kit-Integration verwenden Sie den [SDK or Software-Development-Kit-Endpunkt]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), nicht den Representational State Transfer-Endpunkt.
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

### API-Limits

Für die meisten APIs hat Braze ein Standard-Rate-Limit von 250.000 Anfragen pro Stunde. Bestimmte Anfragetypen haben jedoch eigene Rate-Limits, um große Datenmengen über den gesamten Kundenstamm hinweg besser verarbeiten zu können. Weitere Informationen finden Sie unter [API-Rate-Limits]({{site.baseurl}}/api/api_limits).

### Nutzer-IDs {#user-ids}

- **Externe Nutzer-ID**: Die `external_id` dient als eindeutiger Bezeichner für die Nutzer:innen, für die Sie Daten übermitteln. Dieser Bezeichner sollte derselbe sein, den Sie im Braze SDK or Software-Development-Kit festlegen, um die Erstellung mehrerer Profile für dieselbe Person zu vermeiden.
- **Braze-Nutzer-ID**: Die `braze_id` dient als eindeutiger Bezeichner für Nutzer:innen, der von Braze vergeben wird. Sie können diesen Bezeichner verwenden, um Nutzer:innen über die Representational State Transfer API zusätzlich zu external_ids zu löschen.

Weitere Informationen finden Sie in den folgenden Artikeln basierend auf Ihrer Plattform: [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=android) und [Internet]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web).

## Über Representational State Transfer-API-Schlüssel {#about-rest-api-keys}

Ein Representational State Transfer-Application-Programming-Interface-Schlüssel (Representational State Transfer-API-Schlüssel) ist ein eindeutiger Code, den Sie an eine API übergeben, um den API-Aufruf zu authentifizieren und die aufrufende Anwendung oder den aufrufenden Nutzer zu identifizieren. Sie greifen über HTTPS-Webanfragen an den Representational State Transfer-API-Endpunkt Ihres Unternehmens auf die API zu. Representational State Transfer-API-Schlüssel arbeiten zusammen mit App-Identifier-Schlüsseln, um Daten zu verfolgen, abzurufen, zu senden, zu exportieren und zu analysieren und so sicherzustellen, dass alles reibungslos funktioniert.

Workspaces und API-Schlüssel gehören bei Braze zusammen. Workspaces sind dafür konzipiert, Versionen derselben Anwendung über mehrere Plattformen hinweg zu verwalten. Viele Kund:innen nutzen Workspaces auch, um kostenlose und Premium-Versionen ihrer Anwendungen auf derselben Plattform zu verwalten. Wie Sie vielleicht bemerken, nutzen diese Workspaces ebenfalls die Representational State Transfer API und verfügen über eigene Representational State Transfer-API-Schlüssel. Diese Schlüssel können individuell konfiguriert werden, um Zugriff auf bestimmte Endpunkte der API zu gewähren. Jeder API-Aufruf muss einen Schlüssel mit Zugriff auf den aufgerufenen Endpunkt enthalten.

Wir bezeichnen sowohl den Representational State Transfer-API-Schlüssel als auch den Workspace-API-Schlüssel als `api_key`. Der `api_key` ist in jeder Anfrage als Anfrage-Header enthalten und dient als Authentifizierungsschlüssel, der Ihnen die Nutzung unserer Representational State Transfer APIs ermöglicht. Diese Representational State Transfer APIs werden verwendet, um Nutzer:innen zu tracken, Nachrichten zu senden, Nutzerdaten zu exportieren und mehr. Wenn Sie einen neuen Representational State Transfer-API-Schlüssel erstellen, müssen Sie ihm Zugriff auf bestimmte Endpunkte gewähren. Durch die Zuweisung spezifischer Berechtigungen an einen API-Schlüssel können Sie genau einschränken, welche Aufrufe ein API-Schlüssel authentifizieren kann.

![Panel für Representational State Transfer-API-Schlüssel im Tab „API-Schlüssel“.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
Neben Representational State Transfer-API-Schlüsseln gibt es auch einen Schlüsseltyp namens Identifier-Schlüssel, der verwendet werden kann, um bestimmte Elemente wie Apps, Templates, Canvase, Campaigns, Content Cards und Segmente über die API zu referenzieren. Weitere Informationen finden Sie unter [API-Bezeichnertypen]({{site.baseurl}}/api/identifier_types).
{% endalert %}

### Representational State Transfer-API-Schlüssel erstellen {#creating-rest-api-keys}

So erstellen Sie einen neuen Representational State Transfer-API-Schlüssel:

1. Navigieren Sie zu **Einstellungen** > **APIs und Bezeichner**.
2. Wählen Sie **API-Schlüssel erstellen**.
3. Geben Sie Ihrem neuen Schlüssel einen Namen zur schnellen Identifizierung.
4. Geben Sie [erlaubte IP-Adressen](#api-ip-allowlisting) und Subnetze für den neuen Schlüssel an.
5. Wählen Sie die [Berechtigungen](#rest-api-key-permissions) aus, die mit Ihrem neuen Schlüssel verknüpft werden sollen.

{% alert important %}
Beachten Sie, dass Sie nach der Erstellung eines neuen API-Schlüssels weder den Berechtigungsumfang noch die erlaubten IPs bearbeiten können. Diese Einschränkung besteht aus Sicherheitsgründen. Wenn Sie den Umfang eines Schlüssels ändern müssen, erstellen Sie einen neuen Schlüssel mit den aktualisierten Berechtigungen und implementieren Sie diesen Schlüssel anstelle des alten. Nachdem Sie Ihre Implementierung abgeschlossen haben, können Sie den alten Schlüssel löschen.
{% endalert %}

### Berechtigungen für Representational State Transfer-API-Schlüssel {#rest-api-key-permissions}

API-Schlüssel-Berechtigungen sind Rechte, die Sie einer Nutzer:in oder Gruppe zuweisen können, um deren Zugriff auf bestimmte API-Aufrufe einzuschränken. Um Ihre Liste der API-Schlüssel-Berechtigungen einzusehen, navigieren Sie zu **Einstellungen** > **APIs und Bezeichner** und wählen Sie Ihren API-Schlüssel aus.

{% tabs %}
{% tab Nutzerdaten %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | Nutzerattribute, angepasste Events und Käufe aufzeichnen. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | Beliebige Nutzer:innen löschen. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias) | Einen neuen Alias für eine:n bestehende:n Nutzer:in erstellen. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) | Eine:n Alias-only-Nutzer:in mit einer externen ID identifizieren. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | Nutzerprofilinformationen anhand der Nutzer-ID abfragen. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | Nutzerprofilinformationen anhand eines Segments abfragen. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) | Zwei bestehende Nutzer:innen zusammenführen. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename) | Die externe ID einer/eines bestehenden Nutzer:in ändern. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove) | Die externe ID einer/eines bestehenden Nutzer:in entfernen. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update) | Einen Alias für eine:n bestehende:n Nutzer:in Update or aktualisieren or aktualisieren. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group) | Nutzerprofilinformationen in der globalen Kontrollgruppe abfragen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

 {% endtab %}
 {% tab E-Mail %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses) | Abgemeldete E-Mail-Adressen abfragen. |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status) | E-Mail-Adressstatus ändern. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces) | Hard-Bounce-E-Mail-Adressen abfragen. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces) | E-Mail-Adressen von Ihrer Hard-Bounce-Liste entfernen. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam) | E-Mail-Adressen von Ihrer Spam-Liste entfernen. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist) | E-Mail-Adressen auf die Blocklist setzen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Nachrichten %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | Eine sofortige Nachricht an bestimmte Nutzer:innen senden. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages) | Den Versand einer Nachricht zu einem bestimmten Zeitpunkt planen. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages) | Eine geplante Nachricht Update or aktualisieren or aktualisieren. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages) | Eine geplante Nachricht löschen. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) | Alle geplanten Broadcast-Nachrichten abfragen. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) | Eine iOS Live Activity Update or aktualisieren or aktualisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Campaigns %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) | Den Versand einer bestehenden Campaign auslösen. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns) | Einen Versand einer Campaign mit API-ausgelöster Zustellung planen. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns) | Eine Campaign mit API-ausgelöster Zustellung Update or aktualisieren or aktualisieren. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages) | Eine Campaign mit API-ausgelöster Zustellung löschen. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns) | Eine Liste von Campaigns abfragen. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | Campaign-Analytics über einen Zeitraum abfragen. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | Details einer bestimmten Campaign abfragen. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics) | Nachrichtenversand-Analytics über einen Zeitraum abfragen. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids) | Eine Send-ID für das Tracking von Massenversand erstellen. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | URL-Details einer bestimmten Nachrichtenvariante innerhalb einer Campaign abfragen. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) | Ermöglicht den Versand transaktionaler Nachrichten über den Endpunkt für transaktionales Messaging. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Canvas %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) | Den Versand eines bestehenden Canvas auslösen. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases) | Einen Versand eines Canvas mit API-ausgelöster Zustellung planen. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases) | Einen Canvas mit API-ausgelöster Zustellung Update or aktualisieren or aktualisieren. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases) | Einen Canvas mit API-ausgelöster Zustellung löschen. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | Eine Liste von Canvase abfragen. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | Canvas-Analytics über einen Zeitraum abfragen. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) | Details eines bestimmten Canvas abfragen. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) | Zusammenfassungen der Canvas-Analytics über einen Zeitraum abfragen. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias) | URL-Details einer bestimmten Nachrichtenvariante innerhalb eines Canvas-Schritts abfragen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Segments %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Eine Liste von Segmenten abfragen. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | Segment-Analytics über einen Zeitraum abfragen. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details) | Details eines bestimmten Segments abfragen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Käufe %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id) | Eine Liste der in Ihrer App gekauften Produkte abfragen. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series) | Die gesamten täglichen Ausgaben in Ihrer App über einen Zeitraum abfragen. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases) | Die Gesamtanzahl der täglichen Käufe in Ihrer App über einen Zeitraum abfragen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Ereignisse %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events) | Eine Liste angepasster Events abfragen. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics) | Vorkommen eines angepassten Events über einen Zeitraum abfragen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Sitzungen %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics) | Sitzungen pro Tag über einen Zeitraum abfragen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab KPIs %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date) | Eindeutige aktive Nutzer:innen pro Tag über einen Zeitraum abfragen. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days) | Gesamtzahl der eindeutigen aktiven Nutzer:innen über ein rollendes 30-Tage-Fenster über einen Zeitraum abfragen. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date) | Neue Nutzer:innen pro Tag über einen Zeitraum abfragen. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date) | App-Deinstallationen pro Tag über einen Zeitraum abfragen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Templates %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | Ein neues E-Mail-Template im Dashboard erstellen. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information) | Informationen zu einem bestimmten Template abfragen. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | Eine Liste von E-Mail-Templates abfragen. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | Ein im Dashboard gespeichertes E-Mail-Template Update or aktualisieren or aktualisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Single Sign-on %}

| Berechtigung | Beschreibung |
| --- | --- |
| `sso.saml.login` | Identitätsanbieter-initiierte Anmeldung einrichten. Weitere Informationen finden Sie unter [Service-Provider (SP)-initiierte Anmeldung]({{site.baseurl}}/user_guide/administer/global/saml_single_sign_on/saml_sso_setup). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Content Blocks %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information) | Informationen zu einem bestimmten Template abfragen. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks) | Eine Liste von Content Blocks abfragen. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) | Einen neuen Content-Block im Dashboard erstellen. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block) | Einen bestehenden Content-Block im Dashboard Update or aktualisieren or aktualisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Einstellungscenter %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Ein Einstellungscenter abrufen. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center) | Einstellungscenter auflisten. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center) | Ein Einstellungscenter erstellen oder Update or aktualisieren or aktualisieren. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Einen Link zum Einstellungscenter für eine:n Nutzer:in abrufen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Abo %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) | Abo-Gruppenstatus festlegen. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) | Abo-Gruppenstatus abrufen. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) | Den Status der Abo-Gruppen abrufen, für die bestimmte Nutzer:innen explizit angemeldet oder abgemeldet sind. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Kurzmitteilungsdienst or SMS %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers) | Ungültige Telefonnummern abfragen. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers) | Die Markierung für ungültige Telefonnummern von Nutzer:innen entfernen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab Kataloge %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk) | Mehrere Artikel zu einem bestehenden Katalog hinzufügen. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk) | Mehrere Artikel in einem bestehenden Katalog Update or aktualisieren or aktualisieren. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Mehrere Artikel aus einem bestehenden Katalog löschen. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details) | Einen einzelnen Artikel aus einem bestehenden Katalog abrufen. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | Einen einzelnen Artikel in einem bestehenden Katalog Update or aktualisieren or aktualisieren. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item) | Einen einzelnen Artikel in einem bestehenden Katalog erstellen. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item) | Einen einzelnen Artikel aus einem bestehenden Katalog löschen. |
| `catalogs.replace_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item) | Einen einzelnen Artikel in einem bestehenden Katalog ersetzen. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog) | Einen Katalog erstellen. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs) | Eine Liste von Katalogen abrufen. |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog) | Einen Katalog löschen. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk) | Vorschau der Artikel eines bestehenden Katalogs abrufen. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) | Artikel in einem bestehenden Katalog ersetzen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% tab SDK or Software-Development-Kit-Authentifizierung %}

| Berechtigung | Endpunkt | Beschreibung |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | Einen neuen SDK or Software-Development-Kit-Authentifizierungsschlüssel für Ihre App erstellen. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key) | Einen SDK or Software-Development-Kit-Authentifizierungsschlüssel als primären Schlüssel für Ihre App markieren. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | Einen SDK or Software-Development-Kit-Authentifizierungsschlüssel für Ihre App löschen. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Alle SDK or Software-Development-Kit-Authentifizierungsschlüssel für Ihre App abrufen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Berechtigungen für Representational State Transfer-API-Schlüssel" }

{% endtab %}
{% endtabs %}

### Representational State Transfer-API-Schlüssel verwalten {#managing-rest-api-keys}

Sie können Details bestehender Representational State Transfer-API-Schlüssel einsehen oder sie löschen, indem Sie zu **Einstellungen** > **APIs und Bezeichner** > Tab **API-Schlüssel** navigieren. Beachten Sie, dass Sie Representational State Transfer-API-Schlüssel nach der Erstellung nicht mehr bearbeiten können.

Der Tab **API-Schlüssel** enthält die folgenden Informationen für jeden Schlüssel:

| Feld | Beschreibung |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| API-Schlüssel-Name | Der Name, der dem Schlüssel bei der Erstellung gegeben wurde. |
| Bezeichner | Der API-Schlüssel. |
| Erstellt von | Die E-Mail-Adresse der Nutzer:in, die den Schlüssel erstellt hat. Dieses Feld zeigt „N/A“ für Schlüssel an, die vor Juni 2023 erstellt wurden. |
| Erstellungsdatum | Das Datum, an dem dieser Schlüssel erstellt wurde. |
| Zuletzt gesehen | Das Datum, an dem dieser Schlüssel zuletzt verwendet wurde. Dieses Feld zeigt „N/A“ für Schlüssel an, die noch nie verwendet wurden. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Representational State Transfer-API-Schlüssel verwalten" }

Um die Details eines API-Schlüssels einzusehen, fahren Sie mit der Maus über den Schlüssel und wählen Sie <i class="fa-solid fa-eye" alt="Anzeigen"></i> **Anzeigen**. Dies umfasst alle Berechtigungen dieses Schlüssels, die erlaubten IPs (falls vorhanden) und ob dieser Schlüssel für das Braze-IP-Whitelisting aktiviert ist.

![Die Liste der API-Schlüssel-Berechtigungen im Braze-Dashboard.]({% image_buster /assets/img_archive/view-api-key.png %})

Beachten Sie, dass beim [Löschen einer Nutzer:in]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) Braze die zugehörigen API-Schlüssel, die diese Nutzer:in erstellt hat, nicht löscht. Um einen Schlüssel zu löschen, fahren Sie mit der Maus über den Schlüssel und wählen Sie <i class="fa-solid fa-trash-can" alt="Löschen"></i> **Löschen**.

![Ein API-Schlüssel mit dem Namen „Last Seen“ und hervorgehobenem Papierkorb-Symbol mit der Beschriftung „Löschen“.]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### Sicherheit von Representational State Transfer-API-Schlüsseln {#rest-api-key-security}

API-Schlüssel werden verwendet, um einen API-Aufruf zu authentifizieren. Wenn Sie einen neuen Representational State Transfer-API-Schlüssel erstellen, müssen Sie ihm Zugriff auf bestimmte Endpunkte gewähren. Durch die Zuweisung spezifischer Berechtigungen an einen API-Schlüssel können Sie genau einschränken, welche Aufrufe ein API-Schlüssel authentifizieren kann.

Da Representational State Transfer-API-Schlüssel Zugriff auf potenziell sensible Representational State Transfer-API-Endpunkte ermöglichen, sichern Sie diese Schlüssel und teilen Sie sie nur mit vertrauenswürdigen Partnern. Sie sollten niemals öffentlich zugänglich gemacht werden. Verwenden Sie diesen Schlüssel beispielsweise nicht für AJAX-Aufrufe von Ihrer Website oder stellen Sie ihn auf andere Weise öffentlich bereit.

Eine gute Sicherheitspraxis ist es, Nutzer:innen nur so viel Zugriff zu gewähren, wie für ihre Arbeit notwendig ist: Dieses Prinzip kann auch auf API-Schlüssel angewendet werden, indem Sie jedem Schlüssel Berechtigungen zuweisen. Diese Berechtigungen bieten Ihnen bessere Sicherheit und Kontrolle über die verschiedenen Bereiche Ihres Kontos.

{% alert warning %}
Da Representational State Transfer-API-Schlüssel Zugriff auf potenziell sensible Representational State Transfer-API-Endpunkte ermöglichen, stellen Sie sicher, dass sie sicher gespeichert und verwendet werden. Verwenden Sie diesen Schlüssel beispielsweise nicht für AJAX-Aufrufe von Ihrer Website oder stellen Sie ihn auf andere Weise öffentlich bereit.
{% endalert %}

Wenn Sie versehentlich einen Schlüssel offenlegen, können Sie ihn in der Entwicklungskonsole löschen. Für Hilfe bei diesem Vorgang erstellen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Sicherheit von Representational State Transfer-API-Schlüsseln und SDK or Software-Development-Kit-API-Schlüsseln {#security-of-rest-api-keys-and-sdk-api-keys}

Representational State Transfer-API-Schlüssel und SDK or Software-Development-Kit-API-Schlüssel haben unterschiedliche Sicherheitsprofile.

| | Representational State Transfer-API-Schlüssel | SDK or Software-Development-Kit-API-Schlüssel |
|---|---|---|
| Zweck | Serverseitige Authentifizierung für die Representational State Transfer API (Nachrichten senden, Daten exportieren, Nutzer:innen verwalten) | Clientseitige Identifizierung für das Braze SDK or Software-Development-Kit (Datenaufnahme, In-App-Nachrichten, Content Cards) |
| Sichtbarkeit | **Muss privat bleiben**. Niemals in clientseitigem Code, öffentlichen Repositories oder Nutzeranwendungen offenlegen. | Für die öffentliche Nutzung konzipiert. Im App-Binary gebündelt oder im Webbrowser-JavaScript sichtbar, ähnlich einer Google-Analytics-Tracking-ID. |
| Lösung bei Offenlegung | Den Schlüssel sofort widerrufen und einen Ersatz unter **Einstellungen** > **APIs und Bezeichner** > **API-Schlüssel** erstellen. Ein offengelegter Representational State Transfer-API-Schlüssel kann zum Senden von Nachrichten, Exportieren von Nutzerdaten oder Ändern von Kontoeinstellungen verwendet werden. | Keine Maßnahme erforderlich. Ein SDK or Software-Development-Kit-API-Schlüssel kann nur Daten aufnehmen und clientseitige Nachrichten abrufen (wie In-App-Nachrichten und Content Cards). Er kann keine Nutzerdaten exportieren, Nachrichten in Ihrem Namen senden oder Campaigns ändern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sicherheit von Representational State Transfer-API-Schlüsseln und SDK or Software-Development-Kit-API-Schlüsseln" }

### API-IP-Allowlisting {#api-ip-allowlisting}

Für zusätzliche Sicherheit können Sie eine Liste von IP-Adressen und Subnetzen festlegen, die Representational State Transfer-API-Anfragen für einen bestimmten Representational State Transfer-API-Schlüssel senden dürfen. Dies wird als Allowlisting oder Whitelisting bezeichnet. Um bestimmte IP-Adressen oder Subnetze zuzulassen, fügen Sie diese beim Erstellen eines neuen Representational State Transfer-API-Schlüssels im Abschnitt **Whitelist IPs** hinzu:

![Option zum Allowlisting von IPs beim Erstellen eines API-Schlüssels.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Wenn Sie keine angeben, können Anfragen von jeder IP-Adresse gesendet werden.

{% alert tip %}
Wenn Sie einen Braze-zu-Braze-Webhook erstellen und Allowlisting verwenden, sehen Sie sich die Liste der [IPs zum Whitelisten]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) an.
{% endalert %}

## API-Authentifizierung und -Sicherheit {#api-authentication-and-security}

### Bearer-Token / Textbaustein-Authentifizierung {#bearer-token-authentication}

Braze authentifiziert Representational State Transfer API-Anfragen mithilfe des Representational State Transfer-API-Schlüssels, der als Bearer-Token / Textbaustein im `Authorization`-Anfrage-Header übergeben wird. Wenn Sie eine Anfrage senden, geben Sie Ihren API-Schlüssel im folgenden Format an:

```bash
Authorization: Bearer YOUR_REST_API_KEY
```

Bei jeder Anfrage führt Braze die folgenden serverseitigen Validierungsprüfungen durch:

1. **Token / Textbaustein-Gültigkeit:** Überprüft, ob der Representational State Transfer-API-Schlüssel in Braze existiert und aktiv ist (zum Beispiel nicht widerrufen oder deaktiviert).
2. **Token / Textbaustein-Autorisierung:** Bestätigt, dass der API-Schlüssel über die erforderlichen Berechtigungen für den angeforderten Endpunkt verfügt.

Wenn die Authentifizierung fehlschlägt, gibt die API eine Fehlerantwort mit einem HTTP-Statuscode zurück. Zum Beispiel zeigt `401 Unauthorized` einen ungültigen oder fehlenden Schlüssel an, während `403 Forbidden` darauf hinweist, dass der Schlüssel keine Berechtigung für den angeforderten Endpunkt hat. Weitere Informationen finden Sie unter [API-Fehler]({{site.baseurl}}/api/errors).

### Groß-/Kleinschreibung von Anfrage-Headern {#header-casing}

HTTP-Header-Namen sind nicht zwischen Groß- und Kleinschreibung unterscheidend, daher sind `Authorization` und `authorization` gleichwertig. Das Gleiche gilt für andere Standard-Anfrage-Header wie `Content-Type`. Senden Sie die Schreibweise, die Ihr HTTP-Client erzeugt.

Braze akzeptiert außerdem jede Schreibweise des `Bearer`-Schemas (`Bearer`, `bearer` oder `BEARER`). Senden Sie den Representational State Transfer-API-Schlüssel selbst genau so, wie er ausgestellt wurde.

### Sicherheit auf Netzwerkebene {#network-level-security}

Representational State Transfer API-Anfragen an Braze werden durch Transport Layer Security (TLS)-Verschlüsselung über den gesamten Anfragepfad geschützt. Die folgende Tabelle beschreibt den Netzwerkfluss für eine API-Anfrage von Ihrem Server an Braze:

| Schritt | Komponente | Beschreibung |
| --- | --- | --- |
| 1 | Ihr Server | Initiiert eine HTTPS-Anfrage mit TLS-Verschlüsselung. |
| 2 | Cloudflare | Beendet die Client-TLS-Verbindung und wendet Schutzmaßnahmen auf Netzwerkebene an. |
| 3 | Network Load Balancer (NLB) | Leitet Pakete an die Anwendungsinfrastruktur weiter. NLBs arbeiten auf Layer 4, das heißt, es findet kein Layer-7-Proxying statt. Pakete werden ohne HTTP-Inspektion oder -Modifikation weitergeleitet. |
| 4 | NGINX Ingress | Beendet die interne TLS-Verbindung und leitet die Anfrage weiter. |
| 5 | Unicorn (Anwendungsserver) | Verarbeitet die authentifizierte Anfrage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Sicherheit auf Netzwerkebene" }

Die TLS-Verschlüsselung deckt jedes Glied in der Kette ab. Ihr Server verbindet sich über TLS mit Cloudflare, und Cloudflare stellt eine separate TLS-Verbindung über den NLB zum NGINX Ingress her, sodass Ihr API-Schlüssel und Ihre Anfragedaten während der Übertragung verschlüsselt bleiben.

## Zusätzliche Ressourcen {#additional-resources}

### Ruby-Client-Bibliothek {#ruby-client-library}

Wenn Sie Braze mit Ruby implementieren, können Sie die [Ruby-Client-Bibliothek](https://github.com/braze-inc/braze-api-client-ruby) verwenden, um die Dauer Ihres Datenimports zu verkürzen. Eine Client-Bibliothek ist eine Sammlung von Code, der auf eine bestimmte Programmiersprache zugeschnitten ist – in diesem Fall Ruby – und die Nutzung einer API erleichtert.

Die Ruby-Client-Bibliothek unterstützt die [Nutzer:innen-Endpunkte]({{site.baseurl}}/api/endpoints/user_data).

{% alert important %}
Diese Client-Bibliothek befindet sich in der Betaphase. Um diese Bibliothek zu verbessern, senden Sie Ihr Feedback an [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}