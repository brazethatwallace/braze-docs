---
nav_title: Campaign-Daten exportieren
article_title: Campaign-Daten exportieren
page_order: 2
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Campaign-Ergebnisdaten aus Singlechannel-, Multichannel- oder Multivarianten-Campaigns exportieren können. Außerdem erfahren Sie, wie Sie Nutzerdaten der Empfänger:innen exportieren können."
tool:
  - Campaigns
  - Reports

---

# Campaign-Daten exportieren {#export-campaign-data}

> Wählen Sie auf der Seite **Campaigns** des Dashboards die gewünschte Campaign aus und scrollen Sie nach unten zu den historischen Performance-Diagrammen, die exportiert werden können.<br><br>Auf dieser Seite erfahren Sie, wie Sie Campaign-Ergebnisdaten aus Singlechannel-, Multichannel- und Multivarianten-Campaigns exportieren und wie Sie Nutzerdaten der Empfänger:innen exportieren können.

## Multichannel-Campaigns {#multichannel-campaigns}

Bei Multichannel-Campaigns hängen die exportierbaren Daten davon ab, welche Messaging-Kanäle Sie verwendet haben. Hier finden Sie eine Liste aller Daten, die aus einer Campaign exportiert werden können, die iOS-Push, Android-Push, E-Mail und In-App-Nachrichten verwendet hat:

- Gesendete Nachrichten nach Datum
    - Gesendete Nachrichten insgesamt
    - Über die Kanäle der Campaign gesendete Nachrichten (kann Push, E-Mail und In-App-Nachrichten umfassen)
- E-Mail-Nachrichten-Engagement nach Datum
    - Anzahl der zugestellten E-Mails
    - Anzahl der gesendeten E-Mails
    - Anzahl der geöffneten E-Mails
    - Anzahl der E-Mail-Klicks
    - Anzahl der E-Mail-Bounces
    - Anzahl der als Spam gemeldeten E-Mails
- In-App-Nachrichten-Engagement nach Datum
    - Anzahl der gesendeten In-App-Nachrichten
    - In-App-Nachrichten-Impressionen
    - Anzahl der Klicks auf In-App-Nachrichten
- iOS-Push-Engagement nach Datum
    - Anzahl der gesendeten iOS-Push-Benachrichtigungen
    - Öffnungen gesamt
    - Direkte Öffnungen
    - Bounces
- Android-Push-Engagement nach Datum
    - Anzahl der gesendeten Android-Push-Benachrichtigungen
    - Öffnungen gesamt
    - Direkte Öffnungen
    - Bounces

## Multivarianten-Campaigns {#multivariate-campaigns}

Für Multivarianten-Campaigns, die nur einen Messaging-Kanal verwenden, können Sie Daten exportieren, die zeigen, wie jede Variante im Laufe der Zeit in den Analytics des jeweiligen Messaging-Kanals abgeschnitten hat. Sie können diese Daten nach Statistik oder nach Nachrichtenvariante gruppiert anzeigen.

Die Ergebnisse von Push-Campaigns enthalten Diagramme für die folgenden Analytics:

- Gesendete Nachrichten nach Datum für jede Variante
- Conversions nach Datum für jede Variante
- Eindeutige Empfänger:innen nach Datum für jede Variante
- Öffnungen nach Datum für jede Variante
- Direkte Öffnungen nach Datum für jede Variante
- Bounces nach Datum für jede Variante

Die Ergebnisse von E-Mail-Campaigns enthalten Diagramme für die folgenden Analytics:

- Anzahl zugestellt nach Datum für jede Variante
- Anzahl gesendet nach Datum für jede Variante
- Öffnungen nach Datum für jede Variante
- Klicks nach Datum für jede Variante
- Bounces nach Datum für jede Variante
- Spam-Berichte nach Datum für jede Variante

Die Ergebnisse von In-App-Nachrichten-Campaigns enthalten Diagramme für die folgenden Analytics:

- Gesendet nach Datum für jede Variante
- Impressionen nach Datum für jede Variante
- Klicks nach Datum für jede Variante

## Empfänger:innen der Campaign {#campaign-recipients}

Sie können Nutzerdaten für alle Empfänger:innen einer Campaign als CSV-Datei exportieren. Wählen Sie dazu den Button **User Data** im Abschnitt **Campaign Details** aus.

{% alert note %}
Sie können den Button **User Data** nicht sehen? Um Nutzerdaten zu exportieren, benötigen Sie die [Berechtigungen]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#limited-and-team-role-permissions) **Export User Data** für diesen Workspace.
{% endalert %}

![User-Data-Dropdown auf der Seite „Campaign Details“]({% image_buster /assets/img/campaign_export_example.png %})

Die CSV-Ausgabe enthält Nutzerprofil-Daten für alle Empfänger:innen der Campaign. Braze erstellt den Bericht im Hintergrund und sendet ihn per E-Mail an die aktuell angemeldete Person.

Wenn Sie Ihre [Amazon S3-Anmeldedaten]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3) mit Braze verknüpft haben, wird die CSV-Datei auch in Ihren S3-Bucket hochgeladen. Andernfalls läuft der Ihnen per E-Mail zugesandte Link nach einigen Stunden ab.

Die exportierte Datei enthält dieselben Nutzerdatenfelder, die auch beim [Export von Nutzerdaten für ein Segment]({{site.baseurl}}/user_guide/analytics/dashboards/home#exporting-app-usage-data) enthalten sind. Wenn Sie zusätzlich zu diesen Datenfeldern die Option „Export All Recipient Data“ wählen, enthält die exportierte Datei außerdem die folgenden Daten für jede:n Nutzer:in:

- Name der erhaltenen Campaign-Variante
- API-ID der erhaltenen Campaign-Variante
- Ob die/der Nutzer:in zur Kontrollgruppe gehört

{% alert tip %}
Hilfe bei CSV- und API-Exporten finden Sie unter [Fehlerbehebung beim Export]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}