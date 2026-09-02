---
nav_title: Kubit
article_title: Kubit-Kohortenimport
description: "Dieser Artikel beschreibt die Kohortenimport-Funktionalität von Kubit, einer no-code, self-service Analytics-Plattform, die sofortige Produkt-Insights liefert und es Ihnen erlaubt, Kubit-Nutzer:innen-Kohorten zu importieren und sie im Messaging von Braze anzusprechen."
page_type: partner
search_tag: Partner
---

# Kubit-Kohortenimport {#kubit-cohort-import}

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten aus [Kubit](https://kubit.ai/) nach Braze importieren. Weitere Informationen zur Integration von Kubit und seinen anderen Funktionalitäten finden Sie im [Hauptartikel zu Kubit]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit).

## Integration von Datenimporten {#data-import-integration}

### Schritt 1: Datenimport-Schlüssel für Braze abrufen {#step-1-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Kubit** aus. Hier finden Sie den Representational State Transfer-Endpunkt und können Ihren Datenimport-Schlüssel für Braze generieren.

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der Representational State Transfer-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Kubit einrichten.

![Die Technologie-Partnerseite von Kubit in Braze.]({% image_buster /assets/img/kubit/kubit.png %}){: style="max-width:90%;"}

### Schritt 2: Braze in Kubit konfigurieren {#step-2-configure-braze-in-kubit}

Geben Sie den Datenimport-Schlüssel und den Braze-Representational State Transfer-Endpunkt an Ihren Kubit-Supportkontakt weiter. Dieser wird die Integration auf seiner Seite konfigurieren und Sie informieren, sobald die Integration aktiv ist.

### Schritt 3: Kohorten nach Braze importieren {#step-3-import-cohorts-to-braze}

#### Kohorte in Kubit erstellen {#create-a-cohort-in-kubit}
[Erstellen Sie eine Kohorte](https://www.kubit.ai/doc/fundamentals#cohort) in Kubit und definieren Sie die Kriterien Ihrer Zielnutzer:innen.<br><br>![Kubit-Kohorten-Builder mit konfigurierten Zielnutzer:innen-Kriterien.]({% image_buster /assets/img/kubit/create_cohort.png %}){: style="max-width:80%;"}

#### Nutzer:innen nach Braze importieren {#import-users-to-braze}
Sobald Sie Ihre Kohorte gespeichert haben, können Sie sie nach Braze importieren, um sie in Braze-Segmenten zu verwenden. Diese Segmente können dann zur Erstellung gezielter E-Mail- oder Push-Campaigns und Canvase verwendet werden.

Navigieren Sie dazu zu Ihrer bestehenden Kohorte und wählen Sie unter **Cohort Control** die Option **Import to Braze**.

![Kubit-Menü „Cohort Control“ mit ausgewählter Option „Import to Braze“.]({% image_buster /assets/img/kubit/import_to_braze.png %}){: style="max-width:80%;"}

Wählen Sie anschließend die gewünschte Importkadenz aus. Einmalige Importe ermöglichen es Ihnen, sofort einmal zu importieren. Geplante Importe erlauben tägliche, wöchentliche oder monatliche Importe zu einer bestimmten Uhrzeit. Beachten Sie, dass jede Kohorte nur einen aktiven Importzeitplan haben kann.

![Kubit-Importzeitplan-Einstellungen mit Kadenzoptionen für Braze-Importe.]({% image_buster /assets/img/kubit/import_schedule.png %}){: style="max-width:40%;"}

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

#### Importstatus überprüfen {#verify-import-status}
Sobald ein Import abgeschlossen ist, wird eine E-Mail-Benachrichtigung an die im Importzeitplan angegebenen Empfänger:innen gesendet. Sie können den Importstatus einer Kohorte auch unter **Schedule** in Kubit überprüfen. Der Zeitplanverlauf zeigt die Ausführungszeit jedes Imports, das Ergebnis und die Gesamtzahl der Nutzer:innen in der Kohorte, die nach Braze importiert wurden.<br><br>![Kubit-Zeitplanverlauf mit Import-Ausführungszeiten, Ergebnissen und Anzahl importierter Nutzer:innen.]({% image_buster /assets/img/kubit/import_history.png %})<br><br>Sie können einen Import manuell triggern, indem Sie auf das Symbol **Import to Braze** für den jeweiligen Importzeitplan klicken.

### Schritt 4: Braze-Segmente mit Kubit-Kohorten erstellen {#step-4-create-braze-segments-with-kubit-cohorts}
Nachdem Sie Kohorten nach Braze importiert haben, können Sie diese als Filter verwenden, um Braze-Segmente zu erstellen und sie in Braze-Campaigns oder Canvase einzubinden. Besuchen Sie unsere Dokumentation zu Segmenten, um mehr darüber zu erfahren, [wie Sie Braze-Segmente erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#step-4-add-filters-to-your-segment).

![Im Braze-Segment-Builder ist das Nutzerattribut „Kubit cohorts“ auf „includes_value“ gesetzt und zeigt eine Liste der verfügbaren Kohorten an.]({% image_buster /assets/img/kubit/segment_with_kubit_cohorts.png %}){: style="max-width:70%;"}

## Nutzer:innen-Abgleich {#user-matching}

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` abgeglichen werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.