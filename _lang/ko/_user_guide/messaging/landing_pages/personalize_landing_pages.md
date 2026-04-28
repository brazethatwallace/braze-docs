---
nav_title: 랜딩 페이지 개인화
article_title: 랜딩 페이지 개인화
description: "이 문서에서는 드래그 앤 드롭 에디터를 사용하여 Braze 랜딩 페이지를 개인화하는 방법을 다룹니다."
page_order: 4
---

# 랜딩 페이지 개인화 {#personalize-landing-pages}

> 랜딩 페이지에서 Liquid 개인화를 사용하여 고객 프로필 데이터로 콘텐츠를 동적으로 맞춤 설정할 수 있습니다. 예를 들어, 여러 정적 랜딩 페이지를 관리하지 않고도 다양한 사용자 속성에 따라 헤드라인을 개인화할 수 있습니다.

{% alert important %}
랜딩 페이지의 Liquid 개인화는 랜딩 페이지 Pro 티어에서만 사용할 수 있습니다. 현재 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/), [다국어]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/), [프로모션 코드]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/)는 랜딩 페이지의 Liquid 개인화에서 지원되지 않습니다.
{% endalert %}

## Liquid 삽입 {#inserting-liquid}

드래그 앤 드롭 에디터에서 에디터 내부와 오른쪽 패널의 페이지 또는 블록 설정 모두에서 Liquid 개인화를 삽입할 수 있습니다. Liquid 구현에 대한 자세한 내용은 전용 [Liquid 설명서]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/#using-liquid)를 참조하세요.

![Liquid 개인화가 추가된 랜딩 페이지 에디터.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## 미리보기 및 테스트 {#previewing-and-testing}

에디터에서 랜딩 페이지를 미리볼 때 임의 사용자, 기존 사용자 또는 커스텀 사용자로 페이지를 볼 수 있습니다.

그러나 데이터 테이블이나 **랜딩 페이지 세부 정보** 페이지에서 랜딩 페이지를 미리볼 때는 임의 사용자로만 볼 수 있습니다.

## 개인화 고려 사항 {#personalization-considerations}

개인화된 랜딩 페이지의 최적 성능을 유지하려면 다음 크기 제한에 유의하세요.

- **랜딩 페이지 저장:** 크기가 500&nbsp;KB를 초과하면 페이지가 크기 제한을 초과했으며 게시가 불가능할 수 있다는 경고 메시지가 표시될 수 있습니다.
- **Liquid 개인화를 사용한 렌더링:** 총 크기가 1&nbsp;MB를 초과하면 안 됩니다. 그렇지 않으면 Braze에 의해 페이지가 자동으로 게시 취소될 수 있습니다.

### 랜딩 페이지 게시 취소 방지 {#avoid-unpublishing-landing-pages}

페이지가 이러한 크기 제한을 초과하면 제한을 계속 초과할 경우 게시 취소될 수 있다는 이메일을 받게 됩니다. 임계값에 도달하면 페이지가 자동으로 게시 취소되며 알림을 받게 됩니다.

페이지가 크기 제한을 초과하거나 느린 로드 시간을 경험하지 않도록 하려면 다음과 같은 Liquid 개인화를 사용하세요.

- 대규모 데이터 세트를 지속적으로 반복하거나 참조하지 않습니다.
- Liquid 블록 내에서 광범위한 수학적 또는 조건 로직에 의존하지 않습니다.

또한 대용량 스크립트, 스타일시트 및 base64 인코딩된 자산을 랜딩 페이지 코드에 직접 삽입하지 마세요. 이러한 인라인 자산은 페이지 크기 제한에 포함되며 렌더링 속도를 저하시킬 수 있습니다. 대신 글꼴, 이미지, 스타일시트 및 스크립트를 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/)에 업로드하세요. 미디어 라이브러리에서 제공되는 자산은 Braze의 CDN에서 호스팅되므로 Liquid 렌더링을 위해 처리되지 않으며 페이지 크기 제한에 포함되지 않습니다.

### 식별된 사용자와 익명 사용자를 위한 Liquid 사용 {#use-liquid-for-identified-and-anonymous-users}

Liquid는 식별된 사용자와 익명 방문자 모두를 위해 랜딩 페이지 경험을 맞춤 설정할 수 있습니다.

- **식별된 사용자:** Braze 메시지에서 랜딩 페이지로 링크하고 [랜딩 페이지 Liquid 태그]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users/#using-landing-page-liquid-tags)를 포함하세요. 이렇게 하면 사용자가 Braze 프로필과 연결되어 페이지 경험이 개인화됩니다.
- **익명 방문자:** 임의 숫자나 시간대별 인사말과 같은 상황별, 비프로필 기반 콘텐츠에 Liquid를 사용하세요.

## 대체 페이지 {#fallback-pages}

사용자가 게시 취소된 페이지에 접근하려고 하면 현재 페이지를 로드할 수 없다는 메시지가 표시됩니다. 페이지가 게시 취소된 이유는 다음과 같습니다.

- 긴 렌더링 시간을 유발할 수 있는 복잡하거나 손상된 Liquid
- 사용자 네트워크 문제
- 최대 랜딩 페이지 크기 제한 초과