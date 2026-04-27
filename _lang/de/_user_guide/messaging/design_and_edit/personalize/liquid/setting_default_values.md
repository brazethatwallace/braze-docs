---
nav_title: Standardwerte festlegen
article_title: Standard-Liquid-Werte festlegen
page_order: 5
description: "Dieser Referenzartikel beschreibt, wie Sie Standard-Fallback-Werte für alle Personalisierungsattribute festlegen, die Sie in Ihren Nachrichten verwenden."

---

# Standardwerte festlegen

{% raw %}

> Für alle Personalisierungsattribute, die Sie in Ihren Nachrichten verwenden, können Standard-Fallback-Werte festgelegt werden. Dieser Artikel beschreibt, wie Standardwerte funktionieren, wie Sie sie einrichten und wie Sie sie in Ihren Nachrichten verwenden.

## Funktionsweise

Standardwerte können durch Angabe eines [Liquid-Filters](http://docs.shopify.com/themes/liquid-documentation/filters) (verwenden Sie `|`, um den Filter inline zu kennzeichnen, wie gezeigt) mit dem Namen „default" hinzugefügt werden.

```
| default: 'Insert Your Desired Default Here'
```

Wenn kein Standardwert angegeben wird und das Feld bei der Nutzer:in fehlt oder nicht gesetzt ist, bleibt das Feld in der Nachricht leer.

Das folgende Beispiel zeigt die korrekte Syntax zum Hinzufügen eines Standardwerts. In diesem Fall ersetzen die Wörter „Valued User" das Attribut `{{ ${first_name} }}`, wenn das Feld `first_name` einer Nutzer:in leer oder nicht verfügbar ist.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Für eine Nutzerin namens Janet Doe würde die Nachricht wie folgt erscheinen:

```
Hi Janet, thanks for using the App!
```

Oder...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
Der Standardwert wird für leere Werte (empty) angezeigt, aber nicht für Leerzeichenwerte (blank). Ein leerer Wert enthält nichts, während ein Leerzeichenwert Leerzeichen (wie Spaces) und keine anderen Zeichen enthält. Zum Beispiel könnte ein leerer String wie `""` aussehen und ein Leerzeichenstring wie `" "`.
{% endalert %}

## Standardwerte für verschiedene Datentypen festlegen

Das obige Beispiel zeigt, wie Sie einen Standardwert für einen String festlegen. Sie können Standardwerte für jeden Liquid-Datentyp festlegen, der den Wert `empty`, `nil` (undefiniert) oder `false` hat, einschließlich Strings, Boolescher Werte, Arrays, Objekte und Zahlen.

### Anwendungsfall: Boolesche Werte

Angenommen, Sie haben ein angepasstes Attribut vom Typ Boolescher Wert namens `premium_user` und möchten eine personalisierte Nachricht basierend auf dem Premium-Status der Nutzer:in senden. Einige Nutzer:innen haben keinen Premium-Status eingerichtet, daher müssen Sie einen Standardwert festlegen, um diese Nutzer:innen zu erfassen.

1. Sie weisen einer Variablen namens `is_premium_user` das Attribut `premium_user` mit einem Standardwert von `false` zu. Das bedeutet, wenn `premium_user` `nil` ist, wird der Wert von `is_premium_user` standardmäßig auf `false` gesetzt.

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2. Verwenden Sie dann bedingte Logik, um die Nachricht festzulegen, die gesendet werden soll, wenn `is_premium_user` `true` ist. Mit anderen Worten: was gesendet werden soll, wenn `premium_user` `true` ist. Sie weisen auch dem Vornamen der Nutzer:in einen Standardwert zu, falls der Name nicht vorhanden ist.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3. Legen Sie abschließend fest, welche Nachricht gesendet werden soll, wenn `is_premium_user` `false` ist (was bedeutet, dass `premium_user` `false` oder `nil` ist). Dann schließen Sie die bedingte Logik ab.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### Anwendungsfall: Zahlen

Angenommen, Sie haben ein numerisches angepasstes Attribut namens `reward_points` und möchten eine Nachricht mit den Prämienpunkten der Nutzer:in senden. Einige Nutzer:innen haben keine Prämienpunkte eingerichtet, daher müssen Sie einen Standardwert festlegen, um diese Nutzer:innen zu berücksichtigen.

1. Beginnen Sie die Nachricht mit der Anrede des Vornamens der Nutzer:in oder einem Standardwert von `Valued User`, falls der Name nicht vorhanden ist.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. Beenden Sie die Nachricht mit der Anzahl der Prämienpunkte der Nutzer:in, indem Sie das angepasste Attribut `reward_points` mit dem Standardwert `0` verwenden. Allen Nutzer:innen, deren `reward_points` einen `nil`-Wert haben, werden in der Nachricht `0` Prämienpunkte angezeigt.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### Anwendungsfall: Objekte

Angenommen, Sie haben ein verschachteltes angepasstes Attribut-Objekt namens `location`, das die Eigenschaften `city` und `state` enthält. Wenn eine dieser Eigenschaften nicht gesetzt ist, möchten Sie die Nutzer:in auffordern, diese anzugeben.

1. Sprechen Sie die Nutzer:in mit ihrem Vornamen an und fügen Sie einen Standardwert hinzu, falls der Name nicht vorhanden ist.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. Schreiben Sie eine Nachricht, die besagt, dass Sie den Standort der Nutzer:in bestätigen möchten.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3. Fügen Sie den Standort der Nutzer:in in die Nachricht ein und weisen Sie Standardwerte zu, wenn die Adresseigenschaft nicht gesetzt ist.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### Anwendungsfall: Arrays

Angenommen, Sie haben ein angepasstes Array-Attribut namens `upcoming_trips`, das Reisen mit den Eigenschaften `destination` und `departure_date` enthält. Sie möchten Nutzer:innen personalisierte Nachrichten senden, je nachdem, ob sie geplante Reisen haben.

1. Schreiben Sie bedingte Logik, die festlegt, dass keine Nachricht gesendet werden soll, wenn `upcoming_trips` `empty` ist.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2. Legen Sie fest, welche Nachricht gesendet werden soll, wenn `upcoming_trips` Inhalt hat:<br><br>**2a.** Sprechen Sie die Nutzer:in an und fügen Sie einen Standardwert hinzu, falls der Name nicht vorhanden ist. <br>**2b.** Verwenden Sie ein `for`-Tag, um festzulegen, dass Sie Eigenschaften (oder Informationen) für jede Reise abrufen, die in `upcoming_trips` enthalten ist. <br>**2c.** Listen Sie die Eigenschaften in der Nachricht auf und fügen Sie einen Standardwert hinzu, falls `departure_date` nicht gesetzt ist. (Nehmen wir an, dass ein `destination` erforderlich ist, damit eine Reise erstellt werden kann, sodass Sie dafür keinen Standardwert festlegen müssen.)<br>**2d.** Schließen Sie das `for`-Tag und dann die bedingte Logik.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values