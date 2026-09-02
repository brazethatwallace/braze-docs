---
nav_title: Redpoint
article_title: Redpoint
description: "Die Integration von Redpoint und Braze ermöglicht es Ihnen, Braze-Nutzerprofile mit Ihren First-Party-Daten zu onboarden und anzureichern."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint](https://www.redpointglobal.com) ist eine Technologieplattform, die Marketern eine vollständig integrierte Plattform für die Orchestrierung von Kampagnen bietet. Nutzen Sie die Segmentierungs-, Zeitplanungs- und Automatisierungsfunktionen von Redpoint, um zu steuern, wie und wann Customer Data Platform (CDP)-Daten in Braze importiert werden.

_Diese Integration wird von Redpoint gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Redpoint ermöglicht es Ihnen, Braze-Segmente auf der Grundlage Ihrer Redpoint-Customer Data Platform (CDP)-Daten zu erstellen. Redpoint bietet zwei Modi für die Übergabe von Daten an Braze:

1. **Braze Onboarding und Upsert**-Modus: Führt ein „Upsert“ eines Nutzerprofils von Redpoint in Braze durch. Dieser Modus ist für das Onboarding oder die Aktualisierung von Nutzerdatensätzen vorgesehen, wenn sich Daten geändert haben.
2. **Braze Append**-Modus: Aktualisiert ein Kundenprofil, wenn die Nutzer:in bereits in Braze existiert.

Sie konfigurieren eine Exportvorlage und einen ausgehenden Kanal für jeden Modus.

{% alert note %}
„Upsert“ ist eine Kombination aus den Wörtern „Update“ und „Insert“. Es wird verwendet, wenn Sie einen neuen Datensatz in eine Datenbanktabelle einfügen möchten, falls er noch nicht existiert, oder den Datensatz aktualisieren möchten, falls er bereits existiert. Im Wesentlichen prüft Upsert, ob ein bestimmter Datensatz in der Datenbank vorhanden ist. Wenn der Datensatz vorhanden ist, wird er aktualisiert, und wenn er nicht vorhanden ist, wird ein neuer Datensatz eingefügt.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Redpoint Data Management-Artefakte | Die Braze-Integration wird von einer Reihe von Redpoint Data Management-Artefakten unterstützt. Kontaktieren Sie den [Redpoint Support](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us), um die Artefakte für Ihre Version von Redpoint Data Management anzufordern. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Angepasste Attribute von Redpoint Customer Data Platform (CDP) {#redpoint-cdp-custom-attributes}

Die folgenden angepassten Attribute von Redpoint können einem Braze-Kundenprofil hinzugefügt werden.

| Feld               | Beschreibung                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Das Redpoint-Customer Data Platform (CDP)-Profilattribut-Objekt                                                                                  |
| `rpi_audience_outputs`| Array von Zielgruppen-Ausgabe-Tags, bei denen die Nutzer:in in einer Redpoint Outbound Delivery Braze-Kanalausführung angesprochen wird         |
| `rpi_offers`         | Array von Angebots-Tags, bei denen die Nutzer:in in einer Redpoint Outbound Delivery Braze-Kanalausführung angesprochen wird                   |
| `rpi_contact_ids`    | Array von Kontakt-IDs aus dem Angebotsverlauf, bei denen die Nutzer:in in einer Redpoint Outbound Delivery Braze-Kanalausführung angesprochen wird     |
| `rpi_channel_exec_ids`| Array von Kanalausführungs-IDs, bei denen die Nutzer:in in einer Redpoint Outbound Delivery Braze-Kanalausführung angesprochen wird       |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Angepasste Attribute von Redpoint Customer Data Platform (CDP)" }

![Tabelle der angepassten Attribute von Redpoint CDP mit den Feldern, die Braze-Nutzerprofilen hinzugefügt werden.]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## Integration

### Schritt 1: Templates einrichten {#step-1-set-up-templates}

#### Schritt 1a: Erstellen Sie das Braze Onboarding und Upsert Template {#step-1a-create-the-braze-onboarding-and-upsert-template}

Erstellen Sie in Redpoint Interaction (RPI) eine neue Exportvorlage und nennen Sie sie **Braze Onboarding and Upsert**. Diese Vorlage definiert die wichtigsten Abbildungen zwischen dem Redpoint Customer Data Platform (CDP) und dem Braze-Kundenprofil sowie alle zusätzlichen angepassten Attribute, die Sie Ihren Nutzerprofilen in Braze hinzufügen möchten.

Ziehen Sie Redpoint-Customer Data Platform (CDP)-Attribute in die Spalte **Attribute**. Setzen Sie jeden **Header Row Value** auf das entsprechende Braze-[Nutzerattribut]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields).

In der folgenden Tabelle sind die Customer Data Platform (CDP)-Attribute von Redpoint und die entsprechenden Braze-Attribute aufgeführt:

| Redpoint-Attribut | Header Row Value |
|--------------------|------------------|
| PID                | `external_id`    |
| First Name          | `first_name`     |
| Last Name          | `last_name`      |
| Primary Email      | `email`          |
| Primary Country    | `country`        |
| DOB                | `dob`            |
| Gender             | `gender`         |
| Primary City       | `home_city`      |
| Primary Phone      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 1a: Erstellen Sie das Braze Onboarding und Upsert Template" }

Fügen Sie das Attribut **Output Name** aus der Tabelle **Offer History** hinzu. Fügen Sie abschließend alle weiteren angepassten Redpoint-Attribute hinzu, die Sie in Braze zusammenführen möchten. Im Folgenden sehen Sie beispielsweise ein Onboarding- und Upsert-Template mit Bildung, Einkommen und Familienstand als zusätzliche Attribute.

![Redpoint Onboarding- und Upsert-Exportvorlage mit Attribut-zu-Header-Abbildungen.]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### Schritt 1b: Erstellen Sie das Braze Append Template {#step-1b-create-the-braze-append-template}

Erstellen Sie eine zweite Exportvorlage für reine Append-Operationen namens **Braze Append**.

Sie legen nur zwei Attribute für diese Vorlage fest. Setzen Sie für **PID** den **Header Row Value** auf `external_id`. Setzen Sie für **Output Name** die **Header Row** auf `output_name`.

![Eine Beispiel-Exportvorlage mit den Attributen „external_id“ und „output name“.]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### Schritt 1c: Datumsformat einstellen {#step-1c-set-date-format}

Navigieren Sie bei beiden Export-Templates zum Tab **Options** und setzen Sie das **Date Format** auf den Wert **Custom Format**. Legen Sie das Format als **yyyy-MM-dd** fest.

![Der Tab „Options“ mit dem Datumsformat „yyyy-MM-dd“.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### Schritt 2: Ausgehende Kanäle erstellen {#step-2-create-outbound-channels}

Erstellen Sie in RPI zwei neue Kanäle. Stellen Sie beide Kanäle auf **Outbound Delivery** ein. Nennen Sie einen Kanal **Braze Onboarding and Upsert** und den anderen **Braze Append**.

![Allgemeiner Tab der Redpoint Outbound Delivery-Kanalkonfiguration.]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Prüfen Sie nach dem anfänglichen Onboarding Ihrer Customer Data Platform (CDP)-Datensätze in Braze, ob nachfolgende Redpoint Interaction-Workflows, die den Braze Onboarding- und Upsert-Kanal verwenden, so konzipiert sind, dass sie nur Datensätze auswählen, die sich seit der anfänglichen Onboarding-Synchronisierung geändert haben.
{% endalert %}

### Schritt 3: Kanäle konfigurieren {#step-3-configure-the-channels}

#### Schritt 3a: Template und Exportpfadformat festlegen {#step-3a-set-template-and-export-path-format}

Navigieren Sie im Bildschirm **Configuration** der Kanäle zum Tab **General**. Legen Sie die Exportvorlage für den jeweiligen Kanal fest.

Definieren Sie als Nächstes auf beiden Kanälen ein **Export path format**, das auf ein gemeinsames Netzwerk, ein Dateiübertragungsprotokoll oder einen Speicherort eines externen Inhaltsanbieters verweist, der sowohl für Redpoint Interaction als auch für Redpoint Data Management zugänglich ist.

![Redpoint-Kanalkonfiguration mit den Feldern für Exportvorlage und Exportpfadformat.]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

Das Format des Exportverzeichnisses ist auf beiden Kanälen identisch und sollte mit `\\[Channel]\\[Offer]\\[Workflow ID]` enden.

![Redpoint-Exportverzeichnis-Pfadformat, das mit Kanal, Angebot und Workflow-ID endet.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### Schritt 3b: Post Execution konfigurieren {#step-3b-configure-post-execution}

Navigieren Sie im Bildschirm **Configuration** der Kanäle zum Tab **Post Execution**.

Aktivieren Sie das Kontrollkästchen **Post-execution**, um nach der Kanalausführung eine Dienst-URL aufzurufen. Geben Sie die URL Ihres Redpoint Data Management-Webdienstes ein. Dieser Eintrag ist sowohl auf Ihrem Onboarding- als auch auf Ihrem Append-Kanal identisch.

![Redpoint Post-Execution-Einstellungen mit konfigurierter Dienst-URL.]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### Schritt 4: Braze-Komponenten in Redpoint Data Management einrichten {#step-4-set-up-braze-components-in-redpoint-data-management}

Das Archiv mit den Redpoint Data Management (RPDM)-Artefakten zur Unterstützung der Braze-Integration enthält eine README mit detaillierten Anweisungen zur Einrichtung der erforderlichen Komponenten. Beachten Sie bei der Konfiguration Ihrer Integration die folgenden Details.

#### Schritt 4a: Aktualisieren Sie die RPI-to-Braze-Automatisierung mit Ihrem Braze REST-Endpunkt und dem Basis-RPI-Ausgabeverzeichnis {#step-4a-update-the-rpi-to-braze-automation-with-your-braze-rest-endpoint-and-base-rpi-output-directory}

Nachdem Sie die Braze-bezogenen Artefakte in Redpoint Data Management importiert haben, öffnen Sie die Automatisierung namens **AUTO_Process_RPI_to_Braze** und aktualisieren Sie die folgenden zwei Automatisierungsvariablen mit den Werten für Ihre Umgebung:

* **BRAZE_API_URL**: Der Braze REST-Endpunkt
* **BASE_OUTPUT_DIRECTORY**: Das gemeinsame Ausgabeverzeichnis von Redpoint Interaction und Redpoint Data Management

![Redpoint-Automatisierungsvariablen mit den Werten für BRAZE_API_URL und BASE_OUTPUT_DIRECTORY.]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### Schritt 4b: Aktualisieren Sie das RPI-to-Braze-Append-Projekt {#step-4b-update-the-rpi-to-braze-append-project}

Das Redpoint Data Management-Projekt namens **PROJ_RPI_to_Braze_Append** enthält das Schema der Exportdatei für die ausgehende Zustellung und die Abbildungen für das angepasste Attribut-Objekt `rpi_cdp_attributes` in Braze.

Aktualisieren Sie das Dateieingabeschema und das Document-Injector-Tool namens **RPI to Braze Document Injector** mit allen zusätzlichen angepassten Customer Data Platform (CDP)-Attributen, die in Ihrem Exportdatei-Template definiert sind. Dieses Beispiel zeigt die zusätzliche Abbildung von Bildung, Einkommen und Familienstand:

![Redpoint Document-Injector-Abbildungen für angepasste Braze-CDP-Attribute.]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## Verwendung der Integration {#using-the-integration}

Der Outbound Delivery Braze-Kanal kann jetzt innerhalb der Redpoint Interaction-Workflows genutzt werden. Befolgen Sie die Standardverfahren zum Erstellen von Auswahlregeln und Zielgruppen in RPI sowie zum Erstellen der zugehörigen Workflow-Zeitpläne und -Trigger.

Um die Synchronisierung einer RPI-Zielgruppen-Ausgabe mit Braze zu ermöglichen, erstellen Sie ein Outbound-Delivery-Angebot und verknüpfen es entweder mit dem **Braze Onboarding and Upsert**- oder dem **Braze Append**-Kanal. Dies hängt davon ab, ob die Absicht darin besteht, neue Datensätze in Braze zu erstellen oder zusammenzuführen, oder ob nur Kampagnendaten angehängt werden sollen, wenn der Datensatz bereits in Braze vorhanden ist.

![Redpoint Interaction Canvas-Workflow mit dem Braze Outbound Delivery-Kanal.]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

Sobald der Workflow in RPI erfolgreich ausgeführt wurde, können die Orchestrierungs- und Customer Data Platform (CDP)-Daten aus RPI zur Erstellung von Segmenten in Braze verwendet werden.

![Braze Segment Builder mit von Redpoint synchronisierten Zielgruppendaten.]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Sie können die mit Redpoint verknüpften Eigenschaften im Kundenprofil einsehen.

![Braze-Nutzerprofil mit den von Redpoint verknüpften angepassten Eigenschaften.]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}