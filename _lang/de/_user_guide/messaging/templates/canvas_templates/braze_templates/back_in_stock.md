---
nav_title: Wieder auf Lager
article_title: Wieder auf Lager
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie ein Braze-Canvas-Template verwenden, um Käufe zu fördern, indem Sie Ihre Nutzer:innen mit personalisierten Nachrichten benachrichtigen, wenn ein Artikel wieder auf Lager ist."
tool: Canvas
---

# Wieder auf Lager {#back-in-stock}

> Verwenden Sie das Template „Wieder auf Lager“, um Nachrichten zu erstellen, die Nutzer:innen ansprechen, die zuvor einen Artikel angesehen oder Interesse daran bekundet haben, der nicht vorrätig war, aber jetzt wieder zum Kauf verfügbar ist. Dies hilft Nutzer:innen, die gewünschten Produkte zu erhalten, indem sie genau in dem entscheidenden Moment angesprochen werden, in dem ein Produkt wieder verfügbar wird.

Dieser Artikel führt Sie durch einen Anwendungsfall für das Template **Wieder auf Lager**, das für den Conversion-Schritt des Nutzer:innen-Lebenszyklus konzipiert ist. Wenn Sie fertig sind, haben Sie ein Canvas erstellt, das einen Push (Web oder Mobilgerät), eine SMS oder eine E-Mail an Nutzer:innen sendet, wenn ein Artikel wieder auf Lager ist, sowie bis zu zwei Erinnerungen.

## Voraussetzungen {#prerequisites}

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Einen [Katalog]({{site.baseurl}}/user_guide/data/activation/catalogs/create) mit Informationen über Ihren Artikel
- [Wieder-auf-Lager-Benachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications#back-in-stock-notifications) müssen für den Artikel eingerichtet sein, über den Sie Nutzer:innen benachrichtigen möchten

## Das Template an Ihre Bedürfnisse anpassen {#tailoring-the-template-to-your-needs}

Nehmen wir an, wir arbeiten für PantsLabyrinth, einen Direktvertriebshändler für Bekleidung, der sich auf Stoffhosen, Jeans, Culottes und viele andere Hosenarten spezialisiert hat. Wir können das Template „Wieder auf Lager“ verwenden, um Kund:innen über verschiedene Kanäle zu benachrichtigen, wenn eine beliebte Jeans, die Classic Straight Leg, wieder auf Lager ist.

Bevor wir das Canvas erstellen, [richten wir einen Katalog ein]({{site.baseurl}}/user_guide/data/activation/catalogs/create), der Informationen über unser Straight-Leg-Hosen-Sortiment enthält, und [richten Wieder-auf-Lager-Benachrichtigungen ein]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications#setting-up-back-in-stock-notifications) für die Classic Straight Leg Jeans. Wir haben es so eingerichtet, dass Nutzer:innen Benachrichtigungen abonnieren, nachdem sie das angepasste Event ausgeführt haben, die Classic Straight Leg Jeans in der App als Favorit zu markieren.

Um auf das Template „Wieder auf Lager“ zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Canvas-Template verwenden** > **Braze-Templates**. Wählen Sie dann neben **Back in Stock** die Option **Template anwenden**. Jetzt können wir das Template durchgehen und an unsere Bedürfnisse anpassen.

### 1. Schritt: Details einrichten {#step-1-set-up-the-details}

Passen wir die Canvas-Details an, um unser Ziel widerzuspiegeln.

1. Wählen Sie **Bearbeiten** neben dem Template-Namen.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas für das Targeting von Nutzer:innen gedacht ist, wenn unser Produkt Classic Straight Leg wieder auf Lager ist.
3. Aktualisieren Sie die Beschreibung, um zu erklären, dass dieses Canvas personalisierte Nachrichten enthält.
4. Fügen Sie den Tag **Wieder auf Lager** hinzu, der unter dem Tag **Werbung** verschachtelt ist, damit wir auf der Canvas-Startseite danach filtern können.

![Der Schritt „Canvas-Details einrichten“ mit dem Canvas-Namen „Wieder auf Lager – Classic Straight Leg“ und einer kurzen Canvas-Beschreibung.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### 2. Schritt: Konversions-Events zuweisen {#step-2-assign-conversion-events}

Ändern Sie das **Primäres Konversions-Event – A** zu **Einen bestimmten Kauf tätigen** und wählen Sie **Classic Straight Leg** als Produktnamen.

![Der Abschnitt „Konversions-Events zuweisen“ für den Konversions-Event-Typ „Kauf des Produkts Classic Straight Leg“ mit einer Conversion-Frist von 7 Tagen.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### 3. Schritt: Entry-Zeitplan anpassen {#step-3-tailor-the-entry-schedule}

Behalten wir den Entry-Zeitplan als **Aktionsbasiert** bei, damit Nutzer:innen unser Canvas betreten, wenn sie eine Aktion ausführen, die das Template bereits auf **Wieder-auf-Lager-Event ausführen** eingestellt hat.

Wir nehmen zwei Anpassungen an diesem Schritt vor:

1. Wählen Sie den Katalog aus, der Informationen über unsere Classic Straight Leg Jeans enthält, den wir „Straight Leg Pants“ genannt haben.

![Der Schritt „Entry-Zeitplan“ für ein aktionsbasiertes Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2. Legen Sie die **Startzeit (erforderlich)** auf das gewünschte Startdatum und die gewünschte Uhrzeit fest.

![Der Abschnitt „Eintrittsfenster“ mit einer Startzeit am 2. Januar 2025 um 0:00 Uhr.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### 4. Schritt: Zielgruppe auswählen {#step-4-select-the-target-audience}

Wir definieren unsere Zielgruppe als Nutzer:innen, die mit höherer Wahrscheinlichkeit die Classic Straight Leg Jeans kaufen werden.

1. Wählen Sie unser Zielsegment „Favorisiert – Classic Straight Leg Jeans“, das aus Nutzer:innen besteht, die unsere Classic Straight Leg Jeans in unserer App oder auf unserer Website als Favorit markiert haben.
2. Wählen Sie einen Filter, um Nutzer:innen einzuschließen, die „Jeans“ mehr als „0“ Mal gekauft haben.

![Der Schritt „Zielgruppe“ mit dem Segment „Favorisiert – Classic Straight Leg Jeans“.]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3. Passen Sie die Eingangskontrollen an, um Nutzer:innen den erneuten Eintritt in das Canvas nach der maximalen Dauer des Canvas zu ermöglichen, um die Wahrscheinlichkeit zu verringern, dass Nutzer:innen denselben Schritt gleichzeitig auslösen.

![Der Abschnitt „Eingangskontrollen“ mit einem Kontrollkästchen, das Nutzer:innen den erneuten Eintritt in dieses Canvas mit einer maximalen Dauer des Canvas erlaubt.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4. Passen Sie die Austrittskriterien an, um Nutzer:innen zu entfernen, die das angepasste Event ausgeführt haben, die Classic Straight Leg Jeans aus den Favoriten zu entfernen.

![Der Abschnitt „Austrittskriterien“ mit einer Ausnahme für Nutzer:innen, die das angepasste Event „Aus Favoriten entfernt“ ausführen.]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### 5. Schritt: Sendeeinstellungen auswählen {#step-5-select-your-send-settings}

Wir behalten die Standard-Abo-Einstellungen bei, sodass wir nur an Nutzer:innen senden, die Nachrichten oder Benachrichtigungen abonniert haben oder dafür angemeldet sind, und überspringen die anderen Einstellungen (Frequency-Capping, Ruhezeiten und Seed-Gruppen).

![Der Schritt „Sendeeinstellungen“ mit Targeting auf Nutzer:innen, die abonniert oder angemeldet sind.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### 6. Schritt: Ihr Canvas anpassen {#step-6-customize-your-canvas}

Jetzt erstellen wir unser Canvas, indem wir die Kanäle und Inhalte anpassen, die an Nutzer:innen gesendet werden. Da wir alle vier Template-Kanäle (Mobilgerät- und Web-Push, SMS und E-Mail) verwenden und den Filter [Intelligenter Kanal]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) nutzen, müssen wir keine hinzufügen oder entfernen.

{% alert tip %}
Sie können [Canvas-Entry-Eigenschaften]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) verwenden, um die Nachrichten in Ihrem Canvas basierend auf dem Produkt, auf das Sie sich beziehen, anzupassen.
{% endalert %}

Wir beginnen unsere Anpassung, indem wir jeden Nachrichten-Schritt durchgehen und den Inhalt aktualisieren.

1. Ersetzen Sie `!!YOURCATALOGHERE!!` durch unseren Katalognamen („Straight_Leg_Pants“).
2. Ersetzen Sie `[0]` durch die Indexnummer der Classic Straight Leg Jeans, die „9“ ist, da die Jeans der zehnte Artikel im `items`-Array unseres Katalogs ist. (Arrays sind in Liquid nullindexiert, sodass der erste Artikel `0` und nicht `1` ist.)
3. Wiederholen Sie die Schritte 1 und 2 für alle verbleibenden Nachrichten-Schritte, einschließlich:
    - Die Nachricht „In-Product Msg & Email“, die nach der eintägigen Verzögerung gesendet wird
    - Die „Push+Email Alert“-Nachrichten, die an Nutzer:innen gesendet werden, die keinen Kauf getätigt haben
4. Aktualisieren Sie den Aktionspfade-Schritt, indem Sie die Aktionsgruppe **Kauf** auswählen. Wählen Sie dann **Einen bestimmten Kauf tätigen** und wählen Sie die Classic Straight Leg Jeans als Produkt.

![Mobilgerät-Push-Canvas-Schritt mit einer Nachricht, die Nutzer:innen darüber informiert, dass ein Produkt wieder auf Lager ist.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### 7. Schritt: Canvas testen und starten {#step-7-test-and-launch-your-canvas}

Nachdem wir unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten wir es, indem wir **Canvas starten** auswählen. Jetzt erhalten unsere Nutzer:innen, die unsere Classic Straight Leg Jeans als Favorit markiert und unsere Messaging-Kanäle abonniert haben, Benachrichtigungen, wenn die Jeans wieder auf Lager sind!

{% alert tip %}
Sehen Sie sich unsere [Checkliste vor und nach dem Start]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) an, um Dinge zu berücksichtigen, bevor und nachdem Sie ein Canvas starten.
{% endalert %}