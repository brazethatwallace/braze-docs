---
nav_title: JavaScript-Bridge
article_title: JavaScript-Bridge für Landing-Pages
page_order: 5
page_type: reference
description: "Erfahren Sie, wie Sie die brazeBridge-JavaScript-Bridge verwenden, um Events zu protokollieren, angepasste Attribute zu setzen und Braze-Aktionen aus dem Custom-Code-Block einer Landing-Page zu triggern."
---

# JavaScript-Bridge für Landing-Pages {#javascript-bridge-for-landing-pages}

> Landing-Pages unterstützen eine JavaScript-„Bridge“ zur Verbindung Ihres angepassten Codes (HTML, CSS und JavaScript) mit dem Braze SDK.

Greifen Sie auf die Bridge zu, indem Sie `brazeBridge` in einem Custom-Code-Block verwenden, um Events zu protokollieren, angepasste Attribute zu setzen, Nutzer:innen zu identifizieren und mehr, wenn Besucher:innen mit Ihrer Landing-Page interagieren.

## Funktionsweise {#how-it-works}

Landing-Pages ermöglichen es Ihnen, angepasstes HTML, CSS und JavaScript in einem **Custom-Code**-Block hinzuzufügen, um mehr Kontrolle über das Aussehen, das Erscheinungsbild und das Verhalten Ihrer Seite zu erhalten. Custom-Code-Blöcke können die [JavaScript-Bridge](#supported-methods) nutzen, um Events zu protokollieren, angepasste Attribute zu setzen, Nutzer:innen zu identifizieren und mehr:
- Angepasste Events und Käufe protokollieren
- Standard- und angepasste Nutzer:innenattribute setzen
- Klicks und Formularübermittlungen tracken
- Nutzer:innen identifizieren

Wenn Sie `brazeBridge`-Code aus In-App-Nachrichten oder Bannern wiederverwenden, sollte er auch auf Landing-Pages funktionieren. Methoden, die nicht auf Landing-Pages anwendbar sind, werden ignoriert und protokollieren stattdessen eine Warnung in der Browser-Konsole, anstatt einen Fehler zu verursachen. Weitere Details finden Sie unter [Auf Landing-Pages nicht unterstützte Methoden](#methods-not-supported-on-landing-pages).

{% alert important %}
Die Landing-Page-Bridge ist asynchron; jede Methode gibt ein Promise zurück. Das unterscheidet sich von der [angepassten HTML-In-App-Nachrichten-Bridge]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge), deren Methoden sofort zurückkehren. Wenn der nächste Schritt in Ihrem Skript davon abhängt, dass ein Bridge-Aufruf abgeschlossen ist – etwa eine Seitenweiterleitung, eine Formularübermittlung oder das Senden von Daten an Braze – verwenden Sie `await` oder `.then()` und gehen Sie nicht davon aus, dass der Aufruf synchron abgeschlossen wurde.
{% endalert %}

## Verfügbarkeit der Bridge {#bridge-availability}

Wenn Besucher:innen Ihre Landing-Page öffnen, ist `brazeBridge` bereits in Ihrem **Custom-Code**-JavaScript verfügbar. Rufen Sie Bridge-Methoden direkt auf Landing-Pages auf – Sie müssen nicht auf ein separates Ready-Event warten, wie es In-App-Nachrichten mit `ab.BridgeReady` verwenden.

Dass das Bridge-Objekt verfügbar ist, bedeutet nicht, dass das Braze SDK für diese:n Besucher:in initialisiert ist. Das SDK wird bei einem Landing-Page-Besuch in einem der folgenden Fälle initialisiert:

- Die:der Besucher:in öffnet die Seite über einen [Landing-Page-Liquid-Tag]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users), der über einen Braze-Kanal (E-Mail, SMS, Push usw.) gesendet wurde. Das SDK wird automatisch beim Laden der Seite initialisiert.
- Die:der Besucher:in übermittelt das Formular der Seite – zum Beispiel durch Klicken auf einen **Absenden**-Button, der Formulardaten sendet. Dies umfasst auch `brazeBridge`-Aufrufe, die innerhalb der `registerFormInput`-Callbacks eines [angepassten Formularblocks]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) ausgeführt werden, da diese als Teil der Formularübermittlung laufen.

Wenn Besucher:innen die Landing-Page direkt öffnen, ohne einen Landing-Page-Liquid-Tag, und das Formular nie übermitteln, ist die Seite für Braze anonym, und Bridge-Methodenaufrufe haben keine Wirkung.

{% alert note %}
`window.lpBridge` und `window.appboyBridge` verweisen auf dasselbe Bridge-Objekt, sind aber beide veraltet. Verwenden Sie `window.brazeBridge`.
{% endalert %}

## Beispiel {#example}

Da die Methoden asynchron sind, verwenden Sie einen async-Handler und `await` für die Aufrufe, wenn die Reihenfolge oder der Abschluss wichtig ist:

```html
<button id="button">Set Favorite Color</button>
<script>
  document.querySelector("#button").onclick = async function () {
    // Track a click for analytics
    await brazeBridge.logClick("set-favorite-color");
    // Set the user's custom attribute
    await brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    await brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    await brazeBridge.requestImmediateDataFlush();
  };
</script>
```

## Unterstützte Methoden {#supported-methods}

Die folgenden `brazeBridge`-Methoden geben ein Promise zurück und werden in **Custom-Code**-Blöcken von Landing-Pages unterstützt. Verwenden Sie `await` oder `.then()`, wenn Sie Arbeitsschritte sequenzieren oder den Abschluss garantieren müssen.

### Methoden der obersten Ebene {#top-level-methods}

| Methode | Beschreibung |
| --- | --- |
| `brazeBridge.changeUser(userId, signature?)` | Identifiziert die:den Nutzer:in mit einer eindeutigen ID. |
| `brazeBridge.logCustomEvent(eventName, eventProperties?)` | Protokolliert ein angepasstes Event. |
| `brazeBridge.logPurchase(productId, price, currencyCode?, quantity?, purchaseProperties?)` | Protokolliert einen Kauf. |
| `brazeBridge.requestImmediateDataFlush(callback?)` | Sendet die in der Warteschlange befindlichen Daten an die Braze-Server. |
| `brazeBridge.logClick(trackingId)` | Protokolliert einen Landing-Page-Klick (`lp_c`) für die angegebene Tracking-ID. Siehe [Klick-Tracking](#click-tracking). |
| `brazeBridge.logSubmit()` | Protokolliert eine Landing-Page-Formularübermittlung (`lp_fs`). Landing-Page-spezifisch. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Methoden der obersten Ebene" }

### `getUser()`-Methoden {#getuser-methods}

{% alert note %}
`brazeBridge.getUser()` gibt synchron ein einfaches Objekt zurück, sodass Sie `getUser()` nicht mit `await` aufrufen müssen; die Methoden des zurückgegebenen Objekts (wie `getUser().setEmail(email)`) geben Promises zurück.
{% endalert %}

`getUser()` gibt ein Objekt zurück, das die folgenden Nutzer:innenmethoden bereitstellt. Jede Methode gibt ein Promise zurück.

| Methode | Beschreibung |
| --- | --- |
| `getUser().setFirstName(firstName)` | Setzt den Vornamen der:des Nutzer:in. |
| `getUser().setLastName(lastName)` | Setzt den Nachnamen der:des Nutzer:in. |
| `getUser().setEmail(email)` | Setzt die E-Mail-Adresse der:des Nutzer:in. |
| `getUser().setPhoneNumber(phoneNumber)` | Setzt die Telefonnummer der:des Nutzer:in. |
| `getUser().setGender(gender: "m" \| "f" \| "o" \| "u" \| "n" \| "p")` | Setzt das Geschlecht der:des Nutzer:in: männlich, weiblich, andere, unbekannt, nicht zutreffend oder möchte nicht angeben. |
| `getUser().setDateOfBirth(year, month, day)` | Setzt das Geburtsdatum der:des Nutzer:in. |
| `getUser().setCountry(country)` | Setzt das Land der:des Nutzer:in. |
| `getUser().setHomeCity(city)` | Setzt den Wohnort der:des Nutzer:in. |
| `getUser().setLanguage(language)` | Setzt die Sprache der:des Nutzer:in. |
| `getUser().setCustomUserAttribute(key, value, merge?)` | Setzt ein angepasstes Nutzer:innenattribut. |
| `getUser().addToCustomAttributeArray(key, value)` | Fügt einen Wert zu einem angepassten Attribut-Array hinzu. |
| `getUser().removeFromCustomAttributeArray(key, value)` | Entfernt einen Wert aus einem angepassten Attribut-Array. |
| `getUser().incrementCustomUserAttribute(key, incrementValue?)` | Erhöht ein numerisches angepasstes Attribut. |
| `getUser().setCustomLocationAttribute(key, latitude, longitude)` | Setzt ein angepasstes Standortattribut. |
| `getUser().addToSubscriptionGroup(subscriptionGroupId)` | Fügt die:den Nutzer:in einer E-Mail- oder SMS-Abo-Gruppe hinzu. |
| `getUser().removeFromSubscriptionGroup(subscriptionGroupId)` | Entfernt die:den Nutzer:in aus einer E-Mail- oder SMS-Abo-Gruppe. |
| `getUser().setEmailNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Setzt den E-Mail-Benachrichtigungs-Abo-Status. |
| `getUser().setPushNotificationSubscriptionType(type: "opted_in" \| "subscribed" \| "unsubscribed")` | Setzt den Push-Benachrichtigungs-Abo-Status. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="getUser()-Methoden" }

## Klick-Tracking {#click-tracking}

Verwenden Sie `brazeBridge.logClick(trackingId)`, um Klicks auf Ihrer Landing-Page zu tracken. Jeder Aufruf protokolliert ein Landing-Page-Klick-Event (`lp_c`), das mit der von Ihnen übergebenen Tracking-ID versehen ist:

```html
<a href="#" onclick="brazeBridge.logClick('cta-hero')">Get started</a>
```

{% alert note %}
Das Klick-Tracking auf Landing-Pages unterscheidet sich von In-App-Nachrichten, die `logClick('0')` und `logClick('1')` als konventionelle IDs für „Button 1“ und „Button 2“ verwenden. Landing-Pages haben keine entsprechenden speziellen Button-IDs. Jeder `logClick(trackingId)`-Aufruf protokolliert ein `lp_c`-Event, das durch die von Ihnen angegebene Tracking-ID identifiziert wird.
{% endalert %}

## Auf Landing-Pages nicht unterstützte Methoden {#methods-not-supported-on-landing-pages}

Die folgenden Methoden funktionieren in In-App-Nachrichten und Bannern, werden aber auf Landing-Pages nicht unterstützt. Wenn Ihr Code eine davon auf einer Landing-Page aufruft, ignoriert Braze den Aufruf. Ihre Seite funktioniert weiterhin, aber Sie sehen möglicherweise eine Warnung in der Entwicklerkonsole des Browsers.

| Methode | Hinweise |
| --- | --- |
| `brazeBridge.closeMessage()` | Es gibt keine Nachrichten-UI, die auf einer Landing-Page geschlossen werden könnte. |
| `brazeBridge.requestPushPermission(successCallback?, deniedCallback?)` | Push-Berechtigungen werden nicht von einer Landing-Page aus angefordert. |
| `brazeBridge.web.registerAppboyPushMessages(successCallback?, deniedCallback?)` | Web-Push-Registrierung ist auf Landing-Pages nicht verfügbar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Auf Landing-Pages nicht unterstützte Methoden" }

## Verwandte Inhalte {#related-content}

- [Angepasste Formularblöcke erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) behandelt eine fortgeschrittenere Nutzung dieser Bridge: die Verbindung einer vollständig angepassten UI mit einem Landing-Page-Formular.
- [Landing-Pages erstellen]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)