## Sobre o SDK Braze para React Native {#about-the-react-native-braze-sdk}

Integrar o SDK Braze para React Native fornece funcionalidade básica de análise de dados e permite integrar mensagens no app e Content Cards para iOS e Android com apenas uma base de código.

## Compatibilidade com a nova arquitetura {#new-architecture-compatibility}

A seguinte versão mínima do SDK é compatível com todos os apps que usam a [Nova Arquitetura do React Native](https://reactnative.dev/docs/the-new-architecture/landing-page):

{% sdk_min_versions reactnative:2.0.1 %}

A partir da versão 6.0.0 do SDK, a Braze utiliza um Módulo Turbo do React Native, que é compatível tanto com a Nova Arquitetura quanto com a arquitetura de ponte legada. Isso significa que nenhuma configuração adicional é necessária.

{% alert warning %}
Se seu app iOS estiver em conformidade com `RCTAppDelegate` e seguir nossa configuração anterior de `AppDelegate`, revise os exemplos em [Configuração nativa completa](#reactnative_step-2-complete-native-setup) para evitar falhas ao se inscrever em eventos no Módulo Turbo.
{% endalert %}

## Requisitos de versão do React e React Native {#react-and-react-native-version-requirements}

A Braze não publica versões mínimas separadas do React além do que o SDK React Native suporta. Para integrar o SDK, use a versão 0.71 ou posterior do React Native. Para a lista completa de versões compatíveis do React Native, consulte o [repositório do GitHub do React Native SDK](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

Ao fazer upgrade do React, React Native ou do SDK da Braze, revise o [CHANGELOG](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) do SDK para verificar alterações incompatíveis antes de implantar.

## Integrando o SDK React Native {#integrating-the-react-native-sdk}

### Pré-requisitos {#prerequisites}

Para versões compatíveis do React Native e orientações de upgrade, consulte [Requisitos de versão do React e React Native](#react-and-react-native-version-requirements).

### Etapa 1: Integrar a biblioteca da Braze {#step-1-integrate-the-braze-library}

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

<a id="step-2-choose-a-setup-option"></a>
<a id="reactnative_step-2-complete-native-setup"></a>
### Etapa 2: Configuração nativa completa {#step-2-complete-native-setup}

Se seu app usa Expo, consulte [Usando o plugin Expo](#reactnative-using-the-expo-plugin). Se seu app usa React Native puro, consulte [Usando React Native CLI](#reactnative-using-react-native-cli).
Escolha um método de configuração em cada guia de versão: plugin Expo ou React Native CLI.

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

#### Método 1: Usando o plugin Expo {#reactnative-using-the-expo-plugin}

##### 2.1 Instale o plugin Braze Expo {#21-install-the-braze-expo-plugin}

Confira se sua versão do plugin Braze Expo é, no mínimo, 4.1.0. Para a lista completa de versões compatíveis, consulte o [repositório do plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

O trecho de código a seguir mostra o comando para instalar o plugin Braze Expo:

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 Adicione o plugin ao seu app.json {#22-add-the-plugin-to-your-appjson}

Em `app.json`, adicione o plugin Braze Expo. A chave de API e o endpoint não são mais definidos aqui. Forneça-os em tempo de execução através de `Braze.initialize()` no JavaScript. Adicione os seguintes parâmetros de configuração opcionais conforme as necessidades da sua implementação:

| Método                                        | Tipo    | Descrição                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | booleano | Somente iOS. Se deve usar a Braze para lidar com notificações por push no iOS.                       |
| `enableFirebaseCloudMessaging`                | booleano | Somente Android. Se deve usar o Firebase Cloud Messaging para notificações por push.             |
| `firebaseCloudMessagingSenderId`              | string  | Somente Android. Seu ID de remetente do Firebase Cloud Messaging.                                    |
| `sessionTimeout`                              | inteiro | O tempo limite da sessão da Braze para seu app, em segundos.                                                                                               |
| `enableSdkAuthentication`                     | booleano | Se deve ativar o recurso de [autenticação do SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication).      |
| `logLevel`                                    | inteiro | O nível de registro do seu app. O nível de log padrão é 8 e registra minimamente informações. Para ativar o registro detalhado para depuração, use o nível de registro 0.    |
| `minimumTriggerIntervalInSeconds`             | inteiro | O intervalo de tempo mínimo, em segundos, entre os disparos. O padrão é 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | booleano | Se a coleta automática de localização está ativada (se o usuário permitir).                                                                                  |
| `enableGeofence`                              | booleano | Se as geofences estão ativadas.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | booleano | Se as solicitações de geofence devem ser feitas automaticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | booleano | Somente iOS. Se uma mensagem modal no app é descartada quando o usuário clica fora da mensagem no app.                                           |
| `androidHandlePushDeepLinksAutomatically`     | booleano | Somente Android. Se o SDK da Braze deve tratar automaticamente os deep links de push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | booleano | Somente Android. Define se o conteúdo do texto em uma notificação por push deve ser interpretado e renderizado como HTML usando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Somente Android. Define a cor de destaque da notificação do Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Somente Android. Define o ícone grande de notificação do Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Somente Android. Define o ícone pequeno de notificação do Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | booleano | Somente iOS. Se o usuário deve ser automaticamente solicitado a fornecer permissões push na inicialização do app.                                                          |
| `enableBrazeIosRichPush`                      | booleano | Somente iOS. Se deve ativar recursos avançados de push para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | booleano | Somente iOS. Se deve ativar Push Stories da Braze para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Somente iOS. O grupo de app usado para Push Stories no iOS.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | booleano | Somente iOS. Se o ID do dispositivo usa um UUID gerado aleatoriamente.                                                                                       |
| `iosForwardUniversalLinks`                    | booleano | Somente iOS. Especifica se o SDK deve reconhecer automaticamente e encaminhar links universais para os métodos do sistema (padrão: `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2.2 Adicione o plugin ao seu app.json" }

O trecho de código a seguir mostra um exemplo de configuração `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ]
    ]
  }
}
```

###### Configurando ícones de notificação por push do Android {#android-push-icons}

Ao usar `androidNotificationLargeIcon` e `androidNotificationSmallIcon`, siga estas práticas recomendadas para exibição adequada dos ícones:

**Posicionamento e formato dos ícones**

Para usar ícones de notificação por push personalizados com o plugin Braze Expo:

1. Crie seus arquivos de ícone seguindo os requisitos de ícone listados abaixo.
2. Coloque-os nos diretórios nativos do Android do seu projeto em `android/app/src/main/res/drawable-<density>/`.
   Por exemplo, use `android/app/src/main/res/drawable-mdpi/` e `android/app/src/main/res/drawable-hdpi/`.
3. Alternativamente, se você estiver gerenciando ativos no seu diretório React Native, pode usar a [configuração de ícone do app.json](https://docs.expo.dev/versions/latest/config/app/#icon) do Expo ou criar um [plugin de configuração do Expo](https://docs.expo.dev/config-plugins/introduction/) para copiar os ícones para as pastas drawable do Android durante a pré-construção.

O plugin Braze Expo referencia esses ícones usando o sistema de recursos drawable do Android.

**Requisitos de ícone**

- **Ícone pequeno:** Deve ser uma silhueta branca em fundo transparente (este é um requisito da plataforma Android)
- **Ícone grande:** Pode ser uma imagem em cores completas.
- **Formato:** O formato PNG é recomendado.
- **Nomenclatura:** Use apenas letras minúsculas, números e sublinhados (por exemplo, `my_large_icon.png`)

**Configuração em app.json**

O trecho de código a seguir mostra como referenciar ícones de notificação do Android em `app.json` usando o prefixo `@drawable/`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
Não use caminhos de arquivo relativos (como `src/assets/images/icon.png`) ou inclua a extensão do arquivo ao referenciar ícones. O plugin Expo requer o prefixo `@drawable/` para localizar corretamente os ícones nas pastas nativas do Android após o processo de pré-construção.
{% endalert %}

**Como funciona**

O plugin Braze Expo referencia seus arquivos de ícone dos diretórios Android `drawable`. Quando você executa `npx expo prebuild`, o Expo gera a estrutura do projeto nativo do Android. Seus ícones devem estar presentes nas pastas Android `drawable` (seja colocados manualmente ou copiados através de um plugin de configuração) antes do processo de construção. O plugin então configura o SDK da Braze para usar esses recursos drawable pelos seus nomes (sem caminho ou extensão), por isso o prefixo `@drawable/` é necessário na sua configuração.

Para saber mais sobre ícones de notificação do Android, consulte as [diretrizes de ícones de notificação do Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### 2.3 Compile e execute seu aplicativo {#23-build-and-run-your-application}

Pré-construir seu aplicativo gera os arquivos nativos necessários para o funcionamento do plugin Braze Expo.

O trecho de código a seguir mostra o comando para pré-construir seu aplicativo:

```bash
npx expo prebuild
```

Execute seu aplicativo conforme especificado nos [documentos da Expo](https://docs.expo.dev/workflow/customizing/). Se você fizer alterações nas opções de configuração, pré-construa e execute o aplicativo novamente.

#### Método 2: Usando React Native CLI {#reactnative-using-react-native-cli}

##### Configurar o Android {#set-up-android}

**2.1 Adicione o plugin Kotlin Gradle**

O trecho de código a seguir mostra como adicionar o plugin Kotlin Gradle no `build.gradle` de nível superior do seu projeto, em `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Isso adiciona Kotlin ao seu projeto.

**2.2 Configure o SDK da Braze**

Crie um arquivo `braze.xml` na pasta `res/values` do seu projeto. A chave de API e o endpoint são fornecidos em tempo de execução pelo JavaScript, portanto não são necessários neste arquivo. O trecho de código a seguir mostra como ativar a inicialização atrasada com `com_braze_enable_delayed_initialization`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
Você ainda pode adicionar outros valores de configuração nativos ao `braze.xml` (como push, tempo limite de sessão e configurações de registro). Eles são aplicados automaticamente quando `Braze.initialize()` é chamado pelo JavaScript.
{% endalert %}

O trecho de código a seguir mostra as permissões necessárias para seu arquivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
No Braze Android SDK versão 12.2.0 ou posterior, você pode importar automaticamente a biblioteca android-sdk-location definindo `importBrazeLocationLibrary=true` no seu arquivo `gradle.properties`.
{% endalert %}

**2.3 Implemente o rastreamento de sessão do usuário**

As chamadas para `openSession()` e `closeSession()` são tratadas automaticamente.
O trecho de código a seguir mostra o que adicionar ao método `onCreate()` da sua classe `MainApplication`:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**2.4 Lide com atualizações de intent**

Se sua MainActivity tiver `android:launchMode` definido como `singleTask`, o trecho de código a seguir mostra o que adicionar à sua classe `MainActivity`:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### Configurar o iOS {#set-up-ios}

**2.5 (Opcional) Configure o Podfile para XCFrameworks dinâmicos**

Para importar certas bibliotecas da Braze, como BrazeUI, em um arquivo Objective-C++, você deve usar a sintaxe `#import`. A partir da versão `7.4.0` do Braze Swift SDK, os binários têm um [canal de distribuição opcional como XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que são compatíveis com essa sintaxe.

Se quiser usar esse canal de distribuição, substitua manualmente os locais de origem do CocoaPods no seu Podfile. Consulte o exemplo abaixo e substitua `{your-version}` pela versão relevante que você deseja importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Instale os pods**

Como o React Native vincula automaticamente as bibliotecas à plataforma nativa, você pode instalar o SDK com a ajuda do CocoaPods.

O trecho de código a seguir mostra como instalar os pods a partir da pasta raiz do projeto:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Configure o SDK da Braze**

Use `BrazeReactInitializer.configure` no seu `AppDelegate` para registrar a configuração nativa. Os closures que você fornece são armazenados e aplicados posteriormente quando `Braze.initialize(apiKey, endpoint)` é chamado pelo JavaScript.

{% subtabs local %}
{% subtab SWIFT %}

O trecho de código a seguir mostra como importar o SDK da Braze no topo do arquivo `AppDelegate.swift`:

```swift
import BrazeKit
import braze_react_native_sdk
```

No método `application(_:didFinishLaunchingWithOptions:)`, registre sua configuração nativa usando `BrazeReactInitializer.configure`. Não defina a chave de API ou o endpoint aqui. Eles são fornecidos pelo JavaScript através de `Braze.initialize()`.

- **Closure `configure`**: Recebe um `Braze.Configuration` e permite definir propriedades de configuração nativa (registro, push, sessões e mais).
- **Closure `postInitialization`** *(opcional)*: Recebe a instância `Braze` ativa após a criação, para configurações que requerem a instância (por exemplo, armazenar uma referência ou definir delegates).

O trecho de código a seguir mostra um exemplo de implementação do `AppDelegate.swift` que usa `BrazeReactInitializer.configure`:

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    BrazeReactInitializer.configure { configuration in
      configuration.logger.level = .info
      configuration.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup

    return true
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

O trecho de código a seguir mostra como importar o SDK da Braze no topo do arquivo `AppDelegate.m`:

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

No método `application:didFinishLaunchingWithOptions:`, registre sua configuração nativa usando `BrazeReactInitializer`. Não defina a chave de API ou o endpoint aqui. Eles são fornecidos pelo JavaScript através de `Braze.initialize()`.

O trecho de código a seguir mostra um exemplo de implementação do `AppDelegate.m` que usa `BrazeReactInitializer`:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazeReactInitializer configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  } postInitialization:^(Braze *braze) {
    // Store the Braze instance for later use.
  }];

  /* Other configuration */

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazeReactInitializer.configure()` apenas armazena sua configuração. Nenhuma instância da Braze existe até que `Braze.initialize()` seja chamado pelo JavaScript, portanto não chame nenhum método do SDK da Braze no AppDelegate após `configure()`.
Quando você chamar `Braze.initialize()` novamente, os mesmos blocos `configure` e `postInitialization` serão aplicados à nova instância da Braze.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 e anterior %}

#### Método 1: Usando o plugin Expo {#method-1-using-the-expo-plugin}

##### Etapa 2.1: Instale o plugin Braze Expo {#step-21-install-the-braze-expo-plugin}

Confira se sua versão do SDK Braze para React Native é, no mínimo, 1.37.0. Para a lista completa de versões compatíveis, consulte o [repositório Braze React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

O trecho de código a seguir mostra o comando para instalar o plugin Braze Expo:

```bash
npx expo install @braze/expo-plugin
```

##### Etapa 2.2: Adicione o plugin ao seu app.json {#step-22-add-the-plugin-to-your-appjson}

Em `app.json`, adicione o plugin Braze Expo. Você pode fornecer as seguintes opções de configuração:

| Método                                        | Tipo    | Descrição                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Obrigatória. A [chave de API]({{site.baseurl}}/api/identifier_types/) do seu aplicativo Android, localizada no dashboard da Braze em **Gerenciar configurações**. |
| `iosApiKey`                                   | string  | Obrigatória. A [chave de API]({{site.baseurl}}/api/identifier_types/) do seu aplicativo iOS, localizada no dashboard da Braze em **Gerenciar configurações**.     |
| `baseUrl`                                     | string  | Obrigatória. O [endpoint de SDK]({{site.baseurl}}/api/basics/#endpoints) do seu app, localizado no dashboard da Braze em **Gerenciar configurações**.    |
| `enableBrazeIosPush`                          | booleano | Somente iOS. Se deve usar a Braze para lidar com notificações por push no iOS. Introduzido no React Native SDK v1.38.0 e no Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | booleano | Somente Android. Se deve usar o Firebase Cloud Messaging para notificações por push. Introduzido no React Native SDK v1.38.0 e no Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Somente Android. Seu ID de remetente do Firebase Cloud Messaging. Introduzido no React Native SDK v1.38.0 e no Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | inteiro | O tempo limite da sessão da Braze para seu app, em segundos.                                                                                               |
| `enableSdkAuthentication`                     | booleano | Se deve ativar o recurso de [autenticação do SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication).      |
| `logLevel`                                    | inteiro | O nível de registro do seu app. O nível de log padrão é 8 e registra minimamente informações. Para ativar o registro detalhado para depuração, use o nível de registro 0.    |
| `minimumTriggerIntervalInSeconds`             | inteiro | O intervalo de tempo mínimo, em segundos, entre os disparos. O padrão é 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | booleano | Se a coleta automática de localização está ativada (se o usuário permitir).                                                                                  |
| `enableGeofence`                              | booleano | Se as geofences estão ativadas.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | booleano | Se as solicitações de geofence devem ser feitas automaticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | booleano | Somente iOS. Se uma mensagem modal no app é descartada quando o usuário clica fora da mensagem no app.                                           |
| `androidHandlePushDeepLinksAutomatically`     | booleano | Somente Android. Se o SDK da Braze deve tratar automaticamente os deep links de push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | booleano | Somente Android. Define se o conteúdo do texto em uma notificação por push deve ser interpretado e renderizado como HTML usando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Somente Android. Define a cor de destaque da notificação do Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Somente Android. Define o ícone grande de notificação do Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Somente Android. Define o ícone pequeno de notificação do Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | booleano | Somente iOS. Se o usuário deve ser automaticamente solicitado a fornecer permissões push na inicialização do app.                                                          |
| `enableBrazeIosRichPush`                      | booleano | Somente iOS. Se deve ativar recursos avançados de push para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | booleano | Somente iOS. Se deve ativar Push Stories da Braze para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Somente iOS. O grupo de app usado para Push Stories no iOS.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | booleano | Somente iOS. Se o ID do dispositivo usará um UUID gerado aleatoriamente.                                                                                       |
| `iosForwardUniversalLinks`                    | booleano | Somente iOS. Especifica se o SDK deve reconhecer automaticamente e encaminhar links universais para os métodos do sistema (padrão: `false`). Quando ativado, o SDK encaminhará automaticamente links universais para os métodos do sistema definidos em [Suporte a links universais no seu app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/). Introduzido no React Native SDK v11.1.0 e no Expo Plugin v3.2.0. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 2.2: Adicione o plugin ao seu app.json" }

O trecho de código a seguir mostra um exemplo de configuração `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

###### Configurando ícones de notificação por push do Android {#configuring-android-push-notification-icons}

Ao usar `androidNotificationLargeIcon` e `androidNotificationSmallIcon`, siga estas práticas recomendadas para exibição adequada dos ícones:

**Posicionamento e formato dos ícones**

Para usar ícones de notificação por push personalizados com o plugin Braze Expo:

1. Crie seus arquivos de ícone seguindo os requisitos de ícone listados abaixo.
2. Coloque-os nos diretórios nativos do Android do seu projeto em `android/app/src/main/res/drawable-<density>/` (por exemplo, `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/` ou similar).
3. Alternativamente, se você estiver gerenciando ativos no seu diretório React Native, pode usar a [configuração de ícone do app.json](https://docs.expo.dev/versions/latest/config/app/#icon) do Expo ou criar um [plugin de configuração do Expo](https://docs.expo.dev/config-plugins/introduction/) para copiar os ícones para as pastas drawable do Android durante a pré-construção.

O plugin Braze Expo referencia esses ícones usando o sistema de recursos drawable do Android.

**Requisitos de ícone**

- **Ícone pequeno:** Deve ser uma silhueta branca em fundo transparente (este é um requisito da plataforma Android)
- **Ícone grande:** Pode ser uma imagem em cores completas.
- **Formato:** O formato PNG é recomendado.
- **Nomenclatura:** Use apenas letras minúsculas, números e sublinhados (por exemplo, `my_large_icon.png`)

**Configuração em app.json**

O trecho de código a seguir mostra como referenciar ícones de notificação do Android em `app.json` usando o prefixo `@drawable/`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
Não use caminhos de arquivo relativos (como `src/assets/images/icon.png`) ou inclua a extensão do arquivo ao referenciar ícones. O plugin Expo requer o prefixo `@drawable/` para localizar corretamente os ícones nas pastas nativas do Android após o processo de pré-construção.
{% endalert %}

**Como funciona**

O plugin Braze Expo referencia seus arquivos de ícone dos diretórios Android `drawable`. Quando você executa `npx expo prebuild`, o Expo gera a estrutura do projeto nativo do Android. Seus ícones devem estar presentes nas pastas Android `drawable` (seja colocados manualmente ou copiados através de um plugin de configuração) antes do processo de construção. O plugin então configura o SDK da Braze para usar esses recursos drawable pelos seus nomes (sem caminho ou extensão), por isso o prefixo `@drawable/` é necessário na sua configuração.

Para saber mais sobre ícones de notificação do Android, consulte as [diretrizes de ícones de notificação do Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### Etapa 2.3: Compile e execute seu aplicativo {#step-23-build-and-run-your-application}

Pré-construir seu aplicativo gera os arquivos nativos necessários para o funcionamento do plugin Braze Expo.

O trecho de código a seguir mostra o comando para pré-construir seu aplicativo:

```bash
npx expo prebuild
```

Execute seu aplicativo conforme especificado nos [documentos da Expo](https://docs.expo.dev/workflow/customizing/). Tenha em mente que, se você fizer alterações nas opções de configuração, será necessário pré-construir e executar o aplicativo novamente.

#### Método 2: Usando React Native CLI {#method-2-using-react-native-cli}

##### Configurar o Android

**Etapa 2.1: Adicione o plugin Kotlin Gradle**

O trecho de código a seguir mostra como adicionar o plugin Kotlin Gradle no `build.gradle` de nível superior do seu projeto, em `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Isso adiciona Kotlin ao seu projeto.

**Etapa 2.2: Configure o SDK da Braze**

Para se conectar aos servidores da Braze, crie um arquivo `braze.xml` na pasta `res/values` do seu projeto. O trecho de código a seguir mostra um exemplo de configuração `braze.xml`. Substitua a [chave]({{site.baseurl}}/api/identifier_types/) de API e o [endpoint]({{site.baseurl}}/api/basics/#endpoints) pelos seus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

O trecho de código a seguir mostra as permissões necessárias para seu arquivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
No Braze Android SDK versão 12.2.0 ou posterior, você pode importar automaticamente a biblioteca android-sdk-location definindo `importBrazeLocationLibrary=true` no seu arquivo `gradle.properties`.
{% endalert %}

**Etapa 2.3: Implemente o rastreamento de sessão do usuário**

As chamadas para `openSession()` e `closeSession()` são tratadas automaticamente.
O trecho de código a seguir mostra o que adicionar ao método `onCreate()` da sua classe `MainApplication`:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**Etapa 2.4: Lide com atualizações de intent**

Se sua MainActivity tiver `android:launchMode` definido como `singleTask`, o trecho de código a seguir mostra o que adicionar à sua classe `MainActivity`:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### Configurar o iOS

**Etapa 2.5: (Opcional) Configure o Podfile para XCFrameworks dinâmicos**

Para importar certas bibliotecas da Braze, como BrazeUI, em um arquivo Objective-C++, você deve usar a sintaxe `#import`. A partir da versão `7.4.0` do Braze Swift SDK, os binários têm um [canal de distribuição opcional como XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que são compatíveis com essa sintaxe.

Se quiser usar esse canal de distribuição, substitua manualmente os locais de origem do CocoaPods no seu Podfile. O trecho de código a seguir mostra um exemplo de substituição. Substitua `{your-version}` pela versão relevante que você deseja importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**Etapa 2.6: Instale os pods**

Como o React Native vincula automaticamente as bibliotecas à plataforma nativa, você pode instalar o SDK com a ajuda do CocoaPods.

O trecho de código a seguir mostra como instalar os pods a partir da pasta raiz do projeto:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**Etapa 2.7: Configure o SDK da Braze**

{% subtabs local %}
{% subtab SWIFT %}

O trecho de código a seguir mostra como importar o SDK da Braze no topo do arquivo `AppDelegate.swift`:
```swift
import BrazeKit
import braze_react_native_sdk
```

No método `application(_:didFinishLaunchingWithOptions:)`, substitua a [chave]({{site.baseurl}}/api/identifier_types/) de API e o [endpoint]({{site.baseurl}}/api/basics/#endpoints) pelos valores do seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática em `AppDelegate` para facilitar o acesso.

{% alert note %}
Nosso exemplo pressupõe uma implementação do [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que fornece várias abstrações na configuração do React Native. Se estiver usando uma configuração diferente para seu app, certifique-se de ajustar sua implementação conforme necessário.
{% endalert %}

O trecho de código a seguir mostra um exemplo de configuração do `AppDelegate.swift`:

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

O trecho de código a seguir mostra como importar o SDK da Braze no topo do arquivo `AppDelegate.m`:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

No método `application:didFinishLaunchingWithOptions:`, substitua a [chave]({{site.baseurl}}/api/identifier_types/) de API e o [endpoint]({{site.baseurl}}/api/basics/#endpoints) pelos valores do seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática em `AppDelegate` para facilitar o acesso.

{% alert note %}
Nosso exemplo pressupõe uma implementação do [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que fornece várias abstrações na configuração do React Native. Se estiver usando uma configuração diferente para seu app, certifique-se de ajustar sua implementação conforme necessário.
{% endalert %}

O trecho de código a seguir mostra um exemplo de configuração do `AppDelegate.m`:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### Etapa 3: Inicialize o SDK {#step-3-initialize-the-sdk}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

O trecho de código a seguir mostra como importar a biblioteca no seu código React Native:

```javascript
import Braze from "@braze/react-native-sdk";
```

Em seguida, chame `Braze.initialize()` com a chave de API do identificador do app e o endpoint de SDK para criar a instância da Braze. Veja as opções abaixo para saber onde chamar esse método no seu app.

#### Inicialização padrão {#standard-initialization}

O trecho de código a seguir mostra como inicializar o SDK quando seu app inicia, chamando `Braze.initialize()` em um `useEffect`:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
  }, []);

  return (
    // Your app components
  );
};
```

#### Inicialização atrasada {#delayed-initialization}

O trecho de código a seguir mostra como adiar a inicialização do SDK para mais tarde na sessão. Por exemplo, após o usuário conceder consentimento ou concluir o login:

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
No iOS, as notificações por push recebidas antes de `Braze.initialize()` são enfileiradas e processadas após a inicialização. No Android, deep links de notificações por push não são resolvidos enquanto o SDK aguarda a inicialização. Se seu app depende do tratamento imediato de deep links na inicialização, use a [inicialização padrão](#standard-initialization).
{% endalert %}

#### Chaves de API específicas por plataforma {#platform-specific-api-keys}

O trecho de código a seguir mostra como usar a detecção de plataforma quando seus apps Android e iOS usam chaves de API diferentes:

```javascript
import { Platform } from "react-native";
import Braze from "@braze/react-native-sdk";

const apiKey = Platform.select({
  android: "YOUR-ANDROID-API-KEY",
  ios: "YOUR-IOS-API-KEY",
}) ?? "";

Braze.initialize(apiKey, "YOUR-SDK-ENDPOINT");
```

#### Reinicialização {#re-initialization}

Você pode chamar `Braze.initialize()` várias vezes para reinicializar o SDK com uma chave de API e endpoint diferentes durante a sessão. Cada chamada encerra a instância anterior da Braze e cria uma nova.

{% alert important %}
Todas as chamadas de métodos do SDK feitas antes de `Braze.initialize()` são ignoradas no iOS, portanto chame `Braze.initialize()` antes de usar qualquer outro método da Braze.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 e anterior %}

Para o React Native SDK 19.1.0 e anterior, a inicialização nativa acontece na Etapa 2. Importe a biblioteca no seu código React Native para chamar os métodos da Braze. Para mais detalhes, confira nosso [projeto de exemplo](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject).

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### Etapa 4: Teste a integração (opcional) {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

Você pode verificar se o SDK está integrado conferindo as estatísticas de sessão no dashboard. Se você executar seu aplicativo em qualquer plataforma, deverá ver uma nova sessão no dashboard (na seção **Visão geral**).

O trecho de código a seguir mostra como abrir uma sessão para um usuário específico no seu app:

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

Pesquise o usuário com `{some-user-id}` no dashboard em **Público** > **Pesquisar usuários**. Lá, você pode verificar se os dados de sessão e dispositivo foram registrados.

{% endtab %}
{% tab React Native SDK 19.1.0 e anterior %}

Para testar sua integração de SDK, o trecho de código a seguir mostra como iniciar uma nova sessão em qualquer plataforma para um usuário.

```javascript
Braze.changeUser("userId");
```

O trecho de código a seguir mostra um exemplo de atribuição do ID do usuário na inicialização do app:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

No dashboard da Braze, acesse [Pesquisa de usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search) e procure o usuário com o ID correspondente a `some-user-id`. Lá, você pode verificar se os dados de sessão e dispositivo foram registrados.

{% endtab %}
{% endtabs %}

## Próximos passos {#next-steps}

Após integrar o SDK da Braze, você pode começar a implementar recursos comuns de envio de mensagens:

- [Notificações por push]({{site.baseurl}}/developer_guide/push_notifications/): Configure e envie notificações por push para seus usuários.
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages/): Exiba mensagens contextuais dentro do seu app.
- [Banners]({{site.baseurl}}/developer_guide/banners/): Mostre banners persistentes na interface do seu app.