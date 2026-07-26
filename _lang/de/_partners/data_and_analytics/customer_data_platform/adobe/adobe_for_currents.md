---
nav_title: Adobe für Currents
article_title: Adobe für Currents
alias: /partners/adobe_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze-Currents und Adobe, einer geschäftskunden Data Platform (CDP), die es Marken erlaubt, ihre Daten von Adobe (angepasste Attribute und Segmente) mit Braze zu verbinden und in Echtzeit abzubilden."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe für Currents {#adobe-for-currents}

> [Adobe](https://www.adobe.com/) ist eine geschäftskunden Data Platform (CDP), die es Marken erlaubt, ihre Daten von Adobe (angepasste Attribute und Segmente) mit Braze zu verbinden und in Echtzeit abzubilden.

Die Integration von Braze und Adobe erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) können Sie auch Daten mit Adobe verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Currents | Um Daten zurück in Adobe zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| Adobe Experience Platform-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Adobe Experience Platform-Konto](https://experience.adobe.com/#/platform/home). |
| Berechtigung zum Erstellen eines Konnektors | Sie benötigen die Berechtigung, eine Verbindung zu einer Streaming-Quelle herzustellen, um diese Integration nutzen zu können. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Erstellen eines XDM-Schemas in Adobe {#step-1-create-an-xdm-schema-in-adobe}

1. Gehen Sie in Adobe Experience Platform zu **Schemas** > wählen Sie **Create schema** > wählen Sie **Experience Event** > wählen Sie **Next**.<br><br>![Adobe-Schemas-Seite für das Schema mit dem Namen „Braze Currents Walk-Through“.]({% image_buster /assets/img/adobe/currents_sources.png %})<br><br>
2. Geben Sie einen Namen und eine Beschreibung für Ihr Schema an.
3. Im Panel **Composition** konfigurieren Sie Ihre Schema-Attribute:
- Wählen Sie unter **Field groups** die Option **Add** und fügen Sie dann die Feldgruppe **Braze Currents User Event** hinzu.
- Wählen Sie **Save**.

Weitere Informationen zu Schemas finden Sie in der Dokumentation von Adobe zur [Erstellung von Schemas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### 2. Schritt: Braze mit der Adobe Experience Platform verbinden {#step-2-connect-braze-to-the-adobe-experience-platform}

1. Gehen Sie in Adobe Experience Platform zu **Sources** > **Catalog** > **Marketing automation**.
2. Wählen Sie **Add data** für Braze-Currents.
3. Laden Sie die [Braze-Currents-Beispieldatei](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json) hoch.<br><br>![Adobe-Seite „Add data“.]({% image_buster /assets/img/adobe/currents_add_data.png %})<br><br>
4. Nachdem Ihre Datei hochgeladen wurde, geben Sie Ihre Datenflussdetails an, einschließlich Informationen über Ihren Datensatz und das Schema, auf das Sie abbilden möchten.
    - Wenn Sie zum ersten Mal eine Braze-Currents-Quelle anschließen, erstellen Sie einen neuen Datensatz und stellen Sie sicher, dass Sie das in [Schritt 1](#step-1-create-an-xdm-schema-in-adobe) erstellte Schema verwenden.
    - Wenn Sie dies nicht zum ersten Mal tun, verwenden Sie einen vorhandenen Datensatz, der auf das Braze-Schema verweist.
5. Konfigurieren Sie die Abbildung für Ihre Daten und lösen Sie die Probleme.
    - Ändern Sie die Abbildung für `id` von `to _braze.appID` auf `_id` auf der Stammebene des Schemas.
    - Stellen Sie sicher, dass `properties.is_amp` auf `_braze.messaging.email.isAMP` abgebildet ist.
    - Löschen Sie die Abbildung für `time` und `timestamp`, wählen Sie dann das Symbol „Hinzufügen“ > **Add calculated field** und geben Sie **time * 1000** ein. Wählen Sie **Save**.
    - Wählen Sie **Map target field** neben dem neuen Quellfeld und ordnen Sie es dem **timestamp** auf der Stammebene des Schemas zu. <br><br>![Adobe-Seite „Add data“ mit Abbildungen.]({% image_buster /assets/img/adobe/currents_mapping.png %})<br><br>
6. Wählen Sie **Validate**, um zu bestätigen, dass Sie die Probleme gelöst haben.

{% alert important %}
Die Zeitstempel von Braze werden in Sekunden angegeben. Um Zeitstempel in Adobe Experience Platform genau wiederzugeben, müssen Ihre berechneten Felder in Millisekunden angegeben werden. Um Sekunden in Millisekunden umzurechnen, verwenden Sie die Berechnung **time * 1000**.
{% endalert %}

{: start="7"}
7. Wählen Sie **Next**, überprüfen Sie Ihre Datenflussdetails und wählen Sie dann **Finish**.<br><br>![Adobe-Seite „Add data“ ohne Abbildungsfehler.]({% image_buster /assets/img/adobe/currents_no_errors.png %})

### 3. Schritt: Zugangsdaten erfassen {#step-3-gather-credentials}

Sammeln Sie die folgenden Zugangsdaten, um sie in Braze einzugeben, damit Braze Daten an die Adobe Experience Platform senden kann.

| Feld         | Beschreibung                          |
|---------------|-------------------------------------|
| Client ID     | Die Client-ID, die mit Ihrer Adobe Experience Platform-Quelle verknüpft ist. |
| Client Secret | Das Client Secret, das mit Ihrer Adobe Experience Platform-Quelle verknüpft ist. |
| Tenant ID     | Die Tenant-ID, die mit Ihrer Adobe Experience Platform-Quelle verknüpft ist. |
| Sandbox Name  | Die Sandbox, die mit Ihrer Adobe Experience Platform-Quelle verknüpft ist.   |
| Dataflow ID   | Die Dataflow-ID, die mit Ihrer Adobe Experience Platform-Quelle verknüpft ist.   |
| Streaming Endpoint  | Der Streaming-Endpunkt, der mit Ihrer Adobe Experience Platform-Quelle verknüpft ist. Braze konvertiert diesen automatisch in den Batch-Streaming-Endpunkt. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3. Schritt: Zugangsdaten erfassen" }

### 4. Schritt: Currents zum Streamen von Daten an Ihre Datenquelle konfigurieren {#step-4-configure-currents-to-stream-data-to-your-data-source}

1. Gehen Sie in Braze zu **Partner Integrations** > **Data Export** und wählen Sie dann **Create New Current**.
2. Geben Sie Folgendes an:
    - Einen Namen für den Konnektor
    - Kontaktinformationen für Benachrichtigungen über den Konnektor
    - Die Zugangsdaten aus [Schritt 3](#step-3-gather-credentials)
3. Wählen Sie die Ereignisse aus, die Sie empfangen möchten.
4. Konfigurieren Sie optional gewünschte Feldausschlüsse oder Transformationen.
5. Wählen Sie **Launch Current**.