## Integrando o SDK Swift {#integrating-the-swift-sdk}

Você pode integrar e personalizar o SDK Swift da Braze usando o Swift Package Manager (SPM), CocoaPods ou métodos de integração manual. Para saber mais sobre os vários símbolos do SDK, consulte a [documentação de referência do Braze Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/).

### Pré-requisitos {#prerequisites}

Antes de começar, verifique se seu ambiente é compatível com a [última versão do SDK Swift da Braze](https://github.com/braze-inc/braze-swift-sdk#version-information).

### Etapa 1: Instale o SDK Swift da Braze {#step-1-install-the-braze-swift-sdk}

Recomendamos usar o [Swift Package Manager (SwiftPM)](https://swift.org/package-manager/) ou [CocoaPods](http://cocoapods.org/) para instalar o SDK Swift da Braze. Alternativamente, você pode instalar o SDK manualmente.

{% tabs local %}
{% tab Swift Package Manager %}
#### Etapa 1.1: Importar versão do SDK {#step-11-import-sdk-version}

Abra seu projeto e navegue até as configurações do seu projeto. Selecione a guia **Swift Packages** e clique no botão adicionar <i class="fas fa-plus"></i> abaixo da lista de pacotes.

![Configurações do projeto Xcode com a guia Swift Packages e o botão de adicionar pacote.]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
A partir da versão 7.4.0, o SDK Swift da Braze tem canais de distribuição adicionais como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) e [XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Se você quiser usar qualquer um desses formatos, siga as instruções de instalação do respectivo repositório.
{% endalert %}

Digite a URL do nosso repositório iOS Swift SDK `https://github.com/braze-inc/braze-swift-sdk` no campo de texto. Na seção **Dependency Rule**, selecione a versão do SDK. Por fim, clique em **Add Package**.

![Diálogo de adicionar pacote do Xcode com a URL do repositório do SDK Swift da Braze inserida.]({% image_buster /assets/img/importsdk_example.png %})

#### Etapa 1.2: Selecione seus pacotes {#step-12-select-your-packages}

O SDK Swift da Braze separa os recursos em bibliotecas independentes para fornecer aos desenvolvedores mais controle sobre quais recursos importar para seus projetos.

| Pacote | Detalhes |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BrazeKit`      | Biblioteca principal do SDK que fornece suporte para análise de dados e notificações por push. |
| `BrazeLocation` | Biblioteca de localização que fornece suporte para análise de dados de local e monitoramento de geofence. |
| `BrazeUI`       | Biblioteca de interface do usuário fornecida pela Braze para mensagens no app, Content Cards e Banners. Importe esta biblioteca se você pretende usar os componentes de UI padrão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1.2: Selecione seus pacotes" }

{: .ws-td-nw-1}

##### Sobre bibliotecas de extensão {#about-extension-libraries}

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) e [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) são módulos de extensão que fornecem funcionalidade adicional e não devem ser adicionados diretamente ao alvo principal do seu aplicativo. Em vez disso, siga os guias vinculados para integrá-los separadamente em suas respectivas extensões de destino.
{% endalert %}

| Pacote | Detalhes |
| -------------------------- | ------------------------------------------------------------------------------------- |
| `BrazeNotificationService` | Biblioteca de extensão de serviço de notificação que fornece suporte para notificações por push avançadas. |
| `BrazePushStory`           | Biblioteca de extensão de conteúdo de notificação que fornece suporte para Push Stories. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sobre bibliotecas de extensão" }

{: .ws-td-nw-1}

Selecione o pacote que melhor atenda às suas necessidades e clique em **Add Package**. Certifique-se de selecionar `BrazeKit` no mínimo.

![Lista de produtos de pacotes do Xcode selecionando BrazeKit antes de adicionar o pacote.]({% image_buster /assets/img/add_package.png %})
{% endtab %}

{% tab CocoaPods %}
#### Etapa 1.1: Instalar o CocoaPods {#step-11-install-cocoapods}

Para um guia completo, consulte o [Guia de Introdução do CocoaPods](https://guides.cocoapods.org/using/getting-started.html). Caso contrário, você pode executar o seguinte comando para começar rapidamente:

```bash
$ sudo gem install cocoapods
```

Se você ficar preso, confira o [Guia de Solução de Problemas do CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

#### Etapa 1.2: Construindo o Podfile {#step-12-constructing-the-podfile}

Em seguida, crie um arquivo no diretório do seu projeto Xcode chamado `Podfile`.

{% alert note %}
A partir da versão 7.4.0, o SDK Swift da Braze tem canais de distribuição adicionais como [XCFrameworks estáticos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) e [XCFrameworks dinâmicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Se você quiser usar qualquer um desses formatos, siga as instruções de instalação do respectivo repositório.
{% endalert %}

Adicione a seguinte linha ao seu Podfile:

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contém a biblioteca principal do SDK que oferece suporte a análise de dados e notificações por push.

Sugerimos que você versione a Braze para que as atualizações do pod capturem automaticamente qualquer coisa menor que uma atualização de versão secundária. Fica assim: `pod 'BrazeKit' ~> Major.Minor.Build`. Se quiser integrar automaticamente a versão mais recente do SDK da Braze, mesmo com grandes alterações, você poderá usar `pod 'BrazeKit'` em seu Podfile.

##### Sobre bibliotecas adicionais {#about-additional-libraries}

O SDK Swift da Braze separa os recursos em bibliotecas independentes para fornecer aos desenvolvedores mais controle sobre quais recursos importar para seus projetos. Além de `BrazeKit`, você pode adicionar as seguintes bibliotecas ao seu Podfile:

| Biblioteca | Detalhes |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pod 'BrazeLocation'` | Biblioteca de localização que fornece suporte para análise de dados de local e monitoramento de geofence. |
| `pod 'BrazeUI'`       | Biblioteca de interface do usuário fornecida pela Braze para mensagens no app, Content Cards e Banners. Importe esta biblioteca se você pretende usar os componentes de UI padrão. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Sobre bibliotecas adicionais" }

{: .ws-td-nw-1}

###### Bibliotecas de extensão {#extension-libraries}

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) e [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) são módulos de extensão que fornecem funcionalidade adicional e não devem ser adicionados diretamente ao alvo principal do seu aplicativo. Em vez disso, será necessário criar alvos de extensão separados para cada um desses módulos e importar os módulos da Braze para seus alvos correspondentes.

| Biblioteca | Detalhes |
| -------------------------------- | ------------------------------------------------------------------------------------- |
| `pod 'BrazeNotificationService'` | Biblioteca de extensão de serviço de notificação que fornece suporte para notificações por push avançadas. |
| `pod 'BrazePushStory'`           | Biblioteca de extensão de conteúdo de notificação que fornece suporte para Push Stories. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Bibliotecas de extensão" }

{: .ws-td-nw-1}

#### Etapa 1.3: Instalar o SDK {#step-13-install-the-sdk}

Para instalar o SDK da Braze via CocoaPods, navegue até o diretório do seu projeto de app do Xcode em seu terminal e execute o seguinte comando:
```
pod install
```

Nesse ponto, você deve conseguir abrir o novo espaço de trabalho do projeto Xcode criado pelo CocoaPods. Use esse espaço de trabalho do Xcode em vez do seu projeto do Xcode.

![Uma pasta de exemplo da Braze expandida para mostrar o novo `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

#### Atualizando o SDK usando CocoaPods {#updating-the-sdk-using-cocoapods}

Para atualizar um CocoaPod, basta executar o seguinte comando no diretório do projeto:

```
pod update
```
{% endtab %}

{% tab Manual %}
#### Etapa 1.1: Baixar o SDK da Braze {#step-11-download-the-braze-sdk}

Acesse a [página de lançamento do SDK da Braze no GitHub](https://github.com/braze-inc/braze-swift-sdk/releases) e baixe `braze-swift-sdk-prebuilt.zip`.

![A página de lançamento do SDK da Braze no GitHub.]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

#### Etapa 1.2: Escolha seus frameworks {#step-12-choose-your-frameworks}

O SDK Swift da Braze contém uma variedade de XCFrameworks independentes, o que lhe dá a liberdade de integrar os recursos que você deseja&#8212;sem precisar integrá-los todos. Consulte a tabela a seguir para escolher seus XCFrameworks:

| Pacote | Obrigatório? | Descrição |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Sim       | Biblioteca principal do SDK que fornece suporte para análise de dados e notificações por push. |
| `BrazeLocation`            | Não       | Biblioteca de localização que fornece suporte para análise de dados de local e monitoramento de geofence. |
| `BrazeUI`                  | Não       | Biblioteca de interface do usuário fornecida pela Braze para mensagens no app, Content Cards e Banners. Importe esta biblioteca se você pretende usar os componentes de UI padrão. |
| `BrazeNotificationService` | Não       | Biblioteca de extensão de serviço de notificação que fornece suporte para notificações por push avançadas. Não adicione esta biblioteca diretamente ao alvo principal do seu aplicativo; em vez disso, [adicione a biblioteca `BrazeNotificationService` separadamente](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications). |
| `BrazePushStory`           | Não       | Biblioteca de extensão de conteúdo de notificação que fornece suporte para Push Stories. Não adicione esta biblioteca diretamente ao alvo principal do seu aplicativo; em vez disso, [adicione a biblioteca `BrazePushStory` separadamente](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories). |
| `BrazeKitCompat`           | Não       | Biblioteca de compatibilidade contendo todas as classes e métodos `Appboy` e `ABK*` que estavam disponíveis na versão `Appboy-iOS-SDK` 4.X.X. Para mais informações sobre o uso, consulte o cenário de migração mínima no [guia de migração](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `BrazeUICompat`            | Não       | Biblioteca de compatibilidade contendo todas as classes e métodos `ABK*` que estavam disponíveis na biblioteca `AppboyUI` da versão `Appboy-iOS-SDK` 4.X.X. Para mais informações sobre o uso, consulte o cenário de migração mínima no [guia de migração](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | Não       | Dependência usada apenas por `BrazeUICompat` no cenário de migração mínima. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Etapa 1.2: Escolha seus frameworks" }

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 1.2: Escolha seus frameworks" }

#### Etapa 1.3: Prepare seus arquivos {#step-13-prepare-your-files}

Decida se você quer usar XCFrameworks **estáticos** ou **dinâmicos** e prepare seus arquivos:

1. Crie um diretório temporário para seus XCFrameworks.
2. No `braze-swift-sdk-prebuilt`, abra o diretório `dynamic` e mova `BrazeKit.xcframework` para o seu diretório. Seu diretório deve ser semelhante ao seguinte:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Mova cada um dos seus [XCFrameworks escolhidos](#swift_step-2-choose-your-frameworks) para o seu diretório temporário. Seu diretório deve ser semelhante ao seguinte:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```

#### Etapa 1.4: Integre seus frameworks {#step-14-integrate-your-frameworks}

Em seguida, integre os XCFrameworks **dinâmicos** ou **estáticos** que você [preparou anteriormente](#swift_step-3-prepare-your-files):

No seu projeto Xcode, selecione seu alvo de build e depois **General**. Em **Frameworks, Libraries, and Embedded Content**, arraste e solte os [arquivos que você preparou anteriormente](#swift_step-3-prepare-your-files).

![Um projeto de exemplo do Xcode com cada biblioteca da Braze configurada para "Embed & Sign".]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert note %}
A partir do SDK Swift 12.0.0, você deve sempre selecionar **Embed & Sign** para os XCFrameworks da Braze, tanto para as variantes estáticas quanto dinâmicas. Isso garante que os recursos dos frameworks sejam devidamente incorporados no pacote do seu app.
{% endalert %}

{% alert tip %}
Para ativar o suporte a GIF, adicione `SDWebImage.xcframework`, localizado em `braze-swift-sdk-prebuilt/static` ou `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}

#### Erros comuns para projetos Objective-C {#common-errors-for-objective-c-projects}

Se o seu projeto Xcode contiver apenas arquivos Objective-C, você poderá receber erros de "missing symbol" ao tentar compilar seu projeto. Para corrigir esses erros, abra seu projeto e adicione um arquivo Swift vazio à sua árvore de arquivos. Isso forçará sua cadeia de ferramentas a incorporar o [Swift Runtime](https://support.apple.com/kb/dl1998) e vincular aos frameworks apropriados durante o build.

```bash
FILE_NAME.swift
```

Substitua `FILE_NAME` por qualquer string sem espaços. Seu arquivo deve ser semelhante ao seguinte:

```bash
empty_swift_file.swift
```
{% endtab %}
{% endtabs local %}

### Etapa 2: Configurar inicialização atrasada (opcional) {#step-2-set-up-delayed-initialization-optional}

Você pode optar por atrasar quando o SDK Swift da Braze é inicializado, o que é útil se seu app precisar carregar uma configuração ou esperar pelo consentimento do usuário antes de iniciar o SDK. A inicialização atrasada garante que as notificações por push da Braze e os tokens de push recebidos antes da inicialização do SDK sejam enfileirados e processados assim que o SDK for inicializado.

Para usar a inicialização atrasada, a versão mínima do SDK da Braze é necessária:
{% sdk_min_versions swift:11.2.0 %}

#### Etapa 2.1: Prepare-se para a inicialização atrasada {#step-21-prepare-for-delayed-initialization}

Chame `Braze.prepareForDelayedInitialization()` o mais cedo possível no ciclo de vida do seu app, idealmente em ou antes de `application(_:didFinishLaunchingWithOptions:)`. Isso garante que as notificações por push recebidas antes da inicialização do SDK sejam devidamente capturadas e processadas posteriormente.

{% alert note %}
Isso se aplica apenas às notificações por push da Braze. Outras notificações por push são tratadas normalmente pelos delegados do sistema.
{% endalert %}

{% tabs %}
{% tab Swift %}
{% subtabs local %}
{% subtab UIKit %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
  // Prepare the SDK for delayed initialization
  Braze.prepareForDelayedInitialization()

  // ... Additional non-Braze setup code

  return true
}
```
{% endsubtab %}

{% subtab SwiftUI %}
```swift
@main
struct MyApp: App {
  @UIApplicationDelegateAdaptor var appDelegate: AppDelegate

  var body: some Scene {
    WindowGroup {
      ContentView()
    }
  }
}

class AppDelegate: NSObject, UIApplicationDelegate {
  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
    // Prepare the SDK for delayed initialization
    Braze.prepareForDelayedInitialization()

    // ... Additional non-Braze setup code

    return true
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Prepare the SDK for delayed initialization
  [Braze prepareForDelayedInitialization];

  // ... Additional non-Braze setup code

  return YES;
}
```
{% endtab %}
{% endtabs %}

Ao usar a inicialização atrasada, a automação de notificações por push é implicitamente ativada. Você pode [personalizar a automação de push](#swift_step-23-customize-push-automation-optional) passando um parâmetro `pushAutomation`.

#### Etapa 2.2: Configurar o comportamento da análise de push (opcional) {#step-22-configure-push-analytics-behavior-optional}

Quando a inicialização atrasada está ativada, as análises de push são enfileiradas por padrão. No entanto, você pode optar por enfileirar ou descartar explicitamente as análises de push.

##### Enfileirar explicitamente {#explicitly-queue}

Para enfileirar explicitamente as análises de push (comportamento padrão), passe `.queue` para o parâmetro `analyticsBehavior`. Eventos de análises de push que são enfileirados antes da inicialização serão processados e enviados ao servidor na inicialização.

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .queue)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

##### Descartar {#drop}

Para descartar as análises de push recebidas antes da inicialização do SDK, passe `.drop` para o parâmetro `analyticsBehavior`. Com esta opção, qualquer evento de análise de push que ocorrer enquanto o SDK não estiver inicializado será ignorado.

{% tabs local %}
{% tab Swift %}
```swift
Braze.prepareForDelayedInitialization(analyticsBehavior: .drop)
```
{% endtab %}
{% tab Objective-C %}
```objc
[Braze prepareForDelayedInitializationWithAnalyticsBehavior:BRZPushEnqueueBehaviorDrop];
```
{% endtab %}
{% endtabs %}

#### Etapa 2.3: Personalizar automação de push (opcional) {#step-23-customize-push-automation-optional}

Você pode personalizar a configuração da automação de push passando um parâmetro `pushAutomation`. Por padrão, todos os recursos de automação estão habilitados, exceto `requestAuthorizationAtLaunch`.

{% tabs local %}
{% tab SWIFT %}
```swift
// Enable all push automation
featuresBraze.prepareForDelayedInitialization(pushAutomation: true)

// Or customize specific automation options
let automation = Braze.Configuration.Push.Automation()
automation.automaticSetup = true
automation.requestAuthorizationAtLaunch = false
Braze.prepareForDelayedInitialization(pushAutomation: automation)
```
{% endtab %}

{% tab OBJECTIVE-C %}
```objc
// Enable all push automation features
[Braze prepareForDelayedInitializationWithPushAutomation:[[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES]];

// Or customize specific automation options
BRZConfigurationPushAutomation *automation = [[BRZConfigurationPushAutomation alloc] init];
automation.automaticSetup = YES;
automation.requestAuthorizationAtLaunch = NO;
[Braze prepareForDelayedInitializationWithPushAutomation:automation analyticsBehavior:BRZPushEnqueueBehaviorQueue];
```
{% endtab %}
{% endtabs %}

#### Etapa 2.4: Inicializar o SDK {#step-24-initialize-the-sdk}

Após o período de postergação escolhido (por exemplo, após buscar a configuração de um servidor ou após o consentimento do usuário), inicialize o SDK normalmente:

{% tabs local %}
{% tab SWIFT %}
```swift
func initializeBraze() {
  let configuration = Braze.Configuration(apiKey: "YOUR-API-KEY", endpoint: "YOUR-ENDPOINT")

  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = true
  let braze = Braze(configuration: configuration)

  // Store the Braze instance for later use
  AppDelegate.braze = braze
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (void)initializeBraze {
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"YOUR-API-KEY" endpoint:@"YOUR-ENDPOINT"];

  // Enable push automation to match the delayed initialization configuration
  configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  Braze *braze = [[Braze alloc] initWithConfiguration:configuration];

  // Store the Braze instance for later use
  AppDelegate.braze = braze;
}
```
{% endtab %}
{% endtabs %}

{% alert note %}
Quando o SDK estiver inicializado, todas as notificações por push enfileiradas, tokens de push e deep links são processados automaticamente.
{% endalert %}

### Etapa 3: Atualize seu delegado do app {#step-3-update-your-app-delegate}

{% alert important %}
O seguinte assume que você já adicionou um `AppDelegate` ao seu projeto (que não é gerado por padrão) e que você não está usando o recurso de inicialização atrasada. Se você não planeja usar um `AppDelegate`, certifique-se de inicializar o SDK da Braze o mais cedo possível, como durante o lançamento do app. Se você estiver usando o recurso de inicialização atrasada, consulte a [Etapa 2.4](#swift_step-24-initialize-the-sdk) para inicializar o SDK e ignore esta etapa.
{% endalert %}

{% subtabs local %}
{% subtab swift %}
Adicione a seguinte linha de código ao seu arquivo `AppDelegate.swift` para importar os recursos incluídos no SDK Swift da Braze:

```swift
import BrazeKit
```

Em seguida, adicione uma propriedade estática à sua classe `AppDelegate` para manter uma referência forte à instância da Braze durante toda a vida útil do seu aplicativo:

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil
}
```

O SDK requer que seu aplicativo mantenha uma referência forte à instância da Braze durante todo o seu uso. Para evitar efeitos colaterais inesperados, certifique-se de que você capturou totalmente essa referência antes de acessar ou modificar quaisquer propriedades ou métodos na instância da Braze.

Por fim, em `AppDelegate.swift`, adicione o seguinte trecho ao seu método `application:didFinishLaunchingWithOptions:`:

```swift
let configuration = Braze.Configuration(
    apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
    endpoint: "YOUR-BRAZE-ENDPOINT"
)
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` e `YOUR-BRAZE-ENDPOINT` com o valor correto da sua página de **Configurações do app**. Confira nossos [tipos de identificadores de API]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) para saber mais sobre onde encontrar a chave de API do seu identificador de app.

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Adicione a seguinte linha de código ao seu arquivo `AppDelegate.m`:

```objc
@import BrazeKit;
```

Em seguida, adicione uma variável estática ao seu arquivo `AppDelegate.m` para manter uma referência à instância da Braze durante toda a vida útil do seu aplicativo:

```objc
static Braze *_braze;

@implementation AppDelegate
+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
@end
```

O SDK requer que seu aplicativo mantenha uma referência forte à instância da Braze durante todo o seu uso. Para evitar efeitos colaterais inesperados, certifique-se de que você capturou totalmente essa referência antes de acessar ou modificar quaisquer propriedades ou métodos na instância da Braze.

Por fim, dentro do seu arquivo `AppDelegate.m`, adicione o seguinte trecho dentro do seu método `application:didFinishLaunchingWithOptions:`:

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:"YOUR-APP-IDENTIFIER-API-KEY"
                                                                  endpoint:"YOUR-BRAZE-ENDPOINT"];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` e `YOUR-BRAZE-ENDPOINT` com o valor correto da sua página **Gerenciar configurações**. Confira nossa [documentação da API]({{site.baseurl}}/api/api_key#the-app-identifier-api-key) para saber mais sobre onde encontrar a chave de API do seu identificador de app.

{% endsubtab %}
{% endsubtabs local %}

{% alert note %}
`Braze.init` retorna imediatamente na thread de chamada. O SDK processa o trabalho de inicialização em uma fila interna. A leitura de propriedades síncronas como `braze.deviceId` diretamente após `init` na thread principal bloqueará a thread de chamada até que o SDK tenha concluído suas operações pós-inicialização. Para contextos na thread principal ou sensíveis à latência, use `braze.getDeviceId(_:)` (Swift) ou `[braze getDeviceIdWithCompletion:^(NSString *deviceId) { ... }]` (Objective-C) para ler o valor sem bloqueio.
{% endalert %}

## Configurações opcionais {#optional-configurations}

### Registro {#logging}

Para uma visão centralizada em todas as plataformas, veja [Registro detalhado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Para aprender a interpretar a saída do registro, veja [Lendo registros detalhados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

#### Níveis de registro {#log-levels}

O nível de registro padrão para o SDK Swift da Braze é `.error`&#8212;é também o nível mínimo suportado quando os registros estão habilitados. Esta é a lista completa de níveis de registro:

| Swift       | Objective-C              | Descrição |
| ----------- | ------------------------ | ------------------------------------------------------------ |
| `.debug`    | `BRZLoggerLevelDebug`    | Registrar informações de depuração + `.info` + `.error`. |
| `.info`     | `BRZLoggerLevelInfo`     | Registrar informações gerais do SDK (alterações de usuário, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Registrar erros. |
| `.disabled` | `BRZLoggerLevelDisabled` | Nenhum registro ocorre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Níveis de registro" }

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Níveis de registro" }

#### Definindo o nível de registro {#setting-the-log-level}

Você pode atribuir o nível de registro em tempo de execução no seu objeto `Braze.Configuration`. Para detalhes completos de uso, veja [`Braze.Configuration.Logger`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}