---
nav_title: Mixpanel
article_title: Mixpanel-Kohortenimport
description: "Dieser Referenzartikel beschreibt die Kohortenimport-Funktionalität von Mixpanel, einer Business-Analytics-Plattform, mit der Sie Mixpanel-Kohorten in Braze importieren können, um Braze-Segmente zu erstellen, die für das Targeting von Nutzer:innen in zukünftigen Braze-Campaigns oder Canvases verwendet werden können."
page_type: partner
search_tag: Partner
---

# Mixpanel-Kohortenimport {#mixpanel-cohort-import}

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten von [Mixpanel](https://mixpanel.com/) nach Braze importieren. Weitere Informationen zur Integration von Mixpanel und seinen anderen Funktionen finden Sie im [Hauptartikel über Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel).

## Integration von Datenimporten {#data-import-integration}

Wenn Sie eine Kohorte von Mixpanel mit Braze synchronisieren, empfängt Braze Aktualisierungen der Kohortenmitgliedschaft für Nutzer:innen, die Mixpanel bestehenden Braze-Profilen zuordnen kann. Nach einer Synchronisierung können Sie diese Nutzer:innen mit dem Segment-Filter **Mixpanel cohorts** ansprechen.

Die Kohortensynchronisierung importiert keine Mixpanel-Ereignisse, Mixpanel-Nutzer:inneneigenschaften oder angepasste Attribute in Braze. Das Konnektor-Verhalten, einschließlich der Synchronisierungsfrequenz, wird in Mixpanel gesteuert. Einzelheiten zur Einrichtung finden Sie in der [Mixpanel-Dokumentation zur Braze-Kohortensynchronisierung](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze). Informationen zu den Anforderungen für den Nutzer:innen-Abgleich finden Sie unter [Nutzer:innen-Abgleich](#user-matching).

Jede Integration, die Sie einrichten, protokolliert Datenpunkte. Wenn Sie Fragen zu den Feinheiten der Braze-Datenpunkte haben, kann Ihr Braze Account Manager:in diese beantworten.

{% alert important %}
In Übereinstimmung mit den Richtlinien von Mixpanel zur Datenaufbewahrung werden Ereignisse, die vor dem 1. Januar 2010 gesendet wurden, beim Import entfernt.
{% endalert %}

### Schritt 1: Braze-Datenimport-Schlüssel abrufen {#step-1-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Mixpanel** aus. Hier finden Sie den REST-Endpunkt und können Ihren Braze-Datenimport-Schlüssel generieren.

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Mixpanel einrichten.<br><br>![Braze-Mixpanel-Technologie-Partnerseite mit Datenimport-Schlüssel und Endpunkt.]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Schritt 2: Braze-Integration in Mixpanel einrichten {#step-2-set-up-the-braze-integration-in-mixpanel}

1. Navigieren Sie in Mixpanel zu **Data Management > Integrations.**
2. Wählen Sie den Tab für die Braze-Integration aus und klicken Sie auf **Connect**.
3. Geben Sie in der daraufhin angezeigten Aufforderung den Braze-Datenimport-Schlüssel und den REST-Endpunkt an.
4. Klicken Sie auf **Continue**.

![Mixpanel-Braze-Integrations-Setup-Modal mit Schlüssel- und Endpunkt-Feldern.]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Schritt 3: Mixpanel-Kohorte nach Braze exportieren {#step-3-export-a-mixpanel-cohort-to-braze}

Navigieren Sie in Mixpanel zu **Data Management > Cohorts**. Wählen Sie die Kohorte aus, die Sie an Braze senden möchten, und klicken Sie dann auf **Export to Braze**. Wählen Sie abschließend eine einmalige oder dynamische Synchronisierung aus. Bei der dynamischen Synchronisierung wird die Kohorte nach einem wiederkehrenden Zeitplan aktualisiert, der von Mixpanel gesteuert wird. Die aktuelle Synchronisierungsfrequenz finden Sie in der [Mixpanel-Dokumentation zur Braze-Kohortensynchronisierung](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).

![Mixpanel-Kohortenexport-Ablauf mit den Synchronisierungsoptionen für „Export to Braze“.]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

### Schritt 4: Nutzer:innen in Braze segmentieren {#step-4-segment-users-in-braze}

Um in Braze ein Segment für diese Nutzer:innen zu erstellen, gehen Sie zu **Zielgruppe** > **Segmente**, benennen Sie Ihr Segment und wählen Sie **Mixpanel_Cohorts** als Filter. Verwenden Sie anschließend die Option „enthält“ und wählen Sie die Kohorte, die Sie in Mixpanel erstellt haben.

![Im Braze-Segment-Builder ist der Nutzer:innen-Attribut-Filter „Mixpanel cohorts“ auf „enthält“ und „Braze cohort“ eingestellt.]({% image_buster /assets/img_archive/mixpanel1.png %})

Nach dem Speichern können Sie dieses Segment bei der Erstellung von Canvases oder Campaigns im Schritt „Zielgruppe zusammenstellen“ referenzieren.

## Nutzer:innen-Abgleich {#user-matching}

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder ihren `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` abgeglichen werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder ihren `alias` identifiziert werden.

## Fehlerbehebung {#troubleshooting}

Wenn eine Mixpanel-Kohortensynchronisierung unvollständig erscheint oder für bestimmte Nutzer:innen nicht aktualisiert wird, lesen Sie den Abschnitt [Fehlerbehebung]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel#troubleshooting) im Hauptartikel über Mixpanel.

Konnektor-spezifische Schritte und Synchronisierungsfrequenzen finden Sie in der [Mixpanel-Dokumentation zur Braze-Kohortensynchronisierung](https://docs.mixpanel.com/docs/cohort-sync/integrations/braze).