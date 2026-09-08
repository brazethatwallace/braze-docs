---
nav_title: Census
article_title: Census
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Census, einer Datenintegrationsplattform, die es Ihnen erlaubt, mit Daten aus Ihrem Cloud Warehouse dynamisch Targeting-Segmente zusammenzustellen."
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# Census

> [Census](https://www.getcensus.com/) ist eine Datenaktivierungsplattform, die Cloud Data Warehouses wie Snowflake und BigQuery mit Braze verbindet. Marketingteams können das Potenzial ihrer First-Party-Daten nutzen, um dynamische Zielgruppensegmente zu erstellen, Kundenattribute zu synchronisieren, Campaigns zu personalisieren und ihre Daten in Braze auf dem neuesten Stand zu halten. Es ist einfacher als je zuvor, mit zuverlässigen, verwertbaren Daten zu handeln – ohne CSV-Uploads oder technische Hilfsmittel.

Die Integration von Braze und Census erlaubt es Ihnen, Zielgruppen oder Produktdaten dynamisch in Braze zu importieren, um personalisierte Campaigns zu versenden. Sie können in Braze zum Beispiel eine Kohorte für „Newsletter-Abonnent:innen mit CLV > 1000“ erstellen, um hochwertige Kund:innen anzusprechen, oder „Nutzer:innen, die in den letzten 30 Tagen aktiv waren“, um bestimmte Nutzer:innen für den Test eines bevorstehenden Beta-Features anzusprechen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| Census-Konto | Ein [Census-Konto](https://www.getcensus.com/) ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit allen Nutzerdaten-Berechtigungen (außer `users.delete`) und `segments.list`-Berechtigungen. Die Berechtigungen können sich ändern, da Census die Unterstützung für weitere Braze-Objekte erweitert. Daher sollten Sie entweder jetzt mehr Berechtigungen erteilen oder planen, diese Berechtigungen in Zukunft zu aktualisieren. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL Ihrer Instanz]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) ab. |
| Data Warehouse und Datenmodell | Bevor Sie mit der Integration beginnen, müssen Sie ein Data Warehouse in Census eingerichtet und ein Modell der Teilmenge der Daten definiert haben, die Sie mit Braze synchronisieren möchten. Besuchen Sie die [Census-Dokumentation](https://docs.getcensus.com/destinations/braze) für eine Liste der verfügbaren Datenquellen und Anleitungen zur Modellerstellung. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Braze-Serviceverbindung erstellen {#step-1-create-braze-service-connection}

Um Census in die Census-Plattform zu integrieren, navigieren Sie zum Tab **Connections** und wählen Sie **New Destination**, um eine neue Braze-Serviceverbindung zu erstellen.

In der daraufhin angezeigten Eingabeaufforderung geben Sie dieser Verbindung einen Namen und die URL des Braze-Endpunkts sowie den REST-API-Schlüssel von Braze an (und optional Ihren Datenimport-Schlüssel für die Synchronisierung von Kohorten).

![Census-Dialog „Neues Ziel“, konfiguriert für Braze-Verbindungszugangsdaten.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Schritt 2: Eine Census-Synchronisation erstellen {#step-2-create-a-census-sync}

Um Kund:innen mit Braze zu synchronisieren, müssen Sie eine Synchronisierung erstellen. Hier legen Sie fest, wo die Daten synchronisiert werden sollen und wie die Felder auf den beiden Plattformen abgebildet werden sollen.

1. Navigieren Sie zum Tab **Syncs** und wählen Sie **New Sync**.<br><br>
2. Wählen Sie im Composer das Quelldatenmodell aus Ihrem Data Warehouse aus.<br><br>
3. Legen Sie fest, wohin das Modell synchronisiert werden soll. Wählen Sie **Braze** als Ziel und den [unterstützten Objekttyp](#supported-objects) für die Synchronisierung aus.<br>![In der Eingabeaufforderung „Ziel auswählen“ wird „Braze“ als Verbindung ausgewählt, und es werden verschiedene Objekte aufgelistet.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Wählen Sie aus, welche Synchronisierungsregel Sie anwenden möchten (**Update or Create** ist die häufigste Wahl, aber Sie können auch erweiterte Regeln wählen, um z. B. das Löschen von Daten zu behandeln).<br><br>
5. Als Nächstes wählen Sie für den Abgleich von Datensätzen einen Synchronisationsschlüssel, um Ihr Braze-Objekt einem Modellfeld [zuzuordnen](#supported-objects).<br>![In der Aufforderung „Sync-Schlüssel auswählen“ wird die „External User ID“ von Braze mit „user_id“ in der Quelle abgeglichen.]({% image_buster /assets/img/census/census_1.png %}){: style="max-width:80%;"}<br><br>
6. Abschließend ordnen Sie die Census-Datenfelder den entsprechenden Braze-Feldern zu.<br>![Census-Feldzuordnung]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
7. Bestätigen Sie die Details und erstellen Sie die Synchronisierung.

Nachdem die Synchronisierung durchgeführt wurde, befinden sich die Nutzerdaten in Braze. Sie können ein Braze Segment erstellen und zu zukünftigen Campaigns und Canvases hinzufügen, um diese Nutzer:innen zu targetieren.

{% alert note %}
Wenn Sie die Integration von Census und Braze verwenden, sendet Census bei jeder Synchronisierung nur die Deltas (sich ändernde Daten) an Braze.
{% endalert %}

## Unterstützte Objekte {#supported-objects}

Census unterstützt derzeit die Synchronisierung der folgenden Braze-Objekte:

| Objektname | Synchronisierungsverhalten |
| --- | --- |
| User | Update, Create, Mirror, Delete |
| Cohort | Update, Create, Mirror |
| Catalog | Update, Create, Mirror |
| Subscription Group Membership | Mirror |
| Event | Append |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unterstützte Objekte" }

Darüber hinaus unterstützt Census das Senden von [strukturierten Daten](https://docs.getcensus.com/destinations/braze#supported-objects) an Braze. Um Push-Token von Nutzer:innen zu senden, sollten Ihre Daten als Array von Objekten mit 2–3 Werten strukturiert sein: `app_id`, `token` und eine optionale `device_id`.