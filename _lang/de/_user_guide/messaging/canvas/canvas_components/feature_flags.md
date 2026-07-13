---
nav_title: Feature-Flag
article_title: Feature-Flag
page_order: 8
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Feature-Flags in Canvas verwendet werden können."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/messaging/feature_flags/create_feature_flags'
---

# Feature-Flag {#feature-flag}

> Feature-Flags ermöglichen es Ihnen, mit neuen Features zu experimentieren und Ihre Hypothesen zu bestätigen. Marketer können Feature-Flags nutzen, um Ihre Zielgruppe in [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) zu segmentieren und die Auswirkungen eines Feature-Rollouts auf Conversions zu verfolgen. Darüber hinaus ermöglichen [Experimentpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step#experiment-paths) die Optimierung dieser Conversions, indem verschiedene Nachrichten oder Pfade gegeneinander getestet werden, um herauszufinden, welcher am effektivsten ist. Nutzen Sie den Gewinnerpfad, während Sie Ihr Feature schrittweise für eine breitere Zielgruppe ausrollen.

Sie suchen nach weiteren Informationen zu Feature-Flags und wie sie in Braze verwendet werden können? Schauen Sie sich unsere speziellen [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags)-Artikel an.

## Ein Feature-Flag erstellen {#creating-a-feature-flag}

![Ein Beispiel für einen Feature-Flag-Schritt für das Feature „Live Chat Button“.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Um eine Feature-Flag-Komponente zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder klicken Sie auf den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und wählen Sie **Feature-Flag** aus. Wählen Sie anschließend das Feature-Flag aus dem Dropdown aus, das alle nicht archivierten Feature-Flags enthält.

## Wie dieser Schritt funktioniert {#how-this-step-works}

Wenn ein Canvas gestoppt oder archiviert wird oder ein Feature-Flag-Schritt entfernt wird, erhalten Nutzer:innen, die diesen Schritt durchlaufen haben, das Feature-Flag dieses Schritts und seine Eigenschaften nicht mehr.

Für ein Feature-Flag ohne Rollout und ohne Feature-Flag-Experiment gilt: Nachdem Sie ein Canvas stoppen, das einen Feature-Flag-Schritt enthält, der auf dieses Flag verweist:

- Keine Nutzer:innen haben dieses Feature-Flag im Tab **Feature Flags Eligibility**.
- Keine Nutzer:innen entsprechen dem Segmentierungsfilter `Feature Flags` für dieses Feature-Flag.

Wenn das Feature-Flag einen Rollout, ein Feature-Flag-Experiment oder ein anderes aktives Canvas hat, das darauf verweist, können Nutzer:innen weiterhin über diese Kanäle berechtigt sein.

Eigenschaften in einem Canvas-Schritt können nach dem Start geändert werden, auch nachdem eine Nutzerin oder ein Nutzer den Schritt durchlaufen hat. Nutzer:innen erhalten immer eine dynamische Realtime-Version des Feature-Flags anstatt der älteren, zuvor gespeicherten Version.

- **Zwei Canvases referenzieren dasselbe Feature-Flag, und eine Nutzerin oder ein Nutzer tritt in beide ein:** Die Person erhält den Wert, der im zuletzt betretenen Canvas festgelegt wurde, nicht den des früheren Canvas. Dieser Wert erscheint im Tab **Feature Flags Eligibility**.
- **Ein Canvas hat zwei Feature-Flag-Schritte, die dasselbe Feature-Flag referenzieren:** Die Person erhält den im zweiten Schritt festgelegten Wert, solange sie sich auf diesem Pfad befindet, und dieser Wert erscheint im Tab **Feature Flags Eligibility**.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

## Eigenschaften überschreiben {#overwriting-properties}

Beim Erstellen eines Feature-Flags legen Sie Standardeigenschaften fest. Beim Einrichten eines Feature-Flag-Canvas-Schritts können Sie entweder die Standardwerte beibehalten oder die Werte für Nutzer:innen überschreiben, die diesen Schritt betreten.

![Ein Feature-Flag „Preference Center“ mit „String“ als Eigenschaft, „url“ als Eigenschaftsschlüssel und einem Wert.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Gehen Sie zu **Messaging** > **Feature-Flags**, um zusätzliche Eigenschaften zu bearbeiten, hinzuzufügen oder zu entfernen.

## Unterschiede zwischen Canvas und Rollout {#canvas-and-rollout-differences}

Canvas und ein Feature-Flag-Rollout (Verschieben des Schiebereglers) können unabhängig voneinander funktionieren. Ein wichtiger Hinweis: Der Eintritt in einen Canvas-Schritt überschreibt jede Standard-Rollout-Konfiguration. Das bedeutet, wenn sich eine Nutzerin oder ein Nutzer nicht für ein Feature-Flag qualifiziert, kann ein Canvas-Schritt das Feature für diese Person aktivieren.

Ebenso gilt: Wenn sich eine Nutzerin oder ein Nutzer für einen Feature-Flag-Rollout mit bestimmten Eigenschaften qualifiziert und gleichzeitig in den Canvas-Schritt eintritt, erhält die Person die überschriebenen Werte aus diesem Canvas-Schritt.