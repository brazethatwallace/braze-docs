---
nav_title: Transformation erstellen
article_title: Transformation erstellen
page_order: 1
page_type: reference
description: "Dieser Referenzartikel beschreibt die Schritte zur Erstellung einer Transformation mit Braze Datentransformation."
---

# Transformation erstellen {#create-a-transformation}

> Mit Braze Datentransformation können Sie Webhook-Integrationen erstellen und verwalten, um den Datenfluss von externen Plattformen in Braze zu automatisieren. Diese Webhook-Integrationen können dann noch leistungsfähigere Anwendungsfälle im Marketing unterstützen. Sie können Ihre Datentransformation aus dem Standardcode erstellen oder unsere spezielle Bibliothek mit Templates verwenden, um Ihnen den Einstieg in bestimmte externe Plattformen zu erleichtern.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Zwei-Faktor-Authentifizierung oder SSO | Sie müssen die [Zwei-Faktor-Authentifizierung]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#two-factor-authentication-2fa) (2FA) oder [Single Sign-on]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#single-sign-on-sso-authentication) (SSO) für Ihr Konto aktiviert haben. |
| Korrekte Berechtigungen | Sie müssen entweder Konto-Admin oder Workspace-Admin sein oder über die Nutzer:innen-Berechtigung „Transformationen verwalten“ verfügen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Schritt 1: Quellplattform identifizieren {#step-1-identify-a-source-platform}

Identifizieren Sie eine externe Plattform, die Sie mit Braze verbinden möchten, und überprüfen Sie, ob die Plattform Webhooks unterstützt. Diese Einstellungen werden manchmal auch als „API-Benachrichtigungen“ oder „Anfragen für Webdienste“ bezeichnet.

Im Folgenden finden Sie ein Beispiel für einen [Typeform-Webhook](https://www.typeform.com/help/a/webhooks-360029573471/), der durch Anmeldung bei der Plattform konfiguriert werden kann:

![Ein Beispiel für eine Typeform-Webhook-Nutzlast in den Typeform-Plattformeinstellungen.]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## Schritt 2: Transformation erstellen {#step-2-create-a-transformation}

{% multi_lang_include data_activation/create_transformation.md location="default" %}

## Schritt 3: Test-Webhook senden (empfohlen) {#step-3-send-a-test-webhook-recommended}

Dieser Schritt ist optional, aber wir empfehlen, einen Test-Webhook von Ihrer Quellplattform an Ihre neu erstellte Transformation zu senden.

1. Kopieren Sie die URL aus Ihrer Transformation.
2. Suchen Sie in Ihrer Quellplattform nach einer „Test senden“-Funktion, um einen Beispiel-Webhook zu generieren, der an diese URL gesendet wird.
   - Wenn Ihre Quellplattform nach einem Anfragetyp fragt, wählen Sie **POST**.
   - Wenn Ihre Quellplattform Authentifizierungsoptionen bietet, wählen Sie **No authentication**.
   - Wenn Ihre Quellplattform nach Geheimnissen fragt, wählen Sie **No secrets**.
3. Aktualisieren Sie Ihre Seite im Braze-Dashboard, um zu sehen, ob der Webhook empfangen wurde. Wenn er empfangen wurde, sollten Sie unter **Most recent webhook** eine Webhook-Nutzlast sehen.

So sieht es bei Typeform aus:

![Beispiel für Datentransformationscode, der den Webhook auf Braze-Nutzerprofile abbildet.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Braze Datentransformation unterstützt möglicherweise noch keine externen Plattformen, die eine spezielle Überprüfung oder Authentifizierung für Webhooks erfordern. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="webhook authentication for external platforms" %}
{% endalert %}

## Schritt 4: Transformationscode schreiben {#step-4-write-transformation-code}

Wenn Sie wenig bis gar keine Erfahrung mit JavaScript-Code haben oder detailliertere Anweisungen bevorzugen, folgen Sie dem Tab **Anfänger – POST: Nutzer:innen tracken** oder **Anfänger – PUT: Mehrere Katalogartikel aktualisieren** zum Schreiben Ihres Transformationscodes.

Wenn Sie Entwickler:in sind oder über umfangreiche Erfahrung mit JavaScript-Code verfügen, folgen Sie dem Tab **Fortgeschritten – POST: Nutzer:innen tracken** für übergeordnete Anweisungen zum Schreiben Ihres Transformationscodes.

{% alert tip %}
Um Transformationscode mit KI zu generieren, wählen Sie **Code with Operator** im Transformationscode-Editor. Dazu muss ein Webhook an Ihre Transformation gesendet worden sein. Um stattdessen mit einem vorgefertigten Template zu beginnen, wählen Sie **Insert Template**. Beispiel-Prompts finden Sie unter [Datentransformationscode generieren]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-data-transformation-code).

**Code with Operator** ist nur verfügbar, wenn Operator für Ihr Konto aktiviert ist. Wenn Sie diese Option nicht sehen, wenden Sie sich an Ihren Account Manager.
{% endalert %}

{% tabs %}
{% tab Anfänger – Nutzer:innen tracken %}

Schreiben Sie hier den Transformationscode, um zu definieren, wie verschiedene Webhook-Werte auf Braze-Nutzerprofile abgebildet werden.

1. Neue Transformationen haben dieses Standard-Template im Abschnitt **Transformation Code**:

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. Um angepasste Attribute, angepasste Events und Käufe in Ihre Transformationsaufrufe einzubeziehen, fahren Sie mit Schritt 3 fort. Andernfalls löschen Sie die Abschnitte, die Sie nicht benötigen.<br><br>
3. Für jedes Attribut-, Event- und Kauf-Objekt ist ein Nutzer:innen-Bezeichner erforderlich, entweder ein `external_id`, `user_alias`, `braze_id`, `email` oder `phone`. Suchen Sie den Nutzer:innen-Bezeichner in der Nutzlast des eingehenden Webhooks und fügen Sie diesen Wert über eine Nutzlastzeile als Template in Ihren Transformationscode ein. Verwenden Sie die Punktnotation, um auf die Eigenschaften von Nutzlastobjekten zuzugreifen.<br><br>
4. Finden Sie die Webhook-Werte, die Sie als Attribute, Events oder Käufe darstellen möchten, und erstellen Sie ein Template für diese Werte in Ihrem Transformationscode über eine Nutzlastzeile. Verwenden Sie die Punktnotation, um auf die Eigenschaften von Nutzlastobjekten zuzugreifen.<br><br>
5. Prüfen Sie für jedes Attribut-, Event- und Kauf-Objekt den Wert `_update_existing_only`. Setzen Sie diesen auf `false`, wenn Sie möchten, dass die Transformation neue Nutzer:innen erstellt, die möglicherweise noch nicht existieren. Belassen Sie den Wert auf `true`, um nur bestehende Profile zu aktualisieren.<br><br>
6. Klicken Sie auf **Validate**, um eine Vorschau der Ausgabe Ihres Codes zu erhalten und zu prüfen, ob es sich um eine akzeptable `/users/track`-Anfrage handelt.<br><br>
7. Aktivieren Sie Ihre Transformation. Wenn Sie weitere Hilfe zu Ihrem Code benötigen, bevor Sie ihn aktivieren, wenden Sie sich an Ihren Braze Account Manager.<br><br>
7. Lassen Sie Ihre Quellplattform mit dem Senden von Webhooks beginnen. Ihr Transformationscode wird für jeden eingehenden Webhook ausgeführt, und die Nutzerprofile werden aktualisiert.

Ihre Webhook-Integration ist nun abgeschlossen!

{% endtab %}
{% tab Anfänger – Katalogartikel aktualisieren %}

Hier können Sie Transformationscode schreiben, um zu definieren, wie Sie verschiedene Webhook-Werte auf Updates von Braze-Katalogartikeln abbilden möchten.

1. Neue Transformationen enthalten dieses Standard-Template im Abschnitt **Transformation Code**:

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",

  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: {{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2. Transformationen für `/catalogs`-Ziele erfordern einen `catalog_name`, um den spezifischen Katalog zu definieren, der aktualisiert werden soll. Sie können dieses Feld fest codieren oder das Feld über eine Nutzlastzeile mit einem Webhook-Feld als Template einfügen. Verwenden Sie die Punktnotation, um auf die Eigenschaften von Nutzlastobjekten zuzugreifen.<br><br>
3. Definieren Sie die Artikel, die Sie im Katalog aktualisieren möchten, mit den `id`-Feldern im Artikel-Array. Sie können diese Felder fest codieren oder ein Webhook-Feld über eine Nutzlastzeile als Template einfügen.<br><br> Beachten Sie, dass `catalog_column` ein Platzhalterwert ist. Stellen Sie sicher, dass Artikelobjekte nur Felder enthalten, die im Katalog vorhanden sind.<br><br>
4. Wählen Sie **Validate**, um eine Vorschau der Ausgabe Ihres Codes zu erhalten und zu prüfen, ob es sich um eine akzeptable Anfrage für den [Endpunkt „Mehrere Katalogartikel aktualisieren“]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) handelt.<br><br>
5. Aktivieren Sie Ihre Transformation. Wenn Sie weitere Hilfe zu Ihrem Code benötigen, bevor Sie ihn aktivieren, wenden Sie sich an Ihren Braze Account Manager.<br><br>
6. Vergewissern Sie sich, ob Ihre Quellplattform über eine Einstellung zum Senden von Webhooks verfügt. Ihr Transformationscode wird für jeden eingehenden Webhook ausgeführt, und die Katalogartikel werden aktualisiert.

Ihre Webhook-Integration ist nun abgeschlossen!

{% endtab %}
{% tab Fortgeschritten – Nutzer:innen tracken %}

In diesem Schritt transformieren Sie die Webhook-Nutzlast von der Quellplattform in einen Rückgabewert für ein JavaScript-Objekt. Dieser Rückgabewert muss dem Format des Anfragekörpers für den `/users/track`-Endpunkt entsprechen:

- Der Transformationscode wird in der Programmiersprache JavaScript akzeptiert. Jeder Standard-JavaScript-Kontrollfluss, wie z. B. die if/else-Logik, wird unterstützt.
- Der Transformationscode greift über die Variable `payload` auf den Anfragekörper des Webhooks zu. Diese Variable ist ein Objekt, das durch das Parsen des JSON-Anfragekörpers erstellt wird.
- Alle Features, die in unserem `/users/track`-Endpunkt unterstützt werden, werden unterstützt, einschließlich:
  - Nutzer:innen-Attribut-Objekte, Event-Objekte und Kauf-Objekte
  - Verschachtelte Attribute und verschachtelte Eigenschaften von angepassten Events
  - Updates für Abo-Gruppen
  - E-Mail-Adresse als Bezeichner

Wählen Sie **Validate**, um eine Vorschau der Ausgabe Ihres Codes zu erhalten und zu prüfen, ob es sich um eine akzeptable `/users/track`-Anfrage handelt.

{% alert note %}
Externe Netzwerkanfragen, Bibliotheken von Drittanbietern und Webhooks, die nicht im JSON-Format vorliegen, werden derzeit nicht unterstützt.
{% endalert %}

{% endtab %}
{% endtabs %}

## Schritt 5: Transformation überwachen {#step-5-monitor-your-transformation}

Nachdem Sie Ihre Transformation aktiviert haben, finden Sie in den Analytics auf der Hauptseite **Transformations** eine Zusammenfassung der Performance.

* **Incoming Requests:** Dies ist die Anzahl der Webhooks, die unter der URL dieser Transformation empfangen wurden. Wenn die eingehenden Anfragen 0 sind, hat Ihre Quellplattform keine Webhooks übermittelt, oder die Verbindung kann nicht hergestellt werden.
* **Deliveries:** Nach dem Empfang eingehender Anfragen wendet die Datentransformation Ihren Transformationscode an, um die Daten an das ausgewählte Braze-Ziel zu senden.

Es ist ein gutes Ziel, dass 100 % der eingehenden Anfragen zu Zustellungen führen. Die Anzahl der Zustellungen wird niemals die Anzahl der eingehenden Anfragen übersteigen.

### Fehlerbehebung {#troubleshooting}

Für eine detailliertere Überwachung und Fehlerbehebung finden Sie auf der Seite **Logs** spezifische Protokolle, in denen die letzten 1.000 eingehenden Anfragen an alle Transformationen in Ihren Workspaces protokolliert werden. Sie können jedes Protokoll auswählen, um den eingehenden Anfragekörper, die Transformationsausgabe und den Antwortkörper des Transformationsziels anzuzeigen.

Wenn es keine Zustellungen gibt, überprüfen Sie Ihren Transformationscode auf Syntaxfehler und stellen Sie sicher, dass der Code kompiliert werden kann. Prüfen Sie dann, ob die Ausgabe eine gültige Zielanfrage ist.

Zustellungen, die geringer sind als die Anzahl der eingehenden Anfragen, zeigen an, dass zumindest einige Webhooks erfolgreich zugestellt wurden. Schauen Sie in den Transformationsprotokollen nach Beispielfehlern und prüfen Sie, ob die Transformationsausgabe den Erwartungen entspricht. Es ist möglich, dass Ihr Transformationscode nicht alle Varianten der empfangenen Webhooks berücksichtigt.