---
page_order: 1.2
nav_title: Authentifizierung
article_title: Authentifizierung für das Braze SDK einrichten
description: "Dieser Referenzartikel behandelt die SDK-Authentifizierung und wie Sie dieses Feature im Braze SDK aktivieren können."
platform:
  - iOS
  - Android
  - Web

---

# Authentifizierung für das Braze SDK einrichten {#set-up-sdk-authentication}

> Mit der SDK-Authentifizierung können Sie SDK-Anfragen, die im Namen von angemeldeten Nutzer:innen gestellt werden, einen (serverseitig generierten) kryptografischen Beweis liefern.

## Funktionsweise {#how-it-works}

Nachdem Sie dieses Feature in Ihrer App aktiviert haben, können Sie das Braze-Dashboard so konfigurieren, dass alle Anfragen mit einem ungültigen oder fehlenden JSON Web Token / Textbaustein (JWT) abgelehnt werden. Dies betrifft:

- Senden von angepassten Events, Attributen, Käufen und Sitzungsdaten
- Erstellen neuer Nutzer:innen in Ihrem Braze-Workspace
- Aktualisieren von Standardattributen des Nutzerprofils
- Empfangen oder Triggern von Nachrichten

So können Sie verhindern, dass nicht authentifizierte angemeldete Nutzer:innen den SDK-API-Schlüssel Ihrer App verwenden, um böswillige Aktionen durchzuführen, wie z. B. das Imitieren anderer Nutzer:innen.

## Authentifizierung einrichten {#setting-up-authentication}

### Schritt 1: Server einrichten {#server-side-integration}

#### Schritt 1.1: Öffentliches/privates Schlüsselpaar generieren {#generate-keys}

Generieren Sie ein RSA256-Public/Private-Key-Paar. Der Public Key wird später im Braze-Dashboard hinzugefügt, während der Private Key sicher auf Ihrem Server gespeichert werden sollte.

Wir empfehlen einen RSA-Schlüssel mit 2048 Bit zur Verwendung mit dem RS256-JWT-Algorithmus.

{% alert warning %}
Denken Sie daran, Ihre Private Keys _privat_ zu halten. Geben Sie Ihren Private Key niemals preis und codieren Sie ihn niemals fest in Ihrer App oder Website. Jede Person, die Ihren Private Key kennt, kann Nutzer:innen in Ihrem Namen imitieren oder erstellen.
{% endalert %}

#### Schritt 1.2: JSON Web Token / Textbaustein für die aktuelle Nutzerin oder den aktuellen Nutzer erstellen {#create-jwt}

Sobald Sie Ihren Private Key haben, sollte Ihre serverseitige Anwendung diesen verwenden, um ein JWT an Ihre App oder Website für die aktuell angemeldete Nutzerin oder den aktuell angemeldeten Nutzer zurückzugeben.

Typischerweise könnte diese Logik dort implementiert werden, wo Ihre App normalerweise das Profil der aktuellen Nutzerin oder des aktuellen Nutzers abfragt – zum Beispiel an einem Login-Endpunkt oder überall dort, wo Ihre App das aktuelle Kundenprofil aktualisiert.

Bei der Generierung des JWT werden die folgenden Felder erwartet:

**JWT-Header**

| Feld | Erforderlich | Beschreibung |
| ----- | -------- | ----------------------------------- |
| `alg` | Ja | Der unterstützte Algorithmus ist `RS256`. |
| `typ` | Ja | Der Typ sollte `JWT` lauten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 1.2: JSON Web Token / Textbaustein für die aktuelle Nutzerin oder den aktuellen Nutzer erstellen" }

**JWT-Payload**

| Feld | Erforderlich | Beschreibung |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | Ja | Das „Subject“ sollte der Nutzer-ID entsprechen, die Sie dem Braze SDK beim Aufruf von `changeUser` übergeben. |
| `exp` | Ja | Die „Expiration“ gibt an, wann dieses Token / Textbaustein ablaufen soll, als Unix-Zeitstempel in Sekunden (zum Beispiel `1893456000` für den 1. Januar 2030). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 1.2: JSON Web Token / Textbaustein für die aktuelle Nutzerin oder den aktuellen Nutzer erstellen" }

{% alert tip %}
Um mehr über JSON Web Tokens zu erfahren oder die vielen Open-Source-Bibliotheken zu durchsuchen, die diesen Signierungsprozess vereinfachen, besuchen Sie [https://jwt.io](https://jwt.io).
{% endalert %}

### Schritt 2: SDK konfigurieren {#sdk-integration}

Dieses Feature ist ab den folgenden [SDK-Versionen]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) verfügbar:

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
Für iOS-Integrationen beschreibt diese Seite die Schritte für das Braze Swift SDK. Für die Beispielverwendung im Legacy-AppboyKit-iOS-SDK beziehen Sie sich auf [diese Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) und [diese Datei](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m).
{% endalert %}

#### Schritt 2.1: Authentifizierung im Braze SDK aktivieren {#step-21-enable-authentication-in-the-braze-sdk}

Wenn dieses Feature aktiviert ist, hängt das Braze SDK das zuletzt bekannte JWT der aktuellen Nutzerin oder des aktuellen Nutzers an Netzwerkanfragen an Braze-Server an.

{% alert note %}
Keine Sorge – die alleinige Initialisierung mit dieser Option hat keinerlei Auswirkungen auf die Datenerfassung, bis Sie die [Authentifizierung erzwingen](#braze-dashboard) im Braze-Dashboard.
{% endalert %}

{% tabs %}
{% tab Internet %}
Setzen Sie beim Aufruf von `initialize` die optionale Eigenschaft `enableSdkAuthentication` auf `true`.
```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab React Native %}
Die SDK-Authentifizierung muss während der nativen SDK-Initialisierung aktiviert werden. Fügen Sie die folgende Konfiguration zu Ihrem nativen iOS- und Android-Code hinzu:

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

Nach der Aktivierung der SDK-Authentifizierung in der nativen Schicht können Sie die in den folgenden Schritten gezeigten React-Native-JavaScript-Methoden verwenden.
{% endtab %}
{% tab Java %}
Rufen Sie beim Konfigurieren der Braze-Instanz `setIsSdkAuthenticationEnabled` mit dem Wert `true` auf.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

Alternativ können Sie `<bool name="com_braze_sdk_authentication_enabled">true</bool>` zu Ihrer braze.xml hinzufügen.
{% endtab %}
{% tab KOTLIN %}
Rufen Sie beim Konfigurieren der Braze-Instanz `setIsSdkAuthenticationEnabled` mit dem Wert `true` auf.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

Alternativ können Sie `<bool name="com_braze_sdk_authentication_enabled">true</bool>` zu Ihrer braze.xml hinzufügen.
{% endtab %}
{% tab Objective-C %}
Um die SDK-Authentifizierung zu aktivieren, setzen Sie die Eigenschaft `configuration.api.sdkAuthentication` Ihres `BRZConfiguration`-Objekts auf `YES`, bevor Sie die Braze-Instanz initialisieren:

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
Um die SDK-Authentifizierung zu aktivieren, setzen Sie die Eigenschaft `configuration.api.sdkAuthentication` Ihres `Braze.Configuration`-Objekts auf `true`, wenn Sie das SDK initialisieren:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
Derzeit muss die SDK-Authentifizierung als Teil der SDK-Initialisierung im nativen iOS- und Android-Code aktiviert werden. Um die SDK-Authentifizierung im Flutter SDK zu aktivieren, folgen Sie den Integrationen für iOS und Android aus den anderen Tabs. Nachdem die SDK-Authentifizierung aktiviert ist, kann der Rest des Features in Dart integriert werden.
{% endtab %}
{% tab Flutter %}
Die SDK-Authentifizierung muss als Teil der SDK-Initialisierung im nativen iOS- und Android-Code aktiviert werden. Wenn sie in der nativen Schicht aktiviert ist, können Sie Flutter-SDK-Methoden verwenden, um die JWT-Signatur zu übergeben.

**iOS**

Um die SDK-Authentifizierung zu aktivieren, setzen Sie die Eigenschaft `configuration.api.sdkAuthentication` in Ihrem nativen iOS-Code auf `true`:

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Nach der Aktivierung der SDK-Authentifizierung in der nativen Schicht können Sie die in den folgenden Schritten gezeigten Flutter-SDK-Methoden verwenden.
{% endtab %}
{% tab Unity %}
Die SDK-Authentifizierung muss während der nativen SDK-Initialisierung aktiviert werden. Fügen Sie die folgende Konfiguration zu Ihrem nativen iOS- und Android-Code hinzu:

**iOS**

Setzen Sie die Eigenschaft `SDKAuthenticationEnabled` in Ihrer Konfigurationsdatei auf `true`:

```xml
<key>SDKAuthenticationEnabled</key>
<true/>
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Nach der Aktivierung der SDK-Authentifizierung in der nativen Schicht können Sie die in den folgenden Schritten gezeigten Unity-C#-Methoden verwenden.
{% endtab %}
{% tab Cordova %}
Die SDK-Authentifizierung muss während der nativen SDK-Initialisierung aktiviert werden. Fügen Sie die folgende Konfiguration zu Ihrem nativen iOS- und Android-Code hinzu:

**iOS**

Um die SDK-Authentifizierung zu aktivieren, setzen Sie die Eigenschaft `enableSDKAuthentication` in Ihrer `config.xml` auf `true`:

```xml
<preference name="com.braze.ios_enable_sdk_authentication" value="true" />
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Nach der Aktivierung der SDK-Authentifizierung in der nativen Schicht können Sie die in den folgenden Schritten gezeigten Cordova-JavaScript-Methoden verwenden.
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
Die SDK-Authentifizierung muss während der nativen SDK-Initialisierung aktiviert werden. Konfigurieren Sie die SDK-Authentifizierung separat für iOS und Android:

**iOS**

Um die SDK-Authentifizierung zu aktivieren, setzen Sie die Eigenschaft `configuration.Api.SdkAuthentication` auf `true`, wenn Sie das SDK initialisieren:

```csharp
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Nach der Aktivierung der SDK-Authentifizierung können Sie die in den folgenden Schritten gezeigten .NET-MAUI-Methoden verwenden.
{% endtab %}
{% tab Expo %}
Wenn Sie das Braze Expo Plugin verwenden, setzen Sie die Eigenschaft `enableSdkAuthentication` in Ihrer App-Konfiguration auf `true`. Dies konfiguriert die SDK-Authentifizierung automatisch in den nativen iOS- und Android-Schichten, ohne dass manuelle native Code-Änderungen erforderlich sind.

**app.json oder app.config.js**

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

Nach der Aktivierung der SDK-Authentifizierung in Ihrer App-Konfiguration können Sie die im React-Native-Tab gezeigten React-Native-JavaScript-Methoden für die folgenden Schritte verwenden.

{% alert note %}
Ein vollständiges Implementierungsbeispiel finden Sie in der [Braze Expo Plugin Beispiel-App](https://github.com/braze-inc/braze-expo-plugin/blob/main/example/components/Braze.tsx) auf GitHub.
{% endalert %}
{% endtab %}
{% endtabs %}

#### Schritt 2.2: JWT der aktuellen Nutzerin oder des aktuellen Nutzers setzen {#step-22-set-the-current-users-jwt}

Immer wenn Ihre App die Braze-Methode `changeUser` aufruft, übergeben Sie auch das JWT, das [serverseitig generiert](#braze-dashboard) wurde.

Sie können das Token / Textbaustein auch so konfigurieren, dass es während der Sitzung für die aktuelle Nutzerin oder den aktuellen Nutzer aktualisiert wird.

{% alert note %}
Beachten Sie, dass `changeUser` nur aufgerufen werden sollte, wenn sich die Nutzer-ID _tatsächlich geändert_ hat. Sie sollten diese Methode nicht verwenden, um das Authentifizierungstoken (JWT) zu aktualisieren, wenn sich die Nutzer-ID nicht geändert hat.
{% endalert %}

{% tabs %}
{% tab Internet %}
Übergeben Sie das JWT beim Aufruf von [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```javascript
import * as braze from "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab React Native %}

Übergeben Sie das JWT beim Aufruf von [`changeUser`](https://braze-inc.github.io/braze-react-native-sdk/classes/Braze.Braze-1.html#changeUser):

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Übergeben Sie das JWT beim Aufruf von [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Übergeben Sie das JWT beim Aufruf von [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

Übergeben Sie das JWT beim Aufruf von [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

Übergeben Sie das JWT beim Aufruf von [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```

{% alert note %}
`changeUser` gibt sofort auf dem aufrufenden Thread zurück. Die hier übergebene SDK-Authentifizierungssignatur wird angehängt, nachdem der Nutzerwechsel abgeschlossen ist.
{% endalert %}

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

Übergeben Sie das JWT beim Aufruf von [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% tab Flutter %}

Übergeben Sie das JWT beim Aufruf von `changeUser`:

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.changeUser("NEW-USER-ID", sdkAuthSignature: "JWT-FROM-SERVER");
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Unity %}

Übergeben Sie das JWT beim Aufruf von `ChangeUser`:

```csharp
BrazeBinding.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```csharp
BrazeBinding.SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Cordova %}

Übergeben Sie das JWT beim Aufruf von `changeUser`:

```javascript
BrazePlugin.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```javascript
BrazePlugin.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}

Übergeben Sie das JWT beim Aufruf von `ChangeUser`:

**iOS**

```csharp
Braze.SharedInstance?.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```csharp
Braze.SharedInstance?.SetSDKAuthenticationSignature("NEW-JWT-FROM-SERVER");
```

**Android**

```csharp
Braze.GetInstance(this).ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```csharp
Braze.GetInstance(this).SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Expo %}

Wenn Sie das Braze Expo Plugin verwenden, nutzen Sie die gleichen React-Native-SDK-Methoden. Übergeben Sie das JWT beim Aufruf von `changeUser`:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Oder wenn Sie das Token / Textbaustein der Nutzerin oder des Nutzers während der Sitzung aktualisiert haben:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% endtabs %}

#### Schritt 2.3: Callback-Funktion für ungültige Token manuell registrieren {#sdk-callback}

Wenn dieses Feature auf [Erforderlich](#enforcement-options) gesetzt ist, führen die folgenden Szenarien dazu, dass SDK-Anfragen von Braze abgelehnt werden:
- Das JWT war zum Zeitpunkt des Eingangs bei der Braze-API abgelaufen
- Das JWT war leer oder fehlte
- Die JWT-Verifizierung ist für die Public Keys, die Sie im Braze-Dashboard hochgeladen haben, fehlgeschlagen

Sie können `subscribeToSdkAuthenticationFailures` verwenden, um benachrichtigt zu werden, wenn SDK-Anfragen aus einem dieser Gründe fehlschlagen. Eine Callback-Funktion enthält ein Objekt mit dem relevanten [`errorCode`](#error-codes), dem `reason` für den Fehler, der `userId` der Anfrage (die Nutzerin oder der Nutzer darf nicht anonym sein) und dem Authentifizierungstoken (JWT), das den Fehler verursacht hat.

Fehlgeschlagene Anfragen werden periodisch wiederholt, bis Ihre App ein neues gültiges JWT bereitstellt. Wenn diese Nutzerin oder dieser Nutzer noch angemeldet ist, können Sie diesen Callback als Gelegenheit nutzen, ein neues JWT von Ihrem Server anzufordern und das Braze SDK mit diesem neuen gültigen Token / Textbaustein zu versorgen.

Wenn Sie einen Authentifizierungsfehler erhalten, überprüfen Sie, ob die `userId` im Fehler mit der aktuell angemeldeten Nutzerin oder dem aktuell angemeldeten Nutzer übereinstimmt. Rufen Sie dann eine neue Signatur von Ihrem Server ab und übergeben Sie sie dem Braze SDK. Sie können diese Fehler auch in Ihrem Monitoring- oder Fehlerberichtsdienst protokollieren.

{% alert tip %}
Diese Callback-Methoden sind ein hervorragender Ort, um Ihren eigenen Monitoring- oder Fehlerprotokollierungsdienst hinzuzufügen, um zu verfolgen, wie oft Ihre Braze-Anfragen abgelehnt werden.
{% endalert %}

{% tabs %}
{% tab Internet %}
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

Setzen Sie den SDK-Authentifizierungs-Delegate in Ihrer nativen iOS-Implementierung:

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

Setzen Sie den SDK-Authentifizierungs-Delegate auf Ihrer `Braze`-Instanz:

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
Wenn Sie das Braze Expo Plugin verwenden, nutzen Sie die gleichen React-Native-SDK-Methoden:

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

### Schritt 3: Authentifizierung im Dashboard aktivieren {#braze-dashboard}

Als Nächstes können Sie die Authentifizierung im Braze-Dashboard für die zuvor eingerichteten Apps aktivieren.

Beachten Sie, dass SDK-Anfragen weiterhin wie gewohnt ohne Authentifizierung fließen, es sei denn, die SDK-Authentifizierungseinstellung der App ist im Braze-Dashboard auf **Erforderlich** gesetzt.

Sollte bei Ihrer Integration etwas schiefgehen (zum Beispiel übergibt Ihre App fälschlicherweise Token / Textbaustein an das SDK oder Ihr Server generiert ungültige Token / Textbaustein), deaktivieren Sie dieses Feature im Braze-Dashboard, und die Daten fließen wie gewohnt ohne Verifizierung weiter.

#### Erzwingungsoptionen {#enforcement-options}

Auf der Seite **Einstellungen verwalten** im Dashboard hat jede App drei SDK-Authentifizierungszustände, die steuern, wie Braze Anfragen verifiziert.

| Einstellung | Beschreibung |
| ------ | ---------- |
| **Deaktiviert** | Braze verifiziert das für eine:n Nutzer:in bereitgestellte JWT nicht. (Standardeinstellung) |
| **Optional** | Braze verifiziert Anfragen für angemeldete Nutzer:innen, lehnt ungültige Anfragen jedoch nicht ab. |
| **Erforderlich** | Braze verifiziert Anfragen für angemeldete Nutzer:innen und lehnt ungültige JWTs ab. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erzwingungsoptionen" }

![Braze-SDK-Authentifizierungseinstellungen mit den Erzwingungsoptionen „Deaktiviert“, „Optional“ und „Erforderlich“.]({% image_buster /assets/img/sdk-auth-settings.png %})

Die Einstellung **Optional** ist eine nützliche Möglichkeit, die potenziellen Auswirkungen dieses Features auf den SDK-Traffic Ihrer App zu überwachen.

Ein ungültiges JWT wird sowohl im Zustand **Optional** als auch im Zustand **Erforderlich** gemeldet. Jedoch lehnt nur der Zustand **Erforderlich** SDK-Anfragen ab, was dazu führt, dass Apps den Vorgang wiederholen und ein neues JWT anfordern.

## Öffentliche Schlüssel verwalten {#key-management}

### Hinzufügen eines Public Keys {#adding-a-public-key}

Sie können bis zu drei öffentliche Schlüssel für jede App hinzufügen: einen primären, einen sekundären und einen tertiären. Sie können denselben Schlüssel bei Bedarf auch zu mehreren Apps hinzufügen. Um einen öffentlichen Schlüssel hinzuzufügen:

1. Gehen Sie zum Braze-Dashboard und wählen Sie **Settings** > **App Settings**.
2. Wählen Sie eine App aus Ihrer Liste der verfügbaren Apps.
3. Wählen Sie unter **SDK Authentication** die Option **Add Public Key**.
4. Geben Sie eine optionale Beschreibung ein, fügen Sie Ihren Public Key ein und wählen Sie **Add Public Key**.

### Einen neuen Primärschlüssel zuweisen {#assign-a-new-primary-key}

So weisen Sie einen Sekundär- oder Tertiärschlüssel als Ihren neuen Primärschlüssel zu:

1. Gehen Sie zum Braze-Dashboard und wählen Sie **Settings** > **App Settings**.
2. Wählen Sie eine App aus Ihrer Liste der verfügbaren Apps.
3. Wählen Sie unter **SDK Authentication** einen Schlüssel und wählen Sie **Manage** > **Make Primary Key**.

### Schlüssel löschen {#deleting-a-key}

Um einen Primärschlüssel zu löschen, [weisen Sie zunächst einen neuen Primärschlüssel zu](#assign-a-new-primary-key) und löschen Sie dann Ihren Schlüssel. So löschen Sie einen nicht-primären Schlüssel:

1. Gehen Sie zum Braze-Dashboard und wählen Sie **Settings** > **App Settings**.
2. Wählen Sie eine App aus Ihrer Liste der verfügbaren Apps.
3. Wählen Sie unter **SDK Authentication** einen nicht-primären Schlüssel und wählen Sie **Manage** > **Delete Public Key**.

## Analytics {#analytics}

Jede App zeigt eine Aufschlüsselung der SDK-Authentifizierungsfehler, die gesammelt wurden, während sich dieses Feature im Status **Optional** oder **Erforderlich** befindet.

Die Daten sind in Realtime verfügbar, und Sie können den Mauszeiger über Datenpunkte im Chart bewegen, um eine Aufschlüsselung der Fehler für ein bestimmtes Datum zu sehen.

![Ein Chart, das die Anzahl der Authentifizierungsfehler anzeigt. Ebenfalls angezeigt werden die Gesamtzahl der Fehler, die Art der Fehler und der einstellbare Datumsbereich.]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## Fehlercodes {#error-codes}

| Fehlercode | Fehlergrund | Beschreibung | Schritte zur Behebung |
| --------  | ------------ | ---------  | ---------  |
| 10 | `EXPIRATION_REQUIRED` | Die Gültigkeitsdauer ist ein Pflichtfeld für die Verwendung von Braze. | Fügen Sie Ihrer JWT-Erstellungslogik ein `exp`- oder Ablaufdatum-Feld hinzu. |
| 20 | `DECODING_ERROR` | Nicht übereinstimmender Public Key oder ein allgemeiner nicht abgefangener Fehler. | Kopieren Sie Ihr JWT in ein JWT-Testtool, um zu diagnostizieren, warum Ihr JWT ein ungültiges Format aufweist. |
| 21 | `SUBJECT_MISMATCH` | Die erwarteten und tatsächlichen Subjects stimmen nicht überein. | Das `sub`-Feld sollte dieselbe Nutzer-ID enthalten, die an die SDK-Methode `changeUser` übergeben wurde. |
| 22 | `EXPIRED` | Das bereitgestellte Token / Textbaustein ist abgelaufen. | Verlängern Sie die Gültigkeitsdauer oder aktualisieren Sie Tokens regelmäßig, bevor sie ablaufen. |
| 23 | `INVALID_PAYLOAD` | Die Payload des Tokens ist ungültig. | Kopieren Sie Ihr JWT in ein JWT-Testtool, um zu diagnostizieren, warum Ihr JWT ein ungültiges Format aufweist. |
| 24 | `INCORRECT_ALGORITHM` | Der Algorithmus des Tokens wird nicht unterstützt. | Ändern Sie Ihr JWT, um `RS256`-Verschlüsselung zu verwenden. Andere Typen werden nicht unterstützt. |
| 25 | `PUBLIC_KEY_ERROR` | Der Public Key konnte nicht in das richtige Format konvertiert werden. | Kopieren Sie Ihr JWT in ein JWT-Testtool, um zu diagnostizieren, warum Ihr JWT ein ungültiges Format aufweist. |
| 26 | `MISSING_TOKEN` | Es wurde kein Token / Textbaustein in der Anfrage angegeben. | Stellen Sie sicher, dass Sie beim Aufruf von `changeUser(id, token)` ein Token / Textbaustein übergeben und dass Ihr Token / Textbaustein nicht leer ist. |
| 27 | `NO_MATCHING_PUBLIC_KEYS` | Es gibt keine öffentlichen Schlüssel, die mit dem bereitgestellten Token / Textbaustein übereinstimmen. | Der im JWT verwendete Private Key stimmt mit keinem der für Ihre App konfigurierten Public Keys überein. Bestätigen Sie, dass Sie die öffentlichen Schlüssel zur richtigen App in Ihrem Workspace hinzugefügt haben, die mit diesem API-Schlüssel übereinstimmt. |
| 28 | `PAYLOAD_USER_ID_MISMATCH` | Nicht alle Nutzer-IDs in der Anfrage-Payload stimmen wie erforderlich überein. | Dies ist unerwartet und kann zu einer fehlerhaften Payload führen. Öffnen Sie ein Support-Ticket, um Unterstützung zu erhalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Fehlercodes" }

## Häufig gestellte Fragen (FAQ) {#faq}

### Muss dieses Feature in allen meinen Apps gleichzeitig aktiviert werden? {#faq-app-by-app}

Nein, dieses Feature kann für bestimmte Apps aktiviert werden und muss nicht für alle Ihre Apps auf einmal verwendet werden.

### Was passiert mit Nutzer:innen, die noch ältere Versionen meiner App verwenden? {#faq-sdk-backward-compatibility}

Wenn Sie damit beginnen, dieses Feature zu erzwingen, werden Anfragen von älteren App-Versionen von Braze abgelehnt und vom SDK erneut versucht. Nachdem Nutzer:innen ihre App auf eine unterstützte Version aktualisiert haben, werden diese in der Warteschlange befindlichen Anfragen wieder akzeptiert.

Wenn möglich, sollten Sie Nutzer:innen zum Upgrade auffordern, wie Sie es bei jedem anderen Pflichtupdate tun würden. Alternativ können Sie das Feature [optional](#enforcement-options) lassen, bis Sie sehen, dass ein akzeptabler Prozentsatz der Nutzer:innen aktualisiert hat.

### Welche Gültigkeitsdauer sollte ich bei der Erstellung eines JWTs verwenden? {#faq-expiration}

Wir empfehlen, den höheren Wert der durchschnittlichen Sitzungsdauer, des Ablaufs von Sitzungs-Cookies/-Tokens oder der Häufigkeit zu verwenden, mit der Ihre Anwendung sonst das Profil der aktuellen Nutzer:in aktualisieren würde.

### Was passiert, wenn ein JWT mitten in der Sitzung einer Nutzer:in abläuft? {#faq-jwt-expiration}

Sollte das Token / Textbaustein einer Nutzer:in mitten in der Sitzung ablaufen, verfügt das SDK über eine [Callback-Funktion](#sdk-callback), die Ihre App darüber informiert, dass ein neues JWT erforderlich ist, um weiterhin Daten an Braze zu senden.

### Was passiert, wenn meine serverseitige Integration nicht mehr funktioniert und ich kein JWT mehr erstellen kann? {#faq-server-downtime}

Wenn Ihr Server kein JWT bereitstellen kann oder Sie ein Problem bei der Integration feststellen, können Sie das Feature jederzeit im Braze-Dashboard deaktivieren.

Nach der Deaktivierung werden alle ausstehenden fehlgeschlagenen SDK-Anfragen vom SDK erneut versucht und von Braze akzeptiert.

### Warum verwendet dieses Feature Public/Private Keys und nicht Shared Secrets? {#faq-shared-secrets}

Bei der Verwendung von Shared Secrets könnte jeder, der Zugriff auf dieses Shared Secret hat, z. B. über die Braze-Dashboard-Seite, Token / Textbaustein generieren und sich als Ihre Endnutzer:innen ausgeben.

Stattdessen verwenden wir Public/Private Keys, sodass selbst Braze-Mitarbeitende (geschweige denn die Nutzer:innen Ihres Unternehmens) keinen Zugriff auf Ihre Private Keys haben.

### Wie werden abgelehnte Anfragen erneut versucht? {#faq-retry-logic}

Wenn eine Anfrage aufgrund eines Authentifizierungsfehlers abgelehnt wird, ruft das SDK Ihren Callback auf, mit dem Sie das JWT der Nutzer:in aktualisieren können.

Anfragen werden in regelmäßigen Abständen mit einem exponentiellen Backoff-Verfahren wiederholt. Nach 50 aufeinanderfolgenden Fehlversuchen werden die Wiederholungen bis zum nächsten Sitzungsstart pausiert. Jedes SDK verfügt auch über eine Methode zur manuellen Anforderung eines Data Flush.

### Kann die SDK-Authentifizierung für anonyme Nutzer:innen verwendet werden? {#faq-anonymous-users}

Nein. Die SDK-Authentifizierung funktioniert, indem Ihre Website die Identität einer Person bestätigt, daher gilt sie nur für identifizierte Nutzer:innen. Als anonyme:r Nutzer:in gibt es keine Identität, die bestätigt werden könnte.

Die Durchsetzung beginnt nach dem Aufruf von `changeUser`. Bevor eine Nutzer:in identifiziert wird (z. B. beim anonymen Browsen vor der Registrierung), kann das SDK weiterhin Daten ohne JWT an Braze senden. Nach dem Aufruf von `changeUser` benötigen Anfragen für dieses identifizierte Profil ein gültiges JWT.

Das bedeutet, dass eine typische User Journey so aussehen könnte:

1. Eine Nutzer:in besucht Ihre Website oder öffnet Ihre App anonym. Braze erfasst diese Aktivität ohne JWT.
2. Die Nutzer:in registriert sich oder meldet sich an, und Ihre App ruft `changeUser` mit einer `external_id` auf.
3. Braze erfasst weiterhin die Aktivität für diese Nutzer:in, und die SDK-Authentifizierung wird für Anfragen dieses identifizierten Profils erzwungen.

### Funktioniert die SDK-Authentifizierung mit Nutzer-Aliasen? {#faq-aliases}

Nein. Die SDK-Authentifizierung erfordert eine `external_id`. Sie kann nicht eingerichtet werden, wenn nur eine `braze_id` oder `alias_id` verfügbar ist, daher können Alias-only-Profile die SDK-Authentifizierung nicht verwenden.

### Blockiert die Aktivierung der SDK-Authentifizierung die Erfassung nicht authentifizierter Aktivitäten? {#faq-unauthenticated-collection}

Nein. Die SDK-Authentifizierung blockiert keine legitime anonyme Aktivitätserfassung. Sie greift erst, nachdem ein Profil mit `changeUser` identifiziert wurde.