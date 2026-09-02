---
nav_title: "In-App-Nachrichten"
article_title: "In-App-Nachrichten"
page_order: 5
page_type: landing
alias: /in-app_messages/
description: "Binden Sie Nutzer:innen mit angepassten In-App-Nachrichten ein, die das Nutzererlebnis durch eine Vielzahl von Layouts und Personalisierungstools in Braze verbessern."
channel:
  - in-app messages
search_rank: 5
---

# In-App-Nachrichten {#in-app-messages}

> In-App-Nachrichten liefern Inhalte innerhalb Ihrer App oder Website, ohne Nutzer:innen mit einer Push-Benachrichtigung zu unterbrechen. Angepasste In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, durch Layouts, Personalisierung und Targeting-Tools mehr Wert aus Ihrem Produkt zu ziehen. Dieser Hub behandelt Nachrichtentypen, den Drag-and-Drop-Editor, Voraussetzungen und gängige Anwendungsfälle wie Onboarding und Aktionen. Integrieren Sie das [Braze SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web), bevor Sie Ihre erste In-App-Nachricht erstellen, und wählen Sie dann ein Standard- oder angepasstes Layout für Ihre Campaign.

## Voraussetzungen {#prerequisites}

Bevor Sie In-App-Nachrichten senden können, müssen Sie das [Braze SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) in Ihre App oder Website integrieren. Eine zusätzliche Einrichtung ist nicht erforderlich.

Informationen zu Mindest-SDK or Software-Development-Kit-Versionen und Feature-spezifischen Anforderungen finden Sie unter:
- [Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Nachrichtentypen]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)

## Anwendungsfälle {#use-cases}

Mit der umfangreichen Gestaltungsmöglichkeit von In-App-Nachrichten können Sie diesen Kanal für eine Vielzahl von Anwendungsfällen nutzen:

| Anwendungsfall | Erklärung |
| --- | --- |
| Push-Vorbereitung | Führen Sie eine [Push-Vorbereitung]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)-Campaign mit einer reichhaltigen In-App-Nachricht durch, um Ihren Kund:innen den Vorteil des Push-Opt-ins für Ihre App oder Website zu zeigen, und fordern Sie sie auf, die Push-Berechtigung zu erteilen.
| Verkaufsaktionen und Aktionen | Verwenden Sie modale In-App-Nachrichten, um Kund:innen mit visuell ansprechenden Medien zu begrüßen, die statische Aktionscodes oder Angebote enthalten. Motivieren Sie sie zu Käufen oder Konversionen, die sie andernfalls nicht getätigt hätten. |
| Förderung der Feature-Nutzung | Ermutigen Sie Kund:innen, andere Bereiche Ihrer App zu nutzen oder einen Dienst in Anspruch zu nehmen. |
| Hochgradig personalisierte Campaigns | Platzieren Sie In-App-Nachrichten als erstes, was Ihre Kund:innen sehen, wenn sie Ihre App oder Website öffnen. Fügen Sie Braze-Personalisierungs-Features wie [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) hinzu, um Nutzer:innen zum Handeln zu bewegen und Ihre Kommunikation so effektiver zu gestalten.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anwendungsfälle" }

Weitere Anwendungsfälle, die Sie in Betracht ziehen sollten:

- Neue App-Features
- App-Verwaltung
- Bewertungen
- App-Upgrades oder -Updates
- Gewinnspiele und Verlosungen

## Standard-Nachrichtentypen {#standard-message-types}

Die folgenden Tabs zeigen, wie es für Ihre Nutzer:innen aussieht, wenn sie einen unserer Standard-In-App-Nachrichtentypen öffnen – Slideup, Modal und Vollbild-In-App-Nachrichten.

{% tabs %}
{% tab Slideup %}

Slideup-Nachrichten erscheinen in der Regel am oberen oder unteren Rand des App-Bildschirms (Sie können dies beim Erstellen Ihrer Nachricht festlegen). Sie eignen sich hervorragend, um Ihre Nutzer:innen über neue Nutzungsbedingungen, Cookies und andere Informationen zu benachrichtigen.

![Slideup-In-App-Nachricht, die vom unteren Rand des App-Bildschirms eingeblendet wird. Das Slideup enthält ein Icon-Bild und eine kurze Nachricht.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Modals erscheinen in der Mitte des Gerätebildschirms mit einem Bildschirm-Overlay, das sie vom Hintergrund Ihrer App abhebt. Sie eignen sich perfekt, um Ihre Nutzer:innen dezent auf einen Sale oder ein Gewinnspiel aufmerksam zu machen.

![Modale In-App-Nachricht, die in der Mitte einer App und Website als Dialog erscheint. Das Modal enthält ein Bild, eine Überschrift, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Vollbild %}

Vollbild-Nachrichten sind genau das, was Sie erwarten – sie nehmen den gesamten Bildschirm des Geräts ein! Dieser Nachrichtentyp eignet sich hervorragend, wenn Sie die Aufmerksamkeit Ihrer Nutzer:innen wirklich brauchen, zum Beispiel für erforderliche App-Updates.

![Vollbild-In-App-Nachricht, die den gesamten App-Bildschirm einnimmt. Die Vollbild-Nachricht enthält ein großes Bild, eine Überschrift, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Zusätzlich zu diesen Standard-Nachrichten-Templates können Sie Ihr Messaging mit benutzerdefinierten HTML-In-App-Nachrichten, Web-Modals mit CSS oder Web-E-Mail-Erfassungsformularen weiter anpassen. Weitere Informationen finden Sie unter [Anpassen]({{site.baseurl}}/user_guide/channels/in_app_messages/customize).

Informationen dazu, wie die Template-basierte Zustellung zum Anzeigezeitpunkt das **Abbruch**-Logging beeinflusst, finden Sie in den [FAQ zu In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Nächste Schritte {#next-steps}

- [Eine In-App-Nachricht mit dem Drag-and-Drop-Editor erstellen]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Eine In-App-Nachricht mit dem traditionellen Editor erstellen]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}