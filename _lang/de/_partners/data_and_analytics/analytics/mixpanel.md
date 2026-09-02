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
| Mixpanel-Konto | Ein [Mixpanel-Konto](https://mixpanel.com/) ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Currents | Um Daten zurück nach Mixpanel zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration des Datenexports {#data-export-integration}

Eine vollständige Liste der Events, die von Braze nach Mixpanel exportiert werden können, finden Sie in diesem Abschnitt. Alle an Mixpanel gesendeten Events enthalten die `external_user_id` der Nutzer:innen als Mixpanel Distinct ID. Derzeit sendet Braze keine Event-Daten für Nutzer:innen, deren `external_user_id` nicht festgelegt ist.

Sie können zwei Arten von Events nach Mixpanel exportieren: [Nachrichteninteraktions-Events](#supported-currents-events), die sich auf die Braze-Events beziehen, die direkt mit dem Nachrichtenversand zusammenhängen, und [Kundenverhalten-Events](#supported-currents-events), die andere App- oder Website-Aktivitäten wie Sitzungen, angepasste Events und über die Plattform erfasste Käufe umfassen. Alle angepassten Events erhalten das Präfix `[Braze Custom Event]`. Angepasste Event-Eigenschaften und Kauf-Event-Eigenschaften erhalten die Präfixe `[Custom event property]` bzw. `[Purchase property]`.

Wenden Sie sich an Ihren Account Manager:in oder eröffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support), wenn Sie Zugang zu zusätzlichen Event-Berechtigungen benötigen.

### Schritt 1: Mixpanel-Zugangsdaten abrufen {#step-1-get-mixpanel-credentials}

Klicken Sie in Ihrem Mixpanel-Dashboard unter einem neuen oder bestehenden Projekt auf **Project Settings**. Dort finden Sie das Mixpanel-API-Secret und das Mixpanel-Token / Textbaustein. Diese Zugangsdaten werden im nächsten Schritt zum Erstellen Ihrer Currents-Verbindung verwendet.

### Schritt 2: Braze-Current erstellen {#step-2-create-braze-current}

1. Gehen Sie in Braze zu **Currents** > **+ Create Current** > **Create Mixpanel Export**.
2. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail, das Mixpanel-API-Secret und das Mixpanel-Token / Textbaustein in die entsprechenden Felder ein.
3. Wählen Sie die Events aus, die Sie verfolgen möchten; eine Liste der verfügbaren Events wird bereitgestellt.
4. Wählen Sie **Launch Current**.

![Die Braze-Mixpanel-Currents-Seite. Diese Seite enthält Felder für den Integrationsnamen, die Kontakt-E-Mail, das API-Secret und das Mixpanel-Export-Token / Textbaustein. Die untere Hälfte der Currents-Seite zeigt die verfügbaren Currents-Events, die Sie senden können.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Weitere Informationen finden Sie in der [Integrationsdokumentation](https://help.mixpanel.com/hc/en-us/articles/360001243663) von Mixpanel.
{% endtab %}

## Unterstützte Currents-Events {#supported-currents-events}

Braze unterstützt den Export der folgenden Events nach Mixpanel:

- [Nachricht-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)
- [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)

Für die Payload-Struktur jedes Events wählen Sie den Tab **Mixpanel** im [Glossar der Nachricht-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und im [Glossar der Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) aus.

## Fehlerbehebung {#troubleshooting}

### Mixpanel-API-Schlüssel und externe Braze-ID überprüfen {#verify-mixpanel-api-key-and-braze-external-id}

Vergewissern Sie sich, dass Ihr Mixpanel-API-Schlüssel und die `braze_external_id`-Werte in Braze und Mixpanel übereinstimmen. Die Kohortensynchronisierungs-API teilt Nutzer:innengruppen zwischen den Produkten, und die Synchronisierung funktioniert nicht korrekt, wenn die `external_id` in Braze und der von Mixpanel gesendete Bezeichner nicht übereinstimmen. Kohortensynchronisierungen von Mixpanel laufen nach dem Zeitplan von Mixpanel – zum Beispiel einmal oder etwa alle zwei Stunden – planen Sie daher zwischen den Überprüfungen ausreichend Zeit ein.

### Implementierungsstatus prüfen {#check-implementation-status}

Bestätigen Sie, dass `braze_external_id` in Mixpanel implementiert ist.

### Nutzer:inneneigenschaft direkt festlegen {#set-the-user-property-directly}

Um Mehrdeutigkeiten zu vermeiden, setzen Sie `braze_external_id` direkt in Mixpanel.

### Automatische Eigenschaftszuweisung (SDKs) {#automatic-property-setting-sdks}

Das Mixpanel-SDK kann `braze_external_id` automatisch setzen, wenn das Braze-SDK in derselben App integriert ist. Wenn Sie sowohl Mixpanel als auch Braze gemeinsam implementieren, ist in der Regel keine zusätzliche Konfiguration über die Installation beider SDKs hinaus erforderlich.

{% alert note %}
`braze_external_id` wird nicht gesetzt, wenn `changeUser()` in Braze aufgerufen wird; es wird gesetzt, wenn Mixpanel initialisiert oder eine Sitzung startet (während „init“ oder „start session“).
{% endalert %}