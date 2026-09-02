## Sobre o SDK or kit de desenvolvimento de software React Native da Braze {#about-the-react-native-braze-sdk}

A integração do SDK or kit de desenvolvimento de software React Native da Braze fornece funcionalidade básica de análise de dados e permite integrar mensagens no app e Content Cards tanto para iOS quanto para Android com uma única base de código.

## Compatibilidade com a Nova Arquitetura {#new-architecture-compatibility}

A seguinte versão mínima do SDK or kit de desenvolvimento de software é compatível com todos os apps que utilizam a [Nova Arquitetura do React Native](https://reactnative.dev/docs/the-new-architecture/landing-page):

{% sdk_min_versions reactnative:2.0.1 %}

A partir da versão 6.0.0 do SDK or kit de desenvolvimento de software, a Braze utiliza um Turbo Module do React Native, que é compatível tanto com a Nova Arquitetura quanto com a arquitetura de bridge legada. Isso significa que nenhuma configuração adicional é necessária.

{% alert warning %}
Se o seu app iOS está em conformidade com `RCTAppDelegate` e segue nossa configuração anterior de `AppDelegate`, revise os exemplos em [Configuração nativa completa](#reactnative_step-2-complete-native-setup) para evitar falhas ao se inscrever em eventos no Turbo Module.
{% endalert %}

## Requisitos de versão do React e React Native {#react-and-react-native-version-requirements}

A Braze não publica versões mínimas separadas do React além do que o SDK or kit de desenvolvimento de software do React Native suporta. Para integrar o SDK or kit de desenvolvimento de software, use o React Native versão 0.71 ou posterior. Para a lista completa de versões suportadas do React Native, consulte o [repositório GitHub do SDK or kit de desenvolvimento de software do React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

Ao fazer upgrade do React, do React Native ou do SDK or kit de desenvolvimento de software da Braze, revise o [CHANGELOG](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) do SDK or kit de desenvolvimento de software para verificar alterações incompatíveis antes de fazer o deploy.

## Integrando o SDK or kit de desenvolvimento de software React Native {#integrating-the-react-native-sdk}

### Pré-requisitos {#prerequisites}

Para versões suportadas do React Native e orientações de upgrade, consulte [Requisitos de versão do React e React Native](#react-and-react-native-version-requirements).

### Etapa 1: Integre a biblioteca da Braze {#step-1-integrate-the-braze-library}

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
### Etapa 2: Complete a configuração nativa {#step-2-complete-native-setup}

Se o seu app usa Expo, consulte [Usando o plugin Expo](#reactnative-using-the-expo-plugin). Se o seu app usa React Native puro, consulte [Usando o React Native CLI](#reactnative-using-react-native-cli).
Escolha um método de configuração em cada aba de versão: plugin Expo ou React Native CLI.

{% tabs %}
{% tab React Native SDK or kit de desenvolvimento de software 19.2.0+ %}

#### Método 1: Usando o plugin Expo {#reactnative-using-the-expo-plugin}

##### 2.1 Instale o plugin Expo da Braze {#21-install-the-braze-expo-plugin}

Certifique-se de que a versão do plugin Expo da Braze seja pelo menos 4.1.0. Para a lista completa de versões suportadas, consulte o [repositório do plugin Expo da Braze](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

O trecho de código a seguir mostra o comando para instalar o plugin Expo da Braze:

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 Adicione o plugin ao seu app.json {#22-add-the-plugin-to-your-appjson}

No seu `app.json`, adicione o plugin Expo da Braze. A chave de API or interface de programação do aplicativo (API) e o endpoint não são mais definidos aqui. Forneça-os em tempo de execução por meio de `Braze.initialize()` a partir do JavaScript. Adicione os seguintes parâmetros de configuração opcionais de acordo com as necessidades da sua implementação:

| Método                                        | Tipo    | Descrição                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | boolean | Apenas iOS. Define se a Braze será usada para lidar com notificações por push no iOS.                       |
| `enableFirebaseCloudMessaging`                | boolean | Apenas Android. Define se o Firebase Cloud Messaging será usado para notificações por push.             |
| `firebaseCloudMessagingSenderId`              | string  | Apenas Android. O ID do remetente do Firebase Cloud Messaging.                                    |
| `sessionTimeout`                              | integer | O tempo limite da sessão da Braze para o seu app, em segundos.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Define se o recurso de [autenticação do SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) será ativado.      |
| `logLevel`                                    | integer | O nível de log do seu app. O nível de log padrão é 8 e registra minimamente informações. Para ativar o registro detalhado para depuração, use o nível de log 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | O intervalo mínimo de tempo em segundos entre disparos. O padrão é 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Define se a coleta automática de localização está ativada (se o usuário permitir).                                                                                  |
| `enableGeofence`                              | boolean | Define se os geofences estão ativados.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Define se as solicitações de geofence devem ser feitas automaticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | Apenas iOS. Define se uma mensagem modal no app é dispensada quando o usuário toca fora da mensagem no app.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Apenas Android. Define se o SDK or kit de desenvolvimento de software da Braze deve lidar automaticamente com deep links de push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Apenas Android. Define se o conteúdo de texto em uma notificação por push deve ser interpretado e renderizado como HTML usando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Apenas Android. Define a cor de destaque da notificação Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Apenas Android. Define o ícone grande da notificação Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Apenas Android. Define o ícone pequeno da notificação Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | Apenas iOS. Define se o usuário deve ser automaticamente solicitado a conceder permissão de push ao iniciar o app.                                                          |
| `enableBrazeIosRichPush`                      | boolean | Apenas iOS. Define se os recursos de push rico serão ativados para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | Apenas iOS. Define se o Braze Push Stories será ativado para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Apenas iOS. O grupo de apps usado para Push Stories no iOS.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | Apenas iOS. Define se o ID do dispositivo usará um UUID gerado aleatoriamente.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | Apenas iOS. Especifica se o SDK or kit de desenvolvimento de software deve reconhecer e encaminhar automaticamente links universais para os métodos do sistema (padrão: `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2.2 Adicione o plugin ao seu app.json" }

O trecho de código a seguir mostra um exemplo de configuração do `app.json`:

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

###### Configurando ícones de notificação por push no Android {#android-push-icons}

Ao usar `androidNotificationLargeIcon` e `androidNotificationSmallIcon`, siga estas boas práticas para a exibição correta dos ícones:

**Posicionamento e formato dos ícones**

Para usar ícones de notificação por push personalizados com o plugin Expo da Braze:

1. Crie seus arquivos de ícone seguindo os requisitos de ícone listados nos requisitos de ícone.
2. Coloque-os nos diretórios nativos Android do seu projeto em `android/app/src/main/res/drawable-<density>/`.
   Por exemplo, use `android/app/src/main/res/drawable-mdpi/` e `android/app/src/main/res/drawable-hdpi/`.
3. Alternativamente, se você estiver gerenciando ativos no diretório React Native, pode usar a [configuração de ícone do app.json](https://docs.expo.dev/versions/latest/config/app/#icon) do Expo ou criar um [plugin de configuração do Expo](https://docs.expo.dev/config-plugins/introduction/) para copiar os ícones para as pastas drawable do Android durante o prebuild.

O plugin Expo da Braze referencia esses ícones usando o sistema de recursos drawable do Android.

**Requisitos dos ícones**

- **Ícone pequeno:** deve ser uma silhueta branca em fundo transparente (este é um requisito da plataforma Android)
- **Ícone grande:** pode ser uma imagem colorida.
- **Formato:** o formato PNG é recomendado.
- **Nomenclatura:** use apenas letras minúsculas, números e underscores (por exemplo, `my_large_icon.png`)

**Configuração no app.json**

O trecho de código a seguir mostra como referenciar ícones de notificação Android no `app.json` usando o prefixo `@drawable/`:

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
Não use caminhos de arquivo relativos (como `src/assets/images/icon.png`) nem inclua a extensão do arquivo ao referenciar ícones. O plugin Expo requer o prefixo `@drawable/` para localizar corretamente os ícones nas pastas nativas do Android após o processo de prebuild.
{% endalert %}

**Como funciona**

O plugin Expo da Braze referencia seus arquivos de ícone nos diretórios `drawable` do Android. Quando você executa `npx expo prebuild`, o Expo gera a estrutura nativa do projeto Android. Seus ícones devem estar presentes nas pastas `drawable` do Android (colocados manualmente ou copiados por meio de um plugin de configuração) antes do processo de build. O plugin então configura o SDK or kit de desenvolvimento de software da Braze para usar esses recursos drawable por seus nomes (sem caminho ou extensão), por isso o prefixo `@drawable/` é necessário na sua configuração.

Para saber mais sobre ícones de notificação Android, consulte as [diretrizes de ícones de notificação do Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### 2.3 Compile e execute seu app {#23-build-and-run-your-application}

Executar o prebuild do seu app gera os arquivos nativos necessários para o plugin Expo da Braze funcionar.

O trecho de código a seguir mostra o comando para executar o prebuild do seu app:

```bash
npx expo prebuild
```

Execute seu app conforme especificado na [documentação do Expo](https://docs.expo.dev/workflow/customizing/). Se você fizer alterações nas opções de configuração, execute o prebuild e o app novamente.

#### Método 2: Usando o React Native CLI {#reactnative-using-react-native-cli}

##### Configure o Android {#set-up-android}

**2.1 Adicione o plugin Kotlin Gradle**

O trecho de código a seguir mostra como adicionar o plugin Kotlin Gradle no `build.gradle` de nível superior do projeto, em `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Isso adiciona o Kotlin ao seu projeto.

**2.2 Configure o SDK or kit de desenvolvimento de software da Braze**

Crie um arquivo `braze.xml` na pasta `res/values` do seu projeto. A chave de API or interface de programação do aplicativo (API) e o endpoint são fornecidos em tempo de execução a partir do JavaScript, portanto não são necessários neste arquivo. O trecho de código a seguir mostra como ativar a inicialização atrasada com `com_braze_enable_delayed_initialization`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
Você ainda pode adicionar outros valores de configuração nativos ao `braze.xml` (como push, tempo limite de sessão e configurações de log). Eles são aplicados automaticamente quando `Braze.initialize()` é chamado a partir do JavaScript.
{% endalert %}

O trecho de código a seguir mostra as permissões necessárias para o seu arquivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
No SDK or kit de desenvolvimento de software Android da Braze versão 12.2.0 ou posterior, você pode importar automaticamente a biblioteca android-SDK or kit de desenvolvimento de software-location definindo `importBrazeLocationLibrary=true` no arquivo `gradle.properties`.
{% endalert %}

**2.3 Implemente o rastreamento de sessão do usuário**

As chamadas para `openSession()` e `closeSession()` são tratadas automaticamente.
O trecho de código a seguir mostra o que adicionar ao método `onCreate()` da classe `MainApplication`:

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

Se a sua MainActivity tem `android:launchMode` definido como `singleTask`, o trecho de código a seguir mostra o que adicionar à classe `MainActivity`:

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

##### Configure o iOS {#set-up-ios}

**2.5 (Opcional) Configure o Podfile para XCFrameworks dinâmicos**

Para importar certas bibliotecas da Braze, como BrazeUI, em um arquivo Objective-C++, você deve usar a sintaxe `#import`. A partir da versão `7.4.0` do SDK or kit de desenvolvimento de software Swift da Braze, os binários possuem um [canal de distribuição opcional como XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que são compatíveis com essa sintaxe.

Se quiser usar esse canal de distribuição, sobrescreva manualmente os locais de origem do CocoaPods no seu Podfile. Consulte este exemplo e substitua `{your-version}` pela versão relevante que deseja importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Instale os pods**

Como o React Native vincula automaticamente as bibliotecas à plataforma nativa, você pode instalar o SDK or kit de desenvolvimento de software com a ajuda do CocoaPods.

O trecho de código a seguir mostra como instalar os pods a partir da pasta raiz do projeto:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Configure o SDK or kit de desenvolvimento de software da Braze**

Use `BrazeReactInitializer.configure` no seu `AppDelegate` para registrar a configuração nativa. As closures que você fornecer são armazenadas e aplicadas posteriormente, quando `Braze.initialize(apiKey, endpoint)` é chamado a partir do JavaScript.

{% subtabs local %}
{% subtab SWIFT %}

O trecho de código a seguir mostra como importar o SDK or kit de desenvolvimento de software da Braze no topo do arquivo `AppDelegate.swift`:

```swift
import BrazeKit
import braze_react_native_sdk
```

No método `application(_:didFinishLaunchingWithOptions:)`, registre sua configuração nativa usando `BrazeReactInitializer.configure`. Não defina a chave de API or interface de programação do aplicativo (API) ou o endpoint aqui. Eles são fornecidos a partir do JavaScript por meio de `Braze.initialize()`.

- **Closure `configure`**: recebe um `Braze.Configuration` e permite definir propriedades de configuração nativas (log, push, sessões e mais).
- **Closure `postInitialization`** _(opcional)_: recebe a instância `Braze` ativa após a criação, para configurações que requerem a instância (por exemplo, armazenar uma referência ou definir delegates).

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

O trecho de código a seguir mostra como importar o SDK or kit de desenvolvimento de software da Braze no topo do arquivo `AppDelegate.m`:

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

No método `application:didFinishLaunchingWithOptions:`, registre sua configuração nativa usando `BrazeReactInitializer`. Não defina a chave de API or interface de programação do aplicativo (API) ou o endpoint aqui. Eles são fornecidos a partir do JavaScript por meio de `Braze.initialize()`.

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
`BrazeReactInitializer.configure()` apenas armazena sua configuração. Nenhuma instância da Braze existe até que `Braze.initialize()` seja chamado a partir do JavaScript, portanto não chame nenhum método do SDK or kit de desenvolvimento de software da Braze no AppDelegate após `configure()`.
Quando você chama `Braze.initialize()` novamente, os mesmos blocos `configure` e `postInitialization` são aplicados à nova instância da Braze.
{% endalert %}

{% endtab %}
{% tab React Native SDK or kit de desenvolvimento de software 19.1.0 e anterior %}

#### Método 1: Usando o plugin Expo {#method-1-using-the-expo-plugin}

##### Etapa 2.1: Instale o plugin Expo da Braze {#step-21-install-the-braze-expo-plugin}

Certifique-se de que a versão do SDK or kit de desenvolvimento de software React Native da Braze seja pelo menos 1.37.0. Para a lista completa de versões suportadas, consulte o [repositório React Native da Braze](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

O trecho de código a seguir mostra o comando para instalar o plugin Expo da Braze:

```bash
npx expo install @braze/expo-plugin
```

##### Etapa 2.2: Adicione o plugin ao seu app.json {#step-22-add-the-plugin-to-your-appjson}

No seu `app.json`, adicione o plugin Expo da Braze. Você pode fornecer as seguintes opções de configuração:

| Método                                        | Tipo    | Descrição                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Obrigatório. A [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/identifier_types) do seu app Android, localizada no dashboard da Braze em **Manage Settings**. |
| `iosApiKey`                                   | string  | Obrigatório. A [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/identifier_types) do seu app iOS, localizada no dashboard da Braze em **Manage Settings**.     |
| `baseUrl`                                     | string  | Obrigatório. O [endpoint do SDK or kit de desenvolvimento de software]({{site.baseurl}}/api/basics#endpoints) do seu app, localizado no dashboard da Braze em **Manage Settings**.    |
| `enableBrazeIosPush`                          | boolean | Apenas iOS. Define se a Braze será usada para lidar com notificações por push no iOS. Introduzido no React Native SDK or kit de desenvolvimento de software v1.38.0 e Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | boolean | Apenas Android. Define se o Firebase Cloud Messaging será usado para notificações por push. Introduzido no React Native SDK or kit de desenvolvimento de software v1.38.0 e Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Apenas Android. O ID do remetente do Firebase Cloud Messaging. Introduzido no React Native SDK or kit de desenvolvimento de software v1.38.0 e Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | integer | O tempo limite da sessão da Braze para o seu app, em segundos.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Define se o recurso de [autenticação do SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) será ativado.      |
| `logLevel`                                    | integer | O nível de log do seu app. O nível de log padrão é 8 e registra minimamente informações. Para ativar o registro detalhado para depuração, use o nível de log 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | O intervalo mínimo de tempo em segundos entre disparos. O padrão é 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Define se a coleta automática de localização está ativada (se o usuário permitir).                                                                                  |
| `enableGeofence`                              | boolean | Define se os geofences estão ativados.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Define se as solicitações de geofence devem ser feitas automaticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | Apenas iOS. Define se uma mensagem modal no app é dispensada quando o usuário toca fora da mensagem no app.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Apenas Android. Define se o SDK or kit de desenvolvimento de software da Braze deve lidar automaticamente com deep links de push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Apenas Android. Define se o conteúdo de texto em uma notificação por push deve ser interpretado e renderizado como HTML usando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Apenas Android. Define a cor de destaque da notificação Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Apenas Android. Define o ícone grande da notificação Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Apenas Android. Define o ícone pequeno da notificação Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | Apenas iOS. Define se o usuário deve ser automaticamente solicitado a conceder permissão de push ao iniciar o app.                                                          |
| `enableBrazeIosRichPush`                      | boolean | Apenas iOS. Define se os recursos de push rico serão ativados para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | Apenas iOS. Define se o Braze Push Stories será ativado para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Apenas iOS. O grupo de apps usado para Push Stories no iOS.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | Apenas iOS. Define se o ID do dispositivo usará um UUID gerado aleatoriamente.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | Apenas iOS. Especifica se o SDK or kit de desenvolvimento de software deve reconhecer e encaminhar automaticamente links universais para os métodos do sistema (padrão: `false`). Quando ativado, o SDK or kit de desenvolvimento de software encaminhará automaticamente links universais para os métodos do sistema definidos em [Supporting universal links in your app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/). Introduzido no React Native SDK or kit de desenvolvimento de software v11.1.0 e Expo Plugin v3.2.0. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 2.2: Adicione o plugin ao seu app.json" }

O trecho de código a seguir mostra um exemplo de configuração do `app.json`:

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

###### Configurando ícones de notificação por push no Android {#configuring-android-push-notification-icons}

Ao usar `androidNotificationLargeIcon` e `androidNotificationSmallIcon`, siga estas boas práticas para a exibição correta dos ícones:

**Posicionamento e formato dos ícones**

Para usar ícones de notificação por push personalizados com o plugin Expo da Braze:

1. Crie seus arquivos de ícone seguindo os requisitos de ícone listados nos requisitos de ícone.
2. Coloque-os nos diretórios nativos Android do seu projeto em `android/app/src/main/res/drawable-<density>/` (por exemplo, `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/` ou similar).
3. Alternativamente, se você estiver gerenciando ativos no diretório React Native, pode usar a [configuração de ícone do app.json](https://docs.expo.dev/versions/latest/config/app/#icon) do Expo ou criar um [plugin de configuração do Expo](https://docs.expo.dev/config-plugins/introduction/) para copiar os ícones para as pastas drawable do Android durante o prebuild.

O plugin Expo da Braze referencia esses ícones usando o sistema de recursos drawable do Android.

**Requisitos dos ícones**

- **Ícone pequeno:** deve ser uma silhueta branca em fundo transparente (este é um requisito da plataforma Android)
- **Ícone grande:** pode ser uma imagem colorida.
- **Formato:** o formato PNG é recomendado.
- **Nomenclatura:** use apenas letras minúsculas, números e underscores (por exemplo, `my_large_icon.png`)

**Configuração no app.json**

O trecho de código a seguir mostra como referenciar ícones de notificação Android no `app.json` usando o prefixo `@drawable/`:

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
Não use caminhos de arquivo relativos (como `src/assets/images/icon.png`) nem inclua a extensão do arquivo ao referenciar ícones. O plugin Expo requer o prefixo `@drawable/` para localizar corretamente os ícones nas pastas nativas do Android após o processo de prebuild.
{% endalert %}

**Como funciona**

O plugin Expo da Braze referencia seus arquivos de ícone nos diretórios `drawable` do Android. Quando você executa `npx expo prebuild`, o Expo gera a estrutura nativa do projeto Android. Seus ícones devem estar presentes nas pastas `drawable` do Android (colocados manualmente ou copiados por meio de um plugin de configuração) antes do processo de build. O plugin então configura o SDK or kit de desenvolvimento de software da Braze para usar esses recursos drawable por seus nomes (sem caminho ou extensão), por isso o prefixo `@drawable/` é necessário na sua configuração.

Para saber mais sobre ícones de notificação Android, consulte as [diretrizes de ícones de notificação do Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### Etapa 2.3: Compile e execute seu app {#step-23-build-and-run-your-application}

Executar o prebuild do seu app gera os arquivos nativos necessários para o plugin Expo da Braze funcionar.

O trecho de código a seguir mostra o comando para executar o prebuild do seu app:

```bash
npx expo prebuild
```

Execute seu app conforme especificado na [documentação do Expo](https://docs.expo.dev/workflow/customizing/). Lembre-se de que, se você fizer alterações nas opções de configuração, será necessário executar o prebuild e o app novamente.

#### Método 2: Usando o React Native CLI {#method-2-using-react-native-cli}

##### Configure o Android

**Etapa 2.1: Adicione o plugin Kotlin Gradle**

O trecho de código a seguir mostra como adicionar o plugin Kotlin Gradle no `build.gradle` de nível superior do projeto, em `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Isso adiciona o Kotlin ao seu projeto.

**Etapa 2.2: Configure o SDK or kit de desenvolvimento de software da Braze**

Para se conectar aos servidores da Braze, crie um arquivo `braze.xml` na pasta `res/values` do seu projeto. O trecho de código a seguir mostra um exemplo de configuração do `braze.xml`. Substitua a [chave]({{site.baseurl}}/api/identifier_types) de API or interface de programação do aplicativo (API) e o [endpoint]({{site.baseurl}}/api/basics#endpoints) pelos seus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

O trecho de código a seguir mostra as permissões necessárias para o seu arquivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
No SDK or kit de desenvolvimento de software Android da Braze versão 12.2.0 ou posterior, você pode importar automaticamente a biblioteca android-SDK or kit de desenvolvimento de software-location definindo `importBrazeLocationLibrary=true` no arquivo `gradle.properties`.
{% endalert %}

**Etapa 2.3: Implemente o rastreamento de sessão do usuário**

As chamadas para `openSession()` e `closeSession()` são tratadas automaticamente.
O trecho de código a seguir mostra o que adicionar ao método `onCreate()` da classe `MainApplication`:

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

Se a sua MainActivity tem `android:launchMode` definido como `singleTask`, o trecho de código a seguir mostra o que adicionar à classe `MainActivity`:

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

##### Configure o iOS

**Etapa 2.5: (Opcional) Configure o Podfile para XCFrameworks dinâmicos**

Para importar certas bibliotecas da Braze, como BrazeUI, em um arquivo Objective-C++, você deve usar a sintaxe `#import`. A partir da versão `7.4.0` do SDK or kit de desenvolvimento de software Swift da Braze, os binários possuem um [canal de distribuição opcional como XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que são compatíveis com essa sintaxe.

Se quiser usar esse canal de distribuição, sobrescreva manualmente os locais de origem do CocoaPods no seu Podfile. O trecho de código a seguir mostra um exemplo de sobrescrita. Substitua `{your-version}` pela versão relevante que deseja importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**Etapa 2.6: Instale os pods**

Como o React Native vincula automaticamente as bibliotecas à plataforma nativa, você pode instalar o SDK or kit de desenvolvimento de software com a ajuda do CocoaPods.

O trecho de código a seguir mostra como instalar os pods a partir da pasta raiz do projeto:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**Etapa 2.7: Configure o SDK or kit de desenvolvimento de software da Braze**

{% subtabs local %}
{% subtab SWIFT %}

O trecho de código a seguir mostra como importar o SDK or kit de desenvolvimento de software da Braze no topo do arquivo `AppDelegate.swift`:
```swift
import BrazeKit
import braze_react_native_sdk
```

No método `application(_:didFinishLaunchingWithOptions:)`, substitua a [chave]({{site.baseurl}}/api/identifier_types) de API or interface de programação do aplicativo (API) e o [endpoint]({{site.baseurl}}/api/basics#endpoints) pelos valores do seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática no `AppDelegate` para fácil acesso.

{% alert note %}
Nosso exemplo assume uma implementação de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que fornece várias abstrações na configuração do React Native. Se você estiver usando uma configuração diferente para o seu app, ajuste sua implementação conforme necessário.
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

O trecho de código a seguir mostra como importar o SDK or kit de desenvolvimento de software da Braze no topo do arquivo `AppDelegate.m`:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

No método `application:didFinishLaunchingWithOptions:`, substitua a [chave]({{site.baseurl}}/api/identifier_types) de API or interface de programação do aplicativo (API) e o [endpoint]({{site.baseurl}}/api/basics#endpoints) pelos valores do seu app. Em seguida, crie a instância da Braze usando a configuração e crie uma propriedade estática no `AppDelegate` para fácil acesso.

{% alert note %}
Nosso exemplo assume uma implementação de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que fornece várias abstrações na configuração do React Native. Se você estiver usando uma configuração diferente para o seu app, ajuste sua implementação conforme necessário.
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

### Etapa 3: Inicialize o SDK or kit de desenvolvimento de software {#step-3-initialize-the-sdk}

{% tabs %}
{% tab React Native SDK or kit de desenvolvimento de software 19.2.0+ %}

O trecho de código a seguir mostra como importar a biblioteca no seu código React Native:

```javascript
import Braze from "@braze/react-native-sdk";
```

{% alert note %}
O React Native SDK or kit de desenvolvimento de software 19.2.0+ suporta a inicialização da Braze a partir da camada React Native ou das camadas nativas iOS e Android. Inicialize a partir da camada React Native para usar a [inicialização atrasada](#delayed-initialization), que inicia o SDK or kit de desenvolvimento de software após um evento como consentimento ou login. Se o seu app inicializa a Braze nas camadas nativas atualmente, você pode manter essa configuração ao fazer o upgrade. Para confirmar como as notificações se comportam em cada configuração, consulte [Notificações por push na inicialização a frio](#push-notifications-on-cold-start).
{% endalert %}

Em seguida, chame `Braze.initialize()` com a chave de API or interface de programação do aplicativo (API) do identificador do app e o endpoint do SDK or kit de desenvolvimento de software para criar a instância da Braze. Veja as opções a seguir para saber onde chamar esse método no fluxo do seu app.

#### Inicialização padrão {#standard-initialization}

O trecho de código a seguir mostra como inicializar o SDK or kit de desenvolvimento de software quando o app inicia, chamando `Braze.initialize()` em um `useEffect`:

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

O trecho de código a seguir mostra como adiar a inicialização do SDK or kit de desenvolvimento de software para mais tarde na sessão. Por exemplo, após o usuário conceder consentimento ou concluir o login:

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
No iOS, as notificações por push recebidas antes de `Braze.initialize()` são enfileiradas e processadas após a inicialização. No Android, a Braze não resolve deep links de notificações por push enquanto o SDK or kit de desenvolvimento de software aguarda ser inicializado. Para manter as notificações funcionando quando uma delas inicia o app, consulte [Notificações por push na inicialização a frio](#push-notifications-on-cold-start).
{% endalert %}

#### Chaves de API or interface de programação do aplicativo (API) específicas por plataforma {#platform-specific-api-keys}

O trecho de código a seguir mostra como usar a detecção de plataforma quando seus apps Android e iOS usam chaves de API or interface de programação do aplicativo (API) diferentes:

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

Você pode chamar `Braze.initialize()` várias vezes para reinicializar o SDK or kit de desenvolvimento de software com uma chave de API or interface de programação do aplicativo (API) e endpoint diferentes durante a sessão. Cada chamada destrói a instância anterior da Braze e cria uma nova.

{% alert important %}
Todas as chamadas de métodos do SDK or kit de desenvolvimento de software feitas antes de `Braze.initialize()` são ignoradas no iOS, então chame `Braze.initialize()` antes de usar quaisquer outros métodos da Braze.
{% endalert %}

#### Notificações por push na inicialização a frio {#push-notifications-on-cold-start}

Quando uma notificação inicia o app a partir de um estado encerrado, a Braze armazena a carga útil da notificação na camada nativa antes que o React Native carregue. Por isso, inicializar a partir da camada React Native não altera se a carga útil chega ao seu app. Para lidar com essas notificações, adicione os hooks nativos e então leia a carga útil no código React Native.

No Android, chame `BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)` no método `onCreate()` da classe `MainActivity`:

```kotlin
import com.braze.reactbridge.BrazeReactUtils

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
}
```

No iOS, chame `populateInitialPayload(fromLaunchOptions:)` no método `application(_:didFinishLaunchingWithOptions:)` do seu `AppDelegate`:

```swift
if let launchOptions {
  BrazeReactUtils.sharedInstance().populateInitialPayload(fromLaunchOptions: launchOptions)
}
```

Em seguida, leia a carga útil no código React Native:

```javascript
Braze.getInitialPushPayload((pushPayload) => {
  if (pushPayload) {
    // Handle the notification, such as navigating to the pushPayload.url value
  }
});
```

{% alert important %}
Quando a inicialização atrasada está ativada no Android, a Braze abre a atividade principal em vez de resolver o deep link na notificação, e então passa os dados da notificação para essa atividade. Lide com a navegação no código React Native usando o valor `url` de `Braze.getInitialPushPayload()`.
{% endalert %}

Suas configurações de registro de push permanecem na configuração nativa para ambos os locais de inicialização, e a Braze as aplica quando `Braze.initialize()` é executado:

- No Android, defina `com_braze_firebase_cloud_messaging_registration_enabled` e `com_braze_firebase_cloud_messaging_sender_id` no `braze.xml`.
- No iOS, defina as propriedades `push` no objeto de configuração na closure `configure` que você passa para `BrazeReactInitializer.configure`.

Se o seu app depende de deep links de notificações que o iniciam a partir de um estado encerrado, use o React Native SDK or kit de desenvolvimento de software 21.1.0 ou posterior. Essas versões incluem correções para capturar a carga útil inicial do push e resolver deep links de push no Android. Para a lista completa de alterações, consulte o [changelog do SDK or kit de desenvolvimento de software React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md).

{% endtab %}
{% tab React Native SDK or kit de desenvolvimento de software 19.1.0 e anterior %}

Para o React Native SDK or kit de desenvolvimento de software 19.1.0 e anterior, a inicialização nativa acontece na etapa 2. Importe a biblioteca no código React Native para chamar os métodos da Braze. Para mais detalhes, confira nosso [projeto de exemplo](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject).

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### Etapa 4: Teste a integração (opcional) {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK or kit de desenvolvimento de software 19.2.0+ %}

Você pode verificar se o SDK or kit de desenvolvimento de software está integrado consultando as estatísticas de sessão no dashboard. Se você executar o app em qualquer plataforma, deverá ver uma nova sessão no dashboard (na seção **Overview**).

O trecho de código a seguir mostra como abrir uma sessão para um usuário específico no seu app:

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

Procure o usuário com `{some-user-id}` no dashboard em **Audience** > **Search Users**. Lá, você pode verificar se os dados de sessão e dispositivo foram registrados.

{% endtab %}
{% tab React Native SDK or kit de desenvolvimento de software 19.1.0 e anterior %}

Para testar a integração do SDK or kit de desenvolvimento de software, o trecho de código a seguir mostra como iniciar uma nova sessão em qualquer plataforma para um usuário.

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

No dashboard da Braze, acesse [Pesquisa de usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search) e procure o usuário com o ID correspondente a `some-user-id`. Lá, você pode verificar se os dados de sessão e dispositivo foram registrados.

{% endtab %}
{% endtabs %}

## Testando com Jest {#testing-with-jest}

Os testes unitários do React Native que importam o SDK or kit de desenvolvimento de software da Braze precisam de mocks para módulos nativos e para o Braze Turbo Module. O [repositório do SDK or kit de desenvolvimento de software React Native da Braze](https://github.com/braze-inc/braze-react-native-sdk) inclui uma configuração de referência do Jest em [`__tests__/jest.setup.js`](https://github.com/braze-inc/braze-react-native-sdk/blob/master/__tests__/jest.setup.js). Adicione esse arquivo (ou uma cópia adaptada) ao `setupFiles` na configuração do Jest para que `NativeEventEmitter`, `TurboModuleRegistry` e `BrazeReactBridge` sejam simulados (mocked) quando você testar componentes que chamam APIs da Braze.

## Próximos passos {#next-steps}

Após integrar o SDK or kit de desenvolvimento de software da Braze, você pode começar a implementar recursos comuns de envio de mensagens:

- [Notificações por push]({{site.baseurl}}/developer_guide/push_notifications): Configure e envie notificações por push para seus usuários.
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages): Exiba mensagens contextuais dentro do seu app.
- [Banners]({{site.baseurl}}/developer_guide/banners): Mostre banners persistentes na interface do seu app.