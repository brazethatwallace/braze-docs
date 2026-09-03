---
nav_title: Liquid-Anwendungsfallbibliothek
article_title: Liquid-Anwendungsfallbibliothek
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "Diese Landing-Page enthält Beispiele für Liquid-Anwendungsfälle, geordnet nach Kategorien wie Jubiläen, App-Nutzung, Countdowns und mehr."

---

{% api %}

## Jubiläen und Feiertage {#anniversaries-and-holidays}

{% apitags %}
Anniversaries and holidays
{% endapitags %}

- [Nachrichten basierend auf dem Jubiläumsjahr personalisieren](#anniversary-year)
- [Nachrichten basierend auf der Geburtstagswoche personalisieren](#birthday-week)
- [Campaigns an Nutzer:innen in ihrem Geburtstagsmonat senden](#birthday-month)
- [Nachrichtenversand an wichtigen Feiertagen vermeiden](#holiday-avoid)

### Nachrichten basierend auf dem Jubiläumsjahr personalisieren {#anniversary-year}

Dieser Anwendungsfall zeigt, wie das App-Jubiläum basierend auf dem ursprünglichen Registrierungsdatum berechnet und je nach Anzahl der gefeierten Jahre unterschiedliche Nachrichten angezeigt werden.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %}
{% if this_day == anniversary_day %}
{% if anniversary_year == '2021' %}
Exactly one year ago today we met for the first time!

{% elsif anniversary_year == '2020' %}
Exactly two years ago today we met for the first time!

{% elsif anniversary_year == '2019' %}
Exactly three years ago today we met for the first time!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %}
{% abort_message("Not same day") %}
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
```
{% endraw %}

**Erklärung:** Hier verwenden wir die reservierte Variable `now`, um das aktuelle Datum und die Uhrzeit im [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)-Format einzufügen. Die Filter `%B` (Monat wie „May“) und `%d` (Tag wie „18“) formatieren den aktuellen Monat und Tag. Anschließend verwenden wir dieselben Datums- und Zeitfilter auf die `signup_date`-Werte, um sicherzustellen, dass wir die beiden Werte mithilfe von bedingten Tags und Logik vergleichen können.

Dann wiederholen wir drei weitere Variablenzuweisungen, um `%B` und `%d` für das `signup_date` zu erhalten, wobei wir zusätzlich `%Y` (Jahr wie „2021“) hinzufügen. Dadurch wird das Datum und die Uhrzeit des `signup_date` auf nur das Jahr reduziert. Wenn wir Tag und Monat kennen, können wir prüfen, ob das Jubiläum heute ist, und wenn wir das Jahr kennen, wissen wir, wie viele Jahre vergangen sind – und können entsprechend gratulieren!

{% alert tip %} Sie können so viele Bedingungen erstellen, wie Sie Jahre an Registrierungsdaten gesammelt haben. {% endalert %}

### Nachrichten basierend auf der Geburtstagswoche personalisieren {#birthday-week}

Dieser Anwendungsfall zeigt, wie der Geburtstag ermittelt, mit dem aktuellen Datum verglichen und spezielle Geburtstagsnachrichten vor, während und nach der Geburtstagswoche angezeigt werden.

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = {{${date_of_birth}}} | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```
{% endraw %}

**Erklärung:** Ähnlich wie beim Anwendungsfall [Jubiläumsjahr](#anniversary-year) nehmen wir hier die reservierte Variable `now` und verwenden den Filter `%W` (Woche, z. B. Woche 12 von 52 in einem Jahr), um die Kalenderwoche des Geburtstags zu ermitteln. Wenn die Geburtstagswoche mit der aktuellen Woche übereinstimmt, senden wir eine Glückwunschnachricht!

Wir fügen außerdem Anweisungen für `last_week` und `next_week` hinzu, um Ihre Nachrichten weiter zu personalisieren.

### Campaigns an Nutzer:innen in ihrem Geburtstagsmonat senden {#birthday-month}

Dieser Anwendungsfall zeigt, wie der Geburtstagsmonat berechnet wird, ob der Geburtstag in den aktuellen Monat fällt, und falls ja, eine spezielle Nachricht gesendet wird.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
Message body
{% else %}
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

**Erklärung:** Ähnlich wie beim Anwendungsfall [Geburtstagswoche](#birthday-week), nur dass wir hier den Filter `%B` (Monat wie „May“) verwenden, um zu berechnen, welche Nutzer:innen in diesem Monat Geburtstag haben. Eine mögliche Anwendung wäre, Geburtstagskinder in einer monatlichen E-Mail anzusprechen.

### Nachrichtenversand an wichtigen Feiertagen vermeiden {#holiday-avoid}

Dieser Anwendungsfall zeigt, wie Nachrichten während der Feiertagszeit gesendet werden, wobei die Tage wichtiger Feiertage ausgenommen werden, an denen das Engagement wahrscheinlich gering ist.

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2023-12-24" or today == "2023-12-25" or today == "2023-12-26" %}
{% abort_message %}
{% else %}
Message if today isn't one of the provided holidays.
{% endif %}
```
{% endraw %}

**Erklärung:** Hier weisen wir den Begriff `today` der reservierten Variable `now` (aktuelles Datum und Uhrzeit) zu und verwenden die Filter `%Y` (Jahr wie „2023“), `%m` (Monat wie „12“) und `%d` (Tag wie „25“), um das Datum zu formatieren. Anschließend führen wir unsere bedingte Anweisung aus: Wenn die Variable `today` mit den gewählten Feiertagen übereinstimmt, wird die Nachricht abgebrochen.

Das bereitgestellte Beispiel verwendet Heiligabend, den ersten und den zweiten Weihnachtsfeiertag.

{% endapi %}

{% api %}

## App-Nutzung {#app-usage}

{% apitags %}
App usage
{% endapitags %}

- [Nachrichten in der Sprache senden, wenn keine Sitzung protokolliert wurde](#app-session-language)
- [Nachrichten basierend auf der letzten App-Öffnung personalisieren](#app-last-opened)
- [Andere Nachricht anzeigen, wenn die App vor weniger als drei Tagen genutzt wurde](#app-last-opened-less-than)

### Nachrichten in der Sprache senden, wenn keine Sitzung protokolliert wurde {#app-session-language}

Dieser Anwendungsfall prüft, ob eine Sitzung protokolliert wurde. Falls nicht, wird eine Logik eingebunden, die eine Nachricht basierend auf der manuell über ein angepasstes Attribut erfassten Sprache anzeigt, sofern vorhanden. Wenn keine Sprachinformation mit dem Konto verknüpft ist, wird die Nachricht in der Standardsprache angezeigt. Wenn eine Sitzung protokolliert wurde, werden die mit dem Profil verknüpften Sprachinformationen abgerufen und die entsprechende Nachricht angezeigt.

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on custom attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on custom attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**Erklärung:** Hier verwenden wir zwei gruppierte, verschachtelte `if`-Anweisungen. Die erste `if`-Anweisung prüft, ob der/die Nutzer:in eine Sitzung gestartet hat, indem geprüft wird, ob `last_used_app_date` den Wert `nil` hat. Das liegt daran, dass `{{${language}}}` automatisch vom SDK erfasst wird, wenn eine Sitzung protokolliert wird. Wenn keine Sitzung protokolliert wurde, haben wir die Sprache noch nicht, daher wird geprüft, ob sprachbezogene angepasste Attribute gespeichert wurden, und basierend auf diesen Informationen wird die Nachricht nach Möglichkeit in dieser Sprache angezeigt.
{% endraw %}

Die zweite `if`-Anweisung prüft einfach das Standard-Attribut, da `last_used_app_date` nicht `nil` ist, was bedeutet, dass eine Sitzung protokolliert wurde und wir die Sprache haben.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) ist eine reservierte Variable, die zurückgegeben wird, wenn Liquid-Code keine Ergebnisse liefert. `Nil` wird in einem `if`-Block als `false` behandelt.
{% endalert %}

### Nachrichten basierend auf der letzten App-Öffnung personalisieren {#app-last-opened}

Dieser Anwendungsfall berechnet, wann die App zuletzt geöffnet wurde, und zeigt je nach Zeitraum eine andere personalisierte Nachricht an.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### Andere Nachricht anzeigen, wenn die App vor weniger als drei Tagen genutzt wurde {#app-last-opened-less-than}

Dieser Anwendungsfall berechnet, wie lange die letzte App-Nutzung zurückliegt, und zeigt je nach Zeitraum eine andere personalisierte Nachricht an.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Countdowns

{% apitags %}
Countdowns
{% endapitags %}

- [X Tage zum heutigen Datum addieren](#countdown-add-x-days)
- [Countdown ab einem festgelegten Zeitpunkt berechnen](#countdown-difference-days)
- [Countdown für bestimmte Versandtermine und Prioritäten erstellen](#countdown-shipping-options)
- [Countdown in Tagen erstellen](#countdown-days)
- [Countdown von Tagen über Stunden bis Minuten erstellen](#countdown-dynamic)
- [Verbleibende Tage bis zu einem bestimmten Datum anzeigen](#countdown-future-date)
- [Verbleibende Tage bis zum Eintreffen eines angepassten Datumsattributs anzeigen](#countdown-custom-date-attribute)
- [Verbleibende Zeit anzeigen und Nachricht abbrechen, wenn nur noch X Zeit übrig ist](#countdown-abort-window)
- [In-App-Nachricht X Tage vor Ablauf der Mitgliedschaft senden](#countdown-membership-expiry)
- [In-App-Nachrichten basierend auf Datum und Sprache personalisieren](#countdown-personalize-language)
- [Datum 30 Tage ab heute als Monat und Tag formatiert einfügen](#countdown-template-date)

### X Tage zum heutigen Datum addieren {#countdown-add-x-days}

Dieser Anwendungsfall addiert eine bestimmte Anzahl von Tagen zum aktuellen Datum, um darauf in Nachrichten zu verweisen. Beispielsweise könnten Sie eine Nachricht unter der Woche senden, die Veranstaltungen in der Umgebung für das Wochenende zeigt.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

Der `plus`-Wert ist immer in Sekunden angegeben, daher verwenden wir am Ende den Filter `%F`, um die Sekunden in Tage umzurechnen.

{% alert important %}
Möglicherweise möchten Sie eine URL oder einen Deeplink zu einer Veranstaltungsliste in Ihre Nachricht einfügen, damit Sie Nutzer:innen zu einer Liste zukünftiger Aktivitäten weiterleiten können.
{% endalert %}

### Countdown ab einem festgelegten Zeitpunkt berechnen {#countdown-difference-days}

Dieser Anwendungsfall berechnet die Differenz in Tagen zwischen einem bestimmten Datum und dem aktuellen Datum. Diese Differenz kann verwendet werden, um Ihren Nutzer:innen einen Countdown anzuzeigen.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### Countdown für bestimmte Versandtermine und Prioritäten erstellen {#countdown-shipping-options}

Dieser Anwendungsfall erfasst verschiedene Versandoptionen, berechnet die jeweilige Lieferzeit und zeigt Nachrichten an, die Nutzer:innen ermutigen, rechtzeitig zu bestellen, damit ihr Paket bis zu einem bestimmten Datum ankommt.

{% raw %}
```liquid
{% assign standard_shipping_start = "2023-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2023-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2023-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2023-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference_o | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping, so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping, so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
```
{% endraw %}

### Countdown in Tagen erstellen {#countdown-days}

Dieser Anwendungsfall berechnet die verbleibende Zeit zwischen einem bestimmten Ereignis und dem aktuellen Datum und zeigt an, wie viele Tage bis zum Ereignis verbleiben.

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```
{% endraw %}

{% alert important %}
Sie benötigen ein angepasstes Attribut-Feld mit einem `date`-Wert.
{% endalert %}

### Countdown von Tagen über Stunden bis Minuten erstellen {#countdown-dynamic}

Dieser Anwendungsfall berechnet die verbleibende Zeit zwischen einem bestimmten Ereignis und dem aktuellen Datum. Je nach verbleibender Zeit wird der Zeitwert (Tage, Stunden, Minuten) geändert, um verschiedene personalisierte Nachrichten anzuzeigen.

Wenn beispielsweise noch zwei Tage bis zur Lieferung einer Bestellung verbleiben, könnte die Nachricht lauten: „Ihre Bestellung kommt in 2 Tagen an.“ Wenn es weniger als ein Tag ist, könnte sie zu „Ihre Bestellung kommt in 17 Stunden an“ geändert werden.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```
{% endraw %}

{% alert important %}
Sie benötigen ein angepasstes Attribut-Feld mit einem `date`-Wert. Außerdem müssen Sie Zeitschwellenwerte festlegen, ab wann die Zeit in Tagen, Stunden und Minuten angezeigt werden soll.
{% endalert %}

### Verbleibende Tage bis zu einem bestimmten Datum anzeigen {#countdown-future-date}

Dieser Anwendungsfall berechnet die Differenz zwischen dem aktuellen Datum und einem zukünftigen Ereignisdatum und zeigt eine Nachricht an, wie viele Tage bis zum Ereignis verbleiben.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### Verbleibende Tage bis zum Eintreffen eines angepassten Datumsattributs anzeigen {#countdown-custom-date-attribute}

Dieser Anwendungsfall berechnet die Differenz in Tagen zwischen dem aktuellen und einem zukünftigen Datum und zeigt eine Nachricht an, wenn die Differenz einer festgelegten Anzahl entspricht.

In diesem Beispiel erhält ein/e Nutzer:in zwei Tage vor dem angepassten Datumsattribut eine Nachricht. Andernfalls wird die Nachricht nicht gesendet.

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Verbleibende Zeit anzeigen und Nachricht abbrechen, wenn nur noch X Zeit übrig ist {#countdown-abort-window}

Dieser Anwendungsfall berechnet, wie lange es bis zu einem bestimmten Datum dauert, und bricht den Nachrichtenversand ab, wenn das Datum zu nah ist. Je nach verbleibender Zeit werden verschiedene personalisierte Nachrichten angezeigt.

Beispiel: „Sie haben noch x Stunden, um Ihr Ticket nach London zu kaufen“, aber die Nachricht wird nicht gesendet, wenn es weniger als zwei Stunden bis zur Abflugzeit nach London sind.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```
{% endraw %}

{% alert important %} Sie benötigen eine angepasste Event-Eigenschaft. {% endalert %}

### In-App-Nachricht X Tage vor Ablauf der Mitgliedschaft senden {#countdown-membership-expiry}

Dieser Anwendungsfall erfasst das Ablaufdatum der Mitgliedschaft, berechnet die verbleibende Zeit und zeigt je nach verbleibender Dauer unterschiedliche Nachrichten an.

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial. Make sure you upgrade!

{% else %}
You have few days left in your trial. Make sure to upgrade!
{% endif %}
```
{% endraw %}

### In-App-Nachrichten basierend auf Datum und Sprache personalisieren {#countdown-personalize-language}

Dieser Anwendungsfall berechnet einen Countdown bis zu einem Ereignis und zeigt basierend auf der Spracheinstellung den Countdown in der jeweiligen Sprache an.

Beispielsweise könnten Sie einmal im Monat eine Reihe von Upsell-Nachrichten senden, die anzeigen, wie lange ein Angebot noch gültig ist, mit vier In-App-Nachrichten:

- Anfangsnachricht
- Noch 2 Tage
- Noch 1 Tag
- Letzter Tag

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
```
{% endraw %}

{% alert important %}
Sie müssen einen `date`-Wert zuweisen und eine Abbruchlogik einbauen, falls das angegebene Datum außerhalb des Datumsbereichs liegt. Für exakte Tagesberechnungen muss das zugewiesene Enddatum 23:59:59 enthalten.
{% endalert %}

### Datum 30 Tage ab heute als Monat und Tag formatiert einfügen {#countdown-template-date}

Dieser Anwendungsfall zeigt das Datum 30 Tage ab heute an, um es in Nachrichten zu verwenden.

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## Angepasstes Attribut {#custom-attribute}

{% apitags %}
Custom attribute
{% endapitags %}

- [Nachricht basierend auf übereinstimmenden angepassten Attributen personalisieren](#attribute-matching)
- [Währung für europäische Zahlenkonventionen formatieren](#european-currency-format)
- [Zwei angepasste Attribute subtrahieren und die Differenz als Geldwert anzeigen](#attribute-monetary-difference)
- [Vornamen referenzieren, wenn der vollständige Name im first_name-Feld gespeichert ist](#attribute-first-name)

### Nachricht basierend auf übereinstimmenden angepassten Attributen personalisieren {#attribute-matching}

Dieser Anwendungsfall prüft, ob bestimmte angepasste Attribute vorhanden sind, und zeigt entsprechend verschiedene personalisierte Nachrichten an.

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead-end of a dirt road. The road goes to the east. In the distance, you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```
{% endraw %}

### Währung für europäische Zahlenkonventionen formatieren {#european-currency-format}

Für Regionen, die ein Komma als Dezimaltrennzeichen und einen Punkt als Tausendertrennzeichen verwenden (z. B. Deutschland oder Italien), verwenden Sie die Filter [`money`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#money-filters) und [`number_with_delimiter`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters#number-formatting-filters) mit `replace`, um die Trennzeichen zu tauschen. Verwenden Sie `#` als temporären Platzhalter, damit Punkte und Kommas nicht im selben Durchgang vertauscht werden.

{% raw %}
```liquid
{{ 1234567.89 | money | number_with_delimiter | replace: '.', '#' | replace: ',', '.' | replace: '#', ',' }}
```

**Ausgabe:** `1.234.567,89`

**Erklärung:** Der `money`-Filter fügt Dezimalstellen hinzu, aber kein Währungssymbol oder regionsspezifische Trennzeichen. `number_with_delimiter` fügt US-amerikanische Tausendertrennzeichen hinzu, und die `replace`-Filter wandeln sie in das europäische Format um.
{% endraw %}

### Zwei angepasste Attribute subtrahieren und die Differenz als Geldwert anzeigen {#attribute-monetary-difference}

Dieser Anwendungsfall erfasst zwei monetäre angepasste Attribute, berechnet die Differenz und zeigt sie an, damit Nutzer:innen wissen, wie weit sie noch von ihrem Ziel entfernt sind.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### Vornamen referenzieren, wenn der vollständige Name im first_name-Feld gespeichert ist {#attribute-first-name}

Dieser Anwendungsfall erfasst den Vornamen (wenn Vor- und Nachname in einem einzigen Feld gespeichert sind) und verwendet diesen Vornamen, um eine Begrüßungsnachricht anzuzeigen.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Erklärung:** Der `split`-Filter teilt den in `{{${first_name}}}` gespeicherten String in ein Array auf. Durch die Verwendung von `{{name[0]}}` verweisen wir dann nur auf das erste Element im Array, also den Vornamen.

{% endraw %}
{% endapi %}

{% api %}

## Angepasstes Event {#custom-event}

{% apitags %}
Custom event
{% endapitags %}

- [Push-Benachrichtigung abbrechen, wenn ein angepasstes Event innerhalb von zwei Stunden stattfindet](#event-abort-push)
- [Campaign senden, wenn ein angepasstes Event dreimal ausgeführt wurde](#event-three-times)
- [Nachricht an Nutzer:innen senden, die nur aus einer Kategorie gekauft haben](#event-purchased-one-category)
- [Verfolgen, wie oft ein angepasstes Event im letzten Monat aufgetreten ist](#track)


### Push-Benachrichtigung abbrechen, wenn ein angepasstes Event innerhalb von zwei Stunden stattfindet {#event-abort-push}

Dieser Anwendungsfall berechnet die Zeit bis zu einem Ereignis und zeigt je nach verbleibender Zeit verschiedene personalisierte Nachrichten an.

Beispielsweise möchten Sie möglicherweise verhindern, dass eine Push-Benachrichtigung gesendet wird, wenn eine angepasste Event-Eigenschaft in den nächsten zwei Stunden eintritt. Dieses Beispiel verwendet das Szenario eines Warenkorb-Abbruchs für ein Zugticket.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```
{% endraw %}

### Campaign senden, wenn ein angepasstes Event dreimal ausgeführt wurde {#event-three-times}

Dieser Anwendungsfall prüft, ob ein angepasstes Event dreimal ausgeführt wurde, und zeigt in diesem Fall eine Nachricht an oder sendet eine Campaign.

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message("Error calculating cadence") %}
{% elsif cadence != 0 %}
{% abort_message("Skip message") %}
{% endif %}
Did you forget something in your shopping cart?
```
{% endraw %}

{% alert important %} Sie benötigen eine Event-Eigenschaft für die Anzahl des angepassten Events oder einen Webhook an Ihren Braze-Endpunkt. Damit wird ein angepasstes Attribut (`example_event_count`) bei jeder Ausführung des Events inkrementiert. Dieses Beispiel verwendet eine Kadenz von drei (1, 4, 7, 10 usw.). Um die Kadenz bei null zu starten (0, 3, 6, 9 usw.), entfernen Sie `minus: 1`.
{% endalert %}

### Nachricht an Nutzer:innen senden, die nur aus einer Kategorie gekauft haben {#event-purchased-one-category}

Dieser Anwendungsfall erfasst eine Liste der Kategorien, aus denen gekauft wurde, und zeigt eine Nachricht an, wenn nur eine Kaufkategorie vorhanden ist.

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1 %}
{{uniq_cat}}
{% else %}
{% abort_message("Purchase category doesn't exist") %}
{% endif %}
```
{% endraw %}

### Verfolgen, wie oft ein angepasstes Event im letzten Monat aufgetreten ist {#track}

Dieser Anwendungsfall berechnet, wie oft ein angepasstes Event zwischen dem 1. des aktuellen Monats und dem Vormonat protokolliert wurde. Anschließend können Sie einen users/track-Aufruf ausführen, um diesen Wert als angepasstes Attribut zu speichern. Beachten Sie, dass diese Campaign zwei aufeinanderfolgende Monate laufen muss, bevor monatliche Daten verwendet werden können.

{% raw %}
```liquid

{% capture body %}
{
 "braze_id": "{{${braze_id}}}",
 "fields_to_export": ["custom_events"]
}

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
 :method post
  :headers { "Authorization": "Bearer YOUR_API_KEY" }
  :body {{body}}
 :content_type application/json
 :save response
  :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} The following custom event name will need to be amended for the target custom event. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}The Custom Event name that is being tracked will be needed to be amended for the target Custom Event in the Attribute Name below. {% endcomment %}
```

```json
"attributes": [
  {
    "external_id":"{{${user_id}}}",
       "projects_exported_{{formatted_month}}_{{previous_year}}": "{{latest_count}}"
  }
]
```

{% endraw %}

{% endapi %}

{% api %}

## Sprache {#language}

{% apitags %}
Language
{% endapitags %}

- [Monatsnamen in einer anderen Sprache anzeigen](#language-display-month)
- [Bild basierend auf der Sprache anzeigen](#language-image-display)
- [Nachrichten basierend auf Wochentag und Sprache personalisieren](#language-personalize-message)

### Monatsnamen in einer anderen Sprache anzeigen {#language-display-month}

Dieser Anwendungsfall zeigt das aktuelle Datum, den Monat und das Jahr an, wobei der Monat in einer anderen Sprache dargestellt wird. Das bereitgestellte Beispiel verwendet Schwedisch.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month}} == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month}} == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month}} == 'April' %}
{{day}} April {{year}}
{% elsif {{month}} == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month}} == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month}} == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month}} == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month}} == 'September' %}
{{day}} September {{year}}
{% elsif {{month}} == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month}} == 'November' %}
{{day}} November {{year}}
{% elsif {{month}} == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### Bild basierend auf der Sprache anzeigen {#language-image-display}

Dieser Anwendungsfall zeigt ein Bild basierend auf der Sprache an. Beachten Sie, dass dieser Anwendungsfall nur mit Bildern getestet wurde, die in die Braze-Medienbibliothek hochgeladen wurden.

{% raw %}
```liquid
{% if ${language} == 'en' %}
English image URL (for example, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
Russian image URL
{% elsif ${language} == 'es' %}
Spanish image URL
{% else %}
Fallback image URL
{% endif %}
```
{% endraw %}

### Nachrichten basierend auf Wochentag und Sprache personalisieren {#language-personalize-message}

Dieser Anwendungsfall prüft den aktuellen Wochentag und zeigt basierend auf dem Tag und der eingestellten Sprache eine spezifische Nachricht in der jeweiligen Sprache an.

Das bereitgestellte Beispiel endet am Dienstag, kann aber für jeden Wochentag wiederholt werden.

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Purchase today and take your language learning to the next level. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
It's Monday, but the language doesn't match
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
Don't forget to unlock the full version of your language. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
tuesday default
{% endif %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Verschiedenes {#miscellaneous}

{% apitags %}
Miscellaneous
{% endapitags %}

- [E-Mail-Versand an Kund:innen vermeiden, die Marketing-E-Mails blockiert haben](#misc-avoid-blocked-emails)
- [Abo-Status zur Personalisierung von Nachrichteninhalten verwenden](#misc-personalize-content)
- [Ersten Buchstaben jedes Wortes in einem String großschreiben](#misc-capitalize-words-string)
- [Wert eines angepassten Attributs mit einem Array vergleichen](#misc-compare-array)
- [Erinnerung für ein bevorstehendes Ereignis erstellen](#misc-event-reminder)
- [String in einem Array finden](#misc-string-in-array)
- [Größten Wert in einem Array finden](#misc-largest-value)
- [Kleinsten Wert in einem Array finden](#misc-smallest-value)
- [Ende eines Strings abfragen](#misc-query-end-of-string)
- [Werte in einem Array aus einem angepassten Attribut mit mehreren Kombinationen abfragen](#misc-query-array-values)
- [String als Telefonnummer formatieren](#phone-number)

### E-Mail-Versand an Kund:innen vermeiden, die Marketing-E-Mails blockiert haben {#misc-avoid-blocked-emails}

Dieser Anwendungsfall nimmt eine Liste blockierter Nutzer:innen, die in einem Content-Block gespeichert ist, und stellt sicher, dass diese blockierten Nutzer:innen in kommenden Campaigns oder Canvases nicht kontaktiert oder angesprochen werden.

{% alert important %}
Um dieses Liquid zu verwenden, speichern Sie zunächst die Liste der blockierten E-Mail-Adressen in einem Content-Block. Die Liste sollte keine zusätzlichen Leerzeichen oder Zeichen zwischen den E-Mail-Adressen enthalten (z. B. `test@braze.com,abc@braze.com`).
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message("Email is blocked") %}
    {% break %}
    {% endif %}
{% endfor %}
Your message here!
```
{% endraw %}

**Erklärung:** Hier prüfen wir, ob die E-Mail-Adresse des potenziellen Empfängers/der potenziellen Empfängerin in dieser Liste enthalten ist, indem wir den Content-Block mit den blockierten E-Mails referenzieren. Wenn die E-Mail gefunden wird, wird die Nachricht nicht gesendet.

{% alert note %}
Content Blocks haben eine Größenbeschränkung von 5 MB.
{% endalert %}

### Abo-Status zur Personalisierung von Nachrichteninhalten verwenden {#misc-personalize-content}

Dieser Anwendungsfall verwendet den Abo-Status, um personalisierte Inhalte zu senden. Kund:innen, die eine bestimmte Abo-Gruppe abonniert haben, erhalten eine exklusive Nachricht für E-Mail-Abo-Gruppen.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### Ersten Buchstaben jedes Wortes in einem String großschreiben {#misc-capitalize-words-string}

Dieser Anwendungsfall nimmt einen String aus Wörtern, teilt ihn in ein Array auf und schreibt den ersten Buchstaben jedes Wortes groß.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %}
```
{% endraw %}

**Erklärung:** Hier haben wir eine Variable unserem gewählten String-Attribut zugewiesen und den `split`-Filter verwendet, um den String in ein Array aufzuteilen. Anschließend haben wir den `for`-Tag verwendet, um die Variable `words` jedem Element in unserem neu erstellten Array zuzuweisen, bevor wir diese Wörter mit dem `capitalize`-Filter und dem `append`-Filter anzeigen, um Leerzeichen zwischen den einzelnen Begriffen hinzuzufügen.

### Wert eines angepassten Attributs mit einem Array vergleichen {#misc-compare-array}

Dieser Anwendungsfall nimmt eine Liste von Lieblingsgeschäften, prüft, ob eines der Lieblingsgeschäfte in dieser Liste enthalten ist, und zeigt in diesem Fall ein Sonderangebot aus diesen Geschäften an.

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} Diese Sequenz enthält einen `break`-Tag in der primären bedingten Anweisung. Dadurch wird die Schleife gestoppt, wenn eine Übereinstimmung gefunden wird. Wenn Sie viele oder alle Übereinstimmungen anzeigen möchten, entfernen Sie den `break`-Tag. {% endalert %}

### Erinnerung für ein bevorstehendes Ereignis erstellen {#misc-event-reminder}

Dieser Anwendungsfall ermöglicht es Nutzer:innen, bevorstehende Erinnerungen basierend auf angepassten Events einzurichten. Das Beispielszenario ermöglicht es, eine Erinnerung für ein Verlängerungsdatum einer Police einzurichten, das 26 oder mehr Tage entfernt ist, wobei Erinnerungen 26, 13, 7 oder 2 Tage vor dem Verlängerungsdatum gesendet werden.

Bei diesem Anwendungsfall sollte Folgendes im Body einer [Webhook-Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) oder eines Canvas-Schritts stehen.

{% raw %}
```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties sent to Braze.
{% endcomment %}

{% comment %}
When testing, make sure the campaign ID, campaign API endpoint, Canvas ID, Canvas API endpoint are entered correctly. In this example, the Canvas ID and Canvas API endpoint have been set up for sharing with the client. In practice, this can be testing using a campaign ID and Campaign API endpoint.
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away; if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 > {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away but more than seven days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 > {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than seven days away but more than two days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% elsif {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %}

Sie benötigen ein angepasstes Event `reminder_capture`, und die angepassten Event-Eigenschaften müssen mindestens Folgendes enthalten:

- `reminder-id`: Bezeichner des angepassten Events
- `reminder_date`: Vom/von der Nutzer:in eingereichtes Datum, an dem die Erinnerung fällig ist
- `message_personalisation_X`: Alle Eigenschaften, die zur Personalisierung der Nachricht zum Sendezeitpunkt benötigt werden

{% endalert %}

### String in einem Array finden {#misc-string-in-array}

Dieser Anwendungsfall prüft, ob ein Array eines angepassten Attributs einen bestimmten String enthält, und zeigt in diesem Fall eine spezifische Nachricht an.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### Größten Wert in einem Array finden {#misc-largest-value}

Dieser Anwendungsfall berechnet den höchsten Wert in einem gegebenen Array eines angepassten Attributs, um ihn in Nachrichten zu verwenden.

Beispielsweise möchten Sie einem/einer Nutzer:in den aktuellen Highscore oder das höchste Gebot für einen Artikel anzeigen.

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
Sie müssen ein angepasstes Attribut verwenden, das einen ganzzahligen Wert hat und Teil eines Arrays (Liste) ist. {% endalert %}

### Kleinsten Wert in einem Array finden {#misc-smallest-value}

Dieser Anwendungsfall berechnet den niedrigsten Wert in einem gegebenen Array eines angepassten Attributs, um ihn in Nachrichten zu verwenden.

Beispielsweise möchten Sie einem/einer Nutzer:in den niedrigsten Punktestand oder den günstigsten Artikel anzeigen.

{% raw %}
```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %} Sie müssen ein angepasstes Attribut verwenden, das einen ganzzahligen Wert hat und Teil eines Arrays (Liste) ist. {% endalert %}

### Ende eines Strings abfragen {#misc-query-end-of-string}

Dieser Anwendungsfall fragt das Ende eines Strings ab, um es in Nachrichten zu verwenden.

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}}} | first %}
{% assign marketplace = interest | split: "" | reverse | join: "" | truncate: 4, "" %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Werte in einem Array aus einem angepassten Attribut mit mehreren Kombinationen abfragen {#misc-query-array-values}

Dieser Anwendungsfall nimmt eine Liste von bald ablaufenden Serien, prüft, ob Lieblingsserien in dieser Liste enthalten sind, und zeigt in diesem Fall eine Nachricht an, dass diese bald ablaufen.

{% raw %}
```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not found") %}
{% endif %}
```
{% endraw %}

{% alert important %} Sie müssen zuerst Übereinstimmungen zwischen den Arrays finden und dann am Ende eine Logik aufbauen, um die Übereinstimmungen aufzuteilen. {% endalert %}

### String als Telefonnummer formatieren {#phone-number}

Dieser Anwendungsfall zeigt, wie das Kundenprofil-Feld `phone_number` (standardmäßig als String aus Ziffern formatiert) indiziert und basierend auf Ihren lokalen Telefonnummernstandards neu formatiert wird. Beispiel: 1234567890 wird zu (123)-456-7890.

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## Plattform-Targeting {#platform-targeting}

{% apitags %}
Platform targeting
{% endapitags %}

- [Text nach Geräte-Betriebssystem differenzieren](#platform-device-os)
- [Nur eine bestimmte Plattform ansprechen](#platform-target)
- [Nur iOS-Geräte mit einer bestimmten Betriebssystemversion ansprechen](#platform-target-ios-version)
- [Nur Webbrowser ansprechen](#platform-target-web)
- [Einen bestimmten Mobilfunkanbieter ansprechen](#platform-target-carrier)

### Text nach Geräte-Betriebssystem differenzieren {#platform-device-os}

Dieser Anwendungsfall prüft, auf welcher Plattform sich ein/e Nutzer:in befindet, und zeigt je nach Plattform spezifische Nachrichten an.

Beispielsweise möchten Sie mobilen Nutzer:innen kürzere Textversionen zeigen, während andere Nutzer:innen die reguläre, längere Version erhalten. Sie könnten mobilen Nutzer:innen auch bestimmte Nachrichten zeigen, die für sie relevant sind, aber für Web-Nutzer:innen nicht. Beispielsweise könnte iOS-Messaging über Apple Pay sprechen, während Android-Messaging Google Pay erwähnen sollte.

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else %}
This is the regular copy and much longer than the short version.
{% endif %}
```
{% endraw %}

{% alert note %}
Liquid unterscheidet Groß- und Kleinschreibung. `targeted_device.${platform}` gibt den Wert in Kleinbuchstaben zurück.
{% endalert %}

### Nur eine bestimmte Plattform ansprechen {#platform-target}

Dieser Anwendungsfall erfasst die Geräteplattform und zeigt je nach Plattform eine Nachricht an.

Beispielsweise möchten Sie eine Nachricht nur an Android-Nutzer:innen senden. Dies kann als Alternative zur Auswahl einer App im Segmentierungs-Tool verwendet werden.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %}

This is a message for an Android user!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Nur Geräte mit einer bestimmten Betriebssystemversion ansprechen {#platform-target-ios-version}

Dieser Anwendungsfall prüft, ob die Betriebssystemversion innerhalb einer bestimmten Gruppe von Versionen liegt, und zeigt in diesem Fall eine spezifische Nachricht an.

Das verwendete Beispiel sendet eine Warnung an Nutzer:innen mit Betriebssystemversion 10.0 oder älter, dass der Support für ihr Geräte-Betriebssystem eingestellt wird.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Nur Webbrowser ansprechen {#platform-target-web}

Dieser Anwendungsfall prüft, ob das Zielgerät unter Mac oder Windows läuft, und zeigt in diesem Fall eine spezifische Nachricht an.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

Der folgende Anwendungsfall prüft, ob ein/e Web-Nutzer:in iOS oder Android verwendet, und zeigt in diesem Fall eine spezifische Nachricht an.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'iOS' and {{targeted_device.${platform}}} == 'web' %}

Content for iOS.

{% elsif {{targeted_device.${os}}} == 'android' and {{targeted_device.${platform}}} == 'web' %}

Content for Android.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Einen bestimmten Mobilfunkanbieter ansprechen {#platform-target-carrier}

Dieser Anwendungsfall prüft, ob der Mobilfunkanbieter des Geräts Verizon ist, und zeigt in diesem Fall eine spezifische Nachricht an.

Für Push-Benachrichtigungen und In-App Messages-Kanäle können Sie den Mobilfunkanbieter im Nachrichtentext mithilfe von Liquid angeben. Wenn der Mobilfunkanbieter des Empfängers/der Empfängerin nicht übereinstimmt, wird die Nachricht nicht gesendet.

{% raw %}
```liquid
{% if {{targeted_device.${carrier}}} contains "verizon" or {{targeted_device.${carrier}}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## SMS

{% apitags %}
SMS
{% endapitags %}

- [Verschiedene Nachrichten basierend auf eingehenden SMS-Schlüsselwörtern senden](#sms-keyword-response)

### Verschiedene Nachrichten basierend auf eingehenden SMS-Schlüsselwörtern senden {#sms-keyword-response}

Dieser Anwendungsfall nutzt die dynamische SMS-Schlüsselwortverarbeitung, um auf bestimmte eingehende Nachrichten mit unterschiedlichem Nachrichtentext zu antworten. Beispielsweise können Sie verschiedene Antworten senden, wenn jemand „START“ im Vergleich zu „JOIN“ schreibt.

{% raw %}
```liquid
{% assign inbound_message = {{sms.${inbound_message_body}}} | downcase | strip %}
{% if inbound_message contains 'start' %}
Thanks for joining our SMS program! Make sure your account is up to date for the best deals!

{% elsif inbound_message contains 'join' %}
Thanks for joining our SMS program! Create an account to get the best deals!

{% else %}
Thanks for joining our SMS program!

{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Zeitzonen {#time-zones}

{% apitags %}
Time zones
{% endapitags %}

- [Zeitzone des/der Nutzer:in einfügen](#users-time-zone)
- [Nachricht basierend auf der Zeitzone personalisieren](#personalize-timezone)
- [CST-Zeitzone an ein angepasstes Attribut anhängen](#time-append-cst)
- [Zeitstempel einfügen](#time-insert-timestamp)
- [Canvas-Push nur innerhalb eines Zeitfensters in der lokalen Zeitzone senden](#time-canvas-window)
- [Wiederkehrende In-App-Nachricht innerhalb eines Zeitfensters in der lokalen Zeitzone senden](#time-reocurring-iam-window)
- [Verschiedene Nachrichten an Wochentagen und Wochenenden in der lokalen Zeitzone senden](#time-weekdays-vs-weekends)
- [Verschiedene Nachrichten basierend auf der Tageszeit in der lokalen Zeitzone senden](#time-of-day)
- [Nachricht außerhalb eines Stundenbereichs zum Sendezeitpunkt abbrechen](#abort-send-time-hour-range)
- [Nachricht außerhalb eines Zeitfensters in einer festen Zeitzone abbrechen](#abort-fixed-timezone-window)

{% alert note %}
Wenn ein/e Nutzer:in eine Nachricht zu einer unerwarteten Ortszeit erhält, hat sich möglicherweise die Zeitzone des Geräts oder Profils geändert (z. B. nach einer Reise). Die Zustellung zur Ortszeit verwendet die Zeitzone im Profil zum Sendezeitpunkt; Nutzer:innen benötigen möglicherweise eine neue Sitzung in ihrer gewohnten Region, bevor Werte wie {% raw %}`{{${time_zone}}}`{% endraw %} das erwartete Ergebnis liefern. Sie können jedoch [die Zeitzone des/der Nutzer:in einfügen](#users-time-zone).
{% endalert %}

### Zeitzone des/der Nutzer:in einfügen {#users-time-zone}

Standardmäßig werden Daten und Uhrzeiten in Liquid in koordinierter Weltzeit (UTC) dargestellt. Um Daten und Uhrzeiten in der lokalen Zeitzone anzuzeigen, verwenden Sie den `time_zone`-Filter zusammen mit dem `date`-Filter.

#### Lokales Datum und Uhrzeit zuweisen {#assign-local-date-and-time}

Um eine Variable zuzuweisen, die das aktuelle Datum und die Uhrzeit in der lokalen Zeitzone widerspiegelt, verwenden Sie dieses Format:

{% raw %}
```liquid
{% assign local_date_time = 'now' | time_zone:{{${time_zone}}} | date: '%B %e, %Y' %}
{{local_date_time}}
```
{% endraw %}

- `now`: Ruft das aktuelle Datum und die Uhrzeit in UTC ab.
- `time_zone`: Ruft die lokale Zeitzone aus dem Standardattribut mithilfe des {% raw %}`{{${time_zone}}}`{% endraw %}-Personalisierungs-Tags ab.
- `date`: Formatiert das lokale Datum und die Uhrzeit gemäß Ihren Angaben. Im vorherigen Beispiel zeigt das System einen String im Format „February 26, 2026“ an. Weitere Formatierungsoptionen finden Sie unter [strftime.net](strftime.net).

#### Zeitzone mit angepassten Attributen anwenden {#apply-the-users-time-zone-with-custom-attributes}

Sie können den `time_zone`-Filter auf angepasste Attribute anwenden, wie folgt:

{% raw %}
```liquid
{{custom_attribute.${date_time_attribute} | time_zone: {{${time_zone}}} | date: '%a, %b %e, %Y'}}
```
{% endraw %}

Dies gibt das `date_time_attribute` formatiert als abgekürzten Wochentag, gefolgt vom abgekürzten Monat, Tag und vierstelligen Jahr aus.

### Nachricht basierend auf der Zeitzone personalisieren {#personalize-timezone}

Dieser Anwendungsfall zeigt verschiedene Nachrichten basierend auf der Zeitzone an.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'xx' %}
Message for time zone xx.
{% elsif {{${time_zone}}} == 'yy' %}
Message for time zone yy.
{% else %}
{% abort_message("Invalid time zone") %}
{% endif %}
```
{% endraw %}

### CST-Zeitzone an ein angepasstes Attribut anhängen {#time-append-cst}

Dieser Anwendungsfall zeigt ein angepasstes Datumsattribut in einer bestimmten Zeitzone an.

Option 1:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

Option 2:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### Zeitstempel einfügen {#time-insert-timestamp}

Dieser Anwendungsfall zeigt eine Nachricht mit einem Zeitstempel in der aktuellen Zeitzone an.

Das folgende Beispiel zeigt das Datum im Format JJJJ-MM-TT HH:MM:SS an, z. B. 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### Canvas-Push nur innerhalb eines Zeitfensters in der lokalen Zeitzone senden {#time-canvas-window}

Dieser Anwendungsfall prüft die Uhrzeit in der lokalen Zeitzone, und wenn sie innerhalb eines festgelegten Zeitfensters liegt, wird eine spezifische Nachricht angezeigt.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8 am and 8 pm!
```
{% endraw %}

### Wiederkehrende In-App-Nachricht innerhalb eines Zeitfensters in der lokalen Zeitzone senden {#time-reocurring-iam-window}

Dieser Anwendungsfall zeigt eine Nachricht an, wenn die aktuelle Uhrzeit innerhalb eines festgelegten Fensters liegt.

Das folgende Szenario informiert beispielsweise darüber, dass ein Geschäft geschlossen ist.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11 am and 9 pm!

{% else %}
{% abort_message("Not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### Verschiedene Nachrichten an Wochentagen und Wochenenden in der lokalen Zeitzone senden {#time-weekdays-vs-weekends}

Dieser Anwendungsfall prüft, ob der aktuelle Wochentag Samstag oder Sonntag ist, und zeigt je nach Tag unterschiedliche Nachrichten an.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It's {{today}}, why don't you open the app for your transactions?

{% else %}
It's {{today}}, why don't you visit the store?
{% endif %}
```
{% endraw %}

### Verschiedene Nachrichten basierend auf der Tageszeit in der lokalen Zeitzone senden {#time-of-day}

Dieser Anwendungsfall zeigt eine Nachricht an, wenn die aktuelle Uhrzeit außerhalb eines festgelegten Fensters liegt.

Beispielsweise möchten Sie über eine zeitkritische Gelegenheit informieren, die von der Tageszeit abhängt.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

{% alert note %} Dies ist das Gegenteil von [Ruhezeiten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types#time-based-options). {% endalert %}

### Nachricht außerhalb eines Stundenbereichs zum Sendezeitpunkt abbrechen {#abort-send-time-hour-range}

Dieser Anwendungsfall bricht die Nachricht ab, wenn die aktuelle Stunde außerhalb eines definierten Bereichs liegt. Er verwendet die Uhrzeit, zu der die Nachricht gerendert wird, die standardmäßig UTC ist, es sei denn, Sie wenden den `time_zone`-Filter an – nicht die lokale Zeitzone des/der Nutzer:in. Um Nachrichten basierend auf der lokalen Zeitzone zu senden, siehe [Verschiedene Nachrichten basierend auf der Tageszeit in der lokalen Zeitzone senden](#time-of-day).

{% raw %}
```liquid
{% assign time = 'now' %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside hour range") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

### Nachricht außerhalb eines Zeitfensters in einer festen Zeitzone abbrechen {#abort-fixed-timezone-window}

Dieser Anwendungsfall bricht die Nachricht ab, wenn die aktuelle Uhrzeit außerhalb eines definierten Fensters in einer bestimmten Zeitzone liegt (in diesem Beispiel Singapur-Zeit). Sie können dieses Muster verwenden, wenn Sie eine Ruhezeiten-ähnliche Regel benötigen, die an eine Region gebunden ist, anstatt an das `time_zone`-Attribut jedes/jeder Nutzer:in.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: 'Asia/Singapore' %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% assign minute = time | date: '%M' | plus: 0 %}

{% if hour < 20 or hour > 21 or (hour == 21 and minute > 45) %}
{% abort_message("Not within eligible time of 8 pm–9:45 pm SGT") %}
{% endif %}

Sign up for our exclusive time-limited offer now!
```
{% endraw %}

{% endapi %}

{% api %}

## Woche/Tag/Monat {#weekdaymonth}

{% apitags %}
Week/Day/Month
{% endapitags %}

- [Namen des Vormonats in eine Nachricht einfügen](#month-name)
- [Campaign am Ende jedes Monats senden](#month-end)
- [Campaign am letzten (Wochen-)Tag des Monats senden](#day-of-month-last)
- [Jeden Tag des Monats eine andere Nachricht senden](#day-of-month)
- [Jeden Wochentag eine andere Nachricht senden](#day-of-week)
- [Nachricht an einem bestimmten Kalenderdatum abbrechen](#abort-specific-calendar-date)
- [Nachricht an einem bestimmten Wochentag abbrechen](#abort-specific-weekday)

### Namen des Vormonats in eine Nachricht einfügen {#month-name}

Dieser Anwendungsfall nimmt den aktuellen Monat und zeigt den Vormonat an, um ihn in Nachrichten zu verwenden.

{% raw %}
```liquid
{% assign today = 'now' | date: "%m" %}
{% assign last_month = {{today}} | minus: 1 %}
{% if last_month == 1 %}
{% assign month = "January" %}
{% elsif last_month == 2 %}
{% assign month = "February" %}
{% elsif last_month == 3 %}
{% assign month = "March" %}
{% elsif last_month == 4 %}
{% assign month = "April" %}
{% elsif last_month == 5 %}
{% assign month = "May" %}
{% elsif last_month == 6 %}
{% assign month = "June" %}
{% elsif last_month == 7 %}
{% assign month = "July" %}
{% elsif last_month == 8 %}
{% assign month = "August" %}
{% elsif last_month == 9 %}
{% assign month = "September" %}
{% elsif last_month == 10 %}
{% assign month = "October" %}
{% elsif last_month == 11 %}
{% assign month = "November" %}
{% elsif last_month == 0 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

Alternativ können Sie Folgendes verwenden, um dasselbe Ergebnis zu erzielen.

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{last_month_name}}.
```
{% endraw %}

### Campaign am Ende jedes Monats senden {#month-end}

Dieser Anwendungsfall prüft, ob das aktuelle Datum in einer Liste von Daten enthalten ist, und zeigt je nach Datum eine spezifische Nachricht an.

{% alert note %} Schaltjahre (29. Februar) werden nicht berücksichtigt. {% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

The date is correct

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
```
{% endraw %}

### Campaign am letzten (Wochen-)Tag des Monats senden {#day-of-month-last}

Dieser Anwendungsfall erfasst den aktuellen Monat und Tag und berechnet, ob der aktuelle Tag auf den letzten Wochentag des Monats fällt.

Beispielsweise möchten Sie am letzten Mittwoch des Monats eine Umfrage an Ihre Nutzer:innen senden, um Produktfeedback einzuholen.

{% raw %}
```liquid
{% comment %}Pull the day, day name, month, and year from today's date.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assign the correct number of days for the current month.{% endcomment %}

{% if current_month == "Jan" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Mar" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Apr" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "May" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Jun" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Jul" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Aug" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Sep" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Oct" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Nov" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Dec" %}
{% assign last_day_of_month = 31 %}
{% endif %}

{% comment %}Assign the correct number of days if the current month is February, taking into account leap years.{% endcomment %}

{% assign leap_year_remainder = current_year | modulo: 4 %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Check that today's date is within a week of the last day of the month. If not, abort the message. If so, check that today is Wednesday. If not, abort the message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%}
{% if diff_in_days <= 7 %}
{% unless current_day_name == "Wed" %}
{% abort_message("Wrong day of the week") %}
{% endunless %}
{% else %}
{% abort_message("Not the last week of the month") %}
{% endif %}
```
{% endraw %}

### Jeden Tag des Monats eine andere Nachricht senden {#day-of-month}

Dieser Anwendungsfall prüft, ob das aktuelle Datum mit einem Datum in einer Liste übereinstimmt, und zeigt je nach Tag eine eigene Nachricht an.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
```
{% endraw %}

### Jeden Wochentag eine andere Nachricht senden {#day-of-week}

Dieser Anwendungsfall prüft den aktuellen Wochentag und zeigt je nach Tag eine eigene Nachricht an.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
{% when 'Monday' %}
Monday copy

{% when 'Tuesday' %}
Tuesday copy

{% when 'Wednesday' %}
Wednesday copy

{% when  'Thursday' %}
Thursday copy

{% when  'Friday' %}
Friday copy

{% when 'Saturday' %}
Saturday copy

{% when 'Sunday' %}
Sunday copy

{% else %}
Default copy
{% endcase %}
```
{% endraw %}

{% alert note %}
Sie können die Zeile „Default copy“ durch {% raw %}`{% abort_message() %}`{% endraw %} ersetzen, um zu verhindern, dass die Nachricht gesendet wird, wenn der Wochentag unbekannt ist.
{% endalert %}

### Nachricht an einem bestimmten Kalenderdatum abbrechen {#abort-specific-calendar-date}

Dieser Anwendungsfall bricht die Nachricht an einem gewählten Monat und Tag jedes Jahr ab (im Beispiel der 5. Mai). Er vergleicht das aktuelle Datum mit einem eindeutigen Monat-Tag-String, der mit dem `date`-Filter erstellt wird.

{% raw %}
```liquid
{% assign date = 'now' | date: '%d/%m' %}
{% if date == '05/05' %}
{% abort_message('No message on the 5th of May') %}
{% endif %}
```
{% endraw %}

### Nachricht an einem bestimmten Wochentag abbrechen {#abort-specific-weekday}

Dieser Anwendungsfall bricht die Nachricht ab, wenn Liquid an einem bestimmten Wochentag ausgeführt wird (im Beispiel `Wednesday`). Der Filter `%A` gibt den vollständigen englischen Wochentagsnamen zurück.

{% raw %}
```liquid
{% assign weekday = 'now' | date: '%A' %}
{% if weekday == 'Wednesday' %}
{% abort_message("No message on Wednesdays") %}
{% endif %}
```
{% endraw %}

{% endapi %}

Viele Beispiele in dieser Bibliothek verwenden den `abort_message`-Tag, um einen Versand zu überspringen, wenn Bedingungen nicht erfüllt sind. Eine vollständige Referenz zum Abbrechen von Versendungen mit Liquid, einschließlich datums- und zeitbasierter Muster, finden Sie unter [Liquid-Nachrichten abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).