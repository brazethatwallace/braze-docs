---
nav_title: Canvas-Versionsverlauf
article_title: Canvas-Versionsverlauf
alias: "/canvas_version_history/"
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie Ihren Canvas-Versionsverlauf verwalten."
page_type: reference
tool: Canvas
---

# Canvas-Versionsverlauf {#canvas-version-history}

> Der Versionsverlauf ermöglicht es Ihnen, Canvas-Analytics und die Nutzer:innen-Journeys für jede frühere Version Ihres Canvas einzusehen und darauf zuzugreifen.

Das Referenzieren Ihres Canvas-Versionsverlaufs kann besonders hilfreich sein, um die Entwicklung eines Canvas nachzuverfolgen. Wenn Sie beispielsweise eine umfangreiche Änderung vornehmen, können Sie frühere Canvas-Versionen referenzieren, um besser zu verstehen, wie sich Ihre Workflows entwickelt haben.

{% alert tip %}
Für eine vollständige Liste der Canvases in Ihrem Workspace (z. B. für ein Audit) verwenden Sie den [Endpunkt „Canvas-Liste exportieren“]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) und blättern Sie durch die Ergebnisse.
{% endalert %}

## Versionen verwalten {#managing-versions}

![Screenshot zur Verwaltung von Versionen.]({% image_buster /assets/img_archive/canvas_version_history.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Um eine neue Version zu erstellen, klicken Sie auf **Canvas aktualisieren**. So können Sie Änderungen vornehmen, ohne das vorherige Setup des Canvas zu überschreiben. Wenn eine neue Canvas-Version erstellt wird, durchlaufen die Nutzer:innen, die sich bereits im Canvas befinden, den Workflow der neuen Version. Nutzer:innen, die den Canvas betreten, gelangen ebenfalls in die neue Version.

Um auf den Versionsverlauf zuzugreifen, navigieren Sie zu den Canvas-Details oben in Ihrem Canvas und wählen Sie **# Versions** aus. Hier haben Sie Zugriff auf die Seitenleiste **Version history**. Wählen Sie eine beliebige Canvas-Version in der Seitenleiste aus, um Canvas-Details einzusehen und zu vergleichen. Um zwischen den Canvas-Analytics und dem Canvas-Setup zu wechseln, klicken Sie auf **Analytics anzeigen** oder **Canvas anzeigen** in der unteren Symbolleiste.

{% alert note %}
Canvases, die unter **Version history** aufgeführt sind, können nur angezeigt werden.
{% endalert %}

Um eine Liste der Änderungen anzuzeigen, die an einer Version vorgenommen wurden, während sie aktiv war, wählen Sie **View Changes** in der Seitenleiste des Versionsverlaufs aus. Sie können auch alle mit einer Version verbundenen Änderungen im Canvas-Changelog einsehen.

Beachten Sie: Wenn Sie zwischen dem Starten eines Canvas und dem Erstellen einer zweiten Version keine Bearbeitungen vorgenommen haben, werden unter **See Changes** für die erste Version des Canvas keine Änderungen angezeigt.

Wenn Ihr Versionsverlauf wächst, können Sie jede Version in der Seitenleiste umbenennen, um den Überblick zu behalten. Standardmäßig werden Versionsnamen als Nummer basierend auf der Anzahl der zuvor erstellten Versionen generiert. Wenn Sie eine Version umbenennen, die nicht mehr aktiv ist, wird dies im Canvas-Changelog angezeigt, aber nicht im Changelog der Version innerhalb der Versionsverlaufsansicht.

![Beispiel eines Canvas-Changelogs, das zeigt, dass zwei neue Canvas-Versionen erstellt wurden.]({% image_buster /assets/img_archive/canvas_version_history_changelog.png %}){: style="max-width:85%" }

### Versionen verwerfen {#discarding-versions}

Sie können bis zu 10 Versionen pro Canvas erstellen. Wenn Sie dieses Limit erreichen, können Sie eine Version verwerfen, um Platz für eine neue zu schaffen. Beachten Sie, dass Versionen beim Klicken auf **Discard** verworfen werden, nicht wenn Sie den Canvas aktualisieren. Das Verwerfen einer Version wird im übergeordneten Canvas-Changelog erfasst, nicht im Changelog einer bestimmten Version.

Wenn Sie eine Version verwerfen, geht das Canvas-Setup sofort verloren, aber die mit der verworfenen Version verbundenen Analytics werden beibehalten.

## Analytics anzeigen {#viewing-analytics}

Innerhalb des Versionsverlaufs können Sie Analytics auf Canvas-Ebene und auf Step-Ebene einsehen. In der Canvas-Versionsansicht werden die Daten für den gesamten Datumsbereich angezeigt, nicht nur für den Datumsbereich dieser Version. Auf Step-Ebene werden Analytics jedoch nur für Steps angezeigt, die existierten, während diese Version aktiv war. Diese Analytics werden anhand von Kalendertagen berechnet, die der Zeitzone Ihres Unternehmens entsprechen, sodass die Analytics nicht auf den genauen Zeitpunkt der Versionserstellung bezogen sind.