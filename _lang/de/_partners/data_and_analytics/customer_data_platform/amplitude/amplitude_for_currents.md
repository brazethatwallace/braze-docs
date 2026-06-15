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

Die bidirektionale Integration von Braze und Amplitude ermöglicht es Ihnen, Ihre [Amplitude-Kohorten]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/), Nutzermerkmale und Events mit Braze zu synchronisieren und Braze-Currents zu nutzen, um [Ihre Braze-Events nach Amplitude zu exportieren](#data-export-integration) und so tiefere Analysen Ihrer Produkt- und Marketingdaten durchzuführen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Amplitude-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Amplitude-Konto](https://amplitude.com/). |
| Currents | Um Daten zurück nach Amplitude zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Datenexport-Integration {#data-export-integration}

Eine vollständige Liste der Events und Event-Eigenschaften, die von Braze nach Amplitude exportiert werden können, finden Sie in den folgenden Abschnitten. Alle Events, die an Amplitude gesendet werden, enthalten die `external_user_id` der Nutzer:innen als Amplitude-Nutzer-ID. Braze-spezifische Event-Eigenschaften werden in den an Amplitude gesendeten Daten unter dem Schlüssel `event_properties` übermittelt.

{% alert important %}
Um dieses Feature zu nutzen, muss Ihre Amplitude-Nutzer-ID mit der externen ID von Braze übereinstimmen.
{% endalert %}

Braze sendet nur Event-Daten für Nutzer:innen, deren `external_user_id` gesetzt ist, oder für anonyme Nutzer:innen, deren `device_id` gesetzt ist. Für anonyme Nutzer:innen müssen Sie Ihre Amplitude-Geräte-ID mit der Braze-Geräte-ID im SDK synchronisieren. Zum Beispiel:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Sie können zwei Arten von Events nach Amplitude exportieren: [Message-Engagement-Events](#supported-currents-events), bestehend aus den Braze-Events, die direkt mit dem Nachrichtenversand zusammenhängen, und [Kundenverhalten-Events](#supported-currents-events), einschließlich anderer App- oder Website-Aktivitäten wie Sitzungen, angepasste Events und Käufe, die über die Plattform getrackt werden. Allen regulären Events ist das Präfix `[Appboy]` vorangestellt, allen angepassten Events das Präfix `[Appboy] [Custom Event]`. Angepassten Event- und Kauf-Event-Eigenschaften wird das Präfix `[Custom event property]` bzw. `[Purchase property]` vorangestellt.

Alle Kohorten, die benannt und in Braze importiert werden, erhalten das Präfix `[Amplitude]` und das Suffix `cohort_id`. Das bedeutet, dass eine Kohorte mit dem Namen „TEST_COHORT“ und der `cohort_id` „abcd1234“ in den Braze-Filtern als `[Amplitude] TEST_COHORT: abcd1234` angezeigt wird.

Wenden Sie sich an Ihren Account Manager oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen.

### 1. Schritt: Amplitude-Integration in Braze konfigurieren {#step-1-configure-amplitude-integration-in-braze}

Suchen Sie in Amplitude nach Ihrem Amplitude-Export-API-Schlüssel.

{% alert warning %}
Halten Sie Ihren Amplitude-API-Schlüssel auf dem neuesten Stand. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Events mehr senden. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Events des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

### 2. Schritt: Braze-Current erstellen {#step-2-create-braze-current}

Navigieren Sie in Braze zu **Currents > + Create Current > Create Amplitude Export**. Geben Sie den Integrationsnamen, eine Kontakt-E-Mail, den Amplitude-Export-API-Schlüssel und die Amplitude-Region in die aufgeführten Felder ein. Wählen Sie anschließend die Events aus, die Sie tracken möchten; eine Liste der verfügbaren Events wird angezeigt. Klicken Sie abschließend auf **Launch Current**.

{% alert note %}
Events, die von Braze-Currents an Amplitude gesendet werden, werden auf Ihr Amplitude-Event-Volumen-Kontingent angerechnet.
{% endalert %}

![Die Braze-Amplitude-Currents-Seite. Diese Seite enthält Felder für den Integrationsnamen, die Kontakt-E-Mail, den API-Schlüssel und die US-Region. In der unteren Hälfte der Currents-Seite finden Sie eine Liste der verfügbaren Currents-Events, die Sie senden können.]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
Lesen Sie die [Integrationsdokumentation](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) von Amplitude, um mehr zu erfahren.
{% endtab %}

## Rate-Limits

Currents verbindet sich mit der HTTP-API von Amplitude, die ein [Rate-Limit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) von 30 Events/Sekunde pro Gerät und ein undokumentiertes Limit von 500K Events/Tag pro Gerät hat. Wenn diese Schwellenwerte überschritten werden, drosselt Amplitude die über Currents protokollierten Events. Wenn ein Gerät in Ihrer Integration dieses Rate-Limit überschreitet, kann es zu einer Verzögerung kommen, bis Events von allen Geräten in Amplitude erscheinen.

Geräte sollten unter normalen Umständen nicht mehr als 30 Events/Sekunde oder 500K Events/Tag melden, und dieses Event-Muster sollte nur aufgrund einer falsch konfigurierten Integration auftreten. Um diese Art von Verzögerung zu vermeiden, stellen Sie sicher, dass Ihre SDK-Integration Events in einem normalen Rhythmus meldet, wie in unseren SDK-Integrationsanweisungen angegeben, und verzichten Sie auf die Durchführung automatisierter Tests, die viele Events für ein einzelnes Gerät erzeugen.

## Unterstützte Currents-Events {#supported-currents-events}

Braze unterstützt den Export der folgenden Events nach Amplitude:

- [Message-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)
- [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)

Die Payload-Struktur der einzelnen Events finden Sie auf dem Tab **Amplitude** im [Glossar der Message-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) und im [Glossar der Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/).