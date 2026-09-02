{% alert important %}
A partir do iOS 14, geofences não funcionam de forma confiável para usuários que optam por dar apenas permissão de localização aproximada.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Configurando geofences {#setting-up-geofences}

### Etapa 1: Ativar na Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Etapa 2: Ative os serviços de localização do seu app {#step-2-enable-your-apps-location-services}

Por padrão, os serviços de localização da Braze não estão ativados. Para ativá-los no seu app, complete as seguintes etapas. Para um tutorial passo a passo, veja [Tutorial: Localizações e Geofences da Braze](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### Etapa 2.1: Adicione o módulo `BrazeLocation` {#step-21-add-the-brazelocation-module}

No Xcode, abra a guia **General**. Em **Frameworks, Libraries, and Embedded Content**, adicione o módulo `BrazeLocation`.

![Adicione o módulo BrazeLocation no seu projeto Xcode]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Etapa 2.2: Atualize seu `Info.plist` {#step-22-update-your-infoplist}

No seu `info.plist`, atribua um valor `String` a uma das seguintes chaves que descrevem por que seu aplicativo precisa rastrear a localização. Essa string será exibida quando seus usuários forem solicitados a permitir serviços de localização, então certifique-se de explicar claramente o valor de ativar esse recurso para seu app.

- `NSLocationAlwaysAndWhenInUseUsageDescription`
- `NSLocationWhenInUseUsageDescription`

![Strings de localização do Info.plist no Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
A Apple descontinuou `NSLocationAlwaysUsageDescription`. Para saber mais, veja a [documentação do desenvolvedor da Apple](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Etapa 3: Ative geofences no seu código {#step-3-enable-geofences-in-your-code}

No código do seu app, ative geofences definindo `location.geofencesEnabled` como `true` no objeto `configuration` que inicializa a instância [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/). Para outras opções de configuração `location`, veja a [referência do SDK Braze Swift](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Additional configuration customization...

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### Etapa 3.1: Ativar relatórios em segundo plano (opcional) {#step-31-enable-background-reporting-optional}

Por padrão, eventos de geofence são monitorados apenas se seu app estiver em primeiro plano ou tiver autorização `Always`, que monitora todos os estados do aplicativo.

No entanto, você também pode optar por monitorar eventos de geofence quando seu app estiver em segundo plano ou tiver [autorização `When In Use`](#swift_request-authorization).

Para monitorar esses eventos adicionais de geofence, abra seu projeto no Xcode e vá para **Signing & Capabilities**. Em **Background Modes**, marque **Location updates**.

![No Xcode, Background Mode > Location Updates]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

Em seguida, ative `allowBackgroundGeofenceUpdates` no código do seu app. Isso permite que a Braze estenda o status "When In Use" do seu app, monitorando continuamente as atualizações de localização. Essa configuração só funciona quando seu app está em segundo plano. Quando o app é reaberto, todos os processos em segundo plano existentes são pausados e os processos em primeiro plano são priorizados.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
Para evitar consumo excessivo de bateria e limitação de frequência, configure `distanceFilter` para um valor que atenda às necessidades específicas do seu app. Configurar `distanceFilter` para um valor mais alto impede que seu app solicite a localização do usuário com muita frequência.
{% endalert %}

### Etapa 4: Solicitar autorização {#request-authorization}

Ao solicitar autorização de um usuário, peça autorização `When In Use` ou `Always`.

{% tabs local %}
{% tab When In Use %}
Para solicitar autorização `When In Use`, use o método `requestWhenInUseAuthorization()`:

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Always %}
Por padrão, `requestAlwaysAuthorization()` só concede ao seu app autorização `When In Use` e solicitará novamente ao seu usuário a autorização `Always` após algum tempo.

No entanto, você pode optar por solicitar imediatamente ao seu usuário, chamando primeiro `requestWhenInUseAuthorization()` e depois chamando `requestAlwaysAuthorization()` após receber sua autorização inicial `When In Use`.

{% alert important %}
Você só pode solicitar autorização `Always` imediatamente uma única vez.
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Solicitar geofences manualmente {#manually-request-geofences}

Quando o SDK da Braze solicita geofences do backend, ele reporta a localização atual do usuário e recebe geofences que são determinadas como otimamente relevantes com base na localização reportada.

Para controlar a localização que o SDK reporta para receber as geofences mais relevantes, você pode solicitar geofences manualmente fornecendo as coordenadas desejadas.

### Etapa 1: Defina `automaticGeofenceRequests` como `false` {#step-1-set-automaticgeofencerequests-to-false}

Você pode desativar solicitações automáticas de geofence no objeto `configuration` passado para [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)). Defina `automaticGeofenceRequests` como `false`.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### Etapa 2: Chame `requestGeofences` manualmente {#step-2-call-requestgeofences-manually}

No seu código, solicite geofences com a latitude e longitude apropriadas.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

## Perguntas frequentes (FAQ) {#faq}

### Por que não estou recebendo geofences no meu dispositivo? {#why-am-i-not-receiving-geofences-on-my-device}

Para confirmar se os geofences estão sendo recebidos no seu dispositivo, primeiro use a [ferramenta Depurador do SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para verificar os registros do SDK. Você poderá ver se os geofences estão sendo recebidos com sucesso do servidor e se há algum erro notável.

Outras possíveis razões pelas quais os geofences podem não ser recebidos no seu dispositivo:

#### Limitações do sistema operacional iOS {#ios-operating-system-limitations}

O sistema operacional iOS permite armazenar até 20 geofences para um determinado app. Com as geofences ativadas, a Braze usará alguns desses 20 slots disponíveis.

Para evitar interrupções acidentais ou indesejadas em outras funcionalidades relacionadas a geofences no seu app, você deve ativar os geofences de localização para aplicativos individuais no dashboard. Para que nossos serviços de localização funcionem corretamente, verifique se seu app não está usando todos os slots de geofence disponíveis.

#### Limite de frequência {#rate-limiting}

A Braze tem um limite de 1 atualização de geofence por sessão para evitar solicitações desnecessárias.

### Como funciona se estou usando recursos de geofence da Braze e de terceiros? {#how-does-it-work-if-i-am-using-both-braze-and-non-braze-geofence-features}

Como mencionado acima, o iOS permite que um único app armazene um máximo de 20 geofences. Esse armazenamento é compartilhado entre geofences da Braze e de terceiros e é gerenciado pelo [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager).

Por exemplo, se seu app contém 20 geofences de terceiros, não haverá armazenamento para rastrear geofences da Braze (ou vice-versa). Para receber novos geofences, você precisará usar as [APIs de localização da Apple](https://developer.apple.com/documentation/corelocation) para parar de monitorar alguns dos geofences existentes no dispositivo.

### A funcionalidade de geofences pode ser usada enquanto um dispositivo está offline? {#can-the-geofences-feature-be-used-while-a-device-is-offline}

Um dispositivo precisa estar conectado à internet apenas quando uma atualização ocorre. Uma vez que ele tenha recebido com sucesso geofences do servidor, é possível registrar uma entrada ou saída de geofence mesmo que o dispositivo esteja offline. Isso ocorre porque a localização de um dispositivo opera separadamente da sua conectividade com a internet.

Por exemplo, digamos que um dispositivo recebeu e registrou com sucesso geofences no início da sessão e fica offline. Se entrar em uma dessas geofences registradas, isso pode disparar uma Campaign da Braze.

### Por que as geofences não são monitoradas quando meu app está em segundo plano/terminado? {#why-are-geofences-not-monitored-when-my-app-is-backgroundedterminated}

Sem autorização `Always`, a Apple restringe os serviços de localização de funcionar enquanto um app não está em uso. Isso é imposto pelo sistema operacional e está fora do controle do SDK da Braze. Embora a Braze ofereça configurações separadas para executar serviços enquanto o app está em segundo plano, não há como contornar essas restrições para apps que são terminados sem receber autorização explícita do usuário.