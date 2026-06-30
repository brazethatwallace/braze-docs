---
nav_title: Message-Extras-Tag
article_title: Message-Extras-Tag
page_order: 1
description: "In diesem Artikel erfahren Sie, wie Sie den message_extras-Liquid-Tag verwenden und die Syntax überprüfen."
alias: "/message_extras_tag/"
---

# Message-Extras-Liquid-Tag {#message-extras-liquid-tag}

> Verwenden Sie den `message_extras`-Liquid-Tag, um Ihre Sendeereignisse mit dynamischen Daten aus Connected-Content, Katalogen, angepassten Attributen (wie Sprache, Land), Canvas-Eingangs-Eigenschaften oder anderen Datenquellen zu annotieren.

Der `message_extras`-Liquid-Tag fügt dem entsprechenden Sendeereignis in Currents und der Snowflake-Datenfreigabe Schlüssel-Wert-Paare hinzu.

Um dynamische oder zusätzliche Daten an Ihr Currents- oder Snowflake-Datenfreigabe-Sendeereignis zurückzusenden, fügen Sie den entsprechenden Liquid-Tag in Ihren Nachrichtentext ein.

Hier ist ein Beispiel für das Standard-Liquid-Tag-Format für `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Sie können diese Tags nach Bedarf für Ihre Schlüssel-Wert-Paare im Nachrichtentext hinzufügen. Die Gesamtlänge aller Schlüssel und Werte sollte jedoch 1.000 Bytes (1&nbsp;KB) nicht überschreiten. In Currents und der Snowflake-Datenfreigabe sehen Sie ein neues Ereignisfeld namens `message_extras` für Ihre Sendeereignisse. Dieses generiert einen JSON-serialisierten String in einem Feld.

## Wie Message-Extras-Daten über Currents gesendet werden {#how-message-extras-data-is-sent-using-currents}

**Message Extras** sind Schlüssel-Wert-Paare, die zum Sendezeitpunkt angehängt werden. Die Konfiguration hängt vom Kanal ab. Bei E-Mails werden sie über Header hinzugefügt. Bei iOS-Push werden sie in die Push-Payload aufgenommen. Alle unterstützten Sendeereignisse zeigen dasselbe `message_extras`-Feld in Currents (und Snowflake) an, sobald die Nachricht gesendet wurde.

## Unterstützte Kanäle {#supported-channels}

Der `message_extras`-Tag wird für alle Nachrichtentypen mit einem Sendeereignis sowie für Impressionsereignisse von In-App-Nachrichten unterstützt. Die Verwendung von `message_extras` mit In-App-Nachrichten erfordert bestimmte [Mindest-SDK-Versionen](#iam-sdk).

## So verwenden Sie den `message_extras`-Tag {#how-to-use-the-message_extras-tag}

1. Geben Sie im Nachrichtentext für den Kanal den `message_extras`-Liquid-Tag ein. Alternativ können Sie das Modal **Personalisierung hinzufügen** verwenden und **Message Extras** als Personalisierungstyp auswählen.

![Das Modal „Personalisierung hinzufügen“ mit „Message Extras“ als ausgewähltem Personalisierungstyp.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Geben Sie das [Schlüssel-Wert-Paar]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) für jeden `message_extras`-Tag ein.

![Ein Beispiel für Schlüssel-Wert-Paare für den Message-Extras-Tag. Das Titelfeld lautet „Your New Favorites“. Die Nachricht enthält Schlüssel-Wert-Paare für den Message-Extras-Tag und den folgenden Satz: „We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites“]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Nachdem Ihre Kampagne oder Ihr Canvas gesendet wurde, hängt Braze die dynamischen Daten zum Sendezeitpunkt über die Currents- oder Snowflake-Datenfreigabe-Sendeereignisse an das `message_extras`-Feld an.

## Syntax überprüfen {#checking-syntax}

Jede andere Eingabe, die nicht dem oben beschriebenen Tag-Standard entspricht, wird möglicherweise nicht an Currents oder Snowflake weitergeleitet. Überprüfen Sie, ob Ihre Syntax oder Formatierung keine der folgenden Probleme enthält:

- Nicht vorhandene, leere oder falsch eingegebene Trennzeichen
- Doppelte Schlüssel (Braze sendet standardmäßig das zuerst gefundene Schlüssel-Wert-Paar)
- Zusätzlicher Text, bevor Schlüssel oder Werte definiert werden
- Schlüssel und Werte in falscher Reihenfolge
  - {% raw %}Zum Beispiel: `{% message_extras :value 123 :key test %}`{% endraw %}

## Aktionscode-Informationen an Currents senden {#sending-promotion-code-information-to-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## Hinweise {#considerations}

- Schlüssel-Wert-Paare, die 1.000 Bytes (1&nbsp;KB) überschreiten, werden abgeschnitten.
- Leerzeichen zählen zur Zeichenanzahl. Beachten Sie, dass Braze führende und abschließende Leerzeichen entfernt.
- Die resultierende JSON-Ausgabe enthält nur String-Werte.
- Sie können Liquid-Variablen als Schlüssel oder Wert verwenden, aber Sie können keine zusätzlichen Liquid-Tags innerhalb von `message_extras` verschachteln.
  - Zum Beispiel könnten Sie folgendes Liquid verwenden: {% raw %}`{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}`{% endraw %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Wie kann ich das message_extras-Feld in den Sendeereignissen mit meinen Engagement-Ereignissen wie Öffnungen und Klicks verknüpfen? {#how-can-i-associate-the-message_extras-field-in-the-send-events-to-my-engagement-events-like-opens-and-clicks}

Eine `dispatch_id` wird generiert und in Ihren Sendeereignissen bereitgestellt. Diese kann als eindeutiger Bezeichner verwendet werden, um sie mit bestimmten Klick-, Öffnungs- oder Zustellungsereignissen zu verknüpfen. Sie können dieses Feld in Currents oder Snowflake abfragen. Weitere Informationen finden Sie unter [Dispatch-ID-Verhalten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

#### Kann ich message_extras mit In-App-Nachrichten verwenden? {#iam-sdk}

Ja, Sie können `message_extras` in Ihren In-App-Nachrichten verwenden, sofern die Geräte Ihrer Nutzer:innen die folgenden Mindest-SDK-Versionen erfüllen:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}