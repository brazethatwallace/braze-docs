---
page_order: 1
nav_title: Currents
article_title: Currents

layout: dev_guide

page_type: landing
description: "Auf dieser Landing-Page finden Sie Artikel über das Braze-Datenprodukt Currents. Hier erfahren Sie, wie Sie Currents einrichten, welche Partner verfügbar sind, wie die Zustellung funktioniert, was es mit dem Event-Glossar auf sich hat und vieles mehr."
tool: currents
search_rank: 9
guide_top_header: "Braze-Currents"
guide_top_text: "Die Wirkung Ihrer Engagement-Strategie zu verstehen, ist entscheidend, um Ihre Kommunikation mit Ihren Nutzer:innen gezielt weiterzuentwickeln und zu optimieren. Um diese wertvollen Engagement-Daten eng mit Ihren übrigen Abläufen zu verknüpfen und Ihre Investitionen in Data Science zu verstärken, verfolgt die Braze-Plattform eine breite Palette von Event-Daten aus Ihrer Integration für Analysen, Retargeting und andere Anwendungsfälle in Ihren eigenen Systemen. <br> <br>Currents ist ein Realtime-Datenstream Ihrer Engagement-Events – der robusteste und zugleich granularste Export der Braze-Plattform. Currents stellt Ihnen Daten im Avro-Dateiformat für einen unserer zahlreichen <a href='/docs/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners'>Datenpartner</a> bereit und ermöglicht es Ihnen, die einzigartigen und wertvollen Daten, die Braze erzeugt, für Ihre Business-Intelligence-(BI-) und Analytics-Initiativen in anderen erstklassigen Plattformen zu nutzen."

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: Currents einrichten
    link: /docs/user_guide/data/distribution/braze_currents/setting_up_currents
    image: /assets/img/braze_icons/building-01.svg
  - name: Currents-Event-Glossar
    link: /docs/user_guide/data/distribution/braze_currents/event_glossary
    image: /assets/img/braze_icons/data.svg
  - name: Anwendungsfälle
    link: /docs/user_guide/data/distribution/braze_currents/use_cases
    image: /assets/img/braze_icons/expand-05.svg
  - name: FAQ
    link: /docs/user_guide/data/distribution/braze_currents/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## Currents-Funktionen {#currents-capabilities}

Currents ermöglichen Ihnen:
* Braze-Event-Daten in ein Data Warehouse oder an einen unserer [Analytics-Partner]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners) zur detaillierten Analyse zu streamen.
* Braze-Event-Daten kontinuierlich zu streamen, um Business-Intelligence-Tools, Algorithmen für maschinelles Lernen und vieles mehr zu unterstützen.
* Braze-Event-Daten mithilfe von [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium), [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment) oder [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents) an eine Vielzahl anderer Systeme weiterzuleiten.

Es gibt noch so viel mehr, was Sie mit Event-Daten tun können, auf die Sie über Currents zugreifen. [Braze nutzt Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents) ebenfalls!

## Currents-Datenverteilungsmodell {#currents-data-distribution-model}

Currents verwendet Berechtigungskontingente, um die Erstellung von Konnektoren und das optionale Event-Tracking zu steuern.

- **Engagement-Events-Kontingente** sind für jeden Standard-Currents-Konnektor erforderlich, den Sie erstellen.
- **Kundenverhalten-Events-Kontingente** sind erforderlich, wenn Sie **Track Customer Behavior and User Events** für einen Konnektor aktivieren.
- **Nutzerprofil- und Attribut-Kontingente** sind erforderlich, wenn Sie **Track user profiles and attributes** für einen Konnektor aktivieren.

Test-Currents-Konnektoren verwenden ein separates Testlimit und verbrauchen keine Standard-Konnektor-Kontingente.

Wenn Sie ein Kontingentlimit erreichen, lesen Sie die [Fehlerbehebung bei der Einrichtung von Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#troubleshooting) und die [Currents FAQ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq), oder wenden Sie sich an Ihren Account Manager.

## So greifen Sie auf Currents zu {#how-to-access-currents}

Ein Currents-Konnektor ist bereits in vielen unserer Pro- und Enterprise-Pakete enthalten. Wenn Sie daran interessiert sind, Currents zu nutzen, wenden Sie sich an Ihren Account Manager. Ihr Account Manager und unsere Datenspezialist:innen können Sie bei der [Einrichtung und Integration von Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents) unterstützen.

<br><br>