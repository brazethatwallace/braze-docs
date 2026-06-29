---
nav_title: Linkrunner
article_title: Linkrunner
alias: /partners/linkrunner/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Linkrunner, einer mobilen Attributions- und Analytics-Plattform, mit der Sie Attributionsdaten importieren können, um Ihre Nutzerakquise-Kampagnen besser zu verstehen."
page_type: partner
search_tag: Partner

---

# Linkrunner

> [Linkrunner](https://linkrunner.io/) ist eine mobile Attributions- und Analytics-Plattform, die Ihnen hilft, Ihre Nutzerakquise-Kampagnen zu verfolgen und zu analysieren.

_Diese Integration wird von Linkrunner gepflegt._

## Über die Integration {#about-the-integration}

Die Integration von Braze und Linkrunner ermöglicht es Ihnen, Attributionsdaten zu importieren, um besser zu verstehen, welche Kampagnen die Nutzerakquise und das Engagement fördern.

## Voraussetzungen {#prerequisites}

Folgendes ist erforderlich, bevor Sie beginnen:

| Anforderung | Beschreibung |
|---|---|
| Linkrunner-Konto | Ein Linkrunner-Konto ist erforderlich, um diese Partnerschaft zu nutzen. |
| iOS- oder Android-App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code-Snippets in Ihrer Anwendung erforderlich sein. |
| Linkrunner SDK | Sie müssen das [Linkrunner SDK](https://docs.linkrunner.io/introduction) installieren. |
| Braze SDK | Sie müssen das [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/) integrieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Nutzer-IDs zuordnen {#step-1-map-user-ids}

Wenn Sie die Braze SDK-Funktion `changeUser` verwenden, übergeben Sie dieselbe Nutzer-ID im Parameter `userData` der Linkrunner SDK-Funktion `signup`.

Wenn Sie `changeUser` nicht verwenden, übergeben Sie die `brazeDeviceId` im Parameter `userData` der Linkrunner SDK-Funktion `signup`. Rufen Sie die `brazeDeviceId` vom Braze SDK ab.

{% tabs local %}
{% tab Android (Kotlin) %}
```kotlin
val userData = UserDataRequest(
    id = "123", // Your user ID
    // ...other user fields
    brazeDeviceId = "BRAZE_DEVICE_ID", // Braze device ID from the Braze SDK (Required if you are not using the changeUser function)
)

LinkRunner.getInstance().signup(userData = userData)
```
{% endtab %}

{% tab iOS (Swift) %}
```swift
let userData = UserData(
    id: "123", // Your user ID
    // ...other user fields
    brazeDeviceId: "BRAZE_DEVICE_ID" // Braze Device ID from the Braze SDK (Required if you are not using the changeUser function)
)

try await LinkrunnerSDK.shared.signup(userData: userData)
```
{% endtab %}
{% endtabs %}

### 2. Schritt: API-Schlüssel in Braze erstellen {#step-2-create-api-key-in-braze}

Gehen Sie in Ihrem Braze-Dashboard zu **Einstellungen** > **Einrichtung und Tests** > **APIs und Bezeichner** > **API-Schlüssel**.

1. Wählen Sie **API-Schlüssel erstellen**.
2. Wählen Sie unter **Nutzerdaten** die folgenden Berechtigungen aus:
   - `users.track`
   - `users.export.ids`
3. Speichern Sie den API-Schlüssel.
4. Kopieren Sie den API-Schlüssel und den REST-Endpunkt. Fügen Sie diese Werte im nächsten Schritt in Linkrunner ein. Behandeln Sie den API-Schlüssel als Geheimnis und teilen Sie ihn nicht öffentlich.

### 3. Schritt: Braze im Linkrunner-Dashboard konfigurieren {#step-3-configure-braze-in-linkrunners-dashboard}

1. Gehen Sie in Linkrunner im linken Panel zu **Integrationen**.
2. Wählen Sie unter **Analytics** die Option **Konfigurieren** für Braze.
3. Geben Sie den API-Schlüssel und den REST-Endpunkt ein, die Sie in [Schritt 2](#step-2-create-api-key-in-braze) kopiert haben.

Weitere Informationen finden Sie in der [Linkrunner-Dokumentation](https://docs.linkrunner.io/analytics-integrations/braze).

### 4. Schritt: Nutzer-Attributionsdaten anzeigen {#step-4-view-user-attribution-data}

Linkrunner sendet `lr_campaign` und `lr_ad_network` als angepasste Attribute. Sie können diese Daten im Abschnitt **Angepasste Attribute** des Nutzerprofils im Braze-Dashboard einsehen.

## Attributionsdaten von Facebook und X (ehemals Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Attributionsdaten für Kampagnen auf Facebook und X (ehemals Twitter) sind über unsere Partner nicht verfügbar. Diese Medienquellen gestatten es ihren Partnern nicht, Attributionsdaten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.