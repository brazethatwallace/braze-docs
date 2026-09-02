## Requisitos previos {#prerequisites}

Antes de comenzar este tutorial, comprueba que tu SDK de Braze cumple los requisitos mínimos de versión:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Mostrar banners para el SDK de Swift {#displaying-banners-for-the-swift-sdk}

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

### 1. Habilitar depuración (opcional) {#1-enable-debugging-optional} {#1-enable-debugging-optional}

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-AppDelegate.swift=20

### 2. Actualizar tus ubicaciones {#2-refresh-your-placements} {#2-refresh-your-placements}

Después de inicializar el SDK de Braze, llama a `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` para actualizar el contenido de los banners al inicio de cada sesión.

!!step
lines-BannerViewController.swift=19-37

### 3. Inicializar el banner y proporcionar una devolución de llamada {#3-initialize-the-banner-and-provide-a-callback} {#3-initialize-the-banner-and-provide-a-callback}

Crea una instancia de `BrazeBannerUI.BannerUIView` con tu objeto Braze y el ID de ubicación, y proporciona una devolución de llamada `processContentUpdates` para mostrar el banner y actualizar su restricción de altura en función de la altura del contenido proporcionado.

!!step
lines-BannerViewController.swift=38-40

### 4. Habilitar restricciones de Auto Layout {#4-enable-auto-layout-constraints} {#4-enable-auto-layout-constraints}

Oculta la vista del banner de forma predeterminada y luego desactiva la traducción de máscara de redimensionamiento automático para habilitar las restricciones de Auto Layout.

!!step
lines-BannerViewController.swift=43-58

### 5. Anclar el contenido y establecer restricciones de altura {#5-anchor-content-and-set-height-constraints} {#5-anchor-content-and-set-height-constraints}

Ancla tu contenido principal en la parte superior usando Auto Layout y coloca la vista del banner después de él. Fija los bordes izquierdo, derecho e inferior del banner al área segura, y establece una restricción de altura inicial de `0` que se actualizará cuando se cargue el contenido.

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

### 1. Habilitar depuración (opcional) {#1-enable-debugging-optional}

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-AppDelegate.swift=19

### 2. Actualizar tus ubicaciones {#2-refresh-your-placements}

Después de inicializar el SDK de Braze, llama a `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` para actualizar el contenido de los banners al inicio de cada sesión.

!!step
lines-BannerSwiftUIView.swift=1-46

### 3. Crear un componente de vista {#3-create-a-view-component} {#3-create-a-view-component}

Crea un componente de vista SwiftUI reutilizable que muestre los banners disponibles y contenga el contenido principal de tu aplicación si es necesario.

!!step
lines-BannerSwiftUIView.swift=36-43

### 4. Mostrar solo los banners disponibles {#4-only-display-available-banners} {#4-only-display-available-banners}

Solo intenta mostrar `BrazeBannerUI.BannerView` si el SDK está inicializado y existe contenido de banner para ese usuario. En `.onAppear`, llama a `getBanner(for:placementID)` para establecer el estado de `hasBannerForPlacement`.

!!step
lines-BannerSwiftUIView.swift=17-32

### 5. Mostrar `BannerView` solo después de que se cargue {#5-only-show-bannerview-after-it-loads} {#5-only-show-bannerview-after-it-loads}

Para evitar espacios en blanco en tu interfaz, solo muestra `BrazeBannerUI.BannerView` si hay un banner presente y el SDK está inicializado.

!!step
lines-BannerSwiftUIView.swift=23-32

### 6. Actualizar dinámicamente la altura del banner {#6-dynamically-update-banner-height} {#6-dynamically-update-banner-height}

Usa la devolución de llamada `processContentUpdates` para obtener la altura del contenido del banner tan pronto como se cargue. Actualiza el estado de SwiftUI (`contentHeight`) y aplica una restricción `.frame(height:)` usando la altura proporcionada.

!!step
lines-BannerSwiftUIView.swift=34

### 7. Limitar la altura del banner {#7-limit-the-banner-height} {#7-limit-the-banner-height}

Para asegurarte de que tu banner nunca exceda la altura máxima, aplica un modificador `.frame(height: min(contentHeight, 80))`. Esto mantendrá tu interfaz visualmente equilibrada independientemente del contenido del banner.

{% endscrolly %}
{% endtab %}
{% endtabs %}