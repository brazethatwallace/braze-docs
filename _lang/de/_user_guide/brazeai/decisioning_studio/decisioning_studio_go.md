---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 5.5
description: "Erfahren Sie, wie Sie BrazeAI Decisioning Studio<sup>TM</sup> Go einrichten und in Braze integrieren."
---

# BrazeAI Decisioning Studio™ Go

> Erfahren Sie, wie Sie BrazeAI Decisioning Studio™ Go einrichten und in Braze integrieren.

## Über Decisioning Studio Go {#about-decisioning-studio-go}

Decisioning Studio Go ist ein KI-Decisioning-Agent für wiederkehrende E-Mail-Programme. Anstatt eine einzelne gewinnende Betreffzeile, Versandzeit oder ein einzelnes Bild für eine gesamte Zielgruppe auszuwählen, wählt der Agent die beste Kombination für jede:n Empfänger:in basierend auf deren bisherigem Engagement aus.

Sie definieren die Varianten, aus denen der Agent wählen kann – wie Betreffzeilen, CTAs, Bilder, Versandtage und Versandzeiten. Für jede:n Nutzer:in in Ihrem Segment wählt der Agent die Option aus, die am wahrscheinlichsten Engagement erzeugt, innerhalb der Einschränkungen und des Zeitplans, die Sie konfigurieren.

Dies unterscheidet sich von A/B-Tests auf Campaign-Ebene oder der [intelligenten Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_selection), die eine einzelne Variante für die gesamte Zielgruppe optimieren. Decisioning Studio Go personalisiert auf individueller Ebene über jeden Versand im Programm hinweg.

### Funktionsweise {#how-it-works}

Der Agent teilt ein Braze-Segment in zwei Gruppen auf: eine Decisioning-Studio-Gruppe, die KI-optimierte E-Mail-Inhalte erhält, und eine zufällige Kontrollgruppe (mindestens 5 %), die zufällige Kombinationen derselben Optionen erhält. Die zufällige Kontrollgruppe bietet Ihnen eine fortlaufende, vergleichbare Messung des Uplifts durch den Agenten; Sie können jederzeit sehen, wie das personalisierte Erlebnis im Vergleich zu denselben Inhalten ohne Personalisierung abschneidet.

Für jede:n Nutzer:in in der Decisioning-Studio-Gruppe wählt der Agent aus den von Ihnen bereitgestellten Optionen: welches Kreativ versendet wird (einschließlich der spezifischen Betreffzeile, des CTA und des Bildes darin), und wann es versendet wird (Wochentag und Tageszeit, unter Berücksichtigung von Ruhezeiten und der Ortszeit der/des Nutzer:in). Unter [Richten Sie Ihren Decisioning Studio Go-Agenten ein]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) werden all diese Punkte im Detail behandelt.

Wenn Nutzer:innen interagieren – oder nicht – lernt der Agent dazu. Das Reporting zeigt an, ob sich der Agent noch in seiner Trainingsphase befindet oder ob er bereits aktiv personalisiert, sodass Sie immer wissen, in welcher Phase sich der Agent befindet.

### Was Sie konfigurieren {#what-you-configure}

| Konfiguration | Beschreibung |
|---|---|
| **Zielgruppe** | Ein einzelnes Braze-Segment als Eintritts-Zielgruppe. Der Agent teilt das Segment automatisch zwischen der Decisioning-Gruppe und der zufälligen Kontrollgruppe auf. |
| **Zeitplan** | Versandfrequenz (zum Beispiel eine einzelne Auswahl dreimal pro Woche), zulässige Wochentage, Ruhezeiten in der Ortszeit der/des Nutzer:in und Einhaltung der Frequency-Capping-Regeln auf Agentenebene. |
| **Kreativinhalte** | Ein oder mehrere Basis-Kreativinhalte, die im Braze-Composer erstellt werden. Innerhalb jedes Basis-Kreativs können Sie eine Betreffzeile, einen CTA und ein Bild mithilfe von Liquid-Tags als Personalisierungspunkte markieren und dann eine Liste von Varianten für jeden bereitstellen. Der Agent entscheidet, welches Basis-Kreativ und welche Variante für jede:n Empfänger:in verwendet wird. |
| **Einschränkungen** | Limits, die verhindern, dass der Agent dasselbe Basis-Kreativ oder dieselbe Betreffzeile innerhalb eines von Ihnen definierten Zeitfensters mehr als einmal an eine:n Nutzer:in sendet. |
| **Überprüfen und starten** | Ein abschließender Validierungsbildschirm zeigt alle Warnungen an, die vor dem Start beachtet werden sollten. Der Agent wechselt von **Entwurf** zu **Aktiv** und beginnt mit dem Versand. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studio Go-Konfiguration" }

### Wann Sie Decisioning Studio Go verwenden sollten {#when-to-use-decisioning-studio-go}

Die beste Eignung besteht bei wiederkehrenden E-Mail-Programmen mit stabilen Zielgruppen und klickbaren Inhalten, wie beispielsweise Always-on-Kalendern (Rewards, Content-Drops, Lifecycle-Nudges), Evergreen-Programmen (Winbacks, erneute Interaktion) und mehrteiligen Aktionen. Diese bieten dem Agenten genügend Volumen und Vielfalt, um sinnvoll zu lernen.

Unter [Beispiele für Decisioning Studio Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples) finden Sie detaillierte Eignungshinweise nach Programmtyp.

### Wo Decisioning Studio Go in der Decisioning Studio Suite steht {#where-decisioning-studio-go-sits-in-the-decisioning-studio-suite}

Decisioning Studio Go ist die Einstiegsstufe von BrazeAI Decisioning Studio. Es ist für Marketer konzipiert, die Eins-zu-eins-E-Mail-Personalisierung ohne den Einrichtungsaufwand einer vollständigen Decisioning Studio Pro-Implementierung wünschen.

Decisioning Studio Pro bietet zusätzlich:
- Optimierung für jede beliebige Geschäftsmetrik (nicht nur Klicks)
- Anbindung an jede First-Party-Datenquelle
- Multi-Channel-Decisioning
- Erweiterte Orchestrierungsmuster
- Dedizierte Unterstützung durch das Braze AI Decisioning Services-Team

## Nächste Schritte {#next-steps}

- [Richten Sie Ihren Decisioning Studio Go-Agenten ein]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/setup) und konfigurieren Sie Zielgruppe, Zeitplan, Kreativinhalte und Einschränkungen
- [Sehen Sie sich Beispiele für Decisioning Studio Go an]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/examples), um zu prüfen, ob Ihr Programm gut geeignet ist
- Lesen Sie die [FAQ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/faq) für häufig gestellte Fragen