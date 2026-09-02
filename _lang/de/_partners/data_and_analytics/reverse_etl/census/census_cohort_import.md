---
nav_title: Census
article_title: Census Kohortenimport
description: "Dieser Referenzartikel beschreibt die Kohortenimport-Funktionalität von Census, einer Datenintegrationsplattform, die es Ihnen erlaubt, mit Daten aus Ihrem Cloud Data Warehouse dynamisch Targeting-Segmente zusammenzustellen."
page_type: partner
search_tag: Partner

---

# Census Kohortenimport {#census-cohort-import}

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten aus [Census](https://www.getcensus.com/) nach Braze importieren. Weitere Informationen zur Integration von Census finden Sie im [Hauptartikel zu Census]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/census).

## Integration des Kohortenimports {#cohort-import-integration}

### Schritt 1: Braze-Serviceverbindung erstellen {#step-1-create-braze-service-connection}

Um Census in die Census-Plattform zu integrieren, navigieren Sie zum Tab **Connections** und wählen Sie **New Destination**, um eine neue Braze-Serviceverbindung zu erstellen.

In der daraufhin angezeigten Eingabeaufforderung geben Sie dieser Verbindung einen Namen und die URL des Braze-Endpunkts, den Representational State Transfer-API-Schlüssel von Braze und den Datenimport-Schlüssel an. Der Datenimport-Schlüssel ist für die Synchronisierung von Kohorten erforderlich und kann in Braze unter **Partnerintegrationen** > **Technologie-Partner** > **Census** gefunden werden.

![Census-Dialog „Neues Ziel“, konfiguriert für Braze-Kohortenimport-Zugangsdaten.]({% image_buster /assets/img/census/add_service.png %}){: style="max-width:60%;"}

### Schritt 2: Eine Census-Synchronisation erstellen {#step-2-create-a-census-sync}

Um Kund:innen mit Braze zu synchronisieren, müssen Sie eine Synchronisierung erstellen. Hier legen Sie fest, wo die Daten synchronisiert werden sollen und wie die Felder auf den beiden Plattformen abgebildet werden sollen.

1. Navigieren Sie zum Tab **Syncs** und wählen Sie **New Sync**.<br><br>
2. Wählen Sie im Composer das Quelldatenmodell aus Ihrem Data Warehouse aus.<br><br>
3. Legen Sie fest, wohin das Modell synchronisiert werden soll. Wählen Sie **Braze** als Ziel und **User & Cohort** als zu synchronisierendes Objekt aus.<br>![In der Eingabeaufforderung „Ziel auswählen“ wird „Braze“ als Verbindung ausgewählt, und es werden verschiedene Objekte aufgelistet.]({% image_buster /assets/img/census/census_2.png %}){: style="max-width:80%;"}<br><br>
4. Wählen Sie die **Source Column** aus, die die Nutzer:innen identifiziert, die einer Kohorte hinzugefügt werden sollen, und wählen Sie **External User ID** als **Identifier Type**.<br><br>
5. Wählen Sie im Dropdown **Cohort Name** eine Kohorte aus, erstellen Sie eine Kohorte oder wählen Sie eine Quellspalte, um den Kohortennamen zu füllen.<br><br>
6. Verwenden Sie das Dropdown **When a record is removed from source data**, um auszuwählen, was mit Nutzer:innen geschieht, wenn sie aus dem Quelldatensatz entfernt werden, z. B. **Do nothing** oder **Remove matching record from cohort**.<br><br>
7. Abschließend ordnen Sie die Census-Datenfelder den entsprechenden Braze-Feldern zu.<br>![Census-Abbildung]({% image_buster /assets/img/census/census_3.png %}){: style="max-width:80%;"}<br><br>
8. Bestätigen Sie die Details und erstellen Sie die Synchronisierung.

Jetzt können Sie Ihre Synchronisierung durchführen!

Bei einer Synchronisierung werden alle Felder, die Sie abbilden, zunächst mit dem Nutzer:innen-Objekt synchronisiert, um das zu Update or aktualisieren or aktualisieren, was bereits in Braze vorhanden ist. Danach werden die aktualisierten Nutzer:innen zur angegebenen Kohorte hinzugefügt.

Nach der Synchronisierung können Sie für zukünftige Braze-Campaigns und Canvase ein Braze-Segment mit einem Census-Kohortenfilter erstellen und hinzufügen, um diese Nutzer:innen anzusprechen.

{% alert note %}
Wenn Sie die Integration von Census und Braze verwenden, sendet Census bei jeder Synchronisierung nur die Deltas (sich ändernde Daten) an Braze.
{% endalert %}

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

## Nutzer:innen-Abgleich {#user-matching}

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` abgeglichen werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.