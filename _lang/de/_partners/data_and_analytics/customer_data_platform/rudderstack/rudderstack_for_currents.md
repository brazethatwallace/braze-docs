---
nav_title: RudderStack für Currents
article_title: RudderStack für Currents
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze-Currents und RudderStack, einer Open-Source-Infrastruktur für Kundendaten, die eine nahtlose Integration von Braze für Ihre Android-, iOS- und Internet-Anwendungen bietet."
page_type: partner
tool: Currents
search_tag: Partner

---

# RudderStack für Currents {#rudderstack-for-currents}

> Mit [RudderStack](https://www.rudderstack.com/) können Sie Ihre Kundendaten über Ihren Stack hinweg sammeln, transformieren und aktivieren, indem Sie Ihr Cloud Data Warehouse als zentrale Wahrheitsquelle nutzen. Dieser Artikel gibt eine Übersicht darüber, wie Sie eine Verbindung zwischen Braze-Currents und RudderStack einrichten.

Die Integration von Braze und RudderStack erlaubt es Ihnen, Braze-Currents zu nutzen, um Ihre Braze-Ereignisse nach RudderStack zu exportieren und so tiefere Analytics zu ermöglichen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| RudderStack-Konto | Sie benötigen ein [RudderStack-Konto](https://app.rudderstack.com/login), um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze-Ziel | Wir empfehlen, in RudderStack [Braze als Ziel einzurichten]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/rudderstack/rudderstack/#integration). |
| Currents | Um Daten zurück in RudderStack zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto einrichten lassen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Erstellen Sie eine Datenquelle für Braze in RudderStack {#step-1-create-a-data-source-for-braze-within-rudderstack}

Zunächst müssen Sie eine Braze-Quelle in der RudderStack-Web-App erstellen. Eine Anleitung zum Erstellen einer Datenquelle finden Sie auf der [RudderStack-Website](https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/braze-currents/).

Sobald dies geschehen ist, stellt RudderStack eine Webhook-URL zur Verfügung, einschließlich des Schreibschlüssels, den Sie im nächsten Schritt verwenden müssen. Sie finden die Webhook-URL auf dem Tab **Settings** Ihrer Braze-Quelle.

### 2. Schritt: Current erstellen {#step-2-create-current}

Navigieren Sie in Braze zu **Currents > + Create Current > RudderStack Export**. Geben Sie den Namen der Integration, die Kontakt-E-Mail, die Webhook-URL von RudderStack (die in das Schlüsselfeld gehört) und die Region von RudderStack an.

### 3. Schritt: Ereignisse exportieren {#step-3-export-events}

Wählen Sie dann die Ereignisse aus, die Sie exportieren möchten. Klicken Sie abschließend auf **Launch Current**.

Alle Ereignisse, die an RudderStack gesendet werden, enthalten die `external_user_id` der Nutzer:innen. Derzeit sendet Braze keine Ereignisdaten an RudderStack für Nutzer:innen, deren `external_user_id` nicht gesetzt ist.

## Details zur Integration {#integration-details}

Braze unterstützt den Export aller Daten, die in den [Currents-Ereignisglossaren]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) aufgeführt sind, nach RudderStack.

Die Payload-Struktur für exportierte Daten entspricht der Payload-Struktur für angepasste HTTP-Konnektoren, die Sie im [Beispiel-Repository für angepasste HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) einsehen können.