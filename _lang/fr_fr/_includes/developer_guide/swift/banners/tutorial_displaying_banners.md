## Conditions préalables {#prerequisites}

Avant de commencer ce tutoriel, veuillez vérifier que votre SDK Braze répond aux exigences minimales en matière de version :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Affichage de bannières pour le SDK Swift {#displaying-banners-for-the-swift-sdk}

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
  var bannerHeightConstraints: NSLayoutConstraint?

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

### 1. Activer le débogage (facultatif) {#1-enable-debugging-optional}

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!!step
lines-AppDelegate.swift=20

### 2. Actualiser vos placements {#2-refresh-your-placements}

Après avoir initialisé le SDK Braze, appelez `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` pour actualiser le contenu de la bannière au début de chaque session.

!!step
lines-BannerViewController.swift=19-37

### 3. Initialiser la bannière et fournir un rappel {#3-initialize-the-banner-and-provide-a-callback}

Créez une instance `BrazeBannerUI.BannerUIView` avec votre objet Braze et votre ID de placement, puis fournissez un rappel `processContentUpdates` pour afficher la bannière et mettre à jour sa contrainte de hauteur en fonction de la hauteur du contenu fourni.

!!step
lines-BannerViewController.swift=38-40

### 4. Activer les contraintes Auto Layout {#4-enable-auto-layout-constraints}

Masquez la vue de la bannière par défaut, puis désactivez la traduction du masque de redimensionnement automatique afin d'activer les contraintes Auto Layout.

!!step
lines-BannerViewController.swift=43-58

### 5. Ancrer le contenu et définir des contraintes de hauteur {#5-anchor-content-and-set-height-constraints}

Ancrez votre contenu principal en haut à l'aide d'Auto Layout et placez la vue de la bannière après celui-ci. Épinglez les bords avant (leading), arrière (trailing) et inférieur de la bannière à la zone sécurisée (safe area), et définissez une contrainte de hauteur initiale de `0` qui sera mise à jour lors du chargement du contenu.

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

### 1. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!!step
lines-AppDelegate.swift=19

### 2. Actualiser vos placements

Après avoir initialisé le SDK Braze, appelez `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` pour actualiser le contenu de la bannière au début de chaque session.

!!step
lines-BannerSwiftUIView.swift=1-46

### 3. Créer un composant de vue {#3-create-a-view-component}

Créez un composant de vue SwiftUI réutilisable qui affiche les bannières disponibles et contient le contenu principal de votre application si nécessaire.

!!step
lines-BannerSwiftUIView.swift=36-43

### 4. Afficher uniquement les bannières disponibles {#4-only-display-available-banners}

N'essayez d'afficher `BrazeBannerUI.BannerView` que si le SDK est initialisé et que du contenu de bannière existe pour cet utilisateur. Dans `.onAppear`, appelez `getBanner(for:placementID)` pour définir l'état de `hasBannerForPlacement`.

!!step
lines-BannerSwiftUIView.swift=17-32

### 5. Afficher `BannerView` uniquement après son chargement {#5-only-show-bannerview-after-it-loads}

Afin d'éviter les espaces vides dans votre interface utilisateur, n'affichez `BrazeBannerUI.BannerView` que si une bannière est présente et que le SDK est initialisé.

!!step
lines-BannerSwiftUIView.swift=23-32

### 6. Mettre à jour dynamiquement la hauteur de la bannière {#6-dynamically-update-banner-height}

Utilisez le rappel `processContentUpdates` pour récupérer la hauteur du contenu de la bannière dès son chargement. Mettez à jour votre état SwiftUI (`contentHeight`) et appliquez une contrainte `.frame(height:)` en utilisant la hauteur fournie.

!!step
lines-BannerSwiftUIView.swift=34

### 7. Limiter la hauteur de la bannière {#7-limit-the-banner-height}

Pour vous assurer que votre bannière ne dépasse jamais la hauteur maximale, appliquez le modificateur `.frame(height: min(contentHeight, 80))`. Cela permet de conserver l'équilibre visuel de votre interface utilisateur, quel que soit le contenu de la bannière.

{% endscrolly %}
{% endtab %}
{% endtabs %}