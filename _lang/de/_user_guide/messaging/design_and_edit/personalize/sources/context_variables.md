---
nav_title: Kontextvariablen
article_title: Kontextvariablen
page_type: reference
description: "Dieser Referenzartikel erklärt Kontextvariablen in Braze Canvases, einschließlich ihrer Typen, Verwendung und Best Practices."
---

# Kontextvariablen {#context-variables}

> Kontextvariablen sind temporäre Daten, die Sie innerhalb der Journey von Nutzer:innen durch ein bestimmtes Canvas erstellen und verwenden können. Sie ermöglichen es Ihnen, Verzögerungen zu personalisieren, Nutzer:innen dynamisch zu segmentieren und Nachrichten anzureichern, ohne die Profilinformationen von Nutzer:innen dauerhaft zu verändern. Kontextvariablen existieren nur innerhalb der Canvas-Sitzung und bleiben nicht über verschiedene Canvases hinweg oder außerhalb der Sitzung bestehen.

## Funktionsweise von Kontextvariablen {#how-context-variables-work}

Kontextvariablen können auf zwei Arten festgelegt werden:

- **Beim Canvas-Eintritt:** Wenn Nutzer:innen ein Canvas betreten, können Daten aus dem Event oder dem API-Trigger automatisch Kontextvariablen befüllen.
- **In einem Kontextschritt:** Sie können Kontextvariablen innerhalb des Canvas manuell definieren oder aktualisieren, indem Sie einen [Kontextschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) hinzufügen.

Jede Kontextvariable umfasst:

- Einen Namen (z. B. `flight_time` oder `subscription_renewal_date`)
- Einen Datentyp (z. B. Zahl, String, Zeit oder Array)
- Einen Wert, den Sie mithilfe von [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) oder über das Tool **Add Personalization** zuweisen.

Nach der Definition können Sie eine Kontextvariable im gesamten Canvas verwenden, indem Sie sie in folgendem Format referenzieren: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Zum Beispiel könnte {% raw %}`{{context.${flight_time}}}`{% endraw %} die geplante Abflugzeit der Nutzer:innen zurückgeben.

Jedes Mal, wenn Nutzer:innen das Canvas betreten – auch wenn sie es zuvor bereits betreten haben – werden die Kontextvariablen basierend auf den neuesten Entry-Daten und der Canvas-Konfiguration neu definiert. Dieser zustandsbehaftete Ansatz ermöglicht es jedem Canvas-Eintritt, seinen eigenen unabhängigen Kontext beizubehalten, sodass Nutzer:innen mehrere aktive Zustände innerhalb derselben Journey haben können, während der spezifische Kontext für jeden Zustand erhalten bleibt.

Wenn eine Kundin oder ein Kunde beispielsweise zwei bevorstehende Flüge hat, laufen zwei separate Journey-Zustände gleichzeitig – jeder mit eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Zielort. So können Sie personalisierte Erinnerungen zum 14-Uhr-Flug nach New York senden und gleichzeitig andere Updates zum 8-Uhr-Flug nach Los Angeles am nächsten Tag verschicken, sodass jede Nachricht für die jeweilige Buchung relevant bleibt.

## Überlegungen {#considerations}

Sie können bis zu 10 Kontextvariablen pro [Kontextschritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) definieren. Jeder Variablenname kann bis zu 100 Zeichen lang sein und darf nur Buchstaben, Zahlen oder Unterstriche enthalten.

Kontextvariablen-Definitionen können bis zu 10.240 Zeichen umfassen. Wenn Sie Kontextvariablen in ein API-getriggertes Canvas übergeben, teilen sie sich denselben Namespace wie Variablen, die in einem Kontextschritt erstellt wurden. Wenn Sie beispielsweise eine Variable `purchased_item` im Kontextobjekt des [`/canvas/trigger/send`-Endpunkts]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) senden, können Sie sie als {% raw %}`{{context.${purchased_item}}}`{% endraw %} referenzieren. Wenn Sie diese Variable in einem Kontextschritt neu definieren, überschreibt der neue Wert den API-Wert für die Journey dieser Nutzer:in.

Sie können bis zu 50 KB pro Kontextschritt speichern, verteilt auf bis zu 10 Variablen. Wenn die Gesamtgröße aller Variablen in einem Schritt 50 KB überschreitet, werden Variablen, die das Limit überschreiten, nicht ausgewertet oder gespeichert. Wenn Sie beispielsweise drei Variablen in einem Kontextschritt haben:

- Variable 1: 30 KB
- Variable 2: 19 KB
- Variable 3: 2 KB

Variable 3 wird nicht ausgewertet oder gespeichert, da die Summe der vorherigen Variablen 50 KB überschreitet.

## Datentypen {#data-types}

Kontextvariablen, die im Schritt erstellt oder aktualisiert werden, können die folgenden Datentypen zugewiesen bekommen.

{% alert note %}
Kontextvariablen haben dieselben erwarteten Formate für Datentypen wie [Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#expected-format). <br><br>Bei Verwendung des Array-Typs versucht Braze, den Wert als JSON zu parsen, wodurch Arrays von Objekten erfolgreich erstellt werden können. Wenn die Objekte innerhalb Ihrer Arrays kein gültiges JSON sind, ist das Ergebnis ein einfaches String-Array. <br><br>Für verschachtelte Objekte und Arrays von Objekten verwenden Sie den [`as_json_string`-Liquid-Filter](#converting-connected-content-strings-to-json). Wenn Sie dasselbe Objekt in einem Kontextschritt erstellen, müssen Sie das Objekt mit `as_json_string` rendern, z. B. {%raw%}`{{context.${object_array} | as_json_string }}`{%endraw%}
{% endalert %}

| Datentyp | Beispiel-Variablenname | Beispielwert |
|---|---|---|
| Boolean | loyalty_program |{% raw %}<code>true</code>{% endraw %}|
| Number | credit_score |{% raw %}<code>740</code>{% endraw %}|
| String | product_name |{% raw %}<code>green_tea</code>{% endraw %} |
| Array | favorite_products |{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
| Array (von Objekten) | pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
| Time (in UTC) | last_purchase_date |{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
| Object (flattened) | user_profile |{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Datentypen" }

Standardmäßig ist der Datentyp „Time“ in UTC angegeben. Wenn Sie einen String-Datentyp verwenden, um einen Zeitwert zu speichern, können Sie die Zeit in einer anderen Zeitzone wie PST definieren.

Wenn Sie beispielsweise einem/einer Nutzer:in am Tag vor dem Geburtstag eine Nachricht senden möchten, würden Sie die Kontextvariable als Time-Datentyp speichern, da es Liquid-Logik gibt, die mit dem Versand am Vortag verknüpft ist. Wenn Sie jedoch eine Feiertagsnachricht am Weihnachtstag (25. Dezember) senden, müssten Sie die Zeit nicht als dynamische Variable referenzieren, sodass die Verwendung eines String-Datentyps vorzuziehen wäre.

Für Object-Datentypen können Sie die Punktnotation verwenden, um einen Pfad durch die Daten anzugeben. Wenn Ihr Kontextschritt beispielsweise eine Kontextvariable `order_summary` mit dieser Struktur definiert:

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

Geben Sie in einem [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)- oder [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)-Filter den Pfad als Kontextvariablennamen in Punktnotation ein (z. B. `order_summary.shipping.carrier`). Wenn der Filter ausgewertet wird, löst Braze diesen Pfad zum Wert `overnight` auf.

Verwenden Sie in Liquid (z. B. in einem [Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)-Schritt) stattdessen {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %}.

## Kontextvariablen verwenden {#using-context-variables}

Sie können Kontextvariablen überall dort verwenden, wo Sie Liquid in einem Canvas einsetzen, z. B. in [Nachrichten-]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) und [Nutzer:innen-Update-]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update)Schritten, indem Sie **Personalisierung hinzufügen** auswählen. Für In-App-Nachrichten und Banner in Nachrichten-Schritten können Sie Kontextvariablen auswählen, um festzulegen, wann die Nachricht ablaufen soll.

Nehmen wir zum Beispiel an, Sie möchten Passagiere über ihren VIP-Lounge-Zugang vor ihrem bevorstehenden Flug benachrichtigen. Diese Nachricht soll nur an Passagiere gesendet werden, die ein First-Class-Ticket gekauft haben. Eine Kontextvariable ist eine flexible Möglichkeit, diese Information zu verfolgen.

Nutzer:innen treten in den Canvas ein, wenn sie ein Flugticket kaufen. Um die Berechtigung für den Lounge-Zugang zu bestimmen, erstellen wir eine Kontextvariable namens `lounge_access_granted` in einem Kontext-Schritt und referenzieren diese Kontextvariable dann in nachfolgenden Schritten der User Journey.

![Kontextvariable, die eingerichtet wurde, um zu verfolgen, ob ein Passagier für VIP-Lounge-Zugang qualifiziert ist.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

In diesem Kontext-Schritt verwenden wir {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %}, um festzustellen, ob der gebuchte Flugtyp `first_class` ist.

Als Nächstes erstellen wir einen Nachrichten-Schritt, der Nutzer:innen anspricht, bei denen {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} den Wert `true` hat. Diese Nachricht wird eine Push-Benachrichtigung mit personalisierten Lounge-Informationen sein. Basierend auf dieser Kontextvariable erhalten die berechtigten Passagiere die relevanten Nachrichten vor ihrem Flug.

- First-Class-Passagiere erhalten: „Genießen Sie exklusiven VIP-Lounge-Zugang!“
- Business- und Economy-Passagiere erhalten: „Upgraden Sie Ihren Flug für exklusiven VIP-Lounge-Zugang.“

![Ein Nachrichten-Schritt mit verschiedenen Nachrichten, die je nach Art des gekauften Flugtickets gesendet werden.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Sie können [personalisierte Verzögerungsoptionen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step#personalized-delays) mit den Informationen aus dem Kontext-Schritt hinzufügen, d. h. Sie können die Variable auswählen, die Nutzer:innen verzögert.
{% endalert %}

### Für Aktionspfade und Exit-Kriterien {#for-action-paths-and-exit-criteria}

Sie können vergleichende Eigenschaftsfilter mit Kontextvariablen oder angepassten Attributen in diesen Trigger-Aktionen nutzen: **Angepasstes Event ausführen** und **Kauf tätigen**. Diese Aktions-Trigger unterstützen auch Eigenschaftsfilter für einfache und verschachtelte Eigenschaften.

- Beim Vergleich mit einfachen Eigenschaften entsprechen die verfügbaren Vergleiche dem Typ der Eigenschaft, die durch das angepasste Event definiert ist. Zum Beispiel haben String-Eigenschaften exakte Gleichheit und Regex-Übereinstimmungen. Boolesche Eigenschaften sind wahr oder falsch.
- Beim Vergleich mit verschachtelten Eigenschaften sind die Typen nicht vordefiniert, sodass Sie Vergleiche über mehrere Datentypen hinweg für boolesche Werte, Zahlen, Strings, Zeit und Tag des Jahres auswählen können, ähnlich wie bei den Vergleichen für verschachtelte angepasste Attribute. Wenn Sie einen Datentyp auswählen, der zum Zeitpunkt des Vergleichs nicht mit dem tatsächlichen Datentyp der verschachtelten Eigenschaft übereinstimmt, wird die Nutzer:in nicht dem Aktionspfad oder den Exit-Kriterien zugeordnet.

#### Aktionspfad-Beispiele {#action-path-examples}

{% alert important %}
Für Vergleiche mit angepassten Attributen wird der Wert des angepassten Attributs zum Zeitpunkt der Ausführung der Aktion verwendet. Das bedeutet, dass Nutzer:innen nicht der Aktionspfad-Gruppe zugeordnet werden, wenn sie dieses angepasste Attribut zum Zeitpunkt des Vergleichs nicht befüllt haben oder wenn der Wert des angepassten Attributs nicht mit den definierten Eigenschaftsvergleichen übereinstimmt. Dies gilt auch dann, wenn die Nutzer:innen beim Eintritt in den Aktionspfad-Schritt zugeordnet worden wären.
{% endalert %}

{% tabs %}
{% tab Angepasstes Event ausführen %}

Der folgende Aktionspfad ist so eingerichtet, dass Nutzer:innen sortiert werden, die das angepasste Event `Account_Created` mit der einfachen Eigenschaft `source` zur Kontextvariable `app_source_variable` ausgeführt haben.

![Ein Beispiel-Aktionspfad, der eine Kontextvariable beim Ausführen eines angepassten Events referenziert.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Kauf tätigen %}

Der folgende Aktionspfad ist so eingerichtet, dass die einfache Eigenschaft `brand` für den spezifischen Produktnamen `shoes` mit einer Kontextvariable `promoted_shoe_brand` abgeglichen wird.

![Ein Beispiel-Aktionspfad, der eine Kontextvariable beim Tätigen eines Kaufs referenziert.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Exit-Kriterien-Beispiele {#exit-criteria-examples}

{% tabs %}
{% tab Angepasstes Event ausführen %}

Die Exit-Kriterien besagen, dass Nutzer:innen an jedem Punkt ihrer Journey im Canvas den Canvas verlassen, wenn:

- Sie das angepasste Event **Warenkorb abbrechen** ausführen, und
- Die einfache Eigenschaft **Artikel im Warenkorb** mit dem String-Wert der Kontextvariable `cart_item_threshold` übereinstimmt.

![Exit-Kriterien, die eingerichtet wurden, um Nutzer:innen zu entfernen, wenn sie ein angepasstes Event basierend auf der Kontextvariable ausführen.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Kauf tätigen %}

Die Exit-Kriterien besagen, dass Nutzer:innen an jedem Punkt ihrer Journey im Canvas den Canvas verlassen, wenn:

- Sie einen bestimmten Kauf für den Produktnamen „book“ tätigen, und
- Die verschachtelte Eigenschaft „loyalty_program“ dieses Kaufs dem angepassten Attribut „VIP“ der Nutzer:in entspricht.

![Exit-Kriterien, die eingerichtet wurden, um Nutzer:innen zu entfernen, wenn sie einen Kauf tätigen.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Ablauf festlegen {#set-an-expiration}

Für [Banner]({{site.baseurl}}/user_guide/channels/banners) und [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages) in einem Canvas-[Nachrichten-]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)Schritt wählen Sie **Eine Dauer, nachdem der Schritt verfügbar ist** für den Ablauf aus und aktivieren dann **Dauer personalisieren**, um das Verfügbarkeitsfenster über eine Kontextvariable zu steuern – zum Beispiel, um es an eine Aktions- oder Buchungsdauer aus einem Kontext-Schritt anzupassen.

**Dauer personalisieren** gilt für diese dauerbasierte Ablaufoption. Wenn Sie stattdessen **An einem bestimmten Datum und Uhrzeit** wählen, legen Sie den Ablauf über die Datums- und Uhrzeitsteuerungen fest.

### Aktionspfad-Verzögerungen {#action-path-delays}

In einem [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths)-Schritt aktivieren Sie unter **Auswertungsfenster** die Option **Verzögerung personalisieren**, um festzulegen, wie lange Nutzer:innen basierend auf einer Kontextvariable im Schritt gehalten werden. Verwenden Sie dies, wenn die Wartezeit je nach Nutzer:in variieren soll, z. B. basierend auf Details wie Stufe oder Region.

### Kontextvariablen-Filter {#context-variable-filters}

Sie können Filter erstellen, die zuvor deklarierte Kontextvariablen in [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)- und [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)-Schritten verwenden.

{% alert note %}
Kontextvariablen-Filter sind nur für Zielgruppenpfade- und Decision-Split-Schritte verfügbar.
{% endalert %}

Kontextvariablen werden deklariert und sind nur im Geltungsbereich eines Canvas zugänglich, d. h. sie können nicht in Segmenten referenziert werden. Kontextvariablen-Filter funktionieren in Zielgruppenpfade- und Decision-Split-Schritten ähnlich – Zielgruppenpfade-Schritte repräsentieren mehrere Gruppen, während Decision-Split-Schritte binäre Entscheidungen darstellen.

![Beispiel eines Decision-Split-Schritts mit der Option, einen Filter mit einer Kontextvariable zu erstellen.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Ähnlich wie Canvas-Kontextvariablen vordefinierte Typen haben, müssen die Vergleiche zwischen Kontextvariablen und statischen Werten [übereinstimmende Datentypen]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support) aufweisen. Der Kontextvariablen-Filter ermöglicht Vergleiche über mehrere Datentypen hinweg für boolesche Werte, Zahlen, Strings, Zeit und Tag des Jahres, ähnlich wie bei den Vergleichen für [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).

Hier ist ein Beispiel für einen Kontextvariablen-Filter, der die Kontextvariable `product_name` mit dem Regex `/braze/` vergleicht.

![Ein Filter-Setup für die Kontextvariable „product_name“, um den Regex „/braze/“ abzugleichen.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Tag-des-Jahres- und Zeit-Filter für Datums-Kontextvariablen {#day-of-year-and-time-filters-for-date-context-variables}

Um **Tag des Jahres**- oder **Zeit**-Vergleichsfilter mit einer Kontextvariable zu verwenden:

1. Fügen Sie einen [Kontext-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) hinzu, der eine Kontextvariable auf ein Kalenderdatum setzt (z. B. 23. Oktober 2025).
2. Fügen Sie einen [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)-Schritt nach dem Kontext-Schritt hinzu.
3. Fügen Sie im Zielgruppenpfade-Schritt einen Filter hinzu, der Nutzer:innen basierend auf dieser Kontextvariable aufteilt.
4. Wählen Sie einen Vergleich aus der Kategorie **Tag des Jahres** oder **Zeit**.

Wenn eine Kontextvariable keinen deklarierten Typ hat, zeigt Braze alle verfügbaren Vergleichstypen im Dropdown an, einschließlich **Tag des Jahres** und **Zeit**. Wenn die Variable im Kontext-Schritt als **Zeit**-Typ deklariert ist, werden nur **Tag des Jahres**- und **Zeit**-Vergleiche angezeigt. Für andere Datentypen mit einem bekannten Typ (z. B. ein verschachteltes angepasstes Attribut mit einem Zeit-Typ) werden nur die Vergleiche angezeigt, die für diesen Typ gelten.

Hier ist ein Beispiel eines Kontextvariablen-Filters, der die Kontextvariable `product_name` mit dem Regex `/braze/` vergleicht.

![Ein Filter-Setup für die Kontextvariable „product_name“, um den Regex „/braze/“ abzugleichen.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Tag-des-Jahres- und Zeit-Filter für Datums-Kontextvariablen {#day-of-year-and-time-filters-for-date-context-variables}

Um **Tag des Jahres**- oder **Zeit**-Vergleichsfilter mit einer Kontextvariable zu verwenden:

1. Fügen Sie einen [Kontext-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) hinzu, der eine Kontextvariable auf ein Kalenderdatum setzt (z. B. 23. Oktober 2025).
2. Fügen Sie nach dem Kontext-Schritt einen [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)-Schritt hinzu.
3. Fügen Sie im Zielgruppenpfade-Schritt einen Filter hinzu, der Nutzer:innen basierend auf dieser Kontextvariable aufteilt.
4. Wählen Sie einen Vergleich aus der Kategorie **Tag des Jahres** oder **Zeit**.

Wenn eine Kontextvariable keinen deklarierten Typ hat, zeigt Braze alle verfügbaren Vergleichstypen im Dropdown an, einschließlich **Tag des Jahres** und **Zeit**. Wenn die Variable im Kontext-Schritt als **Zeit**-Typ deklariert ist, werden nur **Tag des Jahres**- und **Zeit**-Vergleiche angezeigt. Für andere Datentypen mit einem bekannten Typ (z. B. ein verschachteltes angepasstes Attribut mit einem Zeit-Typ) werden nur die Vergleiche angezeigt, die für diesen Typ gelten.

{% alert note %}
Verwenden Sie denselben Datentyp für Ihre Kontextvariable und den Vergleich. Wenn Ihre Kontextvariable beispielsweise ein Zeit-Datentyp ist, verwenden Sie Zeit-Vergleiche (wie „vor“ oder „nach“). Die Verwendung nicht übereinstimmender Datentypen (wie String-Vergleiche mit einer Zeit-Kontextvariable) kann zu unerwartetem Verhalten führen.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

#### Vergleich mit Kontextvariablen oder angepassten Attributen {#comparing-to-context-variables-or-custom-attributes}

Durch Auswahl des Umschalters **Mit einer Kontextvariable oder einem angepassten Attribut vergleichen** können Sie Kontextvariablen-Filter erstellen, die mit zuvor definierten Kontextvariablen oder angepassten Nutzer:innen-Attributen verglichen werden. Dies kann nützlich sein, um Vergleiche durchzuführen, die pro Nutzer:in dynamisch sind, wie API-getriggerter `context`, oder um komplexe Vergleichslogik zu verdichten, die über Kontextvariablen hinweg definiert ist.

{% tabs %}
{% tab Beispiel 1 %}

Nehmen wir an, Sie möchten Nutzer:innen nach einer dynamischen Inaktivitätsperiode eine personalisierte Erinnerung senden, die alle einschließt, die sich in den letzten drei Tagen nicht in Ihrer App angemeldet haben.

Sie haben eine Kontextvariable `re_engagement_date`, die als {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} definiert ist. Beachten Sie, dass `3 days` ein variabler Betrag sein kann, der auch als angepasstes Attribut der Nutzer:in gespeichert ist. Wenn also das `re_engagement_date` nach dem `last_login_date` (als angepasstes Attribut im Nutzerprofil gespeichert) liegt, wird ihnen eine Nachricht gesendet.

![Ein Filter-Setup mit angepassten Attributen als Personalisierungstyp für die Kontextvariable „re_engagement_date“ nach dem angepassten Attribut „last_login_date“.]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Beispiel 2 %}

Der folgende Filter vergleicht die Kontextvariable `reminder_date` so, dass sie vor der Kontextvariable `appointment_deadline` liegt. Dies kann helfen, Nutzer:innen in einem Zielgruppenpfade-Schritt zu gruppieren, um festzustellen, ob sie vor ihrer Terminfrist zusätzliche Erinnerungen erhalten sollen.

![Ein Filter-Setup mit Kontextvariablen als Personalisierungstyp für die Kontextvariable „reminder_date“ zur Kontextvariable „appointment_deadline“.]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Standardisierung der Zeitzonenkonsistenz {#time-zone-consistency-standardization}

Obwohl die meisten Event-Eigenschaften mit dem Timestamp-Typ in Canvas bereits in UTC vorliegen, gibt es einige Ausnahmen. Mit der Einführung von Canvas Context werden alle standardmäßigen Timestamp-Event-Eigenschaften in aktionsbasierten Canvases einheitlich in UTC angegeben. Diese Änderung ist Teil einer umfassenderen Maßnahme, um ein vorhersehbareres und konsistenteres Erlebnis beim Bearbeiten von Canvas-Schritten und Nachrichten zu gewährleisten. Beachten Sie, dass diese Änderung alle aktionsbasierten Canvases betrifft, unabhängig davon, ob das jeweilige Canvas einen Context-Schritt verwendet oder nicht.

{% alert important %}
Unter allen Umständen empfehlen wir dringend, [Liquid-time_zone-Filter]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties#things-to-know) zu verwenden, damit Timestamps in der gewünschten Zeitzone dargestellt werden. Ein Beispiel finden Sie in dieser [häufig gestellten Frage im Artikel zum Context-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#faq-example).
{% endalert %}

## Verwandte Artikel {#related-articles}

- [Context-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)
- [Personalisierung und dynamischer Content mit Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)