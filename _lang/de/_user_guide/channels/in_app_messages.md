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

> In-App-Nachrichten helfen Ihnen, Inhalte an Ihre Nutzer:innen zu übermitteln, ohne deren Tag mit einer Push-Benachrichtigung zu unterbrechen. Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größtmöglichen Nutzen aus Ihrer App zu ziehen. Mit einer Vielzahl von Layouts und Anpassungstools zur Auswahl binden In-App-Nachrichten Ihre Nutzer:innen stärker ein als je zuvor.

## Voraussetzungen {#prerequisites}

Bevor Sie In-App-Nachrichten senden können, müssen Sie das [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) in Ihre App oder Website integrieren. Es ist keine zusätzliche Einrichtung erforderlich.

Informationen zu Mindest-SDK-Versionen und Feature-spezifischen Anforderungen finden Sie unter:
- [Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Nachrichtentypen]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types)

## Anwendungsfälle {#use-cases}

Dank der umfangreichen Inhalte, die In-App-Nachrichten bieten, können Sie diesen Kanal für eine Vielzahl von Anwendungsfällen nutzen:

| Anwendungsfall | Erklärung |
| --- | --- |
| Push-Priming | Führen Sie eine [Push-Priming]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)-Campaign mit einer reichhaltigen In-App-Nachricht durch, um Ihren Kund:innen die Vorteile des Push-Opt-ins für Ihre App oder Website zu zeigen, und präsentieren Sie ihnen eine Aufforderung, die Push-Berechtigung zu erteilen.
| Verkäufe und Aktionen | Verwenden Sie modale In-App-Nachrichten, um Kund:innen mit visuell ansprechenden Medien zu begrüßen, die statische Aktionscodes oder Angebote enthalten. Motivieren Sie sie zu Käufen oder Conversions, die sie sonst nicht getätigt hätten. |
| Feature-Adoption fördern | Ermutigen Sie Kund:innen, andere Bereiche Ihrer App zu nutzen oder einen Dienst in Anspruch zu nehmen. |
| Hochgradig personalisierte Campaigns | Platzieren Sie In-App-Nachrichten als Erstes, was Ihre Kund:innen sehen, wenn sie Ihre App oder Website öffnen. Fügen Sie einige Braze-Personalisierungsfeatures hinzu, wie z. B. [Connected-Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), um Nutzer:innen zum Handeln zu bewegen und so Ihre Ansprache effektiver zu gestalten.
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

Slideup-Nachrichten erscheinen in der Regel am oberen oder unteren Rand des App-Bildschirms (Sie können dies beim Erstellen Ihrer Nachricht festlegen). Diese eignen sich hervorragend, um Ihre Nutzer:innen über neue Nutzungsbedingungen, Cookies und andere Informationen zu informieren.

![Slideup-In-App-Nachricht, die vom unteren Rand des App-Bildschirms erscheint. Der Slideup enthält ein Icon-Bild und eine kurze Nachricht.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Modale Nachrichten erscheinen in der Mitte des Gerätebildschirms mit einem Bildschirm-Overlay, das sie vom Hintergrund Ihrer App abhebt. Diese eignen sich perfekt, um Ihre Nutzer:innen auf einen Verkauf oder ein Gewinnspiel aufmerksam zu machen.

![Modale In-App-Nachricht, die in der Mitte einer App und Website als Dialog erscheint. Das Modal enthält ein Bild, eine Überschrift, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Vollbild %}

Vollbild-Nachrichten sind genau das, was Sie erwarten würden – sie nehmen den gesamten Bildschirm des Geräts ein! Dieser Nachrichtentyp eignet sich hervorragend, wenn Sie wirklich die Aufmerksamkeit Ihrer Nutzer:innen benötigen, z. B. für obligatorische App-Updates.

![Vollbild-In-App-Nachricht, die einen App-Bildschirm einnimmt. Die Vollbild-Nachricht enthält ein großes Bild, eine Überschrift, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Zusätzlich zu diesen Standard-Nachrichtentemplates können Sie Ihr Messaging auch mit benutzerdefinierten HTML-In-App-Nachrichten, Web-Modalen mit CSS oder Web-E-Mail-Erfassungsformularen weiter anpassen. Weitere Informationen finden Sie unter [Anpassen]({{site.baseurl}}/user_guide/channels/in_app_messages/customize).

Informationen dazu, wie die Template-basierte Zustellung zum Anzeigezeitpunkt das **Abbruch**-Logging beeinflusst, finden Sie in den [FAQ zu In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/in_app_messages/faq).

## Nächste Schritte {#next-steps}

- [Erstellen Sie eine In-App-Nachricht mit dem Drag-and-Drop-Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop)
- [Erstellen Sie eine In-App-Nachricht mit dem traditionellen Editor]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}