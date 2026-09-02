---
nav_title: Erweiterte Einstellungen
article_title: Erweiterte Push-Einstellungen
platform: iOS
page_order: 5
description: "Dieser Referenzartikel behandelt erweiterte Einstellungen für iOS-Push-Benachrichtigungen wie Benachrichtigungsoptionen, Töne, Ablauf und mehr."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Erweiterte Einstellungen {#advanced-settings}

Wenn Sie eine Push-Campaign erstellen, wählen Sie im Schritt „Verfassen“ die Option **Settings**, um die verfügbaren erweiterten Einstellungen anzuzeigen.

![Erweiterte Einstellungen für iOS-Push-Campaigns im Braze-Dashboard.]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Extrahieren von Daten aus Push-Schlüssel-Wert-Paaren {#extracting-data-from-push-key-value-pairs}

Braze ermöglicht es Ihnen, benutzerdefinierte String-Schlüssel-Wert-Paare, bekannt als `extras`, zusammen mit einer Push-Benachrichtigung an Ihre Anwendung zu senden. Extras können über das Dashboard oder die API definiert werden und stehen dann als Schlüssel-Wert-Paare im `notification`-Wörterbuch zur Verfügung, das an Ihre Push-Delegate-Implementierungen weitergegeben wird.

## Benachrichtigungsoptionen {#alert-options}

Aktivieren Sie das Kontrollkästchen **Alert Options**, um eine Dropdown-Liste mit Schlüsselwerten anzuzeigen, mit denen Sie die Anzeige der Benachrichtigung auf den Geräten anpassen können.

## Hinzufügen des Content-Available-Flags {#adding-content-available-flag}

Aktivieren Sie das Kontrollkästchen **Add Content-Available Flag**, um die Geräte anzuweisen, neue Inhalte im Hintergrund herunterzuladen. In der Regel können Sie diese Option aktivieren, wenn Sie [stille Benachrichtigungen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications) versenden möchten.

## Hinzufügen des Mutable-Content-Flags {#adding-mutable-content-flag}

Aktivieren Sie das Kontrollkästchen **Add Mutable-Content Flag**, um die erweiterte Empfängeranpassung auf Geräten mit iOS 10+ zu aktivieren. Dieses Flag wird automatisch gesendet, wenn Sie eine [Rich-Benachrichtigung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/rich_notifications) verfassen, unabhängig vom Wert dieses Kontrollkästchens.

## App-Badge-Zähler Update or aktualisieren or aktualisieren {#update-app-badge-count}

Geben Sie die Zahl ein, auf die Sie Ihren Badge-Zähler Update or aktualisieren or aktualisieren möchten, oder verwenden Sie die Liquid-Syntax, um Ihre angepassten Bedingungen festzulegen. Sie können Ihren Badge-Zähler auch manuell über die Eigenschaft `applicationIconBadgeNumber` Ihrer Anwendung oder die Payload der Push-Benachrichtigung Update or aktualisieren or aktualisieren. Weitere Informationen finden Sie in unserem Artikel über [Badge-Zähler]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/badges).

## Töne {#sounds}

Hier können Sie einen Pfad zu einer Tondatei in Ihrem App-Bundle eingeben, um einen Sound festzulegen, der beim Empfang der Push-Nachricht abgespielt wird. Wenn die angegebene Tondatei nicht vorhanden ist oder das Schlüsselwort „default“ eingegeben wird, verwendet Braze den Standard-Gerätealarmton. Weitere Informationen zur Anpassung finden Sie in unserem Artikel über [angepasste Sounds]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/custom_sounds).

## Collapse-ID {#collapse-id}

Geben Sie eine Collapse-ID an, um ähnliche Benachrichtigungen zusammenzufassen. Wenn Sie mehrere Benachrichtigungen mit derselben Collapse-ID senden, zeigt das Gerät nur die zuletzt empfangene Benachrichtigung an. Lesen Sie die Dokumentation von Apple über [zusammengefasste Benachrichtigungen](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Ablauf {#expiry}

Wenn Sie das Kontrollkästchen **Expiry** aktivieren, können Sie eine Ablaufzeit für Ihre Nachricht festlegen. Sollte das Gerät einer Nutzerin oder eines Nutzers die Verbindung verlieren, wird Braze weiterhin versuchen, die Nachricht bis zur angegebenen Zeit zu senden. Wenn dieser Wert nicht festgelegt ist, verwendet die Plattform standardmäßig einen Ablauf von 30 Tagen. Beachten Sie, dass Push-Benachrichtigungen, die vor der Zustellung ablaufen, nicht als fehlgeschlagen gelten und nicht als Bounce registriert werden.