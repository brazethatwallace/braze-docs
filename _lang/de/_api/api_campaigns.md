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

Nachdem die Kampagne begonnen hat, können Sie die Ergebnisse im Dashboard einsehen. API-Kampagnen verwenden die Braze [Messaging-APIs]({{site.baseurl}}/api/endpoints/messaging), die über die gleichen detaillierten Berichts- und Retargeting-Optionen verfügen wie Kampagnen, die vollständig über das Dashboard erstellt wurden.

Da API-Kampagnen immer eine `campaign_id` enthalten, werden ihre Sendungen in den Dashboard-Statistiken berücksichtigt. Wenn Sie [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) ohne eine `campaign_id` aufrufen, erhöht Braze diese Metriken nicht – die Sendungen erscheinen weiterhin im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), aber nicht in den E-Mail-Performance-Metriken im Dashboard.

{% alert warning %}
Da API-Kampagnen in der Regel transaktionsbezogen sind, kommen alle Nutzer:innen für API-Kampagnen in Frage, auch diejenigen in Ihrer globalen Kontrollgruppe. Eine [Ein-Klick-Listenabmeldung]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences)-Kopfzeile wird diesen Sendungen standardmäßig nicht hinzugefügt. Informationen zum Hinzufügen einer Ein-Klick-Listenabmeldung-Kopfzeile zu einer API-Kampagne finden Sie unter [Ein-Klick-Listenabmeldung zu API-Kampagnen hinzufügen](#add-one-click-list-unsubscribe-to-api-campaigns). Wenn Sie allen API-Kampagnen eine Ein-Klick-Listenabmeldung-Kopfzeile hinzufügen möchten, wenden Sie sich an Ihren CSM or Customer-Success-Manager or Customer-Success-Manager:in.
{% endalert %}

## Neue Campaign erstellen {#create-a-new-campaign}

Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign** aus. Wählen Sie dann **API Campaigns**. Nun können Sie mit der Konfiguration Ihrer API-Campaign fortfahren.

Eine [API-getriggerte Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) unterscheidet sich von einer API-Campaign.

## Konfigurieren Sie Ihre Campaign {#configure-your-campaign}

Um Ihre Campaign zu konfigurieren, führen Sie die folgenden Schritte aus:

1. Fügen Sie einen aussagekräftigen Titel hinzu, damit Sie die Ergebnisse auf der Campaigns-Seite finden können, nachdem Sie Ihre Nachrichten gesendet haben.
2. Wählen Sie **Nachricht hinzufügen** und fügen Sie die Nachrichtentypen hinzu, die in Ihrer API-Campaign enthalten sind. So können Sie eine `campaign_id` und eine Nachrichtenvarianten-ID generieren, die sich für jeden enthaltenen Kanal unterscheidet.
3. Optional können Sie ein Konversions-Event hinzufügen, um Konversionen von Nutzer:innen bei einer bestimmten Aktion oder einem Campaign-Ziel zu verfolgen.
4. Wählen Sie **Campaign speichern**, um Ihre API-Campaign zu starten.

## API-Aufrufe {#api-calls}

Nachdem Sie Ihre API-Campaign gespeichert haben, fügen Sie Folgendes in Ihre API-Anfrage ein:

- Die generierten `campaign_id`-Felder in Ihrer API-Anfrage an den entsprechenden Stellen in den [Endpunkten zum Senden von Nachrichten]({{site.baseurl}}/api/endpoints/messaging).
- Ein [Nachrichtenobjekt]({{site.baseurl}}/api/objects_filters#messaging-objects) für jede in der Campaign enthaltene Plattform. Geben Sie im Nachrichtenobjekt die ID der Nachrichtenvariante an. Dadurch wird festgelegt, dass Statistiken unter dieser Variante erfasst und angezeigt werden. Die folgenden Nachrichtenobjekte werden unterstützt: Android, Content Cards, E-Mail, iOS, Kindle, Kurzmitteilungsdienst or SMS/MMS, Web-Push und Webhook.

## Ein-Klick-Abmeldung per Liste zu API-Campaigns hinzufügen {#add-one-click-list-unsubscribe-to-api-campaigns}

{% raw %}
Standardmäßig fügt Braze den Header für die Ein-Klick-Abmeldung per Liste nicht zu API-Campaigns hinzu. Sie können diesen Header zu einzelnen API-Campaign-Sends hinzufügen, indem Sie das Liquid-Tag `{{${set_user_to_one_click_list_unsubscribe}}}` im E-Mail-Header-Feld Ihrer API-Anfrage einfügen.
{% endraw %}

Um [RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058) für die Ein-Klick-Abmeldung per Liste einzuhalten, fügen Sie sowohl den `List-Unsubscribe`- als auch den `List-Unsubscribe-Post`-Header in Ihre API-Anfrage ein:

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
Das Einfügen dieser Header garantiert nicht, dass der E-Mail-Client einen Abmelde-Button anzeigt. E-Mail-Clients entscheiden anhand von Faktoren wie Absender-Reputation und Nachrichteninhalt, ob die Abmeldeoption angezeigt wird.
{% endalert %}

### E-Mail-Anhänge hinzufügen {#add-email-attachments}

Um Anhänge zu API-Campaign-E-Mails hinzuzufügen, fügen Sie ein `attachments`-Array in das [E-Mail-Objekt]({{site.baseurl}}/api/objects_filters/messaging/email_object) ein. Sie können ein E-Mail-Template referenzieren, das im Drag-and-Drop- oder HTML-Editor erstellt wurde, indem Sie dessen `email_template_id` im E-Mail-Objekt angeben und dann Anhänge über den API-Aufruf hinzufügen.

Für Details zu Anhängen, Größenbeschränkungen und Best Practices siehe [Beispiel eines E-Mail-Objekts mit Anhang]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment).