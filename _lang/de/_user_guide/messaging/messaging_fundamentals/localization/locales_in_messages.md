---
nav_title: Mehrsprachige Nachrichten
article_title: Mehrsprachige Nachrichten
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Dieser Artikel beschreibt die Schritte zur Verwendung von Locales in Ihren Nachrichten."
---

# Mehrsprachige Nachrichten {#multi-language-messages}

> Nachdem Sie Locales zu Ihrem Workspace hinzugefügt haben, können Sie Nutzer:innen in verschiedenen Sprachen innerhalb einer einzigen Push-Nachricht, E-Mail, eines Banners, einer In-App-Nachricht oder eines Content-Blocks ansprechen.

## Voraussetzungen {#prerequisites}

Sehen Sie sich das folgende Video an, um einen optionalen Überblick über die Einrichtung und Verwendung mehrsprachiger Nachrichten zu erhalten.

{% multi_lang_include video.html id="whfstwrel5" source="wistia" %}

{% tabs %}
{% tab Mehrsprachige Locales %}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

{% endtab %}
{% tab Nachrichtentypen %}

| Feature | Erforderliche Nutzer:innenberechtigungen |
| --- | --- |
| Nachrichtentypen | Sie benötigen diese Berechtigungen, um Locales und Übersetzungen zu Campaigns und Canvases hinzuzufügen:<br><br> <ul><li>Campaigns bearbeiten</li><li>Canvases bearbeiten</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen"}

{% endtab %}
{% tab Templates %}

| Feature | Erforderliche Nutzer:innenberechtigungen |
| --- | --- |
| Templates | Sie benötigen diese Berechtigungen für den Template-Typ, dem Sie Locales und Übersetzungen hinzufügen möchten:<br><br> <ul><li>E-Mail-Templates bearbeiten</li><li>IAM-Templates bearbeiten</li><li>Content-Block-Templates bearbeiten</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

{% endtab %}
{% endtabs %}

## Locales verwenden {#use-locales}

### 1. Schritt: Locales einrichten {#step-1-set-up-locales}

Bevor Sie Übersetzungen zu einer Nachricht hinzufügen können, müssen Sie zunächst [die Locales erstellen, die Sie unterstützen möchten]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/). Locales definieren die Sprach- (und optional Regions-)Varianten, die für das Messaging verfügbar sind.

### 2. Schritt: Inhalte für die Übersetzung markieren {#step-2-mark-content-for-translation}

Umschließen Sie Text, den Sie übersetzen möchten, mit den Liquid-Übersetzungs-Tags {% raw %}`{% translation your_id_here %}` und `{% endtranslation %}`{% endraw %} und weisen Sie eine Tag-ID zu. Übersetzungs-Tag-IDs müssen innerhalb einer Nachricht eindeutig sein. Verwenden Sie semantische ID-Namen, die den Text klar beschreiben, wie z. B. {% raw %}`{% translation header %}`{% endraw %}.

Hier ist ein Beispiel für eine zur Übersetzung markierte Nachricht: {% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

{% alert tip %}
Markieren Sie den Text, den Sie übersetzen möchten, und verwenden Sie die Tastenkombination **Cmd + Alt + L** (macOS) oder **Strg + Alt + L** (Windows), um ihn in Übersetzungs-Tags einzuschließen.<br><br> Diese Tastenkombination funktioniert in allen Kanälen, die mehrsprachiges Messaging unterstützen, mit Ausnahme der Drag-and-Drop-Editoren für E-Mail und Content Blocks. Verwenden Sie dort den Button **Add personalization** in der linken Seitenleiste, um Übersetzungs-Tags hinzuzufügen.
{% endalert %}

#### URLs lokalisieren {#localize-urls}

Beim Übersetzen von Inhalten erfordern URLs eine besondere Behandlung, um fehlerhafte Links zu vermeiden.

##### Standard-URLs (statisch) {#standard-static-urls}

Statische URLs werden manuell im Editor eingegeben (z. B. `https://example.com`). Wir empfehlen außerdem Folgendes:

| Empfehlung | Begründung |
| --- | --- |
| Belassen Sie das Protokoll (`https://`) außerhalb der Übersetzungs-Tags. Umschließen Sie nur die Domain und den Pfad (z. B. `example.com/en`). | Übersetzer:innen könnten versehentlich Sonderzeichen ändern oder entfernen, was zu fehlerhaften Links führt. |
| Fügen Sie keine Query-Parameter in Übersetzungs-Tags ein (z. B. `?utm_source=promo`). | Übersetzer:innen könnten versehentlich Sonderzeichen ändern oder entfernen, was zu fehlerhaften Links führt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Standard-URLs (statisch)" }

Eine Standard-URL, die beide Empfehlungen befolgt, sieht so aus:

{% raw %}
```
<a href="https://{% translation id_1 %}example.shop.com{% endtranslation %}">Visit our store</a>
```
{% endraw %}

##### Liquid-generierte URLs {#liquid-generated-urls}

Wenn Ihre URL mit Liquid generiert wird (z. B. {% raw %}`{% landing_page_url %}`{% endraw %}), empfehlen wir Folgendes:

| Empfehlung | Begründung |
| --- | --- |
| Umschließen Sie die Liquid-generierte URL nur dann mit Übersetzungs-Tags, wenn sie lokalisiert werden muss. | Die Liquid-Syntax muss sorgfältig beibehalten werden, damit sie korrekt gerendert wird. |
| Fügen Sie keine Query-Parameter (z. B. `?utm_source=promo`) in Übersetzungs-Tags ein. | Übersetzer:innen könnten versehentlich Sonderzeichen ändern oder entfernen, was zu fehlerhaften Links führt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid-generierte URLs" }

Eine Liquid-generierte URL, die beide Empfehlungen befolgt, sieht so aus:

{% raw %}
```
<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}">View details</a>
```
{% endraw %}

{% alert important %}
Wenn Sie [E-Mail-Link-Tracking](#email-link-tracking) (Link Aliasing oder Link-Templates) verwenden, ist eine zusätzliche Konfiguration erforderlich, wenn URLs in Übersetzungs-Tags eingeschlossen sind.
{% endalert %}

#### HTML-Attribute und -Struktur {#html-attributes-and-structure}

Umschließen Sie nur für Menschen lesbaren Text mit Übersetzungs-Tags. Vermeiden Sie es, HTML-Attribute (wie `class`, `style` oder `id`) oder anderen strukturellen Code einzuschließen. HTML-Attribute steuern Layout, Styling und Funktionalität. Wenn Sie sie in Übersetzungs-Tags einschließen, kann dies die Formatierung oder Styles in lokalisierten Versionen Ihrer Nachricht beschädigen.

Dieser Text ist korrekt eingeschlossen:

{% raw %}
```
<p class="headline" style="color: red;">
  {% translation id_1 %}Welcome to our sale{% endtranslation %}
</p>
```
{% endraw %}

{% details Falsch eingeschlossener Text %}

Dieser Text ist **falsch** eingeschlossen:

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

### 3. Schritt: Locales zu Ihrer Nachricht hinzufügen {#step-3-add-locales-to-your-message}

Nachdem Sie Übersetzungs-Tags zu Ihrer Nachricht hinzugefügt haben, wählen Sie im Editor **Manage languages** (in den Drag-and-Drop-Editoren für E-Mail und Content Blocks: **Languages**) und wählen Sie mindestens ein Locale aus, für das Sie Übersetzungen hinzufügen möchten.

![Das Dropdown-Menü „Locale hinzufügen“ mit Optionen zur Auswahl des Standard-Locales oder angepasster Attribute.]({% image_buster /assets/img/multi-language_support/select_locale_type.png %}){: style="max-width:70%;"}

#### Content Blocks mit Übersetzungen {#content-blocks-containing-translation}

Wenn Ihre Nachricht Content Blocks enthält, in denen bereits Übersetzungen gespeichert sind, müssen Sie diese Übersetzungen nicht erneut hochladen. Gespeicherte Übersetzungen werden automatisch angewendet, wenn der Content-Block zu Ihrer Nachricht hinzugefügt wird.

Im Modal **Manage languages** erscheinen Content Blocks mit gespeicherten Übersetzungen in der Liste zusammen mit den Locales, die sie unterstützen. So können Sie sehen, welche Teile Ihrer Nachricht bereits lokalisiert sind, bevor Sie neue Übersetzungen hinzufügen.

![Der Bereich „Manage languages“ mit einer Liste von Content Blocks, die gespeicherte Übersetzungen haben.]({% image_buster /assets/img/multi-language_support/content_blocks_translations.png %}){: style="max-width:70%;"}

{% alert important %}
Stellen Sie sicher, dass jeder Content-Block Übersetzungen für jedes Locale enthält, das zu Ihrer Nachricht hinzugefügt wurde. Wenn einem Content-Block Übersetzungen für eines der hinzugefügten Locales fehlen, wird er für Nutzer:innen in diesem Locale in seiner Originalsprache angezeigt.
{% endalert %}

### 4. Schritt: Übersetzungen hinzufügen {#step-4-add-translations}

Nachdem Sie Locales ausgewählt haben, fügen Sie Übersetzungen zu Ihrer Nachricht mit einer der folgenden Methoden hinzu:

![Der Tab „Übersetzungen hinzufügen“ mit Optionen zum Hochladen von Übersetzungen per CSV oder durch Verbindung mit Übersetzungspartnern.]({% image_buster /assets/img/multi-language_support/add_translations.png %}){: style="max-width:70%;"}

{% tabs %}
{% tab CSV-Template hochladen %}

Wählen Sie **Download template**, um eine CSV-Datei herunterzuladen, die eine Matrix Ihrer ausgewählten Übersetzungs-IDs und Locales enthält. Geben Sie die Übersetzungen für jedes Locale ein. Laden Sie die fertige Datei hoch, und die Übersetzungen werden auf Ihre Nachricht angewendet.

{% alert important %}
Um Anzeigeprobleme mit nicht-englischen Zeichen zu vermeiden, verwenden Sie Excel nicht für Ihre Übersetzungs-CSV.
{% endalert %}

![CSV mit Übersetzungs-Tags für einen Titel, Angebotstext, Angebotsbetrag und CTA.]({% image_buster /assets/img/multi-language_support/csv_template_example.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Übersetzungs-API verwenden %}

Verwenden Sie eine Partner-Übersetzungs-API, um Übersetzungen in Ihren Campaigns und Canvases zu verwalten und zu aktualisieren. Dies ist nützlich, wenn Sie ein externes System für die Lokalisierung verwenden oder eine direkte Verbindung mit einem Übersetzungspartner herstellen möchten.

Um die Übersetzungs-Endpunkte mit Canvases zu verwenden, geben Sie die folgenden Parameter an:
  - `workflow_id`
  - `step_id`
  - `message_variation_id`

{% alert note %}
Wenn Sie die Übersetzungs-API mit Canvas-Schritten verwenden, die nach dem Start des Canvas erstellt wurden, ist die `message_variation_id`, die Sie an die API übergeben, leer.
{% endalert %}

{% endtab %}
{% endtabs %}

### 5. Schritt: Übersetzungen in der Vorschau anzeigen {#step-5-preview-translations}

Um eine Vorschau Ihrer Nachricht anzuzeigen, wählen Sie die Option **Multi-Language User** aus dem Dropdown **Preview as User**. So können Sie zwischen verschiedenen Locale-Definitionen wechseln, um alle Übersetzungen Ihrer Nachricht in der Vorschau anzuzeigen.

![Locale-Vorschauen]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

## Übersetzungen verwalten {#manage-translations}

### Canvas-Schritte oder Campaigns duplizieren und Übersetzungen {#duplicate-canvas-steps-or-campaigns-and-translations}

Wenn Sie einen Canvas-Schritt, eine Campaign oder eine Variante duplizieren, werden Übersetzungen mit übernommen. Dies gilt auch beim Kopieren über Workspaces hinweg, sofern die Locales im Ziel-Workspace definiert sind. Überprüfen und aktualisieren Sie die Übersetzungen entsprechend, wenn Sie Änderungen an Ihrem Canvas oder Ihrer Campaign vornehmen.

### Übersetzungen in Content Blocks speichern {#save-translations-in-content-blocks}

Content Blocks unterstützen Mehrsprachigkeit auf die gleiche Weise wie Nachrichten. Beim Erstellen oder Bearbeiten von Content Blocks können Sie Inhalte für die Übersetzung markieren, Locales hinzufügen und Übersetzungen per CSV oder über die [Übersetzungs-API]({{site.baseurl}}/api/endpoints/translations/) hochladen.

Gespeicherte Übersetzungen bleiben mit dem Content-Block verknüpft. Wenn der Block zu einer Nachricht hinzugefügt wird, werden seine Übersetzungen automatisch einbezogen.

### Rechts-nach-links-Nachrichten {#right-to-left-messages}

Wenn Sie die Übersetzungsdatei für Sprachen ausfüllen, die von rechts nach links geschrieben werden (wie Arabisch), umschließen Sie die Übersetzung mit `span`, damit sie korrekt formatiert wird:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

### E-Mail-Link-Tracking {#email-link-tracking}

In E-Mail-Campaigns verfolgt Braze Links, indem Tracking-Informationen (Query-Parameter) zu jeder URL hinzugefügt werden. Dieses Verhalten unterstützt sowohl [Link Aliasing]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing/) als auch [Link-Templating]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template/).

Wenn eine URL in Übersetzungs-Tags eingeschlossen ist, kann Braze möglicherweise nicht bestimmen, wo diese Tracking-Informationen hinzugefügt werden sollen. Um sicherzustellen, dass dies korrekt funktioniert, müssen Sie ein Sonderzeichen am Ende der URL einfügen, um anzugeben, wo das Tracking hinzugefügt werden soll.

URLs verwenden zwei Sonderzeichen, um dies zu steuern:
  - `?` fügt Tracking zu einer URL hinzu, die noch keines hat.
  - `&` fügt zusätzliches Tracking hinzu, wenn bereits ein `?` in der URL vorhanden ist. Eine URL kann nur ein `?` enthalten.

| URL | Enthält&nbsp;`?` | Beschreibung | Beispiel |
| --- | --- | --- | --- |
| Standard-URL | Nein | Fügen Sie `?` nach dem schließenden Übersetzungs-Tag hinzu, wenn die URL noch keines enthält. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?">Shop Now</a>```{% endraw %} |
| Standard-URL | Ja | Verwenden Sie `&` am Ende der URL (nach dem schließenden Übersetzungs-Tag), wenn sie bereits `?` enthält. | {% raw %}```<a href="https://{% translation id_1 %}example.com{% endtranslation %}?ref=4&">Shop Now</a>```{% endraw %} |
| Liquid-generiert | Nein | Verwenden Sie `?` nach den schließenden Übersetzungs-Tags, wenn die generierte URL noch keines enthält. | {% raw %}```<a href="{% translation id_1 %}{{ product_url }}{% endtranslation %}?">Shop Now</a>``` {% endraw %} |
| Liquid-generiert | Ja | Verwenden Sie `&` nach dem schließenden Übersetzungs-Tag, wenn die generierte URL bereits ein `?` enthält. | {% raw %}```<a href="{% translation id_1 %}{% landing_page_url xyz %}{% endtranslation %}&">Shop Now</a>```{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="E-Mail-Link-Tracking" }

### Spracheinstellungen und Barrierefreiheit {#language-settings-and-accessibility}

Beginnen Sie mit [Barrierefreiheitssprache]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/#accessibility-language) unter [Barrierefreiheit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/) für den WCAG-Kontext, das Verhalten von Kanälen und Editoren (einschließlich Landing-Pages) sowie die **Accessibility**-Einstellungen auf Nachrichtenebene.

Wenn Sie **mehrsprachige Nachrichten** verwenden, stimmen Sie die Barrierefreiheitssprache mit jedem Locale ab, damit lokalisierte Sendungen die entsprechende Sprache deklarieren.

#### Barrierefreiheitssprache konfigurieren {#configuring-the-accessibility-language}

Sie können die Barrierefreiheitssprache auf zwei Ebenen festlegen:

##### Nachrichtenebene {#message-level}

Auf Nachrichtenebene legen Sie die Barrierefreiheitssprache im Abschnitt **Accessibility** Ihrer Nachrichteneinstellungen fest. Informationen zur Sprachauswahl, zur Verwendung von Liquid und zu Einschränkungen nach Kanal finden Sie unter [Barrierefreiheitssprache]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/#accessibility-language).

##### Locale-Ebene {#locale-level}

Für mehrsprachige Nachrichten legen Sie die Barrierefreiheitssprache für jedes Locale in den **Einstellungen für die Lokalisierung** fest. Sie können {% raw %}`{{accessibility_language}}`{% endraw %} im Abschnitt **Accessibility** verwenden, damit die Dokument- oder Card-Sprache diesen Locale-Werten zugeordnet wird.

Ob dieses Token bei neuen Nachrichten standardmäßig angezeigt wird, hängt vom Kanal und Editor ab. Beispielsweise verhalten sich In-App Messages und Banner anders als Landing-Pages und Drag-and-Drop-E-Mails. Weitere Informationen finden Sie unter [Barrierefreiheitssprache]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility/#accessibility-language).

## Häufig gestellte Fragen {#frequently-asked-questions}

#### Welche Limits gelten für Übersetzungs-Tags? {#what-are-the-limits-for-translation-tags}

Bei der Verwendung von Übersetzungs-Tags gelten die folgenden Limits:

- Jede Nachricht kann bis zu 200 Übersetzungs-Tags enthalten.
- Jeder Standardtext (der Inhalt zwischen Übersetzungs-Tags) kann bis zu 2.000 Zeichen umfassen.
- Die Übersetzungen pro Locale können bis zu 409.600 Bytes (ca. 409,6&nbsp;KB) umfassen.

#### Kann ich eine Änderung am übersetzten Text in einem meiner Locales vornehmen? {#can-i-make-a-change-to-the-translated-copy-in-one-of-my-locales}

Ja. Nehmen Sie zuerst die Änderung in der CSV-Datei vor und laden Sie die Datei dann erneut hoch, um den übersetzten Text zu ändern.

### Stellt Braze Übersetzungen bereit? {#does-braze-provide-translations}

Nein. Sie müssen [Ihre eigenen Übersetzungen bereitstellen](#step-4-add-translations), entweder durch Hochladen einer CSV-Datei oder über die Übersetzungs-API.

### Kann ich Übersetzungs-Tags verschachteln? {#can-i-nest-translation-tags}

Nein.

#### Kann ich ganze HTML-Nachrichten in ein Übersetzungs-Tag einschließen? {#can-i-wrap-entire-html-messages-in-a-translation-tag}

Nein. Als Best Practice sollten Sie nur für Menschen lesbaren Text oder Inhalte einschließen, die lokalisiert werden müssen. Dies hilft, fehlerhafte Formatierungen, Links oder andere Nicht-Text-Elemente zu vermeiden.

Erwägen Sie außerdem, kleinere, semantisch zusammenhängende Textabschnitte einzuschließen, um genaue Übersetzungen zu erstellen und Performance- oder Größenbeschränkungen zu vermeiden.

#### Kann ich eine Änderung am übersetzten Text in einem meiner Locales vornehmen?

Ja. Wenn Sie eine CSV-Datei verwenden, nehmen Sie zuerst die Änderung in der Datei vor und laden Sie sie dann erneut hoch, um den übersetzten Text zu ändern. Wenn Sie die [Übersetzungs-API]({{site.baseurl}}/api/endpoints/translations/) verwenden, nutzen Sie die Update-Endpunkte, um Änderungen vorzunehmen.

#### Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch? {#what-validations-or-extra-checks-does-braze-do}

| Szenario | Validierung in Braze |
| --- | --- |
| Eine Nachricht enthält zwei oder mehr übereinstimmende Übersetzungs-IDs, die auf unterschiedlichen Text verweisen. | Diese Übersetzungsdatei wird nicht heruntergeladen. |
| Einer Übersetzungsdatei fehlen eine oder mehrere Übersetzungs-Tag-IDs. | Diese Übersetzungsdatei wird nicht hochgeladen. |
| Eine Übersetzungsdatei enthält Locales, die in der Nachricht fehlen. | Diese Übersetzungsdatei wird nicht hochgeladen. |
| Übersetzungs-Tags müssen zu einer Nachricht hinzugefügt werden, bevor das Übersetzungs-Template heruntergeladen wird. | Diese Übersetzungsdatei wird nicht heruntergeladen. |
| Übersetzungs-Tags in Ihrer hochgeladenen Datei fehlen in Ihrer Nachricht. | Zusätzliche Übersetzungen werden nicht in der Nachricht gespeichert. |
| {% raw %}Eine Nachricht enthält einen oder mehrere fehlerhafte Liquid-Tags. Verwenden Sie zum Öffnen `{% translation your_id_here %}` und schließen Sie Übersetzungs-Tags mit `{% endtranslation %}`.{% endraw %} | Diese Übersetzungsdatei wird nicht heruntergeladen. |
| Eine Übersetzungsdatei enthält Standardtext, der nicht mit dem Text in der Nachricht übereinstimmt. | Übersetzungen werden hinzugefügt, aber der ursprüngliche Nachrichtentext wird nicht aktualisiert. |
| Eines oder mehrere der Locales in einer Nachricht wurden in den Einstellungen gelöscht und existieren nicht mehr. | Bereits hinzugefügte Übersetzungen bleiben in der Nachricht bestehen. Wenn sie aus der Nachricht gelöscht werden, gehen die Übersetzungen verloren. |
| Übersetzungs-Tags enthalten vollständige URLs oder Liquid-generierte URLs. | Übersetzungs-Tags mit URLs werden identifiziert, falls Probleme mit fehlerhaften Links oder Link-Tracking auftreten. |
| Übersetzungs-Tags enthalten Query-Parameter. | Übersetzungs-Tags mit Query-Parametern werden identifiziert, falls Probleme mit fehlerhaften Links oder Link-Tracking auftreten. |
| Übersetzungs-Tags enthalten HTML-Attribute oder -Strukturen. | Übersetzungs-Tags mit HTML-Attributen oder -Strukturen werden identifiziert, falls Probleme mit Styles und Formatierung auftreten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch?" }