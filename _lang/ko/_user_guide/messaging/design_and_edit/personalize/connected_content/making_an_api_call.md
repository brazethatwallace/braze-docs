---
nav_title: 연결된 콘텐츠 호출하기
article_title: 연결된 콘텐츠 API 호출하기
page_order: 0
description: "이 참조 문서에서는 연결된 콘텐츠 API 호출 방법과 유용한 예제 및 고급 연결된 콘텐츠 사용 사례를 다룹니다."
search_rank: 2
toc_headers: h2
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}연결된 콘텐츠 API 호출하기 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomconnected-content-stylefloatrightwidth120pxborder0-classnoimgbordermake-a-connected-content-api-call}

> 연결된 콘텐츠를 사용하면 API로 접근 가능한 모든 정보를 사용자에게 보내는 메시지에 직접 삽입할 수 있습니다. 웹 서버에서 직접 또는 공개적으로 접근 가능한 API에서 콘텐츠를 가져올 수 있습니다.<br><br>이 페이지에서는 연결된 콘텐츠 API 호출 방법, 고급 연결된 콘텐츠 사용 사례, 오류 처리 등을 다룹니다.

## 연결된 콘텐츠 호출 볼륨 이해하기 {#understanding-connected-content-call-volume}

{% alert important %}
한 번의 발송이 한 번의 연결된 콘텐츠 호출과 같지 않습니다. Braze는 메시지 발송과 연결된 콘텐츠 요청 간의 1:1 비율을 보장하지 않습니다. 시스템은 호출 수를 최소화하는 것보다 올바른 메시지 렌더링과 전달을 우선시하도록 설계되어 있습니다. 엔드포인트는 수신자 수 또는 발송된 메시지 수보다 더 많은 요청을 처리할 수 있도록 구축해야 합니다.
{% endalert %}

Braze는 수신자당 동일한 연결된 콘텐츠 API 호출을 두 번 이상 수행할 수 있습니다. 일반적인 이유는 다음과 같습니다.

- **여러 파트가 있는 이메일:** 단일 이메일은 HTML 본문, 일반 텍스트 본문, 가속 모바일 페이지(가속 모바일 페이지) 버전(있는 경우)에 대해 별도의 렌더링 패스를 트리거할 수 있습니다. 각 패스는 해당 파트에서 연결된 콘텐츠를 트리거할 수 있으므로, 한 명의 수신자가 여러 개의 동일하거나 유사한 호출을 생성할 수 있습니다.
- **유효성 검사 및 재시도:** 메시지 페이로드는 유효성 검사, 재시도 로직 또는 기타 내부 목적으로 수신자당 여러 번 렌더링될 수 있습니다.
- **채널 동작:** 연결된 콘텐츠는 메시지가 렌더링될 때 실행됩니다. 인앱 메시지의 경우, 메시지는 노출 시점에 렌더링됩니다.

로그에서 발송 수 또는 수신자 수보다 더 많은 연결된 콘텐츠 호출이 보인다면, 이는 예상되는 동작입니다. 부하를 줄이고 확장을 계획하는 방법에 대한 안내는 [대용량 엔드포인트 모범 사례](#best-practices-for-high-volume-endpoints)를 참조하세요.

## 연결된 콘텐츠 호출 보내기 {#send-a-connected-content-call}

연결된 콘텐츠 호출을 보내려면 {% raw %}`{% connected_content %}`{% endraw %} 태그를 사용합니다. 이 태그를 사용하여 `:save`를 통해 변수를 할당하거나 선언할 수 있습니다. 이러한 변수의 요소들은 나중에 메시지에서 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid)를 사용하여 참조할 수 있습니다.

### API 호출 분석 {#break-down-the-api-call}

다음 예제는 Sunrise-Sunset API를 사용하며, 오늘의 일출 시간을 메시지에 포함합니다:

{% raw %}
```
{% connected_content https://api.sunrise-sunset.org/v2?lat=40.7128&lng=-74.0060&date=today :save result %}
Hi there, today's sunrise in NYC is at {{result.sunrise}}.
```
{% endraw %}

각 구성 요소의 역할은 다음과 같습니다:

| 구성 요소 | 역할 |
| --- | --- |
| `connected_content` 태그 | 메시지를 렌더링하는 동안 HTTP 요청을 수행하도록 Braze에 지시합니다. |
| `https://api.sunrise-sunset.org/v2` | Braze가 호출하는 API 엔드포인트입니다. |
| `lat=40.7128&lng=-74.0060` | 뉴욕시 좌표를 위한 쿼리 매개변수입니다. |
| `date=today` | 해당 좌표의 당일 데이터를 요청합니다. |
| `:save result` | API 응답을 `result`라는 로컬 변수에 저장합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API 호출 분석" }

### Sunrise-Sunset API 응답 작동 방식 {#how-the-sunrise-sunset-api-response-works}

이 엔드포인트는 `sunrise`, `sunset`, `tzid` 등의 최상위 필드가 포함된 JSON을 반환합니다. 시간은 기본적으로 해당 위치의 시간대로 반환됩니다(이 예제에서는 뉴욕 시간).

예를 들어, 응답 형태는 다음과 유사합니다:

```json
{
  "date": "2026-07-23",
  "tzid": "America/New_York",
  "sunrise": "2026-07-23T05:42:11-04:00",
  "sunset": "2026-07-23T20:21:32-04:00"
}
```

### API 응답을 Liquid에 매핑하기 {#map-the-api-response-to-liquid}

응답이 `result`로 저장되었으므로, 해당 객체에서 각 필드를 직접 참조할 수 있습니다.

{% raw %}
```liquid
{{result.sunrise}}
{{result.sunset}}
{{result.tzid}}
```
{% endraw %}

연결된 콘텐츠에서 JSON을 저장할 때마다 이 패턴을 사용합니다:

1. `:save`를 사용하여 API 응답을 저장합니다.
2. JSON 응답에서 원하는 필드를 찾습니다.
3. Liquid에서 `saved_variable.field_name` 형태로 참조합니다.

### 변수 추가하기 {#add-variables}

연결된 콘텐츠 요청을 할 때 고객 프로필 속성을 URL 문자열의 변수로 포함할 수도 있습니다.

예를 들어, 사용자의 이메일 주소와 ID를 기반으로 콘텐츠를 반환하는 웹 서비스가 있을 수 있습니다. 골뱅이 기호(@)와 같은 특수 문자가 포함된 속성을 전달하는 경우, 다음 이메일 주소 속성에 표시된 것처럼 Liquid 필터 `url_param_escape`를 사용하여 URL에서 허용되지 않는 문자를 URL에 적합한 이스케이프 버전으로 대체해야 합니다.

{% raw %}
```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
속성 값은 Braze의 Liquid 구문에서 올바르게 작동하려면 `${}`로 감싸야 합니다.
{% endalert %}

연결된 콘텐츠 요청은 GET 및 POST 요청만 지원합니다.

## 오류 처리 {#error-handling}

URL을 사용할 수 없어 404 페이지에 도달하면, Braze는 해당 위치에 빈 문자열을 렌더링합니다. URL이 HTTP 500 또는 502 페이지에 도달하면, 재시도 로직에서 URL이 실패합니다.

엔드포인트가 JSON을 반환하는 경우, `connected` 값이 null인지 확인한 다음 [조건부로 메시지를 중단]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)할 수 있습니다. Braze는 포트 80(HTTP) 및 443(HTTPS)을 통해 통신하는 URL만 허용합니다.

### 비정상 호스트 감지 {#unhealthy-host-detection}

연결된 콘텐츠는 대상 호스트에서 상당한 수준의 높은 지연 또는 과부하가 발생하여 시간 초과, 과다 요청 또는 Braze가 대상 엔드포인트와 성공적으로 통신하지 못하는 기타 결과가 발생하는 경우를 감지하는 비정상 호스트 감지 메커니즘을 사용합니다. 이는 대상 호스트에 부담을 줄 수 있는 불필요한 부하를 줄이기 위한 안전장치 역할을 합니다. 또한 Braze 인프라를 안정화하고 빠른 메시징 속도를 유지하는 데 도움이 됩니다.

대상 호스트에서 상당한 수준의 높은 지연 또는 과부하가 발생하면, Braze는 대상 호스트에 대한 요청을 1분간 일시 중단하고 대신 실패를 나타내는 응답을 시뮬레이션합니다. 1분 후 Braze는 소수의 요청으로 호스트 상태를 프로빙하며, 호스트가 정상으로 확인되면 전체 속도로 요청을 재개합니다. 호스트가 여전히 비정상이면, Braze는 1분 더 대기한 후 다시 시도합니다.

비정상 호스트 감지기에 의해 대상 호스트에 대한 요청이 중단되면, Braze는 오류 응답 코드를 수신한 것처럼 메시지를 계속 렌더링하고 Liquid 로직을 따릅니다. 비정상 호스트 감지기에 의해 중단된 연결된 콘텐츠 요청을 재시도하려면 `:retry` 옵션을 사용하세요. `:retry` 옵션에 대한 자세한 내용은 [연결된 콘텐츠 재시도]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries)를 참조하세요.

비정상 호스트 감지가 문제를 일으키고 있다고 판단되면 [Braze 지원팀]({{site.baseurl}}/support_contact)에 문의하세요.

{% alert note %}
연결된 콘텐츠에 사용할 특정 URL을 허용 목록에 추가할 수 있습니다. 이 기능에 액세스하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

{% alert tip %}
일반적인 오류 코드에 대한 자세한 내용은 [웹훅 및 연결된 콘텐츠 요청 문제 해결]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection)을 참조하세요.
{% endalert %}

### 사용량 제한(429)과 비정상 호스트 감지 비교 {#rate-limits-429-versus-unhealthy-host-detection}

다음은 서로 다른 메커니즘입니다.

- **429 Too Many Requests:** 엔드포인트(또는 업스트림 서비스)가 이 응답을 반환합니다. 서버 또는 미들웨어가 자체적인 사용량 제한이 있어 트래픽을 거부하고 있다는 의미입니다. Braze는 연결된 콘텐츠에 별도의 사용량 제한을 적용하지 않습니다. 연결된 콘텐츠 요청 볼륨은 [메시지 전송 속도 사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)에 따라 직접 조정됩니다. 메시지는 수신자당 여러 번 렌더링될 수 있으므로(예: 이메일 HTML, 일반 텍스트, 가속 모바일 페이지), 연결된 콘텐츠 요청 수가 해당 사용량 제한을 초과할 수 있습니다. 설정한 분당 메시지 수 이하일 것이라고 가정하지 마세요. 429 오류가 발생하면, 예상되는 요청 볼륨을 처리할 수 있도록 엔드포인트 또는 미들웨어를 확장하거나, Campaign 또는 Canvas [전송 속도 사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)을 낮추어 분당 전송되는 메시지(및 연결된 콘텐츠 호출)를 줄이세요.
- **비정상 호스트 감지:** 1분 이내에 높은 비율과 볼륨의 *실패*가 발생한 후 트리거되는 Braze 측 안전장치입니다. 실패 수에는 `408`, `429`, `502`, `503`, `504`, `529` 상태 코드가 포함됩니다. 트리거되면 Braze는 해당 호스트에 대한 요청을 일시 중단하고 실패 응답을 시뮬레이션합니다. 이는 자체 사용량 제한과 독립적입니다. 감지 임곗값 및 자세한 내용은 [웹훅 및 연결된 콘텐츠 요청 문제 해결]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#unhealthy-host-detection)을 참조하세요. 비정상 호스트 감지를 방지하려면, [연결된 콘텐츠 호출 볼륨 이해](#understanding-connected-content-call-volume) 및 [대용량 엔드포인트를 위한 모범 사례](#best-practices-for-high-volume-endpoints)에 설명된 호출 볼륨을 엔드포인트가 처리할 수 있는지 확인하세요.

## 효율적인 성능을 위한 고려 사항 {#allowing-for-efficient-performance}

Braze는 매우 빠른 속도로 메시지를 전달하므로, 콘텐츠를 가져올 때 과부하가 걸리지 않도록 서버가 수천 개의 동시 연결을 처리할 수 있는지 확인하세요. 공개 API를 사용할 때는 API 제공업체가 적용할 수 있는 사용량 제한을 위반하지 않는지 확인하세요. Braze는 성능상의 이유로 서버 응답 시간이 2초 미만이어야 합니다. 서버가 응답하는 데 2초 이상 걸리면 콘텐츠가 삽입되지 않습니다.

엔드포인트 용량 계획 및 호출 볼륨 줄이기에 대한 자세한 내용은 [대용량 엔드포인트 모범 사례](#best-practices-for-high-volume-endpoints)를 참조하세요.

## 알아두어야 할 사항 {#things-to-know}

- Braze는 API 호출에 대해 요금을 부과하지 않으며, 주어진 데이터 포인트 사용량에 포함되지 않습니다.
- 연결된 콘텐츠 응답에는 1MB 제한이 있습니다.
- 연결된 콘텐츠는 메시지가 렌더링될 때 실행됩니다. 인앱 메시지의 경우, 메시지는 노출 횟수 시점에 렌더링됩니다.
- 연결된 콘텐츠 호출은 리다이렉트를 따르지 않습니다. `2xx` 응답만 성공으로 처리됩니다. 엔드포인트가 `3xx` 리다이렉트(예: `301` 또는 `302`)를 반환하는 경우, Braze는 최종 URL로의 리다이렉트를 따르지 않습니다. 증상 및 문제 해결 단계는 [엔드포인트가 리다이렉트를 반환할 때 연결된 콘텐츠가 실패하는 이유는 무엇인가요?](#why-does-connected-content-fail-when-my-endpoint-returns-a-redirect-301-or-302)를 참조하세요.

### 연결된 콘텐츠 호출이 처리되는 방식 {#how-connected-content-calls-are-processed}

단일 메시지 템플릿 내의 연결된 콘텐츠 호출은 Liquid 렌더링 중에 순차적으로(위에서 아래로) 실행됩니다. 이는 후속 호출이 이전 호출에서 설정한 변수를 참조할 수 있음을 의미합니다. 이 예시에서 첫 번째 호출은 사용자 데이터를 가져오고, 두 번째 호출은 해당 데이터를 사용하여 환경 설정을 가져옵니다:

{% raw %}
```liquid
{% connected_content https://api.example.com/user :save user_data %}
{% connected_content https://api.example.com/preferences?user_id={{user_data.id}} :save preferences %}
```
{% endraw %}

### 글로벌 발송 및 요청 볼륨 {#global-sending-and-request-volume}

연결된 콘텐츠 호출은 단일 메시지 내에서 순차적으로 실행되지만, 메시지는 Campaigns 및 Canvases 전체에서 병렬로 발송됩니다. 대량 발송은 피크 발송 시간 동안 엔드포인트에 상당한 요청 트래픽을 발생시킬 수 있습니다. 해당 트래픽을 관리하고 조절하는 방법(워크스페이스 메시징 사용량 제한, 전달 속도 사용량 제한조치, 캐싱 포함)에 대해서는 [대량 엔드포인트를 위한 모범 사례](#best-practices-for-high-volume-endpoints)를 참조하세요.

## 대량 엔드포인트 모범 사례 {#best-practices-for-high-volume-endpoints}

메시지에서 연결된 콘텐츠를 사용하면서 대량으로 발송하는 경우, 수신자 수나 발송 수보다 더 많은 요청이 발생할 수 있으므로 이를 대비해야 합니다.

- **최대 부하 예측:** 엔드포인트 또는 미들웨어 규모를 산정할 때 보수적인 배수를 적용하세요. 연결된 콘텐츠 요청은 수신자 수나 발송된 메시지 수를 초과할 수 있습니다. 예를 들어 이메일의 경우 한 명의 수신자가 여러 호출을 생성할 수 있으며(HTML, 일반 텍스트, 가속 모바일 페이지), 수신자 × 2 또는 × 3이 보수적인 추정치로 자주 사용됩니다.
- **적절한 경우 캐싱 사용:** GET 요청은 기본적으로 캐싱됩니다. POST 요청의 경우, 일정 기간 동안 응답을 재사용할 수 있다면(예: 요청마다 변경되지 않는 토큰 또는 콘텐츠) `:cache_max_age`를 추가하세요. [응답 캐싱]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) 및 다음 섹션의 [POST 캐싱 FAQ](#what-is-caching-behavior)를 참조하세요.
- **메시지 사용량 제한 설정:** [워크스페이스 메시징 사용량 제한]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) 및 Campaigns 또는 Canvases에 대한 [전달 속도 사용량 제한조치]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)는 연결된 콘텐츠 요청량을 간접적으로 제한합니다. Braze는 연결된 콘텐츠 자체에 사용량 제한을 적용하지 않습니다. 연결된 콘텐츠 요청과 메시지는 1:1 관계가 아니므로 이러한 설정은 완벽한 제어 수단은 아닙니다. 이를 활용하여 메시지(그리고 이에 따른 연결된 콘텐츠) 볼륨을 엔드포인트가 처리할 수 있는 범위 내로 유지하세요.
- **멱등성 및 재시도를 고려한 설계:** Braze는 수신자당 엔드포인트를 두 번 이상 호출할 수 있습니다. 엔드포인트가 중복 요청을 올바르지 않은 부작용 없이 처리할 수 있는지 확인하세요.

## 인증 유형 {#authentication-types}

### 기본 인증 사용 {#using-basic-authentication}

URL에 기본 인증이 필요한 경우, Braze가 API 호출에 사용할 기본 인증 자격 증명을 저장할 수 있습니다. **설정** > **연결된 콘텐츠**에서 기존 기본 인증 자격 증명을 관리하고 새 자격 증명을 추가할 수 있습니다.

![Braze 대시보드의 연결된 콘텐츠 설정입니다.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

새 자격 증명을 추가하려면 **자격 증명 추가** > **기본 인증**을 선택합니다.

![기본 인증 또는 토큰 인증 옵션이 있는 '자격 증명 추가' 드롭다운입니다.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

자격 증명의 이름을 지정하고 사용자 이름과 비밀번호를 입력합니다.

![이름, 사용자 이름, 비밀번호를 입력할 수 있는 '새 자격 증명 생성' 창입니다.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

그런 다음 토큰 이름을 참조하여 API 호출에서 이 기본 인증 자격 증명을 사용할 수 있습니다:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
자격 증명을 삭제하면 해당 자격 증명을 사용하려는 모든 연결된 콘텐츠 호출이 중단됩니다.
{% endalert %}

저장된 자격 증명은 Braze가 메시지를 렌더링하는 동안 {% raw %}`{% connected_content %}`{% endraw %} 요청에 적용됩니다. [웹훅]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#authentication-and-connected-content-credentials) 단계에서 구성된 기본 HTTP 요청에는 적용되지 않습니다. 해당 호출에 대한 시크릿을 가져와야 하는 경우, 요청 헤더 또는 웹훅 헤더나 본문 필드 내의 {% raw %}`{% connected_content %}`{% endraw %} 태그를 사용하세요.

### 토큰 인증 사용 {#using-token-authentication}

Braze 연결된 콘텐츠를 사용할 때 특정 API가 사용자 이름과 비밀번호 대신 토큰을 요구하는 경우가 있습니다. Braze는 토큰 인증 헤더 값을 보유하는 자격 증명도 저장할 수 있습니다.

토큰 값을 보유하는 자격 증명을 추가하려면 **자격 증명 추가** > **토큰 인증**을 선택합니다. 그런 다음 API 호출 헤더에 대한 키-값 페어와 허용된 도메인을 추가합니다.

![토큰 인증 세부 정보가 포함된 예시 토큰 'token_credential_abc'입니다.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

그런 다음 자격 증명 이름을 참조하여 API 호출에서 이 자격 증명을 사용할 수 있습니다:

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### 개방형 인증(OAuth) 사용 {#use-open-authentication-oauth}

일부 API 구성에서는 액세스하려는 API 엔드포인트를 인증하는 데 사용할 수 있는 액세스 토큰을 검색해야 합니다.

#### 1단계: 액세스 토큰 검색 {#step-1-retrieve-the-access-token}

다음 예시는 액세스 토큰을 검색하여 로컬 변수에 저장하는 방법을 보여줍니다. 이 변수는 후속 API 호출을 인증하는 데 사용할 수 있습니다. `:cache_max_age` 매개변수를 추가하여 액세스 토큰의 유효 기간과 일치시키고 아웃바운드 연결된 콘텐츠 호출 수를 줄일 수 있습니다. 자세한 내용은 [구성 가능한 캐싱]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)을 참조하세요.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

{% alert note %}
토큰 엔드포인트가 `application/x-www-form-urlencoded`를 예상하고 `:body`에서 자격 증명을 전달하는 경우, 매개변수 값의 특수 문자를 URL 인코딩하세요. 예를 들어, 슬래시(`/`)는 `%2F`가 되고 더하기 기호(`+`)는 `%2B`가 됩니다. 인코딩되지 않은 특수 문자는 OAuth 토큰 요청 실패를 유발할 수 있습니다.
{% endalert %}

#### 2단계: 검색된 액세스 토큰을 사용하여 API 인증 {#step-2-authorize-the-api-using-the-retrieved-access-token}

토큰이 저장된 후, 후속 연결된 콘텐츠 호출에 동적으로 템플릿화하여 요청을 인증할 수 있습니다:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### 자격 증명 편집 {#editing-credentials}

인증 유형에 대한 자격 증명 이름을 편집할 수 있습니다.

- 기본 인증의 경우, 사용자 이름과 비밀번호를 업데이트할 수 있습니다. 이전에 입력한 비밀번호는 표시되지 않습니다.
- 토큰 인증의 경우, 헤더 키-값 페어와 허용된 도메인을 업데이트할 수 있습니다. 이전에 설정한 헤더 값은 표시되지 않습니다.

## 연결된 콘텐츠 IP 허용 목록 {#connected-content-ip-allowlisting}

연결된 콘텐츠를 사용하는 메시지가 Braze에서 전송되면, Braze 서버는 고객 또는 서드파티 서버에 자동으로 네트워크 요청을 보내 데이터를 가져옵니다. IP 허용 목록을 사용하면 연결된 콘텐츠 요청이 실제로 Braze에서 전송되는지 확인할 수 있어 보안 계층이 추가됩니다.

Braze는 다음 IP 범위에서 연결된 콘텐츠 요청을 전송합니다. 나열된 범위는 허용 목록에 옵트인된 모든 API 키에 자동으로, 동적으로 추가됩니다.

Braze는 모든 서비스에 사용되는 예약된 IP 세트를 보유하고 있으며, 특정 시점에 모든 IP가 활성화되어 있는 것은 아닙니다. 이는 필요한 경우 고객에게 영향을 주지 않으면서 Braze가 다른 데이터 센터에서 전송하거나 유지보수를 수행할 수 있도록 설계되었습니다. Braze는 연결된 콘텐츠 요청을 할 때 나열된 IP 중 하나, 일부 또는 전부를 사용할 수 있습니다.

연결된 콘텐츠 요청이 지속적으로 `403 Forbidden`을 반환하고 인증이 올바르게 구성되어 있다면, 요청을 수신하는 서버에서 이 IP를 허용 목록에 추가하세요. `403`은 권한 부족 또는 유효하지 않은 자격 증명을 나타낼 수도 있으므로 네트워크 및 인증 설정을 모두 확인하세요. 웹훅 관련 안내는 [403 Forbidden 및 IP 허용 목록]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#403-forbidden-and-ip-allowlisting)을 참조하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### Amazon S3에서 IP 허용 목록 사용 {#using-ip-allowlisting-with-amazon-s3}

연결된 콘텐츠를 사용하여 Amazon S3에서 파일을 가져올 때, Braze IP 주소에서의 인증되지 않은 HTTP `GET` 요청을 허용하도록 버킷을 구성하세요.

1. **IP 조건이 포함된 버킷 정책 추가:** `Principal: "*"`와 인스턴스의 [Braze IP 범위](#connected-content-ip-allowlisting)를 사용하는 `IpAddress` 조건을 사용하여 버킷 객체에 `s3:GetObject`를 부여하세요. 개별 객체에 퍼블릭 읽기 ACL을 설정할 필요는 없습니다.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": ["{YOUR_BRAZE_IP_RANGE}"]
        }
      }
    }
  ]
}
```

`{YOUR_BRAZE_IP_RANGE}`를 [연결된 콘텐츠 IP 허용 목록](#connected-content-ip-allowlisting)에 나열된 인스턴스의 Braze IP 범위로 교체하세요. `aws:SourceIp` 배열에 하나 이상의 범위를 별도의 값으로 추가할 수 있습니다.

{: start="2"}
2. **S3 퍼블릭 액세스 차단 설정 검토:** `Principal: "*"`를 사용하는 버킷 정책은 IP 조건이 있더라도 AWS에 의해 퍼블릭 액세스로 처리됩니다. ACL 기반 퍼블릭 액세스는 차단된 상태로 유지하면서 버킷 정책 기반 퍼블릭 액세스를 허용해야 할 수 있습니다.

3. **연결된 콘텐츠 태그에서 S3 객체 URL 사용:** 표준 S3 URL로 객체를 참조하세요(예: `https://your-bucket.s3.amazonaws.com/path/to/object.json`).

버킷 정책 및 조건 키에 대한 자세한 내용은 [AWS 문서](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html)를 참조하세요.

## 발신 요청 헤더 {#outgoing-request-headers}

{% multi_lang_include connected_content/outgoing_request_headers.md %}

웹훅 요청은 해당 헤더를 설정하지 않은 경우 `Braze Sender`로 시작하는 `User-Agent`도 전송합니다.

## 문제 해결 {#troubleshooting}

연결된 콘텐츠 호출이 올바르게 렌더링되지 않거나 전혀 렌더링되지 않는 경우, 다음 사항을 확인하세요.

- **실시간 요청 및 응답 검사:** **미리보기 및 테스트**에서 [연결된 콘텐츠 디버거]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger)를 사용합니다.
- **연결된 콘텐츠 호출이 이루어졌는지 확인:** [메시징 히스토리 탭]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#messaging-history-tab)에서 호출이 이루어졌는지 확인할 수 있습니다. 단일 연결된 콘텐츠 요청을 테스트 발송할 수도 있습니다.
- **Postman 또는 CURL 요청을 통해 이상적인 요청이 성공하는지 확인:** 요청이 작동하고 응답을 반환하면, 헤더를 포함하여 요청을 자세히 비교합니다. 헤더가 큰따옴표가 있는 키-값 페어로 캡처되었는지 확인합니다.
- **인증이 올바르게 처리되는지 검증:** `:basic_auth`/`:auth_credentials` 옵션이 사용되고 있으며, 연결된 콘텐츠 워크스페이스 설정에 연결된 콘텐츠 인증이 추가되었는지 확인합니다. 때때로 연결된 콘텐츠 URL은 인증 이외의 헤더를 필요로 하며, 이를 입력해야 합니다.
- **데이터가 예상된 형식인지 확인:** 응답 본문의 경우, Braze는 유효한 JSON을 Liquid 객체로 파싱합니다. 그렇지 않으면 응답은 HTML을 포함한 일반 텍스트로 처리됩니다. `:content_type` 옵션은 요청의 아웃바운드 `Content-Type` 및 `Accept` 헤더를 설정하며, 응답 파싱에는 영향을 미치지 않습니다. 요청 `:body`의 경우, JSON에 공백이 포함되어 있으면 [JSON 본문 제공]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/local_connected_content_variables#providing-json-body) 섹션의 안내를 따르세요.
- **데이터가 올바르게 파싱되었는지 확인:** Liquid가 예상된 필드를 올바르게 참조하고 있는지 확인합니다. 중첩된 JSON의 경우, {% raw %}`{{sampleresult.data[0].sample_field}}`{% endraw %}를 사용하여 의도한 중첩 필드를 가리킵니다. {% raw %}`RESPONSE:{{sampleresult.data}}`{% endraw %}로 예상 결과를 출력하여 중첩된 JSON 속성을 확인할 수 있습니다.
- **응답 상태 코드 확인:** 응답 상태 코드는 `2XX` 코드여야 합니다. 연결된 콘텐츠는 코드가 `2XX`가 아닌 경우 응답을 소비할 수 없습니다.

**미리보기 및 테스트**에서 미리보기를 생성한 다음, **상세 보기**를 선택하여 [연결된 콘텐츠 디버거]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger)를 엽니다. 디버거는 연결된 콘텐츠 태그의 헤더를 나열합니다. Braze가 발신 요청에 추가하는 헤더에 대해서는 [발신 요청 헤더](#outgoing-request-headers)를 참조하세요.

Liquid 태그에 엔드포인트가 기대하는 매개변수(예: `:method`, `:headers`, `:content_type`, `:body`, 필요한 경우 `:basic_auth`)가 포함되어 있는지도 확인할 수 있습니다. 저장된 JSON 객체의 HTTP 상태 코드 키에 의존하는 경우, 엔드포인트는 JSON 객체와 `2XX` 상태를 반환해야 합니다.

호스트에서 높은 오류율이 발생하는 경우, [비정상 호스트 감지]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content) 및 [연결된 콘텐츠 호출 볼륨 이해](#understanding-connected-content-call-volume)를 검토하세요.

### 이메일 POST 요청에서의 앰퍼샌드 인코딩 {#ampersand-encoding-in-email-post-requests}

이메일 메시지에서 HTML 파싱은 {% raw %}`{% capture %}`{% endraw %} 블록 내의 앰퍼샌드(`&`)를 자동으로 `&amp;`로 변환합니다. `application/x-www-form-urlencoded` POST 요청의 경우, 이로 인해 요청이 `amp;` 접두사가 붙은 매개변수 이름(예: `amp;username`)을 전송하여 API 호출이 실패할 수 있습니다.

이 문제를 해결하려면, `:body`에 본문을 전달하기 전에 `replace` 필터를 사용하여 `amp;` 접두사를 제거합니다:

{% raw %}
```liquid
{% capture body_with_amps %}
grant_type=client_credentials&username=test&password=test
{% endcapture %}
{% connected_content https://api.example.com/token
   :method post
   :body {{body_with_amps | replace: "amp;", ""}}
   :content_type application/x-www-form-urlencoded
   :save token
%}
```
{% endraw %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 엔드포인트가 리다이렉트(301 또는 302)를 반환할 때 연결된 콘텐츠가 실패하는 이유는 무엇인가요? {#why-does-connected-content-fail-when-my-endpoint-returns-a-redirect-301-or-302}

리다이렉트로 인해 연결된 콘텐츠가 미리보기 또는 발송에서 빈 상태로 렌더링되거나, 메시지 활동 로그에 HTTP 상태 코드 `301` 또는 `302` 오류가 기록될 수 있습니다. Postman 및 기타 클라이언트는 보통 리다이렉트를 자동으로 따르기 때문에, URL이 Postman에서는 작동하지만 Braze에서는 실패할 수 있습니다.

Braze가 호출하는 URL에서 응답 본문과 함께 `2xx` 응답(일반적으로 `200`)을 반환하도록 엔드포인트를 구성하세요. 해당 URL 자체가 리다이렉트를 반환하는 경우 최종 대상 URL로 교체하세요.

콘텐츠가 빈 상태로 렌더링될 때 관련 확인 사항은 [연결된 콘텐츠가 응답 본문을 반환하지 않음]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#connected-content-returns-no-response-body)을 참조하세요.

### 사용자 또는 발송 수보다 연결된 콘텐츠 호출이 더 많은 이유는 무엇인가요? {#why-are-there-more-connected-content-calls-than-users-or-sends}

Braze는 메시지 페이로드를 렌더링하기 위해 수신자당 동일한 연결된 콘텐츠 API 호출을 두 번 이상 수행할 수 있습니다. 메시지 페이로드는 유효성 검사, 재시도 로직 또는 기타 내부 목적으로 수신자당 여러 번 렌더링될 수 있습니다. 다만, 연결된 콘텐츠 호출 중 하나만이 메시지를 채웁니다.

재시도 로직이 호출에 사용되지 않는 경우에도 연결된 콘텐츠 API 호출이 수신자당 두 번 이상 수행될 수 있는 것은 예상된 동작입니다. 연결된 콘텐츠를 포함하는 메시지의 사용량 제한을 설정하거나, 메시지 발송당 여러 번의 연결된 콘텐츠 호출을 고려한 예상 볼륨을 더 잘 처리할 수 있도록 서버를 구성하는 것을 권장합니다.

자세한 내용 및 완화 방법은 [연결된 콘텐츠 호출 볼륨 이해](#understanding-connected-content-call-volume) 및 [대용량 엔드포인트를 위한 모범 사례](#best-practices-for-high-volume-endpoints)를 참조하세요.

### 연결된 콘텐츠에서 사용량 제한은 어떻게 작동하나요? {#how-does-rate-limiting-work-with-connected-content}

연결된 콘텐츠에는 자체 사용량 제한이 없습니다. 대신 사용량 제한은 메시지 발송 속도를 기준으로 합니다. 발송되는 메시지보다 연결된 콘텐츠 호출이 더 많은 경우, 의도한 연결된 콘텐츠 사용량 제한보다 메시징 사용량 제한을 더 높게 설정하는 것을 권장합니다.

### 캐싱 동작은 어떻게 되나요? {#what-is-caching-behavior}

GET 요청은 기본적으로 캐싱됩니다([응답 캐싱]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses) 참조). **POST 요청은 기본적으로 캐싱되지 않지만**, 연결된 콘텐츠 호출에 `:cache_max_age`를 추가하여 캐싱을 활성화할 수 있습니다. 이를 통해 동일한 POST(예: 토큰 또는 콘텐츠 요청)가 캐시 기간 내에 반복적으로 수행되는 경우 엔드포인트 부하를 줄일 수 있습니다.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

캐싱은 중복 연결된 콘텐츠 호출을 줄이는 데 도움이 될 수 있지만, 사용자당 단일 호출을 보장하지는 않습니다. 캐시 지속 시간은 5분에서 4시간 사이입니다. 자세한 내용은 [응답 캐싱]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)을 참조하세요.

### 연결된 콘텐츠의 HTTP 기본 동작은 무엇인가요? {#what-is-the-connected-content-http-default-behavior}

{% multi_lang_include connected_content/sections.md section='default behavior' %}

{% multi_lang_include connected_content/sections.md section='http post' %}

### 동일한 연결된 콘텐츠 호출을 여러 곳에서 사용하면 어떻게 되나요? {#what-happens-if-i-use-the-same-connected-content-call-in-multiple-places}

각 연결된 콘텐츠 태그는 여러 태그가 동일한 URL과 파라미터를 사용하더라도 개별적으로 평가됩니다. URL과 캐시 설정이 허용하는 경우, 동일한 요청은 새 아웃바운드 요청을 트리거하는 대신 캐시에서 제공될 수 있습니다(자세한 내용은 [응답 캐싱]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses)을 참조하세요).