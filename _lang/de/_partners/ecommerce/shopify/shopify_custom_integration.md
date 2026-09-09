---
nav_title: Shopify angepasste Integration einrichten
article_title: Shopify angepasste Integration einrichten
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Verbindung zu einem Shopify Hydrogen Shop oder einem beliebigen Headless-Shopify-Shop herstellen, indem Sie eine angepasste Storefront verwenden."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 3
---

# Shopify angepasste Integration einrichten {#shopify-custom-integration-setup}

> Auf dieser Seite erfahren Sie, wie Sie Braze mit einem Shopify Hydrogen Shop oder einem beliebigen Headless-Shopify-Shop integrieren können, indem Sie eine angepasste Storefront verwenden.

Dieser Leitfaden verwendet das Hydrogen-Framework von Shopify als Beispiel. Sie können jedoch einen ähnlichen Ansatz verfolgen, wenn Ihre Marke Shopify für das Backend Ihres Shops mit einem „Headless“-Front-End-Setup verwendet.

Um Ihren Shopify Headless Shop mit Braze zu integrieren, müssen Sie diese beiden Ziele erreichen:

1. **Initialisieren und laden Sie das Braze Web SDK, um das Onsite-Tracking zu ermöglichen**<br><br> Fügen Sie manuell Code in Ihre Shopify-Website ein, um das Braze Onsite-Tracking zu aktivieren. Durch die Implementierung des Braze SDK in Ihrem Shopify Headless Shop können Sie Onsite-Aktivitäten nachverfolgen, einschließlich Sitzungen, anonymes Nutzer:innenverhalten, Aktionen vor dem Checkout und alle [angepassten Events]({{site.baseurl}}/user_guide/data/activation/events/custom_events) oder [angepassten Attribute]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes), die Sie zusammen mit Ihrem Entwicklungsteam einbeziehen möchten. Sie können auch alle Kanäle hinzufügen, die von den SDKs unterstützt werden, wie In-App-Nachrichten oder Content Cards.

{: start="2"}
2. **Installieren Sie die Braze Shopify-Integration**<br><br> Nachdem Sie Ihren Shopify-Shop mit Braze verbunden haben, erhalten Sie über Shopify-Webhooks Zugriff auf Kundendaten, Checkout-, Bestell- und Produktdaten.

{% alert important %}
Bevor Sie mit der Integration beginnen, vergewissern Sie sich, dass Sie die Checkout-Subdomain für Ihre Shopify-Storefront korrekt eingerichtet haben. Weitere Informationen finden Sie unter [Migration vom Online-Shop zu Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> Wenn diese Einrichtung nicht korrekt vorgenommen wird, kann Braze keine Shopify-Checkout-Webhooks verarbeiten. Es ist auch nicht möglich, die Integration in einer lokalen Entwicklungsumgebung zu testen, da dies von einer gemeinsamen Domain zwischen Ihrer Storefront und der Checkout-Seite abhängt.
{% endalert %}

Um diese Ziele zu erreichen, gehen Sie folgendermaßen vor:

## Braze Web SDK initialisieren und laden {#initialize-and-load-the-braze-web-sdk}

### Schritt 1: Website-App auswählen und SDK-Zugangsdaten kopieren {#step-1}

Bevor Sie Code zu Ihrer Hydrogen-Storefront hinzufügen, verbinden Sie Ihren Shopify-Shop und starten Sie das benutzerdefinierte Setup-Onboarding. Falls Sie Ihren Shop noch nicht verbunden haben, führen Sie zunächst [Ihren Shopify-Shop verbinden](#connect-your-shopify-store) durch, fahren Sie dann mit [Braze SDKs aktivieren](#enable-braze-sdks) fort und wählen Sie **Custom setup**.

Im benutzerdefinierten Setup-Flow fordert Braze Sie auf, die Website-App für Ihre Headless-Storefront auszuwählen:

1. Wählen Sie eine bestehende Website-App aus oder erstellen Sie eine neue. Sie können die App beliebig benennen, außer **Shopify** – diesen Namen reserviert Braze für den Standard-Shopify-Integrationspfad.
2. Braze zeigt den API-Schlüssel und die Basis-URL (Ihren SDK-Endpunkt) der ausgewählten App im Onboarding-Schritt an. Wählen Sie **Kopieren** für jeden Wert – Sie müssen nicht **Einstellungen** > **App-Einstellungen** öffnen.
3. Verwenden Sie den kopierten API-Schlüssel als `BRAZE_API_KEY` und den SDK-Endpunkt als `BRAZE_API_URL` in Ihren Shopify-Umgebungsvariablen ([Schritt 2](#step-2)).

Nachdem Sie den Shop verbunden haben, können Sie die ausgewählte Website-App unter **Einstellungen** > **App-Einstellungen** umbenennen. Sie können die App nicht löschen, solange sie mit Ihrer Shopify-Integration verbunden ist.

{% alert warning %}
Verwenden Sie den API-Schlüssel für die Website-App, die Sie beim Onboarding ausgewählt haben. Wenn Ihre Hydrogen-Umgebung einen anderen API-Schlüssel verwendet als den, der mit Ihrer Shopify-Integration verbunden ist, erstellt Braze möglicherweise doppelte Nutzer:innen und SDK-Methoden funktionieren unter Umständen nicht wie erwartet.
{% endalert %}

### Schritt 2: Subdomain und Umgebungsvariablen hinzufügen {#step-2}

1. Richten Sie Ihre Shopify-Subdomain ein, um [Traffic von Ihrem Onlineshop zu Hydrogen umzuleiten](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic).
2. Fügen Sie einen [Callback-URI](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) für die Anmeldung hinzu. (Der URI wird automatisch hinzugefügt, wenn die Domain hinzugefügt wird.)
3. Richten Sie Ihre [Shopify-Umgebungsvariablen](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable) ein:
  - Erstellen Sie zwei Umgebungsvariablen mit dem API-Schlüssel und dem SDK-Endpunkt, die Sie während des benutzerdefinierten Setup-Onboardings in [Schritt 1](#step-1) kopiert haben.
    - `BRAZE_API_KEY`
    - `BRAZE_API_URL`

### Schritt 3: Onsite-Tracking aktivieren {#step-3-enable-onsite-tracking}

Der erste Schritt besteht darin, das Braze Web SDK zu initialisieren. Wir empfehlen dazu die Installation unseres NPM-Pakets:

```java
npm install --save @braze/web-sdk@6.8.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
Die minimale unterstützte Braze Web SDK-Version ist 5.4.0. Für benutzerdefinierte Shopify-Integrationen (einschließlich Headless-Storefronts) erhalten Sie Benachrichtigungen, wenn neue SDK-Versionen verfügbar sind, aber Sie verwalten Upgrades selbst, indem Sie sowohl Ihren Storefront-Code als auch die SDK-Version in den Integrationseinstellungen aktualisieren.
{% endalert %}

Dann [fügen Sie diese Einstellung]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) als Top-Level-Schlüssel in Ihrer `vite.config.js`-Datei hinzu:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

Nach der Installation des NPM-Pakets müssen Sie das SDK innerhalb eines `useEffect`-Hooks in der `Layout`-Komponente initialisieren. Je nach Hydrogen-Version befindet sich diese Komponente entweder in der Datei `root.jsx` oder `layout.jsx`:

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

Die Werte `data.brazeApiKey` und `data.brazeApiUrl` müssen im Komponenten-Loader unter Verwendung der in [Schritt 2](#step-2) erstellten Umgebungsvariablen enthalten sein:

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
Content-Security-Policies (in der Regel in der Hydrogen-Datei `entry.server.jsx` definiert) können die Funktionalität von Braze-Skripten sowohl in lokalen als auch in Produktionsumgebungen beeinträchtigen. Wir empfehlen, Tests über Preview-Builds durchzuführen, die über Oxygen oder benutzerdefinierte Deployments an Shopify gesendet werden. Falls Probleme auftreten, müssen Sie Ihre CSP so konfigurieren, dass unser JavaScript ausgeführt werden kann.
{% endalert %}

### Schritt 4: Ein Shopify-Account-Login-Event hinzufügen {#step-4-add-a-shopify-account-login-event}

Verfolgen Sie, wann sich eine Käuferin oder ein Käufer in ihr bzw. sein Konto einloggt und die Nutzerinformationen mit Braze synchronisiert werden. Dazu gehört der Aufruf unserer `changeUser`-Methode, um Kund:innen mit einer externen Braze-ID zu identifizieren.

{% alert note %}
Derzeit gibt es keine Anleitung zur Unterstützung einer benutzerdefinierten externen Braze-ID. Falls Sie dies für Ihre Integration benötigen, wenden Sie sich an Ihren CSM.
{% endalert %}

Stellen Sie vor dem Start sicher, dass Sie die Callback-URIs für die Kundenanmeldung eingerichtet haben, damit sie innerhalb von Hydrogen funktionieren. Weitere Informationen finden Sie unter [Using the Customer Account API with Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Nachdem Sie die Callback-URIs eingerichtet haben, definieren Sie eine Funktion zum Aufrufen des Braze SDK. Erstellen Sie eine neue Datei (z. B. `Tracking.jsx`) und importieren Sie sie aus Ihren Komponenten:

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
2. Fügen Sie im selben `useEffect`-Hook, der das Braze SDK initialisiert, den Aufruf dieser Funktion hinzu:

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
3. Rufen Sie die E-Mail-Adresse und Telefonnummer der Kund:in in Ihrer Customer-API-GraphQL-Abfrage ab, die sich in der Datei `app/graphql/customer-account/CustomerDetailsQuery.js` befindet:

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
4. Laden Sie abschließend die Kundendaten in Ihrer Loader-Funktion:

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

### Schritt 5: Tracking für „Product Viewed“- und „Cart Updated“-Events hinzufügen {#step-5-add-tracking-for-product-viewed-and-cart-updated-events}

#### „Product Viewed“-Events

1. Fügen Sie diese Funktion zu Ihrer `Tracking.jsx`-Datei hinzu:

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
2. Um die obige Funktion aufzurufen, sobald eine Nutzerin oder ein Nutzer eine Produktseite besucht, fügen Sie einen `useEffect`-Hook zur Product-Komponente in der Datei `app/routes/products.$handle.jsx` hinzu:

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
3. Fügen Sie den Wert für „storefrontUrl“ hinzu (da er standardmäßig nicht im Komponenten-Loader enthalten ist):

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

#### „Cart Updated“-Events

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

1. Definieren Sie Funktionen zum Tracking des `cart_updated`-Events und zum Setzen des Warenkorb-Tokens:

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
2. Geben Sie das `cart`-Objekt aus der Fetcher-Aktion zurück, damit Braze auf dessen Eigenschaften zugreifen kann. Navigieren Sie dazu zu Ihrer Datei `app/routes/cart.jsx` und fügen Sie Folgendes zur `action`-Funktion hinzu:

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

Weitere Informationen zu Remix-Fetchern finden Sie unter [useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher).

{: start="3"}
3. Hydrogen-Shops definieren in der Regel eine `CartForm`-Komponente, die den Zustand des Warenkorb-Objekts verwaltet und beim Hinzufügen, Entfernen und Ändern der Artikelmenge verwendet wird. Fügen Sie einen weiteren `useEffect`-Hook in der `AddToCartButton`-Komponente hinzu, der die `trackCartUpdated`-Funktion aufruft, sobald sich der Fetcher-Zustand ändert (d. h. wenn der Warenkorb aktualisiert wird):

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
4. Verwenden Sie denselben `fetcherKey` für die Aktionen, die für das Aktualisieren eines bestehenden Produkts in Ihrem Warenkorb zuständig sind. Fügen Sie Folgendes zu den Komponenten `CartLineRemoveButton` und `CartLineUpdateButton` hinzu (standardmäßig in der Datei `app/components/CartLineItem.jsx`):

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

## Braze-Shopify-Integration installieren {#install-the-braze-shopify-integration}

### Schritt 1: Ihren Shopify-Shop verbinden {#connect-your-shopify-store}

Rufen Sie die Shopify-Partnerseite auf, um mit der Einrichtung zu beginnen. Wählen Sie zunächst **Begin Setup**, um die Braze-Anwendung aus dem Shopify App Store zu installieren. Folgen Sie den geführten Schritten, um den Installationsprozess abzuschließen.

![Seite zur Einrichtung der Shopify-Integration im Braze-Dashboard.]({% image_buster /assets/img/shopify/braze_shopify_integration_page.png %})

### Schritt 2: Braze SDKs aktivieren {#enable-braze-sdks}

Für Shopify Hydrogen oder Headless-Shops wählen Sie die Option **Custom setup**.

Die benutzerdefinierte Einrichtung enthält eine Website-App-Auswahl. Wählen Sie die App aus, die Ihren Storefront betreibt, oder erstellen Sie eine neue, und kopieren Sie dann den API-Schlüssel und den SDK-Endpunkt, die im Onboarding-Schritt angezeigt werden. Weitere Einzelheiten finden Sie unter [Schritt 1: Website-App auswählen und SDK-Zugangsdaten kopieren](#step-1).

Bevor Sie mit dem Onboarding-Prozess fortfahren, bestätigen Sie, dass Sie das Braze SDK mit diesen Zugangsdaten zu Ihrer Shopify-Website hinzugefügt haben.

![Einrichtungsschritt zur Aktivierung der Braze SDKs.]({% image_buster /assets/img/shopify/enable_braze_sdks_setup.png %})

### Schritt 3: Shopify-Daten tracken {#step-3-track-shopify-data}

Erweitern Sie Ihre Integration, indem Sie weitere Shopify-Events und -Attribute hinzufügen, die über Shopify-Webhooks bereitgestellt werden. Detaillierte Informationen zu den Daten, die durch diese Integration erfasst werden, finden Sie unter [Shopify-Daten-Features]({{site.baseurl}}/shopify_data_features).

![Einrichtungsschritt zum Tracken von Shopify-Daten.]({% image_buster /assets/img/shopify/track_shopify_data_setup.png %})

### Schritt 4: Historischer Backfill (optional) {#step-4-historical-backfill-optional}

Über die benutzerdefinierte Einrichtung können Sie optional denselben historischen Shopify-Datenladevorgang wie bei der [Standard-Integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#historical-backfill-setup) einbeziehen: Bestellevents der letzten 90 Tage und Nutzerprofile des letzten Jahres, jeweils zurückgerechnet vom Datum Ihres Integrationsabschlusses. Um diesen initialen Datenladevorgang einzubeziehen, aktivieren Sie das Kontrollkästchen für die Option des initialen Datenladevorgangs.

Wenn Sie den Backfill lieber später durchführen möchten, können Sie die initiale Einrichtung jetzt abschließen und zu einem späteren Zeitpunkt zu diesem Schritt zurückkehren.

![Bereich zur Einrichtung des historischen Daten-Backfills.]({% image_buster /assets/img/shopify/historical_backfill_setup.png %})

Die vollständige Liste der Daten im initialen Ladevorgang, das Verhalten der Umsatzberichte und die Überwachung der Synchronisierung finden Sie unter [Historischer Backfill]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill).

### Schritt 5: Benutzerdefiniertes Daten-Tracking einrichten (erweitert) {#step-5-custom-data-tracking-setup-advanced}

Mit den Braze SDKs können Sie angepasste Events oder angepasste Attribute tracken, die über die unterstützten Daten dieser Integration hinausgehen. Angepasste Events erfassen einzigartige Interaktionen in Ihrem Shop, wie zum Beispiel:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table aria-label="Schritt 5: Benutzerdefiniertes Daten-Tracking einrichten (erweitert)" style="width: 100%;">
  <caption>Schritt 5: Benutzerdefiniertes Daten-Tracking einrichten (erweitert)</caption>
  <thead>
    <tr>
      <th style="width: 50%;">Angepasste Events</th>
      <th style="width: 50%;">Angepasste Attribute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Verwendung eines benutzerdefinierten Rabattcodes</li>
          <li>Interaktion mit einer personalisierten Produktempfehlung</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Lieblingsmarken oder -produkte</li>
          <li>Bevorzugte Einkaufskategorien</li>
          <li>Mitgliedschafts- oder Kundenbindungsstatus</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

Das SDK muss auf dem Gerät der Nutzerin bzw. des Nutzers initialisiert sein (auf Aktivitäten lauschen), um Events oder angepasste Attribute zu protokollieren. Weitere Informationen zum Protokollieren benutzerdefinierter Daten finden Sie unter [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) und [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### Schritt 6: Nutzerverwaltung konfigurieren (optional) {#step-6}

Wählen Sie Ihren `external_id`-Typ aus dem Dropdown aus.

![Bereich „Abonnent:innen erfassen“.]({% image_buster /assets/img/shopify/external_id_standard.png %})

{% alert important %}
Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe Braze-ID kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die potenziellen Risiken für den Datenschutz und die Datensicherheit zu berücksichtigen.<br><br>

- **Erratbare Informationen:** E-Mail-Adressen sind leicht zu erraten und daher anfällig für Angriffe.
- **Missbrauchsrisiko:** Wenn böswillige Nutzer:innen ihren Webbrowser so manipulieren, dass die E-Mail-Adresse einer anderen Person als externe ID gesendet wird, könnten sie potenziell auf vertrauliche Nachrichten oder Kontoinformationen zugreifen.
{% endalert %}

Standardmäßig konvertiert Braze E-Mail-Adressen aus Shopify automatisch in Kleinbuchstaben, bevor sie als externe ID verwendet werden. Wenn Sie eine E-Mail-Adresse oder eine gehashte E-Mail-Adresse als externe ID verwenden, stellen Sie sicher, dass Ihre E-Mail-Adressen ebenfalls in Kleinbuchstaben konvertiert werden, bevor Sie sie als externe ID zuweisen oder bevor Sie sie aus anderen Datenquellen hashen. Dies hilft, Diskrepanzen bei externen IDs zu vermeiden und die Erstellung doppelter Nutzerprofile in Braze zu verhindern.

{% alert note %}
Die nächsten Schritte hängen von Ihrer Auswahl der externen ID ab:<br><br>
- **Wenn Sie einen benutzerdefinierten externen ID-Typ ausgewählt haben:** Führen Sie die Schritte 6.1–6.3 durch, um Ihre benutzerdefinierte externe-ID-Konfiguration einzurichten.
- **Wenn Sie Shopify-Kunden-ID, E-Mail oder gehashte E-Mail ausgewählt haben:** Überspringen Sie die Schritte 6.1–6.3 und fahren Sie direkt mit Schritt 6.4 fort.
{% endalert %}

#### Schritt 6.1: Das Metafeld `braze.external_id` erstellen {#step-61-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Nachdem das Metafeld erstellt wurde, befüllen Sie es für Ihre Kund:innen. Wir empfehlen die folgenden Ansätze:

- **Kund:innenerstellungs-Webhooks abhören:** Richten Sie einen Webhook ein, der auf [`customer/create`-Events](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) lauscht. So können Sie das Metafeld schreiben, wenn neue Kund:innen erstellt werden.
- **Bestehende Kund:innen nachträglich befüllen:** Verwenden Sie die [Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer), um das Metafeld für zuvor erstellte Kund:innen nachträglich zu befüllen.

#### Schritt 6.2: Einen Endpunkt zum Abrufen Ihrer externen ID erstellen {#step-62-create-an-endpoint-to-retrieve-your-external-id}

Sie müssen einen öffentlichen Endpunkt erstellen, den Braze aufrufen kann, um die externe ID abzurufen. Dadurch kann Braze die ID in Szenarien abrufen, in denen Shopify das Metafeld `braze.external_id` nicht direkt bereitstellen kann.

##### Endpunktspezifikationen {#endpoint-specifications}

**Methode:** GET

Braze sendet die folgenden Parameter an Ihren Endpunkt:

| Parameter | Obligatorisch | Datentyp | Beschreibung |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id | Ja | String | Die Shopify-Kunden-ID. |
| shopify_storefront | Ja | String | Der Storefront-Name für die Anfrage. Beispiel: `<storefront_name>.myshopify.com` |
| email_address | Nein | String | Die E-Mail-Adresse der angemeldeten Nutzerin bzw. des angemeldeten Nutzers. <br><br>Dieses Feld kann in bestimmten Webhook-Szenarien fehlen. Ihre Endpunktlogik sollte Null-Werte hier berücksichtigen (zum Beispiel die E-Mail-Adresse über die shopify_customer_id abrufen, wenn Ihre interne Logik dies erfordert). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Endpunktspezifikationen" }

##### Beispiel-Endpunkt {#example-endpoint}

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```


##### Erwartete Antwort {#expected-response}
Braze erwartet einen `200`-Statuscode, der die externe ID als JSON zurückgibt:
```json
{
  "external_id": "my_external_id"
}
```

##### Validierung {#validation}

Es ist entscheidend, zu validieren, dass die `shopify_customer_id` und die `email_address` (falls vorhanden) mit den Kundenwerten in Shopify übereinstimmen. Sie können die [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) oder die [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) verwenden, um diese Parameter zu validieren und das korrekte Metafeld `braze.external_id` abzurufen.

##### Fehlerverhalten und Zusammenführung {#failure-behavior-and-merging}
Jeder Statuscode außer `200` wird als Fehler betrachtet.

{% multi_lang_include partners/shopify/external_id_merge_implications.md %}

#### Schritt 6.3: Ihre externe ID eingeben {#step-63-input-your-external-id}

Wiederholen Sie [Schritt 6](#step-6) und geben Sie Ihre Endpunkt-URL ein, nachdem Sie den benutzerdefinierten externen ID-Typ als Ihren externen Braze-ID-Typ ausgewählt haben.

##### Hinweise {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

#### Schritt 6.4: E-Mail- oder SMS-Opt-ins aus Shopify erfassen (optional) {#step-64-collect-your-email-or-sms-opt-ins-from-shopify-optional}

Sie haben die Möglichkeit, Ihre E-Mail- oder SMS-Marketing-Opt-ins aus Shopify zu erfassen.

Wenn Sie die E-Mail- oder SMS-Kanäle nutzen, können Sie Ihre E-Mail- und SMS-Marketing-Opt-in-Status in Braze synchronisieren. Wenn Sie E-Mail-Marketing-Opt-ins aus Shopify synchronisieren, erstellt Braze automatisch eine E-Mail-Abo-Gruppe für alle Nutzer:innen, die mit diesem bestimmten Shop verknüpft sind. Sie müssen einen eindeutigen Namen für diese Abo-Gruppe erstellen.

![Bereich „Abonnent:innen erfassen“ mit der Option, E-Mail- oder SMS-Marketing-Opt-ins zu erfassen.]({% image_buster /assets/img/shopify/collect_email_subscribers.png %})

{% multi_lang_include partners/shopify/third_party_capture_form_note.md %}

### Schritt 7: Produkte synchronisieren (optional) {#step-7-sync-products-optional}

Sie können alle Produkte aus Ihrem Shopify-Shop in einen Braze-Katalog synchronisieren, um eine tiefere Messaging-Personalisierung zu ermöglichen. Automatische Aktualisierungen erfolgen nahezu in Echtzeit, sodass Ihr Katalog immer die neuesten Produktdetails widerspiegelt. Weitere Informationen finden Sie unter [Shopify-Produktsynchronisierung]({{site.baseurl}}/shopify_catalogs).

![Einrichtungsschritt zur Synchronisierung von Produktdaten mit Braze.]({% image_buster /assets/img/shopify/sync_product_data.png %})

### Schritt 8: Kanäle aktivieren {#step-8-activate-channels}

Um In-App Messages, Content Cards und Feature-Flags über die direkte Shopify-Integration zu aktivieren, fügen Sie jeden Kanal zu Ihrem SDK hinzu. Folgen Sie den für jeden Kanal bereitgestellten Dokumentationslinks:

- **In-App Messages:** Informationen zur Aktivierung von In-App Messages für Lead-Erfassungsformular-Anwendungsfälle finden Sie unter [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages).
- **Content Cards:** Informationen zur Aktivierung von Content Cards für Posteingangs- oder Website-Banner-Anwendungsfälle finden Sie unter [Content Cards]({{site.baseurl}}/developer_guide/content_cards).
- **Feature-Flags:** Informationen zur Aktivierung von Feature-Flags für Website-Experimentierungs-Anwendungsfälle finden Sie unter [Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags).

### Schritt 9: Einrichtung abschließen {#step-9-finish-setup}

Nachdem Sie alle Schritte durchlaufen haben, wählen Sie **Finish Setup**, um zur Partnerseite zurückzukehren. Aktivieren Sie dann das Braze-App-Embed in Ihrer Shopify-Administrationsseite, wie im angezeigten Banner angegeben.

![Banner mit dem Hinweis, das Braze-App-Embed in Shopify zu aktivieren, um die Einrichtung Ihrer Integration abzuschließen.]({% image_buster /assets/img/shopify/shopify_app_embed_banner.png %})

#### Beispielcode {#example-code}

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) ist eine Beispiel-Hydrogen-App, die den gesamten Code aus den vorherigen Schritten enthält.