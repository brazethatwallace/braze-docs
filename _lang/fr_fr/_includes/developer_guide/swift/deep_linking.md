{% multi_lang_include developer_guide/prerequisites/swift.md %}

{% alert tip %}
Pour obtenir de l'aide afin de choisir entre les deep links à schéma personnalisé, les liens universels et « Ouvrir l'URL Web dans l'application », consultez le [guide de création de liens profonds iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Pour la résolution des problèmes, consultez [Résolution des problèmes de création de liens profonds]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).
{% endalert %}

## Gestion des deep links {#handling-deep-links}

### Étape 1 : Enregistrer un schéma {#register-a-scheme}

Pour gérer les deep links, un schéma personnalisé doit être déclaré dans votre fichier `Info.plist`. La structure de navigation est définie par un tableau de dictionnaires. Chacun de ces dictionnaires contient un tableau de chaînes de caractères.

Utilisez Xcode pour modifier votre fichier `Info.plist` :

1. Ajoutez une nouvelle clé, `URL types`. Xcode en fera automatiquement un tableau contenant un dictionnaire appelé `Item 0`.
2. Dans `Item 0`, ajoutez une clé `URL identifier`. Définissez la valeur sur votre schéma personnalisé.
3. Dans `Item 0`, ajoutez une clé `URL Schemes`. Ce sera automatiquement un tableau contenant une chaîne `Item 0`.
4. Définissez `URL Schemes` >> `Item 0` sur votre schéma personnalisé.

Sinon, si vous souhaitez modifier votre fichier `Info.plist` directement, vous pouvez suivre cette spécification :

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

### Étape 2 : Ajouter une liste d'autorisations de schémas {#step-2-add-a-scheme-allowlist}

Vous devez déclarer les schémas d'URL que vous souhaitez transmettre à `canOpenURL(_:)` en ajoutant la clé `LSApplicationQueriesSchemes` au fichier Info.plist de votre application. Toute tentative d'appel de schémas en dehors de cette liste d'autorisations entraînera l'enregistrement d'une erreur dans les journaux de l'appareil, et le deep link ne s'ouvrira pas. Un exemple de cette erreur ressemblera à ceci :

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

Par exemple, si un message in-app doit ouvrir l'application Facebook lorsqu'on appuie dessus, l'application doit avoir le schéma personnalisé de Facebook (`fb`) dans votre liste d'autorisations. Sinon, le système rejettera le deep link. Les deep links qui dirigent vers une page ou une vue au sein de votre propre application nécessitent toujours que le schéma personnalisé de votre application soit répertorié dans le fichier `Info.plist` de votre application.

Votre liste d'autorisations pourrait ressembler à ceci :

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

Pour plus d'informations, reportez-vous à la [documentation d'Apple](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) sur la clé `LSApplicationQueriesSchemes`.

### Étape 3 : Implémenter un gestionnaire {#step-3-implement-a-handler}

Les applications compilées avec Xcode 27 et versions ultérieures doivent adopter le [cycle de vie `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle), de sorte qu'iOS transmet les URL à schéma personnalisé à votre `SceneDelegate` via [`scene:openURLContexts:`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:openurlcontexts:)) plutôt qu'à votre `AppDelegate`. L'argument important est l'objet [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL).

{% tabs %}
{% tab swift %}

```swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  guard let url = URLContexts.first?.url else { return }
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSURL *url = URLContexts.allObjects.firstObject.URL;
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
}
```

{% endtab %}
{% endtabs %}

{% alert note %}
Si votre application n'a pas encore adopté le cycle de vie `UIScene`, iOS appelle à la place [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc) sur votre `AppDelegate` :

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```
{% endalert %}

## App Transport Security (ATS)

Selon la définition d'[Apple](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14), « App Transport Security est une fonctionnalité qui améliore la sécurité des connexions entre une application et les services web. La fonctionnalité consiste en des exigences de connexion par défaut conformes aux meilleures pratiques visant les connexions sécurisées. Les applications peuvent remplacer ce comportement par défaut et désactiver la sécurité du transport. »

L'ATS est appliqué par défaut. Il nécessite que toutes les connexions utilisent HTTPS et soient chiffrées à l'aide de TLS 1.2 avec confidentialité de transmission. Pour plus d'informations, reportez-vous à la section [Exigences pour la connexion à l'aide de l'ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35). Toutes les images servies par Braze aux terminaux sont gérées par un réseau de diffusion de contenu (« CDN ») qui prend en charge TLS 1.2 et est compatible avec ATS.

À moins qu'elles ne soient spécifiées comme exceptions dans le fichier `Info.plist` de votre application, les connexions qui ne respectent pas ces exigences échoueront et généreront des erreurs similaires à celles ci-dessous.

**Exemple d'erreur 1 :**

```bash
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

**Exemple d'erreur 2 :**

```bash
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

La conformité ATS est appliquée aux liens ouverts dans l'application mobile (notre gestion par défaut des liens cliqués) et ne s'applique pas aux sites ouverts à l'extérieur via un navigateur web.

### Utilisation de l'ATS {#working-with-ats}

Vous pouvez gérer l'ATS de l'une des manières suivantes, mais nous vous recommandons de **vous conformer aux exigences de l'ATS**.

{% tabs local %}
{% tab Se conformer %}
Votre intégration Braze peut satisfaire aux exigences ATS en s'assurant que tous les liens existants vers lesquels vous dirigez les utilisateurs (par exemple, via des messages in-app et des Campaigns de notifications push) satisfont aux exigences ATS. Bien qu'il existe des moyens de contourner les restrictions ATS, nous vous recommandons de vous assurer que toutes les URL liées sont conformes à l'ATS. Compte tenu de l'importance croissante accordée par Apple à la sécurité des applications, il n'est pas garanti que les approches suivantes pour autoriser les exceptions ATS soient prises en charge par Apple.
{% endtab %}

{% tab Désactiver partiellement %}
Vous pouvez autoriser un sous-ensemble de liens avec certains domaines ou schémas à être traités comme des exceptions aux règles ATS. Votre intégration Braze satisfera aux exigences ATS si chaque lien que vous utilisez dans un canal de communication Braze est soit conforme à l'ATS, soit géré par une exception.

Pour ajouter un domaine comme exception de l'ATS, ajoutez ce qui suit au fichier `Info.plist` de votre application :

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

Pour plus d'informations, consultez l'article d'Apple sur les [clés de sécurité pour le transport d'applications](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33).
{% endtab %}

{% tab Désactiver complètement %}
Vous pouvez désactiver complètement l'ATS. Notez que ce n'est pas une pratique recommandée, en raison à la fois des protections de sécurité perdues et de la future compatibilité iOS. Pour désactiver l'ATS, insérez les éléments suivants dans le fichier `Info.plist` de votre application :

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```
{% endtab %}
{% endtabs %}

## Décodage des URL {#decoding-urls}

Le SDK encode les liens en pourcentage pour créer des `URL` valides. Tous les caractères de lien qui ne sont pas autorisés dans une URL correctement formée, tels que les caractères Unicode, seront échappés en pourcentage.

Pour décoder un lien encodé, utilisez la propriété `String` [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding). Vous devez également renvoyer `true` dans `BrazeDelegate.braze(_:shouldOpenURL:)`. Un appel à l'action est nécessaire pour déclencher le traitement de l'URL par votre application. Par exemple, dans votre gestionnaire [`scene:openURLContexts:`](#step-3-implement-a-handler) de l'étape 3 :

{% tabs %}
{% tab swift %}

```swift
  func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    guard let url = URLContexts.first?.url else { return }
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSURL *url = URLContexts.allObjects.firstObject.URL;
  NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
  // Handle urlString
}
```

{% endtab %}
{% endtabs %}

## Création de liens profonds vers les paramètres de l'application {#deep-linking-to-app-settings}

Vous pouvez utiliser `UIApplicationOpenSettingsURLString` pour créer des deep links redirigeant les utilisateurs vers les paramètres de votre application à partir des notifications push Braze et des messages in-app.

Pour diriger les utilisateurs de votre application vers les paramètres iOS :
1. Tout d'abord, assurez-vous que votre application est configurée pour les [deep links basés sur un schéma](#swift_register-a-scheme) ou les [liens universels](#swift_universal-links).
2. Choisissez un URI pour le deep link vers la page **Paramètres** (par exemple, `myapp://settings` ou `https://www.braze.com/settings`).
3. Si vous utilisez des deep links basés sur un schéma personnalisé, ajoutez le code suivant à votre gestionnaire `scene:openURLContexts:` :

{% tabs %}
{% tab swift %}

```swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  guard let path = URLContexts.first?.url.path else { return }
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSString *path  = [URLContexts.allObjects.firstObject.URL path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
}
```

{% endtab %}
{% endtabs %}

## Options de personnalisation {#customization-options}

### Personnalisation de la WebView par défaut {#default-webview-customization}

La classe `Braze.WebViewController` affiche les URL web ouvertes par le SDK, généralement lorsque l'option « Ouvrir l'URL Web dans l'application » est sélectionnée pour un deep link web.

Vous pouvez personnaliser le `Braze.WebViewController` via la méthode de délégué [`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/).

### Personnalisation de la gestion des liens {#linking-handling-customization}

Le protocole `BrazeDelegate` peut être utilisé pour personnaliser la gestion des URL telles que les deep links, les URL web et les liens universels. Pour définir le délégué lors de l'initialisation de Braze, définissez un objet délégué sur l'instance `Braze`. Braze appellera ensuite l'implémentation de `shouldOpenURL` de votre délégué avant de gérer les URI.

Lorsqu'une notification push ou un message in-app utilise **Ouvrir l'URL web dans l'application mobile**, Braze transmet `context.useWebView == true` sur [`Braze.URLContext`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/urlcontext). Lorsque le message ouvre l'URL dans le navigateur système, `useWebView` est `false`. Inspectez `context.useWebView` dans `braze(_:shouldOpenURL:)` pour adapter votre gestion personnalisée — par exemple, pour ouvrir un `WebViewController` in-app uniquement lorsque la Campaign a demandé un affichage in-app.

#### Liens universels {#universal-links}

Braze prend en charge les liens universels dans les notifications push, les messages in-app et les Content Cards. Pour activer la prise en charge des liens universels, [`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) doit être défini sur `true`.

Lorsque cette option est activée, Braze transmet les liens universels à votre `SceneDelegate` via la méthode [`scene:continue:`](https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:continue:)) pour les applications ayant adopté le cycle de vie `UIScene` (requis pour les applications compilées avec Xcode 27 et versions ultérieures), ou à votre `AppDelegate` via [`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) dans le cas contraire.

Votre application doit également être configurée pour gérer les liens universels. Reportez-vous à la [documentation d'Apple](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) pour vous assurer que votre application est configurée correctement pour les liens universels.

{% alert warning %}
Le transfert de liens universels nécessite l'accès aux droits de l'application. Lorsque l'application est exécutée dans un simulateur, ces droits ne sont pas directement disponibles et les liens universels ne sont pas transmis aux gestionnaires du système.
Pour ajouter la prise en charge aux builds de simulateur, vous pouvez ajouter le fichier `.entitlements` de l'application à la phase de build _Copy Bundle Resources_. Consultez la documentation de [`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) pour plus de détails.
{% endalert %}

{% alert note %}
Le SDK n'interroge pas le fichier `apple-app-site-association` de vos domaines. Il fait la différence entre les liens universels et les URL ordinaires en ne tenant compte que du nom de domaine. Par conséquent, le SDK ne respecte aucune règle d'exclusion définie dans le fichier `apple-app-site-association` conformément à la documentation [Prise en charge des domaines associés](https://developer.apple.com/documentation/xcode/supporting-associated-domains).
{% endalert %}

## Exemples {#examples}

### BrazeDelegate

Voici un exemple utilisant `BrazeDelegate`. Pour plus d'informations, consultez la [référence du SDK Swift de Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate).

{% tabs %}
{% tab swift %}

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if context.url.host == "MY-DOMAIN.com" {
    // Custom handle link here
    return false
  }
  // Let Braze handle links otherwise
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}
```

{% endtab %}
{% endtabs %}