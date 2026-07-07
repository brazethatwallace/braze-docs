---
nav_title: Gerenciar posicionamentos
article_title: Gerenciar posicionamentos de Banner para o SDK da Braze
description: "Aprenda como criar e gerenciar posicionamentos de Banner no SDK da Braze, incluindo o acesso às suas propriedades exclusivas e o registro de impressões."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Gerenciar posicionamentos de Banner {#manage-banner-placements}

> Aprenda como criar e gerenciar posicionamentos de Banner no SDK da Braze, incluindo o acesso às suas propriedades exclusivas e o registro de impressões. Para mais informações gerais, veja [Sobre Banners]({{site.baseurl}}/developer_guide/banners).

## Sobre solicitações de posicionamento {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Criar um posicionamento {#create-a-placement}

### Pré-requisitos {#prerequisites}

Estas são as versões mínimas do SDK necessárias para criar posicionamentos de Banner:

{% multi_lang_include developer_guide/sdk_versions.md feature='banners' %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Etapa 2: Atualize os posicionamentos no seu app {#requestBannersRefresh}

Para atualizar os posicionamentos, chame o método de atualização do seu SDK. Se `subscribeToBannersUpdates` estiver ativo, o SDK republica automaticamente os IDs de posicionamento em cache no início de cada nova sessão e quando você chama `changeUser`. Essa atualização automática não consome um token de limite de frequência.

{% alert tip %}
Atualize os posicionamentos o mais rápido possível para evitar atrasos no download ou na exibição dos Banners.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Etapa 3: Ouça as atualizações {#subscribeToBannersUpdates}

{% alert tip %}
Se você inserir Banners usando os métodos do SDK neste guia, todos os eventos de análise de dados (como impressões e cliques) serão tratados automaticamente, e as impressões só serão registradas quando o banner estiver visível.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab JavaScript %}
Se você estiver usando JavaScript puro com o SDK Web da Braze, use [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) para ouvir atualizações de posicionamento e, em seguida, chame [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) para buscá-las.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
Se você estiver usando React com o SDK Web da Braze, configure [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) dentro de um hook `useEffect` e chame [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) após registrar seu ouvinte.

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Swift %}

{% alert note %}
O ouvinte de atualização de banner reflete o estado do banner na memória do SDK. Uma única atualização pode incluir posicionamentos que já estavam em cache (por exemplo, de uma atualização anterior, outra tela ou trabalho automático do SDK), não apenas os IDs de posicionamento da sua chamada `requestRefresh` mais recente. Se você se importa apenas com determinados posicionamentos, verifique o ID de posicionamento de cada banner no seu ouvinte e ignore o restante. Quando tiver registrado seu ouvinte, chame `requestRefresh` para os posicionamentos que deseja sincronizar da Braze.
{% endalert %}

```swift
let placementIds = ["global_banner", "navigation_square_banner"]
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
// Always refresh after your subscriber is registered
brazeClient.braze()?.banners.requestRefresh(placementIds: placementIds)
```

{% endtab %}
{% tab Android %}

{% alert note %}
O ouvinte de atualização de banner reflete o estado do banner na memória do SDK. Uma única atualização pode incluir posicionamentos que já estavam em cache (por exemplo, de uma atualização anterior, outra tela ou trabalho automático do SDK), não apenas os IDs de posicionamento da sua chamada `requestBannersRefresh` mais recente. Se você se importa apenas com determinados posicionamentos, verifique o ID de posicionamento de cada banner no seu ouvinte e ignore o restante. Quando tiver registrado seu ouvinte, chame `requestBannersRefresh` para os posicionamentos que deseja sincronizar da Braze.
{% endalert %}

{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> placementIds = new ArrayList<>();
placementIds.add("global_banner");
placementIds.add("navigation_square_banner");
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val placementIds = listOf("global_banner", "navigation_square_banner")
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
// Always refresh after your subscriber is registered
Braze.getInstance(context).requestBannersRefresh(placementIds)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Etapa 4: Inserir usando o ID do posicionamento {#insertBanner}

{% alert tip %}
Para um tutorial completo passo a passo, confira [Exibindo um Banner por ID de posicionamento]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners).
{% endalert %}

{% tabs %}
{% tab Web %}

Crie um elemento contêiner para o Banner. Certifique-se de definir sua largura e altura.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Se você estiver usando JavaScript puro com o SDK Web da Braze, chame o método [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) para substituir o HTML interno do elemento contêiner.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
  baseUrl: "sdk-base-url",
  allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
  // get this placement's banner. If it's `null` the user did not qualify for one.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  // choose where in the DOM you want to insert the banner HTML
  const container = document.getElementById("global-banner-container");

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}

{% subtab React %}
Se você estiver usando React com o SDK Web da Braze, chame o método [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) com um `ref` para substituir o HTML interno do elemento contêiner.

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Para rastrear impressões, certifique-se de chamar `insertBanner` para `isControl`. Você pode então ocultar ou colapsar seu contêiner depois.
{% endalert %}

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// UIKit implementation:
// If you simply want the Banner view, initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// SwiftUI implementation:
// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}
Para obter o Banner no código Java, use:

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Você pode criar Banners no layout das suas views Android incluindo este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Se estiver usando Android Views, use este XML:

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Para usar Jetpack Compose, adicione o artefato `com.braze:android-sdk-jetpack-compose` ao módulo do seu app. Use a mesma versão das suas outras dependências do SDK Android da Braze. Esse módulo é separado do `android-sdk-ui` e inclui o composable [`Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html) em `com.braze.jetpackcompose.banners`.

{% alert note %}
Algumas bibliotecas de UI do Compose definem seu próprio composable `Banner`. Importe `com.braze.jetpackcompose.banners.Banner` explicitamente para garantir que você está chamando a API da Braze.
{% endalert %}

```kotlin
import com.braze.jetpackcompose.banners.Banner

@Composable
fun myBannerSlot() {
    Banner(placementId = "global_banner")
}
```

Opcionalmente, passe `heightCallback` para receber a altura renderizada em dp quando o tamanho do banner mudar. Para referência, consulte a [documentação KDoc do `Banner`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.jetpackcompose.banners/-banner.html).

Se você não adicionar o módulo Jetpack Compose, envolva [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html) em [`AndroidView`](https://developer.android.com/reference/kotlin/androidx/compose/ui/viewinterop/AndroidView):

```kotlin
import android.view.ViewGroup
import androidx.compose.runtime.Composable
import androidx.compose.ui.viewinterop.AndroidView
import com.braze.ui.banners.BannerView

@Composable
fun myBannerSlot() {
    AndroidView(
        factory = { context ->
            BannerView(context, "global_banner").apply {
                layoutParams = ViewGroup.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT
                )
            }
        },
        update = { it.placementId = "global_banner" }
    )
}
```

Para obter o Banner em Kotlin, use:
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

Se você estiver usando a [Nova Arquitetura do React Native](https://reactnative.dev/architecture/landing-page), será necessário registrar `BrazeBannerView` como um componente Fabric no seu `AppDelegate.mm`.

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```
Para a integração mais simples, adicione o seguinte trecho de JavaScript XML (JSX) na sua hierarquia de views, fornecendo apenas o ID do posicionamento.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

Para obter o modelo de dados do Banner no React Native, ou para verificar a presença desse posicionamento no cache do seu usuário, use:

```javascript
const banner = await Braze.getBanner("global_banner");
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}
Para a integração mais simples, adicione o seguinte widget na sua hierarquia de views, fornecendo apenas o ID do posicionamento.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Você pode usar o método `getBanner` para verificar a presença desse posicionamento no cache do seu usuário.

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Etapa 5: Envie um Banner de teste (opcional) {#handling-test-cards}

Antes de lançar uma Campaign de Banner, você pode [enviar um Banner de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=banners) para verificar sua integração. Banners de teste são armazenados em um cache separado na memória e não persistem entre reinicializações do app. Embora nenhuma configuração extra seja necessária, seu dispositivo de teste deve ser capaz de receber notificações por push em primeiro plano para que possa exibir o teste.

{% alert note %}
Banners de teste são como qualquer outro banner, exceto que são removidos na próxima sessão do app.
{% endalert %}

## Registrar impressões {#log-impressions}

A Braze registra automaticamente impressões para Banners que estão visíveis quando você usa métodos do SDK para inserir um Banner&#8212;portanto, não há necessidade de rastrear impressões manualmente.

## Registrar cliques {#logging-clicks}

O método usado para registrar cliques em Banners depende de como seu Banner é renderizado e onde seu manipulador de cliques está localizado.

### Conteúdo padrão do Banner (automático) {#standard-banner-content-automatic}

Se você estiver usando métodos padrão do SDK, prontos para uso, para inserir Banners, e seu Banner usar componentes padrão do editor (imagens, botões, texto), os cliques são rastreados automaticamente. O SDK anexa ouvintes de cliques a esses elementos, e nenhum código adicional é necessário.

### Blocos de código personalizado {#custom-code-blocks}

Se seu Banner usar o bloco de editor **Custom Code** no dashboard da Braze, você deve usar `brazeBridge.logClick()` para registrar cliques a partir desse HTML personalizado. Isso se aplica mesmo ao usar métodos do SDK para renderizar o Banner, porque o SDK não pode anexar ouvintes automaticamente a elementos dentro do seu código personalizado.

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Para a referência completa, veja [Código personalizado e ponte JavaScript para Banners]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#custom-code). O `brazeBridge` fornece uma camada de comunicação entre o HTML interno do Banner e o SDK da Braze pai.

### Implementações de UI personalizadas (headless) {#custom-ui-implementations-headless}

Se você estiver construindo uma UI totalmente personalizada usando as [propriedades personalizadas](#custom-properties) do Banner em vez de renderizar o HTML do Banner, você deve registrar manualmente cliques e impressões a partir do código do seu aplicativo. Como o SDK não está renderizando o Banner, ele não tem como rastrear automaticamente as interações com seus elementos de UI personalizados.

Para assinaturas de métodos e detalhes completos, consulte a [documentação de referência do SDK da Braze]({{site.baseurl}}/developer_guide/references).

#### Registrar impressões {#logging-impressions}

Chame o método de impressão de Banner da plataforma quando sua UI personalizada considerar o Banner como "visualizado". Construa uma lógica robusta para o que conta como uma impressão, a fim de evitar eventos duplicados — por exemplo, registre apenas quando o Banner entrar na viewport (ou equivalente), e não registre novamente quando o mesmo Banner voltar a aparecer na tela ao rolar ou quando seu componente re-renderizar sem um novo evento de visualização.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
const banner = braze.getBanner("placement_id_homepage_top");
if (banner) {
  braze.logBannerImpressions([banner]);
}
```
[Referência do SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerimpressions)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top")
```
{% endsubtab %}
{% subtab Java %}
```java
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.getInstance(context).logBannerImpression("placement_id_homepage_top");
```
{% endsubtab %}
{% endsubtabs %}
[Referência do SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-impression.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log an impression on it (for example, once when it enters viewport)
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logImpression()
}
```
[Referência do SDK Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logimpression())
{% endtab %}
{% tab React Native %}
```javascript
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
Braze.logBannerImpression("placement_id_homepage_top");
```
Consulte o [repositório do SDK React Native](https://github.com/braze-inc/braze-react-native-sdk) para as assinaturas de métodos mais recentes.
{% endtab %}
{% tab Flutter %}
```dart
// Log impression when your custom UI considers the banner viewed (for example, once when it enters viewport)
braze.logBannerImpression("placement_id_homepage_top");
```
[Referência do SDK Flutter](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerImpression.html)
{% endtab %}
{% endtabs %}

#### Registrar cliques

Chame o método de clique de Banner da plataforma quando o usuário tocar no seu Banner personalizado (ou em um botão específico). Passe o `buttonId` opcional quando o clique for em um botão específico, para que a análise de dados possa atribuir o clique corretamente.

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

// Log click
braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
[Referência do SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logbannerclick)
{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Kotlin %}
```kotlin
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId)  // buttonID parameter can be null
```
{% endsubtab %}
{% subtab Java %}
```java
// Log click
Braze.getInstance(context).logBannerClick("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
{% endsubtab %}
{% endsubtabs %}
[Referência do SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-banner-click.html)
{% endtab %}
{% tab Swift %}
```swift
// Retrieve a banner and log a click on it
braze.banners.getBanner(for: "placement_id_homepage_top") { banner in
  banner?.context.logClick(buttonId: buttonId)  // buttonID is optional
}
```
[Referência do SDK Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/banner/context-swift.class/logclick(buttonid:))
{% endtab %}
{% tab React Native %}
```javascript
// Log click
Braze.logBannerClick("placement_id_homepage_top", buttonId);  // buttonID is optional
```
Consulte o [repositório do SDK React Native](https://github.com/braze-inc/braze-react-native-sdk) para as assinaturas de métodos mais recentes.
{% endtab %}
{% tab Flutter %}
```dart
// Log click
braze.logBannerClicked("placement_id_homepage_top", buttonId);  // buttonID parameter can be null
```
[Referência do SDK Flutter](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazePlugin/logBannerClicked.html)
{% endtab %}
{% endtabs %}

## Registrar dispensas {#log-dismissals}

As dispensas de Banner removem programaticamente um Banner de um posicionamento quando um usuário o dispensa ativamente. Uma vez dispensado, o Banner é suprimido para aquele usuário. Na próxima vez que a lista de posicionamentos for atualizada, um novo banner será retornado se o usuário for elegível para um.

### Pré-requisitos

Estas são as versões mínimas do SDK necessárias para registrar dispensas de Banner:

{% sdk_min_versions swift:14.1.0 android:42.1.0 web:6.7.1 %}

### Integrações {#integrations}

#### Integrações padrão de Banner (editor de arrastar e soltar) {#standard-banner-integrations-drag-and-drop-editor}

Se seu Banner usar o editor de arrastar e soltar e incluir um componente de botão de dispensa, nenhum código adicional é necessário. Quando um usuário clicar no botão de dispensa, a mensagem será ocultada, uma dispensa será acionada e um evento de dispensa será registrado para análise de dados.

#### Blocos de código personalizado

Se seu Banner usar o bloco de editor **Custom Code**, você pode acionar uma dispensa diretamente de dentro do HTML do Banner usando `brazeBridge.closeMessage()`.

```html
<button onclick="brazeBridge.closeMessage()">
  Dismiss
</button>
```

#### Dispensar um banner programaticamente {#dismiss-a-banner-programmatically}

Se você estiver usando o `BrazeBannerView` padrão com o botão de dispensa criado no editor de arrastar e soltar, nenhum código adicional é necessário; a dispensa é tratada automaticamente.

Para integrações de UI personalizadas, você pode chamar o método de dispensa diretamente na sua instância da Braze para dispensar programaticamente um banner e registrar um evento de dispensa. O método de dispensa pode ser chamado várias vezes com segurança — o SDK ignora chamadas duplicadas para o mesmo banner.

Estas são as versões mínimas do SDK necessárias para dispensar um banner programaticamente:

{% sdk_min_versions swift:15.1.0 android:42.3.0 web:6.9.0 reactnative:22.0.0 flutter:20.0.0 %}

{% tabs %}
{% tab Web %}
Passe o objeto `Banner` para `braze.dismissBanner()`. Você pode obter o objeto `Banner` a partir de `braze.getAllBanners()` ou de um retorno de chamada de `subscribeToBannersUpdates`.

{% subtabs %}
{% subtab JavaScript %}
```javascript
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
  braze.dismissBanner(banner);
}
```
{% endsubtab %}
{% subtab React %}
```typescript
import * as braze from "@braze/web-sdk";

const banners = braze.getAllBanners();
const banner = banners["global_banner"];

if (banner) {
  braze.dismissBanner(banner);
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
Braze.getInstance(context).dismissBanner("your-placement-id");
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
Braze.getInstance(context).dismissBanner("your-placement-id")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift %}

Use `dismiss()` no contexto do banner quando disponível. Esse método é idempotente e dispara o retorno de chamada `onDismiss` automaticamente. Se o contexto não estiver disponível, chame `dismiss(using:)` diretamente no banner. Ambos os métodos devem ser chamados a partir da thread principal.

```swift
// Preferred: dismiss via context.
banner.context?.dismiss()

// Fallback: if context is unavailable.
banner.dismiss(using: braze)
```

Em Objective-C, esses métodos estão disponíveis como `[banner.context dismiss]` e `[banner dismissUsing:braze]`.

{% endtab %}

{% tab React Native %}
```javascript
Braze.dismissBanner("your-placement-id");
```
{% endtab %}

{% tab Flutter %}
```dart
braze.dismissBanner("your-placement-id");
```
{% endtab %}
{% endtabs %}

### Registrar análise de dados personalizada na dispensa do banner {#log-custom-analytics-on-banner-dismissal}

Para executar lógica personalizada quando um banner é dispensado — como registrar análise de dados — use o retorno de chamada de dispensa do seu SDK. O retorno de chamada recebe um objeto de evento com o `placementId`, `stableKey` e `trackingId` do banner.

{% tabs %}
{% tab Web %}
Use [`Banner.subscribeToDismissedEvent()`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.banner.html#subscribetodismissedevent) para executar lógica personalizada quando um banner específico é dispensado. Inscreva-se no evento antes de exibir o banner.

{% alert note %}
`Banner.subscribeToDismissedEvent()` requer o SDK Web 6.9.0 ou posterior. Em versões anteriores, use `braze.subscribeToBannersUpdates()` e detecte a dispensa verificando se o banner não está mais presente no mapa de banners atualizado.
{% endalert %}

{% subtabs %}
{% subtab JavaScript %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  const banner = banners["global_banner"];

  if (banner) {
    banner.subscribeToDismissedEvent(() => {
      // Run any custom logic here, such as logging custom analytics
      console.log("Banner was dismissed");
    });
  }
});

braze.requestBannersRefresh(["global_banner"]);
```
{% endsubtab %}
{% subtab React %}
```typescript
import { useEffect } from "react";
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    const banner = banners["global_banner"];

    if (banner) {
      banner.subscribeToDismissedEvent(() => {
        // Run any custom logic here, such as logging custom analytics
        console.log("Banner was dismissed");
      });
    }
  });

  braze.requestBannersRefresh(["global_banner"]);

  return () => {
    braze.removeSubscription(subscriptionId);
  };
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Android %}
Defina a propriedade opcional [`onDismissCallback`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/on-dismiss-callback.html) em [`BannerView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.banners/-banner-view/index.html).

{% subtabs %}
{% subtab Java %}

```java
import android.util.Log;
import com.braze.ui.banners.BannerView;
import kotlin.Unit;

// After obtaining your BannerView instance (for example from XML via findViewById, or `new BannerView(context, "global_banner")`)

bannerView.setOnDismissCallback((snapshot) -> {
  Log.d(TAG, "placementId: " + snapshot.getPlacementId()
    + ", stableKey: " + snapshot.getStableKey()
    + ", trackingId: " + snapshot.getTrackingId());

  // Run any custom logic here, such as logging custom analytics
  return Unit.INSTANCE;
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
import android.util.Log
import com.braze.ui.banners.BannerView

// After obtaining your BannerView instance (for example via findViewById or `BannerView(context, "global_banner")`)

bannerView.onDismissCallback = { snapshot ->
  Log.d(TAG, "placementId: ${snapshot.placementId}, stableKey: ${snapshot.stableKey}, trackingId: ${snapshot.trackingId}")

  // Run any custom logic here, such as logging custom analytics
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift %}
```swift
// After initializing your banner view instance using UIKit or SwiftUI

bannerView.onDismiss = { event in
  print("Banner dismissed — placementId: \(event.placementId ?? "unknown")")
  print("  stableKey: \(event.stableKey ?? "unknown")")
  print("  trackingId: \(event.trackingId ?? "unknown")")

  // Run any custom logic here, such as logging custom analytics
}
```
{% endtab %}

{% tab React Native %}
Defina a prop `onDismiss` em `Braze.BrazeBannerView` para executar lógica personalizada quando um banner é dispensado.

```javascript
import Braze from "@braze/react-native-sdk";

<Braze.BrazeBannerView
  placementId="global_banner"
  onDismiss={(event) => {
    console.log("placementId:", event.placementId, "stableKey:", event.stableKey, "trackingId:", event.trackingId);
    // Run any custom logic here, such as logging custom analytics
  }}
/>
```
{% endtab %}

{% tab Flutter %}
Defina o parâmetro `onDismiss` em `BrazeBannerView` para executar lógica personalizada quando um banner é dispensado.

```dart
BrazeBannerView(
  placementId: 'global_banner',
  onDismiss: (BrazeBannerDismissEvent event) {
    print('placementId: ${event.placementId}, stableKey: ${event.stableKey}, trackingId: ${event.trackingId}');
    // Run any custom logic here, such as logging custom analytics
  },
)
```
{% endtab %}
{% endtabs %}

### Limite de armazenamento de dispensas pendentes {#pending-dismissal-storage-cap}

Os eventos de dispensa são armazenados localmente como entradas pendentes até que possam ser sincronizados com o servidor da Braze na próxima chamada de `requestBannersRefresh`.

{% alert warning %}
Em casos raros em que um grande número de dispensas se acumula sem uma sincronização bem-sucedida, dispensas pendentes mais antigas podem ser descartadas. Se isso ocorrer, Banners previamente dispensados podem reaparecer até que a próxima sincronização seja concluída com sucesso. Para minimizar esse risco, chame `requestBannersRefresh` sempre que seu app recuperar a conectividade de rede.
{% endalert %}

## Dimensões e tamanhos {#dimensions-and-sizing}

Aqui está o que você precisa saber sobre dimensões e tamanhos do Banner:

- Embora o criador permita que você visualize Banners em diferentes dimensões, essa informação não é salva ou enviada para o SDK.
- O HTML ocupará toda a largura do contêiner em que for renderizado.
- Recomendamos criar um elemento de dimensão fixa e testar essas dimensões no criador.

## Propriedades personalizadas {#custom-properties}

Você pode usar propriedades personalizadas da sua Campaign de Banner para recuperar dados chave-valor através do SDK e modificar o comportamento ou a aparência do seu app. Por exemplo, você poderia:

- Enviar metadados para suas análises de terceiros ou integrações.
- Usar metadados como um `timestamp` ou objeto JSON para acionar lógica condicional.
- Controlar o comportamento de um banner com base em metadados incluídos como `ratio` ou `format`.

### Pré-requisitos

Você precisará [adicionar propriedades personalizadas]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#custom-properties) à sua Campaign de Banner. Além disso, estas são as versões mínimas do SDK necessárias para acessar propriedades personalizadas:

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### Acessar propriedades personalizadas {#access-custom-properties}

Para acessar as propriedades personalizadas de um banner, use um dos seguintes métodos com base no tipo da propriedade definido no dashboard. Se a chave não corresponder a uma propriedade desse tipo ou não existir, o método retorna `null`.

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');

  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');

  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');

  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');

  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');

  // Get the JSON object property
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');

  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}