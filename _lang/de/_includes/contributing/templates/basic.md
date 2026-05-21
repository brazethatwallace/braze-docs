Sie können dieses Template verwenden, um eine beliebige Seite oder einen beliebigen Abschnitt für Braze Docs zu erstellen. Informationen zur Einrichtung der Umgebung, zu Vorschauen und Inhaltstypen finden Mitwirkende mit repo-Zugang im Handbuch unter `docs/contributing/` (zum Beispiel `generating_a_preview.md` und `content_types.md`). Alle anderen können über [Dokumentations-Feedback]({{site.baseurl}}/feedback/) das Docs-Team erreichen.

{% details Template anzeigen %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
---

<!-- Der Titel Ihrer Seite, der als Seitentitel gerendert wird. -->
# ARTICLE_TITLE

<!-- Die Übersicht beginnt mit einem '>'-Zeichen und beschreibt, was behandelt wird. In einem optionalen folgenden Absatz wird das Thema auf einer übergeordneten Ebene in einer Einleitung kontextualisiert. -->
> DESCRIPTION.

INTRODUCTION.

<!-- Die Voraussetzungen für diese Aufgabe. Wenn keine Voraussetzungen erforderlich sind, können Sie diesen Abschnitt entfernen. -->
## Voraussetzungen

Vor dem Start müssen Sie Folgendes abschließen:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- Eine optionale, kurze Erklärung, wie der Feature-Workflow aussieht. -->
## So funktioniert es

CONTENT.

<!-- Führen Sie Nutzer:innen durch die Integration und Aktivierung des Features. -->
 ## Integration
CONTENT.

<!-- Eine Schritt-für-Schritt-Anleitung mit verschachtelten Schritten. -->
## TASK_TO_COMPLETE

<!-- Optionale Übersicht der Aufgabe. -->
CONTENT.

<!-- Aktionsorientierte Überschrift, die das Ziel des Schritts beschreibt. -->
### 1. Schritt: ACTION_TO_COMPLETE

<!-- Verwenden Sie nummerierte Aufzählungen oder Absätze, um zu beschreiben, wie diese Aktion abgeschlossen wird. -->
CONTENT.

### 2. Schritt: ACTION_TO_COMPLETE

CONTENT.
<!-- Optionale Referenzen, wie unterstützte Datentypen, Felder, Definitionen und Ähnliches. -->
### REFERENCE_TO_ASSIST_WITH_ACTION

CONTENT.

<!-- Fügen Sie bei optionalen Schritten „(optional)“ am Ende der Überschrift hinzu. -->
### 3. Schritt: OPTIONAL_ACTION_TO_COMPLETE (optional)

CONTENT.
<!-- Ein optionaler Abschnitt für unterstützte Elemente. Fügen Sie verschachtelte Überschriften hinzu, um spezifischer zu sein. -->
## Unterstützte Datentypen / Unterstützte Attribute / Unterstützte Ereignisse / Unterstützte ETC.
CONTENT.
<!-- Ein optionaler Abschnitt mit wichtigen Hinweisen, die Nutzer:innen vor der Verwendung des Features beachten sollten. -->
## Hinweise

CONTENT.

<!-- Ein optionaler Abschnitt, der Nutzer:innen bei der Fehlerbehebung häufiger Probleme unterstützt. -->
## Fehlerbehebung

### ISSUE_TO_TROUBLESHOOT
CONTENT.

`````
{% endraw %}
{% enddetails %}