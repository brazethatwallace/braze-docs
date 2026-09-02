---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Airbridge, die personenbasierte Attribution und inkrementelle Messungen anbietet, um die tatsächliche Effektivität des Marketings über Geräte, Identitäten und Plattformen hinweg zu messen."
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/) ist eine einheitliche Plattform für mobile Messungen, mit der Sie Wachstumsquellen durch mobile Attribution, inkrementelle Messungen und Marketing-Mix-Modellierung entdecken können.

_Diese Integration wird von Airbridge gepflegt._

## Über die Integration {#about-the-integration}

Mit der Integration von Braze und Airbridge können Sie alle nicht-organischen Daten zur Install-Attribution von Airbridge an Braze weitergeben, um personalisierte Marketing-Campaigns zu erstellen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Airbridge-Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein Airbridge-Konto. |
| iOS- oder Android-App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code-Snippets in Ihrer Anwendung erforderlich sein. |
| Airbridge SDK or Software-Development-Kit | Zusätzlich zum erforderlichen Braze SDK or Software-Development-Kit müssen Sie das Airbridge [Android](https://help.airbridge.io/en/developers/android-sdk)- oder [iOS](https://help.airbridge.io/en/developers/ios-sdk)-SDK or Software-Development-Kit installieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### Schritt 1: Geräte-ID zuordnen {#step-1-map-device-id}

Die Server-zu-Server-Integration kann durch Einfügen der folgenden Code-Snippets in Ihre Apps aktiviert werden.

#### Android

Wenn Sie eine Android-App haben, müssen Sie eine eindeutige Braze-Geräte-ID an Airbridge weitergeben.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

Wenn Sie eine iOS-App haben, können Sie sich dafür entscheiden, IDFV zu erfassen, indem Sie das Feld useUUIDAsDeviceId auf false setzen. Wenn diese Option nicht gesetzt ist, wird die iOS-Attribution wahrscheinlich nicht korrekt von Airbridge auf Braze abgebildet. Weitere Informationen finden Sie unter „Erfassen von IDFV“.

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flutter

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### Schritt 2: Datenimport-Schlüssel für Braze abrufen {#step-2-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Airbridge** aus.

Hier finden Sie den Representational State Transfer-Endpunkt und können Ihren Datenimport-Schlüssel für Braze generieren. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der Representational State Transfer-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Airbridge einrichten.

![Braze-Airbridge-Partnerseite mit den Feldern für Datenimport-Schlüssel und REST-Endpunkt.]({% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %})

### Schritt 3: Braze im Dashboard von Airbridge konfigurieren {#step-3-configure-braze-in-airbridges-dashboard}

1. Navigieren Sie in Airbridge in der linken Seitenleiste zu **Integrations > Third-party Integrations** und wählen Sie **Braze** aus.
2. Geben Sie den Datenimport-Schlüssel und den Representational State Transfer-Endpunkt an, den Sie im Braze-Dashboard gefunden haben.
3. Wählen Sie den Ereignistyp (Install-Ereignis oder Install- und Deeplink-Öffnungs-Ereignis) aus und speichern Sie.

{% alert note %}
Die Attributionsdaten für Campaigns, die zu Deeplink-Öffnungen geführt haben, werden auf Geräteebene aktualisiert. Wenn beispielsweise zwei Nutzer:innen ein Gerät verwenden und eine Person ein Deeplink-Öffnungs-Ereignis ausführt, werden die Attributionsdaten dieses Ereignisses auch in die Daten der anderen Person übernommen.
{% endalert %}

Ausführlichere Anweisungen finden Sie unter [Airbridge](https://help.airbridge.io/en/guides/braze).

### Schritt 4: Integration bestätigen {#step-4-confirm-the-integration}

Nachdem Braze Attributionsdaten von Airbridge erhalten hat, ändert sich der Verbindungsstatus auf der Airbridge-Technologie-Partnerseite in Braze von „Nicht verbunden“ zu „Verbunden“ und enthält einen Zeitstempel der letzten erfolgreichen Anfrage.

Dieser Status ändert sich erst, wenn Braze Daten über eine attributierte Installation erhält. Braze ignoriert organische Installationen (schließt sie aus dem Airbridge-Postback aus) und zählt sie nicht, wenn es darum geht, ob die Verbindung erfolgreich ist.

## Verfügbare Datenfelder {#available-data-fields}

Airbridge kann vier Arten von Attributionsdaten an Braze senden, die in der folgenden Tabelle aufgeführt sind. Diese Daten können im Airbridge-Dashboard eingesehen werden und werden für die Install-Attribution und Filterung von Nutzer:innen verwendet.

Vorausgesetzt, Sie konfigurieren Ihre Integration wie vorgeschlagen, wird Braze die Installationsdaten den Segment-Filtern zuordnen.

| Airbridge-Datenfeld | Braze-Segment-Filter | Beschreibung |
| -------------------- | ---------------------| ---- |
| `Channel` | Install-Attribution-Quelle | Der Kanal, dem die Installationen oder Deeplink-Öffnungen zugeschrieben werden |
| `Campaign` | Install-Attribution-Campaign | Die Campaign, der die Installationen oder Deeplink-Öffnungen zugerechnet werden |
| `Ad Group` | Install-Attribution-Anzeigengruppe | Die Anzeigengruppe, der die Installationen oder Deeplink-Öffnungen zugeschrieben werden |
| `Ad Creative` | Install-Attribution-Anzeige | Das Werbemittel, dem die Installationen oder Deeplink-Öffnungen zugeschrieben werden |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Verfügbare Datenfelder" }

Ihre Nutzerbasis kann im Braze-Dashboard mithilfe der Install-Attribution-Filter nach Attributionsdaten segmentiert werden.

![Braze-Segment-Filter mit den verfügbaren Airbridge-Install-Attribution-Feldern.]({% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %})

## Meta Business-Attributionsdaten {#meta-business-attribution-data}

Attributionsdaten für Meta Business-Campaigns sind nicht über unsere Partner verfügbar. Diese Medienquelle erlaubt ihren Partnern nicht, Attributionsdaten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Airbridge-Klick, der or klicken-Tracking-URLs in Braze (optional)

Die Verwendung von Klick, der or klicken-Tracking-Links in Ihren Braze-Campaigns zeigt, welche Campaigns App-Installationen und erneute Interaktionen fördern. Nutzen Sie die Ergebnisse, um die Marketing-Performance zu messen und zu entscheiden, wo Sie Ressourcen für einen höheren Kapitalrendite or ROI investieren sollten.

Um mit Airbridge-Klick, der or klicken-Tracking-Links zu beginnen, besuchen Sie [Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link). Nachdem die Einrichtung abgeschlossen ist, können Sie die Airbridge-Klick, der or klicken-Tracking-Links direkt in Ihre Braze-Campaigns einfügen. Airbridge verwendet dann seine [probabilistischen Attributionsmethoden](https://help.airbridge.io/en/guides/identity-matching), um die Nutzer:innen zu attributieren, die auf den Link geklickt haben. Wir empfehlen, Ihre Airbridge-Tracking-Links mit einem Geräte-Bezeichner zu versehen, um die Genauigkeit der Attributionen Ihrer Braze-Campaigns zu verbessern. Dadurch werden die Nutzer:innen, die auf den Link geklickt haben, deterministisch attributiert.

{% tabs %}
{% tab Android %}
Für Android erlaubt Braze Kund:innen, sich für die [Erfassung der Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection#optional-google-advertising-id) zu entscheiden. Die GAID wird auch nativ über die Airbridge-SDK or Software-Development-Kit-Integration erfasst. Sie können die GAID in Ihre Airbridge-Klick, der or klicken-Tracking-Links einfügen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Airbridge den IDFV automatisch und nativ über unsere SDK or Software-Development-Kit-Integrationen. Dies kann als Geräte-Bezeichner verwendet werden. Sie können den Identifier for Vendors (IDFV) in Ihre Airbridge-Klick, der or klicken-Tracking-Links einfügen, indem Sie die folgende Liquid-Logik verwenden:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Diese Empfehlung ist rein optional**<br>
Wenn Sie derzeit keine Geräte-Bezeichner – wie IDFV oder GAID – in Ihren Klick, der or klicken-Tracking-Links verwenden oder dies in Zukunft nicht vorhaben, ist Airbridge dennoch in der Lage, diese Klicks durch seine probabilistische Modellierung zu attributieren.
{% endalert %}