{% multi_lang_include in-app_messages/troubleshooting.md SDK or Software-Development-Kit="iOS" %}

### Fehlerbehebung beim Laden von Assets (`NSURLError`-Code `-1008`) {#asset-loading}

Bei der Integration von Braze zusammen mit Netzwerkprotokollierungsbibliotheken von Drittanbietern stoßen Entwickler:innen häufig auf einen `NSURLError` mit dem Domain-Code `-1008`. Dieser Fehler zeigt an, dass Assets wie Bilder und Schriftarten nicht abgerufen werden konnten oder nicht in den Cache aufgenommen wurden. Um solche Fälle zu umgehen, müssen Sie die CDN-URLs von Braze in die Liste der Domains eintragen, die von diesen Bibliotheken ignoriert werden sollen.

#### Domains

Die vollständige Liste der CDN-Domains lautet wie folgt:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Beispiele {#examples}

Die folgenden Bibliotheken stehen bekanntermaßen mit dem Asset-Caching von Braze in Konflikt. Zu jeder finden Sie Beispiel-Code, um das Problem zu umgehen. Wenn Ihr Projekt eine Bibliothek verwendet, die einen Fehler wegen nicht verfügbarer Ressourcen verursacht und hier nicht aufgeführt ist, konsultieren Sie die Dokumentation dieser Bibliothek für ähnliche APIs.

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

##### Wormholy

{% tabs %}
{% tab Swift %}
```swift
Wormholy.ignoredHosts = ["cdn.braze.com"]
```
{% endtab %}
{% tab Objective-C %}
```objc
Wormholy.ignoredHosts = @[@"cdn.braze.com"];
```
{% endtab %}
{% endtabs %}