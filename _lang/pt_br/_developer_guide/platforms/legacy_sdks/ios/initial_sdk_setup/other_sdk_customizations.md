---
nav_title: Outras personalizações do SDK
article_title: Outras personalizações do SDK para iOS
platform: iOS
description: "Este artigo de referência aborda a personalização do SDK, como nível de registro, coleta de IDFA e outras personalizações."
page_order: 3

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Outras personalizações do SDK {#other-sdk-customizations}

## Nível de registro da Braze {#braze-log-level}

O nível de registro padrão para o Braze iOS SDK é mínimo, ou `8` no gráfico a seguir. Esse nível suprime a maioria dos registros para que nenhuma informação sensível seja registrada em um aplicativo lançado em produção.

Consulte a seguinte lista de níveis de registro disponíveis:

### Níveis de registro {#log-levels}

| Nível    | Descrição |
|----------|-------------|
| 0        | Verbose. Todas as informações de registro serão registradas no console do iOS.  |
| 1        | Depuração. As informações de depuração e de nível superior serão registradas no console do iOS.  |
| 2        | Aviso. As informações de aviso e de nível superior serão registradas no console do iOS.  |
| 4        | Erro. As informações de erro e de nível superior serão registradas no console do iOS.  |
| 8        | Mínimo. O mínimo de informações será registrado no console do iOS. A configuração padrão do SDK. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Níveis de registro" }

### Registro detalhado {#verbose-logging}

É possível configurar o nível de registro para qualquer valor disponível. No entanto, definir o nível de registro como verbose, ou `0`, pode ser muito útil para depurar problemas com a sua integração. Esse nível é destinado apenas a ambientes de desenvolvimento e não deve ser definido em um aplicativo lançado. O registro detalhado não enviará nenhuma informação extra ou nova do usuário para a Braze.

### Definição do nível de registro {#setting-log-level}

O nível de registro pode ser atribuído em tempo de compilação ou em tempo de execução:

{% tabs local %}
{% tab Compile Time %}

Adicione um dicionário chamado `Braze` ao seu arquivo `Info.plist`. No dicionário `Braze`, adicione a subentrada string `LogLevel` e defina o valor como `0`.

{% alert note %}
Antes do Braze iOS SDK v4.0.2, a chave do dicionário `Appboy` deve ser usada no lugar de `Braze`.
{% endalert %}

Exemplo do conteúdo de `Info.plist`:

```
<key>Braze</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

{% endtab %}
{% tab Runtime %}

Adicione o `ABKLogLevelKey` dentro do parâmetro `appboyOptions` passado para `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Defina seu valor como o número inteiro `0`.

{% subtabs %}
{% subtab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKLogLevelKey] = @(0);
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endsubtab %}
{% subtab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKLogLevelKey : 0
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
O nível de registro só pode ser definido em tempo de execução com o Braze iOS SDK v4.4.0 ou mais recente. Se estiver usando uma versão anterior do SDK, defina o nível de registro no momento da compilação.
{% endalert %}

{% endtab %}
{% endtabs %}

## Coleta opcional de IDFV - Swift {#optional-idfv-collection-swift}

Nas versões anteriores do Braze iOS Swift SDK, o campo IDFV (Identifier for Vendor) era coletado automaticamente como o ID do dispositivo do usuário.

A partir do Swift SDK v5.7.0, o campo IDFV pode ser desativado opcionalmente e, em vez disso, a Braze definirá um UUID aleatório como o ID do dispositivo. Para saber mais, consulte [Coleta de IDFV]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift).

## Coleta opcional de IDFA {#optional-idfa-collection}

A coleta de IDFA é opcional no SDK da Braze e fica desativada por padrão. A coleta de IDFA só é necessária na Braze se você pretender usar nossas [integrações de atribuição da instalação]({{site.baseurl}}/partners/message_orchestration/attribution/adjust). Se você optar por armazenar seu IDFA, nós o armazenaremos gratuitamente, para que você possa aproveitar essas opções imediatamente após o lançamento, sem trabalho de desenvolvimento adicional.

Por isso, recomendamos que você continue coletando o IDFA se atender a qualquer um dos critérios a seguir:

- Você está atribuindo a instalação do app a um anúncio veiculado anteriormente
- Você está atribuindo uma ação no aplicativo a um anúncio veiculado anteriormente

### iOS 14.5 AppTrackingTransparency

A Apple exige que os usuários façam opt-in por meio de uma solicitação de permissão para coletar o IDFA.

Para coletar o IDFA, além de implementar nosso protocolo `ABKIDFADelegate`, seu aplicativo precisará solicitar autorização do usuário usando o `ATTrackingManager` da Apple no framework de transparência de rastreamento do app. Consulte o [artigo sobre privacidade do usuário](https://developer.apple.com/app-store/user-privacy-and-data-use/) da Apple para saber mais.

A solicitação de autorização de transparência de rastreamento do app requer uma entrada `Info.plist` para explicar o uso do identificador:

```
<key>NSUserTrackingUsageDescription</key>
<string>To retarget ads and build a global profile to better serve you things you would like.</string>
```

### Implementação da coleta de IDFA {#implementing-idfa-collection}

Siga estas etapas para implementar a coleta de IDFA:

#### Etapa 1: Implementar o ABKIDFADelegate {#step-1-implement-abkidfadelegate}

Crie uma classe que esteja em conformidade com o protocolo [`ABKIDFADelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKIDFADelegate.h):

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
#import "IDFADelegate.h"
#import <AdSupport/ASIdentifierManager.h>
#import <AppTrackingTransparency/AppTrackingTransparency.h>

@implementation IDFADelegate

- (NSString *)advertisingIdentifierString {
  return [[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];
}

- (BOOL)isAdvertisingTrackingEnabledOrATTAuthorized {
  if (@available(iOS 14, *)) {
    return [ATTrackingManager trackingAuthorizationStatus] == ATTrackingManagerAuthorizationStatusAuthorized;
  }
  return [[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled];
}

@end
```

{% endtab %}
{% tab swift %}

```swift
import Appboy_iOS_SDK
import AdSupport
import AppTrackingTransparency

class IDFADelegate: NSObject, ABKIDFADelegate {
   func advertisingIdentifierString() -> String {
    return ASIdentifierManager.shared().advertisingIdentifier.uuidString
  }

  func isAdvertisingTrackingEnabledOrATTAuthorized() -> Bool {
    if #available(iOS 14, *) {
      return ATTrackingManager.trackingAuthorizationStatus ==  ATTrackingManager.AuthorizationStatus.authorized
    }
    return ASIdentifierManager.shared().isAdvertisingTrackingEnabled
  }
}
```
{% endtab %}
{% endtabs %}

##### Etapa 2: Definir o delegado durante a inicialização da Braze {#step-2-set-the-delegate-during-braze-initialization}

No dicionário `appboyOptions` passado para `startWithApiKey:inApplication:withAppboyOptions:`, defina a chave `ABKIDFADelegateKey` como uma instância da sua classe em conformidade com `ABKIDFADelegate`.

## Tamanho aproximado do SDK do iOS {#ios-sdk-size}

O tamanho aproximado do arquivo do framework do iOS SDK é de 30&nbsp;MB, e o tamanho aproximado do .ipa (adição ao arquivo do app) está entre 1&nbsp;MB e 2&nbsp;MB.

A Braze mede o tamanho do nosso iOS SDK observando o efeito do SDK no tamanho do `.ipa`, de acordo com as [recomendações da Apple sobre tamanho de apps](https://developer.apple.com/library/content/qa/qa1795/_index.html). Se estiver calculando a adição de tamanho do iOS SDK ao seu aplicativo, recomendamos seguir [Obter um relatório de tamanho do app](https://developer.apple.com/library/content/qa/qa1795/_index.html) para comparar a diferença de tamanho no seu `.ipa` antes e depois da integração do Braze iOS SDK. Ao comparar os tamanhos do relatório de afinamento de apps, também recomendamos analisar os tamanhos de apps para arquivos `.ipa` afinados, pois os arquivos `.ipa` universais serão maiores do que os binários baixados da App Store e instalados nos dispositivos dos usuários.

{% alert note %}
Se estiver integrando via CocoaPods com `use_frameworks!`, defina `Enable Bitcode = NO` nas configurações de build do alvo para obter um dimensionamento preciso.
{% endalert %}