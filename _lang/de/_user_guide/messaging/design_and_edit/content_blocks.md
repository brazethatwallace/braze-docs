---
nav_title: Content-Blöcke
article_title: Content-Blöcke
alias: "/dnd/content_blocks/"
page_order: 4
description: "Erfahren Sie, wie Sie wiederverwendbare Content-Blöcke in Ihren Braze-Kampagnen und Canvases erstellen, verwenden und verwalten."
page_type: reference
tool:
  - Templates
  - Media

---

# Content-Blöcke {#content-blocks}

> Mit Content-Blöcken können Sie wiederverwendbare, kanalübergreifende Inhalte an einem einzigen, zentralen Ort verwalten. Nutzen Sie sie, um ein einheitliches Erscheinungsbild in Ihren Kampagnen zu schaffen, dieselben Angebotscodes über verschiedene Kanäle zu verteilen oder vordefinierte Assets für konsistentes Messaging im großen Maßstab zu erstellen. Sie können Ihre Content-Blöcke auch [über die API]({{site.baseurl}}/api/endpoints/templates/) erstellen und verwalten.

## Einen Content-Block erstellen {#create-a-content-block}

Es gibt zwei Arten von Content-Blöcken: Drag-and-Drop und HTML. Jeder Typ entspricht seinem Editor.

{% tabs %}
{% tab Drag-and-Drop %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Jeder Drag-and-Drop-Content-Block ist auf eine Zeile beschränkt. Sie können jedoch Drag-and-Drop-Editor-Blöcke verwenden, um den Content-Block für Ihr E-Mail-Messaging zu erstellen und anzupassen.
{% endalert %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Spezifikationen für Content-Blöcke {#content-block-specifications}

| Content-Block-Attribut | Spezifikationen |
|---|---|
| Name | Pflichtfeld mit maximal 100 Zeichen. Der Name kann nach dem Speichern des Content-Blocks nicht mehr geändert werden. Außerdem können Sie einem neuen Content-Block nicht denselben Namen wie einem vorherigen Content-Block geben, selbst wenn der vorherige archiviert wurde. |
| Beschreibung | (optional) Maximal 250 Zeichen. Beschreiben Sie den Content-Block, damit andere Braze-Nutzer:innen wissen, wofür er gedacht ist und wo er verwendet wird. |
| Inhaltsgröße | Maximal 50 KB. |
| Platzierung | Content-Blöcke können nicht in einer E-Mail-Fußzeile verwendet werden, aber Sie können [einen Content-Block erstellen, der eine Fußzeile enthält](#email-footers), um ihn in Ihren E-Mails zu verwenden. |
| Erstellung | HTML-Editor oder Drag-and-Drop-Editor. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Spezifikationen für Content-Blöcke" }

{% alert tip %}
Beim Erstellen von Content-Blöcken kann es hilfreich sein, HTML und Liquid durch Zeilenumbrüche zu visualisieren. Wenn diese Zeilenumbrüche beim Senden beibehalten werden, riskieren Sie überflüssige Leerzeichen, die das Rendering des Blocks beeinträchtigen können. Um dies zu vermeiden, verwenden Sie den **Capture**-Tag in Ihrem Block zusammen mit dem **&#124; strip**-Filter.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Content-Blöcke verwenden {#use-content-blocks}

Nachdem Sie Ihren Content-Block erstellt haben, können Sie ihn über den Editor oder Liquid in Ihre Nachrichten einfügen.

### Den Drag-and-Drop-Editor verwenden {#using-the-editor}

So fügen Sie einen Content-Block im Drag-and-Drop-Editor hinzu:

1. Gehen Sie im Editor zum Tab **Rows** und wählen Sie **Content Blocks** aus.
2. Ziehen Sie Ihren Content-Block per Drag-and-Drop in den E-Mail-Editor.
3. (Optional) Passen Sie die Breite Ihres Content-Blocks an, indem Sie den Button im Navigationsmenü auswählen. Die Standardbreite beträgt 100 %, wenn sie nicht in Ihren globalen E-Mail-Stileinstellungen festgelegt ist; andernfalls werden die globalen Einstellungen berücksichtigt. <br><br>![Ein doppelseitiger Pfeil mit einer Option zum Bearbeiten der Breite.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

{% alert note %}
Content-Blöcke, die per Drag-and-Drop hinzugefügt werden, sind **nicht verknüpft** mit dem ursprünglichen Content-Block. Um Änderungen am Original zu sehen, ziehen Sie ihn erneut in den E-Mail-Editor.
{% endalert %}

Fehlausrichtungen im Drag-and-Drop-Editor können auftreten, wenn mehrere Content-Blöcke zu einem einzelnen Zeilenblock hinzugefügt werden. Versuchen Sie, separate Zeilenblöcke zu verwenden, um die Ausrichtung Ihrer Inhalte auf Zeilenebene beizubehalten.

### Liquid verwenden {#using-liquid}

So fügen Sie einen Content-Block mit Liquid ein:

1. Kopieren Sie den **Content Block Liquid Tag** aus dem Abschnitt **Content Block Details**.
2. Fügen Sie den Content-Block-Liquid-Tag in die Nachricht ein. Sie können auch beginnen, den Liquid-Code einzugeben, und der Tag wird automatisch vervollständigt.

Im Drag-and-Drop-Editor können Sie einen Content-Block auch über das **Personalization**-Panel hinzufügen:

1. Gehen Sie zu Ihrer E-Mail-Campaign und wählen Sie **Edit Email Body** aus.
2. Klicken Sie auf <i class="fas fa-plus"></i> **Personalization**.
3. Wählen Sie **Content Blocks** im Dropdown **Personalization Type** aus.
4. Wählen Sie den Namen Ihres Content-Blocks im Feld **Attribute** aus.
5. Kopieren Sie das Liquid-Snippet und fügen Sie es in einen Text-Editor-Block ein. <br>![Der Tab „Personalisierung hinzufügen“ mit Optionen.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

{% alert important %}
Content-Blöcke, die über Liquid eingefügt werden, **sind verknüpft** mit dem ursprünglichen Content-Block und spiegeln alle Änderungen am Template wider.
{% endalert %}

### Wissenswertes {#things-to-know}

- Die Verwendung von HTML-Content-Blöcken in Drag-and-Drop-E-Mails **oder** von Drag-and-Drop-Content-Blöcken in HTML-E-Mails kann zu unerwarteten Rendering-Problemen führen. Das liegt daran, dass der Drag-and-Drop-Editor HTML und CSS generiert, die den Inhalt dynamisch rendern, während der HTML-Editor eher statisch ist.
- Wenn Sie einen Drag-and-Drop-Content-Block über Liquid einfügen, übernimmt Braze keine Styles aus dem HTML-`<head>` des Blocks. Responsive Styles, wie mobilspezifisches CSS, werden möglicherweise nicht wie erwartet gerendert. Wenn der Block auf responsives CSS angewiesen ist, fügen Sie dieses CSS der Nachricht oder dem Template hinzu, das den Content-Block enthält.
- Canvas-Event-Eigenschaften werden nur in einem Canvas unterstützt. Wenn Sie einen Content-Block mit Canvas-Eingangs-Eigenschaften in einer Campaign referenzieren, wird er nicht befüllt.

## Content-Blöcke in der Vorschau anzeigen {#preview-content-blocks}

Nachdem Sie einen Content-Block in einer aktiven Campaign oder einem Canvas hinzugefügt haben, können Sie ihn in der Content-Block-Bibliothek in der Vorschau anzeigen, indem Sie mit der Maus über den Content-Block fahren und das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** auswählen.

Diese Vorschau enthält Informationen über den Content-Block, z. B. wer ihn erstellt hat, Tags, Erstellungsdatum, Datum der letzten Bearbeitung, Beschreibung, Editor-Typ, Anzahl der Verwendungen mit Details (eine anklickbare Liste von Nachrichten oder Content-Blöcken, die den Content-Block verwenden) sowie eine tatsächliche Vorschau des Content-Blocks.

## Content-Blöcke verschachteln {#nest-content-blocks}

Content-Blöcke können verschachtelt werden, aber nur einmal. Sie können Content-Block A in Content-Block B verschachteln, aber Sie können Content-Block B dann nicht in Content-Block C verschachteln.

{% alert warning %}
Nichts hindert Sie daran, eine dritte Ebene von Content-Blöcken zu verschachteln, aber der Inhalt wird in Verschachtelungen über die zweite Ebene hinaus nicht erweitert. Der Inhalt und das Liquid-Snippet werden aus der Nachricht entfernt.
{% endalert %}

## Content-Blöcke aktualisieren und kopieren {#update-and-copy-content-blocks}

Wenn Sie einen Content-Block aktualisieren, wird er in allen Nachrichten aktualisiert, in denen der Content-Block über Liquid eingefügt wurde. Wenn der Content-Block über das Dropdown **Content Blocks** unter **Rows** im Drag-and-Drop-Editor importiert wurde, wird er nicht in allen Nachrichten aktualisiert.

Wenn Sie einen Content-Block für eine einzelne Nachricht aktualisieren oder eine Kopie zur Verwendung in anderen Nachrichten erstellen möchten, können Sie entweder den HTML-Code aus der ursprünglichen Nachricht in Ihre neue kopieren oder den ursprünglichen Content-Block bearbeiten (er muss bereits in einer Nachricht verwendet worden sein) und speichern. Sie erhalten dann eine Aufforderung, die es Ihnen ermöglicht, ihn als neuen Content-Block zu speichern.

Nachdem Sie Änderungen an einem Content-Block vorgenommen haben, können Sie den aktualisierten Content-Block speichern und starten, indem Sie **Launch Content Block** auswählen. Oder Sie wählen **More** > **Duplicate**, um ein Duplikat Ihres Content-Blocks zu erstellen.

![Ein Content-Block mit dem Text „Welcome to our newsletter“.]({% image_buster /assets/img/copy-content-block.png %})

## E-Mail-Fußzeilen in Content-Blöcken verwenden {#email-footers}

Content-Blöcke können nicht innerhalb einer E-Mail-Fußzeile verwendet werden, aber Sie können einen Content-Block erstellen, der Fußzeileninhalte enthält, um ihn in Ihren E-Mails zu verwenden. Gehen Sie dazu wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Präferenzen** > **Angepasste Fußzeile** und erstellen Sie die Fußzeile.
2. Fügen Sie die Fußzeile einem Content-Block in der **Content-Block-Bibliothek** hinzu.
3. Fügen Sie diesen Content-Block Ihren E-Mail-Templates oder Nachrichten hinzu.

## Content-Blöcke archivieren {#archive-content-blocks}

![Aufgeklapptes Einstellungs-Dropdown-Menü mit drei Optionen: Archivieren, Duplizieren und In Workspace kopieren.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Wenn Sie einen Content-Block nicht mehr benötigen, können Sie ihn auf der Seite **Templates** archivieren. Archivierte Content-Blöcke sind schreibgeschützt. Heben Sie die Archivierung des Content-Blocks auf, bevor Sie ihn bearbeiten. Content-Blöcke können nicht archiviert werden, wenn sie in Nachrichten verwendet werden.

### Best Practices {#best-practices}

- Wenn Ihr Block nur in wenigen E-Mails verwendet wird, empfehlen wir, den veralteten Block zu archivieren und Ihre aktiven Nachrichten mit einem neueren Block zu aktualisieren, der nicht archiviert wurde.
- Wenn Ihr Block nur einen Tippfehler hat oder eine kleine Änderung benötigt, empfehlen wir nicht, den Block zu archivieren. Aktualisieren Sie stattdessen den Block und senden Sie weiter!
- Wenn Ihr Block in mehr Nachrichten verwendet wird, als Sie mit dem ersten Vorschlag in dieser Liste sinnvoll verwalten können, empfehlen wir, den gesamten Inhalt aus dem Block zu entfernen. Dies verhindert, dass veraltete Informationen in Nachrichten eingebunden werden.
- Wenn Sie versehentlich einen Content-Block archiviert haben, können Sie die Archivierung aufheben.

![Panel „Gespeicherte Content-Blöcke“, in dem das Einstellungs-Dropdown-Menü für „Test_32“ aufgeklappt ist und drei Optionen zeigt: Archivierung aufheben, Duplizieren und In Workspace kopieren]({% image_buster /assets/img/unarchive-content-block.png %})