---
nav_title: Agentenkonsole
article_title: Braze Agents
page_order: 1
description: "Braze Agents können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, damit Sie personalisiertere Kundenerlebnisse bieten können."
---

# Braze Agents in der Agentenkonsole {#braze-agents-in-agent-console}

> Braze Agents sind KI-gestützte Assistenten, die Sie innerhalb von Braze erstellen können. Agenten können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, damit Sie personalisiertere Kundenerlebnisse bieten können.

{% alert important %}
Für den Zugriff auf und die Nutzung von Braze Agents sind Nachrichten- oder Aktionsguthaben erforderlich. Sollten Sie derzeit nicht über Aktionsguthaben verfügen und Braze Agents nutzen möchten, wenden Sie sich an Ihren Account Manager, um die nächsten Schritte zu besprechen.
{% endalert %}

Sehen Sie sich dieses Video an, um einen Überblick über Braze Agents in der Agentenkonsole zu erhalten.

{% multi_lang_include video.html id="afd0hp0vrh" source="wistia" title="Braze Agents in Agent Console overview" %}

## Warum sollten Sie Braze Agents einsetzen? {#why-use-braze-agents}

Braze Agents unterstützen Ihr Team dabei, intelligentere und personalisiertere Erlebnisse zu bieten – ohne zusätzlichen Arbeitsaufwand. Sie agieren als autonome Agenten, die nicht nur auf Eingaben reagieren, sondern auch den Kontext verstehen, Entscheidungen treffen und Maßnahmen ergreifen, um ein Ziel zu erreichen.

In der Praxis können Agenten automatisch Nachrichtentexte erstellen – wie Betreffzeilen oder In-Product-Texte –, sodass jede geschäftskunden eine auf sie zugeschnittene Kommunikation erhält. Sie können sich auch in Echtzeit anpassen und Personen basierend auf Präferenzen, Verhaltensweisen oder anderen Daten über verschiedene Canvas-Pfade leiten.

Über das Messaging hinaus können Agenten Ihre Kataloge bereichern, indem sie Produkt- und Profilfeldwerte berechnen oder generieren und so Ihre Daten aktuell und dynamisch halten. Durch die Übernahme repetitiver oder komplexer Aufgaben ermöglichen sie Ihrem Team, sich auf Strategie und Kreativität zu konzentrieren, anstatt sich mit manuellem Setup zu befassen. Braze Agents agieren eher als Kooperationspartner denn als Hintergrundprozesse – sie unterstützen Sie bei der Lösung von Problemen und erzielen Wirkung in großem Maßstab.

### Wann sollten Braze Agents im Vergleich zu anderen BrazeAI-Features eingesetzt werden? {#when-to-use-braze-agents-versus-other-brazeai-features}

Verwenden Sie Agenten, um Inhalte anhand des spezifischen Kontexts einer Nutzerin oder eines Nutzers in Echtzeit zu personalisieren. Wenn ein Agent beispielsweise weiß, dass die bevorzugte Eissorte einer bestimmten Nutzerin Schokolade ist und das bevorzugte Topping Gummibärchen sind, kann er eine Push-Nachricht erstellen, die speziell auf diese Kombination für diese Nutzerin zugeschnitten ist, während sie den Canvas durchläuft.

Der Agent lernt jedoch nicht durch Versuch und Irrtum und hat keine Vorstellung von einem übergeordneten Marketingziel, das er messen und maximieren möchte. Selbst wenn Sie ihn anweisen, generell Texte zu verfassen, die Conversions fördern, verfügt er über keinen Mechanismus, um die Conversion-Auswirkungen seines agentenbasierten Schreibens zu „überwachen“ und diese Daten in zukünftige agentenbasierte Aufrufe zu integrieren. Man kann sich dies als „Stimmungs“-Entscheidungsfindung vorstellen, nicht als belohnungsbasierte KI-Entscheidungsfindung.

Im Gegensatz dazu sind andere BrazeAI-Tools darauf ausgelegt, die von ihnen gemessenen Metriken zu maximieren. Beispielsweise sind Agenten sehr gut darin, qualitativ zu beurteilen, inwiefern die Eigenschaften einer Nutzerin oder eines Nutzers deren Wahrscheinlichkeit oder Neigung beeinflussen, ein bestimmtes Ereignis auszulösen oder ein bestimmtes Produkt zu mögen. Da der Agent jedoch nicht durch Versuch und Irrtum lernt, hat er keine Vorstellung davon, wie er seine Genauigkeit bei der Vorhersage von Wahrscheinlichkeiten messen und das Signal im Laufe der Zeit verbessern kann. Daher übertrifft die Predictive Suite den Agent-Schritt, wenn man die Genauigkeit der Prognosen und die Verbesserungen im Laufe der Zeit betrachtet.

## Features {#features}

Zu den Features von Braze Agents gehören:

- **Flexible Einrichtung:** Verwenden Sie ein von Braze bereitgestelltes LLM oder verbinden Sie Ihre eigenen [KI-Modellanbieter]({{site.baseurl}}/partners/ai_model_providers) (wie OpenAI, Anthropic, Google Gemini oder Databricks Mosaic).
- **Nahtlose Integration:** Setzen Sie Agenten direkt in Canvas-Schritten oder Katalogfeldern ein.
- **Testen, Protokollierung und Versionsverlauf:** Erhalten Sie eine Vorschau auf die Ausgabe Ihres Agenten, indem Sie ihn vor dem Start mit Beispiel-Eingaben testen. Sehen Sie sich die Protokolle für jeden Ausführungsvorgang des Agenten an, einschließlich der Ein- und Ausgaben für diesen Vorgang. Verwenden Sie den Tab **Versionsverlauf**, um frühere Versionen und Inline-Diffs von Anweisungsänderungen zu überprüfen.
- **Nutzungskontrollen:** Tägliche Limits unterstützen bei der Verwaltung von Performance und Kosten.

## Über Braze Agents {#about-braze-agents}

Agenten werden mit Anweisungen (System-Prompts) konfiguriert, die ihr Verhalten definieren. Wenn ein Agent ausgeführt wird, verwendet er Ihre Anweisungen zusammen mit den von Ihnen explizit übermittelten Daten, um eine Antwort zu generieren. Sie können nicht auf Nutzerdaten zugreifen, die über Ihre Konfiguration hinausgehen – Liquid-Variablen, Agent-Kontextauswahlen, Canvas-Kontextvariablen und Kontextschrittwerte. Agenten durchsuchen keine Profile und warnen nicht, wenn Daten fehlen. Siehe [Welche Daten Agenten erhalten]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

### Wichtige Konzepte {#key-concepts}

| Begriff | Definition |
| --- | --- |
| [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) | Das „Gehirn“ des Agenten, in diesem Fall ein Large Language Model (LLM). Es interpretiert Eingaben, generiert Antworten und führt Schlussfolgerungen durch. Ein leistungsfähigeres Modell (das auf relevanteren Daten trainiert wurde) macht den Agenten leistungsfähiger und vielseitiger. |
| [Anweisungen]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) | Die Regeln oder Richtlinien, die Sie dem Agenten mitteilen (System-Prompt). Sie legen fest, wie sich der Agent bei jeder Ausführung verhalten soll. Klare Anweisungen machen den Agenten zuverlässiger und berechenbarer. |
| Kontext | Daten, die während der Laufzeit an den Agenten übermittelt werden, unabhängig davon, wo dieser eingesetzt wird, wie beispielsweise Felder des Nutzerprofils oder Katalogzeilen. Diese Eingabe liefert die Informationen, die der Agent zur Generierung von Ausgaben verwendet. |
| [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#how-context-variables-work) | Temporäre Datenstücke, die Sie innerhalb der Journey einer Nutzerin oder eines Nutzers durch einen bestimmten Canvas erstellen und verwenden können. |
| [Ausgabevariable]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#define-the-output-variable) | Die Ausgabe, die der Agent erzeugt, wenn er in Canvas-Schritten verwendet wird. Ausgabevariablen speichern das Ergebnis des Agenten, um Inhalte zu personalisieren oder Workflow-Pfade zu steuern. Ausgabevariablen können vom Datentyp String, Zahl oder Boolescher Wert sein. |
| [Ausführung](#limitations) | Ein einzelner Durchlauf des Agenten. Dies wird auf Ihre täglichen Limits angerechnet. |
| [Ausgabeformat]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#select-output) | Die vordefinierte Datenstruktur der Antwort des Agenten. |
| [Wissensquellen]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) | Eine Art von Agent-Kontext, der verwendet wird, um Daten aus einem Katalog genauer abzurufen, als wenn der Katalog direkt in den Anweisungen des Agenten referenziert wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Wichtige Konzepte" }

## Einschränkungen {#limitations}

Es gelten die folgenden Einschränkungen:

- Jeder Agent verfügt über ein standardmäßiges tägliches Ausführungslimit von 250.000 Durchläufen, das auf maximal 1.000.000 Durchläufe pro Tag erhöht werden kann. Wenden Sie sich an Ihren geschäftskunden-Success-Manager, wenn Sie dieses Limit erhöhen möchten.
- Die Agentenkonsole zeigt für jeden Agenten ein **tägliches Aktionsguthaben-Kostenlimit** an – die geschätzten maximalen Credits pro Tag basierend auf dem Credit-Verhältnis pro Ausführung Ihres Modells und dem täglichen Ausführungslimit. Siehe [Tägliche Ausführungs- und Credit-Limits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Standardmäßig muss jeder Durchlauf innerhalb von 20 Sekunden abgeschlossen sein. Nach 20 Sekunden gibt der Agent eine `null`-Antwort zurück, wo immer er verwendet wird.
    - Sollten Ihre Agenten regelmäßig eine Zeitüberschreitung aufweisen, wenden Sie sich an Ihren Braze Account Manager, um dieses Limit zu erhöhen.
- Die Eingabedaten sind auf 25 KB pro Anfrage begrenzt. Längere Eingaben werden gekürzt.

## Best Practices {#best-practices}

Konzentrieren Sie sich auf hochwertige Anwendungsfälle, bei denen Agenten die größte Kapitalrendite (ROI) erzielen können, und wählen Sie Zielgruppen aus, die wahrscheinlich reagieren werden. Eine kleinere Zielgruppe mit hoher Opportunity übertrifft oft eine große Zielgruppe mit geringer Opportunity – beispielsweise das Retargeting von Nutzer:innen, die kürzlich gesucht, aber nicht konvertiert haben, anstatt agentengenerierten Text an Ihre gesamte Nutzerbasis zu senden.

Um den ROI vor der Skalierung zu validieren, verwenden Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt, um nur einen Teil Ihrer Zielgruppe durch einen Agent-Schritt zu leiten. Weitere Hinweise zur Bereitstellung finden Sie unter [Angepasste Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Fehlerbehandlung {#error-handling}

Wenn das verbundene Modell während einer Canvas-Schritt-Agent- oder Katalog-Agent-Ausführung einen [Rate-Limit-Fehler]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) vom LLM-Anbieter zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff.

Bei anderen Fehlern (wie einer Zeitüberschreitung oder einem ungültigen API-Schlüssel) wird die Ausgabe des Canvas-Schritt-Agenten auf `null` gesetzt, es sei denn, der Agent verfügt über [konfigurierte Fallback-Werte]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in der Agentenkonsole (nur Canvas-Schritt-Agenten). Katalog-Agenten wiederholen Fehler, die nicht auf Rate-Limits zurückzuführen sind, nicht. Wenn ein Agent sein tägliches Ausführungslimit erreicht, wendet Braze die konfigurierten Fallback-Werte an, sofern vorhanden; andernfalls wird die Ausgabe auf `null` gesetzt.

Wenn viele Nutzer:innen gleichzeitig einen Agent-Schritt betreten, kann die Verarbeitung aufgrund von [Ausführungsflusskontrollen]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls) länger dauern. Konfigurieren Sie Fallback-Werte in der Agentenkonsole für Canvas-Schritt-Agenten, damit Nutzer:innen auch dann eine Ausgabe erhalten, wenn eine Ausführung fehlschlägt, oder verwenden Sie [Standard-Liquid-Werte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) in nachgelagerten Nachrichten-Schritten.

## Wie werden meine Daten verwendet und an die von Braze bereitgestellten LLMs übermittelt? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Um KI-Ausgaben über die Braze-KI-Features zu generieren, die Braze als Nutzung der von Braze bereitgestellten LLMs identifiziert („Ausgabe“), übermittelt Braze Ihren System-Prompt oder gegebenenfalls andere Eingaben („Eingabe“) an das von Braze bereitgestellte LLM. Die an das entsprechende von Braze bereitgestellte LLM gesendeten Daten werden nicht zum Trainieren oder Verbessern des von Braze bereitgestellten LLM verwendet. Zwischen Ihnen und Braze ist die Ausgabe Ihr geistiges Eigentum. Braze erhebt keine Urheberrechtsansprüche auf solche Ausgaben. Braze übernimmt keinerlei Garantie in Bezug auf KI-generierte Inhalte im Allgemeinen, einschließlich der Ausgabe.

Das von Braze bereitgestellte LLM für Braze Agents, gekennzeichnet als „Auto“, nutzt Google Gemini-Modelle. Google speichert die über Braze übermittelten Eingaben und Ausgaben für 55 Tage, danach werden die Daten gelöscht.

## Nächste Schritte {#next-steps}

Nachdem Sie nun über Braze Agents informiert sind, können Sie mit den nächsten Schritten fortfahren:

- [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Angepasste Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)