---
nav_title: Mehrsprachige Nachrichten
article_title: Mehrsprachige Nachrichten
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Dieser Artikel beschreibt die Schritte zur Verwendung von Locales in Ihren Nachrichten."
---

# Mehrsprachige Nachrichten {#multi-language-messages}

> Nachdem Sie Locales zu Ihrem Workspace hinzugefügt haben, können Sie Nutzer:innen in verschiedenen Sprachen innerhalb einer einzigen Push-Nachricht, E-Mail, eines Webhooks, eines Banners, einer In-App-Nachricht oder eines Content-Blocks ansprechen.

## Voraussetzungen {#prerequisites}

{% tabs %}
{% tab Mehrsprachige Locales %}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Nachrichtentypen %}

| Feature | Erforderliche Nutzer:innen-Berechtigungen |
| --- | --- |
| Nachrichtentypen | Sie benötigen diese Berechtigungen, um Locales und Übersetzungen zu Campaigns und Canvases hinzuzufügen:<br><br> {::nomarkdown} <ul><li>Edit Campaigns</li><li>Edit Canvases</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen"}

{% endtab %}
{% tab Templates %}

| Feature | Erforderliche Nutzer:innen-Berechtigungen |
| --- | --- |
| Templates | Sie benötigen diese Berechtigungen für den Template-Typ, dem Sie Locales und Übersetzungen hinzufügen möchten:<br><br> {::nomarkdown} <ul><li>Edit Email Templates</li><li>Edit IAM Templates</li><li>Edit Webhook Templates</li><li>Edit Content Block Templates</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% endtab %}
{% endtabs %}

## Lokale verwenden {#use-locales}

### Schritt 1: Lokale einrichten {#step-1-set-up-locales}

Bevor Sie Übersetzungen zu einer Nachricht hinzufügen können, müssen Sie zunächst [die Lokale erstellen, die Sie unterstützen möchten]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings). Lokale definieren die Sprach- (und optional Regions-)Varianten, die für Messaging verfügbar sind.

### Schritt 2: Inhalte für die Übersetzung markieren {#step-2-mark-content-for-translation}

Umschließen Sie den Text, den Sie übersetzen möchten, mit den Liquid-Übersetzungs-Tags {% raw %}`{% translation your_id_here %}` und `{% endtranslation %}`{% endraw %} und weisen Sie eine Tag-ID zu. Übersetzungs-Tag-IDs müssen innerhalb einer Nachricht eindeutig sein. Verwenden Sie nach Möglichkeit semantische ID-Namen, die den Text klar beschreiben, wie zum Beispiel {% raw %}`{% translation header %}`{% endraw %}. Wenn die Nachricht Content Blocks enthält, lesen Sie den Abschnitt [Content Blocks mit Übersetzungen](#content-blocks-containing-translation), um zu erfahren, wie die Eindeutigkeit gehandhabt wird.

Hier ist ein Beispiel für eine zur Übersetzung markierte Nachricht: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Markieren Sie den Text, den Sie übersetzen möchten, und verwenden Sie die Tastenkombination **Cmd + Alt + L** (macOS) oder **Strg + Alt + L** (Windows), um ihn in Übersetzungs-Tags einzuschließen.<br><br> Diese Tastenkombination funktioniert in allen Kanälen, die mehrsprachiges Messaging unterstützen, mit Ausnahme der Drag-and-Drop-Editoren für E-Mail und Content Blocks. Verwenden Sie dort den Button **Personalisierung hinzufügen**, um Übersetzungs-Tags hinzuzufügen.
{% endalert %}

#### URLs lokalisieren {#localize-urls}

Beim Übersetzen von Inhalten erfordern URLs eine besondere Behandlung, um defekte Links zu vermeiden.

##### Standard-URLs (statisch) {#standard-static-urls}

Statische URLs werden manuell im Editor eingegeben (zum Beispiel `https://example.com`). Wir empfehlen außerdem Folgendes:

| Empfehlung | Begründung |
| --- | --- |
| Behalten Sie das Protokoll (`https://`) außerhalb der Übersetzungs-Tags. Umschließen Sie nur die Domain und den Pfad (zum Beispiel `example.com/en`). | Übersetzer:innen könnten versehentlich Sonderzeichen ändern oder entfernen, was zu defekten Links führt. |
| Fügen Sie keine Abfrageparameter in Übersetzungs-Tags ein (zum Beispiel `?utm_source=promo`). | Übersetzer:innen könnten versehentlich Sonderzeichen ändern oder entfernen, was zu defekten Links führt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard-URLs (statisch)" }

Eine Standard-URL, die beide Empfehlungen befolgt, sieht wie folgt aus:

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### Mit Liquid generierte URLs {#liquid-generated-urls}

Wenn Ihre URL mit Liquid generiert wird (zum Beispiel {% raw %}`{% landing_page_url %}`{% endraw %}), empfehlen wir Folgendes:

| Empfehlung | Begründung |
| --- | --- |
| Umschließen Sie die mit Liquid generierte URL nur dann in Übersetzungs-Tags, wenn sie lokalisiert werden muss. | Liquid-Syntax muss sorgfältig beibehalten werden, damit sie korrekt gerendert wird. |
| Fügen Sie keine Abfrageparameter (zum Beispiel `?utm_source=promo`) in Übersetzungs-Tags ein. | Übersetzer:innen könnten versehentlich Sonderzeichen ändern oder entfernen, was zu defekten Links führt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Mit Liquid generierte URLs" }

Eine mit Liquid generierte URL, die beide Empfehlungen befolgt, sieht wie folgt aus:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
Wenn Sie [E-Mail-Link-Tracking](#email-link-tracking) (Link Aliasing oder Link-Templates) verwenden, ist eine zusätzliche Konfiguration erforderlich, wenn URLs in Übersetzungs-Tags eingeschlossen sind.
{% endalert %}

#### HTML-Attribute und -Struktur {#html-attributes-and-structure}

Umschließen Sie nur menschenlesbaren Text mit Übersetzungs-Tags. Vermeiden Sie es, HTML-Attribute (wie `class`, `style` oder `id`) oder anderen strukturellen Code einzuschließen. HTML-Attribute steuern Layout, Styling und Funktionalität. Wenn sie in Übersetzungs-Tags eingeschlossen werden, kann dies die Formatierung oder Stile in lokalisierten Versionen Ihrer Nachricht beeinträchtigen.

Dieser Text ist korrekt eingeschlossen:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Fehlerhaft eingeschlossener Text %}

Dieser Text ist **fehlerhaft** eingeschlossen:

{% raw %}
```
{% translation id_1 %}
<p class="headline" style="color: red;">
  Welcome to our sale
</p>
{% endtranslation %}
```
{% endraw %}

{% enddetails %}

### Schritt 3: Lokale zu Ihrer Nachricht hinzufügen {#step-3-add-locales-to-your-message}

Nachdem Sie Übersetzungs-Tags zu Ihrer Nachricht hinzugefügt haben, wählen Sie **Sprachen verwalten** im Editor (in den Drag-and-Drop-Editoren für E-Mail und Content Blocks heißt die Option **Sprachen**) und wählen Sie mindestens ein Lokal aus, für das Sie Übersetzungen hinzufügen möchten.

![Das Dropdown-Menü „Lokal hinzufügen“ mit Optionen zur Auswahl des Standard-Lokals oder angepasster Attribute.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Content Blocks mit Übersetzungen {#content-blocks-containing-translation}

Content Blocks mit Übersetzungs-Tags verhalten sich unterschiedlich, je nachdem, ob der Block eigene gespeicherte Übersetzungen hat:

| Content-Block-Status | Wo Übersetzungen verwaltet werden |
| --- | --- |
| Übersetzungs-Tags, aber keine Lokale oder gespeicherten Übersetzungen | CSV-Datei unter **Sprachen verwalten** der übergeordneten Nachricht |
| Übersetzungs-Tags mit Lokalen und gespeicherten Übersetzungen | Eigene CSV-Datei des Content Blocks oder Übersetzungs-API |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Content-Block-Übersetzungsstatus" }

##### Content Blocks mit gespeicherten Übersetzungen {#content-blocks-with-saved-translations}

Wenn Ihre Nachricht Content Blocks enthält, die bereits gespeicherte Übersetzungen haben, müssen Sie diese Übersetzungen nicht erneut hochladen. Gespeicherte Übersetzungen werden automatisch angewendet, wenn der Content Block zu Ihrer Nachricht hinzugefügt wird. Diese Blöcke behalten ihre eigenen Tag-IDs, die nicht gegenüber der übergeordneten Nachricht eindeutig sein müssen. Informationen zum Speichern von Übersetzungen im Block selbst finden Sie unter [Übersetzungen in Content Blocks speichern](#save-translations-in-content-blocks).

Im Modal **Sprachen verwalten** werden Content Blocks mit gespeicherten Übersetzungen in der Liste zusammen mit den von ihnen unterstützten Lokalen angezeigt. So können Sie sehen, welche Teile Ihrer Nachricht bereits lokalisiert sind, bevor Sie neue Übersetzungen hinzufügen.

![Der Bereich „Sprachen verwalten“ mit einer Liste von Content Blocks, die gespeicherte Übersetzungen haben.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Stellen Sie sicher, dass jeder Content Block Übersetzungen für jedes Lokal enthält, das Sie zu Ihrer Nachricht hinzugefügt haben. Wenn ein Content Block Übersetzungen für eines Ihrer hinzugefügten Lokale nicht enthält, wird er Nutzer:innen in diesem Lokal in der Originalsprache angezeigt.
{% endalert %}

##### Content Blocks nur mit Übersetzungs-Tags {#content-blocks-with-translation-tags-only}

Wenn ein Content Block Übersetzungs-Tags hat, aber keine Lokale oder gespeicherten Übersetzungen, werden seine Tags als nicht übersetzter Quellinhalt in der übergeordneten Nachricht behandelt. Der Export unter **Sprachen verwalten** der übergeordneten Nachricht enthält diese Tags, und die übergeordnete CSV-Datei muss die entsprechenden Übersetzungen liefern. Diese Tags müssen gegenüber anderen Tags in der übergeordneten Nachricht eindeutig sein.

Wenn Sie einen nicht übersetzten Content Block in einer anderen Nachricht wiederverwenden, muss diese zweite Nachricht ebenfalls Übersetzungen für die Tags des Blocks bereitstellen. Um zu vermeiden, dass Sie Übersetzungen in jeder Nachricht bereitstellen müssen, die einen Content Block verwendet, fügen Sie Lokale und Übersetzungen direkt zum Content Block selbst hinzu.

### Schritt 4: Übersetzungen hinzufügen {#step-4-add-translations}

Nachdem Sie Lokale ausgewählt haben, fügen Sie Übersetzungen zu Ihrer Nachricht mit einer der folgenden Methoden hinzu:

![Der Tab „Übersetzungen hinzufügen“ mit Optionen zum Hochladen von Übersetzungen per CSV oder durch Verbindung mit Übersetzungspartnern.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab CSV-Template hochladen %}

Wählen Sie **Template herunterladen**, um eine CSV-Datei herunterzuladen, die eine Matrix Ihrer ausgewählten Übersetzungs-IDs und Lokale enthält.

{% alert important %}
Um Anzeigeproblemen mit nicht-englischen Zeichen vorzubeugen, vermeiden Sie die Verwendung von Excel für Ihre Übersetzungs-CSV.
{% endalert %}

Wenn Sie das Template ausfüllen, übersetzen Sie nur den Textinhalt für jedes Lokal. Wenn HTML-Tags im heruntergeladenen Template vorhanden sind, lassen Sie diese unverändert und übersetzen Sie nur den Text innerhalb der Tags.

Wenn das Template beispielsweise Folgendes enthält:

```
<p style="margin:0;margin-bottom:0">A charming bakery dedicated to crafting artisanal breads.</p>
```

Übersetzen Sie nur den Text `A charming bakery dedicated to crafting artisanal breads.` und belassen Sie die HTML-Tags `<p style="margin:0;margin-bottom:0">` und `</p>` wie sie sind.

Laden Sie anschließend die ausgefüllte Datei hoch und die Übersetzungen werden auf Ihre Nachricht angewendet.

![CSV mit Übersetzungs-Tags für einen Titel, Angebotstext, Angebotsbetrag und CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Übersetzungs-API verwenden %}

Verwenden Sie eine Partner-Übersetzungs-API, um Übersetzungen in Ihren Campaigns, Canvases, Content Blocks, E-Mail-Templates und Webhook-Templates zu verwalten und zu aktualisieren. Dies ist nützlich, wenn Sie ein externes System für die Lokalisierung verwenden oder sich direkt mit einem Übersetzungspartner verbinden möchten.

Um die Übersetzungsendpunkte mit Canvases zu verwenden, geben Sie die folgenden Parameter an:
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
Wenn Sie die Übersetzungs-API mit Canvas-Schritten verwenden, die nach dem Start des Canvas erstellt wurden, ist die `message_variation_id`, die Sie an die API übergeben, leer.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 5: Übersetzungen in der Vorschau anzeigen {#step-5-preview-translations}

Um Ihre Nachricht in der Vorschau anzuzeigen, wählen Sie die Option **Mehrsprachige:r Nutzer:in** aus dem Dropdown **Vorschau als Nutzer:in**. So können Sie zwischen verschiedenen Lokal-Definitionen wechseln und alle Übersetzungen Ihrer Nachricht in der Vorschau anzeigen.

![Lokal-Vorschauen]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Übersetzungen verwalten {#manage-translations}

### Canvas-Schritte oder Campaigns duplizieren und Übersetzungen {#duplicate-canvas-steps-or-campaigns-and-translations}

Wenn Sie einen Canvas-Schritt, eine Campaign oder eine Variante duplizieren, werden die Übersetzungen mit übernommen. Das gilt auch beim Kopieren über Workspaces hinweg, sofern die Locales im Ziel-Workspace definiert sind. Überprüfen und aktualisieren Sie Übersetzungen entsprechend, wenn Sie Änderungen an Ihrem Canvas oder Ihrer Campaign vornehmen.

### Übersetzungen in Content Blocks speichern {#save-translations-in-content-blocks}

Content Blocks unterstützen Mehrsprachigkeit auf die gleiche Weise wie Nachrichten. Beim Erstellen oder Bearbeiten von Content Blocks können Sie Inhalte zur Übersetzung markieren, Locales hinzufügen und Übersetzungen per CSV oder über die [Übersetzungs-API]({{site.baseurl}}/api/endpoints/translations) hochladen.

Gespeicherte Übersetzungen bleiben mit dem Content Block verknüpft. Wenn der Block zu einer Nachricht hinzugefügt wird, werden seine Übersetzungen automatisch einbezogen.

### Rechts-nach-links-Nachrichten {#right-to-left-messages}

Wenn Sie die Übersetzungsdatei für Sprachen ausfüllen, die von rechts nach links geschrieben werden (wie Arabisch), umschließen Sie die Übersetzung mit `span`, damit sie korrekt formatiert wird:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### E-Mail-Link-Tracking {#email-link-tracking}

In E-Mail-Campaigns verfolgt Braze Links, indem Tracking-Informationen (Abfrageparameter) zu jeder URL hinzugefügt werden. Dieses Verhalten unterstützt sowohl [Link Aliasing]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing) als auch [Link-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template).

Wenn eine URL in Übersetzungs-Tags eingeschlossen ist, kann Braze möglicherweise nicht ermitteln, wo diese Tracking-Informationen hinzugefügt werden sollen. Um sicherzustellen, dass dies korrekt funktioniert, müssen Sie ein Sonderzeichen am Ende der URL einfügen, um anzugeben, wo das Tracking hinzugefügt werden soll.

URLs verwenden zwei Sonderzeichen, um dieses Verhalten zu steuern:
  - `?` fügt Tracking zu einer URL hinzu, die noch keines enthält.
  - `&` fügt zusätzliches Tracking hinzu, wenn bereits ein `?` in der URL vorhanden ist. Eine URL kann nur ein `?` enthalten.

| URL | Enthält&nbsp;`?` | Beschreibung | Beispiel |
| --- | --- | --- | --- |
| Standard-URL | Nein | Fügen Sie `?` nach dem schließenden Übersetzungs-Tag hinzu, wenn die URL noch keines enthält. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| Standard-URL | Ja | Verwenden Sie `&` am Ende der URL (nach dem schließenden Übersetzungs-Tag), wenn sie bereits `?` enthält. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Liquid-generiert | Nein | Verwenden Sie `?` nach den schließenden Übersetzungs-Tags, wenn die generierte URL noch keines enthält. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Liquid-generiert | Ja | Verwenden Sie `&` nach dem schließenden Übersetzungs-Tag, wenn die generierte URL bereits ein `?` enthält. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="E-Mail-Link-Tracking" }

### Spracheinstellungen und Barrierefreiheit {#language-settings-and-accessibility}

Beginnen Sie mit [Barrierefreiheitssprache]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language) unter [Barrierefreiheit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility) für WCAG-Kontext, Kanal- und Editor-Verhalten (einschließlich Landing-Pages) sowie Einstellungen zur **Barrierefreiheit** auf Nachrichtenebene.

Wenn Sie **mehrsprachige Nachrichten** verwenden, stimmen Sie die Barrierefreiheitssprache auf jedes Locale ab, damit lokalisierte Sendungen die passende Sprache deklarieren.

#### Die Barrierefreiheitssprache konfigurieren {#configuring-the-accessibility-language}

Sie können die Barrierefreiheitssprache auf zwei Ebenen festlegen:

##### Nachrichtenebene {#message-level}

Auf Nachrichtenebene legen Sie die Barrierefreiheitssprache im Abschnitt **Barrierefreiheit** Ihrer Nachrichteneinstellungen fest. Informationen zur Sprachauswahl, zur Verwendung von Liquid und zu Einschränkungen je nach Kanal finden Sie unter [Barrierefreiheitssprache]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language).

##### Locale-Ebene {#locale-level}

Für mehrsprachige Nachrichten legen Sie die Barrierefreiheitssprache für jedes Locale in den **Lokalisierungseinstellungen** fest. Sie können {% raw %}`{{accessibility_language}}`{% endraw %} im Abschnitt **Barrierefreiheit** verwenden, damit die Dokument- oder Kartensprache auf diese Locale-Werte abgebildet wird.

Ob dieses Token standardmäßig für neue Nachrichten angezeigt wird, hängt vom Kanal und Editor ab. Beispielsweise verhalten sich In-App Messages und Banner anders als Landing-Pages und Drag-and-Drop-E-Mails. Weitere Informationen finden Sie unter [Barrierefreiheitssprache]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#accessibility-language).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Welche Beschränkungen gelten für Übersetzungs-Tags? {#what-are-the-limits-for-translation-tags}

Bei der Verwendung von Übersetzungs-Tags gelten die folgenden Beschränkungen:

- Jede Nachricht kann bis zu 200 Übersetzungs-Tags enthalten.
- Jeder Standardtext (der Inhalt zwischen Übersetzungs-Tags) kann bis zu 2.000 Zeichen umfassen.
- Die Übersetzungen pro Gebietsschema können bis zu 409.600 Bytes (ungefähr 409,6&nbsp;KB) groß sein.

### Warum erhalte ich einen Fehler beim Herunterladen mehrsprachiger E-Mail-Templates? {#why-am-i-receiving-an-error-when-downloading-multi-language-email-templates}

Wenn beim Herunterladen mehrsprachiger E-Mail-Templates Fehler auftreten, umschließen die Übersetzungs-Tags möglicherweise HTML-Attribute oder CSS-Styling, die mit der Art und Weise kollidieren, wie Braze E-Mail-Bodys verarbeitet.

Braze behandelt den HTML-Body und den Plaintext-Body als separate Bestandteile derselben Nachricht. Wenn Übersetzungs-Tags `href`-Referenzen und CSS-Styling enthalten, kann dies zu widersprüchlichen Tags führen, die verhindern, dass das Template korrekt heruntergeladen wird.

So lösen Sie dieses Problem:
- Schließen Sie `href`-Referenzen und CSS-Styling aus Übersetzungs-Tags aus.
- Umschließen Sie nur menschenlesbaren Textinhalt mit Übersetzungs-Tags, wie in [HTML-Attribute und Struktur](#html-attributes-and-structure) beschrieben.
- Für URLs folgen Sie der Anleitung unter [URLs lokalisieren](#localize-urls).

#### Kann ich eine Änderung am übersetzten Text in einem meiner Gebietsschemata vornehmen? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

Ja. Nehmen Sie zunächst die Bearbeitung in der CSV-Datei vor und laden Sie die Datei dann erneut hoch, um eine Änderung am übersetzten Text vorzunehmen.

### Stellt Braze Übersetzungen bereit? {#does-braze-provide-translations}

Nein. Sie müssen [Ihre eigenen Übersetzungen bereitstellen](#step-4-add-translations), entweder durch das Hochladen einer CSV-Datei oder über die Übersetzungs-API.

### Kann ich Übersetzungs-Tags verschachteln? {#can-i-nest-translation-tags}

Nein.

#### Kann ich ganze HTML-Nachrichten in ein Übersetzungs-Tag einschließen? {#can-i-wrap-entire-html-messages-in-a-translation-tag}

Nein. Als Best Practice sollten Sie nur menschenlesbaren Text oder Inhalte umschließen, die lokalisiert werden müssen. Dies hilft, fehlerhafte Formatierungen, Links oder andere Nicht-Text-Elemente zu vermeiden.

Erwägen Sie außerdem, kleinere, semantisch zusammengehörige Textabschnitte zu umschließen, um genaue Übersetzungen zu erstellen und Performance- oder Größenbeschränkungen zu vermeiden.

#### Kann ich eine Änderung am übersetzten Text in einem meiner Gebietsschemata vornehmen?

Ja. Wenn Sie eine CSV-Datei verwenden, nehmen Sie zunächst die Bearbeitung in der Datei vor und laden Sie sie dann erneut hoch, um eine Änderung am übersetzten Text vorzunehmen. Wenn Sie die [Übersetzungs-API]({{site.baseurl}}/api/endpoints/translations) verwenden, nutzen Sie die Update-Endpunkte, um Änderungen vorzunehmen.

#### Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch? {#what-validations-or-extra-checks-does-braze-do}

| Szenario | Validierung in Braze |
| --- | --- |
| Eine Nachricht enthält zwei oder mehr übereinstimmende Übersetzungs-IDs, die auf unterschiedlichen Text verweisen. | Diese Übersetzungsdatei wird nicht heruntergeladen. |
| In einer Übersetzungsdatei fehlen eine oder mehrere Übersetzungs-Tag-IDs. | Diese Übersetzungsdatei wird nicht hochgeladen. |
| Eine Übersetzungsdatei enthält Gebietsschemata, die in der Nachricht fehlen. | Diese Übersetzungsdatei wird nicht hochgeladen. |
| Übersetzungs-Tags müssen einer Nachricht hinzugefügt werden, bevor das Übersetzungs-Template heruntergeladen wird. | Diese Übersetzungsdatei wird nicht heruntergeladen. |
| Übersetzungs-Tags, die in Ihrer hochgeladenen Datei gefunden wurden, fehlen in Ihrer Nachricht. | Zusätzliche Übersetzungen werden nicht in der Nachricht gespeichert. |
| {% raw %}Eine Nachricht enthält ein oder mehrere fehlerhafte Liquid-Tags. Öffnende Tags verwenden `{% translation your_id_here %}`, schließende Übersetzungs-Tags verwenden `{% endtranslation %}`.{% endraw %} | Diese Übersetzungsdatei wird nicht heruntergeladen. |
| Eine Übersetzungsdatei enthält Standardtext, der nicht mit dem Text in der Nachricht übereinstimmt. | Übersetzungen werden hinzugefügt, aber der ursprüngliche Nachrichtentext wird nicht aktualisiert. |
| Ein oder mehrere Gebietsschemata in einer Nachricht wurden in den Einstellungen gelöscht und existieren nicht mehr. | Bereits hinzugefügte Übersetzungen bleiben in der Nachricht erhalten. Wenn sie aus der Nachricht gelöscht werden, gehen die Übersetzungen verloren. |
| Übersetzungs-Tags enthalten vollständige URLs oder Liquid-generierte URLs. | Übersetzungs-Tags mit URLs werden identifiziert, falls Probleme mit fehlerhaften Links oder Link-Tracking auftreten. |
| Übersetzungs-Tags enthalten Abfrageparameter. | Übersetzungs-Tags mit Abfrageparametern werden identifiziert, falls Probleme mit fehlerhaften Links oder Link-Tracking auftreten. |
| Übersetzungs-Tags enthalten HTML-Attribute oder -Strukturen. | Übersetzungs-Tags mit HTML-Attributen oder -Strukturen werden identifiziert, falls Probleme mit Stilen und Formatierung auftreten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch?" }