---
nav_title: Splio
article_title: Splio
alias: /partners/splio/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Splio, mit der Sie gezieltere Kampagnen versenden, neue Produktchancen entdecken und den Umsatz steigern können."
page_type: partner
search_tag: Partner

---

# Splio

> [Splio](https://splio.com/) ist ein Tool zum Aufbau von Zielgruppen, mit dem Sie die Anzahl der Kampagnen und den Umsatz steigern können, ohne das Kundenerlebnis zu beeinträchtigen, und das Analytics zur Verfügung stellt, um die Performance von CRM-Kampagnen sowohl online als auch offline zu verfolgen.

Mit der Integration von Braze und Splio können Sie bessere CRM-Strategien planen und durchführen, gezieltere Kampagnen versenden, neue Produktchancen entdecken und Ihren Umsatz steigern.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Splio-Konto | Für diese Partnerschaft benötigen Sie ein Splio-Konto. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration von Datenimporten {#data-import-integration}

Um Braze und Splio zu integrieren, müssen Sie die Splio-Plattform konfigurieren, eine bestehende Splio-Kampagne exportieren und ein Kohorten-Segment in Braze erstellen, um Nutzer:innen in zukünftigen Kampagnen zu targetieren.

### 1. Schritt: Datenimport-Schlüssel für Braze abrufen {#step-1-get-the-braze-data-import-key}

Gehen Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Splio**.

Suchen Sie Ihren REST-Endpunkt und generieren Sie Ihren Datenimport-Schlüssel für Braze. Nachdem Sie den Schlüssel generiert haben, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.<br><br>![Die Technologie-Partnerseite von Splio mit dem REST-Endpunkt und dem Datenimport-Schlüssel.]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

Um die Integration abzuschließen, geben Sie den Datenimport-Schlüssel und den REST-Endpunkt an Ihr Splio-Data-Operations-Team weiter. Splio stellt die Verbindung her und kontaktiert Sie, nachdem die Einrichtung abgeschlossen ist.

### 2. Schritt: Kampagne aus der Splio-Plattform exportieren {#step-2-export-a-campaign-from-the-splio-platform}

Jedes Mal, wenn Sie in Braze eine Kohorte von Splio-Nutzer:innen erstellen möchten, müssen Sie diese zunächst aus der Splio-Plattform exportieren.

Wählen Sie in Splio die Kampagnen aus, die Sie exportieren möchten, und klicken Sie auf **Export Campaigns**. Nach dem Export wird die Zielgruppe automatisch in Ihr Braze-Konto hochgeladen.

![Exportieren von Kampagnen aus der Splio-Plattform.]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### 3. Schritt: Segment aus der angepassten Splio-Zielgruppe erstellen {#step-3-create-a-segment-from-the-splio-custom-audience}

Navigieren Sie in Braze zu **Segments**, benennen Sie Ihr Splio-Kohorten-Segment und wählen Sie **Splio Cohorts** als Filter. Wählen Sie von hier aus, welche Splio-Kohorte Sie einbeziehen möchten. Nachdem Sie Ihr Splio-Kohorten-Segment erstellt haben, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Campaign oder ein Canvas erstellen.

![Erstellen eines Splio-Kohorten-Segments in Braze.]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![Im Braze-Segment-Builder ist der Nutzerattribut-Filter „Splio cohort“ auf „includes“ und „Primary cohort“ eingestellt.]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Haben Sie Schwierigkeiten, Ihre Kohorte zu finden? Schauen Sie im Abschnitt [Fehlerbehebung](#troubleshooting) nach.

{% alert important %}
Es werden nur Nutzer:innen aus einer Kohorte hinzugefügt oder entfernt, die bereits in Braze existieren. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

## Verwendung dieser Integration {#using-this-integration}

Um Ihr Splio-Segment zu verwenden, erstellen Sie eine Braze-Campaign oder ein Canvas und wählen Sie das Segment als Ihre Zielgruppe aus.

![Im Braze-Campaign-Builder ist im Targeting-Schritt der Filter „Zielgruppen nach Segment zusammenstellen“ auf „Splio cohort“ eingestellt.]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Nutzer:innen-Zuordnung {#user-matching}

Braze ordnet identifizierte Nutzer:innen anhand ihrer `external_id` oder `alias` zu. Anonyme Nutzer:innen werden anhand ihrer `device_id` zugeordnet. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` abgeglichen werden, sondern müssen über ihre `external_id` oder `alias` abgeglichen werden.

## Fehlerbehebung {#troubleshooting}

Wenn Sie die richtige Kohorte in der Liste nicht finden können, sehen Sie sich die Details Ihrer Kampagne in Splio an und überprüfen Sie den Namen, indem Sie den **Export File Name** prüfen.

![Unten auf der Detailseite der Kampagne wird der Name Ihrer Kohorte angezeigt.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

Wenn Sie Probleme haben, Ihre Zielgruppe abzurufen, wenden Sie sich an das [Splio-Team](mailto:support-team@splio.com), um Unterstützung zu erhalten.