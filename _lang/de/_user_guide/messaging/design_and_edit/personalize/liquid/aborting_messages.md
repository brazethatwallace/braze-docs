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

## Testversand mit `abort_message()` {#test-sends-with-abort_message}

`abort_message()` stoppt den Versand für Nutzer:innen, die Ihre Bedingung nicht erfüllen. Die Nachricht wird nicht in ihrem Profil angezeigt und zählt weder als Zustellung noch für das Frequency-Capping.

Wenn Testversand nie ankommt, zeigen Sie eine Vorschau als Nutzer:in an, die die Abbruchbedingung erfüllt, und aktivieren Sie dann unter **Test Send** die Option **Override recipients' attributes with current preview user's attributes** (oder fügen Sie ein Content-Test-Group-Mitglied hinzu, das die Bedingungen erfüllt).

## Nachricht abbrechen, wenn „Number Games Attended“ = 0 {#abort-message-if-number-games-attended-0}

Angenommen, Sie möchten keine Nachricht an Kund:innen senden, die noch kein Spiel besucht haben:

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

## Nur englischsprachige Kund:innen ansprechen {#message-english-speaking-customers-only}

Sie können ausschließlich englischsprachige Kund:innen ansprechen, indem Sie eine „if“-Anweisung erstellen, die zutrifft, wenn die Sprache einer Kundin oder eines Kunden Englisch ist, und eine „else“-Anweisung, die die Nachricht für alle abbricht, die kein Englisch sprechen oder keine Sprache in ihrem Profil hinterlegt haben.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Standardmäßig protokolliert Braze eine allgemeine Fehlermeldung in Ihrem Nachrichtenaktivitätsprotokoll:

```text
{% abort_message %} called
```

Sie können die Abbruchnachricht auch dazu veranlassen, etwas in Ihrem Nachrichtenaktivitätsprotokoll zu protokollieren, indem Sie einen String in die Klammern einfügen:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Fehlermeldungsprotokoll in der Entwicklungskonsole mit einer Abbruchnachricht „language was nil“.]({% image_buster /assets/img_archive/developer_console.png %})

## Abfrage von Abbruchnachrichten {#query-for-abort-messages}

Sie können den [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) oder Ihr eigenes Data Warehouse verwenden, sofern es mit Braze verbunden ist, um nach bestimmten Abbruchnachrichten zu suchen, die ausgelöst werden, wenn Liquid-Logik den Abbruch einer Nachricht verursacht.

## Wann die Abbruchlogik ausgewertet wird {#when-abort-logic-is-evaluated}

Der Zeitpunkt der Auswertung der Abbruchlogik hängt vom Nachrichtenkanal ab.

### Push, E-Mail, SMS, Webhooks und Content Cards {#push-email-sms-webhooks-and-content-cards}

Die Abbruchlogik wird zum Sendezeitpunkt ausgewertet, wenn Braze die Nachricht für die Zustellung verarbeitet.

### In-App Messages {#in-app-messages}

Die Abbruchlogik wird bei [vorlagenbasierten In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated) nur zu dem Zeitpunkt ausgewertet, an dem die In-App-Nachricht ausgelöst wird (z. B. wenn Nutzer:innen das Trigger-Event ausführen oder eine Sitzung starten), nicht wenn die Nachricht ursprünglich an das Gerät gesendet wird. In-App-Nachrichten werden beim Sitzungsstart an das SDK übermittelt und lokal zwischengespeichert; das Liquid – einschließlich aller `abort_message()`-Aufrufe – wird ausgeführt, wenn die Trigger-Bedingung erfüllt ist.

## Fehlerbehebung bei hohen Abbruchraten {#troubleshooting-high-abort-rates}

Wenn eine Campaign oder ein Canvas-Schritt viele eingetretene Nutzer:innen zeigt, aber nur wenige Sends oder Zustellungen niedriger als erwartet ausfallen, ist die Abbruchlogik eine häufige Ursache – insbesondere wenn Liquid Attribute, Katalogdaten oder Listenwerte erfordert, die zum Zeitpunkt der Auswertung fehlen.

### Message Activity Log überprüfen {#check-the-message-activity-log}

1. Öffnen Sie im Braze-Dashboard das [Message Activity Log]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) für die Campaign oder den Canvas-Nachrichtenschritt.
2. Filtern Sie nach abbruchbezogenen Einträgen. Standardmäßig protokolliert Braze den Aufruf von {% raw %}`{% abort_message %}`{% endraw %}. Wenn Sie einen Begründungstext an `abort_message()` übergeben haben, wird stattdessen dieser Text angezeigt.
3. Prüfen Sie, ob die Abbrüche auf einen Kanal beschränkt sind (zum Beispiel nur E-Mail) oder kanalübergreifend im selben Canvas auftreten.

### Attribute und Liquid zum Sendezeitpunkt überprüfen {#verify-attributes-and-liquid-at-send-time}

Bei Push, E-Mail, SMS, Webhooks und Content Cards wird die Abbruchlogik ausgeführt, wenn Braze die Nachricht für die Zustellung verarbeitet – nicht wenn die Nutzer:innen einen Canvas betreten haben oder ein Trigger-Event zuvor ausgelöst wurde.

- Stellen Sie sicher, dass die erforderlichen [angepassten Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), Event-Eigenschaften oder [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs)-Felder für die Nutzer:innen gesetzt sind, bevor der Nachrichtenschritt ausgeführt wird.
- Fügen Sie explizite nil- oder Leerprüfungen hinzu, bevor Sie `abort_message()` aufrufen. Ein `else`-Zweig, der abbricht, wenn ein Wert fehlt, stoppt den Versand für alle Nutzer:innen ohne diese Daten.
- Wenn die Personalisierung von einer Liste, einem Segment oder einer Connected-Content-Antwort abhängt, stellen Sie sicher, dass die Daten verfügbar sind, wenn der Nachrichtenschritt ausgeführt wird. Nutzer:innen können einen Canvas betreten, bevor die Listenzugehörigkeit oder nachgelagerte Daten bereitstehen.

### Canvas-spezifisches Verhalten {#canvas-specific-behavior}

Wenn ein Nachrichtenschritt in einem Canvas abgebrochen wird, verlassen die Nutzer:innen den Canvas nicht. Stattdessen fahren sie mit dem nächsten Schritt fort. Abbrüche wirken sich nur auf die Sendeanzahl dieses Nachrichtenschritts aus.

Bei der Diagnose von Canvas-Abbrüchen:

- Vergleichen Sie die eingetretenen Nutzer:innen im Nachrichtenschritt mit den gesendeten Nutzer:innen im selben Schritt.
- Wenn nur ein Kanal abbricht, überprüfen Sie das kanalspezifische Liquid oder den Abo-Status für diesen Schritt.
- Wenn Abbrüche nach einem Listen- oder Katalog-Update sprunghaft ansteigen, prüfen Sie, ob der Nachrichtenschritt vor Abschluss des Updates ausgeführt wurde.

### Mit Vorschau und Testsendungen validieren {#validate-with-preview-and-test-sends}

Nutzen Sie die Vorschau im Nachrichten-Editor als Nutzer:in, deren Profil einem betroffenen/einer betroffenen Empfänger:in entspricht. Aktivieren Sie bei Testsendungen die Option **Override recipients' attributes with current preview user's attributes**, wenn Ihre Abbruchlogik von Profildaten abhängt.

Weitere Beispiele für Abbrüche finden Sie unter [Abbruchnachrichten abfragen](#query-for-abort-messages).

## Überlegungen {#considerations}

Der Liquid-Nachrichten-Tag `abort_message()` verhindert, dass Nachrichten an Nutzer:innen gesendet werden. Das bedeutet, dass die Nachricht nicht in Nutzerprofilen angezeigt wird und weder bei Zustellungen noch beim Frequency-Capping berücksichtigt wird.