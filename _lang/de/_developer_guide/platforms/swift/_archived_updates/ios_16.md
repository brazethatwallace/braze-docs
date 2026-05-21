---
nav_title: Anleitung zum Upgraden auf iOS 16
article_title: Upgrade-Leitfaden für iOS 16
page_order: 7
platform:
  - iOS
description: "Dieser Referenzartikel behandelt iOS 16, Upgrades, SDK-Updates und mehr."
hidden: true
noindex: true
---

# Upgrade-Leitfaden für das iOS 16-SDK {#ios-16-sdk-upgrade-guide}

> Dieser Leitfaden beschreibt die relevanten Änderungen, die mit iOS 16 (2022) eingeführt wurden, und die Auswirkungen auf Ihre Braze iOS SDK-Integration. Eine vollständige Anleitung für die Migration finden Sie in den [iOS 16 Versionshinweisen](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes).

## Änderungen in iOS 16 {#changes-in-ios-16}

### Safari Web-Push {#safari-web-push}

Apple hat zwei Änderungen an seiner Web-Push-Funktionalität angekündigt.

#### Desktop Web-Push (MacOS) {#macos-push}

Zuvor unterstützte Apple Push-Benachrichtigungen auf macOS (Desktop) über die eigenen Safari-Push-APIs.

Seit macOS Ventura (veröffentlicht am 24\. Oktober 2022) [unterstützt Safari zusätzlich](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos) zu Safari-Push auch Web-Push-APIs. Dies ist ein bestehender browserübergreifender API-Standard, der in anderen gängigen Browsern verwendet wird.

Wenn Sie bereits Web-Push für Safari über Braze senden, ist keine Änderung erforderlich.

#### Mobiles Web-Push (iOS und iPadOS) {#ios-push}

Zuvor unterstützte Safari auf iPhone und iPad den Empfang von Push-Benachrichtigungen nicht.

Ab 2023 wird Apple Web-Push auf iPhones und iPads über Safari unterstützen.

Braze wird dieses neue iOS- und iPadOS-Web-Push unterstützen, ohne dass zusätzliche Änderungen oder Upgrades erforderlich sind.

## Vorbereitungen für iOS 16 {#next-steps}

Sie müssen Ihr Braze iOS SDK nicht für iOS 16 upgraden, aber es gibt zwei weitere spannende Updates:

1. Braze hat ein [neues Swift SDK](https://github.com/braze-inc/braze-swift-sdk) veröffentlicht. Es bietet eine verbesserte Performance, neue Features und viele Verbesserungen.
2. Unser Braze Swift SDK unterstützt ein neues [„No-Code“-Push-Primer-Feature]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/)!