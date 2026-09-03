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

In vielen Fällen können Sie Liquid-Snippets einbinden, indem Sie zu Ihren Campaigns oder Canvases gehen und Liquid über das Personalisierungs-Modal in Bereichen wie dem E-Mail-Nachrichtentext oder in Ihren Segments einfügen.

#### Wo kann ich mehr erfahren? {#where-can-i-learn-more}

Weitere Informationen zu Liquid finden Sie in unserem geführten Braze-Lernpfad [Dynamische Personalisierung mit Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid). Sie können auch die [Liquid-Anwendungsfallbibliothek]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) als Inspiration und für eine Vielzahl von Personalisierungsbeispielen mit Liquid nutzen.

### Was ist der Unterschied zwischen der Verwendung von Liquid und Connected Content für die Personalisierung? {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

Braze Connected Content ist ein Beispiel für einen Liquid-Tag. Es wird ebenfalls für die Personalisierung verwendet, aber die Daten stammen von einem externen Endpunkt und nicht aus gespeicherten Daten innerhalb von Braze. In unserem speziellen Abschnitt zu [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) erfahren Sie mehr darüber, wie Sie die Personalisierung Ihrer Nachrichten erweitern können.

### Was ist Liquid-Templating? {#what-is-liquid-templating}

Dies ist die gebräuchlichste Art, Liquid in Braze zu verwenden. Beim Liquid-Templating werden Daten aus dem Profil einer Nutzerin oder eines Nutzers in eine Nachricht eingefügt. Diese Daten können vom Vornamen bis hin zu angepassten Events aus einer eventgetriggerten Nachricht reichen.

Eine vollständige Liste der unterstützten Liquid-Tags finden Sie unter [Unterstützte Personalisierungs-Tags]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags).

### Werden durch die Verwendung von Liquid Datenpunkte protokolliert? {#does-using-liquid-log-data-points}

Nein.

## Personalisierungs-Tags und Datenquellen {#personalization-tags-and-data-sources}

### Wie kann ich Liquid verwenden, um eine personalisierte Begrüßung zu senden? {#how-can-i-use-liquid-to-send-a-personalized-greeting}

Für eine personalisierte Begrüßung mit dem Vornamen der Nutzer:innen können Sie die Standard-Nutzerprofilattribute wie {% raw %}`{{${first_name}}}` und `{{${last_name}}}`{% endraw %} verwenden.

Sie können auch eine Liquid-{% raw %}`{% if X %}`{% endraw %}-Anweisung verwenden, um bedingtes Rendering basierend auf beliebigen Kriterien durchzuführen, wie z. B. dem Wochentag oder angepassten Attributen. Weitere Informationen zu den unterstützten Liquid-Operatoren, die in bedingten Anweisungen verwendet werden können, finden Sie unter [Operatoren]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators).

### Wie kann ich eine Nachricht basierend auf dem Standort der Nutzer:innen personalisieren? {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
Es gibt ein Standardattribut für den Standort der Nutzer:innen: `{{${most_recent_location}}}`.
{% endraw %}

{% raw %}
### Was ist der Unterschied zwischen {{campaign.${name}}} und {{campaign.${message_name}}}? {#whats-the-difference-between-campaignname-and-campaignmessage_name}

Sowohl `{{campaign.${name}}}` als auch `{{campaign.${message_name}}}` sind unterstützte Liquid-Personalisierungs-Tags. Beide Tags referenzieren Campaign-Attribute. `{{campaign.${name}}}` bezeichnet den Namen Ihrer Campaign, und `{{campaign.${message_name}}}` ist der Name Ihrer Nachrichtenvariante.
{% endraw %}

Zur Verwendung in URLs und Query-Strings (z. B. wenn ein Name `%` oder Leerzeichen enthält), lesen Sie [Campaign-Namen in URLs]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

### Wie verwende ich Liquid mit verschachtelten Objekten? {#how-do-i-use-liquid-with-nested-objects}

Braze verfügt über ein integriertes Feature, das Liquid-Code für Segments generiert, der in einer Nachricht verwendet werden kann. Konkret können Sie ein Segment erstellen, das mehrere Kriterien in einem Objekt abgleicht.

Weitere Informationen finden Sie unter [Segmentierung mit mehreren Kriterien]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#segmentation-behavior-with-arrays-of-objects).

### Wie verwende ich Event-Attribute, um eine Nachricht zu personalisieren, die von einem Event getriggert wird? {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
Sie können auf Eigenschaften von API-getriggerten Events mit dem Tag `api_triggered_property` zugreifen: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Unterstützt Braze ein Array von Arrays in Liquid? {#does-braze-support-an-array-of-arrays-in-liquid}

Liquid unterstützt nativ keine Arrays von Arrays. Speichern Sie Werte als Array kommaseparierter Strings und verwenden Sie den `split`-Filter, um sie bei Bedarf zu parsen.

## Variablen und Syntax {#variables-and-syntax}

### Wie weise ich Variablen mit Liquid zu? {#how-do-i-assign-variables-with-liquid}

Sie können Variablen erstellen und zuweisen, indem Sie den `assign`-Tag verwenden. Dieser erstellt eine Variable im Nachrichten-Editor, die auch in Ihrer gesamten Nachricht referenziert werden kann.

Sie können ein `assign` über mehrere Zeilen aufteilen, wenn Sie alle Braze-Liquid-Variablen mit doppelten geschweiften Klammern {% raw %}(`{{ }}`){% endraw %} umschließen. Ohne diese Klammern können mehrzeilige Assign-Anweisungen zu unerwartetem Rendering führen, einschließlich angepasster Attribute, die nicht korrekt als Template verarbeitet werden. Beispiele und zugehörige Syntaxregeln finden Sie unter [Liquid verwenden]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax).

### Wann sollte ich `assign` und wann `capture` verwenden? {#when-should-i-use-assign-versus-capture}

Sowohl `assign` als auch `capture` erstellen Liquid-Variablen, dienen jedoch unterschiedlichen Zwecken:

- `assign` eignet sich für einfache Variablen, die einen einzelnen Wert speichern, z. B. einen Boolean, eine Zahl oder einen einfachen String. Sie können auch einen einzelnen Filter in derselben Zeile anwenden.
- `capture` eignet sich zum Speichern eines Textblocks, der mehrere Variablen, Strings oder komplexe Ausdrücke enthalten kann.

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

Nein. Braze rendert jede Nachrichtenkomponente separat (z. B. Betreffzeile, HTML-Body, Preheader und Push-Titel). Zuweisungen oder Captures, die Sie in einem Feld vornehmen, stehen in einem anderen nicht zur Verfügung. Wiederholen Sie den Liquid- oder Connected-Content-Aufruf in jedem Feld, das den Wert benötigt.

### Was ist For-Loop-Logik, und wie kann ich sie verwenden? {#what-is-for-loop-logic-and-how-can-i-use-it}

For-Loops sind auch als [Iterations-Tags](https://shopify.github.io/liquid/tags/iteration/) bekannt. Die Verwendung von For-Loop-Logik in Ihren Liquid-Snippets ermöglicht es, Liquid-Blöcke so lange zu durchlaufen, bis eine Bedingung erfüllt ist.

In Braze kann dies zum Prüfen von Elementen in einem angepassten Array-Attribut oder einer Liste von Werten und Objekten verwendet werden, die von einem [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs), einer [Selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) oder einem [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)-Aufruf zurückgegeben werden. Konkret können Sie For-Loop-Logik als Teil Ihres Messagings nutzen, um zu prüfen, ob ein Produkt vorrätig ist oder ob ein Produkt eine Mindestbewertung hat.

Angenommen, Sie haben einen Katalog namens „Games“ mit einer Selection namens „cheap_games“. Um die Titel der Spiele in „cheap_games“ abzurufen, können Sie dieses Liquid-Snippet verwenden:

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

Mit Abbruchlogik können Sie das Senden einer Nachricht stoppen, wenn die Bedingungen erfüllt sind. Dies ist besonders hilfreich, um zu verhindern, dass unvollständige Nachrichten an Ihre Nutzer:innen gesendet werden. Weitere Beispiele für Abbruchlogik in Ihren Marketingkampagnen finden Sie unter [Nachrichten abbrechen]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

### Kann ich Liquid innerhalb des `abort_message`-Tags verwenden? {#can-i-use-liquid-inside-the-abort_message-tag}

Nein. Der {% raw %}`{% abort_message %}`{% endraw %}-Tag akzeptiert einen statischen String in Anführungszeichen, keine Liquid-Personalisierung. Verwenden Sie andere Liquid-Logik vor dem Tag, wenn Sie bedingtes Abbruchverhalten benötigen.

### Wie maskiere ich Telefonnummern mit Liquid? {#how-do-i-mask-phone-numbers-with-liquid}

Sie können Telefonnummern mit dem `slice`-Filter maskieren, um bestimmte Ziffern zu extrahieren, und dem `append`-Filter, um sie mit Maskierungszeichen zu kombinieren.

#### Alle Ziffern außer den letzten vier maskieren {#mask-all-but-the-last-four-digits}

Um eine 10-stellige Telefonnummer als `******7890` anzuzeigen:

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | split: '' %}
{% assign masked_phone = '' %}
{% for i in (0..5) %}
  {% assign masked_phone = masked_phone | append: '*' %}
{% endfor %}
{% for i in (6..9) %}
  {% assign masked_phone = masked_phone | append: phone[i] %}
{% endfor %}
{{ masked_phone }}
```
{% endraw %}

#### Die ersten drei und letzten vier Ziffern anzeigen {#show-the-first-three-and-last-four-digits}

Um eine 10-stellige Telefonnummer als `123***7890` anzuzeigen:

{% raw %}
```liquid
{% assign first_part = {{${phone_number}}} | slice: 0, 3 %}
{% assign last_part = {{${phone_number}}} | slice: -4, 4 %}
{% assign masked_phone_number = first_part | append: "***" | append: last_part %}
{{ masked_phone_number }}
```
{% endraw %}

## Canvas, Kataloge und Trigger-Eigenschaften {#canvas-catalogs-and-trigger-properties}

### Warum schlägt mein API-getriggertes Liquid in Braze fehl? {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
Ein häufiger Grund ist ein zusätzliches Paar geschweifter Klammern. Zum Beispiel ist `{{{api_trigger_properties.${attribute_key}}}}` keine gültige Braze-Personalisierungssyntax. Verwenden Sie genau zwei öffnende und zwei schließende geschweifte Klammern: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Gibt es Größenlimits für Canvas-Kontexteigenschaften? {#are-there-size-limits-for-canvas-context-properties}

Braze erzwingt kein festes Limit für [Canvas-Kontexteigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), aber halten Sie Payloads unter ungefähr 1 KB (~1.000 Zeichen). Größere Objekte können den Speicherverbrauch erhöhen und das Rendering von Nachrichten bei Versendungen mit hohem Volumen verzögern.

### Warum erhalte ich einen Liquid-Fehler, wenn ich bestimmte Datentypen im Dashboard in der Vorschau anzeige? {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

Einige Typen von [Canvas-Kontexteigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) erfordern eine Typkonvertierung in Liquid, bevor Sie sie in Vergleichen oder Berechnungen verwenden können. Wenn Sie beispielsweise numerisches Verhalten benötigen:

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### Warum gibt mein Katalog-Liquid-Snippet eine Abbruchmeldung zurück? {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

Wenn ein Katalog-Liquid-Snippet beim Senden abbricht, erstellen Sie das Snippet über das Personalisierungsmenü neu, indem Sie einzelne Katalogartikel auswählen, anstatt eine Massen- oder vollständig dynamische Auswahl zu verwenden. Siehe [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs) und [Selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Content Blocks und der Nachrichten-Editor {#content-blocks-and-the-message-composer}

### Warum gibt es zusätzliche Abstände in Nachrichten, die Content Blocks verwenden? {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Wenn Sie zusätzliche Abstände in gesendeten Nachrichten bemerken, die Content Blocks mit Liquid verwenden, haben Sie möglicherweise unnötige Absatz- oder Zeilenumbrüche in Ihren bedingten Anweisungen. Schreiben Sie Ihre bedingten Anweisungen in einer einzigen Zeile statt über mehrere Zeilen verteilt.

#### Beispiel {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}


### Warum erzeugt mehrzeiliger Liquid-Code unerwartete Leerzeichen in den Drag-and-drop-Editoren? {#why-does-multi-line-liquid-create-unexpected-whitespace-in-the-drag-and-drop-editors}

Wenn Liquid-Code im Drag-and-drop-Editor für In-App-Nachrichten oder im Drag-and-drop-Editor für E-Mails über mehrere Zeilen verteilt ist, wird jeder {% raw %}`{% %}`{% endraw %}-Block als nicht sichtbarer Text gerendert. Die Zeilenumbrüche werden als leere Zeilen vor der sichtbaren Ausgabe beibehalten, was zu unerwarteten Leerzeichen führt.

#### Lösung 1: Whitespace-Control-Tags verwenden (empfohlen) {#solution-1-use-whitespace-control-tags-recommended}

Fügen Sie Bindestriche innerhalb der Tag-Begrenzer hinzu, um umgebende Leerzeichen zu entfernen, während der Code lesbar bleibt:

{% raw %}
```liquid
{%- assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" -%}
{%- assign today = 'now' | date: "%s" -%}
{%- assign difference = event_date | minus: today -%}
{%- assign difference_days = difference | divided_by: 86400 -%}
Only {{ difference_days }} days until your move!
```
{% endraw %}

#### Lösung 2: Liquid in eine einzige Zeile zusammenfassen {#solution-2-consolidate-liquid-onto-a-single-line}

Entfernen Sie alle Zeilenumbrüche, sodass der Liquid-Code in einer durchgehenden Zeile steht:

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" %}{% assign today = 'now' | date: "%s" %}{% assign difference = event_date | minus: today %}{% assign difference_days = difference | divided_by: 86400 %}Only {{ difference_days }} days until your move!
```
{% endraw %}

Beide Ansätze verhindern unerwünschte leere Zeilen in Ihrer gerenderten Nachricht. Dies gilt für den Drag-and-drop-Editor für In-App-Nachrichten, den Drag-and-drop-Editor für E-Mails und Content Blocks mit Liquid. Weitere Informationen finden Sie in der Shopify-Dokumentation zu [Whitespace control](https://shopify.github.io/liquid/basics/whitespace/) und in der Braze-Dokumentation zur [Liquid-Syntax]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax).

### Warum fehlt mein Content Block unter **Zeile** im Drag-and-drop-Suchtool? {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

Einige Content Blocks werden unter **Zeile** in der Drag-and-drop-Editor-Suche nicht angezeigt. Fügen Sie einen HTML-Block über den Tab **Inhalt** (**Erweitert**) hinzu und setzen Sie dann den Content-Block-Liquid-Tag in diesen HTML-Block ein, um den Blockinhalt zu rendern.

### Warum unterscheidet sich die Drag-and-drop-Content-Block-Vorschau von der Editoransicht? {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Wenn Sie einen Content Block mit Liquid als Template verwenden, werden mobile Media-Queries im Block in der Vorschau möglicherweise nicht auf dieselbe Weise angewendet wie beim direkten Ziehen des Blocks in eine Nachricht. Das Ziehen des Blocks behält das Layout bei, entkoppelt ihn jedoch vom Quellblock, sodass zukünftige Blockänderungen die Nachricht nicht mehr automatisch aktualisieren.

### Wie kann ich Event-Property-Werte im Nachrichten-Editor in der Vorschau anzeigen? {#how-do-i-preview-event-property-values-in-message-composer}

Verwenden Sie **Vorschau als angepasste:r Nutzer:in** und geben Sie Beispielwerte für angepasste Event-Properties für die Person ein, deren Vorschau Sie anzeigen möchten. Dies ist auch nützlich für Nachrichten mit Abbruchlogik, wenn Sie Vorschauwerte benötigen, die keinen Abbruch auslösen.

## Liquid in E-Mail-Nachrichten {#liquid-in-email-messages}

### Warum wird meine Nachricht mit „Invalid from email address for recipient:“ abgebrochen? {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

Dieser Abbruch tritt auf, wenn Liquid in der **Absender**-Adresse ungültige Syntax erzeugt, zum Beispiel eine fehlende Variable, zusätzliche Leerzeichen oder unzulässige Zeichen. Nutzen Sie die Vorschau mit einer/einem Testnutzer:in und überprüfen Sie, ob die gerenderte **Absender**-Adresse mit Ihrer konfigurierten Absenderdomain übereinstimmt.

### Wie erstelle ich eine dynamische Antwortadresse? {#how-do-i-create-a-dynamic-reply-to-address}

Verwenden Sie Liquid im Feld **Reply-To**, wenn Ihr Workspace die Konfiguration dynamischer Antwortadressen unterstützt. Kombinieren Sie es bei Bedarf mit Ihren Einstellungen für den **Absender**-Anzeigenamen. Weitere Informationen zu Workspace-spezifischen Optionen finden Sie unter [E-Mail-Einstellungen]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences).

## Fehlerbehebung bei Liquid-Fehlern {#troubleshooting-liquid-errors}

### Warum funktioniert mein Liquid-Code nicht, obwohl er korrekt aussieht? {#why-is-my-liquid-code-not-working-when-it-looks-correct}

Wenn Ihr Liquid-Code syntaktisch korrekt erscheint, aber nicht funktioniert, prüfen Sie, ob typografische Anführungszeichen (geschweifte Anführungszeichen wie `' '` oder `" "`) und typografische Gedankenstriche (Geviertstriche wie `—`) anstelle von geraden Anführungszeichen (`' '` oder `" "`) und Bindestrichen (`-`) verwendet werden. Liquid erkennt nur gerade ASCII-Zeichen, sodass typografische Anführungszeichen und Striche zu Parsing-Fehlern führen.

Dies passiert häufig, wenn die macOS-Tastatureinstellung **Intelligente Anführungszeichen und Bindestriche verwenden** aktiviert ist, die Zeichen beim Tippen im Braze-Dashboard automatisch umwandelt.

So deaktivieren Sie diese Einstellung unter macOS:

1. Gehen Sie zu **Systemeinstellungen** > **Tastatur** > **Texteingabe** > **Bearbeiten**.
2. Deaktivieren Sie **Intelligente Anführungszeichen und Bindestriche verwenden**.

| Beispiel | Typografische Anführungszeichen (funktioniert nicht) | Gerade Anführungszeichen (funktioniert) |
| --- | --- | --- |
| Standardwert | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} |
| Bedingung | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Beispiele für typografische Anführungszeichen" }

Dies gilt für Standardwerte, Bedingungen und jeden anderen Liquid-Code, der Anführungszeichen verwendet. Typografische und gerade Anführungszeichen können auf dem Bildschirm gleich aussehen – vergleichen Sie Ihren Code daher sorgfältig oder fügen Sie ihn in einen Nur-Text-Editor ein.

Weitere Informationen zur Verwendung von Anführungszeichen in Liquid finden Sie unter [Liquid-Syntax]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax).

### Warum wird der Liquid-Fehler „Unexpected end token“ angezeigt? {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

Dieser Fehler weist in der Regel auf zusätzliche oder fehlende geschweifte Klammern hin. Verschachteln Sie {% raw %}`{{ }}`{% endraw %} nicht innerhalb eines anderen Liquid-Tag-Ausdrucks. Verwenden Sie zum Beispiel {% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %}, anstatt die Attributreferenz in ein zusätzliches Klammernpaar einzuschließen.

### Warum ist der Connected-Content-Retry für meine In-App-Nachricht nicht verfügbar? {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
Der `{% connected_content %}`-Tag mit Retry wird nicht für alle Nachrichtentypen unterstützt, einschließlich einiger In-App-Nachrichtenformate. Entfernen Sie die Retry-Parameter oder verwenden Sie einen unterstützten Kanal für Connected-Content-Aufrufe mit Retry.
{% endraw %}

### Warum wird der Fehler „Liquid Error: Comparison of Time with String Failed“ angezeigt? {#why-am-i-seeing-liquid-error-comparison-of-time-with-string-failed}

Dieser Fehler tritt auf, wenn ein angepasstes Attribut vom Typ „Zeit“ oder eine Event-Eigenschaft direkt mit einem leeren Wert (einem leeren String) verglichen wird. Liquid unterstützt keine direkten Vergleiche zwischen verschiedenen Datentypen, wie z. B. einem Zeitobjekt und einem String.

Das folgende Beispiel zeigt einen häufigen Fall, der diesen Fehler verursacht:

{% raw %}
```liquid
{% if {{custom_attribute.${expiration_date}}} == blank %}
  <a>Some words</a>
{% endif %}
```
{% endraw %}

Dies schlägt fehl, weil ein angepasstes Attribut mit dem Datentyp „Zeit“ nicht mit einem String (`blank`) verglichen werden kann.

Um dies zu beheben, wandeln Sie das Zeit-Attribut in einen String um, indem Sie es einer Variablen zuweisen und den `default`-Filter verwenden, wenn das Attribut zum Rendering-Zeitpunkt leer ist:

{% raw %}
```liquid
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% endif %}
```
{% endraw %}


Wenn Sie ein angepasstes Attribut vom Typ „Zeit“ mit der aktuellen Zeit oder zukünftigen Daten vergleichen, verwenden Sie denselben Ansatz:

{% raw %}
```liquid
{% assign today = 'now' | date: '%s' %}
{% assign month = 'now' | date: '%s' | plus: 2592000 %}
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% elsif expiration_date >= today and expiration_date >= month %}
  <a>More Words</a>
{% endif %}
```
{% endraw %}