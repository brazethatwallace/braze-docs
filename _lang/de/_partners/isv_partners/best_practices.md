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

- `braze_id`: Ein von Braze zugewiesener Bezeichner, der unveränderlich ist und einem/einer bestimmten Nutzer:in bei der Erstellung in unserer Datenbank zugeordnet wird.
- `external_id`: Ein vom Kunden zugewiesener Bezeichner, in der Regel eine UUID. Wir empfehlen, die `external_id` zuzuweisen, wenn die/der Nutzer:in eindeutig identifiziert werden kann. Sobald ein:e Nutzer:in identifiziert wurde, kann der Status nicht mehr auf anonym zurückgesetzt werden.
- `user_alias`: Ein eindeutiger alternativer Bezeichner, den der Kunde zuweisen kann, um die/den Nutzer:in über eine ID zu referenzieren, bevor eine `external_id` zugewiesen wurde. Nutzer-Aliase können später über den Braze-Endpunkt [Nutzer:in identifizieren]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) mit anderen Aliasen oder einer `external_id` zusammengeführt werden, sobald eine verfügbar wird.
    - Innerhalb des Endpunkts [Nutzer:in identifizieren]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) kann das Feld `merge_behavior` verwendet werden, um festzulegen, welche Daten aus dem Nutzer-Alias-Profil im bekannten Nutzerprofil erhalten bleiben sollen.
    - Beachten Sie, dass der Nutzer-Alias nur dann ein versandfähiges Profil darstellt, wenn Sie zusätzlich eine E-Mail-Adresse und/oder Telefonnummer als Standardattribut im Profil hinterlegen.
- `device_id`: Ein automatisch generierter, gerätespezifischer Bezeichner. Einem Nutzerprofil können mehrere `device_ids` zugeordnet sein. Beispielsweise hätte ein:e Nutzer:in, die/der sich auf dem Arbeitscomputer, dem Heimcomputer, dem Tablet und in der iOS-App angemeldet hat, 4 `device_ids`, die mit dem Profil verknüpft sind.
- E-Mail-Adresse und Telefonnummer:
    - Werden als Bezeichner im Braze-Endpunkt „Nutzer:in tracken“ unterstützt.
    - Wenn die E-Mail-Adresse oder Telefonnummer als Bezeichner in einer Anfrage verwendet wird, gibt es drei mögliche Ergebnisse:
        1. Wenn ein:e Nutzer:in mit dieser E-Mail/Telefonnummer in Braze nicht existiert, wird ein reines E-Mail-/Telefon-Nutzerprofil erstellt, und alle Daten in der Anfrage werden dem Profil hinzugefügt.
        2. Wenn ein Profil mit dieser E-Mail/Telefonnummer bereits in Braze existiert, wird es aktualisiert und enthält alle in der Anfrage gesendeten Daten.
        3. In einem Anwendungsfall mit mehr als einem Profil mit dieser E-Mail/Telefonnummer wird das zuletzt aktualisierte Profil priorisiert.
    - Beachten Sie: Wenn ein reines E-Mail-/Telefon-Nutzerprofil existiert und anschließend ein identifiziertes Profil mit derselben E-Mail/Telefonnummer erstellt wird (z. B. ein weiteres Profil mit derselben E-Mail-Adresse UND einer externen ID), erstellt Braze ein zweites Profil. Nachfolgende Aktualisierungen werden an das Profil mit der externen ID gesendet.
        - Die beiden Profile können über den Braze-Endpunkt [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) zusammengeführt werden.

## Anonyme Nutzer:innen verwalten {#handling-anonymous-users}

Für einen Anwendungsfall, in dem Sie ein Nutzerprofil in Braze erstellen oder aktualisieren müssen, ohne Zugriff auf eine `external_id` zu haben, kann ein anderer Bezeichner wie eine E-Mail-Adresse oder Telefonnummer an den Braze-Endpunkt [Nutzer:in nach Bezeichner exportieren]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) übergeben werden, um festzustellen, ob ein Profil für die/den Nutzer:in in Braze existiert.

```json
{
 "email_address": "test@example.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Wenn eine:r Nutzer:in mit dieser E-Mail oder Telefonnummer in Braze existiert, wird das Profil zurückgegeben. Andernfalls wird ein leeres „users“-Array zurückgegeben. Der Vorteil der Nutzung des Export-Endpunkts, um festzustellen, ob bereits eine:r Nutzer:in mit dieser E-Mail-Adresse existiert, besteht darin, dass Sie ermitteln können, ob anonyme Nutzerprofile mit der/dem Nutzer:in verknüpft sind. Zum Beispiel ein anonymes Profil, das über das SDK erstellt wurde (das eine `braze_id` hat), oder ein zuvor erstelltes Nutzer-Alias-Profil.

Wenn die Anfrage kein Nutzerprofil zurückgibt, können Sie entweder einen Nutzer-Alias erstellen oder eine:n reine:n E-Mail-Nutzer:in anlegen:

### Nutzer-Alias {#user-alias}

Verwenden Sie den User-Track-Endpunkt, um einen Nutzer-Alias zu erstellen, wobei Sie den gewählten Bezeichner als Alias-Namen verwenden. Indem Sie `_update_existing_only` als `false` im Attribut-, Ereignis- oder Kauf-Objekt angeben, in dem der neue Nutzer-Alias definiert ist, können Sie das Alias-Profil erstellen und gleichzeitig Attribute, Ereignisse und Käufe zu diesem Profil hinzufügen.

Damit das Nutzer-Alias-Profil versandfähig ist, müssen Sie die E-Mail-Adresse im Feld `email` angeben, wie im folgenden Beispiel gezeigt.

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

Sie können diesen Nutzer-Alias später mit einer `external_id` identifizieren und zusammenführen, wenn eine verfügbar wird, über unseren Endpunkt [Nutzer:innen identifizieren]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

### Reine:n E-Mail-Nutzer:in erstellen {#creating-an-email-only-user}

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
Diese Funktion befindet sich im Early Access.
{% endalert %}

## Daten mit Nutzerprofilen synchronisieren {#syncing-data-to-user-profiles}

[User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- Dies ist ein öffentlich zugänglicher Endpunkt, der Nutzer:innen in Braze erstellen und aktualisieren kann, z. B. durch das Protokollieren von Attributen im Nutzerprofil. Dieser Endpunkt hat ein Rate-Limit von 50.000 Anfragen pro Minute, das auf Workspace-Ebene angewendet wird.
- Wenn Sie diesen Endpunkt verwenden, fügen Sie den `partner`-Schlüssel ein, wie in unserer Partner-Dokumentation beschrieben.

[Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview#what-is-cloud-data-ingestion)
- Ähnlich wie beim User-Track-Endpunkt können Daten über die Cloud-Datenaufnahme mit Nutzerprofilen synchronisiert werden. Bei der Verwendung dieses Tools werden Attribute, Ereignisse und Käufe in Profilen protokolliert, indem Sie die Data-Warehouse-Tabelle oder -Ansicht einrichten und verbinden, die Sie mit dem gewünschten Braze-Workspace synchronisieren möchten.

[Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points)
- Braze verwendet ein Datenpunkt-Modell, bei dem Datenpunkte pro „Schreibvorgang“ im Nutzerprofil protokolliert werden – unabhängig davon, ob sich der Wert geändert hat. Aus diesem Grund empfehlen wir, nur die Attribute an Braze zu senden, die sich geändert haben.

## Zielgruppen von Nutzer:innen an Braze senden {#sending-audiences-of-users-to-braze}

[Dokumentation zu Kohortenimport-Sync-Partnern]({{site.baseurl}}/partners/isv_partners/cohort_import)<br>
- Zielgruppen von Nutzer:innen können mithilfe der Braze-Kohortenimport-API-Endpunkte als Kohorte mit Braze synchronisiert werden. Anstatt diese Zielgruppen als Nutzerattribute im Nutzerprofil zu speichern, können Kund:innen diese Kohorte über einen Partner-gebrandeten Filter innerhalb unseres Segmentierungs-Tools erstellen und ansprechen. So können Sie ein bestimmtes Segment von Nutzer:innen effizienter finden und ansprechen.
- Kohortenimport-Endpunkte sind nicht öffentlich und spezifisch für jeden Partner. Aus diesem Grund werden Synchronisierungen mit den Kohortenendpunkten nicht auf die Workspace-Rate-Limits eines Kunden/einer Kundin angerechnet.

[User Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)<br>
- Dies ist ein öffentlich zugänglicher Endpunkt, der sofort verwendet werden kann, um Nutzer:innen in Braze zu erstellen, indem eine:r Nutzer:in über ein Nutzerattribut einer bestimmten Zielgruppe zugeordnet wird. Der Hauptunterschied zwischen diesem Endpunkt und dem Kohortenimport-Endpunkt besteht darin, dass Zielgruppen, die über diesen Endpunkt gesendet werden, im Nutzerprofil gespeichert werden, während der Kohortenimport-Endpunkt als Filter in unserem Segmentierungs-Tool angezeigt wird. Dieser Endpunkt hat ein Rate-Limit von 50.000 Anfragen pro Minute, das auf Workspace-Ebene angewendet wird.
- Stellen Sie bei der Verwendung dieses Endpunkts sicher, dass Sie den `partner`-Schlüssel wie in unserer [Partner-Dokumentation]({{site.baseurl}}/partners/isv_partners/api_partner) gezeigt einfügen.

[Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points)<br>
- Braze verwendet ein Datenpunkt-Modell, bei dem Datenpunkte pro „Schreibvorgang“ im Nutzerprofil protokolliert werden – unabhängig davon, ob sich der Wert geändert hat.
- Datenpunkte fallen sowohl bei Kohortenimporten als auch bei User-Track-Endpunkten an.

## Streaming von Engagement-Analytics an Partner {#engagement-analytics-streaming-to-partner}

### Currents

Currents ist ein nahezu in Echtzeit arbeitendes Tool zum Streaming von Engagement-Analytics für Nachrichten in Braze. Es streamt Daten auf Nutzer:innenebene zu allen Sendungen, Zustellungen, Öffnungen, Klicks usw. für Campaigns und Canvases, die aus dem Workspace der Kund:innen gesendet werden. Ein paar Hinweise: Currents wird pro Konnektor für Kund:innen bepreist, daher müssen alle neuen Currents-Partner einen EA-Prozess durchlaufen. Wir bitten unsere Partner, fünf Kund:innen im Rahmen des EA einzubinden, bevor wir die individuell gebrandete UI erstellen und den Konnektor öffentlich verfügbar machen.
- [Partnerdokumentation]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)
- [Engagement-Ereignisse für Nachrichten]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) – alle Kund:innen, die einen Currents-Konnektor erwerben, haben Zugriff auf diese Ereignisse.
- [Nutzerverhaltens-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) – nicht alle Kund:innen, die einen Currents-Konnektor erwerben, kaufen auch einen „All Events“-Konnektor, der diese Ereignisse einschließt.

### Snowflake Data Share

Kund:innen, die einen Snowflake-Data-Share-Konnektor erwerben, erhalten automatisch Zugriff auf sowohl Engagement-Ereignisse für Nachrichten als auch Nutzerverhaltens-Ereignisse. Wenn Snowflake Data Share als Partnerintegration genutzt wird, stellt Braze im Auftrag der Kund:innen einen Share für die Snowflake-Instanz des Partners bereit. Ein Hinweis: Regionsübergreifendes Data Sharing ist für unsere Kund:innen mit höheren Kosten verbunden. Wir bitten daher Partner, die eine Integration mit Snowflake anstreben, zu beachten, dass sie ein Konto in `US-EAST-1` und/oder `EU-CENTRAL-1` benötigen.
- [Partnerdokumentation]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/custom_http_connector)

## Campaigns und Canvases erstellen und auslösen {#building-and-triggering-campaigns-and-canvases}

### Assets in Braze erstellen {#creating-assets-in-braze}
Braze bietet eine Reihe von Endpunkten, die es Kund:innen und Partnern ermöglichen, E-Mail-Templates und Content Blocks innerhalb eines Kund:innen-Workspace zu erstellen bzw. zu aktualisieren. Diese Templates und Content Blocks können wiederum in den Braze Campaigns und Canvases der Kund:innen verwendet werden.
- E-Mail-Templates
    - [Endpunkt „Template erstellen“]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template)
    - [Endpunkt „Template aktualisieren“]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template#rate-limit)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
    - [Endpunkt „Content Block erstellen“]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block)
    - [Endpunkt „Content Block aktualisieren“]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)

### API-getriggerte Campaigns und Canvases {#api-triggered-campaigns-and-canvases}

Kund:innen können Campaigns und Canvases so einrichten, dass sie per API getriggert werden. Die API-Anfragen zum Auslösen dieser Campaigns können verwendet werden, um die Campaign durch die Übergabe von API-Trigger-Eigenschaften sowie Zielgruppen- oder Empfänger:innen-Parametern weiter zu personalisieren und zu segmentieren.
- [Campaigns per API triggern]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)
    - Campaigns sind einzelne Nachrichten, z. B. eine einzelne E-Mail.
- [Canvases per API triggern]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases#request-body)
    - Canvas ist eine einheitliche Oberfläche, auf der Marketer Campaigns mit mehreren Nachrichten und Schritten erstellen können, um eine zusammenhängende Journey zu gestalten. Wenn Sie ein Canvas triggern, wird ein:e Nutzer:in in den Canvas-Flow aufgenommen, wo sie weiterhin Nachrichten erhalten, bis sie die Canvas-Kriterien nicht mehr erfüllen.
- [API-Trigger-Eigenschaften/Canvas-Entry-Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object)
    - Daten, die zum Zeitpunkt des Versands dynamisch in die Nachricht eingefügt werden können.

### API-Campaigns
Beim Erstellen von API-Campaigns (nicht zu verwechseln mit den in diesem Abschnitt beschriebenen API-getriggerten Campaigns) wird das Braze-Dashboard lediglich verwendet, um eine `campaign_id` zu generieren, mit der Kund:innen Analytics für das Campaign-Reporting verfolgen können. Die Campaign-Nachricht selbst wird innerhalb der API-Anfrage definiert.
- [API-Campaign sofort senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)
- [API-Campaign planen]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages)

### Sende-IDs {#send-ids}
Verwenden Sie den Braze-Endpunkt, um eine Sende-ID zu generieren, die dazu verwendet werden kann, Campaign-Analytics nach Versand aufzuschlüsseln. Wenn beispielsweise eine `campaign_id` (API-Campaign) pro Standort erstellt wird, kann eine Sende-ID pro Versand generiert werden, um nachzuverfolgen, wie gut unterschiedliche Nachrichten für einen bestimmten Standort performen.
- [Sende-IDs]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids)

## Connected Content

Connected Content kann in jedem Kanaltyp verwendet werden, um zum Zeitpunkt des Versands eine API-Anfrage an den angegebenen Endpunkt zu stellen und die zurückgegebene Antwort in die Nachricht einzufügen.

Die Vielseitigkeit von Connected Content macht dieses Feature zu einem, das von vielen unserer Kund:innen genutzt wird, um Inhalte einzufügen, die nicht in Braze gespeichert sind oder gespeichert werden können. Einige der häufigsten Anwendungsfälle, die wir sehen, sind:
- Einbinden von Blog- oder Artikelinhalten in Nachrichten
- Inhaltsempfehlungen
- Produkt-Metadaten
- Lokalisierung und Übersetzung

Wichtige Hinweise:
- Braze berechnet keine Gebühren für API-Aufrufe und diese werden nicht auf Ihre Datenpunkt-Nutzung angerechnet.
- Es gibt ein Limit von 1 MB für Connected-Content-Antworten.
- Connected-Content-Aufrufe erfolgen beim Versand der Nachricht, mit Ausnahme von In-App-Nachrichten, bei denen der Aufruf erfolgt, wenn die Nachricht angezeigt wird.
- Connected-Content-Aufrufe folgen keinen Weiterleitungen. Braze erfordert aus Performance-Gründen, dass die Server-Antwortzeit weniger als 2 Sekunden beträgt; wenn der Server länger als 2 Sekunden für die Antwort benötigt, wird der Inhalt nicht eingefügt.
- Braze-Systeme können denselben Connected-Content-API-Aufruf pro Empfänger:in mehrmals ausführen. Der Grund dafür ist, dass Braze möglicherweise einen Connected-Content-API-Aufruf durchführen muss, um einen Nachrichten-Payload zu rendern, und Nachrichten-Payloads können pro Empfänger:in mehrmals gerendert werden – für Validierung, Wiederholungslogik oder andere interne Zwecke.

Weitere Informationen zu Connected Content finden Sie in diesen Artikeln:
- [Einen Connected-Content-Aufruf durchführen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [Connected Content abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)
- [Connected-Content-Wiederholungen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)