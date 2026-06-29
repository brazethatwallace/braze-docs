{% multi_lang_include in-app_messages/troubleshooting.md sdk="iOS" %}

### Solução de problemas de carregamento de ativos (`NSURLError` código `-1008`) {#asset-loading}

Ao integrar a Braze com bibliotecas de registro de rede de terceiros, os desenvolvedores geralmente se deparam com um `NSURLError` com o código de domínio `-1008`. Esse erro indica que ativos como imagens e fontes não puderam ser recuperados ou não foram armazenados em cache. Para contornar esses casos, você precisa registrar as URLs do CDN da Braze na lista de domínios que devem ser ignorados por essas bibliotecas.

#### Domínios {#domains}

A lista completa de domínios CDN está listada abaixo:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Exemplos {#examples}

Abaixo estão as bibliotecas conhecidas por entrar em conflito com o cache de ativos da Braze, juntamente com código de exemplo para contornar o problema. Se seu projeto usa uma biblioteca que causa um erro de recurso indisponível e não está listada abaixo, consulte a documentação dessa biblioteca para APIs de uso semelhantes.

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