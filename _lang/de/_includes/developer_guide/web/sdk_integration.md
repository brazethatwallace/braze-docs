## Über das Braze Internet-SDK {#about-the-web-braze-sdk}

Das Braze Internet-SDK ermöglicht es Ihnen, Analytics zu erfassen und Ihren Internet-Nutzer:innen umfangreiche In-App-Nachrichten, Push-Benachrichtigungen und Content-Card-Nachrichten anzuzeigen. Weitere Informationen finden Sie in der [Braze JavaScript-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Das Internet-SDK integrieren {#integrate-the-web-sdk}

Sie können das Internet-SDK von Braze mit den folgenden Methoden integrieren. Weitere Optionen finden Sie unter [Andere Integrationsmethoden](#web_other-integration-methods).

- **Code-basierte Integration:** Integrieren Sie das Internet-SDK von Braze direkt in Ihre Codebasis mit Ihrem bevorzugten Paketmanager oder dem Braze-CDN. So haben Sie die volle Kontrolle darüber, wie das SDK geladen und konfiguriert wird.
- **Google Tag Manager:** Eine No-Code-Lösung, mit der Sie das Internet-SDK von Braze integrieren können, ohne den Code Ihrer Website zu ändern. Weitere Informationen finden Sie unter [Google Tag Manager mit dem Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager).

{% alert important %}
Wir empfehlen die Verwendung der [NPM-Integrationsmethode]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Zu den Vorteilen gehören die lokale Speicherung von SDK-Bibliotheken auf Ihrer Website, Schutz vor Werbeblocker-Erweiterungen und kürzere Ladezeiten durch Bundler-Unterstützung.
{% endalert %}

{% tabs local %}
{% tab Code-basierte Integration %}
### Schritt 1: Die Braze-Bibliothek installieren {#step-1-install-the-braze-library}

Sie können die Braze-Bibliothek mit einer der folgenden Methoden installieren. Falls Ihre Website jedoch eine `Content-Security-Policy` verwendet, lesen Sie zunächst die [Content Security Policy]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy).

{% alert important %}
Obwohl die meisten Werbeblocker das Braze Internet-SDK nicht blockieren, sind einige restriktivere Werbeblocker dafür bekannt, Probleme zu verursachen.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
Falls Ihre Website NPM- oder Yarn-Paketmanager verwendet, können Sie das [Braze NPM-Paket](https://www.npmjs.com/package/@braze/web-sdk) als Abhängigkeit hinzufügen.

TypeScript-Definitionen sind seit v3.0.0 enthalten. Hinweise zum Upgrade von 2.x auf 3.x finden Sie in unserem [Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Nach der Installation können Sie die Bibliothek wie gewohnt mit `import` oder `require` einbinden:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Fügen Sie das Braze Internet-SDK direkt zu Ihrem HTML hinzu, indem Sie unser CDN-gehostetes Skript referenzieren, das die Bibliothek asynchron lädt.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Die Standard-Einstellung **Seitenübergreifendes Tracking verhindern** in Safari kann dazu führen, dass In-App-Nachrichtentypen wie Banner und Content Cards bei Verwendung der CDN-Integrationsmethode nicht angezeigt werden. Um dieses Problem zu vermeiden, verwenden Sie die NPM-Integrationsmethode, damit Safari diese Nachrichten nicht als seitenübergreifenden Datenverkehr einstuft und Ihre Web-Nutzer:innen sie in allen unterstützten Browsern sehen können.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Schritt 2: Das SDK initialisieren {#step-2-initialize-the-sdk}

Nachdem das Braze Internet-SDK zu Ihrer Website hinzugefügt wurde, initialisieren Sie die Bibliothek mit dem API-Schlüssel und der [SDK-Endpunkt-URL]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints), die Sie im Braze-Dashboard unter **Einstellungen** > **App-Einstellungen** finden. Eine vollständige Liste der Optionen für `braze.initialize()` sowie unsere weiteren JavaScript-Methoden finden Sie in der [Braze JavaScript-Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

{% alert note %}
**Angepasste Domains für Internet-SDK-Anfragen werden nicht unterstützt**: Die `baseUrl` des Internet-SDK muss ein Braze-SDK-Endpunkt sein (z. B. `sdk.iad-05.braze.com`). Braze unterstützt kein Routing von Internet-SDK-Datenverkehr über eine kundeneigene Domain via CNAME-Einträge. Falls Sie benötigen, dass Internet-SDK-Anfragen von Ihrer eigenen Domain ausgehen, wenden Sie sich an den Braze-Support.
{% endalert %}

```javascript
// initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
    enableLogging: false, // set to `true` for debugging
    allowUserSuppliedJavascript: false, // set to `true` to support custom HTML messages
});

// Enable automatic display of in-app messages
// Required if you want in-app messages to display automatically when triggered
braze.automaticallyShowInAppMessages();

// if you use Content Cards
braze.subscribeToContentCardsUpdates(function(cards){
    // cards have been updated
});

// optionally set the current user's external ID before starting a new session
// you can also call `changeUser` later in the session after the user logs in
if (isLoggedIn){
    braze.changeUser(userIdentifier);
}

// `openSession` should be called last - after `changeUser` and `automaticallyShowInAppMessages`
braze.openSession();
```

{% alert important %}
**Anzeige von In-App-Nachrichten**: Um In-App-Nachrichten automatisch anzuzeigen, wenn sie getriggert werden, müssen Sie `braze.automaticallyShowInAppMessages()` aufrufen. Ohne diesen Aufruf werden In-App-Nachrichten nicht automatisch angezeigt. Falls Sie die Nachrichtenanzeige manuell steuern möchten, entfernen Sie diesen Aufruf und verwenden Sie stattdessen `braze.subscribeToInAppMessage()`. Weitere Informationen finden Sie unter [Automatische Trigger deaktivieren]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#disabling-automatic-triggers).
{% endalert %}

#### Fehlerbehebung bei fehlenden Sitzungen für anonyme Nutzer:innen {#troubleshooting-missing-sessions-for-anonymous-users}

Falls Sie ein Verhalten beobachten, bei dem Sitzungen fehlen, oder Sie die Sitzung für Nutzer:innen, die auf der Website anonym bleiben, nicht verfolgen können, stellen Sie sicher, dass Ihre Integration `braze.openSession()` während der Initialisierung aufruft.

- **Szenario:** Anonyme Nutzer:innen können eine Braze-ID zurückgeben, aber Sitzungsdaten sind leer oder fehlen.
- **Ursache:** Die Implementierung ruft `braze.openSession()` nicht auf.
- **Lösung:** Rufen Sie `braze.openSession()` immer nach der Initialisierung auf (und nach `braze.changeUser()`, falls Sie eine externe ID setzen).

Weitere Informationen finden Sie unter [Schritt 2: Das SDK initialisieren]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk).

{% alert important %}
Anonyme Nutzer:innen auf Mobilgeräten oder im Internet können zu Ihren [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users) gezählt werden. Daher kann es sinnvoll sein, das SDK bedingt zu laden oder zu initialisieren, um diese Nutzer:innen von Ihrer MAU-Zählung auszuschließen.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Bot-Traffic filtern {#bot-filtering}

MAU kann einen Prozentsatz an Bot-Nutzer:innen enthalten, was die Anzahl Ihrer monatlich aktiven Nutzer:innen erhöht. Das Braze Web SDK verfügt zwar über eine integrierte Erkennung für einige gängige Webcrawler (wie Suchmaschinen-Bots und Social-Media-Vorschau-Bots), dennoch ist es besonders wichtig, proaktiv mit robusten Lösungen zur Erkennung von Bots zu arbeiten, da SDK-Updates allein nicht in der Lage sind, jeden neuen Bot konsistent zu erkennen.

### Einschränkungen der Bot-Erkennung auf SDK-Seite {#limitations-of-sdk-side-bot-detection}

Das Web SDK umfasst eine grundlegende, auf User-Agents basierende Bot-Erkennung, die bekannte Crawler herausfiltert. Dieser Ansatz weist jedoch Einschränkungen auf:

- **Es entstehen ständig neue Bots**: KI-Unternehmen und andere Akteure entwickeln regelmäßig neue Bots, die sich möglicherweise tarnen, um einer Erkennung zu entgehen.
- **User-Agent-Spoofing**: Ausgefeilte Bots können legitime Browser-User-Agents imitieren.
- **Angepasste Bots**: Nicht-technische Nutzer:innen können nun auf einfache Weise Bots mithilfe großer Sprachmodelle (LLMs) erstellen, wodurch das Verhalten der Bots unvorhersehbar wird.

### Implementierung von Bot-Filtern {#implementing-bot-filtering}

{% alert important %}
Die nachfolgend aufgeführten Lösungen sind allgemeine Vorschläge. Passen Sie die Bot-Filterlogik an Ihre individuelle Umgebung und Ihre Datenverkehrsmuster an.
{% endalert %}

Die zuverlässigste Lösung besteht darin, Ihre eigene Bot-Filterlogik zu implementieren, bevor Sie das Braze SDK initialisieren. Zu den gängigen Ansätzen gehören:

#### Nutzerinteraktion erforderlich {#require-user-interaction}

Es wird empfohlen, die Initialisierung des SDK zu verzögern, bis Nutzer:innen eine sinnvolle Interaktion durchführen, wie beispielsweise das Akzeptieren eines Cookie-Consent-Banners, das Scrollen oder einen Klick. Dieser Ansatz ist häufig einfacher umzusetzen und kann beim Filtern von Bot-Traffic sehr effektiv sein.

{% alert important %}
Wenn Sie die Initialisierung des SDK bis zur Nutzerinteraktion verzögern, kann dies dazu führen, dass Banner und Content Cards ebenfalls erst nach dieser Interaktion angezeigt werden.
{% endalert %}

#### Erkennung angepasster Bots {#custom-bot-detection}

Implementieren Sie eine angepasste Erkennung basierend auf Ihren spezifischen Bot-Traffic-Mustern, wie zum Beispiel:

- Analyse von User-Agent-Strings auf Muster, die Sie in Ihrem Datenverkehr identifiziert haben
- Überprüfung auf Indikatoren für einen Headless-Browser
- Nutzung von Bot-Erkennungsdiensten von Drittanbietern
- Überwachung von Verhaltenssignalen, die für Ihre Website spezifisch sind

**Beispiel für bedingte Initialisierung:**

```javascript
// Only initialize Braze if your custom bot detection determines this is not a bot
if (!isLikelyBot()) {
  braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE"
  });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
}
```

### Best Practices

- Analysieren Sie regelmäßig Ihre MAU-Daten und Web-Traffic-Muster, um neues Bot-Verhalten zu erkennen.
- Führen Sie gründliche Tests durch, um sicherzustellen, dass Ihre Bot-Filterung keine legitimen Nutzer:innen vom Tracking ausschließt.
- Aktualisieren Sie Ihre Filterlogik auf Grundlage der Bot-Traffic-Muster, die Sie in Ihrer Umgebung beobachten.

## Optionale Konfigurationen {#optional-configurations}

### Protokollierung {#logging}

Um die Protokollierung schnell zu aktivieren, können Sie `?brazeLogging=true` als Parameter zu Ihrer Website-URL hinzufügen. Alternativ können Sie die [einfache](#web_basic-logging) oder die [benutzerdefinierte](#web_custom-logging) Protokollierung aktivieren. Einen zentralen Überblick über alle Plattformen finden Sie unter [Ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

#### Einfache Protokollierung {#basic-logging}

{% tabs local %}
{% tab Vor der Initialisierung %}
Verwenden Sie `enableLogging`, um einfache Debugging-Nachrichten vor der Initialisierung des SDK in der JavaScript-Konsole zu protokollieren.

```javascript
enableLogging: true
```

Ihre Methode sollte in etwa so aussehen:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab Nach der Initialisierung %}
Verwenden Sie `braze.toggleLogging()`, um einfache Debugging-Nachrichten nach der Initialisierung des SDK in der JavaScript-Konsole zu protokollieren. Ihre Methode sollte in etwa so aussehen:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
});
braze.openSession();
...
braze.toggleLogging();
```
{% endtab %}
{% endtabs %}

{% alert important %}
Einfache Protokolle sind für alle Nutzer:innen sichtbar. Deaktivieren Sie sie daher oder wechseln Sie zu [`setLogger`](#web_custom-logging), bevor Sie Ihren Code in die Produktionsumgebung überführen.
{% endalert %}

#### Benutzerdefinierte Protokollierung {#custom-logging}

Verwenden Sie `setLogger`, um benutzerdefinierte Debugging-Nachrichten in der JavaScript-Konsole zu protokollieren. Im Gegensatz zu einfachen Protokollen sind diese Protokolle für Nutzer:innen nicht sichtbar.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Ersetzen Sie `STRING` durch Ihre Nachricht als einzelnen String-Parameter. Ihre Methode sollte in etwa so aussehen:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Upgrade des SDK {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

Wenn Sie das Braze Internet-SDK über unser Content Delivery Network referenzieren, z. B. `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (wie in unseren standardmäßigen Integrationsanweisungen empfohlen), erhalten Ihre Nutzer:innen kleinere Updates (Fehlerbehebungen und abwärtskompatible Features, in diesem Beispiel die Versionen `a.a.a` bis `a.a.z`) automatisch, wenn sie Ihre Website aktualisieren.

Wenn wir jedoch größere Änderungen veröffentlichen, müssen Sie das Braze Internet-SDK manuell aktualisieren, um sicherzustellen, dass Breaking Changes Ihre Integration nicht beeinträchtigen. Darüber hinaus erhalten Sie keine automatischen Versionsupdates, wenn Sie unser SDK herunterladen und selbst hosten. In diesem Fall sollten Sie manuell aktualisieren, um die neuesten Features und Fehlerbehebungen zu erhalten.

Sie können sich über unsere neuesten Releases auf dem Laufenden halten, indem Sie [unseren Release-Feed verfolgen](https://github.com/braze-inc/braze-web-sdk/tags.atom) – mit dem RSS-Reader oder Dienst Ihrer Wahl – und [unser Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) einsehen, um eine vollständige Übersicht über unseren Internet-SDK-Release-Verlauf zu erhalten. So aktualisieren Sie das Braze Internet-SDK:

- Aktualisieren Sie die Version der Braze-Bibliothek, indem Sie die Versionsnummer von `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ändern – oder in den Abhängigkeiten Ihres Paketmanagers.
- Wenn Sie Web-Push integriert haben, aktualisieren Sie die Service-Worker-Datei auf Ihrer Website. Standardmäßig befindet sich diese unter `/service-worker.js` im Stammverzeichnis Ihrer Website, der Speicherort kann jedoch in einigen Integrationen angepasst sein. Sie müssen auf das Stammverzeichnis zugreifen, um eine Service-Worker-Datei zu hosten.

Sie müssen diese beiden Dateien koordiniert aktualisieren, um eine ordnungsgemäße Funktionalität sicherzustellen.

## Andere Integrationsmethoden {#other-integration-methods}

### Accelerated Mobile Pages (AMP)
{% details Mehr erfahren %}
#### Schritt 1: AMP-Web-Push-Script einbinden {#step-1-include-amp-web-push-script}

Fügen Sie das folgende asynchrone Script-Tag zu Ihrem Head hinzu:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Schritt 2: Abo-Widgets hinzufügen {#step-2-add-subscription-widgets}

Fügen Sie dem Body Ihres HTML ein Widget hinzu, mit dem Nutzer:innen Push-Benachrichtigungen abonnieren und abbestellen können.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

#### Schritt 3: `helper-iframe` und `permission-dialog` hinzufügen {#step-3-add-helper-iframe-and-permission-dialog}

Die AMP-Web-Push-Komponente erstellt ein Popup zur Verwaltung von Push-Abos. Daher müssen Sie die folgenden Hilfsdateien zu Ihrem Projekt hinzufügen, um dieses Feature zu aktivieren:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Schritt 4: Eine Service-Worker-Datei erstellen {#step-4-create-a-service-worker-file}

Erstellen Sie eine Datei `service-worker.js` im Stammverzeichnis Ihrer Website und fügen Sie das folgende Snippet hinzu:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Schritt 5: Das AMP-Web-Push-HTML-Element konfigurieren {#step-5-configure-the-amp-web-push-html-element}

Fügen Sie das folgende `amp-web-push`-HTML-Element zu Ihrem HTML-Body hinzu. Beachten Sie, dass Sie Ihren [`apiKey` und `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) als Query-Parameter an `service-worker-URL` anhängen müssen.

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```
{% enddetails %}

### Asynchronous Module Definition (AMD)

#### Unterstützung deaktivieren {#disable-support}

Wenn Ihre Website RequireJS oder einen anderen AMD-Modul-Loader verwendet, Sie das Braze Internet-SDK aber lieber über eine der anderen Optionen in dieser Liste laden möchten, können Sie eine Version der Bibliothek laden, die keine AMD-Unterstützung enthält. Diese Version der Bibliothek kann vom folgenden CDN-Standort geladen werden:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Modul-Loader {#module-loader}

Wenn Sie RequireJS oder andere AMD-Modul-Loader verwenden, empfehlen wir, eine Kopie unserer Bibliothek selbst zu hosten und sie wie andere Ressourcen zu referenzieren:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

Electron unterstützt Web-Push-Benachrichtigungen nicht offiziell (siehe: dieses [GitHub Issue](https://github.com/electron/electron/issues/6697)). Es gibt andere [Open-Source-Workarounds](https://github.com/MatthieuLemoine/electron-push-receiver), die Sie ausprobieren können, die jedoch nicht von Braze getestet wurden.

### Jest-Framework {#jest}

Bei Verwendung von Jest wird möglicherweise ein Fehler wie `SyntaxError: Unexpected token 'export'` angezeigt. Um dies zu beheben, passen Sie Ihre Konfiguration in `package.json` an, damit das Braze SDK ignoriert wird:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### SSR-Frameworks {#ssr}

Das Internet-SDK wird in einer Browser-Umgebung ausgeführt. In SSR-Frameworks initialisieren Sie Braze in einer Client-Only-Komponente, damit Ihr Server niemals SDK-Code ausführt.

#### Framework-unabhängiger dynamischer Import {#framework-agnostic-dynamic-import}

Wenn Ihr Framework in diesem Abschnitt nicht aufgeführt ist, können Sie Braze dynamisch aus einem Client-Only-Lifecycle-Hook importieren.

```javascript
// MyComponent/braze-exports.js
// Export the parts of the SDK that you need.
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
useEffect(() => {
    import("./braze-exports.js").then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

Wenn Sie webpack verwenden, können Sie dynamisch nur bestimmte SDK-Exporte importieren.

```javascript
// MyComponent.js
useEffect(() => {
    import(
        /* webpackExports: ["initialize", "openSession"] */
        "@braze/web-sdk"
    ).then(({ initialize, openSession }) => {
        initialize("YOUR-API-KEY-HERE", {
            baseUrl: "YOUR-SDK-ENDPOINT",
            enableLogging: true,
        });
        openSession();
    });
}, []);
```

#### Gemeinsamer Hook für Next.js und Remix {#shared-hook-for-nextjs-and-remix}

Erstellen Sie einen wiederverwendbaren `useBraze`-Hook und rufen Sie ihn in der Nähe Ihres App-Roots auf.

```tsx
// hooks/useBraze.ts
import { useEffect, useRef } from "react";

export function useBraze() {
  const didInit = useRef(false);

  useEffect(() => {
    if (didInit.current) {
      return;
    }
    didInit.current = true;

    import("@braze/web-sdk")
      .then((braze) => {
        const initialized = braze.initialize("YOUR-API-KEY-HERE", {
          // Use your Braze Web SDK endpoint, such as sdk.iad-01.braze.com.
          baseUrl: "YOUR-SDK-ENDPOINT",
          enableLogging: false,
        });
        if (!initialized) {
          return;
        }

        // Optional: Identify signed-in users before opening a session.
        // braze.changeUser("external-id");

        // Optional: Automatically display in-app messages.
        // braze.automaticallyShowInAppMessages();
        braze.openSession();
      })
      .catch((error) => {
        console.error("Unable to load Braze SDK:", error);
      });
  }, []);
}
```

#### Next.js (App Router)

Rufen Sie `useBraze` in einer Client-Komponente auf, die Ihre App umschließt.

```tsx
// app/components/AppRoot.tsx
"use client";

import type { ReactNode } from "react";
import { useBraze } from "../hooks/useBraze";

export function AppRoot({ children }: { children: ReactNode }) {
  useBraze();
  return <>{children}</>;
}
```

```tsx
// app/layout.tsx
import type { ReactNode } from "react";
import { AppRoot } from "./components/AppRoot";

export default function RootLayout({
  children,
}: {
  children: ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <AppRoot>{children}</AppRoot>
      </body>
    </html>
  );
}
```

#### Next.js (Pages Router)

Rufen Sie `useBraze` am Anfang Ihrer benutzerdefinierten App-Komponente auf.

```tsx
// pages/_app.tsx
import type { AppProps } from "next/app";
import { useBraze } from "../hooks/useBraze";

export default function App({ Component, pageProps }: AppProps) {
  useBraze();

  return (
    <Component {...pageProps} />
  );
}
```

#### Remix

Rufen Sie `useBraze` am Anfang Ihrer Root-Route-Komponente auf.

Für lokale Remix-Validierungsbeispiele führen Sie `PORT=4013 npm run dev` aus.

```tsx
// app/root.tsx
import { Outlet } from "@remix-run/react";
import { useBraze } from "./hooks/useBraze";

export default function App() {
  useBraze();

  return <Outlet />;
}
```

#### Ereignisse protokollieren und Nutzer:innen aktualisieren {#logging-events-and-updating-users}

Nachdem `useBraze` das SDK an Ihrem App-Root initialisiert hat, können andere Client-Komponenten Braze-Methoden aufrufen. Ein gängiges Muster ist der Aufruf innerhalb von Nutzeraktionen wie `onClick` oder `onSubmit`. Im Beispiel werden die SDK-Methoden innerhalb des Click-Handlers geladen, anstatt am Anfang der Datei. Dadurch bleibt das Internet-SDK außerhalb des Server-Codes und es wird nur das geladen, was diese Aktion benötigt. Der `webpackExports`-Kommentar teilt webpack mit, welche Methoden eingebunden werden sollen, sodass Ihr Bundle kleiner bleibt.

```tsx
// app/components/BuyButton.tsx
"use client";

export function BuyButton() {
  const handleClick = async () => {
    const { logCustomEvent, logPurchase, getUser } = await import(
      /* webpackExports: ["logCustomEvent", "logPurchase", "getUser"] */
      "@braze/web-sdk"
    );

    getUser()?.setCustomUserAttribute("last_purchase_date", "2026-05-04");
    logCustomEvent("clicked_buy", { source: "product_page" });
    logPurchase("sku_123", 19.99, "USD");
  };

  return <button onClick={handleClick}>Buy</button>;
}
```

Dieses Beispiel zeigt eine `BuyButton`-Komponente, die Aktivitäten protokolliert, wenn jemand auf **Kaufen** klickt. Zuerst werden nur `logCustomEvent`, `logPurchase` und `getUser` zum Klick-Zeitpunkt importiert. Dann wird ein Nutzerattribut aktualisiert, ein angepasstes Event protokolliert und ein Kauf erfasst. Dieses Muster hilft Ihnen, die Initialisierung zentral in `useBraze` zu halten, während Sie gleichzeitig bedeutungsvolle Aktionen aus jeder Client-Komponente heraus tracken können.

Wenn Sie Remix mit Vite verwenden und package-root-Importe zur Laufzeit fehlschlagen, nutzen Sie den bestehenden Vite-Workaround. Weitere Informationen finden Sie unter [Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite).

Eine vollständige Liste der verfügbaren Methoden finden Sie in der [Braze JavaScript-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

### Tealium iQ

Tealium iQ bietet eine grundlegende schlüsselfertige Braze-Integration. Um die Integration zu konfigurieren, suchen Sie in der Tealium Tag Management-Oberfläche nach Braze und geben Sie den Internet-SDK-API-Schlüssel aus Ihrem Dashboard an.

Für weitere Details oder ausführliche Unterstützung bei der Tealium-Konfiguration lesen Sie unsere [Integrationsdokumentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium#about-tealium) oder wenden Sie sich an Ihren Tealium Account Manager.

### Vite {#vite}

Wenn Sie Vite verwenden und eine Warnung zu zirkulären Abhängigkeiten oder `Uncaught TypeError: Class extends value undefined is not a constructor or null` sehen, müssen Sie das Braze SDK möglicherweise aus der [Dependency Discovery](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior) ausschließen:

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Andere Tag-Manager {#other-tag-managers}

Braze kann auch mit anderen Tag-Management-Lösungen kompatibel sein, indem Sie unsere Integrationsanweisungen innerhalb eines benutzerdefinierten HTML-Tags befolgen. Wenden Sie sich an eine Braze-Vertretung, wenn Sie Hilfe bei der Bewertung dieser Lösungen benötigen.