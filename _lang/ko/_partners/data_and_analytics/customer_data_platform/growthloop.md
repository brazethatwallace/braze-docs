---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "이 참조 문서에서는 데이터 웨어하우스에서 직접 고객 데이터를 세분화하여 Braze로 전송할 수 있는 플랫폼인 GrowthLoop과 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/)은 마케팅 팀이 클라우드 데이터 웨어하우스에서 고객 데이터를 활성화하여 Braze 및 기타 채널로 전송할 수 있도록 지원합니다. 클라우드 데이터 웨어하우스에서 마케팅 프로그램을 자동화, 확장 및 측정하여 데이터를 하나의 중앙 집중식 위치에 유지합니다.

_이 통합은 GrowthLoop에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 GrowthLoop 통합을 사용하면 데이터 웨어하우스에서 직접 고객 데이터를 세분화하여 Braze로 전송할 수 있으므로, 단일 소스 오브 트루스(Single Source of Truth)와 함께 Braze의 심층 기능 세트를 최적화할 수 있습니다. 고객 세분화 및 활성화를 위한 마케팅 활동을 간소화하여 Braze로 전송되는 타겟팅된 Campaign의 세분화, 시작, 테스트 및 결과 측정에 소요되는 시간을 단축합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| GrowthLoop growth 또는 enterprise 계정 | 이 파트너십을 활용하려면 GrowthLoop 계정이 필요합니다. |
| Braze REST API 키 | 모든 권한이 포함된 Braze REST API 키.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 사용 사례 {#use-cases}

데이터 웨어하우스에서 Braze로 고객 목록을 전송하여 이메일 및 푸시 알림 Campaign을 한 번의 클릭으로 타겟팅하고 항상 동기화 상태를 유지합니다.

- 가입 활성화 기반 이메일 — 가입 플로우에서 이탈한 사용자에게 이메일을 보내 활성 사용자로 전환합니다.
- 사용자 동작 기반 이메일 — "장바구니에 추가"와 같은 사용자 동작을 기반으로 이메일을 전송합니다.
- 이탈 고객 대상 이메일 — 이메일을 통해 이탈 고객에게 오퍼를 제공하여 재참여를 유도합니다.

## 통합 {#integration}

### GrowthLoop에서 Braze 연결 구성 {#configure-braze-connection-in-growthloop}

GrowthLoop 내 세분화 플랫폼에 로그인한 후, 왼쪽 사이드바의 **Destinations** 탭으로 이동하여 오른쪽 상단의 **New Destination**을 클릭합니다.

Braze를 찾을 때까지 스크롤한 다음 **Add Braze**를 클릭합니다.

대상 연결을 구성하기 위한 팝업이 나타납니다.

- **Destination name**: 앱에서 앞으로 대상의 이름으로 지정되고 참조되는 이름입니다.
- **Sync frequency**: Daily 또는 Hourly를 선택합니다. GrowthLoop이 Braze로 오디언스를 내보내는 빈도를 제어합니다.
- **API key**: 필요한 권한이 포함된, 요구 사항에서 생성한 API 키입니다.
- **API URL**: 요구 사항에서 정의한 URL입니다.

**Create**를 클릭하면 첫 번째 오디언스를 Braze로 내보낼 수 있습니다! GrowthLoop에서 오디언스를 생성하려면 [오디언스 생성](https://www.growthloop.com/help-center-articles/create-an-audience)을 참조하세요.

### 내보내기 후 {#post-export}

오디언스가 내보내기되면 GrowthLoop은 15분마다 고객 목록의 업데이트된 버전을 생성하여 Braze로 전송합니다.

동시에 GrowthLoop은 더 이상 자격이 없는 사용자를 오디언스에서 제거하고 새로 자격을 갖춘 사용자를 오디언스에 추가합니다.

Braze는 사용자를 매칭하고 GrowthLoop 오디언스에 속해 있음을 나타내는 플래그를 생성합니다.

Braze에서 Campaign을 생성할 때 해당 GrowthLoop 오디언스의 고객을 선택할 수 있습니다.

## 문제 해결 {#troubleshooting}

추가 정보나 고객지원이 필요한 경우 solutions@growthloop.com으로 GrowthLoop 팀에 문의하세요.