---
nav_title: Amplitude
article_title: Amplitude-Kohortenimport
description: "Dieser Referenzartikel beschreibt die Kohortenimport-Funktionalität von Amplitude, einer Plattform für Produktanalysen und Business-Intelligence."
page_type: partner
search_tag: Partner
---

# Amplitude-Kohortenimport {#amplitude-cohort-import}

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten von [Amplitude](https://amplitude.com/) nach Braze importieren können. Weitere Informationen zur Integration von Amplitude und seinen anderen Funktionen finden Sie im [Hauptartikel zu Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences).

## Datenimport-Integration {#data-import-integration}

Jede Integration, die Sie einrichten, wird auf das Datenpunktvolumen Ihres Kontos angerechnet.

### Schritt 1: Braze-Datenimport-Schlüssel abrufen {#step-1-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Amplitude** aus. Dort finden Sie den Representational State Transfer-Endpunkt und können Ihren Braze-Datenimport-Schlüssel generieren.

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie einen Postback im Dashboard von Amplitude einrichten.<br><br>![Braze-Technologie-Partnerseite für Amplitude mit Datenimport-Schlüssel und Endpunkt.]({% image_buster /assets/img/amplitude3.png %})

### Schritt 2: Braze-Integration in Amplitude einrichten {#step-2-set-up-the-braze-integration-in-amplitude}

Navigieren Sie in Amplitude zu **Sources & Destinations** > **[Projektname]** > **Destinations** > **Braze**. Geben Sie in der angezeigten Eingabeaufforderung den Braze-Datenimport-Schlüssel und den Representational State Transfer-Endpunkt ein und klicken Sie auf **Save**.

![Amplitude-Zieleinstellungen für die Braze-Kohortensynchronisation mit eingegebenen Zugangsdaten.]({% image_buster /assets/img/amplitude.png %})

### Schritt 3: Amplitude-Kohorte nach Braze exportieren {#step-3-export-an-amplitude-cohort-to-braze}

Um zunächst Nutzer:innen von Amplitude nach Braze zu exportieren, erstellen Sie eine [Kohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) der Nutzer:innen, die Sie exportieren möchten. Richten Sie dann zwei Synchronisierungen für diese Kohorte ein, um identifizierte und anonyme Nutzer:innen zu erfassen – mit folgenden Bezeichner-Zuordnungseigenschaften:
- User ID (externe ID)
- Device ID

Sie können mehrere Braze-Verbindungen in Ihrem Amplitude-Konto einrichten. So können Sie eine Verbindung für die Synchronisierung von User IDs für bekannte Nutzer:innen und eine weitere für die Synchronisierung von Device IDs für anonyme Nutzer:innen konfigurieren.

Nachdem Sie eine Kohorte erstellt haben, klicken Sie auf **Sync to...**, um diese Nutzer:innen nach Braze zu exportieren.

{% alert important %}
Nur Nutzer:innen, die bereits in Braze vorhanden sind, werden einer Kohorte hinzugefügt oder daraus entfernt. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

#### Synchronisierungshäufigkeit festlegen {#defining-sync-cadence}

Kohortensynchronisierungen können als einmalige Synchronisierung, täglich oder stündlich geplant oder sogar in Realtime eingerichtet werden, wobei die Aktualisierung jede Minute erfolgt.

Jede Integration, die Sie einrichten, protokolliert Datenpunkte. Bei Fragen zu den Details der Braze-Datenpunkte kann Ihr Braze-Account Manager:in diese beantworten.

### Schritt 4: Nutzer:innen in Braze segmentieren {#step-4-segment-users-in-braze}

Um in Braze ein Segment dieser Nutzer:innen zu erstellen, navigieren Sie unter **Engagement** zu **Segments**, benennen Sie Ihr Segment und wählen Sie **Amplitude Cohorts** als Filter aus. Verwenden Sie dann die Option „includes“ und wählen Sie die Kohorte aus, die Sie in Amplitude erstellt haben.

![Im Braze-Segment-Builder ist der Filter „amplitude_cohorts“ auf „includes_value“ und „Amplitude cohort test“ gesetzt.]({% image_buster /assets/img/amplitude2.png %})

Nach dem Speichern können Sie dieses Segment bei der Erstellung von Canvas oder Campaign im Schritt zur Zielgruppenzusammenstellung referenzieren.

## Nutzer:innen-Zuordnung {#user-matching}

Identifizierte Nutzer:innen können entweder anhand ihrer `external_id` oder ihres `alias` zugeordnet werden. Anonyme Nutzer:innen können anhand ihrer `device_id` zugeordnet werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen erstellt wurden, können nicht anhand ihrer `device_id` identifiziert werden und müssen anhand ihrer `external_id` oder ihres `alias` identifiziert werden.

## FAQ

### Kann ich eine Liste der Amplitude-Kohorten abrufen? {#can-i-pull-a-list-of-amplitude-cohorts}

Braze bietet keine API, um einen Katalog aller Amplitude-Kohortendefinitionen zu exportieren. Sie können Kohorten an folgenden Stellen anzeigen und verwenden:

1. **In Amplitude:** Zeigen Sie Kohorten im Amplitude-Dashboard an und verwalten Sie sie, bevor Sie sie mit Braze synchronisieren.
2. **In Braze:** Nachdem eine Kohorte synchronisiert wurde, können Sie Nutzer:innen mit dem Segment-Filter **Amplitude Cohorts** ansprechen. Der Filter listet synchronisierte Kohorten nach dem von Amplitude gesendeten Namen auf.

Bei Fehlern bei der Kohortensynchronisierung überprüfen Sie zunächst die Nutzer-ID-Zuordnung und die API-Schlüssel in Amplitude. Siehe [„We do not have enough data yet for this filter“ beim Synchronisieren einer Kohorte]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences#we-do-not-have-enough-data-yet-for-this-filter-when-syncing-a-cohort).