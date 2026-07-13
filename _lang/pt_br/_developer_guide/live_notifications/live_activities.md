---
nav_title: Atividades ao vivo para Swift
article_title: Atividades ao vivo para o SDK Swift da Braze
page_order: 0.2
description: "Aprenda como configurar Atividades ao Vivo para o SDK Swift da Braze."
platform:
  - Swift
---

# Atividades ao vivo para Swift {#live-activities-for-swift}

> Aprenda como implementar Atividades ao Vivo para o SDK Swift da Braze. Atividades ao Vivo são notificações persistentes e interativas exibidas diretamente na tela de bloqueio, permitindo que os usuários recebam atualizações dinâmicas em tempo real&#8212;sem desbloquear o dispositivo.

## Como funciona {#how-it-works}

![Atividade ao vivo de um rastreador de entregas em uma tela de bloqueio do iPhone. Uma barra de status com um carro está quase na metade. O texto diz "2 min until pickup"]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

As Atividades ao Vivo apresentam uma combinação de informações estáticas e dinâmicas que você atualiza. Por exemplo, você pode criar uma Atividade ao Vivo que fornece um rastreador de status para uma entrega. Essa Atividade ao Vivo teria o nome da sua empresa como informação estática, bem como um "Tempo para entrega" dinâmico que seria atualizado à medida que o motorista de entrega se aproximasse do destino.

Como desenvolvedor, você pode usar a Braze para gerenciar os ciclos de vida das suas Atividades ao Vivo, fazer chamadas para a REST API da Braze para realizar atualizações e fazer com que todos os dispositivos inscritos recebam a atualização o mais rápido possível. E, como você está gerenciando as Atividades ao Vivo por meio da Braze, pode usá-las em conjunto com seus outros canais de envio de mensagens&mdash;notificações por push, mensagens no app, Content Cards&mdash;para promover a adoção.

## Diagrama de sequência {#sequence-diagram}

{% tabs %}
{% tab Live Activities Sequence Diagram %}
{% details Mostrar diagrama %}
```mermaid
---
config:
  theme: mc
---
sequenceDiagram
  participant Server as Client Server
  participant Device as User Device
  participant App as iOS App / Braze SDK
  participant BrazeAPI as Braze API
  participant APNS as Apple Push Notification Service
  Note over Server, APNS: Launch Option 1<br/>Locally Start Activities
  App ->> App: Register a Live Activity using <br>`launchActivity(pushTokenTag:activity:)`
  App ->> App: Get push token from iOS
  App ->> BrazeAPI: Activity ID & Push token<br>automatically sent to Braze
  Note over Server, APNS: Launch Option 2<br/>Remotely Start Activities
  Device ->> App: Call `registerPushToStart`<br>to collect push tokens early
  App ->> BrazeAPI: Push-to-start tokens sent to Braze
  Server ->> BrazeAPI: POST /messages/live_activity/start
  Note right of BrazeAPI: Payload includes:<br>- push_token<br>- activity_id<br>- external_id<br>- event_name<br>- content_state (optional)
  BrazeAPI ->> APNS: Live activity start request
  APNS ->> Device: APNS sends activity to device
  App ->> App: Get push token from iOS
  App ->> BrazeAPI: Activity ID & Push token<br>automatically sent to Braze
  Note over Server, APNS: Resuming activities upon app launch
  App ->> App: Call `resumeActivities(ofType:)` on each app launch
  Note over Server, APNS: Updating a Live Activity
  loop update a live activity
  Server ->> BrazeAPI: POST /messages/live_activity/update
  Note right of BrazeAPI: Payload includes changes<br>to ContentState (dynamic variables)
  BrazeAPI ->> APNS: Update sent to APNS
  APNS ->> Device: APNS sends update to device
  end
  Note over Server, APNS: Ending a Live Activity
  Server ->> BrazeAPI: POST /messages/live_activity/update
  Note right of BrazeAPI: Activity can be ended via:<br> - User manually dismisses<br>- Times out after 12 hours<br>- Setting `end_activity: true` on `/messages/live_activity/update`
  APNS ->> Device: Live activity is dismissed
```
{% enddetails %}
{% endtab %}
{% endtabs %}

## Implementação de uma Atividade ao Vivo {#implementing-a-live-activity}

#{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará completar o seguinte:

- Certifique-se de que seu projeto está direcionado para iOS 16.1 ou posterior.
- Adicione a autorização `Push Notification` em **Signing & Capabilities** no seu projeto Xcode.
- Certifique-se de que chaves `.p8` são usadas para enviar notificações. Não há suporte para arquivos mais antigos, como `.p12` ou `.pem`.
- A partir da versão 8.2.0 do SDK Swift da Braze, é possível [registrar remotamente uma Atividade ao Vivo](#swift_step-2-start-the-activity). Para usar esse recurso, é necessário o iOS 17.2 ou posterior.

{% alert note %}
Embora as Atividades ao Vivo e as notificações por push sejam semelhantes, suas permissões de sistema são separadas. Por padrão, todos os recursos de Atividade ao Vivo estão ativados, mas os usuários podem desativar esse recurso por app.
{% endalert %}

{% sdk_min_versions swift:5.11.0 %}

### Etapa 1: Crie uma atividade {#create-an-activity}

Primeiro, certifique-se de ter seguido o procedimento [Exibindo dados ao vivo com Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) na documentação da Apple para configurar Atividades ao Vivo no seu aplicativo iOS. Como parte dessa tarefa, inclua `NSSupportsLiveActivities` definido como `YES` no seu `Info.plist`.

Como a natureza exata da sua Atividade ao Vivo será específica para o seu caso de negócios, você precisará configurar e inicializar os objetos [Activity](https://developer.apple.com/documentation/activitykit/activityattributes). É importante ressaltar que você definirá:
* `ActivityAttributes`: Esse protocolo define o conteúdo estático (imutável) e dinâmico (mutável) que aparecerá na sua Atividade ao Vivo.
* `ActivityAttributes.ContentState`: Esse tipo define os dados dinâmicos que serão atualizados no decorrer da atividade.

Você também usará o SwiftUI para criar a apresentação da interface do usuário da tela de bloqueio e do Dynamic Island nos dispositivos compatíveis.

Certifique-se de estar familiarizado com os [pré-requisitos e as limitações](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints) da Apple para Atividades ao Vivo, pois essas restrições são independentes da Braze.

{% alert note %}
Se você espera enviar pushes frequentes para a mesma Atividade ao Vivo, pode evitar ser limitado pelo orçamento da Apple definindo `NSSupportsLiveActivitiesFrequentUpdates` como `YES` no arquivo `Info.plist`. Para saber mais, consulte a seção [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) na documentação do ActivityKit.
{% endalert %}

#### Exemplo {#example}

Vamos imaginar que queremos criar uma Atividade ao Vivo para fornecer aos nossos usuários atualizações sobre o show Superb Owl, em que dois resgates de animais selvagens concorrentes recebem pontos pelas corujas que têm em sua residência. Neste exemplo, criamos uma struct chamada `SportsActivityAttributes`, mas você pode usar sua própria implementação de `ActivityAttributes`.

```swift
#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
struct SportsActivityAttributes: ActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String
}
```

### Etapa 2: Inicie a atividade {#start-the-activity}

Primeiro, escolha como deseja registrar sua atividade:

- **Remoto:** Use o método [`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>) no início do ciclo de vida do usuário e antes que o token de push-to-start seja necessário, e então inicie uma atividade usando o endpoint [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start).
- **Local:** Crie uma instância da sua Atividade ao Vivo e, em seguida, use o método [`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) para criar tokens push para a Braze gerenciar.

{% tabs local %}
{% tab remote %}
{% alert important %}
Para registrar remotamente uma Atividade ao Vivo, é necessário o iOS 17.2 ou posterior.
{% endalert %}

#### Etapa 2.1: Adicione o BrazeKit à sua extensão de widget {#step-21-add-brazekit-to-your-widget-extension}

No seu projeto Xcode, selecione o nome do aplicativo e, em seguida, **General**. Em **Frameworks and Libraries**, confirme se o `BrazeKit` está listado.

![O framework BrazeKit em Frameworks and Libraries em um projeto Xcode de exemplo.]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### Etapa 2.2: Adicione o protocolo BrazeLiveActivityAttributes {#brazeActivityAttributes}

Na sua implementação de `ActivityAttributes`, adicione conformidade ao protocolo `BrazeLiveActivityAttributes` e então adicione a propriedade `brazeActivityId` ao seu modelo de atributos.

{% alert important %}
O iOS mapeia a propriedade `brazeActivityId` para o campo correspondente na carga útil de push-to-start da sua Atividade ao Vivo, portanto ela não deve ser renomeada nem receber nenhum outro valor.
{% endalert %}

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@available(iOS 16.1, *)
// 1. Add the `BrazeLiveActivityAttributes` conformance to your `ActivityAttributes` struct.
struct SportsActivityAttributes: ActivityAttributes, BrazeLiveActivityAttributes {
  public struct ContentState: Codable, Hashable {
    var teamOneScore: Int
    var teamTwoScore: Int
  }

  var gameName: String
  var gameNumber: String

  // 2. Add the `String?` property to represent the activity ID.
  var brazeActivityId: String?
}
```

#### Etapa 2.3: Registre para push-to-start {#step-23-register-for-push-to-start}

Em seguida, registre o tipo de Atividade ao Vivo para que a Braze possa rastrear todos os tokens push-to-start e instâncias de Atividade ao Vivo associadas a esse tipo.

{% alert warning %}
O sistema operacional iOS gera tokens push-to-start somente durante a primeira instalação do app após a reinicialização do dispositivo. Para garantir que seus tokens sejam registrados de forma confiável, chame `registerPushToStart` no seu método `didFinishLaunchingWithOptions`.
{% endalert %}

##### Exemplo

No exemplo a seguir, a classe `LiveActivityManager` manipula objetos de Atividade ao Vivo. Em seguida, o método `registerPushToStart` registra `SportsActivityAttributes`:

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {

  @available(iOS 17.2, *)
  func registerActivityType() {
    // This method returns a Swift background task.
    // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
    let pushToStartObserver: Task = Self.braze?.liveActivities.registerPushToStart(
      forType: Activity<SportsActivityAttributes>.self,
      name: SportsActivityAttributes.name
    )
  }

}
```

#### Etapa 2.4: Envie uma notificação push-to-start {#step-24-send-a-push-to-start-notification}

Envie uma notificação push-to-start remota usando o endpoint [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start).
{% endtab %}

{% tab local %}
Você pode usar o [framework ActivityKit da Apple](https://developer.apple.com/documentation/activitykit) para obter um token de push, que o SDK da Braze pode gerenciar para você. Isso permite que você atualize as Atividades ao Vivo por meio da API da Braze, pois a Braze enviará o token de push para o serviço de Notificações por Push da Apple (APNs) no backend.

1. Crie uma instância da sua implementação de Atividade ao Vivo usando as APIs do ActivityKit da Apple.
2. Defina o parâmetro `pushType` como `.token`.
3. Passe os `ActivitiesAttributes` e `ContentState` das Atividades ao Vivo que você definiu.
4. Registre sua atividade na instância da Braze, passando-a para [`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class). O parâmetro `pushTokenTag` é uma string personalizada que você define. Ele deve ser exclusivo para cada Atividade ao Vivo que você criar.

Depois de registrar a Atividade ao Vivo, o SDK da Braze extrairá e observará as alterações nos tokens de push.

#### Exemplo

No nosso exemplo, criaremos uma classe chamada `LiveActivityManager` como interface para nossos objetos de Atividade ao Vivo. Em seguida, definiremos o `pushTokenTag` como `"sports-game-2024-03-15"`.

```swift
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

class LiveActivityManager {

  @available(iOS 16.2, *)
  func createActivity() {
    let activityAttributes = SportsActivityAttributes(gameName: "Superb Owl", gameNumber: "Game 1")
    let contentState = SportsActivityAttributes.ContentState(teamOneScore: "0", teamTwoScore: "0")
    let activityContent = ActivityContent(state: contentState, staleDate: nil)
    if let activity = try? Activity.request(attributes: activityAttributes,
                                            content: activityContent,
      // Setting your pushType as .token allows the Activity to generate push tokens for the server to watch.
                                            pushType: .token) {
      // Register your Live Activity with Braze using the pushTokenTag.
      // This method returns a Swift background task.
      // You may keep a reference to this task if you need to cancel it wherever appropriate, or ignore the return value if you wish.
      let liveActivityObserver: Task = AppDelegate.braze?.liveActivities.launchActivity(pushTokenTag: "sports-game-2024-03-15",
                                                                                        activity: activity)
    }
  }

}
```

O widget da Atividade ao Vivo exibiria esse conteúdo inicial para os usuários.

![Uma atividade ao vivo em uma tela de bloqueio do iPhone com as pontuações de duas equipes. Tanto o Wild Bird Fund quanto o Owl Rehab têm pontuações de 0.]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### Etapa 3: Retome o rastreamento de atividades {#resume-activity-tracking}

Para garantir que a Braze rastreie sua Atividade ao Vivo na inicialização do app:

1. Abra seu arquivo `AppDelegate`.
2. Importe o módulo `ActivityKit` se ele estiver disponível.
3. Chame [`resumeActivities(ofType:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)) em `application(_:didFinishLaunchingWithOptions:)` para todos os tipos de `ActivityAttributes` que você registrou no seu aplicativo.

Isso permite que a Braze retome as tarefas para rastrear atualizações de tokens push para todas as Atividades ao Vivo ativas. Observe que, se um usuário tiver descartado explicitamente a Atividade ao Vivo no dispositivo, ela será considerada removida e a Braze não a rastreará mais.

#### Exemplo

```swift
import UIKit
import BrazeKit

#if canImport(ActivityKit)
  import ActivityKit
#endif

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {

    if #available(iOS 16.1, *) {
      Self.braze?.liveActivities.resumeActivities(
        ofType: Activity<SportsActivityAttributes>.self
      )
    }

    return true
  }
}
```

### Etapa 4: Atualize a atividade {#update-the-activity}

![Uma atividade ao vivo em uma tela de bloqueio do iPhone com as pontuações de duas equipes. O Wild Bird Fund tem 2 pontos e o Owl Rehab tem 4 pontos.]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

O endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) permite que você atualize uma Atividade ao Vivo por meio de notificações por push enviadas pela REST API da Braze. Use esse endpoint para atualizar o `ContentState` da sua Atividade ao Vivo.

Ao atualizar o `ContentState`, o widget da Atividade ao Vivo exibirá as novas informações. Veja como seria o show Superb Owl no final do primeiro tempo.

Consulte nosso artigo sobre o [endpoint `/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) para obter todos os detalhes.

### Etapa 5: Encerre a atividade {#end-the-activity}

Quando uma Atividade ao Vivo está ativa, ela é exibida na tela de bloqueio do usuário e no Dynamic Island. Para encerrá-la pela Braze, use o endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) com `end_activity` definido como `true`.

Para melhorar a confiabilidade ao encerrar uma Atividade ao Vivo, siga estas etapas opcionais:

1. Opcionalmente, inclua `dismissal_date` na mesma solicitação de `update` para sugerir quando o iOS deve remover a interface da Atividade ao Vivo.
2. Verifique os resultados de entrega no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab).

#### Organizando o descarte automático {#arranging-automatic-dismissal}

Para organizar o descarte automático, agende uma solicitação de acompanhamento para o endpoint de atualização após iniciar a Atividade ao Vivo.

1. Envie uma solicitação `/messages/live_activity/start` com um `activity_id` que você possa rastrear.
2. Armazene esse `activity_id` e o horário de encerramento desejado no agendador do seu backend.
3. No horário de encerramento desejado, envie uma solicitação `/messages/live_activity/update` com `end_activity` definido como `true`.
4. Configure a data de descarte na mesma solicitação de atualização. Para saber mais, consulte o endpoint [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).

Observe que o momento do descarte é controlado pelo iOS. Mesmo após enviar uma solicitação de encerramento válida, a remoção da tela de bloqueio ou do Dynamic Island pode ser atrasada ou se comportar de forma diferente com base em condições do sistema operacional.

Uma Atividade ao Vivo também pode ser encerrada fora da Braze:

* **Descarte pelo usuário**: Um usuário pode descartar manualmente uma Atividade ao Vivo.
* **Tempo limite**: Após um tempo padrão de oito horas, o iOS removerá a Atividade ao Vivo do Dynamic Island do usuário. Após um tempo padrão de 12 horas, o iOS removerá a Atividade ao Vivo da tela de bloqueio do usuário.

Consulte nosso artigo sobre o [endpoint `/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) para obter todos os detalhes.

## Rastreamento de Atividades ao Vivo {#tracking-live-activities}

Os eventos de Atividade ao Vivo estão disponíveis em Currents, Compartilhamento de dados Snowflake e Criador de consultas. Os eventos a seguir podem ajudar você a entender e monitorar o ciclo de vida das suas Atividades ao Vivo, rastrear a disponibilidade de tokens e diagnosticar problemas ou verificar status de entrega de forma independente.

- [Mudança de token push-to-start de Atividade ao Vivo]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events#live-activity-push-to-start-token-change-events): Captura quando um token push-to-start (PTS) é adicionado ou atualizado na Braze, permitindo que você rastreie registros e disponibilidade de tokens por usuário.
- [Mudança de token de atualização de Atividade ao Vivo]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events#live-activity-update-token-change-events): Rastreia a adição, atualização ou remoção de tokens de atualização de Atividade ao Vivo (LAU).
- [Envio de Atividade ao Vivo]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events#live-activity-send-events): Registra cada vez que uma Atividade ao Vivo é iniciada, atualizada ou encerrada pela Braze.
- [Resultado de Atividade ao Vivo]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events#live-activity-outcome-events): Indica o status final de entrega ao serviço de Notificações por Push da Apple (APNs) para cada Atividade ao Vivo enviada pela Braze.

## Verificar envios de Atividade ao Vivo {#verify-live-activity-sends}

Se você precisar confirmar se um espaço de trabalho está enviando Atividades ao Vivo do iOS, pode usar os seguintes métodos:

### Registro de atividades de envio de mensagem {#message-activity-log}

Acesse **Configurações** > **Registro de atividades de envio de mensagem** e filtre por erros de Atividade ao Vivo para ver quaisquer resultados de entrega relacionados a Atividades ao Vivo durante o período esperado. Para saber mais, consulte [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).

### Criador de consultas, Currents ou Compartilhamento de dados Snowflake {#query-builder-currents-or-snowflake-data-sharing}

Verifique os seguintes eventos de Atividade ao Vivo para confirmar o ciclo de vida e a entrega:

- **Envio de Atividade ao Vivo:** Registrado cada vez que uma Atividade ao Vivo é iniciada, atualizada ou encerrada pela Braze
- **Resultado de Atividade ao Vivo:** Status final de entrega aos APNs para cada Atividade ao Vivo enviada

Opcionalmente, você também pode verificar sinais de disponibilidade de tokens:
- **Mudança de token push-to-start de Atividade ao Vivo**
- **Mudança de token de atualização de Atividade ao Vivo**

### Dashboard de uso da API {#api-usage-dashboard}

Acesse **Configurações** > **APIs e identificadores** > **Dashboard**, selecione **Filtros** e filtre por **Endpoint** para ver as respostas da API. Por exemplo, selecione `/messages/live_activity/update` (ou `/messages/live_activity/start`) e visualize o volume de solicitações nos últimos 30 dias. As respostas da API indicam que a API está sendo chamada e que as notificações de Atividade ao Vivo do iOS estão sendo usadas nesse espaço de trabalho. Para saber mais, consulte [Dashboard de uso da API]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage).

## Observar eventos de Atividade ao Vivo (opcional) {#observe-live-activity-events}

{% sdk_min_versions swift:14.2.0 %}

{% alert important %}
Não se inscreva diretamente nesses streams do ActivityKit com a Apple, pois isso entrará em conflito com as inscrições da Braze e impedirá que as Atividades ao Vivo funcionem corretamente:

1. [`pushTokenUpdates`](https://developer.apple.com/documentation/activitykit/activity/pushtokenupdates-swift.property)
2. [`activityStateUpdates`](https://developer.apple.com/documentation/activitykit/activity/activitystateupdates-swift.property)
3. [`contentUpdates`](https://developer.apple.com/documentation/activitykit/activity/contentupdates-swift.property)
4. [`pushToStartTokenUpdates`](https://developer.apple.com/documentation/activitykit/activity/pushtostarttokenupdates)
5. [`activityUpdates`](https://developer.apple.com/documentation/activitykit/activity/activityupdates-swift.type.property)

Em vez disso, use as inscrições mencionadas nesta seção.
{% endalert %}

O SDK da Braze fornece dois métodos de inscrição em `braze.liveActivities` para observar o ciclo de vida completo das Atividades ao Vivo. Para um passo a passo completo, consulte o [tutorial de Atividades ao Vivo](https://braze-inc.github.io/braze-swift-sdk/tutorials/brazekit/b4-live-activities).

- [`subscribeToStateUpdates(_:)`](#subscribe-to-state-updates): Entrega eventos de ciclo de vida tanto para o registro de tokens push-to-start quanto para instâncias de atividades em execução.
- [`subscribeToErrors(_:)`](#subscribe-to-errors): Entrega erros do SDK e do lado do servidor encontrados durante o rastreamento de Atividades ao Vivo.

{% alert note %}
Ambos os métodos retornam um [`Braze.Cancellable`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/cancellable-swift.typealias). A inscrição permanece ativa enquanto o valor retornado for mantido por uma referência forte (por exemplo, armazene-o em uma propriedade com o mesmo ciclo de vida da sua instância `Braze`).
{% endalert %}

### Configurar inscrições {#set-up-subscriptions}

Configure as inscrições uma vez em `application(_:didFinishLaunchingWithOptions:)` e mantenha-as durante toda a vida útil do seu app:

```swift
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze?

  var stateSubscription: Braze.Cancellable?
  var errorSubscription: Braze.Cancellable?

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let braze = Braze(configuration: config)
    Self.braze = braze

    if #available(iOS 16.1, *) {
      stateSubscription = Self.braze?.liveActivities.subscribeToStateUpdates { event in
        self.handleStateUpdate(event)
      }
      errorSubscription = Self.braze?.liveActivities.subscribeToErrors { error in
        self.handleLiveActivityError(error)
      }
    }

    return true
  }
}
```

{% alert note %}
Os retornos de chamada são acionados apenas para eventos futuros de atividades ao vivo — eles não reproduzem o estado atual no momento da inscrição. Para consultar o snapshot do estado atual, use `Activity<T>.activities`.
{% endalert %}

### subscribeToStateUpdates {#subscribe-to-state-updates}

`subscribeToStateUpdates(_:)` entrega valores `UpdateEvent` que cobrem o ciclo de vida completo das Atividades ao Vivo. Os eventos são divididos em dois escopos:

- `.activityType(ActivityType)`: Eventos em nível de tipo para registro de tokens push-to-start (iOS 17.2+). Nenhuma instância de atividade existe ainda.
- `.activityInstance(ActivityInstance)`: Eventos em nível de instância para uma atividade específica em execução.

Múltiplos assinantes são suportados — cada inscrição ativa recebe cada emissão de forma independente.

#### Eventos com escopo de tipo {#type-scoped-events}

| Evento | Quando é disparado |
| ----- | ------------- |
| `.pushToStartTokenRead(activityType:)` | Um token push-to-start foi lido do sistema operacional. A Braze agora pode iniciar remotamente uma nova atividade desse tipo. |
| `.pushToStartTokenFlushed(activityType:)` | O token foi enviado ao servidor da Braze. A Braze pode enviar notificações push-to-start para esse tipo. |
| `.pushToStartOptedOut(activityType:)` | O usuário optou por não receber push-to-start para esse tipo de atividade por meio de `optOutPushToStart(type:)`. |
| `.pushToStartOptOutFlushed(activityType:)` | A opção de não receber foi enviada ao servidor da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos com escopo de tipo" }

#### Eventos com escopo de instância {#instance-scoped-events}

| Evento | Quando é disparado |
| ----- | ------------- |
| `.started(activityId:activityType:pushTokenTag:launchSource:)` | O SDK começou a rastrear essa atividade por meio de `launchActivity(pushTokenTag:activity:)`. O valor de `launchSource` é `.local` para atividades iniciadas pelo app ou `.pushToStart` para atividades iniciadas remotamente. |
| `.resumed(activityId:activityType:pushTokenTag:)` | O SDK retomou o rastreamento dessa atividade por meio de `resumeActivities(ofType:)`. |
| `.pushTokenFlushed(activityId:activityType:pushTokenTag:)` | O token de push da atividade foi aceito pelo servidor da Braze — a atividade agora pode receber atualizações remotas. |
| `.active(activityId:activityType:)` | A atividade está atualmente ativa e visível para o usuário. |
| `.stale(activityId:activityType:staleDate:)` | O conteúdo da atividade ficou desatualizado. Emitido apenas no iOS 16.2 e posterior. |
| `.dismissed(activityId:activityType:)` | O usuário descartou manualmente a atividade. |
| `.ended(activityId:activityType:)` | A atividade foi encerrada. |
| `.contentUpdated(activityId:activityType:)` | O estado do conteúdo da atividade foi atualizado (iOS 16.2+). Use lógica personalizada para buscar a `Activity<T>` pelo ID em `Activity.activities` e acessar o estado tipado por meio de `activity.content.state`. |
| `.pushTokenUpdated(activityId:activityType:)` | O ActivityKit rotacionou o token de push da atividade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos com escopo de instância" }

##### Exemplo

```swift
func handleStateUpdate(_ event: Braze.LiveActivities.UpdateEvent) {
  switch event {

  // Type-scoped: push-to-start token lifecycle (iOS 17.2+)
  case .activityType(.pushToStartTokenRead(let activityType)):
    print("[\(activityType)] Push-to-start token read by SDK")

  // ...

  // Instance-scoped: SDK tracking
  case .activityInstance(.started(let id, let type, let tag, let source)):
    print("[\(type)] Activity \(id) started via \(source), tag: \(tag)")

  // ...

  // Instance-scoped: ActivityKit lifecycle
  case .activityInstance(.active(let id, let type)):
    print("[\(type)] Activity \(id) is active")

  // ...

  case .activityInstance(.ended(let id, let type)):
    print("[\(type)] Activity \(id) ended")

  // Instance-scoped: content updates (iOS 16.2+)
  case .activityInstance(.contentUpdated(let id, let type)):
    // For more advanced use cases of `contentUpdated`, see the section below
    print("[\(type)] Content updated for activity \(id)")

  case .activityInstance(.pushTokenUpdated(let id, let type)):
    print("[\(type)] Activity \(id) push token rotated")
  }
}
```

### subscribeToErrors {#subscribe-to-errors}

`subscribeToErrors(_:)` entrega valores `ErrorEvent` usando os mesmos dois escopos que `UpdateEvent`:

- `.activityType(ActivityType)`: Erros em nível de tipo para falhas de registro push-to-start.
- `.activityInstance(ActivityInstance)`: Erros em nível de instância para uma atividade em execução.

Use a flag `isTransient` para determinar se uma nova tentativa é apropriada. O SDK tenta novamente automaticamente as falhas transitórias.

#### Erros com escopo de tipo {#type-scoped-errors}

| Erro | Quando é disparado |
| ----- | ------------- |
| `.pushToStartRegistrationFailed(activityType:isTransient:reason:)` | O token push-to-start não conseguiu chegar ao servidor da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erros com escopo de tipo" }

#### Erros com escopo de instância {#instance-scoped-errors}

| Erro | Quando é disparado |
| ----- | ------------- |
| `.registrationFailed(activityId:activityType:pushTokenTag:isTransient:reason:)` | O token de push da atividade não conseguiu se registrar na Braze. |
| `.activityNotFound(activityId:activityType:)` | `resumeActivities(ofType:)` encontrou um mapeamento armazenado para uma atividade que não está mais em execução — provavelmente ela foi encerrada enquanto o app estava fechado. |
| `.invalidPushTokenTag(activityId:activityType:tag:)` | `launchActivity(pushTokenTag:activity:)` foi chamado com uma tag inválida. As tags devem ser não vazias e ter menos de 256 bytes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erros com escopo de instância" }

##### Exemplo

```swift
func handleLiveActivityError(_ error: Braze.LiveActivities.ErrorEvent) {
  switch error {

  // Type-scoped errors
  case .activityType(.pushToStartRegistrationFailed(let type, let isTransient, let reason)):
    if isTransient {
      print("[\(type)] Push-to-start registration failed (transient, will retry): \(reason)")
    } else {
      print("[\(type)] Push-to-start registration failed (permanent): \(reason)")
    }

  // Instance-scoped errors
  case .activityInstance(.registrationFailed(let id, let type, _, let isTransient, let reason)):
    if isTransient {
      print("[\(type)] Activity \(id) registration failed (transient, retrying): \(reason)")
    } else {
      print("[\(type)] Activity \(id) registration failed (permanent): \(reason)")
    }

  case .activityInstance(.activityNotFound(let id, let type)):
    print("[\(type)] Stored activity \(id) not found on resume")

  case .activityInstance(.invalidPushTokenTag(let id, let type, let tag)):
    print("[\(type)] Activity \(id) has invalid push token tag '\(tag)'")
  }
}
```

### Lidar com atualizações de estado do conteúdo (opcional) {#handle-content-state}

Se você quiser usar o estado do conteúdo da instância real da Atividade ao Vivo, siga esta seção.

Quando um evento `.contentUpdated` é disparado, use lógica personalizada para buscar a `Activity<T>` em execução pelo seu ID em `Activity.activities` e, em seguida, acesse o `ContentState` tipado por meio de `activity.content.state`.

#### Tipo de atributos único {#single-attributes-type}

```swift
case .activityInstance(.contentUpdated(let id, let type)):
  #if canImport(ActivityKit)
    // Add custom logic look up the Activity<T> by ID and access your app's typed ContentState.
    // In this example, `SportsActivityAttributes` is the app's custom type.
    if #available(iOS 16.2, *),
      let activity = findActivityInstance(id: id, as: SportsActivityAttributes.self)
    {
      // `activityContent` is now strongly typed as a `SportsActivityAttributes`
      let activityContent = activity.content.state
      print("[\(type)] Game \(id) — score: \(activityContent.teamOneScore)–\(activityContent.teamTwoScore)")
      return
    }
  #endif
  print("[\(type)] Content updated for activity \(id)")

// ...

// - MARK: Helper methods

@available(iOS 16.2, *)
func findActivityInstance<Attributes: ActivityAttributes>(
  id: String,
  as type: Attributes.Type
) -> Activity<Attributes>? {
  // Use Apple's API to find the matching Live Activity instance:
  // - https://developer.apple.com/documentation/activitykit/activity/activities
  Activity<Attributes>.activities.first(where: { $0.id == id })
}
```

#### Múltiplos tipos de atributos {#multiple-attributes-types}

Se o seu app usa múltiplos tipos de `ActivityAttributes`, verifique a string `type` para buscar a `Activity<T>` apropriada:

```swift
case .activityInstance(.contentUpdated(let id, let type)):
  #if canImport(ActivityKit)
    if #available(iOS 16.2, *) {
      if type == SportsActivityAttributes.name,
        let activity = findActivityInstance(id: id, as: SportsActivityAttributes.self)
      {
        let activityContent = activity.content.state
        print("[\(type)] Game \(id) — score: \(activityContent.teamOneScore)–\(activityContent.teamTwoScore)")
        return

      } else if type == OrderActivityAttributes.name,
        let activity = findActivityInstance(id: id, as: OrderActivityAttributes.self)
      {
        let activityContent = activity.content.state
        print("[\(type)] Order \(id) — status: \(activityContent.status), ETA: \(activityContent.eta)")
        return
      }
    }
  #endif
  print("[\(type)] Content updated for activity \(id)")

// ...

// - MARK: Helper methods

@available(iOS 16.2, *)
func findActivityInstance<Attributes: ActivityAttributes>(
  id: String,
  as type: Attributes.Type
) -> Activity<Attributes>? {
  // Use Apple's API to find the matching Live Activity instance:
  // - https://developer.apple.com/documentation/activitykit/activity/activities
  Activity<Attributes>.activities.first(where: { $0.id == id })
}
```

## Perguntas frequentes (FAQ) {#faq}

### Funcionalidade e suporte {#functionality-and-support}

#### Quais plataformas suportam Atividades ao Vivo? {#what-platforms-support-live-activities}

Atualmente, as Atividades ao Vivo são um recurso específico do iOS e iPadOS. Por padrão, atividades lançadas em um iPhone ou iPad também são exibidas em qualquer dispositivo watchOS 11+ ou macOS 26+ emparelhado.

![Uma captura de tela de uma barra de menu do macOS exibindo uma Atividade ao Vivo como um alerta.]({% image_buster /assets/img/live-activity-macos.png %}){: style="max-width:60%;"}

O artigo sobre Atividades ao Vivo aborda os [pré-requisitos]({{site.baseurl}}/developer_guide/platforms/swift/live_activities#prerequisites) para o gerenciamento de Atividades ao Vivo por meio do SDK Swift da Braze.

#### Os apps React Native são compatíveis com Atividades ao Vivo? {#do-react-native-apps-support-live-activities}

Sim, o React Native SDK 3.0.0+ oferece suporte a Atividades ao Vivo por meio do SDK Swift da Braze. Ou seja, você precisa escrever código React Native iOS diretamente sobre o SDK Swift da Braze.

Não há uma API de conveniência JavaScript específica do React Native para Atividades ao Vivo porque os recursos de Atividades ao Vivo fornecidos pela Apple usam linguagens intraduzíveis em JavaScript (por exemplo, concorrência Swift, genéricos, SwiftUI).

#### A Braze oferece suporte a Atividades ao Vivo como uma Campaign ou etapa do Canvas? {#does-braze-support-live-activities-as-a-campaign-or-canvas-step}

Não, isso não é suportado no momento.

### Notificações por push e Atividades ao Vivo {#push-notifications-and-live-activities}

#### O que acontece se uma notificação por push for enviada enquanto uma Atividade ao Vivo estiver ativa? {#what-happens-if-a-push-notification-is-sent-while-a-live-activity-is-active}

![Uma tela de telefone com uma Atividade ao Vivo de um jogo esportivo entre Bulls e Bears no meio da tela e um texto de notificação por push lorem ipsum na parte inferior da tela.]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

As Atividades ao Vivo e as notificações por push ocupam espaços diferentes na tela e não entram em conflito na tela do usuário.

#### Se as Atividades ao Vivo utilizam a funcionalidade de mensagens push, as notificações por push precisam estar ativadas para receber Atividades ao Vivo? {#if-live-activities-leverage-push-message-functionality-do-push-notifications-need-to-be-enabled-to-receive-live-activities}

Embora as Atividades ao Vivo dependam de notificações por push para atualizações, elas são controladas por configurações de usuário diferentes. Um usuário pode aceitar Atividades ao Vivo, mas não as notificações por push, e vice-versa.

Os tokens de atualização de Atividade ao Vivo expiram após oito horas.

#### As Atividades ao Vivo requerem push primers? {#do-live-activities-require-push-primers}

Os [push primers]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) são uma prática recomendada para solicitar que os usuários aceitem notificações por push do seu app. No entanto, não há nenhum prompt do sistema para aceitar Atividades ao Vivo. Por padrão, os usuários aceitam Atividades ao Vivo para um app individual quando instalam esse app no iOS 16.1 ou posterior. Essa permissão pode ser desativada ou reativada nas configurações do dispositivo por app.

### Tópicos técnicos e solução de problemas {#technical-topics-and-troubleshooting}

#### Como posso saber se as Atividades ao Vivo têm erros? {#how-do-i-know-if-live-activities-has-errors}

Todos os erros de Atividades ao Vivo são registrados no dashboard da Braze no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log), onde é possível filtrar por "LiveActivity Errors".

#### Depois de enviar uma notificação push-to-start, por que não recebi minha Atividade ao Vivo? {#after-sending-a-push-to-start-notification-why-havent-i-received-my-live-activity}

Primeiro, verifique se sua carga útil inclui todos os campos obrigatórios descritos no endpoint [`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start). Os campos `activity_attributes` e `content_state` devem corresponder às propriedades definidas no código do seu projeto. Se tiver certeza de que a carga útil está correta, é possível que você esteja sendo limitado pelos APNs. Esse limite é imposto pela Apple e não pela Braze.

Para verificar se a notificação push-to-start chegou com sucesso ao dispositivo, mas não foi exibida devido a limites de taxa, você pode depurar o projeto usando o app Console no Mac. Anexe o processo de gravação do dispositivo desejado e, em seguida, filtre os registros por `process:liveactivitiesd` na barra de pesquisa.

#### Depois de iniciar minha Atividade ao Vivo com push-to-start, por que ela não está recebendo novas atualizações? {#after-starting-my-live-activity-with-push-to-start-why-isnt-it-receiving-new-updates}

Verifique se você implementou corretamente as instruções descritas na [configuração do BrazeLiveActivityAttributes](#swift_brazeActivityAttributes). Seu `ActivityAttributes` deve conter tanto a conformidade com o protocolo `BrazeLiveActivityAttributes` quanto a propriedade `brazeActivityId`.

Depois de receber uma notificação push-to-start de Atividade ao Vivo, verifique se você consegue ver uma solicitação de rede de saída para o endpoint `/push_token_tag` da sua URL da Braze e se ela contém o ID da atividade correto no campo `"tag"`.

Por fim, certifique-se de que o tipo de atributo da Atividade ao Vivo na sua carga útil de atualização corresponda exatamente à string e à classe usadas na chamada do método do SDK para `registerPushToStart`. Use constantes para evitar erros de digitação.

#### Estou recebendo uma resposta de acesso negado quando tento usar o endpoint `live_activity/update`. Por quê? {#i-am-receiving-an-access-denied-response-when-i-try-to-use-the-live_activityupdate-endpoint-why}

As chaves de API que você usa precisam ter as permissões corretas para acessar os diferentes endpoints da API da Braze. Se estiver usando uma chave de API criada anteriormente, é possível que tenha se esquecido de atualizar as permissões. Leia nossa [visão geral da segurança da chave de API]({{site.baseurl}}/api/basics#rest-api-key-security) para relembrar.

#### O endpoint `messages/send` compartilha os limites de taxa com o endpoint `messages/live_activity/update`? {#does-the-messagessend-endpoint-share-rate-limits-with-the-messageslive_activityupdate-endpoint}

Por padrão, o limite de taxa do endpoint `messages/live_activity/update` é de 250.000 solicitações por hora, por espaço de trabalho e em vários endpoints. Consulte os [limites de taxa da API]({{site.baseurl}}/api/api_limits) para obter mais informações.