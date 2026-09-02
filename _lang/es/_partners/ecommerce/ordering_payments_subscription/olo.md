---
nav_title: Olo
article_title: Olo
description: "Este artículo describe la asociación entre Braze y Olo, una plataforma SaaS abierta líder para restaurantes que habilita la hostelería en cada punto de intervención."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo](https://www.olo.com/) es una plataforma SaaS abierta líder para restaurantes que habilita la hostelería en cada punto de intervención.

Al integrar Olo y Braze, puedes:

- Actualizar los perfiles de usuario en Braze para mantenerlos coherentes con los perfiles de usuario de Olo
- Enviar el siguiente mejor mensaje desde Braze basándote en eventos de Olo

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Olo | Se requiere una cuenta de Olo con acceso a webhooks para aprovechar esta integración. Configura las suscripciones de webhooks a través de la [herramienta de webhooks de autoservicio](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dentro del panel de Olo. |
| Transformación de datos de Braze | Se necesita una [URL de Transformación de datos]({{site.baseurl}}/user_guide/data/unification/data_transformation) para recibir datos de Olo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

Un webhook es una forma en que Olo envía información basada en eventos a Braze sobre los usuarios y sus acciones, incluidos eventos como Order Placed, Guest Opt In, Order Picked Up y más. El webhook de Olo entrega el evento a Braze generalmente en cuestión de segundos después de que se realiza la acción.

## Descargo de responsabilidad {#disclaimer}

En Olo, estás limitado a un webhook por entorno para cada marca aprobada, todos enviados a la misma **URL de destino**. Las distintas marcas pueden tener URLs diferentes, pero los eventos de la misma marca deben compartir una URL. En Braze, esto significa que solo puedes crear una transformación para usarla con Olo.

Para gestionar múltiples eventos de Olo dentro de esta única transformación, busca el encabezado `X-Olo-Event-Type` en cada webhook. Este encabezado te permite procesar condicionalmente diferentes eventos de Olo.

## Integración {#integration}

### Paso 1: Configura la transformación de datos de Braze para aceptar el evento de prueba de Olo {#step-1}

{% multi_lang_include data_activation/create_transformation.md location="default" %}

### Paso 2: Configura los webhooks de Olo {#step-2-set-up-olo-webhooks}

Usa la [herramienta de webhooks de autoservicio](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dentro del panel de Olo para configurar webhooks que envíen datos a tu transformación de datos.

1. Elige qué eventos deben enviarse a Braze
2. Configura la **URL de destino**. Esta será la URL de la transformación de datos creada en el [paso 1](#step-1).

{% alert note %}
`OAuth` y el secreto compartido del encabezado `X-Olo-Signature` no son necesarios para la transformación.
{% endalert %}

{:start="3"}
3. Verifica que el webhook esté configurado correctamente enviando un [evento de prueba](https://developer.olo.com/docs/load/webhooks#operation/test) a tu transformación de datos. Solo los usuarios del panel de Olo con el [permiso de herramientas de desarrollador](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions) pueden enviar eventos de prueba.

Olo requiere una respuesta exitosa del webhook del evento de prueba antes de que puedas completar el proceso de configuración de webhooks de Olo.

### Paso 3: Escribe el código de transformación para aceptar los eventos de Olo que hayas elegido {#step-3-write-transformation-code-to-accept-your-chosen-olo-events}

En este paso, transformarás la carga útil del webhook que se enviará desde la plataforma de origen en un valor de retorno de objeto JavaScript.

1. Envía una solicitud a la URL de tu transformación de datos con una carga útil de evento de muestra de un evento de Olo que desees soportar. Consulta el [formato del cuerpo de la solicitud](#request-body-format) para obtener ayuda con el formato de tu solicitud.
2. Actualiza tu transformación de datos y asegúrate de que puedas ver la carga útil del evento de muestra en los **detalles del webhook**.
3. Actualiza el código de tu transformación de datos para soportar los eventos de Olo que hayas elegido.
4. Haz clic en **Validar** para obtener una vista previa del resultado de tu código y comprobar si es una solicitud `/users/track` aceptable.
5. Guarda y activa tu transformación de datos.

#### Formato del cuerpo de la solicitud {#request-body-format}

Este valor de retorno debe cumplir con el formato del cuerpo de la solicitud `/users/track` de Braze:

{% multi_lang_include data_transformation/transformation_code_requirements.md %}

## Ejemplos de transformaciones de datos para webhooks de Olo {#example-data-transformations-for-olo-webhooks}

Esta sección contiene plantillas de ejemplo que se pueden utilizar como punto de partida. Puedes partir desde cero o eliminar componentes específicos como consideres necesario.

En cada plantilla, el código define una variable, `brazecall`, para construir una solicitud `/users/track`.

Después de que la solicitud `/users/track` se asigna a `brazecall`, devolverás explícitamente `brazecall` para crear una salida.

### Transformación de un solo evento {#single-event-transformation}

Si solo buscas admitir un único evento de Olo, no necesitarás usar el encabezado `X-Olo-Event-Type` para crear condicionalmente la carga útil de la solicitud `/users/track`. Por ejemplo, registrar un evento de compra o un evento personalizado en el perfil de usuario cuando se envía un webhook de pedido realizado de Olo a Braze.

### Registrar cada producto como una compra {#logging-each-product-as-a-purchase}

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### Registrar un evento personalizado {#logging-a-custom-event}

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = {
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## Transformación multievento {#multi-event-transformation}

Olo envía el tipo de evento dentro del encabezado `X-Olo-Event-Type` de cada webhook. Para admitir múltiples eventos de webhook de Olo dentro de una única transformación, usa lógica condicional para transformar la carga útil del webhook en función del valor de este tipo de encabezado.

En el siguiente ejemplo de transformación, nuestro JavaScript crea una carga útil particular para los eventos `UserSignedUp` y `OrderPlaced`. Además, una condición `else` maneja una carga útil para cualquier evento de Olo enviado a Braze sin el encabezado X-Olo-Event-Type de `UserSignedUp` y `OrderPlaced`.

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### Paso 4: Publica tu webhook de Olo {#step-4-publish-your-olo-webhook}

Después de haber activado tu transformación de datos en Braze, usa la [herramienta de webhooks de autoservicio](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dentro del panel de Olo para publicar tu webhook. Cuando el webhook esté publicado, la transformación de datos comenzará a recibir mensajes de eventos de webhook de Olo.

## Cosas que debes saber {#things-to-know}

### Reintentos {#retries}

Olo reintentará las llamadas de webhook que resulten en un código de estado de respuesta HTTP `429 - Too Many Requests` o en el rango `5xx` (por ejemplo, debido a un tiempo de espera del gateway o un error del servidor), hasta 50 veces durante un período de 24 horas antes de descartar la solicitud.

### Entrega al menos una vez {#at-least-once-delivery}

Si una llamada de webhook resulta en un código de estado de respuesta HTTP `429 - Too Many Requests` o en el rango `5xx` (por ejemplo, debido a un tiempo de espera del gateway o un error del servidor), Olo reintentará el mensaje hasta 50 veces durante un período de 24 horas antes de abandonar el intento.

Por lo tanto, los webhooks pueden ser recibidos varias veces por un suscriptor. Es responsabilidad del suscriptor ignorar los duplicados comprobando el encabezado `X-Olo-Message-Id`.