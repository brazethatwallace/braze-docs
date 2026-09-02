---
nav_title: Bedingte Messaging-Logik
article_title: Bedingte Liquid-Messaging-Logik
page_order: 6
description: "Dieser Referenzartikel behandelt, wie Tags in Ihren Campaigns verwendet werden können und sollten."

---

# Bedingte Messaging-Logik {#conditional-messaging-logic}

> [Tags](https://docs.shopify.com/themes/liquid-documentation/tags) ermöglichen es Ihnen, Programmierlogik in Ihre Messaging-Kampagnen einzubinden. Tags können sowohl für die Ausführung bedingter Anweisungen als auch für fortgeschrittene Anwendungsfälle wie das Zuweisen von Variablen oder das Iterieren durch einen Codeblock verwendet werden. <br><br>Diese Seite behandelt, wie Tags verwendet werden können und sollten, z. B. wie Sie mit null-, nil- und leeren Attributwerten umgehen und wie Sie angepasste Attribute referenzieren.

## Tags formatieren {#formatting-tags}

{% raw %}
Ein Tag muss in `{% %}` eingeschlossen sein.
{% endraw %}

Um Ihnen das Leben etwas leichter zu machen, bietet Braze eine Farbformatierung, die in Grün und Lila aktiviert wird, wenn Sie Ihre Liquid-Syntax korrekt formatiert haben. Die grüne Formatierung hilft beim Erkennen von Tags, während die lila Formatierung Bereiche hervorhebt, die Personalisierung enthalten.

Wenn Sie Schwierigkeiten mit bedingter Nachrichtenlogik haben, versuchen Sie, die bedingte Syntax aufzuschreiben, bevor Sie Ihre angepassten Attribute und andere Liquid-Elemente einfügen.

Fügen Sie zum Beispiel zunächst Folgendes in das Nachrichtenfeld ein:
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

Stellen Sie sicher, dass es grün hervorgehoben wird, und ersetzen Sie dann `X` durch Ihr gewähltes Liquid oder Connected-Content über das blaue `+` in der Ecke des Nachrichtenfelds und die `0` durch Ihren gewünschten Wert.
<br><br>
Fügen Sie dann Ihre Nachrichtenvarianten nach Bedarf zwischen den `else`-Bedingungen hinzu:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## Bedingte Logik {#conditional-logic}

Sie können viele Arten von [intelligenter Logik in Nachrichten](http://docs.shopify.com/themes/liquid-documentation/basics) einbinden, wie z. B. bedingte Anweisungen. Das folgende Beispiel verwendet [Bedingungen](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags), um eine Campaign zu internationalisieren:
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### Bedingte Tags {#conditional-tags}

#### `if` und `elsif` {#if-and-elsif}

Bedingte Logik beginnt mit dem `if`-Tag, der die erste zu prüfende Bedingung festlegt. Nachfolgende Bedingungen verwenden den `elsif`-Tag und werden geprüft, wenn die vorherigen Bedingungen nicht erfüllt sind. In diesem Beispiel prüft der Code, wenn das Gerät einer Nutzerin oder eines Nutzers nicht auf Englisch eingestellt ist, ob das Gerät auf Spanisch eingestellt ist, und falls das fehlschlägt, ob das Gerät auf Chinesisch eingestellt ist. Wenn das Gerät der Nutzerin oder des Nutzers eine dieser Bedingungen erfüllt, erhält sie oder er eine Nachricht in der entsprechenden Sprache.

#### `else`

Sie haben die Möglichkeit, eine `{% else %}`-Anweisung in Ihre bedingte Logik einzufügen. Wenn keine der von Ihnen festgelegten Bedingungen erfüllt ist, gibt die `{% else %}`-Anweisung die Nachricht an, die gesendet werden soll. In diesem Beispiel verwenden wir standardmäßig Englisch, wenn die Sprache einer Nutzerin oder eines Nutzers nicht Englisch, Spanisch oder Chinesisch ist.

#### `case` und `when` {#case-and-when}

`{% case %}`, `{% when %}` und `{% endcase %}` funktionieren wie eine Switch-Anweisung: Sie setzen einen Ausdruck nach `case`, und jeder `when`-Zweig wird ausgeführt, wenn dieser Ausdruck dem aufgelisteten Wert entspricht (Liquid verwendet im Hintergrund Gleichheit, ähnlich wie die Verkettung von `if` und `elsif` mit `==`). Sie können mehrere Werte in einem `when`-Tag auflisten, indem Sie sie mit einem Komma oder `or` trennen. Verwenden Sie `{% else %}` als Fallback, wenn nichts übereinstimmt, und schließen Sie dann mit `{% endcase %}`.

Stellen Sie sicher, dass das Format Ihrer `when`-Werte zum Datentyp passt. Für Text (z. B. einen Sprachcode) verwenden Sie Anführungszeichen: `{% when 'es' %}`. Für Zahlen lassen Sie die Anführungszeichen weg: `{% when 2 %}`.

```liquid
{% assign handle = 'cake' %}
{% case handle %}
{% when 'cake' %}
This is a cake
{% when 'cookie' %}
This is a cookie
{% else %}
This is not a cake nor a cookie
{% endcase %}
```

Sie können dasselbe Muster mit Braze-Personalisierungs-Tags oder anderen Liquid-Ausdrücken anstelle von `handle` verwenden. Weitere Syntaxoptionen finden Sie in der Shopify-Dokumentation zum [`case`-Tag](https://shopify.dev/docs/api/liquid/tags/case).

#### `endif`

Der `{% endif %}`-Tag signalisiert, dass Sie einen `if`-Block abgeschlossen haben. Sie müssen den `{% endif %}`-Tag in jede Nachricht einfügen, die `if`, `elsif`, `unless` oder `else` in dieser Kette verwendet. Wenn Sie keinen `{% endif %}`-Tag einfügen, erhalten Sie einen Fehler, da Braze Ihre Nachricht nicht parsen kann. Wenn Sie stattdessen `{% case %}` verwenden, schließen Sie den Block mit `{% endcase %}`, nicht mit `{% endif %}`.

{% alert note %}
In `if`-, `elsif`- und `unless`-Tags können Sie Operatoren verwenden, aber keine Filter. In `case`- und `when`-Tags stimmt jeder Zweig überein, wenn der `case`-Ausdruck einem `when`-Wert entspricht; Filter werden in diesen Ausdrücken ebenfalls nicht unterstützt. Um einen gefilterten Wert auszuwerten, weisen Sie das Filterergebnis zuerst einer Variablen zu und referenzieren Sie dann diese Variable in Ihrer `case`- oder `when`-Klausel. Weitere Details finden Sie unter [Wo Operatoren und Filter verwendet werden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#where-to-use-operators-and-filters).
{% endalert %}

### Tutorial: Standortbasierte Inhalte bereitstellen {#tutorial-deliver-location-based-content}

Wenn Sie dieses Tutorial abgeschlossen haben, können Sie Tags mit „if“-, „elsif“- und „else“-Anweisungen verwenden, um Inhalte basierend auf dem Standort einer Nutzerin oder eines Nutzers bereitzustellen.

1. Beginnen Sie mit einem `if`-Tag, um festzulegen, welche Nachricht gesendet werden soll, wenn sich der Ort der Nutzerin oder des Nutzers in New York befindet. Wenn der Ort New York ist, wird diese erste Bedingung erfüllt und die Nutzerin oder der Nutzer erhält eine Nachricht, die ihre oder seine New Yorker Identität bestätigt.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at your local Sandwich Emperor.
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2. Verwenden Sie als Nächstes den `elseif`-Tag, um festzulegen, welche Nachricht gesendet werden soll, wenn sich der Ort der Nutzerin oder des Nutzers in Los Angeles befindet.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3. Verwenden wir einen weiteren `elseif`-Tag, um festzulegen, welche Nachricht gesendet werden soll, wenn sich der Ort der Nutzerin oder des Nutzers in Chicago befindet.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
```

{: start="4"}
4. Verwenden wir nun den `{% else %}`-Tag, um festzulegen, welche Nachricht gesendet werden soll, wenn sich der Ort der Nutzerin oder des Nutzers nicht in San Francisco, New York oder Chicago befindet.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5. Abschließend verwenden wir den `{% endif %}`-Tag, um anzugeben, dass unsere bedingte Logik abgeschlossen ist.

```liquid
{% endif %}
```

{% endraw %}

{% details Vollständiger Liquid-Code %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at our New York location.
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

## Umgang mit null-, nil- und leeren Attributwerten {#accounting-for-null-nil-and-blank-attribute-values}

Bedingte Logik ist eine nützliche Methode, um mit Attributwerten umzugehen, die in Nutzerprofilen nicht gesetzt sind.

### Null- und nil-Attributwerte {#null-and-nil-attribute-values}

Ein null- oder nil-Wert tritt auf, wenn der Wert eines angepassten Attributs nicht gesetzt wurde. Zum Beispiel hat eine Nutzerin oder ein Nutzer, die oder der noch keinen Vornamen festgelegt hat, keinen Vornamen in Braze hinterlegt.

In manchen Fällen möchten Sie möglicherweise eine völlig andere Nachricht an Nutzer:innen senden, die einen Vornamen gesetzt haben, und an solche, die keinen Vornamen gesetzt haben.

Der folgende Tag ermöglicht es Ihnen, eine Nachricht für Nutzer:innen mit einem null-Attribut „Vorname“ festzulegen:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %}

![Eine Beispielnachricht im Braze-Dashboard, die ein null-Attribut „Vorname“ verwendet.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

Beachten Sie, dass ein null-Attributwert nicht streng mit einem Werttyp verknüpft ist (zum Beispiel ist ein „null“-String dasselbe wie ein „null“-Array). Im obigen Beispiel referenziert der null-Attributwert einen nicht gesetzten Vornamen, der ein String wäre.

{% endraw %}

### Leere Attributwerte {#blank-attribute-values}

Ein leerer Wert tritt auf, wenn das Attribut in einem Kundenprofil or Nutzerprofil nicht gesetzt ist, mit einem Leerzeichen-String (` `) gesetzt ist oder als `false` gesetzt ist. Leere Werte sollten vor anderen Variablen geprüft werden, um einen Liquid-Verarbeitungsfehler zu vermeiden.

Der folgende Tag ermöglicht es Ihnen, eine Nachricht für Nutzer:innen festzulegen, die ein leeres Attribut „Vorname“ haben.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %}

## Angepasste Attribute referenzieren {#referencing-custom-attributes}

Nachdem Sie [angepasste Attribute erstellt]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes) haben, können Sie diese angepassten Attribute in Ihrem Liquid-Messaging referenzieren.

Bei der Verwendung bedingter Logik müssen Sie den Datentyp des angepassten Attributs kennen, um sicherzustellen, dass Sie die richtige Syntax verwenden. Suchen Sie auf der Seite **Angepasste Attribute** im Dashboard nach dem Datentyp, der Ihrem angepassten Attribut zugeordnet ist, und orientieren Sie sich dann an den folgenden Beispielen für jeden Datentyp.

![Auswahl eines Datentyps für ein angepasstes Attribut. Das gezeigte Beispiel zeigt ein Attribut „Favorite_Category“ mit dem Datentyp String.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
Strings und Arrays erfordern einfache Anführungszeichen, während boolesche Werte und Ganzzahlen niemals Anführungszeichen haben.
{% endalert %}

### Boolescher Wert {#boolean}

[Boolesche Werte]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#booleans) sind binäre Werte und können entweder auf `true` oder `false` gesetzt werden, wie z. B. `registration_complete: true`. Boolesche Werte haben keine Anführungszeichen.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

### Zahl {#number}

[Zahlen]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) sind numerische Werte, die Ganzzahlen oder Gleitkommazahlen sein können. Zum Beispiel könnte eine Nutzerin oder ein Nutzer `shoe_size: 10` oder `levels_completed: 287` haben. Zahlenwerte haben keine Anführungszeichen.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

Sie können auch andere [grundlegende Operatoren](https://shopify.dev/docs/themes/liquid/reference/basics/operators) wie kleiner als (<) oder größer als (>) für Ganzzahlen verwenden:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

### String {#string}

Ein [String]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) besteht aus alphanumerischen Zeichen und speichert Daten über Ihre Nutzerin oder Ihren Nutzer. Zum Beispiel könnten Sie `favorite_color: red` oder `phone_number: 3025981329` haben. String-Werte müssen Anführungszeichen haben.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

Für Strings können Sie sowohl „==“ als auch „contains“ in Ihrem Liquid verwenden.

### Array {#array}

Ein [Array]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types) ist eine Liste von Informationen über Ihre Nutzerin oder Ihren Nutzer. Zum Beispiel könnte eine Nutzerin oder ein Nutzer `last_viewed_shows: stranger things, planet earth, westworld` haben. Array-Werte müssen Anführungszeichen haben.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

Für Arrays müssen Sie `contains` verwenden und können nicht `==` verwenden.

#### Wie `contains` bei Strings und Arrays funktioniert {#how-contains-works-with-strings-versus-arrays}

Der `contains`-Operator verhält sich unterschiedlich, je nachdem, ob er einen String oder ein Array auswertet:

- **Strings:** `contains` prüft auf einen Teilstring an beliebiger Stelle im Text.
- **Arrays:** `contains` prüft auf eine exakte Übereinstimmung mit einem vollständigen Element im Array.

{% alert important %}
Wenn ein Attribut als Array gespeichert ist (zum Beispiel `["med1", "med2", "abc"]`), ergibt die Suche nach `contains "ab"` den Wert `false`, da kein einzelnes Element in dieser Liste exakt `"ab"` ist.
{% endalert %}

##### Teilstring-Suche in Arrays {#substring-matching-on-arrays}

Wenn Sie nach einer teilweisen Übereinstimmung (Teilstring) innerhalb eines Array-Attributs suchen müssen, müssen Sie das Array zunächst mit dem `join`-Filter in einen einzelnen String umwandeln.

Da Braze keine Inline-Filter direkt in bedingten {% raw %}`{% if %}`{% endraw %}-Blöcken unterstützt, müssen Sie einen zweistufigen Prozess befolgen: Weisen Sie zuerst den zusammengefügten Wert einer Variablen zu und führen Sie dann Ihre bedingte Prüfung durch.

{% raw %}
```liquid
{% comment %} 1. Convert the array to a string using a comma separator {% endcomment %}
{% assign products_string = {{custom_attribute.${product_array}}} | join: "," %}

{% comment %} 2. Perform the substring check on the new variable {% endcomment %}
{% if products_string contains "ab" %}
  Match found!
{% else %}
  No match.
{% endif %}
```
{% endraw %}


{% alert tip %}
Da `join` Array-Elemente zu einem String zusammenfügt (Standard-Trennzeichen: ein einzelnes Leerzeichen), können Teilstring-Prüfungen über Elementgrenzen hinweg übereinstimmen (zum Beispiel wird `["Napa", "boulevard"]` zu `Napa boulevard`, wobei `contains "a b"` den Wert `true` ergibt). Verwenden Sie ein explizites Trennzeichen wie „,“, um Grenzen deutlicher zu machen und versehentliche elementübergreifende Übereinstimmungen zu reduzieren.
{% endalert %}

### Zeit {#time}

Ein Zeitstempel, der angibt, wann ein Ereignis stattgefunden hat. [Zeit]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)-Werte müssen einen [mathematischen Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#math-filters) haben, um in bedingter Logik verwendet werden zu können.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %}
```

{% endraw %}