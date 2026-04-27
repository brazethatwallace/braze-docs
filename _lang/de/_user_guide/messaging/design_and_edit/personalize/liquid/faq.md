---
nav_title: FAQ
article_title: Häufig gestellte Fragen
page_order: 12
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Liquid."

---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zu Liquid.<br><br>Braze unterstützt derzeit nicht 100 % von Shopifys Liquid, sondern nur bestimmte Teile, die wir in unserer Dokumentation beschrieben haben. Wir empfehlen dringend, alle Nachrichten mit Liquid vor dem Versand zu testen, um das Risiko von Fehlern oder die Verwendung von nicht unterstütztem Liquid zu minimieren.

### Wie verwende ich Liquid-Snippets in Braze?

In vielen Fällen können Sie Liquid-Snippets einbinden, indem Sie zu Ihren Kampagnen oder Canvases navigieren und Liquid im Personalisierungs-Modal in Bereichen wie dem E-Mail-Nachrichtentext oder in Ihren Segmenten einfügen.

#### Wo kann ich mehr erfahren?

Weitere Informationen zu Liquid finden Sie in unserem geführten Braze-Lernpfad [Dynamische Personalisierung mit Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid)! Sie können auch die [Liquid-Anwendungsbeispiel-Bibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/) als Inspiration und für eine Reihe von Personalisierungsbeispielen mit Liquid nutzen.

### Was ist der Unterschied zwischen der Verwendung von Liquid und Connected-Content für die Personalisierung?

Braze Connected-Content ist ein Beispiel für einen Liquid-Tag. Es wird ebenfalls für die Personalisierung verwendet, aber die Daten stammen von einem externen Endpunkt und nicht aus gespeicherten Daten innerhalb von Braze. Besuchen Sie unseren speziellen Abschnitt [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), um mehr darüber zu erfahren, wie Sie die Personalisierung Ihrer Nachrichten erweitern können.

### Was ist Liquid-Templating?

Dies ist die häufigste Art, Liquid in Braze zu verwenden. Liquid-Templating zieht Daten aus dem Profil einer Nutzerin oder eines Nutzers in eine Nachricht. Diese Daten können vom Vornamen bis hin zu angepassten Events aus einer getriggerten Nachricht reichen.

Eine vollständige Liste der unterstützten Liquid-Tags finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/).

### Wie weise ich Variablen mit Liquid zu?

Sie können Variablen erstellen und zuweisen, indem Sie den `assign`-Tag verwenden. Dieser erstellt eine Variable im Nachrichten-Editor, die auch in Ihrer gesamten Nachricht referenziert werden kann.

### Verbraucht die Verwendung von Liquid Datenpunkte?

Nein.

### Wie kann ich Liquid verwenden, um eine personalisierte Begrüßung zu senden?

Für eine personalisierte Begrüßung mit dem Vornamen einer Nutzerin oder eines Nutzers können Sie die Standard-Nutzerprofilattribute wie {% raw %} `{{${first_name}}}`, `{{${last_name}}}` verwenden.

Sie können auch eine Liquid-`{% if X %}`{% endraw %}-Anweisung für bedingtes Rendering verwenden, basierend auf beliebigen Kriterien wie dem Wochentag oder angepassten Attributen. Weitere Informationen zu den unterstützten Liquid-Operatoren, die in bedingten Anweisungen verwendet werden können, finden Sie unter [Operatoren]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators/).

### Wie kann ich eine Nachricht basierend auf dem Standort einer Kundin oder eines Kunden personalisieren?

{% raw %}
Es gibt ein Standardattribut für den Standort der Nutzerin oder des Nutzers: `{{${most_recent_location}}}`.

### Was ist der Unterschied zwischen {{campaign.${name}}} und {{campaign.${message_name}}}?

Sowohl `{{campaign.${name}}}` als auch `{{campaign.${message_name}}}` sind unterstützte Liquid-Personalisierungs-Tags. Beide Tags referenzieren Kampagnenattribute. `{{campaign.${name}}}` bezeichnet den Namen Ihrer Kampagne, und `{{campaign.${message_name}}}` ist der Name Ihrer Nachrichtenvariante.
{% endraw %}

### Wie verwende ich Liquid mit verschachtelten Objekten?

Braze verfügt über ein integriertes Feature, das Liquid-Code für Segmente generiert, der in einer Nachricht verwendet werden kann. Konkret können Sie ein Segment erstellen, das mehrere Kriterien in einem Objekt abgleicht.

Weitere Informationen finden Sie unter [Multi-Kriterien-Segmentierung]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### Wie verwende ich Event-Eigenschaften, um eine Nachricht zu personalisieren, die ein Event triggert?

{% raw %}
Sie können auf Eigenschaften von API-getriggerten Events mit dem `api_triggered_property`-Tag zugreifen: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Was ist Abbruchlogik, und wie kann ich sie verwenden?

Abbruchlogik ermöglicht es Ihnen, den Versand einer Nachricht zu stoppen, wenn die Bedingungen erfüllt sind. Dies ist besonders hilfreich, um zu verhindern, dass unvollständige Nachrichten an Ihre Nutzer:innen gesendet werden. Beispiele für Abbruchlogik in Ihren Marketingkampagnen finden Sie unter [Nachrichten abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/).

### Was ist For-Loop-Logik, und wie kann ich sie verwenden?

For-Loops werden auch als [Iterations-Tags](https://shopify.github.io/liquid/tags/iteration/) bezeichnet. Die Verwendung von For-Loop-Logik in Ihren Liquid-Snippets ermöglicht es Ihnen, Liquid-Blöcke zu durchlaufen, bis eine Bedingung erfüllt ist.

In Braze kann dies verwendet werden, um Elemente in einem Array-Attribut oder eine Liste von Werten und Objekten zu prüfen, die von einem [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/), einer [Auswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) oder einem [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)-Aufruf zurückgegeben werden. Konkret können Sie For-Loop-Logik als Teil Ihres Messagings verwenden, um zu prüfen, ob ein Produkt auf Lager ist oder ob ein Produkt eine Mindestbewertung hat.

Nehmen wir zum Beispiel an, Sie haben einen Katalog namens „Games" mit einer Auswahl namens „cheap_games". Um die Titel der Spiele in „cheap_games" abzurufen, können Sie dieses Liquid-Snippet verwenden:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Sobald die festgelegten Bedingungen erfüllt sind, kann Ihre Nachricht fortfahren. Die Verwendung dieser Logik ist eine hilfreiche Möglichkeit, Zeit zu sparen, anstatt Liquid-Blöcke für verschiedene Bedingungen zu wiederholen.

### Warum gibt es zusätzliche Abstände in Nachrichten, die Content-Blöcke verwenden?

Wenn Sie zusätzliche Abstände in gesendeten Nachrichten bemerken, die Content-Blöcke mit Liquid verwenden, haben Sie möglicherweise unnötige Absatz- oder Zeilenumbrüche innerhalb Ihrer bedingten Anweisungen. Schreiben Sie Ihre bedingten Anweisungen in einer einzigen Zeile statt über mehrere Zeilen.

#### Beispiel

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
{% endraw %}

### When should I use `assign` versus `capture`?

Both `assign` and `capture` create Liquid variables, but they serve different purposes:

- `assign` is for simple variables that store a single value, such as a boolean, number, or simple string. You can also apply a single filter in the same line.
- `capture` is for storing a block of text that may include multiple variables, strings, or complex expressions. Use `capture` when the value is too complex for a single `assign` statement, such as URLs that utilize other Liquid variables or custom attributes as parameters. `capture` is also preferred when implementing Liquid variables in the body of Connected Content calls.

#### Examples

{% raw %}
```liquid
{% comment %} Valid assign usage {% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %} Use capture for complex strings {% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}
```
{% endraw %}