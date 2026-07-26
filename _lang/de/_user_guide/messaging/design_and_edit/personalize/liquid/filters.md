---
nav_title: Filter
article_title: Liquid-Filter
page_order: 3
description: "Diese Referenzseite listet Filter auf, mit denen Sie statischen oder dynamischen Inhalt umformatieren können."

---

# Filter {#filters}

> Dieser Referenzartikel bietet eine Übersicht über Filter in Liquid und behandelt, welche Filter von Braze unterstützt werden. Sie suchen nach Ideen, wie Sie diese Filter einsetzen können? Schauen Sie sich unsere [Liquid-Anwendungsfallbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) an.

Filter ermöglichen es Ihnen, die Ausgabe von Zahlen, Strings, Variablen und Objekten in Liquid zu verändern. Sie können Filter verwenden, um statischen oder dynamischen Text umzuformatieren, z. B. um einen String von Kleinbuchstaben in Großbuchstaben umzuwandeln oder mathematische Operationen wie Addition oder Division durchzuführen.

{% alert important %}
Braze unterstützt nicht alle Liquid-Filter von Shopify. Diese Seite versucht, die Liquid-Filter aufzulisten, die Braze getestet hat, aber es handelt sich möglicherweise nicht um eine vollständige Liste. Testen Sie Ihr Liquid immer, bevor Sie Nachrichten versenden. <br><br>Wenn Sie Fragen zu einem Filter haben, der hier nicht aufgeführt ist, wenden Sie sich an Ihren geschäftskunden-Success-Manager.
{% endalert %}

## Filter-Syntax {#filter-syntax}

{% raw %}

Filter müssen innerhalb eines Ausgabe-Tags `{{ }}` platziert werden und werden durch ein Pipe-Zeichen `|` gekennzeichnet.

{% endraw %}

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{"Big Sale" | upcase}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
BIG SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

In diesem Beispiel ist `Big Sale` ein String und `upcase` der angewendete Filter.

{% alert note %}
Filter können in `assign`-Anweisungen und Ausgabe-Tags {% raw %}(`{{ }}`){% endraw %} verwendet werden, aber nicht in Bedingungen (`if`, `elsif`, `unless`), `case`/`when`, `for`-Schleifen oder Array-Zugriffsklammern. Um einen gefilterten Wert in einem dieser Kontexte zu verwenden, weisen Sie das Ergebnis zuerst einer Variablen zu. Weitere Details finden Sie unter [Wo Operatoren und Filter verwendet werden können]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#where-to-use-operators-and-filters).
{% endalert %}

### Syntax für mehrere Filter {#syntax-for-multiple-filters}

Sie können mehrere Filter auf eine Ausgabe anwenden. Sie werden von links nach rechts angewendet.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
 {{ "Big Sale" | upcase | remove: "BIG" }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
SALE
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Array-Filter {#array-filters}

Array-Filter werden verwendet, um die Ausgabe von Arrays zu verändern.

| Filter               | Definition                                                                                                         | Unterstützt |
| :------------------- | :----------------------------------------------------------------------------------------------------------------- | :-------- |
| [join](https://shopify.dev/docs/api/liquid/filters/join)          | Verbindet die Elemente eines Arrays mit dem als Parameter übergebenen Zeichen. Das Ergebnis ist ein einzelner String.          | ✅  Ja   |
| [first](https://shopify.dev/docs/api/liquid/filters/first)         | Gibt das erste Element eines Arrays zurück. In einem Array mit angepassten Attributen ist dies der älteste hinzugefügte Wert.                | ✅  Ja   |
| [last](https://shopify.dev/docs/api/liquid/filters/last)          | Gibt das letzte Element eines Arrays zurück. In einem Array mit angepassten Attributen ist dies der zuletzt hinzugefügte Wert.          | ✅  Ja   |
| [compact](https://shopify.dev/api/liquid/filters/compact)       | Entfernt alle `nil`-Elemente aus einem Array.                                                                             | ✅  Ja   |
| [concat](https://shopify.dev/api/liquid/filters/concat)        | Kombiniert ein Array mit einem anderen Array.                                                                              | ✅  Ja   |
| [find_index](https://shopify.dev/docs/api/liquid/filters/find_index)         | Gibt das Element an der angegebenen Indexposition in einem Array zurück. Das erste Element in einem Array wird mit `[0]` referenziert. | ⛔  Nein   |
| [map](https://shopify.dev/api/liquid/filters/map)           | Akzeptiert ein Attribut eines Array-Elements als Parameter und erstellt ein Array aus den Werten jedes Array-Elements.        | ✅  Ja   |
| [reverse](https://shopify.dev/api/liquid/filters/reverse)       | Kehrt die Reihenfolge der Elemente in einem Array um.                                                                       | ✅  Ja   |
| [size](https://shopify.dev/api/liquid/filters/size)          | Gibt die Größe eines Strings (Anzahl der Zeichen) oder eines Arrays (Anzahl der Elemente) zurück.                      | ✅  Ja   |
| [slice](https://shopify.dev/api/liquid/filters/slice)        | Gibt einen Teilstring eines Strings oder eine Teilmenge eines Arrays zurück, beginnend am angegebenen Index.                          | ✅  Ja   |
| [sort](https://shopify.dev/api/liquid/filters/sort)         | Sortiert die Elemente eines Arrays nach einem bestimmten Attribut eines Elements im Array.                                    | ✅  Ja   |
| [sort_natural](https://shopify.dev/api/liquid/sort_natural) | Sortiert die Elemente in einem Array in alphabetischer Reihenfolge ohne Berücksichtigung der Groß-/Kleinschreibung.                                                | ✅  Ja   |
| [uniq](https://shopify.dev/api/liquid/filters/uniq)         | Entfernt alle doppelten Instanzen von Elementen in einem Array.                                                           | ✅  Ja   |
| [where](https://shopify.dev/api/liquid/where)        | Filtert ein Array, sodass nur Elemente mit einem bestimmten Eigenschaftswert enthalten sind.                                             | ✅  Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Array-Filter" }

## Farbfilter {#color-filters}

[Farbfilter](https://shopify.dev/api/liquid/filters/color-filters) werden in Braze nicht unterstützt.

## Schriftfilter {#font-filters}

[Schriftfilter](https://shopify.dev/api/liquid/filters/font-filters) werden in Braze nicht unterstützt.

## Mathematische Filter {#math-filters}

Mathematische Filter ermöglichen es Ihnen, mathematische Operationen durchzuführen. Wenn Sie mehrere Filter auf eine Ausgabe anwenden, werden sie von links nach rechts angewendet.

| Filter  | Definition      | Unterstützt |
| :------ |:----------------| :-------- |
| [abs](https://shopify.dev/api/liquid/filters/abs)        | Gibt den Absolutwert einer Zahl zurück.     | ✅  Ja   |
| [at_most](https://shopify.dev/api/liquid/filters/at_most)    | Begrenzt eine Zahl auf einen Maximalwert.   | ✅  Ja   |
| [at_least](https://shopify.dev/api/liquid/filters/at_least)   | Begrenzt eine Zahl auf einen Minimalwert.   | ✅  Ja   |
| [ceil](https://shopify.dev/api/liquid/filters/ceil)       | Rundet eine Ausgabe auf die nächste ganze Zahl auf.  | ✅  Ja   |
| [divided_by](https://shopify.dev/api/liquid/filters/divided_by) | Teilt eine Ausgabe durch eine Zahl. Die Ausgabe wird auf die nächste ganze Zahl abgerundet. Beachten Sie den folgenden Tipp, um Rundungen zu vermeiden. | ✅  Ja   |
| [floor](https://shopify.dev/api/liquid/filters/floor)      | Rundet eine Ausgabe auf die nächste ganze Zahl ab.        | ✅  Ja   |
| [minus](https://shopify.dev/api/liquid/filters/minus)      | Subtrahiert eine Zahl von einer Ausgabe.          | ✅  Ja   |
| [plus](https://shopify.dev/api/liquid/filters/plus)       | Addiert eine Zahl zu einer Ausgabe.     | ✅  Ja   |
| [round](https://shopify.dev/api/liquid/filters/round)      | Rundet die Ausgabe auf die nächste ganze Zahl oder die angegebene Anzahl von Dezimalstellen.  | ✅  Ja   |
| [times](https://shopify.dev/api/liquid/filters/times)     | Multipliziert eine Ausgabe mit einer Zahl.       | ✅  Ja   |
| [modulo](https://shopify.dev/api/liquid/filters/modulo)    | Teilt eine Ausgabe durch eine Zahl und gibt den Rest zurück.   | ✅  Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mathematische Filter" }

{% alert tip %}
Wenn Sie in Liquid ganze Zahlen (Ganzzahlen) durch ganze Zahlen teilen und das Ergebnis eine Gleitkommazahl (Zahl mit Dezimalstelle) ist, rundet Liquid automatisch auf die nächste ganze Zahl ab. Wenn Sie jedoch ganze Zahlen durch Gleitkommazahlen teilen, erhalten Sie immer eine Gleitkommazahl. Das bedeutet, Sie können Ihre ganzen Zahlen in Gleitkommazahlen umwandeln (1.0, 2.0, 3.0), um eine Gleitkommazahl als Ergebnis zu erhalten.
{% raw %}
<br><br>Zum Beispiel gibt `{{15 | divided_by: 2}}` den Wert `7` aus, während `{{15 | divided_by: 2.0}}` den Wert `7.5` ausgibt.
{% endraw %}
{% endalert %}

### Mathematische Operationen mit angepassten Attributen {#mathematical-operations-with-custom-attributes}

Beachten Sie, dass Sie keine mathematischen Operationen zwischen zwei angepassten Attributen durchführen können.

{% raw %}

```liquid
{{custom_attribute.${current_rewards_balance} | plus: {{custom_attribute.${giftcard_balance}}}}}
```

Dieses Beispiel würde nicht funktionieren, da Sie nicht mehrere angepasste Attribute in einer einzigen Liquid-Zeile referenzieren können. Stattdessen müssten Sie mindestens einem dieser Werte eine Variable zuweisen, bevor die mathematischen Funktionen ausgeführt werden. Das Addieren zweier angepasster Attribute erfordert zwei Zeilen Liquid:

1. Eine, um das angepasste Attribut einer Variablen zuzuweisen,
2. Eine, um die Addition durchzuführen.

#### Anwendungsfall: Aktuellen Kontostand berechnen {#use-case-calculate-current-balance}

Nehmen wir an, wir möchten den aktuellen Kontostand einer Nutzerin oder eines Nutzers berechnen, indem wir das Guthabenkarten-Guthaben und das Rewards-Guthaben addieren.

1. Verwenden Sie den `assign`-Tag, um das angepasste Attribut `current_rewards_balance` durch den Begriff „balance“ zu ersetzen. Das bedeutet, dass Sie jetzt eine Variable namens `balance` haben, die Sie bearbeiten können.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

{: start="2"}
2. Verwenden Sie den `plus`-Filter, um das Guthabenkarten-Guthaben jeder Nutzerin und jedes Nutzers mit dem Rewards-Guthaben zu kombinieren, dargestellt durch das `{{balance}}`-Objekt.
{% endraw %}
{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
You have $35 to spend!
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Geldfilter {#money-filters}

Wenn Sie Nutzer:innen über ihren Kauf, einen Kontostand oder irgendetwas im Zusammenhang mit Geld informieren, sollten Sie Geldfilter verwenden. Geldfilter stellen sicher, dass Ihre Dezimalstellen an der richtigen Stelle stehen und kein Teil Ihres Updates verloren geht (wie die lästige `0` am Ende).

| Filter         | Definition          | Unterstützt |
| :--------------- | :--------------- | :-------- |
| [money](https://shopify.dev/api/liquid/filters/money)      | Formatiert Zahlen, um sicherzustellen, dass Dezimalstellen an der richtigen Stelle stehen und Nullen nicht am Ende von Zahlen abgeschnitten werden.   | ✅  Ja   |
| [money_with_currency](https://shopify.dev/api/liquid/filters/money_with_currency)    | Formatiert Zahlen mit dem Währungssymbol.     | ⛔  Nein    |
| [money_without_currency](https://shopify.dev/api/liquid/filters/money_without_currency)     | Formatiert Zahlen ohne das Währungssymbol.      | ⛔  Nein    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Geldfilter" }

{% alert important %}
Um eine Zahl mit dem `money`-Filter korrekt zu formatieren, entfernen Sie alle Kommas in der Zahl und fügen Sie den `plus: 0`-Filter vor dem `money`-Filter hinzu. Sehen Sie sich zum Beispiel das folgende Liquid an:<br><br>
{% raw %}
```liquid
{% assign my_int = "350000.25" | plus: 0 %}
{{ my_int | money }}
```
{% endraw %}
{% endalert %}

### Shopify-Geldfilter versus Braze-Geldfilter {#shopify-money-filter-versus-braze-money-filter}

{% alert warning %}
Das Verhalten des Shopify-`money`-Filters unterscheidet sich von der Verwendung in Braze. Beachten Sie die folgenden Beispiele für eine genaue Darstellung des erwarteten Verhaltens.
{% endalert %}

{% raw %}
Wenn Sie ein angepasstes Attribut eingeben (wie `account_balance`), sollten Sie immer den `money`-Filter verwenden, um Ihre Dezimalstellen an die richtige Stelle zu setzen und zu verhindern, dass Nullen am Ende von Zahlen abgeschnitten werden:

```liquid
${{custom_attribute.${account_balance} | money}}
```
{% endraw %}

| MIT DEM GELDFILTER                       | OHNE DEN GELDFILTER                    |
| :------------------------------------------ | :------------------------------------------ |
| ![Mit Geldfilter]({% image_buster /assets/img/with_money_filter.png %})                     | ![Ohne Geldfilter]({% image_buster /assets/img/without_money_filter.png %})                  |
| Wobei `account_balance` mit `17.8` eingegeben wird. | Wobei `account_balance` mit `17.8` eingegeben wird. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Shopify-Geldfilter versus Braze-Geldfilter" }

Der `money`-Filter in Braze unterscheidet sich von Shopify, da er nicht automatisch Dezimalpunkte gemäß einer voreingestellten Einstellung anwendet. Nehmen wir zum Beispiel das folgende Szenario, in dem `rewards_redeemed` den Wert `145` enthält:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$145.00
```
{% endraw %}
{% endtab %}
{% endtabs %}

Gemäß dem Shopify-[money](https://shopify.dev/api/liquid/filters/money)-Filter sollte die Ausgabe `$1.45` sein, in Braze wird die Ausgabe jedoch `$145.00` sein. Als Workaround können wir den `divided_by`-Filter verwenden, um die Zahl in eine Dezimalzahl umzuwandeln, bevor der Geldfilter angewendet wird:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
${{event_properties.${rewards_redeemed} | divided_by: 100.00 | money }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
$1.45
```
{% endraw %}
{% endtab %}
{% endtabs %}

## String-Filter {#string-filters}

String-Filter werden verwendet, um die Ausgaben und Variablen von Strings zu bearbeiten. Strings sind eine Kombination aus alphanumerischen Zeichen und müssen in gerade Anführungszeichen eingeschlossen werden.

{% alert note %}
Gerade Anführungszeichen unterscheiden sich von typografischen Anführungszeichen in Liquid. Seien Sie vorsichtig, wenn Sie Liquid aus einem Texteditor in Braze kopieren und einfügen, da typografische Anführungszeichen Fehler in Ihrem Liquid verursachen. Wenn Sie Ihr Liquid direkt in Braze schreiben, werden gerade Anführungszeichen automatisch angewendet.
{% endalert %}

| Filter          | Beschreibung     | Unterstützt |
| :--------------- | ------------- | --------- |
| [append](https://shopify.dev/api/liquid/filters/append)     | Hängt Zeichen an einen String an.           | ✅  Ja   |
| [camelize](https://shopify.dev/docs/api/liquid/filters/camelize)     | Wandelt einen String in CamelCase um.             | ⛔  Nein    |
| [capitalize](https://shopify.dev/api/liquid/filters/capitalize)     | Schreibt das erste Wort in einem String groß und wandelt die restlichen Zeichen in Kleinbuchstaben um.         | ✅  Ja   |
| [downcase](https://shopify.dev/api/liquid/filters/downcase)      | Wandelt einen String in Kleinbuchstaben um.         | ✅  Ja   |
| [escape](https://shopify.dev/api/liquid/filters/escape)    | Escaped einen String.             | ✅  Ja   |
| [handleize](https://shopify.dev/api/liquid/filters/handleize)        | Formatiert einen String in ein Handle.        | ⛔  Nein    |
| [md5](https://shopify.dev/api/liquid/filters/md5)    | Wandelt einen String in einen MD5-Hash um. Weitere Informationen finden Sie unter [Encoding-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#encoding-filters).   | ✅  Ja   |
| [sha1](https://shopify.dev/api/liquid/filters/sha1)    | Wandelt einen String in einen SHA-1-Hash um. Weitere Informationen finden Sie unter [Encoding-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#encoding-filters).  | ✅  Ja   |
| hmac_sha1_hex<br>(zuvor [hmac_sha_1](https://shopify.dev/api/liquid/filters/string-filters#hmac_sha1)) | Wandelt einen String in einen SHA-1-Hash unter Verwendung eines Hash-basierten Nachrichtenauthentifizierungscodes (HMAC) um. Übergeben Sie den geheimen Schlüssel für die Nachricht als Parameter an den Filter. Weitere Informationen finden Sie unter [Encoding-Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#encoding-filters). | ✅  Ja   |
| [hmac_sha256](https://shopify.dev/api/liquid/filters/hmac_sha256)    | Wandelt einen String in einen SHA-256-Hash unter Verwendung eines Hash-basierten Nachrichtenauthentifizierungscodes (HMAC) um. Übergeben Sie den geheimen Schlüssel für die Nachricht als Parameter an den Filter.       | ✅  Ja   |
| hmac_sha512 | Wandelt einen String in einen SHA-512-Hash unter Verwendung eines Hash-basierten Nachrichtenauthentifizierungscodes (HMAC) um. Übergeben Sie den geheimen Schlüssel für die Nachricht als Parameter an den Filter. | ✅  Ja  |
| [newline_to_br](https://shopify.dev/api/liquid/filters/newline_to_br)     | Fügt ein `<br>`-Zeilenumbruch-HTML-Tag vor jedem Zeilenumbruch in einem String ein.        | ✅  Ja   |
| [pluralize](https://shopify.dev/api/liquid/filters/pluralize)   | Gibt die Singular- oder Pluralversion eines englischen Strings basierend auf dem Wert einer Zahl aus.      | ⛔  Nein    |
| [prepend](https://shopify.dev/api/liquid/filters/prepend)     | Stellt Zeichen einem String voran.      | ✅  Ja   |
| [remove](https://shopify.dev/api/liquid/filters/remove)      | Entfernt alle Vorkommen eines Teilstrings aus einem String.       | ✅  Ja   |
| [remove_first](https://shopify.dev/api/liquid/filters/remove_first)    | Entfernt nur das erste Vorkommen eines Teilstrings aus einem String.      | ✅  Ja   |
| [replace](https://shopify.dev/api/liquid/filters/replace)        | Ersetzt alle Vorkommen eines Strings durch einen Teilstring.   | ✅  Ja   |
| [replace_first](https://shopify.dev/api/liquid/filters/replace_first)        | Ersetzt das erste Vorkommen eines Strings durch einen Teilstring.      | ✅  Ja   |
| [slice](https://shopify.dev/api/liquid/filters/slice)       | Der slice-Filter gibt einen Teilstring zurück, beginnend am angegebenen Index.       | ✅  Ja   |
| [split](https://shopify.dev/api/liquid/filters/split)  | Der split-Filter nimmt einen Teilstring als Parameter entgegen. Der Teilstring wird als Trennzeichen verwendet, um einen String in ein Array aufzuteilen.            | ✅  Ja   |
| [strip](https://shopify.dev/api/liquid/filters/strip)   | Entfernt Tabs, Leerzeichen und Zeilenumbrüche (alle Whitespace-Zeichen) von der linken und rechten Seite eines Strings.                                                                                                    | ✅  Ja   |
| [lstrip](https://shopify.dev/api/liquid/filters/lstrip)     | Entfernt Tabs, Leerzeichen und Zeilenumbrüche (alle Whitespace-Zeichen) von der linken Seite eines Strings.    | ⛔  Nein    |
| [rstrip](https://shopify.dev/api/liquid/filters/rstrip)             | Entfernt Tabs, Leerzeichen und Zeilenumbrüche (alle Whitespace-Zeichen) von der rechten Seite eines Strings.          | ⛔  Nein    |
| [strip_html](https://shopify.dev/api/liquid/filters/strip_html)         | Entfernt alle HTML-Tags aus einem String.        | ✅  Ja   |
| [strip_newlines](https://shopify.dev/api/liquid/filters/strip_newlines)  | Entfernt alle Zeilenumbrüche aus einem String.        | ✅  Ja   |
| [truncate](https://shopify.dev/api/liquid/filters/truncate)    | Kürzt einen String auf die als ersten Parameter übergebene Zeichenanzahl. Auslassungspunkte (...) werden an den gekürzten String angehängt und sind in der Zeichenanzahl enthalten.    | ✅  Ja   |
| [truncatewords](https://shopify.dev/api/liquid/filters/truncatewords)   | Kürzt einen String auf die als ersten Parameter übergebene Wortanzahl. Auslassungspunkte (...) werden an den gekürzten String angehängt.    | ✅  Ja   |
| [upcase](https://shopify.dev/api/liquid/filters/upcase)   | Wandelt einen String in Großbuchstaben um.      | ✅  Ja   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="String-Filter" }

## Zusätzliche Filter {#additional-filters}

Die folgenden allgemeinen Filter dienen vielen Zwecken, einschließlich der Formatierung oder Konvertierung von Inhalten.

| Filter                | Beschreibung                                                                                                                      | Unterstützt |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- | :-------- |
| [date](https://shopify.dev/api/liquid/filters/date)           | Wandelt einen Zeitstempel in ein anderes Datumsformat um. Weitere Informationen finden Sie unter [Datumsfilter](#date-filter).         | ✅  Ja   |
| [default](https://shopify.dev/api/liquid/filters/default)        | Legt einen Standardwert für jede Variable ohne zugewiesenen Wert fest. Kann mit Strings, Arrays und Hashes verwendet werden.      | ✅  Ja   |
| [format_address](https://shopify.dev/api/liquid/filters/format_address) | Formatiert eine Adresse, um die Adresselemente in der Reihenfolge gemäß ihrem Gebietsschema auszugeben.        | ⛔  Nein    |
| [highlight](https://shopify.dev/api/liquid/filters/highlight)      | Umschließt Wörter in Suchergebnissen mit einem HTML-`<strong>`-Tag mit der Klasse „highlight“, wenn sie mit den eingegebenen Suchbegriffen übereinstimmen. | ⛔  Nein    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Zusätzliche Filter" }

Weitere unterstützte Filter, wie Encoding- und URL-Filter, finden Sie auf unserer Seite [Erweiterte Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters).

### Datumsfilter {#date-filter}

Der `date`-Filter kann verwendet werden, um einen Zeitstempel in ein anderes Datumsformat umzuwandeln. Sie können Parameter an den `date`-Filter übergeben, um den Zeitstempel umzuformatieren. Beispiele für diese Parameter finden Sie unter [strfti.me](http://www.strfti.me/).

Nehmen wir zum Beispiel an, dass der Wert von `date_attribute` der Zeitstempel `2021-06-03 17:13:41 UTC` ist.

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%b %d'}}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
03 June
```
{% endraw %}
{% endtab %}
{% endtabs %}

Zusätzlich zu den `strftime`-Formatierungsoptionen unterstützt Braze auch die Konvertierung eines Zeitstempels in Unix-Zeit mit dem `%s`-Datumsfilter. Um zum Beispiel `date_attribute` in Unix-Zeit zu erhalten:

{% tabs local %}
{% tab Input %}
{% raw %}
```liquid
{{custom_attribute.${date_attribute} | date: '%s' }}
```
{% endraw %}
{% endtab %}
{% tab Output %}
{% raw %}
```liquid
1433351621
```
{% endraw %}
{% endtab %}
{% endtabs %}