---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Adjust, einem Unternehmen für mobile Attribution und Analytics, das es Ihnen ermöglicht, Daten zur nicht-organischen Install-Attribution zu importieren, um innerhalb Ihrer Lebenszyklus-Kampagnen intelligenter zu segmentieren."
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust](https://www.adjust.com/) ist ein Unternehmen für mobile Attribution und Analytics, das Attribution für Werbequellen mit fortschrittlichen Analytics für ein umfassendes Bild der Business-Intelligence kombiniert.

_Diese Integration wird von Adjust gepflegt._

## Über die Integration {#about-the-integration}

Mit der Integration von Braze und Adjust können Sie Daten zur nicht-organischen Install-Attribution importieren, um innerhalb Ihrer Lebenszyklus-Kampagnen intelligenter zu segmentieren.

## Voraussetzungen {#prerequisites}

| Anforderung | Beschreibung |
|---|---|
| Adjust-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein Adjust-Konto erforderlich. |
| iOS- oder Android-App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code-Snippets in Ihrer Anwendung erforderlich sein. Einzelheiten zu diesen Anforderungen finden Sie in Schritt 1 des Integrationsprozesses. |
| Adjust SDK | Neben dem erforderlichen Braze SDK müssen Sie auch das [Adjust SDK](https://dev.adjust.com/en/sdk) installieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voraussetzungen" }

## Integration

### 1. Schritt: Geräte-IDs zuordnen {#step-1-map-device-ids}

#### Android

Wenn Sie eine Android-App haben, müssen Sie eine eindeutige Braze-Geräte-ID an Adjust übergeben. Diese ID kann in der Methode `addGlobalPartnerParameter()` des Adjust SDK festgelegt werden. Der folgende Code-Snippet muss vor der Initialisierung des SDK auf `Adjust.initSdk.` eingefügt werden.

```
Adjust.addGlobalPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the Identifier for Vendor (IDFV) as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation because there is no service disruption.
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration.

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs local %}
{% tab Objective-C %}

Wenn Sie eine iOS-App haben, wird Ihr IDFV von Adjust erfasst und an Braze gesendet. Diese ID wird dann einer eindeutigen Geräte-ID in Braze zugeordnet.

Braze speichert weiterhin IDFA-Werte für Nutzer:innen, die sich für das Opt-in entschieden haben, wenn Sie den IDFA mit Braze erfassen, wie in unserem [iOS-Upgrade-Leitfaden]({{site.baseurl}}/developer_guide/platforms/swift/ios_18/) beschrieben. Andernfalls wird der IDFV als Fallback-Bezeichner für die Zuordnung von Nutzer:innen verwendet.

{% endtab %}
{% tab Swift %}

Wenn Sie eine iOS-App haben, können Sie sich für die Erfassung von IDFV entscheiden, indem Sie das Feld `useUUIDAsDeviceId` auf `false` setzen. Wenn diese Option nicht gesetzt ist, wird die iOS-Attribution wahrscheinlich nicht korrekt von Adjust auf Braze abgebildet. Weitere Informationen finden Sie unter [IDFV erfassen]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift).

{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Sie planen, Post-Install-Ereignisse von Adjust an Braze zu senden, müssen Sie Folgendes tun: <br><br>1) Stellen Sie sicher, dass Sie `external_id` als Sitzungs- und Ereignisparameter innerhalb des Adjust SDK anhängen. Für die Weiterleitung von Umsatzereignissen müssen Sie auch `product_id` als Parameter für Ereignisse einrichten. In der [Dokumentation von Adjust](https://github.com/adjust/sdks) finden Sie weitere Informationen zur Definition von Partner-Parametern für die Ereignisweiterleitung.<br><br>2) Generieren Sie einen neuen API-Schlüssel für die Eingabe in Adjust. Wählen Sie dazu den Button **Generate API Key** auf der Adjust-Partnerseite im Braze-Dashboard.
{% endalert %}

### 2. Schritt: Braze-Datenimport-Schlüssel abrufen {#step-2-get-the-braze-data-import-key}

Navigieren Sie in Braze zu **Integrationen** > **Technologie-Partner** und wählen Sie **Adjust**.

Hier finden Sie den REST-Endpunkt und können Ihren Braze-Datenimport-Schlüssel generieren. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Adjust einrichten.<br><br>![Dieses Bild zeigt das Feld „Datenimport für Install-Attribution“ auf der Adjust-Technologieseite. In diesem Feld werden Ihnen der Datenimport-Schlüssel und der REST-Endpunkt angezeigt.]({% image_buster /assets/img/attribution/adjust.png %}){: style="max-width:90%;"}

### 3. Schritt: Braze in Adjust konfigurieren {#step-3-configure-braze-in-adjust}

1. Navigieren Sie im Dashboard von Adjust zu **App Settings** und dann zu **Partner Setup** und **Add Partners**.
2. Wählen Sie **Braze (formerly Appboy)** und geben Sie den Datenimport-Schlüssel und den Braze-REST-Endpunkt an.
3. Klicken Sie auf **Save & Close**.

### 4. Schritt: Integration bestätigen {#step-4-confirm-the-integration}

Nachdem Braze Attribution-Daten von Adjust erhalten hat, ändert sich die Statusanzeige der Verbindung auf der Adjust-Technologie-Partnerseite in Braze von „Nicht verbunden“ zu „Verbunden“ und enthält einen Zeitstempel der letzten erfolgreichen Anfrage.

Dieser Status ändert sich erst, wenn Braze Daten über eine attributierte Installation erhält. Braze ignoriert organische Installationen (schließt sie aus dem Adjust-Postback aus) und zählt sie nicht bei der Bestimmung, ob die Verbindung erfolgreich ist.

## Verfügbare Datenfelder {#available-data-fields}

Unter der Voraussetzung, dass Sie Ihre Integration wie vorgeschlagen konfigurieren, ordnet Braze die Daten von Adjust den Segmentfiltern zu, wie in der folgenden Tabelle beschrieben.

| Adjust-Datenfeld | Braze-Segmentfilter |
| --- | --- |
| `{network_name}` | Attributed Source |
| `{campaign_name}` | Attributed Campaign |
| `{adgroup_name}` | Attributed Adgroup |
| `{creative_name}` | Attributed Ad |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Verfügbare Datenfelder" }

## Attribution-Daten von Facebook und X (ehemals Twitter) {#facebook-and-x-formerly-twitter-attribution-data}

Attribution-Daten für Facebook- und X-Kampagnen (ehemals Twitter) sind nicht über unsere Partner verfügbar. Diese Medienquellen erlauben ihren Partnern nicht, Attribution-Daten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Adjust-Klick-Tracking-URLs in Braze (optional) {#adjust-click-tracking-urls-in-braze-optional}

Wenn Sie Klick-Tracking-Links in Ihren Braze-Kampagnen verwenden, können Sie leicht erkennen, welche Kampagnen zu App-Installationen und erneuter Interaktion führen. So können Sie Ihre Marketingmaßnahmen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen für einen maximalen Kapitalrendite investieren sollten.

Um mit Adjust-Klick-Tracking-Links zu beginnen, besuchen Sie die [Dokumentation](https://help.adjust.com/tracking/attribution/tracker-urls). Sie können die Adjust-Klick-Tracking-Links direkt in Ihre Braze-Kampagnen einfügen. Adjust verwendet dann seine [probabilistischen Attribution-Methoden](https://www.adjust.com/blog/attribution-compatible-with-ios14/), um die Nutzer:innen zu attributieren, die auf den Link geklickt haben. Wir empfehlen, Ihre Adjust-Tracking-Links mit einem Geräte-Bezeichner zu versehen, um die Genauigkeit der Attributionen Ihrer Braze-Kampagnen zu verbessern. Dadurch werden die Nutzer:innen, die auf den Link geklickt haben, deterministisch attributiert.

{% tabs local %}
{% tab Android %}
Für Android erlaubt Braze Kund:innen, sich für die [Erfassung der Google Advertising ID (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration/#google-advertising-id) zu entscheiden. Die GAID wird auch nativ über die Adjust-SDK-Integration erfasst. Sie können die GAID in Ihre Adjust-Klick-Tracking-Links einfügen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Adjust den IDFV automatisch und nativ über unsere SDK-Integrationen. Dieser kann als Geräte-Bezeichner verwendet werden. Sie können den IDFV in Ihre Adjust-Klick-Tracking-Links einfügen, indem Sie die folgende Liquid-Logik verwenden:

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
Wenn Sie in Ihren Klick-Tracking-Links derzeit keine Geräte-Bezeichner wie den IDFV oder die GAID verwenden oder dies in Zukunft nicht vorhaben, kann Adjust diese Klicks dennoch durch seine probabilistische Modellierung attributieren.
{% endalert %}