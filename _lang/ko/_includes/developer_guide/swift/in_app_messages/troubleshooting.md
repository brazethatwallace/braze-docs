{% multi_lang_include in-app_messages/troubleshooting.md sdk="iOS" %}

### 자산 로딩 문제 해결(`NSURLError` 코드 `-1008`) {#asset-loading}

Braze를 서드파티 네트워크 로깅 라이브러리와 함께 통합할 때, 개발자는 도메인 코드 `-1008`과 관련된 `NSURLError`를 흔히 접할 수 있습니다. 이 오류는 이미지 및 글꼴과 같은 자산을 검색할 수 없거나 캐시에 실패했음을 나타냅니다. 이러한 경우를 해결하려면 해당 라이브러리에서 무시해야 하는 도메인 목록에 Braze CDN URL을 등록해야 합니다.

#### 도메인 {#domains}

CDN 도메인의 전체 목록은 아래와 같습니다:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### 예시 {#examples}

다음은 Braze 자산 캐싱과 충돌하는 것으로 알려진 라이브러리와 문제를 해결하기 위한 예제 코드입니다. 프로젝트에서 리소스 사용 불가 오류를 발생시키는 라이브러리를 사용하고 있으나 아래에 나열되지 않은 경우, 해당 라이브러리의 설명서에서 유사한 사용 API를 참조하세요.

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