---
nav_title: "Anwendungsfall: Verschachtelte angepasste Attribute"
article_title: "Anwendungsfall: Segmentierung mit verschachtelten angepassten Attributen"
page_order: 10
page_type: tutorial
tool: Segments
description: "Erstellen Sie Segmente mit verschachtelten angepassten Attributen: der Filter für verschachtelte angepasste Attribute, Pfade und Vergleichsoperatoren, Zeitfilter, Multi-Kriterien-Segmentierung, Schema-Generierung und der Explorer für verschachtelte Objekte."
---

# Anwendungsfall: Segmentierung mit verschachtelten angepassten Attributen {#use-case-segment-with-nested-custom-attributes}

> Diese Anwendungsfälle zeigen, wie Sie Nutzer:innen mit verschachtelten angepassten Attributen in Braze segmentieren können. Sie enthalten Beispiel-JSON und Dashboard-Workflows, die Sie an Ihre eigenen Daten anpassen können.

Nehmen wir an, Sie sind in einem Marketing-Team für eine Musik-Streaming-App und möchten Nachrichten basierend auf den verschachtelten angepassten Attributen einer Nutzer:in senden, z. B. Kontoobjekte mit Salden und Typen. Diese Anwendungsfälle zeigen verschiedene Möglichkeiten, wie Ihr Team verschachtelte angepasste Attribute in Segmenten nutzen kann, und vermitteln Ihnen, wie Sie:

- Einen Segmentfilter für verschachtelte angepasste Attribute konfigurieren, Pfade validieren und Vergleichsoperatoren auswählen, die zum Datentyp jeder Eigenschaft passen.
- Wissen, wann Sie **Day of Year**- gegenüber **Time**-Operatoren für verschachtelte Datumswerte verwenden sollten, und wie **Multi-Criteria Segmentation** Nutzer:innen zuordnet, wenn mindestens ein Objekt in einem Array alle aufgeführten Kriterien erfüllt.
- Ein Schema für ein Objekt oder Objekt-Array generieren, es im Dashboard erkunden und ein Segment abschließen (z. B. Nutzer:innen mit einem Saldo unter 100), indem Sie den Pfad-Picker verwenden, anstatt Pfade aus dem Gedächtnis einzugeben.

## Nach verschachtelten angepassten Attributen filtern {#filter-by-nested-custom-attributes}

Erstellen wir ein Segment basierend auf einem verschachtelten angepassten Attribut, um Nutzer:innen anzusprechen, die ihren meistgespielten Song mehr als 300 Mal abgespielt haben.

### 1. Schritt: Filter hinzufügen {#step-1-add-the-filter}

Wählen Sie den Filter **Nested Custom Attributes** aus, um ein Dropdown-Menü anzuzeigen, aus dem Sie ein bestimmtes verschachteltes angepasstes Attribut auswählen können. Wir wählen `most_played_song`, das Daten über den meistgespielten Song einer Nutzer:in enthält.

### 2. Schritt: Eigenschaft auswählen {#step-2-select-the-property}

Wählen Sie die **Property** innerhalb des verschachtelten angepassten Attributs aus, nach der Sie filtern möchten. Wir wählen `play_analytics.count`, das erfasst, wie oft eine Nutzer:in ihren meistgespielten Song abgespielt hat.

### 3. Schritt: Vergleichsoperator und Wert des verschachtelten angepassten Attributs auswählen {#step-3-select-a-comparison-and-nested-custom-attribute-value}

Beim Filtern nach verschachtelten angepassten Attributen bestimmt der Datentyp Ihrer Eigenschaft die verfügbaren Vergleichsoperatoren. Da `play_analytics.count` beispielsweise eine Zahl ist, können Sie einen Vergleichsoperator unter der Kategorie **Number** auswählen.

Um nach Nutzer:innen zu filtern, die ihren meistgespielten Song mindestens 300 Mal abgespielt haben, wählen Sie den Vergleich **More than** und geben dann „300“ als Wert ein.

![Eine Nutzer:in wählt einen Operator basierend auf dem Datentyp für das verschachtelte angepasste Attribut aus]({% image_buster /assets/img_archive/nca_comparator.png %})

## Nach Zeit-Datentypen filtern {#filter-for-time-data-types}

Beim Filtern eines verschachtelten angepassten Zeitattributs können Sie wählen, ob Sie mit Operatoren unter den Kategorien **Day of Year** oder **Time** filtern möchten, wenn Sie den Datumswert vergleichen.

Wenn Sie einen Operator unter der Kategorie **Day of Year** auswählen, werden nur Monat und Tag für den Vergleich herangezogen, anstatt des vollständigen Zeitstempels des verschachtelten angepassten Attributwerts. Die Auswahl eines Operators unter der Kategorie **Time** vergleicht den vollständigen Zeitstempel, einschließlich des Jahres.

## Multi-Criteria Segmentation verwenden {#use-multi-criteria-segmentation}

Verwenden Sie **Multi-Criteria Segmentation**, um ein Segment zu erstellen, das mehrere Kriterien innerhalb eines einzelnen Objekts erfüllt. Dies qualifiziert die Nutzer:in für das Segment, wenn sie mindestens ein Objekt im Array hat, das alle angegebenen Kriterien erfüllt. Beispielsweise werden Nutzer:innen nur dann diesem Segment zugeordnet, wenn ihr Schlüssel nicht leer ist und ihre Zahl größer als 0 ist.

### Liquid für Segment kopieren {#copy-liquid-for-segment}

Sie können auch die Funktion **Copy Liquid for segment** verwenden, um Liquid-Code für dieses Segment zu generieren und in einer Nachricht zu verwenden. Nehmen wir beispielsweise an, Sie haben ein Array von Kontoobjekten und ein Segment, das Kund:innen mit aktiven steuerpflichtigen Konten anspricht. Um Kund:innen dazu zu bewegen, zum Kontoziel eines ihrer aktiven und steuerpflichtigen Konten beizutragen, möchten Sie eine Nachricht erstellen, die sie dazu anregt.

![Ein Beispiel-Segment mit aktiviertem Kontrollkästchen für Multi-Criteria Segmentation.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

Wenn Sie **Copy Liquid for segment** auswählen, generiert Braze automatisch Liquid-Code, der ein Objekt-Array zurückgibt, das nur Konten enthält, die aktiv und steuerpflichtig sind.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

Von hier aus können Sie `segmented_nested_objects` verwenden und Ihre Nachricht personalisieren. In diesem Beispiel möchten wir ein Ziel vom ersten aktiven steuerpflichtigen Konto übernehmen und personalisieren:

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

Dies gibt die folgende Nachricht an Ihre geschäftskunden zurück: „Get to your retirement goal faster, make a deposit using our new fast deposit feature!“

## Schema mit dem Explorer für verschachtelte Objekte generieren {#generate-schema}

Sie können ein Schema für Ihre Objekte generieren, um Segmentfilter zu erstellen, ohne sich verschachtelte Objektpfade merken zu müssen.

### 1. Schritt: Schema generieren {#step-1-generate-a-schema}

Nehmen wir beispielsweise an, wir haben ein `accounts`-Objekt-Array, das wir gerade an Braze gesendet haben:

```json
{"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true}
]}
```

Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > **Angepasste Attribute**.

Suchen Sie nach Ihrem Objekt oder Objekt-Array. Wählen Sie in der Spalte **Attribute Name** die Option **Generate Schema**.

![Eine Liste angepasster Attribute mit der Option, das Schema für das Konten-Attribut zu generieren.]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
Es kann einige Minuten dauern, bis Ihr Schema generiert wird, abhängig davon, wie viele Daten Sie uns gesendet haben.
{% endalert %}

Nachdem das Schema generiert wurde, erscheint ein neuer <i class="fas fa-plus"></i> Plus-Button anstelle des Buttons **Generate Schema**. Sie können darauf klicken, um zu sehen, was Braze über dieses verschachtelte angepasste Attribut weiß.

Während der Schema-Generierung betrachtet Braze zuvor gesendete Daten und erstellt eine ideale Darstellung Ihrer Daten für dieses Attribut. Braze analysiert außerdem Ihre verschachtelten Werte und fügt einen Datentyp hinzu. Dies geschieht durch Stichproben der zuvor an Braze gesendeten Daten für das gegebene verschachtelte Attribut.

Für unser `accounts`-Objekt-Array können Sie sehen, dass innerhalb des Objekt-Arrays ein Objekt vorhanden ist, das Folgendes enthält:

- Einen booleschen Typ mit dem Schlüssel `active` (unabhängig davon, ob das Konto aktiv ist oder nicht)
- Einen Zahlentyp mit dem Schlüssel `balance` (Saldo des Kontos)
- Einen String-Typ mit dem Schlüssel `type` (nicht steuerpflichtiges oder steuerpflichtiges Konto)

![Schema für das Konten-Objekt-Array mit drei verschachtelten Werten: active, balance und type.]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:70%" }

Nachdem wir die Daten analysiert und eine Darstellung erstellt haben, erstellen wir ein Segment.

### 2. Schritt: Segment erstellen {#step-2-build-a-segment}

Sprechen wir Kund:innen an, die einen Saldo von weniger als 100 haben, damit wir ihnen eine Nachricht senden können, die sie zu einer Einzahlung anregt.

Erstellen Sie ein Segment und fügen Sie den Filter `Nested Custom Attribute` hinzu. Suchen Sie dann nach Ihrem Objekt oder Objekt-Array und wählen Sie es aus. Hier haben wir das `accounts`-Objekt-Array hinzugefügt.

![Filterung nach verschachtelten angepassten Attributen für das Konten-Objekt-Array.]({% image_buster /assets/img_archive/nca_segment_schema.png %})

Wählen Sie den <i class="fas fa-plus"></i> Plus-Button im Pfadfeld. Dies öffnet eine Darstellung Ihres Objekts oder Objekt-Arrays. Sie können eines der aufgelisteten Elemente auswählen, und Braze fügt es für Sie in das Pfadfeld ein. In diesem Beispiel benötigen wir den Saldo. Wählen Sie den Saldo als Pfad aus (in diesem Fall `[].balance`), der automatisch im Pfadfeld eingetragen wird.

![Konten-Schema mit durchsuchbarer Liste von Pfaden.]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

Wählen Sie **less than** als Vergleichsoperator und geben Sie dann „100“ als Saldowert ein.

![Ein Filter für Nutzer:innen mit einem Kontosaldo von weniger als 100.]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

Das war's! Sie haben gerade ein Segment mit einem verschachtelten angepassten Attribut erstellt, ganz ohne wissen zu müssen, wie die Daten strukturiert sind. Der Explorer für verschachtelte Objekte in Braze hat eine visuelle Darstellung Ihrer Daten generiert und Ihnen ermöglicht, genau das zu erkunden und auszuwählen, was Sie für die Erstellung eines Segments benötigen.