## 필수 조건 {#prerequisites}

이 튜토리얼을 시작하기 전에 Braze SDK가 최소 버전 요구 사항을 충족하는지 확인하십시오:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## SWIFT SDK용 배너 표시 {#displaying-banners-for-the-swift-sdk}

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

### 1. 디버깅 활성화(선택 사항) {#1-enable-debugging-optional} {#1-enable-debugging-optional}

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!step
lines-AppDelegate.swift=20

### 2. 배치 새로고침 {#2-refresh-your-placements} {#2-refresh-your-placements}

Braze SDK를 초기화한 후 `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`를 호출하여 각 세션 시작 시 배너 콘텐츠를 새로고침합니다.

!!step
lines-BannerViewController.swift=19-37

### 3. 배너 초기화 및 콜백 제공 {#3-initialize-the-banner-and-provide-a-callback} {#3-initialize-the-banner-and-provide-a-callback}

Braze 객체와 배치 ID를 사용하여 `BrazeBannerUI.BannerUIView` 인스턴스를 생성하고, `processContentUpdates` 콜백을 제공하여 배너를 표시하고 제공된 콘텐츠 높이에 따라 높이 제약 조건을 업데이트합니다.

!!step
lines-BannerViewController.swift=38-40

### 4. Auto Layout 제약 조건 활성화 {#4-enable-auto-layout-constraints} {#4-enable-auto-layout-constraints}

기본적으로 배너 뷰를 숨긴 다음, Auto Layout 제약 조건을 활성화하기 위해 autoresizing mask 변환을 비활성화합니다.

!!step
lines-BannerViewController.swift=43-58

### 5. 콘텐츠 앵커 설정 및 높이 제약 조건 지정 {#5-anchor-content-and-set-height-constraints} {#5-anchor-content-and-set-height-constraints}

Auto Layout을 사용하여 메인 콘텐츠를 상단에 앵커하고, 그 아래에 배너 뷰를 배치합니다. 배너의 leading, trailing, bottom 가장자리를 safe area에 고정하고, 콘텐츠가 로드될 때 업데이트될 초기 높이 제약 조건을 `0`으로 설정합니다.

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

### 1. 디버깅 활성화(선택 사항) {#1-enable-debugging-optional}

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!step
lines-AppDelegate.swift=19

### 2. 배치 새로고침 {#2-refresh-your-placements}

Braze SDK를 초기화한 후 `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])`를 호출하여 각 세션 시작 시 배너 콘텐츠를 새로고침합니다.

!!step
lines-BannerSwiftUIView.swift=1-46

### 3. 뷰 컴포넌트 생성 {#3-create-a-view-component} {#3-create-a-view-component}

사용 가능한 배너를 표시하고 필요한 경우 메인 앱 콘텐츠를 포함하는 재사용 가능한 SwiftUI 뷰 컴포넌트를 생성합니다.

!!step
lines-BannerSwiftUIView.swift=36-43

### 4. 사용 가능한 배너만 표시 {#4-only-display-available-banners} {#4-only-display-available-banners}

SDK가 초기화되어 있고 해당 사용자에 대한 배너 콘텐츠가 존재하는 경우에만 `BrazeBannerUI.BannerView`를 표시합니다. `.onAppear`에서 `getBanner(for:placementID)`를 호출하여 `hasBannerForPlacement`의 상태를 설정합니다.

!!step
lines-BannerSwiftUIView.swift=17-32

### 5. 로드 후에만 `BannerView` 표시 {#5-only-show-bannerview-after-it-loads} {#5-only-show-bannerview-after-it-loads}

UI에 빈 공간이 생기지 않도록, 배너가 존재하고 SDK가 초기화된 경우에만 `BrazeBannerUI.BannerView`를 표시합니다.

!!step
lines-BannerSwiftUIView.swift=23-32

### 6. 배너 높이 동적 업데이트 {#6-dynamically-update-banner-height} {#6-dynamically-update-banner-height}

`processContentUpdates` 콜백을 사용하여 배너의 콘텐츠 높이가 로드되는 즉시 가져옵니다. SwiftUI 상태(`contentHeight`)를 업데이트하고 제공된 높이를 사용하여 `.frame(height:)` 제약 조건을 적용합니다.

!!step
lines-BannerSwiftUIView.swift=34

### 7. 배너 높이 제한 {#7-limit-the-banner-height} {#7-limit-the-banner-height}

배너가 최대 높이를 초과하지 않도록 `.frame(height: min(contentHeight, 80))` 수정자를 적용합니다. 이렇게 하면 배너의 콘텐츠에 관계없이 UI가 시각적으로 균형 잡힌 상태를 유지합니다.

{% endscrolly %}
{% endtab %}
{% endtabs %}