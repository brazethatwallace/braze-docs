---
nav_title: Kontextvariablen
article_title: Kontextvariablen
page_type: reference
description: "Dieser Referenzartikel erklärt Kontextvariablen in Braze Canvases, einschließlich ihrer Typen, Verwendung und Best Practices."
---

# Kontextvariablen {#context-variables}

> Kontextvariablen sind temporäre Daten, die Sie innerhalb der Journey von Nutzer:innen durch ein bestimmtes Canvas erstellen und verwenden können. Sie ermöglichen es Ihnen, Verzögerungen zu personalisieren, Nutzer:innen dynamisch zu segmentieren und Nachrichten anzureichern, ohne die Profilinformationen von Nutzer:innen dauerhaft zu verändern. Kontextvariablen existieren nur innerhalb der Canvas-Sitzung und bleiben nicht über verschiedene Canvases hinweg oder außerhalb der Sitzung bestehen.

## Wie Kontextvariablen funktionieren {#how-context-variables-work}

Kontextvariablen können auf zwei Arten gesetzt werden:

- **Beim Canvas-Eintritt:** Wenn Nutzer:innen ein Canvas betreten, können Daten aus dem Event oder API-Trigger automatisch Kontextvariablen befüllen.
- **In einem Kontext-Schritt:** Sie können Kontextvariablen manuell innerhalb des Canvas definieren oder aktualisieren, indem Sie einen [Kontext-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) hinzufügen.

Jede Kontextvariable umfasst:

- Einen Namen (wie `flight_time` oder `subscription_renewal_date`)
- Einen Datentyp (wie Zahl, String, Zeit oder Array)
- Einen Wert, den Sie mit [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/) oder über das Tool **Add Personalization** zuweisen.

Sobald definiert, können Sie eine Kontextvariable im gesamten Canvas verwenden, indem Sie sie in diesem Format referenzieren: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Zum Beispiel könnte {% raw %}`{{context.${flight_time}}}`{% endraw %} die geplante Flugzeit der Nutzer:in zurückgeben.

Jedes Mal, wenn eine Nutzer:in das Canvas betritt – auch wenn sie es zuvor bereits betreten hat – werden die Kontextvariablen basierend auf den neuesten Eintrittsdaten und der Canvas-Konfiguration neu definiert. Dieser zustandsbehaftete Ansatz ermöglicht es jedem Canvas-Eintritt, seinen eigenen unabhängigen Kontext beizubehalten, sodass Nutzer:innen mehrere aktive Zustände innerhalb derselben Journey haben können, während der spezifische Kontext für jeden Zustand erhalten bleibt.

Wenn ein:e Kund:in beispielsweise zwei bevorstehende Flüge hat, werden zwei separate Journey-Zustände gleichzeitig ausgeführt – jeder mit seinen eigenen flugspezifischen Kontextvariablen wie Abflugzeit und Zielort. So können Sie personalisierte Erinnerungen über den 14-Uhr-Flug nach New York senden und gleichzeitig andere Updates über den 8-Uhr-Flug nach Los Angeles am nächsten Tag versenden, sodass jede Nachricht für die jeweilige Buchung relevant bleibt.

## Hinweise {#considerations}

Sie können bis zu 10 Kontextvariablen pro [Kontext-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/) definieren. Jeder Variablenname kann bis zu 100 Zeichen lang sein und darf nur Buchstaben, Zahlen oder Unterstriche enthalten.

Kontextvariablen-Definitionen können bis zu 10.240 Zeichen umfassen. Wenn Sie Kontextvariablen in ein API-getriggertes Canvas übergeben, teilen sie sich denselben Namespace wie Variablen, die in einem Kontext-Schritt erstellt werden. Wenn Sie beispielsweise eine Variable `purchased_item` im [`/canvas/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)-Kontextobjekt senden, können Sie sie als {% raw %}`{{context.${purchased_item}}}`{% endraw %} referenzieren. Wenn Sie diese Variable in einem Kontext-Schritt neu definieren, überschreibt der neue Wert den API-Wert für die Journey dieser Nutzer:in.

Sie können bis zu 50 KB pro Kontext-Schritt speichern, verteilt auf bis zu 10 Variablen. Wenn die Gesamtgröße aller Variablen in einem Schritt 50 KB überschreitet, werden Variablen, die das Limit überschreiten, nicht ausgewertet oder gespeichert. Wenn Sie beispielsweise drei Variablen in einem Kontext-Schritt haben:

- Variable 1: 30 KB
- Variable 2: 19 KB
- Variable 3: 2 KB

Variable 3 wird nicht ausgewertet oder gespeichert, da die Summe der vorherigen Variablen 50 KB überschreitet.

## Datentypen {#data-types}

Kontextvariablen, die im Schritt erstellt oder aktualisiert werden, können die folgenden Datentypen zugewiesen bekommen.

{% alert note %}
Kontextvariablen haben dieselben erwarteten Formate für Datentypen wie [Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#expected-format). <br><br>Bei Verwendung des Array-Typs versucht Braze, den Wert als JSON zu parsen, wodurch Arrays von Objekten erfolgreich erstellt werden können. Wenn die Objekte innerhalb Ihrer Arrays kein gültiges JSON sind, ist das Ergebnis ein einfaches String-Array. <br><br>Für verschachtelte Objekte und Arrays von Objekten verwenden Sie den [`as_json_string`-Liquid-Filter](#converting-connected-content-strings-to-json). Wenn Sie dasselbe Objekt in einem Kontext-Schritt erstellen, müssen Sie das Objekt mit `as_json_string` rendern, wie z. B. {%raw%}`{{context.${object_array} | as_json_string }}`{%endraw%}
{% endalert %}

| Datentyp | Beispiel-Variablenname | Beispielwert |
|---|---|---|
| Boolescher Wert | loyalty_program |{% raw %}<code>true</code>{% endraw %}|
| Zahl | credit_score |{% raw %}<code>740</code>{% endraw %}|
| String | product_name |{% raw %}<code>green_tea</code>{% endraw %} |
| Array | favorite_products |{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
| Array (von Objekten) | pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
| Zeit (in UTC) | last_purchase_date |{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
| Objekt (flach) | user_profile |{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Data types" }

Standardmäßig ist der Zeit-Datentyp in UTC. Wenn Sie einen String-Datentyp verwenden, um einen Zeitwert zu speichern, können Sie die Zeit in einer anderen Zeitzone wie PST definieren.

Wenn Sie beispielsweise eine Nachricht am Tag vor dem Geburtstag einer Nutzer:in senden möchten, würden Sie die Kontextvariable als Zeit-Datentyp speichern, da es Liquid-Logik gibt, die mit dem Versand am Vortag verbunden ist. Wenn Sie jedoch eine Feiertagsnachricht am Weihnachtstag (25. Dezember) senden, müssten Sie die Zeit nicht als dynamische Variable referenzieren, sodass die Verwendung eines String-Datentyps vorzuziehen wäre.

Für Objekt-Datentypen können Sie die Punkt-Notation verwenden, um einen Pfad durch die Daten anzugeben. Wenn Ihr Kontext-Schritt beispielsweise eine Kontextvariable `order_summary` mit dieser Struktur definiert:

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

In einem [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/)- oder [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)-Filter geben Sie den Pfad als Kontextvariablennamen in Punkt-Notation ein (z. B. `order_summary.shipping.carrier`). Wenn der Filter ausgewertet wird, löst Braze diesen Pfad zum Wert `overnight` auf.

In Liquid (z. B. in einem [Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)-Schritt) verwenden Sie stattdessen {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %}.

## Kontextvariablen verwenden {#using-context-variables}

Sie können Kontextvariablen überall dort verwenden, wo Sie Liquid in einem Canvas einsetzen, z. B. in [Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)- und [Nutzeraktualisierung]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update/)-Schritten, indem Sie **Add Personalization** auswählen. Für In-App-Nachrichten und Banner in Nachrichten-Schritten können Sie Kontextvariablen auswählen, um zu bestimmen, wann die Nachricht ablaufen soll.

Nehmen wir beispielsweise an, Sie möchten Passagiere über ihren VIP-Lounge-Zugang vor ihrem bevorstehenden Flug benachrichtigen. Diese Nachricht soll nur an Passagiere gesendet werden, die ein First-Class-Ticket gekauft haben. Eine Kontextvariable ist eine flexible Möglichkeit, diese Information zu verfolgen.

Nutzer:innen betreten das Canvas, wenn sie ein Flugticket kaufen. Um die Berechtigung für den Lounge-Zugang zu bestimmen, erstellen wir eine Kontextvariable namens `lounge_access_granted` in einem Kontext-Schritt und referenzieren diese Kontextvariable dann in nachfolgenden Schritten der Journey.

![Kontextvariable, die eingerichtet wurde, um zu verfolgen, ob ein Passagier für VIP-Lounge-Zugang qualifiziert ist.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

In diesem Kontext-Schritt verwenden wir {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %}, um zu bestimmen, ob der Typ des gekauften Fluges `first_class` ist.

Als Nächstes erstellen wir einen Nachrichten-Schritt, der Nutzer:innen anspricht, bei denen {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} `true` ist. Diese Nachricht wird eine Push-Benachrichtigung sein, die personalisierte Lounge-Informationen enthält. Basierend auf dieser Kontextvariable erhalten die berechtigten Passagiere die relevanten Nachrichten vor ihrem Flug.

- First-Class-Ticket-Passagiere erhalten: „Genießen Sie exklusiven VIP-Lounge-Zugang!“
- Business- und Economy-Ticket-Passagiere erhalten: „Upgraden Sie Ihren Flug für exklusiven VIP-Lounge-Zugang.“

![Ein Nachrichten-Schritt mit verschiedenen Nachrichten, die je nach Art des gekauften Flugtickets gesendet werden.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Sie können [personalisierte Verzögerungsoptionen]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step/#personalized-delays) mit den Informationen aus dem Kontext-Schritt hinzufügen, d. h. Sie können die Variable auswählen, die Nutzer:innen verzögert.
{% endalert %}

### Für Aktionspfade und Ausstiegskriterien {#for-action-paths-and-exit-criteria}

Sie können vergleichende Eigenschaftsfilter mit Kontextvariablen oder angepassten Attributen in diesen Trigger-Aktionen nutzen: **Perform Custom Event** und **Make Purchase**. Diese Aktions-Trigger unterstützen auch Eigenschaftsfilter für sowohl einfache als auch verschachtelte Eigenschaften.

- Beim Vergleich mit einfachen Eigenschaften entsprechen die verfügbaren Vergleiche dem Typ der Eigenschaft, die durch das angepasste Event definiert ist. Zum Beispiel haben String-Eigenschaften „genau gleich“ und Regex-Übereinstimmungen. Boolesche Eigenschaften sind wahr oder falsch.
- Beim Vergleich mit verschachtelten Eigenschaften sind Typen nicht vordefiniert, sodass Sie Vergleiche über mehrere Datentypen für boolesche Werte, Zahlen, Strings, Zeit und Tag des Jahres auswählen können, ähnlich wie die Vergleiche für verschachtelte angepasste Attribute. Wenn Sie einen Datentyp auswählen, der zum Zeitpunkt des Vergleichs nicht mit dem tatsächlichen Datentyp der verschachtelten Eigenschaft übereinstimmt, wird die Nutzer:in nicht dem Aktionspfad oder den Ausstiegskriterien zugeordnet.

#### Aktionspfad-Beispiele {#action-path-examples}

{% alert important %}
Für Vergleiche mit angepassten Attributen wird der Wert des angepassten Attributs zum Zeitpunkt der Aktionsausführung verwendet. Das bedeutet, dass eine Nutzer:in nicht der Aktionspfad-Gruppe zugeordnet wird, wenn sie dieses angepasste Attribut zum Zeitpunkt des Vergleichs nicht befüllt hat oder wenn der Wert des angepassten Attributs nicht mit den definierten Eigenschaftsvergleichen übereinstimmt. Dies gilt auch dann, wenn die Nutzer:in beim Eintritt in den Aktionspfad-Schritt zugeordnet worden wäre.
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

#### Beispiele für Ausstiegskriterien {#exit-criteria-examples}

{% tabs %}
{% tab Angepasstes Event ausführen %}

Die Ausstiegskriterien besagen, dass die Nutzer:in an jedem Punkt ihrer Journey im Canvas das Canvas verlässt, wenn:

- Sie das angepasste Event **Abandon Cart** ausführt, und
- die einfache Eigenschaft **Item in Cart** mit dem String-Wert der Kontextvariable `cart_item_threshold` übereinstimmt.

![Ausstiegskriterien, die eingerichtet wurden, um eine Nutzer:in zu entfernen, wenn sie ein angepasstes Event basierend auf der Kontextvariable ausführt.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Kauf tätigen %}

Die Ausstiegskriterien besagen, dass die Nutzer:in an jedem Punkt ihrer Journey im Canvas das Canvas verlässt, wenn:

- Sie einen bestimmten Kauf für den Produktnamen „book“ tätigt, und
- die verschachtelte Eigenschaft „loyalty_program“ dieses Kaufs dem angepassten Attribut „VIP“ der Nutzer:in entspricht.

![Ausstiegskriterien, die eingerichtet wurden, um eine Nutzer:in zu entfernen, wenn sie einen Kauf tätigt.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Ablauf festlegen {#set-an-expiration}

Für [Banner]({{site.baseurl}}/user_guide/channels/banners/) und [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/) in einem Canvas-[Nachrichten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)-Schritt wählen Sie **A duration after the step is available** für den Ablauf und aktivieren dann **Personalize duration**, um das Verfügbarkeitsfenster über eine Kontextvariable zu steuern – zum Beispiel, um es an eine Aktions- oder Buchungsdauer aus einem Kontext-Schritt anzupassen.

**Personalize duration** gilt für diese dauerbasierte Ablaufoption. Wenn Sie stattdessen **On a specific date and time** wählen, legen Sie den Ablauf über die Datums- und Uhrzeitsteuerungen fest.

### Aktionspfad-Verzögerungen {#action-path-delays}

In einem [Aktionspfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/)-Schritt aktivieren Sie unter **Evaluation Window** die Option **Personalize delay**, um festzulegen, wie lange Nutzer:innen basierend auf einer Kontextvariable im Schritt gehalten werden. Verwenden Sie dies, wenn die Wartezeit je nach Nutzer:in basierend auf Details wie Stufe oder Region unterschiedlich sein soll.

### Kontextvariablen-Filter {#context-variable-filters}

Sie können Filter erstellen, die zuvor deklarierte Kontextvariablen in [Zielgruppenpfade]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths/)- und [Decision-Split]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split/)-Schritten verwenden.

{% alert note %}
Kontextvariablen-Filter sind nur für Zielgruppenpfade- und Decision-Split-Schritte verfügbar.
{% endalert %}

Kontextvariablen werden deklariert und sind nur im Geltungsbereich eines Canvas zugänglich, was bedeutet, dass sie nicht in Segmenten referenziert werden können. Kontextvariablen-Filter funktionieren in Zielgruppenpfade- und Decision-Split-Schritten ähnlich – Zielgruppenpfade-Schritte repräsentieren mehrere Gruppen, während Decision-Split-Schritte binäre Entscheidungen darstellen.

![Beispiel eines Decision-Split-Schritts mit der Option, einen Filter mit einer Kontextvariable zu erstellen.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Ähnlich wie Canvas-Kontextvariablen vordefinierte Typen haben, müssen die Vergleiche zwischen Kontextvariablen und statischen Werten [übereinstimmende Datentypen]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#supported-data-types) aufweisen. Der Kontextvariablen-Filter ermöglicht Vergleiche über mehrere Datentypen für boolesche Werte, Zahlen, Strings, Zeit und Tag des Jahres, ähnlich wie die Vergleiche für [verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/).

{% alert note %}
Verwenden Sie denselben Datentyp für Ihre Kontextvariable und den Vergleich. Wenn Ihre Kontextvariable beispielsweise ein Zeit-Datentyp ist, verwenden Sie Zeitvergleiche (wie „vor“ oder „nach“). Die Verwendung nicht übereinstimmender Datentypen (wie String-Vergleiche mit einer Zeit-Kontextvariable) kann zu unerwartetem Verhalten führen.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Hier ist ein Beispiel eines Kontextvariablen-Filters, der die Kontextvariable `product_name` mit dem Regex `/braze/` vergleicht.

![Ein Filter-Setup für die Kontextvariable „product_name“, um den Regex „/braze/“ abzugleichen.]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Vergleich mit Kontextvariablen oder angepassten Attributen {#comparing-to-context-variables-or-custom-attributes}

Durch Aktivieren des Umschalters **Compare to a context variable or custom attribute** können Sie Kontextvariablen-Filter erstellen, die mit zuvor definierten Kontextvariablen oder angepassten Nutzerattributen verglichen werden. Dies kann nützlich sein, um Vergleiche durchzuführen, die pro Nutzer:in dynamisch sind, wie API-getriggerter `context`, oder um komplexe Vergleichslogik zu verdichten, die über Kontextvariablen definiert ist.

{% tabs %}
{% tab Beispiel 1 %}

Nehmen wir an, Sie möchten eine personalisierte Erinnerung an Nutzer:innen nach einer dynamischen Inaktivitätsperiode senden. Alle, die sich in den letzten drei Tagen nicht in Ihre App eingeloggt haben, sollen eine Nachricht erhalten.

Sie haben eine Kontextvariable `re_engagement_date`, die als {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} definiert ist. Beachten Sie, dass `3 days` ein variabler Betrag sein kann, der auch als angepasstes Attribut einer Nutzer:in gespeichert ist. Wenn also das `re_engagement_date` nach dem `last_login_date` (als angepasstes Attribut im Nutzerprofil gespeichert) liegt, wird eine Nachricht gesendet.

![Ein Filter-Setup mit angepassten Attributen als Personalisierungstyp für die Kontextvariable „re_engagement_date“ nach dem angepassten Attribut „last_login_date“.]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Beispiel 2 %}

Der folgende Filter vergleicht die Kontextvariable `reminder_date` darauf, ob sie vor der Kontextvariable `appointment_deadline` liegt. Dies kann helfen, Nutzer:innen in einem Zielgruppenpfade-Schritt zu gruppieren, um zu bestimmen, ob sie zusätzliche Erinnerungen vor ihrer Terminfrist erhalten sollen.

![Ein Filter-Setup mit Kontextvariablen als Personalisierungstyp für die Kontextvariable „reminder_date“ auf die Kontextvariable „appointment_deadline“.]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Standardisierung der Zeitzonenkonsistenz {#time-zone-consistency-standardization}

Während die meisten Event-Eigenschaften, die den Zeitstempel-Typ verwenden, in Canvas bereits in UTC vorliegen, gibt es einige Ausnahmen. Mit der Einführung von Canvas-Kontext werden alle Standard-Zeitstempel-Event-Eigenschaften in aktionsbasierten Canvases konsistent in UTC sein. Diese Änderung ist Teil einer umfassenderen Maßnahme, um ein vorhersehbareres und konsistenteres Erlebnis beim Bearbeiten von Canvas-Schritten und Nachrichten zu gewährleisten. Beachten Sie, dass diese Änderung alle aktionsbasierten Canvases betrifft, unabhängig davon, ob das jeweilige Canvas einen Kontext-Schritt verwendet oder nicht.

{% alert important %}
Unter allen Umständen empfehlen wir dringend, [Liquid-time_zone-Filter]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/#things-to-know) zu verwenden, damit Zeitstempel in der gewünschten Zeitzone dargestellt werden. Ein Beispiel finden Sie in dieser [häufig gestellten Frage im Kontext-Schritt-Artikel]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/#faq-example).
{% endalert %}

## Verwandte Artikel {#related-articles}

- [Kontext-Schritt]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)
- [Personalisierung und dynamischer Content mit Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)