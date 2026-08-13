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

Eine vollständige Liste der Events und Event-Eigenschaften, die von Braze an Amplitude exportiert werden können, finden Sie in den folgenden Abschnitten. Alle an Amplitude gesendeten Events enthalten die `external_user_id` der Nutzer:innen als Amplitude-Nutzer-ID. Braze-spezifische Event-Eigenschaften werden unter dem Schlüssel `event_properties` in den an Amplitude gesendeten Daten übermittelt.

{% alert important %}
Um dieses Feature zu nutzen, muss Ihre Amplitude-Nutzer-ID mit der externen Braze-ID übereinstimmen.
{% endalert %}

Braze sendet nur Event-Daten für Nutzer:innen, deren `external_user_id` gesetzt ist, oder für anonyme Nutzer:innen, deren `device_id` gesetzt ist. Für anonyme Nutzer:innen müssen Sie Ihre Amplitude-Geräte-ID mit der Braze-Geräte-ID im SDK synchronisieren. Zum Beispiel:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Sie können zwei Arten von Events an Amplitude exportieren: [Nachrichten-Engagement-Events](#supported-currents-events), die aus den direkt mit dem Nachrichtenversand verbundenen Braze-Events bestehen, und [Kundenverhalten-Events](#supported-currents-events), einschließlich anderer App- oder Website-Aktivitäten wie Sitzungen, angepasste Events und über die Plattform erfasste Käufe. Alle regulären Events erhalten das Präfix `[Appboy]`, und alle angepassten Events erhalten das Präfix `[Appboy] [Custom Event]`. Angepasste Event- und Kauf-Event-Eigenschaften erhalten die Präfixe `[Custom event property]` bzw. `[Purchase property]`.

Alle benannten und in Braze importierten Kohorten erhalten das Präfix `[Amplitude]` und das Suffix ihrer `cohort_id`. Das bedeutet, dass eine Kohorte mit dem Namen „TEST_COHORT“ und der `cohort_id` „abcd1234“ in Braze-Filtern als `[Amplitude] TEST_COHORT: abcd1234` angezeigt wird.

Wenden Sie sich an Ihren Account Manager oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen.

### Schritt 1: Amplitude-Integration in Braze konfigurieren {#step-1-configure-amplitude-integration-in-braze}

Suchen Sie in Amplitude Ihren Amplitude-Export-API-Schlüssel.

{% alert warning %}
Halten Sie Ihren Amplitude-API-Schlüssel aktuell. Wenn die Zugangsdaten Ihres Konnektors ablaufen, stellt der Konnektor den Versand von Events ein. Wenn dies länger als **48 Stunden** andauert, werden die Events des Konnektors verworfen und Daten gehen dauerhaft verloren.
{% endalert %}

### Schritt 2: Braze-Current erstellen {#step-2-create-braze-current}

Navigieren Sie in Braze zu **Currents > + Current erstellen > Amplitude-Export erstellen**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail, den Amplitude-Export-API-Schlüssel und die Amplitude-Region in die aufgeführten Felder ein. Wählen Sie anschließend die Events aus, die Sie verfolgen möchten; eine Liste der verfügbaren Events wird bereitgestellt. Klicken Sie abschließend auf **Current starten**.

{% alert note %}
Events, die von Braze-Currents an Amplitude gesendet werden, werden auf Ihr Amplitude-Event-Volumenkontingent angerechnet.
{% endalert %}

![Die Braze-Amplitude-Currents-Seite. Diese Seite enthält Felder für Integrationsname, Kontakt-E-Mail, API-Schlüssel und US-Region. Die untere Hälfte der Currents-Seite listet die verfügbaren Currents-Events auf, die Sie senden können.]({% image_buster /assets/img/amplitude4.png %})

{% alert tip %}
Wenn Sie beim Einfügen Ihres Amplitude-API-Schlüssels den Fehler „Ungültiger API-Schlüssel“ erhalten, versuchen Sie, den Schlüssel manuell einzugeben. Einige Browser können beim Kopieren und Einfügen versteckte Zeichen hinzufügen, die Validierungsfehler verursachen können.
{% endalert %}

{% tab note %}
Weitere Informationen finden Sie in der Amplitude-Dokumentation zur [Appboy-Amplitude-Integration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration).
{% endtab %}

## Rate-Limits

Currents stellt eine Verbindung zur HTTP-API von Amplitude her, die ein [Rate-Limit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) von 30 Events/Sekunde pro Gerät und ein undokumentiertes Limit von 500.000 Events/Tag pro Gerät hat. Wenn diese Schwellenwerte überschritten werden, drosselt Amplitude die über Currents protokollierten Events. Wenn ein Gerät in Ihrer Integration dieses Rate-Limit überschreitet, kann es zu einer Verzögerung kommen, bis Events von allen Geräten in Amplitude angezeigt werden.

Geräte sollten unter normalen Umständen nicht mehr als 30 Events/Sekunde oder 500.000 Events/Tag melden, und dieses Event-Muster sollte nur aufgrund einer fehlerhaft konfigurierten Integration auftreten. Um diese Art von Verzögerung zu vermeiden, stellen Sie sicher, dass Ihre SDK-Integration Events mit einer normalen Rate meldet, wie in unseren Anweisungen zur SDK-Integration angegeben, und verzichten Sie darauf, automatisierte Tests auszuführen, die viele Events für ein einzelnes Gerät erzeugen.

## Unterstützte Currents-Ereignisse {#supported-currents-events}

Braze unterstützt den Export der folgenden Ereignisse an Amplitude:

- [Nachrichteninteraktions-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Kundenverhalten-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Für die Payload-Struktur jedes Ereignisses wählen Sie den Tab **Amplitude** im [Glossar der Nachrichteninteraktions-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und im [Glossar der Kundenverhalten-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) aus.