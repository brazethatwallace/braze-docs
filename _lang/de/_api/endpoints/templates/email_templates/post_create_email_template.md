---
nav_title: "POST: E-Mail-Template erstellen"
article_title: "POST: E-Mail-Templates erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „E-Mail-Templates erstellen“."
---
{% api %}
# E-Mail-Template erstellen {#create-email-template}
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um E-Mail-Templates im Braze-Dashboard zu erstellen.

Diese Templates werden auf der Seite **Templates und Medien** verfügbar sein. Die Antwort dieses Endpunkts enthält ein Feld für `email_template_id`, das zum Update des Templates in nachfolgenden API-Aufrufen verwendet werden kann.

{% alert tip %}
Sie können diesen Endpunkt auch über den [Braze MCP-Server]({{site.baseurl}}/user_guide/brazeai/mcp_server) mit der Funktion [`create_email_template`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#templates) aufrufen. So können KI-Tools wie Claude und Cursor E-Mail-Templates über natürlichsprachliche Eingaben erstellen.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Voraussetzungen {#prerequisites}
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key) mit der Berechtigung `templates.email.create`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "template_name": (required, string) The name of your email template,
   "subject": (required, string) The email template subject line,
   "body": (required, string) The email template body that may include HTML,
   "plaintext_body": (optional, string) A plaintext version of the email template body,
   "preheader": (optional, string) The email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature is used on this template.
 }
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `template_name` | Erforderlich | String | Name Ihres E-Mail-Templates. |
| `subject` | Erforderlich | String | Betreffzeile des E-Mail-Templates. |
| `body` | Erforderlich | String | Body des E-Mail-Templates, der HTML enthalten kann. Bis zu 400&nbsp;KB. |
| `plaintext_body` | Optional | String | Eine Klartextversion des E-Mail-Template-Bodys. |
| `preheader` | Optional | String | E-Mail-Preheader, der in einigen Clients zur Erstellung von Vorschauen verwendet wird. |
| `tags` | Optional | String | [Tags]({{site.baseurl}}/user_guide/messaging/governance/tags) müssen bereits existieren. |
| `should_inline_css` | Optional | Boolescher Wert | Aktiviert oder deaktiviert das Feature `inline_css` pro Template. Wenn nicht angegeben, verwendet Braze die Standardeinstellung für die App-Gruppe. Erwartet wird `true` oder `false`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## Beispielantwort {#example-response}

```json
{
  "email_template_id": "232b6d29-7e41-4106-a0ab-1c4fe915d701",
  "message": "success"
}
```

## Fehlerbehebung {#troubleshooting}

Die folgende Tabelle listet mögliche zurückgegebene Fehler und die zugehörigen Schritte zur Fehlerbehebung auf, falls zutreffend.

| Fehler | Fehlerbehebung |
| --- | --- |
| Template-Name ist erforderlich | Geben Sie einen Template-Namen ein. |
| Tags müssen ein Array sein | Tags müssen als String-Array formatiert werden, zum Beispiel `["marketing", "promotional", "transactional"]`. |
| Alle Tags müssen Strings sein | Stellen Sie sicher, dass Ihre Tags in Anführungszeichen (`""`) eingeschlossen sind. |
| Einige Tags konnten nicht gefunden werden | Um beim Erstellen eines E-Mail-Templates einen Tag hinzuzufügen, muss dieser bereits in Braze vorhanden sein. |
| E-Mail muss gültige Content-Block-Namen haben | Die E-Mail könnte Content Blocks enthalten, die in dieser Umgebung nicht vorhanden sind. |
| Ungültiger Wert für `should_inline_css`. `true` oder `false` wurde erwartet | Dieser Parameter akzeptiert nur boolesche Werte (true oder false). Stellen Sie sicher, dass der Wert für `should_inline_css` nicht in Anführungszeichen (`""`) eingeschlossen ist, da der Wert sonst als String gesendet wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }

{% endapi %}