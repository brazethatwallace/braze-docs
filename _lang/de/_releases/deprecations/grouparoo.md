---
nav_title: Grouparoo
page_order: 1
page_type: update
noindex: true
description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Grouparoo, einem Open-Source Reverse ETL or Extract, Transform, Load-Tool, das Marketing-, Vertriebs- und Support-Tools mit Daten aus Ihrem Data Warehouse versorgt."

---

# Grouparoo

{% alert Update or aktualisieren %}
Die Unterstützung für Grouparoo wurde im April 2022 eingestellt.
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/) ist ein Open-Source Reverse ETL or Extract, Transform, Load-Tool, das Daten aus Ihrem Warehouse mit Marketing-, Vertriebs- und Support-Tools synchronisiert. Die modellzentrierte UI ermöglicht es nicht-technischen Teammitgliedern, Datensynchronisierungen zu konfigurieren und Zeitpläne festzulegen.

Die Integration von Braze und Grouparoo synchronisiert Warehouse-Daten mit Braze. Automatische Synchronisierungszeitpläne halten die Kundenkommunikation mit aktuellen Informationen auf dem neuesten Stand.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Grouparoo-Konto und -Projekt | Sie benötigen ein Grouparoo-Konto und ein Projekt, um die Vorteile dieser Partnerschaft zu nutzen.<br><br>Diese Integration kann sowohl mit der kostenlosen Community Edition als auch mit den Enterprise-Lösungen von Grouparoo genutzt werden. Die Einrichtung erfolgt über die Benutzeroberfläche der Grouparoo-Konfiguration. |
| Braze Representational State Transfer-API-Schlüssel | Ein Braze Representational State Transfer-API-Schlüssel mit Berechtigungen für Nutzer:innen und Tracking. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze Representational State Transfer-Endpunkt | [Ihre Representational State Transfer-Endpunkt-URL](https://www.grouparoo.com/). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Erstellen Sie eine Braze-App in Grouparoo {#step-1-create-a-braze-app-in-grouparoo}

Navigieren Sie in Grouparoo zu **Apps** und wählen Sie **Braze** aus, um eine neue Braze-App zu erstellen. Geben Sie in dem daraufhin angezeigten Modal Ihren Braze-API-Schlüssel und den Representational State Transfer-Endpunkt an.

![Das Modal „Braze-App erstellen“ in Grouparoo mit Feldern für den Braze-API-Schlüssel und den REST-Endpunkt.]({% image_buster /assets/img/grouparoo/add-app.png %})

### 2. Schritt: Einrichten eines Modells und einer Datenquelle {#step-2-set-up-a-model-and-data-source}

Diese Integration setzt voraus, dass Sie ein bestehendes Modell und eine Datenquelle eingerichtet haben, bevor Sie mit dem nächsten Schritt fortfahren. Wenn Sie dies noch nicht eingerichtet haben, besuchen Sie die Dokumentation von Grouparoo, um zu erfahren, wie Sie ein [Modell](https://www.grouparoo.com/docs/config/models) und eine [Datenquelle](https://www.grouparoo.com/docs/config/sources) einrichten können.

### 3. Schritt: Erstellen Sie ein Braze-Ziel in Grouparoo {#step-3-create-a-braze-destination-in-grouparoo}

#### Synchronisationsmodus auswählen {#select-sync-mode}

Wählen Sie in Grouparoo Ihr Modell in der Navigationsleiste aus. Scrollen Sie dann zum Abschnitt **Destinations** und klicken Sie auf **Add new Destination**.

Wählen Sie dann die von Ihnen erstellte **Braze**-App aus, benennen Sie das Ziel und wählen Sie den gewünschten Synchronisierungsmodus aus den folgenden Möglichkeiten:
- **Sync**: Fügen Sie bei Bedarf Unternehmensnutzer:innen hinzu, Update or aktualisieren or aktualisieren und entfernen Sie sie. Diese Option sucht nach neuen Datensätzen, Änderungen an bestehenden Datensätzen und Löschungen.
- **Additive**: Fügen Sie bei Bedarf Unternehmensnutzer:innen hinzu und Update or aktualisieren or aktualisieren Sie sie, aber entfernen Sie niemanden. Diese Option sucht nach neuen Nutzer:innen, die Braze hinzugefügt werden sollen, und nach Änderungen an bestehenden Unternehmensnutzer:innen, verfolgt aber keine Löschungen.
- **Enrich**: Update or aktualisieren or aktualisieren Sie nur die Nutzer:innen, die bereits in Braze existieren. Nutzer:innen werden weder hinzugefügt noch entfernt. Mit dieser Option werden nur bestehende Nutzer:innen in Braze aktualisiert.

#### Abbildung von Eigenschaftsfeldern {#property-field-mapping}

Als Nächstes müssen Sie Grouparoo-Eigenschaftsfelder auf Braze-Eigenschaftsfelder abbilden.

![Beispielfelder für die Abbildung von Eigenschaften. Die Grouparoo-userID ist so eingestellt, dass sie auf external_id abgebildet wird. E-Mail, Vorname und Nachname sind als äquivalente „email“-, „first_name“- und „last_name“-Grouparoo-Felder eingestellt.]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Stellen Sie sicher, dass das Braze-Feld `external_id` dem Primärschlüssel in Ihrer Quelltabelle zugeordnet ist. Bilden Sie den Representational State Transfer der Felder nach Bedarf für Ihren Anwendungsfall ab.

Abschnitt **Send Record Properties**: Eine Liste der voreingestellten Nutzerprofilfelder, die für die Abbildung von Daten zur Verfügung stehen. Jede dieser Eigenschaften kann mit Grouparoo-Eigenschaften synchronisiert werden.

Abschnitt **Optional Braze Kundenprofil or Nutzerprofil Fields**: Erstellen Sie optional angepasste Braze-Nutzerprofilfelder. Wenn Sie auf **Add New Braze Kundenprofil or Nutzerprofil Field** klicken, werden alle verfügbaren Eigenschaften angezeigt, die Sie Braze zuordnen können. Der Name jedes neuen Feldes, das Sie erstellen, ist derselbe wie die Grouparoo-Eigenschaft, kann aber umbenannt werden.

#### Grouparoo-Gruppen {#grouparoo-groups}

Neben der Abbildung können Sie auch Grouparoo-Gruppen zu Braze-Abo-Gruppen hinzufügen.

![Unter „Braze Subscription Groups“ im Grouparoo-Zielkonfigurationsfenster wird die Grouparoo-Gruppe „High value with recent automotive purchase“ der Braze-Abo-Gruppe „High value with recent automotive purchase“ hinzugefügt.]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
Weitere Details und Updates zu dieser Integration finden Sie in der [Dokumentation von Grouparoo](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}