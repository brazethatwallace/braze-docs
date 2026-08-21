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

| Anforderungen | Beschreibung |
| --- | --- |
| E-Mail-Abo-Gruppen | Mindestens eine [E-Mail-Abo-Gruppe]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups), [über das Dashboard erstellt]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-subscription-group) oder über die [Abo-Gruppen-Endpunkte]({{site.baseurl}}/api/endpoints/subscription_groups). |
| Landing-Page-Berechtigungen | Dieselben [Berechtigungen]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites), die zum Erstellen und Bearbeiten jeder Landing-Page erforderlich sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Schritt 1: Den Block „Abos verwalten“ hinzufügen {#step-1-add-the-manage-subscriptions-block}

Gehen Sie im Drag-and-Drop-Landing-Page-Editor zum Abschnitt **Build** und wählen Sie **Form Blocks** aus. Ziehen Sie **Manage Subscriptions** in eine Zeile auf Ihrer Seite; der Block passt sich automatisch an die Spaltenbreite an.

Der Block ist leer, bis Sie ihm Abo-Gruppen hinzufügen.

## Schritt 2: Abo-Gruppen auswählen {#step-2-select-the-subscription-groups}

Wählen Sie den Block **Manage Subscriptions** aus und klicken Sie im rechten Panel **Block properties** auf **+ Add subscription groups**. Daraufhin wird eine Liste der in Ihrem Workspace verfügbaren [E-Mail-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups) angezeigt.

Aktivieren Sie das Kontrollkästchen neben jeder Abo-Gruppe, die Sie einbeziehen möchten, und bestätigen Sie Ihre Auswahl, um sie dem Block hinzuzufügen. Jede Abo-Gruppe wird auf der Landing-Page als eigenes auswählbares Kontrollkästchen angezeigt.

{% alert note %}
Der Block **Manage Subscriptions** listet nur Gruppen auf, die Sie explizit hinzufügen. Das Hinzufügen einer Abo-Gruppe zum Block abonniert Besucher:innen nicht automatisch – Besucher:innen müssen das Kontrollkästchen der Gruppe aktivieren und das Formular absenden.
{% endalert %}

## Schritt 3: Block-Einstellungen konfigurieren {#step-3-configure-the-block-settings}

Verwenden Sie das Panel **Block properties**, um das Verhalten und die Darstellung des Blocks anzupassen.

### Abo-Gruppen {#subscription-groups}

- **Gruppen neu anordnen:** Ziehen Sie eine Abo-Gruppe an ihrem Anfasser, um die Reihenfolge zu ändern, in der sie im Block angezeigt wird.
- **Gruppen hinzufügen oder entfernen:** Wählen Sie **+ Add subscription groups** aus, um weitere Gruppen hinzuzufügen, oder wählen Sie das Löschsymbol neben einer Gruppe aus, um sie aus dem Block zu entfernen.

### Beschreibungen einblenden {#include-descriptions}

Aktivieren Sie **Include descriptions**, um den Beschreibungstext jeder Abo-Gruppe neben ihrem Namen anzuzeigen. So erhalten Besucher:innen mehr Kontext darüber, wofür sie sich anmelden.

### „Subscribe to all“-Checkbox {#subscribe-to-all-checkbox}

Aktivieren Sie die Einstellung **„Subscribe to all“ checkbox**, um dem Block eine zusätzliche Checkbox hinzuzufügen. Wenn Besucher:innen diese auswählen, werden alle Abo-Gruppen-Checkboxen im Block aktiviert – praktisch für ein schnelles Opt-in in alle aufgeführten Gruppen.

## Bestehende Abos aktualisieren {#update-existing-subscriptions}

Um bestehenden Nutzer:innen die Möglichkeit zu geben, ihre E-Mail-Abos zu überprüfen und zu aktualisieren, teilen Sie die Landing-Page mithilfe ihres [Liquid-Tags]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) in einer E-Mail, einem Canvas-Schritt oder einer anderen Nachricht. Wenn Nutzer:innen die Seite über diesen Link öffnen, identifiziert Braze sie und füllt automatisch jedes Kontrollkästchen für Abo-Gruppen im Block **Manage Subscriptions** vor, um ihren aktuellen Abo-Status widerzuspiegeln – ähnlich wie bei einem [E-Mail-Präferenzcenter]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

Nutzer:innen können Kontrollkästchen aktivieren oder deaktivieren, um ihre Abos zu aktualisieren, und dann das Formular absenden, um ihre Änderungen zu speichern.

{% alert note %}
Das Vorausfüllen des aktuellen Abo-Status von Nutzer:innen im Block **Manage Subscriptions** ist standardmäßig enthalten und erfordert nicht die [Landing-Pages-Pro-Stufe]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Dies unterscheidet sich vom [Liquid-basierten Vorausfüllen]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields) für andere Formularfelder, das Landing-Pages Pro erfordert.
{% endalert %}

## Neue Abonnent:innen erfassen {#capture-new-subscribers}

Um neue Abonnent:innen zu erfassen, z. B. auf einer Landing-Page zur Lead-Generierung, kombinieren Sie den Block **Manage Subscriptions** mit einem [E-Mail-Erfassungsblock]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages), damit die Seite die E-Mail-Adresse der Verbraucher:innen zusammen mit deren Abo-Gruppen-Auswahl erfasst.

Wenn die Verbraucher:innen nicht identifiziert sind (z. B. wenn sie ohne einen Landing-Page-Liquid-Tag ankommen), sind die Kontrollkästchen zunächst nicht ausgewählt. Wenn sie das Formular absenden, werden sie für die Abo-Gruppen abonniert, die sie ausgewählt haben.

## Wissenswert {#things-to-know}

- **SMS-, RCS- und WhatsApp-Einwilligung:** Um die Einwilligung für diese Kanäle auf einer Landing-Page statt per E-Mail einzuholen, verwenden Sie einen [Phone-Capture-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
- **Bestätigungserlebnis:** Landing-Pages mit Formularblöcken, einschließlich **Abos verwalten**, benötigen nach dem Absenden ein Bestätigungserlebnis. [Erstellen Sie eine Bestätigungsseite]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) und verlinken Sie diese über Ihren **Absenden**-Button.
- **Editor-Block-Referenz:** Eine vollständige Referenz aller Landing-Page-Blöcke und ihrer Eigenschaften finden Sie unter [Editor-Blöcke (Landing-Pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).