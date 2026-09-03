---
nav_title: Nutzeraktualisierung
article_title: Nutzeraktualisierung
alias: "/user_update/"
page_order: 12
page_type: reference
description: "Dieser Referenzartikel behandelt die Komponente Nutzeraktualisierung und wie Sie sie in Ihren Canvases verwenden können."
tool: Canvas
---

# Nutzeraktualisierung {#user-update}

> Mit der Komponente Nutzeraktualisierung können Sie Attribute, Events und Käufe von Nutzer:innen in einem JSON-Editor aktualisieren, sodass keine sensiblen Informationen wie API-Schlüssel angegeben werden müssen.

## So funktioniert diese Komponente {#how-this-component-works}

![Ein „Nutzer:innen aktualisieren“-Schritt mit dem Namen „Update loyalty“, der ein Attribut „Is Premium Member“ auf „true“ aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Wenn Sie diese Komponente in Ihrem Canvas verwenden, werden die Aktualisierungen nicht auf das Rate-Limit für `/users/track`-Anfragen pro Minute angerechnet. Stattdessen werden diese Aktualisierungen gebündelt, damit Braze sie effizienter verarbeiten kann als über einen Braze-zu-Braze-Webhook. Beachten Sie, dass diese Komponente keine [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points) protokolliert, wenn sie zum Aktualisieren nicht abrechenbarer Datenpunkte verwendet wird (z. B. Abo-Gruppen).

Nachdem Nutzer:innen den „Nutzer:innen aktualisieren“-Schritt erreicht haben und die Verarbeitung abgeschlossen ist, werden sie zum nächsten Schritt weitergeleitet. Das bedeutet, dass alle nachfolgenden Nachrichten, die auf diesen Aktualisierungen basieren, auf dem neuesten Stand sind, wenn der nächste Schritt ausgeführt wird.

## Nutzer:innen-Update erstellen {#creating-a-user-update}

Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand der Variante oder des Schritts und wählen Sie **User Update**.

Es gibt drei Optionen, mit denen Sie bestehende Nutzerprofilinformationen aktualisieren, neue Informationen hinzufügen oder Nutzerprofilinformationen entfernen können. Zusammengenommen können die User-Update-Schritte in einem Workspace bis zu 200.000 Nutzerprofile pro Minute aktualisieren.

{% alert tip %}
Sie können die mit dieser Komponente vorgenommenen Änderungen auch testen, indem Sie nach einer/einem Nutzer:in suchen und die Änderung auf sie/ihn anwenden. Dadurch wird die/der Nutzer:in aktualisiert.
{% endalert %}

## Angepasste Attribute aktualisieren {#updating-custom-attributes}

Um ein angepasstes Attribut zu aktualisieren oder zu entfernen, wählen Sie einen Attributnamen aus Ihrer Liste der Attribute aus und geben Sie den Wert ein.

![User-Update-Schritt, der die beiden Attribute „Loyalty Member“ und „Loyalty Program“ auf „true“ aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Angepasste Attribute entfernen {#removing-custom-attributes}

Um ein angepasstes Attribut zu entfernen, wählen Sie über das Dropdown-Menü einen Attributnamen aus. Sie können zum [erweiterten JSON-Editor](#advanced-json-editor) wechseln, um weitere Bearbeitungen vorzunehmen.

![Canvas-Schritt „Nutzer:innen-Update“, der das Attribut „Loyalty Member“ entfernt.]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Werte erhöhen und verringern {#increasing-and-decreasing-values}

Der Canvas-Schritt „Nutzer:innen-Update“ kann einen Attributwert erhöhen oder verringern. Wählen Sie das Attribut aus, wählen Sie **Increment By** oder **Decrement By** und geben Sie eine Zahl ein.

#### Wöchentlichen Fortschritt verfolgen {#track-weekly-progress}

Durch das Inkrementieren eines angepassten Attributs, das ein Event erfasst, können Sie die Anzahl der Kurse verfolgen, die Nutzer:innen in einer Woche besucht haben. Mithilfe dieser Komponente kann die Kursanzahl zu Beginn der Woche zurückgesetzt und das Tracking erneut gestartet werden.

![Canvas-Schritt „Nutzer:innen-Update“, der das Attribut „class_count“ um eins erhöht.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Ein Array von Objekten aktualisieren {#updating-an-array-of-objects}

Ein [Array von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) ist ein datenreiches angepasstes Attribut, das im Profil von Nutzer:innen gespeichert wird. Sie können es verwenden, um einen Verlauf der Interaktionen von Nutzer:innen mit Ihrer Marke zu erstellen und Segmente basierend auf einem berechneten Feld wie Kaufhistorie oder Gesamt-LTV zu erstellen.

Mit der Option **Advanced JSON Editor** können Sie JSON einfügen, um Elemente zu diesem Array von Objekten hinzuzufügen oder daraus zu entfernen.

#### Anwendungsfall: Wunschliste von Nutzer:innen aktualisieren {#use-case-updating-a-users-wishlist}

Verfolgen Sie die Wunschliste von Nutzer:innen, damit Sie basierend auf den gespeicherten Artikeln segmentieren oder personalisieren können.

1. Erstellen Sie ein angepasstes Attribut, das ein Array von Objekten ist, zum Beispiel `wishlist`. Jedes Objekt kann Felder wie `product_id`, `product_name` und `added_at` enthalten.
2. Wählen Sie im Canvas-Schritt „Nutzer:innen-Update“ die Option **Advanced JSON Editor**. Verwenden Sie dann im Abschnitt **Compose** die Operation `$add`, um ein Element hinzuzufügen, oder die Operation `$remove`, um ein Element nach Wert zu entfernen.

Im Folgenden finden Sie ein Beispiel für das Hinzufügen eines Artikels zur Wunschliste:

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

Um einen Artikel zu entfernen, verwenden Sie `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` mit derselben Objektstruktur, damit Braze ihn zuordnen und entfernen kann.

#### Anwendungsfall: Gesamtbetrag des Warenkorbs berechnen {#use-case-calculating-the-shopping-cart-total}

Verfolgen Sie, wann Nutzer:innen Artikel in ihrem Warenkorb haben, wann sie neue Artikel hinzufügen oder entfernen und wie hoch der Gesamtwert des Warenkorbs ist.

1. Erstellen Sie ein angepasstes Array von Objekten namens `shopping_cart`. Das folgende Beispiel zeigt, wie dieses Attribut aussehen könnte. Jeder Artikel hat eine eindeutige `product_id`, die zusätzliche Daten in einem eigenen verschachtelten Array von Objekten enthält, einschließlich `price`.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2. Erstellen Sie ein [angepasstes Event]({{site.baseurl}}/user_guide/data/activation/events/custom_events) namens `add_item_to_cart`, das protokolliert wird, wenn Nutzer:innen einen Artikel in den Warenkorb legen.
3. Erstellen Sie einen Canvas, der auf Nutzer:innen abzielt, die dieses angepasste Event ausführen. Wenn Nutzer:innen nun einen Artikel in ihren Warenkorb legen, wird dieser Canvas ausgelöst. Sie können dann Nachrichten direkt an diese Nutzer:innen senden und beispielsweise Gutscheincodes anbieten, wenn sie einen bestimmten Betrag erreicht haben, ihren Warenkorb für eine bestimmte Zeit verlassen haben oder andere Szenarien, die zu Ihrem Anwendungsfall passen.

Das Attribut `shopping_cart` enthält die Summe vieler angepasster Events: die Gesamtkosten aller Artikel, die Gesamtanzahl der Artikel im Warenkorb, ob der Warenkorb ein Geschenk enthält und vieles mehr. Das kann in etwa wie folgt aussehen:

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"],
         "gift": true,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Canvas-Entry-Eigenschaft als Attribut festlegen {#setting-canvas-entry-property-as-an-attribute}

Sie können den Schritt „Nutzer:innen-Update“ verwenden, um eine `canvas_entry_property` persistent zu speichern. Nehmen wir an, Sie haben ein Event, das ausgelöst wird, wenn ein Artikel zu einem Warenkorb hinzugefügt wird. Sie können die ID des zuletzt hinzugefügten Artikels speichern und für eine Remarketing-Campaign verwenden. Nutzen Sie das Personalisierungs-Feature, um eine Canvas-Entry-Eigenschaft abzurufen und in einem Attribut zu speichern.

![Schritt „Nutzer:innen-Update“, der das Attribut „most_recent_cart_item“ mit einer Artikel-ID aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalisierung {#personalization}

Um die Eigenschaft des Trigger-Events für einen Canvas als Attribut zu speichern, verwenden Sie das Personalisierungs-Modal, um die Canvas-Entry-Eigenschaft zu extrahieren und zu speichern. Das Nutzer:innen-Update unterstützt außerdem die folgenden Personalisierungs-Features:

* [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
* [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
* [Entry-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties)
* Liquid-Logik (einschließlich [Abbruch von Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages))
* Mehrere Attribut- oder Event-Aktualisierungen pro Objekt

{% alert warning %}
Wir empfehlen, die Connected-Content-Liquid-Personalisierung in Schritten des Typs „Nutzer:innen-Update“ mit Bedacht einzusetzen, da dieser Schritttyp ein Rate-Limit von 200.000 Anfragen pro Minute hat. Dieses Rate-Limit überschreibt das Canvas-Rate-Limit.
{% endalert %}

## Erweiterter JSON-Editor {#advanced-json-editor}

Fügen Sie dem JSON-Editor ein Attribut-, Event- oder Kauf-JSON-Objekt mit bis zu 65.536 Zeichen hinzu. Der [globale Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) und der Status der [Abo-Gruppe]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups) einer Nutzer:in können ebenfalls festgelegt werden.

![Fügen Sie dem JSON-Editor ein Attribut-, Event- oder Kauf-JSON-Objekt mit bis zu 65.536 Zeichen hinzu. Der globale Abo-Status und der Status der Abo-Gruppe einer Nutzer:in können ebenfalls festgelegt werden.]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Mit dem JSON-Editor können Sie auch im Tab **Preview and test** eine Vorschau anzeigen und testen, ob das Kundenprofil mit Ihren Änderungen aktualisiert wird. Sie können entweder eine zufällige Nutzer:in auswählen oder nach einer bestimmten Nutzer:in suchen. Sehen Sie sich dann nach dem Senden eines Tests an eine Nutzer:in das Kundenprofil über den generierten Link an.

![Mit dem JSON-Editor können Sie auch im Tab „Preview and test“ eine Vorschau anzeigen und testen, ob das Kundenprofil mit Ihren Änderungen aktualisiert wird. Sie können entweder eine zufällige Nutzer:in auswählen oder nach einer bestimmten Nutzer:in suchen. Sehen Sie sich dann nach dem Senden eines Tests an eine Nutzer:in das Kundenprofil über den generierten Link an.]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Hinweise {#considerations}

Sie müssen bei der Verwendung des JSON-Editors keine sensiblen Daten wie Ihren API-Schlüssel angeben, da dieser automatisch von der Plattform bereitgestellt wird. Die folgenden Felder sollten nicht im JSON-Editor enthalten sein:
* Externe Nutzer-ID
* API-Schlüssel
* Braze-Cluster-URL
* Felder im Zusammenhang mit Push-Token-Importen

{% alert important %}
Canvas-Eigenschaften (wie die Liquid-Tags `canvas_id`, `canvas_name` und `canvas_variant_name`) werden in Nutzeraktualisierungsschritten nicht unterstützt.
{% endalert %}

{% raw %}
### Angepasste Events protokollieren {#log-custom-events}

Mit dem JSON-Editor können Sie auch angepasste Events protokollieren. Beachten Sie, dass hierfür ein Zeitstempel im ISO-Format erforderlich ist, sodass zunächst eine Zuweisung von Uhrzeit und Datum mit Liquid erfolgen muss. Betrachten Sie dieses Beispiel, das ein Event mit einer Zeitangabe protokolliert.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

Das nächste Beispiel verknüpft ein Event mit einer bestimmten App unter Verwendung eines angepassten Events mit optionalen Eigenschaften und der `app_id`.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### Abo-Status bearbeiten {#edit-subscription-state}

Im JSON-Editor können Sie auch den Abo-Status einer Nutzer:in bearbeiten. Das folgende Beispiel zeigt, wie der Abo-Status einer Nutzer:in auf `opted_in` aktualisiert wird.

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Abo-Gruppen aktualisieren {#update-subscription-groups}

Sie können Abo-Gruppen auch mit diesem Canvas-Schritt aktualisieren. Das folgende Beispiel zeigt, wie eine oder mehrere Abo-Gruppen aktualisiert werden.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}