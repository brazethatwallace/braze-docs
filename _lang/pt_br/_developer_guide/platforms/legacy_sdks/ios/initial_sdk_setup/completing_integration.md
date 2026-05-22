---
nav_title: Concluindo a integração
article_title: Complete a integração do SDK iOS
platform: iOS
description: "Este artigo de referência mostra como concluir a integração do SDK da Braze depois de instalá-lo por meio de uma das opções de integração."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Complete a integração {#complete-the-integration}

Antes de seguir estas etapas, certifique-se de que você já integrou o SDK usando [Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration/), [CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods/), [Swift Package Manager]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager/) ou uma integração [manual]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/).

## Etapa 1: Atualize seu delegado do app {#step-1-update-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Se estiver fazendo a integração do SDK da Braze com CocoaPods, Carthage ou com uma [integração manual dinâmica]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/), adicione a seguinte linha de código ao seu arquivo `AppDelegate.m`:

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Se estiver fazendo a integração com o Swift Package Manager ou com uma [integração manual estática]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/), use esta linha:

```objc
#import "AppboyKit.h"
```

Em seguida, no arquivo `AppDelegate.m`, adicione o seguinte snippet no método `application:didFinishLaunchingWithOptions:`:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` com o valor correto da sua página **Gerenciar configurações**. Consulte nossa [documentação da API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) para saber mais sobre onde encontrar a chave de API do identificador do app.

{% endtab %}
{% tab swift %}

Se estiver fazendo a integração do SDK da Braze com CocoaPods, Carthage ou com uma [integração manual dinâmica]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/), adicione a seguinte linha de código ao seu arquivo `AppDelegate.swift`:

```swift
import Appboy_iOS_SDK
```

Se estiver fazendo a integração com o Swift Package Manager ou com uma [integração manual estática]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options/), use esta linha:

```swift
import AppboyKit
```
Consulte os [documentos para desenvolvedores da Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html) para saber mais sobre o uso de código Objective-C em projetos Swift.

Em seguida, em `AppDelegate.swift`, adicione o seguinte snippet ao método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` com o valor correto da sua página **Gerenciar configurações**. Consulte nossa [documentação da API]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) para saber mais sobre onde encontrar a chave de API do identificador do app.

{% endtab %}
{% endtabs %}

{% alert note %}
O singleton `sharedInstance` será nulo antes de `startWithApiKey:` ser chamado, pois esse é um pré-requisito para usar qualquer funcionalidade da Braze.
{% endalert %}

{% alert warning %}
Certifique-se de inicializar a Braze na thread principal do seu aplicativo. A inicialização de forma assíncrona pode levar a uma funcionalidade interrompida.
{% endalert %}


## Etapa 2: Especifique seu cluster de dados {#step-2-specify-your-data-cluster}

{% alert note %}
A partir de dezembro de 2019, os endpoints personalizados não são mais fornecidos. Se você tiver um endpoint personalizado pré-existente, poderá continuar usando-o. Para saber mais, consulte nossa <a href="{{site.baseurl}}/api/basics/#endpoints">lista de endpoints disponíveis</a>.
{% endalert %}

### Configuração do endpoint em tempo de compilação (recomendado) {#compile-time-endpoint-configuration-recommended}

Se for fornecido um endpoint personalizado pré-existente:
- A partir do SDK da Braze para iOS v3.0.2, você pode definir um endpoint personalizado usando o arquivo `Info.plist`. Adicione o dicionário `Braze` ao seu arquivo `Info.plist`. Dentro do dicionário `Braze`, adicione a subentrada string `Endpoint` e defina o valor como a autoridade do URL do seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`). Antes do Braze iOS SDK v4.0.2, deve-se utilizar a chave do dicionário `Appboy` no lugar de `Braze`.

Seu representante da Braze já deve ter informado sobre o [endpoint correto]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/).

### Configuração do endpoint em tempo de execução {#runtime-endpoint-configuration}

Se for fornecido um endpoint personalizado pré-existente:
- A partir do Braze iOS SDK v3.17.0+, você pode substituir a definição do seu endpoint pela chave `ABKEndpointKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina o valor como a autoridade do URL do seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`).

## Integração do SDK concluída {#sdk-integration-complete}

Agora, a Braze deve estar coletando dados do seu aplicativo, e sua integração básica deve estar concluída. Consulte os artigos a seguir para ativar o [rastreamento de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift), o [envio de mensagens push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/) e o conjunto completo de recursos da Braze.

## Personalização da Braze na inicialização {#customizing-braze-on-startup}

Se desejar personalizar a Braze na inicialização, você pode usar o método de inicialização da Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` e passar um `NSDictionary` opcional de chaves de inicialização da Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

No seu arquivo `AppDelegate.m`, no método `application:didFinishLaunchingWithOptions:`, adicione o seguinte método da Braze:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Note que esse método substituiria o método de inicialização `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% tab swift %}

Em `AppDelegate.swift`, no método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, adicione o seguinte método da Braze, em que `appboyOptions` é um `Dictionary` de valores de configuração de inicialização:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Note que esse método substituiria o método de inicialização `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% endtabs %}

Esse método é chamado com os seguintes parâmetros:

- `YOUR-APP-IDENTIFIER-API-KEY` – Sua chave de API do [identificador do app]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key) no dashboard da Braze.
- `application` – O app atual.
- `launchOptions` – As opções `NSDictionary` que você obtém em `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` – Um `NSDictionary` opcional com valores de configuração de inicialização para a Braze.

Consulte [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para ver a lista de chaves de inicialização da Braze.

## Appboy.sharedInstance() e a anulabilidade do Swift {#appboysharedinstance-and-swift-nullability}
Diferentemente da prática comum, o singleton `Appboy.sharedInstance()` é opcional. Isso ocorre porque `sharedInstance` é `nil` antes da chamada de `startWithApiKey:`, e há algumas implementações não padronizadas, mas ainda válidas, nas quais uma inicialização postergada pode ser utilizada.

Se você chamar `startWithApiKey:` no seu delegado `didFinishLaunchingWithOptions:` antes de qualquer acesso ao `sharedInstance` do Appboy (a implementação padrão), poderá usar o encadeamento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar verificações complicadas. Isso terá paridade com uma implementação em Objective-C que assume um `sharedInstance` não nulo.

## Recursos adicionais {#additional-resources}

A [documentação completa da classe do iOS](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html) está disponível para fornecer orientações adicionais sobre quaisquer métodos do SDK.