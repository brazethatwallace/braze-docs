---
nav_title: 랜딩 페이지 개인화
article_title: 랜딩 페이지 개인화
description: "이 문서에서는 드래그 앤 드롭 에디터를 사용하여 Braze 랜딩 페이지를 개인화하는 방법을 다룹니다."
page_order: 4
---

# 랜딩 페이지 개인화 {#personalize-landing-pages}

> 랜딩 페이지에서 Liquid 개인화를 사용하여 고객 프로필 데이터로 콘텐츠를 동적으로 맞춤 설정할 수 있습니다. 예를 들어, 여러 정적 랜딩 페이지를 관리하지 않고도 다양한 사용자 속성에 따라 헤드라인을 개인화할 수 있습니다.

{% alert important %}
랜딩 페이지의 Liquid 개인화는 랜딩 페이지 Pro 티어에서만 사용할 수 있습니다. 현재 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), [다국어]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings), [프로모션 코드]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)는 랜딩 페이지의 Liquid 개인화에서 지원되지 않습니다.
{% endalert %}

## Liquid 삽입하기 {#inserting-liquid}

드래그 앤 드롭 편집기에서는 편집기 내부와 오른쪽 패널의 페이지 또는 블록 설정 모두에서 Liquid 개인화를 삽입할 수 있습니다. Liquid 구현에 대한 자세한 내용은 전용 [Liquid 설명서]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 참조하세요.

![Liquid 개인화가 추가된 랜딩 페이지 편집기.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## 미리보기 및 테스트 {#previewing-and-testing}

편집기에서 랜딩 페이지를 미리 볼 때 무작위 사용자, 기존 사용자 또는 커스텀 사용자로 페이지를 확인할 수 있습니다.

그러나 데이터 테이블이나 **랜딩 페이지 세부 정보** 페이지에서 랜딩 페이지를 미리 보는 경우에는 무작위 사용자로만 확인할 수 있습니다.

## 개인화 고려 사항 {#personalization-considerations}

개인화된 랜딩 페이지의 최적 성능을 유지하려면 다음 크기 제한에 유의하세요:

- **랜딩 페이지 저장:** 크기가 500&nbsp;KB를 초과하면 페이지가 크기 제한을 초과했다는 경고 메시지가 표시될 수 있으며, 이로 인해 게시가 불가능할 수 있습니다.
- **Liquid 개인화를 사용한 렌더링:** 총 크기가 1&nbsp;MB를 초과하면 안 됩니다. 그렇지 않으면 Braze에 의해 페이지가 자동으로 게시 취소될 수 있습니다.

### 랜딩 페이지 게시 취소 방지 {#avoid-unpublishing-landing-pages}

페이지가 이러한 크기 제한을 초과하면 제한을 계속 초과할 경우 게시 취소될 수 있다는 이메일을 받게 됩니다. 임계값에 도달하면 페이지가 자동으로 게시 취소되며 알림을 받게 됩니다.

페이지가 크기 제한을 초과하거나 느린 로드 시간을 경험하지 않도록 하려면 다음과 같은 Liquid 개인화를 사용하세요:

- 대규모 데이터 세트를 지속적으로 반복하거나 참조하지 않습니다.
- Liquid 블록 내에서 광범위한 수학적 또는 조건 로직에 의존하지 않습니다.

또한 대용량 스크립트, 스타일시트 및 base64로 인코딩된 에셋을 랜딩 페이지 코드에 직접 삽입하지 마세요. 이러한 인라인 에셋은 페이지 크기 제한에 포함되며 렌더링 속도를 저하시킬 수 있습니다. 대신 글꼴, 이미지, 스타일시트 및 스크립트를 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)에 업로드하세요. 미디어 라이브러리에서 제공되는 에셋은 Braze의 CDN에 호스팅되므로 Liquid 렌더링을 위해 처리되지 않으며 페이지 크기 제한에 포함되지 않습니다.

### 식별된 사용자와 익명 사용자를 위한 Liquid 사용 {#use-liquid-for-identified-and-anonymous-users}

Liquid는 식별된 사용자와 익명 방문자 모두를 위해 랜딩 페이지 경험을 커스터마이즈할 수 있습니다.

- **식별된 사용자:** Braze 메시지에서 랜딩 페이지로 링크하고 [랜딩 페이지 Liquid 태그]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users#using-landing-page-liquid-tags)를 포함하세요. 이렇게 하면 사용자가 Braze 프로필과 연결되어 페이지 경험이 개인화됩니다.
- **익명 방문자:** 임의의 숫자나 시간대별 인사말과 같은 상황별, 비프로필 기반 콘텐츠에 Liquid를 사용하세요.

### 양식 필드 미리 채우기 {#pre-fill-form-fields}

랜딩 페이지 양식 필드가 고객 프로필 속성에 매핑되어 있으면 재방문 사용자를 위해 해당 필드를 미리 채울 수 있습니다. 이를 통해 양식 작성의 부담을 줄이고 알려진 방문자의 완료율을 높일 수 있습니다.

양식 필드 미리 채우기 사용 방법:

1. 드래그 앤 드롭 편집기에서 양식 필드를 선택합니다.
2. 오른쪽 설정 패널에서 필드를 적절한 프로필 속성에 매핑합니다.
3. **고객 프로필에서 미리 채우기**를 선택합니다.

![고객 프로필 데이터에서 미리 채우기 옵션을 보여주는 랜딩 페이지 양식 필드 설정.]({% image_buster /assets/img/landing_pages/pre-fill-checkbox.png %}){: style="max-width:70%;"}

미리 채우기는 [식별된 사용자](#use-liquid-for-identified-and-anonymous-users)에게만 작동합니다. 익명 방문자의 경우 양식 필드는 기본값 상태를 유지합니다:

- **입력 필드:** 입력 안내 텍스트를 표시합니다.
- **체크박스, 라디오 버튼 및 유사한 컨트롤:** 사용자가 상호작용할 때까지 선택되지 않은 상태로 유지됩니다.

{% alert warning %}
사용자가 랜딩 페이지 링크(이메일, SMS 또는 기타 메시지에서)를 다른 사람에게 전달하면 수신자는 원래 사용자를 위해 미리 채워진 데이터를 보게 됩니다. 이는 탈퇴 링크 및 환경설정 센터 링크에 적용되는 것과 동일한 보안 고려 사항입니다. 이 기능을 사용할 때 미리 채우는 데이터의 민감도와 오디언스의 공유 행동을 고려하세요.
{% endalert %}

## 커스텀 코드로 외부 데이터 가져오기 {#fetching-external-data-with-custom-code}

**커스텀 코드** 블록을 사용하여 외부 엔드포인트에서 데이터를 가져와 랜딩 페이지에 표시할 수 있습니다. 이 방식은 클라이언트 측(사용자의 브라우저)에서 요청을 수행하므로, 서버 측 렌더링 지연 없이 페이지가 빠르게 로드됩니다.

{% alert warning %}
외부 데이터를 가져올 때 구현의 보안은 사용자의 책임입니다. API 호출에 사용되는 외부 식별자는 UUID이거나 동등하게 안전한 명명 체계를 사용해야 합니다. [사용자 ID 명명 모범 사례]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices)를 참조하세요.
{% endalert %}

### 사용 사례 {#use-case}

이 패턴은 Braze에 저장되지 않은 사용자별 데이터를 표시해야 할 때 유용합니다. 실시간 재고, 개인화된 추천, 또는 조직이 별도 시스템에서 관리하는 기타 데이터 등이 그 예입니다.

### 구현 예시 {#example-implementation}

이 예시는 외부 API에서 사용자 데이터를 가져오는 방법을 보여줍니다. API 엔드포인트를 자체 보안 엔드포인트로 교체하고 안전한 식별자를 사용하세요.

{% raw %}
```html
<script>
window.onload = () => {
  // Use Liquid to template the user's external ID
  const userId = "{{${user_id}}}";

  const loadUserData = async () => {
    try {
      // Replace with your own secure API endpoint
      const response = await fetch(`https://your-api.example.com/user/${userId}`);

      if (!response.ok) {
        throw new Error('Failed to load data');
      }

      const data = await response.json();

      // Update the page with the fetched data
      document.querySelector("#user-data").textContent = JSON.stringify(data, null, 2);
      document.querySelector("#user-name").textContent = data.name || "User";
    } catch (error) {
      // Handle errors gracefully
      document.querySelector("#user-data").textContent = "Unable to load data at this time.";
    }
  };

  loadUserData();
};
</script>

<!-- Display area for fetched data -->
<p>Welcome, <span id="user-name">Loading...</span></p>
<pre id="user-data">Loading your information...</pre>
```
{% endraw %}

### 고려 사항 {#considerations}

랜딩 페이지에서 외부 데이터를 가져올 때 다음 사항을 고려하세요.

- **로딩 상태:** 엔드포인트가 응답할 때까지 사용자에게 입력 안내 텍스트가 표시됩니다. 로딩 인디케이터나 스켈레톤 화면을 추가하는 것을 고려하세요.
- **오류 처리:** 엔드포인트가 실패하거나 응답이 느린 경우 페이지가 깨져 보일 수 있습니다. 적절한 오류 메시지와 대체 콘텐츠를 구현하세요.
- **성능:** 페이지는 즉시 로드되지만, 데이터는 외부 요청이 완료된 후에 표시됩니다. 최상의 사용자 경험을 위해 API 응답 속도를 빠르게 유지하세요.
- **보안:** API 엔드포인트가 식별자를 검증하고 사용자가 볼 수 있도록 승인된 데이터만 반환하는지 확인하세요. 남용을 방지하기 위해 사용량 제한조치를 구현하세요. 안전한 식별자 선택에 대한 지침은 [사용자 ID 명명 모범 사례]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#naming-best-practices)를 참조하세요.

{% alert warning %}
Liquid으로 개인화된 랜딩 페이지의 경우, Braze는 랜딩 페이지 HTML 어디에서든 {% raw %}`{{`{% endraw %} 및 {% raw %}`{%`{% endraw %} 구분자를 처리합니다. 여기에는 JavaScript 문자열, 주석, 정규표현식 내부도 포함됩니다. 이는 전체 페이지에 적용되지만, **커스텀 코드** 블록이 이러한 시퀀스를 실수로 포함할 가능성이 가장 높은 곳입니다.

이러한 시퀀스가 닫는 태그 없이 나타나는 경우(예: {% raw %}`/* version {{ 2.0 */`{% endraw %}), Braze는 이를 열린 Liquid 태그로 처리합니다. 페이지의 다른 유효한 Liquid 태그가 렌더링되지 않거나, 같은 블록의 다른 곳에서 Liquid 렌더링이 중단될 수 있습니다. 심한 경우, 깨진 Liquid으로 인해 페이지가 게시되지 않거나 게시 취소될 수 있습니다([대체 페이지](#fallback-pages) 참조).

이를 방지하려면 Liquid이 아닌 컨텍스트에서 {% raw %}`{{`{% endraw %} 및 {% raw %}`{%`{% endraw %}를 이스케이프하거나 제거하고, JavaScript에서 시퀀스를 분리하세요(예: {% raw %}`'{' + '{'`{% endraw %}). Liquid은 스크립트가 실행되기 전에 서버 측에서 실행됩니다. 또한 Liquid이 아닌 큰 섹션을 {% raw %}`&#123;% raw %&#125;...&#123;% endraw %&#125;`{% endraw %} 태그로 감쌀 수도 있습니다.
{% endalert %}

## 대체 페이지 {#fallback-pages}

사용자가 게시 취소된 페이지에 접근하려고 하면, 해당 페이지를 현재 로드할 수 없다는 메시지가 표시됩니다. 페이지가 게시 취소되는 이유는 다음과 같습니다:

- 복잡하거나 손상된 Liquid로 인해 렌더링 시간이 길어지는 경우
- 사용자 네트워크 문제
- 최대 랜딩 페이지 크기 제한 초과