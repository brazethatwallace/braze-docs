## Über das Web Braze SDK {#about-the-web-braze-sdk}

Mit dem Web Braze SDK können Sie Analytics erfassen und Ihren Web-Nutzer:innen umfangreiche In-App-Nachrichten, Push-Benachrichtigungen und Content-Card-Nachrichten anzeigen. Weitere Informationen finden Sie in der [Braze JavaScript-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Web SDK integrieren {#integrate-the-web-sdk}

Sie können das Web Braze SDK mithilfe der folgenden Methoden integrieren. Weitere Optionen finden Sie unter [anderen Integrationsmethoden](#web_other-integration-methods).

- **Code-basierte Integration:** Führen Sie die Integration des Web Braze SDK direkt in Ihre Codebasis durch, indem Sie Ihren bevorzugten Paketmanager oder das Braze CDN verwenden. Dadurch erhalten Sie die vollständige Kontrolle darüber, wie das SDK geladen und konfiguriert wird.
- **Google Tag Manager:** Eine No-Code-Lösung, mit der Sie die Integration des Web Braze SDK durchführen können, ohne den Code Ihrer Website zu ändern. Weitere Informationen finden Sie unter [Google Tag Manager mit dem Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager).

{% alert important %}
Wir empfehlen die Verwendung der [NPM-Integrationsmethode]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Zu den Vorteilen gehören die lokale Speicherung von SDK-Bibliotheken auf Ihrer Website, die Immunität gegenüber Ad-Blocker-Erweiterungen und die Verkürzung der Ladezeiten im Rahmen der Bundler-Unterstützung.
{% endalert %}

{% tabs local %}
{% tab code-based integration %}
### 1. Schritt: Installieren Sie die Braze-Bibliothek {#step-1-install-the-braze-library}

Sie können die Braze-Bibliothek mit einer der folgenden Methoden installieren. Sollte Ihre Website jedoch eine `Content-Security-Policy` verwenden, überprüfen Sie bitte die [Content Security Policy]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy), bevor Sie fortfahren.

{% alert important %}
Während die meisten Werbeblocker das Braze Web SDK nicht blockieren, ist bekannt, dass einige restriktivere Werbeblocker Probleme verursachen können.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
Wenn Ihre Website die Paketmanager NPM oder Yarn verwendet, können Sie das [NPM-Paket von Braze](https://www.npmjs.com/package/@braze/web-sdk) als Abhängigkeit hinzufügen.

Ab v3.0.0 sind nun auch Typescript-Definitionen enthalten. Hinweise zum Upgrade von 2.x auf 3.x finden Sie in unserem [Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Nach der Installation können Sie die Bibliothek auf die übliche Weise mittels `import` oder `require` verwenden:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Fügen Sie das Braze Web SDK direkt in den HTML-Code ein, indem Sie auf das auf unserem CDN gehostete Skript verweisen, das die Bibliothek asynchron lädt.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Die Standard-Einstellung **Cross-Site-Tracking verhindern** in Safari kann dazu führen, dass In-App-Nachrichtentypen wie Banner und Content Cards nicht angezeigt werden, wenn Sie die CDN-Integrationsmethode verwenden. Um dieses Problem zu vermeiden, empfehlen wir die Verwendung der NPM-Integrationsmethode, damit Safari diese Nachrichten nicht als Cross-Site-Traffic einstuft und Ihre Nutzer:innen sie in allen unterstützten Webbrowsern sehen können.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### 2. Schritt: Initialisieren Sie das SDK {#step-2-initialize-the-sdk}

Nachdem Sie das Braze Web SDK zu Ihrer Website hinzugefügt haben, initialisieren Sie die Bibliothek mit dem API-Schlüssel und der [SDK-Endpunkt-URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints), die Sie in Ihrem Braze-Dashboard unter **Einstellungen** > **App-Einstellungen** finden. Eine vollständige Liste der Optionen für `braze.initialize()` sowie unsere anderen JavaScript-Methoden finden Sie in der [Braze JavaScript-Dokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

{% alert note %}
**Angepasste Domains für Web-SDK-Anfragen werden nicht unterstützt**: Die Web-SDK-`baseUrl` muss ein Braze-SDK-Endpunkt sein (zum Beispiel `sdk.iad-05.braze.com`). Braze unterstützt nicht die Weiterleitung von Web-SDK-Datenverkehr über CNAME-Einträge durch eine kundeneigene Domain. Sollten Sie Web-SDK-Anfragen von Ihrer eigenen Domain aus senden müssen, wenden Sie sich bitte an den Braze-Support.
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
**Anzeige von In-App-Nachrichten**: Um In-App-Nachrichten automatisch anzuzeigen, wenn sie getriggert werden, müssen Sie `braze.automaticallyShowInAppMessages()` aufrufen. Ohne diesen Aufruf werden In-App-Nachrichten nicht automatisch angezeigt. Wenn Sie die Anzeige von Nachrichten manuell verwalten möchten, entfernen Sie diesen Aufruf und verwenden Sie stattdessen `braze.subscribeToInAppMessage()`. Weitere Informationen finden Sie unter [Automatische Trigger deaktivieren]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#disabling-automatic-triggers).
{% endalert %}

#### Fehlerbehebung bei fehlenden Sitzungen für anonyme Nutzer:innen {#troubleshooting-missing-sessions-for-anonymous-users}

Wenn Sie das Verhalten „Sitzung fehlt“ beobachten oder das Tracking der Sitzung für Nutzer:innen, die im Web anonym bleiben, nicht durchführen können, stellen Sie sicher, dass Ihre Integration während der Initialisierung `braze.openSession()` aufruft.

- **Szenario:** Anonyme Nutzer:innen können eine Braze-ID zurückgeben, jedoch sind die Sitzungsdaten leer oder fehlen vollständig.
- **Ursache:** Die Implementierung ruft `braze.openSession()` nicht auf.
- **Lösung:** Rufen Sie `braze.openSession()` nach der Initialisierung immer auf (und nach `braze.changeUser()`, falls Sie eine externe ID festgelegt haben).

Weitere Informationen finden Sie in [Schritt 2: Initialisieren Sie das SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk).

{% alert important %}
Anonyme Nutzer:innen auf Mobil- oder Webgeräten können zu Ihrer [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users) gezählt werden. Vielleicht möchten Sie das SDK deshalb lieber bedingt laden oder initialisieren, um diese Nutzer:innen von der MAU-Zählung auszuschließen.
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

Um die Protokollierung schnell zu aktivieren, können Sie `?brazeLogging=true` als Parameter in die URL Ihrer Website einfügen. Alternativ können Sie auch die [einfache](#web_basic-logging) oder [angepasste](#web_custom-logging) Protokollierung aktivieren. Für eine zentralisierte Übersicht über alle Plattformen hinweg siehe [Ausführliche Protokollierung]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

#### Grundlegende Protokollierung {#basic-logging}

{% tabs local %}
{% tab Vor der Initialisierung %}
Verwenden Sie `enableLogging`, um grundlegende Debugging-Nachrichten in der JavaScript-Konsole zu protokollieren, bevor das SDK initialisiert wird.

```javascript
enableLogging: true
```

Ihre Methode sollte in etwa so aussehen wie die folgende:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab Nach der Initialisierung %}
Verwenden Sie `braze.toggleLogging()`, um grundlegende Debugging-Nachrichten in der JavaScript-Konsole zu protokollieren, nachdem das SDK initialisiert wurde. Ihre Methode sollte in etwa so aussehen wie die folgende:

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
Die Basisprotokolle sind für alle Nutzer:innen sichtbar. Daher sollten Sie diese Funktion deaktivieren oder zu [`setLogger`](#web_custom-logging) wechseln, bevor Sie Ihren Code für die Produktionsumgebung freigeben.
{% endalert %}

#### Angepasste Protokollierung {#custom-logging}

Verwenden Sie `setLogger`, um angepasste Debugging-Nachrichten in der JavaScript-Konsole zu protokollieren. Im Gegensatz zu den Basisprotokollen sind diese Protokolle für die Nutzer:innen nicht sichtbar.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Ersetzen Sie `STRING` durch Ihre Nachricht als einzelnen String-Parameter. Ihre Methode sollte in etwa so aussehen wie die folgende:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Upgraden des SDK {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

Wenn Sie das Braze Web SDK aus unserem Content Delivery Network referenzieren, zum Beispiel `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (wie in unseren Standard-Integrationsanweisungen empfohlen), erhalten Ihre Nutzer:innen automatisch kleinere Updates (Fehlerbehebungen und abwärtskompatible Features, Versionen `a.a.a` bis `a.a.z` in den obigen Beispielen), wenn sie Ihre Website aktualisieren.

Bei der Veröffentlichung größerer Änderungen bitten wir Sie jedoch, das Braze Web SDK manuell zu upgraden, um sicherzustellen, dass sich grundlegende Änderungen nicht auf Ihre Integration auswirken. Wenn Sie unser SDK herunterladen und selbst hosten, erhalten Sie keine automatischen Updates und müssen manuell upgraden, um die neuesten Features und Fehlerbehebungen zu erhalten.

Um auf dem aktuellen Stand zu bleiben, empfehlen wir Ihnen, mit dem RSS-Reader oder einem anderen Dienst Ihrer Wahl [unseren Release-Feed zu abonnieren](https://github.com/braze-inc/braze-web-sdk/tags.atom). Einen vollständigen Überblick über die Release-Historie unseres Web SDK finden Sie in [unserem Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md). So führen Sie ein Upgrade des Braze Web SDK durch:

- Aktualisieren Sie die Version der Braze-Bibliothek, indem Sie die Versionsnummer von `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ändern, oder in den Abhängigkeiten Ihres Paketmanagers.
- Wenn Sie Web-Push integriert haben, aktualisieren Sie die Service-Worker-Datei auf Ihrer Website – standardmäßig befindet sich diese Datei unter `/service-worker.js` im Stammverzeichnis Ihrer Website, aber der Speicherort kann bei einigen Integrationen angepasst werden. Sie müssen auf das Stammverzeichnis zugreifen, um eine Service-Worker-Datei zu hosten.

Bitte führen Sie ein Update für diese beiden Dateien in Abstimmung miteinander durch, um eine ordnungsgemäße Funktionalität zu gewährleisten.

## Andere Integrationsmethoden {#other-integration-methods}

### Accelerated Mobile Pages (AMP)
{% details Mehr anzeigen %}
#### 1. Schritt: AMP-Web-Push-Skript einbinden {#step-1-include-amp-web-push-script}

Fügen Sie den folgenden asynchronen Script-Tag in Ihren Head ein:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### 2. Schritt: Abo-Widgets hinzufügen {#step-2-add-subscription-widgets}

Fügen Sie ein Widget in den Body Ihres HTML-Codes ein, das es Nutzer:innen ermöglicht, Push-Benachrichtigungen zu abonnieren oder sich abzumelden.

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

#### 3. Schritt: `helper-iframe` und `permission-dialog` hinzufügen {#step-3-add-helper-iframe-and-permission-dialog}

Die AMP-Web-Push-Komponente erstellt ein Popup-Fenster zur Verwaltung von Push-Abonnements. Um dieses Feature zu aktivieren, müssen Sie die folgenden Hilfsdateien zu Ihrem Projekt hinzufügen:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### 4. Schritt: Erstellen Sie eine Service-Worker-Datei {#step-4-create-a-service-worker-file}

Erstellen Sie eine `service-worker.js`-Datei im Stammverzeichnis Ihrer Website und fügen Sie das folgende Snippet hinzu:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### 5. Schritt: Konfigurieren Sie das AMP-Web-Push-HTML-Element {#step-5-configure-the-amp-web-push-html-element}

Fügen Sie das folgende `amp-web-push`-HTML-Element in Ihren HTML-Body ein. Bitte beachten Sie, dass Sie Ihre [`apiKey` und `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) als Abfrageparameter an `service-worker-URL` anhängen müssen.

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

### Asynchrone Moduldefinition (AMD) {#asynchronous-module-definition-amd}

#### Unterstützung deaktivieren {#disable-support}

Falls Ihre Website RequireJS oder einen anderen AMD-Modul-Loader verwendet, Sie jedoch das Braze Web SDK lieber über eine der anderen Optionen in dieser Liste laden möchten, können Sie eine Version der Bibliothek laden, die keine AMD-Unterstützung enthält. Diese Version der Bibliothek kann vom folgenden CDN-Standort geladen werden:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Modul-Loader {#module-loader}

Wenn Sie RequireJS oder andere AMD-Modul-Loader verwenden, empfehlen wir Ihnen, selbst eine Kopie unserer Bibliothek zu hosten und genauso auf sie zu verweisen, wie Sie es mit anderen Ressourcen tun würden:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

Electron unterstützt offiziell keine Web-Push-Benachrichtigungen (siehe dieses [GitHub-Issue](https://github.com/electron/electron/issues/6697)). Es gibt andere [Open-Source-Workarounds](https://github.com/MatthieuLemoine/electron-push-receiver), die Sie ausprobieren können, die aber nicht von Braze getestet wurden.

### Jest-Framework {#jest}

Bei der Verwendung von Jest wird möglicherweise eine Fehlermeldung ähnlich `SyntaxError: Unexpected token 'export'` angezeigt. Passen Sie für die Fehlerbehebung Ihre Konfiguration in `package.json` so an, dass das Braze SDK ignoriert wird:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### SSR-Frameworks {#ssr}

Das Web SDK wird in einer Browserumgebung ausgeführt. In SSR-Frameworks initialisieren Sie Braze in einer Client-only-Komponente, damit Ihr Server niemals SDK-Code ausführt.

#### Framework-agnostischer dynamischer Import {#framework-agnostic-dynamic-import}

Wenn Ihr Framework in diesem Abschnitt nicht aufgeführt ist, können Sie Braze dynamisch aus einem Client-only-Lifecycle-Hook importieren.

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

Wenn Sie Webpack verwenden, können Sie nur bestimmte SDK-Exporte dynamisch importieren.

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

Rufen Sie `useBraze` am Anfang Ihrer angepassten App-Komponente auf.

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

Nachdem `useBraze` das SDK an Ihrem App-Root initialisiert hat, können andere Client-Komponenten Braze-Methoden aufrufen. Ein gängiges Muster besteht darin, sie innerhalb von Nutzeraktionen wie `onClick` oder `onSubmit` aufzurufen. Im Beispiel werden die SDK-Methoden innerhalb des Click-Handlers geladen, anstatt am Anfang der Datei. Dadurch bleibt das Web SDK aus dem Server-Code heraus und es wird nur das geladen, was diese Aktion benötigt. Der `webpackExports`-Kommentar teilt Webpack mit, welche Methoden einbezogen werden sollen, sodass Ihr Bundle kleiner bleibt.

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

Dieses Beispiel zeigt eine `BuyButton`-Komponente, die Aktivitäten protokolliert, wenn jemand auf **Buy** klickt. Zunächst werden nur `logCustomEvent`, `logPurchase` und `getUser` zum Zeitpunkt des Klicks importiert. Dann wird ein Nutzerattribut aktualisiert, ein angepasstes Event protokolliert und ein Kauf protokolliert. Dieses Muster hilft Ihnen, die Initialisierung in `useBraze` zentralisiert zu halten, während Sie dennoch sinnvolle Aktionen aus jeder Client-Komponente heraus tracken können.

Wenn Sie Remix mit Vite verwenden und Package-Root-Importe zur Laufzeit fehlschlagen, nutzen Sie den bestehenden Vite-Workaround. Weitere Informationen finden Sie unter [Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite).

Eine vollständige Liste der verfügbaren Methoden finden Sie in der [Braze JavaScript-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

### Tealium iQ

Tealium iQ bietet eine einfache, schlüsselfertige Braze-Integration. Um die Integration zu konfigurieren, suchen Sie in der Tealium Tag-Management-Schnittstelle nach Braze und geben Sie den Web-SDK-API-Schlüssel von Ihrem Dashboard an.

Für weitere Informationen oder umfassende Unterstützung bei der Konfiguration von Tealium empfehlen wir Ihnen, unsere [Integrationsdokumentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium#about-tealium) zu konsultieren oder sich an Ihren Tealium-Account-Manager zu wenden.

### Vite {#vite}

Wenn Sie Vite verwenden und eine Warnung zu zirkulären Abhängigkeiten oder `Uncaught TypeError: Class extends value undefined is not a constructor or null` sehen, müssen Sie das Braze SDK möglicherweise von der [Abhängigkeitserkennung](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior) ausschließen:

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Andere Tag-Manager {#other-tag-managers}

Braze kann auch mit anderen Tag-Management-Lösungen kompatibel sein. Folgen Sie dazu unseren Integrationsanweisungen innerhalb eines angepassten HTML-Tags. Bitte wenden Sie sich an eine Braze-Vertretung, wenn Sie Unterstützung bei der Bewertung dieser Lösungen benötigen.