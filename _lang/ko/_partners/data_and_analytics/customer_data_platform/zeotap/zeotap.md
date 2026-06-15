---
nav_title: Zeotap
description: "이 참조 문서에서는 ID 확인, 인사이트, 데이터 보강을 제공하는 차세대 고객 데이터 플랫폼인 Zeotap과 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/)은 ID 확인, 인사이트, 데이터 보강을 제공하여 모바일 오디언스를 발견하고 이해할 수 있도록 돕는 차세대 고객 데이터 플랫폼입니다.

Zeotap과 Braze 통합을 사용하면 Zeotap 고객 세그먼트를 동기화하여 사용자 데이터를 Braze 사용자 계정에 매핑함으로써 캠페인의 규모와 도달 범위를 확장할 수 있습니다. 이 데이터를 기반으로 사용자에게 개인화된 타겟 경험을 제공할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Zeotap 계정 | 이 파트너십을 활용하려면 [Zeotap 계정](https://zeotap.com/)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL입니다. 엔드포인트는 [인스턴스에 대한 Braze URL]({% image_buster /assets/img/zeotap/zeotap1.png %})에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Zeotap 대상 생성 {#step-1-create-a-zeotap-destination}

1. Zeotap Unity 플랫폼에서 **DESTINATIONS** 애플리케이션으로 이동합니다.
2. **All Channels** 아래에서 **Braze**를 선택합니다.
3. 표시되는 프롬프트에서 대상 이름을 지정하고, Braze 계정과 연결된 클라이언트 이름과 Braze REST API 키를 입력합니다.
4. 마지막으로 드롭다운에서 Braze REST 엔드포인트 인스턴스를 선택하고 대상을 저장합니다. <br><br>![]({% image_buster /assets/img/zeotap/zeotap1.png %})

### 2단계: Zeotap 세그먼트를 생성하고 대상에 연결 {#step-2-create-and-link-a-zeotap-segment-to-your-destination}

1. Zeotap Unity 플랫폼에서 **CONNECT** 애플리케이션으로 이동합니다.
2. 세그먼트를 생성하고 1단계에서 만든 Braze 대상을 선택합니다.
3. 지원되는 출력 식별자를 선택합니다: MAID, SHA256으로 해시된 이메일 주소, 또는 Braze에서 인식하는 1P 고객 식별자(Braze 계정에 커스텀 식별자를 사용하려면 Zeotap에 문의하여 계정에서 활성화할 수 있도록 하세요). Braze 통합에는 하나의 출력 식별자만 사용할 수 있습니다. 이러한 식별자는 Braze SDK 데이터를 수집할 때 설정한 외부 ID와 동일해야 합니다.
4. 세그먼트를 저장합니다.

![]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
표시되는 식별자는 세그먼트에서 사용 가능하며 Braze에서 지원하는 식별자입니다.
{% endalert %}

### 3단계: Braze 세그먼트 생성 {#step-3-create-braze-segment}

Zeotap에서 세그먼트를 성공적으로 생성, 푸시 및 처리하면 Zeotap 사용자가 Braze 대시보드에 표시됩니다. Braze 대시보드에서 사용자 ID로 사용자를 조회할 수 있습니다.

![커스텀 속성 아래에 세그먼트 1~4가 "true"로 나열된 Braze 고객 프로필]({% image_buster /assets/img/zeotap/zeotap4.png %})

사용자가 Zeotap 세그먼트의 일부인 경우 세그먼트 이름이 고객 프로필에 커스텀 속성으로 표시되며 부울 값 `true`가 표시됩니다. Braze 세그먼트를 생성할 때 필요하므로 커스텀 속성 이름을 기록해 두세요.

다음으로 Braze 내에서 이 세그먼트를 생성하고 정의해야 합니다:
1. Braze 대시보드에서 **Segments**를 선택한 다음 **Create Segment**를 선택합니다.
2. 세그먼트 이름을 지정하고 Zeotap에서 만든 커스텀 속성 세그먼트를 선택합니다.
3. 변경 사항을 저장합니다.

![Braze 세그먼트 빌더에서 커스텀 속성으로 설정된 가져온 세그먼트를 찾을 수 있습니다.]({% image_buster /assets/img/zeotap/zeotap3.png %})

이제 새로 생성한 세그먼트를 향후 Braze Campaigns 및 Canvases에 추가하여 이러한 최종 사용자를 타겟팅할 수 있습니다.