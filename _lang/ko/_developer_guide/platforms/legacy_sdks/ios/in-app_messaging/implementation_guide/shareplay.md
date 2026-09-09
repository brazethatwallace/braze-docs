---
nav_title: SharePlay
article_title: SharePlay 인앱 메시지 구현 가이드
platform: iOS
page_order: 1
description: "이 고급 SharePlay 구현 가이드는 인앱 메시지 고급 구현 가이드에서 제공된 비디오 사용 사례를 확장합니다. SharePlay는 iOS 15 FaceTime 사용자가 여러 기기에서 미디어를 공유할 수 있는 새로 출시된 기능으로, 실시간 오디오 및 비디오 동기화를 제공합니다."
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SharePlay 인앱 메시지 구현 가이드 {#shareplay-in-app-message-implementation-guide}

> SharePlay는 iOS 15 FaceTime 사용자가 여러 기기에서 미디어를 공유할 수 있는 새로 출시된 기능으로, 실시간 오디오 및 비디오 동기화를 제공합니다. SharePlay는 사용자가 친구 및 가족과 함께 콘텐츠를 경험할 수 있는 좋은 방법으로, Braze 고객에게 비디오 콘텐츠를 위한 추가적인 경로와 신규 사용자를 애플리케이션에 소개할 수 있는 기회를 제공합니다.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: width="4719" height="2501" style="border:0;margin-top:10px;"}

## 개요 {#overview}

Apple이 iOS 15 업데이트의 일환으로 출시한 새로운 `GroupActivities` 프레임워크를 사용하면 Braze 인앱 메시지의 도움을 받아 SharePlay를 애플리케이션에 통합하여 FaceTime을 활용할 수 있습니다.
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: width="924" height="550" style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

사용자가 FaceTime 통화에서 SharePlay 비디오를 시작하면 모든 참여자의 화면 상단에 "열기" 버튼이 나타납니다. 이 버튼을 누르면 호환되는 모든 기기에서 오디오와 비디오가 동기화되어 사용자들이 실시간으로 함께 비디오를 시청할 수 있습니다. 앱을 다운로드하지 않은 사람은 앱 스토어로 리디렉션됩니다.

**동기화된 미디어 재생**<br>
동기화된 미디어 재생 기능을 사용하면 한 사람이 SharePlay 비디오를 일시 정지하면 모든 기기에서 일시 정지됩니다. <br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: width="3770" height="1408" style="border:0"}

## 통합 {#integration}

이 통합에서 사용되는 인앱 메시지는 서브클래싱된 Modal 인앱 메시지 뷰 컨트롤러입니다. 설정 가이드는 iOS 인앱 메시지 고급 사용 사례 [구현 가이드]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide)에서 확인할 수 있습니다. 통합하기 전에 Xcode 프로젝트에 `GroupActivities` 권한을 추가해야 합니다.

{% alert important %}
통합을 완료하려면 이 가이드와 함께 [Apple SharePlay 설명서](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback)를 나란히 열어두는 것을 권장합니다.
{% endalert %}

### 1단계: XIB 오버라이드 및 로드 {#step-1-overriding-and-loading-xib}

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

### 2단계: 인앱 메시지용 AVPlayer 구성 {#step-2-configure-avplayer-for-in-app-messages}

인앱 메시지는 간단한 개발자 작업만으로 네이티브 비디오 재생이 가능합니다. 이를 통해 SharePlay를 포함한 모든 `AVPlayerVideoController` 기능에 접근할 수 있습니다. 이 예제에서 사용되는 인앱 메시지는 네이티브 비디오 플레이어를 삽입하기 위한 커스텀 뷰가 있는 서브클래싱된 `ABKInAppMessageModalViewController`입니다.

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

#### 대시보드 구성 {#dashboard-configuration}

**키-값 페어**: 비디오 파일은 인앱 메시지의 키-값 페어에서 설정해야 하며, 미디어 항목 자체에 첨부할 수 없습니다. 또한 콘텐츠를 표시하기 전에 `beforeInAppMessageDisplayed`에서 URL 유효성 검사를 추가하여 안전 장치로 활용할 수 있습니다.

**트리거**: 인앱 메시지는 재적격 기능이 활성화된 상태로 모든 사용자에게 표시되도록 설정해야 합니다. 이를 위해 두 개의 트리거를 설정합니다. 하나는 메시지를 실행하기 위한 기본 트리거이고, 다른 하나는 SharePlay에서 시작될 때 메시지를 실행하기 위한 트리거입니다. iOS 15를 사용하지 않는 사용자는 로컬에서만 메시지를 볼 수 있습니다.

{% alert important %}
세션 시작 시 트리거되는 다른 인앱 메시지와 충돌할 수 있으므로 주의하세요.
{% endalert %}

### 3단계: 그룹 시청 활동 생성 {#step-3-create-group-watching-activity}

`GroupActivity` 프로토콜을 준수하는 객체를 생성합니다. 이 객체는 SharePlay 생명주기 동안 공유되는 `GroupSession`의 메타데이터가 됩니다.

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

#### 재생 준비 {#prepare-to-play}

미디어 항목 재생을 준비할 때 각 그룹 활동에는 `prepareForActivation()`의 세 가지 상태가 있습니다:
- `.activationDisabled` - 개별 시청
- `.activationPreferred` - 함께 시청
- `.cancelled` - 무시하고 우아하게 처리

상태가 `activationPreferred`로 반환되면 나머지 그룹 활동 생명주기를 활성화할 차례입니다.

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: width="3816" height="1408" style="border:0;"}

### 4단계: SharePlay API에서 인앱 메시지 실행 {#step-4-launch-in-app-message-from-shareplay-api}

`GroupActivities` API는 비디오가 있는지 확인합니다. 비디오가 있으면 SharePlay 지원 인앱 메시지를 실행하기 위한 커스텀 이벤트를 트리거해야 합니다. `CoordinationManager`는 사용자가 통화를 나가거나 참여하는 등 SharePlay의 상태 변경을 담당합니다.

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

### 5단계: 인앱 메시지 닫기 시 그룹 세션 나가기 {#step-5-leaving-a-group-session-on-in-app-message-dismissal}

인앱 메시지가 닫힐 때가 SharePlay 세션을 나가고 세션 객체를 폐기하기에 적절한 시점입니다.

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

### SharePlay 버튼 가시성 구성 {#configure-shareplay-button-visibility}

SharePlay 표시기를 동적으로 숨기거나 표시하는 것이 모범 사례입니다. `isEligibleForGroupSession` 변수를 사용하여 사용자가 현재 FaceTime 통화 중인지 확인합니다. FaceTime 통화 중인 경우 채팅의 호환 기기 간에 비디오를 공유할 수 있는 버튼이 표시되어야 합니다. 사용자가 처음 SharePlay를 시작하면 원래 기기에 옵션을 선택하라는 프롬프트가 나타납니다. 이후 공유 대상 사용자의 기기에 콘텐츠에 참여하라는 프롬프트가 나타납니다.

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