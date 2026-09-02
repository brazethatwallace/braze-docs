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
Nosso SDK do tvOS atualmente oferece suporte à funcionalidade de análise de dados. Para adicionar um app para tvOS em seu dashboard, abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).
{% endalert %}

O SDK da Braze para tvOS deve ser instalado ou atualizado usando o [CocoaPods](http://cocoapods.org/), um gerenciador de dependências para projetos Objective-C e Swift. O CocoaPods oferece mais simplicidade para integração e atualização.

## Integração do SDK para tvOS com CocoaPods

### Etapa 1: Instale o CocoaPods

A instalação do SDK pelo [CocoaPods](http://cocoapods.org/) para tvOS automatiza a maior parte do processo de instalação. Antes de iniciar esse processo, verifique se você está usando o [Ruby versão 2.0.0](https://www.ruby-lang.org/en/installation/) ou superior.

Execute o seguinte comando para começar:

```bash
$ sudo gem install cocoapods
```

- Se for solicitado a substituir o executável `rake`, consulte [Getting started](http://guides.cocoapods.org/using/getting-started.html) no CocoaPods.org para mais detalhes.
- Se você tiver problemas com o CocoaPods, consulte o [guia de solução de problemas do CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

### Etapa 2: Criação do Podfile

Agora que você instalou a gem Ruby do CocoaPods, será necessário criar um arquivo chamado `Podfile` no diretório do seu projeto Xcode.

Adicione a seguinte linha ao seu Podfile:

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Sugerimos que você versione a Braze para que as atualizações do pod capturem automaticamente qualquer atualização menor que uma versão minor. A configuração fica assim: `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`. Se quiser integrar automaticamente a versão mais recente do SDK da Braze, mesmo com mudanças maiores, você pode usar `pod 'Appboy-tvOS-SDK'` no seu Podfile.

### Etapa 3: Instalação do SDK da Braze

Para instalar o CocoaPods do SDK da Braze, navegue até o diretório do seu projeto Xcode no terminal e execute o seguinte comando:
```
pod install
```

Neste ponto, você deve conseguir abrir o novo espaço de trabalho do projeto Xcode criado pelo CocoaPods. Certifique-se de usar esse espaço de trabalho do Xcode em vez do seu projeto Xcode.

![Neste ponto, você deve conseguir abrir o novo espaço de trabalho do projeto Xcode criado pelo CocoaPods. Certifique-se de usar esse espaço de trabalho do Xcode em vez do seu projeto Xcode.]({% image_buster /assets/img_archive/podsworkspace.png %})

### Etapa 4: Atualize seu app delegate

{% tabs %}
{% tab OBJECTIVE-C %}

Adicione a seguinte linha de código ao seu arquivo `AppDelegate.m`:

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

No seu arquivo `AppDelegate.m`, adicione o seguinte snippet dentro do método `application:didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Por fim, atualize `YOUR-API-KEY` com o valor correto da sua página **Manage Settings**.

{% endtab %}
{% tab swift %}

Se você está integrando o SDK da Braze com CocoaPods ou Carthage, adicione a seguinte linha de código ao seu arquivo `AppDelegate.swift`:

```swift
import AppboyTVOSKit
```

Para saber mais sobre o uso de código Objective-C em projetos Swift, consulte a [documentação da Apple para desenvolvedores](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Em `AppDelegate.swift`, adicione o seguinte snippet ao seu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Em seguida, atualize `YOUR-API-KEY` com o valor correto da sua página **Manage Settings**.

Nosso singleton `sharedInstance` será nil antes que `startWithApiKey:` seja chamado, pois isso é um pré-requisito para usar qualquer funcionalidade da Braze.

{% endtab %}
{% endtabs %}

{% alert warning %}
Certifique-se de inicializar a Braze na thread principal do seu aplicativo. A inicialização assíncrona pode resultar em funcionalidades com defeito.
{% endalert %}

### Etapa 5: Especifique seu endpoint personalizado ou cluster de dados

{% alert note %}
Desde dezembro de 2019, endpoints personalizados não são mais fornecidos. Se você tem um endpoint personalizado pré-existente, pode continuar a usá-lo. Para saber mais, consulte nossa <a href="{{site.baseurl}}/api/basics#endpoints">lista de endpoints disponíveis</a>.
{% endalert %}

Seu representante da Braze já deve ter informado o [endpoint correto]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuração de endpoint em tempo de compilação (recomendado)
Se você recebeu um endpoint personalizado pré-existente:
- A partir do SDK iOS da Braze v3.0.2, você pode definir um endpoint personalizado usando o arquivo `Info.plist`. Adicione o dicionário `Appboy` ao seu arquivo Info.plist. Dentro do dicionário `Appboy`, adicione a subentrada de string `Endpoint` e defina o valor como a autoridade da URL do seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, e não `https://sdk.iad-01.braze.com`).

#### Configuração de endpoint em tempo de execução
Se você recebeu um endpoint personalizado pré-existente:
- A partir do SDK iOS da Braze v3.17.0+, você pode substituir o endpoint por meio do `ABKEndpointKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina o valor como a autoridade da URL do seu endpoint personalizado (por exemplo, `sdk.iad-01.braze.com`, e não `https://sdk.iad-01.braze.com`).

{% alert note %}
O suporte para definir endpoints em tempo de execução usando `ABKAppboyEndpointDelegate` foi removido no SDK iOS da Braze v3.17.0. Se você já usa `ABKAppboyEndpointDelegate`, observe que nas versões v3.14.1 a v3.16.0 do SDK iOS da Braze, qualquer referência a `dev.appboy.com` no seu método `getApiEndpoint()` deve ser substituída por uma referência a `sdk.iad-01.braze.com`.
{% endalert %}

### Integração do SDK concluída

A Braze agora deve estar coletando dados do seu aplicativo, e sua integração básica deve estar concluída. Observe que, ao compilar seu app tvOS e quaisquer outras bibliotecas de terceiros, o Bitcode deve estar ativado.

### Atualizando o SDK da Braze via CocoaPods

Para atualizar um CocoaPod, basta executar os seguintes comandos no diretório do seu projeto:

```
pod update
```

## Personalizando a Braze na inicialização

Se quiser personalizar a Braze na inicialização, você pode usar o método de inicialização da Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` e passar um `NSDictionary` opcional de chaves de inicialização da Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

No arquivo `AppDelegate.m`, dentro do método `application:didFinishLaunchingWithOptions`, adicione o seguinte método da Braze:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

Em `AppDelegate.swift`, dentro do método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, adicione o seguinte método da Braze:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

onde `appboyOptions` é um `Dictionary` de valores de configuração de inicialização.

{% endtab %}
{% endtabs %}

Esse método substitui o método de inicialização `startWithApiKey:inApplication:withLaunchOptions:` e é chamado com os seguintes parâmetros:

- `YOUR-API-KEY`: A chave de API do seu aplicativo pode ser encontrada em **Manage Settings** no dashboard da Braze.
- `application`: O app atual.
- `launchOptions`: O `NSDictionary` de opções que você obtém de `application:didFinishLaunchingWithOptions:`.
- `appboyOptions`: Um `NSDictionary` opcional com valores de configuração de inicialização para a Braze.

Consulte [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para ver a lista de chaves de inicialização da Braze.

## Appboy.sharedInstance() e nullability no Swift
Diferente da prática comum, o singleton `Appboy.sharedInstance()` é opcional. Isso ocorre porque `sharedInstance` é `nil` antes de `startWithApiKey:` ser chamado, e existem algumas implementações não convencionais — mas válidas — em que uma inicialização tardia pode ser usada.

Se você chamar `startWithApiKey:` no delegate `didFinishLaunchingWithOptions:` antes de qualquer acesso ao `sharedInstance` do Appboy (a implementação padrão), é possível usar optional chaining, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar verificações trabalhosas. Isso terá paridade com uma implementação em Objective-C que presumia um `sharedInstance` não nulo.

Você também pode integrar nosso SDK para tvOS manualmente — basta obter o Framework do nosso [repositório público](https://github.com/appboy/appboy-ios-sdk) e inicializar a Braze conforme descrito nas seções anteriores.

## Identificando usuários e reportando análise de dados
Consulte nossa [documentação do iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift) para informações sobre como definir IDs de usuário, registrar eventos personalizados e definir atributos de usuário. Também recomendamos que você se familiarize com nossas [convenções de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).