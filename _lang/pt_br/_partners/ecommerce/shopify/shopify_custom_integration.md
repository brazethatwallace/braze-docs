---
nav_title: Configuração de integração personalizada da Shopify
article_title: Configuração de integração personalizada da Shopify
description: "Este artigo de referência aborda como se conectar a uma loja Shopify Hydrogen ou a qualquer loja Shopify headless usando uma vitrine personalizada."
page_type: partner
search_tag: Partner
alias: /shopify_custom_integration/
page_order: 3
---

# Configuração da integração personalizada do Shopify {#shopify-custom-integration-setup}

> Esta página orienta você sobre como integrar a Braze a uma loja Shopify Hydrogen ou a qualquer loja Shopify headless usando uma vitrine personalizada.

Este guia usa o framework Hydrogen da Shopify como exemplo. No entanto, você pode seguir uma abordagem semelhante se a sua marca usar o Shopify para o backend da sua loja com uma configuração de front-end "headless".

Para integrar sua loja Shopify headless com a Braze, você precisa concluir estas duas metas:

1. **Inicializar e carregar o Braze Web SDK para ativar o rastreamento no site**<br><br> Adicione manualmente o código em seu site do Shopify para ativar o rastreamento no site da Braze. Ao implementar o Braze SDK em sua loja Shopify headless, é possível rastrear as atividades no site, incluindo sessões, comportamento de usuário anônimo, ações do comprador antes do checkout e quaisquer [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events) ou [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) que você decida incluir com sua equipe de desenvolvimento. Você também pode adicionar quaisquer canais compatíveis com os SDKs, como In-App Messages ou Content Cards.

{: start="2"}
2. **Instalar a integração da Braze com o Shopify**<br><br> Depois de conectar sua loja Shopify à Braze, você terá acesso aos dados de clientes, checkout, pedidos e produtos por meio de webhooks do Shopify.

{% alert important %}
Antes de iniciar sua integração, confirme que você configurou corretamente o subdomínio de checkout para sua vitrine do Shopify. Para saber mais, consulte [Migrar da loja on-line para o Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate).<br><br> Se essa configuração não for feita corretamente, a Braze não poderá processar os webhooks de checkout do Shopify. Também não será possível testar a integração em um ambiente de desenvolvimento local, pois isso depende de um domínio compartilhado entre a vitrine e a página de checkout.
{% endalert %}

Para concluir essas metas, siga estas etapas:

## Inicializar e carregar o Braze Web SDK {#initialize-and-load-the-braze-web-sdk}

### Etapa 1: Selecionar um app de website e copiar as credenciais do SDK {#step-1}

Antes de adicionar código à sua loja Hydrogen, conecte sua loja Shopify e inicie a integração de configuração personalizada. Se você ainda não conectou sua loja, conclua [Conectar sua loja Shopify](#connect-your-shopify-store) e, em seguida, prossiga com [Ativar os SDKs da Braze](#enable-braze-sdks) e selecione **Custom setup**.

No fluxo de configuração personalizada, a Braze solicita que você selecione o app de website para sua loja headless:

1. Selecione um app de website existente ou crie um novo. Você pode nomear o app com qualquer nome, exceto **Shopify**, que a Braze reserva para o caminho de integração padrão do Shopify.
2. A Braze exibe a chave de API do app selecionado e a URL base (seu endpoint de SDK) na etapa de integração. Selecione **Copy** para cada valor — não é necessário abrir **Settings** > **App Settings**.
3. Use a chave de API copiada como `BRAZE_API_KEY` e o endpoint de SDK como `BRAZE_API_URL` nas variáveis de ambiente do Shopify ([Etapa 2](#step-2)).

Depois de conectar a loja, você pode renomear o app de website selecionado em **Settings** > **App Settings**. Não é possível excluir o app enquanto ele estiver conectado à sua integração com o Shopify.

{% alert warning %}
Use a chave de API do app de website que você selecionou durante a integração. Se o seu ambiente Hydrogen usar uma chave de API diferente daquela conectada à sua integração com o Shopify, a Braze poderá criar usuários duplicados e os métodos do SDK poderão não funcionar como esperado.
{% endalert %}

### Etapa 2: Adicionar subdomínio e variáveis de ambiente {#step-2}

1. Configure seu subdomínio Shopify para [redirecionar o tráfego da sua loja online para o Hydrogen](https://shopify.dev/docs/storefronts/headless/hydrogen/migrate/redirect-traffic).
2. Adicione um [URI de retorno de chamada](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen#step-2-set-up-the-environment) para login. (O URI será adicionado automaticamente quando o domínio for adicionado.)
3. Configure suas [variáveis de ambiente do Shopify](https://shopify.dev/docs/storefronts/headless/hydrogen/environments#create-a-new-environment-variable):
  - Crie duas variáveis de ambiente usando a chave de API e o endpoint de SDK que você copiou durante a integração de configuração personalizada na [Etapa 1](#step-1).
    - `BRAZE_API_KEY`
    - `BRAZE_API_URL`

### Etapa 3: Ativar o rastreamento no site {#step-3-enable-onsite-tracking}

A primeira etapa é inicializar o Braze Web SDK. Recomendamos fazer isso instalando nosso pacote NPM:

```java
npm install --save @braze/web-sdk@6.8.0
# or, using yarn:
# yarn add @braze/web-sdk
```

{% alert important %}
A versão mínima compatível do Braze Web SDK é a 5.4.0. Para integrações personalizadas do Shopify (incluindo lojas headless), você recebe notificações quando novas versões do SDK estão disponíveis, mas gerencia os upgrades do seu lado, atualizando tanto o código da sua loja quanto a versão do SDK nas configurações de integração.
{% endalert %}

Em seguida, [inclua esta configuração]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=web) como uma chave de nível superior no seu arquivo `vite.config.js`:

```java
optimizeDeps: {
    exclude: ['@braze/web-sdk']
}
```

Após instalar o pacote NPM, você deve inicializar o SDK dentro de um hook `useEffect` no componente `Layout`. Dependendo da sua versão do Hydrogen, esse componente pode estar localizado no arquivo `root.jsx` ou `layout.jsx`:

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

Os valores `data.brazeApiKey` e `data.brazeApiUrl` precisam ser incluídos no loader do componente usando as variáveis de ambiente criadas na [Etapa 2](#step-2):

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
As políticas de segurança de conteúdo (geralmente localizadas no arquivo Hydrogen `entry.server.jsx`) podem afetar a funcionalidade dos scripts da Braze em ambientes locais e de produção. Sugerimos testar por meio de builds de prévia enviados ao Shopify via Oxygen ou implantações personalizadas. Se você encontrar problemas, será necessário configurar seu CSP para permitir que nosso JavaScript funcione.
{% endalert %}

### Etapa 4: Adicionar um evento de login de conta Shopify {#step-4-add-a-shopify-account-login-event}

Rastreie quando um comprador faz login em sua conta e sincroniza suas informações de usuário com a Braze. Isso inclui chamar nosso método `changeUser` para identificar clientes com um ID externo da Braze.

{% alert note %}
No momento, não temos orientações para oferecer suporte a um ID externo personalizado da Braze. Se você precisar disso para sua integração agora, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

Antes de começar, certifique-se de ter configurado os URIs de retorno de chamada para que o login do cliente funcione no Hydrogen. Para saber mais, consulte [Usando a API de conta de cliente com Hydrogen](https://shopify.dev/docs/storefronts/headless/building-with-the-customer-account-api/hydrogen).

1. Depois de configurar os URIs de retorno de chamada, defina uma função para chamar o SDK da Braze. Crie um novo arquivo (como `Tracking.jsx`) e importe-o dos seus componentes:

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
2. No mesmo hook `useEffect` que inicializa o SDK da Braze, adicione a chamada a esta função:

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
3. Busque o endereço de e-mail e o número de telefone do cliente na sua consulta GraphQL da API de clientes, localizada no arquivo `app/graphql/customer-account/CustomerDetailsQuery.js`:

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
4. Por fim, carregue os dados do cliente na sua função loader:

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

### Etapa 5: Adicionar rastreamento para eventos de Product Viewed e Cart Updated {#step-5-add-tracking-for-product-viewed-and-cart-updated-events}

#### Eventos de Product Viewed {#product-viewed-events}

1. Adicione esta função ao seu arquivo `Tracking.jsx`:

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
2. Para chamar a função anterior sempre que um usuário visitar uma página de produto, adicione um hook `useEffect` ao componente Product no arquivo `app/routes/products.$handle.jsx`:

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
3. Adicione o valor de "storefrontUrl" (porque ele não está no loader do componente por padrão):

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

#### Eventos de Cart Updated {#cart-updated-events}

{% multi_lang_include alerts/important_alerts.md alert='Shopify cart token alias' %}

1. Defina funções para rastrear o evento `cart_updated` e configurar o token do carrinho:

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
2. Retorne o objeto `cart` da ação do fetcher para que a Braze possa acessar suas propriedades, indo ao seu arquivo `app/routes/cart.jsx` e adicionando o seguinte à função `action`:

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

Para saber mais sobre os fetchers do Remix, consulte [useFetcher](https://remix.run/docs/ja/main/hooks/use-fetcher).

{: start="3"}
3. Lojas Hydrogen geralmente definem um componente `CartForm` que gerencia o estado do objeto do carrinho, que é usado ao adicionar, remover e alterar a quantidade de itens em um carrinho. Adicione outro hook `useEffect` no componente `AddToCartButton` que chamará a função `trackCartUpdated` sempre que o estado do fetcher do formulário mudar (sempre que o carrinho do usuário for atualizado):

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
4. Use a mesma `fetcherKey` para as ações responsáveis por atualizar um produto existente no seu carrinho. Adicione o seguinte aos componentes `CartLineRemoveButton` e `CartLineUpdateButton` (localizados por padrão no arquivo `app/components/CartLineItem.jsx`):

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

## Instalar a integração Braze Shopify {#install-the-braze-shopify-integration}

### Etapa 1: Conectar sua loja Shopify {#connect-your-shopify-store}

Acesse a página de parceiro Shopify para iniciar sua configuração. Primeiro, selecione **Begin Setup** para instalar o aplicativo da Braze na Shopify App Store. Siga as etapas guiadas para concluir o processo de instalação.

![Página de configuração da integração Shopify no dashboard da Braze.]({% image_buster /assets/img/shopify/braze_shopify_integration_page.png %})

### Etapa 2: Ativar os SDKs da Braze {#enable-braze-sdks}

Para lojas Shopify Hydrogen ou headless, selecione a opção **Custom setup**.

A configuração personalizada inclui um seletor de app do website. Selecione ou crie o app que alimenta sua loja virtual e, em seguida, copie a chave de API e o endpoint de SDK exibidos na etapa de integração. Para mais detalhes, consulte [Etapa 1: Selecionar um app do website e copiar as credenciais do SDK](#step-1).

Antes de continuar com o processo de integração, confirme que você adicionou o SDK da Braze ao seu website Shopify usando essas credenciais.

![Etapa de configuração para ativar os SDKs da Braze.]({% image_buster /assets/img/shopify/enable_braze_sdks_setup.png %})

### Etapa 3: Rastrear dados do Shopify {#step-3-track-shopify-data}

Melhore sua integração adicionando mais eventos e atributos do Shopify, que serão alimentados por webhooks do Shopify. Para informações detalhadas sobre os dados rastreados por essa integração, consulte [Recursos de dados do Shopify]({{site.baseurl}}/shopify_data_features).

![Etapa de configuração para rastrear dados do Shopify.]({% image_buster /assets/img/shopify/track_shopify_data_setup.png %})

### Etapa 4: Preenchimento de dados históricos (opcional) {#step-4-historical-backfill-optional}

Por meio da configuração personalizada, você pode incluir opcionalmente a mesma carga de dados históricos do Shopify que a [integração padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration#historical-backfill-setup): eventos de pedidos dos últimos 90 dias e perfis de usuário do último ano, cada um contado retroativamente a partir da data em que você concluir sua integração. Para incluir essa carga de dados inicial, marque a caixa de seleção da opção de carga de dados inicial.

Se você preferir fazer o preenchimento de dados históricos depois, pode concluir a configuração inicial agora e retornar a essa etapa em outro momento.

![Seção para configurar o preenchimento de dados históricos.]({% image_buster /assets/img/shopify/historical_backfill_setup.png %})

Para a lista completa de dados na carga inicial, o comportamento de relatórios de receita e o monitoramento da sincronização, consulte [Preenchimento de dados históricos]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features#historical-backfill).

### Etapa 5: Configuração de rastreamento de dados personalizados (avançado) {#step-5-custom-data-tracking-setup-advanced}

Com os SDKs da Braze, você pode rastrear eventos personalizados ou atributos personalizados que vão além dos dados suportados por essa integração. Eventos personalizados capturam interações únicas na sua loja, como:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table aria-label="Etapa 5: Configuração de rastreamento de dados personalizados (avançado)" style="width: 100%;">
  <caption>Etapa 5: Configuração de rastreamento de dados personalizados (avançado)</caption>
  <thead>
    <tr>
      <th style="width: 50%;">Eventos personalizados</th>
      <th style="width: 50%;">Atributos personalizados</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Usar um código de desconto personalizado</li>
          <li>Interagir com uma recomendação de produto personalizada</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marcas ou produtos favoritos</li>
          <li>Categorias de compra preferidas</li>
          <li>Status de membro ou de fidelidade</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

O SDK precisa ser inicializado (escutando atividades) no dispositivo do usuário para registrar eventos ou atributos personalizados. Para saber mais sobre o registro de dados personalizados, consulte [User object](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) e [logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

### Etapa 6: Configurar como você gerencia usuários (opcional) {#step-6}

Selecione o tipo de `external_id` no menu suspenso.

![Seção "Coletar inscritos".]({% image_buster /assets/img/shopify/external_id_standard.png %})

{% alert important %}
Usar um endereço de e-mail ou um endereço de e-mail com hash como seu ID externo na Braze pode ajudar a simplificar o gerenciamento de identidade em todas as suas fontes de dados. No entanto, é importante considerar os possíveis riscos à privacidade do usuário e à segurança dos dados.<br><br>

- **Informação previsível:** Endereços de e-mail são facilmente previsíveis, tornando-os vulneráveis a ataques.
- **Risco de exploração:** Se um usuário mal-intencionado alterar seu navegador web para enviar o endereço de e-mail de outra pessoa como seu ID externo, ele poderá acessar mensagens confidenciais ou informações da conta.
{% endalert %}

Por padrão, a Braze converte automaticamente os e-mails do Shopify para letras minúsculas antes de usá-los como ID externo. Se você estiver usando e-mail ou e-mail com hash como seu ID externo, confirme que seus endereços de e-mail também são convertidos para letras minúsculas antes de atribuí-los como seu ID externo ou antes de aplicar o hash a partir de outras fontes de dados. Isso ajuda a evitar discrepâncias nos IDs externos e a criação de perfis de usuário duplicados na Braze.

{% alert note %}
As próximas etapas dependem da sua seleção de ID externo:<br><br>
- **Se você selecionou um tipo de ID externo personalizado:** Conclua as etapas 6.1 a 6.3 para configurar seu ID externo personalizado.
- **Se você selecionou ID de cliente do Shopify, e-mail ou e-mail com hash:** Pule as etapas 6.1 a 6.3 e continue diretamente para a etapa 6.4.
{% endalert %}

#### Etapa 6.1: Criar o metacampo `braze.external_id` {#step-61-create-the-brazeexternal_id-metafield}

{% multi_lang_include partners/shopify/customer_metafield_definition_steps.md %}

Após a criação do metacampo, popule-o para seus clientes. Recomendamos as seguintes abordagens:

- **Escutar webhooks de criação de clientes:** Configure um webhook para escutar [eventos `customer/create`](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Isso permite que você grave o metacampo quando um novo cliente for criado.
- **Preencher dados de clientes existentes:** Use a [Admin API](https://shopify.dev/docs/api/admin-graphql) ou a [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para preencher o metacampo de clientes criados anteriormente.

#### Etapa 6.2: Criar um endpoint para recuperar seu ID externo {#step-62-create-an-endpoint-to-retrieve-your-external-id}

Você precisa criar um endpoint público que a Braze possa chamar para recuperar o ID externo. Isso permite que a Braze busque o ID em cenários onde o Shopify não pode fornecer o metacampo `braze.external_id` diretamente.

##### Especificações do endpoint {#endpoint-specifications}

**Método:** GET

A Braze envia os seguintes parâmetros para o seu endpoint:

| Parâmetro            | Obrigatório | Tipo de dados | Descrição                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | Sim      | String    | O ID de cliente do Shopify.                                         |
| shopify_storefront   | Sim      | String    | O nome da loja virtual para a solicitação. Ex: `<storefront_name>.myshopify.com` |
| email_address        | Não       | String    | O endereço de e-mail do usuário conectado. <br><br>Esse campo pode estar ausente em certos cenários de webhook. A lógica do seu endpoint deve considerar valores nulos aqui (por exemplo, buscar o e-mail usando o shopify_customer_id caso sua lógica interna o exija). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Especificações do endpoint" }

##### Exemplo de endpoint {#example-endpoint}

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@example.com&shopify_storefront=dev-store.myshopify.com
```


##### Resposta esperada {#expected-response}
A Braze espera um código de status `200` retornando o JSON do ID externo:
```json
{
  "external_id": "my_external_id"
}
```

##### Validação {#validation}

É fundamental validar que o `shopify_customer_id` e o `email_address` (se presente) correspondam aos valores do cliente no Shopify. Você pode usar a [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql) ou a [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para validar esses parâmetros e recuperar o metacampo `braze.external_id` correto.

##### Comportamento em caso de falha e mesclagem {#failure-behavior-and-merging}
Qualquer código de status diferente de `200` é considerado uma falha.

{% multi_lang_include partners/shopify/external_id_merge_implications.md %}

#### Etapa 6.3: Inserir seu ID externo {#step-63-input-your-external-id}

Repita a [Etapa 6](#step-6) e insira a URL do seu endpoint após selecionar ID externo personalizado como seu tipo de ID externo da Braze.

##### Considerações {#considerations}

{% multi_lang_include partners/shopify/external_id_generation_notes.md %}

#### Etapa 6.4: Coletar suas aceitações de e-mail ou SMS do Shopify (opcional) {#step-64-collect-your-email-or-sms-opt-ins-from-shopify-optional}

Você tem a opção de coletar suas aceitações de marketing por e-mail ou SMS do Shopify.

Se você utiliza os canais de e-mail ou SMS, pode sincronizar os estados de aceitação de marketing por e-mail e SMS com a Braze. Se você sincronizar as aceitações de marketing por e-mail do Shopify, a Braze criará automaticamente um grupo de inscrições para e-mail para todos os usuários associados a essa loja específica. Você precisa criar um nome exclusivo para esse grupo de inscrições.

![Seção "Coletar inscritos" com opção para coletar aceitações de marketing por e-mail ou SMS.]({% image_buster /assets/img/shopify/collect_email_subscribers.png %})

{% multi_lang_include partners/shopify/third_party_capture_form_note.md %}

### Etapa 7: Sincronizar produtos (opcional) {#step-7-sync-products-optional}

Você pode sincronizar todos os produtos da sua loja Shopify com um catálogo da Braze para uma personalização de mensagens mais profunda. As atualizações automáticas ocorrem em tempo quase real, então seu catálogo sempre reflete os detalhes mais recentes dos produtos. Para saber mais, confira [Sincronização de produtos do Shopify]({{site.baseurl}}/shopify_catalogs).

![Etapa de configuração para sincronizar dados de produtos com a Braze.]({% image_buster /assets/img/shopify/sync_product_data.png %})

### Etapa 8: Ativar canais {#step-8-activate-channels}

Para ativar In-App Messages, Content Cards e Feature Flags usando a integração direta do Shopify, adicione cada canal ao seu SDK. Siga os links da documentação fornecidos para cada canal:

- **In-App Messages:** Para ativar In-App Messages em casos de uso de formulários de captura de leads, consulte [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages).
- **Content Cards:** Para ativar Content Cards em casos de uso de caixa de entrada ou banners de website, consulte [Content Cards]({{site.baseurl}}/developer_guide/content_cards).
- **Feature Flags:** Para ativar Feature Flags em casos de uso de experimentação no site, consulte [Feature Flags]({{site.baseurl}}/developer_guide/feature_flags).

### Etapa 9: Concluir a configuração {#step-9-finish-setup}

Após concluir todas as etapas, selecione **Finish Setup** para retornar à página de parceiro. Em seguida, ative o app embed da Braze na sua página de administração do Shopify, conforme indicado pelo banner exibido.

![Banner informando para ativar o app embed da Braze no Shopify para concluir a configuração da integração.]({% image_buster /assets/img/shopify/shopify_app_embed_banner.png %})

#### Código de exemplo {#example-code}

[shopify-hydrogen-example](https://github.com/braze-inc/shopify-hydrogen-example/) é um app Hydrogen de exemplo que contém todo o código abordado nas etapas anteriores.