---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Optimizely, die es Ihnen ermöglicht, Ihre Braze-Kundensegmente, -Ereignisse und Currents-Ereignisse mit der Optimizely Data Platform zu synchronisieren."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) ist eine führende Plattform für digitale Erlebnisse, die Experimentier- und Content-Management-Tools für digitale Produkte und Marketingkampagnen anbietet.

Die Integration von Braze und Optimizely ist eine bidirektionale Integration, die es Ihnen ermöglicht:

{% multi_lang_include partners/ab_testing/optimizely_integration_bullets.md %}

## Voraussetzungen {#prerequisites}

| Anforderung                     | Beschreibung |
|----------------------------------|-------------|
| Optimizely Data Platform-Konto | Ein Optimizely Data Platform (ODP)-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Braze-REST-API-Schlüssel               | Ein Braze-REST-API-Schlüssel mit den folgenden Berechtigungen: `users.track`, `users.export.segments`, `segments.list`, `campaigns.trigger.send` und `canvas.trigger.send`. |
| Currents                         | Um Daten zurück nach Optimizely zu exportieren, müssen Braze-Currents für Ihr Konto eingerichtet sein. |
| Optimizely-URL und -Token / Textbaustein         | Diese können Sie abrufen, indem Sie zu Ihrem Optimizely-Dashboard navigieren und die Ingestion-URL und das Token / Textbaustein kopieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Integration konfigurieren {#step-1-configure-the-integration}

1. Wählen Sie im **App Directory** der Optimizely Data Platform (ODP) die App **Braze** aus und wählen Sie dann **Install App**.
2. Gehen Sie zum Tab **Settings**. Führen Sie im Abschnitt **Authorization** die folgenden Schritte aus:
    1. Geben Sie den Braze-**REST-API-Schlüssel** ein.
    2. Wählen Sie Ihre Braze-**Instanz-URL** aus.
    2. Wählen Sie **Verify API Key**.
3. Gehen Sie in Braze zu **[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents)**.
4. Wählen Sie **Create New Current** > **Custom Currents Export**.
5. Konfigurieren Sie den Current mit dem Endpunkt und dem Token / Textbaustein, die in ODP bereitgestellt werden. Dies ist erforderlich, um Braze-Ereignisse mit ODP zu synchronisieren.

![Optimizely-Autorisierung.]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6. Erweitern Sie in ODP den Abschnitt **Segments** und wählen Sie bestimmte Segmente aus der Liste **Segments to Sync** aus, oder wählen Sie **Import All Customers**, um alle Segmente zu synchronisieren.
7. Fügen Sie alle gewünschten [zusätzlichen Feldzuordnungen](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) zwischen Braze und ODP hinzu.
8. Wählen Sie **Save**.

![Optimizely-Braze-Segment-Synchronisierung.]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Sie müssen Segmente auswählen, um Braze-Kundenprofile zu importieren. Wenn Sie keine Segmente auswählen, importiert die Integration keine Kundenprofile.
{% endalert %}

### 2. Schritt: Datenfelder zuordnen {#step-2-map-data-fields}

Die Integration verfügt über Standard-Datenfeldzuordnungen zwischen Braze und ODP. Zum Beispiel wird das Feld **Email** in Braze dem Feld **Last Seen Email** in ODP zugeordnet.

![Optimizely- und Braze-Segment-Feldzuordnungen.]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### Zusätzliche Felder zuordnen (optional) {#map-additional-fields-optional}

Wenn es in Braze zusätzliche Datenfelder gibt, die Sie ODP zuordnen möchten, gehen Sie in ODP wie folgt vor:

1. Wählen Sie im Abschnitt **Segments** der App das Braze-Feld aus der Dropdown-Liste **Braze User Data Fields** aus.
2. Wählen Sie das ODP-Feld aus der Dropdown-Liste **ODP Customer Fields** aus.
3. Wählen Sie **Save Field Map**.

![Optimizely-Braze-Segment-Feldzuordnungen speichern]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### Nicht benötigte Feldzuordnungen löschen (optional) {#delete-non-required-field-mappings-optional}

Sie können auch alle Datenfeldzuordnungen löschen, die nicht benötigt werden. Gehen Sie in ODP wie folgt vor:

1. Wählen Sie im Abschnitt **Segments** der App die Feldzuordnung, die Sie löschen möchten, aus der Dropdown-Liste **Field Map** aus.
2. Wählen Sie **Delete Field Map**.

![Optimizely-Braze-Segment-Feldzuordnungen löschen]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### 3. Schritt: Daten von der Optimizely Data Platform (ODP) mit Braze synchronisieren {#step-3-sync-data-from-optimizely-data-platform-odp-to-braze}

Nachdem Sie die Integration konfiguriert haben, können Sie eine Aktivierung in ODP einrichten, um Ihre ODP-Kundendaten mit Braze zu synchronisieren.

1. Gehen Sie zu **Activation** > **Engage** und wählen Sie **Create New Campaign**.
2. Wählen Sie **Behavioral**, um eine automatisierte, wiederkehrende Synchronisierung einzurichten.
3. Wählen Sie **Create From Scratch** und geben Sie dann einen Namen für Ihre Aktivierung ein, der die Daten repräsentiert, die Sie mit Braze synchronisieren (z. B. **Braze Data Sync**).
4. Im Abschnitt **Enrollment** können Sie Daten für Kund:innen synchronisieren, die einem Segment entsprechen, oder Daten für Kund:innen synchronisieren, die ein Ereignis triggern (z. B. wenn ODP registriert, dass ein:e Kund:in eine E-Mail öffnet):
   - **Kund:innen, die einem Segment entsprechen:** Wählen Sie das gewünschte Segment aus und wählen Sie dann **Next**.<br><br>![Optimizely – Segment auswählen]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **Kund:innen, die ein Ereignis triggern:** Erweitern Sie die Dropdown-Liste **Filter** und wählen Sie das ODP-Ereignis aus, das als Auslöser für diese Datensynchronisierung mit Braze dienen soll. Erweitern Sie dann die **Automation Rules** und passen Sie sie wie gewünscht an. <br><br>![Optimizely – Trigger-Ereignis]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. Erweitern Sie **Touchpoints**, wählen Sie **Touchpoint 1** zur Bearbeitung aus und wählen Sie dann **Braze**.
6. Erweitern Sie den Abschnitt **Targeting** und wählen Sie dann den **Target Identifier** aus.
7. Wählen Sie eine der folgenden Optionen für **Add Users To** im Abschnitt **Configure** aus:
    - **Campaign:** Fügen Sie Kund:innen einer bestimmten Campaign in Braze hinzu. Nachdem Sie diese Option gewählt haben, müssen Sie die Braze-Campaign auswählen.
    - **Canvas:** Fügen Sie Kund:innen einem bestimmten Canvas in Braze hinzu. Nachdem Sie diese Option gewählt haben, müssen Sie das Braze-Canvas auswählen.
    - **Profile Update Only:** Aktualisieren Sie nur das Braze-Kundenprofil.
8. (Optional) Wählen Sie die **Number of Additional Fields** aus, die Sie mit Braze synchronisieren möchten (bis zu 20).
    Wählen Sie dann für die Dropdown-Liste und das Eingabefeld jedes zusätzlichen Feldes Folgendes aus:
    - Wählen Sie in jeder Dropdown-Liste **Field #** das Braze-Feld aus, das Sie befüllen möchten.
    - Geben Sie in jedes entsprechende **Field # Value** das ODP-Feld ein, das Sie an das ausgewählte Braze-Feld senden möchten. Wenn Sie z. B. **Company Name** aus der Dropdown-Liste **Field #** ausgewählt haben, geben Sie `{{customer.company_name}}` für den entsprechenden **Field # Value** ein.
9. Wählen Sie **Save** und wählen Sie dann Ihren Aktivierungsnamen im Breadcrumb-Pfad aus.
10. Wählen Sie **Select start time and schedule** im Abschnitt **Touchpoints** aus, wenn Sie für die Registrierung **Customers that match a segment** ausgewählt haben.
11. Nehmen Sie die folgenden Einstellungen vor:
    - **Recurring or Continuous:** Wählen Sie **Recurring**.
    - **Start Date:** Geben Sie das Datum ein, an dem Sie die Daten an Braze senden möchten.
    - **End:** Standardmäßig ist **Never** eingestellt. Wenn Sie die Braze-Datensynchronisierung an einem bestimmten Datum beenden möchten, legen Sie dies hier fest.
    - **Repeats:** Stellen Sie auf **Daily**.
    - **Repeat Every:** Setzen Sie auf **1 day**.
    - **Timing:** Geben Sie den Zeitpunkt ein, zu dem Sie die Daten an Braze senden möchten.
    - **Time Zone:** Wählen Sie die Zeitzone aus, in der Sie diese Daten senden möchten.
12. Wählen Sie **Apply**, **Save** und dann **Go Live**. Ihre Synchronisierung beginnt zum festgelegten Startdatum und -zeitpunkt (oder wenn das triggernde Ereignis eintritt).

## Fehlerbehebung {#troubleshooting}

### Ereignisse überprüfen {#inspect-events}

Um zu überprüfen, ob Daten ordnungsgemäß von ODP zu Braze synchronisiert werden, können Sie Ereignisse in ODP inspizieren.

1. Gehen Sie in ODP zu **Account Settings** > **Event Inspector**.
2. Wählen Sie **Start Inspector** aus.
3. Wenn Daten im Inspector verfügbar sind, wird neben **Refresh** eine Zahl angezeigt. Wählen Sie diese aus, um die Daten anzuzeigen.
4. Die Rohdaten, die ODP und Braze hin und her senden, werden angezeigt. Wählen Sie **View Details** aus, um die formatierte Version dieser Rohdaten zu sehen.
5. Datenfelder, die von Braze zurück an ODP gesendet werden, beginnen mit `_braze`.

### Aktivitätsprotokolle überprüfen {#check-activity-logs}

Jede Datensynchronisierung wird auch im [ODP-Aktivitätsprotokoll](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP) protokolliert:

1. Gehen Sie zu **Account Settings** > **Activity Log**.
2. Filtern Sie die Kategorien nach **braze**.
3. Wählen Sie **View Details** aus, um eine formatierte Ansicht der Protokolldetails einschließlich der Anzahl der Übereinstimmungen zu sehen.