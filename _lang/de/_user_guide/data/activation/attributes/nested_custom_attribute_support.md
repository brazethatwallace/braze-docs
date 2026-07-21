---
nav_title: Verschachtelte angepasste Attribute
article_title: Verschachtelte angepasste Attribute
alias: "/nested_custom_attribute_support/"
page_order: 3
page_type: reference
description: "Dieser Referenzartikel behandelt die Verwendung verschachtelter angepasster Attribute als Datentyp für angepasste Attribute, einschließlich Einschränkungen und Anwendungsbeispielen."
---

# Verschachtelte angepasste Attribute {#nested-custom-attributes}

> Diese Seite behandelt verschachtelte angepasste Attribute, die es Ihnen ermöglichen, eine Reihe von Attributen als Eigenschaft eines anderen Attributs zu definieren. Mit anderen Worten: Wenn Sie ein angepasstes Attribut-Objekt definieren, können Sie eine Reihe von zusätzlichen Attributen für dieses Objekt festlegen.

## Über verschachtelte Attribute {#about-nested-attributes}

Verschachtelte Attribute ermöglichen es Ihnen, reichhaltigere Segmente zu erstellen und Nachrichten mit Daten aus einem einzelnen angepassten Attribut-Objekt zu personalisieren.

Im folgenden Beispiel enthält das angepasste Attribut `favorite_book` die verschachtelten Attribute `title`, `author` und `publishing_date`. Dieses Objekt kann verwendet werden, um Nutzer:innen nach Autor anzusprechen, nach Veröffentlichungsdatum zu filtern oder den Buchtitel direkt in eine Nachricht einzufügen:

```json
"favorite_book": {
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "publishing_date": "1937"
}
```


{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Hinweise {#considerations}

- Verschachtelte angepasste Attribute sind für angepasste Attribute gedacht, die über das Braze SDK oder die API gesendet werden.
- Objekte haben eine maximale Größe von 100&nbsp;KB. Wenn ein Update dazu führt, dass das Objekt 100&nbsp;KB überschreitet, verwirft Braze das Update und das Attribut bleibt unverändert.
- Schlüsselnamen und String-Werte dürfen maximal 255 Zeichen lang sein.
- Schlüsselnamen dürfen keine Leerzeichen enthalten.
- Punkte (`.`) und Dollarzeichen (`$`) sind keine unterstützten Zeichen in einer API-Nutzlast, wenn Sie versuchen, ein verschachteltes angepasstes Attribut an ein Nutzerprofil zu senden.
- Nicht alle Braze-Partner unterstützen verschachtelte angepasste Attribute. Schauen Sie in der [Dokumentation des Partners]({{site.baseurl}}/partners/home) nach, ob bestimmte Partnerintegrationen dieses Feature unterstützen.
- Verschachtelte angepasste Attribute können nicht als Filter verwendet werden, wenn Sie einen Connected Audience API-Aufruf durchführen.
- Standardmäßig enthält der Segmentfilter **Verschachtelte angepasste Attribute** angepasste Attribute vom Typ Objekt, Array-of-Object-Attribute und angepasste Attribute vom Typ Array. Wenn Sie ein Attribut auswählen, enthält der Eigenschafts-Schema-Selektor Array-Pfade (mit `[]`-Notation) für verschachtelte Array-Felder. Um angepasste Attribute auf oberster Ebene vom Typ Array aus diesem Filter auszublenden, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support).
- Wenn Sie Nachrichten im Dashboard mit **Als angepasste Nutzer:in anzeigen** in der Vorschau betrachten, können Sie Testdaten nur als String oder String-Array eingeben – verschachtelte Objekte werden nicht unterstützt. Um eine Nachricht in der Vorschau anzuzeigen, die auf verschachtelte angepasste Attribute verweist, wählen Sie eine vorhandene Nutzer:in aus, die das verschachtelte Attribut bereits in ihrem Profil hat. Für verschachtelte angepasste Event-Eigenschaften müssen Sie eine Live-Campaign starten, die auf eine Testnutzer:in ausgerichtet ist, um das Rendering zu überprüfen.

## API-Beispiel {#api-example}

{% tabs local %}
{% tab Erstellen %}
Das folgende Beispiel zeigt eine `/users/track`-Anfrage mit einem „Most Played Song“-Objekt. Um die Eigenschaften des Songs zu erfassen, senden wir eine API-Anfrage, die `most_played_song` als Objekt zusammen mit einer Reihe von Objekt-Eigenschaften auflistet.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Aktualisieren %}
Um ein bestehendes Objekt zu aktualisieren, senden Sie einen POST an `users/track` mit dem Parameter `_merge_objects` in der Anfrage. Dadurch wird Ihr Update per Deep Merge mit den vorhandenen Objektdaten zusammengeführt. Deep Merging stellt sicher, dass alle Ebenen eines Objekts in ein anderes Objekt zusammengeführt werden und nicht nur die erste Ebene. In diesem Beispiel haben wir bereits ein `most_played_song`-Objekt in Braze und fügen nun ein neues Feld, `year_released`, zum `most_played_song`-Objekt hinzu.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

Nach dem Empfang dieser Anfrage sieht das angepasste Attribut-Objekt wie folgt aus:

```json
{"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}}
```

{% alert warning %}
Sie müssen `_merge_objects` auf `true` setzen, da Ihre Objekte sonst überschrieben werden. `_merge_objects` ist standardmäßig `false`.
{% endalert %}

{% endtab %}
{% tab Löschen %}
Um ein angepasstes Attribut-Objekt zu löschen, senden Sie einen POST an `users/track`, wobei das angepasste Attribut-Objekt auf `null` gesetzt wird.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
Dieser Ansatz kann nicht verwendet werden, um einen verschachtelten Schlüssel innerhalb eines [Objekt-Arrays]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) zu löschen.
{% endalert %}

{% endtab %}
{% endtabs %}

## SDK-Beispiel {#sdk-example}

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**Erstellen**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**Aktualisieren**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**Löschen**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**Erstellen**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**Aktualisieren**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**Löschen**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**Erstellen**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**Aktualisieren**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**Löschen**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## Datumsangaben als Objekt-Eigenschaften erfassen {#capturing-dates-as-object-properties}

Um Datumsangaben als Objekt-Eigenschaften zu erfassen, müssen Sie den Schlüssel `$time` verwenden. Im folgenden Beispiel wird ein „Important Dates“-Objekt verwendet, um die Objekt-Eigenschaften `birthday` und `wedding_anniversary` zu erfassen. Der Wert für diese Datumsangaben ist ein Objekt mit einem `$time`-Schlüssel, der kein Null-Wert sein darf.

{% alert note %}
Wenn Sie Datumsangaben nicht von Anfang an als Objekt-Eigenschaften erfasst haben, empfehlen wir, diese Daten mit dem `$time`-Schlüssel für alle Nutzer:innen erneut zu senden. Andernfalls kann dies zu unvollständigen Segmenten bei der Verwendung des `$time`-Attributs führen. Wenn der Wert für `$time` in einem verschachtelten angepassten Attribut jedoch nicht korrekt formatiert ist, wird das gesamte verschachtelte angepasste Attribut nicht aktualisiert.
{% endalert %}

```json
{
  "attributes": [
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
Bei verschachtelten angepassten Attributen speichert Braze keine Werte, wenn das Jahr kleiner als 0 oder größer als 3000 ist.
{% endalert %}

## Liquid-Templating

Das folgende Liquid-Templating-Beispiel zeigt, wie Sie die angepassten Attribut-Objekt-Eigenschaften referenzieren, die aus der vorherigen API-Anfrage gespeichert wurden, und sie in Ihrem Messaging verwenden können.

Verwenden Sie den Personalisierungs-Tag `custom_attribute` und die Punkt-Notation, um auf Eigenschaften eines Objekts zuzugreifen. Geben Sie den Namen des Objekts (und die Position im Array, wenn Sie ein Objekt-Array referenzieren) an, gefolgt von einem Punkt, gefolgt vom Eigenschaftsnamen.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — „Miles Davis“
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — „Solea“
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — „1000“
{% endraw %}

Um verschachtelte angepasste Attribute als Liquid in Ihrer Nachricht zu verwenden:

1. Gehen Sie zu einer Campaign oder einem Canvas und öffnen Sie den Nachrichtenschritt, in dem Sie Personalisierung hinzufügen möchten.
2. Fügen Sie im Nachrichten-Editor das Liquid-Snippet an der Stelle ein, an der der Wert erscheinen soll.
3. Verwenden Sie **Vorschau und Test** mit einer vorhandenen Nutzer:in, die das verschachtelte angepasste Attribut bereits in ihrem Profil hat, um zu bestätigen, dass der Wert wie erwartet gerendert wird.

### Personalisierung {#personalization}

Sie können **Personalisierung hinzufügen** verwenden, um ein verschachteltes angepasstes Attribut in Ihre Nachricht einzufügen.

So öffnen Sie **Personalisierung hinzufügen**:

1. Gehen Sie zu einer Campaign oder einem Canvas und öffnen Sie den Nachrichtenschritt, in dem Sie Personalisierung hinzufügen möchten.
2. Wählen Sie im Nachrichten-Editor **Personalisierung** aus, um die Seitenleiste **Personalisierung hinzufügen** zu öffnen, in der Sie Personalisierungsoptionen auswählen können.

So konfigurieren Sie die Personalisierung mit verschachtelten angepassten Attributen:

1. Wählen Sie unter **Personalisierungstyp** die Option **Verschachtelte angepasste Attribute** aus.
2. Wählen Sie unter **Übergeordnetes Attribut** den Pfad des verschachtelten angepassten Attributs aus, den Sie einfügen möchten.
   Wählen Sie beispielsweise `preferences.neighborhood_office` aus.
3. Optional: Geben Sie unter **Standardwert** einen Fallback-Wert für Nutzer:innen ein, die keinen eigenen Wert für dieses Attribut haben.
4. Überprüfen Sie das generierte **Liquid-Snippet**, um sicherzustellen, dass es dem erwarteten Pfad entspricht.
5. Wählen Sie **Einfügen** aus.

In diesem Beispiel fügt Braze den verschachtelten Wert für `preferences.neighborhood_office` in Ihre Nachricht ein. Standardwerte sind Fallbacks, die Ihre Nachricht für Nutzer:innen enthält, die keinen eigenen Wert für ein Attribut haben.

{% alert tip %}
Überprüfen Sie, ob ein Schema generiert wurde, wenn Sie die Option zum Einfügen verschachtelter angepasster Attribute nicht sehen.
{% endalert %}

## Schemas neu generieren {#regenerate-schema}

Nachdem ein Schema generiert wurde, können Sie es **einmal pro Kalendertag** (basierend auf der Zeitzone Ihres Unternehmens) neu generieren. Dieser Abschnitt beschreibt, wie Sie Ihr Schema neu generieren. Ausführlichere Informationen zu Schemas finden Sie unter [Schema mit dem Nested-Object-Explorer generieren]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#generate-schema).

So generieren Sie das Schema für Ihr verschachteltes angepasstes Attribut neu:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute**.
2. Suchen Sie nach Ihrem verschachtelten angepassten Attribut.
3. Wählen Sie in der Spalte **Attributname** für Ihr Attribut <i class="fas fa-plus" aria-label="Schema verwalten"></i> **Schema verwalten** aus, um das Schema zu verwalten.
4. Ein Modal wird angezeigt. Wählen Sie **Schema neu generieren**.

Die Aktion **Schema neu generieren** ist auf **einmal pro Kalendertag** in der Zeitzone Ihres Unternehmens beschränkt. Sie können keine weitere Neugenerierung starten, während ein Schema-Job bereits **in Bearbeitung** ist (die Option ist nicht verfügbar, solange der Status **Wird generiert** lautet). Die Schema-Neugenerierung erkennt nur neue Objekte und löscht keine Objekte, die derzeit im Schema vorhanden sind.

{% alert important %}
Um das Schema für ein Objekt-Array mit einem vorhandenen Objekt zurückzusetzen, müssen Sie ein neues angepasstes Attribut erstellen. Die Schema-Neugenerierung löscht keine vorhandenen Objekte.
{% endalert %}

Wenn Daten nach der Schema-Neugenerierung nicht wie erwartet angezeigt werden, wird das Attribut möglicherweise nicht häufig genug erfasst. Nutzerdaten werden auf Basis zuvor an Braze gesendeter Daten für das jeweilige verschachtelte Attribut gesampelt. Wenn das Attribut nicht häufig genug erfasst wird, wird es nicht für das Schema berücksichtigt.

## Änderungen an verschachtelten angepassten Attributen triggern {#trigger-nested-custom-attribute-changes}

Sie können triggern, wenn sich ein verschachteltes angepasstes Attribut-Objekt ändert. Diese Option ist für Änderungen an Objekt-Arrays nicht verfügbar. Wenn Sie keine Option zum Anzeigen des Pfad-Explorers sehen, überprüfen Sie, ob Sie ein Schema generiert haben.

In einer aktionsbasierten Campaign können Sie beispielsweise eine neue Trigger-Aktion für **Wert des angepassten Attributs ändern** hinzufügen, um Nutzer:innen anzusprechen, die ihre Nachbarschaftsbüro-Präferenzen geändert haben.

So konfigurieren Sie diesen Trigger in einer aktionsbasierten Campaign:

1. Erstellen oder bearbeiten Sie eine Campaign und setzen Sie den Zustellungstyp auf **Aktionsbasierte Zustellung**.
2. Wählen Sie in den Trigger-Einstellungen **Wert des angepassten Attributs ändern** aus.
3. Wählen Sie den Pfad des verschachtelten angepassten Attributs aus, den Sie überwachen möchten.
   Wählen Sie beispielsweise `preferences.neighborhood_office` aus.
4. Wählen Sie die gewünschte Trigger-Bedingung aus, z. B. **Beliebiger neuer Wert**.
5. Konfigurieren Sie Ihre Campaign-Nachricht und Zielgruppe fertig und starten Sie dann die Campaign.

## Fehlerbehebung {#troubleshooting}

### Verschachtelte angepasste Attributwerte werden nicht konsistent angewendet {#nested-custom-attribute-values-not-applied-consistently}

Wenn Sie feststellen, dass verschachtelte angepasste Attributwerte nicht konsistent zu Nutzerprofilen hinzugefügt werden, liegt das Problem häufig an Datentyp-Konflikten.

So diagnostizieren und beheben Sie dieses Problem:

1. **Nutzerbeispiele vergleichen:** Nehmen Sie ein erfolgreiches und ein nicht erfolgreiches Nutzerbeispiel, bei dem das verschachtelte angepasste Attribut gesetzt worden sein sollte.
2. **Datenstruktur überprüfen:** Sehen Sie sich die angepassten Attributwerte in beiden Profilen an und vergleichen Sie sie:
   - Sind die Eigenschaften unter einem Objekt gespeichert?
   - Sind die Eigenschaften als Array von Eigenschaften gespeichert?
3. **Segmentierungsfilter prüfen:** Vergleichen Sie die gespeicherte Datenstruktur damit, wie das verschachtelte angepasste Attribut in Ihren Segmentierungsfiltern referenziert wird.
4. **Datentyp überprüfen:** So identifizieren Sie den Datentyp eines angepassten Attributs:
   - Gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute**.
   - Suchen Sie nach dem übergeordneten angepassten Attribut, das das verschachtelte Attribut enthält, das Sie überprüfen möchten.
   - Wenn in der Zeile **Schema generieren** angezeigt wird, wählen Sie diese Option aus, um das Schema zuerst zu generieren.
   - Nachdem das Schema generiert wurde, wählen Sie das Plus-Symbol in der Spalte **Attributname** für dieses Attribut aus.
   - Überprüfen Sie im Modal **Schema bearbeiten** die verschachtelten Attribute und ihre entsprechenden Werte in der Spalte **Datentyp**.

Wenn Sie feststellen, dass der Datentyp nicht dem beabsichtigten Format über die Nutzerprofile hinweg entspricht, entfernen Sie den falsch formatierten Wert aus den betroffenen Nutzerprofilen und senden Sie das Attribut im korrekten Format mit der entsprechenden API-Anfrage oder SDK-Methode erneut.

## Segmentierungsverhalten bei Objekt-Arrays {#segmentation-behavior-with-arrays-of-objects}

Wenn Sie mehrere `Nested Custom Attribute`-Filter mit UND-Logik verwenden, um auf einem Objekt-Array zu segmentieren, wird jeder Filter unabhängig über alle Elemente im Array ausgewertet. Eine Nutzer:in qualifiziert sich für das Segment, wenn _irgendein_ Element im Array jeden einzelnen Filter erfüllt – die Filter müssen nicht auf _dasselbe_ Element zutreffen.

Angenommen, eine Nutzer:in hat das folgende Array:

```json
{
  "orders": [
    {"product": "Shoes", "price": 80},
    {"product": "Hat", "price": 25}
  ]
}
```

Ein Segment mit den folgenden UND-Filtern:

- `orders[].price` ist größer als 50
- `orders[].price` ist kleiner als 30

Diese Nutzer:in würde sich qualifizieren, da der erste Filter auf das „Shoes“-Element zutrifft (80 > 50) und der zweite Filter auf das „Hat“-Element zutrifft (25 < 30). Obwohl kein einzelnes Element beide Bedingungen erfüllt, wird die Nutzer:in dennoch in das Segment aufgenommen.

Wenn alle Bedingungen auf dasselbe Element innerhalb eines Arrays zutreffen müssen, verwenden Sie die [Multi-Kriterien-Segmentierung]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#use-multi-criteria-segmentation) auf demselben Pfad oder strukturieren Sie Ihre Daten um, um elementübergreifendes Matching zu vermeiden.

## Datenpunkte {#data-points}

Jeder gesendete Schlüssel verbraucht einen Datenpunkt. Beispielsweise verbraucht dieses im Nutzerprofil initialisierte Objekt sieben (7) Datenpunkte:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
Das Aktualisieren eines angepassten Attribut-Objekts auf `null` verbraucht ebenfalls einen Datenpunkt.
{% endalert %}