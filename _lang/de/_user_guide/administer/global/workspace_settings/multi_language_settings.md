---
nav_title: Lokalisierungseinstellungen
article_title: Lokalisierungseinstellungen
alias: "/multi_language_support/"
page_order: 4
description: "Dieser Artikel bietet eine Übersicht über die mehrsprachigen Einstellungen im Braze-Dashboard und darüber, wie Sie Lokalisierungen in Ihrem Messaging verwenden können."
---

# Lokalisierungseinstellungen {#localization-settings}

> Das Mehrsprachen-Feature ermöglicht es Ihnen, [Übersetzungs-Tags]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) zu verwenden, um Nutzer:innen in verschiedenen Sprachen und an verschiedenen Standorten mit einer einzigen Nachricht anzusprechen.

## Voraussetzungen {#prerequisites}

{% multi_lang_include messaging/localization/locales.md section='multi-language prerequisites' %}

## Gebietsschema hinzufügen {#add-a-locale}

1. Gehen Sie zu **Einstellungen** > **Lokalisierungseinstellungen**.
2. Wählen Sie **Add locale** und dann **Default locale** oder **Custom Attributes**.
3. Geben Sie einen Namen für das Gebietsschema ein.
4. [Wählen Sie eine Sprache für die Barrierefreiheit aus]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility). Diese Einstellung ermöglicht es assistiven Technologien wie Screenreadern, Text korrekt auszusprechen.
5. Wählen Sie die entsprechenden Nutzerattribute für die von Ihnen gewählte Gebietsschema-Option aus. Beim Einrichten eines Gebietsschemas können Sie entweder Sprachen aus den Standard-Nutzerattributen oder aus angepassten Attributen auswählen. Eine Kombination aus beiden ist nicht möglich.

{% tabs %}
{% tab Default locale %}

Verwenden Sie für **Default locale** die Dropdown-Menüs, um die hinzuzufügende Sprache und optional das mit der Sprache zu verknüpfende Land auszuwählen.

![Ein Fenster mit dem Titel „Add locale – Default Language and Country“ zur Angabe der Sprache und des Landes.]({% image_buster /assets/img/multi-language_support/default_option.png %})

{% endtab %}
{% tab Custom attributes %}

Verwenden Sie für **Custom Attributes** das Dropdown-Menü, um das zugehörige angepasste Attribut auszuwählen, und geben Sie im Textfeld den Wert ein.

![Ein Fenster mit dem Titel „Add locale – Custom Attributes“ zur Angabe des angepassten Attributs und des Werts.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %})

{% endtab %}
{% endtabs %}

{: start="6"}
6. Wählen Sie **Add locale**.

Informationen zur Verwendung dieser Gebietsschemata in Ihren Nachrichten finden Sie unter [Gebietsschemata verwenden]({{site.baseurl}}/locales_in_messages).

## Hinweise {#considerations}

- Sie können bis zu zwei angepasste Attribute in einem einzelnen Gebietsschema oder bis zu zwei Standard-Nutzerattributsprachen auswählen. In beiden Fällen ist das zweite Attribut optional.
- Vermeiden Sie beim Bearbeiten der übersetzten Werte in der CSV-Datei Änderungen an den Standardwerten in der Datei.
- Der Gebietsschema-Schlüssel in Ihrer hochgeladenen Datei muss mit dem in Ihren Mehrsprachen-Einstellungen übereinstimmen.
- Um `device_locale` auf `zh_CN` (Vereinfachtes Chinesisch, wie es in Festlandchina verwendet wird) zu aktualisieren, müssen Sie eine `zh_CN`-Lokalisierungsdatei zu Ihrem Projekt hinzufügen, da iOS nativ `zh-Hans` verwendet.

### Support und Priorisierung {#support-and-prioritization}

- Wenn ein:e Nutzer:in sowohl einem durch angepasste Attribute definierten Gebietsschema als auch einem durch Standard-Nutzerattribute definierten Gebietsschema entspricht, wird das Gebietsschema mit angepassten Attributen priorisiert.
- Angepasste Attribute unterstützen Text-Werte (String) mit exakter Übereinstimmung.
- Wenn ein angepasstes Attribut gelöscht oder sein Typ geändert wird, kann die/der Nutzer:in nicht mehr in dieses Gebietsschema fallen und wird entweder in der Prioritätsliste der Gebietsschemata nach unten verschoben oder erhält die Standard-Marketing-Übersetzungen.
- Wenn ein Gebietsschema ungültig ist (das angepasste Attribut wurde geändert oder gelöscht), wird der Fehler auf der Seite **Multi-Language Support** angezeigt.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie viele Gebietsschemata kann ich hinzufügen? {#how-many-locales-can-i-add}

Sie können bis zu 200 Gebietsschemata hinzufügen.

### Wo werden die Übersetzungsdateien in Braze gespeichert? {#where-are-the-translation-files-stored-in-braze}

Übersetzungsdateien werden auf Campaign-Ebene gespeichert, d. h. für jede Nachrichtenvariante müssen Übersetzungen hochgeladen werden. Übersetzungen können auch in Content Blocks gespeichert werden. Wenn der Block einer Nachricht hinzugefügt wird, werden seine Übersetzungen automatisch einbezogen.

### Muss der Name des Gebietsschemas einem bestimmten Muster oder Format folgen? {#does-the-locale-name-have-to-follow-a-specific-pattern-or-format}

Nein. Sie können Ihre bevorzugte Namenskonvention verwenden. Der Name des Gebietsschemas wird bei der Auswahl des Gebietsschemas im Editor verwendet und erscheint in den Überschriften der Datei, die Sie mit Übersetzungs-IDs herunterladen.