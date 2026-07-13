---
nav_title: Starten Sie Ihren Agenten
article_title: Starten Sie Ihren Agenten
page_order: 4
description: "Erfahren Sie, wie Sie Ihren BrazeAI Decisioning Studio Go-Agenten starten und das Business-as-Usual-Reporting (BAU) für Performance-Vergleiche einrichten."
---

# Starten Sie Ihren Agenten {#launch-your-agent}

> Nachdem Sie Ihre Datenquellen verbunden, die Orchestrierung eingerichtet und Ihren Agenten entworfen haben, können Sie mit dem Start fortfahren. Dieser Artikel behandelt die Aktivierung Ihres Agenten und die Einrichtung der optionalen BAU-Berichterstattung.

## Schritte zum Start {#launch-steps}

Nachdem Sie alle Konfigurationsschritte im Decisioning Studio Go-Portal abgeschlossen haben:

1. Überprüfen Sie Ihre Agenten-Konfiguration, um sicherzustellen, dass alle Einstellungen korrekt sind.
2. Überprüfen Sie, ob Ihre CEP-Integration aktiv ist und die Orchestrierung bereitsteht.
3. Wählen Sie im Decisioning Studio Go-Portal **Launch** (oder eine entsprechende Aktion), um Ihren Agenten zu aktivieren.

Nach dem Start wird Ihr Agent:
- Zielgruppendaten aus Ihrem CEP empfangen
- Personalisierte Empfehlungen für jede Kund:in erstellen
- Sendungen über Ihr konfiguriertes CEP orchestrieren
- Engagement-Daten sammeln, um daraus zu lernen und sich im Laufe der Zeit zu verbessern

## Einrichtung der BAU-Berichterstattung {#set-up-bau-reporting}

Standardmäßig vergleicht das Decisioning Studio Go-Portal die Decisioning Studio Go-Gruppe mit der Random-Kontrollgruppe. Wenn Sie eine bestehende Business-as-Usual-Kampagne (BAU) haben, mit der Sie einen Vergleich durchführen möchten, können Sie die BAU-Berichterstattung einrichten, um alle drei Gruppen an einem Ort anzuzeigen.

### Vorteile der BAU-Berichterstattung {#benefits-of-bau-reporting}

Der Hauptvorteil der Einrichtung der BAU-Berichterstattung besteht in der Anwendung der Filterung ungültiger Klicks durch Decisioning Studio Go. Bei Anwendung auf alle drei Versuchsgruppen ermöglicht dies einen äußerst präzisen und fairen Vergleich der Klick-Performance („Äpfel mit Äpfeln“), indem Störfaktoren aus folgenden Bereichen eliminiert werden:
- Verdächtige maschinelle Klicks
- Klicks auf den Abmelde-Link

### Anforderungen an die BAU-Berichterstattung {#requirements-for-bau-reporting}

Bevor Sie die BAU-Berichterstattung einrichten, stellen Sie sicher, dass ein fairer Vergleich zwischen der BAU-Behandlungsgruppe, der Decisioning Studio Go-Gruppe und der Random-Kontrollgruppe möglich ist:

- **Keine Überschneidung:** Keine Empfänger:in darf während der gesamten Dauer des Experiments mehr als einer Gruppe angehören.
- **Zufällige Zuweisung:** Die Empfänger:innen werden ohne Verzerrung zufällig den Gruppen zugeordnet.
- **Gleiche Optionen:** Alle Optionen, die der BAU-Gruppe zur Verfügung stehen (Kreativmaterial, Häufigkeit, Zeitpunkt, Anreiz oder Angebot), stehen auch den Gruppen „Decisioning Studio Go“ und „Random Control“ zur Verfügung.

{% alert warning %}
Ohne ein Experimentdesign, das einen direkten Vergleich ermöglicht, kann die BAU-Berichterstattung verwirrend oder irreführend sein.
{% endalert %}

### Erforderliche Informationen {#required-information}

Nachdem Sie Ihr Versuchsdesign validiert haben, erfassen Sie die folgenden Details, um die BAU-Berichterstattung einzurichten:

**Campaign-IDs aus Ihrem CEP:**

| CEP | Akzeptierte Typen |
|-----|---------------|
| **Braze** | Campaigns und Canvases |
| **Salesforce Marketing Cloud** | Nur Journeys |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Required information" }

**Zielgruppen-ID aus Ihrem CEP:**

| CEP | Akzeptierte Typen |
|-----|---------------|
| **Braze** | Nur Segmente |
| **Salesforce Marketing Cloud** | Nur Data Extensions |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Required information" }

Sollten Sie noch keine Zielgruppe haben, die Ihre BAU-Zielgruppe trackt, müssen Sie eine solche erstellen.

### Überlegungen {#considerations}

- **Nur Klick-KPIs:** Ähnlich wie bei Decisioning Studio Go im Allgemeinen umfasst die BAU-Berichterstattung nur Klick-KPIs, nicht jedoch Conversion-KPIs.
- **Canvas-Einschränkungen:** Derzeit unterstützen wir keine Filterung nach bestimmten Canvas-Schritt-IDs. Ereignisse aus allen Canvas-Schritten werden in die BAU-Daten aufgenommen. Dies kann Vergleiche mit BAU ungültig machen, wenn nur bestimmte Canvas-Schritte berücksichtigt werden sollen.

### Einrichtung der BAU-Berichterstattung

Befolgen Sie die Anweisungen in Ihrem Decisioning Studio Go-Portal. Sie benötigen:
- Eine oder mehrere Campaign-IDs, bei denen alle Kommunikationen BAU-Kommunikationen sind
- Eine Zielgruppen-ID, die die Empfänger:innen in der BAU-Zielgruppe täglich erfasst

## Überwachung Ihres Agenten {#monitor-your-agent}

Überwachen Sie nach dem Start die Performance Ihres Agenten im Decisioning Studio Go-Portal:

- **Engagement-Metriken:** Klickraten über Versuchsgruppen hinweg verfolgen
- **Lernfortschritt:** Beobachten Sie, wie sich die Empfehlungen des Agenten im Laufe der Zeit weiterentwickeln
- **Gruppenvergleiche:** Vergleichen Sie die Performance von Decisioning Studio Go mit Random Control und BAU (sofern konfiguriert)

{% alert tip %}
Warten Sie mindestens 2–4 Wochen mit der Datenerfassung, bevor Sie Schlussfolgerungen zur Performance ziehen. Der Agent benötigt ausreichend Interaktionen, um effektiv zu lernen und zu optimieren.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

Sollte Ihr Agent nicht die erwartete Performance erbringen:

1. **Orchestrierung überprüfen:** Bestätigen Sie, dass Ihre CEP-Integration aktiv ist, Campaigns und Journeys ausgeführt werden und keine globalen Obergrenzen oder ähnliche Regeln die Orchestrierung beeinträchtigen.
2. **Datenfluss überprüfen:** Bestätigen Sie, dass Zielgruppen- und Engagement-Daten korrekt erfasst werden.
3. **Versuchsgruppen überprüfen:** Stellen Sie eine ordnungsgemäße zufällige Zuordnung sicher und vermeiden Sie Überschneidungen zwischen den Gruppen.
4. **Support kontaktieren:** Wenden Sie sich an den Braze-Support, um weitere Unterstützung zu erhalten.