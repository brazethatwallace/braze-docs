---
nav_title: Angepasste Daten verwalten
article_title: Angepasste Daten verwalten
page_order: 2
page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie angepasste Events und Attribute verwalten – Vorbelegen, Beschreibungen und Tags hinzufügen, Event-Eigenschaften verwalten, Datentypen erzwingen und Attribute als PII kennzeichnen."
---

# Angepasste Daten verwalten {#manage-custom-data}

> Auf dieser Seite erfahren Sie, wie Sie angepasste Daten in Ihren Campaigns und Segments vorbelegen, angepasste Events und Attribute sowie deren Eigenschaften verwalten und Datentypen konfigurieren. Informationen zum Blockieren und Löschen angepasster Daten finden Sie unter [Angepasste Daten blockieren]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

Wie Sie angepasste Attribute im Einzelnen verwalten (einschließlich Beschreibungen hinzufügen, Tags hinzufügen und Attribute als PII kennzeichnen), erfahren Sie unter [Angepasste Attribute verwalten]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes).

## Angepasste Daten vorbelegen {#pre-populate-custom-data}

Es kann vorkommen, dass Sie Campaigns und Segments mit angepassten Daten einrichten möchten, bevor Ihr Entwicklerteam diese angepassten Daten integriert hat. Braze ermöglicht es Ihnen, angepasste Events und Attribute im Dashboard vorzubelegen, bevor das Tracking dieser Daten beginnt, sodass diese Events und Attribute in Dropdowns und als Teil des Kampagnenerstellungsprozesses verfügbar sind.

Um angepasste Events und Attribute vorzubelegen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Events** oder **Angepasste Attribute** oder **Produkte**.

![Navigieren Sie zu „Angepasste Attribute“, „Angepasste Events“ oder „Produkte“.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2. Um ein angepasstes Attribut, Event oder Produkt hinzuzufügen, gehen Sie auf die entsprechende Seite und wählen Sie **Angepasste Attribute hinzufügen** oder **Angepasste Events hinzufügen** oder **Produkte hinzufügen**.<br><br>Für angepasste Attribute wählen Sie einen [Datentyp]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#custom-attribute-data-types) für dieses Attribut aus (z. B. Boolescher Wert oder String). Der Datentyp eines Attributs bestimmt die Segmentierungsfilter, die für dieses Attribut verfügbar sind. <br><br>![Neues Attribut oder Event hinzufügen]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3. Wählen Sie **Speichern**.

### Benennung angepasster Events und angepasster Attribute {#naming-custom-events-and-custom-attributes}

Bei angepassten Events und angepassten Attributen wird zwischen Groß- und Kleinschreibung unterschieden. Behalten Sie dies im Hinterkopf, wenn Ihr Entwicklerteam diese angepassten Events oder Attribute später integriert. Die angepassten Events oder Attribute müssen genau so benannt werden, wie Sie sie hier benannt haben, sonst generiert Braze ein anderes angepasstes Event oder Attribut.

## Eigenschaften verwalten {#managing-properties}

Nachdem Sie ein angepasstes Event oder Produkt erstellt haben, wählen Sie **Eigenschaften verwalten** für dieses Event oder Produkt aus, um neue Eigenschaften hinzuzufügen, vorhandene Eigenschaften zu blockieren und zu sehen, welche Campaigns oder Canvases diese Eigenschaft in einem [triggernden Event]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/) verwenden.

![Angepasste Eigenschaften für ein angepasstes Event.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Um Event- oder Produkt-Eigenschaften zu blockieren, verwenden Sie das Aktionsmenü auf der Eigenschaftenseite. Informationen zum vollständigen Blockieren angepasster Attribute, Events oder Produkte finden Sie unter [Angepasste Daten blockieren]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

Um diese hinzugefügten angepassten Attribute, Events, Produkte oder Event-Eigenschaften nachverfolgbar zu machen, müssen Sie Ihr Entwicklerteam bitten, sie im SDK unter genau dem Namen zu erstellen, den Sie zuvor verwendet haben. Alternativ können Sie die Braze [API]({{site.baseurl}}/api/basics/) verwenden, um Daten zu diesem Attribut zu importieren. Danach ist das angepasste Attribut, Event oder andere Datenobjekt aktiv und wird auf Ihre Nutzer:innen angewendet.

{% include alerts/note_alerts.md alert='Manage custom data storage' %}

## Datentyperkennung über Umgebungen hinweg {#data-type-detection-across-environments}

Braze erkennt den Datentyp eines angepassten Attributs automatisch anhand des ersten empfangenen Werts. Wenn Ihre Entwicklungsumgebung zuerst einen numerischen Wert wie `100` sendet, wird das Attribut als Zahl gespeichert. Wenn der erste Wert aus Ihrer Produktionsumgebung als String eintrifft (z. B. `"100"` in Anführungszeichen), wird das Attribut als String gespeichert.

Um dies zu vermeiden, stellen Sie sicher, dass Ihre Integration konsistente Datentypen über alle Umgebungen hinweg sendet. Wenn bereits der falsche Typ gesetzt ist, können Sie den korrekten Datentyp unter **Dateneinstellungen** > **Angepasste Attribute** über das [Datentyp-Dropdown](#forcing-data-type-comparisons) erzwingen.

## Datentypvergleiche erzwingen {#forcing-data-type-comparisons}

Braze erkennt automatisch die Datentypen für Attributdaten, die gesendet werden. Falls jedoch mehrere Datentypen auf ein einzelnes Attribut angewendet werden, können Sie den Datentyp eines beliebigen Attributs erzwingen, um Braze mitzuteilen, um welchen Typ es sich handelt. Wählen Sie dazu den gewünschten Typ aus dem Dropdown-Menü in der Spalte **Datentyp**.

{% alert note %}
Ab dem 30. März 2026 setzt die automatische Erkennung einen Datentyp nur noch bei der erstmaligen Aufnahme. Um den Datentyp nach der erstmaligen Aufnahme zu ändern, aktualisieren Sie ihn manuell mit den folgenden Schritten.
{% endalert %}

{% alert note %}
Das Erzwingen von Datentypen gilt nicht für Event-Eigenschaften oder Kauf-Details.
{% endalert %}

![Dropdown für den Datentyp angepasster Attribute]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Wenn Sie den Datentyp für ein Attribut erzwingen, werden alle eingehenden Daten, die nicht dem angegebenen Typ entsprechen, in diesen Typ umgewandelt. Wenn eine solche Umwandlung nicht möglich ist (z. B. ein String mit Buchstaben, der in eine Zahl umgewandelt werden soll), werden die Daten ignoriert. Alle Daten, die vor der Typänderung aufgenommen wurden, werden weiterhin als der alte Typ gespeichert (und können daher möglicherweise nicht segmentiert werden), und in den Profilen der betroffenen Nutzer:innen wird neben dem Attribut eine Warnung angezeigt.
{% endalert %}

### Vorhandene Daten nach einer Typänderung {#existing-data-after-a-type-change}

Das Erzwingen einer Datentypänderung wirkt sich nur auf neue Daten aus, die in Braze eingehen. Alle Daten, die vor der Typänderung aufgenommen wurden, werden weiterhin als der alte Typ gespeichert und sind möglicherweise nicht mit den Filtern des neuen Typs segmentierbar. In den Profilen der betroffenen Nutzer:innen wird eine Warnung angezeigt. Wenn bei neuen eingehenden Daten ein Wert nicht dem erzwungenen Typ entspricht, kann Braze ihn in den erzwungenen Typ umwandeln (z. B. den String `"100"` in die Zahl `100`); Werte, die nicht umgewandelt werden können, werden ignoriert und aktualisieren das Attribut nicht.

Wenn alle vorhandenen Nutzerdaten dem neuen Typ entsprechen sollen, müssen Sie die Attributwerte für diese Nutzer:innen erneut über das SDK, die API oder einen CSV-Import senden. Es gibt keine automatische Massenkonvertierung für vorhandene Daten.

### Datentypumwandlung {#data-type-coercion}

| Erzwungener Datentyp | Beschreibung |
|------------------|-------------|
| Boolescher Wert | Eingaben von `1`, `true`, `t` (Groß-/Kleinschreibung wird nicht berücksichtigt) werden als `true` gespeichert |
| Boolescher Wert | Eingaben von `0`, `false`, `f` (Groß-/Kleinschreibung wird nicht berücksichtigt) werden als `false` gespeichert |
| Zahl | Ganzzahlen oder Gleitkommazahlen (wie `1`, `1.5`) werden als Zahlen gespeichert |
| Zahl | Numerische Strings (wie `"100"` oder `"3.14"`) können in Zahlen umgewandelt werden, wenn das Attribut auf **Zahl** erzwungen wird |
| String | Numerische Werte können in ihre String-Form umgewandelt werden, wenn das Attribut auf **String** erzwungen wird |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datentypumwandlung" }

Weitere Informationen zu den spezifischen Filteroptionen, die bei verschiedenen Datentypvergleichen zur Verfügung stehen, finden Sie unter [Berichte konfigurieren]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting/). Weitere Informationen zu den verschiedenen verfügbaren Datentypen finden Sie unter [Datentypen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#custom-attribute-data-types).

{% alert note %}
An Braze gesendete Daten sind unveränderlich und können nicht gelöscht oder verändert werden, nachdem Braze sie erhalten hat. Sie können jedoch jeden der in den vorangegangenen Abschnitten aufgeführten Schritte verwenden, um zu kontrollieren, was Sie in Ihrem Dashboard tracken. Informationen zum Blockieren oder Löschen angepasster Daten finden Sie unter [Angepasste Daten blockieren]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).
{% endalert %}