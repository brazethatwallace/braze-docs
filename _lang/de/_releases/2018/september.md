---
nav_title: September
page_order: 5
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für September 2018."
---
# September 2018

## iOS 12 Benachrichtigungsgruppen: Zusätzliche Funktionen {#ios-12-notification-groups-additional-abilities}

Sie können jetzt über Braze auf [die Features der Benachrichtigungsgruppen von Apple]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) zugreifen! Sie können Zusammenfassungsargumente und Gruppen hinzufügen, kritische Warnungen verwenden, nach provisorisch authentifizierten Nutzer:innen filtern und den Status der provisorischen Authentifizierung in Nutzerprofilen anzeigen.

## Ruhezeiten {#quiet-time}

Kund:innen können jetzt [Ruhezeiten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (die Zeit, in der Ihre Nachrichten nicht gesendet werden) für Canvas festlegen. Gehen Sie einfach zu Ihren **Canvas-Sendeeinstellungen** und aktivieren Sie „Ruhezeiten aktivieren“. Wählen Sie dann Ihre Ruhezeiten in der Ortszeit Ihrer Nutzer:innen und die Aktion, die folgen soll, wenn die Nachricht innerhalb dieser Ruhezeiten ausgelöst wird.

Campaigns verwenden jetzt ebenfalls Ruhezeiten anstelle von „Diese Nachricht während eines bestimmten Teils des Tages senden“.

## Adjust-Kund:innen {#adjust-customers}

Braze-Kund:innen, die [Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/) verwenden, können jetzt ihren Braze-API-Schlüssel und die URL der Braze-Instanz sehen, die sie dann in der Adjust-Plattform zur Integration verwenden.

## Nicht-in-Segment-Filter {#not-in-segment-filter}

Kund:innen können nun ein Segment aus Nutzer:innen erstellen, die [nicht in einem bestimmten Segment enthalten]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting) sind.

## CSV-Exporte von Canvas-Empfänger:innen {#canvas-recipient-csv-exports}

Kund:innen können jetzt [Daten exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/) über die Nutzer:innen, die einen Canvas betreten haben. Die erzeugte CSV-Datei wird der CSV-Datei einer Campaign ähneln.

## Vorläufig autorisierter iOS-12-Segment-Filter {#provisionally-authorized-ios-12-segment-filter}

Es wurde ein [Segment-Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) hinzugefügt, mit dem Sie Nutzer:innen finden können, die unter iOS 12 für eine bestimmte App vorläufig autorisiert sind.

## Bild-Uploader für In-App-Nachrichten {#in-app-message-image-uploader}

Der Bild-Uploader für In-App-Nachrichten wurde vom Design-Panel in das Verfassen-Panel verschoben.

## Nur-Lese-Berechtigungen auf der Nutzerprofil-Seite {#read-only-permissions-on-user-profile-page}

Vor dieser Version konnten Kund:innen den Abo-Status und die E-Mail-Adresse im Nutzerprofil mit [Nur-Lese-Berechtigungen]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions) ändern. Wir haben die Berechtigung `import_user` in die Berechtigung `import_and_update_user` umbenannt und den Bearbeitungszugriff auf den Abo-Status und die E-Mail-Adresse eingeschränkt. Wenn Entwickler:innen nun mit Nur-Lese-Zugriff agieren oder ihnen diese Berechtigung fehlt, können sie den Abo-Status oder die E-Mail-Adresse nicht mehr ändern.