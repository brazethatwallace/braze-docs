---
nav_title: Daten
article_title: Daten
page_order: 3
description: "Erfahren Sie mehr über die Braze-Datenplattform und wie Sie Ihre Daten vereinheitlichen, aktivieren und verteilen können."
---

# Braze-Datenplattform {#braze-data-platform}

> Erfahren Sie mehr über die Braze-Datenplattform und wie Sie Ihre Daten vereinheitlichen, aktivieren und verteilen können.

Die Braze-Datenplattform (BDP) ist ein umfassendes, modulares Set von Datenfunktionen und Partnerintegrationen, mit dem Sie personalisierte Erlebnisse für Ihre Kund:innen schaffen können. Bei Braze denken wir über Daten in drei zentralen Aufgabenbereichen nach: [Vereinheitlichung]({{site.baseurl}}/user_guide/data/unification/), [Aktivierung]({{site.baseurl}}/user_guide/data/activation/) und [Verteilung]({{site.baseurl}}/user_guide/data/distribution/).

Durch die Kombination von Features der Braze-Datenplattform können Sie Ihre Daten nutzen, um aussagekräftige, zielgerichtete Nachrichten zu erstellen, die in Realtime auf das Verhalten Ihrer Kund:innen reagieren.

## Funktionsweise {#how-it-works}

### Vereinheitlichen Sie Ihre Daten {#unify-your-data}

Nutzerdaten fließen über viele Eingänge in Braze ein. Erfassen und konsolidieren Sie First-Party-Daten aus beliebigen Quellen mithilfe von [APIs]({{site.baseurl}}/api/home/) und [SDKs]({{site.baseurl}}/developer_guide/sdk_integration/). Sie können auch integrierte Aufnahme-Tools wie die [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/) verwenden, um eine direkte Integration von Ihrem Data Warehouse oder Ihrer Dateispeicherlösung zu Braze herzustellen, oder die [Datentransformation]({{site.baseurl}}/user_guide/data/unification/data_transformation/) nutzen, um Webhook-Integrationen für die Datenübertragung in Braze zu erstellen und zu verwalten.

### Aktivieren Sie Ihre Daten {#activate-your-data}

Bereinigen, organisieren und bereiten Sie Ihre Daten für die Nutzung vor. Dazu gehört, das Verhalten und die Präferenzen Ihrer Kund:innen in Realtime über Nutzerprofile und Segmente zu verstehen. Nutzen Sie das [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary/) bei der Erstellung zielgerichteter Nachrichten und verwenden Sie [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs/), um Ihre Nachrichten mit Produkt- oder Inhaltsdaten anzureichern. Identifizieren Sie, wie Ihre Kund:innen auf diese personalisierten Erlebnisse reagieren.

### Verteilen Sie Ihre Daten {#distribute-your-data}

Streamen und [exportieren Sie Ihre Daten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/) in externe Systeme für weiterführende Insights und Entscheidungen. Verwenden Sie [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), um Braze-Eventdaten in ein Data Warehouse zu streamen und Business-Intelligence-Tools zu betreiben. Sie können Ihre Datenfunktionen auch mit [Technologie-Partnerintegrationen]({{site.baseurl}}/partners/data_and_analytics/) erweitern.

## Dateninfrastruktur {#data-infrastructure}

Die Braze-Dateninfrastruktur umfasst [Datenzentren]({{site.baseurl}}/user_guide/data/infrastructure/data_centers/), die dazu beitragen, die Latenz zu minimieren – also die Zeit, die Daten benötigen, um zwischen Server und Nutzer:in übertragen zu werden. Diese geografische Verteilung ermöglicht es, dass unsere Dienste zuverlässig und skalierbar sind. Wir bieten außerdem [Verschlüsselung auf Feldebene]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/) an, um sensible Daten zu schützen und die in Braze geteilten personenbezogenen Daten (PII) zu minimieren. Weitere Informationen zu Nutzung und Abrechnung finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).

## Grundprinzipien {#core-principles}

Daten spielen eine entscheidende Rolle bei der Verbesserung Ihrer Customer-Engagement-Strategie, denn sie ermöglichen es Ihnen, personalisierte Erlebnisse zu schaffen, Kundenverhalten zu verstehen und Messaging-Strategien zu optimieren. Bei Braze entwickeln wir alle Datenfunktionen mit drei Grundprinzipien:

{% details Ihre Daten härter arbeiten lassen %}
- **Flexibel und komponentenbasiert:** Unser übergreifendes Ziel ist es, Ihnen zu helfen, Ihre Daten effektiver und umfassender zu nutzen. Dank der modularen Architektur können Sie die Technologien einsetzen, die Sie benötigen, um mehr aus Ihren Daten herauszuholen – ohne unnötige Middleware.
- **Partnerintegrationen:** Braze priorisiert Integrationen mit den besten Ökosystemtechnologien (und bietet APIs an), die die bidirektionale Datenfreigabe in Realtime erleichtern.
- **Stream-Processing-Architektur:** Sie können Aktionen für jeden Datenpunkt triggern, der in Braze aufgenommen wird – für Segmentierung, Orchestrierung und Personalisierung.
{% enddetails %}

{% details Datenagilität steigern, um die Performance zu verbessern %}
- **Flexibler Aufbau von Zielgruppen:** Verringern Sie die Abhängigkeit von technischen Teams bei der Erstellung von Zielgruppen und liefern Sie personalisiertes Customer-Engagement in großem Umfang.
- **Geschwindigkeit und Performance:** Engagement-Daten und Insights werden in Realtime bereitgestellt, was iteratives, effektives Customer-Engagement sowie umfassendere Geschäftsentscheidungen unterstützt.
{% enddetails %}

{% details Ihre Daten sicher und konform halten %}
- **Branchenführende Sicherheitspraktiken:** Wir führen regelmäßig Audits durch Dritte durch, einschließlich SOC 2 Typ 2 und ISO 27001, um die höchsten Branchenstandards zu erfüllen. Wir unterhalten ein öffentliches Bug-Bounty-Programm, um proaktiv potenzielle Schwachstellen zu beheben, und verfügen über ein engagiertes Sicherheitsteam, das sich dem Schutz Ihrer Daten widmet.
- **Branchenkonformität:** Wir stellen Tools bereit, die die Einhaltung von Datenschutzbestimmungen fördern, einschließlich DSGVO und CCPA.
- **Datenschutz:** Sie können die Zustimmung von Endnutzer:innen verwalten, Anfragen bearbeiten und Verbraucherrechte durchsetzen.
{% enddetails %}