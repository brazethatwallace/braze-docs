---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Amplitude, einer Plattform für Produkt-Analytics und Business-Intelligence."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomamplitude-integration-with-braze-stylefloatrightwidth120pxborder0-classnoimgborderamplitude}

> [Amplitude](https://amplitude.com/) ist eine Plattform für Produkt-Analytics und Business-Intelligence.

Die bidirektionale Integration von Braze und Amplitude ermöglicht es Ihnen, [Ihre Amplitude-Kohorten]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/), Nutzermerkmale und Ereignisse in Braze zu importieren und Segmente zu erstellen, die Nutzer:innen in zukünftigen Campaigns oder Canvases ansprechen können. Sie können Braze-Currents auch nutzen, um [Ihre Braze-Ereignisse nach Amplitude zu exportieren]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) und so tiefere Analysen Ihrer Produkt- und Marketingdaten durchzuführen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Amplitude-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Amplitude-Konto](https://amplitude.com/). |
| Currents | Um Daten zurück nach Amplitude zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Wählen Sie eine Integration {#choose-an-integration}

Amplitude und Braze bieten zwei verschiedene Integrationsmethoden. Lesen Sie die folgende Dokumentation, um zu entscheiden, welche Methoden für Ihre Bedürfnisse geeignet sind:

- Braze Event Streaming: Eine Integration, die es Ihnen erlaubt, rohe Amplitude-Ereignisdaten direkt an Braze weiterzuleiten.
- [Kohortenimport]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/): Eine Integration, die es Ihnen erlaubt, Amplitude-Kohorten an Braze weiterzuleiten.

## Braze Event Streaming

### Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit allen Berechtigungen.<br><br> Dieser kann im Braze-Dashboard unter **Settings** > **API Keys** erstellt werden. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze-App-Bezeichner | Der Bezeichner für die App, die Amplitude-Ereignisse empfangen soll. Diesen finden Sie im **Braze-Dashboard > Developer Console > Settings**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

### Amplitude einrichten {#amplitude-setup}

1. Navigieren Sie in Amplitude zu **Data Destinations** und suchen Sie nach „Braze - Event Stream“.
2. Geben Sie einen Sync-Namen ein und klicken Sie dann auf **Create Sync**.
3. Klicken Sie auf **Edit** und geben Sie Ihren Braze-REST-API-Endpunkt, den REST-API-Schlüssel und den Braze-App-Bezeichner an.
4. Verwenden Sie den Filter zum Senden von Ereignissen, um die zu sendenden Ereignisse auszuwählen. Sie können alle Ereignisse senden, aber Amplitude empfiehlt, die wichtigsten auszuwählen.
5. Wenn Sie fertig sind, aktivieren Sie das Ziel und speichern Sie.

Weitere Informationen zu dieser Integration finden Sie unter [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/).

## Nutzermerkmale und Berechnungen synchronisieren {#sync-user-traits-and-computations}

Verwenden Sie Audiences, um Nutzereigenschaften und Berechnungen als angepasste Attribute an Braze zu senden. Sie können Nutzereigenschaften oder berechnete Eigenschaften für Nutzer:innen synchronisieren, die in den letzten 90 Tagen aktiv waren.

Wenn die Eigenschaft oder eine Berechnung einer Nutzerin bzw. eines Nutzers aktualisiert wird, aktualisiert Amplitude ein angepasstes Attribut in Braze mit demselben Namen wie die Nutzereigenschaft oder Berechnung.

Die Synchronisierung von Nutzermerkmalen und Berechnungen erstellt neue Nutzer:innen für Nutzer-Bezeichner, die noch nicht in Braze existieren. Berechnungen und Nutzermerkmale können nur über Nutzer-Bezeichner synchronisiert werden. Ein Nutzer-Bezeichner kann einer der folgenden sein:
- Externe ID
- Braze-ID
- Nutzer-Alias
- E-Mail-Adresse

Lesen Sie die Dokumentation von Amplitude, um mehr über die [Synchronisierung von Eigenschaften, Empfehlungen und Kohorten mit Drittanbieter-Zielen](https://help.amplitude.com/hc/en-us/articles/360060055531) zu erfahren.

#### So synchronisieren Sie Nutzereigenschaften und Berechnungen {#how-to-sync-user-properties-and-computations}

Wählen Sie in Amplitude Audiences **Syncs > Create Sync**.

![]({% image_buster /assets/img/amplitude11.png %})

Wählen Sie als Nächstes, ob Sie eine Nutzereigenschaft, eine Berechnung, eine Kohorte oder eine Empfehlung synchronisieren möchten.

{% tabs %}
{% tab Syncing user property %}

Wählen Sie **User Property** und dann die gewünschte Nutzereigenschaft zur Synchronisierung aus.

![]({% image_buster /assets/img/amplitude7.png %})

Wählen Sie als Nächstes ein Ziel aus, mit dem Sie Ihre Nutzereigenschaft synchronisieren möchten.

![]({% image_buster /assets/img/amplitude8.png %})

Legen Sie schließlich die Häufigkeit Ihrer Synchronisierung fest.

![Definieren Sie Ihren Rhythmus als einmalige oder geplante Synchronisierung.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Syncing computation %}

Wählen Sie **Computation** und dann die gewünschte Berechnung zur Synchronisierung aus.

![]({% image_buster /assets/img/amplitude10.png %})

Wählen Sie als Nächstes ein Ziel aus, mit dem Sie Ihre Berechnung synchronisieren möchten.

![]({% image_buster /assets/img/amplitude8.png %})

Legen Sie schließlich die Häufigkeit Ihrer Synchronisierung fest.

![Definieren Sie Ihren Rhythmus als einmalige oder geplante Synchronisierung.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Fehlerbehebung {#troubleshooting}

### „We do not have enough data yet for this filter“ beim Synchronisieren einer Kohorte {#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort}

Wenn Sie diesen Fehler beim [Importieren einer Amplitude-Kohorte]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/) in Braze erhalten, versuchen Sie Folgendes:

1. **Überprüfen Sie die Übereinstimmung der Nutzer-IDs.** Die User ID in Amplitude (nicht die Amplitude ID) muss exakt mit der externen Nutzer-ID in Braze (nicht der Braze- oder BSON-ID) übereinstimmen. Zum Beispiel muss die User ID `12345` in Amplitude mit der externen Nutzer-ID `12345` in Braze übereinstimmen.
2. **Generieren Sie Ihren Braze-API-Schlüssel neu.** Gehen Sie im Braze-Dashboard zu **Partner Integrations** > **Technology Partners** > **Amplitude** und wählen Sie **Generate New Key**. Versuchen Sie dann die Amplitude-Kohortensynchronisierung mit dem neuen API-Schlüssel erneut.
3. **Bestätigen Sie, dass die Kohorte in Amplitude synchronisiert wurde.** Kontaktieren Sie den [Amplitude-Support](https://help.amplitude.com/), um zu bestätigen, dass die Kohorte auf Amplitude-Seite erfolgreich synchronisiert wurde, bevor Sie die Fehlerbehebung in Braze fortsetzen.

## Amplitude-Nutzerprofil-API-Endpunkte {#amplitude-user-profile-api-endpoints}

Einige der gängigen Amplitude-API-Endpunkte, die mit Connected-Content verwendet werden können, finden Sie in unserer speziellen [Amplitude-API-Dokumentation]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_user_profile_api/).