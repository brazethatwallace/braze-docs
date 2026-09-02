---
nav_title: Sendbird
article_title: Sendbird
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Sendbird, einer führenden Lösung für In-App Messaging, die es Nutzer:innen erlaubt, In-App-Benachrichtigungen auf der Sendbird-Plattform zu empfangen."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird](https://sendbird.com/) Notifications bietet Marketern und Produktmanagern einen leistungsstarken neuen Kanal zur Kommunikation mit ihren Kund:innen in der App mit persistenten, interaktiven Einweg-Nachrichten. Diese Nachrichten können für jede Art von Kommunikation verwendet werden und werden am häufigsten für Werbe- und Transaktionszwecke eingesetzt.

_Diese Integration wird von Sendbird gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Sendbird ermöglicht es Unternehmensnutzer:innen:
{% multi_lang_include partners/instant_chat/sendbird_integration_bullets.md %}

Durch die Nutzung der gemeinsamen Funktionen von Braze und Sendbird Notifications können Unternehmen das Customer-Engagement steigern und durch effektive In-App-Benachrichtigungsstrategien höhere Konversionsraten erzielen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Sendbird-Konto | Ein Sendbird-Konto ist erforderlich, um diese Partnerschaft nutzen zu können. |
| Sendbird UIKit | Sie müssen das Sendbird UIKit in Ihrer [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit)- oder [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit)-App installiert haben. |
| Braze-Representational State Transfer-API-Schlüssel | Ein Braze-Representational State Transfer-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Representational State Transfer-Endpunkt | [Ihre Representational State Transfer-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL Ihrer Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

![Diagramm, das die Anwendungsfälle der Integration von Braze und Sendbird Notifications für Marketing- und Transaktionsnachrichten zusammenfasst.]({% image_buster /assets/img/sendbird/use-cases.png %})

Die Integration von Braze und Sendbird Notifications bietet eine Reihe von Anwendungsfällen, um das Customer-Engagement zu steigern und ein herausragendes Nutzererlebnis zu bieten:

- **Marketing**: Verbessern Sie gezielte Campaigns mit personalisierten Aktionen und Empfehlungen, die auf die Präferenzen der Nutzer:innen zugeschnitten sind, wie z. B. exklusive Rabatte basierend auf dem Browserverlauf oder früheren Käufen.
- **Transaktional**: Optimieren Sie die Kundenkommunikation durch Realtime-Updates zu Bestellungen, Lieferungen, Rechnungen und Zahlungen, einschließlich Benachrichtigungen zum Auftragsstatus, Versanddetails und voraussichtlichen Lieferzeiten.

## Integration

### 1. Schritt: Erstellen Sie ein Benachrichtigungs-Template {#step-1-create-a-notification-template}

[Sendbird Templates](https://sendbird.com/docs/notifications/v1/templates) erlauben es Ihnen, personalisierte In-App-Benachrichtigungen zu versenden, indem Sie mehrere Templates für jeden Kanal erstellen und verwenden. Templates können auf dem Sendbird Dashboard erstellt und angepasst werden, ohne dass Sie Code schreiben müssen.

![Sendbird-Dashboard-Template-Editor zum Erstellen von Benachrichtigungs-Templates.]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### 2. Schritt: Einrichten der Braze-Integration im Sendbird-Dashboard {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

Wählen Sie im **Sendbird Dashboard** Ihre Anwendung aus, navigieren Sie zu **Notifications > Integrations** und klicken Sie unter dem Abschnitt **Braze** auf **Add**. Hier benötigen Sie Ihren Braze Representational State Transfer-API-Schlüssel und den Braze Representational State Transfer-Endpunkt.

Sobald Sie alle Felder ausgefüllt haben, klicken Sie auf **Save**, um die Integration abzuschließen und auf die Endpunkte der Integration und das API-Token / Textbaustein zuzugreifen.

### 3. Schritt: Sendbird Notification Builder installieren {#step-3-install-sendbird-notification-builder}

Als Nächstes müssen Sie den [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji) installieren. Mit dieser Google Chrome-Erweiterung können Sie angepasste Benachrichtigungen über Sendbird im Braze-Dashboard senden.

![Sendbird Notification Builder Chrome-Erweiterungspanel im Braze-Dashboard.]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Fügen Sie die Sendbird-Zugangsdaten zur Erweiterung hinzu {#add-sendbird-credentials-to-the-extension}

Sobald die Erweiterung installiert ist, klicken Sie auf das Sendbird-Symbol in der Symbolleiste Ihres Browsers und wählen Sie **Settings**. Geben Sie hier Ihre App-ID und Ihr API-Token / Textbaustein aus dem **Sendbird Notification Builder** an.

### 4. Schritt: Sendbird-Nutzer-ID der Braze-Nutzer-ID zuordnen {#step-4-map-sendbird-user-id-to-braze-user-id}

Eine Sendbird-Nutzer-ID muss als [angepasstes Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) zu einem Braze-Kundenprofil or Nutzerprofil hinzugefügt werden, damit die Integration genutzt werden kann. Sie können Nutzerprofile über CSV-Dateien von der Seite [Nutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) hochladen und Update or aktualisieren or aktualisieren. Alternativ können Sie auch die Braze-Nutzer-ID als Sendbird-Nutzer-ID verwenden.

### 5. Schritt: Richten Sie Ihr Webhook-Template ein {#step-5-set-up-your-webhook-template}

Gehen Sie in Braze unter **Templates und Medien** zu **Webhook-Templates** und wählen Sie das **Sendbird Webhook-Template**. Beachten Sie, dass dieses Template nur verfügbar ist, wenn Sie die Sendbird Notification Builder-Erweiterung installiert haben.

{% raw %}
1. Geben Sie einen Template-Namen an und fügen Sie Teams und Tags nach Bedarf hinzu.
2. Kopieren Sie einen Realtime- oder Batch-Endpunkt aus dem Sendbird Dashboard in die **Webhook-URL**.
3. Klicken Sie im Feld **Receiver** auf das Symbol <i class="fas fa-plus" aria-label="Hinzufügen"></i> und fügen Sie das Nutzerattribut ein, das der Sendbird-Nutzer-ID zugeordnet ist.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` wenn Sie ein angepasstes Attribut `sendbird_id` als Sendbird-Nutzer-ID verwenden.
    - `{{ '{{' }}${user_id}}}` wenn Sie die Braze-Nutzer-ID als Sendbird-Nutzer-ID verwenden.
4. Ersetzen Sie im Tab **Settings** den Wert `SENDBIRD_API_TOKEN` durch das Benachrichtigungs-API-Token / Textbaustein aus dem Sendbird Dashboard.
5. Speichern Sie das Template.
{% endraw %}

## Diese Integration verwenden {#using-this-integration}

### Campaigns

1. Klicken Sie im Braze-Dashboard auf der Seite **Campaigns** auf **Create Campaign** > **Webhook**.
2. Wählen Sie das Webhook-Template aus, das Sie in diesem Abschnitt erstellt haben. Es wird dringend empfohlen, den Batch-Endpunkt für Campaigns zu verwenden.
3. Passen Sie das Template an, indem Sie die Variablen im Tab **Compose** bearbeiten.

### Canvas

1. Fügen Sie in einem neuen oder bestehenden Canvas eine **Message**-Komponente hinzu.
2. Öffnen Sie die Komponente und wählen Sie **Webhook** aus den **Messaging Channels** aus.
3. Wählen Sie das Webhook-Template aus, das Sie in diesem Abschnitt erstellt haben. Es wird dringend empfohlen, den Realtime-Endpunkt für Canvase zu verwenden.
4. Passen Sie das Template an, indem Sie die Variablen im Tab **Compose** bearbeiten.

## Anpassung {#customization}

### Zustell- und Öffnungsstatus verfolgen {#track-delivery-and-open-status}

Um die Zustell- und Öffnungsstatus-Events von Benachrichtigungen mit der Konversionsmetrik einer Campaign zu integrieren, fügen Sie ein angepasstes Event im Braze-Dashboard hinzu.

1. Gehen Sie im Braze-Dashboard zu **Einstellungen > Einstellungen verwalten > Angepasste Events** und klicken Sie auf **+ Angepasstes Event hinzufügen**.
2. Nachdem Sie ein angepasstes Event erstellt haben, klicken Sie auf **Eigenschaften verwalten**, fügen Sie eine Eigenschaft mit dem Namen „status“ hinzu und wählen Sie „String“ als Eigenschaftstyp.
3. Wenn Sie eine Benachrichtigung in Campaigns oder Canvase verfassen, geben Sie den Namen des angepassten Events in das Feld **Event Name** ein.

Dieses angepasste Event wird für jede Benachrichtigung zweimal ausgelöst: wenn eine Nachricht gesendet wird und wenn ein:e Nutzer:in die Nachricht öffnet.
- Wenn eine Nachricht gesendet wird, wird ein angepasstes Event mit dem Status `SENT` ausgelöst.
- Wenn eine Nachricht gelesen wird, wird ein angepasstes Event mit dem Status `READ` ausgelöst.