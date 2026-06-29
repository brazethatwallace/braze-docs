---
nav_title: Webhook-Templates
article_title: Webhook-Templates
page_order: 5
tool:
  - Templates
channel:
  - webhooks
description: "Erfahren Sie, wie Sie Webhook-Templates erstellen und anpassen, um sie später in der Braze-Plattform wiederzuverwenden."

---

# Ein Webhook-Template erstellen {#create-a-webhook-template}

> Wenn Sie Ihre Webhooks erstellen und anpassen, können Sie Webhook-Templates für die spätere Verwendung in der Braze-Plattform erstellen und nutzen. So können Sie konsistent eine Vielzahl von Webhooks für Ihre verschiedenen Campaigns erstellen.

## 1. Schritt: Zum Webhook-Template-Editor navigieren {#step-1-go-to-the-webhook-template-editor}

Gehen Sie im Braze-Dashboard zu **Inhalt** > **Webhook**.

![Die Seite „Webhook-Templates“ mit vorgefertigten und gespeicherten Webhook-Templates.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## 2. Schritt: Template auswählen {#step-2-choose-your-template}

Hier können Sie ein neues Template erstellen, eines der vorgefertigten Webhook-Templates verwenden oder ein bestehendes Template bearbeiten.

Wenn Sie beispielsweise [LINE]({{site.baseurl}}/user_guide/channels/line/) als Messaging-Kanal verwenden, können Sie mithilfe der vorgefertigten Templates für **LINE Carousel** oder **LINE Image** mehrere Webhooks einrichten.

## 3. Schritt: Template-Details ausfüllen {#step-3-fill-out-template-details}

1. Geben Sie Ihrem Webhook-Template einen eindeutigen Namen.
2. (Optional) Fügen Sie eine Template-Beschreibung hinzu, die erklärt, wie dieses Template verwendet werden soll.
3. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) und [Tags]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/) hinzu, um Ihr Template leichter finden und filtern zu können.

## 4. Schritt: Template erstellen {#step-4-build-your-template}

1. Geben Sie die Webhook-URL ein.
2. Wählen Sie die HTTP-Methode aus.
3. Fügen Sie einen Anfrage-Body hinzu. Dieser kann entweder aus **JSON Key/Value Pairs** oder **Raw Text** bestehen.
4. (Optional) Fügen Sie einen Anfrage-Header hinzu. Dieser kann je nach Webhook-Ziel erforderlich sein.

![Der Tab „Verfassen“ beim Erstellen eines Webhook-Templates. Verfügbare Felder sind Webhook-URL, HTTP-Methode, Anfrage-Body und Anfrage-Header. Sie können auch Sprachen hinzufügen.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## 5. Schritt: Template testen {#step-5-test-your-template}

Um zu sehen, wie Ihr Webhook aussieht, bevor Sie ihn an Ihre Nutzer:innen senden, können Sie über den Tab **Test** einen Test-Webhook senden. Hier können Sie auswählen, ob Sie die Nachricht als zufällige:r Nutzer:in, bestehende:r Nutzer:in oder benutzerdefinierte:r Nutzer:in in der Vorschau anzeigen möchten.

## 6. Schritt: Template speichern {#step-6-save-your-template}

Speichern Sie Ihr Template, indem Sie **Save Template** auswählen. Jetzt können Sie dieses Template in jeder beliebigen Campaign verwenden.

{% alert note %}
Änderungen an einem bestehenden Template werden nicht in Campaigns übernommen, die mit früheren Versionen dieses Templates erstellt wurden.
{% endalert %}

## Ihre Templates verwalten {#managing-your-templates}

Sie können Webhook-Templates [duplizieren und archivieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates/), um Ihre Liste von Templates besser zu organisieren und zu verwalten.