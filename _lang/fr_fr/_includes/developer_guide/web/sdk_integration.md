## À propos du SDK Web de Braze {#about-the-web-braze-sdk}

Le SDK Web de Braze vous permet de collecter des données analytiques et d'afficher des messages in-app enrichis, des notifications push et des messages Content Cards à vos utilisateurs web. Pour en savoir plus, consultez la [documentation de référence JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Intégrer le SDK Web {#integrate-the-web-sdk}

Vous pouvez intégrer le SDK Web de Braze à l'aide des méthodes suivantes. Pour des options supplémentaires, consultez [autres méthodes d'intégration](#web_other-integration-methods).

- **Intégration basée sur le code :** Intégrez le SDK Web de Braze directement dans votre base de code à l'aide de votre gestionnaire de paquets préféré ou du CDN de Braze. Cela vous donne un contrôle total sur la manière dont le SDK est chargé et configuré.
- **Google Tag Manager :** Une solution sans code qui vous permet d'intégrer le SDK Web de Braze sans modifier le code de votre site. Pour en savoir plus, consultez [Google Tag Manager avec le SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager).

{% alert important %}
Nous recommandons d'utiliser la [méthode d'intégration NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Les avantages incluent le stockage local des bibliothèques du SDK sur votre site web, l'immunité contre les extensions de blocage de publicités et des temps de chargement plus rapides grâce à la prise en charge des bundlers.
{% endalert %}

{% tabs local %}
{% tab Intégration basée sur le code %}
### Étape 1 : Installer la bibliothèque Braze {#step-1-install-the-braze-library}

Vous pouvez installer la bibliothèque Braze à l'aide de l'une des méthodes suivantes. Toutefois, si votre site web utilise une `Content-Security-Policy`, consultez la section [Content Security Policy]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy) avant de continuer.

{% alert important %}
Bien que la plupart des bloqueurs de publicités ne bloquent pas le SDK Web de Braze, certains bloqueurs plus restrictifs sont connus pour causer des problèmes.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
Si votre site utilise les gestionnaires de paquets NPM ou Yarn, vous pouvez ajouter le [paquet NPM de Braze](https://www.npmjs.com/package/@braze/web-sdk) comme dépendance.

Les définitions Typescript sont incluses depuis la version 3.0.0. Pour les notes de mise à niveau de la version 2.x vers la version 3.x, consultez notre [journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Une fois installée, vous pouvez utiliser `import` ou `require` de la manière habituelle :

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Ajoutez le SDK Web de Braze directement à votre HTML en référençant notre script hébergé sur le CDN, qui charge la bibliothèque de manière asynchrone.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Le paramètre par défaut **Empêcher le suivi intersite** dans Safari peut empêcher l'affichage de certains types de messages in-app tels que les bannières et les Content Cards lorsque vous utilisez la méthode d'intégration CDN. Pour éviter ce problème, utilisez la méthode d'intégration NPM afin que Safari ne classe pas ces messages comme du trafic intersite et que vos utilisateurs web puissent les voir dans tous les navigateurs pris en charge.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Étape 2 : Initialiser le SDK {#step-2-initialize-the-sdk}

Une fois le SDK Web de Braze ajouté à votre site web, initialisez la bibliothèque avec la clé API et l'[URL de l'endpoint du SDK]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) disponibles dans **Paramètres** > **Paramètres de l'application** dans votre tableau de bord de Braze. Pour une liste complète des options pour `braze.initialize()`, ainsi que nos autres méthodes JavaScript, consultez la [documentation JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

{% alert note %}
**Les domaines personnalisés pour les requêtes du SDK Web ne sont pas pris en charge** : le `baseUrl` du SDK Web doit être un endpoint du SDK de Braze (par exemple, `sdk.iad-05.braze.com`). Braze ne prend pas en charge le routage du trafic du SDK Web via un domaine appartenant au client par le biais d'enregistrements CNAME. Si vous avez besoin que les requêtes du SDK Web proviennent de votre propre domaine, contactez le support Braze.
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
**Affichage des messages in-app** : pour afficher automatiquement les messages in-app lorsqu'ils sont déclenchés, vous devez appeler `braze.automaticallyShowInAppMessages()`. Sans cet appel, les messages in-app ne s'affichent pas automatiquement. Si vous souhaitez gérer l'affichage des messages manuellement, supprimez cet appel et utilisez `braze.subscribeToInAppMessage()` à la place. Pour en savoir plus, consultez [Désactiver les déclencheurs automatiques]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#disabling-automatic-triggers).
{% endalert %}

#### Résolution des problèmes de sessions manquantes pour les utilisateurs anonymes {#troubleshooting-missing-sessions-for-anonymous-users}

Si vous constatez un comportement de type « session manquante » ou si vous n'êtes pas en mesure de suivre la session des utilisateurs qui restent anonymes sur le web, assurez-vous que votre intégration appelle `braze.openSession()` lors de l'initialisation.

- **Scénario :** Les utilisateurs anonymes peuvent renvoyer un ID Braze, mais les données de session sont vides ou manquantes.
- **Cause :** L'implémentation n'appelle pas `braze.openSession()`.
- **Résolution :** Appelez toujours `braze.openSession()` après l'initialisation (et après `braze.changeUser()` si vous définissez un ID externe).

Pour en savoir plus, consultez [Étape 2 : Initialiser le SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk).

{% alert important %}
Les utilisateurs anonymes sur appareils mobiles ou web peuvent être comptabilisés dans vos [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users). Par conséquent, vous pouvez souhaiter charger ou initialiser le SDK de manière conditionnelle afin d'exclure ces utilisateurs de votre comptage de MAU.
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

Pour activer rapidement la journalisation, vous pouvez ajouter `?brazeLogging=true` comme paramètre à l'URL de votre site web. Vous pouvez également activer la journalisation [basique](#web_basic-logging) ou [personnalisée](#web_custom-logging). Pour un aperçu centralisé sur toutes les plateformes, consultez [Journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

#### Journalisation basique {#basic-logging}

{% tabs local %}
{% tab Avant l'initialisation %}
Utilisez `enableLogging` pour journaliser les messages de débogage basiques dans la console JavaScript avant l'initialisation du SDK.

```javascript
enableLogging: true
```

Votre méthode devrait ressembler à ce qui suit :

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab Après l'initialisation %}
Utilisez `braze.toggleLogging()` pour journaliser les messages de débogage basiques dans la console JavaScript après l'initialisation du SDK. Votre méthode devrait ressembler à ce qui suit :

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
Les journaux basiques sont visibles par tous les utilisateurs. Pensez à les désactiver ou à passer à [`setLogger`](#web_custom-logging) avant de déployer votre code en production.
{% endalert %}

#### Journalisation personnalisée {#custom-logging}

Utilisez `setLogger` pour journaliser des messages de débogage personnalisés dans la console JavaScript. Contrairement aux journaux basiques, ces journaux ne sont pas visibles par les utilisateurs.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Remplacez `STRING` par votre message sous la forme d'un paramètre de chaîne de caractères unique. Votre méthode devrait ressembler à ce qui suit :

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Mise à jour du SDK {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

Lorsque vous référencez le SDK Web de Braze depuis notre réseau de diffusion de contenu, par exemple `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (comme recommandé par nos instructions d'intégration par défaut), vos utilisateurs reçoivent automatiquement les mises à jour mineures (corrections de bugs et fonctionnalités rétrocompatibles, versions `a.a.a` à `a.a.z` dans cet exemple) lorsqu'ils actualisent votre site.

Cependant, lorsque nous publions des changements majeurs, nous vous demandons de mettre à jour manuellement le SDK Web de Braze afin de vous assurer que les changements non rétrocompatibles n'impactent pas votre intégration. De plus, si vous téléchargez notre SDK et l'hébergez vous-même, vous ne recevez aucune mise à jour de version automatiquement et devez effectuer la mise à jour manuellement pour bénéficier des dernières fonctionnalités et corrections de bugs.

Vous pouvez rester informé de nos dernières versions [en suivant notre flux de versions](https://github.com/braze-inc/braze-web-sdk/tags.atom) avec le lecteur RSS ou le service de votre choix, et consulter [notre journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) pour un historique complet des versions de notre SDK Web. Pour mettre à jour le SDK Web de Braze :

- Mettez à jour la version de la bibliothèque Braze en modifiant le numéro de version de `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`, ou dans les dépendances de votre gestionnaire de paquets.
- Si vous avez intégré les notifications push Web, mettez à jour le fichier du service de traitement sur votre site. Par défaut, celui-ci se trouve à l'emplacement `/service-worker.js` dans le répertoire racine de votre site, mais cet emplacement peut être personnalisé dans certaines intégrations. Vous devez accéder au répertoire racine pour héberger un fichier de service de traitement.

Vous devez mettre à jour ces deux fichiers de manière coordonnée pour garantir un fonctionnement correct.

## Autres méthodes d'intégration {#other-integration-methods}

### Pages mobiles accélérées (AMP) {#accelerated-mobile-pages-amp}
{% details Voir plus %}
#### Étape 1 : Inclure le script AMP web push {#step-1-include-amp-web-push-script}

Ajoutez la balise de script asynchrone suivante dans votre en-tête :

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Étape 2 : Ajouter les widgets d'abonnement {#step-2-add-subscription-widgets}

Ajoutez un widget dans le corps de votre HTML permettant aux utilisateurs de s'abonner et de se désabonner des notifications push.

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

Le composant AMP Web Push crée une fenêtre contextuelle pour gérer les abonnements push. Vous devez donc ajouter les fichiers d'aide suivants à votre projet pour activer cette fonctionnalité :

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Étape 4 : Créer un fichier de service de traitement {#step-4-create-a-service-worker-file}

Créez un fichier `service-worker.js` dans le répertoire racine de votre site web et ajoutez l'extrait de code suivant :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Étape 5 : Configurer l'élément HTML AMP web push {#step-5-configure-the-amp-web-push-html-element}

Ajoutez l'élément HTML `amp-web-push` suivant dans le corps de votre HTML. Gardez à l'esprit que vous devez ajouter votre [`apiKey` et `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) en tant que paramètres de requête à `service-worker-URL`.

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

#### Désactiver la prise en charge {#disable-support}

Si votre site utilise RequireJS ou un autre chargeur de modules AMD, mais que vous préférez charger le SDK Web de Braze via l'une des autres options de cette liste, vous pouvez charger une version de la bibliothèque qui n'inclut pas la prise en charge d'AMD. Cette version de la bibliothèque peut être chargée depuis l'emplacement CDN suivant :

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Chargeur de modules {#module-loader}

Si vous utilisez RequireJS ou d'autres chargeurs de modules AMD, nous vous recommandons d'héberger vous-même une copie de notre bibliothèque et de la référencer comme vous le feriez avec d'autres ressources :

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

Electron ne prend pas officiellement en charge les notifications push Web (voir : ce [ticket GitHub](https://github.com/electron/electron/issues/6697)). Il existe d'autres [solutions open source](https://github.com/MatthieuLemoine/electron-push-receiver) que vous pouvez essayer, mais qui n'ont pas été testées par Braze.

### Framework Jest {#jest}

Lorsque vous utilisez Jest, vous pouvez voir une erreur similaire à `SyntaxError: Unexpected token 'export'`. Pour résoudre ce problème, ajustez votre configuration dans `package.json` pour ignorer le SDK Braze :

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

Créez un hook réutilisable `useBraze` et appelez-le à proximité de la racine de votre application.

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

Appelez `useBraze` en haut du composant de votre route racine.

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

#### Journaliser des événements et mettre à jour les utilisateurs {#logging-events-and-updating-users}

Après que `useBraze` a initialisé le SDK à la racine de votre application, d'autres composants client peuvent appeler les méthodes Braze. Un schéma courant consiste à les appeler dans des actions utilisateur, telles que `onClick` ou `onSubmit`. Dans cet exemple, les méthodes du SDK sont chargées dans le gestionnaire de clic plutôt qu'en haut du fichier. Cela permet de garder le SDK Web hors du code serveur et de ne charger que ce dont cette action a besoin. Le commentaire `webpackExports` indique à webpack quelles méthodes inclure, ce qui maintient un bundle plus léger.

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

Cet exemple montre un composant `BuyButton` qui journalise l'activité lorsqu'un utilisateur clique sur **Buy**. Premièrement, il importe uniquement `logCustomEvent`, `logPurchase` et `getUser` au moment du clic. Ensuite, il met à jour un attribut utilisateur, journalise un événement personnalisé et journalise un achat. Ce schéma vous permet de centraliser l'initialisation dans `useBraze`, tout en suivant les actions significatives depuis n'importe quel composant client.

Si vous utilisez Remix avec Vite et que les imports depuis la racine du paquet échouent au moment de l'exécution, utilisez la solution de contournement Vite existante. Pour plus d'informations, consultez [Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite).

Pour une liste complète des méthodes disponibles, consultez la [documentation de référence JavaScript de Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

### Tealium iQ

Tealium iQ offre une intégration Braze clé en main. Pour configurer l'intégration, recherchez Braze dans l'interface de gestion des balises Tealium, puis fournissez la clé API du SDK Web depuis votre tableau de bord.

Pour plus de détails ou pour une assistance approfondie sur la configuration Tealium, consultez notre [documentation d'intégration]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium#about-tealium) ou contactez votre gestionnaire de compte Tealium.

### Vite {#vite}

Si vous utilisez Vite et que vous voyez un avertissement concernant des dépendances circulaires ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, vous devrez peut-être exclure le SDK Braze de sa [découverte de dépendances](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior) :

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Autres gestionnaires de balises {#other-tag-managers}

Braze peut également être compatible avec d'autres solutions de gestion de balises en suivant nos instructions d'intégration au sein d'une balise HTML personnalisée. Contactez un conseiller Braze si vous avez besoin d'aide pour évaluer ces solutions.