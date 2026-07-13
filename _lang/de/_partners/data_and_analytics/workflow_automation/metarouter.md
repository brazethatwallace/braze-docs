---
nav_title: MetaRouter
article_title: MetaRouter
description: "Verbessern Sie Ihr Kundendaten-Management in Braze mit MetaRouter. Diese leistungsstarke, serverseitige Tag-Management-Lösung bietet ein Höchstmaß an Konformität und Kontrolle mit nahtlosen Bereitstellungsoptionen – ob in einer von MetaRouter gehosteten privaten Cloud oder in Ihrer eigenen Infrastruktur."
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter](https://www.metarouter.io/) steigert Ihr Braze-Erlebnis durch nahtlose Integration als leistungsstarke serverseitige Tag-Management-Plattform. Es ermöglicht Ihnen die Orchestrierung einer kompletten Customer-Data-Journey innerhalb von Braze – von der zuverlässigen, vollständig auf First-Party-Daten basierenden Datenerfassung mit einer Anreicherung von bis zu 30 % bis hin zur Aktivierung von Realtime-Event-Streams für personalisierte Journeys. Darüber hinaus vereinfacht MetaRouter die Implementierung, da keine Tags von Braze oder anderen Drittanbietern mehr benötigt werden. So erhalten Sie eine granulare, Parameter-für-Parameter-Kontrolle über die Daten, die in Braze einfließen.

_Diese Integration wird von Metarouter gepflegt._

## Unterstützte Features {#supported-features}

- Wiederholungen können eingebaut werden.
- Anfragen werden gebündelt.
- Rate-Limiting-Probleme werden mit einem erneuten Versuch behandelt.
- Externe ID und PII werden unterstützt. MetaRouter gibt die anonyme ID und alle von den Clients gewünschten PII (E-Mail, Telefonnummer, Name) weiter.
- Sie können Braze-Daten zu Käufen und angepassten Events senden.
  - Event-Eigenschaften werden unterstützt.
  - Verschachtelte Event-Eigenschaften werden nicht unterstützt.

## Voraussetzungen {#prerequisites}

Bevor Sie beginnen, benötigen Sie Folgendes:

| Anforderung           | Beschreibung                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ein MetaRouter-Konto  | Ein [MetaRouter Enterprise-Konto](https://enterprise.metarouter.io/).                                                                                |
| Braze REST-API-Schlüssel    | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. Um einen zu erstellen, gehen Sie zu **Einstellungen** > **API-Schlüssel**.                                                |
| Ein Braze REST-Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## MetaRouter einrichten {#setting-up-metarouter}

So richten Sie MetaRouter für Ihre Integration in Braze ein:

1. Gehen Sie zu MetaRouter und erstellen Sie einen neuen Cluster.
2. Wählen Sie die Events aus, die Sie tracken möchten.
3. Installieren Sie ein MetaRouter SDK und integrieren Sie Events in Ihre Website.
4. Verbinden Sie Ihren Cluster mit der UI Ihrer Website.
5. Erstellen Sie eine neue Pipeline.
6. Überprüfen Sie, ob Ihre Website Events an MetaRouter sendet.

## Integration von Braze {#integrating-braze}

### 1. Schritt: Braze-Integration hinzufügen {#step-1-add-the-braze-integration}

Wählen Sie in Enterprise MetaRouter **Integrations** > **New Integration** > **Braze** und benennen Sie Ihre Integration. Geben Sie als Nächstes Ihre Instanz-URL und Ihren API-Schlüssel ein und wählen Sie dann **Apply Changes**.

![Hinzufügen von Braze als Integration in MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### 2. Schritt: Event-Abbildung hinzufügen {#step-2-add-event-mapping}

Fügen Sie für jeden Identitätsausgang eine Event-Abbildung hinzu und konfigurieren Sie dann die Events, die Sie an Braze senden möchten. Wenn Sie fertig sind, wählen Sie **Save as New Revision**.

![Event-Abbildung für jeden der Identitätsausgänge hinzufügen.]({% image_buster /assets/img/metarouter/img2.png %})