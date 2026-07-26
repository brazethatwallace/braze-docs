---
nav_title: "Katalogsegmente"
article_title: "Katalogsegmente"
page_order: 0
page_type: reference
alias: "/catalog_segments/"
description: "Dieser Artikel beschreibt, wie Sie Katalogsegmente erstellen, die Katalogdaten in SQL-Segmenterweiterungen verwenden, um Zielgruppen von Nutzer:innen aufzubauen."
tool: Segments
---

# Katalogsegmente {#catalog-segments}

> Katalogsegmente sind eine Art von SQL-Segmenterweiterung, die durch die Kombination von Katalogdaten mit Daten aus angepassten Events oder Käufen erstellt werden. Sie können in einem Segment referenziert und dann von Campaigns und Canvases angesprochen werden.

Katalogsegmente verwenden SQL, um Daten aus Katalogen mit Daten aus angepassten Events oder Käufen zu verknüpfen. Dazu benötigen Sie ein gemeinsames Bezeichnerfeld in Ihren Katalogen und Ihren angepassten Events oder Käufen. Zum Beispiel muss der Wert einer Artikel-ID in einem Katalog mit dem Wert einer Eigenschaft in einem angepassten Event übereinstimmen.

## Ein Katalogsegment erstellen {#creating-a-catalog-segment}

1. Gehen Sie zu **Segmenterweiterungen** > **Neue Erweiterung erstellen** > **Mit Template starten** und wählen Sie ein Template aus. <br>![Modal mit der Option, ein Katalogsegment für Events, Käufe oder RFM-Segmente zu erstellen.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2. Der SQL-Editor wird automatisch mit einem Template befüllt. <br>![SQL-Editor mit einem vorgenerierten Template.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Dieses Template verknüpft Nutzer-Event-Daten mit Katalogdaten, um Nutzer:innen zu segmentieren, die mit bestimmten Katalogartikeln interagiert haben.

3. Verwenden Sie den Tab **Variablen**, um die erforderlichen Felder für Ihr Template bereitzustellen, bevor Sie Ihr Segment generieren. <br>Damit Braze Nutzer:innen anhand ihres Engagements mit Katalogartikeln identifizieren kann, müssen Sie Folgendes tun: <br> - Einen Katalog auswählen, der ein Katalogfeld enthält <br> - Ein angepasstes Event auswählen, das eine Event-Eigenschaft enthält <br> - Ihr Katalogfeld und die Werte der Event-Eigenschaft abgleichen

Hier sind Richtlinien zur Auswahl der Variablen:

| Variablenfeld | Beschreibung |
| --- | --- |
| `Catalog` | Der Name des Katalogs, den Sie verwenden, um Nutzer:innen anzusprechen. |
| `Catalog field` | Das Feld in Ihrem Katalog, das dieselben Werte wie Ihre `Custom event property` enthält. Dies ist oft eine Art von ID. Im E-Commerce-Anwendungsfall wäre dies `shopify_id`. |
| `Custom event` | Der Name Ihres angepassten Events, das dasselbe Event ist, das eine Eigenschaft mit Werten enthält, die mit Ihrem `Catalog field` übereinstimmen. Im E-Commerce-Anwendungsfall wäre dies `Made Order`. |
| `Custom event property` | Der Name Ihrer angepassten Event-Eigenschaft, die Werte mit Ihrem `Catalog field` abgleicht. Im E-Commerce-Beispiel wäre dies `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ein Katalogsegment erstellen" }

{: start="4"}
4. Füllen Sie bei Bedarf zusätzliche optionale Felder für Ihren Anwendungsfall aus, um nach einem bestimmten Feldwert innerhalb Ihres Katalogs zu segmentieren:
- `Catalog field`: Ein bestimmtes Feld (Spaltenname) innerhalb dieses Katalogs
- `Value`: Ein bestimmter Wert innerhalb dieses Felds oder dieser Spalte <br><br> Am Beispiel einer Gesundheits-App: Nehmen wir an, dass es innerhalb des Katalogs für jeden Arzt, den Sie buchen können, ein Feld namens `specialty` gibt, das einen Wert wie `vision` oder `dental` enthält. Um Nutzer:innen zu segmentieren, die einen Arzt mit dem Wert `dental` besucht haben, wählen Sie `specialty` als `Catalog field` und `dental` als `Value` aus.

5. Nach dem Erstellen einer SQL-Segmenterweiterung empfehlen wir, auf **Vorschau ausführen** zu klicken, um zu sehen, ob Ihre Abfrage Nutzer:innen zurückgibt oder ob Fehler vorliegen. Weitere Informationen zur [Vorschau von Abfrageergebnissen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-3-preview-the-query), zur Verwaltung von [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#managing-your-segment-extensions) und mehr finden Sie unter [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments).

{% alert note %}
Wenn Sie ein SQL-Segment erstellen, das die Tabelle `CATALOGS_ITEMS_SHARED` verwendet, müssen Sie eine Katalog-ID angeben. Zum Beispiel:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Feststellen, ob Sie SQL invertieren müssen {#determining-if-you-need-to-invert-sql}

Es ist zwar nicht möglich, direkt nach Nutzer:innen mit null Events zu suchen, aber Sie können **SQL invertieren** verwenden, um diese Nutzer:innen anzusprechen.

Um beispielsweise Nutzer:innen mit weniger als drei Käufen anzusprechen, schreiben Sie zunächst eine Abfrage, die Nutzer:innen mit drei oder mehr Käufen auswählt. Wählen Sie dann **SQL invertieren**, um Nutzer:innen mit weniger als drei Käufen anzusprechen (einschließlich derjenigen mit null Käufen).

![Segmenterweiterung mit dem Namen „1–4 E-Mails in den letzten 30 Tagen angeklickt“ mit der ausgewählten Option „SQL invertieren“.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
Sofern Sie nicht gezielt Nutzer:innen mit null Events ansprechen möchten, müssen Sie SQL nicht invertieren. Wenn **SQL invertieren** ausgewählt ist, bestätigen Sie, dass die Funktion benötigt wird und dass das Segment Ihrer gewünschten Zielgruppe entspricht. Wenn eine Abfrage beispielsweise Nutzer:innen mit mindestens einem Event anspricht, werden bei Invertierung nur Nutzer:innen mit null Events angesprochen.
{% endalert %}

## Segmentzugehörigkeit aktualisieren {#refreshing-segment-membership}

Um die Segmentzugehörigkeit eines Katalogsegments zu aktualisieren, öffnen Sie das Katalogsegment und wählen Sie **Aktionen** > **Aktualisieren** > **Ja, aktualisieren**.

{% alert tip %}
Wenn Sie ein Segment erstellt haben, bei dem Sie erwarten, dass Nutzer:innen regelmäßig ein- und austreten, aktualisieren Sie das verwendete Katalogsegment manuell, bevor Sie dieses Segment in einer Campaign oder einem Canvas ansprechen.
{% endalert %}

### Aktualisierungseinstellungen festlegen {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Anwendungsfälle {#use-cases}

{% tabs local %}
{% tab Gesundheit %}

### Gesundheits-App {#health-app}

Nehmen wir an, Sie haben eine Gesundheits-App und möchten Nutzer:innen segmentieren, die einen Zahnarztbesuch gebucht haben. Sie haben außerdem Folgendes:

- Einen Katalog `Doctors`, der die verschiedenen Ärzte enthält, die ein:e Patient:in buchen kann, jeweils mit einer `doctor ID` versehen
- Ein angepasstes Event `Booked Visit` mit einer `doctor ID`-Eigenschaft, die dieselben Werte wie das Feld `doctor ID` in Ihrem Katalog teilt
- Ein Feld `speciality` innerhalb Ihres Katalogs, das den Wert `dental` enthält

Sie würden ein Katalogsegment mit den folgenden Variablen einrichten:

| Variable | Eigenschaft |
| --- | --- |
| `Catalog` | Doctors |
| `Catalog field` | doctor ID |
| `Custom event` | Booked Visit |
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value` | Dental |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gesundheits-App" }

{% endtab %}
{% tab SaaS %}

### SaaS-Plattform {#saas-platform}

Nehmen wir an, Sie haben eine B2B-SaaS-Plattform und möchten Nutzer:innen segmentieren, die Mitarbeitende eines bestehenden Kunden sind. Sie haben außerdem Folgendes:

- Einen Katalog `Accounts`, der die verschiedenen Konten enthält, die derzeit Ihre SaaS-Plattform nutzen, jeweils mit einer `account ID` versehen
- Ein angepasstes Event `Event Attendance` mit einer `account ID`-Eigenschaft, die dieselben Werte wie das Feld `account ID` in Ihrem Katalog teilt
- Ein Feld `Classification` innerhalb Ihres Katalogs, das den Wert `enterprise` enthält

Sie würden ein Katalogsegment mit den folgenden Variablen einrichten:

| Variable | Eigenschaft |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field` | account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SaaS-Plattform" }

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen {#frequently-asked-questions}

### Verbraucht das Ausführen eines Katalogsegments SQL-Segmenterweiterungs-Credits? {#does-running-a-catalog-segment-consume-sql-segment-extension-credits}

Ja, Katalogsegmente werden von SQL betrieben und verbrauchen SQL-Segmenterweiterungs-Credits. Weitere Informationen finden Sie unter [Nutzung von SQL-Segmenten]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#credits).

### Verbraucht das Erstellen eines Katalogsegments SQL-Segmenterweiterungs-Kontingente? {#does-creating-a-catalog-segment-consume-sql-segment-extension-allotments}

Ja. Genauso wie SQL-Segmenterweiterungen auf Ihr Segmenterweiterungs-Kontingent angerechnet werden, zählen auch Katalogsegmente zu diesem Kontingent.

### Ich habe einen Anwendungsfall für Katalogsegmente, den das aktuelle Template nicht abdeckt. Wie sollte ich das einrichten? {#i-have-a-catalog-segment-use-case-that-the-current-template-doesnt-serve-how-should-i-set-that-up}

Kontaktieren Sie Ihre:n geschäftskunden-Support-Manager:in oder den [Braze-Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) für weitere Unterstützung.