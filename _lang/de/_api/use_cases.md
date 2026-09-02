---
nav_title: API-Anwendungsfälle
article_title: API-Anwendungsfälle
description: "Ganz gleich, ob Sie erfahrene Entwickler:innen oder Marketer mit minimalen Entwicklerressourcen sind – dieser Referenzartikel soll Ihnen zeigen, wie Sie die leistungsstarke Representational State Transfer API von Braze nutzen können, um verschiedene Aufgaben zu erfüllen und Ihre Customer-Engagement-Strategie zu verbessern."
page_type: reference
page_order: 4.8
---

# API-Anwendungsfälle {#api-use-cases}

> Die [Representational State Transfer API von Braze]({{site.baseurl}}/api/basics) bietet eine breite Palette von Endpunkten, die Sie bei der Verwaltung und Optimierung Ihrer Customer-Engagement-Strategie unterstützen. In diesem Artikel werden wir verschiedene Anwendungsfälle für jede Endpunkt-Sammlung untersuchen: Kataloge, E-Mail-Listen und -Adressen, Export, Nachrichten, Präferenzzentrum, Kurzmitteilungsdienst or SMS, Abo-Gruppen, Templates und Nutzerdaten.<br><br>In jedem Abschnitt wird ein Szenario mit einer Schritt-für-Schritt-Anleitung, einem Code-Beispiel und dem erwarteten Ergebnis vorgestellt. Am Ende dieses Artikels werden Sie besser verstehen, wie Sie die Representational State Transfer API von Braze nutzen können, um Ihr Customer-Engagement zu verbessern.

## Mehrere Artikel aus einem Katalog löschen {#deleting-multiple-items-in-a-catalog}

Ein neues Jahr bringt neue Produkteinführungen bei Kitchenerie, einer Einzelhandelsmarke, die sich auf Küchenartikel spezialisiert hat. Im Braze-Dashboard hat Kitchenerie einen Katalog für seine Geschirrkollektion mit dem Namen „Dishware“ eingerichtet. Das neue Jahr bedeutet auch, die folgenden Produkte aus der Geschirrkollektion zu entfernen.

* Plain Bisque
* Pearl Porcelain
* Pink Shimmer

Um diese Produkte aus seinem Katalog zu entfernen, kann Kitchener den [Endpunkt `/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) verwenden, um die Artikel-IDs zu übergeben.

Hier ist die Beispielanfrage:

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/dishware/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "plainbisque"},
    {"id": "pearlporcelain"},
    {"id": "pinkshimmer"}
  ]
}'
```

Nach dem Senden dieser Nutzlast bestätigt die Antwort, dass Braze die drei Kollektionen erfolgreich aus dem Geschirrkatalog von Kitchenerie entfernt hat.

```json
{
  "message": "success"
}
```

## Entfernen von E-Mails aus der Braze-Spam-Liste {#removing-emails-from-the-braze-spam-list}

Bei MovieCanon, einem Streaming-Dienstleister, ist das Entwickler:innen-Team dafür verantwortlich, die E-Mail-Listen regelmäßig zu überprüfen, um Nutzer:innen zu identifizieren und zu behalten, die E-Mail-Campaigns abonniert haben. Im Rahmen dieser Prüfung möchte MovieCanon die folgende Liste von E-Mails aus seiner Spam-Liste entfernen:

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

Um diese Aufgabe zu erfüllen, benötigt das Entwickler:innen-Team einen API-Schlüssel mit der Berechtigung `email.spam.remove`, um den Endpunkt `/email/spam/remove` zu verwenden. Dieser Endpunkt entfernt E-Mail-Adressen aus der Spam-Liste von Braze und der Spam-Liste, die vom E-Mail-Anbieter von MovieCanon geführt wird.

Um diese Anfrage zu senden, geben Sie entweder eine String-E-Mail-Adresse oder ein Array mit bis zu 50 zu ändernden E-Mail-Adressen an. Da die Liste der zu entfernenden E-Mails unter 50 liegt, kann MovieCanon diese Aufgabe mit dem folgenden Anfragetext erledigen:

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

Nach dem erfolgreichen Versand dieser Nutzlast bestätigt die Antwort, dass Braze die E-Mails aus der Spam-Liste von MovieCanon entfernt hat.

```json
{
  "message": "success"
}
```

## Prüfen aller Canvase {#auditing-all-canvases}

Siege Valley Health ist ein Krankenhaussystem, das 10 Krankenhäuser und Forschungszentren mit Tausenden von Patient:innen umfasst. Das Marketingteam möchte die Canvase vergleichen, die in den letzten 3 Jahren der Braze-Nutzung an Patient:innen gesendet wurden, um sie an die Terminvereinbarung für Grippeimpfungen zu erinnern. Das Marketingteam von Siege Valley Health wünscht sich außerdem eine schnelle und effiziente Möglichkeit, sowohl die Liste der Canvase als auch die Analytics-Zusammenfassung einzusehen.

Sehen wir uns an, wie Siege Valley Health diese beiden Aufgaben mit einer Kombination von Endpunkten erfüllen kann, anstatt über das Braze-Dashboard zu filtern.

Für die erste Aufgabe der Prüfung von Canvase verwenden Sie den [Endpunkt `/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases), um eine Liste der Canvase zu exportieren, die den Namen und die Tags enthält. Hier ist eine Beispielanfrage:

{% details Hier ist die Antwort, die das Marketingteam von Siege Valley Health erhalten würde. %}
```json
{
  "canvases" : [
  	{
  		"id": "canvas_identifier_1",
  		"last_edited": "2020-07-10T23:59:59",
  		"name": "PatientReminder_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "2020"
      }
  	},
  	{
  		"id": "canvas_identifier_2",
  		"last_edited": "2020-07-30T23:59:59",
  		"name": "PatientReminder2_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "reminder", "2020"
      }
  	},
    ... (more Canvases)
  ],
  "message": 'success'
}
```
{% enddetails %}

Fahren wir mit der nächsten Aufgabe fort: der Anzeige der Analytics-Zusammenfassung für den ersten Canvas aus der Liste der Canvase von Siege Valley Health. Dazu verwenden wir den [Endpunkt `/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary) mit den folgenden Anfrageparametern:

* `canvas_id`: "canvas_identifier_2"
* `ending_at`: 2023-07-10T23:59:59
* `starting_at`: 2020-07-10T23:59:59

Hier ist eine Beispielanfrage:

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_identifier_2}}&ending_at=2023-07-10T23:59:59&starting_at=2020-07-10T23:59:59&length=5&include_variant_breakdown=false&include_step_breakdown=false&include_deleted_step_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Prüfen der anstehenden geplanten Campaigns und Canvase {#checking-upcoming-scheduled-campaigns-and-canvases}

Die geschäftigste Zeit des Jahres rückt für Flash & Thread, eine Einzelhandelsmarke, die Kleidung und Beauty-Produkte online und in Shops verkauft, schnell näher. Das Marketingteam möchte die anstehenden Campaigns und Canvase im Braze-Dashboard vor dem 31. März 2024 um 12 Uhr überprüfen. Dies kann über den [Endpunkt `/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled) erfolgen.

Hier ist die Beispielanfrage:

```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2024-03-31T12:00:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

Dieser Endpunkt gibt die Liste der bevorstehenden Campaigns und Canvase zurück. Von hier aus kann das Marketingteam seine Nachrichtenliste bestätigen, indem es sich auf das Feld `name` für die Campaigns und Canvase in der Antwort bezieht.

## Anzeigen eines älteren Präferenzzentrums {#viewing-an-older-preference-center}

PoliterWeekly ist eine digitale Zeitschrift, deren Abonnent:innen per E-Mail erreichbar sind. Um die User Journey seiner Abonnent:innen besser zu verstehen, möchte das Marketingteam die Details des Präferenzzentrums von PoliterWeekly überprüfen, um festzustellen, wann es erstellt und zuletzt aktualisiert wurde.

Bei Verwendung des [Endpunkts `/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) muss das Marketingteam lediglich die externe ID des Präferenzzentrums als Pfadparameter einfügen, was wie folgt aussehen würde:

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/politer_weekly_preference_center_api_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

{% details Hier ist die Antwort, die das Marketingteam von PoliterWeekly erhalten würde. %}

```json
{
  "name": "PoliterWeekly Notification Preferences",
  "preference_center_api_id": "user_engage_pref_123",
  "created_at": "2021-04-03T12:00:00",
  "updated_at": "2024-08-15T15:00:00",
  "preference_center_title": "Manage Your PoliterWeekly Notification Preferences",
  "preference_center_page_html": "<!DOCTYPE html><html><head><title>Your PoliterWeekly Newsletter Preferences</title><style>body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }.container { max-width: 600px; margin: auto; }h1 { color: #333; }.preference { margin-bottom: 20px; }.preference label { font-size: 16px; }.preference input[type=\"checkbox\"] { margin-right: 10px; }.submit-btn { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }</style></head><body><div class=\"container\"><h1>Manage your notification preferences</h1><p>Select the types of updates you wish to receive from us:</p><form id=\"preferencesForm\"><div class=\"preference\"><label><input type=\"checkbox\" name=\"newsUpdates\" checked> News Updates</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"editorialPicks\"> Editorial Picks</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"events\"> Events & Webinars</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"specialOffers\"> Special Offers & Promotions</label></div><button type=\"submit\" class=\"submit-btn\">Save Preferences</button></form></div><script>document.getElementById('preferencesForm').addEventListener('submit', function(e) {e.preventDefault();alert('Your preferences have been saved!');});</script></body></html>",
  "confirmation_page_html": "<!DOCTYPE html><html><head><title>PoliterWeekly Preferences Updated</title></head><body><h1>You're good to go!</h1><p>Braze updated your preferences successfully.</p></body></html>",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=1"
  },
  "state": "active"
}
```

Anhand dieser Antwort kann das Marketingteam erkennen, dass das Präferenzzentrum 3 Jahre vor dem letzten Update or aktualisieren erstellt wurde. Mit diesen Informationen im Hinterkopf könnte das Marketingteam ein neues Präferenzzentrum erstellen und starten.

{% enddetails %}

## Entfernen von ungültigen Telefonnummern {#removing-invalid-phone-numbers}

Das Hauptziel von CashBlastr ist es, die Art und Weise zu optimieren, wie Menschen schnelle Zahlungen senden und empfangen können. Als Finanzdienstleister möchte CashBlastr die Liste der Telefonnummern seiner Kund:innen aktuell und korrekt halten. Das Entwickler:innen-Team wurde beauftragt, die folgende Liste der als „ungültig“ markierten Telefonnummern zu entfernen, damit die Kurzmitteilungsdienst or SMS-Nachrichten des Marketingteams die entsprechenden CashBlastr-Kund:innen erreichen können.

- 12223135467
- 12183095514
- 14235662245
- 14324567892

Um eine Anfrage mit dem [Endpunkt `/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers) zu senden, müssen die Telefonnummern in einem String-Array im [E.164-Format](https://en.wikipedia.org/wiki/E.164) vorliegen, mit bis zu 50 Telefonnummern pro Anfrage. Da die Liste nicht mehr als 50 Telefonnummern umfasst, hier ein Beispiel für den Anfragetext, den das Entwickler:innen-Team von CashBlastr senden würde:

```http
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

Nach dem Senden dieser Nutzlast bestätigt die Antwort, dass Braze die ungültigen Telefonnummern von CashBlastr aus der Braze-Liste ungültiger Nummern entfernt hat.

```json
{
  "message": "success"
}
```

## Anzeigen des Abo-Gruppenstatus einer Nutzerin oder eines Nutzers {#viewing-a-users-subscription-group-status}

SandwichEmperor ist eine Schnellrestaurantkette in den Vereinigten Staaten, deren Marketingteam die Abo-Gruppenstatus für eine zufällige Liste seiner Nutzer:innen per Kurzmitteilungsdienst or SMS überprüfen möchte. Mit dem [Endpunkt `/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) kann SandwichEmperor diese Aufgabe für eine einzelne Nutzerin oder einen einzelnen Nutzer mit der folgenden Beispielanfrage erfüllen:

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11232223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

Dieser Endpunkt listet auch die Abo-Gruppenstatus einer Nutzerin oder eines Nutzers für E-Mails auf. Verwenden Sie ihn, um den Abo-Gruppenstatus für mehrere Nutzer:innen anzuzeigen.

## Prüfen eines HTML-Templates für E-Mail-Messaging {#checking-an-html-template-for-email-messaging}

Bei WorkFriends, einem sozialen Netzwerk, das den Aufbau von Verbindungen zwischen Arbeitnehmer:innen aus verschiedenen Branchen unterstützt, ist das Marketingteam für den Versand von E-Mail-Campaigns an seine Nutzer:innen verantwortlich. Diese Campaigns beinhalten häufig Erinnerungen an lokale Ereignisse, wöchentliche Newsletter und die Hervorhebung von Profilaktivitäten.

In diesem Szenario hat WorkFriends in der Vergangenheit ein einzelnes HTML-Template mit seinem alten Branding verwendet. Um seine Markenidentität anzugleichen, möchte WorkFriends überprüfen, ob dieses HTML-Template hilfreiche Informationen enthält, die vor dem Umstieg auf ein neues Template genutzt werden können.

{% details Hier ist die Antwort, die das WorkFriends-Team erhalten würde. %}

```json
{
  "email_template_id": "WorkFriends_Email_Template_ID",
  "template_name": "Promo template",
  "description": "Promo template",
  "subject": "WorkFriends Weekly Newsletter",
  "preheader": "Another week, another WorkFriends update",
  "body": "<!DOCTYPE html><html><head><title>WorkFriends Weekly Newsletter</title><style>body {font-family: Arial, sans-serif; color: #333;}.container {padding: 20px;}.header {background-color: #f2f2f2; padding: 10px; text-align: center;}.content {margin-top: 20px;}.footer {margin-top: 20px; font-size: 12px; text-align: center; color: #777;}</style></head><body><div class=\"container\"><div class=\"header\"><h2>WorkFriends Weekly Newsletter</h2></div><div class=\"content\"><p>Hello WorkFriends,</p><p>Welcome to another edition of our weekly newsletter. We've got some exciting updates and promos for you this week!</p><!-- Add more content here --><p>Don't forget to check out our latest promos and updates. Stay connected, stay informed!</p></div><div class=\"footer\"><p>Thank you for being a part of WorkFriends.</p><p>Unsubscribe | Update Preferences</p></div></div></body></html>",
  "tags": "promo",
  "created_at": "2020-07-10 13:00:00.000",
  "updated_at": "2024-02-04 17:00:00.000"
}
```

{% enddetails %}

Nach Überprüfung dieser Template-Informationen kann WorkFriends auch den [Endpunkt `/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) verwenden, um das E-Mail-Template über die API zu Update or aktualisieren or aktualisieren. Das E-Mail-Template im Braze-Dashboard spiegelt diese Änderungen wider.