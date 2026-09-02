---
nav_title: Postman und Beispielanfragen
article_title: Postman und Beispielanfragen
page_order: 3
description: "Dieser Referenzartikel behandelt die Braze Postman Collection, was sie ist, wie Sie die Collection einrichten und verwenden und wie Sie Anfragen bearbeiten und versenden können."
page_type: reference
---

# Postman und Beispielanfragen {#postman-and-sample-requests}

> Braze ermöglicht es Ihnen, über unsere Postman Collection Beispiel-API-Anfragen für alle unsere Endpunkte zu generieren. Dieser Referenzartikel behandelt die Braze Postman Collection, was sie ist, wie Sie die Collection einrichten und verwenden und wie Sie Anfragen bearbeiten und versenden können.

## Was ist Postman? {#what-is-postman}

Postman ist ein kostenloses visuelles Bearbeitungstool zum Erstellen und Testen von API-Anfragen. Im Vergleich zu anderen Methoden (z. B. der Verwendung von cURL) können Sie mit Postman API-Anfragen bearbeiten, Header-Informationen anzeigen und vieles mehr. Sie können Collections (Bibliotheken mit vorgefertigten API-Beispielanfragen) speichern. Um die Einrichtung mit unserer Representational State Transfer API zu beschleunigen, stellen wir eine Collection mit vorgefertigten Beispielen für alle Endpunkte bereit.

Sehen Sie sich unsere Postman Collection an oder laden Sie sie herunter, indem Sie in unserer [Postman-Dokumentation](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) auf **Run in Postman** klicken.

## Die Braze Postman-Sammlung verwenden {#using-the-braze-postman-collection}

Wenn Sie ein Postman-Konto haben (Sie können macOS-, Windows- und Linux-Versionen von der [Postman-Website](https://www.getpostman.com) herunterladen), können Sie unsere Postman-Dokumentation in Ihrer eigenen Postman-App öffnen, indem Sie auf den orangefarbenen Button **Run in Postman** klicken. Sie können dann [eine Umgebung erstellen](#setting-up-your-postman-environment) oder unsere Braze Representational State Transfer API-Umgebung als Template verwenden und die verfügbaren `POST`- und `GET`-Anfragen an Ihre eigenen Bedürfnisse anpassen.

### Ihre Postman-Umgebung einrichten {#setting-up-your-postman-environment}

{% raw %}
Die Braze Postman-Sammlung verwendet eine Template-Variable `{{instance_url}}`, um die Representational State Transfer-API-URL Ihrer Braze-Instanz in die vorgefertigten Anfragen einzusetzen, und die Variable `{{api_key}}` für Ihren API-Schlüssel. Anstatt alle Anfragen in der Sammlung manuell bearbeiten zu müssen, können Sie diese Variable in Ihrer Postman-Umgebung einrichten. Sie können entweder unsere vorbereitete Umgebung (Braze Representational State Transfer API Environment Template) aus dem Dropdown-Menü auswählen und die Variablenwerte durch Ihre eigenen ersetzen, oder Sie können Ihre eigene Umgebung einrichten.
{% endraw %}

Um Ihre eigene Umgebung einzurichten, führen Sie die folgenden Schritte aus:

1. Wählen Sie im Tab **Workspaces** die Option **Environments** aus.
2. Klicken Sie auf den **+**-Plus-Button, um eine neue Umgebung zu erstellen.
3. Geben Sie dieser Umgebung einen Namen (zum Beispiel „Braze API Requests“) und fügen Sie Schlüssel für `instance_url` und `api_key` mit Werten hinzu, die Ihrer [Braze-Instanz]({{site.baseurl}}/api/basics) und Ihrem [Braze Representational State Transfer-API-Schlüssel]({{site.baseurl}}/api/basics) entsprechen.
4. Klicken Sie auf **Save**.

{% alert note %}
In `POST`-Anfragekörpern sollte der `api_key` in Anführungszeichen eingeschlossen sein: `"MY-API-KEY-EXAMPLE"`. In `GET`-URLs sollte dies nicht der Fall sein. Wir haben diese Formatierung bereits in den `POST`-Anfragekörpern, `GET`-URLs und dem Umgebungstemplate für `YOUR-API-KEY-HERE` in dieser Dokumentation für Sie bereitgestellt.
{% endalert %}

![Hinzufügen von Variablen für API-Schlüssel und Instanz-URL zur Braze Representational State Transfer API-Umgebung in Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Die vorgefertigten Anfragen aus der Sammlung verwenden {#using-the-pre-built-requests-from-the-collection}

Nachdem Sie Ihre Umgebung konfiguriert haben, können Sie jede der vorgefertigten Anfragen in der Sammlung als Template zum Erstellen neuer API-Anfragen verwenden. Um eine der vorgefertigten Anfragen zu verwenden, klicken Sie im Menü **Collections** von Postman darauf. Dadurch wird die Anfrage als neuer Tab im Hauptfenster der Postman-App geöffnet.

Im Allgemeinen gibt es zwei Arten von Anfragen, die Braze-API-Endpunkte akzeptieren – `GET` und `POST`. Je nachdem, welche `HTTP`-Methode der Endpunkt verwendet, müssen Sie die vorgefertigte Anfrage unterschiedlich bearbeiten.

#### Eine POST-Anfrage bearbeiten {#edit-a-post-request}

Wenn Sie eine `POST`-Anfrage bearbeiten, öffnen Sie die Anfrage und navigieren Sie zum Abschnitt **Body** im Anfrage-Editor. Wählen Sie für eine bessere Lesbarkeit den Radio-Button **raw** aus, um den `JSON`-Anfragekörper zu formatieren.

![Tab „Body“ beim Bearbeiten einer POST-User-Track-Anfrage in Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Eine GET-Anfrage bearbeiten {#edit-a-get-request}

Wenn Sie eine `GET`-Anfrage bearbeiten, bearbeiten Sie die in der Anfrage-URL übergebenen Parameter. Wählen Sie dazu den Tab **Params** aus und bearbeiten Sie die Schlüssel-Wert-Paare in den angezeigten Feldern.

![Tab „Params“ beim Bearbeiten einer GET-Anfrage zur Abfrage einer Liste abgemeldeter E-Mail-Adressen in Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Ihre Anfrage senden {#send-your-request}

Wenn Ihre API-Anfrage bereit ist, klicken Sie auf **Send**. Die Anfrage wird gesendet und die Antwortdaten werden in einem Bereich unterhalb des Anfrage-Editors angezeigt. Von hier aus können Sie die von der Braze-API zurückgegebenen Rohdaten einsehen, den HTTP-Antwortcode anzeigen, die Verarbeitungsdauer der Anfrage sehen und Header-Informationen anzeigen.

![Beispiel für Antwortdaten einer POST-Anfrage mit dem Status 201 Created und einer Antwortzeit von 269 Millisekunden.]({% image_buster /assets/img_archive/postman_response.png %})