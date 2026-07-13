---
nav_title: B.Layer
article_title: B.Layer
description: "이 참조 문서에서는 Braze와 인앱 메시지 빌더인 B.Layer 간의 파트너십을 설명합니다. B.Layer를 사용하면 코딩 없이 간편하고 빠르게 커스텀 디자인 인앱 메시지를 만들 수 있습니다."
alias: /partners/blayer-inapps/
page_type: partner
search_tag: Partner

---

# B.Layer

> [B.Layer](https://blayer.phiture.com)는 Phiture의 인앱 메시지 빌더로, 모바일 앱 CRM 팀이 코딩 없이 간편하고 빠르게 커스텀 디자인 인앱 메시지를 만들 수 있도록 도와줍니다.

_이 통합은 B.Layer에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 B.Layer 통합을 통해 B.Layer 인앱 메시지 빌더를 사용하면 zip 파일 또는 인라인 HTML로 Braze에 내보낼 수 있는 온브랜드 인앱 메시지를 구축할 수 있습니다. 이 통합은 추가 개발자 리소스가 필요하지 않으므로 시간과 비용을 절약할 수 있습니다.

![브랜드 인앱 메시지를 미리 보여주는 B.Layer 빌더 인터페이스]({% image_buster /assets/img/blayer/blayer2.png %})

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| B.Layer 계정 | 이 파트너십을 활용하려면 [B.Layer](https://blayer.phiture.com) 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 사용 사례 {#use-cases}

B.Layer를 사용하면 제품 추천 슬라이더, 멀티 스크린 온보딩 또는 설문조사, 순고객추천지수, 이메일 수집, 특별 혜택 등 무한한 가능성을 구축하고 실험할 수 있습니다.

B.Layer는 Lifesum, Blinkist, OnX Hunt 등 다양한 브랜드와 협력하여 추가 리소스 없이 사용자 경험을 개선하도록 돕고 있습니다. 또한 APS Awards 2022 앱 혁신 부문 최종 후보에 선정되기도 했습니다.

## 통합 {#integration}

### 1단계: 인앱 메시지 만들기 {#step-1-create-your-in-app-message}

#### 브랜드 색상 및 글꼴 설정 {#set-brand-colors-and-fonts}

B.Layer에서 페이지 상단의 햄버거 메뉴를 클릭한 다음 **Brand assets > add your brand assets**를 클릭합니다. 여기에서 브랜드 색상과 글꼴을 할당할 수 있습니다.
이제 준비가 완료되었습니다. 인앱 메시지 디자인을 시작할 수 있습니다.

![색상 및 글꼴을 구성하는 B.Layer 브랜드 에셋 화면]({% image_buster /assets/img/blayer/blayer4.png %})

#### 인앱 메시지 디자인 {#design-your-in-app-message}

인앱 메시지를 디자인하려면 단일 인앱 메시지를 선택합니다. 그런 다음 메시지 스타일을 지정하고 필요한 구성요소를 추가합니다. 각 구성요소는 조정할 수 있습니다.

![구성요소 및 스타일 컨트롤이 있는 B.Layer 메시지 편집기]({% image_buster /assets/img/blayer/blayer5.png %})

### 인앱 메시지 다운로드 {#download-your-in-app-message}

완료되면 메시지를 다운로드합니다. 메시지는 ZIP 또는 인라인 HTML로 다운로드할 수 있습니다.

### 2단계: B.Layer 커스텀 코드 추가 {#step-2-add-blayer-custom-code}

Braze에서 사용자 지정 코드 인앱 메시지를 생성합니다. ZIP 파일이 있는 경우 이 섹션의 업로드 상자에 드래그 앤 드롭합니다. 인라인 HTML 파일이 있는 경우 인라인 HTML을 HTML 섹션에 붙여넣습니다.

![B.Layer 내보내기 콘텐츠가 포함된 Braze 사용자 지정 코드 인앱 메시지 편집기]({% image_buster /assets/img/blayer/blayer6.png %})

## 버튼 추적 {#button-tracking}

B.Layer를 사용하면 버튼 상호작용이나 텍스트 입력을 Braze 속성으로 기록할 수 있습니다. 이 작업은 편집기 내에서 수행할 수 있습니다. 대표적인 예로 순고객추천지수 설문조사가 있습니다.

B.Layer는 입력한 링크에 추가된 Braze 버튼 추적을 사용합니다(예: `?button=0`). 이를 통해 Campaign의 분석 섹션에서 버튼 클릭 수를 확인할 수 있습니다.