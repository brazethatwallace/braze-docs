---
nav_title: Configuration de l'intégration personnalisée de Shopify
article_title: Configuration de l'intégration personnalisée de Shopify
description: "Cet article de référence explique comment se connecter à une boutique Shopify Hydrogen ou à n'importe quelle boutique Shopify headless en utilisant une vitrine personnalisée."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 3
---

# Configuration de l'intégration personnalisée de Shopify {#shopify-custom-integration-setup}

> Cette page vous explique comment intégrer Braze à une boutique Shopify Hydrogen ou à n'importe quelle boutique Shopify headless en utilisant une vitrine personnalisée.

Ce guide utilise le framework Hydrogen de Shopify comme exemple. Cependant, vous pouvez suivre une approche similaire si votre marque utilise Shopify pour le backend de votre boutique avec une configuration front-end « headless ».

Pour intégrer votre boutique Shopify headless à Braze, vous devez remplir ces deux objectifs :

1. **Initialiser et charger le SDK Web de Braze pour permettre le suivi sur site**<br><br> Ajoutez manuellement du code dans votre site Shopify pour activer le suivi sur site de Braze. En implémentant le SDK de Braze sur votre boutique Shopify headless, vous pouvez suivre les activités sur site, notamment les sessions, le comportement des utilisateurs anonymes, les actions des acheteurs avant le passage en caisse, ainsi que tout [événement personnalisé]({{site.baseurl}}/user_guide/data/activation/events/custom_events) ou [attribut personnalisé]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) que vous choisissez d'inclure avec votre équipe de développement. Vous pouvez également ajouter tous les canaux pris en charge par les SDK, tels que les In-App Messages ou Content Cards.

{: start="2"}
2. **Installer l'intégration Braze pour Shopify**<br><br> Après avoir connecté votre boutique Shopify à Braze, vous aurez accès aux données des clients, des paiements, des commandes et des produits grâce aux webhooks de Shopify.

{% alert important %}
Avant de commencer votre intégration, vérifiez que vous avez correctement configuré le sous-domaine de paiement pour votre vitrine Shopify. Pour plus d'informations, consultez [Migrer de la boutique en ligne vers Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> Si cette configuration n'est pas effectuée correctement, Braze ne pourra pas traiter les webhooks de paiement de Shopify. Il ne sera pas non plus possible de tester l'intégration dans un environnement de développement local, car cela nécessite un domaine partagé entre votre vitrine et la page de paiement.
{% endalert %}

Pour atteindre ces objectifs, suivez les étapes suivantes :

## Initialiser et charger le SDK Web de Braze {#initialize-and-load-the-braze-web-sdk}

### Étape 1 : Sélectionner une application de site web et copier les identifiants du SDK {#step-1}

Avant d'ajouter du code à votre vitrine Hydrogen, connectez votre boutique Shopify et démarrez l'onboarding de configuration personnalisée. Si vous n'avez pas encore connecté votre boutique, suivez les instructions dans [Connecter votre boutique Shopify](#connect-your-shopify-store), puis continuez avec [Activer les SDK Braze](#enable-braze-sdks) et sélectionnez **Custom setup**.

Dans le flux de configuration personnalisée, Braze vous invite à sélectionner l'application de site web pour votre vitrine headless :

1. Sélectionnez une application de site web existante ou créez-en une nouvelle. Vous pouvez nommer l'application comme vous le souhaitez, sauf **Shopify**, nom que Braze réserve au parcours d'intégration Shopify standard.
2. Braze affiche la clé API et l'URL de base (votre endpoint SDK) de l'application sélectionnée dans l'étape d'onboarding. Sélectionnez **Copy** pour chaque valeur — vous n'avez pas besoin d'ouvrir **Settings** > **App Settings**.
3. Utilisez la clé API copiée comme `BRAZE_API_KEY` et l'endpoint SDK comme `BRAZE_API_URL` dans vos variables d'environnement Shopify ([Étape 2](#step-2)).

Après avoir connecté la boutique, vous pouvez renommer l'application de site web sélectionnée dans **Settings** > **App Settings**. Vous ne pouvez pas supprimer l'application tant qu'elle est connectée à votre intégration Shopify.

{% alert warning %}
Utilisez la clé API de l'application de site web que vous avez sélectionnée lors de l'onboarding. Si votre environnement Hydrogen utilise une clé API différente de celle connectée à votre intégration Shopify, Braze pourrait créer des utilisateurs en double et les méthodes du SDK pourraient ne pas fonctionner comme prévu.
{% endalert %}

### Étape 2 : Ajouter le sous-domaine et les variables d'environnement {#step-2}

1. Configurez votre sous-domaine Shopify pour [rediriger le trafic de votre boutique en ligne vers Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic).
2. Ajoutez un [URI de rappel](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) pour la connexion. (L'URI sera automatiquement ajouté lorsque le domaine sera ajouté.)
3. Configurez vos [variables d'environnement Shopify](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable) :
  - Créez deux variables d'environnement en utilisant la clé API et l'endpoint SDK que vous avez copiés lors de l'onboarding de configuration personnalisée à l'[Étape 1](#step-1).
    - `BRAZE_API_KEY`
    - `BRAZE_API_URL`

### Étape 3 : Activer le suivi sur site {#step-3-enable-onsite-tracking}

La première étape consiste à initialiser le SDK Web de Braze. Nous recommandons de le faire en installant notre package NPM :

```java
npm install --save @braze/web-sdk@6.8.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
La version minimale prise en charge du SDK Web de Braze est la 5.4.0. Pour les intégrations Shopify personnalisées (y compris les vitrines headless), vous recevez des notifications lorsque de nouvelles versions du SDK sont disponibles, mais vous gérez les mises à jour de votre côté en mettant à jour à la fois le code de votre vitrine et la version du SDK dans les paramètres d'intégration.
{% endalert %}

Ensuite, [incluez ce paramètre]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) comme clé de premier niveau dans votre fichier `vite.config.js` :

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

Après avoir installé le package NPM, vous devez initialiser le SDK dans un hook `useEffect` à l'intérieur du composant `Layout`. Selon votre version de Hydrogen, ce composant peut se trouver dans le fichier `root.jsx` ou `layout.jsx` :

```java
// Add these imports
import * as braze from "@braze/web-sdk";
import { useEffect } from 'react';

export function Layout({children}) {
  const nonce = useNonce();
  // @type {RootLoader}
  const data = useRouteLoaderData('root');

  // Add useEffect call to initialize Braze SDK
  useEffect(() => {
    if(!braze.isInitialized()) {
      braze.initialize(data.brazeApiKey, {
        baseUrl: data.brazeApiUrl,
      });
      braze.openSession()
    }
  }, [data])

  return (...);
}
```

Les valeurs `data.brazeApiKey` et `data.brazeApiUrl` doivent être incluses dans le loader du composant en utilisant les variables d'environnement créées à l'[Étape 2](#step-2) :

```java
export async function loader(args) {
  // Start fetching non-critical data without blocking time to first byte
  const deferredData = loadDeferredData(args);

  // Await the critical data required to render initial state of the page
  const criticalData = await loadCriticalData(args);

  const {storefront, env} = args.context;

  return {
    ...deferredData,
    ...criticalData,
    publicStoreDomain: env.PUBLIC_STORE_DOMAIN,
    // Add the two properties below to the returned value
    brazeApiKey: env.BRAZE_API_KEY,
    brazeApiUrl: env.BRAZE_API_URL,
    shop: getShopAnalytics({
      storefront,
      publicStorefrontId: env.PUBLIC_STOREFRONT_ID,
    }),
    consent: {
      checkoutDomain: env.PUBLIC_CHECKOUT_DOMAIN,
      storefrontAccessToken: env.PUBLIC_STOREFRONT_API_TOKEN,
      withPrivacyBanner: false,
      // Localize the privacy banner
      country: args.context.storefront.i18n.country,
      language: args.context.storefront.i18n.language,
    },
  };
}
```

{% alert note %}
Les politiques de sécurité du contenu (généralement situées dans le fichier Hydrogen `entry.server.jsx`) peuvent affecter le fonctionnement des scripts Braze dans les environnements locaux et de production. Nous vous suggérons de tester via des builds de prévisualisation envoyés à Shopify via Oxygen ou des déploiements personnalisés. Si vous rencontrez des problèmes, vous devrez configurer votre CSP pour permettre à notre JavaScript de fonctionner.
{% endalert %}

### Étape 4 : Ajouter un événement de connexion au compte Shopify {#step-4-add-a-shopify-account-login-event}

Suivez le moment où un acheteur se connecte à son compte et synchronise ses informations utilisateur avec Braze. Cela inclut l'appel à notre méthode `changeUser` pour identifier les clients avec un ID externe Braze.

{% alert note %}
Nous n'avons actuellement pas de guide pour prendre en charge un ID externe Braze personnalisé. Si vous en avez besoin pour votre intégration maintenant, contactez votre gestionnaire du succès des clients.
{% endalert %}

Avant de commencer, assurez-vous d'avoir configuré les URI de rappel pour que la connexion client fonctionne dans Hydrogen. Pour plus d'informations, consultez [Using the Customer Account API with Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Après avoir configuré les URI de rappel, définissez une fonction pour appeler le SDK Braze. Créez un nouveau fichier (tel que `Tracking.jsx`) et importez-le depuis vos composants :

```java
import * as braze from "@braze/web-sdk";

export function trackCustomerLogin(customerData, storefrontUrl) {
  const customerId = customerData.id.substring(customerData.id.lastIndexOf('/') + 1)
  const customerSessionKey = `ab.shopify.shopify_customer_${customerId}`;
  const alreadySetCustomerInfo = sessionStorage.getItem(customerSessionKey);

  if(!alreadySetCustomerInfo) {
    const user = braze.getUser()

    // To use Shopify customer ID as Braze External ID, use:
    // braze.changeUser(customerId)

    // To use Shopify customer email as Braze External ID, use:
      // braze.changeUser(customerData.emailAddress?.emailAddress)
        // To use hashing for email addresses, apply hashing before calling changeUser

    // To use your own custom ID as the Braze External ID, pass that value to the changeUser call.

    user.setFirstName(customerData.firstName);
    user.setLastName(customerData.lastName);
    if(customerData.emailAddress.emailAddress) {
      user.setEmail(customerData.emailAddress?.emailAddress);
    }

    if(customerData.phoneNumber?.phoneNumber) {
      user.setPhoneNumber(customerData.phoneNumber?.phoneNumber);
    }
    braze.logCustomEvent(
      "shopify_account_login",
      { source: storefrontUrl }
    )
    sessionStorage.setItem(customerSessionKey, customerId);
  }
}
```

{: start="2"}
2. Dans le même hook `useEffect` qui initialise le SDK Braze, ajoutez l'appel à cette fonction :

```java
import { trackCustomerLogin } from './Tracking';

export function Layout({children}) {
  const nonce = useNonce();
  // @type {RootLoader}
  const data = useRouteLoaderData('root');

  useEffect(() => {
    if(!braze.isInitialized()) {
      braze.initialize(data.brazeApiKey, {
        baseUrl: data.brazeApiUrl,
        enableLogging: true,
      });
      braze.openSession()
    }

    // Add call to trackCustomerLogin function
    data.isLoggedIn.then((isLoggedIn) => {
      if(isLoggedIn) {
        trackCustomerLogin(data.customerData, data.publicStoreDomain)
      }
    })

  }, [data])
```

{: start="3"}
3. Récupérez l'adresse e-mail et le numéro de téléphone du client dans votre requête GraphQL de l'API Customer, située dans le fichier `app/graphql/customer-account/CustomerDetailsQuery.js` :

```java
export const CUSTOMER_FRAGMENT = `#graphql
  fragment Customer on Customer {
    id
    firstName
    lastName
    emailAddress {
      emailAddress
    }
    phoneNumber {
      phoneNumber
    }
    defaultAddress {
      ...Address
    }
    addresses(first: 6) {
      nodes {
        ...Address
      }
    }
  }
  fragment Address on CustomerAddress {
    id
    formatted
    firstName
    lastName
    company
    address1
    address2
    territoryCode
    zoneCode
    city
    zip
    phoneNumber
  }
`;
```

{: start="4"}
4. Enfin, chargez les données client dans votre fonction loader :

```java
// Add import for GraphQL Query
import { CUSTOMER_DETAILS_QUERY } from './graphql/customer-account/CustomerDetailsQuery';

export async function loader(args) {
  // Start fetching non-critical data without blocking time to first byte
  const deferredData = loadDeferredData(args);

  // Await the critical data required to render initial state of the page
  const criticalData = await loadCriticalData(args);

  const {storefront, env} = args.context;

  // Add GraphQL call to Customer API
  const isLoggedIn = await deferredData.isLoggedIn;
  let customerData;
  if (isLoggedIn) {
    const { data, errors } = await args.context.customerAccount.query(
        CUSTOMER_DETAILS_QUERY,
    );
    customerData = data.customer
  } else {
    customerData = {}
  }

  return {
    ...deferredData,
    ...criticalData,
    publicStoreDomain: env.PUBLIC_STORE_DOMAIN,
    brazeApiKey: env.BRAZE_API_KEY,
    brazeApiUrl: env.BRAZE_API_URL,
    // Add the property below to the returned value
    customerData: customerData,
    shop: getShopAnalytics({
      storefront,
      publicStorefrontId: env.PUBLIC_STOREFRONT_ID,
    }),
    consent: {
      checkoutDomain: env.PUBLIC_CHECKOUT_DOMAIN,
      storefrontAccessToken: env.PUBLIC_STOREFRONT_API_TOKEN,
      withPrivacyBanner: false,
      // Localize the privacy banner
      country: args.context.storefront.i18n.country,
      language: args.context.storefront.i18n.language,
    },
  };
}
```

### Étape 5 : Ajouter le suivi des événements Product Viewed et Cart Updated {#step-5-add-tracking-for-product-viewed-and-cart-updated-events}

#### Événements Product Viewed {#product-viewed-events}

1. Ajoutez cette fonction à votre fichier `Tracking.jsx` :

```java
export function trackProductViewed(product, storefrontUrl) {
  const eventData = {
    product_id: product.id.substring(product.id.lastIndexOf('/') + 1),
    product_name: product.title,
    variant_id: product.selectedOrFirstAvailableVariant.id.substring(product.selectedOrFirstAvailableVariant.id.lastIndexOf('/') + 1),
    image_url: product.selectedOrFirstAvailableVariant.image?.url,
    product_url: `${storefrontUrl}/products/${product.handle}`,
    price: product.selectedOrFirstAvailableVariant.price.amount,
    currency: product.selectedOrFirstAvailableVariant.price.currencyCode,
    source: storefrontUrl,
    type: ["price_drop", "back_in_stock"],
    metadata: {
    sku: product.selectedOrFirstAvailableVariant.sku
  }

  }
  braze.logCustomEvent(
    "ecommerce.product_viewed",
    eventData
  )
}
```

{: start="2"}
2. Pour appeler la fonction précédente chaque fois qu'un utilisateur visite une page produit, ajoutez un hook `useEffect` au composant Product dans le fichier `app/routes/products.$handle.jsx` :

```java
import { trackProductViewed } from '~/tracking';
import { useEffect } from 'react';

export default function Product() {
  // @type {LoaderReturnData}
  // retrieve storefrontUrl to be passed into trackProductViewed
  const {product, storefrontUrl} = useLoaderData();

  // Add useEffect hook for tracking product_viewed event
  useEffect(() => {
    trackProductViewed(product, storefrontUrl)
  }, [])

  return (...)
}
```

{: start="3"}
3. Ajoutez la valeur pour « storefrontUrl » (car elle n'est pas dans le loader du composant par défaut) :

```java
async function loadCriticalData({context, params, request}) {
  const {handle} = params;
  const {storefront} = context;

  if (!handle) {
    throw new Error('Expected product handle to be defined');
  }

  const [{product}] = await Promise.alll([
    storefront.query(PRODUCT_QUERY, {
      variables: {handle, selectedOptions: getSelectedProductOptions(request)},
    }),
    // Add other queries here, so that they are loaded in parallel
  ]);

  if (!product?.id) {
    throw new Response(null, {status: 404});
  }

  return {
    product,
   // Add this property to the returned value
    storefrontUrl: context.env.PUBLIC_STORE_DOMAIN,
  };
}
```

#### Événements Cart Updated {#cart-updated-events}

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

1. Définissez des fonctions pour le suivi de l'événement `cart_updated` et la définition du jeton de panier :

```java
export function trackCartUpdated(cart, storefrontUrl) {
  const eventData = {
    cart_id: cart.id,
    total_value: cart.cost.totalAmount.amount,
    currency: cart.cost.totalAmount.currencyCode,

    products: cart.lines.nodes.map((line) => {
      return {
        product_id: line.merchandise.product.id.toString(),
        product_name: line.merchandise.product.title,
        variant_id: line.merchandise.id.toString(),
        image_url: line.merchandise.image.url,
        product_url: `${storefrontUrl}/products/${line.merchandise.product.handle}`,
        quantity: Number(line.quantity),
        price: Number(line.cost.totalAmount.amount / Number(line.quantity))
      }
    }),
    source: storefrontUrl,
    metadata: {},
  };

  braze.logCustomEvent(
    "ecommerce.cart_updated",
    eventData
  )
}

export function setCartToken(cart) {
  const cartId = cart.id.substring(cart.id.lastIndexOf('/') + 1)
  const cartToken = cartId.substring(0, cartId.indexOf("?key="));
  if (cartToken) {
    const cartSessionKey = `ab.shopify.shopify_cart_${cartToken}`;
    const alreadySetCartToken = sessionStorage.getItem(cartSessionKey);

    if (!alreadySetCartToken) {
      braze.getUser().addAlias("shopify_cart_token", `shopify_cart_${cartToken}`)
      braze.requestImmediateDataFlush();
      sessionStorage.setItem(cartSessionKey, cartToken);
    }
  }
}
```

{: start="2"}
2. Renvoyez l'objet `cart` depuis l'action du fetcher afin que Braze puisse accéder à ses propriétés en vous rendant dans votre fichier `app/routes/cart.jsx` et en ajoutant ce qui suit à la fonction `action` :

```java
export async function action({request, context}) {
  const {cart} = context;

  ...

  switch (action) {
    case CartForm.ACTIONS.LinesAdd:
      result = await cart.addLines(inputs.lines);
      break;
    ...
  }

  const cartId = result?.cart?.id;
  const headers = cartId ? cart.setCartId(result.cart.id) : new Headers();
  const {cart: cartResult, errors, warnings} = result;

  const redirectTo = formData.get('redirectTo') ?? null;
  if (typeof redirectTo === 'string') {
    status = 303;
    headers.set('Location', redirectTo);
  }

  return data(
    {
      cart: cartResult,
      // Add these two properties to the returned value
      updatedCart: await cart.get(),
      storefrontUrl: context.env.PUBLIC_STORE_DOMAIN,
      errors,
      warnings,
      analytics: {
        cartId,
      },
    },
    {status, headers},
  );
}
```

Pour plus d'informations sur les fetchers Remix, consultez [useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher).

{: start="3"}
3. Les boutiques Hydrogen définissent généralement un composant `CartForm` qui gère l'état de l'objet panier, utilisé lors de l'ajout, la suppression et la modification de la quantité d'articles dans un panier. Ajoutez un autre hook `useEffect` dans le composant `AddToCartButton` qui appellera la fonction `trackCartUpdated` chaque fois que l'état du fetcher du formulaire change (chaque fois que le panier de l'utilisateur est mis à jour) :

```java
// Add imports
import { trackCartUpdated, setCartToken } from '~/tracking';
import { useEffect } from 'react';
import { useFetcher } from '@remix-run/react';

export function AddToCartButton({
  analytics,
  children,
  disabled,
  lines,
  onClick,
}) {

  // Define a new Fetcher to be used for tracking cart updates
  const fetcher = useFetcher({ key: "cart-fetcher" });

  // Add useEffect hook for tracking cart_updated event and setting cart token alias
  useEffect(() => {
    if(fetcher.state === "idle" && fetcher.data) {
      trackCartUpdated(fetcher.data.updatedCart, fetcher.data.storefrontUrl)
      setCartToken(fetcher.data.updatedCart);
    }
  }, [fetcher.state, fetcher.data])

  // Add the fetcherKey prop to the CartForm component
  return (
    <CartForm route="/cart" inputs={{lines}} fetcherKey="cart-fetcher" action={CartForm.ACTIONS.LinesAdd}>
      {(fetcher) => (
        <>
          <input
            name="analytics"
            type="hidden"
            value={JSON.stringify(analytics)}
          />
          <button
            type="submit"
            onClick={onClick}
            disabled={disabled ?? fetcher.state !== 'idle'}
          >
            {children}
          </button>
        </>
      )}
    </CartForm>
  );
}
```

{: start="4"}
4. Utilisez le même `fetcherKey` pour les actions responsables de la mise à jour d'un produit existant dans votre panier. Ajoutez ce qui suit aux composants `CartLineRemoveButton` et `CartLineUpdateButton` (situés par défaut dans le fichier `app/components/CartLineItem.jsx`) :

```java
function CartLineRemoveButton({lineIds, disabled}) {
  // Add the fetcherKey prop to the CartForm component
  return (
    <CartForm
      fetcherKey="cart-fetcher"
      route="/cart"
      action={CartForm.ACTIONS.LinesRemove}
      inputs={{lineIds}}
    >
      <button disabled={disabled} type="submit">
        Remove
      </button>
    </CartForm>
  );
}

function CartLineUpdateButton({children, lines}) {
  // Add the fetcherKey prop to the CartForm component
  return (
    <CartForm
      route="/cart"
      fetcherKey="cart-fetcher"
      action={CartForm.ACTIONS.LinesUpdate}
      inputs={{lines}}
    >
      {children}
    </CartForm>
  );
}
```

## Installer l'intégration Braze Shopify {#install-the-braze-shopify-integration}

### Étape 1 : Connecter votre boutique Shopify {#connect-your-shopify-store}

Accédez à la page partenaire Shopify pour commencer la configuration. Commencez par sélectionner **Commencer la configuration** pour installer l'application Braze depuis le Shopify App Store. Suivez les étapes guidées pour terminer le processus d'installation.

![Page de configuration de l'intégration Shopify sur le tableau de bord de Braze.]({% image_buster /assets/img/shopify/braze_shopify_integration_page.png %})

### Étape 2 : Activer les SDK Braze {#enable-braze-sdks}

Pour les boutiques Shopify Hydrogen ou headless, sélectionnez l'option **Configuration personnalisée**.

La configuration personnalisée comprend un sélecteur d'application web. Sélectionnez ou créez l'application qui alimente votre vitrine, puis copiez la clé API et l'endpoint SDK affichés dans l'étape d'onboarding. Pour plus de détails, consultez [Étape 1 : Sélectionner une application web et copier les identifiants SDK](#step-1).

Avant de poursuivre le processus d'onboarding, confirmez que vous avez ajouté le SDK Braze à votre site Shopify en utilisant ces identifiants.

![Étape de configuration pour activer les SDK Braze.]({% image_buster /assets/img/shopify/enable_braze_sdks_setup.png %})

### Étape 3 : Suivre les données Shopify {#step-3-track-shopify-data}

Enrichissez votre intégration en ajoutant davantage d'événements et d'attributs Shopify, qui seront alimentés par les webhooks Shopify. Pour des informations détaillées sur les données suivies via cette intégration, consultez [Fonctionnalités de données Shopify]({{site.baseurl}}/shopify_data_features).

![Étape de configuration pour suivre les données Shopify.]({% image_buster /assets/img/shopify/track_shopify_data_setup.png %})

### Étape 4 : Remplissage historique (facultatif) {#step-4-historical-backfill-optional}

Via la configuration personnalisée, vous pouvez optionnellement inclure le même chargement de données historiques Shopify que l'[intégration standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#historical-backfill-setup) : les événements de commande des 90 derniers jours et les profils utilisateur de l'année écoulée, chacun comptabilisé à partir de la date à laquelle vous finalisez votre intégration. Pour inclure ce chargement initial de données, cochez la case correspondante.

Si vous préférez effectuer le remplissage ultérieurement, vous pouvez terminer la configuration initiale maintenant et revenir à cette étape plus tard.

![Section pour configurer le remplissage historique des données.]({% image_buster /assets/img/shopify/historical_backfill_setup.png %})

Pour la liste complète des données du chargement initial, le comportement de reporting des revenus et le suivi de la synchronisation, consultez [Remplissage historique]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill).

### Étape 5 : Configuration du suivi de données personnalisées (avancé) {#step-5-custom-data-tracking-setup-advanced}

Avec les SDK Braze, vous pouvez suivre des événements personnalisés ou des attributs personnalisés qui vont au-delà des données prises en charge par cette intégration. Les événements personnalisés capturent des interactions uniques dans votre boutique, tels que :

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table aria-label="Étape 5 : Configuration du suivi de données personnalisées (avancé)" style="width: 100%;">
  <caption>Étape 5 : Configuration du suivi de données personnalisées (avancé)</caption>
  <thead>
    <tr>
      <th style="width: 50%;">Événements personnalisés</th>
      <th style="width: 50%;">Attributs personnalisés</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Utilisation d'un code de réduction personnalisé</li>
          <li>Interaction avec une recommandation produit personnalisée</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marques ou produits favoris</li>
          <li>Catégories d'achat préférées</li>
          <li>Statut d'adhésion ou de fidélité</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Le SDK doit être initialisé (à l'écoute de l'activité) sur l'appareil de l'utilisateur pour enregistrer des événements ou des attributs personnalisés. Pour en savoir plus sur l'enregistrement de données personnalisées, consultez [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) et [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### Étape 6 : Configurer la gestion des utilisateurs (facultatif) {#step-6}

Sélectionnez votre type d'`external_id` dans le menu déroulant.

![Section « Collecter les abonnés ».]({% image_buster /assets/img/shopify/external_id_standard.png %})

{% alert important %}
L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut simplifier la gestion des identités entre vos sources de données. Cependant, il est important de prendre en compte les risques potentiels pour la confidentialité des utilisateurs et la sécurité des données.<br><br>

- **Informations devinables :** Les adresses e-mail sont facilement devinables, ce qui les rend vulnérables aux attaques.
- **Risque d'exploitation :** Si un utilisateur malveillant modifie son navigateur web pour envoyer l'adresse e-mail de quelqu'un d'autre comme ID externe, il pourrait potentiellement accéder à des messages sensibles ou à des informations de compte.
{% endalert %}

Par défaut, Braze convertit automatiquement les e-mails provenant de Shopify en minuscules avant de les utiliser comme ID externe. Si vous utilisez l'e-mail ou l'e-mail haché comme ID externe, vérifiez que vos adresses e-mail sont également converties en minuscules avant de les attribuer comme ID externe ou avant de les hacher à partir d'autres sources de données. Cela permet d'éviter les divergences d'ID externes et la création de profils utilisateur en double dans Braze.

{% alert note %}
Les étapes suivantes dépendent de votre sélection d'ID externe :<br><br>
- **Si vous avez sélectionné un type d'ID externe personnalisé :** Complétez les étapes 6.1 à 6.3 pour configurer votre ID externe personnalisé.
- **Si vous avez sélectionné l'ID client Shopify, l'e-mail ou l'e-mail haché :** Ignorez les étapes 6.1 à 6.3 et passez directement à l'étape 6.4.
{% endalert %}

#### Étape 6.1 : Créer le métachamp `braze.external_id` {#step-61-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Une fois le métachamp créé, remplissez-le pour vos clients. Nous recommandons les approches suivantes :

- **Écouter les webhooks de création de clients :** Configurez un webhook pour écouter les [événements `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Cela vous permet d'écrire le métachamp lorsqu'un nouveau client est créé.
- **Remplir rétroactivement les clients existants :** Utilisez l'[Admin API](https://shopify.dev/docs/api/admin-graphql) ou la [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) pour remplir rétroactivement le métachamp pour les clients précédemment créés.

#### Étape 6.2 : Créer un endpoint pour récupérer votre ID externe {#step-62-create-an-endpoint-to-retrieve-your-external-id}

Vous devez créer un endpoint public que Braze peut appeler pour récupérer l'ID externe. Cela permet à Braze de récupérer l'ID dans les scénarios où Shopify ne peut pas fournir directement le métachamp `braze.external_id`.

##### Spécifications de l'endpoint {#endpoint-specifications}

**Méthode :** GET

Braze envoie les paramètres suivants à votre endpoint :

| Paramètre            | Obligatoire | Type de données | Description                                                      |
|----------------------|-------------|-----------------|------------------------------------------------------------------|
| shopify_customer_id  | Oui         | String          | L'ID client Shopify.                                             |
| shopify_storefront   | Oui         | String          | Le nom de la vitrine pour la requête. Ex : `<storefront_name>.myshopify.com` |
| email_address        | Non         | String          | L'adresse e-mail de l'utilisateur connecté. <br><br>Ce champ peut être absent dans certains scénarios de webhook. La logique de votre endpoint doit prendre en compte les valeurs nulles ici (par exemple, récupérer l'e-mail en utilisant le shopify_customer_id si votre logique interne l'exige). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Spécifications de l'endpoint" }

##### Exemple d'endpoint {#example-endpoint}

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```


##### Réponse attendue {#expected-response}
Braze attend un code de statut `200` renvoyant l'ID externe en JSON :
```json
{
  "external_id": "my_external_id"
}
```

##### Validation

Il est essentiel de valider que le `shopify_customer_id` et l'`email_address` (si présente) correspondent aux valeurs du client dans Shopify. Vous pouvez utiliser la [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) ou la [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) pour valider ces paramètres et récupérer le bon métachamp `braze.external_id`.

##### Comportement en cas d'échec et fusion {#failure-behavior-and-merging}
Tout code de statut autre que `200` est considéré comme un échec.

{% multi_lang_include partners/shopify/external_id_merge_implications.md %}

#### Étape 6.3 : Saisir votre ID externe {#step-63-input-your-external-id}

Répétez l'[étape 6](#step-6), puis saisissez l'URL de votre endpoint après avoir sélectionné l'ID externe personnalisé comme type d'ID externe Braze.

##### Considérations {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

#### Étape 6.4 : Collecter les consentements e-mail ou SMS depuis Shopify (facultatif) {#step-64-collect-your-email-or-sms-opt-ins-from-shopify-optional}

Vous avez la possibilité de collecter les consentements marketing par e-mail ou SMS depuis Shopify.

Si vous utilisez les canaux e-mail ou SMS, vous pouvez synchroniser les états de consentement marketing e-mail et SMS dans Braze. Si vous synchronisez les consentements marketing par e-mail depuis Shopify, Braze créera automatiquement un groupe d'abonnement e-mail pour tous les utilisateurs associés à cette boutique spécifique. Vous devez créer un nom unique pour ce groupe d'abonnement.

![Section « Collecter les abonnés » avec l'option de collecter les consentements marketing par e-mail ou SMS.]({% image_buster /assets/img/shopify/collect_email_subscribers.png %})

{% multi_lang_include partners/shopify/third_party_capture_form_note.md %}

### Étape 7 : Synchroniser les produits (facultatif) {#step-7-sync-products-optional}

Vous pouvez synchroniser tous les produits de votre boutique Shopify vers un catalogue Braze pour une personnalisation approfondie de vos messages. Les mises à jour automatiques s'effectuent en quasi temps réel afin que votre catalogue reflète toujours les derniers détails des produits. Pour en savoir plus, consultez [Synchronisation de produits Shopify]({{site.baseurl}}/shopify_catalogs).

![Étape de configuration pour synchroniser les données produits vers Braze.]({% image_buster /assets/img/shopify/sync_product_data.png %})

### Étape 8 : Activer les canaux {#step-8-activate-channels}

Pour activer les In-App Messages, les Content Cards et les Feature Flags via l'intégration directe Shopify, ajoutez chaque canal à votre SDK. Suivez les liens de documentation fournis pour chaque canal :

- **In-App Messages :** Pour activer les In-App Messages dans les cas d'usage de formulaires de capture de prospects, consultez [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages).
- **Content Cards :** Pour activer les Content Cards dans les cas d'usage de boîte de réception ou de bannières sur le site, consultez [Content Cards]({{site.baseurl}}/developer_guide/content_cards).
- **Feature Flags :** Pour activer les Feature Flags dans les cas d'usage d'expérimentation sur le site, consultez [Feature Flags]({{site.baseurl}}/developer_guide/feature_flags).

### Étape 9 : Finaliser la configuration {#step-9-finish-setup}

Après avoir complété toutes les étapes, sélectionnez **Terminer la configuration** pour revenir à la page partenaire. Ensuite, activez l'intégration de l'application Braze dans votre page d'administration Shopify, comme indiqué par la bannière affichée.

![Bannière indiquant d'activer l'intégration de l'application Braze dans Shopify pour finaliser la configuration de votre intégration.]({% image_buster /assets/img/shopify/shopify_app_embed_banner.png %})

#### Exemple de code {#example-code}

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) est un exemple d'application Hydrogen contenant tout le code abordé dans les étapes précédentes.