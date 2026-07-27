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
Da API-Kampagnen in der Regel transaktionsbezogen sind, kommen alle Nutzer:innen für API-Kampagnen in Frage, auch diejenigen in Ihrer globalen Kontrollgruppe. Eine [Ein-Klick-Listenabmeldung]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings#list-unsubscribe)-Kopfzeile wird diesen Sendungen nicht hinzugefügt. Wenn Sie allen API-Kampagnen eine Ein-Klick-Listenabmeldung-Kopfzeile hinzufügen möchten, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Neue Campaign erstellen {#create-a-new-campaign}

Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign** aus. Wählen Sie dann **API Campaigns** aus. Jetzt können Sie mit der Konfiguration Ihrer API-Campaign fortfahren.

Eine [API-getriggerte Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) unterscheidet sich von einer API-Campaign.

## Konfigurieren Sie Ihre Campaign {#configure-your-campaign}

Um Ihre Campaign zu konfigurieren, führen Sie die folgenden Schritte aus:

1. Fügen Sie einen aussagekräftigen Titel hinzu, damit Sie die Ergebnisse auf der Campaigns-Seite finden können, nachdem Sie Ihre Nachrichten gesendet haben.
2. Wählen Sie **Nachricht hinzufügen** und fügen Sie die Nachrichtentypen hinzu, die in Ihrer API-Campaign enthalten sind. Dadurch können Sie eine `campaign_id` und eine Nachrichtenvarianten-ID generieren, die sich für jeden enthaltenen Kanal unterscheidet.
3. Optional können Sie ein Konversions-Event hinzufügen, um Konversionen von Nutzer:innen für eine bestimmte Aktion oder ein Campaign-Ziel zu verfolgen.
4. Wählen Sie **Campaign speichern** und schon können Sie mit Ihrer API-Campaign beginnen!

## API-Aufrufe {#api-calls}

Nachdem Sie Ihre API-Campaign gespeichert haben, fügen Sie Folgendes in Ihre API-Anfrage ein:
- Die generierten `campaign_id`-Felder in Ihrer API-Anfrage, wie in den [Endpunkten zum Senden von Nachrichten]({{site.baseurl}}/api/endpoints/messaging) angegeben.
- Ein [Nachrichtenobjekt]({{site.baseurl}}/api/objects_filters#messaging-objects) für jede in der Campaign enthaltene Plattform. Geben Sie im Nachrichtenobjekt die ID der Nachrichtenvariante an. Dadurch wird festgelegt, dass Statistiken unter dieser Variante erfasst und angezeigt werden. Die folgenden Nachrichtenobjekte werden unterstützt: Android, Content Cards, E-Mail, iOS, Kindle, SMS/MMS, Web-Push und Webhook.

### E-Mail-Anhänge hinzufügen {#adding-email-attachments}

Um Anhänge zu API-Campaign-E-Mails hinzuzufügen, fügen Sie ein `attachments`-Array in das [E-Mail-Objekt]({{site.baseurl}}/api/objects_filters/messaging/email_object) ein. Sie können ein E-Mail-Template referenzieren, das im Drag-and-Drop- oder HTML-Editor erstellt wurde, indem Sie dessen `email_template_id` im E-Mail-Objekt angeben und dann Anhänge über den API-Aufruf hinzufügen.

Einzelheiten zu Anhängen, Größenbeschränkungen und Best Practices finden Sie unter [Beispiel für ein E-Mail-Objekt mit Anhang]({{site.baseurl}}/api/objects_filters/messaging/email_object#example-email-object-with-attachment).