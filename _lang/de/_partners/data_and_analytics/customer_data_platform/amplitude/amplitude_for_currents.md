---
nav_title: Amplitude für Currents
article_title: Amplitude für Currents
page_order: 0
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und Amplitude, einer Plattform für Produkt-Analytics und Business-Intelligence."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude für Currents {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude-for-currents}

> [Amplitude](https://amplitude.com/) ist eine Plattform für Produkt-Analytics und Business-Intelligence.

Die bidirektionale Integration von Braze und Amplitude ermöglicht es Ihnen, Ihre [Amplitude-Kohorten]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences), Nutzermerkmale und Events mit Braze zu synchronisieren und Braze-Currents zu nutzen, um [Ihre Braze-Events nach Amplitude zu exportieren](#data-export-integration) und so tiefere Analysen Ihrer Produkt- und Marketingdaten durchzuführen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Amplitude-Konto | Ein [Amplitude-Konto](https://amplitude.com/) ist erforderlich, um diese Partnerschaft zu nutzen. |
| Currents | Um Daten zurück nach Amplitude zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Datenexport-Integration {#data-export-integration}

Eine vollständige Liste der Events und Event-Eigenschaften, die von Braze an Amplitude exportiert werden können, finden Sie in den folgenden Abschnitten. Alle an Amplitude gesendeten Events enthalten die `external_user_id` der Nutzer:innen als Amplitude-Nutzer:innen-ID. Braze-spezifische Event-Eigenschaften werden unter dem Schlüssel `event_properties` in den an Amplitude gesendeten Daten übermittelt.

{% alert important %}
Um dieses Feature nutzen zu können, muss Ihre Amplitude-Nutzer:innen-ID mit der externen Braze-ID übereinstimmen.
{% endalert %}

Braze sendet nur Event-Daten für Nutzer:innen, bei denen die `external_user_id` festgelegt ist, oder für anonyme Nutzer:innen, bei denen die `device_id` festgelegt ist. Für anonyme Nutzer:innen müssen Sie Ihre Amplitude-Geräte-ID mit der Braze-Geräte-ID im SDK synchronisieren. Zum Beispiel:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Sie können zwei Arten von Events an Amplitude exportieren: [Nachrichten-Engagement-Events](#supported-currents-events), die sich aus den direkt mit dem Nachrichtenversand verbundenen Braze-Events zusammensetzen, und [Kundenverhalten-Events](#supported-currents-events), die andere App- oder Website-Aktivitäten wie Sitzungen, angepasste Events und über die Plattform erfasste Käufe umfassen. Alle regulären Events erhalten das Präfix `[Appboy]`, und alle angepassten Events erhalten das Präfix `[Appboy] [Custom Event]`. Angepasste Event- und Kauf-Event-Eigenschaften erhalten die Präfixe `[Custom event property]` bzw. `[Purchase property]`.

{% alert note %}
Braze-Currents verwendet beim Export von Events an Amplitude das Präfix `[Appboy]`. Dieses Label bezieht sich auf den früheren Produktnamen von Braze. Dies ist das erwartete Verhalten und weist nicht auf ein SDK- oder Integrationsproblem hin.
{% endalert %}

Alle Kohorten, die in Braze benannt und importiert werden, erhalten das Präfix `[Amplitude]` und das Suffix ihrer `cohort_id`. Das bedeutet, dass eine Kohorte mit dem Namen „TEST_COHORT“ und der `cohort_id` „abcd1234“ in Braze-Filtern als `[Amplitude] TEST_COHORT: abcd1234` angezeigt wird.

Wenden Sie sich an Ihren Account Manager oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen.

### Schritt 1: Amplitude-Integration in Braze konfigurieren {#step-1-configure-amplitude-integration-in-braze}

Suchen Sie in Amplitude Ihren Amplitude-Export-API-Schlüssel.

{% alert warning %}
Halten Sie Ihren Amplitude-API-Schlüssel auf dem neuesten Stand. Wenn die Zugangsdaten Ihres Konnektors ablaufen, stellt der Konnektor das Senden von Events ein. Wenn dies länger als **48 Stunden** anhält, werden die Events des Konnektors verworfen und die Daten gehen dauerhaft verloren.
{% endalert %}

### Schritt 2: Braze-Current erstellen {#step-2-create-braze-current}

Navigieren Sie in Braze zu **Currents > + Create Current > Create Amplitude Export**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail-Adresse, einen Amplitude-Export-API-Schlüssel und eine Amplitude-Region in den aufgeführten Feldern an. Wählen Sie als Nächstes die Events aus, die Sie verfolgen möchten; eine Liste der verfügbaren Events wird bereitgestellt. Klicken Sie abschließend auf **Launch Current**.

{% alert note %}
Events, die von Braze-Currents an Amplitude gesendet werden, werden auf Ihr Amplitude-Event-Volumenkontingent angerechnet.
{% endalert %}

![Die Braze-Amplitude-Currents-Seite. Diese Seite enthält Felder für den Integrationsnamen, die Kontakt-E-Mail, den API-Schlüssel und die US-Region. Die untere Hälfte der Currents-Seite listet die verfügbaren Currents-Events auf, die Sie senden können.]({% image_buster /assets/img/amplitude4.png %})

{% alert tip %}
Wenn beim Einfügen Ihres Amplitude-API-Schlüssels der Fehler „Ungültiger API-Schlüssel“ auftritt, versuchen Sie, den Schlüssel manuell einzugeben. Einige Browser können beim Kopieren und Einfügen unsichtbare Zeichen hinzufügen, die zu Validierungsfehlern führen können.
{% endalert %}

{% tab note %}
Weitere Informationen finden Sie in der Amplitude-Dokumentation zur [Appboy-Amplitude-Integration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration).
{% endtab %}

## Rate-Limits

Currents stellt eine Verbindung zur HTTP-API von Amplitude her, die ein [Rate-Limit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) von 30 Events/Sekunde pro Gerät und ein undokumentiertes Limit von 500.000 Events/Tag pro Gerät hat. Werden diese Schwellenwerte überschritten, drosselt Amplitude die über Currents protokollierten Events. Wenn ein Gerät in Ihrer Integration dieses Rate-Limit überschreitet, kann es zu Verzögerungen kommen, bis Events von allen Geräten in Amplitude angezeigt werden.

Geräte sollten unter normalen Umständen nicht mehr als 30 Events/Sekunde oder 500.000 Events/Tag melden, und dieses Event-Muster sollte nur aufgrund einer fehlerhaften Integration auftreten. Um diese Art von Verzögerung zu vermeiden, stellen Sie sicher, dass Ihre SDK-Integration Events mit einer normalen Rate meldet, wie in unseren Anweisungen zur SDK-Integration angegeben, und verzichten Sie auf automatisierte Tests, die viele Events für ein einzelnes Gerät erzeugen.

## Unterstützte Currents-Ereignisse {#supported-currents-events}

Braze unterstützt den Export der folgenden Ereignisse an Amplitude:

- [Nachrichteninteraktions-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Kundenverhalten-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Für die Payload-Struktur jedes Ereignisses wählen Sie den Tab **Amplitude** im [Glossar der Nachrichteninteraktions-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und im [Glossar der Kundenverhalten-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) aus.