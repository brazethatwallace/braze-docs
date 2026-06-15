---
nav_title: Kubit
article_title: Kubit
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Kubit, einer no-code, self-service Analytics-Plattform, die sofortige Produkt-Insights liefert und es Ihnen erlaubt, Kubit-Nutzer:innen-Kohorten zu importieren und sie im Messaging von Braze anzusprechen."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/) ist eine no-code, self-service Analytics-Plattform, die sofortige Produkt-Insights liefert.

Die Integration von Braze und Kubit erlaubt es Ihnen, [Kubit-Nutzer:innen-Kohorten zu importieren]({{site.baseurl}}/partners/data_and_analytics/cohort_import/kubit/) und sie im Messaging von Braze anzusprechen. Darüber hinaus können Sie durch den Einsatz von [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) die Rohdaten der Campaigns und Impressionen von Braze in die Produkt-Analytics von Kubit integrieren, um die Wirkung dieser Campaigns in Realtime zu messen. Dieser Ansatz bietet Insights über den gesamten Lebenszyklus Ihrer Nutzer:innen, ohne dass dafür technischer Aufwand erforderlich ist.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Kubit-Unternehmenskonto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Kubit-Unternehmenskonto. |
| Übereinstimmende Nutzer-IDs | Ihre Kundendaten in Kubit und Braze müssen übereinstimmende Nutzer-IDs auf beiden Plattformen haben. Dazu gehören auch anonyme UUIDs. Besuchen Sie unsere [Dokumentation]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), um zu erfahren, wie Braze Nutzer-IDs festlegt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Braze-Daten in Kubit analysieren {#analyzing-braze-data-in-kubit}

Nutzen Sie die Vorteile von [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), um Ihre Braze-Rohdaten zu Campaigns und Impressionen mit Kubit zu teilen und sie in die Self-Service-Analytics von Kubit einzubinden, damit Sie ein vollständiges Bild des Nutzer:innen-Lebenszyklus erhalten.

Als Referenz finden Sie hier alle [Braze-Felder]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2), die in Kubit Analytics integriert werden können. Die Details dieses Schrittes sind sehr kundenspezifisch und erfordern spezielle Konfigurationen. Sprechen Sie mit Ihrem Kubit Account Manager oder kontaktieren Sie [support@kubit.ai](support@kubit.ai), um mehr zu erfahren.