---
nav_title: 사용자 추적
article_title: 폼을 통한 사용자 추적
description: "랜딩 페이지를 통해 폼을 제출하는 사용자를 식별하기 위해 메시지에 Liquid 태그를 추가하는 방법을 알아보세요."
page_order: 2
---

# 폼을 통한 사용자 추적 {#track-users-through-a-form}

> 랜딩 페이지 Liquid 태그를 메시지에 추가하여 랜딩 페이지를 통해 폼을 제출하는 사용자를 추적하는 방법을 알아보세요. 이 Liquid 태그는 이메일, SMS, 인앱 메시지 등 모든 Braze 메시징 채널에서 지원됩니다. 추적 데이터에 대해 자세히 알아보려면 [랜딩 페이지 추적 데이터 정보]({{site.baseurl}}/user_guide/messaging/landing_pages/about_tracking_data)를 참조하세요.

## 필수 조건 {#prerequisites}

시작하기 전에 [랜딩 페이지]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages)와 [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign)을 생성해야 합니다.

## 작동 방식 {#how-it-works}

Braze에서 단일 또는 멀티채널 메시지에 {% raw %}`{% landing_page_url %}`{% endraw %} Liquid 태그를 추가할 수 있습니다. 사용자가 해당 랜딩 페이지를 방문하여 폼을 제출하면, Braze는 해당 사용자에 대해 새 프로필을 생성하는 대신 자동으로 해당 데이터를 기존 프로필에 연결합니다. 다음 예시에서는 랜딩 페이지 Liquid 태그를 사용하여 고객을 설문조사에 연결합니다:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
외부 채널에 페이지 URL을 삽입하여 리드 생성에 랜딩 페이지를 활용할 수도 있습니다. 랜딩 페이지를 생성한 후 **랜딩 페이지 세부 정보**로 이동하여 랜딩 페이지의 고유 URL을 확인하세요.
{% endalert %}

## 랜딩 페이지 Liquid 태그 사용하기 {#using-landing-page-liquid-tags}

### 1단계: 페이지 URL 확인 {#page-url}

Braze는 랜딩 페이지의 URL을 사용하여 고유한 Liquid 태그를 생성합니다. 현재 페이지 URL을 변경하려면 **메시징** > **랜딩 페이지**로 이동한 다음 랜딩 페이지를 여세요. **페이지 URL** 아래에서 새 페이지 URL을 입력할 수 있습니다.

{% alert warning %}
메시지를 발송한 후 페이지 URL을 변경하면, 이전 URL을 사용하여 랜딩 페이지를 방문하려는 사용자는 `404` 페이지로 이동하게 됩니다.
{% endalert %}

![Braze의 랜딩 페이지에 대한 예시 페이지 URL.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### 2단계: Liquid 태그 생성 {#step-2-generate-the-liquid-tag}

**메시징** > **Campaigns**로 이동한 다음 Campaign을 선택하세요. 메시지 편집기에서 **개인화**를 선택합니다.

![드래그 앤 드롭 편집기의 '개인화 추가' 버튼.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze는 [랜딩 페이지 URL](#page-url)을 사용하여 자동으로 Liquid 태그를 생성합니다. 태그를 생성하려면 다음 표를 참조하세요:

| **개인화 유형** | **Landing Page**를 선택합니다. |
| **랜딩 페이지** | [이전에 생성한](#prerequisites) 랜딩 페이지를 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="2단계: Liquid 태그 생성" }

메시지에 Liquid 태그를 추가하려면 **삽입**을 선택하거나, 스니펫을 클립보드에 복사하여 수동으로 추가할 수 있습니다.

![선택한 랜딩 페이지에 대해 자동 생성된 Liquid 태그.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

스니펫은 다음과 유사합니다:

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### 3단계: 메시지 완성 및 발송 {#step-3-finalize-and-send-your-message}

Liquid 스니펫을 메시지에 삽입한 다음 나머지 메시지를 완성하세요. 예시:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

준비가 되면 메시지를 발송하여 랜딩 페이지를 통해 사용자 추적을 시작할 수 있습니다.