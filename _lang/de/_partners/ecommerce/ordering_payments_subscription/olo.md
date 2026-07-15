---
nav_title: Olo
article_title: Olo
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Olo, einer führenden offenen SaaS-Plattform für Restaurants, die Gastfreundschaft an jedem Touchpoint ermöglicht."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo](https://www.olo.com/) ist eine führende offene SaaS-Plattform für Restaurants, die Gastfreundschaft an jedem Touchpoint ermöglicht.

Durch die Integration von Olo und Braze können Sie:

- Nutzerprofile in Braze aktualisieren, damit sie mit den Olo-Nutzerprofilen übereinstimmen
- Die richtigen nächstbesten Nachrichten von Braze basierend auf Olo-Events senden

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Olo-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Olo-Konto mit Zugriff auf Webhooks. Richten Sie Webhook-Abonnements über das [Self-Service-Webhooks-Tool](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) im Olo-Dashboard ein. |
| Braze-Datentransformation | Eine [URL für die Datentransformation]({{site.baseurl}}/data_transformation) ist erforderlich, um Daten von Olo zu empfangen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

Ein Webhook ist eine Möglichkeit für Olo, ereignisgesteuerte Informationen über Nutzer:innen und deren Aktionen an Braze zu senden, einschließlich Events wie „Bestellung aufgegeben“, „Gast-Opt-in“, „Bestellung abgeholt“ und mehr. Der Olo-Webhook stellt Braze das Event in der Regel innerhalb von Sekunden nach Ausführung der Aktion zu.

## Haftungsausschluss {#disclaimer}

In Olo sind Sie auf einen Webhook pro Umgebung für jede genehmigte Marke beschränkt, die alle an dieselbe **Ziel-URL** gesendet werden. Verschiedene Marken können unterschiedliche URLs haben, aber Events derselben Marke müssen eine gemeinsame URL haben. In Braze bedeutet dies, dass Sie nur eine Transformation für die Verwendung mit Olo erstellen können.

Um mehrere Olo-Events innerhalb dieser einzigen Transformation zu verarbeiten, suchen Sie in jedem Webhook nach dem `X-Olo-Event-Type`-Header. Dieser Header ermöglicht es Ihnen, verschiedene Olo-Events bedingt zu verarbeiten.

## Integration

### Schritt 1: Braze-Datentransformation einrichten, um das Test-Event von Olo zu akzeptieren {#step-1}

{% multi_lang_include data_activation/create_transformation.md location="default" %}

### Schritt 2: Olo-Webhooks einrichten {#step-2-set-up-olo-webhooks}

Verwenden Sie das [Self-Service-Webhooks-Tool](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) im Olo-Dashboard, um Webhooks einzurichten, die an Ihre Datentransformation gesendet werden.

1. Wählen Sie, welche Events an Braze gesendet werden sollen.
2. Konfigurieren Sie die **Ziel-URL**. Dies ist die in [Schritt 1](#step-1) erstellte URL für die Datentransformation.

{% alert note %}
`OAuth` und das gemeinsame Geheimnis des `X-Olo-Signature`-Headers werden für die Transformation nicht benötigt.
{% endalert %}

{:start="3"}
3. Überprüfen Sie, ob der Webhook richtig konfiguriert ist, indem Sie ein [Test-Event](https://developer.olo.com/docs/load/webhooks#operation/test) an Ihre Datentransformation senden. Nur Nutzer:innen des Olo-Dashboards mit der [Berechtigung für Entwickler:innen-Tools](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions) können Test-Events senden.

Olo benötigt eine erfolgreiche Antwort vom Test-Event-Webhook, bevor Sie die Konfiguration des Olo-Webhooks abschließen können.

### Schritt 3: Transformationscode schreiben, um die von Ihnen gewählten Olo-Events zu akzeptieren {#step-3-write-transformation-code-to-accept-your-chosen-olo-events}

In diesem Schritt transformieren Sie die Webhook-Nutzlast, die von der Quellplattform gesendet wird, in einen Rückgabewert als JavaScript-Objekt.

1. Senden Sie eine Anfrage an Ihre URL für die Datentransformation mit einer Beispiel-Nutzlast eines Olo-Events, das Sie unterstützen möchten. Siehe [Format des Anfragekörpers](#request-body-format) für Hilfe bei der Formatierung Ihrer Anfrage.
2. Aktualisieren Sie Ihre Datentransformation und vergewissern Sie sich, dass Sie die Beispiel-Nutzlast des Events in den **Webhook-Details** sehen können.
3. Aktualisieren Sie Ihren Datentransformationscode, um die von Ihnen gewählten Olo-Events zu unterstützen.
4. Klicken Sie auf **Validate**, um eine Vorschau der Ausgabe Ihres Codes zu erhalten und zu prüfen, ob es sich um eine akzeptable `/users/track`-Anfrage handelt.
5. Speichern und aktivieren Sie Ihre Datentransformation.

#### Format des Anfragekörpers {#request-body-format}

Dieser Rückgabewert muss dem Format des `/users/track`-Anfragekörpers von Braze entsprechen:

- Der Transformationscode wird in der Programmiersprache JavaScript akzeptiert. Jeder Standard-JavaScript-Kontrollfluss, wie z. B. die if/else-Logik, wird unterstützt.
- Der Transformationscode greift über die Nutzlastvariable auf den Körper der Webhook-Anfrage zu. Diese Variable ist ein Objekt, das durch das Parsen des JSON-Körpers der Anfrage erstellt wird.
- Alle Features, die in unserem `/users/track`-Endpunkt unterstützt werden, werden unterstützt, einschließlich:
    - Nutzerattribut-Objekte, Event-Objekte und Kauf-Objekte
    - Verschachtelte Attribute und verschachtelte Event-Eigenschaften angepasster Events
    - Updates für Abo-Gruppen
    - E-Mail-Adresse als Bezeichner

## Beispiel-Datentransformationen für Olo-Webhooks {#example-data-transformations-for-olo-webhooks}

Dieser Abschnitt enthält Beispiel-Templates, die als Ausgangspunkt verwendet werden können. Sie können auch von Grund auf neu beginnen oder bestimmte Komponenten nach Belieben löschen.

In jedem Template definiert der Code eine Variable, `brazecall`, um eine `/users/track`-Anfrage zu erstellen.

Nachdem die `/users/track`-Anfrage `brazecall` zugewiesen wurde, geben Sie explizit `brazecall` zurück, um eine Ausgabe zu erstellen.

### Transformation eines einzelnen Events {#single-event-transformation}

Wenn Sie nur ein einziges Olo-Event unterstützen möchten, brauchen Sie den `X-Olo-Event-Type`-Header nicht zu verwenden, um die Nutzlast der `/users/track`-Anfrage bedingt zu erstellen. Zum Beispiel das Protokollieren eines Kauf-Events oder eines angepassten Events im Nutzerprofil, wenn ein Olo-Order-Placed-Webhook an Braze gesendet wird.

### Jedes Produkt als Kauf protokollieren {#logging-each-product-as-a-purchase}

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

### Protokollieren eines angepassten Events {#logging-a-custom-event}

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

## Multi-Event-Transformation

Olo sendet den Event-Typ im `X-Olo-Event-Type`-Header jedes Webhooks. Um mehrere Olo-Webhook-Events innerhalb einer einzigen Transformation zu unterstützen, verwenden Sie bedingte Logik, um die Webhook-Nutzlast basierend auf dem Wert dieses Header-Typs zu transformieren.

Im folgenden Transformationsbeispiel erstellt unser JavaScript eine bestimmte Nutzlast für die Events `UserSignedUp` und `OrderPlaced`. Zusätzlich behandelt eine `else`-Bedingung eine Nutzlast für alle Olo-Events, die ohne den X-Olo-Event-Type-Header `UserSignedUp` und `OrderPlaced` an Braze gesendet werden.

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

### Schritt 4: Olo-Webhook veröffentlichen {#step-4-publish-your-olo-webhook}

Nachdem Sie Ihre Datentransformation in Braze aktiviert haben, verwenden Sie das [Self-Service-Webhooks-Tool](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) im Olo-Dashboard, um Ihren Webhook zu veröffentlichen. Wenn der Webhook veröffentlicht wird, beginnt die Datentransformation mit dem Empfang von Olo-Webhook-Event-Nachrichten.

## Wissenswertes {#things-to-know}

### Wiederholungsversuche {#retries}

Olo wiederholt Webhook-Aufrufe, die zu einem HTTP-Antwort-Statuscode von `429 - Too Many Requests` oder im Bereich `5xx` führen (z. B. aufgrund eines Gateway-Timeouts oder eines Server-Fehlers), innerhalb von 24 Stunden bis zu 50 Mal, bevor die Anfrage verworfen wird.

### Zustellung mindestens einmal {#at-least-once-delivery}

Wenn ein Webhook-Aufruf zu einem HTTP-Antwort-Statuscode von `429 - Too Many Requests` oder im Bereich `5xx` führt (z. B. aufgrund eines Gateway-Timeouts oder eines Server-Fehlers), versucht Olo die Nachricht innerhalb von 24 Stunden bis zu 50 Mal erneut zu senden, bevor es aufgibt.

Webhooks können daher mehrfach von Abonnent:innen empfangen werden. Es liegt in der Verantwortung der Abonnent:innen, Duplikate zu ignorieren, indem sie den `X-Olo-Message-Id`-Header überprüfen.