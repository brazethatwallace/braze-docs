---
nav_title: Agentenkonsole
article_title: "Braze Agents in der Agentenkonsole"
page_order: 1
description: "Braze Agents können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, damit Sie personalisiertere Kundenerlebnisse bieten können."
---

# Braze Agents in der Agentenkonsole {#braze-agents-in-agent-console}

> Braze Agents sind KI-gestützte Assistenten, die Sie innerhalb von Braze erstellen können. Agenten können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, damit Sie personalisiertere Kundenerlebnisse bieten können.

{% alert important %}
Für den Zugriff auf und die Nutzung von Braze Agents sind Nachrichten- oder Aktionsguthaben erforderlich. Sollten Sie derzeit nicht über Aktionsguthaben verfügen und Braze Agents nutzen möchten, wenden Sie sich an Ihren Account Manager:in, um die nächsten Schritte zu besprechen.
{% endalert %}

Sehen Sie sich dieses Video an, um einen Überblick über Braze Agents in der Agentenkonsole zu erhalten.

{% multi_lang_include video.html id="afd0hp0vrh" source="wistia" title="Braze Agents in Agent Console overview" %}

## Warum Braze Agents nutzen? {#why-use-braze-agents}

Braze Agents helfen Ihrem Team, intelligentere und stärker personalisierte Erlebnisse zu schaffen – ohne zusätzlichen Aufwand. Sie fungieren als autonome Agenten, die nicht nur auf Eingaben reagieren, sondern Kontext verstehen, Entscheidungen treffen und zielgerichtet handeln.

In der Praxis können Agenten automatisch Nachrichtentexte erstellen – wie Betreffzeilen oder In-Product-Texte – sodass jede:r Kund:in eine Kommunikation erhält, die sich individuell zugeschnitten anfühlt. Sie können sich auch in Echtzeit anpassen und Nutzer:innen basierend auf Präferenzen, Verhaltensweisen oder anderen Daten durch verschiedene Canvas-Pfade leiten.

Über Messaging hinaus können Agenten Ihre Kataloge anreichern, indem sie Produkt- und Profilfeldwerte berechnen oder generieren und so Ihre Daten aktuell und dynamisch halten. Indem sie repetitive oder komplexe Aufgaben übernehmen, geben sie Ihrem Team den Freiraum, sich auf Strategie und Kreativität zu konzentrieren, anstatt auf manuelle Einrichtung. Braze Agents agieren dabei eher wie Kolleg:innen als wie Hintergrundprozesse – sie helfen Ihnen, Probleme zu lösen und Wirkung in großem Maßstab zu erzielen.

### Wann Braze Agents im Vergleich zu anderen BrazeAI-Features einsetzen? {#when-to-use-braze-agents-versus-other-brazeai-features}

Verwenden Sie Agenten, um Inhalte spontan auf Basis des spezifischen Kontexts von Nutzer:innen zu personalisieren. Wenn ein Agent beispielsweise weiß, dass die Lieblingssorte Eiscreme einer bestimmten Nutzerin Schokolade ist und ihr Lieblingstopping Gummibärchen, kann er Push-Texte erstellen, die genau auf diese Kombination für diese Nutzerin zugeschnitten sind, während sie den Canvas durchläuft.

Allerdings lernt der Agent nicht durch Versuch und Irrtum, und er kennt kein übergeordnetes Marketingziel, das er messen und maximieren möchte. Selbst wenn Sie ihn anweisen, generell Texte zu schreiben, die Konversionen fördern, hat er keinen Mechanismus, um die Konversionsauswirkungen seiner agentengestützten Texterstellung zu „überwachen“ und diese Daten in zukünftige Agentenaufrufe einfließen zu lassen. Sie können sich das als „instinktbasierte“ Entscheidungsfindung vorstellen, nicht als belohnungsbasiertes KI-Decisioning.

Im Gegensatz dazu sind andere BrazeAI-Tools darauf ausgelegt, die Metriken zu maximieren, die sie messen. Agenten sind beispielsweise sehr gut darin, qualitativ zu bewerten, wie die Eigenschaften von Nutzer:innen deren Wahrscheinlichkeit oder Affinität beeinflussen, ein bestimmtes Ereignis auszuführen oder ein bestimmtes Produkt zu mögen. Da der Agent jedoch nicht durch Versuch und Irrtum lernt, weiß er nicht, wie er die Genauigkeit seiner Wahrscheinlichkeitsvorhersagen messen und das Signal im Laufe der Zeit verbessern kann. Daher übertrifft die Predictive Suite den Agent-Schritt, wenn man die Genauigkeit der Prognosen und deren Verbesserung im Zeitverlauf als Maßstab heranzieht.

## Features {#features}

Features für Braze Agents umfassen:

- **Flexible Einrichtung:** Verwenden Sie ein von Braze bereitgestelltes LLM oder verbinden Sie Ihre eigenen [KI-Modellanbieter]({{site.baseurl}}/partners/ai_model_providers) (wie OpenAI, Anthropic, Google Gemini oder Databricks Mosaic).
- **Nahtlose Integration:** Stellen Sie Agenten direkt in Canvas-Schritten oder Katalogfeldern bereit.
- **Testen, Protokollieren und Verlauf:** Zeigen Sie eine Vorschau der Ausgabe Ihres Agenten an, indem Sie ihn vor dem Start mit Beispieleingaben testen. Sehen Sie sich die Protokolle für jeden Ausführungszeitpunkt des Agenten ein, einschließlich der Ein- und Ausgabe für diesen Durchlauf. Verwenden Sie den Tab **Version history**, um frühere Versionen und Inline-Diffs von Anweisungsänderungen zu überprüfen.
- **Nutzungskontrollen:** Tägliche Limits helfen bei der Verwaltung von Performance und Kosten.

## Über Braze Agents {#about-braze-agents}

Agenten werden mit Anweisungen (Systemprompts) konfiguriert, die ihr Verhalten definieren. Wenn ein Agent ausgeführt wird, nutzt er Ihre Anweisungen zusammen mit allen Daten, die Sie explizit übergeben, um eine Antwort zu generieren. Er kann nicht auf Nutzerdaten zugreifen, die über das hinausgehen, was Sie konfigurieren – Liquid-Variablen, Agentenkontext-Auswahlen, Canvas-Kontextvariablen und Kontextschritt-Werte. Agenten durchsuchen keine Profile und warnen nicht, wenn Daten fehlen. Siehe [Welche Daten Agenten erhalten]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive).

### Schlüsselkonzepte {#key-concepts}

| Begriff | Definition |
| --- | --- |
| [Modell]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) | Das „Gehirn“ des Agenten – in diesem Fall ein Large Language Model (LLM). Es interpretiert Eingaben, generiert Antworten und führt Schlussfolgerungen durch. Ein stärkeres Modell (das mit mehr relevanten Daten trainiert wurde) macht den Agenten leistungsfähiger und vielseitiger. |
| [Anweisungen]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions) | Die Regeln oder Richtlinien, die Sie dem Agenten geben (Systemprompt). Sie definieren, wie sich der Agent bei jeder Ausführung verhalten soll. Klare Anweisungen machen den Agenten zuverlässiger und vorhersehbarer. |
| Kontext | Daten, die dem Agenten zur Laufzeit übergeben werden – unabhängig davon, wo er bereitgestellt wird –, z. B. Nutzerprofilfelder oder Katalogreihen. Diese Eingaben liefern die Informationen, die der Agent zur Generierung seiner Ausgaben verwendet. |
| [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#how-context-variables-work) | Temporäre Datenwerte, die Sie innerhalb der Journey einer Nutzerin oder eines Nutzers durch ein bestimmtes Canvas erstellen und verwenden können. |
| [Ausgabevariable]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step#define-the-output-variable) | Die Ausgabe, die der Agent erzeugt, wenn er in Canvas-Schritten verwendet wird. Ausgabevariablen speichern das Ergebnis des Agenten, um Inhalte zu personalisieren oder Workflow-Pfade zu steuern. Ausgabevariablen können den Datentyp String, Zahl oder Boolean haben. |
| [Aufruf](#limitations) | Eine einzelne Ausführung des Agenten. Dies wird auf Ihre täglichen Limits angerechnet. |
| [Ausgabeformat]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#select-output) | Die vordefinierte Datenstruktur der Antwort des Agenten. |
| [Wissensquellen]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources) | Eine Art von Agentenkontext, die verwendet wird, um Daten aus einem Katalog genauer abzurufen, als wenn der Katalog direkt in den Anweisungen des Agenten referenziert wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schlüsselkonzepte" }

## Einschränkungen {#limitations}

Es gelten die folgenden Einschränkungen:

- Jeder Agent hat ein standardmäßiges tägliches Aufruf-Limit von 250.000 Durchläufen, das auf maximal 1.000.000 Durchläufe pro Tag erhöht werden kann. Wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie dieses Limit erhöhen möchten.
- Die Agent Console zeigt für jeden Agenten ein **Tägliches Aktions-Credit-Kostenlimit** an – die geschätzten maximalen Credits pro Tag basierend auf dem Credit-Verhältnis pro Aufruf Ihres Modells und dem täglichen Aufruf-Limit. Siehe [Tägliche Aufruf- und Credit-Limits]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).
- Standardmäßig muss jeder Durchlauf innerhalb von 20 Sekunden abgeschlossen sein. Nach 20 Sekunden gibt der Agent eine `null`-Antwort zurück, wo immer er eingesetzt wird.
    - Wenn Ihre Agenten regelmäßig ein Timeout erreichen, wenden Sie sich an Ihren Braze Account Manager, um dieses Limit zu erhöhen.
- Eingabedaten sind auf 25 KB pro Anfrage begrenzt. Längere Eingaben werden abgeschnitten.

## Best Practices {#best-practices}

Setzen Sie auf Anwendungsfälle mit hohem Wert, bei denen Agenten die größte Kapitalrendite (ROI) erzielen können, und wählen Sie Zielgruppen, die voraussichtlich reagieren werden. Eine kleinere Zielgruppe mit hohem Potenzial übertrifft oft eine große Zielgruppe mit geringem Potenzial – zum Beispiel ein Retargeting von Nutzer:innen, die kürzlich gesucht, aber nicht konvertiert haben, anstatt vom Agenten generierte Texte an Ihre gesamte Nutzerbasis zu senden.

Um den ROI vor der Skalierung zu validieren, verwenden Sie einen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step)-Schritt, um nur einen Teil Ihrer Zielgruppe durch einen Agent-Schritt zu leiten. Wenn ein Test im kleinen Maßstab vielversprechend aussieht, skalieren Sie den Agenten auf Ihre vollständige Zielgruppe und erhöhen Sie das [tägliche Aufruf-Limit]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits), damit Aufrufe nicht mitten im Versand gedeckelt werden. Vergewissern Sie sich, dass Sie mit dem geschätzten Credit-Verbrauch einverstanden sind, bevor Sie auf Ihre gesamte Zielgruppe skalieren. Weitere Hinweise zur Bereitstellung finden Sie unter [Angepasste Agenten bereitstellen]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents).

## Fehlerbehandlung {#error-handling}

Wenn das verbundene Modell während eines Canvas-Schritt-Agent- oder Katalog-Agent-Aufrufs einen [Rate-Limit-Fehler]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors) vom LLM-Anbieter zurückgibt, wiederholt Braze die Anfrage kontinuierlich mit exponentiellem Backoff.

Bei anderen Fehlern (z. B. Timeout oder ungültiger API-Schlüssel) wird die Ausgabe des Canvas-Schritt-Agents auf `null` gesetzt, sofern der Agent keine [konfigurierten Fallback-Werte]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values) in der Agent Console hat (nur Canvas-Schritt-Agents). Katalog-Agents wiederholen Fehler, die nicht auf Rate-Limits zurückzuführen sind, nicht. Wenn ein Agent sein tägliches Aufruflimit erreicht, wendet Braze konfigurierte Fallback-Werte an, sofern vorhanden; andernfalls wird die Ausgabe auf `null` gesetzt.

Rate-Limit-Fehler, Nichtverfügbarkeit des Modells und Fehler durch das tägliche Aufruflimit verbrauchen keine Braze-Credits. Timeouts verbrauchen Credits. Siehe [Wann Credits verbraucht werden]({{site.baseurl}}/user_guide/brazeai/agents/reference#when-credits-are-consumed).

Wenn viele Nutzer:innen gleichzeitig einen Agent-Schritt betreten, kann die Verarbeitung aufgrund von [Aufruf-Flusskontrollen]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls) länger dauern. Konfigurieren Sie Fallback-Werte in der Agent Console für Canvas-Schritt-Agents, damit Nutzer:innen auch dann eine Ausgabe erhalten, wenn ein Aufruf fehlschlägt, oder verwenden Sie [Standard-Liquid-Werte]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) in nachgelagerten Nachrichtenschritten.

## Wie werden meine Daten verwendet und an von Braze bereitgestellte LLMs gesendet? {#how-is-my-data-used-and-sent-to-braze-provided-llms}

Um KI-Ausgaben über Braze-KI-Features zu generieren, die Braze als von Braze bereitgestellte LLMs nutzend identifiziert („Ausgabe“), sendet Braze Ihren Systemprompt oder andere Eingaben, sofern zutreffend („Eingabe“), an das von Braze bereitgestellte LLM. Daten, die an das jeweilige von Braze bereitgestellte LLM gesendet werden, werden nicht zum Trainieren oder Verbessern des von Braze bereitgestellten LLMs verwendet. Zwischen Ihnen und Braze ist die Ausgabe Ihr geistiges Eigentum. Braze wird keine urheberrechtlichen Eigentumsansprüche an solchen Ausgaben geltend machen. Braze übernimmt keinerlei Gewährleistung in Bezug auf KI-generierte Inhalte im Allgemeinen, einschließlich der Ausgabe.

Das von Braze bereitgestellte LLM für Braze Agents, als „Auto“ gekennzeichnet, verwendet Google-Gemini-Modelle. Google speichert über Braze übermittelte Eingaben und Ausgaben für 55 Tage, danach werden die Daten gelöscht.

## Nächste Schritte {#next-steps}

Jetzt, da Sie Braze Agents kennen, sind Sie bereit für die nächsten Schritte:

{% article_tiles %}
- name: Angepasste Agenten erstellen
  link: /docs/user_guide/brazeai/agents/creating_agents
- name: Angepasste Agenten bereitstellen
  link: /docs/user_guide/brazeai/agents/deploying_agents
{% endarticle_tiles %}