---
nav_title: mParticle für Currents
article_title: mParticle für Currents
alias: /partners/mparticle_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und mParticle, einer geschäftskunden Data Platform, die Informationen sammelt und zwischen Quellen in Ihrem Marketing Stack weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle für Currents {#mparticle-for-currents}

> [mParticle](https://www.mparticle.com) ist eine geschäftskunden Data Platform (CDP), die Daten aus verschiedenen Quellen sammelt und an eine Vielzahl anderer Ziele in Ihrem Marketing Stack weiterleitet.

Die Integration von Braze und mParticle erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) können Sie auch Daten mit mParticle verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Currents | Um Daten zurück in mParticle zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto eingerichtet haben. |
| mParticle-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [mParticle-Konto](https://app.mparticle.com/login). |
| mParticle Server-zu-Server-Schlüssel und -Geheimnis | Diese erhalten Sie, indem Sie zu Ihrem mParticle-Dashboard navigieren und die [erforderlichen Feeds](#step-1-create-feeds) erstellen, die es mParticle ermöglichen, Braze-Interaktionsdaten für iOS-, Android- und Internet-Plattformen zu empfangen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Über mParticle-Zugangsdaten {#about-mparticle-credentials}

mParticle verfügt über Zugangsdaten auf App- und Workspace-Ebene, die beeinflussen, wie Ihre Events gesendet werden.

- **App-Ebene:** mParticle trennt Events nach jeder einzelnen App, d. h. die Zugangsdaten auf App-Ebene, die Sie Ihrer iOS-App zuweisen, können nur zum Senden iOS-spezifischer Events verwendet werden.
- **Workspace-Ebene:** mParticle fasst alle Events zusammen (die **nicht** app-spezifisch sind), d. h. die Zugangsdaten auf Workspace-Ebene, die Sie Ihrer App-Gruppe zuweisen, werden zum Senden aller nicht-app-spezifischen Events verwendet.

Sie können sich das so vorstellen, dass mParticle einen „Feed“ basierend auf jeder einzelnen App aufnimmt. Wenn Sie beispielsweise eine App für iOS, eine für Android und eine für das Internet haben, werden Ihre Events getrennt. Das bedeutet: Wenn Sie für jede App dieselben Zugangsdaten angeben, wird ein einziger mParticle-Feed verwendet, um alle Daten für alle Ihre Apps zu empfangen – ohne Duplikate.

## Integration

### Schritt 1: Feeds erstellen {#step-1-create-feeds}

Navigieren Sie in Ihrem mParticle-Administratorkonto zu **Setup > Inputs**. Suchen Sie **Braze** im mParticle-**Directory** und fügen Sie die Feed-Integration hinzu.

Die Braze-Feed-Integration unterstützt vier separate Feeds: iOS, Android, Internet und Ungebunden. Der ungebundene Feed kann für Events wie E-Mails verwendet werden, die nicht mit einer Plattform verbunden sind. Sie müssen für jeden Hauptplattform-Feed einen Input erstellen. Zusätzliche Inputs können Sie unter **Setup > Inputs** im Tab **Feed Configurations** erstellen.

![Einrichtung der mParticle-Feed-Inputs mit den Braze-Feed-Optionen für iOS, Android, Internet und Ungebunden.]({% image_buster /assets/img/braze-feed-inputs.png %})

Wählen Sie für jeden Feed unter **Act as Platform** die entsprechende Plattform aus der Liste aus. Wenn Sie keine Option zur Auswahl eines **Act-as**-Feeds sehen, werden die Daten als ungebunden behandelt, können aber dennoch an Data-Warehouse-Ausgaben weitergeleitet werden.

![Das erste Integrationsdialogfeld, in dem Sie aufgefordert werden, einen Konfigurationsnamen anzugeben, einen Feed-Status festzulegen und eine Plattform auszuwählen, als die agiert werden soll.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![Das zweite Integrationsdialogfeld, das den Server-zu-Server-Schlüssel und das Server-zu-Server-Geheimnis anzeigt.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

Beim Erstellen jedes Inputs stellt Ihnen mParticle einen Schlüssel und ein Geheimnis zur Verfügung. Kopieren Sie diese Zugangsdaten und notieren Sie, welchem Feed das jeweilige Zugangsdatenpaar zugeordnet ist.

### Schritt 2: Current erstellen {#step-2-create-current}

Navigieren Sie in Braze zu **Currents > + Create Current > Create mParticle Export**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail-Adresse sowie den mParticle-API-Schlüssel und den geheimen mParticle-Schlüssel für jede Plattform an. Wählen Sie anschließend die Events aus, die Sie verfolgen möchten; eine Liste der verfügbaren Events wird bereitgestellt. Klicken Sie abschließend auf **Launch Current**.

![Die mParticle-Currents-Seite in Braze. Hier finden Sie Felder für den Integrationsnamen, die Kontakt-E-Mail, den API-Schlüssel und den geheimen Schlüssel.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Es ist wichtig, Ihren mParticle-API-Schlüssel und Ihr mParticle-Geheimnis aktuell zu halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, stellt der Konnektor das Senden von Events ein. Wenn dies länger als **5 Tage** andauert, werden die Events des Konnektors verworfen und Daten gehen dauerhaft verloren.
{% endalert %}

Alle an mParticle gesendeten Events enthalten die `external_user_id` der Nutzer:innen als `customerid`. Derzeit sendet Braze keine Event-Daten für Nutzer:innen, deren `external_user_id` nicht festgelegt ist. Wenn Sie die `external_user_id` einer anderen ID in mParticle zuordnen möchten, die nicht die Standard-`customerid` ist, wenden Sie sich bitte an Ihren Braze-CSM.

## Unterstützte Currents-Events {#supported-currents-events}

Braze unterstützt den Export der folgenden Events an mParticle:

- [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Für die Payload-Struktur jedes Events wählen Sie den Tab **mParticle** im [Glossar der Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und im [Glossar der Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

Weitere Informationen zur mParticle-Integration finden Sie in der [mParticle-Dokumentation](http://docs.mparticle.com/integrations/braze/feed).