---
nav_title: FAQ
article_title: Häufig gestellte Fragen
page_order: 12
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Liquid."
toc_headers: h2
---

# Häufig gestellte Fragen {#frequently-asked-questions}

> Auf dieser Seite finden Sie Antworten auf häufig gestellte Fragen zu Liquid.

{% alert note %}
Braze unterstützt derzeit nicht 100 % von Shopifys Liquid, sondern nur bestimmte Teile, die wir in unserer Dokumentation beschrieben haben. Testen Sie alle Nachrichten mit Liquid vor dem Versand, um das Risiko von Fehlern oder die Verwendung von nicht unterstütztem Liquid zu minimieren.
{% endalert %}

## Über Liquid in Braze {#about-liquid-in-braze}

### Wie verwende ich Liquid-Snippets in Braze? {#how-do-i-use-liquid-snippets-in-braze}

In vielen Fällen können Sie Liquid-Snippets einbinden, indem Sie zu Ihren Campaigns oder Canvases navigieren und Liquid im Personalisierungs-Modal in Bereichen wie dem E-Mail-Nachrichtentext oder in Ihren Segmenten einfügen.

#### Wo kann ich mehr erfahren? {#where-can-i-learn-more}

Weitere Informationen zu Liquid finden Sie in unserem geführten Braze-Lernpfad [Dynamische Personalisierung mit Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid). Sie können auch die [Liquid-Anwendungsbeispiel-Bibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) als Inspiration und für eine Reihe von Personalisierungsbeispielen mit Liquid nutzen.

### Was ist der Unterschied zwischen der Verwendung von Liquid und Connected-Content für die Personalisierung? {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

Braze Connected-Content ist ein Beispiel für einen Liquid-Tag. Es wird ebenfalls für die Personalisierung verwendet, aber die Daten stammen von einem externen Endpunkt und nicht aus gespeicherten Daten innerhalb von Braze. Besuchen Sie unseren speziellen Abschnitt [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), um mehr darüber zu erfahren, wie Sie die Personalisierung Ihrer Nachrichten erweitern können.

### Was ist Liquid-Templating? {#what-is-liquid-templating}

Dies ist die häufigste Art, Liquid in Braze zu verwenden. Liquid-Templating zieht Daten aus dem Profil einer Nutzerin oder eines Nutzers in eine Nachricht. Diese Daten können vom Vornamen bis hin zu angepassten Events aus einer getriggerten Nachricht reichen.

Eine vollständige Liste der unterstützten Liquid-Tags finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

### Verbraucht die Verwendung von Liquid Datenpunkte? {#does-using-liquid-log-data-points}

Nein.

## Personalisierungs-Tags und Datenquellen {#personalization-tags-and-data-sources}

### Wie kann ich Liquid verwenden, um eine personalisierte Begrüßung zu senden? {#how-can-i-use-liquid-to-send-a-personalized-greeting}

Für eine personalisierte Begrüßung mit dem Vornamen einer Nutzerin oder eines Nutzers können Sie die Standard-Nutzerprofilattribute wie {% raw %}`{{${first_name}}}` und `{{${last_name}}}`{% endraw %} verwenden.

Sie können auch eine Liquid-{% raw %}`{% if X %}`{% endraw %}-Anweisung für bedingtes Rendering verwenden, basierend auf beliebigen Kriterien wie dem Wochentag oder angepassten Attributen. Weitere Informationen zu den unterstützten Liquid-Operatoren, die in bedingten Anweisungen verwendet werden können, finden Sie unter [Operatoren]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators).

### Wie kann ich eine Nachricht basierend auf dem Standort einer Nutzerin oder eines Nutzers personalisieren? {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
Es gibt ein Standardattribut für den Standort der Nutzerin oder des Nutzers: `{{${most_recent_location}}}`.
{% endraw %}

{% raw %}
### Was ist der Unterschied zwischen {{campaign.${name}}} und {{campaign.${message_name}}}? {#whats-the-difference-between-campaignname-and-campaignmessage_name}

Sowohl `{{campaign.${name}}}` als auch `{{campaign.${message_name}}}` sind unterstützte Liquid-Personalisierungs-Tags. Beide Tags referenzieren Campaign-Attribute. `{{campaign.${name}}}` bezeichnet den Namen Ihrer Campaign, und `{{campaign.${message_name}}}` ist der Name Ihrer Nachrichtenvariante.
{% endraw %}

Informationen zur Verwendung in URLs und Query-Strings (z. B. wenn ein Name `%` oder Leerzeichen enthält) finden Sie unter [Campaign-Namen in URLs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

### Wie verwende ich Liquid mit verschachtelten Objekten? {#how-do-i-use-liquid-with-nested-objects}

Braze verfügt über ein integriertes Feature, das Liquid-Code für Segmente generiert, der in einer Nachricht verwendet werden kann. Konkret können Sie ein Segment erstellen, das mehrere Kriterien in einem Objekt abgleicht.

Weitere Informationen finden Sie unter [Multi-Kriterien-Segmentierung]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#multi-criteria-segmentation).

### Wie verwende ich Event-Eigenschaften, um eine Nachricht zu personalisieren, die ein Event triggert? {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
Sie können auf Eigenschaften von API-getriggerten Events mit dem `api_triggered_property`-Tag zugreifen: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Unterstützt Braze ein Array von Arrays in Liquid? {#does-braze-support-an-array-of-arrays-in-liquid}

Liquid unterstützt nativ keine Arrays von Arrays. Speichern Sie Werte als Array von kommaseparierten Strings und verwenden Sie den `split`-Filter, um sie bei Bedarf zu parsen.

## Variablen und Syntax {#variables-and-syntax}

### Wie weise ich Variablen mit Liquid zu? {#how-do-i-assign-variables-with-liquid}

Sie können Variablen erstellen und zuweisen, indem Sie den `assign`-Tag verwenden. Dieser erstellt eine Variable im Nachrichten-Editor, die auch in Ihrer gesamten Nachricht referenziert werden kann.

### Wann sollte ich `assign` und wann `capture` verwenden? {#when-should-i-use-assign-versus-capture}

Sowohl `assign` als auch `capture` erstellen Liquid-Variablen, dienen aber unterschiedlichen Zwecken:

- `assign` ist für einfache Variablen gedacht, die einen einzelnen Wert speichern, z. B. einen booleschen Wert, eine Zahl oder einen einfachen String. Sie können auch einen einzelnen Filter in derselben Zeile anwenden.
- `capture` ist zum Speichern eines Textblocks gedacht, der mehrere Variablen, Strings oder komplexe Ausdrücke enthalten kann.

Verwenden Sie `capture`, wenn der Wert für eine einzelne `assign`-Anweisung zu komplex ist, z. B. bei URLs, die andere Liquid-Variablen oder angepasste Attribute als Parameter verwenden. `capture` wird auch bevorzugt, wenn Liquid-Variablen im Body von Connected-Content-Aufrufen implementiert werden.

#### Beispiele {#examples}

{% raw %}
```liquid
{% comment %}Use assign for custom attributes{% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %}Use assign for a simple variable{% endcomment %}
{% assign discount_label = "20% off" %}
Hello {{ customer.first_name | default: "there" }}, enjoy {{ discount_label }} on your next order!

{% comment %}Use capture for complex strings{% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}

{% comment %}Use capture to create conditional content{% endcomment %}
{% capture promo_block %}
{% if customer.vip == true %}
As a VIP member, you get free shipping.
{% else %}
Join our VIP program to unlock free shipping.
{% endif %}
{% endcapture %}
```
{% endraw %}

### Werden Liquid-Variablen zwischen Betreffzeile und Nachrichtentext übernommen? {#do-liquid-variables-carry-between-subject-line-and-body}

Nein. Braze rendert jede Nachrichtenkomponente separat (z. B. Betreffzeile, HTML-Body, Preheader und Push-Titel). Zuweisungen oder Captures, die Sie in einem Feld vornehmen, sind in einem anderen nicht verfügbar. Wiederholen Sie den Liquid- oder Connected-Content-Aufruf in jedem Feld, das den Wert benötigt.

### Was ist For-Loop-Logik, und wie kann ich sie verwenden? {#what-is-for-loop-logic-and-how-can-i-use-it}

For-Loops werden auch als [Iterations-Tags](https://shopify.github.io/liquid/tags/iteration/) bezeichnet. Die Verwendung von For-Loop-Logik in Ihren Liquid-Snippets ermöglicht es Ihnen, Liquid-Blöcke zu durchlaufen, bis eine Bedingung erfüllt ist.

In Braze kann dies verwendet werden, um Elemente in einem Array-Attribut oder eine Liste von Werten und Objekten zu prüfen, die von einem [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs), einer [Auswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) oder einem [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)-Aufruf zurückgegeben werden. Konkret können Sie For-Loop-Logik als Teil Ihres Messagings verwenden, um zu prüfen, ob ein Produkt auf Lager ist oder ob ein Produkt eine Mindestbewertung hat.

Nehmen wir zum Beispiel an, Sie haben einen Katalog namens „Games“ mit einer Auswahl namens „cheap_games“. Um die Titel der Spiele in „cheap_games“ abzurufen, können Sie dieses Liquid-Snippet verwenden:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Sobald die festgelegten Bedingungen erfüllt sind, kann Ihre Nachricht fortfahren. Die Verwendung dieser Logik ist eine hilfreiche Möglichkeit, Zeit zu sparen, anstatt Liquid-Blöcke für verschiedene Bedingungen zu wiederholen.

### Was ist Abbruchlogik, und wie kann ich sie verwenden? {#what-is-abort-logic-and-how-can-i-use-it}

Abbruchlogik ermöglicht es Ihnen, den Versand einer Nachricht zu stoppen, wenn die Bedingungen erfüllt sind. Dies ist besonders hilfreich, um zu verhindern, dass unvollständige Nachrichten an Ihre Nutzer:innen gesendet werden. Beispiele für Abbruchlogik in Ihren Marketingkampagnen finden Sie unter [Nachrichten abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

### Kann ich Liquid innerhalb des `abort_message`-Tags verwenden? {#can-i-use-liquid-inside-the-abort_message-tag}

Nein. Der {% raw %}`{% abort_message %}`{% endraw %}-Tag akzeptiert einen statischen String in Anführungszeichen, keine Liquid-Personalisierung. Verwenden Sie andere Liquid-Logik vor dem Tag, wenn Sie ein bedingtes Abbruchverhalten benötigen.

## Canvas, Kataloge und Trigger-Eigenschaften {#canvas-catalogs-and-trigger-properties}

### Warum schlägt mein API-getriggertes Liquid in Braze fehl? {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
Eine häufige Ursache ist ein zusätzliches Paar geschweifter Klammern. Zum Beispiel ist `{{{api_trigger_properties.${attribute_key}}}}` keine gültige Braze-Personalisierungssyntax. Verwenden Sie genau zwei öffnende und zwei schließende Klammern: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Gibt es Größenbeschränkungen für Canvas-Kontexteigenschaften? {#are-there-size-limits-for-canvas-context-properties}

Braze erzwingt kein festes Limit für [Canvas-Kontexteigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), aber halten Sie Payloads unter ca. 1 KB (~1.000 Zeichen). Größere Objekte können den Speicherverbrauch erhöhen und das Nachrichten-Rendering bei Massenversendungen verzögern.

### Warum erhalte ich einen Liquid-Fehler bei der Vorschau bestimmter Datentypen im Dashboard? {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

Einige Typen von [Canvas-Kontexteigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) erfordern eine Typumwandlung in Liquid, bevor Sie sie in Vergleichen oder Berechnungen verwenden können. Wenn Sie beispielsweise numerisches Verhalten benötigen:

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### Warum gibt mein Katalog-Liquid-Snippet eine Abbruchnachricht zurück? {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

Wenn ein Katalog-Liquid-Snippet beim Versand abbricht, erstellen Sie das Snippet über das Personalisierungsmenü neu, indem Sie einzelne Katalogartikel auswählen, anstatt eine Massen- oder vollständig dynamische Auswahl zu verwenden. Weitere Informationen finden Sie unter [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs) und [Auswahlen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Content Blocks und der Nachrichten-Editor {#content-blocks-and-the-message-composer}

### Warum gibt es zusätzliche Abstände in Nachrichten, die Content Blocks verwenden? {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Wenn Sie zusätzliche Abstände in gesendeten Nachrichten bemerken, die Content Blocks mit Liquid verwenden, haben Sie möglicherweise unnötige Absatz- oder Zeilenumbrüche innerhalb Ihrer bedingten Anweisungen. Schreiben Sie Ihre bedingten Anweisungen in einer einzigen Zeile statt über mehrere Zeilen.

#### Beispiel {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}

### Warum fehlt mein Content Block unter **Row** im Drag-and-Drop-Suchtool? {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

Einige Content Blocks werden im Drag-and-Drop-Editor unter **Row** nicht angezeigt. Fügen Sie einen HTML-Block über den Tab **Content** (**Advanced**) hinzu und fügen Sie dann den Content-Block-Liquid-Tag in diesen HTML-Block ein, um den Blockinhalt zu rendern.

### Warum unterscheidet sich die Vorschau meines Drag-and-Drop-Content-Blocks von der Ansicht im Editor? {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Wenn Sie einen Content Block mit Liquid als Template verwenden, werden mobile Media-Queries im Block in der Vorschau möglicherweise nicht auf die gleiche Weise angewendet wie beim direkten Ziehen des Blocks in eine Nachricht. Das Ziehen des Blocks behält das Layout bei, entkoppelt ihn jedoch vom Quellblock, sodass zukünftige Blockänderungen die Nachricht nicht mehr automatisch aktualisieren.

### Wie kann ich Event-Eigenschaftswerte im Nachrichten-Editor in der Vorschau anzeigen? {#how-do-i-preview-event-property-values-in-message-composer}

Verwenden Sie **Vorschau als angepasste:r Nutzer:in** und geben Sie Beispielwerte für angepasste Event-Eigenschaften für die Nutzerin oder den Nutzer ein, die/den Sie in der Vorschau anzeigen. Dies ist auch nützlich für Nachrichten mit Abbruchlogik, wenn Sie Vorschauwerte benötigen, die keinen Abbruch auslösen.

## Liquid in E-Mail-Nachrichten {#liquid-in-email-messages}

### Warum bricht meine Nachricht mit „Invalid from email address for recipient:“ ab? {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

Dieser Abbruch tritt auf, wenn Liquid in der **Absender**-Adresse eine ungültige Syntax erzeugt, z. B. eine fehlende Variable, zusätzliche Leerzeichen oder unzulässige Zeichen. Zeigen Sie eine Vorschau mit einer Testnutzerin oder einem Testnutzer an und überprüfen Sie, ob die gerenderte **Absender**-Adresse mit Ihrer konfigurierten Sendedomain übereinstimmt.

### Wie erstelle ich eine dynamische Reply-To-Adresse? {#how-do-i-create-a-dynamic-reply-to-address}

Verwenden Sie Liquid im Feld **Reply-To**, wenn Ihr Workspace die dynamische Reply-To-Konfiguration unterstützt. Kombinieren Sie es bei Bedarf mit Ihren **Absender**-Anzeigenamen-Einstellungen. Weitere Informationen finden Sie unter [E-Mail-Einstellungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) für Workspace-spezifische Optionen.

## Fehlerbehebung bei Liquid-Fehlern {#troubleshooting-liquid-errors}

### Warum erhalte ich den Liquid-Fehler „Unexpected end token“? {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

Dieser Fehler weist in der Regel auf zusätzliche oder fehlende geschweifte Klammern hin. Verschachteln Sie {% raw %}`{{ }}`{% endraw %} nicht innerhalb eines anderen Liquid-Tag-Ausdrucks. Verwenden Sie zum Beispiel {% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %}, anstatt die Attributreferenz in ein zusätzliches Klammernpaar einzuschließen.

### Warum ist der Connected-Content-Retry für meine In-App-Nachricht nicht verfügbar? {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
Der `{% connected_content %}`-Tag mit Retry wird nicht für alle Nachrichtentypen unterstützt, einschließlich einiger In-App-Nachrichtenformate. Entfernen Sie Retry-Parameter oder verwenden Sie einen unterstützten Kanal für Connected-Content-Aufrufe mit Retry.
{% endraw %}