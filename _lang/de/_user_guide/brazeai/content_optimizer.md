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
Der Content Optimizer befindet sich derzeit in der Beta-Phase und ist nur für folgende Kanäle verfügbar: E-Mail, Push-Benachrichtigungen und SMS-/MMS-/RCS-Nachrichten. Für Unterstützung beim Einstieg wenden Sie sich bitte an Ihren CSM.
{% endalert %}

## Über den Otimizador de Conteúdo {#about-content-optimizer}

Der Content Optimizer wird in einem Canvas-Schritt ausgeführt. Er hilft Ihnen, Nachrichtenkomponenten zum Testen zu definieren, Varianten mithilfe von generativer KI oder manueller Eingabe zu erstellen und automatisch zu optimieren, welche Inhaltskombinationen an Nutzer:innen gesendet werden. Dieses Feature hilft Ihnen dabei:

- Betreffzeilen, Body-Header, Body-Inhalt oder primären CTA für E-Mails zu optimieren.
- Titel und Nachrichten für Push-Benachrichtigungen zu optimieren.
- Hooks, Bodys und CTAs für SMS-, MMS- und RCS-Nachrichten zu optimieren.
- Die Nachrichten-Performance kontinuierlich zu verbessern, ohne manuelles A/B-Test-Setup.
- Große Mengen an Inhaltsvarianten schnell zu testen und KI für die Ideenfindung zu nutzen.
- Schlecht performende Inhalte automatisch auszusortieren und Gewinnervarianten hochzuskalieren.

Erfahren Sie, wie Sie einen [Content-Optimizer-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step) erstellen.

{% multi_lang_include brazeai/generative_ai/policy.md %}

### OpenAI und Content Optimizer {#openai-and-content-optimizer}

Content Optimizer verwendet OpenAI nur, wenn Sie explizit KI-generierte Variantenvorschläge anfordern. OpenAI wird nicht verwendet, um auszuwählen, welche Variante einzelne Nutzer:innen erhalten, oder um den Versand-Traffic zuzuweisen.

- **Verwendet OpenAI:** Wenn Sie **KI-Vorschläge generieren** für eine Inhaltskomponente auswählen, sendet Braze Ihre Ausgangsvariante, Anweisungen, optionale [Markenrichtlinie]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines) und (bei gestarteten Schritten mit ausreichenden Versanddaten) aggregierten Performance-Kontext an OpenAI, um Variantenideen zu generieren.
- **Bandit-Optimierung:** Der proprietäre Multi-Armed-Bandit-Algorithmus von Braze übernimmt die Traffic-Zuweisung, die Variantenauswahl zum Sendezeitpunkt und die Performance-basierte Optimierung. Siehe [So funktioniert es](#how-it-works).
- **Manuelle Eingabe:** Sie können Varianten selbst eingeben, ohne Inhalte an OpenAI zu senden.

## Anwendungsfälle {#use-cases}

### E-Mail {#email}

| Optimierungs-Anwendungsfall | Ziel | Beschreibung |
| --- | --- | --- |
| Variationen der Betreffzeile | Öffnungsrate steigern | Testen Sie Tonalität, Dringlichkeit, Personalisierung und den Einsatz von Emojis. |
| Stile für Header-Nachrichten | Engagement steigern | Vergleichen Sie emotionale, wertorientierte und klare Formulierungen im Body-Header. |
| Format des Body-Inhalts | Lesbarkeit und Engagement verbessern | Testen Sie Storytelling im Vergleich zu Feature-Listen, Aufzählungen im Vergleich zu Absätzen und Inhaltslänge. |
| CTA-Text und Tonalität | Klick, der-throughs steigern | Vergleichen Sie handlungsorientierte, nutzenorientierte und in der ersten Person formulierte CTA-Formulierungen. |
| Thematische Inhaltskombinationen | Leistungsstarke Kombinationen entdecken | Kombinieren Sie thematisch passende Betreffzeilen-, Body- und CTA-Komponenten, um die beste Gesamtkombination zu finden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="E-Mail" }

### Push-Benachrichtigungen {#push-notifications}

| Optimierungs-Anwendungsfall | Ziel | Beschreibung |
| --- | --- | --- |
| Titelvariationen | Öffnungsrate steigern | Testen Sie Klarheit, Dringlichkeit, Personalisierung und Tonalität im Push-Titel. |
| Stile für den Body-Text | Engagement verbessern | Vergleichen Sie prägnante, nutzenorientierte und handlungsorientierte Formulierungen im Push-Body. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push-Benachrichtigungen" }

### SMS-, MMS- und RCS-Nachrichten {#sms-mms-and-rcs-messages}

| Optimierungs-Anwendungsfall | Ziel | Beschreibung |
| --- | --- | --- |
| Hook-Variationen | Engagement steigern | Testen Sie Dringlichkeit, Personalisierung und Tonalität in der ersten Zeile, die in SMS-Vorschauen, MMS-Untertiteln oder RCS-Einleitungen angezeigt wird. |
| Stile für den Body-Text | Engagement verbessern | Vergleichen Sie prägnante und handlungsorientierte Formulierungen im Body, einschließlich Texten, die Medien in MMS und RCS begleiten. |
| CTA-Textvariationen | Klick, der-throughs steigern | Vergleichen Sie handlungsorientierte und konversationelle CTA-Formulierungen für Links und Aufforderungen zu nächsten Schritten in SMS, MMS und RCS. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="SMS-, MMS- und RCS-Nachrichten" }

## Funktionsweise {#how-it-works}

Der Bandit-Algorithmus von Braze übernimmt die in diesem Abschnitt beschriebene Optimierung.

Der Content Optimizer verwendet einen nicht-kontextuellen [Multi-Armed-Bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit)-Algorithmus, um leistungsstarken Varianten mehr Sendungen zuzuweisen und die Zuweisung an leistungsschwache Varianten zu reduzieren. Im Laufe der Zeit führt dies zu einer kontinuierlichen Verbesserung Ihrer Nachrichteninhalte bei minimalem manuellem Aufwand.

Der proprietäre Bandit-Optimierungsalgorithmus von Braze wurde speziell für die kombinatorische Natur des Content Optimizer-Schritts entwickelt. Da jede Nachricht aus mehreren Komponenten besteht, lernt der Algorithmus gleichzeitig über die Performance jeder einzelnen Komponente (wie Betreffzeile, Textkörper, CTA) sowie über deren Wechselwirkungen, wenn sie zu einer Nachricht kombiniert werden. Konkret bedeutet dies: Wenn eine bestimmte Kombination gesendet wird, profitieren alle Kombinationen, die dieselben Komponenten enthalten, von den Daten dieser Sendung. Dadurch kann der Bandit im Vergleich zu einem Standard-Bandit-Algorithmus mit derselben Datenmenge wesentlich schneller lernen.

Bei der ersten Ausführung des Schritts sendet der Content Optimizer Varianten zufällig, um erste Performance-Daten zu erfassen. Nach dieser anfänglichen Erkundungsphase beginnt der Algorithmus, den Traffic auf leistungsstärkere Inhaltskombinationen umzuleiten und die Zuweisung an leistungsschwächere Optionen schrittweise zu reduzieren. Während der Erkundungsphase wird der Traffic in der Regel auf die verfügbaren Varianten verteilt, damit der Algorithmus aus deren relativer Performance lernen kann.

Der Content Optimizer ähnelt dem Nachricht-Schritt in Canvas und verfügt über Features wie Ruhezeiten, [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing) und Ereignisprotokollierung. Sie können einen Content Optimizer-Schritt konfigurieren, indem Sie eine Basisnachricht erstellen und festlegen, welche Inhaltskomponenten (wie Betreffzeile, Textkörper oder Call-to-Action) optimiert werden sollen. Varianten für jede Komponente können mit KI generiert oder manuell eingegeben werden. Liquid-Tags müssen zur Basisnachricht hinzugefügt werden, um Komponenten in den Nachrichteninhalt einzubinden.

Jede:r Nutzer:in erhält eine Nachricht pro Eintritt in den Content Optimizer-Schritt. Wiedereintritte werden als neu behandelt, ohne Berücksichtigung früherer Varianten.

Um nachgelagertes Verhalten in Ihren eigenen Analytics-Tools zuzuordnen, fügen Sie Ihrer Nachricht einen Liquid-Tag hinzu, der aufzeichnet, welche Kombination jede:r Nutzer:in erhalten hat. Weitere Informationen finden Sie unter [Kombinations-Token / Textbaustein]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#combination-token).

## Einrichtung des Canvas-Entry {#canvas-entry-setup}

Für die besten Ergebnisse verwenden Sie den Content Optimizer in Canvases, bei denen Nutzer:innen den Schritt nach und nach und regelmäßig über die Zeit betreten, z. B. in wiederkehrenden oder dauerhaft aktiven Canvases mit konsistentem täglichem Volumen. Wenn alle Nutzer:innen den Schritt gleichzeitig betreten, hat der Content Optimizer keine Zeit, aus frühen Ergebnissen zu lernen. Der Schritt verhält sich dann eher wie ein statischer A/B-Test als eine Live-Optimierungs-Engine.

Der Content Optimizer eignet sich am besten für Canvases mit täglichem wiederkehrendem Entry sowie für ereignis- und API-getriggerte Canvases mit relativ konstantem täglichem Nutzer:innen-Eintritt. Wenn Sie den Content Optimizer in Canvases mit Einzelversand oder in Canvases mit „sprunghaftem“ Entry verwenden (z. B. monatlich wiederkehrend), sollten Sie [Entry-Kontrollen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#selecting-entry-controls) nutzen, um den Eintritt der Nutzer:innen über mehrere Tage zu verteilen.

### Wichtige Konzepte {#key-concepts}

| Begriff | Beschreibung |
|-------------------------|-------------|
| Basisnachricht | Das Haupt-Nachrichten-Template, aus dem Varianten erstellt werden, einschließlich aller Versandeinstellungen. |
| Inhaltskomponenten | Elemente innerhalb einer Nachricht (z. B. Betreffzeile oder primärer CTA), die getestet und optimiert werden können. Marketer müssen den entsprechenden Liquid-Tag an der Stelle in die Nachricht einfügen, an der die Komponente erscheinen soll. |
| Inhaltsvarianten | Die verschiedenen Werte, die eine Inhaltskomponente annehmen kann. |
| Inhaltskombinationen | Eindeutige Nachrichten, die durch das Mischen und Kombinieren von Inhaltsvarianten erstellt werden. |
| Optimierungsereignis | Bestimmt, wie der Content Optimizer die Performance bewertet und den Traffic im Laufe der Zeit auf Inhaltskombinationen verteilt, z. B. Klicks oder Öffnungen bei E-Mails. Gilt für alle Inhaltskomponenten in einem Schritt. Der Content Optimizer lernt kontinuierlich aus diesem Ereignis und verschiebt die Zustellung automatisch in Richtung leistungsstärkerer Inhaltskombinationen. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wichtige Konzepte" }

## Überlegungen {#considerations}

- Der Content Optimizer befindet sich derzeit in der Betaphase und ist nur für diese Kanäle verfügbar: E-Mail, Push-Benachrichtigungen und SMS/MMS/RCS-Nachrichten.
- Für E-Mail kann der Content Optimizer bis zu 125 Kombinationen pro Schritt generieren:
   - Bis zu 3 Komponenten pro Schritt
   - Bis zu 5 Varianten pro Komponente
- Für Push-Benachrichtigungen kann der Content Optimizer bis zu 25 Kombinationen pro Schritt generieren:
   - Bis zu 2 Komponenten pro Schritt
   - Bis zu 5 Varianten pro Komponente
- Für SMS-, MMS- und RCS-Nachrichten kann der Content Optimizer bis zu 25 Kombinationen pro Schritt generieren:
   - Bis zu 2 Komponenten pro Schritt
   - Bis zu 5 Varianten pro Komponente
- Pro Nutzer:in und Entry wird nur eine Nachricht gesendet. Es gibt keinen Speicher für vorherige Sendungen bei erneuten Eintritten.
- Marketer müssen Liquid-Tags für jede Komponente manuell im Nachrichten-Editor einfügen, an der Stelle, an der die definierten Varianten der Inhaltskomponenten gerendert werden sollen.

## Nächste Schritte {#next-steps}

- Wenden Sie sich an Ihren CSM, um am Beta-Programm teilzunehmen oder Unterstützung beim Onboarding zu erhalten.
- Erfahren Sie, wie Sie einen [Content-Optimizer-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step) erstellen.