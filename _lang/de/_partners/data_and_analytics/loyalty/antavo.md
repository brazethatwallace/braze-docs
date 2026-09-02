---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Antavo, einem Kundenbindungs-Programm der nächsten Generation, das über die Belohnung von Käufen hinausgeht."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [Antavo](https://antavo.com/) ist ein Anbieter von SaaS-Technologien zur Kundenbindung auf Unternehmensebene, der umfassende Kundenbindungs-Programme entwickelt, um die Markenliebe zu fördern und das Kundenverhalten zu verändern.

_Diese Integration wird von Antavo gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Antavo und Braze ermöglicht es Ihnen, Daten aus Kundenbindungs-Programmen zu nutzen, um personalisierte Campaigns zu erstellen und so das Kundenerlebnis zu verbessern. Antavo unterstützt die Synchronisierung von Treuedaten zwischen den beiden Plattformen – es handelt sich dabei um eine einseitige Datensynchronisierung, ausschließlich von Antavo zu Braze. Die Integration unterstützt das Braze-Feld `external_id`, das Antavo zur Synchronisierung der ID des Treue-Mitglieds verwendet.

## Voraussetzungen {#prerequisites}

| Anforderung          | Beschreibung                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Antavo-Konto       | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Antavo-Konto](https://antavo.com/) mit aktivierter Braze-Integration.                                                |
| Braze REST-API-Schlüssel   | Ein Braze REST-API-Schlüssel mit den folgenden Berechtigungen: `users.track`, `events.list`, `events.data_series` und `events.get`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.  |
| Braze REST-Endpunkt  | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                |
| Braze-App-Bezeichner | Ihr App-Bezeichner-Schlüssel. <br><br>Um diesen Schlüssel im Braze-Dashboard zu finden, gehen Sie zu **Einstellungen** > **API-Schlüssel** und suchen Sie den Abschnitt **Identification**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Braze in Antavo verbinden {#step-1-connect-braze-in-antavo}

Gehen Sie in Antavo zu **Modules** > **Braze** und klicken Sie auf **Configure**. Wenn Sie zum ersten Mal die Konfigurationsseite für die Braze-Integration in Antavo aufrufen, werden Sie über die Schnittstelle aufgefordert, die beiden Systeme miteinander zu verbinden.

Geben Sie die folgenden Zugangsdaten an:

- **Instance URL:** Der Braze REST-Endpunkt der Instanz, für die Sie bereitgestellt werden.
- **API Token / Textbaustein (Identifier):** Der Braze REST-API-Schlüssel, den Antavo beim Senden von Anfragen an Braze verwenden soll.
- **App Identifier:** Der Braze-App-Bezeichner.

Nachdem Sie die Zugangsdaten eingegeben haben, klicken Sie auf **Connect**.

![Braze-Verbindungsbildschirm in Antavo mit Instanz-URL, API-Token und App-Bezeichner.]({% image_buster /assets/img/antavo/connect_braze.png %})

### 2. Schritt: Feld-Abbildung konfigurieren {#step-2-configure-field-mapping}

Nachdem die Verbindung hergestellt wurde, werden Sie in Antavo automatisch zur Seite **Sync Fields** weitergeleitet, um die Feldsynchronisierung zwischen den beiden Systemen zu konfigurieren.   Sie können diese Seite jederzeit über **Modules** > **Braze** erreichen.

So konfigurieren Sie die Feld-Abbildung in Antavo:

1. Klicken Sie auf **Add new field** <i class="fas fa-plus" alt=""></i>.
2. Wählen Sie aus dem Dropdown-Feld das Antavo **Loyalty field** aus, das Sie mit Braze synchronisieren möchten.
3. Geben Sie das **Remote field** ein, das das entsprechende angepasste Attribut in Braze darstellt, in das die Daten eingefügt werden sollen.

{% alert note %}
Sie finden Ihre Liste der angepassten Attribute in Braze unter **Dateneinstellungen** > **Angepasste Attribute**. Wenn das von Ihnen eingegebene Feld nicht in Braze definiert ist, wird bei der ersten Synchronisierung automatisch ein neues Feld erzeugt.
{% endalert %}

{:start="4"}
4. Um weitere Feldpaarungen hinzuzufügen, wiederholen Sie die Schritte 1–3.
5. Um ein Feld aus der Liste der synchronisierten Daten zu entfernen, klicken Sie auf <i class="fa-solid fa-rectangle-xmark" title="Löschen"></i> am Ende der Zeile.
6. Klicken Sie auf **Save**.

Wenn sich ein Wert der konfigurierten Felder in Antavo ändert, wird nicht nur die Synchronisierung dieses einzelnen Wertes ausgelöst, sondern jedes Feld, das der Feld-Abbildung hinzugefügt wurde, wird in die Anfrage aufgenommen.

![Seite „Sync Fields“ in Antavo.]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
Um die Datenpunkt-Nutzung zu minimieren, empfehlen wir, nur die Felder abzubilden, die in Braze tatsächlich verwendet werden sollen.
{% endalert %}

#### Unterstützte Datentypen {#supported-data-types}

Die Integration unterstützt alle [Datentypen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) für angepasste Braze-Attribute, nämlich: Zahl (Integer, Gleitkommazahl), String, Array, Boolescher Wert, Objekt, Objekt-Array und Datum.

![Braze-Profil mit verschiedenen angepassten Attributen.]({% image_buster /assets/img/antavo/braze_profile.png %})

Die Datenfelder werden auf Grundlage der konfigurierten Feld-Abbildung ausgefüllt.

## Trigger {#triggers}

Neben der Konfiguration der Feld-Abbildung bietet die Integration weitere Möglichkeiten durch Features, die in Antavos [Workflows](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629)-Tool integriert sind. Alle [Datentypen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) für angepasste Braze-Attribute und [Datentypen für Event-Eigenschaften]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#event-property-data-types) angepasster Events können ebenfalls über Workflows synchronisiert werden.

### Gelegentliches Synchronisieren von Treuedaten {#synchronizing-loyalty-data-occasionally}

Verwenden Sie diese Option, wenn die Daten nicht in Treuefeldern in Antavo gespeichert sind oder wenn die Daten nicht zur Liste der abgebildeten Felder hinzugefügt werden. Die Synchronisierung der angefragten Daten wird ausgelöst, wenn die konfigurierten Workflow-Kriterien erfüllt sind.

Besuchen Sie die Schritt-für-Schritt-Anleitung, um zu erfahren, wie Sie die Synchronisierung von [Treuedaten in Bezug auf den letzten Kauf](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase) konfigurieren.

### Synchronisierung von Events des Kundenbindungs-Programms {#synchronizing-loyalty-program-events}

Verwenden Sie von Antavo synchronisierte Events, um Treue-Mitglieder in aktionsbasierte Braze Canvases einzutragen. Die Integration kann alle Antavo-Events (einschließlich Kauf-Events) synchronisieren, die in Braze als angepasste Events erscheinen.

Besuchen Sie die Schritt-für-Schritt-Anleitung, um zu erfahren, wie Sie die Synchronisierung des [Anmelde-Events für das Kundenbindungs-Programm](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) und die Synchronisierung des [Events für das Sammeln von Vorteilen im Kundenbindungs-Programm](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) konfigurieren.