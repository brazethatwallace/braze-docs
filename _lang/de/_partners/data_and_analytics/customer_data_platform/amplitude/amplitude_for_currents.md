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
| Currents | Um Daten zurück nach Amplitude zu exportieren, muss [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto eingerichtet sein. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Datenexport-Integration {#data-export-integration}

Eine vollständige Liste der Events und Event-Eigenschaften, die von Braze nach Amplitude exportiert werden können, finden Sie in den folgenden Abschnitten. Alle an Amplitude gesendeten Events enthalten die `external_user_id` der Nutzer:innen als Amplitude-Nutzer:innen-ID. Braze-spezifische Event-Eigenschaften werden unter dem Schlüssel `event_properties` in den an Amplitude gesendeten Daten übertragen.

{% alert important %}
Um dieses Feature nutzen zu können, muss Ihre Amplitude-Nutzer:innen-ID mit der externen Braze-ID übereinstimmen.
{% endalert %}

Braze sendet nur Event-Daten für Nutzer:innen, deren `external_user_id` gesetzt ist, oder für anonyme Nutzer:innen, deren `device_id` gesetzt ist. Für anonyme Nutzer:innen müssen Sie Ihre Amplitude-Geräte-ID mit der Braze-Geräte-ID im SDK or Software-Development-Kit synchronisieren. Zum Beispiel:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Sie können zwei Arten von Events nach Amplitude exportieren: [Message-Engagement-Events](#supported-currents-events), die aus den direkt mit dem Nachrichtenversand verbundenen Braze-Events bestehen, und [Kundenverhalten-Events](#supported-currents-events), einschließlich anderer App- oder Website-Aktivitäten wie Sitzungen, angepasste Events und über die Plattform erfasste Käufe. Alle regulären Events erhalten das Präfix `[Appboy]`, und alle angepassten Events erhalten das Präfix `[Appboy] [Custom Event]`. Angepasste Event- und Kauf-Event-Eigenschaften erhalten die Präfixe `[Custom event property]` bzw. `[Purchase property]`.

{% alert note %}
Braze-Currents verwendet beim Export von Events nach Amplitude das Präfix `[Appboy]`. Dieses Label bezieht sich auf den früheren Produktnamen von Braze. Dies ist das erwartete Verhalten und deutet nicht auf ein SDK or Software-Development-Kit- oder Integrationsproblem hin.
{% endalert %}

Alle in Braze benannten und importierten Kohorten erhalten das Präfix `[Amplitude]` und das Suffix ihrer `cohort_id`. Das bedeutet, dass eine Kohorte mit dem Namen „TEST_COHORT“ und der `cohort_id` „abcd1234“ in Braze-Filtern als `[Amplitude] TEST_COHORT: abcd1234` angezeigt wird.

Wenden Sie sich an Ihren Account Manager:in oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen.

### Schritt 1: Amplitude-Integration in Braze konfigurieren {#step-1-configure-amplitude-integration-in-braze}

Suchen Sie in Amplitude Ihren Amplitude-Export-API-Schlüssel.

{% alert warning %}
Halten Sie Ihren Amplitude-API-Schlüssel stets aktuell. Wenn die Zugangsdaten Ihres Konnektors ablaufen, stellt der Konnektor den Versand von Events ein. Wenn dies länger als **48 Stunden** anhält, werden die Events des Konnektors verworfen und Daten gehen dauerhaft verloren.
{% endalert %}

### Schritt 2: Braze-Current erstellen {#step-2-create-braze-current}

Navigieren Sie in Braze zu **Currents > + Current erstellen > Amplitude-Export erstellen**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail, den Amplitude-Export-API-Schlüssel und die Amplitude-Region in die angezeigten Felder ein. Wählen Sie anschließend die Events aus, die Sie verfolgen möchten; eine Liste der verfügbaren Events wird bereitgestellt. Klicken Sie abschließend auf **Current starten**.

{% alert note %}
Von Braze-Currents an Amplitude gesendete Events werden auf Ihr Amplitude-Event-Volumenkontingent angerechnet.
{% endalert %}

![Die Braze-Amplitude-Currents-Seite. Diese Seite enthält Felder für Integrationsname, Kontakt-E-Mail, API-Schlüssel und US-Region. Die untere Hälfte der Currents-Seite zeigt die verfügbaren Currents-Events, die Sie senden können.]({% image_buster /assets/img/amplitude4.png %})

{% alert tip %}
Wenn Sie beim Einfügen Ihres Amplitude-API-Schlüssels den Fehler „Invalid API key“ erhalten, versuchen Sie, den Schlüssel manuell einzugeben. Einige Browser können beim Kopieren und Einfügen versteckte Zeichen hinzufügen, die zu Validierungsfehlern führen.
{% endalert %}

{% tab note %}
Weitere Informationen finden Sie in Amplitudes [Appboy Amplitude Integration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration).
{% endtab %}

## Rate-Limits

Currents stellt eine Verbindung zur HTTP-API von Amplitude her, die ein [Rate-Limit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) von 30 Events/Sekunde pro Gerät sowie ein undokumentiertes Limit von 500.000 Events/Tag pro Gerät hat. Werden diese Schwellenwerte überschritten, drosselt Amplitude die über Currents protokollierten Events. Wenn ein Gerät in Ihrer Integration dieses Rate-Limit überschreitet, kann es zu einer Verzögerung kommen, bis Events von allen Geräten in Amplitude angezeigt werden.

Geräte sollten unter normalen Umständen nicht mehr als 30 Events/Sekunde oder 500.000 Events/Tag melden, und dieses Event-Muster sollte nur bei einer fehlerhaft konfigurierten Integration auftreten. Um diese Art von Verzögerung zu vermeiden, stellen Sie sicher, dass Ihre SDK or Software-Development-Kit-Integration Events mit einer normalen Rate meldet, wie in unseren Anweisungen zur SDK or Software-Development-Kit-Integration angegeben, und führen Sie keine automatisierten Tests durch, die viele Events für ein einzelnes Gerät erzeugen.

## Unterstützte Currents-Events {#supported-currents-events}

Braze unterstützt den Export der folgenden Events an Amplitude:

- [Nachrichteninteraktions-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Für die Payload-Struktur jedes Events wählen Sie den Tab **Amplitude** im [Glossar der Nachrichteninteraktions-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und im [Glossar der Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) aus.