---
nav_title: Zendesk
article_title: Zendesk
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Zendesk, einer beliebten Support-Suite, die es Ihnen ermöglicht, Braze-Webhooks zu verwenden, um Support-Daten zwischen den beiden Plattformen zu synchronisieren."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> Die [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS) bietet Unternehmen die Möglichkeit, über Omnichannel-Support per E-Mail, Webchat, Voice oder Social-Messaging-Apps natürliche Konversationen mit ihren Kund:innen zu führen. Zendesk bietet ein optimiertes Ticketing-System, das Wert auf Tracking und Priorisierung von Interaktionen legt und es Unternehmen ermöglicht, eine einheitliche historische Übersicht über ihre Kund:innen zu erhalten.

Die Server-zu-Server-Integration von Braze und Zendesk ermöglicht Ihnen die Nutzung von:
- Braze-Webhooks zur Automatisierung der Erstellung von Support-Tickets in Zendesk aufgrund von Nachrichten-Engagement in Nutzer-Journeys in Braze. Nachdem Sie beispielsweise eine Integration erfolgreich implementiert und getestet haben, kann Braze ein Support-Ticket erstellen, wenn Nutzer:innen eine In-App-Nachricht mit der Frage „Gefällt Ihnen unsere App?“ negativ beantworten, sodass Ihr Support-Team mit den Kund:innen nachfassen kann.
- Zendesk-Webhooks zur Unterstützung bidirektionaler Anwendungsfälle wie dem Update des Nutzerprofils in Braze aufgrund einer Aktivität in Zendesk. Wenn zum Beispiel ein Ticket gelöst wurde, protokollieren Sie ein Ereignis im Kundenprofil in Braze.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Zendesk-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Zendesk-Administratorkonto](https://`<your-zendesk-instance>`.zendesk.com/agent/admin). |
| Zendesk-API-Token | Ein Zendesk-[API-Token](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\) ist erforderlich, um Anfragen von Braze an den Zendesk-Ticket-Endpunkt zu senden. |
| Gemeinsamer Bezeichner (empfohlen) | Ein [gemeinsamer Bezeichner](#common-identifier) zwischen Braze und Zendesk wird empfohlen. |
| Braze-API-Schlüssel | Ein Braze-API-Schlüssel ist erforderlich, um Anfragen von Zendesk an einen Braze-Endpunkt zu senden. Vergewissern Sie sich, dass der von Ihnen verwendete API-Schlüssel die richtigen Berechtigungen für den Braze-Endpunkt hat, den Ihr Zendesk-Webhook verwendet. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration von Braze zu Zendesk {#braze-to-zendesk-integration}

### Schritt 1: Erstellen Sie Ihren Braze-Webhook {#step-1-create-your-braze-webhook}

So erstellen Sie einen Webhook:

- **Campaigns:** Gehen Sie im Braze-Dashboard auf die Seite **Campaigns**. Klicken Sie auf **Create Campaign** und wählen Sie **Webhook**.
- **Canvas:** Erstellen Sie in einem neuen oder bestehenden Canvas einen vollständigen Schritt oder einen Nachrichten-Schritt im Canvas-Builder. Klicken Sie dann auf **Messages** und wählen Sie **Webhook** aus den Nachrichtenoptionen.

Füllen Sie in Ihrem Webhook die folgenden Felder aus:
- **Webhook-URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **Anfragetext**: Rohtext

Weitere Anwendungsfälle können über die [Zendesk-Support-APIs](https://developer.zendesk.com/rest_api/docs/support/introduction) gehandhabt werden, wodurch der `/api/v2/`-Endpunkt am Ende der Webhook-URL entsprechend geändert wird.

#### Anfrage-Header und Methode {#request-header-and-method}

Zendesk benötigt einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Ersetzen Sie im Tab **Settings** <email_address> durch Ihre Zendesk-Admin-E-Mail und <api_token> durch Ihr Zendesk-API-Token.

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Authorization**: Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Braze-Webhook-Einstellungen mit Zendesk-Autorisierungs-Header und konfigurierter POST-Methode.]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### Anfragetext {#request-body}

Definieren Sie die Ticketdetails wie Typ, Betreff und Status in Ihrem Webhook-Payload. Die Ticketdetails sind erweiterbar und werden auf der Grundlage der [Zendesk-Ticket-API](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket) angepasst. Verwenden Sie das folgende Beispiel, um Ihren Payload zu strukturieren und die gewünschten Felder einzugeben.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}",
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### Schritt 2: Vorschau Ihrer Anfrage {#step-2-preview-your-request}

Ihr Rohtext wird automatisch hervorgehoben, wenn es sich um einen passenden Braze-Tag handelt.

Eine Vorschau Ihrer Anfrage finden Sie im Panel **Preview**. Alternativ können Sie zum Tab **Test** navigieren, wo Sie zufällige Nutzer:innen, bereits vorhandene Nutzer:innen oder eine eigene Konfiguration auswählen können, um Ihren Webhook zu testen.

Prüfen Sie abschließend, ob das Ticket auf der Zendesk-Seite erstellt wurde.

## Gemeinsamer Bezeichner {#common-identifier}

Wenn Sie einen gemeinsamen Bezeichner für Braze und Zendesk haben, empfiehlt es sich, diesen als `requester_id` zu verwenden. Dies hilft dabei, die beiden Gruppen von Nutzer:innen zu vereinheitlichen. Sollte dies nicht der Fall sein, empfehlen wir, eine Reihe von identifizierenden Attributen wie Name, E-Mail-Adresse, Telefonnummer oder andere zu übergeben.

## Integration von Zendesk zu Braze {#zendesk-to-braze-integration}

### Schritt 1: Einen Webhook erstellen {#step-1-create-a-webhook}

1. Klicken Sie im [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb) in der Seitenleiste auf **Apps and integrations** und wählen Sie dann **Webhooks > Webhooks**.<br><br>
2. Klicken Sie auf **Create webhook**.<br><br>
3. Wählen Sie **Trigger** oder **Automation** und klicken Sie auf **Next**.<br>![Zendesk-Webhook-Erstellungsbildschirm mit Trigger- und Automatisierungsoptionen.]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. Geben Sie in Ihrem Webhook die folgenden Informationen an:
- Geben Sie einen Namen und eine Beschreibung für den Webhook ein.
- Geben Sie die URL des Braze-Endpunkts ein, den Ihr Webhook verwenden soll. {% raw %}Unser Beispiel verwendet `https://{{instance_url}}/users/track`.{% endraw %}
- Wählen Sie POST als Anfragemethode des Webhooks und setzen Sie das Anfrageformat auf JSON.
- Wählen Sie die Bearer-Token-Authentifizierungsmethode für den Webhook und geben Sie Ihren [Braze-API-Schlüssel]({{site.baseurl}}/api/basics#creating-rest-api-keys) an.
  - Vergewissern Sie sich, dass der API-Schlüssel, den Sie verwenden, die [richtigen Berechtigungen]({{site.baseurl}}/api/basics#rest-api-key-permissions) für den Braze-Endpunkt hat, den Ihr Webhook verwendet.<br><br>
5. (Empfohlen) Testen Sie den Webhook, um zu überprüfen, ob er ordnungsgemäß funktioniert.<br><br>
6. Bei Trigger- und Automatisierungs-Webhooks müssen Sie den Webhook mit einem Trigger oder einer Automatisierung verbinden, bevor Sie die Einrichtung abschließen. Im folgenden Schritt finden Sie ein Beispiel für die Erstellung eines Triggers für den Webhook. Nachdem der Trigger erstellt wurde, können Sie zu dieser Seite zurückkehren und **Finish setup** auswählen.

### Schritt 2: Einen Trigger oder eine Automatisierung erstellen {#step-2-create-a-trigger-or-automation}

[Folgen Sie den Anweisungen von Zendesk](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb), um Ihren Webhook mit einem Trigger oder einer Automatisierung zu verbinden.

In unserem Beispiel unten wird ein Trigger verwendet, um den Webhook aufzurufen, wenn der Status eines Supportfalls auf „Gelöst“ oder „Geschlossen“ geändert wurde.

1. Klicken Sie im **Admin Center** in der Seitenleiste auf **Objects and rules** und wählen Sie dann **Business rules > Triggers**.<br><br>
2. Wählen Sie **Add trigger**.<br><br>
3. Benennen Sie Ihren Trigger und wählen Sie eine Kategorie aus.<br><br>
4. Wählen Sie **Add condition**, um festzulegen, welche Bedingungen den Webhook auslösen sollen. Zum Beispiel: „Status category changed to closed“ oder „Status category changed to solved“.![Zendesk-Trigger-Bedingungseditor mit Statuskategorie-Bedingungen.]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. Wählen Sie **Add action**, wählen Sie **Notify active webhook** und wählen Sie aus dem Dropdown den Webhook aus, den Sie im vorherigen Schritt erstellt haben.<br><br>
6. Definieren Sie den JSON-Body so, dass er Ihrem Braze-Endpunkt entspricht, und verwenden Sie variable Platzhalter von Zendesk, um die relevanten Felder dynamisch zu füllen.<br>![Zendesk-Webhook-Aktions-Payload-Editor mit JSON-Body-Variablen.]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. Wählen Sie **Create**.<br><br>
8. Kehren Sie zu Ihrem Webhook zurück und klicken Sie auf **Finish setup**.