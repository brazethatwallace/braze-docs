---
nav_title: Erste Schritte
article_title: Erste Schritte mit Decisioning Studio
layout: dev_guide
guide_top_header: "Erste Schritte mit Decisioning Studio"
guide_top_text: ""
page_order: 0
search_rank: 2
page_type: landing
description: "Dieser Abschnitt bietet eine Einführung in Decisioning Studio und zeigt, wie Sie damit KI-Entscheidungsagenten entwerfen und bereitstellen können, die jede beliebige Geschäftsmetrik optimieren."

guide_featured_title: "Artikel in diesem Abschnitt"
guide_featured_list:
  - name: Ihren Agenten entwerfen
    link: /docs/user_guide/brazeai/decisioning_studio/design_agents
    image: /assets/img/braze_icons/settings-01.svg
  - name: Ihre Daten vorbereiten
    link: /docs/user_guide/brazeai/decisioning_studio/prepare_data
    image: /assets/img/braze_icons/database-01.svg
  - name: Ihre Zielgruppe definieren
    link: /docs/user_guide/brazeai/decisioning_studio/audience
    image: /assets/img/braze_icons/users-01.svg
  - name: Orchestrierung einrichten
    link: /docs/user_guide/brazeai/decisioning_studio/orchestration_setup
    image: /assets/img/braze_icons/dataflow-04.svg

guide_menu_title: "Zusätzliche Ressourcen"
guide_menu_list:
  - name: Über Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio
    image: /assets/img/braze_icons/info-circle.svg
  - name: Decisioning Studio FAQ
    link: /docs/user_guide/brazeai/decisioning_studio/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

BrazeAI Decisioning Studio™ ermöglicht es Ihnen, KI-Entscheidungsagenten zu entwerfen und bereitzustellen, die jede beliebige Geschäftsmetrik optimieren.

Diese Referenz gibt einen Überblick über die Schritte zur Einrichtung von Decisioning Studio, einschließlich des Entwurfs Ihres Agenten, der Konfiguration und Anbindung von Datenquellen, der Einrichtung der Orchestrierung und der Bewertung der Performance.

## Wichtige Designentscheidungen {#key-design-decisions}

Arbeiten Sie mit dem KI Decisioning Services-Team zusammen, um die folgenden Entscheidungen zu treffen:

| Entscheidung | Beschreibung | Beispiele |
|----------|-------------|----------|
| **Erfolgsmetrik** | Das Geschäftsergebnis, das der Agent bei der Personalisierung des Customer-Engagements maximiert. | Umsatz, LTV, ARPU, Conversions, Bindung |
| **Zielgruppe** | Die Kund:innen, für die der Decisioning-Studio-Agent Engagement-Entscheidungen trifft. | Alle Kund:innen, Mitglieder von Treueprogrammen, gefährdete Abonnent:innen |
| **Experimentgruppen** | Wie sollen die randomisierten kontrollierten Studien von Decisioning Studio strukturiert sein? | Decisioning Studio, Random Control, BAU, Holdout |
| **Dimensionen** | Die Engagement-Entscheidungen, die der Agent für jede:n Kund:in personalisiert. | Tageszeit, Betreffzeile, Häufigkeit, Angebote, Kanal |
| **Optionen** | Die spezifischen Varianten, die der Agent innerhalb jeder Dimension auswählen kann. | Bestimmte Templates, Angebote, Zeitfenster |
| **Einschränkungen** | Die Geschäftsregeln und Limits, die die Entscheidungen des Agenten einschränken. | Geografische Beschränkungen, Budgetlimits, Berechtigungsregeln |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Wichtige Designentscheidungen" }

Jede dieser Entscheidungen hat Auswirkungen darauf, wie viel inkrementellen Uplift der Agent generieren kann und wie schnell. Unser KI Decisioning Services-Team arbeitet mit Ihnen zusammen, um einen Agenten zu entwerfen, der maximalen Mehrwert generiert und gleichzeitig alle Ihre Geschäftsregeln einhält.

![Diagramm, das zeigt, wie Erfolgsmetriken, Zielgruppe, Experimentgruppen, Dimensionen, Optionen und Einschränkungen in das Design eines Decisioning-Studio-Agenten einfließen]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Funktionen von Decisioning Studio {#decisioning-studio-capabilities}

| Funktion | Details |
|------------|---------|
| **Jede Erfolgsmetrik** | Optimierung für Umsatz, Conversions, ARPU, LTV oder jeden beliebigen Geschäfts-KPI |
| **Unbegrenzte Dimensionen** | Personalisierung über Angebote, Kanäle, Timing, Häufigkeit, Kreativmaterial und mehr |
| **Jede CEP** | Native Integrationen mit Braze, Salesforce Marketing Cloud oder angepasste Integrationen für jede Plattform |
| **KI Decisioning Services** | Dedizierter Support durch das Data-Science-Team von Braze |
| **Erweitertes Experimentdesign** | Vollständig anpassbare Behandlungsgruppen und Holdouts |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Funktionen von Decisioning Studio" }

## Best Practices {#best-practices}

Einige Best Practices für das Design von Decisioning-Studio-Agenten:

- **Maximieren Sie die Datenvielfalt:** Je mehr Informationen die Agenten über Ihre Kund:innen haben, desto besser ist ihre Performance.
- **Diversifizieren Sie die Aktionen:** Je vielfältiger die Aktionen sind, die der Agent ausführen kann, desto stärker kann er seine Strategie für jede:n einzelne:n Nutzer:in personalisieren.
- **Minimieren Sie Einschränkungen:** Je weniger Einschränkungen Ihre Agenten haben, desto besser. Einschränkungen sollten so gestaltet sein, dass sie Geschäftsregeln einhalten und gleichzeitig dem Agenten so viel Freiraum wie möglich für Experimente lassen.