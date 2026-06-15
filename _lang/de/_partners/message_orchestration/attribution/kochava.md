---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Kochava, einer mobilen Attributions-Plattform, die Ihnen Insights zu Attribution und Analytics bietet, damit Sie Ihre Daten für Ihr Wachstum nutzen können."
page_type: partner
search_tag: Partner

---

# Kochava

> [Kochava](https://www.kochava.com/) bietet mobile Attribution und Analytics, damit Sie Ihre Daten für Ihr Wachstum nutzen können. Die Kochava Audience Platform ermöglicht Ihnen die Planung, das Targeting, die Aktivierung, die Messung und die Optimierung Ihrer App-Campaigns.

_Diese Integration wird von Kochava gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Kochava trägt zu einem ganzheitlicheren Verständnis Ihrer Campaigns bei, indem sie Attributionsdaten an Braze sendet, um besser zu verstehen, welche Campaigns zu Installationen, In-App-Aktivitäten und mehr führen.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Kochava-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein Kochava-Konto. |
| iOS- oder Android-App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code-Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| Kochava SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [Kochava SDK](https://support.kochava.com/sdk-integration/) installieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Abbildung der Nutzer:innen-IDs {#step-1-map-user-ids}

#### Android

Das [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) SDK generiert beim Sitzungsstart einen Globally Unique Identifier (GUID) als Braze-ID. Dieser Bezeichner sollte an die Kochava-Methode `IdentityLink` übergeben werden, damit Braze die Daten wieder mit dem richtigen Nutzerprofil abgleichen kann. Rufen Sie die Braze-ID mit der folgenden Methode ab:

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Vor Februar 2023 verwendete unsere Kochava-Attribution-Integration den Identifier for Vendors (IDFV) als primären Bezeichner, um iOS-Attributionsdaten abzugleichen. Für Braze-Kund:innen, die Objective-C verwenden, ist es nicht notwendig, die Braze `device_id` abzurufen und sie bei der Installation an Kochava zu senden, da es keine Unterbrechung des Dienstes gibt.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitigen Bezeichner verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, damit die Integration nicht unterbrochen wird. Wenn Sie diese Option auf `true` setzen, müssen Sie die Abbildung der iOS-Geräte-ID für Swift implementieren, um die Braze `device_id` bei der Installation der App an Kochava zu übergeben, damit Braze die iOS-Attributionen richtig zuordnen kann.

Braze verfügt über zwei APIs, die denselben Wert erzeugen: eine mit einem Completion Handler und eine andere, die die neue Swift-Gleichzeitigkeitsunterstützung nutzt. Beachten Sie, dass Sie die folgenden Code-Snippets ändern müssen, damit sie den Anweisungen des [iOS SDK](https://support.kochava.com/sdk-integration/ios-sdk-integration/) von Kochava entsprechen. Wenn Sie weitere Hilfe benötigen, wenden Sie sich an den Kochava-Support.

##### Completion Handler
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Swift-Gleichzeitigkeit {#swift-concurrency}
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### 2. Schritt: Datenimport-Schlüssel für Braze abrufen {#step-2-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **Kochava** aus.

Hier finden Sie den REST-Endpunkt und können Ihren Braze-Datenimport-Schlüssel generieren. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Kochava einrichten.<br><br>![Dieses Bild zeigt das Feld „Datenimport für Install-Attribution“, das Sie auf der Kochava-Technologieseite finden. In diesem Feld werden Ihnen der Datenimport-Schlüssel und der REST-Endpunkt angezeigt.]({% image_buster /assets/img/attribution/kochava.png %}){: style="max-width:90%;"}

### 3. Schritt: Postback von Kochava einrichten {#step-3-set-up-a-postback-from-kochava}

Fügen Sie ein [Postback](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback) in Ihrem Kochava-Dashboard hinzu. Sie werden zur Eingabe des Datenimport-Schlüssels und des REST-Endpunkts aufgefordert, die Sie im Braze-Dashboard gefunden haben.

### 4. Schritt: Integration bestätigen {#step-4-confirm-the-integration}

Nachdem Braze Attributionsdaten von Kochava erhalten hat, ändert sich der Verbindungsstatus auf der Kochava-Technologie-Partnerseite in Braze von „Nicht verbunden“ zu „Verbunden“ und enthält einen Zeitstempel der letzten erfolgreichen Anfrage.

Dieser Status ändert sich erst, wenn Braze Daten über eine attributierte Installation erhält. Braze ignoriert organische Installationen (schließt sie aus dem Kochava-Postback aus) und zählt sie nicht, wenn es darum geht, ob die Verbindung erfolgreich war.

## Attributionsdaten von Facebook und X (ehemals Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Attributionsdaten für Facebook- und X-Campaigns (ehemals Twitter) sind nicht über unsere Partner verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attributionsdaten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Kochava-Click-Tracking-URLs in Braze (optional)

Wenn Sie Click-Tracking-Links in Ihren Braze-Campaigns verwenden, können Sie leicht erkennen, welche Campaigns zu App-Installationen und erneuter Interaktion führen. So können Sie Ihre Marketing-Bemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen für einen maximalen ROI investieren sollten.

Um mit Kochava-Click-Tracking-Links zu beginnen, besuchen Sie die [Dokumentation](https://support.kochava.com/reference-information/attribution-overview/). Sie können die Kochava-Click-Tracking-Links direkt in Ihre Braze-Campaigns einfügen. Kochava verwendet dann seine [probabilistischen Attributionsmethoden](https://www.kochava.com/getting-prepared-for-ios-14/), um die Nutzer:innen zuzuordnen, die auf den Link geklickt haben. Wir empfehlen, Ihre Kochava-Tracking-Links mit einem Geräte-Bezeichner zu versehen, um die Genauigkeit der Attributionen Ihrer Braze-Campaigns zu verbessern. Dadurch werden die Nutzer:innen, die auf den Link geklickt haben, deterministisch attributiert.

{% tabs local %}
{% tab Android %}
Für Android erlaubt Braze Kund:innen, sich für die [Erfassung der Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id) zu entscheiden. Die GAID wird auch nativ über die Kochava-SDK-Integration erfasst. Sie können die GAID in Ihre Kochava-Click-Tracking-Links integrieren, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Kochava den IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Geräte-Bezeichner verwendet werden. Sie können den IDFV in Ihre Kochava-Click-Tracking-Links integrieren, indem Sie die folgende Liquid-Logik verwenden:

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
Wenn Sie derzeit keine Geräte-Bezeichner – wie IDFV oder GAID – in Ihren Click-Tracking-Links verwenden oder dies in Zukunft nicht vorhaben, ist Kochava dennoch in der Lage, diese Klicks durch seine probabilistische Modellierung zu attributieren.
{% endalert %}