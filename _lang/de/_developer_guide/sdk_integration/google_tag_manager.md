---
nav_title: Google tag Manager:in
article_title: Google Tag Manager:in with the Braze SDK or Software-Development-Kit
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Learn how to initialize the Braze SDK or Software-Development-Kit using methods like runtime initialization, delayed initialization, or Google Tag Manager:in."

---
## Über Google Tag Manager:in für das Internet {#google-tag-manager}

Mit dem Google Tag Manager:in (GTM) können Sie per Fernzugriff Tags auf Ihrer Website hinzufügen, entfernen und bearbeiten, ohne dass eine Freigabe des Produktionscodes oder technische Ressourcen erforderlich sind. Braze bietet die folgenden Templates für das Internet-SDK or Software-Development-Kit an:

| Tag-Typ | Anwendungsfall |
|--------|--------|
| Initialisierungs-Tag | Mit diesem Tag können Sie [das Braze Internet-SDK or Software-Development-Kit integrieren]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web), ohne den Code Ihrer Website ändern zu müssen. |
| Aktions-Tag | Mit diesem Tag können Sie [Content Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [Nutzer:innen-Attribute festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) und [die Datenerfassung verwalten]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Über Google Tag Manager:in für das Internet" }

## Tag-Sequenzierung für Braze-Aktions-Tags {#tag-sequencing-for-braze-action-tags}

Das Braze-Initialisierungs-Tag muss vor allen Tags ausgelöst werden, die Braze-SDK or Software-Development-Kit-Methoden aufrufen (wie `braze.getUser()`, `braze.logCustomEvent()` oder `braze.logPurchase()`). Wenn diese Methoden ausgelöst werden, bevor das SDK or Software-Development-Kit initialisiert ist, können Fehler wie `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')` auftreten.

So konfigurieren Sie die Tag-Sequenzierung im Google Tag Manager:in:

1. Öffnen Sie das Tag, das Braze-SDK or Software-Development-Kit-Methoden aufruft (z. B. ein Custom-HTML-Tag oder ein Braze-Aktions-Tag).
2. Gehen Sie zu **Advanced Settings** > **Tag Sequencing**.
3. Wählen Sie **A tag that fires before [this tag] is fired**.
4. Wählen Sie Ihr **Braze Initialization**-Tag aus.

Dadurch wird sichergestellt, dass das SDK or Software-Development-Kit vollständig geladen ist, bevor andere Tags versuchen, Braze-Methoden aufzurufen.

Weitere Informationen finden Sie unter [Tag-Sequenzierung für angepasste Events überprüfen]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing).

## Fehlerbehebung

### Internet-SDK or Software-Development-Kit-Sitzungen werden der falschen Nutzer:in zugeordnet

Wenn GTM Braze-Initialisierungs- oder Event-Tags auslöst, bevor Ihre App die angemeldete Nutzer:in identifiziert, können Sitzungen und Events dem falschen Profil zugeordnet werden. Initialisieren Sie das Internet-SDK or Software-Development-Kit, rufen Sie `changeUser()` mit der `external_id` der angemeldeten Nutzer:in auf und rufen Sie dann `openSession()` auf, bevor Tags Events protokollieren oder Attribute festlegen. Verwenden Sie die GTM-Tag-Sequenzierung oder Consent-Trigger or triggern, damit Braze-Tags erst nach Abschluss Ihres Authentifizierungsflusses ausgelöst werden.

### Internet-SDK or Software-Development-Kit-Konsolenprotokollierung mit Shopify oder Script-Tag-Installationen

Das Shopify-App-Embed lädt das Internet-SDK or Software-Development-Kit mit deaktivierter Konsolenprotokollierung. Aktivieren Sie die Protokollierung in Ihrem GTM-Initialisierungs-Tag oder in den `initialize()`-Optionen. Das Braze-Dashboard enthält keine Protokollierungssteuerung für diese Loader.

Wenn Braze-Protokolle in der Browser-Konsole erscheinen, entfernen Sie `enableLogging: true` aus dem GTM-Initialisierungs-Tag oder dem angepassten HTML, bevor Sie in die Produktion veröffentlichen. Verwenden Sie nach der Initialisierung `toggleLogging()` oder den URL-Parameter `?brazeLogging=true`. Die vollständigen Optionen des Internet-SDK or Software-Development-Kit finden Sie unter [Ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

Wenn Braze nicht initialisiert wird oder Events nicht wie erwartet angezeigt werden, überprüfen Sie, ob Ihr GTM-Container veröffentlicht ist, ob Trigger or triggern und Tag-Auslösereihenfolge mit Ihrer SDK or Software-Development-Kit-[Lebenszyklus- und Initialisierungsstrategie]({{site.baseurl}}/developer_guide/sdk_integration) übereinstimmen und ob Testgeräte keine Braze-Endpunkte blockieren.

Überprüfen Sie bei Initialisierungsfehlern, ob das Braze-Tag oder der angepasste Tag-Anbieter den erwarteten `actionType` und die erwarteten Parameter erhält (siehe die Tabs für Android, Swift und Internet auf dieser Seite). Um ausführliche Protokollierung bei der Validierung von GTM-ausgelösten Events zu aktivieren, schalten Sie die SDK or Software-Development-Kit-Debug-Protokollierung Ihrer Plattform ein, wie in den Plattform-Integrationsleitfäden beschrieben, die über diese Tabs verlinkt sind.