---
nav_title: 테스트 캔버스 보내기
article_title: 테스트 캔버스 보내기
page_order: 1
description: "이 참조 문서에서는 Canvas를 시작하기 전에 테스트하는 방법과 모범 사례를 다룹니다."
page_type: reference
tool: Canvas
---

# 테스트 캔버스 보내기 {#send-test-canvases}

> [Canvas를 생성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)한 후, 오디언스 규모나 세분화 필터 수와 같은 세부 사항에 따라 시작 전에 수행해야 할 여러 가지 확인 사항이 있습니다.

가능하면 Braze는 Canvas를 시작하기 전에 테스트하는 것을 권장합니다. 이 테스트는 일반적으로 Braze 환경에서 진행됩니다. Canvas 테스트에는 Canvas를 복제하고, 테스트 사용자를 사용자 여정에 통과시키며, 사용자 동작이 Canvas에서 설계한 내용과 일치하는지 확인하는 과정이 포함됩니다.

## 1단계: 테스트 계획 수립 {#step-1-create-your-test-plan}

Canvas 테스트를 시작하기 전에 테스트 계획을 수립하는 것이 필수적입니다. 테스트 계획은 Canvas 여정의 특정 영역을 식별하고 추적하는 데 도움이 됩니다.

테스트 계획을 수립할 때 다음 질문을 고려하세요:
- 각 Canvas 분기와 경로에 대해 최소 한 명의 사용자가 생성되었나요?
- Canvas에서 Segment를 사용하고 있나요?
	- Segment를 사용하는 경우, 사용자가 사용자 여정에 적격하기 전에 Canvas에 진입하기 위한 필수 조건이 있을 수 있습니다.
- 테스트 Canvas의 메시지 제목에 사용자 ID나 이메일 주소를 가져오는 Liquid가 포함되어 있어 테스트 목적으로 메시지와 사용자를 쉽게 식별할 수 있나요?

## 2단계: 테스트 사용자 식별 {#step-2-identify-test-users}

다음으로, 의도한 사용자에게 실제로 메시지를 보내지 않고 캔버스 단계를 통과할 테스트 사용자 세트를 식별합니다. 테스트 사용자는 Braze 대시보드에서 실제 서비스에 사용되지 않는 기존 이메일 주소이거나, 테스트 목적으로만 사용되는 새 이메일 주소일 수 있습니다.

## 3단계: Canvas 설정 {#step-3-set-up-your-canvas}

다음으로, Canvas를 테스트할 차례입니다! 원본 Canvas와 테스트 Canvas 정보를 체계적으로 관리하기 위해 테스트 목적으로 Canvas의 복제본을 생성하세요.

Canvas를 테스트하는 방법은 두 가지가 있습니다.

- **방법 1:** 복제된 Canvas에서 Canvas 빌더의 **진입 오디언스** 부분을 편집하여 테스트 사용자만 Canvas에 적격하도록 설정합니다. **이메일 주소** 테스트 필터를 추가하여 자신의 이메일 주소를 테스트 사용자로 입력할 수도 있습니다. 다음 섹션의 예시에서는 3일 이내에 앱을 처음 사용한 두 명의 테스트 사용자로 Canvas를 제한했습니다.

![진입 오디언스가 "3일 이내에 이 앱을 처음 사용한 사용자"이고 두 명의 테스트 사용자 이메일 주소가 포함된 Canvas.]({% image_buster /assets/img_archive/canvas_test2.png %}){: style="max-width:90%;"}

- **방법 2:** Canvas 빌더 하단의 **테스트 Canvas** 버튼을 선택하여 [사용자 경로를 미리보기]({{site.baseurl}}/preview_user_paths)합니다.

## 4단계: 테스트 시작 {#step-4-launch-your-test}

테스트 Canvas를 시작하여 사용자가 진입할 수 있도록 합니다. 애플리케이션에서 사용자를 해당 Canvas 여정으로 보내는 사용자 동작을 완료하세요.

테스트 사용자가 캔버스 단계에서 의도한 메시지를 수신하는지 확인합니다. 테스트 사용자가 다음과 같은 이유(이에 국한되지 않음)로 메시지를 수신하지 못할 수 있습니다:

- 글로벌 컨트롤 그룹에 적격하지 않음
- 최대 게재빈도 설정 제한
- Segment 멤버십 불일치
- 중단된 메시지
- 다른 사용자와 연결된 푸시 토큰

Canvas가 의도한 대로 작동하는지 확인하기 위해 Canvas 테스트를 계속 반복하세요.

## 일반 팁 {#general-tips}

### 캔버스 단계 식별 {#identify-your-canvas-steps}

경우에 따라 사용자가 Canvas를 통과하면서 여러 메시지를 수신할 수 있습니다. 테스트를 위해 단계 간 지연 시간을 크게 줄인 경우, 테스트 중에 어떤 메시지가 트리거되는지 항상 명확하지 않을 수 있습니다. 테스트 메시지에 단계 이름이나 사용자 ID(Liquid 사용)를 포함하면 올바른 메시지가 올바른 사용자에게 전송되었는지 식별하고 확인하기가 더 쉬워집니다.

### 내부 그룹 생성 {#create-an-internal-group}

개별 테스트 사용자를 생성하는 대신, [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)을 생성할 수 있습니다. 이는 메시지 콘텐츠를 검토하는 것을 목적으로 하는 내부 그룹입니다. 여기에는 Campaigns와 Canvases에서 테스트 메시지를 수신할 사용자 그룹이 포함됩니다. 그런 다음 **테스트 수신자** 아래의 **콘텐츠 테스트 그룹 추가** 필드에 이 테스트 그룹을 추가할 수 있습니다.

### 시간 지연 줄이기 {#reduce-time-delays}

테스트를 더 효율적으로 실행하려면 테스트 목적으로 시간 지연을 분 또는 초 단위로 줄여 메시지를 적시에 확인할 수 있도록 하는 것이 좋습니다. 예를 들어, 특정 동작을 특정 Canvas 여정에 분리할 수 있도록 테스트 간에 최소 2~3분의 간격을 두세요.

### Content Blocks 활용 {#leverage-content-blocks}

테스트 프레임워크에서 반복되는 콘텐츠가 있는 경우(예: 사용자를 다른 캔버스 단계로 필터링하는 복잡한 Liquid), 이 반복 콘텐츠를 [콘텐츠 블록]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)으로 저장해 보세요. 이제 개별 캔버스 단계 전체에 콘텐츠 블록을 포함할 수 있습니다.

### Postman과 사용자 추적 엔드포인트 사용 {#use-postman-and-the-track-user-endpoint}

Postman과 [Braze Postman 컬렉션]({{site.baseurl}}/api/postman_collection)을 사용하여 테스트를 실행할 수 있습니다. [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 사용하여 다양한 테스트 사용자의 커스텀 이벤트와 구매를 기록하고 추적하세요.

사용자 추적 API로 데이터를 전송하는 것은 외부 ID로만 가능합니다. 따라서 특정 오류를 추가로 조사할 수 있도록 테스트 사용자를 Braze 대시보드의 내부 그룹 내에 테스트 사용자로 추가해야 할 수 있습니다.

#### 다중 분기 테스트 {#testing-for-multiple-branches}

다양한 속성과 이벤트를 기반으로 사용자를 타겟팅하는 여러 분기가 있는 Canvas를 테스트할 때는 다음 테스트 계획을 따르세요:

1. 각 분기에 대해 사용자가 Canvas 여정에 포함되기 위해 가져야 할 속성과 이벤트를 식별합니다.
2. `/users/track` 엔드포인트를 사용하여 게시할 JSON 페이로드에 이를 구축합니다.