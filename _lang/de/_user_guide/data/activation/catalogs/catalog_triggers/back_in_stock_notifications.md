---
nav_title: „Wieder verfügbar“-Benachrichtigungen
article_title: „Wieder verfügbar“-Benachrichtigungen einrichten
page_order: 2
description: "Erfahren Sie, wie Sie mit Hilfe Ihres Katalogs und angepasster Events „Wieder verfügbar“-Benachrichtigungen einrichten, damit Kund:innen automatisch benachrichtigt werden, wenn ein Artikel wieder vorrätig ist."
---

# „Wieder verfügbar“-Benachrichtigungen {#back-in-stock-notifications}

> Erfahren Sie, wie Sie mit Hilfe Ihres Katalogs und angepasster Events „Wieder verfügbar“-Benachrichtigungen einrichten, damit Kund:innen automatisch benachrichtigt werden, wenn ein Artikel wieder vorrätig ist. Beachten Sie, dass dies nur für Nutzer:innen gilt, die sich bereits für Benachrichtigungen entschieden haben.

## So funktioniert es {#how-it-works}

Sie können ein angepasstes Event als Abo-Event einrichten, z. B. ein `product_clicked`-Event. Dieses Event muss eine Eigenschaft mit der Artikel-ID (Katalog-Artikel-IDs) enthalten. Wir empfehlen, einen Katalognamen anzugeben, dies ist jedoch nicht erforderlich. Außerdem geben Sie den Namen eines Felds für die Bestandsmenge an, das den Datentyp „Zahl“ haben muss.

Beachten Sie, dass der Bestand eines Katalogartikels null sein muss, damit Nutzer:innen ihn erfolgreich abonnieren können. Wenn ein Artikel eine Bestandsmenge größer als null hat, sucht Braze alle Nutzer:innen, die diesen Artikel abonniert haben, und sendet ein angepasstes Event, das Sie verwenden können, um eine Campaign oder ein Canvas zu triggern.

Die Event-Eigenschaften werden zusammen mit Ihren Nutzer:innen gesendet, sodass Sie die Artikeldetails per Template in die Campaign oder das Canvas einfügen können, die bzw. das versendet wird.

## Einrichten von Wieder-verfügbar-Benachrichtigungen {#setting-up-back-in-stock-notifications}

Befolgen Sie diese Schritte, um Wieder-verfügbar-Benachrichtigungen in einem bestimmten Katalog einzurichten.

1. Gehen Sie zu Ihrem Katalog und wählen Sie den Tab **Einstellungen** aus.
2. Wählen Sie den **Wieder verfügbar**-Toggle aus.
3. Wenn die globalen Wieder-verfügbar-Einstellungen noch nicht konfiguriert wurden, werden Sie aufgefordert, die angepassten Events und Eigenschaften einzurichten, die zum Triggern von Wieder-verfügbar-Benachrichtigungen verwendet werden:
    <br> ![Einstellungsbereich des Katalogs.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Fallback-Katalog** Dies ist der Katalog, der für das Wieder-verfügbar-Abo verwendet wird, wenn keine `catalog_name`-Eigenschaft im angepassten Event vorhanden ist.
    - **Angepasstes Event für Abos** ist das angepasste Braze-Event, das verwendet wird, um Nutzer:innen für Wieder-verfügbar-Benachrichtigungen zu abonnieren. Wenn dieses Event auftritt, wird die Person, die das Event ausgeführt hat, abonniert.
    - **Angepasstes Event zum Abmelden** ist das angepasste Braze-Event, das verwendet wird, um Nutzer:innen von Wieder-verfügbar-Benachrichtigungen abzumelden. Dieses Event ist optional. Wenn Nutzer:innen dieses Event nicht ausführen, werden sie nach 90 Tagen oder wenn das Wieder-verfügbar-Event ausgelöst wird, abgemeldet – je nachdem, was zuerst eintritt.
    - **Artikel-ID-Event-Eigenschaft** ist die Eigenschaft des weiter oben in diesem Abschnitt beschriebenen angepassten Events, die verwendet wird, um den Artikel für ein Wieder-verfügbar-Abo oder eine Abmeldung zu bestimmen. Diese Eigenschaft des angepassten Events sollte eine Artikel-ID (`id`) enthalten, die in einem Katalog vorhanden ist. Die Artikel-ID muss als String gesendet werden, damit sie mit dem `id`-Datentyp übereinstimmt, der im Zielkatalog gespeichert ist. Das angepasste Event sollte außerdem eine `catalog_name`-Eigenschaft enthalten, um anzugeben, in welchem Katalog sich dieser Artikel befindet.

    - Das folgende Beispiel zeigt ein angepasstes Event, das über die REST API gesendet wird:

```json
{
    "events": [
        {
            "external_id": "<external_id>",
            "name": "subscription",
            "time": "2024-04-15T19:22:28Z",
            "properties": {
                "id": "shirt-xl",
                "catalog_name": "on_sale_products",
                "type": ["back_in_stock"]
            }
        }
    ]
}
```

Um dasselbe Abo-Event mit den Braze SDKs zu tracken, verwenden Sie den folgenden Code:

{% tabs %}
{% tab Web SDK %}

```javascript
import { logCustomEvent } from "@braze/web-sdk";

logCustomEvent("subscription", {
  id: "shirt-xl",
  catalog_name: "on_sale_products",
  type: ["back_in_stock"]
});
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.logCustomEvent(
  name: "subscription",
  properties: [
    "id": "shirt-xl",
    "catalog_name": "on_sale_products",
    "type": ["back_in_stock"]
  ]
)
```

{% endtab %}
{% tab Android %}

```kotlin
Braze.getInstance(context).logCustomEvent(
  "subscription",
  BrazeProperties(
    JSONObject()
      .put("id", "shirt-xl")
      .put("catalog_name", "on_sale_products")
      .put("type", JSONArray().put("back_in_stock")),
  ),
)
```

{% endtab %}
{% endtabs %}

{% alert note %}
Wieder-verfügbar- und Preissenkung-Trigger verwenden dasselbe Event, um Nutzer:innen für die Benachrichtigung zu abonnieren. Sie können daher die `type`-Eigenschaft verwenden, um sowohl Preissenkung- als auch Wieder-verfügbar-Benachrichtigungen im selben Event festzulegen. Beachten Sie, dass die `type`-Eigenschaft ein Array sein muss.
{% endalert %}

{: start="4"}
4. Wählen Sie **Speichern** aus und fahren Sie mit der **Einstellungen**-Seite des Katalogs fort.
5. Legen Sie Ihre Benachrichtigungsregel fest. Es gibt zwei Optionen:
    - **Alle abonnierten Nutzer:innen benachrichtigen** benachrichtigt alle Kund:innen, die warten, wenn der Artikel wieder verfügbar ist.
    - **Benachrichtigungslimits festlegen** benachrichtigt eine bestimmte Anzahl von Kund:innen alle 10 Minuten. Braze benachrichtigt die angegebene Anzahl von Kund:innen in Schritten, bis keine weiteren Kund:innen mehr zu benachrichtigen sind oder bis der Artikel nicht mehr auf Lager ist. Ihre Benachrichtigungsrate darf 10.000 Nutzer:innen pro Minute nicht überschreiten.
6. Legen Sie das **Bestandsfeld im Katalog** fest. Dieses Katalogfeld wird verwendet, um zu bestimmen, ob der Artikel nicht auf Lager ist. Das Feld muss ein Zahlentyp sein.
7. Wählen Sie **Einstellungen speichern** aus.

![Katalogeinstellungen, die die aktivierte Wieder-verfügbar-Funktion zeigen. Die Benachrichtigungsregeln sehen vor, tausend Nutzer:innen alle zehn Minuten zu benachrichtigen.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
Benachrichtigungsregeln in diesen Einstellungen ersetzen nicht die Canvas-Benachrichtigungseinstellungen, wie z. B. Ruhezeiten.
{% endalert %}

## Wieder-auf-Lager-Benachrichtigungen in einem Canvas verwenden {#using-back-in-stock-notifications-in-a-canvas}

Nachdem Sie das Wieder-auf-Lager-Feature in einem Katalog eingerichtet haben, folgen Sie diesen Schritten, um es mit Canvas zu verwenden.

1. Richten Sie ein aktionsbasiertes Canvas ein.
2. Wählen Sie **Wieder auf Lager** als Trigger aus.
3. Wählen Sie den Namen des Katalogs mit den Wieder-auf-Lager-Benachrichtigungen aus.
4. Fahren Sie mit der [Einrichtung]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) Ihres Canvas wie gewohnt fort.

Jetzt können Ihre Kund:innen benachrichtigt werden, wenn ein Artikel wieder auf Lager ist.

### Liquid verwenden {#using-liquid}

Um Details über den Katalogartikel einzufügen, der wieder auf Lager ist, können Sie den `context`-Liquid-Tag verwenden, um auf die `item_id` zuzugreifen.

Mit {%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} wird die ID des Artikels zurückgegeben, der wieder auf Lager ist. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} gibt den Bestandswert des Artikels vor der Aktualisierung zurück, und {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} gibt den neuen Bestandswert nach der Aktualisierung zurück.

Verwenden Sie den Liquid-Tag {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} am Anfang Ihrer Nachricht und dann {%raw%}``{{ items[0].<field_name> }}``{%endraw%}, um in der gesamten Nachricht auf Daten zu diesem Artikel zuzugreifen.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Überlegungen {#considerations}

- Nutzer:innen sind nur 90 Tage lang abonniert. Wenn der Artikel nicht innerhalb von 90 Tagen wieder auf Lager ist, wird die Nutzerin bzw. der Nutzer abgemeldet.
- Bei Verwendung der Benachrichtigungsregel **Alle abonnierten Nutzer:innen benachrichtigen** benachrichtigt Braze 100.000 Nutzer:innen innerhalb von 10 Minuten.
- Braze unterstützt täglich bis zu 50.000 aktualisierte Artikel, die für das Auslösen von Wieder-auf-Lager-Benachrichtigungen infrage kommen. Sie können zu einem bestimmten Zeitpunkt bis zu 100 Millionen aktive Abos haben, wobei jedes Abo ein Nutzerprofil darstellt, das einen Katalogartikel beobachtet.