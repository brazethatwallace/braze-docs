---
nav_title: Verschachtelte Objekte
article_title: Verschachtelte Objekte in angepassten Events
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie verschachtelte JSON-Daten als Eigenschaften von angepassten Events und Käufen senden und wie Sie diese verschachtelten Objekte in Ihrem Messaging verwenden können."
---

# Verschachtelte Objekte in angepassten Events {#nested-objects-in-custom-events}

> Auf dieser Seite erfahren Sie, wie Sie verschachtelte JSON-Daten als Eigenschaften von angepassten Events und Käufen senden und wie Sie diese verschachtelten Objekte in Ihrem Messaging verwenden können.

Sie können verschachtelte Objekte – also Objekte innerhalb eines anderen Objekts – verwenden, um verschachtelte JSON-Daten als Eigenschaften von angepassten Events und Käufen zu senden. Diese verschachtelten Daten können für die Personalisierung von Nachrichten per Template, das Trigger or triggern or triggern von Nachrichtenversand und die Segmentierung von Nutzer:innen verwendet werden.

## Hinweise {#considerations}

- Verschachtelte Daten werden sowohl für [angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) als auch für [Kauf-Events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events) unterstützt, jedoch nicht für andere Event-Typen.
- Event-Eigenschafts-Objekte, die Array- oder Objektwerte enthalten, können eine Event-Eigenschafts-Payload von bis zu 100 KB haben.
- Event-Eigenschafts-Schemas können nicht für Kauf-Events generiert werden.
- Event-Eigenschafts-Schemas werden durch Sampling angepasster Events der letzten 24 Stunden generiert.

### Mindest-SDK or Software-Development-Kit-Versionen {#minimum-sdk-versions}

Die folgenden SDK or Software-Development-Kit-Versionen unterstützen verschachtelte Objekte:

{% sdk_min_versions swift:5.0.0 android:20.0.0 web:3.3.0 %}

## 1. Schritt: Schema generieren {#step-1-generate-a-schema}

Sie können auf die verschachtelten Daten in Ihrem angepassten Event zugreifen, indem Sie für jedes Event mit verschachtelten Event-Eigenschaften ein Schema generieren. So generieren Sie ein Schema:

1. Gehen Sie zu **Dateneinstellungen** > **Angepasste Events**.
2. Wählen Sie **Eigenschaften verwalten** für die Events mit verschachtelten Eigenschaften.
3. Wählen Sie den <i class="fas fa-arrows-rotate"></i> Button, um das Schema zu generieren. Um das Schema anzuzeigen, wählen Sie den <i class="fas fa-plus"></i> Plus-Button.

![Wählen Sie den Button, um das Schema zu generieren. Um das Schema anzuzeigen, wählen Sie den Plus-Button.]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Wenn in Zukunft neue Eigenschaften gesendet werden, sind diese erst nach einer erneuten Generierung im Schema enthalten. Schemas können alle 24 Stunden neu generiert werden.

## 2. Schritt: Das verschachtelte Objekt verwenden {#step-2-use-the-nested-object}

Sie können die verschachtelten Daten bei der Segmentierung und Personalisierung referenzieren. Beachten Sie, dass kein Schema erforderlich ist. In den folgenden Abschnitten finden Sie Anwendungsbeispiele:

- [API-Anfragekörper](#api-request-body)
- [Liquid-Templating](#liquid-templating)
- [Nachrichten-Triggering](#message-triggering)
- [Segmentierung](#segmentation)
- [Personalisierung](#personalization)

### API-Anfragekörper {#api-request-body}

{% tabs %}
{% tab Music Example %}

Das folgende Beispiel zeigt eine `/users/track`-Anfrage mit einem angepassten Event „Created Playlist“. Nachdem eine Playlist erstellt wurde, erfassen Sie die Eigenschaften der Playlist, indem Sie Folgendes senden:
- Eine API-Anfrage, die „songs“ als Eigenschaft auflistet
- Ein Array der verschachtelten Eigenschaften der Songs

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

Das folgende Beispiel zeigt eine `/users/track`-Anfrage mit einem angepassten Event „Ordered“. Nachdem eine Bestellung abgeschlossen wurde, erfassen Sie die Eigenschaften dieser Bestellung, indem Sie Folgendes senden:
- Eine API-Anfrage, die `r_details` als Eigenschaft auflistet
- Die verschachtelten Eigenschaften dieser Bestellung

```
...
"properties": {
  "r_details": {
    "name": "SandwichEmperor",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
Bei verschachtelten angepassten Event-Eigenschaften speichert Braze keine Werte, wenn das Jahr kleiner als 0 oder größer als 3000 ist.
{% endalert %}

### Liquid-Templating {#liquid-templating}

Das Folgende zeigt, wie Sie ein Liquid-Template erstellen, das die verschachtelten Eigenschaften aus der [vorherigen API-Anfrage](#api-request-body) referenziert.

{% tabs %}
{% tab Music Example %}
Templating in Liquid in einer Nachricht, die durch das Event „Created Playlist“ getriggert wird:

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind"<br>
`{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Templating in Liquid in einer Nachricht, die durch das Event „Ordered“ getriggert wird:

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Nachrichten-Triggering {#message-triggering}

Um diese Eigenschaften zum Trigger or triggern or triggern einer Campaign zu verwenden, wählen Sie Ihr angepasstes Event oder Ihren Kauf aus und fügen Sie dann einen Filter für **verschachtelte Eigenschaften** hinzu. Beachten Sie, dass das Nachrichten-Triggering für In-App-Nachrichten noch nicht unterstützt wird, aber verschachtelte Eigenschaften in der Liquid-Personalisierung in den Nachrichten werden trotzdem angezeigt.

{% tabs %}
{% tab Music Example %}

Trigger or triggern or triggern einer Campaign mit verschachtelten Eigenschaften aus dem Event „Created Playlist“:

![Nutzer:in wählt eine verschachtelte Eigenschaft für Eigenschaftsfilter bei einem angepassten Event aus.]({% image_buster /assets/img/nested_object2.png %})

Die Trigger or triggern-Bedingung `songs[].album.yearReleased` „ist“ „1968“ trifft auf ein Event zu, bei dem einer der Songs ein Album hat, das 1968 veröffentlicht wurde. Wir verwenden die Klammer-Notation `[]` zum Durchlaufen von Arrays und matchen, wenn **ein beliebiges** Element im durchlaufenen Array mit der Event-Eigenschaft übereinstimmt.

{% alert important %}
Der Filter **ist nicht gleich** matcht nur, wenn keine der Eigenschaften in Ihrem Array dem angegebenen Wert entspricht. <br><br>Nehmen wir zum Beispiel an, Canvas A hat den aktionsbasierten Filter für verschachtelte angepasste Event-Eigenschaften **ist gleich** „smartwatch“, und Canvas B hat den aktionsbasierten Filter für verschachtelte angepasste Event-Eigenschaften **ist nicht gleich** „simphone“. Wenn Sie „smartwatch“ und „simphone“ in Ihren Eigenschaften haben, werden beide Canvase getriggert. Wenn Sie jedoch „simphone“ oder „sim only“ in einer beliebigen Eigenschaft haben, wird keines der beiden Canvase getriggert.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

Trigger or triggern or triggern einer Campaign mit verschachtelten Eigenschaften aus dem Event „Ordered“:

![Nutzer:in fügt den Eigenschaftsfilter r_details.name ist SandwichEmperor für ein angepasstes Event hinzu.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "SandwichEmperor"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Ihre Event-Eigenschaft die Zeichen `[]` oder `.` enthält, escapen Sie diese, indem Sie den entsprechenden Teil in doppelte Anführungszeichen setzen. Zum Beispiel wird `"songs[].album".yearReleased` ein Event mit der literalen Eigenschaft `"songs[].album"` matchen.
{% endalert %}

### Segmentierung {#segmentation}

Um Nutzer:innen basierend auf verschachtelten Event-Eigenschaften zu segmentieren, müssen Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension) verwenden. Nachdem Sie ein Schema generiert haben, wird der Explorer für verschachtelte Objekte im Segmentierungsbereich angezeigt.

![Screenshot des Segmentierungsbereichs mit dem Explorer für verschachtelte Objekte.]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

Die Segmentierung verwendet die gleiche Notation wie das Triggering (siehe [Nachrichten-Triggering](#message-triggering)).

Um Segmenterweiterungen zu bearbeiten oder zu erstellen, benötigen Sie die Berechtigung „Segmente bearbeiten“.

### Personalisierung {#personalization}

Wählen Sie im Modal **Personalisierung hinzufügen** die Option **Erweiterte Event-Eigenschaften** als Personalisierungstyp aus. Dies ermöglicht es, verschachtelte Event-Eigenschaften hinzuzufügen, nachdem ein Schema generiert wurde.

![Im Modal „Personalisierung hinzufügen“ wird „Erweiterte Event-Eigenschaften“ als Personalisierungstyp ausgewählt. Dies ermöglicht es, verschachtelte Event-Eigenschaften hinzuzufügen, nachdem ein Schema generiert wurde.]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Verschachtelte Objekte in Nachrichten testen {#testing-nested-objects-in-messages}

Das Dashboard-Tool **Vorschau & Test** unterstützt nicht das Hinzufügen von Mock-Daten für verschachtelte Objekte oder verschachtelte angepasste Attribute. Um Nachrichten zu testen, die über Liquid auf verschachtelte Daten verweisen, können Sie Nachrichten mit verschachtelten Attributen als bestehende:r Nutzer:in mit diesem verschachtelten Attribut in der Vorschau anzeigen oder Nachrichten mit angepassten Event-Eigenschaften testen, indem Sie eine Live-Campaign an Testnutzer:innen starten.

### Verschachtelte angepasste Attribute {#nested-custom-attributes}

1. Importieren Sie die verschachtelten Attribute über die API in das Testnutzer:innen-Profil.
2. Gehen Sie in Ihrer Campaign oder Ihrem Canvas zu **Vorschau & Test**.
3. Wählen Sie **Vorschau als Nutzer:in** und suchen Sie nach der/dem Testnutzer:in. Das Liquid wird mit den tatsächlichen verschachtelten Attributen im Profil dieser/dieses Nutzer:in aufgelöst.

### Verschachtelte Event-Eigenschaften {#nested-event-properties}

Verschachtelte Event-Eigenschaften können im Dashboard nicht in der Vorschau angezeigt werden, da sie einen Live-Event-Trigger or triggern erfordern. So testen Sie:

1. Erstellen Sie eine Campaign oder einen Canvas-Schritt, der nur Ihre Testnutzer:innen anspricht und durch das angepasste Event mit verschachtelten Eigenschaften getriggert wird (oder darauf verweist).
2. Starten Sie die Campaign für Ihre Testzielgruppe.
3. Loggen Sie das angepasste Event mit der verschachtelten Objekt-Payload im Profil Ihrer/Ihres Testnutzer:in (über die API oder das SDK or Software-Development-Kit).
4. Überprüfen Sie, ob die Nachricht mit den verschachtelten Eigenschaftswerten korrekt gerendert wird.

## Häufig gestellte Fragen {#frequently-asked-questions}

### Werden durch die Verwendung verschachtelter Objekte zusätzliche Datenpunkte protokolliert? {#does-using-nested-objects-log-additional-data-points}

Es gibt keine Änderung bei der Protokollierung von Datenpunkten durch das Hinzufügen dieser Funktion. Die Segmentierung basierend auf verschachtelten Objekten verwendet Segmenterweiterungen, die keine zusätzlichen Datenpunkte verbrauchen.

### Wie viele verschachtelte Daten können gesendet werden? {#how-much-nested-data-can-be-sent}

Wenn eine oder mehrere Eigenschaften des Events verschachtelte Daten enthalten, beträgt die maximale Payload für alle kombinierten Eigenschaften eines Events 100 KB. Jede Anfrage, die dieses Größenlimit überschreitet, wird abgelehnt.