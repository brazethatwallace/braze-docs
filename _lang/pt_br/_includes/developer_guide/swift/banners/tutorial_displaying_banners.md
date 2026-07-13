## Pré-requisitos {#prerequisites}

Antes de começar este tutorial, verifique se o seu SDK Braze atende aos requisitos mínimos de versão:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Exibindo banners para o SDK Swift {#displaying-banners-for-the-swift-sdk}

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

### 1. Ativar depuração (opcional) {#1-enable-debugging-optional}

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!step
lines-AppDelegate.swift=20

### 2. Atualize seus posicionamentos {#2-refresh-your-placements}

Após inicializar o SDK da Braze, chame `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` para atualizar o conteúdo do Banner no início de cada sessão.

!!step
lines-BannerViewController.swift=19-37

### 3. Inicialize o Banner e forneça um retorno de chamada {#3-initialize-the-banner-and-provide-a-callback}

Crie uma instância de `BrazeBannerUI.BannerUIView` com seu objeto Braze e ID de colocação, e forneça um retorno de chamada `processContentUpdates` para exibir o Banner e atualizar sua restrição de altura com base na altura do conteúdo fornecido.

!!step
lines-BannerViewController.swift=38-40

### 4. Ativar restrições de Auto Layout {#4-enable-auto-layout-constraints}

Oculte a visualização do Banner por padrão e desative a tradução da máscara de redimensionamento automático para ativar as restrições de Auto Layout.

!!step
lines-BannerViewController.swift=43-58

### 5. Ancore o conteúdo e defina restrições de altura {#5-anchor-content-and-set-height-constraints}

Ancore seu conteúdo principal na parte superior usando Auto Layout e coloque a visualização do Banner logo abaixo dele. Prenda as bordas leading, trailing e inferior do Banner à área segura e defina uma restrição de altura inicial de `0` que será atualizada quando o conteúdo for carregado.

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

### 1. Ativar depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!step
lines-AppDelegate.swift=19

### 2. Atualize seus posicionamentos

Após inicializar o SDK da Braze, chame `requestBannersRefresh(placementIds: ["PLACEMENT_ID"])` para atualizar o conteúdo do Banner no início de cada sessão.

!!step
lines-BannerSwiftUIView.swift=1-46

### 3. Crie um componente de visualização {#3-create-a-view-component}

Crie um componente de visualização reutilizável em SwiftUI que exiba Banners disponíveis e contenha o conteúdo principal do seu app, se necessário.

!!step
lines-BannerSwiftUIView.swift=36-43

### 4. Exiba apenas Banners disponíveis {#4-only-display-available-banners}

Tente mostrar `BrazeBannerUI.BannerView` apenas se o SDK estiver inicializado e houver conteúdo de Banner para esse usuário. Em `.onAppear`, chame `getBanner(for:placementID)` para definir o estado de `hasBannerForPlacement`.

!!step
lines-BannerSwiftUIView.swift=17-32

### 5. Mostre `BannerView` apenas após o carregamento {#5-only-show-bannerview-after-it-loads}

Para evitar espaço em branco na sua interface, mostre `BrazeBannerUI.BannerView` apenas se um Banner estiver presente e o SDK estiver inicializado.

!!step
lines-BannerSwiftUIView.swift=23-32

### 6. Atualize dinamicamente a altura do Banner {#6-dynamically-update-banner-height}

Use o retorno de chamada `processContentUpdates` para obter a altura do conteúdo do Banner assim que ele for carregado. Atualize seu estado SwiftUI (`contentHeight`) e aplique uma restrição `.frame(height:)` usando a altura fornecida.

!!step
lines-BannerSwiftUIView.swift=34

### 7. Limite a altura do Banner {#7-limit-the-banner-height}

Para garantir que seu Banner nunca exceda a altura máxima, aplique o modificador `.frame(height: min(contentHeight, 80))`. Isso manterá sua interface visualmente equilibrada, independentemente do conteúdo do Banner.

{% endscrolly %}
{% endtab %}
{% endtabs %}