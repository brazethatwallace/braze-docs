## Sobre o Web Braze SDK or kit de desenvolvimento de software {#about-the-web-braze-sdk}

O Web Braze SDK or kit de desenvolvimento de software permite coletar dados de análise e exibir mensagens avançadas no app, push e Content Cards para seus usuários web. Para saber mais, consulte a [documentação de referência do JavaScript da Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

{% multi_lang_include archive/web-v4-rename.md %}

## Integre o Web SDK or kit de desenvolvimento de software {#integrate-the-web-sdk}

Você pode integrar o Web Braze SDK or kit de desenvolvimento de software usando os métodos a seguir. Para opções adicionais, veja [outros métodos de integração](#web_other-integration-methods).

- **Integração baseada em código:** Integre o Web Braze SDK or kit de desenvolvimento de software diretamente na sua base de código usando seu gerenciador de pacotes preferido ou o CDN da Braze. Isso lhe dá controle total sobre como o SDK or kit de desenvolvimento de software é carregado e configurado.
- **Google Tag Manager:** Uma solução sem código que permite integrar o Web Braze SDK or kit de desenvolvimento de software sem modificar o código do seu site. Para saber mais, veja [Google Tag Manager com o SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/sdk_integration/google_tag_manager).

{% alert important %}
Recomendamos usar o [método de integração NPM]({{site.baseurl}}/developer_guide/sdk_integration/?subtab=package%20manager&sdktab=web). Os benefícios incluem armazenar as bibliotecas do SDK or kit de desenvolvimento de software localmente no seu site, fornecer imunidade contra extensões de bloqueio de anúncios e contribuir para tempos de carregamento mais rápidos como parte do suporte a bundlers.
{% endalert %}

{% tabs local %}
{% tab code-based integration %}
### Etapa 1: Instale a biblioteca da Braze {#step-1-install-the-braze-library}

Você pode instalar a biblioteca da Braze usando um dos métodos a seguir. No entanto, se seu site usa uma `Content-Security-Policy`, revise a [Política de segurança de conteúdo]({{site.baseurl}}/developer_guide/platforms/web/content_security_policy) antes de continuar.

{% alert important %}
Embora a maioria dos bloqueadores de anúncios não bloqueie o Web Braze SDK or kit de desenvolvimento de software, alguns bloqueadores mais restritivos são conhecidos por causar problemas.
{% endalert %}

{% subtabs %}
{% subtab package manager %}
Se o seu site usa gerenciadores de pacotes NPM ou Yarn, você pode adicionar o [pacote NPM da Braze](https://www.npmjs.com/package/@braze/web-sdk) como dependência.

As definições de Typescript estão incluídas a partir da v3.0.0. Para notas sobre a atualização de 2.x para 3.x, consulte nosso [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md).

```bash
npm install --save @braze/web-sdk
# or, using yarn:
# yarn add @braze/web-sdk
```

Depois de instalado, você pode usar `import` ou `require` da maneira habitual:

```typescript
import * as braze from "@braze/web-sdk";
// or, using `require`
const braze = require("@braze/web-sdk");
```
{% endsubtab %}

{% subtab braze cdn %}
Adicione o Web Braze SDK or kit de desenvolvimento de software diretamente ao seu HTML referenciando nosso script hospedado no CDN, que carrega a biblioteca de forma assíncrona.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-SDK or kit de desenvolvimento de software%2Fblob%2Fmaster%2Fsnippets%2Floading-snippet.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
A configuração padrão **Impedir rastreamento entre sites** no Safari pode impedir que tipos de mensagem no app como Banners e Content Cards sejam exibidos quando você usa o método de integração por CDN. Para evitar esse problema, use o método de integração NPM para que o Safari não classifique essas mensagens como tráfego entre sites, permitindo que seus usuários web possam vê-las em todos os navegadores compatíveis.
{% endalert %}

{% endsubtab %}
{% endsubtabs %}

### Etapa 2: Inicialize o SDK or kit de desenvolvimento de software {#step-2-initialize-the-sdk}

Depois que o Web Braze SDK or kit de desenvolvimento de software for adicionado ao seu site, inicialize a biblioteca com a chave de API or interface de programação do aplicativo (API) e a [URL do endpoint do SDK or kit de desenvolvimento de software]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) encontradas em **Configurações** > **Configurações do app** no dashboard da Braze. Para uma lista completa de opções do `braze.initialize()`, junto com nossos outros métodos JavaScript, veja a [documentação JavaScript da Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

{% alert note %}
**Domínios personalizados para solicitações do Web SDK or kit de desenvolvimento de software não são suportados**: O `baseUrl` do Web SDK or kit de desenvolvimento de software deve ser um endpoint do SDK or kit de desenvolvimento de software da Braze (por exemplo, `sdk.iad-05.braze.com`). A Braze não suporta o roteamento de tráfego do Web SDK or kit de desenvolvimento de software por meio de um domínio de propriedade do cliente via registros CNAME. Se você precisar que as solicitações do Web SDK or kit de desenvolvimento de software sejam originadas do seu próprio domínio, entre em contato com o suporte da Braze.
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
**Exibição de In-App Messages**: Para exibir mensagens no app automaticamente quando são disparadas, você deve chamar `braze.automaticallyShowInAppMessages()`. Sem essa chamada, as mensagens no app não são exibidas automaticamente. Se você quiser gerenciar a exibição de mensagens manualmente, remova essa chamada e use `braze.subscribeToInAppMessage()` em seu lugar. Para saber mais, veja [Desativando disparos automáticos]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#disabling-automatic-triggers).
{% endalert %}

#### Resolução de problemas com sessões ausentes para usuários anônimos {#troubleshooting-missing-sessions-for-anonymous-users}

Se você está percebendo um comportamento de "sessão ausente", ou não consegue rastrear a sessão de usuários que permanecem anônimos na web, verifique se sua integração chama `braze.openSession()` durante a inicialização.

- **Cenário:** Usuários anônimos podem retornar um ID da Braze, mas os dados da sessão estão em branco ou ausentes.
- **Causa:** A implementação não chama `braze.openSession()`.
- **Solução:** Sempre chame `braze.openSession()` após a inicialização (e após `braze.changeUser()` se você definir um ID externo).

Para saber mais, veja [Etapa 2: Inicialize o SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web&tab=code-based%20integration#step-2-initialize-the-sdk).

{% alert important %}
Usuários anônimos em dispositivos móveis ou web podem ser contabilizados no seu [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data#monthly-active-users). Como resultado, você pode querer carregar ou inicializar o SDK or kit de desenvolvimento de software condicionalmente para excluir esses usuários da sua contagem de MAU.
{% endalert %}
{% endtab %}

{% tab Google Tag Manager %}
{% multi_lang_include developer_guide/web/google_tag_manager/initialization_tag.md %}
{% endtab %}
{% endtabs %}

## Filtrando tráfego de bots {#bot-filtering}

O MAU pode incluir uma porcentagem de usuários bots, o que inflaciona sua contagem de usuários ativos mensais. Embora o SDK or kit de desenvolvimento de software Braze para Web inclua detecção integrada para alguns crawlers web comuns (como bots de motores de busca e bots de pré-visualização de redes sociais), é especialmente importante permanecer proativo com soluções robustas para detectar bots, já que atualizações do SDK or kit de desenvolvimento de software sozinhas não podem detectar consistentemente todos os novos bots.

### Limitações da detecção de bots do lado do SDK or kit de desenvolvimento de software {#limitations-of-sdk-side-bot-detection}

O Web SDK or kit de desenvolvimento de software inclui detecção básica de bots baseada em user-agent que filtra crawlers conhecidos. No entanto, essa abordagem tem limitações:

- **Novos bots surgem constantemente**: Empresas de IA e outros atores criam regularmente novos bots que podem se disfarçar para evitar a detecção.
- **Falsificação de user-agent**: Bots sofisticados podem imitar user-agents de navegadores legítimos.
- **Bots personalizados**: Usuários não técnicos agora podem criar facilmente bots usando grandes modelos de linguagem (LLMs), tornando o comportamento dos bots imprevisível.

### Implementando filtragem de bots {#implementing-bot-filtering}

{% alert important %}
As soluções descritas abaixo são sugestões gerais. Adapte a lógica de filtragem de bots ao seu ambiente e padrões de tráfego únicos.
{% endalert %}

A solução mais robusta é implementar sua própria lógica de filtragem de bots antes de inicializar o SDK or kit de desenvolvimento de software da Braze. As abordagens comuns incluem:

#### Exigir interação do usuário {#require-user-interaction}

Considere atrasar a inicialização do SDK or kit de desenvolvimento de software até que um usuário realize uma interação significativa, como aceitar um banner de consentimento de cookies, rolar ou clicar. Essa abordagem é frequentemente mais fácil de implementar e pode ser altamente eficaz na filtragem de tráfego de bots.

{% alert important %}
Atrasar a inicialização do SDK or kit de desenvolvimento de software até a interação do usuário pode fazer com que Banners e Content Cards também não sejam exibidos até que essa interação ocorra.
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

### Registro de logs {#logging}

Para ativar rapidamente o registro de logs, você pode adicionar `?brazeLogging=true` como parâmetro à URL do seu website. Alternativamente, você pode ativar o registro [básico](#web_basic-logging) ou [personalizado](#web_custom-logging). Para uma visão geral centralizada em todas as plataformas, consulte [Registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

#### Registro básico {#basic-logging}

{% tabs local %}
{% tab antes da inicialização %}
Use `enableLogging` para registrar mensagens básicas de depuração no console do JavaScript antes que o SDK or kit de desenvolvimento de software seja inicializado.

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

{% tab após a inicialização %}
Use `braze.toggleLogging()` para registrar mensagens básicas de depuração no console do JavaScript após o SDK or kit de desenvolvimento de software ser inicializado. Seu método deve ser semelhante ao seguinte:

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
Os logs básicos são visíveis para todos os usuários. Considere desativá-los ou mudar para [`setLogger`](#web_custom-logging) antes de liberar seu código para produção.
{% endalert %}

#### Registro personalizado {#custom-logging}

Use `setLogger` para registrar mensagens de depuração personalizadas no console do JavaScript. Diferentemente dos logs básicos, esses logs não são visíveis para os usuários.

```javascript
setLogger(loggerFunction: (message: STRING) => void): void
```

Substitua `STRING` pela sua mensagem como um parâmetro de string único. Seu método deve ser semelhante ao seguinte:

```javascript
braze.initialize('API-KEY');
braze.setLogger(function(message) {
    console.log("Braze Custom Logger: " + message);
});
braze.openSession();
```

## Fazendo upgrade do SDK or kit de desenvolvimento de software {#upgrading-the-sdk}

{% multi_lang_include archive/web-v4-rename.md %}

Quando você faz referência ao SDK or kit de desenvolvimento de software da Braze para Web a partir da nossa rede de distribuição de conteúdo (CDN), por exemplo, `https://js.appboycdn.com/web-sdk/a.a/braze.min.js` (conforme recomendado pelas nossas instruções de integração padrão), seus usuários recebem atualizações menores (correções de bugs e recursos compatíveis com versões anteriores, versões de `a.a.a` até `a.a.z` neste exemplo) automaticamente quando atualizam o seu site.

No entanto, quando lançamos mudanças significativas, é necessário que você faça o upgrade do SDK or kit de desenvolvimento de software da Braze para Web manualmente para garantir que mudanças incompatíveis não afetem sua integração. Além disso, se você baixar nosso SDK or kit de desenvolvimento de software e hospedá-lo por conta própria, não receberá nenhuma atualização de versão automaticamente e deverá fazer o upgrade manualmente para receber os recursos e correções de bugs mais recentes.

Você pode se manter atualizado com nossas versões mais recentes [acompanhando nosso feed de lançamentos](https://github.com/braze-inc/braze-web-sdk/tags.atom) com o leitor de RSS ou serviço de sua preferência, e consultar [nosso changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) para um registro completo do histórico de lançamentos do nosso SDK or kit de desenvolvimento de software para Web. Para fazer upgrade do SDK or kit de desenvolvimento de software da Braze para Web:

- Atualize a versão da biblioteca da Braze alterando o número da versão em `https://js.appboycdn.com/web-sdk/[OLD VERSION NUMBER]/braze.min.js`, ou nas dependências do seu gerenciador de pacotes.
- Se você tiver o web push integrado, atualize o arquivo do service worker no seu site — por padrão, ele está localizado em `/service-worker.js` no diretório raiz do seu site, mas a localização pode ser personalizada em algumas integrações. Você precisa ter acesso ao diretório raiz para hospedar um arquivo de service worker.

Esses dois arquivos devem ser atualizados em conjunto para que tudo funcione corretamente.

## Outros métodos de integração {#other-integration-methods}

### Accelerated Mobile Pages (AMP) (AMP)
{% details Saiba mais %}
#### Etapa 1: Inclua o script de web push do AMP {#step-1-include-amp-web-push-script}

Adicione a seguinte tag de script assíncrono ao seu head:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

#### Etapa 2: Adicione widgets de inscrição {#step-2-add-subscription-widgets}

Adicione um widget ao body do seu HTML que permita aos usuários se inscreverem e cancelarem a inscrição de push.

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

#### Etapa 3: Adicione o `helper-iframe` e o `permission-dialog` {#step-3-add-helper-iframe-and-permission-dialog}

O componente AMP Web Push cria um popup para lidar com inscrições de push, então é necessário adicionar os seguintes arquivos auxiliares ao seu projeto para ativar esse recurso:

- [`helper-iframe.html`](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html)
- [`permission-dialog.html`](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html)

#### Etapa 4: Crie um arquivo de service worker {#step-4-create-a-service-worker-file}

Crie um arquivo `service-worker.js` no diretório raiz do seu website e adicione o seguinte snippet:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Etapa 5: Configure o elemento HTML de web push do AMP {#step-5-configure-the-amp-web-push-html-element}

Adicione o seguinte elemento HTML `amp-web-push` ao body do seu HTML. Lembre-se de que é necessário incluir sua [`apiKey` e `baseUrl`](https://documenter.getpostman.com/view/4689407/SVYrsdsG) como parâmetros de consulta em `service-worker-URL`.

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

#### Desativar suporte {#disable-support}

Se o seu site usa RequireJS ou outro carregador de módulos AMD, mas você prefere carregar o Web SDK or kit de desenvolvimento de software da Braze por meio de uma das outras opções desta lista, é possível carregar uma versão da biblioteca que não inclui suporte a AMD. Essa versão da biblioteca pode ser carregada a partir do seguinte local de CDN:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-SDK or kit de desenvolvimento de software%2Fblob%2Fmaster%2Fsnippets%2Fno-amd-library.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Carregador de módulos {#module-loader}

Se você usa RequireJS ou outros carregadores de módulos AMD, recomendamos hospedar uma cópia da nossa biblioteca e referenciá-la como faria com outros recursos:

```javascript
require(['path/to/braze.min.js'], function(braze) {
  braze.initialize('YOUR-API-KEY-HERE', { baseUrl: 'YOUR-SDK-ENDPOINT' });
  // Required if you want in-app messages to display automatically
  braze.automaticallyShowInAppMessages();
  braze.openSession();
});
```

### Electron {#electron}

O Electron não oferece suporte oficial a notificações por web push (veja: esta [issue no GitHub](https://github.com/electron/electron/issues/6697)). Existem outras [soluções alternativas de código aberto](https://github.com/MatthieuLemoine/electron-push-receiver) que você pode experimentar, mas que não foram testadas pela Braze.

### Framework Jest {#jest}

Ao usar o Jest, você pode encontrar um erro semelhante a `SyntaxError: Unexpected token 'export'`. Para corrigir isso, ajuste a configuração no `package.json` para ignorar o SDK or kit de desenvolvimento de software da Braze:

```
"jest": {
  "transformIgnorePatterns": [
    "/node_modules/(?!@braze)"
  ]
}
```

### Frameworks SSR {#ssr}

O Web SDK or kit de desenvolvimento de software é executado em um ambiente de navegador. Em frameworks SSR, inicialize a Braze em um componente exclusivo do cliente para que o servidor nunca execute código do SDK or kit de desenvolvimento de software.

#### Importação dinâmica independente de framework {#framework-agnostic-dynamic-import}

Se o seu framework não está listado nesta seção, você pode importar a Braze dinamicamente a partir de um hook de ciclo de vida exclusivo do cliente.

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

Se você usa webpack, pode importar dinamicamente apenas exportações específicas do SDK or kit de desenvolvimento de software.

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

Chame `useBraze` em um componente de cliente que envolve o seu app.

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

Para exemplos de validação local com Remix, execute `PORT=4013 npm run dev`.

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

Depois que `useBraze` inicializa o SDK or kit de desenvolvimento de software na raiz do app, outros componentes de cliente podem chamar os métodos da Braze. Um padrão comum é chamá-los dentro de ações do usuário, como `onClick` ou `onSubmit`. No exemplo, os métodos do SDK or kit de desenvolvimento de software são carregados dentro do handler de clique, e não no topo do arquivo. Isso mantém o Web SDK or kit de desenvolvimento de software fora do código do servidor e carrega apenas o que a ação precisa. O comentário `webpackExports` informa ao webpack quais métodos incluir, mantendo o bundle mais enxuto.

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

Este exemplo mostra um componente `BuyButton` que registra atividade quando alguém clica em **Buy**. Primeiro, ele importa apenas `logCustomEvent`, `logPurchase` e `getUser` no momento do clique. Em seguida, atualiza um atributo do usuário, registra um evento personalizado e registra uma compra. Esse padrão ajuda a manter a inicialização centralizada em `useBraze`, enquanto ainda rastreia ações significativas a partir de qualquer componente de cliente.

Se você usa Remix com Vite e as importações a partir da raiz do pacote falham em tempo de execução, use a solução alternativa existente para Vite. Para saber mais, consulte [Vite]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web#web_vite).

Para uma lista completa dos métodos disponíveis, consulte a [documentação de referência JavaScript da Braze](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

### Tealium iQ

O Tealium iQ oferece uma integração básica e pronta para uso com a Braze. Para configurar a integração, procure por Braze na interface de gerenciamento de tags do Tealium e forneça a chave de API or interface de programação do aplicativo (API) do Web SDK or kit de desenvolvimento de software disponível no seu dashboard.

Para mais detalhes ou suporte aprofundado de configuração do Tealium, confira nossa [documentação de integração]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium#about-tealium) ou entre em contato com o seu gerente de conta do Tealium.

### Vite {#vite}

Se você usa Vite e encontra um aviso sobre dependências circulares ou `Uncaught TypeError: Class extends value undefined is not a constructor or null`, pode ser necessário excluir o SDK or kit de desenvolvimento de software da Braze da [descoberta de dependências](https://vitejs.dev/guide/dep-pre-bundling.html#customizing-the-behavior):

```
optimizeDeps: {
    exclude: ['@braze/web-sdk']
},
```

### Outros gerenciadores de tags {#other-tag-managers}

A Braze também pode ser compatível com outras soluções de gerenciamento de tags seguindo nossas instruções de integração dentro de uma tag HTML personalizada. Entre em contato com um representante da Braze se precisar de ajuda para avaliar essas soluções.