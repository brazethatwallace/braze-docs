---
nav_title: Nachrichten abbrechen
article_title: Liquid-Nachrichten abbrechen
page_order: 7
description: "Dieser Referenzartikel behandelt das Abbrechen von Liquid-Nachrichten und einige Beispielanwendungsfälle."

---

# Nachrichten abbrechen {#abort-messages}

> Optional können Sie den Liquid-Nachrichten-Tag `abort_message("optional reason for aborting")` innerhalb von Bedingungen verwenden, um das Senden einer Nachricht an eine:n Nutzer:in zu verhindern. Dieser Referenzartikel listet einige Beispiele auf, wie dieses Feature in Marketing-Kampagnen verwendet werden kann.

{% alert note %}
Wenn ein Nachrichtenschritt in einem Canvas abgebrochen wird, verlässt die/der Nutzer:in den Canvas **nicht** und **wird** zum nächsten Schritt weitergeleitet.
{% endalert %}

## Testsendungen mit `abort_message()` {#test-sends-with-abort_message}

`abort_message()` stoppt den Versand für Nutzer:innen, die Ihre Bedingung nicht erfüllen. Die Nachricht wird nicht in ihrem Profil angezeigt und zählt weder als Zustellung noch für das Frequency-Capping.

Wenn Testsendungen nie ankommen, zeigen Sie eine Vorschau als Nutzer:in an, die/der die Abbruchbedingung erfüllt, und aktivieren Sie dann unter **Test Send** die Option **Override recipients' attributes with current preview user's attributes** (oder fügen Sie ein Mitglied einer Content-Testgruppe hinzu, das die Bedingung erfüllt).

## Nachricht abbrechen, wenn „Number Games Attended“ = 0 {#abort-message-if-number-games-attended-0}

Nehmen wir zum Beispiel an, Sie möchten keine Nachricht an Kund:innen senden, die kein Spiel besucht haben:

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

Diese Nachricht wird nur an Kund:innen gesendet, die nachweislich ein Spiel besucht haben.

## Nur englischsprachige Kund:innen anschreiben {#message-english-speaking-customers-only}

Sie können nur englischsprachige Kund:innen anschreiben, indem Sie eine „if“-Anweisung erstellen, die zutrifft, wenn die Sprache der/des Kund:in Englisch ist, und eine „else“-Anweisung, die die Nachricht für alle abbricht, die kein Englisch sprechen oder keine Sprache in ihrem Profil hinterlegt haben.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Standardmäßig protokolliert Braze eine allgemeine Fehlermeldung in Ihrem Nachrichten-Aktivitätsprotokoll:

```text
{% abort_message %} called
```

Sie können die Abbruchnachricht auch dazu veranlassen, etwas in Ihrem Nachrichten-Aktivitätsprotokoll zu protokollieren, indem Sie einen String in die Klammern einfügen:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Fehlerprotokoll für Nachrichten in der Entwicklungskonsole mit einer Abbruchnachricht „language was nil“.]({% image_buster /assets/img_archive/developer_console.png %})

## Abbruchnachrichten abfragen {#query-for-abort-messages}

Sie können den [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) oder Ihr eigenes Data Warehouse verwenden, sofern es mit Braze verbunden ist, um bestimmte Abbruchnachrichten abzufragen, die ausgelöst werden, wenn Liquid-Logik den Abbruch einer Nachricht verursacht.

## Wann die Abbruchlogik ausgewertet wird {#when-abort-logic-is-evaluated}

Der Zeitpunkt der Auswertung der Abbruchlogik hängt vom Nachrichtenkanal ab.

### Push, E-Mail, SMS, Webhooks und Content Cards {#push-email-sms-webhooks-and-content-cards}

Die Abbruchlogik wird zum Sendezeitpunkt ausgewertet, wenn Braze die Nachricht für die Zustellung verarbeitet.

### In-App-Nachrichten {#in-app-messages}

Die Abbruchlogik wird nur bei [vorlagenbasierten In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/#templated_iam-templated) zu dem Zeitpunkt ausgewertet, an dem die In-App-Nachricht getriggert wird (zum Beispiel wenn die/der Nutzer:in das Trigger-Ereignis ausführt oder eine Sitzung startet), nicht wenn die Nachricht ursprünglich an das Gerät gesendet wird. In-App-Nachrichten werden beim Sitzungsstart an das SDK übermittelt und lokal zwischengespeichert; das Liquid – einschließlich aller `abort_message()`-Aufrufe – wird ausgeführt, wenn die Trigger-Bedingung erfüllt ist.

## Hinweise {#considerations}

Der Liquid-Nachrichten-Tag `abort_message()` verhindert das Senden von Nachrichten an Nutzer:innen, was bedeutet, dass die Nachricht nicht in Nutzerprofilen angezeigt wird und weder als Zustellung noch für das Frequency-Capping gezählt wird.