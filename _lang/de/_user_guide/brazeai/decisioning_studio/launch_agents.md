---
nav_title: Agent starten
article_title: Agent starten
page_order: 5
page_type: reference
description: "Erfahren Sie, wie Sie Ihren Decisioning Studio Agent starten und den KI-Entscheidungskreislauf für selbstlernende Optimierung schließen."
---

# Agent starten {#launch-your-agent}

> Nachdem Sie Datenquellen verbunden, die Orchestrierung eingerichtet und Ihren Agent entworfen haben, können Sie ihn starten. Dieser Artikel behandelt die Aktivierung Ihres Agents und das Schließen des KI-Entscheidungskreislaufs, damit der Agent kontinuierlich lernen und sich verbessern kann.

## Schritte zum Starten {#launch-steps}

Nachdem Sie alle Konfigurationsschritte mit Ihrem AI Decisioning Services-Team abgeschlossen haben:

1. Überprüfen Sie die Konfiguration Ihres Agents, um sicherzustellen, dass alle Einstellungen korrekt sind.
2. Stellen Sie sicher, dass Ihre Datenverbindungen und Orchestrierungs-Integrationen aktiv sind.
3. Arbeiten Sie mit Ihrem AI Decisioning Services-Team zusammen, um den Agent zu aktivieren.

Nach dem Start wird Ihr Agent:
- Zielgruppen- und Kundendaten empfangen
- Personalisierte Empfehlungen für jede Kund:in erstellen
- Aktionen über Ihre konfigurierte Customer-Engagement-Plattform orchestrieren
- Feedback-Daten sammeln, um im Laufe der Zeit zu lernen und sich zu verbessern

## Den KI-Entscheidungskreislauf schließen {#close-the-ai-decisioning-loop}

Nach dem Start benötigt Ihr Agent Feedback-Daten, um zu lernen und sich zu verbessern. Dazu gehören Conversion-Daten, Engagement-Daten und Aktivierungsdaten, die dem Agent mitteilen, was nach dem Versand der Customer-Engagement-Entscheidungen passiert ist.

Detaillierte Anforderungen zur Vorbereitung dieser wichtigen Feedback-Datenbestände finden Sie unter [Datenquellen vorbereiten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data).

{% alert note %}
Wenn der Agent nativ in die Customer-Engagement-Plattform integriert ist (z. B. Braze oder Salesforce Marketing Cloud), sind möglicherweise keine zusätzlichen Konfigurationsschritte für Feedback-Daten erforderlich, da diese automatisch mit den Kundendaten gesendet werden können.
{% endalert %}

## Agent überwachen {#monitor-your-agent}

Arbeiten Sie nach dem Start mit Ihrem AI Decisioning Services-Team zusammen, um die Performance zu überwachen:

- **Performance-Metriken:** Verfolgen Sie Ihre Erfolgsmetrik über Experimentgruppen hinweg
- **Lernfortschritt:** Beobachten Sie, wie sich die Empfehlungen des Agents im Laufe der Zeit entwickeln
- **Insights:** Verstehen Sie, welche Dimensionen und Optionen für verschiedene Kundensegmente zu Ergebnissen führen

## Laufende Optimierung {#ongoing-optimization}

Ihr AI Decisioning Services-Team wird weiterhin mit Ihnen zusammenarbeiten, um:

- Die Performance des Agents zu analysieren und Optimierungsmöglichkeiten zu identifizieren
- Dimensionen oder Optionen nach Bedarf zu erweitern
- Einschränkungen basierend auf Änderungen der Geschäftsregeln anzupassen
- Erfolgreiche Agents auf zusätzliche Anwendungsfälle zu skalieren

{% alert tip %}
Der Agent lernt und verbessert sich kontinuierlich im Laufe der Zeit. Geben Sie dem Agent ausreichend Zeit, um Daten zu sammeln und zu optimieren, bevor Sie wesentliche Änderungen an der Konfiguration vornehmen.
{% endalert %}