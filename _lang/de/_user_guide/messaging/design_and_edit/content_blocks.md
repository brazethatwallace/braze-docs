---
nav_title: Content-Blöcke
article_title: Content-Blöcke
alias: "/dnd/content_blocks/"
page_order: 4
description: "Erfahren Sie, wie Sie wiederverwendbare Content-Blöcke in Ihren Braze Campaigns und Canvases erstellen, verwenden und verwalten."
page_type: reference
tool:
  - Templates
  - Media

---

# Content-Blöcke {#content-blocks}

> Mit Content-Blöcken können Sie wiederverwendbare, kanalübergreifende Inhalte an einem einzigen, zentralen Ort verwalten. Nutzen Sie sie, um ein einheitliches Erscheinungsbild in Ihren Campaigns zu schaffen, dieselben Angebotscodes über verschiedene Kanäle zu verteilen oder vordefinierte Assets für konsistentes Messaging im großen Maßstab zu erstellen. Sie können Ihre Content-Blöcke auch [über die API]({{site.baseurl}}/api/endpoints/templates) erstellen und verwalten.

## Content-Block erstellen {#create-a-content-block}

Es gibt zwei Arten von Content Blocks: Drag-and-Drop und HTML. Jeder Typ entspricht seinem Editor.

{% tabs %}
{% tab Drag-and-Drop %}

{% multi_lang_include messaging/create_content_block.md location="dnd" %}

{% alert important %}
Jeder Drag-and-Drop-Content-Block ist auf eine Zeile beschränkt. Sie können jedoch Drag-and-Drop-Editor-Blöcke verwenden, um den Content-Block zu erstellen und an Ihr E-Mail-Messaging anzupassen.
{% endalert %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include messaging/create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Content-Block-Spezifikationen {#content-block-specifications}

| Content-Block-Attribut | Spezifikationen |
|---|---|
| Name | Pflichtfeld mit maximal 100 Zeichen. Content-Block-Namen dürfen nur Buchstaben (A–Z), Zahlen (0–9), Bindestriche (`-`) und Unterstriche (`_`) enthalten. Leerzeichen und andere Sonderzeichen sind nicht zulässig und werden automatisch konvertiert (z. B. werden Leerzeichen durch Unterstriche ersetzt). Namen können nach dem Speichern des Content-Blocks nicht mehr geändert werden, und Sie können den Namen eines früheren Content-Blocks nicht wiederverwenden, auch nicht, wenn dieser archiviert wurde. |
| Beschreibung | (optional) Maximal 250 Zeichen. Beschreiben Sie den Content-Block, damit andere Braze-Nutzer:innen wissen, wofür er gedacht ist und wo er verwendet wird. |
| Inhaltsgröße | Maximal 50 KB. |
| Platzierung | Content Blocks können nicht in einer E-Mail-Fußzeile verwendet werden, aber Sie können [einen Content-Block erstellen, der eine Fußzeile enthält](#email-footers), um ihn in Ihren E-Mails zu verwenden. |
| Erstellung | HTML-Editor oder Drag-and-Drop-Editor. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content-Block-Spezifikationen" }

{% alert tip %}
Beim Erstellen von Content Blocks kann es hilfreich sein, HTML und Liquid durch Zeilenumbrüche zu visualisieren. Wenn diese Zeilenumbrüche beim Versand beibehalten werden, riskieren Sie überflüssige Leerzeichen, die das Rendering des Blocks beeinträchtigen können. Um dies zu vermeiden, verwenden Sie den **Capture**-Tag in Ihrem Block zusammen mit dem **&#124; strip**-Filter.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Content Blocks verwenden {#use-content-blocks}

Nachdem Sie Ihren Content-Block erstellt haben, können Sie ihn über den Editor oder Liquid in Ihre Nachrichten einfügen.

### Den Drag-and-drop-Editor verwenden {#using-the-editor}

So fügen Sie einen Content-Block im Drag-and-drop-Editor hinzu:

1. Gehen Sie im Editor zum Tab **Rows** und wählen Sie **Content Blocks** aus.
2. Ziehen Sie Ihren Content-Block per Drag-and-drop in den E-Mail-Editor.
3. (Optional) Passen Sie die Breite Ihres Content-Blocks an, indem Sie den Button im Navigationsmenü auswählen. Die Standardbreite beträgt 100 %, wenn in Ihren globalen E-Mail-Stileinstellungen nichts anderes angegeben ist; andernfalls werden die globalen Einstellungen berücksichtigt. <br><br>![Ein Doppelpfeil mit einer Option zum Bearbeiten der Breite.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

{% alert note %}
Content Blocks, die per Drag-and-drop hinzugefügt werden, sind **nicht verknüpft** mit dem ursprünglichen Content-Block. Um Änderungen am Original anzuzeigen, ziehen Sie ihn erneut in den E-Mail-Editor.
{% endalert %}

Fehlausrichtungen im Drag-and-drop-Editor können auftreten, wenn mehrere Content Blocks in einen einzelnen Zeilenblock eingefügt werden. Versuchen Sie, separate Zeilenblöcke zu verwenden, um die Ausrichtung Ihrer Inhalte auf Zeilenebene beizubehalten.

### Liquid verwenden {#using-liquid}

So fügen Sie einen Content-Block mit Liquid ein:

1. Kopieren Sie den **Content Block Liquid Tag** aus dem Abschnitt **Content Block Details**.
2. Fügen Sie den Content-Block-Liquid-Tag in die Nachricht ein. Sie können auch beginnen, den Liquid-Code einzugeben, und der Tag wird automatisch vervollständigt.

Im Drag-and-drop-Editor können Sie einen Content-Block auch über das Panel **Personalisierung** hinzufügen:

1. Gehen Sie zu Ihrer E-Mail-Campaign und wählen Sie **Edit Email Body** aus.
2. Klicken Sie auf <i class="fas fa-plus" aria-label="Personalisierung hinzufügen"></i> **Personalization**.
3. Wählen Sie **Content Blocks** im Dropdown **Personalization Type** aus.
4. Wählen Sie den Namen Ihres Content-Blocks im Feld **Attribute** aus.
5. Kopieren Sie das Liquid-Snippet und fügen Sie es in einen Text-Editor-Block ein. <br>![Der Tab „Personalisierung hinzufügen“ mit Optionen.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

{% alert important %}
Content Blocks, die über Liquid eingefügt werden, **sind verknüpft** mit dem ursprünglichen Content-Block und spiegeln alle Änderungen am Template wider.
{% endalert %}

## Content Blocks in der Vorschau anzeigen {#preview-content-blocks}

Nachdem Sie einen Content-Block in einer aktiven Campaign oder einem Canvas hinzugefügt haben, können Sie ihn in der Content-Block-Bibliothek in der Vorschau anzeigen, indem Sie mit dem Mauszeiger über den Content-Block fahren und das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** auswählen.

Diese Vorschau enthält Informationen über den Content-Block, z. B. wer ihn erstellt hat, Tags, Erstellungsdatum, Datum der letzten Bearbeitung, Beschreibung, Editor-Typ, Anzahl der Verwendungen mit Details (eine anklickbare Liste von Nachrichten oder Content Blocks, die den Content-Block verwenden) sowie eine tatsächliche Vorschau des Content-Blocks.

{% alert note %}
Wenn Sie überprüfen, wo ein Content-Block verwendet wird, prüfen Sie jede verknüpfte Nachricht oder jeden Schritt einzeln, um den jeweiligen Status zu bestätigen.
{% endalert %}

## Content Blocks verschachteln {#nest-content-blocks}

Content Blocks können verschachtelt werden, jedoch nur einmal. Sie können Content-Block A in Content-Block B verschachteln, aber Sie können Content-Block B dann nicht in Content-Block C verschachteln.

{% alert warning %}
Nichts hindert Sie daran, eine dritte Ebene von Content Blocks zu verschachteln, aber der Inhalt wird in Verschachtelungen über die zweite Ebene hinaus nicht erweitert. Der Inhalt und das Liquid-Snippet werden aus der Nachricht entfernt.
{% endalert %}

Links innerhalb eines verschachtelten Content-Blocks zählen zur Gesamtanzahl der Links der übergeordneten Nachricht. Wenn Sie einen einzelnen Content-Block mit vielen bedingten Links verwenden, z. B. länderspezifische URLs für die Lokalisierung, kann die übergeordnete Nachricht eine große Anzahl von Links ansammeln, was das Speichern eines Canvas verlangsamen oder verhindern kann. Für groß angelegte Lokalisierung sind [mehrsprachige Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) besser geeignet als bedingte Links in einem einzelnen Content-Block.

## Content Blocks aktualisieren und kopieren {#update-and-copy-content-blocks}

Wenn Sie einen Content-Block aktualisieren, wird er in allen Nachrichten aktualisiert, in denen der Content-Block über Liquid eingefügt wurde. Wenn der Content-Block über das **Content Blocks**-Dropdown unter **Zeilen** im Drag-and-Drop-Editor importiert wurde, wird er nicht in allen Nachrichten aktualisiert.

Wenn Sie einen Content-Block für eine einzelne Nachricht aktualisieren oder eine Kopie zur Verwendung in anderen Nachrichten erstellen möchten, können Sie entweder den HTML-Code aus der ursprünglichen Nachricht in Ihre neue kopieren oder den ursprünglichen Content-Block bearbeiten (er muss bereits in einer Nachricht verwendet worden sein) und speichern. Sie erhalten dann eine Aufforderung, die es Ihnen ermöglicht, ihn als neuen Content-Block zu speichern.

Nachdem Sie Änderungen an einem Content-Block vorgenommen haben, können Sie den aktualisierten Content-Block speichern und starten, indem Sie **Launch Content Block** auswählen. Alternativ können Sie **Mehr** > **Duplizieren** auswählen, um ein Duplikat Ihres Content-Blocks zu erstellen.

![Ein Content-Block mit dem Text „Willkommen bei unserem Newsletter“.]({% image_buster /assets/img/copy-content-block.png %})

## E-Mail-Fußzeilen in Content-Blöcken verwenden {#email-footers}

Content-Blöcke können nicht innerhalb einer E-Mail-Fußzeile verwendet werden, aber Sie können einen Content-Block erstellen, der Fußzeileninhalte enthält, um ihn in Ihren E-Mails zu verwenden. Gehen Sie dazu wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Einstellungen** > **Angepasste Fußzeile** und erstellen Sie die Fußzeile.
2. Fügen Sie die Fußzeile einem Content-Block in der **Content-Block-Bibliothek** hinzu.
3. Fügen Sie diesen Content-Block Ihren E-Mail-Templates oder Nachrichten hinzu.

## Wissenswertes {#things-to-know}

- Die Verwendung von HTML-Content-Blöcken in Drag-and-Drop-E-Mails oder von Drag-and-Drop-Content-Blöcken in HTML-E-Mails kann zu unerwarteten Darstellungsproblemen führen. Der Grund dafür ist, dass der Drag-and-Drop-Editor HTML und CSS generiert, die den Inhalt dynamisch rendern, während der HTML-Editor eher statisch arbeitet.
- Wenn Sie einen Drag-and-Drop-Content-Block über Liquid einfügen, übernimmt Braze keine Styles aus dem HTML-`<head>` des Blocks. Responsive Styles, wie z. B. mobilspezifisches CSS, werden möglicherweise nicht wie erwartet dargestellt. Wenn der Block auf responsives CSS angewiesen ist, fügen Sie dieses CSS der Nachricht oder dem Template hinzu, das den Content-Block enthält.
- Canvas-Entry-Eigenschaften werden nur in Canvases unterstützt. Wenn Sie in einer Campaign auf einen Content-Block mit Canvas-Entry-Eigenschaften verweisen, wird dieser nicht befüllt.
- Wenn eine Nachricht mit mehreren Content-Blöcken nicht wie erwartet dargestellt wird – beispielsweise wenn Liquid-Tags oder HTML als sichtbarer Text erscheinen, anstatt verarbeitet zu werden – ist häufig ein nicht geschlossener Tag oder ein anderer Fehler in einem der Content-Blöcke die Ursache. So identifizieren Sie die Quelle:
    1. Entfernen Sie die Content-Blöcke nacheinander aus der betroffenen Nachricht.
    2. Prüfen Sie nach jeder Entfernung, ob die Nachricht korrekt dargestellt wird.
    3. Der letzte Content-Block, den Sie entfernen, bevor das Problem verschwindet, ist derjenige, der das Problem verursacht.
- `<code>`-HTML-Tags werden in den meisten E-Mail-Clients standardmäßig in Monospace-Schrift dargestellt, unabhängig von der im Content-Block festgelegten Schriftformatierung. Vermeiden Sie es, Text in `<code>`-Tags einzuschließen, es sei denn, Sie möchten diese Monospace-Darstellung.
- Wenn Sie einen Content-Block über Liquid in ein benutzerdefiniertes HTML-E-Mail-Template einfügen, können CSS-Regeln im übergeordneten Template die im Content-Block definierten Styles überschreiben. Weitere Informationen finden Sie unter [Content-Blöcke in benutzerdefinierten HTML-Templates]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline#content-blocks-in-custom-html-templates).

## Content Blocks archivieren {#archive-content-blocks}

![Aufgeklapptes Einstellungs-Dropdown-Menü mit drei Optionen: Archivieren, Duplizieren und In Workspace kopieren.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Wenn Sie einen Content-Block nicht mehr benötigen, können Sie ihn auf der Seite **Templates** archivieren. Archivierte Content Blocks sind schreibgeschützt – heben Sie die Archivierung des Content-Blocks auf, bevor Sie ihn bearbeiten. Content Blocks können nicht archiviert werden, wenn sie in Nachrichten verwendet werden.

### Best Practices {#best-practices}

- Wenn Ihr Block nur in wenigen E-Mails verwendet wird, empfehlen wir, den veralteten Block zu archivieren und Ihre aktiven Nachrichten mit einem neueren Block zu aktualisieren, der nicht archiviert wurde.
- Wenn Ihr Block nur einen Tippfehler enthält oder eine kleine Änderung benötigt, empfehlen wir nicht, den Block zu archivieren. Aktualisieren Sie stattdessen den Block und senden Sie weiter!
- Wenn Ihr Block in mehr Nachrichten verwendet wird, als Sie mit dem ersten Vorschlag in dieser Liste sinnvoll verwalten können, empfehlen wir, den gesamten Inhalt aus dem Block zu entfernen. So wird verhindert, dass veraltete Informationen in Nachrichten eingefügt werden.
- Wenn Sie versehentlich einen Content-Block archiviert haben, können Sie die Archivierung wieder aufheben.

![Panel „Gespeicherte Content Blocks“, in dem das Einstellungs-Dropdown-Menü für „Test_32“ aufgeklappt ist und drei Optionen zeigt: Archivierung aufheben, Duplizieren und In Workspace kopieren]({% image_buster /assets/img/unarchive-content-block.png %})