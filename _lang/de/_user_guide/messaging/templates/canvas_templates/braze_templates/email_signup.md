---
nav_title: E-Mail-Registrierung mit Double-Opt-in
article_title: E-Mail-Registrierung mit Double-Opt-in
page_order: 2
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie ein Braze-Canvas-Template verwenden, um Ihre Reichweite mit verifizierten E-Mail-Registrierungen zu erweitern."
tool: Canvas
---

# E-Mail-Registrierung mit Double-Opt-in {#email-sign-up-with-double-opt-in}

> Verwenden Sie das Template für die E-Mail-Registrierung mit Double-Opt-in, um Ihre Reichweite mit verifizierten E-Mail-Registrierungen zu erweitern. Sprechen Sie neue Nutzer:innen an, um deren E-Mail-Adresse zu erfassen, ihr Abo zu bestätigen und einen Aktionscode zu erhalten – alles in einer nahtlosen Journey.

Dieser Artikel führt Sie durch einen Anwendungsfall für das Template **E-Mail-Registrierung mit Double-Opt-in**, das für die Erwägungsphase des Nutzerlebenszyklus konzipiert ist. Am Ende werden Sie ein Canvas erstellt haben, das E-Mails und In-App-Nachrichten an Nutzer:innen sendet, wenn sie eine Sitzung starten oder ihr Onboarding nicht abgeschlossen haben.

## Voraussetzungen {#prerequisites}

Um dieses Template erfolgreich zu verwenden, benötigen Sie Folgendes:

- Eine [mehrseitige In-App-Nachricht]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/#multi-page) mit einer Seite zur Erfassung der E-Mail-Adressen Ihrer Nutzer:innen und einer weiteren Seite für eine Erfolgsmeldung.
- Eine Bestätigungs-E-Mail, damit Nutzer:innen ihre E-Mail-Adresse verifizieren können.
- Eine Willkommens-E-Mail mit einem exklusiven Aktionscode für Nutzer:innen, die das Double-Opt-in abschließen.

## Das Template an Ihre Bedürfnisse anpassen {#tailoring-the-template-to-your-needs}

Nehmen wir an, Sie arbeiten für Steppington, eine Gesundheits-App, die für Features wie Kalorienverfolgung, digitale Fitnesskurse und Flashmob-Marathons bekannt ist. Bevor Sie das Canvas erstellen, [richten Sie mehrseitige In-App- und In-Browser-Nachrichten ein]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/#multi-page), die eine Reihe ansprechender Fragen enthalten, um die Erfahrung und den Eindruck der ersten Nutzung der App zu ermitteln.

Um auf das Template zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Use a Canvas template** > **Braze templates**. Wählen Sie dann neben **Email sign-up with double opt-in** die Option **Apply Template**. Nun können wir das Template an unsere Bedürfnisse anpassen.

### 1. Schritt: Details einrichten {#step-1-set-up-the-details}

Passen Sie die Canvas-Details an Ihr Ziel an.

1. Wählen Sie **Edit** neben dem Template-Namen.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas für das Targeting neuer Nutzer:innen bei der ersten Nutzung der App bestimmt ist.
3. Aktualisieren Sie die Beschreibung, um zu erklären, dass dieses Canvas personalisiertes Messaging für Nutzer:innen enthält, die das Double-Opt-in durchführen sollen.
4. Fügen Sie den Tag **Email** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### 2. Schritt: Konversions-Events zuweisen {#step-2-assign-conversion-events}

Weisen Sie als Nächstes unsere Konversions-Events zu. Konversions-Events sind eine Art Metrik, mit der Sie den Erfolg des Canvas messen können. Wählen Sie für **Conversion event type** die Option **Performs Custom Event**. Wählen Sie dann **email_opt_in** als **Custom event name**.

![Abschnitt „Konversions-Events zuweisen“ für den Konversions-Event-Typ des E-Mail-Opt-ins.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Behalten Sie die Conversion-Frist des Templates von drei Tagen bei, da Sie Ihre neuesten Nutzer:innen ansprechen möchten.

### 3. Schritt: Entry-Zeitplan anpassen {#step-3-tailor-the-entry-schedule}

Behalten Sie den Entry-Zeitplan als **Action-Based** bei, damit Nutzer:innen Ihr Canvas betreten, wenn sie eine Sitzung in der App starten. So können Sie mit zeitnahem Engagement beginnen, eine Beziehung aufzubauen.

Erwägen Sie außerdem, die **Action Based Options** beizubehalten, damit Nutzer:innen das Canvas nur betreten, wenn sie eine Sitzung starten.

![Ein aktionsbasierter Entry-Zeitplan, um Nutzer:innen, die eine Sitzung starten, in das Canvas aufzunehmen.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Aktualisieren Sie für das **Entry Window** die **Started Time (Required)** auf das gewünschte Datum und die gewünschte Uhrzeit.

![Ein Einstiegsfenster mit der Startzeit 16. Januar 2025 um 12:30 Uhr. Nutzer:innen betreten diese Nachricht in ihrer Ortszeit.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### 4. Schritt: Zielgruppe auswählen {#step-4-select-the-target-audience}

Definieren Sie Ihre Zielgruppe als Steppington-Nutzer:innen, die keine E-Mail-Adresse in ihrem Nutzerprofil haben, indem Sie den Standard-[Segmentierungsfilter]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/) des Templates `Email Available is false` beibehalten.

![Entry-Zielgruppe mit dem Filter „Email Available is false“.]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### 5. Schritt: Sendeeinstellungen auswählen {#step-5-select-your-send-settings}

Behalten Sie die Standard-Abo-Einstellungen bei, sodass Sie nur an Nutzer:innen senden, die Nachrichten oder Benachrichtigungen abonniert haben oder dafür angemeldet sind, und überspringen Sie die anderen Einstellungen (Frequency-Capping, Ruhezeiten und Seed-Gruppen).

![Standard-Sendeoptionen, um nur an Nutzer:innen zu senden, die abonniert oder angemeldet sind.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### 6. Schritt: Ihr Canvas anpassen {#step-6-customize-your-canvas}

Erstellen Sie als Nächstes das Canvas, indem Sie die Kanäle und Inhalte anpassen, die Sie an Nutzer:innen senden möchten. Da Sie sich auf die Verifizierung von E-Mail-Registrierungen konzentrieren, müssen Sie keine Canvas-Schritte und Kanäle des Templates hinzufügen oder entfernen.

1. Wählen Sie den ersten Nachrichtenschritt mit dem Namen **Email Sign-up**. Hier aktualisieren Sie das Template, um unsere mehrseitige In-App- (und In-Browser-) Nachricht zu verwenden.

- Seite 1 erfasst die E-Mail-Adressen.
- Seite 2 zeigt eine Bestätigungsnachricht an.

![Zwei Seiten einer In-App-Nachricht zur Erfassung von Nutzer-E-Mails und Anzeige einer Erfolgsmeldung.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2. Behalten Sie von hier aus den Aktions-Pfad-Schritt **Subscribed** bei. Dieser Schritt teilt unsere Nutzer:innen in einem Zeitfenster von einem Tag in zwei Gruppen auf:

- Nutzer:innen, die sich mit ihrer E-Mail bei Steppington angemeldet haben
- Nutzer:innen, die sich nicht mit ihrer E-Mail bei Steppington angemeldet haben

{:start="3"}
3. Ersetzen Sie als Nächstes den E-Mail-Text durch unsere gebrandete Bestätigungs-E-Mail für den Nachrichtenschritt **Verify Email**. Dieser sendet eine E-Mail an unsere abonnierten Nutzer:innen und fordert sie auf, ihre E-Mail-Adresse zu bestätigen und sich für unser Messaging anzumelden.
4. Behalten Sie den Aktions-Pfad-Schritt **Confirm Subscription** bei. Dieser Schritt teilt unsere Nutzer:innen weiter in diejenigen auf, die ihre E-Mail bestätigt haben, und diejenigen, die dies nicht getan haben, mit einem Zeitfenster von einer Woche.
5. Aktualisieren Sie abschließend den Nachrichtenschritt **Welcome + Discount** mit unserer Bestätigungs-E-Mail, die einen exklusiven Aktionscode enthält.

{% alert note %}
Der Nachrichtenschritt **Verify Email** wird bei der zweiten Sitzung der Nutzer:innen ausgelöst. Dies liegt daran, dass das erste Sitzungsstart-Event das Canvas auslöst, aber ein zweiter Sitzungsstart erforderlich ist, nachdem die Nutzer:innen den ersten Nachrichtenschritt **Email Sign-up** erreicht haben, damit sie berechtigt sind, die zweite In-App-Nachricht auszulösen.
{% endalert %}

### 7. Schritt: Canvas testen und starten {#step-7-test-and-launch-your-canvas}

Nachdem Sie Ihr Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, starten Sie es, indem Sie **Launch Canvas** auswählen.

{% alert tip %}
Sehen Sie sich unsere [Checkliste vor und nach dem Start]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) an, um Dinge zu berücksichtigen, bevor und nachdem Sie ein Canvas starten.
{% endalert %}