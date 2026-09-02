---
nav_title: Liquid verwenden
article_title: Liquid verwenden
page_order: 0
description: "Dieser Referenzartikel bietet einen Überblick über gängige Liquid-Anwendungsfälle und wie Sie Liquid-Tags in Ihr Messaging einbinden können."
search_rank: 2
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Liquid verwenden {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdynamic-personalization-with-liquid-stylefloatrightwidth120pxborder0-classnoimgborderuse-liquid}

> Dieser Artikel zeigt Ihnen, wie Sie verschiedene Nutzerattribute verwenden können, um persönliche Informationen dynamisch in Ihr Messaging einzufügen.

Liquid ist eine Open-Source-Template-Sprache, die von Shopify entwickelt und in Ruby geschrieben wurde. Sie können sie in Braze nutzen, um Nutzerprofildaten in Ihre Nachrichten einzubinden und diese Daten anzupassen. Beispielsweise können Sie Liquid-Tags verwenden, um bedingte Nachrichten zu erstellen, etwa um verschiedene Angebote basierend auf dem Abo-Jubiläumsdatum einer Nutzerin oder eines Nutzers zu versenden. Darüber hinaus können Filter Daten manipulieren, z. B. das Registrierungsdatum einer Nutzerin oder eines Nutzers von einem Zeitstempel in ein besser lesbares Format umwandeln, wie „15. Januar 2022“. Weitere Details zur Liquid-Syntax und ihren Möglichkeiten finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Funktionsweise {#how-it-works}

Liquid-Tags fungieren als Platzhalter in Ihren Nachrichten, die genehmigte Informationen aus dem Konto Ihrer Nutzer:innen abrufen und Personalisierung sowie relevante Messaging-Praktiken ermöglichen können.

Im folgenden Block sehen Sie eine doppelte Verwendung eines Liquid-Tags, um den Vornamen der Nutzer:innen abzurufen, sowie einen Standard-Tag für den Fall, dass ein:e Nutzer:in keinen Vornamen hinterlegt hat.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Für eine Nutzerin namens Janet Doe würde die Nachricht folgendermaßen erscheinen:

```
Hi Janet, thanks for using the App!
```

Oder...

```
Hi Valued User, thanks for using the App!
```

{% alert important %}
HTML-Kommentare (`<!-- -->`) werden entfernt, bevor Liquid gelesen wird. Daher werden Liquid-Tags innerhalb von HTML-Kommentaren in Ihrer Nachricht **nicht** gerendert. Für eine korrekte Darstellung stellen Sie sicher, dass sich alle Liquid-Tags, die Sie verwenden möchten, außerhalb von HTML-Kommentaren befinden.
{% endalert %}

## Unterstützte Werte zum Einsetzen {#supported-values-to-substitute}

Die folgenden Werte können je nach Verfügbarkeit in eine Nachricht eingesetzt werden:

- [Grundlegende Nutzerinformationen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) (zum Beispiel `first_name`, `last_name`, `email_address`)
- [Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
    - [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#liquid-templating)
- [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- [Zuletzt verwendete Geräteinformationen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#most-recently-used-device-information)
- [Zielgeräteinformationen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information)

Sie können Inhalte auch direkt von einem Webserver über Braze [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) abrufen.

{% alert important %}
Braze unterstützt derzeit Liquid bis einschließlich Liquid 5 von Shopify.
{% endalert %}

## Liquid verwenden {#using-liquid}

Mit [Liquid-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) können Sie die Qualität Ihrer Nachrichten steigern, indem Sie ihnen eine persönliche Note verleihen.

### Liquid-Syntax {#liquid-syntax}

Liquid folgt einer bestimmten Struktur bzw. Syntax, die Sie beim Erstellen dynamischer Personalisierung beachten müssen. Hier sind einige grundlegende Regeln, die Sie im Hinterkopf behalten sollten:

- **Verwenden Sie gerade Anführungszeichen in Braze:** Es gibt einen Unterschied zwischen typografischen Anführungszeichen (**' '**) und geraden Anführungszeichen (**&#39; &#39;**). Verwenden Sie gerade Anführungszeichen (**&#39; &#39;**) in Ihrem Liquid in Braze. Beim Kopieren und Einfügen aus bestimmten Texteditoren können typografische Anführungszeichen erscheinen, die Probleme in Ihrem Liquid verursachen können. Wenn Sie Anführungszeichen direkt im Braze-Dashboard eingeben, sind Sie auf der sicheren Seite.
- **Klammern kommen paarweise vor:** Jede Klammer muss sowohl geöffnet als auch geschlossen werden **{ }**. Achten Sie darauf, geschweifte Klammern zu verwenden.
- **If-Anweisungen kommen paarweise vor:** Für jedes `if` benötigen Sie ein `endif`, um anzuzeigen, dass die `if`-Anweisung beendet ist.
- **Case-Anweisungen kommen paarweise vor:** Für jedes `case` benötigen Sie ein `endcase`, um den Block zu schließen.
- **Variablennamen müssen ASCII-Zeichen verwenden:** Liquid-Variablennamen (erstellt mit `assign` oder `capture`) unterstützen nur ASCII-Buchstaben, Ziffern und Unterstriche. Braze-Personalisierungsattributnamen (innerhalb von `custom_attribute.${...}` oder `event_properties.${...}`) können Nicht-ASCII-Zeichen enthalten.
- **Braze-Liquid-Variablen in mehrzeiligen `assign`-Tags mit doppelten geschweiften Klammern umschließen:** Verwenden Sie doppelte geschweifte Klammern {% raw %}(`{{ }}`){% endraw %} um Braze-Liquid-Variablen, wenn ein `assign` über mehrere Zeilen geht.

#### Mehrzeilige `assign`-Tags {#multi-line-assign-tags}

Sie können ein `assign` über mehrere Zeilen aufteilen (zum Beispiel, indem Sie Filter mit `|` vor dem schließenden Tag fortsetzen), solange Sie alle Braze-Liquid-Variablen mit doppelten geschweiften Klammern {% raw %}(`{{ }}`){% endraw %} umschließen. Ohne diese Klammern können mehrzeilige Assign-Anweisungen zu unerwartetem Rendering führen, einschließlich angepasster Attribute, die nicht korrekt als Template eingefügt werden. Das folgende Beispiel zeigt ein funktionierendes mehrzeiliges Assign:

{% raw %}
```liquid
{%- assign color = {{custom_attribute.${favorite_color}}}
| default: {{custom_attribute.${fav_color}}}
| default: 'blue'
%}
```

Sie können das vollständige `assign` auch in einer Zeile schreiben:

```liquid
{%- assign color = custom_attribute.${favorite_color} | default: custom_attribute.${fav_color} | default: 'blue' %}
```
{% endraw %}

#### Wo Operatoren und Filter verwendet werden können {#where-to-use-operators-and-filters}

Operatoren (wie `==`, `!=`, `>`, `and`, `or`) und Filter (wie `| size`, `| plus`) können jeweils nur in bestimmten Liquid-Kontexten verwendet werden.

| Kontext | Operatoren | Filter |
|-----------|-----------|---------|
| `assign` | Nicht unterstützt | Unterstützt |
| `if`, `elsif`, `unless` | Unterstützt | Nicht unterstützt |
| `case`, `when` | Nur Gleichheitsvergleich[^case_when_ops] | Nicht unterstützt |
| `for` | Nicht unterstützt | Nicht unterstützt |
| Array-Zugriff (`[ ]`) | Nicht unterstützt | Nicht unterstützt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Wo Operatoren und Filter verwendet werden können" }

[^case_when_ops]: In `case`- und `when`-Tags vergleicht Liquid den `case`-Ausdruck mit jedem `when`-Wert mittels Gleichheit (ähnlich wie die Verkettung von `if` und `elsif` mit `==`). Sie können keine beliebigen Vergleichs- oder logischen Operatoren innerhalb einer `when`-Klausel verwenden, wie Sie es mit `if` und `elsif` tun. Beispiele finden Sie unter [Bedingte Nachrichtenlogik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#case-and-when).

Wenn Sie einen gefilterten Wert in einem Kontext benötigen, der keine Filter unterstützt, weisen Sie das Ergebnis zuerst einer Variablen zu.

{% raw %}

##### Ein Filterergebnis in einer Bedingung verwenden {#use-a-filter-result-in-a-conditional}

Sie können einen Filter nicht direkt in einer bedingten Anweisung verwenden. Dies ist falsch:

```liquid
{% if my_array | size > 3 %}
You have more than 3 items!
{% endif %}
```

Weisen Sie stattdessen das Filterergebnis einer Variablen zu:

```liquid
{% assign array_size = my_array | size %}
{% if array_size > 3 %}
You have more than 3 items!
{% endif %}
```

##### Ein Filterergebnis in einer For-Schleife verwenden {#use-a-filter-result-in-a-for-loop}

Sie können keinen Filter auf das Iterable in einer `for`-Schleife anwenden. Dies ist falsch:

```liquid
{% for item in my_array | reverse %}
{{ item }}
{% endfor %}
```

Weisen Sie stattdessen den gefilterten Wert einer Variablen zu:

```liquid
{% assign reversed = my_array | reverse %}
{% for item in reversed %}
{{ item }}
{% endfor %}
```

##### Ein Filterergebnis für den Array-Zugriff verwenden {#use-a-filter-result-for-array-access}

Sie können keinen Filter innerhalb eckiger Klammern verwenden. Dies ist falsch:

```liquid
{{ my_array[my_var | minus: 1] }}
```

Weisen Sie stattdessen zuerst den gefilterten Wert zu:

```liquid
{% assign adjusted_index = my_var | minus: 1 %}
{{ my_array[adjusted_index] }}
```

##### Ein Vergleichsergebnis in einer Variablen speichern {#store-a-comparison-result-in-a-variable}

Sie können keinen Operator in einer `assign`-Anweisung verwenden. Dies ist falsch:

```liquid
{% assign is_vip = total_spend > 100 %}
{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

Verwenden Sie stattdessen eine Bedingung, um die Variable zu setzen:

```liquid
{% assign is_vip = false %}
{% if total_spend > 100 %}
{% assign is_vip = true %}
{% endif %}

{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

{% endraw %}

#### Standardattribute und angepasste Attribute {#default-attributes-and-custom-attributes}

{% raw %}

Wenn Sie den folgenden Text in Ihre Nachricht einfügen: `{{${first_name}}}`, wird der Vorname der Nutzer:in (aus dem Kundenprofil or Nutzerprofil abgerufen) beim Senden der Nachricht eingesetzt. Sie können dasselbe Format mit anderen Standardattributen verwenden.

Wenn Sie den Wert eines angepassten Attributs verwenden möchten, müssen Sie den Namespace „custom_attribute“ zur Variablen hinzufügen. Um beispielsweise ein angepasstes Attribut namens „zip code“ zu verwenden, würden Sie `{{custom_attribute.${zip code}}}` in Ihre Nachricht einfügen.

### Tags einfügen {#inserting-tags}

Sie können Tags einfügen, indem Sie zwei öffnende geschweifte Klammern `{{` in einer beliebigen Nachricht eingeben. Dadurch wird eine Autovervollständigungsfunktion ausgelöst, die sich während der Eingabe weiter aktualisiert. Sie können sogar eine Variable aus den Optionen auswählen, die während der Eingabe erscheinen.

Wenn Sie einen angepassten Tag verwenden, können Sie den Tag kopieren und in die gewünschte Nachricht einfügen.

#### Ausnahmen für doppelte Klammern {#exceptions-for-double-brackets}

Wenn Sie einen Tag innerhalb eines anderen Liquid-Tags verwenden, wie z. B. `{% assign %}` oder `{% if %}`, können Sie entweder doppelte Klammern oder keine Klammern verwenden. Nur wenn der Tag allein steht, muss er in doppelte Klammern eingeschlossen werden. Der Einfachheit halber können Sie immer doppelte Klammern verwenden.

Die folgenden Tags sind alle korrekt:

```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}
```

{% endraw %}

{% alert note %}

Wenn Sie Liquid in Ihren E-Mail-Nachrichten verwenden, achten Sie darauf:

1. Es über den HTML-Editor einzufügen, nicht über den klassischen Editor. Der klassische Editor kann das Liquid als Klartext interpretieren. Zum Beispiel würde das Liquid als {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} dargestellt, anstatt den Vornamen der Nutzer:in einzusetzen.
2. Liquid-Code nur innerhalb des `<body>`-Tags zu platzieren. Eine Platzierung außerhalb dieses Tags kann bei der Zustellung zu inkonsistentem Rendering führen.

{% endalert %}

### Zwischen HTML- und klassischem Editor wechseln {#switching-between-html-and-classic-editors}

Wenn Sie zwischen dem HTML- und dem klassischen Editor wechseln, können sich Liquid-Snippets und Content Blocks in Ihrer Nachricht verschieben. Überprüfen Sie Ihr Template nach dem Wechsel des Editors. Wenn Sie eine besser vorhersagbare Layout-Kontrolle benötigen, verwenden Sie den Drag-and-Drop-Editor.

### Vorformatierte Variablen einfügen {#inserting-pre-formatted-variables}

Sie können vorformatierte Variablen mit Standardwerten über das Modal **Personalisierung hinzufügen** einfügen, das sich in der Nähe jedes Template-Textfelds befindet.

![Das Modal „Personalisierung hinzufügen“, das nach Auswahl von „Personalisierung einfügen“ erscheint. Das Modal enthält Felder für Personalisierungstyp, Attribut, optionalen Standardwert und zeigt eine Vorschau der Liquid-Syntax an.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

Das Modal fügt Liquid mit Ihrem angegebenen Standardwert an der Stelle ein, an der sich Ihr Cursor befand. Die Einfügeposition wird auch durch das Vorschaufeld angegeben, das den Text davor und danach anzeigt. Wenn ein Textblock markiert ist, wird der markierte Text ersetzt.

![Ein GIF des Modals „Personalisierung hinzufügen“, das zeigt, wie eine Nutzer:in „fellow traveler“ als Standardwert einfügt und das Modal den markierten Text „name“ im Composer durch das Liquid-Snippet ersetzt.]({% image_buster /assets/img_archive/insert_var_shot.gif %})