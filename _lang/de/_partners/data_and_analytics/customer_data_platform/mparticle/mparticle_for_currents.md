---
nav_title: mParticle für Currents
article_title: mParticle für Currents
alias: /partners/mparticle_for_currents/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze-Currents und mParticle, einer Kundendaten-Plattform, die Informationen sammelt und zwischen Quellen in Ihrem Marketing Stack weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle für Currents {#mparticle-for-currents}

> [mParticle](https://www.mparticle.com) ist eine Customer Data Platform (CDP), die Daten aus verschiedenen Quellen sammelt und an eine Vielzahl anderer Standorte in Ihrem Marketing Stack weiterleitet.

Die Integration von Braze und mParticle erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) können Sie auch Daten mit mParticle verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Currents | Um Daten zurück in mParticle zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| mParticle-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [mParticle-Konto](https://app.mparticle.com/login). |
| mParticle Server-zu-Server-Schlüssel und -Geheimnis | Diese erhalten Sie, indem Sie zu Ihrem mParticle-Dashboard navigieren und die [erforderlichen Feeds](#step-1-create-feeds) erstellen, die es mParticle ermöglichen, Braze-Interaktionsdaten für iOS-, Android- und Internet-Plattformen zu empfangen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Über mParticle-Zugangsdaten {#about-mparticle-credentials}

mParticle verfügt über Zugangsdaten auf App- und Workspace-Ebene, die beeinflussen, wie Ihre Ereignisse gesendet werden.

- **App-Ebene:** mParticle trennt Ereignisse nach jeder einzelnen App, d. h. die Zugangsdaten auf App-Ebene, die Sie Ihrer iOS-App zuweisen, können nur zum Senden iOS-spezifischer Ereignisse verwendet werden.
- **Workspace-Ebene:** mParticle fasst alle Ereignisse zusammen (die **nicht** app-spezifisch sind), d. h. die Zugangsdaten auf Workspace-Ebene, die Sie Ihrer App-Gruppe zuweisen, werden zum Senden aller nicht-app-spezifischen Ereignisse verwendet.

Sie können sich das so vorstellen, dass mParticle einen „Feed“ basierend auf jeder einzelnen App aufnimmt. Wenn Sie beispielsweise eine App für iOS, eine für Android und eine für das Internet haben, werden Ihre Ereignisse getrennt. Das bedeutet: Wenn Sie für jede App dieselben Zugangsdaten angeben, wird ein einziger mParticle-Feed verwendet, um alle Daten für alle Ihre Apps zu empfangen – ohne Duplikate.

## Integration

### 1. Schritt: Feeds erstellen {#step-1-create-feeds}

Navigieren Sie in Ihrem mParticle-Administratorkonto zu **Setup > Inputs**. Suchen Sie **Braze** im mParticle-**Directory** und fügen Sie die Feed-Integration hinzu.

Die Braze-Feed-Integration unterstützt vier separate Feeds: iOS, Android, Internet und Ungebunden. Der ungebundene Feed kann für Ereignisse wie E-Mails verwendet werden, die nicht mit einer Plattform verbunden sind. Sie müssen für jeden Hauptplattform-Feed einen Input erstellen. Zusätzliche Inputs können Sie unter **Setup > Inputs** im Tab **Feed Configurations** erstellen.

![]({% image_buster /assets/img/braze-feed-inputs.png %})

Wählen Sie für jeden Feed unter **Act as Platform** die entsprechende Plattform aus der Liste aus. Wenn Sie keine Option zur Auswahl eines **Act-as**-Feeds sehen, werden die Daten als ungebunden behandelt, können aber dennoch an Data-Warehouse-Ausgaben weitergeleitet werden.

![Das erste Integrationsdialogfeld, in dem Sie aufgefordert werden, einen Konfigurationsnamen anzugeben, einen Feed-Status festzulegen und eine Plattform auszuwählen, als die agiert werden soll.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![Das zweite Integrationsdialogfeld, das den Server-zu-Server-Schlüssel und das Server-zu-Server-Geheimnis anzeigt.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

Beim Erstellen jedes Inputs stellt Ihnen mParticle einen Schlüssel und ein Geheimnis zur Verfügung. Kopieren Sie diese Zugangsdaten und notieren Sie, welchem Feed das jeweilige Zugangsdatenpaar zugeordnet ist.

### 2. Schritt: Current erstellen {#step-2-create-current}

Navigieren Sie in Braze zu **Currents > + Create Current > Create mParticle Export**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail-Adresse sowie den mParticle-API-Schlüssel und den geheimen mParticle-Schlüssel für jede Plattform an. Wählen Sie anschließend die Ereignisse aus, die Sie verfolgen möchten; eine Liste der verfügbaren Ereignisse wird bereitgestellt. Klicken Sie abschließend auf **Launch Current**.

![Die mParticle-Currents-Seite in Braze. Hier finden Sie Felder für den Integrationsnamen, die Kontakt-E-Mail, den API-Schlüssel und den geheimen Schlüssel.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Es ist wichtig, Ihren mParticle-API-Schlüssel und Ihr mParticle-Geheimnis aktuell zu halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, stellt der Konnektor das Senden von Ereignissen ein. Wenn dies länger als **5 Tage** andauert, werden die Ereignisse des Konnektors verworfen und Daten gehen dauerhaft verloren.
{% endalert %}

Alle an mParticle gesendeten Ereignisse enthalten die `external_user_id` der Nutzer:innen als `customerid`. Derzeit sendet Braze keine Ereignisdaten für Nutzer:innen, deren `external_user_id` nicht festgelegt ist. Wenn Sie die `external_user_id` einer anderen ID in mParticle zuordnen möchten, die nicht die Standard-`customerid` ist, wenden Sie sich bitte an Ihren Braze-CSM.

## Unterstützte Currents-Ereignisse {#supported-currents-events}

Braze unterstützt den Export der folgenden Daten, die in den Currents-Glossaren für [Nutzerverhalten]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) und [Nachrichten-Engagement]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) aufgeführt sind, an mParticle:

### Verhalten {#behaviors}
- Deinstallation: `users.behaviors.Uninstall`
- Abo (globale Statusänderung): `users.behaviors.subscription.GlobalStateChange`
- Abo-Gruppe (Statusänderung): `users.behaviors.subscriptiongroup.StateChange`

### Campaigns
- Abbruch: `users_campaigns_abort`
- Conversion: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`

### Canvas
- Abbruch: `users_canvas_abort`
- Conversion: `users.canvas.Conversion`
- Eingang: `users.canvas.Entry`
- Austritt (Zielgruppe erreicht, Ereignis ausgeführt)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Experimentschritt (Conversion, Split-Eingang)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Nachrichten {#messages}
- Content-Card (Abbruch, Klick, Schließen, Impression, Senden)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- E-Mail (Abbruch, Bounce, Klick, Zustellung, als Spam markieren, Öffnung, Senden, Soft-Bounce, Abmeldung)
- In-App-Nachricht (Abbruch, Klick, Impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Push-Benachrichtigung (Abbruch, Bounce, Öffnung, Senden)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (Abbruch, Carrier-Senden, Zustellung, Zustellungsfehler, eingehender Empfang, Ablehnung, Senden, Kurzlink-Klick)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (Abbruch, Senden)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (Abbruch, Zustellung, Fehler, eingehender Empfang, Gelesen, Senden)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`


Weitere Informationen zur mParticle-Integration finden Sie in der zugehörigen Dokumentation [hier](http://docs.mparticle.com/integrations/braze/feed).