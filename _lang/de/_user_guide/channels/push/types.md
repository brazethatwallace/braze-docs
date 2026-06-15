---
nav_title: "Nachrichtentypen"
article_title: Push-Nachrichtentypen
page_order: 3
page_type: reference
description: "Dieser Referenzartikel listet die verschiedenen Arten von Push-Benachrichtigungen auf, die Sie mit Braze senden können."
channel: push
---

# Push-Nachrichtentypen {#push-message-types}

> Es gibt viele Arten von Push-Benachrichtigungen, die Sie nutzen können, um mit Ihren Kund:innen zu interagieren. Die meisten dieser Einstellungen können Sie in Ihren Push-Campaigns konfigurieren, einige erfordern jedoch Backend-Konfigurationen, wie in den Beschreibungen angegeben.

## Standard-Push

Die universelle Push-Nachricht. Diese erscheinen auf dem Gerät Ihrer Nutzer:innen mit einem Benachrichtigungston und einer Nachricht, die eingeblendet wird oder in einer Benachrichtigungsleiste bzw. einem Stack erscheint.

**Unterstützt auf:** Web, Android, iOS

Weitere Informationen finden Sie unter [Push-Nachricht erstellen]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/).

## Web-Push

Diese Push-Nachrichten erscheinen in Web-Apps oder Browsern. Sie erfordern eine Berechtigung, um die Kund:innen zu erreichen. Web-Push funktioniert nicht, wenn Nutzer:innen einen versteckten Browser verwenden.

**Unterstützt auf:** Web

Weitere Informationen finden Sie unter [Web-Push-Benachrichtigungen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web/).

## Push-Primer-Campaigns

In-App-Nachricht-Campaigns, die dazu dienen, ein explizites Push-Opt-in- oder Opt-out-Signal von Nutzer:innen zu erhalten. Durch den Primer können Sie vermeiden, Benachrichtigungen an Nutzer:innen zu senden, die Push wahrscheinlich über die Geräteeinstellungen deaktivieren würden. Für iOS sind Push-Campaigns relevant, da Vordergrund-Push-Benachrichtigungen (z. B. Benachrichtigungen, die das Gerät aufwecken) erst aktiviert werden, wenn Nutzer:innen explizit dem nativen iOS-Push-Prompt zustimmen.

**Unterstützt auf:** Web, Android, iOS

Weitere Informationen finden Sie unter [Push-Primer-In-App-Nachrichten]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/).

## Push Stories

Push Stories sind immersive Nachrichten, die Ihre Nutzer:innen in Form eines Karussells durch eine visuelle Journey führen. Diese sind nur für Mobilgeräte verfügbar.

**Unterstützt auf:** iOS, Android

Weitere Informationen finden Sie unter [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories/).

## Push mit Aktions-Buttons {#push-with-action-buttons}

Push mit Aktions-Buttons sind Nachrichten, mit denen Sie Ihren Nutzer:innen Optionen anbieten und mehrere Handlungsaufforderungen bereitstellen können.

**Unterstützt auf:** Web, Android, iOS

Weitere Informationen finden Sie unter [Push-Aktions-Buttons]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/).

## Rich-Push-Benachrichtigungen {#rich-push-notifications}

Rich-Push-Benachrichtigungen sind Benachrichtigungen mit immersiven Bildern und kreativen Inhalten, die über ein Symbol und einen Handlungsaufforderungstext hinausgehen können.

**Unterstützt auf:** iOS, Android

Weitere Informationen finden Sie unter [Rich-Benachrichtigungen für iOS erstellen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications/) oder [Rich-Benachrichtigungen für Android erstellen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications/).

## Vorläufige Push-Benachrichtigungen für iOS {#provisional-push-notifications-for-ios}

Von Apple in iOS 12 eingeführt, erfolgt die vorläufige Autorisierung automatisch bei der Installation von iOS-Apps, sodass Marken stille Benachrichtigungen senden können, ohne den Nutzer:innen einen Push-Prompt anzuzeigen. Wenn die stille Push-Benachrichtigung gesendet und im Benachrichtigungsfach des Geräts angezeigt wird, erhalten Nutzer:innen die Möglichkeit, Push-Benachrichtigungen zuzulassen oder abzulehnen.

**Unterstützt auf:** iOS

Weitere Informationen finden Sie unter [iOS-Benachrichtigungsoptionen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options/#provisional-push).

## HTML-Push-Benachrichtigungen {#html-push-notifications}

HTML-Push-Benachrichtigungen sind Push-Nachrichten, die in HTML fest codiert sind und nicht die vorgefertigten Push-Templates verwenden, die Braze bereitstellt. Die Möglichkeit, HTML-Push-Benachrichtigungen zu erstellen, gibt Ihrem Unternehmen volle kreative Freiheit und ein einheitliches Branding bei der Gestaltung dieser Push-Nachrichten.

**Unterstützt auf:** Android

## Benachrichtigungs-IDs und Kanal-IDs {#notification-ids-and-channel-ids}

Benachrichtigungs-IDs und Kanal-IDs ermöglichen es Ihnen, Push-Benachrichtigungen zu ersetzen oder zu aktualisieren, die bereits von Nutzer:innen empfangen, aber noch nicht geöffnet wurden.

**Unterstützt auf:** iOS, Android

Weitere Informationen finden Sie unter [Benachrichtigungskanäle]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels/) und [Erweiterte Push-Campaign-Einstellungen]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/advanced_campaign_settings/).

## Hintergrund- oder stille Push-Benachrichtigungen {#background-push-notifications}

Push-Benachrichtigungen, die nicht auf dem Gerät angezeigt werden. Sie werden in der Regel verwendet, um Informationspakete an die App für Hintergrundprozesse und Uninstall-Tracking zu senden. Ein hintergrundfähiges Push-Token ist erforderlich, damit eine Hintergrund- oder stille Push-Benachrichtigung gesendet werden kann.

**Unterstützt auf:** Web, Android, iOS

Weitere Informationen finden Sie unter [Stille Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/silent/).

## Wearable-Push-Benachrichtigungen {#wearable-push-notifications}

Diese Push-Benachrichtigungen ermöglichen es Marken, Nachrichten direkt an Wearable-Geräte wie die Apple Watch zu senden.

**Unterstützt auf:** iOS