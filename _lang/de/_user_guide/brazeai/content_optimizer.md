---
nav_title: Content Optimizer
article_title: Content Optimizer
alias: "/content_optimizer/"
description: "Der Content Optimizer hilft Ihnen dabei, Nachrichteninhalte in großem Umfang zu testen und zu optimieren. Dabei wird KI eingesetzt, um automatisch große Mengen an Inhaltsvarianten zu generieren und zu bewerten."
page_type: reference
page_order: 3
---

# Content Optimizer {#content-optimizer}

> Der Content Optimizer hilft Ihnen dabei, Nachrichteninhalte in großem Umfang zu testen und zu optimieren. Dabei wird KI eingesetzt, um automatisch große Mengen an Inhaltsvarianten zu generieren und zu bewerten.

{% alert important %}
Der Content Optimizer befindet sich derzeit in der Beta-Phase und ist nur für folgende Kanäle verfügbar: E-Mail, Push-Benachrichtigungen und SMS-/MMS-/RCS-Nachrichten. Für Unterstützung beim Einstieg wenden Sie sich bitte an Ihren geschäftskunden-Success-Manager.
{% endalert %}

## Über den Content Optimizer {#about-content-optimizer}

Der Content Optimizer wird in einem Canvas-Schritt ausgeführt. Er unterstützt Sie dabei, zu testende Nachrichtenkomponenten zu definieren, Varianten mithilfe generativer KI oder manueller Eingaben zu erstellen und automatisch zu optimieren, welche Inhaltskombinationen an Nutzer:innen gesendet werden. Dieses Feature hilft Ihnen dabei:

- Betreffzeilen, Kopfzeilen, Textinhalte oder primäre CTAs für E-Mails zu optimieren.
- Titel und Nachrichten für Push-Benachrichtigungen zu optimieren.
- Hooks, Textkörper und CTAs für SMS-, MMS- und RCS-Nachrichten zu optimieren.
- Die Performance von Nachrichten kontinuierlich zu verbessern, ohne manuelle A/B-Tests einrichten zu müssen.
- Große Mengen an Inhaltsvarianten schnell zu testen und dabei KI zur Ideenfindung zu nutzen.
- Leistungsschwache Inhalte automatisch auszumustern und erfolgreiche Inhalte auszubauen.

Erfahren Sie, wie Sie einen [Content Optimizer-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step) erstellen.

{% multi_lang_include brazeai/generative_ai/policy.md %}

### OpenAI und Content Optimizer {#openai-and-content-optimizer}

Der Content Optimizer verwendet OpenAI nur dann, wenn Sie explizit KI-generierte Variantenvorschläge anfordern. OpenAI wird nicht verwendet, um zu entscheiden, welche Variante einzelne Nutzer:innen erhalten, oder um den Sendeverkehr zuzuweisen.

- **Verwendet OpenAI:** Wenn Sie **Generate AI suggestions** für eine Inhaltskomponente auswählen, sendet Braze Ihre Ausgangsvariante, Anweisungen, optionale [Markenrichtlinien]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) und (bei gestarteten Schritten mit ausreichenden Sendedaten) aggregierten Performance-Kontext an OpenAI, um Variantenideen zu generieren.
- **Bandit-Optimierung:** Der proprietäre Multi-Armed-Bandit-Algorithmus von Braze übernimmt die Traffic-Zuweisung, die Variantenauswahl zum Sendezeitpunkt und die Performance-basierte Optimierung. Siehe [Funktionsweise](#how-it-works).
- **Manuelle Eingabe:** Sie können Varianten selbst eingeben, ohne Inhalte an OpenAI zu senden.

## Anwendungsfälle {#use-cases}

### E-Mail {#email}

| Anwendungsfall Optimierung | Ziel | Beschreibung |
| --- | --- | --- |
| Variationen der Betreffzeile | Öffnungsrate erhöhen | Testen Sie Tonalität, Dringlichkeit, Personalisierung und den Einsatz von Emojis. |
| Stile für Kopfzeilen-Nachrichten | Engagement steigern | Vergleichen Sie emotionale, werteorientierte und klare Nachrichten in der Kopfzeile des Textes. |
| Format des Textinhalts | Lesbarkeit und Engagement verbessern | Vergleichen Sie Storytelling mit Feature-Listen, Aufzählungspunkte mit Absätzen und verschiedene Inhaltslängen. |
| CTA-Text und Tonalität | Click-throughs steigern | Vergleichen Sie handlungsorientierte, vorteilsorientierte und in der ersten Person formulierte CTA-Formulierungen. |
| Thematische Inhaltskombinationen | Kombinationen mit hoher Performance entdecken | Kombinieren Sie thematische Betreffzeilen, Texte und CTA-Komponenten, um die beste Gesamtkombination zu finden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="E-Mail" }

### Push-Benachrichtigungen {#push-notifications}

| Anwendungsfall Optimierung | Ziel | Beschreibung |
| --- | --- | --- |
| Variationen des Titels | Öffnungsrate erhöhen | Testen Sie Klarheit, Dringlichkeit, Personalisierung und Tonalität im Push-Titel. |
| Stile für den Nachrichtentext | Engagement verbessern | Vergleichen Sie prägnante, vorteilsorientierte und handlungsorientierte Nachrichten im Push-Text. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push-Benachrichtigungen" }

### SMS-, MMS- und RCS-Nachrichten {#sms-mms-and-rcs-messages}

| Anwendungsfall Optimierung | Ziel | Beschreibung |
| --- | --- | --- |
| Hook-Variationen | Engagement steigern | Testen Sie Dringlichkeit, Personalisierung und Tonalität in der ersten Zeile, die in SMS-Vorschauen, MMS-Bildunterschriften oder RCS-Einleitungen angezeigt wird. |
| Stile für den Nachrichtentext | Engagement verbessern | Vergleichen Sie prägnante und handlungsorientierte Nachrichten im Textkörper, einschließlich Formulierungen, die Medien in MMS und RCS begleiten. |
| CTA-Text-Variationen | Click-throughs steigern | Vergleichen Sie handlungsorientierte und konversationelle CTA-Formulierungen für Links und Nächste-Schritte-Aufforderungen in SMS, MMS und RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS-, MMS- und RCS-Nachrichten" }

## Funktionsweise {#how-it-works}

Der Bandit-Algorithmus von Braze übernimmt die in diesem Abschnitt beschriebene Optimierung.

Der Content Optimizer verwendet einen nicht-kontextuellen [Multi-Armed-Bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit)-Algorithmus, um leistungsstarken Varianten mehr Sendungen zuzuweisen und die Zuweisung an leistungsschwache Varianten zu reduzieren. Im Laufe der Zeit führt dies zu einer kontinuierlichen Verbesserung Ihrer Nachrichteninhalte bei minimalem manuellem Aufwand.

Der proprietäre Bandit-Optimierungsalgorithmus von Braze wurde speziell für die kombinatorische Natur des Content Optimizer-Schritts entwickelt. Da jede Nachricht aus mehreren Komponenten besteht, lernt der Algorithmus gleichzeitig über die Performance jeder einzelnen Komponente (wie Betreffzeile, Textkörper, CTA) sowie über deren Wechselwirkungen, wenn sie zu einer Nachricht kombiniert werden. Konkret bedeutet dies: Wenn eine bestimmte Kombination gesendet wird, profitieren alle Kombinationen, die dieselben Komponenten enthalten, von den Daten dieser Sendung. Dadurch kann der Bandit im Vergleich zu einem Standard-Bandit-Algorithmus mit derselben Datenmenge wesentlich schneller lernen.

Bei der ersten Ausführung des Schritts sendet der Content Optimizer Varianten zufällig, um erste Performance-Daten zu erfassen. Nach dieser anfänglichen Erkundungsphase beginnt der Algorithmus, den Traffic auf leistungsstärkere Inhaltskombinationen umzuleiten und die Zuweisung an leistungsschwächere Optionen schrittweise zu reduzieren. Während der Erkundungsphase wird der Traffic in der Regel auf die verfügbaren Varianten verteilt, damit der Algorithmus aus deren relativer Performance lernen kann.

Der Content Optimizer ähnelt dem Nachricht-Schritt in Canvas und verfügt über Features wie Ruhezeiten, [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) und Ereignisprotokollierung. Sie können einen Content Optimizer-Schritt konfigurieren, indem Sie eine Basisnachricht erstellen und festlegen, welche Inhaltskomponenten (wie Betreffzeile, Textkörper oder Call-to-Action) optimiert werden sollen. Varianten für jede Komponente können mit KI generiert oder manuell eingegeben werden. Liquid-Tags müssen zur Basisnachricht hinzugefügt werden, um Komponenten in den Nachrichteninhalt einzubinden.

Jede:r Nutzer:in erhält eine Nachricht pro Eintritt in den Content Optimizer-Schritt. Wiedereintritte werden als neu behandelt, ohne Berücksichtigung früherer Varianten.

## Canvas-Eintritts-Setup {#canvas-entry-setup}

Für optimale Ergebnisse verwenden Sie den Content Optimizer in Canvases, in denen Nutzer:innen den Schritt schrittweise und regelmäßig über einen längeren Zeitraum hinweg erreichen – beispielsweise in wiederkehrenden oder dauerhaft aktiven Canvases mit konstantem täglichem Volumen. Wenn alle Nutzer:innen gleichzeitig in den Schritt eintreten, hat der Content Optimizer keine Zeit, aus den ersten Ergebnissen zu lernen. Der Schritt verhält sich dann eher wie ein statischer A/B-Test als wie eine Live-Optimierungs-Engine.

Am besten eignet sich der Content Optimizer für täglich wiederkehrende Eintritts-Canvases sowie für Event-getriggerte und API-getriggerte Canvases mit relativ konstantem täglichem Nutzer:innen-Eintritt. Wenn Sie den Content Optimizer in Einmal-Sende-Canvases oder Canvases mit unregelmäßigem Eintritt (z. B. monatlich wiederkehrend) verwenden, sollten Sie [Eintrittskontrollen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) nutzen, um die Nutzer:innen-Eintritte über mehrere Tage zu verteilen.

### Wichtige Konzepte {#key-concepts}

| Begriff | Beschreibung |
|-------------------------|-------------|
| Basisnachricht | Das Haupt-Template für Nachrichten, auf dem die Varianten basieren, einschließlich aller Sendeeinstellungen. |
| Inhaltskomponenten | Elemente innerhalb einer Nachricht (z. B. Betreffzeile oder primärer CTA), die getestet und optimiert werden können. Marketer müssen den entsprechenden Liquid-Tag an der Stelle in die Nachricht einfügen, an der die Komponente erscheinen soll. |
| Inhaltsvarianten | Die verschiedenen Werte, die eine Inhaltskomponente annehmen kann. |
| Inhaltskombinationen | Eindeutige Nachrichten, die durch die Kombination verschiedener Inhaltsvarianten erstellt werden. |
| Optimierungs-Event | Legt fest, wie der Content Optimizer die Performance bewertet und den Traffic im Laufe der Zeit auf Inhaltskombinationen verteilt – beispielsweise Klicks oder Öffnungen für E-Mails. Gilt für alle Inhaltskomponenten in einem Schritt. Der Content Optimizer lernt kontinuierlich aus diesem Ereignis und verschiebt die Zustellung automatisch hin zu leistungsstärkeren Inhaltskombinationen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wichtige Konzepte" }

## Hinweise {#considerations}

- Der Content Optimizer befindet sich derzeit in der Beta-Phase und ist nur für folgende Kanäle verfügbar: E-Mail, Push-Benachrichtigungen und SMS-/MMS-/RCS-Nachrichten.
- Für E-Mails kann der Content Optimizer bis zu 125 Kombinationen pro Schritt generieren:
   - Bis zu 3 Komponenten pro Schritt
   - Bis zu 5 Varianten für jede Komponente
- Für Push-Benachrichtigungen kann der Content Optimizer bis zu 25 Kombinationen pro Schritt generieren:
   - Bis zu 2 Komponenten pro Schritt
   - Bis zu 5 Varianten für jede Komponente
- Für SMS-, MMS- und RCS-Nachrichten kann der Content Optimizer bis zu 25 Kombinationen pro Schritt generieren:
   - Bis zu 2 Komponenten pro Schritt
   - Bis zu 5 Varianten für jede Komponente
- Pro Nutzer:in und Eintritt wird nur eine Nachricht gesendet. Es gibt keine Speicherung früherer Sendungen bei Wiedereintritten.
- Marketer müssen Liquid-Tags manuell für jede Komponente im Nachrichten-Editor einfügen, an der Stelle, an der die definierten Inhaltsvarianten gerendert werden sollen.

## Nächste Schritte {#next-steps}

- Wenden Sie sich an Ihren geschäftskunden-Success-Manager, um an der Beta-Phase teilzunehmen oder Unterstützung beim Onboarding zu erhalten.
- Erfahren Sie, wie Sie einen [Content Optimizer-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step) erstellen.