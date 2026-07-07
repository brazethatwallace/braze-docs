## À propos du SDK Web Braze {#about-the-web-braze-sdk}

Le SDK Web Braze vous permet de collecter des données analytiques et d'afficher des messages in-app enrichis, des notifications push et des messages Content Cards à vos utilisateurs Web. Pour plus d'informations, consultez la [documentation de référence JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Intégrer le SDK Web {#integrate-the-web-sdk}

Vous pouvez intégrer le SDK Web Braze en utilisant les méthodes suivantes. Pour des options supplémentaires, consultez les [autres méthodes d'intégration](#web_other-integration-methods).

- **Intégration basée sur le code :** Intégrez le SDK Web Braze directement dans votre base de code à l'aide de votre gestionnaire de paquets préféré ou du réseau de diffusion de contenu Braze. Cela vous permet de contrôler entièrement le chargement et la configuration du SDK.
- **Google Tag Manager :** Une solution sans code qui vous permet d'intégrer le SDK Web Braze sans modifier le code de votre site. Pour plus d'informations, consultez [Google Tag Manager avec le SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/).

{% alert important %}
Nous recommandons d'utiliser la [méthode d'intégration NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Les avantages comprennent le stockage local des bibliothèques SDK sur votre site web, l'immunité contre les extensions de blocage des publicités et la contribution à des temps de chargement plus rapides dans le cadre de la prise en charge des bundlers.
{% endalert %}

{% tabs local %}
{% tab code-based integration %}
### Étape 1 : Installer la bibliothèque Braze {#step-1-install-the-braze-library}

Vous pouvez installer la bibliothèque Braze en utilisant l'une des méthodes suivantes. Toutefois, si votre site web utilise un `Content-Security-Policy`, consultez la [politique de sécurité du contenu]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/) avant de poursuivre.

{% alert important %}
Bien que la plupart des bloqueurs de publicités ne bloquent pas le SDK Web Braze, certains bloqueurs plus restrictifs sont connus pour causer des problèmes.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
Si votre site utilise les gestionnaires de paquets NPM ou Yarn, vous pouvez ajouter le [paquet NPM de Braze](https://www.npmjs.com/package/@braze/web-sdk) comme dépendance.

Les définitions TypeScript sont désormais incluses à partir de la version v3.0.0. Pour les notes sur la mise à jour de 2.x vers 3.x, consultez notre [journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Une fois installé, vous pouvez `import` ou `require` la bibliothèque de la manière habituelle :

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Ajoutez le SDK Web Braze directement à votre code HTML en faisant référence à notre script hébergé par le réseau de diffusion de contenu, qui charge la bibliothèque de manière asynchrone.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Le paramètre par défaut **Empêcher le suivi intersites** dans Safari peut empêcher l'affichage de certains types de messages in-app, tels que les bannières et les Content Cards, lorsque vous utilisez la méthode d'intégration par réseau de diffusion de contenu. Pour éviter ce problème, utilisez la méthode d'intégration NPM afin que Safari ne classe pas ces messages comme du trafic intersite et que vos utilisateurs web puissent les voir dans tous les navigateurs pris en charge.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Étape 2 : Initialiser le SDK {#step-2-initialize-the-sdk}

Une fois le SDK Web Braze ajouté à votre site web, initialisez la bibliothèque à l'aide de la clé API et de l'[URL de l'endpoint SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) disponibles dans **Paramètres** > **Paramètres des applications** dans votre tableau de bord de Braze. Pour obtenir la liste complète des options de `braze.initialize()`, ainsi que nos autres méthodes JavaScript, consultez la [documentation JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

{% alert note %}
**Les domaines personnalisés pour les requêtes du SDK Web ne sont pas pris en charge** : Le `baseUrl` du SDK Web doit être un endpoint du SDK Braze (par exemple, `sdk.iad-05.braze.com`). Braze ne prend pas en charge le routage du trafic du SDK Web via un domaine appartenant au client à l'aide d'enregistrements CNAME. Si vous avez besoin que les requêtes du SDK Web proviennent de votre propre domaine, contactez l'assistance Braze.
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
**Affichage des messages in-app** : Pour afficher automatiquement les messages in-app lorsqu'ils sont déclenchés, vous devez appeler `braze.automaticallyShowInAppMessages()`. Sans cet appel, les messages in-app ne s'affichent pas automatiquement. Si vous souhaitez gérer manuellement l'affichage des messages, supprimez cet appel et utilisez `braze.subscribeToInAppMessage()` à la place. Pour plus d'informations, consultez la section [Réception/distribution de messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/delivery/).
{% endalert %}

#### Résolution des problèmes de sessions manquantes pour les utilisateurs anonymes {#troubleshooting-missing-sessions-for-anonymous-users}

Si vous constatez un comportement de « session manquante » ou si vous n'êtes pas en mesure de suivre la session des utilisateurs anonymes sur le web, assurez-vous que votre intégration appelle `braze.openSession()` lors de l'initialisation.

- **Scénario :** Les utilisateurs anonymes peuvent renvoyer un ID Braze, mais les données de session sont vides ou manquantes.
- **Cause :** L'implémentation n'appelle pas `braze.openSession()`.
- **Résolution :** Appelez toujours `braze.openSession()` après l'initialisation (et après `braze.changeUser()` si vous définissez un ID externe).

Pour plus d'informations, consultez l'[étape 2 : Initialiser le SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk).

{% alert important %}
Les utilisateurs anonymes sur des appareils mobiles ou web peuvent être comptabilisés dans votre [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). Par conséquent, vous pouvez charger ou initialiser conditionnellement le SDK pour exclure ces utilisateurs de votre décompte de MAU.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Filtrage du trafic des robots {#bot-filtering}

Le nombre de MAU peut inclure un pourcentage d'utilisateurs robots, ce qui gonfle votre nombre d'utilisateurs actifs par mois. Bien que le SDK Web Braze intègre une détection de certains robots d'indexation courants (tels que les robots des moteurs de recherche et les robots de prévisualisation des réseaux sociaux), il est particulièrement important de rester proactif en mettant en place des solutions robustes pour détecter les robots, car les mises à jour du SDK ne permettent pas à elles seules de détecter systématiquement tous les nouveaux robots.

### Limites de la détection des robots côté SDK {#limitations-of-sdk-side-bot-detection}

Le SDK Web comprend une détection de base des robots fondée sur l'agent utilisateur, qui filtre les robots d'indexation connus. Cependant, cette approche présente certaines limites :

- **De nouveaux robots apparaissent constamment** : Les entreprises spécialisées dans l'intelligence artificielle et d'autres acteurs développent régulièrement de nouveaux robots qui peuvent se dissimuler afin d'échapper à la détection.
- **Usurpation de l'agent utilisateur** : Les robots sophistiqués peuvent imiter les agents utilisateurs légitimes des navigateurs.
- **Robots personnalisés** : Les utilisateurs non techniciens peuvent désormais créer facilement des robots à l'aide de grands modèles de langage (LLM), rendant le comportement des robots imprévisible.

### Mise en œuvre du filtrage des robots {#implementing-bot-filtering}

{% alert important %}
Les solutions présentées ci-dessous sont des suggestions générales. Adaptez la logique de filtrage des robots à votre environnement unique et à vos modèles de trafic spécifiques.
{% endalert %}

La solution la plus robuste consiste à mettre en œuvre votre propre logique de filtrage des robots avant d'initialiser le SDK Braze. Les approches courantes comprennent :

#### Exiger une interaction de l'utilisateur {#require-user-interaction}

Envisagez de retarder l'initialisation du SDK jusqu'à ce qu'un utilisateur effectue une interaction significative, telle que l'acceptation d'une bannière de consentement aux cookies, le défilement ou un clic. Cette approche est souvent plus facile à mettre en œuvre et peut s'avérer très efficace pour filtrer le trafic des robots.

{% alert important %}
Retarder l'initialisation du SDK jusqu'à l'interaction de l'utilisateur peut également entraîner le non-affichage des bannières et des Content Cards jusqu'à ce que cette interaction ait lieu.
{% endalert %}

#### Détection personnalisée des robots {#custom-bot-detection}

Mettez en place une détection personnalisée en fonction des modèles de trafic spécifiques de vos robots, par exemple :

- Analyse des chaînes de caractères des agents utilisateurs pour identifier les modèles que vous avez détectés dans votre trafic
- Vérification des indicateurs de navigateur sans interface graphique
- Utilisation de services tiers de détection des robots
- Surveillance des signaux comportementaux spécifiques à votre site

**Exemple d'initialisation conditionnelle :**

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

### Bonnes pratiques {#best-practices}

- Analysez régulièrement vos données MAU et les tendances de trafic web afin d'identifier tout nouveau comportement de robot.
- Effectuez des tests approfondis pour vous assurer que votre filtrage des robots n'empêche pas le suivi des utilisateurs légitimes.
- Mettez à jour votre logique de filtrage en fonction des modèles de trafic des robots que vous observez dans votre environnement.

## Configurations optionnelles {#optional-configurations}

### Journalisation {#logging}

Pour activer rapidement la journalisation, vous pouvez ajouter `?brazeLogging=true` comme paramètre à l'URL de votre site web. Vous pouvez également activer la journalisation [de base](#web_basic-logging) ou [personnalisée](#web_custom-logging). Pour un aperçu centralisé sur toutes les plateformes, consultez la section [Journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/).

#### Journalisation de base {#basic-logging}

{% tabs local %}
{% tab before initialization %}
Utilisez `enableLogging` pour enregistrer les messages de débogage de base dans la console JavaScript avant l'initialisation du SDK.

```javascript
enableLogging: true
```

Votre méthode doit être similaire à la suivante :

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab after initialization %}
Utilisez `braze.toggleLogging()` pour enregistrer les messages de débogage de base dans la console JavaScript après l'initialisation du SDK. Votre méthode doit être similaire à la suivante :

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
Les journaux de base sont visibles par tous les utilisateurs. Envisagez de les désactiver ou de passer à [`setLogger`](#web_custom-logging) avant de mettre votre code en production.
{% endalert %}

#### Journalisation personnalisée {#custom-logging}

Utilisez `setLogger` pour enregistrer des messages de débogage personnalisés dans la console JavaScript. Contrairement aux journaux de base, ces journaux ne sont pas visibles par les utilisateurs.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Remplacez `STRING` par votre message sous la forme d'un paramètre de chaîne de caractères unique. Votre méthode doit être similaire à la suivante :

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Mise à niveau du SDK {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

Lorsque vous faites référence au SDK Web Braze à partir de notre réseau de diffusion de contenu, par exemple `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (comme recommandé par nos instructions d'intégration par défaut), vos utilisateurs reçoivent automatiquement les mises à jour mineures (corrections de bogues et fonctionnalités rétrocompatibles, versions `a.a.a` à `a.a.z` dans les exemples ci-dessus) lorsqu'ils actualisent votre site.

Cependant, lorsque nous publions des modifications majeures, nous vous demandons de mettre à jour manuellement le SDK Web Braze afin de garantir que les changements majeurs n'affectent pas votre intégration. De plus, si vous téléchargez notre SDK et l'hébergez vous-même, vous ne recevrez aucune mise à jour automatique et devrez effectuer la mise à niveau manuellement pour bénéficier des dernières fonctionnalités et corrections de bogues.

Vous pouvez vous tenir au courant de notre dernière version [en suivant notre flux de publication](https://github.com/braze-inc/braze-web-sdk/tags.atom) avec le lecteur RSS ou le service de votre choix, et consulter [notre journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) pour un compte-rendu complet de l'historique des versions de notre SDK Web. Pour mettre à niveau le SDK Web Braze :

- Mettez à jour la version de la bibliothèque Braze en modifiant le numéro de version de `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ou dans les dépendances de votre gestionnaire de paquets.
- Si vous avez intégré les notifications push web, mettez à jour le fichier du service de traitement sur votre site. Par défaut, celui-ci se trouve à `/service-worker.js` dans le répertoire racine de votre site, mais l'emplacement peut être personnalisé dans certaines intégrations. Vous devez accéder au répertoire racine pour héberger un fichier de service de traitement.

Vous devez mettre à jour ces deux fichiers de manière coordonnée afin d'assurer un fonctionnement correct.

## Autres méthodes d'intégration {#other-integration-methods}

### Pages mobiles accélérées (AMP) {#accelerated-mobile-pages-amp}
{% details Voir plus %}
#### Étape 1 : Inclure le script de notification push web AMP {#step-1-include-amp-web-push-script}

Ajoutez la balise de script asynchrone suivante à votre en-tête :

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Étape 2 : Ajouter des widgets d'abonnement {#step-2-add-subscription-widgets}

Ajoutez un widget au corps de votre code HTML qui permet aux utilisateurs de s'abonner et de se désabonner des notifications push.

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

#### Étape 3 : Ajouter `helper-iframe` et `permission-dialog` {#step-3-add-helper-iframe-and-permission-dialog}

Le composant AMP Web Push génère une fenêtre contextuelle pour gérer les abonnements push. Il est donc nécessaire d'ajouter les fichiers d'aide suivants à votre projet pour activer cette fonctionnalité :

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Étape 4 : Créer un fichier de service de traitement {#step-4-create-a-service-worker-file}

Créez un fichier `service-worker.js` dans le répertoire racine de votre site web et ajoutez-y l'extrait de code suivant :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Étape 5 : Configurer l'élément HTML de notification push web AMP {#step-5-configure-the-amp-web-push-html-element}

Ajoutez l'élément HTML `amp-web-push` suivant au corps de votre page HTML. Notez que vous devez ajouter vos paramètres de requête [`apiKey` et `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) à `service-worker-URL`.

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

### Définition de module asynchrone (AMD) {#asynchronous-module-definition-amd}

#### Désactiver la prise en charge {#disable-support}

Si votre site utilise RequireJS ou un autre chargeur de modules AMD, mais que vous préférez charger le SDK Web Braze via l'une des autres options de cette liste, vous pouvez charger une version de la bibliothèque qui n'inclut pas la prise en charge AMD. Cette version de la bibliothèque peut être chargée depuis l'emplacement suivant du réseau de diffusion de contenu :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Chargeur de modules {#module-loader}

Si vous utilisez RequireJS ou d'autres chargeurs de modules AMD, nous vous recommandons d'auto-héberger une copie de notre bibliothèque et de la référencer comme vous le feriez avec d'autres ressources :

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

Electron ne prend pas officiellement en charge les notifications push web (voir ce [problème GitHub](https://github.com/electron/electron/issues/6697)). Il existe d'autres [solutions de contournement open source](https://github.com/MatthieuLemoine/electron-push-receiver) que vous pouvez essayer, mais qui n'ont pas été testées par Braze.

### Framework Jest {#jest}

Lorsque vous utilisez Jest, vous pouvez rencontrer une erreur similaire à `SyntaxError: Unexpected token 'export'`. Pour la corriger, ajustez votre configuration dans `package.json` pour ignorer le SDK Braze :

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### Frameworks SSR {#ssr}

Le SDK Web s'exécute dans un environnement de navigateur. Dans les frameworks SSR, initialisez Braze dans un composant côté client uniquement afin que votre serveur n'exécute jamais le code du SDK.

#### Import dynamique indépendant du framework {#framework-agnostic-dynamic-import}

Si votre framework n'est pas répertorié dans cette section, vous pouvez importer dynamiquement Braze depuis un hook de cycle de vie côté client uniquement.

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

Si vous utilisez webpack, vous pouvez importer dynamiquement uniquement les exports spécifiques du SDK.

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

#### Hook partagé pour Next.js et Remix {#shared-hook-for-nextjs-and-remix}

Créez un hook réutilisable `useBraze` et appelez-le à la racine de votre application.

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

Appelez `useBraze` dans un composant client qui encapsule votre application.

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

Appelez `useBraze` en haut de votre composant d'application personnalisé.

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

Appelez `useBraze` en haut de votre composant de route racine.

Pour les exemples de validation Remix en local, exécutez `PORT=4013 npm run dev`.

```tsx
// app/root.tsx
import { Outlet } from "@remix-run/react";
import { useBraze } from "./hooks/useBraze";

export default function App() {
  useBraze();

  return <Outlet />;
}
```

#### Journalisation des événements et mise à jour des utilisateurs {#logging-events-and-updating-users}

Une fois que `useBraze` a initialisé le SDK à la racine de votre application, d'autres composants côté client peuvent appeler les méthodes Braze. Un modèle courant consiste à les appeler dans des actions utilisateur, telles que `onClick` ou `onSubmit`. Dans l'exemple, les méthodes du SDK sont chargées dans le gestionnaire de clic plutôt qu'en haut du fichier. Cela permet de garder le SDK Web hors du code serveur et de ne charger que ce dont l'action a besoin. Le commentaire `webpackExports` indique à webpack quelles méthodes inclure, ce qui réduit la taille de votre bundle.

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

Cet exemple montre un composant `BuyButton` qui enregistre l'activité lorsqu'un utilisateur clique sur **Acheter**. Il commence par importer uniquement `logCustomEvent`, `logPurchase` et `getUser` au moment du clic. Ensuite, il met à jour un attribut utilisateur, enregistre un événement personnalisé et enregistre un achat. Ce modèle vous permet de centraliser l'initialisation dans `useBraze`, tout en suivant les actions significatives depuis n'importe quel composant côté client.

Si vous utilisez Remix avec Vite et que les imports depuis la racine du paquet échouent à l'exécution, utilisez la solution de contournement Vite existante. Pour plus d'informations, consultez [Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite).

Pour une liste complète des méthodes disponibles, consultez la [documentation de référence JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

### Tealium iQ

Tealium iQ propose une intégration de base clé en main de Braze. Pour configurer l'intégration, recherchez Braze dans l'interface Tealium Tag Management et fournissez la clé API du SDK Web à partir de votre tableau de bord.

Pour plus de détails ou pour obtenir une assistance approfondie concernant la configuration de Tealium, consultez notre [documentation sur l'intégration]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou contactez votre gestionnaire de compte Tealium.

### Vite {#vite}

Si vous utilisez Vite et voyez un avertissement concernant des dépendances circulaires ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, vous devrez peut-être exclure le SDK Braze de sa [découverte de dépendances](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior) :

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Autres gestionnaires de balises {#other-tag-managers}

Braze peut également être compatible avec d'autres solutions de gestion des balises en suivant nos instructions d'intégration au sein d'une balise HTML personnalisée. Contactez un conseiller Braze si vous avez besoin d'aide pour évaluer ces solutions.