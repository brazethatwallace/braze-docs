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

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: width="4719" height="2501" style="border:0;margin-top:10px;"}

## Übersicht {#overview}

Das neue `GroupActivities`-Framework, das Apple als Teil des iOS-15-Updates veröffentlicht hat, ermöglicht es Ihnen, FaceTime zu nutzen, indem Sie SharePlay mithilfe von Braze In-App Messages in Ihre Anwendungen integrieren.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: width="924" height="550" style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

Wenn Nutzer:innen ein SharePlay-Video in einem FaceTime-Anruf starten, erscheint oben auf dem Bildschirm aller Teilnehmenden ein „Öffnen“-Button. Nach dem Öffnen werden Audio und Video auf allen kompatiblen Geräten synchronisiert, sodass Nutzer:innen Videos gemeinsam in Realtime ansehen können. Nutzer:innen, die die App nicht installiert haben, werden zum App Store weitergeleitet.

**Synchronisierte Medienwiedergabe**<br>
Bei synchronisierter Medienwiedergabe wird das SharePlay-Video auf allen Geräten pausiert, wenn eine Person es pausiert. <br><br>
![Synchronisierte Medienwiedergabe mit SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: width="3770" height="1408" style="border:0"}

## Integration {#integration}

Die In-App-Nachricht, die in dieser Integration verwendet wird, ist ein unterklassifizierter modaler In-App-Nachrichten-View-Controller. Eine Anleitung zur Einrichtung finden Sie im [Implementierungsleitfaden]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide) für erweiterte Anwendungsfälle von iOS-In-App-Nachrichten. Stellen Sie vor der Integration sicher, dass Sie die `GroupActivities`-Berechtigung zu Ihrem Xcode-Projekt hinzufügen.

{% alert important %}
Wir empfehlen, die [Apple SharePlay-Dokumentation](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback) parallel zu diesem Leitfaden geöffnet zu haben, um die Integration abzuschließen.
{% endalert %}

### Schritt 1: XIB überschreiben und laden {#step-1-overriding-and-loading-xib}

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

### Schritt 2: AVPlayer für In-App-Nachrichten konfigurieren {#step-2-configure-avplayer-for-in-app-messages}

In-App-Nachrichten können Videos nativ abspielen – mit nur geringem Entwicklungsaufwand. Dadurch haben Sie Zugriff auf alle Features des `AVPlayerVideoController`, wie zum Beispiel SharePlay. Die In-App-Nachricht in diesem Beispiel ist ein unterklassifizierter `ABKInAppMessageModalViewController` mit einer angepassten Ansicht, in die ein nativer Videoplayer eingebettet ist.

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

**Schlüssel-Wert-Paare**: Die Videodatei muss in den Schlüssel-Wert-Paaren der In-App-Nachricht festgelegt werden und kann nicht direkt an das Medienelement angehängt werden. Sie können auch eine URL-Gültigkeitsprüfung in `beforeInAppMessageDisplayed` als Sicherheitsmechanismus hinzufügen, bevor der Inhalt angezeigt wird.

**Trigger or triggern or triggern**: Die In-App-Nachricht sollte für alle Nutzer:innen mit aktivierter erneuter Berechtigung verfügbar sein. Dies kann durch Festlegen von zwei Trigger or triggern or triggern erreicht werden: ein Standard-Trigger or triggern zum Starten der Nachricht und ein weiterer zum Starten der Nachricht, wenn sie über SharePlay initiiert wird. Nutzer:innen, die nicht iOS 15 verwenden, können Nachrichten nur lokal anzeigen.

{% alert important %}
Achten Sie auf andere In-App-Nachrichten, die beim Sitzungsstart getriggert werden und miteinander in Konflikt geraten könnten.
{% endalert %}

### Schritt 3: Gemeinsame Wiedergabe-Aktivität erstellen {#step-3-create-group-watching-activity}

Erstellen Sie ein Objekt, das dem `GroupActivity`-Protokoll entspricht. Das Objekt enthält die Metadaten der `GroupSession`, die während des gesamten SharePlay-Lebenszyklus geteilt werden.

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
- `.activationDisabled` – individuelle Wiedergabe
- `.activationPreferred` – gemeinsame Wiedergabe
- `.cancelled` – ignorieren und elegant behandeln

Wenn der Zustand als `activationPreferred` zurückkommt, ist das Ihr Signal, den restlichen Lebenszyklus der Gruppenaktivität zu aktivieren.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: width="3816" height="1408" style="border:0;"}

### Schritt 4: In-App-Nachricht über die SharePlay-API starten {#step-4-launch-in-app-message-from-shareplay-api}

Die `GroupActivities`-API prüft, ob ein Video vorhanden ist. Falls ja, sollten Sie das angepasste Event Trigger or triggern or triggern, um Ihre SharePlay-fähige In-App-Nachricht zu starten. Der `CoordinationManager` ist für die Zustandsänderungen von SharePlay verantwortlich, zum Beispiel wenn Nutzer:innen den Anruf verlassen oder ihm beitreten.

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

### Schritt 5: Gruppensitzung beim Schließen der In-App-Nachricht verlassen {#step-5-leaving-a-group-session-on-in-app-message-dismissal}

Wenn die In-App-Nachricht geschlossen wird, ist ein geeigneter Zeitpunkt, um die SharePlay-Sitzung zu verlassen und das Sitzungsobjekt zu verwerfen.

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

Es ist Best Practice, jeglichen SharePlay-Indikator dynamisch ein- oder auszublenden. Verwenden Sie die Variable `isEligibleForGroupSession`, um zu beobachten, ob sich die Nutzer:innen aktuell in einem FaceTime-Anruf befinden oder nicht. Falls sie sich in einem FaceTime-Anruf befinden, sollte ein Button sichtbar sein, um das Video auf den kompatiblen Geräten im Chat zu teilen. Wenn Nutzer:innen SharePlay zum ersten Mal initiieren, erscheint eine Aufforderung auf dem Ursprungsgerät, um die Optionen auszuwählen. Anschließend erscheint eine weitere Aufforderung auf den Geräten der anderen Nutzer:innen, um mit dem Inhalt zu interagieren.

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