## Voraussetzungen {#prerequisites}

Bevor Sie mit diesem Tutorial beginnen, überprüfen Sie, ob Ihr Braze SDK die Mindestanforderungen erfüllt:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Anzeige von Bannern für das Swift SDK {#displaying-banners-for-the-swift-sdk}

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

### 1. Debugging aktivieren (optional) {#1-enable-debugging-optional} {#1-enable-debugging-optional}

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie Debugging aktivieren.

!!step
lines-AppDelegate.swift=20

### 2. Platzierungen aktualisieren {#2-refresh-your-placements} {#2-refresh-your-placements}

Rufen Sie nach der Initialisierung des Braze SDK `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` auf, um den Banner-Inhalt zu Beginn jeder Sitzung zu aktualisieren.

!!step
lines-BannerViewController.swift=19-37

### 3. Banner initialisieren und Callback bereitstellen {#3-initialize-the-banner-and-provide-a-callback} {#3-initialize-the-banner-and-provide-a-callback}

Erstellen Sie eine `BrazeBannerUI.BannerUIView`-Instanz mit Ihrem Braze-Objekt und der Platzierungs-ID und stellen Sie einen `processContentUpdates`-Callback bereit, um das Banner einzublenden und seine Höhenbeschränkung basierend auf der bereitgestellten Inhaltshöhe zu aktualisieren.

!!step
lines-BannerViewController.swift=38-40

### 4. Auto-Layout-Constraints aktivieren {#4-enable-auto-layout-constraints} {#4-enable-auto-layout-constraints}

Blenden Sie die Banner-Ansicht standardmäßig aus und deaktivieren Sie dann die Autoresizing-Mask-Übersetzung, um Auto-Layout-Constraints zu aktivieren.

!!step
lines-BannerViewController.swift=43-58

### 5. Inhalte verankern und Höhenbeschränkungen festlegen {#5-anchor-content-and-set-height-constraints} {#5-anchor-content-and-set-height-constraints}

Verankern Sie Ihren Hauptinhalt mithilfe von Auto Layout oben und platzieren Sie die Banner-Ansicht danach. Heften Sie die führende, nachfolgende und untere Kante des Banners an den sicheren Bereich und legen Sie eine anfängliche Höhenbeschränkung von `0` fest, die aktualisiert wird, wenn der Inhalt geladen ist.

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

### 1. Debugging aktivieren (optional) {#1-enable-debugging-optional}

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie Debugging aktivieren.

!!step
lines-AppDelegate.swift=19

### 2. Platzierungen aktualisieren {#2-refresh-your-placements}

Rufen Sie nach der Initialisierung des Braze SDK `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` auf, um den Banner-Inhalt zu Beginn jeder Sitzung zu aktualisieren.

!!step
lines-BannerSwiftUIView.swift=1-46

### 3. View-Komponente erstellen {#3-create-a-view-component} {#3-create-a-view-component}

Erstellen Sie eine wiederverwendbare SwiftUI-View-Komponente, die verfügbare Banner anzeigt und bei Bedarf Ihren Hauptinhalt der App enthält.

!!step
lines-BannerSwiftUIView.swift=36-43

### 4. Nur verfügbare Banner anzeigen {#4-only-display-available-banners} {#4-only-display-available-banners}

Versuchen Sie nur dann, `BrazeBannerUI.BannerView` anzuzeigen, wenn das SDK initialisiert ist und Banner-Inhalt für diese Nutzer:in vorhanden ist. Rufen Sie in `.onAppear` die Methode `getBanner(for:placementID)` auf, um den Status von `hasBannerForPlacement` festzulegen.

!!step
lines-BannerSwiftUIView.swift=17-32

### 5. `BannerView` erst nach dem Laden anzeigen {#5-only-show-bannerview-after-it-loads} {#5-only-show-bannerview-after-it-loads}

Um leeren Platz in Ihrer UI zu vermeiden, zeigen Sie `BrazeBannerUI.BannerView` nur an, wenn ein Banner vorhanden und das SDK initialisiert ist.

!!step
lines-BannerSwiftUIView.swift=23-32

### 6. Banner-Höhe dynamisch aktualisieren {#6-dynamically-update-banner-height} {#6-dynamically-update-banner-height}

Verwenden Sie den `processContentUpdates`-Callback, um die Inhaltshöhe des Banners abzurufen, sobald es geladen ist. Aktualisieren Sie Ihren SwiftUI-Status (`contentHeight`) und wenden Sie eine `.frame(height:)`-Beschränkung mit der bereitgestellten Höhe an.

!!step
lines-BannerSwiftUIView.swift=34

### 7. Banner-Höhe begrenzen {#7-limit-the-banner-height} {#7-limit-the-banner-height}

Um sicherzustellen, dass Ihr Banner die maximale Höhe nie überschreitet, wenden Sie den Modifier `.frame(height: min(contentHeight, 80))` an. Dadurch bleibt Ihre UI unabhängig vom Inhalt des Banners visuell ausgewogen.

{% endscrolly %}
{% endtab %}
{% endtabs %}