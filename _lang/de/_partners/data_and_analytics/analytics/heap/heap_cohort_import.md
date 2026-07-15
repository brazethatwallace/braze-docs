---
nav_title: Heap - Kohortenimport
article_title: Heap - Kohortenimport
description: "Dieser Referenzartikel beschreibt die Integration zwischen Braze und Heap, einer Plattform für digitale Insights, die es Ihnen ermöglicht, Heap-Daten in Braze zu importieren, Nutzer:innen-Kohorten zu erstellen sowie Braze-Daten in Heap zu exportieren, um Segmente zu erstellen."
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Heap - Kohortenimport {#heap-cohort-import}

> [Heap](https://heap.io/), eine Plattform für digitale Insights, konzentriert sich auf die Chancen in Ihrem digitalen Erlebnis, die sich am stärksten auf Ihr Geschäft auswirken, indem sie Reibungsverluste beseitigt, Ihre Kund:innen begeistert und Ihren Umsatz beschleunigt.

Die Integration von Braze und Heap ermöglicht Ihnen den [Import von Heap-Daten in Braze](#data-import-integration), die Erstellung von Nutzer:innen-Kohorten sowie den [Export von Braze-Daten in Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap), um Segmente zu erstellen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Heap-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Heap-Konto](https://heap.io/about). |
| Braze-Datenimport-Schlüssel | Diesen finden Sie im Braze-Dashboard unter **Partnerintegrationen** > **Technologie-Partner**. Wählen Sie dort **Heap** aus. |
| Braze-REST-Endpunkt | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze-Currents | Um Daten von Braze nach Heap zu exportieren, müssen [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) in Ihrem Konto aktiviert sein. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}
- Erneute Interaktion mit Nutzer:innen, die einen Funnel verlassen haben: Triggern Sie erneute Interaktionsnachrichten, wenn Nutzer:innen den Kauf- oder Abo-Funnel abbrechen.
- Personalisieren Sie das Testerlebnis: Identifizieren Sie Reibungspunkte in Ihrer Testphase und senden Sie zeitlich passende Erinnerungen, um Nutzer:innen während einer Testphase erneut zu aktivieren und ihnen zu helfen, einen Mehrwert zu erzielen.
- Steigern Sie das Engagement bei Ankündigungen und Angeboten: Richten Sie Aktionen, Updates und Ankündigungen neuer Dienste gezielt an die relevanten Zielgruppen.

## Integration von Datenimporten {#data-import-integration}

Verwenden Sie die Heap-zu-Braze-Integration, um Kohorten, die in Heap definiert sind, automatisch mit Braze zu synchronisieren.

### Schritt 1: Braze-Datenimport-Schlüssel abrufen {#step-1-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie dann **Heap** aus.

Auf dieser Seite finden Sie Ihren Datenimport-Schlüssel und einen REST-Endpunkt. Notieren Sie sich diese beiden Werte und geben Sie sie an Ihren Heap Account Manager weiter, um die Einrichtung der Integration abzuschließen.

![Braze-Technologie-Partnerseite für Heap mit Datenimport-Schlüssel und Endpunkt.]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### Schritt 2: Importierte Nutzer:innen in Braze segmentieren {#step-2-segment-imported-users-in-braze}

Navigieren Sie in Braze zu **Segments**, benennen Sie Ihr Heap-Kohorten-Segment und wählen Sie **Heap Cohorts** als Filter. Von hier aus können Sie auswählen, welche Heap-Kohorte Sie einbeziehen möchten. Nachdem Ihr Heap-Kohorten-Segment erstellt wurde, können Sie es als Zielgruppenfilter auswählen, wenn Sie eine Campaign oder ein Canvas erstellen.

![Im Braze-Segment-Builder ist der Nutzerattribut-Filter „Heap cohort“ auf „includes“ und „Heap Test Cohort“ gesetzt.]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### Verwendung dieser Integration {#using-this-integration}

Um Ihr Heap-Segment zu verwenden, erstellen Sie eine Braze-Campaign oder ein Canvas und wählen Sie das Segment als Ihre Zielgruppe aus.

![Im Braze-Campaign-Builder ist im Targeting-Schritt der Filter „Zielgruppen nach Segment zusammenstellen“ auf „Heap cohort“ gesetzt.]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Nur Nutzer:innen, die bereits in Braze vorhanden sind, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

## Details zur Integration {#integration-details}

Die Payload-Struktur für exportierte Daten entspricht der Payload-Struktur für angepasste HTTP-Konnektoren, die im [Beispiel-Repository für angepasste HTTP-Konnektoren](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors) eingesehen werden kann.

## Nutzer:innen-Abgleich {#user-matching}

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder ihren `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` abgeglichen werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder ihren `alias` identifiziert werden.