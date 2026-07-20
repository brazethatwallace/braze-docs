---
nav_title: Braze Pilot
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze Pilot"
guide_top_text: "Braze Pilot ist eine mobile App, die für die nahtlose Verbindung mit Ihrem Braze-Dashboard entwickelt wurde. Sie ermöglicht es Ihnen, Campaigns und Canvases in der App zu starten und Braze-Nachrichten auf Ihrem eigenen Smartphone zum Leben zu erwecken. Braze Pilot umfasst eine Bibliothek mit App-Simulationen für fiktive Marken aus verschiedenen Branchen, mit denen Sie erleben können, wie Ihr Messaging aus der Perspektive Ihrer Kund:innen aussehen könnte."
description: "Entdecken Sie die verschiedenen Möglichkeiten, wie Sie Braze nutzen können, um Nachrichten vom Braze-Dashboard auf Ihr Smartphone zu senden."

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: Erste Schritte mit Braze Pilot
    link: /docs/user_guide/get_started/braze_pilot/getting_started
    image: /assets/img/braze_icons/brush-02.svg
  - name: Datenwörterbuch
    link: /docs/user_guide/get_started/braze_pilot/data_dictionary
    image: /assets/img/braze_icons/book-closed.svg
  - name: Navigations-Deeplinks
    link: /docs/user_guide/get_started/braze_pilot/deep_links
    image: /assets/img/braze_icons/link-03.svg

---

## Pilot-App-Simulationen {#pilot-app-simulations}

Das Herzstück von Braze Pilot ist die Bibliothek mit App-Simulationen. Jede App ist eine realistische Simulation einer branchenspezifischen fiktiven Marke, die so instrumentiert ist, dass sie eine Vielzahl von Ereignissen und Attributen protokolliert und damit unzählige Möglichkeiten für gängige Braze-Anwendungsfälle bietet.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington ist eine Fitness-App mit Trainingsprogrammen, Trainingszielen und einem Steppington+ Premium-Dienst. Sie bietet mehrere Möglichkeiten zur Demonstration von [Content Cards]({{site.baseurl}}/user_guide/channels/content_cards), einen Bereich, der mit [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags) freigeschaltet werden kann, sowie eine umfangreiche Bibliothek zur Protokollierung angepasster Events, mit denen sich viele Customer Journeys für diese Branche veranschaulichen lassen.

![Die Startseite von Steppington mit Symbolen für Marathontraining, Yoga, Radfahren und Krafttraining.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab E-Commerce %}

### PantsLabyrinth

PantsLabyrinth ist eine E-Commerce-App, die (Sie haben es erraten) Hosen verkauft! Die PantsLabyrinth-App umfasst ein vollständiges Warenkorb-Checkout-Erlebnis, eine optionale Wunschliste, die mit einem Feature-Flag aktiviert werden kann, sowie zahlreiche Möglichkeiten für humorvolle Anspielungen mit Freunden aus Großbritannien.

![Eine Produktseite für PantsLabyrinth mit Optionen zum Hinzufügen von Jeans zum Warenkorb.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon

MovieCanon ist ein Streaming-Dienst, der ideal geeignet ist, um gängige Braze-Anwendungsfälle rund um Content-Engagement zu veranschaulichen.

![Die MovieCanon-App mit einer Auswahl an verschiedenen Thrillern zum Anschauen.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Wie Pilot sich mit Ihrem Braze-Dashboard verbindet {#how-pilot-connects-with-your-braze-dashboard}

Das Braze SDK ist ein Code-Paket, das Daten von Ihren Nutzer:innen sammelt, sobald es in Ihre App oder Website integriert ist. Wenn Sie Pilot mit Ihrem Dashboard verbinden, initialisieren Sie diese Verbindung zwischen der Pilot-App auf Ihrem Smartphone und dem Braze SDK und stellen eine eindeutige Verbindung zu Ihrer Braze-Instanz her, indem Sie Pilot Ihren API-Schlüssel-Bezeichner für Ihr Dashboard mitteilen.

![Der erste Schritt zur Einrichtung von Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Nachdem Pilot eine Verbindung zu Ihrem Braze-Dashboard hergestellt hat, funktioniert das Braze SDK in der App genauso wie nach der Integration des SDK in Ihre eigene App oder Website. Das bedeutet, dass Braze:

- Daten zu Ihren Nutzeraktivitäten in Pilot speichert, einschließlich angepasster Daten, die für die fiktiven Marken in der App spezifisch sind.
- Automatisch Sitzungsdaten, Geräteinformationen und Push-Token erfasst.
- Push-Benachrichtigungen, In-App-Nachrichten und Content-Card-Messaging-Kanäle unterstützt, die eine SDK-Integration erfordern, um zu funktionieren.

Weitere Informationen zum Braze SDK finden Sie unter [Integration]({{site.baseurl}}/user_guide/get_started/integrations).

![Der Braze-Customer-Engagement-Stack umfasst Integrationen, APIs und SDKs für die Datenaufnahme, Klassifizierung, Orchestrierung, Personalisierung und Aktionen mit Messaging-Kanälen für einen interaktiven Feedback-Loop mit Ihren Kund:innen.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Nutzerprofile in Braze {#user-profiles-in-braze}

Jedes an Braze gesendete Datenelement wird in einem Nutzerprofil gespeichert, das einer/einem bestimmten Nutzer:in Ihrer App oder Website zugeordnet ist. Sobald Sie Pilot mit Ihrem Braze-Dashboard verbinden, beginnt Braze mit der Protokollierung von Daten über Sie als Nutzer:in von Pilot. Es gibt zwei Arten von Nutzer:innen, die über diese Verbindung für Sie erstellt werden können: anonyme und identifizierte.

### Anonym {#anonymous}

Dieser Verbindungsstatus spiegelt die Erfahrung eines Gastes Ihrer App oder Website wider, der sich noch nicht angemeldet hat. Wenn Sie Pilot als anonyme:r Nutzer:in initialisieren, erstellt Braze ein [anonymes Nutzerprofil]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users) für Sie und protokolliert dort Daten zu Ihren Aktivitäten. Anonyme Nutzer:innen können weiterhin mit Campaigns angesprochen werden, jedoch ist es nicht möglich, ihr Nutzerprofil direkt in Ihrem Braze-Dashboard aufzurufen.

### Identifiziert {#identified}

Dieser Verbindungsstatus bedeutet, dass Braze Ihr Nutzerprofil anhand eines Ihnen zugewiesenen eindeutigen Bezeichners erkennt, der als externe ID bezeichnet wird. Sie können auf der Seite **Nutzersuche** Ihres Dashboards nach dieser externen ID suchen, um Ihr Nutzerprofil zu finden, in dem alle Nutzerattribute und Events gespeichert sind, die von Pilot basierend auf Ihren Aktivitäten in der App protokolliert wurden. Gehen Sie im Braze-Dashboard zu **Audience** > **Nutzersuche**, geben Sie Ihre **externe ID** für Pilot ein und öffnen Sie das Profil, um Attribute und Events zu prüfen.

### Verbindungstyp {#connection-type}

Um zu überprüfen, welche Art von Verbindung Sie haben, sehen Sie oben in der Pilot-App den Verbindungsstatus.

{% tabs local %}
{% tab Anonyme:r Nutzer:in  %}

**Anonym** bedeutet, dass Sie Daten als anonyme:r Nutzer:in protokollieren. Der Statusbereich zeigt eine **Anonym**-Kennzeichnung (z. B. ein Masken- oder Inkognito-Symbol).

{% endtab %}
{% tab Identifizierte:r Nutzer:in %}

Wenn Sie Daten als identifizierte:r Nutzer:in protokollieren, zeigt der Statusbereich **Identifizierte:r Nutzer:in** und Ihre externe ID an.

{% endtab %}
{% tab Nicht verbunden %}

**Nicht verbunden** bedeutet, dass Sie die Braze-SDK-Verbindung mit Pilot noch nicht initialisiert haben. Der Statusbereich weist darauf hin, dass Pilot noch nicht mit Ihrem Braze-Workspace verbunden ist.

{% endtab %}
{% endtabs %}

## Campaigns und Canvases {#campaigns-and-canvases}

Mit Campaigns und Canvases senden Sie Nachrichten an Ihre Nutzer:innen.

- Campaigns eignen sich am besten für einzelne Nachrichten, die über verschiedene Kanäle an ein bestimmtes Zielgruppensegment gesendet werden.
- Canvases sind fortgeschrittene Campaign-Workflows, mit denen Sie personalisierte Customer Journeys über mehrere Kanäle hinweg automatisieren und orchestrieren können. Innerhalb eines Canvas können Sie Verzweigungslogiken, Verzögerungen, Entscheidungspunkte und Konversions-Events einrichten, um Kund:innen durch eine Reihe von Interaktionen zu führen. Canvases tragen dazu bei, eine konsistente und nahtlose Kommunikation über verschiedene Kontaktpunkte hinweg sicherzustellen und so die Chancen für Customer-Engagement und Konversion zu erhöhen.

## Unterstützte Messaging-Kanäle {#supported-messaging-channels}

Braze Pilot unterstützt derzeit [In-App-Nachrichten]({{site.baseurl}}/in-app_messages), die in Ihrer App angezeigt werden und zeitnahe Nachrichten übermitteln, während die Nutzer:innen aktiv mit der App interagieren.

![Eine In-App-Nachricht in der MovieCanon-App: „Gefällt Ihnen MovieCanon? Empfehlen Sie es Ihren Freunden!“ mit der Option, Ihre E-Mail-Adresse einzugeben, um eine Empfehlung zu versenden.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}