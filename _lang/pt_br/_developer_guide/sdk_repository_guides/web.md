---
nav_title: Web SDK
article_title: Guia do repositório do Web SDK
page_order: 1
description: "Referência do README do Braze Web SDK espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do Web SDK {#web-sdk-repository-guide}

## Sobre o Braze Web SDK {#about-the-braze-web-sdk}

O Braze Web SDK permite integrar a plataforma de engajamento com clientes da Braze diretamente nos seus aplicativos web. Desenvolvido com TypeScript e projetado para o desenvolvimento web moderno, este SDK oferece ferramentas abrangentes para gerenciamento de usuários, envio de mensagens, análise de dados e Feature Flags.

### O que você pode fazer {#what-you-can-do}

- **Gerenciamento de usuários**: Rastreie e gerencie identidades, atributos e comportamentos de usuários em todo o seu aplicativo web
- **In-App Messages**: Exiba mensagens e notificações direcionadas aos usuários enquanto eles estão usando ativamente o seu site
- **Content Cards**: Mostre feeds de conteúdo personalizados e cartões promocionais que se atualizam em tempo real
- **Banners**: Exiba mensagens em formato de banner em posicionamentos específicos dentro do seu site
- **Notificações por push**: Envie notificações por push para a web para engajar os usuários mesmo quando eles não estão no seu site
- **Feature Flags**: Controle lançamentos de recursos e testes A/B com gerenciamento de Feature Flags no lado do servidor
- **Análise de dados**: Rastreie eventos personalizados, interações de usuários e métricas de conversão
- **Gerenciamento de sessões**: Monitore sessões de usuários e padrões de engajamento

Seja para construir um aplicativo de página única, um site de e-commerce ou uma plataforma de conteúdo, o Braze Web SDK oferece as ferramentas necessárias para criar experiências de usuário personalizadas e envolventes que impulsionam o crescimento e a retenção.

## Pré-requisitos {#prerequisites}

Antes de integrar o Braze Web SDK, você precisará de:

{% multi_lang_include developer_guide/sdk_api_prerequisites.md %}

### Obtendo suas credenciais {#getting-your-credentials}

1. **Chave de API**: Encontrada no dashboard da Braze em **Configurações** > **Chaves de API**
2. **Endpoint do SDK**: Localizado em **Configurações** > **Autenticação do SDK** > **Endpoints**
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
|-------|------|--------|-----------|
| `baseUrl` | `string` | **Obrigatória** | Esta opção é obrigatória para configurar o Braze Web SDK para usar o endpoint apropriado para a sua integração — por exemplo: `braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'sdk.iad-03.braze.com' })` |
| `enableLogging` | `boolean` | `false` | Defina como true para ativar o registro por padrão. Isso fará com que a Braze registre no console JavaScript, que é visível para todos os usuários! Você provavelmente deve remover isso ou fornecer um logger alternativo com setLogger antes de lançar sua página em produção. |
| `allowUserSuppliedJavascript` | `boolean` | `false` | Por padrão, o Braze Web SDK não permite ações de clique em Javascript fornecidas pelo usuário, nem ativa mensagens no app em HTML e Banners, pois eles permitem que usuários do dashboard da Braze executem Javascript no seu site. Para indicar que você confia nos usuários do dashboard da Braze para escrever ações de clique em Javascript não maliciosas, defina esta propriedade como true. |
| `doNotLoadFontAwesome` | `boolean` | `false` | A Braze usa Font Awesome para ícones de mensagens no app. Por padrão, a Braze carregará automaticamente o FontAwesome 4.7.0 do CDN do FontAwesome. Para desativar esse comportamento (por exemplo, porque seu site usa uma versão personalizada do FontAwesome), defina esta opção como `true`. Se fizer isso, você é responsável por garantir que o FontAwesome esteja carregado no seu site — caso contrário, as mensagens no app podem não ser renderizadas corretamente. |
| `inAppMessageZIndex` | `number` | `999999` | Por padrão, o Braze SDK exibirá In-App Messages com um z-index de 999999. Forneça um valor para esta opção para substituir esse padrão. |
| `sessionTimeoutInSeconds` | `number` | `30` | Por padrão, uma sessão expira após 30 segundos de inatividade. Forneça um valor para esta opção para substituir esse padrão. |
| `deviceId` | `string` | Gerado automaticamente | Por padrão, a Braze atribuirá um guid aleatório como ID do dispositivo. Forneça um valor para esta opção de configuração para substituir esse padrão com um valor próprio. |
| `appVersion` | `string` | `undefined` | Se você fornecer um valor para esta opção, os eventos de usuário enviados à Braze serão associados à versão fornecida, que pode ser usada para segmentação de usuários. |
| `appVersionNumber` | `string` | `undefined` | Um valor numérico de versão do app que pode ser usado para segmentação de usuários. Este valor deve ser enviado com quatro campos, como "1.2.3.4", caso contrário será ignorado. Nota: `appVersion` também deve ser definido, com o mesmo valor ou um nome exclusivo para esta versão. |
| `contentSecurityNonce` | `string` | `undefined` | Se você fornecer um valor para esta opção, o Braze SDK adicionará o nonce a qualquer elemento `<script>` e `<style>` criado pelo SDK. Isso pode ser usado para permitir que o Braze SDK funcione com a Política de Segurança de Conteúdo do seu site. Além de definir este nonce, você também pode precisar permitir o carregamento do FontAwesome, o que pode ser feito adicionando `use.fontawesome.com` à lista de permissões da sua Política de Segurança de Conteúdo ou usando a opção `doNotLoadFontAwesome` e carregando-o manualmente. |
| `noCookies` | `boolean` | `false` | Por padrão, o Braze Web SDK usa cookies. Para desativar o uso de cookies, defina esta opção como true. A desativação de cookies pode afetar a capacidade do SDK de lembrar as identidades dos usuários entre sessões. |
| `allowCrawlerActivity` | `boolean` | `false` | Por padrão, o Braze Web SDK ignora atividades de spiders ou web crawlers conhecidos, como o Google, com base na string do user agent. Isso economiza pontos de dados, torna a análise de dados mais precisa e pode melhorar o ranking da página. No entanto, se você quiser que a Braze registre a atividade desses crawlers, defina esta opção como true. |
| `disablePushTokenMaintenance` | `boolean` | `false` | Por padrão, usuários que já concederam permissão de push para a web (por exemplo, por meio de requestPushPermission ou de um provedor de push anterior) sincronizarão seu token de push com o backend da Braze automaticamente em novas sessões para garantir a entregabilidade. Para desativar esse comportamento, defina esta opção como true. |
| `enableSdkAuthentication` | `boolean` | `false` | Defina como true para ativar o recurso de autenticação do SDK. Para mais informações sobre autenticação do SDK, consulte nossa documentação do produto. |
| `manageServiceWorkerExternally` | `boolean` | `false` | Por padrão, o Braze Web SDK gerencia seu próprio service worker para notificações por push. Se você já gerencia um service worker no seu aplicativo e deseja incorporar a funcionalidade do service worker da Braze nele, defina esta opção como true e inclua o código do service worker da Braze no seu arquivo de service worker. |
| `minimumIntervalBetweenTriggerActionsInSeconds` | `number` | `30` | Por padrão, ações-gatilho (por exemplo, exibir uma mensagem no app) podem ser disparadas no máximo uma vez a cada 30 segundos por usuário. Forneça um valor para esta opção para substituir esse padrão. |
| `serviceWorkerLocation` | `string` | `undefined` | Por padrão, o Braze Web SDK procurará seu arquivo de service worker na raiz do seu domínio. Forneça um valor para esta opção para substituir esse padrão e especificar um local personalizado para o arquivo de service worker. |
| `safariWebsitePushId` | `string` | `undefined` | Obrigatório para notificações por push no Safari. Este valor pode ser encontrado na sua conta Apple Developer. Para mais informações sobre como configurar notificações por push no Safari, consulte nossa documentação do produto. |
| `localization` | `string` | `undefined` | Se você fornecer um valor para esta opção, o Braze SDK tentará exibir mensagens no app e Content Cards nesse idioma. |
| `openInAppMessagesInNewTab` | `boolean` | `false` | Por padrão, links em mensagens no app abrem na mesma aba. Defina esta opção como true para que abram em uma nova aba. |
| `openCardsInNewTab` | `boolean` | `false` | Por padrão, links em Content Cards abrem na mesma aba. Defina esta opção como true para que abram em uma nova aba. |
| `requireExplicitInAppMessageDismissal` | `boolean` | `false` | Por padrão, mensagens no app podem ser dispensadas clicando fora delas ou pressionando a tecla Escape. Defina esta opção como true para exigir que os usuários cliquem explicitamente em um botão de dispensar ou botão de ação para fechar a mensagem. |
| `devicePropertyAllowlist` | `string[]` | `undefined` | Por padrão, o Braze SDK detecta e coleta automaticamente todas as propriedades do dispositivo em DeviceProperties. Para substituir esse comportamento, forneça um array de DeviceProperties. Para desativar o envio de todas as propriedades aos servidores da Braze, forneça um array vazio. Sem algumas propriedades, nem todos os recursos funcionarão corretamente. Por exemplo, sem o fuso horário, a entrega no fuso horário local não funcionará. |
| `serviceWorkerScope` | `string` | `undefined` | Por padrão, o Braze Web SDK registrará seu service worker com o escopo padrão (o diretório do service worker). Forneça um valor para esta opção para substituir esse padrão e especificar um escopo personalizado para o service worker. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Initialization Options" }

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

### In-App Messages

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

#### Tratamento personalizado de In-App Messages {#custom-in-app-message-handling}

``` typescript
import { subscribeToInAppMessage, showInAppMessage } from "@braze/web-sdk";

subscribeToInAppMessage((inAppMessage) => {
    // Custom logic before showing
    if (inAppMessage.getExtras()['priority'] === 'high') {
        showInAppMessage(inAppMessage);
    }
});
```

#### Registrar interações com In-App Messages {#log-in-app-message-interactions}

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

#### In-App Messages com HTML personalizado {#custom-html-in-app-messages}

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

#### Inscrever-se para atualizações de Content Cards {#subscribe-to-content-cards-updates}

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

#### Inscrever-se para atualizações de Feature Flags {#subscribe-to-feature-flag-updates}

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

#### Inscrever-se para atualizações de banners {#subscribe-to-banner-updates}

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

#### Dispensar banners em uma UI personalizada {#dismiss-banners-in-a-custom-ui}

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

Quando você chama `dismissBanner(banner)`, o SDK gerencia o estado de dispensa do banner, remove o banner das atualizações ativas de banners, notifica os assinantes do evento de dispensa do banner e sincroniza a dispensa com a Braze. UIs personalizadas devem usar `subscribeToBannersUpdates` para reagir à remoção do banner dispensado, em vez de tratar `dismissBanner` apenas como uma alteração local na UI ou apenas como um método de registro de análise de dados.

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

### Gerenciamento de sessões {#session-management}

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

#### Inscrever-se para falhas de autenticação {#subscribe-to-authentication-failures}

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

Se você usa um framework de renderização no lado do servidor (SSR), como o Next.js, pode encontrar erros porque o SDK foi projetado para ser executado em um ambiente de navegador. Você pode resolver esses problemas importando o SDK dinamicamente.

Você pode manter os benefícios do tree-shaking ao fazer isso, exportando as partes do SDK que você precisa em um arquivo separado e, em seguida, importando dinamicamente esse arquivo no seu componente.

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

Alternativamente, se você usa webpack para empacotar seu app, pode aproveitar os comentários mágicos dele para importar dinamicamente apenas as partes do SDK que você precisa.

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

Se você usa Vite e vê um aviso sobre dependências circulares ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, pode ser necessário excluir o Braze SDK da descoberta de dependências:

``` javascript
export default {
    optimizeDeps: {
        exclude: ['@braze/web-sdk']
    }
}
```

### Framework Jest {#jest-framework}

Ao usar Jest, você pode ver um erro semelhante a `SyntaxError: Unexpected token 'export'`. Para corrigir isso, ajuste sua configuração no `package.json` para ignorar o Braze SDK:

``` json
{
  "jest": {
    "transformIgnorePatterns": [
      "/node_modules/(?!@braze)"
    ]
  }
}
```

### Asynchronous Module Definition (AMD) {#asynchronous-module-definition-amd}

#### Desativar suporte a AMD {#disable-amd-support}

Se o seu site usa RequireJS ou outro carregador de módulos AMD, mas você prefere carregar o Braze Web SDK pelo CDN, pode carregar uma versão da biblioteca que não inclui suporte a AMD. Esta versão da biblioteca pode ser carregada a partir do CDN: `https://js.appboycdn.com/web-sdk/6.3/braze.no-amd.min.js`

#### Carregador de módulos {#module-loader}

Se você usa RequireJS ou outros carregadores de módulos AMD, recomendamos hospedar uma cópia da nossa biblioteca e referenciá-la como faria com outros recursos:

``` javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Accelerated Mobile Pages (AMP) {#accelerated-mobile-pages-amp}

Para integração com AMP, você precisará:

1. **Incluir o script de push para a web do AMP**: Adicione a tag de script assíncrono ao seu head
2. **Adicionar widgets de inscrição**: Adicione widgets para permitir que os usuários se inscrevam/cancelem a inscrição
3. **Adicionar arquivos auxiliares**: Inclua `helper-iframe.html` e `permission-dialog.html`
4. **Criar service worker**: Adicione o arquivo de service worker da Braze
5. **Configurar o elemento amp-web-push**: Adicione o elemento `amp-web-push` com sua chave de API e URL base como parâmetros de consulta

Para instruções detalhadas de integração com AMP, consulte o [Guia do desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web#amp).

### Electron

O Electron não oferece suporte oficial a notificações por push para a web (veja: esta [issue no GitHub](https://github.com/electron/electron/issues/6697)). Existem outras [soluções alternativas de código aberto](https://github.com/MatthieuLemoine/electron-push-receiver) que você pode experimentar, mas que não foram testadas pela Braze.

### Integração via CDN {#cdn-integration}

- **Carregamento do script**: Inicialize após o carregamento da tag de script, colocando o código de inicialização após a tag de script, ou use o manipulador de evento `onload` da tag de script
- **Acesso global**: O SDK está disponível como `window.braze` quando carregado via CDN

### Service Worker (notificações por push) {#service-worker-push-notifications}

- **Obrigatório**: É necessário incluir o service worker da Braze para que as notificações por push funcionem
- **Registro padrão**: Por padrão, o Braze Web SDK registra e gerencia seu service worker automaticamente quando `requestPushPermission()` é chamado, assim como no início de cada nova sessão para usuários que já concederam permissão de push. Você ainda precisa hospedar um arquivo de service worker no local esperado contendo o código do service worker da Braze.
- **Gerenciando seu próprio service worker**: Se você já gerencia um service worker no seu aplicativo, defina a opção de inicialização `manageServiceWorkerExternally` como `true`, adicione o código do service worker da Braze ao seu arquivo de service worker e registre-o você mesmo usando `navigator.serviceWorker.register()`
- **Permissões de push**: Chame `braze.requestPushPermission()` em resposta a interações do usuário (por exemplo, cliques em botões). Use prompts de push suaves (UI personalizada) antes de solicitar a permissão do navegador

### Gerenciadores de tags {#tag-managers}

#### Tealium iQ

O Tealium iQ oferece uma integração básica e pronta com a Braze. Para configurar a integração, pesquise por Braze na interface de gerenciamento de tags do Tealium e forneça a chave de API do Web SDK do seu dashboard. Para mais detalhes ou suporte aprofundado de configuração do Tealium, confira nossa [documentação de integração](https://www.braze.com/docs/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou entre em contato com seu gerente de conta do Tealium.

#### Google Tag Manager

O Web SDK pode ser inicializado e chamado a partir de uma tag HTML personalizada no seu contêiner do Google Tag Manager. Consulte nosso [app de exemplo do Google Tag Manager](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/google-tag-manager) para ver um exemplo de envio de eventos para a Braze via GTM, ou confira nossa [documentação de integração](https://www.braze.com/docs/developer_guide/sdk_integration/google_tag_manager) para mais detalhes.

#### Outros gerenciadores de tags {#other-tag-managers}

A Braze também pode ser compatível com outras soluções de gerenciamento de tags seguindo nossas instruções de integração dentro de uma tag HTML personalizada. Entre em contato com um representante da Braze se precisar de ajuda para avaliar essas soluções.

---

## Bibliotecas {#libraries}

A tabela a seguir descreve as distribuições disponíveis do Braze Web SDK.

| Nome | Descrição | npm | URL do CDN |
| ---- | --------- | --- | ---------- |
| Full | SDK completo com UI. Ao usar a versão npm, empacotadores JavaScript removem código não utilizado, incluindo código de UI. | `@braze/web-sdk` | https://js.appboycdn.com/web-sdk/6.10/braze.min.js |
| Core | Contém o SDK sem UI. Implemente sua própria UI para In-App Messages e Content Cards ao usar esta versão do SDK. Use a biblioteca completa para a maioria das integrações, pois ela fornece elementos de UI personalizáveis via CSS. | N/A | https://js.appboycdn.com/web-sdk/6.10/braze.core.min.js |
| No-AMD | Contém o SDK completo sem suporte a AMD. Isso é útil se o seu site usa RequireJS ou outro carregador de módulos AMD, mas você prefere carregar o SDK pelo CDN. | N/A | https://js.appboycdn.com/web-sdk/6.10/braze.no-amd.min.js |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Libraries" }

## Navegadores compatíveis {#supported-browsers}

- Navegadores modernos baseados em Chromium (Chrome, Edge, Opera)
- Firefox
- Safari

## Depuração e solução de problemas {#debugging-troubleshooting}

Passe a opção `enableLogging: true` para a função de inicialização (`braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT', enableLogging: true });`) para que a Braze registre no console JavaScript. Isso é valioso para desenvolvimento, mas é visível para todos os usuários, então remova esta opção ou [forneça um logger alternativo](https://js.appboycdn.com/web-sdk/6.10/doc/modules/braze.html#setlogger) antes de lançar sua página em produção.

## Font Awesome

A Braze usa [Font Awesome](http://fortawesome.github.io/Font-Awesome/) 4.7.0 para ícones de mensagens no app. Para desativar o carregamento do Font Awesome, use a opção de inicialização `doNotLoadFontAwesome`. Confira a [folha de referência](http://fortawesome.github.io/Font-Awesome/cheatsheet/) para ver os ícones disponíveis.

## Recursos adicionais {#additional-resources}

- [Guia do desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web)
- [Documentação do SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)
- [Exemplos de builds](https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/)

## Fale com a gente {#contact}

Se você tiver dúvidas, entre em contato com o suporte técnico da Braze para obter assistência.
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, acesse [https://github.com/braze-inc/braze-web-sdk](https://github.com/braze-inc/braze-web-sdk).