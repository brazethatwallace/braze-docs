---
nav_title: Smart-TV-Unterstützung
article_title: Smart-TV-Unterstützung für das Braze Web SDK or Software-Development-Kit
platform: Web
page_order: 30
description: "Dieser Artikel beschreibt, wie Sie das Braze Web SDK or Software-Development-Kit für die Integration mit Smart-TVs (Samsung und LG) verwenden."

---

# Smart-TV-Unterstützung {#smart-tv-support}

> Mit dem Braze Web SDK or Software-Development-Kit können Sie Analytics erfassen und Smart-TV-Nutzer:innen reichhaltige In-App-Nachrichten und Content-Card-Nachrichten anzeigen, einschließlich [Samsung Tizen-TVs](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) und [LG-TVs (webOS)](https://webostv.developer.lge.com/discover). Dieser Artikel beschreibt, wie Sie das Braze Web SDK or Software-Development-Kit für die Integration mit Smart-TVs verwenden.

{% alert tip %}
Eine vollständige technische Referenz finden Sie in unserer [JavaScript-Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) oder in unseren [Beispiel-Apps](https://github.com/Appboy/smart-tv-sample-apps), um das Web SDK or Software-Development-Kit auf einem Fernseher in Aktion zu sehen.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Konfigurieren des Braze Web SDK or Software-Development-Kit {#configuring-the-web-braze-sdk}

Für die Integration mit Smart-TVs sind zwei Änderungen erforderlich:

1. Achten Sie beim Herunterladen oder Importieren des Web SDK or Software-Development-Kit darauf, dass Sie das „core“-Bundle verwenden (verfügbar unter `https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js`, wobei `x.y` die gewünschte Version ist). Wir empfehlen die Verwendung der CDN-Version unseres Web SDK or Software-Development-Kit, da die NPM-Version in nativen ES-Modulen geschrieben ist, während die CDN-Version in ES5 transpiliert wird. Wenn Sie die [NPM-Version](https://www.npmjs.com/package/@braze/web-sdk) bevorzugen, stellen Sie sicher, dass Sie einen Bundler wie Webpack verwenden, der ungenutzten Code entfernt, und dass der Code in ES5 transpiliert wird.
2. Bei der Initialisierung des Web SDK or Software-Development-Kit müssen Sie die Initialisierungsoptionen `disablePushTokenMaintenance` und `manageServiceWorkerExternally` auf `true` setzen.

## Analytics {#analytics}

Alle Analytics-Methoden des Web SDK or Software-Development-Kit können auch bei Smart-TVs verwendet werden. Eine vollständige Anleitung zum Tracking von angepassten Events, angepassten Attributen und mehr finden Sie unter [Analytics]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web).

## In-App-Nachrichten und Content Cards {#in-app-messages-and-content-cards}

Das Braze Web SDK or Software-Development-Kit unterstützt sowohl [In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=web) als auch [Content Cards]({{site.baseurl}}/developer_guide/content_cards?sdktab=web) auf Smart-TVs. Beachten Sie, dass Sie das [„Core“-Web-SDK or Software-Development-Kit](https://www.npmjs.com/package/@braze/web-sdk) verwenden müssen, da das Rendern von In-App-Nachrichten und Content Cards über unsere Standard-UI-Anzeige nicht unterstützt wird und stattdessen von Ihrer App angepasst werden sollte, um sich in das Erlebnis Ihrer TV-App einzufügen.

Weitere Informationen darüber, wie Ihre Smart-TV-App In-App-Nachrichten empfangen und anzeigen kann, finden Sie unter [Trigger or triggern or triggern von Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web).