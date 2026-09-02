---
nav_title: Shareplay
article_title: Guia de implementação de mensagens no app com SharePlay
platform: iOS
page_order: 1
description: "Este guia avançado de implementação do SharePlay expande o caso de uso de vídeo apresentado no guia avançado de implementação de mensagens no app. O SharePlay é um recurso recém-lançado que permite aos usuários do FaceTime no iOS 15 ter uma experiência de mídia compartilhada entre seus dispositivos, oferecendo sincronização de áudio e vídeo em tempo real."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guia de implementação de mensagem no app do SharePlay {#shareplay-in-app-message-implementation-guide}

> O SharePlay é um recurso recém-lançado que permite aos usuários do FaceTime no iOS 15 ter uma experiência de mídia compartilhada entre seus dispositivos, oferecendo sincronização de áudio e vídeo em tempo real. O SharePlay é uma ótima maneira para os usuários experimentarem conteúdo com amigos e familiares, oferecendo aos clientes da Braze uma via adicional para conteúdo de vídeo e oportunidades para apresentar novos usuários ao seu aplicativo.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: width="4719" height="2501" style="border:0;margin-top:10px;"}

## Visão geral {#overview}

O novo framework `GroupActivities` lançado pela Apple como parte da atualização do iOS 15 permite que você aproveite o FaceTime integrando o SharePlay aos seus aplicativos com a ajuda das In-App Messages da Braze.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: width="924" height="550" style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

Quando os usuários iniciam um vídeo do SharePlay em uma chamada do FaceTime, um botão "Abrir" aparece na parte superior da tela de todos. Quando aberto, o áudio e o vídeo são sincronizados em todos os dispositivos compatíveis, permitindo que os usuários assistam a vídeos juntos em tempo real. Aqueles que não têm o app instalado são redirecionados para a App Store.

**Reprodução de mídia sincronizada**<br>
Com a reprodução de mídia sincronizada, se uma pessoa pausar o vídeo do SharePlay, ele será pausado em todos os dispositivos. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: width="3770" height="1408" style="border:0"}

## Integração {#integration}

A mensagem no app usada nesta integração é um controlador de visualização de mensagem no app modal com subclasse. Um guia de configuração pode ser encontrado no [guia de implementação]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide) de casos de uso avançados de mensagens no app do iOS. Antes de integrar, certifique-se de adicionar o entitlement `GroupActivities` ao seu projeto Xcode.

{% alert important %}
Recomendamos abrir a [documentação do Apple SharePlay](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) lado a lado com este guia para concluir a integração.
{% endalert %}

### Etapa 1: Sobrescrever e carregar o XIB {#step-1-overriding-and-loading-xib}

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

### Etapa 2: Configurar o AVPlayer para mensagens no app {#step-2-configure-avplayer-for-in-app-messages}

As mensagens no app podem reproduzir vídeos nativamente com um trabalho leve de desenvolvimento. Ao fazer isso, você tem acesso a todos os recursos do `AVPlayerVideoController`, como o SharePlay. A mensagem no app usada neste exemplo é um `ABKInAppMessageModalViewController` com subclasse que possui uma visualização personalizada para incorporar um player de vídeo nativo.

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

#### Configuração do dashboard {#dashboard-configuration}

**Pares chave-valor**: O arquivo de vídeo deve ser definido nos pares chave-valor da mensagem no app e não pode ser anexado ao item de mídia em si. Você também pode adicionar verificação de validade de URL em `beforeInAppMessageDisplayed` como uma proteção antes de exibir o conteúdo.

**Disparo**: A mensagem no app deve ser elegível para todos os usuários com reelegibilidade ativada. Isso pode ser feito definindo dois disparadores: um disparador padrão para lançar a mensagem e outro para lançá-la quando iniciada pelo SharePlay. Usuários que não estiverem no iOS 15 só poderão visualizar as mensagens localmente.

{% alert important %}
Tenha cuidado com outras mensagens no app disparadas no início da sessão que possam entrar em conflito entre si.
{% endalert %}

### Etapa 3: Criar atividade de visualização em grupo {#step-3-create-group-watching-activity}

Crie um objeto que esteja em conformidade com o protocolo `GroupActivity`. O objeto será os metadados da `GroupSession` compartilhados ao longo do ciclo de vida do SharePlay.

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

#### Preparar para reprodução {#prepare-to-play}

Quando você se prepara para reproduzir o item de mídia, cada atividade de grupo tem três estados de `prepareForActivation()`:
- `.activationDisabled` - visualização individual
- `.activationPreferred` - visualização conjunta
- `.cancelled` - ignorar e tratar de forma adequada

Quando o estado retorna como `activationPreferred`, esse é o sinal para ativar o restante do ciclo de vida da atividade de grupo.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: width="3816" height="1408" style="border:0;"}

### Etapa 4: Iniciar mensagem no app a partir da API or interface de programação do aplicativo (API) do SharePlay {#step-4-launch-in-app-message-from-shareplay-api}

A API or interface de programação do aplicativo (API) `GroupActivities` determina se há um vídeo presente. Se houver, você deve disparar o evento personalizado para lançar sua mensagem no app compatível com SharePlay. O `CoordinationManager` é responsável pelas mudanças de estado do SharePlay, como quando o(s) usuário(s) sai(em) ou entra(m) na chamada.

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

### Etapa 5: Sair de uma sessão de grupo ao dispensar a mensagem no app {#step-5-leaving-a-group-session-on-in-app-message-dismissal}

Quando a mensagem no app é dispensada, é o momento apropriado para sair da sessão do SharePlay e descartar o objeto de sessão.

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

### Configurar visibilidade do botão SharePlay {#configure-shareplay-button-visibility}

A melhor prática é ocultar ou exibir dinamicamente qualquer indicador do SharePlay. Use a variável `isEligibleForGroupSession` para observar se o usuário está atualmente em uma chamada do FaceTime ou não. Se ele estiver em uma chamada do FaceTime, um botão deve ficar visível para compartilhar o vídeo entre os dispositivos compatíveis no chat. Na primeira vez que o usuário inicia o SharePlay, um prompt aparecerá no dispositivo original para selecionar as opções. Um prompt subsequente aparecerá nos dispositivos dos usuários compartilhados para interagir com o conteúdo.

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