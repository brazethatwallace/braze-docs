---
nav_title: SharePlay
article_title: Guía de implementación de mensajes dentro de la aplicación SharePlay
platform: iOS
page_order: 1
description: "Esta guía de implementación avanzada de SharePlay amplía el caso de uso de video proporcionado en la guía de implementación avanzada de mensajes dentro de la aplicación. SharePlay es una característica recién lanzada que habilita a los usuarios de FaceTime de iOS 15 a tener una experiencia multimedia compartida en todos sus dispositivos, ofreciendo sincronización de audio y video en tiempo real."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guía de implementación de mensajes dentro de la aplicación SharePlay {#shareplay-in-app-message-implementation-guide}

> SharePlay es una característica recién lanzada que habilita a los usuarios de FaceTime de iOS 15 a tener una experiencia multimedia compartida en todos sus dispositivos, ofreciendo sincronización de audio y video en tiempo real. SharePlay es una forma estupenda de que los usuarios experimenten el contenido con amigos y familiares, ofreciendo a los clientes de Braze una vía adicional para el contenido de video y oportunidades para presentar tu aplicación a nuevos usuarios.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: style="border:0;margin-top:10px;"}

## Resumen {#overview}

El nuevo framework `GroupActivities` lanzado por Apple como parte de la actualización de iOS 15 te permite aprovechar FaceTime integrando SharePlay en tus aplicaciones con la ayuda de los mensajes dentro de la aplicación de Braze.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: width="924" height="550" style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

Cuando los usuarios inician un video de SharePlay en una llamada de FaceTime, aparece un botón "Abrir" en la parte superior de la pantalla de todos. Al abrirlo, el audio y el video se sincronizan en todos los dispositivos compatibles, lo que permite a los usuarios ver videos juntos en tiempo real. Quienes no tengan la aplicación descargada son redirigidos a la App Store.

**Reproducción de medios sincronizada**<br>
Con la reproducción de medios sincronizada, si una persona pausa el video de SharePlay, se pausará en todos los dispositivos. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: width="3770" height="1408" style="border:0"}

## Integración {#integration}

El mensaje dentro de la aplicación utilizado en esta integración es un controlador de vista de mensaje dentro de la aplicación modal subclasificado. Puedes encontrar una guía de configuración en la [guía de implementación]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide) de casos de uso avanzados de mensajes dentro de la aplicación de iOS. Antes de integrar, asegúrate de agregar la autorización `GroupActivities` a tu proyecto Xcode.

{% alert important %}
Recomendamos abrir la [documentación de Apple SharePlay](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) junto con esta guía para completar la integración.
{% endalert %}

### Paso 1: Sobrescribir y cargar XIB {#step-1-overriding-and-loading-xib}

{% tabs %}
{% tab Swift %}
```swift
override var nibName: String {
  return "ModalVideoViewController"
}

/// Overriding loadView() from ABKInAppMessageModalViewController to provide our own view for the in-app message
override func loadView() {
  Bundle.main.loadNibNamed(nibName, owner: self, options: nil)
}
```
{% endtab %}
{% endtabs %}

### Paso 2: Configurar AVPlayer para mensajes dentro de la aplicación {#step-2-configure-avplayer-for-in-app-messages}

Los mensajes dentro de la aplicación pueden reproducir videos de forma nativa con algo de trabajo ligero del desarrollador. Al hacer esto, tienes acceso a todas las características de `AVPlayerVideoController`, como SharePlay. El mensaje dentro de la aplicación utilizado en este ejemplo es un `ABKInAppMessageModalViewController` subclasificado que tiene una vista personalizada para incrustar un reproductor de video nativo.

{% tabs %}
{% tab Swift %}
```swift
func configureVideoPlayer() {
  guard let urlString = inAppMessage.extras?["video_url"] as? String,
        let url = URL(string: urlString) else { return }

  let videoTitle = inAppMessage.extras?["video_title"] as? String
  mediaItem = MediaItem(title: videoTitle ?? "Video Content", url: url)

  let asset = AVAsset(url: url)
  let playerItem = AVPlayerItem(asset: asset)
  player.replaceCurrentItem(with: playerItem)
  playerViewController.player = player

  addChild(playerViewController)
  videoPlayerContainer.addSubview(playerViewController.view)
  playerViewController.didMove(toParent: self)
}
```
{% endtab %}
{% endtabs %}

#### Configuración del panel {#dashboard-configuration}

**Pares clave-valor**: El archivo de video debe configurarse en los pares clave-valor del mensaje dentro de la aplicación y no puede adjuntarse al elemento multimedia en sí. También puedes agregar una verificación de validez de URL en `beforeInAppMessageDisplayed` como medida de seguridad antes de mostrar el contenido.

**Desencadenamiento**: El mensaje dentro de la aplicación debe ser elegible para todos los usuarios con la reelegibilidad habilitada. Esto se puede hacer configurando dos desencadenadores, uno predeterminado para lanzar el mensaje y otro para lanzar el mensaje cuando se inicia desde SharePlay. Los usuarios que no estén en iOS 15 solo podrán ver los mensajes de forma local.

{% alert important %}
Ten en cuenta cualquier otro mensaje dentro de la aplicación desencadenado al inicio de sesión que pueda entrar en conflicto entre sí.
{% endalert %}

### Paso 3: Crear actividad de visualización grupal {#step-3-create-group-watching-activity}

Crea un objeto que se ajuste al protocolo `GroupActivity`. El objeto será los metadatos del `GroupSession` compartido durante todo el ciclo de vida de SharePlay.

{% tabs %}
{% tab Swift %}
```swift
struct MediaItem: Hashable, Codable {
  let title: String
  let url: URL
}

@available(iOS 15, *)
struct MediaItemActivity: GroupActivity {
  static let activityIdentifier = "com.book-demo.GroupWatching"

  let mediaItem: MediaItem

  var metadata: GroupActivityMetadata {
    var metadata = GroupActivityMetadata()
    metadata.type = .watchTogether
    metadata.title = mediaItem.title
    metadata.fallbackURL = mediaItem.url
    return metadata
  }
}
```
{% endtab %}
{% endtabs %}

#### Prepararse para reproducir {#prepare-to-play}

Cuando te preparas para reproducir el elemento multimedia, cada actividad grupal tiene tres estados de `prepareForActivation()`:
- `.activationDisabled` - visualización individual
- `.activationPreferred` - visualización en conjunto
- `.cancelled` - ignorar y manejar con gracia

Cuando el estado regresa como `activationPreferred`, esa es tu señal para activar el resto del ciclo de vida de la actividad grupal.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: width="3816" height="1408" style="border:0;"}

### Paso 4: Lanzar mensaje dentro de la aplicación desde la API de SharePlay {#step-4-launch-in-app-message-from-shareplay-api}

La API `GroupActivities` determina si hay un video presente. Si es así, deberías desencadenar el evento personalizado para lanzar tu mensaje dentro de la aplicación compatible con SharePlay. El `CoordinationManager` es responsable de los cambios de estado de SharePlay, como cuando los usuarios abandonan o se unen a la llamada.

{% tabs %}
{% tab Swift %}
```swift
private var subscriptions = Set<AnyCancellable>()
private var selectedMediaItem: MediaItem? {
  didSet {
    // Ensure the UI selection always represents the currently playing media.
    guard let _ = selectedMediaItem else { return }

    if !BrazeManager.shared.inAppMessageCurrentlyVisible {
      BrazeManager.shared.logCustomEvent("SharePlay Event")
    }
  }
}

private func launchVideoPlayerIfNecessary() {
  CoordinationManager.shared.$enqueuedMediaItem
      .receive(on: DispatchQueue.main)
      .compactMap { $0 }
      .assign(to: \.selectedMediaItem, on: self)
      .store(in: &subscriptions)
}
```
{% endtab %}
{% endtabs %}

### Paso 5: Abandonar una sesión grupal al cerrar el mensaje dentro de la aplicación {#step-5-leaving-a-group-session-on-in-app-message-dismissal}

Cuando se cierra el mensaje dentro de la aplicación, es un momento apropiado para abandonar la sesión de SharePlay y descartar el objeto de sesión.

{% tabs %}
{% tab Swift %}
```swift
override func viewDidDisappear(_ animated: Bool) {
  super.viewDidDisappear(animated)
  groupSession?.leave()
  CoordinationManager.shared.leave()
}

class CoordinationManager() {
...
  // Published values that the player, and other UI items, observe.
  @Published var enqueuedMediaItem: MediaItem?
  @Published var groupSession: GroupSession<MediaItemActivity>?

  // Clear activity when the user leaves
  func leave() {
    groupSession = nil
    enqueuedMediaItem = nil
  }
...
}
```
{% endtab %}
{% endtabs %}

### Configurar la visibilidad del botón de SharePlay {#configure-shareplay-button-visibility}

Es una buena práctica ocultar o mostrar dinámicamente cualquier indicador de SharePlay. Usa la variable `isEligibleForGroupSession` para observar si el usuario se encuentra actualmente en una llamada de FaceTime o no. Si está en una llamada de FaceTime, debería mostrarse un botón para compartir el video en los dispositivos compatibles del chat. La primera vez que el usuario inicia SharePlay, aparecerá un aviso en el dispositivo original para seleccionar las opciones. Un aviso posterior aparecerá entonces en los dispositivos de los usuarios compartidos para interactuar con el contenido.

{% tabs %}
{% tab Swift %}
```swift
private var isEligibleForSharePlay: Bool = false {
  didSet {
    sharePlayButton.isHidden = !isEligibleForSharePlay
  }
}

override func viewDidLoad() {
  super.viewDidLoad()

  // SharePlay button eligibility
  groupStateObserver.$isEligibleForGroupSession
    .receive(on: DispatchQueue.main)
    .assign(to: \.isEligibleForSharePlay, on: self)
    .store(in: &subscriptions)
}
```
{% endtab %}
{% endtabs %}