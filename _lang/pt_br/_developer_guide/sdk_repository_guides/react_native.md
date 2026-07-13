---
nav_title: React Native SDK
article_title: Guia do repositório do React Native SDK
page_order: 7
description: "Referência do README do Braze React Native SDK espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do React Native SDK {#react-native-sdk-repository-guide}

## Sobre o Braze React Native SDK {#about-the-braze-react-native-sdk}

O Braze React Native SDK conecta seus apps iOS e Android à Braze: perfis de usuário, superfícies de envio de mensagens, análise de dados e Feature Flags. Ele encapsula os SDKs nativos [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) e [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk) por trás de uma API JavaScript.

**A inicialização é orientada por JavaScript:** você configura a parte nativa (push, logging, delegates) nos recursos do Android e no `AppDelegate` do iOS, e então chama `Braze.initialize(apiKey, endpoint)` a partir do JavaScript para iniciar o SDK. Isso dá a você controle total sobre quando o SDK é inicializado e com quais credenciais. Após a inicialização, chame outros métodos do SDK (por exemplo, `changeUser`, `logCustomEvent`) conforme necessário.

### O que você pode fazer {#what-you-can-do}

- **Gerenciamento de usuários**: identificar usuários, definir campos de perfil, atributos personalizados, aliases e grupos de inscrições
- **Mensagens no app**: interface padrão da Braze ou tratamento personalizado via inscrições e APIs de registro
- **Content Cards**: interface de feed padrão, ou buscar cartões e criar sua própria interface
- **Banners**: banners HTML baseados em posicionamento, incluindo `BrazeBannerView`
- **Notificações por push**: solicitações de permissão, registro de token, listeners de carga útil (veja [Notificações por push](#push-notifications))
- **Feature Flags**: atualizar, ler propriedades, registrar impressões
- **Análise de dados**: eventos personalizados, compras, envio imediato
- **Controles do SDK**: ativar/desativar o SDK, limpar dados locais, assinaturas de autenticação do SDK

## Pré-requisitos {#prerequisites}

- **Conta Braze** com chave de API do app e endpoint do SDK
- Ambiente de desenvolvimento **React Native** ([configuração do ambiente React Native](https://reactnative.dev/docs/set-up-your-environment))
- **iOS**: Xcode, CocoaPods (`cd ios && pod install`)
- **Android**: Android Studio / Gradle; plugin Kotlin Gradle conforme exigido pelo seu template React Native
- **Push** (se utilizado): configuração de FCM (Android) e APNs (iOS) conforme a [documentação de push](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)

Para localizar as credenciais no dashboard, siga a [visão geral da integração](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native).

## Instalação {#installation}

``` bash
npm install @braze/react-native-sdk
# or:
# yarn add @braze/react-native-sdk
```

---

## Início rápido {#quick-start}

Esta seção mostra a configuração mínima necessária para inicializar o Braze React Native SDK.

1. Instale o pacote npm em [Instalação](#installation).
2. Conclua a **configuração nativa** para Android e iOS (configuração, permissões, push se necessário).
3. Inicialize o SDK a partir do JavaScript e comece a usá-lo:

``` typescript
import Braze from "@braze/react-native-sdk";

// Initialize the SDK — call early in your app lifecycle (e.g. in a useEffect).
// The API key and endpoint are passed from JavaScript; native configuration
// (push, logging, etc.) is applied automatically from your native setup.
Braze.initialize("<YOUR_API_KEY>", "<YOUR_SDK_ENDPOINT>");

Braze.changeUser("user-123");
Braze.logCustomEvent("button_clicked", { screen: "home" });
```

As tipagens TypeScript são incluídas no pacote (`src/index.d.ts` no GitHub).

Chamar `Braze.initialize` novamente com credenciais diferentes destrói a instância atual e a recria, suportando reinicialização durante a sessão.

---

## Configuração nativa {#native-setup}

> **Fonte oficial:** telas passo a passo, alterações de Gradle/CocoaPods e a lista completa de chaves XML do Android estão no [guia do desenvolvedor Braze React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native). Os trechos abaixo são exemplos mínimos.

### Android

- Adicione o **plugin Kotlin Gradle** no seu `build.gradle` raiz, caso seu template ainda não o inclua (as versões dependem da sua versão do React Native).
- Adicione um arquivo de recurso `braze.xml` em `res/values` com sua configuração. Ative a inicialização atrasada para que o SDK aguarde a chamada de `Braze.initialize()` a partir do JavaScript antes de iniciar. Outros valores de configuração (push, tempo limite de sessão, etc.) ainda são lidos deste arquivo e aplicados no momento da inicialização.
- Garanta permissões básicas como `INTERNET` e `ACCESS_NETWORK_STATE` no `AndroidManifest.xml`.
- Para push, conclua a integração do FCM e quaisquer flags de ID de remetente / registro específicas da Braze descritas na documentação.

``` xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- Enable delayed initialization so the SDK starts when
       Braze.initialize() is called from JavaScript. -->
  <bool name="com_braze_enable_delayed_initialization">true</bool>

  <!-- Additional native configuration (applied at initialization time) -->
  <bool name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">YOUR_SENDER_ID</string>
</resources>
```

{% alert note %}
A chave de API e o endpoint não são mais definidos no `braze.xml` — eles são passados a partir do JavaScript via `Braze.initialize(apiKey, endpoint)`.
{% endalert %}
### iOS

``` bash
cd ios && pod install
```

Use `BrazeReactInitializer.configure` no seu `AppDelegate` para registrar a configuração nativa. As closures que você fornece são armazenadas e aplicadas posteriormente quando `Braze.initialize(apiKey, endpoint)` é chamado a partir do JavaScript.

``` swift
import BrazeKit
import braze_react_native_sdk

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Register native configuration for when JS calls Braze.initialize().
    BrazeReactInitializer.configure { config in
      config.logger.level = .info
      config.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup
    return true
  }
}
```

- **Closure `configure`**: recebe um `Braze.Configuration` e permite definir propriedades de configuração nativa (logging, push, sessões, etc.). A chave de API e o endpoint são fornecidos a partir do JavaScript — você não os define aqui.
- **Closure `postInitialization`** *(opcional)*: recebe a instância `Braze` ativa após a criação, para configurações que exigem a instância (por exemplo, armazenar uma referência, definir delegates).

{% alert note %}
`BrazeReactInitializer.configure` é uma API Swift-first que substitui o descontinuado `BrazeReactBridge.initBraze(_:)`. Ela também resolve um problema de resolução de tipo Swift com `Braze.Configuration` na bridge Objective-C.
{% endalert %}
---

## Referência de configuração {#configuration-reference}

No React Native, **a configuração é nativa**: o Android lê `res/values/braze.xml`, e o iOS usa closures registradas via **`BrazeReactInitializer.configure`**. Ambas são aplicadas quando `Braze.initialize(apiKey, endpoint)` é chamado a partir do JavaScript.

### Android (`braze.xml`)

Os padrões ficam em XML; [`BrazeConfig.Builder`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) pode sobrescrevê-los na inicialização. A lista oficial de chaves e tipos está no [guia de integração do Android SDK](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/) e em [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) (cada propriedade Kotlin corresponde a recursos `com_braze_*` documentados).

Entradas comumente usadas:

| Chave | Tipo de recurso | Descrição |
|-------|-----------------|-----------|
| `com_braze_enable_delayed_initialization` | `bool` | **Obrigatória.** Defina como `true` para que o SDK aguarde a chamada de `Braze.initialize()` a partir do JavaScript. |
| `com_braze_api_key` | `string` | Não é necessária ao usar `Braze.initialize()` a partir do JavaScript (as credenciais são passadas pelo JS). Necessária apenas para inicialização legada nativa. |
| `com_braze_custom_endpoint` | `string` | Não é necessária ao usar `Braze.initialize()` a partir do JavaScript. Necessária apenas para inicialização legada nativa. |
| `com_braze_server_target` | `string` | Seletor opcional de cluster / ambiente (por exemplo, builds internos ou de staging). Prefira `com_braze_custom_endpoint` para produção, a menos que sua integração Braze especifique o contrário. |
| `com_braze_firebase_cloud_messaging_registration_enabled` | `bool` | Quando `true`, a Braze registra para FCM (configuração típica de push). |
| `com_braze_firebase_cloud_messaging_sender_id` | `string` | ID de remetente do FCM quando o registro automático está ativado. |
| `com_braze_handle_push_deep_links_automatically` | `bool` | Permite que a Braze abra deep links de push automaticamente. |
| `com_braze_trigger_action_minimum_time_interval_seconds` | `integer` | Mínimo de segundos entre ações de gatilho de mensagens no app. |
| **Outras** | *diversos* | Chaves adicionais não listadas aqui (tempo limite de sessão, geofences, localização, padrões de notificação, listas de permissão de dispositivos, inicialização atrasada, autenticação do SDK, etc.). Consulte [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) e o [guia de integração do Android SDK](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android (braze.xml)" }

### iOS (`Braze.Configuration`)

Defina propriedades de configuração nativa na closure `configure` passada para `BrazeReactInitializer.configure`. A closure recebe uma instância de `Braze.Configuration` — a chave de API e o endpoint são definidos automaticamente a partir da chamada JavaScript `Braze.initialize`. Detalhes completos: [`Braze.Configuration`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) e tipos aninhados **`api`**, **`push`**, **`logger`**, **`location`**.

| Área | Membros (representativos) | Notas |
|------|---------------------------|-------|
| **Credenciais** | `api.key`, `api.endpoint` | Definidos automaticamente a partir de `Braze.initialize(apiKey, endpoint)` no JavaScript. Não defina esses valores na closure `configure`. |
| **Logging** | `logger.level` | Logging detalhado é para desenvolvimento; reduza o ruído em produção. |
| **Push** | `push.automation`, `push.appGroup`, … | A automação simplifica o registro; `appGroup` é necessário para Push Stories / extensões quando utilizados. |
| **Mensagens no app** | `triggerMinimumTimeInterval` | Padrão de **30** segundos entre gatilhos. |
| **Sessões** | `sessionTimeout` | Inatividade antes de uma nova sessão (consulte a documentação de sessões da Braze). |
| **Privacidade / dados** | `api.trackingPropertyAllowList`, `devicePropertyAllowList`, `api.sdkAuthentication` | Alinhe com o [manifesto de privacidade](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/) e as configurações do produto de autenticação do SDK. |
| **Rede** | `api.requestPolicy`, `api.flushInterval` | Política de retry de requisições e cadência de envio. |
| **Inscrição push** | `optInWhenPushAuthorized` | Quando `true`, a inscrição pode mudar para opted-in após o usuário autorizar notificações. |
| **IAM e mudanças de usuário** | `preventInAppMessageDisplayForDifferentUser` | Reduz mensagens no app incompatíveis se o ID do usuário mudar. |
| **Outros** | `forwardUniversalLinks`, `ephemeralEvents`, `useUUIDAsDeviceId`, … | Consulte a documentação Swift para o comportamento completo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS (Braze.Configuration)" }

A bridge React Native define **`api.sdkFlavor`** / metadados do SDK específicos do React na inicialização; não sobrescreva esses valores a menos que a documentação da Braze instrua você a fazê-lo.

---

## API JavaScript / TypeScript {#javascript-typescript-api}

A exportação padrão do pacote é a classe `Braze` com métodos **estáticos** (por exemplo, `Braze.changeUser`, `Braze.logPurchase`). Constantes como `Braze.Events`, `Braze.Genders` e `Braze.NotificationSubscriptionTypes` estão vinculadas à mesma exportação.

---

## Recursos principais {#core-features}

### Gerenciamento de usuários {#user-management}

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.changeUser("user-123");
Braze.setEmail("user@example.com");
Braze.setCustomUserAttribute("plan", "premium");
Braze.addAlias("external_id", "marketing_id");
Braze.addToSubscriptionGroup("NEWSLETTER_GROUP_UUID");
```

**Autenticação do SDK** opcional: passe uma assinatura como segundo argumento de `changeUser`, ou chame `Braze.setSdkAuthenticationSignature(signature)` quando ativado no dashboard.

### Mensagens no app {#in-app-messages}

- Com a **interface padrão da Braze**, siga a [documentação de mensagens no app](https://www.braze.com/docs/developer_guide/in_app_messages?sdktab=react%20native); normalmente você **não** precisa chamar `subscribeToInAppMessage` apenas para exibir a interface padrão.
- Para tratamento **personalizado**, inscreva-se com `useBrazeUI: false` e registre impressões/cliques conforme necessário:

``` typescript
Braze.subscribeToInAppMessage(false, (event) => {
  const msg = event.inAppMessage;
  // Render your own UI from msg.message, msg.buttons, etc.
  Braze.logInAppMessageImpression(msg);
});
```

### Content Cards

``` typescript
const cards = await Braze.getCachedContentCards();
Braze.requestContentCardsRefresh();
Braze.launchContentCards(); // default Braze UI

Braze.logContentCardImpression(cardId);
Braze.logContentCardClicked(cardId);
```

Ouça atualizações com `Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, ...)`.

### Banners

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.requestBannersRefresh(["homepage_banner"]);
const banner = await Braze.getBanner("homepage_banner");

// Or use the native Banner view:
// <Braze.BrazeBannerView placementId="homepage_banner" />
```

### Notificações por push {#push-notifications}

``` typescript
Braze.requestPushPermission({
  alert: true,
  badge: true,
  sound: true,
});
// Token registration is usually handled natively; see docs for your setup.
Braze.registerPushToken(token);
```

- **`getInitialPushPayload`**: use quando o app é aberto a partir de uma notificação para evitar condições de corrida com `Linking` do RN; requer hooks nativos (`BrazeReactUtils` no iOS, `BrazeReactUtils.populateInitialPushPayloadFromIntent` no Android) conforme descrito nos comentários de documentação do TypeScript e no app de exemplo.
- **`Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, ...)`** é **exclusivo para Android** conforme as tipagens públicas.

### Feature Flags

``` typescript
const flag = await Braze.getFeatureFlag("new_checkout");
if (flag?.enabled) {
  const rollout = flag.getNumberProperty("rollout_percentage") ?? 0;
}
Braze.refreshFeatureFlags();
Braze.logFeatureFlagImpression("new_checkout");
```

### Análise de dados e compras {#analytics-and-purchases}

``` typescript
Braze.logCustomEvent("purchase_completed", { sku: "sku-1" });
Braze.logPurchase("sku-1", "29.99", "USD", 1, { source: "cart" });
Braze.requestImmediateDataFlush();
```

Nota: `logPurchase` recebe o **preço como string** (consulte as tipagens).

### Gerenciamento de dados e estado do SDK {#data-management-and-sdk-state}

**`changeUser`** apenas informa à Braze qual ID de usuário deve receber a atribuição de **novas** atividades. Ele **não** limpa os dados do SDK em cache no dispositivo. Não existe uma API separada de "logout": se você precisa de um sign-out tradicional (limpar o estado local da Braze para que o perfil, mensagens e tokens em cache do usuário anterior sejam removidos desta instalação), normalmente você usa **`wipeData()`**. Isso é um reset local completo.

``` typescript
Braze.wipeData();
Braze.disableSDK();
Braze.enableSDK();
```

**`wipeData()`** — Limpa os dados **locais** da Braze para esta instalação (estado de usuário/sessão/cartão em cache, associação de token de push, etc.). Use para comportamento de **sign-out**, quando você não deve deixar o estado da Braze do usuário anterior no dispositivo, além de resets de **"excluir meus dados neste dispositivo"**, resets de **QA** sem reinstalar, ou fluxos rigorosos de **privacidade**. **`changeUser`** sozinho não realiza essa limpeza — ele apenas define qual ID de usuário recebe **novos** eventos. No **iOS**, o comportamento pode diferir do Android (por exemplo, interação com o estado de SDK desativado); consulte a documentação nativa da Braze se você usar isso em produção.

**`disableSDK()`** — Interrompe a operação do SDK (sem coleta/encaminhamento conforme configurado). Use para toggles de **opt-out do usuário**, **modos restritos** (conformidade, configurações infantis) ou **depuração** sem remover a dependência.

**`enableSDK()`** — Reativa o SDK após **`disableSDK()`**. No **iOS**, a reativação pode **não** ser aplicada até o **próximo lançamento do app**; verifique na documentação Braze Swift/iOS antes de depender de reativação imediata.

---

## Eventos {#events}

Inscreva-se com `Braze.addListener(event, callback)`. A chamada retorna um objeto de inscrição; chame **`.remove()`** nele para parar de ouvir.

**Configurando um listener:**

``` typescript
import Braze from "@braze/react-native-sdk";

const subscription = Braze.addListener(
  Braze.Events.CONTENT_CARDS_UPDATED,
  (update) => {
    console.log("Content cards:", update.cards);
  }
);
```

**Removendo o listener:**

``` typescript
subscription.remove();
```

Em um componente React, armazene a inscrição e chame `.remove()` na sua limpeza (por exemplo, no retorno de um `useEffect`):

``` typescript
useEffect(() => {
  const sub = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
    setCards(update.cards);
  });
  return () => sub.remove();
}, []);
```

| Constante de evento | Carga útil (resumo) |
|---------------------|---------------------|
| `Braze.Events.CONTENT_CARDS_UPDATED` | Content Cards mais recentes |
| `Braze.Events.BANNER_CARDS_UPDATED` | Banners mais recentes |
| `Braze.Events.FEATURE_FLAGS_UPDATED` | Array de Feature Flags |
| `Braze.Events.IN_APP_MESSAGE_RECEIVED` | Evento de mensagem no app |
| `Braze.Events.SDK_AUTHENTICATION_ERROR` | Detalhes de erro de autenticação do SDK |
| `Braze.Events.PUSH_NOTIFICATION_EVENT` | Carga útil de push (**exclusivo para Android**) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos" }

---

## Notas de integração {#integration-notes}

- **Expo**: use o [plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin) para evitar configuração nativa manual sempre que possível.
- **Nova Arquitetura / Turbo Modules**: suportada em versões recentes do plugin; siga o guia do desenvolvedor e as configurações de exemplo do `AppDelegate` / Gradle se você migrar.
- **Privacidade (iOS)**: métodos como `updateTrackingPropertyAllowList` suportam configuração relacionada ao manifesto de privacidade; consulte o [manifesto de privacidade Swift](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/).
## - **Jest**: faça mock dos módulos nativos do `react-native` ou do Turbo module da Braze (consulte `__tests__/jest.setup.js` neste repositório para padrões). {#jest-mock-react-native-native-modules-or-the-braze-turbo-module-see-__tests__jestsetupjs-in-this-repo-for-patterns}

## Suporte de versão {#version-support}

{% alert note %}
Este SDK foi testado com a versão **0.85.3** do React Native.
{% endalert %}
A tabela a seguir lista as versões do React Native suportadas por release do plugin Braze.

| Plugin Braze | React Native | Nova Arquitetura |
|--------------|--------------|------------------|
| 9.0.0+       | ≥ 0.71       | Sim              |
| 6.0.0+       | ≥ 0.68       | Sim (≥ 0.70.0)  |
| 2.0.0+       | ≥ 0.68       | Sim              |
| ≤ 1.41.0     | ≤ 0.71       | Não              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Suporte de versão" }

Respeite também os requisitos dos SDKs nativos:

- [Informações de versão do Android SDK](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Informações de versão do Swift SDK](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

---

## Plugin Braze Expo {#braze-expo-plugin}

Para fluxos de trabalho gerenciados pelo Expo, consulte o [repositório do plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin).

---

## App de exemplo {#sample-app}

`BrazeProject` neste repositório é um exemplo completo (gerenciamento de usuários, Content Cards, Feature Flags, banners, etc.).

``` bash
cd BrazeProject/
yarn install
npx react-native start
```

**iOS** (a partir de `BrazeProject`):

``` bash
cd ios && pod install && cd ..
npx react-native run-ios
```

Use `RCT_NEW_ARCH_ENABLED=0 pod install` se você precisar da arquitetura legada.

**Android** (a partir de `BrazeProject`):

``` bash
npx react-native run-android
```

---

## Depuração e solução de problemas {#debugging-and-troubleshooting}

Ative o logging da Braze na configuração **nativa** durante o desenvolvimento para que o SDK escreva no console do sistema (Xcode / Android Logcat). Isso ajuda a verificar a inicialização, mudanças de usuário e entrega de eventos.

- **iOS** — Na closure `configure` passada para `BrazeReactInitializer.configure`, defina `config.logger.level = .debug` (ou `.info`). Reduza ou desative em produção para que os logs não fiquem visíveis para os usuários.
- **Android** — Use o recurso `com_braze_logger_initial_log_level` no `braze.xml` ou defina o equivalente em `BrazeConfig.Builder` (consulte [BrazeConfigurationProvider](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/logger-initial-log-level.html)). Use um nível não detalhado ou remova a sobrescrita antes do lançamento.

Para solução de problemas mais aprofundada (rede, sessão ou comportamento de Campaign), consulte o [guia do desenvolvedor Braze React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native) e a documentação dos SDKs nativos ([Swift](https://github.com/braze-inc/braze-swift-sdk) · [Android](https://github.com/braze-inc/braze-android-sdk)).

---

## Recursos adicionais {#additional-resources}

- [Guia do desenvolvedor Braze — React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native)
- [Notificações por push — React Native](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)
- [Repositório GitHub](https://github.com/braze-inc/braze-react-native-sdk)
- [Pacote npm](https://www.npmjs.com/package/@braze/react-native-sdk)

## Contato {#contact}

Se você tiver dúvidas, entre em contato com o suporte técnico da Braze para obter assistência.
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-react-native-sdk](https://github.com/braze-inc/braze-react-native-sdk).