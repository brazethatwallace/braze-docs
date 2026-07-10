{% multi_lang_include in-app_messages/troubleshooting.md sdk="iOS" %}

### Résolution des problèmes de chargement des ressources (`NSURLError` code `-1008`) {#asset-loading}

Lors de l'intégration de Braze avec des bibliothèques tierces de journalisation réseau, les développeurs peuvent fréquemment rencontrer une `NSURLError` avec le code de domaine `-1008`. Cette erreur indique que des ressources telles que des images et des polices n'ont pas pu être récupérées ou que leur mise en cache a échoué. Pour contourner ces cas, vous devez enregistrer les URL du CDN de Braze dans la liste des domaines à ignorer par ces bibliothèques.

#### Domaines {#domains}

La liste complète des domaines du CDN est la suivante :

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Exemples {#examples}

Vous trouverez ci-dessous les bibliothèques connues pour entrer en conflit avec la mise en cache des ressources de Braze, ainsi qu'un exemple de code permettant de contourner le problème. Si votre projet utilise une bibliothèque qui provoque une erreur de ressource indisponible et qui n'est pas répertoriée ici, consultez la documentation de cette bibliothèque pour des API d'utilisation similaires.

##### Netfox

{% tabs %}
{% tab Swift %}
```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
[NFX.sharedInstance ignoreURLs:@[@"https://cdn.braze.com"]];
```
{% endtab %}
{% endtabs %}

##### NetGuard

{% tabs %}
{% tab Swift %}
```swift
NetGuard.blackListHosts.append(contentsOf: ["cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
NSMutableArray<NSString *> *blackListHosts = [NetGuard.blackListHosts mutableCopy];
[blackListHosts addObject:@"cdn.braze.com"];
NetGuard.blackListHosts = blackListHosts;
```
{% endtab %}
{% endtabs %}

##### XNLogger

{% tabs %}
{% tab Swift %}
```swift
let brazeAssetsHostFilter = XNHostFilter(host: "https://cdn.braze.com")
XNLogger.shared.addFilters([brazeAssetsHostFilter])
```
{% endtab %}
{% tab Objective-C %}
```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```
{% endtab %}
{% endtabs %}