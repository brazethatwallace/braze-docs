---
nav_title: AppsFlyer Audiences
article_title: AppsFlyer Audiences
alias: /partners/appsflyer_audiences/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und AppsFlyer Audiences, ein Feature der AppsFlyer-Plattform, mit dem Sie Zielgruppen-Segmente effizient erstellen und mit Partnernetzwerken verbinden können."
page_type: partner
search_tag: Partner

---

# AppsFlyer Audiences

> Dieser Artikel beschreibt, wie Sie Nutzer:innen-Kohorten aus AppsFlyer in Braze importieren können, indem Sie die [AppsFlyer Audiences](https://www.appsflyer.com/product/audiences/)-Integration verwenden. Weitere Informationen zur Integration von AppsFlyer und seinen anderen Funktionalitäten, wie z. B. der mobilen Attribution, finden Sie im [Hauptartikel zu AppsFlyer]({{site.baseurl}}/partners/message_orchestration/deeplinking/appsflyer/appsflyer/).

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| AppsFlyer-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein AppsFlyer-Konto. |
| iOS- oder Android-App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code-Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| AppsFlyer SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [AppsFlyer SDK](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview) installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Datenimport-Integration {#data-import-integration}

### 1. Schritt: AppsFlyer SDK konfigurieren {#step-1-configure-the-appsflyer-sdk}

Um diese Integration zu nutzen, müssen Sie die externe Braze-ID der Nutzer:innen über die Funktion `setPartnerData()` des AppsFlyer SDK an AppsFlyer übergeben:

#### Android
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### 2. Schritt: Datenimport-Schlüssel für Braze abrufen {#step-2-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **AppsFlyer** aus.

Hier finden Sie den REST-Endpunkt und können Ihren Braze-Datenimport-Schlüssel generieren. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im AppsFlyer-Dashboard einrichten.<br><br>![Das Feld „Datenimport über Kohortenimport“ auf der AppsFlyer-Technologieseite. In diesem Feld werden Ihnen der Datenimport-Schlüssel und der REST-Endpunkt angezeigt.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### 3. Schritt: Braze-Verbindung in AppsFlyer Audiences konfigurieren {#step-3-configure-a-braze-connection-in-appsflyer-audiences}

1. Gehen Sie in [AppsFlyer Audiences](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections) auf den Tab **Connections** und klicken Sie auf **Add partner connection**.
2. Wählen Sie Braze als Partner aus und geben Sie der Verbindung einen Namen.
3. Geben Sie den Datenimport-Schlüssel und den Braze-REST-Endpunkt an.
4. Speichern Sie die Verbindung – sie kann dann mit jeder neuen oder bestehenden Zielgruppe verknüpft werden.

![Die Konfigurationsseite der AppsFlyer-Audiences-Plattform für Partnerverbindungen. Im unteren Teil des Bildes sehen Sie, dass das Feld „Braze externe ID“ markiert ist.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### 4. Schritt: AppsFlyer-Audiences-Kohorten in Braze verwenden {#step-4-using-appsflyer-audiences-cohorts-in-braze}

Sobald eine AppsFlyer-Zielgruppe in Braze hochgeladen wurde, können Sie sie als Filter bei der Definition von Segmenten in Braze verwenden, indem Sie den Filter **AppsFlyer Cohorts** auswählen.

![Nutzer:innen-Attribut-Filter „AppsFlyer Cohorts“ ausgewählt.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Der Kohortenimport erstellt keine neuen Nutzer:innen in Braze.
{% endalert %}

## Nutzer:innen-Abgleich {#user-matching}

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder ihren `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` abgeglichen werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder ihren `alias` identifiziert werden.