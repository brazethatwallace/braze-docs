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

API-Kampagnen werden in der Regel für transaktionsbezogene Nachrichten verwendet. Bei der Erstellung von API-Kampagnen (nicht [API-getriggerten Kampagnen]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/)) wird das Braze-Dashboard nur verwendet, um eine `campaign_id` zu generieren, mit der Sie Analytics für die Kampagnenberichterstattung verfolgen können. Sie können auch eine Nachrichtenvarianten-ID generieren, die für jede Variante Ihrer Kampagne unterschiedlich ist.

Diese Informationen senden Sie dann an Ihr Entwicklungsteam, um sie in der API-Anfrage zu verwenden, zusammen mit:
- Texte für die Kampagne
- Zielgruppenzugehörigkeit
- Assets

Nachdem die Kampagne begonnen hat, können Sie die Ergebnisse im Dashboard einsehen. API-Kampagnen verwenden die [Messaging-APIs]({{site.baseurl}}/api/endpoints/messaging/) von Braze, die über die gleichen detaillierten Berichts- und Retargeting-Optionen verfügen wie Kampagnen, die vollständig über das Dashboard erstellt wurden.

{% alert warning %}
Da API-Kampagnen in der Regel transaktionsbezogen sind, kommen alle Nutzer:innen für API-Kampagnen in Frage, auch diejenigen in Ihrer globalen Kontrollgruppe. Eine [Ein-Klick-Listenabmeldung]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe)-Kopfzeile wird diesen Sendungen nicht hinzugefügt. Wenn Sie allen API-Kampagnen eine Ein-Klick-Listenabmeldung-Kopfzeile hinzufügen möchten, wenden Sie sich an Ihren Customer-Success-Manager.
{% endalert %}

## Neue Kampagne erstellen {#create-a-new-campaign}

Gehen Sie zu **Messaging** > **Campaigns** und wählen Sie **Create Campaign**, dann wählen Sie **API Campaigns**. Jetzt können Sie mit der Konfiguration Ihrer API-Kampagne fortfahren.

Eine [API-getriggerte Kampagne]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery/) unterscheidet sich von einer API-Kampagne.

## Ihre Kampagne konfigurieren {#configure-your-campaign}

Um Ihre Kampagne zu konfigurieren, führen Sie die folgenden Schritte aus:

1. Fügen Sie einen beschreibenden Titel hinzu, damit Sie die Ergebnisse auf der Kampagnenseite finden können, nachdem Sie Ihre Nachrichten versendet haben.
2. Klicken Sie auf **Add Message** und fügen Sie die Nachrichtentypen hinzu, die in Ihre API-Kampagne aufgenommen werden sollen. Damit können Sie eine `campaign_id` und eine Nachrichtenvarianten-ID generieren, die für jeden Kanal, den Sie einbeziehen, unterschiedlich ist.
3. Optional können Sie ein Konversions-Event hinzufügen, um die Conversions der Nutzer:innen für eine bestimmte Aktion oder ein Kampagnenziel zu verfolgen.
4. Klicken Sie auf **Save Campaign** und schon können Sie mit Ihrer API-Kampagne beginnen!

## API-Aufrufe {#api-calls}

Nachdem Sie Ihre API-Kampagne gespeichert haben, fügen Sie Folgendes in Ihre API-Anfrage ein:
- Die generierten `campaign_id`-Felder in Ihrer API-Anfrage, wie in den [Endpunkten zum Senden von Nachrichten]({{site.baseurl}}/api/endpoints/messaging/#send-endpoints) beschrieben.
- Ein [Nachrichten-Objekt]({{site.baseurl}}/api/objects_filters/#messaging-objects) für jede in der Kampagne enthaltene Plattform. Geben Sie im Nachrichten-Objekt die Nachrichtenvarianten-ID an. Damit legen Sie fest, dass die Statistiken unter dieser Variante gesammelt und angezeigt werden. Die folgenden Nachrichten-Objekte werden unterstützt: Android, Content Cards, E-Mail, iOS, Kindle, SMS/MMS, Web-Push und Webhook.