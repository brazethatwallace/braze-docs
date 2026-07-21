---
nav_title: Array von Objekten
article_title: Array von Objekten
alias: "/array_of_objects/"
page_order: 2
page_type: reference
description: "Dieser Referenzartikel behandelt die Verwendung eines Arrays von Objekten als Datentyp für angepasste Attribute, einschließlich Einschränkungen und Anwendungsbeispielen."
---

# Array von Objekten {#array-of-objects}

> Auf dieser Seite erfahren Sie, wie Sie ein Array von Objekten verwenden können, um verwandte Attribute zu gruppieren. Sie können z. B. eine Gruppe von Haustierobjekten, Liedobjekten und Kontoobjekten haben, die alle zu einer Nutzer:in gehören. Diese Arrays von Objekten können verwendet werden, um Ihr Messaging mit Liquid zu personalisieren oder Zielgruppen-Segmente zu erstellen, wenn irgendein Element innerhalb eines Objekts den Kriterien entspricht.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Hinweise {#considerations}

- Arrays von Objekten sind für angepasste Attribute vorgesehen, die über die API gesendet werden. CSV-Uploads werden nicht unterstützt. Das liegt daran, dass Kommas in der CSV-Datei als Spaltentrennzeichen interpretiert werden und Kommas in Werten zu Parsing-Fehlern führen.
- Arrays von Objekten haben keine Begrenzung der Anzahl von Elementen, aber eine maximale Größe von 100&nbsp;KB. Wenn ein Update (z.&nbsp;B. `$add` oder `$update`) dazu führt, dass das Array dieses Limit überschreitet, verwirft Braze das Update und das Attribut bleibt unverändert. Die API-Anfrage gibt dennoch eine Erfolgsantwort zurück. Um das Array unter dem Limit zu halten, damit neue Elemente hinzugefügt werden können, verwenden Sie `$remove`, um zuerst Elemente aus dem Array zu löschen.
- Nicht alle Braze-Partner unterstützen Arrays von Objekten. Lesen Sie die [Partner-Dokumentation]({{site.baseurl}}/partners/home), um zu prüfen, ob die Integration dieses Feature unterstützt.

Das Aktualisieren oder Entfernen von Elementen in einem Array erfordert die Identifizierung des Elements anhand von Schlüssel und Wert. Erwägen Sie daher, jedem Element im Array einen eindeutigen Bezeichner hinzuzufügen. Die Eindeutigkeit bezieht sich nur auf das Array und ist nützlich, wenn Sie bestimmte Objekte aus Ihrem Array aktualisieren und entfernen möchten. Dies wird von Braze nicht erzwungen.

{% alert important %}
Wenn ein verschachteltes angepasstes Attribut in Ihrer Anfrage ungültige Werte enthält (z.&nbsp;B. ungültige Zeitformate oder `null`-Werte), verwirft Braze alle Updates verschachtelter angepasster Attribute in der Anfrage. Dies gilt für alle verschachtelten Strukturen innerhalb dieses spezifischen Attributs. Stellen Sie sicher, dass alle Werte innerhalb verschachtelter angepasster Attribute gültig sind, bevor Sie sie senden. Weitere Informationen finden Sie unter [Nutzer:innen erstellen und aktualisieren]({{site.baseurl}}/api/endpoints/user_data/post_user_track#how-does-userstrack-handle-invalid-nested-custom-attributes).
{% endalert %}

{% alert tip %}
Weitere Informationen zur Verwendung von Arrays von Objekten für Nutzerattribut-Objekte finden Sie unter [Nutzerattribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens).
{% endalert %}

## API-Beispiel {#api-example}

Verwenden Sie diese Beispiele, wenn Sie `/users/track`-Anfragen senden, die verschachtelte angepasste Attribute erstellen oder aktualisieren, die als Arrays von Objekten gespeichert sind. Der Payload verwendet die Operatoren `$add`, `$remove` und `$update`, sodass Sie bestimmte Objekte ändern können, ohne bei jeder Anfrage das gesamte Array neu aufzubauen.

{% tabs local %}
{% tab Erstellen %}

Das Folgende ist ein `/users/track`-Beispiel mit einem `pets`-Array. Um die Eigenschaften der Haustiere zu erfassen, senden Sie eine API-Anfrage, die `pets` als Array von Objekten auflistet. Beachten Sie, dass jedem Objekt eine eindeutige `id` zugewiesen wurde, auf die später bei Updates verwiesen werden kann.

Verwenden Sie dieses Format, wenn Sie das Attribut zum ersten Mal erstellen oder das gesamte Array durch einen neuen Basissatz von Objekten ersetzen möchten.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Hinzufügen %}

Fügen Sie dem Array mit dem `$add`-Operator ein weiteres Element hinzu. Das folgende Beispiel zeigt das Hinzufügen von drei weiteren Haustier-Objekten zum `pets`-Array der Nutzer:in.

Verwenden Sie `$add`, wenn Sie ein oder mehrere neue Objekte anhängen und bestehende Objekte unverändert lassen möchten.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Biscuit"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Pepper"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Noodle"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Aktualisieren %}

Aktualisieren Sie Werte für bestimmte Objekte innerhalb eines Arrays mit dem Parameter `_merge_objects` und dem Operator `$update`. Ähnlich wie bei Updates anderer [verschachtelter angepasster Attribute]({{site.baseurl}}/nested_custom_attribute_support#api-request-body) wird hierbei ein Deep Merge durchgeführt.

Beachten Sie, dass `$update` nicht verwendet werden kann, um eine verschachtelte Eigenschaft aus einem Objekt innerhalb eines Arrays zu entfernen. Dazu müssen Sie das gesamte Element aus dem Array entfernen und dann das Objekt ohne diesen spezifischen Schlüssel wieder hinzufügen (mit einer Kombination aus `$remove` und `$add`).

Verwenden Sie `$update`, wenn das Objekt bereits existiert und Sie ein oder mehrere Felder ändern möchten, indem Sie nach `$identifier_key` und `$identifier_value` abgleichen.

Das folgende Beispiel zeigt die Aktualisierung der Eigenschaft `breed` auf `goldfish` für das Objekt mit einer `id` von `4`. Dieses Anfrage-Beispiel aktualisiert auch das Objekt mit `id` gleich `5` mit einem neuen `name` von `Annette`. Da der Parameter `_merge_objects` auf `true` gesetzt ist, bleiben alle anderen Felder für diese beiden Objekte unverändert.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
Sie müssen `_merge_objects` auf true setzen, da Ihre Objekte sonst überschrieben werden. `_merge_objects` ist standardmäßig false.
{% endalert %}

{% endtab %}
{% tab Entfernen %}

Entfernen Sie Objekte aus einem Array mit dem Operator `$remove` in Kombination mit einem passenden Schlüssel (`$identifier_key`) und Wert (`$identifier_value`).

Verwenden Sie `$remove`, wenn Sie alle übereinstimmenden Objekte für ein bekanntes Bezeichner-Paar löschen möchten, z.&nbsp;B. `id = 2` oder `type = dog`.

Das folgende Beispiel zeigt das Entfernen aller Objekte im `pets`-Array, die eine `id` mit dem Wert `1`, eine `id` mit dem Wert `2` und einen `type` mit dem Wert `dog` haben. Wenn es mehrere Objekte mit dem `type`-Wert `dog` gibt, werden alle übereinstimmenden Objekte entfernt.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Verarbeitungsreihenfolge {#processing-order}

Wenn eine einzelne `/users/track`-Anfrage `$add`-, `$remove`- und `$update`-Operationen für dasselbe Array-Attribut enthält, verarbeitet Braze diese in folgender Reihenfolge:

1. `$add`
2. `$remove`
3. `$update`

Diese Reihenfolge gilt innerhalb eines einzelnen Attribut-Update-Objekts in einer Anfrage und bestimmt den endgültigen Zustand des Arrays, nachdem alle Operationen ausgewertet wurden.

Da `$add` vor `$remove` ausgeführt wird, können Sie `$remove` gefolgt von `$add` nicht als Upsert-Mechanismus innerhalb einer einzelnen Anfrage verwenden. `$add` wird zuerst verarbeitet, dann löscht `$remove` das Element. Für einen Upsert senden Sie `$remove` in einer separaten Anfrage vor `$add`.

### Zeitstempel {#timestamps}

Wenn Sie Felder wie Zeitstempel in einem Array von Objekten einschließen, verwenden Sie das `$time`-Format anstelle von einfachen Strings oder Unix-Epoch-Ganzzahlen.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support).
{% endalert %}

## SDK-Beispiel {#sdk-example}

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab Erstellen %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Pixel")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab Hinzufügen %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Pepper"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Noodle")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Aktualisieren %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Löschen %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab Erstellen %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Mochi"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Pixel"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab Hinzufügen %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Biscuit"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Pepper"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Noodle"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Aktualisieren %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Löschen %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Verschachtelte angepasste Attribute werden für AppboyKit nicht unterstützt.
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab Erstellen %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Mochi"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Pixel"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab Hinzufügen %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Pepper",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Noodle",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Aktualisieren %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Löschen %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Liquid-Templating {#liquid-templating}

Sie können dieses `pets`-Array verwenden, um eine Nachricht zu personalisieren. Das folgende Liquid-Templating-Beispiel zeigt, wie Sie auf die Eigenschaften des angepassten Attribut-Objekts verweisen, die aus der vorherigen API-Anfrage gespeichert wurden, und diese in Ihrem Messaging verwenden.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %}

{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %}
```
{% endraw %}

In diesem Szenario können Sie Liquid verwenden, um das `pets`-Array zu durchlaufen und für jedes Haustier eine Aussage auszugeben. [Weisen Sie eine Variable]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/dashboard_tools#assign-variables) dem angepassten Attribut `pets` zu und verwenden Sie die Punkt-Notation, um auf Eigenschaften eines Objekts zuzugreifen. Geben Sie den Namen des Objekts an, gefolgt von einem Punkt `.`, gefolgt vom Eigenschaftsnamen.

## Segmentierung {#segmentation}

Wenn Sie Nutzer:innen basierend auf Arrays von Objekten segmentieren, qualifiziert sich eine Nutzer:in für das Segment, wenn ein beliebiges Objekt im Array den Kriterien entspricht.

Erstellen Sie ein neues Segment und wählen Sie **Nested Custom Attribute** als Filter. Suchen und wählen Sie dann den Namen Ihres Arrays von Objekten aus.

![Nach Array von Objekten filtern.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Verwenden Sie die Punkt-Notation, um anzugeben, welches Feld im Array von Objekten Sie verwenden möchten. Beginnen Sie das Textfeld mit einem leeren Paar eckiger Klammern `[]`, um Braze mitzuteilen, dass Sie innerhalb eines Arrays von Objekten suchen. Fügen Sie danach einen Punkt `.` hinzu, gefolgt vom Namen des Feldes, das Sie verwenden möchten.

Wenn Sie beispielsweise ein `top_3_movies`-Array von Objekten basierend auf dem Feld `type` filtern möchten, geben Sie `[].type` ein und wählen Sie die Filme aus, nach denen gefiltert werden soll, z.&nbsp;B. `Fantasy Movie`.


### Verschachtelungsebenen {#levels-of-nesting}

Sie können ein Segment mit bis zu einer Ebene der Array-Verschachtelung erstellen (Array innerhalb eines anderen Arrays). Angenommen, Sie haben die folgenden Attribute: Sie können ein Segment für `pets[].name` enthält `Mochi` erstellen, aber Sie können kein Segment für `pets[].nicknames[]` enthält `Gugu` erstellen.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi",
          "nicknames": [
            "MoMo",
            "Mochi"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel",
          "nicknames": [
            "PiPi",
            "Pixel"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## Datenpunkte {#data-points}

Datenpunkte werden unterschiedlich protokolliert, je nachdem, ob Sie eine Eigenschaft erstellen, aktualisieren oder entfernen.

{% tabs local %}
{% tab Erstellen %}

Das Erstellen eines neuen Arrays protokolliert einen Datenpunkt für jedes Attribut in einem Objekt. Dieses Beispiel kostet acht Datenpunkte – jedes Haustier-Objekt hat vier Attribute und es gibt zwei Objekte.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Aktualisieren %}

Das Aktualisieren eines bestehenden Arrays protokolliert einen Datenpunkt für jede hinzugefügte Eigenschaft. Dieses Beispiel kostet zwei Datenpunkte, da es nur eine Eigenschaft in jedem der beiden Objekte aktualisiert.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Entfernen %}

Das Entfernen eines Objekts aus einem Array protokolliert einen Datenpunkt für jedes gesendete Entfernungskriterium. Dieses Beispiel kostet drei Datenpunkte, auch wenn Sie mit dieser Anweisung möglicherweise mehrere Hunde entfernen.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}