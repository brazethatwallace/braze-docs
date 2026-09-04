---
nav_title: Auswahlen
article_title: Auswahlen
page_order: 5
alias: /catalog_selections/
description: "In diesem Referenzartikel erfahren Sie, wie Sie Auswahlen mit Ihren Katalogen erstellen und verwenden, um Daten in Ihren Braze Campaigns zu referenzieren."
---

# Auswahlen {#selections}

> Auswahlen sind Gruppen von Daten, die dazu verwendet werden können, eine Nachricht für jede:n Nutzer:in in Ihrer Campaign zu personalisieren. Wenn Sie eine Auswahl verwenden, richten Sie im Wesentlichen angepasste Filter ein, die auf bestimmten Spalten in Ihrem Katalog basieren. Dies kann Filter für Marke, Größe, Standort, Hinzufügedatum und mehr umfassen. Damit haben Sie die Kontrolle darüber, was Sie den Nutzer:innen zeigen, indem Sie Kriterien festlegen, die die Artikel zuerst erfüllen müssen.<br><br>Auf dieser Seite erfahren Sie, wie Sie Auswahlen mit Ihren Katalogen erstellen und verwenden.

Nachdem Sie einen [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs) erstellt haben, können Sie Ihre Katalogdaten weiter referenzieren, indem Sie Auswahlen in Ihre Braze Campaigns oder Empfehlungen einbauen.

![Der Abschnitt „Auswahlen“ in einem Beispielkatalog.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Wissenswertes {#things-to-know}

- Sie können bis zu 30 Selections pro Katalog erstellen.
- Sie können bis zu 10 Filter pro Selection hinzufügen.
- Selections eignen sich hervorragend zur Verfeinerung von Empfehlungen aus Braze-Katalogdaten. Wenn Sie nach Inspiration suchen, lesen Sie [Über Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations) für Beispiel-Anwendungsfälle.

## Geolocation-Filter {#geolocation-filters}

Wenn Ihr Katalog einen [Geolocation-Feldtyp]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types) enthält, können Sie geolocation-basierte Filter in Ihren Auswahlen verwenden, um Katalogartikel basierend auf ihrer Nähe zu einem geografischen Punkt anzuzeigen.

Zwei Geolocation-Operatoren stehen zur Verfügung:

| Operator | Beschreibung |
| -------- | ----------- |
| `geo within` | Gibt Artikel zurück, deren Geolocation-Feld innerhalb eines bestimmten Radius um einen Mittelpunkt liegt. |
| `geo outside` | Gibt Artikel zurück, deren Geolocation-Feld außerhalb eines bestimmten Radius um einen Mittelpunkt liegt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn ein Geolocation-Filter angewendet wird, werden die Ergebnisse nach Entfernung sortiert, wobei der nächstgelegene Artikel zuerst angezeigt wird.

### Mittelpunkt mit Liquid festlegen {#setting-the-center-point-with-liquid}

Sie können den Mittelpunkt dynamisch mit Liquid festlegen. Um beispielsweise Artikel relativ zum letzten bekannten Standort jedes Nutzers bzw. jeder Nutzerin zu filtern, verwenden Sie das Attribut {% raw %}`{{${most_recent_location}}}`{% endraw %} als Filterwert:

{% raw %}
```
{{${most_recent_location}}}
```
{% endraw %}

### Anwendungsfall: Die nächstgelegenen Shop-Standorte anzeigen {#use-case-show-the-nearest-store-locations}

Angenommen, Ihr Katalog enthält ein Feld `store_location` vom Typ Geolocation. Sie können eine Auswahl erstellen, die den Operator `geo within` verwendet, um Shop-Standorte innerhalb eines festgelegten Radius vom letzten bekannten Standort der einzelnen Nutzer:innen zurückzugeben. Setzen Sie den Filterwert auf {% raw %}`{{${most_recent_location}}}`{% endraw %}, damit sich der Mittelpunkt pro Nutzer:in aktualisiert. Da die Ergebnisse nach Entfernung sortiert werden, ist der erste zurückgegebene Artikel immer der nächstgelegene Shop.

## Auswahl erstellen {#creating-a-selection}

Um eine Auswahl zu erstellen, gehen Sie wie folgt vor.

1. Gehen Sie zu **Kataloge** und wählen Sie Ihren Katalog aus der Liste aus.
2. Wählen Sie den Tab **Auswahl** und klicken Sie auf **Auswahl erstellen**.
3. Geben Sie Ihrer Auswahl einen Namen und optional eine Beschreibung.
4. Wählen Sie unter **Filterfeld** die Katalogspalte aus, nach der Sie filtern möchten. String-Felder mit mehr als 1.000 Zeichen können nicht als Filter ausgewählt werden.
5. Definieren Sie Ihre Filterkriterien, indem Sie den entsprechenden Operator (z. B. „ist gleich“ oder „ist nicht gleich“) und das Attribut auswählen.
6. Legen Sie im Abschnitt **Sortiertyp** fest, wie die Ergebnisse sortiert werden. Standardmäßig werden Ergebnisse in keiner bestimmten Reihenfolge zurückgegeben. Um die Sortierung nach einem bestimmten Feld festzulegen, deaktivieren Sie **Zufällige Sortierreihenfolge** und geben Sie das **Sortierfeld** und die **Sortierreihenfolge** (aufsteigend oder absteigend) an.
7. Geben Sie im Abschnitt **Ergebnislimit** die Anzahl der Ergebnisse ein (bis zu 50).
8. Wählen Sie **Auswahl erstellen**.

### Testen und Vorschau {#test-and-preview}

Nach dem Erstellen einer Auswahl können Sie den Abschnitt **Vorschau für Nutzer:in** verwenden, um zu sehen, was eine Auswahl für eine:n zufällige:n oder eine:n bestimmte:n Nutzer:in zurückgeben würde. Bei Auswahlen, die Personalisierung verwenden, können Sie die Vorschau erst nach der Auswahl einer/eines Nutzer:in anzeigen.

### Liquid in Auswahlergebnissen {#liquid-in-selection-results}

Die Verwendung von Liquid in Katalogen, wie z. B. angepasste Attribute und angepasste Events, kann dazu führen, dass für jede:n Nutzer:in in Ihrer Auswahl unterschiedliche Ergebnisse zurückgegeben werden.

{% alert note %}
Connected-Content-Liquid wird in diesen Filtereinstellungen nicht unterstützt.
{% endalert %}

![Filtereinstellungen für die Katalogauswahl, bei der das Attribut auf ein angepasstes Liquid-Attribut gesetzt ist.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Verwendung von Selections in Nachrichten {#using-selections-in-messaging}

Nachdem Sie Ihre Selection erstellt haben, personalisieren Sie Ihre Nachrichten mit Liquid, um die gefilterten Artikel aus diesem Katalog einzufügen. Sie können Braze das Liquid für Sie über das Personalisierungsfenster in den Nachrichten-Editoren generieren lassen:

1. Wählen Sie in jedem Nachrichten-Editor, der Personalisierung unterstützt, <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Personalisierung hinzufügen"></i> **Personalisierung hinzufügen** aus, um das Personalisierungsfenster zu öffnen.
2. Wählen Sie für **Personalisierungstyp** die Option **Katalogartikel** aus.
3. Wählen Sie Ihren Katalognamen aus.
4. Wählen Sie für **Artikelauswahlmethode** die Option **Selection verwenden** aus.
4. Wählen Sie Ihre Selection aus der Liste aus.
5. Wählen Sie für **Anzuzeigende Informationen** aus, welche Felder aus dem Katalog für jeden Artikel enthalten sein sollen.
6. Wählen Sie das **Kopieren**-Symbol aus und fügen Sie das Liquid an der gewünschten Stelle in Ihre Nachricht ein.

![Das Modal „Personalisierung hinzufügen“ mit den folgenden Auswahlen: „Katalogartikel“ für „Personalisierungstyp“, „Games“ für „Katalogname“, „Selections“ für „Selection-Typ“, „game_selection“ für „Selection“ sowie „title“ und „description_en“ für „Anzuzeigende Informationen“.]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

{% alert note %}
Die Personalisierungsvorschau im Liquid-Kompositionspanel zeigt bis zu drei Katalog-Selections an, unabhängig vom von Ihnen festgelegten Ergebnislimit. Dies ist das erwartete Verhalten – die tatsächlich an Nutzer:innen gesendete Nachricht berücksichtigt Ihr konfiguriertes Ergebnislimit.
{% endalert %}

## Anwendungsfall {#use-case}

Nehmen wir an, Sie betreiben einen Essenslieferdienst und möchten eine personalisierte Nachricht an Nutzer:innen senden, die bestimmte Essensvorlieben haben, basierend auf der zuletzt angesehenen Lebensmittelkategorie.

Mit einem Katalog, der die Informationen Ihres Essenslieferdienstes zu Mahlzeitenname, Preis, Bild und Kategorie der Mahlzeit enthält, können Sie eine Auswahl erstellen, um drei Mahlzeiten basierend auf der zuletzt angesehenen Kategorie der Nutzer:innen zu empfehlen.

![Ein Beispiel für eine Auswahl für einen Essenslieferdienst mit zwei Filtern: einer, der einen Produkttyp als Mahlzeit identifiziert, und einer, der die Kategorie als die zuletzt angesehene identifiziert. Die Auswahl ist so eingestellt, dass die Reihenfolge der drei Ergebnisse zufällig zurückgegeben wird.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Um diesen Katalog und diese Auswahl in einer Campaign zu verwenden, nutzen Sie das Modal **Personalisierung hinzufügen** im Bereich der Nachrichtenzusammenstellung beim Erstellen einer Campaign. In diesem Beispiel haben wir den Katalog mit den Informationen Ihres Essenslieferdienstes und die Auswahl für Mahlzeitenempfehlungen basierend auf der zuletzt angesehenen Kategorie ausgewählt. Damit können wir den Mahlzeitenname und den Preis anzeigen. Um Ihre Nachricht weiter auszubauen, können Sie die Auswahl auch verwenden, um ein Bild der ersten empfohlenen Mahlzeit hinzuzufügen.

![Eine Content-Card mit der Überschrift „You will LOVE these highly rated meals!“ mit der Auswahl „recommendations_be_recent_category“ im Bereich der Nachrichtenzusammenstellung.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Nehmen wir beispielsweise an, Sie haben eine:n Nutzer:in, deren zuletzt angesehene Kategorie „Chicken“ ist. Mithilfe der festgelegten Personalisierung und einer Content-Card-Kampagne können Sie drei Mahlzeitenempfehlungen senden, die Hähnchen für diese:n Nutzer:in enthalten.

![Eine Content-Card mit einem Bild von gegrilltem Zitronen-Hähnchen und einer Liste von drei Mahlzeitenempfehlungen, die Hähnchen enthalten, basierend auf der zuletzt angesehenen Kategorie der Nutzer:innen.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

Mithilfe der gleichen Personalisierung können Sie auch drei Mahlzeitenempfehlungen für eine:n Nutzer:in senden, deren zuletzt angesehene Kategorie „Beef“ ist.

![Eine Content-Card mit einem Bild von Beef Stroganoff und einer Liste von zwei Mahlzeitenempfehlungen, die Rindfleisch enthalten, basierend auf der zuletzt angesehenen Kategorie der Nutzer:innen.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}