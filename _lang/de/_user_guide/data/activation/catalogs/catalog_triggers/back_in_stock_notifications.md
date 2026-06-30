---
nav_title: „Wieder verfügbar“-Benachrichtigungen
article_title: „Wieder verfügbar“-Benachrichtigungen einrichten
page_order: 2
description: "Erfahren Sie, wie Sie mit Hilfe Ihres Katalogs und angepasster Events „Wieder verfügbar“-Benachrichtigungen einrichten, damit Kund:innen automatisch benachrichtigt werden, wenn ein Artikel wieder vorrätig ist."
---

# „Wieder verfügbar“-Benachrichtigungen {#back-in-stock-notifications}

> Erfahren Sie, wie Sie mit Hilfe Ihres Katalogs und angepasster Events „Wieder verfügbar“-Benachrichtigungen einrichten, damit Kund:innen automatisch benachrichtigt werden, wenn ein Artikel wieder vorrätig ist. Beachten Sie, dass dies nur für Nutzer:innen gilt, die sich bereits für Benachrichtigungen entschieden haben.

## Funktionsweise {#how-it-works}

Sie können ein angepasstes Event als Abo-Event einrichten, z. B. ein `product_clicked`-Event. Dieses Event muss eine Eigenschaft mit der Artikel-ID enthalten (Katalogartikel-IDs). Wir empfehlen, einen Katalognamen anzugeben, dies ist jedoch nicht erforderlich. Außerdem müssen Sie den Namen eines Bestandsmengenfelds angeben, das vom Datentyp „Zahl“ sein muss.

Beachten Sie, dass der Bestand eines Katalogartikels auf Null stehen muss, damit ein:e Nutzer:in diesen Artikel erfolgreich abonnieren kann. Wenn ein Artikel eine Bestandsmenge größer als Null hat, sucht Braze alle Nutzer:innen, die diesen Artikel abonniert haben, und sendet ein angepasstes Event, das Sie zum Triggern einer Campaign oder eines Canvas verwenden können.

Die Event-Eigenschaften werden zusammen mit den Nutzerdaten gesendet, sodass Sie die Artikeldetails als Template in die Campaign oder das Canvas einfügen können.

## „Wieder verfügbar“-Benachrichtigungen einrichten {#setting-up-back-in-stock-notifications}

Führen Sie die folgenden Schritte aus, um „Wieder verfügbar“-Benachrichtigungen in einem bestimmten Katalog einzurichten.

1. Gehen Sie zu Ihrem Katalog und wählen Sie den Tab **Einstellungen**.
2. Wählen Sie den Schalter **Back in stock**.
3. Wenn die globalen „Wieder verfügbar“-Einstellungen noch nicht konfiguriert wurden, werden Sie aufgefordert, die angepassten Events und Eigenschaften einzurichten, die zum Auslösen von „Wieder verfügbar“-Benachrichtigungen verwendet werden:
    <br> ![Katalogeinstellungen.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **Fallback-Katalog** Dies ist der Katalog, der für das „Wieder verfügbar“-Abo verwendet wird, wenn die Eigenschaft `catalog_name` im angepassten Event nicht vorhanden ist.
    - **Angepasstes Event für Abos** ist das angepasste Braze-Event, mit dem ein:e Nutzer:in für „Wieder verfügbar“-Benachrichtigungen registriert wird. Wenn dieses Event eintritt, wird die Person, die das Event ausgeführt hat, abonniert.
    - **Angepasstes Event zum Abmelden** ist das angepasste Braze-Event, mit dem ein:e Nutzer:in von „Wieder verfügbar“-Benachrichtigungen abgemeldet wird. Dieses Event ist optional. Wenn die Person dieses Event nicht ausführt, wird sie nach 90 Tagen oder wenn das „Wieder verfügbar“-Event ausgelöst wird, abgemeldet – je nachdem, was zuerst eintritt.
    - **Artikel-ID-Event-Eigenschaft** ist die Eigenschaft des oben genannten angepassten Events, die verwendet wird, um den Artikel für ein „Wieder verfügbar“-Abo oder eine Abmeldung zu bestimmen. Diese Eigenschaft des angepassten Events sollte eine Artikel-ID (`id`) enthalten, die in einem Katalog vorhanden ist. Die Artikel-ID muss als String gesendet werden, damit sie mit dem im Zielkatalog gespeicherten Datentyp `id` übereinstimmt. Das angepasste Event sollte außerdem eine `catalog_name`-Eigenschaft enthalten, um anzugeben, in welchem Katalog sich dieser Artikel befindet.

    - Ein Beispiel für ein angepasstes Event könnte wie folgt aussehen:

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

{% alert note %}
Back-in-Stock- und Price-Drop-Trigger verwenden dasselbe Event, um Nutzer:innen für die Benachrichtigung zu abonnieren. Sie können also die Eigenschaft `type` verwenden, um sowohl Price-Drop- als auch Back-in-Stock-Benachrichtigungen im selben Event einzurichten. Beachten Sie, dass die Eigenschaft `type` ein Array sein muss.
{% endalert %}

{: start="4"}
4. Wählen Sie **Save** und fahren Sie mit der Seite **Einstellungen** des Katalogs fort.
5. Legen Sie Ihre Benachrichtigungsregel fest. Es gibt zwei Optionen:
    - **Alle abonnierten Nutzer:innen benachrichtigen** benachrichtigt alle Kund:innen, die warten, wenn der Artikel wieder vorrätig ist.
    - **Benachrichtigungslimits festlegen** benachrichtigt eine bestimmte Anzahl von Kund:innen pro konfiguriertem Benachrichtigungszeitraum. Braze benachrichtigt die angegebene Anzahl von Kund:innen schrittweise, bis keine Kund:innen mehr zu benachrichtigen sind oder bis der Artikel nicht mehr vorrätig ist. Ihre Benachrichtigungsrate darf 10.000 Nutzer:innen pro Minute nicht überschreiten.
6. Legen Sie das **Bestandsfeld im Katalog** fest. Dieses Katalogfeld wird verwendet, um festzustellen, ob der Artikel nicht vorrätig ist. Das Feld muss vom Typ „Zahl“ sein.
7. Wählen Sie **Einstellungen speichern**.

![Katalogeinstellungen, in denen das Feature „Wieder verfügbar“ aktiviert ist. Die Benachrichtigungsregeln sehen vor, dass alle zehn Minuten tausend Nutzer:innen benachrichtigt werden.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
Die Benachrichtigungsregeln in diesen Einstellungen ersetzen nicht die Canvas-Benachrichtigungseinstellungen, wie z. B. Ruhezeiten.
{% endalert %}

## „Wieder verfügbar“-Benachrichtigungen in einem Canvas verwenden {#using-back-in-stock-notifications-in-a-canvas}

Nachdem Sie das Feature „Wieder verfügbar“ in einem Katalog eingerichtet haben, führen Sie die folgenden Schritte aus, um es mit Canvas zu verwenden.

1. Richten Sie einen aktionsbasierten Canvas ein.
2. Wählen Sie **Back in stock** als Trigger.
3. Wählen Sie den Namen des Katalogs mit den „Wieder verfügbar“-Benachrichtigungen.
4. Fahren Sie mit der [Einrichtung]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) Ihres Canvas fort, wie gewohnt.

Jetzt können Ihre Kund:innen benachrichtigt werden, wenn ein Artikel wieder vorrätig ist.

### Liquid verwenden {#using-liquid}

Um Details zum wieder verfügbaren Katalogartikel als Template einzufügen, können Sie den `context`-Liquid-Tag verwenden, um auf die `item_id` zuzugreifen.

{%raw%}``{{context.${catalog_update}.item_id}}``{%endraw%} gibt die ID des Artikels zurück, der wieder vorrätig ist. {%raw%}``{{context.${catalog_update}.previous_value}}``{%endraw%} gibt den Bestandswert des Artikels vor dem Update zurück, und {%raw%}``{{context.${catalog_update}.new_value}}``{%endraw%} gibt den neuen Bestandswert nach dem Update zurück.

Verwenden Sie den Liquid-Tag {%raw%}``{% catalog_items <name_of_your_catalog> {{context.${catalog_update}.item_id}} %}``{%endraw%} am Anfang Ihrer Nachricht und nutzen Sie anschließend {%raw%}``{{ items[0].<field_name> }}``{%endraw%}, um in der gesamten Nachricht auf Daten zu diesem Artikel zuzugreifen.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}

## Hinweise {#considerations}

- Nutzer:innen werden nur für 90 Tage abonniert. Wenn der Artikel nicht innerhalb von 90 Tagen wieder vorrätig ist, werden sie abgemeldet.
- Bei Verwendung der Benachrichtigungsregel **Alle abonnierten Nutzer:innen benachrichtigen** benachrichtigt Braze 100.000 Nutzer:innen innerhalb von 10 Minuten.
- Braze unterstützt bis zu 50.000 aktualisierte Artikel pro Tag, die für das Auslösen von „Wieder verfügbar“-Benachrichtigungen infrage kommen. Es können bis zu 100 Millionen aktive Abos gleichzeitig bestehen, wobei jedes Abo ein Nutzerprofil darstellt, das einen Katalogartikel beobachtet.