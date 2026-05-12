---
nav_title: Event-Prognose erstellen
article_title: Event-Prognose erstellen
page_order: 1.1
description: "In diesem Artikel erfahren Sie, wie Sie im Braze-Dashboard eine Event-Prognose erstellen."

---

# Event-Prognose erstellen {#create-an-event-prediction}

> Eine Prognose ist eine Instanz eines trainierten Modells des maschinellen Lernens und aller Parameter und Daten, die es verwendet. Um mehr über Predictive Events zu erfahren, lesen Sie die [Übersicht über Predictive Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/).

Gehen Sie in Braze zu **Analytics** > **Predictive Events**.

Auf dieser Seite sehen Sie eine Liste aktueller aktiver Event-Prognosen und einige grundlegende Informationen dazu. Hier können Sie Prognosen umbenennen, archivieren und neue erstellen. Archivierte Prognosen sind inaktiv und aktualisieren die Bewertungen der Nutzer:innen nicht.

## 1. Schritt: Neue Prognose erstellen {#step-1-create-a-new-prediction}

1. Wählen Sie **Create Prediction** und dann eine neue **Event Prediction**.

{% alert note %}
Es gibt ein Limit von fünf gleichzeitig aktiven Prognosen. Vor dem Kauf von Predictive Events ist das Limit eine aktive Vorschauprognose. Eine Vorschauprognose aktualisiert nicht regelmäßig die Bewertungen und spricht keine Nutzer:innen auf Grundlage der Prognoseergebnisse an. Kontaktieren Sie Ihren Account Manager für weitere Informationen.
{% endalert %}

{: start="2"}
2. Geben Sie Ihrer Prognose einen eindeutigen Namen. Sie können auch eine Beschreibung eingeben, um relevante Notizen zu speichern.

![]({% image_buster /assets/img/purchasePrediction/purchases_step1.png %})

{: start="3"}
3. Klicken Sie auf **Forward**, um zum nächsten Schritt zu gelangen. <br><br>Optional können Sie auf **Build Now** klicken, um alle Standardeinstellungen zu verwenden und zum letzten Schritt der Erstellung zu springen. Sie haben die Möglichkeit, die Einstellungen zu überprüfen, bevor Sie den Erstellungsprozess starten. Außerdem können Sie später zu jedem Schritt zurückkehren, indem Sie ihn in der oberen Leiste anklicken.

## 2. Schritt: Event-Tracking festlegen {#event-tracking}

Geben Sie an, ob die Events Ihrer Nutzer:innen in Braze als [Kauf-Events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events/), [angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events/) oder als [Bestellungs-Event]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/?tab=ecommerce.order_placed) gespeichert werden.

Hier sehen Sie, ob die ausgewählte Methode genügend Daten für Braze liefert, um ein Modell des maschinellen Lernens zu erstellen. Wenn die Anforderung nicht erfüllt ist, versuchen Sie, die andere Protokollierungsmethode auszuwählen, sofern diese ebenfalls von Ihrer Anwendung verwendet wird. Leider ist Braze nicht in der Lage, mit der Menge der verfügbaren Daten eine Prognose zu erstellen, wenn dies nicht der Fall ist. Wenn Sie glauben, dass Sie diesen Fehler fälschlicherweise sehen, wenden Sie sich an Ihren Customer-Success-Manager.

#### Event-Fenster {#event-window}

Das Event-Fenster ist der Zeitrahmen, in dem Sie prognostizieren möchten, ob ein:e Nutzer:in das Event durchführen wird. Es kann auf bis zu 60 Tage eingestellt werden. Dieses Fenster wird verwendet, um historische Daten für das Training der Prognose abzufragen. Nachdem die Prognose erstellt wurde und Nutzer:innen Bewertungen erhalten haben, zeigt der Wahrscheinlichkeitswert an, wie wahrscheinlich es ist, dass ein:e Nutzer:in das Event innerhalb der durch das Event-Fenster festgelegten Anzahl von Tagen durchführt.

### 3. Schritt: Prognosezielgruppe filtern (optional) {#audience}

Ihre Prognosezielgruppe ist die Gruppe von Nutzer:innen, deren Wahrscheinlichkeitswert Sie vorhersagen möchten. Falls gewünscht, können Sie eine Prognose für Ihre gesamte Nutzerpopulation durchführen. Lassen Sie dazu die Standardoption **All Users** ausgewählt.

Je nach Anwendungsfall können Sie Filter verwenden, um die Nutzer:innen anzugeben, die Sie für das Modell bewerten möchten. Wählen Sie dazu **Define my own prediction audience** und wählen Sie Ihre Zielgruppen-Filter. Sie könnten sich zum Beispiel auf Nutzer:innen konzentrieren, die Ihre App seit mindestens 30 Tagen nutzen, indem Sie den Filter „First Used App“ auf 30 Tage setzen. Durch die Einrichtung dieser Zielgruppe wird Braze mitgeteilt, dass Ihr Modell speziell von Nutzer:innen lernen soll, die (zum Zeitpunkt der Ausführung des Modells) die App seit mindestens 30 Tagen verwenden.

{% alert important %}
Konzentrieren Sie Ihre Filter auf für Ihren Anwendungsfall relevante Nutzermerkmale, wie aktive Nutzer:innen, neue Nutzer:innen, hochwertige Nutzer:innen oder Nutzer:innen in einem bestimmten Land. Filtern Sie Ihre Prognosezielgruppe nicht danach, ob die Nutzer:innen das von Ihnen vorhergesagte Event bereits durchgeführt haben. Die Prognosezielgruppe bestimmt, von wem das Modell lernen soll, nicht das Event-Ergebnis selbst. Das Modell muss sowohl Nutzer:innen, die das Event abgeschlossen haben, als auch Nutzer:innen, die dies nicht getan haben, beobachten, um die Wahrscheinlichkeit des zukünftigen Event-Abschlusses genau zu erlernen und Prognosen darüber zu erstellen.
{% endalert %}

Die Prognosezielgruppe definiert die Gruppe der Nutzer:innen, die das Modell des maschinellen Lernens betrachtet, um aus der Vergangenheit zu lernen. Braze zeigt Ihnen die geschätzte Größe Ihrer Prognosezielgruppe an. Wenn Sie Ihre gewünschte Zielgruppe angeben und die Mindestanforderungen für die Ausführung des Modells nicht erfüllen, versuchen Sie, einen breiteren Filter anzugeben, oder verwenden Sie die Option **All Users**. Beachten Sie, dass es in vielen Anwendungsfällen nicht erforderlich ist, eine bestimmte Prognosezielgruppe auszuwählen. Wenn Ihr Anwendungsfall beispielsweise darin besteht, Nutzer:innen in der EU-Region anzusprechen, bei denen die Churn-Wahrscheinlichkeit am höchsten ist, können Sie Ihr Modell auf alle Nutzer:innen anwenden und dann einen Filter für die EU-Region in das Segment der Campaign einfügen.

{% alert note %}
Die Prognosezielgruppe darf 100 Millionen Nutzer:innen nicht überschreiten.
{% endalert %}

Wenn das Event-Fenster 14 Tage oder weniger beträgt, kann das Zeitfenster für Filter, die mit „Last…“ beginnen, wie z. B. „Last Used App“ und „Last placed an order“, **das im [Event-Tracking](#event-tracking) angegebene Event-Fenster nicht überschreiten**. Wenn zum Beispiel das Event-Fenster auf 14 Tage eingestellt ist, kann das Zeitfenster für die „Last…“-Filter 14 Tage nicht überschreiten.

#### Alle-Filter-Modus {#full-filter-mode}

Um sofort eine neue Prognose erstellen zu können, wird nur eine Teilmenge der Braze-Segmentierungsfilter unterstützt. Im Alle-Filter-Modus können Sie alle Braze-Filter verwenden, benötigen aber ein Event-Fenster, um die Prognose zu erstellen.

Wenn zum Beispiel das Event-Fenster auf 14 Tage eingestellt ist, dauert es 14 Tage, um die Nutzerdaten zu sammeln und die Prognose zu erstellen, wenn Sie Filter verwenden, die nur im Alle-Filter-Modus unterstützt werden. Außerdem sind einige Schätzungen über Zielgruppengrößen im Alle-Filter-Modus nicht verfügbar.

### 4. Schritt: Aktualisierungszeitplan wählen {#step-4-choose-the-update-schedule}

Das Modell des maschinellen Lernens generiert Event-Wahrscheinlichkeitswerte für Nutzer:innen, und diese Werte werden auf Grundlage des hier ausgewählten Zeitplans aktualisiert. Sie können Nutzer:innen anhand ihres Event-Wahrscheinlichkeitswerts gezielt ansprechen.

Wählen Sie die **maximale Häufigkeit der Aktualisierungen**, die Sie für sinnvoll halten. Wenn Sie beispielsweise Bestellungen prognostizieren und eine wöchentliche Aktion planen, stellen Sie die Häufigkeit der Updates auf **Weekly** an einem Tag und zu einer Uhrzeit Ihrer Wahl ein.

{% alert note %}
Vorschau- und Demo-Prognosen aktualisieren die Wahrscheinlichkeitswerte der Nutzer:innen nicht.
{% endalert %}

### 5. Schritt: Prognose erstellen {#step-5-build-prediction}

Überprüfen Sie, ob Ihre Angaben korrekt sind, und wählen Sie **Build Prediction**. Sie können Ihre Änderungen auch als Entwurf speichern, indem Sie **Save As Draft** wählen, um zu dieser Seite zurückzukehren und das Modell später zu erstellen.

Nachdem Sie auf **Build Prediction** geklickt haben, beginnt der Prozess zur Erstellung des Modells. Dies kann je nach Datenvolumen zwischen 30 Minuten und einigen Stunden dauern. Für diese Prognose sehen Sie eine Seite, auf der erklärt wird, dass das Training für die Dauer der Modellerstellung im Gange ist. Das Braze-Modell berücksichtigt angepasste Events, Kauf-Events, E-Commerce-Events, Campaign-Interaktions-Events und Sitzungsdaten.

Wenn der Vorgang abgeschlossen ist, wechselt die Seite automatisch in die Analytics-Ansicht, und Sie erhalten eine E-Mail, die Sie darüber informiert, dass die Prognose und die Ergebnisse bereit sind. Im Falle eines Fehlers kehrt die Seite in den Bearbeitungsmodus zurück und gibt eine Erklärung, was schiefgelaufen ist.

Die Prognose wird alle **zwei Wochen** automatisch neu erstellt („trainiert“), um sie auf dem neuesten Stand der verfügbaren Daten zu halten. Beachten Sie, dass dies ein anderer Prozess ist als die Erstellung der Wahrscheinlichkeitswerte der Nutzer:innen, die die Ausgabe der Prognose darstellen. Letzteres hängt von der Häufigkeit der Updates ab, die Sie in [Schritt 4](#step-4-choose-the-update-schedule) gewählt haben.

## Archivierte Prognosen {#archived-predictions}

Bei archivierten Prognosen werden die Bewertungen der Nutzer:innen nicht mehr aktualisiert. Alle archivierten Prognosen, die wieder aktiviert werden, aktualisieren die Bewertungen der Nutzer:innen weiterhin nach ihrem festgelegten Zeitplan. Archivierte Prognosen werden nie gelöscht und bleiben in der Liste.