---
nav_title: Stripe
article_title: Stripe
description: "Este artículo describe la asociación entre Braze y Stripe."
alias: /partners/stripe/
page_type: partner
search_tag: Partner
---

# Stripe

> [Stripe](https://www.stripe.com/) es una plataforma integral de infraestructura financiera que permite a las empresas aceptar pagos, gestionar operaciones de ingresos y facilitar el comercio global a través de una línea de productos de API y servicios integrados.

Al integrar Braze y Stripe, puedes:

- Actualizar los perfiles de usuario en Braze con datos de pago y facturación en tiempo real de Stripe.
- Desencadenar mensajería en Braze basándote en eventos de Stripe como inicio de prueba, activación de suscripción, cancelación de suscripción y más.
- Personalizar la mensajería de Braze en función del historial de pagos de un usuario o del estado de facturación recibido mediante webhooks de Stripe.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Stripe | Se requiere una cuenta de Stripe con acceso a webhooks para aprovechar esta asociación. |
| Transformación de datos de Braze | Se necesita una [URL de Transformación de datos]({{site.baseurl}}/data_transformation/) para recibir datos de Stripe. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

## Integración {#integration}

### Paso 1: Configura la Transformación de datos de Braze para aceptar los webhooks de Stripe {#step-1}

{% multi_lang_include create_transformation.md %}

### Paso 2: Configura los webhooks de Stripe {#step-2-set-up-stripe-webhooks}

Sigue los pasos de la [documentación de webhooks de Stripe](https://docs.stripe.com/development/dashboard/webhooks) para configurar un webhook.

Añade la URL de tu webhook de Transformación de datos como **Destination URL** y selecciona los tipos de eventos que deseas enviar a Braze. Consulta la [documentación de Stripe](https://docs.stripe.com/api/events/types) para obtener una lista completa de tipos de eventos.

![Un ejemplo de configuración de webhook de Stripe.]({% image_buster /assets/img/stripe/stripe_webhook_configuration.png %}){: style="max-width:80%;"}

A continuación, envía un evento de prueba a tu Transformación de datos.

### Paso 3: Escribe el código de transformación para aceptar los eventos de Stripe que elijas {#step-3-write-transformation-code-to-accept-your-chosen-stripe-events}

A continuación, transformarás la carga útil del webhook que se enviará desde Stripe en un valor de retorno de objeto JavaScript.

1. Actualiza tu Transformación de datos y asegúrate de que puedes ver la carga útil de prueba de Stripe en la sección **Webhook details**.
2. Actualiza tu código de Transformación de datos para que admita los eventos de Stripe que hayas elegido.
3. Selecciona **Validate** para obtener una vista previa de la salida de tu código y comprobar si se trata de una solicitud `/users/track` aceptable.
4. Guarda y activa tu Transformación de datos.

![Un ejemplo de detalles de webhook y código de transformación.]({% image_buster /assets/img/stripe/stripe_data_transformation.png %})

#### Formato del cuerpo de la solicitud {#request-body-format}

Este valor de retorno debe ajustarse al formato del cuerpo de la solicitud del punto de conexión `/users/track`:

- El código de transformación se acepta en el lenguaje de programación JavaScript. Se admite cualquier flujo de control estándar de JavaScript, como la lógica if/else.
- El código de transformación accede al cuerpo de la solicitud del webhook utilizando la variable de carga útil. Esta variable es un objeto poblado por el análisis del cuerpo de la solicitud JSON.
- Se admite cualquier característica de nuestro punto de conexión `/users/track`, incluidos:
    - Objetos de atributo de usuario, objetos de evento y objetos de compra
    - Atributos anidados y propiedades anidadas de eventos personalizados
    - Actualizaciones de grupos de suscripción
    - Dirección de correo electrónico como identificador

### Paso 4: Publica tu webhook de Stripe {#step-4-publish-your-stripe-webhook}

Después de escribir tu Transformación de datos, selecciona **Validate** para asegurarte de que tu código de Transformación de datos tiene el formato correcto y funcionará como se espera. A continuación, guarda y activa tu Transformación de datos. Tras la activación, los datos del evento personalizado se registrarán en el perfil de un usuario cuando este complete el evento.

![Un evento personalizado de Stripe "Charge Succeeded" en un perfil de usuario de Braze.]({% image_buster /assets/img/stripe/stripe_braze_profile_event.png %}){: style="max-width:80%;"}

## Ejemplo de carga útil de webhook de Stripe {#example}

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

## Casos de uso de Transformación de datos {#data-transformation-use-cases}

Las siguientes son plantillas de ejemplo creadas utilizando nuestro [ejemplo de carga útil de webhook de Stripe](#example). Estas plantillas pueden servirte de punto de partida. Puedes empezar desde cero o eliminar componentes específicos según te convenga.

En esta plantilla de ejemplo, estamos registrando un evento personalizado en el perfil de Braze. El tipo de evento se enviará como nombre del evento personalizado, y el objeto de datos se pasará como propiedades del evento.

### Caso de uso: el cliente como identificador {#use-case-customer-as-an-identifier}

En esta plantilla de ejemplo, estamos utilizando el campo de cliente como identificador.

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

## Supervisión y solución de problemas {#monitoring-and-troubleshooting}

Consulta [Supervisar tu transformación]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#step-5-monitor-your-transformation) para obtener más información sobre la supervisión y solución de problemas de tu transformación.