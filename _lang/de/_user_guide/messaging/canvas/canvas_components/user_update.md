---
nav_title: Nutzeraktualisierung
article_title: Nutzeraktualisierung
alias: "/user_update/"
page_order: 12
page_type: reference
description: "Dieser Referenzartikel behandelt die Komponente Nutzeraktualisierung und wie Sie sie in Ihren Canvases verwenden können."
tool: Canvas
---

# Nutzeraktualisierung

> Mit der Komponente Nutzeraktualisierung können Sie Attribute, Events und Käufe von Nutzer:innen in einem JSON-Editor aktualisieren, sodass keine sensiblen Informationen wie API-Schlüssel angegeben werden müssen.

## Funktionsweise dieser Komponente

![Ein Nutzeraktualisierungs-Schritt namens „Update loyalty", der ein Attribut „Is Premium Member" auf „true" aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Wenn Sie diese Komponente in Ihrem Canvas verwenden, werden die Aktualisierungen nicht auf Ihr Rate-Limit für `/users/track`-Anfragen pro Minute angerechnet. Stattdessen werden diese Aktualisierungen gebündelt, damit Braze sie effizienter verarbeiten kann als einen Braze-zu-Braze-Webhook. Beachten Sie, dass diese Komponente keine [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) protokolliert, wenn sie zur Aktualisierung nicht abrechnungspflichtiger Datenpunkte verwendet wird (z. B. Abo-Gruppen).

Nachdem Nutzer:innen den Nutzeraktualisierungs-Schritt erreicht haben und die Verarbeitung abgeschlossen ist, werden sie zum nächsten Schritt weitergeleitet. Das bedeutet, dass alle nachfolgenden Nachrichten, die auf diesen Nutzeraktualisierungen basieren, auf dem neuesten Stand sind, wenn der nächste Schritt ausgeführt wird.

## Eine Nutzeraktualisierung erstellen

Ziehen Sie die Komponente per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand der Variante oder des Schritts und wählen Sie **Nutzeraktualisierung**.

Es gibt drei Optionen, mit denen Sie bestehende Nutzerprofil-Informationen aktualisieren, neue Informationen hinzufügen oder Nutzerprofil-Informationen entfernen können. Zusammengenommen können die Nutzeraktualisierungs-Schritte in einem Workspace bis zu 200.000 Nutzerprofile pro Minute aktualisieren.

{% alert tip %}
Sie können die mit dieser Komponente vorgenommenen Änderungen auch testen, indem Sie nach einer/einem Nutzer:in suchen und die Änderung auf sie/ihn anwenden. Dadurch wird das Nutzerprofil aktualisiert.
{% endalert %}

## Angepasste Attribute aktualisieren

Um ein angepasstes Attribut zu aktualisieren oder zu entfernen, wählen Sie einen Attributnamen aus Ihrer Attributliste und geben Sie den Wert ein.

![Nutzeraktualisierungs-Schritt, der die beiden Attribute „Loyalty Member" und „Loyalty Program" auf „true" aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Angepasste Attribute entfernen

Um ein angepasstes Attribut zu entfernen, wählen Sie einen Attributnamen über das Dropdown-Menü aus. Sie können zum [erweiterten JSON-Editor](#advanced-json-editor) wechseln, um weitere Bearbeitungen vorzunehmen.

![Nutzeraktualisierungs-Schritt, der ein Attribut „Loyalty Member" entfernt.]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Werte erhöhen und verringern

Der Nutzeraktualisierungs-Schritt kann einen Attributwert erhöhen oder verringern. Wählen Sie das Attribut aus, wählen Sie **Increment By** oder **Decrement By** und geben Sie eine Zahl ein.

#### Wöchentlichen Fortschritt verfolgen

Indem Sie ein angepasstes Attribut inkrementieren, das ein Event verfolgt, können Sie die Anzahl der Kurse nachverfolgen, die ein:e Nutzer:in in einer Woche besucht hat. Mit dieser Komponente kann der Kurszähler zu Beginn der Woche zurückgesetzt werden und das Tracking erneut beginnen.

![Nutzeraktualisierungs-Schritt, der das Attribut „class_count" um eins erhöht.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Ein Array von Objekten aktualisieren

Ein [Array von Objekten]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects/) ist ein datenreiches angepasstes Attribut, das im Profil von Nutzer:innen gespeichert wird. Sie können es verwenden, um einen Verlauf der Interaktionen von Nutzer:innen mit Ihrer Marke zu erstellen und Segmente basierend auf einem berechneten Feld zu erstellen, z. B. Kaufhistorie oder gesamter Lifetime-Value.

Mit der Option **Advanced JSON Editor** können Sie JSON einfügen, um Elemente zu diesem Array von Objekten hinzuzufügen oder daraus zu entfernen.

#### Anwendungsfall: Wunschliste von Nutzer:innen aktualisieren

Verfolgen Sie die Wunschliste von Nutzer:innen, um basierend auf ihren gespeicherten Artikeln zu segmentieren oder zu personalisieren.

1. Erstellen Sie ein angepasstes Attribut, das ein Array von Objekten ist, z. B. `wishlist`. Jedes Objekt kann Felder wie `product_id`, `product_name` und `added_at` enthalten.
2. Wählen Sie im Nutzeraktualisierungs-Schritt **Advanced JSON Editor**. Verwenden Sie dann im Abschnitt **Verfassen** die Operation `$add`, um ein Element hinzuzufügen, oder die Operation `$remove`, um ein Element nach Wert zu entfernen.

Das folgende Beispiel zeigt das Hinzufügen eines Elements zur Wunschliste:

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

Um ein Element zu entfernen, verwenden Sie `"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }` mit derselben Objektstruktur, damit Braze es zuordnen und entfernen kann.

#### Anwendungsfall: Warenkorb-Gesamtbetrag berechnen

Verfolgen Sie, wann Nutzer:innen Artikel in ihrem Warenkorb haben, wann sie neue Artikel hinzufügen oder entfernen und wie hoch der Gesamtwert des Warenkorbs ist.

1. Erstellen Sie ein angepasstes Array von Objekten namens `shopping_cart`. Das folgende Beispiel zeigt, wie dieses Attribut aussehen kann. Jeder Artikel hat eine eindeutige `product_id` mit zusätzlichen Daten in einem eigenen verschachtelten Array von Objekten, einschließlich `price`.

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
2. Erstellen Sie ein [angepasstes Event]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) namens `add_item_to_cart`, das protokolliert wird, wenn ein:e Nutzer:in einen Artikel in den Warenkorb legt.
3. Erstellen Sie ein Canvas, das Nutzer:innen anspricht, die dieses angepasste Event ausführen. Wenn nun ein:e Nutzer:in einen Artikel in den Warenkorb legt, wird dieses Canvas getriggert. Sie können dann Nachrichten direkt an diese:n Nutzer:in senden, z. B. Gutscheincodes anbieten, wenn ein bestimmter Betrag erreicht wurde, der Warenkorb für eine bestimmte Zeit verlassen wurde, oder alles andere, was zu Ihrem Anwendungsfall passt.

Das Attribut `shopping_cart` enthält die Summe vieler angepasster Events: die Gesamtkosten aller Artikel, die Gesamtanzahl der Artikel im Warenkorb, ob der Warenkorb ein Geschenk enthält und so weiter. Das kann etwa so aussehen:

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

## Canvas-Eingangs-Eigenschaft als Attribut festlegen

Sie können den Nutzeraktualisierungs-Schritt verwenden, um eine `canvas_entry_property` zu speichern. Angenommen, Sie haben ein Event, das ausgelöst wird, wenn ein Artikel in den Warenkorb gelegt wird. Sie können die ID des zuletzt hinzugefügten Artikels speichern und für eine Remarketing-Kampagne verwenden. Nutzen Sie die Personalisierungsfunktion, um eine Canvas-Eingangs-Eigenschaft abzurufen und in einem Attribut zu speichern.

![Nutzeraktualisierungs-Schritt, der das Attribut „most_recent_cart_item" mit einer Artikel-ID aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalisierung

Um die Eigenschaft des Trigger-Events für ein Canvas als Attribut zu speichern, verwenden Sie das Personalisierungs-Modal, um die Canvas-Eingangs-Eigenschaft zu extrahieren und zu speichern. Die Nutzeraktualisierung unterstützt außerdem die folgenden Personalisierungsfunktionen:

* [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)
* [Content-Blöcke]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)
* [Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/)
* Liquid-Logik (einschließlich [Abbruch von Nachrichten]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/))
* Mehrere Attribut- oder Event-Aktualisierungen pro Objekt

{% alert warning %}
Wir empfehlen, Connected-Content-Liquid-Personalisierung in Nutzeraktualisierungs-Schritten mit Bedacht einzusetzen, da dieser Schritttyp ein Rate-Limit von 200.000 Anfragen pro Minute hat. Dieses Rate-Limit überschreibt das Canvas-Rate-Limit.
{% endalert %}

## Erweiterter JSON-Editor

Fügen Sie ein Attribut-, Event- oder Kauf-JSON-Objekt mit bis zu 65.536 Zeichen zum JSON-Editor hinzu. Der [globale Abo-Status]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states) und der Status der [Abo-Gruppe]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) von Nutzer:innen können ebenfalls festgelegt werden.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Mit dem JSON-Editor können Sie auch eine Vorschau anzeigen und testen, ob das Nutzerprofil mit Ihren Änderungen aktualisiert wird – im Tab **Preview and test**. Sie können entweder eine:n zufällige:n Nutzer:in auswählen oder nach einer/einem bestimmten Nutzer:in suchen. Nachdem Sie einen Test an eine:n Nutzer:in gesendet haben, können Sie das Nutzerprofil über den generierten Link anzeigen.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Hinweise

Sie müssen bei der Verwendung des JSON-Editors keine sensiblen Daten wie Ihren API-Schlüssel angeben, da dieser automatisch von der Plattform bereitgestellt wird. Die folgenden Felder sollten nicht im JSON-Editor enthalten sein:
* Externe Nutzer-ID
* API-Schlüssel
* Braze-Cluster-URL
* Felder im Zusammenhang mit Push-Token-Importen

{% alert important %}
Canvas-Eigenschaften (wie die Liquid-Tags `canvas_id`, `canvas_name` und `canvas_variant_name`) werden in Nutzeraktualisierungs-Schritten nicht unterstützt.
{% endalert %}

{% raw %}
### Angepasste Events protokollieren

Mit dem JSON-Editor können Sie auch angepasste Events protokollieren. Beachten Sie, dass hierfür ein Zeitstempel im ISO-Format erforderlich ist, sodass zunächst eine Zeit- und Datumszuweisung mit Liquid erfolgen muss. Betrachten Sie dieses Beispiel, das ein Event mit einer Zeitangabe protokolliert.

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

### Abo-Status bearbeiten

Im JSON-Editor können Sie auch den Abo-Status von Nutzer:innen bearbeiten. Das folgende Beispiel zeigt, wie der Abo-Status auf `opted_in` aktualisiert wird.

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Abo-Gruppen aktualisieren

Sie können Abo-Gruppen auch mit diesem Canvas-Schritt aktualisieren. Das folgende Beispiel zeigt, wie Sie eine oder mehrere Abo-Gruppen aktualisieren.

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