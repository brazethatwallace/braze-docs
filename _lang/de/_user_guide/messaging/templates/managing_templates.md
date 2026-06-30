---
nav_title: Templates verwalten
article_title: Templates verwalten
page_order: 1

page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Templates im Bereich „Templates“ des Braze-Dashboards duplizieren und archivieren können."
tool:
  - Templates
  - Media

---

# Templates verwalten {#manage-templates}

> Das Archivieren oder Duplizieren von Templates kann dabei helfen, diese besser zu organisieren und zu verwalten. Dieser Referenzartikel beschreibt, wie Sie Templates im Abschnitt **Templates** des Braze-Dashboards archivieren und duplizieren können.

## Templates duplizieren {#duplicating-templates}

{% tabs %}
{% tab Einzelnes Template %}

![Dropdown-Menü mit der Option „Duplizieren“.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Um ein einzelnes Template zu duplizieren, wählen Sie <i class="fas fa-ellipsis-v"></i> **Weitere Optionen** für das Template aus und wählen Sie dann **Duplizieren** aus dem Dropdown-Menü.
<br><br>

{% alert note %}
Für [Content-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)-Templates wird ein Entwurf erstellt. Für alle anderen Templates wird automatisch eine neue Kopie erstellt.
{% endalert %}

{% endtab %}
{% tab Mehrere Templates %}

{% raw %}

Das Duplizieren mehrerer Templates ist möglich, indem Sie das Kontrollkästchen neben dem Template-Namen aktivieren. Wählen Sie zunächst die Templates aus und wählen Sie dann **Duplizieren**.

Duplizierte Templates können gefunden werden, indem Sie die Spalte **Zuletzt bearbeitet** sortieren. Standardmäßig werden neue Templates mit dem Namen `Copy of ORIGINAL_TEMPLATE_NAME` versehen.

{% endraw %}

![Drei Templates, sortiert nach dem Zeitpunkt der letzten Bearbeitung, mit einem kopierten Template am Anfang der Liste.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

{% endtab %}
{% endtabs %}

## Templates archivieren {#archiving-templates}

![Aufgeklapptes Einstellungs-Dropdown-Menü mit drei Optionen: „Archivieren“, „Duplizieren“ und „In Workspace kopieren“, wobei die Option „Archivieren“ hervorgehoben ist.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

Um ein einzelnes Template zu archivieren, wählen Sie <i class="fas fa-ellipsis-v"></i> **Weitere Optionen** auf dem Template-Raster aus und wählen Sie **Archivieren**. Wenn ein Template archiviert wird, beachten Sie die folgenden Szenarien:

- Aktive Campaigns verwenden das archivierte Template weiterhin ohne Unterbrechung.
- Entwürfe von Campaigns behalten den Inhalt des archivierten Templates bei und können bearbeitet und gestartet werden.
- Um ein archiviertes Template zu bearbeiten, müssen Sie es zuerst aus dem Archiv wiederherstellen. Ebenso müssen Sie ein archiviertes Template zuerst aus dem Archiv wiederherstellen, um es für eine Campaign zu verwenden.

Um mehrere Templates zu archivieren, aktivieren Sie das Kontrollkästchen neben jedem Template, das Sie archivieren möchten. Nachdem Sie mehrere Templates ausgewählt haben, wählen Sie **Archivieren**. Sie finden Ihre archivierten Templates, indem Sie im Template-Raster unter **Anzeigen** die Option **Archiviert** auswählen.

![Abschnitt „Gespeicherte Drag-&-Drop-E-Mail-Templates“ mit zwei ausgewählten Templates und einer Symbolleiste mit der Option zum Archivieren.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
Das Archivieren ist derzeit nicht für [Link-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing#link-templates) verfügbar.
{% endalert %}