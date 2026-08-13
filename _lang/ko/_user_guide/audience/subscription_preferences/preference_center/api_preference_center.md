---
nav_title: API 이메일 환경설정 센터
article_title: API 이메일 환경설정 센터
page_order: 1
description: "이 문서에서는 API 이메일 환경설정 센터와 이를 커스터마이즈하는 방법을 설명합니다."
channel:
  - email
---

# API 이메일 환경설정 센터 {#api-email-preference-center}

> 환경설정 센터를 설정하면 사용자가 [이메일 메시징]({{site.baseurl}}/user_guide/channels/email)에 대한 알림 환경설정을 한 곳에서 편집하고 관리할 수 있습니다. 이 문서에서는 API로 생성하는 환경설정 센터를 구축하는 단계를 설명하지만, [드래그 앤 드롭 에디터]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center)를 사용하여 환경설정 센터를 구축할 수도 있습니다.

Braze 대시보드에서 **오디언스** > **이메일 환경설정 센터**로 이동합니다.

여기에서 각 구독 그룹을 관리하고 확인할 수 있습니다. 생성한 각 구독 그룹은 이 환경설정 센터 목록에 추가됩니다. 여러 개의 환경설정 센터를 생성할 수 있습니다.

{% alert important %}
환경설정 센터는 Braze 이메일 채널 내에서 사용하도록 설계되었습니다. 환경설정 센터 링크는 각 사용자에 따라 동적으로 생성되며 외부에서 호스팅할 수 없습니다.
{% endalert %}

## API로 환경설정 센터 생성하기 {#create-a-preference-center-with-api}

[환경설정 센터 Braze 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center)를 사용하면 Braze에서 호스팅하는 웹사이트인 환경설정 센터를 생성하여 사용자의 구독 상태와 구독 그룹 상태를 표시할 수 있습니다. HTML과 CSS를 사용하여 개발자 팀이 환경설정 센터를 구축하면 페이지 스타일이 브랜드 가이드라인에 맞게 됩니다.

Liquid를 사용하면 구독 그룹의 이름과 각 사용자의 상태를 가져올 수 있습니다. 이렇게 하면 페이지가 로드될 때 Braze가 이 데이터를 저장하고 검색합니다.

### 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| 활성화된 환경설정 센터 | Braze 대시보드에 환경설정 센터 기능을 사용할 수 있는 권한이 있어야 합니다. |
| 이메일, SMS 또는 WhatsApp 구독 그룹이 있는 유효한 워크스페이스 | 유효한 사용자와 이메일, SMS 또는 WhatsApp 구독 그룹이 있는 작동 중인 워크스페이스가 필요합니다. |
| 유효한 사용자 | 이메일 주소와 외부 ID가 있는 사용자가 필요합니다. |
| 환경설정 센터 권한이 있는 생성된 API 키 | Braze 대시보드에서 **설정** > **API 키**로 이동하여 환경설정 센터 권한이 있는 API 키에 접근할 수 있는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

### 1단계: 환경설정 센터 생성 엔드포인트 사용하기 {#step-1-use-the-create-preference-center-endpoint}

[환경설정 센터 생성 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)를 사용하여 환경설정 센터를 구축해 보겠습니다. 환경설정 센터를 커스터마이즈하려면 `preference_center_page_html` 필드와 `confirmation_page_html` 필드에 브랜딩에 맞는 HTML을 포함할 수 있습니다.

[환경설정 센터 URL 생성 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)를 사용하면 Braze를 통해 발송된 이메일 외부에서 특정 사용자의 환경설정 센터 URL을 가져올 수 있습니다.

{% alert note %}
Braze는 `data:` URL을 사용하는 iframe에서 `confirmation_page_html`을 렌더링합니다. 브라우저는 `data:` URL을 불투명한 출처로 처리합니다. 따라서 해당 iframe 내의 스크립트는 추가 외부 리소스를 로드할 수 없으며, 해당 페이지에서 상위 창을 탐색하거나 프레임 간 통신을 수행할 수 없습니다.<br><br>대신 스크립트를 삽입하는 대신 호스팅된 설문조사 URL과 같은 외부 콘텐츠에 링크할 수 있습니다. 서드파티 도구를 삽입해야 하고 해당 벤더가 허용하는 경우, `<iframe title="삽입된 콘텐츠에 대한 설명" src="https://example.com/...">`을 사용하여 도구의 호스팅된 HTTPS URL을 가리키세요.
{% endalert %}

### 2단계: 이메일 Campaign에 포함하기 {#step-2-include-in-your-email-campaign}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

이메일에 환경설정 센터 링크를 배치하려면 탈퇴 URL을 삽입하는 방식과 유사하게 이메일의 원하는 위치에 다음 Liquid 태그를 사용합니다.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Liquid를 포함하는 HTML 조합을 사용할 수도 있습니다. 예를 들어, HTML 에디터 또는 드래그 앤 드롭 에디터에서 다음을 URL로 붙여넣을 수 있습니다. 이렇게 하면 모든 이메일 구독 그룹을 자동으로 나열하는 기본 환경설정 센터 레이아웃이 표시됩니다. [링크 별칭 지정]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing)을 사용하는 경우, Braze가 추적 파라미터를 추가할 수 있도록 Liquid 태그 뒤에 물음표(`?`)를 추가하세요.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

환경설정 센터에는 사용자가 모든 이메일을 탈퇴할 수 있는 체크박스가 있습니다.

{% multi_lang_include preference_center/testing.md section="api" %}

#### 환경설정 센터 편집하기 {#edit-a-preference-center}

[환경설정 센터 업데이트 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center)를 사용하여 환경설정 센터를 편집하고 업데이트할 수 있습니다.

#### 환경설정 센터 및 세부 정보 확인하기 {#identify-preference-centers-and-details}

환경설정 센터를 확인하려면 [환경설정 센터 세부 정보 보기 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center)를 사용하여 마지막 업데이트 타임스탬프, 환경설정 센터 ID 등 관련 정보를 반환합니다.

## 환경설정 센터 커스터마이즈하기 {#customize-a-preference-center}

Braze는 환경설정 센터에서 구독 상태 업데이트를 관리하여 환경설정 센터를 동기화 상태로 유지합니다. 그러나 다음 옵션과 함께 [구독 그룹 API]({{site.baseurl}}/api/endpoints/subscription_groups)를 사용하여 자체 환경설정 센터를 생성하고 호스팅할 수도 있습니다.

### 옵션 1: 문자열 쿼리 파라미터를 사용한 링크 {#option-1-link-with-string-query-parameters}

URL 본문에 쿼리 문자열 필드-값 쌍을 사용하여 사용자 ID와 이메일 카테고리를 페이지에 전달하면 사용자가 탈퇴 선택을 확인하기만 하면 됩니다. 이 옵션은 사용자 식별자를 해시 형식으로 저장하고 아직 구독 센터가 없는 경우에 적합합니다.

이 옵션의 경우 각 이메일 카테고리에 고유한 탈퇴 링크가 필요합니다:<br>
`http://mycompany.com/query-string-form-fill?field_id=Alex&field_category=offers`

{% alert tip %}
Liquid 필터를 사용하여 발송 시점에 사용자의 외부 ID를 해시할 수도 있습니다. 이렇게 하면 `user_id`가 MD5 해시 값으로 변환됩니다. 예를 들어:
{% raw %}
```liquid
{% assign my_string = ${user_id} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### 옵션 2: JSON 웹 토큰으로 인증하기 {#option-2-authenticate-with-json-web-token}

[JSON 웹 토큰](https://auth0.com/learn/json-web-tokens/)을 사용하여 일반적으로 사용자 이름과 비밀번호 로그인과 같은 인증 계층 뒤에 있는 웹 서버의 일부(예: 계정 환경설정)에 사용자를 인증합니다.

이 접근 방식은 URL에 쿼리 문자열 값 쌍을 삽입할 필요가 없으며, 이러한 값은 JSON 웹 토큰의 페이로드에 전달할 수 있습니다. 예를 들어:

```json
{
    "user_id": "1234567890",
    "name": "Alex Smith",
    "category": "offers"
}
```

## 자주 묻는 질문 {#frequently-asked-questions}

### 테스트 발송에서 환경설정 센터가 작동하지 않는 이유는 무엇인가요? {#why-doesnt-my-preference-center-work-in-a-test-send}

환경설정 센터 링크는 실제 발송 컨텍스트가 필요합니다. 테스트 발송에서는 유효한 환경설정 센터 URL이 생성되지 않으며, 페이지가 로드되면 **Save Preferences** 버튼이 비활성화됩니다. 이는 예상되는 동작입니다. 포괄적인 테스트를 수행하려면 테스트 사용자 또는 소규모 내부 Segment에 Campaign 또는 캔버스 단계를 시작하거나, [환경설정 센터 URL 생성 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)를 사용하세요. 자세한 내용은 [환경설정 센터 테스트하기](#testing-preference-centers)를 참조하세요.

### 환경설정 센터를 생성하지 않았는데 대시보드에 "PreferenceCenterBrazeDefault"가 표시되는 이유는 무엇인가요? {#i-havent-created-a-preference-center-why-am-i-seeing-preferencecenterbrazedefault-on-my-dashboard}

이는 레거시 Liquid {%raw%}`${preference_center_url}`{%endraw%}이 사용될 때 환경설정 센터를 렌더링하는 데 사용됩니다. 즉, {%raw%}`${preference_center_url}` 또는 `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%}를 참조하는 캔버스 단계나 템플릿은 작동하지 않습니다. 이는 레거시 Liquid 또는 "PreferenceCenterBrazeDefault"를 메시지의 일부로 포함한 이전에 발송된 메시지에도 적용됩니다.

새 메시지에서 {%raw%}`${preference_center_url}`{%endraw%}을 다시 참조하면 "PreferenceCenterBrazeDefault"라는 이름의 환경설정 센터가 다시 생성됩니다.

### 환경설정 센터는 여러 언어를 지원하나요? {#do-preference-centers-support-multiple-languages}

아니요. 그러나 커스텀 옵트인 및 옵트아웃 페이지의 HTML을 작성할 때 Liquid를 활용할 수 있습니다. 동적 링크를 사용하여 탈퇴를 관리하는 경우 이는 단일 링크입니다.

예를 들어, 스페인어 사용자의 탈퇴율을 추적하는 경우 별도의 Campaign을 사용하거나 Currents 관련 분석(예: 사용자가 탈퇴하는 시점을 확인하고 해당 사용자의 선호 언어를 확인하는 것)을 활용해야 합니다.

또 다른 예로, 스페인어 사용자의 탈퇴율을 추적하려면 사용자의 언어가 스페인어인 경우 탈퇴 URL에 `?Spanish=true`와 같은 쿼리 파라미터 문자열을 추가하고, 그렇지 않은 경우 일반 탈퇴 링크를 사용할 수 있습니다:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

그런 다음 Currents를 통해 스페인어를 사용하는 사용자를 식별하고 해당 탈퇴 링크에 대한 클릭 이벤트가 몇 건인지 확인할 수 있습니다.

### 발송 시 탈퇴 링크와 이메일 환경설정 센터가 모두 필요한가요? {#are-both-unsubscribe-links-and-email-preference-centers-required-for-sending}

아니요. 이메일 Campaign을 작성할 때 "이메일 본문에 탈퇴 링크가 포함되어 있지 않습니다"라는 메시지가 표시되는 경우, 탈퇴 링크가 콘텐츠 블록에 있으면 이 경고는 예상되는 동작입니다.

### 기본 브라우저 아이콘을 어떻게 업데이트하나요? {#how-do-i-update-the-default-browser-icon}

기본적으로 브라우저 탭 이름 옆의 아이콘(파비콘)은 Braze 로고를 사용합니다. 커스텀 파비콘을 추가하려면 생성 또는 업데이트 [환경설정 센터 API 호출]({{site.baseurl}}/api/endpoints/preference_center)의 `links-tags` 속성을 통해 설정합니다. 그러면 Braze가 호스팅된 페이지에 {% raw %}`<link rel="icon" ...>`{% endraw %} 태그를 삽입합니다.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}