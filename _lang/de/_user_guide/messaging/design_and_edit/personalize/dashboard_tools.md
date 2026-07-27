---
nav_title: Dashboard-Tools
article_title: Dashboard-Tools für Personalisierung
page_order: 0
description: "Dieser Referenzartikel beschreibt die Funktion „Personalisierung hinzufügen“ in den Braze-Nachrichten- und Landing-Page-Editoren, einschließlich vorformatiertem Liquid, Standardwerten und Liquid-Editor-Verbesserungen wie Farbkennzeichnungen und prädiktiven Vorschlägen."
---

# Dashboard-Tools für Personalisierung {#dashboard-tools-for-personalization}

> Verwenden Sie die Braze-Dashboard-Tools, um Liquid-Personalisierung einzufügen, ohne jeden Tag manuell schreiben zu müssen. Der Ablauf **Personalisierung hinzufügen** erstellt die richtige Syntax für Sie, und der Liquid-Editor hilft Ihnen, Templates schnell zu lesen und zu erweitern.

Informationen zu Liquid-Syntaxregeln, unterstützten Tags und erweiterten Mustern finden Sie unter [Liquid verwenden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) und [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

## Personalisierung in Composern und Einstellungen hinzufügen {#add-personalization-in-composers-and-settings}

Das Tool **Personalisierung hinzufügen** erscheint neben Template-Textfeldern im gesamten Dashboard, darunter:

- **Campaign- und Canvas-Schritte** für Kanäle, die Liquid im Textkörper oder in Headern unterstützen (zum Beispiel E-Mail, Push, SMS, In-App-Nachrichten, Content Cards und Webhooks).
- **Drag-and-Drop-Editoren**, wo sich die Steuerung häufig in der Block- oder Editor-Symbolleiste befindet. Beispielsweise können Sie in Drag-and-Drop-In-App-Nachrichten **Personalisierung hinzufügen** auswählen, einen Personalisierungstyp wählen und dann das generierte Snippet in Ihren Inhalt einfügen, bevor Sie unter **Vorschau & Test** eine Vorschau anzeigen. Weitere kanalspezifische Hinweise finden Sie im Drag-and-Drop- oder Composer-Artikel Ihres Kanals (z. B. [Stileinstellungen für In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#add-liquid) oder [E-Mail mit Drag-and-Drop erstellen]({{site.baseurl}}/user_guide/channels/email/drag_and_drop)).
- **Spezialisierte Composer**, die eine Personalisierungsauswahl bereitstellen – zum Beispiel verwenden [Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations) Optionen für den **Personalisierungstyp** wie **Artikelempfehlung** im selben Fensterformat.
- **Landing-Pages**, auf denen Sie Liquid-Personalisierung im Drag-and-Drop-Editor oder in Seiten- und Blockeinstellungen hinzufügen können. Weitere Informationen finden Sie unter [Landing-Pages personalisieren]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages).

## Vorformatierte Variablen und Standardwerte einfügen {#insert-pre-formatted-variables-and-defaults}

Das Tool **Personalisierung hinzufügen** hilft Ihnen, Liquid mit optionalen Standardwerten einzufügen, damit leere Profildaten Ihren Text nicht beeinträchtigen.

![Das Modal „Personalisierung hinzufügen“, das nach Auswahl von „Personalisierung einfügen“ erscheint. Das Modal enthält Felder für den Personalisierungstyp, das Attribut, einen optionalen Standardwert und zeigt eine Vorschau der Liquid-Syntax an.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

Das Tool fügt Liquid mit Ihrem angegebenen Standardwert an der Stelle ein, an der sich Ihr Cursor befand. Die Einfügestelle wird auch durch das Vorschaufeld angegeben, das den Text davor und danach anzeigt. Wenn ein Textblock markiert ist, wird der markierte Text ersetzt.

![Ein GIF des Modals „Personalisierung hinzufügen“, das zeigt, wie der/die Nutzer:in „fellow traveler“ als Standardwert eingibt und das Modal den markierten Text „name“ im Composer durch das Liquid-Snippet ersetzt.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

Sie können in vielen Composern auch {% raw %}`{{`{% endraw %} eingeben, um die Autovervollständigung zu nutzen, oder Tags von anderer Stelle einfügen. Weitere Informationen finden Sie unter [Tags einfügen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#inserting-tags) in **Liquid verwenden**.

### Variablen zuweisen {#assign-variables}

{% raw %}
Einige Operationen in Liquid erfordern, dass Sie den Wert, den Sie bearbeiten möchten, als Variable speichern. Dies ist häufig der Fall, wenn Ihre Liquid-Anweisung mehrere Attribute, Event-Eigenschaften oder Filter enthält.

Nehmen wir zum Beispiel an, Sie möchten zwei angepasste Daten-Ganzzahlen addieren.

#### Fehlerhaftes Liquid-Beispiel {#incorrect-liquid-example}

Sie können Folgendes nicht verwenden:

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

Dieses Liquid funktioniert nicht, da Sie nicht mehrere Attribute in einer Zeile referenzieren können. Sie müssen mindestens einem dieser Werte eine Variable zuweisen, bevor die mathematischen Funktionen ausgeführt werden. Das Addieren zweier angepasster Attribute erfordert zwei Zeilen Liquid: eine, um das angepasste Attribut einer Variablen zuzuweisen, und eine, um die Addition durchzuführen.

#### Korrektes Liquid-Beispiel {#correct-liquid-example}

Sie können Folgendes verwenden:

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### Tutorial: Variablen zur Berechnung eines Guthabens verwenden {#tutorial-using-variables-to-calculate-a-balance}

Berechnen wir das aktuelle Guthaben eines/einer Nutzer:in, indem wir das Geschenkkarten-Guthaben und das Rewards-Guthaben addieren:

Verwenden Sie zunächst den `assign`-Tag, um das angepasste Attribut `current_rewards_balance` durch den Begriff „balance“ zu ersetzen. Das bedeutet, dass Sie jetzt eine Variable namens `balance` haben, die Sie bearbeiten können.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

Als Nächstes verwenden wir den `plus`-Filter, um das Geschenkkarten-Guthaben jedes/jeder Nutzer:in mit dem Rewards-Guthaben zu kombinieren, das durch `{{balance}}` dargestellt wird.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
Weisen Sie in jeder Nachricht dieselben Variablen zu? Anstatt den `assign`-Tag immer wieder auszuschreiben, können Sie diesen Tag als Content-Block speichern und ihn stattdessen an den Anfang Ihrer Nachricht setzen.<br><br>

1. [Erstellen Sie einen Content-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block).
2. Geben Sie Ihrem Content-Block einen Namen (ohne Leerzeichen oder Sonderzeichen).
3. Wählen Sie **Bearbeiten** am unteren Rand der Seite.
4. Geben Sie Ihre `assign`-Tags ein.

Solange sich der Content-Block am Anfang Ihrer Nachricht befindet, bezieht sich die Variable jedes Mal, wenn sie als Objekt in Ihre Nachricht eingefügt wird, auf Ihr gewähltes angepasstes Attribut!
{% endalert %}

## Verbesserungen im Liquid-Editor {#liquid-editor-enhancements}

Diese Dashboard-Funktionen erleichtern die Arbeit mit Liquid beim Verfassen von Nachrichten.

### Farbliche Kennzeichnungen {#color-labels}

Jedes Liquid-Element entspricht einer Farbe, sodass Sie Ihren Liquid-Code im Liquid-Editor auf einen Blick unterscheiden können.

![Diagramm verschiedener farblicher Kennzeichnungen für unterschiedliche Liquid-Elemente.]({% image_buster /assets/img/liquid_color_code.png %})

### Prädiktives Liquid {#predictive-liquid}

Sie können beim Erstellen Ihrer personalisierten Nachrichten auch prädiktives Liquid für angepasste Attribute, Attributnamen und mehr verwenden.

![Braze schlägt verschiedene Liquid-Attribute vor, während Text in ein Feld eingegeben wird.]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## Nächste Schritte {#next-steps}

- [Liquid verwenden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) — Syntax, `assign`, Bedingungen und Filter in Braze
- [Standardwerte festlegen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) — Standardwerte in Liquid über das Modal hinaus
- [Filter]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters) — Datumsangaben, Berechnungen, Strings und mehr formatieren