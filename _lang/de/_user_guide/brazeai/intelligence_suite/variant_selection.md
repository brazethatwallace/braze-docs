---
nav_title: Optimieren mit BrazeAI<sup>TM</sup>
article_title: A/B-Tests mit BrazeAI<sup>TM</sup> optimieren
page_order: 1.6
description: "Erfahren Sie, wie „Optimieren mit BrazeAI“ automatisch die leistungsstärksten Varianten in Campaigns mit einmaligem oder mehrfachem Versand auswählt und verteilt."
search_rank: 10
toc_headers: h2
---

# A/B-Tests mit BrazeAI<sup>TM</sup> optimieren {#optimizing-ab-tests-with-brazeai}

> Aktivieren Sie **Optimieren mit BrazeAI<sup>TM</sup>**, um eine Campaign mit mehreren Varianten automatisch zu optimieren. Die Optimierungsmethode hängt davon ab, ob die Campaign einmalig oder mehrfach versendet wird.

## Voraussetzungen {#prerequisites}

Um **Optimize with BrazeAI<sup>TM</sup>** zu verwenden, muss Ihre Campaign mindestens zwei Nachrichtenvarianten enthalten.

Für eine Campaign mit mehrfachem Versand müssen Sie außerdem:

- Mindestens ein Konversions-Event definieren.
- Das Fenster für die erneute Berechtigung auf 24 Stunden oder länger einstellen.

## Optimierung aktivieren {#turn-on-optimization}

Gehen Sie im Schritt **Target Audiences** zu **A/B Testing** und aktivieren Sie dann **Optimize with BrazeAI<sup>TM</sup>**.

## Einmalversand-Campaigns {#single-send-campaigns}

Bei einer Einmalversand-Campaign sendet Braze einen ersten Teil der Zielgruppe an jede Variante. Nach Ablauf der Experimentdauer wählt BrazeAI<sup>TM</sup> die leistungsstärkste Variante aus und sendet sie an die verbleibende Zielgruppe.

Braze wendet empfohlene Einstellungen an, wenn Sie die Optimierung aktivieren. Um diese Einstellungen zu ändern, öffnen Sie **Advanced controls**:

- **Optimization Goal:** Wählen Sie die Metrik aus, die BrazeAI<sup>TM</sup> zum Vergleich der Varianten verwendet. Die verfügbaren Ziele hängen vom Kanal ab.
- **Experiment duration:** Wählen Sie 4 Stunden, 24 Stunden, 72 Stunden oder geben Sie eine benutzerdefinierte Dauer ein.
- **Variant distribution:** Ändern Sie den Prozentsatz, der jeder Variante oder Kontrollgruppe zugewiesen wird.

Die standardmäßige Experimentdauer beträgt 4 Stunden. Wenn Sie für ein primäres Konversions-Event optimieren, beträgt der Standard 24 Stunden.

### Standard-Optimierungsziele nach Kanal {#default-optimization-goals-by-channel}

| Kanal | Standardziel |
|---|---|
| Push-Benachrichtigungen | *Opens* |
| E-Mail | *Unique Clicks* |
| SMS, MMS, RCS und WhatsApp | *Clicks* |
| Andere unterstützte Kanäle | *Primary Conversion Event - A* |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard-Optimierungsziele nach Kanal" }

## Campaigns mit mehrfachem Versand {#multi-send-campaigns}

Bei wiederkehrenden, aktionsbasierten und API-getriggerten Campaigns, die mehrfach versendet werden, optimiert BrazeAI<sup>TM</sup> die Verteilung Ihrer Zielgruppe kontinuierlich. Nach Ablauf der initialen Konversionsfrist überprüft Braze die Performance alle 12 Stunden und sendet mehr Nutzer:innen an die besser performenden Varianten.

Die anfängliche Verteilung kann gleichmäßig sein, während BrazeAI<sup>TM</sup> Performance-Daten sammelt. Die Verteilung ändert sich, sobald die Optimierung Performance-Trends erkennt.

Öffnen Sie **Advanced controls**, um eine Kontrollgruppe hinzuzufügen oder zu entfernen. Eine Kontrollgruppe bietet eine Grundlage zur Messung der Campaign-Performance und erhält keine Nachricht.

## Berichterstattung {#reporting}

Nachdem ein Einzelversand-Experiment abgeschlossen ist oder eine Mehrfachversand-Campaign genügend Daten gesammelt hat, zeigt die Seite **Campaign Analytics** den durch die Optimierung erzielten Uplift an.

![Campaign Analytics mit Uplift durch „Optimieren mit BrazeAI<sup>TM</sup>“, einschließlich Vergleichsmetriken nach dem Experimentfenster.]({% image_buster /assets/img_archive/braze_ai_variant_selection_reporting.png %})

Weitere Informationen finden Sie unter [A/B-Test-Analytics]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Warum kann ich „Mit BrazeAI<sup>TM</sup> optimieren“ nicht aktivieren? {#why-cant-i-turn-on-optimize-with-brazeai}

Die Optimierung ist nicht verfügbar, wenn:

- Die Campaign weniger als zwei aktive Varianten hat.
- Eine Campaign mit mehreren Sendungen keine Konversions-Events hat.
- Eine Campaign mit mehreren Sendungen ein Fenster für die erneute Berechtigung von weniger als 24 Stunden hat.

### Warum haben meine Varianten anfangs ähnliche Sendezahlen? {#why-do-my-variants-have-similar-send-counts-at-first}

BrazeAI<sup>TM</sup> beginnt mit einer anfänglichen Verteilung, um Performance-Daten zu sammeln. Die Verteilung wird im Laufe der Zeit angepasst, sobald Performance-Trends erkannt werden.

### Kann eine Campaign mit mehreren Sendungen aufhören zu optimieren, ohne eine Variante auszuwählen? {#can-a-multi-send-campaign-stop-optimizing-without-selecting-one-variant}

Ja. Die Optimierung stoppt, wenn BrazeAI<sup>TM</sup> mit 95-prozentiger Konfidenz feststellt, dass eine Fortsetzung des Experiments die Konversionsrate nicht um mehr als 1 % ihres aktuellen Werts verbessern würde.