---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und AppsFlyer, einer Analytics-Plattform für Mobile-Marketing und Attribution, die Ihnen hilft, Ihre Apps zu analysieren und zu optimieren."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> [AppsFlyer](https://www.appsflyer.com/) ist eine Analytics-Plattform für Mobile-Marketing und Attribution, die Ihnen hilft, Ihre Apps durch Marketing-Analysen, Mobile-Attribution und Deeplinking zu analysieren und zu optimieren.

Die Integration von Braze und AppsFlyer lässt Sie besser verstehen, wie Sie Ihre Campaigns optimieren und ganzheitlicher gestalten können, indem Sie die mobilen Install-Attribution-Daten von AppsFlyer nutzen.

Mit der [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences/)-Integration können Sie Ihre AppsFlyer-Zielgruppen (Kohorten) direkt an Braze weitergeben, was es Ihnen erlaubt, leistungsstarke Customer-Engagement-Campaigns zu erstellen, die genau auf die richtigen Nutzer:innen zur richtigen Zeit ausgerichtet sind.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| AppsFlyer-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein AppsFlyer-Konto. |
| iOS- oder Android-App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code-Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| AppsFlyer SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started) installieren.
| Einrichtung der E-Mail-Domain abgeschlossen | Sie müssen beim Onboarding von Braze den [Schritt zur Einrichtung von IP und Domain]({{site.baseurl}}/user_guide/channels/email/email_setup/setting_up_ips_and_domains/) abgeschlossen haben, um Ihre E-Mail einzurichten. |
| SSL-Zertifikat | Ihr [SSL-Zertifikat]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate) muss konfiguriert sein. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### 1. Schritt: Geräte-ID abbilden {#step-1-map-device-id}

{% tabs local %}
{% tab Android %}
Wenn Sie eine Android-App haben, müssen Sie eine eindeutige Braze-Geräte-ID an AppsFlyer übergeben.

Stellen Sie sicher, dass die folgenden Code-Zeilen an der richtigen Stelle eingefügt werden – nachdem das Braze SDK gestartet wurde und vor dem Initialisierungscode für das AppsFlyer SDK. Weitere Informationen finden Sie im AppsFlyer [SDK-Integrationshandbuch für Android](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk).

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
Vor Februar 2023 verwendete unsere AppsFlyer-Attribution-Integration den Identifier for Vendors (IDFV) als primären Bezeichner, um iOS-Attribution-Daten abzugleichen. Für Braze-Kund:innen, die Objective-C verwenden, ist es nicht notwendig, die Braze `device_id` abzurufen und sie bei der Installation an AppsFlyer zu senden, da es keine Unterbrechung des Dienstes gibt.
{% endalert%}

Wenn Sie das Swift SDK v5.7.0+ verwenden und weiterhin IDFV als gegenseitigen Bezeichner verwenden möchten, müssen Sie sicherstellen, dass das Feld `useUUIDAsDeviceId` auf `false` gesetzt ist, um eine Unterbrechung der Integration zu vermeiden.

Wenn Sie diese Option auf `true` setzen, müssen Sie die Abbildung der iOS-Geräte-ID für Swift implementieren, um die Braze `device_id` bei der Installation der App an AppsFlyer weiterzugeben, damit Braze die iOS-Attributionen richtig zuordnen kann.

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab unity %}
Um die Geräte-ID in Unity abzubilden, gehen Sie wie folgt vor:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### 2. Schritt: Datenimport-Schlüssel für Braze abrufen {#step-2-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologie-Partner** und wählen Sie **AppsFlyer** aus.

Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im AppsFlyer-Dashboard einrichten.<br><br>![Das Feld „Datenimport für Install-Attribution“ ist auf der AppsFlyer-Technologie-Seite verfügbar. In diesem Feld sind der Datenimport-Schlüssel und der REST-Endpunkt enthalten.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### 3. Schritt: Braze im Dashboard von AppsFlyer konfigurieren {#step-3-configure-braze-in-appsflyers-dashboard}

1. Navigieren Sie in AppsFlyer auf die Seite **Integrated Partners** in der linken Leiste. Suchen Sie dann nach **Braze** und wählen Sie das Braze-Logo aus, um ein Konfigurationsfenster zu öffnen.
2. Schalten Sie auf dem Tab **Integration** die Option **Activate Partner** ein.
3. Geben Sie den Datenimport-Schlüssel und den REST-Endpunkt an, den Sie im Braze-Dashboard gefunden haben.
4. Schalten Sie **Advanced Privacy** aus und speichern Sie Ihre Konfiguration.

{% alert important %}
Wenn Sie den Braze-REST-Endpunkt im Tab „Integration“ von AppsFlyer eingeben, geben Sie nur die Domain ein (z. B. `rest.fra-02.braze.eu`) ohne das Protokoll `https://` und ohne den Pfad `/attribution/appsflyer`. AppsFlyer stellt das Protokoll automatisch voran und hängt den Pfad an. Wenn Sie eines von beiden in Ihre Eingabe aufnehmen, führt dies zu Postback-Fehlern.
{% endalert %}

Weitere Informationen zu diesen Anweisungen finden Sie in der [AppsFlyer-Dokumentation](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### 4. Schritt: Integration bestätigen {#step-4-confirm-the-integration}

Auf der AppsFlyer-Technologie-Partnerseite in Braze zeigt der Verbindungsindikator **Not Connected** an, bis Sie in Schritt 2 einen Datenimport-API-Schlüssel generieren. Nachdem Sie den Schlüssel generiert haben, ändert sich der Indikator zu **Connected** und zeigt einen Zeitstempel an. Dieser Zeitstempel gibt an, wann die Integration erstmals in Braze eingerichtet wurde (als der Datenimport-Schlüssel erstellt wurde), nicht wann AppsFlyer zuletzt ein Postback gesendet hat.

Um zu bestätigen, dass Install-Attribution-Daten von AppsFlyer fließen, verwenden Sie Schritt 5, um zu überprüfen, ob nicht-organische Installationsdaten in den Braze-Segmentfiltern erscheinen. Braze ignoriert organische Installationen aus AppsFlyer-Postbacks und speichert sie nicht als attributierte Installationsdaten.

### 5. Schritt: Daten zur Nutzer:innen-Attribution anzeigen {#step-5-viewing-user-attribution-data}

#### Verfügbare Datenfelder {#available-data-fields}

Wenn Ihre Integration erfolgreich war, bildet Braze alle nicht-organischen Installationsdaten in Segmentfiltern ab.

| AppsFlyer-Datenfeld | Braze-Segmentfilter |
| -------------------- | --------------------- |
| `media_source` | Attributed Source |
| `campaign` | Attributed Campaign |
| `af_adset` | Attributed Adgroup |
| `af_ad` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Available data fields" }

Im Braze-Dashboard können Sie Ihre Nutzerbasis anhand von Attributionsdaten segmentieren, indem Sie die Filter für Install-Attribution verwenden.

![Vier verfügbare Filter. Der erste ist „Install Attribution Source ist network_val_0“. Der zweite ist „Install Attribution Source ist campaign_val_0“. Der dritte ist „Install Attribution Source ist adgroup_val_0“. Der vierte ist „Install Attribution Source ist creative_val_0“. Neben den aufgeführten Filtern können Sie sehen, wie diese Attributionsquellen dem Nutzerprofil hinzugefügt werden. Im Feld „Install Attribution“ auf der Informationsseite einer Nutzer:in wird die Installationsquelle als network_val_0 aufgeführt, die Campaign als campaign_val_0 usw.]({% image_buster /assets/img/braze_attribution.png %})

Außerdem sind die Attributionsdaten für eine bestimmte Nutzer:in auf dem Profil jeder Nutzer:in im Braze-Dashboard verfügbar.

{% alert note %}
Attribution-Daten für Facebook- und X-Campaigns (ehemals Twitter) sind nicht über unsere Partner verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attribution-Daten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.
{% endalert %}

## AppsFlyer mit Braze für Deeplinking integrieren {#integrate-appsflyer-with-braze-for-deep-linking}

Deeplinks&#8212;Links, die Nutzer:innen zu einer bestimmten Seite oder Stelle innerhalb einer App oder Website führen&#8212;werden verwendet, um ein maßgeschneidertes Nutzer-Erlebnis zu schaffen.

Obwohl weit verbreitet, können bei der Verwendung von per E-Mail versendeten Deeplinks mit Click-Tracking&#8212;einem weiteren wichtigen Feature für die Erfassung von Nutzerdaten&#8212;Probleme auftreten. Diese Probleme sind darauf zurückzuführen, dass E-Mail-Anbieter (ESPs) Deeplinks in eine Domain zur Aufzeichnung von Klicks einbetten, wodurch der ursprüngliche Link unterbrochen wird. Die Unterstützung von Deeplinks erfordert daher eine zusätzliche Einrichtung.

AppsFlyer bietet einen [Dienst](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer), der diese Probleme vermeidet, indem AppsFlyer als Vermittler zwischen dem ESP-Server und Ihrer Domain fungiert. Seine Rolle als Proxy ermöglicht die Bereitstellung von Assoziationsdateien (AASA/Asset-Links), die das Deeplinking erleichtern.

## 1. Schritt: Click-Tracking-Domain erstellen {#step-1-create-a-click-tracking-domain}

Befolgen Sie die ersten Elemente der [E-Mail-Einrichtungsanleitung von Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate) und erstellen Sie eine Domain für den E-Mail-Versand und eine Domain für das Click-Tracking. Für Support können Sie über das Braze-Dashboard ein Ticket erstellen, um die Einrichtung der neuen CTD beim Braze-E-Mail-Team einzuleiten.

![Braze-UI mit dem Button „Get Help“, der sich unter dem Button „Support“ in der rechten oberen Ecke befindet]({% image_buster /assets/img/attribution/appsflyer/1.png %})

Die Erstellung einer neuen CTD ist Pflicht, auch wenn Sie bereits eine bestehende verwenden. Dadurch wird sichergestellt, dass es keine Auswirkungen auf den Datenverkehr der laufenden Live-E-Mail-Campaigns gibt.

{% alert important%}
AppsFlyer erstellt das SSL-Zertifikat. In diesem Stadium sind E-Mail-Links wahrscheinlich nicht gesichert, d. h. der URL-Präfix ist HTTP statt HTTPS. Dies wird in späteren Schritten behoben.
{%endalert%}

## 2. Schritt: OneLink-Template in AppsFlyer erstellen {#step-2-create-a-onelink-template-in-appsflyer}
Erstellen Sie ein [OneLink-Template](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures) und konfigurieren Sie Universal Links/App Links unter „When app is installed“. Dieses Template wird später verwendet, um OneLink-Links für Ihre E-Mail-Campaigns zu erstellen.

{% alert note%} Wenn Sie bereits ein OneLink-Template konfiguriert haben, das Universal Links/App Links aktiviert, können Sie es verwenden.
{%endalert%}

## 3. Schritt: Braze-Integration in AppsFlyer einrichten {#step-3-set-up-your-braze-integration-in-appsflyer}
Jetzt ist es an der Zeit, Ihre Braze-Integration in AppsFlyer einzurichten. Dieser Schritt und der folgende Schritt („App konfigurieren“) können gleichzeitig eingerichtet werden.
So richten Sie Ihre Braze-Integration in AppsFlyer ein:

### 1. Wählen Sie in AppsFlyer aus dem Seitenmenü Engage > ESP Integration {#1-in-appsflyer-from-the-side-menu-select-engage-esp-integration}
![AppsFlyer-UI mit dem Button „ESP Integration“, der sich im linken Menü befindet]({% image_buster /assets/img/attribution/appsflyer/2.png %})


### 2. Wählen Sie Braze aus {#2-select-braze}
![AppsFlyer-UI zeigt die Liste der ESP-Integrationen, einschließlich Braze.]({% image_buster /assets/img/attribution/appsflyer/3.png %})


### 3. Wählen Sie das OneLink-Template aus, das Sie für Ihre E-Mail-Campaigns verwenden möchten, und klicken Sie dann auf „Next“ {#3-select-the-onelink-template-you-want-to-use-for-email-campaigns-then-click-next}
![AppsFlyer-UI zeigt das Dropdown-Menü, mit dem Nutzer:innen ihr Template auswählen können.]({% image_buster /assets/img/attribution/appsflyer/4.png %})


### 4. Geben Sie Ihre Click-Tracking-Domain und den Wert für den „Braze endpoint“ ein, der mit der in Schritt 1 erstellten neuen CTD bereitgestellt wurde, und klicken Sie dann auf „Validate connection“ {#4-enter-your-click-tracking-domain-and-braze-endpoint-value-which-was-provided-with-the-new-ctd-created-in-step-1-then-click-validate-connection}

Damit wird bestätigt, dass die Click-Tracking-Domain auf den von Ihnen angegebenen Endpunkt verweist.

![AppsFlyer-UI, die hervorhebt, wo Kund:innen ihre Click-Tracking-Domain und die zugehörigen Details hinzufügen sollten.]({% image_buster /assets/img/attribution/appsflyer/5.png %})

Mit „Braze Endpoint“ fragt AppsFlyer nach den von Braze in [Schritt 1](#step-1-create-a-click-tracking-domain) dieser Anleitung angegebenen Details, insbesondere nach der neuen CTD.

Klicken Sie dann auf **Validate connection**, um zu überprüfen, ob die Click-Tracking-Domain auf den von Ihnen eingegebenen Endpunkt zeigt.
Wenn Sie fertig sind, klicken Sie auf **Next**.

### 5. Leiten Sie den Link-Datenverkehr an AppsFlyer weiter {#5-route-link-traffic-to-appsflyer}

#### a. Kopieren Sie die angepassten, vorgefertigten Anweisungen in AppsFlyer und senden Sie sie an Ihren IT- oder Domain-Administrator {#a-copy-and-send-the-customized-pre-fabricated-instructions-in-appsflyer-to-your-it-or-domain-administrator}

Ihr Administrator muss den Datenverkehr Ihrer E-Mail-Campaigns von den ESP-Servern zu den AppsFlyer-Servern umleiten, indem er Ihre DNS-CNAME-Einträge mit der neuen Domain aktualisiert, die AppsFlyer zur Verfügung gestellt hat.

Daher wird jeder Klick auf einen Link an AppsFlyer weitergeleitet, das ihn wiederum an den ESP-Endpunkt weiterleitet.

![Diagramm zur Veranschaulichung, wie Klick-Daten von Ihrer Domain zu AppsFlyer und zu Ihrem ESP-Endpunkt gelangen]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. Nachdem Sie die Anweisungen kopiert und abgeschickt haben, klicken Sie auf „Done“ {#b-after-copying-and-sending-the-instructions-click-done}
Ihre Braze-Integration wurde erstellt.

{%alert important%}
Der Status Ihrer Braze-Integration ist ausstehend und funktioniert erst, wenn der CNAME-Eintrag zugeordnet ist. Es kann bis zu 24 Stunden nach der Zuordnung dauern, bis eine neue Integration funktioniert und aktiv wird.
{%endalert%}

## 4. Schritt: App konfigurieren (Entwickler:in-Aufgabe) {#step-4-configure-your-app-developer-task}
AppsFlyer [bietet eine Anleitung](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task) zur korrekten App-Konfiguration, die von Ihren Web- oder App-Teams befolgt werden sollte, um Universal Linking zu unterstützen.

## 5. Schritt: Bestätigen, dass SSL-Click-Tracking mit Braze aktiviert ist {#step-5-confirm-ssl-click-tracking-is-enabled-with-braze}

In diesem Stadium, nachdem Sie die CTD-Details in AppsFlyer freigegeben und validiert haben, empfehlen wir Ihnen, einen Testversand durchzuführen, um zu überprüfen, ob Ihre OneLink-Sendedomain über ein SSL-Zertifikat verfügt. Dies entspricht unserer Anleitung zur [E-Mail-Einrichtung](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate).

Sie können eine Qualitätssicherung und Fehlerbehebung durchführen, indem Sie mit OneLink einen Deeplink senden. Einzelheiten zur Verwendung von OneLink finden Sie in der [AppsFlyer-Dokumentation](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a).

Wenn CTD-Links als HTTP identifiziert werden, wenden Sie sich an das E-Mail-Ops-Team von Braze, um das SSL-Click-Tracking zu aktivieren. Dadurch wird sichergestellt, dass alle HTTP-Links automatisch in HTTPS umgewandelt werden.
Sie können den folgenden Beispieltext für eine Nachricht verwenden, wenn Sie sich an Ihren Customer-Success-Manager wenden, oder indem Sie wie in [Schritt 1](#step-1-create-a-click-tracking-domain) ein Ticket im Braze-Dashboard erstellen:

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS.
```

### AppsFlyer-Click-Tracking-URLs in Braze (optional)

Sie können die [OneLink-Attribution-Links](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) von AppsFlyer in Braze-Campaigns für Push, E-Mail und mehr verwenden. Dies erlaubt es Ihnen, Daten zur Install-Attribution oder zur erneuten Interaktion aus Ihren Braze-Campaigns an AppsFlyer zurückzusenden. Auf diese Weise können Sie Ihre Marketing-Bemühungen effektiver messen und datengestützte Entscheidungen treffen.

Sie können Ihre OneLink-Tracking-URL einfach in AppsFlyer erstellen und sie direkt in Ihre Braze-Campaigns einfügen. AppsFlyer verwendet dann seine [probabilistischen Attributionsmethoden](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling), um die Nutzer:innen zu attributieren, die auf den Link geklickt haben. Wir empfehlen, Ihre AppsFlyer-Tracking-Links mit einem Gerätebezeichner zu versehen, um die Genauigkeit der Attributionen Ihrer Braze-Campaigns zu verbessern. Dadurch werden die Nutzer:innen, die auf den Link geklickt haben, deterministisch attributiert.

{% tabs local %}
{% tab Android %}
Für Android erlaubt Braze seinen Kund:innen, die [Sammlung der Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id) zu aktivieren. Die AppsFlyer-SDK-Integration sammelt ebenfalls die GAID. Sie können die GAID in Ihre AppsFlyer-Click-Tracking-Links integrieren, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch AppsFlyer den IDFV automatisch und nativ über unsere SDK-Integrationen. Sie können den IDFV als Gerätebezeichner verwenden. Sie können den IDFV in Ihre AppsFlyer-Click-Tracking-Links aufnehmen, indem Sie die folgende Liquid-Logik verwenden:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}