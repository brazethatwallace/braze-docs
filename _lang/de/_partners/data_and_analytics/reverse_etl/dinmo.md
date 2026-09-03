---
nav_title: DinMo
article_title: DinMo
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und DinMo, einer Composable Customer Data Platform, die Reverse-ETL nutzt, um Data-Warehouse-Daten in Braze zu synchronisieren."
alias: /partners/dinmo/
page_type: partner
search_tag: Partner

---

# DinMo

> [DinMo](https://www.dinmo.com/) ist eine Composable Customer Data Platform (CDP), die Ihr Cloud Data Warehouse über Reverse Extract, Transform, Load (ETL) mit Braze verbindet. Marketing-Teams können Zielgruppen-Segmente aus Data-Warehouse-Daten erstellen, Nutzerattribute und Events in Braze synchronisieren und Abo-Status ohne CSV-Uploads oder technischen Support aktuell halten.

_Diese Integration wird von DinMo verwaltet._

Die Integration von Braze und DinMo überträgt Segmente und Datenmodelle aus Ihrem Data Warehouse über die Braze REST API in Braze. Wenn Sie ein Braze-Ziel in DinMo verbinden, senden Aktivierungen Daten aus Ihren Modellen oder Segmenten an Braze.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| DinMo-Konto | Ein [DinMo-Konto](https://www.dinmo.com/) mit der Berechtigung, Ziele zu erstellen, ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Braze-REST-API-Schlüssel | Ein Braze-REST-API-Schlüssel mit den für die Ziel-Dienste, die Sie nutzen möchten, [erforderlichen Berechtigungen](#api-key-permissions). Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-REST-Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von den [API-Endpunkten]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints) Ihrer Braze-Instanz ab. |
| Braze-Dashboard-URL | Ihre Braze-Dashboard-URL für Ihre Instanz (zum Beispiel `https://dashboard.iad-01.braze.com`). Weitere Informationen finden Sie unter [Verfügbare SDK-Endpunkte]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints). |
| Data Warehouse und Datenmodell | Bevor Sie mit der Integration beginnen, verbinden Sie Ihr Data Warehouse in DinMo und definieren Sie ein Modell oder Segment für die Daten, die Sie mit Braze synchronisieren möchten. Weitere Informationen finden Sie im [DinMo-Braze-Integrationsleitfaden](https://docs.dinmo.io/integrations/destination-platforms/braze). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

Mit dieser Integration können Sie:

* Nutzerattribute aus Ihrem Data Warehouse mit Braze synchronisieren, um Campaigns und Canvases zu personalisieren.
* Angepasste Events und Kauf-Events aus Data-Warehouse-Daten an Braze senden, um verhaltensbasiertes Targeting zu ermöglichen.
* Die Mitgliedschaft in Braze-Abo-Gruppen mit den in DinMo definierten Zielgruppen-Segmenten abgleichen.
* DinMo-Segmente als Braze-Nutzerattribute exportieren und daraus Braze-Segments erstellen.

## API-Schlüssel-Berechtigungen {#api-key-permissions}

Gewähren Sie die folgenden Berechtigungen für Ihren Braze REST-API-Schlüssel basierend auf den von Ihnen verwendeten Ziel-Diensten:

| Berechtigung | Erforderlich für |
| --- | --- |
| `users.track` | Synchronisierung von Nutzerattributen, Senden von Track-Events und Validierung der Zielverbindung |
| `users.export.ids` | Export von Nutzer-IDs für Massenoperationen |
| `users.alias.update` | Aktualisierung von Nutzer-Aliasen |
| `subscription.status.set` | Synchronisierung von Abo-Status |
| `users.delete` | Nur Mirror-Sync-Modus (optional für andere Ziel-Dienste) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API-Schlüssel-Berechtigungen" }

## Integration

### Schritt 1: Braze-Ziel in DinMo konfigurieren {#step-1-configure-the-braze-destination-in-dinmo}

1. Navigieren Sie in DinMo zu **Destinations** in der Seitennavigation.
2. Wählen Sie **Add a new destination** > **Connect a new platform** > **Braze**.
3. Geben Sie im Verbindungsformular die folgenden Details ein:
   * **Platform Name**: Zum Beispiel `Braze – Ihr Unternehmen`
   * **REST API URL**: Ihr Instanz-REST-Endpunkt (zum Beispiel `https://rest.eu-01.braze.com`)
   * **Dashboard URL**: Ihre Instanz-Dashboard-URL (zum Beispiel `https://dashboard.eu-01.braze.com`)
   * **API Key**: Der Schlüssel, den Sie aus Braze kopiert haben
4. Wählen Sie **Connect**, um Ihre Zugangsdaten zu validieren.

{% alert note %}
Sie müssen sowohl die REST-API-URL als auch die Dashboard-URL angeben. Fügen Sie keinen abschließenden Schrägstrich an die REST-API-URL an.
{% endalert %}

### Schritt 2: Verbindung überprüfen {#step-2-verify-the-connection}

Nachdem Sie das Ziel gespeichert haben, führt DinMo einen Testaufruf durch (zum Beispiel `users.track`), um zu bestätigen, dass Ihr API-Schlüssel und Endpunkt funktionieren.

Wenn die Validierung fehlschlägt, überprüfen Sie Folgendes:

* Die REST-API-URL ist korrekt und hat keinen abschließenden Schrägstrich.
* Der API-Schlüssel ist gültig und verfügt über die erforderlichen Berechtigungen.
* Wenn Ihr Braze-Workspace eine IP-Zulassungsliste verwendet, sind die IP-Adressen von DinMo enthalten.

## Unterstützte Zieldienste {#supported-destination-services}

Jeder Zieldienst in DinMo folgt dem gleichen allgemeinen Workflow: Erstellen Sie ein Braze-Ziel, bauen Sie ein DinMo-Modell oder -Segment auf und erstellen Sie dann eine Aktivierung, um Daten an Braze zu senden. Eine schrittweise Anleitung zur Aktivierung finden Sie unter [DinMo Braze-Zieldienste](https://docs.dinmo.io/integrations/destination-platforms/braze).

Die folgenden Zieldienste stehen zur Verfügung:

| Zieldienst | Beschreibung |
| --- | --- |
| [Nutzerattribute synchronisieren](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-users-attributes) | Aktualisieren Sie Nutzerprofilattribute in Braze und fügen Sie optional neue Nutzer:innen ein. |
| [Track-Events senden](https://docs.dinmo.io/integrations/destination-platforms/braze/send-track-events) | Senden Sie angepasste Events und Kauf-Events an Braze. |
| [Abo-Status synchronisieren](https://docs.dinmo.io/integrations/destination-platforms/braze/synchronize-subscription-statuses) | Abonnieren oder melden Sie Nutzer:innen in einer Braze-Abo-Gruppe basierend auf der DinMo-Segmentzugehörigkeit ab. |
| [Nutzerlisten exportieren](https://docs.dinmo.io/integrations/destination-platforms/braze/export-user-lists) | Synchronisieren Sie die Segmentzugehörigkeit mit einem Braze-Nutzerattribut zur Verwendung in der Braze-Segmentierung. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Unterstützte Zieldienste" }

### Nutzerattribute synchronisieren {#synchronize-user-attributes}

Verwenden Sie diesen Zieldienst, um Attribute auf bestehenden Braze-Nutzerprofilen zu aktualisieren und optional neue Nutzer:innen einzufügen.

Wenn Sie eine Aktivierung ausführen:

* Wenn Sie den Einfügemodus aktivieren, werden neue Nutzer:innen aus dem Modell in Braze erstellt (UPSERT-Verhalten).
* Geänderte Attributwerte seit der letzten Aktivierung werden in Braze aktualisiert.

Wenn Sie den Einfügemodus nicht aktivieren, aktualisiert DinMo nur Nutzer:innen, die bereits in Braze vorhanden sind und eine übereinstimmende externe ID haben.

Ordnen Sie während der Aktivierungseinrichtung das Feld in Ihrem DinMo-Modell zu, das der [externen ID]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web) oder Braze-ID der Nutzer:innen entspricht. Ordnen Sie jedes DinMo-Feld dem genauen Attributnamen in Braze zu. Wenn ein Attribut in Braze nicht existiert, erstellt DinMo es.

Die folgenden Synchronisierungsmodi stehen für Nutzerattribut-Aktivierungen zur Verfügung:

| Synchronisierungsmodus | Beschreibung |
| --- | --- |
| UPDATE | Aktualisiert geänderte Datensätze für Nutzer:innen, die bereits in Braze vorhanden sind. Fügt keine Datensätze ein und löscht keine. |
| UPSERT | Fügt neue Datensätze ein und aktualisiert geänderte Datensätze. Löscht keine Datensätze. |
| MIRROR | Fügt Datensätze ein, aktualisiert und löscht sie in Braze, um die Quelle zu spiegeln. Erfordert Konnektor-Unterstützung für Löschvorgänge. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Synchronisierungsmodi für Nutzerattribute" }

{% alert warning %}
Der Mirror-Synchronisierungsmodus löscht Datensätze dauerhaft aus Braze, wenn sie in der DinMo-Quelle nicht mehr vorhanden sind. Verwenden Sie den Mirror-Modus nur, wenn Ihr Data Warehouse die einzige Quelle der Wahrheit ist und Löschungen beabsichtigt sind. Validieren Sie die Löschregeln, bevor Sie Mirror-Synchronisierungen in der Produktion ausführen.
{% endalert %}

### Track-Events senden {#send-track-events}

Verwenden Sie diesen Zieldienst, um angepasste Events oder Kauf-Events aus einem DinMo-Event-Modell oder -Segment an Braze zu senden. DinMo behandelt angepasste Events und Käufe als separate Zieldienste, da Braze für jeden Typ unterschiedliche APIs verwendet.

Jeder Datensatz im Modell repräsentiert einen einzelnen Event-Typ (zum Beispiel `Purchase`). DinMo sendet bei jeder Aktivierung nur neue Events und aktualisiert keine zuvor gesendeten Events.

Während der Aktivierungseinrichtung:

1. Geben Sie den Event-Namen genau so an, wie er in Braze erscheinen soll. Wenn das Event nicht existiert, erstellt DinMo es.
2. Ordnen Sie die erforderlichen Felder zu:
   * **Event-Zeitpunkt**: Zeitstempel, wann das Event aufgetreten ist
   * **Externe ID**: Externe ID der Nutzer:innen, die mit dem Event verknüpft sind
3. Ordnen Sie optionale Event-Eigenschaften den Braze-Attributnamen zu.
4. Legen Sie den Zeitplan fest, wie oft neue Events an Braze gesendet werden.

### Abo-Status synchronisieren {#synchronize-subscription-statuses}

Verwenden Sie diesen Zieldienst, um eine Braze-Abo-Gruppe mit einem DinMo-Segment oder -Modell abzugleichen.

Bevor Sie diesen Dienst aktivieren:

1. Erstellen Sie die Ziel-Abo-Gruppe (SMS oder E-Mail) in Braze.
2. Erstellen Sie ein DinMo-Modell oder -Segment mit den Nutzer:innen, die zu dieser Abo-Gruppe gehören sollen.

Geben Sie während der Aktivierungseinrichtung die genaue Abo-Gruppen-ID aus Braze ein. Um mehrere Abo-Gruppen zu synchronisieren, erstellen Sie eine Aktivierung pro Gruppe.

Wenn die Aktivierung ausgeführt wird:

* Wenn Nutzer:innen bereits in Braze vorhanden sind, werden Nutzer:innen, die dem DinMo-Segment beitreten, als abonniert für die Ziel-Abo-Gruppe markiert.
* Nutzer:innen, die das DinMo-Segment verlassen, werden als abgemeldet von der Abo-Gruppe markiert.

DinMo ändert keine Nutzer:innen, die nie Teil des Segments waren, und erstellt keine neuen Braze-Nutzer:innen in diesem Zieldienst.

### Nutzerlisten exportieren {#export-user-lists}

Verwenden Sie diesen Zieldienst, um ein DinMo-Segment als Braze-Nutzerattribut darzustellen. Aufgrund einer Braze-Einschränkung erstellt DinMo keine Braze-Liste direkt. Stattdessen setzt es ein Nutzerattribut auf `true` für Nutzer:innen im Segment und auf `false` für Nutzer:innen, die das Segment verlassen.

Geben Sie während der Aktivierungseinrichtung den Zielgruppennamen an. DinMo verwendet diesen Namen als Braze-Attribut (Leerzeichen werden durch Unterstriche ersetzt). Stellen Sie sicher, dass kein Attribut mit demselben Namen bereits in Braze existiert. Ordnen Sie das DinMo-Feld zu, das der externen ID der Nutzer:innen entspricht.

Erstellen Sie nach der Aktivierung ein Braze-Segment, das Nutzer:innen filtert, bei denen das synchronisierte Attribut gleich `true` ist.

Nur Nutzer:innen mit einer externen ID, die mit bestehenden Braze-Nutzer:innen übereinstimmt, werden aktualisiert. Dieser Zieldienst erstellt keine neuen Nutzer:innen.