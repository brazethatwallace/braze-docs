---
page_order: 1.2
nav_title: Autenticación
article_title: Configurar la autenticación para el SDK or kit de desarrollo de software de Braze
description: "Este artículo de referencia cubre la autenticación del SDK or kit de desarrollo de software y cómo habilitar esta característica en el SDK or kit de desarrollo de software de Braze."
platform:
  - iOS
  - Android
  - Web

---

# Configurar la autenticación del SDK or kit de desarrollo de software {#set-up-sdk-authentication}

> La autenticación del SDK or kit de desarrollo de software te permite proporcionar una prueba criptográfica (generada en el servidor) a las solicitudes del SDK or kit de desarrollo de software realizadas en nombre de usuarios que han iniciado sesión.

## Cómo funciona {#how-it-works}

Después de habilitar esta característica en tu aplicación, puedes configurar el panel de Braze para que rechace cualquier solicitud con un JSON Web Token (JWT) no válido o ausente, lo que incluye:

- Enviar eventos personalizados, atributos, compras y datos de sesión
- Crear nuevos usuarios en tu espacio de trabajo de Braze
- Actualizar atributos estándar del perfil de usuario
- Recibir o desencadenar mensajes

Ahora puedes evitar que los usuarios autenticados que han iniciado sesión utilicen la clave de API de SDK or kit de desarrollo de software de tu aplicación para realizar acciones maliciosas, como suplantar a otros usuarios.

## Configuración de la autenticación {#setting-up-authentication}

### Paso 1: Configura tu servidor {#server-side-integration}

#### Paso 1.1: Genera un par de claves pública/privada {#generate-keys}

Genera un par de claves pública/privada RSA256. La clave pública se añadirá eventualmente al panel de Braze, mientras que la clave privada debe almacenarse de forma segura en tu servidor.

Recomendamos una clave RSA de 2048 bits para su uso con el algoritmo JWT RS256.

{% alert warning %}
Recuerda mantener tus claves privadas en _privado_. Nunca expongas ni codifiques de forma fija tu clave privada en tu aplicación o sitio web. Cualquier persona que conozca tu clave privada puede suplantar o crear usuarios en nombre de tu aplicación.
{% endalert %}

#### Paso 1.2: Crea un JSON Web Token para el usuario actual {#create-jwt}

Una vez que tengas tu clave privada, tu aplicación del lado del servidor debe usarla para devolver un JWT a tu aplicación o sitio web para el usuario que ha iniciado sesión actualmente.

Normalmente, esta lógica podría ir donde tu aplicación solicita habitualmente el perfil del usuario actual; como un endpoint de inicio de sesión o donde tu aplicación actualiza el perfil del usuario actual.

Al generar el JWT, se esperan los siguientes campos:

**Encabezado JWT**

| Campo | Obligatorio | Descripción                         |
| ----- | -------- | ----------------------------------- |
| `alg` | Sí  | El algoritmo compatible es `RS256`. |
| `typ` | Sí  | El tipo debe ser igual a `JWT`.        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 1.2: Crea un JSON Web Token para el usuario actual" }

**Carga útil JWT**

| Campo | Obligatorio | Descripción                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | Sí  | El "subject" debe ser igual al ID de usuario que proporcionas al SDK or kit de desarrollo de software de Braze al llamar a `changeUser`  |
| `exp` | Sí | La "expiration" de cuándo deseas que este token expire, como una marca de tiempo Unix en segundos (por ejemplo, `1893456000` para el 1 de enero de 2030).                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 1.2: Crea un JSON Web Token para el usuario actual" }

{% alert tip %}
Para obtener más información sobre los JSON Web Tokens, o para explorar las muchas bibliotecas de código abierto que simplifican este proceso de firma, consulta [https://jwt.io](https://jwt.io).
{% endalert %}

### Paso 2: Configura el SDK or kit de desarrollo de software {#sdk-integration}

Esta característica está disponible a partir de las siguientes [versiones del SDK or kit de desarrollo de software]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
Para integraciones de iOS, esta página detalla los pasos para el SDK or kit de desarrollo de software Swift de Braze. Para ver un ejemplo de uso en el SDK or kit de desarrollo de software legacy de iOS de Appboy, consulta [este archivo](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) y [este archivo](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m).
{% endalert %}

#### Paso 2.1: Habilita la autenticación en el SDK or kit de desarrollo de software de Braze. {#step-21-enable-authentication-in-the-braze-sdk}

Cuando esta característica está habilitada, el SDK or kit de desarrollo de software de Braze añadirá el último JWT conocido del usuario actual a las solicitudes de red realizadas a los servidores de Braze.

{% alert note %}
No te preocupes, inicializar con esta opción por sí sola no afectará la recopilación de datos de ninguna manera, hasta que comiences a [aplicar la autenticación](#braze-dashboard) dentro del panel de Braze.
{% endalert %}

{% tabs %}
{% tab Web %}
Al llamar a `initialize`, establece la propiedad opcional `enableSdkAuthentication` en `true`.
```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab React Native %}
La autenticación del SDK or kit de desarrollo de software debe habilitarse durante la inicialización nativa del SDK or kit de desarrollo de software. Añade la siguiente configuración a tu código nativo de iOS y Android:

**iOS (AppDelegate.swift)**

```swift
import BrazeKit
import braze_react_native_sdk

let configuration = Braze.Configuration(
  apiKey: "{YOUR-BRAZE-API-KEY}",
  endpoint: "{YOUR-BRAZE-ENDPOINT}"
)
configuration.api.sdkAuthentication = true
let braze = BrazeReactBridge.perform(
  #selector(BrazeReactBridge.initBraze(_:)),
  with: configuration
).takeUnretainedValue() as! Braze
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Después de habilitar la autenticación del SDK or kit de desarrollo de software en la capa nativa, puedes usar los métodos de JavaScript de React Native que se muestran en los siguientes pasos.
{% endtab %}
{% tab Java %}
Al configurar la instancia de Braze, llama a `setIsSdkAuthenticationEnabled` con `true`.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

Alternativamente, puedes añadir `<bool name="com_braze_sdk_authentication_enabled">true</bool>` a tu braze.xml.
{% endtab %}
{% tab KOTLIN %}
Al configurar la instancia de Braze, llama a `setIsSdkAuthenticationEnabled` con `true`.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

Alternativamente, puedes añadir `<bool name="com_braze_sdk_authentication_enabled">true</bool>` a tu braze.xml.
{% endtab %}
{% tab Objective-C %}
Para habilitar la autenticación del SDK or kit de desarrollo de software, establece la propiedad `configuration.api.sdkAuthentication` de tu objeto `BRZConfiguration` en `YES` antes de inicializar la instancia de Braze:

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
Para habilitar la autenticación del SDK or kit de desarrollo de software, establece la propiedad `configuration.api.sdkAuthentication` de tu objeto `Braze.Configuration` en `true` al inicializar el SDK or kit de desarrollo de software:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
Actualmente, la autenticación del SDK or kit de desarrollo de software debe habilitarse como parte de la inicialización del SDK or kit de desarrollo de software en código nativo de iOS y Android. Para habilitar la autenticación del SDK or kit de desarrollo de software en el SDK or kit de desarrollo de software de Flutter, sigue las integraciones para iOS y Android desde las otras pestañas. Después de habilitar la autenticación del SDK or kit de desarrollo de software, el resto de la característica puede integrarse en Dart.
{% endtab %}
{% tab Flutter %}
La autenticación del SDK or kit de desarrollo de software debe habilitarse como parte de la inicialización del SDK or kit de desarrollo de software en código nativo de iOS y Android. Cuando está habilitada en la capa nativa, puedes usar los métodos del SDK or kit de desarrollo de software de Flutter para pasar la firma JWT.

**iOS**

Para habilitar la autenticación del SDK or kit de desarrollo de software, establece la propiedad `configuration.api.sdkAuthentication` en `true` en tu código nativo de iOS:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Después de habilitar la autenticación del SDK or kit de desarrollo de software en la capa nativa, puedes usar los métodos del SDK or kit de desarrollo de software de Flutter que se muestran en los siguientes pasos.
{% endtab %}
{% tab Unity %}
La autenticación del SDK or kit de desarrollo de software debe habilitarse durante la inicialización nativa del SDK or kit de desarrollo de software. Añade la siguiente configuración a tu código nativo de iOS y Android:

**iOS**

Establece la propiedad `SDKAuthenticationEnabled` en `true` en tu archivo de configuración:

```xml
<key>SDKAuthenticationEnabled</key>
<true/>
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Después de habilitar la autenticación del SDK or kit de desarrollo de software en la capa nativa, puedes usar los métodos de C# de Unity que se muestran en los siguientes pasos.
{% endtab %}
{% tab Cordova %}
La autenticación del SDK or kit de desarrollo de software debe habilitarse durante la inicialización nativa del SDK or kit de desarrollo de software. Añade la siguiente configuración a tu código nativo de iOS y Android:

**iOS**

Para habilitar la autenticación del SDK or kit de desarrollo de software, establece la propiedad `enableSDKAuthentication` en `true` en tu `config.xml`:

```xml
<preference name="com.braze.ios_enable_sdk_authentication" value="true" />
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Después de habilitar la autenticación del SDK or kit de desarrollo de software en la capa nativa, puedes usar los métodos de JavaScript de Cordova que se muestran en los siguientes pasos.
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
La autenticación del SDK or kit de desarrollo de software debe habilitarse durante la inicialización nativa del SDK or kit de desarrollo de software. Configura la autenticación del SDK or kit de desarrollo de software por separado para iOS y Android:

**iOS**

Para habilitar la autenticación del SDK or kit de desarrollo de software, establece la propiedad `configuration.Api.SdkAuthentication` en `true` al inicializar el SDK or kit de desarrollo de software:

```csharp
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Después de habilitar la autenticación del SDK or kit de desarrollo de software, puedes usar los métodos de .NET MAUI que se muestran en los siguientes pasos.
{% endtab %}
{% tab Expo %}
Al usar el plugin de Braze Expo, establece la propiedad `enableSdkAuthentication` en `true` en la configuración de tu aplicación. Esto configura automáticamente la autenticación del SDK or kit de desarrollo de software en las capas nativas de iOS y Android sin requerir cambios manuales en el código nativo.

**app.json o app.config.js**

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "enableSdkAuthentication": true
        }
      ]
    ]
  }
}
```

Después de habilitar la autenticación del SDK or kit de desarrollo de software en la configuración de tu aplicación, puedes usar los métodos de JavaScript de React Native que se muestran en la pestaña de React Native para los siguientes pasos.

{% alert note %}
Para un ejemplo completo de implementación, consulta la [aplicación de ejemplo del plugin de Braze Expo](https://github.com/braze-inc/braze-expo-plugin/blob/main/example/components/Braze.tsx) en GitHub.
{% endalert %}
{% endtab %}
{% endtabs %}

#### Paso 2.2: Establece el JWT del usuario actual {#step-22-set-the-current-users-jwt}

Siempre que tu aplicación llame al método `changeUser` de Braze, proporciona también el JWT que fue [generado del lado del servidor](#braze-dashboard).

También puedes configurar el token para que se actualice a mitad de sesión para el usuario actual.

{% alert note %}
Ten en cuenta que `changeUser` solo debe llamarse cuando el ID de usuario haya _cambiado realmente_. No debes usar este método como una forma de actualizar el token de autenticación (JWT) si el ID de usuario no ha cambiado.
{% endalert %}

{% tabs %}
{% tab Web %}
Proporciona el JWT al llamar a [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```javascript
import * as braze from "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab React Native %}

Proporciona el JWT al llamar a [`changeUser`](https://braze-inc.github.io/braze-react-native-sdk/classes/Braze.Braze-1.html#changeUser):

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Proporciona el JWT al llamar a [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Proporciona el JWT al llamar a [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

Proporciona el JWT al llamar a [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

Proporciona el JWT al llamar a [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```

{% alert note %}
`changeUser` retorna inmediatamente en el hilo que lo llama. La firma de autenticación del SDK or kit de desarrollo de software proporcionada aquí se adjunta después de que se completa el trabajo de cambio de usuario.
{% endalert %}

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

Proporciona el JWT al llamar a [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
O, cuando hayas actualizado el token del usuario a mitad de sesión:

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% tab Flutter %}

Proporciona el JWT al llamar a `changeUser`:

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.changeUser("NEW-USER-ID", sdkAuthSignature: "JWT-FROM-SERVER");
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Unity %}

Proporciona el JWT al llamar a `ChangeUser`:

```csharp
BrazeBinding.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```csharp
BrazeBinding.SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Cordova %}

Proporciona el JWT al llamar a `changeUser`:

```javascript
BrazePlugin.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```javascript
BrazePlugin.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}

Proporciona el JWT al llamar a `ChangeUser`:

**iOS**

```csharp
Braze.SharedInstance?.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```csharp
Braze.SharedInstance?.SetSDKAuthenticationSignature("NEW-JWT-FROM-SERVER");
```

**Android**

```csharp
Braze.GetInstance(this).ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```csharp
Braze.GetInstance(this).SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Expo %}

Al usar el plugin de Braze Expo, usa los mismos métodos del SDK or kit de desarrollo de software de React Native. Proporciona el JWT al llamar a `changeUser`:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

O, cuando hayas actualizado el token del usuario a mitad de sesión:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% endtabs %}

#### Paso 2.3: Registra una función de devolución de llamada para tokens no válidos {#sdk-callback}

Cuando esta característica se establece como [Obligatoria](#enforcement-options), los siguientes escenarios harán que las solicitudes del SDK or kit de desarrollo de software sean rechazadas por Braze:
- El JWT estaba expirado en el momento en que fue recibido por la API de Braze
- El JWT estaba vacío o ausente
- El JWT no pudo verificarse con las claves públicas que cargaste en el panel de Braze

Puedes usar `subscribeToSdkAuthenticationFailures` para suscribirte y recibir notificaciones cuando las solicitudes del SDK or kit de desarrollo de software fallen por alguna de estas razones. Una función de devolución de llamada contiene un objeto con el [`errorCode`](#error-codes) relevante, la `reason` del error, el `userId` de la solicitud (el usuario no puede ser anónimo) y el token de autenticación (JWT) que causó el error.

Las solicitudes fallidas se reintentarán periódicamente hasta que tu aplicación proporcione un nuevo JWT válido. Si ese usuario sigue con sesión iniciada, puedes usar esta devolución de llamada como una oportunidad para solicitar un nuevo JWT a tu servidor y proporcionar al SDK or kit de desarrollo de software de Braze este nuevo token válido.

Cuando recibas un error de autenticación, verifica que el `userId` en el error coincida con tu usuario actualmente con sesión iniciada, luego obtén una nueva firma de tu servidor y proporciónala al SDK or kit de desarrollo de software de Braze. También puedes registrar estos errores en tu servicio de monitoreo o informe de errores.

{% alert tip %}
Estos métodos de devolución de llamada son un excelente lugar para añadir tu propio servicio de monitoreo o registro de errores para hacer seguimiento de la frecuencia con la que tus solicitudes de Braze son rechazadas.
{% endalert %}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToSdkAuthenticationFailures((error) => {
  console.error("SDK authentication failed:", error);
  console.log("Error code:", error.errorCode);
  console.log("User ID:", error.userId);
  // Note: Do not log error.signature as it contains sensitive authentication credentials

  // Verify the error.userId matches the currently logged-in user
  // Fetch a new token from your server and set it
  fetchNewSignature(error.userId).then((newSignature) => {
    braze.setSdkAuthenticationSignature(newSignature);
  });
});
```
{% endtab %}
{% tab React Native %}
```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);

    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  NSLog(@"Invalid SDK Authentication Token.");
  NSString *newSignature = getNewTokenSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("Invalid SDK Authentication Token.");
  final newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Flutter %}
```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();

braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.");

  String newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Unity %}
**iOS**

Establece el delegado de autenticación del SDK or kit de desarrollo de software en tu implementación nativa de iOS:

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Debug.Log("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    BrazeBinding.SetSdkAuthenticationSignature(newSignature);
  }
}
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.subscribeToSdkAuthenticationFailures((error) => {
  console.log(`SDK Authentication for ${error.user_id} failed with error code ${error.error_code}.`);

  const newSignature = getNewTokenSomehow(error);
  BrazePlugin.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
**iOS**

Establece el delegado de autenticación del SDK or kit de desarrollo de software en tu instancia de `Braze`:

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public override void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Console.WriteLine("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    Braze.SharedInstance?.SetSDKAuthenticationSignature(newSignature);
  }
}

// Set the delegate during initialization
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
braze.SdkAuthDelegate = new SdkAuthDelegate();
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Expo %}
Al usar el plugin de Braze Expo, usa los mismos métodos del SDK or kit de desarrollo de software de React Native:

```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);

    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% endtabs %}

### Paso 3: Habilita la autenticación en el panel {#braze-dashboard}

A continuación, puedes habilitar la autenticación en el panel de Braze para las aplicaciones que configuraste anteriormente.

Ten en cuenta que las solicitudes del SDK or kit de desarrollo de software seguirán fluyendo con normalidad sin autenticación a menos que la configuración de autenticación del SDK or kit de desarrollo de software de la aplicación se establezca como **Obligatorio** en el panel de Braze.

Si algo sale mal con tu integración (por ejemplo, tu aplicación pasa tokens incorrectamente al SDK or kit de desarrollo de software, o tu servidor genera tokens no válidos), deshabilita esta característica en el panel de Braze, y los datos se reanudarán fluyendo con normalidad sin verificación.

#### Opciones de aplicación {#enforcement-options}

En la página **Administrar configuración** del panel, cada aplicación tiene tres estados de autenticación del SDK or kit de desarrollo de software que controlan cómo Braze verifica las solicitudes.

| Configuración | Descripción |
| ------ | ---------- |
| **Deshabilitado** | Braze no verificará el JWT proporcionado para un usuario. (Configuración predeterminada) |
| **Opcional** | Braze verificará las solicitudes de usuarios con sesión iniciada, pero no rechazará solicitudes no válidas. |
| **Obligatorio** | Braze verificará las solicitudes de usuarios con sesión iniciada y rechazará los JWT no válidos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Opciones de aplicación" }

![Configuración de autenticación del SDK de Braze que muestra las opciones de aplicación Deshabilitado, Opcional y Obligatorio.]({% image_buster /assets/img/sdk-auth-settings.png %})

La configuración **Opcional** es una forma útil de monitorizar el posible impacto que esta característica tendrá en el tráfico del SDK or kit de desarrollo de software de tu aplicación.

Un JWT no válido se reportará tanto en los estados **Opcional** como **Obligatorio**, sin embargo solo el estado **Obligatorio** rechazará las solicitudes del SDK or kit de desarrollo de software, lo que hará que las aplicaciones reintenten y soliciten un nuevo JWT.

## Administración de claves públicas {#key-management}

### Añadir una clave pública {#adding-a-public-key}

Puedes añadir hasta tres claves públicas para cada aplicación: una principal, una secundaria y una terciaria. También puedes añadir la misma clave a más de una aplicación si es necesario. Para añadir una clave pública:

1. Ve al panel de Braze y selecciona **Configuración** > **Configuración de la aplicación**.
2. Elige una aplicación de tu lista de aplicaciones disponibles.
3. En **SDK or kit de desarrollo de software Authentication**, selecciona **Add Public Key**.
4. Introduce una descripción opcional, pega tu clave pública y selecciona **Add Public Key**.

### Asignar una nueva clave primaria {#assign-a-new-primary-key}

Para asignar una clave secundaria o terciaria como nueva clave primaria:

1. Ve al panel de Braze y selecciona **Configuración** > **Configuración de la aplicación**.
2. Elige una aplicación de tu lista de aplicaciones disponibles.
3. En **SDK or kit de desarrollo de software Authentication**, elige una clave y selecciona **Manage** > **Make Primary Key**.

### Eliminar una clave {#deleting-a-key}

Para eliminar una clave primaria, [asigna primero una nueva primaria](#assign-a-new-primary-key) y luego elimina tu clave. Para eliminar una clave no primaria:

1. Ve al panel de Braze y selecciona **Configuración** > **Configuración de la aplicación**.
2. Elige una aplicación de tu lista de aplicaciones disponibles.
3. En **SDK or kit de desarrollo de software Authentication**, elige una clave no primaria y selecciona **Manage** > **Delete Public Key**.

## Análisis {#analytics}

Cada aplicación mostrará un desglose de los errores de autenticación del SDK or kit de desarrollo de software recopilados mientras esta característica está en estado **Opcional** u **Obligatoria**.

Los datos están disponibles en tiempo real, y puedes pasar el ratón por encima de los puntos del gráfico para ver un desglose de los errores de una fecha determinada.

![Un gráfico que muestra el número de instancias de errores de autenticación. También se muestra el número total de errores, el tipo de error y el intervalo de fechas ajustable.]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## Códigos de error {#error-codes}

| Código de error | Motivo del error | Descripción | Pasos para resolver |
| --------  | ------------ | ---------  | ---------  |
| 10 | `EXPIRATION_REQUIRED` | La caducidad es un campo obligatorio para el uso de Braze. | Añade un campo `exp` o de caducidad a tu lógica de creación de JWT. |
| 20 | `DECODING_ERROR` | Clave pública no coincidente o error general no detectado. | Copia tu JWT en una herramienta de prueba de JWT para diagnosticar por qué tu JWT tiene un formato no válido. |
| 21 | `SUBJECT_MISMATCH` | Los sujetos esperados y los reales no son los mismos. | El campo `sub` debe ser el mismo ID de usuario que se pasa al método `changeUser` del SDK or kit de desarrollo de software. |
| 22 | `EXPIRED` | El token proporcionado ha caducado. | Amplía tu caducidad o actualiza periódicamente los tokens antes de que caduquen. |
| 23 | `INVALID_PAYLOAD` | La carga útil del token no es válida. | Copia tu JWT en una herramienta de prueba de JWT para diagnosticar por qué tu JWT tiene un formato no válido. |
| 24 | `INCORRECT_ALGORITHM` | No se admite el algoritmo del token. | Cambia tu JWT para utilizar cifrado `RS256`. No se admiten otros tipos. |
| 25 | `PUBLIC_KEY_ERROR` | No se ha podido convertir la clave pública al formato adecuado. | Copia tu JWT en una herramienta de prueba de JWT para diagnosticar por qué tu JWT tiene un formato no válido. |
| 26 | `MISSING_TOKEN` | No se ha proporcionado ningún token en la solicitud. | Asegúrate de que estás pasando un token al llamar a `changeUser(id, token)` y de que tu token no está en blanco. |
| 27 | `NO_MATCHING_PUBLIC_KEYS` | Ninguna clave pública coincide con el token proporcionado. | La clave privada utilizada en el JWT no coincide con ninguna de las claves públicas configuradas para tu aplicación. Confirma que has añadido las claves públicas a la aplicación correcta de tu espacio de trabajo que coincide con esta clave de API. |
| 28 | `PAYLOAD_USER_ID_MISMATCH` | No todos los ID de usuario de la carga útil de la solicitud coinciden como se requiere. | Esto es inesperado y puede dar lugar a una carga útil malformada. Abre un ticket de soporte para obtener ayuda. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Códigos de error" }

## Preguntas frecuentes (FAQ) {#faq}

### ¿Es necesario habilitar esta característica en todas mis aplicaciones al mismo tiempo? {#faq-app-by-app}

No, esta característica puede habilitarse para aplicaciones concretas y no es necesario utilizarla en todas tus aplicaciones a la vez.

### ¿Qué ocurre con los usuarios que siguen utilizando versiones anteriores de mi aplicación? {#faq-sdk-backward-compatibility}

Cuando empieces a aplicar esta característica, las solicitudes realizadas por versiones anteriores de la aplicación serán rechazadas por Braze y reintentadas por el SDK or kit de desarrollo de software. Después de que los usuarios actualicen su aplicación a una versión compatible, esas solicitudes en cola empezarán a aceptarse de nuevo.

Si es posible, debes animar a los usuarios a actualizarse como harías con cualquier otra actualización obligatoria. Alternativamente, puedes mantener la característica como [Opcional](#enforcement-options) hasta que veas que un porcentaje aceptable de usuarios se ha actualizado.

### ¿Qué caducidad debo usar al generar un JWT? {#faq-expiration}

Te recomendamos que utilices el valor más alto de la duración media de la sesión, la caducidad de la cookie/token de sesión o la frecuencia con la que tu aplicación actualizaría el perfil del usuario actual.

### ¿Qué ocurre si un JWT caduca en mitad de la sesión de un usuario? {#faq-jwt-expiration}

Si el token de un usuario caduca durante la sesión, el SDK or kit de desarrollo de software tiene una [función de devolución de llamada](#sdk-callback) que invocará para informar a tu aplicación de que se necesita un nuevo JWT para continuar enviando datos a Braze.

### ¿Qué ocurre si mi integración en servidor se rompe y ya no puedo crear un JWT? {#faq-server-downtime}

Si tu servidor no puede proporcionar un JWT o detectas algún problema de integración, siempre puedes desactivar la característica en el panel de Braze.

Una vez desactivada, el SDK or kit de desarrollo de software reintentará cualquier solicitud fallida pendiente, y Braze la aceptará.

### ¿Por qué esta característica utiliza claves públicas/privadas en lugar de secretos compartidos? {#faq-shared-secrets}

Al utilizar secretos compartidos, cualquiera con acceso a ese secreto compartido, como la página del panel de Braze, podría generar tokens y suplantar la identidad de tus usuarios finales.

En su lugar, utilizamos claves públicas/privadas para que ni siquiera los empleados de Braze (y mucho menos los usuarios de tu empresa) tengan acceso a tus claves privadas.

### ¿Cómo se reintentan las solicitudes rechazadas? {#faq-retry-logic}

Cuando una solicitud es rechazada debido a un error de autenticación, el SDK or kit de desarrollo de software invocará tu devolución de llamada utilizada para actualizar el JWT del usuario.

Las solicitudes se reintentarán periódicamente utilizando una retirada exponencial. Después de 50 intentos fallidos consecutivos, los reintentos se pausarán hasta el siguiente inicio de sesión. Cada SDK or kit de desarrollo de software también tiene un método para solicitar manualmente un vaciado de datos.

### ¿Se puede utilizar la autenticación del SDK or kit de desarrollo de software para usuarios anónimos? {#faq-anonymous-users}

No. La autenticación del SDK or kit de desarrollo de software funciona cuando tu sitio web confirma la identidad de alguien, por lo que solo se aplica a usuarios identificados. Como usuario anónimo, no hay identidad que confirmar.

La aplicación comienza después de llamar a `changeUser`. Antes de que un usuario sea identificado (por ejemplo, mientras navega de forma anónima antes de registrarse), el SDK or kit de desarrollo de software puede seguir enviando datos a Braze sin un JWT. Después de llamar a `changeUser`, las solicitudes para ese perfil identificado requieren un JWT válido.

Esto significa que un recorrido típico de usuario podría verse así:

1. Un usuario visita tu sitio o abre tu aplicación de forma anónima. Braze recopila esta actividad sin un JWT.
2. El usuario se registra o inicia sesión, y tu aplicación llama a `changeUser` con un `external_id`.
3. Braze continúa recopilando la actividad de ese usuario, y la autenticación del SDK or kit de desarrollo de software se aplica a las solicitudes de ese perfil identificado.

### ¿Funciona la autenticación del SDK or kit de desarrollo de software con alias de usuario? {#faq-aliases}

No. La autenticación del SDK or kit de desarrollo de software requiere un `external_id`. No puedes configurarla cuando solo hay un `braze_id` o `alias_id` disponible, por lo que los perfiles que solo tienen alias no pueden usar la autenticación del SDK or kit de desarrollo de software.

### ¿Habilitar la autenticación del SDK or kit de desarrollo de software bloquea la recopilación de actividad no autenticada? {#faq-unauthenticated-collection}

No. La autenticación del SDK or kit de desarrollo de software no bloquea la recopilación legítima de actividad anónima. Solo se aplica después de que un perfil es identificado con `changeUser`.