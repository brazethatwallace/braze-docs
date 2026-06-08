---
nav_title: Amplitude
article_title: Amplitude-Kohortenimport
description: "Dieser Referenzartikel beschreibt die Kohortenimport-Funktionalität von Amplitude, einer Plattform für Produktanalysen und Business-Intelligence."
page_type: partner
search_tag: Partner
---

# Amplitude-Kohortenimport {#amplitude-cohort-import}

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten von [Amplitude](https://amplitude.com/) nach Braze importieren können. Weitere Informationen zur Integration von Amplitude und seinen anderen Funktionen finden Sie im [Hauptartikel zu Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Integration von Datenimporten {#data-import-integration}

Jede Integration, die Sie einrichten, wird auf das Datenpunktvolumen Ihres Kontos angerechnet.

### 1. Schritt: Braze-Datenimport-Schlüssel abrufen {#step-1-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Amplitude** aus. Hier finden Sie den REST-Endpunkt und können Ihren Braze-Datenimport-Schlüssel generieren.

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Amplitude einrichten.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### 2. Schritt: Braze-Integration in Amplitude einrichten {#step-2-set-up-the-braze-integration-in-amplitude}

Navigieren Sie in Amplitude zu **Sources & Destinations** > **[Projektname]** > **Destinations** > **Braze**. Geben Sie in der daraufhin angezeigten Eingabeaufforderung den Braze-Datenimport-Schlüssel und den REST-Endpunkt an und klicken Sie auf **Save**.

![]({% image_buster /assets/img/amplitude.png %})

### 3. Schritt: Amplitude-Kohorte nach Braze exportieren {#step-3-export-an-amplitude-cohort-to-braze}

Um Nutzer:innen aus Amplitude nach Braze zu exportieren, erstellen Sie zunächst eine [Kohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) von Nutzer:innen, die Sie exportieren möchten. Richten Sie dann zwei Synchronisationen für diese Kohorte ein, um identifizierte und anonyme Nutzer:innen zu erfassen, mit den folgenden Bezeichner-Zuordnungseigenschaften:
- Nutzer-ID (externe ID)
- Geräte-ID

Sie können in Ihrem Amplitude-Konto mehrere Braze-Verbindungen einrichten. So können Sie eine Verbindung konfigurieren, die Nutzer-IDs für bekannte Nutzer:innen synchronisiert, und eine weitere, die Geräte-IDs für anonyme Nutzer:innen synchronisiert.

Sobald Sie eine Kohorte erstellt haben, klicken Sie auf **Sync to...**, um diese Nutzer:innen nach Braze zu exportieren.

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

#### Sync-Kadenz festlegen {#defining-sync-cadence}

Kohorten-Synchronisationen können als einmalige Synchronisation, als täglicher oder stündlicher Zeitplan oder sogar als Realtime-Synchronisation eingestellt werden, die jede Minute aktualisiert wird.

Jede Integration, die Sie einrichten, protokolliert Datenpunkte. Wenn Sie Fragen zu den Feinheiten der Braze-Datenpunkte haben, kann Ihr Braze Account Manager diese beantworten.

### 4. Schritt: Nutzer:innen in Braze segmentieren {#step-4-segment-users-in-braze}

Um in Braze ein Segment dieser Nutzer:innen zu erstellen, navigieren Sie unter **Engagement** zu **Segments**, benennen Sie Ihr Segment und wählen Sie **Amplitude Cohorts** als Filter aus. Verwenden Sie anschließend die Option „enthält“ und wählen Sie die Kohorte, die Sie in Amplitude erstellt haben.

![Im Braze Segment Builder ist der Filter „amplitude_cohorts“ auf „includes_value“ und „Amplitude cohort test“ eingestellt.]({% image_buster /assets/img/amplitude2.png %})

Nach dem Speichern können Sie dieses Segment bei der Erstellung von Canvas oder Campaigns im Schritt „Targeting“ referenzieren.

## Nutzer:innen-Abgleich {#user-matching}

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder ihren `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` abgeglichen werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder ihren `alias` identifiziert werden.