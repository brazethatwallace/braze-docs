---
nav_title: Google Tag Manager
article_title: Google Tag Manager mit dem Braze SDK
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Erfahren Sie, wie Sie das Braze SDK mit Methoden wie der Laufzeitinitialisierung, der verzögerten Initialisierung oder dem Google Tag Manager initialisieren."

---

# Google Tag Manager mit dem Braze SDK {#google-tag-manager-with-the-braze-sdk}

> Erfahren Sie, wie Sie den [Google Tag Manager (GTM)](https://developers.google.com/tag-platform/tag-manager) mit dem Braze SDK verwenden, um das Braze-Event-Tracking und Aktualisierungen von Nutzer:innen-Attributen per Fernzugriff zu steuern, ohne Codeänderungen oder neue App-Releases zu benötigen.

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

Das Braze-Initialisierungs-Tag muss vor allen Tags ausgelöst werden, die Braze-SDK-Methoden aufrufen (wie `braze.getUser()`, `braze.logCustomEvent()` oder `braze.logPurchase()`). Wenn diese Methoden ausgelöst werden, bevor das SDK initialisiert ist, können Fehler wie `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')` auftreten.

So konfigurieren Sie die Tag-Sequenzierung im Google Tag Manager:

1. Öffnen Sie das Tag, das Braze-SDK-Methoden aufruft (z. B. ein Custom-HTML-Tag oder ein Braze-Aktions-Tag).
2. Gehen Sie zu **Advanced Settings** > **Tag Sequencing**.
3. Wählen Sie **A tag that fires before [this tag] is fired**.
4. Wählen Sie Ihr **Braze Initialization**-Tag aus.

Dadurch wird sichergestellt, dass das SDK vollständig geladen ist, bevor andere Tags versuchen, Braze-Methoden aufzurufen.

Weitere Informationen finden Sie unter [Tag-Sequenzierung für angepasste Events überprüfen]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing).

## Käufe mit GTM protokollieren {#log-purchases-with-gtm}

In Braze-Aktions-Tags und Custom-HTML-Tags rufen Sie `braze.logPurchase()` auf, um Umsätze zu erfassen. Der veraltete Namespace `appboy.logPurchase()` wird in aktuellen Internet-SDK-Integrationen nicht unterstützt.

## Angepasste Events mit GTM protokollieren {#logging-custom-events-with-gtm}

Sie können angepasste Events mit einem **Custom HTML**-Tag in GTM protokollieren. Dieser Ansatz nutzt den GTM-[Data Layer](https://developers.google.com/tag-platform/tag-manager/datalayer), um Event-Daten von Ihrer Website an ein GTM-Tag zu übergeben, das das Braze Internet-SDK aufruft.

### Schritt 1: Event in den Data Layer pushen {#step-1-push-the-event-to-the-data-layer}

Pushen Sie in Ihrem Website-Code ein Event in den Data Layer, wo immer Sie das angepasste Event auslösen möchten. Um beispielsweise ein angepasstes Event zu protokollieren, wenn ein Button geklickt wird:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Schritt 2: Trigger im GTM erstellen {#step-2-create-a-trigger-in-gtm}

1. Gehen Sie in Ihrem GTM-Container zu **Triggers** und erstellen Sie einen neuen Trigger.
2. Setzen Sie den **Trigger Type** auf **Custom Event**.
3. Setzen Sie den **Event Name** auf denselben Wert, den Sie in den Data Layer gepusht haben (z. B. `my_custom_event`).
4. Wählen Sie, wann der Trigger ausgelöst werden soll (z. B. **All Custom Events**).

### Schritt 3: Custom-HTML-Tag erstellen {#step-3-create-a-custom-html-tag}

1. Gehen Sie im GTM zu **Tags** und erstellen Sie ein neues Tag.
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
Google aktualisiert seine [EU-Richtlinie zur Nutzer:innen-Einwilligung](https://www.google.com/about/company/user-consent-policy/) als Reaktion auf Änderungen des [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), der seit dem 6. März 2024 in Kraft ist. Diese neue Änderung verpflichtet Werbetreibende, bestimmte Informationen an ihre Endnutzer:innen im EWR und in Großbritannien weiterzugeben sowie die erforderlichen Einwilligungen von ihnen einzuholen. Lesen Sie die folgende Dokumentation, um mehr zu erfahren.
{% endalert %}

Im Rahmen von Googles EU-Richtlinie zur Nutzer:innen-Einwilligung müssen die folgenden booleschen angepassten Attribute in Nutzerprofilen protokolliert werden:

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

Wenn Braze nicht initialisiert wird oder Events nicht wie erwartet angezeigt werden, überprüfen Sie, ob Ihr GTM-Container veröffentlicht ist, ob Trigger und die Reihenfolge der Tag-Auslösung mit Ihrem SDK-[Lebenszyklus und Ihrer Initialisierungsstrategie]({{site.baseurl}}/developer_guide/sdk_integration) übereinstimmen und ob Testgeräte keine Braze-Endpunkte blockieren.

Bei Initialisierungsfehlern überprüfen Sie, ob das Braze-Tag oder der Anbieter der angepassten Tags den erwarteten `actionType` und die erwarteten Parameter erhält (siehe die Tabs für Android, Swift und Internet auf dieser Seite). Um bei der Validierung von GTM-ausgelösten Events eine ausführliche Protokollierung zu aktivieren, aktivieren Sie das SDK-Debug-Logging Ihrer Plattform, wie in den Plattform-Integrationsleitfäden beschrieben, die über diese Tabs verlinkt sind.