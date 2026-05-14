---
nav_title: Inaktive Nutzer:innen
article_title: Inaktive Nutzer:innen
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie ein Braze-Canvas-Template verwenden, um Nutzer:innen mit Anreizen basierend auf ihren bisherigen Interaktionen zurück in Ihre App zu bringen."
tool: Canvas
---

# Inaktive Nutzer:innen {#lapsed-user}

> Verwenden Sie das Template für inaktive Nutzer:innen, um Nutzer:innen an den Mehrwert Ihrer Marke zu erinnern und sie mit attraktiven Angeboten und Anreizen basierend auf ihren bisherigen Interaktionen zur Rückkehr zu motivieren.

Dieser Artikel führt Sie durch einen Anwendungsfall für das Template **Lapsed User**, das für die Bindungs- und Loyalitätsphase des Nutzer:innen-Lebenszyklus konzipiert ist. Am Ende werden Sie ein Canvas erstellt haben, das Nutzer:innen mit Aktionen zur Rückkehr in Ihre App motiviert – basierend auf ihrem Verhalten, z. B. ob sie nach Erhalt einer Werbenachricht eine Sitzung in Ihrer App gestartet haben.

## Voraussetzungen {#prerequisites}

Um das Template für inaktive Nutzer:innen erfolgreich zu verwenden, müssen Sie [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) mit den Partnern und Zielgruppen konfigurieren, die Sie nutzen.

## Das Template an Ihre Bedürfnisse anpassen {#tailoring-the-template-to-your-needs}

Nehmen wir an, wir arbeiten für MovieCanon, einen Streaming-Dienst mit exklusiven Inhalten für Filme und Serien. Wir können das Template für inaktive Nutzer:innen verwenden, um Vorteile und Premium-Inhalte für Nutzer:innen zu bewerben, die unsere App seit 30 Tagen nicht besucht haben.

Bevor wir das Canvas erstellen, richten wir die Integration [Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) ein, damit wir Nutzerdaten aus Braze zu Google Audiences hinzufügen können, um Werbung basierend auf Verhaltens-Triggern, Segmentierung und mehr zu schalten.

Um auf das Template für inaktive Nutzer:innen zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Use a Canvas template** > **Braze templates**. Wählen Sie dann neben **Lapsing User** die Option **Apply Template**. Jetzt können wir das Template durchgehen und an unsere Bedürfnisse anpassen.

### 1. Schritt: Details einrichten {#step-1-set-up-the-details}

Passen wir die Canvas-Details an unser Ziel an.

1. Wählen Sie **Edit** neben dem Template-Namen.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/lapsed_user_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass dieses Canvas Nutzer:innen mit Aktionen anspricht und einen Audience Sync für diejenigen durchführt, die eine Sitzung starten.
3. Aktualisieren Sie die Beschreibung, um zu erklären, dass dieses Canvas Vorteile und Aktionen enthält.
4. Fügen Sie den Tag **Lapsing/Retention** hinzu, damit wir auf der Canvas-Startseite nach diesem Canvas filtern können.

![Der Schritt „Canvas-Details einrichten“ mit dem Canvas-Namen „Lapsed User - Visit App“ und einer kurzen Canvas-Beschreibung.]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### 2. Schritt: Konversions-Events zuweisen {#step-2-assign-your-conversion-events}

Aktualisieren Sie **Primary Conversion Event - A**, um Nutzer:innen aus unserer App (MovieCanon) anzusprechen, und belassen Sie **Primary Conversion Event - B** bei der Standardeinstellung „Beliebigen Kauf tätigen“.

![Der Abschnitt „Konversions-Events zuweisen“ mit einem primären Konversions-Event, bei dem Nutzer:innen eine Sitzung in einer bestimmten App starten.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### 3. Schritt: Entry-Zeitplan anpassen {#step-3-tailor-the-entry-schedule}

Belassen wir den Entry-Zeitplan auf **Geplant** und die standardmäßigen zeitbasierten Optionen, damit das Canvas täglich nach inaktiven Nutzer:innen sucht.

Wir nehmen zwei Anpassungen an diesem Schritt vor:

1. Wählen Sie ein Startdatum und eine Startzeit.
2. Wählen Sie als Endparameter **An einem bestimmten Datum** und ein Datum in zwei Monaten. Nehmen wir an, wir haben ein weiteres Canvas für inaktive Nutzer:innen, das nach diesem starten soll.

![Der Schritt „Entry-Zeitplan“ für ein geplantes Canvas, das Nutzer:innen zu einem festgelegten Zeitpunkt eintreten lässt.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### 4. Schritt: Zielgruppe auswählen {#step-4-select-our-target-audience}

Wir behalten die Standardeinstellungen für die Entry-Zielgruppe bei, die auf Nutzer:innen eingestellt ist, die unsere App seit über 30 Tagen nicht genutzt haben. Wir behalten auch die Standard-Entry-Kontrollen bei, damit Nutzer:innen nach vier Wochen erneut in das Canvas eintreten können. Das bedeutet, dass Nutzer:innen jedes Mal, wenn sie unsere App über 30 Tage am Stück nicht besuchen, in das Canvas aufgenommen werden.

![Der Schritt „Zielgruppe“ mit Targeting auf Nutzer:innen, die die Apps zuletzt vor 30 Tagen genutzt haben.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### 5. Schritt: Sendeeinstellungen auswählen {#step-5-select-your-send-settings}

Wir behalten die meisten Standard-Abo-Einstellungen bei:

- Nur an Nutzer:innen senden, die Nachrichten oder Benachrichtigungen abonniert haben oder dafür angemeldet sind.
- Unsere [Frequency-Capping-Regeln]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping) anwenden, damit wir unsere Zielgruppe nicht mit zu vielen Nachrichten überfordern. In diesem Fall setzen wir unser Frequency-Capping so, dass die Anzahl der Campaigns oder Canvas-Schritte mit dem Tag „Lapsing/Retention“, die Nutzer:innen erhalten können, auf zwei pro Woche begrenzt wird.
- Keine Nachrichten während der Ruhezeiten in der Ortszeit der Nutzer:innen senden (0:00 bis 8:00 Uhr).

Die einzige Einstellung, die wir ändern, betrifft das Verhalten, wenn eine Nachricht während der Ruhezeiten ausgelöst wird. Anstatt die Nachricht abzubrechen, wählen Sie **Zum nächsten verfügbaren Zeitpunkt senden**, damit unsere Nutzer:innen keine Aktionen verpassen.

![Der Abschnitt „Ruhezeiten“ mit einer Startzeit von 0:00 Uhr und einer Endzeit von 8:00 Uhr.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### 6. Schritt: Canvas anpassen {#step-6-customize-your-canvas}

Jetzt erstellen wir unser Canvas, indem wir die vordefinierten Schritte anpassen:

1. Passen Sie die erste E-Mail an, die an alle Nutzer:innen gesendet wird, die unsere App seit über 30 Tagen nicht besucht haben. Für unseren Anwendungsfall gestalten wir eine E-Mail, die Nutzer:innen mitteilt, dass sie neue Vorteile freischalten, wenn sie heute unsere App besuchen.

![Canvas-Nachrichtenschritt für eine E-Mail, die Nutzer:innen auffordert, neue Vorteile freizuschalten, wenn sie heute vorbeischauen.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2. Passen Sie die Aktions-Pfad-Komponente namens „Start Session?“ an, indem Sie unsere App für den Pfad **Started Session** auswählen.

![Aktions-Pfad für Sitzungen, die in einer bestimmten App gestartet werden.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3. Behalten Sie die Standardeinstellung für den Decision-Split-Schritt namens „Sessions?“ bei, der die Gruppe „>1 Session“ als Nutzer:innen definiert, die unsere App am letzten Kalendertag mehr als einmal genutzt haben.
4. Passen Sie den Nachrichtenschritt für Nutzer:innen an, die in die Gruppe „>1 Session“ fallen. In unserem Anwendungsfall bedanken wir uns bei den Nutzer:innen für ihren Besuch in unserer App und heben die Vorteile hervor, die sie freigeschaltet haben.
5. Stellen Sie sicher, dass unser Google Audience Sync im Schritt „Ad Audience Update“ eingerichtet ist, damit wir die Nutzerdaten von Nutzer:innen aktualisieren und synchronisieren, die nach Erhalt unserer ersten E-Mail mehrere Sitzungen hatten.
6. Behalten Sie die Standardeinstellung für die [Experiment-Pfad]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step/#experiment-paths)-Komponente namens „A/B Test“ bei. Diese sendet zufällig eine von zwei Aktionen (die wir im nächsten Schritt anpassen) an Nutzer:innen, die weniger als zwei Sitzungen hatten.
7. Passen Sie die beiden Aktionen an, die im Rahmen des Experiment-Pfads an Nutzer:innen gesendet werden. In unserem Anwendungsfall machen wir eine zu einer 20%-Aktion für ein Drei-Monats-Abo und die andere zu einer 10%-Aktion für ein Ein-Monats-Abo.

![Canvas-Schritte mit verzweigten Pfaden basierend darauf, wie viele Sitzungen Nutzer:innen hatten.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### 7. Schritt: Canvas testen und starten {#step-7-test-and-launch-the-canvas}

Nachdem wir unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten wir es, indem wir **Launch Canvas** auswählen. Jetzt erhalten unsere Nutzer:innen, die unsere App seit über 30 Tagen nicht besucht haben und unsere Messaging-Kanäle abonniert haben, E-Mails, die sie zur Rückkehr ermutigen!

{% alert tip %}
Schauen Sie sich unsere [Checkliste vor und nach dem Start]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) an, um zu erfahren, was Sie vor und nach dem Start eines Canvas beachten sollten.
{% endalert %}