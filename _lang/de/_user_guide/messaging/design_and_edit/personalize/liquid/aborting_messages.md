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

Wenn Testsendungen nie ankommen, zeigen Sie eine Vorschau als Nutzer:in an, die/der die Abbruchbedingung erfüllt, und aktivieren Sie dann unter **Testsendung** die Option **Attribute der Empfänger:innen mit den Attributen der aktuellen Vorschau-Nutzer:in überschreiben** (oder fügen Sie ein Mitglied einer Content-Testgruppe hinzu, das die Bedingung erfüllt).

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

Sie können nur englischsprachige Kund:innen anschreiben, indem Sie eine „if“-Anweisung erstellen, die zutrifft, wenn die Sprache der/des geschäftskunden Englisch ist, und eine „else“-Anweisung, die die Nachricht für alle abbricht, die kein Englisch sprechen oder keine Sprache in ihrem Profil hinterlegt haben.

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

Sie können den [Abfrage-Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) oder Ihr eigenes Data Warehouse verwenden, sofern es mit Braze verbunden ist, um bestimmte Abbruchnachrichten abzufragen, die ausgelöst werden, wenn Liquid-Logik den Abbruch einer Nachricht verursacht.

## Wann die Abbruchlogik ausgewertet wird {#when-abort-logic-is-evaluated}

Der Zeitpunkt der Auswertung der Abbruchlogik hängt vom Nachrichtenkanal ab.

### Push, E-Mail, SMS, Webhooks und Content Cards {#push-email-sms-webhooks-and-content-cards}

Die Abbruchlogik wird zum Sendezeitpunkt ausgewertet, wenn Braze die Nachricht für die Zustellung verarbeitet.

### In-App-Nachrichten {#in-app-messages}

Die Abbruchlogik wird nur bei [vorlagenbasierten In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated) zu dem Zeitpunkt ausgewertet, an dem die In-App-Nachricht getriggert wird (zum Beispiel wenn die/der Nutzer:in das Trigger-Ereignis ausführt oder eine Sitzung startet), nicht wenn die Nachricht ursprünglich an das Gerät gesendet wird. In-App-Nachrichten werden beim Sitzungsstart an das SDK übermittelt und lokal zwischengespeichert; das Liquid – einschließlich aller `abort_message()`-Aufrufe – wird ausgeführt, wenn die Trigger-Bedingung erfüllt ist.

## Fehlerbehebung bei hohen Abbruchraten {#troubleshooting-high-abort-rates}

Wenn eine Campaign oder ein Canvas-Schritt viele eingetretene Nutzer:innen zeigt, aber nur wenige Sendungen, oder wenn die Zustellungen niedriger als erwartet ausfallen, ist die Abbruchlogik eine häufige Ursache – insbesondere wenn Liquid Attribute, Katalogdaten oder Listenwerte erfordert, die zum Auswertungszeitpunkt fehlen.

### Nachrichten-Aktivitätsprotokoll prüfen {#check-the-message-activity-log}

1. Öffnen Sie im Braze-Dashboard das [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) für die Campaign oder den Canvas-Nachrichtenschritt.
2. Filtern Sie nach abbruchbezogenen Einträgen. Standardmäßig protokolliert Braze {% raw %}`{% abort_message %}`{% endraw %} called. Wenn Sie einen Begründungsstring an `abort_message()` übergeben haben, wird stattdessen dieser Text angezeigt.
3. Beachten Sie, ob sich Abbrüche auf einen Kanal konzentrieren (zum Beispiel nur E-Mail) oder kanalübergreifend im selben Canvas auftreten.

### Attribute und Liquid zum Sendezeitpunkt überprüfen {#verify-attributes-and-liquid-at-send-time}

Für Push, E-Mail, SMS, Webhooks und Content Cards wird die Abbruchlogik ausgeführt, wenn Braze die Nachricht für die Zustellung verarbeitet – nicht wenn die/der Nutzer:in einen Canvas betreten hat oder ein Trigger-Ereignis zuvor ausgelöst wurde.

- Stellen Sie sicher, dass erforderliche [angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes), Event-Eigenschaften oder [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs)-Felder bei der/dem Nutzer:in gesetzt sind, bevor der Nachrichtenschritt ausgeführt wird.
- Fügen Sie explizite nil- oder Leer-Prüfungen hinzu, bevor Sie `abort_message()` aufrufen. Ein `else`-Zweig, der abbricht, wenn ein Wert fehlt, stoppt den Versand für alle Nutzer:innen ohne diese Daten.
- Wenn die Personalisierung von einer Liste, einem Segment oder einer Connected-Content-Antwort abhängt, stellen Sie sicher, dass diese Daten verfügbar sind, wenn der Nachrichtenschritt ausgeführt wird. Eine:r Nutzer:in kann einen Canvas betreten, bevor die Listenmitgliedschaft oder nachgelagerte Daten bereit sind.

### Canvas-spezifisches Verhalten {#canvas-specific-behavior}

Wenn ein Nachrichtenschritt in einem Canvas abgebrochen wird, verlässt die/der Nutzer:in den Canvas nicht. Stattdessen wird sie/er zum nächsten Schritt weitergeleitet. Abbrüche wirken sich nur auf die Sendezählung für diesen Nachrichtenschritt aus.

Bei der Diagnose von Canvas-Abbrüchen:

- Vergleichen Sie die eingetretenen Nutzer:innen beim Nachrichtenschritt mit den gesendeten Nutzer:innen desselben Schritts.
- Wenn nur ein Kanal abbricht, überprüfen Sie die kanalspezifische Liquid-Logik oder den Abo-Status für diesen Schritt.
- Wenn Abbrüche nach einer Listen- oder Katalogaktualisierung sprunghaft ansteigen, prüfen Sie, ob der Nachrichtenschritt vor Abschluss der Aktualisierung ausgeführt wurde.

### Mit Vorschau und Testsendungen validieren {#validate-with-preview-and-test-sends}

Zeigen Sie im Nachrichten-Editor eine Vorschau als Nutzer:in an, deren Profil einer/einem betroffenen Empfänger:in entspricht. Aktivieren Sie bei Testsendungen die Option **Attribute der Empfänger:innen mit den Attributen der aktuellen Vorschau-Nutzer:in überschreiben**, wenn Ihre Abbruchlogik von Profildaten abhängt.

Weitere Abbruchbeispiele finden Sie unter [Abbruchnachrichten abfragen](#query-for-abort-messages).

## Hinweise {#considerations}

Der Liquid-Nachrichten-Tag `abort_message()` verhindert das Senden von Nachrichten an Nutzer:innen, was bedeutet, dass die Nachricht nicht in Nutzerprofilen angezeigt wird und weder als Zustellung noch für das Frequency-Capping gezählt wird.