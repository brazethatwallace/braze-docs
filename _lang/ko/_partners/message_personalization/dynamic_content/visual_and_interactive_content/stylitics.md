---
nav_title: Stylitics
article_title: Stylitics
description: "이 참조 문서에서는 Braze와 Stylitics 간의 파트너십에 대해 설명합니다. Stylitics는 클라우드 기반 SaaS 플랫폼으로, 기존 이메일 캠페인에 매력적이고 관련성 높은 번들 콘텐츠를 추가하여 개인화된 고객 경험을 만들 수 있습니다."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> [Stylitics](https://stylitics.com/)는 소매업체가 시각적 콘텐츠를 대규모로 자동화하고 배포할 수 있는 클라우드 기반 SaaS 플랫폼입니다. Stylitics 번들은 제품에 상황별 맥락을 부여하여 영감을 주고, 구매 확신을 높이며, 참여를 증가시켜 궁극적으로 평균 주문 금액과 전환율을 향상시킵니다.

_이 통합은 Stylitics에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Stylitics 통합을 사용하면 기존 이메일 캠페인에 매력적이고 관련성 높은 번들 콘텐츠를 추가하여 개인화된 고객 경험을 만들 수 있습니다.

![]({% image_buster /assets/img/stylitics.png %}){: style="max-width:60%;"}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Stylitics 계정 | 이 파트너십을 활용하려면 [Stylitics](https://stylitics.com/) 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

다음은 일반적인 트리거 이메일 프로그램 예시입니다:
- 유기한 장바구니 이메일
- 탐색 중단 이메일
- 배송 확인 이메일
- 구매 후 이메일

## 통합 {#integration}

Stylitics는 이 통합을 위한 번들 데이터를 제공합니다. 이메일 서비스 공급자가 Stylitics 번들을 포함하도록 이메일 템플릿을 생성하거나 업데이트할 수 있습니다. Stylitics는 이메일의 레이아웃이나 디자인을 변경할 수 없습니다.

1. 이메일에 번들을 통합합니다. 이메일 서비스 공급자가 위치와 커스터마이징을 결정합니다.
2. 이메일 서비스 공급자가 Stylitics 콘텐츠를 포함하도록 트리거 이메일 코드를 업데이트합니다.
3. 이메일 서비스 공급자가 업데이트된 트리거 시리즈를 테스트, 미리보기 및 시작합니다.

Stylitics는 아이템에 대한 번들 데이터만 제공합니다. 귀하와 이메일 서비스 공급자 사이에서 사용자 데이터를 보유하고 Stylitics 번들 데이터를 연결하여 사용자에게 전송할 수 있습니다.

## 데이터 교환 {#data-exchange}

다음 세 가지 접근 방식을 통해 트리거 이메일에 Stylitics 번들을 포함할 수 있습니다.

### 1. API 접근 방식(권장) {#1-api-approach-recommended}

귀하 또는 이메일 서비스 공급자가 아이템별로 API 호출을 수행하여 이메일에 번들 데이터를 채울 수 있습니다. Stylitics는 즉시 사용할 수 있는 자체 API를 사용하여 API 호출을 수행할 것을 권장합니다.

{% alert note %}
Stylitics에서 실행하는 A/B 테스트를 진행하는 경우, 사용자가 이메일에서 클릭하는 Stylitics 아이템의 PDP URL에 `styliticsCID` 및 `styliticsoverride` 파라미터를 추가해야 합니다.
<br><br>
예: {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2. 플랫 파일 접근 방식 {#2-flat-file-approach}
귀하 또는 이메일 서비스 공급자가 플랫 파일에서 아이템의 번들 데이터를 참조하여 이메일에 번들 데이터를 채울 수 있습니다. Stylitics는 번들 데이터를 CSV, TXT 또는 XML 형식으로 변환하여 매일 전송할 수 있습니다. 또한 이메일 서비스 공급자의 요구 사항에 맞게 파일 형식을 조정하는 데 도움을 줄 수 있습니다. 이 파일을 생성하는 데 2~3주가 소요됩니다.

#### 요구 사항: {#requirements}
- **위치**: Stylitics가 매일 파일을 Stylitics SFTP에 올려 귀하가 가져갈 수 있도록 하거나, 귀하의 SFTP 자격 증명을 전달하여 파일을 올릴 수 있습니다.
- **시간**: Stylitics는 매일 아침 파일을 올립니다. 파일이 필요한 특정 시간이 있으면 알려주세요.
- **파일 키**: 이메일 서비스 공급자가 데이터를 참조할 수 있도록 파일의 키로 사용할 아이템 데이터 문자열에 대해 귀하와 Stylitics가 합의해야 합니다. SKU, `item_group_id` 또는 `item_number`가 일반적으로 사용됩니다.

### 3. 웹사이트 데이터 추출 접근 방식 {#3-website-data-extraction-approach}
벤더가 귀하의 사이트 프론트엔드에서 Stylitics 콘텐츠를 스크래핑하여 이메일에 번들 데이터를 삽입할 수 있습니다. Stylitics의 추가 작업은 필요하지 않습니다.

## 이메일 템플릿 모범 사례 {#email-template-best-practices}

귀하와 이메일 서비스 공급자가 Stylitics 데이터와 번들을 삽입할 HTML 이메일 템플릿을 생성합니다. 다음은 몇 가지 모범 사례와 권장 사항입니다.
- 사용자가 구매하거나 상호작용한 가장 비싼 아이템 또는 첫 번째 정가 아이템에 대해 이메일에 2~4개의 번들을 표시합니다
- 여러 `item_numbers`를 호출하고 처음 몇 개의 번들 응답을 표시합니다
- 아이템에 사용 가능한 번들이 없는 경우 대체 옵션을 마련합니다
	- Stylitics 번들이 있는 섹션을 숨깁니다
	- 사용자가 조회한 다음 아이템의 번들을 표시합니다
- 사용자가 명확하게 클릭할 수 있도록 번들 이미지와 제품 제목 목록 및 썸네일 이미지를 표시합니다

{% alert note %}
이메일은 JavaScript를 지원하지 않으므로 Stylitics 위젯 JavaScript를 이메일에 삽입할 수 없습니다.
{% endalert %}

## 분석 {#analytics}

Stylitics는 이 유형의 이메일 프로그램에 대한 번들 데이터를 제공합니다. 따라서 귀하, 이메일 서비스 공급자 및 Stylitics 간의 공개 데이터 공유를 요청합니다. 가능하다면 성과 향상을 이해하고 프로그램을 개선하기 위해 다음 측정기준을 제공해 주시기 바랍니다:
- 발송된 이메일 수
- 열린 이메일 수
- 조회 및 참여
- 클릭률
- 장바구니 추가
- 구매

## 다음 단계 {#next-steps}

Stylitics 계정 매니저에게 연락하여 이메일 프로그램의 다음 단계와 일정을 조율하세요. 다음 단계에는 다음이 포함됩니다:
- 사용할 이메일 결정
- 데이터 교환을 논의하기 위해 Stylitics와 이메일 서비스 공급자를 연결하여 API 옵션 또는 플랫 파일 옵션 결정
- 이메일 서비스 공급자와 목업 생성
- 분석 방법 조율
- 출시 일정 조율