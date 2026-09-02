---
nav_title: Daten
article_title: Braze-Datenplattform
page_order: 3
description: "Erfahren Sie mehr über die Braze-Datenplattform und wie Sie Ihre Daten vereinheitlichen, aktivieren und verteilen können."
---

# Braze-Datenplattform {#braze-data-platform}

> Erfahren Sie mehr über die Braze-Datenplattform und wie Sie Ihre Daten vereinheitlichen, aktivieren und verteilen können.

Die Braze-Datenplattform (BDP) ist ein umfassendes, modulares Set von Datenfunktionen und Partnerintegrationen, mit dem Sie personalisierte Erlebnisse für Ihre Kund:innen schaffen können. Bei Braze denken wir über Daten in drei zentralen Aufgabenbereichen nach: [Vereinheitlichung]({{site.baseurl}}/user_guide/data/unification), [Aktivierung]({{site.baseurl}}/user_guide/data/activation) und [Verteilung]({{site.baseurl}}/user_guide/data/distribution).

Durch die Kombination von Features der Braze-Datenplattform können Sie Ihre Daten nutzen, um aussagekräftige, zielgerichtete Nachrichten zu erstellen, die in Realtime auf das Verhalten Ihrer Kund:innen reagieren.

## Funktionsweise {#how-it-works}

### Daten vereinheitlichen {#unify-your-data}

Nutzerdaten fließen über viele Einstiegspunkte in Braze ein. Erfassen und konsolidieren Sie First-Party-Daten aus jeder Quelle mithilfe von [APIs]({{site.baseurl}}/api/home) und [SDKs]({{site.baseurl}}/developer_guide/sdk_integration). Sie können auch integrierte Aufnahme-Tools wie [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) nutzen, um eine direkte Integration von Ihrem Data Warehouse oder Ihrer Dateispeicherlösung zu Braze zu erstellen, oder [Datentransformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) verwenden, um Webhook-Integrationen für die Übertragung von Daten in Braze zu erstellen und zu verwalten.

### Daten aktivieren {#activate-your-data}

Bereinigen, organisieren und bereiten Sie Ihre Daten für die Nutzung vor. Dazu gehört, das Verhalten und die Präferenzen Ihrer Kund:innen in Realtime mithilfe von Nutzerprofilen und Segmenten zu verstehen. Nutzen Sie das [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary) als Referenz, wenn Sie zielgerichtete Nachrichten erstellen, und verwenden Sie [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs), um Ihre Nachrichten mit Produkt- oder Inhaltsdaten anzureichern. Identifizieren Sie, wie Ihre Kund:innen auf diese personalisierten Erlebnisse reagieren.

### Daten verteilen {#distribute-your-data}

Streamen und [exportieren Sie Ihre Daten]({{site.baseurl}}/user_guide/data/distribution/export_braze_data) in externe Systeme für weiterführende Insights und Entscheidungen. Verwenden Sie [Braze-Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents), um Braze-Event-Daten in ein Data Warehouse zu streamen und Business-Intelligence-Tools zu betreiben. Sie können Ihre Datenfähigkeiten auch mit [Technologie-Partnerintegrationen]({{site.baseurl}}/partners/data_and_analytics) erweitern.

## Dateninfrastruktur {#data-infrastructure}

Die Braze-Dateninfrastruktur umfasst [Datenzentren]({{site.baseurl}}/user_guide/data/infrastructure/data_centers), die dazu beitragen, die Latenz zu minimieren – also die Zeit, die Daten für den Weg zwischen Server und Nutzer:in benötigen. Diese geografische Verteilung sorgt dafür, dass unsere Dienste zuverlässig und skalierbar sind. Darüber hinaus bieten wir [Verschlüsselung auf Feldebene]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption) an, um sensible Daten zu schützen und die Menge an personenbezogenen Daten (PII) zu minimieren, die in Braze geteilt werden. Weitere Informationen zu Nutzung und Abrechnung finden Sie unter [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Grundprinzipien {#core-principles}

Daten spielen eine entscheidende Rolle bei der Verbesserung Ihrer Engagement-Strategie, indem sie es Ihnen ermöglichen, personalisierte Erlebnisse zu schaffen, Kundenverhalten zu verstehen und Messaging-Strategien zu optimieren. Bei Braze entwickeln wir alle Datenfunktionen mit drei Grundprinzipien:

{% details Ihre Daten effektiver nutzen %}
- **Flexibel und komponentenbasiert:** Unser übergeordnetes Ziel ist es, Ihnen zu helfen, Ihre Daten effektiver und umfassender zu nutzen. Dank einer modularen Architektur können Sie die Technologien nutzen, die Sie brauchen, um mehr aus Ihren Daten herauszuholen – ohne unnötige Middleware.
- **Partnerintegrationen:** Braze priorisiert Integrationen mit erstklassigen Ökosystem-Technologien (und bietet APIs), die Realtime-Datenaustausch in beide Richtungen unkompliziert machen.
- **Stream-Processing-Architektur:** Sie können Aktionen auf Basis jedes in Braze aufgenommenen Datenpunkts für Segmentierung, Orchestrierung und Personalisierung triggern.
{% enddetails %}

{% details Datenagilität steigern, um Performance zu verbessern %}
- **Flexible Zielgruppenerstellung:** Reduzieren Sie die Abhängigkeit von technischen Teams bei der Erstellung von Zielgruppen und ermöglichen Sie personalisiertes Customer-Engagement im großen Maßstab.
- **Geschwindigkeit und Performance:** Engagement-Daten und Insights werden in Realtime bereitgestellt, was iteratives, effektives Customer-Engagement sowie umfassendere Geschäftsentscheidungen unterstützt.
{% enddetails %}

{% details Ihre Daten sicher und konform halten %}
- **Branchenführende Sicherheitspraktiken:** Wir führen regelmäßige Audits durch Dritte durch, darunter SOC 2 Type 2 und ISO 27001, um die höchsten Branchenstandards einzuhalten. Wir betreiben ein öffentliches Bug-Bounty-Programm, um potenzielle Schwachstellen proaktiv zu adressieren, und haben ein dediziertes Sicherheitsteam, das sich dem Schutz Ihrer Daten widmet.
- **Branchenkonformität:** Wir stellen Tools bereit, die die Einhaltung von Datenschutzvorschriften fördern, darunter die DSGVO und der CCPA.
- **Datenschutz:** Sie können die Einwilligung von Endnutzer:innen verwalten, Anfragen bearbeiten und Verbraucher:innenrechte umsetzen.
{% enddetails %}