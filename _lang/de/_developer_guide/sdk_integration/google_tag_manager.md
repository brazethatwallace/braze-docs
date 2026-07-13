---
nav_title: Google Tag Manager
article_title: Google Tag Manager mit dem Braze SDK
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Erfahren Sie, wie Sie das Braze SDK mit Methoden wie Laufzeitinitialisierung, verzögerter Initialisierung oder Google Tag Manager initialisieren."

---

# Google Tag Manager mit dem Braze SDK {#google-tag-manager-with-the-braze-sdk}

> Erfahren Sie, wie Sie [Google Tag Manager (GTM)](https://developers.google.com/tag-platform/tag-manager) mit dem Braze SDK verwenden können, um das Braze-Event-Tracking und Updates von Nutzer:innen-Attributen per Fernzugriff zu steuern, ohne dass Codeänderungen oder neue App-Versionen erforderlich sind.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/google_tag_manager.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## Fehlerbehebung {#troubleshooting}

Wenn Braze nicht initialisiert wird oder Ereignisse nicht wie erwartet angezeigt werden, überprüfen Sie, ob Ihr GTM-Container veröffentlicht ist, ob Trigger und die Reihenfolge der Tag-Auslösung mit dem [Lebenszyklus und der Initialisierungsstrategie]({{site.baseurl}}/developer_guide/sdk_integration) Ihres SDK übereinstimmen und ob Testgeräte keine Braze-Endpunkte blockieren.

Bei Initialisierungsfehlern überprüfen Sie, ob das Braze-Tag oder der angepasste Tag-Anbieter den erwarteten `actionType` und die erwarteten Parameter erhält (siehe die Tabs für Android, Swift und Internet auf dieser Seite). Um beim Validieren von GTM-ausgelösten Ereignissen eine ausführliche Protokollierung zu erhalten, aktivieren Sie das SDK-Debug-Logging Ihrer Plattform, wie in den Integrationsleitfäden beschrieben, die in diesen Tabs verlinkt sind.