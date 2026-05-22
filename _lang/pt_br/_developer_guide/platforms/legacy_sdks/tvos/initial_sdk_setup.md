---
nav_title: Configuração inicial do SDK
article_title: Configuração inicial do SDK para tvOS
platform: tvOS
page_order: 0
page_type: reference
description: "Esta página aborda as etapas de configuração inicial do SDK da Braze para tvOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuração inicial do SDK {#initial-sdk-setup}

> Este artigo de referência aborda como instalar o SDK da Braze para tvOS. A instalação do SDK da Braze fornecerá a funcionalidade básica de análise de dados.

{% alert note %}
Nosso SDK do tvOS atualmente oferece suporte à funcionalidade de análise de dados. Para adicionar um app para tvOS em seu dashboard, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).
{% endalert %}

O SDK da Braze para tvOS deve ser instalado ou atualizado usando o [CocoaPods](http://cocoapods.org/), um gerenciador de dependências para projetos Objective-C e Swift. O CocoaPods oferece mais simplicidade para integração e atualização.

## Integração do SDK do tvOS com o CocoaPods {#tvos-sdk-cocoapods-integration}

### Etapa 1: Instalar o CocoaPods {#step-1-install-cocoapods}

A instalação do SDK por meio do tvOS [CocoaPods](http://cocoapods.org/) automatiza a maior parte do processo de instalação para você. Antes de iniciar esse processo, verifique se você está usando a [versão 2.0.0 ou superior do Ruby](https://www.ruby-lang.org/en/installation/).

Execute o seguinte comando para começar:

```bash
$ sudo gem install cocoapods
```

- Se o sistema pedir que você substitua o executável `rake`, consulte [Getting Started](http://guides.cocoapods.org/using/getting-started.html) em CocoaPods.org para obter mais detalhes.
- Se você tiver problemas relacionados ao CocoaPods, consulte o [guia de solução de problemas do CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

### Etapa 2: Construindo o Podfile {#step-2-constructing-the-podfile}

Agora que você instalou o CocoaPods Ruby Gem, precisará criar um arquivo no diretório do projeto Xcode chamado `Podfile`.

Adicione a seguinte linha ao seu Podfile:

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Sugerimos que você versione a Braze para que as atualizações do pod capturem automaticamente qualquer coisa menor que uma atualização de versão secundária. Isso se parece com `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`. Se quiser integrar automaticamente a versão mais recente do SDK da Braze, mesmo com grandes alterações, você poderá usar `pod 'Appboy-tvOS-SDK'` em seu Podfile.

### Etapa 3: Instalação do SDK da Braze {#step-3-installing-the-braze-sdk}

Para instalar o SDK da Braze via CocoaPods, navegue até o diretório do seu projeto de app do Xcode em seu terminal e execute o seguinte comando:
```
pod install
```

Nesse ponto, você deve conseguir abrir o novo espaço de trabalho do projeto Xcode criado pelo CocoaPods. Use esse espaço de trabalho do Xcode em vez do seu projeto do Xcode.

![]({% image_buster /assets/img_archive/podsworkspace.png %})

### Etapa 4: Atualização do delegate do seu app {#step-4-updating-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Adicione a seguinte linha de código ao seu arquivo `AppDelegate.m`:

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

No arquivo `AppDelegate.m`, adicione o seguinte snippet no método `application:didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Por fim, atualize `YOUR-API-KEY` com o valor correto na sua página **Gerenciar configurações**.

{% endtab %}
{% tab swift %}

Se estiver integrando o SDK da Braze com o CocoaPods ou o Carthage, adicione a seguinte linha de código ao seu arquivo `AppDelegate.swift`:

```swift
import AppboyTVOSKit
```

Para saber mais sobre o uso de código Objective-C em projetos Swift, consulte os [documentos para desenvolvedores da Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Em `AppDelegate.swift`, adicione o seguinte snippet ao seu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Em seguida, atualize `YOUR-API-KEY` com o valor correto na sua página **Gerenciar configurações**.

Nosso singleton `sharedInstance` será nulo antes de `startWithApiKey:` ser chamado, pois esse é um pré-requisito para usar qualquer funcionalidade da Braze.

{% endtab %}
{% endtabs %}

{% alert warning %}
Não se esqueça de inicializar a Braze na thread principal do seu aplicativo. A inicialização de forma assíncrona pode levar a uma funcionalidade interrompida.
{% endalert %}

### Etapa 5: Especifique seu endpoint personalizado ou cluster de dados {#step-5-specify-your-custom-endpoint-or-data-cluster}

{% alert note %}
A partir de dezembro de 2019, os endpoints personalizados não serão mais fornecidos. Se você tiver um endpoint personalizado pré-existente, poderá continuar a usá-lo. Para saber mais, consulte nossa <a href="{{site.baseurl}}/api/basics/#endpoints">lista de endpoints disponíveis</a>.
{% endalert %}

Seu representante da Braze já deve ter lhe informado sobre o [endpoint correto]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuração do endpoint em tempo de compilação (recomendado) {#compile-time-endpoint-configuration-recommended}
Se for fornecido um endpoint personalizado pré-existente:
- A partir do SDK da Braze para iOS v3.0.2, você pode definir um endpoint personalizado usando o arquivo `Info.plist`. Adicione o dicionário `Appboy` ao seu arquivo Info.plist. Dentro do dicionário `Appboy`, adicione a subentrada de string `Endpoint` e defina o valor para a autoridade dos seus URLs de endpoint personalizados (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`).

#### Configuração do endpoint em tempo de execução {#runtime-endpoint-configuration}
Se for fornecido um endpoint personalizado pré-existente:
- A partir do SDK da Braze para iOS v3.17.0+, você pode substituir a definição do seu endpoint por meio do `ABKEndpointKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina o valor como a autoridade do URL do seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, não `https://sdk.iad-01.braze.com`).

{% alert note %}
O suporte à configuração de endpoints em tempo de execução usando `ABKAppboyEndpointDelegate` foi removido no SDK da Braze para iOS v3.17.0. Se você já usa `ABKAppboyEndpointDelegate`, note que nas versões v3.14.1 a v3.16.0 do SDK da Braze para iOS, qualquer referência a `dev.appboy.com` em seu método `getApiEndpoint()` deve ser substituída por uma referência a `sdk.iad-01.braze.com`.
{% endalert %}

### Integração do SDK concluída {#sdk-integration-complete}

Agora, a Braze está coletando dados do seu aplicativo e sua integração básica está concluída. Note que, ao compilar seu app para tvOS e quaisquer outras bibliotecas de terceiros, o Bitcode deve ser ativado.

### Atualizando o SDK da Braze via CocoaPods {#updating-the-braze-sdk-via-cocoapods}

Para atualizar um CocoaPod, basta executar o seguinte comando no diretório do projeto:

```
pod update
```

## Personalização da Braze na inicialização {#customizing-braze-on-startup}

Se desejar personalizar a Braze na inicialização, você poderá usar o método de inicialização da Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` e passar um `NSDictionary` opcional de chaves de inicialização da Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

Em seu arquivo `AppDelegate.m`, no método `application:didFinishLaunchingWithOptions`, adicione o seguinte método da Braze:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

Em `AppDelegate.swift`, no método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, adicione o seguinte método da Braze:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

em que `appboyOptions` é um `Dictionary` de valores de configuração de inicialização.

{% endtab %}
{% endtabs %}

Esse método substituiria o método de inicialização `startWithApiKey:inApplication:withLaunchOptions:` e é chamado com os seguintes parâmetros:

- `YOUR-API-KEY`: A chave de API do seu aplicativo pode ser encontrada em **Gerenciar configurações** no dashboard da Braze.
- `application`: O app atual.
- `launchOptions`: As opções `NSDictionary` que você obtém em `application:didFinishLaunchingWithOptions:`.
- `appboyOptions`: Um `NSDictionary` opcional com valores de configuração de inicialização para a Braze.

Veja [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para obter uma lista das chaves de inicialização da Braze.

## Appboy.sharedInstance() e a anulabilidade do Swift {#appboysharedinstance-and-swift-nullability}
Diferentemente da prática comum, o singleton `Appboy.sharedInstance()` é opcional. Isso ocorre porque `sharedInstance` é `nil` antes da chamada de `startWithApiKey:`, e há algumas implementações não padronizadas, mas ainda válidas, nas quais uma inicialização postergada pode ser utilizada.

Se você chamar `startWithApiKey:` em seu delegado `didFinishLaunchingWithOptions:` antes de qualquer acesso ao `sharedInstance` do Appboy (a implementação padrão), poderá usar o encadeamento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar verificações complicadas. Isso terá paridade com uma implementação em Objective-C que assume um `sharedInstance` não nulo.

## Opções de integração manual {#manual-integration-options}

Você também pode integrar nosso SDK do tvOS manualmente — basta obter o framework do nosso [repositório público](https://github.com/appboy/appboy-ios-sdk) e inicializar a Braze conforme descrito nas seções anteriores.

## Identificação de usuários e análise de dados {#identifying-users-and-reporting-analytics}
Consulte nossa [documentação do iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift) para obter informações sobre a definição de IDs de usuário, registro de eventos personalizados e definição de atributos de usuário. Recomendamos também que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions/).