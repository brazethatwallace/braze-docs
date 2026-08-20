---
nav_title: Link-Templates
article_title: Link-Templates
page_order: 4
description: "In diesem Artikel erfahren Sie, wie Sie verschiedene Arten von Link-Templates in Ihren E-Mails erstellen."
tool:
  - Templates
channel:
  - email

---

# Link-Templates {#link-templates}

> Mit Link-Templates können Sie dynamische und wiederverwendbare Links für Ihre E-Mail-Campaigns erstellen, indem Sie Parameter anhängen oder URLs voranstellen. So schaffen Sie Konsistenz bei den URLs in Ihren Campaigns und Nachrichten.

{% alert note %}
Link-Templates sind ein optionales Feature. Wenn **E-Mail-Link-Templates** im Abschnitt **Templates** fehlt, wenden Sie sich an Ihren Account Manager, um das Feature zu aktivieren.
{% endalert %}

## Funktionsweise {#how-it-works}

Link Templates werden am häufigsten in den folgenden Anwendungsfällen eingesetzt:

- Anhängen von Google Analytics-Abfrageparametern an alle Links in einer bestimmten E-Mail-Nachricht
- Voranstellen einer URL vor alle Links in einer bestimmten E-Mail-Nachricht

Angenommen, Sie führen eine E-Mail-Campaign für die Einführung eines neuen Produkts durch. Sie können ein Link Template verwenden, das Nutzer:innen auf die Produktseite leitet, und den Link personalisieren, um den Namen Ihrer Nutzer:innen oder einen bestimmten Aktionscode einzufügen. So können Sie nachverfolgen, wie viele Nutzer:innen auf den Link geklickt und einen Kauf getätigt haben. Auf diese Weise können Sie Konsistenz über Ihre Links hinweg schaffen und Ihre Analytics besser verfolgen.

## Link-Template erstellen {#creating-a-link-template}

Sie können eine unbegrenzte Anzahl von Link-Templates erstellen, um Ihre verschiedenen Anforderungen zu unterstützen. Gehen Sie wie folgt vor, um ein Link-Template zu erstellen:

1. Gehen Sie zu **Inhalt** > **E-Mail-Link**.
2. Wählen Sie **E-Mail-Link-Template erstellen** aus.
3. Geben Sie Ihrem Link-Template einen Namen.
4. (Optional) Fügen Sie eine Beschreibung, ein Team oder einen Tag hinzu, um weitere Details zum Link-Template anzugeben.
5. (Optional) Aktivieren Sie den Schalter, um das Link-Template automatisch zu Links in E-Mail-Campaigns und Canvases hinzuzufügen. Dies gilt beim Hinzufügen eines neuen Links zu jeder neuen oder bestehenden E-Mail.

Es gibt zwei Arten von Link-Templates, die Sie erstellen können:

- [Link-Template, das vor einer URL eingefügt wird](#prepend-link-template)
- [Link-Template, das nach einer URL eingefügt wird](#append-link-template)

Wenn Sie Link-Templates und [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) verwenden, darf Liquid nur innerhalb des Body-Tags hinzugefügt werden, um ein konsistentes Rendering sicherzustellen.

### Voranstellen: Ein Link-Template erstellen, das vor einer URL eingefügt wird {#prepend-link-template}

Gehen Sie wie folgt vor, um einen String oder eine URL vor den Links in Ihrer E-Mail-Nachricht hinzuzufügen:

1. Erstellen Sie ein neues Link-Template.
2. Setzen Sie die **Template-Position** auf **Vor URL**.
3. Geben Sie einen String ein, der immer vor Ihre URL gestellt wird.

Die **Template-Vorschau** zeigt Ihnen ein Beispiel, wie das Link-Template vor einer URL eingefügt wird.

![Felder für Template-Position, vorangestellte URL und Template-Vorschau für den Einfügeprozess des Link-Templates vor einer URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Anhängen: Ein Link-Template erstellen, das nach einer URL eingefügt wird {#append-link-template}

Wenn Sie Query-Parameter nach einer URL in Ihrer E-Mail-Nachricht hinzufügen möchten:

1. Erstellen Sie ein neues Link-Template.
2. Setzen Sie die **Template-Position** auf **Nach URL**.
3. Geben Sie die Query-Parameter (`value=example`) am Ende jeder URL ein. Sie können mehrere Parameter an das Ende einer URL anhängen.

![Felder für Template-Position, Query-Parameter und Template-Vorschau für den Einfügeprozess des Link-Templates nach einer URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Link-Templates in E-Mail-Campaigns verwenden {#using-link-templates-in-email-campaigns}

Nachdem Sie Ihre Link-Templates eingerichtet haben, können Sie sie in Ihren E-Mails anwenden.

Um ein Link-Template im HTML-Editor oder im Drag-and-Drop-Editor anzuwenden, führen Sie die folgenden Schritte aus:

{% alert note %}
Wenn E-Mail-Link-Templates oder [Link Aliasing]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) für Ihren Workspace aktiviert sind, können Sie im aktualisierten HTML-Editor und im Drag-and-Drop-Editor auf den Tab **Link Management** zugreifen.
{% endalert %}

- **Aktualisierter HTML-Editor:** Wählen Sie auf dem Tab **Content** die Option **Link Management** aus, wählen Sie **Add a Link Template**, wählen Sie Ihr Link-Template aus und wählen Sie dann **Add**.
- **Drag-and-Drop-Editor:** Wählen Sie auf dem Tab **Content** die Option **Link Management** aus, wählen Sie **Add a Link Template**, wählen Sie Ihr Link-Template aus und wählen Sie dann **Add**.

![Tab „Link Management“ im Drag-and-Drop-Editor mit einer Beispielliste von Link-Templates.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Link-Templates werden nicht auf Nur-Text angewendet. Das bedeutet, dass Currents möglicherweise Klicks anzeigt, die die Parameter aus den Link-Templates nicht enthalten, da diese Klicks von der Nur-Text-Version der E-Mail stammen können.
{% endalert %}

Wenn Sie Link-Templates im Tab **Link Management** hinzufügen, wird jedes Template als zusätzliche Spalte in der Tabelle angezeigt. Wenn vorhandene Links in einer E-Mail bereits ein Link-Template hinzugefügt haben, wird neu hinzugefügten Links das Link-Template ebenfalls standardmäßig hinzugefügt.

{% alert tip %}
Wenn Sie Links in Ihre Nachricht einfügen, stellen Sie sicher, dass die URLs mit `http://` oder `https://` beginnen.
{% endalert %}

## Link-Templates verwalten {#managing-link-templates}

Sie können Link-Templates auch [duplizieren]({{site.baseurl}}/user_guide/messaging/templates/managing_templates). Erfahren Sie mehr über das Erstellen und Verwalten von Templates und kreativen Inhalten unter [Templates und Medien]({{site.baseurl}}/user_guide/messaging/templates).

{% alert important %}
Das Archivieren von Templates ist derzeit für Link-Templates nicht verfügbar.
{% endalert %}

## Fehlerbehebung {#troubleshooting}

### Fehlende UTM-Parameter {#missing-utm-parameters}

Link-Templates werden nicht auf Links in Standard-HTML-Kommentaren (`<!-- ... -->`) angewendet. Bei bedingten Outlook-Kommentaren (zum Beispiel `<!--[if mso]>`) werden Link-Templates angewendet, wenn Link Aliasing für Ihren Workspace aktiviert ist. Workspaces ohne aktiviertes Link Aliasing überspringen bedingte Kommentare weiterhin.

### UTM-Parameter im Browser vorhanden, aber in Links fehlend {#utm-parameters-present-in-browser-but-missing-from-links}

Dies kann passieren, wenn der URL-Pfad in Ihrer E-Mail nicht mit dem vollständigen Pfad übereinstimmt, den Sie beabsichtigen (zum Beispiel ein verkürzter oder anderer Pfad als die vollständige URL der Website).

- **Was Sie überprüfen sollten:** Das `href` in der E-Mail enthält den vollständigen Pfad zur Seite (nicht nur einen Teilpfad, der auf Weiterleitungen angewiesen ist).
- **Was Sie erwarten können:** Wenn der Pfad in der E-Mail unvollständig oder anders ist, werden UTM-Parameter aus Ihrem Link-Template möglicherweise nicht auf diesen Link angewendet, wenn er angeklickt wird, auch wenn die Website den Besucher trotzdem auf die richtige Seite weiterleiten könnte.

Wenn der vollständige Link beispielsweise `https://www.somewebsite.com/women/designer/johnjane` lautet, die E-Mail aber `https://www.somewebsite.com/designer/johnjane` verwendet, ist es erwartungsgemäß, dass UTM-Parameter nicht zum E-Mail-Link hinzugefügt werden.

### UTM-Parameter fehlen bei Liquid-gerenderten Links {#utm-parameters-missing-from-liquid-rendered-links}

Beim Anwenden von Link-Templates analysiert Braze jede URL, um zu bestimmen, wo Parameter angehängt werden sollen. Wenn ein Liquid-Tag eine URL rendert, die nicht als gültige URI geparst werden kann, wird das Link-Template stillschweigend übersprungen. Überprüfen Sie, ob Ihre Liquid-Ausgabe eine wohlgeformte URL erzeugt. Testen Sie dies, indem Sie die Nachricht für eine:n bestimmte:n Nutzer:in in der Vorschau anzeigen und überprüfen, ob die gerenderte URL gültig ist. Wenn die URL Liquid-Variablen im Pfad oder Query-String enthält, stellen Sie sicher, dass die Ausgabe keine ungültigen Zeichen oder fehlerhafte Kodierung enthält.

### UTM-Werte fehlen bei Testversendungen {#utm-values-missing-in-test-sends}

Beim Testversand von Link-Templates wird {% raw %}`{{${user_id}}}`{% endraw %} nicht gerendert. Duplizieren Sie stattdessen die Campaign und richten Sie sie so ein, dass sie auf die E-Mail oder `external_id` Ihrer internen Nutzer:innen abzielt, und starten Sie die Campaign, um zu überprüfen, ob alle UTM-Parameter aus dem Link-Template befüllt werden.

## Häufig gestellte Fragen {#frequently-asked-questions}

Antworten auf häufig gestellte Fragen zu Link-Templates finden Sie auf unserer Seite [Templates FAQ]({{site.baseurl}}/user_guide/messaging/templates/email_templates/faq).