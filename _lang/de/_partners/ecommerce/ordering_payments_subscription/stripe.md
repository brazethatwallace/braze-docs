---
nav_title: Stripe
article_title: Stripe
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Stripe."
alias: /partners/stripe/
page_type: partner
search_tag: Partner
---

# Stripe

> [Stripe](https://www.stripe.com/) ist eine umfassende Plattform für die finanzielle Infrastruktur, die es Unternehmen ermöglicht, über eine Suite von integrierten APIs und Diensten Zahlungen zu akzeptieren, Einnahmen zu verwalten und den globalen Handel zu erleichtern.

Durch die Integration von Braze und Stripe können Sie:

- Nutzerprofile in Braze mit Realtime-Zahlungs- und Abrechnungsdaten von Stripe aktualisieren.
- Messaging in Braze auf der Grundlage von Stripe-Events triggern, wie z. B. Beginn einer Testphase, Aktivierung eines Abos, Kündigung eines Abos und mehr.
- Braze-Messaging auf der Grundlage des Zahlungsverlaufs oder des Rechnungsstatus einer Nutzerin bzw. eines Nutzers personalisieren, die über Stripe-Webhooks empfangen werden.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Stripe-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Stripe-Konto mit Zugang zu Webhooks. |
| Braze-Datentransformation | Um Daten von Stripe zu empfangen, ist eine [URL für die Datentransformation]({{site.baseurl}}/data_transformation) erforderlich. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Richten Sie die Braze-Datentransformation ein, um Webhooks von Stripe zu akzeptieren {#step-1}

{% multi_lang_include data_activation/create_transformation.md %}

### 2. Schritt: Webhooks für Stripe einrichten {#step-2-set-up-stripe-webhooks}

Folgen Sie den Schritten in der [Dokumentation zu den Webhooks von Stripe](https://docs.stripe.com/development/dashboard/webhooks), um einen Webhook einzurichten.

Fügen Sie Ihre Datentransformation-Webhook-URL als **Ziel-URL** hinzu und wählen Sie die Event-Typen aus, die Sie an Braze senden möchten. In der [Dokumentation von Stripe](https://docs.stripe.com/api/events/types) finden Sie eine vollständige Liste der Event-Typen.

![Ein Beispiel für die Webhook-Konfiguration von Stripe.]({% image_buster /assets/img/stripe/stripe_webhook_configuration.png %}){: style="max-width:80%;"}

Senden Sie dann ein Test-Event an Ihre Datentransformation.

### 3. Schritt: Schreiben Sie den Code für die Transformation, um die von Ihnen gewählten Stripe-Events zu akzeptieren {#step-3-write-transformation-code-to-accept-your-chosen-stripe-events}

Als Nächstes transformieren Sie die Webhook-Nutzdaten, die von Stripe gesendet werden, in einen JavaScript-Objektrückgabewert.

1. Aktualisieren Sie Ihre Datentransformation und vergewissern Sie sich, dass Sie die Stripe-Test-Nutzdaten im Bereich **Webhook details** sehen können.
2. Aktualisieren Sie Ihren Code für die Datentransformation, um die von Ihnen gewählten Stripe-Events zu unterstützen.
3. Wählen Sie **Validate** aus, um eine Vorschau auf die Ausgabe Ihres Codes zu erhalten und um zu prüfen, ob es sich um eine akzeptable `/users/track`-Anfrage handelt.
4. Speichern und aktivieren Sie Ihre Datentransformation.

![Ein Beispiel für Webhook-Details und den Code für die Transformation.]({% image_buster /assets/img/stripe/stripe_data_transformation.png %})

#### Format des Anfragekörpers {#request-body-format}

Dieser Rückgabewert muss dem Format des Anfragekörpers für den Endpunkt `/users/track` entsprechen:

- Der Code für die Transformation wird in der Programmiersprache JavaScript akzeptiert. Jeder Standard-JavaScript-Kontrollfluss, wie z. B. die if/else-Logik, wird unterstützt.
- Der Code der Transformation greift über die Nutzlastvariable auf den Körper der Webhook-Anfrage zu. Diese Variable ist ein Objekt, das durch das Parsen des JSON-Körpers der Anfrage erstellt wird.
- Alle Features, die in unserem `/users/track`-Endpunkt unterstützt werden, werden unterstützt, einschließlich:
    - Nutzerattribut-Objekte, Event-Objekte und Kauf-Objekte
    - Verschachtelte Attribute und verschachtelte Eigenschaften von angepassten Events
    - Updates für Abo-Gruppen
    - E-Mail-Adresse als Bezeichner

### 4. Schritt: Veröffentlichen Sie Ihren Stripe-Webhook {#step-4-publish-your-stripe-webhook}

Nachdem Sie Ihre Datentransformation geschrieben haben, wählen Sie **Validate**, um sicherzustellen, dass Ihr Code für die Datentransformation richtig formatiert ist und wie erwartet funktioniert. Dann speichern und aktivieren Sie Ihre Datentransformation. Nach der Aktivierung werden angepasste Event-Daten im Profil einer Nutzerin bzw. eines Nutzers protokolliert, wenn diese bzw. dieser das Event abschließt.

![Ein angepasstes Stripe-Event „Charge Succeeded“ in einem Braze-Nutzerprofil.]({% image_buster /assets/img/stripe/stripe_braze_profile_event.png %}){: style="max-width:80%;"}

## Beispiel für Webhook-Nutzdaten von Stripe {#example}

```json
{
 "headers": {
   "Version": "HTTP/1.1",
   "X-Datadog-Trace-Id": "9124157397962821303",
   "X-Datadog-Parent-Id": "9124157397962821303",
   "X-Datadog-Sampling-Priority": "2",
   "Host": "xxx",
   "X-Request-Id": "xxx",
   "X-Real-Ip": "165.159.72.690",
   "X-Forwarded-For": "161.123.56.890",
   "X-Forwarded-Host": "xxx",
   "X-Forwarded-Port": "443",
   "X-Forwarded-Proto": "https",
   "X-Forwarded-Scheme": "https",
   "X-Scheme": "https",
   "X-Original-Forwarded-For": "12.345.678.123",
   "Cf-Ray": "9470a06172f8816e-IAD",
   "Cache-Control": "no-cache",
   "User-Agent": "Stripe/1.0 (+https://stripe.com/docs/webhooks)",
   "Accept-Encoding": "gzip",
   "Cf-Connecting-Ip": "12.123.456.789",
   "Cf-Visitor": "{\"scheme\":\"https\"}",
   "X-Worker-Executions": "1",
   "Cf-Worker": "xxx",
   "X-Fastly-Geoloc-Countrycode": "US",
   "Stripe-Signature": "t=xxx,v1=xxxx,v0=xxxx",
   "Cf-Ew-Via": "15",
   "Cdn-Loop": "cloudflare; loops=1; subreqs=1",
   "Accept": "*/*; q=0.5, application/xml"
 },
 "payload": {
   "id": "evt_3RTqw0RMEOaIvYpU1k2TFajH",
   "object": "event",
   "api_version": "2025-04-30.basil",
   "created": 1748465448,
   "data": {
     "object": {
       "id": "ch_3RTqw0RMEOaIvYpU1M9ZYtjP",
       "object": "charge",
       "amount": 100,
       "amount_captured": 100,
       "amount_refunded": 0,
       "application": null,
       "application_fee": null,
       "application_fee_amount": null,
       "balance_transaction": null,
       "billing_details": {
         "address": {
           "city": null,
           "country": null,
           "line1": null,
           "line2": null,
           "postal_code": null,
           "state": null
         },
         "email": null,
         "name": null,
         "phone": null,
         "tax_id": null
       },
       "calculated_statement_descriptor": "Stripe",
       "captured": true,
       "created": 1748465448,
       "currency": "usd",
       "customer": "cus_SOeDf39aosGb97",
       "description": "(created by Stripe CLI)",
       "destination": null,
       "dispute": null,
       "disputed": false,
       "failure_balance_transaction": null,
       "failure_code": null,
       "failure_message": null,
       "fraud_details": {},
       "livemode": false,
       "metadata": {},
       "on_behalf_of": null,
       "order": null,
       "outcome": {
         "advice_code": null,
         "network_advice_code": null,
         "network_decline_code": null,
         "network_status": "approved_by_network",
         "reason": null,
         "risk_level": "normal",
         "risk_score": 9,
         "seller_message": "Payment complete.",
         "type": "authorized"
       },
       "paid": true,
       "payment_intent": "pi_3RTqw0RMEOaIvYpU1pQl3Lmp",
       "payment_method": "pm_1RTqw0RMEOaIvYpU5VE8HFlp",
       "payment_method_details": {
         "card": {
           "amount_authorized": 100,
           "authorization_code": null,
           "brand": "visa",
           "checks": {
             "address_line1_check": null,
             "address_postal_code_check": null,
             "cvc_check": "pass"
           },
           "country": "US",
           "exp_month": 5,
           "exp_year": 2026,
           "extended_authorization": {
             "status": "disabled"
           },
           "fingerprint": "HAKdyqJ9xh2YhbzT",
           "funding": "credit",
           "incremental_authorization": {
             "status": "unavailable"
           },
           "installments": null,
           "last4": "4242",
           "mandate": null,
           "multicapture": {
             "status": "unavailable"
           },
           "network": "visa",
           "network_token": {
             "used": false
           },
           "network_transaction_id": "726575100121113",
           "overcapture": {
             "maximum_amount_capturable": 100,
             "status": "unavailable"
           },
           "regulated_status": "unregulated",
           "three_d_secure": null,
           "wallet": null
         },
         "type": "card"
       },
       "radar_options": {},
       "receipt_email": null,
       "receipt_number": null,
       "receipt_url": "https://pay.stripe.com/receipts/payment/xxx",
       "refunded": false,
       "review": null,
       "shipping": null,
       "source": null,
       "source_transfer": null,
       "statement_descriptor": null,
       "statement_descriptor_suffix": null,
       "status": "succeeded",
       "transfer_data": null,
       "transfer_group": null
     }
   },
   "livemode": false,
   "pending_webhooks": 3,
   "request": {
     "id": "req_jqtL1Q6CPaNx8x",
     "idempotency_key": "f0f9aee4-a889-4fcc-bc2e-fa41fa426f05"
   },
   "type": "charge.succeeded"
 }
}
```

## Anwendungsfälle der Datentransformation {#data-transformation-use-cases}

Nachfolgend finden Sie Beispiel-Templates, die mit unserem [Stripe-Webhook-Beispiel](#example) erstellt wurden. Diese Templates können als Ausgangspunkt verwendet werden. Sie können ganz von vorne anfangen oder bestimmte Komponenten löschen, wenn Sie es für richtig halten.

In diesem Beispiel-Template protokollieren wir ein angepasstes Event für das Braze-Profil. Der Event-Typ wird als angepasster Event-Name gesendet, und das Datenobjekt wird als Event-Eigenschaften übergeben.

### Anwendungsfall: geschäftskunden als Bezeichner {#use-case-customer-as-an-identifier}

In diesem Beispiel-Template verwenden wir das Feld „geschäftskunden“ als Bezeichner.

{% tabs local %}
{% tab Input %}

```javascript

/* This template is based on the source platform's documentation here: https://stripe.com/docs/webhooks


/* Braze's /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Stripe's charge succeeded event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.data.object.created;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();


/* defines a variable 'brazecall' that will hold the request payload for the /users/track request
let brazecall;


/* if the type is charge.succeeded and customer field is not null, build the /users/track request to log an event to the user profile
if (payload.type == "charge.succeeded" && payload.data.object.customer) {
 brazecall = {
   "events": [
     {
       "external_id": payload.data.object.customer,
       "name": "Charge Succeeded",
       "time": isoString,
       "properties": {
         "amount": payload.data.object.amount,
         "paid": payload.data.object.paid,
         "status": payload.data.object.status
       }
     }
   ]
 };
}
/* After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Output %}

```json
{
  "events": [
    {
      "external_id": "an_account@example.com",
      "name": "Charge Succeeded",
      "time": "2025-05-28T18:21:39.527Z",
      "properties": {
        "amount": 100,
    "paid":true,
    "Status":"succeeded"
    }
   }
  ]
}
```

{% endtab %}
{% endtabs %}

## Überwachung und Fehlerbehebung {#monitoring-and-troubleshooting}

Weitere Informationen zur Überwachung und Fehlerbehebung Ihrer Transformation finden Sie unter [Überwachung Ihrer Transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-5-monitor-your-transformation).