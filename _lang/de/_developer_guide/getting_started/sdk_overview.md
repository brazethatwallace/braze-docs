---
nav_title: SDK or Software-Development-Kit-Übersicht
article_title: SDK or Software-Development-Kit-Übersicht für Entwickler:innen
description: "Dieser Onboarding-Referenzartikel bietet eine technische Übersicht für Entwickler:innen des Braze SDK or Software-Development-Kit. Er behandelt die Standard-Analytics, die vom SDK or Software-Development-Kit erfasst werden."
page_order: 0
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"} SDK-Übersicht für Entwickler:innen {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdevelopersdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordersdk-overview-for-developers}

> Bevor Sie mit der Integration der Braze SDKs beginnen, werden Sie sich vielleicht fragen, was genau Sie da eigentlich entwickeln und integrieren. Vielleicht sind Sie neugierig, wie Sie das SDK or Software-Development-Kit weiter an Ihre Bedürfnisse anpassen können. Dieser Artikel hilft Ihnen, alle Ihre Fragen zum SDK or Software-Development-Kit zu beantworten.

Sind Sie ein Marketer, der einen grundlegenden Überblick über das SDK or Software-Development-Kit benötigt? Sehen Sie sich stattdessen unsere [Übersicht für Marketer]({{site.baseurl}}/user_guide/get_started/sdk_overview) an.

Kurz gesagt, das Braze SDK or Software-Development-Kit:
* Sammelt und synchronisiert Nutzerdaten in einem konsolidierten Kundenprofil or Nutzerprofil
* Sammelt automatisch Sitzungsdaten, Geräteinformationen und Push-Token / Textbaustein
* Erfasst Marketingdaten und angepasste Daten speziell für Ihr Unternehmen
* Unterstützt Push-Benachrichtigungen, In-App Messages und Content-Card-Nachrichtenkanäle

Sehen Sie sich das folgende Video an, um eine kurze Einführung in die Grundlagen der Braze SDK or Software-Development-Kit-Integration und die Kernfunktionalität zu erhalten.

{% multi_lang_include video.html id="il152jayp0" source="wistia" %}

## App-Performance

Braze sollte keine negativen Auswirkungen auf die Performance Ihrer App haben.

Die Braze SDKs haben einen sehr geringen Ressourcenverbrauch. Wir passen automatisch die Rate an, mit der Nutzerdaten übertragen werden, abhängig von der Netzwerkqualität, und ermöglichen zusätzlich eine manuelle Netzwerksteuerung. Wir fassen API-Anfragen aus dem SDK or Software-Development-Kit automatisch in Batches zusammen, um sicherzustellen, dass Daten schnell protokolliert werden und gleichzeitig eine maximale Netzwerkeffizienz gewährleistet ist. Zudem ist die Datenmenge, die bei jedem API-Aufruf vom Client an Braze gesendet wird, äußerst gering.

## SDK or Software-Development-Kit-Kompatibilität {#sdk-compatibility}

Das Braze SDK or Software-Development-Kit ist so konzipiert, dass es sich sehr gut verhält und nicht mit anderen SDKs in Ihrer App interferiert. Wenn Sie Probleme feststellen, die möglicherweise auf eine Inkompatibilität mit einem anderen SDK or Software-Development-Kit zurückzuführen sind, wenden Sie sich an den Braze-Support.

## Standard-Analytics und Sitzungsbehandlung {#default-analytics-and-session-handling}

Bestimmte Nutzerdaten werden automatisch von unserem SDK or Software-Development-Kit erfasst – zum Beispiel „Erste App-Nutzung“, „Letzte App-Nutzung“, „Gesamtanzahl der Sitzungen“, „Geräte-Betriebssystem“ usw. Wenn Sie unsere Integrationsleitfäden befolgen, um unsere SDKs zu implementieren, können Sie von dieser [standardmäßigen Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection) profitieren. Ein Blick auf diese Liste kann Ihnen helfen, die gleichen Informationen über Nutzer:innen nicht mehrfach zu speichern. Mit Ausnahme von Sitzungsstart und Sitzungsende zählen alle anderen automatisch erfassten Daten nicht zu Ihrer Datenpunkt-Nutzung.

{% alert note %}
Alle unsere Features sind konfigurierbar, aber es empfiehlt sich, das standardmäßige Datenerfassungsmodell vollständig zu implementieren.

<br>Falls es für Ihren Anwendungsfall erforderlich ist, können Sie die [Erfassung bestimmter Daten nach Abschluss der Integration einschränken](#blocking-data-collection).
{% endalert %}

## Daten-Upload und -Download {#data-upload-and-download}

Das Braze SDK or Software-Development-Kit speichert Daten (Sitzungen, angepasste Events usw.) zwischen und lädt sie regelmäßig hoch. Erst nachdem die Daten hochgeladen wurden, werden die Werte im Dashboard aktualisiert. Das Upload-Intervall berücksichtigt den Zustand des Geräts und wird durch die Qualität der Netzwerkverbindung bestimmt:

|Qualität der Netzwerkverbindung |    Intervall für Datenübertragung|
|---|---|
|Sehr gut    |10 Sekunden|
|Gut    |30 Sekunden|
|Schlecht    |60 Sekunden|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Daten-Upload und -Download" }

Wenn keine Netzwerkverbindung besteht, werden die Daten lokal auf dem Gerät zwischengespeichert, bis die Netzwerkverbindung wiederhergestellt ist. Sobald die Verbindung wiederhergestellt ist, werden die Daten an Braze hochgeladen.

Braze sendet zu Beginn einer Sitzung Daten an das SDK or Software-Development-Kit, basierend darauf, in welche Segmente die Nutzer:innen zum Zeitpunkt der Sitzung fallen. Die neuen In-App Messages werden während der Sitzung nicht aktualisiert. Nutzerdaten, die während der Sitzung erfasst werden, werden jedoch kontinuierlich verarbeitet, sobald sie vom Client gesendet werden. Zum Beispiel erhalten inaktive Nutzer:innen (die die App seit mehr als 7 Tagen nicht mehr genutzt haben) bei ihrer ersten Sitzung nach der Rückkehr in die App weiterhin Inhalte, die auf inaktive Nutzer:innen ausgerichtet sind.

## Datenerfassung blockieren {#blocking-data-collection}

Es ist möglich (jedoch nicht empfohlen), die automatische Erfassung bestimmter Daten aus Ihrer SDK or Software-Development-Kit-Integration zu blockieren oder Prozesse, die dies tun, auf eine Zulassungsliste zu setzen.

Das Blockieren der Datenerfassung wird nicht empfohlen, da das Entfernen analytischer Daten die Fähigkeit Ihrer Plattform zur Personalisierung und zum Targeting verringert. Zum Beispiel:

- Wenn Sie die Standortintegration bei einem der SDKs nicht vollständig vornehmen, können Sie Ihr Messaging nicht basierend auf Sprache oder Standort personalisieren.
- Wenn Sie die Zeitzonenintegration nicht vornehmen, können Sie möglicherweise keine Nachrichten innerhalb der Zeitzone der Nutzer:innen senden.
- Wenn Sie bestimmte visuelle Geräteinformationen nicht integrieren, werden Nachrichteninhalte möglicherweise nicht für das jeweilige Gerät optimiert.

Wir empfehlen dringend, die SDKs vollständig zu integrieren, um die Funktionen unseres Produkts voll auszuschöpfen.

{% tabs %}
{% tab Web SDK or Software-Development-Kit %}

Sie können bestimmte Teile des SDK or Software-Development-Kit einfach nicht integrieren oder [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) für eine:n Nutzer:in verwenden. Diese Methode synchronisiert Daten, die vor dem Aufruf von `disableSDK()` protokolliert wurden, und bewirkt, dass alle nachfolgenden Aufrufe des Braze Web SDK or Software-Development-Kit für diese Seite und zukünftige Seitenladevorgänge ignoriert werden. Wenn Sie die Datenerfassung zu einem späteren Zeitpunkt wieder aufnehmen möchten, können Sie die Methode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) verwenden, um die Datenerfassung fortzusetzen. Weitere Informationen finden Sie in unserem Artikel [Web-Tracking deaktivieren]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=web).

{% endtab %}
{% tab Android SDK or Software-Development-Kit %}

Sie können [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) verwenden, um das SDK or Software-Development-Kit so zu konfigurieren, dass nur eine Teilmenge der Geräteobjekt-Schlüssel oder -Werte gemäß einer festgelegten Zulassungsliste gesendet wird. Dies muss über [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder) aktiviert werden.

{% alert important %}
Eine leere Zulassungsliste führt dazu, dass **keine** Gerätedaten an Braze gesendet werden.
{% endalert %}

{% endtab %}
{% tab Swift SDK or Software-Development-Kit %}

Sie können eine Gruppe zulässiger Felder [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) in Ihrer `Braze.Configuration` zuweisen, um eine Zulassungsliste für Gerätefelder festzulegen, die vom SDK or Software-Development-Kit erfasst werden. Die vollständige Liste der Felder ist in [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty) definiert. Um die Erfassung aller Gerätefelder zu deaktivieren, setzen Sie den Wert dieser Eigenschaft auf ein leeres Set (`[]`).

{% alert important %}
Standardmäßig werden alle Felder vom Braze Swift SDK or Software-Development-Kit erfasst. Das Entfernen einiger Geräteeigenschaften kann SDK or Software-Development-Kit-Features deaktivieren.
{% endalert %}

Weitere Details zur Verwendung finden Sie unter [Speicher]({{site.baseurl}}/developer_guide/storage?tab=swift) in der Swift-SDK or Software-Development-Kit-Dokumentation.

{% endtab %}
{% endtabs %}

## Welche SDK or Software-Development-Kit-Version verwende ich? {#what-version-of-the-sdk-am-i-on}

Sie können über das Dashboard die SDK or Software-Development-Kit-Version einer bestimmten App einsehen, indem Sie **Einstellungen > App-Einstellungen** aufrufen. Die **Live-SDK or Software-Development-Kit-Version** zeigt die höchste Braze-SDK or Software-Development-Kit-Version an, die von Ihrer aktuellsten Live-Anwendung bei mindestens 5 % Ihrer Nutzer:innen verwendet wird.

![Eine App namens „Swifty“ in einem Workspace. Die Live-SDK-Version ist 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"}

{% alert tip %}
Wenn Sie eine iOS-App haben, können Sie bestätigen, dass Sie das [Swift SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=swift) anstelle des veralteten [Objective-C iOS SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) verwenden, wenn Ihre **Live-SDK or Software-Development-Kit-Version** 5.0.0 oder höher ist – das war die erste veröffentlichte Version des Swift SDK or Software-Development-Kit.
{% endalert %}