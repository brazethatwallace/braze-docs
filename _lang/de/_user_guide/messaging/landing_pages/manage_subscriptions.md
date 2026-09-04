---
nav_title: Block „Abos verwalten“
article_title: Block „Abos verwalten“
description: "Dieser Artikel beschreibt, wie Sie den Formularblock „Abos verwalten“ auf einer Braze Landing-Page hinzufügen und konfigurieren, damit Verbraucher:innen sich für ihre E-Mail-, SMS- oder WhatsApp-Abo-Gruppen anmelden und diese verwalten können."
page_order: 5
---

# Block „Abos verwalten“ {#manage-subscriptions-block}

> Fügen Sie einer Landing-Page einen Block **Abos verwalten** hinzu, damit Nutzer:innen ihre E-Mail-, SMS- oder WhatsApp-Abo-Gruppen einsehen, sich dafür anmelden und sie aktualisieren können.

Der Block **Abos verwalten** unterstützt zwei zentrale Anwendungsfälle:

- **[Bestehende Abos verwalten](#update-existing-subscriptions):** Teilen Sie den [Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) der Landing-Page in einer E-Mail-, SMS-, WhatsApp- oder einer anderen Kanalnachricht. Wenn identifizierte Nutzer:innen die Seite öffnen, füllt der Block automatisch die Checkbox jeder Abo-Gruppe mit dem aktuellen Abo-Status vor, sodass sie ihre Einstellungen überprüfen und aktualisieren können.
- **[Neue Opt-ins erfassen](#capture-new-subscribers):** Fügen Sie den Block zusammen mit einem **E-Mail-Erfassungs**- oder **Telefonnummern-Erfassungs**-Block zu einer Landing-Page für die Lead-Generierung hinzu, damit neue Besucher:innen beim Absenden des Formulars auswählen können, welchen Abo-Gruppen sie beitreten möchten.

{% alert important %}
Jeder Block **Abos verwalten** ist für einen Kanal bestimmt: [E-Mail]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) oder [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states). Um mehr als einen Kanal abzudecken, fügen Sie jeweils einen Block pro Kanal hinzu. Für die RCS-Einwilligung verwenden Sie stattdessen einen Block [Telefonnummern-Erfassung]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| E-Mail-, SMS- oder WhatsApp-Abo-Gruppen | Mindestens eine [E-Mail-Abo-Gruppe]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups), [SMS-Abo-Gruppe]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) oder [WhatsApp-Abo-Gruppe]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states) für den Kanal, den Sie zum Block hinzufügen. Erstellen Sie E-Mail-Gruppen über das Dashboard oder die [Abo-Gruppen-Endpunkte]({{site.baseurl}}/api/endpoints/subscription_groups). SMS-Gruppen werden während der [SMS-Einrichtung]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#enable-subscription-groups) bereitgestellt. WhatsApp-Gruppen werden erstellt, wenn Sie [WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup) in Ihren Workspace integrieren. |
| Landing-Page-Berechtigungen | Dieselben [Berechtigungen]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites), die zum Erstellen und Bearbeiten einer Landing-Page erforderlich sind. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Schritt 1: Den Block „Abos verwalten“ hinzufügen {#step-1-add-the-manage-subscriptions-block}

Gehen Sie im Drag-and-Drop-Landing-Page-Editor zum Abschnitt **Build** und wählen Sie **Form Blocks** aus. Ziehen Sie **Manage Subscriptions** in eine Zeile auf Ihrer Seite; der Block passt sich automatisch an die Spaltenbreite an.

Der Block ist leer, bis Sie Abo-Gruppen hinzufügen. Um Gruppen für mehr als einen Kanal anzuzeigen, fügen Sie für jeden Kanal einen Block **Manage Subscriptions** hinzu.

## Schritt 2: Kanal und Abo-Gruppen auswählen {#step-2-select-the-channel-and-subscription-groups}

Wählen Sie bei ausgewähltem Block **Manage Subscriptions** im rechten Panel **Block properties** die Option **+ Add subscription groups** aus. Das Modal **Add subscription groups** wird geöffnet.

1. Wählen Sie unter **Select channel** entweder **Email**, **SMS** oder **WhatsApp** aus. Jeder Block unterstützt einen Kanal. Wenn ein Kanal bereits einen **Manage Subscriptions**-Block auf der Seite hat, ist die entsprechende Kanalkarte deaktiviert und mit **Added** gekennzeichnet.
2. Wählen Sie unter **Select subscription groups** die Gruppen aus, die einbezogen werden sollen. Die Listenüberschrift entspricht dem Kanal (**Email subscription groups**, **SMS subscription groups** oder **WhatsApp subscription groups**).
3. Wählen Sie **Add selected** aus.

Jede Abo-Gruppe wird als eigene auswählbare Checkbox auf der Landing-Page angezeigt.

Wenn Sie **SMS** auswählen und Ihr Workspace noch keine SMS-Abo-Gruppen hat, zeigt das Modal **No SMS subscription groups yet** an. Schließen Sie die [Einrichtung von SMS-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states) ab und kehren Sie dann zum Block zurück.

Wenn Sie **WhatsApp** auswählen und Ihr Workspace noch keine WhatsApp-Abo-Gruppen hat, zeigt das Modal **No WhatsApp subscription groups yet** an. Schließen Sie die [Einrichtung von WhatsApp-Abo-Gruppen]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states) ab und kehren Sie dann zum Block zurück.

{% alert note %}
Der Block **Manage Subscriptions** listet nur Gruppen auf, die Sie explizit hinzufügen. Das Hinzufügen einer Abo-Gruppe zum Block abonniert Besucher:innen nicht automatisch – Besucher:innen müssen die Checkbox der Gruppe auswählen und das Formular absenden.
{% endalert %}

## Schritt 3: Blockeinstellungen konfigurieren {#step-3-configure-the-block-settings}

Verwenden Sie das Panel **Block properties**, um das Verhalten und die Darstellung des Blocks anzupassen.

### Abo-Gruppen {#subscription-groups}

- **Gruppen neu anordnen:** Ziehen Sie eine Abo-Gruppe an ihrem Griff, um die Reihenfolge zu ändern, in der sie im Block angezeigt wird.
- **Gruppen hinzufügen oder entfernen:** Wählen Sie **+ Add subscription groups** aus, um weitere Gruppen hinzuzufügen, oder wählen Sie das Löschsymbol neben einer Gruppe aus, um sie aus dem Block zu entfernen.

### Beschreibungen einbeziehen {#include-descriptions}

Aktivieren Sie **Include descriptions**, um den Beschreibungstext jeder Abo-Gruppe neben ihrem Namen anzuzeigen. So erhalten Besucher:innen mehr Kontext darüber, wofür sie sich anmelden. E-Mail-Gruppen können eine Beschreibung im Abo-Management enthalten. SMS- und WhatsApp-Gruppen in diesem Block zeigen keinen Beschreibungstext an.

### Checkbox „Alle abonnieren“ {#subscribe-to-all-checkbox}

Aktivieren Sie die Einstellung **"Subscribe to all" checkbox**, um dem Block eine zusätzliche Checkbox hinzuzufügen. Wenn Besucher:innen diese auswählen, werden alle Abo-Gruppen-Checkboxen im Block ausgewählt – praktisch für ein schnelles Opt-in in alle aufgelisteten Gruppen.

## Bestehende Abos aktualisieren {#update-existing-subscriptions}

Damit bestehende Nutzer:innen ihre E-Mail-, SMS- oder WhatsApp-Abos überprüfen und aktualisieren können, teilen Sie die Landing-Page über ihren [Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users) in einer E-Mail, SMS, WhatsApp-Nachricht, einem Canvas-Schritt oder einer anderen Nachricht. Wenn Nutzer:innen die Seite über diesen Link öffnen, identifiziert Braze sie und füllt automatisch jedes Kontrollkästchen der Abo-Gruppe im Block **Manage Subscriptions** entsprechend ihrem aktuellen Abo-Status vor – ähnlich wie bei einem [E-Mail-Präferenzcenter]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center).

Die Nutzer:innen können Kontrollkästchen aktivieren oder deaktivieren, um ihre Abos zu aktualisieren, und anschließend das Formular absenden, um ihre Änderungen zu speichern.

{% alert note %}
Das Vorbefüllen des aktuellen Abo-Status von Nutzer:innen im Block **Manage Subscriptions** ist standardmäßig enthalten und erfordert nicht die [Landing Pages Pro-Stufe]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers). Dies unterscheidet sich vom [Liquid-basierten Vorbefüllen]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields) für andere Formularfelder, wofür Landing Pages Pro erforderlich ist.
{% endalert %}

## Neue Abonnent:innen erfassen {#capture-new-subscribers}

Um neue Abonnent:innen zu erfassen, kombinieren Sie den Block **Manage Subscriptions** mit einem Erfassungsfeld für den jeweiligen Kanal:

- **E-Mail:** Fügen Sie einen [Email Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)-Block hinzu, damit die Seite die E-Mail-Adresse der Besucher:innen zusammen mit deren Auswahl der E-Mail-Abo-Gruppen erfasst.
- **SMS oder WhatsApp:** Fügen Sie einen [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)-Block hinzu, damit die Seite die Telefonnummer der Besucher:innen zusammen mit deren Auswahl der SMS- oder WhatsApp-Abo-Gruppen erfasst.

Wenn die Besucher:innen nicht identifiziert sind (zum Beispiel, wenn sie ohne einen Landing-Page-Liquid-Tag ankommen), sind die Kontrollkästchen zunächst nicht ausgewählt. Wenn sie das Formular absenden, werden sie bei den Abo-Gruppen angemeldet, die sie ausgewählt haben.

## Wissenswertes {#things-to-know}

- **Ein Kanal pro Block:** Sie können pro Kanal einen **Manage Subscriptions**-Block auf einer Seite hinzufügen (einen für E-Mail, einen für SMS und einen für WhatsApp).
- **RCS:** Dieser Block listet keine RCS-Abo-Gruppen auf. Um die Einwilligung für RCS einzuholen, verwenden Sie einen [Phone Capture]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)-Block.
- **Bestätigungserlebnis:** Landing-Pages mit Formularblöcken, einschließlich **Manage Subscriptions**, benötigen nach dem Absenden ein Bestätigungserlebnis. [Erstellen Sie eine Bestätigungsseite]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional) und verlinken Sie diese über Ihren **Submit**-Button.
- **Editor-Block-Referenz:** Eine vollständige Referenz aller Landing-Page-Blöcke und ihrer Eigenschaften finden Sie unter [Editor-Blöcke (Landing-Pages)]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages).