---
nav_title: Shopify カスタム統合設定
article_title: Shopify カスタム統合設定
description: "この参考記事では、カスタムストアフロントを使用して Shopify Hydrogen ストアやヘッドレス Shopify ストアに接続する方法を説明します。"
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 3
---

# Shopify カスタム統合設定 {#shopify-custom-integration-setup}

> このページでは、カスタムストアフロントを使用して、Shopify Hydrogen ストアやヘッドレス Shopify ストアとBrazeを統合する方法を説明します。

このガイドでは、Shopifyの Hydrogen フレームワークを例にしています。ただし、ブランドが「ヘッドレス」フロントエンド設定でストアのバックエンドに Shopify を使用している場合も、同様のアプローチをとることができます。

Shopify のヘッドレスストアをBrazeと統合するには、以下の2つの目標を達成する必要があります。

1. **Braze Web SDKを初期化してロードし、オンサイトトラッキングを有効にする**<br><br> 手動で Shopify Webサイトにコードを追加して、Brazeオンサイトトラッキングを有効にします。Shopify ヘッドレスストアにBraze SDKを実装することで、セッション、匿名のユーザー行動、チェックアウト前のショッパーアクション、そして開発チームと一緒に選択した[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)や[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)を含むオンサイトアクティビティをトラッキングできます。また、アプリ内メッセージやContent Cardsなど、SDKがサポートするチャネルを追加することもできます。

{: start="2"}
2. **BrazeのShopify統合をインストールする**<br><br> ShopifyストアをBrazeに接続すると、Shopify webhookを通じて顧客、チェックアウト、注文、商品データにアクセスできるようになります。

{% alert important %}
統合を開始する前に、Shopify ストアフロントのチェックアウトサブドメインが正しく設定されていることを確認してください。詳細については、[Migrate from the online store to Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate) を参照してください。<br><br> この設定が正しく行われないと、BrazeはShopifyチェックアウトwebhookを処理できません。また、ローカルの開発環境で統合をテストすることもできません。ストアフロントとチェックアウトページ間の共有ドメインに依存しているためです。
{% endalert %}

これらの目標を達成するには、以下のステップに従ってください。

## Braze Web SDKの初期化と読み込み {#initialize-and-load-the-braze-web-sdk}

### ステップ1：Webサイトアプリを選択してSDK認証情報をコピーする {#step-1}

Hydrogen ストアフロントにコードを追加する前に、Shopifyストアを接続してカスタムセットアップのオンボーディングを開始してください。ストアをまだ接続していない場合は、[Shopifyストアを接続する](#connect-your-shopify-store)を完了してから、[Braze SDKを有効にする](#enable-braze-sdks)に進み、**カスタムセットアップ**を選択します。

カスタムセットアップフローでは、ヘッドレスストアフロント用のWebサイトアプリを選択するよう求められます。

1. 既存のWebサイトアプリを選択するか、新しいアプリを作成します。アプリには **Shopify** 以外の任意の名前を付けることができます。**Shopify** はBrazeが標準のShopify統合パスのために予約しています。
2. Brazeは選択したアプリのAPIキーとベースURL（SDKエンドポイント）をオンボーディングステップに表示します。それぞれの値の**コピー**を選択してください。**設定** > **アプリ設定**を開く必要はありません。
3. コピーしたAPIキーを `BRAZE_API_KEY` として、SDKエンドポイントを `BRAZE_API_URL` としてShopifyの環境変数で使用します（[ステップ2](#step-2)）。

ストアを接続した後、**設定** > **アプリ設定**で選択したWebサイトアプリの名前を変更できます。Shopify統合に接続されている間はアプリを削除できません。

{% alert warning %}
オンボーディング時に選択したWebサイトアプリのAPIキーを使用してください。Hydrogen環境がShopify統合に接続されているものとは異なるAPIキーを使用している場合、Brazeが重複ユーザーを作成したり、SDKメソッドが期待どおりに動作しなかったりする可能性があります。
{% endalert %}

### ステップ2：サブドメインと環境変数を追加する {#step-2}

1. Shopifyサブドメインを設定して、[オンラインストアからHydrogenにトラフィックをリダイレクト](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic)します。
2. ログイン用の[コールバックURI](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment)を追加します（ドメインが追加されると、URIは自動的に追加されます）。
3. [Shopify環境変数](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable)を設定します：
  - [ステップ1](#step-1)のカスタムセットアップオンボーディング時にコピーしたAPIキーとSDKエンドポイントを使用して、2つの環境変数を作成します。
    - `BRAZE_API_KEY`
    - `BRAZE_API_URL`

### ステップ3：オンサイトトラッキングを有効にする {#step-3-enable-onsite-tracking}

最初のステップは、Braze Web SDKを初期化することです。NPMパッケージをインストールすることをお勧めします：

```java
npm install --save @braze/web-sdk@6.8.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
サポートされるBraze Web SDKの最小バージョンは5.4.0です。Shopifyカスタム統合（ヘッドレスストアフロントを含む）では、新しいSDKバージョンが利用可能になると通知を受け取りますが、ストアフロントのコードと統合設定のSDKバージョンの両方を更新することで、アップグレードはお客様側で管理していただきます。
{% endalert %}

次に、`vite.config.js` ファイルのトップレベルキーとして[この設定を含めます]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web)：

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

NPMパッケージをインストールした後、`Layout` コンポーネント内の `useEffect` フック内でSDKを初期化する必要があります。Hydrogenのバージョンに応じて、このコンポーネントは `root.jsx` または `layout.jsx` ファイルにある場合があります：

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

`data.brazeApiKey` と `data.brazeApiUrl` の値は、[ステップ2](#step-2)で作成した環境変数を使用してコンポーネントローダーに含める必要があります：

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
コンテンツセキュリティポリシー（通常はHydrogenの `entry.server.jsx` ファイルにあります）は、ローカル環境と本番環境の両方でBrazeスクリプトの機能に影響を与える可能性があります。OxygenまたはカスタムデプロイメントでShopifyに送信されるプレビュービルドを通じてテストすることをお勧めします。問題が発生した場合は、JavaScriptが機能するようCSPを設定する必要があります。
{% endalert %}

### ステップ4：Shopifyアカウントログインイベントを追加する {#step-4-add-a-shopify-account-login-event}

買い物客がアカウントにサインインし、ユーザー情報をBrazeに同期するタイミングを追跡します。これには、Braze external IDで顧客を識別するための `changeUser` メソッドの呼び出しが含まれます。

{% alert note %}
現在、カスタムのBraze external IDのサポートに関するガイダンスは提供していません。統合で今すぐこれが必要な場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

開始する前に、Hydrogen内で顧客ログインが機能するようにコールバックURIを設定していることを確認してください。詳細については、[HydrogenでのCustomer Account APIの使用](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen)を参照してください。

1. コールバックURIを設定した後、Braze SDKを呼び出すための関数を定義します。新しいファイル（`Tracking.jsx` など）を作成し、コンポーネントからインポートします：

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
2. Braze SDKを初期化する同じ `useEffect` フック内に、この関数の呼び出しを追加します：

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
3. Customer API GraphQLクエリで顧客のメールアドレスと電話番号をフェッチします。このクエリは `app/graphql/customer-account/CustomerDetailsQuery.js` ファイルにあります：

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
4. 最後に、ローダー関数で顧客データを読み込みます：

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

### ステップ5：Product ViewedイベントとCart Updatedイベントのトラッキングを追加する {#step-5-add-tracking-for-product-viewed-and-cart-updated-events}

#### Product Viewedイベント {#product-viewed-events}

1. `Tracking.jsx` ファイルにこの関数を追加します：

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
2. ユーザーが商品ページにアクセスするたびにこの関数を呼び出すには、`app/routes/products.$handle.jsx` ファイル内のProductコンポーネントに `useEffect` フックを追加します：

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
3. 「storefrontUrl」の値を追加します（デフォルトではコンポーネントローダーに含まれていないため）：

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

#### Cart Updatedイベント {#cart-updated-events}

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

1. `cart_updated` イベントのトラッキングとカートトークンの設定を行う関数を定義します：

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
2. Brazeがそのプロパティにアクセスできるよう、フェッチャーアクションから `cart` オブジェクトを返します。`app/routes/cart.jsx` ファイルに移動し、`action` 関数に以下を追加します：

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

Remixフェッチャーの詳細については、[useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher)を参照してください。

{: start="3"}
3. Hydrogenストアでは通常、カートオブジェクトの状態を管理する `CartForm` コンポーネントを定義しており、カート内のアイテムの追加、削除、数量変更時に使用されます。`AddToCartButton` コンポーネントに別の `useEffect` フックを追加して、フォームフェッチャーの状態が変更されるたびに（ユーザーのカートが更新されるたびに）`trackCartUpdated` 関数を呼び出すようにします：

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
4. カートの既存商品を更新するアクションにも同じ `fetcherKey` を使用します。`CartLineRemoveButton` と `CartLineUpdateButton` コンポーネント（デフォルトでは `app/components/CartLineItem.jsx` ファイルにあります）に以下を追加します：

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

## Braze Shopifyインテグレーションのインストール {#install-the-braze-shopify-integration}

### ステップ1：Shopifyストアを接続する {#connect-your-shopify-store}

Shopifyパートナーページに移動して設定を開始します。まず、**Begin Setup** を選択してShopify App StoreからBrazeアプリケーションをインストールします。ガイドに従ってインストールプロセスを完了してください。

![BrazeダッシュボードのShopifyインテグレーション設定ページ。]({% image_buster /assets/img/shopify/braze_shopify_integration_page.png %})

### ステップ2：Braze SDKを有効にする {#enable-braze-sdks}

Shopify Hydrogenまたはヘッドレスストアの場合は、**Custom setup** オプションを選択します。

カスタム設定にはWebサイトアプリピッカーが含まれています。ストアフロントを動かすアプリを選択または作成し、オンボーディングステップに表示されるAPIキーとSDKエンドポイントをコピーします。詳細については、[ステップ1：Webサイトアプリを選択してSDK認証情報をコピーする](#step-1)を参照してください。

オンボーディングプロセスを続行する前に、これらの認証情報を使用してBraze SDKをShopify Webサイトに追加したことを確認してください。

![Braze SDKを有効にする設定ステップ。]({% image_buster /assets/img/shopify/enable_braze_sdks_setup.png %})

### ステップ3：Shopifyデータをトラッキングする {#step-3-track-shopify-data}

Shopifyイベントと属性を追加してインテグレーションを強化します。これらはShopify webhookによって動作します。このインテグレーションでトラッキングされるデータの詳細については、[Shopifyデータ機能]({{site.baseurl}}/shopify_data_features)を参照してください。

![Shopifyデータをトラッキングする設定ステップ。]({% image_buster /assets/img/shopify/track_shopify_data_setup.png %})

### ステップ4：過去データのバックフィル（オプション） {#step-4-historical-backfill-optional}

カスタム設定では、[標準インテグレーション]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#historical-backfill-setup)と同じ過去のShopifyデータロードをオプションで含めることができます。これには、インテグレーション完了日から遡って過去90日間の注文イベントと過去1年間のユーザープロファイルが含まれます。この初期データロードを含めるには、初期データロードオプションのチェックボックスを選択してください。

後でバックフィルを実行したい場合は、今は初期設定を完了し、後からこのステップに戻ることができます。

![過去データのバックフィル設定セクション。]({% image_buster /assets/img/shopify/historical_backfill_setup.png %})

初期ロードのデータ一覧、収益レポートの動作、同期の監視については、[過去データのバックフィル]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill)を参照してください。

### ステップ5：カスタムデータトラッキング設定（上級） {#step-5-custom-data-tracking-setup-advanced}

Braze SDKを使用すると、このインテグレーションでサポートされているデータを超えるカスタムイベントやカスタム属性をトラッキングできます。カスタムイベントは、ストアでのユニークなインタラクションをキャプチャします。例：

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table aria-label="ステップ5：カスタムデータトラッキング設定（上級）" style="width: 100%;">
  <caption>ステップ5：カスタムデータトラッキング設定（上級）</caption>
  <thead>
    <tr>
      <th style="width: 50%;">カスタムイベント</th>
      <th style="width: 50%;">カスタム属性</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>カスタム割引コードの使用</li>
          <li>パーソナライズされた商品レコメンデーションとのインタラクション</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>お気に入りのブランドや商品</li>
          <li>希望するショッピングカテゴリ</li>
          <li>メンバーシップまたはロイヤルティステータス</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

SDKは、イベントやカスタム属性をログに記録するために、ユーザーのデバイス上で初期化（アクティビティのリスニング）されている必要があります。カスタムデータのログ記録について詳しくは、[User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html)および[logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent)を参照してください。

### ステップ6：ユーザー管理方法を設定する（オプション） {#step-6}

ドロップダウンから`external_id`タイプを選択します。

![「購読者を収集」セクション。]({% image_buster /assets/img/shopify/external_id_standard.png %})

{% alert important %}
メールアドレスまたはハッシュ化されたメールアドレスをBraze external IDとして使用すると、データソース間のアイデンティティ管理を簡素化できます。ただし、ユーザーのプライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。<br><br>

- **推測可能な情報：**メールアドレスは容易に推測可能であり、攻撃に対して脆弱になります。
- **悪用のリスク：**悪意のあるユーザーがWebブラウザを変更して他人のメールアドレスをexternal IDとして送信した場合、機密メッセージやアカウント情報にアクセスされる可能性があります。
{% endalert %}

デフォルトでは、BrazeはShopifyからのメールをexternal IDとして使用する前に自動的に小文字に変換します。メールアドレスまたはハッシュ化されたメールアドレスをexternal IDとして使用している場合は、他のデータソースからexternal IDとして割り当てる前またはハッシュ化する前に、メールアドレスも小文字に変換されていることを確認してください。これにより、external IDの不一致を防ぎ、Brazeで重複したユーザープロファイルが作成されることを回避できます。

{% alert note %}
次のステップはexternal IDの選択によって異なります。<br><br>
- **カスタムexternal IDタイプを選択した場合：**ステップ6.1～6.3を完了してカスタムexternal ID設定を行います。
- **Shopify顧客ID、メール、またはハッシュ化されたメールを選択した場合：**ステップ6.1～6.3をスキップして、ステップ6.4に直接進みます。
{% endalert %}

#### ステップ6.1：`braze.external_id`メタフィールドを作成する {#step-61-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

メタフィールドが作成されたら、顧客に対してデータを入力します。以下のアプローチを推奨します：

- **顧客作成webhookをリスニングする：**[`customer/create`イベント](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks)をリスニングするwebhookを設定します。これにより、新しい顧客が作成されたときにメタフィールドを書き込むことができます。
- **既存の顧客をバックフィルする：**[Admin API](https://shopify.dev/docs/api/admin-graphql)または[Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用して、以前に作成された顧客のメタフィールドをバックフィルします。

#### ステップ6.2：external IDを取得するエンドポイントを作成する {#step-62-create-an-endpoint-to-retrieve-your-external-id}

Brazeがexternal IDを取得するために呼び出せるパブリックエンドポイントを作成する必要があります。これにより、Shopifyが`braze.external_id`メタフィールドを直接提供できないシナリオでBrazeがIDを取得できます。

##### エンドポイント仕様 {#endpoint-specifications}

**メソッド：**GET

Brazeはエンドポイントに以下のパラメーターを送信します：

| パラメーター | 必須 | データ型 | 説明 |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id | はい | String | Shopify顧客ID。 |
| shopify_storefront | はい | String | リクエストのストアフロント名。例：`<storefront_name>.myshopify.com` |
| email_address | いいえ | String | ログインユーザーのメールアドレス。<br><br>特定のwebhookシナリオではこのフィールドが欠落する場合があります。エンドポイントのロジックではnull値を考慮する必要があります（例えば、内部ロジックで必要な場合は、shopify_customer_idを使用してメールを取得するなど）。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="エンドポイント仕様" }

##### エンドポイントの例 {#example-endpoint}

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```


##### 期待されるレスポンス {#expected-response}
Brazeは、external IDのJSONを返す`200`ステータスコードを期待します：
```json
{
  "external_id": "my_external_id"
}
```

##### バリデーション {#validation}

`shopify_customer_id`と`email_address`（存在する場合）がShopifyの顧客値と一致することを検証することが重要です。[Shopify Admin API](https://shopify.dev/docs/api/admin-graphql)または[Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer)を使用して、これらのパラメーターを検証し、正しい`braze.external_id`メタフィールドを取得できます。

##### 失敗時の動作とマージ {#failure-behavior-and-merging}
`200`以外のステータスコードはすべて失敗とみなされます。

{% multi_lang_include partners/shopify/external_id_merge_implications.md %}

#### ステップ6.3：external IDを入力する {#step-63-input-your-external-id}

[ステップ6](#step-6)を繰り返し、Braze external IDタイプとしてカスタムexternal IDを選択した後、エンドポイントURLを入力します。

##### 考慮事項 {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

#### ステップ6.4：ShopifyからメールまたはSMSオプトインを収集する（オプション） {#step-64-collect-your-email-or-sms-opt-ins-from-shopify-optional}

ShopifyからメールまたはSMSマーケティングオプトインを収集するオプションがあります。

メールまたはSMSチャネルを使用している場合は、メールおよびSMSマーケティングオプトインのステータスをBrazeに同期できます。Shopifyからメールマーケティングオプトインを同期すると、Brazeはその特定のストアに関連付けられたすべてのユーザーに対してメール購読グループを自動的に作成します。この購読グループには一意の名前を作成する必要があります。

![メールまたはSMSマーケティングオプトインを収集するオプション付きの「購読者を収集」セクション。]({% image_buster /assets/img/shopify/collect_email_subscribers.png %})

{% multi_lang_include partners/shopify/third_party_capture_form_note.md %}

### ステップ7：商品を同期する（オプション） {#step-7-sync-products-optional}

Shopifyストアのすべての商品をBrazeカタログに同期して、より深いメッセージングパーソナライゼーションを実現できます。自動更新はほぼリアルタイムで行われるため、カタログには常に最新の商品詳細が反映されます。詳しくは、[Shopify商品同期]({{site.baseurl}}/shopify_catalogs)をご覧ください。

![商品データをBrazeに同期する設定ステップ。]({% image_buster /assets/img/shopify/sync_product_data.png %})

### ステップ8：チャネルを有効化する {#step-8-activate-channels}

Shopifyダイレクトインテグレーションを使用してアプリ内メッセージ、Content Cards、およびフィーチャーフラグを有効化するには、各チャネルをSDKに追加します。各チャネルについて提供されているドキュメントリンクに従ってください：

- **アプリ内メッセージ：**リードキャプチャフォームのユースケース向けにアプリ内メッセージを有効化するには、[アプリ内メッセージ]({{site.baseurl}}/developer_guide/in_app_messages)を参照してください。
- **Content Cards：**受信トレイやWebサイトバナーのユースケース向けにContent Cardsを有効化するには、[Content Cards]({{site.baseurl}}/developer_guide/content_cards)を参照してください。
- **フィーチャーフラグ：**サイト実験のユースケース向けにフィーチャーフラグを有効化するには、[フィーチャーフラグ]({{site.baseurl}}/developer_guide/feature_flags)を参照してください。

### ステップ9：設定を完了する {#step-9-finish-setup}

すべてのステップが完了したら、**Finish Setup** を選択してパートナーページに戻ります。次に、表示されるバナーの指示に従って、Shopify管理ページでBrazeアプリ埋め込みを有効化します。

![インテグレーションの設定を完了するためにShopifyでBrazeアプリ埋め込みを有効化するよう促すバナー。]({% image_buster /assets/img/shopify/shopify_app_embed_banner.png %})

#### サンプルコード {#example-code}

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/)は、前述のステップで説明したすべてのコードを含むHydrogenアプリの例です。