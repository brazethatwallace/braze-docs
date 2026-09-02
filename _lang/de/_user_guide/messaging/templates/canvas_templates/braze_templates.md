---
nav_title: Braze-Templates verwenden
article_title: Braze-Canvas-Templates verwenden
alias: "/canvas_templates/templates/"
page_order: 2
description: "Dieser Referenzartikel beschreibt, wie Sie die verfügbaren Canvas-Templates erstellen und verwenden können."
page_type: reference
---

# Braze-Canvas-Templates verwenden {#use-braze-canvas-templates}

> Braze bietet eine Auswahl an Canvas-Templates, die Sie als Referenz und Best Practices für gängige Anwendungsfälle nutzen können. Diese Templates können zwar nicht bearbeitet werden, aber Sie können sie unter **Inhalt** > **Canvas** > **Braze templates** ansehen oder in Ihren Canvase verwenden.

![Braze-Templates im Bereich „Canvas-Templates“ mit dreizehn verfügbaren Templates.]({% image_buster /assets/img/braze_canvas_templates.png %})

Wählen Sie aus den folgenden verfügbaren Templates, um sie als Referenz oder als Grundlage für Ihr Canvas zu verwenden.

## Standard-Canvas-Templates {#standard-canvas-templates}

{% tabs %}
{% tab Abandoned Intent %}

### Abandoned Intent {#abandoned-intent}

Sprechen Sie Nutzer:innen in Echtzeit an, um sie zum Abschluss ihrer Käufe zu ermutigen.

Beachten Sie Folgendes bei der Verwendung dieses Templates:

- Der Entry-Zeitplan ist API-getriggert. Verwenden Sie den [`/canvas/trigger/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases), um Nutzer:innen einzutragen, wenn sie einen Warenkorb abbrechen, oder wechseln Sie zu einem aktionsbasierten Zeitplan mit einem Trigger or triggern wie **Angepasstes Event ausführen** oder **Warenkorb-Update or aktualisieren-Event ausführen**, wenn dies besser zu Ihrem Setup passt.
- Die Standard-Conversion trackt **Beliebigen Kauf tätigen (Legacy)**. Passen Sie Konversions-Events und die **Kauf getätigt?**-Aktionspfade-Schritte bei Bedarf auf bestimmte Produkte an.
- Nutzer:innen verlassen das Canvas, wenn sie in den **Kauf getätigt?**-Aktionspfade-Schritten einen Kauf tätigen. Dieses Template setzt voraus, dass Sie eine separate Post-Purchase-Journey haben.
- Das Canvas enthält eine E-Mail für **Artikelbasierte Erinnerung**, einen Delay-Schritt, einen intelligenten Kanal-Split für E-Mail und Kurzmitteilungsdienst or SMS, Kanalnachrichten mit Content Cards (E-Mail, Kurzmitteilungsdienst or SMS und In-App-Nachricht) sowie einen Audience-Sync-Schritt. Konfigurieren Sie **Ad Retargeting** mit Ihren Partnern und Zielgruppen.

Eine Schritt-für-Schritt-Anleitung finden Sie unter [Warenkorb-Abbruch]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates/abandoned_cart).

{% endtab %}
{% tab Back In Stock %}

### Back in Stock {#back-in-stock}

Steigern Sie Käufe, indem Sie Ihre Nutzer:innen mit personalisiertem Messaging benachrichtigen, wenn ein Artikel wieder auf Lager ist. Beachten Sie Folgendes bei der Verwendung dieses Templates:

- Wählen Sie unter **Entry-Zeitplan** einen Katalog aus. So können Sie auf Daten wie Produkte, Rabatte und Aktionen zugreifen, um Ihre Nutzer:innen gezielter anzusprechen.
- Fügen Sie unter **Zielgruppe** ein Segment hinzu, um Nutzer:innen anzusprechen, die Interesse an einem bestimmten Artikel bekundet haben.
- Update or aktualisieren or aktualisieren Sie in den Nachrichtenschritten im gesamten Canvas die Liquid-Referenzen auf Ihren Katalog.

{% endtab %}
{% tab Feature Adoption %}

### Feature-Adoption {#feature-adoption}

Senden Sie zeitlich abgestimmte, personalisierte Nachrichten, die die Vorteile und Nutzungstipps hervorheben. Beachten Sie Folgendes bei der Verwendung dieses Templates:

- Schließen Sie Nutzer:innen aus, die das Feature bereits übernommen haben. Fügen Sie beispielsweise unter **Zielgruppe** einen Filter für ein angepasstes Event wie „Activated Feature“ hinzu, das bereits stattgefunden hat.
- Um den Experiment-Pfad-Schritt zu verwenden, definieren Sie ein Konversions-Event. Dieses Event sollte das Event sein, das die Feature-Übernahme signalisiert.
- Richten Sie den Aktionspfad-Schritt im Template mit angepassten Events für „Activated Feature“ und „Taken Tour“ ein.
- Richten Sie die angepassten Attribute im Nachrichtenschritt „Feedback Survey“ ein, um die Stimmung des Feedbacks zu erfassen.

{% endtab %}
{% tab Lapsed User %}

### Lapsed User {#lapsed-user}

Holen Sie Nutzer:innen mit Anreizen basierend auf ihren bisherigen Interaktionen zurück in Ihre App. Beachten Sie Folgendes bei der Verwendung dieses Templates:

- Wählen Sie unter **Basics** eine bestimmte App aus, für die Conversions getrackt werden sollen.
- Fügen Sie im Canvas-Editor bestimmte Apps für die Aktionspfade-Schritte hinzu.
- Konfigurieren Sie den Audience-Sync-Schritt mit den Partnern und Zielgruppen für Ihren Anwendungsfall.

{% endtab %}
{% tab Onboarding %}

### Onboarding {#onboarding}

Erstellen Sie Onboarding-Journeys, die eine starke anfängliche Nutzung fördern und dauerhafte Beziehungen zu Ihren Nutzer:innen aufbauen. Beachten Sie Folgendes bei der Verwendung dieses Templates:

- Erwägen Sie im Zielgruppenpfad-Schritt „Audience Split“, die Schlüsselaktionen für engagierte Nutzer:innen anzupassen. Im Template lautet der Segment-Filter „Has clicked email for step Welcome Email“.

{% endtab %}
{% tab Post-Purchase Feedback %}

### Post-Purchase Feedback {#post-purchase-feedback}

Orchestrieren Sie personalisierte Erlebnisse, die es Ihnen ermöglichen, auf Feedback zu reagieren und eine Beziehung zu Ihren Nutzer:innen aufzubauen. Beachten Sie Folgendes bei der Verwendung dieses Templates:

- Im ersten Schritt des Canvas-Editors:
    - Geben Sie die angepassten Attribute in der In-App-Nachricht an, um die Stimmung des Feedbacks basierend auf der ausgewählten Umfrageoption zu kennzeichnen.
    - Geben Sie Attribute auf Links für jeden Call-to-Action an, um zu erfassen, welche Option ausgewählt wurde. Diese Attribute werden im nachfolgenden Zielgruppenpfad referenziert.
- Passen Sie den Zielgruppenpfad mit den Attributen aus dem ersten Schritt dieses Templates an.
- Richten Sie den Audience-Sync-Schritt „Ad Retargeting“ ein.

{% endtab %}
{% endtabs %}

## E-Commerce-Canvas-Templates {#ecommerce-canvas-templates}

E-Commerce-Canvas-Templates sind speziell auf E-Commerce-Marketer zugeschnitten und erleichtern die Umsetzung wesentlicher Strategien.

{% multi_lang_include Canvas/ecommerce_templates.md %}