---
nav_title: Agentenkonsole
article_title: "Braze Agents in der Agentenkonsole"
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

## Warum Braze Agents verwenden? {#why-use-braze-agents}

Braze Agents helfen Ihrem Team, intelligentere, stärker personalisierte Erlebnisse zu schaffen – ohne zusätzlichen Aufwand. Sie agieren als autonome Agenten, die nicht nur auf Prompts reagieren, sondern Kontext verstehen, Entscheidungen treffen und zielgerichtet handeln.

In der Praxis können Agenten automatisch Nachrichtentexte erstellen – wie Betreffzeilen oder In-Product-Texte –, sodass jede Kundin und jeder Kunde eine Kommunikation erhält, die sich individuell zugeschnitten anfühlt. Sie können sich auch in Echtzeit anpassen und Nutzer:innen basierend auf Präferenzen, Verhalten oder anderen Daten durch verschiedene Canvas-Pfade leiten.

Über Messaging hinaus können Agenten Ihre Kataloge anreichern, indem sie Produkt- und Profilfeldwerte berechnen oder generieren und so Ihre Daten aktuell und dynamisch halten. Indem sie sich wiederholende oder komplexe Aufgaben übernehmen, geben sie Ihrem Team die Freiheit, sich auf Strategie und Kreativität zu konzentrieren, anstatt auf manuelle Einrichtung. Braze Agents agieren eher wie Mitarbeitende als wie Hintergrundprozesse – sie helfen Ihnen, Probleme zu lösen und skalierbar Wirkung zu erzielen.

### Wann Sie Braze Agents im Vergleich zu anderen BrazeAI-Features verwenden sollten {#when-to-use-braze-agents-versus-other-brazeai-features}

Verwenden Sie Agenten, um Inhalte spontan mithilfe des spezifischen Kontexts einer Nutzerin oder eines Nutzers zu personalisieren. Wenn ein Agent beispielsweise weiß, dass die Lieblingseissorte einer bestimmten Nutzerin Schokolade ist und ihr bevorzugtes Topping Gummibärchen, kann er Push-Texte erstellen, die genau auf diese Kombination zugeschnitten sind, während die Nutzerin den Canvas durchläuft.

Der Agent lernt jedoch nicht durch Versuch und Irrtum und hat keine Vorstellung von einem übergeordneten Marketingziel, das er messen und maximieren möchte. Selbst wenn Sie ihm sagen, dass er generell Texte schreiben soll, die Konversionen fördern, hat er keinen Mechanismus, um die Auswirkungen seines agentischen Schreibens auf Konversionen zu „überwachen“ und diese Daten in zukünftige agentische Aufrufe einfließen zu lassen. Sie können sich das als „Vibe“-Entscheidungsfindung vorstellen, nicht als belohnungsbasiertes KI-Decisioning.

Im Gegensatz dazu sind andere BrazeAI-Tools darauf ausgelegt, die Metriken zu maximieren, die sie messen. Agenten sind beispielsweise sehr gut darin, qualitativ zu bewerten, wie die Eigenschaften einer Nutzerin oder eines Nutzers die Wahrscheinlichkeit oder Neigung beeinflussen, ein bestimmtes Ereignis auszuführen oder ein bestimmtes Produkt zu mögen. Da der Agent jedoch nicht durch Versuch und Irrtum lernt, hat er keine Möglichkeit, die Genauigkeit seiner Wahrscheinlichkeitsprognosen zu messen und das Signal im Laufe der Zeit zu verbessern. Daher übertrifft die Predictive Suite den Agent-Schritt, wenn es um die Genauigkeit der Prognosen und deren Verbesserung im Laufe der Zeit geht.

## Features {#features}

Features für Braze Agents umfassen:

- **Flexible Einrichtung:** Verwenden Sie ein von Braze bereitgestelltes LLM oder verbinden Sie Ihre eigenen [KI-Modellanbieter]({{site.baseurl}}/partners/ai_model_providers) (wie OpenAI, Anthropic, Google Gemini oder Databricks Mosaic).
- **Nahtlose Integration:** Stellen Sie Agenten direkt in Canvas-Schritten oder Katalogfeldern bereit.
- **Testen, Protokollierung und Versionsverlauf:** Zeigen Sie eine Vorschau der Ausgabe Ihres Agenten an, indem Sie vor dem Start mit Beispiel-Eingaben testen. Sehen Sie sich Protokolle für jede Ausführung des Agenten ein, einschließlich der Ein- und Ausgabe für diesen Durchlauf. Verwenden Sie den Tab **Versionsverlauf**, um frühere Versionen und Inline-Vergleiche von Anweisungsänderungen zu überprüfen.
- **Nutzungskontrollen:** Tägliche Limits helfen, Performance und Kosten zu verwalten.

## Über Braze Agents {#about-braze-agents}

Agenten werden mit Anweisungen (Systemprompts) konfiguriert, die ihr Verhalten definieren. Wenn ein Agent ausgeführt wird, verwendet er Ihre Anweisungen zusammen mit allen Daten, die Sie explizit übergeben, um eine Antwort zu generieren. Er kann nicht auf Nutzerdaten zugreifen, die über Ihre Konfiguration hinausgehen – Liquid-Variablen, Agent-Kontext-Auswahlen, Canvas-Kontextvariablen und Kontextschritt-Werte. Agenten durchsuchen keine Profile und warnen nicht, wenn Daten fehlen. Siehe [Welche Daten Agenten erhalten]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

### Schlüsselkonzepte {#key-concepts}

| Begriff | Definition |
| --- | --- |
| [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) | Das „Gehirn“ des Agenten – in diesem Fall ein Large Language Model (LLM). Es interpretiert Eingaben, generiert Antworten und führt Schlussfolgerungen durch. Ein stärkeres Modell (trainiert mit relevanteren Daten) macht den Agenten leistungsfähiger und vielseitiger. |
| [Anweisungen]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) | Die Regeln oder Richtlinien, die Sie dem Agenten geben (Systemprompt). Sie definieren, wie sich der Agent bei jeder Ausführung verhalten soll. Klare Anweisungen machen den Agenten zuverlässiger und vorhersehbarer. |
| Kontext | Daten, die dem Agenten zur Laufzeit übergeben werden – unabhängig davon, wo er bereitgestellt wird – wie z. B. Nutzerprofilfelder oder Katalogreihen. Diese Eingaben liefern die Informationen, die der Agent zur Generierung von Ausgaben verwendet. |
| [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#how-context-variables-work) | Temporäre Datenstücke, die Sie innerhalb der Journey einer Nutzerin oder eines Nutzers durch ein bestimmtes Canvas erstellen und verwenden können. |
| [Ausgabevariable]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#define-the-output-variable) | Die Ausgabe, die der Agent erzeugt, wenn er in Canvas-Schritten verwendet wird. Ausgabevariablen speichern das Ergebnis des Agenten, um Inhalte zu personalisieren oder Workflow-Pfade zu steuern. Ausgabevariablen können den Datentyp String, Zahl oder Boolean haben. |
| [Aufruf](#limitations) | Eine einzelne Ausführung des Agenten. Dies wird auf Ihre täglichen Limits angerechnet. |
| [Ausgabeformat]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#select-output) | Die vordefinierte Datenstruktur der Antwort des Agenten. |
| [Wissensquellen]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) | Eine Art von Agentenkontext, mit dem Daten aus einem Katalog genauer abgerufen werden können, als wenn der Katalog direkt in den Anweisungen des Agenten referenziert wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schlüsselkonzepte" }

## Einschränkungen {#limitations}

Die folgenden Einschränkungen gelten:

- Jeder Agent hat ein standardmäßiges tägliches Aufruf-Limit von 250.000 Durchläufen, das auf maximal 1.000.000 Durchläufe pro Tag erhöht werden kann. Kontaktieren Sie Ihren Customer-Success-Manager, wenn Sie dieses Limit erhöhen möchten.
- Die Agent Console zeigt für jeden Agenten ein **Tägliches Aktions-Credit-Kostenlimit** an – die geschätzten maximalen Credits pro Tag basierend auf dem Credit-Verhältnis pro Aufruf Ihres Modells und dem täglichen Aufruf-Limit. Siehe [Tägliche Aufruf- und Credit-Limits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Standardmäßig muss jeder Durchlauf innerhalb von 20 Sekunden abgeschlossen sein. Nach 20 Sekunden gibt der Agent eine `null`-Antwort zurück, wo immer er eingesetzt wird.
    - Wenn Ihre Agenten regelmäßig ein Timeout erreichen, kontaktieren Sie Ihren Braze Account Manager, um dieses Limit zu erhöhen.
- Eingabedaten sind auf 25 KB pro Anfrage begrenzt. Längere Eingaben werden abgeschnitten.

## Best Practices {#best-practices}

Setzen Sie auf hochwertige Anwendungsfälle, bei denen Agenten die größte Kapitalrendite (ROI) erzielen können, und wählen Sie Zielgruppen, die wahrscheinlich reagieren. Eine kleinere Zielgruppe mit hoher Opportunity übertrifft oft eine große Zielgruppe mit geringer Opportunity – zum Beispiel das Retargeting von Nutzer:innen, die kürzlich gesucht, aber keine Konversion durchgeführt haben, anstatt agentengenerierte Texte an Ihre gesamte Nutzerbasis zu senden.

Um die ROI vor der Skalierung zu validieren, verwenden Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt, um nur einen Teil Ihrer Zielgruppe durch einen Agent-Schritt zu senden. Wenn ein Test im kleinen Maßstab gute Ergebnisse zeigt, skalieren Sie den Agenten auf Ihre vollständige Zielgruppe und erhöhen Sie das [tägliche Aufruf-Limit]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits), damit Aufrufe nicht mitten im Versand begrenzt werden. Vergewissern Sie sich, dass Sie mit dem geschätzten Credit-Verbrauch einverstanden sind, bevor Sie auf Ihre vollständige Zielgruppe skalieren. Weitere Hinweise zur Bereitstellung finden Sie unter [Angepasste Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Fehlerbehandlung {#error-handling}

Wenn das verbundene Modell während eines Canvas-Schritt-Agent- oder Katalog-Agent-Aufrufs einen [Rate-Limit-Fehler]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) des LLM-Anbieters zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff.

Bei anderen Fehlern (z. B. einem Timeout oder einem ungültigen API-Schlüssel) wird die Ausgabe des Canvas-Schritt-Agents auf `null` gesetzt, es sei denn, der Agent verfügt über [konfigurierte Fallback-Werte]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in der Agent Console (nur Canvas-Schritt-Agents). Katalog-Agents wiederholen Fehler, die keine Rate-Limit-Fehler sind, nicht. Wenn ein Agent sein tägliches Aufruflimit erreicht, wendet Braze die konfigurierten Fallback-Werte an, sofern vorhanden; andernfalls wird die Ausgabe auf `null` gesetzt.

Rate-Limit-Fehler, Modellunverfügbarkeit und Fehler durch Erreichen des täglichen Aufruflimits verbrauchen keine Braze-Credits. Timeouts verbrauchen Credits. Siehe [Wann Credits verbraucht werden]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

Wenn viele Nutzer:innen gleichzeitig einen Agent-Schritt betreten, kann die Verarbeitung aufgrund von [Aufruf-Flow-Controls]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls) länger dauern. Konfigurieren Sie Fallback-Werte in der Agent Console für Canvas-Schritt-Agents, damit Nutzer:innen auch dann eine Ausgabe erhalten, wenn ein Aufruf fehlschlägt, oder verwenden Sie [Standard-Liquid-Werte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) in nachgelagerten Nachrichten-Schritten.

## Wie werden meine Daten verwendet und an von Braze bereitgestellte LLMs gesendet? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Um KI-Ausgaben über Braze-KI-Features zu generieren, die Braze als von Braze bereitgestellte LLMs nutzend kennzeichnet („Ausgabe“), sendet Braze Ihren System-Prompt oder andere Eingaben, soweit zutreffend („Eingabe“), an das von Braze bereitgestellte LLM. Daten, die an das jeweilige von Braze bereitgestellte LLM gesendet werden, werden nicht zum Trainieren oder Verbessern des von Braze bereitgestellten LLMs verwendet. Zwischen Ihnen und Braze ist die Ausgabe Ihr geistiges Eigentum. Braze erhebt keine Urheberrechtsansprüche auf solche Ausgaben. Braze übernimmt keinerlei Gewährleistung in Bezug auf KI-generierte Inhalte im Allgemeinen, einschließlich der Ausgabe.

Das von Braze bereitgestellte LLM für Braze Agents, gekennzeichnet als „Auto“, verwendet Google-Gemini-Modelle. Google speichert Eingaben und Ausgaben, die über Braze übermittelt werden, für 55 Tage, danach werden die Daten gelöscht.

## Nächste Schritte {#next-steps}

Jetzt, da Sie Braze Agents kennen, sind Sie bereit für die nächsten Schritte:

- [Angepasste Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [Angepasste Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)