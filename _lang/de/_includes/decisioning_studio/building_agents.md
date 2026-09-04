# Entwicklungsprozess von KI-Entscheidungsagenten {#building-ai-decisioning-agents}

> Erfahren Sie, wie Sie einen Agenten für BrazeAI Decisioning Studio™ erstellen, damit Sie personalisierte Experimente automatisieren und Ergebnisse wie Konversionen, Bindung oder Umsatz optimieren können – ohne manuelle A/B-Tests.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## Über Agenten {#about-agents}

Ein KI-Decisioning-Agent ist eine angepasste Konfiguration für die BrazeAI<sup>TM</sup>-Decisioning-Engine, die speziell auf ein bestimmtes Geschäftsziel zugeschnitten ist.

Zum Beispiel könnten Sie einen Wiederholungskauf-Agenten erstellen, um Folge-Conversions nach einem ersten Verkauf zu steigern. Sie definieren die Zielgruppe und die Nachricht in Braze, während Ihr Decisioning-Agent täglich Experimente durchführt und automatisch verschiedene Kombinationen aus Produktangeboten, Nachrichtenzeitpunkt und Häufigkeit für jede Kund:in testet. Im Laufe der Zeit lernt BrazeAI<sup>TM</sup>, was am besten funktioniert, und orchestriert personalisierte Sendungen über Braze, um die Wiederkaufraten zu maximieren.

Um einen guten Agenten zu erstellen, müssen Sie:

- Eine Erfolgsmetrik auswählen, für die BrazeAI<sup>TM</sup> optimieren soll, z. B. Umsatz, Conversions oder ARPU.
- Festlegen, welche Dimensionen getestet werden sollen, z. B. Angebot, Betreffzeile, Kreativmaterial, Kanal oder Sendezeitpunkt.
- Die Optionen für jede Dimension auswählen, z. B. E-Mail im Vergleich zu SMS oder tägliche im Vergleich zu wöchentlicher Häufigkeit.

![Beispieldiagramm eines Decisioning-Studio-Agenten für Empfehlungs-E-Mails.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Beispiel-Agenten {#sample-agents}

Hier sind einige Beispiele für Agenten, die Sie mit BrazeAI Decisioning Studio™ erstellen können. Ihre KI-Decisioning-Agenten lernen aus jeder Kundeninteraktion und wenden diese Insights auf die Aktionen des nächsten Tages an.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## Einen Agenten erstellen {#building-an-agent}

### Voraussetzungen {#prerequisites}

Bevor Sie einen Agenten erstellen können, müssen Sie [BrazeAI Decisioning Studio™ integrieren]({{site.baseurl}}/developer_guide/decisioning_studio/integration).

### Schritt 1: AI Expert Services kontaktieren {#step-1-contact-ai-expert-services}

Das AI Expert Services-Team arbeitet eng mit Ihnen zusammen, um Ihren Decisioning-Agenten zu planen, zu entwerfen und zu erstellen. Falls noch nicht geschehen, [kontaktieren Sie uns](https://www.braze.com/get-started/), um loszulegen.

Gemeinsam durchlaufen Sie die folgenden Schritte, um einen maßgeschneiderten Agenten zu erstellen, der zu Ihnen passt.

### Schritt 2: Ihren Agenten entwerfen {#step-2-design-your-agent}

Gemeinsam mit dem AI Expert Services-Team definieren Sie:

- eine Zielgruppe,
- die zu optimierende Geschäftsmetrik,
- die Aktionen für den BrazeAI<sup>TM</sup>-Decisioning-Agenten und
- alle First-Party-Kundendaten, die der Agent nutzen soll, um Ihre Geschäftsergebnisse zu steigern.

Sobald das Design steht, arbeitet das Team mit Ihnen daran, zusätzliche Integrationsanforderungen zu identifizieren und umzusetzen.

### Schritt 3: Ihre Zustellplattform einrichten {#step-3-set-up-your-delivery-platform}

Als Nächstes unterstützt Sie das AI Expert Services-Team bei der Einrichtung Ihrer Customer-Engagement-Plattform. Decisioning Studio funktioniert am besten mit Braze, es werden jedoch auch verschiedene andere Plattformen unterstützt&#8212;wenden Sie sich an Ihr AI Expert Services-Team für weitere Informationen.

{% tabs local %}
{% tab Braze %}
So richten Sie Braze ein:

1. Erstellen Sie eine [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery) oder ein [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=api-triggered%20delivery#step-12-determine-your-canvas-entry-schedule). BrazeAI Decisioning Studio™ nutzt diese Zustellmethode, um personalisierte 1:1-Aktivierungsereignisse an die Nutzer:innen in Ihrer definierten Zielgruppe zu senden.
2. Stellen Sie sicher, dass Sie keine Braze-[Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) einschließen, damit BrazeAI<sup>TM</sup> stattdessen als dedizierte Kontrollgruppe fungieren kann.
3. Je nach Ihren Dimensionen können Sie Liquid-Tags in Ihren kreativen Inhalten konfigurieren, um Ihr Messaging dynamisch mit BrazeAI<sup>TM</sup>-Empfehlungen zu befüllen. BrazeAI<sup>TM</sup> übergibt kundenspezifische Inhalte über die Braze-API an die Liquid-Tags in Ihren Templates.
{% endtab %}
{% endtabs %}

### Schritt 4: Starten und überwachen {#step-4-launch-and-monitor}

Nach dem Start Ihres Agenten überwacht und optimiert Ihr AI Expert Services-Team diesen weiterhin gemäß dem vereinbarten Design. Das Team hilft Ihnen außerdem bei Anpassungen, Erweiterungen oder Änderungen am Agenten, falls erforderlich.