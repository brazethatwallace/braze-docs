---
nav_title: API-Kampagnen
article_title: API-Kampagnen
page_order: 5
description: "Dieser Referenzartikel beschreibt, wie Sie eine campaign_id generieren, die Sie in Ihre API-Aufrufe einbinden können, und wie Sie diese Kampagne konfigurieren."
page_type: reference
tool: Campaigns
---

# API-Kampagnen {#api-campaigns}

> Dieser Referenzartikel beschreibt, wie Sie eine `campaign_id` generieren, die Sie in Ihre API-Aufrufe einbinden können, und wie Sie diese Kampagne konfigurieren.

API-Kampagnen werden in der Regel für transaktionsbezogene Nachrichten verwendet. Bei der Erstellung von API-Kampagnen (nicht [API-getriggerten Kampagnen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)) wird das Braze-Dashboard nur verwendet, um eine `campaign_id` zu generieren, mit der Sie Analytics für die Kampagnenberichterstattung verfolgen können. Sie können auch eine Nachrichtenvarianten-ID generieren, die für jede Variante Ihrer Kampagne unterschiedlich ist.

Diese Informationen senden Sie dann an Ihr Entwicklungsteam, um sie in der API-Anfrage zu verwenden, zusammen mit:
- Texte für die Kampagne
- Zielgruppenzugehörigkeit
- Assets

Nachdem die Kampagne begonnen hat, können Sie die Ergebnisse im Dashboard einsehen. API-Kampagnen verwenden die [Messaging-APIs]({{site.baseurl}}/api/endpoints/messaging) von Braze, die über die gleichen detaillierten Berichts- und Retargeting-Optionen verfügen wie Kampagnen, die vollständig über das Dashboard erstellt wurden.

{% alert warning %}
Da API-Kampagnen in der Regel transaktionsbezogen sind, kommen alle Nutzer:innen für API-Kampagnen in Frage, auch diejenigen in Ihrer globalen Kontrollgruppe. Eine [Ein-Klick-Listenabmeldung]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#list-unsubscribe)-Kopfzeile wird diesen Sendungen standardmäßig nicht hinzugefügt. Informationen zum Hinzufügen einer Ein-Klick-Listenabmeldung-Kopfzeile zu einer API-Kampagne finden Sie unter [Ein-Klick-Listenabmeldung zu API-Kampagnen hinzufügen](#add-one-click-list-unsubscribe-to-api-campaigns). Wenn Sie allen API-Kampagnen eine Ein-Klick-Listenabmeldung-Kopfzeile hinzufügen möchten, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Neue Kampagne erstellen {#create-a-new-campaign}

Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign** aus. Wählen Sie dann **API Campaigns** aus. Jetzt können Sie mit der Konfiguration Ihrer API-Kampagne fortfahren.

Eine [API-getriggerte Kampagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) unterscheidet sich von einer API-Kampagne.

## Ihre Kampagne konfigurieren {#configure-your-campaign}

Um Ihre Kampagne zu konfigurieren, führen Sie die folgenden Schritte aus:

1. Fügen Sie einen aussagekräftigen Titel hinzu, damit Sie die Ergebnisse auf der Campaigns-Seite finden können, nachdem Sie Ihre Nachrichten gesendet haben.
2. Wählen Sie **Add Message** und fügen Sie die Nachrichtentypen hinzu, die in Ihrer API-Kampagne enthalten sind. Dadurch können Sie eine `campaign_id` und eine Nachrichtenvarianten-ID generieren, die sich für jeden enthaltenen Kanal unterscheidet.
3. Optional können Sie ein Konversions-Event hinzufügen, um Konversionen von Nutzer:innen für eine bestimmte Aktion oder ein Kampagnenziel zu verfolgen.
4. Wählen Sie **Save Campaign**, um Ihre API-Kampagne zu starten.

## API-Aufrufe {#api-calls}

Nachdem Sie Ihre API-Kampagne gespeichert haben, fügen Sie Folgendes in Ihre API-Anfrage ein:

- Die generierten `campaign_id`-Felder in Ihrer API-Anfrage, wie in den [Endpunkten zum Senden von Nachrichten]({{site.baseurl}}/api/endpoints/messaging) angegeben.
- Ein [Nachrichtenobjekt]({{site.baseurl}}/api/objects_filters#messaging-objects) für jede in der Kampagne enthaltene Plattform. Geben Sie im Nachrichtenobjekt die ID der Nachrichtenvariante an. Dadurch wird festgelegt, dass Statistiken unter dieser Variante erfasst und angezeigt werden. Die folgenden Nachrichtenobjekte werden unterstützt: Android, Content Cards, E-Mail, iOS, Kindle, SMS/MMS, Web-Push und Webhook.

## Ein-Klick-Listenabmeldung zu API-Kampagnen hinzufügen {#add-one-click-list-unsubscribe-to-api-campaigns}

{% raw %}
Standardmäßig fügt Braze die Ein-Klick-Listenabmeldung-Kopfzeile nicht zu API-Kampagnen hinzu. Sie können diese Kopfzeile zu einzelnen API-Kampagnensendungen hinzufügen, indem Sie den Liquid-Tag `{{${set_user_to_one_click_list_unsubscribe}}}` im E-Mail-Header-Feld Ihrer API-Anfrage einfügen.
{% endraw %}

Um [RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058) für die Ein-Klick-Listenabmeldung einzuhalten, fügen Sie sowohl den `List-Unsubscribe`- als auch den `List-Unsubscribe-Post`-Header in Ihre API-Anfrage ein:

{% raw %}
```json
{
  "external_user_ids": ["user_id"],
  "messages": {
    "email": {
      "app_id": "your_app_id",
      "subject": "Your Subject",
      "from": "Sender Name <sender@example.com>",
      "body": "<p>Email body content</p>",
      "headers": {
        "List-Unsubscribe": "<{{${set_user_to_one_click_list_unsubscribe}}}>",
        "List-Unsubscribe-Post": "List-Unsubscribe=One-Click"
      }
    }
  }
}
```
{% endraw %}

{% alert note %}
Das Einfügen dieser Header garantiert nicht, dass der E-Mail-Client eine Abmelde-Schaltfläche anzeigt. E-Mail-Clients entscheiden anhand von Faktoren wie Absender-Reputation und Nachrichteninhalt, ob die Abmeldeoption angezeigt wird.
{% endalert %}

### E-Mail-Anhänge hinzufügen {#add-email-attachments}

Um Anhänge zu API-Kampagnen-E-Mails hinzuzufügen, fügen Sie ein `attachments`-Array in das [E-Mail-Objekt]({{site.baseurl}}/api/objects_filters/messaging/email_object) ein. Sie können ein E-Mail-Template referenzieren, das im Drag-and-Drop- oder HTML-Editor erstellt wurde, indem Sie dessen `email_template_id` im E-Mail-Objekt angeben und dann Anhänge über den API-Aufruf hinzufügen.

Einzelheiten zu Anhängen, Größenbeschränkungen und Best Practices finden Sie unter [Beispiel für ein E-Mail-Objekt mit Anhang]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment).