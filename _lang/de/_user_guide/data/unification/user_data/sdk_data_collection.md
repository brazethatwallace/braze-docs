---
nav_title: SDK-Datenerfassung
article_title: SDK-Datenerfassung
page_order: 1
page_type: reference
description: "Dieser Referenzartikel befasst sich mit den Daten, die vom SDK über personalisierte Integrationen, automatisch erfasste Integrationen und minimale Integrationen gesammelt werden."
---

# SDK-Datenerfassung {#sdk-data-collection}

> Wenn Sie das Braze SDK in Ihre App oder Website integrieren, sammelt Braze automatisch bestimmte Arten von Daten. Einige dieser Daten sind für unsere Prozesse unerlässlich, und einige dieser Daten können je nach Ihren Bedürfnissen ein- oder ausgeschaltet werden. Sie können Braze auch so konfigurieren, dass es weitere Datentypen erfasst, um Segmentierung und Messaging zu verbessern.

Braze ist auf eine flexible Datenerfassung ausgelegt. Daher können Sie das Braze SDK auf folgende Weise integrieren:

- **[Minimale Integration](#minimum-integration):** Braze sammelt automatisch Daten, die für die Kommunikation mit den Braze-Diensten erforderlich sind.
- **[Optionale Daten, die standardmäßig erfasst werden](#optional-data-collected-by-default):** Braze erfasst automatisch bestimmte Daten, die für die meisten Anwendungsfälle nützlich sind. Sie können die automatische Erfassung dieser Daten deaktivieren, wenn sie für die Kommunikation mit den Diensten von Braze nicht erforderlich sind.
- **[Optionale Daten, die standardmäßig nicht erfasst werden](#data-not-collected-by-default):** Braze erfasst bestimmte Daten, die für einzelne Anwendungsfälle nützlich sind, tut dies aber aus allgemeinen Compliance-Gründen nicht automatisch. Sie können diese Daten in den Fällen erfassen lassen, in denen dies zweckdienlich ist.
- **[Personalisierte Integration](#personalized-integration):** Braze bietet Ihnen die Möglichkeit, zusätzlich zu den standardmäßigen optionalen Daten weitere Daten zu erfassen.

## Mindestintegration {#minimum-integration}

In der folgenden Liste sind die streng notwendigen Daten aufgeführt, die von Braze generiert und empfangen werden, wenn Sie das SDK initialisieren. Diese Daten sind nicht konfigurierbar und für die Kernfunktionen der Plattform unerlässlich. Mit Ausnahme von Sitzungsstart und Sitzungsende zählen alle anderen automatisch erfassten Daten nicht zu Ihrer Datenpunkt-Nutzung.

| Attribut | Beschreibung | Warum es erfasst wird |
| --------- | ----------- | ------------------ |
| App-Versionsname /<br> App-Versionscode | Die neueste App-Version | Dieses Attribut wird verwendet, um Nachrichten zur App-Versionskompatibilität an die richtigen Geräte zu senden. Es kann verwendet werden, um Nutzer:innen über Dienstunterbrechungen oder Fehler zu informieren. |
| Land | Land, identifiziert durch IP-Adress-Geolocation. Wenn die IP-Adress-Geolocation nicht verfügbar ist, wird es anhand der [Geräte-Locale](#optional-data-collected-by-default) identifiziert. Der Wert kann alternativ das sein, was die SDKs direkt mit `setCountry` festlegen, aber beachten Sie, dass das Übergeben eines Attributwerts per SDK oder API Datenpunkte protokolliert. **Nachdem das Land manuell festgelegt wurde (über die SDK-Methode, REST API oder CSV-Upload), aktualisiert das SDK diesen Wert nicht mehr automatisch.** | Dieses Attribut wird verwendet, um Nachrichten basierend auf dem Standort zu targeten. |
| Geräte-ID | Gerätebezeichner, ein zufällig generierter String | Dieses Attribut wird verwendet, um die Geräte der Nutzer:innen zu unterscheiden und Nachrichten an das richtige Gerät zu senden. |
| Betriebssystem und Betriebssystemversion | Aktuell gemeldetes Gerät oder Browser und Geräte- oder Browserversion | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden. Es kann auch innerhalb der Segmentierung verwendet werden, um Nutzer:innen zum Upgrade von App-Versionen anzusprechen. |
| Sitzungsstart und Sitzungsende | Wann der/die Nutzer:in beginnt, Ihre integrierte App oder Website zu verwenden | Das Braze SDK meldet Sitzungsdaten, die vom Braze-Dashboard verwendet werden, um das Nutzer:innen-Engagement und andere Analytics zu berechnen, die für das Verständnis Ihrer Nutzer:innen wesentlich sind. Wann genau der Sitzungsstart und das Sitzungsende von Ihrer App oder Website aufgerufen wird, kann von Entwickler:innen konfiguriert werden ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)). |
| SDK-Nachrichteninteraktionsdaten | Push-Direktöffnungen, In-App-Nachricht-Interaktionen, Content-Card-Interaktionen | Dieses Attribut wird zur Qualitätskontrolle verwendet, z. B. um zu prüfen, ob eine Nachricht empfangen wurde und ob der Versand nicht dupliziert wird. |
| SDK-Version | Aktuelle SDK-Version | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden und Dienstunterbrechungen zu vermeiden. |
| Sitzungs-ID und Sitzungszeitstempel | Sitzungsbezeichner, ein zufällig generierter String und Sitzungszeitstempel | Wird verwendet, um festzustellen, ob der/die Nutzer:in eine neue oder bestehende Sitzung startet, und um die erneute Berechtigung für Nachrichten zu bestimmen, die für diese:n Nutzer:in bestimmt sind.<br><br>Bestimmte Messaging-Kanäle wie In-App-Nachrichten und Content Cards werden beim Sitzungsstart mit dem Gerät synchronisiert. Unser Backend verwendet dann Daten darüber, wann es zuletzt die Braze-Server kontaktiert hat (die das Gerät speichert und zurücksendet), um festzustellen, ob der/die Nutzer:in für neue Nachrichten berechtigt ist.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mindestintegration" }

### Berechnete Metriken {#calculated-metrics}

Braze generiert berechnete Metriken aus drei Eingaben: [SDK-erfasste Daten](#minimum-integration) (zum Beispiel [Sitzungsstart und Sitzungsende]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)), [Nachrichteninteraktionsdaten für Nicht-SDK-Kanäle]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und [von Braze abgeleitete Berichtsfelder]({{site.baseurl}}/user_guide/analytics/metrics_glossary). Diese Werte werden von Braze-Diensten generiert, sodass ein Kundenprofil sowohl SDK-erfasste als auch von Braze generierte Daten enthalten kann.

Berechnete Metriken umfassen kanalbasierte Metriken (aufgelistet im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/analytics/metrics_glossary)) und die folgenden Attribute.

| Attribut                                       | Beschreibung                                                         |
|------------------------------------------------|----------------------------------------------------------------------|
| App erstmals verwendet                         | Zeitpunkt                                                            |
| App zuletzt verwendet                          | Zeitpunkt                                                            |
| Gesamtanzahl der Sitzungen                     | Anzahl                                                               |
| Karte angeklickt                               | Anzahl                                                               |
| Zuletzt eine Nachricht erhalten                | Zeitpunkt                                                            |
| Zuletzt E-Mail-Campaign erhalten               | Zeitpunkt                                                            |
| Zuletzt Push-Campaign erhalten                 | Zeitpunkt                                                            |
| Anzahl der Feedback-Elemente                   | Anzahl                                                               |
| Anzahl der Sitzungen in den letzten Y Tagen    | Anzahl und Zeitpunkt                                                 |
| Nachricht von Campaign erhalten                | Boolean. Dieser Filter richtet sich an Nutzer:innen basierend darauf, ob sie eine frühere Campaign erhalten haben. |
| Nachricht von Campaign mit Tag erhalten        | Boolean. Dieser Filter richtet sich an Nutzer:innen basierend darauf, ob sie eine Campaign erhalten haben, die derzeit einen Tag hat. |
| Retarget-Campaign                              | Boolean. Dieser Filter richtet sich an Nutzer:innen basierend darauf, ob sie in der Vergangenheit eine bestimmte E-Mail, Push-Benachrichtigung oder In-App-Nachricht geöffnet oder angeklickt haben. |
| Deinstalliert                                  | Boolean und Zeitpunkt                                                |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Berechnete Metriken" }

Mindestintegration bedeutet, dass Sie nur die erforderlichen Daten erfassen, die unter [Mindestintegration](#minimum-integration) aufgeführt sind, und sich von den [optional standardmäßig erfassten Daten](#optional-data-collected-by-default) abmelden, indem Sie die [optionale SDK-Datenerfassung blockieren]({{site.baseurl}}/developer_guide/getting_started/sdk_overview).

{% alert important %}
Wenn Sie eine Mindestintegration wünschen und mParticle, Segment, Tealium oder GTM verwenden, beachten Sie Folgendes:
- **Mobile Plattformen**: Sie müssen den Code für diese Konfigurationen manuell aktualisieren. mParticle und Segment bieten keine Möglichkeit, dies über ihre Plattform zu tun.
- **Web**: Die Braze-Integration muss nativ erfolgen, um die Konfiguration der Mindestintegration zu ermöglichen. Tag-Manager bieten keine Möglichkeit, dies über ihre Plattform zu tun.
{% endalert %}

## Optionale Daten, die standardmäßig erfasst werden {#optional-data-collected-by-default}

Zusätzlich zu den Mindestintegrationsdaten werden die folgenden Attribute automatisch von Braze erfasst, wenn Sie die SDK-Integration initialisieren. Sie können die Erfassung dieser Attribute [deaktivieren]({{site.baseurl}}/developer_guide/getting_started/sdk_overview), um eine Mindestintegration zu ermöglichen.

| Attribut                | Plattform         | Beschreibung                                                                       | Warum es erfasst wird                                                                                                                                                   |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Browsername             | Web               | Name des Browsers                                                                  | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Browser zu senden. Es kann auch für browserbasierte Segmentierung verwendet werden.                     |
| Geräte-Locale           | Android, iOS, Web | Die Standard-Locale des Geräts                                                     | Dieses Attribut wird verwendet, um Nachrichten in die bevorzugte Sprache der Nutzer:innen zu übersetzen.                                                                |
| Letzte Geräte-Locale    | Android, iOS, Web | Die zuletzt eingestellte Standard-Locale des Geräts                                | Dieses Attribut stammt aus den Geräteeinstellungen der Nutzer:innen und wird verwendet, um Nachrichten in die bevorzugte Sprache der Nutzer:innen zu übersetzen. Es ist unabhängig vom Attribut `Most Recent Location`.                                                                                            |
| Gerätemodell            | Android, iOS      | Die spezifische Hardware des Geräts                                                | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden. Es kann auch innerhalb der Segmentierung verwendet werden.                           |
| Gerätemarke             | Android           | Die Marke des Geräts (z. B. Samsung)                                               | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden.                                                                                      |
| Mobilfunkanbieter des Geräts | Android, iOS | Der Mobilfunkanbieter                                                              | Dieses Attribut wird optional für das Nachrichten-Targeting verwendet.<br><br>**Hinweis:** Dieses Feld wurde ab iOS 16 als veraltet markiert und wird in einer zukünftigen iOS-Version standardmäßig `--` sein. |
| Sprache                 | Android, iOS, Web | Geräte- oder Browsersprache, abgeleitet aus der Geräte-Locale.                     | Dieses Attribut wird verwendet, um Nachrichten in die bevorzugte Sprache der Nutzer:innen zu übersetzen. Es basiert auf der Geräte-Locale.                              |
| Benachrichtigungseinstellungen | Android, iOS, Web | Ob für diese App Push-Benachrichtigungen aktiviert sind.                     | Dieses Attribut wird verwendet, um Push-Benachrichtigungen zu ermöglichen.                                                                                              |
| Auflösung               | Android, iOS, Web | Geräte- oder Browserauflösung                                                      | Wird optional für gerätebasiertes Nachrichten-Targeting verwendet. Das Format dieses Werts ist „`<width>`x`<height>`“.                                                  |
| Zeitzone                | Android, iOS, Web | Geräte- oder Browserzeitzone                                                       | Dieses Attribut wird verwendet, um Nachrichten zur passenden Zeit gemäß der Ortszeit jeder Nutzerin und jedes Nutzers zu senden.                             |
| User Agent              | Web               | [User Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Dieses Attribut wird verwendet, um Nachrichten nur an kompatible Geräte zu senden. Es kann auch innerhalb der Segmentierung verwendet werden.                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Optionale Daten, die standardmäßig erfasst werden" }

Weitere Informationen zum Tracking von Eigenschaften auf Geräteebene (wie Mobilfunkanbieter des Geräts, Zeitzone, Auflösung und andere) finden Sie in der plattformspezifischen Dokumentation: [Android]({{site.baseurl}}/developer_guide/storage?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage#cookies).

## Standardmäßig nicht erfasste Daten {#data-not-collected-by-default}

Standardmäßig werden die folgenden Attribute nicht erfasst. Jedes Attribut muss manuell integriert werden.

| Attribut                  | Plattform     | Beschreibung                                                                                                                                                                                                                                                                                                               | Warum es nicht erfasst wird                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device Ad Tracking Enabled | Android, iOS | Unter iOS:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>Unter Android:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Diese Eigenschaft erfordert zusätzliche Berechtigungen auf App-Ebene, die von der integrierenden Partei erteilt werden müssen.                                                                                                                                                                                      |
| Device IDFA                | iOS          | Geräte-Bezeichner für Werbetreibende                                                                                                                                                                                                                                                                                         | Dies erfordert das Ad Tracking Transparency Framework, das eine zusätzliche Datenschutzprüfung durch den App Store auslöst. Weitere Informationen finden Sie unter [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| Google Advertising ID      | Android      | Bezeichner für Werbung innerhalb von Google Play Apps                                                                                                                                                                                                                                                                        | Dies erfordert, dass die App die GAID abruft und an Braze übergibt. Weitere Informationen finden Sie unter [Optionale Google Advertising ID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id).                                         |
| Letzter bekannter Standort | Android, iOS | Dies ist der zuletzt bekannte GPS-Standort des Geräts der Nutzer:innen. Dieser wird beim Sitzungsstart aktualisiert und im Kundenprofil gespeichert. | Dies erfordert, dass Nutzer:innen Ihrer App eine Standortberechtigung erteilen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Standardmäßig nicht erfasste Daten" }

{% alert note %}
Das Braze SDK speichert keine IP-Adressen lokal.
{% endalert %}

## Personalisierte Integration {#personalized-integration}

Um das Beste aus Braze herauszuholen, implementieren unsere SDK-Integratoren häufig die Braze SDKs und protokollieren [angepasste Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#set-custom-attributes), [angepasste Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events#logging-custom-events) und [Kauf-Events]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#log-purchase-events), die für ihr Geschäft relevant sind – zusätzlich zu den automatisch erfassten Daten.

Eine personalisierte Integration ermöglicht eine maßgeschneiderte Kommunikation, die für die Erfahrung Ihrer Nutzer:innen relevant ist.

{% alert important %}
Braze blockiert Nutzerprofile („Dummy-Nutzer:innen“) mit mehr als 5.000.000 Sitzungen, mehr als 20.000 unterschiedlichen angepassten Event-Namen oder mehr als 20.000 unterschiedlichen Produktnamen bei Käufen und stoppt die Aufnahme aller eingehenden Daten für dieses Profil – sowohl über die SDKs als auch über die REST API. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_archival).
{% endalert %}