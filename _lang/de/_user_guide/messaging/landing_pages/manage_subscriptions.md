---
nav_title: Block „Abos verwalten“
article_title: Block „Abos verwalten“
description: "Dieser Artikel beschreibt, wie Sie den Formularblock „Abos verwalten“ auf einer Braze Landing-Page hinzufügen und konfigurieren, damit Verbraucher:innen sich für E-Mail-Abo-Gruppen anmelden und diese verwalten können."
page_order: 5
---

# Block „Abos verwalten“ {#manage-subscriptions-block}

> Fügen Sie einer Landing-Page einen Block **Abos verwalten** hinzu, damit Nutzer:innen ihre E-Mail-Abo-Gruppen einsehen, sich dafür anmelden und sie aktualisieren können.

Der Block **Abos verwalten** unterstützt zwei zentrale Anwendungsfälle:

- **[Bestehende Abos verwalten](#update-existing-subscriptions):** Teilen Sie den [Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) der Landing-Page in einer E-Mail oder einer anderen Kanalnachricht. Wenn identifizierte Nutzer:innen die Seite öffnen, füllt der Block automatisch die Checkbox jeder Abo-Gruppe mit dem aktuellen Abo-Status vor, sodass sie ihre Einstellungen überprüfen und aktualisieren können.
- **[Neue Opt-ins erfassen](#capture-new-subscribers):** Fügen Sie den Block zusammen mit einem **E-Mail-Erfassungs**-Block zu einer Landing-Page für die Lead-Generierung hinzu, damit neue Besucher:innen beim Absenden des Formulars auswählen können, welchen Abo-Gruppen sie beitreten möchten.

{% alert important %}
Der Block **Abos verwalten** unterstützt nur [E-Mail-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups). SMS-, RCS- oder WhatsApp-Abo-Gruppen werden nicht unterstützt.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| E-Mail-Abo-Gruppen | Mindestens eine [E-Mail-Abo-Gruppe]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups), die [über das Dashboard]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-subscription-group) oder die [Abo-Gruppen-Endpunkte]({{site.baseurl}}/api/endpoints/subscription_groups) erstellt wurde. |
| Landing-Page-Berechtigungen | Dieselben [Berechtigungen]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites), die zum Erstellen und Bearbeiten jeder Landing-Page erforderlich sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Schritt 1: Block „Abos verwalten“ hinzufügen {#step-1-add-the-manage-subscriptions-block}

Gehen Sie im Drag-and-Drop-Editor für Landing-Pages zum Abschnitt **Erstellen** und wählen Sie **Formularblöcke** aus. Ziehen Sie **Abos verwalten** in eine Zeile auf Ihrer Seite; der Block passt sich automatisch an die Spaltenbreite an.

Der Block ist leer, bis Sie Abo-Gruppen hinzufügen.

## Schritt 2: Abo-Gruppen auswählen {#step-2-select-the-subscription-groups}

Wählen Sie bei ausgewähltem Block **Abos verwalten** im rechten Panel **Blockeigenschaften** die Option **+ Abo-Gruppen hinzufügen** aus. Daraufhin wird eine Liste der in Ihrem Workspace verfügbaren [E-Mail-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) angezeigt.

Aktivieren Sie die Checkbox neben jeder Abo-Gruppe, die Sie einschließen möchten, und bestätigen Sie Ihre Auswahl, um sie dem Block hinzuzufügen. Jede Abo-Gruppe wird als eigene auswählbare Checkbox auf der Landing-Page angezeigt.

{% alert note %}
Der Block **Abos verwalten** listet nur Gruppen auf, die Sie explizit hinzufügen. Das Hinzufügen einer Abo-Gruppe zum Block abonniert Besucher:innen nicht automatisch – sie müssen die Checkbox der Gruppe aktivieren und das Formular absenden.
{% endalert %}

## Schritt 3: Blockeinstellungen konfigurieren {#step-3-configure-the-block-settings}

Verwenden Sie das Panel **Blockeigenschaften**, um das Verhalten und die Darstellung des Blocks anzupassen.

### Abo-Gruppen {#subscription-groups}

- **Gruppen neu anordnen:** Ziehen Sie eine Abo-Gruppe an ihrem Griff, um die Reihenfolge im Block zu ändern.
- **Gruppen hinzufügen oder entfernen:** Wählen Sie **+ Abo-Gruppen hinzufügen**, um weitere Gruppen einzuschließen, oder wählen Sie das Löschsymbol neben einer Gruppe, um sie aus dem Block zu entfernen.

### Beschreibungen einschließen {#include-descriptions}

Aktivieren Sie **Beschreibungen einschließen**, um den Beschreibungstext jeder Abo-Gruppe neben ihrem Namen anzuzeigen, damit Besucher:innen mehr Kontext darüber erhalten, wofür sie sich anmelden.

### Checkbox „Auswahl aufheben“ {#clear-selections-checkbox}

Aktivieren Sie die Einstellung **Checkbox „Auswahl aufheben“**, um dem Block eine zusätzliche Checkbox hinzuzufügen. Wenn Besucher:innen diese aktivieren, werden alle Abo-Gruppen-Checkboxen im Block abgewählt – nützlich, damit Besucher:innen sich vor dem Absenden des Formulars schnell von allem abmelden können.

### Checkbox „Alle abonnieren“ {#subscribe-to-all-checkbox}

Aktivieren Sie die Einstellung **Checkbox „Alle abonnieren“**, um dem Block eine zusätzliche Checkbox hinzuzufügen. Wenn Besucher:innen diese aktivieren, werden alle Abo-Gruppen-Checkboxen im Block ausgewählt – nützlich für ein schnelles Opt-in in alle aufgelisteten Gruppen.

## Bestehende Abos aktualisieren {#update-existing-subscriptions}

Damit bestehende Nutzer:innen ihre E-Mail-Abos überprüfen und aktualisieren können, teilen Sie die Landing-Page über ihren [Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) in einer E-Mail, einem Canvas-Schritt oder einer anderen Nachricht. Wenn Nutzer:innen die Seite über diesen Link öffnen, identifiziert Braze sie und füllt automatisch jede Abo-Gruppen-Checkbox im Block **Abos verwalten** mit ihrem aktuellen Abo-Status vor – ähnlich wie bei einem [E-Mail-Präferenzcenter]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

Nutzer:innen können Checkboxen aktivieren oder deaktivieren, um ihre Abos zu aktualisieren, und dann das Formular absenden, um ihre Änderungen zu speichern.

{% alert note %}
Das Vorbefüllen des aktuellen Abo-Status von Nutzer:innen im Block **Abos verwalten** ist standardmäßig enthalten und erfordert nicht die [Landing-Pages-Pro-Stufe]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Dies unterscheidet sich vom [Liquid-basierten Vorbefüllen]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields) für andere Formularfelder, das Landing-Pages Pro erfordert.
{% endalert %}

## Neue Abonnent:innen erfassen {#capture-new-subscribers}

Um neue Abonnent:innen zu gewinnen, z. B. auf einer Landing-Page zur Lead-Generierung, kombinieren Sie den Block **Abos verwalten** mit einem [E-Mail-Erfassungsblock]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages), damit die Seite die E-Mail-Adresse der Verbraucher:innen zusammen mit ihrer Abo-Gruppen-Auswahl erfasst.

Wenn Verbraucher:innen nicht identifiziert sind (z. B. wenn sie ohne einen Landing-Page-Liquid-Tag ankommen), sind die Checkboxen zunächst nicht aktiviert. Beim Absenden des Formulars werden sie für die von ihnen ausgewählten Abo-Gruppen abonniert.

## Wissenswertes {#things-to-know}

- **SMS-, RCS- und WhatsApp-Einwilligung:** Um auf einer Landing-Page die Einwilligung für diese Kanäle statt für E-Mail zu erfassen, verwenden Sie einen [Telefonnummern-Erfassungsblock]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
- **Bestätigungserlebnis:** Landing-Pages mit Formularblöcken, einschließlich **Abos verwalten**, benötigen nach dem Absenden ein Bestätigungserlebnis. [Erstellen Sie eine Bestätigungsseite]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) und verlinken Sie diese über Ihren **Absenden**-Button.
- **Referenz für Editor-Blöcke:** Eine vollständige Referenz aller Landing-Page-Blöcke und ihrer Eigenschaften finden Sie unter [Editor-Blöcke (Landing-Pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).