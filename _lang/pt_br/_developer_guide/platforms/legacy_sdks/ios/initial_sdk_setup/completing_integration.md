---
nav_title: Concluindo a integração
article_title: Complete a integração do SDK or kit de desenvolvimento de software iOS
platform: iOS
description: "Este artigo de referência mostra como concluir a integração do SDK or kit de desenvolvimento de software da Braze depois de instalá-lo por meio de uma das opções de integração."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Complete a integração {#complete-the-integration}

Antes de seguir estas etapas, certifique-se de que você já integrou o SDK or kit de desenvolvimento de software usando [Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration), [CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods), [Swift Package Manager]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager) ou uma integração [manual]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options).

## Etapa 1: Atualize seu app delegate {#step-1-update-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Se você está integrando o SDK or kit de desenvolvimento de software da Braze com CocoaPods, Carthage ou com uma [integração manual dinâmica]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), adicione a seguinte linha de código ao seu arquivo `AppDelegate.m`:

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Se você está integrando com Swift Package Manager ou com uma [integração manual estática]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), use esta linha no lugar:

```objc
#import "AppboyKit.h"
```

Em seguida, no seu arquivo `AppDelegate.m`, adicione o seguinte snippet dentro do seu método `application:didFinishLaunchingWithOptions:`:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` com o valor correto da sua página **Manage Settings**. Consulte nossa [documentação de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/identifier_types#app-identifier) para saber mais sobre onde encontrar sua chave de API or interface de programação do aplicativo (API) do identificador do app.

{% endtab %}
{% tab swift %}

Se você está integrando o SDK or kit de desenvolvimento de software da Braze com CocoaPods, Carthage ou com uma [integração manual dinâmica]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), adicione a seguinte linha de código ao seu arquivo `AppDelegate.swift`:

```swift
import Appboy_iOS_SDK
```

Se você está integrando com Swift Package Manager ou com uma [integração manual estática]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), use esta linha no lugar:

```swift
import AppboyKit
```
Consulte a [documentação para desenvolvedores da Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html) para saber mais sobre como usar código Objective-C em projetos Swift.

Em seguida, em `AppDelegate.swift`, adicione o seguinte snippet ao seu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Atualize `YOUR-APP-IDENTIFIER-API-KEY` com o valor correto da sua página **Manage Settings**. Consulte nossa [documentação de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/identifier_types#app-identifier) para saber mais sobre onde encontrar sua chave de API or interface de programação do aplicativo (API) do identificador do app.

{% endtab %}
{% endtabs %}

{% alert note %}
O singleton `sharedInstance` será nil antes de `startWithApiKey:` ser chamado, pois isso é um pré-requisito para usar qualquer funcionalidade da Braze.
{% endalert %}

{% alert warning %}
Certifique-se de inicializar a Braze na thread principal da sua aplicação. Inicializar de forma assíncrona pode levar a funcionalidades com comportamento incorreto.
{% endalert %}

## Etapa 2: Especifique seu cluster de dados {#step-2-specify-your-data-cluster}

{% alert note %}
Observe que, desde dezembro de 2019, endpoints personalizados não são mais fornecidos. Se você já possui um endpoint personalizado preexistente, pode continuar a usá-lo. Para saber mais, consulte nossa <a href="{{site.baseurl}}/API or interface de programação do aplicativo (API)/basics#endpoints">lista de endpoints disponíveis</a>.
{% endalert %}

### Configuração de endpoint em tempo de compilação (recomendado) {#compile-time-endpoint-configuration-recommended}

Se você recebeu um endpoint personalizado preexistente:
- A partir do Braze iOS SDK or kit de desenvolvimento de software v3.0.2, você pode definir um endpoint personalizado usando o arquivo `Info.plist`. Adicione o dicionário `Braze` ao seu arquivo `Info.plist`. Dentro do dicionário `Braze`, adicione a subentrada de string `Endpoint` e defina o valor como a autoridade da URL do seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`). Observe que, antes do Braze iOS SDK v4.0.2, a chave de dicionário `Appboy` deve ser usada no lugar de `Braze`.

Seu representante da Braze já deve ter orientado você sobre o [endpoint correto]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints).

### Configuração de endpoint em tempo de execução {#runtime-endpoint-configuration}

Se você recebeu um endpoint personalizado preexistente:
- A partir do Braze iOS SDK or kit de desenvolvimento de software v3.17.0+, você pode substituir e definir seu endpoint por meio do `ABKEndpointKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina o valor como a autoridade da URL do seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`).

## Integração SDK or kit de desenvolvimento de software concluída {#sdk-integration-complete}

A Braze agora deve estar coletando dados do seu aplicativo, e sua integração básica deve estar concluída. Consulte os artigos a seguir para ativar o [rastreamento de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift), o [envio de mensagens push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) e o pacote completo de recursos da Braze.

## Personalizando a Braze na inicialização {#customizing-braze-on-startup}

Se você deseja personalizar a Braze na inicialização, pode usar o método de inicialização da Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` e passar um `NSDictionary` opcional de chaves de inicialização da Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

No seu arquivo `AppDelegate.m`, dentro do método `application:didFinishLaunchingWithOptions:`, adicione o seguinte método da Braze:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Esse método substitui o método de inicialização `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% tab swift %}

Em `AppDelegate.swift`, dentro do método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, adicione o seguinte método da Braze, onde `appboyOptions` é um `Dictionary` de valores de configuração de inicialização:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Esse método substitui o método de inicialização `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% endtabs %}

Esse método é chamado com os seguintes parâmetros:

- `YOUR-APP-IDENTIFIER-API-KEY` – Sua chave de API or interface de programação do aplicativo (API) do [identificador do app]({{site.baseurl}}/api/identifier_types#app-identifier) no dashboard da Braze.
- `application` – O app atual.
- `launchOptions` – O `NSDictionary` de opções que você obtém de `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` – Um `NSDictionary` opcional com valores de configuração de inicialização da Braze.

Consulte [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para uma lista de chaves de inicialização da Braze.

## Appboy.sharedInstance() e nulabilidade no Swift {#appboysharedinstance-and-swift-nullability}
Diferindo um pouco da prática comum, o singleton `Appboy.sharedInstance()` é opcional. Isso ocorre porque `sharedInstance` é `nil` antes de `startWithApiKey:` ser chamado, e existem algumas implementações não padronizadas, mas válidas, em que uma inicialização postergada pode ser usada.

Se você chamar `startWithApiKey:` no delegate `didFinishLaunchingWithOptions:` antes de qualquer acesso ao `sharedInstance` da Appboy (a implementação padrão), pode usar optional chaining, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar verificações trabalhosas. Isso terá paridade com uma implementação em Objective-C que assumia um `sharedInstance` não nulo.

## Recursos adicionais {#additional-resources}

A [documentação completa das classes do iOS](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html) está disponível para fornecer orientações adicionais sobre quaisquer métodos do SDK or kit de desenvolvimento de software.