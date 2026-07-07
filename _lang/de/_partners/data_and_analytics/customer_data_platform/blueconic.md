---
nav_title: BlueConic
article_title: BlueConic
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und BlueConic, einer führenden Pure-Play Customer Data Platform, die es Ihnen ermöglicht, Daten in persistenten, individuellen Profilen zu vereinheitlichen und sie dann über einen Amazon Web Services S3-Server für Importziele zwischen den beiden Systemen zu synchronisieren."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic](https://www.blueconic.com/), die führende Pure-Play Customer Data Platform, befreit die First-Party-Daten von Unternehmen aus unterschiedlichen Systemen und macht sie zugänglich, wo und wann immer sie benötigt werden, um Kundenbeziehungen zu transformieren und das Geschäftswachstum zu fördern.

_Diese Integration wird von Blueconic gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und BlueConic ermöglicht es Nutzer:innen, Daten in persistenten, individuellen Profilen zu vereinheitlichen und sie dann über einen Amazon Web Services S3-Server für Importziele zwischen den beiden Systemen zu synchronisieren. Zu den möglichen Zielen gehören wachstumsorientierte Initiativen, Orchestrierung des Kundenlebenszyklus, Modellierung und Analytics, digitale Produkte und Erlebnisse, zielgruppenbasierte Monetarisierung und vieles mehr. Diese Integration unterstützt sowohl den geplanten Batch-Import als auch den Export.

{% alert important %}
Wenn Sie die Integration verwenden, sendet BlueConic bei jeder Synchronisierung Deltas (sich ändernde Daten). Dazu gehören alle Profile, die sich seit dem letzten Senden geändert haben, sowie alle Attribute dieses Profils. Überwachen Sie die Datenpunkt-Nutzung entsprechend.
{% endalert %}

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| --- | --- |
| BlueConic-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [BlueConic-Konto](https://www.blueconic.com/). Um auf die Plugins zugreifen zu können, benötigen Sie in Ihrem BlueConic-Konto einen Zugang zum [Anzeigen und Bearbeiten von Verbindungen](https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles). |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit den Berechtigungen `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists` und `segments.details`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz](https://portal.aws.amazon.com/billing/signup#/start) ab. |
| S3-Authentifizierung | Zum Exportieren und Importieren der Daten benötigen Sie Zugang zu einem Amazon Web Services (S3)-Server. |
| ID des Zugriffsschlüssels<br>Geheimer Zugriffsschlüssel | Die ID des Zugriffsschlüssels und der geheime Zugriffsschlüssel ermöglichen Ihnen die Authentifizierung Ihres S3-Servers für den Import und Export. |
| AWS-Bucket | Sie müssen innerhalb des Plugins eine Verbindung zu S3 herstellen. Nach der Authentifizierung werden die verfügbaren Buckets in einem Dropdown-Menü angezeigt. Hier werden die zu importierenden oder zu exportierenden Dateien gespeichert. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### 1. Schritt: Erstellen einer Braze-Verbindung {#step-1-creating-a-braze-connection}

Wählen Sie in BlueConic in der Navigationsleiste **Connections** aus und dann **Add Connection**. Suchen Sie in der daraufhin angezeigten Eingabeaufforderung nach **Braze** und wählen Sie **Braze connection** aus.

Erweitern oder reduzieren Sie die verfügbaren Metadatenfelder in der Verbindung, indem Sie auf das graue Chevron-Symbol klicken. In diesen Feldern können Sie diese Verbindung favorisieren, ihr einen Namen geben, Beschriftungen hinzufügen, eine Beschreibung einfügen und festlegen, dass Sie per E-Mail benachrichtigt werden, wenn die Verbindung [läuft oder nicht läuft](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ).

Speichern Sie Ihre Einstellungen.

### 2. Schritt: Konfigurieren einer Braze-Verbindung {#step-2-configuring-a-braze-connection}

Um die Verbindung zwischen BlueConic und Braze zu konfigurieren, müssen Sie die Zugangsdaten Ihres Braze-Kontos und die Daten Ihres Amazon Web Services (S3)-Kontos hinzufügen, um die Verbindung zu authentifizieren.

1. Wählen Sie in BlueConic im linken Panel im Bereich **Setup** die Option **Set up and run**.<br><br>
2. Geben Sie auf der sich öffnenden Braze-Authentifizierungsseite Ihren Braze REST-API-Endpunkt und Ihren Braze-API-Schlüssel ein.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. Im Abschnitt S3-Einrichtung und Authentifizierung geben Sie diese Zugangsdaten ein: Amazon Web Services (S3) ID des Zugriffsschlüssels, geheimer Zugriffsschlüssel und S3-Bucket. Es müssen [dieselben Zugangsdaten]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) sein, die Sie bei der Einrichtung Ihrer Braze- und Amazon S3-Integration konfiguriert haben. Speichern Sie Ihre Einstellungen. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### 3. Schritt: Erstellen von Import- oder Exportzielen (Import-Abbildung) {#step-3-creating-import-or-export-goals-import-mapping}

Sobald die Authentifizierung abgeschlossen ist, müssen Sie mindestens ein Import- oder Exportziel erstellen, die Verbindung einschalten und die Verbindung planen oder ausführen.

{% tabs %}
{% tab Import %}

1. Wählen Sie im linken Panel **Import data into BlueConic**, um die Konfigurationsseite für Braze-Daten zu öffnen.<br><br>
2. Wählen Sie den Speicherort der Daten in Braze aus. Hier können Sie BlueConic mitteilen, wo die zu importierenden Daten zu finden sind, indem Sie Ihre Braze-Zielgruppe auswählen.<br>![Die BlueConic-Braze-Zielgruppe ist auf „BlueConic Test Users“ eingestellt.]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Als Nächstes bilden Sie Bezeichner zwischen Braze und BlueConic ab. <br>![Das Braze-Feld „External ID“ ist so eingestellt, dass es auf das BlueConic-Feld „Braze external ID“ abgebildet wird.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Um die Kundendaten zwischen den beiden Systemen zu verknüpfen, geben Sie einen oder mehrere Bezeichner für Kund:innen ein.<br>Verwenden Sie das Kontrollkästchen **Allow creation...**, um BlueConic zu erlauben, neue Profile für Daten zu erstellen, die nicht zu einem bestehenden BlueConic-Profil passen.<br><br>
4. Als Nächstes stimmen Sie die BlueConic-Datenfelder, die Sie exportieren, mit den Braze-Feldern ab. Verwenden Sie die Dropdown-Felder, um entweder den BlueConic-Profilbezeichner oder eine Profileigenschaft auf der linken Seite auszuwählen, und wählen Sie den entsprechenden Braze-Profilbezeichner aus. Verwenden Sie als Nächstes das Dropdown-Menü, um festzulegen, wie importierte Inhalte zu den vorhandenen Werten hinzugefügt werden sollen: addiert, summiert, nur gesetzt, wenn die Profileigenschaft leer ist, oder auf Löschen gesetzt (wenn das Braze-Feld leer ist).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Verwenden Sie den Button **Add Mapping**, um bei Bedarf weitere Abbildungszeilen zu erstellen. Mit der Option **Add remaining fields** können Sie mehrere Abbildungszeilen hinzufügen. BlueConic erkennt die übrigen Braze-Felder und gleicht sie mit den BlueConic-Profileigenschaften ab. Sie können die Zusammenführungsstrategie für Importe festlegen (setzen, hinzufügen, summieren, setzen wenn leer oder löschen) und ein angepasstes Präfix für die Namen der BlueConic-Profileigenschaften angeben.<br><br>
5. Wählen Sie abschließend **Run the connection**, um die Verbindung zu starten. Besuchen Sie [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections), um mehr über den Zeitplan und die Ausführung von Verbindungen zu erfahren.
{% endtab %}
{% tab Export %}

1. Wählen Sie im linken Panel **Export data to Braze** aus, um Ihren Datenexport von BlueConic nach Braze zu konfigurieren.<br><br>
2. Wählen Sie ein BlueConic-Segment für den Export. Es werden nur Profile in diesem Segment mit übereinstimmenden Bezeichnern in Braze exportiert.<br>![Ein BlueConic-Segment mit 20.000 Profilen.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. Als Nächstes verknüpfen Sie Bezeichner zwischen BlueConic-Profilen und Braze-Feldern. Sie können optional festlegen, dass BlueConic neue Datensätze anlegen soll, wenn keine Übereinstimmung gefunden wird.<br>![Das Braze-Feld „External ID“ ist so eingestellt, dass es auf das BlueConic-Feld „Braze external ID“ abgebildet wird.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. Als Nächstes stimmen Sie die BlueConic-Datenfelder, die Sie exportieren, mit den Braze-Feldern ab. Verwenden Sie das Dropdown-Menü des BlueConic-Symbols, um die Art der [Informationen](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) zu wählen, die Sie exportieren möchten. Zu den verfügbaren Informationen gehören Profileigenschaften, BlueConic-Profilbezeichner, zugehörige Segmente, alle angesehenen Interaktionen, Berechtigungsstufen und ein statischer Textwert.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Klicken Sie abschließend auf **Run the connection**, um die Verbindung zu starten. Besuchen Sie [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections), um mehr über den Zeitplan und die Ausführung von Verbindungen zu erfahren.
{% endtab %}
{% endtabs %}

## 4. Schritt: Verbindung umschalten {#step-4-toggle-connection-on}

Verwenden Sie den Kippschalter neben dem Titel der Braze-Verbindung, um die Verbindung ein- und auszuschalten. Eine Verbindung muss eingeschaltet sein, um zu den geplanten Zeiten ausgeführt zu werden.