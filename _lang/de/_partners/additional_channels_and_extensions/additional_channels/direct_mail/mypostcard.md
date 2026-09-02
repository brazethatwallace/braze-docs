---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und MyPostcard, die es Ihnen ermöglicht, Direkt-Mailing als zusätzlichen Kanal für Ihren CRM or Customer-Relationship-Management [-System] (CRM)-Workflow zu nutzen."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard](https://www.mypostcard.com), eine weltweit führende App für Postkarten, ermöglicht es Ihnen, Direkt-Mailing-Kampagnen mit Leichtigkeit durchzuführen und bietet eine nahtlose und gewinnbringende Möglichkeit, mit Ihren Kund:innen in Kontakt zu treten.

Nutzen Sie die Integration von MyPostcard und Braze, um Ihren Kund:innen mühelos Print-Mailings zu senden.

## Voraussetzungen {#prerequisites}

| Anforderung                      | Beschreibung                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| MyPostcard B2B-Konto           | Um die Vorteile dieser Integration zu nutzen, müssen Sie sich bei MyPostcard Registrierung or registrieren.                                          |
| B2B-API-Schlüssel und Zugangsdaten        | Sie finden Ihren API-Schlüssel und die Zugangsdaten im MyPostcard B2B Admin Tool.                                         |
| Genehmigte MyPostcard B2B-Kampagne | Um die Vorteile dieser Integration zu nutzen, müssen Sie eine Print-Mailing-Kampagne im MyPostcard B2B-Tool einrichten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Anwendungsfälle {#use-cases}

Um Ihre Direkt-Mailing-Kampagnen aufzuwerten, ist es entscheidend, über traditionelle Massenmailings hinauszugehen und Print-Mailings nahtlos in Ihre Workflows zu integrieren. Auf diese Weise können Sie gezielt Kund:innen erreichen, die sich von Ihren E-Mail-Newslettern abgemeldet haben oder deren E-Mails als Spam markiert sind. Mit MyPostcard können Sie mühelos Print-Mailing-Kampagnen direkt über Braze versenden.

- Erstellen Sie in Braze intuitive Workflows, die Print-Mailings als leistungsstarken neuen Kanal einbeziehen – ganz ohne technisches Know-how.
- Erschließen Sie das Potenzial personalisierter Print-Mailings mit wenigen einfachen Schritten.
- Profitieren Sie von einer unkomplizierten Implementierung, die durch personalisierten Support eines engagierten Teams unterstützt wird.

## Integration

Um MyPostcard zu integrieren, [melden Sie sich an oder Registrierung or registrieren Sie sich](https://www.mypostcard.com/b2b/admin/) und erstellen Sie Ihre erste Kampagne, um sie über [Braze-Webhooks]({{site.baseurl}}/user_guide/channels/webhooks/) zu nutzen.

### 1. Schritt: Erstellen Sie Ihr Braze-Webhook-Template {#step-1-create-your-braze-webhook-template}

Um ein MyPostcard-Webhook-Template zur Verwendung in zukünftigen Campaigns oder Canvase zu erstellen, navigieren Sie auf der Braze-Plattform zu **Content** > **Webhook**. Wählen Sie dann **Create webhook template** aus.

Wenn Sie eine einmalige MyPostcard-Webhook-Campaign erstellen oder ein vorhandenes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Campaign **Webhook** in Braze aus. Füllen Sie die folgenden Felder aus:

| Feld         | Beschreibung                                               |
|---------------|-----------------------------------------------------------|
| **Webhook URL** | Die Webhook-URL, wie sie im B2B Admin Tool angezeigt wird.             |
| **Request Body** | Rohtext (JSON-Format, zu finden im B2B Admin Tool).        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Create your Braze webhook template" }

#### Anfragemethode und Header {#request-method-and-headers}

MyPostcard erfordert eine HTTP-Methode zusammen mit den folgenden HTTP-Headern, die in das Template aufgenommen werden müssen.

{% raw %}
<table aria-label="Request method and headers">
  <caption>Anfragemethode und Header</caption>
  <thead>
    <tr>
      <th><strong>Feld</strong></th>
      <th><strong>Details</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>HTTP-Methode</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Username</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Passwort</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Content-Type</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 aria-label="Request method and headers" }

#### Anfragetext {#request-body}

Kopieren Sie den Anfragetext, der im B2B Admin Tool angezeigt wird, und füllen Sie die Platzhalter mit Inhalten aus, indem Sie beliebige Liquid-Personalisierungs-Tags verwenden.

![Tab „Verfassen“ mit dem JSON-Body und den Webhook-Informationen.]({% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %})

### 2. Schritt: Vorschau Ihrer Anfrage {#step-2-preview-your-request}

Sehen Sie sich als Nächstes eine Vorschau Ihrer Anfrage im Panel **Vorschau** an oder wechseln Sie zum Tab **Test**, wo Sie eine:n zufällige:n Nutzer:in, eine:n bestehende:n Nutzer:in oder eine:n angepasste:n Nutzer:in auswählen können, um Ihren Webhook zu testen. Vergessen Sie nicht, Ihr Template zu speichern, bevor Sie die Seite verlassen!

![Tab „Webhook testen“ mit verschiedenen Feldern zur Validierung der Implementierung.]({% image_buster /assets/img/mypostcard/mypostcard_test.jpg %})

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/) erstellen.
{% endalert %}