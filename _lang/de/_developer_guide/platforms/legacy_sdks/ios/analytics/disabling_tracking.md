---
nav_title: iOS SDK-Tracking deaktivieren
article_title: SDK-Tracking für iOS deaktivieren
platform: iOS
page_order: 8
description: "Dieser Artikel zeigt, wie Sie die Datenerfassung für Ihre iOS-Anwendung deaktivieren können."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Datenerfassung für iOS deaktivieren {#disable-data-collection-for-ios}

Um den Datenschutzbestimmungen zu entsprechen, kann die Tracking-Aktivität im iOS SDK mit der Methode [`disableSDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733) vollständig gestoppt werden. Diese Methode führt dazu, dass alle Netzwerkverbindungen abgebrochen werden und das Braze SDK keine Daten an unsere Server weitergibt. Wenn Sie die Datenerfassung später wieder aufnehmen möchten, können Sie die Methode [`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b) verwenden, um die Datenerfassung fortzusetzen.

Außerdem können Sie die Methode [`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3) verwenden, um alle auf dem Gerät gespeicherten clientseitigen Daten vollständig zu löschen.

Sofern ein:e Nutzer:in nicht alle Apps eines Anbieters auf einem bestimmten Gerät deinstalliert, führt die nächste Ausführung von Braze SDK und App nach dem Aufruf von `wipeDataAndDisableForAppRun()` dazu, dass unser Server diese:n Nutzer:in über den Identifier for Vendors (IDFV) erneut identifiziert. Um alle Nutzerdaten vollständig zu löschen, sollten Sie einen Aufruf von `wipeDataAndDisableForAppRun` mit einer Anfrage zum Löschen von Daten auf dem Server über die Braze [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) kombinieren.

## iOS SDK v5.7.0+ {#ios-sdk-v570}
Bei Geräten, die iOS SDK v5.7.0 und höher verwenden, führt der Aufruf von [`wipeData`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) bei [deaktivierter IDFV-Erfassung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfv-collection---swift) nicht dazu, dass unser Server diese Nutzer:innen über ihren Gerätebezeichner (IDFV) erneut identifiziert.