---
nav_title: SmarterSends
article_title: SmarterSends
description: "이 참조 문서에서는 마케터가 아닌 사용자도 브랜드 규정을 준수하는 이메일 캠페인을 쉽게 생성, 예약 및 배포할 수 있도록 설계된 사용하기 쉬운 인터페이스인 SmarterSends와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSends](https://smartersends.com)는 비즈니스가 마케팅 캠페인을 생성, 예약 및 배포하여 사용되는 콘텐츠와 데이터에 대한 제어를 통해 브랜드 및 법적 규정 준수를 시행할 수 있도록 개인화를 지원합니다.

_이 통합은 SmarterSends에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 SmarterSends 파트너십을 통해 Braze의 강력한 기능과 분산된 사용자가 소유한 하이퍼 로컬 콘텐츠를 결합하여 마케팅 캠페인을 한 단계 끌어올릴 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| SmarterSends 계정 | 이 파트너십을 활용하려면 [SmarterSends 계정](https://smartersends.com)이 필요합니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. 추가 보안을 위해 SmarterSends IP 주소를 허용 목록에 추가하세요(인스턴스에서 확인 가능). |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Braze API Campaign ID | [Braze API Campaign ID]({{site.baseurl}}/api/api_campaigns/)는 SmarterSends를 통해 전송되는 모든 Campaign의 고유 식별자입니다. Braze 대시보드의 **메시징** > **Campaigns**에서 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 활용 사례 {#use-cases}

Braze와 SmarterSends 통합을 통해 여러 채널과 위치에서 마케팅 Campaign을 생성하고 실행하여 분산 마케팅을 활용할 수 있습니다. 이러한 이점은 다음과 같습니다.

1. **도달 범위 확대:** 여러 채널과 위치를 활용하여 더 넓은 오디언스에 도달하고 다양한 위치의 고객을 타겟팅하여 브랜드 노출을 높일 수 있습니다.
2. **타겟 메시징:** 채널과 위치에 따라 메시징을 맞춤화하여 현지 오디언스에게 공감을 이끌어내고 고객과의 커뮤니케이션 및 참여를 더욱 효과적으로 만들 수 있습니다.
3. **브랜드 일관성 향상:** 모든 채널과 위치에서 브랜드 메시징과 이미지를 일관되게 유지하여 강력하고 인지도 높은 브랜드를 구축하는 데 도움이 됩니다.
4. **더 나은 인사이트:** 다양한 채널과 위치에서 데이터를 수집하여 고객 행동과 선호도에 대한 귀중한 인사이트를 제공하며, 이를 통해 로컬 및 글로벌 수준에서 마케팅 전략과 전술을 개선할 수 있습니다.
5. **효율성 향상:** 다양한 채널과 위치의 강점을 활용하여 원하는 마케팅 목표를 달성하면서도 리소스를 더 효율적으로 사용할 수 있습니다.

## 통합 {#integration}

### 1단계: REST API 키 생성 {#step-1-create-a-rest-api-key}

1. Braze에서 **설정** > **API 키**로 이동하여 **새 API 키 생성**을 클릭합니다.
2. API 키의 이름을 입력합니다.
3. SmarterSends가 Braze 워크스페이스와 상호 작용할 수 있도록 이 키에 대해 다음 권한을 선택합니다.
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. **IP 허용 목록** 섹션에 SmarterSends IP 주소를 추가합니다.
5. **API 키 저장**을 클릭합니다.
6. 적절한 권한이 있는 API 키를 복사하여 SmarterSends의 **Braze Email Service Provider** 설정에 붙여넣습니다.

### 2단계: 애플리케이션 ID 생성 또는 복사 {#step-2-create-or-copy-an-application-id}

1. Braze 워크스페이스에서 **설정** > **앱 설정**으로 이동합니다.
2. 새 앱을 설정하거나 워크스페이스 내 기존 애플리케이션의 애플리케이션 ID를 사용합니다. 애플리케이션 ID는 **API Key**로 표시됩니다.
3. 이 ID를 복사하여 SmarterSends의 **App ID** 필드에 붙여넣습니다.

### 3단계: API Campaign 생성 {#step-3-create-an-api-campaign}

API Campaign을 사용하면 Braze 내에서 모든 SmarterSends 메일의 측정기준을 추적할 수 있으며, SmarterSends가 이러한 API 기반 Campaign을 트리거할 수 있습니다.

1. Braze에서 [API Campaign을 생성]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign)합니다.
2. **Select Message Channel** 아래의 **Email**을 클릭하여 메시징 채널을 추가하고 측정기준 추적을 시작합니다.
3. 다음으로, Braze의 Campaign ID를 복사하여 SmarterSends의 **Campaign ID** 필드에 붙여넣습니다.
4. Braze의 메시지 배리언트 ID를 복사하여 SmarterSends의 **Message Variant ID** 필드에 붙여넣습니다. 이것은 SmarterSends에서 각 그룹에 대한 메시지 ID를 생성하지 않기로 결정한 경우 사용되는 기본 메시지 ID입니다.
5. SmarterSends에서 생성하는 각 그룹에 대해 Braze의 API Campaign에 메시지 배리언트를 추가합니다. 그런 다음 메시지 배리언트 ID를 SmarterSends의 해당 그룹 메시지 배리언트 ID에 복사합니다.

{% alert tip %}
SmarterSends에서 생성하는 각 그룹에 대해 메시지 배리언트 ID를 생성하면 Braze 워크스페이스에서 각 그룹의 발송 측정기준을 별도로 확인할 수 있습니다. 이는 Braze에서 보고서를 작성할 때 그룹 간 트렌드를 파악하는 데 유용합니다.
{% endalert %}

## 커스터마이징 {#customization}

각 SmarterSends 인스턴스는 브랜드의 로고 색상과 커스텀 도메인 이름으로 완전히 커스터마이징할 수 있어 익숙한 환경을 제공합니다. 또한 추가적인 개인화를 위해 Braze 워크스페이스 내 Segments를 기반으로 Campaign에서 사용자를 타겟팅할 속성 및 커스텀 속성을 정의할 수 있습니다.