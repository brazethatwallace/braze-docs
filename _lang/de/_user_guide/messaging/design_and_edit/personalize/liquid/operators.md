---
nav_title: Operatoren
article_title: Liquid-Operatoren
page_order: 2
description: "Diese Referenzseite beschreibt die von Liquid unterstützten Operatoren sowie relevante Beispiele."

---

# Operatoren {#operators}

> Liquid unterstützt viele [Operatoren](https://docs.shopify.com/themes/liquid/basics/operators), die Sie in Ihren bedingten Anweisungen verwenden können. Diese Seite behandelt die von Liquid unterstützten Operatoren und zeigt Anwendungsfälle, wie Sie diese in Ihren Nachrichten einsetzen können.

Diese Tabelle listet die unterstützten Operatoren auf. Beachten Sie, dass Klammern in Liquid ungültige Zeichen sind und verhindern, dass Ihre Tags funktionieren.

| Syntax | Beschreibung des Operators |
|---------|-----------|
| ==  | ist gleich        |
| !=  | ist nicht gleich |
|  >  | größer als  |
| <   | kleiner als     |
| >= | größer als oder gleich |
| <= | kleiner als oder gleich |
| or | Bedingung A oder Bedingung B |
| and | Bedingung A und Bedingung B |
| contains | prüft, ob ein String oder String-Array einen String enthält |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Operatoren" }

{% alert note %}
Operatoren können in bedingten Anweisungen (`if`, `elsif`, `unless`) verwendet werden, jedoch nicht in `assign`-Anweisungen, `for`-Schleifen oder Array-Zugriffsklammern. In `case`- und `when`-Tags vergleicht jeder Branch den `case`-Ausdruck mit einem `when`-Wert mittels Gleichheit anstelle beliebiger Operator-Ausdrücke. Beispiele finden Sie unter [Bedingte Messaging-Logik]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#case-and-when-tags). Eine vollständige Aufschlüsselung finden Sie unter [Wo Operatoren und Filter verwendet werden können]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#where-to-use-operators-and-filters).
{% endalert %}

## Bedingungen ohne Klammern gruppieren {#grouping-conditions-without-parentheses}

Liquid unterstützt keine Klammern zum Gruppieren von Ausdrücken. Um komplexe boolesche Logik wie `(a and b) or c` auszuwerten, verwenden Sie verschachtelte `if`-Anweisungen oder Zwischenvariablen.

Um beispielsweise zu prüfen, ob ein Wert eine zusammengesetzte Bedingung erfüllt, weisen Sie eine Zwischenvariable zu:

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## Tutorials {#tutorials}

Lassen Sie uns einige Tutorials durchgehen, um zu lernen, wie Sie diese Operatoren für Ihre Marketing-Kampagnen einsetzen können:

### Eine Nachricht mit einem ganzzahligen angepassten Attribut auswählen {#choose-a-message-with-an-integer-custom-attribute}

Senden wir Push-Benachrichtigungen mit personalisierten Rabattaktionen an Nutzer:innen, die Käufe getätigt haben oder nicht. Die Push-Benachrichtigung verwendet ein ganzzahliges angepasstes Attribut namens `total_spend`, um die Gesamtausgaben der Nutzer:innen zu prüfen.

1. Schreiben Sie eine bedingte Anweisung mit dem Größer-als-Operator (`>`), um zu prüfen, ob die Gesamtausgaben der Nutzer:innen größer als `0` sind, was darauf hinweist, dass sie einen Kauf getätigt haben. Erstellen Sie dann eine Nachricht, die an diese Nutzer:innen gesendet wird.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2. Fügen Sie den {% raw %}`{% else %}`{% endraw %}-Tag hinzu, um Nutzer:innen zu erfassen, deren Gesamtausgaben gleich `0` sind oder nicht existieren. Erstellen Sie dann eine Nachricht, die an diese Nutzer:innen gesendet wird.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3. Schließen Sie die bedingte Logik mit dem {% raw %}`{% endif %}`{% endraw %}-Tag ab.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![Ein Push-Benachrichtigungs-Composer mit dem vollständigen Liquid-Code aus dem Tutorial.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

Wenn nun das angepasste Attribut „Total Spend“ der Nutzer:innen größer als `0` ist, erhalten sie folgende Nachricht:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Wenn das angepasste Attribut „Total Spend“ der Nutzer:innen nicht existiert oder gleich `0` ist, erhalten sie folgende Nachricht:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Eine Nachricht mit einem String-basierten angepassten Attribut auswählen {#choose-a-message-with-a-string-custom-attribute}

Senden wir Push-Benachrichtigungen an Nutzer:innen und personalisieren die Nachricht basierend auf dem zuletzt gespielten Spiel jeder Person. Dazu wird ein String-basiertes angepasstes Attribut namens `recent_game` verwendet, um zu prüfen, welches Spiel zuletzt gespielt wurde.

1. Schreiben Sie eine bedingte Anweisung mit dem Gleich-Operator (`==`), um zu prüfen, ob das zuletzt gespielte Spiel *Awkward Dinner Party* ist. Erstellen Sie dann eine Nachricht, die an diese Nutzer:innen gesendet wird.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2. Verwenden Sie den `elsif`-Tag mit dem Gleich-Operator (`==`), um zu prüfen, ob das zuletzt gespielte Spiel *Proxy War 3: War of Thirst* ist. Erstellen Sie dann eine Nachricht, die an diese Nutzer:innen gesendet wird.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3. Verwenden Sie den `elsif`-Tag mit den Operatoren „ist nicht gleich“ (`!=`) und „und“ (`and`), um zu prüfen, ob die Nutzer:innen ein kürzlich gespieltes Spiel haben (d. h. der Wert ist nicht leer) und dass das Spiel weder *Awkward Dinner Party* noch *Proxy War 3: War of Thirst* ist. Erstellen Sie dann eine Nachricht, die an diese Nutzer:innen gesendet wird.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4. Fügen Sie den {% raw %}`{% else %}`{% endraw %}-Tag hinzu, um Nutzer:innen zu erfassen, die kein kürzlich gespieltes Spiel haben. Erstellen Sie dann eine Nachricht, die an diese Nutzer:innen gesendet wird.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5. Schließen Sie die bedingte Logik mit dem {% raw %}`{% endif %}`{% endraw %}-Tag ab.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![Ein Push-Benachrichtigungs-Composer mit dem vollständigen Liquid-Code aus dem Tutorial.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Wenn Nutzer:innen zuletzt *Awkward Dinner Party* gespielt haben, erhalten sie folgende Nachricht:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

Wenn das zuletzt gespielte Spiel *Proxy War 3: War of Thirst* ist, erhalten sie folgende Nachricht:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

Wenn Nutzer:innen kürzlich ein Spiel gespielt haben, das weder *Awkward Dinner Party* noch *Proxy War 3: War of Thirst* war, erhalten sie folgende Nachricht:

```
Limited Time Deal! Get 15% off our best-selling classics!
```

Wenn Nutzer:innen keine Spiele gespielt haben oder dieses angepasste Attribut in ihrem Profil nicht existiert, erhalten sie folgende Nachricht:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Nachricht basierend auf dem Standort abbrechen {#abort-message-based-on-location}

Sie können eine Nachricht basierend auf nahezu allem abbrechen. Brechen wir eine Nachricht ab, wenn Nutzer:innen sich nicht in einem bestimmten Gebiet befinden, da sie möglicherweise nicht für die Aktion, Sendung oder Zustellung qualifiziert sind.

1. Schreiben Sie eine bedingte Anweisung mit dem Gleich-Operator (`==`), um zu prüfen, ob die Zeitzone der Nutzer:innen `America/Los_Angeles` ist, und erstellen Sie dann eine Nachricht, die an diese Nutzer:innen gesendet wird.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2. Um zu vermeiden, dass Nachrichten an Nutzer:innen außerhalb der Zeitzone `America/Los_Angeles` gesendet werden, umschließen Sie einen {% raw %}`{% abort_message () %}`{% endraw %}-Tag mit {% raw %}`{% else %}`{% endraw %}- und {% raw %}`{% endif %}`{% endraw %}-Tags.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

![Ein Push-Benachrichtigungs-Composer mit dem vollständigen Liquid-Code aus dem Tutorial.]({% image_buster /assets/img/abort-if.png %})

Sie können Nachrichten auch basierend auf Connected Content [abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content).

## Fehlerbehebung {#troubleshooting}

### Testversand kommt bei Verwendung von `abort_message` nicht an {#test-send-doesnt-arrive-when-using-abort_message}

Wenn Sie [`abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) verwenden und ein Testversand nie ankommt, fehlen der Vorschau-Nutzer:in möglicherweise Attribute, die Ihr Liquid erwartet. Die Abbruchlogik wird beim Rendern ausgeführt; wenn sie greift, sendet Braze die Nachricht nicht. Verwenden Sie für die Vorschau Nutzer:innen mit den erforderlichen Profildaten oder nutzen Sie **Als Nutzer:in anzeigen**, um Empfängerfelder zu testen, die dieselben Werte liefern wie Ihre Produktionszielgruppe.

### Die Vorschau kann Eigenschaftstypen falsch umwandeln {#preview-may-incorrectly-coerce-property-types}

Bei der Vorschau einer Nachricht im Dashboard werden die meisten Variablen (wie angepasste Attribute) in den korrekten Typ umgewandelt. Einige Variablen haben jedoch keinen definierten Typ, den die Vorschau nachschlagen kann:

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

Für diese Eigenschaften versucht die Vorschau, den Typ aus dem Wert abzuleiten. Das bedeutet, dass ein Wert, den Sie als **String** beabsichtigen, fälschlicherweise als **Zahl** interpretiert werden kann. Wenn beispielsweise ein Eigenschaftswert der String `"3"` ist, kann die Vorschau ihn in die Ganzzahl `3` umwandeln, was zu unerwartetem Verhalten bei String-Operationen wie `contains` oder `split` führen kann.

Wenn Sie bei der Verwendung dieser Eigenschaftstypen unerwartete Vorschauergebnisse sehen, beachten Sie, dass die Typableitung der Vorschau möglicherweise nicht mit dem übereinstimmt, was zum Sendezeitpunkt passiert. Zum Sendezeitpunkt werden die tatsächlichen Datentypen aus dem auslösenden Ereignis oder API-Aufruf beibehalten.

Um einen bestimmten Typ in der Vorschau zu erzwingen, können Sie den Wert explizit umwandeln:

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}