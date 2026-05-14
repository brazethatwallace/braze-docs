---
nav_title: 동적 코드 생성
article_title: Punchh 동적 코드 생성
page_order: 2
description: "이 참조 문서에서는 Braze에서 Punchh 동적 코드 생성을 사용하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
---

# Punchh를 활용한 동적 코드 생성 {#dynamic-code-generation-with-punchh}

> 쿠폰 코드는 단일 사용자가 사용할 수 있는 고유 코드입니다(단일 또는 다중 사용). Punchh 프레임워크는 모바일 앱 또는 POS(판매 시점) 시스템에서 처리할 수 있는 쿠폰 코드를 생성합니다.

_이 통합은 Punchh에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Punchh 쿠폰 프레임워크와 Braze를 사용하면 다음과 같은 시나리오를 구현할 수 있습니다:

- 게스트가 이메일에서 쿠폰 생성 링크를 클릭할 때 쿠폰 코드 생성: 쿠폰 코드가 동적으로 생성되어 웹 페이지에 표시됩니다.
- 게스트가 이메일을 열 때 쿠폰 코드 생성: 쿠폰 코드가 동적으로 생성되어 이메일 내 이미지로 표시됩니다.

## 동적 쿠폰 코드 생성 통합 {#integrating-dynamic-coupon-code-generation}

### 1단계: 쿠폰 Campaign 생성 {#step-1-create-a-coupon-campaign}

1. Punchh 쿠폰 Campaign을 사용하여 다음 이미지와 같이 동적 생성 쿠폰 Campaign을 생성합니다.
2. Punchh 쿠폰 프레임워크가 동적 쿠폰 생성을 활성화하기 위해 다음 매개변수를 생성합니다:
    - 동적 쿠폰 생성 토큰: 암호화를 위해 시스템에서 생성된 보안 토큰입니다.
    - 동적 쿠폰 생성 URL: 이 URL은 비즈니스 요구 사항에 따라 이메일에 링크 또는 이미지로 삽입됩니다.

![Punchh에서 쿠폰 Campaign을 생성하기 위한 양식입니다.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### 2단계: 서명 생성 및 URL 구성 {#step-2-generate-signature-and-construct-url}

JWT.IO 라이브러리는 JSON 웹 토큰을 디코딩, 검증 및 생성합니다. 이는 두 당사자 간에 클레임을 안전하게 표현하기 위한 개방형 산업 표준 RFC 7519 메서드입니다.

다음 `ClaimType` 이름을 사용하여 게스트와 쿠폰의 고유성을 보장할 수 있습니다:

- `campaign_id`: 시스템에서 생성된 Punchh Campaign ID를 나타냅니다.
- `email`: 사용자의 이메일 주소를 나타냅니다.
- `first_name`: 사용자의 이름을 캡처합니다.
- `last_name`: 사용자의 성을 캡처합니다.

Punchh 동적 쿠폰 코드 API를 사용하려면 JWT 토큰을 구성해야 합니다. 사용하려는 채널의 메시지 본문에 다음 Liquid 템플릿을 Braze 대시보드에 추가하세요:

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


다음을 교체하세요:

| 플레이스홀더 | 설명 |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | 동적 쿠폰 생성 토큰입니다. |
| `CAMPAIGN_ID`                     | Campaign ID입니다.                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Generate signature and construct URL" }

### 3단계: 메시지 본문에 쿠폰 코드 추가 {#step-3-append-coupon-code-to-message-body}

#### Punchh 웹 페이지로 연결 {#linking-to-punchh-web-page}

Punchh에서 호스팅하는 웹 페이지로 연결하려면 [이전에 생성한](#step-1-create-a-coupon-campaign-in-punchh) 동적 생성 URL에 `{% raw %}{{jwt}}{% endraw %}`를 추가하세요. 링크는 다음과 유사해야 합니다:

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

사용자가 쿠폰 URL을 클릭하면 Punchh에서 호스팅하는 웹 페이지로 리디렉션되며, 생성된 쿠폰이 표시됩니다.

![사용자가 쿠폰 코드를 성공적으로 생성한 후의 확인 메시지 예시입니다.]({% image_buster /assets/img/punchh/punchh7.png %})

#### JSON을 통해 일반 텍스트로 코드 추출 {#extracting-code-via-json-as-plain-text}

JSON 응답을 반환하려면 [이전에 생성한](#step-1-create-a-coupon-campaign-in-punchh) 동적 생성 URL에 `{% raw %}{{jwt}}{% endraw %}`를 추가한 다음, URL 문자열에서 토큰 뒤에 `.json`을 추가하세요. 링크는 다음과 유사해야 합니다:

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

그런 다음 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)를 활용하여 모든 메시지 본문에 일반 텍스트로 코드를 삽입할 수 있습니다. 예를 들어:

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### 이메일 콘텐츠 내 이미지에 연결 {#linking-an-image-inside-email-content}

쿠폰 코드를 이미지 내에 연결하려면:

1. [이전에 생성한](#step-1-create-a-coupon-campaign-in-punchh) 동적 생성 URL에 `{% raw %}{{jwt}}{% endraw %}`를 추가합니다.
2. URL 문자열에서 토큰 뒤에 `.png`를 추가합니다.
3. HTML {% raw %}`<img>`{% endraw %} 태그에 링크를 삽입합니다.

{% tabs local %}
{% tab 입력 예시 %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab 출력 예시 %}
![쿠폰 코드 이미지 태그의 렌더링된 출력입니다.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## 오류 메시지 {#error-messages}

| 오류 코드 | 오류 메시지 | 설명 |
| --- | --- | --- |
| `coupon_code_expired` | This promo code has expired | 코드가 설정된 만료일 이후에 사용되었습니다. |
| `coupon_code_success` | Congratulations, Promo Code Applied Successfully. | 코드가 성공적으로 사용되었습니다. |
| `coupon_code_error` | Please enter a valid promo code | 사용된 코드가 유효하지 않습니다. |
| `coupon_code_type_error` | Incorrect coupon type. This coupon can only be redeemed at `%{coupon_type}`. | POS에서 사용해야 하는 코드가 모바일 앱에서 사용된 경우 이 오류가 발생합니다. |
| `usage_exceeded` | The usage for this coupon code's campaign is full. Please try next time. | 코드 사용량이 허용된 사용자 수를 초과했습니다. 예를 들어, 대시보드 구성에서 코드를 3,000명의 사용자가 사용할 수 있도록 허용했는데 사용자 수가 3,000명을 초과하면 이 오류가 발생합니다. |
| `usage_exceeded_by_guest` | This promo code has already been processed. | 사용자의 코드 사용량이 해당 사용자가 사용할 수 있는 횟수를 초과했습니다. 예를 들어, 대시보드 구성에서 단일 코드를 사용자당 3회 사용할 수 있도록 허용한 경우, 그 이상 사용하면 이 오류가 발생합니다. |
| `already_used_by_other_guest` | This promo code has already been used by some other guest. | 다른 사용자가 이미 해당 코드를 사용했습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Error messages" }