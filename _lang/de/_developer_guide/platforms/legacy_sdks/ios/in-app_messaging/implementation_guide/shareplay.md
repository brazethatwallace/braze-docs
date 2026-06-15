---
nav_title: SharePlay
article_title: SharePlay-Implementierungsleitfaden für In-App-Nachrichten
platform: iOS
page_order: 1
description: "Dieser Leitfaden für die erweiterte SharePlay-Implementierung erweitert den Anwendungsfall Video, der im Leitfaden für die erweiterte Implementierung von In-App-Nachrichten beschrieben ist. SharePlay ist ein neues Feature, das Nutzer:innen von iOS 15 FaceTime ein gemeinsames Medienerlebnis auf ihren Geräten ermöglicht, indem es Audio und Video in Echtzeit synchronisiert."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SharePlay-Implementierungsleitfaden für In-App-Nachrichten {#shareplay-in-app-message-implementation-guide}

> SharePlay ist ein neues Feature, das Nutzer:innen von iOS 15 FaceTime ein gemeinsames Medienerlebnis auf ihren Geräten ermöglicht, indem es Audio und Video in Echtzeit synchronisiert. SharePlay ist eine großartige Möglichkeit für Nutzer:innen, Inhalte mit Freunden und Familie zu erleben. Es bietet Braze-Kund:innen eine zusätzliche Möglichkeit für Video-Inhalte und Gelegenheiten, neue Nutzer:innen in Ihre Anwendung einzuführen.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: style="border:0;margin-top:10px;"}
## Übersicht {#overview}

Das neue Framework `GroupActivities`, das Apple im Rahmen des iOS 15 Updates veröffentlicht hat, erlaubt es Ihnen, FaceTime zu nutzen, indem Sie SharePlay mit Hilfe der In-App-Nachrichten von Braze in Ihre Anwendungen integrieren.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

Wenn Nutzer:innen ein SharePlay-Video in einem FaceTime-Anruf initiieren, erscheint ein „Öffnen“-Button am oberen Rand des Bildschirms aller Teilnehmer:innen. Nach dem Öffnen werden Audio und Video auf allen kompatiblen Geräten synchronisiert, sodass Nutzer:innen gemeinsam Videos in Realtime ansehen können. Diejenigen, die die App nicht heruntergeladen haben, werden zum App Store weitergeleitet.

**Synchrone Medienwiedergabe**<br>
Bei der synchronisierten Medienwiedergabe wird das SharePlay-Video, wenn es von einer Person angehalten wird, auf allen Geräten angehalten. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: style="border:0"}

## Integration

Die In-App-Nachricht, die in dieser Integration verwendet wird, ist ein unterklassifizierter View-Controller für modale In-App-Nachrichten. Eine Anleitung für die Einrichtung finden Sie im [Implementierungsleitfaden]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide/) für erweiterte Anwendungsfälle bei In-App-Nachrichten unter iOS. Stellen Sie vor der Integration sicher, dass Sie die Berechtigung `GroupActivities` zu Ihrem Xcode-Projekt hinzufügen.

{% alert important %}
Wir empfehlen, die [Apple SharePlay-Dokumentation](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) parallel zu dieser Anleitung zu öffnen, um die Integration abzuschließen.
{% endalert %}

### 1. Schritt: Überschreiben und Laden von XIB {#step-1-overriding-and-loading-xib}

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

### 2. Schritt: AVPlayer für In-App-Nachrichten konfigurieren {#step-2-configure-avplayer-for-in-app-messages}

In-App-Nachrichten können mit geringem Entwicklungsaufwand nativ Videos abspielen. Auf diese Weise haben Sie Zugriff auf alle Features von `AVPlayerVideoController`, wie z. B. SharePlay. Die für dieses Beispiel verwendete In-App-Nachricht ist eine Unterklasse von `ABKInAppMessageModalViewController`, die über eine angepasste Ansicht verfügt, um einen nativen Video-Player einzubetten.

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

#### Dashboard-Konfiguration {#dashboard-configuration}

**Schlüssel-Wert-Paare**: Die Videodatei muss in den Schlüssel-Wert-Paaren der In-App-Nachricht angegeben werden und kann nicht an das Medienelement selbst angehängt werden. Sie können auch eine URL-Gültigkeitsprüfung in `beforeInAppMessageDisplayed` als Sicherheitsmechanismus hinzufügen, bevor Sie den Inhalt anzeigen.

**Trigger**: Die In-App-Nachricht sollte für alle Nutzer:innen mit aktivierter erneuter Berechtigung zugänglich sein. Dazu können Sie zwei Trigger festlegen: einen Standard-Trigger, um die Nachricht zu starten, und einen weiteren, um die Nachricht zu starten, wenn sie von SharePlay initiiert wird. Nutzer:innen, die nicht über iOS 15 verfügen, können Nachrichten nur lokal einsehen.

{% alert important %}
Achten Sie auf andere In-App-Nachrichten, die beim Start der Sitzung getriggert werden und miteinander in Konflikt geraten können.
{% endalert %}

### 3. Schritt: Gruppenbeobachtungsaktivität erstellen {#step-3-create-group-watching-activity}

Erstellen Sie ein Objekt, das dem Protokoll `GroupActivity` entspricht. Bei dem Objekt handelt es sich um die Metadaten der `GroupSession`, die während des SharePlay-Lebenszyklus gemeinsam genutzt werden.

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

#### Wiedergabe vorbereiten {#prepare-to-play}

Wenn Sie die Wiedergabe des Medienelements vorbereiten, hat jede Gruppenaktivität drei Zustände von `prepareForActivation()`:
- `.activationDisabled` – einzeln ansehen
- `.activationPreferred` – gemeinsam ansehen
- `.cancelled` – ignorieren und ordnungsgemäß behandeln

Wenn der Status als `activationPreferred` zurückkommt, ist das Ihr Signal, den Rest des Lebenszyklus der Gruppenaktivität zu aktivieren.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: style="border:0;"}

### 4. Schritt: In-App-Nachricht über die SharePlay-API starten {#step-4-launch-in-app-message-from-shareplay-api}

Die `GroupActivities`-API ermittelt, ob ein Video vorhanden ist. Wenn ja, sollten Sie das angepasste Event triggern, um Ihre SharePlay-fähige In-App-Nachricht zu starten. Der `CoordinationManager` ist für die Zustandsänderungen von SharePlay verantwortlich, z. B. wenn Nutzer:innen den Anruf verlassen oder ihm beitreten.

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

### 5. Schritt: Gruppensitzung beim Verwerfen der In-App-Nachricht verlassen {#step-5-leaving-a-group-session-on-in-app-message-dismissal}

Wenn die In-App-Nachricht verworfen wird, ist ein geeigneter Zeitpunkt, um die SharePlay-Sitzung zu verlassen und das Sitzungsobjekt zu verwerfen.

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

### Sichtbarkeit des SharePlay-Buttons konfigurieren {#configure-shareplay-button-visibility}

Es empfiehlt sich, jeden SharePlay-Indikator dynamisch aus- oder einzublenden. Verwenden Sie die Variable `isEligibleForGroupSession`, um festzustellen, ob die Nutzer:innen gerade ein FaceTime-Gespräch führen oder nicht. Wenn ja, sollte ein Button sichtbar sein, mit dem das Video für alle kompatiblen Geräte im Chat geteilt werden kann. Wenn Nutzer:innen zum ersten Mal SharePlay starten, erscheint auf dem ursprünglichen Gerät eine Aufforderung zur Auswahl der Optionen. Auf den Geräten der eingeladenen Nutzer:innen erscheint dann eine Aufforderung, sich mit dem Inhalt zu beschäftigen.

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