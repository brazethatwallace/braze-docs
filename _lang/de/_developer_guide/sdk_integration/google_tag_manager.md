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
## Über Google Tag Manager für das Internet {#google-tag-manager}

Mit dem Google Tag Manager (GTM) können Sie per Fernzugriff Tags auf Ihrer Website hinzufügen, entfernen und bearbeiten, ohne dass eine Freigabe des Produktionscodes oder technische Ressourcen erforderlich sind. Braze bietet die folgenden Templates für das Internet-SDK an:

| Tag-Typ | Anwendungsfall |
|--------|--------|
| Initialisierungs-Tag | Mit diesem Tag können Sie [das Braze Internet-SDK integrieren]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web), ohne den Code Ihrer Website ändern zu müssen. |
| Aktions-Tag | Mit diesem Tag können Sie [Content Cards erstellen]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [Nutzer:innen-Attribute festlegen]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) und [die Datenerfassung verwalten]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Über Google Tag Manager für das Internet" }

## Tag-Sequenzierung für Braze-Aktions-Tags {#tag-sequencing-for-braze-action-tags}

Angepasste Events und andere Braze-Aktions-Tags können fehlschlagen, wenn sie ausgelöst werden, bevor das **Braze Initialization**-Tag das Internet-SDK vollständig geladen hat. Öffnen Sie im Google Tag Manager das Aktions-Tag, gehen Sie zu **Advanced Settings** > **Tag Sequencing**, wählen Sie **A tag that fires before [this tag] is fired** und wählen Sie Ihr Braze-Initialisierungs-Tag aus.

Weitere Informationen finden Sie unter [Tag-Sequenzierung für angepasste Events überprüfen]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing).

## Käufe mit GTM protokollieren {#log-purchases-with-gtm}

Rufen Sie in Braze-Aktions-Tags und Custom-HTML-Tags `braze.logPurchase()` auf, um Umsätze zu erfassen. Der veraltete Namespace `appboy.logPurchase()` wird in aktuellen Internet-SDK-Integrationen nicht unterstützt.

## Angepasste Events mit GTM protokollieren {#logging-custom-events-with-gtm}

Sie können angepasste Events mit einem **Custom HTML**-Tag in GTM protokollieren. Dieser Ansatz nutzt den GTM-[Data Layer](https://developers.google.com/tag-platform/tag-manager/datalayer), um Event-Daten von Ihrer Website an ein GTM-Tag zu übergeben, das das Braze Internet-SDK aufruft.

### Schritt 1: Event in den Data Layer pushen {#step-1-push-the-event-to-the-data-layer}

Pushen Sie im Code Ihrer Website ein Event in den Data Layer, wo immer Sie das angepasste Event auslösen möchten. Um beispielsweise ein angepasstes Event zu protokollieren, wenn ein Button geklickt wird:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Schritt 2: Trigger in GTM erstellen {#step-2-create-a-trigger-in-gtm}

1. Gehen Sie in Ihrem GTM-Container zu **Triggers** und erstellen Sie einen neuen Trigger.
2. Setzen Sie den **Trigger Type** auf **Custom Event**.
3. Setzen Sie den **Event Name** auf denselben Wert, den Sie in den Data Layer gepusht haben (zum Beispiel `my_custom_event`).
4. Wählen Sie aus, wann der Trigger ausgelöst werden soll (zum Beispiel **All Custom Events**).

### Schritt 3: Custom-HTML-Tag erstellen {#step-3-create-a-custom-html-tag}

1. Gehen Sie in GTM zu **Tags** und erstellen Sie ein neues Tag.
2. Setzen Sie den **Tag Type** auf **Custom HTML**.
3. Fügen Sie im HTML-Feld Folgendes hinzu:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. Wählen Sie unter **Triggering** den Trigger aus, den Sie in Schritt 2 erstellt haben.
5. Speichern und veröffentlichen Sie Ihren Container.

Um Event-Eigenschaften einzuschließen, übergeben Sie diese als zweites Argument:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Googles EU-Richtlinie zur Nutzer:innen-Einwilligung {#googles-eu-user-consent-policy}

{% alert important %}
Google aktualisiert seine [EU-Richtlinie zur Nutzer:innen-Einwilligung](https://www.google.com/about/company/user-consent-policy/) als Reaktion auf Änderungen des [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), der seit dem 6. März 2024 in Kraft ist. Diese neue Änderung verpflichtet Werbetreibende, ihren Endnutzer:innen im EWR und in Großbritannien bestimmte Informationen offenzulegen und die erforderlichen Einwilligungen von ihnen einzuholen. Lesen Sie die folgende Dokumentation, um mehr zu erfahren.
{% endalert %}

Im Rahmen der EU-Richtlinie zur Nutzer:innen-Einwilligung von Google müssen die folgenden booleschen angepassten Attribute in Nutzerprofilen protokolliert werden:

- `$google_ad_user_data`
- `$google_ad_personalization`

Wenn Sie diese über die GTM-Integration festlegen, erfordern angepasste Attribute die Erstellung eines Custom-HTML-Tags. Das folgende Beispiel zeigt, wie Sie diese Werte als boolesche Datentypen (nicht als Strings) protokollieren:

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Weitere Informationen finden Sie unter [Audience Sync mit Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync).

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