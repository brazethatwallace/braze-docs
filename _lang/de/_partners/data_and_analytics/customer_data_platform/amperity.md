---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Amperity, einer umfassenden Customer Data Platform für Unternehmen, mit der Sie Amperity-Nutzer:innen synchronisieren, Daten vereinheitlichen, Daten über AWS S3-Buckets an Braze senden und vieles mehr können."
page_type: partner
search_tag: Partner

---

# Amperity

> [Amperity](https://amperity.com/) ist eine umfassende Customer Data Platform (CDP) für Unternehmen, die Marken dabei hilft, ihre Kund:innen kennenzulernen, strategische Entscheidungen zu treffen und konsequent die richtigen Maßnahmen zu ergreifen, um ihre Verbraucher:innen besser zu bedienen. Amperity bietet intelligente Funktionen für die Vereinheitlichung der Datenverwaltung, Analytics, Insights und Aktivierung.

_Diese Integration wird von Amperity gepflegt._

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

Die Integration von Braze und Amperity bietet eine einheitliche Sicht auf Ihre Kund:innen auf beiden Plattformen. Diese Integration ermöglicht es Ihnen:
- **Kundenprofile synchronisieren**: Bilden Sie Nutzerdaten und angepasste Attribute von Amperity auf Braze ab.
- **Zielgruppen erstellen und versenden**: Erstellen Sie Segmente, die Listen aktiver Kund:innen und die dazugehörigen angepassten Attribute zurückgeben, und senden Sie diese an Braze.
- **Daten-Updates verwalten**: Steuern Sie die Häufigkeit, mit der Updates für angepasste Attribute an Braze gesendet werden.
- **Daten vereinheitlichen**: Vereinheitlichen Sie Daten über verschiedene von Amperity unterstützte Plattformen und Braze.
- **Braze-Daten mit Amazon S3 synchronisieren**: Verwenden Sie Braze-Currents zur Integration von Engagement-Daten aus Braze-Kampagnen, um Daten im Apache Avro-Format mit Amazon S3 zu synchronisieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Amperity-Konto | Sie benötigen ein [Amperity-Konto](https://amperity.com/request-a-demo), um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br> Dieser kann im Braze-Dashboard erstellt werden, indem Sie zu **Entwicklungskonsole** > **REST-API-Schlüssel** > **Neuen API-Schlüssel erstellen** navigieren. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager oder auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints). |
| Braze-REST-Endpunkt | Ihre Braze-Endpunkt-URL. Ihr Endpunkt hängt von Ihrer Braze-Instanz ab. |
| Currents-Konnektor (optional) | Der S3-Currents-Konnektor. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Datenabbildung {#data-mapping}

Sowohl Standard- als auch angepasste Attribute können von Amperity an Braze gesendet werden, sodass Sie Kundenprofile in Braze mit Daten aus verschiedenen Quellen über Amperity anreichern können. Die spezifischen Attribute, die Sie senden können, hängen von den Daten in Ihrem Amperity-System und den Attributen ab, die Sie in Braze eingerichtet haben.

Lesen Sie weiter, um mehr über diese Attribute zu erfahren.

### Standard-Attribute {#standard-attributes}

[Profilattribute]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) beschreiben, wer Ihre Kund:innen sind. Sie sind oft mit der Identität der Kund:innen verbunden, wie z. B.:
- Namen
- Geburtsdaten
- E-Mail-Adressen
- Telefonnummern

### Angepasste Attribute {#custom-attributes}

[Angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) in Braze sind Felder, die von Ihrer Marke bestimmt werden. Wenn Sie möchten, dass Amperity angepasste Attribute verwaltet, die bereits in Braze vorhanden sind, passen Sie die von Amperity gesendete Ausgabe an die Namen an, die sich bereits in Ihrem Braze-Workspace befinden. Dies kann Folgendes beinhalten:
- Kaufverläufe
- Loyalitätsstatus
- Wertstufen
- Aktuelle Engagement-Daten

Überprüfen Sie die Namen der angepassten Attribute, die von Amperity an Braze gesendet werden. Amperity fügt ein angepasstes Attribut hinzu, wenn es keinen passenden Namen gibt.

Angepasste Attribute werden nur für diejenigen Nutzer:innen aktualisiert, die über eine passende `external_id` oder `braze_id` in Braze verfügen.

### Amperity-Zielgruppen {#amperity-audiences}

Zielgruppen, die von Amperity mit Braze synchronisiert werden, werden als angepasste Attribute in Nutzerprofilen gespeichert. Diese können dann verwendet werden, um diese Nutzer:innen in Braze zu targetieren.

![Dropdown-Liste der Filter mit angepassten Attributen in der Kategorie „Angepasste Daten“.]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

![Dropdown-Liste mit angepassten Attributen wie „l12m_frequency“ und „l12m_monetary“.]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### Datentypen {#data-types}

Folgende Datentypen werden unterstützt:
- Boolescher Wert
- Datum
- Datetime
- Dezimalzahl
- Gleitkommazahl
- Integer
- String
- Varchar

Der verwendete Datentyp hängt von der Art des Attributs ab. Eine E-Mail-Adresse wäre zum Beispiel ein String, während das Alter einer Kund:in ein Integer sein könnte.

### Duplizierung von Attributen {#duplication-of-attributes}

Vermeiden Sie das Senden angepasster Attribute, die die Felder des Standard-Nutzerprofils duplizieren. Das Geburtsdatum sollte beispielsweise als Nutzerprofil-Feld mit dem Namen „dob“ an Braze gesendet werden, damit es mit dem Braze-Standardattribut übereinstimmt. Wenn es als „birthday“, „Birthdate“ oder ein anderer String gesendet wird, wird ein angepasstes Attribut erstellt, und die Werte im Feld „dob“ werden nicht aktualisiert.

### Datenpunkte {#data-points}

Amperity verfolgt, was sich zwischen den Synchronisierungen mit Braze ändert und wie der Status der Sendungen insgesamt ist. Amperity sendet Braze nur die Listenmitgliedschaft und andere ausgewählte Attribute, die sich seit der letzten Synchronisierung geändert haben.

## Integration

### 1. Schritt: Konfigurationsdetails für Braze erfassen {#step-1-capture-configuration-details-for-braze}

1. Erstellen Sie einen Braze REST-API-Schlüssel für Ihren Braze-Workspace mit den `users.track`-Berechtigungen unter **User Data**. Der Endpunkt `users.track` synchronisiert die Amperity-Zielgruppe mit Braze als angepasstes Attribut.
2. Ermitteln Sie den [REST-API-Endpunkt]({{site.baseurl}}/api/basics/#endpoints) für Ihre Braze-Instanz. Wenn Ihre Braze-URL beispielsweise `https://dashboard-03.braze.com` lautet, ist Ihr REST-API-Endpunkt `https://rest.iad-03.braze.com` und Ihre Instanz ist „US-03“.
3. Bestimmen Sie eine Liste von [Nutzerprofilfeldern]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields) und [angepassten Attributen]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/), die von Amperity an Braze gesendet werden können.

### 2. Schritt: Braze als Ziel einrichten – DataGrid Operator {#step-2-set-up-braze-as-a-destinationdatagrid-operator}

#### Schritt 2a: Kundenprofile-Tabelle erstellen {#step-2a-build-the-customer-profiles-table}

Erstellen Sie eine neue Tabelle mit dem Namen „Braze Customer Attributes“ in Ihrer Customer 360-Datenbank in Amperity. Diese Tabelle sollte alle Attribute von Braze enthalten, die Ihre Marke von Amperity aus verwalten möchte, einschließlich der von Braze geforderten Standard-Nutzerprofilfelder und aller angepassten Attribute. Verwenden Sie SQL, um die Struktur dieser Tabelle zu definieren, wie in [der Amperity-Dokumentation](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table) beschrieben.

#### Schritt 2b: Tabelle benennen, validieren und speichern {#step-2b-name-validate-and-save-the-table}

Benennen Sie die Tabelle „Braze Customer Attributes“ und speichern Sie sie. Überprüfen Sie, ob die Tabelle für den **Segment Editor** und den Editor **Edit Attributes** innerhalb von Campaigns zugänglich ist.

#### Schritt 2c: Braze als Ziel hinzufügen {#step-2c-add-braze-as-a-destination}

Navigieren Sie in der Amperity-Plattform zum Tab **Destinations**. Suchen Sie nach der Option, ein neues Ziel hinzuzufügen. Wählen Sie aus den verfügbaren Optionen **Braze** aus.

![Der Abschnitt „New Destination“ mit dem Namen „Braze API“, der Beschreibung „Send audience attributes to Braze.“ und dem Plugin „Braze“.]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### Schritt 2d: Zieldetails konfigurieren {#step-2d-configure-destination-details}

Geben Sie unter **Braze settings** die Braze-Zugangsdaten und die Zieleinstellungen an, wie in [der Amperity-Dokumentation](https://docs.amperity.com/datagrid/destination_braze.html#add-destination) beschrieben. Geben Sie die im letzten Schritt gesammelten Konfigurationsdetails ein und definieren Sie den Braze-Bezeichner. Verfügbare Bezeichner für den Abgleich sind:
- `braze_id`: Ein automatisch zugewiesener Braze-Bezeichner, der nicht geändert werden kann und mit bestimmten Nutzer:innen verknüpft ist, wenn diese in Braze erstellt werden.
- `external_id`: Ein von Kund:innen zugewiesener Bezeichner, normalerweise eine UUID.

![Der Abschnitt „Braze Settings“ mit der Instanz „US-03“, dem Nutzerbezeichner „external_id“, leerem Segmentnamen, dem S3-Bucket „amperity-training-abc123“ und dem S3-Ordner „braze-attributes“.]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### Schritt 2e: Daten-Template hinzufügen {#step-2e-add-a-data-template}

Öffnen Sie auf dem Tab **Destinations** das Menü für das Braze-Ziel und wählen Sie **Add data template**. Geben Sie einen Namen und eine Beschreibung für das Template ein (z. B. „Braze“ und „Send custom attributes to Braze“), überprüfen Sie den Zugriff der geschäftlichen Nutzer:innen und kontrollieren Sie alle Konfigurationseinstellungen.

Wenn die erforderlichen Einstellungen nicht als Teil des Ziels konfiguriert wurden, konfigurieren Sie sie als Teil des Daten-Templates. Speichern Sie das Daten-Template.

![Der Abschnitt „Data Template Name“ mit dem Namen „Braze Audience Attributes“ und der Beschreibung „Send audience attributes to Braze.“]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### Schritt 2f: Konfiguration speichern {#step-2f-save-the-configuration}

Nachdem Sie die erforderlichen Angaben gemacht haben, speichern Sie die Konfiguration. Da Braze nun als Ziel konfiguriert ist, können Nutzer:innen von Amp360 und AmpIQ Daten mit Braze synchronisieren.

### 3. Schritt: Daten mit Braze synchronisieren {#step-3-sync-data-to-braze}

Stellen Sie sicher, dass Braze für Ihren Amperity-Mandanten aktiviert ist. Wenn dies nicht der Fall ist, wenden Sie sich an Ihren DataGrid Operator oder die Vertretung von Amperity.

Befolgen Sie dann die Synchronisierungsanweisungen für Amp360 oder AmpIQ, je nachdem, was für Ihr Unternehmen zutrifft.

#### Synchronisierungsoption 1: Abfrageergebnisse über Amp360 an Braze senden {#syncing-option-1-send-query-results-to-braze-via-amp360}

Nutzer:innen von Amp360 können mit SQL Abfragen in freier Form schreiben und dann einen Zeitplan konfigurieren, der die Ergebnisse an Braze sendet.

##### 1. Schritt: Abfrage in Amperity erstellen {#step-1-create-a-query-in-amperity}

Navigieren Sie zur Abfragefunktion in Amperity und erstellen Sie eine SQL-Abfrage, die den gewünschten Satz an Kundendaten liefert. Die Ergebnisse sollten die spezifischen Attribute enthalten, die Sie an Braze senden möchten. Sehen Sie sich dieses Beispiel einer Amperity-Abfrage an, mit der Sie eine Liste von Nutzer:innen mit ihren Kaufverläufen erhalten.

##### 2. Schritt: Neue Orchestrierung in Amperity hinzufügen {#step-2-add-a-new-orchestration-in-amperity}

1. Gehen Sie zum Bereich **Orchestration** und klicken Sie auf die Option zum Hinzufügen einer neuen Orchestrierung.
2. Geben Sie an, was die Orchestrierung tun soll. Dazu gehört in der Regel die Angabe der SQL-Abfrage, die ausgeführt werden soll, und wohin die Ergebnisse gesendet werden sollen. Wählen Sie in diesem Fall die SQL-Abfrage aus, die Sie erstellt haben, um die Liste der aktiven Kund:innen zu generieren, und geben Sie Braze als Ziel für die Ergebnisse an.
3. Legen Sie fest, wann und wie oft die Orchestrierung ausgeführt werden soll. Sie können die Orchestrierung zum Beispiel täglich zu einer bestimmten Zeit ausführen.
4. Speichern Sie die Orchestrierung, nachdem Sie sie nach Ihren Wünschen konfiguriert haben. Sie wird zu Ihrer Liste der Orchestrierungen in Amperity hinzugefügt.
5. Testen Sie die Orchestrierung, um sicherzustellen, dass sie wie erwartet funktioniert. Sie können dies tun, indem Sie die Orchestrierung manuell triggern und die Ergebnisse in Braze überprüfen.

##### 3. Schritt: Orchestrierung ausführen {#step-3-run-the-orchestration}

Führen Sie die Orchestrierung aus, um die Abfrage auszuführen und die Ergebnisse an Braze zu senden. Dies kann manuell geschehen oder nach dem Zeitplan, den Sie in den Orchestrierungseinstellungen festgelegt haben.

#### Synchronisierungsoption 2: Zielgruppen über AmpIQ an Braze senden {#syncing-option-2-send-audiences-to-braze-via-ampiq}

Nutzer:innen von AmpIQ können Segmente in Amperity über eine Nicht-SQL-Schnittstelle erstellen und diese mit nachgelagerten Zielen wie Braze synchronisieren. Nutzer:innen können Ziele auswählen und dann eine Liste von Attributen konfigurieren, die an jedes Ziel gesendet werden sollen.

##### 1. Schritt: Segment in Amperity erstellen {#step-1-create-a-segment-in-amperity}

Erstellen Sie ein Segment in Amperity, das eine Liste von Kund:innen liefert. Dieses Segment sollte mit den angepassten Attributen verknüpft sein, die Sie in Braze aktualisieren möchten.

{% alert note %}
In der Dokumentation von Amperity finden Sie Beispiele für verschiedene Segmenttypen, die Sie möglicherweise an Braze senden möchten.
{% endalert %}

##### 2. Schritt: Kampagne in Amperity erstellen {#step-2-build-a-campaign-in-amperity}

1. Gehen Sie in den Bereich **Campaign** und klicken Sie auf die Option zum Erstellen einer neuen Kampagne.
2. Geben Sie Ihrer Kampagne einen beschreibenden und eindeutigen Namen, mit dem Sie sie später leichter identifizieren können, insbesondere wenn Sie mehrere Kampagnen haben.
3. Wählen Sie das Segment der Kund:innen aus, das Sie mit dieser Kampagne ansprechen möchten. Dies sollte das Segment sein, das Sie zuvor erstellt haben. <br>![Das Dropdown-Feld für Segmente, die vom Targeting ausgeschlossen werden sollen.]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. Wählen Sie die Daten aus, die Sie im Rahmen der Kampagne versenden möchten. Dies kann eine Reihe von Kundenattributen umfassen. ![Im Modal „Edit Campaign Attributes“ können Sie ein Ziel und Kundenattribute auswählen.]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. Wählen Sie **Braze** als das Ziel aus, an das die Kampagnendaten gesendet werden sollen.
6. Wählen Sie, wann und wie oft die Kampagne laufen soll. Dies kann ein einmaliges Ereignis oder ein wiederkehrender Zeitplan sein.
7. Speichern Sie Ihre Kampagne und führen Sie einen Test durch, um sicherzustellen, dass sie wie erwartet funktioniert.

##### 3. Schritt: Kampagne ausführen {#step-3-run-the-campaign}

Führen Sie die Kampagne aus, um das Segment an Braze zu senden. Dies kann manuell geschehen oder auf der Grundlage des Zeitplans, den Sie in den Kampagneneinstellungen eingerichtet haben.


### Verwendung von Amperity mit Braze-Currents {#using-amperity-with-braze-currents}
So senden Sie Braze-Currents-Daten an Amperity:
1. [Richten Sie einen Braze Current ein]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/), um Daten an einen Amazon S3-Bucket zu senden.
2. Konfigurieren Sie Amperity so, dass es [Apache Avro-Dateien aus diesem Amazon S3-Bucket liest](https://docs.amperity.com/datagrid/source_amazon_s3.html).
3. Konfigurieren Sie Feeds und automatisieren Sie das Laden von Daten mithilfe von Standard-Workflows.