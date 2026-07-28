---
nav_title: Branch für Attribution
article_title: Branch für Attribution
alias: /partners/branch_for_attribution/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Branch, einer mobilen Linking-Plattform, die Sie bei der Akquise, dem Engagement und der Messung über alle Geräte, Kanäle und Plattformen hinweg unterstützt."
page_type: partner
search_tag: Partner
---

# Branch für Attribution {#branch}

{% multi_lang_include video.html id="PwGKqfwV-Ss" align="right" %}

> [Branch](https://docs.branch.io/pages/integrations/braze/), eine mobile Linking-Plattform, unterstützt Sie bei der Akquise, dem Engagement und der Messung über alle Geräte, Kanäle und Plattformen hinweg, indem sie einen ganzheitlichen Überblick über alle Nutzer:innen-Touchpoints bietet.

_Diese Integration wird von Branch gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Branch hilft Ihnen dabei, genau zu verstehen, wann und wo Nutzer:innen akquiriert wurden und wie Sie ihre Journeys durch robuste Attribution und [Deeplinking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking) personalisieren können.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Branch-Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein Branch-Konto. |
| iOS- oder Android-App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code-Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| Branch SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [Branch SDK](https://help.branch.io/developers-hub/docs/native-sdks-overview) installieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Geräte-IDs zuordnen {#step-1-map-device-ids}

#### Android

Wenn Sie eine Android-App haben, müssen Sie eine eindeutige Braze-Geräte-ID an Branch übergeben. Diese ID kann in der Methode `setRequestMetadataKey()` des Branch SDK festgelegt werden. Der folgende Code-Snippet muss vor dem Aufruf von `initSession` eingefügt werden. Sie müssen außerdem das Braze SDK initialisieren, bevor Sie die Anfrage-Metadaten im Branch SDK festlegen.

{% tabs local %}
{% tab Java %}
```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId);
```
{% endtab %}
{% tab Kotlin %}
```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```
{% endtab %}
{% endtabs %}

#### iOS

{% alert important %}
Vor Februar 2023 verwendete unsere Branch-Attribution-Integration den Identifier for Vendors (IDFV) als primären Bezeichner, um iOS-Attribution-Daten abzugleichen. Für Braze-Kund:innen, die Objective-C verwenden, ist es nicht notwendig, die Braze `device_id` abzurufen und bei der Installation an Branch zu senden, da der Dienst nicht unterbrochen wird.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gemeinsamen Bezeichner nutzen möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird.

Bei der Einstellung `true` müssen Sie die iOS-Geräte-ID-Zuordnung für Swift implementieren, um die Braze `device_id` bei der App-Installation an Branch zu übergeben, damit Braze iOS-Attributionen korrekt zuordnen kann.

{% tabs local %}
{% tab Objective-C %}
```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```
{% endtab %}
{% tab Swift %}

```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init
}
```

{% endtab %}
{% endtabs %}

### 2. Schritt: Datenimport-Schlüssel für Braze abrufen {#step-2-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Branch** aus.

Hier finden Sie den REST-Endpunkt und können Ihren Braze-Datenimport-Schlüssel generieren. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Branch einrichten.<br><br>![Dieses Bild zeigt das Feld „Datenimport für Install-Attribution“ auf der Branch-Technologieseite. In diesem Feld werden Ihnen der Datenimport-Schlüssel und der REST-Endpunkt angezeigt.]({% image_buster /assets/img/attribution/branch.png %}){: style="max-width:90%;"}

### 3. Schritt: Daten-Feeds einrichten {#step-3-set-up-data-feeds}

1. Wählen Sie in Branch unter dem Abschnitt **Exports** die Option **Data Feeds**.
2. Wählen Sie auf der Seite **Data Feeds Manager** den Tab **Data Integrations** am oberen Rand der Seite aus.
3. Wählen Sie Braze aus der Liste der verfügbaren Datenpartner aus.
4. Geben Sie auf der Braze-Exportseite den Datenimport-Schlüssel und den REST-Endpunkt ein, die Sie im Braze-Dashboard gefunden haben, und wählen Sie **Enable**.

### 4. Schritt: Integration bestätigen {#step-4-confirm-the-integration}

Nachdem Braze Attribution-Daten von Branch erhalten hat, ändert sich die Statusanzeige der Verbindung auf der Branch-Technologie-Partnerseite in Braze von „Nicht verbunden“ zu „Verbunden“ und enthält einen Zeitstempel der letzten erfolgreichen Anfrage.

Dieser Status ändert sich erst, wenn Braze Daten über eine attributierte Installation erhält. Braze ignoriert organische Installationen (schließt sie aus dem Branch-Postback aus) und zählt sie nicht bei der Bestimmung, ob die Verbindung erfolgreich war.

## Feldzuordnung {#field-mapping}

Branch-Attribution-Felder werden wie folgt auf Braze abgebildet:

| Branch-Feld | Braze-Feld |
| --- | --- |
| Campaign | `campaign` |
| Channel | `source` |
| Ad Set Name | `adgroup` |
| Ad Name | `ad` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Branch-Feldzuordnung" }

## Attribution-Daten von Facebook und X (ehemals Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Attribution-Daten für Campaigns auf Facebook und X (ehemals Twitter) sind nicht über unsere Partner verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attribution-Daten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Branch-Klick-Tracking-URLs in Braze (optional) {#branch-click-tracking-urls-in-braze-optional}

Wenn Sie Klick-Tracking-Links in Ihren Braze-Campaigns verwenden, können Sie leicht erkennen, welche Campaigns zu App-Installationen und erneuter Interaktion führen. So können Sie Ihre Marketing-Bemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen für einen maximalen ROI investieren sollten.

Um mit Branch-Klick-Tracking-Links zu beginnen, besuchen Sie die [Dokumentation](https://help.branch.io/using-branch/docs/ad-links). Sie können die Branch-Klick-Tracking-Links direkt in Ihre Braze-Campaigns einfügen. Branch verwendet dann seine [probabilistischen Attribution-Methoden](https://help.branch.io/using-branch/docs/branch-attribution-logic-settings), um die Nutzer:innen zu attributieren, die auf den Link geklickt haben. Wir empfehlen, Ihre Branch-Tracking-Links mit einem Gerätebezeichner zu versehen, um die Genauigkeit der Attributionen Ihrer Braze-Campaigns zu verbessern. Dadurch werden die Nutzer:innen, die auf den Link geklickt haben, deterministisch attributiert.

{% tabs local %}
{% tab Android %}
Für Android erlaubt Braze Kund:innen, sich für die [Erfassung der Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id) zu entscheiden. Die GAID wird auch nativ über die Branch-SDK-Integration erfasst. Sie können die GAID in Ihre Branch-Klick-Tracking-Links aufnehmen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Branch den IDFV automatisch und nativ über unsere SDK-Integrationen. Dieser kann als Gerätebezeichner verwendet werden. Sie können den IDFV in Ihre Branch-Klick-Tracking-Links aufnehmen, indem Sie die folgende Liquid-Logik verwenden:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Diese Empfehlung ist rein optional**<br>
Wenn Sie derzeit keine Gerätebezeichner – wie IDFV oder GAID – in Ihren Klick-Tracking-Links verwenden oder dies in Zukunft nicht vorhaben, kann Branch diese Klicks dennoch durch seine probabilistische Modellierung attributieren.
{% endalert %}