## Manifesto de privacidade da Apple {#privacy-manifest}

### O que são dados de rastreamento? {#what-is-tracking-data}

A Apple define "dados de rastreamento" como os dados coletados em seu app sobre um usuário final ou dispositivo que estão vinculados a dados de terceiros (como publicidade direcionada) ou a um corretor de dados. Para uma definição completa com exemplos, consulte [Apple: Rastreamento](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Por padrão, o SDK da Braze não coleta dados de rastreamento. No entanto, dependendo da configuração do SDK da Braze, talvez seja necessário listar dados específicos da Braze no manifesto de privacidade do seu app.

### O que é um manifesto de privacidade? {#what-is-a-privacy-manifest}

Um manifesto de privacidade é um arquivo em seu projeto Xcode que descreve o motivo pelo qual seu app e SDKs de terceiros coletam dados, juntamente com seus métodos de coleta de dados. Cada um dos seus SDKs de terceiros que rastreiam dados exige seu próprio manifesto de privacidade. Quando você [cria o relatório de privacidade do seu app](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), esses arquivos de manifesto de privacidade são automaticamente agregados em um único relatório.

### Domínios de dados de rastreamento da API {#api-tracking-data-domains}

A partir do iOS 17.2, a Apple bloqueará todos os endpoints de rastreamento declarados em seu app até que o usuário final aceite um [aviso de Transparência de Rastreamento de Anúncios (ATT)](https://support.apple.com/en-us/HT212025). A Braze fornece endpoints de rastreamento para encaminhar seus dados de rastreamento e, ao mesmo tempo, permite que você encaminhe dados primários que não sejam de rastreamento para o endpoint original.

## Declarar dados de rastreamento da Braze {#declaring-braze-tracking-data}

{% alert tip %}
Para um passo a passo completo, consulte o [tutorial de dados de rastreamento de privacidade](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Pré-requisitos {#prerequisites}

A seguinte versão do SDK da Braze é necessária para implementar esse recurso:

{% sdk_min_versions swift:9.0.0 %}

### Etapa 1: Revisar suas políticas atuais {#step-1-review-your-current-policies}

Revise as políticas atuais de coleta de dados do SDK da Braze com sua equipe jurídica para determinar se o seu app coleta dados de rastreamento [conforme definido pela Apple](#what-is-tracking-data). Se você não estiver coletando nenhum dado de rastreamento, não será necessário personalizar o manifesto de privacidade do SDK da Braze neste momento. Para saber mais sobre as políticas de coleta de dados do SDK da Braze, consulte [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection).

{% alert important %}
Se algum dos seus SDKs que não são da Braze coletar dados de rastreamento, você precisará revisar essas políticas separadamente.
{% endalert %}

### Etapa 2: Criar um manifesto de privacidade {#step-2-create-a-privacy-manifest}

Primeiro, verifique se você já possui um manifesto de privacidade procurando por um arquivo `PrivacyInfo.xcprivacy` no seu projeto Xcode. Se você já tiver esse arquivo, pode prosseguir para a próxima etapa. Caso contrário, consulte [Apple: Criar um manifesto de privacidade](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

### Etapa 3: Adicionar seu endpoint ao manifesto de privacidade {#step-3-add-your-endpoint-to-the-privacy-manifest}

No seu projeto Xcode, abra o arquivo `PrivacyInfo.xcprivacy` do seu app, clique com o botão direito na tabela e marque **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![Um projeto Xcode com o menu de contexto aberto e "Raw Keys and Values" destacado.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Em **App Privacy Configuration**, escolha **NSPrivacyTracking** e defina seu valor como **YES**.

![O arquivo "PrivacyInfo.xcprivacy" aberto com "NSPrivacyTracking" definido como "YES".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Em **App Privacy Configuration**, escolha **NSPrivacyTrackingDomains**. No array de domínios, adicione um novo elemento e defina seu valor como o endpoint que você [adicionou anteriormente ao seu `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate) com o prefixo `sdk-tracking`.

![O arquivo "PrivacyInfo.xcprivacy" aberto com um endpoint de rastreamento da Braze listado em "NSPrivacyTrackingDomains".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Etapa 4: Declarar seus dados de rastreamento {#step-4-declare-your-tracking-data}

Em seguida, abra o `AppDelegate.swift` e liste cada [propriedade de rastreamento](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) que você deseja declarar, criando uma lista de rastreamento estática ou dinâmica. Lembre-se de que a Apple bloqueará essas propriedades até que o usuário final aceite o prompt de ATT, então liste apenas as propriedades que você e sua equipe jurídica consideram como dados de rastreamento. Por exemplo:

{% tabs %}
{% tab exemplo estático %}
No exemplo a seguir, `dateOfBirth`, `customEvent` e `customAttribute` são declarados como dados de rastreamento em uma lista estática.

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab exemplo dinâmico %}
No exemplo a seguir, a lista de rastreamento é atualizada automaticamente após o usuário final aceitar o [prompt de App Tracking Transparency (ATT)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)). Solicitar autorização na ativação do app é um evento por cena, então esse código pertence ao método `sceneDidBecomeActive(_:)` do seu arquivo `SceneDelegate.swift`, e não ao `applicationDidBecomeActive(_:)` do `AppDelegate.swift` (necessário para apps que adotaram o [ciclo de vida `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)). Sua instância da Braze permanece acessível a partir do `SceneDelegate` por meio da propriedade estática `AppDelegate.braze` configurada na Etapa 1.

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze?.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Etapa 5: Evitar loops infinitos de tentativas {#step-5-prevent-infinite-retry-loops}

Para evitar que o SDK entre em um loop infinito de tentativas, use o método `set(adTrackingEnabled: enableAdTracking)` para lidar com as permissões de ATT. A propriedade `adTrackingEnabled` no método do seu `SceneDelegate.swift` deve ser tratada de forma semelhante ao seguinte:

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Desabilitando o rastreamento de dados {#disabling-data-tracking}

Para desabilitar a atividade de rastreamento de dados no SDK Swift, defina a propriedade [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) como `false` na sua instância da Braze. Quando `enabled` é definido como `false`, o SDK da Braze ignora todas as chamadas à API pública. O SDK também cancela todas as ações em andamento, como solicitações de rede, processamento de eventos, etc.

## Limpando dados armazenados anteriormente {#wiping-previously-stored-data}

Você pode usar o método [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) para limpar completamente os dados do SDK armazenados localmente no dispositivo de um usuário.

Para versões 7.0.0 e posteriores do Braze Swift, o SDK e o método `wipeData()` geram aleatoriamente um UUID para o ID do dispositivo. No entanto, se o seu `useUUIDAsDeviceId` estiver definido como `false` _ou_ se você estiver usando a versão 5.7.0 ou anterior do Swift SDK, também será necessário fazer uma solicitação POST para [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete), pois o Identifier for Vendors (IDFV) será automaticamente usado como o ID do dispositivo desse usuário.

Se você usa integração manual de push e seu app chama `wipeData()` e depois reativa o SDK na mesma execução do app, chame `registerForRemoteNotifications()` novamente para que a Braze possa receber um token de dispositivo atualizado. Para saber mais, consulte [configuração de notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Retomando o rastreamento de dados {#resuming-data-tracking}

Para retomar a coleta de dados, defina [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) como `true`. Lembre-se de que isso não recuperará nenhum dado que tenha sido apagado anteriormente.

## Logout e cancelamento de registro de push {#logout-and-unregister-push}

O SDK da Braze fornece métodos para parar de direcionar um dispositivo quando um usuário cancela o registro de notificações por push ou faz logout. Esses métodos removem os dados de registro de push do usuário atual no servidor da Braze e no SDK, de modo que a Braze não envie mais Campaigns de notificação por push para esse usuário.

### Logout {#logout}

Quando um usuário faz logout de um aplicativo, chame o método `logout` do SDK para remover o registro de push do dispositivo do usuário atual e executar automaticamente ações de limpeza no SDK. O método `logout` realiza o seguinte:

- Cancela o registro do token de push do dispositivo e de quaisquer tokens push-to-start de Live Activities do usuário atual no servidor da Braze.
- Se a chamada de cancelamento de registro for bem-sucedida, o SDK apaga os dados armazenados localmente e desativa o SDK.
- Em caso de falha, gera um erro e um sinalizador `isRetriable` para permitir que o integrador tome uma ação.

{% subtabs local %}
{% subtab Swift %}

O exemplo a seguir com completion handler mostra o tratamento de sucesso e falha do `logout`. Use-o para fluxos baseados em retorno de chamada e substitua o registro de log pela lógica de nova tentativa ou reautenticação do seu app.

```swift
// Completion handler
AppDelegate.braze?.logout { result in
  switch result {
  case .success:
    print("Logout successful")
  case .failure(let error):
    print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

O exemplo assíncrono a seguir mostra a API suspensa `logout`. Use-o para fluxos de trabalho assíncronos e personalize as ramificações de sucesso e falha para o seu app.

```swift
// Async/await
do {
  try await AppDelegate.braze?.logout()
  print("Logout successful")
} catch let error as Braze.LogoutErrorResult {
  print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Este exemplo em Objective-C mostra o tratamento do `logout` baseado em completion. Use-o em integrações Objective-C e substitua o registro de log pelo fluxo do seu app.

```objc
[AppDelegate.braze logoutWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZLogoutErrorUserInfoKey.isRetriable];
    NSLog(@"Logout failed: %@, isRetriable=%@", error.localizedDescription, isRetriable);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

{% alert note %}
O `logout` não encerra Live Activities em execução. No retorno de chamada de sucesso, encerre manualmente quaisquer Live Activities em execução usando o método [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)) do ActivityKit.
{% endalert %}

#### Reativar o rastreamento e push após o `logout` {#re-enable-tracking-and-push-after-logout}

Após um `logout` bem-sucedido, defina [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) de volta para `true` e, em seguida, registre-se novamente para notificações com o seu sistema operacional (SO) ou provedor de push seguindo a [configuração de push para Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

#### Evite chamadas imediatas de cancelamento de registro {#avoid-immediate-unregister-calls}

Evite chamar `logout` ou `unregisterPush` diretamente após registrar-se para notificações por push com o SO ou provedor de push. Devido ao processamento assíncrono do servidor, isso pode, em casos raros, readicionar o token de push ao usuário da Braze.

### Cancelar registro de push {#unregister-push}

Para parar de enviar push para um dispositivo sem limpeza automatizada adicional, use o método `unregisterPush`. Isso remove o token de push do dispositivo do usuário atual no servidor da Braze e limpa o token armazenado localmente.

{% subtabs local %}
{% subtab Swift %}

O exemplo a seguir com completion handler mostra o tratamento de sucesso e falha do `unregisterPush`. Use-o para fluxos baseados em retorno de chamada e substitua o registro de log pela sua própria lógica de nova tentativa.

```swift
// Completion handler
AppDelegate.braze?.notifications.unregisterPush { result in
  switch result {
  case .success:
    print("Push unregistered successfully")
  case .failure(let error):
    print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

O exemplo assíncrono a seguir mostra a API suspensa `unregisterPush`. Use-o para fluxos de trabalho assíncronos e personalize as ramificações de sucesso e falha para o seu app.

```swift
// Async/await
do {
  try await AppDelegate.braze?.notifications.unregisterPush()
  print("Push unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Este exemplo em Objective-C mostra o tratamento do `unregisterPush` baseado em completion. Use-o em integrações Objective-C e substitua o registro de log pelo fluxo do seu app.

```objc
[AppDelegate.braze.notifications unregisterPushWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.isRetriable];
    NSNumber *statusCode = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.httpStatusCode];
    NSLog(@"Push unregistration failed: %@, isRetriable=%@ status=%@",
          error.localizedDescription, isRetriable, statusCode);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

#### Registrar push novamente após `unregisterPush` {#re-register-push-after-unregisterpush}

Após chamar `unregisterPush`, registre-se novamente para notificações com o seu SO ou provedor de push seguindo a [configuração de push para Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) antes de enviar notificações por push da Braze novamente.

#### Evite chamadas imediatas de cancelamento de registro

Evite chamar `logout` ou `unregisterPush` diretamente após registrar-se para notificações por push com o SO ou provedor de push. Devido ao processamento assíncrono do servidor, isso pode, em casos raros, readicionar o token de push ao usuário da Braze.

### Cancelar registro de tokens push-to-start para Live Activities {#unregister-push-to-start}

Live Activities podem ser iniciadas remotamente usando tokens push-to-start. Para impedir que a Braze inicie remotamente Live Activities em um dispositivo, chame o método `unregisterPushToStart` para cancelar o registro de todos os tipos registrados atualmente (padrão) ou de uma lista específica de tipos de Activity.

Observe que Live Activities em execução continuam recebendo atualizações e que esse método apenas remove a capacidade de iniciar novas atividades remotamente. Para saber mais sobre Live Activities, consulte [Live Activities]({{site.baseurl}}/developer_guide/live_notifications/live_activities).

#### Encerrar quaisquer Live Activities em execução {#end-any-running-live-activities}

O `unregisterPushToStart` não encerra Live Activities em execução. No retorno de chamada de sucesso, encerre manualmente quaisquer Live Activities em execução usando o método [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)) do ActivityKit.

{% alert note %}
Evite chamar `logout` ou `unregisterPushToStart` diretamente após chamar `registerPushToStart` para uma Live Activity. Devido à natureza assíncrona do processamento do servidor, em casos raros, isso pode fazer com que o token push-to-start seja readicionado ao usuário da Braze.
{% endalert %}

O exemplo a seguir mostra como cancelar o registro de todos os tipos de atividade push-to-start. Use-o quando um usuário desconectado não deve mais receber novas Live Activities iniciadas remotamente.

```swift
// Unregister all currently-registered activity types
// Completion handler
AppDelegate.braze?.liveActivities.unregisterPushToStart { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}

// Async/await
do {
  try await AppDelegate.braze?.liveActivities.unregisterPushToStart()
  print("Push-to-start unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

O exemplo a seguir mostra como cancelar o registro de tipos de atividade específicos. Use-o quando apenas Live Activities selecionadas devem parar de ser iniciadas remotamente.

```swift
// Unregister specific activity types
AppDelegate.braze?.liveActivities.unregisterPushToStart(types: ["ActivityType1", "ActivityType2"]) { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

{% alert note %}
O `unregisterPushToStart` não possui uma API em Objective-C, pois Live Activities dependem de tipos exclusivos do Swift.
{% endalert %}

## Coleta de IDFV {#idfv-collection}

Em versões anteriores do SDK da Braze para iOS, o campo IDFV (Identifier for Vendor) era coletado automaticamente como o ID do dispositivo do usuário. A partir do Swift SDK `v5.7.0`, o campo IDFV passou a poder ser desativado opcionalmente, e a Braze passaria a definir um UUID aleatório como o ID do dispositivo. A partir do Swift SDK `v7.0.0`, o campo IDFV não será coletado por padrão, e um UUID será definido como o ID do dispositivo.

O recurso `useUUIDAsDeviceId` configura o [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) para definir o ID do dispositivo como um UUID. Tradicionalmente, o SDK para iOS atribuía ao ID do dispositivo o valor IDFV gerado pela Apple. Com esse recurso ativado por padrão no seu app iOS, todos os novos usuários criados pelo SDK receberão um ID de dispositivo igual a um UUID.

Se você ainda quiser coletar o IDFV separadamente, pode usar [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

{% alert note %}
A leitura de `braze.deviceId` bloqueia a thread de chamada até que o SDK conclua suas operações pós-inicialização. Para contextos na thread principal ou sensíveis à latência, use as alternativas não bloqueantes.

{% subtabs local %}
{% subtab Swift %}
```swift
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.getDeviceId { deviceId in
  print("Device ID:", deviceId)
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let deviceId = await AppDelegate.braze?.getDeviceId()
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// Completion handler — always delivers on the main thread.
[AppDelegate.braze getDeviceIdWithCompletion:^(NSString *deviceId) {
  NSLog(@"Device ID: %@", deviceId);
}];
```
{% endsubtab %}
{% endsubtabs local %}
{% endalert %}

### Considerações {#considerations}

#### Versão do SDK {#sdk-version}

No Swift SDK `v7.0.0+`, quando `useUUIDAsDeviceId` está ativado (padrão), todos os novos usuários criados receberão um ID de dispositivo aleatório. Todos os usuários existentes manterão o mesmo valor de ID de dispositivo, que pode ter sido o IDFV.

Quando esse recurso não está ativado, os dispositivos continuarão recebendo o IDFV na criação.

#### Impactos posteriores {#downstream}

**Parceiros de tecnologia**: quando esse recurso está ativado, qualquer parceiro de tecnologia que derive o valor do IDFV a partir do ID de dispositivo da Braze não terá mais acesso a esse dado. Se o valor do IDFV derivado do dispositivo for necessário para sua integração com parceiros, recomendamos definir esse recurso como `false`.

**Currents**: `useUUIDAsDeviceId` definido como true significa que o ID de dispositivo enviado no Currents não será mais igual ao valor do IDFV.

### Perguntas frequentes {#frequently-asked-questions}

#### Essa mudança afetará meus usuários existentes na Braze? {#will-this-change-impact-my-existing-users-in-braze}

Não. Quando ativado, esse recurso não sobrescreverá nenhum dado de usuário na Braze. Novos IDs de dispositivo UUID serão criados apenas para novos dispositivos ou quando `wipedata()` for chamado.

#### Posso desativar esse recurso depois de ativá-lo? {#can-i-turn-this-feature-off-after-turning-it-on}

Sim, esse recurso pode ser ativado e desativado conforme sua necessidade. IDs de dispositivo armazenados anteriormente nunca serão sobrescritos.

#### Ainda posso capturar o valor do IDFV pela Braze de outra forma? {#can-i-still-capture-the-idfv-value-through-braze-elsewhere}

Sim, você ainda pode coletar opcionalmente o IDFV pelo Swift SDK (a coleta é desativada por padrão).