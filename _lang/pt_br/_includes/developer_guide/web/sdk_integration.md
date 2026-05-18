## Sobre o SDK Braze para Web {#about-the-web-braze-sdk}

O SDK Braze para Web permite coletar análises e exibir mensagens ricas no app, push e mensagens de Content Cards para seus usuários da web. Para mais informações, veja a [documentação de referência JavaScript da Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Integrar o Web SDK {#integrate-the-web-sdk}

Você pode integrar o SDK Braze para Web usando os seguintes métodos. Para opções adicionais, veja [outros métodos de integração](#web_other-integration-methods).

- **Integração baseada em código:** Integre o SDK Braze para Web diretamente em seu código usando seu gerenciador de pacotes preferido ou o CDN da Braze. Isso lhe dá controle total sobre como o SDK é carregado e configurado.
- **Google Tag Manager:** Uma solução sem código que permite integrar o SDK Braze para Web sem modificar o código do seu site. Para mais informações, veja [Google Tag Manager com o SDK do Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager/).

{% alert important %}
Recomendamos usar o [método de integração NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Os benefícios incluem armazenar bibliotecas do SDK localmente em seu site, proporcionando imunidade contra extensões bloqueadoras de anúncios e contribuindo para tempos de carregamento mais rápidos como parte do suporte a empacotadores.
{% endalert %}

{% tabs local %}
{% tab code-based integration %}
### Etapa 1: Instalar a biblioteca da Braze {#step-1-install-the-braze-library}

Você pode instalar a biblioteca da Braze usando um dos seguintes métodos. No entanto, se seu site usar um `Content-Security-Policy`, revise a [Política de Segurança de Conteúdo]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy/) antes de continuar.

{% alert important %}
Embora a maioria dos bloqueadores de anúncios não bloqueie o SDK Braze para Web, alguns bloqueadores de anúncios mais restritivos são conhecidos por causar problemas.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
Se o seu site usar os gerenciadores de pacotes NPM ou Yarn, você poderá adicionar o [pacote Braze NPM](https://www.npmjs.com/package/@braze/web-sdk) como uma dependência.

As definições do Typescript agora estão incluídas a partir da versão 3.0.0. Para notas sobre como fazer upgrade da versão 2.x para a 3.x, consulte nosso [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Depois de instalada, você pode `import` ou `require` a biblioteca da maneira habitual:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Adicione o SDK da Braze para Web diretamente ao seu HTML fazendo referência ao nosso script hospedado na CDN, que carrega a biblioteca de forma assíncrona.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
A configuração padrão **Prevenir Rastreamento entre Sites** no Safari pode impedir que tipos de mensagens no app, como Banners e Content Cards, sejam exibidos quando você usa o método de integração CDN. Para evitar esse problema, use o método de integração NPM para que o Safari não classifique essas mensagens como tráfego entre sites e seus usuários da web possam vê-las em todos os navegadores suportados.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Etapa 2: Inicializar o SDK {#step-2-initialize-the-sdk}

Após adicionar o SDK Braze para Web ao seu site, inicialize a biblioteca com a chave de API e a [URL do endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) encontradas em **Settings** > **App Settings** dentro do seu dashboard da Braze. Para uma lista completa de opções para `braze.initialize()`, junto com nossos outros métodos JavaScript, veja a [documentação JavaScript da Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

{% alert note %}
**Domínios personalizados para solicitações do Web SDK não são suportados**: O `baseUrl` do Web SDK deve ser um endpoint de SDK da Braze (por exemplo, `sdk.iad-05.braze.com`). A Braze não suporta o roteamento do tráfego do Web SDK através de um domínio de propriedade do cliente via registros CNAME. Se você precisar que as solicitações do Web SDK se originem do seu próprio domínio, entre em contato com o suporte da Braze.
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
**Exibição de mensagens no app**: Para exibir mensagens no app automaticamente quando forem acionadas, você deve chamar `braze.automaticallyShowInAppMessages()`. Sem essa chamada, as mensagens no app não são exibidas automaticamente. Se você quiser gerenciar a exibição das mensagens manualmente, remova essa chamada e use `braze.subscribeToInAppMessage()` em vez disso. Para saber mais, veja [Entrega de mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/delivery/).
{% endalert %}

#### Solução de problemas de sessões ausentes para usuários anônimos {#troubleshooting-missing-sessions-for-anonymous-users}

Se você está vendo o comportamento "Sessão ausente", ou não consegue rastrear a sessão para usuários que permanecem anônimos na web, certifique-se de que sua integração chama `braze.openSession()` durante a inicialização.

- **Cenário:** Usuários anônimos podem retornar um ID da Braze, mas os dados da sessão estão em branco ou ausentes.
- **Causa:** A implementação não chama `braze.openSession()`.
- **Resolução:** Sempre chame `braze.openSession()` após a inicialização (e após `braze.changeUser()` se você definir um ID externo).

Para saber mais, veja [Etapa 2: Inicializar o SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk).

{% alert important %}
Usuários anônimos em dispositivos móveis ou da web podem ser contabilizados no seu [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). Como resultado, talvez seja necessário carregar ou inicializar condicionalmente o SDK para excluir esses usuários da sua contagem de MAU.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Filtrando tráfego de bots {#bot-filtering}

O MAU pode incluir uma porcentagem de usuários bots, o que inflaciona sua contagem de usuários ativos mensais. Embora o SDK Braze para Web inclua detecção integrada para alguns crawlers web comuns (como bots de motores de busca e bots de pré-visualização de redes sociais), é especialmente importante permanecer proativo com soluções robustas para detectar bots, já que atualizações do SDK sozinhas não podem detectar consistentemente todos os novos bots.

### Limitações da detecção de bots do lado do SDK {#limitations-of-sdk-side-bot-detection}

O Web SDK inclui detecção básica de bots baseada em user-agent que filtra crawlers conhecidos. No entanto, essa abordagem tem limitações:

- **Novos bots surgem constantemente**: Empresas de IA e outros atores criam regularmente novos bots que podem se disfarçar para evitar a detecção.
- **Falsificação de user-agent**: Bots sofisticados podem imitar user-agents de navegadores legítimos.
- **Bots personalizados**: Usuários não técnicos agora podem criar facilmente bots usando grandes modelos de linguagem (LLMs), tornando o comportamento dos bots imprevisível.

### Implementando filtragem de bots {#implementing-bot-filtering}

{% alert important %}
As soluções descritas abaixo são sugestões gerais. Adapte a lógica de filtragem de bots ao seu ambiente e padrões de tráfego únicos.
{% endalert %}

A solução mais robusta é implementar sua própria lógica de filtragem de bots antes de inicializar o SDK da Braze. As abordagens comuns incluem:

#### Exigir interação do usuário {#require-user-interaction}

Considere atrasar a inicialização do SDK até que um usuário realize uma interação significativa, como aceitar um banner de consentimento de cookies, rolar ou clicar. Essa abordagem é frequentemente mais fácil de implementar e pode ser altamente eficaz na filtragem de tráfego de bots.

{% alert important %}
Atrasar a inicialização do SDK até a interação do usuário pode fazer com que Banners e Content Cards também não sejam exibidos até que essa interação ocorra.
{% endalert %}

#### Detecção personalizada de bots {#custom-bot-detection}

Implemente detecção personalizada com base em seus padrões específicos de tráfego de bots, como:

- Analisando strings de user-agent em busca de padrões que você identificou no seu tráfego
- Verificando indicadores de navegador headless
- Usando serviços de detecção de bots de terceiros
- Monitorando sinais comportamentais específicos do seu site

**Exemplo de inicialização condicional:**

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

### Melhores práticas {#best-practices}

- Analise regularmente seus dados de MAU e padrões de tráfego da web para identificar novos comportamentos de bots.
- Teste minuciosamente para garantir que seu filtro de bots não impeça que usuários legítimos sejam rastreados.
- Atualize sua lógica de filtragem com base nos padrões de tráfego de bots que você observa em seu ambiente.

## Configurações opcionais {#optional-configurations}

### Registro {#logging}

Para ativar rapidamente o registro, adicione `?brazeLogging=true` como um parâmetro ao URL do seu site. Como alternativa, é possível ativar o registro [básico](#web_basic-logging) ou [personalizado](#web_custom-logging). Para uma visão centralizada em todas as plataformas, veja [Registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging/).

#### Registro básico {#basic-logging}

{% tabs local %}
{% tab before initialization %}
Use `enableLogging` para registrar mensagens básicas de depuração no console JavaScript antes que o SDK seja inicializado.

```javascript
enableLogging: true
```

Seu método deve ser semelhante ao seguinte:

```javascript
braze.initialize('API-KEY', {
    baseUrl: 'API-ENDPOINT',
    enableLogging: true
});
braze.openSession();
```
{% endtab %}

{% tab after initialization %}
Use `braze.toggleLogging()` para registrar mensagens básicas de depuração no console JavaScript após a inicialização do SDK. Seu método deve ser semelhante ao seguinte:

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
Os registros básicos são visíveis para todos os usuários, portanto, considere desativar ou mudar para [`setLogger`](#web_custom-logging) antes de liberar seu código para produção.
{% endalert %}

#### Registro personalizado {#custom-logging}

Use `setLogger` para registrar mensagens de depuração personalizadas no console JavaScript. Ao contrário dos registros básicos, esses registros não são visíveis para os usuários.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Substitua `STRING` por sua mensagem como um único parâmetro string. Seu método deve ser semelhante ao seguinte:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Fazendo upgrade do SDK {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

Quando você referencia o Braze Web SDK a partir da nossa rede de entrega de conteúdo, por exemplo, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (como recomendado pelas nossas instruções de integração padrão), seus usuários recebem atualizações menores (correções de bugs e recursos compatíveis com versões anteriores, versões `a.a.a` a `a.a.z` nos exemplos acima) automaticamente quando atualizam seu site.

No entanto, quando lançamos mudanças significativas, exigimos que você faça o upgrade do Braze Web SDK manualmente para garantir que mudanças disruptivas não impactem sua integração. Além disso, se você baixar nosso SDK e hospedá-lo por conta própria, não receberá atualizações de versão automaticamente e deve fazer o upgrade manualmente para receber os recursos e correções de bugs mais recentes.

Mantenha-se atualizado com a versão mais recente [seguindo nosso feed de versões](https://github.com/braze-inc/braze-web-sdk/tags.atom) com o leitor de RSS ou serviço de sua preferência e consulte [nosso changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) para obter um histórico completo de versões do Web SDK. Para fazer upgrade do SDK Braze para Web:

- Atualize a versão da biblioteca da Braze alterando o número da versão em `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js` ou nas dependências do gerenciador de pacotes.
- Se você tiver o push para a web integrado, atualize o arquivo do service worker em seu site — por padrão, ele está localizado em `/service-worker.js` no diretório raiz do site, mas o local pode ser personalizado em algumas integrações. Você deve acessar o diretório raiz para hospedar um arquivo de service worker.

Você deve atualizar esses dois arquivos em coordenação um com o outro para um funcionamento adequado.

## Outros métodos de integração {#other-integration-methods}

### Accelerated Mobile Pages (AMP)
{% details Saiba mais %}
#### Etapa 1: Incluir script de push para web de AMP {#step-1-include-amp-web-push-script}

Adicione a seguinte tag de script assíncrono em seu cabeçalho:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Etapa 2: Adicionar widgets de inscrição {#step-2-add-subscription-widgets}

Adicione um widget ao corpo do seu HTML que permita aos usuários se inscreverem e cancelarem a inscrição do push.

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

#### Etapa 3: Adicionar `helper-iframe` e `permission-dialog` {#step-3-add-helper-iframe-and-permission-dialog}

O componente AMP Web Push cria um popup para gerenciar as inscrições de push, então você deve adicionar os seguintes arquivos auxiliares ao seu projeto para ativar esse recurso:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Etapa 4: Criar um arquivo de service worker {#step-4-create-a-service-worker-file}

Crie um arquivo `service-worker.js` no diretório raiz do seu site e adicione o seguinte trecho:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Etapa 5: Configurar o elemento HTML do AMP web push {#step-5-configure-the-amp-web-push-html-element}

Adicione o seguinte elemento HTML `amp-web-push` ao corpo do seu HTML. Tenha em mente que você precisa anexar seu [`apiKey` e `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) como parâmetros de consulta ao `service-worker-URL`.

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

### Definição de Módulo Assíncrono (AMD) {#asynchronous-module-definition-amd}

#### Desativar suporte {#disable-support}

Se o seu site usa RequireJS ou outro carregador de módulo AMD, mas você prefere carregar o Braze Web SDK através de uma das outras opções nesta lista, você pode carregar uma versão da biblioteca que não inclui suporte a AMD. Essa versão da biblioteca pode ser carregada no seguinte local da CDN:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Carregador de módulo {#module-loader}

Se você usa o RequireJS ou outros carregadores de módulos AMD, recomendamos que hospede uma cópia da nossa biblioteca e faça referência a ela como faria com outros recursos:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

O Electron não oferece suporte oficial a notificações por push na web (consulte: este [problema no GitHub](https://github.com/electron/electron/issues/6697)). Há outras [soluções alternativas de código aberto](https://github.com/MatthieuLemoine/electron-push-receiver) que você pode tentar e que não foram testadas pela Braze.

### Framework Jest {#jest}

Ao usar o Jest, você poderá ver um erro semelhante a `SyntaxError: Unexpected token 'export'`. Para corrigir isso, ajuste sua configuração em `package.json` para ignorar o SDK da Braze:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### Frameworks SSR {#ssr}

O Web SDK é executado em um ambiente de navegador. Em frameworks SSR, inicialize a Braze em um componente exclusivo do cliente para que seu servidor nunca execute código do SDK.

#### Importação dinâmica agnóstica de framework {#framework-agnostic-dynamic-import}

Se o seu framework não está listado nesta seção, você pode importar dinamicamente a Braze a partir de um hook de ciclo de vida exclusivo do cliente.

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

Se estiver usando webpack, você pode importar dinamicamente apenas exportações específicas do SDK.

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

#### Hook compartilhado para Next.js e Remix {#shared-hook-for-nextjs-and-remix}

Crie um hook reutilizável `useBraze` e chame-o próximo à raiz do seu app.

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

Chame `useBraze` em um componente de cliente que envolve seu app.

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

Chame `useBraze` no topo do seu componente de app personalizado.

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

Chame `useBraze` no topo do componente da rota raiz.

Para exemplos de validação local do Remix, execute `PORT=4013 npm run dev`.

```tsx
// app/root.tsx
import { Outlet } from "@remix-run/react";
import { useBraze } from "./hooks/useBraze";

export default function App() {
  useBraze();

  return <Outlet />;
}
```

#### Registrando eventos e atualizando usuários {#logging-events-and-updating-users}

Depois que `useBraze` inicializa o SDK na raiz do seu app, outros componentes de cliente podem chamar métodos da Braze. Um padrão comum é chamá-los dentro de ações do usuário, como `onClick` ou `onSubmit`. No exemplo, os métodos do SDK são carregados dentro do handler de clique em vez de no topo do arquivo. Isso mantém o Web SDK fora do código do servidor e carrega apenas o que aquela ação precisa. O comentário `webpackExports` informa ao webpack quais métodos incluir, para que seu bundle permaneça menor.

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

Este exemplo mostra um componente `BuyButton` que registra atividade quando alguém clica em **Buy**. Primeiro, ele importa apenas `logCustomEvent`, `logPurchase` e `getUser` no momento do clique. Em seguida, atualiza um atributo de usuário, registra um evento personalizado e registra uma compra. Esse padrão ajuda a manter a inicialização centralizada em `useBraze`, enquanto ainda rastreia ações significativas de qualquer componente de cliente.

Se estiver usando Remix com Vite e as importações da raiz do pacote falharem em tempo de execução, use a solução alternativa existente do Vite. Para mais informações, veja [Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite).

Para uma lista completa dos métodos disponíveis, veja a [documentação de referência JavaScript da Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

### Tealium iQ

O Tealium iQ oferece uma integração básica da Braze pronta para uso. Para configurar a integração, procure a Braze na interface do Tealium Tag Management e forneça a chave de API do Web SDK do seu dashboard.

Para mais detalhes ou suporte aprofundado de configuração do Tealium, confira nossa [documentação de integração]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/#about-tealium) ou entre em contato com seu gerente de conta Tealium.

### Vite {#vite}

Se você usa o Vite e vir um aviso sobre dependências circulares ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, talvez seja necessário excluir o SDK da Braze da sua [descoberta de dependências](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Outros gerenciadores de tags {#other-tag-managers}

A Braze também pode ser compatível com outras soluções de gerenciamento de tags, seguindo nossas instruções de integração em uma tag HTML personalizada. Entre em contato com um representante da Braze se precisar de ajuda para avaliar essas soluções.