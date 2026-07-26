---
nav_title: Zeotap für Currents
article_title: Zeotap für Currents
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und Zeotap, einer geschäftskunden Data Platform (CDP) der nächsten Generation, die Ihnen hilft, Ihre mobile Zielgruppe zu entdecken und zu verstehen, indem sie Identitätsauflösung, Insights und Datenanreicherung bietet."
page_type: partner
tool: Currents
search_tag: Partner
---

# Zeotap für Currents {#zeotap-for-currents}

> [Zeotap](https://zeotap.com/) ist eine geschäftskunden Data Platform (CDP) der nächsten Generation, die Ihnen hilft, Ihre mobile Zielgruppe zu entdecken und zu verstehen, indem sie Identitätsauflösung, Insights und Datenanreicherung bietet.

Die Integration von Braze und Zeotap ermöglicht es Ihnen, den Umfang und die Reichweite Ihrer Campaigns zu erweitern, indem Sie Zeotap-Kundensegmente mit Braze-Nutzerprofilen synchronisieren. Mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) können Sie Daten auch mit Zeotap verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Zeotap-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Zeotap-Konto](https://zeotap.com/). |
| Currents | Um Daten zurück in Zeotap zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Implementierung {#implementation}

### 1. Schritt: Erstellen Sie eine Currents-Quelle {#step-1-create-a-currents-source}

1. Gehen Sie in Zeotap unter **Integrate** auf **Sources**.
2. Wählen Sie **Create Source**.
3. Wählen Sie **Customer Engagement Channels** als Kategorie aus.<br><br>![Ein „Create Source“-Fenster, das verschiedene Kategorien auflistet, darunter „Customer Engagement Channels“.]({% image_buster /assets/img/zeotap/cec.png %}){: style="max-width:70%;"}<br><br>
4. Wählen Sie **Braze** als Datenquelle aus.
5. Geben Sie einen Quellennamen ein.
6. Wählen Sie Ihre Region aus.<br><br>![Fenster mit Optionen zum Auswählen Ihrer Region und der Dateneinheit.]({% image_buster /assets/img/zeotap/select_region.png %}){: style="max-width:70%;"}<br><br>
7. Wählen Sie **Create Source**.
8. Gehen Sie zum Tab **Implementation Details** und notieren Sie sich die **API URL** und den **Write Key**.<br><br>![Implementierungsdetails für Braze-Currents, die die API-URL und den Write Key enthalten.]({% image_buster /assets/img/zeotap/implementation_details.png %})

### 2. Schritt: Konfigurieren Sie das Datenstreaming in Currents {#step-2-configure-data-streaming-in-currents}

1. Gehen Sie in Braze zu **Partner Integrations** > **Data Export**.
2. Wählen Sie **Create New Current** und **Custom Currents Export**.<br><br>![Der Button „Create New Current“ mit einem Dropdown-Menü, das „Custom Currents Export“ enthält.]({% image_buster /assets/img/zeotap/custom_currents_export.png %}){: style="max-width:60%;"}<br><br>
3. Geben Sie einen Integrationsnamen und eine E-Mail-Adresse ein, über die Sie bei Fehlern mit der Integration kontaktiert werden können.
4. Geben Sie unter **Credentials** die folgenden Informationen ein, die Sie in [Schritt 1](#step-1-create-a-currents-source) notiert haben:
- Die API-URL als **Endpoint**
- Den Write Key als **Bearer Token**<br><br>![Abschnitte zur Eingabe von Integrationsdetails und Zugangsdaten.]({% image_buster /assets/img/zeotap/credentials.png %})<br><br>
5. Wählen Sie die Nachrichten-Engagement-Ereignisse aus, die Sie an Zeotap senden möchten.<br><br>![Der Tab „General Settings“ mit einem Abschnitt zum Auswählen von Nachrichten-Engagement-Ereignissen.]({% image_buster /assets/img/zeotap/message_engagement_events.png %})
6. Wählen Sie **Launch Current**, um die Änderungen zu speichern und mit dem Senden von Ereignissen an Zeotap zu beginnen.

{% alert important %}
Der Currents-Konnektor unterstützt keine anonymen Nutzer:innen (Nutzer:innen ohne `external_id`).
{% endalert %}