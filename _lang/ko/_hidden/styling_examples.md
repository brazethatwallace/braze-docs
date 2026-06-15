---
nav_title: 스타일링 예시
article_title: 스타일링 예시
description: "Braze Docs에서 헤더, 탭, 코드 블록 등 페이지가 스타일링되는 방식입니다."
page_order: 8
noindex: true
---

# 스타일링 예시 {#styling-examples}

Braze Docs에서 헤더, 탭, 코드 블록 등 페이지가 스타일링되는 방식입니다.

## 헤더 테스트 {#header-test}

{% tabs %}
{% tab Styling %}

# H1 배너 {#h1-banner}
H1 텍스트

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

## H2 배너 {#h2-banner}
H2 텍스트

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

### H3 배너 {#h3-banner}
H3 텍스트

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### H4 배너 {#h4-banner}
H4 텍스트

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

##### H5 배너 {#h5-banner}
H5 텍스트

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

###### H6 배너 {#h6-banner}
H6 텍스트

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

{% endtab %}
{% tab Markdown %}

```
# H1 Banner

## H2 Banner

### H3 Banner

#### H4 Banner

##### H5 Banner

###### H6 Banner
```
{% endtab %}
{% endtabs %}

## 커스텀 헤더 앵커 {#custom-header-anchor}

헤더에 앵커를 추가하려면 헤더가 있는 줄 끝에 다음 코드를 추가합니다. `anchor-text`를 이 헤더의 앵커로 바꿉니다. 소문자를 사용하고 단어 사이에 하이픈을 넣습니다.

```
# Heading Text {#anchor-text}
```

커스텀 앵커가 있는 헤더에 링크하려면 숫자 기호 `#` 뒤에 커스텀 앵커를 붙인 표준 링크를 만듭니다.

{% raw %}
```
Here is my [link](#anchor-text)
```
{% endraw %}

## 글꼴 테스트 {#font-test}

{% tabs %}
{% tab Styling %}

일반 텍스트

*강조 텍스트*

**굵게**

_**굵은 강조**_

~~취소선~~

{% endtab %}
{% tab Markdown %}
```
Normal Text

*Emphasize Text*

**Bold**

_**Bold Emphasize**_

~~Strikethrough~~
```
{% endtab %}
{% endtabs %}

## 인용 테스트 {#quote-test}

{% tabs %}
{% tab Styling %}
> 인용된 텍스트

#### 인라인 인용 {#inline-quote}
Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

#### 인용 블록 {#quote-chunk}
```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor.
```
{% endtab %}
{% tab Markdown %}
```
> Quoted Text

Lorem ipsum dolor ``sit amet, consectetur adipiscing elit``. Sed nec tortor at lectus tempus tempor.

``` Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. ```
```
{% endtab %}
{% endtabs %}

## 테이블 테스트

{% tabs %}
{% tab Styling %}
| 인스턴스 | 대시보드 URL                                                         | REST 엔드포인트                   |
| -------- | --------------------------------------------------------------------- | ------------------------------- |
| US-01    | `https://dashboard.braze.com` 또는<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                      | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                      | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                      | `https://rest.iad-04.braze.com` |
| US-05    | `https://dashboard-05.braze.com`                                      | `https://rest.iad-05.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                      | `https://rest.iad-06.braze.com` |
| US-07    | `https://dashboard-07.braze.com`                                      | `https://rest.iad-07.braze.com` |
| US-08    | `https://dashboard-08.braze.com`                                      | `https://rest.iad-08.braze.com` |
| EU-01    | `https://dashboard.braze.eu` 또는<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
| AU-01    | `https://dashboard.au-01.braze.com/`                                  | `https://rest.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table Test" }
{% endtab %}
{% tab Markdown %}
```
| Instance | Dashboard URL                                                         | REST Endpoint                   |
|----------|-----------------------------------------------------------------------|---------------------------------|
| US-01    | `https://dashboard.braze.com` or<br> `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` |
| US-02    | `https://dashboard-02.braze.com`                                      | `https://rest.iad-02.braze.com` |
| US-03    | `https://dashboard-03.braze.com`                                      | `https://rest.iad-03.braze.com` |
| US-04    | `https://dashboard-04.braze.com`                                      | `https://rest.iad-04.braze.com` |
| US-05    | `https://dashboard-05.braze.com`                                      | `https://rest.iad-05.braze.com` |
| US-06    | `https://dashboard-06.braze.com`                                      | `https://rest.iad-06.braze.com` |
| US-07    | `https://dashboard-07.braze.com`                                      | `https://rest.iad-07.braze.com` |
| US-08    | `https://dashboard-08.braze.com`                                      | `https://rest.iad-08.braze.com` |
| EU-01    | `https://dashboard.braze.eu` or<br> `https://dashboard-01.braze.eu`   | `https://rest.fra-01.braze.eu`  |
| EU-02    | `https://dashboard-02.braze.eu`                                       | `https://rest.fra-02.braze.eu`  |
| AU-01    | `https://dashboard.au-01.braze.com/`                                  | `https://rest.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table Test" }
```
{% endtab %}
{% endtabs %}

#### 열별 테이블 줄바꿈 초기화

열별로 테이블 줄바꿈을 초기화하려면 다음 구문을 사용합니다:

```markdown
{: .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM .reset-td-br-NUM aria-label="Resetting Table word-break by column" }
```

`NUM`을 해당 열 번호로 바꿉니다. 최대 4개 열까지 지원됩니다. 열이 4개 미만인 경우 추가 `.reset-td-br-NUM` 자리 표시자를 제거합니다. 테이블은 다음과 유사해야 합니다:

```markdown
| Event Name                                                       | Feed Type              | Description                                                  | Custom Attributes                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | An email was successfully delivered to a User's mail server. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | User opened an email.                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App Message Impression                                        | Platform-specific Feed | User viewed an In-App Message.                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }

```
{% tabs local %}
{% tab 이전 %}

| 이벤트 이름                                                       | 피드 유형              | 설명                                                  | 커스텀 속성                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | 이메일이 사용자의 메일 서버에 성공적으로 전달되었습니다. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | 사용자가 이메일을 열었습니다.                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | 사용자가 인앱 메시지를 조회했습니다.                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |

{% endtab %}
{% tab 이후 %}

| 이벤트 이름                                                       | 피드 유형              | 설명                                                  | 커스텀 속성                                                             |
| ---------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| UNBROKENWORDTHATISVERYLONGUNBROKENWORDTHATISVERYLONG             | Unbound Feed           | 이메일이 사용자의 메일 서버에 성공적으로 전달되었습니다. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| `UNBROKENHIGHLIGHTTHATISVERYLONGUNBROKENHIGHLIGHTTHATISVERYLONG` | Unbound Feed           | 사용자가 이메일을 열었습니다.                                        | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`           |
| In-App-Message-Impression                                        | Platform-specific Feed | 사용자가 인앱 메시지를 조회했습니다.                               | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Resetting Table word-break by column" }
{% endtab %}
{% endtabs %}

## 링크 테스트
{% tabs %}
{% tab Styling %}
여기 링크: [Braze.com](https://www.braze.com){: height="36px" width="36px"}
{% endtab %}
{% tab Markdown %}
```
[Braze.com](https://www.braze.com)
```
{% endtab %}
{% endtabs %}

## 이미지 테스트
{% tabs %}
{% tab Styling %}
이미지: ![로고]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

#### 링크된 이미지 테스트

링크된 이미지: [![Braze]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}](https://www.braze.com)

#### 이미지 스타일링

![텍스트]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

#### 이미지 앵커링

![텍스트]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%; color: green" }
<br><br><br><br><br>
{% endtab %}
{% tab Markdown %}

```
![Logo]({% image_buster /assets/img/braze-logo-mark.png %}){: style="max-width:30%;"}

[![Braze]({% image_buster /assets/img/braze-logo-mark.png %})](https://www.braze.com)

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="max-width:30%; color: green" }

![Text]({% image_buster /assets/img/logo-braze-fa.svg %}){: style="float:right;max-width:30%;" }
```
{% endtab %}
{% endtabs %}

## 갤러리 테스트
{% tabs %}
{% tab Styling %}
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d <br> 이것은 [링크](https://www.braze.com)입니다.
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e <br> 이것은 또 다른 `comment`입니다.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68 <br> 이것은 또 다른 **comment**입니다.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **이미지 제목** <br> 줄바꿈이 되는지 확인하는 테스트입니다.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a <br> 이것은 일반 코멘트입니다.
{% endgallery %}
{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% gallery %}
{{site.baseurl}}/assets/img_archive/EBTH_Email.png?bf892368baf287cba5ab9a6e3b09431d  <br> This is a [link](https://www.braze.com).
{{site.baseurl}}/assets/img_archive/iHeartRadio_Email.png?ecd2c8fe148939b7de957fe85cd6317e  <br> This is another `comment`.
{{site.baseurl}}/assets/img_archive/Saucey_Email.png?b9768937a1cc12d4c08e55a52e700d68  <br> This is yet another **comment**.
{{site.baseurl}}/assets/img/schellman_iso27001_seal_grey_CMYK_300dpi_jpg.png?1b1fb9dbb80b0332c62512dcf9c83258 <br> **IMAGE TITLE** <br> This is a test to see if it will line break.
{{site.baseurl}}/assets/img/SOC2.png?6338040be8e98c4c9abe1f35b3e43e3a  <br> This is a regular comment.
{% endgallery %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 인터랙티브 이미지 테스트
{% tabs %}
{% tab Styling %}
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
{% endtab %}
{% tab Markdown %}
```
<div class="iactiveImg" data-ii="6967"></div><script src="https://interactive-img.com/js/include.js"></script>
```
{% endtab %}
{% endtabs %}
<!--- Leaving formatting here just in case it's important...
<div style="position: relative; padding-bottom: 83%; padding-top: 0; height: 0;"><iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border-width:0px; max-width:100%; overflow-y:auto;" width="100%" height="100%" src="https://interactive-img.com/view?id=6967&iframe=true"></iframe></div>
-->

## 코드 스니펫 테스트

{% tabs %}
{% tab Styling %}
#### 코드 테스트 Objective C
```objc
- (void)submitFeedback:(ABKFeedback * )feedback
 withCompletionHandler:(nullable void (^)(ABKFeedbackSentResult feedbackSentResult))completionHandler;
```

#### 코드 테스트 Swift
```swift
Appboy.sharedInstance()?.submitFeedback(feedback) { (feedbackSentResult) in
      print("Feedback sent: (feedbackSentResult)")
    }
```

#### 코드 테스트 Java
```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

#### 코드 테스트 json
```json
{
   "attributes" : "Attributes" ,
   "events" : ["Array", "Of", "Object"],
   "purchases" : ["Array" ,"Of" ,"Purchase" ,"Object"]
}
```

#### 코드 테스트 JavaScript
```javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

#### Pygments 테스트
```python
#!/usr/bin/python3

from engine import RunForrestRun

"""Test code for syntax highlighting!"""

class Foo:
	def __init__(self, var):
		self.var = var
		self.run()

	def run(self):
		RunForrestRun()  # run along!

```
{% endtab %}
{% tab Markdown %}
![마크다운 예시]({% image_buster /assets/img_archive/code_snippet.png %})
{% endtab %}
{% endtabs %}

## 알림 테스트

{% tabs %}
{% tab Styling %}

{% alert tip %}이것은 팁입니다{% endalert %}

{% alert note %}이것은 참고 사항입니다{% endalert %}

{% alert important %}이것은 중요한 알림입니다{% endalert %}

{% alert warning %}이것은 경고입니다{% endalert %}

{% alert update %}이것은 업데이트입니다{% endalert %}

{% endtab %}
{% tab Markdown %}
{% raw %}
```
{% alert tip %}
This is a tip
{% endalert %}

{% alert note %}
This is a note
{% endalert %}

{% alert important %}
This is a important alert
{% endalert %}

{% alert warning %}
This is a warning
{% endalert %}

{% alert update %}
This is a update
{% endalert %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 임베디드 비디오 테스트
{% tabs %}
{% tab Styling %}
#### 임베디드 비디오/YouTube
기본값은 YouTube 임베디드입니다.
{% multi_lang_include video.html id="9SrKbY4BV2E" source="youtube" %}

#### 임베디드 비디오/Wistia
Wistia 비디오를 임베드합니다.
{% multi_lang_include video.html id="c5lgi4xnvo" source="wistia" %}

#### 임베디드 비디오 오른쪽 정렬
{% multi_lang_include video.html id="9SrKbY4BV2E" align="right" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.

#### 임베디드 비디오 왼쪽 정렬
{% multi_lang_include video.html id="9SrKbY4BV2E" align="left" source="youtube" %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec tortor at lectus tempus tempor. Suspendisse tellus diam, finibus eu dictum non, varius et ipsum.
<br /><br />

#### Loom 예시
* `source="loom"` 사용
{% multi_lang_include video.html id="c1d3199463c448e8918f046265b54eb2" source="loom" %}

{% endtab %}
{% tab Markdown %}

YouTube 비디오를 임베드하려면 YouTube ID가 필요합니다. URL에서 `v=` 뒤에 나타납니다. 예를 들어, `https://www.youtube.com/watch?v=VR1qn1OBP7k`의 ID는 `VR1qn1OBP7k`입니다.

{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" source="youtube" %}
```
{% endraw %}

오른쪽 또는 왼쪽으로 정렬하고 최대 너비를 50%로 제한하려면 `align` 파라미터를 `left` 또는 `right`로 사용합니다:
{% raw %}
```html
{% multi_lang_include video.html id="[youtube_id]" align="left" source="youtube" %}

{% multi_lang_include video.html id="[youtube_id]" align="right" source="youtube" %}
```
{% endraw %}

Loom 예시:
{% raw %}
```html
{% multi_lang_include video.html id="[lid]" source="loom" %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### 고해상도를 위한 상태 배치가 포함된 추천 비디오 레이아웃

고해상도 디스플레이를 위해 왼쪽에 정적 비디오를 배치하는 추천 비디오 레이아웃을 사용하려면 페이지의 YAML 헤더에 `video_id`와 `video_type`(예: `youtube`)을 추가합니다. 기본적으로 `video_source`는 `youtube`로 설정되어 있습니다.

{% raw %}
```yaml
layout: featured_video
video_id: [video_id]
video_source: youtube
```
{% endraw %}

## 목록 테스트
{% tabs %}
{% tab Styling %}
#### 글머리 기호

- 목록 1
  - 하위 목록 1
- 목록 2
  - 하위 목록 2a
    - 하위 하위 목록 2
- 목록 3

#### 번호 매기기

1. 목록 1
   - 하위 목록 1
2. 목록 2
3. 목록 3
   - 하위 목록 3a
   - 하위 목록 3b
     - 하위 하위 목록 3
4. 목록 4
    1. 하위 목록 4a
        1. 하위 하위 목록 4
    2. 하위 목록 4b
        1. 하위 하위 목록 4

{% endtab %}
{% tab Markdown %}
```
#### Bullet

- List 1
  - Sub List 1
- List 2
  - Sub List 2a
    - Sub Sub List 2
- List 3

#### Numbered

1. List 1
   - Sub List 1
2. List 2
3. List 3
   - Sub List 3a
   - Sub List 3b
     - Sub Sub List 3
4. List 4
    1. Sub list 4a
        1. Sub Sub List 4
    2. Sub list 4b
        1. sub sub list 4
```
{% endtab %}
{% endtabs %}

## 접을 수 있는 콘텐츠 테스트 {#collapsible-content}
{% tabs %}
{% tab Styling %}
{% details 클릭하여 펼치기 %}
#### 보세요! 숨겨진 코드 블록입니다!

```python
print("hello world!")
```
{% enddetails %}
{% endtab %}
{% tab Markdown %}
{% raw %}
```liquid
{% details Click me to Expand %}
...
{% enddetails %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 탭 테스트

#### 커스텀 탭

{% tabs local %}
{% tab OBJECTIVE-C %}

`AppDelegate.m` 파일에 다음 코드 줄을 추가합니다:

```objc
{% if include.platform == 'iOS' %}#import "Appboy-iOS-SDK/AppboyKit.h"{% else %}#import <AppboyTVOSKit/AppboyKit.h>{% endif %}
```

`AppDelegate.m` 파일 내에서 `application:didFinishLaunchingWithOptions` 메서드 안에 다음 스니펫을 추가합니다:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

{% endtab %}
{% tab swift %}

CocoaPods 또는 Carthage로 Braze SDK를 통합하는 경우 `AppDelegate.swift` 파일에 다음 코드 줄을 추가합니다:

```swift
{% if include.platform == 'iOS' %}#import Appboy_iOS_SDK{% else %}#import AppboyTVOSKit{% endif %}
```

Swift 프로젝트에서 Objective-C 코드를 사용하는 방법에 대한 자세한 내용은 [Apple 개발자 문서][apple_initial_setup_19]를 참조하세요.

`AppDelegate.swift`에서 `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`에 다음 스니펫을 추가합니다:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```
{% endtab %}
{% endtabs %}

#### 사용법
{% raw %}
**탭**을 `{% tabs %}` 및 `{% endtabs %}`로 감쌉니다.
개별 **탭**은 Liquid 코드와 탭 이름 `{% tab [Tab name] %}` 및 `{% endtab %}`로 감쌉니다.
{% endraw %}

{% alert important %}
 페이지의 탭 수는 일관되어야 합니다. 그렇지 않으면 탭 콘텐츠가 숨겨질 수 있습니다.
 예를 들어, 한 탭 세트에 `C++`, `C-Sharp`, `JS`가 있고 다른 탭 세트에 `C-Sharp`와 `JS`만 있는 경우,
누군가 `C++`를 클릭하면 다른 섹션에 아무것도 표시되지 않습니다. 해결 방법은 아래의 로컬 탭 옵션을 참조하세요.
{% endalert %}

{% raw %}
```liquid
{% tabs %}
{% tab objective-c %}
Content of objective-c
{% endtab %}
{% tab swift %}
Content of swift
{% endtab %}
{% endtabs %}
```
{% endraw %}

#### 로컬 탭
특정 섹션의 탭 콘텐츠만 변경하는 자체 포함 탭의 경우 상위 탭 블록에서 local 파라미터를 사용합니다.

{% raw %}
```liquid
{% tabs local %}
...
{% endtabs %}
```
{% endraw %}

#### 하위 탭
탭 안의 탭에는 `subtabs`와 `subtab`을 사용할 수 있습니다. 기본 설정은 `local`입니다.
글로벌 `subtabs`의 경우 `global` 옵션을 사용합니다: {% raw %}`{% subtabs global %}`{% endraw %}

{% tabs local %}
{% tab Tab 1 %}
탭 콘텐츠 1
{% subtabs %}
{% subtab Subtab 1a %}
하위 탭 1a 콘텐츠
{% endsubtab %}
{% subtab Subtab 2a %}
하위 탭 2a 콘텐츠
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
탭 콘텐츠 2
{% subtabs %}
{% subtab Subtab 1b %}
하위 탭 1b 콘텐츠
{% endsubtab %}
{% subtab Subtab 2b %}
하위 탭 2b 콘텐츠
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### 마크다운
{% raw %}
```
{% tabs local %}
{% tab Tab 1 %}
tab content 1
{% subtabs %}
{% subtab Subtab 1a %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2a %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Tab 2 %}
tab content 2
{% subtabs %}
{% subtab Subtab 1b %}
Subtab 1a content
{% endsubtab %}
{% subtab Subtab 2b %}
Subtab 2a content
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
```
{% endraw %}

[1]: {% image_buster /assets/img_archive/code_snippet.png %}