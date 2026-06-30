---
nav_title: Liquid
article_title: Liquid im WhatsApp-Template-Builder
description: "Dieser Referenzartikel behandelt Message Extras und bedingte Liquid-Logik im WhatsApp-Template-Builder."
alias: /whatsapp_template_builder_liquid/
page_type: reference
channel:
  - WhatsApp
page_order: 1
---

# Liquid im WhatsApp-Template-Builder {#liquid-in-the-whatsapp-template-builder}

> Sie können Liquid verwenden, um Templates im WhatsApp-Template-Builder zu personalisieren. Die Template-Struktur von Meta bringt jedoch Einschränkungen mit sich, die es in anderen Braze-Kanälen nicht gibt. Zwei Liquid-Muster erfordern besondere Beachtung: Message Extras und bedingte Messaging-Logik.

Für Message Extras und bedingte Messaging-Logik verlangt Meta, dass jede Variable in einem Template zum Sendezeitpunkt tatsächlich gerenderten Inhalt enthält. Variablen, die leere Strings liefern oder sich wie unsichtbare Metadaten statt sichtbarer Text verhalten, führen zu Sendefehlern. Bedingungen, die die statische Nachrichtenstruktur verändern, anstatt nur den Inhalt der Variable zu ändern, verursachen ebenfalls unerwartetes Verhalten.

{% alert note %}
Die in diesem Artikel beschriebenen Einschränkungen gelten nur für Template-Nachrichten (ausgehende Nachrichten, die ein von Meta genehmigtes Template verwenden). Die Einschränkungen gelten nicht für Antwortnachrichten (die innerhalb eines 24-Stunden-Messaging-Fensters gesendet werden, das von einer/einem Nutzer:in geöffnet wurde), oder für Message Extras, bedingte Logik und andere Liquid-Muster in anderen Braze-Kanälen.
{% endalert %}

## Übersicht {#overview}

| Muster | Unterstützt? | Hinweise |
| ----- | ----- | ----- |
| `message_extras` innerhalb einer Variable mit anderem sichtbaren Inhalt | ✅ Ja | Tag wird erfasst; sichtbarer Text erfüllt Metas Anforderung an Variableninhalte |
| `message_extras` als einziger Inhalt einer Variable | ❌ Nein | Wird zu leerem String aufgelöst; verursacht Sendefehler |
| Bedingtes Liquid innerhalb eines Variablen-Slots | ✅ Ja | Braze wertet vor dem Senden aus; Meta sieht nur den endgültig gerenderten Wert |
| Bedingtes Liquid außerhalb eines Variablen-Slots | ❌ Nein | Liquid-Tags werden als Klartext gerendert; Empfänger:in sieht die rohe Syntax |
| Template beginnt oder endet mit einem Variablen-Slot | ❌ Nein | Meta verlangt statischen Text am Anfang und Ende jedes Templates |
| Variablen-Slot, der zu einem leeren String aufgelöst wird | ❌ Nein | Meta verlangt zum Sendezeitpunkt nicht-leeren Inhalt in jeder Variable |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Kurzreferenz" }

## Message Extras {#message-extras}

Der [`message_extras`-Liquid-Tag]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras) ermöglicht es Ihnen, eine Nachricht zum Sendezeitpunkt mit Schlüssel-Wert-Metadaten zu versehen. Diese Daten werden nicht im Nachrichtentext gerendert. Stattdessen fließen die Daten an Connected-Content, Currents oder andere Datenerfassungsmechanismen für Zwecke wie Attribution, Wirkungsmessung und Event-Anreicherung.

{% raw %}
```liquid
{% message_extras :key campaign_id :value "spring_promo_2025" %}
```
{% endraw %}

### Warum eigenständige Message-Extras-Variablen fehlschlagen {#why-standalone-message-extras-variables-fail}

Im WhatsApp-Template-Builder werden Template-Variablen (wie {% raw %}`{{1}}`, `{{2}}`{% endraw %}) direkt auf Liquid-Ausdrücke abgebildet. Metas Validierung verlangt, dass jeder Variablen-Slot im genehmigten Template zum Sendezeitpunkt nicht-leeren Inhalt enthält; es muss etwas sein, das als sichtbarer Text für die/den Empfänger:in gerendert wird.

Da `message_extras` keine Ausgabe erzeugt, wird durch das alleinige Platzieren in einer Template-Variable ein leerer String für diesen Variablen-Slot übermittelt. Meta lehnt dies ab, sodass der Nachrichtenversand fehlschlägt.

{% details Falsche Verwendung für den WhatsApp-Template-Builder %}

{% raw %}
```
Template variable {{1}}: {% message_extras :key attribution_source :value "canvas_a" %}
```
{% endraw %}

Zum Sendezeitpunkt wird {% raw %}`{{1}}`{% endraw %} zu einem leeren String aufgelöst, was einen Sendefehler verursacht.

{% enddetails %}

### Korrekte Verwendung {#correct-usage}

Um einen `message_extras`-Tag korrekt einzubinden, betten Sie den Tag in eine bestehende Variable ein. Das bedeutet, den Tag innerhalb eines Liquid-Blocks zu platzieren, der sichtbare Ausgabe erzeugt – konkret innerhalb desselben Ausdrucks, der eine echte Template-Variable befüllt. Meta akzeptiert die Variable, weil sie Inhalt enthält, Braze erfasst die Metadaten, und die/der Empfänger:in sieht nur den gerenderten Text.

#### Beispiel {#example}

Angenommen, der Template-Text lautet:

{% raw %}
```
Hi {{1}}, your order has shipped.
```
{% endraw %}

Und die Variable {% raw %}`{{1}}`{% endraw %} ist zugeordnet zu:

{% raw %}
```
{{ ${first_name} | default: "there" }}
```
{% endraw %}

Um ein Message Extra anzuhängen, schreiben Sie den Variablenausdruck wie folgt um:

{% raw %}
```
{{ ${first_name} | default: "there" }}{% message_extras :key order_source :value "canvas_spring" %}
```
{% endraw %}

Zum Sendezeitpunkt wird {% raw %}`{{1}}`{% endraw %} zu etwas wie `"Alex"` aufgelöst – sichtbarer Inhalt, der Metas Anforderung erfüllt. Der `message_extras`-Tag wird ausgewertet und seine Daten werden erfasst, trägt aber nichts zum gerenderten String bei, den die/der Empfänger:in sieht.

### Wichtige Regeln {#key-rules}

- Weisen Sie `message_extras` niemals als einzigen Inhalt einer Template-Variable zu.
- Hängen Sie den Tag immer an eine Variable an, die zu sichtbarem Text aufgelöst wird.
- Sie können mehrere `message_extras`-Tags an denselben Variablenausdruck anhängen, ohne die gerenderte Ausgabe zu beeinflussen.
- Verwenden Sie dieses Muster im Text, in der Kopfzeile und in allen anderen Variablen-Slots.

## Bedingte Messaging-Logik {#conditional-messaging-logic}

In Messaging-Kanälen können Liquid-`if/elsif/else`-Blöcke bedingt ganze Textabschnitte ein- oder ausschließen. Braze rendert die vollständige Liquid-Ausgabe vor dem Senden, und das Ergebnis ist das, was die Logik erzeugt.

Meta-genehmigte WhatsApp-Templates haben jedoch eine feste Struktur. Meta unterscheidet Template-Inhalte in zwei Kategorien:

- **Statischer Text:** Fest codierte Strings, die bei der Template-Erstellung bestätigt werden und für jede/n Empfänger:in identisch bleiben.
- **Variablen-Slots:** Platzhalter-Positionen (wie {% raw %}`{{1}}`{% endraw %}), deren Inhalt zum Sendezeitpunkt befüllt wird.

### Warum bedingte Messaging-Logik außerhalb eines Variablen-Slots fehlschlägt {#why-conditional-messaging-logic-outside-a-variable-slot-fails}

Das Verhältnis von statischem Text zu Variablen-Slots in einem genehmigten Template ist fest, kann sich nicht pro Sendung ändern und hat feste Grenzen. Meta verlangt eine Mindestmenge an statischem Text für jeden Variablen-Slot im Template; Sie können kein Template haben, das überwiegend oder vollständig aus Variablen besteht. Das bedeutet, dass Sie kein bedingtes Liquid verwenden können, das Text hinzufügt oder entfernt, den Meta als bestätigten statischen Inhalt betrachtet.

Wenn Sie versuchen, einen `if/else`-Block zu verwenden, um einen Abschnitt statischen Texts bedingt ein- oder auszuschließen, wertet Meta die Logik nicht aus. Liquid-Tags außerhalb eines Variablen-Slots werden als Klartext-Ausgabe behandelt. Die/der Empfänger:in sieht die rohen Liquid-Syntax-Tags ({% raw %}`{% if %}`, `{% else %}`, `{% endif %}`{% endraw %}) und den gesamten Branch-Inhalt wörtlich in der Nachricht.

{% details Falsche Verwendung für den WhatsApp-Template-Builder %}

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}Hi {{1}}, we have an exclusive Gold member offer.{% else %}Hi {{1}}, we have a special offer for you.{% endif %}
```
{% endraw %}

Dies versucht, zwei verschiedene genehmigte Templates in einem zu kombinieren. Die bedingte Umschließung von statischem Text verhält sich nicht wie erwartet.

{% enddetails %}

### Korrekte Verwendung

Bedingungen sind innerhalb eines Variablen-Slots gültig und unterstützt, wo sie steuern, welcher Wert diese Variable befüllt. Meta sieht nur, dass {% raw %}`{{1}}`{% endraw %} mit Inhalt befüllt wurde; es prüft nicht, wie das Liquid im Inneren zu diesem Wert gelangt ist.

#### Beispiel

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}exclusive Gold member{% else %}valued customer{% endif %}
```
{% endraw %}

Als Wert für eine Template-Variable verwendet, erzeugt dies entweder `"exclusive Gold member"` oder `"valued customer"`. Beides sind nicht-leere Strings, die Metas Anforderung an Variableninhalte erfüllen.

Der Template-Text selbst bleibt strukturell unverändert:

{% raw %}
```
Hi {{1}}, we have a special offer for you.
```
{% endraw %}

### Bedingte Logik in einem Variablen-Slot platzieren {#place-conditional-logic-inside-a-variable-slot}

Es gibt zwei Möglichkeiten, bedingtes Liquid in einen Variablen-Slot im Template-Builder einzufügen:

1. **Einen Content-Block verwenden (unterstützt Prefill):** Erstellen Sie Ihre bedingte Logik in einem Content-Block und referenzieren Sie den Block dann aus der Variable. Dieser Ansatz unterstützt Prefill, d. h. die Variable kann im Template-Builder vor dem Senden einen Vorschauwert anzeigen.
2. **Einen Platzhalter verwenden und Liquid einfügen (kein Prefill):** Fügen Sie beim Erstellen des Templates einen Platzhalter wie {% raw %}`{{1}}`{% endraw %} hinzu und fügen Sie dann Ihren vollständigen Liquid-Ausdruck direkt in diesen Variablen-Slot ein. Dieser Ansatz unterstützt kein Prefill, funktioniert aber für jede Liquid-Logik.

### Andere Liquid-Komponenten, die von derselben Einschränkung betroffen sind {#other-liquid-components-affected-by-the-same-constraint}

Jeder Liquid-Tag, der keine sichtbare Ausgabe erzeugt, wird als Rohtext gerendert, wenn er außerhalb einer Variable platziert wird. Dazu gehören:

- **`catalog_items`:** Liquid, das Katalogdaten nachschlägt und referenziert, muss sich innerhalb eines Variablen-Slots befinden, sonst erscheinen die Tags wörtlich in der Nachricht.
- **`assign`:** Variablenzuweisungs-Tags (wie {% raw %}{% assign discount = "20%" %}{% endraw %}) erzeugen selbst keine Ausgabe. Wenn sie außerhalb eines Variablen-Slots verwendet werden, um einen Wert für die spätere Verwendung in der Nachricht festzulegen, wird der `assign`-Tag wörtlich gerendert. Fügen Sie jede `assign`-Logik am Anfang des Liquid-Ausdrucks innerhalb des Variablen-Slots ein, in dem die Ausgabe benötigt wird.
- **Content Blocks, die nur Liquid-Tags enthalten:** Wenn ein Content-Block Liquid-Logik enthält, aber keinen sichtbaren Text erzeugt (z. B. nur `assign`- oder `message_extras`-Tags verwendet), erscheint beim Referenzieren außerhalb eines Variablen-Slots der rohe Block-Inhalt in der Nachricht. Content Blocks, die keine sichtbare Ausgabe erzeugen, müssen innerhalb eines Variablen-Slots zusammen mit Inhalt eingebettet werden, der gerendert wird.

### Zusätzliche strukturelle Einschränkungen {#additional-structural-constraints}

Meta verlangt, dass Templates:

- **Mit statischem Text beginnen.** Templates dürfen nicht mit einem Variablen-Slot beginnen (wie {% raw %}`{{1}} is ready for you`{% endraw %}).
- **Mit statischem Text enden.** Templates dürfen nicht mit einem Variablen-Slot enden.

Diese Einschränkungen bestehen unabhängig davon, ob Liquid verwendet wird. Sie gelten für die genehmigte Template-Struktur selbst.

### Wichtige Regeln

- Verwenden Sie Bedingungen frei innerhalb von Variablen-Slot-Ausdrücken, um zu steuern, welcher Wert gerendert wird.
- Verwenden Sie keine Bedingungen, um statischen Text hinzuzufügen, zu entfernen oder auszutauschen (die Teile der Nachricht, die keine Variablen-Slots sind).
- Stellen Sie sicher, dass jeder bedingte Branch innerhalb einer Variable einen nicht-leeren String erzeugt (siehe [Message Extras](#message-extras) für die Erklärung, warum leere Strings Fehler verursachen).
- Das Template muss mit statischem Text beginnen und enden, wie es bei Meta eingereicht wurde.