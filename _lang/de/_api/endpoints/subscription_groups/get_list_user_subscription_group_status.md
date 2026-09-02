---
nav_title: "GET: Abo-Gruppenstatus der Nutzer:innen auflisten"
article_title: "GET: Abo-Gruppenstatus der Nutzer:innen auflisten"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Abo-Gruppenstatus der Nutzer:innen auflisten“."

---
{% api %}
# Abo-Gruppenstatus der Nutzer:innen auflisten {#list-users-subscription-group-status}
{% apimethod get %}
/subscription/status/get
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Abo-Status einer Nutzer:in in einer Abo-Gruppe abzurufen.

Diese Gruppen sind auf der Seite **Abo-Gruppe** verfügbar. Die Antwort dieses Endpunkts enthält die externe ID sowie den Status „Abonniert“, „Abgemeldet“ oder „Unbekannt“ für die im API-Aufruf angeforderte Abo-Gruppe. Dies kann verwendet werden, um den Abo-Gruppenstatus in nachfolgenden API-Aufrufen zu Update or aktualisieren or aktualisieren oder auf einer gehosteten Webseite anzuzeigen.

Wenn Sie E-Mails über ein angepasstes Formular erfassen und dann die Abo-Gruppenmitgliedschaft über die Representational State Transfer API festlegen, rufen Sie diesen Endpunkt zuerst auf, um zu prüfen, ob bereits ein Profil vorhanden ist. Wenn kein übereinstimmendes Profil existiert, erstellen oder abonnieren Sie die Nutzer:in mit dem Endpunkt [Abo-Gruppenstatus der Nutzer:innen Update or aktualisieren or aktualisieren]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Andernfalls Update or aktualisieren or aktualisieren Sie das vorhandene Profil, anstatt ein Duplikat zu erstellen. Weitere Erfassungsmuster finden Sie unter [Best Practices für die Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/best_practices).

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail-Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#488c8923-fa44-4124-9245-036d13c615f2 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **Kurzmitteilungsdienst or SMS-Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **WhatsApp-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4b8515b8-067f-41fd-b213-8bb2d18b1557 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `subscription.status.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types?tab=subscription%20group%20ids) | Erforderlich | String | Die `id` Ihrer Abo-Gruppe. |
| `external_id` | Erforderlich* | String | Die `external_id` der Nutzer:in (muss mindestens eine und höchstens 50 `external_ids` enthalten). <br><br>Wenn sowohl eine `external_id` als auch `email`/`phone` übermittelt werden, werden nur die angegebenen `external_id`(s) auf die Ergebnisabfrage angewendet. |
| `email` | Erforderlich* | String | Die E-Mail-Adresse der Nutzer:in. Kann als String-Array mit maximal 50 Einträgen übergeben werden.<br><br> Die gleichzeitige Übermittlung einer E-Mail-Adresse und einer Telefonnummer (ohne `external_id`) führt zu einem Fehler. |
| `phone` | Erforderlich* | String im [E.164](https://en.wikipedia.org/wiki/E.164)-Format | Die Telefonnummer der Nutzer:in. Wenn keine E-Mail angegeben wird, müssen Sie mindestens eine Telefonnummer angeben (maximal 50).<br><br> Die gleichzeitige Übermittlung einer E-Mail-Adresse und einer Telefonnummer (ohne `external_id`) führt zu einem Fehler. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter" }

*Für jede Nutzer:in ist entweder `external_id`, `email` oder `phone` erforderlich.

- Für Kurzmitteilungsdienst or SMS- und WhatsApp-Abo-Gruppen ist entweder `external_id` oder `phone` erforderlich. Wenn beide übermittelt werden, wird nur die `external_id` für die Abfrage verwendet und die Telefonnummer wird dieser Nutzer:in zugeordnet.
- Für E-Mail-Abo-Gruppen ist entweder `external_id` oder `email` erforderlich. Wenn beide übermittelt werden, wird nur die `external_id` für die Abfrage verwendet und die E-Mail-Adresse wird dieser Nutzer:in zugeordnet.

## Beispielanfrage {#example-request}

{% tabs %}
{% tab Mehrere Nutzer:innen %}
{% raw %}
```
https://rest.iad-03.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&external_id[]=1&external_id[]=2
```
{% endraw %}
{% endtab %}
{% tab Kurzmitteilungsdienst or SMS und WhatsApp %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11112223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% tab E-Mail %}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&email=example@example.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Antwort {#response}

Alle erfolgreichen Antworten geben je nach Status und Verlauf der Nutzer:innen mit der Abo-Gruppe `Subscribed`, `Unsubscribed` oder `Unknown` zurück.

```json
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```

{% alert important %}
Dieser Endpunkt gibt den Abo-Gruppenstatus unabhängig vom globalen Abo-Status der Nutzer:innen zurück. Wenn eine Nutzer:in global abgemeldet ist, wird sie im Braze-Dashboard als von jeder Abo-Gruppe abgemeldet angezeigt. Dieser Endpunkt gibt jedoch weiterhin den zuletzt gespeicherten Abo-Gruppenstatus zurück (z. B. `Subscribed`), da der globale Abo-Status einzelne Abo-Gruppen überlagert, ohne sie zu überschreiben.<br><br>Braze bewahrt die einzelnen Abo-Gruppenstatus auf, sodass bei einer erneuten globalen Anmeldung der Nutzer:in jede Abo-Gruppe auf ihren zuvor gespeicherten Status zurückgesetzt wird. Um den effektiven Abo-Status einer Nutzer:in zu ermitteln, prüfen Sie sowohl den globalen Abo-Status als auch den von diesem Endpunkt zurückgegebenen Abo-Gruppenstatus.
{% endalert %}

{% endapi %}