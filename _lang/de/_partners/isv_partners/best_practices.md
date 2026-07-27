---
nav_title: Best Practices
hidden: true
---

# Best Practices für den Nutzerprofil-Lebenszyklus und Bezeichner {#user-lifecycle-and-identifiers-best-practices}

## Datenerfassung {#data-collection}

Erfahren Sie mehr darüber, wie Braze Daten erfasst:
- [SDK-Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection)
- [Best Practices für die Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices)
- [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)

## Braze-Bezeichner {#braze-identifiers}

- `braze_id`: Ein von Braze zugewiesener Bezeichner, der unveränderlich ist und mit einer bestimmten Nutzer:in verknüpft wird, wenn er in unserer Datenbank erstellt wird.
- `external_id`: Ein von der Kund:in zugewiesener Bezeichner, in der Regel eine UUID. Wir empfehlen, die `external_id` zuzuweisen, sobald die Nutzer:in eindeutig identifiziert werden kann. Nachdem eine Nutzer:in identifiziert wurde, kann sie nicht mehr in den anonymen Zustand zurückversetzt werden.
- `user_alias`: Ein eindeutiger alternativer Bezeichner, den die Kund:in zuweisen kann, um die Nutzer:in über eine ID zu referenzieren, bevor eine `external_id` zugewiesen wird. Nutzer-Aliase können später mit anderen Aliasen oder einer `external_id` zusammengeführt werden, wenn eine solche über den Braze-Endpunkt [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) verfügbar wird.
    - Innerhalb des Endpunkts [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) kann das Feld `merge_behavior` verwendet werden, um anzugeben, welche Daten aus dem Nutzer-Alias-Profil im bekannten Nutzerprofil erhalten bleiben sollen.
    - Beachten Sie, dass der Nutzer-Alias nur dann ein sendefähiges Profil ist, wenn Sie E-Mail und/oder Telefon als Standardattribut im Profil hinterlegen.
- `device_id`: Ein automatisch generierter, gerätespezifischer Bezeichner. Einem Nutzerprofil kann eine Reihe von `device_ids` zugeordnet sein. Eine Nutzer:in, die sich beispielsweise auf ihrem Arbeitscomputer, ihrem Heimcomputer, ihrem Tablet und in der iOS-App in ihr Konto eingeloggt hat, hätte 4 `device_ids`, die mit ihrem Profil verknüpft sind.
- E-Mail-Adresse und Telefonnummer:
    - Werden als Bezeichner im Braze-Endpunkt zum Tracking von Nutzer:innen unterstützt.
    - Wenn Sie die E-Mail-Adresse oder Telefonnummer als Bezeichner in einer Anfrage verwenden, gibt es drei mögliche Ergebnisse:
        1. Wenn eine Nutzer:in mit dieser E-Mail/Telefonnummer nicht in Braze existiert, wird ein reines E-Mail-/Telefon-Nutzerprofil erstellt, und alle Daten in der Anfrage werden dem Profil hinzugefügt.
        2. Wenn ein Profil mit dieser E-Mail/Telefonnummer bereits in Braze existiert, wird es aktualisiert und enthält die in der Anfrage gesendeten Daten.
        3. In einem Anwendungsfall mit mehr als einem Profil mit dieser E-Mail/Telefonnummer wird das zuletzt aktualisierte Profil priorisiert.
    - Beachten Sie: Wenn ein reines E-Mail-/Telefon-Nutzerprofil existiert und dann ein identifiziertes Profil mit derselben E-Mail/Telefonnummer erstellt wird (z. B. ein weiteres Profil mit derselben E-Mail-Adresse UND einer externen ID), erstellt Braze ein zweites Profil. Nachfolgende Updates werden an das Profil mit der externen ID weitergeleitet.
        - Die beiden Profile können über den Braze-Endpunkt [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) zusammengeführt werden.

## Umgang mit anonymen Nutzer:innen {#handling-anonymous-users}

Für einen Anwendungsfall, in dem Sie ein Nutzerprofil in Braze erstellen oder aktualisieren müssen, ohne Zugriff auf eine `external_id` zu haben, kann ein anderer Bezeichner wie eine E-Mail-Adresse oder Telefonnummer an den Braze-Endpunkt [Export user by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) übergeben werden, um festzustellen, ob ein Profil für die Nutzer:in in Braze existiert.

```json
{
 "email_address": "test@example.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Wenn eine Nutzer:in mit dieser E-Mail oder Telefonnummer in Braze existiert, wird ihr Profil zurückgegeben. Andernfalls wird ein leeres „users“-Array zurückgegeben. Der Vorteil der Verwendung des Export-Endpunkts zur Prüfung, ob eine Nutzer:in mit dieser E-Mail-Adresse bereits existiert, besteht darin, dass Sie feststellen können, ob anonyme Nutzerprofile mit der Nutzer:in verknüpft sind. Zum Beispiel ein anonymes Profil, das über das SDK erstellt wurde (mit `braze_id`), oder ein zuvor erstelltes Nutzer-Alias-Profil.

Wenn die Anfrage kein Nutzerprofil zurückgibt, können Sie entweder einen Nutzer-Alias oder eine reine E-Mail-Nutzer:in erstellen:

### Nutzer-Alias {#user-alias}

Verwenden Sie den User-Track-Endpunkt, um einen Nutzer-Alias zu erstellen, wobei Sie den von Ihnen gewählten Bezeichner als Alias-Namen verwenden. Indem Sie `_update_existing_only` als `false` im Attribut-, Event- oder Kauf-Objekt angeben, in dem der neue Nutzer-Alias definiert ist, können Sie das Alias-Profil erstellen und gleichzeitig Attribute, Events und Käufe zu diesem Profil hinzufügen.

Damit der Nutzer-Alias ein sendefähiges Profil ist, müssen Sie die E-Mail-Adresse im Feld `email` angeben, wie im folgenden Beispiel gezeigt.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@example.com",
       "alias_label" : "email"
     },
     "email": "test@example.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

Sie können diesen Nutzer-Alias später über unseren Endpunkt [Identify users]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) identifizieren und mit einer `external_id` zusammenführen, wenn eine solche verfügbar wird.

### Erstellen einer reinen E-Mail-Nutzer:in {#creating-an-email-only-user}

Verwenden Sie die E-Mail-Adresse als Bezeichner im User-Track-Endpunkt.

```json
{
    "attributes": [
        {
            "email": "test@example.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
Diese Funktion befindet sich in der Early-Access-Phase.
{% endalert %}

## Synchronisierung von Daten mit Nutzerprofilen {#syncing-data-to-user-profiles}

[User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- Dies ist ein öffentlich zugänglicher Endpunkt, mit dem Nutzer:innen in Braze erstellt und aktualisiert werden können, z. B. durch die Protokollierung von Attributen im Nutzerprofil. Für diesen Endpunkt gilt ein Rate-Limit von 50.000 Anfragen pro Minute auf Workspace-Ebene.
- Wenn Sie diesen Endpunkt verwenden, geben Sie den Schlüssel `partner` an, wie in unserer Partner-Dokumentation beschrieben.

[Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview#what-is-cloud-data-ingestion)
- Ähnlich wie beim User-Track-Endpunkt können Daten über die Cloud-Datenaufnahme mit Nutzerprofilen synchronisiert werden. Wenn Sie dieses Tool verwenden, werden Attribute, Events und Käufe in Profilen protokolliert, indem Sie die Data-Warehouse-Tabelle oder -Ansicht, die Sie mit dem gewünschten Braze-Workspace synchronisieren möchten, einrichten und verbinden.

[Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points)
- Braze hat ein Datenpunktmodell, bei dem Datenpunkte pro „Schreibvorgang“ im Nutzerprofil protokolliert werden, unabhängig davon, ob sich der Wert geändert hat. Aus diesem Grund empfehlen wir, nur die Attribute an Braze zu senden, die sich geändert haben.

## Zielgruppen von Nutzer:innen an Braze senden {#sending-audiences-of-users-to-braze}

[Dokumentation zum Kohortenimport-Sync-Partner]({{site.baseurl}}/partners/isv_partners/cohort_import)<br>
- Zielgruppen von Nutzer:innen können über die Braze-Kohortenimport-API-Endpunkte als Kohorte mit Braze synchronisiert werden. Anstatt diese Zielgruppen als Nutzerattribute im Nutzerprofil zu speichern, können Kund:innen diese Kohorte über einen vom Partner gebrandeten Filter in unserem Segmentierungs-Tool aufbauen und ansprechen. So können Sie ein bestimmtes Segment von Nutzer:innen effizienter finden und targetieren.
- Die Endpunkte für den Kohortenimport sind nicht öffentlich und werden für jeden Partner individuell festgelegt. Aus diesem Grund werden Synchronisierungen mit den Kohorten-Endpunkten nicht auf die Rate-Limits des Workspace einer Kund:in angerechnet.

[User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)<br>
- Dies ist ein öffentlich zugänglicher Endpunkt, der sofort verwendet werden kann, um Nutzer:innen in Braze zu erstellen, indem eine Nutzer:in in einer bestimmten Zielgruppe durch ein Nutzerattribut gekennzeichnet wird. Der Hauptunterschied zwischen diesem Endpunkt und dem Kohortenimport-Endpunkt besteht darin, dass Zielgruppen, die über diesen Endpunkt gesendet werden, im Nutzerprofil gespeichert werden, während der Kohortenimport-Endpunkt als Filter in unserem Segmentierungs-Tool angezeigt wird. Für diesen Endpunkt gilt ein Rate-Limit von 50.000 Anfragen pro Minute auf Workspace-Ebene.
- Wenn Sie diesen Endpunkt verwenden, stellen Sie sicher, dass Sie den Schlüssel `partner` angeben, wie in unserer [Partner-Dokumentation]({{site.baseurl}}/partners/isv_partners/api_partner) beschrieben.

[Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points)<br>
- Braze hat ein Datenpunktmodell, bei dem Datenpunkte pro „Schreibvorgang“ im Nutzerprofil protokolliert werden, unabhängig davon, ob sich der Wert geändert hat.
- Datenpunkte fallen sowohl beim Kohortenimport als auch bei den User-Track-Endpunkten an.

## Streaming von Engagement-Analytics zum Partner {#engagement-analytics-streaming-to-partner}

### Currents

Currents ist ein nahezu in Realtime arbeitendes Streaming-Tool für Nachrichten-Engagement-Analytics in Braze. Es streamt Daten auf Nutzerebene zu allen Sendungen, Zustellungen, Öffnungen, Klicks usw. für Campaigns und Canvases, die aus dem Workspace der Kund:in gesendet werden. Einige Hinweise: Currents wird pro Konnektor für die Kund:in berechnet, daher müssen alle neuen Currents-Partner einen EA-Prozess durchlaufen. Wir verlangen von unseren Partnern, dass sie fünf Kund:innen im Rahmen des EA einbinden, bevor wir die angepasste UI erstellen und den Konnektor öffentlich zur Verfügung stellen.
- [Partner-Dokumentation]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)
- [Message-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) – alle Kund:innen, die einen Currents-Konnektor erwerben, haben Zugriff auf diese Events.
- [Nutzerverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) – nicht alle Kund:innen, die einen Currents-Konnektor erwerben, kaufen auch einen „Alle Events“-Konnektor, der diese Events enthält.

### Snowflake Data Share

Kund:innen, die einen Snowflake-Data-Share-Konnektor erwerben, haben automatisch Zugriff auf sowohl Message-Engagement- als auch Nutzerverhalten-Events. Wenn Snowflake Data Share als Partnerintegration verwendet wird, stellt Braze im Namen der Kund:in eine Freigabe für die Snowflake-Instanz des Partners bereit. Da die regionsübergreifende Datenfreigabe für unsere Kund:innen mit höheren Kosten verbunden ist, bitten wir Partner, die eine Integration mit Snowflake anstreben, zu beachten, dass sie ein Konto in `US-EAST-1` und/oder `EU-CENTRAL-1` benötigen.
- [Partner-Dokumentation]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)

## Erstellen und Triggern von Campaigns und Canvases {#building-and-triggering-campaigns-and-canvases}

### Erstellen von Assets in Braze {#creating-assets-in-braze}
Braze bietet eine Reihe von Endpunkten, die es Kund:innen und Partnern ermöglichen, E-Mail-Templates und Content Blocks innerhalb des Workspace einer Kund:in zu erstellen bzw. zu aktualisieren. Diese Templates und Content Blocks können wiederum in den Campaigns und Canvases der Kund:in verwendet werden.
- E-Mail-Templates
    - [Template-Endpunkt erstellen]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
    - [Template-Endpunkt aktualisieren]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks)
    - [Content-Block-Endpunkt erstellen]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
    - [Content-Block-Endpunkt aktualisieren]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)

### API-getriggerte Campaigns und Canvases {#api-triggered-campaigns-and-canvases}

Kund:innen können Campaigns und Canvases so einrichten, dass sie über die API getriggert werden. Die API-Anfragen zum Triggern dieser Campaigns können verwendet werden, um die Campaign weiter zu personalisieren und zu segmentieren, indem API-Trigger-Eigenschaften und Zielgruppen- oder Empfängerparameter übergeben werden.
- [Campaigns über API triggern]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)
    - Campaigns sind einzelne Nachrichten, wie z. B. individuelle E-Mails.
- [Canvases über API triggern]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#request-body)
    - Canvas ist eine einheitliche Oberfläche, auf der Marketer Campaigns mit mehreren Nachrichten und Schritten erstellen können, um eine zusammenhängende Journey zu gestalten. Wenn Sie ein Canvas triggern, nehmen Sie eine Nutzer:in in den Canvas-Flow auf, wo sie so lange Nachrichten erhält, bis sie die Canvas-Kriterien nicht mehr erfüllt.
- [API-Trigger-Eigenschaften/Canvas-Entry-Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    - Daten, die zum Zeitpunkt des Versands dynamisch in die Nachricht eingefügt werden können.

### API-Campaigns
Bei der Erstellung von API-Campaigns (im Unterschied zu den oben genannten API-getriggerten Campaigns) wird das Braze-Dashboard nur dazu verwendet, eine `campaign_id` zu generieren, mit der die Kund:in Analytics für die Campaign-Berichterstattung verfolgen kann. Die Nachricht der Campaign selbst wird in der API-Anfrage definiert.
- [API-Campaign sofort senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [API-Campaign planen]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)

### Sende-IDs {#send-ids}
Verwenden Sie den Braze-Endpunkt, um eine Sende-ID zu generieren, mit der Sie die Campaign-Analytics nach Sendungen aufschlüsseln können. Wenn beispielsweise eine `campaign_id` (API-Campaign) pro Standort erstellt wird, könnte eine Sende-ID pro Sendung generiert werden, um zu verfolgen, wie gut verschiedene Nachrichten für einen bestimmten Standort performen.
- [Sende-IDs]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)

## Connected-Content

Connected-Content kann innerhalb eines beliebigen Kanals verwendet werden, um zum Zeitpunkt des Versands eine API-Anfrage an den angegebenen Endpunkt zu stellen und das, was in der Antwort zurückgegeben wird, in die Nachricht einzufügen.

Die Vielseitigkeit von Connected-Content macht dies zu einem Feature, das von vielen unserer Kund:innen genutzt wird, um Inhalte einzufügen, die nicht in Braze vorhanden sind oder sein können. Einige der häufigsten Anwendungsfälle sind:
- Templating von Blog- oder Artikelinhalten in Nachrichten
- Inhaltsempfehlungen
- Produkt-Metadaten
- Lokalisierung und Übersetzung

Dinge, die Sie beachten sollten:
- Braze erhebt keine Gebühren für API-Aufrufe, und diese werden nicht auf Ihre Datenpunkt-Nutzung angerechnet.
- Es gibt ein Limit von 1 MB für Connected-Content-Antworten.
- Connected-Content-Aufrufe erfolgen, wenn die Nachricht gesendet wird, mit Ausnahme von In-App-Nachrichten, bei denen der Aufruf erfolgt, wenn die Nachricht angezeigt wird.
- Connected-Content-Aufrufe folgen keinen Weiterleitungen. Braze verlangt aus Performance-Gründen, dass die Antwortzeit des Servers weniger als 2 Sekunden beträgt; wenn der Server länger als 2 Sekunden braucht, um zu antworten, wird der Inhalt nicht eingefügt.
- Die Systeme von Braze können denselben Connected-Content-API-Aufruf mehr als einmal pro Empfänger:in tätigen. Das liegt daran, dass Braze möglicherweise einen Connected-Content-API-Aufruf tätigen muss, um eine Nachrichten-Payload zu rendern, und Nachrichten-Payloads können pro Empfänger:in mehrfach gerendert werden – für Validierung, Wiederholungslogik oder andere interne Zwecke.

Lesen Sie diese Artikel, um mehr über Connected-Content zu erfahren:
- [Einen Connected-Content-Aufruf tätigen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Connected-Content abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)
- [Connected-Content-Wiederholungsversuche]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)