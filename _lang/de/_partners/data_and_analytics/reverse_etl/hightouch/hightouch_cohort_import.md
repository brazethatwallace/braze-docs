---
nav_title: Hightouch Kohortenimport
article_title: Hightouch Kohortenimport
description: "Dieser Referenzartikel beschreibt die Kohortenimport-Funktionalität von Hightouch, einer Plattform zur Synchronisierung Ihrer Kundendaten aus Ihrem Data Warehouse mit Business Tools."
page_type: partner
search_tag: Partner

---
# Hightouch Kohortenimport {#hightouch-cohort-import}

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten aus [Hightouch](https://hightouch.io) in Braze importieren, damit Sie gezielte Campaigns auf der Grundlage von Daten versenden können, die möglicherweise nur in Ihrem Warehouse vorhanden sind. Weitere Informationen zur Integration von Hightouch und seinen anderen Funktionen finden Sie im [Hauptartikel zu Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch).

## Integration von Datenimporten {#data-import-integration}

### Schritt 1: Braze Datenimport-Schlüssel abrufen {#step-1-get-the-braze-data-import-key}
Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Hightouch** aus.

Hier finden Sie Ihren REST-Endpunkt und können Ihren Braze Datenimport-Schlüssel generieren. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden ungültig machen.<br><br>![Braze Hightouch Technologie-Partnerseite mit REST-Endpunkt und Datenimport-Schlüssel-Steuerelementen.]({% image_buster /assets/img/hightouch/data_import_key.png %}){: style="max-width:90%;"}

### Schritt 2: Braze Kohorten als Ziel in Hightouch hinzufügen {#step-2-add-braze-cohorts-as-a-destination-in-hightouch}
Navigieren Sie zur Seite **Destination** in Ihrem Hightouch Workspace, suchen Sie nach **Braze Cohorts** und klicken Sie auf **Continue**. Geben Sie dort Ihren REST-Endpunkt und Ihren Datenimport-Schlüssel ein und klicken Sie auf **Continue**.<br><br>![Hightouch-Zielkonfiguration für Braze Cohorts mit Anmeldedatenfeldern.]({% image_buster /assets/img/hightouch/cohort1.png %}){: style="max-width:90%;"}

### Schritt 3: Ein Modell (oder eine Zielgruppe) mit Braze Kohorten synchronisieren {#step-3-sync-a-model-or-audience-into-braze-cohorts}
Erstellen Sie in Hightouch unter Verwendung Ihres erstellten [Modells](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) oder Ihrer [Zielgruppe](https://hightouch.io/docs/audiences/usage/) eine neue Synchronisierung. Wählen Sie dann das Braze-Kohorten-Ziel aus, das Sie im vorherigen Schritt erstellt haben. Wählen Sie abschließend in der Braze-Kohorten-Zielkonfiguration den Bezeichner aus, den Sie abgleichen möchten, und entscheiden Sie, ob Hightouch eine neue Braze Kohorte erstellen oder eine bestehende aktualisieren soll.<br><br>![Hightouch Braze-Kohorten-Synchronisierungskonfiguration mit Abgleichbezeichner und Kohortenoptionen.]({% image_buster /assets/img/hightouch/cohort2.png %}){: style="max-width:90%;"}

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

### Schritt 4: Ein Braze Segment aus der angepassten Hightouch-Zielgruppe erstellen {#step-4-create-a-braze-segment-from-the-hightouch-custom-audience}
Navigieren Sie in Braze zu **Segments**, erstellen Sie ein neues Segment und wählen Sie **Hightouch Cohorts** als Filter aus. Von hier aus können Sie auswählen, welche Hightouch Kohorte Sie einbeziehen möchten. Nachdem Ihr Hightouch-Kohorten-Segment erstellt wurde, können Sie es als Zielgruppenfilter auswählen, wenn Sie eine Campaign oder ein Canvas erstellen.<br><br>![Braze Segment Builder mit dem Hightouch-Kohorten-Filter.]({% image_buster /assets/img/hightouch/cohort3.png %}){: style="max-width:90%;"}

### Verwendung dieser Integration {#using-this-integration}
Um Ihr Hightouch Segment zu verwenden, erstellen Sie eine Braze Campaign oder ein Canvas und wählen Sie das Segment als Ihre Zielgruppe aus.<br><br>![Braze Zielgruppen-Targeting-Schritt mit einem ausgewählten Hightouch-gestützten Segment.]({% image_buster /assets/img/hightouch/cohort4.png %}){: style="max-width:90%;"}

## Nutzer:innen-Abgleich {#user-matching}

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder ihren `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` abgeglichen werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden und müssen über ihre `external_id` oder ihren `alias` identifiziert werden.