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
* Die Segmentierungs- und Triggerfunktionen von Braze zu nutzen, um personalisierte In-App-Benachrichtigungen zu initiieren.
* Maßgeschneiderte In-App-Benachrichtigungen auf der Sendbird Notifications Plattform zu erstellen, die dann innerhalb der App-Umgebung zugestellt werden und das Engagement der Nutzer:innen erhöhen.

Durch die Nutzung der gemeinsamen Fähigkeiten von Braze und Sendbird Notifications können Unternehmen das Customer-Engagement steigern und durch effektive In-App-Benachrichtigungsstrategien höhere Konversionsraten erzielen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Sendbird-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Sendbird-Konto. |
| Sendbird UIKit | Sie müssen das Sendbird UIKit in Ihrer [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit)- oder [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit)-App installiert haben. |
| Braze REST-API-Schlüssel | Ein Braze REST-API-Schlüssel mit `users.track`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Anwendungsfälle {#use-cases}

![Diagramm, das die Anwendungsfälle der Integration von Braze und Sendbird Notifications für Marketing- und Transaktionsnachrichten zusammenfasst.]({% image_buster /assets/img/sendbird/use-cases.png %})

Die Integration von Braze und Sendbird Notifications bietet eine Reihe von Anwendungsfällen, um das Customer-Engagement zu steigern und ein außergewöhnliches Nutzererlebnis zu bieten:

- **Marketing**: Verbessern Sie zielgerichtete Campaigns mit personalisierten Aktionen und Empfehlungen, die auf die Vorlieben der Nutzer:innen zugeschnitten sind, wie z. B. exklusive Rabatte auf der Grundlage des Browserverlaufs oder früherer Käufe.
- **Transaktionen**: Verbessern Sie die Kundenkommunikation durch Realtime-Updates zu Bestellungen, Lieferungen, Rechnungen und Zahlungen, einschließlich Benachrichtigungen über den Auftragsstatus, Versanddetails und geschätzte Zustellungszeiten.

## Integration

### 1. Schritt: Erstellen Sie ein Benachrichtigungs-Template {#step-1-create-a-notification-template}

[Sendbird Templates](https://sendbird.com/docs/notifications/v1/templates) erlauben es Ihnen, personalisierte In-App-Benachrichtigungen zu versenden, indem Sie mehrere Templates für jeden Kanal erstellen und verwenden. Templates können auf dem Sendbird Dashboard erstellt und angepasst werden, ohne dass Sie Code schreiben müssen.

![Sendbird-Dashboard-Template-Editor zum Erstellen von Benachrichtigungs-Templates.]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### 2. Schritt: Einrichten der Braze-Integration im Sendbird-Dashboard {#step-2-set-up-the-braze-integration-on-sendbird-dashboard}

Wählen Sie im **Sendbird Dashboard** Ihre Anwendung aus, navigieren Sie zu **Notifications > Integrations** und klicken Sie unter dem Abschnitt **Braze** auf **Add**. Hier benötigen Sie Ihren Braze REST-API-Schlüssel und den Braze REST-Endpunkt.

Sobald Sie alle Felder ausgefüllt haben, klicken Sie auf **Save**, um die Integration abzuschließen und auf die Endpunkte der Integration und das API-Token zuzugreifen.

### 3. Schritt: Sendbird Notification Builder installieren {#step-3-install-sendbird-notification-builder}

Als Nächstes müssen Sie den [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji) installieren. Mit dieser Google Chrome-Erweiterung können Sie angepasste Benachrichtigungen über Sendbird im Braze-Dashboard senden.

![Sendbird Notification Builder Chrome-Erweiterungspanel im Braze-Dashboard.]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Fügen Sie die Sendbird-Zugangsdaten zur Erweiterung hinzu {#add-sendbird-credentials-to-the-extension}

Sobald die Erweiterung installiert ist, klicken Sie auf das Sendbird-Symbol in der Symbolleiste Ihres Browsers und wählen Sie **Settings**. Geben Sie hier Ihre App-ID und Ihr API-Token aus dem **Sendbird Notification Builder** an.

### 4. Schritt: Sendbird-Nutzer-ID der Braze-Nutzer-ID zuordnen {#step-4-map-sendbird-user-id-to-braze-user-id}

Eine Sendbird-Nutzer-ID muss als [angepasstes Attribut]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) zu einem Braze-Nutzerprofil hinzugefügt werden, damit die Integration genutzt werden kann. Sie können Nutzerprofile über CSV-Dateien von der Seite [Nutzerimport]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv) hochladen und aktualisieren. Alternativ können Sie auch die Braze-Nutzer-ID als Sendbird-Nutzer-ID verwenden.

### 5. Schritt: Richten Sie Ihr Webhook-Template ein {#step-5-set-up-your-webhook-template}

Gehen Sie in Braze unter **Templates und Medien** zu **Webhook-Templates** und wählen Sie das **Sendbird Webhook-Template**. Beachten Sie, dass dieses Template nur verfügbar ist, wenn Sie die Sendbird Notification Builder-Erweiterung installiert haben.

{% raw %}
1. Geben Sie einen Template-Namen an und fügen Sie Teams und Tags nach Bedarf hinzu.
2. Kopieren Sie einen Realtime- oder Batch-Endpunkt aus dem Sendbird Dashboard in die **Webhook-URL**.
3. Klicken Sie im Feld **Receiver** auf das Symbol <i class="fas fa-plus" aria-label="Hinzufügen"></i> und fügen Sie das Nutzerattribut ein, das der Sendbird-Nutzer-ID zugeordnet ist.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` wenn Sie ein angepasstes Attribut `sendbird_id` als Sendbird-Nutzer-ID verwenden.
    - `{{ '{{' }}${user_id}}}` wenn Sie die Braze-Nutzer-ID als Sendbird-Nutzer-ID verwenden.
4. Ersetzen Sie im Tab **Settings** den Wert `SENDBIRD_API_TOKEN` durch das Benachrichtigungs-API-Token aus dem Sendbird Dashboard.
5. Speichern Sie das Template.
{% endraw %}

## Verwendung dieser Integration {#using-this-integration}

### Campaigns

1. Klicken Sie im Braze-Dashboard auf der Seite **Campaigns** auf **Kampagne erstellen** > **Webhook**.
2. Wählen Sie das Webhook-Template aus, das Sie oben erstellt haben. Es wird dringend empfohlen, den Batch-Endpunkt für Campaigns zu verwenden.
3. Passen Sie das Template an, indem Sie seine Variablen im Tab **Verfassen** bearbeiten.

### Canvas

1. Fügen Sie in einem neuen oder bestehenden Canvas eine **Message**-Komponente hinzu.
2. Öffnen Sie die Komponente und wählen Sie **Webhook** aus den **Messaging-Kanälen**.
3. Wählen Sie das Webhook-Template aus, das Sie oben erstellt haben. Es wird dringend empfohlen, den Realtime-Endpunkt für Canvases zu verwenden.
4. Passen Sie das Template an, indem Sie seine Variablen im Tab **Verfassen** bearbeiten.

## Anpassung {#customization}

### Zustellungs- und Öffnungsstatus tracken {#track-delivery-and-open-status}

Um den Zustellungs- und Öffnungsstatus der Benachrichtigungen in die Konversionsmetrik einer Campaign zu integrieren, fügen Sie ein angepasstes Event im Braze-Dashboard hinzu.

1. Gehen Sie im Braze-Dashboard zu **Einstellungen > Einstellungen verwalten > Angepasste Events** und klicken Sie auf **+ Angepasstes Event hinzufügen**.
2. Nachdem Sie ein angepasstes Event erstellt haben, klicken Sie auf **Eigenschaften verwalten**, fügen Sie eine Eigenschaft namens „status“ hinzu und wählen Sie als Eigenschaftstyp „String“.
3. Wenn Sie eine Benachrichtigung in Campaigns oder Canvases verfassen, geben Sie den Namen des angepassten Events in das Feld **Event Name** ein.

Dieses angepasste Event wird für jede Benachrichtigung zweimal ausgelöst: wenn eine Nachricht gesendet wird und wenn Nutzer:innen die Nachricht öffnen.
- Wenn eine Nachricht gesendet wird, wird ein angepasstes Event mit dem Status `SENT` ausgelöst.
- Wenn eine Nachricht gelesen wird, wird ein angepasstes Event mit dem Status `READ` ausgelöst.