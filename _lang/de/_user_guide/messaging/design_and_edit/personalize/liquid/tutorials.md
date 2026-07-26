---
nav_title: Tutorials
article_title: "Tutorials: Liquid-Code schreiben"
page_order: 11
description: "Diese Referenzseite enthält einsteigerfreundliche Tutorials, die Ihnen den Einstieg in Liquid-Code erleichtern."
page_type: tutorial
---

# Tutorials: Liquid-Code schreiben {#tutorials-writing-liquid-code}

> Neu bei Liquid? Diese Tutorials helfen Ihnen beim Einstieg in das Schreiben von Liquid-Code für einsteigerfreundliche Anwendungsfälle. Jedes Tutorial behandelt eine andere Kombination von Lernzielen, wie bedingte Logik und Operatoren.

Wenn Sie diese Tutorials abgeschlossen haben, können Sie:

- Liquid-Code für gängige Anwendungsfälle schreiben
- Bedingte Liquid-Logik verketten, um Nachrichten basierend auf Nutzerdaten zu personalisieren
- Variablen und Filter verwenden, um Gleichungen zu schreiben, die die Werte von Attributen nutzen
- Grundlegende Befehle in Liquid-Code erkennen und ein allgemeines Verständnis dafür entwickeln, was der Code bewirkt

| Tutorial | Lernziele |
| --- | --- |
| [Nachrichten für Nutzersegmente personalisieren](#segments) | Standardwerte, bedingte Logik |
| [Warenkorb-Abbruch-Erinnerungen](#reminders) | Operatoren, bedingte Logik |
| [Event-Countdown](#countdown) | Variablen, Datumsfilter |
| [Monatliche Geburtstagsnachricht](#birthday) | Variablen, Datumsfilter, Operatoren |
| [Lieblingsprodukt bewerben](#favorite-product) | Variablen, Datumsfilter, Gleichungen, Operatoren |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Tutorials: Liquid-Code schreiben" }

## Personalisierte Nachrichten für Nutzersegmente {#segments}

Lassen Sie uns Nachrichten für verschiedene Nutzersegmente anpassen, z. B. für VIP-Kund:innen und neue Abonnent:innen.

1. Öffnen Sie die Nachricht mit personalisierten Begrüßungen, die gesendet werden soll, wenn Sie den Vornamen einer Nutzer:in haben und wenn nicht. Erstellen Sie dazu einen Liquid-Tag, der das Attribut `first_name` und einen Standardwert enthält, der verwendet wird, wenn `first_name` leer ist. In diesem Szenario verwenden wir „traveler“ als Standardwert.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2. Jetzt legen wir die Nachricht fest, die gesendet werden soll, wenn die Nutzer:in eine VIP-geschäftskunden ist. Dafür benötigen wir einen bedingten Logik-Tag: `if`. Dieser Tag besagt, dass wenn das angepasste Attribut `vip_status` gleich `VIP` ist, der folgende Liquid-Code ausgeführt wird. In diesem Fall wird eine bestimmte Nachricht gesendet.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3. Senden wir eine angepasste Nachricht für Nutzer:innen, die neue Abonnent:innen sind. Wir verwenden den bedingten Logik-Tag `elsif`, um festzulegen, dass wenn der `vip_status` der Nutzer:in `new` ist, die folgende Nachricht gesendet wird.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4. Was ist mit Nutzer:innen, die weder VIP noch neu sind? Wir können mit dem `else`-Tag eine Nachricht an alle anderen Nutzer:innen senden, der festlegt, dass die folgende Nachricht gesendet werden soll, wenn die vorherigen Bedingungen nicht erfüllt sind. Dann können wir die bedingte Logik mit dem `endif`-Tag schließen, da es keine weiteren VIP-Status zu berücksichtigen gibt.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## Warenkorb-Abbruch-Erinnerungen {#reminders}

Senden wir personalisierte Nachrichten, um Nutzer:innen an Artikel in ihrem Warenkorb zu erinnern. Wir passen sie weiter an, sodass sie basierend auf der Anzahl der Artikel im Warenkorb gesendet werden – wenn drei oder weniger Artikel vorhanden sind, listen wir alle Artikel auf. Bei mehr als drei Artikeln senden wir eine kompaktere Nachricht.

1. Prüfen wir zunächst, ob der Warenkorb der Nutzer:in leer ist, indem wir eine bedingte Liquid-Logik mit dem Operator `!=` öffnen, der „ist nicht gleich“ bedeutet. In diesem Fall setzen wir die Bedingung so, dass das angepasste Attribut `cart_items` nicht einem leeren Wert entspricht.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2. Dann müssen wir den Fokus eingrenzen und prüfen, ob der Warenkorb mehr als drei Artikel enthält, indem wir den Operator `>` verwenden, der „größer als“ bedeutet.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3. Schreiben Sie eine Nachricht, die die Nutzer:in mit ihrem Vornamen begrüßt, oder verwenden Sie „there“ als Standardwert, falls dieser nicht verfügbar ist. Geben Sie an, was angezeigt werden soll, wenn mehr als drei Artikel im Warenkorb sind. Da wir die Nutzer:in nicht mit einer vollständigen Liste überfordern möchten, listen wir die ersten drei `cart_items` auf.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4. Verwenden Sie den `else`-Tag, um festzulegen, was passieren soll, wenn die vorherigen Bedingungen nicht erfüllt sind (mit anderen Worten, wenn `cart_items` leer ist oder weniger als drei enthält), und geben Sie dann die zu sendende Nachricht an. Da drei Artikel nicht viel Platz einnehmen, können wir alle auflisten. Wir verwenden den Liquid-Operator `join` und `,`, um festzulegen, dass die Artikel durch ein Komma getrennt aufgelistet werden. Schließen Sie die Logik mit `endif`.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
```
{% endraw %}

{: start="5"}
5. Verwenden Sie `else` und dann eine `abort_message`, um dem Liquid-Code mitzuteilen, dass keine Nachricht gesendet werden soll, wenn der Warenkorb keine der vorherigen Bedingungen erfüllt. Mit anderen Worten, wenn der Warenkorb leer ist. Schließen Sie die Logik mit `endif`.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Event-Countdown {#countdown}

Senden wir Nutzer:innen eine Nachricht, die angibt, wie viele Tage bis zu einem Jubiläumsverkauf verbleiben. Dazu verwenden wir Variablen, um Gleichungen zu erstellen, die die Werte von Attributen manipulieren.

1. Weisen wir zunächst der Variablen `sale_date` das angepasste Attribut `anniversary_date` zu und wenden den Filter `date: "s"` an. Dieser konvertiert das `anniversary_date` in ein Zeitstempel-Format, das in Sekunden ausgedrückt wird, und weist diesen Wert dann `sale_date` zu.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2. Wir müssen auch eine Variable zuweisen, die den heutigen Zeitstempel erfasst. Weisen wir die Variable `today` dem Wert `now` (aktuelles Datum und Uhrzeit) zu und wenden dann den Filter `date: "%s"` an.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3. Berechnen wir nun, wie viele Sekunden zwischen jetzt (`today`) und dem Jubiläumsverkauf (`sale_date`) liegen. Weisen Sie dazu der Variablen `difference` den Wert von `sale_date` minus `today` zu.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4. Jetzt müssen wir `difference` in einen Wert umwandeln, den wir in einer Nachricht referenzieren können, da es nicht ideal ist, der Nutzer:in mitzuteilen, wie viele Sekunden es bis zu einem Verkauf sind. Weisen wir `difference_days` dem `difference`-Wert zu und teilen ihn durch `86400`, um die Anzahl der Tage zu erhalten.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5. Erstellen wir abschließend die zu sendende Nachricht.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## Monatliche Geburtstagsnachricht {#birthday}

Senden wir eine besondere Aktion an alle Nutzer:innen, deren Geburtstag in den aktuellen Monat fällt. Nutzer:innen, die in diesem Monat keinen Geburtstag haben, erhalten keine Nachricht.

1. Ziehen wir zunächst den aktuellen Monat. Wir weisen die Variable `this_month` dem Wert `now` (aktuelles Datum und Uhrzeit) zu und verwenden dann den Filter `date: "%B"`, um festzulegen, dass die Variable dem Monat entsprechen soll.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2. Ziehen wir nun den Geburtsmonat aus dem `date_of_birth` der Nutzer:in. Wir weisen die Variable `birth_month` dem Wert `date_of_birth` zu und verwenden dann den Filter `date: "%B"`.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3. Da wir nun zwei Variablen haben, die einen Monat als Wert enthalten, können wir sie mit bedingter Logik vergleichen. Setzen wir die Bedingung so, dass `this_month` dem `birth_month` der Nutzer:in entspricht.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4. Erstellen wir die Nachricht, die gesendet werden soll, wenn dieser Monat auch der Geburtsmonat der Nutzer:in ist.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5. Verwenden Sie den `else`-Tag, um festzulegen, was passiert, wenn die Bedingung nicht erfüllt ist (weil dieser Monat nicht der Geburtsmonat der Nutzer:in ist).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="6"}
6. Wir möchten keine Nachricht senden, wenn der Geburtsmonat der Nutzer:in nicht dieser Monat ist, also verwenden wir `abort_message`, um die Nachricht abzubrechen, und schließen dann die bedingte Logik mit `endif`.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %}
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Lieblingsprodukt bewerben {#favorite-product}

Bewerben wir das Lieblingsprodukt einer Nutzer:in, wenn ihr letzter Kauf mehr als sechs Monate zurückliegt.

1. Zunächst verwenden wir bedingte Logik, um zu prüfen, ob wir das Lieblingsprodukt und das letzte Kaufdatum der Nutzer:in haben.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2. Dann legen wir fest, dass keine Nachricht gesendet werden soll, wenn wir das Lieblingsprodukt oder das letzte Kaufdatum der Nutzer:in nicht haben.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3. Wir verwenden `else`, um festzulegen, was passieren soll, wenn die obige Bedingung nicht erfüllt ist (weil wir das Lieblingsprodukt und das letzte Kaufdatum der Nutzer:in _haben_).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4. Wenn wir das Kaufdatum haben, müssen wir es einer Variablen zuweisen, damit wir es mit dem heutigen Datum vergleichen können. Erstellen wir zunächst einen Wert für das heutige Datum, indem wir die Variable `today` dem Wert `now` (aktuelles Datum und Uhrzeit) zuweisen und den Filter `date: "%s"` verwenden, um den Wert in ein Zeitstempel-Format in Sekunden umzuwandeln. Wir fügen den Filter `plus: 0` hinzu, um eine „0“ zum Zeitstempel hinzuzufügen. Dies ändert den Wert des Zeitstempels nicht, ist aber nützlich für die Verwendung des Zeitstempels in zukünftigen Gleichungen.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5. Erfassen wir nun das letzte Kaufdatum in Sekunden, indem wir die Variable `last_purchase_date` dem angepassten Attribut `last_purchase_date` zuweisen und den Filter `date: "s"` verwenden. Wir fügen erneut den Filter `plus: 0` hinzu.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6. Da das letzte Kaufdatum und das heutige Datum in Sekunden vorliegen, müssen wir berechnen, wie viele Sekunden sechs Monate entsprechen. Erstellen wir eine Gleichung (ungefähr 6 Monate \* 30,44 Tage \* 24 Stunden \* 60 Minuten \* 60 Sekunden) und weisen sie der Variablen `six_months` zu. Wir verwenden `times`, um die Multiplikation der Zeiteinheiten anzugeben.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7. Da nun alle unsere Zeitwerte in Sekunden vorliegen, können wir ihre Werte in Gleichungen verwenden. Weisen wir eine Variable namens `today_minus_last_purchase_date` zu, die den heutigen Wert nimmt und das `last_purchase_date` davon abzieht. Dies ergibt, wie viele Sekunden seit dem letzten Kauf vergangen sind.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8. Vergleichen wir nun unsere Zeitwerte direkt in bedingter Logik. Definieren wir die Bedingung so, dass `today_minus_last_purchase_date` größer oder gleich (`>=`) sechs Monaten ist. Mit anderen Worten: Der letzte Kauf liegt mindestens sechs Monate zurück.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9. Erstellen wir die Nachricht, die gesendet werden soll, wenn der letzte Kauf mindestens sechs Monate zurückliegt.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10. Wir verwenden den `else`-Tag, um festzulegen, was passieren soll, wenn die Bedingung nicht erfüllt ist (weil der Kauf nicht mindestens sechs Monate zurückliegt).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11. Wir fügen eine `abort_message` ein, um die Nachricht abzubrechen.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12. Zum Abschluss beenden wir den Liquid-Code mit zwei `endif`-Tags. Das erste `endif` schließt die bedingte Prüfung für das Lieblingsprodukt oder das letzte Kaufdatum, und das zweite `endif` schließt die bedingte Prüfung, ob der letzte Kauf mindestens sechs Monate zurückliegt.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details Vollständiger Liquid-Code %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}