---
nav_title: SharePlay
article_title: Guide de déploiement des messages in-app SharePlay
platform: iOS
page_order: 1
description: "Ce guide de déploiement avancé de SharePlay développe le cas d'usage vidéo fourni dans le guide de déploiement avancé des messages in-app. SharePlay est une fonctionnalité qui permet aux utilisateurs iOS 15 FaceTime de bénéficier d'une expérience multimédia partagée sur leurs appareils, offrant une synchronisation audio et vidéo en temps réel."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guide de déploiement des messages in-app SharePlay {#shareplay-in-app-message-implementation-guide}

> SharePlay est une fonctionnalité qui permet aux utilisateurs iOS 15 FaceTime de bénéficier d'une expérience multimédia partagée sur leurs appareils, offrant une synchronisation audio et vidéo en temps réel. SharePlay est un excellent moyen pour les utilisateurs de partager du contenu avec leurs amis et leur famille, offrant aux clients Braze une possibilité supplémentaire pour le contenu vidéo et des opportunités de présenter votre application à de nouveaux utilisateurs.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: width="4719" height="2501" style="border:0;margin-top:10px;"}

## Aperçu {#overview}

Le nouveau framework `GroupActivities` publié par Apple dans le cadre de la mise à jour iOS 15 vous permet de tirer parti de FaceTime en intégrant SharePlay dans vos applications à l'aide des messages in-app de Braze.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: width="924" height="550" style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

Lorsque les utilisateurs lancent une vidéo SharePlay lors d'un appel FaceTime, un bouton « Ouvrir » apparaît en haut de l'écran de chaque participant. Une fois ouvert, l'audio et la vidéo se synchronisent sur tous les appareils compatibles, permettant aux utilisateurs de regarder des vidéos ensemble en temps réel. Ceux qui n'ont pas téléchargé l'application sont redirigés vers la boutique d'applications.

**Lecture multimédia synchronisée**<br>
Avec la lecture multimédia synchronisée, si une personne met en pause la vidéo SharePlay, celle-ci sera mise en pause sur tous les appareils. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: width="3770" height="1408" style="border:0"}

## Intégration {#integration}

Le message in-app utilisé dans cette intégration est un contrôleur de vue de message in-app modal sous-classé. Un guide de configuration est disponible dans le [guide de déploiement]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide) des cas d'usage avancés des messages in-app iOS. Avant de procéder à l'intégration, assurez-vous d'ajouter l'autorisation `GroupActivities` à votre projet Xcode.

{% alert important %}
Nous vous recommandons d'ouvrir la [documentation Apple SharePlay](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) côte à côte avec ce guide pour réaliser l'intégration.
{% endalert %}

### Étape 1 : Surcharger et charger le XIB {#step-1-overriding-and-loading-xib}

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

### Étape 2 : Configurer AVPlayer pour les messages in-app {#step-2-configure-avplayer-for-in-app-messages}

Les messages in-app peuvent lire des vidéos nativement avec un travail de développement léger. Cela vous donne accès à toutes les fonctionnalités d'`AVPlayerVideoController`, comme SharePlay. Le message in-app utilisé dans cet exemple est un `ABKInAppMessageModalViewController` sous-classé qui dispose d'une vue personnalisée pour intégrer un lecteur vidéo natif.

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

#### Configuration du tableau de bord {#dashboard-configuration}

**Paires clé-valeur** : Le fichier vidéo doit être défini dans les paires clé-valeur du message in-app et ne peut pas être rattaché directement à l'élément multimédia. Vous pouvez également ajouter une vérification de validité d'URL dans `beforeInAppMessageDisplayed` comme garde-fou avant d'afficher le contenu.

**Déclenchement** : Le message in-app doit être éligible pour tous les utilisateurs avec la rééligibilité activée. Pour cela, définissez deux déclencheurs : un déclencheur par défaut pour lancer le message, et un autre pour le lancer lorsqu'il est initié depuis SharePlay. Les utilisateurs qui ne sont pas sur iOS 15 ne pourront voir les messages que localement.

{% alert important %}
Faites attention à tout autre message in-app déclenché au démarrage de la session qui pourrait entrer en conflit.
{% endalert %}

### Étape 3 : Créer une activité de visionnage en groupe {#step-3-create-group-watching-activity}

Créez un objet conforme au protocole `GroupActivity`. Cet objet contiendra les métadonnées de la `GroupSession` partagées tout au long du cycle de vie de SharePlay.

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

#### Préparer la lecture {#prepare-to-play}

Lorsque vous préparez la lecture de l'élément multimédia, chaque activité de groupe possède trois états de `prepareForActivation()` :
- `.activationDisabled` – visionnage individuel
- `.activationPreferred` – visionnage ensemble
- `.cancelled` – ignorer et gérer proprement

Lorsque l'état retourné est `activationPreferred`, c'est le signal pour activer le reste du cycle de vie de l'activité de groupe.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: width="3816" height="1408" style="border:0;"}

### Étape 4 : Lancer le message in-app depuis l'API SharePlay {#step-4-launch-in-app-message-from-shareplay-api}

L'API `GroupActivities` détermine si une vidéo est présente. Si c'est le cas, vous devez déclencher l'événement personnalisé pour lancer votre message in-app compatible SharePlay. Le `CoordinationManager` est responsable des changements d'état de SharePlay, par exemple lorsque le ou les utilisateurs quittent ou rejoignent l'appel.

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

### Étape 5 : Quitter une session de groupe lors de la fermeture du message in-app {#step-5-leaving-a-group-session-on-in-app-message-dismissal}

La fermeture du message in-app est le moment approprié pour quitter la session SharePlay et supprimer l'objet de session.

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

### Configurer la visibilité du bouton SharePlay {#configure-shareplay-button-visibility}

Il est recommandé de masquer ou d'afficher dynamiquement tout indicateur SharePlay. Utilisez la variable `isEligibleForGroupSession` pour observer si l'utilisateur est actuellement en appel FaceTime ou non. S'il est en appel FaceTime, un bouton doit être visible pour partager la vidéo sur les appareils compatibles dans la conversation. La première fois que l'utilisateur lance SharePlay, une invite apparaîtra sur l'appareil d'origine pour sélectionner les options. Une invite ultérieure apparaîtra ensuite sur les appareils des autres utilisateurs pour interagir avec le contenu.

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