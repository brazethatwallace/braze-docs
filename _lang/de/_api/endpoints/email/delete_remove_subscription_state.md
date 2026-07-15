---
nav_title: "DELETE: Abo-Status nach E-Mail-Adresse oder Telefonnummer löschen"
article_title: "DELETE: Abo-Status nach E-Mail-Adresse oder Telefonnummer löschen"
search_tag: Endpoint
page_order: 0
hidden: true
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Abo-Status nach E-Mail-Adresse oder Telefonnummer löschen“."

---

{% api %}
# Abo-Status nach E-Mail-Adresse oder Telefonnummer löschen {#delete-subscription-state-by-email-address-or-phone-number}
{% apimethod delete %}
/users/subscription
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Wert des Abo-Status basierend auf einer E-Mail-Adresse oder Telefonnummer zu löschen.

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `email` | Ja | String | Die E-Mail-Adresse des/der Nutzer:in (muss mindestens eine Adresse und höchstens 50 Adressen enthalten). |
| `phone` | Ja | String | Die Telefonnummer des/der Nutzer:in (muss mindestens eine Telefonnummer und höchstens 50 Telefonnummern enthalten). Wir empfehlen, diese im E.164-Format bereitzustellen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

```http
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  {phone: "+12125551212"},
  {email: "dont.spam@example.com"},
  {phone: "+17185551212"}
}
```

## Antwort {#response}

```json
{
  "status": "The emails and/or phone numbers have been queued for deletion",
  "message": "success"
}
```

{% endapi %}