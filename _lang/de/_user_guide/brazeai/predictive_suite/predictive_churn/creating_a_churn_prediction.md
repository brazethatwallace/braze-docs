---
nav_title: Churn-Prognose erstellen
article_title: Churn-Prognose erstellen
description: "Dieser Artikel beschreibt, wie Sie im Braze-Dashboard eine Churn-Prognose erstellen."
page_order: 1.1

---

# Churn-Prognose erstellen {#create-a-churn-prediction}

> Erfahren Sie, wie Sie im Braze-Dashboard eine Churn-Prognose erstellen.

## 1. Schritt: Neue Prognose erstellen {#step-1-create-a-new-prediction}

Gehen Sie in Braze zu **Analytics** > **Predictive Churn**.

Eine Prognose ist eine Instanz eines trainierten Modells für maschinelles Lernen und aller Parameter und Daten, die es verwendet. Auf dieser Seite sehen Sie eine Liste der aktuell aktiven Prognosen zusammen mit einigen grundlegenden Informationen. Hier können Sie Prognosen umbenennen, archivieren und neue erstellen. Archivierte Prognosen sind inaktiv und aktualisieren keine Nutzer:innen-Bewertungen.

Um eine neue Prognose zu erstellen, wählen Sie **Create Prediction** und dann eine neue **Churn Prediction**.

{% alert note %}
Es gibt eine Obergrenze von fünf gleichzeitig aktiven Churn-Prognosen. Vor dem Erwerb von Predictive Churn ist die Anzahl auf eine aktive Vorschau-Churn-Prognose begrenzt. Eine Vorschau-Churn-Prognose aktualisiert die Bewertungen nicht regelmäßig und ermöglicht es Ihnen nicht, Nutzer:innen auf Grundlage der Prognoseausgabe gezielt anzusprechen. Kontaktieren Sie Ihren Account Manager für weitere Informationen.
{% endalert %}

Auf der Seite **Basics** geben Sie Ihrer neuen Prognose einen eindeutigen Namen. Sie können auch eine optionale Beschreibung eingeben, um sich Notizen zu dieser speziellen Prognose zu machen.

Wählen Sie **Forward**, um zum nächsten Schritt zu gelangen. Alternativ können Sie **Build Now** auswählen, um alle Standardeinstellungen zu verwenden und zum letzten Schritt der Erstellung zu springen. Sie haben die Möglichkeit, die Einstellungen zu überprüfen, bevor Sie den Erstellungsprozess starten. Sie können jederzeit zu einem früheren Schritt zurückkehren, indem Sie ihn im Fortschrittsbalken auswählen.

## 2. Schritt: Churn definieren {#step-2-define-churn}

Verwenden Sie im Bereich **Churn Definition** die bereitgestellten Filter, um festzulegen, wie Sie die Nutzer:innen-Abwanderung für Ihr Unternehmen definieren. Mit anderen Worten: Was muss ein:e Nutzer:in in welchem Zeitraum tun, damit Sie sie:ihn als abgewandert betrachten?

Denken Sie daran, dass Sie nicht erklären müssen, welche Verhaltensweisen der Abwanderung vorausgehen – nur, was ein:e Nutzer:in zu einer:m abgewanderten Nutzer:in macht. Stellen Sie sich das so vor, dass ein:e Nutzer:in etwas entweder einmal tut (`do`) oder nicht mehr tut (`do not`), was als Abwanderung gilt. Sie könnten zum Beispiel Nutzer:innen, die Ihre App seit 7 Tagen nicht mehr geöffnet haben, als abgewandert betrachten. Sie können auch die Deinstallation oder angepasste Events wie die Abmeldung, die Deaktivierung eines Kontos oder andere Aktionen in Betracht ziehen, die dazu führen, dass ein:e Nutzer:in als abgewandert gilt.

#### Churn-Fenster {#churn-window}

Das Churn-Fenster ist der Zeitraum, in dem die Aktivität einer:s Nutzer:in die Kriterien für die Abwanderung erfüllt. Sie können es je nach verfügbaren Daten auf bis zu 60 Tage einstellen. Dieses Fenster dient dazu, historische Daten abzurufen, um Ihre Prognose zu trainieren. Sobald die Prognose erstellt ist, können Sie feststellen, ob ausreichend Daten für genaue Ergebnisse vorhanden waren.

Nachdem die Prognose erstellt wurde und die Nutzer:innen ihre Bewertungen erhalten haben, zeigt der _Churn-Risiko-Score_ an, wie wahrscheinlich es ist, dass ein:e Nutzer:in innerhalb des im Churn-Fenster festgelegten Zeitraums abwandert.

Hier ein Beispiel für eine einfache Definition auf Grundlage ausbleibender Sitzungen in den letzten 7 Tagen.

![Churn-Definition: Ein:e Nutzer:in gilt als abgewandert, wenn sie:er innerhalb von 7 Tagen keine Sitzung startet]({% image_buster /assets/img/churn/churn1.png %})

Für diesen Fall wählen wir `do not` und `start a session` aus. Sie können andere Filter mit `AND` und `OR` nach Belieben kombinieren, um die gewünschte Definition zu erstellen. Interessieren Sie sich für mögliche Churn-Definitionen? Im folgenden Abschnitt zu den [Beispieldefinitionen für Churn](#sample-definitions) finden Sie einige Anregungen.

{% alert note %}
Bei `do` nehmen wir an, dass aktive Nutzer:innen die von Ihnen für diese Zeile angegebene Aktion nicht durchgeführt haben, bevor sie abgewandert sind. Die Durchführung dieser Aktion führt zur Abwanderung. <br><br>Bei `do not` betrachten wir aktive Nutzer:innen als diejenigen, die diese Aktion in den Tagen zuvor durchgeführt haben und dann damit aufgehört haben. <br><br>**Beispiel:** Wenn Churn als „hat in den letzten 60 Tagen keine Sitzung gestartet“ definiert wird, betrachten wir diejenigen als aktive Nutzer:innen, die in den letzten 60 Tagen eine Sitzung gestartet haben. Daher wird jede:r, der:die in den letzten 60 Tagen keine Sitzung gestartet hat, nicht als aktive:r Nutzer:in betrachtet. Das bedeutet, dass eine anhand dieser Churn-Definition erstellte Churn-Zielgruppe nur Nutzer:innen umfasst, die in den letzten 60 Tagen eine Sitzung gestartet haben. Dies kann dazu führen, dass die resultierende Predictive-Churn-Zielgruppe deutlich kleiner erscheint als die ursprüngliche Population – die meisten Nutzer:innen in einem Workspace könnten bereits die Churn-Definition erfüllen und daher in der Churn-Prognose nicht als aktiv gelten.
{% endalert %}

Unterhalb der Definition sehen Sie Schätzungen darüber, wie viele Nutzer:innen (die in der Vergangenheit abgewandert sind und die nach Ihrer Definition nicht abgewandert sind) verfügbar sind. Sie sehen auch die erforderlichen Mindestwerte. Braze muss über diese Mindestanzahl von Nutzer:innen in den historischen Daten verfügen, damit die Prognose über genügend Daten verfügt, um daraus zu lernen.

## 3. Schritt: Prognosezielgruppe filtern {#step-3-filter-your-prediction-audience}

Ihre Prognosezielgruppe ist die Gruppe von Nutzer:innen, für die Sie das Churn-Risiko prognostizieren möchten. Die Prognosezielgruppe definiert die Gruppe von Nutzer:innen, die das Modell für maschinelles Lernen betrachtet, um aus der Vergangenheit zu lernen. Standardmäßig ist diese Option auf **All Users** eingestellt, was bedeutet, dass diese Prognose Churn-Risiko-Scores für alle Ihre aktiven Nutzer:innen erstellt (Informationen dazu, wer für ein Churn-Modell als aktiv gilt, finden Sie im vorherigen Hinweis).

Je nach Anwendungsfall können Sie Filter verwenden, um die Nutzer:innen anzugeben, die Sie für das Modell bewerten möchten. Wählen Sie dazu **Define my own prediction audience** und wählen Sie Ihre Zielgruppen-Filter. Wenn Sie beispielsweise eine Mitfahr-App mit Fahrer:innen und Fahrgästen in Ihrer Nutzerbasis betreiben und ein Churn-Modell für Fahrgäste erstellen, sollten Sie Ihre Prognosezielgruppe auf Fahrgäste beschränken. Beachten Sie, dass es in vielen Anwendungsfällen nicht erforderlich ist, eine bestimmte Prognosezielgruppe auszuwählen. Wenn Ihr Anwendungsfall beispielsweise darin besteht, Nutzer:innen in der EU-Region gezielt anzusprechen, bei denen die Wahrscheinlichkeit der Abwanderung am höchsten ist, können Sie Ihr Modell auf alle Nutzer:innen anwenden und dann einfach einen Filter für die EU-Region im Segment der Campaign einfügen.

Braze zeigt Ihnen die geschätzte Größe Ihrer Prognosezielgruppe an. Wenn Sie Ihre gewünschte Zielgruppe angeben und die Mindestanforderungen für die Ausführung des Modells nicht erfüllen, versuchen Sie, einen breiteren Filter anzugeben, oder verwenden Sie die Option **All Users**. Beachten Sie, dass die Größe Ihrer Gruppe „Alle Nutzer:innen“ nicht statisch ist und von Modell zu Modell variiert, da sie Ihre Churn-Definition berücksichtigt. Angenommen, die Churn-Definition lautet, dass innerhalb von 30 Tagen **keine** Sitzung gestartet wurde. In diesem Fall wendet Braze das Modell auf Nutzer:innen an, die in den letzten 30 Tagen eine Sitzung gestartet **haben** (und prognostiziert die Wahrscheinlichkeit, dass sie in den nächsten 30 Tagen **keine** Sitzung starten werden). Diese Nutzer:innen werden dann in der Metrik „Alle Nutzer:innen“ berücksichtigt.

{% alert note %}
Die Prognosezielgruppe darf 100 Millionen Nutzer:innen nicht überschreiten.
{% endalert %}

Wenn das Prognosefenster 14 Tage oder weniger beträgt, **darf** das Zeitfenster für Filter, die mit „Last…“ beginnen, wie „Last Used App“ und „Last placed an order“, **das in der Churn-Definition angegebene Churn-Fenster nicht überschreiten**. Wenn Ihre Churn-Definition beispielsweise ein Zeitfenster von 14 Tagen hat, darf das Zeitfenster für die „Last…“-Filter 14 Tage nicht überschreiten.

Das Churn-Fenster wird anhand der Anzahl der Tage seit dem letzten Ausführen des Modells berechnet. Wenn das Churn-Fenster also 15 Tage beträgt und das Modell zuletzt am 1. Dezember ausgeführt wurde, analysiert das Modell den Zeitraum vom 16. bis zum 30. November, um die Nutzer:innen-Aktivität für die Zielgruppenberechtigung und das Training zu erfassen.

#### Alle-Filter-Modus {#full-filter-mode}

Um umgehend eine neue Prognose zu erstellen, wird nur eine Teilmenge der Braze-Segmentierungsfilter unterstützt. Im Alle-Filter-Modus können Sie alle Braze-Filter verwenden, jedoch ist ein Churn-Fenster erforderlich, um die Prognose zu erstellen. Wenn das Churn-Fenster beispielsweise auf 15 Tage eingestellt ist, dauert es 15 Tage, um die Nutzerdaten zu sammeln und die Prognose zu erstellen, wenn Sie Filter verwenden, die nur im Alle-Filter-Modus unterstützt werden. Außerdem sind einige Schätzungen zu Zielgruppengrößen im Alle-Filter-Modus nicht verfügbar.

Eine Beispielliste mit Definitionen für die Prognosezielgruppe finden Sie im folgenden Abschnitt zu den [Beispieldefinitionen für Churn](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Genau wie auf der vorherigen Seite sehen Sie im unteren Bereich die geschätzte Anzahl der historischen Nutzer:innen, die sich aus Ihrer Churn-Definition und Prognosezielgruppen-Definition ergeben. Diese Schätzungen müssen die angegebenen Mindestanforderungen erfüllen, um eine Prognose erstellen zu können.

## 4. Schritt: Update-Häufigkeit für die Churn-Prognose wählen {#step-4-choose-the-update-frequency-for-churn-prediction}

Das Modell für maschinelles Lernen generiert Ereigniswahrscheinlichkeitswerte für Nutzer:innen, und diese Werte werden auf Grundlage des hier ausgewählten Zeitplans aktualisiert. Sie können Nutzer:innen anhand ihres Ereigniswahrscheinlichkeitswerts gezielt ansprechen.

Wählen Sie die **maximale Häufigkeit der Aktualisierungen**, die Sie für sinnvoll halten. Wenn Sie z. B. eine wöchentliche Aktion versenden möchten, um zu verhindern, dass Nutzer:innen abwandern, stellen Sie die Aktualisierungshäufigkeit auf **Weekly** an einem Tag und zu einer Uhrzeit Ihrer Wahl ein.

![Zeitplan für das Prognose-Update, eingestellt auf täglich um 17 Uhr]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
Vorschau- und Demo-Prognosen aktualisieren das Churn-Risiko der Nutzer:innen niemals. Darüber hinaus erfordern tägliche Updates für Prognosen einen zusätzlichen Kauf im Vergleich zu wöchentlichen oder monatlichen Updates mit Predictive Churn. Um diese Funktionalität zu erwerben, wenden Sie sich an Ihren Account Manager.
{% endalert %}

## 5. Schritt: Prognose erstellen {#step-5-build-prediction}

Überprüfen Sie, ob Ihre Angaben korrekt sind, und wählen Sie **Build Prediction**. Sie können Ihre Änderungen auch als Entwurf speichern, indem Sie **Save As Draft** wählen, um zu dieser Seite zurückzukehren und das Modell später zu erstellen. Nachdem Sie **Build Prediction** ausgewählt haben, beginnt der Prozess zur Generierung des Modells. Dies kann je nach Datenvolumen zwischen 30 Minuten und einigen Stunden dauern. Für diese Prognose wird eine Seite angezeigt, auf der erläutert wird, dass das Training während des Modellbildungsprozesses läuft. Das Braze-Modell berücksichtigt angepasste Events, Kauf-Events, E-Commerce-Events, Campaign-Interaktions-Events und Sitzungsdaten.

Nach Abschluss wechselt die Seite automatisch zur Analytics-Ansicht, und Sie erhalten eine E-Mail, die Sie darüber informiert, dass die Prognose und die Ergebnisse verfügbar sind. Im Falle eines Fehlers kehrt die Seite in den Bearbeitungsmodus zurück und gibt eine Erklärung, was schiefgelaufen ist.

Die Prognose wird alle **zwei Wochen automatisch** neu erstellt („retrainiert“), um sie auf Grundlage der neuesten verfügbaren Daten aktuell zu halten. Beachten Sie, dass dies ein anderer Prozess ist als die Erstellung der _Churn-Risiko-Scores_ der Nutzer:innen, die die Ausgabe der Prognose sind. Letzteres hängt von der Update-Häufigkeit ab, die Sie in [Schritt 4](#step-4-choose-the-update-frequency-for-churn-prediction) gewählt haben.

## Beispieldefinitionen für Churn und Prognosezielgruppen {#sample-definitions}

**Beispiele für Churn-Definitionen**<br>
- „Innerhalb von 7 Tagen ein angepasstes Event ‚Abo-Kündigung' durchführen“<br>
- „Innerhalb von 30 Tagen ein angepasstes Event ‚Probezeit abgelaufen' durchführen“<br>
- „Innerhalb von 1 Tag deinstallieren.“<br>
- „Innerhalb von 14 Tagen keinen Kauf tätigen.“<br>

Für die oben skizzierten Churn-Definitionen gibt es möglicherweise entsprechende Definitionen für Prognosezielgruppen:<br>
- **Abo vor mehr als 2 Wochen begonnen ODER Abo vor weniger als zwei Wochen begonnen**<br>Vielleicht möchten Sie in diesem Fall 2 Prognosen erstellen und neuen Abonnent:innen andere Nachrichten schicken als längerfristigen Abonnent:innen. Sie könnten dies auch als „Erster getätigter Kauf vor mehr als 30 Tagen“ definieren.<br>
- **Deinstallationen**<br>Sie könnten sich auf Kund:innen konzentrieren, die in der jüngsten Vergangenheit etwas gekauft oder die App erst kürzlich genutzt haben.<br>
- **Diejenigen, die Gefahr laufen, keinen Kauf zu tätigen, als Churn-Definition**<br>Sie möchten sich möglicherweise auf Kund:innen konzentrieren, die kürzlich Ihre App besucht, darin gesucht oder mit ihr interagiert haben. Vielleicht kann die richtige Rabattaktion die Abwanderung dieser engagierten Gruppe verhindern.

## Archivierte Prognosen {#archived-predictions}

Bei archivierten Prognosen werden die Nutzer:innen-Bewertungen nicht mehr aktualisiert. Alle archivierten Prognosen, die wieder aktiviert werden, aktualisieren die Nutzer:innen-Bewertungen weiterhin nach ihrem festgelegten Zeitplan. Archivierte Prognosen werden nie gelöscht und bleiben in der Liste.