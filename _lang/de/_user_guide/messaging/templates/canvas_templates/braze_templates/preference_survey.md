---
nav_title: Onboarding mit Präferenzumfrage
article_title: Onboarding mit Präferenzumfrage
page_order: 5.5
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie ein Braze-Canvas-Template verwenden, um die frühe Akzeptanz mit einem geführten Onboarding-Flow zu fördern, der neue Nutzer:innen mit Ihrer Marke vertraut macht und Präferenzen erfasst, um sie langfristig zu binden."
tool: Canvas
---

# Onboarding mit Präferenzumfrage {#onboarding-with-preferences-survey}

> Verwenden Sie das Template „Onboarding mit Präferenzumfrage“, um einen geführten Onboarding-Workflow zu erstellen, der auf neue Nutzer:innen abzielt. Stellen Sie ihnen Ihre Marke vor, helfen Sie ihnen beim Einstieg und erfassen Sie ihre Präferenzen, um sie langfristig zu binden.

Dieser Artikel führt Sie durch einen Anwendungsfall für das Template **Onboarding with preferences survey**, das für die Überlegungsphase des Nutzer:innen-Lebenszyklus konzipiert ist. Am Ende werden Sie ein Canvas erstellt haben, das E-Mails und In-App-Nachrichten an Nutzer:innen sendet, wenn sie eine Sitzung starten und wenn sie ihr Onboarding noch nicht abgeschlossen haben.

## Voraussetzungen {#prerequisites}

Um dieses Template erfolgreich zu nutzen, benötigen Sie Folgendes:

- Eine Willkommens-E-Mail, die Nutzer:innen auffordert, mit dem Onboarding zu beginnen.
- Eine Folge-E-Mail mit Tipps für den Einstieg in die App für Nutzer:innen, die das Onboarding abgeschlossen haben.
- Eine Folge-E-Mail, die Nutzer:innen auffordert, ihr Onboarding abzuschließen.
- Eine [Umfrage]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/simple_survey) mit mehreren Fragen zur Ermittlung der Nutzer:innen-Präferenzen.

## Das Template an Ihre Bedürfnisse anpassen {#tailoring-the-template-to-your-needs}

Nehmen wir an, wir arbeiten für StyleRyde, eine On-Demand-Ridesharing-App, die Menschen dorthin bringt, wo sie hin müssen. Bevor wir das Canvas erstellen, [richten wir eine einfache Umfrage ein]({{site.baseurl}}/user_guide/data/activation/catalogs/create), die eine Reihe ansprechender Fragen enthält, um die Erfahrung und den Eindruck der ersten Fahrt einer Nutzer:in mit der App zu ermitteln.

Um auf das Template zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Use a Canvas template** > **Braze templates**. Wählen Sie dann neben **Onboarding with preferences survey** die Option **Apply Template**. Jetzt können wir das Template durchgehen und an unsere Bedürfnisse anpassen.

### 1. Schritt: Details einrichten {#step-1-set-up-the-details}

Passen wir die Canvas-Details an, um unser Ziel widerzuspiegeln.

1. Wählen Sie **Edit** neben dem Template-Namen.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas auf neue Nutzer:innen bei ihrer ersten Nutzung der App abzielt.
3. Aktualisieren Sie die Beschreibung, um zu erklären, dass dieses Canvas personalisiertes Messaging enthält.
4. Fügen Sie den Tag **Onboarding** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### 2. Schritt: Konversions-Events zuweisen {#step-2-assign-conversion-events}

Aktualisieren Sie das **Primary Conversion Event - A** auf **Performs Custom Event**. Wählen Sie dann **Last Used App** als angepasstes Event aus.

![„Last Used App“ als ausgewählter Name des angepassten Events für das Konversions-Event.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### 3. Schritt: Den Entry-Zeitplan anpassen {#step-3-tailor-the-entry-schedule}

Behalten wir den Entry-Zeitplan als **Action-Based** bei, damit Nutzer:innen unser Canvas betreten, wenn sie eine Sitzung in der App starten. So können wir mit zeitnahem Engagement beginnen, unsere Beziehung aufzubauen.

Wir nehmen eine Änderung in diesem Abschnitt vor, indem wir das **Entry Window** auf unser gewünschtes Datum und unsere gewünschte Uhrzeit anpassen.

![Abschnitt „Entry Window“ mit der Startzeit 30. Januar 2025 um 12 Uhr.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### 4. Schritt: Die Zielgruppe auswählen {#step-4-select-the-target-audience}

Wir behalten die Zielgruppe bei, um unsere Nutzer:innen anzusprechen, die die StyleRyde-App vor weniger als einem Tag zum ersten Mal genutzt haben.

![Der Filter „First used these apps less than 1 days ago“ ist ausgewählt, um die Entry-Zielgruppe anzusprechen.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### 5. Schritt: Sendeeinstellungen auswählen {#step-5-select-your-send-settings}

Wir behalten die Standard-Abo-Einstellungen bei, sodass wir nur an Nutzer:innen senden, die Nachrichten oder Benachrichtigungen abonniert haben oder dafür angemeldet sind, mit aktivierten Ruhezeiten, und überspringen die anderen Einstellungen (Frequency-Capping und Seed-Gruppen).

![Abschnitt „Sendeeinstellungen“ mit den Abo-Einstellungen für Nutzer:innen, die abonniert oder angemeldet sind, mit aktivierten Ruhezeiten zwischen 0 Uhr und 20 Uhr.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### 6. Schritt: Ihr Canvas anpassen {#step-6-customize-your-canvas}

Jetzt erstellen wir unser Canvas, indem wir den Inhalt anpassen, der an Nutzer:innen gesendet wird.

1. Für den ersten Nachrichtenschritt **Welcome Email** aktualisieren wir diesen Schritt, um unsere StyleRyde-Willkommens-E-Mail einzufügen.
2. Als Nächstes behalten wir den Aktions-Pfad-Schritt bei. Dieser Schritt teilt unsere Nutzer:innen in einem Drei-Tage-Fenster in zwei Gruppen auf:

- Nutzer:innen, die eine Sitzung gestartet oder die Onboarding-E-Mail angeklickt haben
- Nutzer:innen, die keine Sitzung gestartet oder die Onboarding-E-Mail nicht angeklickt haben

![Ein Aktions-Pfad-Schritt, der in zwei Pfade aufgeteilt ist: einen für Nutzer:innen, die eine Sitzung gestartet haben, und einen für alle anderen.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

Von hier aus sprechen wir unsere Nutzer:innen gezielt an und passen das Messaging basierend auf den oben genannten Gruppen an.

#### Engagierte Nutzer:innen ansprechen {#target-your-engaged-users}

Für unsere Nutzer:innen, die eine Sitzung gestartet oder mit unserer Onboarding-E-Mail aus dem ersten Nachrichtenschritt interagiert haben, aktualisieren wir den Nachrichtenschritt **Getting Started Tips**, um die wichtigsten Reise- und Sicherheitstipps für unsere neuen StyleRyde-Nutzer:innen einzufügen.

Nachdem Nutzer:innen ihr Onboarding abgeschlossen haben, verlassen sie das Canvas.

Aktualisieren Sie als Nächstes den Nachrichtenschritt **Content Preferences Survey**, um unsere Präferenzumfrage einzufügen, die Nutzer:innen auffordert, auszuwählen, zu welchen Themen sie in Zukunft Informationen erhalten möchten.

![Eine Vorschau der Präferenzumfrage, die Nutzer:innen auffordert, alle zutreffenden Interessen auszuwählen.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Nutzer:innen anstoßen, die das Onboarding noch nicht begonnen haben {#nudge-users-who-havent-started-onboarding}

Für unsere anderen Nutzer:innen aktualisieren wir den Nachrichtenschritt **Winback Nudge** mit unserer Folge-E-Mail, um Nutzer:innen aufzufordern, ihr Onboarding abzuschließen.

Als letzten Schritt für die erneute Interaktion benennen wir **Step 2** in **Final Winback Nudge** um und aktualisieren den Schritt mit unserer In-App-Nachricht, um unsere neuen Nutzer:innen aufzufordern, ihr Onboarding abzuschließen.

### 7. Schritt: Ihr Canvas testen und starten {#step-7-test-and-launch-your-canvas}

Nachdem wir unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten wir es, indem wir **Launch Canvas** auswählen.

{% alert tip %}
Schauen Sie sich unsere [Checkliste vor und nach dem Start]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) an, um zu erfahren, was Sie vor und nach dem Start eines Canvas beachten sollten.
{% endalert %}