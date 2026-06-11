{% if include.location == "dnd" %}

1. Gehen Sie zu **Content** > **Content Block**. Wählen Sie <i class="fas fa-plus"></i> **Create Content Block** und dann **Drag-and-drop Content Block** aus.
2. Ziehen Sie die [Editor-Blöcke]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) per Drag-and-Drop, um einen Drag-and-Drop-Content-Block zu erstellen.
3. Ziehen Sie einen Formatblock aus dem Tab **Rows** per Drag-and-Drop in den Editor, um das Layout Ihres Content-Blocks zu erstellen. <br><br> ![Drag-and-Drop-Content-Block-Composer.]({% image_buster /assets/img_archive/dnd_content_block_composer.png %})<br><br>
4. Fügen Sie bei Bedarf Drag-and-Drop-Content-Blöcke hinzu, um Ihre E-Mail-Campaigns aufzubauen.
5. Nachdem Sie Ihren Content-Block erstellt haben, wählen Sie **Done**.
6. Geben Sie Ihrem Content-Block einen Namen. Dieser Name wird automatisch als Teil des **Content Block Liquid Tag** übernommen.
7. (Optional) Fügen Sie eine Beschreibung hinzu.
8. Wählen Sie den Tab **Preview**, um zu sehen, wie Ihr Content-Block aussehen wird. Optional können Sie **Copy preview link** auswählen, um einen teilbaren Vorschau-Link zu generieren und zu kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussehen wird. Der Link ist sieben Tage lang gültig und muss danach neu generiert werden.<br><br> ![Tab „Vorschau“ für den Drag-and-Drop-Content-Block-Composer.]({% image_buster /assets/img_archive/dnd_content_block_preview_link.png %})<br><br>
9. Wählen Sie **Launch Content Block**.

{% elsif include.location == "html" %}

1. Gehen Sie zu **Content** > **Content Block**. Wählen Sie <i class="fas fa-plus"></i> **Create Content Block** und dann **HTML code editor** aus.
2. Geben Sie Ihren HTML-Code im Tab **HTML** ein oder erstellen Sie Ihren Content-Block im Tab **Classic**. <br><br> ![HTML-Code-Editor-Composer.]({% image_buster /assets/img_archive/html_content_block_composer.png %})<br><br>
3. Nachdem Sie Ihren Content-Block erstellt haben, wählen Sie **Done**.
4. Geben Sie einen Namen für Ihren Content-Block ein. Dieser Name wird automatisch als Teil des **Content Block Liquid Tag** übernommen.
5. (Optional) Fügen Sie eine Beschreibung hinzu.
6. Wählen Sie den Tab **Preview**, um zu sehen, wie Ihr Content-Block aussehen wird. Optional können Sie **Copy preview link** auswählen, um einen teilbaren Vorschau-Link zu generieren und zu kopieren, der zeigt, wie die E-Mail für eine:n zufällige:n Nutzer:in aussehen wird. Der Link ist sieben Tage lang gültig und muss danach neu generiert werden.<br><br> ![Tab „Vorschau“ für den HTML-Code-Editor-Composer.]({% image_buster /assets/img_archive/content_block_html_preview_link.png %})<br><br>
7. Wählen Sie **Launch Content Block**.

{% endif %}