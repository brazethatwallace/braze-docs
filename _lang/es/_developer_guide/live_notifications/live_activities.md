---
nav_title: Actividades en vivo para Swift
article_title: Actividades en vivo para el SDK Swift de Braze
page_order: 0.2
description: "Aprende a configurar las actividades en vivo para el SDK Swift de Braze."
platform:
  - Swift
---

# Actividades en vivo para Swift {#live-activities-for-swift}

> Aprende a implementar las actividades en vivo para el SDK Swift de Braze. Las actividades en vivo son notificaciones persistentes e interactivas que se muestran directamente en la pantalla de bloqueo, lo que permite a los usuarios obtener actualizaciones dinámicas en tiempo real&#8212;sin necesidad de desbloquear el dispositivo.

## Cómo funciona {#how-it-works}

![Actividad en vivo de un rastreador de entregas en la pantalla de bloqueo de un iPhone. Una barra de estado con un coche está casi medio llena. El texto dice «2 minutos hasta la recogida».]({% image_buster /assets/img/swift/live_activities/example_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

Las actividades en vivo presentan una combinación de información estática e información dinámica que tú actualizas. Por ejemplo, puedes crear una actividad en vivo que ofrezca un seguimiento del estado de una entrega. Esta actividad en vivo tendría el nombre de tu empresa como información estática, así como un "Tiempo de entrega" dinámico que se actualizaría a medida que el conductor de la entrega se acercara a su destino.

Como desarrollador, puedes utilizar Braze para gestionar los ciclos de vida de tus actividades en vivo, hacer llamadas a la REST API de Braze para realizar actualizaciones de actividades en vivo y hacer que todos los dispositivos suscritos reciban la actualización lo antes posible. Y, como gestionas las actividades en vivo a través de Braze, puedes utilizarlas en tándem con tus otros canales de mensajería&mdash;notificaciones push, mensajes dentro de la aplicación, Content Cards&mdash;para impulsar la adopción.

## Diagrama de secuencia {#sequence-diagram}

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

## Implementación de una actividad en vivo {#implementing-a-live-activity}

#{% multi_lang_include developer_guide/prerequisites/swift.md %} También deberás completar lo siguiente:

- Asegúrate de que tu proyecto esté dirigido a iOS 16.1 o posterior.
- Añade el derecho `Push Notification` en **Signing & Capabilities** en tu proyecto Xcode.
- Asegúrate de que se usen claves `.p8` para enviar notificaciones. Los archivos antiguos como `.p12` o `.pem` no son compatibles.
- A partir de la versión 8.2.0 del SDK Swift de Braze, puedes [registrar remotamente una actividad en vivo](#swift_step-2-start-the-activity). Para utilizar esta característica, se necesita iOS 17.2 o posterior.

{% alert note %}
Aunque las actividades en vivo y las notificaciones push son similares, sus permisos de sistema son distintos. Por defecto, todas las características de las actividades en vivo están habilitadas, pero los usuarios pueden deshabilitar esta característica por aplicación.
{% endalert %}

{% sdk_min_versions swift:5.11.0 %}

### Paso 1: Crear una actividad {#create-an-activity}

En primer lugar, asegúrate de que has seguido [Mostrar datos en vivo con Live Activities](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities) en la documentación de Apple para configurar las actividades en vivo en tu aplicación iOS. Como parte de esta tarea, asegúrate de incluir `NSSupportsLiveActivities` configurado como `YES` en tu `Info.plist`.

Dado que la naturaleza exacta de tu actividad en vivo será específica de tu caso empresarial, tendrás que configurar e inicializar los objetos de [Activity](https://developer.apple.com/documentation/activitykit/activityattributes). Es importante que definas lo siguiente:
* `ActivityAttributes`: Este protocolo define el contenido estático (invariable) y dinámico (cambiante) que aparecerá en tu actividad en vivo.
* `ActivityAttributes.ContentState`: Este tipo define los datos dinámicos que se actualizarán en el transcurso de la actividad.

También utilizarás SwiftUI para crear la presentación de la interfaz de usuario de la pantalla de bloqueo y la Dynamic Island en los dispositivos compatibles.

Asegúrate de que conoces los [requisitos previos y las limitaciones](https://developer.apple.com/documentation/activitykit/displaying-live-data-with-live-activities#Understand-constraints) de Apple para las actividades en vivo, ya que estas limitaciones son independientes de Braze.

{% alert note %}
Si esperas enviar push frecuentes a la misma actividad en vivo, puedes evitar que el límite de presupuesto de Apple te restrinja configurando `NSSupportsLiveActivitiesFrequentUpdates` en `YES` en tu archivo `Info.plist`. Para más detalles, consulta la sección [`Determine the update frequency`](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications#Determine-the-update-frequency) de la documentación de ActivityKit.
{% endalert %}

#### Ejemplo {#example}

Imaginemos que queremos crear una actividad en vivo para ofrecer a nuestros usuarios actualizaciones sobre el espectáculo Superb Owl, en el que dos rescates de animales salvajes que compiten entre sí reciben puntos por los búhos que tienen en residencia. Para este ejemplo, hemos creado una estructura llamada `SportsActivityAttributes`, pero puedes utilizar tu propia implementación de `ActivityAttributes`.

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

### Paso 2: Iniciar la actividad {#start-the-activity}

Primero, elige cómo quieres registrar tu actividad:

- **Remoto:** Utiliza el método [`registerPushToStart`](<http://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/registerpushtostart(fortype:name:)>) al principio del ciclo de vida del usuario y antes de que sea necesario el token push-to-start, y luego inicia una actividad utilizando el punto de conexión [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/).
- **Local:** Crea una instancia de tu actividad en vivo y utiliza el método [`launchActivity`](<https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)>) para crear tokens de notificaciones push para que los administre Braze.

{% tabs local %}
{% tab remote %}
{% alert important %}
Para registrar remotamente una actividad en vivo, se necesita iOS 17.2 o posterior.
{% endalert %}

#### Paso 2.1: Añade BrazeKit a tu extensión de widget {#step-21-add-brazekit-to-your-widget-extension}

En tu proyecto de Xcode, selecciona el nombre de tu aplicación y luego **General**. En **Frameworks and Libraries**, confirma que `BrazeKit` está en la lista.

![El framework BrazeKit en Frameworks and Libraries en un proyecto Xcode de ejemplo.]({% image_buster /assets/img/swift/live_activities/xcode_frameworks_and_libraries.png %})

#### Paso 2.2: Añadir el protocolo BrazeLiveActivityAttributes {#brazeActivityAttributes}

En tu implementación de `ActivityAttributes`, añade la conformidad con el protocolo `BrazeLiveActivityAttributes` y, a continuación, añade la propiedad `brazeActivityId` al modelo de atributos.

{% alert important %}
iOS mapea la propiedad `brazeActivityId` con el campo correspondiente en la carga útil push-to-start de la actividad en vivo, por lo que no se debe cambiar el nombre ni asignarle ningún otro valor.
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

#### Paso 2.3: Registro para push-to-start {#step-23-register-for-push-to-start}

A continuación, registra el tipo de actividad en vivo, para que Braze pueda hacer un seguimiento de todos los tokens push-to-start y de las instancias de actividad en vivo asociadas a este tipo.

{% alert warning %}
El sistema operativo iOS solo genera tokens push-to-start durante la primera instalación de una aplicación después de reiniciar un dispositivo. Para asegurarte de que tus tokens se registran de forma fiable, llama a `registerPushToStart` en tu método `didFinishLaunchingWithOptions`.
{% endalert %}

###### Ejemplo

En el siguiente ejemplo, la clase `LiveActivityManager` maneja objetos de actividad en vivo. A continuación, el método `registerPushToStart` registra `SportsActivityAttributes`:

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

#### Paso 2.4: Enviar una notificación push-to-start {#step-24-send-a-push-to-start-notification}

Envía una notificación push-to-start remota utilizando el punto de conexión [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/).
{% endtab %}

{% tab local %}
Puedes utilizar [el framework ActivityKit de Apple](https://developer.apple.com/documentation/activitykit) para obtener un token de notificaciones push, que el SDK de Braze puede administrar por ti. Esto te permite actualizar actividades en vivo a través de la API de Braze, ya que Braze enviará el token de notificaciones push al servicio de notificaciones push de Apple (APNs) en el backend.

1. Crea una instancia de tu implementación de actividad en vivo utilizando las API de ActivityKit de Apple.
2. Configura el parámetro `pushType` como `.token`.
3. Introduce los `ActivitiesAttributes` y `ContentState` de las actividades en vivo que hayas definido.
4. Registra tu actividad en tu instancia de Braze pasándola a [`launchActivity(pushTokenTag:activity:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class). El parámetro `pushTokenTag` es una cadena personalizada que tú defines. Debe ser única para cada actividad en vivo que crees.

Una vez que hayas registrado la actividad en vivo, el SDK de Braze extraerá y observará los cambios en los tokens de notificaciones push.

#### Ejemplo

Para nuestro ejemplo, crearemos una clase llamada `LiveActivityManager` como interfaz para nuestros objetos de actividad en vivo. A continuación, configuraremos `pushTokenTag` como `"sports-game-2024-03-15"`.

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

Tu widget de actividad en vivo mostraría este contenido inicial a tus usuarios.

![Una actividad en vivo en la pantalla de bloqueo de un iPhone con los resultados de dos equipos. Tanto el Wild Bird Fund como el Owl Rehab tienen puntuaciones de 0.]({% image_buster /assets/img/swift/live_activities/example_1_1.png %}){: style="max-width:40%;"}
{% endtab %}
{% endtabs %}

### Paso 3: Reanudar el seguimiento de la actividad {#resume-activity-tracking}

Para garantizar que Braze realiza un seguimiento de tu actividad en vivo al iniciar la aplicación:

1. Abre tu archivo `AppDelegate`.
2. Importa el módulo `ActivityKit` si está disponible.
3. Llama a [`resumeActivities(ofType:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/resumeactivities(oftype:)) en `application(_:didFinishLaunchingWithOptions:)` para todos los tipos de `ActivityAttributes` que hayas registrado en tu aplicación.

Esto permite a Braze reanudar las tareas de seguimiento de las actualizaciones de tokens de notificaciones push de todas las actividades en vivo activas. Ten en cuenta que si un usuario ha descartado explícitamente la actividad en vivo en su dispositivo, se considera eliminada, y Braze dejará de seguirla.

###### Ejemplo

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

### Paso 4: Actualizar la actividad {#update-the-activity}

![Una actividad en vivo en la pantalla de bloqueo de un iPhone con los resultados de dos equipos. El Wild Bird Fund tiene 2 puntos y el Owl Rehab tiene 4 puntos.]({% image_buster /assets/img/swift/live_activities/example_1_2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

El punto de conexión [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) te permite actualizar una actividad en vivo mediante notificaciones push enviadas a través de la REST API de Braze. Utiliza este punto de conexión para actualizar el `ContentState` de tu actividad en vivo.

A medida que actualices tu `ContentState`, tu widget de actividad en vivo mostrará la nueva información. Así es como podría verse el espectáculo Superb Owl al final del primer tiempo.

Consulta nuestro artículo sobre el [punto de conexión `/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) para conocer todos los detalles.

### Paso 5: Finalizar la actividad {#end-the-activity}

Cuando una actividad en vivo está activa, se muestra tanto en la pantalla de bloqueo del usuario como en la Dynamic Island. Para finalizarla a través de Braze, utiliza el punto de conexión [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) con `end_activity` configurado como `true`.

Para mejorar la fiabilidad al finalizar una actividad en vivo, sigue estos pasos opcionales:

1. Opcionalmente, incluye `dismissal_date` en esa misma solicitud de `update` para sugerir cuándo iOS debe eliminar la interfaz de la actividad en vivo.
2. Verifica los resultados de entrega en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).

#### Programar el descarte automático {#arranging-automatic-dismissal}

Para programar el descarte automático, planifica una solicitud de seguimiento al punto de conexión de actualización después de iniciar la actividad en vivo.

1. Envía una solicitud `/messages/live_activity/start` con un `activity_id` que puedas rastrear.
2. Almacena ese `activity_id` y tu hora de finalización objetivo en tu programador del backend.
3. En la hora de finalización objetivo, envía una solicitud `/messages/live_activity/update` con `end_activity` configurado como `true`.
4. Configura la fecha de descarte en la misma solicitud de actualización. Para más detalles, consulta el punto de conexión [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/).

Ten en cuenta que el momento del descarte lo controla iOS. Incluso después de enviar una solicitud de finalización válida, la eliminación de la pantalla de bloqueo o la Dynamic Island puede retrasarse o comportarse de forma diferente según las condiciones del sistema operativo.

Una actividad en vivo también puede finalizar fuera de Braze:

* **Descarte del usuario**: Un usuario puede descartar manualmente una actividad en vivo.
* **Tiempo de espera agotado**: Tras un tiempo predeterminado de ocho horas, iOS eliminará la actividad en vivo de la Dynamic Island del usuario. Tras un tiempo predeterminado de 12 horas, iOS eliminará la actividad en vivo de la pantalla de bloqueo del usuario.

Consulta nuestro artículo sobre el [punto de conexión `/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) para conocer todos los detalles.

## Seguimiento de actividades en vivo {#tracking-live-activities}

Los eventos de actividad en vivo están disponibles en Currents, Snowflake Data Sharing y el Generador de consultas. Los siguientes eventos pueden ayudarte a comprender y supervisar el ciclo de vida de tus actividades en vivo, realizar un seguimiento de la disponibilidad de tokens y diagnosticar problemas o verificar el estado de entrega de forma independiente.

- [Cambio de token push-to-start de actividad en vivo]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/#live-activity-push-to-start-token-change-events): Captura cuándo se añade o actualiza un token push-to-start (PTS) en Braze, lo que te permite realizar el seguimiento de los registros y la disponibilidad de tokens por usuario.
- [Cambio en el token de actualización de actividad en vivo]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/#live-activity-update-token-change-events): Realiza un seguimiento de la adición, actualización o eliminación de tokens de actualización de actividad en vivo (LAU).
- [Envío de actividad en vivo]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#live-activity-send-events): Registra cada vez que Braze inicia, actualiza o finaliza una actividad en vivo.
- [Resultado de la actividad en vivo]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#live-activity-outcome-events): Indica el estado final de entrega al servicio de notificaciones push de Apple (APNs) para cada actividad en vivo enviada desde Braze.

## Observar eventos de actividad en vivo (opcional) {#observe-live-activity-events}

{% sdk_min_versions swift:14.2.0 %}

{% alert important %}
No te suscribas directamente a estos flujos de ActivityKit con Apple, ya que entrará en conflicto con las suscripciones de Braze e impedirá que las actividades en vivo funcionen correctamente:

1. [`pushTokenUpdates`](https://developer.apple.com/documentation/activitykit/activity/pushtokenupdates-swift.property)
2. [`activityStateUpdates`](https://developer.apple.com/documentation/activitykit/activity/activitystateupdates-swift.property)
3. [`contentUpdates`](https://developer.apple.com/documentation/activitykit/activity/contentupdates-swift.property)
4. [`pushToStartTokenUpdates`](https://developer.apple.com/documentation/activitykit/activity/pushtostarttokenupdates)
5. [`activityUpdates`](https://developer.apple.com/documentation/activitykit/activity/activityupdates-swift.type.property)

En su lugar, utiliza las suscripciones que se mencionan a continuación.
{% endalert %}

El SDK de Braze proporciona dos métodos de suscripción en `braze.liveActivities` para observar el ciclo de vida completo de las actividades en vivo. Para un tutorial paso a paso completo, consulta el [tutorial de actividades en vivo](https://braze-inc.github.io/braze-swift-sdk/tutorials/brazekit/b4-live-activities).

- [`subscribeToStateUpdates(_:)`](#subscribe-to-state-updates): Entrega eventos del ciclo de vida tanto para el registro de tokens push-to-start como para las instancias de actividad en ejecución.
- [`subscribeToErrors(_:)`](#subscribe-to-errors): Entrega errores del SDK y del lado del servidor encontrados durante el seguimiento de actividades en vivo.

{% alert note %}
Ambos métodos devuelven un [`Braze.Cancellable`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/cancellable-swift.typealias). La suscripción permanece activa mientras el valor devuelto se mantenga a través de una referencia fuerte (por ejemplo, almacénalo en una propiedad con el mismo ciclo de vida que tu instancia de `Braze`).
{% endalert %}

### Configurar suscripciones {#set-up-subscriptions}

Configura las suscripciones una vez en `application(_:didFinishLaunchingWithOptions:)` y mantenlas durante toda la vida de tu aplicación:

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
Las devoluciones de llamada solo se activan para eventos futuros de actividad en vivo; no reproducen el estado actual en el momento de la suscripción. Para consultar la instantánea del estado actual, utiliza `Activity<T>.activities`.
{% endalert %}

### subscribeToStateUpdates {#subscribe-to-state-updates}

`subscribeToStateUpdates(_:)` entrega valores `UpdateEvent` que cubren el ciclo de vida completo de las actividades en vivo. Los eventos se dividen en dos ámbitos:

- `.activityType(ActivityType)`: Eventos a nivel de tipo para el registro de tokens push-to-start (iOS 17.2+). Aún no existe ninguna instancia de actividad.
- `.activityInstance(ActivityInstance)`: Eventos a nivel de instancia para una actividad en ejecución específica.

Se admiten múltiples suscriptores: cada suscripción activa recibe cada emisión de forma independiente.

#### Eventos a nivel de tipo {#type-scoped-events}

| Evento | Cuándo se activa |
| ----- | ------------- |
| `.pushToStartTokenRead(activityType:)` | Se leyó un token push-to-start del sistema operativo. Braze ahora puede iniciar remotamente una nueva actividad de este tipo. |
| `.pushToStartTokenFlushed(activityType:)` | El token se envió al servidor de Braze. Braze puede enviar notificaciones push-to-start para este tipo. |
| `.pushToStartOptedOut(activityType:)` | El usuario fue excluido de push-to-start para este tipo de actividad a través de `optOutPushToStart(type:)`. |
| `.pushToStartOptOutFlushed(activityType:)` | La exclusión se envió al servidor de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos a nivel de tipo" }

#### Eventos a nivel de instancia {#instance-scoped-events}

| Evento | Cuándo se activa |
| ----- | ------------- |
| `.started(activityId:activityType:pushTokenTag:launchSource:)` | El SDK comenzó a rastrear esta actividad a través de `launchActivity(pushTokenTag:activity:)`. El valor de `launchSource` es `.local` para actividades iniciadas por la aplicación o `.pushToStart` para actividades iniciadas remotamente. |
| `.resumed(activityId:activityType:pushTokenTag:)` | El SDK reanudó el seguimiento de esta actividad a través de `resumeActivities(ofType:)`. |
| `.pushTokenFlushed(activityId:activityType:pushTokenTag:)` | El token push de la actividad fue aceptado por el servidor de Braze; la actividad ahora puede recibir actualizaciones remotas. |
| `.active(activityId:activityType:)` | La actividad está actualmente activa y visible para el usuario. |
| `.stale(activityId:activityType:staleDate:)` | El contenido de la actividad se ha vuelto obsoleto. Solo se emite en iOS 16.2 y posterior. |
| `.dismissed(activityId:activityType:)` | El usuario descartó manualmente la actividad. |
| `.ended(activityId:activityType:)` | La actividad ha finalizado. |
| `.contentUpdated(activityId:activityType:)` | El estado del contenido de la actividad se actualizó (iOS 16.2+). Utiliza lógica personalizada para buscar la `Activity<T>` por ID desde `Activity.activities` y acceder al estado tipado a través de `activity.content.state`. |
| `.pushTokenUpdated(activityId:activityType:)` | ActivityKit rotó el token push de la actividad. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Eventos a nivel de instancia" }

###### Ejemplo

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

`subscribeToErrors(_:)` entrega valores `ErrorEvent` utilizando los mismos dos ámbitos que `UpdateEvent`:

- `.activityType(ActivityType)`: Errores a nivel de tipo para fallos en el registro push-to-start.
- `.activityInstance(ActivityInstance)`: Errores a nivel de instancia para una actividad en ejecución.

Utiliza la bandera `isTransient` para determinar si es apropiado reintentar. El SDK reintenta automáticamente los fallos transitorios.

#### Errores a nivel de tipo {#type-scoped-errors}

| Error | Cuándo se activa |
| ----- | ------------- |
| `.pushToStartRegistrationFailed(activityType:isTransient:reason:)` | El token push-to-start no pudo llegar al servidor de Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Errores a nivel de tipo" }

#### Errores a nivel de instancia {#instance-scoped-errors}

| Error | Cuándo se activa |
| ----- | ------------- |
| `.registrationFailed(activityId:activityType:pushTokenTag:isTransient:reason:)` | El token push de la actividad no se pudo registrar en Braze. |
| `.activityNotFound(activityId:activityType:)` | `resumeActivities(ofType:)` encontró un mapeado almacenado para una actividad que ya no está en ejecución; probablemente finalizó mientras la aplicación estaba cerrada. |
| `.invalidPushTokenTag(activityId:activityType:tag:)` | `launchActivity(pushTokenTag:activity:)` fue llamado con una etiqueta no válida. Las etiquetas deben ser no vacías y de menos de 256 bytes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Errores a nivel de instancia" }

###### Ejemplo

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

### Manejar actualizaciones del estado del contenido (opcional) {#handle-content-state}

Si deseas utilizar el estado del contenido de la instancia real de la actividad en vivo, sigue esta sección.

Cuando se activa un evento `.contentUpdated`, utiliza lógica personalizada para buscar la `Activity<T>` en ejecución por su ID desde `Activity.activities` y luego accede al `ContentState` tipado a través de `activity.content.state`.

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

#### Múltiples tipos de atributos {#multiple-attributes-types}

Si tu aplicación utiliza múltiples tipos de `ActivityAttributes`, comprueba la cadena `type` para buscar la `Activity<T>` apropiada:

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

## Preguntas más frecuentes (FAQ) {#faq}

### Funcionalidad y soporte {#functionality-and-support}

#### ¿Qué plataformas admiten actividades en vivo? {#what-platforms-support-live-activities}

Actualmente, las actividades en vivo son una característica específica de iOS y iPadOS. De forma predeterminada, las actividades iniciadas en un iPhone o iPad se muestran adicionalmente en cualquier dispositivo watchOS 11+ o macOS 26+ emparejado.

![Captura de pantalla de la barra de menú de macOS mostrando una actividad en vivo como alerta.]({% image_buster /assets/img/live-activity-macos.png %}){: style="max-width:60%;"}

El artículo de actividades en vivo cubre los [requisitos previos]({{site.baseurl}}/developer_guide/platforms/swift/live_activities/#prerequisites) para gestionar actividades en vivo a través del SDK Swift de Braze.

#### ¿Son compatibles las aplicaciones React Native con las actividades en vivo? {#do-react-native-apps-support-live-activities}

Sí, a partir de la versión 3.0.0+ del SDK de React Native se admiten actividades en vivo a través del SDK Swift de Braze. Es decir, tienes que escribir código iOS de React Native directamente sobre el SDK Swift de Braze.

No existe una API de conveniencia JavaScript específica de React Native para las actividades en vivo porque las características de las actividades en vivo proporcionadas por Apple utilizan lenguajes intraducibles en JavaScript (por ejemplo, concurrencia Swift, genéricos, SwiftUI).

#### ¿Admite Braze actividades en vivo como campaña o paso en Canvas? {#does-braze-support-live-activities-as-a-campaign-or-canvas-step}

No, actualmente no es posible.

### Notificaciones push y actividades en vivo {#push-notifications-and-live-activities}

#### ¿Qué ocurre si se envía una notificación push mientras está activa una actividad en vivo? {#what-happens-if-a-push-notification-is-sent-while-a-live-activity-is-active}

![Una pantalla de teléfono con un partido deportivo de los Bulls contra los Bears como actividad en vivo hacia el centro de la pantalla y texto de notificación push lorem ipsum en la parte inferior de la pantalla.]({% image_buster /assets/img/push-vs-live-activities.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

Las actividades en vivo y las notificaciones push ocupan un espacio de pantalla diferente y no entrarán en conflicto en la pantalla del usuario.

#### Si las actividades en vivo aprovechan la funcionalidad de los mensajes push, ¿es necesario habilitar las notificaciones push para recibir actividades en vivo? {#if-live-activities-leverage-push-message-functionality-do-push-notifications-need-to-be-enabled-to-receive-live-activities}

Aunque las actividades en vivo se basan en notificaciones push para las actualizaciones, están controladas por diferentes configuraciones de usuario. Un usuario puede optar por las actividades en vivo pero no por las notificaciones push, y viceversa.

Los tokens de actualización de actividad en vivo caducan a las ocho horas.

#### ¿Las actividades en vivo requieren push primers? {#do-live-activities-require-push-primers}

Los [push primers]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/) son una buena práctica para pedir a tus usuarios que acepten las notificaciones push de tu aplicación. Sin embargo, no hay ninguna indicación del sistema para participar en las actividades en vivo. Por defecto, los usuarios están incluidos en las actividades en vivo para una aplicación individual cuando instalan esa aplicación en iOS 16.1 o posterior. Este permiso puede habilitarse o deshabilitarse en la configuración del dispositivo para cada aplicación.

### Temas técnicos y solución de problemas {#technical-topics-and-troubleshooting}

#### ¿Cómo sé si las actividades en vivo tienen errores? {#how-do-i-know-if-live-activities-has-errors}

Cualquier error de actividad en vivo se registrará en el panel de Braze, en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/), donde puedes filtrar por "LiveActivity Errors".

#### Después de enviar una notificación push-to-start, ¿por qué no he recibido mi actividad en vivo? {#after-sending-a-push-to-start-notification-why-havent-i-received-my-live-activity}

En primer lugar, comprueba que tu carga útil incluye todos los campos obligatorios descritos en el punto de conexión [`messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/). Los campos `activity_attributes` y `content_state` deben coincidir con las propiedades definidas en el código de tu proyecto. Si estás seguro de que la carga útil es correcta, es posible que APNs te esté aplicando un límite de velocidad. Este límite lo impone Apple y no Braze.

Para verificar que tu notificación push-to-start ha llegado correctamente al dispositivo pero no se ha mostrado debido a los límites de velocidad, puedes depurar tu proyecto utilizando la aplicación Consola de tu Mac. Adjunta el proceso de grabación del dispositivo que desees y, a continuación, filtra los registros por `process:liveactivitiesd` en la barra de búsqueda.

#### Después de iniciar mi actividad en vivo con push-to-start, ¿por qué no recibe nuevas actualizaciones? {#after-starting-my-live-activity-with-push-to-start-why-isnt-it-receiving-new-updates}

Comprueba que has seguido correctamente las instrucciones descritas [anteriormente](#swift_brazeActivityAttributes). Tu `ActivityAttributes` debe contener tanto la conformidad con el protocolo `BrazeLiveActivityAttributes` como la propiedad `brazeActivityId`.

Después de recibir una notificación push-to-start de actividad en vivo, comprueba que puedes ver una solicitud de red saliente al punto de conexión `/push_token_tag` de tu URL de Braze y que contiene el ID de actividad correcto en el campo `"tag"`.

Por último, asegúrate de que el tipo de atributo de actividad en vivo en tu carga útil de actualización coincida exactamente con la cadena y la clase utilizadas en tu llamada al método del SDK `registerPushToStart`. Utiliza constantes para evitar errores tipográficos.

#### Recibo una respuesta de acceso denegado cuando intento utilizar el punto de conexión `live_activity/update`. ¿Por qué? {#i-am-receiving-an-access-denied-response-when-i-try-to-use-the-live_activityupdate-endpoint-why}

Las claves de API que utilices deben tener los permisos correctos para acceder a los distintos puntos de conexión de la API de Braze. Si estás utilizando una clave de API que creaste anteriormente, es posible que hayas olvidado actualizar sus permisos. Lee nuestro [resumen de seguridad de la clave de API]({{site.baseurl}}/api/basics/#rest-api-key-security) para refrescarte la memoria.

#### ¿Comparte el punto de conexión `messages/send` límites de velocidad con el punto de conexión `messages/live_activity/update`? {#does-the-messagessend-endpoint-share-rate-limits-with-the-messageslive_activityupdate-endpoint}

De manera predeterminada, el límite de velocidad para el punto de conexión `messages/live_activity/update` es de 250 000 solicitudes por hora, por espacio de trabajo y a través de múltiples puntos de conexión. Para más información, consulta los [límites de velocidad de la API]({{site.baseurl}}/api/api_limits/).