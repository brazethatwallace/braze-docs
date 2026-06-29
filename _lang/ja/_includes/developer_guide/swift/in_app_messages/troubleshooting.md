{% multi_lang_include in-app_messages/troubleshooting.md sdk="iOS" %}

### アセット読み込みのトラブルシューティング（`NSURLError`コード`-1008`） {#asset-loading}

Brazeをサードパーティのネットワークロギングライブラリーと統合する際、開発者はドメインコード`-1008`の`NSURLError`に遭遇することがよくあります。このエラーは、画像やフォントなどのアセットを取得できなかったか、キャッシュに失敗したことを示しています。このようなケースを回避するには、Braze CDNのURLを、これらのライブラリーによって無視されるべきドメインのリストに登録する必要があります。

#### ドメイン {#domains}

CDNドメインの全リストは以下の通りです。

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### 例 {#examples}

以下は、Brazeのアセットキャッシュと競合することが知られているライブラリーと、問題を回避するためのサンプルコードです。利用できないリソースエラーを引き起こすライブラリーをプロジェクトで使用しており、以下にリストされていない場合は、そのライブラリーのドキュメントを参照して、同様の使用方法のAPIを確認してください。

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