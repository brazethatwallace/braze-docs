---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Mixpanel, einer Business-Analytics-Plattform, die es Ihnen erlaubt, Mixpanel-Kohorten in Braze zu importieren, um Braze-Segmente zu erstellen, die für das Targeting von Nutzer:innen in zukünftigen Braze-Campaigns oder Canvases verwendet werden können."
page_type: partner
search_tag: Partner
tool: Currents

---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecommixpanel-integration-with-braze339085scorm2u7y2e6qrldh2-stylefloatrightwidth120pxborder0-classnoimgbordermixpanel}

> [Mixpanel](https://mixpanel.com/) ist eine Business-Analytics-Plattform, die es Ihnen erlaubt, Events aus Mixpanel in andere Plattformen zu exportieren, um tiefere Analysen durchzuführen. Die gesammelten Daten können dann dazu verwendet werden, angepasste Berichte zu erstellen und das Engagement und die Bindung der Nutzer:innen zu messen.

Die Integration von Braze und Mixpanel erlaubt es Ihnen, [Mixpanel-Kohorten in Braze zu importieren]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import), um Braze-Segmente zu erstellen, die für das Targeting von Nutzer:innen in zukünftigen Braze-Campaigns oder Canvases verwendet werden können. Die Kohortensynchronisierung aktualisiert die Kohortenmitgliedschaft in Braze und importiert keine Mixpanel-Events oder Nutzer:innen-Eigenschaften. Weitere Informationen finden Sie unter [Mixpanel-Kohortenimport]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import#data-import-integration).

Sie können Braze-Currents auch nutzen, um [Ihre Braze-Events nach Mixpanel zu exportieren](#data-export-integration) und so tiefere Analytics zu Conversions, Bindung und Produktnutzung zu erhalten.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Mixpanel-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Mixpanel-Konto](https://mixpanel.com/). |
| Currents | Um Daten zurück in Mixpanel zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Datenexport-Integration {#data-export-integration}

Eine vollständige Liste der Events, die von Braze nach Mixpanel exportiert werden können, finden Sie in diesem Abschnitt. Alle Events, die an Mixpanel gesendet werden, enthalten die `external_user_id` der Nutzer:innen als Mixpanel Distinct ID. Derzeit sendet Braze keine Event-Daten für Nutzer:innen, deren `external_user_id` nicht gesetzt ist.

Sie können zwei Arten von Events nach Mixpanel exportieren: [Nachrichten-Engagement-Events](#supported-currents-events), bestehend aus den Braze-Events, die direkt mit dem Versand von Nachrichten zusammenhängen, und [Kundenverhalten-Events](#supported-currents-events), einschließlich anderer App- oder Website-Aktivitäten wie Sitzungen, angepasste Events und Käufe, die über die Plattform getrackt werden. Allen angepassten Events ist das Präfix `[Braze Custom Event]` vorangestellt. Angepassten Event-Eigenschaften und Kauf-Event-Eigenschaften wird das Präfix `[Custom event property]` bzw. `[Purchase property]` vorangestellt.

Wenden Sie sich an Ihren Account Manager oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen.

### Schritt 1: Zugangsdaten für Mixpanel abrufen {#step-1-get-mixpanel-credentials}

Klicken Sie in Ihrem Mixpanel-Dashboard in einem neuen oder bestehenden Projekt auf die **Project Settings**. Hier finden Sie das Mixpanel-API-Secret und das Mixpanel-Token. Diese Zugangsdaten werden im nächsten Schritt verwendet, um Ihre Currents-Verbindung herzustellen.

### Schritt 2: Braze-Currents erstellen {#step-2-create-braze-current}

1. Navigieren Sie in Braze zu **Currents** > **+ Create Current** > **Create Mixpanel Export**.
2. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail, das Mixpanel-API-Secret und das Mixpanel-Token in den aufgeführten Feldern an.
3. Wählen Sie die Events aus, die Sie tracken möchten; eine Liste der verfügbaren Events wird angezeigt.
4. Klicken Sie auf **Launch Current**.

![Die Braze Mixpanel Currents-Seite. Diese Seite enthält Felder für den Integrationsnamen, die Kontakt-E-Mail, das API-Secret und das Mixpanel-Export-Token. In der unteren Hälfte der Currents-Seite finden Sie eine Liste der verfügbaren Currents-Events, die Sie senden können.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Lesen Sie die [Integrationsdokumentation](https://help.mixpanel.com/hc/en-us/articles/360001243663) von Mixpanel, um mehr zu erfahren.
{% endtab %}

## Unterstützte Currents-Events {#supported-currents-events}

Braze unterstützt den Export der folgenden Events nach Mixpanel:

- [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Informationen zur Payload-Struktur der einzelnen Events finden Sie auf dem Tab **Mixpanel** im [Glossar der Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und im [Glossar der Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).

## Fehlerbehebung {#troubleshooting}

### Mixpanel-API-Schlüssel und externe Braze-ID überprüfen {#verify-mixpanel-api-key-and-braze-external-id}

Stellen Sie sicher, dass Ihr Mixpanel-API-Schlüssel und die `braze_external_id`-Werte in Braze und Mixpanel übereinstimmen. Die Kohorten-Sync-API teilt Nutzer:innen-Gruppen zwischen den Produkten, und der Sync funktioniert nicht korrekt, wenn die `external_id` in Braze und der von Mixpanel gesendete Bezeichner nicht übereinstimmen. Kohorten-Syncs von Mixpanel laufen nach dem Zeitplan von Mixpanel – zum Beispiel einmal oder ungefähr alle zwei Stunden – lassen Sie daher zwischen den Überprüfungen etwas Zeit.

### Implementierungsstatus prüfen {#check-implementation-status}

Stellen Sie sicher, dass `braze_external_id` in Mixpanel implementiert ist.

### Nutzer:innen-Eigenschaft direkt setzen {#set-the-user-property-directly}

Um Mehrdeutigkeiten zu vermeiden, setzen Sie `braze_external_id` direkt in Mixpanel.

### Automatisches Setzen der Eigenschaft (SDKs) {#automatic-property-setting-sdks}

Das Mixpanel SDK kann `braze_external_id` automatisch setzen, wenn das Braze SDK in derselben Anwendung integriert ist. Wenn Sie sowohl Mixpanel als auch Braze gemeinsam implementieren, benötigen Sie in der Regel keine zusätzliche Konfiguration über die Installation beider SDKs hinaus.

{% alert note %}
`braze_external_id` wird nicht gesetzt, wenn `changeUser()` in Braze aufgerufen wird; es wird gesetzt, wenn Mixpanel initialisiert oder eine Sitzung startet (während „init“ oder „start session“).
{% endalert %}