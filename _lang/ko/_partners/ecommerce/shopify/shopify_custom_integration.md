---
nav_title: Shopify 커스텀 통합 설정
article_title: Shopify 커스텀 통합 설정
description: "이 참조 문서에서는 커스텀 스토어프론트를 사용하여 Shopify Hydrogen 스토어 또는 헤드리스 Shopify 스토어에 연결하는 방법을 다룹니다."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 3
---

# Shopify 커스텀 통합 설정 {#shopify-custom-integration-setup}

> 이 페이지에서는 커스텀 스토어프론트를 사용하여 Braze를 Shopify Hydrogen 스토어 또는 헤드리스 Shopify 스토어와 통합하는 방법을 안내합니다.

이 가이드에서는 Shopify의 Hydrogen 프레임워크를 예시로 사용합니다. 그러나 브랜드에서 Shopify를 스토어 백엔드로 사용하면서 "헤드리스" 프론트엔드 설정을 사용하는 경우에도 유사한 접근 방식을 따를 수 있습니다.

Shopify 헤드리스 스토어를 Braze와 통합하려면 다음 두 가지 목표를 완료해야 합니다:

1. **Braze Web SDK를 초기화하고 로드하여 온사이트 추적 활성화**<br><br> Shopify 웹사이트에 코드를 수동으로 추가하여 Braze 온사이트 추적을 활성화합니다. Shopify 헤드리스 스토어에 Braze SDK를 구현하면 세션, 익명 사용자 행동, 결제 전 쇼핑객 동작, 그리고 개발팀과 함께 포함하기로 선택한 [커스텀 이벤트]({{site.baseurl}}/user_guide/data/activation/events/custom_events) 또는 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)을 포함한 온사이트 활동을 추적할 수 있습니다. In-App Messages나 Content Cards와 같이 SDK에서 지원하는 채널도 추가할 수 있습니다.

{: start="2"}
2. **Braze Shopify 통합 설치**<br><br> Shopify 스토어를 Braze에 연결하면 Shopify 웹훅을 통해 고객, 결제, 주문 및 제품 데이터에 접근할 수 있습니다.

{% alert important %}
통합을 시작하기 전에 Shopify 스토어프론트의 결제 하위 도메인이 올바르게 설정되었는지 확인하세요. 자세한 내용은 [온라인 스토어에서 Hydrogen으로 마이그레이션](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate)을 참조하세요.<br><br> 이 설정이 올바르게 되어 있지 않으면 Braze가 Shopify 결제 웹훅을 처리할 수 없습니다. 또한 스토어프론트와 결제 페이지 간의 공유 도메인에 의존하기 때문에 로컬 개발 환경에서 통합을 테스트하는 것도 불가능합니다.
{% endalert %}

이러한 목표를 완료하려면 다음 단계를 따르세요:

## Braze 웹 SDK 초기화 및 로드 {#initialize-and-load-the-braze-web-sdk}

### 1단계: 웹사이트 앱 선택 및 SDK 자격 증명 복사 {#step-1}

Hydrogen 스토어프론트에 코드를 추가하기 전에 Shopify 스토어를 연결하고 커스텀 설정 온보딩을 시작하세요. 아직 스토어를 연결하지 않았다면 [Shopify 스토어 연결](#connect-your-shopify-store)을 완료한 다음 [Braze SDK 활성화](#enable-braze-sdks)로 계속 진행하고 **커스텀 설정**을 선택하세요.

커스텀 설정 플로우에서 Braze는 헤드리스 스토어프론트의 웹사이트 앱을 선택하라는 메시지를 표시합니다.

1. 기존 웹사이트 앱을 선택하거나 새로 만드세요. 앱 이름은 **Shopify**를 제외하고 자유롭게 지정할 수 있습니다. Shopify는 Braze가 표준 Shopify 통합 경로를 위해 예약한 이름입니다.
2. Braze는 선택한 앱의 API 키와 기본 URL(SDK 엔드포인트)을 온보딩 단계에 표시합니다. 각 값에 대해 **복사**를 선택하세요. **설정** > **앱 설정**을 열 필요는 없습니다.
3. 복사한 API 키를 `BRAZE_API_KEY`로, SDK 엔드포인트를 `BRAZE_API_URL`로 Shopify 환경 변수에 사용하세요([2단계](#step-2)).

스토어를 연결한 후에는 **설정** > **앱 설정**에서 선택한 웹사이트 앱의 이름을 변경할 수 있습니다. Shopify 통합에 연결되어 있는 동안에는 해당 앱을 삭제할 수 없습니다.

{% alert warning %}
온보딩 중 선택한 웹사이트 앱의 API 키를 사용하세요. Hydrogen 환경에서 Shopify 통합에 연결된 API 키와 다른 키를 사용하면 Braze가 중복 사용자를 생성하고 SDK 메서드가 예상대로 작동하지 않을 수 있습니다.
{% endalert %}

### 2단계: 하위 도메인 및 환경 변수 추가 {#step-2}

1. Shopify 하위 도메인을 설정하여 [온라인 스토어에서 Hydrogen으로 트래픽을 리디렉션](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic)하세요.
2. 로그인을 위한 [콜백 URI](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment)를 추가하세요. (도메인을 추가하면 URI가 자동으로 추가됩니다.)
3. [Shopify 환경 변수](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable)를 설정하세요:
  - [1단계](#step-1)의 커스텀 설정 온보딩 중에 복사한 API 키와 SDK 엔드포인트를 사용하여 두 개의 환경 변수를 만드세요.
    - `BRAZE_API_KEY`
    - `BRAZE_API_URL`

### 3단계: 온사이트 추적 활성화 {#step-3-enable-onsite-tracking}

첫 번째 단계는 Braze 웹 SDK를 초기화하는 것입니다. NPM 패키지를 설치하여 진행하는 것을 권장합니다:

```java
npm install --save @braze/web-sdk@6.8.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
지원되는 최소 Braze 웹 SDK 버전은 5.4.0입니다. Shopify 커스텀 통합(헤드리스 스토어프론트 포함)의 경우 새로운 SDK 버전이 출시되면 알림을 받지만, 스토어프론트 코드와 통합 설정의 SDK 버전을 모두 업데이트하여 업그레이드를 직접 관리해야 합니다.
{% endalert %}

그런 다음 `vite.config.js` 파일에 [이 설정을 포함]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)하여 최상위 키로 추가하세요:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

NPM 패키지를 설치한 후에는 `Layout` 컴포넌트 내부의 `useEffect` 훅에서 SDK를 초기화해야 합니다. Hydrogen 버전에 따라 이 컴포넌트는 `root.jsx` 또는 `layout.jsx` 파일에 위치할 수 있습니다:

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

`data.brazeApiKey`와 `data.brazeApiUrl` 값은 [2단계](#step-2)에서 생성한 환경 변수를 사용하여 컴포넌트 로더에 포함해야 합니다:

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
콘텐츠 보안 정책(일반적으로 Hydrogen의 `entry.server.jsx` 파일에 위치)은 로컬 및 프로덕션 환경에서 Braze 스크립트의 기능에 영향을 줄 수 있습니다. Oxygen을 통해 Shopify로 전송되는 미리보기 빌드 또는 커스텀 배포를 통해 테스트하는 것을 권장합니다. 문제가 발생하면 JavaScript가 작동할 수 있도록 CSP를 구성해야 합니다.
{% endalert %}

### 4단계: Shopify 계정 로그인 이벤트 추가 {#step-4-add-a-shopify-account-login-event}

구매자가 자신의 계정에 로그인하고 사용자 정보를 Braze에 동기화할 때 이를 추적합니다. 여기에는 Braze 외부 ID로 고객을 식별하기 위해 `changeUser` 메서드를 호출하는 것이 포함됩니다.

{% alert note %}
현재 커스텀 Braze 외부 ID를 지원하기 위한 가이드를 제공하고 있지 않습니다. 지금 통합에 이 기능이 필요한 경우 고객 성공 매니저에게 문의하세요.
{% endalert %}

시작하기 전에 Hydrogen 내에서 고객 로그인이 작동하도록 콜백 URI를 설정했는지 확인하세요. 자세한 내용은 [Hydrogen에서 Customer Account API 사용](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen)을 참조하세요.

1. 콜백 URI를 설정한 후 Braze SDK를 호출하는 함수를 정의하세요. 새 파일(예: `Tracking.jsx`)을 만들고 컴포넌트에서 가져오세요:

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
2. Braze SDK를 초기화하는 동일한 `useEffect` 훅에 이 함수 호출을 추가하세요:

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
3. `app/graphql/customer-account/CustomerDetailsQuery.js` 파일에 있는 Customer API GraphQL 쿼리에서 고객 이메일 주소와 전화번호를 가져오세요:

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
4. 마지막으로 로더 함수에서 고객 데이터를 로드하세요:

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

### 5단계: 제품 조회 및 장바구니 업데이트 이벤트 추적 추가 {#step-5-add-tracking-for-product-viewed-and-cart-updated-events}

#### 제품 조회 이벤트 {#product-viewed-events}

1. `Tracking.jsx` 파일에 이 함수를 추가하세요:

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
2. 사용자가 제품 페이지를 방문할 때마다 위 함수를 호출하려면, `app/routes/products.$handle.jsx` 파일의 Product 컴포넌트에 `useEffect` 훅을 추가하세요:

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
3. "storefrontUrl" 값을 추가하세요(기본적으로 컴포넌트 로더에 포함되어 있지 않기 때문입니다):

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

#### 장바구니 업데이트 이벤트 {#cart-updated-events}

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

1. `cart_updated` 이벤트를 추적하고 장바구니 토큰을 설정하기 위한 함수를 정의하세요:

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
2. Braze가 장바구니의 속성에 접근할 수 있도록 fetcher 액션에서 `cart` 객체를 반환하세요. `app/routes/cart.jsx` 파일로 이동하여 `action` 함수에 다음을 추가하세요:

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

Remix fetcher에 대한 자세한 내용은 [useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher)를 참조하세요.

{: start="3"}
3. Hydrogen 스토어는 일반적으로 장바구니 객체 상태를 관리하는 `CartForm` 컴포넌트를 정의하며, 이는 장바구니에서 항목을 추가, 제거 및 수량 변경할 때 사용됩니다. `AddToCartButton` 컴포넌트에 form fetcher 상태가 변경될 때(사용자의 장바구니가 업데이트될 때마다) `trackCartUpdated` 함수를 호출하는 또 다른 `useEffect` 훅을 추가하세요:

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
4. 장바구니에서 기존 제품을 업데이트하는 작업에도 동일한 `fetcherKey`를 사용하세요. `CartLineRemoveButton` 및 `CartLineUpdateButton` 컴포넌트(기본적으로 `app/components/CartLineItem.jsx` 파일에 위치)에 다음을 추가하세요:

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

## Braze Shopify 연동 설치하기 {#install-the-braze-shopify-integration}

### 1단계: Shopify 스토어 연결 {#connect-your-shopify-store}

Shopify 파트너 페이지로 이동하여 설정을 시작합니다. 먼저 **설정 시작**을 선택하여 Shopify 앱 스토어에서 Braze 애플리케이션을 설치합니다. 안내에 따라 설치 과정을 완료합니다.

![Braze 대시보드의 Shopify 연동 설정 페이지.]({% image_buster /assets/img/shopify/braze_shopify_integration_page.png %})

### 2단계: Braze SDK 활성화 {#enable-braze-sdks}

Shopify Hydrogen 또는 헤드리스 스토어의 경우 **커스텀 설정** 옵션을 선택합니다.

커스텀 설정에는 웹사이트 앱 선택기가 포함됩니다. 스토어프론트를 구동하는 앱을 선택하거나 새로 생성한 다음, 온보딩 단계에 표시되는 API 키와 SDK 엔드포인트를 복사합니다. 자세한 내용은 [1단계: 웹사이트 앱 선택 및 SDK 자격 증명 복사](#step-1)를 참조하세요.

온보딩 과정을 계속하기 전에, 해당 자격 증명을 사용하여 Shopify 웹사이트에 Braze SDK를 추가했는지 확인합니다.

![Braze SDK 활성화 설정 단계.]({% image_buster /assets/img/shopify/enable_braze_sdks_setup.png %})

### 3단계: Shopify 데이터 추적 {#step-3-track-shopify-data}

Shopify 웹훅을 통해 더 많은 Shopify 이벤트와 속성을 추가하여 연동을 강화합니다. 이 연동을 통해 추적되는 데이터에 대한 자세한 정보는 [Shopify 데이터 기능]({{site.baseurl}}/shopify_data_features)을 참조하세요.

![Shopify 데이터 추적 설정 단계.]({% image_buster /assets/img/shopify/track_shopify_data_setup.png %})

### 4단계: 과거 데이터 백필 (선택 사항) {#step-4-historical-backfill-optional}

커스텀 설정을 통해 [표준 연동]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#historical-backfill-setup)과 동일한 과거 Shopify 데이터 로드를 선택적으로 포함할 수 있습니다: 연동 완료 날짜로부터 최근 90일간의 주문 이벤트와 최근 1년간의 사용자 프로필이 해당됩니다. 이 초기 데이터 로드를 포함하려면 초기 데이터 로드 옵션의 체크박스를 선택합니다.

나중에 백필을 수행하려면 지금 초기 설정을 완료하고 나중에 이 단계로 돌아올 수 있습니다.

![과거 데이터 백필 설정 섹션.]({% image_buster /assets/img/shopify/historical_backfill_setup.png %})

초기 로드의 전체 데이터 목록, 매출 리포팅 동작, 동기화 모니터링에 대해서는 [과거 데이터 백필]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill)을 참조하세요.

### 5단계: 커스텀 데이터 추적 설정 (고급) {#step-5-custom-data-tracking-setup-advanced}

Braze SDK를 사용하면 이 연동에서 지원하는 데이터 이외에 커스텀 이벤트 또는 커스텀 속성을 추적할 수 있습니다. 커스텀 이벤트는 스토어에서의 고유한 상호작용을 캡처합니다. 예를 들면 다음과 같습니다:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table aria-label="5단계: 커스텀 데이터 추적 설정 (고급)" style="width: 100%;">
  <caption>5단계: 커스텀 데이터 추적 설정 (고급)</caption>
  <thead>
    <tr>
      <th style="width: 50%;">커스텀 이벤트</th>
      <th style="width: 50%;">커스텀 속성</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>커스텀 할인 코드 사용</li>
          <li>개인화된 제품 추천과의 상호작용</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>선호 브랜드 또는 제품</li>
          <li>선호 쇼핑 카테고리</li>
          <li>멤버십 또는 로열티 상태</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

SDK는 이벤트 또는 커스텀 속성을 기록하려면 사용자의 기기에서 초기화(활동 수신 대기)되어 있어야 합니다. 커스텀 데이터 기록에 대해 자세히 알아보려면 [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) 및 [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)를 참조하세요.

### 6단계: 사용자 관리 방식 구성 (선택 사항) {#step-6}

드롭다운에서 `external_id` 유형을 선택합니다.

![구독자 수집 섹션.]({% image_buster /assets/img/shopify/external_id_standard.png %})

{% alert important %}
이메일 주소 또는 해시된 이메일 주소를 Braze 외부 ID로 사용하면 데이터 소스 전반에서 ID 관리를 간소화할 수 있습니다. 그러나 사용자 개인정보 보호 및 데이터 보안에 대한 잠재적 위험을 고려하는 것이 중요합니다.<br><br>

- **추측 가능한 정보:** 이메일 주소는 쉽게 추측할 수 있어 공격에 취약합니다.
- **악용 위험:** 악의적인 사용자가 웹 브라우저를 변조하여 다른 사람의 이메일 주소를 외부 ID로 전송하면 민감한 메시지나 계정 정보에 접근할 수 있습니다.
{% endalert %}

기본적으로 Braze는 Shopify에서 가져온 이메일을 외부 ID로 사용하기 전에 자동으로 소문자로 변환합니다. 이메일 또는 해시된 이메일을 외부 ID로 사용하는 경우, 외부 ID로 할당하기 전에 또는 다른 데이터 소스에서 해싱하기 전에 이메일 주소도 소문자로 변환되었는지 확인합니다. 이렇게 하면 외부 ID 불일치를 방지하고 Braze에서 중복 사용자 프로필이 생성되는 것을 피할 수 있습니다.

{% alert note %}
다음 단계는 외부 ID 선택에 따라 달라집니다:<br><br>
- **커스텀 외부 ID 유형을 선택한 경우:** 6.1~6.3 단계를 완료하여 커스텀 외부 ID 구성을 설정합니다.
- **Shopify 고객 ID, 이메일 또는 해시된 이메일을 선택한 경우:** 6.1~6.3 단계를 건너뛰고 6.4 단계로 바로 진행합니다.
{% endalert %}

#### 6.1단계: `braze.external_id` 메타필드 생성 {#step-61-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

메타필드가 생성되면 고객에 대해 이를 채웁니다. 다음 접근 방식을 권장합니다:

- **고객 생성 웹훅 수신:** [`customer/create` 이벤트](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks)를 수신하는 웹훅을 설정합니다. 이를 통해 새 고객이 생성될 때 메타필드를 작성할 수 있습니다.
- **기존 고객 백필:** [Admin API](https://shopify.dev/docs/api/admin-graphql) 또는 [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)를 사용하여 이전에 생성된 고객에 대한 메타필드를 백필합니다.

#### 6.2단계: 외부 ID 검색을 위한 엔드포인트 생성 {#step-62-create-an-endpoint-to-retrieve-your-external-id}

Braze가 외부 ID를 검색하기 위해 호출할 수 있는 퍼블릭 엔드포인트를 생성해야 합니다. 이를 통해 Shopify가 `braze.external_id` 메타필드를 직접 제공할 수 없는 시나리오에서 Braze가 ID를 가져올 수 있습니다.

##### 엔드포인트 사양 {#endpoint-specifications}

**메서드:** GET

Braze는 엔드포인트에 다음 파라미터를 전송합니다:

| 파라미터 | 필수 | 데이터 유형 | 설명 |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id | 예 | 문자열 | Shopify 고객 ID입니다. |
| shopify_storefront | 예 | 문자열 | 요청에 대한 스토어프론트 이름입니다. 예: `<storefront_name>.myshopify.com` |
| email_address | 아니오 | 문자열 | 로그인한 사용자의 이메일 주소입니다. <br><br>이 필드는 특정 웹훅 시나리오에서 누락될 수 있습니다. 엔드포인트 로직에서 null 값을 처리해야 합니다(예: 내부 로직에 필요한 경우 shopify_customer_id를 사용하여 이메일을 가져옵니다). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="엔드포인트 사양" }

##### 엔드포인트 예시 {#example-endpoint}

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```


##### 예상 응답 {#expected-response}
Braze는 외부 ID JSON을 반환하는 `200` 상태 코드를 기대합니다:
```json
{
  "external_id": "my_external_id"
}
```

##### 유효성 검사 {#validation}

`shopify_customer_id`와 `email_address`(있는 경우)가 Shopify의 고객 값과 일치하는지 검증하는 것이 중요합니다. [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) 또는 [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)를 사용하여 이러한 파라미터를 검증하고 올바른 `braze.external_id` 메타필드를 가져올 수 있습니다.

##### 실패 동작 및 병합 {#failure-behavior-and-merging}
`200` 이외의 모든 상태 코드는 실패로 간주됩니다.

{% multi_lang_include partners/shopify/external_id_merge_implications.md %}

#### 6.3단계: 외부 ID 입력 {#step-63-input-your-external-id}

[6단계](#step-6)를 반복하고, Braze 외부 ID 유형으로 커스텀 외부 ID를 선택한 후 엔드포인트 URL을 입력합니다.

##### 고려 사항 {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

#### 6.4단계: Shopify에서 이메일 또는 SMS 옵트인 수집 (선택 사항) {#step-64-collect-your-email-or-sms-opt-ins-from-shopify-optional}

Shopify에서 이메일 또는 SMS 마케팅 옵트인을 수집하는 옵션이 있습니다.

이메일 또는 SMS 채널을 사용하는 경우 이메일 및 SMS 마케팅 옵트인 상태를 Braze로 동기화할 수 있습니다. Shopify에서 이메일 마케팅 옵트인을 동기화하면 Braze는 해당 특정 스토어와 연결된 모든 사용자에 대해 이메일 구독 그룹을 자동으로 생성합니다. 이 구독 그룹에 고유한 이름을 지정해야 합니다.

![이메일 또는 SMS 마케팅 옵트인 수집 옵션이 있는 구독자 수집 섹션.]({% image_buster /assets/img/shopify/collect_email_subscribers.png %})

{% multi_lang_include partners/shopify/third_party_capture_form_note.md %}

### 7단계: 제품 동기화 (선택 사항) {#step-7-sync-products-optional}

Shopify 스토어의 모든 제품을 Braze 카탈로그에 동기화하여 더 깊은 메시징 개인화를 구현할 수 있습니다. 자동 업데이트가 거의 실시간으로 이루어지므로 카탈로그에 항상 최신 제품 세부 정보가 반영됩니다. 자세한 내용은 [Shopify 제품 동기화]({{site.baseurl}}/shopify_catalogs)를 확인하세요.

![Braze로 제품 데이터 동기화 설정 단계.]({% image_buster /assets/img/shopify/sync_product_data.png %})

### 8단계: 채널 활성화 {#step-8-activate-channels}

Shopify 직접 연동을 사용하여 인앱 메시지, Content Cards 및 기능 플래그를 활성화하려면 각 채널을 SDK에 추가합니다. 각 채널에 대해 제공된 설명서 링크를 따릅니다:

- **In-App Messages:** 리드 캡처 양식 사용 사례를 위한 인앱 메시지 활성화는 [인앱 메시지]({{site.baseurl}}/developer_guide/in_app_messages)를 참조하세요.
- **Content Cards:** 받은편지함 또는 웹사이트 배너 사용 사례를 위한 Content Cards 활성화는 [Content Cards]({{site.baseurl}}/developer_guide/content_cards)를 참조하세요.
- **기능 플래그:** 사이트 실험 사용 사례를 위한 기능 플래그 활성화는 [기능 플래그]({{site.baseurl}}/developer_guide/feature_flags)를 참조하세요.

### 9단계: 설정 완료 {#step-9-finish-setup}

모든 단계를 완료한 후 **설정 완료**를 선택하여 파트너 페이지로 돌아갑니다. 그런 다음 표시되는 배너에 안내된 대로 Shopify 관리자 페이지에서 Braze 앱 임베드를 활성화합니다.

![연동 설정을 완료하려면 Shopify에서 Braze 앱 임베드를 활성화하라는 배너.]({% image_buster /assets/img/shopify/shopify_app_embed_banner.png %})

#### 예제 코드 {#example-code}

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/)은 이전 단계에서 다룬 모든 코드를 포함하는 Hydrogen 앱 예제입니다.