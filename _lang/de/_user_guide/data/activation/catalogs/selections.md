---
nav_title: Auswahlen
article_title: Auswahlen
page_order: 5
alias: /catalog_selections/
description: "In diesem Referenzartikel erfahren Sie, wie Sie Auswahlen mit Ihren Katalogen erstellen und verwenden, um Daten in Ihren Braze Campaigns zu referenzieren."
---

# Auswahlen {#selections}

> Auf dieser Seite erfahren Sie, wie Sie Auswahlen mit Ihren [Katalogen]({{site.baseurl}}/user_guide/data/activation/catalogs/) erstellen und verwenden.

## So funktioniert es {#how-it-works}

Auswahlen sind Gruppen von Daten, die dazu verwendet werden können, eine Nachricht für jede:n Nutzer:in in Ihrer Campaign zu personalisieren. Wenn Sie eine Auswahl verwenden, richten Sie im Wesentlichen angepasste Filter ein, die auf bestimmten Spalten in Ihrem Katalog basieren. Dies kann Filter für Marke, Größe, Standort, Hinzufügedatum und mehr umfassen. Damit haben Sie die Kontrolle darüber, was Sie den Nutzer:innen zeigen, indem Sie Kriterien festlegen, die die Artikel zuerst erfüllen müssen.

Nachdem Sie einen Katalog erstellt haben, können Sie Ihre Katalogdaten weiter referenzieren, indem Sie Auswahlen in Ihre Braze Campaigns oder Empfehlungen einbauen.

![Der Abschnitt „Auswahlen“ in einem Beispielkatalog.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Was Sie wissen sollten {#things-to-know}

- Sie können bis zu 30 Auswahlen pro Katalog erstellen.
- Sie können bis zu 10 Filter pro Auswahl hinzufügen.
- Auswahlen eignen sich hervorragend zur Verfeinerung von Empfehlungen aus Braze-Katalogdaten. Wenn Sie nach Inspiration suchen, sehen Sie sich die Anwendungsbeispiele unter [Über Artikelempfehlungen]({{site.baseurl}}/user_guide/brazeai/item_recommendations/) an.

## Eine Auswahl erstellen {#creating-a-selection}

Um eine Auswahl zu erstellen, gehen Sie wie folgt vor.

1. Gehen Sie zu **Catalogs** und wählen Sie Ihren Katalog aus der Liste aus.
2. Wählen Sie den Tab **Selection** und klicken Sie auf **Create Selection**.
3. Geben Sie Ihrer Auswahl einen Namen und optional eine Beschreibung.
4. Wählen Sie unter **Filter Field** die Katalogspalte aus, nach der Sie filtern möchten. String-Felder mit mehr als 1.000 Zeichen können nicht für Filter ausgewählt werden.
5. Schließen Sie die Definition Ihrer Filterkriterien ab, indem Sie den entsprechenden Operator (z. B. „equals“ oder „does not equal“) und das Attribut auswählen.
6. Im Abschnitt **Sort type** legen Sie fest, wie die Ergebnisse sortiert werden. Standardmäßig werden die Ergebnisse in keiner bestimmten Reihenfolge zurückgegeben. Um die Sortierung nach einem bestimmten Feld festzulegen, deaktivieren Sie **Randomize Sort Order** und geben Sie das **Sort Field** und die **Sort Order** (aufsteigend oder absteigend) an.
7. Geben Sie im Abschnitt **Results limit** die Ergebnisse ein (bis zu 50).
8. Wählen Sie **Create Selection**.

### Test und Vorschau {#test-and-preview}

Nachdem Sie eine Auswahl erstellt haben, können Sie im Bereich **Preview for user** sehen, was die Auswahl für eine:n zufällige:n oder eine:n bestimmte:n Nutzer:in ergeben würde. Bei Auswahlen, die Personalisierung verwenden, können Sie die Vorschau erst nach dem Auswählen einer Nutzerin oder eines Nutzers sehen.

### Liquid in den Auswahlergebnissen {#liquid-in-selection-results}

Die Verwendung von Liquid in Katalogen, wie z. B. angepasste Attribute und angepasste Events, kann dazu führen, dass für jede:n Nutzer:in in Ihrer Auswahl unterschiedliche Ergebnisse zurückgegeben werden.

{% alert note %}
Connected-Content-Liquid wird in diesen Filtereinstellungen nicht unterstützt.
{% endalert %}

![Filtereinstellungen für die Katalogauswahl, bei der das Attribut auf ein angepasstes Liquid-Attribut gesetzt ist.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Auswahlen im Messaging verwenden {#using-selections-in-messaging}

Nachdem Sie Ihre Auswahl erstellt haben, personalisieren Sie Ihre Nachrichten mit Liquid, um die gefilterten Artikel aus diesem Katalog einzufügen. Sie können Braze das Liquid über das Personalisierungsfenster in den Nachrichten-Editoren für Sie generieren lassen:

1. Wählen Sie in jedem Nachrichten-Editor, der Personalisierung unterstützt, <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Personalisierung hinzufügen"></i>, um das Personalisierungsfenster zu öffnen.
2. Wählen Sie für **Personalization Type** die Option **Catalog Items**.
3. Wählen Sie Ihren Katalognamen aus.
4. Wählen Sie für **Item selection method** die Option **Use a selection**.
4. Wählen Sie Ihre Auswahl aus der Liste aus.
5. Wählen Sie unter **Information to Display** aus, welche Felder aus dem Katalog für jeden Artikel angezeigt werden sollen.
6. Wählen Sie das Symbol **Copy** und fügen Sie das Liquid an der gewünschten Stelle in Ihrer Nachricht ein.

![Das Modal „Add Personalization“ mit den folgenden Auswahlmöglichkeiten: „Catalog Items“ für „Personalization Type“, „Games“ für „Catalog Name“, „Selections“ für „Selection Type“, „game_selection“ für „Selection“ und „title“ und „description_en“ für „Information to Display“.]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## Anwendungsfall {#use-case}

Nehmen wir an, Sie besitzen einen Essenslieferdienst und möchten Ihren Nutzer:innen, die bestimmte Essensvorlieben haben, eine personalisierte Nachricht auf der Grundlage ihrer zuletzt angesehenen Lebensmittelkategorie senden.

Mithilfe eines Katalogs mit den Informationen Ihres Essenslieferdienstes zu Name, Preis, Bild und Kategorie der Mahlzeit können Sie eine Auswahl erstellen, um drei Mahlzeiten auf der Grundlage der zuletzt angesehenen Kategorie einer Nutzerin oder eines Nutzers zu empfehlen.

![Ein Beispiel für eine Auswahl eines Essenslieferdienstes mit zwei Filtern: einer, der einen Produkttyp als Mahlzeit identifiziert, und einer, der die Kategorie als die zuletzt angesehene identifiziert. Die Auswahl ist so eingestellt, dass die Reihenfolge, in der die drei Ergebnisse zurückgegeben werden, zufällig ist.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Um diesen Katalog und die Auswahl in einer Campaign zu verwenden, nutzen Sie das Modal **Add Personalization** im Abschnitt Nachrichtenzusammenstellung beim Erstellen einer Campaign. In diesem Beispiel haben wir den Katalog mit den Informationen Ihres Essenslieferdienstes und die Auswahl für Essensempfehlungen basierend auf der zuletzt angesehenen Kategorie ausgewählt. So können wir den Namen und den Preis der Mahlzeit anzeigen. Um Ihre Nachricht weiter auszubauen, können Sie die Auswahl nutzen, um auch ein Bild der ersten empfohlenen Mahlzeit hinzuzufügen.

![Eine Content-Card mit der Überschrift „Sie werden diese hoch bewerteten Mahlzeiten LIEBEN!“ mit der Auswahl „recommendations_be_recent_category“ im Bereich Nachrichtengestaltung.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Nehmen wir an, Sie haben eine:n Nutzer:in, deren/dessen zuletzt angesehene Kategorie „Huhn“ ist. Mit der eingestellten Personalisierung und einer Content-Card-Kampagne können Sie dieser/diesem Nutzer:in drei Essensempfehlungen mit Huhn senden.

![Eine Content-Card mit einem Bild von gegrilltem Zitronenhähnchen und einer Liste von drei Essensempfehlungen, die Hähnchen enthalten, basierend auf der zuletzt angesehenen Kategorie der Nutzerin oder des Nutzers.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

Mit der gleichen Personalisierung können Sie auch drei Essensempfehlungen an eine:n Nutzer:in senden, deren/dessen zuletzt angesehene Kategorie „Rindfleisch“ ist.

![Eine Content-Card mit einem Bild von Bœuf Stroganoff und einer Liste von zwei Essensempfehlungen, die Rindfleisch enthalten, basierend auf der zuletzt angesehenen Kategorie der Nutzerin oder des Nutzers.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}