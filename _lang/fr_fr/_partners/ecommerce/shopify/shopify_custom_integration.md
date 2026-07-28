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

### Étape 1 : Créer une application web Braze {#step-1}

Dans Braze, accédez à **Paramètres** > **Paramètres des applications**, puis sélectionnez **Ajouter une application**. Saisissez « Shopify » comme nom d'application.

{% alert warning %}
La boutique doit être nommée « Shopify », sinon l'intégration risque de ne pas fonctionner correctement.
{% endalert %}

### Étape 2 : Ajouter un sous-domaine et des variables d'environnement {#step-2}

1. Configurez votre sous-domaine Shopify pour [rediriger le trafic de votre boutique en ligne vers Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic).
2. Ajoutez un [URI de rappel](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) pour la connexion. (L'URI sera automatiquement ajouté lors de l'ajout du domaine.)
3. Configurez vos [variables d'environnement Shopify](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable) :
  - Créez deux variables d'environnement en utilisant les valeurs de l'application web que vous avez créée à l'[étape 1](#step-1).
    - `BRAZE_API_KEY`
    - `BRAZE_API_URL`

### Étape 3 : Activer le suivi sur site {#step-3-enable-onsite-tracking}

La première étape consiste à initialiser le SDK Web de Braze. Nous vous recommandons de le faire en installant notre package NPM :

```java
npm install --save @braze/web-sdk@6.8.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
La version du SDK Web de Braze doit être 5.4.0 ou ultérieure.
{% endalert %}

Ensuite, [incluez ce paramètre]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) en tant que clé de premier niveau dans votre fichier `vite.config.js` :

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

Les valeurs `data.brazeApiKey` et `data.brazeApiUrl` doivent être incluses dans le loader du composant à l'aide des variables d'environnement créées à l'[étape 2](#step-2) :

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
Les politiques de sécurité du contenu (généralement situées dans le fichier Hydrogen `entry.server.jsx`) peuvent affecter le fonctionnement des scripts Braze, tant dans les environnements locaux que de production. Nous vous suggérons de tester via des builds de prévisualisation envoyés à Shopify via Oxygen ou des déploiements personnalisés. Si vous rencontrez des problèmes, vous devrez configurer votre CSP pour permettre à notre JavaScript de fonctionner.
{% endalert %}

### Étape 4 : Ajouter un événement de connexion au compte Shopify {#step-4-add-a-shopify-account-login-event}

Suivez le moment où un acheteur se connecte à son compte et synchronise ses informations utilisateur avec Braze. Cela inclut l'appel à notre méthode `changeUser` pour identifier les clients avec un ID externe Braze.

{% alert note %}
Nous ne disposons pas actuellement de recommandations pour la prise en charge d'un ID externe Braze personnalisé. Si vous en avez besoin pour votre intégration, contactez votre CSM.
{% endalert %}

Avant de commencer, assurez-vous d'avoir configuré les URI de rappel pour que la connexion client fonctionne dans Hydrogen. Pour plus d'informations, consultez [Utilisation de l'API de compte client avec Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Après avoir configuré les URI de rappel, définissez une fonction pour appeler le SDK de Braze. Créez un nouveau fichier (tel que `Tracking.jsx`) et importez-le depuis vos composants :

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
2. Dans le même hook `useEffect` qui initialise le SDK de Braze, ajoutez l'appel à cette fonction :

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
3. Récupérez l'adresse e-mail et le numéro de téléphone du client dans votre requête GraphQL de l'API Client, située dans le fichier `app/graphql/customer-account/CustomerDetailsQuery.js` :

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

1. Définissez les fonctions pour suivre l'événement `cart_updated` et définir le jeton du panier :

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
2. Renvoyez l'objet `cart` depuis l'action du fetcher afin que Braze puisse accéder à ses propriétés. Pour cela, ouvrez votre fichier `app/routes/cart.jsx` et ajoutez ce qui suit à la fonction `action` :

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
3. Les boutiques Hydrogen définissent généralement un composant `CartForm` qui gère l'état de l'objet panier, utilisé lors de l'ajout, de la suppression et de la modification de la quantité d'articles dans un panier. Ajoutez un autre hook `useEffect` dans le composant `AddToCartButton` qui appellera la fonction `trackCartUpdated` chaque fois que l'état du fetcher du formulaire change (c'est-à-dire chaque fois que le panier de l'utilisateur est mis à jour) :

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
4. Utilisez le même `fetcherKey` pour les actions responsables de la mise à jour d'un produit existant dans votre panier. Ajoutez les éléments suivants aux composants `CartLineRemoveButton` et `CartLineUpdateButton` (situés par défaut dans le fichier `app/components/CartLineItem.jsx`) :

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

## Installer l'intégration Braze pour Shopify {#install-the-braze-shopify-integration}

### Étape 1 : Connecter votre boutique Shopify {#step-1-connect-your-shopify-store}

Rendez-vous sur la page partenaire de Shopify pour commencer votre configuration. Tout d'abord, sélectionnez **Begin Setup** pour installer l'application Braze depuis l'App Store de Shopify. Suivez les étapes guidées pour terminer le processus d'installation.

![Page de configuration de l'intégration Shopify sur le tableau de bord de Braze.]({% image_buster /assets/img/shopify/braze_shopify_integration_page.png %})

### Étape 2 : Activer les SDK de Braze {#step-2-enable-braze-sdks}

Pour les boutiques Shopify Hydrogen ou headless, sélectionnez l'option **Custom setup**.

Avant de poursuivre le processus d'onboarding, vérifiez que vous avez activé le SDK de Braze sur votre site Shopify.

![Étape de configuration pour activer les SDK de Braze.]({% image_buster /assets/img/shopify/enable_braze_sdks_setup.png %})

### Étape 3 : Suivre les données Shopify {#step-3-track-shopify-data}

Enrichissez votre intégration en ajoutant davantage d'événements et d'attributs Shopify, alimentés par les webhooks de Shopify. Pour des informations détaillées sur les données suivies via cette intégration, consultez [Fonctionnalités des données Shopify]({{site.baseurl}}/shopify_data_features).

![Étape de configuration pour le suivi des données Shopify.]({% image_buster /assets/img/shopify/track_shopify_data_setup.png %})

### Étape 4 : Remplissage historique (facultatif) {#step-4-historical-backfill-optional}

Grâce à la configuration personnalisée, vous pouvez optionnellement inclure le même chargement de données historiques Shopify que l'[intégration standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#historical-backfill-setup) : les événements de commande des 90 derniers jours et les profils utilisateurs de l'année écoulée, chacun comptabilisé à partir de la date à laquelle vous finalisez votre intégration. Pour inclure ce chargement initial de données, cochez la case correspondante.

Si vous préférez effectuer le remplissage plus tard, vous pouvez terminer la configuration initiale maintenant et revenir à cette étape ultérieurement.

![Section pour configurer le remplissage des données historiques.]({% image_buster /assets/img/shopify/historical_backfill_setup.png %})

Pour la liste complète des données du chargement initial, le comportement du reporting des revenus et le suivi de la synchronisation, consultez [Remplissage historique]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill).

### Étape 5 : Configuration personnalisée du suivi des données (avancée) {#step-5-custom-data-tracking-setup-advanced}

Avec les SDK de Braze, vous pouvez suivre des événements personnalisés ou des attributs personnalisés qui vont au-delà des données prises en charge par cette intégration. Les événements personnalisés capturent les interactions uniques dans votre boutique, comme :

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table aria-label="Étape 5 : Configuration personnalisée du suivi des données (avancée)" style="width: 100%;">
  <caption>Étape 5 : Configuration personnalisée du suivi des données (avancée)</caption>
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
L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut simplifier la gestion des identités dans l'ensemble de vos sources de données. Toutefois, il est important de prendre en compte les risques potentiels pour la confidentialité des utilisateurs et la sécurité des données.<br><br>

- **Informations devinables :** Les adresses e-mail sont facilement devinables, ce qui les rend vulnérables aux attaques.
- **Risque d'exploitation :** Si un utilisateur malveillant modifie son navigateur web pour envoyer l'adresse e-mail d'une autre personne comme ID externe, il pourrait potentiellement accéder à des messages sensibles ou à des informations de compte.
{% endalert %}

Par défaut, Braze convertit automatiquement les e-mails provenant de Shopify en minuscules avant de les utiliser comme ID externe. Si vous utilisez l'e-mail ou l'e-mail haché comme ID externe, vérifiez que vos adresses e-mail sont également converties en minuscules avant de les attribuer comme ID externe ou avant de les hacher depuis d'autres sources de données. Cela permet d'éviter les divergences dans les ID externes et la création de profils utilisateurs en double dans Braze.

{% alert note %}
Les étapes suivantes dépendent de votre sélection d'ID externe :<br><br>
- **Si vous avez sélectionné un type d'ID externe personnalisé :** Effectuez les étapes 6.1 à 6.3 pour configurer votre ID externe personnalisé.
- **Si vous avez sélectionné l'ID client Shopify, l'e-mail ou l'e-mail haché :** Passez directement à l'étape 6.4 en ignorant les étapes 6.1 à 6.3.
{% endalert %}

#### Étape 6.1 : Créer le métafield `braze.external_id` {#step-61-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Une fois le métafield créé, renseignez-le pour vos clients. Nous recommandons les approches suivantes :

- **Écouter les webhooks de création de clients :** Configurez un webhook pour écouter les [événements `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Cela vous permet d'écrire le métafield lors de la création d'un nouveau client.
- **Remplir les clients existants :** Utilisez l'[API Admin](https://shopify.dev/docs/api/admin-graphql) ou l'[API Client](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) pour remplir le métafield des clients précédemment créés.

#### Étape 6.2 : Créer un endpoint pour récupérer votre ID externe {#step-62-create-an-endpoint-to-retrieve-your-external-id}

Vous devez créer un endpoint public que Braze peut appeler pour récupérer l'ID externe. Cela permet à Braze de récupérer l'ID dans les scénarios où Shopify ne peut pas fournir directement le métafield `braze.external_id`.

##### Spécifications de l'endpoint {#endpoint-specifications}

**Méthode :** GET

Braze envoie les paramètres suivants à votre endpoint :

| Paramètre            | Requis | Type de données | Description                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | Oui      | Chaîne de caractères    | L'ID du client Shopify.                                         |
| shopify_storefront   | Oui      | Chaîne de caractères    | Le nom de la vitrine pour la requête. Ex : `<storefront_name>.myshopify.com` |
| email_address        | Non       | Chaîne de caractères    | L'adresse e-mail de l'utilisateur connecté. <br><br>Ce champ peut être absent dans certains scénarios de webhook. La logique de votre endpoint doit gérer les valeurs nulles (par exemple, récupérer l'e-mail via shopify_customer_id si votre logique interne l'exige). |
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

Il est essentiel de valider que `shopify_customer_id` et `email_address` (le cas échéant) correspondent aux valeurs du client dans Shopify. Vous pouvez utiliser l'[API Admin de Shopify](https://shopify.dev/docs/api/admin-graphql) ou l'[API Client](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) pour valider ces paramètres et récupérer le métafield `braze.external_id` correct.

##### Comportement en cas d'échec et fusion {#failure-behavior-and-merging}
Tout code de statut autre que `200` est considéré comme un échec.

{% multi_lang_include partners/shopify/external_id_merge_implications.md %}

#### Étape 6.3 : Saisir votre ID externe {#step-63-input-your-external-id}

Répétez l'[étape 6](#step-6) et saisissez l'URL de votre endpoint après avoir sélectionné l'ID externe personnalisé comme type d'ID externe Braze.

##### Considérations {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

#### Étape 6.4 : Collecter vos abonnements e-mail ou SMS depuis Shopify (facultatif) {#step-64-collect-your-email-or-sms-opt-ins-from-shopify-optional}

Vous avez la possibilité de collecter vos abonnements marketing par e-mail ou par SMS depuis Shopify.

Si vous utilisez les canaux e-mail ou SMS, vous pouvez synchroniser vos états d'abonnement marketing e-mail et SMS dans Braze. Si vous synchronisez les abonnements marketing par e-mail depuis Shopify, Braze créera automatiquement un groupe d'abonnement e-mail pour tous les utilisateurs associés à cette boutique spécifique. Vous devez créer un nom unique pour ce groupe d'abonnement.

![Section « Collecter les abonnés » avec option de collecte des abonnements marketing par e-mail ou SMS.]({% image_buster /assets/img/shopify/collect_email_subscribers.png %})

{% multi_lang_include partners/shopify/third_party_capture_form_note.md %}

### Étape 7 : Synchroniser les produits (facultatif) {#step-7-sync-products-optional}

Vous pouvez synchroniser tous les produits de votre boutique Shopify vers un catalogue Braze pour une personnalisation plus poussée des messages. Les mises à jour automatiques s'effectuent quasiment en temps réel, de sorte que votre catalogue reflète toujours les derniers détails des produits. Pour en savoir plus, consultez [Synchronisation des produits Shopify]({{site.baseurl}}/shopify_catalogs).

![Étape de configuration pour synchroniser les données produit avec Braze.]({% image_buster /assets/img/shopify/sync_product_data.png %})

### Étape 8 : Activer les canaux {#step-8-activate-channels}

Pour activer les In-App Messages, Content Cards et les Feature Flags via l'intégration directe de Shopify, ajoutez chaque canal à votre SDK. Suivez les liens de documentation fournis pour chaque canal :

- **In-App Messages :** Pour activer les In-App Messages dans les cas d'usage de formulaires de capture de prospects, consultez [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages).
- **Content Cards :** Pour activer Content Cards dans les cas d'usage de boîte de réception ou de bannières de site web, consultez [Content Cards]({{site.baseurl}}/developer_guide/content_cards).
- **Feature Flags :** Pour activer les Feature Flags dans les cas d'usage d'expérimentation sur site, consultez [Feature Flags]({{site.baseurl}}/developer_guide/feature_flags).

### Étape 9 : Terminer la configuration {#step-9-finish-setup}

Une fois toutes les étapes terminées, sélectionnez **Finish Setup** pour revenir à la page partenaire. Ensuite, activez l'intégration de l'application Braze dans votre page d'administration Shopify, comme indiqué par la bannière qui s'affiche.

![Bannière indiquant d'activer l'intégration de l'application Braze dans Shopify pour terminer la configuration de votre intégration.]({% image_buster /assets/img/shopify/shopify_app_embed_banner.png %})

#### Exemple de code {#example-code}

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) est un exemple d'application Hydrogen contenant tout le code présenté dans les étapes précédentes.