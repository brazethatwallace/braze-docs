---
nav_title: SharePlay
article_title: SharePlay アプリ内メッセージ実装ガイド
platform: iOS
page_order: 1
description: "この高度なSharePlay実装ガイドは、アプリ内メッセージの高度な実装ガイドで提供される動画のユースケースを詳しく説明しています。SharePlayは、iOS 15 FaceTimeユーザーがデバイス間でメディア体験を共有し、リアルタイムでオーディオと動画を同期することを可能にする新たにリリースされた機能です。"
channel:
  - in-app messages
alias: /shareplay/

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SharePlay アプリ内メッセージ実装ガイド {#shareplay-in-app-message-implementation-guide}

> SharePlayは、iOS 15 FaceTimeユーザーがデバイス間でメディア体験を共有し、リアルタイムでオーディオと動画を同期することを可能にする新たにリリースされた機能です。SharePlayは、ユーザーが友人や家族と一緒にコンテンツを体験できる優れた方法であり、Brazeの顧客に動画コンテンツを利用する新たな手段を提供し、アプリケーションを新しいユーザーに紹介する機会を提供します。

![SharePlay]({% image_buster /assets/img/shareplay/shareplay6.png %}){: style="border:0;margin-top:10px;"}
## 概要 {#overview}

iOS 15アップデートの一部としてAppleがリリースした新しい`GroupActivities`フレームワークを使用すると、Brazeアプリ内メッセージを利用してSharePlayをアプリケーションに統合することで、FaceTimeを活用できるようになります。
![SharePlay]({% image_buster /assets/img/shareplay/shareplay3.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;"}

ユーザーがFaceTime通話でSharePlay動画を開始すると、全員の画面の上部に「Open」ボタンが表示されます。開くと、オーディオと動画がすべての互換性のあるデバイス間で同期され、ユーザーはリアルタイムで動画を一緒に視聴できるようになります。アプリをダウンロードしていない人は、App Storeにリダイレクトされます。

**同期メディア再生**<br>
同期メディア再生では、1人がSharePlay動画を一時停止すると、すべてのデバイスで一時停止されます。<br><br>
![SharePlay]({% image_buster /assets/img/shareplay/shareplay7.png %}){: style="border:0"}

## 統合 {#integration}

この統合で使用されるアプリ内メッセージは、サブクラス化されたモーダルアプリ内メッセージビューコントローラーです。セットアップのガイドは、iOSアプリ内メッセージの高度なユースケース[実装ガイド]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide)に記載されています。統合する前に、Xcodeプロジェクトに`GroupActivities`エンタイトルメントを追加してください。

{% alert important %}
統合を完了するには、このガイドと並行して[Apple SharePlayドキュメント](https://developer.apple.com/documentation/avfoundation/media_playback_and_selection/supporting_coordinated_media_playback)を開くことをお勧めします。
{% endalert %}

### ステップ1:XIBのオーバーライドと読み込み {#step-1-overriding-and-loading-xib}

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

### ステップ2:アプリ内メッセージ用にAVPlayerを設定する {#step-2-configure-avplayer-for-in-app-messages}

アプリ内メッセージでは、開発者の軽微な作業だけで動画をネイティブに再生できます。こうすることで、SharePlayなど、すべての`AVPlayerVideoController`機能にアクセスできるようになります。この例で使用されるアプリ内メッセージは、ネイティブ動画プレーヤーを埋め込むためのカスタムビューを持つサブクラス化された`ABKInAppMessageModalViewController`です。

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

**キーと値のペア**:動画ファイルはアプリ内メッセージのキーと値のペアで設定する必要があり、メディア項目自体に添付することはできません。コンテンツを表示する前に、ガードレールとして`beforeInAppMessageDisplayed`にURLの有効性チェックを追加することもできます。

**トリガー**:アプリ内メッセージは、再適格性が有効になっているすべてのユーザーに対して有効にする必要があります。これは、メッセージを起動するデフォルトのトリガーと、SharePlayから開始されたときにメッセージを起動するもう1つのトリガーの2つのトリガーを設定することで実行できます。iOS 15を使用していないユーザーは、メッセージをローカルでのみ表示できます。

{% alert important %}
セッション開始時にトリガーされる他のアプリ内メッセージが互いに競合する可能性があることに注意してください。
{% endalert %}

### ステップ3:グループ視聴アクティビティを作成する {#step-3-create-group-watching-activity}

`GroupActivity`プロトコルに準拠したオブジェクトを作成します。このオブジェクトは、SharePlayライフサイクル全体で共有される`GroupSession`のメタデータになります。

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

#### 再生の準備をする {#prepare-to-play}

メディア項目の再生を準備するとき、各グループアクティビティの`prepareForActivation()`には以下の3つの状態があります。
- `.activationDisabled` - 個別視聴
- `.activationPreferred` - 一緒に視聴
- `.cancelled` - 無視して適切に処理する

状態が`activationPreferred`として返されたら、残りのグループアクティビティのライフサイクルをアクティブにする合図です。

![SharePlay]({% image_buster /assets/img/shareplay/shareplay.png %}){: style="border:0;"}

### ステップ4:SharePlay APIからアプリ内メッセージを起動する {#step-4-launch-in-app-message-from-shareplay-api}

`GroupActivities` APIは動画が存在するかどうかを判別します。存在する場合は、カスタムイベントをトリガーして、SharePlay対応のアプリ内メッセージを起動する必要があります。`CoordinationManager`は、ユーザーが通話から離れた場合や通話に参加した場合など、SharePlayの状態変更を管理します。

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

### ステップ5:アプリ内メッセージの終了時にグループセッションを退出する {#step-5-leaving-a-group-session-on-in-app-message-dismissal}

アプリ内メッセージが閉じられたときが、SharePlayセッションを退出し、セッションオブジェクトを破棄する適切なタイミングです。

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

### SharePlayボタンの表示を設定する {#configure-shareplay-button-visibility}

SharePlayインジケーターを動的に非表示または表示することがベストプラクティスです。`isEligibleForGroupSession`変数を使用して、ユーザーが現在FaceTime通話中かどうかを確認します。FaceTime通話中の場合は、チャット内の互換性のあるデバイス間で動画を共有するためのボタンが表示されるようにします。ユーザーが初めてSharePlayを開始すると、元のデバイスにオプションを選択するためのプロンプトが表示されます。その後、共有ユーザーのデバイスに、コンテンツに参加するためのプロンプトが表示されます。

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