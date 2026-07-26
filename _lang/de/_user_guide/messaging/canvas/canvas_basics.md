---
nav_title: Canvas-Grundlagen
article_title: Canvas-Grundlagen
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt die Grundlagen von Canvas und geht auf verschiedene Fragen ein, die Sie sich beim Einrichten Ihres ersten Canvas stellen sollten."
tool: Canvas

---

# Canvas-Grundlagen {#canvas-basics}

> Dieser Referenzartikel behandelt die Grundlagen von Canvas und geht auf verschiedene Fragen ein, die Sie sich beim Einrichten Ihres ersten Canvas stellen sollten. Wir erklären außerdem die fünf W-Fragen (Was, Wann, Wer, Warum und Wo) der Visualisierung und wie diese die Gestaltung und Definition Ihres Canvas beeinflussen können.

## Die Struktur von Canvas verstehen {#understanding-canvas-structure}

Bevor wir uns mit den Details der [Canvas-Einrichtung]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) befassen, lassen Sie uns die wichtigsten Bestandteile eines Canvas identifizieren.

{% tabs %}
  {% tab Canvas %}
  Canvas ist eine einheitliche Oberfläche, auf der Marketer Campaigns mit mehreren Nachrichten erstellen können. Es funktioniert ähnlich wie ein visuelles Programmiertool und ermöglicht es Ihnen, eine zusammenhängende User Journey aus einer Reihe von Schritten aufzubauen.

  ![Ein Beispiel für ein Canvas mit einem Decision-Split-Schritt, der je nachdem, ob Push für eine:n Nutzer:in aktiviert ist, in zwei verschiedene User Journeys verzweigt.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %})

  {% endtab %}

  {% tab Journey %}

  Eine Journey, häufig auch als User Journey bezeichnet, ist die individuelle Erfahrung einer/eines Nutzer:in innerhalb des Canvas.<br><br> ![Ein Chart mit der geschäftskunden Journey für eine:n neue:n Nutzer:in. Eine anonyme Person installiert eine App, Kat erstellt ein Konto, Kat öffnet die App eine Woche lang nicht, eine Push-Benachrichtigung bringt Kat zurück in die App, dann nutzt Kat die App regelmäßig.]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Canvas Builder %}
  Der Canvas Builder bildet die Schritte ab, die beim Erstellen Ihres Canvas zu durchlaufen sind. Dazu gehören grundlegende Dinge wie die Benennung Ihres Canvas und das Hinzufügen von Teams. Im Wesentlichen ist der Canvas Builder die entscheidende Einrichtung, die vor dem eigentlichen Aufbau Ihres Canvas erforderlich ist. Hier steuern Sie, wie Ihre Nutzer:innen ihre geschäftskunden Journey beginnen und durchlaufen – mit Optionen zur Bearbeitung des [Entry-Zeitplans]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule), der [Zielgruppe]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-13-set-your-target-entry-audience) und der [Sendeeinstellungen]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-14-select-your-send-settings).<br><br> ![Der Canvas Builder im Abschnitt „Grundlagen“ für ein Canvas mit dem Namen „New Canvas“.]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Varianten %}
  Eine Variante ist der Pfad, dem jede:r Kund:in auf der Journey folgt. Canvas unterstützt bis zu acht Varianten mit einer Kontrollgruppe. Sie bestimmen, welcher Teil Ihrer Zielgruppe welcher Variante folgt.<br><br> ![Auswahl des Buttons „Variante hinzufügen“.]({% image_buster /assets/img/canvas_intro/add_canvas_variant.gif %})

  {% endtab %}

  {% tab Schritte %}
  Ein Schritt in Canvas ist ein Marketing-Entscheidungspunkt: „Wenn dies, dann das.“ Nutzen Sie [Canvas-Komponenten]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components), um die Schritte einer User Journey aufzubauen.<br><br> ![Beispiel für das Hinzufügen eines Verzögerungsschritts zu einem Canvas.]({% image_buster /assets/img/canvas_intro/add_canvas_step.gif %}) <br><br> Wenn eine:r Nutzer:in ein Canvas betritt, beginnt sie/er beim ersten Schritt. Jeder Schritt hat Bedingungen, die bestimmen, ob eine:r Nutzer:in zum nächsten Schritt übergehen kann. Innerhalb eines Schritts können Sie Trigger festlegen oder die Zustellung planen, das Targeting durch Hinzufügen von Filtern oder Markieren von Ausnahme-Events verfeinern und verschiedene Kanäle wie Push-Benachrichtigungen oder Webhook-Events angeben. In Canvas erfolgen Schritte in einer Reihenfolge, d. h. der erste Schritt wird ausgeführt, bevor der zweite Schritt stattfinden kann. Nehmen wir an, wir haben ein Canvas mit den folgenden Schritten: Verzögerungsschritt A mit einer 24-Stunden-Verzögerung, Nachrichtenschritt A mit einer Push-Nachricht und Nachrichtenschritt B mit einer In-App-Nachricht. Nutzer:in A wird 24 Stunden lang in der Verzögerung gehalten, dann erhält sie/er nach 24 Stunden eine Push-Nachricht und anschließend eine In-App-Nachricht.

  {% endtab %}
{% endtabs %}

## Die geschäftskunden Journey aufbauen {#building-the-customer-journey}

Die fünf W-Fragen (Was, Wann, Wer, Warum und Wo) der Visualisierung können Ihnen helfen, Ihre geschäftskunden-Engagement-Strategien zu identifizieren und eine personalisierte Nachrichten-Journey für jede:n Ihrer Nutzer:innen zu erstellen.

### Das „Was“: Benennen Sie Ihr Canvas {#the-what-name-your-canvas}

*Was versuchen Sie, der/dem Nutzer:in zu helfen zu tun oder zu verstehen?*

Unterschätzen Sie niemals die Kraft des Namens. Braze ist auf Zusammenarbeit ausgelegt, daher ist dies ein guter Zeitpunkt, um festzulegen, wie Sie Ziele mit Ihrem Team kommunizieren.

Sie können Tags hinzufügen und die Schritte sowie Varianten in einem Canvas benennen. Weitere Informationen zu geschäftskunden Journeys finden Sie in unserem Braze-Lernkurs zum [Mapping von Nutzer-Lebenszyklen](https://learning.braze.com/mapping-customer-lifecycles).

### Das „Warum“: Konversions-Events identifizieren {#the-why-identify-conversion-events}

*Aufbauend auf dem „Was“ – warum erstellen Sie dieses Canvas?*

Es ist immer wichtig, ein klar definiertes Ziel vor Augen zu haben, und Canvas hilft Ihnen zu verstehen, wie Sie bei KPIs wie Session-Engagement, Käufen und angepassten Events abschneiden.

Die Auswahl mindestens eines [Konversions-Events]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) gibt Ihnen die Möglichkeit zu verstehen, wie Sie die Performance innerhalb des Canvas optimieren können. Und wenn Ihr Canvas mehrere Varianten oder eine Kontrollgruppe hat, verwendet Braze das Konversions-Event, um die beste Variante zur Erreichung dieses Ziels zu bestimmen.

* **Session starten**: Ich möchte, dass meine Nutzer:innen zurückkommen und sich mit der App beschäftigen.
* **Kauf tätigen**: Ich möchte, dass meine Nutzer:innen etwas kaufen.
* **Angepasstes Event ausführen**: Ich möchte, dass meine Nutzer:innen eine bestimmte Aktion ausführen, die ich als angepasstes Event tracke.
* **App upgraden**: Ich möchte, dass meine Nutzer:innen ihre App-Version upgraden.

### Das „Wann“: Startbedingungen erstellen {#the-when-create-starting-conditions}

*Wann wird eine:r Nutzer:in diese Erfahrung beginnen?*

Ihre Antwort bestimmt die Details, wann und wie Ihr Canvas an Ihre Kund:innen zugestellt wird. Nutzer:innen können Ihr Canvas auf zwei Arten betreten: durch geplante oder aktionsbasierte Trigger.

{% alert tip %}
Weitere Strategien und Antworten auf häufige Fragen finden Sie unter [Zeitbasierte Funktionen]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) für Canvas.
{% endalert %}

Die geplante Zustellung ermöglicht es Ihnen, ein Canvas sofort an Ihre Zielgruppe zu senden. Sie können es auch regelmäßig senden lassen oder für einen bestimmten Zeitpunkt in der Zukunft planen. Aktionsbasierte Canvases reagieren auf bestimmtes Kundenverhalten in Echtzeit. Beispielsweise kann ein aktionsbasierter Trigger das Öffnen einer App, einen Kauf, die Interaktion mit einer anderen Campaign oder das Auslösen eines beliebigen angepassten Events umfassen. Zum Zeitpunkt der Aktion können Sie das Canvas an Ihre Nutzer:innen senden lassen.

### Das „Wer“: Eine Zielgruppe auswählen {#the-who-select-an-audience}

*Wen versuchen Sie zu erreichen?*

Um Ihr „Wer“ zu definieren, können Sie vordefinierte Segmente verwenden, die in Canvas verfügbar sind. Sie können auch weitere Filter hinzufügen, um den Fokus auf Ihre Zielgruppe weiter zu verfeinern. Nach dem Aufbau dieser Segmente können nur die Nutzer:innen, die den Kriterien der Zielgruppe entsprechen, die Canvas-Journey betreten, was zu einer stärker personalisierten Erfahrung führt. In dieser Tabelle finden Sie die verfügbaren Filter und wie sie Ihre Nutzer:innen für Ihren Anwendungsfall segmentieren.

| Filter | Beschreibung |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Angepasste Daten | Segmentieren Sie Nutzer:innen basierend auf Events und Attributen, die Sie definieren. Kann produktspezifische Features verwenden. |
| Nutzeraktivität | Segmentieren Sie Kund:innen basierend auf ihren Aktionen und Käufen. |
| Retargeting | Segmentieren Sie Kund:innen, denen vorherige Canvases gesendet wurden, die sie erhalten oder mit denen sie interagiert haben. |
| Marketing-Aktivität | Segmentieren Sie Kund:innen basierend auf universellen Verhaltensweisen wie dem letzten Engagement. |
| Nutzerattribute | Segmentieren Sie Kund:innen nach ihren konstanten Attributen und Eigenschaften. |
| Install-Attribution | Segmentieren Sie Kund:innen nach ihrer ersten Quelle, Anzeigengruppe, Campaign oder Anzeige. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Das „Wer“: Eine Zielgruppe auswählen" }

### Das „Wo“: Meine Zielgruppe finden {#the-where-find-my-audience}

*Wo kann ich meine Zielgruppe am besten erreichen?*

Hier bestimmen wir, welche Messaging-Kanäle für Ihre User Journey am sinnvollsten sind. Idealerweise möchten Sie Ihre Nutzer:innen dort erreichen, wo sie am besten erreichbar sind. Vor diesem Hintergrund können Sie jeden der folgenden Kanäle mit Canvas verwenden:
* [E-Mail]({{site.baseurl}}/user_guide/channels/email)
* [Push]({{site.baseurl}}/user_guide/channels/push)
* [In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages)
* [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)
* [SMS oder MMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs)
* [Webhook]({{site.baseurl}}/user_guide/channels/webhooks)

### Das „Wie“: Die vollständige Erfahrung aufbauen {#the-how-build-the-complete-experience}

*Wie baue ich meine Canvas-Journey auf, nachdem ich die fünf W-Fragen identifiziert habe?*

Das „Wie“ fasst zusammen, wie Sie Ihr Canvas erstellen und wie Sie Ihre Nutzer:innen mit Ihrer Nachricht erreichen. Damit eine Nachricht beispielsweise effektiv ist, sollten Sie das Timing Ihres Messagings in Bezug auf die Zeitzonen Ihrer verschiedenen Nutzer:innen optimieren.

Die Beantwortung des „Wie“ bestimmt auch die Frequenz, mit der ein Canvas an Ihre Zielgruppe gesendet wird (z. B. einmal pro Woche oder alle zwei Wochen), und welche Messaging-Kanäle für jedes Canvas genutzt werden sollen, wie beim „Wo“ beschrieben.

## Anwendungsfall: Kunden-Onboarding-Flow {#use-case-customer-onboarding-flow}

Nehmen wir beispielsweise an, Sie sind Marketer bei MovieCanon, einem Online-Streaming-Unternehmen, und Sie sind für die Erstellung eines Onboarding-Flows für neue Nutzer:innen Ihrer App verantwortlich. Anhand der fünf W-Fragen könnten wir das Canvas folgendermaßen aufbauen.

* **Was**: Unser Canvas-Name wird „New Onboarding Journey“ sein.
* **Warum**: Das Ziel unseres Canvas ist es, unsere Nutzer:innen willkommen zu heißen und sie dazu zu bringen, die App weiterhin zu nutzen.
* **Wann**: Nachdem eine:r Nutzer:in die App zum ersten Mal öffnet, möchten wir eine Willkommens-E-Mail senden.
* **Wer**: Wir sprechen neue Nutzer:innen an, die unsere App zum ersten Mal verwenden.
* **Wo**: Wir sind zuversichtlich, dass wir neue Nutzer:innen per E-Mail erreichen können – so haben wir auch unser bisheriges Messaging gestaltet.
* **Wie**: Wir möchten eine eintägige Verzögerung einrichten, um unsere neuen Nutzer:innen nicht mit Benachrichtigungen zu überfordern. Nach dieser Verzögerung senden wir eine E-Mail mit einer Liste der beliebtesten Filme und TV-Serien, um sie dazu zu motivieren, die App weiterhin zu nutzen.

## Allgemeine Tipps {#general-tips}

### Bestimmen Sie, wann und wie Sie Schritte und Varianten verwenden {#determine-when-and-how-to-use-steps-and-variants}

Jedes Canvas muss mindestens eine Variante und mindestens einen Schritt haben. Darüber hinaus sind keine Grenzen gesetzt – wie entscheiden Sie also über die Form Ihres Canvas? Hier kommen Ihre Ziele, Daten und Hypothesen ins Spiel. Das Brainstorming zum „Wie“ und „Wo“ hilft Ihnen, die richtige Form und Struktur Ihres Canvas zu planen.

### Rückwärts arbeiten {#work-backwards}

Einige Ziele haben kleinere Unterziele. Wenn Sie beispielsweise darauf abzielen, eine:n kostenlose:n Nutzer:in in ein Abo umzuwandeln, benötigen Sie möglicherweise eine Seite, auf der Ihre Abo-Dienste aufgeführt sind. Besucher:innen müssen möglicherweise die Optionen sehen, bevor sie kaufen. Sie könnten Ihre Messaging-Bemühungen darauf konzentrieren, ihnen diese Seite vor einer Checkout-Seite zu zeigen. Rückwärts zu arbeiten, um die Journey zu verstehen, die Kund:innen durchlaufen müssen, um Ihr Ziel zu erreichen, ist der Schlüssel, um sie zur Konversion zu führen.

### Variieren Sie Ihr Messaging {#mix-up-your-messaging}

Haben Sie in der Vergangenheit eine ähnliche Campaign durchgeführt? Oder läuft gerade eine? Versuchen Sie, diese eine Nachricht zu verwenden und mehr Personalisierung hinzuzufügen. Probieren Sie einen neuen Filter aus oder fügen Sie eine Follow-up-Nachricht hinzu. Wenn Sie Ihre Messaging-Techniken variieren, beobachten Sie Ihre Performance und optimieren Sie kontinuierlich durch schrittweise Änderungen.