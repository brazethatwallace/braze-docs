---
nav_title: SharePlay
article_title: SharePlay アプリ内メッセージ実装ガイド
platform: iOS
page_order: 1
description: "この高度なSharePlay実装ガイドは、アプリ内メッセージの高度な実装ガイドで提供される動画のユースケースを拡張したものです。SharePlayは、iOS 15 FaceTimeユーザーがデバイス間で共有メディア体験を実現し、リアルタイムでオーディオと動画を同期できる新機能です。"
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SharePlay アプリ内メッセージ実装ガイド {#shareplay-in-app-message-implementation-guide}

> SharePlayは、iOS 15 FaceTimeユーザーがデバイス間で共有メディア体験を実現し、リアルタイムでオーディオと動画を同期できる新機能です。SharePlayは、ユーザーが友人や家族と一緒にコンテンツを体験できる優れた方法であり、Brazeの顧客に動画コンテンツのための新たな手段を提供し、アプリケーションを新しいユーザーに紹介する機会を提供します。

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: width="4719" height="2501" style="border:0;margin-top:10px;"}

## 概要 {#overview}

Appleが iOS 15 アップデートの一部としてリリースした新しい`GroupActivities`フレームワークにより、Brazeのアプリ内メッセージを活用してSharePlayをアプリケーションに統合し、FaceTimeを活用できます。
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: width="924" height="550" style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

ユーザーがFaceTime通話中にSharePlay動画を開始すると、全員の画面上部に「Open」ボタンが表示されます。開くと、すべての対応デバイスでオーディオとビデオが同期され、ユーザーはリアルタイムで一緒に動画を視聴できます。アプリをダウンロードしていないユーザーは、App Storeにリダイレクトされます。

**同期メディア再生**<br>
同期メディア再生では、誰か1人がSharePlay動画を一時停止すると、すべてのデバイスで一時停止されます。<br><br>
![SharePlayの同期メディア再生]({% image_buster /assets/img/shareplay/shareplay7.png %}){: width="3770" height="1408" style="border:0"}

## 統合 {#integration}

この統合で使用されるアプリ内メッセージは、モーダルアプリ内メッセージビューコントローラーをサブクラス化したものです。設定のガイドは、iOSアプリ内メッセージの高度なユースケース[実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide)にあります。統合する前に、Xcodeプロジェクトに`GroupActivities`エンタイトルメントを追加してください。

{% alert important %}
統合を完了するために、[Apple SharePlayドキュメント](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback)をこのガイドと並べて開くことをお勧めします。
{% endalert %}

### ステップ1：XIBのオーバーライドとロード {#step-1-overriding-and-loading-xib}

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

### ステップ2：アプリ内メッセージ用のAVPlayerを構成する {#step-2-configure-avplayer-for-in-app-messages}

アプリ内メッセージは、軽量な開発者の作業でネイティブに動画を再生できます。これにより、SharePlayなど、`AVPlayerVideoController`のすべての機能にアクセスできます。この例で使用されるアプリ内メッセージは、ネイティブ動画プレーヤーを埋め込むカスタムビューを持つ`ABKInAppMessageModalViewController`のサブクラスです。

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

#### ダッシュボードの設定 {#dashboard-configuration}

**キーと値のペア**：動画ファイルはアプリ内メッセージのキーと値のペアで設定する必要があり、メディアアイテム自体にアタッチすることはできません。また、コンテンツを表示する前のガードレールとして、`beforeInAppMessageDisplayed`でURL有効性チェックを追加することもできます。

**トリガー**：アプリ内メッセージは、再適格性を有効にして、すべてのユーザーに対して適格となるようにする必要があります。これは、メッセージを起動するデフォルトのトリガーと、SharePlayから開始されたときにメッセージを起動するもう1つのトリガーの、2つのトリガーを設定することで実現できます。iOS 15を使用していないユーザーは、ローカルでのみメッセージを表示できます。

{% alert important %}
セッション開始時にトリガーされる他のアプリ内メッセージが互いに競合する可能性にご注意ください。
{% endalert %}

### ステップ3：グループ視聴アクティビティを作成する {#step-3-create-group-watching-activity}

`GroupActivity`プロトコルに準拠するオブジェクトを作成します。このオブジェクトは、SharePlayライフサイクル全体で共有される`GroupSession`のメタデータになります。

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

#### 再生の準備 {#prepare-to-play}

メディアアイテムの再生を準備する際、各グループアクティビティには`prepareForActivation()`の3つの状態があります：
- `.activationDisabled` - 個別視聴
- `.activationPreferred` - 一緒に視聴
- `.cancelled` - 無視して適切に処理する

状態が`activationPreferred`として返された場合、それはグループアクティビティライフサイクルの残りの部分をアクティベートするタイミングです。

![SharePlayの図]({% image_buster /assets/img/shareplay/shareplay.png %}){: width="3816" height="1408" style="border:0;"}

### ステップ4：SharePlay APIからアプリ内メッセージを起動する {#step-4-launch-in-app-message-from-shareplay-api}

`GroupActivities` APIは、動画が存在するかどうかを判断します。存在する場合、SharePlay対応のアプリ内メッセージを起動するカスタムイベントをトリガーする必要があります。`CoordinationManager`は、ユーザーが通話から離脱または参加した場合など、SharePlayの状態変更を担当します。

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

### ステップ5：アプリ内メッセージの非表示時にグループセッションを離脱する {#step-5-leaving-a-group-session-on-in-app-message-dismissal}

アプリ内メッセージが非表示になったとき、SharePlayセッションを離脱し、セッションオブジェクトを破棄する適切なタイミングです。

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

### SharePlayボタンの表示設定 {#configure-shareplay-button-visibility}

SharePlayインジケーターを動的に非表示または表示することがベストプラクティスです。`isEligibleForGroupSession`変数を使用して、ユーザーが現在FaceTime通話中かどうかを監視します。FaceTime通話中の場合、チャット内の互換性のあるデバイス間で動画を共有するボタンが表示される必要があります。ユーザーが初めてSharePlayを開始すると、元のデバイスにオプションを選択するプロンプトが表示されます。その後、共有先のユーザーのデバイスにコンテンツに参加するためのプロンプトが表示されます。

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