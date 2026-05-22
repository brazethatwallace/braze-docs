---
nav_title: Feature-Adoption
article_title: Feature-Adoption
page_order: 3
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie ein Braze-Canvas-Template verwenden, um zeitnahe, personalisierte Nachrichten zu versenden, die die Vorteile und Nutzungstipps hervorheben."
tool: Canvas
---

# Feature-Adoption

> Dieses Template wurde entwickelt, um die Nutzung Ihrer neuen Features, bestehenden Produkte, zusätzlichen Angebote oder anderer Bereiche zu fördern, die Ihre Kund:innen erleben sollen. Durch den Einsatz personalisierter Kommunikation und einer strukturierten Abfolge von Nachrichten können Sie Nutzer:innen nahtlos neue Features vorstellen und wertvolles Feedback von ihnen erhalten.

In diesem Artikel führen wir Sie durch einen Anwendungsfall für das **Feature-Adoption**-Template, das für die Bindungs- und Loyalitätsphasen des Nutzer:innen-Lebenszyklus vorgesehen ist. Nach diesem Artikel haben Sie eine User-Journey angepasst, die Nutzer:innen dazu ermutigt, neue Features zu nutzen, und die Nutzer:innen-Stimmung erfasst.

## Voraussetzungen {#prerequisites}

Um dieses Template erfolgreich zu verwenden, benötigen Sie ein [angepasstes Event]({{site.baseurl}}/user_guide/data/activation/events/custom_events/), das erfasst, wann Nutzer:innen das Feature verwendet haben.

## Das Template an Ihre Bedürfnisse anpassen {#tailoring-the-template-to-your-needs}

Nehmen wir an, Sie arbeiten bei Calorie Rocket, einer App für Essenslieferungen, die kürzlich Cruise Control eingeführt hat – ein Feature zur Planung wiederkehrender Essenslieferungen – und Sie möchten mehr Nutzer:innen dazu ermutigen, dieses neue Feature zu nutzen. In unserem Beispiel verwenden wir das angepasste Event `scheduled_delivery`, um zu verfolgen, wann Nutzer:innen das Cruise-Control-Feature ausprobiert haben.

Um auf das Back-in-Stock-Template zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Use a Canvas template** > **Braze templates**. Wählen Sie dann neben **Feature Adoption** die Option **Apply Template**. Nun können wir das Template an unsere Bedürfnisse anpassen.

### 1. Schritt: Details einrichten {#step-1-set-up-the-details}

Passen wir die Canvas-Details an, um unser Ziel widerzuspiegeln.

1. Wählen Sie **Edit** neben dem Template-Namen.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas darauf abzielt, Nutzer:innen-Feedback zu sammeln.
3. Aktualisieren Sie die Beschreibung, um anzugeben, dass das Canvas Nutzer:innen dazu ermutigen soll, Feedback einzureichen und die Nutzer:innen-Stimmung für das neue Cruise-Control-Feature zu verfolgen.
4. Fügen Sie den Tag **Feature adoption** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name und die neue Beschreibung für das Canvas. Die neue Beschreibung lautet: „Ein Feature-Adoption-Canvas zur Verfolgung der Adoption und Nutzer:innen-Stimmung für Cruise Control, ein Feature zur Planung wiederkehrender Essenslieferungen.“]({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### 2. Schritt: Ein Konversions-Event zuweisen {#step-2-assign-a-conversion-event}

Als Nächstes fügen wir ein Konversions-Event für unser Canvas hinzu, um die Feature-Adoption zu signalisieren. Dies ermöglicht es uns, den Experiment-Pfad in unserer User-Journey später anzupassen.

1. Wählen Sie unter **Assign Conversion Events** die Option **Add Conversion Event**.
2. Wählen Sie unter **Primary Conversion Event - A** die Option **Performs Custom Event** als **Conversion event type**.
3. Wählen Sie unser angepasstes Event `scheduled_delivery`.
4. Wir belassen die Conversion-Frist bei drei Tagen.

![Das Konversions-Event-Fenster im Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### 3. Schritt: Den Entry-Zeitplan anpassen {#step-3-tailor-the-entry-schedule}

Unser Ziel ist es, unsere Nutzer:innen zur Nutzung von Cruise Control zu ermutigen, aber wir möchten nicht, dass unsere Nachrichten zu häufig sind. Daher belassen wir dieses Canvas als geplante Zustellung und nehmen die folgenden Anpassungen im Abschnitt **Time-Based Options** vor.

1. Aktualisieren Sie die **Entry Frequency** auf **Weekly**.
2. Belassen Sie die Wiederholung wie sie ist.
3. Wählen Sie **Mon**, um Nutzer:innen zu Beginn der Woche anzusprechen.
4. Wählen Sie die Startzeit für unser Canvas.
5. Aktualisieren Sie die **Ending parameters**, um das Canvas am letzten Tag des Jahres zu beenden.

Wir belassen die Option, Nutzer:innen in ihrer Ortszeit in das Canvas eintreten zu lassen.

### 4. Schritt: Die Zielgruppe auswählen {#step-4-select-the-target-audience}

Nun richten wir unsere Zielgruppe ein, indem wir die folgenden Details im Template aktualisieren:

1. Wählen Sie das Segment **All Users**.
2. Entfernen Sie die zusätzlichen Filter des Templates.
3. Erstellen Sie diesen Filter mit unserem angepassten Event: `Has scheduled_delivery for exactly 0 times`. So können wir Nutzer:innen, die das Feature bereits verwendet haben, vom Eintritt in unser Canvas ausschließen.

![Das Segment für alle Nutzer:innen, die Cruise Control noch nicht verwendet haben.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4. Da Calorie Rocket zuvor einigen Nutzer:innen erlaubt hat, das neue Feature Cruise Control als Beta zu testen, aktualisieren wir die Austrittskriterien, um diese Nutzer:innen vom Eintritt in das Canvas auszuschließen.

### 5. Schritt: Sendeeinstellungen auswählen {#step-5-select-your-send-settings}

Wir belassen die Standard-Abo-Einstellungen, sodass wir nur an Nutzer:innen senden, die Nachrichten oder Benachrichtigungen abonniert haben oder sich dafür angemeldet haben, und überspringen die anderen Einstellungen (Frequency-Capping, Ruhezeiten und Seed-Gruppen).

### 6. Schritt: Ihr Canvas anpassen {#step-6-customize-your-canvas}

#### Den Aktions-Pfad aufbauen {#build-out-the-action-path}

Als Nächstes bauen wir den ersten Aktions-Pfad-Schritt auf, der anzeigen soll, ob unsere Nutzer:innen Interesse am neuen Feature haben. Wir nehmen die folgenden Anpassungen am Template vor:

1. Da das Cruise-Control-Feature erst verfügbar ist, nachdem eine Bestellung in den Warenkorb gelegt wurde, benennen wir die erste Aktionsgruppe **Added to cart** und wählen `added_to_cart` als angepasstes Event.

![Der Name der Aktionsgruppe ist auf „Added to cart“ gesetzt und „Perform Custom Event“ ist auf „added_to_cart“ gesetzt.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2. Belassen Sie die zweite Aktionsgruppe **Taken Tour** wie sie ist, da wir auswerten möchten, ob Nutzer:innen eine Tour durch die App gemacht haben. Falls ja, gelangen sie zum zweiten Pfad.
3. Ersetzen Sie für den nachfolgenden Aktions-Pfad namens **Assess Usage** den Eintrag **Used Feature >3x** durch **Viewed Cruise Control settings**.
4. Wählen Sie das Dropdown **Perform Custom Event** und dann `scheduled_delivery` als angepasstes Event.

![Der Name der Aktionsgruppe ist auf „Used Feature >3x“ gesetzt und „Perform Custom Event“ ist auf „scheduled_delivery“ gesetzt.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Feedback-Umfrage einrichten {#set-up-feedback-survey}

Als Nächstes gehen wir zum Nachrichtenschritt namens **Feedback Survey**, um unsere Feedback-Umfrage einzufügen, die unsere Nutzer:innen nach der ersten Nutzung von Cruise Control ausfüllen sollen. Unsere Umfrage-Antwortoptionen für unsere Nutzer:innen sind:

- **Loved it!**
- **Not for me.**

1. Wählen Sie für die beiden Umfrage-Optionen **Experience Feedback** als unser angepasstes Attribut, um Feedback zu Cruise Control zu erfassen und zu verfolgen. Dieses angepasste Attribut hat zwei Werte, die die Umfrageantworten repräsentieren (`good` und `bad`).
2. Aktualisieren Sie die Attributwerte, damit sie zu den Umfrage-Optionen passen. So können wir die Antwort der Nutzer:innen verfolgen.

### 7. Schritt: Ihr Canvas testen und starten {#step-7-test-and-launch-your-canvas}

Nachdem Sie unser Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, wählen Sie **Launch Canvas**, um das Canvas zu starten. Jetzt können wir Nutzer:innen mit einer personalisierten User-Journey ansprechen, um sie zur Nutzung unseres neuen Features Cruise Control zu ermutigen.

{% alert tip %}
Sehen Sie sich unsere [Checkliste vor und nach dem Start]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) an, um zu erfahren, was Sie vor und nach dem Start eines Canvas beachten sollten.
{% endalert %}