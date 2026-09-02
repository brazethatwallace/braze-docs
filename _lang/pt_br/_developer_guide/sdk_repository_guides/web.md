---
nav_title: Web SDK
article_title: Guia do repositório do Web SDK
page_order: 1
description: "Referência do README do Braze Web SDK espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do Web SDK {#web-sdk-repository-guide}

## Sobre o Braze Web SDK {#about-the-braze-web-sdk}

O Braze Web SDK permite integrar a plataforma de engajamento do cliente da Braze diretamente nos seus aplicativos web. Desenvolvido com TypeScript e projetado para o desenvolvimento web moderno, este SDK oferece ferramentas completas para gerenciamento de usuários, envio de mensagens, análise de dados e Feature Flags.

### O que você pode fazer {#what-you-can-do}

- **Gerenciamento de usuários**: Rastreie e gerencie identidades, atributos e comportamento dos usuários em todo o seu aplicativo web
- **In-App Messages**: Exiba mensagens e notificações direcionadas aos usuários enquanto eles estão usando seu site ativamente
- **Content Cards**: Mostre feeds de conteúdo personalizados e cartões promocionais que se atualizam em tempo real
- **Banners**: Exiba mensagens em formato de banner em posições específicas dentro do seu site
- **Notificações por push**: Envie notificações por push para a web para engajar usuários mesmo quando eles não estão no seu site
- **Feature Flags**: Controle o lançamento de recursos e testes A/B com gerenciamento de Feature Flags no lado do servidor
- **Análise de dados**: Rastreie eventos personalizados, interações de usuários e métricas de conversão
- **Gerenciamento de sessões**: Monitore sessões de usuários e padrões de engajamento

Seja para construir um aplicativo de página única, um site de e-commerce ou uma plataforma de conteúdo, o Braze Web SDK oferece as ferramentas necessárias para criar experiências de usuário personalizadas e envolventes que impulsionam o crescimento e a retenção.

## Pré-requisitos {#prerequisites}

Antes de integrar o Web Braze SDK, você precisará de:

- **Conta na Braze**: Uma conta na Braze com acesso à API
- **Chave de API**: A chave de API do seu app, disponível no dashboard da Braze
- **Endpoint de SDK**: A URL do seu endpoint de SDK da Braze (por exemplo, `sdk.iad-01.braze.com`)

### Obtendo suas credenciais {#getting-your-credentials}

1. **Chave de API**: Encontrada no dashboard da Braze em **Configurações** > **Chaves de API**
2. **Endpoint de SDK**: Localizado em **Configurações** > **Autenticação do SDK** > **Endpoints**
3. **Service Worker**: Necessário para notificações por push (consulte a seção Notificações por push)

## Instalação {#installation}

``` bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

## Início rápido {#quick-start}

O snippet a seguir mostra a configuração mínima necessária para inicializar o Braze Web SDK.

``` typescript
import * as braze from "@braze/web-sdk";

// Initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});

braze.changeUser('Jane Doe');
```

## Referência de configuração {#configuration-reference}

### Opções de inicialização {#initialization-options}

A função `initialize` aceita um objeto de opções com as seguintes propriedades:

| Opção | Tipo | Padrão | Descrição |
|--------|------|---------|-------------|
| `baseUrl` | `string` | **Obrigatório** | Esta opção é obrigatória para configurar o Braze Web SDK para usar o endpoint apropriado para a sua integração — por exemplo: `braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'sdk.iad-03.braze.com' })` |
| `enableLogging` | `boolean` | `false` | Defina como true para ativar o registro de log por padrão. Isso fará com que a Braze registre no console de javascript, que é visível para todos os usuários! É recomendável remover essa opção ou fornecer um logger alternativo com setLogger antes de publicar sua página em produção. |
| `allowUserSuppliedJavascript` | `boolean` | `false` | Por padrão, o Braze Web SDK não permite ações de clique em Javascript fornecidas pelo usuário, nem ativa mensagens no app em HTML e Banners, pois esses recursos permitem que os usuários do dashboard da Braze executem Javascript no seu site. Para indicar que você confia nos usuários do dashboard da Braze para escrever ações de clique em Javascript não maliciosas, defina esta propriedade como true. |
| `doNotLoadFontAwesome` | `boolean` | `false` | A Braze usa Font Awesome para ícones de mensagens no app. Por padrão, a Braze carregará automaticamente o FontAwesome 4.7.0 a partir da CDN do FontAwesome. Para desativar esse comportamento (por exemplo, porque seu site usa uma versão personalizada do FontAwesome), defina esta opção como `true`. Se você fizer isso, é sua responsabilidade garantir que o FontAwesome esteja carregado no seu site — caso contrário, as mensagens no app podem não ser exibidas corretamente. |
| `inAppMessageZIndex` | `number` | `999999` | Por padrão, o Braze SDK exibirá In-App Messages com um z-index de 999999. Forneça um valor para esta opção para substituir esse padrão. |
| `sessionTimeoutInSeconds` | `number` | `30` | Por padrão, uma sessão expira após 30 segundos de inatividade. Forneça um valor para esta opção para substituir esse padrão. |
| `deviceId` | `string` | Gerado automaticamente | Por padrão, a Braze atribui um guid aleatório como ID do dispositivo. Forneça um valor para esta opção de configuração para substituir esse padrão com um valor próprio. |
| `appVersion` | `string` | `undefined` | Se você fornecer um valor para esta opção, os eventos de usuário enviados à Braze serão associados à versão informada, que pode ser usada para segmentação de usuários. |
| `appVersionNumber` | `string` | `undefined` | Um valor numérico de versão do app que pode ser usado para segmentação de usuários. Esse valor deve ser enviado com quatro campos, como "1.2.3.4"; caso contrário, será ignorado. Nota: `appVersion` também deve ser definido, seja com o mesmo valor ou com um nome exclusivo para esta versão. |
| `contentSecurityNonce` | `string` | `undefined` | Se você fornecer um valor para esta opção, o Braze SDK adicionará o nonce a quaisquer elementos `<script>` e `<style>` criados pelo SDK. Isso pode ser usado para permitir que o Braze SDK funcione com a Content Security Policy do seu site. Além de definir este nonce, pode ser necessário permitir o carregamento do FontAwesome, o que pode ser feito adicionando `use.fontawesome.com` à lista de permissões da sua Content Security Policy ou usando a opção `doNotLoadFontAwesome` e carregando-o manualmente. |
| `noCookies` | `boolean` | `false` | Por padrão, o Braze Web SDK usa cookies. Para desativar o uso de cookies, defina esta opção como true. A desativação de cookies pode afetar a capacidade do SDK de lembrar a identidade dos usuários entre sessões. |
| `allowCrawlerActivity` | `boolean` | `false` | Por padrão, o Braze Web SDK ignora atividades de spiders ou web crawlers conhecidos, como o Google, com base na string de user agent. Isso economiza pontos de dados, torna a análise de dados mais precisa e pode melhorar o ranking da página. No entanto, se você quiser que a Braze registre a atividade desses crawlers, pode definir esta opção como true. |
| `disablePushTokenMaintenance` | `boolean` | `false` | Por padrão, os usuários que já concederam permissão de push para a web (por exemplo, por meio de requestPushPermission ou de um provedor de push anterior) sincronizarão seu token por push com o backend da Braze automaticamente em novas sessões para garantir a entregabilidade. Para desativar esse comportamento, defina esta opção como true. |
| `enableSdkAuthentication` | `boolean` | `false` | Defina como true para ativar o recurso de autenticação do SDK. Para saber mais sobre a autenticação do SDK, consulte nossa documentação do produto. |
| `manageServiceWorkerExternally` | `boolean` | `false` | Por padrão, o Braze Web SDK gerencia seu próprio service worker para notificações por push. Se você já gerencia um service worker na sua aplicação e deseja incorporar a funcionalidade do service worker da Braze a ele, defina esta opção como true e inclua o código do service worker da Braze no seu arquivo de service worker. |
| `minimumIntervalBetweenTriggerActionsInSeconds` | `number` | `30` | Por padrão, ações-gatilho (por exemplo, exibir uma mensagem no app) podem ser disparadas no máximo uma vez a cada 30 segundos por usuário. Forneça um valor para esta opção para substituir esse padrão. |
| `serviceWorkerLocation` | `string` | `undefined` | Por padrão, o Braze Web SDK procurará o arquivo do service worker na raiz do seu domínio. Forneça um valor para esta opção para substituir esse padrão e especificar um local personalizado para o arquivo do service worker. |
| `safariWebsitePushId` | `string` | `undefined` | Obrigatório para notificações por push no Safari. Esse valor pode ser encontrado na sua conta Apple Developer. Para saber mais sobre a configuração de notificações por push no Safari, consulte nossa documentação do produto. |
| `localization` | `string` | `undefined` | Se você fornecer um valor para esta opção, o Braze SDK tentará exibir mensagens no app e Content Cards no idioma especificado. |
| `openInAppMessagesInNewTab` | `boolean` | `false` | Por padrão, links em mensagens no app abrem na mesma aba. Defina esta opção como true para que eles abram em uma nova aba. |
| `openCardsInNewTab` | `boolean` | `false` | Por padrão, links em Content Cards abrem na mesma aba. Defina esta opção como true para que eles abram em uma nova aba. |
| `requireExplicitInAppMessageDismissal` | `boolean` | `false` | Por padrão, mensagens no app podem ser fechadas clicando fora delas ou pressionando a tecla Escape. Defina esta opção como true para exigir que os usuários cliquem explicitamente em um botão de fechar ou em um botão de ação para dispensar a mensagem. |
| `devicePropertyAllowlist` | `string[]` | `undefined` | Por padrão, o Braze SDK detecta e coleta automaticamente todas as propriedades de dispositivo em DeviceProperties. Para substituir esse comportamento, forneça um array de DeviceProperties. Para desativar o envio de todas as propriedades aos servidores da Braze, forneça um array vazio. Sem algumas propriedades, nem todos os recursos funcionarão corretamente. Por exemplo, sem o fuso horário, a entrega com base no fuso local não funcionará. |
| `serviceWorkerScope` | `string` | `undefined` | Por padrão, o Braze Web SDK registrará seu service worker com o escopo padrão (o diretório do service worker). Forneça um valor para esta opção para substituir esse padrão e especificar um escopo personalizado para o service worker. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Opções de inicialização" }

---

## Recursos principais {#core-features}

### Inicialização e configuração {#initialization-setup}

#### Inicialização básica {#basic-initialization}

``` typescript
import * as braze from "@braze/web-sdk";

// Initialize the SDK
braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: 'YOUR-SDK-ENDPOINT-HERE',
    enableLogging: true // Remove in production
});

// Start a session
braze.openSession();
```

#### Opções avançadas de inicialização {#advanced-initialization-options}

``` typescript
import * as braze from "@braze/web-sdk";

braze.initialize('YOUR-API-KEY-HERE', {
    baseUrl: 'YOUR-SDK-ENDPOINT-HERE',
    enableLogging: true,
    allowUserSuppliedJavascript: true,
    doNotLoadFontAwesome: false,
    inAppMessageZIndex: 999999,
    sessionTimeoutInSeconds: 30,
    deviceId: 'custom-device-id',
    appVersion: '1.0.0',
    contentSecurityNonce: 'your-nonce-here'
});
```

### Gerenciamento de usuários {#user-management}

#### Alterar usuário {#change-user}

``` typescript
import { changeUser } from "@braze/web-sdk";

// Change to a new user
changeUser('user-123');
```

#### Definir atributos do usuário {#set-user-attributes}

``` typescript
import { getUser } from "@braze/web-sdk";

const user = getUser();
if (user) {
    user.setEmail('user@example.com');
    user.setFirstName('John');
    user.setLastName('Doe');
    user.setCustomUserAttribute('subscription_tier', 'premium');
    user.setCustomUserAttribute('last_login', new Date());
}
```

#### Definir localização do usuário {#set-user-location}

``` typescript
import { getUser } from "@braze/web-sdk";

const user = getUser();
if (user) {
    user.setCountry('US');
    user.setHomeCity('San Francisco');
    user.setLanguage('en');
    user.setCustomLocationAttribute('latitude', 37.7749);
    user.setCustomLocationAttribute('longitude', -122.4194);
}
```

#### Aliases de usuário e grupos de inscrições {#user-aliases-and-subscription-groups}

``` typescript
import { getUser } from "@braze/web-sdk";

const user = getUser();
if (user) {
    // Add alias
    user.addAlias('external_id', '12345');

    // Add to subscription group
    user.addToSubscriptionGroup('newsletter_subscribers');

    // Remove from subscription group
    user.removeFromSubscriptionGroup('old_subscribers');
}
```

#### Logout do usuário {#user-logout}

``` typescript
import { wipeData } from "@braze/web-sdk";

// There is no explicit method to logout. To "forget" the current users entirely, use wipeData().
// This is a complete data wipe (use with caution, this wipes things such as device ID)
wipeData();
```

### Mensagens no app {#in-app-messages}

#### Exibição automática {#automatic-display}

``` typescript
import { automaticallyShowInAppMessages } from "@braze/web-sdk";

// Automatically show in-app messages
automaticallyShowInAppMessages();
```

#### Exibição manual {#manual-display}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

// Subscribe to in-app messages
subscribeToInAppMessage((inAppMessage) => {
    // Show the message
    showInAppMessage(inAppMessage);
});
```

#### Tratamento personalizado de mensagens no app {#custom-in-app-message-handling}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

subscribeToInAppMessage((inAppMessage) => {
    // Custom logic before showing
    if (inAppMessage.getExtras()['priority'] === 'high') {
        showInAppMessage(inAppMessage);
    }
});
```

#### Registrar interações com mensagens no app {#log-in-app-message-interactions}

``` typescript
import {
    logInAppMessageClick,
    logInAppMessageImpression,
    logInAppMessageButtonClick
} from "@braze/web-sdk";

// Log when user sees the message
logInAppMessageImpression(inAppMessage);

// Log when user clicks the message
logInAppMessageClick(inAppMessage);

// Log when user clicks a button in the message
logInAppMessageButtonClick(inAppMessage, button);
```

#### Mensagens no app com HTML personalizado {#custom-html-in-app-messages}

``` typescript
import { subscribeToInAppMessage, logInAppMessageImpression, logInAppMessageClick } from "@braze/web-sdk";

// Don't call automaticallyShowInAppMessages() when using custom rendering
// braze.automaticallyShowInAppMessages(); // Comment this out

subscribeToInAppMessage((inAppMessage) => {
    // Extract message data
    const messageData = {
        title: inAppMessage.getMessage(),
        body: inAppMessage.getBody(),
        imageUrl: inAppMessage.getImageUrl(),
        buttons: inAppMessage.getButtons(),
        deepLink: inAppMessage.getExtras()['deep_link_url']
    };

    // Define your own HTML structure, using messageData
    const customHTML = ` <!-- Add your custom styling and structure -->`;

    /* Render the In-App Message here */

    // Here we naively log an impression once the message is rendered.
    // Be precise about exactly when you want to log an impression (ie. only the first time it enters the view port).
    logInAppMessageImpression(inAppMessage);
});

// Handle button clicks and deep linking
const handleButtonClick = (button, inAppMessage) => {
    logInAppMessageClick(inAppMessage);
    // Handle additional click actions (ie. deep linking)
};
```

### Content Cards

#### Exibir Content Cards {#display-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show content cards in default location
showContentCards();

// Show in specific container
const container = document.getElementById('content-cards-container');
showContentCards(container);
```

#### Assinar atualizações de Content Cards {#subscribe-to-content-cards-updates}

``` typescript
import { subscribeToContentCardsUpdates } from "@braze/web-sdk";

subscribeToContentCardsUpdates((cards) => {
    console.log('Content cards updated:', cards);
    // Display cards or update UI
});
```

#### Registrar interações com Content Cards {#log-content-card-interactions}

``` typescript
import {
    logContentCardClick,
    logContentCardImpressions,
    logCardDismissal
} from "@braze/web-sdk";

// Log card impressions
logContentCardImpressions(cards);

// Log card clicks
logContentCardClick(card);

// Log card dismissals
logCardDismissal(card);
```

#### Filtrar Content Cards {#filter-content-cards}

``` typescript
import { showContentCards } from "@braze/web-sdk";

// Show only pinned cards
// You can also provide a parent element instead of null
showContentCards(null, (cards) => {
    return cards.filter(card => card.getIsPinned());
});
```

#### Solicitar atualização de Content Cards {#request-content-cards-refresh}

``` typescript
import { requestContentCardsRefresh } from "@braze/web-sdk";

requestContentCardsRefresh(
    () => console.log('Content cards refreshed'),
    () => console.log('Failed to refresh content cards')
);
```

#### Content Cards personalizados {#custom-content-cards}

``` typescript
import { subscribeToContentCardsUpdates, logContentCardClick, logContentCardImpressions, requestContentCardsRefresh } from "@braze/web-sdk";

// State for impression de-duping
const loggedImpressions = new Set();
const idToCard = new Map();

subscribeToContentCardsUpdates((cards) => {
    // Build cards one by one
    cards.getCards().forEach(card => {
        // Skip control cards
        if (card.getIsControl()) return;

        // Extract card data
        const cardData = {
            id: card.getId(),
            title: card.getTitle(),
            description: card.getDescription(),
            imageUrl: card.getImageUrl(),
            url: card.getUrl(),
            extras: card.getExtras()
        };

        // Define your own HTML structure, using cardData
        const customHTML = ` <!-- Add your custom styling and structure -->`;

        /* Render each card here */

        // Basic observer for impression logging.
        // Be precise about exactly when you want to log an impression (ie. only the first time it enters the view port).
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    logContentCardImpressions([card]);
                }
            });
        });

        // Observe card element when rendered
        // observer.observe(cardElement);
    });
});

// Handle card clicks
const handleCardClick = (card) => {
    logContentCardClick(card);
    // Handle additional click actions (ie. navigation)
};

```

### Notificações por push {#push-notifications}

#### Solicitar permissão de push {#request-push-permission}

``` typescript
import { requestPushPermission } from "@braze/web-sdk";

requestPushPermission(
    () => console.log('Push permission granted'),
    () => console.log('Push permission denied')
);
```

#### Verificar suporte a push {#check-push-support}

``` typescript
import { isPushSupported, isPushPermissionGranted } from "@braze/web-sdk";

if (isPushSupported()) {
    if (isPushPermissionGranted()) {
        console.log('Push notifications are enabled');
    } else {
        console.log('Push permission not granted');
    }
}
```

#### Cancelar registro de push {#unregister-push}

``` typescript
import { unregisterPush } from "@braze/web-sdk";

unregisterPush(
    () => console.log('Successfully unregistered'),
    () => console.log('Failed to unregister')
);
```

### Feature Flags {#feature-flags}

#### Obter Feature Flag {#get-feature-flag}

``` typescript
import { getFeatureFlag } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_checkout_flow');
if (featureFlag) {
    const isEnabled = featureFlag.getBooleanProperty('enabled', false);
    const rolloutPercentage = featureFlag.getNumberProperty('rollout_percentage', 0);

    if (isEnabled) {
        // Enable new checkout flow
    }
}
```

#### Assinar atualizações de Feature Flags {#subscribe-to-feature-flag-updates}

``` typescript
import { subscribeToFeatureFlagsUpdates } from "@braze/web-sdk";

subscribeToFeatureFlagsUpdates((featureFlags) => {
    featureFlags.forEach(flag => {
        console.log(`Feature flag ${flag.getId()}: ${flag.getBooleanProperty('enabled')}`);
    });
});
```

#### Registrar impressões de Feature Flags {#log-feature-flag-impressions}

``` typescript
import { logFeatureFlagImpression } from "@braze/web-sdk";

const featureFlag = getFeatureFlag('new_feature');
if (featureFlag) {
    logFeatureFlagImpression(featureFlag);
}
```

#### Solicitar atualização de Feature Flags {#request-feature-flags-refresh}

``` typescript
import { refreshFeatureFlags } from "@braze/web-sdk";

refreshFeatureFlags(
    () => console.log('Feature flags refreshed'),
    () => console.log('Failed to refresh feature flags')
);
```

### Banners {#banners}

#### Obter e exibir banners {#get-and-display-banners}

``` typescript
import { getBanner, insertBanner } from "@braze/web-sdk";

const banner = getBanner('homepage_banner');
if (banner) {
    // Insert banner into specific element
    const container = document.getElementById('banner-container');
    insertBanner(banner, container);
}
```

#### Assinar atualizações de banners {#subscribe-to-banner-updates}

``` typescript
import { insertBanner, subscribeToBannersUpdates } from "@braze/web-sdk";

subscribeToBannersUpdates((banners) => {
    Object.entries(banners).forEach(([placementId, banner]) => {
        if (banner) {
            console.log(`Banner for ${placementId}:`, banner);

            // Insert banner into specific element
            const container = document.getElementById(`banner-container-${placementId}`);
            insertBanner(banner, container);
        }
    });
});
```

#### Descartar banners em uma UI personalizada {#dismiss-banners-in-a-custom-ui}

``` typescript
import { dismissBanner, getBanner, subscribeToBannersUpdates } from "@braze/web-sdk";

subscribeToBannersUpdates((banners) => {
    const banner = getBanner("homepage_banner");
    const container = document.getElementById("custom-banner-container");
    if (!container) {
        return;
    }

    if (!banner) {
        container.replaceChildren();
        return;
    }

    banner.subscribeToDismissedEvent(() => {
        console.log("Dismissed banner:", banner);
    });

    const closeButton = document.createElement("button");
    closeButton.textContent = "Close";
    closeButton.addEventListener("click", () => {
        dismissBanner(banner);
    });

    // Render your custom UI here and include the close button.
});
```

Quando você chama `dismissBanner(banner)`, o SDK gerencia o estado de descarte do banner, remove o banner das atualizações ativas de banners, notifica os assinantes do evento de descarte do banner e sincroniza o descarte com a Braze. UIs personalizadas devem usar `subscribeToBannersUpdates` para reagir à remoção do banner descartado, em vez de tratar `dismissBanner` apenas como uma alteração local de UI ou apenas como um método de registro de análise de dados.

#### Solicitar atualização de banners {#request-banner-refresh}

``` typescript
import { requestBannersRefresh } from "@braze/web-sdk";

requestBannersRefresh(
    ["placement_1", "placement_2"],
    () => console.log('Banners refreshed'),
    () => console.log('Failed to refresh banners')
);
```

### Análise de dados e eventos {#analytics-events}

#### Registrar eventos personalizados {#log-custom-events}

``` typescript
import { logCustomEvent } from "@braze/web-sdk";

// Simple event
logCustomEvent('button_clicked');

// Event with properties
logCustomEvent('purchase', {
    product_id: '123',
    price: 29.99,
    currency: 'USD'
});
```

#### Registrar compras {#log-purchases}

``` typescript
import { logPurchase } from "@braze/web-sdk";

logPurchase('product-123', 29.99, 'USD', 1, {
    category: 'electronics',
    brand: 'Apple'
});
```

#### Solicitar envio imediato de dados {#request-data-flush}

``` typescript
import { requestImmediateDataFlush } from "@braze/web-sdk";

// Force immediate data send
requestImmediateDataFlush();
```

### Gerenciamento de sessão {#session-management}

#### Abrir sessão {#open-session}

``` typescript
import { openSession } from "@braze/web-sdk";

// Start a new session
openSession();
```

#### Verificar status do SDK {#check-sdk-status}

``` typescript
import { isInitialized, isDisabled } from "@braze/web-sdk";

if (isInitialized()) {
    console.log('SDK is initialized');

    if (isDisabled()) {
        console.log('SDK is disabled');
    }
}
```

#### Ativar/desativar SDK {#enabledisable-sdk}

``` typescript
import { enableSDK, disableSDK } from "@braze/web-sdk";

// Disable SDK
disableSDK();

// Re-enable SDK
enableSDK();
```

### Gerenciamento de dados {#data-management}

#### Limpar dados {#wipe-data}

``` typescript
import { wipeData } from "@braze/web-sdk";

// Remove all locally stored data
wipeData();
```

#### Destruir SDK {#destroy-sdk}

``` typescript
import { destroy } from "@braze/web-sdk";

// Clean up SDK resources
destroy();
```

#### Obter ID do dispositivo {#get-device-id}

``` typescript
import { getDeviceId } from "@braze/web-sdk";

const deviceId = getDeviceId();
console.log('Device ID:', deviceId);
```

#### Autenticação do SDK {#sdk-authentication}

``` typescript
import { setSdkAuthenticationSignature } from "@braze/web-sdk";

// Set authentication signature
setSdkAuthenticationSignature('your-signature-here');
```

#### Assinar falhas de autenticação {#subscribe-to-authentication-failures}

``` typescript
import { subscribeToSdkAuthenticationFailures } from "@braze/web-sdk";

subscribeToSdkAuthenticationFailures((error) => {
    console.log('Authentication failed:', error);
    // Provide new signature
    setSdkAuthenticationSignature('new-signature');
});
```

---

## Padrões de integração {#integration-patterns}

### Frameworks SSR {#ssr-frameworks}

Se você usa um framework de renderização do lado do servidor (SSR), como o Next.js, pode encontrar erros porque o SDK foi projetado para ser executado em um ambiente de navegador. Você pode resolver esses problemas importando o SDK dinamicamente.

Você pode manter os benefícios do tree-shaking ao exportar as partes do SDK de que precisa em um arquivo separado e, em seguida, importar esse arquivo dinamicamente no seu componente.

``` javascript
// MyComponent/braze-exports.js
// export the parts of the SDK you need here
export { initialize, openSession } from "@braze/web-sdk";

// MyComponent/MyComponent.js
// import the functions you need from the braze exports file
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

Como alternativa, se você usa o webpack para empacotar seu app, pode aproveitar os comentários mágicos para importar dinamicamente apenas as partes do SDK de que precisa.

``` javascript
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

### Vite

Se você usa o Vite e vê um aviso sobre dependências circulares ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, pode ser necessário excluir o SDK da Braze da descoberta de dependências:

``` javascript
export default {
    optimizeDeps: {
        exclude: ['@braze/web-sdk']
    }
}
```

### Framework Jest {#jest-framework}

Ao usar o Jest, você pode ver um erro semelhante a `SyntaxError: Unexpected token 'export'`. Para corrigir isso, ajuste sua configuração no `package.json` para ignorar o SDK da Braze:

``` json
{
  "jest": {
    "transformIgnorePatterns": [
      "/node_modules/(?!@braze)"
    ]
  }
}
```

### Definição de módulo assíncrono (AMD) {#asynchronous-module-definition-amd}

#### Desativar suporte a AMD {#disable-amd-support}

Se o seu site usa o RequireJS ou outro carregador de módulo AMD, mas você prefere carregar o SDK Web da Braze pela CDN, é possível carregar uma versão da biblioteca que não inclui suporte a AMD. Essa versão da biblioteca pode ser carregada pelo endereço da CDN: `https://js.appboycdn.com/web-sdk/6.3/braze.no-amd.min.js`

#### Carregador de módulo {#module-loader}

Se você usa o RequireJS ou outros carregadores de módulo AMD, recomendamos hospedar uma cópia da nossa biblioteca por conta própria e referenciá-la como faria com outros recursos:

``` javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Accelerated Mobile Pages (AMP) (AMP) {#accelerated-mobile-pages-amp}

Para a integração com AMP, será necessário:

1. **Incluir o script de web push para AMP**: adicione a tag de script assíncrono ao head.
2. **Adicionar widgets de inscrição**: adicione widgets para permitir que os usuários se inscrevam/cancelem a inscrição.
3. **Adicionar arquivos auxiliares**: inclua `helper-iframe.html` e `permission-dialog.html`.
4. **Criar service worker**: adicione o arquivo de service worker da Braze.
5. **Configurar o elemento amp-web-push**: adicione o elemento `amp-web-push` com sua chave de API e URL base como parâmetros de consulta.

Para instruções detalhadas de integração com AMP, consulte o [guia do desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web#amp).

### Electron

O Electron não oferece suporte oficial a notificações por push para a web (veja esta [issue no GitHub](https://github.com/electron/electron/issues/6697)). Existem outras [soluções alternativas de código aberto](https://github.com/MatthieuLemoine/electron-push-receiver) que você pode testar, mas que não foram validadas pela Braze.

### Integração via CDN {#cdn-integration}

- **Carregamento do script**: inicialize após o carregamento da tag de script, colocando o código de inicialização depois da tag, ou use o manipulador de evento `onload` da tag de script.
- **Acesso global**: o SDK fica disponível como `window.braze` quando carregado via CDN.

### Service worker (notificações por push) {#service-worker-push-notifications}

- **Obrigatório**: é necessário incluir o service worker da Braze para que as notificações por push funcionem.
- **Registro padrão**: por padrão, o SDK Web da Braze registra e gerencia seu service worker automaticamente quando `requestPushPermission()` é chamado, assim como no início de cada nova sessão para usuários que já concederam permissão de push. Você ainda precisa hospedar um arquivo de service worker no local esperado, contendo o código do service worker da Braze.
- **Gerenciar seu próprio service worker**: se você já gerencia um service worker no seu aplicativo, defina a opção de inicialização `manageServiceWorkerExternally` como `true`, adicione o código do service worker da Braze ao seu arquivo de service worker e registre-o manualmente usando `navigator.serviceWorker.register()`.
- **Permissões de push**: chame `braze.requestPushPermission()` em resposta a interações do usuário (por exemplo, cliques em botões). Use solicitações suaves de push (interface personalizada) antes de solicitar a permissão do navegador.

### Gerenciadores de tags {#tag-managers}

#### Tealium iQ

O Tealium iQ oferece uma integração básica e pronta com a Braze. Para configurar a integração, pesquise por Braze na interface de gerenciamento de tags do Tealium e forneça a chave de API do SDK Web do seu dashboard. Para mais detalhes ou suporte aprofundado de configuração do Tealium, consulte nossa [documentação de integração](https://www.braze.com/docs/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou entre em contato com o gerente de contas do Tealium.

#### Google Tag Manager

O SDK Web pode ser inicializado e chamado a partir de uma tag HTML personalizada no seu contêiner do Google Tag Manager. Confira nosso [app de exemplo para Google Tag Manager](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/google-tag-manager) para ver um exemplo de envio de eventos para a Braze via GTM, ou consulte nossa [documentação de integração](https://www.braze.com/docs/developer_guide/sdk_integration/google_tag_manager) para mais detalhes.

#### Outros gerenciadores de tags {#other-tag-managers}

A Braze também pode ser compatível com outras soluções de gerenciamento de tags seguindo nossas instruções de integração dentro de uma tag HTML personalizada. Entre em contato com um representante da Braze se precisar de ajuda para avaliar essas soluções.

---

## Bibliotecas {#libraries}

A tabela a seguir descreve as distribuições disponíveis do Braze Web SDK.

| Nome | Descrição | npm | URL do CDN
| ---- | ----------- | --- | -------
| Full | SDK completo com interface. Ao usar a versão npm, os bundlers JavaScript removem código não utilizado, incluindo código de interface. | `@braze/web-sdk` | https://js.appboycdn.com/web-sdk/6.11/braze.min.js
| Core | Contém o SDK sem interface. Implemente sua própria interface para In-App Messages e Content Cards ao usar esta versão do SDK. Use a biblioteca completa para a maioria das integrações, pois ela fornece elementos de interface personalizáveis por CSS. | N/A | https://js.appboycdn.com/web-sdk/6.11/braze.core.min.js
| No-AMD | Contém o SDK completo sem suporte a AMD. Isso é útil se o seu site usa RequireJS ou outro carregador de módulos AMD, mas você prefere carregar o SDK pelo CDN. | N/A | https://js.appboycdn.com/web-sdk/6.11/braze.no-amd.min.js
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bibliotecas" }

## Navegadores compatíveis {#supported-browsers}

- Navegadores modernos baseados em Chromium (Chrome, Edge, Opera)
- Firefox
- Safari

## Depuração e solução de problemas {#debugging-troubleshooting}

Passe a opção `enableLogging: true` para a função de inicialização (`braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT', enableLogging: true });`) para fazer a Braze registrar logs no console do JavaScript. Isso é útil durante o desenvolvimento, mas fica visível para todos os usuários. Portanto, remova essa opção ou [forneça um logger alternativo](https://js.appboycdn.com/web-sdk/6.11/doc/modules/braze.html#setlogger) antes de publicar sua página em produção.

## Font Awesome

A Braze usa [Font Awesome](http://fortawesome.github.io/Font-Awesome/) 4.7.0 para ícones de mensagens no app. Para desativar o carregamento do Font Awesome, use a opção de inicialização `doNotLoadFontAwesome`. Confira a [folha de referência](http://fortawesome.github.io/Font-Awesome/cheatsheet/) para ver os ícones disponíveis.

## Recursos adicionais {#additional-resources}

- [Guia do desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web)
- [Documentação do SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)
- [Exemplos de compilação](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/)

## Contato {#contact}

Em caso de dúvidas, entre em contato com o suporte técnico da Braze para obter assistência.
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-web-sdk](https://github.com/braze-inc/braze-web-sdk).