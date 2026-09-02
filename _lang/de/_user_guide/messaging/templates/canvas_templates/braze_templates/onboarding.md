---
nav_title: Onboarding
article_title: Onboarding
page_order: 5
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie ein Braze-Canvas-Template verwenden, um Onboarding-Journeys zu erstellen, die eine starke anfängliche Akzeptanz fördern und dauerhafte Beziehungen zu Ihren Nutzer:innen aufbauen."
tool: Canvas
---

# Onboarding {#onboarding}

> Starten Sie die Journey Ihrer Nutzer:innen mit diesem Onboarding-Template. Dieses Template wurde entwickelt, um eine starke anfängliche Akzeptanz zu fördern und dauerhafte Beziehungen zu Ihren Nutzer:innen aufzubauen. Durch den Einsatz personalisierter Kommunikation und einer strukturierten Abfolge von Nachrichten können Sie Ihre Nutzer:innen nahtlos mit Ihrer Marke vertraut machen und den Grundstein für eine langfristige Beziehung legen.

In diesem Artikel führen wir Sie durch einen Anwendungsfall für das **Onboarding**-Template, das für die Überlegungsphase des Nutzer:innen-Lebenszyklus gedacht ist, um eine nahtlose Onboarding-Journey für neue Nutzer:innen zu erstellen. Nach diesem Artikel haben Sie dieses Braze-Canvas-Template mit personalisierten Nachrichten für diese neuen Nutzer:innen angepasst.

## Voraussetzungen {#prerequisites}

Bevor Sie dieses Template verwenden, müssen Sie die folgenden [E-Mail-Templates]({{site.baseurl}}/user_guide/messaging/templates/email_templates/email_template) erstellen, um sie im Canvas zu referenzieren:

- Eine Willkommens-E-Mail für alle Nutzer:innen Ihrer App
- Eine E-Mail mit Tipps zur Nutzung Ihrer App
- Eine Feedback-E-Mail, die eine Nutzer:innen-Umfrage enthält

## Das Template an Ihre Bedürfnisse anpassen {#tailoring-the-template-to-your-needs}

Nehmen wir an, wir arbeiten bei PantsLabyrinth und unser Ziel ist es, das Nutzer:innen-Engagement zu steigern, Vertrauen und Loyalität bei unseren Nutzer:innen aufzubauen und sie dazu zu ermutigen, engagiert zu bleiben. Dazu möchten wir uns darauf konzentrieren, Nachrichten zu erstellen, die neue Nutzer:innen ansprechen, die noch nicht mit der App interagiert haben.

Um auf das Onboarding-Template zuzugreifen, wählen Sie beim Erstellen eines neuen Canvas **Use a Canvas template** > **Braze templates**. Wählen Sie dann neben **Onboarding** die Option **Apply Template**. Beginnen wir damit, dieses Template an unseren Anwendungsfall anzupassen.

### 1. Schritt: Details einrichten {#step-1-set-up-the-details}

Passen wir die Canvas-Details an, um unser Ziel widerzuspiegeln.

1. Wählen Sie **Edit** neben dem Template-Namen.

![Der aktuelle Titel und die Beschreibung des Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Aktualisieren Sie den Canvas-Namen, um anzugeben, dass das Canvas für das Onboarding neuer Nutzer:innen bestimmt ist.
3. Aktualisieren Sie die Beschreibung, um anzugeben, dass das Canvas eine Nutzer:innen-Journey abbildet, die Vertrauen und Loyalität bei Nutzer:innen fördert.
4. Fügen Sie den Tag **Onboarding** hinzu, damit wir auf der Canvas-Startseite danach filtern können.

![Der neue Name, die Beschreibung und der Tag für das Canvas.]({% image_buster /assets/img/canvas_templates/onboarding_new_name_description.png %}){: style="max-width:60%;"}

### 2. Schritt: Konversions-Events zuweisen {#step-2-assign-your-conversion-events}

Als Nächstes weisen wir unsere Konversions-Events zu. Konversions-Events sind eine Art Metrik, die verwendet werden kann, um den Erfolg des Canvas zu messen. Wählen Sie für **Custom event name** die Option **Email Klick, der** als angepasstes Event.

![Primäres Konversions-Event – A mit dem Konversionstyp „Performs Custom Event“ und dem angepassten Event-Namen „Email Click“. Es gibt eine Konversionsfrist von 4 Tagen.]({% image_buster /assets/img/canvas_templates/onboarding1.png %})

Das bedeutet, dass neue Nutzer:innen bis zu vier Tage Zeit haben, auf die Willkommens-E-Mail zu klicken. In diesem Fall möchten wir, dass unsere neuen Nutzer:innen ein Gefühl der Dringlichkeit verspüren, sich mit PantsLabyrinth zu beschäftigen und ein wiederkehrendes Abo für saisonale Kleidung abzuschließen.

### 3. Schritt: Entry-Zeitplan festlegen {#step-3-set-an-entry-schedule}

Da das Ziel darin besteht, neue Nutzer:innen von PantsLabyrinth anzusprechen, belassen wir das Canvas als aktionsbasiert. Wählen Sie für **Start Session** die Option **Start Session in Any App**, damit Nutzer:innen, die eine Sitzung in einer beliebigen App starten, das Canvas betreten können.

Passen Sie als Nächstes das **Entry Window** an, um festzulegen, wann Nutzer:innen das Canvas betreten können. Nehmen wir an, es steht ein PantsLabyrinth-Abo-Launch Ende Oktober bevor. Hier setzen wir die Startzeit auf **28.10.2024, 8:00 Uhr**. Optional können wir Nutzer:innen auch erlauben, das Canvas in ihrer Ortszeit zu betreten.

![Ein Entry-Fenster mit der Startzeit 28. Oktober 2024 um 8:00 Uhr. Nutzer:innen betreten diese Nachricht in ihrer Ortszeit.]({% image_buster /assets/img/canvas_templates/onboarding4.png %})

### 4. Schritt: Zielgruppe festlegen {#step-4-target-your-audience}

Indem wir die richtige Zielgruppe ansprechen, können wir effektiv mit neuen Nutzer:innen interagieren. Dieses Template richtet sich beispielsweise an alle Nutzer:innen, die eine App vor weniger als einem Tag zum ersten Mal genutzt haben, was für unseren Anwendungsfall zutreffend ist. Wir belassen diesen Abschnitt also unverändert.

### 5. Schritt: Sendeeinstellungen festlegen {#step-5-set-send-settings}

Standardmäßig wird dieses Canvas an Nutzer:innen gesendet, die abonniert oder angemeldet sind, und folgt den Frequency-Capping-Regeln. Wir belassen diese Einstellungen unverändert.

### 6. Schritt: Canvas anpassen {#step-6-customize-your-canvas}

Jetzt erstellen wir das Canvas, indem wir die vordefinierten Schritte anpassen.

#### Willkommens-E-Mail einrichten {#set-up-the-welcome-email}

1. Wählen Sie den Nachrichtenschritt mit dem Namen „Welcome Email“.
2. Wählen Sie **Edit message**, um die E-Mail des Templates durch unsere Willkommens-E-Mail zu ersetzen.
3. Wählen Sie **Done**.

Jetzt erhalten unsere Nutzer:innen diese Willkommens-E-Mail, nachdem sie eine Sitzung in unserer App gestartet haben. Um Nutzer:innen nicht mit wiederholten Nachrichten zu überfordern, empfehlen wir, den Verzögerungsschritt als Teil der Nutzer:innen-Journey zu verwenden.

#### Zielgruppenpfad anpassen {#customize-the-audience-path}

Im Zielgruppenpfad-Schritt mit dem Namen **Audience Split** können wir den Filter für unsere engagierten Nutzer:innen anpassen. Im Template lautet der Filter **Has clicked email for step Welcome Email**, was bedeutet, dass Nutzer:innen in zwei Gruppen aufgeteilt werden: Nutzer:innen, die auf die Willkommens-E-Mail geklickt haben, und solche, die es nicht getan haben.

![Ein Audience-Split-Schritt mit einem Pfad für engagierte Nutzer:innen und einem Pfad für alle anderen.]({% image_buster /assets/img/canvas_templates/onboarding2.png %}){: style="max-width:70%;"}

Als Online-Bekleidungshändler hat PantsLabyrinth auch eine aktive Gruppe von mobilen Nutzer:innen. In einem separaten Onboarding-Canvas können wir daher auch den folgenden Filter auswählen, um unsere mobilen Nutzer:innen zu identifizieren und in diese Segmente aufzuteilen:

- **Has clicked content card for step Welcome Content Card**
- **Everyone Else**

#### Mehr Nutzer:innen mit Zielgruppenpfaden ansprechen {#target-more-users-with-audience-paths}

Aus der Gruppe der Nutzer:innen, die nicht mit unserer App interagiert haben, können wir diese Nutzer:innen weiter ansprechen, indem wir den Schritt „Check for Clicks“ und den Schritt „Winback Nudge“ bearbeiten.

### 7. Schritt: Canvas testen und starten {#step-7-test-and-launch-your-canvas}

Nachdem Sie das Canvas getestet und überprüft haben, um sicherzustellen, dass es wie erwartet funktioniert, wählen Sie **Launch Canvas**, um das Canvas zu starten. Jetzt können wir unseren neuen Nutzer:innen ein personalisiertes Onboarding-Erlebnis bieten, um eine dauerhafte Beziehung zu fördern!

{% alert tip %}
Sehen Sie sich unsere [Checkliste vor und nach dem Start]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch) an, um zu erfahren, was Sie vor und nach dem Start eines Canvas beachten sollten.
{% endalert %}