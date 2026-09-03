## 前提条件 {#prerequisites}

このチュートリアルを始める前に、Braze SDKが最低バージョン要件を満たしていることを確認してください：

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Swift SDKのバナーを表示する {#displaying-banners-for-the-swift-sdk}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Displaying Banners Swift" %}

{% tabs %}
{% tab UIKit %}
{% scrolly %}

```swift file=AppDelegate.swift
import UIKit
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze? = nil

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR-API-TOKEN", endpoint: "YOUR-ENDPOINT")
        configuration.logger.level = .debug

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        // Request a banners refresh
        AppDelegate.braze?.banners.requestBannersRefresh(placementIds: ["top-1"])

        return true
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
    // Bind the AppDelegate into the SwiftUI lifecycle
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

```swift file=BannerViewController.swift
import UIKit
import BrazeKit
import BrazeUI

final class BannerViewController: UIViewController {

  static let bannerPlacementID = "top-1"
  var bannerHeightConstraint: NSLayoutConstraint?

  lazy var contentView: UILabel = {
    let contentView = UILabel()
    contentView.text = "Your Content Here"
    contentView.textAlignment = .center
    contentView.translatesAutoresizingMaskIntoConstraints = false
    return contentView
  }()

  lazy var bannerView: BrazeBannerUI.BannerUIView = {
    var bannerView = BrazeBannerUI.BannerUIView(
      placementId: BannerViewController.bannerPlacementID,
      braze: AppDelegate.braze!,
      processContentUpdates: { [weak self] result in
        // Update layout properties when banner content has finished loading.
        DispatchQueue.main.async {
          guard let self else { return }
          switch result {
          case .success(let updates):
            if let height = updates.height {
              self.bannerView.isHidden = false
              self.bannerHeightConstraint?.constant = min(height, 80)
            }
          case .failure(let error):
            return
          }
        }
      }
    )
    bannerView.translatesAutoresizingMaskIntoConstraints = false
    bannerView.isHidden = true
    return bannerView
  }()

  override func viewDidLoad() {
    super.viewDidLoad()
    self.view.addSubview(contentView)
    self.view.addSubview(bannerView)
    bannerHeightConstraint = bannerView.heightAnchor.constraint(equalToConstant: 0)
    NSLayoutConstraint.activate([
      contentView.topAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.topAnchor),
      contentView.leadingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.leadingAnchor),
      contentView.trailingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.trailingAnchor),
      bannerView.topAnchor.constraint(equalTo: self.contentView.bottomAnchor),
      bannerView.leadingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.leadingAnchor),
      bannerView.trailingAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.trailingAnchor),
      bannerView.bottomAnchor.constraint(equalTo: self.view.safeAreaLayoutGuide.bottomAnchor),
      bannerHeightConstraint!,
    ])
  }
}
```

!!step
lines-AppDelegate.swift=14

### 1. デバッグを有効にする（オプション） {#1-enable-debugging-optional} {#1-enable-debugging-optional}

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=20

### 2. プレースメントを更新する {#2-refresh-your-placements} {#2-refresh-your-placements}

Braze SDKを初期化した後、`requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`を呼び出して、各セッションの開始時にバナーコンテンツを更新します。

!!step
lines-BannerViewController.swift=19-37

### 3. バナーを初期化してコールバックを提供する {#3-initialize-the-banner-and-provide-a-callback} {#3-initialize-the-banner-and-provide-a-callback}

BrazeオブジェクトとプレースメントIDを使用して`BrazeBannerUI.BannerUIView`インスタンスを作成し、`processContentUpdates`コールバックを提供してバナーを表示し、提供されたコンテンツの高さに基づいて高さの制約を更新します。

!!step
lines-BannerViewController.swift=38-40

### 4. Auto Layoutの制約を有効にする {#4-enable-auto-layout-constraints} {#4-enable-auto-layout-constraints}

デフォルトでバナービューを非表示にし、Auto Layoutの制約を有効にするためにautoresizingマスクの変換を無効にします。

!!step
lines-BannerViewController.swift=43-58

### 5. コンテンツをアンカーして高さの制約を設定する {#5-anchor-content-and-set-height-constraints} {#5-anchor-content-and-set-height-constraints}

Auto Layoutを使用してメインコンテンツを上部にアンカーし、その後にバナービューを配置します。バナーのleading、trailing、bottomエッジをセーフエリアにピン留めし、コンテンツが読み込まれたときに更新される初期高さ制約を`0`に設定します。

{% endscrolly %}
{% endtab %}
{% tab SwiftUI %}
{% scrolly %}

```swift file=AppDelegate.swift
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate {
    static var braze: Braze? = nil

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        // Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR-API-TOKEN", endpoint: "YOUR-ENDPOINT")
        configuration.logger.level = .debug

        // Initialize Braze SDK instance
        AppDelegate.braze = Braze(configuration: configuration)

        // Request a banners refresh
        AppDelegate.braze?.banners.requestBannersRefresh(placementIds: ["top-1"])

        return true
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
    // Bind the AppDelegate into the SwiftUI lifecycle
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            BannerSwiftUIView()
        }
    }
}
```

```swift file=BannerSwiftUIView.swift
import BrazeKit
import BrazeUI
import SwiftUI

@available(iOS 13.0, *)
struct BannerSwiftUIView: View {

  static let bannerPlacementID = "top-1"

  @State var hasBannerForPlacement: Bool = false
  @State var contentHeight: CGFloat = 0

  var body: some View {
    VStack {
      Text("Your Content Here")
        .frame(maxWidth: .infinity, maxHeight: .infinity)
      if let braze = AppDelegate.braze,
        hasBannerForPlacement
      {
        BrazeBannerUI.BannerView(
          placementId: BannerSwiftUIView.bannerPlacementID,
          braze: braze,
          processContentUpdates: { result in
            switch result {
            case .success(let updates):
              if let height = updates.height {
                self.contentHeight = height
              }
            case .failure:
              return
            }
          }
        )
        .frame(height: min(contentHeight, 80))
      }
    }.onAppear {
      AppDelegate.braze?.banners.getBanner(
        for: BannerSwiftUIView.bannerPlacementID,
        { banner in
          hasBannerForPlacement = banner != nil
        }
      )
    }
  }
}

```

!!step
lines-AppDelegate.swift=13

### 1. デバッグを有効にする（オプション） {#1-enable-debugging-optional}

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=19

### 2. プレースメントを更新する {#2-refresh-your-placements}

Braze SDKを初期化した後、`requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`を呼び出して、各セッションの開始時にバナーコンテンツを更新します。

!!step
lines-BannerSwiftUIView.swift=1-46

### 3. ビューコンポーネントを作成する {#3-create-a-view-component} {#3-create-a-view-component}

利用可能なバナーを表示し、必要に応じてメインアプリのコンテンツを含む再利用可能なSwiftUIビューコンポーネントを作成します。

!!step
lines-BannerSwiftUIView.swift=36-43

### 4. 利用可能なバナーのみを表示する {#4-only-display-available-banners} {#4-only-display-available-banners}

SDKが初期化されており、そのユーザーにバナーコンテンツが存在する場合にのみ、`BrazeBannerUI.BannerView`の表示を試みます。`.onAppear`で`getBanner(for:placementID)`を呼び出して、`hasBannerForPlacement`のステートを設定します。

!!step
lines-BannerSwiftUIView.swift=17-32

### 5. 読み込み後にのみ`BannerView`を表示する {#5-only-show-bannerview-after-it-loads} {#5-only-show-bannerview-after-it-loads}

UIに空白スペースが表示されないようにするために、バナーが存在しSDKが初期化されている場合にのみ`BrazeBannerUI.BannerView`を表示します。

!!step
lines-BannerSwiftUIView.swift=23-32

### 6. バナーの高さをダイナミックに更新する {#6-dynamically-update-banner-height} {#6-dynamically-update-banner-height}

`processContentUpdates`コールバックを使用して、バナーのコンテンツの高さが読み込まれたらすぐに取得します。SwiftUIのステート（`contentHeight`）を更新し、提供された高さを使用して`.frame(height:)`制約を適用します。

!!step
lines-BannerSwiftUIView.swift=34

### 7. バナーの高さを制限する {#7-limit-the-banner-height} {#7-limit-the-banner-height}

バナーが最大高さを超えないようにするために、`.frame(height: min(contentHeight, 80))`モディファイアを適用します。これにより、バナーのコンテンツに関係なく、UIの視覚的なバランスが保たれます。

{% endscrolly %}
{% endtab %}
{% endtabs %}